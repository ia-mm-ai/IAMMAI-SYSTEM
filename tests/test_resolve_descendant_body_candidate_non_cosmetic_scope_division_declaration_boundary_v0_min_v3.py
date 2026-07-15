"""V3 tests for the candidate non-cosmetic scope-division declaration boundary.

V1 and v2 remain preserved lineage only. V2 synthetic, canonical false,
summary, and blocking posture held, but its default-live test exposed a brittle
completed differentiation terminal-summary marker count. This v3 suite targets
only the additive v3 resolver and pins the repair: completed differentiation is
accepted by five clean posture classes, not by an over-specific eight-marker
literal list. The boundary remains boundary-only: no scope declaration, no
candidate-specific content, no reruns, no standing, no descendant body, no
crossing or relation, no runtime, no authority/currentness, no repair, no scan,
and no follow-on work.
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

import resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3 as resolver


class CandidateNonCosmeticScopeDivisionDeclarationBoundaryV3Tests(unittest.TestCase):
    V3_REPAIR_KEYS = (
        "standing_authorized",
        "crossing_authorized",
        "follow_on_authorized",
        "follow_on_work_authorized",
        "affected_file_edited",
        "affected_file_deleted",
        "affected_file_overwritten",
        "affected_file_replaced",
        "affected_file_redeemed",
    )

    ALLOWED_TRUE_KEYS = (
        "candidate_non_cosmetic_scope_division_declaration_boundary_recorded",
        "boundary_created",
        "upstream_emission_operation_result_is_requires_additional_basis",
        "requires_additional_basis_preserved_as_clean_result",
        "candidate_a_scope_missing_upstream",
        "candidate_b_scope_missing_upstream",
        "basis_bearing_scope_division_missing_upstream",
        "future_scope_declaration_operation_shape_allowed",
        "scope_label_laundering_not_allowed",
        "cosmetic_scope_naming_not_allowed",
        "id_role_label_difference_not_allowed_as_scope_basis",
        "shared_evidence_not_allowed_as_scope_basis",
        "operation_evidence_alone_not_allowed_as_scope_basis",
        "contaminated_lineage_not_allowed_as_clean_scope_basis",
        "future_scope_declaration_operation_not_created",
        "candidate_a_scope_not_declared",
        "candidate_b_scope_not_declared",
        "basis_bearing_scope_division_not_declared",
        "candidate_specific_content_not_emitted",
        "separate_seal_material_not_emitted",
        "separate_lineage_receipt_material_not_emitted",
        "separate_digest_material_not_emitted",
        "emission_operation_not_rerun",
        "distinctness_operation_not_rerun",
        "distinctness_supported_not_recorded",
        "candidate_records_not_marked_distinct",
        "candidate_standing_not_authorized",
        "descendant_bodies_not_created",
        "standing_descendants_not_created",
        "first_crossing_not_authorized",
        "relation_not_created",
        "field_machinery_not_created",
        "runtime_not_created",
        "api_not_created",
        "currentness_not_created",
        "authority_not_created",
        "standing_not_created",
        "output_not_authorized",
        "action_not_authorized",
        "derivative_reception_not_authorized",
        "synchronization_not_authorized",
        "follow_on_not_authorized",
        "prior_unsupported_claims_not_validated",
        "affected_file_not_repaired",
        "affected_file_not_treated_as_clean_basis",
        "contaminated_lineage_not_treated_as_clean_basis",
        "existence_claim_evidence_check_not_overridden",
        "existence_claim_evidence_check_not_bypassed",
        "differentiation_operation_not_overridden",
        "differentiation_operation_not_bypassed",
        "distinctness_operation_boundary_not_overridden",
        "distinctness_operation_boundary_not_bypassed",
        "distinctness_operation_not_overridden",
        "distinctness_operation_not_bypassed",
        "basis_emission_boundary_not_overridden",
        "basis_emission_boundary_not_bypassed",
        "basis_emission_operation_not_overridden",
        "basis_emission_operation_not_bypassed",
        "scan_not_performed",
        "repository_scan_not_performed",
        "repair_not_performed",
        "validation_not_enforced",
        "hidden_repair_not_performed",
        "silent_overwrite_not_performed",
        "boundary_spec_markers_present",
        "completed_basis_emission_operation_terminal_summary_markers_present",
        "completed_basis_emission_boundary_terminal_summary_markers_present",
        "completed_distinctness_operation_terminal_summary_markers_present",
        "completed_differentiation_operation_terminal_summary_markers_present",
        "result_level_non_claims_canonical_false",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def block_code(self, result: dict) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("code") or block.get("block_code")

    def checks(self, result: dict) -> list[dict]:
        checks = result.get("candidate_non_cosmetic_scope_division_declaration_boundary_checks")
        return checks if isinstance(checks, list) else []

    def passed_check_count(self, result: dict) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def failed_check_count(self, result: dict) -> int:
        summary = result.get("candidate_non_cosmetic_scope_division_declaration_boundary_summary")
        if isinstance(summary, dict) and isinstance(summary.get("failed_check_count"), int):
            return summary["failed_check_count"]
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

    def emitted_codes(self, result: dict) -> set[str]:
        codes: set[str] = set()
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value:
                    codes.add(value)
        code = self.block_code(result)
        if code:
            codes.add(code)
        return codes

    def boundary(self, result: dict) -> dict:
        boundary = result.get("descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def summary(self, result: dict) -> dict:
        summary = result.get("candidate_non_cosmetic_scope_division_declaration_boundary_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def assert_not_blocked(self, result: dict) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(self, result: dict) -> None:
        for code in self.emitted_codes(result):
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: dict) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_v3_repair_keys_false(self, result: dict) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        summary = self.summary(result)
        for key in self.V3_REPAIR_KEYS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIn(key, summary)
            self.assertIs(summary[key], False, key)

    def assert_boundary_wrapper_separate(self, result: dict) -> None:
        boundary = self.boundary(result)
        for key in (
            "outcome",
            "block",
            "candidate_non_cosmetic_scope_division_declaration_boundary_checks",
            "non_claims",
            "candidate_non_cosmetic_scope_division_declaration_boundary_summary",
            "candidate_non_cosmetic_scope_division_declaration_boundary_metadata",
        ):
            self.assertNotIn(key, boundary)

    def assert_no_raw_markdown_body_returned(self, result: dict) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        ):
            self.assertNotIn(sentinel, serialized)

    def assert_no_forbidden_boundary_posture(self, result: dict) -> None:
        boundary = self.boundary(result)
        for key in (
            "future_scope_declaration_operation_not_created",
            "candidate_a_scope_not_declared",
            "candidate_b_scope_not_declared",
            "basis_bearing_scope_division_not_declared",
            "candidate_specific_content_not_emitted",
            "separate_seal_material_not_emitted",
            "separate_lineage_receipt_material_not_emitted",
            "separate_digest_material_not_emitted",
            "emission_operation_not_rerun",
            "distinctness_operation_not_rerun",
            "distinctness_supported_not_recorded",
            "candidate_records_not_marked_distinct",
            "candidate_standing_not_authorized",
            "descendant_bodies_not_created",
            "standing_descendants_not_created",
            "first_crossing_not_authorized",
            "relation_not_created",
            "field_machinery_not_created",
            "runtime_not_created",
            "currentness_not_created",
            "authority_not_created",
            "follow_on_not_authorized",
            "affected_file_not_repaired",
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
        ):
            self.assertIs(boundary.get(key), True, key)

    def assert_blocked_with_public_code(self, result: dict) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_v3_repair_keys_false(result)
        self.assert_no_forbidden_boundary_posture(result)

    def assert_recorded_boundary_posture(self, result: dict) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_canonical_false_non_claims(result)
        self.assert_v3_repair_keys_false(result)
        self.assert_boundary_wrapper_separate(result)
        boundary = self.boundary(result)
        for key in self.ALLOWED_TRUE_KEYS:
            if key == "result_level_non_claims_canonical_false":
                self.assertIs(self.summary(result).get(key), True, key)
            else:
                self.assertIs(boundary.get(key), True, key)
        self.assertEqual(
            boundary["candidate_non_cosmetic_scope_division_declaration_boundary_type"],
            resolver.BOUNDARY_TYPE,
        )
        self.assertEqual(
            boundary["candidate_non_cosmetic_scope_division_declaration_boundary_version"],
            resolver.BOUNDARY_VERSION,
        )
        self.assertEqual(
            boundary["future_scope_declaration_operation_type"],
            resolver.FUTURE_DECLARATION_OPERATION_TYPE,
        )
        self.assertEqual(boundary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
        self.assertEqual(boundary["upstream_emission_operation_result"], "REQUIRES_ADDITIONAL_BASIS")

    def differentiation_text(self, missing_class: str | None = None, variant: bool = False) -> str:
        if variant:
            lines = {
                "completion": "outcome = DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
                "two_records": "candidate_record_count = 2",
                "nonstanding": "candidate records are non-standing",
                "not_descendant": "candidate records are not descendant bodies",
                "standing": "standing_authorized = false",
                "crossing": "crossing_authorized = false",
                "relation": "relation_created = false",
            }
        else:
            lines = {
                "completion": "completed descendant-body differentiation operation line exists",
                "two_records": "exactly two candidate records emitted",
                "nonstanding": "candidate records are non-standing",
                "not_descendant": "candidate records are not descendant bodies",
                "standing": "standing descendants were not created",
                "crossing": "crossing was not authorized",
                "relation": "relation was not created",
            }
        omit = {
            "completion_or_operation_result": {"completion"},
            "exactly_two_candidate_records": {"two_records"},
            "nonstanding_and_not_descendant_body": {"not_descendant"},
            "standing_or_descendant_creation_not_authorized": {"standing"},
            "crossing_and_relation_not_authorized": {"relation"},
        }.get(missing_class, set())
        return "\n".join(value for key, value in lines.items() if key not in omit) + "\n"

    def basis_texts(
        self,
        include_sentinels: bool = False,
        differentiation_text: str | None = None,
    ) -> dict[str, str]:
        sentinels = ""
        if include_sentinels:
            sentinels = (
                "\nraw_body_note: RAW_MARKDOWN_BODY_MUST_NOT_RETURN\n"
                "hidden_repo_state_note: HIDDEN_REPO_STATE_MUST_NOT_RETURN\n"
                "current_working_tree_note: CURRENT_WORKING_TREE_MUST_NOT_RETURN\n"
            )
        return {
            "boundary_spec": (
                "# Descendant Body Candidate Non-Cosmetic Scope Division Declaration Boundary V0 Minimum Specification\n"
                "This file defines one boundary for a future candidate non-cosmetic scope-division declaration operation.\n"
                "This file is boundary-only.\n"
                "This file does not define, implement, or perform the future declaration operation.\n"
                "This file does not declare candidate A scope, candidate B scope, or basis-bearing scope division.\n"
                "This boundary exists to prevent a future scope declaration operation from laundering labels into scope division.\n"
                "Scope declaration is not scope standing.\n"
                "Scope declaration is not candidate-specific basis emission.\n"
                "Scope declaration is not distinctness support.\n"
                "A scope label is not a scope.\n"
                "A scope title is not a mandate.\n"
                "A scope id is not a governed surface.\n"
                "Scope division must be basis-bearing, not label-bearing.\n"
                "Candidate-specific basis must be basis-bearing, not label-bearing.\n"
                "For the immediate next repo-local step, this boundary permits only a future non-cosmetic scope-division declaration operation shape to be defined.\n"
                "candidate_a_scope_declared = false\n"
                "candidate_b_scope_declared = false\n"
                "basis_bearing_scope_division_declared = false\n"
                "scope_label_laundering_treated_as_basis = false\n"
                "cosmetic_scope_naming_treated_as_basis = false\n"
                "id_role_label_difference_treated_as_scope_basis = false\n"
                "shared_evidence_treated_as_scope_basis = false\n"
                "operation_evidence_alone_treated_as_scope_basis = false\n"
                "contaminated_lineage_treated_as_clean_scope_basis = false\n"
                + sentinels
            ),
            "basis_emission_operation": (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS\n"
                "REQUIRES_ADDITIONAL_BASIS\n"
                "failed_check_count = 0\n"
                "missing non-cosmetic candidate A scope\n"
                "missing non-cosmetic candidate B scope\n"
                "missing basis-bearing scope division\n"
                "material_emitted = false\n"
                "candidate_specific_content_emitted = false\n"
                "separate_seal_material_emitted = false\n"
                "separate_lineage_receipt_material_emitted = false\n"
                "separate_digest_material_emitted = false\n"
                "distinctness_operation_rerun = false\n"
                "distinctness_supported_recorded = false\n"
                "candidate_records_marked_distinct = false\n"
                "candidate_standing_authorized = false\n"
                "descendant_body_created = false\n"
                + sentinels
            ),
            "basis_emission_boundary": (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED\n"
                "SCOPE_DIVISION_ONLY\n"
                "scope division is the only immediate admissible future repo-local route\n"
                "scope division route allowed\n"
                "Candidate-specific basis must be basis-bearing, not label-bearing\n"
                "Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis\n"
                + sentinels
            ),
            "distinctness_operation": (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT\n"
                "distinctness_result = NOT_DISTINCT\n"
                "failed_check_count = 0\n"
                "candidate_record_count_compared = 2\n"
                "distinctness_supported = false\n"
                "NOT_DISTINCT is a clean operation result, not a failure\n"
                "id and role difference alone is not distinctness\n"
                "shared evidence reference alone is not distinctness\n"
                "Operation evidence alone is not distinctness\n"
                + sentinels
            ),
            "differentiation_operation": (differentiation_text or self.differentiation_text())
            + sentinels,
        }

    def write_synthetic_basis(self, base: Path, texts: dict[str, str] | None = None) -> dict[str, str]:
        texts = texts or self.basis_texts()
        basis_dir = base / "basis"
        basis_dir.mkdir(parents=True, exist_ok=True)
        filenames = {
            "boundary_spec": "boundary_spec.md",
            "basis_emission_operation": "basis_emission_operation_terminal_summary.md",
            "basis_emission_boundary": "basis_emission_boundary_terminal_summary.md",
            "distinctness_operation": "distinctness_operation_terminal_summary.md",
            "differentiation_operation": "differentiation_operation_terminal_summary.md",
        }
        paths: dict[str, str] = {}
        for key, filename in filenames.items():
            path = basis_dir / filename
            path.write_text(texts[key], encoding="utf-8")
            paths[key] = str(path)
        return paths

    def valid_request(
        self,
        base: Path,
        include_sentinels: bool = False,
        differentiation_text: str | None = None,
    ) -> dict:
        paths = self.write_synthetic_basis(
            base,
            self.basis_texts(include_sentinels, differentiation_text=differentiation_text),
        )
        return resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_request(
            boundary_spec_reference=paths["boundary_spec"],
            completed_basis_emission_operation_terminal_summary_reference=paths["basis_emission_operation"],
            completed_basis_emission_boundary_terminal_summary_reference=paths["basis_emission_boundary"],
            completed_distinctness_operation_terminal_summary_reference=paths["distinctness_operation"],
            completed_differentiation_operation_terminal_summary_reference=paths["differentiation_operation"],
        )

    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3(
            request
        )

    def test_public_api_and_constants_v3(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_from_path",
            "write_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result",
            "build_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_summary",
            "build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_request",
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
            "BOUNDARY_TYPE",
            "FUTURE_DECLARATION_OPERATION_TYPE",
            "BOUNDARY_VERSION",
            "RUPTURE_CLASS_BLOCKED",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.3.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY",
        )
        self.assertEqual(
            resolver.FUTURE_DECLARATION_OPERATION_TYPE,
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
        )
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.RUPTURE_CLASS_BLOCKED, "SCOPE_LABEL_LAUNDERING")
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        output_root = str(resolver.OUTPUT_ROOT)
        self.assertTrue(
            output_root.endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3"
            )
        )
        self.assertNotEqual(
            output_root,
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min",
        )
        self.assertNotEqual(
            output_root,
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v2",
        )
        for key in self.V3_REPAIR_KEYS:
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS, key)
        for key in self.ALLOWED_TRUE_KEYS:
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS, key)
        for code in (
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "SCOPE_LABEL_LAUNDERING_TREATED_AS_BASIS_TRUE",
            "COSMETIC_SCOPE_NAMING_TREATED_AS_BASIS_TRUE",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_SCOPE_BASIS_TRUE",
            "SHARED_EVIDENCE_TREATED_AS_SCOPE_BASIS_TRUE",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_SCOPE_BASIS_TRUE",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_SCOPE_BASIS_TRUE",
        ):
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_default_synthetic_basis_records_boundary_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir))
            result = self.resolve(request)
            self.assertIsInstance(result, dict)
            self.assert_recorded_boundary_posture(result)
            self.assertEqual(self.summary(result)["result_version"], "0.3.0")
            self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(
                self.boundary(result)["candidate_non_cosmetic_scope_division_declaration_boundary_id"],
                "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_001",
            )
            for key in (
                "candidate_non_cosmetic_scope_division_declaration_boundary_metadata",
                "declared_candidate_non_cosmetic_scope_division_declaration_boundary_question",
                "upstream_basis",
                "candidate_non_cosmetic_scope_division_declaration_boundary_basis",
                "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary",
                "candidate_non_cosmetic_scope_division_declaration_boundary_checks",
                "candidate_non_cosmetic_scope_division_declaration_boundary_statement",
                "candidate_non_cosmetic_scope_division_declaration_boundary_non_meaning",
                "not_recorded_basis",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "candidate_non_cosmetic_scope_division_declaration_boundary_summary",
            ):
                self.assertIn(key, result)

    def test_records_default_live_target_if_present_v3(self) -> None:
        required = [
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md",
        ]
        missing = [path for path in required if not path.exists()]
        if missing:
            self.skipTest(f"default live target files missing: {missing}")
        request = resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_request()
        result = self.resolve(request)
        self.assert_recorded_boundary_posture(result)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], "0.3.0")
        self.assertIs(summary["completed_differentiation_operation_terminal_summary_markers_present"], True)
        basis = result["upstream_basis"]["basis_summaries"]["completed_differentiation_operation_terminal_summary"]
        self.assertEqual(basis["required_marker_count"], 5)
        self.assertEqual(basis["present_marker_count"], 5)
        self.assertEqual(basis["missing_posture_classes"], [])

    def test_completed_differentiation_marker_acceptance_by_posture_class_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(
                Path(temp_dir),
                differentiation_text=self.differentiation_text(variant=True),
            )
            result = self.resolve(request)
            self.assert_recorded_boundary_posture(result)
            basis = result["upstream_basis"]["basis_summaries"]["completed_differentiation_operation_terminal_summary"]
            self.assertTrue(basis["markers_present"])
            self.assertEqual(basis["required_marker_count"], 5)
            self.assertEqual(basis["present_marker_count"], 5)
            self.assertEqual(basis["missing_posture_classes"], [])
            self.assertTrue(all(basis["posture_classes"].values()))

    def test_completed_differentiation_marker_rejection_by_missing_posture_class_v3(self) -> None:
        for posture_class in (
            "completion_or_operation_result",
            "exactly_two_candidate_records",
            "nonstanding_and_not_descendant_body",
            "standing_or_descendant_creation_not_authorized",
            "crossing_and_relation_not_authorized",
        ):
            with self.subTest(posture_class=posture_class), tempfile.TemporaryDirectory() as temp_dir:
                request = self.valid_request(
                    Path(temp_dir),
                    differentiation_text=self.differentiation_text(missing_class=posture_class),
                )
                result = self.resolve(request)
                self.assert_blocked_with_public_code(result)
                self.assertEqual(
                    self.block_code(result),
                    "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
                )
                basis = result["upstream_basis"]["basis_summaries"]["completed_differentiation_operation_terminal_summary"]
                self.assertIn(posture_class, basis["missing_posture_classes"])

    def test_do_not_record_intent_does_not_record_boundary_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir))
            request["candidate_non_cosmetic_scope_division_declaration_boundary_intent"] = (
                "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
            )
            result = self.resolve(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            boundary = self.boundary(result)
            self.assertIs(boundary["boundary_created"], False)
            self.assertIs(
                boundary["candidate_non_cosmetic_scope_division_declaration_boundary_recorded"],
                False,
            )
            self.assert_no_forbidden_boundary_posture(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_v3_repair_keys_false(result)

    def test_block_intent_blocks_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir))
            request["candidate_non_cosmetic_scope_division_declaration_boundary_intent"] = (
                "BLOCK_DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY"
            )
            result = self.resolve(request)
            self.assert_blocked_with_public_code(result)

    def test_request_shape_and_blocking_behavior_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base_request = self.valid_request(Path(temp_dir))
            non_mapping = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3([])
            self.assert_blocked_with_public_code(non_mapping)
            cases = [
                ("missing_question", lambda r: r.pop("candidate_non_cosmetic_scope_division_declaration_boundary_question", None)),
                ("unsupported_intent", lambda r: r.__setitem__("candidate_non_cosmetic_scope_division_declaration_boundary_intent", "UNSUPPORTED")),
                ("missing_type", lambda r: r.pop("candidate_non_cosmetic_scope_division_declaration_boundary_type", None)),
                ("wrong_type", lambda r: r.__setitem__("candidate_non_cosmetic_scope_division_declaration_boundary_type", "WRONG")),
                ("missing_version", lambda r: r.pop("candidate_non_cosmetic_scope_division_declaration_boundary_version", None)),
                ("wrong_version", lambda r: r.__setitem__("candidate_non_cosmetic_scope_division_declaration_boundary_version", "9.9.9")),
                ("missing_future_type", lambda r: r.pop("future_scope_declaration_operation_type", None)),
                ("wrong_future_type", lambda r: r.__setitem__("future_scope_declaration_operation_type", "WRONG")),
                ("missing_rupture", lambda r: r.pop("rupture_class_blocked", None)),
                ("wrong_rupture", lambda r: r.__setitem__("rupture_class_blocked", "WRONG")),
                ("missing_boundary_spec", lambda r: r.pop("boundary_spec_reference", None)),
                ("missing_operation_summary", lambda r: r.pop("completed_basis_emission_operation_terminal_summary_reference", None)),
                ("missing_boundary_summary", lambda r: r.pop("completed_basis_emission_boundary_terminal_summary_reference", None)),
                ("missing_distinctness_summary", lambda r: r.pop("completed_distinctness_operation_terminal_summary_reference", None)),
                ("missing_differentiation_summary", lambda r: r.pop("completed_differentiation_operation_terminal_summary_reference", None)),
                ("wrong_upstream_result", lambda r: r.__setitem__("upstream_emission_operation_result", "RECORDED")),
                ("requires_additional_not_clean", lambda r: r.__setitem__("requires_additional_basis_preserved_as_clean_result", False)),
                ("candidate_a_missing_false", lambda r: r.__setitem__("candidate_a_scope_missing_upstream", False)),
                ("candidate_b_missing_false", lambda r: r.__setitem__("candidate_b_scope_missing_upstream", False)),
                ("scope_division_missing_false", lambda r: r.__setitem__("basis_bearing_scope_division_missing_upstream", False)),
                ("future_shape_false", lambda r: r.__setitem__("future_scope_declaration_operation_shape_allowed", False)),
                ("scan_allowed", lambda r: r.__setitem__("scan_allowed", True)),
                ("repair_allowed", lambda r: r.__setitem__("repair_allowed", True)),
                ("validation_allowed", lambda r: r.__setitem__("validation_enforcement_allowed", True)),
            ]
            for field in (
                "scope_label_laundering_treated_as_basis",
                "cosmetic_scope_naming_treated_as_basis",
                "id_role_label_difference_treated_as_scope_basis",
                "shared_evidence_treated_as_scope_basis",
                "operation_evidence_alone_treated_as_scope_basis",
                "contaminated_lineage_treated_as_clean_scope_basis",
                "future_scope_declaration_operation_created",
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
                "candidate_standing_authorized",
                "descendant_body_created",
                "standing_authorized",
                "crossing_authorized",
                "relation_authorized",
                "field_machinery_authorized",
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
            ):
                cases.append((field, lambda r, f=field: r.__setitem__(f, True)))
            for field in getattr(resolver, "REQUESTED_ACTION_FIELD_CODES", {}):
                request_alias = "request_" + field.removeprefix("requested_")
                cases.append(
                    (
                        request_alias,
                        lambda r, f=field, a=request_alias: (
                            r.__setitem__(a, True),
                            r.__setitem__(f, True),
                        ),
                    )
                )
            cases.append(
                (
                    "return_raw_markdown_body",
                    lambda r: (
                        r.__setitem__("return_raw_markdown_body", True),
                        r.__setitem__("requested_raw_markdown_body_return", True),
                    ),
                )
            )
            for name, mutate in cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)

    def test_marker_validation_blocking_behavior_v3(self) -> None:
        marker_cases = {
            "boundary_spec": ("A scope title is not a mandate.", "BOUNDARY_SPEC_MARKER_MISSING"),
            "basis_emission_operation": ("missing non-cosmetic candidate A scope", "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            "basis_emission_boundary": ("Candidate-specific basis must be basis-bearing, not label-bearing", "COMPLETED_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"),
            "distinctness_operation": ("Operation evidence alone is not distinctness", "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
        }
        for key, (marker, expected_code) in marker_cases.items():
            with self.subTest(key=key), tempfile.TemporaryDirectory() as temp_dir:
                texts = self.basis_texts()
                texts[key] = texts[key].replace(marker, "")
                paths = self.write_synthetic_basis(Path(temp_dir), texts)
                request = resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_request(
                    boundary_spec_reference=paths["boundary_spec"],
                    completed_basis_emission_operation_terminal_summary_reference=paths["basis_emission_operation"],
                    completed_basis_emission_boundary_terminal_summary_reference=paths["basis_emission_boundary"],
                    completed_distinctness_operation_terminal_summary_reference=paths["distinctness_operation"],
                    completed_differentiation_operation_terminal_summary_reference=paths["differentiation_operation"],
                )
                result = self.resolve(request)
                self.assert_blocked_with_public_code(result)
                self.assertIn(expected_code, self.emitted_codes(result))

    def test_required_false_top_level_posture_blocks_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base_request = self.valid_request(Path(temp_dir))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(field=field):
                    request = copy.deepcopy(base_request)
                    request[field] = True
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"].get(field), False)

    def test_required_false_non_claim_canonicalization_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base_request = self.valid_request(Path(temp_dir))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = {
                "missing_declared_non_claims": lambda r: r.pop("declared_non_claims", None),
                "non_mapping_declared_non_claims": lambda r: r.__setitem__("declared_non_claims", []),
                "missing_required_key": lambda r: r["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0], None),
                "non_bool_value": lambda r: r["declared_non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false"),
            }
            for name, mutate in malformed_cases.items():
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)

    def test_sanitizer_behavior_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir), include_sentinels=True)
            recorded = self.resolve(request)
            self.assertEqual(recorded["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_no_raw_markdown_body_returned(recorded)
            serialized = json.dumps(recorded, sort_keys=True)
            self.assertIn(resolver.BOUNDARY_TYPE, serialized)
            self.assertIn(resolver.OUTCOME_RECORDED, serialized)
            blocked_request = copy.deepcopy(request)
            blocked_request["scope_label_laundering_treated_as_basis"] = True
            blocked = self.resolve(blocked_request)
            self.assert_blocked_with_public_code(blocked)
            self.assert_no_raw_markdown_body_returned(blocked)
            self.assertIn(resolver.BOUNDARY_TYPE, json.dumps(blocked, sort_keys=True))

    def test_from_path_and_write_behavior_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            request = self.valid_request(base)
            request_path = base / "request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_from_path(request_path)
            self.assert_recorded_boundary_posture(result)
            missing = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_from_path(base / "missing.json")
            self.assert_blocked_with_public_code(missing)
            malformed = base / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_from_path(malformed)
            self.assert_blocked_with_public_code(malformed_result)
            array_path = base / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_from_path(array_path)
            self.assert_blocked_with_public_code(array_result)

            explicit_dir = base / "explicit_v3_output"
            explicit = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result(
                result,
                explicit_dir,
            )
            self.assertTrue(explicit.exists())
            self.assertIsInstance(json.loads(explicit.read_text(encoding="utf-8")), dict)
            self.assertIn("candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result", explicit.name)

            old_output_root = resolver.OUTPUT_ROOT
            patched_output_root = (
                base
                / "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3"
            )
            try:
                resolver.OUTPUT_ROOT = patched_output_root
                first = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result(result)
                second = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result(result)
            finally:
                resolver.OUTPUT_ROOT = old_output_root

            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_result", first.name)
            self.assertIn(
                "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
                first.parts,
            )
            self.assertIsInstance(json.loads(first.read_text(encoding="utf-8")), dict)
            forbidden_parts = {
                "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v2",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_operation",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary",
                "integrity_host_v0_min_coexistence_descendant_body_basis",
                "integrity_host_v0_min_coexistence_seam_case",
                "integrity_host_v0_min_coexistence_local_relevance_medium",
                "integrity_host_v0_min_coexistence_source_transfer",
                "integrity_host_v0_min_coexistence_source_receipt",
                "integrity_host_v0_min_coexistence_public_api",
                "integrity_host_v0_min_coexistence_participant_facing_interface",
                "integrity_host_v0_min_coexistence_distributed_network",
                "integrity_host_v0_min_coexistence_runtime_hosting",
                "integrity_host_v0_min_coexistence_runtime_loop",
                "integrity_host_v0_min_coexistence_daemon",
            }
            self.assertTrue(forbidden_parts.isdisjoint(set(first.parts)))

    def test_non_mutation_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            request = self.valid_request(base, include_sentinels=True)
            before_request = copy.deepcopy(request)
            basis_paths = [
                Path(request["boundary_spec_reference"]),
                Path(request["completed_basis_emission_operation_terminal_summary_reference"]),
                Path(request["completed_basis_emission_boundary_terminal_summary_reference"]),
                Path(request["completed_distinctness_operation_terminal_summary_reference"]),
                Path(request["completed_differentiation_operation_terminal_summary_reference"]),
            ]
            before_files = {path: path.read_text(encoding="utf-8") for path in basis_paths}
            result = self.resolve(request)
            self.assertEqual(request, before_request)
            self.assert_recorded_boundary_posture(result)
            for path, text in before_files.items():
                self.assertEqual(path.read_text(encoding="utf-8"), text)

    def test_summary_behavior_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir))
            result = self.resolve(request)
            summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.3.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(
                summary["candidate_non_cosmetic_scope_division_declaration_boundary_id"],
                "descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_001",
            )
            self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(summary["boundary_version"], "0.1.0")
            self.assertEqual(summary["future_declaration_operation_type"], resolver.FUTURE_DECLARATION_OPERATION_TYPE)
            self.assertEqual(summary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
            self.assertEqual(summary["upstream_emission_operation_result"], "REQUIRES_ADDITIONAL_BASIS")
            for key in self.ALLOWED_TRUE_KEYS:
                self.assertIs(summary.get(key), True, key)
            for key in (
                "scope_label_laundering_treated_as_basis",
                "cosmetic_scope_naming_treated_as_basis",
                "id_role_label_difference_treated_as_scope_basis",
                "shared_evidence_treated_as_scope_basis",
                "operation_evidence_alone_treated_as_scope_basis",
                "contaminated_lineage_treated_as_clean_scope_basis",
                "candidate_non_cosmetic_scope_division_declaration_operation_created",
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
                "candidate_standing_authorized",
                "descendant_body_created",
                "standing_authorized",
                "crossing_authorized",
                "relation_authorized",
                "field_machinery_authorized",
                "runtime_created",
                "api_created",
                "currentness_created",
                "authority_created",
                "output_authorized",
                "action_authorized",
                "derivative_reception_authorized",
                "synchronization_authorized",
                "follow_on_authorized",
                "follow_on_work_authorized",
                "prior_unsupported_candidate_a_claim_validated",
                "prior_unsupported_candidate_b_claim_validated",
                "prior_unsupported_derivation_event_claim_validated",
                "affected_file_repaired",
                "affected_file_edited",
                "affected_file_deleted",
                "affected_file_overwritten",
                "affected_file_replaced",
                "affected_file_redeemed",
                "affected_file_treated_as_clean_basis",
                "contaminated_lineage_treated_as_clean_basis",
                "existence_claim_evidence_check_overridden",
                "existence_claim_evidence_check_bypassed",
                "differentiation_operation_overridden",
                "differentiation_operation_bypassed",
                "distinctness_operation_boundary_overridden",
                "distinctness_operation_boundary_bypassed",
                "distinctness_operation_overridden",
                "distinctness_operation_bypassed",
                "candidate_specific_distinctness_basis_emission_boundary_overridden",
                "candidate_specific_distinctness_basis_emission_boundary_bypassed",
                "candidate_specific_distinctness_basis_emission_operation_overridden",
                "candidate_specific_distinctness_basis_emission_operation_bypassed",
                "scan_performed",
                "repository_scan_performed",
                "repair_performed",
                "validation_enforced",
                "hidden_repair_performed",
                "silent_overwrite_performed",
            ):
                self.assertIs(summary.get(key), False, key)

    def test_smoke_behavior_default_boundary_recorded_v3(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(Path(temp_dir))
            result = self.resolve(request)
            summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.3.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            boundary = self.boundary(result)
            self.assertEqual(boundary["candidate_non_cosmetic_scope_division_declaration_boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(boundary["candidate_non_cosmetic_scope_division_declaration_boundary_version"], "0.1.0")
            self.assertEqual(boundary["future_scope_declaration_operation_type"], resolver.FUTURE_DECLARATION_OPERATION_TYPE)
            self.assertEqual(boundary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
            self.assertEqual(boundary["upstream_emission_operation_result"], "REQUIRES_ADDITIONAL_BASIS")
            for key in (
                "candidate_non_cosmetic_scope_division_declaration_boundary_recorded",
                "boundary_created",
                "requires_additional_basis_preserved_as_clean_result",
                "candidate_a_scope_missing_upstream",
                "candidate_b_scope_missing_upstream",
                "basis_bearing_scope_division_missing_upstream",
                "future_scope_declaration_operation_shape_allowed",
                "scope_label_laundering_not_allowed",
                "cosmetic_scope_naming_not_allowed",
                "id_role_label_difference_not_allowed_as_scope_basis",
                "shared_evidence_not_allowed_as_scope_basis",
                "operation_evidence_alone_not_allowed_as_scope_basis",
                "contaminated_lineage_not_allowed_as_clean_scope_basis",
                "future_scope_declaration_operation_not_created",
                "candidate_a_scope_not_declared",
                "candidate_b_scope_not_declared",
                "basis_bearing_scope_division_not_declared",
                "candidate_specific_content_not_emitted",
                "separate_seal_material_not_emitted",
                "separate_lineage_receipt_material_not_emitted",
                "separate_digest_material_not_emitted",
                "emission_operation_not_rerun",
                "distinctness_operation_not_rerun",
                "distinctness_supported_not_recorded",
                "candidate_records_not_marked_distinct",
                "candidate_standing_not_authorized",
                "descendant_bodies_not_created",
                "first_crossing_not_authorized",
                "relation_not_created",
                "runtime_not_created",
                "currentness_not_created",
                "authority_not_created",
                "follow_on_not_authorized",
                "completed_differentiation_operation_terminal_summary_markers_present",
            ):
                self.assertIs(boundary.get(key), True, key)
            self.assert_boundary_wrapper_separate(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_v3_repair_keys_false(result)


if __name__ == "__main__":
    unittest.main()
