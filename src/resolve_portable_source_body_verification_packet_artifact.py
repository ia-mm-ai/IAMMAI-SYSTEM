"""Bounded portable source-body verification packet artifact resolver.

This module records at most one local packet-artifact posture downstream of the
clean packet-boundary basis. Packet artifact remains local artifact posture
only. It is not packet emission, packet transfer, copying to another device,
source transfer, source receipt, second-carrier execution, second-carrier
receipt, external result, cross-carrier evidence, runtime, source, authority,
currentness, final completion, continuation, reusable permission, derivative
reception, vessel relation, another reception request, or follow-on work.

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


class PortableSourceBodyVerificationPacketArtifactError(Exception):
    """Raised for explicit unreadable path or malformed JSON path inputs."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_packet_artifact"
RESULT_TYPE = "portable_source_body_verification_packet_artifact_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_packet_artifact"
)

CORE_QUESTION = (
    "Can the recorded packet-boundary basis be used to define one local "
    "portable verification packet artifact without emitting it, transferring "
    "it, copying it to another carrier, treating it as source, authority, "
    "currentness, final completion, runtime, cross-carrier proof, continuation, "
    "reusable permission, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

PACKET_BOUNDARY_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
COMMAND_SUCCESS_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)

SUPPORTED_PACKET_ARTIFACT_SCOPE = (
    "PACKET_ARTIFACT_SPEC_ONLY",
    "ONE_LOCAL_PACKET_ARTIFACT_RECORDED",
    "PACKET_BOUNDARY_BASIS_PRESERVED",
    "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED",
    "COPYABLE_PACKET_SHAPE_DECLARED",
    "SELECTED_PACKET_BASIS_DECLARED",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_PACKET_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_PACKET_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "PACKET_ARTIFACT_NOT_SOURCE",
    "PACKET_ARTIFACT_NOT_AUTHORITY",
    "PACKET_ARTIFACT_NOT_CURRENTNESS",
    "PACKET_ARTIFACT_NOT_FINAL_COMPLETION",
    "PACKET_ARTIFACT_NOT_RUNTIME",
    "PACKET_ARTIFACT_NOT_CROSS_CARRIER_PROOF",
    "PACKET_NOT_EMITTED",
    "PACKET_NOT_TRANSFERRED",
    "PACKET_EMISSION_NOT_PERFORMED",
    "PACKET_TRANSFER_NOT_AUTHORIZED",
    "SOURCE_TRANSFER_NOT_AUTHORIZED",
    "SOURCE_RECEIPT_NOT_CREATED",
    "RECEPTION_AUTHORIZATION_NOT_CREATED",
    "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED",
    "SECOND_CARRIER_RECEIPT_NOT_CREATED",
    "EXTERNAL_RESULT_NOT_CREATED",
    "CROSS_CARRIER_EVIDENCE_NOT_CREATED",
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
)

POSTURE_KEYS = (
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
)

REQUIRED_FALSE_NON_CLAIMS = (
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
    "artifact_existence_treated_as_packet_authority",
    "artifact_path_treated_as_currentness",
    "repo_local_availability_treated_as_packet_authority",
    "hidden_repo_state_used_as_packet_content",
    "hidden_repo_state_used_as_packet_authority",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
)

EXTRA_FALSE_NON_CLAIMS = (
    "packet_boundary_already_created_packet",
    "packet_boundary_already_emitted_packet",
    "packet_boundary_authorized_transfer",
    "packet_boundary_authorized_second_carrier_execution",
    "packet_boundary_created_cross_carrier_evidence",
    "packet_boundary_used_hidden_repo_state_as_packet_authority",
    "packet_boundary_returned_raw_full_prior_artifact_body",
    "command_success_treated_as_packet_permission",
    "full_prior_artifact_body_emitted",
    "predecessor_failures_repaired",
    "predecessor_failures_hidden",
    "predecessor_failures_claimed_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
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

PUBLIC_BLOCK_CODES = frozenset(
    {
        "DECLARED_PACKET_ARTIFACT_REQUEST_MALFORMED",
        "DECLARED_PACKET_ARTIFACT_REQUEST_UNREADABLE",
        "PACKET_ARTIFACT_QUESTION_UNDECLARED",
        "PACKET_ARTIFACT_INTENT_UNSUPPORTED",
        "PACKET_ARTIFACT_EXPLICIT_BLOCK_INTENT",
        "PACKET_BOUNDARY_BASIS_MISSING",
        "PACKET_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING",
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
        "COMMAND_SUCCESS_TERMINAL_SUMMARY_BASIS_MISSING",
        "COMMAND_SUCCESS_NOT_RECORDED",
        "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
        "COMMAND_SUCCESS_TREATED_AS_PACKET_PERMISSION",
        "COMMAND_RESULT_V2_BASIS_MISSING",
        "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "COMMAND_EXECUTION_BASIS_MISSING",
        "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "PREDECESSOR_FAILURE_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "ARTIFACT_CONTAINMENT_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "COMMAND_RESULT_V2_NOT_RECORDED",
        "OUTPUT_CAPTURE_V2_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        "EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "COMMAND_REPORT_LINEAGE_NOT_LINEAGE_ONLY",
        "PREDECESSOR_FAILURE_EVIDENCE_NOT_VISIBLE",
        "PACKET_ARTIFACT_SPEC_ONLY_POSTURE_MISSING",
        "ONE_LOCAL_PACKET_ARTIFACT_POSTURE_MISSING",
        "PACKET_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
        "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED_POSTURE_MISSING",
        "COPYABLE_PACKET_SHAPE_DECLARED_POSTURE_MISSING",
        "SELECTED_PACKET_BASIS_DECLARED_POSTURE_MISSING",
        "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
        "REPO_LOCAL_AVAILABILITY_NOT_PACKET_AUTHORITY_POSTURE_MISSING",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "PACKET_NOT_EMITTED_POSTURE_MISSING",
        "PACKET_NOT_TRANSFERRED_POSTURE_MISSING",
        "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
        "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
        "NO_SOURCE_AUTHORITY_CURRENTNESS_FINAL_COMPLETION_RUNTIME_FOLLOW_ON_POSTURE_MISSING",
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
        "DERIVATIVE_RECEPTION_AUTHORIZED",
        "VESSEL_RELATION_AUTHORIZED",
        "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        "FOLLOW_ON_WORK_AUTHORIZED",
        "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY",
        "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_PACKET_AUTHORITY",
        "HIDDEN_REPO_STATE_USED_AS_PACKET_CONTENT",
        "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "ARTIFACTS_MUTATED",
        "MUTATION_PERFORMED",
        "REPLAY_PERFORMED",
        "MERGE_PERFORMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_PACKET_ARTIFACT_SCOPE",
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
        "raw_packet_body",
        "raw_packet_artifact_body",
        "packet_body",
        "packet_artifact_body",
        "packet_payload",
        "source_body",
        "source_body_packet",
        "authority_body",
        "currentness_claim",
        "final_completion_claim",
        "raw_command_success_body",
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
        "external_result_body",
        "cross_carrier_evidence_body",
        "hidden_repo_state",
        "current_working_tree",
        "local_cache",
        "unlisted_file_dependency",
    }
)
RAW_SENTINELS = (
    "RAW_PACKET_ARTIFACT_BODY_MUST_NOT_RETURN",
    "RAW_PACKET_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMMAND_SUCCESS_BODY_MUST_NOT_RETURN",
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
    for container_key in (
        "metadata",
        "summary",
        "packet_boundary_statement",
        "packet_artifact_statement",
        "command_success_statement",
        "non_claims",
    ):
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
    value = request.get("packet_artifact_scope", [])
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
    section.setdefault("hidden_repo_state_used_as_packet_content", False)
    section.setdefault("hidden_repo_state_used_as_packet_authority", False)
    section.setdefault("repo_local_availability_treated_as_packet_authority", False)
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
    section.setdefault("packet_artifact_posture_only", True)
    section.setdefault("recorded_outcome_only", recorded)
    section.setdefault("packet_emitted", False)
    section.setdefault("packet_transferred", False)
    section.setdefault("packet_copied_to_another_device", False)
    section.setdefault("source_transfer_occurred", False)
    section.setdefault("source_receipt_occurred", False)
    section.setdefault("reception_authorization_created", False)
    section.setdefault("second_carrier_execution_created", False)
    section.setdefault("second_carrier_receipt_created", False)
    section.setdefault("external_result_created", False)
    section.setdefault("cross_carrier_evidence_created", False)
    section.setdefault("source_created", False)
    section.setdefault("authority_created", False)
    section.setdefault("currentness_created", False)
    section.setdefault("final_completion_claimed", False)
    section.setdefault("runtime_hosting_created", False)
    section.setdefault("follow_on_work_authorized", False)
    section.setdefault("hidden_repo_state_used_as_packet_authority", False)
    section.setdefault("repo_local_availability_treated_as_packet_authority", False)
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
            (
                "reference_shaped",
                "selected_basis_reference_shape_preserved",
                "basis_remains_reference_shaped",
            ),
            default=True,
        ) is False:
            return False
    return True


def _all_raw_full_prior_body_not_returned(request: Mapping[str, Any]) -> bool:
    for key in SELECTED_BASIS_KEYS:
        if _value(
            request,
            key,
            (
                "raw_full_prior_artifact_body_returned",
                "full_prior_artifact_body_emitted",
                "full_prior_artifacts_embedded",
            ),
            default=False,
        ) is True:
            return False
    return True


def _hidden_repo_state_excluded(request: Mapping[str, Any]) -> bool:
    if request.get("hidden_repo_state_used_as_packet_authority") is True:
        return False
    if request.get("hidden_repo_state_used_as_packet_content") is True:
        return False
    for key in SELECTED_BASIS_KEYS:
        if _value(
            request,
            key,
            ("hidden_repo_state_used_as_packet_authority", "hidden_repo_state_used_as_packet_content"),
            default=False,
        ) is True:
            return False
    return (
        _value(
            request,
            "hidden_repo_state_excluded_posture",
            ("hidden_repo_state_used_as_packet_content",),
            default=False,
        )
        is False
        and _value(
            request,
            "hidden_repo_state_excluded_posture",
            ("hidden_repo_state_used_as_packet_authority",),
            default=False,
        )
        is False
    )


def _build_checks(request: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(request, Mapping):
        return [
            _check(
                "declared packet artifact request is mapping",
                False,
                "JSON object mapping",
                type(request).__name__,
                "DECLARED_PACKET_ARTIFACT_REQUEST_MALFORMED",
            )
        ]

    packet_boundary = "selected_packet_boundary_basis"
    packet_boundary_summary = "selected_packet_boundary_terminal_summary_basis"
    command_success = "selected_command_success_basis"
    command_success_summary = "selected_command_success_terminal_summary_basis"
    result_v2 = "selected_command_result_v2_basis"
    capture_v2 = "selected_output_capture_v2_basis"
    report_artifact = "selected_command_output_report_artifact_basis"
    execution = "selected_command_execution_basis"
    lineage = "selected_command_report_lineage_basis"
    predecessor = "selected_predecessor_failure_basis"
    evidence = "selected_evidence_manifest_basis"
    containment = "selected_artifact_containment_basis"
    portable = "selected_portable_verification_basis"
    checks: list[dict[str, Any]] = []

    checks.append(
        _check(
            "packet artifact question declared",
            request.get("packet_artifact_question") == CORE_QUESTION,
            CORE_QUESTION,
            request.get("packet_artifact_question"),
            "PACKET_ARTIFACT_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "packet artifact intent supported",
            request.get("packet_artifact_intent") in SUPPORTED_INTENTS,
            str(SUPPORTED_INTENTS),
            request.get("packet_artifact_intent"),
            "PACKET_ARTIFACT_INTENT_UNSUPPORTED",
        )
    )
    if request.get("packet_artifact_intent") == INTENT_BLOCK:
        checks.append(
            _check(
                "packet artifact explicit block intent absent",
                False,
                "record or do-not-record intent",
                request.get("packet_artifact_intent"),
                "PACKET_ARTIFACT_EXPLICIT_BLOCK_INTENT",
            )
        )

    unsupported_scope = [
        value for value in _scope_values(request) if value not in SUPPORTED_PACKET_ARTIFACT_SCOPE
    ]
    checks.append(
        _check(
            "packet artifact scope supported",
            bool(_scope_values(request)) and not unsupported_scope,
            "supported packet artifact scope values only",
            {"values": _scope_values(request), "unsupported": unsupported_scope},
            "UNSUPPORTED_PACKET_ARTIFACT_SCOPE",
        )
    )

    declared_basis_codes = (
        (packet_boundary, "PACKET_BOUNDARY_BASIS_MISSING"),
        (packet_boundary_summary, "PACKET_BOUNDARY_TERMINAL_SUMMARY_BASIS_MISSING"),
        (command_success, "COMMAND_SUCCESS_BASIS_MISSING"),
        (command_success_summary, "COMMAND_SUCCESS_TERMINAL_SUMMARY_BASIS_MISSING"),
        (result_v2, "COMMAND_RESULT_V2_BASIS_MISSING"),
        (capture_v2, "OUTPUT_CAPTURE_V2_BASIS_MISSING"),
        (report_artifact, "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"),
        (execution, "COMMAND_EXECUTION_BASIS_MISSING"),
        (lineage, "COMMAND_REPORT_LINEAGE_BASIS_MISSING"),
        (predecessor, "PREDECESSOR_FAILURE_BASIS_MISSING"),
        (evidence, "EVIDENCE_MANIFEST_BASIS_MISSING"),
        (containment, "ARTIFACT_CONTAINMENT_BASIS_MISSING"),
        (portable, "PORTABLE_VERIFICATION_BASIS_MISSING"),
    )
    for key, code in declared_basis_codes:
        checks.append(
            _check(
                f"{key} declared",
                _basis_declared(request, key),
                f"{key} declared as bounded reference-shaped basis only",
                request.get(key),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "packet boundary outcome recorded",
                _value(
                    request,
                    packet_boundary,
                    ("outcome", "result_outcome"),
                    ("selected_packet_boundary_result_outcome",),
                )
                == PACKET_BOUNDARY_RECORDED,
                PACKET_BOUNDARY_RECORDED,
                _value(
                    request,
                    packet_boundary,
                    ("outcome", "result_outcome"),
                    ("selected_packet_boundary_result_outcome",),
                ),
                "PACKET_BOUNDARY_NOT_RECORDED",
            ),
            _check(
                "packet boundary version 0.1.0",
                _value(
                    request,
                    packet_boundary,
                    ("result_version", "version"),
                    ("selected_packet_boundary_result_version",),
                )
                == "0.1.0",
                "0.1.0",
                _value(
                    request,
                    packet_boundary,
                    ("result_version", "version"),
                    ("selected_packet_boundary_result_version",),
                ),
                "PACKET_BOUNDARY_VERSION_NOT_0_1_0",
            ),
            _check(
                "packet boundary failed check count zero",
                _as_int(
                    _value(
                        request,
                        packet_boundary,
                        ("failed_check_count",),
                        ("selected_packet_boundary_failed_check_count",),
                    )
                )
                == 0,
                "0",
                _value(
                    request,
                    packet_boundary,
                    ("failed_check_count",),
                    ("selected_packet_boundary_failed_check_count",),
                ),
                "PACKET_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "packet boundary declared future packet step",
                _true(
                    request,
                    packet_boundary,
                    ("one_future_packet_step_declared", "declared_future_packet_step"),
                    ("selected_packet_boundary_declared_future_packet_step",),
                ),
                "one future packet step declared",
                _value(
                    request,
                    packet_boundary,
                    ("one_future_packet_step_declared", "declared_future_packet_step"),
                    ("selected_packet_boundary_declared_future_packet_step",),
                ),
                "PACKET_BOUNDARY_DID_NOT_DECLARE_FUTURE_PACKET_STEP",
            ),
            _check(
                "packet boundary did not create packet",
                _false(
                    request,
                    packet_boundary,
                    ("packet_created", "packet_boundary_already_created_packet"),
                    ("selected_packet_boundary_packet_created",),
                ),
                "packet created false",
                _value(
                    request,
                    packet_boundary,
                    ("packet_created", "packet_boundary_already_created_packet"),
                    ("selected_packet_boundary_packet_created",),
                    False,
                ),
                "PACKET_BOUNDARY_ALREADY_CREATED_PACKET",
            ),
            _check(
                "packet boundary did not emit packet",
                _false(
                    request,
                    packet_boundary,
                    ("packet_emitted", "packet_boundary_already_emitted_packet"),
                    ("selected_packet_boundary_packet_emitted",),
                ),
                "packet emitted false",
                _value(
                    request,
                    packet_boundary,
                    ("packet_emitted", "packet_boundary_already_emitted_packet"),
                    ("selected_packet_boundary_packet_emitted",),
                    False,
                ),
                "PACKET_BOUNDARY_ALREADY_EMITTED_PACKET",
            ),
            _check(
                "packet boundary did not authorize transfer",
                _false(
                    request,
                    packet_boundary,
                    ("packet_boundary_authorized_transfer", "authorized_transfer"),
                    ("selected_packet_boundary_authorized_transfer",),
                ),
                "packet boundary authorized transfer false",
                _value(
                    request,
                    packet_boundary,
                    ("packet_boundary_authorized_transfer", "authorized_transfer"),
                    ("selected_packet_boundary_authorized_transfer",),
                    False,
                ),
                "PACKET_BOUNDARY_AUTHORIZED_TRANSFER",
            ),
            _check(
                "packet boundary did not authorize second-carrier execution",
                _false(
                    request,
                    packet_boundary,
                    (
                        "packet_boundary_authorized_second_carrier_execution",
                        "authorized_second_carrier_execution",
                    ),
                    ("selected_packet_boundary_authorized_second_carrier_execution",),
                ),
                "second-carrier execution authorization false",
                _value(
                    request,
                    packet_boundary,
                    (
                        "packet_boundary_authorized_second_carrier_execution",
                        "authorized_second_carrier_execution",
                    ),
                    ("selected_packet_boundary_authorized_second_carrier_execution",),
                    False,
                ),
                "PACKET_BOUNDARY_AUTHORIZED_SECOND_CARRIER_EXECUTION",
            ),
            _check(
                "packet boundary did not create cross-carrier evidence",
                _false(
                    request,
                    packet_boundary,
                    (
                        "cross_carrier_evidence_created",
                        "packet_boundary_created_cross_carrier_evidence",
                    ),
                    ("selected_packet_boundary_created_cross_carrier_evidence",),
                ),
                "cross-carrier evidence created false",
                _value(
                    request,
                    packet_boundary,
                    (
                        "cross_carrier_evidence_created",
                        "packet_boundary_created_cross_carrier_evidence",
                    ),
                    ("selected_packet_boundary_created_cross_carrier_evidence",),
                    False,
                ),
                "PACKET_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            _check(
                "packet boundary did not use hidden repo state as packet authority",
                _false(
                    request,
                    packet_boundary,
                    ("hidden_repo_state_used_as_packet_authority",),
                    ("selected_packet_boundary_used_hidden_repo_state_as_packet_authority",),
                ),
                "hidden repo state used as packet authority false",
                _value(
                    request,
                    packet_boundary,
                    ("hidden_repo_state_used_as_packet_authority",),
                    ("selected_packet_boundary_used_hidden_repo_state_as_packet_authority",),
                    False,
                ),
                "PACKET_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_PACKET_AUTHORITY",
            ),
            _check(
                "packet boundary did not return raw full prior artifact body",
                _false(
                    request,
                    packet_boundary,
                    ("raw_full_prior_artifact_body_returned",),
                    ("selected_packet_boundary_raw_full_prior_artifact_body_returned",),
                ),
                "raw full prior artifact body returned false",
                _value(
                    request,
                    packet_boundary,
                    ("raw_full_prior_artifact_body_returned",),
                    ("selected_packet_boundary_raw_full_prior_artifact_body_returned",),
                    False,
                ),
                "PACKET_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
            ),
            _check(
                "command success outcome recorded",
                _value(
                    request,
                    command_success,
                    ("outcome", "result_outcome"),
                    ("selected_command_success_result_outcome",),
                )
                == COMMAND_SUCCESS_RECORDED,
                COMMAND_SUCCESS_RECORDED,
                _value(
                    request,
                    command_success,
                    ("outcome", "result_outcome"),
                    ("selected_command_success_result_outcome",),
                ),
                "COMMAND_SUCCESS_NOT_RECORDED",
            ),
            _check(
                "command success failed check count zero",
                _as_int(
                    _value(
                        request,
                        command_success,
                        ("failed_check_count",),
                        ("selected_command_success_failed_check_count",),
                    )
                )
                == 0,
                "0",
                _value(
                    request,
                    command_success,
                    ("failed_check_count",),
                    ("selected_command_success_failed_check_count",),
                ),
                "COMMAND_SUCCESS_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "command success not packet permission",
                _false(
                    request,
                    command_success,
                    ("command_success_treated_as_packet_permission",),
                    ("selected_command_success_treated_as_packet_permission",),
                ),
                "command success treated as packet permission false",
                _value(
                    request,
                    command_success,
                    ("command_success_treated_as_packet_permission",),
                    ("selected_command_success_treated_as_packet_permission",),
                    False,
                ),
                "COMMAND_SUCCESS_TREATED_AS_PACKET_PERMISSION",
            ),
            _check(
                "command result v2 basis recorded if outcome supplied",
                _value(request, result_v2, ("outcome", "result_outcome"))
                in (None, COMMAND_RESULT_V2_RECORDED),
                COMMAND_RESULT_V2_RECORDED,
                _value(request, result_v2, ("outcome", "result_outcome")),
                "COMMAND_RESULT_V2_NOT_RECORDED",
            ),
            _check(
                "output capture v2 basis recorded if outcome supplied",
                _value(request, capture_v2, ("outcome", "result_outcome"))
                in (None, OUTPUT_CAPTURE_V2_RECORDED),
                OUTPUT_CAPTURE_V2_RECORDED,
                _value(request, capture_v2, ("outcome", "result_outcome")),
                "OUTPUT_CAPTURE_V2_NOT_RECORDED",
            ),
            _check(
                "command output/report artifact basis recorded if outcome supplied",
                _value(request, report_artifact, ("outcome", "result_outcome"))
                in (None, OUTPUT_REPORT_ARTIFACT_RECORDED),
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
                or _true(request, command_success, ("execution_trace_audit_only_preserved",)),
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
        ("command_report_lineage_treated_as_current_report_artifact", "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
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

    posture_codes = {
        "packet_artifact_spec_only_posture": "PACKET_ARTIFACT_SPEC_ONLY_POSTURE_MISSING",
        "one_local_packet_artifact_posture": "ONE_LOCAL_PACKET_ARTIFACT_POSTURE_MISSING",
        "packet_boundary_basis_preserved_posture": "PACKET_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
        "local_command_success_basis_preserved_posture": "LOCAL_COMMAND_SUCCESS_BASIS_PRESERVED_POSTURE_MISSING",
        "copyable_packet_shape_declared_posture": "COPYABLE_PACKET_SHAPE_DECLARED_POSTURE_MISSING",
        "selected_packet_basis_declared_posture": "SELECTED_PACKET_BASIS_DECLARED_POSTURE_MISSING",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "hidden_repo_state_excluded_posture": "HIDDEN_REPO_STATE_EXCLUDED_POSTURE_MISSING",
        "repo_local_availability_not_packet_authority_posture": "REPO_LOCAL_AVAILABILITY_NOT_PACKET_AUTHORITY_POSTURE_MISSING",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "packet_not_emitted_posture": "PACKET_NOT_EMITTED_POSTURE_MISSING",
        "packet_not_transferred_posture": "PACKET_NOT_TRANSFERRED_POSTURE_MISSING",
        "second_carrier_execution_not_authorized_posture": "SECOND_CARRIER_EXECUTION_NOT_AUTHORIZED_POSTURE_MISSING",
        "second_carrier_receipt_not_created_posture": "SECOND_CARRIER_RECEIPT_NOT_CREATED_POSTURE_MISSING",
        "external_result_not_created_posture": "EXTERNAL_RESULT_NOT_CREATED_POSTURE_MISSING",
        "cross_carrier_evidence_not_created_posture": "CROSS_CARRIER_EVIDENCE_NOT_CREATED_POSTURE_MISSING",
    }
    for key, code in posture_codes.items():
        checks.append(
            _check(f"{key} declared", _declared(request.get(key)), f"{key} declared", request.get(key), code)
        )

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

    for key in (evidence, containment, portable):
        checks.append(
            _check(
                f"{key} declared as selected upstream basis",
                _basis_declared(request, key),
                f"{key} declared",
                request.get(key),
                {
                    evidence: "EVIDENCE_MANIFEST_BASIS_MISSING",
                    containment: "ARTIFACT_CONTAINMENT_BASIS_MISSING",
                    portable: "PORTABLE_VERIFICATION_BASIS_MISSING",
                }[key],
            )
        )

    for posture_key, field, code in (
        ("packet_not_emitted_posture", "packet_emitted", "PACKET_EMITTED"),
        ("packet_not_transferred_posture", "packet_transferred", "PACKET_TRANSFERRED"),
        ("second_carrier_execution_not_authorized_posture", "second_carrier_execution_created", "SECOND_CARRIER_EXECUTION_CREATED"),
        ("second_carrier_receipt_not_created_posture", "second_carrier_receipt_created", "SECOND_CARRIER_RECEIPT_CREATED"),
        ("external_result_not_created_posture", "external_result_created", "EXTERNAL_RESULT_CREATED"),
        ("cross_carrier_evidence_not_created_posture", "cross_carrier_evidence_created", "CROSS_CARRIER_EVIDENCE_CREATED"),
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
                {
                    key: _value(
                        request,
                        key,
                        ("reference_shaped", "selected_basis_reference_shape_preserved"),
                        default=True,
                    )
                    for key in SELECTED_BASIS_KEYS
                },
                "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
            ),
            _check(
                "raw full prior artifact body not returned",
                _all_raw_full_prior_body_not_returned(request),
                "raw full prior artifact body returned false",
                {
                    key: _value(
                        request,
                        key,
                        (
                            "raw_full_prior_artifact_body_returned",
                            "full_prior_artifact_body_emitted",
                            "full_prior_artifacts_embedded",
                        ),
                        default=False,
                    )
                    for key in SELECTED_BASIS_KEYS
                },
                "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
            ),
            _check(
                "hidden repo state excluded",
                _hidden_repo_state_excluded(request),
                "hidden repo state excluded and not used as packet authority",
                {
                    "hidden_repo_state_used_as_packet_authority": request.get(
                        "hidden_repo_state_used_as_packet_authority"
                    ),
                    "hidden_repo_state_used_as_packet_content": request.get(
                        "hidden_repo_state_used_as_packet_content"
                    ),
                },
                "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
            ),
            _check(
                "repo-local availability not packet authority",
                _value(
                    request,
                    "repo_local_availability_not_packet_authority_posture",
                    ("repo_local_availability_treated_as_packet_authority",),
                    ("repo_local_availability_treated_as_packet_authority",),
                    False,
                )
                is False,
                "repo-local availability treated as packet authority false",
                _value(
                    request,
                    "repo_local_availability_not_packet_authority_posture",
                    ("repo_local_availability_treated_as_packet_authority",),
                    ("repo_local_availability_treated_as_packet_authority",),
                    False,
                ),
                "REPO_LOCAL_AVAILABILITY_TREATED_AS_PACKET_AUTHORITY",
            ),
        ]
    )

    non_claims = _non_claims_from_request(request)
    checks.append(
        _check(
            "required non-claims remain false",
            _non_claims_false(request),
            "all required non-claims explicit and false",
            {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    non_claim_code_map = {
        "packet_emitted": "PACKET_EMITTED",
        "packet_transferred": "PACKET_TRANSFERRED",
        "packet_copied_to_another_device": "PACKET_COPIED_TO_ANOTHER_DEVICE",
        "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
        "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
        "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
        "second_carrier_execution_created": "SECOND_CARRIER_EXECUTION_CREATED",
        "second_carrier_receipt_created": "SECOND_CARRIER_RECEIPT_CREATED",
        "external_result_created": "EXTERNAL_RESULT_CREATED",
        "cross_carrier_evidence_created": "CROSS_CARRIER_EVIDENCE_CREATED",
        "manifest_created_without_bounded_admission": "MANIFEST_CREATED_WITHOUT_BOUNDED_ADMISSION",
        "checksum_created_without_bounded_admission": "CHECKSUM_CREATED_WITHOUT_BOUNDED_ADMISSION",
        "signature_created_without_bounded_admission": "SIGNATURE_CREATED_WITHOUT_BOUNDED_ADMISSION",
        "reproducible_environment_declared_without_bounded_admission": "REPRODUCIBLE_ENVIRONMENT_DECLARED_WITHOUT_BOUNDED_ADMISSION",
        "packet_artifact_treated_as_packet_emission": "PACKET_ARTIFACT_TREATED_AS_PACKET_EMISSION",
        "packet_artifact_treated_as_packet_transfer": "PACKET_ARTIFACT_TREATED_AS_PACKET_TRANSFER",
        "packet_artifact_treated_as_source": "PACKET_ARTIFACT_TREATED_AS_SOURCE",
        "packet_artifact_treated_as_authority": "PACKET_ARTIFACT_TREATED_AS_AUTHORITY",
        "packet_artifact_treated_as_currentness": "PACKET_ARTIFACT_TREATED_AS_CURRENTNESS",
        "packet_artifact_treated_as_final_completion": "PACKET_ARTIFACT_TREATED_AS_FINAL_COMPLETION",
        "packet_artifact_treated_as_runtime": "PACKET_ARTIFACT_TREATED_AS_RUNTIME",
        "packet_artifact_treated_as_cross_carrier_proof": "PACKET_ARTIFACT_TREATED_AS_CROSS_CARRIER_PROOF",
        "source_created": "SOURCE_CREATED",
        "authority_created": "AUTHORITY_CREATED",
        "currentness_created": "CURRENTNESS_CREATED",
        "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
        "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
        "deployment_created": "DEPLOYMENT_CREATED",
        "public_release_created": "PUBLIC_RELEASE_CREATED",
        "operation_permission_created": "OPERATION_PERMISSION_CREATED",
        "continuation_authorized": "CONTINUATION_AUTHORIZED",
        "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
        "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
        "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
        "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
        "artifact_existence_treated_as_packet_authority": "ARTIFACT_EXISTENCE_TREATED_AS_PACKET_AUTHORITY",
        "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "repo_local_availability_treated_as_packet_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_PACKET_AUTHORITY",
        "hidden_repo_state_used_as_packet_content": "HIDDEN_REPO_STATE_USED_AS_PACKET_CONTENT",
        "hidden_repo_state_used_as_packet_authority": "HIDDEN_REPO_STATE_USED_AS_PACKET_AUTHORITY",
        "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
        "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
        "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    }
    for field, code in non_claim_code_map.items():
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
            "packet_artifact_is_local_artifact_posture_only": True,
            "packet_artifact_is_not_packet_emission": True,
            "packet_artifact_is_not_packet_transfer": True,
            "packet_artifact_is_not_copying_to_another_device": True,
            "packet_artifact_is_not_second_carrier_execution": True,
            "packet_artifact_is_not_cross_carrier_proof": True,
            "packet_artifact_is_not_source": True,
            "packet_artifact_is_not_authority": True,
            "packet_artifact_is_not_currentness": True,
            "packet_artifact_is_not_final_completion": True,
            "packet_artifact_is_not_runtime": True,
            "packet_boundary_remains_boundary_basis_only": True,
            "local_command_success_remains_local_command_success_posture_only": True,
            "command_result_v2_remains_command_result_posture_only": True,
            "output_capture_v2_remains_output_capture_posture_only": True,
            "execution_trace_remains_audit_only": True,
            "selected_basis_remains_reference_shaped": True,
            "hidden_repo_state_remains_non_authority": True,
            "repo_local_availability_remains_non_authority": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "packet_emitted": False,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "second_carrier_received_it": False,
        "second_carrier_executed_anything": False,
        "external_result_exists": False,
        "cross_carrier_evidence_exists": False,
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
        "local_packet_artifact_is_source_standing": False,
        "local_packet_artifact_is_authority": False,
        "local_packet_artifact_is_currentness": False,
        "local_packet_artifact_is_cross_carrier_proof": False,
        "local_packet_artifact_is_runtime": False,
        "artifact_existence_is_packet_authority": False,
        "artifact_path_is_currentness": False,
        "hidden_repo_state_is_packet_content_authority": False,
        "predecessor_failures_repaired_hidden_erased_or_claimed_passed": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "packet artifact test",
            "packet artifact live artifact",
            "packet artifact terminal summary, if needed",
            "packet emission boundary/spec",
            "packet emission resolver/test/live artifact",
            "packet transfer",
            "manifest/checksum/signature implementation, if separately specified",
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
    if request.get("packet_artifact_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None
    if (
        request.get("additional_basis_context")
        or request.get("requires_additional_basis")
        or request.get("requested_packet_artifact_outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    ):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    if request.get("requested_packet_artifact_outcome") == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None
    return OUTCOME_RECORDED, None


def resolve_portable_source_body_verification_packet_artifact(
    declared_packet_artifact_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded packet artifact result without mutating inputs."""

    if isinstance(declared_packet_artifact_request, Mapping):
        request = copy.deepcopy(dict(declared_packet_artifact_request))
    else:
        request = {
            "packet_artifact_request_id": "malformed_packet_artifact_request",
            "packet_artifact_question": None,
            "packet_artifact_intent": None,
            "packet_artifact_scope": [],
            "declared_non_claims": {},
        }
    checks = _build_checks(request if isinstance(declared_packet_artifact_request, Mapping) else None)
    outcome, block_code = _outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    statement = _statement(recorded)
    metadata = {
        "portable_source_body_verification_packet_artifact_result_id": (
            f"{_safe_text(request.get('packet_artifact_request_id'))}"
            "__portable_source_body_verification_packet_artifact_result"
        ),
        "portable_source_body_verification_packet_artifact_result_type": RESULT_TYPE,
        "portable_source_body_verification_packet_artifact_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "packet_artifact_request_id": _safe_text(request.get("packet_artifact_request_id")),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
    }

    result: dict[str, Any] = {
        "portable_source_body_verification_packet_artifact_metadata": metadata,
        "declared_packet_artifact_question": {
            "packet_artifact_request_id": metadata["packet_artifact_request_id"],
            "question": _json_safe(request.get("packet_artifact_question")),
            "intent": _json_safe(request.get("packet_artifact_intent")),
            "core_question": CORE_QUESTION,
            "question_scope": "one local portable verification packet artifact only",
        },
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _safe_basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key, recorded)

    result.update(
        {
            "packet_artifact_scope": {
                "scope_values": _scope_values(request),
                "supported_scope_family": list(SUPPORTED_PACKET_ARTIFACT_SCOPE),
                "unsupported_scope_values": [
                    value for value in _scope_values(request) if value not in SUPPORTED_PACKET_ARTIFACT_SCOPE
                ],
            },
            "packet_artifact_checks": checks,
            "packet_artifact_statement": statement,
            "packet_artifact_non_meaning": _non_meaning(),
            "additional_basis_required": {
                "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "missing_or_unclear_basis": _json_safe(request.get("additional_basis_context", []))
                if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
                else [],
                "basis_not_scheduled": True,
                "basis_not_authorized": True,
                "basis_not_executed": True,
                "packet_emitted": False,
                "packet_transferred": False,
                "source_created": False,
                "authority_created": False,
                "currentness_created": False,
                "final_completion_claimed": False,
                "cross_carrier_evidence_created": False,
                "follow_on_work_authorized": False,
            },
            "not_recorded_basis": {
                "not_recorded": outcome == OUTCOME_NOT_RECORDED,
                "not_recorded_reason": _json_safe(request.get("not_recorded_basis"))
                if outcome == OUTCOME_NOT_RECORDED
                else None,
                "prior_artifacts_mutated": False,
                "prior_artifacts_repaired": False,
                "next_work_authorized": False,
                "packet_emitted": False,
                "packet_transferred": False,
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
    result["portable_source_body_verification_packet_artifact_summary"] = (
        build_portable_source_body_verification_packet_artifact_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_packet_artifact_from_path(
    declared_packet_artifact_request_path: Path | str,
) -> dict:
    """Resolve from an explicit JSON object request path."""

    path = Path(declared_packet_artifact_request_path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationPacketArtifactError(
            f"Declared packet artifact request unreadable: {path}"
        ) from exc
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationPacketArtifactError(
            f"Declared packet artifact request malformed JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        raise PortableSourceBodyVerificationPacketArtifactError(
            "Declared packet artifact request path must contain a JSON object."
        )
    return resolve_portable_source_body_verification_packet_artifact(parsed)


def _section(result: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = result.get(key)
    return value if isinstance(value, Mapping) else {}


def build_portable_source_body_verification_packet_artifact_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the public bounded packet-artifact summary surface."""

    metadata = _section(result, "portable_source_body_verification_packet_artifact_metadata")
    question = _section(result, "declared_packet_artifact_question")
    statement = _section(result, "packet_artifact_statement")
    non_claims = _section(result, "non_claims")
    block = _section(result, "block")
    checks = result.get("packet_artifact_checks", [])
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("packet_artifact_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "packet_artifact_recorded": statement.get("packet_artifact_recorded", False),
        "one_local_packet_artifact_recorded": statement.get("one_local_packet_artifact_recorded", False),
        "packet_boundary_basis_preserved": statement.get("packet_boundary_basis_preserved", False),
        "local_command_success_basis_preserved": statement.get("local_command_success_basis_preserved", False),
        "copyable_packet_shape_declared": statement.get("copyable_packet_shape_declared", False),
        "selected_packet_basis_declared": statement.get("selected_packet_basis_declared", False),
        "selected_basis_reference_shape_preserved": statement.get("selected_basis_reference_shape_preserved", False),
        "hidden_repo_state_excluded": statement.get("hidden_repo_state_excluded", False),
        "hidden_repo_state_not_used_as_packet_authority": statement.get("hidden_repo_state_not_used_as_packet_authority", False),
        "repo_local_availability_not_packet_authority": statement.get("repo_local_availability_not_packet_authority", False),
        "raw_full_prior_artifact_body_not_returned": statement.get("raw_full_prior_artifact_body_not_returned", False),
        "packet_not_emitted": statement.get("packet_not_emitted", False),
        "packet_not_transferred": statement.get("packet_not_transferred", False),
        "second_carrier_execution_not_authorized": statement.get("second_carrier_execution_not_authorized", False),
        "second_carrier_receipt_not_created": statement.get("second_carrier_receipt_not_created", False),
        "external_result_not_created": statement.get("external_result_not_created", False),
        "cross_carrier_evidence_not_created": statement.get("cross_carrier_evidence_not_created", False),
        "source_not_created": statement.get("source_not_created", False),
        "authority_not_created": statement.get("authority_not_created", False),
        "currentness_not_created": statement.get("currentness_not_created", False),
        "final_completion_not_created": statement.get("final_completion_not_created", False),
        "runtime_not_created": statement.get("runtime_not_created", False),
        "follow_on_work_not_authorized": statement.get("follow_on_work_not_authorized", False),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked", False),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", False),
        "selected_packet_boundary_outcome": _section(result, "selected_packet_boundary_basis").get("outcome"),
        "selected_packet_boundary_version": _section(result, "selected_packet_boundary_basis").get("result_version"),
        "selected_packet_boundary_failed_check_count": _section(result, "selected_packet_boundary_basis").get("failed_check_count"),
        "no_packet_emission_transfer_receipt_cross_carrier_evidence": non_claims.get("packet_emitted") is False
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
        "hidden_repo_state_not_packet_authority": non_claims.get("hidden_repo_state_used_as_packet_authority") is False,
        "repo_local_availability_not_packet_authority_non_claim": non_claims.get("repo_local_availability_treated_as_packet_authority") is False,
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


def write_portable_source_body_verification_packet_artifact_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a stable UTF-8 JSON result without overwriting prior artifacts."""

    metadata = _section(result, "portable_source_body_verification_packet_artifact_metadata")
    request_id = _safe_filename_part(
        metadata.get(
            "packet_artifact_request_id",
            "portable_source_body_verification_packet_artifact_request",
        )
    )
    if output_path is None:
        output_path = OUTPUT_ROOT / f"{request_id}__portable_source_body_verification_packet_artifact_result.json"
    path = _unique_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def _safe_filename_part(value: Any) -> str:
    text = _safe_text(value).strip()
    safe = "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in text)
    return safe or "portable_source_body_verification_packet_artifact_request"


def _basis_stub(label: str, **overrides: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_only": True,
        "reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "full_prior_artifact_body_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used_as_packet_content": False,
        "hidden_repo_state_used_as_packet_authority": False,
        "repo_local_availability_treated_as_packet_authority": False,
    }
    basis.update(overrides)
    return basis


def _posture_stub(label: str) -> dict[str, Any]:
    return {
        "posture_label": label,
        "declared": True,
        "packet_artifact_posture_only": True,
        "packet_emitted": False,
        "packet_transferred": False,
        "packet_copied_to_another_device": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_created": False,
        "second_carrier_execution_created": False,
        "second_carrier_receipt_created": False,
        "external_result_created": False,
        "cross_carrier_evidence_created": False,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "runtime_hosting_created": False,
        "deployment_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "continuation_authorized": False,
        "reusable_permission_created": False,
        "follow_on_work_authorized": False,
        "hidden_repo_state_used_as_packet_content": False,
        "hidden_repo_state_used_as_packet_authority": False,
        "repo_local_availability_treated_as_packet_authority": False,
    }


def build_declared_portable_source_body_verification_packet_artifact_request(
    packet_artifact_request_id: str = "portable_source_body_verification_packet_artifact_reference_review_001",
    packet_artifact_intent: str = INTENT_RECORD,
    selected_packet_boundary_result_path: Path | str | None = None,
    selected_packet_boundary_terminal_summary_path: Path | str | None = None,
) -> dict[str, Any]:
    """Build a reference-shaped declared request with required non-claims false."""

    request: dict[str, Any] = {
        "packet_artifact_request_id": packet_artifact_request_id,
        "packet_artifact_question": CORE_QUESTION,
        "packet_artifact_intent": packet_artifact_intent,
        "packet_artifact_scope": list(SUPPORTED_PACKET_ARTIFACT_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    request["selected_packet_boundary_basis"] = _basis_stub(
        "selected_packet_boundary_basis",
        path=_safe_text(selected_packet_boundary_result_path) if selected_packet_boundary_result_path else None,
        outcome=PACKET_BOUNDARY_RECORDED,
        result_version="0.1.0",
        failed_check_count=0,
        packet_boundary_recorded=True,
        one_future_packet_step_declared=True,
        local_command_success_basis_preserved=True,
        packet_created=False,
        packet_emitted=False,
        packet_boundary_authorized_transfer=False,
        packet_boundary_authorized_second_carrier_execution=False,
        cross_carrier_evidence_created=False,
        hidden_repo_state_used_as_packet_authority=False,
        selected_basis_reference_shape_preserved=True,
        raw_full_prior_artifact_body_returned=False,
    )
    request["selected_packet_boundary_terminal_summary_basis"] = _basis_stub(
        "selected_packet_boundary_terminal_summary_basis",
        path=_safe_text(selected_packet_boundary_terminal_summary_path)
        if selected_packet_boundary_terminal_summary_path
        else "spec/PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        terminal_summary_readability_basis_only=True,
        packet_boundary_is_not_packet_emission=True,
        no_packet_exists=True,
    )
    request["selected_command_success_basis"] = _basis_stub(
        "selected_command_success_basis",
        outcome=COMMAND_SUCCESS_RECORDED,
        result_version="0.1.0",
        failed_check_count=0,
        command_success_recorded=True,
        bounded_command_success_recorded=True,
        command_success_treated_as_packet_permission=False,
        command_success_treated_as_packet_emission=False,
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
        path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_TERMINAL_SUMMARY_V0.md",
        terminal_summary_readability_basis_only=True,
        local_command_success_not_packet_permission=True,
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
    request["selected_evidence_manifest_basis"] = _basis_stub(
        "selected_evidence_manifest_basis",
        evidence_manifest_basis_declared=True,
    )
    request["selected_artifact_containment_basis"] = _basis_stub(
        "selected_artifact_containment_basis",
        reference_only_selected_basis_required=True,
        recursive_full_artifact_embedding_blocked=True,
    )
    request["selected_portable_verification_basis"] = _basis_stub(
        "selected_portable_verification_basis",
        portable_verification_basis_declared=True,
        portable_verification_is_not_cross_carrier_proof=True,
    )
    for key in POSTURE_KEYS:
        request[key] = _posture_stub(key)
    request["copyable_packet_shape_declared_posture"].update(copyable_packet_shape_declared=True)
    request["selected_packet_basis_declared_posture"].update(selected_packet_basis_declared=True)
    request["selected_basis_reference_shape_posture"].update(
        selected_basis_reference_shape_preserved=True
    )
    request["hidden_repo_state_excluded_posture"].update(
        hidden_repo_state_used_as_packet_content=False,
        hidden_repo_state_used_as_packet_authority=False,
    )
    request["repo_local_availability_not_packet_authority_posture"].update(
        repo_local_availability_treated_as_packet_authority=False
    )
    request["raw_full_prior_artifact_body_not_returned_posture"].update(
        raw_full_prior_artifact_body_returned=False
    )
    return request
