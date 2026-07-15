"""Bounded tests for the candidate-record distinctness support recheck.

The suite proves a supported recheck stays local to two existing non-standing
candidate records. It records no standing, descendant body, relation, runtime,
authority, coupling, presence, identity, repair, discovery, or follow-on work.
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

import resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min as resolver


class DescendantBodyCandidateRecordDistinctnessSupportRecheckOperationV0MinTests(unittest.TestCase):
    """Exercise one support recheck without broadening its bounded posture."""

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, directory: Path, name: str, text: str) -> Path:
        path = directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.exists() and path.is_dir(), f"synthetic Markdown path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, directory: Path, name: str, value: object) -> Path:
        path = directory / self.safe_json_filename(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.exists() and path.is_dir(), f"synthetic JSON path is a directory: {path}")
        path.write_text(json.dumps(value, ensure_ascii=True, indent=2, default=str), encoding="utf-8")
        return path

    def valid_recheck_spec_text(self) -> str:
        lines = ["# Synthetic Distinctness Support Recheck Operation"]
        for _, markers in resolver.OPERATION_SPEC_MARKER_CLASSES:
            lines.extend(markers)
        return "\n".join(lines) + "\n"

    def valid_prior_distinctness_summary_text(self) -> str:
        return "\n".join((
            "# Prior Distinctness Summary",
            resolver.PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 80",
            "distinctness_result = NOT_DISTINCT",
            "distinctness_supported = false",
            "candidate records with distinct ids and roles",
            "candidate-specific content and separate seal, receipt, and digest material were absent",
            "compared 2 candidate records",
            "ids and roles were distinct",
            "candidate-specific content was absent",
            "separate seal, receipt, and digest material were absent",
        )) + "\n"

    def valid_successor_basis_emission_summary_text(self) -> str:
        return "\n".join((
            "# Successor Basis Emission Summary",
            resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 83",
            resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED,
            "candidate_specific_content_emitted = true",
            "candidate_a_basis_material_emitted = true",
            "candidate_b_basis_material_emitted = true",
            "separate_candidate_basis_material_emitted = true",
            "basis_pair_emitted = true",
            resolver.UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            resolver.UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            resolver.UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            resolver.UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "basis_pair_scope = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
            "Candidate A basis material is non-standing.",
            "Candidate B basis material is non-standing.",
            "non_standing_basis = true",
            "candidate_a_and_b_are_sibling_non_standing_basis_materials = true",
            "neither_candidate_ranks_above_the_other = true",
            "regulation_not_sovereign_over_motion = true",
            "motion_does_not_erase_regulation = true",
            "coupling_assigned = false",
            "coupling_created = false",
            "third_candidate_created = false",
            "third_model_admitted = false",
            "candidate_records_marked_distinct = false",
            "candidate_records_distinct = false",
            "distinctness_supported_recorded = false",
            "candidate_standing_authorized = false",
            "descendant_body_created = false",
            "relation_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
            "Candidate A and Candidate B basis materials remain sibling non-standing basis materials.",
            "neither candidate basis ranks above the other",
            "Regulation is not sovereign over Motion",
            "Motion does not erase Regulation",
            "coupling remains unassigned and uncreated",
        )) + "\n"

    def valid_existence_claim_evidence_check_summary_text(self) -> str:
        return "\n".join((
            "# Existence Claim Evidence Check Summary",
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        )) + "\n"

    def valid_prior_basis_emission_summary_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS\n"

    def valid_successor_closure_summary_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED\n"

    def valid_scope_division_operation_summary_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS\n"

    def build_synthetic_paths(self, directory: Path) -> dict[str, Path]:
        return {
            "operation_spec_reference": self.write_markdown(directory, "recheck_spec.md", self.valid_recheck_spec_text()),
            "prior_distinctness_operation_terminal_summary_reference": self.write_markdown(
                directory, "prior_distinctness.md", self.valid_prior_distinctness_summary_text()
            ),
            "successor_basis_emission_terminal_summary_reference": self.write_markdown(
                directory, "successor_basis_emission.md", self.valid_successor_basis_emission_summary_text()
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(
                directory, "existence_claim.md", self.valid_existence_claim_evidence_check_summary_text()
            ),
            "basis_emission_operation_terminal_summary_reference": self.write_markdown(
                directory, "prior_basis_emission.md", self.valid_prior_basis_emission_summary_text()
            ),
            "successor_closure_operation_terminal_summary_reference": self.write_markdown(
                directory, "successor_closure.md", self.valid_successor_closure_summary_text()
            ),
            "scope_division_operation_terminal_summary_reference": self.write_markdown(
                directory, "scope_division.md", self.valid_scope_division_operation_summary_text()
            ),
        }

    def build_valid_request(self, directory: Path, **overrides: object) -> tuple[dict[str, object], dict[str, Path]]:
        paths = self.build_synthetic_paths(directory)
        request = resolver.build_declared_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_request(
            **paths
        )
        request.update(overrides)
        return request, paths

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def passed_check_count(self, result: dict[str, object]) -> int:
        checks = result.get("distinctness_support_recheck_operation_checks", [])
        return sum(check.get("passed") is True for check in checks if isinstance(check, dict))

    def failed_check_count(self, result: dict[str, object]) -> int:
        checks = result.get("distinctness_support_recheck_operation_checks", [])
        return sum(check.get("passed") is False for check in checks if isinstance(check, dict))

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        operation = result.get("descendant_body_candidate_record_distinctness_support_recheck_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        checks = result.get("distinctness_support_recheck_operation_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, dict):
                continue
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_operation_excludes_wrapper(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in (
            "outcome",
            "block",
            "distinctness_support_recheck_operation_checks",
            "non_claims",
            "distinctness_support_recheck_operation_summary",
            "distinctness_support_recheck_operation_metadata",
            "distinctness_support_recheck_material",
        ):
            self.assertNotIn(key, operation)

    def assert_no_downstream_conversion(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation[key], False, key)
        self.assertIs(operation["candidate_standing_authorized"], False)
        self.assertIs(operation["descendant_body_created"], False)
        self.assertIs(operation["relation_created"], False)
        self.assertIs(operation["runtime_created"], False)
        self.assertIs(operation["coupling_created"], False)
        self.assertIs(operation["third_model_admitted"], False)
        self.assertIs(operation["presence_established"], False)
        self.assertIs(operation["identity_created"], False)
        self.assertIs(operation["follow_on_authorized"], False)

    def assert_supported_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertEqual(result["block"], {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        })

    def assert_requires_basis_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_BASIS_EMISSION)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block["blocked"], False)
        self.assertIsNone(block["code"])

    def assert_not_supported_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_SUPPORTED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block["blocked"], False)
        self.assertIsNone(block["code"])

    def assert_blocked_public(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_check_count(result), 0)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_downstream_conversion(result)

    def assert_supported_shape(self, result: dict[str, object]) -> None:
        self.assert_supported_not_blocked(result)
        self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_canonical_non_claims(result)
        self.assert_operation_excludes_wrapper(result)
        self.assert_no_downstream_conversion(result)
        operation = self.operation(result)
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[field], True, field)
        self.assertEqual(operation["distinctness_support_recheck_result"], "DISTINCTNESS_SUPPORT_RECHECKED")
        self.assertEqual(operation["distinctness_support_result"], "DISTINCTNESS_SUPPORTED")
        self.assertNotIn("distinctness_support_recheck_material", operation)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min",
            "resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path",
            "write_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_result",
            "build_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min")
        self.assertEqual(resolver.OPERATION_ID, "descendant_body_candidate_record_distinctness_support_recheck_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "RECHECK_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_AFTER_CANDIDATE_SPECIFIC_BASIS_EMISSION_ONLY")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_RESULT_REQUIRED, "NOT_DISTINCT")
        self.assertIs(resolver.PRIOR_DISTINCTNESS_SUPPORTED_REQUIRED, False)
        self.assertEqual(resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION")
        self.assertEqual(resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED")
        self.assertEqual(resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED, "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED")
        for name in (
            "UPSTREAM_CANDIDATE_SPECIFIC_CONTENT_EMITTED_REQUIRED",
            "UPSTREAM_CANDIDATE_A_BASIS_MATERIAL_EMITTED_REQUIRED",
            "UPSTREAM_CANDIDATE_B_BASIS_MATERIAL_EMITTED_REQUIRED",
            "UPSTREAM_SEPARATE_CANDIDATE_BASIS_MATERIAL_EMITTED_REQUIRED",
            "UPSTREAM_BASIS_PAIR_EMITTED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        self.assertEqual(resolver.UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED, "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis")
        self.assertEqual(resolver.UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED, "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis")
        self.assertEqual(resolver.UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED, "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS")
        self.assertEqual(resolver.UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED, "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS")
        self.assertEqual(resolver.UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED, "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY")
        for name in (
            "UPSTREAM_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED",
            "UPSTREAM_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED",
            "UPSTREAM_CANDIDATE_STANDING_AUTHORIZED_REQUIRED",
            "UPSTREAM_DESCENDANT_BODY_CREATED_REQUIRED",
            "UPSTREAM_RELATION_CREATED_REQUIRED",
            "UPSTREAM_COUPLING_CREATED_REQUIRED",
            "UPSTREAM_PRESENCE_ESTABLISHED_REQUIRED",
            "UPSTREAM_IDENTITY_CREATED_REQUIRED",
            "UPSTREAM_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "DISTINCTNESS_SUPPORT_RECHECK_THEN_CANDIDATE_STANDING_BOUNDARY_CONSIDERATION_ONLY")
        self.assertTrue(set((
            resolver.OUTCOME_SUPPORTED,
            resolver.OUTCOME_NOT_SUPPORTED,
            resolver.OUTCOME_REQUIRES_BASIS_EMISSION,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        )).issubset(resolver.OUTCOME_FAMILY))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min"
        ))
        for code in (
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SPEC_REFERENCE_MISSING",
            "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "BASIS_EMISSION_MATERIAL_MISSING_OR_INSUFFICIENT", "BASIS_EMISSION_MATERIAL_NOT_SUPPORTING_DISTINCTNESS",
            "NON_CLAIM_MISSING_OR_FLIPPED", "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
            "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED", "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
            "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_synthetic_complete_recheck_records_supported_and_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_request(Path(temporary))
            result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(request)
        self.assert_supported_shape(result)
        expected_sections = {
            "distinctness_support_recheck_operation_metadata",
            "declared_distinctness_support_recheck_operation_basis",
            "upstream_basis",
            "descendant_body_candidate_record_distinctness_support_recheck_operation",
            "distinctness_support_recheck_material",
            "distinctness_support_recheck_operation_checks",
            "distinctness_support_recheck_operation_statement",
            "distinctness_support_recheck_operation_non_meaning",
            "recheck_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "distinctness_support_recheck_operation_summary",
        }
        self.assertTrue(expected_sections.issubset(result))
        operation = self.operation(result)
        self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["prior_distinctness_operation_type"], resolver.PRIOR_DISTINCTNESS_OPERATION_TYPE)
        self.assertEqual(operation["prior_distinctness_operation_outcome_required"], resolver.PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(operation["prior_distinctness_result_required"], resolver.PRIOR_DISTINCTNESS_RESULT_REQUIRED)
        self.assertIs(operation["prior_distinctness_supported_required"], False)
        self.assertEqual(operation["upstream_basis_emission_successor_operation_type"], resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_TYPE)
        self.assertEqual(operation["upstream_basis_emission_successor_operation_outcome_required"], resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(operation["upstream_basis_emission_successor_result_required"], resolver.UPSTREAM_BASIS_EMISSION_SUCCESSOR_RESULT_REQUIRED)
        self.assertEqual(operation["upstream_candidate_a_basis_id_required"], resolver.UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED)
        self.assertEqual(operation["upstream_candidate_b_basis_id_required"], resolver.UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED)
        self.assertEqual(operation["upstream_candidate_a_basis_label_required"], resolver.UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED)
        self.assertEqual(operation["upstream_candidate_b_basis_label_required"], resolver.UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED)
        self.assertEqual(operation["upstream_basis_pair_scope_required"], resolver.UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED)
        self.assertEqual(result["recheck_result_detail"]["missing_or_insufficient_basis_emission_material"], [])
        self.assertEqual(result["recheck_result_detail"]["not_supported_reasons"], [])
        self.assertTrue(all(value is True for key, value in operation.items() if key.endswith("markers_present")))

        material = result["distinctness_support_recheck_material"]
        self.assertEqual(set(material), {
            "candidate_a_basis_reference", "candidate_b_basis_reference", "basis_pair_reference", "support_evaluation",
        })
        candidate_a = material["candidate_a_basis_reference"]
        self.assertEqual(candidate_a, {
            "basis_id": resolver.UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED,
            "candidate_record_id": "descendant_body_basis_candidate_a_001",
            "candidate_role": "CANDIDATE_A",
            "basis_label": resolver.UPSTREAM_CANDIDATE_A_BASIS_LABEL_REQUIRED,
            "source_scope": "Motion-side admissible variation",
            "source_mandate": "Motion mandate",
            "non_standing_basis": True,
            "distinctness_supported_at_emission_time": False,
        })
        candidate_b = material["candidate_b_basis_reference"]
        self.assertEqual(candidate_b, {
            "basis_id": resolver.UPSTREAM_CANDIDATE_B_BASIS_ID_REQUIRED,
            "candidate_record_id": "descendant_body_basis_candidate_b_001",
            "candidate_role": "CANDIDATE_B",
            "basis_label": resolver.UPSTREAM_CANDIDATE_B_BASIS_LABEL_REQUIRED,
            "source_scope": "Regulation-side admissibility bounds",
            "source_mandate": "Regulation mandate",
            "non_standing_basis": True,
            "distinctness_supported_at_emission_time": False,
        })
        pair = material["basis_pair_reference"]
        for field in (
            "candidate_a_and_b_are_sibling_non_standing_basis_materials",
            "neither_candidate_ranks_above_the_other",
            "regulation_not_sovereign_over_motion",
            "motion_does_not_erase_regulation",
        ):
            self.assertIs(pair[field], True)
        self.assertEqual(pair["basis_pair_scope"], resolver.UPSTREAM_BASIS_PAIR_SCOPE_REQUIRED)
        for field in (
            "coupling_assigned", "coupling_created", "third_candidate_created", "third_model_admitted", "candidate_standing_authorized",
        ):
            self.assertIs(pair[field], False)
        evaluation = material["support_evaluation"]
        self.assertEqual(evaluation["prior_distinctness_result"], "NOT_DISTINCT")
        self.assertIs(evaluation["prior_distinctness_supported"], False)
        self.assertIn("candidate-specific content and separate seal, receipt, and digest material were absent", evaluation["prior_absence_reason"])
        for field in (
            "candidate_specific_basis_material_present", "candidate_specific_basis_material_separate",
            "candidate_specific_basis_material_non_standing", "basis_pair_non_hierarchy_preserved",
            "candidate_records_marked_distinct", "candidate_records_distinct",
        ):
            self.assertIs(evaluation[field], True)
        self.assertEqual(evaluation["distinctness_support_result"], "DISTINCTNESS_SUPPORTED")
        for field in (
            "candidate_standing_authorized", "descendant_body_created", "relation_created", "coupling_created",
            "presence_established", "identity_created",
        ):
            self.assertIs(evaluation[field], False)

    def test_default_live_repo_target_records_supported_when_present(self) -> None:
        required = [REPO_ROOT / resolver.DEFAULT_OPERATION_SPEC_REFERENCE]
        required.extend(REPO_ROOT / default for _, default, *_ in resolver.UPSTREAM_REQUIREMENTS)
        if not all(path.is_file() for path in required):
            self.skipTest("default recheck target or upstream terminal summaries are not present")
        result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min()
        self.assert_supported_shape(result)
        material = result["distinctness_support_recheck_material"]
        self.assertEqual(set(material), {
            "candidate_a_basis_reference", "candidate_b_basis_reference", "basis_pair_reference", "support_evaluation",
        })

    def test_missing_or_non_supporting_basis_emission_is_contained(self) -> None:
        cases = (
            ("missing_emission_flag", "candidate_a_basis_material_emitted = true", "candidate_a_basis_material_emitted = false"),
            ("missing_candidate_a_id", resolver.UPSTREAM_CANDIDATE_A_BASIS_ID_REQUIRED, "wrong_candidate_a_basis"),
            ("missing_pair_scope", "basis_pair_scope = SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY", "basis_pair_scope = WRONG"),
            ("not_sibling", "candidate_a_and_b_are_sibling_non_standing_basis_materials = true", "candidate_a_and_b_are_sibling_non_standing_basis_materials = false"),
            ("hierarchy", "neither_candidate_ranks_above_the_other = true", "neither_candidate_ranks_above_the_other = false"),
            ("sovereignty", "regulation_not_sovereign_over_motion = true", "regulation_not_sovereign_over_motion = false"),
            ("coupling", "coupling_created = false", "coupling_created = true"),
            ("premature_distinct", "candidate_records_marked_distinct = false", "candidate_records_marked_distinct = true"),
            ("standing", "candidate_standing_authorized = false", "candidate_standing_authorized = true"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, (name, old, new) in enumerate(cases):
                with self.subTest(name=name):
                    case_directory = root / f"{index:03d}_{name}"
                    request, paths = self.build_valid_request(case_directory)
                    path = paths["successor_basis_emission_terminal_summary_reference"]
                    path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(request)
                    self.assertIn(result["outcome"], (
                        resolver.OUTCOME_REQUIRES_BASIS_EMISSION,
                        resolver.OUTCOME_NOT_SUPPORTED,
                        resolver.OUTCOME_BLOCKED,
                    ))
                    if result["outcome"] == resolver.OUTCOME_REQUIRES_BASIS_EMISSION:
                        self.assert_requires_basis_not_blocked(result)
                        self.assertTrue(result["recheck_result_detail"]["missing_or_insufficient_basis_emission_material"])
                    elif result["outcome"] == resolver.OUTCOME_NOT_SUPPORTED:
                        self.assert_not_supported_not_blocked(result)
                        self.assertTrue(result["recheck_result_detail"]["not_supported_reasons"])
                    else:
                        self.assert_blocked_public(result)
                    operation = self.operation(result)
                    self.assertIs(operation["distinctness_supported_recorded"], False)
                    self.assertIs(operation["candidate_records_marked_distinct"], False)
                    self.assertIs(operation["candidate_records_distinct"], False)
                    self.assert_canonical_non_claims(result)
                    self.assert_no_downstream_conversion(result)

    def test_missing_prior_distinctness_and_marker_classes_are_contained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            prior_cases = (
                ("prior_missing", resolver.PRIOR_DISTINCTNESS_OPERATION_OUTCOME_REQUIRED, "NOT_A_PRIOR_OUTCOME"),
                ("prior_result", "distinctness_result = NOT_DISTINCT", "distinctness_result = WRONG"),
                ("prior_support", "distinctness_supported = false", "distinctness_supported = true"),
                ("prior_count", "candidate records with distinct ids and roles", "candidate records without a valid comparison"),
            )
            for index, (name, old, new) in enumerate(prior_cases):
                with self.subTest(name=name):
                    request, paths = self.build_valid_request(root / f"prior_{index:03d}")
                    path = paths["prior_distinctness_operation_terminal_summary_reference"]
                    text = path.read_text(encoding="utf-8").replace(old, new, 1)
                    if name == "prior_count":
                        text = text.replace("compared exactly two candidate records", "compared no candidate records", 1)
                    path.write_text(text, encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_BASIS_EMISSION, resolver.OUTCOME_BLOCKED))
                    self.assert_canonical_non_claims(result)
                    self.assert_no_downstream_conversion(result)

            marker_fields = (
                "operation_spec_reference",
                "prior_distinctness_operation_terminal_summary_reference",
                "successor_basis_emission_terminal_summary_reference",
                "existence_claim_evidence_check_terminal_summary_reference",
                "basis_emission_operation_terminal_summary_reference",
                "successor_closure_operation_terminal_summary_reference",
                "scope_division_operation_terminal_summary_reference",
            )
            for index, field in enumerate(marker_fields):
                with self.subTest(marker_field=field):
                    request, paths = self.build_valid_request(root / f"marker_{index:03d}")
                    paths[field].write_text("marker class absent\n", encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_BASIS_EMISSION, resolver.OUTCOME_BLOCKED))
                    self.assert_canonical_non_claims(result)
                    self.assert_no_downstream_conversion(result)
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_public(result)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_request(Path(temporary))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(result["block"]["blocked"], False)
            operation = self.operation(result)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[field], False, field)
            self.assert_canonical_non_claims(result)
            self.assert_no_downstream_conversion(result)

            explicit_block = copy.deepcopy(request)
            explicit_block["intent"] = resolver.INTENT_BLOCK
            blocked = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(explicit_block)
            self.assert_blocked_public(blocked)
            self.assertEqual(self.block_code(blocked), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_exact_values_and_prohibited_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_request(Path(temporary))
            self.assert_blocked_public(
                resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min([request])
            )
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED"
            self.assert_blocked_public(
                resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(unsupported)
            )
            exact_cases = (
                ("operation_id", "wrong"),
                ("operation_type", "wrong"),
                ("operation_version", "9.9.9"),
                ("operation_scope", "wrong"),
                ("prior_distinctness_operation_type", "wrong"),
                ("prior_distinctness_operation_outcome_required", "wrong"),
                ("prior_distinctness_result_required", "wrong"),
                ("prior_distinctness_supported_required", True),
                ("upstream_basis_emission_successor_operation_type", "wrong"),
                ("upstream_basis_emission_successor_operation_outcome_required", "wrong"),
                ("upstream_basis_emission_successor_result_required", "wrong"),
                ("upstream_candidate_specific_content_emitted_required", False),
                ("upstream_candidate_a_basis_id_required", "wrong"),
                ("upstream_candidate_b_basis_id_required", "wrong"),
                ("upstream_candidate_a_basis_label_required", "wrong"),
                ("upstream_candidate_b_basis_label_required", "wrong"),
                ("upstream_basis_pair_scope_required", "wrong"),
                ("upstream_candidate_standing_authorized_required", True),
                ("admissible_future_route", "wrong"),
            )
            for field, value in exact_cases:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = value
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(malformed)
                    self.assert_blocked_public(result)

            for flag in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(prohibited_flag=flag):
                    prohibited = copy.deepcopy(request)
                    prohibited[flag] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(prohibited)
                    self.assert_blocked_public(result)

    def test_non_claim_and_result_posture_preclaims_block_and_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_non_claim=key):
                    malformed = copy.deepcopy(request)
                    malformed[key] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(malformed)
                    self.assert_blocked_public(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(result_posture=key):
                    malformed = copy.deepcopy(request)
                    malformed[key] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(malformed)
                    self.assert_blocked_public(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
            for field, value in (
                ("distinctness_support_recheck_result", "DISTINCTNESS_SUPPORT_RECHECKED"),
                ("distinctness_support_result", "DISTINCTNESS_SUPPORTED"),
            ):
                with self.subTest(result_value=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = value
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(malformed)
                    self.assert_blocked_public(result)

            declared_cases: list[tuple[str, object]] = [
                ("missing", None),
                ("non_mapping", []),
                ("non_bool", {**request["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}),
            ]
            missing_key = dict(request["declared_non_claims"])
            missing_key.pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            declared_cases.append(("missing_key", missing_key))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                declared = dict(request["declared_non_claims"])
                declared[key] = True
                declared_cases.append((f"flipped_{key}", declared))
            for name, declared in declared_cases:
                with self.subTest(declared_non_claims=name):
                    malformed = copy.deepcopy(request)
                    if name == "missing":
                        malformed.pop("declared_non_claims")
                    else:
                        malformed["declared_non_claims"] = declared
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min(malformed)
                    self.assert_blocked_public(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_path_write_summary_smoke_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request, paths = self.build_valid_request(root / "basis")
            request["hostile_payload"] = {"raw_body": "HOSTILE_BODY_MUST_NOT_RETURN"}
            request_before = copy.deepcopy(request)
            source_texts = {field: path.read_text(encoding="utf-8") for field, path in paths.items()}
            request_path = self.write_json(root, "declared_request", request)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path(request_path)
            self.assert_supported_shape(result)
            self.assertEqual(request, request_before)
            self.assertNotIn("HOSTILE_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))
            for field, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), source_texts[field], field)
            summary = resolver.build_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_SUPPORTED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["distinctness_support_recheck_result"], "DISTINCTNESS_SUPPORT_RECHECKED")
            self.assertEqual(summary["distinctness_support_result"], "DISTINCTNESS_SUPPORTED")
            self.assertIs(summary["distinctness_supported_recorded"], True)
            self.assertIs(summary["candidate_records_marked_distinct"], True)
            self.assertIs(summary["candidate_records_distinct"], True)
            self.assertEqual(summary["missing_or_insufficient_basis_emission_material"], [])
            self.assertEqual(summary["not_supported_reasons"], [])
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIs(summary[key], False, key)

            malformed_path = root / self.safe_json_filename("malformed request")
            malformed_path.write_text("{not JSON", encoding="utf-8")
            self.assert_blocked_public(
                resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path(malformed_path)
            )
            array_path = root / self.safe_json_filename("array request")
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked_public(
                resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path(array_path)
            )
            self.assert_blocked_public(
                resolver.resolve_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_from_path(root / "missing.json")
            )

            output = root / "output" / "distinctness_support_recheck_operation_v0_min_result.json"
            first = resolver.write_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_result(result, output)
            second = resolver.write_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_SUPPORTED)
            self.assertIn("distinctness_support_recheck_operation_v0_min_result", first.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_support_recheck_operation_v0_min", str(resolver.OUTPUT_ROOT))
            for forbidden_root in (
                "basis_emission_successor", "successor_closure", "receipt", "audit", "digest", "boundary",
                "prior_distinctness", "runtime", "daemon", "api", "field", "presence", "identity", "externalization",
            ):
                self.assertNotIn(forbidden_root, str(first.parent).casefold())


if __name__ == "__main__":
    unittest.main()
