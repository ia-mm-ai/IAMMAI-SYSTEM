"""Executable tests for the post-runtime-hosting ongoing-runtime resolver.

This suite is bounded to ongoing-runtime posture only. Ongoing-runtime-boundary
is upstream basis, runtime hosting is upstream basis, runtime-hosting-boundary
v2 is upstream boundary basis, and runtime-hosting-boundary v1 remains
preserved predecessor failure lineage. These tests do not create reusable
runtime permission, continuation, self-continuation, daemon, loop, public API,
participant-facing interface, distributed network behavior, source transfer,
source receipt, reception authorization, source, authority, currentness,
deployment, public release, operation permission, reusable permission,
adoption, receiving-context governance, publication flow, or follow-on work.
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

import resolve_post_runtime_hosting_ongoing_runtime as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_runtime_hosting_ongoing_runtime_boundary",
    "post_successor_runtime_step_runtime_hosting",
    "post_successor_runtime_step_runtime_hosting_boundary_v2",
    "post_successor_runtime_step_runtime_hosting_boundary",
    "post_minimal_runtime_successor_runtime_step",
    "post_portable_verification_minimal_runtime",
    "post_portable_verification_runtime_boundary",
    "post_portable_verification_runtime_readiness",
    "post_portable_verification_runtime_readiness_boundary",
    "portable_source_body_verification_final_completion",
    "reusable-runtime-permission",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

OFFICIAL_SCOPE_VALUES = (
    "ONGOING_RUNTIME_SPEC_ONLY",
    "ONE_BOUNDED_ONGOING_RUNTIME_POSTURE_RECORDED",
    "ONGOING_RUNTIME_BOUNDARY_BASIS_PRESERVED",
    "RUNTIME_HOSTING_BASIS_PRESERVED",
    "RUNTIME_HOSTING_HOST_RELATION_NOT_CONTINUOUS_RUNTIME",
    "ONGOING_RUNTIME_NOT_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_NOT_CONTINUATION",
    "ONGOING_RUNTIME_NOT_SELF_CONTINUATION",
    "ONGOING_RUNTIME_NOT_DAEMON",
    "ONGOING_RUNTIME_NOT_LOOP",
    "ONGOING_RUNTIME_NOT_PUBLIC_API",
    "ONGOING_RUNTIME_NOT_PARTICIPANT_FACING_INTERFACE",
    "ONGOING_RUNTIME_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_ONGOING_RUNTIME_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_ONGOING_RUNTIME_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_ONGOING_RUNTIME_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "ONGOING_RUNTIME_QUESTION_UNDECLARED",
    "ONGOING_RUNTIME_INTENT_UNSUPPORTED",
    "ONGOING_RUNTIME_BOUNDARY_BASIS_MISSING",
    "ONGOING_RUNTIME_BOUNDARY_NOT_RECORDED",
    "ONGOING_RUNTIME_BOUNDARY_FAILED_CHECKS_PRESENT",
    "ONGOING_RUNTIME_BOUNDARY_VERSION_NOT_0_1_0",
    "ONGOING_RUNTIME_BOUNDARY_DID_NOT_DECLARE_FUTURE_ONGOING_RUNTIME_REVIEW",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_AUTHORIZED_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "ONGOING_RUNTIME_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_HOST_RELATION_RAN_CONTINUOUSLY_WITHOUT_ONGOING_RUNTIME_ADMISSION",
    "RUNTIME_HOSTING_HOST_RELATION_CREATED_ACTIVE_EXECUTION",
    "RUNTIME_HOSTING_HOST_RELATION_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "ONGOING_RUNTIME_CREATED_BEFORE_REVIEW",
    "ONGOING_RUNTIME_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_TREATED_AS_CONTINUATION",
    "ONGOING_RUNTIME_TREATED_AS_SELF_CONTINUATION",
    "ONGOING_RUNTIME_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "ONGOING_RUNTIME_TREATED_AS_RUNTIME_DAEMON",
    "ONGOING_RUNTIME_TREATED_AS_RUNTIME_LOOP",
    "ONGOING_RUNTIME_TREATED_AS_PUBLIC_API",
    "ONGOING_RUNTIME_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "ONGOING_RUNTIME_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "ONGOING_RUNTIME_TREATED_AS_SOURCE_TRANSFER",
    "ONGOING_RUNTIME_TREATED_AS_SOURCE_RECEIPT",
    "ONGOING_RUNTIME_TREATED_AS_RECEPTION_AUTHORIZATION",
    "ONGOING_RUNTIME_TREATED_AS_SOURCE",
    "ONGOING_RUNTIME_TREATED_AS_AUTHORITY",
    "ONGOING_RUNTIME_TREATED_AS_CURRENTNESS",
    "ONGOING_RUNTIME_TREATED_AS_DEPLOYMENT",
    "ONGOING_RUNTIME_TREATED_AS_PUBLIC_RELEASE",
    "ONGOING_RUNTIME_TREATED_AS_OPERATION_PERMISSION",
    "ONGOING_RUNTIME_TREATED_AS_REUSABLE_PERMISSION",
    "ONGOING_RUNTIME_TREATED_AS_FOLLOW_ON_WORK",
    "REUSABLE_RUNTIME_PERMISSION_CREATED",
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
    "REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_ONGOING_RUNTIME_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_ONGOING_RUNTIME_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ONGOING_RUNTIME_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_ONGOING_RUNTIME_SCOPE",
    "DECLARED_ONGOING_RUNTIME_REQUEST_MALFORMED",
    "DECLARED_ONGOING_RUNTIME_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_runtime_hosting_ongoing_runtime_metadata",
    "declared_ongoing_runtime_question",
    "selected_ongoing_runtime_boundary_basis",
    "selected_ongoing_runtime_boundary_terminal_summary_basis",
    "selected_runtime_hosting_basis",
    "selected_runtime_hosting_terminal_summary_basis",
    "selected_runtime_hosting_boundary_v2_basis",
    "selected_runtime_hosting_boundary_v1_failure_lineage_basis",
    "selected_successor_runtime_step_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "ongoing_runtime_spec_only_posture",
    "one_bounded_ongoing_runtime_posture",
    "ongoing_runtime_boundary_basis_preserved_posture",
    "runtime_hosting_basis_preserved_posture",
    "runtime_hosting_host_relation_not_continuous_runtime_posture",
    "ongoing_runtime_not_reusable_runtime_permission_posture",
    "ongoing_runtime_not_continuation_posture",
    "ongoing_runtime_not_self_continuation_posture",
    "ongoing_runtime_not_daemon_posture",
    "ongoing_runtime_not_loop_posture",
    "ongoing_runtime_not_public_api_posture",
    "ongoing_runtime_not_participant_facing_interface_posture",
    "ongoing_runtime_not_distributed_network_behavior_posture",
    "reusable_runtime_permission_not_created_posture",
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
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_ongoing_runtime_authority_posture",
    "artifact_existence_not_ongoing_runtime_authority_posture",
    "latest_file_posture_not_ongoing_runtime_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "ongoing_runtime_scope",
    "ongoing_runtime_checks",
    "ongoing_runtime_statement",
    "ongoing_runtime_non_meaning",
    "ongoing_runtime_persistence_posture",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_runtime_hosting_ongoing_runtime_summary",
)

SELECTED_BASIS_FIELDS = (
    "selected_ongoing_runtime_boundary_basis",
    "selected_ongoing_runtime_boundary_terminal_summary_basis",
    "selected_runtime_hosting_basis",
    "selected_runtime_hosting_terminal_summary_basis",
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

POSTURE_FIELDS = (
    "ongoing_runtime_spec_only_posture",
    "one_bounded_ongoing_runtime_posture",
    "ongoing_runtime_boundary_basis_preserved_posture",
    "runtime_hosting_basis_preserved_posture",
    "runtime_hosting_host_relation_not_continuous_runtime_posture",
    "ongoing_runtime_not_reusable_runtime_permission_posture",
    "ongoing_runtime_not_continuation_posture",
    "ongoing_runtime_not_self_continuation_posture",
    "ongoing_runtime_not_daemon_posture",
    "ongoing_runtime_not_loop_posture",
    "ongoing_runtime_not_public_api_posture",
    "ongoing_runtime_not_participant_facing_interface_posture",
    "ongoing_runtime_not_distributed_network_behavior_posture",
    "reusable_runtime_permission_not_created_posture",
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
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_ongoing_runtime_authority_posture",
    "artifact_existence_not_ongoing_runtime_authority_posture",
    "latest_file_posture_not_ongoing_runtime_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

STATEMENT_TRUE_FIELDS = (
    "ongoing_runtime_recorded",
    "bounded_ongoing_runtime_posture_recorded",
    "ongoing_runtime_boundary_basis_preserved",
    "runtime_hosting_basis_preserved",
    "runtime_hosting_host_relation_not_continuous_runtime",
    "ongoing_runtime_not_reusable_runtime_permission",
    "ongoing_runtime_not_continuation",
    "ongoing_runtime_not_self_continuation",
    "ongoing_runtime_not_daemon",
    "ongoing_runtime_not_loop",
    "ongoing_runtime_not_public_api",
    "ongoing_runtime_not_participant_facing_interface",
    "ongoing_runtime_not_distributed_network_behavior",
    "reusable_runtime_permission_not_created",
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
    "reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_ongoing_runtime_authority",
    "repo_local_availability_not_ongoing_runtime_authority",
    "artifact_existence_not_ongoing_runtime_authority",
    "latest_file_posture_not_ongoing_runtime_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

HOSTILE_SENTINELS = (
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
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

RAW_BODY_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_ongoing_runtime_body",
    "raw_reusable_runtime_permission_body",
    "raw_continuation_body",
    "raw_self_continuation_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "ongoing_runtime_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_post_runtime_hosting_ongoing_runtime_request(
        **overrides
    )


def resolve_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return resolver.resolve_post_runtime_hosting_ongoing_runtime(request)


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return list(result.get("ongoing_runtime_checks", []))


def failed_checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [check for check in checks(result) if check.get("passed") is not True]


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result.get("ongoing_runtime_statement", {})


def non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result.get("non_claims", {})


def summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result.get("post_runtime_hosting_ongoing_runtime_summary", {})


def mutate_request(
    request: dict[str, Any], updates: Mapping[str, Any] | Callable[[dict[str, Any]], None]
) -> dict[str, Any]:
    mutated = copy.deepcopy(request)
    if callable(updates):
        updates(mutated)
    else:
        mutated.update(updates)
    return mutated


class PostRuntimeHostingOngoingRuntimeTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_bools_are_bool(self, result: Mapping[str, Any]) -> None:
        for key, value in statement(result).items():
            self.assertIsInstance(value, bool, key)
        for key, value in non_claims(result).items():
            self.assertIsInstance(value, bool, key)
        for check in checks(result):
            self.assertIsInstance(check.get("passed"), bool, check.get("check_name"))
        block = result.get("block")
        if isinstance(block, Mapping) and "blocked" in block:
            self.assertIsInstance(block["blocked"], bool)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
            self.assertIsInstance(emitted[key], bool, key)

    def assert_no_hostile_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True, ensure_ascii=False)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("ongoing_runtime_scope", [])
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-ongoing-runtime-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_ONGOING_RUNTIME_SCOPE:
            self.assertIn(value, scope)
            self.assertNotEqual(value, "[bounded-ongoing-runtime-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")

    def assert_protective_posture(self, result: Mapping[str, Any]) -> None:
        stmt = statement(result)
        for key in (
            "reusable_runtime_permission_not_created",
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
            "follow_on_work_not_authorized",
            "predecessor_failure_evidence_preserved",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(stmt.get(key), True, key)
        self.assert_non_claims_canonical_false(result)
        self.assertIs(non_claims(result)["predecessor_failure_repaired"], False)
        self.assertIs(non_claims(result)["predecessor_failure_hidden"], False)
        self.assertIs(non_claims(result)["predecessor_failure_claimed_passed"], False)
        self.assertIs(non_claims(result)["consumed_request_reopened"], False)
        self.assertIs(non_claims(result)["authorization_token_reused"], False)

    def assert_blocked_public_result(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsInstance(result.get("block"), Mapping)
        self.assertIn(result["block"].get("block_code"), resolver.BLOCK_CODES)
        self.assertGreaterEqual(len(failed_checks(result)), 1)
        self.assert_public_codes(result)
        self.assert_generated_bools_are_bool(result)
        self.assert_protective_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_runtime_hosting_ongoing_runtime",
            "resolve_post_runtime_hosting_ongoing_runtime_from_path",
            "write_post_runtime_hosting_ongoing_runtime_result",
            "build_post_runtime_hosting_ongoing_runtime_summary",
            "build_declared_post_runtime_hosting_ongoing_runtime_request",
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
            "SUPPORTED_ONGOING_RUNTIME_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_runtime_hosting_ongoing_runtime",
        )
        self.assertEqual(
            resolver.SUPPORTED_ONGOING_RUNTIME_SCOPE, resolver.SUPPORTED_SCOPE_VALUES
        )
        output_root = str(resolver.OUTPUT_ROOT)
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolve_request(request)
        built_summary = resolver.build_post_runtime_hosting_ongoing_runtime_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(built_summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertEqual(built_summary["result_version"], "0.1.0")
        self.assertEqual(
            built_summary["resolver_module"],
            "resolve_post_runtime_hosting_ongoing_runtime",
        )
        self.assertGreater(built_summary["passed_check_count"], 0)
        self.assertEqual(
            built_summary["request_id"], request["ongoing_runtime_request_id"]
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        for key in STATEMENT_TRUE_FIELDS:
            self.assertIs(statement(result).get(key), True, key)
        self.assert_non_claims_canonical_false(result)
        self.assert_public_codes(result)
        self.assert_generated_bools_are_bool(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_hostile_sentinels(result)

        persistence = result["ongoing_runtime_persistence_posture"]
        self.assertIs(persistence.get("bounded_ongoing_runtime_persistence_posture"), True)
        for key in (
            "executes_arbitrary_work",
            "creates_reusable_runtime_permission",
            "authorizes_continuation",
            "authorizes_self_continuation",
            "creates_runtime_daemon",
            "creates_runtime_loop",
            "creates_public_api",
            "creates_participant_facing_interface",
            "creates_distributed_network_behavior",
            "mutates_prior_artifacts",
            "authorizes_follow_on_work",
        ):
            self.assertIs(persistence.get(key), False, key)

    def test_critical_canonicalization_for_required_false_non_claims(self) -> None:
        clean = build_request()
        explicit_names = {
            "reusable_runtime_permission_created",
            "continuation_authorized",
            "self_continuation_authorized",
            "self_recursive_growth_created",
            "runtime_daemon_created",
            "runtime_loop_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "ongoing_runtime_treated_as_reusable_runtime_permission",
            "ongoing_runtime_treated_as_continuation",
            "ongoing_runtime_treated_as_self_continuation",
            "ongoing_runtime_treated_as_self_recursive_growth",
            "ongoing_runtime_treated_as_runtime_daemon",
            "ongoing_runtime_treated_as_runtime_loop",
            "ongoing_runtime_treated_as_public_api",
            "ongoing_runtime_treated_as_participant_facing_interface",
            "ongoing_runtime_treated_as_distributed_network_behavior",
            "ongoing_runtime_treated_as_source",
            "ongoing_runtime_treated_as_authority",
            "ongoing_runtime_treated_as_currentness",
            "ongoing_runtime_boundary_treated_as_ongoing_runtime_without_review",
            "runtime_hosting_treated_as_ongoing_runtime_without_review",
            "runtime_hosting_host_relation_ran_continuously_without_ongoing_runtime_admission",
            "runtime_hosting_host_relation_created_active_execution",
            "runtime_hosting_host_relation_authorized_follow_on_work",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(explicit_names.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(required_false_non_claim=key):
                request = copy.deepcopy(clean)
                request["declared_non_claims"][key] = True
                result = resolve_request(request)
                self.assert_blocked_public_result(result)
                self.assertIs(non_claims(result)[key], False)
                self.assertFalse(any(non_claims(result).values()))

    def test_representative_blocking_behavior(self) -> None:
        first_non_claim = resolver.REQUIRED_FALSE_NON_CLAIMS[0]

        def remove_required_non_claim(request: dict[str, Any]) -> None:
            request["declared_non_claims"].pop(first_non_claim)

        cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", {"ongoing_runtime_intent": "BLOCK_POST_RUNTIME_HOSTING_ONGOING_RUNTIME"}),
            ("missing ongoing-runtime question", {"ongoing_runtime_question": None}),
            ("unsupported intent", {"ongoing_runtime_intent": "UNSUPPORTED"}),
            ("unsupported scope", {"ongoing_runtime_scope": ["UNSUPPORTED_SCOPE"]}),
            ("missing ongoing-runtime-boundary basis", {"selected_ongoing_runtime_boundary_basis": None}),
            ("missing ongoing-runtime-boundary terminal summary basis", {"selected_ongoing_runtime_boundary_terminal_summary_basis": None}),
            ("ongoing-runtime-boundary not recorded", {"selected_ongoing_runtime_boundary_result_outcome": "NOT_RECORDED"}),
            ("ongoing-runtime-boundary failed checks present", {"selected_ongoing_runtime_boundary_failed_check_count": 1}),
            ("ongoing-runtime-boundary version not 0.1.0", {"selected_ongoing_runtime_boundary_result_version": "0.2.0"}),
            ("ongoing-runtime-boundary did not declare future ongoing-runtime review", {"selected_ongoing_runtime_boundary_declared_future_ongoing_runtime_review": False}),
            ("ongoing-runtime-boundary already created ongoing runtime", {"selected_ongoing_runtime_boundary_already_created_ongoing_runtime": True}),
            ("ongoing-runtime-boundary already created reusable runtime permission", {"selected_ongoing_runtime_boundary_already_created_reusable_runtime_permission": True}),
            ("ongoing-runtime-boundary already authorized continuation", {"selected_ongoing_runtime_boundary_already_authorized_continuation": True}),
            ("ongoing-runtime-boundary already authorized self-continuation", {"selected_ongoing_runtime_boundary_already_authorized_self_continuation": True}),
            ("ongoing-runtime-boundary already created daemon", {"selected_ongoing_runtime_boundary_already_created_runtime_daemon": True}),
            ("ongoing-runtime-boundary already created loop", {"selected_ongoing_runtime_boundary_already_created_runtime_loop": True}),
            ("ongoing-runtime-boundary already created public API", {"selected_ongoing_runtime_boundary_already_created_public_api": True}),
            ("ongoing-runtime-boundary already created participant-facing interface", {"selected_ongoing_runtime_boundary_already_created_participant_facing_interface": True}),
            ("ongoing-runtime-boundary already created distributed network behavior", {"selected_ongoing_runtime_boundary_already_created_distributed_network_behavior": True}),
            ("ongoing-runtime-boundary treated boundary as ongoing runtime", {"selected_ongoing_runtime_boundary_treated_boundary_as_ongoing_runtime": True}),
            ("ongoing-runtime-boundary treated boundary as reusable runtime permission", {"selected_ongoing_runtime_boundary_treated_boundary_as_reusable_runtime_permission": True}),
            ("ongoing-runtime-boundary treated boundary as continuation", {"selected_ongoing_runtime_boundary_treated_boundary_as_continuation": True}),
            ("ongoing-runtime-boundary treated boundary as self-continuation", {"selected_ongoing_runtime_boundary_treated_boundary_as_self_continuation": True}),
            ("ongoing-runtime-boundary authorized future work", {"selected_ongoing_runtime_boundary_authorized_future_work": True}),
            ("runtime-hosting basis missing", {"selected_runtime_hosting_basis": None}),
            ("runtime-hosting terminal summary missing", {"selected_runtime_hosting_terminal_summary_basis": None}),
            ("runtime-hosting not recorded", {"selected_runtime_hosting_result_outcome": "NOT_RECORDED"}),
            ("runtime-hosting-boundary v2 basis missing", {"selected_runtime_hosting_boundary_v2_basis": None}),
            ("runtime-hosting-boundary v2 not recorded", {"selected_runtime_hosting_boundary_v2_result_outcome": "NOT_RECORDED"}),
            ("runtime-hosting-boundary v2 version wrong", {"selected_runtime_hosting_boundary_v2_result_version": "0.1.0"}),
            ("runtime-hosting-boundary v2 failed checks", {"selected_runtime_hosting_boundary_v2_failed_check_count": 1}),
            ("runtime-hosting host relation ran continuously without ongoing-runtime admission", {"selected_runtime_hosting_host_relation_ran_continuously": True}),
            ("runtime-hosting host relation created active execution", {"selected_runtime_hosting_host_relation_created_active_execution": True}),
            ("runtime-hosting host relation authorized follow-on work", {"selected_runtime_hosting_host_relation_authorized_follow_on_work": True}),
            ("runtime-hosting-boundary v1 failure repaired", {"selected_runtime_hosting_boundary_v1_failure_repaired": True}),
            ("runtime-hosting-boundary v1 failure hidden", {"selected_runtime_hosting_boundary_v1_failure_hidden": True}),
            ("runtime-hosting-boundary v1 failure claimed passed", {"selected_runtime_hosting_boundary_v1_failure_claimed_passed": True}),
            ("successor-runtime-step basis missing", {"selected_successor_runtime_step_basis": None}),
            ("minimal-runtime basis missing", {"selected_minimal_runtime_basis": None}),
            ("runtime-boundary basis missing", {"selected_runtime_boundary_basis": None}),
            ("runtime-readiness basis missing", {"selected_runtime_readiness_basis": None}),
            ("final-completion basis missing", {"selected_portable_verification_final_completion_basis": None}),
            ("post-portable currentness basis missing", {"selected_post_portable_verification_currentness_basis": None}),
            ("ongoing runtime created before review", {"ongoing_runtime_created_before_review": True}),
            ("ongoing runtime treated as reusable runtime permission", {"ongoing_runtime_treated_as_reusable_runtime_permission": True}),
            ("ongoing runtime treated as continuation", {"ongoing_runtime_treated_as_continuation": True}),
            ("ongoing runtime treated as self-continuation", {"ongoing_runtime_treated_as_self_continuation": True}),
            ("ongoing runtime treated as self-recursive growth", {"ongoing_runtime_treated_as_self_recursive_growth": True}),
            ("ongoing runtime treated as daemon", {"ongoing_runtime_treated_as_runtime_daemon": True}),
            ("ongoing runtime treated as loop", {"ongoing_runtime_treated_as_runtime_loop": True}),
            ("ongoing runtime treated as public API", {"ongoing_runtime_treated_as_public_api": True}),
            ("ongoing runtime treated as participant-facing interface", {"ongoing_runtime_treated_as_participant_facing_interface": True}),
            ("ongoing runtime treated as distributed network behavior", {"ongoing_runtime_treated_as_distributed_network_behavior": True}),
            ("ongoing runtime treated as source transfer", {"ongoing_runtime_treated_as_source_transfer": True}),
            ("ongoing runtime treated as source receipt", {"ongoing_runtime_treated_as_source_receipt": True}),
            ("ongoing runtime treated as reception authorization", {"ongoing_runtime_treated_as_reception_authorization": True}),
            ("ongoing runtime treated as source", {"ongoing_runtime_treated_as_source": True}),
            ("ongoing runtime treated as authority", {"ongoing_runtime_treated_as_authority": True}),
            ("ongoing runtime treated as currentness", {"ongoing_runtime_treated_as_currentness": True}),
            ("ongoing runtime treated as deployment", {"ongoing_runtime_treated_as_deployment": True}),
            ("ongoing runtime treated as public release", {"ongoing_runtime_treated_as_public_release": True}),
            ("ongoing runtime treated as operation permission", {"ongoing_runtime_treated_as_operation_permission": True}),
            ("ongoing runtime treated as reusable permission", {"ongoing_runtime_treated_as_reusable_permission": True}),
            ("ongoing runtime treated as follow-on work", {"ongoing_runtime_treated_as_follow_on_work": True}),
            ("reusable runtime permission created", {"reusable_runtime_permission_created": True}),
            ("continuation authorized", {"continuation_authorized": True}),
            ("self-continuation authorized", {"self_continuation_authorized": True}),
            ("self-recursive growth created", {"self_recursive_growth_created": True}),
            ("runtime daemon created", {"runtime_daemon_created": True}),
            ("runtime loop created", {"runtime_loop_created": True}),
            ("public API created", {"public_api_created": True}),
            ("participant-facing interface created", {"participant_facing_interface_created": True}),
            ("distributed network behavior created", {"distributed_network_behavior_created": True}),
            ("source transfer occurred", {"source_transfer_occurred": True}),
            ("source receipt occurred", {"source_receipt_occurred": True}),
            ("reception authorization created", {"reception_authorization_created": True}),
            ("source created", {"source_created": True}),
            ("authority created", {"authority_created": True}),
            ("currentness created", {"currentness_created": True}),
            ("deployment created", {"deployment_created": True}),
            ("public release created", {"public_release_created": True}),
            ("operation permission created", {"operation_permission_created": True}),
            ("reusable permission created", {"reusable_permission_created": True}),
            ("derivative reception authorized", {"derivative_reception_authorized": True}),
            ("vessel relation authorized", {"vessel_relation_authorized": True}),
            ("adoption created", {"adoption_created": True}),
            ("receiving-context governance created", {"receiving_context_governance_created": True}),
            ("publication flow created", {"publication_flow_created": True}),
            ("follow-on work authorized", {"follow_on_work_authorized": True}),
            ("artifact existence treated as ongoing-runtime authority", {"artifact_existence_treated_as_ongoing_runtime_authority": True}),
            ("artifact path treated as currentness", {"artifact_path_treated_as_currentness": True}),
            ("latest file posture treated as ongoing-runtime authority", {"latest_file_posture_treated_as_ongoing_runtime_authority": True}),
            ("repo-local availability treated as ongoing-runtime authority", {"repo_local_availability_treated_as_ongoing_runtime_authority": True}),
            ("hidden repo state used as ongoing-runtime content", {"hidden_repo_state_used_as_ongoing_runtime_content": True}),
            ("hidden repo state used as ongoing-runtime authority", {"hidden_repo_state_used_as_ongoing_runtime_authority": True}),
            ("selected basis not reference-shaped", {"selected_basis_not_reference_shaped": True}),
            ("raw full prior artifact body returned", {"raw_full_prior_artifact_body_returned": True}),
            ("predecessor failure evidence hidden/repaired/claimed passed", {"predecessor_failure_evidence_hidden_or_repaired": True}),
            ("consumed request reopened", {"consumed_request_reopened": True}),
            ("authorization token reused", {"authorization_token_reused": True}),
            ("required non-claim missing or flipped", remove_required_non_claim),
        )

        for name, updates in cases:
            with self.subTest(name=name):
                result = resolve_request(mutate_request(build_request(), updates))
                self.assert_blocked_public_result(result)

        for name, raw_request in (
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        ):
            with self.subTest(name=name):
                result = resolver.resolve_post_runtime_hosting_ongoing_runtime(raw_request)  # type: ignore[arg-type]
                self.assert_blocked_public_result(result)

    def test_missing_or_incomplete_declared_non_claims_behavior(self) -> None:
        required = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        variants = (
            ("remove declared_non_claims", lambda req: req.pop("declared_non_claims")),
            ("empty declared_non_claims", lambda req: req.__setitem__("declared_non_claims", {})),
            ("remove one required non-claim", lambda req: req["declared_non_claims"].pop(required)),
            ("set one required non-claim to string", lambda req: req["declared_non_claims"].__setitem__(required, "false")),
            ("set one required non-claim to None", lambda req: req["declared_non_claims"].__setitem__(required, None)),
        )
        for name, mutator in variants:
            with self.subTest(name=name):
                request = build_request()
                mutator(request)
                result = resolve_request(request)
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolve_request(build_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)

        custom = build_request(ongoing_runtime_scope=list(resolver.SUPPORTED_ONGOING_RUNTIME_SCOPE))
        custom_result = resolve_request(custom)
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(custom_result)

    def test_raw_hidden_hostile_content_is_contained(self) -> None:
        request = build_request()
        for section in SELECTED_BASIS_FIELDS:
            basis = request[section]
            for index, key in enumerate(RAW_BODY_KEYS):
                basis[key] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
        original = copy.deepcopy(request)

        result = resolve_request(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_protective_posture(result)
        self.assertEqual(request, original)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            temp_root = Path(tempdir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(build_request()), encoding="utf-8")

            result = resolver.resolve_post_runtime_hosting_ongoing_runtime_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                summary(result)["resolver_module"],
                "resolve_post_runtime_hosting_ongoing_runtime",
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_post_runtime_hosting_ongoing_runtime_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(malformed)

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_runtime_hosting_ongoing_runtime_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)

            missing_result = resolver.resolve_post_runtime_hosting_ongoing_runtime_from_path(
                temp_root / "missing.json"
            )
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(missing_result)

            output_root = temp_root / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_post_runtime_hosting_ongoing_runtime_result(result)
                second = resolver.write_post_runtime_hosting_ongoing_runtime_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("post_runtime_hosting_ongoing_runtime", str(first))
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, str(first))
                self.assertNotIn(fragment, str(second))

    def test_non_mutation(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        result = resolve_request(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])
        for field in SELECTED_BASIS_FIELDS:
            self.assertEqual(request[field], original[field], field)
        for field in POSTURE_FIELDS:
            self.assertEqual(request[field], original[field], field)
        self.assertEqual(request["ongoing_runtime_scope"], original["ongoing_runtime_scope"])

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request(build_request())
        result_summary = summary(result)
        self.assertTrue(
            result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"][
                "declared"
            ]
        )
        self.assertIs(statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result_summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims(result)["runtime_hosting_boundary_v1_failure_repaired"], False)
        self.assertIs(non_claims(result)["runtime_hosting_boundary_v1_failure_hidden"], False)
        self.assertIs(
            non_claims(result)["runtime_hosting_boundary_v1_failure_claimed_passed"],
            False,
        )
        self.assertIs(non_claims(result)["predecessor_failure_repaired"], False)
        self.assertIs(non_claims(result)["predecessor_failure_hidden"], False)
        self.assertIs(non_claims(result)["predecessor_failure_claimed_passed"], False)
        self.assertIs(statement(result)["consumed_request_token_remains_closed"], True)
        self.assertIs(statement(result)["authorization_token_reuse_blocked"], True)
        self.assertIs(result_summary["consumed_request_token_remains_closed"], True)
        self.assertIs(result_summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
