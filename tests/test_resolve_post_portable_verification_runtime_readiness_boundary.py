"""Tests for the post-portable-verification runtime-readiness-boundary resolver.

This suite exercises runtime-readiness-boundary posture only. It is downstream
of post-portable-verification currentness compression and portable source-body
verification final completion. It records one future runtime-readiness review
step only, while preserving that runtime-readiness, runtime, continuation,
source transfer, source receipt, reception authorization, source, authority,
operative currentness, deployment, public release, operation permission,
reusable permission, adoption, receiving-context governance, publication flow,
and follow-on work are not created.
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

import resolve_post_portable_verification_runtime_readiness_boundary as resolver  # noqa: E402


TOP_LEVEL_SECTIONS = (
    "post_portable_verification_runtime_readiness_boundary_metadata",
    "declared_runtime_readiness_boundary_question",
    "selected_post_portable_verification_currentness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_portable_verification_final_completion_terminal_summary_basis",
    "selected_final_completion_artifact_basis",
    "selected_final_completion_boundary_basis",
    "selected_portable_verification_closure_basis",
    "selected_cross_carrier_evidence_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "runtime_readiness_boundary_only_posture",
    "one_future_runtime_readiness_review_step_posture",
    "portable_verification_final_completion_basis_preserved_posture",
    "post_portable_verification_currentness_basis_preserved_posture",
    "checkability_not_continuation_preserved_posture",
    "final_completion_not_runtime_posture",
    "final_completion_not_continuation_posture",
    "currentness_compression_not_operative_currentness_posture",
    "currentness_surface_not_runtime_permission_posture",
    "currentness_surface_not_operation_permission_posture",
    "runtime_readiness_not_created_posture",
    "runtime_not_created_posture",
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
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "runtime_readiness_boundary_scope",
    "runtime_readiness_boundary_checks",
    "runtime_readiness_boundary_statement",
    "runtime_readiness_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_portable_verification_runtime_readiness_boundary_summary",
)

SELECTED_BASIS_FIELDS = (
    "selected_post_portable_verification_currentness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_portable_verification_final_completion_terminal_summary_basis",
    "selected_final_completion_artifact_basis",
    "selected_final_completion_boundary_basis",
    "selected_portable_verification_closure_basis",
    "selected_cross_carrier_evidence_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "runtime_readiness_boundary_only_posture",
    "one_future_runtime_readiness_review_step_posture",
    "portable_verification_final_completion_basis_preserved_posture",
    "post_portable_verification_currentness_basis_preserved_posture",
    "checkability_not_continuation_preserved_posture",
    "final_completion_not_runtime_posture",
    "final_completion_not_continuation_posture",
    "currentness_compression_not_operative_currentness_posture",
    "currentness_surface_not_runtime_permission_posture",
    "currentness_surface_not_operation_permission_posture",
    "runtime_readiness_not_created_posture",
    "runtime_not_created_posture",
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
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

OFFICIAL_SCOPE_VALUES = (
    "CHECKABILITY_NOT_CONTINUATION_PRESERVED",
    "CURRENTNESS_COMPRESSION_NOT_OPERATIVE_CURRENTNESS",
    "CURRENTNESS_SURFACE_NOT_RUNTIME_PERMISSION",
    "CURRENTNESS_SURFACE_NOT_OPERATION_PERMISSION",
    "RUNTIME_READINESS_NOT_CREATED",
    "RUNTIME_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_READINESS_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_READINESS_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_READINESS_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_READINESS_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_READINESS_BOUNDARY_INTENT_UNSUPPORTED",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_BASIS_MISSING",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_TREATED_AS_RUNTIME_PERMISSION",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_TREATED_AS_OPERATION_PERMISSION",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_TREATED_AS_OPERATIVE_CURRENTNESS",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_AUTHORIZED_NEXT_WORK",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_CREATED_RUNTIME",
    "POST_PORTABLE_VERIFICATION_CURRENTNESS_SURFACE_CREATED_CONTINUATION",
    "FINAL_COMPLETION_BASIS_MISSING",
    "FINAL_COMPLETION_NOT_RECORDED",
    "FINAL_COMPLETION_FAILED_CHECKS_PRESENT",
    "FINAL_COMPLETION_VERSION_NOT_0_1_0",
    "FINAL_COMPLETION_NOT_BOUNDED",
    "FINAL_COMPLETION_TREATED_AS_RUNTIME",
    "FINAL_COMPLETION_TREATED_AS_CONTINUATION",
    "FINAL_COMPLETION_TREATED_AS_SOURCE_TRANSFER",
    "FINAL_COMPLETION_TREATED_AS_SOURCE_RECEIPT",
    "FINAL_COMPLETION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "FINAL_COMPLETION_TREATED_AS_SOURCE",
    "FINAL_COMPLETION_TREATED_AS_AUTHORITY",
    "FINAL_COMPLETION_TREATED_AS_CURRENTNESS",
    "FINAL_COMPLETION_TREATED_AS_DEPLOYMENT",
    "FINAL_COMPLETION_TREATED_AS_PUBLIC_RELEASE",
    "FINAL_COMPLETION_TREATED_AS_OPERATION_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_REUSABLE_PERMISSION",
    "FINAL_COMPLETION_TREATED_AS_FOLLOW_ON_WORK",
    "FINAL_COMPLETION_TERMINAL_SUMMARY_SELECTED_NEXT_BOUNDARY_AUTOMATICALLY",
    "FINAL_COMPLETION_TERMINAL_SUMMARY_AUTHORIZED_FUTURE_WORK",
    "PORTABLE_VERIFICATION_FINAL_COMPLETION_TREATED_AS_SYSTEM_COMPLETION",
    "CHECKABILITY_TREATED_AS_CONTINUATION",
    "RUNTIME_READINESS_BOUNDARY_TREATED_AS_RUNTIME_READINESS",
    "RUNTIME_READINESS_BOUNDARY_TREATED_AS_RUNTIME",
    "RUNTIME_READINESS_CREATED",
    "RUNTIME_CREATED",
    "CONTINUATION_AUTHORIZED",
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
    "UNSUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_READINESS_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_READINESS_BOUNDARY_REQUEST_UNREADABLE",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "runtime_readiness_boundary_recorded",
    "one_future_runtime_readiness_review_step_declared",
    "portable_verification_final_completion_basis_preserved",
    "post_portable_verification_currentness_basis_preserved",
    "checkability_not_continuation_preserved",
    "final_completion_not_runtime",
    "final_completion_not_continuation",
    "currentness_compression_not_operative_currentness",
    "currentness_surface_not_runtime_permission",
    "currentness_surface_not_operation_permission",
    "runtime_readiness_not_created",
    "runtime_not_created",
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
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

EXPECTED_FALSE_NON_CLAIMS = (
    "runtime_readiness_created",
    "runtime_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_readiness_boundary_treated_as_runtime_readiness",
    "runtime_readiness_boundary_treated_as_runtime",
    "portable_verification_final_completion_treated_as_runtime",
    "portable_verification_final_completion_treated_as_continuation",
    "portable_verification_final_completion_treated_as_source_transfer",
    "portable_verification_final_completion_treated_as_source_receipt",
    "portable_verification_final_completion_treated_as_reception_authorization",
    "portable_verification_final_completion_treated_as_source",
    "portable_verification_final_completion_treated_as_authority",
    "portable_verification_final_completion_treated_as_currentness",
    "portable_verification_final_completion_treated_as_deployment",
    "portable_verification_final_completion_treated_as_public_release",
    "portable_verification_final_completion_treated_as_operation_permission",
    "post_portable_verification_currentness_surface_treated_as_runtime_permission",
    "post_portable_verification_currentness_surface_treated_as_operation_permission",
    "post_portable_verification_currentness_surface_treated_as_operative_currentness",
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

SENSITIVE_KEYS = (
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
    "raw_runtime_readiness_body",
    "raw_runtime_body",
    "runtime_readiness_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

HOSTILE_SENTINELS = (
    "RAW_RUNTIME_READINESS_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

HOSTILE_VALUES = (
    "HOSTILE_RUNTIME_READINESS_FULL_BODY_VALUE_MUST_NOT_RETURN",
    "HOSTILE_RUNTIME_BODY_VALUE_MUST_NOT_RETURN",
)

FORBIDDEN_WRITE_ROOT_FRAGMENTS = (
    "actual_second_carrier_live_capture",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion_boundary",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_portable_verification_closure",
    "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
    "source_transfer",
    "source-transfer",
    "source_receipt",
    "source-receipt",
    "reception",
    "deployment",
    "public_release",
    "public-release",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    request = (
        resolver.build_declared_post_portable_verification_runtime_readiness_boundary_request()
    )
    request.update(overrides)
    return request


def resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_post_portable_verification_runtime_readiness_boundary(request)


def block_from_request(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = build_request()
    mutator(request)
    return resolve(request)


def set_non_claim(request: dict[str, Any], key: str, value: bool = True) -> None:
    request.setdefault("declared_non_claims", {})[key] = value


def set_posture_value(request: dict[str, Any], key: str, value: bool = False) -> None:
    request[key] = {"declared": value, "value": value}


class PostPortableVerificationRuntimeReadinessBoundaryTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("runtime_readiness_boundary_checks", ()):
            code = check.get("block_code") or check.get("failure_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "runtime_readiness_boundary_statement",
            "runtime_readiness_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name, {})
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                self.assertIsInstance(value, bool, f"{section_name}.{key} is not bool")

    def assert_no_raw_or_hidden_sentinels(
        self,
        result: Mapping[str, Any],
        extra_forbidden_values: tuple[str, ...] = (),
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS + extra_forbidden_values:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("runtime_readiness_boundary_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-runtime-readiness-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in scope:
            self.assertNotEqual(value, "[bounded-runtime-readiness-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")
        for value in resolver.SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE:
            self.assertNotEqual(value, "[bounded-runtime-readiness-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")

    def assert_no_runtime_or_escalated_posture_created(
        self, result: Mapping[str, Any]
    ) -> None:
        non_claims = result["non_claims"]
        statement = result["runtime_readiness_boundary_statement"]
        for key in (
            "runtime_readiness_created",
            "runtime_created",
            "continuation_authorized",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "runtime_readiness_boundary_treated_as_runtime_readiness",
            "runtime_readiness_boundary_treated_as_runtime",
            "portable_verification_final_completion_treated_as_runtime",
            "portable_verification_final_completion_treated_as_continuation",
            "post_portable_verification_currentness_surface_treated_as_runtime_permission",
            "post_portable_verification_currentness_surface_treated_as_operation_permission",
            "post_portable_verification_currentness_surface_treated_as_operative_currentness",
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
            "follow_on_work_authorized",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertFalse(non_claims[key], key)
        for key in (
            "runtime_readiness_not_created",
            "runtime_not_created",
            "continuation_not_authorized",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "follow_on_work_not_authorized",
            "hidden_repo_state_excluded",
            "hidden_repo_state_not_used_as_runtime_readiness_authority",
            "repo_local_availability_not_runtime_readiness_authority",
            "artifact_existence_not_runtime_readiness_authority",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertTrue(statement[key], key)

    def assert_safe_blocked_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsInstance(result["block"], Mapping)
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_runtime_or_escalated_posture_created(result)
        non_claims = result["non_claims"]
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertFalse(non_claims[key], key)
        self.assertTrue(
            result["runtime_readiness_boundary_statement"][
                "predecessor_failure_evidence_preserved"
            ]
        )

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_portable_verification_runtime_readiness_boundary",
            "resolve_post_portable_verification_runtime_readiness_boundary_from_path",
            "write_post_portable_verification_runtime_readiness_boundary_result",
            "build_post_portable_verification_runtime_readiness_boundary_summary",
            "build_declared_post_portable_verification_runtime_readiness_boundary_request",
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
            "SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_portable_verification_runtime_readiness_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary"
            )
        )
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolve(request)
        summary = (
            resolver.build_post_portable_verification_runtime_readiness_boundary_summary(
                result
            )
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["runtime_readiness_boundary_request_id"])
        self.assertEqual(
            result["post_portable_verification_runtime_readiness_boundary_metadata"][
                "post_portable_verification_runtime_readiness_boundary_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            result["post_portable_verification_runtime_readiness_boundary_metadata"][
                "resolver_module"
            ],
            resolver.RESOLVER_MODULE,
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(
                result["runtime_readiness_boundary_statement"][field],
                True,
                field,
            )
        for field in EXPECTED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False, field)

        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_no_runtime_or_escalated_posture_created(result)

    def test_official_enum_strings_preserved_and_all_supported_scope_records(
        self,
    ) -> None:
        result = resolve(build_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)
        for check in result["runtime_readiness_boundary_checks"]:
            code = check.get("block_code") or check.get("failure_code")
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
                self.assertNotEqual(code, "[bounded-runtime-readiness-redacted]")
                self.assertNotEqual(code, "[bounded-redacted-raw-or-hidden-state]")

        all_scope_request = build_request(
            runtime_readiness_boundary_scope=list(
                resolver.SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE
            )
        )
        all_scope_result = resolve(all_scope_request)
        self.assertEqual(all_scope_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            set(all_scope_result["runtime_readiness_boundary_scope"]),
            set(resolver.SUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE),
        )
        self.assert_official_scope_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained_without_mutating_request(
        self,
    ) -> None:
        request = build_request()
        for section_name in SELECTED_BASIS_FIELDS:
            request[section_name] = copy.deepcopy(request[section_name])
            for index, key in enumerate(SENSITIVE_KEYS):
                request[section_name][key] = HOSTILE_VALUES[index % len(HOSTILE_VALUES)]
            request[section_name]["nested"] = {
                "list": [
                    "reference-shaped-safe-item",
                    "RAW_RUNTIME_READINESS_BOUNDARY_BODY_MUST_NOT_RETURN",
                    {"inner": "RAW_RUNTIME_BODY_MUST_NOT_RETURN"},
                    {"prior": "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN"},
                    {"hidden": "HIDDEN_REPO_STATE_MUST_NOT_RETURN"},
                ],
                "official_scope_echo": "CHECKABILITY_NOT_CONTINUATION_PRESERVED",
            }

        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_raw_or_hidden_sentinels(result, HOSTILE_VALUES)
        self.assert_official_scope_preserved(result)
        self.assert_public_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_runtime_or_escalated_posture_created(result)

    def test_representative_blocking_behavior(self) -> None:
        special_cases: tuple[tuple[str, Callable[[], dict[str, Any]]], ...] = (
            ("missing request", lambda: resolve(None)),
            (
                "non-mapping request",
                lambda: resolver.resolve_post_portable_verification_runtime_readiness_boundary(
                    []
                ),
            ),
        )
        for name, case in special_cases:
            with self.subTest(name=name):
                self.assert_safe_blocked_result(case())

        block_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            (
                "explicit block intent",
                lambda r: r.__setitem__(
                    "runtime_readiness_boundary_intent",
                    "BLOCK_POST_PORTABLE_VERIFICATION_RUNTIME_READINESS_BOUNDARY",
                ),
            ),
            (
                "unsupported intent",
                lambda r: r.__setitem__(
                    "runtime_readiness_boundary_intent", "UNSUPPORTED"
                ),
            ),
            (
                "missing question",
                lambda r: r.__setitem__("runtime_readiness_boundary_question", ""),
            ),
            (
                "unsupported scope",
                lambda r: r.__setitem__(
                    "runtime_readiness_boundary_scope",
                    ["UNSUPPORTED_RUNTIME_READINESS_BOUNDARY_SCOPE_VALUE"],
                ),
            ),
            (
                "missing post-portable currentness surface basis",
                lambda r: r.__setitem__(
                    "selected_post_portable_verification_currentness_basis", {}
                ),
            ),
            (
                "currentness surface treated as runtime permission",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_treated_as_runtime_permission",
                    True,
                ),
            ),
            (
                "currentness surface treated as operation permission",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_treated_as_operation_permission",
                    True,
                ),
            ),
            (
                "currentness surface treated as operative currentness",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_treated_as_operative_currentness",
                    True,
                ),
            ),
            (
                "currentness surface authorized next work",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_authorized_next_work",
                    True,
                ),
            ),
            (
                "currentness surface created runtime",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_created_runtime", True
                ),
            ),
            (
                "currentness surface created continuation",
                lambda r: r.__setitem__(
                    "selected_post_portable_currentness_surface_created_continuation",
                    True,
                ),
            ),
            (
                "missing final-completion basis",
                lambda r: r.__setitem__("selected_final_completion_artifact_basis", {}),
            ),
            (
                "final completion not recorded",
                lambda r: r.__setitem__(
                    "selected_final_completion_result_outcome", "NOT_RECORDED"
                ),
            ),
            (
                "final completion failed checks present",
                lambda r: r.__setitem__("selected_final_completion_failed_check_count", 1),
            ),
            (
                "final-completion version not 0.1.0",
                lambda r: r.__setitem__(
                    "selected_final_completion_result_version", "9.9.9"
                ),
            ),
            (
                "final completion not bounded",
                lambda r: r.__setitem__(
                    "selected_final_completion_bounded_final_completion_recorded",
                    False,
                ),
            ),
            (
                "final completion treated as runtime",
                lambda r: r.__setitem__("selected_final_completion_treated_as_runtime", True),
            ),
            (
                "final completion treated as continuation",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_continuation", True
                ),
            ),
            (
                "final completion treated as source transfer",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_source_transfer", True
                ),
            ),
            (
                "final completion treated as source receipt",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_source_receipt", True
                ),
            ),
            (
                "final completion treated as reception authorization",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_reception_authorization", True
                ),
            ),
            (
                "final completion treated as source",
                lambda r: r.__setitem__("selected_final_completion_treated_as_source", True),
            ),
            (
                "final completion treated as authority",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_authority", True
                ),
            ),
            (
                "final completion treated as currentness",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_currentness", True
                ),
            ),
            (
                "final completion treated as deployment",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_deployment", True
                ),
            ),
            (
                "final completion treated as public release",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_public_release", True
                ),
            ),
            (
                "final completion treated as operation permission",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_operation_permission", True
                ),
            ),
            (
                "final completion treated as reusable permission",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_reusable_permission", True
                ),
            ),
            (
                "final completion treated as follow-on work",
                lambda r: r.__setitem__(
                    "selected_final_completion_treated_as_follow_on_work", True
                ),
            ),
            (
                "final-completion terminal summary selected next boundary automatically",
                lambda r: r.__setitem__(
                    "selected_final_completion_terminal_summary_selected_next_boundary_automatically",
                    True,
                ),
            ),
            (
                "final-completion terminal summary authorized future work",
                lambda r: r.__setitem__(
                    "selected_final_completion_terminal_summary_authorized_future_work",
                    True,
                ),
            ),
            (
                "portable verification final completion treated as system completion",
                lambda r: r.__setitem__(
                    "runtime_readiness_boundary_scope",
                    ["PORTABLE_VERIFICATION_FINAL_COMPLETION_TREATED_AS_SYSTEM_COMPLETION"],
                ),
            ),
            (
                "checkability treated as continuation",
                lambda r: set_non_claim(r, "checkability_treated_as_continuation"),
            ),
            (
                "runtime-readiness boundary treated as runtime-readiness",
                lambda r: set_non_claim(
                    r, "runtime_readiness_boundary_treated_as_runtime_readiness"
                ),
            ),
            (
                "runtime-readiness boundary treated as runtime",
                lambda r: set_non_claim(r, "runtime_readiness_boundary_treated_as_runtime"),
            ),
            (
                "runtime-readiness created",
                lambda r: set_non_claim(r, "runtime_readiness_created"),
            ),
            ("runtime created", lambda r: set_non_claim(r, "runtime_created")),
            (
                "continuation authorized",
                lambda r: set_non_claim(r, "continuation_authorized"),
            ),
            (
                "source transfer occurred",
                lambda r: set_non_claim(r, "source_transfer_occurred"),
            ),
            (
                "source receipt occurred",
                lambda r: set_non_claim(r, "source_receipt_occurred"),
            ),
            (
                "reception authorization created",
                lambda r: set_non_claim(r, "reception_authorization_created"),
            ),
            ("source created", lambda r: set_non_claim(r, "source_created")),
            ("authority created", lambda r: set_non_claim(r, "authority_created")),
            ("currentness created", lambda r: set_non_claim(r, "currentness_created")),
            ("deployment created", lambda r: set_non_claim(r, "deployment_created")),
            (
                "public release created",
                lambda r: set_non_claim(r, "public_release_created"),
            ),
            (
                "operation permission created",
                lambda r: set_non_claim(r, "operation_permission_created"),
            ),
            (
                "reusable permission created",
                lambda r: set_non_claim(r, "reusable_permission_created"),
            ),
            (
                "derivative reception authorized",
                lambda r: set_non_claim(r, "derivative_reception_authorized"),
            ),
            (
                "vessel relation authorized",
                lambda r: set_non_claim(r, "vessel_relation_authorized"),
            ),
            (
                "adoption created",
                lambda r: set_non_claim(r, "adoption_created"),
            ),
            (
                "receiving-context governance created",
                lambda r: set_non_claim(r, "receiving_context_governance_created"),
            ),
            (
                "publication flow created",
                lambda r: set_non_claim(r, "publication_flow_created"),
            ),
            (
                "follow-on work authorized",
                lambda r: set_non_claim(r, "follow_on_work_authorized"),
            ),
            (
                "artifact existence treated as runtime-readiness authority",
                lambda r: set_non_claim(
                    r, "artifact_existence_treated_as_runtime_readiness_authority"
                ),
            ),
            (
                "artifact path treated as currentness",
                lambda r: set_non_claim(r, "artifact_path_treated_as_currentness"),
            ),
            (
                "latest file posture treated as runtime-readiness authority",
                lambda r: set_non_claim(
                    r, "latest_file_posture_treated_as_runtime_readiness_authority"
                ),
            ),
            (
                "repo-local availability treated as runtime-readiness authority",
                lambda r: set_non_claim(
                    r, "repo_local_availability_treated_as_runtime_readiness_authority"
                ),
            ),
            (
                "hidden repo state used as runtime-readiness content",
                lambda r: set_non_claim(
                    r, "hidden_repo_state_used_as_runtime_readiness_content"
                ),
            ),
            (
                "hidden repo state used as runtime-readiness authority",
                lambda r: set_non_claim(
                    r, "hidden_repo_state_used_as_runtime_readiness_authority"
                ),
            ),
            (
                "selected basis not reference-shaped",
                lambda r: set_posture_value(r, "selected_basis_reference_shape_posture"),
            ),
            (
                "raw full prior artifact body returned",
                lambda r: set_non_claim(r, "raw_full_prior_artifact_body_returned"),
            ),
            (
                "predecessor failure hidden/repaired/claimed passed",
                lambda r: r.__setitem__("predecessor_failure_hidden", True),
            ),
            (
                "consumed request reopened",
                lambda r: set_non_claim(r, "consumed_request_reopened"),
            ),
            (
                "authorization token reused",
                lambda r: set_non_claim(r, "authorization_token_reused"),
            ),
            (
                "required non-claim missing",
                lambda r: r["declared_non_claims"].__delitem__("source_created"),
            ),
        )

        for name, mutator in block_cases:
            with self.subTest(name=name):
                self.assert_safe_blocked_result(block_from_request(mutator))

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request = build_request()
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = (
                resolver.resolve_post_portable_verification_runtime_readiness_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                result["post_portable_verification_runtime_readiness_boundary_metadata"][
                    "post_portable_verification_runtime_readiness_boundary_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                result["post_portable_verification_runtime_readiness_boundary_metadata"][
                    "resolver_module"
                ],
                resolver.RESOLVER_MODULE,
            )

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_safe_blocked_result(
                resolver.resolve_post_portable_verification_runtime_readiness_boundary_from_path(
                    malformed_path
                )
            )

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_safe_blocked_result(
                resolver.resolve_post_portable_verification_runtime_readiness_boundary_from_path(
                    array_path
                )
            )
            self.assert_safe_blocked_result(
                resolver.resolve_post_portable_verification_runtime_readiness_boundary_from_path(
                    root / "missing.json"
                )
            )

            output_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = (
                    resolver.write_post_portable_verification_runtime_readiness_boundary_result(
                        result
                    )
                )
                written_again = (
                    resolver.write_post_portable_verification_runtime_readiness_boundary_result(
                        result
                    )
                )

            self.assertTrue(written.parent.exists())
            self.assertTrue(written.exists())
            self.assertTrue(written_again.exists())
            self.assertNotEqual(written, written_again)
            self.assertTrue(written_again.stem.endswith("_001"))
            loaded = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(loaded["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary",
                written.as_posix(),
            )
            for fragment in FORBIDDEN_WRITE_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, written.as_posix())
                self.assertNotIn(fragment, written_again.as_posix())

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)
        for field in SELECTED_BASIS_FIELDS + POSTURE_FIELDS:
            self.assertEqual(request[field], original[field], field)
        self.assertEqual(
            request["runtime_readiness_boundary_scope"],
            original["runtime_readiness_boundary_scope"],
        )
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_predecessor_failure_preservation_and_token_closure(self) -> None:
        result = resolve(build_request())
        summary = (
            resolver.build_post_portable_verification_runtime_readiness_boundary_summary(
                result
            )
        )
        statement = result["runtime_readiness_boundary_statement"]
        non_claims = result["non_claims"]
        self.assertTrue(statement["predecessor_failure_evidence_preserved"])
        self.assertTrue(summary["predecessor_failure_evidence_preserved"])
        self.assertFalse(non_claims["predecessor_failure_repaired"])
        self.assertFalse(non_claims["predecessor_failure_hidden"])
        self.assertFalse(non_claims["predecessor_failure_claimed_passed"])
        self.assertTrue(statement["consumed_request_token_remains_closed"])
        self.assertTrue(statement["authorization_token_reuse_blocked"])
        self.assertTrue(summary["consumed_request_token_remains_closed"])
        self.assertTrue(summary["authorization_token_reuse_blocked"])
        self.assertFalse(non_claims["consumed_request_reopened"])
        self.assertFalse(non_claims["authorization_token_reused"])


if __name__ == "__main__":
    unittest.main()
