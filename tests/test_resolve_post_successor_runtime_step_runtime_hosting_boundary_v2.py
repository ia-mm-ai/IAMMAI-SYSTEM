"""Executable tests for the v2 runtime-hosting-boundary resolver.

This suite is additive and preserves the v1 resolver/test failure as
predecessor evidence. It proves the v2 correction: incoming illegal or flipped
``declared_non_claims`` may block a request, but emitted result-level
``non_claims`` are always canonical false posture. These tests do not create
runtime hosting, ongoing runtime, reusable runtime permission, continuation,
self-continuation, daemon, loop, public API, participant-facing interface,
distributed network behavior, source, authority, currentness, deployment,
public release, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_post_successor_runtime_step_runtime_hosting_boundary_v2 as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary_v2"
)
V1_OUTPUT_ROOT_SUFFIX = (
    "artifacts/"
    "integrity_host_v0_min_coexistence_post_successor_runtime_step_runtime_hosting_boundary"
)

OFFICIAL_SCOPE_VALUES = (
    "RUNTIME_HOSTING_BOUNDARY_NOT_RUNTIME_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_NOT_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_BOUNDARY_NOT_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_NOT_CONTINUATION",
    "RUNTIME_HOSTING_NOT_CREATED",
    "ONGOING_RUNTIME_NOT_CREATED",
    "REUSABLE_RUNTIME_PERMISSION_NOT_CREATED",
    "NO_CONTINUATION_AUTHORIZED",
    "SELF_CONTINUATION_NOT_AUTHORIZED",
    "RUNTIME_DAEMON_NOT_CREATED",
    "RUNTIME_LOOP_NOT_CREATED",
    "PUBLIC_API_NOT_CREATED",
    "PARTICIPANT_FACING_INTERFACE_NOT_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_NOT_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
)

REPRESENTATIVE_BLOCK_CODES = (
    "RUNTIME_HOSTING_BOUNDARY_QUESTION_UNDECLARED",
    "RUNTIME_HOSTING_BOUNDARY_INTENT_UNSUPPORTED",
    "SUCCESSOR_RUNTIME_STEP_BASIS_MISSING",
    "SUCCESSOR_RUNTIME_STEP_NOT_RECORDED",
    "SUCCESSOR_RUNTIME_STEP_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RUNTIME_STEP_VERSION_NOT_0_1_0",
    "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_SUCCESSOR_RUNTIME_STEP",
    "SUCCESSOR_RUNTIME_STEP_DID_NOT_RECORD_BOUNDED_RESULT_OR_REFUSAL",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_CREATED_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_ALREADY_AUTHORIZED_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_RUNTIME_HOSTING",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_ONGOING_RUNTIME",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_TREATED_AS_SELF_CONTINUATION",
    "SUCCESSOR_RUNTIME_STEP_AUTHORIZED_FUTURE_WORK",
    "BOUNDED_SUCCESSOR_RUNTIME_RESULT_OR_REFUSAL_AUTHORIZED_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_CREATED_BEFORE_REVIEW",
    "RUNTIME_HOSTING_CREATED",
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
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RUNTIME_HOSTING",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_ONGOING_RUNTIME",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_RUNTIME_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CONTINUATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SELF_CONTINUATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_TRANSFER",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE_RECEIPT",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_RECEPTION_AUTHORIZATION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_SOURCE",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_AUTHORITY",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_CURRENTNESS",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_DEPLOYMENT",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_PUBLIC_RELEASE",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_OPERATION_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_REUSABLE_PERMISSION",
    "RUNTIME_HOSTING_BOUNDARY_TREATED_AS_FOLLOW_ON_WORK",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RUNTIME_HOSTING_BOUNDARY_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_MALFORMED",
    "DECLARED_RUNTIME_HOSTING_BOUNDARY_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "post_successor_runtime_step_runtime_hosting_boundary_metadata",
    "declared_runtime_hosting_boundary_question",
    "selected_successor_runtime_step_basis",
    "selected_successor_runtime_step_terminal_summary_basis",
    "selected_successor_runtime_step_boundary_basis",
    "selected_minimal_runtime_basis",
    "selected_runtime_boundary_basis",
    "selected_runtime_readiness_basis",
    "selected_portable_verification_final_completion_basis",
    "selected_post_portable_verification_currentness_basis",
    "selected_returned_second_carrier_capture_lineage_basis",
    "runtime_hosting_boundary_spec_only_posture",
    "one_future_runtime_hosting_review_posture",
    "successor_runtime_step_basis_preserved_posture",
    "successor_runtime_step_not_runtime_hosting_posture",
    "bounded_successor_runtime_result_or_refusal_not_hosting_authorization_posture",
    "runtime_hosting_boundary_not_runtime_hosting_posture",
    "runtime_hosting_boundary_not_ongoing_runtime_posture",
    "runtime_hosting_boundary_not_reusable_runtime_permission_posture",
    "runtime_hosting_boundary_not_continuation_posture",
    "runtime_hosting_not_created_posture",
    "ongoing_runtime_not_created_posture",
    "reusable_runtime_permission_not_created_posture",
    "continuation_not_authorized_posture",
    "self_continuation_not_authorized_posture",
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
    "repo_local_availability_not_runtime_hosting_boundary_authority_posture",
    "artifact_existence_not_runtime_hosting_boundary_authority_posture",
    "latest_file_posture_not_runtime_hosting_boundary_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "runtime_hosting_boundary_scope",
    "runtime_hosting_boundary_checks",
    "runtime_hosting_boundary_statement",
    "runtime_hosting_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "post_successor_runtime_step_runtime_hosting_boundary_summary",
)

TRUE_STATEMENT_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)

SENTINELS = (
    "RAW_RUNTIME_HOSTING_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_HOSTING_BODY_MUST_NOT_RETURN",
    "RAW_ONGOING_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_DAEMON_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_LOOP_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)


def build_request(**overrides) -> dict:
    return resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request(
        **overrides
    )


def resolve(request: Mapping | None = None) -> dict:
    return resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_v2(request)


def summary(result: Mapping) -> dict:
    return resolver.build_post_successor_runtime_step_runtime_hosting_boundary_v2_summary(result)


def metadata(result: Mapping) -> Mapping:
    return result["post_successor_runtime_step_runtime_hosting_boundary_metadata"]


def statement(result: Mapping) -> Mapping:
    return result["runtime_hosting_boundary_statement"]


def non_claims(result: Mapping) -> Mapping:
    return result["non_claims"]


def checks(result: Mapping) -> list:
    return result["runtime_hosting_boundary_checks"]


class PostSuccessorRuntimeStepRuntimeHostingBoundaryV2Tests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping) -> None:
        block = result.get("block")
        if isinstance(block, Mapping) and block.get("block_code") is not None:
            self.assertIn(block["block_code"], resolver.BLOCK_CODES)
        for check in checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: Mapping) -> None:
        emitted = non_claims(result)
        self.assertEqual(set(emitted), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, emitted)
            self.assertIs(emitted[key], False, key)
            self.assertIs(type(emitted[key]), bool, key)

    def assert_safe_boundary_posture(self, result: Mapping) -> None:
        emitted = non_claims(result)
        for key in (
            "runtime_hosting_created",
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
            "source_created",
            "authority_created",
            "currentness_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
            "consumed_request_reopened",
            "authorization_token_reused",
        ):
            self.assertIs(emitted[key], False, key)

    def assert_no_sentinels(self, result: Mapping) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_scope_preserved(self, result: Mapping) -> None:
        scope = result["runtime_hosting_boundary_scope"]
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, scope)
        self.assertNotIn("[bounded-runtime-hosting-boundary-redacted]", scope)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", scope)
        for value in resolver.SUPPORTED_SCOPE_VALUES:
            self.assertIn(value, scope)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_v2",
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path",
            "write_post_successor_runtime_step_runtime_hosting_boundary_v2_result",
            "build_post_successor_runtime_step_runtime_hosting_boundary_v2_summary",
            "build_declared_post_successor_runtime_step_runtime_hosting_boundary_v2_request",
            "resolve_post_successor_runtime_step_runtime_hosting_boundary",
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_from_path",
            "write_post_successor_runtime_step_runtime_hosting_boundary_result",
            "build_post_successor_runtime_step_runtime_hosting_boundary_summary",
            "build_declared_post_successor_runtime_step_runtime_hosting_boundary_request",
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
            "SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_v2",
        )
        self.assertEqual(
            resolver.SUPPORTED_RUNTIME_HOSTING_BOUNDARY_SCOPE,
            resolver.SUPPORTED_SCOPE_VALUES,
        )
        self.assertTrue(resolver.OUTPUT_ROOT.as_posix().endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        self.assertNotEqual(resolver.OUTPUT_ROOT.as_posix(), V1_OUTPUT_ROOT_SUFFIX)

        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

        alias_result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary(
            resolver.build_declared_post_successor_runtime_step_runtime_hosting_boundary_request()
        )
        alias_summary = resolver.build_post_successor_runtime_step_runtime_hosting_boundary_summary(
            alias_result
        )
        self.assertEqual(alias_summary["result_version"], "0.2.0")
        self.assertEqual(
            alias_summary["resolver_module"],
            "resolve_post_successor_runtime_step_runtime_hosting_boundary_v2",
        )

    def test_no_argument_builder_records_cleanly(self) -> None:
        request = build_request()
        result = resolve(request)
        result_summary = summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIsNone(result["block"])
        self.assertEqual(result_summary["failed_check_count"], 0)
        self.assertGreater(result_summary["passed_check_count"], 0)
        self.assertEqual(result_summary["result_version"], "0.2.0")
        self.assertEqual(result_summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            metadata(result)["post_successor_runtime_step_runtime_hosting_boundary_id"],
            request["runtime_hosting_boundary_request_id"],
        )

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result, section)
        for field in TRUE_STATEMENT_FIELDS:
            self.assertIn(field, statement(result))
            self.assertIs(statement(result)[field], True, field)
            self.assertIs(type(statement(result)[field]), bool, field)

        self.assert_canonical_non_claims(result)
        self.assert_public_codes(result)
        self.assert_safe_boundary_posture(result)

    def test_each_flipped_declared_non_claim_blocks_but_output_stays_canonical(self) -> None:
        explicit_named_keys = {
            "runtime_hosting_boundary_treated_as_runtime_hosting",
            "runtime_hosting_boundary_treated_as_ongoing_runtime",
            "runtime_hosting_boundary_treated_as_reusable_runtime_permission",
            "runtime_hosting_boundary_treated_as_continuation",
            "runtime_hosting_boundary_treated_as_self_continuation",
            "runtime_hosting_boundary_treated_as_source_transfer",
            "runtime_hosting_boundary_treated_as_source_receipt",
            "runtime_hosting_boundary_treated_as_reception_authorization",
            "runtime_hosting_boundary_treated_as_source",
            "runtime_hosting_boundary_treated_as_authority",
            "runtime_hosting_boundary_treated_as_currentness",
            "runtime_hosting_boundary_treated_as_deployment",
            "runtime_hosting_boundary_treated_as_public_release",
            "runtime_hosting_boundary_treated_as_operation_permission",
            "runtime_hosting_boundary_treated_as_reusable_permission",
            "runtime_hosting_boundary_treated_as_follow_on_work",
            "successor_runtime_step_treated_as_runtime_hosting",
            "successor_runtime_step_treated_as_ongoing_runtime",
            "successor_runtime_step_treated_as_reusable_runtime_permission",
            "successor_runtime_step_treated_as_continuation",
            "successor_runtime_step_treated_as_self_continuation",
            "bounded_successor_runtime_result_or_refusal_authorized_hosting",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(explicit_named_keys.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))

        clean = build_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = copy.deepcopy(clean)
                request["declared_non_claims"][key] = True
                result = resolve(request)

                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIsNotNone(result["block"])
                self.assertIn(result["block"]["block_code"], resolver.BLOCK_CODES)
                self.assertTrue(any(not check["passed"] for check in checks(result)))
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)
                self.assertIs(non_claims(result)[key], False)
                self.assert_safe_boundary_posture(result)

    def test_missing_or_incomplete_declared_non_claims_do_not_leak_to_output(self) -> None:
        variants: list[tuple[str, dict]] = []
        request = build_request()
        removed = copy.deepcopy(request)
        removed.pop("declared_non_claims")
        variants.append(("missing declared_non_claims", removed))
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
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_codes(result)
                self.assert_canonical_non_claims(result)
                self.assert_safe_boundary_posture(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolve(build_request())
        self.assert_official_scope_preserved(result)

    def test_raw_and_hidden_hostile_content_is_contained_without_mutation(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        raw_keys = (
            "raw_body",
            "raw_full_body",
            "full_body",
            "artifact_body",
            "raw_runtime_hosting_boundary_body",
            "raw_runtime_hosting_body",
            "raw_ongoing_runtime_body",
            "raw_runtime_body",
            "runtime_hosting_boundary_body",
            "runtime_hosting_body",
            "ongoing_runtime_body",
            "runtime_body",
            "hidden_repo_state",
            "current_working_tree",
            "local_cache",
            "repo_local_only_dependency",
        )
        basis_sections = (
            "selected_successor_runtime_step_basis",
            "selected_successor_runtime_step_terminal_summary_basis",
            "selected_successor_runtime_step_boundary_basis",
            "selected_minimal_runtime_basis",
            "selected_runtime_boundary_basis",
            "selected_runtime_readiness_basis",
            "selected_portable_verification_final_completion_basis",
            "selected_post_portable_verification_currentness_basis",
            "selected_returned_second_carrier_capture_lineage_basis",
        )
        for section in basis_sections:
            for index, raw_key in enumerate(raw_keys):
                request[section][raw_key] = SENTINELS[index % len(SENTINELS)]
            request[section]["nested"] = {"payload": list(SENTINELS)}
        hostile_original = copy.deepcopy(request)

        result = resolve(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_public_codes(result)
        self.assert_no_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_canonical_non_claims(result)
        self.assert_safe_boundary_posture(result)
        self.assertEqual(request, hostile_original)

        for section in basis_sections:
            self.assertNotEqual(request[section], original[section])
        clean_again = build_request()
        self.assertEqual(original, clean_again)

    def test_path_and_write_behavior_are_v2_contained(self) -> None:
        request = build_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path(
                request_path
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary(result)["result_version"], "0.2.0")
            self.assertEqual(summary(result)["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(malformed)
            self.assert_canonical_non_claims(malformed)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(array_result)
            self.assert_canonical_non_claims(array_result)

            missing = resolver.resolve_post_successor_runtime_step_runtime_hosting_boundary_v2_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_codes(missing)
            self.assert_canonical_non_claims(missing)

            redirected_root = tmp_path / "artifacts" / "post_successor_runtime_step_runtime_hosting_boundary_v2"
            with mock.patch.object(resolver, "OUTPUT_ROOT", redirected_root):
                first = resolver.write_post_successor_runtime_step_runtime_hosting_boundary_v2_result(result)
                second = resolver.write_post_successor_runtime_step_runtime_hosting_boundary_v2_result(result)

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("post_successor_runtime_step_runtime_hosting_boundary_v2", first.as_posix())
            forbidden_fragments = (
                "post_successor_runtime_step_runtime_hosting_boundary/",
                "successor_runtime_step/post",
                "successor_runtime_step_boundary",
                "minimal_runtime",
                "runtime_boundary",
                "runtime_readiness",
                "final_completion",
                "portable_verification",
                "runtime-hosting",
                "ongoing-runtime",
                "deployment",
                "public-release",
                "source-transfer",
                "source-receipt",
                "reception",
            )
            for fragment in forbidden_fragments:
                self.assertNotIn(fragment, first.as_posix())

    def test_resolver_does_not_mutate_input_request(self) -> None:
        request = build_request()
        original = copy.deepcopy(request)
        result = resolve(request)
        self.assertEqual(request, original)
        self.assert_canonical_non_claims(result)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve(build_request())
        result_summary = summary(result)
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

    def test_canonical_non_claims_for_all_outcome_family_members(self) -> None:
        recorded = resolve(build_request())
        blocked_request = build_request()
        blocked_request["declared_non_claims"]["runtime_hosting_created"] = True
        blocked = resolve(blocked_request)
        not_recorded_request = build_request(
            requested_runtime_hosting_boundary_outcome=resolver.OUTCOME_NOT_RECORDED
        )
        not_recorded = resolve(not_recorded_request)
        additional_request = build_request(
            requested_runtime_hosting_boundary_outcome=resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
        )
        additional = resolve(additional_request)

        expected = (
            (resolver.OUTCOME_RECORDED, recorded),
            (resolver.OUTCOME_BLOCKED, blocked),
            (resolver.OUTCOME_NOT_RECORDED, not_recorded),
            (resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS, additional),
        )
        for outcome, result in expected:
            with self.subTest(outcome=outcome):
                self.assertEqual(result["outcome"], outcome)
                self.assert_canonical_non_claims(result)
                self.assert_safe_boundary_posture(result)


if __name__ == "__main__":
    unittest.main()
