"""Tests for one bounded descendant-body candidate-standing operation.

The operation can support Candidate A and Candidate B standing only after the
declared boundary allowance.  These tests keep that support separate from
descendant-body creation, relation, coupling, presence, identity, and all
downstream authorization.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_descendant_body_candidate_standing_operation_v0_min as resolver


class DescendantBodyCandidateStandingOperationV0MinTests(unittest.TestCase):
    """Exercise one candidate-standing operation without downstream conversion."""

    REFERENCE_FILENAMES = {
        "candidate_standing_operation_spec_reference": "candidate_standing_operation_spec.md",
        "candidate_standing_boundary_terminal_summary_reference": "candidate_standing_boundary_summary.md",
        "distinctness_support_recheck_terminal_summary_reference": "distinctness_support_summary.md",
        "successor_basis_emission_terminal_summary_reference": "successor_basis_summary.md",
        "existence_claim_evidence_check_terminal_summary_reference": "existence_claim_summary.md",
        "prior_distinctness_operation_terminal_summary_reference": "prior_distinctness_summary.md",
        "successor_closure_operation_terminal_summary_reference": "successor_closure_summary.md",
        "scope_division_operation_terminal_summary_reference": "scope_division_summary.md",
    }

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        """Return a stable local filename for a generated subtest case."""

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

    def _write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic JSON path is a directory: {path}")
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _operation_spec_text(self) -> str:
        return "\n".join(
            (
                "# Descendant Body Candidate Standing Operation V0 Minimum Specification",
                "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
                "descendant_body_candidate_standing_operation_001",
                "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY",
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
                "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
                "candidate_standing_operation_consideration_allowed = true",
                "supported_distinctness_referenced = true",
                "candidate_records_distinct_referenced = true",
                "candidate_standing_check_performed = false",
                "candidate_standing_authorized = false",
                "candidate_standing_created = false",
                "descendant_body_created = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
                "DISTINCTNESS_SUPPORTED",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "candidate records marked distinct are not standing candidates",
                "separate non-standing Candidate A and Candidate B basis material",
                "basis-pair non-hierarchy",
                resolver.CANDIDATE_A_BASIS_ID,
                resolver.CANDIDATE_B_BASIS_ID,
                resolver.CANDIDATE_A_BASIS_LABEL,
                resolver.CANDIDATE_B_BASIS_LABEL,
                resolver.BASIS_PAIR_SCOPE,
                resolver.CANDIDATE_A_RECORD_ID,
                resolver.CANDIDATE_B_RECORD_ID,
                resolver.CANDIDATE_A_ROLE,
                resolver.CANDIDATE_B_ROLE,
                "Motion-side admissible variation",
                "Regulation-side admissibility bounds",
                "candidate_a_standing_evaluation",
                "candidate_b_standing_evaluation",
                "standing_pair_evaluation",
                "candidate_standing_supported = true",
                "candidate_standing_authorized = true",
                "candidate_standing_created = true",
                "Candidate standing is not descendant-body creation",
                "Candidate standing is not crossing",
                "Candidate standing is not relation",
                "Candidate standing is not runtime",
                "Candidate standing is not currentness",
                "Candidate standing is not authority",
                "Candidate standing is not coupling",
                "Candidate standing is not presence",
                "Candidate standing is not identity",
                "Candidate standing is not follow-on authorization",
                "Candidate standing is not standing descendant",
                "Candidate standing is not descendant body",
                "Candidate standing is not relation participation",
                "Candidate standing is not presence-bearing",
                "Candidate standing is not identity-bearing",
                "Candidate A and Candidate B remain sibling candidate records",
                "Neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "Coupling remains unassigned",
                resolver.ADMISSIBLE_FUTURE_ROUTE,
                "Only after a future candidate-standing operation records CANDIDATE_STANDING_SUPPORTED may a separately bounded descendant-body creation boundary be considered",
                "No later operation is authorized by this specification alone",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct candidate-standing operation spec to candidate-standing operation completion",
                "direct boundary allowance to candidate standing without operation",
                "direct supported distinctness to candidate standing without boundary and operation",
                "direct candidate standing to descendant-body creation",
                "direct candidate standing to crossing",
                "direct candidate standing to relation",
                "direct candidate standing to runtime",
                "direct candidate standing to authority/currentness",
                "direct candidate standing to coupling creation",
                "direct candidate standing to third-candidate route",
                "direct candidate standing to third-model route",
                "direct candidate standing to presence",
                "direct candidate standing to identity",
                "direct candidate standing to follow-on work",
                "direct candidate standing to standing descendant",
                "direct candidate standing to descendant standing",
                "direct candidate standing to output/action",
                "repository scan route",
                "file discovery route",
                "affected-file repair route",
                "prior unsupported-claim validation route",
                "This operation spec defines only a future candidate-standing operation shape",
                "It does not perform candidate-standing checks",
                "Candidate-standing operation spec is not candidate-standing operation result",
                "Candidate-standing operation permission is not candidate-standing completion",
                "Candidate standing, if later supported, remains prior to any descendant-body creation boundary",
                "Open means not scheduled, not authorized, and not executed",
            )
        )

    def _boundary_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
                "failed_check_count = 0",
                "passed_check_count = 170",
                "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
                "candidate_standing_operation_consideration_allowed = true",
                "supported_distinctness_referenced = true",
                "candidate_records_distinct_referenced = true",
                "candidate_standing_check_performed = false",
                "candidate_standing_authorized = false",
                "candidate_standing_created = false",
                "descendant_body_created = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            )
        )

    def _distinctness_support_text(self) -> str:
        return "\n".join(
            (
                "DISTINCTNESS_SUPPORTED",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "candidate records marked distinct are not standing candidates",
                "candidate_standing_authorized = false",
                "descendant_body_created = false",
                "relation_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            )
        )

    def _successor_basis_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED",
                "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
                "Separate non-standing Candidate A and Candidate B basis material",
                "basis-pair non-hierarchy",
                resolver.CANDIDATE_A_BASIS_ID,
                resolver.CANDIDATE_B_BASIS_ID,
                resolver.CANDIDATE_A_BASIS_LABEL,
                resolver.CANDIDATE_B_BASIS_LABEL,
                resolver.BASIS_PAIR_SCOPE,
            )
        )

    def _existence_claim_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        )

    def _prior_distinctness_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT\n"

    def _successor_closure_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED\n"

    def _scope_division_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS\n"

    def _fixture_texts(self) -> dict[str, str]:
        return {
            "candidate_standing_operation_spec_reference": self._operation_spec_text(),
            "candidate_standing_boundary_terminal_summary_reference": self._boundary_summary_text(),
            "distinctness_support_recheck_terminal_summary_reference": self._distinctness_support_text(),
            "successor_basis_emission_terminal_summary_reference": self._successor_basis_text(),
            "existence_claim_evidence_check_terminal_summary_reference": self._existence_claim_text(),
            "prior_distinctness_operation_terminal_summary_reference": self._prior_distinctness_text(),
            "successor_closure_operation_terminal_summary_reference": self._successor_closure_text(),
            "scope_division_operation_terminal_summary_reference": self._scope_division_text(),
        }

    def _build_valid_request(
        self, root: Path, text_overrides: dict[str, str] | None = None
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, str]]:
        texts = self._fixture_texts()
        if text_overrides:
            texts.update(text_overrides)
        paths: dict[str, Path] = {}
        for field, filename in self.REFERENCE_FILENAMES.items():
            path = root / "synthetic_basis" / filename
            self._write_markdown(path, texts[field])
            paths[field] = path
        request = resolver.build_declared_descendant_body_candidate_standing_operation_v0_min_request(
            **{field: str(path) for field, path in paths.items()}
        )
        return request, paths, texts

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("candidate_standing_operation_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is False for check in checks)

    def passed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("candidate_standing_operation_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is True for check in checks)

    def operation(self, result: dict[str, Any]) -> dict[str, Any]:
        operation = result.get("descendant_body_candidate_standing_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def material(self, result: dict[str, Any]) -> dict[str, Any]:
        material = result.get("candidate_standing_operation_material")
        self.assertIsInstance(material, dict)
        return material

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_supported(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_SUPPORTED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_requires_boundary_allowance(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)
        self.assert_not_blocked(result)
        self.assertEqual(self.operation(result).get("candidate_standing_result"), "REQUIRES_BOUNDARY_ALLOWANCE")
        self.assertFalse(self.operation(result).get("candidate_standing_authorized"))
        self.assertFalse(self.operation(result).get("candidate_standing_created"))

    def assert_not_supported(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_SUPPORTED)
        self.assert_not_blocked(result)
        self.assertEqual(self.operation(result).get("candidate_standing_result"), "CANDIDATE_STANDING_NOT_SUPPORTED")
        self.assertFalse(self.operation(result).get("candidate_standing_authorized"))
        self.assertFalse(self.operation(result).get("candidate_standing_created"))

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("candidate_standing_operation_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, dict):
                continue
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_downstream_posture(result)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_downstream_posture(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation.get(key), False, key)

    def assert_all_marker_flags_true(self, result: dict[str, Any]) -> None:
        checks = result.get("candidate_standing_operation_checks")
        self.assertIsInstance(checks, list)
        marker_checks = [
            check for check in checks
            if isinstance(check, dict)
            and isinstance(check.get("check_name"), str)
            and check["check_name"].endswith("markers present")
        ]
        self.assertTrue(marker_checks)
        for check in marker_checks:
            self.assertIs(check.get("passed"), True, check.get("check_name"))

    def assert_operation_separate_from_wrapper(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        for key in (
            "outcome",
            "block",
            "candidate_standing_operation_checks",
            "candidate_standing_operation_summary",
            "candidate_standing_operation_metadata",
            "candidate_standing_operation_material",
            "non_claims",
        ):
            self.assertNotIn(key, operation)

    def assert_bounded_non_supported_result(self, result: dict[str, Any]) -> None:
        self.assertIn(
            result.get("outcome"),
            {
                resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                resolver.OUTCOME_NOT_SUPPORTED,
                resolver.OUTCOME_BLOCKED,
            },
        )
        if result.get("outcome") == resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
            self.assert_requires_boundary_allowance(result)
            detail = result.get("candidate_standing_result_detail", {})
            self.assertTrue(detail.get("missing_or_insufficient_boundary_allowance"))
        elif result.get("outcome") == resolver.OUTCOME_NOT_SUPPORTED:
            self.assert_not_supported(result)
            detail = result.get("candidate_standing_result_detail", {})
            self.assertTrue(detail.get("not_supported_reasons"))
        else:
            self.assert_blocked_with_public_code(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_downstream_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_standing_operation_v0_min",
            "resolve_descendant_body_candidate_standing_operation_v0_min_from_path",
            "write_descendant_body_candidate_standing_operation_v0_min_result",
            "build_descendant_body_candidate_standing_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_standing_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_descendant_body_candidate_standing_operation_v0_min",
            "OPERATION_ID": "descendant_body_candidate_standing_operation_001",
            "OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_CANDIDATE_STANDING_BOUNDARY_TYPE": "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY",
            "PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED": "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
            "PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED": "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY",
            "CANDIDATE_A_RECORD_ID": "descendant_body_basis_candidate_a_001",
            "CANDIDATE_B_RECORD_ID": "descendant_body_basis_candidate_b_001",
            "CANDIDATE_A_BASIS_ID": "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
            "CANDIDATE_B_BASIS_ID": "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
            "CANDIDATE_A_ROLE": "CANDIDATE_A",
            "CANDIDATE_B_ROLE": "CANDIDATE_B",
            "CANDIDATE_A_BASIS_LABEL": "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS",
            "CANDIDATE_B_BASIS_LABEL": "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS",
            "BASIS_PAIR_SCOPE": "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_SUPPORTED_DISTINCTNESS_REFERENCED_REQUIRED",
            "PRIOR_CANDIDATE_RECORDS_DISTINCT_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_CANDIDATE_STANDING_CHECK_PERFORMED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertTrue(set(resolver.OUTCOME_FAMILY).issuperset({
            resolver.OUTCOME_SUPPORTED,
            resolver.OUTCOME_NOT_SUPPORTED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        }))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_operation_v0_min"
        ))
        self.assertTrue(set(resolver.BLOCK_CODES))
        self.assertTrue(set(resolver.ALLOWED_TRUE_RECORDED_FIELDS))
        self.assertTrue(set(resolver.REQUIRED_FALSE_NON_CLAIMS))

    def test_synthetic_supported_result_and_operation_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
        self.assert_supported(result)
        self.assertEqual(result.get("result_version"), "0.1.0")
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        for key in (
            "candidate_standing_operation_metadata",
            "declared_candidate_standing_operation_basis",
            "upstream_basis",
            "descendant_body_candidate_standing_operation",
            "candidate_standing_operation_material",
            "candidate_standing_operation_checks",
            "candidate_standing_operation_statement",
            "candidate_standing_operation_non_meaning",
            "candidate_standing_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "candidate_standing_operation_summary",
        ):
            self.assertIn(key, result)
        operation = self.operation(result)
        self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["prior_candidate_standing_boundary_type"], resolver.PRIOR_CANDIDATE_STANDING_BOUNDARY_TYPE)
        self.assertEqual(operation["prior_candidate_standing_boundary_outcome_required"], resolver.PRIOR_CANDIDATE_STANDING_BOUNDARY_OUTCOME_REQUIRED)
        self.assertEqual(operation["prior_candidate_standing_boundary_result_required"], resolver.PRIOR_CANDIDATE_STANDING_BOUNDARY_RESULT_REQUIRED)
        self.assertIs(operation["prior_candidate_standing_operation_consideration_allowed_required"], True)
        for key, expected in (
            ("candidate_a_record_id", resolver.CANDIDATE_A_RECORD_ID),
            ("candidate_b_record_id", resolver.CANDIDATE_B_RECORD_ID),
            ("candidate_a_role", resolver.CANDIDATE_A_ROLE),
            ("candidate_b_role", resolver.CANDIDATE_B_ROLE),
            ("candidate_a_basis_id", resolver.CANDIDATE_A_BASIS_ID),
            ("candidate_b_basis_id", resolver.CANDIDATE_B_BASIS_ID),
            ("candidate_a_basis_label", resolver.CANDIDATE_A_BASIS_LABEL),
            ("candidate_b_basis_label", resolver.CANDIDATE_B_BASIS_LABEL),
            ("basis_pair_scope", resolver.BASIS_PAIR_SCOPE),
        ):
            self.assertEqual(operation[key], expected)
        self.assertEqual(operation["candidate_standing_result"], "CANDIDATE_STANDING_SUPPORTED")
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[key], True, key)
        self.assert_no_downstream_posture(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)
        self.assert_operation_separate_from_wrapper(result)
        detail = result["candidate_standing_result_detail"]
        self.assertEqual(detail["missing_or_insufficient_boundary_allowance"], [])
        self.assertEqual(detail["not_supported_reasons"], [])

    def test_synthetic_supported_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
        self.assert_supported(result)
        material = self.material(result)
        self.assertEqual(set(material), {
            "candidate_a_standing_evaluation",
            "candidate_b_standing_evaluation",
            "standing_pair_evaluation",
        })
        for prefix, record, role, basis, label, scope in (
            ("candidate_a", resolver.CANDIDATE_A_RECORD_ID, resolver.CANDIDATE_A_ROLE, resolver.CANDIDATE_A_BASIS_ID, resolver.CANDIDATE_A_BASIS_LABEL, "Motion-side admissible variation"),
            ("candidate_b", resolver.CANDIDATE_B_RECORD_ID, resolver.CANDIDATE_B_ROLE, resolver.CANDIDATE_B_BASIS_ID, resolver.CANDIDATE_B_BASIS_LABEL, "Regulation-side admissibility bounds"),
        ):
            evaluation = material[f"{prefix}_standing_evaluation"]
            self.assertEqual(evaluation["candidate_record_id"], record)
            self.assertEqual(evaluation["candidate_role"], role)
            self.assertEqual(evaluation["candidate_basis_id"], basis)
            self.assertEqual(evaluation["candidate_basis_label"], label)
            self.assertEqual(evaluation["candidate_basis_scope"], scope)
            for key in (
                "candidate_record_distinct",
                "candidate_basis_separate",
                "candidate_basis_non_standing_at_emission",
                "candidate_standing_supported",
                "candidate_standing_authorized",
                "candidate_standing_created",
            ):
                self.assertIs(evaluation[key], True, f"{prefix}.{key}")
            for key in ("descendant_body_created", "relation_created", "presence_established", "identity_created"):
                self.assertIs(evaluation[key], False, f"{prefix}.{key}")
        pair = material["standing_pair_evaluation"]
        for key in (
            "both_candidate_standings_supported",
            "both_candidate_standings_authorized",
            "both_candidate_standings_created",
            "candidate_records_remain_sibling",
            "candidate_record_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
            "regulation_not_sovereign_over_motion",
            "motion_does_not_erase_regulation",
        ):
            self.assertIs(pair[key], True, key)
        for key in (
            "coupling_assigned",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "descendant_body_created",
            "relation_created",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
        ):
            self.assertIs(pair[key], False, key)

    def test_default_live_target_is_supported_when_all_references_exist(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_standing_operation_v0_min_request()
        reference_paths = [
            REPOSITORY_ROOT / value
            for key, value in request.items()
            if key.endswith("_reference") and isinstance(value, str)
        ]
        if not all(path.is_file() for path in reference_paths):
            self.skipTest("default candidate-standing references are not all present")
        result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
        self.assert_supported(result)
        operation = self.operation(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[key], True, key)
        self.assert_no_downstream_posture(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)

    def test_missing_boundary_allowance_and_insufficient_support_are_bounded(self) -> None:
        boundary_markers = (
            "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
            "candidate_standing_operation_consideration_allowed",
            "candidate_standing_operation_consideration_allowed = true",
            "supported_distinctness_referenced = true",
            "candidate_records_distinct_referenced = true",
            "candidate_standing_check_performed = false",
            "candidate_standing_authorized = false",
            "candidate_standing_created = false",
            "descendant_body_created = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        )
        support_markers = (
            "DISTINCTNESS_SUPPORTED",
            "candidate_records_marked_distinct = true",
            "candidate_records_distinct = true",
            "candidate records marked distinct are not standing candidates",
        )
        basis_markers = (
            "Separate non-standing Candidate A and Candidate B basis material",
            "basis-pair non-hierarchy",
            resolver.CANDIDATE_A_BASIS_ID,
            resolver.CANDIDATE_B_BASIS_ID,
        )
        variants: list[tuple[str, str, str]] = []
        variants.extend(("candidate_standing_boundary_terminal_summary_reference", marker, "requires") for marker in boundary_markers)
        variants.extend(("distinctness_support_recheck_terminal_summary_reference", marker, "requires") for marker in support_markers)
        variants.extend(("successor_basis_emission_terminal_summary_reference", marker, "requires") for marker in basis_markers)
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker, expected) in enumerate(variants):
                with self.subTest(field=field, marker=marker):
                    request, paths, texts = self._build_valid_request(root / f"variant_{index:03d}")
                    self._write_markdown(paths[field], texts[field].replace(marker, "[removed marker]"))
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
                    self.assert_bounded_non_supported_result(result)
                    if expected == "requires":
                        self.assert_requires_boundary_allowance(result)
            for index, field in enumerate(self.REFERENCE_FILENAMES, start=len(variants)):
                with self.subTest(missing_reference=field):
                    request, _, _ = self._build_valid_request(root / f"missing_{index:03d}")
                    request[field] = str(root / "unavailable" / self.safe_json_filename(field, index))
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
                    self.assert_bounded_non_supported_result(result)
            request, _, _ = self._build_valid_request(root / "insufficient")
            request["candidate_standing_support_evidence_sufficient"] = False
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
            self.assert_not_supported(result)
            self.assertTrue(result["candidate_standing_result_detail"]["not_supported_reasons"])
            self.assert_canonical_false_non_claims(result)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            operation = self.operation(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[key], False, key)
            self.assert_no_downstream_posture(result)
            self.assert_canonical_false_non_claims(result)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            blocked_result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(blocked)
        self.assert_blocked_with_public_code(blocked_result)
        self.assertEqual(self.block_code(blocked_result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_exact_fields_block(self) -> None:
        self.assert_blocked_with_public_code(
            resolver.resolve_descendant_body_candidate_standing_operation_v0_min(["not", "a", "mapping"])
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            request, _, _ = self._build_valid_request(root)
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_INTENT"
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_standing_operation_v0_min(unsupported)
            )
            for index, (field, expected) in enumerate(resolver.EXPECTED_REQUEST_VALUES.items()):
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = not expected if isinstance(expected, bool) else f"not_{expected}"
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
            for field in (
                "operation_id",
                "operation_type",
                "operation_version",
                "operation_scope",
                "prior_candidate_standing_boundary_type",
                "prior_candidate_standing_boundary_outcome_required",
                "prior_candidate_standing_boundary_result_required",
                "candidate_a_record_id",
                "candidate_b_record_id",
                "candidate_a_role",
                "candidate_b_role",
                "candidate_a_basis_id",
                "candidate_b_basis_id",
                "candidate_a_basis_label",
                "candidate_b_basis_label",
                "basis_pair_scope",
                "admissible_future_route",
            ):
                self.assertIn(field, resolver.EXPECTED_REQUEST_VALUES)

    def test_marker_class_validation(self) -> None:
        mutations: tuple[tuple[str, str], ...] = (
            ("candidate_standing_operation_spec_reference", resolver.OPERATION_ID),
            ("candidate_standing_boundary_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED"),
            ("distinctness_support_recheck_terminal_summary_reference", "DISTINCTNESS_SUPPORTED"),
            ("successor_basis_emission_terminal_summary_reference", "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED"),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            ("prior_distinctness_operation_terminal_summary_reference", "NOT_DISTINCT"),
            ("successor_closure_operation_terminal_summary_reference", "CLOSED"),
            ("scope_division_operation_terminal_summary_reference", "REQUIRES_ADDITIONAL_BASIS"),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker) in enumerate(mutations):
                with self.subTest(field=field):
                    request, paths, texts = self._build_valid_request(root / f"markers_{index:03d}")
                    self._write_markdown(paths[field], texts[field].replace(marker, "[removed marker]"))
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
                    self.assert_bounded_non_supported_result(result)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            required_flags = {
                "request_descendant_body_a_creation",
                "request_descendant_body_b_creation",
                "request_descendant_body_creation",
                "request_standing_authorization",
                "request_standing_descendant_creation",
                "request_descendant_standing_check",
                "request_crossing_authorization",
                "request_first_crossing_authorization",
                "request_relation_creation",
                "request_field_machinery_creation",
                "request_runtime_creation",
                "request_api_creation",
                "request_currentness_creation",
                "request_authority_creation",
                "request_standing_creation",
                "request_output_authorization",
                "request_action_authorization",
                "request_derivative_reception_authorization",
                "request_synchronization_authorization",
                "request_coupling_assignment_to_candidate_a",
                "request_coupling_assignment_to_candidate_b",
                "request_coupling_creation",
                "request_third_candidate_creation",
                "request_third_model_admission",
                "request_presence_establishment",
                "request_identity_creation",
                "request_follow_on_authorization",
                "request_repository_scan",
                "request_file_discovery",
                "request_affected_file_repair",
                "request_affected_file_mutation",
                "request_prior_unsupported_claim_validation",
                "request_validation_enforcement",
            }
            self.assertTrue(required_flags.issubset(resolver.PROHIBITED_REQUEST_FLAGS))
            for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(field=field):
                    prohibited = copy.deepcopy(request)
                    prohibited[field] = True
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(prohibited)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_false_posture_preclaims_and_non_claims_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed[key] = True
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                with self.subTest(declared_non_claim=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(result_posture_preclaimed=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed[key] = True
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
            preclaimed_result = copy.deepcopy(request)
            preclaimed_result["candidate_standing_result"] = "CANDIDATE_STANDING_SUPPORTED"
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(preclaimed_result)
            self.assert_blocked_with_public_code(result)
            self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
            for label, declared_non_claims in (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_boolean", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            ):
                with self.subTest(declared_non_claims=label):
                    malformed = copy.deepcopy(request)
                    if declared_non_claims is None:
                        malformed.pop("declared_non_claims")
                    else:
                        malformed["declared_non_claims"] = declared_non_claims
                    result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_path_write_and_non_mutation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            request, paths, texts = self._build_valid_request(root)
            original_request = copy.deepcopy(request)
            original_texts = copy.deepcopy(texts)
            original_paths = copy.deepcopy(paths)
            request["raw_payload"] = "RAW_CANDIDATE_STANDING_BODY_MUST_NOT_RETURN"
            request_path = self._write_json(root / "requests" / "valid.json", request)
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min_from_path(request_path)
            self.assert_supported(result)
            self.assertNotIn("RAW_CANDIDATE_STANDING_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))
            output_path = root / "output" / "candidate_standing_operation_v0_min_result.json"
            first_path = resolver.write_descendant_body_candidate_standing_operation_v0_min_result(result, output_path)
            second_path = resolver.write_descendant_body_candidate_standing_operation_v0_min_result(result, output_path)
            self.assertTrue(first_path.is_file())
            self.assertTrue(second_path.is_file())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_SUPPORTED)
            self.assertIn("candidate_standing_operation_v0_min_result", first_path.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_standing_operation_v0_min", str(resolver.OUTPUT_ROOT))
            for forbidden_root in (
                "candidate_standing_boundary",
                "distinctness_support_recheck",
                "successor_basis_emission",
                "successor_closure",
                "runtime",
                "daemon",
                "api",
            ):
                self.assertNotIn(forbidden_root, str(first_path.relative_to(root)))
            self.assertEqual(paths, original_paths)
            self.assertEqual(texts, original_texts)
            self.assertEqual(request["intent"], original_request["intent"])
            self.assertEqual(request["declared_non_claims"], original_request["declared_non_claims"])
            self.assertEqual(request["raw_payload"], "RAW_CANDIDATE_STANDING_BODY_MUST_NOT_RETURN")
            for path, text in ((paths[field], content) for field, content in texts.items()):
                self.assertEqual(path.read_text(encoding="utf-8"), text)
            missing_result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min_from_path(root / "requests" / "missing.json")
            self.assert_blocked_with_public_code(missing_result)
            malformed_path = self._write_markdown(root / "requests" / "malformed.json", "{not JSON")
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_standing_operation_v0_min_from_path(malformed_path)
            )
            array_path = self._write_json(root / "requests" / "array.json", [])
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_candidate_standing_operation_v0_min_from_path(array_path)
            )

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_candidate_standing_operation_v0_min(request)
            summary = resolver.build_descendant_body_candidate_standing_operation_v0_min_summary(result)
        self.assert_supported(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        for key, expected in (
            ("operation_id", resolver.OPERATION_ID),
            ("operation_type", resolver.OPERATION_TYPE),
            ("operation_version", resolver.OPERATION_VERSION),
            ("operation_scope", resolver.OPERATION_SCOPE),
            ("candidate_standing_result", "CANDIDATE_STANDING_SUPPORTED"),
            ("candidate_a_record_id", resolver.CANDIDATE_A_RECORD_ID),
            ("candidate_b_record_id", resolver.CANDIDATE_B_RECORD_ID),
            ("basis_pair_scope", resolver.BASIS_PAIR_SCOPE),
        ):
            self.assertEqual(summary[key], expected)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(summary[key], True, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary[key], False, key)
        self.assertEqual(summary["missing_or_insufficient_boundary_allowance"], [])
        self.assertEqual(summary["not_supported_reasons"], [])
        self.assertEqual(set(self.material(result)), {
            "candidate_a_standing_evaluation",
            "candidate_b_standing_evaluation",
            "standing_pair_evaluation",
        })
        self.assert_operation_separate_from_wrapper(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)


if __name__ == "__main__":
    unittest.main()
