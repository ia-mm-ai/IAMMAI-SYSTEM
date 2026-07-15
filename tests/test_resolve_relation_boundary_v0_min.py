"""Executable boundary checks for one local relation-boundary resolver.

The suite keeps relation boundary separate from relation.  It proves that
completed first-crossing v2 support can allow only a future, separately
bounded relation-operation consideration, while preserving no coupling,
runtime, authority, presence, identity, standing descendant, repair,
discovery, validation enforcement, or follow-on authorization.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_boundary_v0_min as resolver


class RelationBoundaryV0MinTests(unittest.TestCase):
    """Test one bounded relation-boundary result and its refusal posture."""

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
        return path

    def valid_relation_boundary_spec_text(self) -> str:
        return "\n".join(
            (
                "# Relation Boundary V0 Minimum Specification",
                "RELATION_BOUNDARY",
                "relation_boundary_001",
                "CONSIDER_RELATION_AFTER_FIRST_CROSSING_ONLY",
                "FIRST_CROSSING_OPERATION_RECORDED",
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "First Crossing A and First Crossing B were evaluated, supported, authorized, performed, and recorded as first-crossing records only",
                "first crossing is not relation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
                "first crossing is not follow-on authorization",
                "first crossing is not follow-on work authorization",
                "first crossing is not standing descendant",
                "first crossing is not descendant standing",
                "crossing authorization and performance are not relation creation",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
                "RELATION_BOUNDARY_ALLOWED",
                "RELATION_BOUNDARY_REQUIRES_FIRST_CROSSING",
                "RELATION_BOUNDARY_BLOCKED",
                "RELATION_OPERATION_CONSIDERATION_ALLOWED",
                "REQUIRES_FIRST_CROSSING",
                "Relation boundary is not relation operation",
                "Relation boundary permission is not relation creation",
                "Relation operation consideration is not relation",
                "First crossing is not relation",
                "Crossing authorization is not relation creation",
                "Crossing performance is not relation creation",
                "First crossing is not coupling",
                "First crossing is not presence",
                "First crossing is not identity",
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
                "RELATION_BOUNDARY_THEN_RELATION_OPERATION_ONLY",
                "Only after a future relation boundary records RELATION_OPERATION_CONSIDERATION_ALLOWED may a separately bounded relation operation be considered",
                "No later operation is authorized by this boundary spec alone",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct relation boundary to relation operation completion",
                "direct first crossing to relation without relation boundary and operation",
                "direct crossing authorization to relation",
                "direct crossing performance to relation",
                "direct relation boundary to relation authorization",
                "direct relation boundary to relation creation",
                "direct relation boundary to FIELD machinery",
                "direct relation boundary to runtime",
                "direct relation boundary to authority/currentness",
                "direct relation boundary to coupling assignment",
                "direct relation boundary to coupling creation",
                "direct relation boundary to third-candidate route",
                "direct relation boundary to third-model route",
                "direct relation boundary to presence",
                "direct relation boundary to identity",
                "direct relation boundary to standing descendant",
                "direct relation boundary to descendant standing",
                "direct relation boundary to output/action",
                "direct relation boundary to follow-on work",
                "repository scan route",
                "file discovery route",
                "affected-file repair route",
                "prior unsupported-claim validation route",
                "This boundary spec defines only a future relation boundary shape",
                "It does not authorize relation",
                "First-crossing, if later used as relation basis, remains prior basis only",
                "Open means not scheduled, not authorized, and not executed",
            )
        )

    def valid_first_crossing_operation_v2_summary_text(self) -> str:
        return "\n".join(
            (
                "FIRST_CROSSING_OPERATION_RECORDED",
                "failed_check_count = 0",
                "passed_check_count = 243",
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "First Crossing A and First Crossing B were evaluated, supported, authorized, performed, and recorded as first-crossing records only",
                "first crossing is not relation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
                "first crossing is not follow-on authorization",
                "first crossing is not follow-on work authorization",
                "first crossing is not standing descendant",
                "first crossing is not descendant standing",
                "crossing authorization is not relation creation",
                "crossing performance is not relation creation",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
            )
        )

    def valid_first_crossing_boundary_summary_text(self) -> str:
        return "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED\n"

    def valid_descendant_body_creation_operation_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CREATION_SUPPORTED",
                "Descendant Body A and Descendant Body B were evaluated, supported, and created as descendant-body records only",
                "Descendant Body A and Descendant Body B were created as descendant-body records only",
                "while preserving relation, presence, identity, coupling, and follow-on false",
                "preserved no standing descendant, crossing, relation, presence, identity, or follow-on",
            )
        )

    def valid_existence_claim_evidence_check_summary_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        )

    def synthetic_paths(self, root: Path) -> dict[str, Path]:
        return {
            "relation_boundary_spec_reference": root / "relation_boundary_spec.md",
            "first_crossing_operation_v2_terminal_summary_reference": root
            / "first_crossing_operation_v2_summary.md",
            "first_crossing_boundary_terminal_summary_reference": root
            / "first_crossing_boundary_summary.md",
            "descendant_body_creation_operation_terminal_summary_reference": root
            / "descendant_body_creation_operation_summary.md",
            "existence_claim_evidence_check_terminal_summary_reference": root
            / "existence_claim_evidence_check_summary.md",
        }

    def build_valid_synthetic_request(self, root: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = self.synthetic_paths(root)
        self.write_markdown(paths["relation_boundary_spec_reference"], self.valid_relation_boundary_spec_text())
        self.write_markdown(
            paths["first_crossing_operation_v2_terminal_summary_reference"],
            self.valid_first_crossing_operation_v2_summary_text(),
        )
        self.write_markdown(
            paths["first_crossing_boundary_terminal_summary_reference"],
            self.valid_first_crossing_boundary_summary_text(),
        )
        self.write_markdown(
            paths["descendant_body_creation_operation_terminal_summary_reference"],
            self.valid_descendant_body_creation_operation_summary_text(),
        )
        self.write_markdown(
            paths["existence_claim_evidence_check_terminal_summary_reference"],
            self.valid_existence_claim_evidence_check_summary_text(),
        )
        return resolver.build_relation_boundary_v0_min_request(**paths), paths

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code")
        return code if isinstance(code, str) else block.get("block_code")

    def failed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get("relation_boundary_checks", [])
        return sum(
            item.get("passed") is False for item in checks if isinstance(item, dict)
        )

    def assert_allowed_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_requires_first_crossing_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_FIRST_CROSSING)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsInstance(code, str)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("relation_boundary_checks", [])
        for check in checks:
            if not isinstance(check, dict):
                continue
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)

    def assert_boundary_without_wrapper_fields(self, result: dict[str, Any]) -> None:
        boundary = result.get("relation_boundary")
        self.assertIsInstance(boundary, dict)
        for field in (
            "outcome",
            "block",
            "relation_boundary_checks",
            "non_claims",
            "relation_boundary_summary",
            "relation_boundary_metadata",
            "relation_boundary_material",
        ):
            self.assertNotIn(field, boundary)

    def assert_final_refusal_posture(self, result: dict[str, Any]) -> None:
        self.assert_canonical_non_claims(result)
        boundary = result["relation_boundary"]
        for field in (
            "relation_authorized",
            "relation_created",
            "relation_operation_performed",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "currentness_created",
            "authority_created",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "presence_established",
            "identity_created",
            "standing_descendant_created",
            "descendant_standing_check_performed",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "repository_scan_performed",
            "file_discovery_performed",
            "affected_file_repaired",
            "validation_enforced",
        ):
            self.assertIs(boundary[field], False, field)

    def assert_allowed_boundary_shape(self, result: dict[str, Any]) -> None:
        self.assert_allowed_not_blocked(result)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], "resolve_relation_boundary_v0_min")
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_canonical_non_claims(result)
        self.assert_boundary_without_wrapper_fields(result)
        boundary = result["relation_boundary"]
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            boundary["relation_boundary_result"], "RELATION_OPERATION_CONSIDERATION_ALLOWED"
        )
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(boundary[field], True, field)
        self.assert_final_refusal_posture(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relation_boundary_v0_min",
            "resolve_relation_boundary_v0_min_from_path",
            "write_relation_boundary_v0_min_result",
            "build_relation_boundary_v0_min_summary",
            "build_relation_boundary_v0_min_request",
            "build_declared_relation_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_relation_boundary_v0_min",
            "BOUNDARY_ID": "relation_boundary_001",
            "BOUNDARY_TYPE": "RELATION_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": "CONSIDER_RELATION_AFTER_FIRST_CROSSING_ONLY",
            "PRIOR_FIRST_CROSSING_OPERATION_TYPE": "FIRST_CROSSING_OPERATION",
            "PRIOR_FIRST_CROSSING_OPERATION_OUTCOME_REQUIRED": "FIRST_CROSSING_OPERATION_RECORDED",
            "PRIOR_FIRST_CROSSING_RESULT_REQUIRED": "FIRST_CROSSING_SUPPORTED",
            "ADMISSIBLE_FUTURE_ROUTE": "RELATION_BOUNDARY_THEN_RELATION_OPERATION_ONLY",
            "FIRST_CROSSING_A_ID": "first_crossing_a_001",
            "FIRST_CROSSING_B_ID": "first_crossing_b_001",
            "FIRST_CROSSING_PAIR_SCOPE": "SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "DESCENDANT_BODY_A_ID": "descendant_body_a_001",
            "DESCENDANT_BODY_B_ID": "descendant_body_b_001",
            "DESCENDANT_BODY_PAIR_SCOPE": "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
            "CANDIDATE_A_STANDING_SOURCE_ID": "descendant_body_basis_candidate_a_001",
            "CANDIDATE_B_STANDING_SOURCE_ID": "descendant_body_basis_candidate_b_001",
            "CANDIDATE_A_ROLE": "CANDIDATE_A",
            "CANDIDATE_B_ROLE": "CANDIDATE_B",
            "CANDIDATE_A_STANDING_LABEL": "CANDIDATE_A_STANDING",
            "CANDIDATE_B_STANDING_LABEL": "CANDIDATE_B_STANDING",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_FIRST_CROSSING_SUPPORTED_REQUIRED",
            "PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_CROSSING_AUTHORIZED_REQUIRED",
            "PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED",
            "PRIOR_CROSSING_PERFORMED_REQUIRED",
            "PRIOR_FIRST_CROSSING_A_RECORDED_REQUIRED",
            "PRIOR_FIRST_CROSSING_B_RECORDED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_relation_boundary_v0_min"))
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_REQUIRES_FIRST_CROSSING,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        for code in (
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "RELATION_BOUNDARY_SPEC_REFERENCE_MISSING",
            "FIRST_CROSSING_MISSING_OR_INSUFFICIENT",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_RELATION_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )

    def test_synthetic_allowed_result_and_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_boundary_v0_min(request)
            self.assert_allowed_boundary_shape(result)
            self.assertGreater(result["relation_boundary_summary"]["passed_check_count"], 0)
            for field in (
                "relation_boundary_metadata",
                "declared_relation_boundary_basis",
                "upstream_basis",
                "relation_boundary",
                "relation_boundary_material",
                "relation_boundary_checks",
                "relation_boundary_statement",
                "relation_boundary_non_meaning",
                "boundary_result_detail",
                "permitted_future_route",
                "blocked_routes",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "relation_boundary_summary",
            ):
                self.assertIn(field, result)
            self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_first_crossing"], [])
            material = result["relation_boundary_material"]
            self.assertEqual(set(material), {
                "first_crossing_operation_reference",
                "first_crossing_pair_reference",
                "relation_boundary_evaluation",
            })
            operation = material["first_crossing_operation_reference"]
            self.assertEqual(operation["prior_first_crossing_operation_type"], "FIRST_CROSSING_OPERATION")
            self.assertEqual(operation["prior_first_crossing_operation_outcome"], "FIRST_CROSSING_OPERATION_RECORDED")
            self.assertEqual(operation["prior_first_crossing_result"], "FIRST_CROSSING_SUPPORTED")
            for field in (
                "prior_first_crossing_supported",
                "prior_first_crossing_authorized",
                "prior_crossing_authorized",
                "prior_first_crossing_performed",
                "prior_crossing_performed",
                "prior_first_crossing_a_recorded",
                "prior_first_crossing_b_recorded",
            ):
                self.assertIs(operation[field], True, field)
            pair = material["first_crossing_pair_reference"]
            self.assertEqual(pair["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
            self.assertEqual(pair["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
            self.assertEqual(pair["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
            for field in (
                "first_crossing_a_recorded",
                "first_crossing_b_recorded",
                "first_crossing_supported",
                "first_crossing_pair_non_hierarchy_preserved",
                "first_crossings_remain_sibling",
            ):
                self.assertIs(pair[field], True, field)
            for field in (
                "first_crossing_is_relation",
                "first_crossing_is_coupling",
                "first_crossing_is_presence",
                "first_crossing_is_identity",
                "first_crossing_is_standing_descendant",
                "first_crossing_is_descendant_standing",
                "coupling_created",
            ):
                self.assertIs(pair[field], False, field)
            evaluation = material["relation_boundary_evaluation"]
            self.assertIs(evaluation["relation_operation_consideration_allowed"], True)
            for field in (
                "relation_authorized",
                "relation_created",
                "relation_operation_performed",
                "coupling_created",
                "presence_established",
                "identity_created",
                "follow_on_authorized",
                "follow_on_work_authorized",
            ):
                self.assertIs(evaluation[field], False, field)

    def test_default_live_request_if_references_exist(self) -> None:
        request = resolver.build_relation_boundary_v0_min_request()
        references = [request["relation_boundary_spec_reference"]]
        references.extend(request[item[0]] for item in resolver.UPSTREAM_REQUIREMENTS)
        resolved = [
            Path(reference) if Path(reference).is_absolute() else REPO_ROOT / reference
            for reference in references
        ]
        if not all(path.is_file() for path in resolved):
            self.skipTest("required default relation-boundary references are unavailable")
        result = resolver.resolve_relation_boundary_v0_min(request)
        self.assert_allowed_boundary_shape(result)
        self.assertTrue(
            all(value is True for key, value in result["relation_boundary"].items() if key.endswith("markers_present"))
        )

    def test_missing_or_insufficient_basis_returns_bounded_outcome(self) -> None:
        cases = (
            ("first_crossing_missing", "first_crossing_operation_v2_terminal_summary_reference", None),
            ("first_crossing_outcome", "first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_OPERATION_RECORDED"),
            ("first_crossing_result", "first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
            ("first_crossing_support", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_supported = true"),
            ("first_crossing_authorized", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_authorized = true"),
            ("crossing_authorized", "first_crossing_operation_v2_terminal_summary_reference", "crossing_authorized = true"),
            ("first_crossing_performed", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_performed = true"),
            ("crossing_performed", "first_crossing_operation_v2_terminal_summary_reference", "crossing_performed = true"),
            ("first_crossing_a_recorded", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_a_recorded = true"),
            ("first_crossing_b_recorded", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_b_recorded = true"),
            ("first_crossing_pair_statement", "first_crossing_operation_v2_terminal_summary_reference", "First Crossing A and First Crossing B were evaluated, supported, authorized, performed, and recorded as first-crossing records only"),
            ("first_crossing_non_conversion", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not relation"),
            ("first_crossing_not_coupling", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not coupling"),
            ("first_crossing_not_presence", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not presence"),
            ("first_crossing_not_identity", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not identity"),
            ("first_crossing_not_follow_on", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not follow-on authorization"),
            ("first_crossing_not_follow_on_work", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not follow-on work authorization"),
            ("first_crossing_not_standing_descendant", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not standing descendant"),
            ("first_crossing_not_descendant_standing", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not descendant standing"),
            ("crossing_not_relation_creation", "first_crossing_operation_v2_terminal_summary_reference", "crossing authorization is not relation creation"),
            ("crossing_performance_not_relation_creation", "first_crossing_operation_v2_terminal_summary_reference", "crossing performance is not relation creation"),
            ("first_crossing_false_posture", "first_crossing_operation_v2_terminal_summary_reference", "relation_created = false"),
            ("first_crossing_coupling_false", "first_crossing_operation_v2_terminal_summary_reference", "coupling_created = false"),
            ("first_crossing_presence_false", "first_crossing_operation_v2_terminal_summary_reference", "presence_established = false"),
            ("first_crossing_identity_false", "first_crossing_operation_v2_terminal_summary_reference", "identity_created = false"),
            ("first_crossing_standing_false", "first_crossing_operation_v2_terminal_summary_reference", "standing_descendant_created = false"),
            ("first_crossing_descendant_check_false", "first_crossing_operation_v2_terminal_summary_reference", "descendant_standing_check_performed = false"),
            ("first_crossing_follow_on_false", "first_crossing_operation_v2_terminal_summary_reference", "follow_on_authorized = false"),
            ("first_crossing_follow_on_work_false", "first_crossing_operation_v2_terminal_summary_reference", "follow_on_work_authorized = false"),
            ("boundary_missing", "first_crossing_boundary_terminal_summary_reference", None),
            ("boundary_marker", "first_crossing_boundary_terminal_summary_reference", "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"),
            ("descendant_missing", "descendant_body_creation_operation_terminal_summary_reference", None),
            ("descendant_marker", "descendant_body_creation_operation_terminal_summary_reference", "DESCENDANT_BODY_CREATION_SUPPORTED"),
            ("existence_missing", "existence_claim_evidence_check_terminal_summary_reference", None),
            ("existence_marker", "existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, (name, field, marker) in enumerate(cases):
                with self.subTest(name=name):
                    case_root = root / self.safe_json_filename(name, index).removesuffix(".json")
                    request, paths = self.build_valid_synthetic_request(case_root)
                    if marker is None:
                        request[field] = case_root / "missing" / "unavailable.md"
                    else:
                        original = paths[field].read_text(encoding="utf-8")
                        corrupted = original.replace(marker, "[removed]", 1)
                        # The textual result token is a case-insensitive prefix of
                        # the support field name, so remove both in this fixture.
                        if marker == "FIRST_CROSSING_SUPPORTED":
                            corrupted = corrupted.replace(
                                "first_crossing_supported = true", "[removed]", 1
                            )
                        self.write_markdown(paths[field], corrupted)
                    result = resolver.resolve_relation_boundary_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_REQUIRES_FIRST_CROSSING, resolver.OUTCOME_BLOCKED),
                    )
                    if result["outcome"] == resolver.OUTCOME_REQUIRES_FIRST_CROSSING:
                        self.assert_requires_first_crossing_not_blocked(result)
                        self.assertTrue(
                            result["boundary_result_detail"]["missing_or_insufficient_first_crossing"]
                        )
                    else:
                        self.assert_blocked_with_public_code(result)
                    self.assert_final_refusal_posture(result)

    def test_intent_and_request_shape_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            not_recorded = resolver.resolve_relation_boundary_v0_min(
                {**request, "intent": resolver.INTENT_DO_NOT_RECORD}
            )
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(not_recorded["block"]["blocked"], False)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(not_recorded["relation_boundary"][field], False, field)
            self.assert_final_refusal_posture(not_recorded)

            blocked = resolver.resolve_relation_boundary_v0_min(
                {**request, "intent": resolver.INTENT_BLOCK}
            )
            self.assert_blocked_with_public_code(blocked)
            self.assert_final_refusal_posture(blocked)

            non_mapping = resolver.resolve_relation_boundary_v0_min(["not", "a", "mapping"])
            self.assert_blocked_with_public_code(non_mapping)

            unsupported = resolver.resolve_relation_boundary_v0_min(
                {**request, "intent": "UNSUPPORTED"}
            )
            self.assert_blocked_with_public_code(unsupported)

            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    changed = copy.deepcopy(request)
                    changed[field] = (not expected) if isinstance(expected, bool) else "WRONG_VALUE"
                    result = resolver.resolve_relation_boundary_v0_min(changed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_refusal_posture(result)

    def test_target_marker_class_validation(self) -> None:
        marker_cases = (
            ("identity", "Relation Boundary V0 Minimum Specification"),
            ("basis", "FIRST_CROSSING_OPERATION_RECORDED"),
            ("non_conversion", "first crossing is not follow-on work authorization"),
            ("permitted_result", "RELATION_BOUNDARY_ALLOWED"),
            ("sibling", "Regulation may not become sovereign over Motion"),
            ("permitted_route", "RELATION_BOUNDARY_THEN_RELATION_OPERATION_ONLY"),
            ("contaminated_lineage", "descendant_body_basis_derivation_event_recorded = true"),
            ("blocked_route", "direct relation boundary to relation operation completion"),
            ("closing_lock", "This boundary spec defines only a future relation boundary shape"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, (name, marker) in enumerate(marker_cases):
                with self.subTest(name=name):
                    request, paths = self.build_valid_synthetic_request(root / str(index))
                    text = paths["relation_boundary_spec_reference"].read_text(encoding="utf-8")
                    self.write_markdown(
                        paths["relation_boundary_spec_reference"],
                        text.replace(marker, "[removed]", 1),
                    )
                    result = resolver.resolve_relation_boundary_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "RELATION_BOUNDARY_SPEC_MARKER_MISSING")
                    self.assert_final_refusal_posture(result)

    def test_prohibited_flags_and_false_posture_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            for flag, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    changed = copy.deepcopy(request)
                    changed[flag] = True
                    result = resolver.resolve_relation_boundary_v0_min(changed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), code)
                    self.assert_final_refusal_posture(result)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_field=field):
                    changed = copy.deepcopy(request)
                    changed[field] = True
                    result = resolver.resolve_relation_boundary_v0_min(changed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_refusal_posture(result)

    def test_declared_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(field=field):
                    changed = copy.deepcopy(request)
                    changed["declared_non_claims"][field] = True
                    result = resolver.resolve_relation_boundary_v0_min(changed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_final_refusal_posture(result)
            malformed = (
                None,
                [],
                {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS if key != "relation_created"},
                {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS} | {"relation_created": "false"},
            )
            for declared in malformed:
                with self.subTest(declared_type=type(declared).__name__):
                    changed = copy.deepcopy(request)
                    changed["declared_non_claims"] = declared
                    result = resolver.resolve_relation_boundary_v0_min(changed)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_final_refusal_posture(result)

    def test_path_write_non_mutation_and_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, paths = self.build_valid_synthetic_request(root / "basis")
            request_snapshot = json.dumps(request, sort_keys=True, default=str)
            contents_snapshot = {
                name: path.read_text(encoding="utf-8") for name, path in paths.items()
            }
            request_path = self.write_json(root / "request.json", request)
            result = resolver.resolve_relation_boundary_v0_min_from_path(request_path)
            self.assert_allowed_boundary_shape(result)
            self.assertEqual(json.dumps(request, sort_keys=True, default=str), request_snapshot)
            self.assertEqual(
                {name: path.read_text(encoding="utf-8") for name, path in paths.items()},
                contents_snapshot,
            )
            summary = resolver.build_relation_boundary_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
            self.assertEqual(summary["relation_boundary_result"], "RELATION_OPERATION_CONSIDERATION_ALLOWED")
            self.assertIs(summary["relation_operation_consideration_allowed"], True)
            self.assertEqual(summary["missing_or_insufficient_first_crossing"], [])
            self.assertTrue(
                summary["selected_relation_boundary_spec_path"].endswith("relation_boundary_spec.md")
            )
            self.assertTrue(
                summary["completed_first_crossing_operation_v2_terminal_summary_path"].endswith(
                    "first_crossing_operation_v2_summary.md"
                )
            )

            output_path = root / "nested" / "relation_boundary_001__relation_boundary_v0_min_result.json"
            first = resolver.write_relation_boundary_v0_min_result(result, output_path)
            second = resolver.write_relation_boundary_v0_min_result(result, output_path)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("relation_boundary_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn("integrity_host_v0_min_coexistence_relation_boundary_v0_min", str(resolver.OUTPUT_ROOT))

            missing = resolver.resolve_relation_boundary_v0_min_from_path(root / "missing.json")
            self.assert_blocked_with_public_code(missing)
            malformed = self.write_markdown(root / "malformed.json", "not json")
            malformed_result = resolver.resolve_relation_boundary_v0_min_from_path(malformed)
            self.assert_blocked_with_public_code(malformed_result)
            array_path = self.write_json(root / "array.json", [])
            array_result = resolver.resolve_relation_boundary_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array_result)

    def test_smoke_valid_synthetic_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_boundary_v0_min(request)
            summary = resolver.build_relation_boundary_v0_min_summary(result)
            self.assert_allowed_boundary_shape(result)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], "resolve_relation_boundary_v0_min")
            self.assertEqual(result["relation_boundary"]["boundary_id"], "relation_boundary_001")
            self.assertEqual(result["relation_boundary"]["boundary_type"], "RELATION_BOUNDARY")
            self.assertEqual(
                set(result["relation_boundary_material"]),
                {
                    "first_crossing_operation_reference",
                    "first_crossing_pair_reference",
                    "relation_boundary_evaluation",
                },
            )


if __name__ == "__main__":
    unittest.main()
