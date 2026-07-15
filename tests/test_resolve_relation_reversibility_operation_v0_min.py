"""Tests for one bounded relation-reversibility operation result.

The operation may record historical-relation reversibility support only after a
completed boundary allowance.  These tests keep every conversion route,
living-state posture, repair route, and downstream authorization out of scope.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPOSITORY_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_reversibility_operation_v0_min as resolver


class RelationReversibilityOperationV0MinTests(unittest.TestCase):
    """Exercise the bounded operation without creating a relation conversion."""

    _WRAPPER_FIELDS = (
        "outcome",
        "block",
        "relation_reversibility_operation_checks",
        "non_claims",
        "relation_reversibility_operation_summary",
        "relation_reversibility_operation_metadata",
        "relation_reversibility_operation_material",
    )
    _CONVERSION_FIELDS = (
        "relation_record_is_living_relation_state",
        "living_relation_state_created",
        "living_relation_state_lapsed",
        "living_relation_state_dissolved",
        "relation_lapse_authorized",
        "relation_lapse_performed",
        "relation_dissolution_authorized",
        "relation_dissolution_performed",
        "relation_reversed",
        "relation_terminated",
        "relation_erased",
        "relation_mutated",
        "relation_invalidated",
        "relation_punished",
        "relation_teardown_created",
        "historical_receipt_preservation_authorized",
        "historical_receipt_preserved",
        "presence_boundary_authorized",
        "presence_established",
        "identity_created",
        "field_machinery_created",
        "runtime_created",
        "api_created",
        "currentness_created",
        "authority_created",
        "coupling_created",
        "third_candidate_created",
        "third_model_admitted",
        "standing_descendant_created",
        "descendant_standing_check_performed",
        "follow_on_authorized",
        "follow_on_work_authorized",
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def _write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _target_spec_text(self) -> str:
        markers: list[str] = ["# Synthetic Relation Reversibility Operation V0 Minimum Specification"]
        for _, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            markers.extend(variants[0])
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _upstream_text(self, field: str) -> str:
        for requirement in resolver.UPSTREAM_REQUIREMENTS:
            if requirement[0] == field:
                return "# Synthetic upstream terminal summary\n" + "\n".join(requirement[4][0]) + "\n"
        self.fail(f"unknown upstream field: {field}")

    def _remove_marker(self, text: str, marker: str) -> str:
        """Remove a marker case-insensitively so aliases cannot retain it."""
        return re.sub(re.escape(marker), "removed_marker", text, flags=re.IGNORECASE)

    def _boundary_summary_text(self) -> str:
        return self._upstream_text("relation_reversibility_boundary_terminal_summary_reference")

    def _relation_operation_summary_text(self) -> str:
        return self._upstream_text("relation_operation_terminal_summary_reference")

    def _first_crossing_summary_text(self) -> str:
        return self._upstream_text("first_crossing_operation_v2_terminal_summary_reference")

    def _existence_claim_summary_text(self) -> str:
        return self._upstream_text("existence_claim_evidence_check_terminal_summary_reference")

    def _valid_synthetic_request(self, root: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        references = {
            "relation_reversibility_operation_spec_reference": self._write_markdown(
                root / "target" / "relation_reversibility_operation_spec.md", self._target_spec_text()
            ),
            "relation_reversibility_boundary_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "relation_reversibility_boundary_terminal_summary.md", self._boundary_summary_text()
            ),
            "relation_operation_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "relation_operation_terminal_summary.md", self._relation_operation_summary_text()
            ),
            "first_crossing_operation_v2_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "first_crossing_operation_v2_terminal_summary.md", self._first_crossing_summary_text()
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "existence_claim_evidence_check_terminal_summary.md", self._existence_claim_summary_text()
            ),
        }
        request = resolver.build_relation_reversibility_operation_v0_min_request(
            **{field: str(path) for field, path in references.items()}
        )
        return request, references

    def _summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("relation_reversibility_operation_summary")
        self.assertIsInstance(summary, Mapping)
        return summary

    def _operation(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        operation = result.get("relation_reversibility_operation")
        self.assertIsInstance(operation, Mapping)
        return operation

    def _block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def _failed_check_count(self, result: Mapping[str, Any]) -> int:
        return int(self._summary(result).get("failed_check_count", -1))

    def assert_recorded_not_blocked(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(self._failed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_requires_boundary_allowance_not_blocked(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_blocked_with_public_code(self, result: Mapping[str, Any], expected: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertGreater(self._failed_check_count(result), 0)
        code = self._block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected is not None:
            self.assertEqual(code, expected)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_conversion_posture(result)

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        checks = result.get("relation_reversibility_operation_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, Mapping):
                continue
            for name in ("block_code", "failure_code"):
                code = check.get(name)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)
            self.assertIsInstance(non_claims[field], bool, field)

    def assert_operation_not_wrapper(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        for field in self._WRAPPER_FIELDS:
            self.assertNotIn(field, operation)

    def assert_no_conversion_posture(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        for field in self._CONVERSION_FIELDS:
            self.assertIs(operation.get(field), False, field)

    def _assert_recorded_operation(self, result: Mapping[str, Any]) -> None:
        self.assert_recorded_not_blocked(result)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertGreater(self._summary(result).get("passed_check_count", 0), 0)
        operation = self._operation(result)
        self.assertEqual(operation.get("operation_id"), resolver.OPERATION_ID)
        self.assertEqual(operation.get("operation_type"), resolver.OPERATION_TYPE)
        self.assertEqual(operation.get("operation_version"), resolver.OPERATION_VERSION)
        self.assertEqual(operation.get("operation_scope"), resolver.OPERATION_SCOPE)
        self.assertEqual(operation.get("prior_relation_reversibility_boundary_type"), resolver.PRIOR_RELATION_REVERSIBILITY_BOUNDARY_TYPE)
        self.assertEqual(operation.get("prior_relation_reversibility_boundary_outcome_required"), resolver.PRIOR_RELATION_REVERSIBILITY_BOUNDARY_OUTCOME_REQUIRED)
        self.assertEqual(operation.get("prior_relation_reversibility_boundary_result_required"), resolver.PRIOR_RELATION_REVERSIBILITY_BOUNDARY_RESULT_REQUIRED)
        self.assertEqual(operation.get("relation_reversibility_result"), "RELATION_REVERSIBILITY_SUPPORTED")
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation.get(field), True, field)
        self.assert_no_conversion_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_operation_not_wrapper(result)
        self.assertNotIn("relation_reversibility_operation_material", operation)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relation_reversibility_operation_v0_min",
            "resolve_relation_reversibility_operation_v0_min_from_path",
            "write_relation_reversibility_operation_v0_min_result",
            "build_relation_reversibility_operation_v0_min_summary",
            "build_relation_reversibility_operation_v0_min_request",
            "build_declared_relation_reversibility_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_relation_reversibility_operation_v0_min",
            "OPERATION_ID": "relation_reversibility_operation_001",
            "OPERATION_TYPE": "RELATION_REVERSIBILITY_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_RELATION_REVERSIBILITY_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_RELATION_REVERSIBILITY_BOUNDARY_TYPE": "RELATION_REVERSIBILITY_BOUNDARY",
            "PRIOR_RELATION_REVERSIBILITY_BOUNDARY_OUTCOME_REQUIRED": "RELATION_REVERSIBILITY_BOUNDARY_ALLOWED",
            "PRIOR_RELATION_REVERSIBILITY_BOUNDARY_RESULT_REQUIRED": "RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "RELATION_REVERSIBILITY_OPERATION_THEN_RELATION_LAPSE_OR_PRESENCE_BOUNDARY_CONSIDERATION_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_REVERSIBILITY_ID": "relation_reversibility_001",
            "RELATION_REVERSIBILITY_SCOPE": "RELATION_REVERSIBILITY_FOR_RELATION_RECORD_ONLY",
            "RELATION_LAPSE_ID": "relation_lapse_001",
            "RELATION_LAPSE_SCOPE": "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY",
            "RELATION_DISSOLUTION_ID": "relation_dissolution_001",
            "RELATION_DISSOLUTION_SCOPE": "RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_RELATION_OPERATION_REFERENCED_REQUIRED",
            "PRIOR_RELATION_RECORD_REFERENCED_REQUIRED",
            "PRIOR_RELATION_BASIS_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_RELATION_REVERSIBILITY_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_REVERSIBILITY_PERFORMED_REQUIRED",
            "PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED",
            "PRIOR_RELATION_ERASED_REQUIRED",
            "PRIOR_RELATION_MUTATED_REQUIRED",
            "PRIOR_RELATION_INVALIDATED_REQUIRED",
            "PRIOR_RELATION_PUNISHED_REQUIRED",
            "PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED",
            "PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_relation_reversibility_operation_v0_min"))
        for field in (
            "request_relation_lapse_authorization",
            "request_relation_dissolution_authorization",
            "request_relation_reversal",
            "request_relation_termination",
            "request_relation_erasure",
            "request_relation_mutation",
            "request_relation_invalidation",
            "request_presence_boundary_authorization",
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
        ):
            self.assertIn(field, resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"], "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED")
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"], "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED")
        self.assertTrue({
            "REQUEST_NOT_MAPPING",
            "REQUEST_PATH_UNREADABLE",
            "REQUEST_JSON_INVALID",
            "UNSUPPORTED_INTENT",
            "REQUEST_VALUE_MISMATCH",
            "RESULT_POSTURE_PRECLAIMED",
            "RELATION_REVERSIBILITY_OPERATION_SPEC_REFERENCE_MISSING",
            "RELATION_REVERSIBILITY_OPERATION_SPEC_MARKER_MISSING",
            "RELATION_REVERSIBILITY_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "RELATION_REVERSIBILITY_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_RELATION_LAPSE_REQUESTED",
            "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
            "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
            "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
            "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
            "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
            "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
            "PROHIBITED_PRESENCE_BOUNDARY_OR_PRESENCE_REQUESTED",
            "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
            "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
            "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
            "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
            "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        }.issubset(set(resolver.BLOCK_CODES)))

    def test_synthetic_recorded_result_and_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_reversibility_operation_v0_min(request)
            self._assert_recorded_operation(result)
            for field in (
                "relation_reversibility_operation_metadata",
                "declared_relation_reversibility_operation_basis",
                "upstream_basis",
                "relation_reversibility_operation",
                "relation_reversibility_operation_material",
                "relation_reversibility_operation_checks",
                "relation_reversibility_operation_statement",
                "relation_reversibility_operation_non_meaning",
                "operation_result_detail",
                "permitted_future_route",
                "blocked_routes",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "relation_reversibility_operation_summary",
            ):
                self.assertIn(field, result)
            material = result["relation_reversibility_operation_material"]
            self.assertEqual(set(material), {
                "boundary_allowance_reference",
                "relation_record_reversibility_evaluation",
                "reversibility_result_evaluation",
            })
            boundary = material["boundary_allowance_reference"]
            for key in (
                "prior_relation_reversibility_operation_consideration_allowed",
                "prior_relation_operation_referenced",
                "prior_relation_record_referenced",
                "prior_relation_basis_referenced",
            ):
                self.assertIs(boundary[key], True)
            for key in (
                "prior_relation_reversibility_authorized",
                "prior_relation_lapse_authorized",
                "prior_relation_dissolution_authorized",
                "prior_relation_reversibility_performed",
                "prior_relation_lapse_performed",
                "prior_relation_dissolution_performed",
                "prior_relation_erased",
                "prior_relation_mutated",
                "prior_relation_invalidated",
                "prior_relation_punished",
                "prior_relation_teardown_created",
                "prior_living_relation_state_created",
                "prior_presence_boundary_authorized",
                "prior_presence_established",
                "prior_identity_created",
                "prior_coupling_created",
                "prior_follow_on_authorized",
                "prior_follow_on_work_authorized",
            ):
                self.assertIs(boundary[key], False, key)
            evaluation = material["relation_record_reversibility_evaluation"]
            self.assertEqual(evaluation["relation_id"], resolver.RELATION_ID)
            self.assertEqual(evaluation["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
            self.assertEqual(evaluation["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
            self.assertEqual(evaluation["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
            self.assertEqual(evaluation["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
            self.assertIs(evaluation["relation_record_confirmed_as_historical_only"], True)
            for key in (
                "relation_record_is_living_relation_state",
                "relation_record_is_presence",
                "relation_record_is_identity",
                "relation_record_is_coupling",
                "relation_record_is_landlord_of_between",
                "relation_record_outranks_first_crossing_a",
                "relation_record_outranks_first_crossing_b",
                "relation_record_outranks_first_crossing_pair",
                "relation_lapse_authorized",
                "relation_dissolution_authorized",
                "relation_reversed",
                "relation_terminated",
                "relation_erased",
                "relation_mutated",
                "relation_invalidated",
                "relation_punished",
                "relation_teardown_created",
            ):
                self.assertIs(evaluation[key], False, key)
            reversibility = material["reversibility_result_evaluation"]
            self.assertEqual(reversibility["relation_reversibility_result"], "RELATION_REVERSIBILITY_SUPPORTED")
            for key in (
                "relation_reversibility_supported",
                "relation_reversibility_authorized",
                "relation_reversibility_performed",
                "relation_reversibility_recorded",
            ):
                self.assertIs(reversibility[key], True, key)
            self.assertEqual(reversibility["relation_reversibility_id"], resolver.RELATION_REVERSIBILITY_ID)
            self.assertEqual(reversibility["relation_reversibility_scope"], resolver.RELATION_REVERSIBILITY_SCOPE)
            for key, value in reversibility.items():
                if key not in {
                    "relation_reversibility_result",
                    "relation_reversibility_supported",
                    "relation_reversibility_authorized",
                    "relation_reversibility_performed",
                    "relation_reversibility_recorded",
                    "relation_reversibility_id",
                    "relation_reversibility_scope",
                }:
                    self.assertIs(value, False, key)

    def test_default_live_target_records_when_present(self) -> None:
        references = [
            resolver.DEFAULT_RELATION_REVERSIBILITY_OPERATION_SPEC_REFERENCE,
            *(requirement[1] for requirement in resolver.UPSTREAM_REQUIREMENTS),
        ]
        missing = [reference for reference in references if not (resolver.REPO_ROOT / reference).is_file()]
        if missing:
            self.skipTest(f"required default files are absent: {missing}")
        result = resolver.resolve_relation_reversibility_operation_v0_min(
            resolver.build_relation_reversibility_operation_v0_min_request()
        )
        self._assert_recorded_operation(result)

    def test_missing_or_insufficient_boundary_allowance(self) -> None:
        boundary_markers = resolver.UPSTREAM_REQUIREMENTS[0][4][0]
        non_boundary = tuple(resolver.UPSTREAM_REQUIREMENTS[1:])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, references = self._valid_synthetic_request(root)
            missing = copy.deepcopy(request)
            missing["relation_reversibility_boundary_terminal_summary_reference"] = str(root / "missing" / "boundary.md")
            result = resolver.resolve_relation_reversibility_operation_v0_min(missing)
            self.assert_requires_boundary_allowance_not_blocked(result)
            self.assertTrue(self._summary(result)["missing_or_insufficient_boundary_allowance"])
            self.assert_no_conversion_posture(result)
            self.assert_canonical_non_claims(result)

            for index, marker in enumerate(boundary_markers):
                with self.subTest(boundary_marker=marker):
                    altered = self._remove_marker(self._boundary_summary_text(), marker)
                    self._write_markdown(references["relation_reversibility_boundary_terminal_summary_reference"], altered)
                    result = resolver.resolve_relation_reversibility_operation_v0_min(request)
                    self.assert_requires_boundary_allowance_not_blocked(result)
                    self.assert_no_conversion_posture(result)
                    self.assert_canonical_non_claims(result)
            self._write_markdown(
                references["relation_reversibility_boundary_terminal_summary_reference"], self._boundary_summary_text()
            )

            for field, _, missing_code, marker_code, variants, _, _ in non_boundary:
                with self.subTest(upstream_missing=field):
                    altered = copy.deepcopy(request)
                    altered[field] = str(root / "missing" / self.safe_json_filename(field))
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), missing_code
                    )
                with self.subTest(upstream_marker=field):
                    marker = variants[0][0]
                    path = references[field]
                    self._write_markdown(path, self._upstream_text(field).replace(marker, "missing_upstream_marker"))
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(request), marker_code
                    )
                    self._write_markdown(path, self._upstream_text(field))

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            not_recorded = copy.deepcopy(request)
            not_recorded["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_relation_reversibility_operation_v0_min(not_recorded)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertEqual(self._failed_check_count(result), 0)
            operation = self._operation(result)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[field], False, field)
            self.assert_no_conversion_posture(result)
            self.assert_canonical_non_claims(result)

            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            self.assert_blocked_with_public_code(
                resolver.resolve_relation_reversibility_operation_v0_min(blocked), "EXPLICIT_BLOCK_REQUESTED"
            )

    def test_missing_target_operation_spec_reference_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            request["relation_reversibility_operation_spec_reference"] = str(
                Path(directory) / "missing" / "relation_reversibility_operation_spec.md"
            )
            self.assert_blocked_with_public_code(
                resolver.resolve_relation_reversibility_operation_v0_min(request),
                "RELATION_REVERSIBILITY_OPERATION_SPEC_REFERENCE_MISSING",
            )

    def test_malformed_request_shape_and_exact_values_block(self) -> None:
        self.assert_blocked_with_public_code(
            resolver.resolve_relation_reversibility_operation_v0_min(["not", "a", "mapping"]), "REQUEST_NOT_MAPPING"
        )
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_RELATION_REVERSIBILITY_OPERATION"
            self.assert_blocked_with_public_code(
                resolver.resolve_relation_reversibility_operation_v0_min(unsupported), "UNSUPPORTED_INTENT"
            )
            for field, value in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    altered = copy.deepcopy(request)
                    altered[field] = not value if isinstance(value, bool) else f"wrong_{value}"
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), "REQUEST_VALUE_MISMATCH"
                    )

    def test_target_and_upstream_marker_validation(self) -> None:
        marker_breaks = {
            "operation identity": "Relation Reversibility Operation V0 Minimum Specification",
            "boundary allowance": "RELATION_REVERSIBILITY_BOUNDARY_ALLOWED",
            "operation support": "RELATION_REVERSIBILITY_SUPPORTED",
            "operation non-conversion": "Relation reversibility support is not relation lapse",
            "historical relation record": "Historical receipt preservation requires a separately bounded operation",
            "landlord and rank": "Regulation may not become sovereign over Motion",
            "permitted route": resolver.ADMISSIBLE_FUTURE_ROUTE,
            "contaminated lineage preservation": "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            "blocked routes": "repository scan route",
            "closing lock": "Open means not scheduled, not authorized, and not executed",
        }
        with tempfile.TemporaryDirectory() as directory:
            request, references = self._valid_synthetic_request(Path(directory))
            target_path = references["relation_reversibility_operation_spec_reference"]
            for name, marker in marker_breaks.items():
                with self.subTest(target_marker_class=name):
                    self._write_markdown(target_path, self._remove_marker(self._target_spec_text(), marker))
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(request),
                        "RELATION_REVERSIBILITY_OPERATION_SPEC_MARKER_MISSING",
                    )
            self._write_markdown(target_path, self._target_spec_text())

            for field, _, _, marker_code, variants, _, boundary_basis in resolver.UPSTREAM_REQUIREMENTS:
                with self.subTest(upstream_marker_class=field):
                    marker = variants[0][0]
                    self._write_markdown(references[field], self._remove_marker(self._upstream_text(field), marker))
                    result = resolver.resolve_relation_reversibility_operation_v0_min(request)
                    if boundary_basis:
                        self.assert_requires_boundary_allowance_not_blocked(result)
                        self.assert_canonical_non_claims(result)
                        self.assert_no_conversion_posture(result)
                    else:
                        self.assert_blocked_with_public_code(result, marker_code)
                    self._write_markdown(references[field], self._upstream_text(field))

    def test_every_prohibited_request_flag_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            for flag, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    altered = copy.deepcopy(request)
                    altered[flag] = True
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), code
                    )

    def test_top_level_preclaims_and_declared_nonclaims_canonicalize_false(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_preclaim=field):
                    altered = copy.deepcopy(request)
                    altered[field] = True
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), "RESULT_POSTURE_PRECLAIMED"
                    )
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_nonclaim=field):
                    altered = copy.deepcopy(request)
                    altered["declared_non_claims"][field] = True
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), "NON_CLAIM_MISSING_OR_FLIPPED"
                    )
            malformed_cases: dict[str, Any] = {
                "missing": None,
                "non_mapping": [],
                "missing_key": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]},
                "non_bool": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            }
            malformed_cases["non_bool"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
            for name, value in malformed_cases.items():
                with self.subTest(declared_nonclaims_shape=name):
                    altered = copy.deepcopy(request)
                    if name == "missing":
                        altered.pop("declared_non_claims")
                    else:
                        altered["declared_non_claims"] = value
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_reversibility_operation_v0_min(altered), "NON_CLAIM_MISSING_OR_FLIPPED"
                    )

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _ = self._valid_synthetic_request(root)
            request_path = self._write_json(root / "requests" / "valid.json", request)
            result = resolver.resolve_relation_reversibility_operation_v0_min_from_path(request_path)
            self._assert_recorded_operation(result)

            missing = resolver.resolve_relation_reversibility_operation_v0_min_from_path(root / "requests" / "missing.json")
            self.assert_blocked_with_public_code(missing, "REQUEST_PATH_UNREADABLE")
            invalid_path = self._write_markdown(root / "requests" / "invalid.json", "{not valid json")
            invalid = resolver.resolve_relation_reversibility_operation_v0_min_from_path(invalid_path)
            self.assert_blocked_with_public_code(invalid, "REQUEST_JSON_INVALID")
            array_path = self._write_json(root / "requests" / "array.json", [])
            array = resolver.resolve_relation_reversibility_operation_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array, "REQUEST_NOT_MAPPING")

            output_path = root / "written" / resolver.DETERMINISTIC_FILENAME
            written = resolver.write_relation_reversibility_operation_v0_min_result(result, output_path)
            self.assertTrue(written.is_file())
            self.assertEqual(json.loads(written.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            repeated = resolver.write_relation_reversibility_operation_v0_min_result(result, output_path)
            self.assertNotEqual(written, repeated)
            self.assertTrue(repeated.name.endswith("_001.json"))
            self.assertIn("relation_reversibility_operation_v0_min_result", written.name)
            default_path = resolver.REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            self.assertIn("integrity_host_v0_min_coexistence_relation_reversibility_operation_v0_min", str(default_path))
            self.assertTrue(str(written).startswith(str(root)))
            for upstream_root in (
                "integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2",
                "integrity_host_v0_min_coexistence_first_crossing_operation_v0_min",
                "integrity_host_v0_min_coexistence_first_crossing_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_creation_operation_v0_min",
                "integrity_host_v0_min_coexistence_candidate_standing_operation_v0_min",
                "runtime",
                "daemon",
                "api",
                "field",
                "presence",
                "identity",
                "externalization",
            ):
                self.assertNotIn(upstream_root, written.parts)
            output_directory = root / "written" / "directory"
            output_directory.mkdir()
            with self.assertRaises(resolver.RelationReversibilityOperationV0MinError):
                resolver.write_relation_reversibility_operation_v0_min_result(result, output_directory)

    def test_non_mutation_of_request_and_synthetic_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, references = self._valid_synthetic_request(Path(directory))
            request["hostile_payload"] = {
                "raw_relation_body": "RAW_RELATION_BODY_MUST_NOT_RETURN",
                "nested": {"attempt": "no mutation"},
            }
            before = copy.deepcopy(request)
            file_before = {field: path.read_text(encoding="utf-8") for field, path in references.items()}
            result = resolver.resolve_relation_reversibility_operation_v0_min(request)
            self._assert_recorded_operation(result)
            self.assertEqual(request, before)
            for field, path in references.items():
                self.assertEqual(path.read_text(encoding="utf-8"), file_before[field])
            self.assertNotIn("RAW_RELATION_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_reversibility_operation_v0_min(request)
            summary = resolver.build_relation_reversibility_operation_v0_min_summary(result)
            self._assert_recorded_operation(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(summary["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(summary["relation_id"], resolver.RELATION_ID)
            self.assertEqual(summary["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
            self.assertEqual(summary["relation_reversibility_result"], "RELATION_REVERSIBILITY_SUPPORTED")
            self.assertEqual(summary["missing_or_insufficient_boundary_allowance"], [])
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(summary[field], True, field)
            for field in self._CONVERSION_FIELDS:
                self.assertIs(summary[field], False, field)


if __name__ == "__main__":
    unittest.main()
