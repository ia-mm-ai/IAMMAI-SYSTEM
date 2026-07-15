"""Bounded portable source-body verification command success resolver.

This module records at most one bounded command-success posture downstream of
the clean command success boundary v3 basis. Command success remains command
success only. It is not source, authority, currentness, final completion, public
readiness, deployment readiness, operation permission, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on work.

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


class PortableSourceBodyVerificationCommandSuccessError(Exception):
    """Raised for explicit unreadable path or malformed JSON path inputs."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_success"
RESULT_TYPE = "portable_source_body_verification_command_success_result"
RESULT_VERSION = "0.1.0"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success"
)

CORE_QUESTION = (
    "Can the recorded command success boundary v3 basis be used to record one "
    "bounded command success without creating source, authority, currentness, "
    "final completion, public readiness, deployment readiness, operation "
    "permission, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

BOUNDARY_V3_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_RECORDED"
COMMAND_RESULT_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
OUTPUT_REPORT_ARTIFACT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)
OUTPUT_CAPTURE_V2_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"

SUPPORTED_COMMAND_SUCCESS_SCOPE = (
    "COMMAND_SUCCESS_ONLY",
    "ONE_BOUNDED_COMMAND_SUCCESS_RECORDED",
    "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_PRESERVED",
    "COMMAND_SUCCESS_BOUNDARY_V1_PREDECESSOR_FAILURE_PRESERVED",
    "COMMAND_SUCCESS_BOUNDARY_V2_PREDECESSOR_FAILURE_PRESERVED",
    "COMMAND_RESULT_V2_BASIS_PRESERVED",
    "BOUNDED_COMMAND_RESULT_PRESERVED",
    "COMMAND_RESULT_V1_PREDECESSOR_FAILURE_PRESERVED",
    "COMMAND_RESULT_BOUNDARY_BASIS_PRESERVED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED",
    "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_PRESERVED",
    "OUTPUT_CAPTURE_V2_BASIS_PRESERVED",
    "OUTPUT_CAPTURE_V1_PREDECESSOR_FAILURE_PRESERVED",
    "BOUNDED_OUTPUT_CAPTURE_EVENT_PRESERVED",
    "COMMAND_OUTPUT_BASIS_PRESERVED",
    "RECORDED_COMMAND_EXECUTION_EVENT_PRESERVED",
    "EXECUTION_TRACE_AUDIT_ONLY_PRESERVED",
    "REPORT_BODY_ABSENT_OR_BOUNDED",
    "RESULT_BODY_ABSENT_OR_BOUNDED",
    "SUCCESS_BODY_ABSENT_OR_BOUNDED",
    "REPORT_BODY_NOT_INVENTED",
    "RESULT_BODY_NOT_INVENTED",
    "SUCCESS_BODY_NOT_INVENTED",
    "COMMAND_SUCCESS_IS_NOT_SOURCE",
    "COMMAND_SUCCESS_IS_NOT_AUTHORITY",
    "COMMAND_SUCCESS_IS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_IS_NOT_FINAL_COMPLETION",
    "COMMAND_SUCCESS_IS_NOT_PUBLIC_READINESS",
    "COMMAND_SUCCESS_IS_NOT_DEPLOYMENT_READINESS",
    "COMMAND_SUCCESS_IS_NOT_OPERATION_PERMISSION",
    "COMMAND_SUCCESS_IS_NOT_CONTINUATION",
    "COMMAND_SUCCESS_IS_NOT_REUSABLE_PERMISSION",
    "COMMAND_SUCCESS_IS_NOT_DERIVATIVE_RECEPTION",
    "COMMAND_SUCCESS_IS_NOT_VESSEL_RELATION",
    "COMMAND_SUCCESS_IS_NOT_ANOTHER_RECEPTION_REQUEST",
    "COMMAND_SUCCESS_IS_NOT_FOLLOW_ON_WORK",
    "COMMAND_SUCCESS_BOUNDARY_IS_NOT_SUCCESS",
    "COMMAND_RESULT_IS_NOT_SUCCESS",
    "COMMAND_RESULT_IS_NOT_SOURCE",
    "COMMAND_RESULT_IS_NOT_AUTHORITY",
    "COMMAND_RESULT_IS_NOT_CURRENTNESS",
    "COMMAND_RESULT_IS_NOT_FINAL_COMPLETION",
    "COMMAND_RESULT_IS_NOT_PUBLIC_READINESS",
    "COMMAND_RESULT_IS_NOT_DEPLOYMENT_READINESS",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_RESULT_AUTHORITY",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_SUCCESS",
    "OUTPUT_CAPTURE_IS_NOT_RESULT",
    "OUTPUT_CAPTURE_IS_NOT_SUCCESS",
    "OUTPUT_CAPTURE_IS_NOT_SOURCE",
    "OUTPUT_CAPTURE_IS_NOT_AUTHORITY",
    "OUTPUT_CAPTURE_IS_NOT_CURRENTNESS",
    "OUTPUT_CAPTURE_IS_NOT_FINAL_COMPLETION",
    "EXECUTION_TRACE_IS_NOT_SUCCESS",
    "EXECUTION_TRACE_IS_NOT_SOURCE",
    "EXECUTION_TRACE_IS_NOT_AUTHORITY",
    "EXECUTION_TRACE_IS_NOT_CURRENTNESS",
    "EXECUTION_TRACE_IS_NOT_FINAL_COMPLETION",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
    "NO_PUBLIC_READINESS_CREATED",
    "NO_DEPLOYMENT_READINESS_CREATED",
    "NO_OPERATION_PERMISSION_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_DERIVATIVE_RECEPTION",
    "NO_VESSEL_RELATION",
    "NO_ANOTHER_RECEPTION_REQUEST",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
    "NO_SOURCE_INFERENCE",
    "NO_AUTHORITY_INFERENCE",
    "NO_CURRENTNESS_INFERENCE",
    "NO_FINAL_COMPLETION_INFERENCE",
    "NO_PUBLIC_READINESS_INFERENCE",
    "NO_DEPLOYMENT_READINESS_INFERENCE",
    "NO_OPERATION_PERMISSION_INFERENCE",
    "NO_FOLLOW_ON_WORK_INFERENCE",
    "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
    "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
    "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
    "CONSUMED_REQUEST_NOT_REOPENED",
    "V1_COMMAND_SUCCESS_BOUNDARY_FAILURE_REMAINS_VISIBLE",
    "V1_COMMAND_SUCCESS_BOUNDARY_NOT_REPAIRED",
    "V1_COMMAND_SUCCESS_BOUNDARY_NOT_HIDDEN",
    "V1_COMMAND_SUCCESS_BOUNDARY_NOT_CLAIMED_PASSED",
    "V2_COMMAND_SUCCESS_BOUNDARY_FAILURE_REMAINS_VISIBLE",
    "V2_COMMAND_SUCCESS_BOUNDARY_NOT_REPAIRED",
    "V2_COMMAND_SUCCESS_BOUNDARY_NOT_HIDDEN",
    "V2_COMMAND_SUCCESS_BOUNDARY_NOT_CLAIMED_PASSED",
    "V3_COMMAND_SUCCESS_BOUNDARY_SUCCESSOR_DOES_NOT_ERASE_V1",
    "V3_COMMAND_SUCCESS_BOUNDARY_SUCCESSOR_DOES_NOT_ERASE_V2",
    "V1_COMMAND_RESULT_FAILURE_REMAINS_VISIBLE",
    "V1_COMMAND_RESULT_NOT_REPAIRED",
    "V1_COMMAND_RESULT_NOT_HIDDEN",
    "V1_COMMAND_RESULT_NOT_CLAIMED_PASSED",
    "V2_COMMAND_RESULT_SUCCESSOR_DOES_NOT_ERASE_V1",
    "V1_OUTPUT_CAPTURE_FAILURE_REMAINS_VISIBLE",
    "V1_OUTPUT_CAPTURE_NOT_REPAIRED",
    "V1_OUTPUT_CAPTURE_NOT_HIDDEN",
    "V1_OUTPUT_CAPTURE_NOT_CLAIMED_PASSED",
    "V2_OUTPUT_CAPTURE_SUCCESSOR_DOES_NOT_ERASE_V1",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_NOT_COMMAND_RESULT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_COMMAND_SUCCESS",
    "COMMAND_REPORT_LINEAGE_NOT_SOURCE",
    "COMMAND_REPORT_LINEAGE_NOT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_NOT_CURRENTNESS",
    "V1_REQUEST_ADMISSION_PREDECESSOR_FAILURE_REMAINS_VISIBLE",
    "V2_SUCCESSOR_DOES_NOT_REPAIR_V1_REQUEST_ADMISSION",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "SELECTED_BASIS_REFERENCE_SHAPE_PRESERVED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "SUMMARY_SURFACE_CONFORMANCE_PRESERVED",
    "REFERENCE_SHAPED_BASIS_REQUIRED",
    "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
)

SELECTED_BASIS_KEYS = (
    "selected_command_success_boundary_v3_basis",
    "selected_command_success_boundary_v3_terminal_summary_basis",
    "selected_command_success_boundary_v1_predecessor_failure_basis",
    "selected_command_success_boundary_v2_predecessor_failure_basis",
    "selected_command_success_boundary_spec_basis",
    "selected_command_result_v2_basis",
    "selected_command_result_v2_terminal_summary_basis",
    "selected_command_result_v1_predecessor_failure_basis",
    "selected_command_result_boundary_basis",
    "selected_command_result_boundary_terminal_summary_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_output_report_artifact_terminal_summary_basis",
    "selected_command_output_report_artifact_boundary_basis",
    "selected_command_output_report_artifact_boundary_terminal_summary_basis",
    "selected_output_capture_v2_basis",
    "selected_output_capture_v2_terminal_summary_basis",
    "selected_output_capture_v1_predecessor_failure_basis",
    "selected_output_capture_boundary_basis",
    "selected_command_output_basis",
    "selected_command_output_boundary_basis",
    "selected_command_output_containment_basis",
    "selected_post_invocation_command_execution_basis",
    "selected_post_invocation_command_execution_terminal_summary_basis",
    "selected_command_invocation_basis",
    "selected_command_execution_review_basis",
    "selected_request_consumption_basis",
    "selected_consumed_request_basis",
    "selected_v2_admitted_request_basis",
    "selected_v1_predecessor_failure_basis",
    "selected_older_command_execution_boundary_lineage_basis",
    "selected_command_report_lineage_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
)

POSTURE_KEYS = (
    "command_success_only_posture",
    "one_bounded_command_success_posture",
    "command_success_boundary_v3_basis_preserved_posture",
    "command_success_boundary_v1_predecessor_failure_preserved_posture",
    "command_success_boundary_v2_predecessor_failure_preserved_posture",
    "command_result_v2_basis_preserved_posture",
    "bounded_command_result_preserved_posture",
    "command_result_v1_predecessor_failure_preserved_posture",
    "command_result_boundary_basis_preserved_posture",
    "command_output_report_artifact_basis_preserved_posture",
    "bounded_command_output_report_artifact_preserved_posture",
    "command_output_report_artifact_boundary_basis_preserved_posture",
    "output_capture_v2_basis_preserved_posture",
    "output_capture_v1_predecessor_failure_preserved_posture",
    "bounded_output_capture_event_preserved_posture",
    "command_output_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "report_body_absent_or_bounded_posture",
    "result_body_absent_or_bounded_posture",
    "success_body_absent_or_bounded_posture",
    "no_report_body_invented_posture",
    "no_result_body_invented_posture",
    "no_success_body_invented_posture",
    "no_source_created_posture",
    "no_authority_created_posture",
    "no_currentness_created_posture",
    "no_final_completion_posture",
    "no_public_readiness_created_posture",
    "no_deployment_readiness_created_posture",
    "no_operation_permission_created_posture",
    "no_continuation_authorized_posture",
    "no_reusable_permission_posture",
    "no_derivative_reception_posture",
    "no_vessel_relation_posture",
    "no_another_reception_request_posture",
    "no_follow_on_work_posture",
    "no_source_inference_posture",
    "no_authority_inference_posture",
    "no_currentness_inference_posture",
    "no_final_completion_inference_posture",
    "no_public_readiness_inference_posture",
    "no_deployment_readiness_inference_posture",
    "no_operation_permission_inference_posture",
    "no_follow_on_work_inference_posture",
    "no_unbounded_pass_fail_inference_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "summary_surface_conformance_preserved_posture",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "success_body_invented",
    "source_created",
    "authority_created",
    "currentness_created",
    "final_completion_claimed",
    "public_readiness_created",
    "deployment_readiness_created",
    "operation_permission_created",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "source_inference_made",
    "authority_inference_made",
    "currentness_inference_made",
    "final_completion_inference_made",
    "public_readiness_inference_made",
    "deployment_readiness_inference_made",
    "operation_permission_inference_made",
    "follow_on_work_inference_made",
    "unbounded_pass_fail_inference_made",
    "command_success_treated_as_source",
    "command_success_treated_as_authority",
    "command_success_treated_as_currentness",
    "command_success_treated_as_final_completion",
    "command_success_treated_as_public_readiness",
    "command_success_treated_as_deployment_readiness",
    "command_success_treated_as_operation_permission",
    "command_success_treated_as_continuation",
    "command_success_treated_as_reusable_permission",
    "command_success_treated_as_derivative_reception",
    "command_success_treated_as_vessel_relation",
    "command_success_treated_as_another_reception_request",
    "command_success_treated_as_follow_on_work",
    "command_success_boundary_treated_as_success",
    "command_result_treated_as_success",
    "command_result_treated_as_source",
    "command_result_treated_as_authority",
    "command_result_treated_as_currentness",
    "command_result_treated_as_final_completion",
    "command_result_treated_as_public_readiness",
    "command_result_treated_as_deployment_readiness",
    "command_output_report_artifact_treated_as_result_authority",
    "command_output_report_artifact_treated_as_success",
    "output_capture_treated_as_result",
    "output_capture_treated_as_success",
    "output_capture_treated_as_source",
    "output_capture_treated_as_authority",
    "output_capture_treated_as_currentness",
    "output_capture_treated_as_final_completion",
    "execution_trace_treated_as_success",
    "execution_trace_treated_as_source",
    "execution_trace_treated_as_authority",
    "execution_trace_treated_as_currentness",
    "execution_trace_treated_as_final_completion",
    "authorization_token_reused",
    "consumed_request_reopened",
    "full_prior_artifacts_embedded",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "v1_command_success_boundary_repaired",
    "v1_command_success_boundary_hidden",
    "v1_command_success_boundary_claimed_passed",
    "v2_command_success_boundary_repaired",
    "v2_command_success_boundary_hidden",
    "v2_command_success_boundary_claimed_passed",
    "v3_command_success_boundary_erased_v1",
    "v3_command_success_boundary_erased_v2",
    "v1_command_result_repaired",
    "v1_command_result_hidden",
    "v1_command_result_claimed_passed",
    "v2_command_result_erased_v1",
    "v1_output_capture_repaired",
    "v1_output_capture_hidden",
    "v1_output_capture_claimed_passed",
    "v2_output_capture_erased_v1",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "command_success_recorded",
    "bounded_command_success_recorded",
    "command_success_boundary_v3_basis_preserved",
    "command_success_boundary_v1_predecessor_failure_preserved",
    "command_success_boundary_v2_predecessor_failure_preserved",
    "command_result_v2_basis_preserved",
    "bounded_command_result_preserved",
    "command_result_v1_predecessor_failure_preserved",
    "command_result_boundary_basis_preserved",
    "command_output_report_artifact_basis_preserved",
    "bounded_command_output_report_artifact_preserved",
    "command_output_report_artifact_boundary_basis_preserved",
    "output_capture_v2_basis_preserved",
    "output_capture_v1_predecessor_failure_preserved",
    "bounded_output_capture_event_preserved",
    "command_output_basis_preserved",
    "recorded_command_execution_event_preserved",
    "execution_trace_audit_only_preserved",
    "report_body_absent_or_bounded",
    "result_body_absent_or_bounded",
    "success_body_absent_or_bounded",
    "report_body_not_invented",
    "result_body_not_invented",
    "success_body_not_invented",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "final_completion_not_created",
    "public_readiness_not_created",
    "deployment_readiness_not_created",
    "operation_permission_not_created",
    "continuation_not_authorized",
    "reusable_permission_not_created",
    "derivative_reception_not_authorized",
    "vessel_relation_not_authorized",
    "another_reception_request_not_authorized",
    "follow_on_work_not_authorized",
    "source_inference_blocked",
    "authority_inference_blocked",
    "currentness_inference_blocked",
    "final_completion_inference_blocked",
    "public_readiness_inference_blocked",
    "deployment_readiness_inference_blocked",
    "operation_permission_inference_blocked",
    "follow_on_work_inference_blocked",
    "unbounded_pass_fail_inference_blocked",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "returned_result_containment_preserved",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "summary_surface_conformance_preserved",
)

PUBLIC_BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_SUCCESS_REQUEST_MALFORMED",
        "DECLARED_COMMAND_SUCCESS_REQUEST_UNREADABLE",
        "COMMAND_SUCCESS_QUESTION_UNDECLARED",
        "COMMAND_SUCCESS_INTENT_UNSUPPORTED",
        "COMMAND_SUCCESS_EXPLICIT_BLOCK_INTENT",
        "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED",
        "COMMAND_SUCCESS_BOUNDARY_V3_FAILED_CHECKS_PRESENT",
        "COMMAND_SUCCESS_BOUNDARY_V3_VERSION_NOT_0_3_0",
        "COMMAND_SUCCESS_BOUNDARY_V3_PREDECESSOR_CHAIN_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_V1_FAILURE_EVIDENCE_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_V2_FAILURE_EVIDENCE_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V1",
        "COMMAND_SUCCESS_BOUNDARY_V3_HID_V1",
        "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V1_PASSED",
        "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V1",
        "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V2",
        "COMMAND_SUCCESS_BOUNDARY_V3_HID_V2",
        "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V2_PASSED",
        "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V2",
        "COMMAND_SUCCESS_BOUNDARY_V3_DID_NOT_DECLARE_FUTURE_SUCCESS_STEP",
        "COMMAND_SUCCESS_BOUNDARY_V3_ALREADY_CREATED_SUCCESS",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_SUCCESS",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_CURRENTNESS",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FINAL_COMPLETION",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_PUBLIC_READINESS",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_DEPLOYMENT_READINESS",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_AUTHORITY",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FOLLOW_ON_WORK",
        "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_UNBOUNDED_PASS_FAIL",
        "COMMAND_SUCCESS_BOUNDARY_V3_SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        "COMMAND_SUCCESS_BOUNDARY_V3_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
        "COMMAND_SUCCESS_BOUNDARY_V3_SUMMARY_SURFACE_CONFORMANCE_MISSING",
        "COMMAND_RESULT_V2_BASIS_MISSING",
        "COMMAND_RESULT_V2_NOT_RECORDED",
        "COMMAND_RESULT_V2_FAILED_CHECKS_PRESENT",
        "COMMAND_RESULT_V2_VERSION_NOT_0_2_0",
        "COMMAND_RESULT_V2_ALREADY_CREATED_SUCCESS",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_SUCCESS",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_SOURCE",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_AUTHORITY",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_CURRENTNESS",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_FINAL_COMPLETION",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_PUBLIC_READINESS",
        "COMMAND_RESULT_V2_TREATED_RESULT_AS_DEPLOYMENT_READINESS",
        "COMMAND_RESULT_BOUNDARY_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT_AUTHORITY",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_MISSING",
        "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        "OUTPUT_CAPTURE_V2_NOT_RECORDED",
        "OUTPUT_CAPTURE_V2_FAILED_CHECKS_PRESENT",
        "OUTPUT_CAPTURE_V2_VERSION_NOT_0_2_0",
        "OUTPUT_CAPTURE_V2_JSON_SAFE_RESULT_NOT_PRESERVED",
        "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING",
        "OUTPUT_CAPTURE_V2_REPAIRED_V1",
        "OUTPUT_CAPTURE_V2_HID_V1",
        "OUTPUT_CAPTURE_V2_CLAIMED_V1_PASSED",
        "OUTPUT_CAPTURE_V2_ERASED_V1",
        "OUTPUT_CAPTURE_V2_INVENTED_STDOUT_CONTENT",
        "OUTPUT_CAPTURE_V2_INVENTED_STDERR_CONTENT",
        "OUTPUT_CAPTURE_V2_INVENTED_PROCESS_OUTPUT_CONTENT",
        "OUTPUT_CAPTURE_V2_INVENTED_RAW_OUTPUT_BODY_CONTENT",
        "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
        "COMMAND_OUTPUT_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
        "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
        "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
        "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_BOUNDARY_BASIS_MISSING",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "COMMAND_SUCCESS_TREATED_AS_SOURCE",
        "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS",
        "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS",
        "COMMAND_SUCCESS_TREATED_AS_OPERATION_PERMISSION",
        "COMMAND_SUCCESS_TREATED_AS_CONTINUATION",
        "COMMAND_SUCCESS_TREATED_AS_REUSABLE_PERMISSION",
        "COMMAND_SUCCESS_TREATED_AS_DERIVATIVE_RECEPTION",
        "COMMAND_SUCCESS_TREATED_AS_VESSEL_RELATION",
        "COMMAND_SUCCESS_TREATED_AS_ANOTHER_RECEPTION_REQUEST",
        "COMMAND_SUCCESS_TREATED_AS_FOLLOW_ON_WORK",
        "SUCCESS_BODY_INVENTED",
        "SOURCE_CREATED",
        "AUTHORITY_CREATED",
        "CURRENTNESS_CREATED",
        "FINAL_COMPLETION_CLAIMED",
        "PUBLIC_READINESS_CREATED",
        "DEPLOYMENT_READINESS_CREATED",
        "OPERATION_PERMISSION_CREATED",
        "CONTINUATION_AUTHORIZED",
        "REUSABLE_PERMISSION_CREATED",
        "DERIVATIVE_RECEPTION_AUTHORIZED",
        "VESSEL_RELATION_AUTHORIZED",
        "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        "FOLLOW_ON_WORK_AUTHORIZED",
        "SOURCE_INFERENCE_MADE",
        "AUTHORITY_INFERENCE_MADE",
        "CURRENTNESS_INFERENCE_MADE",
        "FINAL_COMPLETION_INFERENCE_MADE",
        "PUBLIC_READINESS_INFERENCE_MADE",
        "DEPLOYMENT_READINESS_INFERENCE_MADE",
        "OPERATION_PERMISSION_INFERENCE_MADE",
        "FOLLOW_ON_WORK_INFERENCE_MADE",
        "UNBOUNDED_PASS_FAIL_INFERENCE_MADE",
        "EXECUTION_TRACE_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_SOURCE",
        "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
        "EXECUTION_TRACE_TREATED_AS_CURRENTNESS",
        "EXECUTION_TRACE_TREATED_AS_FINAL_COMPLETION",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_SUCCESS",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_SOURCE",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_AUTHORITY",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_ONLY_POSTURE_MISSING",
        "ONE_BOUNDED_COMMAND_SUCCESS_POSTURE_MISSING",
        "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_PRESERVED_POSTURE_MISSING",
        "COMMAND_RESULT_V2_BASIS_PRESERVED_POSTURE_MISSING",
        "BOUNDED_COMMAND_RESULT_PRESERVED_POSTURE_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
        "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING",
        "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "SUMMARY_SURFACE_CONFORMANCE_POSTURE_MISSING",
        "SUCCESS_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
        "NO_SOURCE_CREATED_POSTURE_MISSING",
        "NO_AUTHORITY_CREATED_POSTURE_MISSING",
        "NO_CURRENTNESS_CREATED_POSTURE_MISSING",
        "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "NO_PUBLIC_READINESS_CREATED_POSTURE_MISSING",
        "NO_DEPLOYMENT_READINESS_CREATED_POSTURE_MISSING",
        "NO_OPERATION_PERMISSION_CREATED_POSTURE_MISSING",
        "NO_CONTINUATION_REUSABLE_FOLLOW_ON_POSTURE_MISSING",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "ARTIFACTS_MUTATED",
        "DEPLOYMENT_CREATED",
        "RUNTIME_HOSTING_CREATED",
        "PUBLIC_RELEASE_CREATED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "UNSUPPORTED_COMMAND_SUCCESS_SCOPE",
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
        "authority_body",
        "currentness_claim",
        "final_completion_claim",
        "public_readiness_claim",
        "deployment_readiness_claim",
    }
)
RAW_SENTINELS = ("RAW_COMMAND_SUCCESS_BOUNDARY_BODY_MUST_NOT_RETURN", "MUST_NOT_RETURN")


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
    for container_key in ("metadata", "summary"):
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
        return bool(value) and value.get("declared", True) is not False and value.get("basis_declared", True) is not False
    return value is not None


def _basis_declared(request: Mapping[str, Any], key: str) -> bool:
    return _declared(request.get(key))


def _true(request: Mapping[str, Any], key: str, names: Sequence[str], shortcuts: Sequence[str] = ()) -> bool:
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
    value = request.get("command_success_scope", [])
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
    section.setdefault("reference_shaped", True)
    section.setdefault("full_prior_artifact_body_embedded", False)
    section.setdefault("raw_full_prior_artifact_body_returned", False)
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
    section.setdefault("command_success_posture_only", True)
    section.setdefault("recorded_outcome_only", recorded)
    section.setdefault("source_created", False)
    section.setdefault("authority_created", False)
    section.setdefault("currentness_created", False)
    section.setdefault("final_completion_claimed", False)
    section.setdefault("public_readiness_created", False)
    section.setdefault("deployment_readiness_created", False)
    section.setdefault("operation_permission_created", False)
    section.setdefault("follow_on_work_authorized", False)
    return section


def _non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = _non_claims_from_request(request)
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _build_checks(request: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(request, Mapping):
        return [
            _check(
                "declared command success request is mapping",
                False,
                "JSON object mapping",
                type(request).__name__,
                "DECLARED_COMMAND_SUCCESS_REQUEST_MALFORMED",
            )
        ]

    b3 = "selected_command_success_boundary_v3_basis"
    result = "selected_command_result_v2_basis"
    artifact = "selected_command_output_report_artifact_basis"
    capture = "selected_output_capture_v2_basis"
    execution = "selected_post_invocation_command_execution_basis"
    lineage = "selected_command_report_lineage_basis"
    checks: list[dict[str, Any]] = []

    checks.append(_check("command success question declared", request.get("command_success_question") == CORE_QUESTION, CORE_QUESTION, request.get("command_success_question"), "COMMAND_SUCCESS_QUESTION_UNDECLARED"))
    checks.append(_check("command success intent supported", request.get("command_success_intent") in SUPPORTED_INTENTS, str(SUPPORTED_INTENTS), request.get("command_success_intent"), "COMMAND_SUCCESS_INTENT_UNSUPPORTED"))
    if request.get("command_success_intent") == INTENT_BLOCK:
        checks.append(_check("command success explicit block intent absent", False, "record or do-not-record intent", request.get("command_success_intent"), "COMMAND_SUCCESS_EXPLICIT_BLOCK_INTENT"))

    unsupported_scope = [value for value in _scope_values(request) if value not in SUPPORTED_COMMAND_SUCCESS_SCOPE]
    checks.append(_check("command success scope supported", bool(_scope_values(request)) and not unsupported_scope, "supported command success scope values only", {"values": _scope_values(request), "unsupported": unsupported_scope}, "UNSUPPORTED_COMMAND_SUCCESS_SCOPE"))

    declared_basis_codes = (
        ("selected_command_success_boundary_v3_terminal_summary_basis", "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING"),
        (b3, "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_MISSING"),
        ("selected_command_result_boundary_basis", "COMMAND_RESULT_BOUNDARY_BASIS_MISSING"),
        ("selected_command_output_report_artifact_boundary_basis", "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_MISSING"),
        ("selected_output_capture_boundary_basis", "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING"),
        ("selected_command_output_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
        ("selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
        ("selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
        (lineage, "COMMAND_REPORT_LINEAGE_BASIS_MISSING"),
        ("selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
        ("selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
        ("selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
        ("selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
        ("selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
    )
    for key, code in declared_basis_codes:
        checks.append(_check(f"{key} declared", _basis_declared(request, key), f"{key} declared as basis only", request.get(key), code))

    checks.extend(
        [
            _check("command success boundary v3 outcome recorded", _value(request, b3, ("outcome", "result_outcome"), ("selected_command_success_boundary_v3_result_outcome",)) == BOUNDARY_V3_RECORDED, BOUNDARY_V3_RECORDED, _value(request, b3, ("outcome", "result_outcome"), ("selected_command_success_boundary_v3_result_outcome",)), "COMMAND_SUCCESS_BOUNDARY_V3_NOT_RECORDED"),
            _check("command success boundary v3 version 0.3.0", _value(request, b3, ("result_version", "version"), ("selected_command_success_boundary_v3_result_version",)) == "0.3.0", "0.3.0", _value(request, b3, ("result_version", "version"), ("selected_command_success_boundary_v3_result_version",)), "COMMAND_SUCCESS_BOUNDARY_V3_VERSION_NOT_0_3_0"),
            _check("command success boundary v3 failed check count zero", _as_int(_value(request, b3, ("failed_check_count",), ("selected_command_success_boundary_v3_failed_check_count",))) == 0, "0", _value(request, b3, ("failed_check_count",), ("selected_command_success_boundary_v3_failed_check_count",)), "COMMAND_SUCCESS_BOUNDARY_V3_FAILED_CHECKS_PRESENT"),
            _check("command success boundary v3 predecessor chain present", bool(_value(request, b3, ("predecessor_chain",), ("selected_command_success_boundary_v3_predecessor_chain_preserved",))), "predecessor chain present", _value(request, b3, ("predecessor_chain",), ("selected_command_success_boundary_v3_predecessor_chain_preserved",)), "COMMAND_SUCCESS_BOUNDARY_V3_PREDECESSOR_CHAIN_MISSING"),
            _check("command success boundary v3 v1 failure preserved", _true(request, b3, ("v1_predecessor_failure_preserved", "command_success_boundary_v1_predecessor_failure_preserved"), ("selected_command_success_boundary_v3_v1_failure_preserved",)), "v1 predecessor failure preserved", _value(request, b3, ("v1_predecessor_failure_preserved", "command_success_boundary_v1_predecessor_failure_preserved"), ("selected_command_success_boundary_v3_v1_failure_preserved",)), "COMMAND_SUCCESS_BOUNDARY_V3_V1_FAILURE_EVIDENCE_MISSING"),
            _check("command success boundary v3 v2 failure preserved", _true(request, b3, ("v2_predecessor_failure_preserved", "command_success_boundary_v2_predecessor_failure_preserved"), ("selected_command_success_boundary_v3_v2_failure_preserved",)), "v2 predecessor failure preserved", _value(request, b3, ("v2_predecessor_failure_preserved", "command_success_boundary_v2_predecessor_failure_preserved"), ("selected_command_success_boundary_v3_v2_failure_preserved",)), "COMMAND_SUCCESS_BOUNDARY_V3_V2_FAILURE_EVIDENCE_MISSING"),
            _check("command success boundary v3 one future success step declared", _true(request, b3, ("one_future_command_success_step_declared",), ("selected_command_success_boundary_v3_future_success_step_declared",)), "one future command-success step declared", _value(request, b3, ("one_future_command_success_step_declared",), ("selected_command_success_boundary_v3_future_success_step_declared",)), "COMMAND_SUCCESS_BOUNDARY_V3_DID_NOT_DECLARE_FUTURE_SUCCESS_STEP"),
            _check("command success boundary v3 selected basis reference shape preserved", _true(request, b3, ("selected_basis_reference_shape_preserved",), ("selected_command_success_boundary_v3_selected_basis_reference_shape_preserved",)), "selected basis reference shape preserved", _value(request, b3, ("selected_basis_reference_shape_preserved",), ("selected_command_success_boundary_v3_selected_basis_reference_shape_preserved",)), "COMMAND_SUCCESS_BOUNDARY_V3_SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
            _check("command success boundary v3 raw full prior body not returned", _false(request, b3, ("raw_full_prior_artifact_body_returned",), ("selected_command_success_boundary_v3_raw_full_prior_artifact_body_returned",)), "raw full prior artifact body returned false", _value(request, b3, ("raw_full_prior_artifact_body_returned",), ("selected_command_success_boundary_v3_raw_full_prior_artifact_body_returned",), False), "COMMAND_SUCCESS_BOUNDARY_V3_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY"),
            _check("command success boundary v3 summary surface conformance preserved", _true(request, b3, ("summary_surface_conformance_preserved",), ("selected_command_success_boundary_v3_summary_surface_conformance_preserved",)), "summary-surface conformance preserved", _value(request, b3, ("summary_surface_conformance_preserved",), ("selected_command_success_boundary_v3_summary_surface_conformance_preserved",)), "COMMAND_SUCCESS_BOUNDARY_V3_SUMMARY_SURFACE_CONFORMANCE_MISSING"),
            _check("command success boundary v3 command success not created", _false(request, b3, ("command_success_created",), ("selected_command_success_boundary_v3_already_created_success",)) and _value(request, b3, ("command_success_still_not_created",), (), True) is True, "command success not created", {"command_success_created": _value(request, b3, ("command_success_created",), ("selected_command_success_boundary_v3_already_created_success",), False), "command_success_still_not_created": _value(request, b3, ("command_success_still_not_created",), (), True)}, "COMMAND_SUCCESS_BOUNDARY_V3_ALREADY_CREATED_SUCCESS"),
            _check("command success boundary v3 success body not invented", _false(request, b3, ("success_body_invented",)) and _true(request, b3, ("success_body_not_invented",)), "success body not invented", {"success_body_invented": _value(request, b3, ("success_body_invented",), (), False), "success_body_not_invented": _value(request, b3, ("success_body_not_invented",))}, "SUCCESS_BODY_INVENTED"),
        ]
    )

    for field, code in (
        ("v1_repaired", "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V1"),
        ("v1_hidden", "COMMAND_SUCCESS_BOUNDARY_V3_HID_V1"),
        ("v1_claimed_passed", "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V1_PASSED"),
        ("v2_repaired", "COMMAND_SUCCESS_BOUNDARY_V3_REPAIRED_V2"),
        ("v2_hidden", "COMMAND_SUCCESS_BOUNDARY_V3_HID_V2"),
        ("v2_claimed_passed", "COMMAND_SUCCESS_BOUNDARY_V3_CLAIMED_V2_PASSED"),
        ("v3_command_success_boundary_erased_v1", "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V1"),
        ("v3_command_success_boundary_erased_v2", "COMMAND_SUCCESS_BOUNDARY_V3_ERASED_V2"),
        ("success_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_SUCCESS"),
        ("currentness_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_CURRENTNESS"),
        ("final_completion_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FINAL_COMPLETION"),
        ("public_readiness_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_PUBLIC_READINESS"),
        ("deployment_readiness_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_DEPLOYMENT_READINESS"),
        ("authority_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_AUTHORITY"),
        ("follow_on_work_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_FOLLOW_ON_WORK"),
        ("unbounded_pass_fail_inference_made", "COMMAND_SUCCESS_BOUNDARY_V3_INFERRED_UNBOUNDED_PASS_FAIL"),
    ):
        checks.append(_check(f"command success boundary v3 {field} false", _false(request, b3, (field,)), f"{field} false", _value(request, b3, (field,), (), False), code))

    checks.extend(
        [
            _check("command result v2 basis declared", _basis_declared(request, result) or bool(request.get("selected_command_result_v2_result_path")), "command result v2 basis declared", request.get(result) or request.get("selected_command_result_v2_result_path"), "COMMAND_RESULT_V2_BASIS_MISSING"),
            _check("command result v2 outcome recorded", _value(request, result, ("outcome", "result_outcome"), ("selected_command_result_v2_result_outcome",)) == COMMAND_RESULT_V2_RECORDED, COMMAND_RESULT_V2_RECORDED, _value(request, result, ("outcome", "result_outcome"), ("selected_command_result_v2_result_outcome",)), "COMMAND_RESULT_V2_NOT_RECORDED"),
            _check("command result v2 version 0.2.0", _value(request, result, ("result_version", "version"), ("selected_command_result_v2_result_version",)) == "0.2.0", "0.2.0", _value(request, result, ("result_version", "version"), ("selected_command_result_v2_result_version",)), "COMMAND_RESULT_V2_VERSION_NOT_0_2_0"),
            _check("command result v2 failed count zero", _as_int(_value(request, result, ("failed_check_count",), ("selected_command_result_v2_failed_check_count",))) == 0, "0", _value(request, result, ("failed_check_count",), ("selected_command_result_v2_failed_check_count",)), "COMMAND_RESULT_V2_FAILED_CHECKS_PRESENT"),
            _check("command result v2 bounded command result preserved", _true(request, result, ("bounded_command_result_recorded", "bounded_command_result_preserved")), "bounded command result preserved", _value(request, result, ("bounded_command_result_recorded", "bounded_command_result_preserved")), "BOUNDED_COMMAND_RESULT_PRESERVED_POSTURE_MISSING"),
            _check("command result v2 did not create command success", _false(request, result, ("command_success_created",)), "command success created false", _value(request, result, ("command_success_created",), (), False), "COMMAND_RESULT_V2_ALREADY_CREATED_SUCCESS"),
            _check("command output/report artifact basis declared", _basis_declared(request, artifact), "command output/report artifact basis declared", request.get(artifact), "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"),
            _check("command output/report artifact outcome recorded", _value(request, artifact, ("outcome", "result_outcome")) == OUTPUT_REPORT_ARTIFACT_RECORDED, OUTPUT_REPORT_ARTIFACT_RECORDED, _value(request, artifact, ("outcome", "result_outcome")), "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED"),
            _check("command output/report artifact failed count zero", _as_int(_value(request, artifact, ("failed_check_count",))) == 0, "0", _value(request, artifact, ("failed_check_count",)), "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT"),
            _check("command output/report artifact bounded artifact preserved", _true(request, artifact, ("bounded_command_output_report_artifact_recorded", "bounded_command_output_report_artifact_preserved")), "bounded command output/report artifact preserved", _value(request, artifact, ("bounded_command_output_report_artifact_recorded", "bounded_command_output_report_artifact_preserved")), "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING"),
            _check("output capture v2 basis declared", _basis_declared(request, capture) or bool(request.get("selected_output_capture_v2_result_path")), "output capture v2 basis declared", request.get(capture) or request.get("selected_output_capture_v2_result_path"), "OUTPUT_CAPTURE_V2_BASIS_MISSING"),
            _check("output capture v2 outcome recorded", _value(request, capture, ("outcome", "result_outcome")) == OUTPUT_CAPTURE_V2_RECORDED, OUTPUT_CAPTURE_V2_RECORDED, _value(request, capture, ("outcome", "result_outcome")), "OUTPUT_CAPTURE_V2_NOT_RECORDED"),
            _check("output capture v2 version 0.2.0", _value(request, capture, ("result_version", "version"), ("selected_output_capture_v2_result_version",)) == "0.2.0", "0.2.0", _value(request, capture, ("result_version", "version"), ("selected_output_capture_v2_result_version",)), "OUTPUT_CAPTURE_V2_VERSION_NOT_0_2_0"),
            _check("output capture v2 failed count zero", _as_int(_value(request, capture, ("failed_check_count",), ("selected_output_capture_v2_failed_check_count",))) == 0, "0", _value(request, capture, ("failed_check_count",), ("selected_output_capture_v2_failed_check_count",)), "OUTPUT_CAPTURE_V2_FAILED_CHECKS_PRESENT"),
            _check("output capture v2 JSON-safe result preserved", _true(request, capture, ("json_safe_result", "json_safe_result_preserved")), "JSON-safe result preserved", _value(request, capture, ("json_safe_result", "json_safe_result_preserved")), "OUTPUT_CAPTURE_V2_JSON_SAFE_RESULT_NOT_PRESERVED"),
            _check("output capture v2 predecessor failure preserved", _true(request, capture, ("v1_predecessor_failure_preserved", "output_capture_v1_predecessor_failure_preserved")), "v1 output-capture predecessor failure preserved", _value(request, capture, ("v1_predecessor_failure_preserved", "output_capture_v1_predecessor_failure_preserved")), "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING"),
            _check("post-invocation command execution basis declared", _basis_declared(request, execution), "post-invocation command execution basis declared", request.get(execution), "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"),
            _check("post-invocation command execution recorded", _value(request, execution, ("outcome", "result_outcome")) is not None, "post-invocation command execution recorded", _value(request, execution, ("outcome", "result_outcome")), "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED"),
            _check("post-invocation command execution failed count zero", _as_int(_value(request, execution, ("failed_check_count",), (), 0)) == 0, "0", _value(request, execution, ("failed_check_count",), (), 0), "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT"),
            _check("post-invocation execution trace audit-only", _true(request, execution, ("execution_trace_audit_only", "execution_trace_audit_only_preserved")), "execution trace audit-only", _value(request, execution, ("execution_trace_audit_only", "execution_trace_audit_only_preserved")), "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY"),
        ]
    )

    for field, code in (
        ("command_result_treated_as_success", "COMMAND_RESULT_V2_TREATED_RESULT_AS_SUCCESS"),
        ("command_result_treated_as_source", "COMMAND_RESULT_V2_TREATED_RESULT_AS_SOURCE"),
        ("command_result_treated_as_authority", "COMMAND_RESULT_V2_TREATED_RESULT_AS_AUTHORITY"),
        ("command_result_treated_as_currentness", "COMMAND_RESULT_V2_TREATED_RESULT_AS_CURRENTNESS"),
        ("command_result_treated_as_final_completion", "COMMAND_RESULT_V2_TREATED_RESULT_AS_FINAL_COMPLETION"),
        ("command_result_treated_as_public_readiness", "COMMAND_RESULT_V2_TREATED_RESULT_AS_PUBLIC_READINESS"),
        ("command_result_treated_as_deployment_readiness", "COMMAND_RESULT_V2_TREATED_RESULT_AS_DEPLOYMENT_READINESS"),
    ):
        checks.append(_check(f"command result v2 {field} false", _false(request, result, (field,)), f"{field} false", _value(request, result, (field,), (), False), code))

    for field, code in (
        ("command_output_report_artifact_treated_as_result_authority", "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT_AUTHORITY"),
        ("command_output_report_artifact_treated_as_success", "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS"),
    ):
        checks.append(_check(f"command output/report artifact {field} false", _false(request, artifact, (field,)), f"{field} false", _value(request, artifact, (field,), (), False), code))

    for field, code in (
        ("v1_repaired", "OUTPUT_CAPTURE_V2_REPAIRED_V1"),
        ("v1_hidden", "OUTPUT_CAPTURE_V2_HID_V1"),
        ("v1_claimed_passed", "OUTPUT_CAPTURE_V2_CLAIMED_V1_PASSED"),
        ("v2_output_capture_erased_v1", "OUTPUT_CAPTURE_V2_ERASED_V1"),
        ("stdout_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDOUT_CONTENT"),
        ("stderr_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDERR_CONTENT"),
        ("process_output_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_PROCESS_OUTPUT_CONTENT"),
        ("raw_output_body_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_RAW_OUTPUT_BODY_CONTENT"),
    ):
        checks.append(_check(f"output capture v2 {field} false", _false(request, capture, (field,)), f"{field} false", _value(request, capture, (field,), (), False), code))

    posture_codes = {
        "command_success_only_posture": "COMMAND_SUCCESS_ONLY_POSTURE_MISSING",
        "one_bounded_command_success_posture": "ONE_BOUNDED_COMMAND_SUCCESS_POSTURE_MISSING",
        "command_success_boundary_v3_basis_preserved_posture": "COMMAND_SUCCESS_BOUNDARY_V3_BASIS_PRESERVED_POSTURE_MISSING",
        "command_result_v2_basis_preserved_posture": "COMMAND_RESULT_V2_BASIS_PRESERVED_POSTURE_MISSING",
        "bounded_command_result_preserved_posture": "BOUNDED_COMMAND_RESULT_PRESERVED_POSTURE_MISSING",
        "command_output_report_artifact_basis_preserved_posture": "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
        "bounded_command_output_report_artifact_preserved_posture": "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING",
        "selected_basis_reference_shape_posture": "SELECTED_BASIS_REFERENCE_SHAPE_POSTURE_MISSING",
        "raw_full_prior_artifact_body_not_returned_posture": "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED_POSTURE_MISSING",
        "summary_surface_conformance_preserved_posture": "SUMMARY_SURFACE_CONFORMANCE_POSTURE_MISSING",
        "success_body_absent_or_bounded_posture": "SUCCESS_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
        "no_source_created_posture": "NO_SOURCE_CREATED_POSTURE_MISSING",
        "no_authority_created_posture": "NO_AUTHORITY_CREATED_POSTURE_MISSING",
        "no_currentness_created_posture": "NO_CURRENTNESS_CREATED_POSTURE_MISSING",
        "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "no_public_readiness_created_posture": "NO_PUBLIC_READINESS_CREATED_POSTURE_MISSING",
        "no_deployment_readiness_created_posture": "NO_DEPLOYMENT_READINESS_CREATED_POSTURE_MISSING",
        "no_operation_permission_created_posture": "NO_OPERATION_PERMISSION_CREATED_POSTURE_MISSING",
    }
    for key, code in posture_codes.items():
        checks.append(_check(f"{key} declared", _declared(request.get(key)), f"{key} declared", request.get(key), code))
    checks.append(_check("no continuation/reusable/follow-on posture declared", all(_declared(request.get(key)) for key in ("no_continuation_authorized_posture", "no_reusable_permission_posture", "no_follow_on_work_posture")), "no continuation, reusable, and follow-on posture declared", {key: request.get(key) for key in ("no_continuation_authorized_posture", "no_reusable_permission_posture", "no_follow_on_work_posture")}, "NO_CONTINUATION_REUSABLE_FOLLOW_ON_POSTURE_MISSING"))

    for field, code in (
        ("command_report_lineage_basis_treated_as_current_report_artifact", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
        ("command_report_lineage_basis_treated_as_command_result_authority", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT_AUTHORITY"),
        ("command_report_lineage_basis_treated_as_command_success", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_SUCCESS"),
        ("command_report_lineage_basis_treated_as_source", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_SOURCE"),
        ("command_report_lineage_basis_treated_as_authority", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_AUTHORITY"),
        ("command_report_lineage_basis_treated_as_currentness", "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENTNESS"),
    ):
        checks.append(_check(f"command report lineage {field} false", _false(request, lineage, (field,)), f"{field} false", _value(request, lineage, (field,), (), False), code))

    non_claims = _non_claims_from_request(request)
    checks.append(_check("required non-claims remain false", _non_claims_false(request), "all required non-claims false", {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS}, "NON_CLAIM_MISSING_OR_FLIPPED"))
    for field, code in (
        ("command_success_treated_as_source", "COMMAND_SUCCESS_TREATED_AS_SOURCE"),
        ("command_success_treated_as_authority", "COMMAND_SUCCESS_TREATED_AS_AUTHORITY"),
        ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("command_success_treated_as_public_readiness", "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS"),
        ("command_success_treated_as_deployment_readiness", "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS"),
        ("command_success_treated_as_operation_permission", "COMMAND_SUCCESS_TREATED_AS_OPERATION_PERMISSION"),
        ("command_success_treated_as_continuation", "COMMAND_SUCCESS_TREATED_AS_CONTINUATION"),
        ("command_success_treated_as_reusable_permission", "COMMAND_SUCCESS_TREATED_AS_REUSABLE_PERMISSION"),
        ("command_success_treated_as_derivative_reception", "COMMAND_SUCCESS_TREATED_AS_DERIVATIVE_RECEPTION"),
        ("command_success_treated_as_vessel_relation", "COMMAND_SUCCESS_TREATED_AS_VESSEL_RELATION"),
        ("command_success_treated_as_another_reception_request", "COMMAND_SUCCESS_TREATED_AS_ANOTHER_RECEPTION_REQUEST"),
        ("command_success_treated_as_follow_on_work", "COMMAND_SUCCESS_TREATED_AS_FOLLOW_ON_WORK"),
        ("success_body_invented", "SUCCESS_BODY_INVENTED"),
        ("source_created", "SOURCE_CREATED"),
        ("authority_created", "AUTHORITY_CREATED"),
        ("currentness_created", "CURRENTNESS_CREATED"),
        ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
        ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
        ("deployment_readiness_created", "DEPLOYMENT_READINESS_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ("source_inference_made", "SOURCE_INFERENCE_MADE"),
        ("authority_inference_made", "AUTHORITY_INFERENCE_MADE"),
        ("currentness_inference_made", "CURRENTNESS_INFERENCE_MADE"),
        ("final_completion_inference_made", "FINAL_COMPLETION_INFERENCE_MADE"),
        ("public_readiness_inference_made", "PUBLIC_READINESS_INFERENCE_MADE"),
        ("deployment_readiness_inference_made", "DEPLOYMENT_READINESS_INFERENCE_MADE"),
        ("operation_permission_inference_made", "OPERATION_PERMISSION_INFERENCE_MADE"),
        ("follow_on_work_inference_made", "FOLLOW_ON_WORK_INFERENCE_MADE"),
        ("unbounded_pass_fail_inference_made", "UNBOUNDED_PASS_FAIL_INFERENCE_MADE"),
        ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
        ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
        ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
        ("execution_trace_treated_as_currentness", "EXECUTION_TRACE_TREATED_AS_CURRENTNESS"),
        ("execution_trace_treated_as_final_completion", "EXECUTION_TRACE_TREATED_AS_FINAL_COMPLETION"),
        ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
        ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
        ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ):
        checks.append(_check(f"non-claim {field} false", non_claims.get(field) is False, f"{field} false", non_claims.get(field), code))

    return checks


def _statement(recorded: bool) -> dict[str, Any]:
    statement = {key: recorded for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    statement.update(
        {
            "command_success_boundary_v3_remains_boundary_basis_only": True,
            "command_result_v2_remains_command_result_posture_only": True,
            "command_output_report_artifact_remains_artifact_posture_only": True,
            "output_capture_v2_remains_output_capture_posture_only": True,
            "execution_trace_remains_audit_only": True,
            "consumed_request_token_remains_closed": True,
            "authorization_token_reuse_blocked": True,
        }
    )
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "source_exists": False,
        "authority_exists": False,
        "currentness_exists": False,
        "final_completion_exists": False,
        "public_readiness_exists": False,
        "deployment_readiness_exists": False,
        "operation_permission_exists": False,
        "continuation_is_authorized": False,
        "reusable_permission_exists": False,
        "derivative_reception_is_authorized": False,
        "vessel_relation_is_authorized": False,
        "another_reception_request_is_authorized": False,
        "follow_on_work_is_authorized": False,
        "success_body_was_invented": False,
        "source_was_inferred": False,
        "authority_was_inferred": False,
        "currentness_was_inferred": False,
        "final_completion_was_inferred": False,
        "public_readiness_was_inferred": False,
        "deployment_readiness_was_inferred": False,
        "operation_permission_was_inferred": False,
        "follow_on_work_was_inferred": False,
        "unbounded_pass_fail_was_inferred": False,
        "command_success_boundary_v3_became_success_source_or_authority": False,
        "command_result_v2_became_command_success": False,
        "command_output_report_artifact_became_result_authority": False,
        "command_output_report_artifact_became_success_authority": False,
        "output_capture_became_result_success_source_authority_currentness_completion": False,
        "execution_trace_became_success_source_authority_currentness_completion": False,
        "v1_command_success_boundary_resolver_was_repaired_hidden_or_passed": False,
        "v2_command_success_boundary_resolver_was_repaired_hidden_or_passed": False,
        "v3_command_success_boundary_erased_v1_or_v2": False,
        "v1_command_result_resolver_was_repaired_hidden_or_passed": False,
        "v1_output_capture_predecessor_was_repaired_hidden_or_passed": False,
        "command_report_lineage_is_current_report_artifact_result_authority_success_source_authority_currentness": False,
        "consumed_request_token_reopened": False,
        "authorization_token_reusable": False,
        "deployment_runtime_public_release_created": False,
        "follow_on_work_authorized": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command success test",
            "command success live artifact",
            "command success terminal summary, if needed",
            "success body, if separately specified",
            "success verdict, if separately specified",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
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
            "public readiness",
            "deployment readiness",
            "final completion",
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
    if request.get("command_success_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None
    if request.get("additional_basis_context") or request.get("requires_additional_basis"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None
    return OUTCOME_RECORDED, None


def resolve_portable_source_body_verification_command_success(
    declared_command_success_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded command success result without mutating inputs."""

    if isinstance(declared_command_success_request, Mapping):
        request = copy.deepcopy(dict(declared_command_success_request))
    else:
        request = {
            "command_success_request_id": "malformed_command_success_request",
            "command_success_question": None,
            "command_success_intent": None,
            "command_success_scope": [],
            "declared_non_claims": {},
        }
    checks = _build_checks(request if isinstance(declared_command_success_request, Mapping) else None)
    outcome, block_code = _outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    statement = _statement(recorded)
    metadata = {
        "portable_source_body_verification_command_success_result_id": (
            f"{_safe_text(request.get('command_success_request_id'))}"
            "__portable_source_body_verification_command_success_result"
        ),
        "portable_source_body_verification_command_success_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_success_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "command_success_request_id": _safe_text(request.get("command_success_request_id")),
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
    }

    result: dict[str, Any] = {
        "portable_source_body_verification_command_success_metadata": metadata,
        "declared_command_success_question": {
            "command_success_request_id": metadata["command_success_request_id"],
            "question": _json_safe(request.get("command_success_question")),
            "intent": _json_safe(request.get("command_success_intent")),
            "core_question": CORE_QUESTION,
            "question_scope": "one bounded command success posture only",
        },
    }
    for key in SELECTED_BASIS_KEYS:
        result[key] = _safe_basis_section(request, key)
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key, recorded)

    result.update(
        {
            "command_success_scope": {
                "scope_values": _scope_values(request),
                "supported_scope_family": list(SUPPORTED_COMMAND_SUCCESS_SCOPE),
                "unsupported_scope_values": [
                    value for value in _scope_values(request) if value not in SUPPORTED_COMMAND_SUCCESS_SCOPE
                ],
            },
            "command_success_checks": checks,
            "command_success_statement": statement,
            "command_success_non_meaning": _non_meaning(),
            "additional_basis_required": {
                "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "missing_or_unclear_basis": _json_safe(request.get("additional_basis_context", [])) if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS else [],
                "basis_not_scheduled": True,
                "basis_not_authorized": True,
                "basis_not_executed": True,
                "source_created": False,
                "authority_created": False,
                "currentness_created": False,
                "final_completion_claimed": False,
                "follow_on_work_authorized": False,
            },
            "not_recorded_basis": {
                "not_recorded": outcome == OUTCOME_NOT_RECORDED,
                "not_recorded_reason": _json_safe(request.get("not_recorded_basis")) if outcome == OUTCOME_NOT_RECORDED else None,
                "prior_artifacts_mutated": False,
                "prior_artifacts_repaired": False,
                "next_work_authorized": False,
                "source_created": False,
                "authority_created": False,
                "currentness_created": False,
                "final_completion_claimed": False,
                "public_readiness_created": False,
                "deployment_readiness_created": False,
                "operation_permission_created": False,
                "follow_on_work_authorized": False,
            },
            "what_remains_open": _what_remains_open(),
            "non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
            "outcome": outcome,
            "block": {
                "blocked": block_code is not None,
                "block_code": block_code,
                "block_reason": _json_safe(request.get("block_reason", block_code)),
            },
        }
    )
    result["portable_source_body_verification_command_success_summary"] = (
        build_portable_source_body_verification_command_success_summary(result)
    )
    return _json_safe(result)


def resolve_portable_source_body_verification_command_success_from_path(
    declared_command_success_request_path: Path | str,
) -> dict:
    """Resolve from an explicit JSON object request path."""

    path = Path(declared_command_success_request_path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PortableSourceBodyVerificationCommandSuccessError(
            f"Declared command success request unreadable: {path}"
        ) from exc
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PortableSourceBodyVerificationCommandSuccessError(
            f"Declared command success request malformed JSON: {path}"
        ) from exc
    if not isinstance(parsed, Mapping):
        raise PortableSourceBodyVerificationCommandSuccessError(
            "Declared command success request path must contain a JSON object."
        )
    return resolve_portable_source_body_verification_command_success(parsed)


def _section(result: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = result.get(key)
    return value if isinstance(value, Mapping) else {}


def build_portable_source_body_verification_command_success_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the public bounded summary surface."""

    metadata = _section(result, "portable_source_body_verification_command_success_metadata")
    question = _section(result, "declared_command_success_question")
    statement = _section(result, "command_success_statement")
    non_claims = _section(result, "non_claims")
    block = _section(result, "block")
    checks = result.get("command_success_checks", [])
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": metadata.get("command_success_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "command_success_recorded": statement.get("command_success_recorded", False),
        "bounded_command_success_recorded": statement.get("bounded_command_success_recorded", False),
        "command_success_boundary_v3_basis_preserved": statement.get("command_success_boundary_v3_basis_preserved", False),
        "command_success_boundary_v1_predecessor_failure_preserved": statement.get("command_success_boundary_v1_predecessor_failure_preserved", False),
        "command_success_boundary_v2_predecessor_failure_preserved": statement.get("command_success_boundary_v2_predecessor_failure_preserved", False),
        "command_result_v2_basis_preserved": statement.get("command_result_v2_basis_preserved", False),
        "bounded_command_result_preserved": statement.get("bounded_command_result_preserved", False),
        "command_output_report_artifact_basis_preserved": statement.get("command_output_report_artifact_basis_preserved", False),
        "bounded_command_output_report_artifact_preserved": statement.get("bounded_command_output_report_artifact_preserved", False),
        "report_body_absent_or_bounded": statement.get("report_body_absent_or_bounded", False),
        "result_body_absent_or_bounded": statement.get("result_body_absent_or_bounded", False),
        "success_body_absent_or_bounded": statement.get("success_body_absent_or_bounded", False),
        "report_body_not_invented": statement.get("report_body_not_invented", False),
        "result_body_not_invented": statement.get("result_body_not_invented", False),
        "success_body_not_invented": statement.get("success_body_not_invented", False),
        "source_not_created": statement.get("source_not_created", False),
        "authority_not_created": statement.get("authority_not_created", False),
        "currentness_not_created": statement.get("currentness_not_created", False),
        "final_completion_not_created": statement.get("final_completion_not_created", False),
        "public_readiness_not_created": statement.get("public_readiness_not_created", False),
        "deployment_readiness_not_created": statement.get("deployment_readiness_not_created", False),
        "operation_permission_not_created": statement.get("operation_permission_not_created", False),
        "continuation_not_authorized": statement.get("continuation_not_authorized", False),
        "reusable_permission_not_created": statement.get("reusable_permission_not_created", False),
        "derivative_reception_not_authorized": statement.get("derivative_reception_not_authorized", False),
        "vessel_relation_not_authorized": statement.get("vessel_relation_not_authorized", False),
        "another_reception_request_not_authorized": statement.get("another_reception_request_not_authorized", False),
        "follow_on_work_not_authorized": statement.get("follow_on_work_not_authorized", False),
        "source_inference_blocked": statement.get("source_inference_blocked", False),
        "authority_inference_blocked": statement.get("authority_inference_blocked", False),
        "currentness_inference_blocked": statement.get("currentness_inference_blocked", False),
        "final_completion_inference_blocked": statement.get("final_completion_inference_blocked", False),
        "public_readiness_inference_blocked": statement.get("public_readiness_inference_blocked", False),
        "deployment_readiness_inference_blocked": statement.get("deployment_readiness_inference_blocked", False),
        "operation_permission_inference_blocked": statement.get("operation_permission_inference_blocked", False),
        "follow_on_work_inference_blocked": statement.get("follow_on_work_inference_blocked", False),
        "unbounded_pass_fail_inference_blocked": statement.get("unbounded_pass_fail_inference_blocked", False),
        "selected_command_success_boundary_v3_outcome": _section(result, "selected_command_success_boundary_v3_basis").get("outcome"),
        "selected_command_success_boundary_v3_version": _section(result, "selected_command_success_boundary_v3_basis").get("result_version"),
        "selected_command_success_boundary_v3_failed_check_count": _section(result, "selected_command_success_boundary_v3_basis").get("failed_check_count"),
        "selected_command_result_v2_outcome": _section(result, "selected_command_result_v2_basis").get("outcome"),
        "selected_command_result_v2_version": _section(result, "selected_command_result_v2_basis").get("result_version"),
        "selected_command_result_v2_failed_check_count": _section(result, "selected_command_result_v2_basis").get("failed_check_count"),
        "selected_output_capture_v2_outcome": _section(result, "selected_output_capture_v2_basis").get("outcome"),
        "selected_output_capture_v2_version": _section(result, "selected_output_capture_v2_basis").get("result_version"),
        "selected_output_capture_v2_failed_check_count": _section(result, "selected_output_capture_v2_basis").get("failed_check_count"),
        "selected_command_output_report_artifact_outcome": _section(result, "selected_command_output_report_artifact_basis").get("outcome"),
        "selected_command_output_report_artifact_failed_check_count": _section(result, "selected_command_output_report_artifact_basis").get("failed_check_count"),
        "selected_post_invocation_execution_outcome": _section(result, "selected_post_invocation_command_execution_basis").get("outcome"),
        "selected_post_invocation_execution_failed_check_count": _section(result, "selected_post_invocation_command_execution_basis").get("failed_check_count"),
        "command_success_not_source_authority_currentness_final_completion_readiness_permission_follow_on": not any(non_claims.get(key, True) for key in ("command_success_treated_as_source", "command_success_treated_as_authority", "command_success_treated_as_currentness", "command_success_treated_as_final_completion", "command_success_treated_as_public_readiness", "command_success_treated_as_deployment_readiness", "command_success_treated_as_operation_permission", "command_success_treated_as_follow_on_work")),
        "command_result_v2_not_success_source_authority_currentness_final_completion_readiness": not any(non_claims.get(key, True) for key in ("command_result_treated_as_success", "command_result_treated_as_source", "command_result_treated_as_authority", "command_result_treated_as_currentness", "command_result_treated_as_final_completion", "command_result_treated_as_public_readiness", "command_result_treated_as_deployment_readiness")),
        "output_capture_not_result_success_source_authority_currentness_final_completion": not any(non_claims.get(key, True) for key in ("output_capture_treated_as_result", "output_capture_treated_as_success", "output_capture_treated_as_source", "output_capture_treated_as_authority", "output_capture_treated_as_currentness", "output_capture_treated_as_final_completion")),
        "execution_trace_not_success_source_authority_currentness_final_completion": not any(non_claims.get(key, True) for key in ("execution_trace_treated_as_success", "execution_trace_treated_as_source", "execution_trace_treated_as_authority", "execution_trace_treated_as_currentness", "execution_trace_treated_as_final_completion")),
        "command_report_lineage_not_current_report_artifact_result_authority_success_source_authority_currentness": True,
        "raw_full_prior_artifact_body_not_returned": statement.get("raw_full_prior_artifact_body_not_returned", False),
        "artifacts_not_mutated": non_claims.get("prior_artifacts_mutated") is False,
        "deployment_runtime_public_release_not_created": non_claims.get("deployment_created") is False and non_claims.get("runtime_hosting_created") is False and non_claims.get("public_release_created") is False,
        "continuation_publication_reusable_follow_on_not_authorized": non_claims.get("continuation_authorized") is False and non_claims.get("publication_flow_opened") is False and non_claims.get("reusable_permission_created") is False and non_claims.get("follow_on_work_authorized") is False,
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


def write_portable_source_body_verification_command_success_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a stable UTF-8 JSON result without overwriting prior artifacts."""

    metadata = _section(result, "portable_source_body_verification_command_success_metadata")
    request_id = _safe_text(metadata.get("command_success_request_id", "portable_source_body_verification_command_success_request"))
    if output_path is None:
        output_path = OUTPUT_ROOT / f"{request_id}__portable_source_body_verification_command_success_result.json"
    path = _unique_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(dict(result)), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _basis_stub(label: str, **overrides: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "reference_shaped": True,
        "full_prior_artifact_body_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(overrides)
    return basis


def _posture_stub(label: str) -> dict[str, Any]:
    return {
        "posture_label": label,
        "declared": True,
        "command_success_posture_only": True,
        "source_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "public_readiness_created": False,
        "deployment_readiness_created": False,
        "operation_permission_created": False,
        "follow_on_work_authorized": False,
    }


def build_declared_portable_source_body_verification_command_success_request(
    command_success_request_id: str = "portable_source_body_verification_command_success_reference_review_001",
    command_success_intent: str = INTENT_RECORD,
    selected_command_success_boundary_v3_result_path: Path | str | None = None,
    selected_command_result_v2_result_path: Path | str | None = None,
    selected_output_capture_v2_result_path: Path | str | None = None,
) -> dict[str, Any]:
    """Build a reference-shaped declared request with required non-claims false."""

    request: dict[str, Any] = {
        "command_success_request_id": command_success_request_id,
        "command_success_question": CORE_QUESTION,
        "command_success_intent": command_success_intent,
        "command_success_scope": list(SUPPORTED_COMMAND_SUCCESS_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    request["selected_command_success_boundary_v3_basis"] = _basis_stub(
        "selected_command_success_boundary_v3_basis",
        path=_safe_text(selected_command_success_boundary_v3_result_path) if selected_command_success_boundary_v3_result_path else None,
        outcome=BOUNDARY_V3_RECORDED,
        result_version="0.3.0",
        failed_check_count=0,
        predecessor_chain=["resolve_portable_source_body_verification_command_success_boundary", "resolve_portable_source_body_verification_command_success_boundary_v2"],
        v1_predecessor_failure_preserved=True,
        v2_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_repaired=False,
        v2_hidden=False,
        v2_claimed_passed=False,
        v3_command_success_boundary_erased_v1=False,
        v3_command_success_boundary_erased_v2=False,
        one_future_command_success_step_declared=True,
        selected_basis_reference_shape_preserved=True,
        raw_full_prior_artifact_body_returned=False,
        summary_surface_conformance_preserved=True,
        command_success_created=False,
        command_success_still_not_created=True,
        success_body_invented=False,
        success_body_not_invented=True,
        success_inference_made=False,
        currentness_inference_made=False,
        final_completion_inference_made=False,
        public_readiness_inference_made=False,
        deployment_readiness_inference_made=False,
        authority_inference_made=False,
        follow_on_work_inference_made=False,
        unbounded_pass_fail_inference_made=False,
    )
    request["selected_command_result_v2_basis"] = _basis_stub(
        "selected_command_result_v2_basis",
        path=_safe_text(selected_command_result_v2_result_path) if selected_command_result_v2_result_path else None,
        outcome=COMMAND_RESULT_V2_RECORDED,
        result_version="0.2.0",
        failed_check_count=0,
        bounded_command_result_recorded=True,
        command_success_created=False,
        command_result_treated_as_success=False,
        command_result_treated_as_source=False,
        command_result_treated_as_authority=False,
        command_result_treated_as_currentness=False,
        command_result_treated_as_final_completion=False,
        command_result_treated_as_public_readiness=False,
        command_result_treated_as_deployment_readiness=False,
    )
    request["selected_command_output_report_artifact_basis"] = _basis_stub(
        "selected_command_output_report_artifact_basis",
        outcome=OUTPUT_REPORT_ARTIFACT_RECORDED,
        failed_check_count=0,
        bounded_command_output_report_artifact_recorded=True,
        report_body_absent_or_bounded=True,
        report_body_not_invented=True,
        command_output_report_artifact_treated_as_result_authority=False,
        command_output_report_artifact_treated_as_success=False,
    )
    request["selected_output_capture_v2_basis"] = _basis_stub(
        "selected_output_capture_v2_basis",
        path=_safe_text(selected_output_capture_v2_result_path) if selected_output_capture_v2_result_path else None,
        outcome=OUTPUT_CAPTURE_V2_RECORDED,
        result_version="0.2.0",
        failed_check_count=0,
        json_safe_result=True,
        v1_predecessor_failure_preserved=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_output_capture_erased_v1=False,
        stdout_content_invented=False,
        stderr_content_invented=False,
        process_output_content_invented=False,
        raw_output_body_content_invented=False,
    )
    request["selected_post_invocation_command_execution_basis"] = _basis_stub(
        "selected_post_invocation_command_execution_basis",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED",
        failed_check_count=0,
        bounded_command_execution_event_recorded=True,
        execution_trace_audit_only=True,
    )
    request["selected_command_report_lineage_basis"] = _basis_stub(
        "selected_command_report_lineage_basis",
        command_report_lineage_basis_treated_as_current_report_artifact=False,
        command_report_lineage_basis_treated_as_command_result_authority=False,
        command_report_lineage_basis_treated_as_command_success=False,
        command_report_lineage_basis_treated_as_source=False,
        command_report_lineage_basis_treated_as_authority=False,
        command_report_lineage_basis_treated_as_currentness=False,
    )
    for key in SELECTED_BASIS_KEYS:
        request.setdefault(key, _basis_stub(key))
    for key in POSTURE_KEYS:
        request[key] = _posture_stub(key)
    return request
