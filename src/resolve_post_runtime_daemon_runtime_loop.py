"""Post-runtime-daemon runtime-loop resolver.

This module records one bounded runtime-loop posture downstream of the
runtime-loop-boundary line. It does not create a public API,
participant-facing interface, distributed network behavior, source transfer,
source receipt, reception authorization, source, authority, currentness,
deployment, public release, operation permission, broader reusable permission,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class PostRuntimeDaemonRuntimeLoopError(ValueError):
    """Raised when a runtime-loop request cannot be read as bounded input."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_post_runtime_daemon_runtime_loop"

OUTCOME_RECORDED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_RECORDED"
OUTCOME_NOT_RECORDED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "POST_RUNTIME_DAEMON_RUNTIME_LOOP_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_POST_RUNTIME_DAEMON_RUNTIME_LOOP"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_POST_RUNTIME_DAEMON_RUNTIME_LOOP"
INTENT_BLOCK = "BLOCK_POST_RUNTIME_DAEMON_RUNTIME_LOOP"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"
)

RUNTIME_LOOP_QUESTION = (
    "Can the clean post-runtime-daemon runtime-loop-boundary basis be used to "
    "record one bounded runtime-loop posture without creating public API, "
    "participant-facing interface, distributed network behavior, source "
    "transfer, source receipt, reception authorization, source, authority, "
    "currentness, deployment, public release, operation permission, broader "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, adoption, receiving-context governance, publication "
    "flow, or follow-on work?"
)

SUPPORTED_SCOPE_VALUES = (
    "RUNTIME_LOOP_SPEC_ONLY",
    "ONE_BOUNDED_RUNTIME_LOOP_POSTURE_RECORDED",
    "RUNTIME_LOOP_BOUNDARY_BASIS_PRESERVED",
    "RUNTIME_DAEMON_BASIS_PRESERVED",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_PRESERVED",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_DECLARED",
    "RUNTIME_LOOP_NOT_PUBLIC_API",
    "RUNTIME_LOOP_NOT_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
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
    "NO_BROADER_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_ADOPTION",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "NO_PUBLICATION_FLOW",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
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
    "HIDDEN_REPO_STATE_NOT_USED_AS_RUNTIME_LOOP_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_LOOP_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_LOOP_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_LOOP_AUTHORITY",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)
SUPPORTED_RUNTIME_LOOP_SCOPE = SUPPORTED_SCOPE_VALUES

REQUIRED_FALSE_NON_CLAIMS = (
    "runtime_loop_recorded_before_review",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_loop_treated_as_public_api",
    "runtime_loop_treated_as_participant_facing_interface",
    "runtime_loop_treated_as_distributed_network_behavior",
    "runtime_loop_treated_as_source_transfer",
    "runtime_loop_treated_as_source_receipt",
    "runtime_loop_treated_as_reception_authorization",
    "runtime_loop_treated_as_source",
    "runtime_loop_treated_as_authority",
    "runtime_loop_treated_as_currentness",
    "runtime_loop_treated_as_deployment",
    "runtime_loop_treated_as_public_release",
    "runtime_loop_treated_as_operation_permission",
    "runtime_loop_treated_as_broader_reusable_permission",
    "runtime_loop_treated_as_follow_on_work",
    "runtime_loop_boundary_treated_as_runtime_loop_without_review",
    "runtime_daemon_treated_as_runtime_loop_without_review",
    "bounded_runtime_daemon_envelope_treated_as_runtime_loop_without_review",
    "artifact_existence_treated_as_runtime_loop_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_loop_authority",
    "repo_local_availability_treated_as_runtime_loop_authority",
    "hidden_repo_state_used_as_runtime_loop_content",
    "hidden_repo_state_used_as_runtime_loop_authority",
    "source_created",
    "authority_created",
    "currentness_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
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
    "runtime_daemon_boundary_v1_failure_hidden",
    "runtime_daemon_boundary_v1_failure_repaired",
    "runtime_daemon_boundary_v1_failure_claimed_passed",
    "runtime_hosting_boundary_v1_failure_hidden",
    "runtime_hosting_boundary_v1_failure_repaired",
    "runtime_hosting_boundary_v1_failure_claimed_passed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "runtime_loop_recorded",
    "bounded_runtime_loop_posture_recorded",
    "runtime_loop_boundary_basis_preserved",
    "runtime_daemon_basis_preserved",
    "bounded_runtime_daemon_envelope_preserved",
    "bounded_runtime_loop_envelope_declared",
    "runtime_loop_not_public_api",
    "runtime_loop_not_participant_facing_interface",
    "runtime_loop_not_distributed_network_behavior",
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
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_runtime_loop_authority",
    "repo_local_availability_not_runtime_loop_authority",
    "artifact_existence_not_runtime_loop_authority",
    "latest_file_posture_not_runtime_loop_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "RUNTIME_LOOP_QUESTION_UNDECLARED",
    "RUNTIME_LOOP_INTENT_UNSUPPORTED",
    "RUNTIME_LOOP_BOUNDARY_BASIS_MISSING",
    "RUNTIME_LOOP_BOUNDARY_NOT_RECORDED",
    "RUNTIME_LOOP_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_LOOP_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_LOOP_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_LOOP_REVIEW",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_DAEMON_BASIS_MISSING",
    "RUNTIME_DAEMON_NOT_RECORDED",
    "RUNTIME_DAEMON_FAILED_CHECKS_PRESENT",
    "RUNTIME_DAEMON_VERSION_NOT_0_1_0",
    "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_POSTURE",
    "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_ENVELOPE",
    "RUNTIME_DAEMON_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_DAEMON_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_DAEMON_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP_BEFORE_REVIEW",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
    "RUNTIME_DAEMON_BOUNDARY_BASIS_MISSING",
    "RUNTIME_DAEMON_BOUNDARY_NOT_RECORDED",
    "RUNTIME_DAEMON_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_DAEMON_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "RUNTIME_LOOP_RECORDED_BEFORE_REVIEW",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP_WITHOUT_REVIEW",
    "RUNTIME_DAEMON_TREATED_AS_RUNTIME_LOOP_WITHOUT_REVIEW",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_PUBLIC_API",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_LOOP_TREATED_AS_PUBLIC_API",
    "RUNTIME_LOOP_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_LOOP_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_LOOP_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_LOOP_TREATED_AS_SOURCE",
    "RUNTIME_LOOP_TREATED_AS_AUTHORITY",
    "RUNTIME_LOOP_TREATED_AS_CURRENTNESS",
    "RUNTIME_LOOP_TREATED_AS_DEPLOYMENT",
    "RUNTIME_LOOP_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_LOOP_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_LOOP_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "RUNTIME_LOOP_TREATED_AS_FOLLOW_ON_WORK",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_LOOP_SCOPE",
    "DECLARED_RUNTIME_LOOP_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_LOOP_REQUEST_UNREADABLE",
    "SELF_RECURSIVE_GROWTH_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_NOT_RECORDED",
    "SELF_RECURSIVE_GROWTH_VERSION_NOT_0_1_0",
    "SELF_RECURSIVE_GROWTH_FAILED_CHECKS_PRESENT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_VERSION_NOT_0_1_0",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SELF_CONTINUATION_BASIS_MISSING",
    "SELF_CONTINUATION_NOT_RECORDED",
    "SELF_CONTINUATION_VERSION_NOT_0_1_0",
    "SELF_CONTINUATION_FAILED_CHECKS_PRESENT",
    "SELF_CONTINUATION_BOUNDARY_BASIS_MISSING",
    "SELF_CONTINUATION_BOUNDARY_NOT_RECORDED",
    "SELF_CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
    "SELF_CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "CONTINUATION_BASIS_MISSING",
    "CONTINUATION_NOT_RECORDED",
    "CONTINUATION_VERSION_NOT_0_1_0",
    "CONTINUATION_FAILED_CHECKS_PRESENT",
    "CONTINUATION_BOUNDARY_BASIS_MISSING",
    "CONTINUATION_BOUNDARY_NOT_RECORDED",
    "CONTINUATION_BOUNDARY_VERSION_NOT_0_1_0",
    "CONTINUATION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "ONGOING_RUNTIME_BASIS_MISSING",
    "ONGOING_RUNTIME_NOT_RECORDED",
    "ONGOING_RUNTIME_VERSION_NOT_0_1_0",
    "ONGOING_RUNTIME_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
    "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_BOUNDARY_V2_BASIS_MISSING",
    "RUNTIME_HOSTING_BOUNDARY_V2_NOT_RECORDED",
    "RUNTIME_HOSTING_BOUNDARY_V2_VERSION_NOT_0_2_0",
    "RUNTIME_HOSTING_BOUNDARY_V2_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
    "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
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
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_BASIS_MISSING",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_NOT_RECORDED",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_VERSION_NOT_0_1_0",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    "POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_AS_CONTINUATION",
    "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    "RUNTIME_LOOP_SPEC_ONLY_POSTURE_UNDECLARED",
    "ONE_BOUNDED_RUNTIME_LOOP_POSTURE_UNDECLARED",
    "RUNTIME_LOOP_BOUNDARY_BASIS_PRESERVED_POSTURE_UNDECLARED",
    "RUNTIME_DAEMON_BASIS_PRESERVED_POSTURE_UNDECLARED",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_PRESERVED_POSTURE_UNDECLARED",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_DECLARED_POSTURE_UNDECLARED",
    "RUNTIME_LOOP_NOT_PUBLIC_API_POSTURE_UNDECLARED",
    "RUNTIME_LOOP_NOT_PARTICIPANT_FACING_INTERFACE_POSTURE_UNDECLARED",
    "RUNTIME_LOOP_NOT_DISTRIBUTED_NETWORK_BEHAVIOR_POSTURE_UNDECLARED",
    "PUBLIC_API_NOT_CREATED_POSTURE_UNDECLARED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED_POSTURE_UNDECLARED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED_POSTURE_UNDECLARED",
    "SOURCE_AUTHORITY_CURRENTNESS_DEPLOYMENT_PUBLIC_RELEASE_OPERATION_PERMISSION_FOLLOW_ON_POSTURE_UNDECLARED",
    "HIDDEN_REPO_STATE_NOT_EXCLUDED",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
)

_BLOCK_CODE_SET = set(BLOCK_CODES)
_SCOPE_SET = set(SUPPORTED_SCOPE_VALUES)
_SENSITIVE_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_loop_body",
    "raw_bounded_runtime_loop_envelope_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "runtime_loop_body",
    "bounded_runtime_loop_envelope_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}
_HOSTILE_SENTINELS = (
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RUNTIME_LOOP_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)
_OFFICIAL_STRINGS = (
    set(SUPPORTED_SCOPE_VALUES)
    | set(OUTCOME_FAMILY)
    | set(BLOCK_CODES)
    | set(REQUIRED_FALSE_NON_CLAIMS)
    | set(ALLOWED_TRUE_RECORDED_FIELDS)
    | set(SUPPORTED_INTENTS)
    | {RESULT_VERSION, RESOLVER_MODULE}
)

_RESULT_SECTIONS = (
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_loop_boundary_terminal_summary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_terminal_summary_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_self_recursive_growth_basis",
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_continuation_basis",
    "selected_self_continuation_boundary_basis",
    "selected_continuation_basis",
    "selected_continuation_boundary_basis",
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
    "selected_runtime_hosting_basis",
    "selected_runtime_hosting_boundary_v2_basis",
    "selected_runtime_hosting_boundary_v1_failure_lineage_basis",
    "selected_successor_runtime_step_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

_POSTURE_SECTIONS = (
    "runtime_loop_spec_only_posture",
    "one_bounded_runtime_loop_posture",
    "runtime_loop_boundary_basis_preserved_posture",
    "runtime_daemon_basis_preserved_posture",
    "bounded_runtime_daemon_envelope_preserved_posture",
    "bounded_runtime_loop_envelope_declared_posture",
    "runtime_loop_not_public_api_posture",
    "runtime_loop_not_participant_facing_interface_posture",
    "runtime_loop_not_distributed_network_behavior_posture",
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
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_runtime_loop_authority_posture",
    "artifact_existence_not_runtime_loop_authority_posture",
    "latest_file_posture_not_runtime_loop_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str) -> bool:
    return key in _SENSITIVE_KEYS or key.endswith("_body")


def _contains_hostile_sentinel(value: Any) -> bool:
    if isinstance(value, str):
        return any(sentinel in value for sentinel in _HOSTILE_SENTINELS)
    if isinstance(value, Mapping):
        return any(
            _contains_hostile_sentinel(item_key)
            or _contains_hostile_sentinel(item_value)
            for item_key, item_value in value.items()
        )
    if isinstance(value, (list, tuple, set)):
        return any(_contains_hostile_sentinel(item) for item in value)
    return False


def _sanitize_value(value: Any, parent_key: str | None = None) -> Any:
    if parent_key is not None and _is_sensitive_key(str(parent_key)):
        return "[bounded-redacted-raw-or-hidden-state]"
    if isinstance(value, str):
        if value in _OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in _HOSTILE_SENTINELS):
            return "[bounded-redacted-raw-or-hidden-state]"
        return value
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            sanitized[key_text] = _sanitize_value(item, key_text)
        return sanitized
    if isinstance(value, tuple):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, list):
        return [_sanitize_value(item) for item in value]
    if isinstance(value, set):
        return sorted(_sanitize_value(item) for item in value)
    return value


def _copy_mapping(value: Mapping[str, Any] | None) -> dict[str, Any]:
    if value is None:
        return {}
    return copy.deepcopy(dict(value))


def _basis_section(request: Mapping[str, Any], section_name: str) -> Any:
    return request.get(section_name)


def _basis_declared(request: Mapping[str, Any], section_name: str) -> bool:
    section = _basis_section(request, section_name)
    if section is None:
        return False
    if isinstance(section, Mapping) and section.get("declared") is False:
        return False
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


def _is_zero(value: Any) -> bool:
    return _as_int(value) == 0


def _mapping_value(mapping: Mapping[str, Any], names: tuple[str, ...]) -> Any:
    for name in names:
        if name in mapping:
            return mapping[name]
    for name in names:
        summary = mapping.get("summary")
        if isinstance(summary, Mapping) and name in summary:
            return summary[name]
    for name in names:
        statement = mapping.get("statement")
        if isinstance(statement, Mapping) and name in statement:
            return statement[name]
        runtime_statement = mapping.get("runtime_loop_statement")
        if isinstance(runtime_statement, Mapping) and name in runtime_statement:
            return runtime_statement[name]
        boundary_statement = mapping.get("runtime_loop_boundary_statement")
        if isinstance(boundary_statement, Mapping) and name in boundary_statement:
            return boundary_statement[name]
        daemon_statement = mapping.get("runtime_daemon_statement")
        if isinstance(daemon_statement, Mapping) and name in daemon_statement:
            return daemon_statement[name]
    return None


def _basis_value(
    request: Mapping[str, Any],
    section_name: str,
    shortcut_name: str | None,
    names: tuple[str, ...],
    default: Any = None,
) -> Any:
    if shortcut_name is not None and shortcut_name in request:
        return request[shortcut_name]
    section = request.get(section_name)
    if isinstance(section, Mapping):
        value = _mapping_value(section, names)
        if value is not None:
            return value
    return default


def _truthy(value: Any) -> bool:
    return value is True


def _falsey(value: Any) -> bool:
    return value is False


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> None:
    if code not in _BLOCK_CODE_SET:
        raise PostRuntimeDaemonRuntimeLoopError(f"Unknown block code: {code}")
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize_value(expected_posture),
        "actual_posture": _sanitize_value(actual_posture),
    }
    if passed:
        check["block_code"] = None
        check["failure_code"] = None
    else:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _first_failed_check(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _selected_scope(request: Mapping[str, Any]) -> list[Any]:
    scope = request.get("runtime_loop_scope", list(SUPPORTED_SCOPE_VALUES))
    if isinstance(scope, Mapping):
        values = scope.get("values", [])
    else:
        values = scope
    if isinstance(values, str):
        return [values]
    if isinstance(values, (list, tuple, set)):
        return list(values)
    return [values]


def _posture(
    declared: bool,
    posture: str,
    meaning: str,
    *,
    value: bool | None = None,
) -> dict[str, Any]:
    return {
        "declared": bool(declared),
        "posture": posture,
        "meaning": meaning,
        "value": bool(declared if value is None else value),
    }


def _basis_reference(
    name: str,
    outcome: str,
    *,
    path: str,
    result_version: str = RESULT_VERSION,
    failed_check_count: int = 0,
    declared: bool = True,
    **extra: Any,
) -> dict[str, Any]:
    basis = {
        "declared": declared,
        "basis_name": name,
        "path": path,
        "outcome": outcome,
        "result_outcome": outcome,
        "result_version": result_version,
        "failed_check_count": failed_check_count,
        "reference_shape": "selected-basis-reference",
    }
    basis.update(extra)
    return basis


def _default_bounded_runtime_loop_envelope(declared: bool = True) -> dict[str, Any]:
    return {
        "declared": bool(declared),
        "envelope_name": "one_bounded_post_runtime_daemon_runtime_loop_envelope",
        "scope": "one bounded repeating-autonomous-runtime posture from selected runtime-loop-boundary and runtime-daemon basis",
        "may_repeat": [
            "bounded runtime-loop review posture",
            "selected bounded runtime-daemon envelope only where this resolver records one runtime-loop posture",
        ],
        "does_not_authorize": [
            "arbitrary runtime activity",
            "public API",
            "participant-facing interface",
            "distributed network behavior",
            "source transfer",
            "source receipt",
            "reception authorization",
            "source",
            "authority",
            "currentness",
            "deployment",
            "public release",
            "operation permission",
            "broader reusable permission",
            "follow-on work",
        ],
        "fresh_admission_required_for": [
            "anything outside the bounded runtime-loop envelope",
            "public API",
            "participant-facing interface",
            "distributed network behavior",
            "source transfer",
            "source receipt",
            "reception authorization",
            "source",
            "authority",
            "currentness",
            "deployment",
            "public release",
            "operation permission",
            "broader reusable permission",
            "follow-on work",
        ],
        "arbitrary_runtime_activity_authorized": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _runtime_loop_envelope_from_request(
    request: Mapping[str, Any],
    *,
    declared: bool,
) -> dict[str, Any]:
    candidate = request.get("requested_bounded_runtime_loop_envelope")
    if isinstance(candidate, Mapping):
        envelope = _sanitize_value(candidate)
        envelope["declared"] = bool(declared)
        envelope.setdefault("fresh_admission_required_for", ["anything outside the bounded runtime-loop envelope"])
        envelope.setdefault("arbitrary_runtime_activity_authorized", False)
        envelope.setdefault("public_api_created", False)
        envelope.setdefault("participant_facing_interface_created", False)
        envelope.setdefault("distributed_network_behavior_created", False)
        envelope.setdefault("follow_on_work_authorized", False)
        return envelope
    return _default_bounded_runtime_loop_envelope(declared)


def _add_basis_recorded_checks(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    basis_label: str,
    section_name: str,
    outcome_shortcut: str,
    version_shortcut: str,
    failed_shortcut: str,
    expected_outcome: str,
    expected_version: str,
    missing_code: str,
    outcome_code: str,
    version_code: str,
    failed_code: str,
) -> None:
    _add_check(
        checks,
        f"{basis_label} basis declared",
        _basis_declared(request, section_name),
        "declared selected reference-shaped basis",
        _basis_section(request, section_name),
        missing_code,
    )
    outcome = _basis_value(
        request,
        section_name,
        outcome_shortcut,
        ("outcome", "result_outcome", "selected_outcome"),
    )
    _add_check(
        checks,
        f"{basis_label} outcome recorded",
        outcome == expected_outcome,
        expected_outcome,
        outcome,
        outcome_code,
    )
    version = _basis_value(
        request,
        section_name,
        version_shortcut,
        ("result_version", "version", "selected_version"),
    )
    _add_check(
        checks,
        f"{basis_label} version {expected_version}",
        version == expected_version,
        expected_version,
        version,
        version_code,
    )
    failed_count = _basis_value(
        request,
        section_name,
        failed_shortcut,
        ("failed_check_count", "failed_checks", "failed_count"),
    )
    _add_check(
        checks,
        f"{basis_label} failed checks zero",
        _is_zero(failed_count),
        0,
        failed_count,
        failed_code,
    )


def _add_posture_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    section_name: str,
    check_name: str,
    code: str,
) -> None:
    section = request.get(section_name)
    declared = False
    if isinstance(section, Mapping):
        declared = section.get("declared") is True or section.get("value") is True
    elif isinstance(section, bool):
        declared = section
    _add_check(
        checks,
        check_name,
        declared,
        "declared true bounded posture",
        section,
        code,
    )


def _add_false_absence_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    field_name: str,
    code: str,
    check_name: str | None = None,
) -> None:
    actual = request.get(field_name, False)
    _add_check(
        checks,
        check_name or f"{field_name} false",
        actual is False,
        False,
        actual,
        code,
    )


def _add_selected_false_absence_check(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    *,
    section_name: str,
    shortcut_name: str,
    names: tuple[str, ...],
    code: str,
    check_name: str,
) -> None:
    actual = _basis_value(request, section_name, shortcut_name, names, False)
    _add_check(checks, check_name, actual is False, False, actual, code)


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("runtime_loop_question")
    _add_check(
        checks,
        "runtime-loop question declared",
        isinstance(question, str) and question.strip() == RUNTIME_LOOP_QUESTION,
        RUNTIME_LOOP_QUESTION,
        question,
        "RUNTIME_LOOP_QUESTION_UNDECLARED",
    )

    intent = request.get("runtime_loop_intent")
    _add_check(
        checks,
        "runtime-loop intent supported",
        intent in SUPPORTED_INTENTS and intent == INTENT_RECORD,
        INTENT_RECORD,
        intent,
        "RUNTIME_LOOP_INTENT_UNSUPPORTED",
    )

    selected_scope = _selected_scope(request)
    unsupported_scope = [value for value in selected_scope if value not in _SCOPE_SET]
    _add_check(
        checks,
        "runtime-loop scope supported",
        not unsupported_scope,
        list(SUPPORTED_SCOPE_VALUES),
        selected_scope,
        "UNSUPPORTED_RUNTIME_LOOP_SCOPE",
    )

    _add_basis_recorded_checks(
        request,
        checks,
        basis_label="runtime-loop-boundary",
        section_name="selected_runtime_loop_boundary_basis",
        outcome_shortcut="selected_runtime_loop_boundary_result_outcome",
        version_shortcut="selected_runtime_loop_boundary_result_version",
        failed_shortcut="selected_runtime_loop_boundary_failed_check_count",
        expected_outcome="POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_RECORDED",
        expected_version=RESULT_VERSION,
        missing_code="RUNTIME_LOOP_BOUNDARY_BASIS_MISSING",
        outcome_code="RUNTIME_LOOP_BOUNDARY_NOT_RECORDED",
        version_code="RUNTIME_LOOP_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_LOOP_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    _add_check(
        checks,
        "runtime-loop-boundary declared future runtime-loop review",
        _basis_value(
            request,
            "selected_runtime_loop_boundary_basis",
            "selected_runtime_loop_boundary_declared_future_review",
            (
                "one_future_runtime_loop_review_declared",
                "runtime_loop_future_review_declared",
            ),
            False,
        )
        is True,
        True,
        _basis_value(
            request,
            "selected_runtime_loop_boundary_basis",
            "selected_runtime_loop_boundary_declared_future_review",
            (
                "one_future_runtime_loop_review_declared",
                "runtime_loop_future_review_declared",
            ),
            False,
        ),
        "RUNTIME_LOOP_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_LOOP_REVIEW",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_already_created_runtime_loop",
        names=("runtime_loop_created", "already_created_runtime_loop"),
        code="RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
        check_name="runtime-loop-boundary did not create runtime loop",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_already_created_public_api",
        names=("public_api_created", "already_created_public_api"),
        code="RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
        check_name="runtime-loop-boundary did not create public API",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_already_created_participant_facing_interface",
        names=("participant_facing_interface_created",),
        code="RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        check_name="runtime-loop-boundary did not create participant-facing interface",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_already_created_distributed_network_behavior",
        names=("distributed_network_behavior_created",),
        code="RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        check_name="runtime-loop-boundary did not create distributed network behavior",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_treated_as_runtime_loop",
        names=("runtime_loop_boundary_treated_as_runtime_loop",),
        code="RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
        check_name="runtime-loop-boundary did not treat itself as runtime loop",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_treated_as_public_api",
        names=("runtime_loop_boundary_treated_as_public_api",),
        code="RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_API",
        check_name="runtime-loop-boundary did not treat itself as public API",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_treated_as_distributed_network_behavior",
        names=("runtime_loop_boundary_treated_as_distributed_network_behavior",),
        code="RUNTIME_LOOP_BOUNDARY_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        check_name="runtime-loop-boundary did not treat itself as distributed behavior",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_loop_boundary_basis",
        shortcut_name="selected_runtime_loop_boundary_authorized_future_work",
        names=("follow_on_work_authorized", "authorized_future_work"),
        code="RUNTIME_LOOP_BOUNDARY_AUTHORIZED_FUTURE_WORK",
        check_name="runtime-loop-boundary did not authorize future work",
    )
    _add_check(
        checks,
        "runtime-loop-boundary canonicalized result-level non-claims",
        _basis_value(
            request,
            "selected_runtime_loop_boundary_basis",
            "selected_runtime_loop_boundary_non_claims_canonicalized",
            ("result_level_non_claims_canonical_false", "non_claims_canonicalized"),
            False,
        )
        is True,
        True,
        _basis_value(
            request,
            "selected_runtime_loop_boundary_basis",
            "selected_runtime_loop_boundary_non_claims_canonicalized",
            ("result_level_non_claims_canonical_false", "non_claims_canonicalized"),
            False,
        ),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    terminal_summary = request.get("selected_runtime_loop_boundary_terminal_summary_basis")
    _add_check(
        checks,
        "runtime-loop-boundary terminal summary declared",
        _basis_declared(request, "selected_runtime_loop_boundary_terminal_summary_basis"),
        "declared terminal summary basis",
        terminal_summary,
        "RUNTIME_LOOP_BOUNDARY_BASIS_MISSING",
    )
    terminal_mapping = terminal_summary if isinstance(terminal_summary, Mapping) else {}
    _add_check(
        checks,
        "runtime-loop-boundary terminal summary states runtime loop not created",
        terminal_mapping.get("runtime_loop_not_created") is True,
        True,
        terminal_mapping.get("runtime_loop_not_created"),
        "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    )
    _add_check(
        checks,
        "runtime-loop-boundary terminal summary states no runtime loop selected",
        terminal_mapping.get("no_runtime_loop_selected") is True,
        True,
        terminal_mapping.get("no_runtime_loop_selected"),
        "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    )
    _add_check(
        checks,
        "runtime-loop-boundary terminal summary requires separate future review",
        terminal_mapping.get("separate_future_review_required") is True
        or terminal_mapping.get("future_work_requires_step_back_review") is True,
        True,
        {
            "separate_future_review_required": terminal_mapping.get(
                "separate_future_review_required"
            ),
            "future_work_requires_step_back_review": terminal_mapping.get(
                "future_work_requires_step_back_review"
            ),
        },
        "RUNTIME_LOOP_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    )

    _add_basis_recorded_checks(
        request,
        checks,
        basis_label="runtime-daemon",
        section_name="selected_runtime_daemon_basis",
        outcome_shortcut="selected_runtime_daemon_result_outcome",
        version_shortcut="selected_runtime_daemon_result_version",
        failed_shortcut="selected_runtime_daemon_failed_check_count",
        expected_outcome="POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
        expected_version=RESULT_VERSION,
        missing_code="RUNTIME_DAEMON_BASIS_MISSING",
        outcome_code="RUNTIME_DAEMON_NOT_RECORDED",
        version_code="RUNTIME_DAEMON_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_DAEMON_FAILED_CHECKS_PRESENT",
    )
    _add_check(
        checks,
        "runtime-daemon recorded bounded runtime-daemon posture",
        _basis_value(
            request,
            "selected_runtime_daemon_basis",
            "selected_runtime_daemon_bounded_posture_recorded",
            ("bounded_runtime_daemon_posture_recorded", "runtime_daemon_recorded"),
            False,
        )
        is True,
        True,
        _basis_value(
            request,
            "selected_runtime_daemon_basis",
            "selected_runtime_daemon_bounded_posture_recorded",
            ("bounded_runtime_daemon_posture_recorded", "runtime_daemon_recorded"),
            False,
        ),
        "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_POSTURE",
    )
    _add_check(
        checks,
        "runtime-daemon recorded bounded runtime-daemon envelope",
        _basis_value(
            request,
            "selected_runtime_daemon_basis",
            "selected_runtime_daemon_bounded_runtime_daemon_envelope_recorded",
            ("bounded_runtime_daemon_envelope_recorded",),
            False,
        )
        is True,
        True,
        _basis_value(
            request,
            "selected_runtime_daemon_basis",
            "selected_runtime_daemon_bounded_runtime_daemon_envelope_recorded",
            ("bounded_runtime_daemon_envelope_recorded",),
            False,
        ),
        "RUNTIME_DAEMON_DID_NOT_RECORD_BOUNDED_RUNTIME_DAEMON_ENVELOPE",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_daemon_basis",
        shortcut_name="selected_runtime_daemon_already_created_public_api",
        names=("public_api_created",),
        code="RUNTIME_DAEMON_ALREADY_CREATED_PUBLIC_API",
        check_name="runtime-daemon did not create public API",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_daemon_basis",
        shortcut_name="selected_runtime_daemon_already_created_participant_facing_interface",
        names=("participant_facing_interface_created",),
        code="RUNTIME_DAEMON_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
        check_name="runtime-daemon did not create participant-facing interface",
    )
    _add_selected_false_absence_check(
        request,
        checks,
        section_name="selected_runtime_daemon_basis",
        shortcut_name="selected_runtime_daemon_already_created_distributed_network_behavior",
        names=("distributed_network_behavior_created",),
        code="RUNTIME_DAEMON_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
        check_name="runtime-daemon did not create distributed network behavior",
    )
    _add_false_absence_check(
        request,
        checks,
        field_name="selected_bounded_runtime_daemon_envelope_treated_as_runtime_loop_before_review",
        code="BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP_BEFORE_REVIEW",
        check_name="bounded runtime-daemon envelope not treated as runtime loop before review",
    )
    _add_false_absence_check(
        request,
        checks,
        field_name="selected_bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity_before_review",
        code="BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
        check_name="bounded runtime-daemon envelope did not authorize arbitrary runtime activity before review",
    )

    _add_basis_recorded_checks(
        request,
        checks,
        basis_label="runtime-daemon-boundary",
        section_name="selected_runtime_daemon_boundary_basis",
        outcome_shortcut="selected_runtime_daemon_boundary_result_outcome",
        version_shortcut="selected_runtime_daemon_boundary_result_version",
        failed_shortcut="selected_runtime_daemon_boundary_failed_check_count",
        expected_outcome="POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_RECORDED",
        expected_version=RESULT_VERSION,
        missing_code="RUNTIME_DAEMON_BOUNDARY_BASIS_MISSING",
        outcome_code="RUNTIME_DAEMON_BOUNDARY_NOT_RECORDED",
        version_code="RUNTIME_DAEMON_BOUNDARY_VERSION_NOT_0_1_0",
        failed_code="RUNTIME_DAEMON_BOUNDARY_FAILED_CHECKS_PRESENT",
    )
    for field_name in (
        "selected_runtime_daemon_boundary_v1_failure_hidden",
        "selected_runtime_daemon_boundary_v1_failure_repaired",
        "selected_runtime_daemon_boundary_v1_failure_claimed_passed",
    ):
        _add_false_absence_check(
            request,
            checks,
            field_name=field_name,
            code="RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
            check_name=f"{field_name} false",
        )

    upstream_basis = (
        (
            "self-recursive-growth",
            "selected_self_recursive_growth_basis",
            "selected_self_recursive_growth_result_outcome",
            "selected_self_recursive_growth_result_version",
            "selected_self_recursive_growth_failed_check_count",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED",
            RESULT_VERSION,
            "SELF_RECURSIVE_GROWTH",
        ),
        (
            "self-recursive-growth-boundary",
            "selected_self_recursive_growth_boundary_basis",
            "selected_self_recursive_growth_boundary_result_outcome",
            "selected_self_recursive_growth_boundary_result_version",
            "selected_self_recursive_growth_boundary_failed_check_count",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
            RESULT_VERSION,
            "SELF_RECURSIVE_GROWTH_BOUNDARY",
        ),
        (
            "self-continuation",
            "selected_self_continuation_basis",
            "selected_self_continuation_result_outcome",
            "selected_self_continuation_result_version",
            "selected_self_continuation_failed_check_count",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
            RESULT_VERSION,
            "SELF_CONTINUATION",
        ),
        (
            "self-continuation-boundary",
            "selected_self_continuation_boundary_basis",
            "selected_self_continuation_boundary_result_outcome",
            "selected_self_continuation_boundary_result_version",
            "selected_self_continuation_boundary_failed_check_count",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
            RESULT_VERSION,
            "SELF_CONTINUATION_BOUNDARY",
        ),
        (
            "continuation",
            "selected_continuation_basis",
            "selected_continuation_result_outcome",
            "selected_continuation_result_version",
            "selected_continuation_failed_check_count",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
            RESULT_VERSION,
            "CONTINUATION",
        ),
        (
            "continuation-boundary",
            "selected_continuation_boundary_basis",
            "selected_continuation_boundary_result_outcome",
            "selected_continuation_boundary_result_version",
            "selected_continuation_boundary_failed_check_count",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
            RESULT_VERSION,
            "CONTINUATION_BOUNDARY",
        ),
        (
            "reusable-runtime-permission",
            "selected_reusable_runtime_permission_basis",
            "selected_reusable_runtime_permission_result_outcome",
            "selected_reusable_runtime_permission_result_version",
            "selected_reusable_runtime_permission_failed_check_count",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
            RESULT_VERSION,
            "REUSABLE_RUNTIME_PERMISSION",
        ),
        (
            "reusable-runtime-permission-boundary",
            "selected_reusable_runtime_permission_boundary_basis",
            "selected_reusable_runtime_permission_boundary_result_outcome",
            "selected_reusable_runtime_permission_boundary_result_version",
            "selected_reusable_runtime_permission_boundary_failed_check_count",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            RESULT_VERSION,
            "REUSABLE_RUNTIME_PERMISSION_BOUNDARY",
        ),
        (
            "ongoing-runtime",
            "selected_ongoing_runtime_basis",
            "selected_ongoing_runtime_result_outcome",
            "selected_ongoing_runtime_result_version",
            "selected_ongoing_runtime_failed_check_count",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
            RESULT_VERSION,
            "ONGOING_RUNTIME",
        ),
        (
            "runtime-hosting",
            "selected_runtime_hosting_basis",
            "selected_runtime_hosting_result_outcome",
            "selected_runtime_hosting_result_version",
            "selected_runtime_hosting_failed_check_count",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
            RESULT_VERSION,
            "RUNTIME_HOSTING",
        ),
        (
            "runtime-hosting-boundary-v2",
            "selected_runtime_hosting_boundary_v2_basis",
            "selected_runtime_hosting_boundary_v2_result_outcome",
            "selected_runtime_hosting_boundary_v2_result_version",
            "selected_runtime_hosting_boundary_v2_failed_check_count",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            "0.2.0",
            "RUNTIME_HOSTING_BOUNDARY_V2",
        ),
        (
            "successor-runtime-step",
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step_result_outcome",
            "selected_successor_runtime_step_result_version",
            "selected_successor_runtime_step_failed_check_count",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            RESULT_VERSION,
            "SUCCESSOR_RUNTIME_STEP",
        ),
        (
            "minimal-runtime",
            "selected_minimal_runtime_basis",
            "selected_minimal_runtime_result_outcome",
            "selected_minimal_runtime_result_version",
            "selected_minimal_runtime_failed_check_count",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            RESULT_VERSION,
            "MINIMAL_RUNTIME",
        ),
        (
            "runtime-boundary",
            "selected_runtime_boundary_basis",
            "selected_runtime_boundary_result_outcome",
            "selected_runtime_boundary_result_version",
            "selected_runtime_boundary_failed_check_count",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            RESULT_VERSION,
            "RUNTIME_BOUNDARY",
        ),
        (
            "runtime-readiness",
            "selected_runtime_readiness_basis",
            "selected_runtime_readiness_result_outcome",
            "selected_runtime_readiness_result_version",
            "selected_runtime_readiness_failed_check_count",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            RESULT_VERSION,
            "RUNTIME_READINESS",
        ),
        (
            "portable-verification-final-completion",
            "selected_portable_verification_final_completion_basis",
            "selected_portable_verification_final_completion_result_outcome",
            "selected_portable_verification_final_completion_result_version",
            "selected_portable_verification_final_completion_failed_check_count",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            RESULT_VERSION,
            "PORTABLE_VERIFICATION_FINAL_COMPLETION",
        ),
    )
    for (
        label,
        section,
        outcome_shortcut,
        version_shortcut,
        failed_shortcut,
        outcome,
        version,
        code_prefix,
    ) in upstream_basis:
        _add_basis_recorded_checks(
            request,
            checks,
            basis_label=label,
            section_name=section,
            outcome_shortcut=outcome_shortcut,
            version_shortcut=version_shortcut,
            failed_shortcut=failed_shortcut,
            expected_outcome=outcome,
            expected_version=version,
            missing_code=f"{code_prefix}_BASIS_MISSING",
            outcome_code=f"{code_prefix}_NOT_RECORDED",
            version_code=f"{code_prefix}_VERSION_NOT_{version.replace('.', '_')}",
            failed_code=f"{code_prefix}_FAILED_CHECKS_PRESENT",
        )

    for field_name in (
        "selected_runtime_hosting_boundary_v1_failure_repaired",
        "selected_runtime_hosting_boundary_v1_failure_hidden",
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed",
    ):
        _add_false_absence_check(
            request,
            checks,
            field_name=field_name,
            code="RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
            check_name=f"{field_name} false",
        )

    _add_check(
        checks,
        "post-portable currentness surface basis declared",
        _basis_declared(request, "selected_post_portable_verification_currentness_basis"),
        "declared post-portable currentness surface basis",
        request.get("selected_post_portable_verification_currentness_basis"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_BASIS_MISSING",
    )
    _add_check(
        checks,
        "post-portable currentness surface states checkability not continuation",
        request.get("selected_post_portable_currentness_surface_states_checkability_not_continuation")
        is True,
        True,
        request.get(
            "selected_post_portable_currentness_surface_states_checkability_not_continuation"
        ),
        "POST_PORTABLE_CURRENTNESS_SURFACE_TREATED_AS_CONTINUATION",
    )
    _add_check(
        checks,
        "post-portable currentness surface does not authorize next work",
        request.get("selected_post_portable_currentness_surface_authorized_next_work")
        is False,
        False,
        request.get("selected_post_portable_currentness_surface_authorized_next_work"),
        "POST_PORTABLE_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    )

    posture_checks = (
        (
            "runtime_loop_spec_only_posture",
            "runtime-loop-spec-only posture declared",
            "RUNTIME_LOOP_SPEC_ONLY_POSTURE_UNDECLARED",
        ),
        (
            "one_bounded_runtime_loop_posture",
            "one-bounded-runtime-loop-posture declared",
            "ONE_BOUNDED_RUNTIME_LOOP_POSTURE_UNDECLARED",
        ),
        (
            "runtime_loop_boundary_basis_preserved_posture",
            "runtime-loop-boundary-basis-preserved posture declared",
            "RUNTIME_LOOP_BOUNDARY_BASIS_PRESERVED_POSTURE_UNDECLARED",
        ),
        (
            "runtime_daemon_basis_preserved_posture",
            "runtime-daemon-basis-preserved posture declared",
            "RUNTIME_DAEMON_BASIS_PRESERVED_POSTURE_UNDECLARED",
        ),
        (
            "bounded_runtime_daemon_envelope_preserved_posture",
            "bounded-runtime-daemon-envelope-preserved posture declared",
            "BOUNDED_RUNTIME_DAEMON_ENVELOPE_PRESERVED_POSTURE_UNDECLARED",
        ),
        (
            "bounded_runtime_loop_envelope_declared_posture",
            "bounded-runtime-loop-envelope-declared posture declared",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_DECLARED_POSTURE_UNDECLARED",
        ),
        (
            "runtime_loop_not_public_api_posture",
            "runtime-loop-not-public-api posture declared",
            "RUNTIME_LOOP_NOT_PUBLIC_API_POSTURE_UNDECLARED",
        ),
        (
            "runtime_loop_not_participant_facing_interface_posture",
            "runtime-loop-not-participant-facing-interface posture declared",
            "RUNTIME_LOOP_NOT_PARTICIPANT_FACING_INTERFACE_POSTURE_UNDECLARED",
        ),
        (
            "runtime_loop_not_distributed_network_behavior_posture",
            "runtime-loop-not-distributed-network-behavior posture declared",
            "RUNTIME_LOOP_NOT_DISTRIBUTED_NETWORK_BEHAVIOR_POSTURE_UNDECLARED",
        ),
        (
            "public_api_not_created_posture",
            "public-api-not-created posture declared",
            "PUBLIC_API_NOT_CREATED_POSTURE_UNDECLARED",
        ),
        (
            "participant_facing_interface_not_created_posture",
            "participant-facing-interface-not-created posture declared",
            "PARTICIPANT_FACING_INTERFACE_NOT_CREATED_POSTURE_UNDECLARED",
        ),
        (
            "distributed_network_behavior_not_created_posture",
            "distributed-network-behavior-not-created posture declared",
            "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED_POSTURE_UNDECLARED",
        ),
    )
    for section_name, check_name, code in posture_checks:
        _add_posture_check(
            request,
            checks,
            section_name=section_name,
            check_name=check_name,
            code=code,
        )

    for section_name in (
        "source_transfer_not_created_posture",
        "source_receipt_not_created_posture",
        "reception_authorization_not_created_posture",
        "source_not_created_posture",
        "authority_not_created_posture",
        "currentness_not_created_posture",
        "deployment_not_created_posture",
        "public_release_not_created_posture",
        "operation_permission_not_created_posture",
        "broader_reusable_permission_not_created_posture",
        "follow_on_work_not_authorized_posture",
    ):
        _add_posture_check(
            request,
            checks,
            section_name=section_name,
            check_name=f"{section_name} declared",
            code="SOURCE_AUTHORITY_CURRENTNESS_DEPLOYMENT_PUBLIC_RELEASE_OPERATION_PERMISSION_FOLLOW_ON_POSTURE_UNDECLARED",
        )

    _add_posture_check(
        request,
        checks,
        section_name="hidden_repo_state_excluded_posture",
        check_name="hidden repo state excluded",
        code="HIDDEN_REPO_STATE_NOT_EXCLUDED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="repo_local_availability_not_runtime_loop_authority_posture",
        check_name="repo-local availability not runtime-loop authority",
        code="REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    )
    _add_posture_check(
        request,
        checks,
        section_name="artifact_existence_not_runtime_loop_authority_posture",
        check_name="artifact existence not runtime-loop authority",
        code="ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    )
    _add_posture_check(
        request,
        checks,
        section_name="latest_file_posture_not_runtime_loop_authority_posture",
        check_name="latest file posture not runtime-loop authority",
        code="LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    )
    _add_posture_check(
        request,
        checks,
        section_name="selected_basis_reference_shape_posture",
        check_name="selected basis reference-shaped",
        code="SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _add_check(
        checks,
        "reference-shaped input posture preserved",
        request.get("reference_shaped_input_posture", True) is True,
        True,
        request.get("reference_shaped_input_posture", True),
        "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="raw_full_prior_artifact_body_not_returned_posture",
        check_name="raw full prior artifact body not returned",
        code="RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="official_enum_scope_strings_not_redacted_posture",
        check_name="official enum scope strings not redacted",
        code="OFFICIAL_ENUM_SCOPE_STRINGS_REDACTED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="hostile_raw_body_content_contained_posture",
        check_name="hostile raw body content contained",
        code="HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="predecessor_failure_evidence_preserved_posture",
        check_name="predecessor failure evidence preserved",
        code="PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _add_posture_check(
        request,
        checks,
        section_name="result_level_non_claims_canonical_false_posture",
        check_name="result-level required false non-claims canonical false",
        code="NON_CLAIM_MISSING_OR_FLIPPED",
    )

    for field_name, code in (
        ("runtime_loop_recorded_before_review", "RUNTIME_LOOP_RECORDED_BEFORE_REVIEW"),
        (
            "runtime_loop_boundary_treated_as_runtime_loop_without_review",
            "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP_WITHOUT_REVIEW",
        ),
        (
            "runtime_daemon_treated_as_runtime_loop_without_review",
            "RUNTIME_DAEMON_TREATED_AS_RUNTIME_LOOP_WITHOUT_REVIEW",
        ),
        ("runtime_loop_treated_as_public_api", "RUNTIME_LOOP_TREATED_AS_PUBLIC_API"),
        (
            "runtime_loop_treated_as_participant_facing_interface",
            "RUNTIME_LOOP_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "runtime_loop_treated_as_distributed_network_behavior",
            "RUNTIME_LOOP_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        ("runtime_loop_treated_as_source_transfer", "RUNTIME_LOOP_TREATED_AS_SOURCE_TRANSFER"),
        ("runtime_loop_treated_as_source_receipt", "RUNTIME_LOOP_TREATED_AS_SOURCE_RECEIPT"),
        (
            "runtime_loop_treated_as_reception_authorization",
            "RUNTIME_LOOP_TREATED_AS_RECEPTION_AUTHORIZATION",
        ),
        ("runtime_loop_treated_as_source", "RUNTIME_LOOP_TREATED_AS_SOURCE"),
        ("runtime_loop_treated_as_authority", "RUNTIME_LOOP_TREATED_AS_AUTHORITY"),
        ("runtime_loop_treated_as_currentness", "RUNTIME_LOOP_TREATED_AS_CURRENTNESS"),
        ("runtime_loop_treated_as_deployment", "RUNTIME_LOOP_TREATED_AS_DEPLOYMENT"),
        ("runtime_loop_treated_as_public_release", "RUNTIME_LOOP_TREATED_AS_PUBLIC_RELEASE"),
        (
            "runtime_loop_treated_as_operation_permission",
            "RUNTIME_LOOP_TREATED_AS_OPERATION_PERMISSION",
        ),
        (
            "runtime_loop_treated_as_broader_reusable_permission",
            "RUNTIME_LOOP_TREATED_AS_BROADER_REUSABLE_PERMISSION",
        ),
        ("runtime_loop_treated_as_follow_on_work", "RUNTIME_LOOP_TREATED_AS_FOLLOW_ON_WORK"),
        ("public_api_created", "PUBLIC_API_CREATED"),
        (
            "participant_facing_interface_created",
            "PARTICIPANT_FACING_INTERFACE_CREATED",
        ),
        ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
        ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        ("reception_authorization_created", "RECEPTION_AUTHORIZATION_CREATED"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("adoption_created", "ADOPTION_CREATED"),
        ("receiving_context_governance_created", "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
        ("publication_flow_created", "PUBLICATION_FLOW_CREATED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        (
            "artifact_existence_treated_as_runtime_loop_authority",
            "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
        ),
        ("artifact_path_treated_as_currentness", "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
        (
            "latest_file_posture_treated_as_runtime_loop_authority",
            "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
        ),
        (
            "repo_local_availability_treated_as_runtime_loop_authority",
            "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
        ),
        (
            "hidden_repo_state_used_as_runtime_loop_content",
            "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_CONTENT",
        ),
        (
            "hidden_repo_state_used_as_runtime_loop_authority",
            "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_AUTHORITY",
        ),
        ("raw_full_prior_artifact_body_returned", "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
        (
            "bounded_runtime_daemon_envelope_treated_as_runtime_loop_without_review",
            "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP_BEFORE_REVIEW",
        ),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("predecessor_failure_repaired", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        ("predecessor_failure_hidden", "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
        (
            "predecessor_failure_claimed_passed",
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        ),
    ):
        _add_false_absence_check(request, checks, field_name=field_name, code=code)

    envelope = request.get("requested_bounded_runtime_loop_envelope")
    envelope_mapping = envelope if isinstance(envelope, Mapping) else {}
    for field_name, code in (
        (
            "arbitrary_runtime_activity_authorized",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
        ),
        ("public_api_created", "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_PUBLIC_API"),
        (
            "participant_facing_interface_created",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE",
        ),
        (
            "distributed_network_behavior_created",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR",
        ),
        (
            "follow_on_work_authorized",
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_AUTHORIZED_FOLLOW_ON_WORK",
        ),
    ):
        actual = envelope_mapping.get(field_name, False)
        _add_check(
            checks,
            f"bounded runtime-loop envelope {field_name} false",
            actual is False,
            False,
            actual,
            code,
        )

    declared_non_claims = request.get("declared_non_claims")
    non_claims_valid = isinstance(declared_non_claims, Mapping)
    actual_non_claims: dict[str, Any] = {}
    if isinstance(declared_non_claims, Mapping):
        actual_non_claims = dict(declared_non_claims)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            if key not in declared_non_claims or declared_non_claims.get(key) is not False:
                non_claims_valid = False
                break
    _add_check(
        checks,
        "required non-claims false",
        non_claims_valid,
        _canonical_non_claims(),
        actual_non_claims if isinstance(declared_non_claims, Mapping) else declared_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    _add_check(
        checks,
        "hostile raw body content contained",
        not _contains_hostile_sentinel(_sanitize_value(request)),
        "no hostile raw/hidden sentinel returned",
        _sanitize_value(request),
        "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED",
    )
    return checks


def _statement(outcome: str, checks: list[dict[str, Any]]) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    failed_codes = {
        check.get("failure_code") or check.get("block_code")
        for check in checks
        if check.get("passed") is not True
    }
    no_reference_shape_failure = "SELECTED_BASIS_NOT_REFERENCE_SHAPED" not in failed_codes
    no_raw_failure = "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED" not in failed_codes
    no_hostile_failure = "HOSTILE_RAW_BODY_CONTENT_NOT_CONTAINED" not in failed_codes
    no_predecessor_failure = (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED" not in failed_codes
        and "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED"
        not in failed_codes
        and "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"
        not in failed_codes
    )
    return {
        "runtime_loop_recorded": recorded,
        "bounded_runtime_loop_posture_recorded": recorded,
        "runtime_loop_boundary_basis_preserved": recorded,
        "runtime_daemon_basis_preserved": recorded,
        "bounded_runtime_daemon_envelope_preserved": recorded,
        "bounded_runtime_loop_envelope_declared": recorded,
        "runtime_loop_not_public_api": True,
        "runtime_loop_not_participant_facing_interface": True,
        "runtime_loop_not_distributed_network_behavior": True,
        "public_api_not_created": True,
        "participant_facing_interface_not_created": True,
        "distributed_network_behavior_not_created": True,
        "source_transfer_not_created": True,
        "source_receipt_not_created": True,
        "reception_authorization_not_created": True,
        "source_not_created": True,
        "authority_not_created": True,
        "currentness_not_created": True,
        "deployment_not_created": True,
        "public_release_not_created": True,
        "operation_permission_not_created": True,
        "broader_reusable_permission_not_created": True,
        "follow_on_work_not_authorized": True,
        "hidden_repo_state_excluded": True,
        "hidden_repo_state_not_used_as_runtime_loop_authority": True,
        "repo_local_availability_not_runtime_loop_authority": True,
        "artifact_existence_not_runtime_loop_authority": True,
        "latest_file_posture_not_runtime_loop_authority": True,
        "selected_basis_reference_shape_preserved": no_reference_shape_failure,
        "raw_full_prior_artifact_body_not_returned": no_raw_failure,
        "official_enum_scope_strings_not_redacted": True,
        "hostile_raw_body_content_contained": no_hostile_failure,
        "predecessor_failure_evidence_preserved": no_predecessor_failure,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "result_level_non_claims_canonical_false": True,
    }


def _runtime_loop_non_meaning() -> dict[str, bool]:
    return {
        "runtime_loop_is_public_api": False,
        "runtime_loop_is_participant_facing_interface": False,
        "runtime_loop_is_distributed_network_behavior": False,
        "runtime_loop_is_source_transfer": False,
        "runtime_loop_is_source_receipt": False,
        "runtime_loop_is_reception_authorization": False,
        "runtime_loop_is_source": False,
        "runtime_loop_is_authority": False,
        "runtime_loop_is_currentness": False,
        "runtime_loop_is_deployment": False,
        "runtime_loop_is_public_release": False,
        "runtime_loop_is_operation_permission": False,
        "runtime_loop_is_broader_reusable_permission": False,
        "runtime_loop_is_follow_on_work": False,
        "runtime_loop_boundary_is_runtime_loop_without_review": False,
        "runtime_daemon_is_runtime_loop_without_review": False,
        "bounded_runtime_daemon_envelope_is_runtime_loop_without_review": False,
        "artifact_existence_is_runtime_loop_authority": False,
        "repo_local_availability_is_runtime_loop_authority": False,
        "latest_file_posture_is_runtime_loop_authority": False,
        "hidden_repo_state_is_runtime_loop_authority": False,
    }


def _block_from_failure(failure: dict[str, Any] | None) -> dict[str, Any] | None:
    if failure is None:
        return None
    code = failure.get("block_code") or failure.get("failure_code")
    return {
        "block_code": code,
        "reason": failure.get("check_name"),
        "expected_posture": failure.get("expected_posture"),
        "actual_posture": failure.get("actual_posture"),
    }


def _result_from_request(
    request: Mapping[str, Any],
    *,
    outcome: str,
    checks: list[dict[str, Any]],
    block: dict[str, Any] | None,
) -> dict[str, Any]:
    request_id = str(request.get("runtime_loop_request_id") or "undeclared_runtime_loop_request")
    statement = _statement(outcome, checks)
    recorded = outcome == OUTCOME_RECORDED
    result: dict[str, Any] = {
        "post_runtime_daemon_runtime_loop_metadata": {
            "post_runtime_daemon_runtime_loop_id": request_id,
            "post_runtime_daemon_runtime_loop_type": "post_runtime_daemon_runtime_loop",
            "post_runtime_daemon_runtime_loop_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_runtime_loop_question": {
            "runtime_loop_request_id": request_id,
            "runtime_loop_question": request.get("runtime_loop_question"),
            "runtime_loop_intent": request.get("runtime_loop_intent"),
        },
    }
    for section in _RESULT_SECTIONS:
        result[section] = _sanitize_value(request.get(section, {}))

    default_postures = {
        "runtime_loop_spec_only_posture": ("RUNTIME_LOOP_SPEC_ONLY", "runtime-loop specification posture only"),
        "one_bounded_runtime_loop_posture": (
            "ONE_BOUNDED_RUNTIME_LOOP_POSTURE_RECORDED",
            "one bounded runtime-loop posture only",
        ),
        "runtime_loop_boundary_basis_preserved_posture": (
            "RUNTIME_LOOP_BOUNDARY_BASIS_PRESERVED",
            "runtime-loop-boundary remains preserved basis",
        ),
        "runtime_daemon_basis_preserved_posture": (
            "RUNTIME_DAEMON_BASIS_PRESERVED",
            "runtime daemon remains one bounded runtime-daemon posture",
        ),
        "bounded_runtime_daemon_envelope_preserved_posture": (
            "BOUNDED_RUNTIME_DAEMON_ENVELOPE_PRESERVED",
            "bounded runtime-daemon envelope remains preserved",
        ),
        "bounded_runtime_loop_envelope_declared_posture": (
            "BOUNDED_RUNTIME_LOOP_ENVELOPE_DECLARED",
            "one bounded runtime-loop envelope declared",
        ),
    }
    for section in _POSTURE_SECTIONS:
        if section in request:
            result[section] = _sanitize_value(request.get(section))
        else:
            posture, meaning = default_postures.get(
                section,
                (section.upper(), "bounded runtime-loop non-creation posture"),
            )
            result[section] = _posture(recorded, posture, meaning)

    result.update(
        {
            "runtime_loop_scope": list(SUPPORTED_SCOPE_VALUES),
            "runtime_loop_checks": checks,
            "runtime_loop_statement": statement,
            "runtime_loop_non_meaning": _runtime_loop_non_meaning(),
            "bounded_runtime_loop_envelope": _runtime_loop_envelope_from_request(
                request, declared=recorded
            ),
            "additional_basis_required": _sanitize_value(
                request.get("additional_basis_context", [])
            )
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else [],
            "not_recorded_basis": _sanitize_value(request.get("not_recorded_basis", []))
            if outcome == OUTCOME_NOT_RECORDED
            else [],
            "what_remains_open": [
                "public API",
                "participant-facing interface",
                "distributed network behavior",
                "source transfer",
                "source receipt",
                "reception authorization",
                "source",
                "authority",
                "currentness",
                "deployment",
                "public release",
                "operation permission",
                "broader reusable permission",
                "derivative reception",
                "vessel relation",
                "another reception request",
                "adoption",
                "receiving-context governance",
                "publication flow",
                "follow-on work",
            ],
            "non_claims": _canonical_non_claims(),
            "outcome": outcome,
            "block": block,
        }
    )
    result["post_runtime_daemon_runtime_loop_summary"] = (
        build_post_runtime_daemon_runtime_loop_summary(result)
    )
    return result


def _blocked_result(
    code: str,
    reason: str,
    *,
    actual: Any = None,
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _add_check(checks, reason, False, "bounded readable runtime-loop request", actual, code)
    block = _block_from_failure(_first_failed_check(checks))
    return _result_from_request(request or {}, outcome=OUTCOME_BLOCKED, checks=checks, block=block)


def resolve_post_runtime_daemon_runtime_loop(
    declared_runtime_loop_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded post-runtime-daemon runtime-loop request."""

    if declared_runtime_loop_request is None:
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_MALFORMED",
            "declared runtime-loop request missing",
            actual=None,
        )
    if not isinstance(declared_runtime_loop_request, Mapping):
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_MALFORMED",
            "declared runtime-loop request is not a mapping",
            actual=declared_runtime_loop_request,
        )

    request = _copy_mapping(declared_runtime_loop_request)
    requested_outcome = request.get("requested_runtime_loop_outcome")
    checks = _build_checks(request)
    first_failure = _first_failed_check(checks)
    if first_failure is not None:
        outcome = OUTCOME_BLOCKED
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_BLOCKED:
        outcome = OUTCOME_BLOCKED
        _add_check(
            checks,
            "explicit block intent",
            False,
            "recorded runtime-loop posture",
            requested_outcome,
            "RUNTIME_LOOP_INTENT_UNSUPPORTED",
        )
    else:
        outcome = OUTCOME_RECORDED
    block = _block_from_failure(_first_failed_check(checks)) if outcome == OUTCOME_BLOCKED else None
    return _result_from_request(request, outcome=outcome, checks=checks, block=block)


def resolve_post_runtime_daemon_runtime_loop_from_path(
    declared_runtime_loop_request_path: Path | str,
) -> dict:
    """Read a declared runtime-loop request JSON file and resolve it."""

    path = Path(declared_runtime_loop_request_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError:
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_UNREADABLE",
            "declared runtime-loop request path missing",
            actual=str(path),
        )
    except json.JSONDecodeError as exc:
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_UNREADABLE",
            "declared runtime-loop request JSON unreadable",
            actual=str(exc),
        )
    except OSError as exc:
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_UNREADABLE",
            "declared runtime-loop request path unreadable",
            actual=str(exc),
        )
    if not isinstance(loaded, Mapping):
        return _blocked_result(
            "DECLARED_RUNTIME_LOOP_REQUEST_MALFORMED",
            "declared runtime-loop request JSON is not an object",
            actual=loaded,
        )
    return resolve_post_runtime_daemon_runtime_loop(loaded)


def _basis_summary(result: Mapping[str, Any], section_name: str) -> dict[str, Any]:
    section = result.get(section_name)
    if not isinstance(section, Mapping):
        return {"outcome": None, "result_version": None, "failed_check_count": None}
    return {
        "path": section.get("path") or section.get("result_path"),
        "outcome": section.get("outcome") or section.get("result_outcome"),
        "result_version": section.get("result_version") or section.get("version"),
        "failed_check_count": section.get("failed_check_count"),
    }


def build_post_runtime_daemon_runtime_loop_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact summary for a runtime-loop result."""

    checks = result.get("runtime_loop_checks", [])
    checks_list = checks if isinstance(checks, list) else []
    passed = sum(1 for check in checks_list if check.get("passed") is True)
    failed = sum(1 for check in checks_list if check.get("passed") is not True)
    metadata = result.get("post_runtime_daemon_runtime_loop_metadata", {})
    declared = result.get("declared_runtime_loop_question", {})
    statement = result.get("runtime_loop_statement", {})
    block = result.get("block")
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("reason") if isinstance(block, Mapping) else None,
        "request_id": declared.get("runtime_loop_request_id")
        if isinstance(declared, Mapping)
        else None,
        "question": declared.get("runtime_loop_question")
        if isinstance(declared, Mapping)
        else None,
        "intent": declared.get("runtime_loop_intent")
        if isinstance(declared, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "result_version": metadata.get("post_runtime_daemon_runtime_loop_version")
        if isinstance(metadata, Mapping)
        else RESULT_VERSION,
        "resolver_module": metadata.get("resolver_module")
        if isinstance(metadata, Mapping)
        else RESOLVER_MODULE,
        "bounded_runtime_loop_envelope_posture": result.get("bounded_runtime_loop_envelope"),
        "bounded_runtime_loop_envelope": result.get("bounded_runtime_loop_envelope"),
        "no_api_interface_distributed_network_source_authority_currentness_deployment_public_release_follow_on": True,
        "key_non_claims": _canonical_non_claims(),
        "predecessor_failure_evidence_preserved": bool(
            statement.get("predecessor_failure_evidence_preserved")
        )
        if isinstance(statement, Mapping)
        else False,
        "consumed_request_token_remains_closed": bool(
            statement.get("consumed_request_token_remains_closed")
        )
        if isinstance(statement, Mapping)
        else False,
        "authorization_token_reuse_blocked": bool(
            statement.get("authorization_token_reuse_blocked")
        )
        if isinstance(statement, Mapping)
        else False,
    }
    if isinstance(statement, Mapping):
        for field in ALLOWED_TRUE_RECORDED_FIELDS:
            summary[field] = bool(statement.get(field))

    basis_aliases = {
        "selected_runtime_loop_boundary": "selected_runtime_loop_boundary_basis",
        "selected_runtime_daemon": "selected_runtime_daemon_basis",
        "selected_runtime_daemon_boundary": "selected_runtime_daemon_boundary_basis",
        "selected_self_recursive_growth": "selected_self_recursive_growth_basis",
        "selected_self_recursive_growth_boundary": "selected_self_recursive_growth_boundary_basis",
        "selected_self_continuation": "selected_self_continuation_basis",
        "selected_self_continuation_boundary": "selected_self_continuation_boundary_basis",
        "selected_continuation": "selected_continuation_basis",
        "selected_continuation_boundary": "selected_continuation_boundary_basis",
        "selected_reusable_runtime_permission": "selected_reusable_runtime_permission_basis",
        "selected_reusable_runtime_permission_boundary": "selected_reusable_runtime_permission_boundary_basis",
        "selected_ongoing_runtime": "selected_ongoing_runtime_basis",
        "selected_runtime_hosting": "selected_runtime_hosting_basis",
        "selected_runtime_hosting_boundary_v2": "selected_runtime_hosting_boundary_v2_basis",
        "selected_successor_runtime_step": "selected_successor_runtime_step_basis",
        "selected_minimal_runtime": "selected_minimal_runtime_basis",
        "selected_runtime_boundary": "selected_runtime_boundary_basis",
        "selected_runtime_readiness": "selected_runtime_readiness_basis",
        "selected_final_completion": "selected_portable_verification_final_completion_basis",
    }
    for alias, section_name in basis_aliases.items():
        basis = _basis_summary(result, section_name)
        summary[f"{alias}_path"] = basis.get("path")
        summary[f"{alias}_outcome"] = basis.get("outcome")
        summary[f"{alias}_version"] = basis.get("result_version")
        summary[f"{alias}_result_version"] = basis.get("result_version")
        summary[f"{alias}_failed_check_count"] = basis.get("failed_check_count")

    currentness_basis = result.get("selected_post_portable_verification_currentness_basis")
    if isinstance(currentness_basis, Mapping):
        summary["selected_post_portable_currentness_surface_path"] = currentness_basis.get(
            "path"
        )
    else:
        summary["selected_post_portable_currentness_surface_path"] = None
    return summary


def _safe_filename_part(value: Any) -> str:
    text = str(value or "undeclared_runtime_loop_request").strip()
    safe = []
    for char in text:
        if char.isalnum() or char in ("-", "_", "."):
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or "undeclared_runtime_loop_request"


def _dedupe_path(path: Path) -> Path:
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


def write_post_runtime_daemon_runtime_loop_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a runtime-loop result JSON file without overwriting prior output."""

    if not isinstance(result, Mapping):
        raise PostRuntimeDaemonRuntimeLoopError("result must be a mapping")
    if output_path is None:
        metadata = result.get("post_runtime_daemon_runtime_loop_metadata", {})
        request_id = None
        if isinstance(metadata, Mapping):
            request_id = metadata.get("post_runtime_daemon_runtime_loop_id")
        filename = f"{_safe_filename_part(request_id)}__post_runtime_daemon_runtime_loop_result.json"
        path = OUTPUT_ROOT / filename
    else:
        path = Path(output_path)
        if path.suffix != ".json":
            metadata = result.get("post_runtime_daemon_runtime_loop_metadata", {})
            request_id = None
            if isinstance(metadata, Mapping):
                request_id = metadata.get("post_runtime_daemon_runtime_loop_id")
            path = path / f"{_safe_filename_part(request_id)}__post_runtime_daemon_runtime_loop_result.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _dedupe_path(path)
    payload = json.dumps(_sanitize_value(result), ensure_ascii=False, indent=2, sort_keys=True)
    final_path.write_text(payload + "\n", encoding="utf-8")
    return final_path


def build_declared_post_runtime_daemon_runtime_loop_request(
    *,
    runtime_loop_request_id: str = "post_runtime_daemon_runtime_loop_reference_review_001",
    runtime_loop_question: str = RUNTIME_LOOP_QUESTION,
    runtime_loop_intent: str = INTENT_RECORD,
    runtime_loop_scope: list[str] | tuple[str, ...] | None = None,
    requested_bounded_runtime_loop_envelope: Mapping[str, Any] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded declared runtime-loop request that records cleanly."""

    request: dict[str, Any] = {
        "runtime_loop_request_id": runtime_loop_request_id,
        "runtime_loop_question": runtime_loop_question,
        "runtime_loop_intent": runtime_loop_intent,
        "selected_runtime_loop_boundary_basis": _basis_reference(
            "post-runtime-daemon runtime-loop-boundary",
            "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop_boundary/post_runtime_daemon_runtime_loop_boundary_reference_review_001__post_runtime_daemon_runtime_loop_boundary_result.json",
            one_future_runtime_loop_review_declared=True,
            runtime_loop_created=False,
            public_api_created=False,
            participant_facing_interface_created=False,
            distributed_network_behavior_created=False,
            runtime_loop_boundary_treated_as_runtime_loop=False,
            runtime_loop_boundary_treated_as_public_api=False,
            runtime_loop_boundary_treated_as_distributed_network_behavior=False,
            follow_on_work_authorized=False,
            result_level_non_claims_canonical_false=True,
        ),
        "selected_runtime_loop_boundary_terminal_summary_basis": {
            "declared": True,
            "path": "spec/POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "runtime_loop_not_created": True,
            "no_runtime_loop_selected": True,
            "separate_future_review_required": True,
            "future_work_requires_step_back_review": True,
        },
        "selected_runtime_daemon_basis": _basis_reference(
            "post-self-recursive-growth runtime-daemon",
            "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon/post_self_recursive_growth_runtime_daemon_reference_review_001__post_self_recursive_growth_runtime_daemon_result.json",
            bounded_runtime_daemon_posture_recorded=True,
            bounded_runtime_daemon_envelope_recorded=True,
            public_api_created=False,
            participant_facing_interface_created=False,
            distributed_network_behavior_created=False,
        ),
        "selected_runtime_daemon_terminal_summary_basis": {
            "declared": True,
            "path": "spec/POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_TERMINAL_SUMMARY_V0.md",
            "runtime_loop_not_created": True,
            "runtime_daemon_bounded": True,
        },
        "selected_runtime_daemon_boundary_basis": _basis_reference(
            "post-self-recursive-growth runtime-daemon-boundary",
            "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon_boundary/post_self_recursive_growth_runtime_daemon_boundary_reference_review_001__post_self_recursive_growth_runtime_daemon_boundary_result.json",
        ),
        "selected_runtime_daemon_boundary_v1_failure_lineage_basis": {
            "declared": True,
            "path": "tests/test_resolve_post_self_recursive_growth_runtime_daemon_boundary.py",
            "failure_lineage_preserved": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_self_recursive_growth_basis": _basis_reference(
            "self-recursive-growth",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth/post_self_continuation_self_recursive_growth_reference_review_001__post_self_continuation_self_recursive_growth_result.json",
        ),
        "selected_self_recursive_growth_boundary_basis": _basis_reference(
            "self-recursive-growth-boundary",
            "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth_boundary/post_self_continuation_self_recursive_growth_boundary_reference_review_001__post_self_continuation_self_recursive_growth_boundary_result.json",
        ),
        "selected_self_continuation_basis": _basis_reference(
            "self-continuation",
            "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation/post_continuation_self_continuation_reference_review_001__post_continuation_self_continuation_result.json",
        ),
        "selected_self_continuation_boundary_basis": _basis_reference(
            "self-continuation-boundary",
            "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary/post_continuation_self_continuation_boundary_reference_review_001__post_continuation_self_continuation_boundary_result.json",
        ),
        "selected_continuation_basis": _basis_reference(
            "continuation",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation/post_reusable_runtime_permission_continuation_reference_review_001__post_reusable_runtime_permission_continuation_result.json",
        ),
        "selected_continuation_boundary_basis": _basis_reference(
            "continuation-boundary",
            "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_reusable_runtime_permission_continuation_boundary/post_reusable_runtime_permission_continuation_boundary_reference_review_001__post_reusable_runtime_permission_continuation_boundary_result.json",
        ),
        "selected_reusable_runtime_permission_basis": _basis_reference(
            "reusable-runtime-permission",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission/post_ongoing_runtime_reusable_runtime_permission_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_result.json",
        ),
        "selected_reusable_runtime_permission_boundary_basis": _basis_reference(
            "reusable-runtime-permission-boundary",
            "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_ongoing_runtime_reusable_runtime_permission_boundary/post_ongoing_runtime_reusable_runtime_permission_boundary_reference_review_001__post_ongoing_runtime_reusable_runtime_permission_boundary_result.json",
        ),
        "selected_ongoing_runtime_basis": _basis_reference(
            "ongoing-runtime",
            "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime/post_runtime_hosting_ongoing_runtime_reference_review_001__post_runtime_hosting_ongoing_runtime_result.json",
        ),
        "selected_runtime_hosting_basis": _basis_reference(
            "runtime-hosting",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting/post_successor_runtime_step_runtime_hosting_reference_review_001__post_successor_runtime_step_runtime_hosting_result.json",
        ),
        "selected_runtime_hosting_boundary_v2_basis": _basis_reference(
            "runtime-hosting-boundary-v2",
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2/post_successor_runtime_step_runtime_hosting_boundary_reference_review_001__post_successor_runtime_step_runtime_hosting_boundary_result.json",
            result_version="0.2.0",
        ),
        "selected_runtime_hosting_boundary_v1_failure_lineage_basis": {
            "declared": True,
            "path": "tests/test_resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            "failure_lineage_preserved": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        },
        "selected_successor_runtime_step_basis": _basis_reference(
            "successor-runtime-step",
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step/post_minimal_runtime_successor_runtime_step_reference_review_001__post_minimal_runtime_successor_runtime_step_result.json",
        ),
        "selected_minimal_runtime_basis": _basis_reference(
            "minimal-runtime",
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime/post_portable_verification_minimal_runtime_reference_review_001__post_portable_verification_minimal_runtime_result.json",
        ),
        "selected_runtime_boundary_basis": _basis_reference(
            "runtime-boundary",
            "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary/post_portable_verification_runtime_boundary_reference_review_001__post_portable_verification_runtime_boundary_result.json",
        ),
        "selected_runtime_readiness_basis": _basis_reference(
            "runtime-readiness",
            "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness/post_portable_verification_runtime_readiness_reference_review_001__post_portable_verification_runtime_readiness_result.json",
        ),
        "selected_portable_verification_final_completion_basis": _basis_reference(
            "portable-verification-final-completion",
            "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
            path="artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion/portable_source_body_verification_final_completion_reference_review_001__portable_source_body_verification_final_completion_result.json",
        ),
        "selected_post_portable_verification_currentness_basis": {
            "declared": True,
            "path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
            "checkability_beyond_original_carrier_not_continuation": True,
            "authorized_next_work": False,
        },
        "selected_returned_second_carrier_capture_lineage_basis": {
            "declared": True,
            "basis_name": "returned second-carrier capture lineage",
            "lineage_only": True,
            "raw_full_prior_artifact_body_returned": False,
        },
        "runtime_loop_scope": list(runtime_loop_scope or SUPPORTED_SCOPE_VALUES),
        "declared_non_claims": dict(declared_non_claims or _canonical_non_claims()),
        "requested_bounded_runtime_loop_envelope": dict(
            requested_bounded_runtime_loop_envelope
            or _default_bounded_runtime_loop_envelope(True)
        ),
        "selected_runtime_loop_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop_boundary/post_runtime_daemon_runtime_loop_boundary_reference_review_001__post_runtime_daemon_runtime_loop_boundary_result.json",
        "selected_runtime_loop_boundary_result_outcome": "POST_RUNTIME_DAEMON_RUNTIME_LOOP_BOUNDARY_RECORDED",
        "selected_runtime_loop_boundary_result_version": RESULT_VERSION,
        "selected_runtime_loop_boundary_failed_check_count": 0,
        "selected_runtime_loop_boundary_declared_future_review": True,
        "selected_runtime_loop_boundary_already_created_runtime_loop": False,
        "selected_runtime_loop_boundary_already_created_public_api": False,
        "selected_runtime_loop_boundary_already_created_participant_facing_interface": False,
        "selected_runtime_loop_boundary_already_created_distributed_network_behavior": False,
        "selected_runtime_loop_boundary_treated_as_runtime_loop": False,
        "selected_runtime_loop_boundary_treated_as_public_api": False,
        "selected_runtime_loop_boundary_treated_as_distributed_network_behavior": False,
        "selected_runtime_loop_boundary_authorized_future_work": False,
        "selected_runtime_loop_boundary_non_claims_canonicalized": True,
        "selected_runtime_daemon_result_path": "artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon/post_self_recursive_growth_runtime_daemon_reference_review_001__post_self_recursive_growth_runtime_daemon_result.json",
        "selected_runtime_daemon_result_outcome": "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_RECORDED",
        "selected_runtime_daemon_result_version": RESULT_VERSION,
        "selected_runtime_daemon_failed_check_count": 0,
        "selected_runtime_daemon_bounded_posture_recorded": True,
        "selected_runtime_daemon_bounded_runtime_daemon_envelope_recorded": True,
        "selected_runtime_daemon_already_created_public_api": False,
        "selected_runtime_daemon_already_created_participant_facing_interface": False,
        "selected_runtime_daemon_already_created_distributed_network_behavior": False,
        "selected_bounded_runtime_daemon_envelope_treated_as_runtime_loop_before_review": False,
        "selected_bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity_before_review": False,
        "selected_runtime_daemon_boundary_result_path": "artifacts/integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon_boundary/post_self_recursive_growth_runtime_daemon_boundary_reference_review_001__post_self_recursive_growth_runtime_daemon_boundary_result.json",
        "selected_runtime_daemon_boundary_result_outcome": "POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY_RECORDED",
        "selected_runtime_daemon_boundary_result_version": RESULT_VERSION,
        "selected_runtime_daemon_boundary_failed_check_count": 0,
        "selected_runtime_daemon_boundary_v1_failure_hidden": False,
        "selected_runtime_daemon_boundary_v1_failure_repaired": False,
        "selected_runtime_daemon_boundary_v1_failure_claimed_passed": False,
        "selected_self_recursive_growth_result_outcome": "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_RECORDED",
        "selected_self_recursive_growth_result_version": RESULT_VERSION,
        "selected_self_recursive_growth_failed_check_count": 0,
        "selected_self_recursive_growth_boundary_result_outcome": "POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY_RECORDED",
        "selected_self_recursive_growth_boundary_result_version": RESULT_VERSION,
        "selected_self_recursive_growth_boundary_failed_check_count": 0,
        "selected_self_continuation_result_outcome": "POST_CONTINUATION_SELF_CONTINUATION_RECORDED",
        "selected_self_continuation_result_version": RESULT_VERSION,
        "selected_self_continuation_failed_check_count": 0,
        "selected_self_continuation_boundary_result_outcome": "POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY_RECORDED",
        "selected_self_continuation_boundary_result_version": RESULT_VERSION,
        "selected_self_continuation_boundary_failed_check_count": 0,
        "selected_continuation_result_outcome": "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_RECORDED",
        "selected_continuation_result_version": RESULT_VERSION,
        "selected_continuation_failed_check_count": 0,
        "selected_continuation_boundary_result_outcome": "POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY_RECORDED",
        "selected_continuation_boundary_result_version": RESULT_VERSION,
        "selected_continuation_boundary_failed_check_count": 0,
        "selected_reusable_runtime_permission_result_outcome": "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_RECORDED",
        "selected_reusable_runtime_permission_result_version": RESULT_VERSION,
        "selected_reusable_runtime_permission_failed_check_count": 0,
        "selected_reusable_runtime_permission_boundary_result_outcome": "POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION_BOUNDARY_RECORDED",
        "selected_reusable_runtime_permission_boundary_result_version": RESULT_VERSION,
        "selected_reusable_runtime_permission_boundary_failed_check_count": 0,
        "selected_ongoing_runtime_result_outcome": "POST_RUNTIME_HOSTING_ONGOING_RUNTIME_RECORDED",
        "selected_ongoing_runtime_result_version": RESULT_VERSION,
        "selected_ongoing_runtime_failed_check_count": 0,
        "selected_runtime_hosting_result_outcome": "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        "selected_runtime_hosting_result_version": RESULT_VERSION,
        "selected_runtime_hosting_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v2_result_outcome": "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
        "selected_runtime_hosting_boundary_v2_result_version": "0.2.0",
        "selected_runtime_hosting_boundary_v2_failed_check_count": 0,
        "selected_runtime_hosting_boundary_v1_failure_repaired": False,
        "selected_runtime_hosting_boundary_v1_failure_hidden": False,
        "selected_runtime_hosting_boundary_v1_failure_claimed_passed": False,
        "selected_successor_runtime_step_result_outcome": "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        "selected_successor_runtime_step_result_version": RESULT_VERSION,
        "selected_successor_runtime_step_failed_check_count": 0,
        "selected_minimal_runtime_result_outcome": "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        "selected_minimal_runtime_result_version": RESULT_VERSION,
        "selected_minimal_runtime_failed_check_count": 0,
        "selected_runtime_boundary_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_BOUNDARY_RECORDED",
        "selected_runtime_boundary_result_version": RESULT_VERSION,
        "selected_runtime_boundary_failed_check_count": 0,
        "selected_runtime_readiness_result_outcome": "POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_RECORDED",
        "selected_runtime_readiness_result_version": RESULT_VERSION,
        "selected_runtime_readiness_failed_check_count": 0,
        "selected_portable_verification_final_completion_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_FINAL_COMPLETION_RECORDED",
        "selected_portable_verification_final_completion_result_version": RESULT_VERSION,
        "selected_portable_verification_final_completion_failed_check_count": 0,
        "selected_post_portable_currentness_surface_path": "spec/POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_V0.md",
        "selected_post_portable_currentness_surface_states_checkability_not_continuation": True,
        "selected_post_portable_currentness_surface_authorized_next_work": False,
        "reference_shaped_input_posture": True,
    }
    for section in _POSTURE_SECTIONS:
        request[section] = _posture(
            True,
            section.upper(),
            "declared bounded runtime-loop posture",
        )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request.setdefault(key, False)
    if overrides:
        request.update(copy.deepcopy(overrides))
    return request
