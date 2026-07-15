"""Executable tests for the bounded relevance receipt resolver.

This suite is bounded to one inspectable bounded relevance receipt object. The
receipt object points to the upstream bounded relevance reception artifact and
preserves signal, basis, scope, carrier-context, and envelope identifiers
without expanding reception.

These tests do not create source transfer, source receipt, reception
authorization, source, authority, currentness, truth, action, synchronization,
participation authorization, participant role, runtime permission, public API,
participant-facing interface, distributed network behavior, deployment, public
release, operation permission, broader reusable permission, adoption,
receiving-context governance, publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_bounded_relevance_receipt_v0_min as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "bounded_relevance_reception_v0_min",
    "post_runtime_loop_internal_runtime_layer_closure",
    "post_runtime_daemon_runtime_loop/",
    "source-transfer",
    "source-receipt",
    "reception/",
    "public-api",
    "participant-facing-interface",
    "distributed-network",
    "deployment/",
    "public-release",
)

TOP_LEVEL_SECTIONS = (
    "bounded_relevance_receipt_metadata",
    "declared_bounded_relevance_receipt_question",
    "selected_bounded_relevance_reception_artifact_basis",
    "receipt_object",
    "bounded_relevance_receipt_checks",
    "bounded_relevance_receipt_statement",
    "bounded_relevance_receipt_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "bounded_relevance_receipt_summary",
)

RECEIPT_OBJECT_FIELDS = (
    "receipt_id",
    "receipt_type",
    "receipt_version",
    "received_relevance_artifact",
    "received_relevance_artifact_outcome",
    "received_relevance_artifact_result_version",
    "received_relevance_artifact_failed_check_count",
    "received_signal_id",
    "received_relevance_basis_id",
    "received_relevance_scope_id",
    "received_carrier_context_id",
    "received_reception_envelope_id",
    "receipt_scope",
    "does_not_expand_reception",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "follow_on_work_authorized",
)

RECEIPT_OBJECT_WRAPPER_KEYS = (
    "outcome",
    "block",
    "bounded_relevance_receipt_checks",
    "non_claims",
    "bounded_relevance_receipt_summary",
    "bounded_relevance_receipt_metadata",
)

EXPECTED_BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEIPT_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEIPT_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEIPT_BLOCK_REQUESTED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "BOUNDED_RELEVANCE_RECEPTION_ARTIFACT_VERSION_NOT_0_1_0",
    "BOUNDED_RELEVANCE_RECEPTION_SIGNAL_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_BASIS_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SCOPE_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_CARRIER_CONTEXT_ID_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_ID_MISSING",
    "RECEIPT_SCOPE_MISSING",
    "RECEIPT_SCOPE_NOT_INSPECTABLE_ONLY",
    "RECEIPT_EXPANDS_RECEPTION",
    "RECEIPT_CREATED_NEW_SIGNAL",
    "RECEIPT_CREATED_NEW_RELEVANCE_BASIS",
    "RECEIPT_CREATED_NEW_RELEVANCE_SCOPE",
    "RECEIPT_CREATED_NEW_CARRIER_CONTEXT",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_RECEIPT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_RECEIPT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_RECEIPT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_RECEIPT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_MALFORMED",
    "DECLARED_BOUNDED_RELEVANCE_RECEIPT_REQUEST_UNREADABLE",
)

HOSTILE_SENTINELS = (
    "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

HOSTILE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_bounded_relevance_receipt_body",
    "raw_bounded_relevance_reception_body",
    "raw_receipt_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "bounded_relevance_receipt_body",
    "bounded_relevance_reception_body",
    "receipt_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)


def clean_request() -> dict[str, Any]:
    return resolver.build_declared_bounded_relevance_receipt_v0_min_request()


def resolve_request(request: dict[str, Any] | None = None) -> dict[str, Any]:
    return resolver.resolve_bounded_relevance_receipt_v0_min(clean_request() if request is None else request)


class BoundedRelevanceReceiptResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: dict[str, Any]) -> None:
        block = result.get("block") or {}
        for key in ("code", "block_code"):
            code = block.get(key)
            if code:
                self.assertIn(code, resolver.BLOCK_CODES)
        for code in block.get("failed_block_codes", []):
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("bounded_relevance_receipt_checks", []):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIsInstance(non_claims[key], bool, key)

    def assert_bool_fields_are_bool(self, result: dict[str, Any]) -> None:
        for section_name in ("bounded_relevance_receipt_statement", "non_claims"):
            for key, value in result[section_name].items():
                self.assertIsInstance(value, bool, f"{section_name}.{key}")
        receipt_object = result.get("receipt_object") or {}
        for key, value in receipt_object.items():
            if key in resolver.REQUIRED_FALSE_NON_CLAIMS or key == "does_not_expand_reception":
                self.assertIsInstance(value, bool, key)

    def assert_receipt_object_is_small(self, result: dict[str, Any]) -> None:
        receipt_object = result.get("receipt_object")
        self.assertIsInstance(receipt_object, dict)
        for key in RECEIPT_OBJECT_WRAPPER_KEYS:
            self.assertNotIn(key, receipt_object)
        if result.get("outcome") == resolver.OUTCOME_RECORDED:
            self.assertEqual(set(receipt_object), set(RECEIPT_OBJECT_FIELDS))

    def assert_no_created_posture(self, result: dict[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        receipt_object = result.get("receipt_object") or {}
        if receipt_object:
            self.assertIs(receipt_object["does_not_expand_reception"], True)
            for key in (
                "source_transfer_occurred",
                "source_receipt_occurred",
                "reception_authorization_created",
                "source_created",
                "authority_created",
                "currentness_created",
                "truth_created",
                "action_created",
                "synchronization_created",
                "participation_authorized",
                "participant_role_created",
                "runtime_permission_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "deployment_created",
                "public_release_created",
                "operation_permission_created",
                "follow_on_work_authorized",
            ):
                self.assertIs(receipt_object[key], False, key)

    def assert_no_hostile_sentinels(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in HOSTILE_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_official_values_preserved(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn("INSPECTABLE_RECEIPT_ONLY", serialized)
        self.assertIn(str(result["outcome"]), serialized)
        self.assertIn(resolver.RESOLVER_MODULE, serialized)
        self.assertNotIn("[bounded-relevance-receipt-redacted]", serialized)
        self.assertNotIn("[bounded-redacted-raw-or-hidden-state]", serialized)

    def assert_blocked_public_and_safe(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertTrue(result["block"]["code"])
        self.assert_public_block_codes(result)
        self.assert_no_created_posture(result)
        self.assert_receipt_object_is_small(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_bounded_relevance_receipt_v0_min",
            "resolve_bounded_relevance_receipt_v0_min_from_path",
            "write_bounded_relevance_receipt_v0_min_result",
            "build_bounded_relevance_receipt_v0_min_summary",
            "build_declared_bounded_relevance_receipt_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTPUT_ROOT",
            "SUPPORTED_RECEIPT_SCOPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_bounded_relevance_receipt_v0_min")
        output_root = str(resolver.OUTPUT_ROOT)
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        self.assertIn("INSPECTABLE_RECEIPT_ONLY", resolver.SUPPORTED_RECEIPT_SCOPE_VALUES)
        for code in EXPECTED_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = clean_request()
        result = resolver.resolve_bounded_relevance_receipt_v0_min(request)
        summary = resolver.build_bounded_relevance_receipt_v0_min_summary(result)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(result["block"]["code"])
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(
            result["bounded_relevance_receipt_metadata"]["bounded_relevance_receipt_id"],
            request["bounded_relevance_receipt_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        receipt_object = result["receipt_object"]
        self.assertEqual(receipt_object["receipt_id"], "bounded_relevance_receipt_001")
        self.assertEqual(receipt_object["receipt_type"], "bounded_relevance_receipt")
        self.assertEqual(receipt_object["receipt_version"], "0.1.0")
        self.assertTrue(
            receipt_object["received_relevance_artifact"].endswith(
                "bounded_relevance_reception_reference_review_001__bounded_relevance_reception_v0_min_result.json"
            )
        )
        self.assertEqual(receipt_object["received_relevance_artifact_outcome"], "BOUNDED_RELEVANCE_RECEPTION_RECORDED")
        self.assertEqual(receipt_object["received_relevance_artifact_result_version"], "0.1.0")
        self.assertEqual(receipt_object["received_relevance_artifact_failed_check_count"], 0)
        self.assertEqual(receipt_object["received_signal_id"], "bounded_relevance_signal_001")
        self.assertEqual(receipt_object["received_relevance_basis_id"], "bounded_relevance_basis_001")
        self.assertEqual(receipt_object["received_relevance_scope_id"], "bounded_relevance_scope_001")
        self.assertEqual(receipt_object["received_carrier_context_id"], "bounded_relevance_signal_carrier_context_001")
        self.assertEqual(receipt_object["received_reception_envelope_id"], "bounded_relevance_reception_envelope_v0")
        self.assertEqual(receipt_object["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        self.assertIs(receipt_object["does_not_expand_reception"], True)
        for key in (
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "deployment_created",
            "public_release_created",
            "operation_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(receipt_object[key], False, key)

        self.assert_receipt_object_is_small(result)
        statement = result["bounded_relevance_receipt_statement"]
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(statement[key], True, key)
        self.assert_non_claims_canonical_false(result)
        self.assert_bool_fields_are_bool(result)
        self.assert_public_block_codes(result)

    def test_critical_non_claim_canonicalization(self) -> None:
        base_request = clean_request()
        named_keys = (
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "participation_authorized",
            "participant_role_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "receipt_expanded_reception",
            "receipt_created_new_signal",
            "receipt_created_new_relevance_basis",
            "receipt_created_new_relevance_scope",
            "receipt_created_new_carrier_context",
            "artifact_existence_treated_as_receipt_authority",
            "latest_file_posture_treated_as_receipt_authority",
            "repo_local_availability_treated_as_receipt_authority",
            "hidden_repo_state_used_as_receipt_content",
            "hidden_repo_state_used_as_receipt_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        )
        self.assertTrue(set(named_keys).issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = copy.deepcopy(base_request)
                request["declared_non_claims"][key] = True
                result = resolver.resolve_bounded_relevance_receipt_v0_min(request)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertTrue(result["block"]["code"])
                self.assert_public_block_codes(result)
                failed = [check for check in result["bounded_relevance_receipt_checks"] if not check["passed"]]
                self.assertTrue(failed)
                self.assertIs(result["non_claims"][key], False)
                self.assert_non_claims_canonical_false(result)
                self.assert_no_created_posture(result)
                self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
                self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
                self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)

    def test_representative_blocking_behavior(self) -> None:
        def remove(key: str):
            return lambda request: request.pop(key, None)

        cases: tuple[tuple[str, Any], ...] = (
            ("explicit block intent", lambda request: request.update({"bounded_relevance_receipt_intent": resolver.INTENT_BLOCK})),
            ("missing request", lambda request: request.clear()),
            ("non-mapping request", ["not", "a", "mapping"]),
            ("unsupported intent", lambda request: request.update({"bounded_relevance_receipt_intent": "UNSUPPORTED"})),
            ("artifact missing", lambda request: request.update({"selected_bounded_relevance_reception_artifact_missing": True})),
            ("artifact not recorded", lambda request: request.update({"selected_bounded_relevance_reception_artifact_not_recorded": True})),
            ("artifact failed checks present", lambda request: request.update({"selected_bounded_relevance_reception_artifact_failed_checks_present": True})),
            ("artifact version wrong", lambda request: request.update({"selected_bounded_relevance_reception_artifact_result_version": "0.2.0"})),
            ("missing signal id", remove("selected_bounded_relevance_reception_signal_id")),
            ("missing basis id", remove("selected_bounded_relevance_reception_basis_id")),
            ("missing scope id", remove("selected_bounded_relevance_reception_scope_id")),
            ("missing carrier context id", remove("selected_bounded_relevance_reception_carrier_context_id")),
            ("missing envelope id", remove("selected_bounded_relevance_reception_envelope_id")),
            ("missing receipt scope", remove("receipt_scope")),
            ("receipt scope not inspectable", lambda request: request.update({"receipt_scope": "BROAD_RECEIPT"})),
            ("receipt expands reception", lambda request: request.update({"receipt_expands_reception": True})),
            ("new signal", lambda request: request.update({"receipt_creates_new_signal": True})),
            ("new basis", lambda request: request.update({"receipt_creates_new_relevance_basis": True})),
            ("new scope", lambda request: request.update({"receipt_creates_new_relevance_scope": True})),
            ("new carrier context", lambda request: request.update({"receipt_creates_new_carrier_context": True})),
            ("source transfer", lambda request: request.update({"source_transfer_occurred": True})),
            ("source receipt", lambda request: request.update({"source_receipt_occurred": True})),
            ("reception authorization", lambda request: request.update({"reception_authorization_created": True})),
            ("source", lambda request: request.update({"source_created": True})),
            ("authority", lambda request: request.update({"authority_created": True})),
            ("currentness", lambda request: request.update({"currentness_created": True})),
            ("truth", lambda request: request.update({"truth_created": True})),
            ("action", lambda request: request.update({"action_created": True})),
            ("synchronization", lambda request: request.update({"synchronization_created": True})),
            ("participation", lambda request: request.update({"participation_authorized": True})),
            ("participant role", lambda request: request.update({"participant_role_created": True})),
            ("runtime permission", lambda request: request.update({"runtime_permission_created": True})),
            ("public API", lambda request: request.update({"public_api_created": True})),
            ("participant interface", lambda request: request.update({"participant_facing_interface_created": True})),
            ("distributed network", lambda request: request.update({"distributed_network_behavior_created": True})),
            ("deployment", lambda request: request.update({"deployment_created": True})),
            ("public release", lambda request: request.update({"public_release_created": True})),
            ("operation permission", lambda request: request.update({"operation_permission_created": True})),
            ("broader reusable permission", lambda request: request.update({"broader_reusable_permission_created": True})),
            ("follow-on", lambda request: request.update({"follow_on_work_authorized": True})),
            ("artifact authority", lambda request: request.update({"artifact_existence_treated_as_receipt_authority": True})),
            ("latest authority", lambda request: request.update({"latest_file_posture_treated_as_receipt_authority": True})),
            ("repo-local authority", lambda request: request.update({"repo_local_availability_treated_as_receipt_authority": True})),
            ("hidden content", lambda request: request.update({"hidden_repo_state_used_as_receipt_content": True})),
            ("hidden authority", lambda request: request.update({"hidden_repo_state_used_as_receipt_authority": True})),
            ("predecessor repaired", lambda request: request.update({"predecessor_failure_repaired": True})),
            ("predecessor hidden", lambda request: request.update({"predecessor_failure_hidden": True})),
            ("predecessor claimed passed", lambda request: request.update({"predecessor_failure_claimed_passed": True})),
            ("consumed reopened", lambda request: request.update({"consumed_request_reopened": True})),
            ("authorization reused", lambda request: request.update({"authorization_token_reused": True})),
            ("nonclaim missing", lambda request: request["declared_non_claims"].pop("source_transfer_occurred")),
            ("nonclaim flipped", lambda request: request["declared_non_claims"].update({"authority_created": True})),
        )

        for name, mutate in cases:
            with self.subTest(block_case=name):
                if name == "non-mapping request":
                    result = resolver.resolve_bounded_relevance_receipt_v0_min(mutate)
                else:
                    request = clean_request()
                    mutate(request)
                    result = resolver.resolve_bounded_relevance_receipt_v0_min(request)
                self.assert_blocked_public_and_safe(result)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        variants = []
        request = clean_request()
        request.pop("declared_non_claims")
        variants.append(("missing declared_non_claims", request))
        request = clean_request()
        request["declared_non_claims"] = {}
        variants.append(("empty declared_non_claims", request))
        request = clean_request()
        request["declared_non_claims"].pop("source_transfer_occurred")
        variants.append(("one missing declared_non_claim", request))
        request = clean_request()
        request["declared_non_claims"]["authority_created"] = "false"
        variants.append(("non-bool declared_non_claim", request))
        request = clean_request()
        request["declared_non_claims"]["truth_created"] = None
        variants.append(("none declared_non_claim", request))

        for name, request in variants:
            with self.subTest(variant=name):
                result = resolver.resolve_bounded_relevance_receipt_v0_min(request)
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_block_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_official_values_are_preserved(self) -> None:
        result = resolve_request()
        self.assertEqual(result["receipt_object"]["receipt_scope"], "INSPECTABLE_RECEIPT_ONLY")
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        for outcome in (
            "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
            "BOUNDED_RELEVANCE_RECEIPT_NOT_RECORDED",
            "BOUNDED_RELEVANCE_RECEIPT_REQUIRES_ADDITIONAL_BASIS",
            "BOUNDED_RELEVANCE_RECEIPT_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assert_official_values_preserved(result)

    def test_raw_hidden_hostile_content_containment(self) -> None:
        request = clean_request()
        for index, key in enumerate(HOSTILE_KEYS):
            request[key] = HOSTILE_SENTINELS[index % len(HOSTILE_SENTINELS)]
        request["block_reason"] = {
            "raw_body": "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
            "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
        }
        request["bounded_relevance_receipt_intent"] = resolver.INTENT_BLOCK
        original = copy.deepcopy(request)

        result = resolver.resolve_bounded_relevance_receipt_v0_min(request)

        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertEqual(request, original)
        self.assert_no_hostile_sentinels(result)
        self.assert_official_values_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(clean_request()), encoding="utf-8")

            result = resolver.resolve_bounded_relevance_receipt_v0_min_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(result["bounded_relevance_receipt_metadata"]["bounded_relevance_receipt_version"], "0.1.0")
            self.assertEqual(result["bounded_relevance_receipt_metadata"]["resolver_module"], resolver.RESOLVER_MODULE)

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_bounded_relevance_receipt_v0_min_from_path(malformed_path)
            self.assertEqual(malformed["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(malformed)

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_bounded_relevance_receipt_v0_min_from_path(array_path)
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(array_result)

            missing = resolver.resolve_bounded_relevance_receipt_v0_min_from_path(tmp_path / "missing.json")
            self.assertEqual(missing["outcome"], resolver.OUTCOME_BLOCKED)
            self.assert_public_block_codes(missing)

            output_root = tmp_path / "artifacts" / "bounded_relevance_receipt_v0_min"
            with mock.patch.object(resolver, "OUTPUT_ROOT", output_root):
                first_path = resolver.write_bounded_relevance_receipt_v0_min_result(result)
                second_path = resolver.write_bounded_relevance_receipt_v0_min_result(result)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(first_path.parent.exists())
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn("bounded_relevance_receipt_v0_min", str(first_path))
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, str(first_path))

    def test_non_mutation(self) -> None:
        request = clean_request()
        request["nested_payload"] = {
            "raw_body": "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
            "selected": {
                "signal_id": request["selected_bounded_relevance_reception_signal_id"],
                "basis_id": request["selected_bounded_relevance_reception_basis_id"],
                "scope_id": request["selected_bounded_relevance_reception_scope_id"],
                "context_id": request["selected_bounded_relevance_reception_carrier_context_id"],
                "envelope_id": request["selected_bounded_relevance_reception_envelope_id"],
                "receipt_scope": request["receipt_scope"],
            },
        }
        original = copy.deepcopy(request)
        result = resolver.resolve_bounded_relevance_receipt_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(request, original)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolve_request()
        summary = resolver.build_bounded_relevance_receipt_v0_min_summary(result)
        self.assertTrue(summary["predecessor_failure_evidence_preserved"])
        self.assertIs(result["non_claims"]["predecessor_failure_repaired"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_hidden"], False)
        self.assertIs(result["non_claims"]["predecessor_failure_claimed_passed"], False)
        self.assertIs(result["non_claims"]["consumed_request_reopened"], False)
        self.assertIs(result["non_claims"]["authorization_token_reused"], False)
        self.assertIs(summary["key_non_claims"]["consumed_request_reopened"], False)
        self.assertIs(summary["key_non_claims"]["authorization_token_reused"], False)


if __name__ == "__main__":
    unittest.main()
