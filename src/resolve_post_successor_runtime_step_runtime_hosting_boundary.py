"""Resolve one post-successor-runtime-step runtime-hosting-boundary posture.

This module records a bounded runtime-hosting-boundary posture only. It is
downstream of the post-minimal-runtime successor-runtime-step line and does not
create runtime hosting, ongoing runtime, reusable runtime permission,
continuation, self-continuation, source transfer, source receipt, reception
authorization, source, authority, currentness, deployment, public release,
operation permission, reusable permission, or follow-on work.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Mapping


class PostSuccessorRuntimeStepRuntimeHostingBoundaryError(Exception):
    """Bounded resolver error for runtime-hosting-boundary requests."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_successor_runtime_step_runtime_hosting_boundary"

OUTCOME_RECORDED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary"
)

CORE_QUESTION = (
    "Can the clean post-minimal-runtime successor-runtime-step basis be bounded "
    "for one future runtime-hosting review without creating runtime hosting, "
    "ongoing runtime, reusable runtime permission, continuation, self-continuation, "
    "self-recursive growth, runtime daemon, runtime loop, public API, "
    "participant-facing interface, distributed network behavior, source transfer, "
    "source receipt, reception authorization, source, authority, currentness, "
    "deployment, public release, operation permission, reusable permission, "
    "derivative reception, vessel relation, another reception request, adoption, "
    "receiving-context governance, publication flow, or follow-on work?"
)

EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME = (
    "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED"
)
EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME = (
    "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_RECORDED"
)
EXPECTED_MINIMAL_RUNTIME_OUTCOME = "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED"
EXPECTED_RUNTIME_BOUNDARY_OUTCOME = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED"
EXPECTED_RUNTIME_READINESS_OUTCOME = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED"
)
EXPECTED_FINAL_COMPLETION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "RUNTIME_HOSTING_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_RUNTIME_HOSTING_REVIEW_DECLARED",
    "SUCCESSOR_RUNTIME_STEP_BASIS_PRESERVED",
    "SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING",
    "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_NOT_HOSTING_AUTHORIZATION",
    "RUNTIME_HOSTING_BOUNDARY_NOT_RUNTIME_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_NOT_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_BOUNDARY_NOT_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_NOT_CONTINUATION",
    "RUNTIME_HOSTING_NOT_CREATED",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "NO_SOURCE_TRANSFER",
    "NO_SOURCE_RECEIPT",
    "NO_RECEPTION_AUTHORIZATION",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_DEPLOYMENT_CREATED",
    "NO_PUBLIC_RELEASE_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_RUNTIME_HOSTING_INFERENCE",
    "NO_ONGOING_RUNTIME_INFERENCE",
    "NO_REUSABLE_RUNTIME_PERMISSION_INFERENCE",
    "NO_CONTINUATION_INFERENCE",
    "NO_SELF_CONTINUATION_INFERENCE",
    "NO_DAEMON_INFERENCE",
    "NO_LOOP_INFERENCE",
    "NO_PUBLIC_API_INFERENCE",
    "NO_PARTICIPANT_INTERFACE_INFERENCE",
    "NO_DISTRIBUTED_NETWORK_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
)
SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "runtime_hosting_created",
    "ongoing_runtime_created",
    "reusable_runtime_permission_created",
    "continuation_authorized",
    "self_continuation_authorized",
    "self_recursive_growth_created",
    "runtime_daemon_created",
    "runtime_loop_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_hosting_boundary_treated_as_runtime_hosting",
    "runtime_hosting_boundary_treated_as_ongoing_runtime",
    "runtime_hosting_boundary_treated_as_reusable_runtime_permission",
    "runtime_hosting_boundary_treated_as_continuation",
    "runtime_hosting_boundary_treated_as_self_continuation",
    "runtime_hosting_boundary_treated_as_source_transfer",
    "runtime_hosting_boundary_treated_as_source_receipt",
    "runtime_hosting_boundary_treated_as_reception_authorization",
    "runtime_hosting_boundary_treated_as_source",
    "runtime_hosting_boundary_treated_as_authority",
    "runtime_hosting_boundary_treated_as_currentness",
    "runtime_hosting_boundary_treated_as_deployment",
    "runtime_hosting_boundary_treated_as_public_release",
    "runtime_hosting_boundary_treated_as_operation_permission",
    "runtime_hosting_boundary_treated_as_reusable_permission",
    "runtime_hosting_boundary_treated_as_follow_on_work",
    "successor_runtime_step_treated_as_runtime_hosting",
    "successor_runtime_step_treated_as_ongoing_runtime",
    "successor_runtime_step_treated_as_reusable_runtime_permission",
    "successor_runtime_step_treated_as_continuation",
    "successor_runtime_step_treated_as_self_continuation",
    "bounded_successor_runtime_result_or_refusal_authorized_hosting",
    "artifact_existence_treated_as_runtime_hosting_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_hosting_boundary_authority",
    "repo_local_availability_treated_as_runtime_hosting_boundary_authority",
    "hidden_repo_state_used_as_runtime_hosting_boundary_content",
    "hidden_repo_state_used_as_runtime_hosting_boundary_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "consumed_request_reopened",
    "authorization_token_reused",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "runtime_hosting_boundary_recorded",
    "one_future_runtime_hosting_review_declared",
    "successor_runtime_step_basis_preserved",
    "successor_runtime_step_not_runtime_hosting",
    "bounded_successor_runtime_result_or_refusal_not_hosting_authorization",
    "runtime_hosting_boundary_not_runtime_hosting",
    "runtime_hosting_boundary_not_ongoing_runtime",
    "runtime_hosting_boundary_not_reusable_runtime_permission",
    "runtime_hosting_boundary_not_continuation",
    "runtime_hosting_not_created",
    "ongoing_runtime_not_created",
    "reusable_runtime_permission_not_created",
    "continuation_not_authorized",
    "self_continuation_not_authorized",
    "runtime_daemon_not_created",
    "runtime_loop_not_created",
    "public_api_not_created",
    "participant_facing_interface_not_created",
    "distributed_network_behavior_not_created",
    "source_transfer_not_created",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_runtime_hosting_boundary_authority",
    "repo_local_availability_not_runtime_hosting_boundary_authority",
    "artifact_existence_not_runtime_hosting_boundary_authority",
    "latest_file_posture_not_runtime_hosting_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

BLOCK_CODES = (
    "RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED",
    "RUNTIME_HOSTING_BOUNDARY_REQUEST_DECLARED_BLOCK",
    "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
    "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_CREATED_BEFORE_REVIEW",
    "RUNTIME_HOSTING_CREATED",
    "ONGOING_RUNTIME_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CONTINUATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_AUTHORITY",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CURRENTNESS",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PRIOR_ARTIFACTS_MUTATED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT",
    "MINIMAL_RUNTIME_BASIS_MISSING",
    "MINIMAL_RUNTIME_NOT_RECORDED",
    "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
    "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    "RUNTIME_BOUNDARY_BASIS_MISSING",
    "RUNTIME_BOUNDARY_NOT_RECORDED",
    "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_READINESS_BASIS_MISSING",
    "RUNTIME_READINESS_NOT_RECORDED",
    "RUNTIME_READINESS_VERSION_NOT_0_1_0",
    "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_BASIS_MISSING",
    "FINAL_COMPLETION_NOT_RECORDED",
    "FINAL_COMPLETION_VERSION_NOT_0_1_0",
    "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    "POST_PORTABLE_CURRENTNESS_SURFACE_DID_NOT_PRESERVE_CHECKABILITY_NOT_CONTINUATION",
)

POSTURE_FIELDS = (
    "runtime_hosting_boundary_spec_only_posture",
    "one_future_runtime_hosting_review_posture",
    "successor_runtime_step_basis_preserved_posture",
    "successor_runtime_step_not_runtime_hosting_posture",
    "bounded_successor_runtime_result_or_refusal_not_hosting_authorization_posture",
    "runtime_hosting_boundary_not_runtime_hosting_posture",
    "runtime_hosting_boundary_not_ongoing_runtime_posture",
    "runtime_hosting_boundary_not_reusable_runtime_permission_posture",
    "runtime_hosting_boundary_not_continuation_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
    "continuation_not_authorized_posture",
    "self_continuation_not_authorized_posture",
    "runtime_daemon_not_created_posture",
    "runtime_loop_not_created_posture",
    "public_api_not_created_posture",
    "participant_facing_interface_not_created_posture",
    "distributed_network_behavior_not_created_posture",
    "source_transfer_not_created_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "deployment_not_created_posture",
    "public_release_not_created_posture",
    "operation_permission_not_created_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_runtime_hosting_boundary_authority_posture",
    "artifact_existence_not_runtime_hosting_boundary_authority_posture",
    "latest_file_posture_not_runtime_hosting_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

RAW_OR_HIDDEN_SENTINELS = (
    "RAW_RUNTIME_HOSTING_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RUNTIME_STEP_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RUNTIME_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTION_VALUE = "[bounded-redacted-raw-or-hidden-state]"

SENSITIVE_KEY_PARTS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "raw_capture_body",
    "raw_success_body",
    "raw_verification_body",
    "raw_external_result_body",
    "raw_cross_carrier_evidence_body",
    "raw_portable_verification_closure_body",
    "raw_final_completion_body",
    "raw_runtime_readiness_boundary_body",
    "raw_runtime_readiness_body",
    "raw_runtime_boundary_body",
    "raw_minimal_runtime_body",
    "raw_successor_runtime_step_boundary_body",
    "raw_successor_runtime_step_body",
    "raw_successor_runtime_result_body",
    "raw_runtime_hosting_boundary_body",
    "raw_runtime_hosting_body",
    "raw_ongoing_runtime_body",
    "raw_runtime_body",
    "runtime_hosting_boundary_body",
    "runtime_readiness_body",
    "runtime_boundary_body",
    "minimal_runtime_body",
    "successor_runtime_step_boundary_body",
    "successor_runtime_step_body",
    "successor_runtime_result_body",
    "runtime_hosting_body",
    "ongoing_runtime_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

PROHIBITED_OUTPUT_MARKERS = (
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/",
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary/",
    "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary/",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/",
    "final-completion-boundary",
    "portable-verification-closure",
    "cross-carrier-evidence",
    "actual_second_carrier_live_capture",
    "second-carrier",
    "packet-transfer",
    "packet-emission",
    "command-success",
    "command-result",
    "source-transfer",
    "source-receipt",
    "reception",
    "runtime-hosting/",
    "ongoing-runtime/",
    "deployment/",
    "public-release/",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _safe_deepcopy(value: Any) -> Any:
    return deepcopy(value)


def _is_sensitive_key(key: str) -> bool:
    lower_key = key.lower()
    return any(part in lower_key for part in SENSITIVE_KEY_PARTS)


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            text_key = str(key)
            if _is_sensitive_key(text_key):
                sanitized[text_key] = REDACTION_VALUE
            else:
                sanitized[text_key] = _sanitize(item)
        return sanitized
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, str):
        if any(sentinel in value for sentinel in RAW_OR_HIDDEN_SENTINELS):
            return REDACTION_VALUE
        return value
    return value


def _mapping_copy(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(_safe_deepcopy(value))
    return {}


def _as_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return True


def _find_key(value: Any, key: str) -> Any:
    if isinstance(value, Mapping):
        if key in value:
            return value[key]
        for item in value.values():
            found = _find_key(item, key)
            if found is not None:
                return found
    elif isinstance(value, list):
        for item in value:
            found = _find_key(item, key)
            if found is not None:
                return found
    return None


def _value_from_request_or_basis(
    request: Mapping[str, Any],
    request_key: str,
    basis_key: str | None = None,
    basis_field: str | None = None,
    default: Any = None,
) -> Any:
    if request_key in request:
        return request[request_key]
    if basis_field:
        basis = request.get(basis_field)
        if _is_mapping(basis):
            found = _find_key(basis, basis_key or request_key)
            if found is not None:
                return found
    return default


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    value = request.get("runtime_hosting_boundary_scope", SUPPORTED_SCOPE_VALUES)
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        return [str(item) for item in value.values()]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": expected,
        "actual_posture": actual,
    }
    if code:
        key = "block_code" if not passed else "block_code"
        record[key] = None if passed else code
    return record


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    checks.append(_check(name, passed, expected, actual, code))


def _basis_present(request: Mapping[str, Any], basis_field: str, path_field: str | None = None) -> bool:
    if _present(request.get(basis_field)):
        return True
    if path_field and _present(request.get(path_field)):
        return True
    return False


def _default_basis(
    basis_id: str,
    path: str,
    outcome: str,
    result_version: str = RESULT_VERSION,
    failed_check_count: int = 0,
    **extra: Any,
) -> dict[str, Any]:
    basis = {
        "basis_id": basis_id,
        "basis_path": path,
        "basis_role": "selected_standing_basis",
        "outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _posture(name: str, declared: bool = True, **extra: Any) -> dict[str, Any]:
    posture = {
        "posture_name": name,
        "declared": bool(declared),
        "preserved": bool(declared),
        "bounded_runtime_hosting_boundary_only": True,
        "creates_runtime_hosting": False,
        "creates_ongoing_runtime": False,
        "creates_reusable_runtime_permission": False,
        "authorizes_continuation": False,
        "authorizes_self_continuation": False,
        "creates_self_recursive_growth": False,
        "creates_runtime_daemon": False,
        "creates_runtime_loop": False,
        "creates_public_api": False,
        "creates_participant_facing_interface": False,
        "creates_distributed_network_behavior": False,
        "creates_source_transfer": False,
        "creates_source_receipt": False,
        "creates_reception_authorization": False,
        "creates_source": False,
        "creates_authority": False,
        "creates_currentness": False,
        "creates_deployment": False,
        "creates_public_release": False,
        "creates_operation_permission": False,
        "creates_reusable_permission": False,
        "authorizes_follow_on_work": False,
    }
    posture.update(extra)
    return posture


def _default_postures(declared: bool = True) -> dict[str, dict[str, Any]]:
    return {
        field: _posture(field.removesuffix("_posture"), declared=declared)
        for field in POSTURE_FIELDS
    }


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {field: bool(recorded) for field in ALLOWED_TRUE_RECORDED_FIELDS}
    if not recorded:
        for field in ALLOWED_TRUE_RECORDED_FIELDS:
            statement[field] = False
        safe_true_fields = (
            "runtime_hosting_not_created",
            "ongoing_runtime_not_created",
            "reusable_runtime_permission_not_created",
            "continuation_not_authorized",
            "self_continuation_not_authorized",
            "runtime_daemon_not_created",
            "runtime_loop_not_created",
            "public_api_not_created",
            "participant_facing_interface_not_created",
            "distributed_network_behavior_not_created",
            "source_transfer_not_created",
            "source_receipt_not_created",
            "reception_authorization_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "reusable_permission_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_runtime_hosting_boundary_authority",
            "repo_local_availability_not_runtime_hosting_boundary_authority",
            "artifact_existence_not_runtime_hosting_boundary_authority",
            "latest_file_posture_not_runtime_hosting_boundary_authority",
            "raw_full_prior_artifact_body_not_returned",
            "official_enum_scope_strings_not_redacted",
            "hostile_raw_body_content_contained",
            "predecessor_failure_evidence_preserved",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        )
        for field in safe_true_fields:
            statement[field] = True
    return statement


def _non_claims_from_request(request: Mapping[str, Any] | None) -> dict[str, bool]:
    non_claims = {field: False for field in REQUIRED_FALSE_NON_CLAIMS}
    if request and _is_mapping(request.get("declared_non_claims")):
        for field in REQUIRED_FALSE_NON_CLAIMS:
            if field in request["declared_non_claims"]:
                non_claims[field] = bool(request["declared_non_claims"][field])
    return non_claims


def _non_meaning() -> dict[str, bool]:
    return {
        "runtime_hosting_boundary_means_runtime_hosting": False,
        "runtime_hosting_boundary_means_ongoing_runtime": False,
        "runtime_hosting_boundary_means_reusable_runtime_permission": False,
        "runtime_hosting_boundary_means_continuation": False,
        "runtime_hosting_boundary_means_self_continuation": False,
        "runtime_hosting_boundary_means_self_recursive_growth": False,
        "runtime_hosting_boundary_means_runtime_daemon": False,
        "runtime_hosting_boundary_means_runtime_loop": False,
        "runtime_hosting_boundary_means_public_api": False,
        "runtime_hosting_boundary_means_participant_facing_interface": False,
        "runtime_hosting_boundary_means_distributed_network_behavior": False,
        "runtime_hosting_boundary_means_source_transfer": False,
        "runtime_hosting_boundary_means_source_receipt": False,
        "runtime_hosting_boundary_means_reception_authorization": False,
        "runtime_hosting_boundary_means_source": False,
        "runtime_hosting_boundary_means_authority": False,
        "runtime_hosting_boundary_means_currentness": False,
        "runtime_hosting_boundary_means_deployment": False,
        "runtime_hosting_boundary_means_public_release": False,
        "runtime_hosting_boundary_means_operation_permission": False,
        "runtime_hosting_boundary_means_reusable_permission": False,
        "runtime_hosting_boundary_means_follow_on_work": False,
        "successor_runtime_step_means_runtime_hosting": False,
        "successor_runtime_step_means_ongoing_runtime": False,
        "successor_runtime_step_means_reusable_runtime_permission": False,
        "successor_runtime_step_means_continuation": False,
        "bounded_successor_runtime_result_or_refusal_means_hosting_authorization": False,
        "artifact_existence_means_runtime_hosting_boundary_authority": False,
        "repo_local_availability_means_runtime_hosting_boundary_authority": False,
        "latest_file_posture_means_runtime_hosting_boundary_authority": False,
        "hidden_repo_state_means_runtime_hosting_boundary_authority": False,
        "predecessor_failure_repaired_hidden_or_claimed_passed": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "runtime-hosting-boundary resolver test",
        "runtime-hosting-boundary live artifact",
        "runtime-hosting-boundary terminal summary, if needed",
        "runtime-hosting specification",
        "runtime-hosting resolver/test/live artifact",
        "ongoing runtime",
        "reusable runtime permission",
        "continuation beyond bounded steps",
        "self-continuation",
        "self-recursive growth",
        "runtime daemon",
        "runtime loop",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
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
        "deployment",
        "public release",
        "publication flow",
        "reusable permission",
        "successor reception request",
        "follow-on work",
    ]


def _first_failure(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not check.get("passed"):
            return check
    return None


def _add_outcome_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    label: str,
    basis_field: str,
    path_field: str,
    outcome_key: str,
    version_key: str,
    failed_count_key: str,
    expected_outcome: str,
    missing_code: str,
    outcome_code: str,
    version_code: str,
    failed_code: str,
) -> None:
    present = _basis_present(request, basis_field, path_field)
    _add_check(
        checks,
        f"{label} basis declared",
        present,
        "declared selected basis",
        request.get(basis_field) or request.get(path_field),
        missing_code,
    )
    outcome = _value_from_request_or_basis(
        request, outcome_key, "outcome", basis_field, default=None
    )
    version = _value_from_request_or_basis(
        request, version_key, "result_version", basis_field, default=None
    )
    failed_count = _value_from_request_or_basis(
        request, failed_count_key, "failed_check_count", basis_field, default=None
    )
    _add_check(
        checks,
        f"{label} outcome recorded",
        outcome == expected_outcome,
        expected_outcome,
        outcome,
        outcome_code,
    )
    _add_check(
        checks,
        f"{label} version 0.1.0",
        version == RESULT_VERSION,
        RESULT_VERSION,
        version,
        version_code,
    )
    _add_check(
        checks,
        f"{label} failed checks zero",
        _as_int(failed_count) == 0,
        0,
        failed_count,
        failed_code,
    )


def _add_false_basis_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    name: str,
    request_key: str,
    basis_key: str | None,
    basis_field: str,
    code: str,
) -> None:
    actual = _value_from_request_or_basis(
        request, request_key, basis_key or request_key, basis_field, default=False
    )
    _add_check(checks, name, actual is False, False, actual, code)


def _add_true_basis_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    name: str,
    request_key: str,
    basis_key: str | None,
    basis_field: str,
    code: str,
) -> None:
    actual = _value_from_request_or_basis(
        request, request_key, basis_key or request_key, basis_field, default=None
    )
    _add_check(checks, name, actual is True, True, actual, code)


def _add_runtime_hosting_boundary_checks(
    request: Mapping[str, Any],
    forced_block_code: str | None = None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if forced_block_code:
        _add_check(
            checks,
            "declared runtime-hosting-boundary request readable and well formed",
            False,
            "readable mapping request",
            forced_block_code,
            forced_block_code,
        )
        return checks

    question = request.get("runtime_hosting_boundary_question")
    _add_check(
        checks,
        "runtime-hosting-boundary question declared",
        question == CORE_QUESTION,
        CORE_QUESTION,
        question,
        "RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED",
    )

    intent = request.get("runtime_hosting_boundary_intent")
    _add_check(
        checks,
        "runtime-hosting-boundary intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED",
    )
    _add_check(
        checks,
        "runtime-hosting-boundary explicit block intent absent",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "RUNTIME_HOSTING_BOUNDARY_REQUEST_DECLARED_BLOCK",
    )

    scope = _scope_values(request)
    unsupported_scope = [value for value in scope if value not in SUPPORTED_SCOPE_VALUES]
    _add_check(
        checks,
        "runtime-hosting-boundary scope supported",
        not unsupported_scope,
        "only supported runtime-hosting-boundary scope values",
        unsupported_scope,
        "UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
    )

    _add_outcome_checks(
        request,
        checks,
        label="successor-runtime-step",
        basis_field="selected_successor_runtime_step_basis",
        path_field="selected_successor_runtime_step_result_path",
        outcome_key="selected_successor_runtime_step_result_outcome",
        version_key="selected_successor_runtime_step_result_version",
        failed_count_key="selected_successor_runtime_step_failed_check_count",
        expected_outcome=EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        missing_code="SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        outcome_code="SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
        version_code="SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
        failed_code="SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    )
    _add_check(
        checks,
        "successor-runtime-step terminal summary basis declared",
        _basis_present(request, "selected_successor_runtime_step_terminal_summary_basis"),
        "declared selected terminal summary basis",
        request.get("selected_successor_runtime_step_terminal_summary_basis"),
        "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    )
    _add_true_basis_check(
        request,
        checks,
        name="successor-runtime-step recorded bounded successor-runtime step",
        request_key="selected_successor_runtime_step_bounded_successor_runtime_step_recorded",
        basis_key="bounded_successor_runtime_step_recorded",
        basis_field="selected_successor_runtime_step_basis",
        code="SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP",
    )
    _add_true_basis_check(
        request,
        checks,
        name="successor-runtime-step recorded bounded successor-runtime result/refusal",
        request_key=(
            "selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded"
        ),
        basis_key="bounded_successor_runtime_result_or_refusal_recorded",
        basis_field="selected_successor_runtime_step_basis",
        code="SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    )
    _add_true_basis_check(
        request,
        checks,
        name="successor-runtime-step did not authorize successor-after-successor action",
        request_key=(
            "selected_successor_runtime_step_no_successor_after_successor_action_authorized"
        ),
        basis_key="no_successor_after_successor_action_authorized",
        basis_field="selected_successor_runtime_step_basis",
        code="SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK",
    )

    successor_false_checks = (
        (
            "successor-runtime-step did not create runtime hosting",
            "selected_successor_runtime_step_already_created_runtime_hosting",
            "runtime_hosting_created",
            "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_RUNTIME_HOSTING",
        ),
        (
            "successor-runtime-step did not create ongoing runtime",
            "selected_successor_runtime_step_already_created_ongoing_runtime",
            "ongoing_runtime_created",
            "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_ONGOING_RUNTIME",
        ),
        (
            "successor-runtime-step did not create reusable runtime permission",
            "selected_successor_runtime_step_already_created_reusable_runtime_permission",
            "reusable_runtime_permission_created",
            "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "successor-runtime-step did not authorize continuation",
            "selected_successor_runtime_step_already_authorized_continuation",
            "continuation_authorized",
            "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "successor-runtime-step did not authorize self-continuation",
            "selected_successor_runtime_step_already_authorized_self_continuation",
            "self_continuation_authorized",
            "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
        (
            "successor-runtime-step not treated as runtime hosting",
            "selected_successor_runtime_step_treated_as_runtime_hosting",
            "successor_runtime_step_treated_as_runtime_hosting",
            "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING",
        ),
        (
            "successor-runtime-step not treated as ongoing runtime",
            "selected_successor_runtime_step_treated_as_ongoing_runtime",
            "successor_runtime_step_treated_as_ongoing_runtime",
            "SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME",
        ),
        (
            "successor-runtime-step not treated as reusable runtime permission",
            "selected_successor_runtime_step_treated_as_reusable_runtime_permission",
            "successor_runtime_step_treated_as_reusable_runtime_permission",
            "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "successor-runtime-step not treated as continuation",
            "selected_successor_runtime_step_treated_as_continuation",
            "successor_runtime_step_treated_as_continuation",
            "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION",
        ),
        (
            "successor-runtime-step not treated as self-continuation",
            "selected_successor_runtime_step_treated_as_self_continuation",
            "successor_runtime_step_treated_as_self_continuation",
            "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "successor-runtime-step did not authorize future work",
            "selected_successor_runtime_step_authorized_future_work",
            "follow_on_work_authorized",
            "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK",
        ),
        (
            "bounded successor-runtime result/refusal did not authorize hosting",
            "selected_bounded_successor_runtime_result_or_refusal_authorized_hosting",
            "bounded_successor_runtime_result_or_refusal_authorized_hosting",
            "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
        ),
    )
    for name, request_key, basis_key, code in successor_false_checks:
        _add_false_basis_check(
            request,
            checks,
            name=name,
            request_key=request_key,
            basis_key=basis_key,
            basis_field="selected_successor_runtime_step_basis",
            code=code,
        )

    _add_outcome_checks(
        request,
        checks,
        label="successor-runtime-step-boundary",
        basis_field="selected_successor_runtime_step_boundary_basis",
        path_field="selected_successor_runtime_step_boundary_result_path",
        outcome_key="selected_successor_runtime_step_boundary_result_outcome",
        version_key="selected_successor_runtime_step_boundary_result_version",
        failed_count_key="selected_successor_runtime_step_boundary_failed_check_count",
        expected_outcome=EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
        missing_code="SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING",
        outcome_code="SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED",
        version_code="SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _add_outcome_checks(
        request,
        checks,
        label="minimal-runtime",
        basis_field="selected_minimal_runtime_basis",
        path_field="selected_minimal_runtime_result_path",
        outcome_key="selected_minimal_runtime_result_outcome",
        version_key="selected_minimal_runtime_result_version",
        failed_count_key="selected_minimal_runtime_failed_check_count",
        expected_outcome=EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        missing_code="MINIMAL_RUNTIME_BASIS_MISSING",
        outcome_code="MINIMAL_RUNTIME_NOT_RECORDED",
        version_code="MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
        failed_code="MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    )
    _add_outcome_checks(
        request,
        checks,
        label="runtime-boundary",
        basis_field="selected_runtime_boundary_basis",
        path_field="selected_runtime_boundary_result_path",
        outcome_key="selected_runtime_boundary_result_outcome",
        version_key="selected_runtime_boundary_result_version",
        failed_count_key="selected_runtime_boundary_failed_check_count",
        expected_outcome=EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        missing_code="RUNTIME_BOUNDARY_BASIS_MISSING",
        outcome_code="RUNTIME_BOUNDARY_NOT_RECORDED",
        version_code="RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _add_outcome_checks(
        request,
        checks,
        label="runtime-readiness",
        basis_field="selected_runtime_readiness_basis",
        path_field="selected_runtime_readiness_result_path",
        outcome_key="selected_runtime_readiness_result_outcome",
        version_key="selected_runtime_readiness_result_version",
        failed_count_key="selected_runtime_readiness_failed_check_count",
        expected_outcome=EXPECTED_RUNTIME_READINESS_OUTCOME,
        missing_code="RUNTIME_READINESS_BASIS_MISSING",
        outcome_code="RUNTIME_READINESS_NOT_RECORDED",
        version_code="RUNTIME_READINESS_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    )
    _add_outcome_checks(
        request,
        checks,
        label="portable verification final completion",
        basis_field="selected_portable_verification_final_completion_basis",
        path_field="selected_portable_verification_final_completion_result_path",
        outcome_key="selected_portable_verification_final_completion_result_outcome",
        version_key="selected_portable_verification_final_completion_result_version",
        failed_count_key="selected_portable_verification_final_completion_failed_check_count",
        expected_outcome=EXPECTED_FINAL_COMPLETION_OUTCOME,
        missing_code="FINAL_COMPLETION_BASIS_MISSING",
        outcome_code="FINAL_COMPLETION_NOT_RECORDED",
        version_code="FINAL_COMPLETION_VERSION_NOT_0_1_0",
        failed_code="FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    )

    _add_check(
        checks,
        "post-portable currentness surface basis declared",
        _basis_present(
            request,
            "selected_post_portable_verification_currentness_basis",
            "selected_post_portable_currentness_surface_path",
        ),
        "declared selected currentness-compression basis",
        request.get("selected_post_portable_verification_currentness_basis")
        or request.get("selected_post_portable_currentness_surface_path"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    )
    _add_true_basis_check(
        request,
        checks,
        name="post-portable currentness surface states checkability not continuation",
        request_key=(
            "selected_post_portable_currentness_surface_states_checkability_not_continuation"
        ),
        basis_key="states_checkability_not_continuation",
        basis_field="selected_post_portable_verification_currentness_basis",
        code="POST_PORTABLE_CURRENTNESS_SURFACE_DID_NOT_PRESERVE_CHECKABILITY_NOT_CONTINUATION",
    )
    currentness_authorized_next = _value_from_request_or_basis(
        request,
        "selected_post_portable_currentness_surface_authorized_next_work",
        "authorized_next_work",
        "selected_post_portable_verification_currentness_basis",
        default=False,
    )
    _add_check(
        checks,
        "post-portable currentness surface does not authorize next work",
        currentness_authorized_next is False,
        False,
        currentness_authorized_next,
        "FOLLOW_ON_WORK_AUTHORIZED",
    )

    predecessor_visible = request.get("predecessor_failure_evidence_preserved", True)
    predecessor_repaired = request.get("predecessor_failure_repaired", False)
    predecessor_hidden = request.get("predecessor_failure_hidden", False)
    predecessor_claimed = request.get("predecessor_failure_claimed_passed", False)
    _add_check(
        checks,
        "predecessor failure evidence visible and unrepaired",
        predecessor_visible is True
        and predecessor_repaired is False
        and predecessor_hidden is False
        and predecessor_claimed is False,
        "visible, unrepaired, unhidden, not claimed passed",
        {
            "predecessor_failure_evidence_preserved": predecessor_visible,
            "predecessor_failure_repaired": predecessor_repaired,
            "predecessor_failure_hidden": predecessor_hidden,
            "predecessor_failure_claimed_passed": predecessor_claimed,
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )

    for posture_field in POSTURE_FIELDS:
        posture_value = request.get(posture_field)
        declared = _is_mapping(posture_value) and posture_value.get("declared") is True
        _add_check(
            checks,
            f"{posture_field} declared",
            declared,
            "declared true posture mapping",
            posture_value,
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )

    grouped_posture_fields = (
        "source_not_created_posture",
        "authority_not_created_posture",
        "currentness_not_created_posture",
        "deployment_not_created_posture",
        "public_release_not_created_posture",
        "operation_permission_not_created_posture",
        "follow_on_work_not_authorized_posture",
    )
    grouped_declared = all(
        _is_mapping(request.get(field)) and request[field].get("declared") is True
        for field in grouped_posture_fields
    )
    _add_check(
        checks,
        "source/authority/currentness/deployment/public-release/operation-permission/follow-on not-created posture declared",
        grouped_declared,
        "all grouped not-created postures declared",
        {field: request.get(field) for field in grouped_posture_fields},
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )

    direct_false_checks = (
        ("runtime-hosting boundary not created before review", "runtime_hosting_boundary_created_before_review", "RUNTIME_HOSTING_BOUNDARY_CREATED_BEFORE_REVIEW"),
        ("runtime hosting not created", "runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("ongoing runtime not created", "ongoing_runtime_created", "ONGOING_RUNTIME_CREATED"),
        ("reusable runtime permission not created", "reusable_runtime_permission_created", "REUSABLE_RUNTIME_PERMISSION_CREATED"),
        ("continuation not authorized", "continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("self-continuation not authorized", "self_continuation_authorized", "SELF_CONTINUATION_AUTHORIZED"),
        ("self-recursive growth not created", "self_recursive_growth_created", "SELF_RECURSIVE_GROWTH_CREATED"),
        ("runtime daemon not created", "runtime_daemon_created", "RUNTIME_DAEMON_CREATED"),
        ("runtime loop not created", "runtime_loop_created", "RUNTIME_LOOP_CREATED"),
        ("public API not created", "public_api_created", "PUBLIC_API_CREATED"),
        ("participant-facing interface not created", "participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
        ("distributed network behavior not created", "distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
        ("source transfer did not occur", "source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source receipt did not occur", "source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception authorization not created", "reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("source not created", "source_created", "SOURCE_CREATED"),
        ("authority not created", "authority_created", "AUTHORITY_CREATED"),
        ("currentness not created", "currentness_created", "CURRENTNESS_CREATED"),
        ("deployment not created", "deployment_created", "DEPLOYMENT_CREATED"),
        ("public release not created", "public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation permission not created", "operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("reusable permission not created", "reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative reception not authorized", "derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel relation not authorized", "vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("adoption not created", "adoption_created", "ADOPTION_CREATED"),
        ("receiving-context governance not created", "receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
        ("publication flow not created", "publication_flow_created", "PUBLICATION_FLOW_CREATED"),
        ("follow-on work not authorized", "follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("artifact existence not treated as runtime-hosting-boundary authority", "artifact_existence_treated_as_runtime_hosting_boundary_authority", "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY"),
        ("artifact path not treated as currentness", "artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        ("latest file posture not treated as runtime-hosting-boundary authority", "latest_file_posture_treated_as_runtime_hosting_boundary_authority", "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY"),
        ("repo-local availability not treated as runtime-hosting-boundary authority", "repo_local_availability_treated_as_runtime_hosting_boundary_authority", "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY"),
        ("hidden repo state not used as runtime-hosting-boundary content", "hidden_repo_state_used_as_runtime_hosting_boundary_content", "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_CONTENT"),
        ("hidden repo state not used as runtime-hosting-boundary authority", "hidden_repo_state_used_as_runtime_hosting_boundary_authority", "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY"),
        ("selected basis remains reference-shaped", "selected_basis_not_reference_shaped", "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
        ("raw full prior artifact body not returned", "raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        ("prior artifacts not mutated", "prior_artifacts_mutated", "PRIOR_ARTIFACTS_MUTATED"),
        ("consumed request token not reopened", "consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization token not reused", "authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
    )
    for name, field, code in direct_false_checks:
        actual = request.get(field, False)
        _add_check(checks, name, actual is False, False, actual, code)

    declared_non_claims = request.get("declared_non_claims")
    non_claims_ok = _is_mapping(declared_non_claims)
    bad_non_claims: dict[str, Any] = {}
    if non_claims_ok:
        for field in REQUIRED_FALSE_NON_CLAIMS:
            actual = declared_non_claims.get(field)
            if actual is not False:
                bad_non_claims[field] = actual
    else:
        bad_non_claims["declared_non_claims"] = declared_non_claims
    _add_check(
        checks,
        "required non-claims are explicit and false",
        non_claims_ok and not bad_non_claims,
        "all required non-claims false",
        bad_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _block_from_checks(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    failure = _first_failure(checks)
    if not failure:
        return None
    code = failure.get("block_code") or failure.get("failure_code")
    return {
        "blocked": True,
        "block_code": code,
        "block_reason": failure.get("check_name"),
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = request.get(
        "runtime_hosting_boundary_request_id",
        "post_successor_runtime_step_runtime_hosting_boundary_reference_review_001",
    )
    return {
        "post_successor_runtime_step_runtime_hosting_boundary_id": str(request_id),
        "post_successor_runtime_step_runtime_hosting_boundary_type": (
            "post_successor_runtime_step_runtime_hosting_boundary_result"
        ),
        "post_successor_runtime_step_runtime_hosting_boundary_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _result_body(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block: dict[str, Any] | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    postures = _default_postures(declared=recorded)
    for posture_field in POSTURE_FIELDS:
        if posture_field in request and _is_mapping(request[posture_field]):
            postures[posture_field] = _sanitize(request[posture_field])

    result: dict[str, Any] = {
        "post_successor_runtime_step_runtime_hosting_boundary_metadata": _metadata(request),
        "declared_runtime_hosting_boundary_question": {
            "runtime_hosting_boundary_request_id": request.get(
                "runtime_hosting_boundary_request_id"
            ),
            "runtime_hosting_boundary_question": request.get(
                "runtime_hosting_boundary_question"
            ),
            "runtime_hosting_boundary_intent": request.get(
                "runtime_hosting_boundary_intent"
            ),
        },
        "selected_successor_runtime_step_basis": _sanitize(
            request.get("selected_successor_runtime_step_basis", {})
        ),
        "selected_successor_runtime_step_terminal_summary_basis": _sanitize(
            request.get("selected_successor_runtime_step_terminal_summary_basis", {})
        ),
        "selected_successor_runtime_step_boundary_basis": _sanitize(
            request.get("selected_successor_runtime_step_boundary_basis", {})
        ),
        "selected_minimal_runtime_basis": _sanitize(
            request.get("selected_minimal_runtime_basis", {})
        ),
        "selected_runtime_boundary_basis": _sanitize(
            request.get("selected_runtime_boundary_basis", {})
        ),
        "selected_runtime_readiness_basis": _sanitize(
            request.get("selected_runtime_readiness_basis", {})
        ),
        "selected_portable_verification_final_completion_basis": _sanitize(
            request.get("selected_portable_verification_final_completion_basis", {})
        ),
        "selected_post_portable_verification_currentness_basis": _sanitize(
            request.get("selected_post_portable_verification_currentness_basis", {})
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _sanitize(
            request.get("selected_returned_second_carrier_capture_lineage_basis", {})
        ),
        **postures,
        "runtime_hosting_boundary_scope": list(_scope_values(request)),
        "runtime_hosting_boundary_checks": checks,
        "runtime_hosting_boundary_statement": _statement(recorded),
        "runtime_hosting_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
        "what_remains_open": _what_remains_open(),
        "non_claims": _non_claims_from_request(request),
        "outcome": outcome,
        "block": block,
    }
    result["post_successor_runtime_step_runtime_hosting_boundary_summary"] = (
        build_post_successor_runtime_step_runtime_hosting_boundary_summary(result)
    )
    return result


def _resolve_outcome(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> str:
    if _first_failure(checks):
        return OUTCOME_BLOCKED
    requested = request.get("requested_runtime_hosting_boundary_outcome")
    if requested in OUTCOME_FAMILY and requested != OUTCOME_RECORDED:
        return requested
    if request.get("runtime_hosting_boundary_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    if _present(request.get("additional_basis_context")):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if _present(request.get("not_recorded_basis")):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _forced_block_result(
    code: str,
    request: Mapping[str, Any] | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    base_request = _mapping_copy(request)
    base_request.setdefault(
        "runtime_hosting_boundary_request_id",
        "post_successor_runtime_step_runtime_hosting_boundary_blocked_request",
    )
    base_request.setdefault("runtime_hosting_boundary_question", None)
    base_request.setdefault("runtime_hosting_boundary_intent", None)
    checks = _add_runtime_hosting_boundary_checks(base_request, forced_block_code=code)
    block = {
        "blocked": True,
        "block_code": code,
        "block_reason": reason or "declared runtime-hosting-boundary request blocked",
    }
    return _result_body(base_request, checks, OUTCOME_BLOCKED, block)


def resolve_post_successor_runtime_step_runtime_hosting_boundary(
    declared_runtime_hosting_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded post-successor-runtime-step runtime-hosting boundary."""

    if declared_runtime_hosting_boundary_request is None:
        request = build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
    elif not _is_mapping(declared_runtime_hosting_boundary_request):
        return _forced_block_result(
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
            reason="declared request is not a mapping",
        )
    else:
        request = _mapping_copy(declared_runtime_hosting_boundary_request)

    checks = _add_runtime_hosting_boundary_checks(request)
    block = _block_from_checks(checks)
    outcome = _resolve_outcome(request, checks)
    if outcome == OUTCOME_BLOCKED and block is None:
        block = {
            "blocked": True,
            "block_code": "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
            "block_reason": "runtime-hosting-boundary review blocked",
        }
    return _result_body(request, checks, outcome, block)


def resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path(
    declared_runtime_hosting_boundary_request_path: Path | str,
) -> dict:
    """Resolve a declared runtime-hosting-boundary request loaded from JSON."""

    path = Path(declared_runtime_hosting_boundary_request_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return _forced_block_result(
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE",
            {
                "runtime_hosting_boundary_request_id": path.stem
                or "unreadable_runtime_hosting_boundary_request",
                "runtime_hosting_boundary_request_path": str(path),
            },
            reason=str(exc),
        )
    if not _is_mapping(payload):
        return _forced_block_result(
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
            {
                "runtime_hosting_boundary_request_id": path.stem
                or "malformed_runtime_hosting_boundary_request",
                "runtime_hosting_boundary_request_path": str(path),
            },
            reason="declared request JSON is not an object",
        )
    return resolve_post_successor_runtime_step_runtime_hosting_boundary(payload)


def build_post_successor_runtime_step_runtime_hosting_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary for a runtime-hosting-boundary result."""

    metadata = result.get("post_successor_runtime_step_runtime_hosting_boundary_metadata", {})
    declared = result.get("declared_runtime_hosting_boundary_question", {})
    checks = result.get("runtime_hosting_boundary_checks", [])
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    statement = result.get("runtime_hosting_boundary_statement", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block")
    successor_basis = result.get("selected_successor_runtime_step_basis", {})
    successor_boundary_basis = result.get("selected_successor_runtime_step_boundary_basis", {})
    minimal_basis = result.get("selected_minimal_runtime_basis", {})
    runtime_boundary_basis = result.get("selected_runtime_boundary_basis", {})
    runtime_readiness_basis = result.get("selected_runtime_readiness_basis", {})
    final_basis = result.get("selected_portable_verification_final_completion_basis", {})
    currentness_basis = result.get("selected_post_portable_verification_currentness_basis", {})

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "request_id": declared.get("runtime_hosting_boundary_request_id")
        or metadata.get("post_successor_runtime_step_runtime_hosting_boundary_id"),
        "question": declared.get("runtime_hosting_boundary_question"),
        "intent": declared.get("runtime_hosting_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get(
            "post_successor_runtime_step_runtime_hosting_boundary_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "selected_successor_runtime_step_outcome": successor_basis.get("outcome"),
        "selected_successor_runtime_step_result_version": successor_basis.get(
            "result_version"
        ),
        "selected_successor_runtime_step_failed_check_count": successor_basis.get(
            "failed_check_count"
        ),
        "selected_successor_runtime_step_boundary_outcome": successor_boundary_basis.get(
            "outcome"
        ),
        "selected_successor_runtime_step_boundary_result_version": successor_boundary_basis.get(
            "result_version"
        ),
        "selected_successor_runtime_step_boundary_failed_check_count": successor_boundary_basis.get(
            "failed_check_count"
        ),
        "selected_minimal_runtime_outcome": minimal_basis.get("outcome"),
        "selected_minimal_runtime_result_version": minimal_basis.get("result_version"),
        "selected_minimal_runtime_failed_check_count": minimal_basis.get(
            "failed_check_count"
        ),
        "selected_runtime_boundary_outcome": runtime_boundary_basis.get("outcome"),
        "selected_runtime_boundary_result_version": runtime_boundary_basis.get(
            "result_version"
        ),
        "selected_runtime_boundary_failed_check_count": runtime_boundary_basis.get(
            "failed_check_count"
        ),
        "selected_runtime_readiness_outcome": runtime_readiness_basis.get("outcome"),
        "selected_runtime_readiness_result_version": runtime_readiness_basis.get(
            "result_version"
        ),
        "selected_runtime_readiness_failed_check_count": runtime_readiness_basis.get(
            "failed_check_count"
        ),
        "selected_final_completion_outcome": final_basis.get("outcome"),
        "selected_final_completion_result_version": final_basis.get("result_version"),
        "selected_final_completion_failed_check_count": final_basis.get(
            "failed_check_count"
        ),
        "selected_post_portable_currentness_surface_path": currentness_basis.get(
            "basis_path"
        ),
        "source_authority_currentness_deployment_public_release_operation_permission_follow_on_not_created": (
            statement.get("source_not_created") is True
            and statement.get("authority_not_created") is True
            and statement.get("currentness_not_created") is True
            and statement.get("deployment_not_created") is True
            and statement.get("public_release_not_created") is True
            and statement.get("operation_permission_not_created") is True
            and statement.get("follow_on_work_not_authorized") is True
        ),
        "no_runtime_hosting_ongoing_runtime_reusable_runtime_permission_continuation_self_continuation_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": (
            non_claims.get("runtime_hosting_created") is False
            and non_claims.get("ongoing_runtime_created") is False
            and non_claims.get("reusable_runtime_permission_created") is False
            and non_claims.get("continuation_authorized") is False
            and non_claims.get("self_continuation_authorized") is False
            and non_claims.get("runtime_daemon_created") is False
            and non_claims.get("runtime_loop_created") is False
            and non_claims.get("public_api_created") is False
            and non_claims.get("participant_facing_interface_created") is False
            and non_claims.get("distributed_network_behavior_created") is False
            and non_claims.get("source_created") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("deployment_created") is False
            and non_claims.get("public_release_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            field: non_claims.get(field) for field in REQUIRED_FALSE_NON_CLAIMS
        },
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = statement.get(field)
    return summary


def _ensure_allowed_output_path(path: Path) -> None:
    normalized = path.as_posix()
    output_root = OUTPUT_ROOT.as_posix().rstrip("/") + "/"
    if output_root in normalized or normalized.startswith(output_root):
        return
    for marker in PROHIBITED_OUTPUT_MARKERS:
        if marker in normalized:
            raise PostSuccessorRuntimeStepRuntimeHostingBoundaryError(
                f"refusing to write runtime-hosting-boundary result into prohibited root: {path}"
            )


def _next_available_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_post_successor_runtime_step_runtime_hosting_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded runtime-hosting-boundary result without overwriting."""

    if not _is_mapping(result):
        raise PostSuccessorRuntimeStepRuntimeHostingBoundaryError(
            "runtime-hosting-boundary result must be a mapping"
        )
    metadata = result.get(
        "post_successor_runtime_step_runtime_hosting_boundary_metadata", {}
    )
    request_id = (
        metadata.get("post_successor_runtime_step_runtime_hosting_boundary_id")
        if isinstance(metadata, Mapping)
        else None
    ) or "post_successor_runtime_step_runtime_hosting_boundary_result"
    filename = f"{request_id}__post_successor_runtime_step_runtime_hosting_boundary_result.json"
    path = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    if path.exists() and path.is_dir():
        path = path / filename
    _ensure_allowed_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _next_available_path(path)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_post_successor_runtime_step_runtime_hosting_boundary_request(
    runtime_hosting_boundary_request_id: str = (
        "post_successor_runtime_step_runtime_hosting_boundary_reference_review_001"
    ),
    runtime_hosting_boundary_question: str = CORE_QUESTION,
    runtime_hosting_boundary_intent: str = INTENT_RECORD,
    runtime_hosting_boundary_scope: Any = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared request that records cleanly by default."""

    successor_step_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/"
        "post_minimal_runtime_successor_runtime_step_reference_review_001__"
        "post_minimal_runtime_successor_runtime_step_result.json"
    )
    successor_boundary_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary/"
        "post_minimal_runtime_successor_runtime_step_boundary_reference_review_001__"
        "post_minimal_runtime_successor_runtime_step_boundary_result.json"
    )
    minimal_runtime_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/"
        "post_portable_verification_minimal_runtime_reference_review_001__"
        "post_portable_verification_minimal_runtime_result.json"
    )
    runtime_boundary_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/"
        "post_portable_verification_runtime_boundary_reference_review_001__"
        "post_portable_verification_runtime_boundary_result.json"
    )
    runtime_readiness_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/"
        "post_portable_verification_runtime_readiness_reference_review_001__"
        "post_portable_verification_runtime_readiness_result.json"
    )
    final_completion_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/"
        "portable_source_body_verification_final_completion_reference_review_001__"
        "portable_source_body_verification_final_completion_result.json"
    )
    currentness_path = "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md"

    postures = _default_postures(declared=True)
    non_claims = {field: False for field in REQUIRED_FALSE_NON_CLAIMS}
    request: dict[str, Any] = {
        "runtime_hosting_boundary_request_id": runtime_hosting_boundary_request_id,
        "runtime_hosting_boundary_question": runtime_hosting_boundary_question,
        "runtime_hosting_boundary_intent": runtime_hosting_boundary_intent,
        "selected_successor_runtime_step_basis": _default_basis(
            "post_minimal_runtime_successor_runtime_step_reference_review_001",
            successor_step_path,
            EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
            bounded_successor_runtime_step_recorded=True,
            bounded_successor_runtime_result_or_refusal_recorded=True,
            no_successor_after_successor_action_authorized=True,
            runtime_hosting_created=False,
            ongoing_runtime_created=False,
            reusable_runtime_permission_created=False,
            continuation_authorized=False,
            self_continuation_authorized=False,
            successor_runtime_step_treated_as_runtime_hosting=False,
            successor_runtime_step_treated_as_ongoing_runtime=False,
            successor_runtime_step_treated_as_reusable_runtime_permission=False,
            successor_runtime_step_treated_as_continuation=False,
            successor_runtime_step_treated_as_self_continuation=False,
            bounded_successor_runtime_result_or_refusal_authorized_hosting=False,
            follow_on_work_authorized=False,
        ),
        "selected_successor_runtime_step_terminal_summary_basis": {
            "basis_id": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_TERMINAL_SUMMARY_V0",
            "basis_path": "spec/POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_TERMINAL_SUMMARY_V0.md",
            "basis_role": "selected_standing_terminal_summary_basis",
            "runtime_hosting_not_created": True,
            "ongoing_runtime_not_created": True,
            "reusable_runtime_permission_not_created": True,
            "continuation_not_authorized": True,
            "self_continuation_not_authorized": True,
            "no_runtime_hosting_selected": True,
            "future_work_requires_separate_step_back_review": True,
            "future_work_requires_separately_bounded_specification": True,
            "reference_shape_preserved": True,
        },
        "selected_successor_runtime_step_boundary_basis": _default_basis(
            "post_minimal_runtime_successor_runtime_step_boundary_reference_review_001",
            successor_boundary_path,
            EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
        ),
        "selected_minimal_runtime_basis": _default_basis(
            "post_portable_verification_minimal_runtime_reference_review_001",
            minimal_runtime_path,
            EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        ),
        "selected_runtime_boundary_basis": _default_basis(
            "post_portable_verification_runtime_boundary_reference_review_001",
            runtime_boundary_path,
            EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        ),
        "selected_runtime_readiness_basis": _default_basis(
            "post_portable_verification_runtime_readiness_reference_review_001",
            runtime_readiness_path,
            EXPECTED_RUNTIME_READINESS_OUTCOME,
        ),
        "selected_portable_verification_final_completion_basis": _default_basis(
            "portable_source_body_verification_final_completion_reference_review_001",
            final_completion_path,
            EXPECTED_FINAL_COMPLETION_OUTCOME,
        ),
        "selected_post_portable_verification_currentness_basis": {
            "basis_id": "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0",
            "basis_path": currentness_path,
            "basis_role": "selected_currentness_compression_basis",
            "states_checkability_not_continuation": True,
            "authorized_next_work": False,
            "operative_currentness_created": False,
            "operation_permission_created": False,
            "reference_shape_preserved": True,
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "basis_id": "PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0",
            "basis_path": (
                "spec/"
                "PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
            ),
            "basis_role": "preserved_lineage_only",
            "runtime_basis": False,
            "reference_shape_preserved": True,
        },
        "runtime_hosting_boundary_scope": (
            list(SUPPORTED_SCOPE_VALUES)
            if runtime_hosting_boundary_scope is None
            else runtime_hosting_boundary_scope
        ),
        "declared_non_claims": non_claims,
        "selected_successor_runtime_step_result_path": successor_step_path,
        "selected_successor_runtime_step_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        "selected_successor_runtime_step_result_version": RESULT_VERSION,
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_successor_runtime_step_bounded_successor_runtime_step_recorded": True,
        "selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded": True,
        "selected_successor_runtime_step_no_successor_after_successor_action_authorized": True,
        "selected_successor_runtime_step_already_created_runtime_hosting": False,
        "selected_successor_runtime_step_already_created_ongoing_runtime": False,
        "selected_successor_runtime_step_already_created_reusable_runtime_permission": False,
        "selected_successor_runtime_step_already_authorized_continuation": False,
        "selected_successor_runtime_step_already_authorized_self_continuation": False,
        "selected_successor_runtime_step_treated_as_runtime_hosting": False,
        "selected_successor_runtime_step_treated_as_ongoing_runtime": False,
        "selected_successor_runtime_step_treated_as_reusable_runtime_permission": False,
        "selected_successor_runtime_step_treated_as_continuation": False,
        "selected_successor_runtime_step_treated_as_self_continuation": False,
        "selected_successor_runtime_step_authorized_future_work": False,
        "selected_bounded_successor_runtime_result_or_refusal_authorized_hosting": False,
        "selected_successor_runtime_step_boundary_result_path": successor_boundary_path,
        "selected_successor_runtime_step_boundary_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
        "selected_successor_runtime_step_boundary_result_version": RESULT_VERSION,
        "selected_successor_runtime_step_boundary_failed_check_count": 0,
        "selected_minimal_runtime_result_path": minimal_runtime_path,
        "selected_minimal_runtime_result_outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        "selected_minimal_runtime_result_version": RESULT_VERSION,
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_path": runtime_boundary_path,
        "selected_runtime_boundary_result_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "selected_runtime_boundary_result_version": RESULT_VERSION,
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_path": runtime_readiness_path,
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_path": final_completion_path,
        "selected_portable_verification_final_completion_result_outcome": EXPECTED_FINAL_COMPLETION_OUTCOME,
        "selected_portable_verification_final_completion_result_version": RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": currentness_path,
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "runtime_hosting_boundary_created_before_review": False,
        "selected_basis_not_reference_shaped": False,
        "predecessor_failure_evidence_preserved": True,
        "requested_runtime_hosting_boundary_outcome": OUTCOME_RECORDED,
    }
    request.update(postures)
    for field in REQUIRED_FALSE_NON_CLAIMS:
        request[field] = False
    request.update(overrides)
    return request
