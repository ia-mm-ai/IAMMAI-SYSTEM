"""Executable v2 coverage for bounded non-cosmetic scope declaration.

V1 is preserved lineage.  V2 proves only the two successor repairs: clean
boundary posture-class acceptance and equivalent differentiation no-standing
posture acceptance.  It otherwise preserves the operation's refusal surface.
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

import resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2 as resolver


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationOperationV2Tests(unittest.TestCase):
    """One v2 scope-declaration operation, without standing or downstream work."""

    OPERATION_KEY = "descendant_body_candidate_non_cosmetic_scope_division_declaration_operation"
    CHECKS_KEY = "candidate_non_cosmetic_scope_division_declaration_operation_checks"
    SUMMARY_KEY = "candidate_non_cosmetic_scope_division_declaration_operation_summary"
    SENTINELS = (
        "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
        "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
        "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
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

    def _operation_spec_text(self, hostile: bool = False) -> str:
        lines = [
            "Descendant Body Candidate Non-Cosmetic Scope Division Declaration Operation V0 Minimum Specification",
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
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _boundary_summary_text(self, variant: str = "full", missing_class: str | None = None) -> str:
        classes = {
            "boundary_recorded": [
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
                "RECORDED as the live v3 boundary outcome",
            ],
            "clean_v3_result": [
                "failed_check_count = 0",
                "result_version = 0.3.0",
                "resolver_module = resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
                "Ran 16 tests",
                "OK",
            ],
            "future_operation_shape_allowed": [
                "future_scope_declaration_operation_type = DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
                "future_scope_declaration_operation_shape_allowed = true",
                "allows only future scope declaration operation shape",
            ],
            "missing_upstream_scope_declarations_preserved": [
                "candidate_a_scope_missing_upstream = true",
                "candidate_b_scope_missing_upstream = true",
                "basis_bearing_scope_division_missing_upstream = true",
            ],
            "scope_declarations_not_created": [
                "candidate_a_scope_not_declared = true",
                "candidate_b_scope_not_declared = true",
                "basis_bearing_scope_division_not_declared = true",
            ],
            "scope_label_laundering_blocked": [
                "rupture_class_blocked = SCOPE_LABEL_LAUNDERING",
                "scope_label_laundering_not_allowed = true",
                "scope-label laundering remains blocked",
            ],
            "scope_thesis": [
                "Scope declaration is not scope standing",
                "A scope label is not a scope",
                "Scope division must be basis-bearing, not label-bearing",
            ],
        }
        if variant == "equivalent":
            classes["boundary_recorded"] = ["RECORDED as the live v3 boundary outcome"]
            classes["clean_v3_result"] = ["v3 live artifact recorded cleanly", "Ran 16 tests", "OK"]
            classes["future_operation_shape_allowed"] = ["allowed only a future scope declaration operation shape"]
            classes["missing_upstream_scope_declarations_preserved"] = [
                "non-cosmetic candidate A scope is still missing upstream",
                "non-cosmetic candidate B scope is still missing upstream",
                "basis-bearing scope division is still missing upstream",
            ]
            classes["scope_declarations_not_created"] = [
                "does not declare candidate A scope",
                "does not declare candidate B scope",
                "does not declare basis-bearing scope division",
            ]
            classes["scope_label_laundering_blocked"] = ["scope-label laundering remains blocked"]
        lines: list[str] = []
        for name, content in classes.items():
            if name != missing_class:
                lines.extend(content)
        return "\n".join(lines) + "\n"

    def _basis_emission_summary_text(self) -> str:
        return "\n".join(
            (
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
            )
        ) + "\n"

    def _distinctness_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                "distinctness_result = NOT_DISTINCT",
                "failed_check_count = 0",
                "candidate_record_count_compared = 2",
                "distinctness_supported = false",
                "NOT_DISTINCT is a clean operation result, not a failure",
                "id and role difference alone is not distinctness",
                "shared evidence reference alone is not distinctness",
                "Operation evidence alone is not distinctness",
            )
        ) + "\n"

    def _differentiation_summary_text(
        self, standing_phrase: str = "standing descendants were not created", missing_class: str | None = None
    ) -> str:
        classes = {
            "completion": ["outcome = DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED"],
            "exactly_two_candidates": ["exactly two result-contained non-standing candidate records"],
            "non_standing_not_descendant_bodies": [
                "candidate records are non-standing",
                "candidate records are not descendant bodies",
            ],
            "standing_descendant_creation_not_authorized": [standing_phrase],
            "crossing_relation_not_authorized": ["crossing_authorized = false", "relation_created = false"],
        }
        lines: list[str] = []
        for name, content in classes.items():
            if name != missing_class:
                lines.extend(content)
        return "\n".join(lines) + "\n"

    def _basis_files(
        self,
        directory: Path,
        *,
        boundary_text: str | None = None,
        differentiation_text: str | None = None,
        hostile: bool = False,
    ) -> dict[str, Path]:
        files = {
            "operation_spec_reference": self._write_text(
                directory / "operation-spec.md", self._operation_spec_text(hostile)
            ),
            "completed_scope_division_declaration_boundary_terminal_summary_reference": self._write_text(
                directory / "boundary-summary.md", boundary_text or self._boundary_summary_text()
            ),
            "completed_basis_emission_operation_terminal_summary_reference": self._write_text(
                directory / "basis-emission-operation-summary.md", self._basis_emission_summary_text()
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": self._write_text(
                directory / "basis-emission-boundary-summary.md", "declared basis-emission boundary only\n"
            ),
            "completed_distinctness_operation_terminal_summary_reference": self._write_text(
                directory / "distinctness-summary.md", self._distinctness_summary_text()
            ),
            "completed_differentiation_operation_terminal_summary_reference": self._write_text(
                directory / "differentiation-summary.md", differentiation_text or self._differentiation_summary_text()
            ),
            "completed_scope_division_declaration_boundary_artifact_reference": self._write_json(
                directory / "boundary-artifact.json", {"declared_only": True}
            ),
        }
        if hostile:
            for key, path in files.items():
                if path.suffix == ".md":
                    self._write_text(path, path.read_text(encoding="utf-8") + "\n".join(self.SENTINELS))
        return files

    def _missing_scope_request(self, files: dict[str, Path]) -> dict[str, object]:
        return resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_request(
            **{key: str(path) for key, path in files.items()}
        )

    def _recorded_request(self, files: dict[str, Path]) -> dict[str, object]:
        request = self._missing_scope_request(files)
        request.update(
            {
                "candidate_a_scope_id": "candidate_a_scope_mandate_integrity_gate",
                "candidate_b_scope_id": "candidate_b_scope_governed_surface_receipt_trace",
                "candidate_a_scope_statement": "Candidate A scope governs mandate integrity for proposed scope declarations.",
                "candidate_b_scope_statement": "Candidate B scope governs receipt trace for proposed scope declarations.",
                "candidate_a_scope_basis": "Mandate: integrity gate responsibility.",
                "candidate_b_scope_basis": "Governed surface: receipt trace responsibility.",
                "basis_bearing_scope_division_statement": "Candidate A and B differ by mandate and governed surface.",
                "basis_bearing_scope_division_basis": "The basis-bearing division names mandate and governed surface.",
            }
        )
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

    def assert_requires_basis(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_recorded(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_public_codes(self, result: dict[str, object]) -> None:
        for check in self._checks(result):
            for key in ("block_code", "failure_code"):
                if check.get(key) is not None:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_refusal_posture(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for key in (
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
            self.assertIs(operation.get(key), False, key)
        self.assertIs(operation.get("candidate_records_remain_non_standing"), True)
        self.assertIs(operation.get("candidate_records_remain_not_descendant_bodies"), True)

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_public_codes(result)
        self.assert_canonical_non_claims(result)
        self.assert_refusal_posture(result)

    def assert_wrapper_separation(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for key in (
            "outcome",
            "block",
            self.CHECKS_KEY,
            "non_claims",
            self.SUMMARY_KEY,
            "candidate_non_cosmetic_scope_division_declaration_operation_metadata",
        ):
            self.assertNotIn(key, operation)

    def assert_no_raw_bodies(self, result: dict[str, object]) -> None:
        serialized = json.dumps(result, ensure_ascii=True, sort_keys=True)
        for sentinel in self.SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_and_constants_v2(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2",
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path",
            "write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result",
            "build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_summary",
            "build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_DECLARATION_ONLY")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "NON_COSMETIC_SCOPE_DIVISION_DECLARATION_ONLY")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2"))
        self.assertNotEqual(str(resolver.OUTPUT_ROOT), str(resolver._v1.OUTPUT_ROOT))
        self.assertTrue(set(resolver._v1.REQUIRED_FALSE_NON_CLAIMS).issubset(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(set(resolver._v1.ALLOWED_TRUE_RECORDED_FIELDS).issubset(resolver.ALLOWED_TRUE_RECORDED_FIELDS))
        self.assertTrue({
            "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        }.issubset(resolver.BLOCK_CODES))

    def test_default_synthetic_missing_scope_request_returns_requires_additional_basis_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                self._missing_scope_request(self._basis_files(Path(temporary_directory)))
            )
        self.assert_requires_basis(result)
        metadata = result["candidate_non_cosmetic_scope_division_declaration_operation_metadata"]
        self.assertEqual(metadata["result_version"], "0.2.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertEqual(set(result["additional_basis_required"]), {
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        })
        operation = self._operation(result)
        for key, expected in {
            "candidate_non_cosmetic_scope_division_declaration_operation_type": resolver.OPERATION_TYPE,
            "candidate_non_cosmetic_scope_division_declaration_operation_version": resolver.OPERATION_VERSION,
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
            "operation_spec_markers_present": True,
            "completed_scope_division_declaration_boundary_terminal_summary_markers_present": True,
            "completed_basis_emission_operation_terminal_summary_markers_present": True,
            "completed_distinctness_operation_terminal_summary_markers_present": True,
            "completed_differentiation_operation_terminal_summary_markers_present": True,
        }.items():
            if isinstance(expected, bool):
                self.assertIs(operation.get(key), expected, key)
            else:
                self.assertEqual(operation.get(key), expected, key)
        self.assert_wrapper_separation(result)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)

    def test_default_live_target_requires_additional_basis_if_present_v2(self) -> None:
        required = (
            REPO_ROOT / resolver.DEFAULT_OPERATION_SPEC_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            REPO_ROOT / resolver.DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        )
        if not all(path.is_file() for path in required):
            self.skipTest("default v2 basis files are not all present")
        result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
            resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_request()
        )
        self.assert_requires_basis(result)
        operation = self._operation(result)
        self.assertIs(operation["completed_scope_division_declaration_boundary_terminal_summary_markers_present"], True)
        self.assertIs(operation["completed_differentiation_operation_terminal_summary_markers_present"], True)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)

    def test_completed_boundary_terminal_summary_acceptance_by_posture_class_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            for index, variant in enumerate(("full", "equivalent")):
                with self.subTest(variant=variant):
                    files = self._basis_files(
                        Path(temporary_directory) / self.safe_json_filename(variant, index).replace(".json", ""),
                        boundary_text=self._boundary_summary_text(variant),
                    )
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                        self._missing_scope_request(files)
                    )
                    self.assert_requires_basis(result)
                    self.assertIs(self._operation(result)["completed_scope_division_declaration_boundary_terminal_summary_markers_present"], True)
                    self.assert_refusal_posture(result)

    def test_completed_boundary_marker_rejection_by_missing_posture_class_v2(self) -> None:
        classes = (
            "boundary_recorded",
            "clean_v3_result",
            "future_operation_shape_allowed",
            "missing_upstream_scope_declarations_preserved",
            "scope_declarations_not_created",
            "scope_label_laundering_blocked",
            "scope_thesis",
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            for index, missing in enumerate(classes):
                with self.subTest(missing=missing):
                    files = self._basis_files(
                        Path(temporary_directory) / self.safe_json_filename(missing, index).replace(".json", ""),
                        boundary_text=self._boundary_summary_text(missing_class=missing),
                    )
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                        self._missing_scope_request(files)
                    )
                    self.assert_blocked(result)
                    self.assertEqual(self.block_code(result), "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING")

    def test_completed_differentiation_marker_acceptance_includes_standing_descendant_equivalents_v2(self) -> None:
        phrases = (
            "standing descendants were not created",
            "no standing descendants",
            "standing_descendant_created = false",
            "descendant_body_created = false",
            "no descendant bodies",
            "candidate_standing_authorized = false",
            "candidate records remain non-standing",
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            for index, phrase in enumerate(phrases):
                with self.subTest(phrase=phrase):
                    files = self._basis_files(
                        Path(temporary_directory) / self.safe_json_filename(phrase, index).replace(".json", ""),
                        differentiation_text=self._differentiation_summary_text(phrase),
                    )
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                        self._missing_scope_request(files)
                    )
                    self.assert_requires_basis(result)
                    self.assertIs(self._operation(result)["completed_differentiation_operation_terminal_summary_markers_present"], True)

    def test_completed_differentiation_marker_rejection_by_missing_posture_class_v2(self) -> None:
        classes = (
            "completion",
            "exactly_two_candidates",
            "non_standing_not_descendant_bodies",
            "standing_descendant_creation_not_authorized",
            "crossing_relation_not_authorized",
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            for index, missing in enumerate(classes):
                with self.subTest(missing=missing):
                    differentiation_text = self._differentiation_summary_text(
                        "standing descendants were not created", missing
                    )
                    if missing == "standing_descendant_creation_not_authorized":
                        differentiation_text = "\n".join(
                            (
                                "outcome = DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
                                "exactly two result-contained non-standing candidate records",
                                "two records are non-standing",
                                "two records are not descendant bodies",
                                "crossing_authorized = false",
                                "relation_created = false",
                            )
                        ) + "\n"
                    files = self._basis_files(
                        Path(temporary_directory) / self.safe_json_filename(missing, index).replace(".json", ""),
                        differentiation_text=differentiation_text,
                    )
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                        self._missing_scope_request(files)
                    )
                    self.assert_blocked(result)
                    self.assertEqual(self.block_code(result), "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING")

    def test_supported_declared_non_cosmetic_scope_request_records_operation_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._basis_files(Path(temporary_directory))
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                self._recorded_request(files)
            )
        self.assert_recorded(result)
        operation = self._operation(result)
        for key in (
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
            self.assertIs(operation[key], True, key)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)

    def test_cosmetic_or_label_only_scope_requests_do_not_record_v2(self) -> None:
        cases = {
            "identical": {"candidate_b_scope_statement": "Candidate A scope governs mandate integrity for proposed scope declarations."},
            "labels_only": {
                "candidate_a_scope_statement": "Candidate A label only.",
                "candidate_b_scope_statement": "Candidate B label only.",
                "candidate_a_scope_basis": "candidate id role label only",
                "candidate_b_scope_basis": "candidate id role label only",
                "basis_bearing_scope_division_statement": "candidate id role label only",
                "basis_bearing_scope_division_basis": "candidate id role label only",
            },
            "shared_evidence": {"basis_bearing_scope_division_basis": "shared evidence alone with mandate wording"},
            "operation_evidence": {"basis_bearing_scope_division_basis": "operation evidence alone with mandate wording"},
            "contaminated_lineage": {"basis_bearing_scope_division_basis": "contaminated lineage with mandate wording"},
            "laundering": {"scope_label_laundering_treated_as_basis": True},
            "cosmetic": {"cosmetic_scope_naming_treated_as_basis": True},
            "role_difference": {"id_role_label_difference_treated_as_scope_basis": True},
            "shared_flag": {"shared_evidence_treated_as_scope_basis": True},
            "operation_flag": {"operation_evidence_alone_treated_as_scope_basis": True},
            "lineage_flag": {"contaminated_lineage_treated_as_clean_scope_basis": True},
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._basis_files(Path(temporary_directory))
            for name, updates in cases.items():
                with self.subTest(name=name):
                    request = self._recorded_request(files)
                    request.update(updates)
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked(result)
                    else:
                        self.assert_requires_basis(result)
                        self.assert_refusal_posture(result)
                        self.assert_canonical_non_claims(result)

    def test_do_not_record_and_block_intents_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._basis_files(Path(temporary_directory))
            do_not_record = self._recorded_request(files)
            do_not_record["candidate_non_cosmetic_scope_division_declaration_operation_intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(do_not_record)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(not_recorded)
            self.assertIs(self._operation(not_recorded)["candidate_non_cosmetic_scope_division_declaration_operation_recorded"], False)
            self.assert_refusal_posture(not_recorded)
            self.assert_canonical_non_claims(not_recorded)
            blocked_request = self._recorded_request(files)
            blocked_request["candidate_non_cosmetic_scope_division_declaration_operation_intent"] = resolver.INTENT_BLOCK
            blocked = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(blocked_request)
        self.assert_blocked(blocked)
        self.assertEqual(self.block_code(blocked), "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCK_REQUESTED")

    def test_request_shape_and_marker_validation_blocking_behavior_v2(self) -> None:
        cases = {
            "unsupported_intent": ("candidate_non_cosmetic_scope_division_declaration_operation_intent", "OTHER"),
            "missing_type": ("candidate_non_cosmetic_scope_division_declaration_operation_type", None),
            "wrong_version": ("candidate_non_cosmetic_scope_division_declaration_operation_version", "9.9.9"),
            "wrong_scope": ("candidate_non_cosmetic_scope_division_declaration_operation_scope", "OTHER"),
            "wrong_route": ("admissible_future_route", "OTHER"),
            "missing_spec_ref": ("operation_spec_reference", ""),
            "missing_boundary_ref": ("completed_scope_division_declaration_boundary_terminal_summary_reference", ""),
            "wrong_candidate_id": ("candidate_record_a_id", "other"),
            "wrong_role": ("candidate_record_b_role", "OTHER"),
            "wrong_upstream_result": ("upstream_emission_operation_result", "RECORDED"),
            "wrong_policy": ("scope_declaration_policy", "OTHER"),
            "content_allowed": ("candidate_specific_content_emission_allowed", True),
            "rerun_allowed": ("basis_emission_operation_rerun_allowed", True),
            "standing_allowed": ("candidate_standing_authorized", True),
            "runtime_allowed": ("runtime_authorized", True),
            "scan_allowed": ("scan_allowed", True),
            "request_content": ("requested_candidate_specific_content_emission", True),
            "request_runtime": ("requested_runtime_creation", True),
            "request_repair": ("requested_affected_file_repair", True),
            "request_raw_body": ("requested_raw_markdown_body_return", True),
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._basis_files(Path(temporary_directory))
            for name, (field, value) in cases.items():
                with self.subTest(name=name):
                    request = self._recorded_request(files)
                    request[field] = value
                    self.assert_blocked(
                        resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
                    )
            files["operation_spec_reference"].write_text("missing all required markers\n", encoding="utf-8")
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
                    self._missing_scope_request(files)
                )
            )

    def test_required_false_posture_and_non_claim_canonicalization_v2(self) -> None:
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
            files = self._basis_files(Path(temporary_directory))
            clean = self._recorded_request(files)
            for field in fields:
                with self.subTest(top_level=field):
                    request = copy.deepcopy(clean)
                    request[field] = True
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][field], False)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=field):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][field], False)
            for malformed in (None, [], {}, {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}):
                with self.subTest(malformed=type(malformed).__name__):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"] = malformed
                    self.assert_blocked(
                        resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
                    )

    def test_sanitizer_path_write_non_mutation_summary_and_smoke_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            files = self._basis_files(directory / "basis", hostile=True)
            request = self._recorded_request(files)
            request["raw_markdown_body"] = self.SENTINELS[0]
            request["hidden_repo_state"] = self.SENTINELS[1]
            request["current_working_tree"] = self.SENTINELS[2]
            request_before = copy.deepcopy(request)
            contents_before = {key: path.read_text(encoding="utf-8") for key, path in files.items() if path.suffix == ".md"}
            recorded = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(request)
            self.assert_recorded(recorded)
            self.assert_no_raw_bodies(recorded)
            self.assertEqual(request, request_before)
            for key, original in contents_before.items():
                self.assertEqual(files[key].read_text(encoding="utf-8"), original)
            default_request = self._missing_scope_request(files)
            request_path = self._write_json(directory / "request.json", default_request)
            default_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path(request_path)
            self.assert_requires_basis(default_result)
            summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_summary(default_result)
            self.assertEqual(summary["result_version"], "0.2.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertIs(summary["completed_scope_division_declaration_boundary_terminal_summary_markers_present"], True)
            self.assertIs(summary["completed_differentiation_operation_terminal_summary_markers_present"], True)
            first = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result(
                default_result, directory / "output"
            )
            second = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result(
                default_result, directory / "output"
            )
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2", str(resolver.OUTPUT_ROOT))
            self.assertNotIn("scope_division_declaration_operation_v0_min/", str(resolver.OUTPUT_ROOT))
            malformed = directory / "malformed.json"
            self._write_text(malformed, "{")
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path(malformed)
            )
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path(directory / "missing.json")
            )
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path(
                    self._write_json(directory / "array.json", [])
                )
            )
        self.assert_wrapper_separation(default_result)
        self.assert_refusal_posture(default_result)
        self.assert_canonical_non_claims(default_result)


if __name__ == "__main__":
    unittest.main()
