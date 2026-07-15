"""Executable tests for the post-self-continuation self-recursive-growth boundary.

This suite is bounded to self-recursive-growth-boundary posture only.
Self-continuation and self-continuation-boundary are upstream basis, and
runtime-hosting-boundary v1 remains preserved predecessor failure lineage.
These tests do not create self-recursive growth, daemon, loop, public API,
participant-facing interface, distributed network behavior, source transfer,
source receipt, reception authorization, source, authority, currentness,
deployment, public release, operation permission, broader reusable permission,
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

import resolve_post_self_continuation_self_recursive_growth_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth_boundary"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_continuation_self_continuation",
    "post_continuation_self_continuation_boundary",
    "post_reusable_runtime_permission_continuation",
    "post_ongoing_runtime_reusable_runtime_permission",
    "post_runtime_hosting_ongoing_runtime",
    "post_successor_runtime_step_runtime_hosting",
    "self-recursive-growth",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

FORBIDDEN_WRITE_FRAGMENTS = (
    "post_continuation_self_continuation/",
    "post_continuation_self_continuation_boundary",
    "post_reusable_runtime_permission_continuation/",
    "post_reusable_runtime_permission_continuation_boundary",
    "post_ongoing_runtime_reusable_runtime_permission/",
    "post_ongoing_runtime_reusable_runtime_permission_boundary",
    "post_runtime_hosting_ongoing_runtime/",
    "post_runtime_hosting_ongoing_runtime_boundary",
    "post_successor_runtime_step_runtime_hosting/",
    "post_successor_runtime_step_runtime_hosting_boundary_v2",
    "post_successor_runtime_step_runtime_hosting_boundary/",
    "post_minimal_runtime_successor_runtime_step",
    "post_portable_verification_runtime_boundary",
    "post_portable_verification_runtime_readiness",
    "portable_source_body_verification_final_completion",
    "portable-verification",
    "self-recursive-growth",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception/",
)

OFFICIAL_SCOPE_VALUES = (
    "SELF_RECURSIVE_GROWTH_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW_DECLARED",
    "SELF_CONTINUATION_BASIS_PRESERVED",
    "SELF_CONTINUATION_NOT_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_NOT_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_LOOP",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SELF_RECURSIVE_GROWTH_BOUNDARY_QUESTION_UNDECLARED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_INTENT_UNSUPPORTED",
    "SELF_CONTINUATION_BASIS_MISSING",
    "SELF_CONTINUATION_NOT_RECORDED",
    "SELF_CONTINUATION_FAILED_CHECKS_PRESENT",
    "SELF_CONTINUATION_VERSION_NOT_0_1_0",
    "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_POSTURE",
    "SELF_CONTINUATION_DID_NOT_RECORD_BOUNDED_SELF_CONTINUATION_ENVELOPE",
    "SELF_CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP",
    "SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API",
    "SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_TREATED_AS_RUNTIME_DAEMON",
    "SELF_CONTINUATION_TREATED_AS_RUNTIME_LOOP",
    "SELF_CONTINUATION_TREATED_AS_PUBLIC_API",
    "SELF_CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "SELF_CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_CONTINUATION_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_SELF_RECURSIVE_GROWTH",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_DAEMON",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_RUNTIME_LOOP",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_CREATED_BEFORE_REVIEW",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SOURCE",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_AUTHORITY",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE",
    "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SELF_RECURSIVE_GROWTH_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_self_continuation_self_recursive_growth_boundary_metadata",
    "declared_self_recursive_growth_boundary_question",
    "selected_self_continuation_basis",
    "selected_self_continuation_terminal_summary_basis",
    "selected_self_continuation_boundary_basis",
    "selected_continuation_basis",
    "selected_continuation_boundary_basis",
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
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
    "self_recursive_growth_boundary_spec_only_posture",
    "one_future_self_recursive_growth_review_posture",
    "self_continuation_basis_preserved_posture",
    "self_continuation_not_self_recursive_growth_posture",
    "bounded_self_continuation_envelope_not_self_recursive_growth_posture",
    "self_recursive_growth_boundary_not_self_recursive_growth_posture",
    "self_recursive_growth_boundary_not_daemon_posture",
    "self_recursive_growth_boundary_not_loop_posture",
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
    "repo_local_availability_not_self_recursive_growth_boundary_authority_posture",
    "artifact_existence_not_self_recursive_growth_boundary_authority_posture",
    "latest_file_posture_not_self_recursive_growth_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "self_recursive_growth_boundary_scope",
    "self_recursive_growth_boundary_checks",
    "self_recursive_growth_boundary_statement",
    "self_recursive_growth_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_self_continuation_self_recursive_growth_boundary_summary",
)

STATEMENT_TRUE_FIELDS = (
    "self_recursive_growth_boundary_recorded",
    "one_future_self_recursive_growth_review_declared",
    "self_continuation_basis_preserved",
    "self_continuation_not_self_recursive_growth",
    "bounded_self_continuation_envelope_not_self_recursive_growth",
    "self_recursive_growth_boundary_not_self_recursive_growth",
    "self_recursive_growth_boundary_not_daemon",
    "self_recursive_growth_boundary_not_loop",
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
    "hidden_repo_state_not_used_as_self_recursive_growth_boundary_authority",
    "repo_local_availability_not_self_recursive_growth_boundary_authority",
    "artifact_existence_not_self_recursive_growth_boundary_authority",
    "latest_file_posture_not_self_recursive_growth_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SENTINELS = (
    "RAW_SELF_RECURSIVE_GROWTH_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SELF_RECURSIVE_GROWTH_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

SENSITIVE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_self_recursive_growth_boundary_body",
    "raw_self_recursive_growth_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_recursive_growth_boundary_body",
    "self_recursive_growth_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

BASIS_SECTION_NAMES = (
    "selected_self_continuation_basis",
    "selected_self_continuation_terminal_summary_basis",
    "selected_self_continuation_boundary_basis",
    "selected_continuation_basis",
    "selected_continuation_boundary_basis",
    "selected_reusable_runtime_permission_basis",
    "selected_reusable_runtime_permission_boundary_basis",
    "selected_ongoing_runtime_basis",
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


def build_request(**overrides: Any) -> dict[str, Any]:
    return resolver.build_declared_post_self_continuation_self_recursive_growth_boundary_request(
        **overrides
    )


def resolve(request: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return resolver.resolve_post_self_continuation_self_recursive_growth_boundary(request)


def metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["post_self_continuation_self_recursive_growth_boundary_metadata"]


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["self_recursive_growth_boundary_statement"]


def non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return result["non_claims"]


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return result["self_recursive_growth_boundary_checks"]


def mutate_basis(field: str, key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        basis = request.setdefault(field, {})
        if not isinstance(basis, dict):
            request[field] = {}
            basis = request[field]
        basis[key] = value

    return apply


def set_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        request[field] = value

    return apply


def remove_field(field: str) -> Callable[[dict[str, Any]], None]:
    def apply(request: dict[str, Any]) -> None:
        request.pop(field, None)

    return apply


class PostSelfContinuationSelfRecursiveGrowthBoundaryTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_boolean_posture(self, result: Mapping[str, Any]) -> None:
        for key, value in statement(result).items():
            self.assertIs(type(value), bool, key)
        for key, value in non_claims(result).items():
            self.assertIs(type(value), bool, key)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        self.assertEqual(set(emitted), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
            self.assertIs(type(emitted[key]), bool, key)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope(self, result: Mapping[str, Any]) -> None:
        scope = result["self_recursive_growth_boundary_scope"]
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-self-recursive-growth-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE:
            self.assertIn(value, scope)

    def assert_safe_boundary_posture(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        for key in (
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
            "self_recursive_growth_boundary_treated_as_self_recursive_growth",
            "self_continuation_treated_as_self_recursive_growth",
            "bounded_self_continuation_envelope_treated_as_self_recursive_growth",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(emitted[key], False, key)
        stmt = statement(result)
        for key in (
            "self_recursive_growth_not_created",
            "runtime_daemon_not_created",
            "runtime_loop_not_created",
            "public_api_not_created",
            "participant_facing_interface_not_created",
            "distributed_network_behavior_not_created",
            "source_not_created",
            "authority_not_created",
            "currentness_not_created",
            "deployment_not_created",
            "public_release_not_created",
            "operation_permission_not_created",
            "broader_reusable_permission_not_created",
            "follow_on_work_not_authorized",
            "predecessor_failure_evidence_preserved",
            "consumed_request_token_remains_closed",
            "authorization_token_reuse_blocked",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(stmt[key], True, key)

    def assert_blocked_public_safe(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIsNotNone(result.get("block"))
        self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
        self.assertGreater(
            sum(1 for check in checks(result) if check.get("passed") is not True),
            0,
        )
        self.assert_public_codes(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_boundary_posture(result)
        self.assert_boolean_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_self_continuation_self_recursive_growth_boundary",
            "resolve_post_self_continuation_self_recursive_growth_boundary_from_path",
            "write_post_self_continuation_self_recursive_growth_boundary_result",
            "build_post_self_continuation_self_recursive_growth_boundary_summary",
            "build_declared_post_self_continuation_self_recursive_growth_boundary_request",
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
            "SUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_self_continuation_self_recursive_growth_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        output_root = Path(resolver.OUTPUT_ROOT).as_posix()
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)

        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolve(request)
        summary = resolver.build_post_self_continuation_self_recursive_growth_boundary_summary(
            result
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(
            summary["resolver_module"],
            "resolve_post_self_continuation_self_recursive_growth_boundary",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            summary["request_id"],
            request["self_recursive_growth_boundary_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        stmt = statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIs(stmt[field], True, field)

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_boolean_posture(result)
        self.assert_official_scope(result)
        self.assert_no_sentinels(result)

    def test_critical_declared_non_claim_canonicalization_blocks_flipped_input(self) -> None:
        explicit_names = (
            "self_recursive_growth_created",
            "runtime_daemon_created",
            "runtime_loop_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "self_recursive_growth_boundary_treated_as_self_recursive_growth",
            "self_recursive_growth_boundary_treated_as_runtime_daemon",
            "self_recursive_growth_boundary_treated_as_runtime_loop",
            "self_continuation_treated_as_self_recursive_growth",
            "self_continuation_treated_as_runtime_daemon",
            "self_continuation_treated_as_runtime_loop",
            "self_continuation_treated_as_public_api",
            "self_continuation_treated_as_participant_facing_interface",
            "self_continuation_treated_as_distributed_network_behavior",
            "bounded_self_continuation_envelope_treated_as_self_recursive_growth",
            "bounded_self_continuation_envelope_authorized_self_recursive_growth",
            "bounded_self_continuation_envelope_authorized_runtime_daemon",
            "bounded_self_continuation_envelope_authorized_runtime_loop",
            "bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        for name in explicit_names:
            self.assertIn(name, resolver.REQUIRED_FALSE_NON_CLAIMS)

        clean_request = build_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = copy.deepcopy(clean_request)
                request["declared_non_claims"][key] = True
                result = resolve(request)
                self.assert_blocked_public_safe(result)
                self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None] | None], ...] = (
            ("explicit block intent", set_field("self_recursive_growth_boundary_intent", "BLOCK_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH_BOUNDARY")),
            ("unsupported intent", set_field("self_recursive_growth_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", set_field("self_recursive_growth_boundary_scope", ["UNSUPPORTED_SCOPE_VALUE"])),
            ("missing self-continuation basis", remove_field("selected_self_continuation_basis")),
            ("self-continuation not recorded", mutate_basis("selected_self_continuation_basis", "outcome", "NOT_RECORDED")),
            ("self-continuation failed checks present", mutate_basis("selected_self_continuation_basis", "failed_check_count", 1)),
            ("self-continuation version not 0.1.0", mutate_basis("selected_self_continuation_basis", "result_version", "9.9.9")),
            ("self-continuation did not record bounded posture", set_field("selected_self_continuation_bounded_posture_recorded", False)),
            ("self-continuation did not record bounded envelope", set_field("selected_self_continuation_bounded_self_continuation_envelope_recorded", False)),
            ("self-continuation already created self-recursive growth", set_field("selected_self_continuation_already_created_self_recursive_growth", True)),
            ("self-continuation already created daemon", set_field("selected_self_continuation_already_created_runtime_daemon", True)),
            ("self-continuation already created loop", set_field("selected_self_continuation_already_created_runtime_loop", True)),
            ("self-continuation already created public API", set_field("selected_self_continuation_already_created_public_api", True)),
            ("self-continuation already created participant-facing interface", set_field("selected_self_continuation_already_created_participant_facing_interface", True)),
            ("self-continuation already created distributed behavior", set_field("selected_self_continuation_already_created_distributed_network_behavior", True)),
            ("self-continuation treated as self-recursive growth", set_field("selected_self_continuation_treated_as_self_recursive_growth", True)),
            ("self-continuation treated as daemon", set_field("selected_self_continuation_treated_as_runtime_daemon", True)),
            ("self-continuation treated as loop", set_field("selected_self_continuation_treated_as_runtime_loop", True)),
            ("self-continuation treated as public API", set_field("selected_self_continuation_treated_as_public_api", True)),
            ("self-continuation treated as participant-facing interface", set_field("selected_self_continuation_treated_as_participant_facing_interface", True)),
            ("self-continuation treated as distributed behavior", set_field("selected_self_continuation_treated_as_distributed_network_behavior", True)),
            ("self-continuation authorized future work", set_field("selected_self_continuation_authorized_future_work", True)),
            ("bounded envelope treated as self-recursive growth", set_field("selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth", True)),
            ("bounded envelope authorized self-recursive growth", set_field("selected_bounded_self_continuation_envelope_authorized_self_recursive_growth", True)),
            ("bounded envelope authorized daemon", set_field("selected_bounded_self_continuation_envelope_authorized_runtime_daemon", True)),
            ("bounded envelope authorized loop", set_field("selected_bounded_self_continuation_envelope_authorized_runtime_loop", True)),
            ("bounded envelope authorized arbitrary runtime", set_field("selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity", True)),
            ("self-recursive-growth-boundary created before review", set_field("self_recursive_growth_boundary_created_before_review", True)),
            ("self-recursive growth created", set_field("self_recursive_growth_created", True)),
            ("runtime daemon created", set_field("runtime_daemon_created", True)),
            ("runtime loop created", set_field("runtime_loop_created", True)),
            ("public API created", set_field("public_api_created", True)),
            ("participant-facing interface created", set_field("participant_facing_interface_created", True)),
            ("distributed network behavior created", set_field("distributed_network_behavior_created", True)),
            ("boundary treated as self-recursive growth", set_field("self_recursive_growth_boundary_treated_as_self_recursive_growth", True)),
            ("boundary treated as daemon", set_field("self_recursive_growth_boundary_treated_as_runtime_daemon", True)),
            ("boundary treated as loop", set_field("self_recursive_growth_boundary_treated_as_runtime_loop", True)),
            ("boundary treated as source transfer", set_field("self_recursive_growth_boundary_treated_as_source_transfer", True)),
            ("boundary treated as source receipt", set_field("self_recursive_growth_boundary_treated_as_source_receipt", True)),
            ("boundary treated as reception authorization", set_field("self_recursive_growth_boundary_treated_as_reception_authorization", True)),
            ("boundary treated as source", set_field("self_recursive_growth_boundary_treated_as_source", True)),
            ("boundary treated as authority", set_field("self_recursive_growth_boundary_treated_as_authority", True)),
            ("boundary treated as currentness", set_field("self_recursive_growth_boundary_treated_as_currentness", True)),
            ("boundary treated as deployment", set_field("self_recursive_growth_boundary_treated_as_deployment", True)),
            ("boundary treated as public release", set_field("self_recursive_growth_boundary_treated_as_public_release", True)),
            ("boundary treated as operation permission", set_field("self_recursive_growth_boundary_treated_as_operation_permission", True)),
            ("boundary treated as broader reusable permission", set_field("self_recursive_growth_boundary_treated_as_broader_reusable_permission", True)),
            ("boundary treated as follow-on work", set_field("self_recursive_growth_boundary_treated_as_follow_on_work", True)),
            ("source transfer occurred", set_field("source_transfer_occurred", True)),
            ("source receipt occurred", set_field("source_receipt_occurred", True)),
            ("reception authorization created", set_field("reception_authorization_created", True)),
            ("source created", set_field("source_created", True)),
            ("authority created", set_field("authority_created", True)),
            ("currentness created", set_field("currentness_created", True)),
            ("deployment created", set_field("deployment_created", True)),
            ("public release created", set_field("public_release_created", True)),
            ("operation permission created", set_field("operation_permission_created", True)),
            ("broader reusable permission created", set_field("broader_reusable_permission_created", True)),
            ("derivative reception authorized", set_field("derivative_reception_authorized", True)),
            ("vessel relation authorized", set_field("vessel_relation_authorized", True)),
            ("adoption created", set_field("adoption_created", True)),
            ("receiving-context governance created", set_field("receiving_context_governance_created", True)),
            ("publication flow created", set_field("publication_flow_created", True)),
            ("follow-on work authorized", set_field("follow_on_work_authorized", True)),
            ("artifact existence treated as authority", set_field("artifact_existence_treated_as_self_recursive_growth_boundary_authority", True)),
            ("artifact path treated as currentness", set_field("artifact_path_treated_as_currentness", True)),
            ("latest file posture treated as authority", set_field("latest_file_posture_treated_as_self_recursive_growth_boundary_authority", True)),
            ("repo-local availability treated as authority", set_field("repo_local_availability_treated_as_self_recursive_growth_boundary_authority", True)),
            ("hidden repo state used as content", set_field("hidden_repo_state_used_as_self_recursive_growth_boundary_content", True)),
            ("hidden repo state used as authority", set_field("hidden_repo_state_used_as_self_recursive_growth_boundary_authority", True)),
            ("selected basis not reference-shaped", set_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", set_field("raw_full_prior_artifact_body_returned", True)),
            ("predecessor failure repaired", set_field("predecessor_failure_repaired", True)),
            ("predecessor failure hidden", set_field("predecessor_failure_hidden", True)),
            ("predecessor failure claimed passed", set_field("predecessor_failure_claimed_passed", True)),
            ("runtime-hosting-boundary v1 failure repaired", set_field("selected_runtime_hosting_boundary_v1_failure_repaired", True)),
            ("runtime-hosting-boundary v1 failure hidden", set_field("selected_runtime_hosting_boundary_v1_failure_hidden", True)),
            ("runtime-hosting-boundary v1 failure claimed passed", set_field("selected_runtime_hosting_boundary_v1_failure_claimed_passed", True)),
            ("consumed request reopened", set_field("consumed_request_reopened", True)),
            ("authorization token reused", set_field("authorization_token_reused", True)),
        )

        for name, mutation in cases:
            with self.subTest(name=name):
                request = build_request()
                if mutation is not None:
                    mutation(request)
                result = resolve(request)
                self.assert_blocked_public_safe(result)

        with self.subTest(name="missing request"):
            self.assert_blocked_public_safe(
                resolver.resolve_post_self_continuation_self_recursive_growth_boundary(None)
            )
        with self.subTest(name="non-mapping request"):
            self.assert_blocked_public_safe(
                resolver.resolve_post_self_continuation_self_recursive_growth_boundary(["not", "mapping"])  # type: ignore[arg-type]
            )
        with self.subTest(name="required non-claim flipped"):
            request = build_request()
            request["declared_non_claims"]["self_recursive_growth_created"] = True
            self.assert_blocked_public_safe(resolve(request))

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        variants: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("remove declared_non_claims", remove_field("declared_non_claims")),
            ("empty declared_non_claims", set_field("declared_non_claims", {})),
            (
                "remove one required non-claim",
                lambda request: request["declared_non_claims"].pop("self_recursive_growth_created"),
            ),
            (
                "non-bool string non-claim",
                lambda request: request["declared_non_claims"].update({"runtime_daemon_created": "false"}),
            ),
            (
                "none non-claim",
                lambda request: request["declared_non_claims"].update({"runtime_loop_created": None}),
            ),
        )
        for name, mutation in variants:
            with self.subTest(name=name):
                request = build_request()
                mutation(request)
                result = resolve(request)
                self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
                self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolve(build_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope(result)

        custom_request = build_request(
            self_recursive_growth_boundary_scope=list(
                resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_BOUNDARY_SCOPE
            )
        )
        custom_result = resolve(custom_request)
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope(custom_result)

    def test_raw_hidden_hostile_content_is_contained_without_mutating_input(self) -> None:
        request = build_request()
        for index, section in enumerate(BASIS_SECTION_NAMES):
            basis = request.setdefault(section, {})
            self.assertIsInstance(basis, dict)
            for key in SENSITIVE_KEYS:
                basis[key] = SENTINELS[index % len(SENTINELS)]
        before = copy.deepcopy(request)
        result = resolve(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, before)
        self.assert_no_sentinels(result)
        self.assert_official_scope(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_boundary_posture(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(build_request()), encoding="utf-8")
            result = resolver.resolve_post_self_continuation_self_recursive_growth_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(
                metadata(result)["post_self_continuation_self_recursive_growth_boundary_version"],
                "0.1.0",
            )
            self.assertEqual(metadata(result)["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_post_self_continuation_self_recursive_growth_boundary_from_path(
                malformed_path
            )
            self.assert_blocked_public_safe(malformed)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_self_continuation_self_recursive_growth_boundary_from_path(
                array_path
            )
            self.assert_blocked_public_safe(array_result)

            missing_result = resolver.resolve_post_self_continuation_self_recursive_growth_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assert_blocked_public_safe(missing_result)

            output_root = tmp_path / "post_self_continuation_self_recursive_growth_boundary"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_post_self_continuation_self_recursive_growth_boundary_result(
                    result
                )
                second = resolver.write_post_self_continuation_self_recursive_growth_boundary_result(
                    result
                )

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            written = first.as_posix()
            self.assertIn("post_self_continuation_self_recursive_growth_boundary", written)
            for fragment in FORBIDDEN_WRITE_FRAGMENTS:
                self.assertNotIn(fragment, written)

    def test_non_mutation_of_request_and_selected_basis(self) -> None:
        request = build_request()
        before = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, before)
        for section in BASIS_SECTION_NAMES:
            self.assertEqual(request[section], before[section], section)
        self.assertEqual(request["declared_non_claims"], before["declared_non_claims"])
        self.assertEqual(
            request["self_recursive_growth_boundary_scope"],
            before["self_recursive_growth_boundary_scope"],
        )
        for section in (
            "self_recursive_growth_boundary_spec_only_posture",
            "one_future_self_recursive_growth_review_posture",
            "self_continuation_basis_preserved_posture",
            "self_continuation_not_self_recursive_growth_posture",
            "bounded_self_continuation_envelope_not_self_recursive_growth_posture",
        ):
            self.assertEqual(request[section], before[section], section)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve(build_request())
        result_summary = resolver.build_post_self_continuation_self_recursive_growth_boundary_summary(
            result
        )

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertTrue(
            result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"][
                "basis_declared"
            ]
        )
        self.assertIs(statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement(result)["consumed_request_token_remains_closed"], True)
        self.assertIs(statement(result)["authorization_token_reuse_blocked"], True)
        self.assertIs(result_summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(result_summary["consumed_request_token_remains_closed"], True)
        self.assertIs(result_summary["authorization_token_reuse_blocked"], True)
        for key in (
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
        ):
            self.assertIs(non_claims(result)[key], False, key)


if __name__ == "__main__":
    unittest.main()
