"""Bounded tests for one candidate-specific basis emission successor operation.

The resolver may emit separate non-standing Candidate A and Candidate B basis
material only after completed successor closure. Emission remains separate from
distinctness, standing, bodies, runtime, authority, coupling, and follow-on.
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

import resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min as resolver


class BasisEmissionSuccessorOperationTests(unittest.TestCase):
    """Verify bounded non-standing basis material emission only."""

    OPERATION_KEY = "descendant_body_candidate_specific_distinctness_basis_emission_successor_operation"
    MATERIAL_KEY = "emitted_candidate_specific_basis_material"
    CHECKS_KEY = "basis_emission_successor_operation_checks"
    SUMMARY_KEY = "basis_emission_successor_operation_summary"
    WRAPPER_FIELDS = (
        "outcome",
        "block",
        CHECKS_KEY,
        "non_claims",
        SUMMARY_KEY,
        "basis_emission_successor_operation_metadata",
        MATERIAL_KEY,
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, root: Path, name: str, content: str) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def operation_spec_text(self) -> str:
        lines = [
            "# Descendant Body Candidate Specific Distinctness Basis Emission Successor Operation V0 Minimum Specification",
        ]
        for _, markers in resolver.OPERATION_SPEC_MARKER_CLASSES:
            lines.extend(markers)
        return "\n".join(lines)

    def prior_basis_emission_text(self) -> str:
        return "\n".join((
            resolver.PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 161",
            "candidate_specific_content_emitted = false",
            "separate_seal_material_emitted = false",
            "separate_lineage_receipt_material_emitted = false",
            "separate_digest_material_emitted = false",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        ))

    def successor_closure_text(self) -> str:
        return "\n".join((
            resolver.UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 93",
            resolver.UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
            "prior_additional_basis_gap_closed = true",
            "closure_basis_received = true",
            "closure_basis_audited = true",
            "closure_basis_digest_custody_sealed = true",
            "candidate_a_missing_basis_resolved = true",
            "candidate_b_missing_basis_resolved = true",
            "basis_bearing_scope_division_missing_basis_resolved = true",
            "declaration_accepted_as_basis = true",
            "declaration_admitted_as_standing_basis = false",
            "candidate_a_scope_declared = false",
            "candidate_b_scope_declared = false",
            "basis_bearing_scope_division_declared = false",
            "distinctness_supported_recorded = false",
            "candidate_records_marked_distinct = false",
            "descendant_body_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ))

    def distinctness_text(self) -> str:
        return "\n".join((
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
            "distinctness_result = NOT_DISTINCT",
            "distinctness_supported = false",
            "candidate-specific content was absent",
            "separate seal, receipt, and digest material were absent",
        ))

    def existence_claim_text(self) -> str:
        return "\n".join((
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        ))

    def scope_division_operation_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS"

    def receipt_operation_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED"

    def audit_operation_text(self) -> str:
        return "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS"

    def digest_custody_operation_text(self) -> str:
        return "\n".join((
            "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_RECORDED",
            resolver.TARGET_PRIMARY_MATERIAL_DIGEST_SHA256,
        ))

    def marker_paths(self, root: Path) -> dict[str, Path]:
        return {
            "operation_spec_reference": self.write_markdown(root, "successor_spec.md", self.operation_spec_text()),
            "prior_basis_emission_operation_terminal_summary_reference": self.write_markdown(root, "prior_basis_emission.md", self.prior_basis_emission_text()),
            "successor_closure_operation_terminal_summary_reference": self.write_markdown(root, "successor_closure.md", self.successor_closure_text()),
            "distinctness_operation_terminal_summary_reference": self.write_markdown(root, "distinctness.md", self.distinctness_text()),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(root, "existence_claim.md", self.existence_claim_text()),
            "scope_division_operation_terminal_summary_reference": self.write_markdown(root, "scope_division.md", self.scope_division_operation_text()),
            "receipt_operation_terminal_summary_reference": self.write_markdown(root, "receipt.md", self.receipt_operation_text()),
            "audit_operation_terminal_summary_reference": self.write_markdown(root, "audit.md", self.audit_operation_text()),
            "digest_custody_operation_terminal_summary_reference": self.write_markdown(root, "digest_custody.md", self.digest_custody_operation_text()),
        }

    def valid_request(self, paths: dict[str, Path]) -> dict[str, object]:
        return resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_request(
            **{key: str(value) for key, value in paths.items()}
        )

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def material(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.MATERIAL_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get(self.CHECKS_KEY)
        self.assertIsInstance(value, list)
        return value

    def summary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.SUMMARY_KEY)
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def failed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is False for check in self.checks(result))

    def passed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is True for check in self.checks(result))

    def assert_public_codes(self, result: dict[str, object]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                if key in check:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        operation = self.operation(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)

    def assert_operation_not_wrapper(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in self.WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def assert_emitted(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_EMITTED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(self.block_code(result))
        self.assert_non_claims_false(result)
        self.assert_operation_not_wrapper(result)

    def assert_requires_successor_closure(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE)
        self.assertIs(result["block"]["blocked"], False)
        self.assertTrue(result["emission_result_detail"]["missing_or_insufficient_successor_closure_basis"])
        self.assert_public_codes(result)
        operation = self.operation(result)
        self.assertIs(operation["candidate_specific_content_emitted"], False)
        self.assert_non_claims_false(result)

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        operation = self.operation(result)
        self.assertIs(operation["candidate_specific_content_emitted"], False)
        self.assertIs(operation["candidate_records_marked_distinct"], False)
        self.assertIs(operation["distinctness_supported_recorded"], False)
        self.assert_non_claims_false(result)
        self.assert_operation_not_wrapper(result)

    def assert_no_downstream_posture(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in (
            "candidate_records_marked_distinct", "candidate_records_distinct", "distinctness_supported_recorded",
            "distinctness_operation_rerun", "candidate_standing_authorized", "descendant_body_created",
            "standing_authorized", "standing_descendant_created", "crossing_authorized",
            "first_crossing_authorized", "relation_created", "field_machinery_created", "runtime_created",
            "api_created", "currentness_created", "authority_created", "coupling_created",
            "third_candidate_created", "third_model_admitted", "presence_established", "identity_created",
            "output_authorized", "action_authorized", "derivative_reception_authorized",
            "synchronization_authorized", "follow_on_authorized", "follow_on_work_authorized",
        ):
            self.assertIs(operation[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min",
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_from_path",
            "write_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_result",
            "build_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name, None)), name)
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min",
            "OPERATION_ID": "descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_001",
            "OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "EMIT_CANDIDATE_SPECIFIC_BASIS_MATERIAL_AFTER_SUCCESSOR_CLOSURE_ONLY",
            "PRIOR_BASIS_EMISSION_OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION",
            "PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION",
            "UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED": "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED",
            "UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED": "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED",
            "TARGET_PRIMARY_MATERIAL_FILENAME": "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf",
            "TARGET_PRIMARY_MATERIAL_DIGEST_SHA256": "1ca450ea9762f2b2782b7edf3a1a08df3f292abbbd3aec78aa2890384b720dd0",
            "CANDIDATE_A_BASIS_ID": "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis",
            "CANDIDATE_B_BASIS_ID": "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis",
            "CANDIDATE_A_BASIS_LABEL": "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS",
            "CANDIDATE_B_BASIS_LABEL": "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS",
            "BASIS_PAIR_SCOPE": "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
            "ADMISSIBLE_FUTURE_ROUTE": "BASIS_EMISSION_SUCCESSOR_THEN_DISTINCTNESS_SUPPORT_RECHECK_ONLY",
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value, name)
        for name in (
            "UPSTREAM_PRIOR_ADDITIONAL_BASIS_GAP_CLOSED_REQUIRED",
            "UPSTREAM_CLOSURE_BASIS_RECEIVED_REQUIRED",
            "UPSTREAM_CLOSURE_BASIS_AUDITED_REQUIRED",
            "UPSTREAM_CLOSURE_BASIS_DIGEST_CUSTODY_SEALED_REQUIRED",
            "UPSTREAM_CANDIDATE_A_MISSING_BASIS_RESOLVED_REQUIRED",
            "UPSTREAM_CANDIDATE_B_MISSING_BASIS_RESOLVED_REQUIRED",
            "UPSTREAM_BASIS_BEARING_SCOPE_DIVISION_MISSING_BASIS_RESOLVED_REQUIRED",
            "UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True, name)
        self.assertTrue({resolver.OUTCOME_EMITTED, resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED}.issubset(resolver.OUTCOME_FAMILY))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min"))
        expected_codes = {
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_REFERENCE_MISSING",
            "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_MARKER_MISSING", "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING", "UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT",
            "NON_CLAIM_MISSING_OR_FLIPPED", "PROHIBITED_DISTINCTNESS_SUPPORT_REQUESTED",
            "PROHIBITED_CANDIDATE_RECORDS_DISTINCT_REQUESTED", "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
            "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED", "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
            "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        }
        self.assertTrue(expected_codes.issubset(resolver.BLOCK_CODES))

    def test_synthetic_emitted_result_wrapper_and_posture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(
                self.valid_request(self.marker_paths(Path(directory)))
            )
            self.assert_emitted(result)
            self.assertEqual(result["result_version"], "0.1.0")
            self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
            operation = self.operation(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[key], True, key)
            self.assertEqual(operation["basis_emission_successor_result"], "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED")
            self.assert_no_downstream_posture(result)
            for key in (
                "basis_emission_successor_operation_metadata", "declared_basis_emission_successor_operation_basis",
                "upstream_basis", self.OPERATION_KEY, self.MATERIAL_KEY, self.CHECKS_KEY,
                "basis_emission_successor_operation_statement", "basis_emission_successor_operation_non_meaning",
                "emission_result_detail", "permitted_future_route", "blocked_routes", "what_remains_open",
                "non_claims", "outcome", "block", self.SUMMARY_KEY,
            ):
                self.assertIn(key, result)
            self.assertEqual(result["emission_result_detail"]["missing_or_insufficient_successor_closure_basis"], [])
            self.assertTrue(all(value is True for key, value in operation.items() if key.endswith("_markers_present")))

    def test_emitted_basis_object_shape_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self.valid_request(self.marker_paths(Path(directory)))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request)
            self.assert_emitted(result)
            material = self.material(result)
            self.assertEqual(set(material), {"candidate_a_basis", "candidate_b_basis", "basis_pair"})
            candidate_a = material["candidate_a_basis"]
            candidate_b = material["candidate_b_basis"]
            pair = material["basis_pair"]
            self.assertIsInstance(candidate_a, dict)
            self.assertIsInstance(candidate_b, dict)
            self.assertIsInstance(pair, dict)
            self.assertEqual(candidate_a["basis_id"], resolver.CANDIDATE_A_BASIS_ID)
            self.assertEqual(candidate_a["candidate_record_id"], "descendant_body_basis_candidate_a_001")
            self.assertEqual(candidate_a["candidate_role"], "CANDIDATE_A")
            self.assertEqual(candidate_a["basis_label"], resolver.CANDIDATE_A_BASIS_LABEL)
            self.assertEqual(candidate_a["source_scope"], "Motion-side admissible variation")
            self.assertEqual(candidate_a["source_mandate"], "Motion mandate")
            self.assertEqual(candidate_a["basis_function"], "preserves variation side of parent basis")
            for term in ("preserve variation", "frequency", "rhythm", "phase", "amplitude", "periodicity", "latency", "no fixed values", "no targets", "no optimization", "no preferred trajectory", "no steering"):
                self.assertIn(term, candidate_a["responsibility_terms"])
            self.assertIs(candidate_a["non_standing_basis"], True)
            self.assertIs(candidate_a["standing_created"], False)
            self.assertIs(candidate_a["candidate_scope_declared"], False)
            self.assertIs(candidate_a["distinctness_supported"], False)
            self.assertEqual(candidate_b["basis_id"], resolver.CANDIDATE_B_BASIS_ID)
            self.assertEqual(candidate_b["candidate_record_id"], "descendant_body_basis_candidate_b_001")
            self.assertEqual(candidate_b["candidate_role"], "CANDIDATE_B")
            self.assertEqual(candidate_b["basis_label"], resolver.CANDIDATE_B_BASIS_LABEL)
            self.assertEqual(candidate_b["source_scope"], "Regulation-side admissibility bounds")
            self.assertEqual(candidate_b["source_mandate"], "Regulation mandate")
            self.assertEqual(candidate_b["basis_function"], "preserves admissibility-bound side of parent basis")
            for term in ("preserve bounds without collapsing motion", "coherence", "stability", "persistence", "damping", "modulation", "thresholds/ranges/rejection conditions", "no outcome encoding", "no constants", "no deciding trajectories", "no replacing motion with control"):
                self.assertIn(term, candidate_b["responsibility_terms"])
            self.assertIs(candidate_b["non_standing_basis"], True)
            self.assertIs(candidate_b["standing_created"], False)
            self.assertIs(candidate_b["candidate_scope_declared"], False)
            self.assertIs(candidate_b["distinctness_supported"], False)
            self.assertEqual(pair["basis_pair_scope"], resolver.BASIS_PAIR_SCOPE)
            for key in ("candidate_a_and_b_are_sibling_non_standing_basis_materials", "neither_candidate_ranks_above_the_other", "regulation_not_sovereign_over_motion", "motion_does_not_erase_regulation"):
                self.assertIs(pair[key], True, key)
            for key in ("coupling_assigned", "coupling_created", "third_candidate_created", "third_model_admitted", "distinctness_supported_recorded", "candidate_records_marked_distinct", "candidate_standing_authorized"):
                self.assertIs(pair[key], False, key)
            summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_EMITTED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["basis_emission_successor_result"], "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED")
            self.assertEqual(summary["candidate_a_basis_id"], resolver.CANDIDATE_A_BASIS_ID)
            self.assertEqual(summary["candidate_b_basis_id"], resolver.CANDIDATE_B_BASIS_ID)
            self.assertEqual(summary["candidate_a_basis_label"], resolver.CANDIDATE_A_BASIS_LABEL)
            self.assertEqual(summary["candidate_b_basis_label"], resolver.CANDIDATE_B_BASIS_LABEL)
            self.assertEqual(summary["basis_pair_scope"], resolver.BASIS_PAIR_SCOPE)
            self.assertEqual(summary["missing_or_insufficient_successor_closure_basis"], [])
            self.assertTrue(summary["basis_emission_successor_operation_spec_markers_present"])
            self.assertTrue(summary["successor_closure_operation_terminal_summary_markers_present"])

    def test_default_live_result_if_available(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_request()
        required_paths = [Path(value) if Path(value).is_absolute() else REPO_ROOT / value for key, value in request.items() if key.endswith("_reference")]
        if not all(path.is_file() for path in required_paths):
            self.skipTest("default target or upstream summaries are unavailable")
        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request)
        self.assert_emitted(result)
        self.assert_no_downstream_posture(result)
        self.assertEqual(set(self.material(result)), {"candidate_a_basis", "candidate_b_basis", "basis_pair"})

    def test_missing_upstream_basis_requires_successor_closure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            originals = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            cases = (
                ("prior_basis_emission_operation_terminal_summary_reference", None),
                ("prior_basis_emission_operation_terminal_summary_reference", resolver.PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED),
                ("successor_closure_operation_terminal_summary_reference", None),
                ("successor_closure_operation_terminal_summary_reference", "closure_basis_received = true"),
                ("distinctness_operation_terminal_summary_reference", None),
                ("distinctness_operation_terminal_summary_reference", "distinctness_supported = false"),
            )
            for index, (field, retained_marker) in enumerate(cases):
                with self.subTest(field=field, index=index):
                    request = self.valid_request(paths)
                    if retained_marker is None:
                        request[field] = str(root / self.safe_json_filename(f"missing_{field}", index))
                    else:
                        paths[field].write_text(retained_marker, encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request)
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE, resolver.OUTCOME_BLOCKED))
                    if result["outcome"] == resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE:
                        self.assert_requires_successor_closure(result)
                        self.assertTrue(result["emission_result_detail"]["missing_or_insufficient_successor_closure_basis"])
                        self.assertEqual(set(self.material(result).values()), {None})
                    else:
                        self.assert_blocked(result)
                    paths[field].write_text(originals[field], encoding="utf-8")
            marker_cases = {
                "prior_basis_emission_operation_terminal_summary_reference": (
                    resolver.PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
                    "missing non-cosmetic candidate A scope declaration",
                    "missing non-cosmetic candidate B scope declaration",
                    "missing basis-bearing scope division declaration",
                ),
                "successor_closure_operation_terminal_summary_reference": (
                    resolver.UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
                    resolver.UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
                    "prior_additional_basis_gap_closed = true",
                    "closure_basis_received = true",
                    "closure_basis_audited = true",
                    "closure_basis_digest_custody_sealed = true",
                    "candidate_a_missing_basis_resolved = true",
                    "candidate_b_missing_basis_resolved = true",
                    "basis_bearing_scope_division_missing_basis_resolved = true",
                    "declaration_accepted_as_basis = true",
                    "declaration_admitted_as_standing_basis = false",
                    "candidate_a_scope_declared = false",
                    "candidate_b_scope_declared = false",
                    "basis_bearing_scope_division_declared = false",
                    "distinctness_supported_recorded = false",
                    "candidate_records_marked_distinct = false",
                    "descendant_body_created = false",
                    "presence_established = false",
                    "identity_created = false",
                    "follow_on_authorized = false",
                ),
                "distinctness_operation_terminal_summary_reference": (
                    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                    "distinctness_result = NOT_DISTINCT",
                    "distinctness_supported = false",
                    "candidate-specific content was absent",
                    "separate seal, receipt, and digest material were absent",
                ),
            }
            for field, markers in marker_cases.items():
                for index, marker in enumerate(markers):
                    with self.subTest(corrupt_marker_field=field, marker=marker):
                        path = paths[field]
                        corrupted = originals[field].replace(marker, f"MISSING_{index}", 1)
                        if marker == resolver.UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED:
                            corrupted = corrupted.replace("prior_additional_basis_gap_closed", "missing_prior_gap_result")
                        path.write_text(corrupted, encoding="utf-8")
                        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(
                            self.valid_request(paths)
                        )
                        self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE, resolver.OUTCOME_BLOCKED))
                        if result["outcome"] == resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE:
                            self.assert_requires_successor_closure(result)
                        else:
                            self.assert_blocked(result)
                        path.write_text(originals[field], encoding="utf-8")

    def test_do_not_record_and_explicit_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self.valid_request(self.marker_paths(Path(directory)))
            do_not_record = copy.deepcopy(request)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(result["block"]["blocked"], False)
            operation = self.operation(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[key], False, key)
            self.assertEqual(set(self.material(result).values()), {None})
            self.assert_no_downstream_posture(result)
            self.assert_non_claims_false(result)
            blocked = copy.deepcopy(request)
            blocked["intent"] = resolver.INTENT_BLOCK
            self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(blocked))

    def test_request_shape_exact_fields_and_marker_classes_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            base = self.valid_request(paths)
            for key, wrong in (
                ("operation_id", "wrong"), ("operation_type", "wrong"), ("operation_version", "wrong"),
                ("operation_scope", "wrong"), ("prior_basis_emission_operation_type", "wrong"),
                ("prior_basis_emission_operation_outcome_required", "wrong"),
                ("upstream_successor_closure_operation_type", "wrong"),
                ("upstream_successor_closure_operation_outcome_required", "wrong"),
                ("upstream_successor_closure_result_required", "wrong"),
                ("upstream_prior_additional_basis_gap_closed_required", False),
                ("upstream_closure_basis_received_required", False),
                ("upstream_closure_basis_audited_required", False),
                ("upstream_closure_basis_digest_custody_sealed_required", False),
                ("upstream_candidate_a_missing_basis_resolved_required", False),
                ("upstream_candidate_b_missing_basis_resolved_required", False),
                ("upstream_basis_bearing_scope_division_missing_basis_resolved_required", False),
                ("upstream_declaration_accepted_as_basis_required", False),
                ("target_primary_material_filename", "wrong"),
                ("target_primary_material_digest_sha256", "wrong"), ("candidate_a_basis_id", "wrong"),
                ("candidate_b_basis_id", "wrong"), ("candidate_a_basis_label", "wrong"),
                ("candidate_b_basis_label", "wrong"), ("basis_pair_scope", "wrong"),
                ("admissible_future_route", "wrong"),
            ):
                with self.subTest(request_key=key):
                    request = copy.deepcopy(base)
                    request[key] = wrong
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request))
            self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min([]))
            unsupported = copy.deepcopy(base)
            unsupported["intent"] = "UNSUPPORTED"
            self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(unsupported))
            originals = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            for index, (field, path) in enumerate(paths.items()):
                with self.subTest(marker_field=field):
                    path.write_text("missing marker class", encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(self.valid_request(paths))
                    if field == "operation_spec_reference":
                        self.assert_blocked(result)
                    else:
                        self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_SUCCESSOR_CLOSURE, resolver.OUTCOME_BLOCKED))
                        self.assert_public_codes(result)
                        self.assert_non_claims_false(result)
                    self.assertTrue(self.safe_json_filename(field, index).endswith(".json"))
                    path.write_text(originals[field], encoding="utf-8")

    def test_prohibited_flags_and_false_posture_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = self.valid_request(self.marker_paths(Path(directory)))
            for flag in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(flag=flag):
                    request = copy.deepcopy(base)
                    request[flag] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level_false_posture=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request))
                with self.subTest(declared_non_claim=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][key], False)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(preclaim=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request))
            malformed = (
                None,
                [],
                {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]},
                {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            )
            for index, declared in enumerate(malformed):
                with self.subTest(declared_non_claims=index):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"] = declared
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request))

    def test_path_write_non_mutation_and_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            request = self.valid_request(paths)
            request["raw_pdf_body"] = "RAW_BASIS_BODY_MUST_NOT_RETURN"
            original_request = copy.deepcopy(request)
            original_text = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_from_path(request_path)
            self.assert_emitted(result)
            self.assertEqual(request, original_request)
            for key, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), original_text[key])
            self.assertNotIn("RAW_BASIS_BODY_MUST_NOT_RETURN", json.dumps(result, sort_keys=True))
            first = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_result(result, root / "output")
            second = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_result(result, root / "output")
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("basis_emission_successor_operation_v0_min_result", first.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min", str(resolver.REPO_ROOT / resolver.OUTPUT_ROOT))
            for prior_root in (
                "successor_closure_operation_v0_min",
                "authored_scope_division_declaration_receipt_operation",
                "authored_scope_division_declaration_audit_operation",
                "authored_scope_division_declaration_digest_custody_operation",
                "candidate_specific_distinctness_basis_emission_operation_v0_min",
                "candidate_record_distinctness_operation",
            ):
                self.assertNotIn(prior_root, str(first.parent))
            written = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(written["outcome"], resolver.OUTCOME_EMITTED)
            self.assertEqual(set(written[self.MATERIAL_KEY]), {"candidate_a_basis", "candidate_b_basis", "basis_pair"})
            for name, contents in (("missing.json", None), ("malformed.json", "{"), ("array.json", "[]")):
                path = root / name
                if contents is not None:
                    path.write_text(contents, encoding="utf-8")
                self.assert_blocked(resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_from_path(path))


if __name__ == "__main__":
    unittest.main()
