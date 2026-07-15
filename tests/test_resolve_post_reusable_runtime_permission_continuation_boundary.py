"""Executable tests for the continuation-boundary resolver.

This suite is bounded to post-reusable-runtime-permission continuation-boundary
posture only. Reusable-runtime-permission is upstream basis,
reusable-runtime-permission-boundary is upstream basis, ongoing runtime is
upstream basis, and runtime-hosting-boundary v1 remains preserved predecessor
failure lineage. These tests do not create continuation, self-continuation,
self-recursive growth, daemon, loop, public API, participant-facing interface,
distributed network behavior, source transfer, source receipt, reception
authorization, source, authority, currentness, deployment, public release,
operation permission, broader reusable permission, adoption,
receiving-context governance, publication flow, or follow-on work.
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

import resolve_post_reusable_runtime_permission_continuation_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_reusable_runtime_permission_"
    "continuation_boundary"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_ongoing_runtime_reusable_runtime_permission/",
    "post_ongoing_runtime_reusable_runtime_permission_boundary",
    "post_runtime_hosting_ongoing_runtime/",
    "post_runtime_hosting_ongoing_runtime_boundary",
    "post_successor_runtime_step_runtime_hosting/",
    "post_successor_runtime_step_runtime_hosting_boundary_v2",
    "post_successor_runtime_step_runtime_hosting_boundary/",
    "post_minimal_runtime_successor_runtime_step/",
    "post_minimal_runtime_successor_runtime_step_boundary",
    "post_portable_verification_minimal_runtime",
    "post_portable_verification_runtime_boundary",
    "post_portable_verification_runtime_readiness",
    "post_portable_verification_runtime_readiness_boundary",
    "portable_source_body_verification_final_completion",
    "final-completion",
    "portable-verification",
    "/continuation/",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

OFFICIAL_SCOPE_VALUES = (
    "CONTINUATION_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_CONTINUATION_REVIEW_DECLARED",
    "REUSABLE_RUNTIME_PERMISSION_BASIS_PRESERVED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CONTINUATION",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_NOT_CONTINUATION",
    "CONTINUATION_BOUNDARY_NOT_CONTINUATION",
    "CONTINUATION_BOUNDARY_NOT_SELF_CONTINUATION",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_CONTINUATION_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_CONTINUATION_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_CONTINUATION_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "CONTINUATION_BOUNDARY_QUESTION_UNDECLARED",
    "CONTINUATION_BOUNDARY_INTENT_UNSUPPORTED",
    "REUSABLE_RUNTIME_PERMISSION_BASIS_MISSING",
    "REUSABLE_RUNTIME_PERMISSION_NOT_RECORDED",
    "REUSABLE_RUNTIME_PERMISSION_FAILED_CHECKS_PRESENT",
    "REUSABLE_RUNTIME_PERMISSION_VERSION_NOT_0_1_0",
    "REUSABLE_RUNTIME_PERMISSION_DID_NOT_RECORD_BOUNDED_REUSABLE_RUNTIME_PERMISSION_POSTURE",
    "REUSABLE_RUNTIME_PERMISSION_DID_NOT_RECORD_BOUNDED_RUNTIME_REUSE_ENVELOPE",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_AUTHORIZED_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_CREATED_RUNTIME_DAEMON",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_CREATED_RUNTIME_LOOP",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_CREATED_PUBLIC_API",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "REUSABLE_RUNTIME_PERMISSION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_SELF_CONTINUATION",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_DAEMON",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_RUNTIME_LOOP",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PUBLIC_API",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "REUSABLE_RUNTIME_PERMISSION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "REUSABLE_RUNTIME_PERMISSION_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_TREATED_AS_CONTINUATION",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_AUTHORIZED_CONTINUATION",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_AUTHORIZED_SELF_CONTINUATION",
    "BOUNDED_RUNTIME_REUSE_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "CONTINUATION_BOUNDARY_CREATED_BEFORE_REVIEW",
    "CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "CONTINUATION_BOUNDARY_TREATED_AS_CONTINUATION",
    "CONTINUATION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "CONTINUATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "CONTINUATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "CONTINUATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "CONTINUATION_BOUNDARY_TREATED_AS_SOURCE",
    "CONTINUATION_BOUNDARY_TREATED_AS_AUTHORITY",
    "CONTINUATION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "CONTINUATION_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "CONTINUATION_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "CONTINUATION_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "CONTINUATION_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "CONTINUATION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_CONTINUATION_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_CONTINUATION_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_CONTINUATION_BOUNDARY_SCOPE",
    "DECLARED_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_CONTINUATION_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_reusable_runtime_permission_continuation_boundary_metadata",
    "declared_continuation_boundary_question",
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_terminal_summary_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
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
    "continuation_boundary_spec_only_posture",
    "one_future_continuation_review_posture",
    "reusable_runtime_permission_basis_preserved_posture",
    "reusable_runtime_permission_not_continuation_posture",
    "bounded_runtime_reuse_envelope_not_continuation_posture",
    "continuation_boundary_not_continuation_posture",
    "continuation_boundary_not_self_continuation_posture",
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
    "repo_local_availability_not_continuation_boundary_authority_posture",
    "artifact_existence_not_continuation_boundary_authority_posture",
    "latest_file_posture_not_continuation_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "continuation_boundary_scope",
    "continuation_boundary_checks",
    "continuation_boundary_statement",
    "continuation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_reusable_runtime_permission_continuation_boundary_summary",
)

STATEMENT_TRUE_FIELDS = (
    "continuation_boundary_recorded",
    "one_future_continuation_review_declared",
    "reusable_runtime_permission_basis_preserved",
    "reusable_runtime_permission_not_continuation",
    "bounded_runtime_reuse_envelope_not_continuation",
    "continuation_boundary_not_continuation",
    "continuation_boundary_not_self_continuation",
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
    "hidden_repo_state_not_used_as_continuation_boundary_authority",
    "repo_local_availability_not_continuation_boundary_authority",
    "artifact_existence_not_continuation_boundary_authority",
    "latest_file_posture_not_continuation_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

BASIS_SECTION_KEYS = (
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_terminal_summary_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
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

POSTURE_FIELDS = tuple(
    section for section in TOP_LEVEL_SECTIONS if section.endswith("_posture")
)

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_continuation_boundary_body",
    "raw_continuation_body",
    "raw_self_continuation_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "continuation_boundary_body",
    "continuation_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

HOSTILE_SENTINELS = (
    "RAW_CONTINUATION_BOUNDARY_BODY_MUST_NOT_RETURN",
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
    return resolver.build_declared_post_reusable_runtime_permission_continuation_boundary_request()


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return list(result.get("continuation_boundary_checks", []))


def failed_checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [check for check in checks(result) if check.get("passed") is not True]


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["continuation_boundary_statement"]


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


class ContinuationBoundaryResolverTests(unittest.TestCase):
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
            "continuation_boundary_statement",
            "continuation_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name)
            if not isinstance(section, Mapping):
                continue
            for key, value in section.items():
                if isinstance(value, bool):
                    self.assertIs(type(value), bool, key)
                elif key in STATEMENT_TRUE_FIELDS:
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
        scope = result.get("continuation_boundary_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-continuation-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_CONTINUATION_BOUNDARY_SCOPE:
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
        non_claims = result["non_claims"]
        for key in (
            "continuation_authorized",
            "self_continuation_authorized",
            "self_recursive_growth_created",
            "runtime_daemon_created",
            "runtime_loop_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "broader_reusable_permission_created",
            "follow_on_work_authorized",
            "continuation_boundary_treated_as_continuation",
            "reusable_runtime_permission_treated_as_continuation",
            "bounded_runtime_reuse_envelope_treated_as_continuation",
            "consumed_request_reopened",
            "authorization_token_reused",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        self.assert_non_claims_canonical_false(result)

    def assert_recorded_result(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        summary = result["post_reusable_runtime_permission_continuation_boundary_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_post_reusable_runtime_permission_continuation_boundary",
        )
        self.assert_public_block_codes(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_generated_booleans_are_bool(result)

    def resolve_blocked(self, mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
        request = clean_request()
        mutator(request)
        return resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
            request
        )

    def test_public_api_constants_scope_and_block_codes(self) -> None:
        for name in (
            "resolve_post_reusable_runtime_permission_continuation_boundary",
            "resolve_post_reusable_runtime_permission_continuation_boundary_from_path",
            "write_post_reusable_runtime_permission_continuation_boundary_result",
            "build_post_reusable_runtime_permission_continuation_boundary_summary",
            "build_declared_post_reusable_runtime_permission_continuation_boundary_request",
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
            "SUPPORTED_CONTINUATION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_reusable_runtime_permission_continuation_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_CONTINUATION_BOUNDARY_SCOPE,
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
        result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
            request
        )
        self.assert_recorded_result(result)
        metadata = result["post_reusable_runtime_permission_continuation_boundary_metadata"]
        self.assertEqual(
            metadata["post_reusable_runtime_permission_continuation_boundary_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            metadata["post_reusable_runtime_permission_continuation_boundary_id"],
            request["continuation_boundary_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        stmt = statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIn(field, stmt)
            self.assertIs(stmt[field], True, field)
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
            "continuation_boundary_treated_as_continuation",
            "continuation_boundary_treated_as_self_continuation",
            "reusable_runtime_permission_treated_as_continuation",
            "reusable_runtime_permission_treated_as_self_continuation",
            "reusable_runtime_permission_treated_as_runtime_daemon",
            "reusable_runtime_permission_treated_as_runtime_loop",
            "reusable_runtime_permission_treated_as_public_api",
            "reusable_runtime_permission_treated_as_participant_facing_interface",
            "reusable_runtime_permission_treated_as_distributed_network_behavior",
            "bounded_runtime_reuse_envelope_treated_as_continuation",
            "bounded_runtime_reuse_envelope_authorized_continuation",
            "bounded_runtime_reuse_envelope_authorized_self_continuation",
            "bounded_runtime_reuse_envelope_authorized_arbitrary_runtime_activity",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(required_named.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = clean_request()
                request["declared_non_claims"][key] = True
                result = (
                    resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
                        request
                    )
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
            ("explicit block intent", mutate("continuation_boundary_intent", "BLOCK_POST_REUSABLE_RUNTIME_PERMISSION_CONTINUATION_BOUNDARY"), None),
            ("missing request", None, None),
            ("non-mapping request", None, ["not", "mapping"]),
            ("unsupported intent", mutate("continuation_boundary_intent", "UNSUPPORTED"), None),
            ("unsupported scope", mutate("continuation_boundary_scope", list(resolver.SUPPORTED_SCOPE_VALUES) + ["UNSUPPORTED"]), None),
            ("missing reusable-runtime-permission basis", mutate("selected_reusable_runtime_permission_basis", None), None),
            ("reusable-runtime-permission not recorded", mutate("selected_reusable_runtime_permission_result_outcome", "NO"), None),
            ("reusable-runtime-permission failed checks", mutate("selected_reusable_runtime_permission_failed_check_count", 1), None),
            ("reusable-runtime-permission wrong version", mutate("selected_reusable_runtime_permission_result_version", "9.9.9"), None),
            ("reusable-runtime-permission no bounded posture", mutate("selected_reusable_runtime_permission_bounded_posture_recorded", False), None),
            ("reusable-runtime-permission no envelope", mutate("selected_reusable_runtime_permission_bounded_runtime_reuse_envelope_recorded", False), None),
            ("reusable-runtime-permission authorized continuation", mutate("selected_reusable_runtime_permission_already_authorized_continuation", True), None),
            ("reusable-runtime-permission authorized self continuation", mutate("selected_reusable_runtime_permission_already_authorized_self_continuation", True), None),
            ("reusable-runtime-permission created daemon", mutate("selected_reusable_runtime_permission_already_created_runtime_daemon", True), None),
            ("reusable-runtime-permission created loop", mutate("selected_reusable_runtime_permission_already_created_runtime_loop", True), None),
            ("reusable-runtime-permission created public api", mutate("selected_reusable_runtime_permission_already_created_public_api", True), None),
            ("reusable-runtime-permission created participant interface", mutate("selected_reusable_runtime_permission_already_created_participant_facing_interface", True), None),
            ("reusable-runtime-permission created distributed behavior", mutate("selected_reusable_runtime_permission_already_created_distributed_network_behavior", True), None),
            ("reusable-runtime-permission treated as continuation", mutate("selected_reusable_runtime_permission_treated_as_continuation", True), None),
            ("reusable-runtime-permission treated as self continuation", mutate("selected_reusable_runtime_permission_treated_as_self_continuation", True), None),
            ("reusable-runtime-permission treated as daemon", mutate("selected_reusable_runtime_permission_treated_as_runtime_daemon", True), None),
            ("reusable-runtime-permission treated as loop", mutate("selected_reusable_runtime_permission_treated_as_runtime_loop", True), None),
            ("reusable-runtime-permission treated as public api", mutate("selected_reusable_runtime_permission_treated_as_public_api", True), None),
            ("reusable-runtime-permission treated as participant interface", mutate("selected_reusable_runtime_permission_treated_as_participant_facing_interface", True), None),
            ("reusable-runtime-permission treated as distributed behavior", mutate("selected_reusable_runtime_permission_treated_as_distributed_network_behavior", True), None),
            ("reusable-runtime-permission authorized future work", mutate("selected_reusable_runtime_permission_authorized_future_work", True), None),
            ("bounded envelope treated as continuation", mutate("selected_bounded_runtime_reuse_envelope_treated_as_continuation", True), None),
            ("bounded envelope authorized continuation", mutate("selected_bounded_runtime_reuse_envelope_authorized_continuation", True), None),
            ("bounded envelope authorized self continuation", mutate("selected_bounded_runtime_reuse_envelope_authorized_self_continuation", True), None),
            ("bounded envelope authorized arbitrary runtime activity", mutate("selected_bounded_runtime_reuse_envelope_authorized_arbitrary_runtime_activity", True), None),
            ("continuation-boundary created before review", mutate("continuation_boundary_created_before_review", True), None),
            ("continuation authorized", mutate("continuation_authorized", True), None),
            ("self continuation authorized", mutate("self_continuation_authorized", True), None),
            ("self recursive growth created", mutate("self_recursive_growth_created", True), None),
            ("runtime daemon created", mutate("runtime_daemon_created", True), None),
            ("runtime loop created", mutate("runtime_loop_created", True), None),
            ("public api created", mutate("public_api_created", True), None),
            ("participant interface created", mutate("participant_facing_interface_created", True), None),
            ("distributed behavior created", mutate("distributed_network_behavior_created", True), None),
            ("continuation-boundary treated as continuation", mutate("continuation_boundary_treated_as_continuation", True), None),
            ("continuation-boundary treated as self continuation", mutate("continuation_boundary_treated_as_self_continuation", True), None),
            ("continuation-boundary treated as source transfer", mutate("continuation_boundary_treated_as_source_transfer", True), None),
            ("continuation-boundary treated as source receipt", mutate("continuation_boundary_treated_as_source_receipt", True), None),
            ("continuation-boundary treated as reception authorization", mutate("continuation_boundary_treated_as_reception_authorization", True), None),
            ("continuation-boundary treated as source", mutate("continuation_boundary_treated_as_source", True), None),
            ("continuation-boundary treated as authority", mutate("continuation_boundary_treated_as_authority", True), None),
            ("continuation-boundary treated as currentness", mutate("continuation_boundary_treated_as_currentness", True), None),
            ("continuation-boundary treated as deployment", mutate("continuation_boundary_treated_as_deployment", True), None),
            ("continuation-boundary treated as public release", mutate("continuation_boundary_treated_as_public_release", True), None),
            ("continuation-boundary treated as operation permission", mutate("continuation_boundary_treated_as_operation_permission", True), None),
            ("continuation-boundary treated as broader reusable", mutate("continuation_boundary_treated_as_broader_reusable_permission", True), None),
            ("continuation-boundary treated as follow-on", mutate("continuation_boundary_treated_as_follow_on_work", True), None),
            ("source transfer occurred", mutate("source_transfer_occurred", True), None),
            ("source receipt occurred", mutate("source_receipt_occurred", True), None),
            ("reception authorization created", mutate("reception_authorization_created", True), None),
            ("source created", mutate("source_created", True), None),
            ("authority created", mutate("authority_created", True), None),
            ("currentness created", mutate("currentness_created", True), None),
            ("deployment created", mutate("deployment_created", True), None),
            ("public release created", mutate("public_release_created", True), None),
            ("operation permission created", mutate("operation_permission_created", True), None),
            ("broader reusable permission created", mutate("broader_reusable_permission_created", True), None),
            ("derivative reception authorized", mutate("derivative_reception_authorized", True), None),
            ("vessel relation authorized", mutate("vessel_relation_authorized", True), None),
            ("adoption created", mutate("adoption_created", True), None),
            ("receiving governance created", mutate("receiving_context_governance_created", True), None),
            ("publication flow created", mutate("publication_flow_created", True), None),
            ("follow-on work authorized", mutate("follow_on_work_authorized", True), None),
            ("artifact existence authority", mutate("artifact_existence_treated_as_continuation_boundary_authority", True), None),
            ("artifact path currentness", mutate("artifact_path_treated_as_currentness", True), None),
            ("latest file authority", mutate("latest_file_posture_treated_as_continuation_boundary_authority", True), None),
            ("repo local authority", mutate("repo_local_availability_treated_as_continuation_boundary_authority", True), None),
            ("hidden content", mutate("hidden_repo_state_used_as_continuation_boundary_content", True), None),
            ("hidden authority", mutate("hidden_repo_state_used_as_continuation_boundary_authority", True), None),
            ("selected basis not reference shaped", mutate("selected_basis_not_reference_shaped", True), None),
            ("raw body returned", mutate("raw_full_prior_artifact_body_returned", True), None),
            ("predecessor hidden repaired", mutate("predecessor_failure_evidence_hidden_or_repaired", True), None),
            ("consumed request reopened", mutate("consumed_request_reopened", True), None),
            ("authorization reused", mutate("authorization_token_reused", True), None),
            ("required non-claim missing or flipped", mutate_declared_non_claim("continuation_authorized", True), None),
        )
        for name, mutator, direct_request in block_cases:
            with self.subTest(name=name):
                if mutator is None:
                    result = (
                        resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
                            direct_request
                        )
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
        result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
            clean_request()
        )
        self.assert_recorded_result(result)
        self.assert_official_scope_preserved(result)
        custom_request = resolver.build_declared_post_reusable_runtime_permission_continuation_boundary_request(
            continuation_boundary_scope=list(
                resolver.SUPPORTED_CONTINUATION_BOUNDARY_SCOPE
            )
        )
        custom_result = (
            resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
                custom_request
            )
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
        result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
            request
        )
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
            result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary_from_path(
                request_path
            )
            self.assert_recorded_result(result)
            malformed_path = temp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_post_reusable_runtime_permission_continuation_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            array_path = temp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            missing = resolver.resolve_post_reusable_runtime_permission_continuation_boundary_from_path(
                temp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], resolver.OUTCOME_BLOCKED)
            for blocked in (malformed, array_result, missing):
                self.assert_public_block_codes(blocked)
                self.assert_non_claims_canonical_false(blocked)

            output_root = temp_path / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_post_reusable_runtime_permission_continuation_boundary_result(
                    result
                )
                second = resolver.write_post_reusable_runtime_permission_continuation_boundary_result(
                    result
                )
            self.assertTrue(first.parent.exists())
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            path_text = str(first).replace("\\", "/")
            self.assertIn("post_reusable_runtime_permission_continuation_boundary", path_text)
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, path_text)

    def test_non_mutation(self) -> None:
        request = clean_request()
        before = copy.deepcopy(request)
        result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
            request
        )
        self.assert_recorded_result(result)
        self.assertEqual(request, before)
        for section in BASIS_SECTION_KEYS:
            self.assertEqual(request[section], before[section])
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])
        self.assertEqual(
            request["continuation_boundary_scope"],
            before["continuation_boundary_scope"],
        )
        for section in POSTURE_FIELDS:
            self.assertEqual(request[section], before[section])

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_post_reusable_runtime_permission_continuation_boundary(
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
        summary = result["post_reusable_runtime_permission_continuation_boundary_summary"]
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
