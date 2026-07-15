"""Executable boundary tests for the bounded relation-lapse resolver.

These tests exercise one relation-lapse boundary only.  The boundary may
record future lapse-operation consideration after clean reversibility support;
it never performs lapse, conversion, repair, discovery, or downstream work.
"""

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

import resolve_relation_lapse_boundary_v0_min as resolver


TARGET_PRIOR_FALSE_MARKERS = (
    "relation record is not living relation state",
    "living relation state was not created",
    "living relation state did not lapse",
    "living relation state did not dissolve",
    "relation did not lapse",
    "relation did not dissolve",
    "relation was not reversed",
    "relation was not terminated",
    "relation was not erased",
    "relation was not mutated",
    "relation was not invalidated",
    "relation was not punished",
    "teardown logic was not created",
    "historical receipt preservation was not authorized",
    "historical receipt was not preserved",
    "presence boundary is not authorized",
    "presence is not established",
    "identity is not created",
    "coupling remains unassigned and uncreated",
    "no follow-on work is authorized",
)

REVERSIBILITY_MARKERS = (
    "RELATION_REVERSIBILITY_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 339",
    "RELATION_REVERSIBILITY_SUPPORTED",
    "relation_reversibility_supported = true",
    "relation_reversibility_authorized = true",
    "relation_reversibility_performed = true",
    "relation_reversibility_recorded = true",
    "relation_operation_referenced = true",
    "relation_record_referenced = true",
    "relation_basis_referenced = true",
    "relation_record_confirmed_as_historical_only = true",
    *TARGET_PRIOR_FALSE_MARKERS,
)


class RelationLapseBoundaryResolverTests(unittest.TestCase):
    """Verify bounded relation-lapse boundary recording and refusal posture."""

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

    def valid_boundary_spec_text(self) -> str:
        identity = (
            "Relation Lapse Boundary V0 Minimum Specification",
            "RELATION_LAPSE_BOUNDARY",
            "relation_lapse_boundary_001",
            "CONSIDER_RELATION_LAPSE_AFTER_RELATION_REVERSIBILITY_SUPPORT_BEFORE_PRESENCE_ONLY",
        )
        basis = (
            "RELATION_REVERSIBILITY_OPERATION_RECORDED",
            "RELATION_REVERSIBILITY_SUPPORTED",
            "relation_reversibility_supported = true",
            "relation_reversibility_authorized = true",
            "relation_reversibility_performed = true",
            "relation_reversibility_recorded = true",
            "relation_operation_referenced = true",
            "relation_record_referenced = true",
            "relation_basis_referenced = true",
            "relation_record_confirmed_as_historical_only = true",
        )
        outcomes = (
            "RELATION_LAPSE_BOUNDARY_ALLOWED",
            "RELATION_LAPSE_BOUNDARY_REQUIRES_REVERSIBILITY",
            "RELATION_LAPSE_BOUNDARY_BLOCKED",
            "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED",
            "REQUIRES_REVERSIBILITY",
        )
        non_conversion = (
            "Relation lapse boundary is not relation lapse operation",
            "Relation lapse boundary permission is not relation lapse",
            "Relation lapse operation consideration is not relation lapse",
            "Relation lapse operation consideration is not relation dissolution",
            "Relation lapse operation consideration is not relation reversal",
            "Relation lapse operation consideration is not relation termination",
            "Relation lapse operation consideration is not relation erasure",
            "Relation lapse operation consideration is not relation mutation",
            "Relation lapse operation consideration is not relation invalidation",
            "Relation lapse operation consideration is not punishment",
            "Relation lapse operation consideration is not teardown",
            "Relation lapse is not punishment",
            "Relation lapse is not dissolution",
            "Relation lapse is not erasure",
            "Relation lapse is not teardown",
            "Relation lapse is not presence boundary authorization",
            "Relation lapse is not presence",
            "Relation lapse is not identity",
            "Relation lapse is not coupling",
            "Relation lapse is not FIELD machinery",
            "Relation lapse is not runtime",
            "Relation lapse is not currentness",
            "Relation lapse is not authority",
            "Relation lapse is not follow-on authorization",
            "Relation lapse is not follow-on work",
        )
        historical = (
            "Historical relation record is not living relation state",
            "Relation record was confirmed historical-only by relation reversibility operation",
            "Living relation state may not be created by relation lapse boundary",
            "Living relation state may lapse only by separately bounded operation",
            "Historical receipt preservation requires a separately bounded operation",
            "Relation_001 must not become landlord of the between",
            "Relation_001 must not outrank First Crossing A",
            "Relation_001 must not outrank First Crossing B",
            "Relation_001 must not outrank the related first-crossing pair",
            "First Crossing A and First Crossing B remain sibling records",
            "neither first crossing ranks above the other",
            "Descendant Body A and Descendant Body B remain sibling records",
            "neither descendant body ranks above the other",
            "Candidate A and Candidate B remain sibling candidate standings",
            "neither candidate standing ranks above the other",
            "Regulation may not become sovereign over Motion",
            "Motion may not erase Regulation",
            "coupling remains unassigned",
        )
        route = (
            "RELATION_LAPSE_BOUNDARY_THEN_RELATION_LAPSE_OPERATION_ONLY",
            "Only after a future relation lapse boundary records RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED may a separately bounded relation lapse operation be considered",
            "No relation lapse, relation dissolution, presence boundary, or later operation is authorized by this boundary specification alone",
        )
        contaminated = (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        )
        blocked = (
            "direct relation lapse boundary to relation lapse operation completion",
            "direct relation reversibility operation to relation lapse without lapse boundary and operation",
            "direct relation reversibility operation to relation dissolution without dissolution boundary and operation",
            "direct relation reversibility operation to presence boundary without lapse boundary consideration",
            "direct relation lapse boundary to relation lapse",
            "direct relation lapse boundary to relation dissolution",
            "direct relation lapse boundary to relation reversal",
            "direct relation lapse boundary to relation termination",
            "direct relation lapse boundary to relation erasure",
            "direct relation lapse boundary to relation mutation",
            "direct relation lapse boundary to relation invalidation",
            "direct relation lapse boundary to punitive lapse interpretation",
            "direct relation lapse boundary to teardown logic",
            "direct relation lapse boundary to living relation state",
            "direct relation lapse boundary to historical receipt preservation",
            "direct relation lapse boundary to presence boundary authorization",
            "direct relation lapse boundary to presence establishment",
            "direct relation to presence",
            "direct relation to identity",
            "direct relation to coupling assignment",
            "direct relation to coupling creation",
            "direct relation to FIELD machinery",
            "direct relation to runtime",
            "direct relation to authority/currentness",
            "direct relation lapse boundary to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        )
        closing = (
            "This boundary spec defines only a future relation lapse boundary shape",
            "It does not lapse relation",
            "It does not dissolve relation",
            "It does not reverse relation",
            "It does not terminate relation",
            "It does not erase relation",
            "It does not mutate relation_001",
            "Relation lapse boundary is not relation lapse operation",
            "Relation lapse boundary permission is not relation lapse",
            "Relation lapse operation consideration is not relation lapse, relation dissolution, relation reversal, relation termination, relation erasure, relation mutation, relation invalidation, punishment, or teardown",
            "Relation lapse is not punishment, dissolution, erasure, teardown, presence boundary authorization, presence, identity, coupling, FIELD machinery, runtime, currentness, authority, follow-on authorization, or follow-on work",
            "Relation record is historical-only and not living relation state",
            "No presence boundary is authorized by this boundary spec",
            "Open means not scheduled, not authorized, and not executed",
        )
        return "\n".join((*identity, *basis, *TARGET_PRIOR_FALSE_MARKERS, *outcomes, *non_conversion, *historical, *route, *contaminated, *blocked, *closing))

    def valid_reversibility_terminal_summary_text(self) -> str:
        return "\n".join(REVERSIBILITY_MARKERS)

    def valid_relation_operation_terminal_summary_text(self) -> str:
        return "RELATION_OPERATION_RECORDED\nRELATION_SUPPORTED\n"

    def valid_first_crossing_terminal_summary_text(self) -> str:
        return "FIRST_CROSSING_SUPPORTED\n"

    def valid_evidence_terminal_summary_text(self) -> str:
        return "\n".join((
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        ))

    def build_valid_synthetic_request(self, base: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = {
            "relation_lapse_boundary_spec_reference": self.write_markdown(base / "relation_lapse_boundary.md", self.valid_boundary_spec_text()),
            "relation_reversibility_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_reversibility_operation.md", self.valid_reversibility_terminal_summary_text()
            ),
            "relation_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_operation.md", self.valid_relation_operation_terminal_summary_text()
            ),
            "first_crossing_operation_v2_terminal_summary_reference": self.write_markdown(
                base / "first_crossing_operation_v2.md", self.valid_first_crossing_terminal_summary_text()
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(
                base / "existence_claim_evidence.md", self.valid_evidence_terminal_summary_text()
            ),
        }
        request = resolver.build_relation_lapse_boundary_v0_min_request(**{key: str(value) for key, value in paths.items()})
        return request, paths

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        summary = result.get("relation_lapse_boundary_summary")
        self.assertIsInstance(summary, dict)
        return summary["failed_check_count"]

    def assert_allowed(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(self.failed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_requires_reversibility(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_REVERSIBILITY)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        detail = result.get("boundary_result_detail")
        self.assertIsInstance(detail, dict)
        self.assertTrue(detail.get("missing_or_insufficient_reversibility"))

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        records = result.get("relation_lapse_boundary_checks")
        self.assertIsInstance(records, list)
        for record in records:
            self.assertIsInstance(record, dict)
            for key in ("block_code", "failure_code"):
                code = record.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def assert_boundary_has_no_wrapper_fields(self, result: dict[str, Any]) -> None:
        boundary = result.get("relation_lapse_boundary")
        self.assertIsInstance(boundary, dict)
        for key in (
            "outcome",
            "block",
            "relation_lapse_boundary_checks",
            "non_claims",
            "relation_lapse_boundary_summary",
            "relation_lapse_boundary_metadata",
            "relation_lapse_boundary_material",
        ):
            self.assertNotIn(key, boundary)

    def assert_refusal_posture(self, result: dict[str, Any]) -> None:
        boundary = result["relation_lapse_boundary"]
        self.assertIsInstance(boundary, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            if key not in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(boundary.get(key), False, key)
        self.assertFalse(boundary["relation_lapse_authorized"])
        self.assertFalse(boundary["relation_dissolution_authorized"])
        self.assertFalse(boundary["relation_reversed"])
        self.assertFalse(boundary["living_relation_state_created"])
        self.assertFalse(boundary["presence_boundary_authorized"])
        self.assertFalse(boundary["identity_created"])
        self.assertFalse(boundary["follow_on_work_authorized"])

    def assert_allowed_boundary_posture(self, result: dict[str, Any]) -> None:
        self.assert_allowed(result)
        boundary = result["relation_lapse_boundary"]
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(boundary["relation_lapse_boundary_result"], "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED")
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_boundary_has_no_wrapper_fields(result)

    def test_01_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_relation_lapse_boundary_v0_min",
            "resolve_relation_lapse_boundary_v0_min_from_path",
            "write_relation_lapse_boundary_v0_min_result",
            "build_relation_lapse_boundary_v0_min_summary",
            "build_relation_lapse_boundary_v0_min_request",
            "build_declared_relation_lapse_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_relation_lapse_boundary_v0_min")
        self.assertEqual(resolver.BOUNDARY_ID, "relation_lapse_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "RELATION_LAPSE_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.BOUNDARY_SCOPE,
            "CONSIDER_RELATION_LAPSE_AFTER_RELATION_REVERSIBILITY_SUPPORT_BEFORE_PRESENCE_ONLY",
        )
        self.assertEqual(resolver.PRIOR_RELATION_REVERSIBILITY_OPERATION_TYPE, "RELATION_REVERSIBILITY_OPERATION")
        self.assertEqual(resolver.PRIOR_RELATION_REVERSIBILITY_OPERATION_OUTCOME_REQUIRED, "RELATION_REVERSIBILITY_OPERATION_RECORDED")
        self.assertEqual(resolver.PRIOR_RELATION_REVERSIBILITY_RESULT_REQUIRED, "RELATION_REVERSIBILITY_SUPPORTED")
        for name in (
            "PRIOR_RELATION_REVERSIBILITY_SUPPORTED_REQUIRED",
            "PRIOR_RELATION_REVERSIBILITY_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_REVERSIBILITY_PERFORMED_REQUIRED",
            "PRIOR_RELATION_REVERSIBILITY_RECORDED_REQUIRED",
            "PRIOR_RELATION_OPERATION_REFERENCED_REQUIRED",
            "PRIOR_RELATION_RECORD_REFERENCED_REQUIRED",
            "PRIOR_RELATION_BASIS_REFERENCED_REQUIRED",
            "PRIOR_RELATION_RECORD_CONFIRMED_AS_HISTORICAL_ONLY_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_RELATION_RECORD_IS_LIVING_RELATION_STATE_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED",
            "PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_DISSOLUTION_PERFORMED_REQUIRED",
            "PRIOR_RELATION_REVERSED_REQUIRED",
            "PRIOR_RELATION_TERMINATED_REQUIRED",
            "PRIOR_RELATION_ERASED_REQUIRED",
            "PRIOR_RELATION_MUTATED_REQUIRED",
            "PRIOR_RELATION_INVALIDATED_REQUIRED",
            "PRIOR_RELATION_PUNISHED_REQUIRED",
            "PRIOR_RELATION_TEARDOWN_CREATED_REQUIRED",
            "PRIOR_HISTORICAL_RECEIPT_PRESERVATION_AUTHORIZED_REQUIRED",
            "PRIOR_HISTORICAL_RECEIPT_PRESERVED_REQUIRED",
            "PRIOR_PRESENCE_BOUNDARY_AUTHORIZED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_IDENTITY_CREATED_REQUIRED",
            "PRIOR_COUPLING_CREATED_REQUIRED",
            "PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED",
            "PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "RELATION_LAPSE_BOUNDARY_THEN_RELATION_LAPSE_OPERATION_ONLY")
        self.assertEqual(resolver.RELATION_ID, "relation_001")
        self.assertEqual(resolver.RELATION_PAIR_SCOPE, "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY")
        self.assertEqual(resolver.RELATION_LAPSE_ID, "relation_lapse_001")
        self.assertEqual(resolver.RELATION_LAPSE_SCOPE, "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY")
        self.assertEqual(resolver.RELATION_LAPSE_RESULT, "RELATION_LAPSE_SUPPORTED")
        self.assertEqual(resolver.RELATION_DISSOLUTION_ID, "relation_dissolution_001")
        self.assertEqual(resolver.RELATION_DISSOLUTION_SCOPE, "RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_REQUIRES_REVERSIBILITY,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min"))
        for key in (
            "request_relation_lapse_authorization",
            "request_relation_lapse_performed",
            "request_relation_lapse_recorded",
            "request_relation_lapse_supported",
            "request_relation_dissolution_authorization",
            "request_relation_reversal",
            "request_relation_termination",
            "request_relation_erasure",
            "request_relation_mutation",
            "request_relation_invalidation",
            "request_presence_boundary_authorization",
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
        ):
            self.assertIn(key, resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"], "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED")
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"], "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED")
        request = resolver.build_relation_lapse_boundary_v0_min_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        for key in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(request[key], False)

    def test_02_synthetic_complete_boundary_records_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_relation_lapse_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        self.assertGreater(result["relation_lapse_boundary_summary"]["passed_check_count"], 0)
        self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        expected_sections = {
            "relation_lapse_boundary_metadata",
            "declared_relation_lapse_boundary_basis",
            "upstream_basis",
            "relation_lapse_boundary",
            "relation_lapse_boundary_material",
            "relation_lapse_boundary_checks",
            "relation_lapse_boundary_statement",
            "relation_lapse_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "relation_lapse_boundary_summary",
        }
        self.assertTrue(expected_sections.issubset(result))
        self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_reversibility"], [])
        marker_values = {
            value for key, value in result["relation_lapse_boundary"].items() if key.endswith("markers_present")
        }
        self.assertEqual(marker_values, {True})

    def test_03_relation_lapse_boundary_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_relation_lapse_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        material = result["relation_lapse_boundary_material"]
        self.assertEqual(set(material), {
            "relation_reversibility_operation_reference",
            "relation_record_lapse_boundary_reference",
            "relation_lapse_boundary_evaluation",
        })
        reversibility = material["relation_reversibility_operation_reference"]
        for key in (
            "prior_relation_reversibility_supported",
            "prior_relation_reversibility_authorized",
            "prior_relation_reversibility_performed",
            "prior_relation_reversibility_recorded",
            "prior_relation_operation_referenced",
            "prior_relation_record_referenced",
            "prior_relation_basis_referenced",
            "prior_relation_record_confirmed_as_historical_only",
        ):
            self.assertIs(reversibility[key], True)
        for key, value in reversibility.items():
            if key.endswith("_required") or key in {"prior_relation_reversibility_operation_type", "prior_relation_reversibility_operation_outcome", "prior_relation_reversibility_result"}:
                continue
            if key.startswith("prior_") and key not in {
                "prior_relation_reversibility_supported",
                "prior_relation_reversibility_authorized",
                "prior_relation_reversibility_performed",
                "prior_relation_reversibility_recorded",
                "prior_relation_operation_referenced",
                "prior_relation_record_referenced",
                "prior_relation_basis_referenced",
                "prior_relation_record_confirmed_as_historical_only",
            }:
                self.assertIs(value, False, key)
        relation = material["relation_record_lapse_boundary_reference"]
        self.assertEqual(relation["relation_id"], resolver.RELATION_ID)
        self.assertEqual(relation["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
        self.assertEqual(relation["first_crossing_a_id"], resolver.FIRST_CROSSING_A_ID)
        self.assertEqual(relation["first_crossing_b_id"], resolver.FIRST_CROSSING_B_ID)
        self.assertEqual(relation["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
        self.assertIs(relation["relation_record_referenced"], True)
        self.assertIs(relation["relation_record_confirmed_as_historical_only"], True)
        for key in (
            "relation_record_is_living_relation_state",
            "relation_record_is_presence",
            "relation_record_is_identity",
            "relation_record_is_coupling",
            "relation_record_is_landlord_of_between",
            "relation_record_outranks_first_crossing_a",
            "relation_record_outranks_first_crossing_b",
            "relation_record_outranks_first_crossing_pair",
        ):
            self.assertIs(relation[key], False)
        evaluation = material["relation_lapse_boundary_evaluation"]
        self.assertIs(evaluation["relation_lapse_operation_consideration_allowed"], True)
        self.assertEqual(evaluation["relation_lapse_boundary_result"], "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED")
        for key, value in evaluation.items():
            if key not in {"relation_lapse_operation_consideration_allowed", "relation_lapse_boundary_result"}:
                self.assertIs(value, False, key)

    def test_04_default_live_repo_target_records_allowed_when_present(self) -> None:
        request = resolver.build_relation_lapse_boundary_v0_min_request()
        references = [request["relation_lapse_boundary_spec_reference"]]
        references.extend(request[key] for key, *_ in resolver.UPSTREAM_REQUIREMENTS)
        paths = [Path(reference) if Path(reference).is_absolute() else REPO_ROOT / reference for reference in references]
        if not all(path.is_file() for path in paths):
            self.skipTest("required live target or upstream summary is unavailable")
        result = resolver.resolve_relation_lapse_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        self.assertEqual(result["relation_lapse_boundary_summary"]["result_version"], "0.1.0")
        self.assertEqual(result["relation_lapse_boundary_summary"]["resolver_module"], resolver.RESOLVER_MODULE)

    def test_05_missing_or_insufficient_upstream_posture_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            missing_request = copy.deepcopy(request)
            missing_request["relation_reversibility_operation_terminal_summary_reference"] = str(base / "missing_reversibility.md")
            required = resolver.resolve_relation_lapse_boundary_v0_min(missing_request)
            self.assert_requires_reversibility(required)
            self.assert_refusal_posture(required)
            reversibility_text = self.valid_reversibility_terminal_summary_text()
            for marker in REVERSIBILITY_MARKERS:
                with self.subTest(reversibility_marker=marker):
                    insufficient = reversibility_text.replace(marker, "MISSING_MARKER")
                    if marker == "RELATION_REVERSIBILITY_SUPPORTED":
                        insufficient = insufficient.replace("relation_reversibility_supported = true", "MISSING_MARKER")
                    self.write_markdown(paths["relation_reversibility_operation_terminal_summary_reference"], insufficient)
                    result = resolver.resolve_relation_lapse_boundary_v0_min(request)
                    self.assertIn(result["outcome"], {resolver.OUTCOME_REQUIRES_REVERSIBILITY, resolver.OUTCOME_BLOCKED})
                    self.assert_refusal_posture(result)
                    self.assert_canonical_non_claims(result)
                    self.write_markdown(paths["relation_reversibility_operation_terminal_summary_reference"], reversibility_text)
            non_reversibility_cases = (
                ("relation_operation_terminal_summary_reference", "RELATION_OPERATION_RECORDED"),
                ("relation_operation_terminal_summary_reference", "RELATION_SUPPORTED"),
                ("first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
                ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            )
            for key, marker in non_reversibility_cases:
                with self.subTest(upstream_key=key, marker=marker):
                    original = paths[key].read_text(encoding="utf-8")
                    self.write_markdown(paths[key], original.replace(marker, "MISSING_MARKER", 1))
                    result = resolver.resolve_relation_lapse_boundary_v0_min(request)
                    self.assertIn(result["outcome"], {resolver.OUTCOME_REQUIRES_REVERSIBILITY, resolver.OUTCOME_BLOCKED})
                    self.assert_refusal_posture(result)
                    self.assert_canonical_non_claims(result)
                    self.write_markdown(paths[key], original)

    def test_06_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            do_not_record = resolver.resolve_relation_lapse_boundary_v0_min(
                {**request, "intent": resolver.INTENT_DO_NOT_RECORD}
            )
            self.assertEqual(do_not_record["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertEqual(self.block_code(do_not_record), None)
            for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(do_not_record["relation_lapse_boundary"][key], False)
            self.assert_refusal_posture(do_not_record)
            self.assert_canonical_non_claims(do_not_record)
            blocked = resolver.resolve_relation_lapse_boundary_v0_min({**request, "intent": resolver.INTENT_BLOCK})
            self.assert_blocked_with_public_code(blocked)
            self.assertEqual(self.block_code(blocked), "EXPLICIT_BLOCK_REQUESTED")
            self.assert_refusal_posture(blocked)

    def test_07_request_shape_and_exact_fields_block(self) -> None:
        self.assert_blocked_with_public_code(resolver.resolve_relation_lapse_boundary_v0_min([]))
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            unsupported = resolver.resolve_relation_lapse_boundary_v0_min({**request, "intent": "UNSUPPORTED"})
            self.assert_blocked_with_public_code(unsupported)
            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    invalid = copy.deepcopy(request)
                    invalid[field] = (not expected) if isinstance(expected, bool) else f"wrong_{expected}"
                    result = resolver.resolve_relation_lapse_boundary_v0_min(invalid)
                    self.assert_blocked_with_public_code(result)
                    self.assert_refusal_posture(result)

    def test_08_marker_validation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, paths = self.build_valid_synthetic_request(Path(temporary))
            cases = (
                ("relation_lapse_boundary_spec_reference", "Relation Lapse Boundary V0 Minimum Specification"),
                ("relation_reversibility_operation_terminal_summary_reference", "RELATION_REVERSIBILITY_OPERATION_RECORDED"),
                ("relation_operation_terminal_summary_reference", "RELATION_OPERATION_RECORDED"),
                ("first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
                ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            )
            for index, (key, marker) in enumerate(cases):
                with self.subTest(case=key):
                    original = paths[key].read_text(encoding="utf-8")
                    path = paths[key]
                    isolated = path.with_name(self.safe_json_filename(f"marker_{key}", index).replace(".json", ".md"))
                    self.write_markdown(isolated, original.replace(marker, "MISSING_MARKER", 1))
                    candidate = copy.deepcopy(request)
                    candidate[key] = str(isolated)
                    result = resolver.resolve_relation_lapse_boundary_v0_min(candidate)
                    self.assertIn(result["outcome"], {resolver.OUTCOME_REQUIRES_REVERSIBILITY, resolver.OUTCOME_BLOCKED})
                    self.assert_canonical_non_claims(result)
                    self.assert_refusal_posture(result)
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_with_public_code(result)

    def test_09_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    candidate = copy.deepcopy(request)
                    candidate[flag] = True
                    result = resolver.resolve_relation_lapse_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assert_refusal_posture(result)

    def test_10_required_false_posture_and_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_key=key):
                    candidate = copy.deepcopy(request)
                    candidate[key] = True
                    result = resolver.resolve_relation_lapse_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assert_refusal_posture(result)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_non_claim_key=key):
                    candidate = copy.deepcopy(request)
                    candidate["declared_non_claims"][key] = True
                    result = resolver.resolve_relation_lapse_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_refusal_posture(result)
            malformed_cases: list[tuple[str, Any]] = (
                ("missing", None),
                ("non_mapping", []),
                ("non_bool", {**request["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}),
            )
            for name, declared in malformed_cases:
                with self.subTest(declared_non_claims=name):
                    candidate = copy.deepcopy(request)
                    if name == "missing":
                        candidate.pop("declared_non_claims")
                    else:
                        candidate["declared_non_claims"] = declared
                    result = resolver.resolve_relation_lapse_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_refusal_posture(result)

    def test_11_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, _ = self.build_valid_synthetic_request(base / "basis")
            request_path = base / "input" / "request.json"
            request_path.parent.mkdir(parents=True, exist_ok=True)
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_relation_lapse_boundary_v0_min_from_path(request_path)
            self.assert_allowed_boundary_posture(result)
            for name, payload in (("missing", None), ("malformed", "{"), ("array", "[]")):
                with self.subTest(path_case=name):
                    path = base / "path_cases" / self.safe_json_filename(name)
                    if payload is not None:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(payload, encoding="utf-8")
                    malformed = resolver.resolve_relation_lapse_boundary_v0_min_from_path(path)
                    self.assert_blocked_with_public_code(malformed)
                    self.assert_refusal_posture(malformed)
            output = base / "output" / resolver.DETERMINISTIC_FILENAME
            first = resolver.write_relation_lapse_boundary_v0_min_result(result, output)
            second = resolver.write_relation_lapse_boundary_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("relation_lapse_boundary_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            default_output = REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            self.assertIn("integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min", str(default_output))
            self.assertNotIn("relation_reversibility_operation", str(first.parent))

    def test_12_non_mutation_and_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            request_before = copy.deepcopy(request)
            files_before = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = resolver.resolve_relation_lapse_boundary_v0_min(request)
            self.assertEqual(request, request_before)
            self.assertEqual({key: path.read_text(encoding="utf-8") for key, path in paths.items()}, files_before)
            summary = resolver.build_relation_lapse_boundary_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
            self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
            self.assertEqual(summary["relation_lapse_boundary_result"], "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED")
            for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(summary[key], True, key)
            self.assertEqual(summary["missing_or_insufficient_reversibility"], [])
            requires_request = copy.deepcopy(request)
            requires_request["relation_reversibility_operation_terminal_summary_reference"] = str(base / "absent.md")
            requires = resolver.resolve_relation_lapse_boundary_v0_min(requires_request)
            self.assert_requires_reversibility(requires)
            requires_summary = resolver.build_relation_lapse_boundary_v0_min_summary(requires)
            self.assertFalse(requires_summary["relation_lapse_operation_consideration_allowed"])
            self.assertTrue(requires_summary["missing_or_insufficient_reversibility"])

    def test_13_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_relation_lapse_boundary_v0_min(request)
            summary = resolver.build_relation_lapse_boundary_v0_min_summary(result)
        self.assert_allowed_boundary_posture(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_relation_lapse_boundary_v0_min")
        material = result["relation_lapse_boundary_material"]
        self.assertEqual(set(material), {
            "relation_reversibility_operation_reference",
            "relation_record_lapse_boundary_reference",
            "relation_lapse_boundary_evaluation",
        })
        self.assert_boundary_has_no_wrapper_fields(result)
        self.assert_canonical_non_claims(result)


if __name__ == "__main__":
    unittest.main()
