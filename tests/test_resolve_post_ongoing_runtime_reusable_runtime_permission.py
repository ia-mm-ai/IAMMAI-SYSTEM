"""Executable tests for the reusable-runtime-permission resolver.

This suite is bounded to post-ongoing-runtime reusable-runtime-permission
posture only. Reusable-runtime-permission-boundary and ongoing runtime are
upstream basis, and runtime-hosting-boundary v1 remains preserved predecessor
failure lineage. These tests do not create continuation, self-continuation,
self-recursive growth, daemon, loop, public API, participant-facing interface,
distributed network behavior, source transfer, source receipt, reception
authorization, source, authority, currentness, deployment, public release,
operation permission, broader reusable permission, adoption, receiving-context
governance, publication flow, or follow-on work.
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

import resolve_post_ongoing_runtime_reusable_runtime_permission as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_ongoing_runtime_"
    "reusable_runtime_permission"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_ongoing_runtime_reusable_runtime_permission_boundary",
    "post_runtime_hosting_ongoing_runtime",
    "post_runtime_hosting_ongoing_runtime_boundary",
    "post_successor_runtime_step_runtime_hosting",
    "post_successor_runtime_step_runtime_hosting_boundary_v2",
    "post_successor_runtime_step_runtime_hosting_boundary",
    "post_minimal_runtime_successor_runtime_step",
    "post_minimal_runtime_successor_runtime_step_boundary",
    "post_portable_verification_minimal_runtime",
    "post_portable_verification_runtime_boundary",
    "post_portable_verification_runtime_readiness",
    "post_portable_verification_runtime_readiness_boundary",
    "portable_source_body_verification_final_completion",
    "final-completion",
    "portable-verification",
    "continuation",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

OFFICIAL_SCOPE_VALUES = (
    "REUSABLE_RUNTIME_PERMISSION_SPEC_ONLY",
    "ONE_BOUNDED_REUSABLE_RUNTIME_PERMISSION_POSTURE_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_PRESERVED",
    "ONGOING_RUNTIME_BASIS_PRESERVED",
    "ONGOING_RUNTIME_PERSISTENCE_NOT_REPEATABILITY_WITHOUT_PERMISSION",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_DECLARED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_NOT_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_NOT_DAEMON",
    "REUSABLE_RUNTIME_PERMISSION_NOT_LOOP",
    "REUSABLE_RUNTIME_PERMISSION_NOT_PUBLIC_API",
    "REUSABLE_RUNTIME_PERMISSION_NOT_PARTICIPANT_FACING_INTERFACE",
    "REUSABLE_RUNTIME_PERMISSION_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "REUSABLE_RUNTIME_PERMISSION_QUESTION_UNDECLARED",
    "REUSABLE_RUNTIME_PERMISSION_INTENT_UNSUPPORTED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_DID_NOT_DECLARE_FUTURE_REUSABLE_RUNTIME_PERMISSION_REVIEW",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "ONGOING_RUNTIME_BASIS_MISSING",
    "ONGOING_RUNTIME_NOT_RECORDED",
    "ONGOING_RUNTIME_PERSISTENCE_TREATED_AS_REPEATABILITY_BEFORE_PERMISSION",
    "ONGOING_RUNTIME_PERSISTENCE_AUTHORIZED_REUSE_BEFORE_PERMISSION",
    "ONGOING_RUNTIME_ALREADY_AUTHORIZED_CONTINUATION",
    "ONGOING_RUNTIME_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "REUSABLE_RUNTIME_PERMISSION_CREATED_BEFORE_REVIEW",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_DAEMON",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_LOOP",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_API",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_TRANSFER",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE_RECEIPT",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RECEPTION_AUTHORIZATION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SOURCE",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_AUTHORITY",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CURRENTNESS",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DEPLOYMENT",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_RELEASE",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_OPERATION_PERMISSION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_FOLLOW_ON_WORK",
    "CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
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
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_REUSABLE_RUNTIME_PERMISSION_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE",
    "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_MALFORMED",
    "DECLARED_REUSABLE_RUNTIME_PERMISSION_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_ongoing_runtime_reusable_runtime_permission_metadata",
    "declared_reusable_runtime_permission_question",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_reusable_runtime_permission_boundary_terminal_summary_basis",
    "selected_ongoing_runtime_basis",
    "selected_ongoing_runtime_terminal_summary_basis",
    "selected_ongoing_runtime_boundary_basis",
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
    "reusable_runtime_permission_spec_only_posture",
    "one_bounded_reusable_runtime_permission_posture",
    "reusable_runtime_permission_boundary_basis_preserved_posture",
    "ongoing_runtime_basis_preserved_posture",
    "ongoing_runtime_persistence_not_repeatability_without_permission_posture",
    "bounded_runtime_reuse_envelope_declared_posture",
    "reusable_runtime_permission_not_continuation_posture",
    "reusable_runtime_permission_not_self_continuation_posture",
    "reusable_runtime_permission_not_daemon_posture",
    "reusable_runtime_permission_not_loop_posture",
    "reusable_runtime_permission_not_public_api_posture",
    "reusable_runtime_permission_not_participant_facing_interface_posture",
    "reusable_runtime_permission_not_distributed_network_behavior_posture",
    "continuation_not_authorized_posture",
    "self_continuation_not_authorized_posture",
    "self_recursive_growth_not_created_posture",
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
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_reusable_runtime_permission_authority_posture",
    "artifact_existence_not_reusable_runtime_permission_authority_posture",
    "latest_file_posture_not_reusable_runtime_permission_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "reusable_runtime_permission_scope",
    "reusable_runtime_permission_checks",
    "reusable_runtime_permission_statement",
    "reusable_runtime_permission_non_meaning",
    "bounded_runtime_reuse_envelope",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_ongoing_runtime_reusable_runtime_permission_summary",
)

STATEMENT_TRUE_FIELDS = (
    "reusable_runtime_permission_recorded",
    "bounded_reusable_runtime_permission_posture_recorded",
    "reusable_runtime_permission_boundary_basis_preserved",
    "ongoing_runtime_basis_preserved",
    "ongoing_runtime_persistence_not_repeatability_without_permission",
    "bounded_runtime_reuse_envelope_declared",
    "reusable_runtime_permission_not_continuation",
    "reusable_runtime_permission_not_self_continuation",
    "reusable_runtime_permission_not_daemon",
    "reusable_runtime_permission_not_loop",
    "reusable_runtime_permission_not_public_api",
    "reusable_runtime_permission_not_participant_facing_interface",
    "reusable_runtime_permission_not_distributed_network_behavior",
    "continuation_not_authorized",
    "self_continuation_not_authorized",
    "self_recursive_growth_not_created",
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
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_reusable_runtime_permission_authority",
    "repo_local_availability_not_reusable_runtime_permission_authority",
    "artifact_existence_not_reusable_runtime_permission_authority",
    "latest_file_posture_not_reusable_runtime_permission_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

ENVELOPE_FALSE_FIELDS = (
    "arbitrary_runtime_activity_authorized",
    "authorizes_continuation",
    "authorizes_self_continuation",
    "creates_self_recursive_growth",
    "creates_runtime_daemon",
    "creates_runtime_loop",
    "creates_public_api",
    "creates_participant_facing_interface",
    "creates_distributed_network_behavior",
    "creates_source_transfer",
    "creates_source_receipt",
    "creates_reception_authorization",
    "creates_source",
    "creates_authority",
    "creates_currentness",
    "creates_deployment",
    "creates_public_release",
    "creates_operation_permission",
    "creates_broader_reusable_permission",
    "creates_derivative_reception",
    "creates_vessel_relation",
    "creates_another_reception_request",
    "creates_adoption",
    "creates_receiving_context_governance",
    "creates_publication_flow",
    "authorizes_follow_on_work",
)

BASIS_SECTION_KEYS = (
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_reusable_runtime_permission_boundary_terminal_summary_basis",
    "selected_ongoing_runtime_basis",
    "selected_ongoing_runtime_terminal_summary_basis",
    "selected_ongoing_runtime_boundary_basis",
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

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_reusable_runtime_permission_body",
    "raw_bounded_runtime_reuse_envelope_body",
    "raw_runtime_reuse_body",
    "raw_continuation_body",
    "raw_self_continuation_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "reusable_runtime_permission_body",
    "bounded_runtime_reuse_envelope_body",
    "runtime_reuse_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

HOSTILE_SENTINELS = (
    "RAW_REUSABLE_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RUNTIME_REUSE_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_REUSE_BODY_MUST_NOT_RETURN",
    "RAW_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_SELF_CONTINUATION_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def clean_request() -> dict[str, Any]:
    return resolver.build_declared_post_ongoing_runtime_reusable_runtime_permission_request()


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return list(result.get("reusable_runtime_permission_checks", []))


def failed_checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [check for check in checks(result) if check.get("passed") is not True]


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["reusable_runtime_permission_statement"]


def mutate(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        request[field] = value

    return apply


def remove_field(field: str) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        request.pop(field, None)

    return apply


def mutate_declared_non_claim(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = value

    return apply


class ReusableRuntimePermissionResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "reusable_runtime_permission_statement",
            "reusable_runtime_permission_non_meaning",
            "non_claims",
            "bounded_runtime_reuse_envelope",
        ):
            section = result.get(section_name)
            if not isinstance(section, Mapping):
                continue
            for key, value in section.items():
                if isinstance(value, bool):
                    self.assertIs(type(value), bool, key)
                elif key in STATEMENT_TRUE_FIELDS or key in ENVELOPE_FALSE_FIELDS:
                    self.assertNotIsInstance(value, str, key)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("reusable_runtime_permission_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-reusable-runtime-permission-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE:
            self.assertIn(value, scope)

    def assert_no_forbidden_runtime_effects(self, result: Mapping[str, Any]) -> None:
        stmt = statement(result)
        for key in (
            "continuation_not_authorized",
            "self_continuation_not_authorized",
            "self_recursive_growth_not_created",
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
            "broader_reusable_permission_not_created",
            "follow_on_work_not_authorized",
            "predecessor_failure_evidence_preserved",
            "authorization_token_reuse_blocked",
            "consumed_request_token_remains_closed",
        ):
            self.assertIs(stmt.get(key), True, key)
        self.assert_non_claims_canonical_false(result)

    def assert_recorded_result(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        summary = result["post_ongoing_runtime_reusable_runtime_permission_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_post_ongoing_runtime_reusable_runtime_permission",
        )
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_generated_booleans_are_bool(result)

    def resolve_blocked(self, mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
        request = clean_request()
        mutator(request)
        return resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(request)

    def test_public_api_constants_scope_and_block_codes(self) -> None:
        for name in (
            "resolve_post_ongoing_runtime_reusable_runtime_permission",
            "resolve_post_ongoing_runtime_reusable_runtime_permission_from_path",
            "write_post_ongoing_runtime_reusable_runtime_permission_result",
            "build_post_ongoing_runtime_reusable_runtime_permission_summary",
            "build_declared_post_ongoing_runtime_reusable_runtime_permission_request",
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
            "SUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_ongoing_runtime_reusable_runtime_permission",
        )
        self.assertEqual(
            resolver.SUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        output_root = str(resolver.OUTPUT_ROOT).replace("\\", "/")
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = clean_request()
        result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(request)
        self.assert_recorded_result(result)
        metadata = result["post_ongoing_runtime_reusable_runtime_permission_metadata"]
        self.assertEqual(
            metadata["post_ongoing_runtime_reusable_runtime_permission_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            metadata["post_ongoing_runtime_reusable_runtime_permission_id"],
            request["reusable_runtime_permission_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        stmt = statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIn(field, stmt)
            self.assertIs(stmt[field], True, field)
        envelope = result["bounded_runtime_reuse_envelope"]
        self.assertIsInstance(envelope, Mapping)
        self.assertIs(envelope["declared"], True)
        self.assertEqual(envelope["envelope_type"], "bounded_runtime_reuse_envelope")
        self.assertIs(envelope["runtime_reuse_limited_to_declared_envelope"], True)
        for field in ENVELOPE_FALSE_FIELDS:
            self.assertIs(envelope[field], False, field)
        self.assertIs(envelope["anything_outside_envelope_requires_fresh_admission"], True)
        self.assert_official_scope_preserved(result)
        self.assert_no_hostile_sentinels(result)

    def test_critical_non_claim_canonicalization(self) -> None:
        required_named = {
            "continuation_authorized",
            "self_continuation_authorized",
            "self_recursive_growth_created",
            "runtime_daemon_created",
            "runtime_loop_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "reusable_runtime_permission_treated_as_continuation",
            "reusable_runtime_permission_treated_as_self_continuation",
            "reusable_runtime_permission_treated_as_self_recursive_growth",
            "reusable_runtime_permission_treated_as_runtime_daemon",
            "reusable_runtime_permission_treated_as_runtime_loop",
            "reusable_runtime_permission_treated_as_public_api",
            "reusable_runtime_permission_treated_as_participant_facing_interface",
            "reusable_runtime_permission_treated_as_distributed_network_behavior",
            "reusable_runtime_permission_treated_as_source",
            "reusable_runtime_permission_treated_as_authority",
            "reusable_runtime_permission_treated_as_currentness",
            "reusable_runtime_permission_boundary_treated_as_reusable_runtime_permission_without_review",
            "ongoing_runtime_treated_as_reusable_runtime_permission_without_review",
            "ongoing_runtime_persistence_treated_as_unbounded_repeatability",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(required_named.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = clean_request()
                request["declared_non_claims"][key] = True
                result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(
                    request
                )
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                self.assertGreaterEqual(len(failed_checks(result)), 1)
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)
                self.assertIs(result["non_claims"][key], False)
                self.assert_no_forbidden_runtime_effects(result)

    def test_representative_blocking_behavior(self) -> None:
        block_cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None] | None, Any],
            ...,
        ] = (
            ("explicit block intent", mutate("reusable_runtime_permission_intent", "BLOCK_POST_ONGOING_RUNTIME_REUSABLE_RUNTIME_PERMISSION"), None),
            ("missing request", None, None),
            ("non-mapping request", None, ["not", "mapping"]),
            ("unsupported intent", mutate("reusable_runtime_permission_intent", "UNSUPPORTED"), None),
            ("unsupported scope", mutate("reusable_runtime_permission_scope", list(resolver.SUPPORTED_SCOPE_VALUES) + ["UNSUPPORTED"]), None),
            ("missing boundary basis", mutate("selected_reusable_runtime_permission_boundary_basis", None), None),
            ("boundary not recorded", mutate("selected_reusable_runtime_permission_boundary_result_outcome", "NO"), None),
            ("boundary failed checks", mutate("selected_reusable_runtime_permission_boundary_failed_check_count", 1), None),
            ("boundary wrong version", mutate("selected_reusable_runtime_permission_boundary_result_version", "9.9.9"), None),
            ("boundary future review missing", mutate("selected_reusable_runtime_permission_boundary_declared_future_review", False), None),
            ("boundary created permission", mutate("selected_reusable_runtime_permission_boundary_already_created_reusable_runtime_permission", True), None),
            ("boundary authorized continuation", mutate("selected_reusable_runtime_permission_boundary_already_authorized_continuation", True), None),
            ("boundary authorized self continuation", mutate("selected_reusable_runtime_permission_boundary_already_authorized_self_continuation", True), None),
            ("boundary created daemon", mutate("selected_reusable_runtime_permission_boundary_already_created_runtime_daemon", True), None),
            ("boundary created loop", mutate("selected_reusable_runtime_permission_boundary_already_created_runtime_loop", True), None),
            ("boundary created public api", mutate("selected_reusable_runtime_permission_boundary_already_created_public_api", True), None),
            ("boundary created participant interface", mutate("selected_reusable_runtime_permission_boundary_already_created_participant_facing_interface", True), None),
            ("boundary created distributed behavior", mutate("selected_reusable_runtime_permission_boundary_already_created_distributed_network_behavior", True), None),
            ("boundary treated as permission", mutate("selected_reusable_runtime_permission_boundary_treated_as_reusable_runtime_permission", True), None),
            ("boundary treated as continuation", mutate("selected_reusable_runtime_permission_boundary_treated_as_continuation", True), None),
            ("boundary treated as self continuation", mutate("selected_reusable_runtime_permission_boundary_treated_as_self_continuation", True), None),
            ("boundary authorized future work", mutate("selected_reusable_runtime_permission_boundary_authorized_future_work", True), None),
            ("ongoing basis missing", mutate("selected_ongoing_runtime_basis", None), None),
            ("ongoing not recorded", mutate("selected_ongoing_runtime_result_outcome", "NO"), None),
            ("ongoing repeatability", mutate("selected_ongoing_runtime_persistence_treated_as_repeatability_before_permission", True), None),
            ("ongoing reuse", mutate("selected_ongoing_runtime_persistence_authorized_reuse_before_permission", True), None),
            ("ongoing continuation", mutate("selected_ongoing_runtime_already_authorized_continuation", True), None),
            ("ongoing self continuation", mutate("selected_ongoing_runtime_already_authorized_self_continuation", True), None),
            ("v1 repaired", mutate("selected_runtime_hosting_boundary_v1_failure_repaired", True), None),
            ("v1 hidden", mutate("selected_runtime_hosting_boundary_v1_failure_hidden", True), None),
            ("v1 claimed passed", mutate("selected_runtime_hosting_boundary_v1_failure_claimed_passed", True), None),
            ("permission created before review", mutate("reusable_runtime_permission_created_before_review", True), None),
            ("permission continuation", mutate("reusable_runtime_permission_treated_as_continuation", True), None),
            ("permission self continuation", mutate("reusable_runtime_permission_treated_as_self_continuation", True), None),
            ("permission self recursive growth", mutate("reusable_runtime_permission_treated_as_self_recursive_growth", True), None),
            ("permission daemon", mutate("reusable_runtime_permission_treated_as_runtime_daemon", True), None),
            ("permission loop", mutate("reusable_runtime_permission_treated_as_runtime_loop", True), None),
            ("permission public api", mutate("reusable_runtime_permission_treated_as_public_api", True), None),
            ("permission participant interface", mutate("reusable_runtime_permission_treated_as_participant_facing_interface", True), None),
            ("permission distributed behavior", mutate("reusable_runtime_permission_treated_as_distributed_network_behavior", True), None),
            ("permission source transfer", mutate("reusable_runtime_permission_treated_as_source_transfer", True), None),
            ("permission source receipt", mutate("reusable_runtime_permission_treated_as_source_receipt", True), None),
            ("permission reception authorization", mutate("reusable_runtime_permission_treated_as_reception_authorization", True), None),
            ("permission source", mutate("reusable_runtime_permission_treated_as_source", True), None),
            ("permission authority", mutate("reusable_runtime_permission_treated_as_authority", True), None),
            ("permission currentness", mutate("reusable_runtime_permission_treated_as_currentness", True), None),
            ("permission deployment", mutate("reusable_runtime_permission_treated_as_deployment", True), None),
            ("permission public release", mutate("reusable_runtime_permission_treated_as_public_release", True), None),
            ("permission operation", mutate("reusable_runtime_permission_treated_as_operation_permission", True), None),
            ("permission broader reusable", mutate("reusable_runtime_permission_treated_as_broader_reusable_permission", True), None),
            ("permission follow on", mutate("reusable_runtime_permission_treated_as_follow_on_work", True), None),
            ("continuation authorized", mutate("continuation_authorized", True), None),
            ("self continuation authorized", mutate("self_continuation_authorized", True), None),
            ("self recursive growth created", mutate("self_recursive_growth_created", True), None),
            ("daemon created", mutate("runtime_daemon_created", True), None),
            ("loop created", mutate("runtime_loop_created", True), None),
            ("public api created", mutate("public_api_created", True), None),
            ("participant interface created", mutate("participant_facing_interface_created", True), None),
            ("distributed behavior created", mutate("distributed_network_behavior_created", True), None),
            ("source transfer occurred", mutate("source_transfer_occurred", True), None),
            ("source receipt occurred", mutate("source_receipt_occurred", True), None),
            ("reception authorization created", mutate("reception_authorization_created", True), None),
            ("source created", mutate("source_created", True), None),
            ("authority created", mutate("authority_created", True), None),
            ("currentness created", mutate("currentness_created", True), None),
            ("deployment created", mutate("deployment_created", True), None),
            ("public release created", mutate("public_release_created", True), None),
            ("operation permission created", mutate("operation_permission_created", True), None),
            ("broader reusable created", mutate("broader_reusable_permission_created", True), None),
            ("derivative reception", mutate("derivative_reception_authorized", True), None),
            ("vessel relation", mutate("vessel_relation_authorized", True), None),
            ("adoption", mutate("adoption_created", True), None),
            ("receiving governance", mutate("receiving_context_governance_created", True), None),
            ("publication flow", mutate("publication_flow_created", True), None),
            ("follow on", mutate("follow_on_work_authorized", True), None),
            ("artifact authority", mutate("artifact_existence_treated_as_reusable_runtime_permission_authority", True), None),
            ("artifact path currentness", mutate("artifact_path_treated_as_currentness", True), None),
            ("latest file authority", mutate("latest_file_posture_treated_as_reusable_runtime_permission_authority", True), None),
            ("repo local authority", mutate("repo_local_availability_treated_as_reusable_runtime_permission_authority", True), None),
            ("hidden content", mutate("hidden_repo_state_used_as_reusable_runtime_permission_content", True), None),
            ("hidden authority", mutate("hidden_repo_state_used_as_reusable_runtime_permission_authority", True), None),
            ("basis not reference shaped", mutate("selected_basis_not_reference_shaped", True), None),
            ("raw body returned", mutate("raw_full_prior_artifact_body_returned", True), None),
            ("predecessor hidden repaired", mutate("predecessor_failure_evidence_hidden_or_repaired", True), None),
            ("consumed request reopened", mutate("consumed_request_reopened", True), None),
            ("authorization reused", mutate("authorization_token_reused", True), None),
            ("required non-claim missing", mutate_declared_non_claim("continuation_authorized", True), None),
        )
        for name, mutator, direct_request in block_cases:
            with self.subTest(name=name):
                if mutator is None:
                    result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(
                        direct_request
                    )
                else:
                    result = self.resolve_blocked(mutator)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                self.assert_public_block_codes(result)
                self.assert_no_forbidden_runtime_effects(result)

    def test_missing_incomplete_declared_non_claims_behavior(self) -> None:
        variants = (
            remove_field("declared_non_claims"),
            mutate("declared_non_claims", {}),
            lambda request: request["declared_non_claims"].pop("continuation_authorized"),
            mutate_declared_non_claim("continuation_authorized", "false"),
            mutate_declared_non_claim("continuation_authorized", None),
        )
        for index, variant in enumerate(variants):
            with self.subTest(variant=index):
                result = self.resolve_blocked(variant)
                self.assertIn(
                    result["outcome"],
                    (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                )
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(
            clean_request()
        )
        self.assert_recorded_result(result)
        self.assert_official_scope_preserved(result)
        custom_request = resolver.build_declared_post_ongoing_runtime_reusable_runtime_permission_request(
            reusable_runtime_permission_scope=list(
                resolver.SUPPORTED_REUSABLE_RUNTIME_PERMISSION_SCOPE
            )
        )
        custom_result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(
            custom_request
        )
        self.assert_recorded_result(custom_result)
        self.assert_official_scope_preserved(custom_result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        request = clean_request()
        original = copy.deepcopy(request)
        for index, section in enumerate(BASIS_SECTION_KEYS):
            basis = request[section]
            self.assertIsInstance(basis, dict)
            for key in HOSTILE_KEYS:
                basis[key] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
        before_resolve = copy.deepcopy(request)
        result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_forbidden_runtime_effects(result)
        self.assertEqual(request, before_resolve)
        for section in BASIS_SECTION_KEYS:
            for key in HOSTILE_KEYS:
                self.assertIn(key, request[section])
        clean_original = clean_request()
        for section in BASIS_SECTION_KEYS:
            self.assertEqual(original[section], clean_original[section])

    def test_path_and_write_behavior(self) -> None:
        request = clean_request()
        with tempfile.TemporaryDirectory() as tempdir:
            temp_path = Path(tempdir)
            request_path = temp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission_from_path(
                request_path
            )
            self.assert_recorded_result(result)
            malformed_path = temp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            array_path = temp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            missing = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission_from_path(
                temp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], resolver.OUTCOME_BLOCKED)
            for blocked in (malformed, array_result, missing):
                self.assert_public_block_codes(blocked)
                self.assert_non_claims_canonical_false(blocked)

            output_root = temp_path / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_post_ongoing_runtime_reusable_runtime_permission_result(
                    result
                )
                second = resolver.write_post_ongoing_runtime_reusable_runtime_permission_result(
                    result
                )
            self.assertTrue(first.parent.exists())
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            path_text = str(first).replace("\\", "/")
            self.assertIn("post_ongoing_runtime_reusable_runtime_permission", path_text)
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, path_text)

    def test_non_mutation(self) -> None:
        request = clean_request()
        before = copy.deepcopy(request)
        result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(request)
        self.assert_recorded_result(result)
        self.assertEqual(request, before)
        for section in BASIS_SECTION_KEYS:
            self.assertEqual(request[section], before[section])
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])
        self.assertEqual(
            request["requested_bounded_runtime_reuse_envelope"],
            before["requested_bounded_runtime_reuse_envelope"],
        )
        self.assertEqual(
            request["reusable_runtime_permission_scope"],
            before["reusable_runtime_permission_scope"],
        )
        for key, value in before.items():
            if key.endswith("_posture"):
                self.assertEqual(request[key], value)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_post_ongoing_runtime_reusable_runtime_permission(
            clean_request()
        )
        self.assert_recorded_result(result)
        lineage = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]
        self.assertTrue(lineage["declared"])
        self.assertIn(
            "resolve_post_successor_runtime_step_runtime_hosting_boundary.py",
            json.dumps(lineage),
        )
        stmt = statement(result)
        self.assertIs(stmt["predecessor_failure_evidence_preserved"], True)
        self.assertIs(stmt["consumed_request_token_remains_closed"], True)
        self.assertIs(stmt["authorization_token_reuse_blocked"], True)
        non_claims = result["non_claims"]
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
        summary = result["post_ongoing_runtime_reusable_runtime_permission_summary"]
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
