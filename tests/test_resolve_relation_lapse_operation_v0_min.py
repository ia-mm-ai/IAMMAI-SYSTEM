"""Tests for one bounded relation-lapse operation result.

The operation may record non-punitive lapse support for a historical relation
record only after completed boundary allowance.  These tests keep dissolution,
relation conversion, living state, repair, presence, and downstream work out of
scope.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPOSITORY_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_lapse_operation_v0_min as resolver


class RelationLapseOperationV0MinTests(unittest.TestCase):
    """Exercise relation lapse without converting or dissolving relation."""

    _WRAPPER_FIELDS = (
        "outcome",
        "block",
        "result_version",
        "resolver_module",
        "relation_lapse_operation_metadata",
        "declared_relation_lapse_operation_basis",
        "upstream_basis",
        "relation_lapse_operation_material",
        "relation_lapse_operation_checks",
        "relation_lapse_operation_statement",
        "relation_lapse_operation_non_meaning",
        "operation_result_detail",
        "permitted_future_route",
        "blocked_routes",
        "what_remains_open",
        "non_claims",
        "relation_lapse_operation_summary",
    )
    _POSITIVE_RECORDED_FIELDS = frozenset(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
    _PRESERVED_FALSE_FIELDS = tuple(
        field
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS
        if field not in frozenset(resolver.ALLOWED_TRUE_RECORDED_FIELDS)
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        """Return a deterministic filename safe for subtest-generated paths."""
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

    def _relation_lapse_operation_spec_text(self) -> str:
        markers: list[str] = ["# Synthetic Relation Lapse Operation V0 Minimum Specification"]
        for _, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            markers.extend(variants[0])
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _relation_lapse_boundary_terminal_summary_text(self) -> str:
        requirement = resolver.UPSTREAM_REQUIREMENTS[0]
        return "# Synthetic Relation Lapse Boundary Terminal Summary\n" + "\n".join(requirement[4][0]) + "\n"

    def _relation_reversibility_operation_terminal_summary_text(self) -> str:
        return "\n".join((
            "# Synthetic Relation Reversibility Operation Terminal Summary",
            "RELATION_REVERSIBILITY_OPERATION_RECORDED",
            "RELATION_REVERSIBILITY_SUPPORTED",
            "",
        ))

    def _relation_operation_terminal_summary_text(self) -> str:
        return "\n".join((
            "# Synthetic Relation Operation Terminal Summary",
            "RELATION_OPERATION_RECORDED",
            "RELATION_SUPPORTED",
            "",
        ))

    def _first_crossing_operation_v2_terminal_summary_text(self) -> str:
        return "# Synthetic First Crossing Operation V2 Terminal Summary\nFIRST_CROSSING_SUPPORTED\n"

    def _existence_claim_evidence_check_terminal_summary_text(self) -> str:
        return "\n".join((
            "# Synthetic Existence Claim Evidence Check Terminal Summary",
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "",
        ))

    def _upstream_text(self, field: str) -> str:
        helpers = {
            "relation_lapse_boundary_terminal_summary_reference": self._relation_lapse_boundary_terminal_summary_text,
            "relation_reversibility_operation_terminal_summary_reference": self._relation_reversibility_operation_terminal_summary_text,
            "relation_operation_terminal_summary_reference": self._relation_operation_terminal_summary_text,
            "first_crossing_operation_v2_terminal_summary_reference": self._first_crossing_operation_v2_terminal_summary_text,
            "existence_claim_evidence_check_terminal_summary_reference": self._existence_claim_evidence_check_terminal_summary_text,
        }
        helper = helpers.get(field)
        if helper is None:
            self.fail(f"unknown upstream field: {field}")
        return helper()

    def _valid_synthetic_request(self, root: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        references = {
            "relation_lapse_operation_spec_reference": self._write_markdown(
                root / "target" / "relation_lapse_operation_spec.md",
                self._relation_lapse_operation_spec_text(),
            ),
            "relation_lapse_boundary_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "relation_lapse_boundary_terminal_summary.md",
                self._relation_lapse_boundary_terminal_summary_text(),
            ),
            "relation_reversibility_operation_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "relation_reversibility_operation_terminal_summary.md",
                self._relation_reversibility_operation_terminal_summary_text(),
            ),
            "relation_operation_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "relation_operation_terminal_summary.md",
                self._relation_operation_terminal_summary_text(),
            ),
            "first_crossing_operation_v2_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "first_crossing_operation_v2_terminal_summary.md",
                self._first_crossing_operation_v2_terminal_summary_text(),
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self._write_markdown(
                root / "upstream" / "existence_claim_evidence_check_terminal_summary.md",
                self._existence_claim_evidence_check_terminal_summary_text(),
            ),
        }
        request = resolver.build_relation_lapse_operation_v0_min_request(
            **{field: str(path) for field, path in references.items()}
        )
        return request, references

    def _remove_marker(self, text: str, marker: str) -> str:
        return re.sub(re.escape(marker), "removed_marker", text, flags=re.IGNORECASE)

    def _remove_marker_class(self, text: str, variants: tuple[tuple[str, ...], ...]) -> str:
        altered = text
        for marker in dict.fromkeys(marker for group in variants for marker in group):
            altered = self._remove_marker(altered, marker)
        return altered

    def _summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("relation_lapse_operation_summary")
        self.assertIsInstance(summary, Mapping)
        return summary

    def _operation(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        operation = result.get("relation_lapse_operation")
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

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        checks = result.get("relation_lapse_operation_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, Mapping):
                continue
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, f"{field}={code}")
        block_code = self._block_code(result)
        if block_code is not None:
            self.assertIn(block_code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIsInstance(non_claims[field], bool, field)
            self.assertIs(non_claims[field], False, field)

    def assert_operation_separate_from_wrappers(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        for field in self._WRAPPER_FIELDS:
            self.assertNotIn(field, operation)
        self.assertNotIn("relation_lapse_operation_material", operation)

    def assert_bounded_false_posture(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        for field in self._PRESERVED_FALSE_FIELDS:
            self.assertIn(field, operation)
            self.assertIs(operation[field], False, field)

    def assert_operation_required_fields_false(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, operation)
            self.assertIs(operation[field], False, field)

    def assert_all_marker_booleans_true(self, result: Mapping[str, Any]) -> None:
        operation = self._operation(result)
        summary = self._summary(result)
        checks = result.get("relation_lapse_operation_checks")
        self.assertIsInstance(checks, list)
        marker_count = 0
        for check in checks:
            if not isinstance(check, Mapping):
                continue
            name = check.get("check_name")
            if isinstance(name, str) and name.endswith("markers present"):
                marker_count += 1
                key = name.replace(" ", "_")
                self.assertIs(check.get("passed"), True, name)
                self.assertIs(operation.get(key), True, key)
                self.assertIs(summary.get(key), True, key)
        self.assertGreater(marker_count, 0)

    def assert_recorded_not_blocked(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(self._failed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assert_all_emitted_codes_public(result)

    def assert_requires_boundary_allowance_not_blocked(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_operation_required_fields_false(result)

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
        self.assert_operation_required_fields_false(result)
        self.assert_operation_separate_from_wrappers(result)

    def _assert_recorded_result(self, result: Mapping[str, Any]) -> None:
        self.assert_recorded_not_blocked(result)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertGreater(self._summary(result).get("passed_check_count", 0), 0)
        expected_sections = {
            "relation_lapse_operation_metadata",
            "declared_relation_lapse_operation_basis",
            "upstream_basis",
            "relation_lapse_operation",
            "relation_lapse_operation_material",
            "relation_lapse_operation_checks",
            "relation_lapse_operation_statement",
            "relation_lapse_operation_non_meaning",
            "operation_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "relation_lapse_operation_summary",
        }
        self.assertTrue(expected_sections.issubset(result))
        operation = self._operation(result)
        for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
            if field != "relation_lapse_result":
                self.assertEqual(operation.get(field), expected, field)
        self.assertEqual(operation.get("relation_lapse_result"), resolver.RELATION_LAPSE_RESULT)
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation.get(field), True, field)
        self.assert_bounded_false_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_operation_separate_from_wrappers(result)
        self.assert_all_marker_booleans_true(result)
        detail = result.get("operation_result_detail")
        self.assertIsInstance(detail, Mapping)
        self.assertEqual(detail.get("missing_or_insufficient_boundary_allowance"), [])
        self.assertEqual(detail.get("not_recorded_reasons"), [])

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relation_lapse_operation_v0_min",
            "resolve_relation_lapse_operation_v0_min_from_path",
            "write_relation_lapse_operation_v0_min_result",
            "build_relation_lapse_operation_v0_min_summary",
            "build_relation_lapse_operation_v0_min_request",
            "build_declared_relation_lapse_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_relation_lapse_operation_v0_min",
            "OPERATION_ID": "relation_lapse_operation_001",
            "OPERATION_TYPE": "RELATION_LAPSE_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_RELATION_LAPSE_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_RELATION_LAPSE_BOUNDARY_TYPE": "RELATION_LAPSE_BOUNDARY",
            "PRIOR_RELATION_LAPSE_BOUNDARY_OUTCOME_REQUIRED": "RELATION_LAPSE_BOUNDARY_ALLOWED",
            "PRIOR_RELATION_LAPSE_BOUNDARY_RESULT_REQUIRED": "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "RELATION_LAPSE_OPERATION_THEN_PRESENCE_BOUNDARY_OR_DISSOLUTION_BOUNDARY_CONSIDERATION_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_LAPSE_ID": "relation_lapse_001",
            "RELATION_LAPSE_SCOPE": "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY",
            "RELATION_LAPSE_RESULT": "RELATION_LAPSE_SUPPORTED",
            "RELATION_DISSOLUTION_ID": "relation_dissolution_001",
            "RELATION_DISSOLUTION_SCOPE": "RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value, name)
        for name in (
            "PRIOR_RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_RELATION_REVERSIBILITY_OPERATION_REFERENCED_REQUIRED",
            "PRIOR_RELATION_RECORD_REFERENCED_REQUIRED",
            "PRIOR_RELATION_BASIS_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True, name)
        for name in (
            "PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED",
            "PRIOR_RELATION_LAPSE_RECORDED_REQUIRED",
            "PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED",
            "PRIOR_RELATION_REVERSED_REQUIRED",
            "PRIOR_RELATION_TERMINATED_REQUIRED",
            "PRIOR_RELATION_ERASED_REQUIRED",
            "PRIOR_RELATION_MUTATED_REQUIRED",
            "PRIOR_RELATION_INVALIDATED_REQUIRED",
            "PRIOR_RELATION_PUNISHED_REQUIRED",
            "PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED",
            "PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED",
            "PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED",
            "PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False, name)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min"
        ))
        required_codes = {
            "REQUEST_NOT_MAPPING", "REQUEST_PATH_UNREADABLE", "REQUEST_JSON_INVALID",
            "UNSUPPORTED_INTENT", "REQUEST_VALUE_MISMATCH", "RESULT_POSTURE_PRECLAIMED",
            "RELATION_LAPSE_OPERATION_SPEC_REFERENCE_MISSING", "RELATION_LAPSE_OPERATION_SPEC_MARKER_MISSING",
            "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING", "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT", "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_RELATION_DISSOLUTION_REQUESTED", "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
            "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED", "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
            "PROHIBITED_LIVING_RELATION_STATE_REQUESTED", "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
            "PROHIBITED_PRESENCE_BOUNDARY_OR_PRESENCE_REQUESTED", "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
            "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED", "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
            "PROHIBITED_STANDING_DESCENDANT_REQUESTED", "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED", "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
            "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        }
        self.assertTrue(required_codes.issubset(set(resolver.BLOCK_CODES)))
        required_flags = {
            "request_relation_dissolution_authorization", "request_relation_reversal",
            "request_relation_termination", "request_relation_erasure", "request_relation_mutation",
            "request_relation_invalidation", "request_relation_punishment", "request_relation_teardown_creation",
            "request_living_relation_state_creation", "request_historical_receipt_preservation",
            "request_presence_boundary_authorization", "request_follow_on_authorization",
            "request_follow_on_work_authorization",
        }
        self.assertTrue(required_flags.issubset(resolver.PROHIBITED_REQUEST_FLAGS))
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )

    def test_synthetic_recorded_result_and_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_lapse_operation_v0_min(request)
            self._assert_recorded_result(result)
            material = result.get("relation_lapse_operation_material")
            self.assertIsInstance(material, Mapping)
            self.assertEqual(set(material), {
                "boundary_allowance_reference",
                "relation_record_lapse_evaluation",
                "lapse_result_evaluation",
            })

            boundary = material["boundary_allowance_reference"]
            self.assertEqual(boundary["prior_relation_lapse_boundary_type"], resolver.PRIOR_RELATION_LAPSE_BOUNDARY_TYPE)
            self.assertEqual(boundary["prior_relation_lapse_boundary_outcome"], resolver.PRIOR_RELATION_LAPSE_BOUNDARY_OUTCOME_REQUIRED)
            self.assertEqual(boundary["prior_relation_lapse_boundary_result"], resolver.PRIOR_RELATION_LAPSE_BOUNDARY_RESULT_REQUIRED)
            boundary_true = {
                "prior_relation_lapse_operation_consideration_allowed",
                "prior_relation_reversibility_operation_referenced",
                "prior_relation_record_referenced",
                "prior_relation_basis_referenced",
            }
            for field in boundary_true:
                self.assertIs(boundary[field], True, field)
            for field, value in boundary.items():
                if field not in boundary_true | {
                    "prior_relation_lapse_boundary_type",
                    "prior_relation_lapse_boundary_outcome",
                    "prior_relation_lapse_boundary_result",
                }:
                    self.assertIs(value, False, field)

            relation_record = material["relation_record_lapse_evaluation"]
            expected_relation_values = {
                "relation_id": resolver.RELATION_ID,
                "relation_pair_scope": resolver.RELATION_PAIR_SCOPE,
                "first_crossing_a_id": resolver.FIRST_CROSSING_A_ID,
                "first_crossing_b_id": resolver.FIRST_CROSSING_B_ID,
                "first_crossing_pair_scope": resolver.FIRST_CROSSING_PAIR_SCOPE,
            }
            for field, expected_value in expected_relation_values.items():
                self.assertEqual(relation_record[field], expected_value, field)
            self.assertIs(relation_record["relation_record_confirmed_as_historical_only"], True)
            for field, value in relation_record.items():
                if field not in set(expected_relation_values) | {"relation_record_confirmed_as_historical_only"}:
                    self.assertIs(value, False, field)

            lapse = material["lapse_result_evaluation"]
            self.assertEqual(lapse["relation_lapse_result"], resolver.RELATION_LAPSE_RESULT)
            self.assertEqual(lapse["relation_lapse_id"], resolver.RELATION_LAPSE_ID)
            self.assertEqual(lapse["relation_lapse_scope"], resolver.RELATION_LAPSE_SCOPE)
            lapse_true = {
                "relation_lapse_supported",
                "relation_lapse_authorized",
                "relation_lapse_performed",
                "relation_lapse_recorded",
            }
            for field in lapse_true:
                self.assertIs(lapse[field], True, field)
            for field, value in lapse.items():
                if field not in lapse_true | {"relation_lapse_result", "relation_lapse_id", "relation_lapse_scope"}:
                    self.assertIs(value, False, field)

    def test_default_live_repo_target_records_when_present(self) -> None:
        references = [
            resolver.DEFAULT_RELATION_LAPSE_OPERATION_SPEC_REFERENCE,
            *(requirement[1] for requirement in resolver.UPSTREAM_REQUIREMENTS),
        ]
        missing = [reference for reference in references if not (resolver.REPO_ROOT / reference).is_file()]
        if missing:
            self.skipTest(f"required default files are absent: {missing}")
        result = resolver.resolve_relation_lapse_operation_v0_min(
            resolver.build_relation_lapse_operation_v0_min_request()
        )
        self._assert_recorded_result(result)

    def test_missing_or_insufficient_boundary_and_upstream_support(self) -> None:
        boundary_requirement = resolver.UPSTREAM_REQUIREMENTS[0]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, references = self._valid_synthetic_request(root)

            missing_boundary = copy.deepcopy(request)
            missing_boundary[boundary_requirement[0]] = str(root / "missing" / "boundary.md")
            result = resolver.resolve_relation_lapse_operation_v0_min(missing_boundary)
            self.assert_requires_boundary_allowance_not_blocked(result)
            self.assertTrue(self._summary(result)["missing_or_insufficient_boundary_allowance"])

            for marker in boundary_requirement[4][0]:
                with self.subTest(boundary_marker=marker):
                    path = references[boundary_requirement[0]]
                    self._write_markdown(
                        path,
                        self._remove_marker(self._relation_lapse_boundary_terminal_summary_text(), marker),
                    )
                    result = resolver.resolve_relation_lapse_operation_v0_min(request)
                    self.assert_requires_boundary_allowance_not_blocked(result)
                    self.assertTrue(self._summary(result)["missing_or_insufficient_boundary_allowance"])
            self._write_markdown(
                references[boundary_requirement[0]],
                self._relation_lapse_boundary_terminal_summary_text(),
            )

            for field, _, missing_code, marker_code, variants, _, _ in resolver.UPSTREAM_REQUIREMENTS[1:]:
                with self.subTest(upstream_missing=field):
                    altered = copy.deepcopy(request)
                    altered[field] = str(root / "missing" / self.safe_json_filename(field))
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_lapse_operation_v0_min(altered),
                        missing_code,
                    )
                for marker in variants[0]:
                    with self.subTest(upstream_marker=field, marker=marker):
                        path = references[field]
                        self._write_markdown(path, self._remove_marker(self._upstream_text(field), marker))
                        self.assert_blocked_with_public_code(
                            resolver.resolve_relation_lapse_operation_v0_min(request),
                            marker_code,
                        )
                self._write_markdown(references[field], self._upstream_text(field))

    def test_do_not_record_intent_does_not_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            request["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_relation_lapse_operation_v0_min(request)
            self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_RECORDED)
            self.assertEqual(self._failed_check_count(result), 0)
            block = result.get("block")
            self.assertIsInstance(block, Mapping)
            self.assertIs(block.get("blocked"), False)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(self._operation(result)[field], False, field)
            self.assert_bounded_false_posture(result)
            self.assert_canonical_non_claims(result)
            self.assert_operation_separate_from_wrappers(result)

    def test_explicit_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            request["intent"] = resolver.INTENT_BLOCK
            self.assert_blocked_with_public_code(
                resolver.resolve_relation_lapse_operation_v0_min(request),
                "EXPLICIT_BLOCK_REQUESTED",
            )

    def test_request_shape_and_exact_field_mismatches_block(self) -> None:
        self.assert_blocked_with_public_code(
            resolver.resolve_relation_lapse_operation_v0_min(["not", "a", "mapping"]),
            "REQUEST_NOT_MAPPING",
        )
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_RELATION_LAPSE_OPERATION"
            self.assert_blocked_with_public_code(
                resolver.resolve_relation_lapse_operation_v0_min(unsupported),
                "UNSUPPORTED_INTENT",
            )
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(exact_field=field):
                    altered = copy.deepcopy(request)
                    altered[field] = not expected if isinstance(expected, bool) else f"wrong_{expected}"
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_lapse_operation_v0_min(altered),
                        "REQUEST_VALUE_MISMATCH",
                    )

    def test_target_and_upstream_marker_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, references = self._valid_synthetic_request(Path(directory))
            target_path = references["relation_lapse_operation_spec_reference"]
            for name, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
                with self.subTest(target_marker_class=name):
                    altered = self._remove_marker_class(self._relation_lapse_operation_spec_text(), variants)
                    self._write_markdown(target_path, altered)
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_lapse_operation_v0_min(request),
                        "RELATION_LAPSE_OPERATION_SPEC_MARKER_MISSING",
                    )
            self._write_markdown(target_path, self._relation_lapse_operation_spec_text())

            for field, _, _, marker_code, variants, _, boundary_basis in resolver.UPSTREAM_REQUIREMENTS:
                with self.subTest(upstream_marker_class=field):
                    path = references[field]
                    self._write_markdown(path, self._remove_marker_class(self._upstream_text(field), variants))
                    result = resolver.resolve_relation_lapse_operation_v0_min(request)
                    if boundary_basis:
                        self.assert_requires_boundary_allowance_not_blocked(result)
                    else:
                        self.assert_blocked_with_public_code(result, marker_code)
                    self._write_markdown(path, self._upstream_text(field))

    def test_every_prohibited_request_flag_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            for flag, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(prohibited_request_flag=flag):
                    altered = copy.deepcopy(request)
                    altered[flag] = True
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_lapse_operation_v0_min(altered),
                        code,
                    )

    def test_every_top_level_preclaim_true_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_preclaim=field):
                    altered = copy.deepcopy(request)
                    altered[field] = True
                    self.assert_blocked_with_public_code(
                        resolver.resolve_relation_lapse_operation_v0_min(altered),
                        "RESULT_POSTURE_PRECLAIMED",
                    )

    def test_declared_nonclaims_canonicalize_false(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_nonclaim=field):
                    altered = copy.deepcopy(request)
                    altered["declared_non_claims"][field] = True
                    result = resolver.resolve_relation_lapse_operation_v0_min(altered)
                    self.assert_blocked_with_public_code(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][field], False)

            malformed_cases: dict[str, Any] = {
                "missing": None,
                "non_mapping": [],
                "missing_key": {field: False for field in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]},
                "non_bool": {field: False for field in resolver.REQUIRED_FALSE_NON_CLAIMS},
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
                        resolver.resolve_relation_lapse_operation_v0_min(altered),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _ = self._valid_synthetic_request(root)
            request_path = self._write_json(root / "requests" / "valid.json", request)
            result = resolver.resolve_relation_lapse_operation_v0_min_from_path(request_path)
            self._assert_recorded_result(result)

            missing = resolver.resolve_relation_lapse_operation_v0_min_from_path(root / "requests" / "missing.json")
            self.assert_blocked_with_public_code(missing, "REQUEST_PATH_UNREADABLE")
            malformed_path = self._write_markdown(root / "requests" / "malformed.json", "{not valid json")
            malformed = resolver.resolve_relation_lapse_operation_v0_min_from_path(malformed_path)
            self.assert_blocked_with_public_code(malformed, "REQUEST_JSON_INVALID")
            array_path = self._write_json(root / "requests" / "array.json", [])
            array_result = resolver.resolve_relation_lapse_operation_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array_result, "REQUEST_NOT_MAPPING")

            output_path = root / "written" / resolver.DETERMINISTIC_FILENAME
            written = resolver.write_relation_lapse_operation_v0_min_result(result, output_path)
            self.assertTrue(written.is_file())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            repeated = resolver.write_relation_lapse_operation_v0_min_result(result, output_path)
            self.assertNotEqual(written, repeated)
            self.assertTrue(repeated.name.endswith("_001.json"))
            self.assertIn("relation_lapse_operation_v0_min_result", written.name)
            self.assertTrue(str(written).startswith(str(root)))

            default_path = resolver.REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            self.assertIn("integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min", str(default_path))
            prohibited_roots = (
                "integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_reversibility_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min",
                "integrity_host_v0_min_coexistence_relation_operation_v0_min",
                "integrity_host_v0_min_coexistence_relation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2",
                "integrity_host_v0_min_coexistence_first_crossing_operation_v0_min",
                "integrity_host_v0_min_coexistence_first_crossing_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_creation_operation_v0_min",
                "integrity_host_v0_min_coexistence_candidate_standing_operation_v0_min",
            )
            for prohibited_root in prohibited_roots:
                self.assertNotIn(prohibited_root, str(resolver.OUTPUT_ROOT))
            for prohibited_part in ("runtime", "daemon", "api", "field", "presence", "identity", "externalization"):
                self.assertNotIn(prohibited_part, {part.casefold() for part in resolver.OUTPUT_ROOT.parts})

            directory_path = root / "written" / "directory"
            directory_path.mkdir()
            with self.assertRaises(resolver.RelationLapseOperationV0MinError):
                resolver.write_relation_lapse_operation_v0_min_result(result, directory_path)
            with self.assertRaises(resolver.RelationLapseOperationV0MinError):
                resolver.write_relation_lapse_operation_v0_min_result([], root / "invalid.json")

    def test_non_mutation_of_request_references_and_contaminated_lineage(self) -> None:
        contaminated_path = REPOSITORY_ROOT / "spec" / "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
        contaminated_before = contaminated_path.read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            request, references = self._valid_synthetic_request(Path(directory))
            request["hostile_payload"] = {
                "raw_relation_body": "RAW_RELATION_BODY_MUST_NOT_RETURN",
                "nested": {"sentinel": ["unchanged", {"attempt": True}]},
            }
            before = copy.deepcopy(request)
            file_before = {field: path.read_text(encoding="utf-8") for field, path in references.items()}
            result = resolver.resolve_relation_lapse_operation_v0_min(request)
            self._assert_recorded_result(result)
            self.assertEqual(request, before)
            for field, path in references.items():
                self.assertEqual(path.read_text(encoding="utf-8"), file_before[field], field)
            self.assertNotIn("RAW_RELATION_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))
        self.assertEqual(contaminated_path.read_text(encoding="utf-8"), contaminated_before)

    def test_summary_behavior_for_recorded_and_missing_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, references = self._valid_synthetic_request(root)
            result = resolver.resolve_relation_lapse_operation_v0_min(request)
            summary = resolver.build_relation_lapse_operation_v0_min_summary(result)
            self._assert_recorded_result(result)
            self.assertEqual(summary, result["relation_lapse_operation_summary"])
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["selected_relation_lapse_operation_spec_path"], str(
                references["relation_lapse_operation_spec_reference"]
            ))
            self.assertEqual(summary["completed_relation_lapse_boundary_terminal_summary_path"], str(
                references["relation_lapse_boundary_terminal_summary_reference"]
            ))
            self.assertEqual(summary["relation_lapse_result"], resolver.RELATION_LAPSE_RESULT)
            self.assertEqual(summary["missing_or_insufficient_boundary_allowance"], [])
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                if field != "relation_lapse_result":
                    self.assertEqual(summary[field], expected, field)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(summary[field], True, field)
            for field in self._PRESERVED_FALSE_FIELDS:
                self.assertIs(summary[field], False, field)

            missing_request = copy.deepcopy(request)
            missing_request["relation_lapse_boundary_terminal_summary_reference"] = str(root / "missing.md")
            missing_result = resolver.resolve_relation_lapse_operation_v0_min(missing_request)
            self.assert_requires_boundary_allowance_not_blocked(missing_result)
            missing_summary = resolver.build_relation_lapse_operation_v0_min_summary(missing_result)
            self.assertTrue(missing_summary["missing_or_insufficient_boundary_allowance"])
            self.assertIs(missing_summary["relation_lapse_supported"], False)

    def test_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self._valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_lapse_operation_v0_min(request)
            summary = resolver.build_relation_lapse_operation_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], "resolve_relation_lapse_operation_v0_min")
            operation = self._operation(result)
            self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(operation["relation_lapse_result"], resolver.RELATION_LAPSE_RESULT)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[field], True, field)
            self.assertEqual(set(result["relation_lapse_operation_material"]), {
                "boundary_allowance_reference",
                "relation_record_lapse_evaluation",
                "lapse_result_evaluation",
            })
            self.assert_bounded_false_posture(result)
            self.assert_operation_separate_from_wrappers(result)
            self.assert_canonical_non_claims(result)


if __name__ == "__main__":
    unittest.main()
