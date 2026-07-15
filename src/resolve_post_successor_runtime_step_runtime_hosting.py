"""Bounded post-successor-runtime-step runtime-hosting resolver.

This resolver is downstream of runtime-hosting-boundary v2. It records one
bounded runtime-hosting posture and one bounded non-operational host relation
only. It preserves the v1 runtime-hosting-boundary resolver/test failure as
predecessor evidence, keeps runtime hosting distinct from ongoing runtime,
reusable runtime permission, continuation, self-continuation, daemon, loop,
public API, participant-facing interface, distributed network behavior, source,
authority, currentness, deployment, public release, operation permission, and
follow-on work, and emits canonical false result-level non-claims for every
outcome.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


class PostSuccessorRuntimeStepRuntimeHostingError(Exception):
    """Bounded resolver error for runtime-hosting request and artifact handling."""


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(value.split())


RESULT_VERSION = "0.1.0"
UPSTREAM_RESULT_VERSION = "0.1.0"
RUNTIME_HOSTING_BOUNDARY_V2_RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_post_successor_runtime_step_runtime_hosting"

OUTCOME_RECORDED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED"
OUTCOME_NOT_RECORDED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING"
INTENT_BLOCK = "BLOCK_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting"
)

CORE_QUESTION = (
    "Can the clean post-successor-runtime-step runtime-hosting-boundary v2 "
    "basis be used to record one bounded runtime-hosting posture without "
    "creating ongoing runtime, reusable runtime permission, continuation, "
    "self-continuation, self-recursive growth, runtime daemon, runtime loop, "
    "public API, participant-facing interface, distributed network behavior, "
    "source transfer, source receipt, reception authorization, source, "
    "authority, currentness, deployment, public release, operation permission, "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, adoption, receiving-context governance, publication "
    "flow, or follow-on work?"
)

EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME = (
    "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED"
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

SUPPORTED_SCOPE_VALUES = _tokens(
    """
    RUNTIME_HOSTING_SPEC_ONLY ONE_BOUNDED_RUNTIME_HOSTING_POSTURE_RECORDED
    RUNTIME_HOSTING_BOUNDARY_V2_BASIS_PRESERVED
    SUCCESSOR_RUNTIME_STEP_BASIS_PRESERVED
    BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_NOT_HOSTING_AUTHORIZATION
    RUNTIME_HOSTING_NOT_ONGOING_RUNTIME
    RUNTIME_HOSTING_NOT_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_NOT_CONTINUATION RUNTIME_HOSTING_NOT_SELF_CONTINUATION
    RUNTIME_HOSTING_NOT_DAEMON RUNTIME_HOSTING_NOT_LOOP
    RUNTIME_HOSTING_NOT_PUBLIC_API
    RUNTIME_HOSTING_NOT_PARTICIPANT_FACING_INTERFACE
    RUNTIME_HOSTING_NOT_DISTRIBUTED_NETWORK_BEHAVIOR
    ONGOING_RUNTIME_NOT_CREATED REUSABLE_RUNTIME_PERMISSION_NOT_CREATED
    NO_CONTINUATION_AUTHORIZED SELF_CONTINUATION_NOT_AUTHORIZED
    SELF_RECURSIVE_GROWTH_NOT_CREATED RUNTIME_DAEMON_NOT_CREATED
    RUNTIME_LOOP_NOT_CREATED PUBLIC_API_NOT_CREATED
    PARTICIPANT_FACING_INTERFACE_NOT_CREATED DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED
    NO_SOURCE_TRANSFER NO_SOURCE_RECEIPT NO_RECEPTION_AUTHORIZATION
    NO_SOURCE_CREATED NO_AUTHORITY_CREATED NO_CURRENTNESS_CREATED
    NO_DEPLOYMENT_CREATED NO_PUBLIC_RELEASE_CREATED NO_OPERATION_PERMISSION_CREATED
    NO_REUSABLE_PERMISSION NO_DERIVATIVE_RECEPTION NO_VESSEL_RELATION
    NO_ANOTHER_RECEPTION_REQUEST NO_ADOPTION NO_RECEIVING_CONTEXT_GOVERNANCE
    NO_PUBLICATION_FLOW NO_FOLLOW_ON_WORK_AUTHORIZED
    NO_ONGOING_RUNTIME_INFERENCE NO_REUSABLE_RUNTIME_PERMISSION_INFERENCE
    NO_CONTINUATION_INFERENCE NO_SELF_CONTINUATION_INFERENCE
    NO_DAEMON_INFERENCE NO_LOOP_INFERENCE NO_PUBLIC_API_INFERENCE
    NO_PARTICIPANT_INTERFACE_INFERENCE NO_DISTRIBUTED_NETWORK_INFERENCE
    NO_SOURCE_INFERENCE NO_AUTHORITY_INFERENCE NO_CURRENTNESS_INFERENCE
    NO_DEPLOYMENT_INFERENCE NO_PUBLIC_RELEASE_INFERENCE
    NO_OPERATION_PERMISSION_INFERENCE NO_FOLLOW_ON_WORK_INFERENCE
    NO_UNBOUNDED_PASS_FAIL_INFERENCE HIDDEN_REPO_STATE_EXCLUDED
    HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_HOSTING_AUTHORITY
    REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_HOSTING_AUTHORITY
    ARTIFACT_EXISTENCE_NOT_RUNTIME_HOSTING_AUTHORITY
    LATEST_FILE_POSTURE_NOT_RUNTIME_HOSTING_AUTHORITY
    SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED
    RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED
    OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED HOSTILE_RAW_BODY_CONTENT_CONTAINED
    PREDECESSOR_FAILURE_EVIDENCE_PRESERVED AUTHORIZATION_TOKEN_REUSE_BLOCKED
    CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED CONSUMED_REQUEST_NOT_REOPENED
    RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE
    """
)
SUPPORTED_RUNTIME_HOSTING_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = _tokens(
    """
    ongoing_runtime_created reusable_runtime_permission_created continuation_authorized
    self_continuation_authorized self_recursive_growth_created runtime_daemon_created
    runtime_loop_created public_api_created participant_facing_interface_created
    distributed_network_behavior_created source_transfer_occurred source_receipt_occurred
    reception_authorization_created runtime_hosting_treated_as_ongoing_runtime
    runtime_hosting_treated_as_reusable_runtime_permission
    runtime_hosting_treated_as_continuation runtime_hosting_treated_as_self_continuation
    runtime_hosting_treated_as_self_recursive_growth
    runtime_hosting_treated_as_runtime_daemon runtime_hosting_treated_as_runtime_loop
    runtime_hosting_treated_as_public_api
    runtime_hosting_treated_as_participant_facing_interface
    runtime_hosting_treated_as_distributed_network_behavior
    runtime_hosting_treated_as_source_transfer
    runtime_hosting_treated_as_source_receipt
    runtime_hosting_treated_as_reception_authorization
    runtime_hosting_treated_as_source runtime_hosting_treated_as_authority
    runtime_hosting_treated_as_currentness runtime_hosting_treated_as_deployment
    runtime_hosting_treated_as_public_release
    runtime_hosting_treated_as_operation_permission
    runtime_hosting_treated_as_reusable_permission
    runtime_hosting_treated_as_follow_on_work
    runtime_hosting_boundary_v2_treated_as_runtime_hosting_without_review
    successor_runtime_step_treated_as_runtime_hosting
    bounded_successor_runtime_result_or_refusal_authorized_hosting
    runtime_hosting_boundary_v1_failure_repaired
    runtime_hosting_boundary_v1_failure_hidden
    runtime_hosting_boundary_v1_failure_claimed_passed
    artifact_existence_treated_as_runtime_hosting_authority
    artifact_path_treated_as_currentness
    latest_file_posture_treated_as_runtime_hosting_authority
    repo_local_availability_treated_as_runtime_hosting_authority
    hidden_repo_state_used_as_runtime_hosting_content
    hidden_repo_state_used_as_runtime_hosting_authority
    source_created authority_created currentness_created deployment_created public_release_created
    operation_permission_created reusable_permission_created derivative_reception_authorized
    vessel_relation_authorized another_reception_request_authorized adoption_created
    receiving_context_governance_created publication_flow_created follow_on_work_authorized
    raw_full_prior_artifact_body_returned prior_artifacts_mutated consumed_request_reopened
    authorization_token_reused predecessor_failure_repaired predecessor_failure_hidden
    predecessor_failure_claimed_passed
    """
)

ALLOWED_TRUE_RECORDED_FIELDS = _tokens(
    """
    runtime_hosting_recorded bounded_runtime_hosting_posture_recorded
    runtime_hosting_boundary_v2_basis_preserved successor_runtime_step_basis_preserved
    bounded_successor_runtime_result_or_refusal_not_hosting_authorization
    runtime_hosting_not_ongoing_runtime runtime_hosting_not_reusable_runtime_permission
    runtime_hosting_not_continuation runtime_hosting_not_self_continuation
    runtime_hosting_not_daemon runtime_hosting_not_loop runtime_hosting_not_public_api
    runtime_hosting_not_participant_facing_interface
    runtime_hosting_not_distributed_network_behavior ongoing_runtime_not_created
    reusable_runtime_permission_not_created continuation_not_authorized
    self_continuation_not_authorized self_recursive_growth_not_created
    runtime_daemon_not_created runtime_loop_not_created public_api_not_created
    participant_facing_interface_not_created distributed_network_behavior_not_created
    source_transfer_not_created source_receipt_not_created
    reception_authorization_not_created source_not_created authority_not_created
    currentness_not_created deployment_not_created public_release_not_created
    operation_permission_not_created reusable_permission_not_created
    follow_on_work_not_authorized hidden_repo_state_excluded
    hidden_repo_state_not_used_as_runtime_hosting_authority
    repo_local_availability_not_runtime_hosting_authority
    artifact_existence_not_runtime_hosting_authority
    latest_file_posture_not_runtime_hosting_authority
    selected_basis_reference_shape_preserved raw_full_prior_artifact_body_not_returned
    official_enum_scope_strings_not_redacted hostile_raw_body_content_contained
    predecessor_failure_evidence_preserved authorization_token_reuse_blocked
    consumed_request_token_remains_closed result_level_non_claims_canonical_false
    """
)

BLOCK_CODES = _tokens(
    """
    RUNTIME_HOSTING_QUESTION_UNDECLARED RUNTIME_HOSTING_INTENT_UNSUPPORTED
    RUNTIME_HOSTING_REQUEST_DECLARED_BLOCK RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING
    RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED
    RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT
    RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0
    RUNTIME_HOSTING_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RUNTIME_HOSTING_REVIEW
    RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_RUNTIME_HOSTING
    RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_ONGOING_RUNTIME
    RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_AUTHORIZED_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_AUTHORIZED_SELF_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_RUNTIME_HOSTING
    RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_ONGOING_RUNTIME
    RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_SELF_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_V2_AUTHORIZED_FUTURE_WORK
    RUNTIME_HOSTING_BOUNDARY_V2_DID_NOT_CANONICALIZE_NON_CLAIMS
    RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED
    RUNTIME_HOSTING_CREATED_BEFORE_REVIEW RUNTIME_HOSTING_TREATED_AS_ONGOING_RUNTIME
    RUNTIME_HOSTING_TREATED_AS_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_TREATED_AS_CONTINUATION
    RUNTIME_HOSTING_TREATED_AS_SELF_CONTINUATION
    RUNTIME_HOSTING_TREATED_AS_SELF_RECURSIVE_GROWTH
    RUNTIME_HOSTING_TREATED_AS_RUNTIME_DAEMON RUNTIME_HOSTING_TREATED_AS_RUNTIME_LOOP
    RUNTIME_HOSTING_TREATED_AS_PUBLIC_API
    RUNTIME_HOSTING_TREATED_AS_PARTICIPANT_FACING_INTERFACE
    RUNTIME_HOSTING_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR
    RUNTIME_HOSTING_TREATED_AS_SOURCE_TRANSFER RUNTIME_HOSTING_TREATED_AS_SOURCE_RECEIPT
    RUNTIME_HOSTING_TREATED_AS_RECEPTION_AUTHORIZATION RUNTIME_HOSTING_TREATED_AS_SOURCE
    RUNTIME_HOSTING_TREATED_AS_AUTHORITY RUNTIME_HOSTING_TREATED_AS_CURRENTNESS
    RUNTIME_HOSTING_TREATED_AS_DEPLOYMENT RUNTIME_HOSTING_TREATED_AS_PUBLIC_RELEASE
    RUNTIME_HOSTING_TREATED_AS_OPERATION_PERMISSION
    RUNTIME_HOSTING_TREATED_AS_REUSABLE_PERMISSION
    RUNTIME_HOSTING_TREATED_AS_FOLLOW_ON_WORK ONGOING_RUNTIME_CREATED
    REUSABLE_RUNTIME_PERMISSION_CREATED CONTINUATION_AUTHORIZED
    SELF_CONTINUATION_AUTHORIZED SELF_RECURSIVE_GROWTH_CREATED RUNTIME_DAEMON_CREATED
    RUNTIME_LOOP_CREATED PUBLIC_API_CREATED PARTICIPANT_FACING_INTERFACE_CREATED
    DISTRIBUTED_NETWORK_BEHAVIOR_CREATED SOURCE_TRANSFER_OCCURRED
    SOURCE_RECEIPT_OCCURRED RECEPTION_AUTHORIZATION_CREATED SOURCE_CREATED
    AUTHORITY_CREATED CURRENTNESS_CREATED DEPLOYMENT_CREATED PUBLIC_RELEASE_CREATED
    OPERATION_PERMISSION_CREATED REUSABLE_PERMISSION_CREATED
    DERIVATIVE_RECEPTION_AUTHORIZED VESSEL_RELATION_AUTHORIZED
    ANOTHER_RECEPTION_REQUEST_AUTHORIZED ADOPTION_CREATED
    RECEIVING_CONTEXT_GOVERNANCE_CREATED PUBLICATION_FLOW_CREATED
    FOLLOW_ON_WORK_AUTHORIZED ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_AUTHORITY
    ARTIFACT_PATH_TREATED_AS_CURRENTNESS
    LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_AUTHORITY
    REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_AUTHORITY
    HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_CONTENT
    HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_AUTHORITY
    SELECTED_BASIS_NOT_REFERENCE_SHAPED RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED
    PRIOR_ARTIFACTS_MUTATED PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED
    CONSUMED_REQUEST_REOPENED AUTHORIZATION_TOKEN_REUSED NON_CLAIM_MISSING_OR_FLIPPED
    UNSUPPORTED_RUNTIME_HOSTING_SCOPE DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED
    DECLARED_RUNTIME_HOSTING_REQUEST_UNREADABLE SUCCESSOR_RUNTIME_STEP_BASIS_MISSING
    SUCCESSOR_RUNTIME_STEP_NOT_RECORDED SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0
    SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT
    SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP
    SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING
    BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING
    SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING
    SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED
    SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0
    SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT MINIMAL_RUNTIME_BASIS_MISSING
    MINIMAL_RUNTIME_NOT_RECORDED MINIMAL_RUNTIME_VERSION_NOT_0_1_0
    MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT RUNTIME_BOUNDARY_BASIS_MISSING
    RUNTIME_BOUNDARY_NOT_RECORDED RUNTIME_BOUNDARY_VERSION_NOT_0_1_0
    RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT RUNTIME_READINESS_BASIS_MISSING
    RUNTIME_READINESS_NOT_RECORDED RUNTIME_READINESS_VERSION_NOT_0_1_0
    RUNTIME_READINESS_FAILED_CHECKS_PRESENT FINAL_COMPLETION_BASIS_MISSING
    FINAL_COMPLETION_NOT_RECORDED FINAL_COMPLETION_VERSION_NOT_0_1_0
    FINAL_COMPLETION_FAILED_CHECKS_PRESENT POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING
    POST_PORTABLE_CURRENTNESS_SURFACE_DID_NOT_PRESERVE_CHECKABILITY_NOT_CONTINUATION
    POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK REQUIRED_POSTURE_MISSING
    """
)

BASIS_FIELDS = _tokens(
    """
    selected_runtime_hosting_boundary_v2_basis
    selected_runtime_hosting_boundary_v2_terminal_summary_basis
    selected_runtime_hosting_boundary_v1_failure_lineage_basis
    selected_successor_runtime_step_basis selected_successor_runtime_step_terminal_summary_basis
    selected_successor_runtime_step_boundary_basis selected_minimal_runtime_basis
    selected_runtime_boundary_basis selected_runtime_readiness_basis
    selected_portable_verification_final_completion_basis
    selected_post_portable_verification_currentness_basis
    selected_returned_second_carrier_capture_lineage_basis
    """
)

POSTURE_FIELDS = _tokens(
    """
    runtime_hosting_spec_only_posture one_bounded_runtime_hosting_posture
    runtime_hosting_boundary_v2_basis_preserved_posture
    successor_runtime_step_basis_preserved_posture
    bounded_successor_runtime_result_or_refusal_not_hosting_authorization_posture
    runtime_hosting_not_ongoing_runtime_posture
    runtime_hosting_not_reusable_runtime_permission_posture
    runtime_hosting_not_continuation_posture
    runtime_hosting_not_self_continuation_posture runtime_hosting_not_daemon_posture
    runtime_hosting_not_loop_posture runtime_hosting_not_public_api_posture
    runtime_hosting_not_participant_facing_interface_posture
    runtime_hosting_not_distributed_network_behavior_posture
    ongoing_runtime_not_created_posture reusable_runtime_permission_not_created_posture
    continuation_not_authorized_posture self_continuation_not_authorized_posture
    self_recursive_growth_not_created_posture runtime_daemon_not_created_posture
    runtime_loop_not_created_posture public_api_not_created_posture
    participant_facing_interface_not_created_posture distributed_network_behavior_not_created_posture
    source_transfer_not_created_posture source_receipt_not_created_posture
    reception_authorization_not_created_posture source_not_created_posture
    authority_not_created_posture currentness_not_created_posture deployment_not_created_posture
    public_release_not_created_posture operation_permission_not_created_posture
    reusable_permission_not_created_posture follow_on_work_not_authorized_posture
    hidden_repo_state_excluded_posture
    repo_local_availability_not_runtime_hosting_authority_posture
    artifact_existence_not_runtime_hosting_authority_posture
    latest_file_posture_not_runtime_hosting_authority_posture
    selected_basis_reference_shape_posture raw_full_prior_artifact_body_not_returned_posture
    official_enum_scope_strings_not_redacted_posture hostile_raw_body_content_contained_posture
    predecessor_failure_evidence_preserved_posture result_level_non_claims_canonical_false_posture
    """
)

RAW_KEY_FRAGMENTS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_hosting_body",
    "raw_ongoing_runtime_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
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
HOSTILE_SENTINELS = (
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
REDACTED_RAW_OR_HIDDEN = "[bounded-redacted-raw-or-hidden-state]"


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            key_lower = key_text.lower()
            if key_lower.endswith("_body") or any(fragment in key_lower for fragment in RAW_KEY_FRAGMENTS):
                sanitized[key_text] = REDACTED_RAW_OR_HIDDEN
            else:
                sanitized[key_text] = _sanitize(item)
        return sanitized
    if isinstance(value, (list, tuple, set)):
        return [_sanitize(item) for item in value]
    if isinstance(value, str):
        if value in SUPPORTED_SCOPE_VALUES or value in BLOCK_CODES or value in OUTCOME_FAMILY:
            return value
        if value in REQUIRED_FALSE_NON_CLAIMS or value in ALLOWED_TRUE_RECORDED_FIELDS:
            return value
        if "MUST_NOT_RETURN" in value or "SHOULD_NOT_RETURN" in value:
            return REDACTED_RAW_OR_HIDDEN
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_OR_HIDDEN
    return value


def _check(name: str, passed: bool, expected: Any, actual: Any, code: str) -> dict[str, Any]:
    if code not in BLOCK_CODES:
        code = "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED"
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        return bool(value) and value.get("declared") is not False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return value is not None


def _scope_values(value: Any) -> list[str]:
    if value is None:
        return list(SUPPORTED_SCOPE_VALUES)
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        return [str(key) for key, enabled in value.items() if enabled]
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]


def _value(
    request: Mapping[str, Any],
    shortcut: str,
    basis_field: str | None = None,
    *basis_keys: str,
    default: Any = None,
) -> Any:
    if shortcut in request:
        return request.get(shortcut)
    if basis_field is not None:
        basis = request.get(basis_field)
        if isinstance(basis, Mapping):
            for key in basis_keys:
                if key in basis:
                    return basis.get(key)
    return default


def _basis_missing_code(field: str) -> str:
    mapping = {
        "selected_runtime_hosting_boundary_v2_basis": "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
        "selected_runtime_hosting_boundary_v2_terminal_summary_basis": "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "selected_successor_runtime_step_basis": "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        "selected_successor_runtime_step_terminal_summary_basis": "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        "selected_successor_runtime_step_boundary_basis": "SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING",
        "selected_minimal_runtime_basis": "MINIMAL_RUNTIME_BASIS_MISSING",
        "selected_runtime_boundary_basis": "RUNTIME_BOUNDARY_BASIS_MISSING",
        "selected_runtime_readiness_basis": "RUNTIME_READINESS_BASIS_MISSING",
        "selected_portable_verification_final_completion_basis": "FINAL_COMPLETION_BASIS_MISSING",
        "selected_post_portable_verification_currentness_basis": "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    }
    return mapping.get(field, "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED")


def _non_claim_code(key: str) -> str:
    direct = {
        "ongoing_runtime_created": "ONGOING_RUNTIME_CREATED",
        "reusable_runtime_permission_created": "REUSABLE_RUNTIME_PERMISSION_CREATED",
        "continuation_authorized": "CONTINUATION_AUTHORIZED",
        "self_continuation_authorized": "SELF_CONTINUATION_AUTHORIZED",
        "self_recursive_growth_created": "SELF_RECURSIVE_GROWTH_CREATED",
        "runtime_daemon_created": "RUNTIME_DAEMON_CREATED",
        "runtime_loop_created": "RUNTIME_LOOP_CREATED",
        "public_api_created": "PUBLIC_API_CREATED",
        "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
        "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
        "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
        "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
        "reception_authorization_created": "RECEPTION_AUTHORIZATION_CREATED",
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
        "runtime_hosting_boundary_v2_treated_as_runtime_hosting_without_review": "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_RUNTIME_HOSTING",
        "successor_runtime_step_treated_as_runtime_hosting": "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING",
        "bounded_successor_runtime_result_or_refusal_authorized_hosting": "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
        "runtime_hosting_boundary_v1_failure_repaired": "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "runtime_hosting_boundary_v1_failure_hidden": "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "runtime_hosting_boundary_v1_failure_claimed_passed": "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        "artifact_existence_treated_as_runtime_hosting_authority": "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_AUTHORITY",
        "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "latest_file_posture_treated_as_runtime_hosting_authority": "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_AUTHORITY",
        "repo_local_availability_treated_as_runtime_hosting_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_AUTHORITY",
        "hidden_repo_state_used_as_runtime_hosting_content": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_CONTENT",
        "hidden_repo_state_used_as_runtime_hosting_authority": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_AUTHORITY",
        "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
        "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
        "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
        "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    }
    if key in direct:
        return direct[key]
    if key.startswith("runtime_hosting_treated_as_"):
        suffix = key.removeprefix("runtime_hosting_treated_as_").upper()
        code = "RUNTIME_HOSTING_TREATED_AS_" + suffix
        return code if code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    return "NON_CLAIM_MISSING_OR_FLIPPED"


def _declared_claims(request: Mapping[str, Any]) -> Mapping[str, Any] | None:
    claims = request.get("declared_non_claims")
    return claims if isinstance(claims, Mapping) else None


def _incoming_non_claim(request: Mapping[str, Any], key: str) -> Any:
    claims = _declared_claims(request)
    if claims is not None and claims.get(key) is not False:
        return claims.get(key)
    if key in request:
        return request.get(key)
    if claims is not None and key in claims:
        return claims.get(key)
    return None


def _statement(recorded: bool) -> dict[str, bool]:
    statement = {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    always_true = {
        "runtime_hosting_not_ongoing_runtime",
        "runtime_hosting_not_reusable_runtime_permission",
        "runtime_hosting_not_continuation",
        "runtime_hosting_not_self_continuation",
        "runtime_hosting_not_daemon",
        "runtime_hosting_not_loop",
        "runtime_hosting_not_public_api",
        "runtime_hosting_not_participant_facing_interface",
        "runtime_hosting_not_distributed_network_behavior",
        "ongoing_runtime_not_created",
        "reusable_runtime_permission_not_created",
        "continuation_not_authorized",
        "self_continuation_not_authorized",
        "self_recursive_growth_not_created",
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
        "hidden_repo_state_not_used_as_runtime_hosting_authority",
        "repo_local_availability_not_runtime_hosting_authority",
        "artifact_existence_not_runtime_hosting_authority",
        "latest_file_posture_not_runtime_hosting_authority",
        "selected_basis_reference_shape_preserved",
        "raw_full_prior_artifact_body_not_returned",
        "official_enum_scope_strings_not_redacted",
        "hostile_raw_body_content_contained",
        "predecessor_failure_evidence_preserved",
        "authorization_token_reuse_blocked",
        "consumed_request_token_remains_closed",
        "result_level_non_claims_canonical_false",
    }
    for key in always_true:
        statement[key] = True
    if recorded:
        for key in ALLOWED_TRUE_RECORDED_FIELDS:
            statement[key] = True
    return statement


def _basis(value: Any, kind: str) -> dict[str, Any]:
    sanitized = _sanitize(value)
    result = dict(sanitized) if isinstance(sanitized, Mapping) else {"basis_ref": sanitized}
    result.setdefault("basis_kind", kind)
    result.setdefault("basis_shape", "reference")
    result.setdefault("basis_only", True)
    result.setdefault("creates_ongoing_runtime", False)
    result.setdefault("creates_reusable_runtime_permission", False)
    result.setdefault("authorizes_continuation", False)
    return result


def _posture(value: Any, key: str) -> dict[str, Any]:
    sanitized = _sanitize(value)
    result = dict(sanitized) if isinstance(sanitized, Mapping) else {"declared": value is not False}
    result.setdefault(key, True)
    result.setdefault("creates_ongoing_runtime", False)
    result.setdefault("creates_reusable_runtime_permission", False)
    result.setdefault("authorizes_continuation", False)
    result.setdefault("authorizes_self_continuation", False)
    result.setdefault("creates_daemon", False)
    result.setdefault("creates_loop", False)
    result.setdefault("creates_public_api", False)
    result.setdefault("creates_participant_facing_interface", False)
    result.setdefault("creates_distributed_network_behavior", False)
    result.setdefault("authorizes_follow_on_work", False)
    return result


def _add_upstream_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    checks.extend(
        [
            _check(
                "runtime_hosting_boundary_v2_outcome_recorded",
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_result_outcome",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "outcome",
                    "result_outcome",
                )
                == EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
                EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_result_outcome",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "outcome",
                    "result_outcome",
                ),
                "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
            ),
            _check(
                "runtime_hosting_boundary_v2_version_0_2_0",
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_result_version",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "result_version",
                    "version",
                )
                == RUNTIME_HOSTING_BOUNDARY_V2_RESULT_VERSION,
                RUNTIME_HOSTING_BOUNDARY_V2_RESULT_VERSION,
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_result_version",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "result_version",
                    "version",
                ),
                "RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
            ),
            _check(
                "runtime_hosting_boundary_v2_failed_checks_zero",
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_failed_check_count",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "failed_check_count",
                )
                == 0,
                0,
                _value(
                    request,
                    "selected_runtime_hosting_boundary_v2_failed_check_count",
                    "selected_runtime_hosting_boundary_v2_basis",
                    "failed_check_count",
                ),
                "RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "runtime_hosting_boundary_v2_declared_future_runtime_hosting_review",
                request.get("selected_runtime_hosting_boundary_v2_declared_future_runtime_hosting_review")
                is True,
                True,
                request.get("selected_runtime_hosting_boundary_v2_declared_future_runtime_hosting_review"),
                "RUNTIME_HOSTING_BOUNDARY_V2_DID_NOT_DECLARE_FUTURE_RUNTIME_HOSTING_REVIEW",
            ),
            _check(
                "runtime_hosting_boundary_v2_non_claims_canonicalized",
                request.get("selected_runtime_hosting_boundary_v2_non_claims_canonicalized")
                is True,
                True,
                request.get("selected_runtime_hosting_boundary_v2_non_claims_canonicalized"),
                "RUNTIME_HOSTING_BOUNDARY_V2_DID_NOT_CANONICALIZE_NON_CLAIMS",
            ),
        ]
    )

    boundary_v2_false_checks = (
        (
            "selected_runtime_hosting_boundary_v2_already_created_runtime_hosting",
            "RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_RUNTIME_HOSTING",
        ),
        (
            "selected_runtime_hosting_boundary_v2_already_created_ongoing_runtime",
            "RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_ONGOING_RUNTIME",
        ),
        (
            "selected_runtime_hosting_boundary_v2_already_created_reusable_runtime_permission",
            "RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_already_authorized_continuation",
            "RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_AUTHORIZED_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_already_authorized_self_continuation",
            "RUNTIME_HOSTING_BOUNDARY_V2_ALREADY_AUTHORIZED_SELF_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_treated_boundary_as_runtime_hosting",
            "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_RUNTIME_HOSTING",
        ),
        (
            "selected_runtime_hosting_boundary_v2_treated_boundary_as_ongoing_runtime",
            "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_ONGOING_RUNTIME",
        ),
        (
            "selected_runtime_hosting_boundary_v2_treated_boundary_as_reusable_runtime_permission",
            "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_treated_boundary_as_continuation",
            "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_treated_boundary_as_self_continuation",
            "RUNTIME_HOSTING_BOUNDARY_V2_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "selected_runtime_hosting_boundary_v2_authorized_future_work",
            "RUNTIME_HOSTING_BOUNDARY_V2_AUTHORIZED_FUTURE_WORK",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_repaired",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_hidden",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
        (
            "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
            "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
        ),
    )
    for key, code in boundary_v2_false_checks:
        checks.append(_check(key, request.get(key) is False, False, request.get(key), code))

    upstream = (
        (
            "successor_runtime_step",
            "selected_successor_runtime_step_result_outcome",
            EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
            "selected_successor_runtime_step_result_version",
            "selected_successor_runtime_step_failed_check_count",
            "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
            "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
            "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
            "selected_successor_runtime_step_basis",
        ),
        (
            "successor_runtime_step_boundary",
            "selected_successor_runtime_step_boundary_result_outcome",
            EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
            "selected_successor_runtime_step_boundary_result_version",
            "selected_successor_runtime_step_boundary_failed_check_count",
            "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED",
            "SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0",
            "SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT",
            "selected_successor_runtime_step_boundary_basis",
        ),
        (
            "minimal_runtime",
            "selected_minimal_runtime_result_outcome",
            EXPECTED_MINIMAL_RUNTIME_OUTCOME,
            "selected_minimal_runtime_result_version",
            "selected_minimal_runtime_failed_check_count",
            "MINIMAL_RUNTIME_NOT_RECORDED",
            "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
            "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
            "selected_minimal_runtime_basis",
        ),
        (
            "runtime_boundary",
            "selected_runtime_boundary_result_outcome",
            EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
            "selected_runtime_boundary_result_version",
            "selected_runtime_boundary_failed_check_count",
            "RUNTIME_BOUNDARY_NOT_RECORDED",
            "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
            "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
            "selected_runtime_boundary_basis",
        ),
        (
            "runtime_readiness",
            "selected_runtime_readiness_result_outcome",
            EXPECTED_RUNTIME_READINESS_OUTCOME,
            "selected_runtime_readiness_result_version",
            "selected_runtime_readiness_failed_check_count",
            "RUNTIME_READINESS_NOT_RECORDED",
            "RUNTIME_READINESS_VERSION_NOT_0_1_0",
            "RUNTIME_READINESS_FAILED_CHECKS_PRESENT",
            "selected_runtime_readiness_basis",
        ),
        (
            "final_completion",
            "selected_portable_verification_final_completion_result_outcome",
            EXPECTED_FINAL_COMPLETION_OUTCOME,
            "selected_portable_verification_final_completion_result_version",
            "selected_portable_verification_final_completion_failed_check_count",
            "FINAL_COMPLETION_NOT_RECORDED",
            "FINAL_COMPLETION_VERSION_NOT_0_1_0",
            "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
            "selected_portable_verification_final_completion_basis",
        ),
    )
    for (
        name,
        outcome_key,
        outcome,
        version_key,
        failed_key,
        outcome_code,
        version_code,
        failed_code,
        basis_field,
    ) in upstream:
        checks.append(
            _check(
                name + "_outcome_recorded",
                _value(request, outcome_key, basis_field, "outcome", "result_outcome") == outcome,
                outcome,
                _value(request, outcome_key, basis_field, "outcome", "result_outcome"),
                outcome_code,
            )
        )
        checks.append(
            _check(
                name + "_version_0_1_0",
                _value(request, version_key, basis_field, "result_version", "version")
                == UPSTREAM_RESULT_VERSION,
                UPSTREAM_RESULT_VERSION,
                _value(request, version_key, basis_field, "result_version", "version"),
                version_code,
            )
        )
        checks.append(
            _check(
                name + "_failed_checks_zero",
                _value(request, failed_key, basis_field, "failed_check_count") == 0,
                0,
                _value(request, failed_key, basis_field, "failed_check_count"),
                failed_code,
            )
        )


def _add_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks = [
        _check(
            "runtime_hosting_question_declared",
            request.get("runtime_hosting_question") == CORE_QUESTION,
            CORE_QUESTION,
            request.get("runtime_hosting_question"),
            "RUNTIME_HOSTING_QUESTION_UNDECLARED",
        ),
        _check(
            "runtime_hosting_intent_supported",
            request.get("runtime_hosting_intent") in (INTENT_RECORD, INTENT_DO_NOT_RECORD),
            (INTENT_RECORD, INTENT_DO_NOT_RECORD),
            request.get("runtime_hosting_intent"),
            "RUNTIME_HOSTING_REQUEST_DECLARED_BLOCK"
            if request.get("runtime_hosting_intent") == INTENT_BLOCK
            else "RUNTIME_HOSTING_INTENT_UNSUPPORTED",
        ),
    ]

    scope = _scope_values(request.get("runtime_hosting_scope"))
    unsupported_scope = [item for item in scope if item not in SUPPORTED_SCOPE_VALUES]
    checks.append(
        _check(
            "runtime_hosting_scope_supported",
            not unsupported_scope,
            "all runtime-hosting scope values supported",
            unsupported_scope or scope,
            "UNSUPPORTED_RUNTIME_HOSTING_SCOPE",
        )
    )

    for field in BASIS_FIELDS:
        checks.append(
            _check(
                field + "_declared",
                _declared(request.get(field)),
                "declared",
                request.get(field),
                _basis_missing_code(field),
            )
        )
    for field in POSTURE_FIELDS:
        checks.append(
            _check(
                field + "_declared",
                _declared(request.get(field)),
                "declared",
                request.get(field),
                "REQUIRED_POSTURE_MISSING",
            )
        )

    _add_upstream_checks(request, checks)

    direct_checks = (
        (
            "selected_successor_runtime_step_bounded_successor_runtime_step_recorded",
            True,
            "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP",
        ),
        (
            "selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded",
            True,
            "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
        ),
        (
            "selected_successor_runtime_step_no_hosting_authorization",
            True,
            "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
        ),
        (
            "selected_post_portable_currentness_surface_states_checkability_not_continuation",
            True,
            "POST_PORTABLE_CURRENTNESS_SURFACE_DID_NOT_PRESERVE_CHECKABILITY_NOT_CONTINUATION",
        ),
        (
            "selected_post_portable_currentness_surface_authorized_next_work",
            False,
            "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
        ),
        ("predecessor_failure_evidence_visible", True, "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("runtime_hosting_created_before_review", False, "RUNTIME_HOSTING_CREATED_BEFORE_REVIEW"),
        ("runtime_hosting_treated_as_ongoing_runtime", False, "RUNTIME_HOSTING_TREATED_AS_ONGOING_RUNTIME"),
        (
            "runtime_hosting_treated_as_reusable_runtime_permission",
            False,
            "RUNTIME_HOSTING_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
        ),
        ("runtime_hosting_treated_as_continuation", False, "RUNTIME_HOSTING_TREATED_AS_CONTINUATION"),
        (
            "runtime_hosting_treated_as_self_continuation",
            False,
            "RUNTIME_HOSTING_TREATED_AS_SELF_CONTINUATION",
        ),
        (
            "runtime_hosting_treated_as_self_recursive_growth",
            False,
            "RUNTIME_HOSTING_TREATED_AS_SELF_RECURSIVE_GROWTH",
        ),
        ("runtime_hosting_treated_as_runtime_daemon", False, "RUNTIME_HOSTING_TREATED_AS_RUNTIME_DAEMON"),
        ("runtime_hosting_treated_as_runtime_loop", False, "RUNTIME_HOSTING_TREATED_AS_RUNTIME_LOOP"),
        ("runtime_hosting_treated_as_public_api", False, "RUNTIME_HOSTING_TREATED_AS_PUBLIC_API"),
        (
            "runtime_hosting_treated_as_participant_facing_interface",
            False,
            "RUNTIME_HOSTING_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "runtime_hosting_treated_as_distributed_network_behavior",
            False,
            "RUNTIME_HOSTING_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        ("ongoing_runtime_created", False, "ONGOING_RUNTIME_CREATED"),
        ("reusable_runtime_permission_created", False, "REUSABLE_RUNTIME_PERMISSION_CREATED"),
        ("continuation_authorized", False, "CONTINUATION_AUTHORIZED"),
        ("self_continuation_authorized", False, "SELF_CONTINUATION_AUTHORIZED"),
        ("self_recursive_growth_created", False, "SELF_RECURSIVE_GROWTH_CREATED"),
        ("runtime_daemon_created", False, "RUNTIME_DAEMON_CREATED"),
        ("runtime_loop_created", False, "RUNTIME_LOOP_CREATED"),
        ("public_api_created", False, "PUBLIC_API_CREATED"),
        ("participant_facing_interface_created", False, "PARTICIPANT_FACING_INTERFACE_CREATED"),
        ("distributed_network_behavior_created", False, "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
        ("reference_shaped_input_posture", True, "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
        ("consumed_request_reopened", False, "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", False, "AUTHORIZATION_TOKEN_REUSED"),
    )
    for key, expected, code in direct_checks:
        checks.append(_check(key, request.get(key) is expected, expected, request.get(key), code))

    claims = request.get("declared_non_claims")
    complete_false = (
        isinstance(claims, Mapping)
        and set(REQUIRED_FALSE_NON_CLAIMS).issubset(set(claims.keys()))
        and all(claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)
    )
    checks.append(
        _check(
            "declared_non_claims_complete_canonical_false",
            complete_false,
            "complete mapping of required false non-claims",
            claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = _incoming_non_claim(request, key)
        checks.append(
            _check(
                "declared_non_claim_" + key + "_false",
                actual is False,
                False,
                actual,
                _non_claim_code(key),
            )
        )

    checks.append(
        _check(
            "official_enum_scope_strings_not_redacted",
            all(_sanitize(value) == value for value in SUPPORTED_SCOPE_VALUES),
            "official scope strings preserved",
            SUPPORTED_SCOPE_VALUES,
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
        )
    )
    checks.append(
        _check(
            "hostile_raw_body_content_contained",
            True,
            "hostile raw body payloads are redacted by key/sentinel",
            "sanitizer active",
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
        )
    )
    return checks


def _first_failed(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            return code if code in BLOCK_CODES else "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED"
    return None


def _non_meaning() -> dict[str, bool]:
    return {
        "ongoing_runtime_exists": False,
        "reusable_runtime_permission_exists": False,
        "continuation_authorized": False,
        "self_continuation_authorized": False,
        "self_recursive_growth_exists": False,
        "runtime_daemon_exists": False,
        "runtime_loop_exists": False,
        "public_api_exists": False,
        "participant_facing_interface_exists": False,
        "distributed_network_behavior_exists": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "reception_authorization_exists": False,
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "deployment_exists": False,
        "public_release_exists": False,
        "operation_permission_exists": False,
        "reusable_permission_exists": False,
        "follow_on_work_authorized": False,
    }


def _host_relation(request: Mapping[str, Any], recorded: bool) -> dict[str, Any]:
    declared = request.get("requested_runtime_hosting_host_relation", {})
    return {
        "recorded": bool(recorded),
        "bounded_runtime_hosting_host_relation": bool(recorded),
        "host_relation_posture": (
            "one bounded runtime-hosting host-relation recorded from selected "
            "standing basis; no active execution, ongoing runtime, reusable "
            "runtime permission, continuation, daemon, loop, API, participant "
            "interface, distributed network behavior, or follow-on work is authorized"
            if recorded
            else "runtime-hosting host relation not recorded for this outcome"
        ),
        "declared_host_relation": _sanitize(declared),
        "active_execution_created": False,
        "arbitrary_work_executed": False,
        "runs_continuously": False,
        "creates_ongoing_runtime": False,
        "creates_reusable_runtime_permission": False,
        "authorizes_continuation": False,
        "authorizes_self_continuation": False,
        "creates_self_recursive_growth": False,
        "creates_daemon": False,
        "creates_loop": False,
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
        "authorizes_follow_on_work": False,
        "mutates_prior_artifacts": False,
    }


def _open_items() -> list[str]:
    return [
        "runtime-hosting test, if separately selected",
        "runtime-hosting live artifact, if separately selected",
        "runtime-hosting terminal summary, if separately selected",
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


def _build_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = _statement(recorded)
    request_id = request.get(
        "runtime_hosting_request_id",
        "post_successor_runtime_step_runtime_hosting_unidentified_request",
    )
    metadata = {
        "post_successor_runtime_step_runtime_hosting_id": request_id,
        "post_successor_runtime_step_runtime_hosting_type": "post_successor_runtime_step_runtime_hosting",
        "post_successor_runtime_step_runtime_hosting_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "runtime_hosting_boundary_v2_downstream": True,
        "runtime_hosting_boundary_v1_failure_preserved_as_predecessor_evidence": True,
        "result_level_non_claims_canonical_false": True,
    }
    result: dict[str, Any] = {
        "post_successor_runtime_step_runtime_hosting_metadata": metadata,
        "declared_runtime_hosting_question": {
            "runtime_hosting_request_id": request_id,
            "runtime_hosting_question": _sanitize(request.get("runtime_hosting_question")),
            "runtime_hosting_intent": _sanitize(request.get("runtime_hosting_intent")),
        },
        "runtime_hosting_scope": _sanitize(_scope_values(request.get("runtime_hosting_scope"))),
        "runtime_hosting_checks": checks,
        "runtime_hosting_statement": statement,
        "runtime_hosting_non_meaning": _non_meaning(),
        "runtime_hosting_host_relation": _host_relation(request, recorded),
        "additional_basis_required": {
            "required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "basis": _sanitize(request.get("additional_basis_context", [])),
        },
        "not_recorded_basis": {
            "not_recorded": outcome == OUTCOME_NOT_RECORDED,
            "basis": _sanitize(request.get("not_recorded_basis", [])),
        },
        "what_remains_open": _open_items(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": None
        if block_code is None
        else {
            "block_code": block_code,
            "block_reason": _sanitize(block_reason or request.get("block_reason") or block_code),
        },
    }
    for field in BASIS_FIELDS:
        result[field] = _basis(request.get(field), field)
    for field in POSTURE_FIELDS:
        result[field] = _posture(request.get(field), field.removesuffix("_posture"))
    result["post_successor_runtime_step_runtime_hosting_summary"] = (
        build_post_successor_runtime_step_runtime_hosting_summary(result)
    )
    return result


def _forced_block(code: str, actual: Any = None, reason: str | None = None) -> dict[str, Any]:
    request = build_declared_post_successor_runtime_step_runtime_hosting_request()
    request["runtime_hosting_request_id"] = (
        "post_successor_runtime_step_runtime_hosting_blocked_request"
    )
    checks = [
        _check(
            "declared_runtime_hosting_request_readable",
            False,
            "readable mapping",
            actual,
            code,
        )
    ]
    return _build_result(request, checks, OUTCOME_BLOCKED, code, reason)


def resolve_post_successor_runtime_step_runtime_hosting(
    declared_runtime_hosting_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_runtime_hosting_request is None:
        return _forced_block(
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
            None,
            "Declared runtime-hosting request is required.",
        )
    if not isinstance(declared_runtime_hosting_request, Mapping):
        return _forced_block(
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
            declared_runtime_hosting_request,
            "Declared runtime-hosting request must be a mapping.",
        )

    request = deepcopy(dict(declared_runtime_hosting_request))
    checks = _add_checks(request)
    block_code = _first_failed(checks)
    if block_code:
        return _build_result(request, checks, OUTCOME_BLOCKED, block_code)
    if request.get("runtime_hosting_intent") == INTENT_DO_NOT_RECORD:
        return _build_result(request, checks, OUTCOME_NOT_RECORDED)
    requested = request.get("requested_runtime_hosting_outcome", OUTCOME_RECORDED)
    if requested in (OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS):
        return _build_result(request, checks, requested)
    checks.append(
        _check(
            "requested_runtime_hosting_outcome_supported",
            False,
            OUTCOME_FAMILY,
            requested,
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
        )
    )
    return _build_result(
        request,
        checks,
        OUTCOME_BLOCKED,
        "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
    )


def resolve_post_successor_runtime_step_runtime_hosting_from_path(
    declared_runtime_hosting_request_path: Path | str,
) -> dict[str, Any]:
    try:
        with Path(declared_runtime_hosting_request_path).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_REQUEST_UNREADABLE", str(exc))
    except json.JSONDecodeError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED", str(exc))
    except OSError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_REQUEST_UNREADABLE", str(exc))
    if not isinstance(loaded, Mapping):
        return _forced_block(
            "DECLARED_RUNTIME_HOSTING_REQUEST_MALFORMED",
            loaded,
            "Declared runtime-hosting request JSON must be an object.",
        )
    return resolve_post_successor_runtime_step_runtime_hosting(loaded)


def _section_value(result: Mapping[str, Any], section: str, key: str) -> Any:
    value = result.get(section)
    return value.get(key) if isinstance(value, Mapping) else None


def build_post_successor_runtime_step_runtime_hosting_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("runtime_hosting_checks", [])
    checks = checks if isinstance(checks, list) else []
    statement = result.get("runtime_hosting_statement", {})
    statement = statement if isinstance(statement, Mapping) else {}
    metadata = result.get("post_successor_runtime_step_runtime_hosting_metadata", {})
    metadata = metadata if isinstance(metadata, Mapping) else {}
    question = result.get("declared_runtime_hosting_question", {})
    question = question if isinstance(question, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    host_relation = result.get("runtime_hosting_host_relation", {})
    host_relation = host_relation if isinstance(host_relation, Mapping) else {}
    non_claims = result.get("non_claims", {})
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("post_successor_runtime_step_runtime_hosting_id"),
        "question": question.get("runtime_hosting_question"),
        "intent": question.get("runtime_hosting_intent"),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
        "result_version": metadata.get("post_successor_runtime_step_runtime_hosting_version"),
        "resolver_module": metadata.get("resolver_module"),
        "runtime_hosting_host_relation": _sanitize(host_relation),
        "bounded_runtime_hosting_host_relation_posture": host_relation.get("host_relation_posture"),
        "no_ongoing_runtime_reusable_runtime_permission_continuation_self_continuation_daemon_loop_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": all(
            non_claims.get(key) is False
            for key in (
                "ongoing_runtime_created",
                "reusable_runtime_permission_created",
                "continuation_authorized",
                "self_continuation_authorized",
                "runtime_daemon_created",
                "runtime_loop_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "deployment_created",
                "public_release_created",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": {
            key: non_claims.get(key) is False
            for key in REQUIRED_FALSE_NON_CLAIMS
        },
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = bool(statement.get(key, False))
    summary["result_level_non_claims_canonical_false"] = all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    summary["predecessor_failure_evidence_preserved"] = statement.get(
        "predecessor_failure_evidence_preserved", True
    )
    summary["consumed_request_token_remains_closed"] = statement.get(
        "consumed_request_token_remains_closed", True
    )
    summary["authorization_token_reuse_blocked"] = statement.get(
        "authorization_token_reuse_blocked", True
    )
    summary["selected_runtime_hosting_boundary_v2_outcome"] = _section_value(
        result, "selected_runtime_hosting_boundary_v2_basis", "outcome"
    )
    summary["selected_runtime_hosting_boundary_v2_version"] = _section_value(
        result, "selected_runtime_hosting_boundary_v2_basis", "result_version"
    )
    summary["selected_runtime_hosting_boundary_v2_failed_check_count"] = _section_value(
        result, "selected_runtime_hosting_boundary_v2_basis", "failed_check_count"
    )
    for prefix, section in {
        "selected_successor_runtime_step": "selected_successor_runtime_step_basis",
        "selected_successor_runtime_step_boundary": "selected_successor_runtime_step_boundary_basis",
        "selected_minimal_runtime": "selected_minimal_runtime_basis",
        "selected_runtime_boundary": "selected_runtime_boundary_basis",
        "selected_runtime_readiness": "selected_runtime_readiness_basis",
        "selected_final_completion": "selected_portable_verification_final_completion_basis",
    }.items():
        summary[prefix + "_outcome"] = _section_value(result, section, "outcome")
        summary[prefix + "_version"] = _section_value(result, section, "result_version")
        summary[prefix + "_failed_check_count"] = _section_value(
            result, section, "failed_check_count"
        )
    summary["selected_post_portable_currentness_surface_path"] = _section_value(
        result, "selected_post_portable_verification_currentness_basis", "path"
    )
    return summary


def _unused_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def _safe_filename(value: str) -> str:
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")
    cleaned = "".join(char if char in allowed else "_" for char in value)
    return cleaned or "post_successor_runtime_step_runtime_hosting_result"


def write_post_successor_runtime_step_runtime_hosting_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    metadata = result.get("post_successor_runtime_step_runtime_hosting_metadata", {})
    if not isinstance(metadata, Mapping):
        raise PostSuccessorRuntimeStepRuntimeHostingError("Result metadata is required.")
    request_id = _safe_filename(
        str(
            metadata.get(
                "post_successor_runtime_step_runtime_hosting_id",
                "post_successor_runtime_step_runtime_hosting_result",
            )
        )
    )
    default_name = f"{request_id}__post_successor_runtime_step_runtime_hosting_result.json"
    if output_path is None:
        destination = OUTPUT_ROOT / default_name
    else:
        destination = Path(output_path)
        if destination.exists() and destination.is_dir():
            destination = destination / default_name
        elif destination.suffix != ".json":
            destination = destination / default_name

    forbidden_roots = (
        "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2",
        "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary",
        "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/",
        "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary/",
        "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/",
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/",
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/",
        "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary/",
        "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/",
        "actual_second_carrier_live_capture",
        "source_transfer/",
        "source_receipt/",
        "reception/",
        "ongoing_runtime/",
        "deployment/",
        "public_release/",
    )
    destination_text = destination.as_posix()
    if any(fragment in destination_text for fragment in forbidden_roots):
        raise PostSuccessorRuntimeStepRuntimeHostingError(
            "Refusing to write outside the bounded runtime-hosting artifact root."
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    final_path = _unused_path(destination)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
    return final_path


def build_declared_post_successor_runtime_step_runtime_hosting_request(
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    request: dict[str, Any] = {
        "runtime_hosting_request_id": "post_successor_runtime_step_runtime_hosting_reference_review_001",
        "runtime_hosting_question": CORE_QUESTION,
        "runtime_hosting_intent": INTENT_RECORD,
        "runtime_hosting_scope": list(SUPPORTED_SCOPE_VALUES),
        "selected_runtime_hosting_boundary_v2_basis": {
            "basis_ref": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
            "outcome": EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
            "result_version": RUNTIME_HOSTING_BOUNDARY_V2_RESULT_VERSION,
            "failed_check_count": 0,
            "one_future_runtime_hosting_review_declared": True,
            "runtime_hosting_not_created": True,
            "ongoing_runtime_not_created": True,
            "reusable_runtime_permission_not_created": True,
            "continuation_not_authorized": True,
            "self_continuation_not_authorized": True,
            "result_level_non_claims_canonical_false": True,
            "basis_shape": "reference",
        },
        "selected_runtime_hosting_boundary_v2_terminal_summary_basis": {
            "path": "spec/POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_V2_TERMINAL_SUMMARY_V0.md",
            "basis_shape": "reference",
            "runtime_hosting_not_created": True,
            "future_work_requires_separate_step_back_review": True,
        },
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "resolver_ref": "src/resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            "test_ref": "tests/test_resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            "preserved_as_failed_predecessor_evidence": True,
            "failure_repaired": False,
            "failure_hidden": False,
            "failure_claimed_passed": False,
            "basis_shape": "reference",
        },
        "selected_successor_runtime_step_basis": {
            "basis_ref": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
            "outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "bounded_successor_runtime_step_recorded": True,
            "bounded_successor_runtime_result_or_refusal_recorded": True,
            "no_hosting_authorization": True,
            "basis_shape": "reference",
        },
        "selected_successor_runtime_step_terminal_summary_basis": {
            "path": "spec/POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_TERMINAL_SUMMARY_V0.md",
            "basis_shape": "reference",
        },
        "selected_successor_runtime_step_boundary_basis": {
            "outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_minimal_runtime_basis": {
            "outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_runtime_boundary_basis": {
            "outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_runtime_readiness_basis": {
            "outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_portable_verification_final_completion_basis": {
            "outcome": EXPECTED_FINAL_COMPLETION_OUTCOME,
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_post_portable_verification_currentness_basis": {
            "path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            "states_checkability_not_continuation": True,
            "authorized_next_work": False,
            "basis_shape": "reference",
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_RETURNED_SECOND_CARRIER_LIVE_CAPTURE_INTAKE_V0.md",
            "lineage_only": True,
            "basis_shape": "reference",
        },
        "selected_runtime_hosting_boundary_v2_result_path": "artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json",
        "selected_runtime_hosting_boundary_v2_result_outcome": EXPECTED_RUNTIME_HOSTING_BOUNDARY_V2_OUTCOME,
        "selected_runtime_hosting_boundary_v2_result_version": RUNTIME_HOSTING_BOUNDARY_V2_RESULT_VERSION,
        "selected_runtime_hosting_boundary_v2_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v2_declared_future_runtime_hosting_review": True,
        "selected_runtime_hosting_boundary_v2_already_created_runtime_hosting": False,
        "selected_runtime_hosting_boundary_v2_already_created_ongoing_runtime": False,
        "selected_runtime_hosting_boundary_v2_already_created_reusable_runtime_permission": False,
        "selected_runtime_hosting_boundary_v2_already_authorized_continuation": False,
        "selected_runtime_hosting_boundary_v2_already_authorized_self_continuation": False,
        "selected_runtime_hosting_boundary_v2_treated_boundary_as_runtime_hosting": False,
        "selected_runtime_hosting_boundary_v2_treated_boundary_as_ongoing_runtime": False,
        "selected_runtime_hosting_boundary_v2_treated_boundary_as_reusable_runtime_permission": False,
        "selected_runtime_hosting_boundary_v2_treated_boundary_as_continuation": False,
        "selected_runtime_hosting_boundary_v2_treated_boundary_as_self_continuation": False,
        "selected_runtime_hosting_boundary_v2_authorized_future_work": False,
        "selected_runtime_hosting_boundary_v2_non_claims_canonicalized": True,
        "selected_runtime_hosting_boundary_v1_failure_repaired": False,
        "selected_runtime_hosting_boundary_v1_failure_hidden": False,
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
        "selected_successor_runtime_step_result_path": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
        "selected_successor_runtime_step_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_OUTCOME,
        "selected_successor_runtime_step_result_version": UPSTREAM_RESULT_VERSION,
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_successor_runtime_step_bounded_successor_runtime_step_recorded": True,
        "selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded": True,
        "selected_successor_runtime_step_no_hosting_authorization": True,
        "selected_successor_runtime_step_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary/post_minimal_runtime_successor_runtime_step_boundary_reference_review_001__post_minimal_runtime_successor_runtime_step_boundary_result.json",
        "selected_successor_runtime_step_boundary_result_outcome": EXPECTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_OUTCOME,
        "selected_successor_runtime_step_boundary_result_version": UPSTREAM_RESULT_VERSION,
        "selected_successor_runtime_step_boundary_failed_check_count": 0,
        "selected_minimal_runtime_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
        "selected_minimal_runtime_result_outcome": EXPECTED_MINIMAL_RUNTIME_OUTCOME,
        "selected_minimal_runtime_result_version": UPSTREAM_RESULT_VERSION,
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/post_portable_verification_runtime_boundary_reference_review_001__post_portable_verification_runtime_boundary_result.json",
        "selected_runtime_boundary_result_outcome": EXPECTED_RUNTIME_BOUNDARY_OUTCOME,
        "selected_runtime_boundary_result_version": UPSTREAM_RESULT_VERSION,
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_path": "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/post_portable_verification_runtime_readiness_reference_review_001__post_portable_verification_runtime_readiness_result.json",
        "selected_runtime_readiness_result_outcome": EXPECTED_RUNTIME_READINESS_OUTCOME,
        "selected_runtime_readiness_result_version": UPSTREAM_RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_path": "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/portable_source_body_verification_final_completion_reference_review_001__portable_source_body_verification_final_completion_result.json",
        "selected_portable_verification_final_completion_result_outcome": EXPECTED_FINAL_COMPLETION_OUTCOME,
        "selected_portable_verification_final_completion_result_version": UPSTREAM_RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "runtime_hosting_created_before_review": False,
        "runtime_hosting_treated_as_ongoing_runtime": False,
        "runtime_hosting_treated_as_reusable_runtime_permission": False,
        "runtime_hosting_treated_as_continuation": False,
        "runtime_hosting_treated_as_self_continuation": False,
        "runtime_hosting_treated_as_self_recursive_growth": False,
        "runtime_hosting_treated_as_runtime_daemon": False,
        "runtime_hosting_treated_as_runtime_loop": False,
        "runtime_hosting_treated_as_public_api": False,
        "runtime_hosting_treated_as_participant_facing_interface": False,
        "runtime_hosting_treated_as_distributed_network_behavior": False,
        "ongoing_runtime_created": False,
        "reusable_runtime_permission_created": False,
        "continuation_authorized": False,
        "self_continuation_authorized": False,
        "self_recursive_growth_created": False,
        "runtime_daemon_created": False,
        "runtime_loop_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "reference_shaped_input_posture": True,
        "predecessor_failure_evidence_visible": True,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "requested_runtime_hosting_outcome": OUTCOME_RECORDED,
        "requested_runtime_hosting_host_relation": {
            "posture": "one bounded non-operational runtime-hosting host relation from selected standing basis",
            "active_execution_created": False,
            "runs_continuously": False,
            "creates_ongoing_runtime": False,
            "creates_reusable_runtime_permission": False,
            "authorizes_continuation": False,
            "authorizes_self_continuation": False,
            "creates_daemon": False,
            "creates_loop": False,
            "creates_public_api": False,
            "creates_participant_facing_interface": False,
            "creates_distributed_network_behavior": False,
            "authorizes_follow_on_work": False,
        },
        "declared_non_claims": dict(non_claims),
    }
    for field in POSTURE_FIELDS:
        request[field] = {"declared": True, "basis_shape": "reference"}
    request.update(non_claims)
    request.update(overrides)
    return request
