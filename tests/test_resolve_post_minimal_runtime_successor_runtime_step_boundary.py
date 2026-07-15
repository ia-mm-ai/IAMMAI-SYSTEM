"""Tests for the post-minimal-runtime successor-runtime-step-boundary resolver.

This suite exercises successor-runtime-step-boundary posture only. It is
downstream of minimal runtime, records one bounded successor-runtime-step-
boundary posture only, declares one future successor-runtime-step review only,
and preserves that successor runtime step, runtime hosting, ongoing runtime,
reusable runtime permission, continuation, source transfer, source receipt,
reception authorization, source, authority, currentness, deployment, public
release, operation permission, reusable permission, adoption, receiving-context
governance, publication flow, and follow-on work are not created.
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

import resolve_post_minimal_runtime_successor_runtime_step_boundary as resolver  # noqa: E402


TOP_LEVEL_SECTIONS = (
    "post_minimal_runtime_successor_runtime_step_boundary_metadata",
    "declared_successor_runtime_step_boundary_question",
    "selected_minimal_runtime_basis",
    "selected_minimal_runtime_terminal_summary_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "successor_runtime_step_boundary_spec_only_posture",
    "one_future_successor_runtime_step_review_posture",
    "minimal_runtime_basis_preserved_posture",
    "minimal_runtime_not_successor_runtime_step_posture",
    "bounded_runtime_result_or_refusal_not_successor_authorization_posture",
    "successor_runtime_step_boundary_not_successor_runtime_step_posture",
    "successor_runtime_step_boundary_not_runtime_hosting_posture",
    "successor_runtime_step_boundary_not_ongoing_runtime_posture",
    "successor_runtime_step_boundary_not_continuation_posture",
    "successor_runtime_step_not_created_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
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
    "repo_local_availability_not_successor_runtime_step_boundary_authority_posture",
    "artifact_existence_not_successor_runtime_step_boundary_authority_posture",
    "latest_file_posture_not_successor_runtime_step_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "successor_runtime_step_boundary_scope",
    "successor_runtime_step_boundary_checks",
    "successor_runtime_step_boundary_statement",
    "successor_runtime_step_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_minimal_runtime_successor_runtime_step_boundary_summary",
)

SELECTED_BASIS_FIELDS = (
    "selected_minimal_runtime_basis",
    "selected_minimal_runtime_terminal_summary_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
)

POSTURE_FIELDS = (
    "successor_runtime_step_boundary_spec_only_posture",
    "one_future_successor_runtime_step_review_posture",
    "minimal_runtime_basis_preserved_posture",
    "minimal_runtime_not_successor_runtime_step_posture",
    "bounded_runtime_result_or_refusal_not_successor_authorization_posture",
    "successor_runtime_step_boundary_not_successor_runtime_step_posture",
    "successor_runtime_step_boundary_not_runtime_hosting_posture",
    "successor_runtime_step_boundary_not_ongoing_runtime_posture",
    "successor_runtime_step_boundary_not_continuation_posture",
    "successor_runtime_step_not_created_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
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
    "repo_local_availability_not_successor_runtime_step_boundary_authority_posture",
    "artifact_existence_not_successor_runtime_step_boundary_authority_posture",
    "latest_file_posture_not_successor_runtime_step_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
)

OFFICIAL_SCOPE_VALUES = (
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_NOT_CONTINUATION",
    "MINIMAL_RUNTIME_NOT_SUCCESSOR_RUNTIME_STEP",
    "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_NOT_SUCCESSOR_AUTHORIZATION",
    "SUCCESSOR_RUNTIME_STEP_NOT_CREATED",
    "RUNTIME_HOSTING_NOT_CREATED",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "REPO_LOCAL_AVAILABILITY_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_QUESTION_UNDECLARED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_INTENT_UNSUPPORTED",
    "MINIMAL_RUNTIME_BASIS_MISSING",
    "MINIMAL_RUNTIME_NOT_RECORDED",
    "MINIMAL_RUNTIME_FAILED_CHECKS_PRESENT",
    "MINIMAL_RUNTIME_VERSION_NOT_0_1_0",
    "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_MINIMAL_RUNTIME_STEP",
    "MINIMAL_RUNTIME_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    "MINIMAL_RUNTIME_ALREADY_CREATED_RUNTIME_HOSTING",
    "MINIMAL_RUNTIME_ALREADY_CREATED_ONGOING_RUNTIME",
    "MINIMAL_RUNTIME_ALREADY_CREATED_SUCCESSOR_RUNTIME_STEP",
    "MINIMAL_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION_BEYOND_SINGLE_STEP",
    "MINIMAL_RUNTIME_TREATED_AS_RUNTIME_HOSTING",
    "MINIMAL_RUNTIME_TREATED_AS_ONGOING_RUNTIME",
    "MINIMAL_RUNTIME_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    "MINIMAL_RUNTIME_TREATED_AS_CONTINUATION",
    "MINIMAL_RUNTIME_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_SUCCESSOR",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_CREATED_BEFORE_REVIEW",
    "SUCCESSOR_RUNTIME_STEP_CREATED",
    "RUNTIME_HOSTING_CREATED",
    "ONGOING_RUNTIME_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_SOURCE",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_AUTHORITY",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SUCCESSOR_RUNTIME_STEP_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_REQUEST_UNREADABLE",
)

EXPECTED_TRUE_STATEMENT_FIELDS = (
    "successor_runtime_step_boundary_recorded",
    "one_future_successor_runtime_step_review_declared",
    "minimal_runtime_basis_preserved",
    "minimal_runtime_not_successor_runtime_step",
    "bounded_runtime_result_or_refusal_not_successor_authorization",
    "successor_runtime_step_boundary_not_successor_runtime_step",
    "successor_runtime_step_boundary_not_runtime_hosting",
    "successor_runtime_step_boundary_not_ongoing_runtime",
    "successor_runtime_step_boundary_not_continuation",
    "successor_runtime_step_not_created",
    "runtime_hosting_not_created",
    "ongoing_runtime_not_created",
    "reusable_runtime_permission_not_created",
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
    "hidden_repo_state_not_used_as_successor_runtime_step_boundary_authority",
    "repo_local_availability_not_successor_runtime_step_boundary_authority",
    "artifact_existence_not_successor_runtime_step_boundary_authority",
    "latest_file_posture_not_successor_runtime_step_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
)

EXPECTED_FALSE_NON_CLAIMS = (
    "successor_runtime_step_created",
    "runtime_hosting_created",
    "ongoing_runtime_created",
    "reusable_runtime_permission_created",
    "continuation_authorized",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "successor_runtime_step_boundary_treated_as_successor_runtime_step",
    "successor_runtime_step_boundary_treated_as_runtime_hosting",
    "successor_runtime_step_boundary_treated_as_ongoing_runtime",
    "successor_runtime_step_boundary_treated_as_continuation",
    "successor_runtime_step_boundary_treated_as_source_transfer",
    "successor_runtime_step_boundary_treated_as_source_receipt",
    "successor_runtime_step_boundary_treated_as_reception_authorization",
    "successor_runtime_step_boundary_treated_as_source",
    "successor_runtime_step_boundary_treated_as_authority",
    "successor_runtime_step_boundary_treated_as_currentness",
    "successor_runtime_step_boundary_treated_as_deployment",
    "successor_runtime_step_boundary_treated_as_public_release",
    "successor_runtime_step_boundary_treated_as_operation_permission",
    "successor_runtime_step_boundary_treated_as_reusable_permission",
    "successor_runtime_step_boundary_treated_as_follow_on_work",
    "minimal_runtime_treated_as_successor_runtime_step",
    "minimal_runtime_treated_as_runtime_hosting",
    "minimal_runtime_treated_as_ongoing_runtime",
    "minimal_runtime_treated_as_continuation",
    "bounded_runtime_result_or_refusal_authorized_successor",
    "artifact_existence_treated_as_successor_runtime_step_boundary_authority",
    "artifact_path_treated_as_currentness",
    "latest_file_posture_treated_as_successor_runtime_step_boundary_authority",
    "repo_local_availability_treated_as_successor_runtime_step_boundary_authority",
    "hidden_repo_state_used_as_successor_runtime_step_boundary_content",
    "hidden_repo_state_used_as_successor_runtime_step_boundary_authority",
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
    "RAW_SUCCESSOR_RUNTIME_STEP_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RUNTIME_STEP_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
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
    "raw_minimal_runtime_body",
    "raw_successor_runtime_step_boundary_body",
    "raw_successor_runtime_step_body",
    "raw_runtime_hosting_body",
    "raw_ongoing_runtime_body",
    "raw_runtime_body",
    "runtime_readiness_body",
    "runtime_boundary_body",
    "minimal_runtime_body",
    "successor_runtime_step_boundary_body",
    "successor_runtime_step_body",
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

REDACTION_PLACEHOLDERS = (
    "[bounded-successor-runtime-step-boundary-redacted]",
    "[bounded-redacted-raw-or-hidden-state]",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_post_minimal_runtime_successor_runtime_step_boundary_request(
        overrides=overrides or None
    )


def set_request_value(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[key] = value

    return mutate


def remove_request_keys(*keys: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        for key in keys:
            request.pop(key, None)

    return mutate


def set_non_claim(key: str, value: Any = True) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = value

    return mutate


def clear_basis(field: str, shortcut_path_key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[field] = {}
        request[shortcut_path_key] = ""

    return mutate


def missing_minimal_runtime_basis(request: dict[str, Any]) -> None:
    request["selected_minimal_runtime_basis"] = {}
    request["selected_minimal_runtime_terminal_summary_basis"] = {}
    request["selected_minimal_runtime_result_path"] = ""


class PostMinimalRuntimeSuccessorRuntimeStepBoundaryTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in result.get("successor_runtime_step_boundary_checks", []):
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "successor_runtime_step_boundary_statement",
            "successor_runtime_step_boundary_non_meaning",
            "non_claims",
        ):
            section = result[section_name]
            for key, value in section.items():
                self.assertIs(type(value), bool, f"{section_name}.{key}")
        for check in result["successor_runtime_step_boundary_checks"]:
            self.assertIs(type(check["passed"]), bool)

    def assert_no_raw_sentinels(
        self, result: Mapping[str, Any], extra_forbidden: tuple[str, ...] = ()
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS + extra_forbidden:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result["successor_runtime_step_boundary_scope"]
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        for value in scope:
            self.assertNotIn(value, REDACTION_PLACEHOLDERS)
        for supported_value in resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE:
            self.assertIn(supported_value, resolver.SUPPORTED_SCOPE_VALUES)
            self.assertNotIn(supported_value, REDACTION_PLACEHOLDERS)

    def assert_successor_runtime_step_boundary_membrane(
        self, result: Mapping[str, Any]
    ) -> None:
        statement = result["successor_runtime_step_boundary_statement"]
        non_claims = result["non_claims"]
        self.assertIs(statement["minimal_runtime_not_successor_runtime_step"], True)
        self.assertIs(
            statement["bounded_runtime_result_or_refusal_not_successor_authorization"],
            True,
        )
        self.assertIs(
            statement["successor_runtime_step_boundary_not_successor_runtime_step"],
            True,
        )
        self.assertIs(statement["successor_runtime_step_boundary_not_runtime_hosting"], True)
        self.assertIs(statement["successor_runtime_step_boundary_not_ongoing_runtime"], True)
        self.assertIs(statement["successor_runtime_step_boundary_not_continuation"], True)
        self.assertIs(statement["successor_runtime_step_not_created"], True)
        self.assertIs(statement["runtime_hosting_not_created"], True)
        self.assertIs(statement["ongoing_runtime_not_created"], True)
        self.assertIs(statement["reusable_runtime_permission_not_created"], True)
        self.assertIs(statement["continuation_not_authorized"], True)
        self.assertIs(statement["source_transfer_not_created"], True)
        self.assertIs(statement["source_receipt_not_created"], True)
        self.assertIs(statement["reception_authorization_not_created"], True)
        self.assertIs(statement["source_not_created"], True)
        self.assertIs(statement["authority_not_created"], True)
        self.assertIs(statement["currentness_not_created"], True)
        self.assertIs(statement["deployment_not_created"], True)
        self.assertIs(statement["public_release_not_created"], True)
        self.assertIs(statement["operation_permission_not_created"], True)
        self.assertIs(statement["follow_on_work_not_authorized"], True)
        self.assertIs(non_claims["successor_runtime_step_created"], False)
        self.assertIs(non_claims["runtime_hosting_created"], False)
        self.assertIs(non_claims["ongoing_runtime_created"], False)
        self.assertIs(non_claims["reusable_runtime_permission_created"], False)
        self.assertIs(non_claims["continuation_authorized"], False)
        self.assertIs(
            non_claims["successor_runtime_step_boundary_treated_as_successor_runtime_step"],
            False,
        )
        self.assertIs(
            non_claims["successor_runtime_step_boundary_treated_as_runtime_hosting"],
            False,
        )
        self.assertIs(
            non_claims["successor_runtime_step_boundary_treated_as_ongoing_runtime"],
            False,
        )
        self.assertIs(
            non_claims["successor_runtime_step_boundary_treated_as_continuation"],
            False,
        )
        self.assertIs(
            non_claims["bounded_runtime_result_or_refusal_authorized_successor"],
            False,
        )
        self.assertIs(non_claims["source_created"], False)
        self.assertIs(non_claims["authority_created"], False)
        self.assertIs(non_claims["currentness_created"], False)
        self.assertIs(non_claims["deployment_created"], False)
        self.assertIs(non_claims["public_release_created"], False)
        self.assertIs(non_claims["operation_permission_created"], False)
        self.assertIs(non_claims["follow_on_work_authorized"], False)
        self.assertIs(
            non_claims["hidden_repo_state_used_as_successor_runtime_step_boundary_content"],
            False,
        )
        self.assertIs(
            non_claims["hidden_repo_state_used_as_successor_runtime_step_boundary_authority"],
            False,
        )
        self.assertIs(
            non_claims[
                "repo_local_availability_treated_as_successor_runtime_step_boundary_authority"
            ],
            False,
        )
        self.assertIs(
            non_claims[
                "artifact_existence_treated_as_successor_runtime_step_boundary_authority"
            ],
            False,
        )
        self.assertIs(
            non_claims[
                "latest_file_posture_treated_as_successor_runtime_step_boundary_authority"
            ],
            False,
        )

    def assert_predecessor_and_tokens_preserved(
        self, result: Mapping[str, Any]
    ) -> None:
        statement = result["successor_runtime_step_boundary_statement"]
        non_claims = result["non_claims"]
        summary = resolver.build_post_minimal_runtime_successor_runtime_step_boundary_summary(
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
        self.assert_successor_runtime_step_boundary_membrane(result)
        self.assert_predecessor_and_tokens_preserved(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_minimal_runtime_successor_runtime_step_boundary",
            "resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path",
            "write_post_minimal_runtime_successor_runtime_step_boundary_result",
            "build_post_minimal_runtime_successor_runtime_step_boundary_summary",
            "build_declared_post_minimal_runtime_successor_runtime_step_boundary_request",
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
            "SUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name))

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_minimal_runtime_successor_runtime_step_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_post_minimal_runtime_"
                "successor_runtime_step_boundary"
            )
        )
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
            request
        )
        summary = resolver.build_post_minimal_runtime_successor_runtime_step_boundary_summary(
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
            "resolve_post_minimal_runtime_successor_runtime_step_boundary",
        )
        self.assertEqual(
            summary["request_id"],
            request["successor_runtime_step_boundary_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        for field in EXPECTED_TRUE_STATEMENT_FIELDS:
            self.assertIs(
                result["successor_runtime_step_boundary_statement"][field],
                True,
                field,
            )
        for field in EXPECTED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][field], False, field)

        self.assert_successor_runtime_step_boundary_membrane(result)
        self.assert_predecessor_and_tokens_preserved(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_public_block_codes(result)
        self.assert_no_raw_sentinels(result)
        self.assert_official_scope_preserved(result)

        all_scope_request = (
            resolver.build_declared_post_minimal_runtime_successor_runtime_step_boundary_request(
                successor_runtime_step_boundary_scope=list(
                    resolver.SUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE
                )
            )
        )
        all_scope_result = (
            resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
                all_scope_request
            )
        )
        self.assertEqual(all_scope_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(all_scope_result)

    def test_raw_hidden_hostile_content_is_contained(self) -> None:
        request = build_request()
        hostile_full_body = "HOSTILE_FULL_BODY_VALUE_DO_NOT_RETURN"
        for field in SELECTED_BASIS_FIELDS:
            request[field]["nested_hostile_payload"] = {
                "list": list(RAW_SENTINELS),
            }
            for key in HOSTILE_BODY_KEYS:
                request[field][key] = hostile_full_body + "::" + key
        original = copy.deepcopy(request)

        result = resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
            request
        )

        self.assertEqual(request, original)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_no_raw_sentinels(result, (hostile_full_body,))
        self.assert_official_scope_preserved(result)
        self.assert_successor_runtime_step_boundary_membrane(result)

    def test_representative_blocking_behavior(self) -> None:
        cases: tuple[
            tuple[str, Any],
            ...,
        ] = (
            (
                "explicit block intent",
                set_request_value(
                    "successor_runtime_step_boundary_intent",
                    "BLOCK_POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_BOUNDARY",
                ),
            ),
            ("missing request fields", {}),
            ("non-mapping request", ["not", "a", "mapping"]),
            (
                "unsupported intent",
                set_request_value(
                    "successor_runtime_step_boundary_intent",
                    "UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_INTENT",
                ),
            ),
            (
                "unsupported scope",
                set_request_value(
                    "successor_runtime_step_boundary_scope",
                    ["UNSUPPORTED_SUCCESSOR_RUNTIME_STEP_BOUNDARY_SCOPE_VALUE"],
                ),
            ),
            ("missing minimal-runtime basis", missing_minimal_runtime_basis),
            (
                "missing minimal-runtime terminal summary basis",
                set_request_value("selected_minimal_runtime_terminal_summary_basis", {}),
            ),
            (
                "minimal runtime not recorded",
                set_request_value("selected_minimal_runtime_result_outcome", "NOT_RECORDED"),
            ),
            (
                "minimal runtime failed checks present",
                set_request_value("selected_minimal_runtime_failed_check_count", 1),
            ),
            (
                "minimal runtime version not 0.1.0",
                set_request_value("selected_minimal_runtime_result_version", "0.2.0"),
            ),
            (
                "minimal runtime did not record bounded minimal-runtime step",
                set_request_value(
                    "selected_minimal_runtime_bounded_minimal_runtime_step_recorded",
                    False,
                ),
            ),
            (
                "minimal runtime did not record bounded runtime result/refusal",
                set_request_value(
                    "selected_minimal_runtime_bounded_runtime_result_or_refusal_recorded",
                    False,
                ),
            ),
            (
                "minimal runtime already created runtime hosting",
                set_request_value("selected_minimal_runtime_already_created_runtime_hosting", True),
            ),
            (
                "minimal runtime already created ongoing runtime",
                set_request_value("selected_minimal_runtime_already_created_ongoing_runtime", True),
            ),
            (
                "minimal runtime already created successor runtime step",
                set_request_value(
                    "selected_minimal_runtime_already_created_successor_runtime_step",
                    True,
                ),
            ),
            (
                "minimal runtime already authorized continuation beyond single step",
                set_request_value(
                    "selected_minimal_runtime_already_authorized_continuation_beyond_single_step",
                    True,
                ),
            ),
            (
                "minimal runtime treated as runtime hosting",
                set_request_value("selected_minimal_runtime_treated_as_runtime_hosting", True),
            ),
            (
                "minimal runtime treated as ongoing runtime",
                set_request_value("selected_minimal_runtime_treated_as_ongoing_runtime", True),
            ),
            (
                "minimal runtime treated as successor runtime step",
                set_request_value(
                    "selected_minimal_runtime_treated_as_successor_runtime_step",
                    True,
                ),
            ),
            (
                "minimal runtime treated as continuation",
                set_request_value("selected_minimal_runtime_treated_as_continuation", True),
            ),
            (
                "minimal runtime authorized future work",
                set_request_value("selected_minimal_runtime_authorized_future_work", True),
            ),
            (
                "bounded runtime result/refusal authorized successor",
                set_request_value(
                    "selected_bounded_runtime_result_or_refusal_authorized_successor",
                    True,
                ),
            ),
            (
                "missing runtime-boundary basis",
                clear_basis(
                    "selected_runtime_boundary_basis",
                    "selected_runtime_boundary_result_path",
                ),
            ),
            (
                "runtime-boundary not recorded",
                set_request_value("selected_runtime_boundary_result_outcome", "NOT_RECORDED"),
            ),
            (
                "runtime-boundary failed checks present",
                set_request_value("selected_runtime_boundary_failed_check_count", 1),
            ),
            (
                "runtime-boundary version not 0.1.0",
                set_request_value("selected_runtime_boundary_result_version", "0.2.0"),
            ),
            (
                "missing runtime-readiness basis",
                clear_basis(
                    "selected_runtime_readiness_basis",
                    "selected_runtime_readiness_result_path",
                ),
            ),
            (
                "runtime-readiness not recorded",
                set_request_value("selected_runtime_readiness_result_outcome", "NOT_RECORDED"),
            ),
            (
                "runtime-readiness failed checks present",
                set_request_value("selected_runtime_readiness_failed_check_count", 1),
            ),
            (
                "runtime-readiness version not 0.1.0",
                set_request_value("selected_runtime_readiness_result_version", "0.2.0"),
            ),
            (
                "missing portable verification final-completion basis",
                clear_basis(
                    "selected_portable_verification_final_completion_basis",
                    "selected_portable_verification_final_completion_result_path",
                ),
            ),
            (
                "portable verification final-completion not recorded",
                set_request_value(
                    "selected_portable_verification_final_completion_result_outcome",
                    "NOT_RECORDED",
                ),
            ),
            (
                "portable verification final-completion failed checks present",
                set_request_value(
                    "selected_portable_verification_final_completion_failed_check_count",
                    1,
                ),
            ),
            (
                "portable verification final-completion version not 0.1.0",
                set_request_value(
                    "selected_portable_verification_final_completion_result_version",
                    "0.2.0",
                ),
            ),
            (
                "missing post-portable currentness surface basis",
                clear_basis(
                    "selected_post_portable_verification_currentness_basis",
                    "selected_post_portable_currentness_surface_path",
                ),
            ),
            (
                "post-portable currentness surface did not separate checkability from continuation",
                set_request_value(
                    "selected_post_portable_currentness_surface_states_checkability_not_continuation",
                    False,
                ),
            ),
            (
                "post-portable currentness surface authorized next work",
                set_request_value(
                    "selected_post_portable_currentness_surface_authorized_next_work",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary created before review",
                set_request_value("successor_runtime_step_boundary_created_before_review", True),
            ),
            ("successor runtime step created", set_request_value("successor_runtime_step_created", True)),
            ("runtime hosting created", set_request_value("runtime_hosting_created", True)),
            ("ongoing runtime created", set_request_value("ongoing_runtime_created", True)),
            (
                "reusable runtime permission created",
                set_request_value("reusable_runtime_permission_created", True),
            ),
            ("continuation authorized", set_request_value("continuation_authorized", True)),
            (
                "successor-runtime-step boundary treated as successor runtime step",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_successor_runtime_step",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as runtime hosting",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_runtime_hosting",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as ongoing runtime",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_ongoing_runtime",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as continuation",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_continuation",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as source transfer",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_source_transfer",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as source receipt",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_source_receipt",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as reception authorization",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_reception_authorization",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as source",
                set_request_value("successor_runtime_step_boundary_treated_as_source", True),
            ),
            (
                "successor-runtime-step boundary treated as authority",
                set_request_value("successor_runtime_step_boundary_treated_as_authority", True),
            ),
            (
                "successor-runtime-step boundary treated as currentness",
                set_request_value("successor_runtime_step_boundary_treated_as_currentness", True),
            ),
            (
                "successor-runtime-step boundary treated as deployment",
                set_request_value("successor_runtime_step_boundary_treated_as_deployment", True),
            ),
            (
                "successor-runtime-step boundary treated as public release",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_public_release",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as operation permission",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_operation_permission",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as reusable permission",
                set_request_value(
                    "successor_runtime_step_boundary_treated_as_reusable_permission",
                    True,
                ),
            ),
            (
                "successor-runtime-step boundary treated as follow-on work",
                set_request_value("successor_runtime_step_boundary_treated_as_follow_on_work", True),
            ),
            ("source transfer occurred", set_request_value("source_transfer_occurred", True)),
            ("source receipt occurred", set_request_value("source_receipt_occurred", True)),
            (
                "reception authorization created",
                set_request_value("reception_authorization_created", True),
            ),
            ("source created", set_request_value("source_created", True)),
            ("authority created", set_request_value("authority_created", True)),
            ("currentness created", set_request_value("currentness_created", True)),
            ("deployment created", set_request_value("deployment_created", True)),
            ("public release created", set_request_value("public_release_created", True)),
            (
                "operation permission created",
                set_request_value("operation_permission_created", True),
            ),
            (
                "reusable permission created",
                set_request_value("reusable_permission_created", True),
            ),
            (
                "derivative reception authorized",
                set_request_value("derivative_reception_authorized", True),
            ),
            ("vessel relation authorized", set_request_value("vessel_relation_authorized", True)),
            ("adoption created", set_request_value("adoption_created", True)),
            (
                "receiving-context governance created",
                set_request_value("receiving_context_governance_created", True),
            ),
            ("publication flow created", set_request_value("publication_flow_created", True)),
            ("follow-on work authorized", set_request_value("follow_on_work_authorized", True)),
            (
                "artifact existence treated as successor-runtime-step-boundary authority",
                set_request_value(
                    "artifact_existence_treated_as_successor_runtime_step_boundary_authority",
                    True,
                ),
            ),
            (
                "artifact path treated as currentness",
                set_request_value("artifact_path_treated_as_currentness", True),
            ),
            (
                "latest file posture treated as successor-runtime-step-boundary authority",
                set_request_value(
                    "latest_file_posture_treated_as_successor_runtime_step_boundary_authority",
                    True,
                ),
            ),
            (
                "repo-local availability treated as successor-runtime-step-boundary authority",
                set_request_value(
                    "repo_local_availability_treated_as_successor_runtime_step_boundary_authority",
                    True,
                ),
            ),
            (
                "hidden repo state used as successor-runtime-step-boundary content",
                set_request_value(
                    "hidden_repo_state_used_as_successor_runtime_step_boundary_content",
                    True,
                ),
            ),
            (
                "hidden repo state used as successor-runtime-step-boundary authority",
                set_request_value(
                    "hidden_repo_state_used_as_successor_runtime_step_boundary_authority",
                    True,
                ),
            ),
            (
                "selected basis not reference-shaped",
                set_request_value("reference_shaped_input_posture", False),
            ),
            (
                "raw full prior artifact body returned",
                set_request_value("raw_full_prior_artifact_body_returned", True),
            ),
            (
                "predecessor failure evidence hidden",
                set_request_value("predecessor_failure_hidden", True),
            ),
            (
                "predecessor failure evidence repaired",
                set_request_value("predecessor_failure_repaired", True),
            ),
            (
                "predecessor failure evidence claimed passed",
                set_request_value("predecessor_failure_claimed_passed", True),
            ),
            (
                "consumed request reopened",
                set_request_value("consumed_request_reopened", True),
            ),
            (
                "authorization token reused",
                set_request_value("authorization_token_reused", True),
            ),
            (
                "required non-claim missing or flipped",
                set_non_claim("runtime_hosting_created", True),
            ),
        )

        for label, mutation in cases:
            with self.subTest(label=label):
                if isinstance(mutation, Mapping) or not callable(mutation):
                    request_or_value = mutation
                else:
                    request = build_request()
                    mutation(request)
                    request_or_value = request
                result = (
                    resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
                        request_or_value
                    )
                )
                self.assert_blocked_result(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request = build_request()
            request_path.write_text(
                json.dumps(request, indent=2, sort_keys=True),
                encoding="utf-8",
            )

            result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path(
                    request_path
                )
            )
            summary = (
                resolver.build_post_minimal_runtime_successor_runtime_step_boundary_summary(
                    result
                )
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_post_minimal_runtime_successor_runtime_step_boundary",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_result(malformed_result)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path(
                    array_path
                )
            )
            self.assert_blocked_result(array_result)

            missing_result = (
                resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary_from_path(
                    tmp_path / "missing.json"
                )
            )
            self.assert_blocked_result(missing_result)

            redirected_output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_minimal_runtime_"
                "successor_runtime_step_boundary"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", redirected_output_root):
                first_path = (
                    resolver.write_post_minimal_runtime_successor_runtime_step_boundary_result(
                        result
                    )
                )
                second_path = (
                    resolver.write_post_minimal_runtime_successor_runtime_step_boundary_result(
                        result
                    )
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(second_path.parent.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], result["outcome"])
            self.assertEqual(json.loads(second_path.read_text(encoding="utf-8"))["outcome"], result["outcome"])
            self.assertIn(
                "artifacts/integrity_host_v0_min_coexistence_post_minimal_runtime_"
                "successor_runtime_step_boundary",
                first_path.as_posix(),
            )

            prohibited_roots = (
                "actual_second_carrier_live_capture",
                "integrity_host_v0_min_coexistence_post_portable_verification_minimal_runtime",
                "integrity_host_v0_min_coexistence_post_portable_verification_runtime_boundary",
                "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness",
                "integrity_host_v0_min_coexistence_post_portable_verification_runtime_readiness_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_final_completion",
                "portable_verification_closure",
                "cross_carrier_evidence",
                "runtime_hosting",
                "ongoing_runtime",
                "source_transfer",
                "source_receipt",
                "deployment",
                "public_release",
            )
            first_path_text = first_path.as_posix()
            for prohibited in prohibited_roots:
                self.assertNotIn(prohibited, first_path_text)

    def test_non_mutation(self) -> None:
        request = build_request()
        basis_copies = {field: copy.deepcopy(request[field]) for field in SELECTED_BASIS_FIELDS}
        posture_copies = {field: copy.deepcopy(request[field]) for field in POSTURE_FIELDS}
        scope_copy = copy.deepcopy(request["successor_runtime_step_boundary_scope"])
        non_claims_copy = copy.deepcopy(request["declared_non_claims"])
        original_request = copy.deepcopy(request)

        result = resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
            request
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original_request)
        for field, value in basis_copies.items():
            self.assertEqual(request[field], value, field)
        for field, value in posture_copies.items():
            self.assertEqual(request[field], value, field)
        self.assertEqual(request["successor_runtime_step_boundary_scope"], scope_copy)
        self.assertEqual(request["declared_non_claims"], non_claims_copy)

    def test_predecessor_failure_preservation(self) -> None:
        request = build_request()
        result = resolver.resolve_post_minimal_runtime_successor_runtime_step_boundary(
            request
        )
        summary = resolver.build_post_minimal_runtime_successor_runtime_step_boundary_summary(
            result
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(
            result["successor_runtime_step_boundary_statement"][
                "predecessor_failure_evidence_preserved"
            ],
            True,
        )
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
