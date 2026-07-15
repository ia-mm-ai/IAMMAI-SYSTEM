"""Tests for one bounded descendant-body creation operation result.

Synthetic fixtures exercise creation as descendant-body records only: no
standing descendants, crossing, relation, runtime, coupling, presence,
identity, repair, discovery, validation, or downstream authorization.
"""

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

import resolve_descendant_body_creation_operation_v0_min as resolver


class DescendantBodyCreationOperationV0MinTests(unittest.TestCase):
    """Exercise the selected operation without permitting conversion routes."""

    REFERENCE_FILENAMES = {
        "descendant_body_creation_operation_spec_reference": "operation_spec.md",
        "descendant_body_creation_boundary_terminal_summary_reference": "boundary_summary.md",
        "candidate_standing_operation_terminal_summary_reference": "candidate_standing_operation.md",
        "candidate_standing_boundary_terminal_summary_reference": "candidate_standing_boundary.md",
        "existence_claim_evidence_check_terminal_summary_reference": "existence_claim.md",
        "successor_closure_operation_terminal_summary_reference": "successor_closure.md",
        "scope_division_operation_terminal_summary_reference": "scope_division.md",
    }

    DOWNSTREAM_FALSE_FIELDS = (
        "standing_descendant_created",
        "descendant_body_a_is_standing_descendant",
        "descendant_body_b_is_standing_descendant",
        "descendant_standing_check_performed",
        "crossing_authorized",
        "first_crossing_authorized",
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
        "coupling_assigned_to_candidate_a",
        "coupling_assigned_to_candidate_b",
        "coupling_created",
        "third_candidate_created",
        "third_model_admitted",
        "presence_established",
        "identity_created",
        "follow_on_authorized",
        "follow_on_work_authorized",
        "affected_file_repaired",
        "repository_scan_performed",
        "file_discovery_performed",
        "validation_enforced",
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
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
        return "\n".join((
            "# Descendant Body Creation Operation V0 Minimum Specification",
            "DESCENDANT_BODY_CREATION_OPERATION",
            "descendant_body_creation_operation_001",
            "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
            "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
            "descendant_body_creation_operation_consideration_allowed = true",
            "candidate_standing_referenced = true",
            "candidate_a_standing_referenced = true",
            "candidate_b_standing_referenced = true",
            "candidate_standing_created_referenced = true",
            "descendant_body_creation_performed = false",
            "descendant_body_created = false",
            "standing_descendant_created = false",
            "crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
            "CANDIDATE_STANDING_SUPPORTED",
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not relation",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
            "descendant_body_a_creation_evaluation",
            "descendant_body_b_creation_evaluation",
            "descendant_body_pair_evaluation",
            "descendant_body_a_001",
            "descendant_body_b_001",
            "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
            "DESCENDANT_BODY_CREATION_SUPPORTED",
            "descendant_body_creation_supported = true",
            "descendant_body_creation_authorized = true",
            "descendant_body_creation_performed = true",
            "descendant_body_a_created = true",
            "descendant_body_b_created = true",
            "descendant_body_created = true",
            "Descendant-body creation is not standing descendant creation",
            "Descendant body is not standing descendant",
            "Descendant body is not descendant standing",
            "Descendant body is not crossing",
            "Descendant body is not relation",
            "Descendant body is not runtime",
            "Descendant body is not currentness",
            "Descendant body is not authority",
            "Descendant body is not coupling",
            "Descendant body is not presence",
            "Descendant body is not identity",
            "Descendant body is not follow-on authorization",
            "Descendant body is not relation participation",
            "Descendant body is not presence-bearing",
            "Descendant body is not identity-bearing",
            "Descendant Body A and Descendant Body B remain sibling records",
            "neither descendant body ranks above the other",
            "Candidate A and Candidate B remain sibling candidate standings",
            "neither candidate standing ranks above the other",
            "Regulation may not become sovereign over Motion",
            "Motion may not erase Regulation",
            "coupling remains unassigned",
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future descendant-body creation operation records DESCENDANT_BODY_CREATION_SUPPORTED may a separately bounded first-crossing boundary be considered",
            "No later operation is authorized by this operation specification alone",
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
            "direct descendant-body creation operation spec to descendant-body creation operation completion",
            "direct boundary allowance to descendant-body creation without operation",
            "direct candidate standing to descendant-body creation without boundary and operation",
            "direct descendant-body creation to standing descendant",
            "direct descendant-body creation to descendant standing",
            "direct descendant-body creation to crossing",
            "direct descendant-body creation to relation",
            "direct descendant-body creation to runtime",
            "direct descendant-body creation to authority/currentness",
            "direct descendant-body creation to coupling creation",
            "direct descendant-body creation to third-candidate route",
            "direct descendant-body creation to third-model route",
            "direct descendant-body creation to presence",
            "direct descendant-body creation to identity",
            "direct descendant-body creation to output/action",
            "direct descendant-body creation to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
            "This operation spec defines only a future descendant-body creation operation shape",
            "It does not perform descendant-body creation",
            "Descendant-body creation operation spec is not descendant-body creation operation result",
            "Descendant-body creation operation permission is not descendant-body creation completion",
            "Descendant-body creation, if later supported, remains prior to any first-crossing boundary",
            "Open means not scheduled, not authorized, and not executed",
        ))

    def _boundary_summary_text(self) -> str:
        return "\n".join((
            "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
            "failed_check_count = 0",
            "passed_check_count = 153",
            "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
            "descendant_body_creation_operation_consideration_allowed = true",
            "candidate_standing_referenced = true",
            "candidate_a_standing_referenced = true",
            "candidate_b_standing_referenced = true",
            "candidate_standing_created_referenced = true",
            "descendant_body_creation_performed = false",
            "descendant_body_created = false",
            "standing_descendant_created = false",
            "crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ))

    def _candidate_standing_operation_text(self) -> str:
        return "\n".join((
            "CANDIDATE_STANDING_SUPPORTED",
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not relation",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
        ))

    def _candidate_standing_boundary_text(self) -> str:
        return "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED\n"

    def _existence_claim_text(self) -> str:
        return "\n".join((
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        ))

    def _successor_closure_text(self) -> str:
        return (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
            "SUCCESSOR_CLOSURE_OPERATION_CLOSED\n"
        )

    def _scope_division_text(self) -> str:
        return (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
            "OPERATION_REQUIRES_ADDITIONAL_BASIS\n"
        )

    def _fixture_texts(self) -> dict[str, str]:
        return {
            "descendant_body_creation_operation_spec_reference": self._operation_spec_text(),
            "descendant_body_creation_boundary_terminal_summary_reference": self._boundary_summary_text(),
            "candidate_standing_operation_terminal_summary_reference": self._candidate_standing_operation_text(),
            "candidate_standing_boundary_terminal_summary_reference": self._candidate_standing_boundary_text(),
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
        request = resolver.build_declared_descendant_body_creation_operation_v0_min_request(
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
        checks = result.get("descendant_body_creation_operation_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is False for check in checks)

    def passed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("descendant_body_creation_operation_checks", [])
        return sum(isinstance(check, dict) and check.get("passed") is True for check in checks)

    def operation(self, result: dict[str, Any]) -> dict[str, Any]:
        operation = result.get("descendant_body_creation_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def material(self, result: dict[str, Any]) -> dict[str, Any]:
        material = result.get("descendant_body_creation_operation_material")
        self.assertIsInstance(material, dict)
        return material

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_created(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_CREATED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_requires_allowance(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(operation["descendant_body_creation_result"], "REQUIRES_BOUNDARY_ALLOWANCE")
        self.assertIs(operation["descendant_body_creation_authorized"], False)
        self.assertIs(operation["descendant_body_created"], False)

    def assert_not_created(self, result: dict[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_CREATED)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(operation["descendant_body_creation_result"], "DESCENDANT_BODY_CREATION_NOT_SUPPORTED")
        self.assertIs(operation["descendant_body_creation_authorized"], False)
        self.assertIs(operation["descendant_body_created"], False)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("descendant_body_creation_operation_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, dict):
                continue
            for key in ("block_code", "failure_code"):
                if key in check:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_blocked_public(self, result: dict[str, Any]) -> None:
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
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)

    def assert_operation_separate_from_wrapper(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        for key in (
            "outcome",
            "block",
            "descendant_body_creation_operation_checks",
            "non_claims",
            "descendant_body_creation_operation_summary",
            "descendant_body_creation_operation_metadata",
            "descendant_body_creation_operation_material",
        ):
            self.assertNotIn(key, operation)
        self.assertNotIn("descendant_body_creation_operation_material", operation)

    def assert_no_downstream_posture(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        for field in self.DOWNSTREAM_FALSE_FIELDS:
            self.assertIs(operation.get(field), False, field)

    def assert_created_operation_shape(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        expected = {
            "operation_id": resolver.OPERATION_ID,
            "operation_type": resolver.OPERATION_TYPE,
            "operation_version": resolver.OPERATION_VERSION,
            "operation_scope": resolver.OPERATION_SCOPE,
            "prior_descendant_body_creation_boundary_type": resolver.PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_TYPE,
            "prior_descendant_body_creation_boundary_outcome_required": resolver.PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED,
            "prior_descendant_body_creation_boundary_result_required": resolver.PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED,
            "candidate_a_standing_source_id": resolver.CANDIDATE_A_STANDING_SOURCE_ID,
            "candidate_b_standing_source_id": resolver.CANDIDATE_B_STANDING_SOURCE_ID,
            "candidate_a_role": resolver.CANDIDATE_A_ROLE,
            "candidate_b_role": resolver.CANDIDATE_B_ROLE,
            "candidate_a_standing_label": resolver.CANDIDATE_A_STANDING_LABEL,
            "candidate_b_standing_label": resolver.CANDIDATE_B_STANDING_LABEL,
            "candidate_a_basis_id": resolver.CANDIDATE_A_BASIS_ID,
            "candidate_b_basis_id": resolver.CANDIDATE_B_BASIS_ID,
            "candidate_a_basis_label": resolver.CANDIDATE_A_BASIS_LABEL,
            "candidate_b_basis_label": resolver.CANDIDATE_B_BASIS_LABEL,
            "descendant_body_a_id": resolver.DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": resolver.DESCENDANT_BODY_B_ID,
            "descendant_body_pair_scope": resolver.DESCENDANT_BODY_PAIR_SCOPE,
            "descendant_body_creation_result": "DESCENDANT_BODY_CREATION_SUPPORTED",
        }
        for key, value in expected.items():
            self.assertEqual(operation.get(key), value, key)
        for field in (
            "prior_descendant_body_creation_operation_consideration_allowed_required",
            "prior_candidate_standing_referenced_required",
            "prior_candidate_a_standing_referenced_required",
            "prior_candidate_b_standing_referenced_required",
            "prior_candidate_standing_created_referenced_required",
        ):
            self.assertIs(operation.get(field), True, field)
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation.get(field), True, field)
        self.assert_no_downstream_posture(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_operation_separate_from_wrapper(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_creation_operation_v0_min",
            "resolve_descendant_body_creation_operation_v0_min_from_path",
            "write_descendant_body_creation_operation_v0_min_result",
            "build_descendant_body_creation_operation_v0_min_summary",
            "build_declared_descendant_body_creation_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        expected_constants = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_descendant_body_creation_operation_v0_min",
            "OPERATION_ID": "descendant_body_creation_operation_001",
            "OPERATION_TYPE": "DESCENDANT_BODY_CREATION_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_TYPE": "DESCENDANT_BODY_CREATION_BOUNDARY",
            "PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_OUTCOME_REQUIRED": "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
            "PRIOR_DESCENDANT_BODY_CREATION_BOUNDARY_RESULT_REQUIRED": "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "DESCENDANT_BODY_CREATION_OPERATION_THEN_FIRST_CROSSING_BOUNDARY_ONLY",
            "CANDIDATE_A_STANDING_SOURCE_ID": "descendant_body_basis_candidate_a_001",
            "CANDIDATE_B_STANDING_SOURCE_ID": "descendant_body_basis_candidate_b_001",
            "CANDIDATE_A_BASIS_ID": "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
            "CANDIDATE_B_BASIS_ID": "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
            "CANDIDATE_A_ROLE": "CANDIDATE_A",
            "CANDIDATE_B_ROLE": "CANDIDATE_B",
            "CANDIDATE_A_STANDING_LABEL": "CANDIDATE_A_STANDING",
            "CANDIDATE_B_STANDING_LABEL": "CANDIDATE_B_STANDING",
            "CANDIDATE_A_BASIS_LABEL": "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS",
            "CANDIDATE_B_BASIS_LABEL": "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS",
            "BASIS_PAIR_SCOPE": "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
            "DESCENDANT_BODY_A_ID": "descendant_body_a_001",
            "DESCENDANT_BODY_B_ID": "descendant_body_b_001",
            "DESCENDANT_BODY_PAIR_SCOPE": "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
        }
        for name, value in expected_constants.items():
            self.assertEqual(getattr(resolver, name), value, name)
        for name in (
            "PRIOR_DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_REFERENCED_REQUIRED",
            "PRIOR_CANDIDATE_A_STANDING_REFERENCED_REQUIRED",
            "PRIOR_CANDIDATE_B_STANDING_REFERENCED_REQUIRED",
            "PRIOR_CANDIDATE_STANDING_CREATED_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True, name)
        for name in (
            "PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED",
            "PRIOR_DESCENDANT_BODY_CREATED_REQUIRED",
            "PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED",
            "PRIOR_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False, name)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_operation_v0_min"
        ))
        for outcome in (
            resolver.OUTCOME_CREATED,
            resolver.OUTCOME_NOT_CREATED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        for code in (
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "DESCENDANT_BODY_CREATION_OPERATION_SPEC_REFERENCE_MISSING",
            "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
            "DESCENDANT_BODY_CREATION_NOT_SUPPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
            "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
            "PROHIBITED_CROSSING_REQUESTED",
            "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
            "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
            "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_synthetic_created_result_and_wrapper_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
            self.assert_created(result)
            self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_created_operation_shape(result)
            expected_sections = {
                "descendant_body_creation_operation_metadata",
                "declared_descendant_body_creation_operation_basis",
                "upstream_basis",
                "descendant_body_creation_operation",
                "descendant_body_creation_operation_material",
                "descendant_body_creation_operation_checks",
                "descendant_body_creation_operation_statement",
                "descendant_body_creation_operation_non_meaning",
                "descendant_body_creation_result_detail",
                "permitted_future_route",
                "blocked_routes",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "descendant_body_creation_operation_summary",
            }
            self.assertTrue(expected_sections.issubset(result))
            detail = result["descendant_body_creation_result_detail"]
            self.assertEqual(detail["missing_or_insufficient_boundary_allowance"], [])
            self.assertEqual(detail["not_created_reasons"], [])
            self.assertTrue(all(value is True for key, value in self.operation(result).items() if key.endswith("markers_present")))

    def test_created_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
            self.assert_created(result)
            material = self.material(result)
            self.assertEqual(set(material), {
                "descendant_body_a_creation_evaluation",
                "descendant_body_b_creation_evaluation",
                "descendant_body_pair_evaluation",
            })
            a = material["descendant_body_a_creation_evaluation"]
            b = material["descendant_body_b_creation_evaluation"]
            pair = material["descendant_body_pair_evaluation"]
            self.assertEqual(a["descendant_body_id"], resolver.DESCENDANT_BODY_A_ID)
            self.assertEqual(a["candidate_standing_source_id"], resolver.CANDIDATE_A_STANDING_SOURCE_ID)
            self.assertEqual(a["candidate_role"], resolver.CANDIDATE_A_ROLE)
            self.assertEqual(a["candidate_standing_label"], resolver.CANDIDATE_A_STANDING_LABEL)
            self.assertEqual(a["candidate_basis_id"], resolver.CANDIDATE_A_BASIS_ID)
            self.assertEqual(a["candidate_basis_label"], resolver.CANDIDATE_A_BASIS_LABEL)
            self.assertEqual(a["candidate_basis_scope"], "Motion-side admissible variation")
            self.assertEqual(b["descendant_body_id"], resolver.DESCENDANT_BODY_B_ID)
            self.assertEqual(b["candidate_standing_source_id"], resolver.CANDIDATE_B_STANDING_SOURCE_ID)
            self.assertEqual(b["candidate_role"], resolver.CANDIDATE_B_ROLE)
            self.assertEqual(b["candidate_standing_label"], resolver.CANDIDATE_B_STANDING_LABEL)
            self.assertEqual(b["candidate_basis_id"], resolver.CANDIDATE_B_BASIS_ID)
            self.assertEqual(b["candidate_basis_label"], resolver.CANDIDATE_B_BASIS_LABEL)
            self.assertEqual(b["candidate_basis_scope"], "Regulation-side admissibility bounds")
            for evaluation in (a, b):
                for key in (
                    "candidate_standing_created",
                    "descendant_body_creation_supported",
                    "descendant_body_creation_authorized",
                    "descendant_body_created",
                ):
                    self.assertIs(evaluation[key], True, key)
                for key in (
                    "candidate_standing_is_descendant_body",
                    "standing_descendant_created",
                    "descendant_body_is_standing_descendant",
                    "crossing_authorized",
                    "relation_created",
                    "presence_established",
                    "identity_created",
                ):
                    self.assertIs(evaluation[key], False, key)
            for key in (
                "both_descendant_body_creations_supported",
                "both_descendant_body_creations_authorized",
                "both_descendant_bodies_created",
                "descendant_body_a_created",
                "descendant_body_b_created",
                "descendant_body_created",
                "descendant_bodies_remain_sibling",
                "descendant_body_non_hierarchy_preserved",
                "candidate_standing_non_hierarchy_preserved",
                "candidate_basis_non_hierarchy_preserved",
                "regulation_not_sovereign_over_motion",
                "motion_does_not_erase_regulation",
            ):
                self.assertIs(pair[key], True, key)
            for key in (
                "standing_descendant_created",
                "descendant_standing_check_performed",
                "crossing_authorized",
                "first_crossing_authorized",
                "coupling_assigned",
                "coupling_created",
                "third_candidate_created",
                "third_model_admitted",
                "relation_created",
                "presence_established",
                "identity_created",
                "follow_on_authorized",
            ):
                self.assertIs(pair[key], False, key)

    def test_default_live_target_created_when_present(self) -> None:
        request = resolver.build_declared_descendant_body_creation_operation_v0_min_request()
        references = [request["descendant_body_creation_operation_spec_reference"]]
        references.extend(request[field] for field in self.REFERENCE_FILENAMES if field != "descendant_body_creation_operation_spec_reference")
        if not all((REPOSITORY_ROOT / Path(reference)).is_file() for reference in references):
            self.skipTest("default operation target or upstream summaries are not all present")
        result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
        self.assert_created(result)
        self.assert_created_operation_shape(result)
        self.assertTrue(all(value is True for key, value in self.operation(result).items() if key.endswith("markers_present")))

    def test_missing_or_corrupt_boundary_allowance_is_bounded(self) -> None:
        cases = (
            ("descendant_body_creation_boundary_terminal_summary_reference", None),
            ("descendant_body_creation_boundary_terminal_summary_reference", "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"),
            ("candidate_standing_operation_terminal_summary_reference", None),
            ("candidate_standing_operation_terminal_summary_reference", "CANDIDATE_STANDING_SUPPORTED"),
            ("candidate_standing_boundary_terminal_summary_reference", None),
            ("candidate_standing_boundary_terminal_summary_reference", "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED"),
            ("existence_claim_evidence_check_terminal_summary_reference", None),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker) in enumerate(cases):
                with self.subTest(field=field, marker=marker):
                    request, paths, _ = self._build_valid_request(root / f"case_{index:03d}")
                    if marker is None:
                        request[field] = str(root / "missing" / self.safe_json_filename(field, index))
                    else:
                        # Do not retain the requested marker in explanatory text:
                        # some required markers are valid substrings of other lines.
                        self._write_markdown(paths[field], "[corrupt synthetic basis]\n")
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
                    self.assertIn(result["outcome"], {
                        resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                        resolver.OUTCOME_NOT_CREATED,
                        resolver.OUTCOME_BLOCKED,
                    })
                    if result["outcome"] == resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
                        self.assert_requires_allowance(result)
                        self.assertTrue(result["descendant_body_creation_result_detail"]["missing_or_insufficient_boundary_allowance"])
                    elif result["outcome"] == resolver.OUTCOME_NOT_CREATED:
                        self.assert_not_created(result)
                        self.assertTrue(result["descendant_body_creation_result_detail"]["not_created_reasons"])
                    else:
                        self.assert_blocked_public(result)
                    self.assert_canonical_false_non_claims(result)

    def test_not_recorded_not_created_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = resolver.resolve_descendant_body_creation_operation_v0_min(do_not_record)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(not_recorded)
            operation = self.operation(not_recorded)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[field], False, field)
            self.assert_no_downstream_posture(not_recorded)
            self.assert_canonical_false_non_claims(not_recorded)

            insufficient = copy.deepcopy(request)
            insufficient["descendant_body_creation_support_evidence_present"] = False
            not_created = resolver.resolve_descendant_body_creation_operation_v0_min(insufficient)
            self.assert_not_created(not_created)
            self.assertTrue(not_created["descendant_body_creation_result_detail"]["not_created_reasons"])
            self.assert_no_downstream_posture(not_created)
            self.assert_canonical_false_non_claims(not_created)

            explicit = copy.deepcopy(request)
            explicit["intent"] = resolver.INTENT_BLOCK
            blocked = resolver.resolve_descendant_body_creation_operation_v0_min(explicit)
            self.assert_blocked_public(blocked)
            self.assertEqual(self.block_code(blocked), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_exact_values_block(self) -> None:
        result = resolver.resolve_descendant_body_creation_operation_v0_min([])
        self.assert_blocked_public(result)
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_INTENT"
            self.assert_blocked_public(resolver.resolve_descendant_body_creation_operation_v0_min(unsupported))
            for index, (field, value) in enumerate(resolver.EXPECTED_REQUEST_VALUES.items()):
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = "wrong" if not isinstance(value, bool) else not value
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(malformed)
                    self.assert_blocked_public(result)
                    self.assertIn(self.block_code(result), {
                        "REQUEST_VALUE_MISMATCH",
                        "RESULT_POSTURE_PRECLAIMED",
                    })

    def test_target_and_upstream_marker_class_validation(self) -> None:
        cases = (
            ("descendant_body_creation_operation_spec_reference", "Descendant Body Creation Operation V0 Minimum Specification"),
            ("descendant_body_creation_boundary_terminal_summary_reference", "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"),
            ("candidate_standing_operation_terminal_summary_reference", "CANDIDATE_STANDING_SUPPORTED"),
            ("candidate_standing_boundary_terminal_summary_reference", "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED"),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            ("successor_closure_operation_terminal_summary_reference", "CLOSED"),
            ("scope_division_operation_terminal_summary_reference", "REQUIRES_ADDITIONAL_BASIS"),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for index, (field, marker) in enumerate(cases):
                with self.subTest(field=field, marker=marker):
                    request, paths, texts = self._build_valid_request(root / f"marker_{index:03d}")
                    # A marker can be a substring of a fuller required line.  Replace
                    # the complete fixture with marker-free content to test the class.
                    self._write_markdown(paths[field], "[marker-free synthetic basis]\n")
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
                    self.assertIn(result["outcome"], {
                        resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                        resolver.OUTCOME_BLOCKED,
                    })
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_public(result)
                    else:
                        self.assert_requires_allowance(result)
                        self.assert_canonical_false_non_claims(result)

    def test_prohibited_flags_and_top_level_false_posture_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            for field, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(prohibited_flag=field):
                    blocked = copy.deepcopy(request)
                    blocked[field] = True
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(blocked)
                    self.assert_blocked_public(result)
                    self.assertEqual(self.block_code(result), code)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_false_posture=field):
                    blocked = copy.deepcopy(request)
                    blocked[field] = True
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(blocked)
                    self.assert_blocked_public(result)
                    expected = (
                        "RESULT_POSTURE_PRECLAIMED"
                        if field in resolver.ALLOWED_TRUE_RECORDED_FIELDS
                        else "NON_CLAIM_MISSING_OR_FLIPPED"
                    )
                    self.assertEqual(self.block_code(result), expected)

    def test_declared_non_claims_canonicalize_after_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=field):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_creation_operation_v0_min(malformed)
                    self.assert_blocked_public(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
            malformed_cases: tuple[tuple[str, Any], ...] = (
                ("missing", None),
                ("non_mapping", []),
                ("non_bool", {**request["declared_non_claims"], "relation_created": "false"}),
            )
            for name, value in malformed_cases:
                with self.subTest(case=name):
                    malformed = copy.deepcopy(request)
                    if name == "missing":
                        malformed.pop("declared_non_claims")
                    else:
                        malformed["declared_non_claims"] = value
                    self.assert_blocked_public(
                        resolver.resolve_descendant_body_creation_operation_v0_min(malformed)
                    )
            missing_key = copy.deepcopy(request)
            missing_key["declared_non_claims"].pop("relation_created")
            self.assert_blocked_public(
                resolver.resolve_descendant_body_creation_operation_v0_min(missing_key)
            )

    def test_path_write_and_non_mutation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            request, paths, texts = self._build_valid_request(root)
            original_request = copy.deepcopy(request)
            original_texts = copy.deepcopy(texts)
            request_path = self._write_json(root / "request" / "valid.json", request)
            result = resolver.resolve_descendant_body_creation_operation_v0_min_from_path(request_path)
            self.assert_created(result)
            self.assertEqual(request, original_request)
            for field, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), original_texts[field])
            missing = resolver.resolve_descendant_body_creation_operation_v0_min_from_path(root / "missing.json")
            self.assert_blocked_public(missing)
            malformed_path = root / "request" / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_blocked_public(
                resolver.resolve_descendant_body_creation_operation_v0_min_from_path(malformed_path)
            )
            array_path = self._write_json(root / "request" / "array.json", [])
            self.assert_blocked_public(
                resolver.resolve_descendant_body_creation_operation_v0_min_from_path(array_path)
            )
            output = root / "output" / resolver.DETERMINISTIC_FILENAME
            first = resolver.write_descendant_body_creation_operation_v0_min_result(result, output)
            second = resolver.write_descendant_body_creation_operation_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("descendant_body_creation_operation_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_CREATED)
            default_root = REPOSITORY_ROOT / resolver.OUTPUT_ROOT
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_creation_operation_v0_min", str(default_root))
            for forbidden in (
                "descendant_body_creation_boundary",
                "candidate_standing_operation",
                "candidate_standing_boundary",
                "runtime",
                "daemon",
                "api",
                "field",
                "presence",
                "identity",
                "externalization",
            ):
                self.assertNotIn(forbidden, str(first.relative_to(root / "output")))

    def test_summary_and_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            request, _, _ = self._build_valid_request(Path(temporary_directory))
            result = resolver.resolve_descendant_body_creation_operation_v0_min(request)
            self.assert_created(result)
            summary = resolver.build_descendant_body_creation_operation_v0_min_summary(result)
            expected = {
                "outcome": resolver.OUTCOME_CREATED,
                "failed_check_count": 0,
                "result_version": resolver.RESULT_VERSION,
                "resolver_module": resolver.RESOLVER_MODULE,
                "operation_id": resolver.OPERATION_ID,
                "operation_type": resolver.OPERATION_TYPE,
                "operation_version": resolver.OPERATION_VERSION,
                "operation_scope": resolver.OPERATION_SCOPE,
                "descendant_body_creation_result": "DESCENDANT_BODY_CREATION_SUPPORTED",
                "descendant_body_creation_supported": True,
                "descendant_body_creation_authorized": True,
                "descendant_body_creation_performed": True,
                "descendant_body_a_created": True,
                "descendant_body_b_created": True,
                "descendant_body_created": True,
                "missing_or_insufficient_boundary_allowance": [],
                "not_created_reasons": [],
            }
            for key, value in expected.items():
                self.assertEqual(summary.get(key), value, key)
            self.assertGreater(summary["passed_check_count"], 0)
            for field in self.DOWNSTREAM_FALSE_FIELDS:
                self.assertIs(summary.get(field), False, field)
            self.assertTrue(any(key.endswith("markers_present") and value is True for key, value in summary.items()))
            self.assertIn("operation_spec.md", summary["selected_target_spec_path"])
            self.assertIn("boundary_summary.md", summary["completed_descendant_body_creation_boundary_terminal_summary_path"])
            self.assertIn("candidate_standing_operation.md", summary["completed_candidate_standing_operation_terminal_summary_path"])
            self.assert_created_operation_shape(result)
            self.assertEqual(
                set(self.material(result)),
                {
                    "descendant_body_a_creation_evaluation",
                    "descendant_body_b_creation_evaluation",
                    "descendant_body_pair_evaluation",
                },
            )


if __name__ == "__main__":
    unittest.main()
