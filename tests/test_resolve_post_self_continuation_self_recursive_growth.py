"""Executable tests for the post-self-continuation self-recursive-growth resolver.

This suite is bounded to self-recursive-growth posture only. The
self-recursive-growth-boundary line is upstream basis, self-continuation remains
upstream bounded basis, and runtime-hosting-boundary v1 remains preserved
predecessor failure lineage. These tests do not create runtime daemon, runtime
loop, public API, participant-facing interface, distributed network behavior,
source transfer, source receipt, reception authorization, source, authority,
currentness, deployment, public release, operation permission, broader reusable
permission, adoption, receiving-context governance, publication flow, or
follow-on work.
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

import resolve_post_self_continuation_self_recursive_growth as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_self_continuation_self_recursive_growth"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
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
    "post_self_continuation_self_recursive_growth_boundary/",
    "post_continuation_self_continuation/",
    "post_continuation_self_continuation_boundary/",
    "post_reusable_runtime_permission_continuation/",
    "post_ongoing_runtime_reusable_runtime_permission/",
    "post_runtime_hosting_ongoing_runtime/",
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
    "SELF_RECURSIVE_GROWTH_SPEC_ONLY",
    "ONE_BOUNDED_SELF_RECURSIVE_GROWTH_POSTURE_RECORDED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_PRESERVED",
    "SELF_CONTINUATION_BASIS_PRESERVED",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_PRESERVED",
    "BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_DECLARED",
    "SELF_RECURSIVE_GROWTH_NOT_DAEMON",
    "SELF_RECURSIVE_GROWTH_NOT_LOOP",
    "SELF_RECURSIVE_GROWTH_NOT_PUBLIC_API",
    "SELF_RECURSIVE_GROWTH_NOT_PARTICIPANT_FACING_INTERFACE",
    "SELF_RECURSIVE_GROWTH_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SELF_RECURSIVE_GROWTH_QUESTION_UNDECLARED",
    "SELF_RECURSIVE_GROWTH_INTENT_UNSUPPORTED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_VERSION_NOT_0_1_0",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PUBLIC_API",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORIZED_FUTURE_WORK",
    "SELF_CONTINUATION_BASIS_MISSING",
    "SELF_CONTINUATION_NOT_RECORDED",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON",
    "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP",
    "SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API",
    "SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH_BEFORE_REVIEW",
    "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW",
    "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED",
    "SELF_RECURSIVE_GROWTH_CREATED_BEFORE_REVIEW",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_DAEMON",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_LOOP",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_API",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_TRANSFER",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_RECEIPT",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_AUTHORITY",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_CURRENTNESS",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_DEPLOYMENT",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_RELEASE",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_OPERATION_PERMISSION",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "SELF_RECURSIVE_GROWTH_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE",
    "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
    "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_self_continuation_self_recursive_growth_metadata",
    "declared_self_recursive_growth_question",
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_recursive_growth_boundary_terminal_summary_basis",
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
    "self_recursive_growth_spec_only_posture",
    "one_bounded_self_recursive_growth_posture",
    "self_recursive_growth_boundary_basis_preserved_posture",
    "self_continuation_basis_preserved_posture",
    "bounded_self_continuation_envelope_preserved_posture",
    "bounded_self_recursive_growth_envelope_declared_posture",
    "self_recursive_growth_not_daemon_posture",
    "self_recursive_growth_not_loop_posture",
    "self_recursive_growth_not_public_api_posture",
    "self_recursive_growth_not_participant_facing_interface_posture",
    "self_recursive_growth_not_distributed_network_behavior_posture",
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
    "repo_local_availability_not_self_recursive_growth_authority_posture",
    "artifact_existence_not_self_recursive_growth_authority_posture",
    "latest_file_posture_not_self_recursive_growth_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "self_recursive_growth_scope",
    "self_recursive_growth_checks",
    "self_recursive_growth_statement",
    "self_recursive_growth_non_meaning",
    "bounded_self_recursive_growth_envelope",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_self_continuation_self_recursive_growth_summary",
)

SELECTED_BASIS_SECTIONS = (
    "selected_self_recursive_growth_boundary_basis",
    "selected_self_recursive_growth_boundary_terminal_summary_basis",
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

POSTURE_SECTIONS = (
    "self_recursive_growth_spec_only_posture",
    "one_bounded_self_recursive_growth_posture",
    "self_recursive_growth_boundary_basis_preserved_posture",
    "self_continuation_basis_preserved_posture",
    "bounded_self_continuation_envelope_preserved_posture",
    "bounded_self_recursive_growth_envelope_declared_posture",
    "self_recursive_growth_not_daemon_posture",
    "self_recursive_growth_not_loop_posture",
    "self_recursive_growth_not_public_api_posture",
    "self_recursive_growth_not_participant_facing_interface_posture",
    "self_recursive_growth_not_distributed_network_behavior_posture",
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
    "repo_local_availability_not_self_recursive_growth_authority_posture",
    "artifact_existence_not_self_recursive_growth_authority_posture",
    "latest_file_posture_not_self_recursive_growth_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
)

TRUE_STATEMENT_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)

SENTINELS = (
    "RAW_SELF_RECURSIVE_GROWTH_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_SELF_RECURSIVE_GROWTH_ENVELOPE_BODY_MUST_NOT_RETURN",
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
    "raw_self_recursive_growth_body",
    "raw_bounded_self_recursive_growth_envelope_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_recursive_growth_body",
    "bounded_self_recursive_growth_envelope_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

SAFETY_STATEMENT_FIELDS = (
    "self_recursive_growth_not_daemon",
    "self_recursive_growth_not_loop",
    "self_recursive_growth_not_public_api",
    "self_recursive_growth_not_participant_facing_interface",
    "self_recursive_growth_not_distributed_network_behavior",
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
    "result_level_non_claims_canonical_false",
)

EXPECTED_SUCCESS_CHECK_NAMES = (
    "self-recursive-growth question declared",
    "self-recursive-growth intent supported",
    "self-recursive-growth scope supported",
    "self-recursive-growth-boundary basis declared",
    "self-recursive-growth-boundary terminal summary basis declared",
    "self-recursive-growth-boundary outcome recorded",
    "self-recursive-growth-boundary version 0.1.0",
    "self-recursive-growth-boundary failed checks zero",
    "self-recursive-growth-boundary declared future review",
    "self-recursive-growth-boundary canonicalized result-level non-claims",
    "self-recursive-growth-boundary terminal summary states self-recursive growth not created",
    "self-recursive-growth-boundary terminal summary states no self-recursive growth selected",
    "self-recursive-growth-boundary terminal summary requires separate future review",
    "self-continuation basis declared",
    "self-continuation terminal summary basis declared",
    "self-continuation outcome recorded",
    "self-continuation version 0.1.0",
    "self-continuation failed checks zero",
    "self-continuation recorded bounded self-continuation posture",
    "self-continuation recorded bounded self-continuation envelope",
    "selected_self_continuation_boundary_basis declared",
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
    "returned second-carrier capture lineage basis declared",
    "predecessor failure evidence remains visible and unrepaired",
    "official enum scope strings not redacted",
    "hostile raw body content contained",
)


def _valid_request() -> dict[str, Any]:
    return resolver.build_declared_post_self_continuation_self_recursive_growth_request()


def _serialized(value: Mapping[str, Any]) -> str:
    return json.dumps(value, sort_keys=True)


def _failed_checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("self_recursive_growth_checks")
    if not isinstance(checks, list):
        return []
    return [check for check in checks if isinstance(check, Mapping) and check.get("passed") is False]


def _emitted_codes(result: Mapping[str, Any]) -> set[str]:
    codes: set[str] = set()
    block = result.get("block")
    if isinstance(block, Mapping) and isinstance(block.get("block_code"), str):
        codes.add(block["block_code"])
    checks = result.get("self_recursive_growth_checks")
    if isinstance(checks, list):
        for check in checks:
            if not isinstance(check, Mapping):
                continue
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if isinstance(code, str):
                    codes.add(code)
    return codes


def _set_basis_value(request: dict[str, Any], basis_field: str, key: str, value: Any) -> None:
    basis = request.setdefault(basis_field, {})
    if isinstance(basis, dict):
        basis[key] = value


def _set_request_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[field] = value

    return mutate


class PostSelfContinuationSelfRecursiveGrowthResolverTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        checks = result.get("self_recursive_growth_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, Mapping)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_statement_booleans(self, result: Mapping[str, Any]) -> None:
        statement = result.get("self_recursive_growth_statement")
        self.assertIsInstance(statement, Mapping)
        for key, value in statement.items():
            self.assertIsInstance(value, bool, key)
        non_meaning = result.get("self_recursive_growth_non_meaning")
        self.assertIsInstance(non_meaning, Mapping)
        for key, value in non_meaning.items():
            self.assertIsInstance(value, bool, key)
        envelope = result.get("bounded_self_recursive_growth_envelope")
        self.assertIsInstance(envelope, Mapping)
        for key, value in envelope.items():
            if isinstance(value, bool):
                self.assertIs(type(value), bool, key)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(type(non_claims[key]), bool, key)

    def assert_no_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _serialized(result)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("self_recursive_growth_scope")
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-self-recursive-growth-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE:
            self.assertNotEqual(value, "[bounded-self-recursive-growth-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")

    def assert_no_created_or_authorized_posture(self, result: Mapping[str, Any]) -> None:
        statement = result.get("self_recursive_growth_statement")
        self.assertIsInstance(statement, Mapping)
        for key in SAFETY_STATEMENT_FIELDS:
            self.assertIs(statement.get(key), True, key)
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for key in (
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
            "broader_reusable_permission_created",
            "follow_on_work_authorized",
            "self_recursive_growth_treated_as_runtime_daemon",
            "self_recursive_growth_treated_as_runtime_loop",
            "self_recursive_growth_treated_as_public_api",
            "self_recursive_growth_treated_as_participant_facing_interface",
            "self_recursive_growth_treated_as_distributed_network_behavior",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(non_claims.get(key), False, key)

    def assert_bounded_envelope(self, result: Mapping[str, Any]) -> None:
        envelope = result.get("bounded_self_recursive_growth_envelope")
        self.assertIsInstance(envelope, Mapping)
        self.assertIs(envelope.get("declared"), True)
        self.assertEqual(envelope.get("envelope_type"), "bounded_self_recursive_growth_envelope")
        self.assertIs(envelope.get("self_recursive_growth_limited_to_declared_envelope"), True)
        for key in (
            "authorizes_arbitrary_runtime_activity",
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
            "authorizes_follow_on_work",
        ):
            self.assertIs(envelope.get(key), False, key)
        self.assertIs(envelope.get("anything_outside_envelope_requires_fresh_admission"), True)

    def test_public_api_constants_and_supported_values(self) -> None:
        for name in (
            "resolve_post_self_continuation_self_recursive_growth",
            "resolve_post_self_continuation_self_recursive_growth_from_path",
            "write_post_self_continuation_self_recursive_growth_result",
            "build_post_self_continuation_self_recursive_growth_summary",
            "build_declared_post_self_continuation_self_recursive_growth_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_SCOPE_VALUES",
            "SUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_post_self_continuation_self_recursive_growth")
        self.assertEqual(resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE, resolver.SUPPORTED_SCOPE_VALUES)
        output_root = str(resolver.OUTPUT_ROOT).replace("\\", "/")
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX), output_root)
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)

        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)
        for value in resolver.SUPPORTED_SCOPE_VALUES:
            self.assertNotEqual(value, "[bounded-self-recursive-growth-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = _valid_request()
        result = resolver.resolve_post_self_continuation_self_recursive_growth(request)
        summary = resolver.build_post_self_continuation_self_recursive_growth_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_post_self_continuation_self_recursive_growth")
        self.assertEqual(summary["request_id"], request["self_recursive_growth_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        statement = result["self_recursive_growth_statement"]
        for key in TRUE_STATEMENT_FIELDS:
            self.assertIs(statement.get(key), True, key)

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_statement_booleans(result)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_created_or_authorized_posture(result)
        self.assert_bounded_envelope(result)

        check_names = {check["check_name"] for check in result["self_recursive_growth_checks"]}
        for check_name in EXPECTED_SUCCESS_CHECK_NAMES:
            self.assertIn(check_name, check_names)

    def test_required_false_non_claims_are_canonicalized_on_illegal_true_input(self) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = _valid_request()
                request["declared_non_claims"][key] = True
                result = resolver.resolve_post_self_continuation_self_recursive_growth(request)

                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsInstance(result["block"], Mapping)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assertTrue(_failed_checks(result))
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)
                self.assertIs(result["non_claims"][key], False)
                self.assertFalse(any(value is True for value in result["non_claims"].values()))
                self.assert_no_created_or_authorized_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        def modified(mutator: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
            request = _valid_request()
            mutator(request)
            return resolver.resolve_post_self_continuation_self_recursive_growth(request)

        cases: tuple[tuple[str, Callable[[], dict[str, Any]], str | None], ...] = (
            (
                "explicit block intent",
                lambda: modified(
                    _set_request_field(
                        "self_recursive_growth_intent",
                        "BLOCK_POST_SELF_CONTINUATION_SELF_RECURSIVE_GROWTH",
                    )
                ),
                "SELF_RECURSIVE_GROWTH_EXPLICIT_BLOCK_REQUESTED",
            ),
            (
                "missing request",
                lambda: resolver.resolve_post_self_continuation_self_recursive_growth(None),
                "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            ),
            (
                "non-mapping request",
                lambda: resolver.resolve_post_self_continuation_self_recursive_growth(["not", "mapping"]),  # type: ignore[arg-type]
                "DECLARED_SELF_RECURSIVE_GROWTH_REQUEST_MALFORMED",
            ),
            ("unsupported intent", lambda: modified(_set_request_field("self_recursive_growth_intent", "UNSUPPORTED")), "SELF_RECURSIVE_GROWTH_INTENT_UNSUPPORTED"),
            ("unsupported scope", lambda: modified(_set_request_field("self_recursive_growth_scope", ["UNSUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE_VALUE"])), "UNSUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE"),
            ("missing self-recursive-growth-boundary basis", lambda: modified(lambda request: request.pop("selected_self_recursive_growth_boundary_basis")), "SELF_RECURSIVE_GROWTH_BOUNDARY_BASIS_MISSING"),
            ("self-recursive-growth-boundary not recorded", lambda: modified(lambda request: _set_basis_value(request, "selected_self_recursive_growth_boundary_basis", "outcome", "NOT_RECORDED")), "SELF_RECURSIVE_GROWTH_BOUNDARY_NOT_RECORDED"),
            ("self-recursive-growth-boundary failed checks present", lambda: modified(lambda request: _set_basis_value(request, "selected_self_recursive_growth_boundary_basis", "failed_check_count", 1)), "SELF_RECURSIVE_GROWTH_BOUNDARY_FAILED_CHECKS_PRESENT"),
            ("self-recursive-growth-boundary version not 0.1.0", lambda: modified(lambda request: _set_basis_value(request, "selected_self_recursive_growth_boundary_basis", "result_version", "9.9.9")), "SELF_RECURSIVE_GROWTH_BOUNDARY_VERSION_NOT_0_1_0"),
            ("self-recursive-growth-boundary did not declare future review", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_declared_future_review", False)), "SELF_RECURSIVE_GROWTH_BOUNDARY_DID_NOT_DECLARE_FUTURE_SELF_RECURSIVE_GROWTH_REVIEW"),
            ("self-recursive-growth-boundary already created self-recursive growth", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_self_recursive_growth", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_SELF_RECURSIVE_GROWTH"),
            ("self-recursive-growth-boundary already created daemon", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_runtime_daemon", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_DAEMON"),
            ("self-recursive-growth-boundary already created loop", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_runtime_loop", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_RUNTIME_LOOP"),
            ("self-recursive-growth-boundary already created public API", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_public_api", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PUBLIC_API"),
            ("self-recursive-growth-boundary already created participant-facing interface", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_participant_facing_interface", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE"),
            ("self-recursive-growth-boundary already created distributed network behavior", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_already_created_distributed_network_behavior", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR"),
            ("self-recursive-growth-boundary treated boundary as self-recursive growth", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_treated_as_self_recursive_growth", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH"),
            ("self-recursive-growth-boundary treated boundary as daemon", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_treated_as_runtime_daemon", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_DAEMON"),
            ("self-recursive-growth-boundary treated boundary as loop", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_treated_as_runtime_loop", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_TREATED_AS_RUNTIME_LOOP"),
            ("self-recursive-growth-boundary authorized future work", lambda: modified(_set_request_field("selected_self_recursive_growth_boundary_authorized_future_work", True)), "SELF_RECURSIVE_GROWTH_BOUNDARY_AUTHORIZED_FUTURE_WORK"),
            ("self-continuation basis missing", lambda: modified(lambda request: request.pop("selected_self_continuation_basis")), "SELF_CONTINUATION_BASIS_MISSING"),
            ("self-continuation not recorded", lambda: modified(lambda request: _set_basis_value(request, "selected_self_continuation_basis", "outcome", "NOT_RECORDED")), "SELF_CONTINUATION_NOT_RECORDED"),
            ("self-continuation already created daemon", lambda: modified(_set_request_field("selected_self_continuation_already_created_runtime_daemon", True)), "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON"),
            ("self-continuation already created loop", lambda: modified(_set_request_field("selected_self_continuation_already_created_runtime_loop", True)), "SELF_CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP"),
            ("self-continuation already created public API", lambda: modified(_set_request_field("selected_self_continuation_already_created_public_api", True)), "SELF_CONTINUATION_ALREADY_CREATED_PUBLIC_API"),
            ("self-continuation already created participant-facing interface", lambda: modified(_set_request_field("selected_self_continuation_already_created_participant_facing_interface", True)), "SELF_CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE"),
            ("self-continuation already created distributed network behavior", lambda: modified(_set_request_field("selected_self_continuation_already_created_distributed_network_behavior", True)), "SELF_CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR"),
            ("bounded self-continuation envelope treated as self-recursive growth before review", lambda: modified(_set_request_field("selected_bounded_self_continuation_envelope_treated_as_self_recursive_growth_before_review", True)), "BOUNDED_SELF_CONTINUATION_ENVELOPE_TREATED_AS_SELF_RECURSIVE_GROWTH_BEFORE_REVIEW"),
            ("bounded self-continuation envelope authorized arbitrary runtime activity before review", lambda: modified(_set_request_field("selected_bounded_self_continuation_envelope_authorized_arbitrary_runtime_activity_before_review", True)), "BOUNDED_SELF_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY_BEFORE_REVIEW"),
            ("runtime-hosting-boundary v1 failure repaired", lambda: modified(_set_request_field("selected_runtime_hosting_boundary_v1_failure_repaired", True)), "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
            ("runtime-hosting-boundary v1 failure hidden", lambda: modified(_set_request_field("selected_runtime_hosting_boundary_v1_failure_hidden", True)), "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
            ("runtime-hosting-boundary v1 failure claimed passed", lambda: modified(_set_request_field("selected_runtime_hosting_boundary_v1_failure_claimed_passed", True)), "RUNTIME_HOSTING_BOUNDARY_V1_FAILURE_REPAIRED_OR_HIDDEN_OR_CLAIMED_PASSED"),
            ("self-recursive growth created before review", lambda: modified(_set_request_field("self_recursive_growth_created_before_review", True)), "SELF_RECURSIVE_GROWTH_CREATED_BEFORE_REVIEW"),
            ("self-recursive growth treated as daemon", lambda: modified(_set_request_field("self_recursive_growth_treated_as_runtime_daemon", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_DAEMON"),
            ("self-recursive growth treated as loop", lambda: modified(_set_request_field("self_recursive_growth_treated_as_runtime_loop", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_RUNTIME_LOOP"),
            ("self-recursive growth treated as public API", lambda: modified(_set_request_field("self_recursive_growth_treated_as_public_api", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_API"),
            ("self-recursive growth treated as participant-facing interface", lambda: modified(_set_request_field("self_recursive_growth_treated_as_participant_facing_interface", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_PARTICIPANT_FACING_INTERFACE"),
            ("self-recursive growth treated as distributed network behavior", lambda: modified(_set_request_field("self_recursive_growth_treated_as_distributed_network_behavior", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR"),
            ("self-recursive growth treated as source transfer", lambda: modified(_set_request_field("self_recursive_growth_treated_as_source_transfer", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_TRANSFER"),
            ("self-recursive growth treated as source receipt", lambda: modified(_set_request_field("self_recursive_growth_treated_as_source_receipt", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE_RECEIPT"),
            ("self-recursive growth treated as reception authorization", lambda: modified(_set_request_field("self_recursive_growth_treated_as_reception_authorization", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_RECEPTION_AUTHORIZATION"),
            ("self-recursive growth treated as source", lambda: modified(_set_request_field("self_recursive_growth_treated_as_source", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_SOURCE"),
            ("self-recursive growth treated as authority", lambda: modified(_set_request_field("self_recursive_growth_treated_as_authority", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_AUTHORITY"),
            ("self-recursive growth treated as currentness", lambda: modified(_set_request_field("self_recursive_growth_treated_as_currentness", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_CURRENTNESS"),
            ("self-recursive growth treated as deployment", lambda: modified(_set_request_field("self_recursive_growth_treated_as_deployment", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_DEPLOYMENT"),
            ("self-recursive growth treated as public release", lambda: modified(_set_request_field("self_recursive_growth_treated_as_public_release", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_PUBLIC_RELEASE"),
            ("self-recursive growth treated as operation permission", lambda: modified(_set_request_field("self_recursive_growth_treated_as_operation_permission", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_OPERATION_PERMISSION"),
            ("self-recursive growth treated as broader reusable permission", lambda: modified(_set_request_field("self_recursive_growth_treated_as_broader_reusable_permission", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_BROADER_REUSABLE_PERMISSION"),
            ("self-recursive growth treated as follow-on work", lambda: modified(_set_request_field("self_recursive_growth_treated_as_follow_on_work", True)), "SELF_RECURSIVE_GROWTH_TREATED_AS_FOLLOW_ON_WORK"),
            ("runtime daemon created", lambda: modified(_set_request_field("runtime_daemon_created", True)), "RUNTIME_DAEMON_CREATED"),
            ("runtime loop created", lambda: modified(_set_request_field("runtime_loop_created", True)), "RUNTIME_LOOP_CREATED"),
            ("public API created", lambda: modified(_set_request_field("public_api_created", True)), "PUBLIC_API_CREATED"),
            ("participant-facing interface created", lambda: modified(_set_request_field("participant_facing_interface_created", True)), "PARTICIPANT_FACING_INTERFACE_CREATED"),
            ("distributed network behavior created", lambda: modified(_set_request_field("distributed_network_behavior_created", True)), "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
            ("source transfer occurred", lambda: modified(_set_request_field("source_transfer_occurred", True)), "SOURCE_TRANSFER_OCCURRED"),
            ("source receipt occurred", lambda: modified(_set_request_field("source_receipt_occurred", True)), "SOURCE_RECEIPT_OCCURRED"),
            ("reception authorization created", lambda: modified(_set_request_field("reception_authorization_created", True)), "RECEPTION_AUTHORIZATION_CREATED"),
            ("source created", lambda: modified(_set_request_field("source_created", True)), "SOURCE_CREATED"),
            ("authority created", lambda: modified(_set_request_field("authority_created", True)), "AUTHORITY_CREATED"),
            ("currentness created", lambda: modified(_set_request_field("currentness_created", True)), "CURRENTNESS_CREATED"),
            ("deployment created", lambda: modified(_set_request_field("deployment_created", True)), "DEPLOYMENT_CREATED"),
            ("public release created", lambda: modified(_set_request_field("public_release_created", True)), "PUBLIC_RELEASE_CREATED"),
            ("operation permission created", lambda: modified(_set_request_field("operation_permission_created", True)), "OPERATION_PERMISSION_CREATED"),
            ("broader reusable permission created", lambda: modified(_set_request_field("broader_reusable_permission_created", True)), "BROADER_REUSABLE_PERMISSION_CREATED"),
            ("derivative reception authorized", lambda: modified(_set_request_field("derivative_reception_authorized", True)), "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel relation authorized", lambda: modified(_set_request_field("vessel_relation_authorized", True)), "VESSEL_RELATION_AUTHORIZED"),
            ("adoption created", lambda: modified(_set_request_field("adoption_created", True)), "ADOPTION_CREATED"),
            ("receiving-context governance created", lambda: modified(_set_request_field("receiving_context_governance_created", True)), "RECEIVING_CONTEXT_GOVERNANCE_CREATED"),
            ("publication flow created", lambda: modified(_set_request_field("publication_flow_created", True)), "PUBLICATION_FLOW_CREATED"),
            ("follow-on work authorized", lambda: modified(_set_request_field("follow_on_work_authorized", True)), "FOLLOW_ON_WORK_AUTHORIZED"),
            ("artifact existence treated as self-recursive-growth authority", lambda: modified(_set_request_field("artifact_existence_treated_as_self_recursive_growth_authority", True)), "ARTIFACT_EXISTENCE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
            ("artifact path treated as currentness", lambda: modified(_set_request_field("artifact_path_treated_as_currentness", True)), "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
            ("latest file posture treated as self-recursive-growth authority", lambda: modified(_set_request_field("latest_file_posture_treated_as_self_recursive_growth_authority", True)), "LATEST_FILE_POSTURE_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
            ("repo-local availability treated as self-recursive-growth authority", lambda: modified(_set_request_field("repo_local_availability_treated_as_self_recursive_growth_authority", True)), "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
            ("hidden repo state used as self-recursive-growth content", lambda: modified(_set_request_field("hidden_repo_state_used_as_self_recursive_growth_content", True)), "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_CONTENT"),
            ("hidden repo state used as self-recursive-growth authority", lambda: modified(_set_request_field("hidden_repo_state_used_as_self_recursive_growth_authority", True)), "HIDDEN_REPO_STATE_USED_AS_SELF_RECURSIVE_GROWTH_AUTHORITY"),
            ("selected basis not reference-shaped", lambda: modified(_set_request_field("reference_shaped_input_posture", False)), "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
            ("raw full prior artifact body returned", lambda: modified(_set_request_field("raw_full_prior_artifact_body_returned", True)), "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
            ("predecessor failure evidence hidden", lambda: modified(_set_request_field("predecessor_failure_evidence_visible", False)), "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
            ("predecessor failure repaired", lambda: modified(_set_request_field("predecessor_failure_repaired", True)), "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
            ("predecessor failure claimed passed", lambda: modified(_set_request_field("predecessor_failure_claimed_passed", True)), "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"),
            ("consumed request reopened", lambda: modified(_set_request_field("consumed_request_reopened", True)), "CONSUMED_REQUEST_REOPENED"),
            ("authorization token reused", lambda: modified(_set_request_field("authorization_token_reused", True)), "AUTHORIZATION_TOKEN_REUSED"),
            ("required non-claim missing", lambda: modified(lambda request: request["declared_non_claims"].pop("runtime_daemon_created")), "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("required non-claim flipped", lambda: modified(lambda request: request["declared_non_claims"].__setitem__("runtime_loop_created", True)), "NON_CLAIM_MISSING_OR_FLIPPED"),
        )

        for name, build_result, expected_code in cases:
            with self.subTest(name=name):
                result = build_result()
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsInstance(result["block"], Mapping)
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assert_public_codes(result)
                if expected_code is not None:
                    self.assertIn(expected_code, resolver.BLOCK_CODES)
                    self.assertIn(expected_code, _emitted_codes(result))
                self.assertTrue(_failed_checks(result))
                self.assert_canonical_non_claims(result)
                self.assert_no_created_or_authorized_posture(result)

    def test_missing_or_incomplete_declared_non_claims_still_emit_canonical_false(self) -> None:
        variants: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("remove declared_non_claims", lambda request: request.pop("declared_non_claims")),
            ("empty declared_non_claims", lambda request: request.__setitem__("declared_non_claims", {})),
            ("remove one required non-claim", lambda request: request["declared_non_claims"].pop("runtime_daemon_created")),
            (
                "non-bool declared non-claim",
                lambda request: request["declared_non_claims"].__setitem__("runtime_loop_created", "false"),
            ),
            ("none declared non-claim", lambda request: request["declared_non_claims"].__setitem__("public_api_created", None)),
        )
        for name, mutate in variants:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                result = resolver.resolve_post_self_continuation_self_recursive_growth(request)
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolver.resolve_post_self_continuation_self_recursive_growth(_valid_request())
        self.assert_official_scope_preserved(result)

        request = _valid_request()
        request["self_recursive_growth_scope"] = list(resolver.SUPPORTED_SELF_RECURSIVE_GROWTH_SCOPE)
        custom_result = resolver.resolve_post_self_continuation_self_recursive_growth(request)
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(custom_result)
        self.assert_canonical_non_claims(custom_result)

    def test_raw_hidden_hostile_content_is_contained_without_mutating_input(self) -> None:
        request = _valid_request()
        for index, section in enumerate(SELECTED_BASIS_SECTIONS):
            basis = request.setdefault(section, {})
            self.assertIsInstance(basis, dict)
            for key_index, key in enumerate(SENSITIVE_KEYS):
                basis[key] = {
                    "sentinel": SENTINELS[(index + key_index) % len(SENTINELS)],
                    "official_scope_value": OFFICIAL_SCOPE_VALUES[(index + key_index) % len(OFFICIAL_SCOPE_VALUES)],
                }
        before = copy.deepcopy(request)

        result = resolver.resolve_post_self_continuation_self_recursive_growth(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_created_or_authorized_posture(result)
        self.assertEqual(request, before)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(_valid_request(), indent=2, sort_keys=True), encoding="utf-8")

            result = resolver.resolve_post_self_continuation_self_recursive_growth_from_path(request_path)
            summary = resolver.build_post_self_continuation_self_recursive_growth_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], "resolve_post_self_continuation_self_recursive_growth")

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self._assert_path_blocks_or_raises(malformed_path)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self._assert_path_blocks_or_raises(array_path)
            self._assert_path_blocks_or_raises(tmp_path / "missing.json")

            output_root = tmp_path / EXPECTED_OUTPUT_ROOT_SUFFIX
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_post_self_continuation_self_recursive_growth_result(result)
                second = resolver.write_post_self_continuation_self_recursive_growth_result(result)

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            normalized_first = str(first).replace("\\", "/")
            normalized_second = str(second).replace("\\", "/")
            self.assertIn("post_self_continuation_self_recursive_growth", normalized_first)
            self.assertTrue(second.stem.endswith("_001"), normalized_second)
            for fragment in FORBIDDEN_WRITE_FRAGMENTS:
                self.assertNotIn(fragment, normalized_first)
                self.assertNotIn(fragment, normalized_second)

    def _assert_path_blocks_or_raises(self, path: Path) -> None:
        try:
            result = resolver.resolve_post_self_continuation_self_recursive_growth_from_path(path)
        except resolver.PostSelfContinuationSelfRecursiveGrowthError:
            return
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assert_public_codes(result)
        self.assert_canonical_non_claims(result)

    def test_resolver_does_not_mutate_request_or_selected_basis_inputs(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        selected_before = {section: copy.deepcopy(request[section]) for section in SELECTED_BASIS_SECTIONS}
        posture_before = {section: copy.deepcopy(request[section]) for section in POSTURE_SECTIONS}
        non_claims_before = copy.deepcopy(request["declared_non_claims"])
        scope_before = copy.deepcopy(request["self_recursive_growth_scope"])
        envelope_before = copy.deepcopy(request["requested_bounded_self_recursive_growth_envelope"])

        resolver.resolve_post_self_continuation_self_recursive_growth(request)

        self.assertEqual(request, before)
        self.assertEqual(request["declared_non_claims"], non_claims_before)
        self.assertEqual(request["self_recursive_growth_scope"], scope_before)
        self.assertEqual(request["requested_bounded_self_recursive_growth_envelope"], envelope_before)
        for section, value in selected_before.items():
            self.assertEqual(request[section], value, section)
        for section, value in posture_before.items():
            self.assertEqual(request[section], value, section)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_post_self_continuation_self_recursive_growth(_valid_request())
        summary = resolver.build_post_self_continuation_self_recursive_growth_summary(result)
        lineage = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]

        self.assertIs(lineage.get("preserved_as_failure_evidence"), True)
        self.assertIs(lineage.get("repaired"), False)
        self.assertIs(lineage.get("hidden"), False)
        self.assertIs(lineage.get("claimed_passed"), False)
        self.assertIs(result["self_recursive_growth_statement"]["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        for key in (
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(result["non_claims"][key], False, key)


if __name__ == "__main__":
    unittest.main()
