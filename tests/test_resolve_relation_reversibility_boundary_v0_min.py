"""Tests for one bounded relation-reversibility boundary.

The boundary can record only consideration for a separately bounded relation
reversibility operation.  It neither performs reversibility nor converts the
historical relation record into living state, presence, identity, coupling,
runtime, or downstream authorization.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_reversibility_boundary_v0_min as resolver


RELATION_OPERATION_MARKERS = (
    "RELATION_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 252",
    "RELATION_SUPPORTED",
    "relation_supported = true",
    "relation_authorized = true",
    "relation_created = true",
    "relation_operation_performed = true",
    "relation_recorded = true",
    "first_crossing_a_used_as_relation_basis = true",
    "first_crossing_b_used_as_relation_basis = true",
    "first_crossing_pair_used_as_relation_basis = true",
    "Relation was supported, authorized, created, performed, and recorded as one relation record between separate first-crossing records only",
    "Relation is not FIELD machinery",
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
    "First crossing remains prior basis only",
    "is not erased",
    "field_machinery_created = false",
    "runtime_created = false",
    "api_created = false",
    "currentness_created = false",
    "authority_created = false",
    "coupling_created = false",
    "presence_established = false",
    "identity_created = false",
    "standing_descendant_created = false",
    "descendant_standing_check_performed = false",
    "follow_on_authorized = false",
    "follow_on_work_authorized = false",
)


class RelationReversibilityBoundaryV0MinTests(unittest.TestCase):
    """Exercise only the local relation-reversibility boundary contract."""

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
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

    def valid_relation_reversibility_boundary_spec_text(self) -> str:
        lines = ["# Relation Reversibility Boundary V0 Minimum Specification", ""]
        for marker_class, variants in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.append(f"## {marker_class}")
            lines.extend(variants[0])
            lines.append("")
        return "\n".join(lines)

    def valid_relation_operation_terminal_summary_text(self) -> str:
        return "\n".join(("# Relation Operation Terminal Summary V0", *RELATION_OPERATION_MARKERS, ""))

    def valid_relation_boundary_terminal_summary_text(self) -> str:
        return "# Relation Boundary Terminal Summary V0\nRELATION_OPERATION_CONSIDERATION_ALLOWED\n"

    def valid_first_crossing_operation_v2_terminal_summary_text(self) -> str:
        return "# First Crossing Operation V2 Terminal Summary V0\nFIRST_CROSSING_SUPPORTED\n"

    def valid_existence_claim_evidence_check_terminal_summary_text(self) -> str:
        return "\n".join(
            (
                "# Existence Claim Evidence Check Terminal Summary V0",
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "",
            )
        )

    def build_valid_synthetic_request(
        self,
        root: Path,
        text_overrides: Mapping[str, str] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Path]]:
        texts = {
            "relation_reversibility_boundary_spec_reference": self.valid_relation_reversibility_boundary_spec_text(),
            "relation_operation_terminal_summary_reference": self.valid_relation_operation_terminal_summary_text(),
            "relation_boundary_terminal_summary_reference": self.valid_relation_boundary_terminal_summary_text(),
            "first_crossing_operation_v2_terminal_summary_reference": self.valid_first_crossing_operation_v2_terminal_summary_text(),
            "existence_claim_evidence_check_terminal_summary_reference": self.valid_existence_claim_evidence_check_terminal_summary_text(),
        }
        if text_overrides:
            texts.update(text_overrides)
        paths: dict[str, Path] = {}
        for index, (field, text) in enumerate(texts.items(), 1):
            path = root / "basis" / self.safe_json_filename(field, index).replace(".json", ".md")
            paths[field] = self.write_markdown(path, text)
        request = resolver.build_relation_reversibility_boundary_v0_min_request(
            **{field: str(path) for field, path in paths.items()}
        )
        return request, paths

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code") or block.get("block_code")
        return str(code) if isinstance(code, str) else None

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        value = result.get("relation_reversibility_boundary_checks")
        return [item for item in value if isinstance(item, Mapping)] if isinstance(value, list) else []

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        value = result.get("relation_reversibility_boundary")
        self.assertIsInstance(value, Mapping)
        return value

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_allowed(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_ALLOWED)
        self.assertEqual(result.get("failed_check_count", 0), 0)
        self.assert_not_blocked(result)
        self.assert_canonical_false_non_claims(result)

    def assert_requires_relation(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_RELATION)
        self.assert_not_blocked(result)
        self.assert_canonical_false_non_claims(result)

    def assert_public_block(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(result.get("relation_reversibility_boundary_summary", {}).get("failed_check_count", 0), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_final_safe_posture(result)

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for check in self.checks(result):
            for field in ("block_code", "failure_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIsInstance(code, str)
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False)

    def assert_boundary_separate_from_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for wrapper_field in (
            "outcome",
            "block",
            "non_claims",
            "relation_reversibility_boundary_checks",
            "relation_reversibility_boundary_summary",
            "relation_reversibility_boundary_metadata",
            "relation_reversibility_boundary_material",
            "upstream_basis",
        ):
            self.assertNotIn(wrapper_field, boundary)
        self.assertNotIn("relation_reversibility_boundary_material", boundary)

    def assert_final_safe_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(boundary.get(field), False, field)
        self.assertFalse(boundary.get("presence_boundary_authorized"))
        self.assertFalse(boundary.get("presence_established"))
        self.assertFalse(boundary.get("identity_created"))
        self.assertFalse(boundary.get("follow_on_authorized"))
        self.assertFalse(boundary.get("follow_on_work_authorized"))

    def assert_allowed_boundary_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for field in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(boundary.get(field), True, field)
        self.assertEqual(
            boundary.get("relation_reversibility_boundary_result"),
            "RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED",
        )
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            if field not in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(boundary.get(field), False, field)
        self.assert_boundary_separate_from_wrapper(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_relation_reversibility_boundary_v0_min",
            "resolve_relation_reversibility_boundary_v0_min_from_path",
            "write_relation_reversibility_boundary_v0_min_result",
            "build_relation_reversibility_boundary_v0_min_summary",
            "build_relation_reversibility_boundary_v0_min_request",
            "build_declared_relation_reversibility_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_relation_reversibility_boundary_v0_min",
            "BOUNDARY_ID": "relation_reversibility_boundary_001",
            "BOUNDARY_TYPE": "RELATION_REVERSIBILITY_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": "CONSIDER_RELATION_REVERSIBILITY_AFTER_RELATION_SUPPORT_BEFORE_PRESENCE_ONLY",
            "PRIOR_RELATION_OPERATION_TYPE": "RELATION_OPERATION",
            "PRIOR_RELATION_OPERATION_OUTCOME_REQUIRED": "RELATION_OPERATION_RECORDED",
            "PRIOR_RELATION_RESULT_REQUIRED": "RELATION_SUPPORTED",
            "ADMISSIBLE_FUTURE_ROUTE": "RELATION_REVERSIBILITY_BOUNDARY_THEN_RELATION_REVERSIBILITY_OPERATION_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_REVERSIBILITY_ID": "relation_reversibility_001",
            "RELATION_LAPSE_ID": "relation_lapse_001",
            "RELATION_DISSOLUTION_ID": "relation_dissolution_001",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        for name in (
            "PRIOR_RELATION_SUPPORTED_REQUIRED",
            "PRIOR_RELATION_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_CREATED_REQUIRED",
            "PRIOR_RELATION_OPERATION_PERFORMED_REQUIRED",
            "PRIOR_RELATION_RECORDED_REQUIRED",
            "PRIOR_FIRST_CROSSING_A_USED_AS_RELATION_BASIS_REQUIRED",
            "PRIOR_FIRST_CROSSING_B_USED_AS_RELATION_BASIS_REQUIRED",
            "PRIOR_FIRST_CROSSING_PAIR_USED_AS_RELATION_BASIS_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_FIELD_MACHINERY_CREATED_REQUIRED",
            "PRIOR_RUNTIME_CREATED_REQUIRED",
            "PRIOR_API_CREATED_REQUIRED",
            "PRIOR_CURRENTNESS_CREATED_REQUIRED",
            "PRIOR_AUTHORITY_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED",
            "PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_REQUIRES_RELATION,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min"
        ))
        self.assertIn("request_relation_reversibility_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_relation_lapse_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_relation_dissolution_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_relation_erasure", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_relation_mutation", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_relation_invalidation", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_presence_boundary_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_follow_on_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertIn("request_follow_on_work_authorization", resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )

    def test_complete_synthetic_request_records_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
        self.assert_allowed(result)
        self.assertEqual(result.get("result_version"), "0.1.0")
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertGreater(result["relation_reversibility_boundary_summary"]["passed_check_count"], 0)
        for section in (
            "relation_reversibility_boundary_metadata",
            "declared_relation_reversibility_boundary_basis",
            "upstream_basis",
            "relation_reversibility_boundary",
            "relation_reversibility_boundary_material",
            "relation_reversibility_boundary_checks",
            "relation_reversibility_boundary_statement",
            "relation_reversibility_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "relation_reversibility_boundary_summary",
        ):
            self.assertIn(section, result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(boundary["prior_relation_operation_type"], resolver.PRIOR_RELATION_OPERATION_TYPE)
        self.assertEqual(boundary["prior_relation_operation_outcome_required"], resolver.PRIOR_RELATION_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(boundary["prior_relation_result_required"], resolver.PRIOR_RELATION_RESULT_REQUIRED)
        self.assert_allowed_boundary_posture(result)

    def test_material_shape_and_boundary_separation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
        self.assert_allowed(result)
        material = result["relation_reversibility_boundary_material"]
        self.assertEqual(set(material), {
            "relation_operation_reference",
            "relation_record_reference",
            "relation_reversibility_boundary_evaluation",
        })
        operation = material["relation_operation_reference"]
        for field in (
            "prior_relation_supported",
            "prior_relation_authorized",
            "prior_relation_created",
            "prior_relation_operation_performed",
            "prior_relation_recorded",
            "prior_first_crossing_a_used_as_relation_basis",
            "prior_first_crossing_b_used_as_relation_basis",
            "prior_first_crossing_pair_used_as_relation_basis",
        ):
            self.assertIs(operation[field], True)
        relation = material["relation_record_reference"]
        self.assertEqual(relation["relation_id"], resolver.RELATION_ID)
        self.assertEqual(relation["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
        self.assertEqual(relation["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
        self.assertEqual(relation["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
        self.assertEqual(relation["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
        self.assertIs(relation["relation_record_referenced"], True)
        self.assertIs(relation["relation_is_historical_record_only"], True)
        for field in (
            "relation_is_living_relation_state",
            "relation_record_is_living_relation_state",
            "relation_record_is_presence",
            "relation_record_is_identity",
            "relation_record_is_coupling",
            "relation_record_is_landlord_of_between",
            "relation_record_outranks_first_crossing_a",
            "relation_record_outranks_first_crossing_b",
            "relation_record_outranks_first_crossing_pair",
        ):
            self.assertIs(relation[field], False)
        evaluation = material["relation_reversibility_boundary_evaluation"]
        self.assertIs(evaluation["relation_reversibility_operation_consideration_allowed"], True)
        self.assertEqual(evaluation["relation_reversibility_boundary_result"], "RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED")
        for field, value in evaluation.items():
            if field not in ("relation_reversibility_operation_consideration_allowed", "relation_reversibility_boundary_result"):
                self.assertIs(value, False, field)
        self.assert_boundary_separate_from_wrapper(result)

    def test_default_live_repo_target_records_allowed_if_present(self) -> None:
        default_references = (
            resolver.DEFAULT_RELATION_REVERSIBILITY_BOUNDARY_SPEC_REFERENCE,
            resolver.DEFAULT_RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_RELATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        )
        if not all((REPO_ROOT / reference).is_file() for reference in default_references):
            self.skipTest("required default relation-reversibility boundary bases are not present")
        result = resolver.resolve_relation_reversibility_boundary_v0_min()
        self.assert_allowed(result)
        self.assert_allowed_boundary_posture(result)
        self.assertIs(result["relation_reversibility_boundary"]["relation_reversibility_authorized"], False)
        self.assertIs(result["relation_reversibility_boundary"]["relation_lapse_authorized"], False)
        self.assertIs(result["relation_reversibility_boundary"]["relation_dissolution_authorized"], False)

    def test_missing_relation_support_requires_relation_or_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, marker in enumerate(RELATION_OPERATION_MARKERS, 1):
                with self.subTest(marker=marker):
                    bad_text = self.valid_relation_operation_terminal_summary_text().replace(marker, "missing marker", 1)
                    if marker == "RELATION_SUPPORTED":
                        # The resolver uses substring markers; remove the exact
                        # support posture as well so this is a real evidence lapse.
                        bad_text = bad_text.replace("relation_supported = true", "relation_supported = false", 1)
                    request, _ = self.build_valid_synthetic_request(
                        root / f"marker_{index:03d}",
                        {"relation_operation_terminal_summary_reference": bad_text},
                    )
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_RELATION, resolver.OUTCOME_BLOCKED))
                    self.assert_all_emitted_codes_public(result)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_final_safe_posture(result)
            request, paths = self.build_valid_synthetic_request(root / "missing_relation_summary")
            paths["relation_operation_terminal_summary_reference"].unlink()
            result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
            self.assert_requires_relation(result)
            self.assertTrue(result["boundary_result_detail"]["missing_or_insufficient_relation"])

    def test_intent_outcomes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_relation_reversibility_boundary_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_final_safe_posture(result)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            blocked_result = resolver.resolve_relation_reversibility_boundary_v0_min(blocked)
            self.assert_public_block(blocked_result)

    def test_request_shape_and_exact_fields_block(self) -> None:
        self.assert_public_block(resolver.resolve_relation_reversibility_boundary_v0_min(["not", "a", "mapping"]))
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            unsupported = copy.deepcopy(request)
            unsupported["intent"] = "UNSUPPORTED_RELATION_REVERSIBILITY_BOUNDARY_INTENT"
            self.assert_public_block(resolver.resolve_relation_reversibility_boundary_v0_min(unsupported))
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = (not expected) if isinstance(expected, bool) else f"wrong_{field}"
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(malformed)
                    self.assert_public_block(result)
                    self.assertEqual(self.block_code(result), "REQUEST_VALUE_MISMATCH")

    def test_marker_validation_behavior(self) -> None:
        marker_cases = (
            ("relation_reversibility_boundary_spec_reference", "Relation Reversibility Boundary V0 Minimum Specification"),
            ("relation_operation_terminal_summary_reference", "RELATION_OPERATION_RECORDED"),
            ("relation_boundary_terminal_summary_reference", "RELATION_OPERATION_CONSIDERATION_ALLOWED"),
            ("first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
            ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, (field, marker) in enumerate(marker_cases, 1):
                with self.subTest(field=field):
                    texts = {
                        "relation_reversibility_boundary_spec_reference": self.valid_relation_reversibility_boundary_spec_text(),
                        "relation_operation_terminal_summary_reference": self.valid_relation_operation_terminal_summary_text(),
                        "relation_boundary_terminal_summary_reference": self.valid_relation_boundary_terminal_summary_text(),
                        "first_crossing_operation_v2_terminal_summary_reference": self.valid_first_crossing_operation_v2_terminal_summary_text(),
                        "existence_claim_evidence_check_terminal_summary_reference": self.valid_existence_claim_evidence_check_terminal_summary_text(),
                    }
                    texts[field] = texts[field].replace(marker, "marker removed")
                    request, _ = self.build_valid_synthetic_request(root / f"marker_{index:03d}", texts)
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_RELATION, resolver.OUTCOME_BLOCKED))
                    self.assert_all_emitted_codes_public(result)
                    self.assert_canonical_false_non_claims(result)
                    self.assert_final_safe_posture(result)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    prohibited = copy.deepcopy(request)
                    prohibited[flag] = True
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(prohibited)
                    self.assert_public_block(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_false_posture_and_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = True
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(malformed)
                    self.assert_public_block(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_non_claim=field):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][field] = True
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(malformed)
                    self.assert_public_block(result)
                    self.assertEqual(result["non_claims"][field], False)
            for declared in (None, [], {"relation_reversibility_authorized": False}, {field: "false" for field in resolver.REQUIRED_FALSE_NON_CLAIMS}):
                with self.subTest(declared_type=type(declared).__name__):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"] = declared
                    result = resolver.resolve_relation_reversibility_boundary_v0_min(malformed)
                    self.assert_public_block(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _ = self.build_valid_synthetic_request(root / "basis")
            request_path = root / self.safe_json_filename("valid request")
            request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")
            result = resolver.resolve_relation_reversibility_boundary_v0_min_from_path(request_path)
            self.assert_allowed(result)
            for name, payload, expected_code in (
                ("missing", None, "REQUEST_PATH_UNREADABLE"),
                ("malformed", "{not json", "REQUEST_JSON_INVALID"),
                ("array", [], "REQUEST_NOT_MAPPING"),
            ):
                with self.subTest(case=name):
                    path = root / self.safe_json_filename(name)
                    if payload is not None:
                        path.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
                    malformed_result = resolver.resolve_relation_reversibility_boundary_v0_min_from_path(path)
                    self.assert_public_block(malformed_result)
                    self.assertEqual(self.block_code(malformed_result), expected_code)
            output_path = root / "out" / "relation_reversibility_boundary_v0_min_result.json"
            first = resolver.write_relation_reversibility_boundary_v0_min_result(result, output_path)
            second = resolver.write_relation_reversibility_boundary_v0_min_result(result, output_path)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn("relation_reversibility_boundary_v0_min_result", first.name)
            default_output = resolver.REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            self.assertIn("integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min", str(default_output))
            forbidden_roots = (
                "relation_operation_v0_min",
                "relation_boundary_v0_min",
                "first_crossing_operation_v0_min",
                "first_crossing_boundary_v0_min",
                "runtime",
                "daemon",
                "presence",
                "identity",
                "externalization",
            )
            self.assertFalse(any(default_output.parent.name.endswith(root_name) for root_name in forbidden_roots))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths = self.build_valid_synthetic_request(Path(directory))
            request["hostile_payload"] = {"raw": "DO_NOT_RETURN_OR_ACT_ON_THIS", "nested": [False, {"value": 1}]}
            before_request = copy.deepcopy(request)
            before_files = {field: path.read_text(encoding="utf-8") for field, path in paths.items()}
            resolver.resolve_relation_reversibility_boundary_v0_min(request)
            self.assertEqual(request, before_request)
            for field, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), before_files[field])

    def test_summary_and_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.build_valid_synthetic_request(Path(directory))
            result = resolver.resolve_relation_reversibility_boundary_v0_min(request)
            summary = resolver.build_relation_reversibility_boundary_v0_min_summary(result)
        self.assert_allowed(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(summary["relation_reversibility_boundary_result"], "RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED")
        self.assertIs(summary["relation_reversibility_operation_consideration_allowed"], True)
        self.assertIs(summary["relation_operation_referenced"], True)
        self.assertIs(summary["relation_record_referenced"], True)
        self.assertIs(summary["relation_basis_referenced"], True)
        self.assertEqual(summary["missing_or_insufficient_relation"], [])
        self.assertTrue(any(key.endswith("markers_present") and value is True for key, value in summary.items()))
        self.assert_allowed_boundary_posture(result)


if __name__ == "__main__":
    unittest.main()
