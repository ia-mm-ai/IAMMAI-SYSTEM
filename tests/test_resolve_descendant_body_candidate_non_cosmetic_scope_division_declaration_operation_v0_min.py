"""Tests for one bounded non-cosmetic candidate scope-division declaration operation.

The default posture preserves missing scope declarations as clean additional
basis, while an explicit mandate/function/responsibility/governed-surface
division may record one non-standing operation without creating content,
distinctness, standing, descendant bodies, relation, runtime, or follow-on
authority.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min as resolver


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationOperationTests(unittest.TestCase):
    """Bounded executable coverage for the scope-declaration operation only."""

    OPERATION_KEY = "descendant_body_candidate_non_cosmetic_scope_division_declaration_operation"
    CHECKS_KEY = "candidate_non_cosmetic_scope_division_declaration_operation_checks"
    SUMMARY_KEY = "candidate_non_cosmetic_scope_division_declaration_operation_summary"

    RAW_SENTINELS = (
        "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
        "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
        "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        """Return a deterministic local JSON filename for subtest artifacts."""

        safe = str(name)
        safe = safe.replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def _write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def _operation_spec_text(self, include_sentinel: bool = False) -> str:
        lines = [
            "# Descendant Body Candidate Non-Cosmetic Scope Division Declaration Operation V0 Minimum Specification",
            "This file defines one future candidate non-cosmetic scope-division declaration operation.",
            "This file is operation-spec-only.",
            "This file does not implement or perform the operation.",
            "This file does not declare candidate A scope, candidate B scope, or basis-bearing scope division.",
            "Scope declaration is not scope standing.",
            "Scope declaration is not candidate-specific basis emission.",
            "Scope declaration is not distinctness support.",
            "A scope label is not a scope.",
            "A scope title is not a mandate.",
            "A scope id is not a governed surface.",
            "Scope division must be basis-bearing, not label-bearing.",
            "Candidate-specific basis must be basis-bearing, not label-bearing.",
            "candidate_non_cosmetic_scope_division_declaration_operation_type = DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
            "candidate_non_cosmetic_scope_division_declaration_operation_scope = TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_DECLARATION_ONLY",
            "admissible_future_route = NON_COSMETIC_SCOPE_DIVISION_DECLARATION_ONLY",
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded = false",
            "candidate_a_scope_declared = false",
            "candidate_b_scope_declared = false",
            "basis_bearing_scope_division_declared = false",
            "scope_label_laundering_treated_as_basis = false",
            "cosmetic_scope_naming_treated_as_basis = false",
            "id_role_label_difference_treated_as_scope_basis = false",
            "shared_evidence_treated_as_scope_basis = false",
            "operation_evidence_alone_treated_as_scope_basis = false",
            "contaminated_lineage_treated_as_clean_scope_basis = false",
        ]
        if include_sentinel:
            lines.extend(self.RAW_SENTINELS)
        return "\n".join(lines) + "\n"

    def _boundary_summary_text(self, include_sentinel: bool = False) -> str:
        lines = [
            "# Scope Division Boundary Summary",
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
            "RECORDED as the live v3 boundary outcome",
            "failed_check_count = 0",
            "result_version = 0.3.0",
            "resolver_module = resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
            "future_scope_declaration_operation_type = DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
            "rupture_class_blocked = SCOPE_LABEL_LAUNDERING",
            "candidate_a_scope_missing_upstream = true",
            "candidate_b_scope_missing_upstream = true",
            "basis_bearing_scope_division_missing_upstream = true",
            "future_scope_declaration_operation_shape_allowed = true",
            "candidate_a_scope_not_declared = true",
            "candidate_b_scope_not_declared = true",
            "basis_bearing_scope_division_not_declared = true",
            "scope_label_laundering_not_allowed = true",
            "Scope declaration is not scope standing",
            "A scope label is not a scope",
            "Scope division must be basis-bearing, not label-bearing",
        ]
        if include_sentinel:
            lines.extend(self.RAW_SENTINELS)
        return "\n".join(lines) + "\n"

    def _basis_emission_summary_text(self, include_sentinel: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "REQUIRES_ADDITIONAL_BASIS",
            "missing non-cosmetic candidate A scope",
            "missing non-cosmetic candidate B scope",
            "missing basis-bearing scope division",
            "material_emitted = false",
            "candidate_specific_content_emitted = false",
            "distinctness_operation_rerun = false",
            "distinctness_supported_recorded = false",
            "candidate_records_marked_distinct = false",
            "candidate_standing_authorized = false",
            "descendant_body_created = false",
        ]
        if include_sentinel:
            lines.extend(self.RAW_SENTINELS)
        return "\n".join(lines) + "\n"

    def _distinctness_summary_text(self, include_sentinel: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
            "distinctness_result = NOT_DISTINCT",
            "failed_check_count = 0",
            "candidate_record_count_compared = 2",
            "distinctness_supported = false",
            "NOT_DISTINCT is a clean operation result, not a failure",
            "id and role difference alone is not distinctness",
            "shared evidence reference alone is not distinctness",
            "Operation evidence alone is not distinctness",
        ]
        if include_sentinel:
            lines.extend(self.RAW_SENTINELS)
        return "\n".join(lines) + "\n"

    def _differentiation_summary_text(self, include_sentinel: bool = False) -> str:
        """Return all five completed differentiation posture classes."""

        lines = [
            "outcome = DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
            "exactly two result-contained non-standing candidate records",
            "candidate records are non-standing",
            "candidate records are not descendant bodies",
            "standing_authorized = false",
            "crossing_authorized = false",
            "relation_created = false",
        ]
        if include_sentinel:
            lines.extend(self.RAW_SENTINELS)
        return "\n".join(lines) + "\n"

    def _synthetic_basis_files(self, directory: Path, include_sentinel: bool = False) -> dict[str, Path]:
        """Write only declared, clean local basis files for one temporary test case."""

        basis = {
            "operation_spec_reference": self._write_text(
                directory / "operation-spec.md", self._operation_spec_text(include_sentinel)
            ),
            "completed_scope_division_declaration_boundary_terminal_summary_reference": self._write_text(
                directory / "boundary-summary.md", self._boundary_summary_text(include_sentinel)
            ),
            "completed_basis_emission_operation_terminal_summary_reference": self._write_text(
                directory / "basis-emission-operation-summary.md",
                self._basis_emission_summary_text(include_sentinel),
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": self._write_text(
                directory / "basis-emission-boundary-summary.md", "basis emission boundary declared only\n"
            ),
            "completed_distinctness_operation_terminal_summary_reference": self._write_text(
                directory / "distinctness-operation-summary.md",
                self._distinctness_summary_text(include_sentinel),
            ),
            "completed_differentiation_operation_terminal_summary_reference": self._write_text(
                directory / "differentiation-operation-summary.md",
                self._differentiation_summary_text(include_sentinel),
            ),
            "completed_scope_division_declaration_boundary_artifact_reference": self._write_json(
                directory / "boundary-artifact.json", {"declared_only": True}
            ),
        }
        return basis

    def _missing_scope_request(self, basis: dict[str, Path]) -> dict[str, object]:
        return resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request(
            **{key: str(value) for key, value in basis.items()}
        )

    def _recorded_scope_request(self, basis: dict[str, Path]) -> dict[str, object]:
        request = self._missing_scope_request(basis)
        request.update(
            {
                "candidate_a_scope_id": "candidate_a_scope_mandate_integrity_gate",
                "candidate_b_scope_id": "candidate_b_scope_governed_surface_receipt_trace",
                "candidate_a_scope_statement": (
                    "Candidate A scope governs mandate integrity for proposed scope declarations."
                ),
                "candidate_b_scope_statement": (
                    "Candidate B scope governs receipt trace for proposed scope declarations."
                ),
                "candidate_a_scope_basis": "Mandate: integrity gate responsibility.",
                "candidate_b_scope_basis": "Governed surface: receipt trace responsibility.",
                "basis_bearing_scope_division_statement": (
                    "Candidate A and B differ by mandate and governed surface."
                ),
                "basis_bearing_scope_division_basis": (
                    "The basis-bearing division names mandate and governed surface."
                ),
            }
        )
        return request

    def _cosmetic_scope_request(self, basis: dict[str, Path], **overrides: object) -> dict[str, object]:
        request = self._recorded_scope_request(basis)
        request.update(overrides)
        return request

    def _operation(self, result: dict[str, object]) -> dict[str, object]:
        operation = result.get(self.OPERATION_KEY)
        self.assertIsInstance(operation, dict)
        return operation

    def _checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        checks = result.get(self.CHECKS_KEY)
        self.assertIsInstance(checks, list)
        self.assertTrue(all(isinstance(check, dict) for check in checks))
        return checks

    def passed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is True for check in self._checks(result))

    def failed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is False for check in self._checks(result))

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_requires_additional_basis(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_clean_recorded(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        for check in self._checks(result):
            for field in ("block_code", "failure_code"):
                value = check.get(field)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_blocked_with_public_code(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_refusal_posture(result)

    def assert_wrapper_separation(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for field in (
            "outcome",
            "block",
            self.CHECKS_KEY,
            "non_claims",
            self.SUMMARY_KEY,
            "candidate_non_cosmetic_scope_division_declaration_operation_metadata",
        ):
            self.assertNotIn(field, operation)

    def assert_refusal_posture(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for field in (
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "basis_emission_operation_rerun",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_authorized",
            "field_machinery_authorized",
            "runtime_authorized",
            "currentness_authorized",
            "authority_authorized",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
        ):
            self.assertIs(operation.get(field), False, field)
        self.assertIs(operation.get("candidate_records_remain_non_standing"), True)
        self.assertIs(operation.get("candidate_records_remain_not_descendant_bodies"), True)

    def assert_no_raw_markdown_body(self, result: dict[str, object]) -> None:
        serialized = json.dumps(result, ensure_ascii=True, sort_keys=True)
        for sentinel in self.RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_operation_false_non_claims(self, result: dict[str, object]) -> None:
        self.assert_refusal_posture(result)
        self.assert_canonical_false_non_claims(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min",
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path",
            "write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result",
            "build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_FAMILY",
            "OPERATION_TYPE",
            "OPERATION_VERSION",
            "OPERATION_SCOPE",
            "ADMISSIBLE_FUTURE_ROUTE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min",
        )
        self.assertEqual(
            resolver.OPERATION_TYPE,
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
        )
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_DECLARATION_ONLY",
        )
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE, "NON_COSMETIC_SCOPE_DIVISION_DECLARATION_ONLY"
        )
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min"
            )
        )
        self.assertNotIn("candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3", str(resolver.OUTPUT_ROOT))
        required_false = {
            "candidate_non_cosmetic_scope_division_declaration_operation_implemented",
            "candidate_non_cosmetic_scope_division_declaration_operation_performed",
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "candidate_specific_distinctness_basis_emission_operation_rerun",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_created",
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
            "affected_file_repaired",
            "affected_file_edited",
            "affected_file_deleted",
            "affected_file_overwritten",
            "affected_file_replaced",
            "affected_file_redeemed",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "candidate_non_cosmetic_scope_division_declaration_boundary_overridden",
            "candidate_non_cosmetic_scope_division_declaration_boundary_bypassed",
            "scope_label_laundering_treated_as_basis",
            "cosmetic_scope_naming_treated_as_basis",
            "id_role_label_difference_treated_as_scope_basis",
            "shared_evidence_treated_as_scope_basis",
            "operation_evidence_alone_treated_as_scope_basis",
            "contaminated_lineage_treated_as_clean_scope_basis",
        }
        self.assertTrue(required_false.issubset(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue({
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_a_scope_non_cosmetic",
            "candidate_b_scope_non_cosmetic",
            "scope_division_basis_bearing",
            "candidate_a_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
            "candidate_b_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
            "candidate_records_remain_non_standing",
            "candidate_records_remain_not_descendant_bodies",
        }.issubset(resolver.ALLOWED_TRUE_RECORDED_FIELDS))
        self.assertTrue({
            "OPERATION_SPEC_MARKER_MISSING",
            "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "CANDIDATE_A_SCOPE_DECLARATION_MISSING",
            "CANDIDATE_B_SCOPE_DECLARATION_MISSING",
            "BASIS_BEARING_SCOPE_DIVISION_DECLARATION_MISSING",
            "CANDIDATE_SCOPE_DECLARATIONS_IDENTICAL",
            "CANDIDATE_SCOPE_DECLARATIONS_COSMETIC_ONLY",
            "BASIS_BEARING_SCOPE_DIVISION_BASIS_MISSING",
            "BASIS_BEARING_SCOPE_DIVISION_BASIS_NOT_NON_COSMETIC",
            "SCOPE_LABEL_LAUNDERING_DETECTED",
            "COSMETIC_SCOPE_NAMING_DETECTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
        }.issubset(resolver.BLOCK_CODES))

    def test_default_synthetic_missing_scope_request_returns_requires_additional_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            request = self._missing_scope_request(basis)
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
        self.assertIsInstance(result, dict)
        self.assert_requires_additional_basis(result)
        self.assertEqual(result["candidate_non_cosmetic_scope_division_declaration_operation_metadata"]["result_version"], "0.1.0")
        self.assertEqual(result["candidate_non_cosmetic_scope_division_declaration_operation_metadata"]["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertEqual(self._operation(result)["candidate_non_cosmetic_scope_division_declaration_operation_id"], resolver.DEFAULT_OPERATION_ID)
        self.assertEqual(set(result["additional_basis_required"]), {
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        })
        for section in (
            "candidate_non_cosmetic_scope_division_declaration_operation_metadata",
            "declared_candidate_non_cosmetic_scope_division_declaration_operation_basis",
            "upstream_basis",
            self.OPERATION_KEY,
            self.CHECKS_KEY,
            "candidate_non_cosmetic_scope_division_declaration_operation_statement",
            "candidate_non_cosmetic_scope_division_declaration_operation_non_meaning",
            "additional_basis_required",
            "not_recorded_basis",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            self.SUMMARY_KEY,
        ):
            self.assertIn(section, result)
        operation = self._operation(result)
        expected = {
            "candidate_non_cosmetic_scope_division_declaration_operation_type": resolver.OPERATION_TYPE,
            "candidate_non_cosmetic_scope_division_declaration_operation_version": "0.1.0",
            "candidate_non_cosmetic_scope_division_declaration_operation_scope": resolver.OPERATION_SCOPE,
            "admissible_future_route": resolver.ADMISSIBLE_FUTURE_ROUTE,
            "upstream_emission_operation_result": "REQUIRES_ADDITIONAL_BASIS",
            "requires_additional_basis_preserved_as_clean_result": True,
            "candidate_a_scope_missing_upstream": True,
            "candidate_b_scope_missing_upstream": True,
            "basis_bearing_scope_division_missing_upstream": True,
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded": False,
            "candidate_a_scope_declared": False,
            "candidate_b_scope_declared": False,
            "basis_bearing_scope_division_declared": False,
            "candidate_a_scope_non_cosmetic": False,
            "candidate_b_scope_non_cosmetic": False,
            "scope_division_basis_bearing": False,
            "candidate_a_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface": False,
            "candidate_b_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface": False,
            "scope_label_laundering_detected": False,
            "scope_label_laundering_treated_as_basis": False,
            "cosmetic_scope_naming_detected": False,
            "cosmetic_scope_naming_treated_as_basis": False,
            "id_role_label_difference_treated_as_scope_basis": False,
            "shared_evidence_treated_as_scope_basis": False,
            "operation_evidence_alone_treated_as_scope_basis": False,
            "contaminated_lineage_treated_as_clean_scope_basis": False,
        }
        for field, value in expected.items():
            self.assertIs(operation.get(field), value, field) if isinstance(value, bool) else self.assertEqual(operation.get(field), value, field)
        for field in (
            "operation_spec_markers_present",
            "completed_scope_division_declaration_boundary_terminal_summary_markers_present",
            "completed_basis_emission_operation_terminal_summary_markers_present",
            "completed_distinctness_operation_terminal_summary_markers_present",
            "completed_differentiation_operation_terminal_summary_markers_present",
        ):
            self.assertIs(operation.get(field), True, field)
        self.assert_wrapper_separation(result)
        self.assert_operation_false_non_claims(result)

    def test_default_live_target_requires_additional_basis_if_present(self) -> None:
        required = (
            REPO_ROOT / resolver.DEFAULT_OPERATION_SPEC_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        )
        if not all(path.is_file() for path in required):
            self.skipTest("default declared basis files are not all present")
        result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
            resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request()
        )
        self.assert_requires_additional_basis(result)
        operation = self._operation(result)
        for field in (
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_a_scope_non_cosmetic",
            "candidate_b_scope_non_cosmetic",
            "scope_division_basis_bearing",
        ):
            self.assertIs(operation.get(field), False, field)
        self.assert_operation_false_non_claims(result)

    def test_supported_declared_non_cosmetic_scope_request_records_operation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            request = self._recorded_scope_request(basis)
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
        self.assert_clean_recorded(result)
        operation = self._operation(result)
        for field in (
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_a_scope_non_cosmetic",
            "candidate_b_scope_non_cosmetic",
            "scope_division_basis_bearing",
            "candidate_a_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
            "candidate_b_scope_differs_by_mandate_or_function_or_responsibility_or_governed_surface",
        ):
            self.assertIs(operation.get(field), True, field)
        for field in (
            "scope_label_laundering_detected",
            "cosmetic_scope_naming_detected",
            "scope_label_laundering_treated_as_basis",
            "id_role_label_difference_treated_as_scope_basis",
            "shared_evidence_treated_as_scope_basis",
            "operation_evidence_alone_treated_as_scope_basis",
            "contaminated_lineage_treated_as_clean_scope_basis",
        ):
            self.assertIs(operation.get(field), False, field)
        self.assert_wrapper_separation(result)
        self.assert_operation_false_non_claims(result)

    def test_cosmetic_or_label_only_scope_requests_do_not_record(self) -> None:
        cases = {
            "identical_statements": {
                "candidate_b_scope_statement": "Candidate A scope governs mandate integrity for proposed scope declarations.",
            },
            "candidate_labels_only": {
                "candidate_a_scope_statement": "Candidate A scope label only.",
                "candidate_b_scope_statement": "Candidate B scope label only.",
            },
            "role_labels_only": {
                "candidate_a_scope_statement": "CANDIDATE_A role label only.",
                "candidate_b_scope_statement": "CANDIDATE_B role label only.",
            },
            "side_order_only": {
                "candidate_a_scope_statement": "Candidate A side only order only.",
                "candidate_b_scope_statement": "Candidate B side only order only.",
            },
            "template_substitution": {
                "candidate_a_scope_statement": "Candidate A template slot string replacement.",
                "candidate_b_scope_statement": "Candidate B template slot string replacement.",
            },
            "id_role_label_basis_only": {
                "candidate_a_scope_statement": "Candidate A id and role label only.",
                "candidate_b_scope_statement": "Candidate B id and role label only.",
                "candidate_a_scope_basis": "candidate id and candidate role label only",
                "candidate_b_scope_basis": "candidate id and candidate role label only",
                "basis_bearing_scope_division_statement": "candidate id and role label only",
                "basis_bearing_scope_division_basis": "candidate id and role label only",
            },
            "shared_evidence_alone": {
                "basis_bearing_scope_division_basis": "shared evidence alone with mandate wording",
            },
            "operation_evidence_alone": {
                "basis_bearing_scope_division_basis": "operation evidence alone with governed surface wording",
            },
            "contaminated_lineage": {
                "basis_bearing_scope_division_basis": "contaminated lineage with mandate wording",
            },
            "laundering_flag": {"scope_label_laundering_treated_as_basis": True},
            "cosmetic_flag": {"cosmetic_scope_naming_treated_as_basis": True},
            "role_difference_flag": {"id_role_label_difference_treated_as_scope_basis": True},
            "shared_evidence_flag": {"shared_evidence_treated_as_scope_basis": True},
            "operation_evidence_flag": {"operation_evidence_alone_treated_as_scope_basis": True},
            "contaminated_lineage_flag": {"contaminated_lineage_treated_as_clean_scope_basis": True},
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            for name, overrides in cases.items():
                with self.subTest(name=name):
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
                        self._cosmetic_scope_request(basis, **overrides)
                    )
                    self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_with_public_code(result)
                    else:
                        self.assert_requires_additional_basis(result)
                        self.assert_operation_false_non_claims(result)

    def test_do_not_record_intent_does_not_record_operation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            request = self._recorded_scope_request(basis)
            request["candidate_non_cosmetic_scope_division_declaration_operation_intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assert_not_blocked(result)
        operation = self._operation(result)
        for field in (
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
        ):
            self.assertIs(operation.get(field), False, field)
        self.assert_operation_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            request = self._recorded_scope_request(basis)
            request["candidate_non_cosmetic_scope_division_declaration_operation_intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
        self.assert_blocked_with_public_code(result)
        self.assertEqual(
            self.block_code(result),
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCK_REQUESTED",
        )

    def test_request_shape_and_prohibited_request_blocking(self) -> None:
        cases: dict[str, tuple[str, object]] = {
            "unsupported_intent": ("candidate_non_cosmetic_scope_division_declaration_operation_intent", "NOPE"),
            "missing_type": ("candidate_non_cosmetic_scope_division_declaration_operation_type", None),
            "wrong_type": ("candidate_non_cosmetic_scope_division_declaration_operation_type", "OTHER"),
            "missing_version": ("candidate_non_cosmetic_scope_division_declaration_operation_version", None),
            "wrong_version": ("candidate_non_cosmetic_scope_division_declaration_operation_version", "9.9.9"),
            "missing_scope": ("candidate_non_cosmetic_scope_division_declaration_operation_scope", None),
            "wrong_scope": ("candidate_non_cosmetic_scope_division_declaration_operation_scope", "OTHER"),
            "missing_route": ("admissible_future_route", None),
            "wrong_route": ("admissible_future_route", "OTHER"),
            "wrong_candidate_a_id": ("candidate_record_a_id", "other"),
            "wrong_candidate_b_id": ("candidate_record_b_id", "other"),
            "wrong_candidate_a_role": ("candidate_record_a_role", "OTHER"),
            "wrong_candidate_b_role": ("candidate_record_b_role", "OTHER"),
            "wrong_upstream_outcome": ("upstream_emission_operation_result", "RECORDED"),
            "clean_basis_not_preserved": ("requires_additional_basis_preserved_as_clean_result", False),
            "candidate_a_missing_not_true": ("candidate_a_scope_missing_upstream", False),
            "candidate_b_missing_not_true": ("candidate_b_scope_missing_upstream", False),
            "division_missing_not_true": ("basis_bearing_scope_division_missing_upstream", False),
            "wrong_scope_policy": ("scope_declaration_policy", "OTHER"),
            "wrong_laundering_policy": ("scope_label_laundering_policy", "OTHER"),
            "wrong_cosmetic_policy": ("cosmetic_scope_naming_policy", "OTHER"),
            "wrong_role_policy": ("id_role_label_difference_policy", "OTHER"),
            "wrong_shared_policy": ("shared_evidence_policy", "OTHER"),
            "wrong_operation_policy": ("operation_evidence_policy", "OTHER"),
            "wrong_lineage_policy": ("contaminated_lineage_policy", "OTHER"),
        }
        false_allowed_fields = tuple(resolver.FALSE_FIELD_CODES)
        prohibited_request_fields = tuple(resolver.PROHIBITED_REQUEST_CODES)
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            for field in (
                "operation_spec_reference",
                "completed_scope_division_declaration_boundary_terminal_summary_reference",
                "completed_basis_emission_operation_terminal_summary_reference",
                "completed_distinctness_operation_terminal_summary_reference",
                "completed_differentiation_operation_terminal_summary_reference",
            ):
                cases[f"missing_{field}"] = (field, "")
            for field in false_allowed_fields + prohibited_request_fields:
                cases[f"prohibited_{field}"] = (field, True)
            for name, (field, value) in cases.items():
                with self.subTest(name=name):
                    request = self._recorded_scope_request(basis)
                    request[field] = value
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
            malformed = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(["not", "a", "mapping"])
        self.assert_blocked_with_public_code(malformed)

    def test_marker_validation_blocking_behavior(self) -> None:
        cases = (
            ("operation_spec_reference", "Scope declaration is not distinctness support.", "OPERATION_SPEC_MARKER_MISSING"),
            (
                "completed_scope_division_declaration_boundary_terminal_summary_reference",
                "future_scope_declaration_operation_shape_allowed = true",
                "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            (
                "completed_basis_emission_operation_terminal_summary_reference",
                "missing non-cosmetic candidate B scope",
                "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            (
                "completed_distinctness_operation_terminal_summary_reference",
                "NOT_DISTINCT is a clean operation result, not a failure",
                "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            (
                "completed_differentiation_operation_terminal_summary_reference",
                "exactly two result-contained non-standing candidate records",
                "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            for index, (field, marker, expected_code) in enumerate(cases):
                with self.subTest(field=field):
                    case_directory = Path(temporary_directory) / self.safe_json_filename(field, index).replace(".json", "")
                    case_basis = self._synthetic_basis_files(case_directory)
                    path = case_basis[field]
                    self._write_text(path, path.read_text(encoding="utf-8").replace(marker, "MISSING_REQUIRED_MARKER", 1))
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
                        self._recorded_scope_request(case_basis)
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        fields = (
            "candidate_non_cosmetic_scope_division_declaration_operation_implemented",
            "candidate_non_cosmetic_scope_division_declaration_operation_performed",
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "candidate_specific_distinctness_basis_emission_operation_rerun",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_created",
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
            "affected_file_repaired",
            "affected_file_edited",
            "affected_file_deleted",
            "affected_file_overwritten",
            "affected_file_replaced",
            "affected_file_redeemed",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "candidate_non_cosmetic_scope_division_declaration_boundary_overridden",
            "candidate_non_cosmetic_scope_division_declaration_boundary_bypassed",
            "scan_performed",
            "repository_scan_performed",
            "repair_performed",
            "validation_enforced",
            "hidden_repair_performed",
            "silent_overwrite_performed",
            "scope_label_laundering_treated_as_basis",
            "cosmetic_scope_naming_treated_as_basis",
            "id_role_label_difference_treated_as_scope_basis",
            "shared_evidence_treated_as_scope_basis",
            "operation_evidence_alone_treated_as_scope_basis",
            "contaminated_lineage_treated_as_clean_scope_basis",
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            for field in fields:
                with self.subTest(field=field):
                    request = self._recorded_scope_request(basis)
                    request[field] = True
                    # The declared non-claim map is the authoritative input posture;
                    # retain the top-level signal while making its prohibition explicit.
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][field], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            clean = self._recorded_scope_request(basis)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(field=field):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][field], False)
            malformed_cases = (
                None,
                [],
                {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS if key != resolver.REQUIRED_FALSE_NON_CLAIMS[0]},
                {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            )
            for declared_non_claims in malformed_cases:
                with self.subTest(malformed=type(declared_non_claims).__name__):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"] = declared_non_claims
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)

    def test_sanitizer_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory), include_sentinel=True)
            request = self._recorded_scope_request(basis)
            request["raw_markdown_body"] = self.RAW_SENTINELS[0]
            request["hidden_repo_state"] = self.RAW_SENTINELS[1]
            request["current_working_tree"] = self.RAW_SENTINELS[2]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
        self.assert_clean_recorded(result)
        self.assert_no_raw_markdown_body(result)
        self.assertIn(resolver.OPERATION_TYPE, json.dumps(result, ensure_ascii=True))
        self.assertEqual(request, request_before)
        self.assert_operation_false_non_claims(result)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            basis = self._synthetic_basis_files(directory / "basis")
            request_path = self._write_json(directory / "request.json", self._missing_scope_request(basis))
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path(request_path)
            self.assert_requires_additional_basis(result)
            malformed = directory / "malformed.json"
            self._write_text(malformed, "{not valid json")
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path(malformed)
            )
            array_path = self._write_json(directory / "array.json", [])
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path(array_path)
            )
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_from_path(directory / "missing.json")
            )
            output_path = directory / "operation-output"
            first = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result(result, output_path)
            second = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result(result, output_path)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
            self.assertIn("candidate_non_cosmetic_scope_division_declaration_operation_v0_min_result", first.name)
            self.assertIn("descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min", str(resolver.OUTPUT_ROOT))
            forbidden_roots = (
                "candidate_non_cosmetic_scope_division_declaration_boundary",
                "candidate_specific_distinctness_basis_emission",
                "candidate_record_distinctness",
                "descendant_body_differentiation",
                "existence_claim",
                "runtime_hosting",
                "runtime_loop",
                "daemon",
            )
            self.assertFalse(any(root in str(first.parent) for root in forbidden_roots))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            basis = self._synthetic_basis_files(directory, include_sentinel=True)
            request = self._recorded_scope_request(basis)
            request["raw_markdown_body"] = self.RAW_SENTINELS[0]
            request_before = copy.deepcopy(request)
            basis_before = {key: path.read_text(encoding="utf-8") for key, path in basis.items() if path.suffix == ".md"}
            resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(request)
            self.assertEqual(request, request_before)
            for key, text in basis_before.items():
                self.assertEqual(basis[key].read_text(encoding="utf-8"), text, key)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            default_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
                self._missing_scope_request(basis)
            )
            recorded_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(
                self._recorded_scope_request(basis)
            )
        default_summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(default_result)
        recorded_summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(recorded_result)
        self.assertEqual(default_summary["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(default_summary["failed_check_count"], 0)
        self.assertEqual(default_summary["result_version"], "0.1.0")
        self.assertEqual(default_summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(default_summary["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(default_summary["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(default_summary["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(default_summary["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(set(default_summary["additional_basis_required"]), {
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        })
        for field in (
            "candidate_non_cosmetic_scope_division_declaration_operation_recorded",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_a_scope_non_cosmetic",
            "candidate_b_scope_non_cosmetic",
            "scope_division_basis_bearing",
        ):
            self.assertIs(default_summary[field], False, field)
            self.assertIs(recorded_summary[field], True, field)
        self.assertIs(default_summary["result_level_non_claims_canonical_false"], True)
        self.assertIs(recorded_summary["result_level_non_claims_canonical_false"], True)
        self.assert_operation_false_non_claims(recorded_result)

    def test_smoke_behavior_default_and_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            basis = self._synthetic_basis_files(Path(temporary_directory))
            default_request = self._missing_scope_request(basis)
            default_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(default_request)
            default_summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(default_result)
            self.assert_requires_additional_basis(default_result)
            self.assertEqual(default_summary["failed_check_count"], 0)
            self.assertEqual(default_summary["result_version"], "0.1.0")
            self.assertEqual(default_summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_wrapper_separation(default_result)
            recorded_request = self._recorded_scope_request(basis)
            recorded_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min(recorded_request)
            self.assert_clean_recorded(recorded_result)
            operation = self._operation(recorded_result)
            self.assertEqual(operation["candidate_non_cosmetic_scope_division_declaration_operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(operation["candidate_non_cosmetic_scope_division_declaration_operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(operation["candidate_non_cosmetic_scope_division_declaration_operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(operation["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
            self.assert_operation_false_non_claims(recorded_result)


if __name__ == "__main__":
    unittest.main()
