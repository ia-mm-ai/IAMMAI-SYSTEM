"""Tests for the post-portable-verification runtime-readiness resolver.

This suite exercises runtime-readiness posture only. It is downstream of the
runtime-readiness-boundary line, records one bounded runtime-readiness posture
only, and preserves that runtime, runtime boundary, runtime step,
continuation, source transfer, source receipt, reception authorization,
source, authority, currentness, deployment, public release, operation
permission, reusable permission, adoption, receiving-context governance,
publication flow, and follow-on work are not created.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_post_portable_verification_runtime_readiness as resolver  # noqa: E402


TOP_LEVEL_SECTIONS = (
    "post_portable_verification_runtime_readiness_metadata",
    "declared_runtime_readiness_question",
    "selected_runtime_readiness_boundary_basis",
    "selected_runtime_readiness_boundary_terminal_summary_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_final_completion_artifact_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "runtime_readiness_spec_only_posture",
    "one_bounded_runtime_readiness_posture",
    "runtime_readiness_boundary_basis_preserved_posture",
    "portable_verification_final_completion_basis_preserved_posture",
    "post_portable_verification_currentness_basis_preserved_posture",
    "checkability_not_continuation_preserved_posture",
    "runtime_readiness_not_runtime_posture",
    "runtime_readiness_not_runtime_boundary_posture",
    "runtime_readiness_not_runtime_step_posture",
    "runtime_readiness_not_continuation_posture",
    "runtime_boundary_not_created_posture",
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
    "repo_local_availability_not_runtime_readiness_authority_posture",
    "artifact_existence_not_runtime_readiness_authority_posture",
    "latest_file_posture_not_runtime_readiness_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "runtime_readiness_scope",
    "runtime_readiness_checks",
    "runtime_readiness_statement",
    "runtime_readiness_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_portable_verification_runtime_readiness_summary",
)

SELECTED_BASIS_FIELDS = (
    "selected_runtime_readiness_boundary_basis",
    "selected_runtime_readiness_boundary_terminal_summary_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_final_completion_artifact_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "runtime_readiness_spec_only_posture",
    "one_bounded_runtime_readiness_posture",
    "runtime_readiness_boundary_basis_preserved_posture",
    "portable_verification_final_completion_basis_preserved_posture",
    "post_portable_verification_currentness_basis_preserved_posture",
    "checkability_not_continuation_preserved_posture",
    "runtime_readiness_not_runtime_posture",
    "runtime_readiness_not_runtime_boundary_posture",
    "runtime_readiness_not_runtime_step_posture",
    "runtime_readiness_not_continuation_posture",
    "runtime_boundary_not_created_posture",
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
    "repo_local_availability_not_runtime_readiness_authority_posture",
    "artifact_existence_not_runtime_readiness_authority_posture",
    "latest_file_posture_not_runtime_readiness_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

OFFICIAL_SCOPE_VALUES = (
    "RUNTIME_READINESS_NOT_RUNTIME",
    "RUNTIME_READINESS_NOT_RUNTIME_BOUNDARY",
    "RUNTIME_READINESS_NOT_RUNTIME_STEP",
    "RUNTIME_READINESS_NOT_CONTINUATION",
    "RUNTIME_BOUNDARY_NOT_CREATED",
    "RUNTIME_NOT_CREATED",
    "RUNTIME_STEP_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "CHECKABILITY_NOT_CONTINUATION_PRESERVED",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_READINESS_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_READINESS_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_READINESS_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_READINESS_QUESTION_UNDECLARED",
    "RUNTIME_READINESS_INTENT_UNSUPPORTED",
    "RUNTIME_READINESS_BOUNDARY_BASIS_MISSING",
    "RUNTIME_READINESS_BOUNDARY_NOT_RECORDED",
    "RUNTIME_READINESS_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_READINESS_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_READINESS_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_READINESS_REVIEW_STEP",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME_READINESS",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_CREATED_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME_READINESS",
    "RUNTIME_READINESS_BOUNDARY_TREATED_BOUNDARY_AS_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CHECKABILITY_AS_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_RUNTIME",
    "RUNTIME_READINESS_BOUNDARY_TREATED_FINAL_COMPLETION_AS_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_RUNTIME_PERMISSION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_CURRENTNESS_SURFACE_AS_OPERATION_PERMISSION",
    "RUNTIME_READINESS_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_READINESS_CREATED_BEFORE_REVIEW",
    "RUNTIME_CREATED",
    "RUNTIME_BOUNDARY_CREATED",
    "RUNTIME_STEP_CREATED",
    "CONTINUATION_AUTHORIZED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_READINESS_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_READINESS_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_READINESS_SCOPE",
    "DECLARED_RUNTIME_READINESS_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_READINESS_REQUEST_UNREADABLE",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "runtime_readiness_recorded",
    "bounded_runtime_readiness_recorded",
    "runtime_readiness_boundary_basis_preserved",
    "portable_verification_final_completion_basis_preserved",
    "post_portable_verification_currentness_basis_preserved",
    "checkability_not_continuation_preserved",
    "runtime_readiness_not_runtime",
    "runtime_readiness_not_runtime_boundary",
    "runtime_readiness_not_runtime_step",
    "runtime_readiness_not_continuation",
    "runtime_boundary_not_created",
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
    "hidden_repo_state_not_used_as_runtime_readiness_authority",
    "repo_local_availability_not_runtime_readiness_authority",
    "artifact_existence_not_runtime_readiness_authority",
    "latest_file_posture_not_runtime_readiness_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

EXPECTED_FALSE_NON_CLAIMS = (
    "runtime_created",
    "runtime_boundary_created",
    "runtime_step_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_readiness_treated_as_runtime",
    "runtime_readiness_treated_as_runtime_boundary",
    "runtime_readiness_treated_as_runtime_step",
    "runtime_readiness_treated_as_continuation",
    "runtime_readiness_treated_as_source_transfer",
    "runtime_readiness_treated_as_source_receipt",
    "runtime_readiness_treated_as_reception_authorization",
    "runtime_readiness_treated_as_source",
    "runtime_readiness_treated_as_authority",
    "runtime_readiness_treated_as_currentness",
    "runtime_readiness_treated_as_deployment",
    "runtime_readiness_treated_as_public_release",
    "runtime_readiness_treated_as_operation_permission",
    "runtime_readiness_treated_as_reusable_permission",
    "runtime_readiness_treated_as_follow_on_work",
    "runtime_readiness_boundary_treated_as_runtime_readiness_without_review",
    "portable_verification_final_completion_treated_as_runtime",
    "portable_verification_final_completion_treated_as_continuation",
    "post_portable_verification_currentness_surface_treated_as_runtime_permission",
    "post_portable_verification_currentness_surface_treated_as_operation_permission",
    "checkability_treated_as_continuation",
    "artifact_existence_treated_as_runtime_readiness_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_runtime_readiness_authority",
    "repo_local_availability_treated_as_runtime_readiness_authority",
    "hidden_repo_state_used_as_runtime_readiness_content",
    "hidden_repo_state_used_as_runtime_readiness_authority",
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

RAW_SENTINELS = (
    "RAW_RUNTIME_READINESS_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

HOSTILE_BODY_KEYS = (
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

REDACTION_PLACEHOLDERS = (
    "[bounded-runtime-readiness-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_post_portable_verification_runtime_readiness_request(
        **overrides
    )


def set_request_value(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def set_non_claim(key: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = value

    return mutate


def remove_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


class PostPortableVerificationRuntimeReadinessTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("runtime_readiness_checks", []):
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "runtime_readiness_statement",
            "runtime_readiness_non_meaning",
            "non_claims",
        ):
            section = result[section_name]
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
        for check in result["runtime_readiness_checks"]:
            self.assertIs(type(check["passed"]), bool)

    def assert_no_raw_sentinels(
        self, result: Mapping[str, Any], extra_forbidden: tuple[str, ...] = ()
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS + extra_forbidden:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result["runtime_readiness_scope"]
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        for value in scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for supported_value in resolver.SUPPORTED_RUNTIME_READINESS_SCOPE:
            self.assertIn(supported_value, resolver.SUPPORTED_SCOPE_VALUES)
            self.assertNotIn(supported_value, REDACTION_PLACEHOLDERS)

    def assert_safe_runtime_readiness_membrane(self, result: Mapping[str, Any]) -> None:
        statement = result["runtime_readiness_statement"]
        non_claims = result["non_claims"]
        self.assertIs(statement["runtime_readiness_not_runtime"], True)
        self.assertIs(statement["runtime_readiness_not_runtime_boundary"], True)
        self.assertIs(statement["runtime_readiness_not_runtime_step"], True)
        self.assertIs(statement["runtime_readiness_not_continuation"], True)
        self.assertIs(statement["runtime_boundary_not_created"], True)
        self.assertIs(statement["runtime_not_created"], True)
        self.assertIs(statement["runtime_step_not_created"], True)
        self.assertIs(statement["continuation_not_authorized"], True)
        self.assertIs(statement["source_not_created"], True)
        self.assertIs(statement["authority_not_created"], True)
        self.assertIs(statement["currentness_not_created"], True)
        self.assertIs(statement["deployment_not_created"], True)
        self.assertIs(statement["public_release_not_created"], True)
        self.assertIs(statement["operation_permission_not_created"], True)
        self.assertIs(statement["follow_on_work_not_authorized"], True)
        self.assertIs(non_claims["runtime_created"], False)
        self.assertIs(non_claims["runtime_boundary_created"], False)
        self.assertIs(non_claims["runtime_step_created"], False)
        self.assertIs(non_claims["continuation_authorized"], False)
        self.assertIs(non_claims["runtime_readiness_treated_as_runtime"], False)
        self.assertIs(non_claims["runtime_readiness_treated_as_runtime_boundary"], False)
        self.assertIs(non_claims["runtime_readiness_treated_as_runtime_step"], False)
        self.assertIs(non_claims["source_created"], False)
        self.assertIs(non_claims["authority_created"], False)
        self.assertIs(non_claims["currentness_created"], False)
        self.assertIs(non_claims["deployment_created"], False)
        self.assertIs(non_claims["public_release_created"], False)
        self.assertIs(non_claims["operation_permission_created"], False)
        self.assertIs(non_claims["follow_on_work_authorized"], False)
        self.assertIs(
            non_claims["hidden_repo_state_used_as_runtime_readiness_content"], False
        )
        self.assertIs(
            non_claims["hidden_repo_state_used_as_runtime_readiness_authority"], False
        )
        self.assertIs(
            non_claims["repo_local_availability_treated_as_runtime_readiness_authority"],
            False,
        )
        self.assertIs(
            non_claims["artifact_existence_treated_as_runtime_readiness_authority"],
            False,
        )
        self.assertIs(
            non_claims["latest_file_posture_treated_as_runtime_readiness_authority"],
            False,
        )

    def assert_predecessor_and_tokens_preserved(
        self, result: Mapping[str, Any]
    ) -> None:
        statement = result["runtime_readiness_statement"]
        non_claims = result["non_claims"]
        summary = resolver.build_post_portable_verification_runtime_readiness_summary(
            result
        )
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)

    def assert_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsInstance(result.get("block"), dict)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_safe_runtime_readiness_membrane(result)
        self.assert_predecessor_and_tokens_preserved(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_portable_verification_runtime_readiness",
            "resolve_post_portable_verification_runtime_readiness_from_path",
            "write_post_portable_verification_runtime_readiness_result",
            "build_post_portable_verification_runtime_readiness_summary",
            "build_declared_post_portable_verification_runtime_readiness_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_RUNTIME_READINESS_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_portable_verification_runtime_readiness",
        )
        self.assertEqual(
            resolver.SUPPORTED_RUNTIME_READINESS_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_post_portable_verification_"
                "runtime_readiness"
            )
        )
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolver.resolve_post_portable_verification_runtime_readiness(request)
        summary = resolver.build_post_portable_verification_runtime_readiness_summary(
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
            "resolve_post_portable_verification_runtime_readiness",
        )
        self.assertEqual(summary["request_id"], request["runtime_readiness_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(result["runtime_readiness_statement"][field], True, field)
        for field in EXPECTED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False, field)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_preserved(result)
        self.assert_safe_runtime_readiness_membrane(result)
        self.assert_predecessor_and_tokens_preserved(result)

        custom_request = build_request(
            runtime_readiness_scope=list(resolver.SUPPORTED_RUNTIME_READINESS_SCOPE)
        )
        custom_result = resolver.resolve_post_portable_verification_runtime_readiness(
            custom_request
        )
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            resolver.build_post_portable_verification_runtime_readiness_summary(
                custom_result
            )["failed_check_count"],
            0,
        )
        self.assert_official_scope_preserved(custom_result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        request = build_request()
        hostile_values = tuple(
            f"hostile-full-body-value-{index}"
            for index, _ in enumerate(HOSTILE_BODY_KEYS)
        )
        for basis_field in SELECTED_BASIS_FIELDS:
            basis = request[basis_field]
            for key, hostile_value in zip(HOSTILE_BODY_KEYS, hostile_values):
                basis[key] = hostile_value
            basis["nested_hostile_values"] = {
                "list": list(RAW_SENTINELS),
                "dict": {"sentinel": RAW_SENTINELS[0]},
            }
        original = copy.deepcopy(request)

        result = resolver.resolve_post_portable_verification_runtime_readiness(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_raw_sentinels(result, hostile_values)
        self.assert_official_scope_preserved(result)
        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_safe_runtime_readiness_membrane(result)
        self.assertEqual(request, original)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None] | None, Any],
            ...,
        ] = (
            ("explicit block intent", set_request_value("runtime_readiness_intent", "BLOCK_POST_PORTABLE_VERIFICATION_RUNTIME_READINESS"), None),
            ("missing request", None, None),
            ("non-mapping request", None, "not-a-mapping"),
            ("unsupported intent", set_request_value("runtime_readiness_intent", "UNSUPPORTED"), None),
            ("unsupported scope", set_request_value("runtime_readiness_scope", ["UNSUPPORTED_RUNTIME_READINESS_SCOPE_VALUE"]), None),
            ("missing runtime-readiness-boundary basis", set_request_value("selected_runtime_readiness_boundary_basis", {}), None),
            ("runtime-readiness-boundary not recorded", set_request_value("selected_runtime_readiness_boundary_result_outcome", "NOT_RECORDED"), None),
            ("runtime-readiness-boundary failed checks present", set_request_value("selected_runtime_readiness_boundary_failed_check_count", 1), None),
            ("runtime-readiness-boundary version not 0.1.0", set_request_value("selected_runtime_readiness_boundary_result_version", "0.2.0"), None),
            ("runtime-readiness-boundary did not declare review step", set_request_value("selected_runtime_readiness_boundary_declared_future_runtime_readiness_review_step", False), None),
            ("runtime-readiness-boundary already created runtime-readiness", set_request_value("selected_runtime_readiness_boundary_already_created_runtime_readiness", True), None),
            ("runtime-readiness-boundary already created runtime", set_request_value("selected_runtime_readiness_boundary_already_created_runtime", True), None),
            ("runtime-readiness-boundary authorized continuation", set_request_value("selected_runtime_readiness_boundary_already_authorized_continuation", True), None),
            ("runtime-readiness-boundary treated boundary as runtime-readiness", set_request_value("selected_runtime_readiness_boundary_treated_boundary_as_runtime_readiness", True), None),
            ("runtime-readiness-boundary treated boundary as runtime", set_request_value("selected_runtime_readiness_boundary_treated_boundary_as_runtime", True), None),
            ("runtime-readiness-boundary treated checkability as continuation", set_request_value("selected_runtime_readiness_boundary_treated_checkability_as_continuation", True), None),
            ("runtime-readiness-boundary treated final completion as runtime", set_request_value("selected_runtime_readiness_boundary_treated_final_completion_as_runtime", True), None),
            ("runtime-readiness-boundary treated final completion as continuation", set_request_value("selected_runtime_readiness_boundary_treated_final_completion_as_continuation", True), None),
            ("runtime-readiness-boundary treated currentness surface as runtime permission", set_request_value("selected_runtime_readiness_boundary_treated_currentness_surface_as_runtime_permission", True), None),
            ("runtime-readiness-boundary treated currentness surface as operation permission", set_request_value("selected_runtime_readiness_boundary_treated_currentness_surface_as_operation_permission", True), None),
            ("runtime-readiness-boundary authorized future work", set_request_value("selected_runtime_readiness_boundary_authorized_future_work", True), None),
            ("missing final-completion basis", set_request_value("selected_portable_verification_final_completion_basis", {}), None),
            ("final completion not recorded", set_request_value("selected_portable_verification_final_completion_result_outcome", "NOT_RECORDED"), None),
            ("final completion failed checks present", set_request_value("selected_portable_verification_final_completion_failed_check_count", 1), None),
            ("final-completion version not 0.1.0", set_request_value("selected_portable_verification_final_completion_result_version", "0.2.0"), None),
            ("missing post-portable currentness basis", set_request_value("selected_post_portable_verification_currentness_basis", {}), None),
            ("post-portable currentness checkability treated as continuation", set_request_value("selected_post_portable_currentness_surface_states_checkability_not_continuation", False), None),
            ("post-portable currentness authorized next work", set_request_value("selected_post_portable_currentness_surface_authorized_next_work", True), None),
            ("runtime-readiness created before review", set_request_value("runtime_readiness_created_before_review", True), None),
            ("runtime created", set_request_value("runtime_created", True), None),
            ("runtime boundary created", set_request_value("runtime_boundary_created", True), None),
            ("runtime step created", set_request_value("runtime_step_created", True), None),
            ("continuation authorized", set_request_value("continuation_authorized", True), None),
            ("runtime-readiness treated as runtime", set_non_claim("runtime_readiness_treated_as_runtime"), None),
            ("runtime-readiness treated as runtime boundary", set_non_claim("runtime_readiness_treated_as_runtime_boundary"), None),
            ("runtime-readiness treated as runtime step", set_non_claim("runtime_readiness_treated_as_runtime_step"), None),
            ("runtime-readiness treated as continuation", set_non_claim("runtime_readiness_treated_as_continuation"), None),
            ("runtime-readiness treated as source transfer", set_non_claim("runtime_readiness_treated_as_source_transfer"), None),
            ("runtime-readiness treated as source receipt", set_non_claim("runtime_readiness_treated_as_source_receipt"), None),
            ("runtime-readiness treated as reception authorization", set_non_claim("runtime_readiness_treated_as_reception_authorization"), None),
            ("runtime-readiness treated as source", set_non_claim("runtime_readiness_treated_as_source"), None),
            ("runtime-readiness treated as authority", set_non_claim("runtime_readiness_treated_as_authority"), None),
            ("runtime-readiness treated as currentness", set_non_claim("runtime_readiness_treated_as_currentness"), None),
            ("runtime-readiness treated as deployment", set_non_claim("runtime_readiness_treated_as_deployment"), None),
            ("runtime-readiness treated as public release", set_non_claim("runtime_readiness_treated_as_public_release"), None),
            ("runtime-readiness treated as operation permission", set_non_claim("runtime_readiness_treated_as_operation_permission"), None),
            ("runtime-readiness treated as reusable permission", set_non_claim("runtime_readiness_treated_as_reusable_permission"), None),
            ("runtime-readiness treated as follow-on work", set_non_claim("runtime_readiness_treated_as_follow_on_work"), None),
            ("source transfer occurred", set_non_claim("source_transfer_occurred"), None),
            ("source receipt occurred", set_non_claim("source_receipt_occurred"), None),
            ("reception authorization created", set_non_claim("reception_authorization_created"), None),
            ("source created", set_non_claim("source_created"), None),
            ("authority created", set_non_claim("authority_created"), None),
            ("currentness created", set_non_claim("currentness_created"), None),
            ("deployment created", set_non_claim("deployment_created"), None),
            ("public release created", set_non_claim("public_release_created"), None),
            ("operation permission created", set_non_claim("operation_permission_created"), None),
            ("reusable permission created", set_non_claim("reusable_permission_created"), None),
            ("derivative reception authorized", set_non_claim("derivative_reception_authorized"), None),
            ("vessel relation authorized", set_non_claim("vessel_relation_authorized"), None),
            ("another reception request authorized", set_non_claim("another_reception_request_authorized"), None),
            ("adoption created", set_non_claim("adoption_created"), None),
            ("receiving-context governance created", set_non_claim("receiving_context_governance_created"), None),
            ("publication flow created", set_non_claim("publication_flow_created"), None),
            ("follow-on work authorized", set_non_claim("follow_on_work_authorized"), None),
            ("artifact existence treated as runtime-readiness authority", set_non_claim("artifact_existence_treated_as_runtime_readiness_authority"), None),
            ("artifact path treated as currentness", set_non_claim("artifact_path_treated_as_currentness"), None),
            ("latest file posture treated as runtime-readiness authority", set_non_claim("latest_file_posture_treated_as_runtime_readiness_authority"), None),
            ("repo-local availability treated as runtime-readiness authority", set_non_claim("repo_local_availability_treated_as_runtime_readiness_authority"), None),
            ("hidden repo state used as runtime-readiness content", set_non_claim("hidden_repo_state_used_as_runtime_readiness_content"), None),
            ("hidden repo state used as runtime-readiness authority", set_non_claim("hidden_repo_state_used_as_runtime_readiness_authority"), None),
            ("selected basis not reference-shaped", set_request_value("reference_shaped_input_posture", False), None),
            ("raw full prior artifact body returned", set_non_claim("raw_full_prior_artifact_body_returned"), None),
            ("predecessor failure evidence hidden", set_request_value("predecessor_failure_hidden", True), None),
            ("predecessor failure evidence repaired", set_request_value("predecessor_failure_repaired", True), None),
            ("predecessor failure claimed passed", set_request_value("predecessor_failure_claimed_passed", True), None),
            ("consumed request reopened", set_non_claim("consumed_request_reopened"), None),
            ("authorization token reused", set_non_claim("authorization_token_reused"), None),
            ("required non-claim missing", remove_non_claim("runtime_created"), None),
            ("required non-claim flipped", set_non_claim("runtime_created"), None),
        )

        for name, mutate, raw_request in block_cases:
            with self.subTest(name=name):
                if raw_request is not None:
                    result = resolver.resolve_post_portable_verification_runtime_readiness(
                        raw_request
                    )
                elif mutate is None:
                    result = resolver.resolve_post_portable_verification_runtime_readiness(
                        None
                    )
                else:
                    request = build_request()
                    mutate(request)
                    result = resolver.resolve_post_portable_verification_runtime_readiness(
                        request
                    )
                self.assert_blocked_result(result)

    def test_path_and_write_behavior(self) -> None:
        request = build_request()
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            request_path = tmp_dir / "request.json"
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True), encoding="utf-8"
            )

            result = resolver.resolve_post_portable_verification_runtime_readiness_from_path(
                request_path
            )
            summary = resolver.build_post_portable_verification_runtime_readiness_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_post_portable_verification_runtime_readiness",
            )

            malformed_path = tmp_dir / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = (
                resolver.resolve_post_portable_verification_runtime_readiness_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_result(malformed_result)

            array_path = tmp_dir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_post_portable_verification_runtime_readiness_from_path(
                    array_path
                )
            )
            self.assert_blocked_result(array_result)

            missing_result = (
                resolver.resolve_post_portable_verification_runtime_readiness_from_path(
                    tmp_dir / "missing.json"
                )
            )
            self.assert_blocked_result(missing_result)

            patched_root = (
                tmp_dir
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", patched_root):
                first_path = resolver.write_post_portable_verification_runtime_readiness_result(
                    result
                )
                second_path = resolver.write_post_portable_verification_runtime_readiness_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn(
                "artifacts/"
                "integrity_host_v0_min_coexistence_post_portable_verification_"
                "runtime_readiness",
                first_path.as_posix(),
            )
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_fragments = (
                "actual_second_carrier_live_capture",
                "runtime_readiness_boundary",
                "final_completion_boundary",
                "portable_verification_closure",
                "cross_carrier_evidence",
                "/runtime/",
                "deployment",
                "public_release",
                "source_transfer",
                "source_receipt",
                "reception",
            )
            for fragment in forbidden_fragments:
                self.assertNotIn(fragment, first_path.as_posix())

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        selected_basis_originals = {
            field: copy.deepcopy(request[field]) for field in SELECTED_BASIS_FIELDS
        }
        posture_originals = {
            field: copy.deepcopy(request[field]) for field in POSTURE_FIELDS
        }
        scope_original = copy.deepcopy(request["runtime_readiness_scope"])
        non_claims_original = copy.deepcopy(request["declared_non_claims"])

        result = resolver.resolve_post_portable_verification_runtime_readiness(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)
        for field, expected in selected_basis_originals.items():
            self.assertEqual(request[field], expected)
        for field, expected in posture_originals.items():
            self.assertEqual(request[field], expected)
        self.assertEqual(request["runtime_readiness_scope"], scope_original)
        self.assertEqual(request["declared_non_claims"], non_claims_original)

    def test_predecessor_failure_and_token_preservation(self) -> None:
        request = build_request()
        result = resolver.resolve_post_portable_verification_runtime_readiness(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_predecessor_and_tokens_preserved(result)
        self.assertIs(
            result["runtime_readiness_statement"][
                "predecessor_failure_evidence_preserved"
            ],
            True,
        )
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(
            result["non_claims"]["predecessor_failure_claimed_passed"], False
        )


if __name__ == "__main__":
    unittest.main()
