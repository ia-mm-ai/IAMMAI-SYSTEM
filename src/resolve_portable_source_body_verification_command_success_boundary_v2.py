"""Resolve command-success-boundary v2 without returning raw prior bodies.

This resolver is an additive successor to
``resolve_portable_source_body_verification_command_success_boundary``. The
v1 resolver remains visible predecessor conformance-failure evidence because it
returned raw full-body sentinel material. This v2 resolver preserves the same
command-success-boundary law while forcing all selected basis material returned
in results into a sanitized, reference-shaped form.

It records one future command-success-step boundary only. It does not create
command success, success body, source, authority, currentness, final completion,
public readiness, deployment readiness, continuation, reusable permission,
derivative reception, vessel relation, another reception request, or follow-on
work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class PortableSourceBodyVerificationCommandSuccessBoundaryV2Error(Exception):
    """Raised for explicit unreadable or contradictory v2 boundary input."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_success_boundary_v2"
SUCCESSOR_OF = "resolve_portable_source_body_verification_command_success_boundary"
SUCCESSOR_REASON = (
    "v2 preserves the v1 command-success-boundary resolver as predecessor "
    "conformance-failure evidence and corrects the v1 raw full-body return "
    "containment failure involving the RAW command-success-boundary body "
    "sentinel marked MUST NOT RETURN."
)
RESULT_VERSION = "0.2.0"
RESULT_TYPE = "portable_source_body_verification_command_success_boundary_result"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_success_boundary_v2"
)

CORE_QUESTION = (
    "Can the recorded command result v2 basis be bounded for one future command "
    "success step without creating command success, success body, source, "
    "authority, currentness, final completion, public readiness, deployment "
    "readiness, continuation, reusable permission, derivative reception, vessel "
    "relation, another reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

COMMAND_RESULT_V2_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
COMMAND_RESULT_V2_VERSION = "0.2.0"
COMMAND_RESULT_V2_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_command_result_v2"
)
COMMAND_RESULT_V2_SUCCESSOR_OF = "resolve_portable_source_body_verification_command_result"
COMMAND_RESULT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_RECORDED"
)
COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)
COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_RECORDED"
)
OUTPUT_CAPTURE_V2_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
OUTPUT_CAPTURE_V2_VERSION = "0.2.0"
OUTPUT_CAPTURE_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_BOUNDARY_RECORDED"
)
COMMAND_OUTPUT_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_RECORDED"
COMMAND_OUTPUT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_RECORDED"
)
COMMAND_OUTPUT_CONTAINMENT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_RECORDED"
)
POST_INVOCATION_COMMAND_EXECUTION_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
)
COMMAND_INVOCATION_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_RECORDED"
COMMAND_EXECUTION_REVIEW_OUTCOME = (
    "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_RECORDED"
)
REQUEST_CONSUMPTION_OUTCOME = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
V2_ADMITTED_REQUEST_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
V2_ADMITTED_REQUEST_VERSION = "0.2.0"

SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE = frozenset(
    {
        "COMMAND_SUCCESS_BOUNDARY_ONLY",
        "ONE_FUTURE_COMMAND_SUCCESS_STEP_ONLY",
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
        "REPORT_BODY_NOT_INVENTED",
        "RESULT_BODY_NOT_INVENTED",
        "SUCCESS_BODY_NOT_INVENTED",
        "COMMAND_SUCCESS_NOT_CREATED",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_SUCCESS",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_SOURCE",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_AUTHORITY",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_CURRENTNESS",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_FINAL_COMPLETION",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_PUBLIC_READINESS",
        "COMMAND_SUCCESS_BOUNDARY_IS_NOT_DEPLOYMENT_READINESS",
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
        "NO_SUCCESS_INFERENCE",
        "NO_CURRENTNESS_INFERENCE",
        "NO_FINAL_COMPLETION_INFERENCE",
        "NO_PUBLIC_READINESS_INFERENCE",
        "NO_DEPLOYMENT_READINESS_INFERENCE",
        "NO_AUTHORITY_INFERENCE",
        "NO_FOLLOW_ON_WORK_INFERENCE",
        "NO_UNBOUNDED_PASS_FAIL_INFERENCE",
        "COMMAND_SUCCESS_NOT_AUTHORITY",
        "COMMAND_SUCCESS_NOT_CURRENTNESS",
        "COMMAND_SUCCESS_NOT_FINAL_COMPLETION",
        "COMMAND_SUCCESS_NOT_PUBLIC_READINESS",
        "COMMAND_SUCCESS_NOT_DEPLOYMENT_READINESS",
        "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
        "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
        "CONSUMED_REQUEST_NOT_REOPENED",
        "NO_AUTHORITY_CREATED",
        "NO_CURRENTNESS_CREATED",
        "NO_FINAL_COMPLETION",
        "NO_PUBLIC_READINESS_CREATED",
        "NO_DEPLOYMENT_READINESS_CREATED",
        "NO_OPERATION_PERMISSION_CREATED",
        "NO_CONTINUATION_AUTHORIZED",
        "NO_REUSABLE_PERMISSION",
        "NO_FOLLOW_ON_WORK_AUTHORIZED",
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
        "REFERENCE_SHAPED_BASIS_REQUIRED",
        "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
    }
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_success_created",
    "success_body_invented",
    "success_inference_made",
    "currentness_inference_made",
    "final_completion_inference_made",
    "public_readiness_inference_made",
    "deployment_readiness_inference_made",
    "authority_inference_made",
    "follow_on_work_inference_made",
    "unbounded_pass_fail_inference_made",
    "command_success_boundary_treated_as_success",
    "command_success_boundary_treated_as_source",
    "command_success_boundary_treated_as_authority",
    "command_success_boundary_treated_as_currentness",
    "command_success_boundary_treated_as_final_completion",
    "command_success_boundary_treated_as_public_readiness",
    "command_success_boundary_treated_as_deployment_readiness",
    "command_result_treated_as_success",
    "command_result_treated_as_source",
    "command_result_treated_as_authority",
    "command_result_treated_as_currentness",
    "command_result_treated_as_final_completion",
    "command_result_treated_as_public_readiness",
    "command_result_treated_as_deployment_readiness",
    "command_output_report_artifact_treated_as_result_authority",
    "command_output_report_artifact_treated_as_success",
    "command_output_report_artifact_treated_as_source",
    "command_output_report_artifact_treated_as_authority",
    "command_output_report_artifact_treated_as_currentness",
    "command_output_report_artifact_treated_as_final_completion",
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
    "command_success_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "authorization_token_reused",
    "consumed_request_reopened",
    "full_prior_artifacts_embedded",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "v1_command_result_repaired",
    "v1_command_result_hidden",
    "v1_command_result_claimed_passed",
    "v2_command_result_erased_v1",
    "v1_output_capture_repaired",
    "v1_output_capture_hidden",
    "v1_output_capture_claimed_passed",
    "v2_output_capture_erased_v1",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
    "operation_permission_created",
    "public_launch_readiness_created",
    "deployment_readiness_created",
    "final_completion_claimed",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "command_success_boundary_recorded",
    "one_future_command_success_step_declared",
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
    "report_body_not_invented",
    "result_body_not_invented",
    "success_body_not_invented",
    "command_success_still_not_created",
    "success_inference_blocked",
    "currentness_inference_blocked",
    "final_completion_inference_blocked",
    "public_readiness_inference_blocked",
    "deployment_readiness_inference_blocked",
    "authority_inference_blocked",
    "follow_on_work_inference_blocked",
    "unbounded_pass_fail_inference_blocked",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "v1_request_admission_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

SELECTED_BASIS_KEYS = (
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
    "command_success_boundary_only_posture",
    "one_future_command_success_step_posture",
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
    "no_report_body_invented_posture",
    "no_result_body_invented_posture",
    "no_success_body_invented_posture",
    "no_command_success_posture",
    "no_success_inference_posture",
    "no_currentness_inference_posture",
    "no_final_completion_inference_posture",
    "no_public_readiness_inference_posture",
    "no_deployment_readiness_inference_posture",
    "no_authority_inference_posture",
    "no_follow_on_work_inference_posture",
    "no_unbounded_pass_fail_inference_posture",
    "no_success_as_currentness_posture",
    "no_success_as_final_completion_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
)

RAW_BODY_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "body",
        "artifact_body",
        "full_prior_artifact_body",
        "raw_prior_artifact_body",
        "raw_full_prior_artifact_body",
        "raw_command_success_boundary_body",
        "raw_command_result_body",
        "raw_result_body",
        "raw_report_body",
        "raw_output_body",
        "prior_artifact_body",
        "embedded_prior_artifact",
        "embedded_prior_artifacts",
        "raw_artifact_body",
        "stdout",
        "stderr",
        "process_output",
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
        "output_body",
        "source_body_content",
    }
)

SAFE_RAW_FIELD_NAMES = frozenset(
    {
        "raw_full_prior_artifact_body_returned",
        "raw_output_body_content_invented",
        "no_raw_full_prior_artifact_body",
    }
)

BASIS_BLOCK_CODES = {
    "selected_command_result_v2_basis": "COMMAND_RESULT_V2_BASIS_MISSING",
    "selected_command_result_v2_terminal_summary_basis": "COMMAND_RESULT_V2_BASIS_MISSING",
    "selected_command_result_v1_predecessor_failure_basis": (
        "COMMAND_RESULT_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING"
    ),
    "selected_command_result_boundary_basis": "COMMAND_RESULT_BOUNDARY_BASIS_MISSING",
    "selected_command_result_boundary_terminal_summary_basis": (
        "COMMAND_RESULT_BOUNDARY_BASIS_MISSING"
    ),
    "selected_command_output_report_artifact_basis": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"
    ),
    "selected_command_output_report_artifact_terminal_summary_basis": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"
    ),
    "selected_command_output_report_artifact_boundary_basis": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"
    ),
    "selected_command_output_report_artifact_boundary_terminal_summary_basis": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING"
    ),
    "selected_output_capture_v2_basis": "OUTPUT_CAPTURE_V2_BASIS_MISSING",
    "selected_output_capture_v2_terminal_summary_basis": "OUTPUT_CAPTURE_V2_BASIS_MISSING",
    "selected_output_capture_v1_predecessor_failure_basis": (
        "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING"
    ),
    "selected_output_capture_boundary_basis": "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING",
    "selected_command_output_basis": "COMMAND_OUTPUT_BASIS_MISSING",
    "selected_command_output_boundary_basis": "COMMAND_OUTPUT_BASIS_MISSING",
    "selected_command_output_containment_basis": "COMMAND_OUTPUT_BASIS_MISSING",
    "selected_post_invocation_command_execution_basis": (
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"
    ),
    "selected_post_invocation_command_execution_terminal_summary_basis": (
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING"
    ),
    "selected_command_invocation_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
    "selected_command_execution_review_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
    "selected_request_consumption_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
    "selected_consumed_request_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
    "selected_v2_admitted_request_basis": "V2_ADMITTED_REQUEST_BASIS_MISSING",
    "selected_v1_predecessor_failure_basis": "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    "selected_older_command_execution_boundary_lineage_basis": (
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_MISSING"
    ),
    "selected_command_report_lineage_basis": "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
    "selected_command_implementation_boundary_basis": (
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"
    ),
    "selected_command_boundary_basis": "COMMAND_BOUNDARY_BASIS_MISSING",
    "selected_artifact_emission_containment_basis": (
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"
    ),
    "selected_evidence_manifest_basis": "EVIDENCE_MANIFEST_BASIS_MISSING",
    "selected_portable_verification_basis": "PORTABLE_VERIFICATION_BASIS_MISSING",
}

POSTURE_BLOCK_CODES = {
    "command_success_boundary_only_posture": "COMMAND_SUCCESS_BOUNDARY_ONLY_POSTURE_MISSING",
    "one_future_command_success_step_posture": "ONE_FUTURE_COMMAND_SUCCESS_STEP_POSTURE_MISSING",
    "command_result_v2_basis_preserved_posture": (
        "COMMAND_RESULT_V2_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "bounded_command_result_preserved_posture": (
        "BOUNDED_COMMAND_RESULT_PRESERVED_POSTURE_MISSING"
    ),
    "command_result_v1_predecessor_failure_preserved_posture": (
        "COMMAND_RESULT_V1_PREDECESSOR_FAILURE_PRESERVED_POSTURE_MISSING"
    ),
    "command_result_boundary_basis_preserved_posture": (
        "COMMAND_RESULT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "command_output_report_artifact_basis_preserved_posture": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "bounded_command_output_report_artifact_preserved_posture": (
        "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING"
    ),
    "command_output_report_artifact_boundary_basis_preserved_posture": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "output_capture_v2_basis_preserved_posture": (
        "OUTPUT_CAPTURE_V2_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "output_capture_v1_predecessor_failure_preserved_posture": (
        "OUTPUT_CAPTURE_V1_PREDECESSOR_FAILURE_PRESERVED_POSTURE_MISSING"
    ),
    "bounded_output_capture_event_preserved_posture": (
        "BOUNDED_OUTPUT_CAPTURE_EVENT_PRESERVED_POSTURE_MISSING"
    ),
    "command_output_basis_preserved_posture": "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
    "execution_trace_audit_only_posture": "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
    "report_body_absent_or_bounded_posture": "REPORT_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
    "result_body_absent_or_bounded_posture": "RESULT_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
    "no_report_body_invented_posture": "NO_REPORT_BODY_INVENTED_POSTURE_MISSING",
    "no_result_body_invented_posture": "NO_RESULT_BODY_INVENTED_POSTURE_MISSING",
    "no_success_body_invented_posture": "NO_SUCCESS_BODY_INVENTED_POSTURE_MISSING",
    "no_command_success_posture": "NO_COMMAND_SUCCESS_POSTURE_MISSING",
    "no_success_inference_posture": "NO_SUCCESS_INFERENCE_POSTURE_MISSING",
    "no_currentness_inference_posture": "NO_CURRENTNESS_INFERENCE_POSTURE_MISSING",
    "no_final_completion_inference_posture": "NO_FINAL_COMPLETION_INFERENCE_POSTURE_MISSING",
    "no_public_readiness_inference_posture": "NO_PUBLIC_READINESS_INFERENCE_POSTURE_MISSING",
    "no_deployment_readiness_inference_posture": (
        "NO_DEPLOYMENT_READINESS_INFERENCE_POSTURE_MISSING"
    ),
    "no_authority_inference_posture": "NO_AUTHORITY_INFERENCE_POSTURE_MISSING",
    "no_follow_on_work_inference_posture": "NO_FOLLOW_ON_WORK_INFERENCE_POSTURE_MISSING",
    "no_unbounded_pass_fail_inference_posture": "NO_UNBOUNDED_PASS_FAIL_INFERENCE_POSTURE_MISSING",
    "no_success_as_currentness_posture": "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
    "no_success_as_final_completion_posture": "NO_SUCCESS_AS_FINAL_COMPLETION_POSTURE_MISSING",
    "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
    "authorization_token_reuse_blocked_posture": "AUTHORIZATION_TOKEN_REUSED",
    "consumed_token_closed_posture": "CONSUMED_REQUEST_REOPENED",
    "no_reopen_consumed_request_posture": "CONSUMED_REQUEST_REOPENED",
    "returned_result_containment_posture": "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
}

EXPLICIT_BLOCK_CODES = (
    "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_UNREADABLE",
    "COMMAND_SUCCESS_BOUNDARY_QUESTION_UNDECLARED",
    "COMMAND_SUCCESS_BOUNDARY_INTENT_UNSUPPORTED",
    "COMMAND_SUCCESS_BOUNDARY_BLOCK_INTENT_REQUESTED",
    "COMMAND_RESULT_V2_NOT_RECORDED",
    "COMMAND_RESULT_V2_FAILED_CHECKS_PRESENT",
    "COMMAND_RESULT_V2_VERSION_NOT_0_2_0",
    "COMMAND_RESULT_V2_SUCCESSOR_METADATA_MISSING",
    "COMMAND_RESULT_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING",
    "COMMAND_RESULT_V2_REPAIRED_V1",
    "COMMAND_RESULT_V2_HID_V1",
    "COMMAND_RESULT_V2_CLAIMED_V1_PASSED",
    "COMMAND_RESULT_V2_ERASED_V1",
    "COMMAND_RESULT_V2_NOT_BOUNDED",
    "COMMAND_RESULT_V2_ALREADY_CREATED_SUCCESS",
    "COMMAND_RESULT_V2_INFERRED_SUCCESS",
    "COMMAND_RESULT_V2_INFERRED_CURRENTNESS",
    "COMMAND_RESULT_V2_INFERRED_FINAL_COMPLETION",
    "COMMAND_RESULT_V2_INFERRED_PUBLIC_READINESS",
    "COMMAND_RESULT_V2_INFERRED_DEPLOYMENT_READINESS",
    "COMMAND_RESULT_V2_INFERRED_AUTHORITY",
    "COMMAND_RESULT_V2_INFERRED_FOLLOW_ON_WORK",
    "COMMAND_RESULT_V2_INFERRED_UNBOUNDED_PASS_FAIL",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_SUCCESS",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_SOURCE",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_AUTHORITY",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_CURRENTNESS",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_FINAL_COMPLETION",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_PUBLIC_READINESS",
    "COMMAND_RESULT_V2_TREATED_RESULT_AS_DEPLOYMENT_READINESS",
    "COMMAND_RESULT_BOUNDARY_NOT_RECORDED",
    "COMMAND_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "COMMAND_RESULT_BOUNDARY_ALREADY_CREATED_SUCCESS",
    "COMMAND_RESULT_BOUNDARY_STEP_NOT_DECLARED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_SUCCESS",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT_AUTHORITY",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SOURCE",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_AUTHORITY",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_CURRENTNESS",
    "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_FINAL_COMPLETION",
    "OUTPUT_CAPTURE_TREATED_AS_RESULT",
    "OUTPUT_CAPTURE_TREATED_AS_SUCCESS",
    "OUTPUT_CAPTURE_TREATED_AS_SOURCE",
    "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY",
    "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
    "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
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
    "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
    "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
    "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_SUCCESS",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_SOURCE",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_AUTHORITY",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_CURRENTNESS",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_PUBLIC_READINESS",
    "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_DEPLOYMENT_READINESS",
    "SUCCESS_BODY_INVENTED",
    "RESULT_BODY_INVENTED",
    "REPORT_BODY_INVENTED",
    "COMMAND_SUCCESS_CREATED",
    "SUCCESS_INFERENCE_MADE",
    "CURRENTNESS_INFERENCE_MADE",
    "FINAL_COMPLETION_INFERENCE_MADE",
    "PUBLIC_READINESS_INFERENCE_MADE",
    "DEPLOYMENT_READINESS_INFERENCE_MADE",
    "AUTHORITY_INFERENCE_MADE",
    "FOLLOW_ON_WORK_INFERENCE_MADE",
    "UNBOUNDED_PASS_FAIL_INFERENCE_MADE",
    "EXECUTION_TRACE_TREATED_AS_SUCCESS",
    "EXECUTION_TRACE_TREATED_AS_SOURCE",
    "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
    "EXECUTION_TRACE_TREATED_AS_CURRENTNESS",
    "EXECUTION_TRACE_TREATED_AS_FINAL_COMPLETION",
    "COMMAND_SUCCESS_TREATED_AS_AUTHORITY",
    "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
    "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS",
    "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
    "V2_TREATED_AS_REPAIRING_V1_REQUEST_ADMISSION",
    "V1_REQUEST_ADMISSION_FAILURE_HIDDEN",
    "V1_REQUEST_ADMISSION_CLAIMED_PASSED",
    "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_BASIS_MISSING",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_SUCCESS",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_SOURCE",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_AUTHORITY",
    "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENTNESS",
    "UNSUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "ARTIFACTS_MUTATED",
    "DEPLOYMENT_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_CREATED",
    "PUBLIC_READINESS_CREATED",
    "DEPLOYMENT_READINESS_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "CONTINUATION_AUTHORIZED",
    "REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "MUTATION_REPLAY_OR_MERGE_DETECTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
)

BLOCK_CODES = frozenset(
    EXPLICIT_BLOCK_CODES
    + tuple(BASIS_BLOCK_CODES.values())
    + tuple(POSTURE_BLOCK_CODES.values())
)

OPEN_ITEMS = (
    "command success boundary test",
    "command success boundary live artifact",
    "command success step, if separately specified",
    "command success",
    "success body",
    "success verdict",
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
    "public readiness",
    "deployment readiness",
    "final completion",
    "continuation",
    "publication flow",
    "reusable permission",
    "successor reception request",
    "follow-on work",
)

COLLAPSE_CHECKS = (
    ("command success boundary not success", ("command_success_boundary_treated_as_success",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_SUCCESS"),
    ("command success boundary not source", ("command_success_boundary_treated_as_source",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_SOURCE"),
    ("command success boundary not authority", ("command_success_boundary_treated_as_authority",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_AUTHORITY"),
    ("command success boundary not currentness", ("command_success_boundary_treated_as_currentness",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_CURRENTNESS"),
    ("command success boundary not final completion", ("command_success_boundary_treated_as_final_completion",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_FINAL_COMPLETION"),
    ("command success boundary not public readiness", ("command_success_boundary_treated_as_public_readiness",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_PUBLIC_READINESS"),
    ("command success boundary not deployment readiness", ("command_success_boundary_treated_as_deployment_readiness",), "COMMAND_SUCCESS_BOUNDARY_TREATED_AS_DEPLOYMENT_READINESS"),
    ("command result v2 not success", ("command_result_treated_as_success", "command_result_v2_treated_result_as_success"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_SUCCESS"),
    ("command result v2 not source", ("command_result_treated_as_source", "command_result_v2_treated_result_as_source"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_SOURCE"),
    ("command result v2 not authority", ("command_result_treated_as_authority", "command_result_became_authority", "command_result_v2_treated_result_as_authority"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_AUTHORITY"),
    ("command result v2 not currentness", ("command_result_treated_as_currentness", "command_result_v2_treated_result_as_currentness"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_CURRENTNESS"),
    ("command result v2 not final completion", ("command_result_treated_as_final_completion", "command_result_v2_treated_result_as_final_completion"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_FINAL_COMPLETION"),
    ("command result v2 not public readiness", ("command_result_treated_as_public_readiness", "command_result_v2_treated_result_as_public_readiness"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_PUBLIC_READINESS"),
    ("command result v2 not deployment readiness", ("command_result_treated_as_deployment_readiness", "command_result_v2_treated_result_as_deployment_readiness"), "COMMAND_RESULT_V2_TREATED_RESULT_AS_DEPLOYMENT_READINESS"),
    ("command output/report artifact not result authority", ("command_output_report_artifact_treated_as_result_authority",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT_AUTHORITY"),
    ("command output/report artifact not success", ("command_output_report_artifact_treated_as_success",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS"),
    ("command output/report artifact not source", ("command_output_report_artifact_treated_as_source",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SOURCE"),
    ("command output/report artifact not authority", ("command_output_report_artifact_treated_as_authority",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_AUTHORITY"),
    ("command output/report artifact not currentness", ("command_output_report_artifact_treated_as_currentness",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_CURRENTNESS"),
    ("command output/report artifact not final completion", ("command_output_report_artifact_treated_as_final_completion",), "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_FINAL_COMPLETION"),
    ("output capture not result", ("output_capture_treated_as_result",), "OUTPUT_CAPTURE_TREATED_AS_RESULT"),
    ("output capture not success", ("output_capture_treated_as_success",), "OUTPUT_CAPTURE_TREATED_AS_SUCCESS"),
    ("output capture not source", ("output_capture_treated_as_source",), "OUTPUT_CAPTURE_TREATED_AS_SOURCE"),
    ("output capture not authority", ("output_capture_treated_as_authority",), "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY"),
    ("output capture not currentness", ("output_capture_treated_as_currentness",), "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS"),
    ("output capture not final completion", ("output_capture_treated_as_final_completion",), "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION"),
    ("execution trace not success", ("execution_trace_treated_as_success",), "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
    ("execution trace not source", ("execution_trace_treated_as_source",), "EXECUTION_TRACE_TREATED_AS_SOURCE"),
    ("execution trace not authority", ("execution_trace_treated_as_authority",), "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
    ("execution trace not currentness", ("execution_trace_treated_as_currentness",), "EXECUTION_TRACE_TREATED_AS_CURRENTNESS"),
    ("execution trace not final completion", ("execution_trace_treated_as_final_completion",), "EXECUTION_TRACE_TREATED_AS_FINAL_COMPLETION"),
    ("command success not authority", ("command_success_became_authority", "command_success_treated_as_authority"), "COMMAND_SUCCESS_TREATED_AS_AUTHORITY"),
    ("command success not currentness", ("command_success_created_currentness", "command_success_treated_as_currentness"), "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command success not final completion", ("command_success_claimed_final_completion", "command_success_treated_as_final_completion"), "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command success not public readiness", ("command_success_treated_as_public_readiness",), "COMMAND_SUCCESS_TREATED_AS_PUBLIC_READINESS"),
    ("command success not deployment readiness", ("command_success_treated_as_deployment_readiness",), "COMMAND_SUCCESS_TREATED_AS_DEPLOYMENT_READINESS"),
    ("success body not invented", ("success_body_invented",), "SUCCESS_BODY_INVENTED"),
    ("result body not invented", ("result_body_invented",), "RESULT_BODY_INVENTED"),
    ("report body not invented", ("report_body_invented",), "REPORT_BODY_INVENTED"),
    ("command success not created", ("command_success_created",), "COMMAND_SUCCESS_CREATED"),
    ("success inference not made", ("success_inference_made",), "SUCCESS_INFERENCE_MADE"),
    ("currentness inference not made", ("currentness_inference_made",), "CURRENTNESS_INFERENCE_MADE"),
    ("final completion inference not made", ("final_completion_inference_made",), "FINAL_COMPLETION_INFERENCE_MADE"),
    ("public readiness inference not made", ("public_readiness_inference_made",), "PUBLIC_READINESS_INFERENCE_MADE"),
    ("deployment readiness inference not made", ("deployment_readiness_inference_made",), "DEPLOYMENT_READINESS_INFERENCE_MADE"),
    ("authority inference not made", ("authority_inference_made",), "AUTHORITY_INFERENCE_MADE"),
    ("follow-on work inference not made", ("follow_on_work_inference_made",), "FOLLOW_ON_WORK_INFERENCE_MADE"),
    ("unbounded pass/fail inference not made", ("unbounded_pass_fail_inference_made", "pass_inference_made", "fail_inference_made"), "UNBOUNDED_PASS_FAIL_INFERENCE_MADE"),
    ("authorization token not reused", ("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED"),
    ("consumed request not reopened", ("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED"),
    ("command report lineage not current report artifact", ("command_report_lineage_basis_treated_as_current_report_artifact",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT"),
    ("command report lineage not command result authority", ("command_report_lineage_basis_treated_as_command_result_authority",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT_AUTHORITY"),
    ("command report lineage not command success", ("command_report_lineage_basis_treated_as_command_success",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_SUCCESS"),
    ("command report lineage not source", ("command_report_lineage_basis_treated_as_source",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_SOURCE"),
    ("command report lineage not authority", ("command_report_lineage_basis_treated_as_authority",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_AUTHORITY"),
    ("command report lineage not currentness", ("command_report_lineage_basis_treated_as_currentness",), "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENTNESS"),
    ("older execution boundary lineage not current execution", ("older_command_execution_boundary_lineage_treated_as_current_execution",), "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION"),
    ("earlier v2 did not repair v1 request admission", ("v2_treated_as_repairing_v1_request_admission",), "V2_TREATED_AS_REPAIRING_V1_REQUEST_ADMISSION"),
    ("earlier v1 request admission not hidden", ("v1_request_admission_failure_hidden",), "V1_REQUEST_ADMISSION_FAILURE_HIDDEN"),
    ("earlier v1 request admission not claimed passed", ("v1_request_admission_claimed_passed",), "V1_REQUEST_ADMISSION_CLAIMED_PASSED"),
    ("full prior artifact body not emitted", ("full_prior_artifacts_embedded", "raw_full_prior_artifact_body_returned"), "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
    ("artifacts not mutated", ("prior_artifacts_mutated",), "ARTIFACTS_MUTATED"),
    ("deployment not created", ("deployment_created",), "DEPLOYMENT_CREATED"),
    ("runtime hosting not created", ("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
    ("public release not created", ("public_release_created",), "PUBLIC_RELEASE_CREATED"),
    ("operation not created", ("operation_permission_created",), "OPERATION_CREATED"),
    ("public readiness not created", ("public_launch_readiness_created",), "PUBLIC_READINESS_CREATED"),
    ("deployment readiness not created", ("deployment_readiness_created",), "DEPLOYMENT_READINESS_CREATED"),
    ("final completion not claimed", ("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED"),
    ("continuation not authorized", ("continuation_authorized",), "CONTINUATION_AUTHORIZED"),
    ("reusable permission not created", ("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
    ("derivative reception not authorized", ("derivative_reception_authorized",), "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel relation not authorized", ("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
    ("another reception request not authorized", ("another_reception_request_authorized",), "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow-on work not authorized", ("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
    ("mutation/replay/merge not performed", ("mutation_performed", "replay_performed", "merge_performed"), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def _to_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _deep_find(value: Any, names: Iterable[str], default: Any = None) -> Any:
    wanted = set(names)
    sentinel = object()

    def walk(item: Any) -> Any:
        if isinstance(item, Mapping):
            for key, nested in item.items():
                if str(key) in wanted:
                    return nested
            for nested in item.values():
                found = walk(nested)
                if found is not sentinel:
                    return found
        elif isinstance(item, (list, tuple)):
            for nested in item:
                found = walk(nested)
                if found is not sentinel:
                    return found
        return sentinel

    found_value = walk(value)
    return default if found_value is sentinel else found_value


def _deep_true(value: Any, names: Iterable[str]) -> bool:
    wanted = set(names)
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in wanted and _truthy(nested):
                return True
            if _deep_true(nested, wanted):
                return True
    if isinstance(value, (list, tuple)):
        return any(_deep_true(item, wanted) for item in value)
    return False


def _contains_hostile_raw_string(value: Any) -> bool:
    if isinstance(value, str):
        if value in BLOCK_CODES:
            return False
        upper = value.upper()
        return (
            "MUST_NOT_RETURN" in upper
            or "RAW_COMMAND_SUCCESS_BOUNDARY_BODY" in upper
            or ("RAW_" in upper and "BODY" in upper)
            or "HOSTILE_FULL_BODY" in upper
            or len(value) > 4096
        )
    if isinstance(value, Mapping):
        return any(_contains_hostile_raw_string(item) for item in value.values())
    if isinstance(value, (list, tuple, set, frozenset)):
        return any(_contains_hostile_raw_string(item) for item in value)
    return False


def _raw_key_allowed(key: str) -> bool:
    return (
        key in SAFE_RAW_FIELD_NAMES
        or key in REQUIRED_FALSE_NON_CLAIMS
        or key in ALLOWED_TRUE_RECORDED_FIELDS
        or key in BLOCK_CODES
    )


def _has_raw_body(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            key_text = str(key)
            if not _raw_key_allowed(key_text) and _contains_hostile_raw_string(key_text):
                return True
            if key_text in RAW_BODY_KEYS and nested not in (None, False, "", [], {}):
                return True
            if _contains_hostile_raw_string(nested):
                return True
            if _has_raw_body(nested):
                return True
    if isinstance(value, (list, tuple, set, frozenset)):
        return any(_has_raw_body(item) for item in value)
    return _contains_hostile_raw_string(value)


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, nested in value.items():
            key_text = str(key)
            if key_text in RAW_BODY_KEYS or (
                not _raw_key_allowed(key_text) and _contains_hostile_raw_string(key_text)
            ):
                result["raw_body_material_key_omitted"] = True
                result.setdefault("omission_reason", "selected basis remains reference-shaped")
                continue
            result[key_text] = _sanitize(nested)
        return result
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_sanitize(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _contains_hostile_raw_string(value):
            return "[raw_full_body_material_omitted]"
        return value
    return copy.deepcopy(value)


def _json_safe(value: Any) -> Any:
    return _sanitize(value)


def _mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _declared(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    return bool(
        value.get("declared") is True
        or value.get("basis_declared") is True
        or value.get("posture_declared") is True
        or value.get("terminal_summary_declared") is True
        or value.get("reference_shaped_basis") is True
        or value.get("path")
        or value.get("result_path")
        or value.get("artifact_path")
        or value
    )


def _scope_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        value = (
            value.get("values")
            or value.get("scope")
            or value.get("supported_scope")
            or value.get("declared_scope")
        )
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple, set, frozenset)):
        return [str(item) for item in value]
    return []


def _check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str,
) -> None:
    public_code = code if code in BLOCK_CODES else "NON_CLAIM_MISSING_OR_FLIPPED"
    checks.append(
        {
            "check_name": name,
            "passed": bool(passed),
            "expected_posture": _json_safe(expected),
            "actual_posture": _json_safe(actual),
            "block_code": None if passed else public_code,
            "failure_code": None if passed else public_code,
        }
    )


def _section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    source = request.get(key, {})
    section = _sanitize(source)
    if not isinstance(section, Mapping):
        section = {"selected_basis": section}
    result = dict(section)
    result.setdefault("basis_declared", _declared(source))
    result.setdefault("basis_remains_reference_shaped", not _has_raw_body(source))
    result.setdefault("selected_basis_reference_shape_preserved", not _has_raw_body(source))
    result.setdefault("full_prior_artifact_body_not_emitted", True)
    result.setdefault("raw_full_prior_artifact_body_returned", False)
    result.setdefault("prior_artifacts_mutated", False)
    return result


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    source = request.get(key, {})
    section = _sanitize(source if isinstance(source, Mapping) else {})
    result = dict(section) if isinstance(section, Mapping) else {}
    result.setdefault("posture_declared", _declared(source))
    for true_key in ALLOWED_TRUE_RECORDED_FIELDS:
        result.setdefault(true_key, True)
    for false_key in REQUIRED_FALSE_NON_CLAIMS:
        result.setdefault(false_key, False)
    result.setdefault("selected_basis_reference_shape_preserved", True)
    result.setdefault("raw_full_prior_artifact_body_returned", False)
    return result


def _first(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _failed_count(section: Mapping[str, Any]) -> int | None:
    return _to_int(_deep_find(section, ("failed_check_count", "failed_checks")))


def _version(section: Mapping[str, Any]) -> Any:
    return _deep_find(section, ("result_version", "version"))


def _outcome(section: Mapping[str, Any]) -> Any:
    return _deep_find(section, ("outcome", "result_outcome", "selected_outcome"))


def _build_sections(request: Mapping[str, Any]) -> dict[str, Any]:
    sections = {key: _section(request, key) for key in SELECTED_BASIS_KEYS}
    for key in POSTURE_KEYS:
        sections[key] = _posture_section(request, key)

    v2 = sections["selected_command_result_v2_basis"]
    v2.setdefault("outcome", request.get("selected_command_result_v2_result_outcome") or _outcome(v2))
    v2.setdefault("result_version", request.get("selected_command_result_v2_result_version") or _version(v2))
    v2.setdefault(
        "failed_check_count",
        _first(request.get("selected_command_result_v2_failed_check_count"), _failed_count(v2)),
    )
    v2.setdefault(
        "successor_metadata_preserved",
        _first(
            request.get("selected_command_result_v2_successor_metadata_preserved"),
            _deep_find(v2, ("successor_metadata_preserved",)),
        ),
    )
    v2.setdefault("successor_of", _deep_find(v2, ("successor_of",), COMMAND_RESULT_V2_SUCCESSOR_OF))
    v2.setdefault("resolver_module", _deep_find(v2, ("resolver_module",), COMMAND_RESULT_V2_RESOLVER_MODULE))
    v2.setdefault(
        "v1_predecessor_failure_preserved",
        _first(
            request.get("selected_command_result_v2_predecessor_failure_preserved"),
            _deep_find(v2, ("v1_predecessor_failure_preserved",)),
        ),
    )
    v2.setdefault(
        "v1_repaired",
        _first(
            request.get("selected_command_result_v2_v1_repaired"),
            _deep_find(v2, ("v1_repaired", "v1_command_result_repaired"), False),
        ),
    )
    v2.setdefault(
        "v1_hidden",
        _first(
            request.get("selected_command_result_v2_v1_hidden"),
            _deep_find(v2, ("v1_hidden", "v1_command_result_hidden"), False),
        ),
    )
    v2.setdefault(
        "v1_claimed_passed",
        _first(
            request.get("selected_command_result_v2_v1_claimed_passed"),
            _deep_find(v2, ("v1_claimed_passed", "v1_command_result_claimed_passed"), False),
        ),
    )
    erased = request.get("selected_command_result_v2_erased_v1")
    v2.setdefault(
        "v2_successor_does_not_erase_v1",
        False if _truthy(erased) else _deep_find(v2, ("v2_successor_does_not_erase_v1",), None),
    )
    v2.setdefault(
        "bounded_command_result_recorded",
        _first(
            request.get("selected_command_result_v2_bounded_command_result_recorded"),
            _deep_find(v2, ("bounded_command_result_recorded",)),
        ),
    )
    v2.setdefault(
        "command_success_created",
        _first(
            request.get("selected_command_result_v2_already_created_success"),
            _deep_find(v2, ("command_success_created",), False),
        ),
    )
    if request.get("selected_command_result_v2_result_path") is not None:
        v2.setdefault("selected_command_result_v2_result_path", str(request["selected_command_result_v2_result_path"]))

    result_boundary = sections["selected_command_result_boundary_basis"]
    result_boundary.setdefault("outcome", _outcome(result_boundary))
    result_boundary.setdefault("failed_check_count", _failed_count(result_boundary))
    result_boundary.setdefault(
        "one_future_command_result_step_declared",
        _deep_find(result_boundary, ("one_future_command_result_step_declared",)),
    )
    result_boundary.setdefault("command_success_created", _deep_find(result_boundary, ("command_success_created",), False))

    artifact = sections["selected_command_output_report_artifact_basis"]
    artifact.setdefault("outcome", _outcome(artifact))
    artifact.setdefault("failed_check_count", _failed_count(artifact))
    artifact.setdefault(
        "bounded_command_output_report_artifact_recorded",
        _deep_find(artifact, ("bounded_command_output_report_artifact_recorded",)),
    )
    artifact.setdefault("command_success_created", _deep_find(artifact, ("command_success_created",), False))

    capture = sections["selected_output_capture_v2_basis"]
    capture.setdefault("outcome", _outcome(capture))
    capture.setdefault("result_version", request.get("selected_output_capture_v2_result_version") or _version(capture))
    capture.setdefault(
        "failed_check_count",
        _first(request.get("selected_output_capture_v2_failed_check_count"), _failed_count(capture)),
    )
    capture.setdefault(
        "json_safe_result",
        _first(request.get("selected_output_capture_v2_json_safe_result"), _deep_find(capture, ("json_safe_result",))),
    )
    capture.setdefault("v1_predecessor_failure_preserved", _deep_find(capture, ("v1_predecessor_failure_preserved",)))
    capture.setdefault("v1_repaired", _deep_find(capture, ("v1_repaired",), False))
    capture.setdefault("v1_hidden", _deep_find(capture, ("v1_hidden",), False))
    capture.setdefault("v1_claimed_passed", _deep_find(capture, ("v1_claimed_passed",), False))
    capture.setdefault("v2_successor_does_not_erase_v1", _deep_find(capture, ("v2_successor_does_not_erase_v1",)))
    for invented in (
        "stdout_content_invented",
        "stderr_content_invented",
        "process_output_content_invented",
        "raw_output_body_content_invented",
    ):
        capture.setdefault(invented, _deep_find(capture, (invented,), False))

    post_execution = sections["selected_post_invocation_command_execution_basis"]
    post_execution.setdefault("outcome", _outcome(post_execution))
    post_execution.setdefault("failed_check_count", _failed_count(post_execution))
    post_execution.setdefault("execution_trace_audit_only", _deep_find(post_execution, ("execution_trace_audit_only",)))

    admitted = sections["selected_v2_admitted_request_basis"]
    admitted.setdefault("outcome", _outcome(admitted))
    admitted.setdefault("result_version", _version(admitted))
    admitted.setdefault("failed_check_count", _failed_count(admitted))
    return sections


def _evaluate_checks(request: Mapping[str, Any], sections: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    intent = request.get("command_success_boundary_intent")
    question = request.get("command_success_boundary_question")
    scopes = _scope_values(request.get("command_success_boundary_scope"))
    unsupported = [scope for scope in scopes if scope not in SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE]

    _check(checks, "command success boundary question declared", isinstance(question, str) and bool(question.strip()), CORE_QUESTION, question, "COMMAND_SUCCESS_BOUNDARY_QUESTION_UNDECLARED")
    _check(checks, "command success boundary intent supported", intent in SUPPORTED_INTENTS and intent != INTENT_BLOCK, sorted(SUPPORTED_INTENTS), intent, "COMMAND_SUCCESS_BOUNDARY_BLOCK_INTENT_REQUESTED" if intent == INTENT_BLOCK else "COMMAND_SUCCESS_BOUNDARY_INTENT_UNSUPPORTED")
    _check(checks, "command success boundary scope supported", bool(scopes) and not unsupported, sorted(SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE), scopes, "UNSUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE")

    for key, code in BASIS_BLOCK_CODES.items():
        _check(checks, f"{key} declared", _declared(request.get(key)), "declared selected basis", request.get(key), code)
        _check(
            checks,
            f"{key} reference-shaped",
            not _has_raw_body(request.get(key)),
            "reference-shaped basis without raw full body",
            request.get(key),
            "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
        )
    for key, code in POSTURE_BLOCK_CODES.items():
        _check(checks, f"{key} declared", _declared(request.get(key)), "declared posture", request.get(key), code)

    v2 = sections["selected_command_result_v2_basis"]
    _check(checks, "command result v2 outcome recorded", v2.get("outcome") == COMMAND_RESULT_V2_OUTCOME, COMMAND_RESULT_V2_OUTCOME, v2.get("outcome"), "COMMAND_RESULT_V2_NOT_RECORDED")
    _check(checks, "command result v2 version 0.2.0", v2.get("result_version") == COMMAND_RESULT_V2_VERSION, COMMAND_RESULT_V2_VERSION, v2.get("result_version"), "COMMAND_RESULT_V2_VERSION_NOT_0_2_0")
    _check(checks, "command result v2 failed check count zero", v2.get("failed_check_count") == 0, 0, v2.get("failed_check_count"), "COMMAND_RESULT_V2_FAILED_CHECKS_PRESENT")
    _check(checks, "command result v2 successor metadata present", v2.get("successor_metadata_preserved") is True and v2.get("successor_of") == COMMAND_RESULT_V2_SUCCESSOR_OF, COMMAND_RESULT_V2_SUCCESSOR_OF, {"successor_metadata_preserved": v2.get("successor_metadata_preserved"), "successor_of": v2.get("successor_of")}, "COMMAND_RESULT_V2_SUCCESSOR_METADATA_MISSING")
    _check(checks, "command result v2 predecessor failure evidence preserved", v2.get("v1_predecessor_failure_preserved") is True, True, v2.get("v1_predecessor_failure_preserved"), "COMMAND_RESULT_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING")
    _check(checks, "command result v2 v1 repaired false", not _truthy(v2.get("v1_repaired")), False, v2.get("v1_repaired"), "COMMAND_RESULT_V2_REPAIRED_V1")
    _check(checks, "command result v2 v1 hidden false", not _truthy(v2.get("v1_hidden")), False, v2.get("v1_hidden"), "COMMAND_RESULT_V2_HID_V1")
    _check(checks, "command result v2 v1 claimed passed false", not _truthy(v2.get("v1_claimed_passed")), False, v2.get("v1_claimed_passed"), "COMMAND_RESULT_V2_CLAIMED_V1_PASSED")
    _check(checks, "command result v2 did not erase v1", v2.get("v2_successor_does_not_erase_v1") is True and not _deep_true(request, ("selected_command_result_v2_erased_v1", "v2_command_result_erased_v1")), True, v2.get("v2_successor_does_not_erase_v1"), "COMMAND_RESULT_V2_ERASED_V1")
    _check(checks, "command result v2 bounded command result recorded", v2.get("bounded_command_result_recorded") is True, True, v2.get("bounded_command_result_recorded"), "COMMAND_RESULT_V2_NOT_BOUNDED")
    _check(checks, "command result v2 command success not created", not _truthy(v2.get("command_success_created")), False, v2.get("command_success_created"), "COMMAND_RESULT_V2_ALREADY_CREATED_SUCCESS")
    for label, key, code in (
        ("success", "selected_command_result_v2_inferred_success", "COMMAND_RESULT_V2_INFERRED_SUCCESS"),
        ("currentness", "selected_command_result_v2_inferred_currentness", "COMMAND_RESULT_V2_INFERRED_CURRENTNESS"),
        ("final completion", "selected_command_result_v2_inferred_final_completion", "COMMAND_RESULT_V2_INFERRED_FINAL_COMPLETION"),
        ("public readiness", "selected_command_result_v2_inferred_public_readiness", "COMMAND_RESULT_V2_INFERRED_PUBLIC_READINESS"),
        ("deployment readiness", "selected_command_result_v2_inferred_deployment_readiness", "COMMAND_RESULT_V2_INFERRED_DEPLOYMENT_READINESS"),
        ("authority", "selected_command_result_v2_inferred_authority", "COMMAND_RESULT_V2_INFERRED_AUTHORITY"),
        ("follow-on work", "selected_command_result_v2_inferred_follow_on_work", "COMMAND_RESULT_V2_INFERRED_FOLLOW_ON_WORK"),
        ("unbounded pass/fail", "selected_command_result_v2_inferred_unbounded_pass_fail", "COMMAND_RESULT_V2_INFERRED_UNBOUNDED_PASS_FAIL"),
    ):
        _check(checks, f"command result v2 did not infer {label}", not _truthy(request.get(key)), False, request.get(key), code)

    result_boundary = sections["selected_command_result_boundary_basis"]
    _check(checks, "command result boundary recorded", result_boundary.get("outcome") == COMMAND_RESULT_BOUNDARY_OUTCOME, COMMAND_RESULT_BOUNDARY_OUTCOME, result_boundary.get("outcome"), "COMMAND_RESULT_BOUNDARY_NOT_RECORDED")
    _check(checks, "command result boundary failed check count zero", result_boundary.get("failed_check_count") in (0, None), 0, result_boundary.get("failed_check_count"), "COMMAND_RESULT_BOUNDARY_FAILED_CHECKS_PRESENT")
    _check(checks, "command result boundary one future result step declared", result_boundary.get("one_future_command_result_step_declared") is True, True, result_boundary.get("one_future_command_result_step_declared"), "COMMAND_RESULT_BOUNDARY_STEP_NOT_DECLARED")
    _check(checks, "command result boundary no command success", not _truthy(result_boundary.get("command_success_created")), False, result_boundary.get("command_success_created"), "COMMAND_RESULT_BOUNDARY_ALREADY_CREATED_SUCCESS")

    artifact = sections["selected_command_output_report_artifact_basis"]
    _check(checks, "command output/report artifact recorded", artifact.get("outcome") == COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME, COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME, artifact.get("outcome"), "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED")
    _check(checks, "command output/report artifact failed check count zero", artifact.get("failed_check_count") in (0, None), 0, artifact.get("failed_check_count"), "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT")
    _check(checks, "command output/report artifact no command success", not _truthy(artifact.get("command_success_created")), False, artifact.get("command_success_created"), "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_SUCCESS")

    capture = sections["selected_output_capture_v2_basis"]
    _check(checks, "output capture v2 recorded", capture.get("outcome") == OUTPUT_CAPTURE_V2_OUTCOME, OUTPUT_CAPTURE_V2_OUTCOME, capture.get("outcome"), "OUTPUT_CAPTURE_V2_NOT_RECORDED")
    _check(checks, "output capture v2 version 0.2.0", capture.get("result_version") == OUTPUT_CAPTURE_V2_VERSION, OUTPUT_CAPTURE_V2_VERSION, capture.get("result_version"), "OUTPUT_CAPTURE_V2_VERSION_NOT_0_2_0")
    _check(checks, "output capture v2 failed check count zero", capture.get("failed_check_count") in (0, None), 0, capture.get("failed_check_count"), "OUTPUT_CAPTURE_V2_FAILED_CHECKS_PRESENT")
    _check(checks, "output capture v2 JSON-safe result preserved", capture.get("json_safe_result") is True, True, capture.get("json_safe_result"), "OUTPUT_CAPTURE_V2_JSON_SAFE_RESULT_NOT_PRESERVED")
    _check(checks, "output capture v2 predecessor failure evidence preserved", capture.get("v1_predecessor_failure_preserved") is True, True, capture.get("v1_predecessor_failure_preserved"), "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING")
    _check(checks, "output capture v2 v1 repaired false", not _truthy(capture.get("v1_repaired")), False, capture.get("v1_repaired"), "OUTPUT_CAPTURE_V2_REPAIRED_V1")
    _check(checks, "output capture v2 v1 hidden false", not _truthy(capture.get("v1_hidden")), False, capture.get("v1_hidden"), "OUTPUT_CAPTURE_V2_HID_V1")
    _check(checks, "output capture v2 v1 claimed passed false", not _truthy(capture.get("v1_claimed_passed")), False, capture.get("v1_claimed_passed"), "OUTPUT_CAPTURE_V2_CLAIMED_V1_PASSED")
    _check(checks, "output capture v2 did not erase v1", capture.get("v2_successor_does_not_erase_v1") is True, True, capture.get("v2_successor_does_not_erase_v1"), "OUTPUT_CAPTURE_V2_ERASED_V1")
    for key, code in (
        ("stdout_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDOUT_CONTENT"),
        ("stderr_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDERR_CONTENT"),
        ("process_output_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_PROCESS_OUTPUT_CONTENT"),
        ("raw_output_body_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_RAW_OUTPUT_BODY_CONTENT"),
    ):
        _check(checks, f"output capture v2 {key} false", not _truthy(capture.get(key)), False, capture.get(key), code)

    execution = sections["selected_post_invocation_command_execution_basis"]
    _check(checks, "post-invocation command execution recorded", execution.get("outcome") == POST_INVOCATION_COMMAND_EXECUTION_OUTCOME, POST_INVOCATION_COMMAND_EXECUTION_OUTCOME, execution.get("outcome"), "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED")
    _check(checks, "post-invocation command execution failed check count zero", execution.get("failed_check_count") in (0, None), 0, execution.get("failed_check_count"), "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT")
    _check(checks, "execution trace audit-only", execution.get("execution_trace_audit_only") is True, True, execution.get("execution_trace_audit_only"), "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY")

    admitted = sections["selected_v2_admitted_request_basis"]
    _check(checks, "v2 admitted request failed check count zero", admitted.get("failed_check_count") in (0, None), 0, admitted.get("failed_check_count"), "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT")

    for label, names, code in COLLAPSE_CHECKS:
        _check(checks, label, not _deep_true(request, names), "all overreach flags false", {name: _deep_find(request, (name,)) for name in names}, code)
    _check(checks, "raw full prior artifact body not emitted", not _has_raw_body(request), "reference-shaped basis only", "raw body present" if _has_raw_body(request) else None, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
    _check(checks, "raw full prior artifact body not returned", not _has_raw_body(request), "returned result excludes raw full prior artifact body", "raw body present" if _has_raw_body(request) else None, "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED")
    non_claims = request.get("declared_non_claims")
    non_claims_false = isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
    )
    _check(checks, "declared non-claims remain false", non_claims_false, {key: False for key in REQUIRED_FALSE_NON_CLAIMS}, non_claims, "NON_CLAIM_MISSING_OR_FLIPPED")
    return checks


def _statement(recorded: bool) -> dict[str, Any]:
    result = {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}
    result.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    result.update(
        {
            "command_success_boundary_is_not_command_success": True,
            "command_success_boundary_is_not_source": True,
            "command_success_boundary_is_not_authority": True,
            "command_success_boundary_is_not_currentness": True,
            "command_success_boundary_is_not_final_completion": True,
            "command_success_boundary_is_not_public_readiness": True,
            "command_success_boundary_is_not_deployment_readiness": True,
            "command_result_v2_remains_command_result_posture_only": True,
            "output_capture_v2_remains_output_capture_posture_only": True,
            "execution_trace_remains_audit_only": True,
            "command_report_lineage_remains_lineage_only": True,
            "v1_predecessor_failure_preserved": True,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
            "v2_successor_does_not_erase_v1": True,
            "returned_result_containment_preserved": True,
            "selected_basis_reference_shape_preserved": True,
            "raw_full_prior_artifact_body_returned": False,
        }
    )
    return result


def _non_meaning() -> dict[str, bool]:
    return {
        "command_success_exists": False,
        "success_body_exists": False,
        "success_was_inferred": False,
        "currentness_was_inferred": False,
        "final_completion_was_inferred": False,
        "public_readiness_was_inferred": False,
        "deployment_readiness_was_inferred": False,
        "authority_was_inferred": False,
        "follow_on_work_was_inferred": False,
        "unbounded_pass_fail_was_inferred": False,
        "command_result_became_success": False,
        "command_result_became_source": False,
        "command_result_became_authority": False,
        "command_result_became_currentness": False,
        "command_result_became_final_completion": False,
        "command_result_became_public_readiness": False,
        "command_result_became_deployment_readiness": False,
        "command_success_boundary_is_success": False,
        "command_success_boundary_is_source": False,
        "command_success_boundary_is_authority": False,
        "command_success_boundary_is_currentness": False,
        "command_success_boundary_is_final_completion": False,
        "command_success_boundary_is_public_readiness": False,
        "command_success_boundary_is_deployment_readiness": False,
        "output_capture_is_result": False,
        "output_capture_is_success": False,
        "output_capture_is_source": False,
        "output_capture_is_authority": False,
        "output_capture_is_currentness": False,
        "output_capture_is_final_completion": False,
        "execution_trace_is_success": False,
        "execution_trace_is_source": False,
        "execution_trace_is_authority": False,
        "execution_trace_is_currentness": False,
        "execution_trace_is_final_completion": False,
        "v1_command_result_predecessor_repaired": False,
        "v1_command_result_predecessor_hidden": False,
        "v1_command_result_predecessor_passed": False,
        "v2_command_result_erased_v1": False,
        "v1_output_capture_predecessor_repaired": False,
        "v1_output_capture_predecessor_hidden": False,
        "v1_output_capture_predecessor_passed": False,
        "v2_output_capture_erased_v1": False,
        "command_report_lineage_is_current_report_artifact": False,
        "command_report_lineage_is_command_result_authority": False,
        "command_report_lineage_is_command_success": False,
        "consumed_request_token_reopened": False,
        "authorization_token_reusable": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "public_readiness_created": False,
        "deployment_readiness_created": False,
        "operation_permission_created": False,
        "final_completion_created": False,
        "continuation_authorized": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
        "raw_full_prior_artifact_body_returned": False,
    }


def _metadata(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]], outcome: str) -> dict[str, Any]:
    request_id = str(
        request.get("command_success_boundary_request_id")
        or "portable_source_body_verification_command_success_boundary_request"
    )
    return {
        "portable_source_body_verification_command_success_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_command_success_boundary_v2_result"
        ),
        "portable_source_body_verification_command_success_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_success_boundary_result_version": RESULT_VERSION,
        "result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of": SUCCESSOR_OF,
        "successor_reason": SUCCESSOR_REASON,
        "v1_predecessor_failure_preserved": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "v2_successor_does_not_erase_v1": True,
        "returned_result_containment_preserved": True,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "outcome": outcome,
        "passed_check_count": sum(1 for check in checks if check.get("passed")),
        "failed_check_count": sum(1 for check in checks if not check.get("passed")),
        "output_root": str(OUTPUT_ROOT),
        "core_question": CORE_QUESTION,
        "command_success_boundary_is_not_command_success": True,
        "command_success_still_requires_separately_bounded_step": True,
    }


def _choose_outcome(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> tuple[str, dict[str, Any]]:
    failed = [check for check in checks if not check.get("passed")]
    if failed:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": failed[0].get("block_code"),
                "block_reason": failed[0].get("check_name"),
                "block_scope": "portable_source_body_verification_command_success_boundary_v2",
            },
        )
    requested = request.get("requested_command_success_boundary_outcome")
    if request.get("command_success_boundary_intent") == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, {"blocked": False, "block_code": None, "block_reason": None, "block_scope": None}
    if request.get("additional_basis_context") or requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, {"blocked": False, "block_code": None, "block_reason": None, "block_scope": None}
    if request.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED, {"blocked": False, "block_code": None, "block_reason": None, "block_scope": None}
    return OUTCOME_RECORDED, {"blocked": False, "block_code": None, "block_reason": None, "block_scope": None}


def _open_items() -> dict[str, Any]:
    return {
        "open_items": list(OPEN_ITEMS),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _build_result(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str | None = None,
    block: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    clean_request = _json_safe(request)
    clean_mapping = clean_request if isinstance(clean_request, Mapping) else {}
    sections = _build_sections(clean_mapping)
    checks_copy = [_json_safe(check) for check in checks]
    selected_outcome, selected_block = (outcome, dict(block or {})) if outcome else _choose_outcome(request, checks)
    selected_block = _json_safe(selected_block)
    statement = _statement(selected_outcome == OUTCOME_RECORDED)
    question = _json_safe(
        {
            "command_success_boundary_request_id": request.get("command_success_boundary_request_id"),
            "question": request.get("command_success_boundary_question"),
            "intent": request.get("command_success_boundary_intent"),
            "core_question": CORE_QUESTION,
            "does_not_create_command_success": True,
            "does_not_create_success_body": True,
        }
    )
    result: dict[str, Any] = {
        "portable_source_body_verification_command_success_boundary_metadata": _metadata(request, checks_copy, selected_outcome),
        "declared_command_success_boundary_question": question,
        **sections,
        "command_success_boundary_scope": {
            "declared_scope": _json_safe(_scope_values(request.get("command_success_boundary_scope"))),
            "supported_scope": sorted(SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE),
            "unsupported_scope_values": [
                scope
                for scope in _scope_values(request.get("command_success_boundary_scope"))
                if scope not in SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE
            ],
        },
        "command_success_boundary_checks": checks_copy,
        "command_success_boundary_statement": statement,
        "command_success_boundary_non_meaning": _non_meaning(),
        "additional_basis_required": {
            "additional_basis_required": selected_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "missing_or_unclear_basis": _json_safe(request.get("additional_basis_context"))
            if selected_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else [],
            "missing_basis_not_scheduled": True,
            "missing_basis_not_authorized": True,
            "missing_basis_not_executed": True,
        },
        "not_recorded_basis": {
            "not_recorded": selected_outcome == OUTCOME_NOT_RECORDED,
            "not_recorded_basis": _json_safe(request.get("not_recorded_basis"))
            if selected_outcome == OUTCOME_NOT_RECORDED
            else [],
            "prior_artifacts_mutated": False,
            "command_success_created": False,
            "follow_on_work_authorized": False,
        },
        "what_remains_open": _open_items(),
        "non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "outcome": selected_outcome,
        "block": dict(selected_block),
    }
    result["portable_source_body_verification_command_success_boundary_summary"] = (
        build_portable_source_body_verification_command_success_boundary_v2_summary(result)
    )
    return _json_safe(result)


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(checks, reason, False, "declared command success boundary request mapping", None, code)
    return _build_result(
        {},
        checks,
        OUTCOME_BLOCKED,
        {
            "blocked": True,
            "block_code": code,
            "block_reason": reason,
            "block_scope": "declared_command_success_boundary_request",
        },
    )


def resolve_portable_source_body_verification_command_success_boundary_v2(
    declared_command_success_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve whether one command result v2 basis may be bounded for success."""

    if not isinstance(declared_command_success_boundary_request, Mapping):
        return _malformed_result(
            "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared command success boundary request malformed",
        )
    request = copy.deepcopy(dict(declared_command_success_boundary_request))
    sections = _build_sections(request)
    checks = _evaluate_checks(request, sections)
    return _build_result(request, checks)


def resolve_portable_source_body_verification_command_success_boundary_v2_from_path(
    declared_command_success_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Read a JSON object request and resolve command success boundary v2 posture."""

    path = Path(declared_command_success_boundary_request_path)
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        return _malformed_result(
            "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_UNREADABLE",
            "declared command success boundary request unreadable",
        )
    except json.JSONDecodeError:
        return _malformed_result(
            "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared command success boundary request JSON malformed",
        )
    if not isinstance(parsed, Mapping):
        return _malformed_result(
            "DECLARED_COMMAND_SUCCESS_BOUNDARY_REQUEST_MALFORMED",
            "declared command success boundary request JSON is not an object",
        )
    return resolve_portable_source_body_verification_command_success_boundary_v2(parsed)


def _safe_filename(value: Any) -> str:
    text = str(value or "portable_source_body_verification_command_success_boundary_request")
    safe = "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in text)
    return safe.strip("_") or "portable_source_body_verification_command_success_boundary_request"


def _dedupe_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationCommandSuccessBoundaryV2Error(
        "could not create deterministic non-overwriting output path"
    )


def write_portable_source_body_verification_command_success_boundary_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded v2 command success boundary result without overwriting."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandSuccessBoundaryV2Error("result must be a mapping")
    metadata = _mapping(
        result.get("portable_source_body_verification_command_success_boundary_metadata")
    )
    question = _mapping(result.get("declared_command_success_boundary_question"))
    request_id = (
        question.get("command_success_boundary_request_id")
        or metadata.get("portable_source_body_verification_command_success_boundary_result_id")
        or "portable_source_body_verification_command_success_boundary_request"
    )
    path = (
        Path(output_path)
        if output_path is not None
        else OUTPUT_ROOT
        / f"{_safe_filename(request_id)}__portable_source_body_verification_command_success_boundary_v2_result.json"
    )
    path = _dedupe_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_safe(result), ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_portable_source_body_verification_command_success_boundary_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary preserving v2 successor boundary posture."""

    metadata = _mapping(result.get("portable_source_body_verification_command_success_boundary_metadata"))
    question = _mapping(result.get("declared_command_success_boundary_question"))
    block = _mapping(result.get("block"))
    statement = _mapping(result.get("command_success_boundary_statement"))
    v2 = _mapping(result.get("selected_command_result_v2_basis"))
    artifact = _mapping(result.get("selected_command_output_report_artifact_basis"))
    capture = _mapping(result.get("selected_output_capture_v2_basis"))
    command_output = _mapping(result.get("selected_command_output_basis"))
    execution = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    admitted = _mapping(result.get("selected_v2_admitted_request_basis"))
    checks = result.get("command_success_boundary_checks", [])
    failed = metadata.get("failed_check_count")
    passed = metadata.get("passed_check_count")
    if failed is None and isinstance(checks, Sequence):
        failed = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    if passed is None and isinstance(checks, Sequence):
        passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("command_success_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "result_version": metadata.get("result_version"),
        "v2_result_version": metadata.get("result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "successor_of": metadata.get("successor_of"),
        "successor_reason": metadata.get("successor_reason"),
        "v1_predecessor_failure_preserved": metadata.get("v1_predecessor_failure_preserved"),
        "v1_repaired": metadata.get("v1_repaired"),
        "v1_hidden": metadata.get("v1_hidden"),
        "v1_claimed_passed": metadata.get("v1_claimed_passed"),
        "v2_successor_does_not_erase_v1": metadata.get("v2_successor_does_not_erase_v1"),
        "returned_result_containment_preserved": metadata.get("returned_result_containment_preserved"),
        "selected_basis_reference_shape_preserved": metadata.get("selected_basis_reference_shape_preserved"),
        "raw_full_prior_artifact_body_returned": metadata.get("raw_full_prior_artifact_body_returned"),
        "command_success_boundary_recorded": statement.get("command_success_boundary_recorded", False),
        "one_future_command_success_step_declared": statement.get("one_future_command_success_step_declared", False),
        "command_result_v2_basis_preserved": statement.get("command_result_v2_basis_preserved", False),
        "bounded_command_result_preserved": statement.get("bounded_command_result_preserved", False),
        "command_result_v1_predecessor_failure_preserved": statement.get("command_result_v1_predecessor_failure_preserved", False),
        "command_result_boundary_basis_preserved": statement.get("command_result_boundary_basis_preserved", False),
        "command_output_report_artifact_basis_preserved": statement.get("command_output_report_artifact_basis_preserved", False),
        "report_body_absent_or_bounded": statement.get("report_body_absent_or_bounded", False),
        "result_body_absent_or_bounded": statement.get("result_body_absent_or_bounded", False),
        "report_body_not_invented": statement.get("report_body_not_invented", False),
        "result_body_not_invented": statement.get("result_body_not_invented", False),
        "success_body_not_invented": statement.get("success_body_not_invented", False),
        "command_success_still_not_created": statement.get("command_success_still_not_created", False),
        "success_inference_blocked": statement.get("success_inference_blocked", False),
        "currentness_inference_blocked": statement.get("currentness_inference_blocked", False),
        "final_completion_inference_blocked": statement.get("final_completion_inference_blocked", False),
        "public_readiness_inference_blocked": statement.get("public_readiness_inference_blocked", False),
        "deployment_readiness_inference_blocked": statement.get("deployment_readiness_inference_blocked", False),
        "authority_inference_blocked": statement.get("authority_inference_blocked", False),
        "follow_on_work_inference_blocked": statement.get("follow_on_work_inference_blocked", False),
        "unbounded_pass_fail_inference_blocked": statement.get("unbounded_pass_fail_inference_blocked", False),
        "selected_command_result_v2_outcome": v2.get("outcome"),
        "selected_command_result_v2_version": v2.get("result_version"),
        "selected_command_result_v2_failed_check_count": v2.get("failed_check_count"),
        "selected_command_result_v2_successor_metadata_preserved": v2.get("successor_metadata_preserved"),
        "selected_command_output_report_artifact_outcome": artifact.get("outcome"),
        "selected_command_output_report_artifact_failed_check_count": artifact.get("failed_check_count"),
        "selected_output_capture_v2_outcome": capture.get("outcome"),
        "selected_output_capture_v2_version": capture.get("result_version"),
        "selected_output_capture_v2_failed_check_count": capture.get("failed_check_count"),
        "selected_command_output_outcome": command_output.get("outcome"),
        "selected_command_output_failed_check_count": command_output.get("failed_check_count"),
        "selected_post_invocation_execution_outcome": execution.get("outcome"),
        "selected_post_invocation_execution_failed_check_count": execution.get("failed_check_count"),
        "selected_v2_admitted_request_outcome": admitted.get("outcome"),
        "selected_v2_admitted_request_version": admitted.get("result_version"),
        "selected_v2_admitted_request_failed_check_count": admitted.get("failed_check_count"),
        "success_boundary_not_success_source_authority_currentness_final_completion_public_readiness_deployment_readiness": True,
        "command_result_not_success_source_authority_currentness_final_completion_public_readiness_deployment_readiness": True,
        "output_capture_not_result_success_source_authority_currentness_final_completion": True,
        "execution_trace_not_success_source_authority_currentness_final_completion": True,
        "command_report_lineage_not_current_report_artifact_result_authority_success_source_authority_currentness": True,
        "no_raw_full_prior_artifact_body": True,
        "no_artifact_mutation": True,
        "no_deployment_runtime_public_release": True,
        "no_operation_public_readiness_deployment_readiness_final_completion": True,
        "no_continuation_publication_reusable_follow_on": True,
        "key_non_claims": {
            key: _mapping(result.get("non_claims")).get(key)
            for key in (
                "command_success_created",
                "success_body_invented",
                "success_inference_made",
                "currentness_inference_made",
                "final_completion_inference_made",
                "public_readiness_inference_made",
                "deployment_readiness_inference_made",
                "authority_inference_made",
                "follow_on_work_inference_made",
                "unbounded_pass_fail_inference_made",
                "authorization_token_reused",
                "consumed_request_reopened",
                "raw_full_prior_artifact_body_returned",
            )
        },
    }


def _basis(label: str, **overrides: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "basis_label": label,
        "declared": True,
        "basis_declared": True,
        "basis_reference": f"synthetic://{label}",
        "path": f"synthetic://{label}.json",
        "result_path": f"synthetic://{label}.json",
        "reference_shaped_basis": True,
        "basis_remains_reference_shaped": True,
        "selected_basis_reference_shape_preserved": True,
        "basis_remains_basis_only": True,
        "full_prior_artifact_body_not_emitted": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
        "report_body_absent_or_bounded": True,
        "report_body_not_invented": True,
        "result_body_absent_or_bounded": True,
        "result_body_not_invented": True,
        "command_success_created": False,
        "success_body_invented": False,
        "success_inference_made": False,
        "currentness_inference_made": False,
        "final_completion_inference_made": False,
        "public_readiness_inference_made": False,
        "deployment_readiness_inference_made": False,
        "authority_inference_made": False,
        "follow_on_work_inference_made": False,
        "unbounded_pass_fail_inference_made": False,
        "authorization_token_reuse_blocked": True,
        "authorization_token_reused": False,
        "consumed_request_token_remains_closed": True,
        "consumed_request_reopened": False,
        "returned_result_containment_preserved": True,
    }
    result.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    result.update(overrides)
    return result


def _terminal(label: str, **overrides: Any) -> dict[str, Any]:
    result = _basis(
        label,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{label}.md",
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    result.update(overrides)
    return result


def _posture(label: str, **overrides: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "posture_label": label,
        "declared": True,
        "posture_declared": True,
        "posture": label,
        "selected_basis_reference_shape_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
    }
    result.update({key: True for key in ALLOWED_TRUE_RECORDED_FIELDS})
    result.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    result.update(overrides)
    return result


def build_declared_portable_source_body_verification_command_success_boundary_v2_request(
    command_success_boundary_request_id: str = "command_success_boundary_reference_review_001_v2",
    command_success_boundary_question: str = CORE_QUESTION,
    command_success_boundary_intent: str = INTENT_RECORD,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a valid reference-shaped command success boundary v2 request."""

    request: dict[str, Any] = {
        "command_success_boundary_request_id": command_success_boundary_request_id,
        "command_success_boundary_question": command_success_boundary_question,
        "command_success_boundary_intent": command_success_boundary_intent,
        "selected_command_result_v2_basis": _basis(
            "command_result_v2",
            outcome=COMMAND_RESULT_V2_OUTCOME,
            result_version=COMMAND_RESULT_V2_VERSION,
            resolver_module=COMMAND_RESULT_V2_RESOLVER_MODULE,
            failed_check_count=0,
            passed_check_count=169,
            successor_metadata_preserved=True,
            successor_of=COMMAND_RESULT_V2_SUCCESSOR_OF,
            v1_predecessor_failure_preserved=True,
            v1_repaired=False,
            v1_hidden=False,
            v1_claimed_passed=False,
            v2_successor_does_not_erase_v1=True,
            bounded_command_result_recorded=True,
            command_success_created=False,
        ),
        "selected_command_result_v2_terminal_summary_basis": _terminal(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_V2_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_result_v1_predecessor_failure_basis": _basis(
            "command_result_v1_predecessor_failure",
            v1_command_result_repaired=False,
            v1_command_result_hidden=False,
            v1_command_result_claimed_passed=False,
            v2_command_result_erased_v1=False,
        ),
        "selected_command_result_boundary_basis": _basis(
            "command_result_boundary",
            outcome=COMMAND_RESULT_BOUNDARY_OUTCOME,
            failed_check_count=0,
            one_future_command_result_step_declared=True,
            command_success_created=False,
        ),
        "selected_command_result_boundary_terminal_summary_basis": _terminal(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_output_report_artifact_basis": _basis(
            "command_output_report_artifact",
            outcome=COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME,
            failed_check_count=0,
            bounded_command_output_report_artifact_recorded=True,
            command_success_created=False,
        ),
        "selected_command_output_report_artifact_terminal_summary_basis": _terminal(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_output_report_artifact_boundary_basis": _basis(
            "command_output_report_artifact_boundary",
            outcome=COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME,
            failed_check_count=0,
        ),
        "selected_command_output_report_artifact_boundary_terminal_summary_basis": _terminal(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_TERMINAL_SUMMARY_V0"
        ),
        "selected_output_capture_v2_basis": _basis(
            "output_capture_v2",
            outcome=OUTPUT_CAPTURE_V2_OUTCOME,
            result_version=OUTPUT_CAPTURE_V2_VERSION,
            failed_check_count=0,
            json_safe_result=True,
            v1_predecessor_failure_preserved=True,
            v1_repaired=False,
            v1_hidden=False,
            v1_claimed_passed=False,
            v2_successor_does_not_erase_v1=True,
            stdout_content_invented=False,
            stderr_content_invented=False,
            process_output_content_invented=False,
            raw_output_body_content_invented=False,
        ),
        "selected_output_capture_v2_terminal_summary_basis": _terminal(
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_V2_TERMINAL_SUMMARY_V0"
        ),
        "selected_output_capture_v1_predecessor_failure_basis": _basis(
            "output_capture_v1_predecessor_failure",
            v1_output_capture_repaired=False,
            v1_output_capture_hidden=False,
            v1_output_capture_claimed_passed=False,
            v2_output_capture_erased_v1=False,
        ),
        "selected_output_capture_boundary_basis": _basis(
            "output_capture_boundary",
            outcome=OUTPUT_CAPTURE_BOUNDARY_OUTCOME,
            failed_check_count=0,
        ),
        "selected_command_output_basis": _basis(
            "command_output",
            outcome=COMMAND_OUTPUT_OUTCOME,
            failed_check_count=0,
        ),
        "selected_command_output_boundary_basis": _basis(
            "command_output_boundary",
            outcome=COMMAND_OUTPUT_BOUNDARY_OUTCOME,
            failed_check_count=0,
        ),
        "selected_command_output_containment_basis": _basis(
            "command_output_containment",
            outcome=COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
            failed_check_count=0,
        ),
        "selected_post_invocation_command_execution_basis": _basis(
            "post_invocation_command_execution",
            outcome=POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            failed_check_count=0,
            one_bounded_command_execution_event_recorded=True,
            execution_trace_audit_only=True,
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": _terminal(
            "post_invocation_command_execution_terminal_summary"
        ),
        "selected_command_invocation_basis": _basis(
            "command_invocation",
            outcome=COMMAND_INVOCATION_OUTCOME,
            failed_check_count=0,
            authorization_token_spent_exactly_once=True,
        ),
        "selected_command_execution_review_basis": _basis(
            "command_execution_review",
            outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
            failed_check_count=0,
        ),
        "selected_request_consumption_basis": _basis(
            "request_consumption",
            outcome=REQUEST_CONSUMPTION_OUTCOME,
            failed_check_count=0,
        ),
        "selected_consumed_request_basis": _basis(
            "consumed_request",
            consumed_request_token_remains_closed=True,
            consumed_request_reopened=False,
        ),
        "selected_v2_admitted_request_basis": _basis(
            "v2_admitted_request",
            outcome=V2_ADMITTED_REQUEST_OUTCOME,
            result_version=V2_ADMITTED_REQUEST_VERSION,
            failed_check_count=0,
        ),
        "selected_v1_predecessor_failure_basis": _basis(
            "earlier_v1_predecessor_failure",
            v1_repaired=False,
            v1_hidden=False,
            v1_claimed_passed=False,
        ),
        "selected_older_command_execution_boundary_lineage_basis": _basis(
            "older_command_execution_boundary_lineage",
            basis_remains_prior_scaffolding_only=True,
            older_command_execution_boundary_lineage_treated_as_current_execution=False,
        ),
        "selected_command_report_lineage_basis": _basis(
            "command_report_lineage",
            basis_remains_lineage_only=True,
            command_report_lineage_basis_treated_as_current_report_artifact=False,
            command_report_lineage_basis_treated_as_command_result_authority=False,
            command_report_lineage_basis_treated_as_command_success=False,
            command_report_lineage_basis_treated_as_source=False,
            command_report_lineage_basis_treated_as_authority=False,
            command_report_lineage_basis_treated_as_currentness=False,
        ),
        "selected_command_implementation_boundary_basis": _basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _basis("evidence_manifest"),
        "selected_portable_verification_basis": _basis("portable_verification"),
        "command_success_boundary_scope": sorted(SUPPORTED_COMMAND_SUCCESS_BOUNDARY_SCOPE),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "reference_shaped_input_posture": True,
        "requested_command_success_boundary_outcome": OUTCOME_RECORDED,
    }
    for key in POSTURE_KEYS:
        request[key] = _posture(key)
    request.update(overrides)
    return request


resolve_portable_source_body_verification_command_success_boundary = (
    resolve_portable_source_body_verification_command_success_boundary_v2
)
resolve_portable_source_body_verification_command_success_boundary_from_path = (
    resolve_portable_source_body_verification_command_success_boundary_v2_from_path
)
write_portable_source_body_verification_command_success_boundary_result = (
    write_portable_source_body_verification_command_success_boundary_v2_result
)
build_portable_source_body_verification_command_success_boundary_summary = (
    build_portable_source_body_verification_command_success_boundary_v2_summary
)
build_declared_portable_source_body_verification_command_success_boundary_request = (
    build_declared_portable_source_body_verification_command_success_boundary_v2_request
)
