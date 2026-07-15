"""Executable tests for the post-successor-runtime-step runtime-hosting boundary.

This suite proves that the resolver records one bounded runtime-hosting-boundary
posture only. It does not create runtime hosting, ongoing runtime, reusable
runtime permission, continuation, self-continuation, runtime daemon, runtime
loop, public API, participant-facing interface, distributed network behavior,
source transfer, source receipt, reception authorization, authority,
currentness, deployment, public release, operation permission, reusable
permission, or follow-on work.
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

import resolve_post_successor_runtime_step_runtime_hosting_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary"
)

OFFICIAL_SCOPE_VALUES = (
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
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED",
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
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE",
)

EXPECTED_TOP_LEVEL_SECTIONS = (
    "post_successor_runtime_step_runtime_hosting_boundary_metadata",
    "declared_runtime_hosting_boundary_question",
    "selected_successor_runtime_step_basis",
    "selected_successor_runtime_step_terminal_summary_basis",
    "selected_successor_runtime_step_boundary_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
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
    "runtime_hosting_boundary_scope",
    "runtime_hosting_boundary_checks",
    "runtime_hosting_boundary_statement",
    "runtime_hosting_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_successor_runtime_step_runtime_hosting_boundary_summary",
)

TRUE_STATEMENT_FIELDS = (
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

FALSE_NON_CLAIMS = (
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

SELECTED_BASIS_FIELDS = (
    "selected_successor_runtime_step_basis",
    "selected_successor_runtime_step_terminal_summary_basis",
    "selected_successor_runtime_step_boundary_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_MAPPING_FIELDS = (
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
    "raw_runtime_hosting_boundary_body",
    "raw_runtime_hosting_body",
    "raw_ongoing_runtime_body",
    "raw_runtime_body",
    "runtime_readiness_body",
    "runtime_boundary_body",
    "minimal_runtime_body",
    "successor_runtime_step_boundary_body",
    "successor_runtime_step_body",
    "successor_runtime_result_body",
    "runtime_hosting_boundary_body",
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
    "UNSAFE_RUNTIME_HOSTING_BOUNDARY_RAW_VALUE_SHOULD_NOT_RETURN",
)

PROHIBITED_OUTPUT_ROOT_MARKERS = (
    "actual_second_carrier_live_capture",
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step",
    "integrity_host_v0_min_coexistence_post_minimal_runtime_successor_runtime_step_boundary",
    "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness",
    "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion",
    "final_completion_boundary",
    "portable_verification_closure",
    "cross_carrier_evidence",
    "runtime-hosting",
    "ongoing-runtime",
    "source-transfer",
    "source-receipt",
    "deployment",
    "public_release",
)


def _build_request(**overrides):
    request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
    for key, value in overrides.items():
        request[key] = value
    return request


def _resolve_request(**overrides):
    return resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
        _build_request(**overrides)
    )


def _statement(result):
    return result["runtime_hosting_boundary_statement"]


def _non_claims(result):
    return result["non_claims"]


def _summary(result):
    return result["post_successor_runtime_step_runtime_hosting_boundary_summary"]


def _flip_non_claim(request, field):
    request["declared_non_claims"][field] = True
    request[field] = True


class PostSuccessorRuntimeStepRuntimeHostingBoundaryTests(unittest.TestCase):
    def assert_public_block_codes(self, result):
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code"):
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)

        for check in result.get("runtime_hosting_boundary_checks", ()):
            self.assertIsInstance(check, Mapping)
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bools(self, result):
        for section_name in (
            "runtime_hosting_boundary_statement",
            "runtime_hosting_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name, {})
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIsInstance(value, bool, f"{section_name}.{key}")

        for section_name in POSTURE_MAPPING_FIELDS:
            section = result.get(section_name, {})
            if isinstance(section, Mapping):
                for key, value in section.items():
                    if isinstance(value, bool):
                        self.assertIs(type(value), bool, f"{section_name}.{key}")

    def assert_serialized_result_contains_no_raw_or_hidden_sentinels(self, result):
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_strings_preserved(self, result):
        scope_values = result["runtime_hosting_boundary_scope"]
        self.assertIsInstance(scope_values, list)
        self.assertNotIn("[bounded-runtime-hosting-boundary-redacted]", scope_values)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope_values)

        for official_value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(official_value, resolver.SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE)
            self.assertIn(official_value, scope_values)

        for supported_value in resolver.SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE:
            self.assertNotEqual(
                supported_value,
                "[bounded-runtime-hosting-boundary-redacted]",
            )
            self.assertNotEqual(
                supported_value,
                "[bounded-redacted-raw-or-hidden-state]",
            )

    def assert_no_runtime_hosting_or_downstream_expansion(self, result):
        statement = _statement(result)
        non_claims = _non_claims(result)
        non_meaning = result.get("runtime_hosting_boundary_non_meaning", {})

        for key in (
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
        ):
            self.assertIs(statement[key], True, key)

        for key in FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)

        for key in (
            "runtime_hosting_boundary_means_runtime_hosting",
            "runtime_hosting_boundary_means_ongoing_runtime",
            "runtime_hosting_boundary_means_reusable_runtime_permission",
            "runtime_hosting_boundary_means_continuation",
            "runtime_hosting_boundary_means_self_continuation",
            "bounded_successor_runtime_result_or_refusal_means_hosting_authorization",
            "artifact_existence_means_runtime_hosting_boundary_authority",
            "repo_local_availability_means_runtime_hosting_boundary_authority",
            "latest_file_posture_means_runtime_hosting_boundary_authority",
            "hidden_repo_state_means_runtime_hosting_boundary_authority",
        ):
            self.assertIs(non_meaning[key], False, key)

    def test_public_api_and_constants(self):
        for name in (
            "resolve_post_successor_runtime_step_runtime_hosting_boundary",
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path",
            "write_post_successor_runtime_step_runtime_hosting_boundary_result",
            "build_post_successor_runtime_step_runtime_hosting_boundary_summary",
            "build_declared_post_successor_runtime_step_runtime_hosting_boundary_request",
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
            "SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_successor_runtime_step_runtime_hosting_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE,
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
        request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
        result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(request)
        summary = resolver.build_post_successor_runtime_step_runtime_hosting_boundary_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_post_successor_runtime_step_runtime_hosting_boundary",
        )
        self.assertEqual(
            summary["request_id"],
            request["runtime_hosting_boundary_request_id"],
        )

        for section in EXPECTED_TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        metadata = result["post_successor_runtime_step_runtime_hosting_boundary_metadata"]
        self.assertEqual(
            metadata["post_successor_runtime_step_runtime_hosting_boundary_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        for field in TRUE_STATEMENT_FIELDS:
            self.assertIs(_statement(result)[field], True, field)

        for field in FALSE_NON_CLAIMS:
            self.assertIs(_non_claims(result)[field], False, field)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_serialized_result_contains_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_no_runtime_hosting_or_downstream_expansion(result)

        all_scope_request = _build_request(
            runtime_hosting_boundary_scope=list(
                resolver.SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE
            )
        )
        all_scope_result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            all_scope_request
        )
        self.assertEqual(all_scope_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(_summary(all_scope_result)["failed_check_count"], 0)
        self.assert_official_scope_strings_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained_without_redacting_official_scope(self):
        request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()

        hostile_payload = {
            key: "UNSAFE_RUNTIME_HOSTING_BOUNDARY_RAW_VALUE_SHOULD_NOT_RETURN"
            for key in RAW_CONTENT_KEYS
        }
        hostile_payload["nested"] = [
            {"raw_runtime_hosting_boundary_body": "RAW_RUNTIME_HOSTING_BOUNDARY_BODY_MUST_NOT_RETURN"},
            {"raw_runtime_hosting_body": "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN"},
            {"raw_ongoing_runtime_body": "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN"},
            {"raw_body": "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN"},
            {"raw_body": "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN"},
            {"raw_body": "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN"},
            {"raw_body": "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN"},
            {"raw_body": "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN"},
            {"raw_runtime_body": "RAW_RUNTIME_BODY_MUST_NOT_RETURN"},
            {"raw_full_body": "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"},
            {"hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
        ]
        hostile_payload["official_scope_value"] = (
            "RUNTIME_HOSTING_BOUNDARY_NOT_RUNTIME_HOSTING"
        )

        for field in SELECTED_BASIS_FIELDS:
            request[field].update(copy.deepcopy(hostile_payload))

        original_request = copy.deepcopy(request)
        result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            request
        )

        self.assertEqual(request, original_request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_serialized_result_contains_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_strings_preserved(result)
        self.assert_generated_booleans_are_bools(result)
        self.assert_no_runtime_hosting_or_downstream_expansion(result)

        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("RUNTIME_HOSTING_BOUNDARY_NOT_RUNTIME_HOSTING", serialized)
        self.assertNotIn("[bounded-runtime-hosting-boundary-redacted]", serialized)

    def test_representative_blocking_behavior(self):
        cases = (
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "runtime_hosting_boundary_intent": (
                            "BLOCK_POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY"
                        )
                    }
                ),
            ),
            (
                "missing request mapping",
                lambda request: request.clear(),
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"runtime_hosting_boundary_intent": "UNSUPPORTED_INTENT"}
                ),
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {"runtime_hosting_boundary_scope": ["UNSUPPORTED_SCOPE"]}
                ),
            ),
            (
                "missing successor-runtime-step basis",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_basis": {},
                        "selected_successor_runtime_step_result_path": "",
                    }
                ),
            ),
            (
                "successor-runtime-step not recorded",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_result_outcome": (
                            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BLOCKED"
                        )
                    }
                ),
            ),
            (
                "successor-runtime-step failed checks present",
                lambda request: request.update(
                    {"selected_successor_runtime_step_failed_check_count": 1}
                ),
            ),
            (
                "successor-runtime-step version not 0.1.0",
                lambda request: request.update(
                    {"selected_successor_runtime_step_result_version": "9.9.9"}
                ),
            ),
            (
                "successor-runtime-step did not record bounded successor-runtime step",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_bounded_successor_runtime_step_recorded": False
                    }
                ),
            ),
            (
                "successor-runtime-step did not record bounded result/refusal",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_bounded_successor_runtime_result_or_refusal_recorded": False
                    }
                ),
            ),
            (
                "successor-runtime-step already created runtime hosting",
                lambda request: request.update(
                    {"selected_successor_runtime_step_already_created_runtime_hosting": True}
                ),
            ),
            (
                "successor-runtime-step already created ongoing runtime",
                lambda request: request.update(
                    {"selected_successor_runtime_step_already_created_ongoing_runtime": True}
                ),
            ),
            (
                "successor-runtime-step already created reusable runtime permission",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_already_created_reusable_runtime_permission": True
                    }
                ),
            ),
            (
                "successor-runtime-step already authorized continuation",
                lambda request: request.update(
                    {"selected_successor_runtime_step_already_authorized_continuation": True}
                ),
            ),
            (
                "successor-runtime-step already authorized self-continuation",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_already_authorized_self_continuation": True
                    }
                ),
            ),
            (
                "successor-runtime-step treated as runtime hosting",
                lambda request: request.update(
                    {"selected_successor_runtime_step_treated_as_runtime_hosting": True}
                ),
            ),
            (
                "successor-runtime-step treated as ongoing runtime",
                lambda request: request.update(
                    {"selected_successor_runtime_step_treated_as_ongoing_runtime": True}
                ),
            ),
            (
                "successor-runtime-step treated as reusable runtime permission",
                lambda request: request.update(
                    {
                        "selected_successor_runtime_step_treated_as_reusable_runtime_permission": True
                    }
                ),
            ),
            (
                "successor-runtime-step treated as continuation",
                lambda request: request.update(
                    {"selected_successor_runtime_step_treated_as_continuation": True}
                ),
            ),
            (
                "successor-runtime-step treated as self-continuation",
                lambda request: request.update(
                    {"selected_successor_runtime_step_treated_as_self_continuation": True}
                ),
            ),
            (
                "successor-runtime-step authorized future work",
                lambda request: request.update(
                    {"selected_successor_runtime_step_authorized_future_work": True}
                ),
            ),
            (
                "bounded successor-runtime result/refusal authorized hosting",
                lambda request: request.update(
                    {
                        "selected_bounded_successor_runtime_result_or_refusal_authorized_hosting": True
                    }
                ),
            ),
            (
                "runtime-hosting boundary created before review",
                lambda request: request.update(
                    {"runtime_hosting_boundary_created_before_review": True}
                ),
            ),
        )

        direct_false_fields = (
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
            "source_created",
            "authority_created",
            "currentness_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "adoption_created",
            "receiving_context_governance_created",
            "publication_flow_created",
            "follow_on_work_authorized",
            "artifact_existence_treated_as_runtime_hosting_boundary_authority",
            "artifact_path_treated_as_currentness",
            "latest_file_posture_treated_as_runtime_hosting_boundary_authority",
            "repo_local_availability_treated_as_runtime_hosting_boundary_authority",
            "hidden_repo_state_used_as_runtime_hosting_boundary_content",
            "hidden_repo_state_used_as_runtime_hosting_boundary_authority",
            "selected_basis_not_reference_shaped",
            "raw_full_prior_artifact_body_returned",
            "consumed_request_reopened",
            "authorization_token_reused",
        )
        non_claim_only_fields = (
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
            "bounded_successor_runtime_result_or_refusal_authorized_hosting",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )

        expanded_cases = list(cases)
        for field in direct_false_fields:
            expanded_cases.append(
                (field, lambda request, item=field: request.update({item: True}))
            )
        for field in non_claim_only_fields:
            expanded_cases.append((field, lambda request, item=field: _flip_non_claim(request, item)))
        expanded_cases.append(
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop(
                    "runtime_hosting_created"
                ),
            )
        )

        for case_name, mutate in expanded_cases:
            with self.subTest(case=case_name):
                request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
                mutate(request)
                result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
                    request
                )
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsInstance(result["block"], Mapping)
                self.assertIsNotNone(result["block"].get("block_code"))
                self.assert_public_block_codes(result)
                self.assert_generated_booleans_are_bools(result)
                self.assert_no_runtime_hosting_or_downstream_expansion(result)

        malformed = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            ["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
        )
        self.assert_public_block_codes(malformed)

    def test_path_and_write_behavior(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
            request_path = temp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path(
                request_path
            )
            summary = resolver.build_post_successor_runtime_step_runtime_hosting_boundary_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_post_successor_runtime_step_runtime_hosting_boundary",
            )

            malformed_path = temp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed)

            array_path = temp_path / "array.json"
            array_path.write_text(json.dumps([]), encoding="utf-8")
            array_result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing_result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path(
                temp_path / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing_result)

            temp_output_root = temp_path / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", temp_output_root):
                first_path = resolver.write_post_successor_runtime_step_runtime_hosting_boundary_result(
                    result
                )
                second_path = resolver.write_post_successor_runtime_step_runtime_hosting_boundary_result(
                    result
                )

            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertTrue(first_path.as_posix().endswith(".json"))
            self.assertIn(EXPECTED_OUTPUT_ROOT_SUFFIX, first_path.as_posix())

            for marker in PROHIBITED_OUTPUT_ROOT_MARKERS:
                self.assertNotIn(marker, first_path.as_posix())

            prohibited_path = temp_path / "actual_second_carrier_live_capture" / "bad.json"
            with self.assertRaises(resolver.PostSuccessorRuntimeStepRuntimeHostingBoundaryError):
                resolver.write_post_successor_runtime_step_runtime_hosting_boundary_result(
                    result,
                    prohibited_path,
                )

    def test_resolver_does_not_mutate_request_or_selected_basis_inputs(self):
        request = resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
        original = copy.deepcopy(request)

        selected_basis_objects = {
            field: request[field] for field in SELECTED_BASIS_FIELDS
        }
        posture_objects = {
            field: request[field] for field in POSTURE_MAPPING_FIELDS
        }
        scope_object = request["runtime_hosting_boundary_scope"]
        non_claims_object = request["declared_non_claims"]

        result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            request
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)
        for field, obj in selected_basis_objects.items():
            self.assertIs(request[field], obj, field)
            self.assertEqual(request[field], original[field], field)
        for field, obj in posture_objects.items():
            self.assertIs(request[field], obj, field)
            self.assertEqual(request[field], original[field], field)
        self.assertIs(request["runtime_hosting_boundary_scope"], scope_object)
        self.assertEqual(request["runtime_hosting_boundary_scope"], original["runtime_hosting_boundary_scope"])
        self.assertIs(request["declared_non_claims"], non_claims_object)
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_predecessor_failure_and_token_preservation(self):
        result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
        )
        summary = _summary(result)
        statement = _statement(result)
        non_claims = _non_claims(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
