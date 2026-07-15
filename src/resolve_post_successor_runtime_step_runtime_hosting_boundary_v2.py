"""Bounded v2 post-successor runtime-step runtime-hosting-boundary resolver.

The v1 resolver is preserved as failed predecessor evidence. This additive v2
resolver keeps the same boundary posture and corrects one defect: incoming
``declared_non_claims`` are validation input only. Emitted result-level
``non_claims`` are canonical false posture for every outcome.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Mapping


class PostSuccessorRuntimeStepRuntimeHostingBoundaryV2Error(Exception):
    """Bounded local resolver error."""


PostSuccessorRuntimeStepRuntimeHostingBoundaryError = (
    PostSuccessorRuntimeStepRuntimeHostingBoundaryV2Error
)


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(value.split())


RESULT_VERSION = "0.2.0"
UPSTREAM_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_successor_runtime_step_runtime_hosting_boundary_v2"

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

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2"
)

INTENT_RECORD = "RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
INTENT_BLOCK = "BLOCK_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

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

SUPPORTED_SCOPE_VALUES = _tokens(
    """
    RUNTIME_HOSTING_BOUNDARY_SPEC_ONLY ONE_FUTURE_RUNTIME_HOSTING_REVIEW_DECLARED
    SUCCESSOR_RUNTIME_STEP_BASIS_PRESERVED SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING
    BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_NOT_HOSTING_AUTHORIZATION
    RUNTIME_HOSTING_BOUNDARY_NOT_RUNTIME_HOSTING
    RUNTIME_HOSTING_BOUNDARY_NOT_ONGOING_RUNTIME
    RUNTIME_HOSTING_BOUNDARY_NOT_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_NOT_CONTINUATION RUNTIME_HOSTING_NOT_CREATED
    ONGOING_RUNTIME_NOT_CREATED REUSABLE_RUNTIME_PERMISSION_NOT_CREATED
    NO_CONTINUATION_AUTHORIZED SELF_CONTINUATION_NOT_AUTHORIZED
    RUNTIME_DAEMON_NOT_CREATED RUNTIME_LOOP_NOT_CREATED PUBLIC_API_NOT_CREATED
    PARTICIPANT_FACING_INTERFACE_NOT_CREATED DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED
    NO_SOURCE_TRANSFER NO_SOURCE_RECEIPT NO_RECEPTION_AUTHORIZATION NO_SOURCE_CREATED
    NO_AUTHORITY_CREATED NO_CURRENTNESS_CREATED NO_DEPLOYMENT_CREATED
    NO_PUBLIC_RELEASE_CREATED NO_OPERATION_PERMISSION_CREATED NO_REUSABLE_PERMISSION
    NO_DERIVATIVE_RECEPTION NO_VESSEL_RELATION NO_ANOTHER_RECEPTION_REQUEST
    NO_ADOPTION NO_RECEIVING_CONTEXT_GOVERNANCE NO_PUBLICATION_FLOW
    NO_FOLLOW_ON_WORK_AUTHORIZED NO_RUNTIME_HOSTING_INFERENCE
    NO_ONGOING_RUNTIME_INFERENCE NO_REUSABLE_RUNTIME_PERMISSION_INFERENCE
    NO_CONTINUATION_INFERENCE NO_SELF_CONTINUATION_INFERENCE NO_DAEMON_INFERENCE
    NO_LOOP_INFERENCE NO_PUBLIC_API_INFERENCE NO_PARTICIPANT_INTERFACE_INFERENCE
    NO_DISTRIBUTED_NETWORK_INFERENCE NO_SOURCE_INFERENCE NO_AUTHORITY_INFERENCE
    NO_CURRENTNESS_INFERENCE NO_DEPLOYMENT_INFERENCE NO_PUBLIC_RELEASE_INFERENCE
    NO_OPERATION_PERMISSION_INFERENCE NO_FOLLOW_ON_WORK_INFERENCE
    NO_UNBOUNDED_PASS_FAIL_INFERENCE HIDDEN_REPO_STATE_EXCLUDED
    HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    ARTIFACT_EXISTENCE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    LATEST_FILE_POSTURE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED
    OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED HOSTILE_RAW_BODY_CONTENT_CONTAINED
    PREDECESSOR_FAILURE_EVIDENCE_PRESERVED AUTHORIZATION_TOKEN_REUSE_BLOCKED
    CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED CONSUMED_REQUEST_NOT_REOPENED
    """
)
SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = _tokens(
    """
    runtime_hosting_created ongoing_runtime_created reusable_runtime_permission_created
    continuation_authorized self_continuation_authorized self_recursive_growth_created
    runtime_daemon_created runtime_loop_created public_api_created
    participant_facing_interface_created distributed_network_behavior_created
    source_transfer_occurred source_receipt_occurred reception_authorization_created
    runtime_hosting_boundary_treated_as_runtime_hosting
    runtime_hosting_boundary_treated_as_ongoing_runtime
    runtime_hosting_boundary_treated_as_reusable_runtime_permission
    runtime_hosting_boundary_treated_as_continuation
    runtime_hosting_boundary_treated_as_self_continuation
    runtime_hosting_boundary_treated_as_source_transfer
    runtime_hosting_boundary_treated_as_source_receipt
    runtime_hosting_boundary_treated_as_reception_authorization
    runtime_hosting_boundary_treated_as_source runtime_hosting_boundary_treated_as_authority
    runtime_hosting_boundary_treated_as_currentness
    runtime_hosting_boundary_treated_as_deployment
    runtime_hosting_boundary_treated_as_public_release
    runtime_hosting_boundary_treated_as_operation_permission
    runtime_hosting_boundary_treated_as_reusable_permission
    runtime_hosting_boundary_treated_as_follow_on_work
    successor_runtime_step_treated_as_runtime_hosting
    successor_runtime_step_treated_as_ongoing_runtime
    successor_runtime_step_treated_as_reusable_runtime_permission
    successor_runtime_step_treated_as_continuation
    successor_runtime_step_treated_as_self_continuation
    bounded_successor_runtime_result_or_refusal_authorized_hosting
    artifact_existence_treated_as_runtime_hosting_boundary_authority
    artifact_path_treated_as_currentness
    latest_file_posture_treated_as_runtime_hosting_boundary_authority
    repo_local_availability_treated_as_runtime_hosting_boundary_authority
    hidden_repo_state_used_as_runtime_hosting_boundary_content
    hidden_repo_state_used_as_runtime_hosting_boundary_authority
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
    runtime_hosting_boundary_recorded one_future_runtime_hosting_review_declared
    successor_runtime_step_basis_preserved successor_runtime_step_not_runtime_hosting
    bounded_successor_runtime_result_or_refusal_not_hosting_authorization
    runtime_hosting_boundary_not_runtime_hosting runtime_hosting_boundary_not_ongoing_runtime
    runtime_hosting_boundary_not_reusable_runtime_permission
    runtime_hosting_boundary_not_continuation runtime_hosting_not_created
    ongoing_runtime_not_created reusable_runtime_permission_not_created continuation_not_authorized
    self_continuation_not_authorized runtime_daemon_not_created runtime_loop_not_created
    public_api_not_created participant_facing_interface_not_created
    distributed_network_behavior_not_created source_transfer_not_created source_receipt_not_created
    reception_authorization_not_created source_not_created authority_not_created
    currentness_not_created deployment_not_created public_release_not_created
    operation_permission_not_created reusable_permission_not_created follow_on_work_not_authorized
    hidden_repo_state_excluded hidden_repo_state_not_used_as_runtime_hosting_boundary_authority
    repo_local_availability_not_runtime_hosting_boundary_authority
    artifact_existence_not_runtime_hosting_boundary_authority
    latest_file_posture_not_runtime_hosting_boundary_authority
    selected_basis_reference_shape_preserved raw_full_prior_artifact_body_not_returned
    official_enum_scope_strings_not_redacted hostile_raw_body_content_contained
    predecessor_failure_evidence_preserved authorization_token_reuse_blocked
    consumed_request_token_remains_closed
    """
)

BLOCK_CODES = _tokens(
    """
    RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED
    RUNTIME_HOSTING_BOUNDARY_REQUEST_DECLARED_BLOCK SUCCESSOR_RUNTIME_STEP_BASIS_MISSING
    SUCCESSOR_RUNTIME_STEP_NOT_RECORDED SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT
    SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0
    SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP
    SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL
    SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_RUNTIME_HOSTING
    SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_ONGOING_RUNTIME
    SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION
    SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_CONTINUATION
    SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_SELF_CONTINUATION
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION
    SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION
    SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK
    BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING
    RUNTIME_HOSTING_BOUNDARY_CREATED_BEFORE_REVIEW RUNTIME_HOSTING_CREATED
    ONGOING_RUNTIME_CREATED REUSABLE_RUNTIME_PERMISSION_CREATED CONTINUATION_AUTHORIZED
    SELF_CONTINUATION_AUTHORIZED SELF_RECURSIVE_GROWTH_CREATED RUNTIME_DAEMON_CREATED
    RUNTIME_LOOP_CREATED PUBLIC_API_CREATED PARTICIPANT_FACING_INTERFACE_CREATED
    DISTRIBUTED_NETWORK_BEHAVIOR_CREATED RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RUNTIME_HOSTING
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_ONGOING_RUNTIME
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SELF_CONTINUATION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_TRANSFER
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_RECEIPT
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE RUNTIME_HOSTING_BOUNDARY_TREATED_AS_AUTHORITY
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CURRENTNESS
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_DEPLOYMENT
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_PUBLIC_RELEASE
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_OPERATION_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION
    RUNTIME_HOSTING_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK SOURCE_TRANSFER_OCCURRED
    SOURCE_RECEIPT_OCCURRED RECEPTION_AUTHORIZATION_CREATED SOURCE_CREATED AUTHORITY_CREATED
    CURRENTNESS_CREATED DEPLOYMENT_CREATED PUBLIC_RELEASE_CREATED OPERATION_PERMISSION_CREATED
    REUSABLE_PERMISSION_CREATED DERIVATIVE_RECEPTION_AUTHORIZED VESSEL_RELATION_AUTHORIZED
    ANOTHER_RECEPTION_REQUEST_AUTHORIZED ADOPTION_CREATED RECEIVING_CONTEXT_GOVERNANCE_CREATED
    PUBLICATION_FLOW_CREATED FOLLOW_ON_WORK_AUTHORIZED
    ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    ARTIFACT_PATH_TREATED_AS_CURRENTNESS
    LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_CONTENT
    HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY
    SELECTED_BASIS_NOT_REFERENCE_SHAPED RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED
    PRIOR_ARTIFACTS_MUTATED PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED
    CONSUMED_REQUEST_REOPENED AUTHORIZATION_TOKEN_REUSED NON_CLAIM_MISSING_OR_FLIPPED
    UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED
    DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE
    SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED
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
    """
)

BASIS_FIELDS = _tokens(
    """
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
    runtime_hosting_boundary_spec_only_posture one_future_runtime_hosting_review_posture
    successor_runtime_step_basis_preserved_posture successor_runtime_step_not_runtime_hosting_posture
    bounded_successor_runtime_result_or_refusal_not_hosting_authorization_posture
    runtime_hosting_boundary_not_runtime_hosting_posture
    runtime_hosting_boundary_not_ongoing_runtime_posture
    runtime_hosting_boundary_not_reusable_runtime_permission_posture
    runtime_hosting_boundary_not_continuation_posture runtime_hosting_not_created_posture
    ongoing_runtime_not_created_posture reusable_runtime_permission_not_created_posture
    continuation_not_authorized_posture self_continuation_not_authorized_posture
    runtime_daemon_not_created_posture runtime_loop_not_created_posture public_api_not_created_posture
    participant_facing_interface_not_created_posture distributed_network_behavior_not_created_posture
    source_transfer_not_created_posture source_receipt_not_created_posture
    reception_authorization_not_created_posture source_not_created_posture authority_not_created_posture
    currentness_not_created_posture deployment_not_created_posture public_release_not_created_posture
    operation_permission_not_created_posture reusable_permission_not_created_posture
    follow_on_work_not_authorized_posture hidden_repo_state_excluded_posture
    repo_local_availability_not_runtime_hosting_boundary_authority_posture
    artifact_existence_not_runtime_hosting_boundary_authority_posture
    latest_file_posture_not_runtime_hosting_boundary_authority_posture
    selected_basis_reference_shape_posture raw_full_prior_artifact_body_not_returned_posture
    official_enum_scope_strings_not_redacted_posture hostile_raw_body_content_contained_posture
    predecessor_failure_evidence_preserved_posture
    """
)

RAW_KEY_FRAGMENTS = (
    "raw_body", "raw_full_body", "full_body", "artifact_body", "raw_", "runtime_body",
    "runtime_hosting_body", "runtime_hosting_boundary_body", "ongoing_runtime_body",
    "source_body", "authority_body", "hidden_repo_state", "current_working_tree",
    "local_cache", "repo_local_only_dependency",
)
HOSTILE_SENTINELS = (
    "RAW_RUNTIME_HOSTING_BOUNDARY_BODY_MUST_NOT_RETURN",
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
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            key_lower = key_text.lower()
            if any(fragment in key_lower for fragment in RAW_KEY_FRAGMENTS):
                result[key_text] = REDACTED_RAW_OR_HIDDEN
            else:
                result[key_text] = _sanitize(item)
        return result
    if isinstance(value, (list, tuple, set)):
        return [_sanitize(item) for item in value]
    if isinstance(value, str):
        if value in SUPPORTED_SCOPE_VALUES or value in BLOCK_CODES or value in OUTCOME_FAMILY:
            return value
        if "MUST_NOT_RETURN" in value or "SHOULD_NOT_RETURN" in value:
            return REDACTED_RAW_OR_HIDDEN
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return REDACTED_RAW_OR_HIDDEN
    return value


def _check(name: str, passed: bool, expected: Any, actual: Any, code: str) -> dict[str, Any]:
    if code not in BLOCK_CODES:
        code = "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED"
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


def _basis_missing_code(field: str) -> str:
    mapping = {
        "selected_successor_runtime_step_basis": "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        "selected_successor_runtime_step_terminal_summary_basis": "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
        "selected_successor_runtime_step_boundary_basis": "SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING",
        "selected_minimal_runtime_basis": "MINIMAL_RUNTIME_BASIS_MISSING",
        "selected_runtime_boundary_basis": "RUNTIME_BOUNDARY_BASIS_MISSING",
        "selected_runtime_readiness_basis": "RUNTIME_READINESS_BASIS_MISSING",
        "selected_portable_verification_final_completion_basis": "FINAL_COMPLETION_BASIS_MISSING",
        "selected_post_portable_verification_currentness_basis": "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    }
    return mapping.get(field, "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED")


def _non_claim_code(key: str) -> str:
    mapping = {
        "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
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
        "bounded_successor_runtime_result_or_refusal_authorized_hosting": "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
        "artifact_existence_treated_as_runtime_hosting_boundary_authority": "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
        "artifact_path_treated_as_currentness": "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
        "latest_file_posture_treated_as_runtime_hosting_boundary_authority": "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
        "repo_local_availability_treated_as_runtime_hosting_boundary_authority": "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
        "hidden_repo_state_used_as_runtime_hosting_boundary_content": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_CONTENT",
        "hidden_repo_state_used_as_runtime_hosting_boundary_authority": "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
        "raw_full_prior_artifact_body_returned": "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
        "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
        "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
        "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
        "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    }
    if key in mapping:
        return mapping[key]
    if key.startswith("runtime_hosting_boundary_treated_as_"):
        code = "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_" + key.removeprefix(
            "runtime_hosting_boundary_treated_as_"
        ).upper()
        return code if code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    if key.startswith("successor_runtime_step_treated_as_"):
        code = "SUCCESSOR_RUNTIME_STEP_TREATED_AS_" + key.removeprefix(
            "successor_runtime_step_treated_as_"
        ).upper()
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
    return result


def _posture(value: Any, key: str) -> dict[str, Any]:
    sanitized = _sanitize(value)
    result = dict(sanitized) if isinstance(sanitized, Mapping) else {"declared": value is not False}
    result.setdefault(key, True)
    result.setdefault("creates_runtime_hosting", False)
    result.setdefault("creates_ongoing_runtime", False)
    result.setdefault("creates_reusable_runtime_permission", False)
    result.setdefault("authorizes_continuation", False)
    return result


def _add_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks = [
        _check(
            "runtime_hosting_boundary_question_declared",
            request.get("runtime_hosting_boundary_question") == CORE_QUESTION,
            CORE_QUESTION,
            request.get("runtime_hosting_boundary_question"),
            "RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED",
        ),
        _check(
            "runtime_hosting_boundary_intent_supported",
            request.get("runtime_hosting_boundary_intent") in (INTENT_RECORD, INTENT_DO_NOT_RECORD),
            (INTENT_RECORD, INTENT_DO_NOT_RECORD),
            request.get("runtime_hosting_boundary_intent"),
            "RUNTIME_HOSTING_BOUNDARY_REQUEST_DECLARED_BLOCK"
            if request.get("runtime_hosting_boundary_intent") == INTENT_BLOCK
            else "RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED",
        ),
    ]
    scope = _scope_values(request.get("runtime_hosting_boundary_scope"))
    unsupported_scope = [item for item in scope if item not in SUPPORTED_SCOPE_VALUES]
    checks.append(
        _check(
            "runtime_hosting_boundary_scope_supported",
            not unsupported_scope,
            "all scope values supported",
            unsupported_scope or scope,
            "UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
        )
    )
    for field in BASIS_FIELDS:
        checks.append(
            _check(field + "_declared", _declared(request.get(field)), "declared", request.get(field), _basis_missing_code(field))
        )
    for field in POSTURE_FIELDS:
        checks.append(
            _check(field + "_declared", _declared(request.get(field)), "declared", request.get(field), "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED")
        )
    upstream = (
        ("successor_runtime_step", "selected_successor_runtime_step_result_outcome", "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED", "selected_successor_runtime_step_result_version", "selected_successor_runtime_step_failed_check_count", "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED", "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0", "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT"),
        ("successor_runtime_step_boundary", "selected_successor_runtime_step_boundary_result_outcome", "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_RECORDED", "selected_successor_runtime_step_boundary_result_version", "selected_successor_runtime_step_boundary_failed_check_count", "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED", "SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0", "SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT"),
        ("minimal_runtime", "selected_minimal_runtime_result_outcome", "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED", "selected_minimal_runtime_result_version", "selected_minimal_runtime_failed_check_count", "MINIMAL_RUNTIME_NOT_RECORDED", "MINIMAL_RUNTIME_VERSION_NOT_0_1_0", "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT"),
        ("runtime_boundary", "selected_runtime_boundary_result_outcome", "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED", "selected_runtime_boundary_result_version", "selected_runtime_boundary_failed_check_count", "RUNTIME_BOUNDARY_NOT_RECORDED", "RUNTIME_BOUNDARY_VERSION_NOT_0_1_0", "RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT"),
        ("runtime_readiness", "selected_runtime_readiness_result_outcome", "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED", "selected_runtime_readiness_result_version", "selected_runtime_readiness_failed_check_count", "RUNTIME_READINESS_NOT_RECORDED", "RUNTIME_READINESS_VERSION_NOT_0_1_0", "RUNTIME_READINESS_FAILED_CHECKS_PRESENT"),
        ("final_completion", "selected_portable_verification_final_completion_result_outcome", "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED", "selected_portable_verification_final_completion_result_version", "selected_portable_verification_final_completion_failed_check_count", "FINAL_COMPLETION_NOT_RECORDED", "FINAL_COMPLETION_VERSION_NOT_0_1_0", "FINAL_COMPLETION_FAILED_CHECKS_PRESENT"),
    )
    for name, outcome_key, outcome, version_key, failed_key, outcome_code, version_code, failed_code in upstream:
        checks.append(_check(name + "_outcome_recorded", request.get(outcome_key) == outcome, outcome, request.get(outcome_key), outcome_code))
        checks.append(_check(name + "_version_0_1_0", request.get(version_key) == UPSTREAM_RESULT_VERSION, UPSTREAM_RESULT_VERSION, request.get(version_key), version_code))
        checks.append(_check(name + "_failed_checks_zero", request.get(failed_key) == 0, 0, request.get(failed_key), failed_code))
    direct_checks = (
        ("selected_successor_runtime_step_bounded_successor_runtime_step_recorded", True, "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP"),
        ("selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded", True, "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL"),
        ("selected_successor_runtime_step_no_successor_after_successor_action_authorized", True, "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK"),
        ("selected_successor_runtime_step_already_created_runtime_hosting", False, "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_RUNTIME_HOSTING"),
        ("selected_successor_runtime_step_already_created_ongoing_runtime", False, "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_ONGOING_RUNTIME"),
        ("selected_successor_runtime_step_already_created_reusable_runtime_permission", False, "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION"),
        ("selected_successor_runtime_step_already_authorized_continuation", False, "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_CONTINUATION"),
        ("selected_successor_runtime_step_already_authorized_self_continuation", False, "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_SELF_CONTINUATION"),
        ("selected_successor_runtime_step_treated_as_runtime_hosting", False, "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING"),
        ("selected_successor_runtime_step_treated_as_ongoing_runtime", False, "SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME"),
        ("selected_successor_runtime_step_treated_as_reusable_runtime_permission", False, "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION"),
        ("selected_successor_runtime_step_treated_as_continuation", False, "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION"),
        ("selected_successor_runtime_step_treated_as_self_continuation", False, "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION"),
        ("selected_successor_runtime_step_authorized_future_work", False, "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK"),
        ("selected_bounded_successor_runtime_result_or_refusal_authorized_hosting", False, "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING"),
        ("runtime_hosting_boundary_created_before_review", False, "RUNTIME_HOSTING_BOUNDARY_CREATED_BEFORE_REVIEW"),
        ("selected_post_portable_currentness_surface_states_checkability_not_continuation", True, "POST_PORTABLE_CURRENTNESS_SURFACE_DID_NOT_PRESERVE_CHECKABILITY_NOT_CONTINUATION"),
        ("selected_post_portable_currentness_surface_authorized_next_work", False, "FOLLOW_ON_WORK_AUTHORIZED"),
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
        checks.append(_check("declared_non_claim_" + key + "_false", actual is False, False, actual, _non_claim_code(key)))
    return checks


def _first_failed(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            return code if code in BLOCK_CODES else "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED"
    return None


def _non_meaning() -> dict[str, bool]:
    return {
        "runtime_hosting_exists": False,
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
        "follow_on_work_authorized": False,
    }


def _open_items() -> list[str]:
    return [
        "runtime-hosting-boundary terminal summary, if separately selected",
        "runtime-hosting specification",
        "runtime hosting",
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
    statement = _statement(outcome == OUTCOME_RECORDED)
    metadata = {
        "post_successor_runtime_step_runtime_hosting_boundary_id": request.get(
            "runtime_hosting_boundary_request_id",
            "post_successor_runtime_step_runtime_hosting_boundary_v2_unidentified_request",
        ),
        "post_successor_runtime_step_runtime_hosting_boundary_type": "post_successor_runtime_step_runtime_hosting_boundary",
        "post_successor_runtime_step_runtime_hosting_boundary_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "v1_failure_preserved_as_predecessor_evidence": True,
        "non_claims_canonicalized": True,
    }
    result: dict[str, Any] = {
        "post_successor_runtime_step_runtime_hosting_boundary_metadata": metadata,
        "declared_runtime_hosting_boundary_question": {
            "runtime_hosting_boundary_request_id": metadata[
                "post_successor_runtime_step_runtime_hosting_boundary_id"
            ],
            "runtime_hosting_boundary_question": _sanitize(request.get("runtime_hosting_boundary_question")),
            "runtime_hosting_boundary_intent": _sanitize(request.get("runtime_hosting_boundary_intent")),
        },
        "runtime_hosting_boundary_scope": _sanitize(_scope_values(request.get("runtime_hosting_boundary_scope"))),
        "runtime_hosting_boundary_checks": checks,
        "runtime_hosting_boundary_statement": statement,
        "runtime_hosting_boundary_non_meaning": _non_meaning(),
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
    result["post_successor_runtime_step_runtime_hosting_boundary_summary"] = (
        build_post_successor_runtime_step_runtime_hosting_boundary_v2_summary(result)
    )
    return result


def _forced_block(code: str, actual: Any = None, reason: str | None = None) -> dict[str, Any]:
    request = build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request()
    request["runtime_hosting_boundary_request_id"] = "post_successor_runtime_step_runtime_hosting_boundary_v2_blocked_request"
    checks = [_check("declared_runtime_hosting_boundary_request_readable", False, "readable mapping", actual, code)]
    return _build_result(request, checks, OUTCOME_BLOCKED, code, reason)


def resolve_post_successor_runtime_step_runtime_hosting_boundary_v2(
    declared_runtime_hosting_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_runtime_hosting_boundary_request is None:
        request = build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request()
    elif not isinstance(declared_runtime_hosting_boundary_request, Mapping):
        return _forced_block(
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
            declared_runtime_hosting_boundary_request,
            "Declared runtime-hosting-boundary request must be a mapping.",
        )
    else:
        request = deepcopy(dict(declared_runtime_hosting_boundary_request))
    checks = _add_checks(request)
    block_code = _first_failed(checks)
    if block_code:
        return _build_result(request, checks, OUTCOME_BLOCKED, block_code)
    if request.get("runtime_hosting_boundary_intent") == INTENT_DO_NOT_RECORD:
        return _build_result(request, checks, OUTCOME_NOT_RECORDED)
    requested = request.get("requested_runtime_hosting_boundary_outcome", OUTCOME_RECORDED)
    if requested in (OUTCOME_RECORDED, OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS):
        return _build_result(request, checks, requested)
    checks.append(
        _check(
            "requested_runtime_hosting_boundary_outcome_supported",
            False,
            OUTCOME_FAMILY,
            requested,
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
        )
    )
    return _build_result(
        request,
        checks,
        OUTCOME_BLOCKED,
        "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
    )


def resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path(
    declared_runtime_hosting_boundary_request_path: Path | str,
) -> dict[str, Any]:
    try:
        with Path(declared_runtime_hosting_boundary_request_path).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE", str(exc))
    except json.JSONDecodeError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED", str(exc))
    except OSError as exc:
        return _forced_block("DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE", str(exc))
    return resolve_post_successor_runtime_step_runtime_hosting_boundary_v2(loaded)


def _section_value(result: Mapping[str, Any], section: str, key: str) -> Any:
    value = result.get(section)
    return value.get(key) if isinstance(value, Mapping) else None


def build_post_successor_runtime_step_runtime_hosting_boundary_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("runtime_hosting_boundary_checks", [])
    checks = checks if isinstance(checks, list) else []
    statement = result.get("runtime_hosting_boundary_statement", {})
    statement = statement if isinstance(statement, Mapping) else {}
    metadata = result.get("post_successor_runtime_step_runtime_hosting_boundary_metadata", {})
    metadata = metadata if isinstance(metadata, Mapping) else {}
    question = result.get("declared_runtime_hosting_boundary_question", {})
    question = question if isinstance(question, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("post_successor_runtime_step_runtime_hosting_boundary_id"),
        "question": question.get("runtime_hosting_boundary_question"),
        "intent": question.get("runtime_hosting_boundary_intent"),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
        "result_version": metadata.get("post_successor_runtime_step_runtime_hosting_boundary_version"),
        "resolver_module": metadata.get("resolver_module"),
        "non_claims_canonicalized": True,
        "predecessor_failure_evidence_preserved": statement.get("predecessor_failure_evidence_preserved", True),
        "consumed_request_token_remains_closed": statement.get("consumed_request_token_remains_closed", True),
        "authorization_token_reuse_blocked": statement.get("authorization_token_reuse_blocked", True),
    }
    summary_sections = {
        "selected_successor_runtime_step": "selected_successor_runtime_step_basis",
        "selected_successor_runtime_step_boundary": "selected_successor_runtime_step_boundary_basis",
        "selected_minimal_runtime": "selected_minimal_runtime_basis",
        "selected_runtime_boundary": "selected_runtime_boundary_basis",
        "selected_runtime_readiness": "selected_runtime_readiness_basis",
        "selected_final_completion": "selected_portable_verification_final_completion_basis",
    }
    for prefix, section in summary_sections.items():
        summary[prefix + "_outcome"] = _section_value(result, section, "outcome")
        summary[prefix + "_version"] = _section_value(result, section, "result_version")
        summary[prefix + "_failed_check_count"] = _section_value(result, section, "failed_check_count")
    summary["selected_post_portable_currentness_surface_path"] = _section_value(
        result, "selected_post_portable_verification_currentness_basis", "path"
    )
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = bool(statement.get(key, False))
    non_claims = result.get("non_claims", {})
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = non_claims.get(key) is False
    return summary


def write_post_successor_runtime_step_runtime_hosting_boundary_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    metadata = result.get("post_successor_runtime_step_runtime_hosting_boundary_metadata", {})
    if not isinstance(metadata, Mapping):
        raise PostSuccessorRuntimeStepRuntimeHostingBoundaryV2Error("Result metadata is required.")
    request_id = str(
        metadata.get(
            "post_successor_runtime_step_runtime_hosting_boundary_id",
            "post_successor_runtime_step_runtime_hosting_boundary_v2_result",
        )
    )
    destination = (
        OUTPUT_ROOT
        / f"{request_id}__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json"
        if output_path is None
        else Path(output_path)
    )
    if destination.exists() and destination.is_dir():
        destination = destination / f"{request_id}__post_successor_runtime_step_runtime_hosting_boundary_v2_result.json"
    forbidden = (
        "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary/",
        "actual_second_carrier_live_capture",
        "runtime_hosting/",
        "ongoing_runtime/",
        "deployment/",
        "public_release/",
        "source_transfer/",
        "source_receipt/",
        "reception",
    )
    if any(fragment in destination.as_posix() for fragment in forbidden):
        raise PostSuccessorRuntimeStepRuntimeHostingBoundaryV2Error(
            "Refusing to write outside the bounded v2 runtime-hosting-boundary root."
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    final_path = _unused_path(destination)
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
    return final_path


def _unused_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    request: dict[str, Any] = {
        "runtime_hosting_boundary_request_id": "post_successor_runtime_step_runtime_hosting_boundary_v2_reference_review_001",
        "runtime_hosting_boundary_question": CORE_QUESTION,
        "runtime_hosting_boundary_intent": INTENT_RECORD,
        "runtime_hosting_boundary_scope": list(SUPPORTED_SCOPE_VALUES),
        "selected_successor_runtime_step_basis": {
            "basis_ref": "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
            "outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_successor_runtime_step_terminal_summary_basis": {
            "path": "spec/POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_TERMINAL_SUMMARY_V0.md",
            "basis_shape": "reference",
        },
        "selected_successor_runtime_step_boundary_basis": {
            "outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_RECORDED",
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_minimal_runtime_basis": {
            "outcome": "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_runtime_boundary_basis": {
            "outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_runtime_readiness_basis": {
            "outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            "result_version": UPSTREAM_RESULT_VERSION,
            "failed_check_count": 0,
            "basis_shape": "reference",
        },
        "selected_portable_verification_final_completion_basis": {
            "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
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
        "selected_successor_runtime_step_result_outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        "selected_successor_runtime_step_result_version": UPSTREAM_RESULT_VERSION,
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
        "selected_successor_runtime_step_boundary_result_outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_RECORDED",
        "selected_successor_runtime_step_boundary_result_version": UPSTREAM_RESULT_VERSION,
        "selected_successor_runtime_step_boundary_failed_check_count": 0,
        "selected_minimal_runtime_result_outcome": "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        "selected_minimal_runtime_result_version": UPSTREAM_RESULT_VERSION,
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
        "selected_runtime_boundary_result_version": UPSTREAM_RESULT_VERSION,
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
        "selected_runtime_readiness_result_version": UPSTREAM_RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
        "selected_portable_verification_final_completion_result_version": UPSTREAM_RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "runtime_hosting_boundary_created_before_review": False,
        "declared_non_claims": dict(non_claims),
        "requested_runtime_hosting_boundary_outcome": OUTCOME_RECORDED,
    }
    for field in POSTURE_FIELDS:
        request[field] = {"declared": True, "basis_shape": "reference"}
    request.update(non_claims)
    request.update(overrides)
    return request


resolve_post_successor_runtime_step_runtime_hosting_boundary = (
    resolve_post_successor_runtime_step_runtime_hosting_boundary_v2
)
resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path = (
    resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path
)
write_post_successor_runtime_step_runtime_hosting_boundary_result = (
    write_post_successor_runtime_step_runtime_hosting_boundary_v2_result
)
build_post_successor_runtime_step_runtime_hosting_boundary_summary = (
    build_post_successor_runtime_step_runtime_hosting_boundary_v2_summary
)
build_declared_post_successor_runtime_step_runtime_hosting_boundary_request = (
    build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request
)
