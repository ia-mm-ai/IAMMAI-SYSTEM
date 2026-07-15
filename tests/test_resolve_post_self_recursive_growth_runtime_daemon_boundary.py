"""Executable tests for the post-self-recursive-growth runtime-daemon boundary.

This suite is bounded to runtime-daemon-boundary posture only. Self-recursive
growth and self-recursive-growth-boundary are upstream basis, and
runtime-hosting-boundary v1 remains preserved predecessor failure lineage.
These tests do not create runtime daemon, runtime loop, public API,
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

import resolve_post_self_recursive_growth_runtime_daemon_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon_boundary"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_self_continuation_self_recursive_growth",
    "post_self_continuation_self_recursive_growth_boundary",
    "post_continuation_self_continuation",
    "post_continuation_self_continuation_boundary",
    "post_reusable_runtime_permission_continuation",
    "post_ongoing_runtime_reusable_runtime_permission",
    "post_runtime_hosting_ongoing_runtime",
    "post_successor_runtime_step_runtime_hosting",
    "runtime-daemon",
    "runtime-loop",
    "public-api",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

FORBIDDEN_WRITE_FRAGMENTS = (
    "post_self_continuation_self_recursive_growth/",
    "post_self_continuation_self_recursive_growth_boundary/",
    "post_continuation_self_continuation/",
    "post_continuation_self_continuation_boundary/",
    "post_reusable_runtime_permission_continuation/",
    "post_reusable_runtime_permission_continuation_boundary/",
    "post_ongoing_runtime_reusable_runtime_permission/",
    "post_ongoing_runtime_reusable_runtime_permission_boundary/",
    "post_runtime_hosting_ongoing_runtime/",
    "post_runtime_hosting_ongoing_runtime_boundary/",
    "post_successor_runtime_step_runtime_hosting/",
    "post_successor_runtime_step_runtime_hosting_boundary_v2/",
    "post_successor_runtime_step_runtime_hosting_boundary/",
    "post_minimal_runtime_successor_runtime_step/",
    "post_minimal_runtime_successor_runtime_step_boundary/",
    "post_portable_verification_minimal_runtime/",
    "post_portable_verification_runtime_boundary/",
    "post_portable_verification_runtime_readiness/",
    "post_portable_verification_runtime_readiness_boundary/",
    "portable_source_body_verification_final_completion/",
    "portable-verification/",
    "runtime-daemon/",
    "runtime-loop/",
    "public-api/",
    "deployment/",
    "public-release/",
    "source-transfer/",
    "source-receipt/",
    "reception/",
)

OFFICIAL_SCOPE_VALUES = (
    "RUNTIME_DAEMON_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_RUNTIME_DAEMON_REVIEW_DECLARED",
    "SELF_RECURSIVE_GROWTH_BASIS_PRESERVED",
    "SELF_RECURSIVE_GROWTH_NOT_RUNTIME_DAEMON",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_NOT_RUNTIME_DAEMON",
    "RUNTIME_DAEMON_BOUNDARY_NOT_RUNTIME_DAEMON",
    "RUNTIME_DAEMON_BOUNDARY_NOT_RUNTIME_LOOP",
    "RUNTIME_DAEMON_BOUNDARY_NOT_PUBLIC_API",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_DAEMON_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_DAEMON_BOUNDARY_INTENT_UNSUPPORTED",
    "SELF_RECURSIVE_GROWTH_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_NOT_RECORDED",
    "SELF_RECURSIVE_GROWTH_FAILED_CHECKS_PRESENT",
    "SELF_RECURSIVE_GROWTH_VERSION_NOT_0_1_0",
    "SELF_RECURSIVE_GROWTH_DID_NOT_RECORD_BOUNDED_SELF_RECURSIVE_GROWTH_POSTURE",
    "SELF_RECURSIVE_GROWTH_DID_NOT_RECORD_BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE",
    "SELF_RECURSIVE_GROWTH_ALREADY_CREATED_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_ALREADY_CREATED_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_ALREADY_CREATED_PUBLIC_API",
    "SELF_RECURSIVE_GROWTH_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "SELF_RECURSIVE_GROWTH_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_API",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_RECURSIVE_GROWTH_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_TREATED_AS_RUNTIME_DAEMON",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_RUNTIME_DAEMON",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_RUNTIME_LOOP",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_PUBLIC_API",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "RUNTIME_DAEMON_BOUNDARY_CREATED_BEFORE_REVIEW",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_RUNTIME_DAEMON",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_PUBLIC_API",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_SOURCE",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_AUTHORITY",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_CURRENTNESS",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "RUNTIME_DAEMON_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_DAEMON_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_DAEMON_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_DAEMON_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_DAEMON_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_DAEMON_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_self_recursive_growth_runtime_daemon_boundary_metadata",
    "declared_runtime_daemon_boundary_question",
    "selected_self_recursive_growth_basis",
    "selected_self_recursive_growth_terminal_summary_basis",
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_continuation_basis",
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
    "runtime_daemon_boundary_spec_only_posture",
    "one_future_runtime_daemon_review_posture",
    "self_recursive_growth_basis_preserved_posture",
    "self_recursive_growth_not_runtime_daemon_posture",
    "bounded_self_recursive_growth_envelope_not_runtime_daemon_posture",
    "runtime_daemon_boundary_not_runtime_daemon_posture",
    "runtime_daemon_boundary_not_runtime_loop_posture",
    "runtime_daemon_boundary_not_public_api_posture",
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
    "repo_local_availability_not_runtime_daemon_boundary_authority_posture",
    "artifact_existence_not_runtime_daemon_boundary_authority_posture",
    "latest_file_posture_not_runtime_daemon_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "runtime_daemon_boundary_scope",
    "runtime_daemon_boundary_checks",
    "runtime_daemon_boundary_statement",
    "runtime_daemon_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_self_recursive_growth_runtime_daemon_boundary_summary",
)

SELECTED_BASIS_SECTIONS = (
    "selected_self_recursive_growth_basis",
    "selected_self_recursive_growth_terminal_summary_basis",
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_continuation_basis",
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

POSTURE_SECTIONS = (
    "runtime_daemon_boundary_spec_only_posture",
    "one_future_runtime_daemon_review_posture",
    "self_recursive_growth_basis_preserved_posture",
    "self_recursive_growth_not_runtime_daemon_posture",
    "bounded_self_recursive_growth_envelope_not_runtime_daemon_posture",
    "runtime_daemon_boundary_not_runtime_daemon_posture",
    "runtime_daemon_boundary_not_runtime_loop_posture",
    "runtime_daemon_boundary_not_public_api_posture",
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
    "repo_local_availability_not_runtime_daemon_boundary_authority_posture",
    "artifact_existence_not_runtime_daemon_boundary_authority_posture",
    "latest_file_posture_not_runtime_daemon_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

EXPECTED_SUCCESS_CHECK_NAMES = (
    "runtime-daemon-boundary question declared",
    "runtime-daemon-boundary intent supported",
    "runtime-daemon-boundary scope supported",
    "self-recursive-growth basis declared",
    "self-recursive-growth terminal summary basis declared",
    "self-recursive-growth outcome recorded",
    "self-recursive-growth version 0.1.0",
    "self-recursive-growth failed checks zero",
    "self-recursive-growth recorded bounded self-recursive-growth posture",
    "self-recursive-growth recorded bounded self-recursive-growth envelope",
    "self-recursive-growth canonicalized result-level non-claims",
    "self-recursive-growth terminal summary states runtime daemon not created",
    "self-recursive-growth terminal summary states no runtime daemon selected",
    "self-recursive-growth terminal summary requires separate future review",
    "selected_self_recursive_growth_boundary_basis declared",
    "selected_self_recursive_growth_boundary_basis outcome recorded",
    "selected_self_recursive_growth_boundary_basis version 0.1.0",
    "selected_self_recursive_growth_boundary_basis failed checks zero",
    "selected_self_continuation_basis declared",
    "selected_continuation_basis declared",
    "selected_continuation_boundary_basis declared",
    "selected_reusable_runtime_permission_basis declared",
    "selected_reusable_runtime_permission_boundary_basis declared",
    "selected_ongoing_runtime_basis declared",
    "selected_runtime_hosting_basis declared",
    "selected_runtime_hosting_boundary_v2_basis declared",
    "runtime-hosting-boundary v1 failure lineage basis declared",
    "selected_successor_runtime_step_basis declared",
    "selected_minimal_runtime_basis declared",
    "selected_runtime_boundary_basis declared",
    "selected_runtime_readiness_basis declared",
    "selected_portable_verification_final_completion_basis declared",
    "post-portable currentness surface basis declared",
    "post-portable currentness surface states checkability is not continuation",
    "post-portable currentness surface does not authorize next work",
    "predecessor failure evidence remains visible and unrepaired",
    "official enum scope strings not redacted",
    "hostile raw body content contained",
)

SAFETY_TRUE_FIELDS = (
    "self_recursive_growth_not_runtime_daemon",
    "bounded_self_recursive_growth_envelope_not_runtime_daemon",
    "runtime_daemon_boundary_not_runtime_daemon",
    "runtime_daemon_boundary_not_runtime_loop",
    "runtime_daemon_boundary_not_public_api",
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
    "repo_local_availability_not_runtime_daemon_boundary_authority",
    "artifact_existence_not_runtime_daemon_boundary_authority",
    "latest_file_posture_not_runtime_daemon_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SAFETY_FALSE_NON_CLAIMS = (
    "runtime_daemon_created",
    "runtime_loop_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "runtime_daemon_boundary_treated_as_runtime_daemon",
    "self_recursive_growth_treated_as_runtime_daemon",
    "bounded_self_recursive_growth_envelope_treated_as_runtime_daemon",
    "source_created",
    "authority_created",
    "currentness_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "follow_on_work_authorized",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

SENSITIVE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_daemon_boundary_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "runtime_daemon_boundary_body",
    "runtime_daemon_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

SENTINELS = (
    "RAW_RUNTIME_DAEMON_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _valid_request() -> dict[str, Any]:
    return resolver.build_declared_post_self_recursive_growth_runtime_daemon_boundary_request()


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("runtime_daemon_boundary_checks")
    return checks if isinstance(checks, list) else []


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("runtime_daemon_boundary_statement")
    return statement if isinstance(statement, Mapping) else {}


def _non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return resolver.build_post_self_recursive_growth_runtime_daemon_boundary_summary(result)


def _serialized(result: Mapping[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def _mutate_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[field] = value

    return mutate


def _remove_field(field: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.pop(field, None)

    return mutate


def _mutate_basis(section: str, key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        basis = request.setdefault(section, {})
        if not isinstance(basis, dict):
            basis = {}
            request[section] = basis
        basis[key] = value

    return mutate


def _mutate_terminal_summary(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    return _mutate_basis("selected_self_recursive_growth_terminal_summary_basis", key, value)


def _remove_declared_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


class PostSelfRecursiveGrowthRuntimeDaemonBoundaryResolverTests(unittest.TestCase):
    """Bounded runtime-daemon-boundary resolver tests."""

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        for check in _checks(result):
            for code_key in ("block_code", "failure_code"):
                code = check.get(code_key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans(self, result: Mapping[str, Any]) -> None:
        for section_name in (
            "runtime_daemon_boundary_statement",
            "runtime_daemon_boundary_non_meaning",
            "non_claims",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, Mapping)
            for key, value in section.items():
                with self.subTest(section=section_name, key=key):
                    self.assertIs(type(value), bool)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = _non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, non_claims)
                self.assertIs(non_claims[key], False)
                self.assertIs(type(non_claims[key]), bool)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _serialized(result)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("runtime_daemon_boundary_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-runtime-daemon-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_RUNTIME_DAEMON_BOUNDARY_SCOPE:
            self.assertIn(value, scope)

    def assert_safe_boundary_posture(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        for key in SAFETY_TRUE_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)
        non_claims = _non_claims(result)
        for key in SAFETY_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)

    def assert_blocked_safely(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIsNotNone(block.get("block_code"))
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assertTrue(any(check.get("passed") is False for check in _checks(result)))
        self.assert_public_codes(result)
        self.assert_generated_booleans(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_boundary_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_self_recursive_growth_runtime_daemon_boundary",
            "resolve_post_self_recursive_growth_runtime_daemon_boundary_from_path",
            "write_post_self_recursive_growth_runtime_daemon_boundary_result",
            "build_post_self_recursive_growth_runtime_daemon_boundary_summary",
            "build_declared_post_self_recursive_growth_runtime_daemon_boundary_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)
            self.assertTrue(callable(getattr(resolver, name)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_RUNTIME_DAEMON_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_self_recursive_growth_runtime_daemon_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_RUNTIME_DAEMON_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )

        output_root = str(resolver.OUTPUT_ROOT).replace("\\", "/")
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX), output_root)
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)

        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = _valid_request()
        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
        summary = _summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["runtime_daemon_boundary_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        check_names = {check.get("check_name") for check in _checks(result)}
        for check_name in EXPECTED_SUCCESS_CHECK_NAMES:
            self.assertIn(check_name, check_names)

        statement = _statement(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)
                self.assertIs(type(statement.get(key)), bool)

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_generated_booleans(result)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_safe_boundary_posture(result)

    def test_critical_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        clean_request = _valid_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped_non_claim=key):
                request = copy.deepcopy(clean_request)
                request["declared_non_claims"][key] = True
                result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
                self.assert_blocked_safely(result)
                self.assertIs(result["non_claims"][key], False)
                self.assertNotEqual(result["non_claims"][key], True)
                self.assertNotIn(f'"{key}": true', _serialized(result))

    def test_representative_blocking_behavior(self) -> None:
        direct_cases: tuple[tuple[str, Any], ...] = (
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        )
        for label, request in direct_cases:
            with self.subTest(case=label):
                result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
                self.assert_blocked_safely(result)

        mutation_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            (
                "explicit block intent",
                _mutate_field(
                    "runtime_daemon_boundary_intent",
                    "BLOCK_POST_SELF_RECURSIVE_GROWTH_RUNTIME_DAEMON_BOUNDARY",
                ),
            ),
            ("unsupported intent", _mutate_field("runtime_daemon_boundary_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", _mutate_field("runtime_daemon_boundary_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing self-recursive-growth basis", _remove_field("selected_self_recursive_growth_basis")),
            (
                "self-recursive-growth not recorded",
                _mutate_basis("selected_self_recursive_growth_basis", "outcome", "NOT_RECORDED"),
            ),
            (
                "self-recursive-growth failed checks present",
                _mutate_basis("selected_self_recursive_growth_basis", "failed_check_count", 1),
            ),
            (
                "self-recursive-growth version not 0.1.0",
                _mutate_basis("selected_self_recursive_growth_basis", "result_version", "9.9.9"),
            ),
            (
                "self-recursive-growth did not record bounded posture",
                _mutate_field("selected_self_recursive_growth_bounded_posture_recorded", False),
            ),
            (
                "self-recursive-growth did not record bounded envelope",
                _mutate_field(
                    "selected_self_recursive_growth_bounded_self_recursive_growth_envelope_recorded",
                    False,
                ),
            ),
            (
                "self-recursive-growth terminal summary missing runtime daemon not-created statement",
                _mutate_terminal_summary("states_runtime_daemon_not_created", False),
            ),
            (
                "self-recursive-growth terminal summary missing no runtime daemon selected statement",
                _mutate_terminal_summary("states_no_runtime_daemon_selected", False),
            ),
            (
                "self-recursive-growth terminal summary missing separate future review",
                _mutate_terminal_summary("requires_separate_future_review", False),
            ),
            (
                "self-recursive-growth already created runtime daemon",
                _mutate_field("selected_self_recursive_growth_already_created_runtime_daemon", True),
            ),
            (
                "self-recursive-growth already created runtime loop",
                _mutate_field("selected_self_recursive_growth_already_created_runtime_loop", True),
            ),
            (
                "self-recursive-growth already created public API",
                _mutate_field("selected_self_recursive_growth_already_created_public_api", True),
            ),
            (
                "self-recursive-growth already created participant-facing interface",
                _mutate_field(
                    "selected_self_recursive_growth_already_created_participant_facing_interface",
                    True,
                ),
            ),
            (
                "self-recursive-growth already created distributed network behavior",
                _mutate_field(
                    "selected_self_recursive_growth_already_created_distributed_network_behavior",
                    True,
                ),
            ),
            (
                "self-recursive-growth treated as runtime daemon",
                _mutate_field("selected_self_recursive_growth_treated_as_runtime_daemon", True),
            ),
            (
                "self-recursive-growth treated as runtime loop",
                _mutate_field("selected_self_recursive_growth_treated_as_runtime_loop", True),
            ),
            (
                "self-recursive-growth treated as public API",
                _mutate_field("selected_self_recursive_growth_treated_as_public_api", True),
            ),
            (
                "self-recursive-growth treated as participant-facing interface",
                _mutate_field(
                    "selected_self_recursive_growth_treated_as_participant_facing_interface",
                    True,
                ),
            ),
            (
                "self-recursive-growth treated as distributed network behavior",
                _mutate_field(
                    "selected_self_recursive_growth_treated_as_distributed_network_behavior",
                    True,
                ),
            ),
            (
                "self-recursive-growth authorized future work",
                _mutate_field("selected_self_recursive_growth_authorized_future_work", True),
            ),
            (
                "bounded self-recursive-growth envelope treated as runtime daemon",
                _mutate_field("selected_bounded_self_recursive_growth_envelope_treated_as_runtime_daemon", True),
            ),
            (
                "bounded self-recursive-growth envelope authorized runtime daemon",
                _mutate_field("selected_bounded_self_recursive_growth_envelope_authorized_runtime_daemon", True),
            ),
            (
                "bounded self-recursive-growth envelope authorized runtime loop",
                _mutate_field("selected_bounded_self_recursive_growth_envelope_authorized_runtime_loop", True),
            ),
            (
                "bounded self-recursive-growth envelope authorized public API",
                _mutate_field("selected_bounded_self_recursive_growth_envelope_authorized_public_api", True),
            ),
            (
                "bounded self-recursive-growth envelope authorized participant-facing interface",
                _mutate_field(
                    "selected_bounded_self_recursive_growth_envelope_authorized_participant_facing_interface",
                    True,
                ),
            ),
            (
                "bounded self-recursive-growth envelope authorized distributed network behavior",
                _mutate_field(
                    "selected_bounded_self_recursive_growth_envelope_authorized_distributed_network_behavior",
                    True,
                ),
            ),
            (
                "bounded self-recursive-growth envelope authorized arbitrary runtime activity",
                _mutate_field(
                    "selected_bounded_self_recursive_growth_envelope_authorized_arbitrary_runtime_activity",
                    True,
                ),
            ),
            (
                "runtime-daemon-boundary created before review",
                _mutate_field("runtime_daemon_boundary_created_before_review", True),
            ),
            ("runtime daemon created", _mutate_field("runtime_daemon_created", True)),
            ("runtime loop created", _mutate_field("runtime_loop_created", True)),
            ("public API created", _mutate_field("public_api_created", True)),
            (
                "participant-facing interface created",
                _mutate_field("participant_facing_interface_created", True),
            ),
            (
                "distributed network behavior created",
                _mutate_field("distributed_network_behavior_created", True),
            ),
            (
                "runtime-daemon-boundary treated as runtime daemon",
                _mutate_field("runtime_daemon_boundary_treated_as_runtime_daemon", True),
            ),
            (
                "runtime-daemon-boundary treated as runtime loop",
                _mutate_field("runtime_daemon_boundary_treated_as_runtime_loop", True),
            ),
            (
                "runtime-daemon-boundary treated as public API",
                _mutate_field("runtime_daemon_boundary_treated_as_public_api", True),
            ),
            (
                "runtime-daemon-boundary treated as source transfer",
                _mutate_field("runtime_daemon_boundary_treated_as_source_transfer", True),
            ),
            (
                "runtime-daemon-boundary treated as source receipt",
                _mutate_field("runtime_daemon_boundary_treated_as_source_receipt", True),
            ),
            (
                "runtime-daemon-boundary treated as reception authorization",
                _mutate_field("runtime_daemon_boundary_treated_as_reception_authorization", True),
            ),
            ("runtime-daemon-boundary treated as source", _mutate_field("runtime_daemon_boundary_treated_as_source", True)),
            (
                "runtime-daemon-boundary treated as authority",
                _mutate_field("runtime_daemon_boundary_treated_as_authority", True),
            ),
            (
                "runtime-daemon-boundary treated as currentness",
                _mutate_field("runtime_daemon_boundary_treated_as_currentness", True),
            ),
            (
                "runtime-daemon-boundary treated as deployment",
                _mutate_field("runtime_daemon_boundary_treated_as_deployment", True),
            ),
            (
                "runtime-daemon-boundary treated as public release",
                _mutate_field("runtime_daemon_boundary_treated_as_public_release", True),
            ),
            (
                "runtime-daemon-boundary treated as operation permission",
                _mutate_field("runtime_daemon_boundary_treated_as_operation_permission", True),
            ),
            (
                "runtime-daemon-boundary treated as broader reusable permission",
                _mutate_field("runtime_daemon_boundary_treated_as_broader_reusable_permission", True),
            ),
            (
                "runtime-daemon-boundary treated as follow-on work",
                _mutate_field("runtime_daemon_boundary_treated_as_follow_on_work", True),
            ),
            ("source transfer occurred", _mutate_field("source_transfer_occurred", True)),
            ("source receipt occurred", _mutate_field("source_receipt_occurred", True)),
            ("reception authorization created", _mutate_field("reception_authorization_created", True)),
            ("source created", _mutate_field("source_created", True)),
            ("authority created", _mutate_field("authority_created", True)),
            ("currentness created", _mutate_field("currentness_created", True)),
            ("deployment created", _mutate_field("deployment_created", True)),
            ("public release created", _mutate_field("public_release_created", True)),
            ("operation permission created", _mutate_field("operation_permission_created", True)),
            ("broader reusable permission created", _mutate_field("broader_reusable_permission_created", True)),
            ("derivative reception authorized", _mutate_field("derivative_reception_authorized", True)),
            ("vessel relation authorized", _mutate_field("vessel_relation_authorized", True)),
            ("adoption created", _mutate_field("adoption_created", True)),
            ("receiving-context governance created", _mutate_field("receiving_context_governance_created", True)),
            ("publication flow created", _mutate_field("publication_flow_created", True)),
            ("follow-on work authorized", _mutate_field("follow_on_work_authorized", True)),
            (
                "artifact existence treated as runtime-daemon-boundary authority",
                _mutate_field("artifact_existence_treated_as_runtime_daemon_boundary_authority", True),
            ),
            ("artifact path treated as currentness", _mutate_field("artifact_path_treated_as_currentness", True)),
            (
                "latest file posture treated as runtime-daemon-boundary authority",
                _mutate_field("latest_file_posture_treated_as_runtime_daemon_boundary_authority", True),
            ),
            (
                "repo-local availability treated as runtime-daemon-boundary authority",
                _mutate_field("repo_local_availability_treated_as_runtime_daemon_boundary_authority", True),
            ),
            (
                "hidden repo state used as runtime-daemon-boundary content",
                _mutate_field("hidden_repo_state_used_as_runtime_daemon_boundary_content", True),
            ),
            (
                "hidden repo state used as runtime-daemon-boundary authority",
                _mutate_field("hidden_repo_state_used_as_runtime_daemon_boundary_authority", True),
            ),
            ("selected basis not reference-shaped", _mutate_field("selected_basis_not_reference_shaped", True)),
            ("raw full prior artifact body returned", _mutate_field("raw_full_prior_artifact_body_returned", True)),
            ("predecessor failure repaired", _mutate_field("predecessor_failure_repaired", True)),
            ("predecessor failure hidden", _mutate_field("predecessor_failure_hidden", True)),
            ("predecessor failure claimed passed", _mutate_field("predecessor_failure_claimed_passed", True)),
            ("consumed request reopened", _mutate_field("consumed_request_reopened", True)),
            ("authorization token reused", _mutate_field("authorization_token_reused", True)),
            (
                "required non-claim missing",
                _remove_declared_non_claim("runtime_daemon_created"),
            ),
        )

        for label, mutate in mutation_cases:
            with self.subTest(case=label):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
                self.assert_blocked_safely(result)

    def test_missing_or_incomplete_declared_non_claims_still_emit_canonical_false(self) -> None:
        variants: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("remove declared_non_claims", _remove_field("declared_non_claims")),
            ("empty declared_non_claims", _mutate_field("declared_non_claims", {})),
            (
                "remove one required non-claim",
                _remove_declared_non_claim("runtime_daemon_created"),
            ),
            (
                "required non-claim is string",
                lambda request: request["declared_non_claims"].__setitem__("runtime_daemon_created", "false"),
            ),
            (
                "required non-claim is none",
                lambda request: request["declared_non_claims"].__setitem__("runtime_daemon_created", None),
            ),
        )

        for label, mutate in variants:
            with self.subTest(case=label):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
                self.assertIn(
                    result["outcome"],
                    (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                )
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)
                self.assert_generated_booleans(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(_valid_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)

        request = resolver.build_declared_post_self_recursive_growth_runtime_daemon_boundary_request(
            runtime_daemon_boundary_scope=list(resolver.SUPPORTED_RUNTIME_DAEMON_BOUNDARY_SCOPE)
        )
        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)

    def test_raw_and_hidden_hostile_content_is_contained_without_mutation(self) -> None:
        request = _valid_request()
        for section_name in SELECTED_BASIS_SECTIONS:
            section = request.setdefault(section_name, {})
            self.assertIsInstance(section, dict)
            for index, key in enumerate(SENSITIVE_KEYS):
                section[key] = SENTINELS[index % len(SENTINELS)]
        original = copy.deepcopy(request)

        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_canonical_non_claims(result)
        self.assert_generated_booleans(result)
        self.assert_safe_boundary_posture(result)
        self.assertEqual(request, original)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "declared_request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary_from_path(request_path)
            summary = _summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            try:
                malformed = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary_from_path(
                    malformed_path
                )
                self.assert_blocked_safely(malformed)
            except resolver.PostSelfRecursiveGrowthRuntimeDaemonBoundaryError:
                pass

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary_from_path(
                array_path
            )
            self.assert_blocked_safely(array_result)

            missing_path = tmp_path / "missing.json"
            try:
                missing_result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary_from_path(
                    missing_path
                )
                self.assert_blocked_safely(missing_result)
            except resolver.PostSelfRecursiveGrowthRuntimeDaemonBoundaryError:
                pass

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_self_recursive_growth_runtime_daemon_boundary"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_post_self_recursive_growth_runtime_daemon_boundary_result(result)
                second_path = resolver.write_post_self_recursive_growth_runtime_daemon_boundary_result(result)

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(second_path.stem.endswith("_001"))
            self.assertIsInstance(json.loads(first_path.read_text(encoding="utf-8")), dict)
            self.assertIsInstance(json.loads(second_path.read_text(encoding="utf-8")), dict)

            normalized = str(first_path).replace("\\", "/")
            self.assertIn("post_self_recursive_growth_runtime_daemon_boundary", normalized)
            for fragment in FORBIDDEN_WRITE_FRAGMENTS:
                self.assertNotIn(fragment, normalized)

    def test_resolver_does_not_mutate_input_request_or_nested_basis(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)

        for field in ("declared_non_claims", "runtime_daemon_boundary_scope", *SELECTED_BASIS_SECTIONS, *POSTURE_SECTIONS):
            with self.subTest(field=field):
                self.assertEqual(request.get(field), original.get(field))

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_post_self_recursive_growth_runtime_daemon_boundary(_valid_request())
        summary = _summary(result)
        v1_basis = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]
        statement = _statement(result)
        non_claims = _non_claims(result)

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(v1_basis["preserved_as_failure_evidence"], True)
        self.assertIs(v1_basis["repaired"], False)
        self.assertIs(v1_basis["hidden"], False)
        self.assertIs(v1_basis["claimed_passed"], False)
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(non_claims["predecessor_failure_repaired"], False)
        self.assertIs(non_claims["predecessor_failure_hidden"], False)
        self.assertIs(non_claims["predecessor_failure_claimed_passed"], False)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        self.assertIs(non_claims["consumed_request_reopened"], False)
        self.assertIs(non_claims["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
