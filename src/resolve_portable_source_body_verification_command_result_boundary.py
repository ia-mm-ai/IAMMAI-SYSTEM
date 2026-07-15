"""Resolve one bounded command result boundary posture.

This module is downstream of the recorded command output/report artifact line.
It records one future command-result-step boundary only. It does not create
command result, invent result body, create command success, infer pass, infer
fail, create source, authority, currentness, final completion, continuation,
reusable permission, derivative reception, vessel relation, another reception
request, deployment, runtime hosting, public release, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class PortableSourceBodyVerificationCommandResultBoundaryError(Exception):
    """Raised for explicit unreadable or contradictory result-boundary input."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_result_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "portable_source_body_verification_command_result_boundary_result"
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_result_boundary"
)

CORE_QUESTION = (
    "Can the recorded command output/report artifact basis be bounded for one "
    "future command result step without creating command result, creating command "
    "success, source, authority, currentness, final completion, continuation, "
    "reusable permission, derivative reception, vessel relation, another "
    "reception request, or follow-on work?"
)

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY"
SUPPORTED_INTENTS = frozenset({INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK})

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_BLOCKED"
OUTCOME_FAMILY = frozenset(
    {
        OUTCOME_RECORDED,
        OUTCOME_NOT_RECORDED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        OUTCOME_BLOCKED,
    }
)

COMMAND_RESULT_BOUNDARY_OUTCOME = OUTCOME_RECORDED
COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
)
COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_RECORDED"
)
OUTPUT_CAPTURE_V2_OUTCOME = "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
OUTPUT_CAPTURE_V2_VERSION = "0.2.0"
OUTPUT_CAPTURE_V2_RESULT_VERSION = OUTPUT_CAPTURE_V2_VERSION
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

SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE = frozenset(
    {
        "COMMAND_RESULT_BOUNDARY_ONLY",
        "ONE_FUTURE_COMMAND_RESULT_STEP_ONLY",
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
        "REPORT_BODY_NOT_INVENTED",
        "RESULT_BODY_NOT_INVENTED",
        "COMMAND_RESULT_NOT_CREATED",
        "COMMAND_SUCCESS_NOT_CREATED",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_RESULT",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_SUCCESS",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_SOURCE",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_AUTHORITY",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_CURRENTNESS",
        "COMMAND_RESULT_BOUNDARY_IS_NOT_FINAL_COMPLETION",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_RESULT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_SUCCESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_SOURCE",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_AUTHORITY",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_CURRENTNESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_IS_NOT_FINAL_COMPLETION",
        "REPORT_BODY_IS_NOT_RESULT",
        "REPORT_BODY_IS_NOT_SUCCESS",
        "REPORT_BODY_IS_NOT_SOURCE",
        "REPORT_BODY_IS_NOT_AUTHORITY",
        "REPORT_BODY_IS_NOT_CURRENTNESS",
        "REPORT_BODY_IS_NOT_FINAL_COMPLETION",
        "OUTPUT_CAPTURE_IS_NOT_RESULT",
        "OUTPUT_CAPTURE_IS_NOT_SUCCESS",
        "OUTPUT_CAPTURE_IS_NOT_SOURCE",
        "OUTPUT_CAPTURE_IS_NOT_AUTHORITY",
        "OUTPUT_CAPTURE_IS_NOT_CURRENTNESS",
        "OUTPUT_CAPTURE_IS_NOT_FINAL_COMPLETION",
        "EXECUTION_TRACE_IS_NOT_RESULT",
        "EXECUTION_TRACE_IS_NOT_SUCCESS",
        "EXECUTION_TRACE_IS_NOT_SOURCE",
        "EXECUTION_TRACE_IS_NOT_AUTHORITY",
        "NO_PASS_INFERENCE",
        "NO_FAIL_INFERENCE",
        "COMMAND_RESULT_NOT_AUTHORITY",
        "COMMAND_SUCCESS_NOT_CURRENTNESS",
        "COMMAND_SUCCESS_NOT_FINAL_COMPLETION",
        "AUTHORIZATION_TOKEN_REUSE_BLOCKED",
        "CONSUMED_REQUEST_TOKEN_REMAINS_CLOSED",
        "CONSUMED_REQUEST_NOT_REOPENED",
        "NO_AUTHORITY_CREATED",
        "NO_CURRENTNESS_CREATED",
        "NO_FINAL_COMPLETION",
        "NO_CONTINUATION_AUTHORIZED",
        "NO_REUSABLE_PERMISSION",
        "NO_FOLLOW_ON_WORK_AUTHORIZED",
        "V1_OUTPUT_CAPTURE_FAILURE_REMAINS_VISIBLE",
        "V1_OUTPUT_CAPTURE_NOT_REPAIRED",
        "V1_OUTPUT_CAPTURE_NOT_HIDDEN",
        "V1_OUTPUT_CAPTURE_NOT_CLAIMED_PASSED",
        "V2_OUTPUT_CAPTURE_SUCCESSOR_DOES_NOT_ERASE_V1",
        "COMMAND_REPORT_LINEAGE_NOT_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_NOT_COMMAND_RESULT",
        "V1_REQUEST_ADMISSION_PREDECESSOR_FAILURE_REMAINS_VISIBLE",
        "V2_SUCCESSOR_DOES_NOT_REPAIR_V1_REQUEST_ADMISSION",
        "RETURNED_RESULT_CONTAINMENT_PRESERVED",
        "REFERENCE_SHAPED_BASIS_REQUIRED",
        "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
    }
)

REQUIRED_FALSE_NON_CLAIMS = (
    "command_result_created",
    "result_body_invented",
    "command_success_created",
    "pass_inference_made",
    "fail_inference_made",
    "command_result_boundary_treated_as_result",
    "command_result_boundary_treated_as_success",
    "command_result_boundary_treated_as_source",
    "command_result_boundary_treated_as_authority",
    "command_result_boundary_treated_as_currentness",
    "command_result_boundary_treated_as_final_completion",
    "command_output_report_artifact_treated_as_result",
    "command_output_report_artifact_treated_as_success",
    "command_output_report_artifact_treated_as_source",
    "command_output_report_artifact_treated_as_authority",
    "command_output_report_artifact_treated_as_currentness",
    "command_output_report_artifact_treated_as_final_completion",
    "report_body_treated_as_result",
    "report_body_treated_as_success",
    "report_body_treated_as_source",
    "report_body_treated_as_authority",
    "report_body_treated_as_currentness",
    "report_body_treated_as_final_completion",
    "output_capture_treated_as_result",
    "output_capture_treated_as_success",
    "output_capture_treated_as_source",
    "output_capture_treated_as_authority",
    "output_capture_treated_as_currentness",
    "output_capture_treated_as_final_completion",
    "execution_trace_treated_as_result",
    "execution_trace_treated_as_success",
    "execution_trace_treated_as_source",
    "execution_trace_treated_as_authority",
    "command_result_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "authorization_token_reused",
    "consumed_request_reopened",
    "full_prior_artifacts_embedded",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
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
    "command_result_boundary_recorded",
    "one_future_command_result_step_declared",
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
    "report_body_not_invented",
    "result_body_not_invented",
    "command_result_still_not_created",
    "command_success_still_not_created",
    "pass_inference_blocked",
    "fail_inference_blocked",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "v1_request_admission_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

SELECTED_BASIS_KEYS = (
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
    "command_result_boundary_only_posture",
    "one_future_command_result_step_posture",
    "command_output_report_artifact_basis_preserved_posture",
    "bounded_command_output_report_artifact_preserved_posture",
    "command_output_report_artifact_boundary_basis_preserved_posture",
    "output_capture_v2_basis_preserved_posture",
    "output_capture_v1_predecessor_failure_preserved_posture",
    "bounded_output_capture_event_preserved_posture",
    "command_output_basis_preserved_posture",
    "execution_trace_audit_only_posture",
    "report_body_absent_or_bounded_posture",
    "no_report_body_invented_posture",
    "no_result_body_invented_posture",
    "no_command_result_posture",
    "no_command_success_posture",
    "no_pass_inference_posture",
    "no_fail_inference_posture",
    "no_artifact_as_source_posture",
    "no_result_as_authority_posture",
    "no_success_as_currentness_posture",
    "no_final_completion_posture",
    "authorization_token_reuse_blocked_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
)

RAW_BODY_KEYS = frozenset(
    {
        "full_prior_artifact_body",
        "raw_full_prior_artifact_body",
        "prior_artifact_body",
        "embedded_prior_artifact",
        "embedded_prior_artifacts",
        "raw_artifact_body",
        "report_body",
        "result_body",
        "success_body",
        "source_body",
        "authority_body",
        "currentness_claim",
        "final_completion_claim",
        "stdout",
        "stderr",
        "process_output",
        "raw_output_body",
        "command_output_body",
        "output_body",
    }
)

BLOCK_CODES = frozenset(
    {
        "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_MALFORMED",
        "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_UNREADABLE",
        "COMMAND_RESULT_BOUNDARY_QUESTION_UNDECLARED",
        "COMMAND_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
        "COMMAND_RESULT_BOUNDARY_BLOCKED_BY_REQUEST",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_BOUNDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_INVENTED_REPORT_BODY",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_RESULT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_SUCCESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SOURCE",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_AUTHORITY",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_CURRENTNESS",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_FINAL_COMPLETION",
        "REPORT_BODY_TREATED_AS_RESULT",
        "REPORT_BODY_TREATED_AS_SUCCESS",
        "REPORT_BODY_TREATED_AS_SOURCE",
        "REPORT_BODY_TREATED_AS_AUTHORITY",
        "REPORT_BODY_TREATED_AS_CURRENTNESS",
        "REPORT_BODY_TREATED_AS_FINAL_COMPLETION",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_NOT_RECORDED",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_FAILED_CHECKS_PRESENT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_ALREADY_CREATED_RESULT",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_ALREADY_CREATED_SUCCESS",
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
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_RESULT",
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_SUCCESS",
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_SOURCE",
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_AUTHORITY",
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_CURRENTNESS",
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
        "RESULT_BODY_INVENTED",
        "COMMAND_RESULT_CREATED",
        "COMMAND_SUCCESS_CREATED",
        "PASS_INFERENCE_MADE",
        "FAIL_INFERENCE_MADE",
        "EXECUTION_TRACE_TREATED_AS_RESULT",
        "EXECUTION_TRACE_TREATED_AS_SUCCESS",
        "EXECUTION_TRACE_TREATED_AS_SOURCE",
        "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
        "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        "CONSUMED_REQUEST_REOPENED",
        "AUTHORIZATION_TOKEN_REUSED",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
        "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
        "V2_TREATED_AS_REPAIRING_V1_REQUEST_ADMISSION",
        "V1_REQUEST_ADMISSION_FAILURE_HIDDEN",
        "V1_REQUEST_ADMISSION_CLAIMED_PASSED",
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
        "COMMAND_REPORT_LINEAGE_BASIS_MISSING",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT",
        "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        "COMMAND_BOUNDARY_BASIS_MISSING",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        "COMMAND_RESULT_BOUNDARY_ONLY_POSTURE_MISSING",
        "ONE_FUTURE_COMMAND_RESULT_STEP_POSTURE_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING",
        "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING",
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING",
        "OUTPUT_CAPTURE_V2_BASIS_PRESERVED_POSTURE_MISSING",
        "OUTPUT_CAPTURE_V1_PREDECESSOR_FAILURE_PRESERVED_POSTURE_MISSING",
        "BOUNDED_OUTPUT_CAPTURE_EVENT_PRESERVED_POSTURE_MISSING",
        "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
        "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
        "REPORT_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
        "NO_REPORT_BODY_INVENTED_POSTURE_MISSING",
        "NO_RESULT_BODY_INVENTED_POSTURE_MISSING",
        "NO_COMMAND_RESULT_POSTURE_MISSING",
        "NO_COMMAND_SUCCESS_POSTURE_MISSING",
        "NO_PASS_INFERENCE_POSTURE_MISSING",
        "NO_FAIL_INFERENCE_POSTURE_MISSING",
        "NO_ARTIFACT_AS_SOURCE_POSTURE_MISSING",
        "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
        "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
        "NO_FINAL_COMPLETION_POSTURE_MISSING",
        "UNSUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE",
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        "ARTIFACTS_MUTATED",
        "DEPLOYMENT_CREATED",
        "RUNTIME_HOSTING_CREATED",
        "PUBLIC_RELEASE_CREATED",
        "OPERATION_CREATED",
        "PUBLIC_READINESS_CREATED",
        "FINAL_COMPLETION_CLAIMED",
        "CONTINUATION_AUTHORIZED",
        "REUSABLE_PERMISSION_CREATED",
        "DERIVATIVE_RECEPTION_AUTHORIZED",
        "VESSEL_RELATION_AUTHORIZED",
        "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
        "FOLLOW_ON_WORK_AUTHORIZED",
        "MUTATION_REPLAY_OR_MERGE_DETECTED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    }
)

OPEN_ITEMS = (
    "command result boundary test",
    "command result boundary live artifact",
    "command result step, if separately specified",
    "command result",
    "command success",
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
    "final completion",
    "continuation",
    "publication flow",
    "reusable permission",
    "successor reception request",
    "follow-on work",
)

ZERO_FAILED_BASIS = (
    ("selected_output_capture_boundary_basis", "OUTPUT_CAPTURE_BOUNDARY_BASIS_MISSING"),
    ("selected_command_output_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
    ("selected_command_output_boundary_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
    ("selected_command_output_containment_basis", "COMMAND_OUTPUT_BASIS_MISSING"),
    (
        "selected_post_invocation_command_execution_basis",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
    ),
    (
        "selected_post_invocation_command_execution_terminal_summary_basis",
        "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
    ),
    ("selected_command_invocation_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected_command_execution_review_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected_request_consumption_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected_consumed_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected_v2_admitted_request_basis", "V2_ADMITTED_REQUEST_BASIS_MISSING"),
    ("selected_v1_predecessor_failure_basis", "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
    (
        "selected_older_command_execution_boundary_lineage_basis",
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    ),
    ("selected_command_report_lineage_basis", "COMMAND_REPORT_LINEAGE_BASIS_MISSING"),
    ("selected_command_implementation_boundary_basis", "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
    ("selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
    ("selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
    ("selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
    ("selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
)

POSTURE_BLOCK_CODES = {
    "command_result_boundary_only_posture": "COMMAND_RESULT_BOUNDARY_ONLY_POSTURE_MISSING",
    "one_future_command_result_step_posture": "ONE_FUTURE_COMMAND_RESULT_STEP_POSTURE_MISSING",
    "command_output_report_artifact_basis_preserved_posture": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "bounded_command_output_report_artifact_preserved_posture": (
        "BOUNDED_COMMAND_OUTPUT_REPORT_ARTIFACT_PRESERVED_POSTURE_MISSING"
    ),
    "command_output_report_artifact_boundary_basis_preserved_posture": (
        "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_PRESERVED_POSTURE_MISSING"
    ),
    "output_capture_v2_basis_preserved_posture": "OUTPUT_CAPTURE_V2_BASIS_PRESERVED_POSTURE_MISSING",
    "output_capture_v1_predecessor_failure_preserved_posture": (
        "OUTPUT_CAPTURE_V1_PREDECESSOR_FAILURE_PRESERVED_POSTURE_MISSING"
    ),
    "bounded_output_capture_event_preserved_posture": "BOUNDED_OUTPUT_CAPTURE_EVENT_PRESERVED_POSTURE_MISSING",
    "command_output_basis_preserved_posture": "COMMAND_OUTPUT_BASIS_PRESERVED_POSTURE_MISSING",
    "execution_trace_audit_only_posture": "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
    "report_body_absent_or_bounded_posture": "REPORT_BODY_ABSENT_OR_BOUNDED_POSTURE_MISSING",
    "no_report_body_invented_posture": "NO_REPORT_BODY_INVENTED_POSTURE_MISSING",
    "no_result_body_invented_posture": "NO_RESULT_BODY_INVENTED_POSTURE_MISSING",
    "no_command_result_posture": "NO_COMMAND_RESULT_POSTURE_MISSING",
    "no_command_success_posture": "NO_COMMAND_SUCCESS_POSTURE_MISSING",
    "no_pass_inference_posture": "NO_PASS_INFERENCE_POSTURE_MISSING",
    "no_fail_inference_posture": "NO_FAIL_INFERENCE_POSTURE_MISSING",
    "no_artifact_as_source_posture": "NO_ARTIFACT_AS_SOURCE_POSTURE_MISSING",
    "no_result_as_authority_posture": "NO_RESULT_AS_AUTHORITY_POSTURE_MISSING",
    "no_success_as_currentness_posture": "NO_SUCCESS_AS_CURRENTNESS_POSTURE_MISSING",
    "no_final_completion_posture": "NO_FINAL_COMPLETION_POSTURE_MISSING",
    "authorization_token_reuse_blocked_posture": "AUTHORIZATION_TOKEN_REUSED",
    "consumed_token_closed_posture": "CONSUMED_REQUEST_REOPENED",
    "no_reopen_consumed_request_posture": "CONSUMED_REQUEST_REOPENED",
    "returned_result_containment_posture": "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
}

COLLAPSE_CHECKS = (
    (
        "command result boundary not result",
        ("command_result_boundary_treated_as_result",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_RESULT",
    ),
    (
        "command result boundary not success",
        ("command_result_boundary_treated_as_success",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_SUCCESS",
    ),
    (
        "command result boundary not source",
        ("command_result_boundary_treated_as_source",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_SOURCE",
    ),
    (
        "command result boundary not authority",
        ("command_result_boundary_treated_as_authority",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_AUTHORITY",
    ),
    (
        "command result boundary not currentness",
        ("command_result_boundary_treated_as_currentness",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_CURRENTNESS",
    ),
    (
        "command result boundary not final completion",
        ("command_result_boundary_treated_as_final_completion",),
        "COMMAND_RESULT_BOUNDARY_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        "command output/report artifact not result",
        ("command_output_report_artifact_treated_as_result",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_RESULT",
    ),
    (
        "command output/report artifact not success",
        ("command_output_report_artifact_treated_as_success",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SUCCESS",
    ),
    (
        "command output/report artifact not source",
        ("command_output_report_artifact_treated_as_source",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_SOURCE",
    ),
    (
        "command output/report artifact not authority",
        ("command_output_report_artifact_treated_as_authority",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_AUTHORITY",
    ),
    (
        "command output/report artifact not currentness",
        ("command_output_report_artifact_treated_as_currentness",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_CURRENTNESS",
    ),
    (
        "command output/report artifact not final completion",
        ("command_output_report_artifact_treated_as_final_completion",),
        "COMMAND_OUTPUT_REPORT_ARTIFACT_TREATED_AS_FINAL_COMPLETION",
    ),
    ("report body not invented", ("report_body_invented",), "COMMAND_OUTPUT_REPORT_ARTIFACT_INVENTED_REPORT_BODY"),
    ("report body not result", ("report_body_treated_as_result",), "REPORT_BODY_TREATED_AS_RESULT"),
    ("report body not success", ("report_body_treated_as_success",), "REPORT_BODY_TREATED_AS_SUCCESS"),
    ("report body not source", ("report_body_treated_as_source",), "REPORT_BODY_TREATED_AS_SOURCE"),
    ("report body not authority", ("report_body_treated_as_authority",), "REPORT_BODY_TREATED_AS_AUTHORITY"),
    ("report body not currentness", ("report_body_treated_as_currentness",), "REPORT_BODY_TREATED_AS_CURRENTNESS"),
    (
        "report body not final completion",
        ("report_body_treated_as_final_completion",),
        "REPORT_BODY_TREATED_AS_FINAL_COMPLETION",
    ),
    ("output capture not result", ("output_capture_treated_as_result",), "OUTPUT_CAPTURE_TREATED_AS_RESULT"),
    ("output capture not success", ("output_capture_treated_as_success",), "OUTPUT_CAPTURE_TREATED_AS_SUCCESS"),
    ("output capture not source", ("output_capture_treated_as_source",), "OUTPUT_CAPTURE_TREATED_AS_SOURCE"),
    ("output capture not authority", ("output_capture_treated_as_authority",), "OUTPUT_CAPTURE_TREATED_AS_AUTHORITY"),
    (
        "output capture not currentness",
        ("output_capture_treated_as_currentness",),
        "OUTPUT_CAPTURE_TREATED_AS_CURRENTNESS",
    ),
    (
        "output capture not final completion",
        ("output_capture_treated_as_final_completion",),
        "OUTPUT_CAPTURE_TREATED_AS_FINAL_COMPLETION",
    ),
    ("result body not invented", ("result_body_invented",), "RESULT_BODY_INVENTED"),
    ("command result not created", ("command_result_created",), "COMMAND_RESULT_CREATED"),
    ("command success not created", ("command_success_created",), "COMMAND_SUCCESS_CREATED"),
    ("pass inference not made", ("pass_inference_made",), "PASS_INFERENCE_MADE"),
    ("fail inference not made", ("fail_inference_made",), "FAIL_INFERENCE_MADE"),
    ("execution trace not result", ("execution_trace_treated_as_result",), "EXECUTION_TRACE_TREATED_AS_RESULT"),
    ("execution trace not success", ("execution_trace_treated_as_success",), "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
    ("execution trace not source", ("execution_trace_treated_as_source",), "EXECUTION_TRACE_TREATED_AS_SOURCE"),
    ("execution trace not authority", ("execution_trace_treated_as_authority",), "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
    ("command result not authority", ("command_result_became_authority",), "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    (
        "command success not currentness",
        ("command_success_created_currentness",),
        "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
    ),
    (
        "command success not final completion",
        ("command_success_claimed_final_completion",),
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    ),
    ("consumed request not reopened", ("consumed_request_reopened",), "CONSUMED_REQUEST_REOPENED"),
    ("authorization token not reused", ("authorization_token_reused",), "AUTHORIZATION_TOKEN_REUSED"),
    (
        "earlier v2 did not repair v1 request admission",
        ("v2_treated_as_repairing_v1_request_admission",),
        "V2_TREATED_AS_REPAIRING_V1_REQUEST_ADMISSION",
    ),
    (
        "earlier v1 request-admission failure not hidden",
        ("v1_request_admission_failure_hidden",),
        "V1_REQUEST_ADMISSION_FAILURE_HIDDEN",
    ),
    (
        "earlier v1 request-admission failure not claimed passed",
        ("v1_request_admission_claimed_passed",),
        "V1_REQUEST_ADMISSION_CLAIMED_PASSED",
    ),
    (
        "command report lineage not current report artifact",
        ("command_report_lineage_basis_treated_as_current_report_artifact",),
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT",
    ),
    (
        "command report lineage not command result",
        ("command_report_lineage_basis_treated_as_command_result",),
        "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT",
    ),
    (
        "older command execution boundary lineage not current execution",
        ("older_command_execution_boundary_lineage_treated_as_current_execution",),
        "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
    ),
    (
        "full prior artifact body not emitted",
        ("full_prior_artifacts_embedded", "raw_full_prior_artifact_body_returned"),
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    ),
    ("artifacts not mutated", ("prior_artifacts_mutated",), "ARTIFACTS_MUTATED"),
    ("deployment not created", ("deployment_created",), "DEPLOYMENT_CREATED"),
    ("runtime hosting not created", ("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
    ("public release not created", ("public_release_created",), "PUBLIC_RELEASE_CREATED"),
    ("operation not created", ("operation_permission_created",), "OPERATION_CREATED"),
    ("public readiness not created", ("public_launch_readiness_created",), "PUBLIC_READINESS_CREATED"),
    ("final completion not claimed", ("final_completion_claimed",), "FINAL_COMPLETION_CLAIMED"),
    ("continuation not authorized", ("continuation_authorized",), "CONTINUATION_AUTHORIZED"),
    ("reusable permission not created", ("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
    (
        "derivative reception not authorized",
        ("derivative_reception_authorized",),
        "DERIVATIVE_RECEPTION_AUTHORIZED",
    ),
    ("vessel relation not authorized", ("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
    (
        "another reception request not authorized",
        ("another_reception_request_authorized",),
        "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
    ),
    ("follow-on work not authorized", ("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        "mutation replay or merge not performed",
        ("mutation_performed", "replay_performed", "merge_performed"),
        "MUTATION_REPLAY_OR_MERGE_DETECTED",
    ),
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (set, frozenset)):
        return [_json_safe(item) for item in sorted(value, key=str)]
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _sanitize_reference(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in RAW_BODY_KEYS:
                result[key_text] = {
                    "raw_full_prior_artifact_body_omitted": True,
                    "reason": "selected basis and command result boundary must remain bounded",
                }
            else:
                result[key_text] = _sanitize_reference(item)
        return result
    if isinstance(value, (list, tuple)):
        return [_sanitize_reference(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [_sanitize_reference(item) for item in sorted(value, key=str)]
    if isinstance(value, Path):
        return str(value)
    return copy.deepcopy(value)


def _mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _present(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    if isinstance(value, (list, tuple, set, frozenset, dict)) and not value:
        return False
    return True


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


def _find(mapping: Mapping[str, Any], names: Sequence[str], default: Any = None) -> Any:
    for name in names:
        if name in mapping:
            return mapping[name]
    return default


def _deep_find(value: Any, names: Iterable[str], default: Any = None) -> Any:
    name_set = set(names)
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in name_set:
                return item
        for item in value.values():
            found = _deep_find(item, name_set, default)
            if found is not default:
                return found
    elif isinstance(value, (list, tuple)):
        for item in value:
            found = _deep_find(item, name_set, default)
            if found is not default:
                return found
    return default


def _deep_any_true(value: Any, names: Iterable[str]) -> bool:
    name_set = set(names)
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in name_set and item is True:
                return True
            if _deep_any_true(item, name_set):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_deep_any_true(item, name_set) for item in value)
    return False


def _deep_key_present(value: Any, names: Iterable[str]) -> bool:
    name_set = set(names)
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in name_set and _present(item):
                return True
            if _deep_key_present(item, name_set):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_deep_key_present(item, name_set) for item in value)
    return False


def _basis_declared(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    return bool(
        value.get("declared") is True
        or value.get("basis_declared") is True
        or value.get("terminal_summary_declared") is True
        or value.get("selected_basis_declared") is True
        or value.get("reference_shaped_basis") is True
        or value.get("basis_remains_reference_shaped") is True
        or value.get("path")
        or value.get("artifact_path")
        or value.get("result_path")
        or value
    )


def _posture_declared(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    return bool(
        value.get("declared") is True
        or value.get("posture_declared") is True
        or value.get("preserved") is True
        or value.get("posture") is not None
        or value
    )


def _outcome(value: Any) -> Any:
    return _find(_mapping(value), ("outcome", "result_outcome", "selected_outcome"))


def _version(value: Any) -> Any:
    return _find(
        _mapping(value),
        (
            "result_version",
            "portable_source_body_verification_output_capture_result_version",
            "portable_source_body_verification_command_output_report_artifact_result_version",
            "version",
        ),
    )


def _failed_check_count(value: Any) -> int | None:
    return _to_int(
        _find(
            _mapping(value),
            (
                "failed_check_count",
                "failed_checks",
                "selected_failed_check_count",
                "selected_output_capture_v2_failed_check_count",
                "selected_command_output_report_artifact_failed_check_count",
                "selected_command_output_report_artifact_boundary_failed_check_count",
            ),
        )
    )


def _reference_shaped(value: Any) -> bool:
    if not isinstance(value, Mapping):
        return False
    return bool(
        value.get("reference_shaped_basis") is True
        or value.get("basis_remains_reference_shaped") is True
        or value.get("selected_basis_is_reference_shaped") is True
        or value.get("path")
        or value.get("artifact_path")
        or value.get("result_path")
        or not _deep_key_present(value, RAW_BODY_KEYS)
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


def _non_claims_false(non_claims: Any) -> bool:
    if not isinstance(non_claims, Mapping):
        return False
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _json_safe(expected_posture),
            "actual_posture": _json_safe(actual_posture),
            "block_code": None if passed else block_code,
            "failure_code": None if passed else block_code,
        }
    )


def _copy_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    source = request.get(key, {})
    copied = _sanitize_reference(source)
    if not isinstance(copied, Mapping):
        copied = {"selected_basis": copied}
    result = dict(copied)
    result.setdefault("basis_declared", _basis_declared(source))
    result.setdefault("basis_remains_reference_shaped", _reference_shaped(source))
    result.setdefault("raw_full_prior_artifact_body_emitted", False)
    return result


def _posture_section(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    source = request.get(key, {})
    copied = _sanitize_reference(source if isinstance(source, Mapping) else {})
    result = dict(copied) if isinstance(copied, Mapping) else {}
    result.setdefault("posture_declared", _posture_declared(source))
    result.setdefault("report_body_absent_or_bounded", True)
    result.setdefault("report_body_not_invented", True)
    result.setdefault("result_body_not_invented", True)
    for false_key in REQUIRED_FALSE_NON_CLAIMS:
        result.setdefault(false_key, False)
    result.setdefault("command_result_still_not_created", True)
    result.setdefault("command_success_still_not_created", True)
    result.setdefault("pass_inference_blocked", True)
    result.setdefault("fail_inference_blocked", True)
    result.setdefault("execution_trace_audit_only", True)
    result.setdefault("authorization_token_reuse_blocked", True)
    result.setdefault("consumed_request_token_remains_closed", True)
    result.setdefault("returned_result_containment_preserved", True)
    return result


def _selected_command_output_report_artifact_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _copy_section(request, "selected_command_output_report_artifact_basis")
    basis = _mapping(request.get("selected_command_output_report_artifact_basis"))
    section.setdefault(
        "selected_command_output_report_artifact_result_id",
        request.get("selected_command_output_report_artifact_result_id"),
    )
    if request.get("selected_command_output_report_artifact_result_path") is not None:
        section.setdefault(
            "selected_command_output_report_artifact_result_path",
            str(request.get("selected_command_output_report_artifact_result_path")),
        )
    section.setdefault(
        "outcome",
        request.get("selected_command_output_report_artifact_result_outcome") or _outcome(basis),
    )
    section.setdefault(
        "failed_check_count",
        request.get("selected_command_output_report_artifact_failed_check_count")
        if request.get("selected_command_output_report_artifact_failed_check_count") is not None
        else _failed_check_count(basis),
    )
    section.setdefault(
        "command_output_report_artifact_recorded",
        request.get("selected_command_output_report_artifact_recorded")
        if request.get("selected_command_output_report_artifact_recorded") is not None
        else _deep_find(section, ("command_output_report_artifact_recorded",)),
    )
    section.setdefault(
        "bounded_command_output_report_artifact_recorded",
        _deep_find(section, ("bounded_command_output_report_artifact_recorded",)),
    )
    section.setdefault(
        "report_body_absent_or_bounded",
        _deep_find(section, ("report_body_absent_or_bounded",)),
    )
    section.setdefault("report_body_not_invented", _deep_find(section, ("report_body_not_invented",)))
    section.setdefault(
        "report_body_invented",
        request.get("selected_command_output_report_artifact_report_body_invented")
        if request.get("selected_command_output_report_artifact_report_body_invented") is not None
        else _deep_find(section, ("report_body_invented",), False),
    )
    section.setdefault(
        "command_result_created",
        request.get("selected_command_output_report_artifact_already_created_result")
        if request.get("selected_command_output_report_artifact_already_created_result") is not None
        else _deep_find(section, ("command_result_created",), False),
    )
    section.setdefault(
        "command_success_created",
        request.get("selected_command_output_report_artifact_already_created_success")
        if request.get("selected_command_output_report_artifact_already_created_success") is not None
        else _deep_find(section, ("command_success_created",), False),
    )
    section.setdefault("artifact_remains_artifact_posture_only", True)
    return section


def _selected_command_output_report_artifact_boundary_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _copy_section(request, "selected_command_output_report_artifact_boundary_basis")
    basis = _mapping(request.get("selected_command_output_report_artifact_boundary_basis"))
    if request.get("selected_command_output_report_artifact_boundary_result_path") is not None:
        section.setdefault(
            "selected_command_output_report_artifact_boundary_result_path",
            str(request.get("selected_command_output_report_artifact_boundary_result_path")),
        )
    section.setdefault(
        "outcome",
        request.get("selected_command_output_report_artifact_boundary_result_outcome")
        or _outcome(basis),
    )
    section.setdefault(
        "failed_check_count",
        request.get("selected_command_output_report_artifact_boundary_failed_check_count")
        if request.get("selected_command_output_report_artifact_boundary_failed_check_count")
        is not None
        else _failed_check_count(basis),
    )
    section.setdefault(
        "one_future_command_output_report_artifact_step_declared",
        _deep_find(
            section,
            (
                "one_future_command_output_report_artifact_step_declared",
                "one_future_report_artifact_step_declared",
                "command_output_report_artifact_boundary_step_declared",
            ),
        ),
    )
    section.setdefault("command_result_created", _deep_find(section, ("command_result_created",), False))
    section.setdefault("command_success_created", _deep_find(section, ("command_success_created",), False))
    section.setdefault("boundary_remains_boundary_only", True)
    return section


def _selected_output_capture_v2_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _copy_section(request, "selected_output_capture_v2_basis")
    basis = _mapping(request.get("selected_output_capture_v2_basis"))
    shortcuts = {
        "selected_output_capture_v2_result_id": request.get("selected_output_capture_v2_result_id"),
        "selected_output_capture_v2_result_path": request.get("selected_output_capture_v2_result_path"),
        "outcome": request.get("selected_output_capture_v2_result_outcome") or _outcome(basis),
        "result_version": request.get("selected_output_capture_v2_result_version") or _version(basis),
        "failed_check_count": request.get("selected_output_capture_v2_failed_check_count")
        if request.get("selected_output_capture_v2_failed_check_count") is not None
        else _failed_check_count(basis),
        "json_safe_result": request.get("selected_output_capture_v2_json_safe_result")
        if request.get("selected_output_capture_v2_json_safe_result") is not None
        else _deep_find(section, ("json_safe_result",)),
        "v1_predecessor_failure_preserved": request.get(
            "selected_output_capture_v2_v1_predecessor_failure_preserved"
        )
        if request.get("selected_output_capture_v2_v1_predecessor_failure_preserved") is not None
        else _deep_find(section, ("v1_predecessor_failure_preserved",)),
        "v1_repaired": request.get("selected_output_capture_v2_v1_repaired")
        if request.get("selected_output_capture_v2_v1_repaired") is not None
        else _deep_find(section, ("v1_repaired", "v1_output_capture_repaired"), False),
        "v1_hidden": request.get("selected_output_capture_v2_v1_hidden")
        if request.get("selected_output_capture_v2_v1_hidden") is not None
        else _deep_find(section, ("v1_hidden", "v1_output_capture_hidden"), False),
        "v1_claimed_passed": request.get("selected_output_capture_v2_v1_claimed_passed")
        if request.get("selected_output_capture_v2_v1_claimed_passed") is not None
        else _deep_find(section, ("v1_claimed_passed", "v1_output_capture_claimed_passed"), False),
        "v2_successor_does_not_erase_v1": _deep_find(section, ("v2_successor_does_not_erase_v1",)),
        "stdout_content_invented": request.get("selected_output_capture_v2_invented_stdout_content")
        if request.get("selected_output_capture_v2_invented_stdout_content") is not None
        else _deep_find(section, ("stdout_content_invented",), False),
        "stderr_content_invented": request.get("selected_output_capture_v2_invented_stderr_content")
        if request.get("selected_output_capture_v2_invented_stderr_content") is not None
        else _deep_find(section, ("stderr_content_invented",), False),
        "process_output_content_invented": request.get(
            "selected_output_capture_v2_invented_process_output_content"
        )
        if request.get("selected_output_capture_v2_invented_process_output_content") is not None
        else _deep_find(section, ("process_output_content_invented",), False),
        "raw_output_body_content_invented": request.get(
            "selected_output_capture_v2_invented_raw_output_body_content"
        )
        if request.get("selected_output_capture_v2_invented_raw_output_body_content") is not None
        else _deep_find(section, ("raw_output_body_content_invented",), False),
    }
    for key, value in shortcuts.items():
        if key.endswith("_path") and value is not None:
            value = str(value)
        section.setdefault(key, value)
    section.setdefault("successor_of", "resolve_portable_source_body_verification_output_capture")
    section.setdefault("output_capture_v2_remains_output_capture_posture_only", True)
    return section


def _selected_v1_failure_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _copy_section(request, "selected_output_capture_v1_predecessor_failure_basis")
    section.setdefault(
        "selected_output_capture_v1_predecessor_path",
        str(request.get("selected_output_capture_v1_predecessor_path"))
        if request.get("selected_output_capture_v1_predecessor_path") is not None
        else None,
    )
    section.setdefault("v1_output_capture_predecessor_failure_preserved", True)
    section.setdefault("v1_output_capture_repaired", False)
    section.setdefault("v1_output_capture_hidden", False)
    section.setdefault("v1_output_capture_claimed_passed", False)
    section.setdefault("v2_output_capture_erased_v1", False)
    section.setdefault("predecessor_failure_basis_only", True)
    return section


def _selected_prior_basis(request: Mapping[str, Any], key: str) -> dict[str, Any]:
    section = _copy_section(request, key)
    shortcut_name = f"{key.removeprefix('selected_')}_result_path"
    if request.get(shortcut_name) is not None:
        section.setdefault("result_path", str(request.get(shortcut_name)))
    return section


def _build_statement(recorded: bool) -> dict[str, Any]:
    statement = {field: bool(recorded) for field in ALLOWED_TRUE_RECORDED_FIELDS}
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    statement.update(
        {
            "command_result_exists": False,
            "result_body_exists": False,
            "command_success_exists": False,
            "report_body_invented": False,
            "v1_request_admission_repaired": False,
            "v1_request_admission_hidden": False,
            "v1_request_admission_claimed_passed": False,
        }
    )
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "command_result_exists": False,
        "result_body_exists": False,
        "command_success_exists": False,
        "pass_was_inferred": False,
        "fail_was_inferred": False,
        "boundary_is_result": False,
        "boundary_is_success": False,
        "boundary_is_source": False,
        "boundary_is_authority": False,
        "boundary_is_currentness": False,
        "boundary_is_final_completion": False,
        "artifact_is_result": False,
        "artifact_is_success": False,
        "artifact_is_source": False,
        "artifact_is_authority": False,
        "artifact_is_currentness": False,
        "artifact_is_final_completion": False,
        "report_body_is_result": False,
        "report_body_is_success": False,
        "report_body_is_source": False,
        "report_body_is_authority": False,
        "report_body_is_currentness": False,
        "report_body_is_final_completion": False,
        "output_capture_is_result": False,
        "output_capture_is_success": False,
        "output_capture_is_source": False,
        "output_capture_is_authority": False,
        "output_capture_is_currentness": False,
        "output_capture_is_final_completion": False,
        "execution_trace_is_result": False,
        "execution_trace_is_success": False,
        "execution_trace_is_source": False,
        "execution_trace_is_authority": False,
        "v1_output_capture_predecessor_repaired": False,
        "v1_output_capture_predecessor_hidden": False,
        "v1_output_capture_predecessor_passed": False,
        "v2_output_capture_erased_v1": False,
        "command_report_lineage_is_current_report_artifact": False,
        "command_report_lineage_is_command_result": False,
        "consumed_request_token_reopened": False,
        "authorization_token_reusable": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "public_readiness_created": False,
        "final_completion_claimed": False,
        "continuation_authorized": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
    }


def _basis_checks(request: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for key, block_code in ZERO_FAILED_BASIS:
        _check(
            checks,
            f"{key} declared",
            _basis_declared(request.get(key)),
            "basis declared and reference-shaped",
            {
                "declared": _basis_declared(request.get(key)),
                "reference_shaped": _reference_shaped(request.get(key))
                if isinstance(request.get(key), Mapping)
                else False,
            },
            block_code,
        )


def _build_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    artifact = _selected_command_output_report_artifact_basis(request)
    boundary = _selected_command_output_report_artifact_boundary_basis(request)
    output_capture_v2 = _selected_output_capture_v2_basis(request)
    scope = _scope_values(request.get("command_result_boundary_scope"))
    unsupported_scope = [item for item in scope if item not in SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE]

    primary_checks = (
        (
            "command result boundary question declared",
            _present(request.get("command_result_boundary_question")),
            "question declared",
            request.get("command_result_boundary_question"),
            "COMMAND_RESULT_BOUNDARY_QUESTION_UNDECLARED",
        ),
        (
            "command result boundary intent supported",
            request.get("command_result_boundary_intent") in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            request.get("command_result_boundary_intent"),
            "COMMAND_RESULT_BOUNDARY_INTENT_UNSUPPORTED",
        ),
        (
            "command result boundary scope supported",
            bool(scope) and not unsupported_scope,
            sorted(SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE),
            scope,
            "UNSUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE",
        ),
        (
            "command output/report artifact terminal summary basis declared",
            _basis_declared(request.get("selected_command_output_report_artifact_terminal_summary_basis")),
            "terminal summary basis declared",
            request.get("selected_command_output_report_artifact_terminal_summary_basis"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        ),
        (
            "command output/report artifact live artifact basis declared",
            _basis_declared(request.get("selected_command_output_report_artifact_basis")),
            "artifact basis declared",
            request.get("selected_command_output_report_artifact_basis"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BASIS_MISSING",
        ),
        (
            "command output/report artifact outcome recorded",
            artifact.get("outcome") == COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME,
            COMMAND_OUTPUT_REPORT_ARTIFACT_OUTCOME,
            artifact.get("outcome"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_RECORDED",
        ),
        (
            "command output/report artifact failed check count zero",
            _to_int(artifact.get("failed_check_count")) == 0,
            0,
            artifact.get("failed_check_count"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_FAILED_CHECKS_PRESENT",
        ),
        (
            "command output/report artifact bounded artifact recorded",
            artifact.get("bounded_command_output_report_artifact_recorded") is True,
            True,
            artifact.get("bounded_command_output_report_artifact_recorded"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_NOT_BOUNDED",
        ),
        (
            "command output/report artifact report body absent or bounded",
            artifact.get("report_body_absent_or_bounded") is True,
            True,
            artifact.get("report_body_absent_or_bounded"),
            "REPORT_BODY_TREATED_AS_RESULT",
        ),
        (
            "command output/report artifact report body not invented",
            artifact.get("report_body_not_invented") is True
            and artifact.get("report_body_invented") is False,
            "not invented",
            {
                "report_body_not_invented": artifact.get("report_body_not_invented"),
                "report_body_invented": artifact.get("report_body_invented"),
            },
            "COMMAND_OUTPUT_REPORT_ARTIFACT_INVENTED_REPORT_BODY",
        ),
        (
            "command output/report artifact command result not created",
            artifact.get("command_result_created") is False,
            False,
            artifact.get("command_result_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_RESULT",
        ),
        (
            "command output/report artifact command success not created",
            artifact.get("command_success_created") is False,
            False,
            artifact.get("command_success_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_ALREADY_CREATED_SUCCESS",
        ),
        (
            "command output/report artifact boundary basis declared",
            _basis_declared(request.get("selected_command_output_report_artifact_boundary_basis")),
            "boundary basis declared",
            request.get("selected_command_output_report_artifact_boundary_basis"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_MISSING",
        ),
        (
            "command output/report artifact boundary outcome recorded",
            boundary.get("outcome") in (None, COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME),
            COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_OUTCOME,
            boundary.get("outcome"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_NOT_RECORDED",
        ),
        (
            "command output/report artifact boundary failed check count zero",
            _to_int(boundary.get("failed_check_count")) in (None, 0),
            0,
            boundary.get("failed_check_count"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_FAILED_CHECKS_PRESENT",
        ),
        (
            "command output/report artifact boundary one future report artifact step declared",
            boundary.get("one_future_command_output_report_artifact_step_declared") is True,
            True,
            boundary.get("one_future_command_output_report_artifact_step_declared"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_BASIS_MISSING",
        ),
        (
            "command output/report artifact boundary command result not created",
            boundary.get("command_result_created") is False,
            False,
            boundary.get("command_result_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_ALREADY_CREATED_RESULT",
        ),
        (
            "command output/report artifact boundary command success not created",
            boundary.get("command_success_created") is False,
            False,
            boundary.get("command_success_created"),
            "COMMAND_OUTPUT_REPORT_ARTIFACT_BOUNDARY_ALREADY_CREATED_SUCCESS",
        ),
    )
    for check_name, passed, expected, actual, code in primary_checks:
        _check(checks, check_name, passed, expected, actual, code)

    output_capture_checks = (
        (
            "output capture v2 basis declared",
            _basis_declared(request.get("selected_output_capture_v2_basis")),
            "output capture v2 basis declared",
            request.get("selected_output_capture_v2_basis"),
            "OUTPUT_CAPTURE_V2_BASIS_MISSING",
        ),
        (
            "output capture v2 outcome recorded",
            output_capture_v2.get("outcome") == OUTPUT_CAPTURE_V2_OUTCOME,
            OUTPUT_CAPTURE_V2_OUTCOME,
            output_capture_v2.get("outcome"),
            "OUTPUT_CAPTURE_V2_NOT_RECORDED",
        ),
        (
            "output capture v2 result version 0.2.0",
            str(output_capture_v2.get("result_version")) == OUTPUT_CAPTURE_V2_VERSION,
            OUTPUT_CAPTURE_V2_VERSION,
            output_capture_v2.get("result_version"),
            "OUTPUT_CAPTURE_V2_VERSION_NOT_0_2_0",
        ),
        (
            "output capture v2 failed check count zero",
            _to_int(output_capture_v2.get("failed_check_count")) == 0,
            0,
            output_capture_v2.get("failed_check_count"),
            "OUTPUT_CAPTURE_V2_FAILED_CHECKS_PRESENT",
        ),
        (
            "output capture v2 JSON-safe result preserved",
            output_capture_v2.get("json_safe_result") is True,
            True,
            output_capture_v2.get("json_safe_result"),
            "OUTPUT_CAPTURE_V2_JSON_SAFE_RESULT_NOT_PRESERVED",
        ),
        (
            "output capture v2 predecessor failure evidence preserved",
            output_capture_v2.get("v1_predecessor_failure_preserved") is True,
            True,
            output_capture_v2.get("v1_predecessor_failure_preserved"),
            "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING",
        ),
        (
            "output capture v2 v1 repaired false",
            output_capture_v2.get("v1_repaired") is False,
            False,
            output_capture_v2.get("v1_repaired"),
            "OUTPUT_CAPTURE_V2_REPAIRED_V1",
        ),
        (
            "output capture v2 v1 hidden false",
            output_capture_v2.get("v1_hidden") is False,
            False,
            output_capture_v2.get("v1_hidden"),
            "OUTPUT_CAPTURE_V2_HID_V1",
        ),
        (
            "output capture v2 v1 claimed passed false",
            output_capture_v2.get("v1_claimed_passed") is False,
            False,
            output_capture_v2.get("v1_claimed_passed"),
            "OUTPUT_CAPTURE_V2_CLAIMED_V1_PASSED",
        ),
        (
            "output capture v2 does not erase v1",
            output_capture_v2.get("v2_successor_does_not_erase_v1") is True,
            True,
            output_capture_v2.get("v2_successor_does_not_erase_v1"),
            "OUTPUT_CAPTURE_V2_ERASED_V1",
        ),
    )
    for check_name, passed, expected, actual, code in output_capture_checks:
        _check(checks, check_name, passed, expected, actual, code)

    for field_name, code in (
        ("stdout_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDOUT_CONTENT"),
        ("stderr_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_STDERR_CONTENT"),
        ("process_output_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_PROCESS_OUTPUT_CONTENT"),
        ("raw_output_body_content_invented", "OUTPUT_CAPTURE_V2_INVENTED_RAW_OUTPUT_BODY_CONTENT"),
    ):
        _check(
            checks,
            f"output capture v2 {field_name} false",
            output_capture_v2.get(field_name) is False,
            False,
            output_capture_v2.get(field_name),
            code,
        )

    _check(
        checks,
        "output capture v2 terminal summary basis declared",
        _basis_declared(request.get("selected_output_capture_v2_terminal_summary_basis")),
        "terminal summary basis declared",
        request.get("selected_output_capture_v2_terminal_summary_basis"),
        "OUTPUT_CAPTURE_V2_BASIS_MISSING",
    )
    _check(
        checks,
        "output capture v1 predecessor failure basis declared",
        _basis_declared(request.get("selected_output_capture_v1_predecessor_failure_basis")),
        "v1 output capture predecessor failure basis declared",
        request.get("selected_output_capture_v1_predecessor_failure_basis"),
        "OUTPUT_CAPTURE_V2_PREDECESSOR_FAILURE_EVIDENCE_MISSING",
    )
    _basis_checks(request, checks)

    post_invocation = _mapping(request.get("selected_post_invocation_command_execution_basis", {}))
    consumed = _mapping(request.get("selected_consumed_request_basis", {}))
    v2_admitted = _mapping(request.get("selected_v2_admitted_request_basis", {}))
    older_lineage = _mapping(request.get("selected_older_command_execution_boundary_lineage_basis", {}))
    command_report = _mapping(request.get("selected_command_report_lineage_basis", {}))

    basis_shape_checks = (
        (
            "post-invocation command execution recorded",
            _outcome(post_invocation) in (None, POST_INVOCATION_COMMAND_EXECUTION_OUTCOME)
            and _basis_declared(post_invocation),
            POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
            _outcome(post_invocation),
            "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
        ),
        (
            "post-invocation command execution failed check count zero",
            _failed_check_count(post_invocation) in (None, 0),
            0,
            _failed_check_count(post_invocation),
            "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
        ),
        (
            "post-invocation command execution trace audit-only",
            _deep_find(post_invocation, ("execution_trace_audit_only",), True) is True,
            True,
            _deep_find(post_invocation, ("execution_trace_audit_only",), True),
            "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
        ),
        (
            "consumed request token remains closed",
            _deep_find(consumed, ("consumed_request_token_remains_closed", "consumption_token_closed"), True)
            is True
            and _deep_find(consumed, ("consumed_request_reopened", "consumed_request_is_reopened"), False)
            is False,
            "closed consumed request token",
            _sanitize_reference(consumed),
            "CONSUMED_REQUEST_REOPENED",
        ),
        (
            "v2 admitted request failed check count zero",
            _failed_check_count(v2_admitted) in (None, 0),
            0,
            _failed_check_count(v2_admitted),
            "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
        ),
        (
            "older command execution boundary lineage not current execution",
            _deep_find(
                older_lineage,
                ("older_command_execution_boundary_lineage_treated_as_current_execution",),
                False,
            )
            is False
            and _deep_find(older_lineage, ("lineage_basis_not_treated_as_current_execution",), True)
            is True,
            "prior scaffolding only",
            _sanitize_reference(older_lineage),
            "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
        ),
        (
            "command report lineage basis not current report artifact",
            _deep_find(command_report, ("current_report_artifact",), False) is False
            and _deep_find(
                command_report,
                ("command_report_lineage_basis_treated_as_current_report_artifact",),
                False,
            )
            is False,
            "lineage only",
            _sanitize_reference(command_report),
            "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_CURRENT_REPORT_ARTIFACT",
        ),
        (
            "command report lineage basis not command result",
            _deep_find(
                command_report,
                ("command_report_lineage_basis_treated_as_command_result",),
                False,
            )
            is False,
            "lineage only, not command result",
            _sanitize_reference(command_report),
            "COMMAND_REPORT_LINEAGE_BASIS_TREATED_AS_COMMAND_RESULT",
        ),
    )
    for check_name, passed, expected, actual, code in basis_shape_checks:
        _check(checks, check_name, passed, expected, actual, code)

    for key in POSTURE_KEYS:
        _check(
            checks,
            f"{key} declared",
            _posture_declared(request.get(key)),
            "posture declared",
            {"declared": _posture_declared(request.get(key))},
            POSTURE_BLOCK_CODES[key],
        )
    for check_name, names, code in COLLAPSE_CHECKS:
        actual = _deep_any_true(request, names)
        _check(checks, check_name, not actual, False, actual, code)
    _check(
        checks,
        "raw full prior artifact body not present",
        not _deep_key_present(request, RAW_BODY_KEYS),
        "reference-shaped basis without raw bodies",
        "raw body key present" if _deep_key_present(request, RAW_BODY_KEYS) else False,
        "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
    )
    _check(
        checks,
        "required non-claims remain false",
        _non_claims_false(request.get("declared_non_claims")),
        {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        _sanitize_reference(request.get("declared_non_claims")),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _first_failure(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _determine_outcome(
    request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]
) -> tuple[str, str | None, str | None]:
    intent = request.get("command_result_boundary_intent")
    first_failure = _first_failure(checks)
    if intent == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            "COMMAND_RESULT_BOUNDARY_BLOCKED_BY_REQUEST",
            "request declared blocked command result boundary posture",
        )
    if first_failure is not None:
        return (
            OUTCOME_BLOCKED,
            str(first_failure.get("block_code") or first_failure.get("failure_code")),
            str(first_failure.get("check_name")),
        )
    requested = request.get("requested_command_result_boundary_outcome")
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS or request.get("additional_basis_context"):
        return (OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None)
    if intent == INTENT_DO_NOT_RECORD or requested == OUTCOME_NOT_RECORDED or request.get("not_recorded_basis"):
        return (OUTCOME_NOT_RECORDED, None, None)
    return (OUTCOME_RECORDED, None, None)


def _metadata(request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    request_id = request.get(
        "command_result_boundary_request_id",
        "portable_source_body_verification_command_result_boundary_request",
    )
    return {
        "portable_source_body_verification_command_result_boundary_result_id": (
            f"{request_id}__portable_source_body_verification_command_result_boundary_result"
        ),
        "portable_source_body_verification_command_result_boundary_result_type": RESULT_TYPE,
        "portable_source_body_verification_command_result_boundary_result_version": RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "governing_specification": "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_BOUNDARY_V0_MIN_SPEC.md",
        "successor_lineage_preserved_in_selected_basis": True,
        "short_resolver_filename_used_under_naming_containment": True,
        "command_output_report_artifact_basis_required": True,
        "output_capture_v2_successor_basis_required": True,
        "v1_output_capture_predecessor_failure_remains_visible": True,
        "creates_command_result": False,
        "invents_result_body": False,
        "creates_command_success": False,
        "infers_pass": False,
        "infers_fail": False,
        "passed_check_count": passed,
        "failed_check_count": len(checks) - passed,
    }


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": _sanitize_reference(request.get("additional_basis_context", {})),
        "missing_basis_is_not_scheduled": True,
        "missing_basis_is_not_authorized": True,
        "missing_basis_is_not_executed": True,
        "creates_command_result": False,
        "invents_result_body": False,
        "creates_command_success": False,
        "infers_pass": False,
        "infers_fail": False,
        "creates_authority": False,
        "creates_currentness": False,
        "claims_final_completion": False,
        "authorizes_follow_on_work": False,
    }


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference(request.get("not_recorded_basis", {})),
        "mutation_performed": False,
        "creates_command_result": False,
        "invents_result_body": False,
        "creates_command_success": False,
        "infers_pass": False,
        "infers_fail": False,
        "creates_authority": False,
        "creates_currentness": False,
        "claims_final_completion": False,
        "authorizes_follow_on_work": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": list(OPEN_ITEMS),
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _build_result(request: Mapping[str, Any]) -> dict[str, Any]:
    checks = _build_checks(request)
    outcome, block_code, block_reason = _determine_outcome(request, checks)
    recorded = outcome == OUTCOME_RECORDED
    result: dict[str, Any] = {
        "portable_source_body_verification_command_result_boundary_metadata": _metadata(
            request, checks
        ),
        "declared_command_result_boundary_question": {
            "command_result_boundary_request_id": request.get("command_result_boundary_request_id"),
            "question": request.get("command_result_boundary_question"),
            "canonical_question": CORE_QUESTION,
            "intent": request.get("command_result_boundary_intent"),
            "request_remains_reference_shaped": not _deep_key_present(request, RAW_BODY_KEYS),
        },
        "selected_command_output_report_artifact_basis": _selected_command_output_report_artifact_basis(
            request
        ),
        "selected_command_output_report_artifact_terminal_summary_basis": _copy_section(
            request,
            "selected_command_output_report_artifact_terminal_summary_basis",
        ),
        "selected_command_output_report_artifact_boundary_basis": (
            _selected_command_output_report_artifact_boundary_basis(request)
        ),
        "selected_command_output_report_artifact_boundary_terminal_summary_basis": _copy_section(
            request,
            "selected_command_output_report_artifact_boundary_terminal_summary_basis",
        ),
        "selected_output_capture_v2_basis": _selected_output_capture_v2_basis(request),
        "selected_output_capture_v2_terminal_summary_basis": _copy_section(
            request,
            "selected_output_capture_v2_terminal_summary_basis",
        ),
        "selected_output_capture_v1_predecessor_failure_basis": _selected_v1_failure_basis(request),
    }
    for key in SELECTED_BASIS_KEYS:
        result.setdefault(key, _selected_prior_basis(request, key))
    for key in POSTURE_KEYS:
        result[key] = _posture_section(request, key)

    scope = _scope_values(request.get("command_result_boundary_scope"))
    result["command_result_boundary_scope"] = {
        "declared_scope": scope,
        "supported_scope": sorted(SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE),
        "unsupported_scope": [
            item for item in scope if item not in SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE
        ],
        "scope_is_command_result_boundary_only": True,
        "one_future_command_result_step_only": True,
    }
    result["command_result_boundary_checks"] = checks
    result["command_result_boundary_statement"] = _build_statement(recorded)
    result["command_result_boundary_non_meaning"] = _build_non_meaning()
    result["additional_basis_required"] = _additional_basis_required(outcome, request)
    result["not_recorded_basis"] = _not_recorded_basis(outcome, request)
    result["what_remains_open"] = _what_remains_open()
    result["non_claims"] = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    result["outcome"] = outcome
    result["block"] = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "block_code": block_code,
        "block_reason": block_reason,
    }
    result["portable_source_body_verification_command_result_boundary_summary"] = (
        build_portable_source_body_verification_command_result_boundary_summary(result)
    )
    return _json_safe(result)


def _malformed_request_result(block_code: str, block_reason: str) -> dict[str, Any]:
    result = _build_result(
        {
            "command_result_boundary_request_id": None,
            "command_result_boundary_question": None,
            "command_result_boundary_intent": None,
            "command_result_boundary_scope": [],
            "declared_non_claims": {},
            "block_reason": block_reason,
        }
    )
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = {
        "blocked": True,
        "block_code": block_code,
        "block_reason": block_reason,
    }
    result["portable_source_body_verification_command_result_boundary_summary"] = (
        build_portable_source_body_verification_command_result_boundary_summary(result)
    )
    return result


def resolve_portable_source_body_verification_command_result_boundary(
    declared_command_result_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Return one bounded command result boundary result."""

    if declared_command_result_boundary_request is None:
        return _malformed_request_result(
            "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "declared command result boundary request missing",
        )
    if not isinstance(declared_command_result_boundary_request, Mapping):
        return _malformed_request_result(
            "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "declared command result boundary request is not a mapping",
        )
    return _build_result(copy.deepcopy(declared_command_result_boundary_request))


def resolve_portable_source_body_verification_command_result_boundary_from_path(
    declared_command_result_boundary_request_path: Path | str,
) -> dict[str, Any]:
    """Load one declared command result boundary request JSON object."""

    path = Path(declared_command_result_boundary_request_path)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return _malformed_request_result(
            "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_UNREADABLE",
            str(exc),
        )
    except json.JSONDecodeError as exc:
        return _malformed_request_result(
            "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_UNREADABLE",
            str(exc),
        )
    if not isinstance(loaded, Mapping):
        return _malformed_request_result(
            "DECLARED_COMMAND_RESULT_BOUNDARY_REQUEST_MALFORMED",
            "declared request JSON must be an object",
        )
    return resolve_portable_source_body_verification_command_result_boundary(
        declared_command_result_boundary_request=loaded
    )


def _safe_request_id(result: Mapping[str, Any]) -> str:
    question = _mapping(result.get("declared_command_result_boundary_question"))
    metadata = _mapping(result.get("portable_source_body_verification_command_result_boundary_metadata"))
    request_id = question.get("command_result_boundary_request_id") or metadata.get(
        "portable_source_body_verification_command_result_boundary_result_id",
        "portable_source_body_verification_command_result_boundary",
    )
    safe = "".join(
        character if character.isalnum() or character in ("-", "_") else "_"
        for character in str(request_id)
    ).strip("_")
    return safe or "portable_source_body_verification_command_result_boundary"


def _with_numeric_suffix(path: Path) -> Path:
    if not path.exists():
        return path
    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def write_portable_source_body_verification_command_result_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a JSON-safe command result boundary result additively."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandResultBoundaryError(
            "command result boundary result must be a mapping"
        )
    safe_result = _json_safe(copy.deepcopy(result))
    if output_path is None:
        request_id = _safe_request_id(safe_result)
        output_path = OUTPUT_ROOT / (
            f"{request_id}__portable_source_body_verification_command_result_boundary_result.json"
        )
    path = _with_numeric_suffix(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(safe_result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def build_portable_source_body_verification_command_result_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact JSON-safe summary for one command result boundary result."""

    metadata = _mapping(result.get("portable_source_body_verification_command_result_boundary_metadata"))
    question = _mapping(result.get("declared_command_result_boundary_question"))
    statement = _mapping(result.get("command_result_boundary_statement"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))
    checks = result.get("command_result_boundary_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes)):
        checks = []
    selected_artifact = _mapping(result.get("selected_command_output_report_artifact_basis"))
    selected_output_capture_v2 = _mapping(result.get("selected_output_capture_v2_basis"))
    selected_command_output = _mapping(result.get("selected_command_output_basis"))
    selected_post_invocation = _mapping(result.get("selected_post_invocation_command_execution_basis"))
    selected_v2_admitted = _mapping(result.get("selected_v2_admitted_request_basis"))
    selected_older_lineage = _mapping(result.get("selected_older_command_execution_boundary_lineage_basis"))
    selected_command_report_lineage = _mapping(result.get("selected_command_report_lineage_basis"))
    summary = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_id": question.get("command_result_boundary_request_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": metadata.get("passed_check_count"),
        "failed_check_count": metadata.get("failed_check_count"),
        "selected_command_output_report_artifact_outcome": selected_artifact.get("outcome"),
        "selected_command_output_report_artifact_failed_check_count": selected_artifact.get("failed_check_count"),
        "selected_output_capture_v2_outcome": selected_output_capture_v2.get("outcome"),
        "selected_output_capture_v2_result_version": selected_output_capture_v2.get("result_version"),
        "selected_output_capture_v2_failed_check_count": selected_output_capture_v2.get("failed_check_count"),
        "selected_output_capture_v2_json_safe_result": selected_output_capture_v2.get("json_safe_result"),
        "selected_command_output_outcome": _outcome(selected_command_output),
        "selected_command_output_failed_check_count": _failed_check_count(selected_command_output),
        "selected_post_invocation_execution_outcome": _outcome(selected_post_invocation),
        "selected_post_invocation_execution_failed_check_count": _failed_check_count(selected_post_invocation),
        "selected_v2_admitted_request_outcome": _outcome(selected_v2_admitted),
        "selected_v2_admitted_request_version": _version(selected_v2_admitted),
        "selected_v2_admitted_request_failed_check_count": _failed_check_count(selected_v2_admitted),
        "older_command_execution_boundary_lineage_not_current_execution": (
            _deep_find(
                selected_older_lineage,
                ("older_command_execution_boundary_lineage_treated_as_current_execution",),
                False,
            )
            is False
        ),
        "command_report_lineage_not_current_report_artifact": (
            _deep_find(selected_command_report_lineage, ("current_report_artifact",), False) is False
        ),
        "command_report_lineage_not_command_result": (
            _deep_find(
                selected_command_report_lineage,
                ("command_report_lineage_basis_treated_as_command_result",),
                False,
            )
            is False
        ),
        "key_non_claims": {
            key: non_claims.get(key, False)
            for key in (
                "command_result_created",
                "result_body_invented",
                "command_success_created",
                "pass_inference_made",
                "fail_inference_made",
                "authorization_token_reused",
                "consumed_request_reopened",
                "v1_output_capture_repaired",
                "v1_output_capture_hidden",
                "v1_output_capture_claimed_passed",
                "v2_output_capture_erased_v1",
                "follow_on_work_authorized",
            )
        },
    }
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        summary[key] = statement.get(key, False)
    for key in REQUIRED_FALSE_NON_CLAIMS:
        summary[key] = non_claims.get(key, statement.get(key, False))
    return _json_safe(summary)


def build_declared_portable_source_body_verification_command_result_boundary_request(
    *,
    command_result_boundary_request_id: str,
    command_result_boundary_question: str = CORE_QUESTION,
    command_result_boundary_intent: str = INTENT_RECORD,
    command_result_boundary_scope: Iterable[str] = SUPPORTED_COMMAND_RESULT_BOUNDARY_SCOPE,
    **selected_basis: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a declared request without inferring result, success, pass, or fail."""

    request: dict[str, Any] = {
        "command_result_boundary_request_id": command_result_boundary_request_id,
        "command_result_boundary_question": command_result_boundary_question,
        "command_result_boundary_intent": command_result_boundary_intent,
        "command_result_boundary_scope": sorted(str(item) for item in command_result_boundary_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    for key in SELECTED_BASIS_KEYS:
        request[key] = _sanitize_reference(selected_basis.get(key, {}))
    for key in POSTURE_KEYS:
        request[key] = {
            "posture_declared": True,
            "posture": key,
            "report_body_absent_or_bounded": True,
            "report_body_not_invented": True,
            "result_body_not_invented": True,
            "command_result_created": False,
            "result_body_invented": False,
            "command_success_created": False,
            "pass_inference_made": False,
            "fail_inference_made": False,
            "command_result_boundary_treated_as_result": False,
            "command_result_boundary_treated_as_success": False,
            "command_result_boundary_treated_as_source": False,
            "command_result_boundary_treated_as_authority": False,
            "command_result_boundary_treated_as_currentness": False,
            "command_result_boundary_treated_as_final_completion": False,
            "command_output_report_artifact_treated_as_result": False,
            "command_output_report_artifact_treated_as_success": False,
            "command_output_report_artifact_treated_as_source": False,
            "command_output_report_artifact_treated_as_authority": False,
            "command_output_report_artifact_treated_as_currentness": False,
            "command_output_report_artifact_treated_as_final_completion": False,
            "execution_trace_audit_only": True,
            "authorization_token_reuse_blocked": True,
            "consumed_request_token_remains_closed": True,
            "consumed_request_reopened": False,
            "returned_result_containment_preserved": True,
            "raw_full_prior_artifact_body_returned": False,
        }
    return _json_safe(request)
