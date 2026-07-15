"""Executable tests for the bounded presence-boundary resolver.

The suite proves that completed relation-lapse support may allow only future
presence-operation consideration.  Boundary allowance is never presence,
identity, coupling, relation conversion, repair, discovery, or downstream
authorization.
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

import resolve_presence_boundary_v0_min as resolver


BOUNDARY_IDENTITY_MARKERS = (
    "Presence Boundary V0 Minimum Specification",
    "PRESENCE_BOUNDARY",
    "presence_boundary_001",
    "CONSIDER_PRESENCE_AFTER_RELATION_LAPSE_OPERATION_ONLY",
)

RELATION_LAPSE_BASIS_MARKERS = (
    "RELATION_LAPSE_OPERATION_RECORDED",
    "RELATION_LAPSE_SUPPORTED",
    "relation_lapse_supported = true",
    "relation_lapse_authorized = true",
    "relation_lapse_performed = true",
    "relation_lapse_recorded = true",
    "relation_record_confirmed_as_historical_only = true",
    "relation_lapse_is_punishment = false",
    "relation_lapse_is_dissolution = false",
    "relation_lapse_is_erasure = false",
    "relation_lapse_is_teardown = false",
    "relation_lapse_is_living_relation_state = false",
    "relation_lapse_is_presence_boundary_authorization = false",
    "relation_lapse_is_presence = false",
    "relation_lapse_is_identity = false",
    "relation_lapse_is_coupling = false",
    "relation_lapse_is_field_machinery = false",
    "relation_lapse_is_runtime = false",
    "relation_lapse_is_currentness = false",
    "relation_lapse_is_authority = false",
    "relation_lapse_is_follow_on_authorization = false",
    "relation_lapse_is_follow_on_work = false",
)

PRIOR_FALSE_MARKERS = (
    "historical relation record is not living relation state",
    "relation record is not presence",
    "relation record is not identity",
    "relation record is not coupling",
    "relation_001 does not become landlord of the between",
    "relation_001 does not outrank First Crossing A",
    "relation_001 does not outrank First Crossing B",
    "relation_001 does not outrank the related first-crossing pair",
    "relation dissolution was not authorized",
    "relation dissolution was not performed",
    "relation was not reversed",
    "relation was not terminated",
    "relation was not erased",
    "relation was not mutated",
    "relation was not invalidated",
    "relation was not punished",
    "teardown logic was not created",
    "living relation state was not created",
    "living relation state did not lapse",
    "living relation state did not dissolve",
    "historical receipt preservation was not authorized",
    "historical receipt was not preserved",
    "presence boundary is not authorized",
    "presence is not established",
    "identity is not created",
    "coupling remains unassigned and uncreated",
    "follow-on work is not authorized",
)

BOUNDARY_RESULT_MARKERS = (
    "PRESENCE_BOUNDARY_ALLOWED",
    "PRESENCE_BOUNDARY_REQUIRES_LAPSE_OPERATION",
    "PRESENCE_BOUNDARY_BLOCKED",
    "PRESENCE_OPERATION_CONSIDERATION_ALLOWED",
    "REQUIRES_RELATION_LAPSE_OPERATION",
)

PRESENCE_NON_CONVERSION_MARKERS = (
    "Presence boundary is not presence operation",
    "Presence boundary permission is not presence",
    "Presence operation consideration is not presence",
    "Presence operation consideration is not identity",
    "Presence operation consideration is not coupling",
    "Presence operation consideration is not FIELD machinery",
    "Presence operation consideration is not runtime",
    "Presence operation consideration is not API",
    "Presence operation consideration is not currentness",
    "Presence operation consideration is not authority",
    "Presence operation consideration is not standing",
    "Presence operation consideration is not output authorization",
    "Presence operation consideration is not action authorization",
    "Presence operation consideration is not derivative reception",
    "Presence operation consideration is not synchronization",
    "Presence operation consideration is not follow-on authorization",
    "Presence operation consideration is not follow-on work",
    "Presence is not identity",
    "Presence is not coupling",
    "Presence is not FIELD machinery",
    "Presence is not runtime",
    "Presence is not API",
    "Presence is not currentness",
    "Presence is not authority",
    "Presence is not standing",
    "Presence is not output authorization",
    "Presence is not action authorization",
    "Presence is not derivative reception",
    "Presence is not synchronization",
    "Presence is not follow-on work",
    "Relation lapse support is not presence",
    "Relation lapse support is not presence boundary authorization",
    "Relation lapse support is not identity",
    "Relation lapse support is not coupling",
)

HISTORICAL_AND_COUPLING_MARKERS = (
    "Relation record remains historical-only",
    "Historical relation record is not living relation state",
    "Historical relation record is not presence",
    "Historical relation record is not identity",
    "Historical relation record is not coupling",
    "Living relation state may not be created by presence boundary",
    "Historical receipt preservation requires a separately bounded operation",
    "Identity requires a separately bounded operation",
    "Coupling remains unassigned",
    "Coupling must not be treated as third candidate",
    "Coupling must not be treated as third model",
    "Coupling must not be created by presence boundary",
    "No third candidate is admitted",
    "No third model is admitted",
)

LANDLORD_AND_RANK_MARKERS = (
    "relation_001 must not become landlord of the between",
    "relation_001 must not outrank First Crossing A",
    "relation_001 must not outrank First Crossing B",
    "relation_001 must not outrank the related first-crossing pair",
    "First Crossing A and First Crossing B remain sibling records",
    "neither first crossing ranks above the other",
    "Descendant Body A and Descendant Body B remain sibling records",
    "neither descendant body ranks above the other",
    "Candidate A and Candidate B remain sibling candidate standings",
    "neither candidate standing ranks above the other",
    "Regulation may not become sovereign over Motion",
    "Motion may not erase Regulation",
)

PERMITTED_ROUTE_MARKERS = (
    "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY",
    "Only after a future presence boundary records PRESENCE_OPERATION_CONSIDERATION_ALLOWED may a separately bounded presence operation be considered",
    "No presence, identity, coupling, FIELD machinery, runtime, currentness, authority, standing, output, action, derivative reception, synchronization, or later operation is authorized by this boundary spec alone",
)

CONTAMINATED_LINEAGE_MARKERS = (
    "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "descendant_body_basis_derivation_event_recorded = true",
    "UNSUPPORTED",
    "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
)

BLOCKED_ROUTE_MARKERS = (
    "direct presence boundary spec to presence operation completion",
    "direct relation lapse operation to presence without presence boundary and operation",
    "direct relation lapse operation to identity",
    "direct relation lapse operation to coupling assignment",
    "direct relation lapse operation to coupling creation",
    "direct relation lapse operation to FIELD machinery",
    "direct relation lapse operation to runtime",
    "direct relation lapse operation to authority/currentness",
    "direct relation lapse operation to follow-on work",
    "direct presence boundary to presence",
    "direct presence boundary to identity",
    "direct presence boundary to coupling assignment",
    "direct presence boundary to coupling creation",
    "direct presence boundary to FIELD machinery",
    "direct presence boundary to runtime",
    "direct presence boundary to authority/currentness",
    "direct presence boundary to standing",
    "direct presence boundary to output authorization",
    "direct presence boundary to action authorization",
    "direct presence boundary to derivative reception",
    "direct presence boundary to synchronization",
    "direct presence boundary to follow-on work",
    "direct presence boundary to relation dissolution",
    "direct presence boundary to relation reversal",
    "direct presence boundary to relation termination",
    "direct presence boundary to relation erasure",
    "direct presence boundary to relation mutation",
    "direct presence boundary to relation invalidation",
    "direct presence boundary to punitive interpretation",
    "direct presence boundary to teardown logic",
    "direct presence boundary to living relation state",
    "direct presence boundary to historical receipt preservation",
    "repository scan route",
    "file discovery route",
    "affected-file repair route",
    "prior unsupported-claim validation route",
)

CLOSING_LOCK_MARKERS = (
    "This boundary spec defines only a future presence boundary shape",
    "It does not itself execute a boundary resolver or record a boundary result",
    "It does not establish presence",
    "It does not create identity",
    "It does not assign coupling",
    "It does not create coupling",
    "It does not create FIELD machinery",
    "It does not create runtime",
    "It does not create API",
    "It does not create currentness",
    "It does not create authority",
    "It does not create standing",
    "Presence boundary is not presence operation",
    "Presence boundary permission is not presence",
    "Presence operation consideration is not presence, identity, coupling, FIELD machinery, runtime, API, currentness, authority, standing, output authorization, action authorization, derivative reception, synchronization, follow-on authorization, or follow-on work",
    "Relation lapse support is not presence, presence boundary authorization, identity, or coupling",
    "Relation record is historical-only and not living relation state, presence, identity, or coupling",
    "Coupling remains unassigned and uncreated",
    "Relation_001 must not become landlord of the between",
    "Relation_001 must not outrank First Crossing A, First Crossing B, or the related first-crossing pair",
    "Open means not scheduled, not authorized, and not executed",
)

SPEC_MARKER_CLASSES = (
    BOUNDARY_IDENTITY_MARKERS,
    RELATION_LAPSE_BASIS_MARKERS,
    PRIOR_FALSE_MARKERS,
    BOUNDARY_RESULT_MARKERS,
    PRESENCE_NON_CONVERSION_MARKERS,
    HISTORICAL_AND_COUPLING_MARKERS,
    LANDLORD_AND_RANK_MARKERS,
    PERMITTED_ROUTE_MARKERS,
    CONTAMINATED_LINEAGE_MARKERS,
    BLOCKED_ROUTE_MARKERS,
    CLOSING_LOCK_MARKERS,
)

SPEC_CLASS_BREAK_MARKERS = (
    "Presence Boundary V0 Minimum Specification",
    "relation_lapse_is_presence_boundary_authorization = false",
    "relation dissolution was not performed",
    "PRESENCE_BOUNDARY_REQUIRES_LAPSE_OPERATION",
    "Presence operation consideration is not API",
    "Living relation state may not be created by presence boundary",
    "Regulation may not become sovereign over Motion",
    "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY",
    "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
    "direct presence boundary spec to presence operation completion",
    "It does not itself execute a boundary resolver or record a boundary result",
)

RELATION_LAPSE_OPERATION_MARKERS = (
    "RELATION_LAPSE_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 365",
    "RELATION_LAPSE_SUPPORTED",
    "relation_lapse_supported = true",
    "relation_lapse_authorized = true",
    "relation_lapse_performed = true",
    "relation_lapse_recorded = true",
    "relation_record_confirmed_as_historical_only = true",
    "relation_lapse_is_punishment = false",
    "relation_lapse_is_dissolution = false",
    "relation_lapse_is_erasure = false",
    "relation_lapse_is_teardown = false",
    "relation_lapse_is_living_relation_state = false",
    "relation_lapse_is_presence_boundary_authorization = false",
    "relation_lapse_is_presence = false",
    "relation_lapse_is_identity = false",
    "relation_lapse_is_coupling = false",
    "relation_lapse_is_field_machinery = false",
    "relation_lapse_is_runtime = false",
    "relation_lapse_is_currentness = false",
    "relation_lapse_is_authority = false",
    "relation_lapse_is_follow_on_authorization = false",
    "relation_lapse_is_follow_on_work = false",
    "relation_record_is_living_relation_state = false",
    "living_relation_state_created = false",
    "living_relation_state_lapsed = false",
    "living_relation_state_dissolved = false",
    "relation_dissolution_authorized = false",
    "relation_dissolution_performed = false",
    "relation_reversed = false",
    "relation_terminated = false",
    "relation_erased = false",
    "relation_mutated = false",
    "relation_invalidated = false",
    "relation_punished = false",
    "relation_teardown_created = false",
    "historical_receipt_preservation_authorized = false",
    "historical_receipt_preserved = false",
    "presence_boundary_authorized = false",
    "presence_established = false",
    "identity_created = false",
    "coupling_created = false",
    "follow_on_authorized = false",
    "follow_on_work_authorized = false",
)

REQUIRED_PUBLIC_BLOCK_CODES = {
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "PRESENCE_BOUNDARY_SPEC_REFERENCE_MISSING",
    "PRESENCE_BOUNDARY_SPEC_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_LAPSE_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_REVERSIBILITY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "RELATION_LAPSE_OPERATION_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_PRESENCE_ESTABLISHMENT_REQUESTED",
    "PROHIBITED_IDENTITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_FIELD_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_STANDING_REQUESTED",
    "PROHIBITED_OUTPUT_ACTION_OR_DERIVATIVE_REQUESTED",
    "PROHIBITED_RELATION_DISSOLUTION_REQUESTED",
    "PROHIBITED_RELATION_REVERSAL_OR_TERMINATION_REQUESTED",
    "PROHIBITED_RELATION_ERASURE_MUTATION_OR_INVALIDATION_REQUESTED",
    "PROHIBITED_PUNITIVE_LAPSE_OR_TEARDOWN_REQUESTED",
    "PROHIBITED_LIVING_RELATION_STATE_REQUESTED",
    "PROHIBITED_HISTORICAL_RECEIPT_PRESERVATION_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
}


class PresenceBoundaryResolverTests(unittest.TestCase):
    """Verify bounded presence-boundary allowance and refusal posture."""

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

    def valid_presence_boundary_spec_text(self) -> str:
        return "\n".join(marker for group in SPEC_MARKER_CLASSES for marker in group) + "\n"

    def valid_relation_lapse_operation_terminal_summary_text(self) -> str:
        return "\n".join(RELATION_LAPSE_OPERATION_MARKERS) + "\n"

    def valid_relation_lapse_boundary_terminal_summary_text(self) -> str:
        return "RELATION_LAPSE_BOUNDARY_ALLOWED\nRELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED\n"

    def valid_relation_reversibility_operation_terminal_summary_text(self) -> str:
        return "RELATION_REVERSIBILITY_OPERATION_RECORDED\nRELATION_REVERSIBILITY_SUPPORTED\n"

    def valid_relation_operation_terminal_summary_text(self) -> str:
        return "RELATION_OPERATION_RECORDED\nRELATION_SUPPORTED\n"

    def valid_first_crossing_operation_v2_terminal_summary_text(self) -> str:
        return "FIRST_CROSSING_SUPPORTED\n"

    def valid_existence_claim_evidence_check_terminal_summary_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        ) + "\n"

    def build_valid_synthetic_request(self, base: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = {
            "presence_boundary_spec_reference": self.write_markdown(
                base / "presence_boundary.md", self.valid_presence_boundary_spec_text()
            ),
            "relation_lapse_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_lapse_operation.md",
                self.valid_relation_lapse_operation_terminal_summary_text(),
            ),
            "relation_lapse_boundary_terminal_summary_reference": self.write_markdown(
                base / "relation_lapse_boundary.md",
                self.valid_relation_lapse_boundary_terminal_summary_text(),
            ),
            "relation_reversibility_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_reversibility_operation.md",
                self.valid_relation_reversibility_operation_terminal_summary_text(),
            ),
            "relation_operation_terminal_summary_reference": self.write_markdown(
                base / "relation_operation.md", self.valid_relation_operation_terminal_summary_text()
            ),
            "first_crossing_operation_v2_terminal_summary_reference": self.write_markdown(
                base / "first_crossing_operation_v2.md",
                self.valid_first_crossing_operation_v2_terminal_summary_text(),
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(
                base / "existence_claim_evidence.md",
                self.valid_existence_claim_evidence_check_terminal_summary_text(),
            ),
        }
        request = resolver.build_presence_boundary_v0_min_request(
            **{key: str(value) for key, value in paths.items()}
        )
        return request, paths

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        summary = result.get("presence_boundary_summary")
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

    def assert_requires_lapse_operation(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_LAPSE_OPERATION)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        detail = result.get("boundary_result_detail")
        self.assertIsInstance(detail, dict)
        self.assertTrue(detail.get("missing_or_insufficient_relation_lapse_operation"))

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        records = result.get("presence_boundary_checks")
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
            self.assertIs(non_claims[key], False, key)

    def assert_boundary_has_no_wrapper_fields(self, result: dict[str, Any]) -> None:
        boundary = result.get("presence_boundary")
        self.assertIsInstance(boundary, dict)
        for key in (
            "outcome",
            "block",
            "presence_boundary_checks",
            "non_claims",
            "presence_boundary_summary",
            "presence_boundary_metadata",
            "presence_boundary_material",
        ):
            self.assertNotIn(key, boundary)
        self.assertNotIn("presence_boundary_material", boundary)

    def assert_refusal_posture(self, result: dict[str, Any]) -> None:
        boundary = result.get("presence_boundary")
        self.assertIsInstance(boundary, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            if key not in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(boundary.get(key), False, key)
        for key in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "identity_created",
            "identity_authorized",
            "coupling_created",
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
            "follow_on_authorized",
            "follow_on_work_authorized",
            "relation_dissolution_authorized",
            "relation_reversed",
            "relation_terminated",
            "relation_erased",
            "relation_mutated",
            "relation_invalidated",
            "relation_punished",
            "relation_teardown_created",
            "living_relation_state_created",
            "historical_receipt_preservation_authorized",
            "historical_receipt_preserved",
        ):
            self.assertIs(boundary[key], False, key)

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_refusal_posture(result)

    def assert_allowed_boundary_posture(self, result: dict[str, Any]) -> None:
        self.assert_allowed(result)
        boundary = result["presence_boundary"]
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            boundary["presence_boundary_result"], "PRESENCE_OPERATION_CONSIDERATION_ALLOWED"
        )
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_boundary_has_no_wrapper_fields(result)

    def test_01_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_presence_boundary_v0_min",
            "resolve_presence_boundary_v0_min_from_path",
            "write_presence_boundary_v0_min_result",
            "build_presence_boundary_v0_min_summary",
            "build_presence_boundary_v0_min_request",
            "build_declared_presence_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        expected_constants = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_presence_boundary_v0_min",
            "BOUNDARY_ID": "presence_boundary_001",
            "BOUNDARY_TYPE": "PRESENCE_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": "CONSIDER_PRESENCE_AFTER_RELATION_LAPSE_OPERATION_ONLY",
            "PRIOR_RELATION_LAPSE_OPERATION_TYPE": "RELATION_LAPSE_OPERATION",
            "PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED": "RELATION_LAPSE_OPERATION_RECORDED",
            "PRIOR_RELATION_LAPSE_RESULT_REQUIRED": "RELATION_LAPSE_SUPPORTED",
            "ADMISSIBLE_FUTURE_ROUTE": "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY",
            "RELATION_ID": "relation_001",
            "RELATION_PAIR_SCOPE": "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
            "RELATION_LAPSE_ID": "relation_lapse_001",
            "RELATION_LAPSE_SCOPE": "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY",
            "PRESENCE_ID": "presence_001",
            "PRESENCE_SCOPE": "PRESENCE_AFTER_RELATION_LAPSE_WITHOUT_IDENTITY_OR_COUPLING_ONLY",
            "PRESENCE_RESULT": "PRESENCE_SUPPORTED",
        }
        for name, expected in expected_constants.items():
            self.assertEqual(getattr(resolver, name), expected, name)

        true_constants = (
            "PRIOR_RELATION_LAPSE_SUPPORTED_REQUIRED",
            "PRIOR_RELATION_LAPSE_AUTHORIZED_REQUIRED",
            "PRIOR_RELATION_LAPSE_PERFORMED_REQUIRED",
            "PRIOR_RELATION_LAPSE_RECORDED_REQUIRED",
            "PRIOR_RELATION_RECORD_CONFIRMED_AS_HISTORICAL_ONLY_REQUIRED",
        )
        false_constants = (
            "PRIOR_RELATION_LAPSE_IS_PUNISHMENT_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_DISSOLUTION_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_ERASURE_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_TEARDOWN_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_LIVING_RELATION_STATE_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_PRESENCE_BOUNDARY_AUTHORIZATION_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_PRESENCE_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_IDENTITY_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_COUPLING_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_FIELD_MACHINERY_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_RUNTIME_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_CURRENTNESS_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_AUTHORITY_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_AUTHORIZATION_REQUIRED",
            "PRIOR_RELATION_LAPSE_IS_FOLLOW_ON_WORK_REQUIRED",
            "PRIOR_RELATION_RECORD_IS_LIVING_RELATION_STATE_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_CREATED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_LAPSED_REQUIRED",
            "PRIOR_LIVING_RELATION_STATE_DISSOLVED_REQUIRED",
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
        )
        for name in true_constants:
            self.assertIs(getattr(resolver, name), True, name)
        for name in false_constants:
            self.assertIs(getattr(resolver, name), False, name)

        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_ALLOWED,
                resolver.OUTCOME_REQUIRES_LAPSE_OPERATION,
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_NOT_RECORDED,
            },
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_presence_boundary_v0_min"
            )
        )
        self.assertTrue(REQUIRED_PUBLIC_BLOCK_CODES.issubset(set(resolver.BLOCK_CODES)))

        required_flags = {
            "request_presence_establishment",
            "request_identity_creation",
            "request_coupling_assignment_to_relation",
            "request_coupling_creation",
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
            "request_relation_dissolution_authorization",
            "request_relation_reversal",
            "request_relation_termination",
            "request_relation_erasure",
            "request_relation_mutation",
            "request_relation_invalidation",
            "request_relation_punishment",
            "request_relation_teardown_creation",
            "request_living_relation_state_creation",
            "request_historical_receipt_preservation",
            "request_third_candidate_creation",
            "request_third_model_admission",
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
        }
        self.assertTrue(required_flags.issubset(resolver.PROHIBITED_REQUEST_FLAGS))
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )
        self.assertEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_follow_on_work_authorization"],
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        )

        request = resolver.build_presence_boundary_v0_min_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["presence_boundary_spec_reference"], resolver.DEFAULT_PRESENCE_BOUNDARY_SPEC_REFERENCE)
        for key, expected in resolver.EXPECTED_REQUEST_VALUES.items():
            if isinstance(expected, bool):
                self.assertIs(request[key], expected, key)
            else:
                self.assertEqual(request[key], expected, key)
        for key in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(request[key], False, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request[key], False, key)
            self.assertIs(request["declared_non_claims"][key], False, key)

    def test_02_synthetic_complete_boundary_records_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        summary = result["presence_boundary_summary"]
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_presence_boundary_v0_min")
        self.assertGreater(summary["passed_check_count"], 0)

        boundary = result["presence_boundary"]
        self.assertEqual(boundary["prior_relation_lapse_operation_type"], resolver.PRIOR_RELATION_LAPSE_OPERATION_TYPE)
        self.assertEqual(
            boundary["prior_relation_lapse_operation_outcome_required"],
            resolver.PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED,
        )
        self.assertEqual(boundary["prior_relation_lapse_result_required"], resolver.PRIOR_RELATION_LAPSE_RESULT_REQUIRED)
        for key in (
            "prior_relation_lapse_supported_required",
            "prior_relation_lapse_authorized_required",
            "prior_relation_lapse_performed_required",
            "prior_relation_lapse_recorded_required",
            "prior_relation_record_confirmed_as_historical_only_required",
        ):
            self.assertIs(boundary[key], True, key)
        self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_relation_lapse_operation"], [])

        required_sections = {
            "presence_boundary_metadata",
            "declared_presence_boundary_basis",
            "upstream_basis",
            "presence_boundary",
            "presence_boundary_material",
            "presence_boundary_checks",
            "presence_boundary_statement",
            "presence_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "presence_boundary_summary",
        }
        self.assertTrue(required_sections.issubset(result))
        marker_values = {
            value for key, value in boundary.items() if key.endswith("markers_present")
        }
        self.assertEqual(marker_values, {True})
        for key in (
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        ):
            self.assertIs(boundary[key], False, key)

    def test_03_presence_boundary_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        material = result["presence_boundary_material"]
        self.assertEqual(
            set(material),
            {
                "relation_lapse_operation_reference",
                "relation_record_presence_boundary_reference",
                "presence_boundary_evaluation",
            },
        )

        lapse = material["relation_lapse_operation_reference"]
        self.assertEqual(lapse["prior_relation_lapse_operation_type"], resolver.PRIOR_RELATION_LAPSE_OPERATION_TYPE)
        self.assertEqual(
            lapse["prior_relation_lapse_operation_outcome"],
            resolver.PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED,
        )
        self.assertEqual(lapse["prior_relation_lapse_result"], resolver.PRIOR_RELATION_LAPSE_RESULT_REQUIRED)
        allowed_lapse_keys = {
            "prior_relation_lapse_supported",
            "prior_relation_lapse_authorized",
            "prior_relation_lapse_performed",
            "prior_relation_lapse_recorded",
            "prior_relation_record_confirmed_as_historical_only",
        }
        for key in allowed_lapse_keys:
            self.assertIs(lapse[key], True, key)
        for key, value in lapse.items():
            if key in allowed_lapse_keys or key in {
                "prior_relation_lapse_operation_type",
                "prior_relation_lapse_operation_outcome",
                "prior_relation_lapse_result",
            }:
                continue
            self.assertIs(value, False, key)

        relation = material["relation_record_presence_boundary_reference"]
        expected_relation_values = {
            "relation_id": resolver.RELATION_ID,
            "relation_pair_scope": resolver.RELATION_PAIR_SCOPE,
            "relation_lapse_id": resolver.RELATION_LAPSE_ID,
            "relation_lapse_scope": resolver.RELATION_LAPSE_SCOPE,
            "first_crossing_a_id": resolver.FIRST_CROSSING_A_ID,
            "first_crossing_b_id": resolver.FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": resolver.FIRST_CROSSING_PAIR_SCOPE,
        }
        for key, expected in expected_relation_values.items():
            self.assertEqual(relation[key], expected, key)
        self.assertIs(relation["relation_record_confirmed_as_historical_only"], True)
        for key, value in relation.items():
            if key in expected_relation_values or key == "relation_record_confirmed_as_historical_only":
                continue
            self.assertIs(value, False, key)

        evaluation = material["presence_boundary_evaluation"]
        self.assertEqual(evaluation["presence_boundary_result"], "PRESENCE_OPERATION_CONSIDERATION_ALLOWED")
        self.assertIs(evaluation["presence_operation_consideration_allowed"], True)
        self.assertEqual(evaluation["presence_id"], resolver.PRESENCE_ID)
        self.assertEqual(evaluation["presence_scope"], resolver.PRESENCE_SCOPE)
        for key, value in evaluation.items():
            if key in {
                "presence_boundary_result",
                "presence_operation_consideration_allowed",
                "presence_id",
                "presence_scope",
            }:
                continue
            self.assertIs(value, False, key)

    def test_04_default_live_repo_target_records_allowed_when_present(self) -> None:
        request = resolver.build_presence_boundary_v0_min_request()
        references = [request["presence_boundary_spec_reference"]]
        references.extend(request[key] for key, *_ in resolver.UPSTREAM_REQUIREMENTS)
        paths = [Path(reference) if Path(reference).is_absolute() else REPO_ROOT / reference for reference in references]
        if not all(path.is_file() for path in paths):
            self.skipTest("required live target or upstream summary is unavailable")
        result = resolver.resolve_presence_boundary_v0_min(request)
        self.assert_allowed_boundary_posture(result)
        summary = result["presence_boundary_summary"]
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["presence_boundary_result"], "PRESENCE_OPERATION_CONSIDERATION_ALLOWED")
        marker_values = {value for key, value in summary.items() if key.endswith("markers_present")}
        self.assertEqual(marker_values, {True})

    def test_05_missing_or_insufficient_upstream_basis_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)

            missing = copy.deepcopy(request)
            missing["relation_lapse_operation_terminal_summary_reference"] = str(base / "missing_lapse.md")
            result = resolver.resolve_presence_boundary_v0_min(missing)
            self.assert_requires_lapse_operation(result)
            self.assert_refusal_posture(result)
            self.assert_canonical_non_claims(result)

            original_lapse = self.valid_relation_lapse_operation_terminal_summary_text()
            for index, marker in enumerate(RELATION_LAPSE_OPERATION_MARKERS):
                with self.subTest(lapse_marker=marker):
                    isolated = base / "lapse_markers" / self.safe_json_filename(marker, index).replace(".json", ".md")
                    corrupted = original_lapse.replace(marker, "MISSING_MARKER")
                    if marker == "RELATION_LAPSE_SUPPORTED":
                        corrupted = corrupted.replace(
                            "relation_lapse_supported", "missing_support_posture"
                        )
                    self.write_markdown(isolated, corrupted)
                    candidate = copy.deepcopy(request)
                    candidate["relation_lapse_operation_terminal_summary_reference"] = str(isolated)
                    marked = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assertIn(
                        marked["outcome"],
                        {resolver.OUTCOME_REQUIRES_LAPSE_OPERATION, resolver.OUTCOME_BLOCKED},
                    )
                    self.assert_refusal_posture(marked)
                    self.assert_canonical_non_claims(marked)
                    if marked["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_with_public_code(marked)

            non_lapse_cases = (
                (
                    "relation_lapse_boundary_terminal_summary_reference",
                    ("RELATION_LAPSE_BOUNDARY_ALLOWED", "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"),
                ),
                (
                    "relation_reversibility_operation_terminal_summary_reference",
                    ("RELATION_REVERSIBILITY_OPERATION_RECORDED", "RELATION_REVERSIBILITY_SUPPORTED"),
                ),
                (
                    "relation_operation_terminal_summary_reference",
                    ("RELATION_OPERATION_RECORDED", "RELATION_SUPPORTED"),
                ),
                ("first_crossing_operation_v2_terminal_summary_reference", ("FIRST_CROSSING_SUPPORTED",)),
                ("existence_claim_evidence_check_terminal_summary_reference", ("UNSUPPORTED",)),
            )
            for field, markers in non_lapse_cases:
                with self.subTest(missing_upstream=field):
                    candidate = copy.deepcopy(request)
                    candidate[field] = str(base / f"missing_{field}.md")
                    blocked = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(blocked)
                original = paths[field].read_text(encoding="utf-8")
                for marker in markers:
                    with self.subTest(upstream_field=field, marker=marker):
                        isolated = base / "upstream_markers" / self.safe_json_filename(f"{field}_{marker}").replace(".json", ".md")
                        self.write_markdown(isolated, original.replace(marker, "MISSING_MARKER"))
                        candidate = copy.deepcopy(request)
                        candidate[field] = str(isolated)
                        blocked = resolver.resolve_presence_boundary_v0_min(candidate)
                        self.assert_blocked_with_public_code(blocked)

    def test_06_do_not_record_intent_does_not_allow_consideration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_boundary_v0_min(
                {**request, "intent": resolver.INTENT_DO_NOT_RECORD}
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(self.block_code(result))
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(result["presence_boundary"][key], False, key)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)

    def test_07_explicit_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_boundary_v0_min(
                {**request, "intent": resolver.INTENT_BLOCK}
            )
        self.assert_blocked_with_public_code(result)
        self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(result["presence_boundary"][key], False, key)

    def test_08_request_shape_and_exact_fields_block(self) -> None:
        self.assert_blocked_with_public_code(resolver.resolve_presence_boundary_v0_min([]))
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            unsupported = resolver.resolve_presence_boundary_v0_min({**request, "intent": "UNSUPPORTED"})
            self.assert_blocked_with_public_code(unsupported)
            self.assertEqual(self.block_code(unsupported), "UNSUPPORTED_INTENT")

            for field, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                with self.subTest(field=field):
                    candidate = copy.deepcopy(request)
                    candidate[field] = (not expected) if isinstance(expected, bool) else f"wrong_{expected}"
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "REQUEST_VALUE_MISMATCH")
                    self.assert_boundary_has_no_wrapper_fields(result)

    def test_09_marker_validation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            original_spec = self.valid_presence_boundary_spec_text()
            for index, marker in enumerate(SPEC_CLASS_BREAK_MARKERS):
                with self.subTest(spec_marker_class=index, marker=marker):
                    isolated = base / "spec_markers" / self.safe_json_filename(marker, index).replace(".json", ".md")
                    self.write_markdown(isolated, original_spec.replace(marker, "MISSING_MARKER"))
                    candidate = copy.deepcopy(request)
                    candidate["presence_boundary_spec_reference"] = str(isolated)
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "PRESENCE_BOUNDARY_SPEC_MARKER_MISSING")

            upstream_cases = (
                ("relation_lapse_operation_terminal_summary_reference", "RELATION_LAPSE_OPERATION_RECORDED"),
                ("relation_lapse_boundary_terminal_summary_reference", "RELATION_LAPSE_BOUNDARY_ALLOWED"),
                (
                    "relation_reversibility_operation_terminal_summary_reference",
                    "RELATION_REVERSIBILITY_OPERATION_RECORDED",
                ),
                ("relation_operation_terminal_summary_reference", "RELATION_OPERATION_RECORDED"),
                ("first_crossing_operation_v2_terminal_summary_reference", "FIRST_CROSSING_SUPPORTED"),
                ("existence_claim_evidence_check_terminal_summary_reference", "UNSUPPORTED"),
            )
            for index, (field, marker) in enumerate(upstream_cases):
                with self.subTest(upstream_marker=field):
                    original = paths[field].read_text(encoding="utf-8")
                    isolated = base / "representative_upstream" / self.safe_json_filename(field, index).replace(".json", ".md")
                    self.write_markdown(isolated, original.replace(marker, "MISSING_MARKER"))
                    candidate = copy.deepcopy(request)
                    candidate[field] = str(isolated)
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assertIn(
                        result["outcome"],
                        {resolver.OUTCOME_REQUIRES_LAPSE_OPERATION, resolver.OUTCOME_BLOCKED},
                    )
                    self.assert_refusal_posture(result)
                    self.assert_canonical_non_claims(result)
                    self.assert_all_emitted_codes_public(result)

    def test_10_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    candidate = copy.deepcopy(request)
                    candidate[flag] = True
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assert_boundary_has_no_wrapper_fields(result)

    def test_11_required_false_top_level_posture_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_key=key):
                    candidate = copy.deepcopy(request)
                    candidate[key] = True
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "RESULT_POSTURE_PRECLAIMED")
                    self.assert_boundary_has_no_wrapper_fields(result)

    def test_12_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(declared_non_claim_key=key):
                    candidate = copy.deepcopy(request)
                    candidate["declared_non_claims"][key] = True
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assertIs(result["non_claims"][key], False)

            malformed_cases: tuple[tuple[str, Any], ...] = (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                (
                    "non_bool",
                    {
                        **request["declared_non_claims"],
                        resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false",
                    },
                ),
            )
            for name, declared in malformed_cases:
                with self.subTest(declared_non_claims=name):
                    candidate = copy.deepcopy(request)
                    if name == "missing":
                        candidate.pop("declared_non_claims")
                    else:
                        candidate["declared_non_claims"] = declared
                    result = resolver.resolve_presence_boundary_v0_min(candidate)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_13_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, _ = self.build_valid_synthetic_request(base / "basis")
            request_path = base / "input" / "request.json"
            request_path.parent.mkdir(parents=True, exist_ok=True)
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_presence_boundary_v0_min_from_path(request_path)
            self.assert_allowed_boundary_posture(result)
            self.assertEqual(result["presence_boundary_summary"]["result_version"], "0.1.0")
            self.assertEqual(result["presence_boundary_summary"]["resolver_module"], resolver.RESOLVER_MODULE)

            path_cases = (
                ("missing", None),
                ("malformed", "{"),
                ("array", "[]"),
            )
            for name, payload in path_cases:
                with self.subTest(path_case=name):
                    path = base / "path_cases" / self.safe_json_filename(name)
                    if payload is not None:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(payload, encoding="utf-8")
                    blocked = resolver.resolve_presence_boundary_v0_min_from_path(path)
                    self.assert_blocked_with_public_code(blocked)

            output = base / "output" / resolver.DETERMINISTIC_FILENAME
            first = resolver.write_presence_boundary_v0_min_result(result, output)
            second = resolver.write_presence_boundary_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("presence_boundary_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)

            default_output = REPO_ROOT / resolver.OUTPUT_ROOT / resolver.DETERMINISTIC_FILENAME
            default_text = str(default_output)
            self.assertIn("integrity_host_v0_min_coexistence_presence_boundary_v0_min", default_text)
            prohibited_roots = (
                "relation_lapse_operation_v0_min",
                "relation_lapse_boundary_v0_min",
                "relation_reversibility_operation_v0_min",
                "relation_reversibility_boundary_v0_min",
                "relation_operation_v0_min",
                "relation_boundary_v0_min",
                "first_crossing_operation_v2",
                "first_crossing_operation_v1",
                "first_crossing_boundary",
                "descendant_body_creation_operation",
                "candidate_standing_operation",
                "runtime",
                "daemon",
                "api",
                "field",
                "presence_operation",
                "identity",
                "externalization",
            )
            for root in prohibited_roots:
                self.assertNotIn(root, str(first.parent).casefold(), root)

    def test_14_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base)
            request["hostile_sentinel"] = {
                "nested": ["do-not-mutate", {"value": True}],
                "path": "../../reference/IAMMAI/do-not-touch",
            }
            request_before = copy.deepcopy(request)
            files_before = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = resolver.resolve_presence_boundary_v0_min(request)
            self.assert_allowed_boundary_posture(result)
            self.assertEqual(request, request_before)
            self.assertEqual(
                {key: path.read_text(encoding="utf-8") for key, path in paths.items()},
                files_before,
            )
            self.assertEqual(request["intent"], resolver.INTENT_RECORD)
            for key, expected in resolver.EXPECTED_REQUEST_VALUES.items():
                self.assertEqual(request[key], expected, key)
            for key in resolver.PROHIBITED_REQUEST_FLAGS:
                self.assertIs(request[key], False, key)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIs(request[key], False, key)
                self.assertIs(request["declared_non_claims"][key], False, key)

    def test_15_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, _ = self.build_valid_synthetic_request(base)
            result = resolver.resolve_presence_boundary_v0_min(request)
            summary = resolver.build_presence_boundary_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
            self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(summary["boundary_version"], resolver.BOUNDARY_VERSION)
            self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
            self.assertEqual(
                summary["prior_relation_lapse_operation_type"],
                resolver.PRIOR_RELATION_LAPSE_OPERATION_TYPE,
            )
            self.assertEqual(
                summary["prior_relation_lapse_operation_outcome_required"],
                resolver.PRIOR_RELATION_LAPSE_OPERATION_OUTCOME_REQUIRED,
            )
            self.assertEqual(
                summary["prior_relation_lapse_result_required"],
                resolver.PRIOR_RELATION_LAPSE_RESULT_REQUIRED,
            )
            self.assertEqual(summary["relation_id"], resolver.RELATION_ID)
            self.assertEqual(summary["relation_pair_scope"], resolver.RELATION_PAIR_SCOPE)
            self.assertEqual(summary["presence_boundary_result"], "PRESENCE_OPERATION_CONSIDERATION_ALLOWED")
            for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(summary[key], True, key)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                if key not in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                    self.assertIs(summary[key], False, key)
            marker_values = {value for key, value in summary.items() if key.endswith("markers_present")}
            self.assertEqual(marker_values, {True})
            self.assertEqual(summary["selected_presence_boundary_spec_path"], request["presence_boundary_spec_reference"])
            self.assertEqual(
                summary["completed_relation_lapse_operation_terminal_summary_path"],
                request["relation_lapse_operation_terminal_summary_reference"],
            )
            self.assertEqual(summary["missing_or_insufficient_relation_lapse_operation"], [])

            missing_request = copy.deepcopy(request)
            missing_request["relation_lapse_operation_terminal_summary_reference"] = str(base / "absent.md")
            requires = resolver.resolve_presence_boundary_v0_min(missing_request)
            self.assert_requires_lapse_operation(requires)
            requires_summary = resolver.build_presence_boundary_v0_min_summary(requires)
            self.assertIs(requires_summary["presence_operation_consideration_allowed"], False)
            self.assertTrue(requires_summary["missing_or_insufficient_relation_lapse_operation"])

    def test_16_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_presence_boundary_v0_min(request)
            summary = resolver.build_presence_boundary_v0_min_summary(result)
        self.assert_allowed_boundary_posture(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], "resolve_presence_boundary_v0_min")
        self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(summary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(summary["presence_boundary_result"], "PRESENCE_OPERATION_CONSIDERATION_ALLOWED")
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(summary[key], True, key)
        self.assertEqual(
            set(result["presence_boundary_material"]),
            {
                "relation_lapse_operation_reference",
                "relation_record_presence_boundary_reference",
                "presence_boundary_evaluation",
            },
        )
        for key in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_is_identity",
            "presence_is_coupling",
            "presence_is_field_machinery",
            "presence_is_runtime",
            "presence_is_currentness",
            "presence_is_authority",
            "presence_is_standing",
            "identity_created",
            "identity_authorized",
            "coupling_created",
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
            "follow_on_authorized",
            "follow_on_work_authorized",
            "relation_dissolution_authorized",
            "relation_reversed",
            "relation_terminated",
            "relation_erased",
            "relation_mutated",
            "relation_invalidated",
            "relation_punished",
            "relation_teardown_created",
            "living_relation_state_created",
            "historical_receipt_preservation_authorized",
            "historical_receipt_preserved",
        ):
            self.assertIs(summary[key], False, key)
        self.assert_boundary_has_no_wrapper_fields(result)
        self.assert_canonical_non_claims(result)


if __name__ == "__main__":
    unittest.main()
