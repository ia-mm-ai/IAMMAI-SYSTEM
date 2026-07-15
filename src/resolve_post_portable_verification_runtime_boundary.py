"""Post-portable-verification runtime-boundary resolver.

This module records one bounded runtime-boundary posture downstream of
post-portable-verification runtime-readiness. It does not create runtime,
runtime step, continuation, source transfer, source receipt, reception
authorization, source, authority, currentness, deployment, public release,
operation permission, reusable permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class PostPortableVerificationRuntimeBoundaryError(Exception):
    """Bounded error for runtime-boundary request and artifact handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_portable_verification_runtime_boundary"

OUTCOME_RECORDED = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary"
)

CORE_QUESTION = (
    "Can the clean post-portable-verification runtime-readiness basis be "
    "bounded for one future minimal-runtime step review without creating "
    "runtime, runtime step, continuation, source transfer, source receipt, "
    "reception authorization, source, authority, currentness, deployment, "
    "public release, operation permission, reusable permission, derivative "
    "reception, vessel relation, another reception request, adoption, "
    "receiving-context governance, publication flow, or follow-on work?"
)

INTENT_RECORD = "RECORD_POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

EXPECTED_RUNTIME_READINESS_OUTCOME = (
    "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED"
)
EXPECTED_FINAL_COMPLETION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED"
)

SUPPORTED_SCOPE_VALUES = (
    "RUNTIME_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_MINIMAL_RUNTIME_STEP_REVIEW_DECLARED",
    "RUNTIME_READINESS_BASIS_PRESERVED",
    "RUNTIME_READINESS_NOT_RUNTIME",
    "RUNTIME_READINESS_NOT_RUNTIME_STEP",
    "RUNTIME_READINESS_NOT_CONTINUATION",
    "RUNTIME_BOUNDARY_NOT_RUNTIME",
    "RUNTIME_BOUNDARY_NOT_RUNTIME_STEP",
    "RUNTIME_BOUNDARY_NOT_CONTINUATION",
    "RUNTIME_NOT_CREATED",
    "RUNTIME_STEP_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
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
    "NO_RUNTIME_INFERENCE",
    "NO_RUNTIME_STEP_INFERENCE",
    "NO_CONTINUATION_INFERENCE",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_DEPLOYMENT_INFERENCE",
    "NO_PUBLIC_RELEASE_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "HIDDEN_REPO_STATE_EXCLUDED",
    "HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
)
SUPPORTED_RUNTIME_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "runtime_created",
    "runtime_step_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_boundary_treated_as_runtime",
    "runtime_boundary_treated_as_runtime_step",
    "runtime_boundary_treated_as_continuation",
    "runtime_boundary_treated_as_source_transfer",
    "runtime_boundary_treated_as_source_receipt",
    "runtime_boundary_treated_as_reception_authorization",
    "runtime_boundary_treated_as_source",
    "runtime_boundary_treated_as_authority",
    "runtime_boundary_treated_as_currentness",
    "runtime_boundary_treated_as_deployment",
    "runtime_boundary_treated_as_public_release",
    "runtime_boundary_treated_as_operation_permission",
    "runtime_boundary_treated_as_reusable_permission",
    "runtime_boundary_treated_as_follow_on_work",
    "runtime_readiness_treated_as_runtime",
    "runtime_readiness_treated_as_runtime_step",
    "runtime_readiness_treated_as_continuation",
    "artifact_existence_treated_as_runtime_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_boundary_authority",
    "repo_local_availability_treated_as_runtime_boundary_authority",
    "hidden_repo_state_used_as_runtime_boundary_content",
    "hidden_repo_state_used_as_runtime_boundary_authority",
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
    "runtime_boundary_recorded",
    "one_future_minimal_runtime_step_review_declared",
    "runtime_readiness_basis_preserved",
    "runtime_readiness_not_runtime",
    "runtime_readiness_not_runtime_step",
    "runtime_readiness_not_continuation",
    "runtime_boundary_not_runtime",
    "runtime_boundary_not_runtime_step",
    "runtime_boundary_not_continuation",
    "runtime_not_created",
    "runtime_step_not_created",
    "continuation_not_authorized",
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
    "hidden_repo_state_not_used_as_runtime_boundary_authority",
    "repo_local_availability_not_runtime_boundary_authority",
    "artifact_existence_not_runtime_boundary_authority",
    "latest_file_posture_not_runtime_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

RECORDING_STATEMENT_FIELDS = (
    "runtime_boundary_recorded",
    "one_future_minimal_runtime_step_review_declared",
)

BLOCK_CODES = (
    "RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    "RUNTIME_BOUNDARY_REQUEST_DECLARED_BLOCK",
    "RUNTIME_READINESS_BASIS_MISSING",
    "RUNTIME_READINESS_NOT_RECORDED",
    "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
    "RUNTIME_READINESS_VERSION_NOT_0_1_0",
    "RUNTIME_READINESS_DID_NOT_RECORD_BOUNDED_READINESS",
    "RUNTIME_READINESS_ALREADY_CREATED_RUNTIME",
    "RUNTIME_READINESS_ALREADY_CREATED_RUNTIME_STEP",
    "RUNTIME_READINESS_ALREADY_AUTHORIZED_CONTINUATION",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME_BOUNDARY",
    "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP",
    "RUNTIME_READINESS_TREATED_AS_CONTINUATION",
    "RUNTIME_READINESS_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_READINESS_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_READINESS_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_READINESS_TREATED_AS_SOURCE",
    "RUNTIME_READINESS_TREATED_AS_AUTHORITY",
    "RUNTIME_READINESS_TREATED_AS_CURRENTNESS",
    "RUNTIME_READINESS_TREATED_AS_DEPLOYMENT",
    "RUNTIME_READINESS_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_READINESS_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_READINESS_TREATED_AS_REUSABLE_PERMISSION",
    "RUNTIME_READINESS_TREATED_AS_FOLLOW_ON_WORK",
    "RUNTIME_READINESS_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_BOUNDARY_CREATED_BEFORE_REVIEW",
    "RUNTIME_CREATED",
    "RUNTIME_STEP_CREATED",
    "CONTINUATION_AUTHORIZED",
    "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME",
    "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME_STEP",
    "RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
    "RUNTIME_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_BOUNDARY_TREATED_AS_SOURCE",
    "RUNTIME_BOUNDARY_TREATED_AS_AUTHORITY",
    "RUNTIME_BOUNDARY_TREATED_AS_CURRENTNESS",
    "RUNTIME_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "RUNTIME_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "RUNTIME_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    "FINAL_COMPLETION_BASIS_MISSING",
    "FINAL_COMPLETION_NOT_RECORDED",
    "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_VERSION_NOT_0_1_0",
)

SELECTED_BASIS_FIELDS = (
    "selected_runtime_readiness_basis",
    "selected_runtime_readiness_terminal_summary_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "runtime_boundary_spec_only_posture",
    "one_future_minimal_runtime_step_review_posture",
    "runtime_readiness_basis_preserved_posture",
    "runtime_readiness_not_runtime_posture",
    "runtime_readiness_not_runtime_step_posture",
    "runtime_readiness_not_continuation_posture",
    "runtime_boundary_not_runtime_posture",
    "runtime_boundary_not_runtime_step_posture",
    "runtime_boundary_not_continuation_posture",
    "runtime_not_created_posture",
    "runtime_step_not_created_posture",
    "continuation_not_authorized_posture",
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
    "repo_local_availability_not_runtime_boundary_authority_posture",
    "artifact_existence_not_runtime_boundary_authority_posture",
    "latest_file_posture_not_runtime_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

SENSITIVE_CONTENT_KEYS = (
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
    "raw_runtime_body",
    "capture_body",
    "runtime_readiness_body",
    "runtime_boundary_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_READINESS_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = frozenset(
    SUPPORTED_SCOPE_VALUES
    + OUTCOME_FAMILY
    + BLOCK_CODES
    + REQUIRED_FALSE_NON_CLAIMS
    + ALLOWED_TRUE_RECORDED_FIELDS
    + POSTURE_FIELDS
    + SELECTED_BASIS_FIELDS
    + SUPPORTED_INTENTS
)

NON_CLAIM_BLOCK_CODE = {
    "runtime_created": "RUNTIME_CREATED",
    "runtime_step_created": "RUNTIME_STEP_CREATED",
    "continuation_authorized": "CONTINUATION_AUTHORIZED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
    "runtime_boundary_treated_as_runtime": "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME",
    "runtime_boundary_treated_as_runtime_step": (
        "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME_STEP"
    ),
    "runtime_boundary_treated_as_continuation": (
        "RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION"
    ),
    "runtime_boundary_treated_as_source_transfer": (
        "RUNTIME_BOUNDARY_TREATED_AS_SOURCE_TRANSFER"
    ),
    "runtime_boundary_treated_as_source_receipt": (
        "RUNTIME_BOUNDARY_TREATED_AS_SOURCE_RECEIPT"
    ),
    "runtime_boundary_treated_as_reception_authorization": (
        "RUNTIME_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION"
    ),
    "runtime_boundary_treated_as_source": "RUNTIME_BOUNDARY_TREATED_AS_SOURCE",
    "runtime_boundary_treated_as_authority": "RUNTIME_BOUNDARY_TREATED_AS_AUTHORITY",
    "runtime_boundary_treated_as_currentness": (
        "RUNTIME_BOUNDARY_TREATED_AS_CURRENTNESS"
    ),
    "runtime_boundary_treated_as_deployment": (
        "RUNTIME_BOUNDARY_TREATED_AS_DEPLOYMENT"
    ),
    "runtime_boundary_treated_as_public_release": (
        "RUNTIME_BOUNDARY_TREATED_AS_PUBLIC_RELEASE"
    ),
    "runtime_boundary_treated_as_operation_permission": (
        "RUNTIME_BOUNDARY_TREATED_AS_OPERATION_PERMISSION"
    ),
    "runtime_boundary_treated_as_reusable_permission": (
        "RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION"
    ),
    "runtime_boundary_treated_as_follow_on_work": (
        "RUNTIME_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK"
    ),
    "runtime_readiness_treated_as_runtime": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
    "runtime_readiness_treated_as_runtime_step": (
        "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP"
    ),
    "runtime_readiness_treated_as_continuation": (
        "RUNTIME_READINESS_TREATED_AS_CONTINUATION"
    ),
    "artifact_existence_treated_as_runtime_boundary_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "latest_file_posture_treated_as_runtime_boundary_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "repo_local_availability_treated_as_runtime_boundary_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "hidden_repo_state_used_as_runtime_boundary_content": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT"
    ),
    "hidden_repo_state_used_as_runtime_boundary_authority": (
        "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_AUTHORITY"
    ),
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


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


def _truth(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "declared", "preserved"}
    if _is_mapping(value):
        return any(
            value.get(key) is True
            for key in (
                "declared",
                "preserved",
                "recorded",
                "not_created",
                "not_authorized",
                "excluded",
                "blocked",
            )
        )
    return False


def _sensitive_key(key: str) -> bool:
    normalized = str(key)
    return normalized in SENSITIVE_CONTENT_KEYS or normalized.endswith("_body")


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in HOSTILE_SENTINELS)


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and _sensitive_key(key):
        return "[bounded-redacted-raw-or-hidden-state]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if _contains_hostile_sentinel(value):
            return "[bounded-redacted-raw-or-hidden-state]"
        return value
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, datetime):
        return value.isoformat()
    if _is_mapping(value):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_sanitize(item) for item in value]
    if isinstance(value, (bool, int, float)) or value is None:
        return value
    return str(value)


def _sanitize_mapping(value: Any) -> dict[str, Any]:
    if not _is_mapping(value):
        return {}
    sanitized = _sanitize(copy.deepcopy(value))
    if _is_mapping(sanitized):
        return dict(sanitized)
    return {}


def _request_value(
    request: Mapping[str, Any],
    key: str,
    *,
    sections: tuple[str, ...] = SELECTED_BASIS_FIELDS,
    default: Any = None,
) -> Any:
    if key in request:
        return request[key]
    for section_name in sections:
        section = request.get(section_name)
        if _is_mapping(section) and key in section:
            return section[key]
    return default


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if passed:
        record["failure_code"] = None
        record["block_code"] = None
    else:
        record["failure_code"] = block_code
        record["block_code"] = block_code
    return record


def _first_failed_check(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _safe_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = request.get("declared_non_claims")
    if _is_mapping(declared):
        return dict(copy.deepcopy(declared))
    return {}


def _request_id(request: Mapping[str, Any] | None) -> str:
    if _is_mapping(request):
        value = request.get("runtime_boundary_request_id")
        if isinstance(value, str) and value.strip():
            return value.strip()
    return "post_portable_verification_runtime_boundary_request"


def _scope_values(request: Mapping[str, Any]) -> list[str]:
    value = request.get("runtime_boundary_scope")
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    if _is_mapping(value):
        declared = value.get("scope_values")
        if isinstance(declared, (list, tuple, set)):
            return [str(item) for item in declared]
    return [str(value)]


def _posture(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "declared": True,
        "preserved": True,
        "bounded_runtime_boundary_only": True,
    }


def _reference_basis(
    *,
    basis_name: str,
    path: str,
    role: str,
    **extra: Any,
) -> dict[str, Any]:
    basis = {
        "basis_name": basis_name,
        "basis_path": path,
        "basis_role": role,
        "reference_shape": "path-and-posture-only",
        "raw_full_prior_artifact_body_returned": False,
        "hidden_repo_state_used": False,
    }
    basis.update(extra)
    return basis


def _runtime_boundary_statement(recorded: bool) -> dict[str, bool]:
    statement: dict[str, bool] = {}
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        if field in RECORDING_STATEMENT_FIELDS:
            statement[field] = bool(recorded)
        else:
            statement[field] = True
    return statement


def _runtime_boundary_non_meaning() -> dict[str, bool]:
    return {
        "runtime_boundary_is_runtime": False,
        "runtime_boundary_is_runtime_step": False,
        "runtime_boundary_is_continuation": False,
        "runtime_boundary_is_runtime_hosting": False,
        "runtime_boundary_is_source_transfer": False,
        "runtime_boundary_is_source_receipt": False,
        "runtime_boundary_is_reception_authorization": False,
        "runtime_boundary_is_source": False,
        "runtime_boundary_is_authority": False,
        "runtime_boundary_is_currentness": False,
        "runtime_boundary_is_deployment": False,
        "runtime_boundary_is_public_release": False,
        "runtime_boundary_is_operation_permission": False,
        "runtime_boundary_is_reusable_permission": False,
        "runtime_boundary_is_follow_on_work": False,
        "runtime_readiness_is_runtime": False,
        "runtime_readiness_is_runtime_step": False,
        "runtime_readiness_is_continuation": False,
        "runtime_exists_here": False,
        "runtime_step_exists_here": False,
        "continuation_is_authorized_here": False,
        "artifact_existence_is_runtime_boundary_authority": False,
        "repo_local_availability_is_runtime_boundary_authority": False,
        "latest_file_posture_is_runtime_boundary_authority": False,
        "hidden_repo_state_is_runtime_boundary_authority": False,
    }


def _what_remains_open() -> list[str]:
    return [
        "runtime-boundary test",
        "runtime-boundary live artifact",
        "runtime-boundary terminal summary, if needed",
        "minimal runtime specification",
        "minimal runtime resolver/test/live artifact",
        "runtime result/refusal artifact",
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
        "runtime hosting",
        "deployment",
        "public release",
        "continuation",
        "publication flow",
        "reusable permission",
        "successor reception request",
        "follow-on work",
    ]


def _posture_block_code(field: str) -> str:
    mapping = {
        "runtime_boundary_spec_only_posture": "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME",
        "one_future_minimal_runtime_step_review_posture": (
            "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME_STEP"
        ),
        "runtime_readiness_basis_preserved_posture": "RUNTIME_READINESS_BASIS_MISSING",
        "runtime_readiness_not_runtime_posture": "RUNTIME_READINESS_TREATED_AS_RUNTIME",
        "runtime_readiness_not_runtime_step_posture": (
            "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP"
        ),
        "runtime_readiness_not_continuation_posture": (
            "RUNTIME_READINESS_TREATED_AS_CONTINUATION"
        ),
        "runtime_boundary_not_runtime_posture": "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME",
        "runtime_boundary_not_runtime_step_posture": (
            "RUNTIME_BOUNDARY_TREATED_AS_RUNTIME_STEP"
        ),
        "runtime_boundary_not_continuation_posture": (
            "RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION"
        ),
        "runtime_not_created_posture": "RUNTIME_CREATED",
        "runtime_step_not_created_posture": "RUNTIME_STEP_CREATED",
        "continuation_not_authorized_posture": "CONTINUATION_AUTHORIZED",
        "source_transfer_not_created_posture": "SOURCE_TRANSFER_OCCURRED",
        "source_receipt_not_created_posture": "SOURCE_RECEIPT_OCCURRED",
        "reception_authorization_not_created_posture": "RECEPTION_AUTHORIZATION_CREATED",
        "source_not_created_posture": "SOURCE_CREATED",
        "authority_not_created_posture": "AUTHORITY_CREATED",
        "currentness_not_created_posture": "CURRENTNESS_CREATED",
        "deployment_not_created_posture": "DEPLOYMENT_CREATED",
        "public_release_not_created_posture": "PUBLIC_RELEASE_CREATED",
        "operation_permission_not_created_posture": "OPERATION_PERMISSION_CREATED",
        "reusable_permission_not_created_posture": "REUSABLE_PERMISSION_CREATED",
        "follow_on_work_not_authorized_posture": "FOLLOW_ON_WORK_AUTHORIZED",
        "hidden_repo_state_excluded_posture": (
            "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT"
        ),
        "repo_local_availability_not_runtime_boundary_authority_posture": (
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
        ),
        "artifact_existence_not_runtime_boundary_authority_posture": (
            "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
        ),
        "latest_file_posture_not_runtime_boundary_authority_posture": (
            "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY"
        ),
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "raw_full_prior_artifact_body_not_returned_posture": (
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
        ),
        "official_enum_scope_strings_not_redacted_posture": (
            "UNSUPPORTED_RUNTIME_BOUNDARY_SCOPE"
        ),
        "hostile_raw_body_content_contained_posture": (
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"
        ),
        "predecessor_failure_evidence_preserved_posture": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
    }
    return mapping.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")


def _add_runtime_boundary_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    forced_block_code: str | None = None,
) -> None:
    if forced_block_code is not None:
        checks.append(
            _check(
                "declared runtime-boundary request readable and mapping-shaped",
                False,
                "mapping request",
                "missing or malformed request",
                forced_block_code,
            )
        )
        return

    question = request.get("runtime_boundary_question")
    checks.append(
        _check(
            "runtime-boundary question declared",
            question == CORE_QUESTION,
            CORE_QUESTION,
            question,
            "RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
        )
    )

    intent = request.get("runtime_boundary_intent")
    checks.append(
        _check(
            "runtime-boundary intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "runtime-boundary request did not declare blocking intent",
            intent != INTENT_BLOCK,
            "not BLOCK_POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY",
            intent,
            "RUNTIME_BOUNDARY_REQUEST_DECLARED_BLOCK",
        )
    )

    scope_values = _scope_values(request)
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_RUNTIME_BOUNDARY_SCOPE
    ]
    checks.append(
        _check(
            "runtime-boundary scope supported",
            bool(scope_values) and not unsupported_scope,
            SUPPORTED_RUNTIME_BOUNDARY_SCOPE,
            scope_values,
            "UNSUPPORTED_RUNTIME_BOUNDARY_SCOPE",
        )
    )

    runtime_readiness_basis = request.get("selected_runtime_readiness_basis")
    checks.append(
        _check(
            "runtime-readiness basis declared",
            _present(runtime_readiness_basis),
            "selected runtime-readiness basis",
            runtime_readiness_basis,
            "RUNTIME_READINESS_BASIS_MISSING",
        )
    )

    terminal_summary_basis = request.get("selected_runtime_readiness_terminal_summary_basis")
    checks.append(
        _check(
            "runtime-readiness terminal summary basis declared",
            _present(terminal_summary_basis),
            "selected runtime-readiness terminal summary basis",
            terminal_summary_basis,
            "RUNTIME_READINESS_BASIS_MISSING",
        )
    )

    checks.append(
        _check(
            "runtime-readiness outcome recorded",
            _request_value(request, "selected_runtime_readiness_result_outcome")
            == EXPECTED_RUNTIME_READINESS_OUTCOME,
            EXPECTED_RUNTIME_READINESS_OUTCOME,
            _request_value(request, "selected_runtime_readiness_result_outcome"),
            "RUNTIME_READINESS_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "runtime-readiness result version 0.1.0",
            _request_value(request, "selected_runtime_readiness_result_version")
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(request, "selected_runtime_readiness_result_version"),
            "RUNTIME_READINESS_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "runtime-readiness failed checks zero",
            _as_int(
                _request_value(request, "selected_runtime_readiness_failed_check_count")
            )
            == 0,
            0,
            _request_value(request, "selected_runtime_readiness_failed_check_count"),
            "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "runtime-readiness recorded bounded runtime-readiness",
            _request_value(
                request,
                "selected_runtime_readiness_bounded_runtime_readiness_recorded",
            )
            is True,
            True,
            _request_value(
                request,
                "selected_runtime_readiness_bounded_runtime_readiness_recorded",
            ),
            "RUNTIME_READINESS_DID_NOT_RECORD_BOUNDED_READINESS",
        )
    )

    runtime_readiness_false_checks = (
        (
            "runtime-readiness did not already create runtime",
            "selected_runtime_readiness_already_created_runtime",
            "RUNTIME_READINESS_ALREADY_CREATED_RUNTIME",
        ),
        (
            "runtime-readiness did not already create runtime step",
            "selected_runtime_readiness_already_created_runtime_step",
            "RUNTIME_READINESS_ALREADY_CREATED_RUNTIME_STEP",
        ),
        (
            "runtime-readiness did not authorize continuation",
            "selected_runtime_readiness_already_authorized_continuation",
            "RUNTIME_READINESS_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "runtime-readiness did not treat readiness as runtime",
            "selected_runtime_readiness_treated_as_runtime",
            "RUNTIME_READINESS_TREATED_AS_RUNTIME",
        ),
        (
            "runtime-readiness did not treat readiness as runtime step",
            "selected_runtime_readiness_treated_as_runtime_step",
            "RUNTIME_READINESS_TREATED_AS_RUNTIME_STEP",
        ),
        (
            "runtime-readiness did not treat readiness as continuation",
            "selected_runtime_readiness_treated_as_continuation",
            "RUNTIME_READINESS_TREATED_AS_CONTINUATION",
        ),
        (
            "runtime-readiness did not treat readiness as source transfer",
            "selected_runtime_readiness_treated_as_source_transfer",
            "RUNTIME_READINESS_TREATED_AS_SOURCE_TRANSFER",
        ),
        (
            "runtime-readiness did not treat readiness as source receipt",
            "selected_runtime_readiness_treated_as_source_receipt",
            "RUNTIME_READINESS_TREATED_AS_SOURCE_RECEIPT",
        ),
        (
            "runtime-readiness did not treat readiness as reception authorization",
            "selected_runtime_readiness_treated_as_reception_authorization",
            "RUNTIME_READINESS_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        (
            "runtime-readiness did not treat readiness as source",
            "selected_runtime_readiness_treated_as_source",
            "RUNTIME_READINESS_TREATED_AS_SOURCE",
        ),
        (
            "runtime-readiness did not treat readiness as authority",
            "selected_runtime_readiness_treated_as_authority",
            "RUNTIME_READINESS_TREATED_AS_AUTHORITY",
        ),
        (
            "runtime-readiness did not treat readiness as currentness",
            "selected_runtime_readiness_treated_as_currentness",
            "RUNTIME_READINESS_TREATED_AS_CURRENTNESS",
        ),
        (
            "runtime-readiness did not treat readiness as deployment",
            "selected_runtime_readiness_treated_as_deployment",
            "RUNTIME_READINESS_TREATED_AS_DEPLOYMENT",
        ),
        (
            "runtime-readiness did not treat readiness as public release",
            "selected_runtime_readiness_treated_as_public_release",
            "RUNTIME_READINESS_TREATED_AS_PUBLIC_RELEASE",
        ),
        (
            "runtime-readiness did not treat readiness as operation permission",
            "selected_runtime_readiness_treated_as_operation_permission",
            "RUNTIME_READINESS_TREATED_AS_OPERATION_PERMISSION",
        ),
        (
            "runtime-readiness did not treat readiness as reusable permission",
            "selected_runtime_readiness_treated_as_reusable_permission",
            "RUNTIME_READINESS_TREATED_AS_REUSABLE_PERMISSION",
        ),
        (
            "runtime-readiness did not treat readiness as follow-on work",
            "selected_runtime_readiness_treated_as_follow_on_work",
            "RUNTIME_READINESS_TREATED_AS_FOLLOW_ON_WORK",
        ),
        (
            "runtime-readiness did not authorize future work",
            "selected_runtime_readiness_authorized_future_work",
            "RUNTIME_READINESS_AUTHORIZED_FUTURE_WORK",
        ),
    )
    for name, key, block_code in runtime_readiness_false_checks:
        actual = _request_value(request, key, default=False)
        checks.append(_check(name, actual is not True, False, actual, block_code))

    top_level_false_checks = (
        (
            "runtime boundary not created before review",
            "runtime_boundary_created_before_review",
            "RUNTIME_BOUNDARY_CREATED_BEFORE_REVIEW",
        ),
        ("runtime not created", "runtime_created", "RUNTIME_CREATED"),
        ("runtime step not created", "runtime_step_created", "RUNTIME_STEP_CREATED"),
        (
            "continuation not authorized",
            "continuation_authorized",
            "CONTINUATION_AUTHORIZED",
        ),
    )
    for name, key, block_code in top_level_false_checks:
        actual = request.get(key, False)
        checks.append(_check(name, actual is not True, False, actual, block_code))

    runtime_boundary_treatment_checks = (
        "runtime_boundary_treated_as_runtime",
        "runtime_boundary_treated_as_runtime_step",
        "runtime_boundary_treated_as_continuation",
        "runtime_boundary_treated_as_source_transfer",
        "runtime_boundary_treated_as_source_receipt",
        "runtime_boundary_treated_as_reception_authorization",
        "runtime_boundary_treated_as_source",
        "runtime_boundary_treated_as_authority",
        "runtime_boundary_treated_as_currentness",
        "runtime_boundary_treated_as_deployment",
        "runtime_boundary_treated_as_public_release",
        "runtime_boundary_treated_as_operation_permission",
        "runtime_boundary_treated_as_reusable_permission",
        "runtime_boundary_treated_as_follow_on_work",
    )
    for key in runtime_boundary_treatment_checks:
        actual = request.get(key, False)
        checks.append(
            _check(
                key.replace("_", " "),
                actual is not True,
                False,
                actual,
                NON_CLAIM_BLOCK_CODE[key],
            )
        )

    final_completion_basis = request.get("selected_portable_verification_final_completion_basis")
    checks.append(
        _check(
            "portable verification final-completion basis declared",
            _present(final_completion_basis),
            "selected final-completion basis",
            final_completion_basis,
            "FINAL_COMPLETION_BASIS_MISSING",
        )
    )
    checks.append(
        _check(
            "portable verification final-completion outcome recorded",
            _request_value(
                request, "selected_portable_verification_final_completion_result_outcome"
            )
            == EXPECTED_FINAL_COMPLETION_OUTCOME,
            EXPECTED_FINAL_COMPLETION_OUTCOME,
            _request_value(
                request, "selected_portable_verification_final_completion_result_outcome"
            ),
            "FINAL_COMPLETION_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "portable verification final-completion version 0.1.0",
            _request_value(
                request, "selected_portable_verification_final_completion_result_version"
            )
            == RESULT_VERSION,
            RESULT_VERSION,
            _request_value(
                request, "selected_portable_verification_final_completion_result_version"
            ),
            "FINAL_COMPLETION_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "portable verification final-completion failed checks zero",
            _as_int(
                _request_value(
                    request,
                    "selected_portable_verification_final_completion_failed_check_count",
                )
            )
            == 0,
            0,
            _request_value(
                request,
                "selected_portable_verification_final_completion_failed_check_count",
            ),
            "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
        )
    )

    currentness_basis = request.get("selected_post_portable_verification_currentness_basis")
    checks.append(
        _check(
            "post-portable currentness surface basis declared",
            _present(currentness_basis),
            "selected post-portable currentness surface basis",
            currentness_basis,
            "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
        )
    )
    checks.append(
        _check(
            "post-portable currentness surface states checkability not continuation",
            _request_value(
                request,
                "selected_post_portable_currentness_surface_states_checkability_not_continuation",
            )
            is True,
            True,
            _request_value(
                request,
                "selected_post_portable_currentness_surface_states_checkability_not_continuation",
            ),
            "RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
        )
    )
    checks.append(
        _check(
            "post-portable currentness surface does not authorize next work",
            _request_value(
                request,
                "selected_post_portable_currentness_surface_authorized_next_work",
                default=False,
            )
            is not True,
            False,
            _request_value(
                request,
                "selected_post_portable_currentness_surface_authorized_next_work",
                default=False,
            ),
            "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
        )
    )

    predecessor_preserved = request.get("predecessor_failure_evidence_preserved", True)
    predecessor_failed = (
        request.get("predecessor_failure_repaired") is True
        or request.get("predecessor_failure_hidden") is True
        or request.get("predecessor_failure_claimed_passed") is True
    )
    checks.append(
        _check(
            "predecessor failure evidence visible and unrepaired",
            predecessor_preserved is True and not predecessor_failed,
            "visible, unrepaired, unhidden, not claimed passed",
            {
                "predecessor_failure_evidence_preserved": predecessor_preserved,
                "predecessor_failure_repaired": request.get(
                    "predecessor_failure_repaired", False
                ),
                "predecessor_failure_hidden": request.get(
                    "predecessor_failure_hidden", False
                ),
                "predecessor_failure_claimed_passed": request.get(
                    "predecessor_failure_claimed_passed", False
                ),
            },
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )

    for field in POSTURE_FIELDS:
        actual = request.get(field)
        checks.append(
            _check(
                field.replace("_", " "),
                _truth(actual),
                "declared preserved runtime-boundary posture",
                actual,
                _posture_block_code(field),
            )
        )

    checks.append(
        _check(
            "hidden repo state not used as runtime-boundary authority",
            request.get("hidden_repo_state_used_as_runtime_boundary_authority", False)
            is not True,
            False,
            request.get("hidden_repo_state_used_as_runtime_boundary_authority", False),
            "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "hidden repo state not used as runtime-boundary content",
            request.get("hidden_repo_state_used_as_runtime_boundary_content", False)
            is not True,
            False,
            request.get("hidden_repo_state_used_as_runtime_boundary_content", False),
            "HIDDEN_REPO_STATE_USED_AS_RUNTIME_BOUNDARY_CONTENT",
        )
    )
    checks.append(
        _check(
            "repo-local availability not runtime-boundary authority",
            request.get("repo_local_availability_treated_as_runtime_boundary_authority", False)
            is not True,
            False,
            request.get(
                "repo_local_availability_treated_as_runtime_boundary_authority", False
            ),
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "artifact existence not runtime-boundary authority",
            request.get("artifact_existence_treated_as_runtime_boundary_authority", False)
            is not True,
            False,
            request.get("artifact_existence_treated_as_runtime_boundary_authority", False),
            "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "latest file posture not runtime-boundary authority",
            request.get("latest_file_posture_treated_as_runtime_boundary_authority", False)
            is not True,
            False,
            request.get("latest_file_posture_treated_as_runtime_boundary_authority", False),
            "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_BOUNDARY_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "selected basis reference-shaped",
            request.get("reference_shaped_input_posture", True) is not False,
            True,
            request.get("reference_shaped_input_posture", True),
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )
    )
    checks.append(
        _check(
            "raw full prior artifact body not returned",
            request.get("raw_full_prior_artifact_body_returned", False) is not True,
            False,
            request.get("raw_full_prior_artifact_body_returned", False),
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        )
    )
    checks.append(
        _check(
            "official enum scope strings not redacted",
            all(value in OFFICIAL_STRINGS for value in scope_values),
            "official scope strings preserved",
            scope_values,
            "UNSUPPORTED_RUNTIME_BOUNDARY_SCOPE",
        )
    )
    checks.append(
        _check(
            "hostile raw body content contained",
            _truth(request.get("hostile_raw_body_content_contained_posture")),
            True,
            request.get("hostile_raw_body_content_contained_posture"),
            "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        )
    )
    checks.append(
        _check(
            "consumed token remains closed",
            request.get("consumed_request_reopened", False) is not True,
            False,
            request.get("consumed_request_reopened", False),
            "CONSUMED_REQUEST_REOPENED",
        )
    )
    checks.append(
        _check(
            "authorization token reuse blocked",
            request.get("authorization_token_reused", False) is not True,
            False,
            request.get("authorization_token_reused", False),
            "AUTHORIZATION_TOKEN_REUSED",
        )
    )

    declared_non_claims = _declared_non_claims(request)
    for field in REQUIRED_FALSE_NON_CLAIMS:
        actual = declared_non_claims.get(field)
        checks.append(
            _check(
                f"required non-claim false: {field}",
                actual is False,
                False,
                actual,
                NON_CLAIM_BLOCK_CODE.get(field, "NON_CLAIM_MISSING_OR_FLIPPED"),
            )
        )


def _block_from_failed_check(
    failed_check: dict[str, Any] | None,
    request: Mapping[str, Any],
) -> dict[str, Any] | None:
    if failed_check is None:
        return None
    block_code = failed_check.get("block_code") or failed_check.get("failure_code")
    if block_code not in BLOCK_CODES:
        block_code = "NON_CLAIM_MISSING_OR_FLIPPED"
    return {
        "blocked": True,
        "block_code": block_code,
        "block_reason": _sanitize(
            request.get("block_reason")
            or failed_check.get("check_name")
            or "runtime-boundary review blocked"
        ),
    }


def _summary_request_value(result: Mapping[str, Any], key: str) -> Any:
    for section_name in SELECTED_BASIS_FIELDS:
        section = result.get(section_name)
        if _is_mapping(section) and key in section:
            return section[key]
    return None


def build_post_portable_verification_runtime_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("runtime_boundary_checks")
    if not isinstance(checks, list):
        checks = []
    passed_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed"))
    failed_count = sum(
        1 for check in checks if _is_mapping(check) and check.get("passed") is not True
    )
    metadata = result.get("post_portable_verification_runtime_boundary_metadata")
    if not _is_mapping(metadata):
        metadata = {}
    question = result.get("declared_runtime_boundary_question")
    if not _is_mapping(question):
        question = {}
    statement = result.get("runtime_boundary_statement")
    if not _is_mapping(statement):
        statement = {}
    non_claims = result.get("non_claims")
    if not _is_mapping(non_claims):
        non_claims = {}
    block = result.get("block")
    if not _is_mapping(block):
        block = {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("runtime_boundary_request_id")
        or metadata.get("post_portable_verification_runtime_boundary_id"),
        "question": question.get("runtime_boundary_question"),
        "intent": question.get("runtime_boundary_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata.get("post_portable_verification_runtime_boundary_version"),
        "resolver_module": metadata.get("resolver_module"),
        "selected_runtime_readiness_outcome": _summary_request_value(
            result, "selected_runtime_readiness_result_outcome"
        ),
        "selected_runtime_readiness_version": _summary_request_value(
            result, "selected_runtime_readiness_result_version"
        ),
        "selected_runtime_readiness_failed_check_count": _summary_request_value(
            result, "selected_runtime_readiness_failed_check_count"
        ),
        "selected_final_completion_outcome": _summary_request_value(
            result, "selected_portable_verification_final_completion_result_outcome"
        ),
        "selected_final_completion_version": _summary_request_value(
            result, "selected_portable_verification_final_completion_result_version"
        ),
        "selected_final_completion_failed_check_count": _summary_request_value(
            result, "selected_portable_verification_final_completion_failed_check_count"
        ),
        "selected_post_portable_currentness_surface_path": _summary_request_value(
            result, "selected_post_portable_currentness_surface_path"
        ),
        "no_runtime_runtime_step_continuation_source_authority_currentness_deployment_public_release_follow_on": True,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "runtime_created",
                "runtime_step_created",
                "continuation_authorized",
                "runtime_boundary_treated_as_runtime",
                "runtime_boundary_treated_as_runtime_step",
                "runtime_boundary_treated_as_continuation",
                "source_created",
                "authority_created",
                "currentness_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
            )
        },
    }
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[field] = bool(statement.get(field))
    summary["source_transfer_source_receipt_reception_authorization_not_created"] = all(
        bool(statement.get(field))
        for field in (
            "source_transfer_not_created",
            "source_receipt_not_created",
            "reception_authorization_not_created",
        )
    )
    summary["source_authority_currentness_deployment_public_release_operation_permission_follow_on_not_created"] = all(
        bool(statement.get(field))
        for field in (
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "follow_on_work_not_authorized",
        )
    )
    summary["predecessor_failure_evidence_preserved"] = bool(
        statement.get("predecessor_failure_evidence_preserved")
    )
    summary["consumed_request_token_remains_closed"] = bool(
        statement.get("consumed_request_token_remains_closed")
    )
    summary["authorization_token_reuse_blocked"] = bool(
        statement.get("authorization_token_reuse_blocked")
    )
    return _sanitize_mapping(summary)


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block: dict[str, Any] | None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED and block is None
    request_id = _request_id(request)
    metadata = {
        "post_portable_verification_runtime_boundary_id": request_id,
        "post_portable_verification_runtime_boundary_type": (
            "post_portable_verification_runtime_boundary_result"
        ),
        "post_portable_verification_runtime_boundary_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    result: dict[str, Any] = {
        "post_portable_verification_runtime_boundary_metadata": metadata,
        "declared_runtime_boundary_question": {
            "runtime_boundary_request_id": request_id,
            "runtime_boundary_question": _sanitize(request.get("runtime_boundary_question")),
            "runtime_boundary_intent": _sanitize(request.get("runtime_boundary_intent")),
        },
        "selected_runtime_readiness_basis": _sanitize(
            request.get("selected_runtime_readiness_basis")
        ),
        "selected_runtime_readiness_terminal_summary_basis": _sanitize(
            request.get("selected_runtime_readiness_terminal_summary_basis")
        ),
        "selected_portable_verification_final_completion_basis": _sanitize(
            request.get("selected_portable_verification_final_completion_basis")
        ),
        "selected_post_portable_verification_currentness_basis": _sanitize(
            request.get("selected_post_portable_verification_currentness_basis")
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _sanitize(
            request.get("selected_returned_second_carrier_capture_lineage_basis")
        ),
    }
    for field in POSTURE_FIELDS:
        result[field] = _sanitize(request.get(field))

    result.update(
        {
            "runtime_boundary_scope": _sanitize(_scope_values(request)),
            "runtime_boundary_checks": checks,
            "runtime_boundary_statement": _runtime_boundary_statement(recorded),
            "runtime_boundary_non_meaning": _runtime_boundary_non_meaning(),
            "additional_basis_required": _sanitize(
                request.get("additional_basis_context", [])
            ),
            "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
            "what_remains_open": _what_remains_open(),
            "non_claims": _safe_non_claims(),
            "outcome": outcome,
            "block": block,
        }
    )
    result["post_portable_verification_runtime_boundary_summary"] = (
        build_post_portable_verification_runtime_boundary_summary(result)
    )
    return _sanitize_mapping(result)


def resolve_post_portable_verification_runtime_boundary(
    declared_runtime_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_runtime_boundary_request is None:
        request: Mapping[str, Any] = {}
        checks: list[dict[str, Any]] = []
        _add_runtime_boundary_checks(
            request,
            checks,
            forced_block_code="DECLARED_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
        )
        block = _block_from_failed_check(_first_failed_check(checks), request)
        return _build_result(request, checks, OUTCOME_BLOCKED, block)

    if not _is_mapping(declared_runtime_boundary_request):
        request = {}
        checks = []
        _add_runtime_boundary_checks(
            request,
            checks,
            forced_block_code="DECLARED_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
        )
        block = _block_from_failed_check(_first_failed_check(checks), request)
        return _build_result(request, checks, OUTCOME_BLOCKED, block)

    request = copy.deepcopy(dict(declared_runtime_boundary_request))
    checks = []
    _add_runtime_boundary_checks(request, checks)
    failed = _first_failed_check(checks)
    block = _block_from_failed_check(failed, request)
    if block is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("runtime_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif request.get("requested_runtime_boundary_outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif request.get("requested_runtime_boundary_outcome") == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    else:
        outcome = OUTCOME_RECORDED
    return _build_result(request, checks, outcome, block)


def resolve_post_portable_verification_runtime_boundary_from_path(
    declared_runtime_boundary_request_path: Path | str,
) -> dict:
    try:
        path = Path(declared_runtime_boundary_request_path)
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError):
        request: Mapping[str, Any] = {}
        checks: list[dict[str, Any]] = []
        _add_runtime_boundary_checks(
            request,
            checks,
            forced_block_code="DECLARED_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
        )
        block = _block_from_failed_check(_first_failed_check(checks), request)
        return _build_result(request, checks, OUTCOME_BLOCKED, block)

    if not _is_mapping(loaded):
        request = {}
        checks = []
        _add_runtime_boundary_checks(
            request,
            checks,
            forced_block_code="DECLARED_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
        )
        block = _block_from_failed_check(_first_failed_check(checks), request)
        return _build_result(request, checks, OUTCOME_BLOCKED, block)
    return resolve_post_portable_verification_runtime_boundary(loaded)


def _safe_filename_stem(value: Any) -> str:
    raw = str(value or "post_portable_verification_runtime_boundary_request").strip()
    allowed = []
    for char in raw:
        if char.isalnum() or char in {"-", "_", "."}:
            allowed.append(char)
        else:
            allowed.append("_")
    stem = "".join(allowed).strip("._")
    return stem or "post_portable_verification_runtime_boundary_request"


def _ensure_allowed_output_path(path: Path) -> None:
    normalized = path.as_posix()
    if OUTPUT_ROOT.as_posix() in normalized:
        return
    prohibited_markers = (
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/",
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary/",
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/",
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary/",
        "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure/",
        "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence/",
        "actual_second_carrier_live_capture",
        "second_carrier",
        "packet_transfer",
        "packet_emission",
        "command_success",
        "command_result",
        "source_transfer",
        "source-transfer",
        "source_receipt",
        "source-receipt",
        "reception",
        "/runtime/",
        "runtime_host",
        "deployment",
        "public_release",
        "public-release",
    )
    if any(marker in normalized for marker in prohibited_markers):
        raise PostPortableVerificationRuntimeBoundaryError(
            "output path targets a prohibited prior/runtime/deployment root"
        )


def write_post_portable_verification_runtime_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not _is_mapping(result):
        raise PostPortableVerificationRuntimeBoundaryError(
            "runtime-boundary result must be mapping-shaped"
        )
    summary = result.get("post_portable_verification_runtime_boundary_summary")
    request_id = None
    if _is_mapping(summary):
        request_id = summary.get("request_id")
    if request_id is None:
        metadata = result.get("post_portable_verification_runtime_boundary_metadata")
        if _is_mapping(metadata):
            request_id = metadata.get("post_portable_verification_runtime_boundary_id")
    filename = (
        f"{_safe_filename_stem(request_id)}"
        "__post_portable_verification_runtime_boundary_result.json"
    )
    if output_path is None:
        path = OUTPUT_ROOT / filename
    else:
        supplied = Path(output_path)
        path = supplied if supplied.suffix == ".json" else supplied / filename
    _ensure_allowed_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    index = 1
    while final_path.exists():
        final_path = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        index += 1
    final_path.write_text(
        json.dumps(_sanitize(result), indent=2, sort_keys=True, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_post_portable_verification_runtime_boundary_request(
    *,
    runtime_boundary_request_id: str = (
        "post_portable_verification_runtime_boundary_reference_review_001"
    ),
    runtime_boundary_question: str = CORE_QUESTION,
    runtime_boundary_intent: str = INTENT_RECORD,
    runtime_boundary_scope: list[str] | tuple[str, ...] | None = None,
    overrides: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    readiness_artifact_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/"
        "post_portable_verification_runtime_readiness_reference_review_001"
        "__post_portable_verification_runtime_readiness_result.json"
    )
    final_completion_artifact_path = (
        "artifacts/"
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/"
        "portable_source_body_verification_final_completion_reference_review_001"
        "__portable_source_body_verification_final_completion_result.json"
    )
    request: dict[str, Any] = {
        "runtime_boundary_request_id": runtime_boundary_request_id,
        "runtime_boundary_question": runtime_boundary_question,
        "runtime_boundary_intent": runtime_boundary_intent,
        "selected_runtime_readiness_basis": _reference_basis(
            basis_name="post_portable_verification_runtime_readiness_result",
            path=readiness_artifact_path,
            role="runtime-readiness live artifact basis",
            selected_runtime_readiness_result_path=readiness_artifact_path,
            selected_runtime_readiness_result_outcome=EXPECTED_RUNTIME_READINESS_OUTCOME,
            selected_runtime_readiness_result_version=RESULT_VERSION,
            selected_runtime_readiness_failed_check_count=0,
            selected_runtime_readiness_bounded_runtime_readiness_recorded=True,
            selected_runtime_readiness_already_created_runtime=False,
            selected_runtime_readiness_already_created_runtime_step=False,
            selected_runtime_readiness_already_authorized_continuation=False,
            selected_runtime_readiness_treated_as_runtime=False,
            selected_runtime_readiness_treated_as_runtime_step=False,
            selected_runtime_readiness_treated_as_continuation=False,
            selected_runtime_readiness_treated_as_source_transfer=False,
            selected_runtime_readiness_treated_as_source_receipt=False,
            selected_runtime_readiness_treated_as_reception_authorization=False,
            selected_runtime_readiness_treated_as_source=False,
            selected_runtime_readiness_treated_as_authority=False,
            selected_runtime_readiness_treated_as_currentness=False,
            selected_runtime_readiness_treated_as_deployment=False,
            selected_runtime_readiness_treated_as_public_release=False,
            selected_runtime_readiness_treated_as_operation_permission=False,
            selected_runtime_readiness_treated_as_reusable_permission=False,
            selected_runtime_readiness_treated_as_follow_on_work=False,
            selected_runtime_readiness_authorized_future_work=False,
        ),
        "selected_runtime_readiness_terminal_summary_basis": _reference_basis(
            basis_name="post_portable_verification_runtime_readiness_terminal_summary",
            path="spec/POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_TERMINAL_SUMMARY_V0.md",
            role="runtime-readiness terminal summary basis",
            runtime_boundary_not_created=True,
            runtime_not_created=True,
            runtime_step_not_created=True,
            continuation_not_authorized=True,
            future_work_requires_separate_bounded_specification=True,
        ),
        "selected_portable_verification_final_completion_basis": _reference_basis(
            basis_name="portable_source_body_verification_final_completion_result",
            path=final_completion_artifact_path,
            role="portable verification final-completion basis",
            selected_portable_verification_final_completion_result_path=(
                final_completion_artifact_path
            ),
            selected_portable_verification_final_completion_result_outcome=(
                EXPECTED_FINAL_COMPLETION_OUTCOME
            ),
            selected_portable_verification_final_completion_result_version=(
                RESULT_VERSION
            ),
            selected_portable_verification_final_completion_failed_check_count=0,
        ),
        "selected_post_portable_verification_currentness_basis": _reference_basis(
            basis_name="post_portable_verification_currentness_surface",
            path="spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            role="currentness-compression basis only",
            selected_post_portable_currentness_surface_path=(
                "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md"
            ),
            selected_post_portable_currentness_surface_states_checkability_not_continuation=True,
            selected_post_portable_currentness_surface_authorized_next_work=False,
        ),
        "selected_returned_second_carrier_capture_lineage_basis": _reference_basis(
            basis_name="returned_second_carrier_live_capture_intake",
            path=(
                "spec/"
                "PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md"
            ),
            role="preserved lineage only, not runtime-boundary basis authority",
            lineage_only=True,
        ),
        "runtime_boundary_scope": list(
            runtime_boundary_scope
            if runtime_boundary_scope is not None
            else SUPPORTED_RUNTIME_BOUNDARY_SCOPE
        ),
        "declared_non_claims": _safe_non_claims(),
        "selected_runtime_readiness_result_path": readiness_artifact_path,
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_runtime_readiness_bounded_runtime_readiness_recorded": True,
        "selected_runtime_readiness_already_created_runtime": False,
        "selected_runtime_readiness_already_created_runtime_step": False,
        "selected_runtime_readiness_already_authorized_continuation": False,
        "selected_runtime_readiness_treated_as_runtime": False,
        "selected_runtime_readiness_treated_as_runtime_step": False,
        "selected_runtime_readiness_treated_as_continuation": False,
        "selected_runtime_readiness_treated_as_source_transfer": False,
        "selected_runtime_readiness_treated_as_source_receipt": False,
        "selected_runtime_readiness_treated_as_reception_authorization": False,
        "selected_runtime_readiness_treated_as_source": False,
        "selected_runtime_readiness_treated_as_authority": False,
        "selected_runtime_readiness_treated_as_currentness": False,
        "selected_runtime_readiness_treated_as_deployment": False,
        "selected_runtime_readiness_treated_as_public_release": False,
        "selected_runtime_readiness_treated_as_operation_permission": False,
        "selected_runtime_readiness_treated_as_reusable_permission": False,
        "selected_runtime_readiness_treated_as_follow_on_work": False,
        "selected_runtime_readiness_authorized_future_work": False,
        "selected_portable_verification_final_completion_result_path": (
            final_completion_artifact_path
        ),
        "selected_portable_verification_final_completion_result_outcome": (
            EXPECTED_FINAL_COMPLETION_OUTCOME
        ),
        "selected_portable_verification_final_completion_result_version": RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": (
            "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md"
        ),
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "runtime_boundary_created_before_review": False,
        "runtime_created": False,
        "runtime_step_created": False,
        "continuation_authorized": False,
        "reference_shaped_input_posture": True,
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_repaired": False,
        "predecessor_failure_hidden": False,
        "predecessor_failure_claimed_passed": False,
        "raw_full_prior_artifact_body_returned": False,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "additional_basis_context": [],
        "not_recorded_basis": [],
        "block_reason": None,
        "requested_runtime_boundary_outcome": OUTCOME_RECORDED,
    }
    for field in POSTURE_FIELDS:
        request[field] = _posture(field)
    if overrides:
        for key, value in copy.deepcopy(dict(overrides)).items():
            request[key] = value
    return request
