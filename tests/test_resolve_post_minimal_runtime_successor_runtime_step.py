"""Executable boundary tests for the post-minimal-runtime successor-runtime step.

This suite proves that the resolver records one bounded successor-runtime-step
posture only. It deliberately keeps runtime hosting, ongoing runtime, reusable
runtime permission, successor-after-successor action, continuation, source
transfer, source receipt, reception authorization, authority, currentness,
deployment, public release, operation permission, and follow-on work outside the
recorded surface.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_post_minimal_runtime_successor_runtime_step as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step"
)

OFFICIAL_SCOPE_VALUES = (
    "SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_NOT_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_NOT_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_NOT_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_NOT_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_NOT_SUCCESSOR_AUTHORIZATION",
    "RUNTIME_HOSTING_NOT_CREATED",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "SUCCESSOR_AFTER_SUCCESSOR_STEP_NOT_CREATED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "REPO_LOCAL_AVAILABILITY_NOT_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SUCCESSOR_RUNTIME_STEP_QUESTION_UNDECLARED",
    "SUCCESSOR_RUNTIME_STEP_INTENT_UNSUPPORTED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_VERSION_NOT_0_1_0",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_DID_NOT_DECLARE_FUTURE_SUCCESSOR_RUNTIME_STEP_REVIEW",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_ALREADY_CREATED_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_ALREADY_CREATED_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_ALREADY_CREATED_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "SUCCESSOR_RUNTIME_STEP_CREATED_BEFORE_REVIEW",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SOURCE_TRANSFER",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SOURCE_RECEIPT",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SOURCE",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_AUTHORITY",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CURRENTNESS",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_DEPLOYMENT",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_PUBLIC_RELEASE",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_OPERATION_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_FOLLOW_ON_WORK",
    "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_SUCCESSOR_AFTER_SUCCESSOR_STEP",
    "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR_AFTER_SUCCESSOR_STEP",
    "RUNTIME_HOSTING_CREATED",
    "ONGOING_RUNTIME_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
    "SUCCESSOR_AFTER_SUCCESSOR_STEP_CREATED",
    "CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_AUTHORIZED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_REQUEST_MALFORMED",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_REQUEST_UNREADABLE",
)

EXPECTED_TOP_LEVEL_SECTIONS = (
    "post_minimal_runtime_successor_runtime_step_metadata",
    "declared_successor_runtime_step_question",
    "selected_successor_runtime_step_boundary_basis",
    "selected_successor_runtime_step_boundary_terminal_summary_basis",
    "selected_minimal_runtime_basis",
    "selected_minimal_runtime_terminal_summary_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "successor_runtime_step_spec_only_posture",
    "one_bounded_successor_runtime_step_posture",
    "successor_runtime_step_boundary_basis_preserved_posture",
    "minimal_runtime_basis_preserved_posture",
    "bounded_runtime_result_or_refusal_basis_preserved_posture",
    "successor_runtime_step_not_runtime_hosting_posture",
    "successor_runtime_step_not_ongoing_runtime_posture",
    "successor_runtime_step_not_reusable_runtime_permission_posture",
    "successor_runtime_step_not_continuation_posture",
    "successor_runtime_step_not_self_continuation_posture",
    "successor_runtime_step_not_successor_authorization_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
    "successor_after_successor_step_not_created_posture",
    "continuation_not_authorized_posture",
    "self_continuation_not_authorized_posture",
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
    "repo_local_availability_not_successor_runtime_step_authority_posture",
    "artifact_existence_not_successor_runtime_step_authority_posture",
    "latest_file_posture_not_successor_runtime_step_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "successor_runtime_step_scope",
    "successor_runtime_step_checks",
    "successor_runtime_step_statement",
    "successor_runtime_step_non_meaning",
    "successor_runtime_step_result_or_refusal",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_minimal_runtime_successor_runtime_step_summary",
)

TRUE_STATEMENT_FIELDS = (
    "successor_runtime_step_recorded",
    "bounded_successor_runtime_step_recorded",
    "successor_runtime_step_boundary_basis_preserved",
    "minimal_runtime_basis_preserved",
    "bounded_runtime_result_or_refusal_basis_preserved",
    "successor_runtime_step_not_runtime_hosting",
    "successor_runtime_step_not_ongoing_runtime",
    "successor_runtime_step_not_reusable_runtime_permission",
    "successor_runtime_step_not_continuation",
    "successor_runtime_step_not_self_continuation",
    "successor_runtime_step_not_successor_authorization",
    "runtime_hosting_not_created",
    "ongoing_runtime_not_created",
    "reusable_runtime_permission_not_created",
    "successor_after_successor_step_not_created",
    "continuation_not_authorized",
    "self_continuation_not_authorized",
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
    "hidden_repo_state_not_used_as_successor_runtime_step_authority",
    "repo_local_availability_not_successor_runtime_step_authority",
    "artifact_existence_not_successor_runtime_step_authority",
    "latest_file_posture_not_successor_runtime_step_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

FALSE_NON_CLAIMS = (
    "runtime_hosting_created",
    "ongoing_runtime_created",
    "reusable_runtime_permission_created",
    "successor_after_successor_step_created",
    "continuation_authorized",
    "self_continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "successor_runtime_step_treated_as_runtime_hosting",
    "successor_runtime_step_treated_as_ongoing_runtime",
    "successor_runtime_step_treated_as_reusable_runtime_permission",
    "successor_runtime_step_treated_as_continuation",
    "successor_runtime_step_treated_as_self_continuation",
    "successor_runtime_step_treated_as_source_transfer",
    "successor_runtime_step_treated_as_source_receipt",
    "successor_runtime_step_treated_as_reception_authorization",
    "successor_runtime_step_treated_as_source",
    "successor_runtime_step_treated_as_authority",
    "successor_runtime_step_treated_as_currentness",
    "successor_runtime_step_treated_as_deployment",
    "successor_runtime_step_treated_as_public_release",
    "successor_runtime_step_treated_as_operation_permission",
    "successor_runtime_step_treated_as_reusable_permission",
    "successor_runtime_step_treated_as_follow_on_work",
    "successor_runtime_step_authorized_successor_after_successor_step",
    "bounded_successor_runtime_result_or_refusal_authorized_successor_after_successor_step",
    "successor_runtime_step_boundary_treated_as_successor_runtime_step_without_review",
    "minimal_runtime_treated_as_successor_runtime_step",
    "bounded_runtime_result_or_refusal_authorized_successor",
    "artifact_existence_treated_as_successor_runtime_step_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_successor_runtime_step_authority",
    "repo_local_availability_treated_as_successor_runtime_step_authority",
    "hidden_repo_state_used_as_successor_runtime_step_content",
    "hidden_repo_state_used_as_successor_runtime_step_authority",
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

SELECTED_BASIS_FIELDS = (
    "selected_successor_runtime_step_boundary_basis",
    "selected_successor_runtime_step_boundary_terminal_summary_basis",
    "selected_minimal_runtime_basis",
    "selected_minimal_runtime_terminal_summary_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_MAPPING_FIELDS = (
    "successor_runtime_step_spec_only_posture",
    "one_bounded_successor_runtime_step_posture",
    "successor_runtime_step_boundary_basis_preserved_posture",
    "minimal_runtime_basis_preserved_posture",
    "bounded_runtime_result_or_refusal_basis_preserved_posture",
    "successor_runtime_step_not_runtime_hosting_posture",
    "successor_runtime_step_not_ongoing_runtime_posture",
    "successor_runtime_step_not_reusable_runtime_permission_posture",
    "successor_runtime_step_not_continuation_posture",
    "successor_runtime_step_not_self_continuation_posture",
    "successor_runtime_step_not_successor_authorization_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
    "successor_after_successor_step_not_created_posture",
    "continuation_not_authorized_posture",
    "self_continuation_not_authorized_posture",
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
    "repo_local_availability_not_successor_runtime_step_authority_posture",
    "artifact_existence_not_successor_runtime_step_authority_posture",
    "latest_file_posture_not_successor_runtime_step_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

RAW_CONTENT_KEYS = (
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
    "raw_runtime_hosting_body",
    "raw_ongoing_runtime_body",
    "raw_runtime_body",
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

HOSTILE_SENTINELS = (
    "RAW_SUCCESSOR_RUNTIME_STEP_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RUNTIME_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "UNSAFE_RAW_FULL_BODY_VALUE_SHOULD_NOT_RETURN",
)

PROHIBITED_OUTPUT_ROOT_MARKERS = (
    "actual_second_carrier_live_capture",
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary",
    "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion",
    "final_completion_boundary",
    "portable_verification_closure",
    "cross_carrier_evidence",
    "runtime_hosting",
    "ongoing_runtime",
    "source_transfer",
    "source_receipt",
    "deployment",
    "public_release",
)


def _build_request(**overrides):
    request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()
    for key, value in overrides.items():
        request[key] = value
    return request


def _resolve_request(**overrides):
    return resolver.resolve_post_minimal_runtime_successor_runtime_step(
        _build_request(**overrides)
    )


def _statement(result):
    return result["successor_runtime_step_statement"]


def _non_claims(result):
    return result["non_claims"]


def _summary(result):
    return result["post_minimal_runtime_successor_runtime_step_summary"]


class PostMinimalRuntimeSuccessorRuntimeStepTests(unittest.TestCase):
    def assert_public_block_codes(self, result):
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code"):
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)

        for check in result.get("successor_runtime_step_checks", ()):
            self.assertIsInstance(check, Mapping)
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bools(self, result):
        for section_name in ("successor_runtime_step_statement", "non_claims"):
            section = result.get(section_name, {})
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIsInstance(value, bool, f"{section_name}.{key}")

        result_or_refusal = result.get("successor_runtime_step_result_or_refusal", {})
        if isinstance(result_or_refusal, Mapping):
            for key, value in result_or_refusal.items():
                if isinstance(value, bool):
                    self.assertIs(type(value), bool, key)

    def assert_serialized_result_contains_no_raw_or_hidden_sentinels(self, result):
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_strings_preserved(self, result):
        scope_values = result["successor_runtime_step_scope"]
        self.assertIsInstance(scope_values, list)
        self.assertNotIn("[bounded-successor-runtime-step-redacted]", scope_values)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope_values)

        for official_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official_value, resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE)
            self.assertIn(official_value, scope_values)

        for supported_value in resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE:
            self.assertNotEqual(
                supported_value,
                "[bounded-successor-runtime-step-redacted]",
            )
            self.assertNotEqual(
                supported_value,
                "[bounded-redacted-raw-or-hidden-state]",
            )

    def assert_no_runtime_or_downstream_expansion(self, result):
        statement = _statement(result)
        non_claims = _non_claims(result)

        for key in (
            "successor_runtime_step_not_runtime_hosting",
            "successor_runtime_step_not_ongoing_runtime",
            "successor_runtime_step_not_reusable_runtime_permission",
            "successor_runtime_step_not_continuation",
            "successor_runtime_step_not_self_continuation",
            "successor_runtime_step_not_successor_authorization",
            "runtime_hosting_not_created",
            "ongoing_runtime_not_created",
            "reusable_runtime_permission_not_created",
            "successor_after_successor_step_not_created",
            "continuation_not_authorized",
            "self_continuation_not_authorized",
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
            "hidden_repo_state_not_used_as_successor_runtime_step_authority",
            "repo_local_availability_not_successor_runtime_step_authority",
            "artifact_existence_not_successor_runtime_step_authority",
            "latest_file_posture_not_successor_runtime_step_authority",
            "selected_basis_reference_shape_preserved",
            "raw_full_prior_artifact_body_not_returned",
            "official_enum_scope_strings_not_redacted",
            "hostile_raw_body_content_contained",
            "predecessor_failure_evidence_preserved",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertIs(statement[key], True, key)

        for key in (
            "runtime_hosting_created",
            "ongoing_runtime_created",
            "reusable_runtime_permission_created",
            "successor_after_successor_step_created",
            "continuation_authorized",
            "self_continuation_authorized",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "successor_runtime_step_treated_as_runtime_hosting",
            "successor_runtime_step_treated_as_ongoing_runtime",
            "successor_runtime_step_treated_as_reusable_runtime_permission",
            "successor_runtime_step_treated_as_continuation",
            "successor_runtime_step_treated_as_self_continuation",
            "successor_runtime_step_authorized_successor_after_successor_step",
            "bounded_successor_runtime_result_or_refusal_authorized_successor_after_successor_step",
            "hidden_repo_state_used_as_successor_runtime_step_content",
            "hidden_repo_state_used_as_successor_runtime_step_authority",
            "source_created",
            "authority_created",
            "currentness_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(non_claims[key], False, key)

    def test_public_api_and_constants(self):
        for name in (
            "resolve_post_minimal_runtime_successor_runtime_step",
            "resolve_post_minimal_runtime_successor_runtime_step_from_path",
            "write_post_minimal_runtime_successor_runtime_step_result",
            "build_post_minimal_runtime_successor_runtime_step_summary",
            "build_declared_post_minimal_runtime_successor_runtime_step_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_minimal_runtime_successor_runtime_step",
        )
        self.assertEqual(
            resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            resolver.OUTPUT_ROOT.as_posix().endswith(EXPECTED_OUTPUT_ROOT_SUFFIX)
        )

        for scope_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(scope_value, resolver.SUPPORTED_SCOPE_VALUES)

        for block_code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(block_code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self):
        request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()
        result = resolver.resolve_post_minimal_runtime_successor_runtime_step(request)
        summary = resolver.build_post_minimal_runtime_successor_runtime_step_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_post_minimal_runtime_successor_runtime_step",
        )
        self.assertEqual(summary["request_id"], request["successor_runtime_step_request_id"])

        for section in EXPECTED_TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["post_minimal_runtime_successor_runtime_step_metadata"]
        self.assertEqual(metadata["post_minimal_runtime_successor_runtime_step_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        for field in TRUE_STATEMENT_FIELDS:
            self.assertIs(_statement(result)[field], True, field)

        for field in FALSE_NON_CLAIMS:
            self.assertIs(_non_claims(result)[field], False, field)

        result_or_refusal = result["successor_runtime_step_result_or_refusal"]
        self.assertIsInstance(result_or_refusal, Mapping)
        self.assertIn(
            result_or_refusal.get("posture"),
            {
                "bounded_successor_runtime_result",
                "bounded_successor_runtime_refusal",
            },
        )
        self.assertIs(result_or_refusal.get("executes_arbitrary_work"), False)
        self.assertIs(result_or_refusal.get("mutates_prior_artifacts"), False)
        self.assertIs(result_or_refusal.get("creates_runtime_hosting"), False)
        self.assertIs(result_or_refusal.get("creates_ongoing_runtime"), False)
        self.assertIs(result_or_refusal.get("creates_reusable_runtime_permission"), False)
        self.assertIs(result_or_refusal.get("creates_successor_after_successor_step", False), False)
        self.assertIs(result_or_refusal.get("authorizes_continuation", False), False)
        self.assertIs(result_or_refusal.get("authorizes_self_continuation"), False)
        self.assertIs(
            result_or_refusal.get("authorizes_successor_after_successor_step"),
            False,
        )
        self.assertIs(result_or_refusal.get("authorizes_follow_on_work"), False)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_serialized_result_contains_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_no_runtime_or_downstream_expansion(result)

        all_scope_request = _build_request(
            successor_runtime_step_scope=list(
                resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE
            )
        )
        all_scope_result = resolver.resolve_post_minimal_runtime_successor_runtime_step(
            all_scope_request
        )
        self.assertEqual(all_scope_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(all_scope_result)["failed_check_count"], 0)
        self.assert_official_scope_strings_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained_without_redacting_official_scope(self):
        request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()

        hostile_payload = {
            key: "UNSAFE_RAW_FULL_BODY_VALUE_SHOULD_NOT_RETURN"
            for key in RAW_CONTENT_KEYS
        }
        hostile_payload["nested"] = [
            {"raw_body": "RAW_SUCCESSOR_RUNTIME_STEP_BODY_MUST_NOT_RETURN"},
            "RAW_SUCCESSOR_RUNTIME_RESULT_BODY_MUST_NOT_RETURN",
            {
                "items": [
                    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
                    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
                    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
                    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
                    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                ]
            },
        ]
        hostile_payload["official_scope_value"] = (
            "SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING"
        )

        for field in SELECTED_BASIS_FIELDS:
            request[field].update(copy.deepcopy(hostile_payload))

        request["requested_successor_runtime_step_result_or_refusal"][
            "raw_successor_runtime_result_body"
        ] = "RAW_SUCCESSOR_RUNTIME_RESULT_BODY_MUST_NOT_RETURN"
        request["requested_successor_runtime_step_result_or_refusal"][
            "ordinary_official_value"
        ] = "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED"

        original_request = copy.deepcopy(request)
        result = resolver.resolve_post_minimal_runtime_successor_runtime_step(request)

        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_serialized_result_contains_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_no_runtime_or_downstream_expansion(result)

        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING", serialized)
        self.assertNotIn("[bounded-successor-runtime-step-redacted]", serialized)

    def test_representative_blocking_behavior(self):
        cases = (
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "successor_runtime_step_intent": (
                            "BLOCK_POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP"
                        )
                    }
                ),
            ),
            (
                "missing request question",
                lambda request: request.update({"successor_runtime_step_question": ""}),
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"successor_runtime_step_intent": "UNSUPPORTED_INTENT"}
                ),
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {"successor_runtime_step_scope": ["UNSUPPORTED_SCOPE_VALUE"]}
                ),
            ),
            (
                "missing successor-runtime-step-boundary basis",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_basis": {},
                        "selected_successor_runtime_step_boundary_terminal_summary_basis": {},
                        "selected_successor_runtime_step_boundary_result_path": "",
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary not recorded",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_result_outcome": (
                            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RECORDED"
                        )
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary failed checks present",
                lambda request: request.update(
                    {"selected_successor_runtime_step_boundary_failed_check_count": 1}
                ),
            ),
            (
                "successor-runtime-step-boundary version not 0.1.0",
                lambda request: request.update(
                    {"selected_successor_runtime_step_boundary_result_version": "9.9.9"}
                ),
            ),
            (
                "successor-runtime-step-boundary did not declare future review",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_declared_future_successor_runtime_step_review": False
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary already created successor runtime step",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_already_created_successor_runtime_step": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary already created runtime hosting",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_already_created_runtime_hosting": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary already created ongoing runtime",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_already_created_ongoing_runtime": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary already authorized continuation",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_already_authorized_continuation": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary treated boundary as successor runtime step",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_treated_boundary_as_successor_runtime_step": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary treated boundary as runtime hosting",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_treated_boundary_as_runtime_hosting": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary treated boundary as ongoing runtime",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_treated_boundary_as_ongoing_runtime": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary treated boundary as continuation",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_boundary_treated_boundary_as_continuation": True
                    }
                ),
            ),
            (
                "successor-runtime-step-boundary authorized future work",
                lambda request: request.update(
                    {"selected_successor_runtime_step_boundary_authorized_future_work": True}
                ),
            ),
            (
                "successor runtime step created before review",
                lambda request: request.update(
                    {"successor_runtime_step_created_before_review": True}
                ),
            ),
            (
                "successor runtime step treated as runtime hosting",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_runtime_hosting": True}
                ),
            ),
            (
                "successor runtime step treated as ongoing runtime",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_ongoing_runtime": True}
                ),
            ),
            (
                "successor runtime step treated as reusable runtime permission",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_reusable_runtime_permission": True}
                ),
            ),
            (
                "successor runtime step treated as continuation",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_continuation": True}
                ),
            ),
            (
                "successor runtime step treated as self-continuation",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_self_continuation": True}
                ),
            ),
            (
                "successor runtime step treated as source transfer",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_source_transfer": True}
                ),
            ),
            (
                "successor runtime step treated as source receipt",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_source_receipt": True}
                ),
            ),
            (
                "successor runtime step treated as reception authorization",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_reception_authorization": True}
                ),
            ),
            (
                "successor runtime step treated as source",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_source": True}
                ),
            ),
            (
                "successor runtime step treated as authority",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_authority": True}
                ),
            ),
            (
                "successor runtime step treated as currentness",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_currentness": True}
                ),
            ),
            (
                "successor runtime step treated as deployment",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_deployment": True}
                ),
            ),
            (
                "successor runtime step treated as public release",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_public_release": True}
                ),
            ),
            (
                "successor runtime step treated as operation permission",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_operation_permission": True}
                ),
            ),
            (
                "successor runtime step treated as reusable permission",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_reusable_permission": True}
                ),
            ),
            (
                "successor runtime step treated as follow-on work",
                lambda request: request.update(
                    {"successor_runtime_step_treated_as_follow_on_work": True}
                ),
            ),
            (
                "successor runtime step authorized successor-after-successor step",
                lambda request: request.update(
                    {"successor_runtime_step_authorized_successor_after_successor_step": True}
                ),
            ),
            (
                "bounded successor-runtime result/refusal authorized successor-after-successor step",
                lambda request: request.update(
                    {
                        "bounded_successor_runtime_result_or_refusal_authorized_successor_after_successor_step": True
                    }
                ),
            ),
            (
                "runtime hosting created",
                lambda request: request.update({"runtime_hosting_created": True}),
            ),
            (
                "ongoing runtime created",
                lambda request: request.update({"ongoing_runtime_created": True}),
            ),
            (
                "reusable runtime permission created",
                lambda request: request.update(
                    {"reusable_runtime_permission_created": True}
                ),
            ),
            (
                "successor-after-successor step created",
                lambda request: request.update(
                    {"successor_after_successor_step_created": True}
                ),
            ),
            (
                "continuation authorized",
                lambda request: request.update({"continuation_authorized": True}),
            ),
            (
                "self-continuation authorized",
                lambda request: request.update({"self_continuation_authorized": True}),
            ),
            (
                "source transfer occurred",
                lambda request: request.update({"source_transfer_occurred": True}),
            ),
            (
                "source receipt occurred",
                lambda request: request.update({"source_receipt_occurred": True}),
            ),
            (
                "reception authorization created",
                lambda request: request.update(
                    {"reception_authorization_created": True}
                ),
            ),
            ("source created", lambda request: request.update({"source_created": True})),
            (
                "authority created",
                lambda request: request.update({"authority_created": True}),
            ),
            (
                "currentness created",
                lambda request: request.update({"currentness_created": True}),
            ),
            (
                "deployment created",
                lambda request: request.update({"deployment_created": True}),
            ),
            (
                "public release created",
                lambda request: request.update({"public_release_created": True}),
            ),
            (
                "operation permission created",
                lambda request: request.update({"operation_permission_created": True}),
            ),
            (
                "reusable permission created",
                lambda request: request.update({"reusable_permission_created": True}),
            ),
            (
                "derivative reception authorized",
                lambda request: request.update(
                    {"derivative_reception_authorized": True}
                ),
            ),
            (
                "vessel relation authorized",
                lambda request: request.update({"vessel_relation_authorized": True}),
            ),
            (
                "adoption created",
                lambda request: request.update({"adoption_created": True}),
            ),
            (
                "receiving-context governance created",
                lambda request: request.update(
                    {"receiving_context_governance_created": True}
                ),
            ),
            (
                "publication flow created",
                lambda request: request.update({"publication_flow_created": True}),
            ),
            (
                "follow-on work authorized",
                lambda request: request.update({"follow_on_work_authorized": True}),
            ),
            (
                "artifact existence treated as successor-runtime-step authority",
                lambda request: request.update(
                    {
                        "artifact_existence_treated_as_successor_runtime_step_authority": True
                    }
                ),
            ),
            (
                "artifact path treated as currentness",
                lambda request: request.update(
                    {"artifact_path_treated_as_currentness": True}
                ),
            ),
            (
                "latest file posture treated as successor-runtime-step authority",
                lambda request: request.update(
                    {
                        "latest_file_posture_treated_as_successor_runtime_step_authority": True
                    }
                ),
            ),
            (
                "repo-local availability treated as successor-runtime-step authority",
                lambda request: request.update(
                    {
                        "repo_local_availability_treated_as_successor_runtime_step_authority": True
                    }
                ),
            ),
            (
                "hidden repo state used as successor-runtime-step content",
                lambda request: request.update(
                    {"hidden_repo_state_used_as_successor_runtime_step_content": True}
                ),
            ),
            (
                "hidden repo state used as successor-runtime-step authority",
                lambda request: request.update(
                    {"hidden_repo_state_used_as_successor_runtime_step_authority": True}
                ),
            ),
            (
                "selected basis not reference-shaped",
                lambda request: request.update({"reference_shaped_input_posture": False}),
            ),
            (
                "raw full prior artifact body returned",
                lambda request: request.update(
                    {"raw_full_prior_artifact_body_returned": True}
                ),
            ),
            (
                "predecessor failure repaired",
                lambda request: request.update({"predecessor_failure_repaired": True}),
            ),
            (
                "predecessor failure hidden",
                lambda request: request.update({"predecessor_failure_hidden": True}),
            ),
            (
                "predecessor failure claimed passed",
                lambda request: request.update(
                    {"predecessor_failure_claimed_passed": True}
                ),
            ),
            (
                "consumed request reopened",
                lambda request: request.update({"consumed_request_reopened": True}),
            ),
            (
                "authorization token reused",
                lambda request: request.update({"authorization_token_reused": True}),
            ),
            (
                "required non-claim missing",
                lambda request: (
                    request["declared_non_claims"].pop("runtime_hosting_created"),
                    request.pop("runtime_hosting_created", None),
                ),
            ),
            (
                "required non-claim flipped",
                lambda request: request["declared_non_claims"].update(
                    {"runtime_hosting_created": True}
                ),
            ),
        )

        malformed_result = resolver.resolve_post_minimal_runtime_successor_runtime_step(
            "not a mapping"
        )
        self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assert_public_block_codes(malformed_result)
        self.assert_no_runtime_or_downstream_expansion(malformed_result)

        for label, mutate in cases:
            with self.subTest(label=label):
                request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()
                mutate(request)
                result = resolver.resolve_post_minimal_runtime_successor_runtime_step(
                    request
                )

                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsInstance(result["block"], Mapping)
                self.assertIn(result["block"].get("block_code"), resolver.BLOCK_CODES)
                self.assert_public_block_codes(result)
                self.assert_generated_booleans_are_bools(result)
                self.assert_no_runtime_or_downstream_expansion(result)

    def test_path_and_write_behavior(self):
        with tempfile.TemporaryDirectory() as tmp_name:
            tmp = Path(tmp_name)
            request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()
            request_path = tmp / "successor_runtime_step_request.json"
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True),
                encoding="utf-8",
            )

            result = resolver.resolve_post_minimal_runtime_successor_runtime_step_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(_summary(result)["result_version"], "0.1.0")
            self.assertEqual(_summary(result)["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_from_path(
                    malformed_path
                )
            )
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed_result)

            array_path = tmp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_from_path(
                    tmp / "missing.json"
                )
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            patched_output_root = tmp / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_output_root):
                first_path = resolver.write_post_minimal_runtime_successor_runtime_step_result(
                    result
                )
                second_path = resolver.write_post_minimal_runtime_successor_runtime_step_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.as_posix().endswith(".json"))
            self.assertIn(EXPECTED_OUTPUT_ROOT_SUFFIX, first_path.as_posix())
            self.assertIn(EXPECTED_OUTPUT_ROOT_SUFFIX, second_path.as_posix())

            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                parsed["post_minimal_runtime_successor_runtime_step_metadata"][
                    "resolver_module"
                ],
                resolver.RESOLVER_MODULE,
            )

            for marker in PROHIBITED_OUTPUT_ROOT_MARKERS:
                self.assertNotIn(marker, first_path.as_posix())
                self.assertNotIn(marker, second_path.as_posix())

    def test_input_request_and_nested_basis_are_not_mutated(self):
        request = resolver.build_declared_post_minimal_runtime_successor_runtime_step_request()

        for field in SELECTED_BASIS_FIELDS:
            request[field]["nested_basis_marker"] = {
                "list": [field, {"kept": True}],
                "scope": "SUCCESSOR_RUNTIME_STEP_NOT_RUNTIME_HOSTING",
            }

        for field in POSTURE_MAPPING_FIELDS:
            request[field]["local_marker"] = {"kept": True}

        request["successor_runtime_step_scope"] = list(
            resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_SCOPE
        )
        request["declared_non_claims"]["local_marker_non_claim"] = False
        request["declared_non_claims"].pop("local_marker_non_claim")

        original_request = copy.deepcopy(request)
        original_selected_basis = {
            field: copy.deepcopy(request[field]) for field in SELECTED_BASIS_FIELDS
        }
        original_postures = {
            field: copy.deepcopy(request[field]) for field in POSTURE_MAPPING_FIELDS
        }
        original_scope = copy.deepcopy(request["successor_runtime_step_scope"])
        original_non_claims = copy.deepcopy(request["declared_non_claims"])

        result = resolver.resolve_post_minimal_runtime_successor_runtime_step(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original_request)
        for field in SELECTED_BASIS_FIELDS:
            self.assertEqual(request[field], original_selected_basis[field], field)
        for field in POSTURE_MAPPING_FIELDS:
            self.assertEqual(request[field], original_postures[field], field)
        self.assertEqual(request["successor_runtime_step_scope"], original_scope)
        self.assertEqual(request["declared_non_claims"], original_non_claims)

    def test_predecessor_failure_preservation(self):
        result = _resolve_request()
        summary = resolver.build_post_minimal_runtime_successor_runtime_step_summary(
            result
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(_statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)

        non_claims = _non_claims(result)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)

        self.assert_no_runtime_or_downstream_expansion(result)


if __name__ == "__main__":
    unittest.main()
