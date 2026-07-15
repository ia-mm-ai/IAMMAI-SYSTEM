"""Tests for one descendant-body creation boundary without creation conversion."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_descendant_body_creation_boundary_v0_min as resolver


class DescendantBodyCreationBoundaryV0MinTests(unittest.TestCase):
    """Exercise bounded boundary allowance after candidate-standing support."""

    REFERENCE_FILENAMES = {
        "descendant_body_creation_boundary_spec_reference": "descendant_body_creation_boundary_spec.md",
        "candidate_standing_operation_terminal_summary_reference": "candidate_standing_operation_summary.md",
        "candidate_standing_boundary_terminal_summary_reference": "candidate_standing_boundary_summary.md",
        "distinctness_support_recheck_terminal_summary_reference": "distinctness_support_summary.md",
        "existence_claim_evidence_check_terminal_summary_reference": "existence_claim_summary.md",
        "successor_closure_operation_terminal_summary_reference": "successor_closure_summary.md",
        "scope_division_operation_terminal_summary_reference": "scope_division_summary.md",
    }

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

    def _write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic JSON path is a directory: {path}")
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _boundary_spec_text(self) -> str:
        return "\n".join(
            (
                "# Descendant Body Creation Boundary V0 Minimum Specification",
                "DESCENDANT_BODY_CREATION_BOUNDARY",
                "descendant_body_creation_boundary_001",
                "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY",
                "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
                "CANDIDATE_STANDING_SUPPORTED",
                "candidate_standing_supported = true",
                "candidate_standing_authorized = true",
                "candidate_standing_created = true",
                "candidate_a_standing_created = true",
                "candidate_b_standing_created = true",
                "Candidate A standing and Candidate B standing were supported, authorized, and created as candidate standing only",
                "Candidate standing is not descendant-body creation",
                "Candidate standing is not relation",
                "Candidate standing is not presence",
                "Candidate standing is not identity",
                "descendant_body_created = false",
                "descendant_body_a_created = false",
                "descendant_body_b_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
                "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUIRES_CANDIDATE_STANDING",
                "DESCENDANT_BODY_CREATION_BOUNDARY_BLOCKED",
                "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
                "REQUIRES_CANDIDATE_STANDING",
                "Descendant-body creation boundary is not descendant-body creation operation",
                "Descendant-body creation boundary permission is not descendant-body creation completion",
                "Descendant-body creation operation consideration is not descendant-body creation",
                "Candidate standing is not standing descendant",
                "Candidate standing is not crossing",
                "Candidate standing is not runtime",
                "Candidate standing is not currentness",
                "Candidate standing is not authority",
                "Candidate standing is not coupling",
                "Candidate standing is not follow-on authorization",
                "Candidate A and Candidate B remain sibling candidate standings",
                "Neither candidate standing ranks above the other",
                "Candidate A and Candidate B remain sibling candidate records",
                "Candidate A basis material and Candidate B basis material remain sibling basis materials",
                "Neither candidate basis ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "Coupling remains unassigned",
                resolver.ADMISSIBLE_FUTURE_ROUTE,
                "Only after a future boundary records DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED may a separately bounded descendant-body creation operation be considered",
                "No later operation is authorized by this boundary specification alone",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct descendant-body creation boundary to descendant-body creation operation completion",
                "direct candidate standing to descendant-body creation without boundary and operation",
                "direct candidate standing to standing descendant",
                "direct candidate standing to descendant standing",
                "direct descendant-body creation boundary to descendant-body creation",
                "direct descendant-body creation boundary to crossing",
                "direct descendant-body creation boundary to relation",
                "direct descendant-body creation boundary to runtime",
                "direct descendant-body creation boundary to authority/currentness",
                "direct descendant-body creation boundary to coupling creation",
                "direct descendant-body creation boundary to third-candidate route",
                "direct descendant-body creation boundary to third-model route",
                "direct descendant-body creation boundary to presence",
                "direct descendant-body creation boundary to identity",
                "direct descendant-body creation boundary to output/action",
                "direct descendant-body creation boundary to follow-on work",
                "repository scan route",
                "file discovery route",
                "affected-file repair route",
                "prior unsupported-claim validation route",
                "This boundary spec defines only a future descendant-body creation boundary shape",
                "It does not create descendant bodies",
                "Open means not scheduled, not authorized, and not executed",
            )
        )

    def _candidate_standing_operation_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
                "failed_check_count = 0",
                "passed_check_count = 176",
                "CANDIDATE_STANDING_SUPPORTED",
                "candidate_standing_supported = true",
                "candidate_standing_authorized = true",
                "candidate_standing_created = true",
                "candidate_a_standing_created = true",
                "candidate_b_standing_created = true",
                "Candidate A standing and Candidate B standing were supported, authorized, and created as candidate standing only",
                "Candidate standing is not descendant-body creation",
                "Candidate standing is not relation",
                "Candidate standing is not presence",
                "Candidate standing is not identity",
                "descendant_body_created = false",
                "descendant_body_a_created = false",
                "descendant_body_b_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            )
        )

    def _candidate_standing_boundary_text(self) -> str:
        return "\n".join((
            "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
            "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
        ))

    def _distinctness_support_text(self) -> str:
        return "DISTINCTNESS_SUPPORTED\ncandidate_records_distinct = true\n"

    def _existence_claim_text(self) -> str:
        return "\n".join((
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        ))

    def _successor_closure_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED\n"

    def _scope_division_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS\n"

    def _fixture_texts(self) -> dict[str, str]:
        return {
            "descendant_body_creation_boundary_spec_reference": self._boundary_spec_text(),
            "candidate_standing_operation_terminal_summary_reference": self._candidate_standing_operation_text(),
            "candidate_standing_boundary_terminal_summary_reference": self._candidate_standing_boundary_text(),
            "distinctness_support_recheck_terminal_summary_reference": self._distinctness_support_text(),
            "existence_claim_evidence_check_terminal_summary_reference": self._existence_claim_text(),
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
        request = resolver.build_declared_descendant_body_creation_boundary_v0_min_request(
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
        checks = result.get("descendant_body_creation_boundary_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is False for check in checks)

    def passed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("descendant_body_creation_boundary_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is True for check in checks)

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        boundary = result.get("descendant_body_creation_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def material(self, result: dict[str, Any]) -> dict[str, Any]:
        material = result.get("descendant_body_creation_boundary_material")
        self.assertIsInstance(material, dict)
        return material

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_allowed(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_ALLOWED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_requires_candidate_standing(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary.get("descendant_body_creation_boundary_result"), "REQUIRES_CANDIDATE_STANDING")
        self.assertIs(boundary.get("descendant_body_creation_operation_consideration_allowed"), False)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("descendant_body_creation_boundary_checks", [])
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
        boundary = self.boundary(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(boundary.get(key), False, key)

    def assert_all_marker_flags_true(self, result: dict[str, Any]) -> None:
        checks = result.get("descendant_body_creation_boundary_checks")
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

    def assert_boundary_separate_from_wrapper(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in (
            "outcome",
            "block",
            "descendant_body_creation_boundary_checks",
            "descendant_body_creation_boundary_summary",
            "descendant_body_creation_boundary_metadata",
            "descendant_body_creation_boundary_material",
            "non_claims",
        ):
            self.assertNotIn(key, boundary)

    def assert_bounded_non_allowed_result(self, result: dict[str, Any]) -> None:
        self.assertIn(result.get("outcome"), {
            resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            resolver.OUTCOME_BLOCKED,
        })
        if result.get("outcome") == resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING:
            self.assert_requires_candidate_standing(result)
            self.assertTrue(result["boundary_result_detail"]["missing_or_insufficient_candidate_standing"])
        else:
            self.assert_blocked_with_public_code(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_downstream_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_creation_boundary_v0_min",
            "resolve_descendant_body_creation_boundary_v0_min_from_path",
            "write_descendant_body_creation_boundary_v0_min_result",
            "build_descendant_body_creation_boundary_v0_min_summary",
            "build_declared_descendant_body_creation_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_descendant_body_creation_boundary_v0_min",
            "BOUNDARY_ID": "descendant_body_creation_boundary_001",
            "BOUNDARY_TYPE": "DESCENDANT_BODY_CREATION_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY",
            "PRIOR_CANDIDATE_STANDING_OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
            "PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
            "PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED": "CANDIDATE_STANDING_SUPPORTED",
            "ADMISSIBLE_FUTURE_ROUTE": "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_DESCENDANT_BODY_CREATION_OPERATION_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_CANDIDATE_STANDING_SUPPORTED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED",
            "PRIOR_CANDIDATE_A_STANDING_CREATED_REQUIRED",
            "PRIOR_CANDIDATE_B_STANDING_CREATED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_DESCENDANT_BODY_CREATED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertTrue(set(resolver.OUTCOME_FAMILY).issuperset({
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        }))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_boundary_v0_min"
        ))
        self.assertTrue(set(resolver.BLOCK_CODES))
        self.assertTrue(set(resolver.REQUIRED_FALSE_NON_CLAIMS))

    def test_synthetic_allowed_result_and_boundary_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
        self.assert_allowed(result)
        self.assertEqual(result.get("result_version"), "0.1.0")
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        for key in (
            "descendant_body_creation_boundary_metadata",
            "declared_descendant_body_creation_boundary_basis",
            "upstream_basis",
            "descendant_body_creation_boundary",
            "descendant_body_creation_boundary_material",
            "descendant_body_creation_boundary_checks",
            "descendant_body_creation_boundary_statement",
            "descendant_body_creation_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "descendant_body_creation_boundary_summary",
        ):
            self.assertIn(key, result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(boundary["prior_candidate_standing_operation_type"], resolver.PRIOR_CANDIDATE_STANDING_OPERATION_TYPE)
        self.assertEqual(boundary["prior_candidate_standing_operation_outcome_required"], resolver.PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(boundary["prior_candidate_standing_result_required"], resolver.PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED)
        for key in (
            "prior_candidate_standing_supported_required",
            "prior_candidate_standing_authorized_required",
            "prior_candidate_standing_created_required",
            "prior_candidate_a_standing_created_required",
            "prior_candidate_b_standing_created_required",
        ):
            self.assertIs(boundary[key], True, key)
        self.assertEqual(boundary["descendant_body_creation_boundary_result"], "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED")
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assert_no_downstream_posture(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)
        self.assert_boundary_separate_from_wrapper(result)
        self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_candidate_standing"], [])

    def test_synthetic_allowed_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
        self.assert_allowed(result)
        material = self.material(result)
        self.assertEqual(set(material), {
            "candidate_standing_reference",
            "candidate_pair_reference",
            "boundary_evaluation",
        })
        standing = material["candidate_standing_reference"]
        self.assertEqual(standing["prior_candidate_standing_operation_type"], resolver.PRIOR_CANDIDATE_STANDING_OPERATION_TYPE)
        self.assertEqual(standing["prior_candidate_standing_operation_outcome"], resolver.PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(standing["prior_candidate_standing_result"], resolver.PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED)
        for key in (
            "prior_candidate_standing_supported",
            "prior_candidate_standing_authorized",
            "prior_candidate_standing_created",
            "prior_candidate_a_standing_created",
            "prior_candidate_b_standing_created",
        ):
            self.assertIs(standing[key], True, key)
        pair = material["candidate_pair_reference"]
        for key in (
            "candidate_a_standing_created",
            "candidate_b_standing_created",
            "candidate_pair_non_hierarchy_preserved",
            "candidate_records_remain_sibling",
        ):
            self.assertIs(pair[key], True, key)
        for key in (
            "candidate_a_standing_is_descendant_body",
            "candidate_b_standing_is_descendant_body",
            "candidate_standing_is_descendant_body_creation",
            "candidate_standing_is_standing_descendant",
            "candidate_standing_is_relation",
            "candidate_standing_is_presence",
            "candidate_standing_is_identity",
            "coupling_created",
        ):
            self.assertIs(pair[key], False, key)
        evaluation = material["boundary_evaluation"]
        self.assertIs(evaluation["descendant_body_creation_operation_consideration_allowed"], True)
        self.assertEqual(evaluation["descendant_body_creation_boundary_result"], "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED")
        for key in (
            "descendant_body_creation_performed",
            "descendant_body_created",
            "standing_descendant_created",
            "crossing_authorized",
            "relation_created",
            "coupling_created",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
        ):
            self.assertIs(evaluation[key], False, key)

    def test_default_live_target_is_allowed_when_references_exist(self) -> None:
        request = resolver.build_declared_descendant_body_creation_boundary_v0_min_request()
        reference_paths = [
            REPOSITORY_ROOT / value
            for key, value in request.items()
            if key.endswith("_reference") and isinstance(value, str)
        ]
        if not all(path.is_file() for path in reference_paths):
            self.skipTest("default descendant-body boundary references are not all present")
        result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
        self.assert_allowed(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(self.boundary(result)[key], True, key)
        self.assert_no_downstream_posture(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)

    def test_missing_candidate_standing_and_upstream_basis_are_bounded(self) -> None:
        operation_markers = (
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate A standing and Candidate B standing were supported, authorized, and created as candidate standing only",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not relation",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
            "descendant_body_created = false",
            "descendant_body_a_created = false",
            "descendant_body_b_created = false",
            "standing_descendant_created = false",
            "descendant_standing_check_performed = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        )
        variants: list[tuple[str, str]] = [
            ("candidate_standing_operation_terminal_summary_reference", marker)
            for marker in operation_markers
        ]
        variants.extend((
            ("candidate_standing_boundary_terminal_summary_reference", "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED"),
            ("distinctness_support_recheck_terminal_summary_reference", "DISTINCTNESS_SUPPORTED"),
            ("distinctness_support_recheck_terminal_summary_reference", "candidate_records_distinct = true"),
        ))
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker) in enumerate(variants):
                with self.subTest(field=field, marker=marker):
                    request, paths, texts = self._build_valid_request(root / f"variant_{index:03d}")
                    self._write_markdown(paths[field], texts[field].replace(marker, "[removed marker]"))
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
                    self.assert_bounded_non_allowed_result(result)
                    self.assert_requires_candidate_standing(result)
            for index, field in enumerate((
                "candidate_standing_operation_terminal_summary_reference",
                "candidate_standing_boundary_terminal_summary_reference",
                "distinctness_support_recheck_terminal_summary_reference",
            ), start=len(variants)):
                with self.subTest(missing_reference=field):
                    request, _, _ = self._build_valid_request(root / f"missing_{index:03d}")
                    request[field] = str(root / "unavailable" / self.safe_json_filename(field, index))
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
                    self.assert_requires_candidate_standing(result)
                    self.assert_canonical_false_non_claims(result)
            for index, field in enumerate((
                "existence_claim_evidence_check_terminal_summary_reference",
                "successor_closure_operation_terminal_summary_reference",
                "scope_division_operation_terminal_summary_reference",
            ), start=100):
                with self.subTest(blocked_upstream=field):
                    request, _, _ = self._build_valid_request(root / f"blocked_{index:03d}")
                    request[field] = str(root / "unavailable" / self.safe_json_filename(field, index))
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
                    self.assert_blocked_with_public_code(result)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_creation_boundary_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            boundary = self.boundary(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(boundary[key], False, key)
            self.assert_no_downstream_posture(result)
            self.assert_canonical_false_non_claims(result)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            blocked_result = resolver.resolve_descendant_body_creation_boundary_v0_min(blocked)
        self.assert_blocked_with_public_code(blocked_result)
        self.assertEqual(self.block_code(blocked_result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_exact_fields_block(self) -> None:
        self.assert_blocked_with_public_code(
            resolver.resolve_descendant_body_creation_boundary_v0_min(["not", "a", "mapping"])
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            request, _, _ = self._build_valid_request(root)
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_INTENT"
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_creation_boundary_v0_min(unsupported)
            )
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = not expected if isinstance(expected, bool) else f"not_{expected}"
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)

    def test_marker_class_validation(self) -> None:
        mutations: tuple[tuple[str, str], ...] = (
            ("descendant_body_creation_boundary_spec_reference", resolver.BOUNDARY_ID),
            ("candidate_standing_operation_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED"),
            ("candidate_standing_boundary_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED"),
            ("distinctness_support_recheck_terminal_summary_reference", "DISTINCTNESS_SUPPORTED"),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            ("successor_closure_operation_terminal_summary_reference", "CLOSED"),
            ("scope_division_operation_terminal_summary_reference", "REQUIRES_ADDITIONAL_BASIS"),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker) in enumerate(mutations):
                with self.subTest(field=field):
                    request, paths, texts = self._build_valid_request(root / f"markers_{index:03d}")
                    self._write_markdown(paths[field], texts[field].replace(marker, "[removed marker]"))
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
                    self.assert_bounded_non_allowed_result(result)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            required_flags = {
                "request_descendant_body_creation", "request_descendant_body_a_creation",
                "request_descendant_body_b_creation", "request_standing_descendant_creation",
                "request_descendant_standing", "request_descendant_standing_check",
                "request_crossing_authorization", "request_first_crossing_authorization",
                "request_relation_creation", "request_field_machinery_creation",
                "request_runtime_creation", "request_api_creation", "request_currentness_creation",
                "request_authority_creation", "request_standing_creation", "request_output_authorization",
                "request_action_authorization", "request_derivative_reception_authorization",
                "request_synchronization_authorization", "request_coupling_assignment_to_candidate_a",
                "request_coupling_assignment_to_candidate_b", "request_coupling_creation",
                "request_third_candidate_creation", "request_third_model_admission",
                "request_presence_establishment", "request_identity_creation",
                "request_follow_on_authorization", "request_follow_on_work_authorization",
                "request_repository_scan", "request_file_discovery", "request_affected_file_repair",
                "request_affected_file_mutation", "request_prior_unsupported_claim_validation",
                "request_validation_enforcement",
            }
            self.assertTrue(required_flags.issubset(resolver.PROHIBITED_REQUEST_FLAGS))
            for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(field=field):
                    prohibited = copy.deepcopy(request)
                    prohibited[field] = True
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(prohibited)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_false_posture_preclaims_and_non_claims_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed[key] = True
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                with self.subTest(declared_non_claim=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(result_posture_preclaimed=key):
                    preclaimed = copy.deepcopy(request)
                    preclaimed[key] = True
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(preclaimed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
            preclaimed_result = copy.deepcopy(request)
            preclaimed_result["descendant_body_creation_boundary_result"] = "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"
            result = resolver.resolve_descendant_body_creation_boundary_v0_min(preclaimed_result)
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
                    result = resolver.resolve_descendant_body_creation_boundary_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_path_write_and_non_mutation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            request, paths, texts = self._build_valid_request(root)
            original_request = copy.deepcopy(request)
            original_paths = copy.deepcopy(paths)
            original_texts = copy.deepcopy(texts)
            request["raw_payload"] = "RAW_DESCENDANT_BODY_CREATION_BOUNDARY_MUST_NOT_RETURN"
            request_path = self._write_json(root / "requests" / "valid.json", request)
            result = resolver.resolve_descendant_body_creation_boundary_v0_min_from_path(request_path)
            self.assert_allowed(result)
            self.assertNotIn("RAW_DESCENDANT_BODY_CREATION_BOUNDARY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))
            output_path = root / "output" / "descendant_body_creation_boundary_v0_min_result.json"
            first_path = resolver.write_descendant_body_creation_boundary_v0_min_result(result, output_path)
            second_path = resolver.write_descendant_body_creation_boundary_v0_min_result(result, output_path)
            self.assertTrue(first_path.is_file())
            self.assertTrue(second_path.is_file())
            self.assertNotEqual(first_path, second_path)
            self.assertEqual(json.loads(first_path.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn("descendant_body_creation_boundary_v0_min_result", first_path.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_creation_boundary_v0_min", str(resolver.OUTPUT_ROOT))
            for forbidden_root in (
                "candidate_standing_operation", "candidate_standing_boundary", "distinctness_support_recheck",
                "successor_basis_emission", "successor_closure", "runtime", "daemon", "api",
            ):
                self.assertNotIn(forbidden_root, str(first_path.relative_to(root)))
            self.assertEqual(paths, original_paths)
            self.assertEqual(texts, original_texts)
            self.assertEqual(request["intent"], original_request["intent"])
            self.assertEqual(request["declared_non_claims"], original_request["declared_non_claims"])
            self.assertEqual(request["raw_payload"], "RAW_DESCENDANT_BODY_CREATION_BOUNDARY_MUST_NOT_RETURN")
            for path, text in ((paths[field], content) for field, content in texts.items()):
                self.assertEqual(path.read_text(encoding="utf-8"), text)
            missing = resolver.resolve_descendant_body_creation_boundary_v0_min_from_path(root / "requests" / "missing.json")
            self.assert_blocked_with_public_code(missing)
            malformed_path = self._write_markdown(root / "requests" / "malformed.json", "{not JSON")
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_creation_boundary_v0_min_from_path(malformed_path)
            )
            array_path = self._write_json(root / "requests" / "array.json", [])
            self.assert_blocked_with_public_code(
                resolver.resolve_descendant_body_creation_boundary_v0_min_from_path(array_path)
            )

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_boundary_v0_min(request)
            summary = resolver.build_descendant_body_creation_boundary_v0_min_summary(result)
        self.assert_allowed(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        for key, expected in (
            ("boundary_id", resolver.BOUNDARY_ID),
            ("boundary_type", resolver.BOUNDARY_TYPE),
            ("boundary_version", resolver.BOUNDARY_VERSION),
            ("boundary_scope", resolver.BOUNDARY_SCOPE),
            ("prior_candidate_standing_operation_type", resolver.PRIOR_CANDIDATE_STANDING_OPERATION_TYPE),
            ("prior_candidate_standing_operation_outcome_required", resolver.PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED),
            ("prior_candidate_standing_result_required", resolver.PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED),
            ("descendant_body_creation_boundary_result", "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"),
        ):
            self.assertEqual(summary[key], expected)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(summary[key], True, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary[key], False, key)
        self.assertEqual(summary["missing_or_insufficient_candidate_standing"], [])
        self.assertEqual(set(self.material(result)), {
            "candidate_standing_reference", "candidate_pair_reference", "boundary_evaluation",
        })
        self.assert_boundary_separate_from_wrapper(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_all_marker_flags_true(result)


if __name__ == "__main__":
    unittest.main()
