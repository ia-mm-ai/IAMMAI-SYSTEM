"""Bounded tests for descendant-body candidate-standing boundary resolution."""

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

import resolve_descendant_body_candidate_standing_boundary_v0_min as resolver


class DescendantBodyCandidateStandingBoundaryV0MinTests(unittest.TestCase):
    """Verify one non-standing boundary for future operation consideration only."""

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture collision: {path} is a directory")
        path.write_text(content, encoding="utf-8")

    def remove_marker(self, content: str, marker: str, index: int) -> str:
        """Remove a tested marker and its only overlapping support alias."""
        changed = content.replace(marker, f"MISSING_{index}")
        if marker == "DISTINCTNESS_SUPPORTED":
            changed = changed.replace(
                "distinctness_supported_recorded = true", f"MISSING_RECORDED_{index}"
            )
        return changed

    def boundary_spec_text(self) -> str:
        return "\n".join(
            (
                "# Descendant Body Candidate Standing Boundary V0 Minimum Specification",
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY",
                "descendant_body_candidate_standing_boundary_001",
                "CONSIDER_CANDIDATE_STANDING_AFTER_SUPPORTED_DISTINCTNESS_ONLY",
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED",
                "DISTINCTNESS_SUPPORT_RECHECKED",
                "DISTINCTNESS_SUPPORTED",
                "distinctness_supported_recorded = true",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "candidate records marked distinct still not standing candidates",
                "candidate records marked distinct still not standing candidates, descendant bodies, relation participants, presence-bearing, or identity-bearing",
                "Candidate records marked distinct are still not standing candidates, descendant bodies, relation participants, presence-bearing, or identity-bearing.",
                "candidate records marked distinct are not descendant bodies.",
                "candidate records marked distinct are not relation participants.",
                "candidate records marked distinct are not presence-bearing.",
                "candidate records marked distinct are not identity-bearing.",
                "Candidate records marked distinct remain non-standing candidate records.",
                "candidate_standing_authorized = false",
                "descendant_body_created = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
                "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
                "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
                "both non-standing at emission time",
                "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
                "basis-pair non-hierarchy preserved",
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_REQUIRES_SUPPORTED_DISTINCTNESS",
                "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_BLOCKED",
                "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
                "REQUIRES_SUPPORTED_DISTINCTNESS",
                "Candidate-standing boundary is not candidate-standing operation.",
                "Candidate-standing boundary permission is not candidate-standing completion.",
                "Candidate-standing operation consideration is not candidate standing.",
                "Supported distinctness is not candidate standing.",
                "Candidate records distinct is not candidate standing.",
                "Candidate records distinct is not descendant-body creation.",
                "Candidate records distinct is not relation.",
                "Candidate records distinct is not presence.",
                "Candidate records distinct is not identity.",
                "Candidate A and Candidate B remain sibling non-standing candidate records.",
                "Candidate A basis material and Candidate B basis material remain sibling non-standing basis materials.",
                "neither ranks above the other.",
                "Regulation may not become sovereign over Motion.",
                "Motion may not erase Regulation.",
                "coupling remains unassigned.",
                "CANDIDATE_STANDING_BOUNDARY_THEN_CANDIDATE_STANDING_OPERATION_ONLY",
                "Only after a future boundary records CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED may a separately bounded candidate-standing operation be considered.",
                "No later operation is authorized by this specification alone.",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage.",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct candidate-standing boundary to candidate-standing operation completion",
                "direct supported distinctness or candidate records distinct to candidate standing, descendant-body creation, relation, presence, or identity",
                "direct candidate-standing boundary to descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, or follow-on work",
                "repository scan; file discovery; affected-file repair; and prior unsupported-claim validation",
                "direct supported distinctness to candidate standing",
                "direct supported distinctness to descendant-body creation",
                "direct supported distinctness to relation",
                "direct supported distinctness to presence",
                "direct supported distinctness to identity",
                "direct candidate records distinct to candidate standing",
                "direct candidate records distinct to descendant-body creation",
                "direct candidate records distinct to relation",
                "direct candidate records distinct to presence",
                "direct candidate records distinct to identity",
                "direct candidate-standing boundary to descendant-body creation",
                "direct candidate-standing boundary to crossing",
                "direct candidate-standing boundary to relation",
                "direct candidate-standing boundary to runtime",
                "direct candidate-standing boundary to authority/currentness",
                "direct candidate-standing boundary to coupling creation",
                "direct candidate-standing boundary to third-candidate route",
                "direct candidate-standing boundary to third-model route",
                "direct candidate-standing boundary to presence",
                "direct candidate-standing boundary to identity",
                "direct candidate-standing boundary to follow-on work",
                "repository scan route",
                "file discovery route",
                "affected-file repair route",
                "prior unsupported-claim validation route",
                "This boundary spec defines only a future candidate-standing boundary shape.",
                "It does not perform candidate-standing checks.",
                "Open means not scheduled, not authorized, and not executed.",
            )
        )

    def recheck_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED",
                "failed_check_count = 0",
                "passed_check_count = 96",
                "DISTINCTNESS_SUPPORT_RECHECKED",
                "DISTINCTNESS_SUPPORTED",
                "distinctness_supported_recorded = true",
                "candidate_records_marked_distinct = true",
                "candidate_records_distinct = true",
                "Candidate records marked distinct are still not standing candidates, descendant bodies, relation participants, presence-bearing, or identity-bearing.",
                "candidate records marked distinct are not standing candidates.",
                "candidate records marked distinct are not descendant bodies.",
                "candidate records marked distinct are not relation participants.",
                "candidate records marked distinct are not presence-bearing.",
                "candidate records marked distinct are not identity-bearing.",
                "Distinctness support is not candidate standing.",
                "candidate_standing_authorized = false",
                "descendant_body_created = false",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
            )
        )

    def synthetic_contents(self) -> dict[str, str]:
        return {
            "candidate_standing_boundary_spec_reference": self.boundary_spec_text(),
            "distinctness_support_recheck_terminal_summary_reference": self.recheck_summary_text(),
            "successor_basis_emission_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED",
                    "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
                    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
                    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
                    "both non-standing at emission time",
                    "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
                    "basis-pair non-hierarchy preserved",
                )
            ),
            "prior_distinctness_operation_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                    "NOT_DISTINCT",
                    "candidate-specific content and separate seal, receipt, and digest material were absent",
                )
            ),
            "existence_claim_evidence_check_terminal_summary_reference": "\n".join(
                (
                    "UNSUPPORTED",
                    "descendant_body_basis_candidate_a_created = true",
                    "descendant_body_basis_candidate_b_created = true",
                    "descendant_body_basis_derivation_event_recorded = true",
                )
            ),
            "basis_emission_operation_terminal_summary_reference": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "successor_closure_operation_terminal_summary_reference": "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED",
            "scope_division_operation_terminal_summary_reference": "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
        }

    def build_valid_synthetic_request(
        self, root: Path
    ) -> tuple[dict[str, Any], dict[str, Path], dict[str, str]]:
        contents = self.synthetic_contents()
        paths: dict[str, Path] = {}
        for index, (field, content) in enumerate(contents.items()):
            path = root / "synthetic_markers" / f"{index:02d}_{field}.md"
            self.write_markdown(path, content)
            paths[field] = path
        request = resolver.build_declared_descendant_body_candidate_standing_boundary_v0_min_request(
            **{field: str(path) for field, path in paths.items()}
        )
        return request, paths, contents

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return str(code) if isinstance(code, str) else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("candidate_standing_boundary_checks")
        return sum(
            check.get("passed") is False for check in checks if isinstance(check, dict)
        ) if isinstance(checks, list) else 0

    def passed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("candidate_standing_boundary_checks")
        return sum(
            check.get("passed") is True for check in checks if isinstance(check, dict)
        ) if isinstance(checks, list) else 0

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        value = result.get("descendant_body_candidate_standing_boundary")
        self.assertIsInstance(value, dict)
        return value

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_canonical_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def assert_all_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("candidate_standing_boundary_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            if isinstance(check, dict):
                for field in ("block_code", "failure_code"):
                    if check.get(field) is not None:
                        self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_boundary_is_not_wrapper(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        forbidden = {
            "outcome",
            "block",
            "candidate_standing_boundary_checks",
            "non_claims",
            "candidate_standing_boundary_summary",
            "candidate_standing_boundary_metadata",
            "candidate_standing_boundary_material",
        }
        self.assertTrue(forbidden.isdisjoint(boundary))

    def assert_final_refusal_posture(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in (
            "candidate_standing_check_performed",
            "candidate_standing_authorized",
            "candidate_standing_created",
            "descendant_body_created",
            "relation_created",
            "runtime_created",
            "coupling_created",
            "third_model_admitted",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[key], False)
        self.assert_canonical_non_claims(result)

    def assert_allowed(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assert_not_blocked(result)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)

    def assert_blocked_public(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_codes_public(result)
        self.assert_final_refusal_posture(result)

    def test_public_api_constants_and_builder_defaults(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_standing_boundary_v0_min",
            "resolve_descendant_body_candidate_standing_boundary_v0_min_from_path",
            "write_descendant_body_candidate_standing_boundary_v0_min_result",
            "build_descendant_body_candidate_standing_boundary_v0_min_summary",
            "build_declared_descendant_body_candidate_standing_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_standing_boundary_v0_min")
        self.assertEqual(resolver.BOUNDARY_ID, "descendant_body_candidate_standing_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.BOUNDARY_SCOPE, "CONSIDER_CANDIDATE_STANDING_AFTER_SUPPORTED_DISTINCTNESS_ONLY")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED, "DISTINCTNESS_SUPPORT_RECHECKED")
        self.assertEqual(resolver.PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED, "DISTINCTNESS_SUPPORTED")
        self.assertIs(resolver.PRIOR_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED, True)
        self.assertIs(resolver.PRIOR_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED, True)
        self.assertIs(resolver.PRIOR_CANDIDATE_RECORDS_DISTINCT_REQUIRED, True)
        self.assertIs(resolver.PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_DESCENDANT_BODY_CREATED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_RELATION_CREATED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_COUPLING_CREATED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_PRESENCE_ESTABLISHED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_IDENTITY_CREATED_REQUIRED, False)
        self.assertIs(resolver.PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED, False)
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "CANDIDATE_STANDING_BOUNDARY_THEN_CANDIDATE_STANDING_OPERATION_ONLY")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {resolver.OUTCOME_ALLOWED, resolver.OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED})
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_boundary_v0_min"))
        for code in (
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "CANDIDATE_STANDING_BOUNDARY_SPEC_REFERENCE_MISSING",
            "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "SUPPORTED_DISTINCTNESS_MISSING_OR_INSUFFICIENT",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_CANDIDATE_STANDING_CHECK_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        request = resolver.build_declared_descendant_body_candidate_standing_boundary_v0_min_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["boundary_id"], resolver.BOUNDARY_ID)
        self.assertTrue(all(value is False for value in request["declared_non_claims"].values()))
        self.assertTrue(all(request[key] is False for key in resolver.PROHIBITED_REQUEST_FLAGS))

    def test_synthetic_allowed_material_summary_and_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
            summary = resolver.build_descendant_body_candidate_standing_boundary_v0_min_summary(result)
        self.assert_allowed(result)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        for section in (
            "candidate_standing_boundary_metadata",
            "declared_candidate_standing_boundary_basis",
            "upstream_basis",
            "descendant_body_candidate_standing_boundary",
            "candidate_standing_boundary_material",
            "candidate_standing_boundary_checks",
            "candidate_standing_boundary_statement",
            "candidate_standing_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "candidate_standing_boundary_summary",
        ):
            self.assertIn(section, result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(boundary["prior_distinctness_support_recheck_operation_type"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE)
        self.assertEqual(boundary["prior_distinctness_support_recheck_operation_outcome_required"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(boundary["prior_distinctness_support_recheck_result_required"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED)
        self.assertEqual(boundary["prior_distinctness_support_result_required"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED)
        self.assertIs(boundary["prior_candidate_records_marked_distinct_required"], True)
        self.assertIs(boundary["prior_candidate_records_distinct_required"], True)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(boundary[key], True)
        self.assertEqual(boundary["candidate_standing_boundary_result"], "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED")
        self.assert_final_refusal_posture(result)
        self.assert_boundary_is_not_wrapper(result)
        marker_flags = [key for key in boundary if key.endswith("markers_present")]
        self.assertTrue(marker_flags)
        self.assertTrue(all(boundary[key] is True for key in marker_flags))
        self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_supported_distinctness"], [])

        material = result["candidate_standing_boundary_material"]
        self.assertEqual(set(material), {"supported_distinctness_reference", "candidate_records_reference", "boundary_evaluation"})
        support = material["supported_distinctness_reference"]
        self.assertEqual(support["prior_distinctness_support_recheck_operation_type"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE)
        self.assertEqual(support["prior_distinctness_support_recheck_operation_outcome"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(support["prior_distinctness_support_recheck_result"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED)
        self.assertEqual(support["prior_distinctness_support_result"], resolver.PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED)
        self.assertTrue(all(support[key] is True for key in ("prior_distinctness_supported_recorded", "prior_candidate_records_marked_distinct", "prior_candidate_records_distinct")))
        records = material["candidate_records_reference"]
        self.assertIs(records["candidate_records_marked_distinct"], True)
        self.assertIs(records["candidate_records_distinct"], True)
        for key in (
            "candidate_records_are_standing_candidates",
            "candidate_records_are_descendant_bodies",
            "candidate_records_are_relation_participants",
            "candidate_records_are_presence_bearing",
            "candidate_records_are_identity_bearing",
        ):
            self.assertIs(records[key], False)
        self.assertEqual(records["candidate_a_basis_id"], resolver.CANDIDATE_A_BASIS_ID)
        self.assertEqual(records["candidate_b_basis_id"], resolver.CANDIDATE_B_BASIS_ID)
        self.assertEqual(records["basis_pair_scope"], resolver.BASIS_PAIR_SCOPE)
        self.assertIs(records["basis_pair_non_hierarchy_preserved"], True)
        evaluation = material["boundary_evaluation"]
        self.assertIs(evaluation["candidate_standing_operation_consideration_allowed"], True)
        self.assertEqual(evaluation["candidate_standing_boundary_result"], "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED")
        for key in (
            "supported_distinctness_is_candidate_standing",
            "candidate_records_distinct_is_candidate_standing",
            "candidate_standing_check_performed",
            "candidate_standing_authorized",
            "descendant_body_created",
            "relation_created",
            "coupling_created",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
        ):
            self.assertIs(evaluation[key], False)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(summary["candidate_standing_boundary_result"], "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED")
        self.assertIs(summary["candidate_standing_operation_consideration_allowed"], True)
        self.assertIs(summary["supported_distinctness_referenced"], True)
        self.assertIs(summary["candidate_records_distinct_referenced"], True)
        self.assertEqual(summary["missing_or_insufficient_supported_distinctness"], [])

    def test_default_live_result_if_declared_files_exist(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_standing_boundary_v0_min_request()
        references = [request["candidate_standing_boundary_spec_reference"]]
        references.extend(request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS)
        if not all((REPO_ROOT / reference).is_file() for reference in references):
            self.skipTest("default target or upstream terminal summary is absent")
        result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
        self.assert_allowed(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["candidate_standing_boundary_result"], "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED")
        self.assert_final_refusal_posture(result)
        self.assertTrue(all(value is True for key, value in boundary.items() if key.endswith("markers_present")))

    def test_missing_supported_distinctness_returns_requires_or_blocked(self) -> None:
        markers = (
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED",
            "DISTINCTNESS_SUPPORT_RECHECKED",
            "DISTINCTNESS_SUPPORTED",
            "distinctness_supported_recorded = true",
            "candidate_records_marked_distinct = true",
            "candidate_records_distinct = true",
            "Candidate records marked distinct are still not standing candidates",
            "Distinctness support is not candidate standing",
            "candidate_standing_authorized = false",
            "descendant_body_created = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        )
        for index, marker in enumerate(markers):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                request, paths, contents = self.build_valid_synthetic_request(Path(directory))
                field = "distinctness_support_recheck_terminal_summary_reference"
                self.write_markdown(
                    paths[field], self.remove_marker(contents[field], marker, index)
                )
                result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
                self.assertIn(result["outcome"], {resolver.OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS, resolver.OUTCOME_BLOCKED})
                if result["outcome"] == resolver.OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS:
                    self.assert_not_blocked(result)
                    self.assertEqual(self.boundary(result)["candidate_standing_boundary_result"], "REQUIRES_SUPPORTED_DISTINCTNESS")
                    self.assertTrue(result["boundary_result_detail"]["missing_or_insufficient_supported_distinctness"])
                    self.assert_final_refusal_posture(result)
                else:
                    self.assert_blocked_public(result)
        with tempfile.TemporaryDirectory() as directory:
            request, _, _ = self.build_valid_synthetic_request(Path(directory))
            request["distinctness_support_recheck_terminal_summary_reference"] = str(Path(directory) / "missing" / self.safe_json_filename("recheck", 1))
            result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS)
            self.assert_not_blocked(result)
            self.assert_final_refusal_posture(result)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _, _ = self.build_valid_synthetic_request(Path(directory))
            no_record = copy.deepcopy(request)
            no_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(no_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(self.boundary(result)[key], False)
            self.assert_final_refusal_posture(result)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(blocked)
            self.assert_blocked_public(result)
            self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_exact_values_and_marker_validation(self) -> None:
        invalid = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min([])
        self.assert_blocked_public(invalid)
        self.assertEqual(self.block_code(invalid), "REQUEST_NOT_MAPPING")
        mutations = {
            "intent": "UNSUPPORTED_BOUNDARY_INTENT",
            "boundary_id": "wrong",
            "boundary_type": "wrong",
            "boundary_version": "wrong",
            "boundary_scope": "wrong",
            "prior_distinctness_support_recheck_operation_type": "wrong",
            "prior_distinctness_support_recheck_operation_outcome_required": "wrong",
            "prior_distinctness_support_recheck_result_required": "wrong",
            "prior_distinctness_support_result_required": "wrong",
            "prior_distinctness_supported_recorded_required": False,
            "prior_candidate_records_marked_distinct_required": False,
            "prior_candidate_records_distinct_required": False,
            "prior_candidate_standing_authorized_required": True,
            "prior_descendant_body_created_required": True,
            "prior_relation_created_required": True,
            "prior_coupling_created_required": True,
            "prior_presence_established_required": True,
            "prior_identity_created_required": True,
            "prior_follow_on_authorized_required": True,
            "admissible_future_route": "wrong",
        }
        with tempfile.TemporaryDirectory() as directory:
            request, _, _ = self.build_valid_synthetic_request(Path(directory))
            for key, value in mutations.items():
                with self.subTest(exact_value=key):
                    changed = copy.deepcopy(request)
                    changed[key] = value
                    self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed))

        marker_cases = (
            ("candidate_standing_boundary_spec_reference", "Descendant Body Candidate Standing Boundary V0 Minimum Specification"),
            ("distinctness_support_recheck_terminal_summary_reference", "DISTINCTNESS_SUPPORTED"),
            ("successor_basis_emission_terminal_summary_reference", "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED"),
            ("prior_distinctness_operation_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT"),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            ("basis_emission_operation_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS"),
            ("successor_closure_operation_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED"),
            ("scope_division_operation_terminal_summary_reference", "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS"),
        )
        for index, (field, marker) in enumerate(marker_cases):
            with self.subTest(marker_field=field), tempfile.TemporaryDirectory() as directory:
                request, paths, contents = self.build_valid_synthetic_request(Path(directory))
                self.write_markdown(
                    paths[field], self.remove_marker(contents[field], marker, index)
                )
                result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
                self.assertIn(result["outcome"], {resolver.OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS, resolver.OUTCOME_BLOCKED})
                if result["outcome"] == resolver.OUTCOME_BLOCKED:
                    self.assert_blocked_public(result)
                else:
                    self.assert_not_blocked(result)
                    self.assert_final_refusal_posture(result)

    def test_prohibited_flags_top_level_posture_and_declared_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _, _ = self.build_valid_synthetic_request(Path(directory))
            for field in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(prohibited_flag=field):
                    changed = copy.deepcopy(request)
                    changed[field] = True
                    self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_false_posture=field):
                    changed = copy.deepcopy(request)
                    changed[field] = True
                    self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed))
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(preclaimed_output=field):
                    changed = copy.deepcopy(request)
                    changed[field] = True
                    self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_non_claim=field):
                    changed = copy.deepcopy(request)
                    changed["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed)
                    self.assert_blocked_public(result)
                    self.assertIs(result["non_claims"][field], False)
            malformed = (
                None,
                [],
                {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]},
                {key: ("false" if key == resolver.REQUIRED_FALSE_NON_CLAIMS[0] else False) for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            )
            for posture in malformed:
                with self.subTest(malformed_type=type(posture).__name__):
                    changed = copy.deepcopy(request)
                    changed["declared_non_claims"] = posture
                    self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(changed))

    def test_path_write_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, paths, _ = self.build_valid_synthetic_request(root)
            original_request = copy.deepcopy(request)
            original_files = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            request["raw_state_body"] = "HOSTILE_SENTINEL_MUST_NOT_MUTATE_INPUT"
            original_with_sentinel = copy.deepcopy(request)
            result = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min(request)
            self.assert_allowed(result)
            self.assertEqual(request, original_with_sentinel)
            for key, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), original_files[key])

            request_path = root / "input" / self.safe_json_filename("valid request")
            request_path.parent.mkdir(parents=True, exist_ok=True)
            request_path.write_text(json.dumps(original_request), encoding="utf-8")
            from_path = resolver.resolve_descendant_body_candidate_standing_boundary_v0_min_from_path(request_path)
            self.assert_allowed(from_path)
            self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min_from_path(root / "missing" / self.safe_json_filename("missing")))
            malformed = root / "input" / self.safe_json_filename("malformed")
            malformed.write_text("{", encoding="utf-8")
            self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min_from_path(malformed))
            array = root / "input" / self.safe_json_filename("array")
            array.write_text("[]", encoding="utf-8")
            self.assert_blocked_public(resolver.resolve_descendant_body_candidate_standing_boundary_v0_min_from_path(array))

            output = root / "output" / "candidate_standing_boundary_v0_min_result.json"
            first = resolver.write_descendant_body_candidate_standing_boundary_v0_min_result(result, output)
            second = resolver.write_descendant_body_candidate_standing_boundary_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("candidate_standing_boundary_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_standing_boundary_v0_min", str(resolver.REPO_ROOT / resolver.OUTPUT_ROOT))
            for forbidden_root in ("distinctness_support_recheck", "successor_basis_emission", "successor_closure", "runtime", "daemon", "api", "field", "presence", "identity", "externalization"):
                self.assertNotEqual((resolver.REPO_ROOT / resolver.OUTPUT_ROOT).name, forbidden_root)


if __name__ == "__main__":
    unittest.main()
