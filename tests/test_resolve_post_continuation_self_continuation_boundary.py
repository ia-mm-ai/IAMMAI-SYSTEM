"""Executable tests for the post-continuation self-continuation boundary.

This suite is bounded to self-continuation-boundary posture only.
Continuation and continuation-boundary are upstream basis, and
runtime-hosting-boundary v1 remains preserved predecessor failure lineage.
These tests do not create self-continuation, self-recursive growth, daemon,
loop, public API, participant-facing interface, distributed network behavior,
source transfer, source receipt, reception authorization, source, authority,
currentness, deployment, public release, operation permission, broader
reusable permission, adoption, receiving-context governance, publication flow,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_post_continuation_self_continuation_boundary as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_continuation_self_continuation_boundary"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_reusable_runtime_permission_continuation",
    "post_reusable_runtime_permission_continuation_boundary",
    "post_ongoing_runtime_reusable_runtime_permission",
    "post_runtime_hosting_ongoing_runtime",
    "post_successor_runtime_step_runtime_hosting",
    "self-continuation",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

FORBIDDEN_WRITE_FRAGMENTS = (
    "post_reusable_runtime_permission_continuation/",
    "post_reusable_runtime_permission_continuation_boundary",
    "post_ongoing_runtime_reusable_runtime_permission/",
    "post_runtime_hosting_ongoing_runtime/",
    "post_successor_runtime_step_runtime_hosting/",
    "post_successor_runtime_step_runtime_hosting_boundary_v2",
    "post_successor_runtime_step_runtime_hosting_boundary/",
    "post_minimal_runtime_successor_runtime_step",
    "post_portable_verification_runtime_boundary",
    "post_portable_verification_runtime_readiness",
    "portable_source_body_verification_final_completion",
    "portable-verification",
    "self-continuation",
    "deployment",
    "public-release",
    "source-transfer",
    "source-receipt",
    "reception",
)

OFFICIAL_SCOPE_VALUES = (
    "SELF_CONTINUATION_BOUNDARY_SPEC_ONLY",
    "ONE_FUTURE_SELF_CONTINUATION_REVIEW_DECLARED",
    "CONTINUATION_BASIS_PRESERVED",
    "CONTINUATION_NOT_SELF_CONTINUATION",
    "BOUNDED_CONTINUATION_ENVELOPE_NOT_SELF_CONTINUATION",
    "SELF_CONTINUATION_BOUNDARY_NOT_SELF_CONTINUATION",
    "SELF_CONTINUATION_BOUNDARY_NOT_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_NOT_CREATED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SELF_CONTINUATION_BOUNDARY_QUESTION_UNDECLARED",
    "SELF_CONTINUATION_BOUNDARY_INTENT_UNSUPPORTED",
    "CONTINUATION_BASIS_MISSING",
    "CONTINUATION_NOT_RECORDED",
    "CONTINUATION_FAILED_CHECKS_PRESENT",
    "CONTINUATION_VERSION_NOT_0_1_0",
    "CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_POSTURE",
    "CONTINUATION_DID_NOT_RECORD_BOUNDED_CONTINUATION_ENVELOPE",
    "CONTINUATION_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "CONTINUATION_ALREADY_CREATED_SELF_RECURSIVE_GROWTH",
    "CONTINUATION_ALREADY_CREATED_RUNTIME_DAEMON",
    "CONTINUATION_ALREADY_CREATED_RUNTIME_LOOP",
    "CONTINUATION_ALREADY_CREATED_PUBLIC_API",
    "CONTINUATION_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "CONTINUATION_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "CONTINUATION_TREATED_AS_SELF_CONTINUATION",
    "CONTINUATION_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "CONTINUATION_TREATED_AS_RUNTIME_DAEMON",
    "CONTINUATION_TREATED_AS_RUNTIME_LOOP",
    "CONTINUATION_TREATED_AS_PUBLIC_API",
    "CONTINUATION_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "CONTINUATION_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "CONTINUATION_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_CONTINUATION_ENVELOPE_TREATED_AS_SELF_CONTINUATION",
    "BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_SELF_CONTINUATION",
    "BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_SELF_RECURSIVE_GROWTH",
    "BOUNDED_CONTINUATION_ENVELOPE_AUTHORIZED_ARBITRARY_RUNTIME_ACTIVITY",
    "SELF_CONTINUATION_BOUNDARY_CREATED_BEFORE_REVIEW",
    "SELF_CONTINUATION_AUTHORIZED",
    "SELF_RECURSIVE_GROWTH_CREATED",
    "RUNTIME_DAEMON_CREATED",
    "RUNTIME_LOOP_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SELF_RECURSIVE_GROWTH",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_SOURCE",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_AUTHORITY",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_CURRENTNESS",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_BROADER_REUSABLE_PERMISSION",
    "SELF_CONTINUATION_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SELF_CONTINUATION_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE",
    "DECLARED_SELF_CONTINUATION_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_SELF_CONTINUATION_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_continuation_self_continuation_boundary_metadata",
    "declared_self_continuation_boundary_question",
    "selected_continuation_basis",
    "selected_continuation_terminal_summary_basis",
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
    "self_continuation_boundary_spec_only_posture",
    "one_future_self_continuation_review_posture",
    "continuation_basis_preserved_posture",
    "continuation_not_self_continuation_posture",
    "bounded_continuation_envelope_not_self_continuation_posture",
    "self_continuation_boundary_not_self_continuation_posture",
    "self_continuation_boundary_not_self_recursive_growth_posture",
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
    "repo_local_availability_not_self_continuation_boundary_authority_posture",
    "artifact_existence_not_self_continuation_boundary_authority_posture",
    "latest_file_posture_not_self_continuation_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "self_continuation_boundary_scope",
    "self_continuation_boundary_checks",
    "self_continuation_boundary_statement",
    "self_continuation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_continuation_self_continuation_boundary_summary",
)

STATEMENT_TRUE_FIELDS = (
    "self_continuation_boundary_recorded",
    "one_future_self_continuation_review_declared",
    "continuation_basis_preserved",
    "continuation_not_self_continuation",
    "bounded_continuation_envelope_not_self_continuation",
    "self_continuation_boundary_not_self_continuation",
    "self_continuation_boundary_not_self_recursive_growth",
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
    "hidden_repo_state_not_used_as_self_continuation_boundary_authority",
    "repo_local_availability_not_self_continuation_boundary_authority",
    "artifact_existence_not_self_continuation_boundary_authority",
    "latest_file_posture_not_self_continuation_boundary_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

RAW_SENTINELS = (
    "RAW_SELF_CONTINUATION_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_SELF_CONTINUATION_BODY_MUST_NOT_RETURN",
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

RAW_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_self_continuation_boundary_body",
    "raw_self_continuation_body",
    "raw_self_recursive_growth_body",
    "raw_runtime_daemon_body",
    "raw_runtime_loop_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "raw_runtime_body",
    "self_continuation_boundary_body",
    "self_continuation_body",
    "runtime_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

BASIS_SECTIONS = (
    "selected_continuation_basis",
    "selected_continuation_terminal_summary_basis",
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
    return resolver.build_declared_post_continuation_self_continuation_boundary_request(
        **overrides
    )


def resolve_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return resolver.resolve_post_continuation_self_continuation_boundary(request)


def checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    value = result.get("self_continuation_boundary_checks", [])
    return value if isinstance(value, list) else []


def statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    value = result.get("self_continuation_boundary_statement", {})
    return value if isinstance(value, Mapping) else {}


def non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    value = result.get("non_claims", {})
    return value if isinstance(value, Mapping) else {}


def failed_checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [check for check in checks(result) if check.get("passed") is not True]


def mutate_request(request: dict[str, Any], key: str, value: Any) -> dict[str, Any]:
    mutated = copy.deepcopy(request)
    if value == "__DELETE__":
        mutated.pop(key, None)
    else:
        mutated[key] = value
    return mutated


class PostContinuationSelfContinuationBoundaryTests(unittest.TestCase):
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
        for field, value in statement(result).items():
            self.assertIs(type(value), bool, field)
        non_meaning = result.get("self_continuation_boundary_non_meaning", {})
        self.assertIsInstance(non_meaning, Mapping)
        for field, value in non_meaning.items():
            self.assertIs(type(value), bool, field)
        for field, value in non_claims(result).items():
            self.assertIs(type(value), bool, field)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        emitted = non_claims(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
            self.assertIs(type(emitted[key]), bool, key)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope = result.get("self_continuation_boundary_scope", [])
        self.assertIsInstance(scope, list)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-self-continuation-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)

    def assert_no_creation_or_authorization(self, result: Mapping[str, Any]) -> None:
        st = statement(result)
        for key in (
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
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(st.get(key), True, key)
        emitted = non_claims(result)
        for key in (
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
            "consumed_request_reopened",
            "authorization_token_reused",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        ):
            self.assertIs(emitted.get(key), False, key)

    def assert_blocked_safely(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIn(block.get("block_code"), resolver.BLOCK_CODES)
        self.assertGreaterEqual(len(failed_checks(result)), 1)
        self.assert_public_codes(result)
        self.assert_no_creation_or_authorization(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_boolean_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_continuation_self_continuation_boundary",
            "resolve_post_continuation_self_continuation_boundary_from_path",
            "write_post_continuation_self_continuation_boundary_result",
            "build_post_continuation_self_continuation_boundary_summary",
            "build_declared_post_continuation_self_continuation_boundary_request",
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
            "SUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_continuation_self_continuation_boundary",
        )
        self.assertEqual(
            resolver.SUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE,
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

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = build_request()
        result = resolve_request(request)
        summary = resolver.build_post_continuation_self_continuation_boundary_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIsNone(result["block"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["request_id"], request["self_continuation_boundary_request_id"])

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        st = statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIn(field, st)
            self.assertIs(st[field], True, field)
            self.assertIs(type(st[field]), bool, field)

        self.assert_non_claims_canonical_false(result)
        self.assert_public_codes(result)
        self.assert_boolean_posture(result)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_sentinels(result)

    def test_declared_non_claims_are_canonicalized_false_on_block(self) -> None:
        named_required = (
            "self_continuation_authorized",
            "self_recursive_growth_created",
            "runtime_daemon_created",
            "runtime_loop_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "self_continuation_boundary_treated_as_self_continuation",
            "self_continuation_boundary_treated_as_self_recursive_growth",
            "continuation_treated_as_self_continuation",
            "continuation_treated_as_self_recursive_growth",
            "continuation_treated_as_runtime_daemon",
            "continuation_treated_as_runtime_loop",
            "continuation_treated_as_public_api",
            "continuation_treated_as_participant_facing_interface",
            "continuation_treated_as_distributed_network_behavior",
            "bounded_continuation_envelope_treated_as_self_continuation",
            "bounded_continuation_envelope_authorized_self_continuation",
            "bounded_continuation_envelope_authorized_self_recursive_growth",
            "bounded_continuation_envelope_authorized_arbitrary_runtime_activity",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        for key in named_required:
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

        clean = build_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = copy.deepcopy(clean)
                request["declared_non_claims"][key] = True
                result = resolve_request(request)
                self.assert_blocked_safely(result)
                self.assertIs(result["non_claims"][key], False)

    def test_representative_blocking_behavior(self) -> None:
        clean = build_request()
        cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", {"self_continuation_boundary_intent": "BLOCK_POST_CONTINUATION_SELF_CONTINUATION_BOUNDARY"}),
            ("missing request", None),
            ("non-mapping request", ["not", "mapping"]),
            ("unsupported intent", {"self_continuation_boundary_intent": "UNSUPPORTED"}),
            ("unsupported scope", {"self_continuation_boundary_scope": ["UNSUPPORTED_SCOPE"]}),
            ("missing continuation basis", {"selected_continuation_basis": "__DELETE__"}),
            ("continuation not recorded", {"selected_continuation_result_outcome": "NOT_RECORDED"}),
            ("continuation failed checks present", {"selected_continuation_failed_check_count": 1}),
            ("continuation version not 0.1.0", {"selected_continuation_result_version": "0.0.1"}),
            ("continuation did not record bounded continuation posture", {"selected_continuation_bounded_posture_recorded": False}),
            ("continuation did not record bounded continuation envelope", {"selected_continuation_bounded_continuation_envelope_recorded": False}),
            ("continuation already authorized self-continuation", {"selected_continuation_already_authorized_self_continuation": True}),
            ("continuation already created self-recursive growth", {"selected_continuation_already_created_self_recursive_growth": True}),
            ("continuation already created daemon", {"selected_continuation_already_created_runtime_daemon": True}),
            ("continuation already created loop", {"selected_continuation_already_created_runtime_loop": True}),
            ("continuation already created public API", {"selected_continuation_already_created_public_api": True}),
            ("continuation already created participant interface", {"selected_continuation_already_created_participant_facing_interface": True}),
            ("continuation already created distributed network", {"selected_continuation_already_created_distributed_network_behavior": True}),
            ("continuation treated as self-continuation", {"selected_continuation_treated_as_self_continuation": True}),
            ("continuation treated as self-recursive growth", {"selected_continuation_treated_as_self_recursive_growth": True}),
            ("continuation treated as daemon", {"selected_continuation_treated_as_runtime_daemon": True}),
            ("continuation treated as loop", {"selected_continuation_treated_as_runtime_loop": True}),
            ("continuation treated as public API", {"selected_continuation_treated_as_public_api": True}),
            ("continuation treated as participant interface", {"selected_continuation_treated_as_participant_facing_interface": True}),
            ("continuation treated as distributed network", {"selected_continuation_treated_as_distributed_network_behavior": True}),
            ("continuation authorized future work", {"selected_continuation_authorized_future_work": True}),
            ("bounded continuation envelope treated as self-continuation", {"selected_bounded_continuation_envelope_treated_as_self_continuation": True}),
            ("bounded continuation envelope authorized self-continuation", {"selected_bounded_continuation_envelope_authorized_self_continuation": True}),
            ("bounded continuation envelope authorized self-recursive growth", {"selected_bounded_continuation_envelope_authorized_self_recursive_growth": True}),
            ("bounded continuation envelope authorized arbitrary runtime activity", {"selected_bounded_continuation_envelope_authorized_arbitrary_runtime_activity": True}),
            ("self-continuation-boundary created before review", {"self_continuation_boundary_created_before_review": True}),
            ("self-continuation authorized", {"self_continuation_authorized": True}),
            ("self-recursive growth created", {"self_recursive_growth_created": True}),
            ("runtime daemon created", {"runtime_daemon_created": True}),
            ("runtime loop created", {"runtime_loop_created": True}),
            ("public API created", {"public_api_created": True}),
            ("participant-facing interface created", {"participant_facing_interface_created": True}),
            ("distributed network behavior created", {"distributed_network_behavior_created": True}),
            ("self-continuation-boundary treated as self-continuation", {"self_continuation_boundary_treated_as_self_continuation": True}),
            ("self-continuation-boundary treated as self-recursive growth", {"self_continuation_boundary_treated_as_self_recursive_growth": True}),
            ("self-continuation-boundary treated as source transfer", {"self_continuation_boundary_treated_as_source_transfer": True}),
            ("self-continuation-boundary treated as source receipt", {"self_continuation_boundary_treated_as_source_receipt": True}),
            ("self-continuation-boundary treated as reception authorization", {"self_continuation_boundary_treated_as_reception_authorization": True}),
            ("self-continuation-boundary treated as source", {"self_continuation_boundary_treated_as_source": True}),
            ("self-continuation-boundary treated as authority", {"self_continuation_boundary_treated_as_authority": True}),
            ("self-continuation-boundary treated as currentness", {"self_continuation_boundary_treated_as_currentness": True}),
            ("self-continuation-boundary treated as deployment", {"self_continuation_boundary_treated_as_deployment": True}),
            ("self-continuation-boundary treated as public release", {"self_continuation_boundary_treated_as_public_release": True}),
            ("self-continuation-boundary treated as operation permission", {"self_continuation_boundary_treated_as_operation_permission": True}),
            ("self-continuation-boundary treated as broader reusable permission", {"self_continuation_boundary_treated_as_broader_reusable_permission": True}),
            ("self-continuation-boundary treated as follow-on work", {"self_continuation_boundary_treated_as_follow_on_work": True}),
            ("source transfer occurred", {"source_transfer_occurred": True}),
            ("source receipt occurred", {"source_receipt_occurred": True}),
            ("reception authorization created", {"reception_authorization_created": True}),
            ("source created", {"source_created": True}),
            ("authority created", {"authority_created": True}),
            ("currentness created", {"currentness_created": True}),
            ("deployment created", {"deployment_created": True}),
            ("public release created", {"public_release_created": True}),
            ("operation permission created", {"operation_permission_created": True}),
            ("broader reusable permission created", {"broader_reusable_permission_created": True}),
            ("derivative reception authorized", {"derivative_reception_authorized": True}),
            ("vessel relation authorized", {"vessel_relation_authorized": True}),
            ("adoption created", {"adoption_created": True}),
            ("receiving-context governance created", {"receiving_context_governance_created": True}),
            ("publication flow created", {"publication_flow_created": True}),
            ("follow-on work authorized", {"follow_on_work_authorized": True}),
            ("artifact existence treated as authority", {"artifact_existence_treated_as_self_continuation_boundary_authority": True}),
            ("artifact path treated as currentness", {"artifact_path_treated_as_currentness": True}),
            ("latest file posture treated as authority", {"latest_file_posture_treated_as_self_continuation_boundary_authority": True}),
            ("repo local availability treated as authority", {"repo_local_availability_treated_as_self_continuation_boundary_authority": True}),
            ("hidden repo state used as content", {"hidden_repo_state_used_as_self_continuation_boundary_content": True}),
            ("hidden repo state used as authority", {"hidden_repo_state_used_as_self_continuation_boundary_authority": True}),
            ("selected basis not reference-shaped", {"reference_shaped_input_posture": False}),
            ("raw full prior artifact body returned", {"raw_full_prior_artifact_body_returned": True}),
            ("predecessor failure repaired", {"predecessor_failure_repaired": True}),
            ("predecessor failure hidden", {"predecessor_failure_hidden": True}),
            ("predecessor failure claimed passed", {"predecessor_failure_claimed_passed": True}),
            ("v1 failure repaired", {"selected_runtime_hosting_boundary_v1_failure_repaired": True}),
            ("v1 failure hidden", {"selected_runtime_hosting_boundary_v1_failure_hidden": True}),
            ("v1 failure claimed passed", {"selected_runtime_hosting_boundary_v1_failure_claimed_passed": True}),
            ("consumed request reopened", {"consumed_request_reopened": True}),
            ("authorization token reused", {"authorization_token_reused": True}),
            ("required non-claim flipped", {"declared_non_claims": {**clean["declared_non_claims"], "self_continuation_authorized": True}}),
        )

        for label, mutation in cases:
            with self.subTest(label=label):
                if mutation is None:
                    result = resolver.resolve_post_continuation_self_continuation_boundary(None)
                elif isinstance(mutation, list):
                    result = resolver.resolve_post_continuation_self_continuation_boundary(mutation)  # type: ignore[arg-type]
                else:
                    request = copy.deepcopy(clean)
                    for key, value in mutation.items():
                        if value == "__DELETE__":
                            request.pop(key, None)
                        else:
                            request[key] = value
                    result = resolve_request(request)
                self.assert_blocked_safely(result)

    def test_missing_or_incomplete_declared_non_claims_block_safely(self) -> None:
        clean = build_request()
        variants = (
            ("remove declared_non_claims", lambda req: req.pop("declared_non_claims", None)),
            ("empty declared_non_claims", lambda req: req.__setitem__("declared_non_claims", {})),
            (
                "remove one required non-claim",
                lambda req: req["declared_non_claims"].pop("self_continuation_authorized", None),
            ),
            (
                "non-bool string",
                lambda req: req["declared_non_claims"].__setitem__(
                    "self_continuation_authorized", "false"
                ),
            ),
            (
                "none value",
                lambda req: req["declared_non_claims"].__setitem__(
                    "self_continuation_authorized", None
                ),
            ),
        )
        for label, mutate in variants:
            with self.subTest(label=label):
                request = copy.deepcopy(clean)
                mutate(request)
                result = resolve_request(request)
                self.assertIn(
                    result["outcome"],
                    (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                )
                self.assert_public_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolve_request(build_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(result)

        custom_request = build_request(
            self_continuation_boundary_scope=list(
                resolver.SUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE
            )
        )
        custom_result = resolve_request(custom_request)
        self.assertEqual(custom_result["outcome"], resolver.OUTCOME_RECORDED)
        self.assert_official_scope_preserved(custom_result)

    def test_raw_hidden_hostile_content_is_contained_without_mutation(self) -> None:
        request = build_request()
        for index, section in enumerate(BASIS_SECTIONS):
            request[section] = copy.deepcopy(request[section])
            for key in RAW_KEYS:
                request[section][key] = RAW_SENTINELS[index % len(RAW_SENTINELS)]
        original = copy.deepcopy(request)

        result = resolve_request(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_raw_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_creation_or_authorization(result)
        self.assertEqual(request, original)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir_name:
            tempdir = Path(tempdir_name)
            request_path = tempdir / "request.json"
            request_path.write_text(json.dumps(build_request()), encoding="utf-8")
            result = resolver.resolve_post_continuation_self_continuation_boundary_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = resolver.build_post_continuation_self_continuation_boundary_summary(result)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tempdir / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            self.assert_blocked_safely(
                resolver.resolve_post_continuation_self_continuation_boundary_from_path(
                    malformed_path
                )
            )

            array_path = tempdir / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked_safely(
                resolver.resolve_post_continuation_self_continuation_boundary_from_path(
                    array_path
                )
            )

            self.assert_blocked_safely(
                resolver.resolve_post_continuation_self_continuation_boundary_from_path(
                    tempdir / "missing.json"
                )
            )

            output_root = tempdir / "post_continuation_self_continuation_boundary"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_post_continuation_self_continuation_boundary_result(
                    result
                )
                second_path = resolver.write_post_continuation_self_continuation_boundary_result(
                    result
                )

            self.assertTrue(first_path.parent.exists())
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            path_text = first_path.as_posix()
            self.assertIn("post_continuation_self_continuation_boundary", path_text)
            for fragment in FORBIDDEN_WRITE_FRAGMENTS:
                self.assertNotIn(fragment, path_text)

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = build_request()
        request["self_continuation_boundary_scope"] = {
            value: True for value in resolver.SUPPORTED_SELF_CONTINUATION_BOUNDARY_SCOPE
        }
        before = copy.deepcopy(request)
        basis_before = {section: copy.deepcopy(request[section]) for section in BASIS_SECTIONS}
        posture_before = {
            key: copy.deepcopy(value)
            for key, value in request.items()
            if key.endswith("_posture")
        }

        result = resolve_request(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, before)
        for section in BASIS_SECTIONS:
            self.assertEqual(request[section], basis_before[section], section)
        for key, value in posture_before.items():
            self.assertEqual(request[key], value, key)
        self.assertEqual(
            request["declared_non_claims"],
            before["declared_non_claims"],
        )
        self.assertEqual(
            request["self_continuation_boundary_scope"],
            before["self_continuation_boundary_scope"],
        )

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request(build_request())
        summary = resolver.build_post_continuation_self_continuation_boundary_summary(result)
        v1_basis = result["selected_runtime_hosting_boundary_v1_failure_lineage_basis"]

        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(v1_basis["preserved_failed_lineage"], True)
        self.assertIs(statement(result)["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)
        emitted = non_claims(result)
        self.assertIs(emitted["predecessor_failure_repaired"], False)
        self.assertIs(emitted["predecessor_failure_hidden"], False)
        self.assertIs(emitted["predecessor_failure_claimed_passed"], False)
        self.assertIs(emitted["consumed_request_reopened"], False)
        self.assertIs(emitted["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
