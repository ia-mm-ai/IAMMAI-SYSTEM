"""Executable tests for the post-runtime-daemon runtime-loop resolver.

This suite is bounded to runtime-loop posture only. Runtime-loop-boundary and
runtime daemon are upstream basis, runtime-daemon-boundary v1 remains preserved
over-strict failed test evidence, and runtime-hosting-boundary v1 remains
preserved predecessor failure lineage.

These tests do not create public API, participant-facing interface,
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

import resolve_post_runtime_daemon_runtime_loop as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_runtime_daemon_runtime_loop_boundary",
    "post_self_recursive_growth_runtime_daemon",
    "post_self_recursive_growth_runtime_daemon_boundary",
    "post_self_continuation_self_recursive_growth",
    "post_self_continuation_self_recursive_growth_boundary",
    "post_continuation_self_continuation",
    "post_continuation_self_continuation_boundary",
    "post_reusable_runtime_permission_continuation",
    "post_ongoing_runtime_reusable_runtime_permission",
    "post_runtime_hosting_ongoing_runtime",
    "post_successor_runtime_step_runtime_hosting",
    "public-api",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

FORBIDDEN_WRITE_FRAGMENTS = (
    "post_runtime_daemon_runtime_loop_boundary/",
    "post_self_recursive_growth_runtime_daemon/",
    "post_self_recursive_growth_runtime_daemon_boundary/",
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
    "final-completion-boundary/",
    "portable-verification/",
    "public-api/",
    "deployment/",
    "public-release/",
    "source-transfer/",
    "source-receipt/",
    "reception/",
)

OFFICIAL_SCOPE_VALUES = (
    "RUNTIME_LOOP_SPEC_ONLY",
    "ONE_BOUNDED_RUNTIME_LOOP_POSTURE_RECORDED",
    "RUNTIME_LOOP_BOUNDARY_BASIS_PRESERVED",
    "RUNTIME_DAEMON_BASIS_PRESERVED",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_PRESERVED",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_DECLARED",
    "RUNTIME_LOOP_NOT_PUBLIC_API",
    "RUNTIME_LOOP_NOT_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_LOOP_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_LOOP_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_LOOP_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_LOOP_QUESTION_UNDECLARED",
    "RUNTIME_LOOP_INTENT_UNSUPPORTED",
    "RUNTIME_LOOP_BOUNDARY_BASIS_MISSING",
    "RUNTIME_LOOP_BOUNDARY_NOT_RECORDED",
    "RUNTIME_LOOP_BOUNDARY_FAILED_CHECKS_PRESENT",
    "RUNTIME_LOOP_BOUNDARY_VERSION_NOT_0_1_0",
    "RUNTIME_LOOP_BOUNDARY_DID_NOT_DECLARE_FUTURE_RUNTIME_LOOP_REVIEW",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_PUBLIC_API",
    "RUNTIME_LOOP_BOUNDARY_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "RUNTIME_DAEMON_BASIS_MISSING",
    "RUNTIME_DAEMON_NOT_RECORDED",
    "RUNTIME_DAEMON_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_DAEMON_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_DAEMON_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_TREATED_AS_RUNTIME_LOOP_BEFORE_REVIEW",
    "BOUNDED_RUNTIME_DAEMON_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
    "RUNTIME_DAEMON_BOUNDARY_V1_FAILURE_HIDDEN_OR_REPAIRED_OR_CLAIMED_PASSED",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "RUNTIME_LOOP_RECORDED_BEFORE_REVIEW",
    "RUNTIME_LOOP_TREATED_AS_PUBLIC_API",
    "RUNTIME_LOOP_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_LOOP_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_LOOP_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_LOOP_TREATED_AS_SOURCE",
    "RUNTIME_LOOP_TREATED_AS_AUTHORITY",
    "RUNTIME_LOOP_TREATED_AS_CURRENTNESS",
    "RUNTIME_LOOP_TREATED_AS_DEPLOYMENT",
    "RUNTIME_LOOP_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_LOOP_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_LOOP_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "RUNTIME_LOOP_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_LOOP_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_LOOP_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_LOOP_SCOPE",
    "DECLARED_RUNTIME_LOOP_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_LOOP_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_runtime_daemon_runtime_loop_metadata",
    "declared_runtime_loop_question",
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_loop_boundary_terminal_summary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_terminal_summary_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_self_recursive_growth_basis",
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
    "runtime_loop_spec_only_posture",
    "one_bounded_runtime_loop_posture",
    "runtime_loop_boundary_basis_preserved_posture",
    "runtime_daemon_basis_preserved_posture",
    "bounded_runtime_daemon_envelope_preserved_posture",
    "bounded_runtime_loop_envelope_declared_posture",
    "runtime_loop_not_public_api_posture",
    "runtime_loop_not_participant_facing_interface_posture",
    "runtime_loop_not_distributed_network_behavior_posture",
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
    "repo_local_availability_not_runtime_loop_authority_posture",
    "artifact_existence_not_runtime_loop_authority_posture",
    "latest_file_posture_not_runtime_loop_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "runtime_loop_scope",
    "runtime_loop_checks",
    "runtime_loop_statement",
    "runtime_loop_non_meaning",
    "bounded_runtime_loop_envelope",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_runtime_daemon_runtime_loop_summary",
)

SELECTED_BASIS_SECTIONS = (
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_loop_boundary_terminal_summary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_terminal_summary_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_self_recursive_growth_basis",
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
    "runtime_loop_spec_only_posture",
    "one_bounded_runtime_loop_posture",
    "runtime_loop_boundary_basis_preserved_posture",
    "runtime_daemon_basis_preserved_posture",
    "bounded_runtime_daemon_envelope_preserved_posture",
    "bounded_runtime_loop_envelope_declared_posture",
    "runtime_loop_not_public_api_posture",
    "runtime_loop_not_participant_facing_interface_posture",
    "runtime_loop_not_distributed_network_behavior_posture",
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
    "repo_local_availability_not_runtime_loop_authority_posture",
    "artifact_existence_not_runtime_loop_authority_posture",
    "latest_file_posture_not_runtime_loop_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

STATEMENT_TRUE_FIELDS = (
    "runtime_loop_recorded",
    "bounded_runtime_loop_posture_recorded",
    "runtime_loop_boundary_basis_preserved",
    "runtime_daemon_basis_preserved",
    "bounded_runtime_daemon_envelope_preserved",
    "bounded_runtime_loop_envelope_declared",
    "runtime_loop_not_public_api",
    "runtime_loop_not_participant_facing_interface",
    "runtime_loop_not_distributed_network_behavior",
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
    "hidden_repo_state_not_used_as_runtime_loop_authority",
    "repo_local_availability_not_runtime_loop_authority",
    "artifact_existence_not_runtime_loop_authority",
    "latest_file_posture_not_runtime_loop_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SAFETY_TRUE_FIELDS = (
    "runtime_loop_not_public_api",
    "runtime_loop_not_participant_facing_interface",
    "runtime_loop_not_distributed_network_behavior",
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
    "hidden_repo_state_not_used_as_runtime_loop_authority",
    "repo_local_availability_not_runtime_loop_authority",
    "artifact_existence_not_runtime_loop_authority",
    "latest_file_posture_not_runtime_loop_authority",
    "official_enum_scope_strings_not_redacted",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SENSITIVE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_runtime_loop_body",
    "raw_bounded_runtime_loop_envelope_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "runtime_loop_body",
    "bounded_runtime_loop_envelope_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

SENTINELS = (
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RUNTIME_LOOP_ENVELOPE_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def _valid_request() -> dict[str, Any]:
    return resolver.build_declared_post_runtime_daemon_runtime_loop_request()


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("runtime_loop_checks")
    return checks if isinstance(checks, list) else []


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("runtime_loop_statement")
    return statement if isinstance(statement, Mapping) else {}


def _non_meaning(result: Mapping[str, Any]) -> Mapping[str, Any]:
    non_meaning = result.get("runtime_loop_non_meaning")
    return non_meaning if isinstance(non_meaning, Mapping) else {}


def _non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return resolver.build_post_runtime_daemon_runtime_loop_summary(result)


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


def _mutate_envelope(key: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        envelope = request.setdefault("requested_bounded_runtime_loop_envelope", {})
        if not isinstance(envelope, dict):
            envelope = {}
            request["requested_bounded_runtime_loop_envelope"] = envelope
        envelope[key] = value

    return mutate


def _remove_declared_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"].pop(key, None)

    return mutate


def _flip_declared_non_claim(key: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request["declared_non_claims"][key] = True

    return mutate


def _paths_to_key_true(value: Any, key: str, path: tuple[Any, ...] = ()) -> list[tuple[Any, ...]]:
    paths: list[tuple[Any, ...]] = []
    if isinstance(value, Mapping):
        for item_key, item_value in value.items():
            next_path = (*path, item_key)
            if item_key == key and item_value is True:
                paths.append(next_path)
            paths.extend(_paths_to_key_true(item_value, key, next_path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            paths.extend(_paths_to_key_true(item, key, (*path, index)))
    return paths


class RuntimeLoopResolverTests(unittest.TestCase):
    """Bounded runtime-loop resolver test surface."""

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
        for section_name in ("runtime_loop_statement", "runtime_loop_non_meaning", "non_claims"):
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

    def assert_no_raw_or_hidden_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _serialized(result)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("runtime_loop_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-runtime-loop-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_RUNTIME_LOOP_SCOPE:
            self.assertIn(value, scope)

    def assert_statement_has_no_illegal_true_posture(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        for key, value in statement.items():
            if value is True:
                self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            if key in statement:
                self.assertIsNot(statement[key], True)

    def assert_runtime_loop_non_meaning_safe(self, result: Mapping[str, Any]) -> None:
        for key, value in _non_meaning(result).items():
            with self.subTest(non_meaning=key):
                self.assertIs(value, False)

    def assert_safe_runtime_loop_posture(self, result: Mapping[str, Any]) -> None:
        statement = _statement(result)
        for key in SAFETY_TRUE_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)
        self.assert_statement_has_no_illegal_true_posture(result)
        self.assert_runtime_loop_non_meaning_safe(result)
        self.assert_canonical_non_claims(result)

    def assert_flipped_non_claim_not_final_posture(self, result: Mapping[str, Any], key: str) -> None:
        self.assertIs(result["non_claims"][key], False)
        self.assert_canonical_non_claims(result)
        self.assert_statement_has_no_illegal_true_posture(result)

        true_paths = _paths_to_key_true(result, key)
        for path in true_paths:
            with self.subTest(flipped_key=key, path=path):
                self.assertNotEqual(path[:1], ("non_claims",))
                self.assertNotEqual(path[:1], ("runtime_loop_statement",))
                self.assertIn(path[0], ("runtime_loop_checks", "block"))

    def assert_blocked_safely(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIsNotNone(block.get("block_code"))
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assertTrue(any(check.get("passed") is False for check in _checks(result)))
        self.assert_public_codes(result)
        self.assert_generated_booleans(result)
        self.assert_safe_runtime_loop_posture(result)

    def assert_envelope_is_bounded(self, result: Mapping[str, Any]) -> None:
        envelope = result.get("bounded_runtime_loop_envelope")
        self.assertIsInstance(envelope, Mapping)
        self.assertIn("one_bounded", str(envelope.get("envelope_name", "")))
        self.assertIs(envelope.get("arbitrary_runtime_activity_authorized"), False)
        self.assertIs(envelope.get("public_api_created"), False)
        self.assertIs(envelope.get("participant_facing_interface_created"), False)
        self.assertIs(envelope.get("distributed_network_behavior_created"), False)
        self.assertIs(envelope.get("follow_on_work_authorized"), False)
        fresh = envelope.get("fresh_admission_required_for")
        self.assertIsInstance(fresh, list)
        self.assertTrue(any("outside" in str(item) for item in fresh))
        denied = " ".join(str(item) for item in envelope.get("does_not_authorize", []))
        for phrase in (
            "public API",
            "participant-facing interface",
            "distributed network behavior",
            "source transfer",
            "source receipt",
            "reception authorization",
            "source",
            "authority",
            "currentness",
            "deployment",
            "public release",
            "operation permission",
            "broader reusable permission",
            "follow-on work",
        ):
            self.assertIn(phrase, denied)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_runtime_daemon_runtime_loop",
            "resolve_post_runtime_daemon_runtime_loop_from_path",
            "write_post_runtime_daemon_runtime_loop_result",
            "build_post_runtime_daemon_runtime_loop_summary",
            "build_declared_post_runtime_daemon_runtime_loop_request",
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
            "SUPPORTED_RUNTIME_LOOP_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_post_runtime_daemon_runtime_loop")
        self.assertEqual(resolver.SUPPORTED_RUNTIME_LOOP_SCOPE, resolver.SUPPORTED_SCOPE_VALUES)

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
        result = resolver.resolve_post_runtime_daemon_runtime_loop(request)
        summary = _summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["runtime_loop_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        statement = _statement(result)
        for key in STATEMENT_TRUE_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)
                self.assertIs(type(statement.get(key)), bool)

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_generated_booleans(result)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_safe_runtime_loop_posture(result)
        self.assert_envelope_is_bounded(result)

    def test_critical_non_claim_canonicalization_allows_validation_evidence_only(self) -> None:
        clean_request = _valid_request()
        required_named_cases = {
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "runtime_loop_treated_as_public_api",
            "runtime_loop_treated_as_participant_facing_interface",
            "runtime_loop_treated_as_distributed_network_behavior",
            "runtime_loop_treated_as_source",
            "runtime_loop_treated_as_authority",
            "runtime_loop_treated_as_currentness",
            "runtime_loop_boundary_treated_as_runtime_loop_without_review",
            "runtime_daemon_treated_as_runtime_loop_without_review",
            "bounded_runtime_daemon_envelope_treated_as_runtime_loop_without_review",
            "runtime_daemon_boundary_v1_failure_repaired",
            "runtime_daemon_boundary_v1_failure_hidden",
            "runtime_daemon_boundary_v1_failure_claimed_passed",
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(required_named_cases.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped_non_claim=key):
                request = copy.deepcopy(clean_request)
                request["declared_non_claims"][key] = True
                result = resolver.resolve_post_runtime_daemon_runtime_loop(request)
                self.assert_blocked_safely(result)
                self.assert_flipped_non_claim_not_final_posture(result, key)

    def test_representative_blocking_behavior(self) -> None:
        direct_cases: tuple[tuple[str, Any], ...] = (
            ("missing request", None),
            ("non-mapping request", ["not", "a", "mapping"]),
        )
        for label, request in direct_cases:
            with self.subTest(case=label):
                result = resolver.resolve_post_runtime_daemon_runtime_loop(request)
                self.assert_blocked_safely(result)

        mutation_cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", _mutate_field("runtime_loop_intent", "BLOCK_POST_RUNTIME_DAEMON_RUNTIME_LOOP")),
            ("unsupported intent", _mutate_field("runtime_loop_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", _mutate_field("runtime_loop_scope", ["UNSUPPORTED_SCOPE"])),
            ("missing runtime-loop-boundary basis", _remove_field("selected_runtime_loop_boundary_basis")),
            ("runtime-loop-boundary not recorded", _mutate_field("selected_runtime_loop_boundary_result_outcome", "NOT_RECORDED")),
            ("runtime-loop-boundary failed checks present", _mutate_field("selected_runtime_loop_boundary_failed_check_count", 1)),
            ("runtime-loop-boundary version not 0.1.0", _mutate_field("selected_runtime_loop_boundary_result_version", "9.9.9")),
            ("runtime-loop-boundary did not declare future runtime-loop review", _mutate_field("selected_runtime_loop_boundary_declared_future_review", False)),
            ("runtime-loop-boundary already created runtime loop", _mutate_field("selected_runtime_loop_boundary_already_created_runtime_loop", True)),
            ("runtime-loop-boundary already created public API", _mutate_field("selected_runtime_loop_boundary_already_created_public_api", True)),
            ("runtime-loop-boundary already created participant-facing interface", _mutate_field("selected_runtime_loop_boundary_already_created_participant_facing_interface", True)),
            ("runtime-loop-boundary already created distributed network behavior", _mutate_field("selected_runtime_loop_boundary_already_created_distributed_network_behavior", True)),
            ("runtime-loop-boundary treated boundary as runtime loop", _mutate_field("selected_runtime_loop_boundary_treated_as_runtime_loop", True)),
            ("runtime-loop-boundary treated boundary as public API", _mutate_field("selected_runtime_loop_boundary_treated_as_public_api", True)),
            ("runtime-loop-boundary treated boundary as distributed network behavior", _mutate_field("selected_runtime_loop_boundary_treated_as_distributed_network_behavior", True)),
            ("runtime-loop-boundary authorized future work", _mutate_field("selected_runtime_loop_boundary_authorized_future_work", True)),
            ("runtime-daemon basis missing", _remove_field("selected_runtime_daemon_basis")),
            ("runtime daemon not recorded", _mutate_field("selected_runtime_daemon_result_outcome", "NOT_RECORDED")),
            ("runtime daemon already created public API", _mutate_field("selected_runtime_daemon_already_created_public_api", True)),
            ("runtime daemon already created participant-facing interface", _mutate_field("selected_runtime_daemon_already_created_participant_facing_interface", True)),
            ("runtime daemon already created distributed network behavior", _mutate_field("selected_runtime_daemon_already_created_distributed_network_behavior", True)),
            ("bounded runtime-daemon envelope treated as runtime loop before review", _mutate_field("selected_bounded_runtime_daemon_envelope_treated_as_runtime_loop_before_review", True)),
            ("bounded runtime-daemon envelope authorized arbitrary runtime activity before review", _mutate_field("selected_bounded_runtime_daemon_envelope_authorized_arbitrary_runtime_activity_before_review", True)),
            ("runtime-daemon-boundary v1 failed test evidence hidden", _mutate_field("selected_runtime_daemon_boundary_v1_failure_hidden", True)),
            ("runtime-daemon-boundary v1 failed test evidence repaired", _mutate_field("selected_runtime_daemon_boundary_v1_failure_repaired", True)),
            ("runtime-daemon-boundary v1 failed test evidence claimed passed", _mutate_field("selected_runtime_daemon_boundary_v1_failure_claimed_passed", True)),
            ("runtime-hosting-boundary v1 failure repaired", _mutate_field("selected_runtime_hosting_boundary_v1_failure_repaired", True)),
            ("runtime-hosting-boundary v1 failure hidden", _mutate_field("selected_runtime_hosting_boundary_v1_failure_hidden", True)),
            ("runtime-hosting-boundary v1 failure claimed passed", _mutate_field("selected_runtime_hosting_boundary_v1_failure_claimed_passed", True)),
            ("runtime loop recorded before review", _mutate_field("runtime_loop_recorded_before_review", True)),
            ("runtime loop treated as public API", _mutate_field("runtime_loop_treated_as_public_api", True)),
            ("runtime loop treated as participant-facing interface", _mutate_field("runtime_loop_treated_as_participant_facing_interface", True)),
            ("runtime loop treated as distributed network behavior", _mutate_field("runtime_loop_treated_as_distributed_network_behavior", True)),
            ("runtime loop treated as source transfer", _mutate_field("runtime_loop_treated_as_source_transfer", True)),
            ("runtime loop treated as source receipt", _mutate_field("runtime_loop_treated_as_source_receipt", True)),
            ("runtime loop treated as reception authorization", _mutate_field("runtime_loop_treated_as_reception_authorization", True)),
            ("runtime loop treated as source", _mutate_field("runtime_loop_treated_as_source", True)),
            ("runtime loop treated as authority", _mutate_field("runtime_loop_treated_as_authority", True)),
            ("runtime loop treated as currentness", _mutate_field("runtime_loop_treated_as_currentness", True)),
            ("runtime loop treated as deployment", _mutate_field("runtime_loop_treated_as_deployment", True)),
            ("runtime loop treated as public release", _mutate_field("runtime_loop_treated_as_public_release", True)),
            ("runtime loop treated as operation permission", _mutate_field("runtime_loop_treated_as_operation_permission", True)),
            ("runtime loop treated as broader reusable permission", _mutate_field("runtime_loop_treated_as_broader_reusable_permission", True)),
            ("runtime loop treated as follow-on work", _mutate_field("runtime_loop_treated_as_follow_on_work", True)),
            ("public API created", _mutate_field("public_api_created", True)),
            ("participant-facing interface created", _mutate_field("participant_facing_interface_created", True)),
            ("distributed network behavior created", _mutate_field("distributed_network_behavior_created", True)),
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
            ("artifact existence treated as runtime-loop authority", _mutate_field("artifact_existence_treated_as_runtime_loop_authority", True)),
            ("artifact path treated as currentness", _mutate_field("artifact_path_treated_as_currentness", True)),
            ("latest file posture treated as runtime-loop authority", _mutate_field("latest_file_posture_treated_as_runtime_loop_authority", True)),
            ("repo-local availability treated as runtime-loop authority", _mutate_field("repo_local_availability_treated_as_runtime_loop_authority", True)),
            ("hidden repo state used as runtime-loop content", _mutate_field("hidden_repo_state_used_as_runtime_loop_content", True)),
            ("hidden repo state used as runtime-loop authority", _mutate_field("hidden_repo_state_used_as_runtime_loop_authority", True)),
            ("selected basis not reference-shaped", _mutate_field("reference_shaped_input_posture", False)),
            ("raw full prior artifact body returned", _mutate_field("raw_full_prior_artifact_body_returned", True)),
            ("predecessor failure evidence repaired", _mutate_field("predecessor_failure_repaired", True)),
            ("predecessor failure evidence hidden", _mutate_field("predecessor_failure_hidden", True)),
            ("predecessor failure evidence claimed passed", _mutate_field("predecessor_failure_claimed_passed", True)),
            ("consumed request reopened", _mutate_field("consumed_request_reopened", True)),
            ("authorization token reused", _mutate_field("authorization_token_reused", True)),
            ("bounded runtime-loop envelope authorized arbitrary runtime activity", _mutate_envelope("arbitrary_runtime_activity_authorized", True)),
            ("bounded runtime-loop envelope authorized public API", _mutate_envelope("public_api_created", True)),
            ("bounded runtime-loop envelope authorized participant-facing interface", _mutate_envelope("participant_facing_interface_created", True)),
            ("bounded runtime-loop envelope authorized distributed network behavior", _mutate_envelope("distributed_network_behavior_created", True)),
            ("bounded runtime-loop envelope authorized follow-on work", _mutate_envelope("follow_on_work_authorized", True)),
            ("required non-claim missing", _remove_declared_non_claim(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
            ("required non-claim flipped", _flip_declared_non_claim(resolver.REQUIRED_FALSE_NON_CLAIMS[1])),
        )

        for label, mutate in mutation_cases:
            with self.subTest(case=label):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_post_runtime_daemon_runtime_loop(request)
                self.assert_blocked_safely(result)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        variants: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("remove declared_non_claims", _remove_field("declared_non_claims")),
            ("empty declared_non_claims", _mutate_field("declared_non_claims", {})),
            ("remove one required non-claim", _remove_declared_non_claim(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
            ("non-bool required non-claim", _mutate_basis("declared_non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false")),
            ("none required non-claim", _mutate_basis("declared_non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0], None)),
        )
        for label, mutate in variants:
            with self.subTest(case=label):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_post_runtime_daemon_runtime_loop(request)
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolver.resolve_post_runtime_daemon_runtime_loop(_valid_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)

        request = _valid_request()
        request["runtime_loop_scope"] = list(resolver.SUPPORTED_RUNTIME_LOOP_SCOPE)
        custom = resolver.resolve_post_runtime_daemon_runtime_loop(request)
        self.assertEqual(custom["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(custom)

    def test_raw_hidden_hostile_content_is_contained_without_mutating_request(self) -> None:
        request = _valid_request()
        for index, section in enumerate(SELECTED_BASIS_SECTIONS):
            basis = request.setdefault(section, {})
            self.assertIsInstance(basis, dict)
            for key in SENSITIVE_KEYS:
                basis[key] = SENTINELS[index % len(SENTINELS)]
        request_before_resolve = copy.deepcopy(request)

        result = resolver.resolve_post_runtime_daemon_runtime_loop(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_raw_or_hidden_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_runtime_loop_posture(result)
        self.assertEqual(request, request_before_resolve)

    def test_path_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_post_runtime_daemon_runtime_loop_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = _summary(result)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed = resolver.resolve_post_runtime_daemon_runtime_loop_from_path(malformed_path)
            self.assert_blocked_safely(malformed)

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_runtime_daemon_runtime_loop_from_path(array_path)
            self.assert_blocked_safely(array_result)

            missing_result = resolver.resolve_post_runtime_daemon_runtime_loop_from_path(
                root / "missing.json"
            )
            self.assert_blocked_safely(missing_result)

            redirected_root = (
                root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_post_runtime_daemon_runtime_loop"
            )
            with mock.patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first = resolver.write_post_runtime_daemon_runtime_loop_result(result)
                second = resolver.write_post_runtime_daemon_runtime_loop_result(result)

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertTrue(first.parent.exists())
            first_text = str(first).replace("\\", "/")
            self.assertIn("post_runtime_daemon_runtime_loop", first_text)
            for fragment in FORBIDDEN_WRITE_FRAGMENTS:
                self.assertNotIn(fragment, first_text)

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        nested_originals = {
            "declared_non_claims": copy.deepcopy(request["declared_non_claims"]),
            "runtime_loop_scope": copy.deepcopy(request["runtime_loop_scope"]),
            "requested_bounded_runtime_loop_envelope": copy.deepcopy(
                request["requested_bounded_runtime_loop_envelope"]
            ),
        }
        for section in SELECTED_BASIS_SECTIONS + POSTURE_SECTIONS:
            nested_originals[section] = copy.deepcopy(request[section])

        resolver.resolve_post_runtime_daemon_runtime_loop(request)

        self.assertEqual(request, original)
        for section, expected in nested_originals.items():
            self.assertEqual(request[section], expected)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_post_runtime_daemon_runtime_loop(_valid_request())
        summary = _summary(result)
        statement = _statement(result)
        non_claims = _non_claims(result)

        boundary_v1 = result["selected_runtime_daemon_boundary_v1_failure_lineage_basis"]
        self.assertTrue(boundary_v1["failure_lineage_preserved"])
        self.assertIs(boundary_v1["repaired"], False)
        self.assertIs(boundary_v1["hidden"], False)
        self.assertIs(boundary_v1["claimed_passed"], False)

        hosting_v1 = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]
        self.assertTrue(hosting_v1["failure_lineage_preserved"])
        self.assertIs(hosting_v1["repaired"], False)
        self.assertIs(hosting_v1["hidden"], False)
        self.assertIs(hosting_v1["claimed_passed"], False)

        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)

        for key in (
            "runtime_daemon_boundary_v1_failure_repaired",
            "runtime_daemon_boundary_v1_failure_hidden",
            "runtime_daemon_boundary_v1_failure_claimed_passed",
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(non_claims[key], False)


if __name__ == "__main__":
    unittest.main()
