"""Executable tests for the bounded relevance reception resolver.

This suite is bounded to bounded relevance reception only. The post-runtime-loop
bounded relevance reception selection is upstream basis, runtime-layer closure is
controlling basis, runtime loop is upstream basis, and carrier-aware /
distributed anatomy remains upstream basis only.

These tests do not create relevance receipt, source transfer, source receipt,
reception authorization, source, authority, currentness, truth, action,
synchronization, inhabitance, runtime permission, public API,
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
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_bounded_relevance_reception_v0_min as resolver  # noqa: E402


EXPECTED_OUTPUT_ROOT_SUFFIX = (
    "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min"
)

FORBIDDEN_OUTPUT_ROOT_FRAGMENTS = (
    "post_runtime_loop_bounded_relevance_reception_selection",
    "post_runtime_loop_internal_runtime_layer_closure",
    "post_runtime_daemon_runtime_loop/",
    "post_runtime_daemon_runtime_loop_boundary/",
    "post_self_recursive_growth_runtime_daemon/",
    "post_self_recursive_growth_runtime_daemon_boundary/",
    "source-transfer",
    "source-receipt",
    "reception/",
    "relevance-receipt",
    "public-api",
    "participant-facing-interface",
    "distributed-network",
    "deployment/",
    "public-release",
)

OFFICIAL_SCOPE_VALUES = (
    "BOUNDED_RELEVANCE_RECEPTION_SPEC_ONLY",
    "ONE_BOUNDED_RELEVANCE_RECEPTION_POSTURE_RECORDED",
    "BOUNDED_RELEVANCE_SIGNAL_DECLARED",
    "BOUNDED_RELEVANCE_RECEPTION_ENVELOPE_DECLARED",
    "RUNTIME_LAYER_CLOSURE_BASIS_PRESERVED",
    "RUNTIME_LOOP_BASIS_PRESERVED",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_PRESERVED",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_PRESERVED",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SOURCE_TRANSFER",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SOURCE_RECEIPT",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_RECEPTION_AUTHORIZATION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_AUTHORITY",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_CURRENTNESS",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_TRUTH",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_ACTION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_SYNCHRONIZATION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_INHABITANCE",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_RUNTIME_PERMISSION",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_PUBLIC_API",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RELEVANCE_RECEPTION_NOT_DISTRIBUTED_NETWORK_BEHAVIOR",
    "NO_SOURCE_TRANSFER",
    "NO_SOURCE_RECEIPT",
    "NO_RECEPTION_AUTHORIZATION",
    "NO_SOURCE_CREATED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_TRUTH_CREATED",
    "NO_ACTION_CREATED",
    "NO_SYNCHRONIZATION_CREATED",
    "NO_INHABITANCE_CREATED",
    "NO_RUNTIME_PERMISSION_CREATED",
    "NO_PUBLIC_API_CREATED",
    "NO_PARTICIPANT_FACING_INTERFACE_CREATED",
    "NO_DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "REPO_LOCAL_AVAILABILITY_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "ARTIFACT_EXISTENCE_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "LATEST_FILE_POSTURE_NOT_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_NOT_RETURNED",
    "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED",
    "HOSTILE_RAW_BODY_CONTENT_CONTAINED",
    "PREDECESSOR_FAILURE_EVIDENCE_PRESERVED",
    "RESULT_LEVEL_NON_CLAIMS_CANONICAL_FALSE",
)

REPRESENTATIVE_BLOCK_CODES = (
    "BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
    "BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_BASIS_MISSING",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_NOT_RECORDED",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_ALREADY_CREATED_RECEPTION",
    "BOUNDED_RELEVANCE_RECEPTION_SELECTION_AUTHORIZED_MECHANISM",
    "RUNTIME_LAYER_CLOSURE_BASIS_MISSING",
    "RUNTIME_LAYER_CLOSURE_NOT_RECORDED",
    "RUNTIME_LAYER_CLOSURE_DID_NOT_CLOSE_INTERNAL_RUNTIME_STACK",
    "RUNTIME_LAYER_CLOSURE_SELECTED_PUBLIC_API",
    "RUNTIME_LAYER_CLOSURE_SELECTED_PARTICIPANT_INTERFACE",
    "RUNTIME_LAYER_CLOSURE_SELECTED_DISTRIBUTED_NETWORK",
    "RUNTIME_LAYER_CLOSURE_SELECTED_SOURCE_AUTHORITY_CURRENTNESS",
    "RUNTIME_LAYER_CLOSURE_SELECTED_DEPLOYMENT_OPERATION",
    "RUNTIME_LAYER_CLOSURE_AUTHORIZED_FOLLOW_ON_WORK",
    "RUNTIME_LOOP_BASIS_MISSING",
    "RUNTIME_LOOP_NOT_RECORDED",
    "RUNTIME_LOOP_FAILED_CHECKS_PRESENT",
    "RUNTIME_LOOP_VERSION_NOT_0_1_0",
    "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_POSTURE",
    "RUNTIME_LOOP_DID_NOT_RECORD_BOUNDED_RUNTIME_LOOP_ENVELOPE",
    "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_API",
    "RUNTIME_LOOP_ALREADY_CREATED_PARTICIPANT_FACING_INTERFACE",
    "RUNTIME_LOOP_ALREADY_CREATED_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RUNTIME_LOOP_ALREADY_CREATED_SOURCE",
    "RUNTIME_LOOP_ALREADY_CREATED_AUTHORITY",
    "RUNTIME_LOOP_ALREADY_CREATED_CURRENTNESS",
    "RUNTIME_LOOP_ALREADY_CREATED_DEPLOYMENT",
    "RUNTIME_LOOP_ALREADY_CREATED_PUBLIC_RELEASE",
    "RUNTIME_LOOP_ALREADY_CREATED_OPERATION_PERMISSION",
    "RUNTIME_LOOP_AUTHORIZED_FOLLOW_ON_WORK",
    "BOUNDED_RUNTIME_LOOP_ENVELOPE_TREATED_AS_RECEPTION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_ACTION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_SYNCHRONIZATION_AUTHORITY",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_RUNTIME_PERMISSION",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PUBLIC_API",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_PARTICIPANT_INTERFACE",
    "CARRIER_AWARE_DISTRIBUTED_ANATOMY_BASIS_TREATED_AS_DISTRIBUTED_NETWORK",
    "BOUNDED_RELEVANCE_SIGNAL_MISSING",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SOURCE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_AUTHORITY",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_CURRENTNESS",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_TRUTH",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_ACTION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_SYNCHRONIZATION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_INHABITANCE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_RUNTIME_PERMISSION",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PUBLIC_API",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_PARTICIPANT_FACING_INTERFACE",
    "BOUNDED_RELEVANCE_SIGNAL_TREATED_AS_DISTRIBUTED_NETWORK_BEHAVIOR",
    "RELEVANCE_BASIS_MISSING",
    "RELEVANCE_BASIS_TREATED_AS_TRUTH",
    "RELEVANCE_BASIS_TREATED_AS_AUTHORITY",
    "RELEVANCE_SCOPE_MISSING",
    "RELEVANCE_SCOPE_UNBOUNDED",
    "BOUNDED_RELEVANCE_RECEPTION_RECORDED_BEFORE_REVIEW",
    "RELEVANCE_RECEIPT_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "INHABITANCE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "LATEST_FILE_POSTURE_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_BOUNDED_RELEVANCE_RECEPTION_AUTHORITY",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE",
    "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
    "DECLARED_BOUNDED_RELEVANCE_RECEPTION_REQUEST_UNREADABLE",
)

TOP_LEVEL_SECTIONS = (
    "bounded_relevance_reception_metadata",
    "declared_bounded_relevance_reception_question",
    "selected_bounded_relevance_reception_selection_basis",
    "selected_runtime_layer_closure_basis",
    "selected_runtime_loop_basis",
    "selected_runtime_loop_terminal_summary_basis",
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_carrier_aware_distributed_anatomy_basis",
    "selected_carrier_role_emission_basis",
    "selected_carrier_lifecycle_basis",
    "selected_registry_persistence_basis",
    "selected_cross_carrier_receipt_refusal_return_basis",
    "selected_divergence_basis",
    "selected_cross_carrier_currentness_caution_basis",
    "selected_standing_propagation_basis",
    "selected_distributed_standing_distinction_basis",
    "selected_synchronization_non_synchronization_basis",
    "selected_operation_admission_basis",
    "selected_execution_emission_boundary_basis",
    "selected_action_consequence_refusal_basis",
    "selected_distributed_chain_closure_basis",
    "bounded_relevance_reception_spec_only_posture",
    "one_bounded_relevance_reception_posture",
    "bounded_relevance_signal",
    "relevance_basis",
    "relevance_scope",
    "relevance_signal_carrier_context",
    "bounded_relevance_reception_envelope",
    "runtime_layer_closure_basis_preserved_posture",
    "runtime_loop_basis_preserved_posture",
    "bounded_runtime_loop_envelope_preserved_posture",
    "carrier_aware_distributed_anatomy_basis_preserved_posture",
    "bounded_relevance_reception_not_source_transfer_posture",
    "bounded_relevance_reception_not_source_receipt_posture",
    "bounded_relevance_reception_not_reception_authorization_posture",
    "bounded_relevance_reception_not_source_posture",
    "bounded_relevance_reception_not_authority_posture",
    "bounded_relevance_reception_not_currentness_posture",
    "bounded_relevance_reception_not_truth_posture",
    "bounded_relevance_reception_not_action_posture",
    "bounded_relevance_reception_not_synchronization_posture",
    "bounded_relevance_reception_not_inhabitance_posture",
    "bounded_relevance_reception_not_runtime_permission_posture",
    "bounded_relevance_reception_not_public_api_posture",
    "bounded_relevance_reception_not_participant_facing_interface_posture",
    "bounded_relevance_reception_not_distributed_network_behavior_posture",
    "source_transfer_not_created_posture",
    "source_receipt_not_created_posture",
    "reception_authorization_not_created_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "truth_not_created_posture",
    "action_not_created_posture",
    "synchronization_not_created_posture",
    "inhabitance_not_created_posture",
    "runtime_permission_not_created_posture",
    "public_api_not_created_posture",
    "participant_facing_interface_not_created_posture",
    "distributed_network_behavior_not_created_posture",
    "deployment_not_created_posture",
    "public_release_not_created_posture",
    "operation_permission_not_created_posture",
    "broader_reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_bounded_relevance_reception_authority_posture",
    "artifact_existence_not_bounded_relevance_reception_authority_posture",
    "latest_file_posture_not_bounded_relevance_reception_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "official_enum_scope_strings_not_redacted_posture",
    "hostile_raw_body_content_contained_posture",
    "predecessor_failure_evidence_preserved_posture",
    "result_level_non_claims_canonical_false_posture",
    "bounded_relevance_reception_scope",
    "bounded_relevance_reception_checks",
    "bounded_relevance_reception_statement",
    "bounded_relevance_reception_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "bounded_relevance_reception_summary",
)

STATEMENT_TRUE_FIELDS = (
    "bounded_relevance_reception_recorded",
    "bounded_relevance_reception_posture_recorded",
    "bounded_relevance_signal_declared",
    "bounded_relevance_reception_envelope_declared",
    "runtime_layer_closure_basis_preserved",
    "runtime_loop_basis_preserved",
    "bounded_runtime_loop_envelope_preserved",
    "carrier_aware_distributed_anatomy_basis_preserved",
    "bounded_relevance_reception_not_source_transfer",
    "bounded_relevance_reception_not_source_receipt",
    "bounded_relevance_reception_not_reception_authorization",
    "bounded_relevance_reception_not_source",
    "bounded_relevance_reception_not_authority",
    "bounded_relevance_reception_not_currentness",
    "bounded_relevance_reception_not_truth",
    "bounded_relevance_reception_not_action",
    "bounded_relevance_reception_not_synchronization",
    "bounded_relevance_reception_not_inhabitance",
    "bounded_relevance_reception_not_runtime_permission",
    "bounded_relevance_reception_not_public_api",
    "bounded_relevance_reception_not_participant_facing_interface",
    "bounded_relevance_reception_not_distributed_network_behavior",
    "source_transfer_not_created",
    "source_receipt_not_created",
    "reception_authorization_not_created",
    "source_not_created",
    "authority_not_created",
    "currentness_not_created",
    "truth_not_created",
    "action_not_created",
    "synchronization_not_created",
    "inhabitance_not_created",
    "runtime_permission_not_created",
    "public_api_not_created",
    "participant_facing_interface_not_created",
    "distributed_network_behavior_not_created",
    "deployment_not_created",
    "public_release_not_created",
    "operation_permission_not_created",
    "broader_reusable_permission_not_created",
    "follow_on_work_not_authorized",
    "hidden_repo_state_excluded",
    "hidden_repo_state_not_used_as_bounded_relevance_reception_authority",
    "repo_local_availability_not_bounded_relevance_reception_authority",
    "artifact_existence_not_bounded_relevance_reception_authority",
    "latest_file_posture_not_bounded_relevance_reception_authority",
    "selected_basis_reference_shape_preserved",
    "raw_full_prior_artifact_body_not_returned",
    "official_enum_scope_strings_not_redacted",
    "hostile_raw_body_content_contained",
    "predecessor_failure_evidence_preserved",
    "authorization_token_reuse_blocked",
    "consumed_request_token_remains_closed",
    "result_level_non_claims_canonical_false",
)

SENSITIVE_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_bounded_relevance_reception_body",
    "raw_bounded_relevance_signal_body",
    "raw_relevance_body",
    "raw_relevance_receipt_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_inhabitance_body",
    "raw_runtime_permission_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "bounded_relevance_reception_body",
    "bounded_relevance_signal_body",
    "relevance_body",
    "relevance_receipt_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "inhabitance_body",
    "runtime_permission_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
)

SENTINELS = (
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_SIGNAL_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_BODY_MUST_NOT_RETURN",
    "RAW_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_INHABITANCE_BODY_MUST_NOT_RETURN",
    "RAW_RUNTIME_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

BASIS_SECTIONS = (
    "selected_bounded_relevance_reception_selection_basis",
    "selected_runtime_layer_closure_basis",
    "selected_runtime_loop_basis",
    "selected_runtime_loop_terminal_summary_basis",
    "selected_runtime_loop_boundary_basis",
    "selected_runtime_daemon_basis",
    "selected_runtime_daemon_boundary_basis",
    "selected_runtime_daemon_boundary_v1_failure_lineage_basis",
    "selected_carrier_aware_distributed_anatomy_basis",
    "selected_carrier_role_emission_basis",
    "selected_carrier_lifecycle_basis",
    "selected_registry_persistence_basis",
    "selected_cross_carrier_receipt_refusal_return_basis",
    "selected_divergence_basis",
    "selected_cross_carrier_currentness_caution_basis",
    "selected_standing_propagation_basis",
    "selected_distributed_standing_distinction_basis",
    "selected_synchronization_non_synchronization_basis",
    "selected_operation_admission_basis",
    "selected_execution_emission_boundary_basis",
    "selected_action_consequence_refusal_basis",
    "selected_distributed_chain_closure_basis",
)


def _valid_request() -> dict[str, Any]:
    return resolver.build_declared_bounded_relevance_reception_v0_min_request()


def _checks(result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    checks = result.get("bounded_relevance_reception_checks")
    return checks if isinstance(checks, list) else []


def _statement(result: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = result.get("bounded_relevance_reception_statement")
    return statement if isinstance(statement, Mapping) else {}


def _non_claims(result: Mapping[str, Any]) -> Mapping[str, Any]:
    non_claims = result.get("non_claims")
    return non_claims if isinstance(non_claims, Mapping) else {}


def _summary(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return resolver.build_bounded_relevance_reception_v0_min_summary(result)


def _serialized(result: Mapping[str, Any]) -> str:
    return json.dumps(result, sort_keys=True)


def _block_code(result: Mapping[str, Any]) -> Any:
    block = result.get("block")
    if not isinstance(block, Mapping):
        return None
    return block.get("block_code") or block.get("code")


def _mutate_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request[field] = value

    return mutate


def _remove_field(field: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.pop(field, None)

    return mutate


def _remove_fields(*fields: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        for field in fields:
            request.pop(field, None)

    return mutate


def _mutate_envelope(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        envelope = request.setdefault("bounded_relevance_reception_envelope", {})
        if not isinstance(envelope, dict):
            envelope = {}
            request["bounded_relevance_reception_envelope"] = envelope
        envelope[field] = value

    return mutate


def _mutate_non_claim(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {})[field] = value

    return mutate


def _remove_non_claim(field: str) -> Callable[[dict[str, Any]], None]:
    def mutate(request: dict[str, Any]) -> None:
        request.setdefault("declared_non_claims", {}).pop(field, None)

    return mutate


def _resolve_mutated(mutate: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    request = _valid_request()
    mutate(request)
    return resolver.resolve_bounded_relevance_reception_v0_min(request)


class BoundedRelevanceReceptionResolverTests(unittest.TestCase):
    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        code = _block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in _checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_non_claims_canonical_false(self, result: Mapping[str, Any]) -> None:
        non_claims = _non_claims(result)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_statement_booleans_are_bools(self, result: Mapping[str, Any]) -> None:
        for key, value in _statement(result).items():
            self.assertIs(type(value), bool, key)
        block = result.get("block", {})
        if isinstance(block, Mapping) and "blocked" in block:
            self.assertIs(type(block["blocked"]), bool)

    def assert_no_created_posture(self, result: Mapping[str, Any]) -> None:
        self.assert_non_claims_canonical_false(result)
        non_claims = _non_claims(result)
        for key in (
            "relevance_receipt_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "inhabitance_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
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
            self.assertIs(non_claims[key], False, key)

    def assert_official_scope_preserved(self, result: Mapping[str, Any]) -> None:
        scope_section = result.get("bounded_relevance_reception_scope", {})
        self.assertIsInstance(scope_section, Mapping)
        selected_scope = scope_section.get("selected_scope", [])
        supported_scope = scope_section.get("supported_scope_values", [])
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, selected_scope)
            self.assertIn(value, supported_scope)
        for value in selected_scope:
            self.assertNotEqual(value, "[bounded-relevance-reception-redacted]")
            self.assertNotEqual(value, "[bounded-redacted-raw-or-hidden-state]")
        for value in resolver.SUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE:
            self.assertIn(value, supported_scope)

    def assert_no_raw_sentinels(self, result: Mapping[str, Any]) -> None:
        serialized = _serialized(result)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_recorded_cleanly(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = _summary(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertFalse(result["block"]["blocked"])
        self.assertIsNone(_block_code(result))
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_bounded_relevance_reception_v0_min")
        self.assert_public_codes(result)
        self.assert_statement_booleans_are_bools(result)
        self.assert_non_claims_canonical_false(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_bounded_relevance_reception_v0_min",
            "resolve_bounded_relevance_reception_v0_min_from_path",
            "write_bounded_relevance_reception_v0_min_result",
            "build_bounded_relevance_reception_v0_min_summary",
            "build_declared_bounded_relevance_reception_v0_min_request",
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
            "SUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_bounded_relevance_reception_v0_min")
        self.assertEqual(resolver.SUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE, resolver.SUPPORTED_SCOPE_VALUES)
        output_root = Path(resolver.OUTPUT_ROOT).as_posix()
        self.assertTrue(output_root.endswith(EXPECTED_OUTPUT_ROOT_SUFFIX))
        for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
            self.assertNotIn(fragment, output_root)
        for value in OFFICIAL_SCOPE_VALUES:
            self.assertIn(value, resolver.SUPPORTED_SCOPE_VALUES)
        for code in REPRESENTATIVE_BLOCK_CODES:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_recorded_result_from_no_argument_builder(self) -> None:
        request = _valid_request()
        result = resolver.resolve_bounded_relevance_reception_v0_min(request)
        self.assert_recorded_cleanly(result)
        self.assertEqual(
            result["bounded_relevance_reception_metadata"]["bounded_relevance_reception_id"],
            request["bounded_relevance_reception_request_id"],
        )
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)

        statement = _statement(result)
        for field in STATEMENT_TRUE_FIELDS:
            self.assertIs(statement[field], True, field)
        self.assertIs(statement["relevance_receipt_created"], False)

        signal = result["bounded_relevance_signal"]
        self.assertTrue(signal["declared"])
        self.assertEqual(signal["signal_kind"], "medium_facing_reception_material")
        basis = result["relevance_basis"]
        self.assertEqual(basis["basis_role"], "declared_relevance_basis_only")
        for key in ("truth_created", "source_created", "authority_created", "currentness_created", "action_created", "permission_created"):
            self.assertIs(basis[key], False)
        scope = result["relevance_scope"]
        self.assertIs(scope["bounded"], True)
        carrier_context = result["relevance_signal_carrier_context"]
        self.assertEqual(carrier_context["basis_role"], "context_only")
        for key in (
            "authority_created",
            "currentness_created",
            "action_created",
            "synchronization_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
        ):
            self.assertIs(carrier_context[key], False)

        envelope = result["bounded_relevance_reception_envelope"]
        self.assertTrue(envelope["declared"])
        for key in (
            "authorize_arbitrary_reception",
            "authorize_repeated_reception",
            "authorize_source_receipt",
            "authorize_reception_authorization",
            "authorize_action",
            "authorize_synchronization",
            "authorize_inhabitance",
            "authorize_runtime_permission",
            "authorize_public_api",
            "authorize_participant_facing_interface",
            "authorize_distributed_network_behavior",
            "authorize_follow_on_work",
        ):
            self.assertIs(envelope[key], False, key)
        self.assertIs(envelope["fresh_admission_required_outside_envelope"], True)
        self.assert_official_scope_preserved(result)
        self.assert_no_raw_sentinels(result)

    def test_critical_non_claim_canonicalization_blocks_flipped_inputs(self) -> None:
        explicit_required_examples = {
            "relevance_receipt_created",
            "source_transfer_occurred",
            "source_receipt_occurred",
            "reception_authorization_created",
            "source_created",
            "authority_created",
            "currentness_created",
            "truth_created",
            "action_created",
            "synchronization_created",
            "inhabitance_created",
            "runtime_permission_created",
            "public_api_created",
            "participant_facing_interface_created",
            "distributed_network_behavior_created",
            "bounded_relevance_reception_treated_as_authority",
            "bounded_relevance_reception_treated_as_truth",
            "bounded_relevance_reception_treated_as_action",
            "bounded_relevance_reception_treated_as_synchronization",
            "bounded_relevance_reception_treated_as_runtime_permission",
            "bounded_relevance_signal_treated_as_authority",
            "bounded_relevance_signal_treated_as_truth",
            "bounded_relevance_signal_treated_as_action",
            "carrier_context_treated_as_authority",
            "carrier_context_treated_as_public_api",
            "bounded_runtime_loop_envelope_treated_as_bounded_relevance_reception_authority",
            "predecessor_failure_repaired",
            "predecessor_failure_hidden",
            "predecessor_failure_claimed_passed",
        }
        self.assertTrue(explicit_required_examples.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                request = _valid_request()
                request["declared_non_claims"][key] = True
                result = resolver.resolve_bounded_relevance_reception_v0_min(request)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                self.assertTrue(any(not check.get("passed") for check in _checks(result)))
                self.assert_public_codes(result)
                self.assertIs(result["non_claims"][key], False)
                self.assert_no_created_posture(result)

    def test_representative_blocking_behavior(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("explicit block intent", _mutate_field("bounded_relevance_reception_intent", "BLOCK_BOUNDED_RELEVANCE_RECEPTION")),
            ("empty request mapping", lambda request: request.clear()),
            ("unsupported intent", _mutate_field("bounded_relevance_reception_intent", "UNSUPPORTED_INTENT")),
            ("unsupported scope", _mutate_field("bounded_relevance_reception_scope", ["UNSUPPORTED_SCOPE"])),
            (
                "missing selection basis",
                _remove_fields("selected_bounded_relevance_reception_selection_basis", "selected_bounded_relevance_reception_selection_path"),
            ),
            (
                "selection not selected pressure",
                _mutate_field("selected_bounded_relevance_reception_selection_states_selected_next_layer_pressure", False),
            ),
            ("selection already created reception", _mutate_field("selected_bounded_relevance_reception_selection_already_created_reception", True)),
            ("selection authorized mechanism", _mutate_field("selected_bounded_relevance_reception_selection_authorized_mechanism", True)),
            ("runtime closure basis missing", _remove_fields("selected_runtime_layer_closure_basis", "selected_runtime_layer_closure_path")),
            ("runtime closure not recorded", _mutate_field("selected_runtime_layer_closure_recorded", False)),
            ("runtime closure not closed", _mutate_field("selected_runtime_layer_closure_closed_internal_runtime_stack", False)),
            ("runtime closure selected public api", _mutate_field("selected_runtime_layer_closure_selected_public_api", True)),
            (
                "runtime closure selected participant interface",
                _mutate_field("selected_runtime_layer_closure_selected_participant_facing_interface", True),
            ),
            (
                "runtime closure selected distributed network",
                _mutate_field("selected_runtime_layer_closure_selected_distributed_network_behavior", True),
            ),
            (
                "runtime closure selected source authority currentness",
                _mutate_field("selected_runtime_layer_closure_selected_source_authority_currentness", True),
            ),
            ("runtime closure selected deployment operation", _mutate_field("selected_runtime_layer_closure_selected_deployment_operation", True)),
            ("runtime closure authorized follow on", _mutate_field("selected_runtime_layer_closure_authorized_follow_on_work", True)),
            ("runtime loop basis missing", _remove_fields("selected_runtime_loop_basis", "selected_runtime_loop_result_path")),
            ("runtime loop not recorded", _mutate_field("selected_runtime_loop_result_outcome", "NOT_RECORDED")),
            ("runtime loop failed checks present", _mutate_field("selected_runtime_loop_failed_check_count", 1)),
            ("runtime loop version wrong", _mutate_field("selected_runtime_loop_result_version", "9.9.9")),
            ("runtime loop posture missing", _mutate_field("selected_runtime_loop_bounded_posture_recorded", False)),
            ("runtime loop envelope missing", _mutate_field("selected_runtime_loop_bounded_runtime_loop_envelope_recorded", False)),
            ("runtime loop created public api", _mutate_field("selected_runtime_loop_already_created_public_api", True)),
            (
                "runtime loop created participant interface",
                _mutate_field("selected_runtime_loop_already_created_participant_facing_interface", True),
            ),
            (
                "runtime loop created distributed network",
                _mutate_field("selected_runtime_loop_already_created_distributed_network_behavior", True),
            ),
            ("runtime loop created source", _mutate_field("selected_runtime_loop_already_created_source", True)),
            ("runtime loop created authority", _mutate_field("selected_runtime_loop_already_created_authority", True)),
            ("runtime loop created currentness", _mutate_field("selected_runtime_loop_already_created_currentness", True)),
            ("runtime loop created deployment", _mutate_field("selected_runtime_loop_already_created_deployment", True)),
            ("runtime loop created public release", _mutate_field("selected_runtime_loop_already_created_public_release", True)),
            ("runtime loop created operation permission", _mutate_field("selected_runtime_loop_already_created_operation_permission", True)),
            ("runtime loop authorized follow on", _mutate_field("selected_runtime_loop_authorized_follow_on_work", True)),
            (
                "bounded runtime loop envelope reception authority",
                _mutate_field("bounded_runtime_loop_envelope_treated_as_reception_authority", True),
            ),
            ("carrier anatomy authority", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_authority", True)),
            ("carrier anatomy action", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_action_authority", True)),
            ("carrier anatomy sync", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_synchronization_authority", True)),
            ("carrier anatomy runtime permission", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_runtime_permission", True)),
            ("carrier anatomy public api", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_public_api", True)),
            ("carrier anatomy participant interface", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_participant_interface", True)),
            ("carrier anatomy distributed", _mutate_field("carrier_aware_distributed_anatomy_basis_treated_as_distributed_network", True)),
            ("bounded relevance signal missing", _mutate_field("bounded_relevance_signal_missing", True)),
            ("bounded relevance signal source", _mutate_field("bounded_relevance_signal_treated_as_source", True)),
            ("bounded relevance signal authority", _mutate_field("bounded_relevance_signal_treated_as_authority", True)),
            ("bounded relevance signal currentness", _mutate_field("bounded_relevance_signal_treated_as_currentness", True)),
            ("bounded relevance signal truth", _mutate_field("bounded_relevance_signal_treated_as_truth", True)),
            ("bounded relevance signal action", _mutate_field("bounded_relevance_signal_treated_as_action", True)),
            ("bounded relevance signal sync", _mutate_field("bounded_relevance_signal_treated_as_synchronization", True)),
            ("bounded relevance signal inhabitance", _mutate_field("bounded_relevance_signal_treated_as_inhabitance", True)),
            ("bounded relevance signal runtime permission", _mutate_field("bounded_relevance_signal_treated_as_runtime_permission", True)),
            ("bounded relevance signal public api", _mutate_field("bounded_relevance_signal_treated_as_public_api", True)),
            (
                "bounded relevance signal participant interface",
                _mutate_field("bounded_relevance_signal_treated_as_participant_facing_interface", True),
            ),
            (
                "bounded relevance signal distributed",
                _mutate_field("bounded_relevance_signal_treated_as_distributed_network_behavior", True),
            ),
            ("relevance basis missing", _mutate_field("relevance_basis_missing", True)),
            ("relevance basis truth", _mutate_field("relevance_basis_treated_as_truth", True)),
            ("relevance basis authority", _mutate_field("relevance_basis_treated_as_authority", True)),
            ("relevance scope missing", _mutate_field("relevance_scope_missing", True)),
            ("relevance scope unbounded", _mutate_field("relevance_scope_unbounded", True)),
            ("recorded before review", _mutate_field("bounded_relevance_reception_recorded_before_review", True)),
            ("relevance receipt created", _mutate_field("relevance_receipt_created", True)),
            ("source transfer occurred", _mutate_field("source_transfer_occurred", True)),
            ("source receipt occurred", _mutate_field("source_receipt_occurred", True)),
            ("reception authorization created", _mutate_field("reception_authorization_created", True)),
            ("source created", _mutate_field("source_created", True)),
            ("authority created", _mutate_field("authority_created", True)),
            ("currentness created", _mutate_field("currentness_created", True)),
            ("truth created", _mutate_field("truth_created", True)),
            ("action created", _mutate_field("action_created", True)),
            ("synchronization created", _mutate_field("synchronization_created", True)),
            ("inhabitance created", _mutate_field("inhabitance_created", True)),
            ("runtime permission created", _mutate_field("runtime_permission_created", True)),
            ("public api created", _mutate_field("public_api_created", True)),
            ("participant interface created", _mutate_field("participant_facing_interface_created", True)),
            ("distributed network created", _mutate_field("distributed_network_behavior_created", True)),
            ("deployment created", _mutate_field("deployment_created", True)),
            ("public release created", _mutate_field("public_release_created", True)),
            ("operation permission created", _mutate_field("operation_permission_created", True)),
            ("broader reusable permission created", _mutate_field("broader_reusable_permission_created", True)),
            ("derivative reception authorized", _mutate_field("derivative_reception_authorized", True)),
            ("vessel relation authorized", _mutate_field("vessel_relation_authorized", True)),
            ("adoption created", _mutate_field("adoption_created", True)),
            ("receiving context governance created", _mutate_field("receiving_context_governance_created", True)),
            ("publication flow created", _mutate_field("publication_flow_created", True)),
            ("follow on authorized", _mutate_field("follow_on_work_authorized", True)),
            (
                "artifact existence authority",
                _mutate_field("artifact_existence_treated_as_bounded_relevance_reception_authority", True),
            ),
            ("artifact path currentness", _mutate_field("artifact_path_treated_as_currentness", True)),
            (
                "latest file authority",
                _mutate_field("latest_file_posture_treated_as_bounded_relevance_reception_authority", True),
            ),
            (
                "repo local availability authority",
                _mutate_field("repo_local_availability_treated_as_bounded_relevance_reception_authority", True),
            ),
            (
                "hidden repo content",
                _mutate_field("hidden_repo_state_used_as_bounded_relevance_reception_content", True),
            ),
            (
                "hidden repo authority",
                _mutate_field("hidden_repo_state_used_as_bounded_relevance_reception_authority", True),
            ),
            ("selected basis not reference shaped", _mutate_field("reference_shaped_input_posture", False)),
            ("raw full artifact body returned", _mutate_field("raw_full_prior_artifact_body_returned", True)),
            ("predecessor failure repaired", _mutate_field("predecessor_failure_repaired", True)),
            ("predecessor failure hidden", _mutate_field("predecessor_failure_hidden", True)),
            ("predecessor failure claimed passed", _mutate_field("predecessor_failure_claimed_passed", True)),
            ("consumed request reopened", _mutate_field("consumed_request_reopened", True)),
            ("authorization token reused", _mutate_field("authorization_token_reused", True)),
            ("required non claim flipped", _mutate_non_claim("source_created", True)),
            ("envelope arbitrary reception", _mutate_envelope("authorize_arbitrary_reception", True)),
            ("envelope repeated reception", _mutate_envelope("authorize_repeated_reception", True)),
            ("envelope source receipt", _mutate_envelope("authorize_source_receipt", True)),
            ("envelope reception authorization", _mutate_envelope("authorize_reception_authorization", True)),
            ("envelope action", _mutate_envelope("authorize_action", True)),
            ("envelope synchronization", _mutate_envelope("authorize_synchronization", True)),
            ("envelope inhabitance", _mutate_envelope("authorize_inhabitance", True)),
            ("envelope runtime permission", _mutate_envelope("authorize_runtime_permission", True)),
            ("envelope public api", _mutate_envelope("authorize_public_api", True)),
            ("envelope participant interface", _mutate_envelope("authorize_participant_facing_interface", True)),
            ("envelope distributed network", _mutate_envelope("authorize_distributed_network_behavior", True)),
            ("envelope follow on", _mutate_envelope("authorize_follow_on_work", True)),
        )
        for name, mutate in cases:
            with self.subTest(case=name):
                result = _resolve_mutated(mutate)
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                if name != "explicit block intent":
                    self.assertIn(_block_code(result), resolver.BLOCK_CODES)
                self.assert_public_codes(result)
                self.assert_no_created_posture(result)

        non_mapping = resolver.resolve_bounded_relevance_reception_v0_min(["not", "mapping"])
        self.assertEqual(non_mapping["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIn(_block_code(non_mapping), resolver.BLOCK_CODES)
        self.assert_no_created_posture(non_mapping)

    def test_missing_or_incomplete_declared_non_claims(self) -> None:
        cases = (
            ("remove declared_non_claims", _remove_field("declared_non_claims")),
            ("empty declared_non_claims", _mutate_field("declared_non_claims", {})),
            ("remove one required non-claim", _remove_non_claim("source_created")),
            ("string non-claim", _mutate_non_claim("source_created", "false")),
            ("none non-claim", _mutate_non_claim("source_created", None)),
        )
        for name, mutate in cases:
            with self.subTest(case=name):
                result = _resolve_mutated(mutate)
                self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                self.assert_public_codes(result)
                self.assert_non_claims_canonical_false(result)

    def test_official_enum_strings_are_preserved(self) -> None:
        result = resolver.resolve_bounded_relevance_reception_v0_min(_valid_request())
        self.assert_recorded_cleanly(result)
        self.assert_official_scope_preserved(result)

        request = _valid_request()
        request["bounded_relevance_reception_scope"] = list(resolver.SUPPORTED_BOUNDED_RELEVANCE_RECEPTION_SCOPE)
        result = resolver.resolve_bounded_relevance_reception_v0_min(request)
        self.assert_recorded_cleanly(result)
        self.assert_official_scope_preserved(result)

    def test_raw_and_hidden_hostile_content_is_contained_without_mutating_input(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        for index, section in enumerate(BASIS_SECTIONS):
            basis = request.setdefault(section, {})
            self.assertIsInstance(basis, dict)
            basis[SENSITIVE_KEYS[index % len(SENSITIVE_KEYS)]] = SENTINELS[index % len(SENTINELS)]
            basis["ordinary_official_scope_value"] = "OFFICIAL_ENUM_SCOPE_STRINGS_NOT_REDACTED"
        for key, sentinel in zip(SENSITIVE_KEYS, SENTINELS * 4):
            request["selected_carrier_aware_distributed_anatomy_basis"][key] = sentinel

        hostile_input = copy.deepcopy(request)
        result = resolver.resolve_bounded_relevance_reception_v0_min(request)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_raw_sentinels(result)
        self.assert_official_scope_preserved(result)
        self.assert_non_claims_canonical_false(result)
        self.assert_no_created_posture(result)
        self.assertEqual(request, hostile_input)
        self.assertNotEqual(request, original)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(_valid_request(), indent=2, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_bounded_relevance_reception_v0_min_from_path(request_path)
            self.assert_recorded_cleanly(result)

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_bounded_relevance_reception_v0_min_from_path(malformed_path)
            self.assertEqual(malformed_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(_block_code(malformed_result), resolver.BLOCK_CODES)

            array_path = temp_root / "array.json"
            array_path.write_text(json.dumps([]), encoding="utf-8")
            array_result = resolver.resolve_bounded_relevance_reception_v0_min_from_path(array_path)
            self.assertEqual(array_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(_block_code(array_result), resolver.BLOCK_CODES)

            missing_result = resolver.resolve_bounded_relevance_reception_v0_min_from_path(temp_root / "missing.json")
            self.assertEqual(missing_result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertIn(_block_code(missing_result), resolver.BLOCK_CODES)

            with mock.patch.object(resolver, "OUTPUT_ROOT", temp_root / "bounded_relevance_reception_v0_min_output"):
                first_path = resolver.write_bounded_relevance_reception_v0_min_result(result)
                second_path = resolver.write_bounded_relevance_reception_v0_min_result(result)
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(json.loads(first_path.read_text(encoding="utf-8")))
            self.assertIn("bounded_relevance_reception_v0_min", first_path.as_posix())
            for fragment in FORBIDDEN_OUTPUT_ROOT_FRAGMENTS:
                self.assertNotIn(fragment, first_path.as_posix())

    def test_non_mutation_of_declared_request_material(self) -> None:
        request = _valid_request()
        request["bounded_relevance_reception_scope"] = list(request["bounded_relevance_reception_scope"])
        for section in BASIS_SECTIONS:
            request[section] = copy.deepcopy(request[section])
        for section in (
            "bounded_relevance_signal",
            "relevance_basis",
            "relevance_scope",
            "relevance_signal_carrier_context",
            "bounded_relevance_reception_envelope",
            "declared_non_claims",
        ):
            request[section] = copy.deepcopy(request[section])
        before = copy.deepcopy(request)
        result = resolver.resolve_bounded_relevance_reception_v0_min(request)
        self.assert_recorded_cleanly(result)
        self.assertEqual(request, before)

    def test_predecessor_failure_preservation(self) -> None:
        result = resolver.resolve_bounded_relevance_reception_v0_min(_valid_request())
        self.assert_recorded_cleanly(result)
        statement = _statement(result)
        summary = _summary(result)
        non_claims = _non_claims(result)

        self.assertIn(
            "tests/test_resolve_post_self_recursive_growth_runtime_daemon_boundary.py",
            json.dumps(result["selected_runtime_daemon_boundary_v1_failure_lineage_basis"], sort_keys=True),
        )
        self.assertIs(statement["predecessor_failure_evidence_preserved"], True)
        self.assertIs(summary["predecessor_failure_evidence_preserved"], True)
        for key in (
            "runtime_daemon_boundary_v1_failure_repaired",
            "runtime_daemon_boundary_v1_failure_hidden",
            "runtime_daemon_boundary_v1_failure_claimed_passed",
            "runtime_hosting_boundary_v1_failure_repaired",
            "runtime_hosting_boundary_v1_failure_hidden",
            "runtime_hosting_boundary_v1_failure_claimed_passed",
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        self.assertIs(statement["consumed_request_token_remains_closed"], True)
        self.assertIs(statement["authorization_token_reuse_blocked"], True)
        self.assertIs(summary["consumed_request_token_remains_closed"], True)
        self.assertIs(summary["authorization_token_reuse_blocked"], True)


if __name__ == "__main__":
    unittest.main()
