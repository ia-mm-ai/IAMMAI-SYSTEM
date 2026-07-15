"""Bounded tests for one local relation operation.

The synthetic fixtures model only the declared relation-boundary and
first-crossing basis.  They do not discover repository state or turn relation
into FIELD machinery, coupling, presence, identity, standing, or downstream
authorization.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_operation_v0_min as resolver


class RelationOperationV0MinTests(unittest.TestCase):
    """Exercise one relation record between separate first-crossing records."""

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
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

    def _write_json(self, path: Path, payload: object) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _relation_operation_spec_text(self) -> str:
        return "\n".join(
            (
                "# Relation Operation V0 Minimum Specification",
                "RELATION_OPERATION",
                "relation_operation_001",
                "EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY",
                "RELATION_BOUNDARY_ALLOWED",
                "RELATION_OPERATION_CONSIDERATION_ALLOWED",
                "relation_operation_consideration_allowed = true",
                "first_crossing_operation_referenced = true",
                "first_crossing_a_referenced = true",
                "first_crossing_b_referenced = true",
                "first_crossing_pair_referenced = true",
                "relation_authorized = false",
                "relation_created = false",
                "relation_operation_performed = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "first crossing is not relation",
                "crossing authorization is not relation creation",
                "crossing performance is not relation creation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
                "relation_evaluation",
                "relation_basis_evaluation",
                "relation_pair_evaluation",
                "relation_001",
                "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
                "RELATION_SUPPORTED",
                "relation_supported = true",
                "relation_authorized = true",
                "relation_created = true",
                "relation_operation_performed = true",
                "relation_recorded = true",
                "first_crossing_a_used_as_relation_basis = true",
                "first_crossing_b_used_as_relation_basis = true",
                "first_crossing_pair_used_as_relation_basis = true",
                "Relation operation spec is not relation operation result",
                "Relation operation permission is not relation creation",
                "Relation creation, if later supported, is not FIELD machinery",
                "Relation is not runtime",
                "Relation is not API",
                "Relation is not currentness",
                "Relation is not authority",
                "Relation is not coupling",
                "Relation is not presence",
                "Relation is not identity",
                "Relation is not follow-on authorization",
                "Relation is not follow-on work authorization",
                "Relation is not standing descendant",
                "Relation is not descendant standing",
                "Relation is not presence-bearing",
                "Relation is not identity-bearing",
                "Relation does not assign coupling",
                "Relation does not create coupling",
                "Relation does not admit a third candidate",
                "Relation does not admit a third model",
                "Relation does not establish presence",
                "Relation does not create identity",
                "First crossing remains prior basis",
                "First crossing is not erased by relation",
                "Crossing authorization and performance are not relation creation",
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
                "RELATION_OPERATION_THEN_PRESENCE_BOUNDARY_ONLY",
                "Only after a future relation operation records RELATION_SUPPORTED may a separately bounded presence boundary be considered",
                "No later operation is authorized by this operation spec alone",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct relation operation spec to relation operation completion",
                "direct relation boundary allowance to relation without operation",
                "direct first crossing to relation without relation boundary and operation",
                "direct relation to FIELD machinery",
                "direct relation to runtime",
                "direct relation to authority/currentness",
                "direct relation to coupling assignment",
                "direct relation to coupling creation",
                "direct relation to third-candidate route",
                "direct relation to third-model route",
                "direct relation to presence",
                "direct relation to identity",
                "direct relation to standing descendant",
                "direct relation to descendant standing",
                "direct relation to output/action",
                "direct relation to follow-on work",
                "repository scan route",
                "file discovery route",
                "affected-file repair route",
                "prior unsupported-claim validation route",
                "This operation spec defines only a future relation operation shape",
                "It does not authorize relation",
                "Relation, if later supported, is not FIELD machinery",
                "First crossing remains prior basis only",
                "Open means not scheduled, not authorized, and not executed",
            )
        )

    def _relation_boundary_text(self) -> str:
        return "\n".join(
            (
                "RELATION_BOUNDARY_ALLOWED",
                "failed_check_count = 0",
                "passed_check_count = 250",
                "RELATION_OPERATION_CONSIDERATION_ALLOWED",
                "relation_operation_consideration_allowed = true",
                "first_crossing_operation_referenced = true",
                "first_crossing_a_referenced = true",
                "first_crossing_b_referenced = true",
                "first_crossing_pair_referenced = true",
                "relation_authorized = false",
                "relation_created = false",
                "relation_operation_performed = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
            )
        )

    def _first_crossing_operation_text(self) -> str:
        return "\n".join(
            (
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "first crossing is not relation",
                "crossing authorization is not relation creation",
                "crossing performance is not relation creation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
            )
        )

    def _first_crossing_boundary_text(self) -> str:
        return "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED\n"

    def _existence_claim_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        )

    def _synthetic_request(self, root: Path) -> tuple[dict[str, object], dict[str, Path]]:
        paths = {
            "relation_operation_spec_reference": root / "relation_operation_spec.md",
            "relation_boundary_terminal_summary_reference": root / "relation_boundary.md",
            "first_crossing_operation_v2_terminal_summary_reference": root / "first_crossing_operation_v2.md",
            "first_crossing_boundary_terminal_summary_reference": root / "first_crossing_boundary.md",
            "existence_claim_evidence_check_terminal_summary_reference": root / "existence_claim.md",
        }
        contents = {
            "relation_operation_spec_reference": self._relation_operation_spec_text(),
            "relation_boundary_terminal_summary_reference": self._relation_boundary_text(),
            "first_crossing_operation_v2_terminal_summary_reference": self._first_crossing_operation_text(),
            "first_crossing_boundary_terminal_summary_reference": self._first_crossing_boundary_text(),
            "existence_claim_evidence_check_terminal_summary_reference": self._existence_claim_text(),
        }
        for key, path in paths.items():
            self._write_text(path, contents[key])
        request = resolver.build_relation_operation_v0_min_request(
            **{key: str(path) for key, path in paths.items()}
        )
        return request, paths

    def _block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def _failed_check_count(self, result: dict[str, object]) -> int:
        checks = result.get("relation_operation_checks")
        if not isinstance(checks, list):
            return 0
        return sum(item.get("passed") is False for item in checks if isinstance(item, dict))

    def _assert_all_codes_public(self, result: dict[str, object]) -> None:
        checks = result.get("relation_operation_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, dict)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def _assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def _operation(self, result: dict[str, object]) -> dict[str, object]:
        operation = result.get("relation_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def _assert_operation_is_not_wrapper(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for key in (
            "outcome",
            "block",
            "relation_operation_checks",
            "relation_operation_material",
            "relation_operation_summary",
            "relation_operation_metadata",
            "non_claims",
        ):
            self.assertNotIn(key, operation)

    def _assert_not_blocked(self, result: dict[str, object], outcome: str) -> None:
        self.assertEqual(result["outcome"], outcome)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def _assert_recorded_not_blocked(self, result: dict[str, object]) -> None:
        self._assert_not_blocked(result, resolver.OUTCOME_RECORDED)

    def _assert_requires_boundary_allowance_not_blocked(
        self, result: dict[str, object]
    ) -> None:
        self._assert_not_blocked(result, resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE)

    def _assert_not_recorded_not_blocked(self, result: dict[str, object]) -> None:
        self._assert_not_blocked(result, resolver.OUTCOME_NOT_RECORDED)

    def _assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self._block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self._failed_check_count(result), 0)
        self._assert_all_codes_public(result)
        self._assert_non_claims_false(result)
        self._assert_safe_final_posture(result)

    def _assert_safe_final_posture(self, result: dict[str, object]) -> None:
        operation = self._operation(result)
        for key in (
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
        ):
            self.assertIs(operation[key], False, key)

    def _assert_recorded(self, result: dict[str, object]) -> None:
        self._assert_recorded_not_blocked(result)
        self.assertEqual(self._failed_check_count(result), 0)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["resolver_module"], "resolve_relation_operation_v0_min")
        operation = self._operation(result)
        self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["relation_result"], "RELATION_SUPPORTED")
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[field], True, field)
        self.assertTrue(
            all(value is True for key, value in operation.items() if key.endswith("_markers_present"))
        )
        self._assert_safe_final_posture(result)
        self._assert_non_claims_false(result)
        self._assert_operation_is_not_wrapper(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relation_operation_v0_min",
            "resolve_relation_operation_v0_min_from_path",
            "write_relation_operation_v0_min_result",
            "build_relation_operation_v0_min_summary",
            "build_relation_operation_v0_min_request",
            "build_declared_relation_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_relation_operation_v0_min",
            "OPERATION_ID": "relation_operation_001",
            "OPERATION_TYPE": "RELATION_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY",
            "PRIOR_RELATION_BOUNDARY_TYPE": "RELATION_BOUNDARY",
            "PRIOR_RELATION_BOUNDARY_OUTCOME_REQUIRED": "RELATION_BOUNDARY_ALLOWED",
            "PRIOR_RELATION_BOUNDARY_RESULT_REQUIRED": "RELATION_OPERATION_CONSIDERATION_ALLOWED",
            "ADMISSIBLE_FUTURE_ROUTE": "RELATION_OPERATION_THEN_PRESENCE_BOUNDARY_ONLY",
            "FIRST_CROSSING_A_ID": "first_crossing_a_001",
            "FIRST_CROSSING_B_ID": "first_crossing_b_001",
            "FIRST_CROSSING_PAIR_SCOPE": "SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_RELATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED",
            "PRIOR_FIRST_CROSSING_OPERATION_REFERENCED_REQUIRED",
            "PRIOR_FIRST_CROSSING_A_REFERENCED_REQUIRED",
            "PRIOR_FIRST_CROSSING_B_REFERENCED_REQUIRED",
            "PRIOR_FIRST_CROSSING_PAIR_REFERENCED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_RELATION_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_RELATION_OPERATION_PERFORMED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertTrue(set(resolver.OUTCOME_FAMILY) >= {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            resolver.OUTCOME_BLOCKED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_relation_operation_v0_min"
        ))
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertTrue(set(resolver.BLOCK_CODES))

    def test_synthetic_recorded_operation_and_wrapper_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            result = resolver.resolve_relation_operation_v0_min(request)
        self._assert_recorded(result)
        for key in (
            "relation_operation_metadata",
            "declared_relation_operation_basis",
            "upstream_basis",
            "relation_operation",
            "relation_operation_material",
            "relation_operation_checks",
            "relation_operation_statement",
            "relation_operation_non_meaning",
            "relation_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "relation_operation_summary",
        ):
            self.assertIn(key, result)
        operation = self._operation(result)
        self.assertEqual(operation["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
        self.assertEqual(operation["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
        self.assertEqual(operation["relation_id"], resolver.RELATION_ID)
        self.assertEqual(operation["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
        self.assertGreater(len(result["relation_operation_checks"]), 0)
        self._assert_all_codes_public(result)

    def test_relation_operation_material_has_exact_bounded_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            result = resolver.resolve_relation_operation_v0_min(request)
        self._assert_recorded(result)
        material = result["relation_operation_material"]
        self.assertIsInstance(material, dict)
        self.assertEqual(set(material), {
            "relation_evaluation",
            "relation_basis_evaluation",
            "relation_pair_evaluation",
        })
        evaluation = material["relation_evaluation"]
        basis = material["relation_basis_evaluation"]
        pair = material["relation_pair_evaluation"]
        for key in (
            "relation_supported",
            "relation_authorized",
            "relation_created",
            "relation_operation_performed",
            "relation_recorded",
        ):
            self.assertIs(evaluation[key], True)
        for key in (
            "first_crossing_a_used_as_relation_basis",
            "first_crossing_b_used_as_relation_basis",
            "first_crossing_pair_used_as_relation_basis",
        ):
            self.assertIs(basis[key], True)
        self.assertEqual(basis["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
        self.assertEqual(basis["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
        self.assertEqual(basis["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
        for key in (
            "first_crossing_a_is_relation",
            "first_crossing_b_is_relation",
            "first_crossing_pair_is_relation",
            "crossing_authorization_is_relation_creation",
            "crossing_performance_is_relation_creation",
            "first_crossing_is_coupling",
            "first_crossing_is_presence",
            "first_crossing_is_identity",
        ):
            self.assertIs(basis[key], False, key)
        self.assertEqual(pair["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
        for key in (
            "first_crossings_remain_sibling",
            "first_crossing_non_hierarchy_preserved",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "regulation_not_sovereign_over_motion",
            "motion_does_not_erase_regulation",
        ):
            self.assertIs(pair[key], True, key)
        for key in (
            "coupling_assigned",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "presence_established",
            "identity_created",
            "standing_descendant_created",
            "descendant_standing_check_performed",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(pair[key], False, key)

    def test_default_live_target_records_if_all_references_exist(self) -> None:
        request = resolver.build_relation_operation_v0_min_request()
        references = [
            request["relation_operation_spec_reference"],
            request["relation_boundary_terminal_summary_reference"],
            request["first_crossing_operation_v2_terminal_summary_reference"],
            request["first_crossing_boundary_terminal_summary_reference"],
            request["existence_claim_evidence_check_terminal_summary_reference"],
        ]
        if not all((REPO_ROOT / Path(reference)).is_file() for reference in references):
            self.skipTest("default relation-operation references are not all present")
        result = resolver.resolve_relation_operation_v0_min(request)
        self._assert_recorded(result)

    def test_boundary_and_upstream_deficiencies_do_not_record_relation(self) -> None:
        cases = (
            ("missing relation boundary", "relation_boundary_terminal_summary_reference", None),
            ("wrong relation boundary marker", "relation_boundary_terminal_summary_reference", "RELATION_BOUNDARY_ALLOWED"),
            (
                "wrong relation boundary result",
                "relation_boundary_terminal_summary_reference",
                ("RELATION_OPERATION_CONSIDERATION_ALLOWED", "relation_operation_consideration_allowed = true"),
            ),
            ("boundary operation reference", "relation_boundary_terminal_summary_reference", "first_crossing_operation_referenced = true"),
            ("boundary first crossing a reference", "relation_boundary_terminal_summary_reference", "first_crossing_a_referenced = true"),
            ("boundary first crossing b reference", "relation_boundary_terminal_summary_reference", "first_crossing_b_referenced = true"),
            ("boundary pair reference", "relation_boundary_terminal_summary_reference", "first_crossing_pair_referenced = true"),
            ("boundary relation authorized false", "relation_boundary_terminal_summary_reference", "relation_authorized = false"),
            ("boundary relation created false", "relation_boundary_terminal_summary_reference", "relation_created = false"),
            ("boundary relation operation false", "relation_boundary_terminal_summary_reference", "relation_operation_performed = false"),
            ("boundary coupling false", "relation_boundary_terminal_summary_reference", "coupling_created = false"),
            ("boundary presence false", "relation_boundary_terminal_summary_reference", "presence_established = false"),
            ("boundary identity false", "relation_boundary_terminal_summary_reference", "identity_created = false"),
            ("boundary follow-on false", "relation_boundary_terminal_summary_reference", "follow_on_authorized = false"),
            ("boundary follow-on work false", "relation_boundary_terminal_summary_reference", "follow_on_work_authorized = false"),
            ("missing crossing operation", "first_crossing_operation_v2_terminal_summary_reference", None),
            (
                "missing crossing support",
                "first_crossing_operation_v2_terminal_summary_reference",
                ("FIRST_CROSSING_SUPPORTED", "first_crossing_supported = true"),
            ),
            ("crossing authorized", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_authorized = true"),
            ("crossing authorization", "first_crossing_operation_v2_terminal_summary_reference", "crossing_authorized = true"),
            ("crossing performed", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_performed = true"),
            ("crossing performance", "first_crossing_operation_v2_terminal_summary_reference", "crossing_performed = true"),
            ("crossing a recorded", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_a_recorded = true"),
            ("crossing b recorded", "first_crossing_operation_v2_terminal_summary_reference", "first_crossing_b_recorded = true"),
            ("crossing not relation", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not relation"),
            ("authorization not relation", "first_crossing_operation_v2_terminal_summary_reference", "crossing authorization is not relation creation"),
            ("performance not relation", "first_crossing_operation_v2_terminal_summary_reference", "crossing performance is not relation creation"),
            ("crossing not coupling", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not coupling"),
            ("crossing not presence", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not presence"),
            ("crossing not identity", "first_crossing_operation_v2_terminal_summary_reference", "first crossing is not identity"),
            ("missing crossing boundary", "first_crossing_boundary_terminal_summary_reference", None),
            ("missing crossing boundary marker", "first_crossing_boundary_terminal_summary_reference", "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"),
            ("missing evidence summary", "existence_claim_evidence_check_terminal_summary_reference", None),
            ("missing unsupported marker", "existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, (name, field, marker) in enumerate(cases):
                with self.subTest(name=name):
                    case_root = root / self.safe_json_filename(name, index).removesuffix(".json")
                    request, paths = self._synthetic_request(case_root)
                    if marker is None:
                        request[field] = str(case_root / "missing" / "summary.md")
                    else:
                        text = paths[field].read_text(encoding="utf-8")
                        markers = marker if isinstance(marker, tuple) else (marker,)
                        for item in markers:
                            text = text.replace(item, "REMOVED_MARKER", 1)
                        self._write_text(paths[field], text)
                    result = resolver.resolve_relation_operation_v0_min(request)
                    self.assertIn(result["outcome"], {
                        resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                        resolver.OUTCOME_NOT_RECORDED,
                        resolver.OUTCOME_BLOCKED,
                    })
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    self._assert_non_claims_false(result)
                    self._assert_safe_final_posture(result)
                    self._assert_all_codes_public(result)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            skipped = copy.deepcopy(request)
            skipped["intent"] = resolver.INTENT_DO_NOT_RECORD
            skipped_result = resolver.resolve_relation_operation_v0_min(skipped)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            blocked_result = resolver.resolve_relation_operation_v0_min(blocked)
        self._assert_not_recorded_not_blocked(skipped_result)
        self.assertEqual(self._operation(skipped_result)["relation_result"], "NOT_EVALUATED")
        self._assert_safe_final_posture(skipped_result)
        self._assert_non_claims_false(skipped_result)
        self._assert_blocked(blocked_result)
        self.assertEqual(self._block_code(blocked_result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_exact_values_block(self) -> None:
        cases = {
            "unsupported intent": ("intent", "UNSUPPORTED"),
            "operation id": ("operation_id", "wrong"),
            "operation type": ("operation_type", "wrong"),
            "operation version": ("operation_version", "wrong"),
            "operation scope": ("operation_scope", "wrong"),
            "boundary type": ("prior_relation_boundary_type", "wrong"),
            "boundary outcome": ("prior_relation_boundary_outcome_required", "wrong"),
            "boundary result": ("prior_relation_boundary_result_required", "wrong"),
            "boundary consideration": ("prior_relation_operation_consideration_allowed_required", False),
            "operation referenced": ("prior_first_crossing_operation_referenced_required", False),
            "first crossing referenced": ("prior_first_crossing_a_referenced_required", False),
            "second crossing referenced": ("prior_first_crossing_b_referenced_required", False),
            "crossing pair referenced": ("prior_first_crossing_pair_referenced_required", False),
            "prior false posture": ("prior_relation_created_required", True),
            "crossing id": ("first_crossing_a_id", "wrong"),
            "crossing pair scope": ("first_crossing_pair_scope", "wrong"),
            "relation id": ("relation_id", "wrong"),
            "relation pair scope": ("relation_pair_scope", "wrong"),
            "future route": ("admissible_future_route", "wrong"),
        }
        self._assert_blocked(resolver.resolve_relation_operation_v0_min(["not", "a", "mapping"]))
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            for name, (field, value) in cases.items():
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    malformed[field] = value
                    self._assert_blocked(resolver.resolve_relation_operation_v0_min(malformed))

    def test_target_and_upstream_marker_validation(self) -> None:
        cases = (
            ("target operation identity", "relation_operation_spec_reference", "Relation Operation V0 Minimum Specification"),
            (
                "relation boundary class",
                "relation_boundary_terminal_summary_reference",
                ("RELATION_OPERATION_CONSIDERATION_ALLOWED", "relation_operation_consideration_allowed = true"),
            ),
            ("crossing operation class", "first_crossing_operation_v2_terminal_summary_reference", "crossing_performed = true"),
            ("crossing boundary class", "first_crossing_boundary_terminal_summary_reference", "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"),
            ("evidence class", "existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, (name, field, marker) in enumerate(cases):
                with self.subTest(name=name):
                    request, paths = self._synthetic_request(root / f"case_{index:03d}")
                    text = paths[field].read_text(encoding="utf-8")
                    markers = marker if isinstance(marker, tuple) else (marker,)
                    for item in markers:
                        text = text.replace(item, "MISSING", 1)
                    self._write_text(paths[field], text)
                    result = resolver.resolve_relation_operation_v0_min(request)
                    self.assertIn(result["outcome"], {
                        resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                        resolver.OUTCOME_BLOCKED,
                    })
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    self._assert_non_claims_false(result)
                    self._assert_safe_final_posture(result)

    def test_prohibited_flags_and_top_level_preclaims_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    converted = copy.deepcopy(request)
                    converted[flag] = True
                    result = resolver.resolve_relation_operation_v0_min(converted)
                    self._assert_blocked(result)
                    self.assertEqual(self._block_code(result), expected_code)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(preclaim=field):
                    converted = copy.deepcopy(request)
                    converted[field] = True
                    self._assert_blocked(resolver.resolve_relation_operation_v0_min(converted))

    def test_declared_non_claims_are_canonicalized_after_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][field] = True
                    result = resolver.resolve_relation_operation_v0_min(malformed)
                    self._assert_blocked(result)
                    self.assertIs(result["non_claims"][field], False)
            for name, declared in (
                ("missing", None),
                ("non-mapping", []),
                ("required-key-missing", {}),
            ):
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    if declared is None:
                        malformed.pop("declared_non_claims")
                    else:
                        malformed["declared_non_claims"] = declared
                    self._assert_blocked(resolver.resolve_relation_operation_v0_min(malformed))
            malformed = copy.deepcopy(request)
            malformed["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
            self._assert_blocked(resolver.resolve_relation_operation_v0_min(malformed))

    def test_path_write_and_non_mutation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request, paths = self._synthetic_request(root / "basis")
            original_request = copy.deepcopy(request)
            original_texts = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            request_path = self._write_json(root / "request.json", request)
            result = resolver.resolve_relation_operation_v0_min_from_path(request_path)
            self._assert_recorded(result)
            self.assertEqual(request, original_request)
            self.assertEqual(
                {key: path.read_text(encoding="utf-8") for key, path in paths.items()},
                original_texts,
            )
            output = root / "nested" / resolver.DETERMINISTIC_FILENAME
            first = resolver.write_relation_operation_v0_min_result(result, output)
            second = resolver.write_relation_operation_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("relation_operation_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            default_path = resolver.REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            self.assertIn("integrity_host_v0_min_coexistence_relation_operation_v0_min", str(default_path))
            self.assertNotIn("relation_boundary_v0_min", str(first))
            for name, payload in (
                ("missing", None),
                ("malformed", "{not json"),
                ("array", []),
            ):
                with self.subTest(name=name):
                    path = root / self.safe_json_filename(name)
                    if payload is None:
                        result_from_path = resolver.resolve_relation_operation_v0_min_from_path(path)
                    elif isinstance(payload, str):
                        self._write_text(path, payload)
                        result_from_path = resolver.resolve_relation_operation_v0_min_from_path(path)
                    else:
                        self._write_json(path, payload)
                        result_from_path = resolver.resolve_relation_operation_v0_min_from_path(path)
                    self._assert_blocked(result_from_path)

    def test_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self._synthetic_request(Path(temporary))
            snapshot = copy.deepcopy(request)
            result = resolver.resolve_relation_operation_v0_min(request)
            summary = resolver.build_relation_operation_v0_min_summary(result)
        self._assert_recorded(result)
        self.assertEqual(request, snapshot)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_relation_operation_v0_min")
        self.assertEqual(summary["relation_result"], "RELATION_SUPPORTED")
        self.assertEqual(summary["missing_or_insufficient_boundary_allowance"], [])
        self.assertEqual(summary["not_recorded_reasons"], [])
        for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(summary[field], True, field)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            if field not in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(summary[field], False, field)
        self.assertIn("relation_evaluation", result["relation_operation_material"])

    def test_not_supported_and_requires_allowance_summaries(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, paths = self._synthetic_request(Path(temporary))
            unsupported = copy.deepcopy(request)
            unsupported["relation_support_found"] = False
            unsupported_result = resolver.resolve_relation_operation_v0_min(unsupported)
            insufficient = copy.deepcopy(request)
            self._write_text(
                paths["relation_boundary_terminal_summary_reference"],
                "missing relation boundary allowance",
            )
            allowance_result = resolver.resolve_relation_operation_v0_min(insufficient)
        self._assert_not_recorded_not_blocked(unsupported_result)
        self.assertEqual(self._operation(unsupported_result)["relation_result"], "RELATION_NOT_SUPPORTED")
        self.assertEqual(
            resolver.build_relation_operation_v0_min_summary(unsupported_result)["not_recorded_reasons"],
            ["relation_support_found"],
        )
        self._assert_requires_boundary_allowance_not_blocked(allowance_result)
        allowance_summary = resolver.build_relation_operation_v0_min_summary(allowance_result)
        self.assertTrue(allowance_summary["missing_or_insufficient_boundary_allowance"])
        self.assertIs(self._operation(allowance_result)["relation_created"], False)
        self._assert_safe_final_posture(unsupported_result)
        self._assert_safe_final_posture(allowance_result)


if __name__ == "__main__":
    unittest.main()
