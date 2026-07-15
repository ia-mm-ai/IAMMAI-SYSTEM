"""Executable checks for second-carrier execution output posture only.

This suite is downstream of recorded second-carrier execution output boundary.
It verifies that the resolver records one bounded execution-output /
second-carrier-output posture only: output capture, result, success, external
result, cross-carrier evidence, source transfer, source receipt, reception
authorization, source, authority, currentness, runtime, final completion, and
follow-on work are not created. Receiving carrier is not authority, hidden repo
state is excluded, repo-local availability is not output authority, selected
basis stays reference-shaped, the consumed request token remains closed, and
authorization token reuse remains blocked.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping as MappingABC
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_second_carrier_execution_output as resolver


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
TRUE_RECORDED_FIELDS = tuple(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
SELECTED_BASIS_KEYS = tuple(resolver.SELECTED_BASIS_KEYS)
POSTURE_KEYS = tuple(resolver.POSTURE_KEYS)

RAW_SENTINEL = "RAW_SECOND_CARRIER_EXECUTION_OUTPUT_BODY_MUST_NOT_RETURN"
HOSTILE_RAW_VALUE = "HOSTILE_SECOND_CARRIER_EXECUTION_OUTPUT_FULL_BODY_VALUE_MUST_NOT_RETURN"
REDACTION_STRINGS = {
    "[bounded-redacted-raw-or-hidden-state]",
    "[bounded-reference-redacted-raw-or-hidden-state]",
    "[bounded-reference-omitted-raw-or-hidden-state]",
}

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_second_carrier_execution_output_metadata",
    "declared_second_carrier_execution_output_question",
    "selected_second_carrier_execution_output_boundary_basis",
    "selected_second_carrier_execution_output_boundary_terminal_summary_basis",
    "selected_second_carrier_execution_basis",
    "selected_second_carrier_execution_terminal_summary_basis",
    "selected_second_carrier_execution_boundary_basis",
    "selected_second_carrier_receipt_basis",
    "selected_second_carrier_receipt_boundary_basis",
    "selected_packet_transfer_basis",
    "selected_packet_transfer_boundary_basis",
    "selected_packet_emission_basis",
    "selected_packet_emission_boundary_v2_basis",
    "selected_packet_emission_boundary_v1_predecessor_failure_basis",
    "selected_packet_artifact_basis",
    "selected_packet_boundary_basis",
    "selected_command_success_basis",
    "selected_command_result_v2_basis",
    "selected_output_capture_v2_basis",
    "selected_command_output_report_artifact_basis",
    "selected_command_execution_basis",
    "selected_command_report_lineage_basis",
    "selected_predecessor_failure_basis",
    "selected_evidence_manifest_basis",
    "selected_artifact_containment_basis",
    "selected_portable_verification_basis",
    "second_carrier_execution_output_spec_only_posture",
    "one_bounded_second_carrier_execution_output_posture",
    "second_carrier_execution_output_boundary_basis_preserved_posture",
    "second_carrier_execution_basis_preserved_posture",
    "execution_artifact_basis_preserved_posture",
    "output_recorded_bounded_posture",
    "output_artifact_recorded_or_bounded_posture",
    "output_not_capture_posture",
    "output_not_result_posture",
    "output_not_success_posture",
    "output_not_external_result_posture",
    "output_not_cross_carrier_evidence_posture",
    "output_not_source_transfer_posture",
    "output_not_source_receipt_posture",
    "output_not_reception_authorization_posture",
    "second_carrier_output_capture_not_created_posture",
    "second_carrier_result_not_created_posture",
    "second_carrier_success_not_created_posture",
    "external_result_not_created_posture",
    "cross_carrier_evidence_not_created_posture",
    "receiving_carrier_not_authority_posture",
    "source_not_created_posture",
    "authority_not_created_posture",
    "currentness_not_created_posture",
    "final_completion_not_created_posture",
    "runtime_not_created_posture",
    "continuation_not_authorized_posture",
    "reusable_permission_not_created_posture",
    "follow_on_work_not_authorized_posture",
    "hidden_repo_state_excluded_posture",
    "repo_local_availability_not_output_authority_posture",
    "selected_basis_reference_shape_posture",
    "raw_full_prior_artifact_body_not_returned_posture",
    "second_carrier_execution_output_scope",
    "second_carrier_execution_output_checks",
    "second_carrier_execution_output_statement",
    "second_carrier_execution_output_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_second_carrier_execution_output_summary",
)

REPRESENTATIVE_BLOCK_CODES = (
    "SECOND_CARRIER_EXECUTION_OUTPUT_QUESTION_UNDECLARED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_INTENT_UNSUPPORTED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_VERSION_NOT_0_1_0",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_DID_NOT_DECLARE_FUTURE_OUTPUT_STEP",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_ARTIFACT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
    "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
    "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
    "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
    "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
    "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CAPTURE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SUCCESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_EXTERNAL_RESULT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_TRANSFER",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_RECEIPT",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RECEPTION_AUTHORIZATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_AUTHORITY",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CURRENTNESS",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FINAL_COMPLETION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RUNTIME",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CONTINUATION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_REUSABLE_PERMISSION",
    "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FOLLOW_ON_WORK",
    "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED",
    "SECOND_CARRIER_RESULT_CREATED",
    "SECOND_CARRIER_SUCCESS_CREATED",
    "EXTERNAL_RESULT_CREATED",
    "CROSS_CARRIER_EVIDENCE_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "FINAL_COMPLETION_CLAIMED",
    "RUNTIME_HOSTING_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "CONTINUATION_AUTHORIZED",
    "REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "RECEIVING_CARRIER_TREATED_AS_AUTHORITY",
    "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY",
    "ARTIFACT_PATH_TREATED_AS_CURRENTNESS",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY",
    "SELECTED_BASIS_NOT_REFERENCE_SHAPED",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT",
    "ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE",
)

NON_MEANING_FALSE_FIELDS = (
    "second_carrier_output_capture_exists",
    "second_carrier_result_exists",
    "second_carrier_success_exists",
    "external_result_exists",
    "cross_carrier_evidence_exists",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_exists",
    "source_exists",
    "authority_exists",
    "currentness_exists",
    "final_completion_exists",
    "runtime_exists",
    "deployment_exists",
    "public_release_exists",
    "continuation_authorized",
    "reusable_permission_exists",
    "follow_on_work_authorized",
    "output_became_capture",
    "output_became_result",
    "output_became_success",
    "output_became_external_result",
    "output_became_cross_carrier_proof",
    "output_became_source_transfer_source_receipt_or_reception_authorization",
    "output_became_source_authority_or_currentness",
    "output_artifact_became_capture_result_success_external_result_or_cross_carrier_evidence",
    "receiving_carrier_became_authority",
    "transferred_packet_became_source_authority_or_currentness",
    "artifact_existence_became_output_authority",
    "artifact_path_became_currentness",
    "repo_local_availability_became_output_authority",
    "hidden_repo_state_became_output_authority",
    "v1_packet_emission_boundary_resolver_repaired_hidden_erased_or_claimed_passed",
)

HOSTILE_RAW_KEYS = (
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_result_body",
    "raw_output_body",
    "execution_body",
    "execution_artifact_body",
    "output_body",
    "output_artifact_body",
    "second_carrier_output_body",
    "second_carrier_output_capture_body",
    "second_carrier_result_body",
    "second_carrier_success_body",
    "external_result_body",
    "cross_carrier_evidence_body",
    "packet_body",
    "source_body",
    "authority_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
    "carrier_possession",
    "copy_presence",
    "receiving_carrier",
    "receipt_artifact_presence",
    "execution_artifact_presence",
    "output_artifact_presence",
    "output_path_existence",
    "unlisted_file_dependency",
)


def _basis(name: str, outcome: str | None = None, **extra: Any) -> dict[str, Any]:
    section: dict[str, Any] = {
        "basis_id": f"{name}_basis_001",
        "basis_name": name,
        "basis_declared": True,
        "basis_role": "selected_reference_basis_only",
        "reference_shape_preserved": True,
    }
    if outcome is not None:
        section["outcome"] = outcome
    section.update(extra)
    return section


def _posture(name: str) -> dict[str, Any]:
    return {
        "posture_name": name,
        "posture_declared": True,
        "preserves_output_membrane": True,
    }


def _clean_request() -> dict[str, Any]:
    if hasattr(
        resolver,
        "build_declared_portable_source_body_verification_second_carrier_execution_output_request",
    ):
        request = (
            resolver.build_declared_portable_source_body_verification_second_carrier_execution_output_request(
                second_carrier_execution_output_request_id=(
                    "second_carrier_execution_output_reference_review_001"
                )
            )
        )
    else:
        request = {
            "second_carrier_execution_output_request_id": (
                "second_carrier_execution_output_reference_review_001"
            ),
            "second_carrier_execution_output_question": resolver.QUESTION,
            "second_carrier_execution_output_intent": resolver.INTENT_RECORD,
        }

    request["second_carrier_execution_output_scope"] = list(SUPPORTED_SCOPE)
    request["declared_non_claims"] = {
        key: False for key in REQUIRED_FALSE_NON_CLAIMS
    }
    request["reference_shaped_input_posture"] = True

    basis_outcomes = {
        "selected_second_carrier_execution_output_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_execution_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_RECORDED"
        ),
        "selected_second_carrier_execution_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_BOUNDARY_RECORDED"
        ),
        "selected_second_carrier_receipt_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_RECORDED"
        ),
        "selected_second_carrier_receipt_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_RECEIPT_BOUNDARY_RECORDED"
        ),
        "selected_packet_transfer_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_RECORDED"
        ),
        "selected_packet_transfer_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_TRANSFER_BOUNDARY_RECORDED"
        ),
        "selected_packet_emission_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_RECORDED"
        ),
        "selected_packet_emission_boundary_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_EMISSION_BOUNDARY_RECORDED"
        ),
        "selected_packet_artifact_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_ARTIFACT_RECORDED"
        ),
        "selected_packet_boundary_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_PACKET_BOUNDARY_RECORDED"
        ),
        "selected_command_success_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_SUCCESS_RECORDED"
        ),
        "selected_command_result_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_RESULT_RECORDED"
        ),
        "selected_output_capture_v2_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_OUTPUT_CAPTURE_RECORDED"
        ),
        "selected_command_output_report_artifact_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_REPORT_ARTIFACT_RECORDED"
        ),
        "selected_command_execution_basis": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_RECORDED"
        ),
    }
    for key in SELECTED_BASIS_KEYS:
        request[key] = _basis(key, basis_outcomes.get(key))

    request["selected_second_carrier_execution_output_boundary_basis"].update(
        {
            "result_version": "0.1.0",
            "failed_check_count": 0,
            "declared_future_output_step": True,
            "one_future_second_carrier_execution_output_step_declared": True,
            "already_created_output": False,
            "already_created_output_artifact": False,
            "already_created_output_capture": False,
            "already_created_second_carrier_result": False,
            "already_created_second_carrier_success": False,
            "created_external_result": False,
            "created_cross_carrier_evidence": False,
            "used_hidden_repo_state_as_output_authority": False,
            "treated_repo_local_availability_as_output_authority": False,
            "treated_receiving_carrier_as_authority": False,
            "raw_full_prior_artifact_body_returned": False,
        }
    )
    request["selected_second_carrier_execution_basis"].update(
        {
            "failed_check_count": 0,
            "bounded_execution_recorded": True,
            "recorded_bounded_execution": True,
            "execution_not_output": True,
            "treated_execution_as_output": False,
        }
    )
    request["selected_command_report_lineage_basis"].update(
        {
            "lineage_only": True,
            "treated_as_current_report_artifact": False,
            "treated_as_source": False,
            "treated_as_authority": False,
            "treated_as_currentness": False,
        }
    )
    request[
        "selected_packet_emission_boundary_v1_predecessor_failure_basis"
    ].update(
        {
            "predecessor_failure_visible": True,
            "repaired": False,
            "hidden": False,
            "claimed_passed": False,
        }
    )
    for key in POSTURE_KEYS:
        request[key] = _posture(key.removesuffix("_posture"))
    for key in REQUIRED_FALSE_NON_CLAIMS:
        request[key] = False
    return request


def _resolve(request: Mapping[str, Any] | None) -> dict[str, Any]:
    return resolver.resolve_portable_source_body_verification_second_carrier_execution_output(
        declared_second_carrier_execution_output_request=request
    )


class SecondCarrierExecutionOutputResolverTests(unittest.TestCase):
    def assert_public_block_codes(self, result: Mapping[str, Any]) -> None:
        block = result.get("block") if isinstance(result, MappingABC) else None
        if isinstance(block, MappingABC):
            code = block.get("block_code")
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)
        for check in result.get("second_carrier_execution_output_checks", []):
            self.assertIsInstance(check, MappingABC)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_generated_booleans(self, result: Mapping[str, Any]) -> None:
        boolean_sections = (
            result.get("second_carrier_execution_output_statement", {}),
            result.get("second_carrier_execution_output_non_meaning", {}),
            result.get("non_claims", {}),
        )
        for section in boolean_sections:
            self.assertIsInstance(section, MappingABC)
            for key, value in section.items():
                with self.subTest(boolean_field=key):
                    self.assertIsInstance(value, bool)
                    self.assertNotIn(value, REDACTION_STRINGS)

        summary = result.get(
            "portable_source_body_verification_second_carrier_execution_output_summary",
            {},
        )
        self.assertIsInstance(summary, MappingABC)
        for key in TRUE_RECORDED_FIELDS:
            if key in summary:
                self.assertIsInstance(summary[key], bool)

    def assert_serialized_omits_raw_sentinels(
        self,
        result: Mapping[str, Any],
        *sentinels: str,
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in (RAW_SENTINEL, HOSTILE_RAW_VALUE, *sentinels):
            self.assertNotIn(sentinel, serialized)

    def assert_no_downstream_created(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims", {})
        self.assertIsInstance(non_claims, MappingABC)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)
        self.assertIs(non_claims.get("consumed_request_reopened"), False)
        self.assertIs(non_claims.get("authorization_token_reused"), False)
        self.assertIs(non_claims.get("v1_repaired"), False)
        self.assertIs(non_claims.get("v1_hidden"), False)
        self.assertIs(non_claims.get("v1_claimed_passed"), False)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_portable_source_body_verification_second_carrier_execution_output",
            "resolve_portable_source_body_verification_second_carrier_execution_output_from_path",
            "write_portable_source_body_verification_second_carrier_execution_output_result",
            "build_portable_source_body_verification_second_carrier_execution_output_summary",
            "build_declared_portable_source_body_verification_second_carrier_execution_output_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        for name in (
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "RESULT_VERSION",
            "OUTPUT_ROOT",
            "SUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "second_carrier_execution_output"
            )
        )
        for code in REPRESENTATIVE_BLOCK_CODES:
            with self.subTest(block_code=code):
                self.assertIn(code, resolver.BLOCK_CODES)

    def test_successful_second_carrier_execution_output_recorded_result(self) -> None:
        request = _clean_request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        failed = [
            check
            for check in result["second_carrier_execution_output_checks"]
            if not check.get("passed")
        ]
        self.assertEqual(failed, [])

        for section in TOP_LEVEL_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, result)

        metadata = result[
            "portable_source_body_verification_second_carrier_execution_output_metadata"
        ]
        self.assertEqual(
            metadata[
                "portable_source_body_verification_second_carrier_execution_output_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_second_carrier_execution_output",
        )
        self.assertEqual(
            metadata["second_carrier_execution_output_request_id"],
            request["second_carrier_execution_output_request_id"],
        )

        statement = result["second_carrier_execution_output_statement"]
        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(statement=key):
                self.assertIs(statement.get(key), True)

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(non_claims.get(key), False)

        non_meaning = result["second_carrier_execution_output_non_meaning"]
        for key in NON_MEANING_FALSE_FIELDS:
            with self.subTest(non_meaning=key):
                self.assertIn(key, non_meaning)
                self.assertIs(non_meaning[key], False)

        self.assert_public_block_codes(result)
        self.assert_generated_booleans(result)
        self.assert_serialized_omits_raw_sentinels(result)
        self.assert_no_downstream_created(result)

    def test_summary_helper_preserves_output_posture(self) -> None:
        request = _clean_request()
        result = _resolve(request)
        summary = (
            resolver.build_portable_source_body_verification_second_carrier_execution_output_summary(
                result
            )
        )

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["request_id"],
            request["second_carrier_execution_output_request_id"],
        )
        self.assertEqual(summary["question"], request["second_carrier_execution_output_question"])
        self.assertEqual(summary["intent"], request["second_carrier_execution_output_intent"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(
            summary["selected_second_carrier_execution_output_boundary_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RECORDED",
        )
        self.assertEqual(
            summary["selected_second_carrier_execution_output_boundary_version"],
            "0.1.0",
        )
        self.assertEqual(
            summary["selected_second_carrier_execution_output_boundary_failed_check_count"],
            0,
        )

        for key in TRUE_RECORDED_FIELDS:
            with self.subTest(summary_true=key):
                self.assertIs(summary.get(key), True)

        self.assertTrue(
            summary["no_output_capture_result_success_external_result_or_cross_carrier_evidence"]
        )
        self.assertTrue(
            summary["no_source_authority_currentness_final_completion_or_runtime"]
        )
        self.assertTrue(summary["no_deployment_public_release_or_follow_on"])
        self.assertTrue(summary["v1_predecessor_failure_preserved"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(summary_non_claim=key):
                self.assertIs(summary["key_non_claims"].get(key), False)

    def test_representative_blocking_behavior(self) -> None:
        def boundary_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request["selected_second_carrier_execution_output_boundary_basis"][
                    field
                ] = value

            return mutate

        def execution_field(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request["selected_second_carrier_execution_basis"][field] = value

            return mutate

        def top_level(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            def mutate(request: dict[str, Any]) -> None:
                request[field] = value

            return mutate

        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str | None], ...] = (
            (
                "explicit block intent",
                lambda request: request.update(
                    {
                        "second_carrier_execution_output_intent": (
                            resolver.INTENT_BLOCK
                        )
                    }
                ),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BLOCK_REQUESTED",
            ),
            (
                "unsupported intent",
                lambda request: request.update(
                    {"second_carrier_execution_output_intent": "UNSUPPORTED"}
                ),
                "SECOND_CARRIER_EXECUTION_OUTPUT_INTENT_UNSUPPORTED",
            ),
            (
                "unsupported scope",
                lambda request: request.update(
                    {"second_carrier_execution_output_scope": ["UNSUPPORTED_SCOPE"]}
                ),
                "UNSUPPORTED_SECOND_CARRIER_EXECUTION_OUTPUT_SCOPE",
            ),
            (
                "missing output boundary basis",
                lambda request: request.pop(
                    "selected_second_carrier_execution_output_boundary_basis"
                ),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_BASIS_MISSING",
            ),
            (
                "output boundary not recorded",
                boundary_field("outcome", "NOT_RECORDED"),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_NOT_RECORDED",
            ),
            (
                "output boundary failed checks",
                boundary_field("failed_check_count", 1),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            (
                "output boundary version mismatch",
                boundary_field("result_version", "0.2.0"),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_VERSION_NOT_0_1_0",
            ),
            (
                "output boundary did not declare future output step",
                lambda request: request[
                    "selected_second_carrier_execution_output_boundary_basis"
                ].update(
                    {
                        "declared_future_output_step": False,
                        "one_future_second_carrier_execution_output_step_declared": False,
                    }
                ),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_DID_NOT_DECLARE_FUTURE_OUTPUT_STEP",
            ),
            (
                "output boundary already created output",
                boundary_field("already_created_output", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT",
            ),
            (
                "output boundary already created output artifact",
                boundary_field("already_created_output_artifact", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_ARTIFACT",
            ),
            (
                "output boundary already created output capture",
                boundary_field("already_created_output_capture", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            (
                "output boundary already created result",
                boundary_field("already_created_second_carrier_result", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_RESULT",
            ),
            (
                "output boundary already created success",
                boundary_field("already_created_second_carrier_success", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_ALREADY_CREATED_SECOND_CARRIER_SUCCESS",
            ),
            (
                "output boundary created external result",
                boundary_field("created_external_result", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_EXTERNAL_RESULT",
            ),
            (
                "output boundary created cross-carrier evidence",
                boundary_field("created_cross_carrier_evidence", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_CREATED_CROSS_CARRIER_EVIDENCE",
            ),
            (
                "output boundary used hidden repo state as authority",
                boundary_field("used_hidden_repo_state_as_output_authority", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_USED_HIDDEN_REPO_STATE_AS_OUTPUT_AUTHORITY",
            ),
            (
                "output boundary treated repo local availability as authority",
                boundary_field("treated_repo_local_availability_as_output_authority", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_REPO_LOCAL_AVAILABILITY_AS_OUTPUT_AUTHORITY",
            ),
            (
                "output boundary treated receiving carrier as authority",
                boundary_field("treated_receiving_carrier_as_authority", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_TREATED_RECEIVING_CARRIER_AS_AUTHORITY",
            ),
            (
                "output boundary returned raw full prior artifact body",
                boundary_field("raw_full_prior_artifact_body_returned", True),
                "SECOND_CARRIER_EXECUTION_OUTPUT_BOUNDARY_RETURNED_RAW_FULL_PRIOR_ARTIFACT_BODY",
            ),
            (
                "missing second-carrier execution basis",
                lambda request: request.pop("selected_second_carrier_execution_basis"),
                "SECOND_CARRIER_EXECUTION_BASIS_MISSING",
            ),
            (
                "second-carrier execution not recorded",
                execution_field("outcome", "NOT_RECORDED"),
                "SECOND_CARRIER_EXECUTION_NOT_RECORDED",
            ),
            (
                "second-carrier execution failed checks",
                execution_field("failed_check_count", 1),
                "SECOND_CARRIER_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            (
                "second-carrier execution did not record bounded execution",
                lambda request: request["selected_second_carrier_execution_basis"].update(
                    {
                        "bounded_execution_recorded": False,
                        "recorded_bounded_execution": False,
                    }
                ),
                "SECOND_CARRIER_EXECUTION_DID_NOT_RECORD_BOUNDED_EXECUTION",
            ),
            (
                "second-carrier execution treated execution as output",
                execution_field("treated_execution_as_output", True),
                "SECOND_CARRIER_EXECUTION_TREATED_EXECUTION_AS_OUTPUT",
            ),
            ("output treated as capture", top_level("second_carrier_execution_output_treated_as_capture", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CAPTURE"),
            ("output treated as result", top_level("second_carrier_execution_output_treated_as_result", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RESULT"),
            ("output treated as success", top_level("second_carrier_execution_output_treated_as_success", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SUCCESS"),
            ("output treated as external result", top_level("second_carrier_execution_output_treated_as_external_result", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_EXTERNAL_RESULT"),
            ("output treated as cross-carrier evidence", top_level("second_carrier_execution_output_treated_as_cross_carrier_evidence", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CROSS_CARRIER_EVIDENCE"),
            ("output treated as source transfer", top_level("second_carrier_execution_output_treated_as_source_transfer", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_TRANSFER"),
            ("output treated as source receipt", top_level("second_carrier_execution_output_treated_as_source_receipt", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE_RECEIPT"),
            ("output treated as reception authorization", top_level("second_carrier_execution_output_treated_as_reception_authorization", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RECEPTION_AUTHORIZATION"),
            ("output treated as source", top_level("second_carrier_execution_output_treated_as_source", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_SOURCE"),
            ("output treated as authority", top_level("second_carrier_execution_output_treated_as_authority", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_AUTHORITY"),
            ("output treated as currentness", top_level("second_carrier_execution_output_treated_as_currentness", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CURRENTNESS"),
            ("output treated as final completion", top_level("second_carrier_execution_output_treated_as_final_completion", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FINAL_COMPLETION"),
            ("output treated as runtime", top_level("second_carrier_execution_output_treated_as_runtime", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_RUNTIME"),
            ("output treated as continuation", top_level("second_carrier_execution_output_treated_as_continuation", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_CONTINUATION"),
            ("output treated as reusable permission", top_level("second_carrier_execution_output_treated_as_reusable_permission", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_REUSABLE_PERMISSION"),
            ("output treated as follow-on", top_level("second_carrier_execution_output_treated_as_follow_on_work", True), "SECOND_CARRIER_EXECUTION_OUTPUT_TREATED_AS_FOLLOW_ON_WORK"),
            ("output capture created", top_level("second_carrier_output_capture_created", True), "SECOND_CARRIER_OUTPUT_CAPTURE_CREATED"),
            ("result created", top_level("second_carrier_result_created", True), "SECOND_CARRIER_RESULT_CREATED"),
            ("success created", top_level("second_carrier_success_created", True), "SECOND_CARRIER_SUCCESS_CREATED"),
            ("external result created", top_level("external_result_created", True), "EXTERNAL_RESULT_CREATED"),
            ("cross-carrier evidence created", top_level("cross_carrier_evidence_created", True), "CROSS_CARRIER_EVIDENCE_CREATED"),
            ("source transfer occurred", top_level("source_transfer_occurred", True), "SOURCE_TRANSFER_OCCURRED"),
            ("source receipt occurred", top_level("source_receipt_occurred", True), "SOURCE_RECEIPT_OCCURRED"),
            ("reception authorization created", top_level("reception_authorization_created", True), "RECEPTION_AUTHORIZATION_CREATED"),
            ("source created", top_level("source_created", True), "SOURCE_CREATED"),
            ("authority created", top_level("authority_created", True), "AUTHORITY_CREATED"),
            ("currentness created", top_level("currentness_created", True), "CURRENTNESS_CREATED"),
            ("final completion claimed", top_level("final_completion_claimed", True), "FINAL_COMPLETION_CLAIMED"),
            ("runtime hosting created", top_level("runtime_hosting_created", True), "RUNTIME_HOSTING_CREATED"),
            ("deployment created", top_level("deployment_created", True), "DEPLOYMENT_CREATED"),
            ("public release created", top_level("public_release_created", True), "PUBLIC_RELEASE_CREATED"),
            ("operation permission created", top_level("operation_permission_created", True), "OPERATION_PERMISSION_CREATED"),
            ("continuation authorized", top_level("continuation_authorized", True), "CONTINUATION_AUTHORIZED"),
            ("reusable permission created", top_level("reusable_permission_created", True), "REUSABLE_PERMISSION_CREATED"),
            ("follow-on work authorized", top_level("follow_on_work_authorized", True), "FOLLOW_ON_WORK_AUTHORIZED"),
            ("receiving carrier treated as authority", top_level("receiving_carrier_treated_as_authority", True), "RECEIVING_CARRIER_TREATED_AS_AUTHORITY"),
            ("artifact existence treated as output authority", top_level("artifact_existence_treated_as_output_authority", True), "ARTIFACT_EXISTENCE_TREATED_AS_OUTPUT_AUTHORITY"),
            ("artifact path treated as currentness", top_level("artifact_path_treated_as_currentness", True), "ARTIFACT_PATH_TREATED_AS_CURRENTNESS"),
            ("repo local availability treated as output authority", top_level("repo_local_availability_treated_as_output_authority", True), "REPO_LOCAL_AVAILABILITY_TREATED_AS_OUTPUT_AUTHORITY"),
            ("hidden repo state used as output content", top_level("hidden_repo_state_used_as_output_content", True), "HIDDEN_REPO_STATE_USED_AS_OUTPUT_CONTENT"),
            ("hidden repo state used as output authority", top_level("hidden_repo_state_used_as_output_authority", True), "HIDDEN_REPO_STATE_USED_AS_OUTPUT_AUTHORITY"),
            ("selected basis not reference-shaped", top_level("reference_shaped_input_posture", False), "SELECTED_BASIS_NOT_REFERENCE_SHAPED"),
            ("raw full prior body returned", top_level("raw_full_prior_artifact_body_returned", True), "RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED"),
            (
                "predecessor failure hidden",
                lambda request: request[
                    "selected_packet_emission_boundary_v1_predecessor_failure_basis"
                ].update({"hidden": True}),
                "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
            ),
            (
                "command report lineage treated as current report artifact",
                lambda request: request["selected_command_report_lineage_basis"].update(
                    {"treated_as_current_report_artifact": True}
                ),
                "COMMAND_REPORT_LINEAGE_TREATED_AS_CURRENTNESS",
            ),
            ("consumed request reopened", top_level("consumed_request_reopened", True), "CONSUMED_REQUEST_REOPENED"),
            ("authorization token reused", top_level("authorization_token_reused", True), "AUTHORIZATION_TOKEN_REUSED"),
            (
                "full prior body emitted outside bounded output",
                top_level("full_prior_artifact_body_emitted_outside_bounded_output", True),
                "FULL_PRIOR_ARTIFACT_BODY_EMITTED_OUTSIDE_BOUNDED_OUTPUT",
            ),
            ("artifacts mutated", top_level("artifacts_mutated", True), "ARTIFACTS_MUTATED"),
            (
                "required non-claim flipped",
                lambda request: request["declared_non_claims"].update(
                    {"source_created": True}
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "required non-claim missing",
                lambda request: request["declared_non_claims"].pop(
                    "source_created"
                ),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        )

        malformed_results = (
            ("missing request", _resolve(None)),
            ("non-mapping request", _resolve(["not", "a", "mapping"])),  # type: ignore[arg-type]
        )
        for label, result in malformed_results:
            with self.subTest(block_case=label):
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                self.assert_public_block_codes(result)
                self.assert_no_downstream_created(result)

        for label, mutate, expected_code in cases:
            with self.subTest(block_case=label):
                request = _clean_request()
                mutate(request)
                result = _resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIsNotNone(result["block"]["block_code"])
                if expected_code is not None:
                    self.assertEqual(result["block"]["block_code"], expected_code)
                self.assert_public_block_codes(result)
                self.assert_no_downstream_created(result)
                self.assert_generated_booleans(result)

    def test_path_and_write_behavior(self) -> None:
        request = _clean_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")

            result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_from_path(
                    request_path
                )
            )
            self.assertEqual(result["outcome"], RECORDED)
            metadata = result[
                "portable_source_body_verification_second_carrier_execution_output_metadata"
            ]
            self.assertEqual(
                metadata[
                    "portable_source_body_verification_second_carrier_execution_output_result_version"
                ],
                "0.1.0",
            )
            self.assertEqual(
                metadata["resolver_module"],
                "resolve_portable_source_body_verification_second_carrier_execution_output",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionOutputError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_from_path(
                    malformed_path
                )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_from_path(
                    array_path
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assert_public_block_codes(array_result)

            with self.assertRaises(
                resolver.PortableSourceBodyVerificationSecondCarrierExecutionOutputError
            ):
                resolver.resolve_portable_source_body_verification_second_carrier_execution_output_from_path(
                    tmp_path / "missing.json"
                )

            output_root = (
                tmp_path
                / "artifacts"
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_output"
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = (
                    resolver.write_portable_source_body_verification_second_carrier_execution_output_result(
                        result
                    )
                )
                second = (
                    resolver.write_portable_source_body_verification_second_carrier_execution_output_result(
                        result
                    )
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, output_root)
            self.assertEqual(second.parent, output_root)
            self.assertTrue(first.parent.is_dir())
            self.assertTrue(second.stem.endswith("_001"))
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], RECORDED)
            self.assertEqual(
                first.parent.name,
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_output",
            )
            forbidden_roots = {
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution_output_boundary",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_second_carrier_execution",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_output_capture_v2",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_result_v2",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_command_success",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_cross_carrier_evidence",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_runtime",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_deployment",
                "integrity_host_v0_min_coexistence_portable_source_body_verification_public_release",
            }
            self.assertNotIn(first.parent.name, forbidden_roots)

    def test_non_mutation(self) -> None:
        request = _clean_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS:
            with self.subTest(selected_basis=key):
                self.assertEqual(request[key], original[key])
        for key in POSTURE_KEYS:
            with self.subTest(posture=key):
                self.assertEqual(request[key], original[key])
        self.assertEqual(
            request["second_carrier_execution_output_scope"],
            original["second_carrier_execution_output_scope"],
        )
        self.assertEqual(request["declared_non_claims"], original["declared_non_claims"])

    def test_raw_full_body_and_hidden_repo_state_containment(self) -> None:
        request = _clean_request()
        raw_payload = {
            key: {
                "sentinel": RAW_SENTINEL,
                "hostile": HOSTILE_RAW_VALUE,
                "nested": [RAW_SENTINEL, {"hostile": HOSTILE_RAW_VALUE}],
            }
            for key in HOSTILE_RAW_KEYS
        }
        injection_targets = (
            "selected_second_carrier_execution_output_boundary_basis",
            "selected_second_carrier_execution_basis",
            "selected_second_carrier_execution_boundary_basis",
            "selected_second_carrier_receipt_basis",
            "selected_packet_transfer_basis",
            "selected_packet_transfer_boundary_basis",
            "selected_packet_emission_basis",
            "selected_packet_emission_boundary_v2_basis",
            "selected_packet_artifact_basis",
            "selected_packet_boundary_basis",
            "selected_command_success_basis",
            "selected_output_capture_v2_basis",
            "selected_command_report_lineage_basis",
            "selected_artifact_containment_basis",
        )
        for key in injection_targets:
            request[key].update(copy.deepcopy(raw_payload))

        original = copy.deepcopy(request)
        result = _resolve(request)

        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assert_public_block_codes(result)
        self.assert_serialized_omits_raw_sentinels(result)
        self.assert_no_downstream_created(result)
        self.assert_generated_booleans(result)
        self.assertEqual(request, original)


if __name__ == "__main__":
    unittest.main()
