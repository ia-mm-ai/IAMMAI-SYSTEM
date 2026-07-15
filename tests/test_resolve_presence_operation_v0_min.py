"""Executable tests for the bounded presence-operation resolver.

The suite proves that completed presence-boundary allowance permits one
presence evaluation only.  Missing receiver-side answerable basis produces a
lawful waiting result, while presence support requires a custody-distinct,
refusable answer that the receiver could have withheld.  Neither path creates
identity, coupling, runtime machinery, relation conversion, repair, discovery,
or downstream authorization.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_presence_operation_v0_min as resolver


REQUIRED_PUBLIC_BLOCK_CODES = {
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "PRESENCE_OPERATION_SPEC_REFERENCE_MISSING",
    "PRESENCE_OPERATION_SPEC_MARKER_MISSING",
    "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "RECEIVER_ANSWERABLE_BASIS_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_SELF_SATISFYING_PRESENCE_REQUESTED",
    "PROHIBITED_REPO_LOCAL_PRESENCE_SUPPORT_REQUESTED",
    "PROHIBITED_OPERATOR_ONLY_ATTESTATION_REQUESTED",
    "PROHIBITED_DERIVATIVE_RENDERING_ATTESTATION_REQUESTED",
    "PROHIBITED_SAME_CUSTODY_COUNTERSIGNATURE_REQUESTED",
    "PROHIBITED_AUTOMATIC_ACKNOWLEDGEMENT_REQUESTED",
    "PROHIBITED_GENERATED_AFFIRMATION_REQUESTED",
    "PROHIBITED_FORGED_RECEIVER_ATTESTATION_REQUESTED",
    "PROHIBITED_NON_REFUSABLE_ANSWER_REQUESTED",
    "PROHIBITED_DECLARING_SIDE_CONTROLLED_BASIS_REQUESTED",
    "PROHIBITED_IDENTITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_STANDING_REQUESTED",
    "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
}

REQUIRED_TOP_LEVEL_SECTIONS = {
    "presence_operation_metadata",
    "declared_presence_operation_basis",
    "upstream_basis",
    "presence_operation",
    "presence_operation_material",
    "presence_operation_checks",
    "presence_operation_statement",
    "presence_operation_non_meaning",
    "operation_result_detail",
    "permitted_future_route",
    "blocked_routes",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "presence_operation_summary",
}

OPERATION_WRAPPER_FIELDS = {
    "outcome",
    "block",
    "presence_operation_checks",
    "non_claims",
    "presence_operation_summary",
    "presence_operation_metadata",
    "declared_presence_operation_basis",
    "upstream_basis",
    "presence_operation_material",
    "presence_operation_statement",
    "presence_operation_non_meaning",
    "operation_result_detail",
    "permitted_future_route",
    "blocked_routes",
    "what_remains_open",
}

PRESENCE_IS_NOT_FIELDS = (
    "presence_is_identity",
    "presence_is_coupling",
    "presence_is_field_machinery",
    "presence_is_runtime",
    "presence_is_api",
    "presence_is_currentness",
    "presence_is_authority",
    "presence_is_standing",
    "presence_is_output_authorization",
    "presence_is_action_authorization",
    "presence_is_derivative_reception",
    "presence_is_synchronization",
    "presence_is_follow_on_authorization",
    "presence_is_follow_on_work",
)

DOWNSTREAM_FALSE_FIELDS = (
    *PRESENCE_IS_NOT_FIELDS,
    "identity_created",
    "identity_authorized",
    "coupling_assigned_to_relation",
    "coupling_assigned_to_first_crossing_a",
    "coupling_assigned_to_first_crossing_b",
    "coupling_assigned_to_descendant_body_a",
    "coupling_assigned_to_descendant_body_b",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "relation_dissolution_authorized",
    "relation_dissolution_performed",
    "relation_reversed",
    "relation_terminated",
    "relation_erased",
    "relation_mutated",
    "relation_invalidated",
    "relation_punished",
    "relation_teardown_created",
    "living_relation_state_created",
    "living_relation_state_lapsed",
    "living_relation_state_dissolved",
    "historical_receipt_preservation_authorized",
    "historical_receipt_preserved",
    "third_candidate_created",
    "third_model_admitted",
    "standing_descendant_created",
    "descendant_standing_check_performed",
)

REPAIR_AND_DISCOVERY_FALSE_FIELDS = (
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_replaced",
    "affected_file_redeemed",
    "affected_file_treated_as_clean_basis",
    "contaminated_lineage_treated_as_clean_basis",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)

SELF_SATISFYING_FLAGS = (
    "request_presence_support_without_receiver_answerable_basis",
    "request_presence_support_by_repo_local_execution",
    "request_presence_support_by_operator_only_attestation",
    "request_presence_support_by_derivative_rendering",
    "request_presence_support_by_same_custody_countersignature",
    "request_presence_support_by_automatic_acknowledgement",
    "request_presence_support_by_generated_affirmation",
    "request_presence_support_by_forged_receiver_attestation",
    "request_presence_support_by_non_refusable_answer",
    "request_presence_support_by_declaring_side_controlled_basis",
)


class PresenceOperationResolverTests(unittest.TestCase):
    """Verify receiver-allocated presence and every bounded refusal posture."""

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(
            character if character.isalnum() or character in "._-" else "_"
            for character in safe
        )
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def without_marker(self, text: str, marker: str) -> str:
        marker_folded = marker.casefold()
        return "\n".join(
            line for line in text.splitlines() if marker_folded not in line.casefold()
        ) + "\n"

    def valid_presence_operation_spec_text(self) -> str:
        lines = ["# Synthetic Presence Operation V0 Minimum Specification"]
        for class_name, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.append(f"## {class_name}")
            lines.extend(variants[0])
        return "\n".join(lines) + "\n"

    def valid_presence_boundary_terminal_summary_text(self) -> str:
        return "\n".join(resolver.PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKERS) + "\n"

    def valid_relation_lapse_operation_terminal_summary_text(self) -> str:
        return "RELATION_LAPSE_OPERATION_RECORDED\nRELATION_LAPSE_SUPPORTED\n"

    def valid_relation_lapse_boundary_terminal_summary_text(self) -> str:
        return "RELATION_LAPSE_BOUNDARY_ALLOWED\nRELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED\n"

    def valid_relation_reversibility_operation_terminal_summary_text(self) -> str:
        return "RELATION_REVERSIBILITY_OPERATION_RECORDED\nRELATION_REVERSIBILITY_SUPPORTED\n"

    def valid_relation_operation_terminal_summary_text(self) -> str:
        return "RELATION_OPERATION_RECORDED\nRELATION_SUPPORTED\n"

    def valid_first_crossing_operation_v2_terminal_summary_text(self) -> str:
        return "FIRST_CROSSING_SUPPORTED\n"

    def valid_existence_claim_evidence_check_terminal_summary_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        ) + "\n"

    def build_valid_synthetic_request(
        self, base: Path
    ) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = {
            "presence_operation_spec_reference": self.write_markdown(
                base / "presence_operation.md", self.valid_presence_operation_spec_text()
            ),
            "presence_boundary_terminal_summary_reference": self.write_markdown(
                base / "presence_boundary.md",
                self.valid_presence_boundary_terminal_summary_text(),
            ),
            "relation_lapse_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_lapse_operation.md",
                self.valid_relation_lapse_operation_terminal_summary_text(),
            ),
            "relation_lapse_boundary_terminal_summary_reference": self.write_markdown(
                base / "relation_lapse_boundary.md",
                self.valid_relation_lapse_boundary_terminal_summary_text(),
            ),
            "relation_reversibility_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_reversibility_operation.md",
                self.valid_relation_reversibility_operation_terminal_summary_text(),
            ),
            "relation_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_operation.md",
                self.valid_relation_operation_terminal_summary_text(),
            ),
            "first_crossing_operation_v2_terminal_summary_reference": self.write_markdown(
                base / "first_crossing_operation_v2.md",
                self.valid_first_crossing_operation_v2_terminal_summary_text(),
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(
                base / "existence_claim_evidence.md",
                self.valid_existence_claim_evidence_check_terminal_summary_text(),
            ),
        }
        request = resolver.build_presence_operation_v0_min_request(
            **{key: str(value) for key, value in paths.items()}
        )
        return request, paths

    def admissible_receiver_basis(self) -> dict[str, bool]:
        return {
            "receiver_attested": True,
            "receiver_answerable_receipt_present": True,
            "receiver_answerable_basis_custody_distinct": True,
            "receiver_answerable_basis_controlled_by_declaring_side": False,
            "receiver_answerable_basis_refusable": True,
            "receiver_answerable_basis_could_have_been_withheld": True,
            "repo_local_execution_only": False,
            "operator_only_attestation": False,
            "derivative_rendering_attestation": False,
            "same_custody_countersignature": False,
            "automatic_acknowledgement": False,
            "generated_affirmation": False,
            "forged_receiver_attestation": False,
            "inadmissible_receiver_basis": False,
        }

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        summary = result.get("presence_operation_summary")
        self.assertIsInstance(summary, dict)
        return summary["failed_check_count"]

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        records = result.get("presence_operation_checks")
        self.assertIsInstance(records, list)
        for record in records:
            self.assertIsInstance(record, dict)
            for key in ("block_code", "failure_code"):
                code = record.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, (key, code))

    def assert_required_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_operation_has_no_wrapper_fields(self, result: dict[str, Any]) -> None:
        operation = result.get("presence_operation")
        self.assertIsInstance(operation, dict)
        for key in OPERATION_WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def assert_presence_operation_material_outside_operation(
        self, result: dict[str, Any]
    ) -> None:
        self.assertIn("presence_operation_material", result)
        self.assertNotIn("presence_operation_material", result["presence_operation"])

    def assert_non_conversion_posture(self, result: dict[str, Any]) -> None:
        operation = result.get("presence_operation")
        self.assertIsInstance(operation, dict)
        self.assertEqual(operation["operation_type"], "PRESENCE_OPERATION")
        for key in (*DOWNSTREAM_FALSE_FIELDS, *REPAIR_AND_DISCOVERY_FALSE_FIELDS):
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)
        self.assert_required_false_non_claims(result)
        self.assert_operation_has_no_wrapper_fields(result)
        self.assert_presence_operation_material_outside_operation(result)

    def assert_waiting_not_blocked_or_supported(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(self.block_code(result))
        operation = result["presence_operation"]
        self.assertEqual(operation["presence_result"], "REQUIRES_RECEIVER_ATTESTATION")
        self.assertIs(operation["presence_operation_recorded"], True)
        self.assertIs(operation["presence_evaluation_performed"], True)
        self.assertIs(operation["presence_result_recorded"], True)
        self.assertIs(operation["presence_operation_requires_receiver_attestation"], True)
        self.assertIs(operation["receiver_attestation_required"], True)
        self.assertIs(operation["receiver_answerable_basis_required"], True)
        for key in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(operation[key], False, key)
        self.assertTrue(
            result["operation_result_detail"][
                "missing_or_insufficient_receiver_answerable_basis"
            ]
        )
        self.assert_all_emitted_codes_public(result)
        self.assert_non_conversion_posture(result)

    def assert_supported_with_admissible_receiver_basis(
        self, result: dict[str, Any]
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(self.block_code(result))
        operation = result["presence_operation"]
        self.assertEqual(operation["presence_result"], resolver.PRESENCE_RESULT)
        for key in (
            "presence_operation_recorded",
            "presence_evaluation_performed",
            "presence_result_recorded",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "receiver_attested",
            "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            self.assertIs(operation[key], True, key)
        self.assertIs(operation["receiver_answerable_basis_controlled_by_declaring_side"], False)
        self.assertIs(operation["repo_local_execution_only"], False)
        self.assertEqual(
            result["operation_result_detail"][
                "missing_or_insufficient_receiver_answerable_basis"
            ],
            [],
        )
        self.assert_all_emitted_codes_public(result)
        self.assert_non_conversion_posture(result)

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIs(result["block"]["blocked"], True)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_non_conversion_posture(result)

    def test_01_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_presence_operation_v0_min",
            "resolve_presence_operation_v0_min_from_path",
            "write_presence_operation_v0_min_result",
            "build_presence_operation_v0_min_summary",
            "build_presence_operation_v0_min_request",
            "build_declared_presence_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)

        expected_constants = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_presence_operation_v0_min",
            "OPERATION_ID": "presence_operation_001",
            "OPERATION_TYPE": "PRESENCE_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_RECEIVER_ATTESTATION_REQUIREMENT_ONLY",
            "PRIOR_PRESENCE_BOUNDARY_TYPE": "PRESENCE_BOUNDARY",
            "PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED": "PRESENCE_BOUNDARY_ALLOWED",
            "PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED": "PRESENCE_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "PRESENCE_OPERATION_WITH_RECEIVER_ATTESTATION_THEN_IDENTITY_OR_COUPLING_BOUNDARY_CONSIDERATION_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_LAPSE_ID": "relation_lapse_001",
            "RELATION_LAPSE_SCOPE": "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY",
            "PRESENCE_ID": "presence_001",
            "PRESENCE_SCOPE": "PRESENCE_AFTER_RELATION_LAPSE_WITH_RECEIVER_ATTESTATION_ONLY",
            "PRESENCE_RESULT": "PRESENCE_SUPPORTED",
            "RECEIVER_ANSWERABLE_BASIS_ID": "receiver_answerable_basis_001",
            "RECEIVER_ANSWERABLE_BASIS_TYPE": "RECEIVER_SIDE_ANSWERABLE_BASIS",
            "RECEIVER_ANSWERABLE_BASIS_SCOPE": "CUSTODY_DISTINCT_REFUSABLE_RECEIVER_ATTESTATION_OR_EXTERNAL_ANSWERABLE_RECEIPT_ONLY",
        }
        for name, expected in expected_constants.items():
            self.assertEqual(getattr(resolver, name), expected, name)

        for name in (
            "PRIOR_PRESENCE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_RELATION_LAPSE_OPERATION_REFERENCED_REQUIRED",
            "PRIOR_RELATION_RECORD_REFERENCED_REQUIRED",
            "PRIOR_RELATION_BASIS_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True, name)
        for name in (
            "PRIOR_PRESENCE_SUPPORTED_REQUIRED",
            "PRIOR_PRESENCE_AUTHORIZED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_PRESENCE_RECORDED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_IDENTITY_AUTHORIZED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_FIELD_MACHINERY_CREATED_REQUIRED",
            "PRIOR_RUNTIME_CREATED_REQUIRED",
            "PRIOR_API_CREATED_REQUIRED",
            "PRIOR_CURRENTNESS_CREATED_REQUIRED",
            "PRIOR_AUTHORITY_CREATED_REQUIRED",
            "PRIOR_STANDING_CREATED_REQUIRED",
            "PRIOR_OUTPUT_AUTHORIZED_REQUIRED",
            "PRIOR_ACTION_AUTHORIZED_REQUIRED",
            "PRIOR_DERIVATIVE_RECEPTION_AUTHORIZED_REQUIRED",
            "PRIOR_SYNCHRONIZATION_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False, name)

        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_SUPPORTED,
                resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION,
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_NOT_RECORDED,
            },
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_presence_operation_v0_min"
            )
        )
        self.assertTrue(REQUIRED_PUBLIC_BLOCK_CODES.issubset(set(resolver.BLOCK_CODES)))
        self.assertTrue(set(SELF_SATISFYING_FLAGS).issubset(resolver.PROHIBITED_REQUEST_FLAGS))
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )

        request = resolver.build_presence_operation_v0_min_request()
        declared = resolver.build_declared_presence_operation_v0_min_request()
        self.assertEqual(request, declared)
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        for key, expected in resolver.EXPECTED_REQUEST_VALUES.items():
            if isinstance(expected, bool):
                self.assertIs(request[key], expected, key)
            else:
                self.assertEqual(request[key], expected, key)
        for key in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(request[key], False, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)
        self.assertIs(request["repo_local_execution_only"], True)
        self.assertIn("Presence is receiver-allocated", self.valid_presence_operation_spec_text())
        self.assertIn(
            "relation_001 must not become landlord of the between",
            self.valid_presence_operation_spec_text(),
        )

    def test_02_default_synthetic_request_records_lawful_waiting_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_operation_v0_min(request)

        self.assert_waiting_not_blocked_or_supported(result)
        self.assertTrue(REQUIRED_TOP_LEVEL_SECTIONS.issubset(result))
        summary = result["presence_operation_summary"]
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        operation = result["presence_operation"]
        self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["prior_presence_boundary_type"], resolver.PRIOR_PRESENCE_BOUNDARY_TYPE)
        self.assertEqual(
            operation["prior_presence_boundary_outcome_required"],
            resolver.PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED,
        )
        self.assertEqual(
            operation["prior_presence_boundary_result_required"],
            resolver.PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED,
        )
        for key in (
            "prior_presence_operation_consideration_allowed_required",
            "prior_relation_lapse_operation_referenced_required",
            "prior_relation_record_referenced_required",
            "prior_relation_basis_referenced_required",
            "relation_record_referenced",
            "relation_basis_referenced",
            "presence_boundary_referenced",
        ):
            self.assertIs(operation[key], True, key)
        for key in resolver.RECEIVER_BASIS_FIELDS:
            self.assertEqual(operation[key], resolver.RECEIVER_BASIS_DEFAULTS[key], key)
        marker_values = {
            value for key, value in summary.items() if key.endswith("markers_present")
        }
        self.assertEqual(marker_values, {True})

    def test_03_admissible_receiver_basis_records_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            request.update(self.admissible_receiver_basis())
            result = resolver.resolve_presence_operation_v0_min(request)

        self.assert_supported_with_admissible_receiver_basis(result)
        for key in (
            "operator_only_attestation",
            "derivative_rendering_attestation",
            "same_custody_countersignature",
            "automatic_acknowledgement",
            "generated_affirmation",
            "forged_receiver_attestation",
            "inadmissible_receiver_basis",
        ):
            self.assertIs(result["presence_operation"][key], False, key)

    def test_04_presence_operation_material_has_exact_bounded_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            waiting = resolver.resolve_presence_operation_v0_min(request)
            supported_request = copy.deepcopy(request)
            supported_request.update(self.admissible_receiver_basis())
            supported = resolver.resolve_presence_operation_v0_min(supported_request)

        for name, result, source_request in (
            ("waiting", waiting, request),
            ("supported", supported, supported_request),
        ):
            with self.subTest(path=name):
                material = result["presence_operation_material"]
                self.assertEqual(
                    set(material),
                    {
                        "presence_boundary_reference",
                        "receiver_answerable_basis_evaluation",
                        "presence_result_evaluation",
                    },
                )
                boundary = material["presence_boundary_reference"]
                self.assertEqual(boundary["prior_presence_boundary_type"], resolver.PRIOR_PRESENCE_BOUNDARY_TYPE)
                self.assertEqual(
                    boundary["prior_presence_boundary_outcome"],
                    resolver.PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED,
                )
                self.assertEqual(
                    boundary["prior_presence_boundary_result"],
                    resolver.PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED,
                )
                for key in (
                    "prior_presence_operation_consideration_allowed",
                    "prior_relation_lapse_operation_referenced",
                    "prior_relation_record_referenced",
                    "prior_relation_basis_referenced",
                ):
                    self.assertIs(boundary[key], True, key)
                for key, value in boundary.items():
                    if key.startswith("prior_") and key not in {
                        "prior_presence_boundary_type",
                        "prior_presence_boundary_outcome",
                        "prior_presence_boundary_result",
                        "prior_presence_operation_consideration_allowed",
                        "prior_relation_lapse_operation_referenced",
                        "prior_relation_record_referenced",
                        "prior_relation_basis_referenced",
                    }:
                        self.assertIs(value, False, key)

                receiver = material["receiver_answerable_basis_evaluation"]
                self.assertEqual(receiver["receiver_answerable_basis_id"], resolver.RECEIVER_ANSWERABLE_BASIS_ID)
                self.assertEqual(receiver["receiver_answerable_basis_type"], resolver.RECEIVER_ANSWERABLE_BASIS_TYPE)
                self.assertEqual(receiver["receiver_answerable_basis_scope"], resolver.RECEIVER_ANSWERABLE_BASIS_SCOPE)
                self.assertIs(receiver["receiver_attestation_required"], True)
                self.assertIs(receiver["receiver_answerable_basis_required"], True)
                for key in resolver.RECEIVER_BASIS_FIELDS:
                    self.assertEqual(receiver[key], source_request[key], key)
                missing = receiver["missing_or_insufficient_receiver_answerable_basis"]
                self.assertTrue(missing if name == "waiting" else not missing)

                evaluation = material["presence_result_evaluation"]
                self.assertEqual(evaluation["presence_id"], resolver.PRESENCE_ID)
                self.assertEqual(evaluation["presence_scope"], resolver.PRESENCE_SCOPE)
                self.assertEqual(
                    evaluation["presence_result"],
                    "REQUIRES_RECEIVER_ATTESTATION" if name == "waiting" else resolver.PRESENCE_RESULT,
                )
                self.assertIs(
                    evaluation["presence_operation_requires_receiver_attestation"],
                    name == "waiting",
                )
                for key in (
                    "presence_supported",
                    "presence_authorized",
                    "presence_established",
                    "presence_recorded",
                ):
                    self.assertIs(evaluation[key], name == "supported", key)
                for key in PRESENCE_IS_NOT_FIELDS:
                    self.assertIs(evaluation[key], False, key)
                self.assert_non_conversion_posture(result)

    def test_05_default_live_repo_target_waits_for_receiver_basis_when_present(self) -> None:
        request = resolver.build_presence_operation_v0_min_request()
        references = [request["presence_operation_spec_reference"]]
        references.extend(request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS)
        missing = [
            reference
            for reference in references
            if not (REPO_ROOT / Path(reference)).is_file()
        ]
        if missing:
            self.skipTest(f"required default files are absent: {missing}")
        result = resolver.resolve_presence_operation_v0_min(request)
        self.assert_waiting_not_blocked_or_supported(result)
        operation = result["presence_operation"]
        self.assertIs(operation["repo_local_execution_only"], True)
        for key in (
            "receiver_attested",
            "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            self.assertIs(operation[key], False, key)
        for key in ("relation_record_referenced", "relation_basis_referenced", "presence_boundary_referenced"):
            self.assertIs(operation[key], True, key)
        marker_values = {
            value
            for key, value in result["presence_operation_summary"].items()
            if key.endswith("markers_present")
        }
        self.assertEqual(marker_values, {True})

    def test_06_missing_or_corrupt_boundary_and_upstream_allowance_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)

            for field, markers in (
                (
                    "presence_boundary_terminal_summary_reference",
                    resolver.PRESENCE_BOUNDARY_TERMINAL_SUMMARY_MARKERS,
                ),
                (
                    "relation_lapse_operation_terminal_summary_reference",
                    ("RELATION_LAPSE_OPERATION_RECORDED", "RELATION_LAPSE_SUPPORTED"),
                ),
                (
                    "relation_lapse_boundary_terminal_summary_reference",
                    ("RELATION_LAPSE_BOUNDARY_ALLOWED", "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"),
                ),
                (
                    "relation_reversibility_operation_terminal_summary_reference",
                    ("RELATION_REVERSIBILITY_OPERATION_RECORDED", "RELATION_REVERSIBILITY_SUPPORTED"),
                ),
                (
                    "relation_operation_terminal_summary_reference",
                    ("RELATION_OPERATION_RECORDED", "RELATION_SUPPORTED"),
                ),
                (
                    "first_crossing_operation_v2_terminal_summary_reference",
                    ("FIRST_CROSSING_SUPPORTED",),
                ),
                (
                    "existence_claim_evidence_check_terminal_summary_reference",
                    ("UNSUPPORTED",),
                ),
            ):
                with self.subTest(missing_reference=field):
                    candidate = copy.deepcopy(request)
                    candidate[field] = str(base / "missing" / f"{field}.md")
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)

                original = paths[field].read_text(encoding="utf-8")
                for index, marker in enumerate(markers):
                    with self.subTest(corrupt_reference=field, marker=marker):
                        path = base / "corrupt" / field / self.safe_json_filename(marker, index).replace(".json", ".md")
                        self.write_markdown(path, self.without_marker(original, marker))
                        candidate = copy.deepcopy(request)
                        candidate[field] = str(path)
                        result = resolver.resolve_presence_operation_v0_min(candidate)
                        self.assert_blocked_with_public_code(result)
                        self.assertNotEqual(result["outcome"], resolver.OUTCOME_SUPPORTED)
                        self.assertNotEqual(
                            result["outcome"], resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION
                        )

    def test_07_receiver_basis_insufficiencies_never_support_presence(self) -> None:
        corruptions: tuple[tuple[str, Any], ...] = (
            ("receiver_attested", False),
            ("receiver_answerable_receipt_present", False),
            ("receiver_answerable_basis_custody_distinct", False),
            ("receiver_answerable_basis_controlled_by_declaring_side", True),
            ("receiver_answerable_basis_refusable", False),
            ("receiver_answerable_basis_could_have_been_withheld", False),
            ("repo_local_execution_only", True),
            ("operator_only_attestation", True),
            ("derivative_rendering_attestation", True),
            ("same_custody_countersignature", True),
            ("automatic_acknowledgement", True),
            ("generated_affirmation", True),
            ("forged_receiver_attestation", True),
            ("inadmissible_receiver_basis", True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            request.update(self.admissible_receiver_basis())
            for field, value in corruptions:
                with self.subTest(receiver_basis=field):
                    candidate = copy.deepcopy(request)
                    candidate[field] = value
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_SUPPORTED)
                    if result["outcome"] == resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION:
                        self.assert_waiting_not_blocked_or_supported(result)
                    else:
                        self.assert_blocked_with_public_code(result)

    def test_08_prohibited_self_satisfying_presence_requests_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for flag in SELF_SATISFYING_FLAGS:
                with self.subTest(flag=flag):
                    candidate = copy.deepcopy(request)
                    candidate[flag] = True
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result), resolver.PROHIBITED_REQUEST_FLAGS[flag]
                    )

    def test_09_do_not_record_intent_does_not_evaluate_support(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            request.update(self.admissible_receiver_basis())
            request["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_presence_operation_v0_min(request)

        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(self.block_code(result))
        operation = result["presence_operation"]
        self.assertEqual(operation["presence_result"], "NOT_EVALUATED")
        for key in (
            "presence_operation_recorded",
            "presence_evaluation_performed",
            "presence_result_recorded",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_operation_requires_receiver_attestation",
        ):
            self.assertIs(operation[key], False, key)
        self.assert_non_conversion_posture(result)

    def test_10_explicit_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            request["intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_presence_operation_v0_min(request)
        self.assert_blocked_with_public_code(result)
        self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")

    def test_11_request_shape_and_exact_field_mismatches_block(self) -> None:
        self.assert_blocked_with_public_code(resolver.resolve_presence_operation_v0_min([]))
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_INTENT_VALUE"
            result = resolver.resolve_presence_operation_v0_min(unsupported)
            self.assert_blocked_with_public_code(result)
            self.assertEqual(self.block_code(result), "UNSUPPORTED_INTENT")

            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    candidate = copy.deepcopy(request)
                    candidate[field] = not expected if isinstance(expected, bool) else f"wrong::{field}"
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "REQUEST_VALUE_MISMATCH")

    def test_12_marker_validation_blocks_each_target_and_upstream_class(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            spec_text = paths["presence_operation_spec_reference"].read_text(encoding="utf-8")
            for index, (class_name, variants) in enumerate(resolver.TARGET_SPEC_MARKER_CLASSES):
                marker = variants[0][0]
                with self.subTest(target_class=class_name):
                    path = base / "target_classes" / self.safe_json_filename(class_name, index).replace(".json", ".md")
                    self.write_markdown(path, self.without_marker(spec_text, marker))
                    candidate = copy.deepcopy(request)
                    candidate["presence_operation_spec_reference"] = str(path)
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result), "PRESENCE_OPERATION_SPEC_MARKER_MISSING"
                    )

            representative_upstream = (
                ("presence_boundary_terminal_summary_reference", "PRESENCE_BOUNDARY_ALLOWED"),
                ("relation_lapse_operation_terminal_summary_reference", "RELATION_LAPSE_OPERATION_RECORDED"),
                ("relation_lapse_boundary_terminal_summary_reference", "RELATION_LAPSE_BOUNDARY_ALLOWED"),
                ("relation_reversibility_operation_terminal_summary_reference", "RELATION_REVERSIBILITY_OPERATION_RECORDED"),
                ("relation_operation_terminal_summary_reference", "RELATION_OPERATION_RECORDED"),
                ("first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
                ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            )
            for index, (field, marker) in enumerate(representative_upstream):
                with self.subTest(upstream_class=field):
                    original = paths[field].read_text(encoding="utf-8")
                    path = base / "upstream_classes" / self.safe_json_filename(field, index).replace(".json", ".md")
                    self.write_markdown(path, self.without_marker(original, marker))
                    candidate = copy.deepcopy(request)
                    candidate[field] = str(path)
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)

    def test_13_every_general_prohibited_request_flag_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    candidate = copy.deepcopy(request)
                    candidate[flag] = True
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_14_false_top_level_preclaims_block_except_bounded_receiver_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            receiver_inputs = set(resolver.ADMISSIBLE_RECEIVER_TRUE_INPUT_FIELDS)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                candidate = copy.deepcopy(request)
                candidate[key] = True
                with self.subTest(top_level_key=key):
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    if key in receiver_inputs:
                        self.assert_waiting_not_blocked_or_supported(result)
                    else:
                        self.assert_blocked_with_public_code(result)
            for key in resolver.PURE_OUTPUT_PRECLAIM_FIELDS:
                with self.subTest(pure_output_preclaim=key):
                    candidate = copy.deepcopy(request)
                    candidate[key] = True
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")

    def test_15_declared_non_claims_are_required_and_canonicalized_false(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_non_claim=key):
                    candidate = copy.deepcopy(request)
                    candidate["declared_non_claims"][key] = True
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)

            malformed: tuple[tuple[str, Any], ...] = (
                ("missing", None),
                ("non_mapping", []),
                (
                    "missing_key",
                    {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]},
                ),
                (
                    "non_bool",
                    {
                        **request["declared_non_claims"],
                        resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false",
                    },
                ),
            )
            for name, value in malformed:
                with self.subTest(malformed_declared_non_claims=name):
                    candidate = copy.deepcopy(request)
                    if name == "missing":
                        candidate.pop("declared_non_claims")
                    else:
                        candidate["declared_non_claims"] = value
                    result = resolver.resolve_presence_operation_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_16_path_and_write_behavior_is_bounded_to_presence_operation_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, _ = self.build_valid_synthetic_request(base / "basis")
            waiting_path = base / "requests" / "waiting.json"
            waiting_path.parent.mkdir(parents=True, exist_ok=True)
            waiting_path.write_text(json.dumps(request), encoding="utf-8")
            waiting = resolver.resolve_presence_operation_v0_min_from_path(waiting_path)
            self.assert_waiting_not_blocked_or_supported(waiting)

            supported_request = copy.deepcopy(request)
            supported_request.update(self.admissible_receiver_basis())
            supported_path = base / "requests" / "supported.json"
            supported_path.write_text(json.dumps(supported_request), encoding="utf-8")
            supported = resolver.resolve_presence_operation_v0_min_from_path(supported_path)
            self.assert_supported_with_admissible_receiver_basis(supported)

            for name, payload in (("missing", None), ("malformed", "{"), ("array", "[]")):
                with self.subTest(path_case=name):
                    path = base / "path_cases" / self.safe_json_filename(name)
                    if payload is not None:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(payload, encoding="utf-8")
                    result = resolver.resolve_presence_operation_v0_min_from_path(path)
                    self.assert_blocked_with_public_code(result)

            output = base / "output" / resolver.DETERMINISTIC_FILENAME
            first = resolver.write_presence_operation_v0_min_result(waiting, output)
            second = resolver.write_presence_operation_v0_min_result(waiting, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("presence_operation_v0_min_result", first.name)
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION)

            default_output = REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            default_text = str(default_output).casefold()
            self.assertIn(
                "integrity_host_v0_min_coexistence_presence_operation_v0_min",
                default_text,
            )
            for prohibited_root in (
                "integrity_host_v0_min_coexistence_presence_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_reversibility_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_boundary_v0_min",
                "first_crossing_operation_v2",
                "first_crossing_operation_v1",
                "first_crossing_boundary",
                "descendant_body_creation_operation",
                "candidate_standing_operation",
                "integrity_host_v0_min_coexistence_runtime",
                "integrity_host_v0_min_coexistence_daemon",
                "integrity_host_v0_min_coexistence_api",
                "integrity_host_v0_min_coexistence_field",
                "integrity_host_v0_min_coexistence_identity",
                "integrity_host_v0_min_coexistence_coupling",
                "integrity_host_v0_min_coexistence_externalization",
            ):
                self.assertNotIn(prohibited_root, default_text, prohibited_root)

    def test_17_resolver_does_not_mutate_inputs_or_referenced_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            request["hostile_sentinel"] = {
                "nested": ["do-not-mutate", {"value": True}],
                "path": "../../reference/IAMMAI/do-not-touch",
            }
            request_before = copy.deepcopy(request)
            files_before = {
                key: path.read_bytes() for key, path in paths.items()
            }
            contaminated_path = REPO_ROOT / "spec" / "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
            contaminated_before = contaminated_path.read_bytes()
            result = resolver.resolve_presence_operation_v0_min(request)
            self.assert_waiting_not_blocked_or_supported(result)
            self.assertEqual(request, request_before)
            self.assertEqual(
                {key: path.read_bytes() for key, path in paths.items()},
                files_before,
            )
            self.assertEqual(contaminated_path.read_bytes(), contaminated_before)
            for key, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                self.assertEqual(request[key], expected, key)
            for key in resolver.PROHIBITED_REQUEST_FLAGS:
                self.assertIs(request[key], False, key)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIs(request["declared_non_claims"][key], False, key)

    def test_18_summary_preserves_waiting_and_supported_postures(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            waiting_result = resolver.resolve_presence_operation_v0_min(request)
            supported_request = copy.deepcopy(request)
            supported_request.update(self.admissible_receiver_basis())
            supported_result = resolver.resolve_presence_operation_v0_min(supported_request)

        waiting = resolver.build_presence_operation_v0_min_summary(waiting_result)
        supported = resolver.build_presence_operation_v0_min_summary(supported_result)
        for summary in (waiting, supported):
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(summary["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(summary["prior_presence_boundary_type"], resolver.PRIOR_PRESENCE_BOUNDARY_TYPE)
            self.assertEqual(
                summary["prior_presence_boundary_outcome_required"],
                resolver.PRIOR_PRESENCE_BOUNDARY_OUTCOME_REQUIRED,
            )
            self.assertEqual(
                summary["prior_presence_boundary_result_required"],
                resolver.PRIOR_PRESENCE_BOUNDARY_RESULT_REQUIRED,
            )
            self.assertEqual(summary["relation_id"], resolver.RELATION_ID)
            self.assertEqual(summary["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
            self.assertEqual(
                summary["selected_presence_operation_spec_path"],
                request["presence_operation_spec_reference"],
            )
            self.assertEqual(
                summary["completed_presence_boundary_terminal_summary_path"],
                request["presence_boundary_terminal_summary_reference"],
            )
            marker_values = {
                value for key, value in summary.items() if key.endswith("markers_present")
            }
            self.assertEqual(marker_values, {True})
            for key in set(DOWNSTREAM_FALSE_FIELDS).intersection(
                resolver.SUMMARY_POSTURE_FIELDS
            ):
                self.assertIs(summary[key], False, key)

        self.assertEqual(waiting["outcome"], resolver.OUTCOME_REQUIRES_RECEIVER_ATTESTATION)
        self.assertEqual(waiting["presence_result"], "REQUIRES_RECEIVER_ATTESTATION")
        self.assertIs(waiting["presence_operation_requires_receiver_attestation"], True)
        self.assertIs(waiting["receiver_attestation_required"], True)
        self.assertIs(waiting["repo_local_execution_only"], True)
        self.assertTrue(waiting["missing_or_insufficient_receiver_answerable_basis"])
        for key in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "receiver_attested",
            "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            self.assertIs(waiting[key], False, key)

        self.assertEqual(supported["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertEqual(supported["presence_result"], resolver.PRESENCE_RESULT)
        for key in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "receiver_attested",
            "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            self.assertIs(supported[key], True, key)
        self.assertIs(supported["receiver_answerable_basis_controlled_by_declaring_side"], False)
        self.assertIs(supported["repo_local_execution_only"], False)
        self.assertEqual(supported["missing_or_insufficient_receiver_answerable_basis"], [])

    def test_19_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_operation_v0_min(request)
            summary = resolver.build_presence_operation_v0_min_summary(result)

        self.assert_waiting_not_blocked_or_supported(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_presence_operation_v0_min")
        self.assertEqual(summary["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(summary["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(summary["presence_result"], "REQUIRES_RECEIVER_ATTESTATION")
        self.assertIs(summary["presence_operation_requires_receiver_attestation"], True)
        self.assertIs(summary["receiver_attestation_required"], True)
        self.assertIs(summary["receiver_answerable_basis_required"], True)
        self.assertTrue(summary["missing_or_insufficient_receiver_answerable_basis"])
        self.assertEqual(
            set(result["presence_operation_material"]),
            {
                "presence_boundary_reference",
                "receiver_answerable_basis_evaluation",
                "presence_result_evaluation",
            },
        )
        self.assert_operation_has_no_wrapper_fields(result)
        self.assert_presence_operation_material_outside_operation(result)
        self.assert_required_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
