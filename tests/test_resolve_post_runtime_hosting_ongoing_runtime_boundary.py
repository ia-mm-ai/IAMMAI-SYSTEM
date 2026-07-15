"""Executable tests for the post-runtime-hosting ongoing-runtime boundary.

This suite is bounded to ongoing-runtime-boundary posture only. Runtime hosting
is upstream basis, runtime-hosting-boundary v2 is upstream boundary basis, and
runtime-hosting-boundary v1 remains preserved predecessor failure lineage. The
tests do not create ongoing runtime, reusable runtime permission, continuation,
self-continuation, daemon, loop, public API, participant-facing interface,
distributed network behavior, source transfer, source receipt, reception
authorization, source, authority, currentness, deployment, public release,
operation permission, reusable permission, adoption, receiving-context
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

import resolve_post_runtime_hosting_ongoing_runtime_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime_boundary"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
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
    "ongoing-runtime",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

OFFICIAL_SCOPE_VALUES = (
    "ONGOING_RUNTIME_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_ONGOING_RUNTIME_REVIEW_DECLARED",
    "RUNTIME_HOSTING_BASIS_PRESERVED",
    "RUNTIME_HOSTING_NOT_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_HOST_RELATION_NOT_CONTINUOUS_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_NOT_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_NOT_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_NOT_CONTINUATION",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "ONGOING_RUNTIME_BOUNDARY_QUESTION_UNDECLARED",
    "ONGOING_RUNTIME_BOUNDARY_INTENT_UNSUPPORTED",
    "RUNTIME_HOSTING_BASIS_MISSING",
    "RUNTIME_HOSTING_NOT_RECORDED",
    "RUNTIME_HOSTING_FAILED_CHECKS_PRESENT",
    "RUNTIME_HOSTING_VERSION_NOT_0_1_0",
    "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_RUNTIME_HOSTING_POSTURE",
    "RUNTIME_HOSTING_DID_NOT_RECORD_BOUNDED_HOST_RELATION",
    "RUNTIME_HOSTING_ALREADY_CREATED_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_ALREADY_AUTHORIZED_CONTINUATION",
    "RUNTIME_HOSTING_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_DAEMON",
    "RUNTIME_HOSTING_ALREADY_CREATED_RUNTIME_LOOP",
    "RUNTIME_HOSTING_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_HOSTING_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_HOSTING_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_HOSTING_TREATED_AS_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_TREATED_AS_CONTINUATION",
    "RUNTIME_HOSTING_TREATED_AS_SELF_CONTINUATION",
    "RUNTIME_HOSTING_TREATED_AS_RUNTIME_DAEMON",
    "RUNTIME_HOSTING_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_HOSTING_TREATED_AS_PUBLIC_API",
    "RUNTIME_HOSTING_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_HOSTING_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_HOSTING_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_HOSTING_HOST_RELATION_RAN_CONTINUOUSLY",
    "RUNTIME_HOSTING_HOST_RELATION_CREATED_ACTIVE_EXECUTION",
    "RUNTIME_HOSTING_HOST_RELATION_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_HOSTING_DID_NOT_CANONICALIZE_NON_CLAIMS",
    "ONGOING_RUNTIME_BOUNDARY_CREATED_BEFORE_REVIEW",
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
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_CONTINUATION",
    "ONGOING_RUNTIME_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ONGOING_RUNTIME_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE",
    "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_ONGOING_RUNTIME_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_runtime_hosting_ongoing_runtime_boundary_metadata",
    "declared_ongoing_runtime_boundary_question",
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
    "ongoing_runtime_boundary_spec_only_posture",
    "one_future_ongoing_runtime_review_posture",
    "runtime_hosting_basis_preserved_posture",
    "runtime_hosting_not_ongoing_runtime_posture",
    "runtime_hosting_host_relation_not_continuous_runtime_posture",
    "ongoing_runtime_boundary_not_ongoing_runtime_posture",
    "ongoing_runtime_boundary_not_reusable_runtime_permission_posture",
    "ongoing_runtime_boundary_not_continuation_posture",
    "ongoing_runtime_not_created_posture",
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
    "repo_local_availability_not_ongoing_runtime_boundary_authority_posture",
    "artifact_existence_not_ongoing_runtime_boundary_authority_posture",
    "latest_file_posture_not_ongoing_runtime_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "ongoing_runtime_boundary_scope",
    "ongoing_runtime_boundary_checks",
    "ongoing_runtime_boundary_statement",
    "ongoing_runtime_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_runtime_hosting_ongoing_runtime_boundary_summary",
)

SELECTED_BASIS_FIELDS = (
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
    "ongoing_runtime_boundary_spec_only_posture",
    "one_future_ongoing_runtime_review_posture",
    "runtime_hosting_basis_preserved_posture",
    "runtime_hosting_not_ongoing_runtime_posture",
    "runtime_hosting_host_relation_not_continuous_runtime_posture",
    "ongoing_runtime_boundary_not_ongoing_runtime_posture",
    "ongoing_runtime_boundary_not_reusable_runtime_permission_posture",
    "ongoing_runtime_boundary_not_continuation_posture",
    "ongoing_runtime_not_created_posture",
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
    "repo_local_availability_not_ongoing_runtime_boundary_authority_posture",
    "artifact_existence_not_ongoing_runtime_boundary_authority_posture",
    "latest_file_posture_not_ongoing_runtime_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

TRUE_STATEMENT_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)

SAFE_STATEMENT_TRUE_FIELDS = (
    "runtime_hosting_basis_preserved",
    "runtime_hosting_not_ongoing_runtime",
    "runtime_hosting_host_relation_not_continuous_runtime",
    "ongoing_runtime_boundary_not_ongoing_runtime",
    "ongoing_runtime_boundary_not_reusable_runtime_permission",
    "ongoing_runtime_boundary_not_continuation",
    "ongoing_runtime_not_created",
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
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SAFE_NON_CLAIM_FALSE_KEYS = (
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
    "another_reception_request_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "ongoing_runtime_boundary_treated_as_ongoing_runtime",
    "ongoing_runtime_boundary_treated_as_reusable_runtime_permission",
    "ongoing_runtime_boundary_treated_as_continuation",
    "ongoing_runtime_boundary_treated_as_self_continuation",
    "runtime_hosting_treated_as_ongoing_runtime",
    "runtime_hosting_treated_as_reusable_runtime_permission",
    "runtime_hosting_treated_as_continuation",
    "runtime_hosting_treated_as_self_continuation",
    "runtime_hosting_treated_as_runtime_daemon",
    "runtime_hosting_treated_as_runtime_loop",
    "runtime_hosting_treated_as_public_api",
    "runtime_hosting_treated_as_participant_facing_interface",
    "runtime_hosting_treated_as_distributed_network_behavior",
    "runtime_hosting_host_relation_ran_continuously",
    "runtime_hosting_host_relation_created_active_execution",
    "runtime_hosting_host_relation_authorized_follow_on_work",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

EXPLICIT_CANONICALIZATION_KEYS = (
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
    "ongoing_runtime_boundary_treated_as_ongoing_runtime",
    "ongoing_runtime_boundary_treated_as_reusable_runtime_permission",
    "ongoing_runtime_boundary_treated_as_continuation",
    "ongoing_runtime_boundary_treated_as_self_continuation",
    "runtime_hosting_treated_as_ongoing_runtime",
    "runtime_hosting_treated_as_reusable_runtime_permission",
    "runtime_hosting_treated_as_continuation",
    "runtime_hosting_treated_as_self_continuation",
    "runtime_hosting_treated_as_runtime_daemon",
    "runtime_hosting_treated_as_runtime_loop",
    "runtime_hosting_treated_as_public_api",
    "runtime_hosting_treated_as_participant_facing_interface",
    "runtime_hosting_treated_as_distributed_network_behavior",
    "runtime_hosting_host_relation_ran_continuously",
    "runtime_hosting_host_relation_created_active_execution",
    "runtime_hosting_host_relation_authorized_follow_on_work",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

SENTINELS = (
    "RAW_ONGOING_RUNTIME_BOUNDARY_BODY_MUST_NOT_RETURN",
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

RAW_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_ongoing_runtime_boundary_body",
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
    "ongoing_runtime_boundary_body",
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
    return resolver.build_declared_post_runtime_hosting_ongoing_runtime_boundary_request(
        **overrides
    )


def resolve(request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary(request)


def summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return resolver.build_post_runtime_hosting_ongoing_runtime_boundary_summary(result)


def metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["post_runtime_hosting_ongoing_runtime_boundary_metadata"]


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["ongoing_runtime_boundary_statement"]


def non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["non_claims"]


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return result["ongoing_runtime_boundary_checks"]


def set_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[field] = value

    return mutate


def remove_field(field: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.pop(field, None)

    return mutate


def flip_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {})[key] = True
        request[key] = True

    return mutate


class PostRuntimeHostingOngoingRuntimeBoundaryTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_blocked_publicly(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsInstance(result.get("block"), Mapping)
        self.assertIsNotNone(result["block"].get("block_code"))
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assertTrue(any(not check["passed"] for check in checks(result)))
        self.assert_public_codes(result)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        self.assertEqual(set(emitted), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
            self.assertIs(type(emitted[key]), bool, key)

    def assert_safe_boundary_posture(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        for key in SAFE_NON_CLAIM_FALSE_KEYS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
        surface = statement(result)
        for key in SAFE_STATEMENT_TRUE_FIELDS:
            self.assertIn(key, surface)
            self.assertIs(surface[key], True, key)
            self.assertIs(type(surface[key]), bool, key)

    def assert_generated_booleans_are_bool(self, result: Mapping[str, Any]) -> None:
        for key, value in statement(result).items():
            self.assertIs(type(value), bool, key)
        for key, value in non_claims(result).items():
            self.assertIs(type(value), bool, key)
        for key, value in result["ongoing_runtime_boundary_non_meaning"].items():
            self.assertIs(type(value), bool, key)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result["ongoing_runtime_boundary_scope"]
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-ongoing-runtime-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE:
            self.assertIn(value, scope)

    def assert_selected_bases_declared(self, result: Mapping[str, Any]) -> None:
        for section in SELECTED_BASIS_FIELDS:
            self.assertIn(section, result)
            self.assertIs(result[section]["declared"], True, section)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_runtime_hosting_ongoing_runtime_boundary",
            "resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path",
            "write_post_runtime_hosting_ongoing_runtime_boundary_result",
            "build_post_runtime_hosting_ongoing_runtime_boundary_summary",
            "build_declared_post_runtime_hosting_ongoing_runtime_boundary_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_runtime_hosting_ongoing_runtime_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        output_root = resolver.OUTPUT_ROOT.as_posix()
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)

        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_no_argument_builder_records_cleanly(self) -> None:
        request = build_request()
        result = resolve(request)
        result_summary = summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(result_summary["failed_check_count"], 0)
        self.assertGreater(result_summary["passed_check_count"], 0)
        self.assertEqual(result_summary["result_version"], "0.1.0")
        self.assertEqual(result_summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            metadata(result)["post_runtime_hosting_ongoing_runtime_boundary_id"],
            request["ongoing_runtime_boundary_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        for field in TRUE_STATEMENT_FIELDS:
            self.assertIn(field, statement(result))
            self.assertIs(statement(result)[field], True, field)
            self.assertIs(type(statement(result)[field]), bool, field)

        self.assert_selected_bases_declared(result)
        self.assertEqual(
            result["selected_runtime_hosting_basis"]["selected_outcome"],
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_RECORDED",
        )
        self.assertEqual(
            result["selected_runtime_hosting_basis"]["selected_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            result["selected_runtime_hosting_basis"]["selected_failed_check_count"],
            0,
        )
        self.assertEqual(
            result["selected_runtime_hosting_boundary_v2_basis"]["selected_outcome"],
            "POST_SUCCESSOR_RUNTIME_STEP_RUNTIME_HOSTING_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            result["selected_runtime_hosting_boundary_v2_basis"][
                "selected_result_version"
            ],
            "0.2.0",
        )
        self.assertEqual(
            result["selected_runtime_hosting_boundary_v2_basis"][
                "selected_failed_check_count"
            ],
            0,
        )
        self.assertEqual(
            result["selected_successor_runtime_step_basis"]["selected_outcome"],
            "POST_MINIMAL_RUNTIME_SUCCESSOR_RUNTIME_STEP_RECORDED",
        )
        self.assertEqual(
            result["selected_minimal_runtime_basis"]["selected_outcome"],
            "POST_PORTABLE_VERIFICATION_MINIMAL_RUNTIME_RECORDED",
        )

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_safe_boundary_posture(result)
        self.assert_generated_booleans_are_bool(result)
        self.assert_official_scope_preserved(result)

    def test_each_flipped_declared_non_claim_blocks_but_output_stays_canonical(self) -> None:
        self.assertTrue(
            set(EXPLICIT_CANONICALIZATION_KEYS).issubset(
                set(resolver.REQUIRED_FALSE_NON_CLAIMS)
            )
        )

        clean = build_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = copy.deepcopy(clean)
                request["declared_non_claims"][key] = True
                result = resolve(request)

                self.assert_blocked_publicly(result)
                self.assert_canonical_non_claims(result)
                self.assertIs(non_claims(result)[key], False)
                self.assert_safe_boundary_posture(result)
                self.assertIs(non_claims(result)["consumed_request_reopened"], False)
                self.assertIs(non_claims(result)["authorization_token_reused"], False)
                self.assertIs(non_claims(result)["predecessor_failure_repaired"], False)
                self.assertIs(non_claims(result)["predecessor_failure_hidden"], False)
                self.assertIs(non_claims(result)["predecessor_failure_claimed_passed"], False)

    def test_representative_blocking_behavior_preserves_boundary_membrane(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None] | str], ...] = (
            ("explicit block intent", set_field("ongoing_runtime_boundary_intent", "BLOCK_POST_RUNTIME_HOSTING_ONGOING_RUNTIME_BOUNDARY")),
            ("missing request", "missing_request"),
            ("non-mapping request", "non_mapping_request"),
            ("unsupported intent", set_field("ongoing_runtime_boundary_intent", "UNSUPPORTED_ONGOING_RUNTIME_BOUNDARY")),
            ("unsupported scope", set_field("ongoing_runtime_boundary_scope", ["UNSUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE"])),
            ("missing runtime-hosting basis", remove_field("selected_runtime_hosting_basis")),
            ("runtime-hosting not recorded", set_field("selected_runtime_hosting_result_outcome", "NOT_RECORDED")),
            ("runtime-hosting failed checks present", set_field("selected_runtime_hosting_failed_check_count", 1)),
            ("runtime-hosting version not 0.1.0", set_field("selected_runtime_hosting_result_version", "0.2.0")),
            ("runtime-hosting did not record bounded posture", set_field("selected_runtime_hosting_bounded_runtime_hosting_posture_recorded", False)),
            ("runtime-hosting did not record host relation", set_field("selected_runtime_hosting_bounded_host_relation_recorded", False)),
            ("runtime-hosting already created ongoing runtime", set_field("selected_runtime_hosting_already_created_ongoing_runtime", True)),
            ("runtime-hosting already created reusable runtime permission", set_field("selected_runtime_hosting_already_created_reusable_runtime_permission", True)),
            ("runtime-hosting already authorized continuation", set_field("selected_runtime_hosting_already_authorized_continuation", True)),
            ("runtime-hosting already authorized self-continuation", set_field("selected_runtime_hosting_already_authorized_self_continuation", True)),
            ("runtime-hosting already created daemon", set_field("selected_runtime_hosting_already_created_runtime_daemon", True)),
            ("runtime-hosting already created loop", set_field("selected_runtime_hosting_already_created_runtime_loop", True)),
            ("runtime-hosting already created public API", set_field("selected_runtime_hosting_already_created_public_api", True)),
            ("runtime-hosting already created participant-facing interface", set_field("selected_runtime_hosting_already_created_participant_facing_interface", True)),
            ("runtime-hosting already created distributed network behavior", set_field("selected_runtime_hosting_already_created_distributed_network_behavior", True)),
            ("runtime-hosting treated as ongoing runtime", set_field("selected_runtime_hosting_treated_as_ongoing_runtime", True)),
            ("runtime-hosting treated as reusable runtime permission", set_field("selected_runtime_hosting_treated_as_reusable_runtime_permission", True)),
            ("runtime-hosting treated as continuation", set_field("selected_runtime_hosting_treated_as_continuation", True)),
            ("runtime-hosting treated as self-continuation", set_field("selected_runtime_hosting_treated_as_self_continuation", True)),
            ("runtime-hosting treated as daemon", set_field("selected_runtime_hosting_treated_as_runtime_daemon", True)),
            ("runtime-hosting treated as loop", set_field("selected_runtime_hosting_treated_as_runtime_loop", True)),
            ("runtime-hosting treated as public API", set_field("selected_runtime_hosting_treated_as_public_api", True)),
            ("runtime-hosting treated as participant-facing interface", set_field("selected_runtime_hosting_treated_as_participant_facing_interface", True)),
            ("runtime-hosting treated as distributed network behavior", set_field("selected_runtime_hosting_treated_as_distributed_network_behavior", True)),
            ("runtime-hosting authorized future work", set_field("selected_runtime_hosting_authorized_future_work", True)),
            ("runtime-hosting host relation ran continuously", set_field("selected_runtime_hosting_host_relation_ran_continuously", True)),
            ("runtime-hosting host relation created active execution", set_field("selected_runtime_hosting_host_relation_created_active_execution", True)),
            ("runtime-hosting host relation authorized follow-on work", set_field("selected_runtime_hosting_host_relation_authorized_follow_on_work", True)),
            ("runtime-hosting did not canonicalize non-claims", set_field("selected_runtime_hosting_non_claims_canonicalized", False)),
            ("runtime-hosting-boundary v2 basis missing", remove_field("selected_runtime_hosting_boundary_v2_basis")),
            ("runtime-hosting-boundary v2 not recorded", set_field("selected_runtime_hosting_boundary_v2_result_outcome", "NOT_RECORDED")),
            ("runtime-hosting-boundary v2 version not 0.2.0", set_field("selected_runtime_hosting_boundary_v2_result_version", "0.1.0")),
            ("runtime-hosting-boundary v2 failed checks present", set_field("selected_runtime_hosting_boundary_v2_failed_check_count", 1)),
            ("v1 failure repaired", set_field("selected_runtime_hosting_boundary_v1_failure_repaired", True)),
            ("v1 failure hidden", set_field("selected_runtime_hosting_boundary_v1_failure_hidden", True)),
            ("v1 failure claimed passed", set_field("selected_runtime_hosting_boundary_v1_failure_claimed_passed", True)),
            ("successor-runtime-step basis missing", remove_field("selected_successor_runtime_step_basis")),
            ("minimal-runtime basis missing", remove_field("selected_minimal_runtime_basis")),
            ("runtime-boundary basis missing", remove_field("selected_runtime_boundary_basis")),
            ("runtime-readiness basis missing", remove_field("selected_runtime_readiness_basis")),
            ("portable final-completion basis missing", remove_field("selected_portable_verification_final_completion_basis")),
            ("currentness surface basis missing", remove_field("selected_post_portable_verification_currentness_basis")),
            ("ongoing-runtime boundary created before review", set_field("ongoing_runtime_boundary_created_before_review", True)),
            ("ongoing runtime created", flip_non_claim("ongoing_runtime_created")),
            ("reusable runtime permission created", flip_non_claim("reusable_runtime_permission_created")),
            ("continuation authorized", flip_non_claim("continuation_authorized")),
            ("self-continuation authorized", flip_non_claim("self_continuation_authorized")),
            ("self-recursive growth created", flip_non_claim("self_recursive_growth_created")),
            ("runtime daemon created", flip_non_claim("runtime_daemon_created")),
            ("runtime loop created", flip_non_claim("runtime_loop_created")),
            ("public API created", flip_non_claim("public_api_created")),
            ("participant-facing interface created", flip_non_claim("participant_facing_interface_created")),
            ("distributed network behavior created", flip_non_claim("distributed_network_behavior_created")),
            ("ongoing-runtime boundary treated as ongoing runtime", flip_non_claim("ongoing_runtime_boundary_treated_as_ongoing_runtime")),
            ("ongoing-runtime boundary treated as reusable runtime permission", flip_non_claim("ongoing_runtime_boundary_treated_as_reusable_runtime_permission")),
            ("ongoing-runtime boundary treated as continuation", flip_non_claim("ongoing_runtime_boundary_treated_as_continuation")),
            ("ongoing-runtime boundary treated as self-continuation", flip_non_claim("ongoing_runtime_boundary_treated_as_self_continuation")),
            ("ongoing-runtime boundary treated as source transfer", flip_non_claim("ongoing_runtime_boundary_treated_as_source_transfer")),
            ("ongoing-runtime boundary treated as source receipt", flip_non_claim("ongoing_runtime_boundary_treated_as_source_receipt")),
            ("ongoing-runtime boundary treated as reception authorization", flip_non_claim("ongoing_runtime_boundary_treated_as_reception_authorization")),
            ("ongoing-runtime boundary treated as source", flip_non_claim("ongoing_runtime_boundary_treated_as_source")),
            ("ongoing-runtime boundary treated as authority", flip_non_claim("ongoing_runtime_boundary_treated_as_authority")),
            ("ongoing-runtime boundary treated as currentness", flip_non_claim("ongoing_runtime_boundary_treated_as_currentness")),
            ("ongoing-runtime boundary treated as deployment", flip_non_claim("ongoing_runtime_boundary_treated_as_deployment")),
            ("ongoing-runtime boundary treated as public release", flip_non_claim("ongoing_runtime_boundary_treated_as_public_release")),
            ("ongoing-runtime boundary treated as operation permission", flip_non_claim("ongoing_runtime_boundary_treated_as_operation_permission")),
            ("ongoing-runtime boundary treated as reusable permission", flip_non_claim("ongoing_runtime_boundary_treated_as_reusable_permission")),
            ("ongoing-runtime boundary treated as follow-on work", flip_non_claim("ongoing_runtime_boundary_treated_as_follow_on_work")),
            ("source transfer occurred", flip_non_claim("source_transfer_occurred")),
            ("source receipt occurred", flip_non_claim("source_receipt_occurred")),
            ("reception authorization created", flip_non_claim("reception_authorization_created")),
            ("source created", flip_non_claim("source_created")),
            ("authority created", flip_non_claim("authority_created")),
            ("currentness created", flip_non_claim("currentness_created")),
            ("deployment created", flip_non_claim("deployment_created")),
            ("public release created", flip_non_claim("public_release_created")),
            ("operation permission created", flip_non_claim("operation_permission_created")),
            ("reusable permission created", flip_non_claim("reusable_permission_created")),
            ("derivative reception authorized", flip_non_claim("derivative_reception_authorized")),
            ("vessel relation authorized", flip_non_claim("vessel_relation_authorized")),
            ("adoption created", flip_non_claim("adoption_created")),
            ("receiving-context governance created", flip_non_claim("receiving_context_governance_created")),
            ("publication flow created", flip_non_claim("publication_flow_created")),
            ("follow-on work authorized", flip_non_claim("follow_on_work_authorized")),
            ("artifact existence treated as authority", flip_non_claim("artifact_existence_treated_as_ongoing_runtime_boundary_authority")),
            ("artifact path treated as currentness", flip_non_claim("artifact_path_treated_as_currentness")),
            ("latest file posture treated as authority", flip_non_claim("latest_file_posture_treated_as_ongoing_runtime_boundary_authority")),
            ("repo-local availability treated as authority", flip_non_claim("repo_local_availability_treated_as_ongoing_runtime_boundary_authority")),
            ("hidden repo state used as content", flip_non_claim("hidden_repo_state_used_as_ongoing_runtime_boundary_content")),
            ("hidden repo state used as authority", flip_non_claim("hidden_repo_state_used_as_ongoing_runtime_boundary_authority")),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", flip_non_claim("raw_full_prior_artifact_body_returned")),
            ("predecessor failure repaired", flip_non_claim("predecessor_failure_repaired")),
            ("predecessor failure hidden", flip_non_claim("predecessor_failure_hidden")),
            ("predecessor failure claimed passed", flip_non_claim("predecessor_failure_claimed_passed")),
            ("consumed request reopened", flip_non_claim("consumed_request_reopened")),
            ("authorization token reused", flip_non_claim("authorization_token_reused")),
            ("required non-claim missing", remove_field("declared_non_claims")),
        )

        for label, mutation in cases:
            with self.subTest(label=label):
                if mutation == "missing_request":
                    result = resolve(None)
                elif mutation == "non_mapping_request":
                    result = resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary(
                        ["not", "a", "mapping"]
                    )
                else:
                    request = build_request()
                    mutation(request)
                    result = resolve(request)

                self.assert_blocked_publicly(result)
                self.assert_canonical_non_claims(result)
                self.assert_safe_boundary_posture(result)

    def test_missing_or_incomplete_declared_non_claims_do_not_leak_to_output(self) -> None:
        request = build_request()
        variants: list[tuple[str, dict[str, Any]]] = []
        missing = copy.deepcopy(request)
        missing.pop("declared_non_claims")
        variants.append(("missing declared_non_claims", missing))
        empty = copy.deepcopy(request)
        empty["declared_non_claims"] = {}
        variants.append(("empty declared_non_claims", empty))
        one_missing = copy.deepcopy(request)
        one_missing["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
        variants.append(("one required non-claim missing", one_missing))
        string_value = copy.deepcopy(request)
        string_value["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[1]] = "false"
        variants.append(("one required non-claim string", string_value))
        none_value = copy.deepcopy(request)
        none_value["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[2]] = None
        variants.append(("one required non-claim None", none_value))

        for label, variant in variants:
            with self.subTest(label=label):
                result = resolve(variant)
                self.assertIn(
                    result["outcome"],
                    (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                )
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)
                self.assert_safe_boundary_posture(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolve(build_request())
        self.assert_official_scope_preserved(result)

        custom_request = build_request()
        custom_request["ongoing_runtime_boundary_scope"] = list(
            resolver.SUPPORTED_ONGOING_RUNTIME_BOUNDARY_SCOPE
        )
        custom_result = resolve(custom_request)
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(custom_result)
        self.assert_canonical_non_claims(custom_result)

    def test_raw_and_hidden_hostile_content_is_contained_without_mutation(self) -> None:
        request = build_request()
        for section in SELECTED_BASIS_FIELDS:
            for index, raw_key in enumerate(RAW_KEYS):
                request[section][raw_key] = SENTINELS[index % len(SENTINELS)]
            request[section]["nested_payload"] = {"payload": list(SENTINELS)}
        original = copy.deepcopy(request)

        result = resolve(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_codes(result)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_boundary_posture(result)
        self.assertEqual(request, original)

    def test_path_and_write_behavior_are_ongoing_runtime_boundary_contained(self) -> None:
        request = build_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.1.0")
            self.assertEqual(summary(result)["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(malformed)
            self.assert_canonical_non_claims(malformed)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)
            self.assert_canonical_non_claims(array_result)

            missing = resolver.resolve_post_runtime_hosting_ongoing_runtime_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(missing)
            self.assert_canonical_non_claims(missing)

            redirected_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_runtime_hosting_ongoing_runtime_boundary"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first = resolver.write_post_runtime_hosting_ongoing_runtime_boundary_result(
                    result
                )
                second = resolver.write_post_runtime_hosting_ongoing_runtime_boundary_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            written_path = first.relative_to(tmp_path).as_posix()
            self.assertIn("post_runtime_hosting_ongoing_runtime_boundary", written_path)
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, written_path)

    def test_resolver_does_not_mutate_input_request(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        result = resolve(request)

        self.assertEqual(request, original)
        self.assert_canonical_non_claims(result)
        for field in ("declared_non_claims", "ongoing_runtime_boundary_scope"):
            self.assertEqual(request[field], original[field], field)
        for field in SELECTED_BASIS_FIELDS:
            self.assertEqual(request[field], original[field], field)
        for field in POSTURE_FIELDS:
            self.assertEqual(request[field], original[field], field)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve(build_request())
        result_summary = summary(result)
        lineage = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]
        lineage_basis = lineage["basis"]

        self.assertIs(lineage["declared"], True)
        self.assertEqual(lineage_basis["basis_kind"], "preserved failed predecessor evidence")
        self.assertIs(lineage_basis["repaired"], False)
        self.assertIs(lineage_basis["hidden"], False)
        self.assertIs(lineage_basis["claimed_passed"], False)
        self.assertIs(statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims(result)["predecessor_failure_repaired"], False)
        self.assertIs(non_claims(result)["predecessor_failure_hidden"], False)
        self.assertIs(non_claims(result)["predecessor_failure_claimed_passed"], False)
        self.assertIs(statement(result)["consumed_request_token_remains_closed"], True)
        self.assertIs(statement(result)["authorization_token_reuse_blocked"], True)
        self.assertIs(result_summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result_summary["consumed_request_token_remains_closed"], True)
        self.assertIs(result_summary["authorization_token_reuse_blocked"], True)
        serialized = json.dumps(result, sort_keys=True).lower()
        self.assertNotIn("v1 passed", serialized)
        self.assertNotIn("v1 test passed", serialized)


if __name__ == "__main__":
    unittest.main()
