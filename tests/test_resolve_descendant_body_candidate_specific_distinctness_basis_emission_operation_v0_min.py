"""Tests for the candidate-specific distinctness basis emission operation resolver.

The target resolver has two lawful clean paths: default current/live posture
records REQUIRES_ADDITIONAL_BASIS because no non-cosmetic A/B scope division is
declared, and an explicit non-cosmetic scope-division request records bounded
non-standing emitted basis material. The tests keep that emission distinct from
distinctness support, candidate standing, descendant bodies, runtime, authority,
scan, repair, validation enforcement, and follow-on work.
"""

from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min as resolver


class CandidateSpecificDistinctnessBasisEmissionOperationTests(unittest.TestCase):
    maxDiff = None

    OPERATION_SPEC_TEXT = """
# Descendant Body Candidate-Specific Distinctness Basis Emission Operation V0 Minimum Specification
This file defines one future candidate-specific distinctness basis emission operation.
This file is operation-spec-only.
This file does not implement or perform the operation.
This file does not emit candidate-specific content, separate seal material, separate lineage receipt material, or separate digest material.
SCOPE_DIVISION_ONLY
REQUIRE_NON_COSMETIC_SCOPE_DIVISION
EMIT_ONLY_NON_STANDING_BASIS_BEARING_CONTENT
SEAL_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_CONTENT
RECEIPT_ONLY_NON_COSMETIC_SCOPE_DIVISION
DIGEST_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_MATERIAL
COSMETIC_SUBSTITUTION_NOT_BASIS
DIGEST_LAUNDERING_NOT_BASIS
ID_ROLE_LABEL_DIFFERENCE_NOT_BASIS
SHARED_EVIDENCE_NOT_BASIS
OPERATION_EVIDENCE_ALONE_NOT_BASIS
Success requires non-cosmetic scope division and basis-bearing candidate-specific material.
No implementation exists in this spec.
candidate_specific_distinctness_basis_emission_operation_implemented = false
candidate_specific_distinctness_basis_emission_operation_recorded = false
candidate_specific_content_emitted = false
distinctness_supported_recorded = false
candidate_standing_authorized = false
"""

    UPSTREAM_BOUNDARY_TEXT = """
# Boundary Summary
DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED
failed_check_count 0
passed_check_count 131
result_version 0.2.0
SCOPE_DIVISION_ONLY
COSMETIC_DIFFERENCE_CRYPTOGRAPHICALLY_DRESSED_AS_DISTINCTNESS
scope_division_route_allowed_for_future_operation_shape = true
NOT_DISTINCT as a clean upstream operation result
Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis
Candidate-specific basis must be basis-bearing, not label-bearing
does not define, implement, or perform emission operation
does not emit candidate-specific content
does not rerun distinctness
does not record DISTINCTNESS_SUPPORTED
"""

    DISTINCTNESS_OPERATION_TEXT = """
# Distinctness Operation Summary
DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT
distinctness_result = NOT_DISTINCT
failed_check_count = 0
candidate_record_count_compared = 2
candidate_ids_distinct = true
candidate_roles_distinct = true
id_and_role_difference_only = true
candidate_specific_content_present = false
separate_seal_material_present = false
separate_lineage_receipt_material_present = false
separate_digest_material_present = false
distinctness_supported = false
NOT_DISTINCT is a clean operation result, not a failure.
missing candidate-specific content
missing separate seal material
missing separate lineage receipt material
missing separate digest material
id and role difference alone is not distinctness
shared evidence reference alone is not distinctness
Operation evidence alone is not distinctness.
"""

    DIFFERENTIATION_TEXT = """
# Differentiation Operation Summary
DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED
completed descendant-body differentiation operation line exists.
completed operation result emitted.
emitted exactly two result-contained non-standing candidate records.
candidate records are operation-evidenced through operation evidence.
candidate records are non-standing.
candidate records are not descendant bodies.
descendant bodies not created.
standing descendants not created.
first crossing not authorized.
relation not created.
"""

    DISTINCTNESS_BOUNDARY_TEXT = """
# Distinctness Boundary Summary
DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED
enumeration is not distinction
id and role difference alone are not distinctness
shared evidence reference alone is not distinctness
distinctness support requires separate candidate-specific evidence
candidate standing is not authorized
"""

    SENTINELS = (
        "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
        "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
        "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, path: Path, value: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def write_synthetic_basis(self, base: Path, *, sentinels: bool = False) -> dict[str, Path]:
        suffix = "\nraw_body: " + "\n".join(self.SENTINELS) if sentinels else ""
        files = {
            "operation_spec": self.write_text(base / "basis" / "operation_spec.md", self.OPERATION_SPEC_TEXT + suffix),
            "boundary": self.write_text(base / "basis" / "boundary_summary.md", self.UPSTREAM_BOUNDARY_TEXT + suffix),
            "distinctness_operation": self.write_text(
                base / "basis" / "distinctness_operation_summary.md",
                self.DISTINCTNESS_OPERATION_TEXT + suffix,
            ),
            "differentiation": self.write_text(
                base / "basis" / "differentiation_summary.md",
                self.DIFFERENTIATION_TEXT + suffix,
            ),
            "distinctness_boundary": self.write_text(
                base / "basis" / "distinctness_boundary_summary.md",
                self.DISTINCTNESS_BOUNDARY_TEXT + suffix,
            ),
            "boundary_artifact": self.write_json(
                base / "basis" / "boundary_artifact.json",
                {"outcome": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED"},
            ),
        }
        return files

    def build_valid_request(self, files: dict[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request(
            operation_spec_reference=str(files["operation_spec"]),
            candidate_specific_distinctness_basis_emission_boundary_reference=str(files["boundary"]),
            candidate_specific_distinctness_basis_emission_boundary_artifact_reference=str(files["boundary_artifact"]),
            completed_distinctness_operation_terminal_summary_reference=str(files["distinctness_operation"]),
            completed_differentiation_operation_terminal_summary_reference=str(files["differentiation"]),
            completed_distinctness_operation_boundary_terminal_summary_reference=str(files["distinctness_boundary"]),
        )

    def build_supported_request(self, files: dict[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request(
            operation_spec_reference=str(files["operation_spec"]),
            candidate_specific_distinctness_basis_emission_boundary_reference=str(files["boundary"]),
            candidate_specific_distinctness_basis_emission_boundary_artifact_reference=str(files["boundary_artifact"]),
            completed_distinctness_operation_terminal_summary_reference=str(files["distinctness_operation"]),
            completed_differentiation_operation_terminal_summary_reference=str(files["differentiation"]),
            completed_distinctness_operation_boundary_terminal_summary_reference=str(files["distinctness_boundary"]),
            candidate_a_scope_id="candidate_a_scope_content_integrity",
            candidate_b_scope_id="candidate_b_scope_receipt_traceability",
            candidate_a_scope_statement="content-integrity sub-scope for non-standing candidate-specific basis emission",
            candidate_b_scope_statement="receipt-traceability sub-scope for non-standing candidate-specific basis emission",
            candidate_a_scope_basis="mandate/function/responsibility/governed-surface content integrity basis, not id/role/label",
            candidate_b_scope_basis="mandate/function/responsibility/governed-surface receipt traceability basis, not id/role/label",
            scope_division_non_cosmetic=True,
            candidate_specific_content_basis_bearing=True,
        )

    def operation(self, result: dict[str, Any]) -> dict[str, Any]:
        value = result.get("descendant_body_candidate_specific_distinctness_basis_emission_operation")
        self.assertIsInstance(value, dict)
        return value

    def material(self, result: dict[str, Any]) -> dict[str, Any]:
        value = result.get("descendant_body_candidate_specific_distinctness_basis_emission_material")
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        value = result.get("candidate_specific_distinctness_basis_emission_operation_checks")
        self.assertIsInstance(value, list)
        return value

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return str(code) if code is not None else None

    def failed_check_count(self, result: dict[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is not True)

    def passed_check_count(self, result: dict[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_requires_additional_basis_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_recorded_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_blocked_public(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_check_count(result), 0)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_downstream_creation(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, check)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_operation_wrapper_separate(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        forbidden = {
            "outcome",
            "block",
            "candidate_specific_distinctness_basis_emission_operation_checks",
            "non_claims",
            "candidate_specific_distinctness_basis_emission_operation_summary",
            "candidate_specific_distinctness_basis_emission_operation_metadata",
            "descendant_body_candidate_specific_distinctness_basis_emission_material",
        }
        self.assertFalse(forbidden.intersection(operation))

    def assert_no_raw_bodies(self, result: dict[str, Any]) -> None:
        encoded = json.dumps(result, sort_keys=True)
        for sentinel in self.SENTINELS:
            self.assertNotIn(sentinel, encoded)
        self.assertNotIn("raw_body", encoded)
        self.assertNotIn("full_body", encoded)
        self.assertNotIn("hidden_repo_state", encoded)
        self.assertNotIn("current_working_tree", encoded)

    def assert_material_has_no_raw_bodies(self, result: dict[str, Any]) -> None:
        material = self.material(result)
        encoded = json.dumps(material, sort_keys=True)
        for sentinel in self.SENTINELS:
            self.assertNotIn(sentinel, encoded)
        for key in material:
            self.assertFalse(key.endswith("_body"), key)

    def assert_no_downstream_creation(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
        material = self.material(result)
        for key in (
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_authorized",
            "field_machinery_authorized",
            "runtime_authorized",
            "currentness_authorized",
            "authority_authorized",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
        ):
            self.assertIs(operation.get(key), False, key)
        if result["outcome"] != resolver.OUTCOME_RECORDED:
            self.assertIs(operation.get("candidate_specific_content_emitted"), False)
            self.assertIs(operation.get("separate_seal_material_emitted"), False)
            self.assertIs(operation.get("separate_lineage_receipt_material_emitted"), False)
            self.assertIs(operation.get("separate_digest_material_emitted"), False)
            self.assertIs(material.get("material_emitted"), False)

    def assert_hex_64(self, value: str) -> None:
        self.assertRegex(value, r"^[0-9a-f]{64}$")

    def assert_default_additional_basis_result(self, result: dict[str, Any]) -> None:
        self.assert_requires_additional_basis_not_blocked(result)
        summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary(result)
        operation = self.operation(result)
        material = self.material(result)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertEqual(
            operation["candidate_specific_distinctness_basis_emission_operation_type"],
            resolver.OPERATION_TYPE,
        )
        self.assertEqual(operation["candidate_specific_distinctness_basis_emission_operation_version"], "0.1.0")
        self.assertEqual(operation["candidate_specific_distinctness_basis_emission_operation_scope"], resolver.OPERATION_SCOPE)
        for key in (
            "candidate_specific_distinctness_basis_emission_operation_recorded",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "scope_division_non_cosmetic",
            "candidate_specific_content_basis_bearing",
            "emitted_basis_non_standing",
        ):
            self.assertIs(operation[key], False, key)
        for key in (
            "operation_spec_markers_present",
            "upstream_boundary_terminal_summary_markers_present",
            "completed_distinctness_operation_terminal_summary_markers_present",
            "completed_differentiation_operation_terminal_summary_markers_present",
            "completed_distinctness_operation_boundary_terminal_summary_markers_present",
        ):
            self.assertIs(operation[key], True, key)
        self.assertIn("missing non-cosmetic candidate A scope", result["additional_basis_required"])
        self.assertIn("missing non-cosmetic candidate B scope", result["additional_basis_required"])
        self.assertIn("missing basis-bearing scope division", result["additional_basis_required"])
        self.assertIs(material["material_emitted"], False)
        for key in (
            "candidate_a_candidate_specific_content_reference",
            "candidate_b_candidate_specific_content_reference",
            "candidate_a_seal_reference",
            "candidate_b_seal_reference",
            "candidate_a_lineage_receipt_reference",
            "candidate_b_lineage_receipt_reference",
            "candidate_a_digest_reference",
            "candidate_b_digest_reference",
            "candidate_a_digest_value",
            "candidate_b_digest_value",
        ):
            self.assertEqual(material[key], "", key)
        self.assert_no_downstream_creation(result)
        self.assert_operation_wrapper_separate(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_material_has_no_raw_bodies(result)

    def assert_supported_recorded_result(self, result: dict[str, Any]) -> None:
        self.assert_recorded_not_blocked(result)
        operation = self.operation(result)
        material = self.material(result)
        for key in (
            "candidate_specific_distinctness_basis_emission_operation_recorded",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "scope_division_non_cosmetic",
            "candidate_specific_content_basis_bearing",
            "emitted_basis_non_standing",
            "candidate_records_remain_non_standing",
            "candidate_records_remain_not_descendant_bodies",
        ):
            self.assertIs(operation[key], True, key)
        self.assertIs(material["material_emitted"], True)
        self.assertEqual(material["candidate_a_scope_id"], "candidate_a_scope_content_integrity")
        self.assertEqual(material["candidate_b_scope_id"], "candidate_b_scope_receipt_traceability")
        self.assertIn("content-integrity", material["candidate_a_scope_statement"])
        self.assertIn("receipt-traceability", material["candidate_b_scope_statement"])
        self.assertIn("content integrity", material["candidate_a_scope_basis_summary"])
        self.assertIn("receipt traceability", material["candidate_b_scope_basis_summary"])
        for key in (
            "candidate_a_candidate_specific_content_reference",
            "candidate_b_candidate_specific_content_reference",
            "candidate_a_seal_reference",
            "candidate_b_seal_reference",
            "candidate_a_lineage_receipt_reference",
            "candidate_b_lineage_receipt_reference",
            "candidate_a_digest_reference",
            "candidate_b_digest_reference",
        ):
            self.assertTrue(material[key].startswith("result://"), key)
        hash_keys = (
            "candidate_a_scope_hash",
            "candidate_b_scope_hash",
            "candidate_a_content_hash",
            "candidate_b_content_hash",
            "candidate_a_seal_hash",
            "candidate_b_seal_hash",
            "candidate_a_lineage_receipt_hash",
            "candidate_b_lineage_receipt_hash",
            "candidate_a_digest_value",
            "candidate_b_digest_value",
        )
        for key in hash_keys:
            self.assert_hex_64(material[key])
        self.assertNotEqual(material["candidate_a_content_hash"], material["candidate_b_content_hash"])
        self.assertNotEqual(material["candidate_a_seal_hash"], material["candidate_b_seal_hash"])
        self.assertNotEqual(material["candidate_a_lineage_receipt_hash"], material["candidate_b_lineage_receipt_hash"])
        self.assertNotEqual(material["candidate_a_digest_value"], material["candidate_b_digest_value"])
        for key in (
            "cosmetic_substitution_treated_as_basis",
            "digest_laundering_treated_as_basis",
            "id_role_label_difference_treated_as_basis",
            "shared_evidence_treated_as_basis",
            "operation_evidence_alone_treated_as_basis",
        ):
            self.assertIs(material[key], False, key)
        self.assert_no_downstream_creation(result)
        self.assert_operation_wrapper_separate(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_material_has_no_raw_bodies(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min",
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path",
            "write_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_result",
            "build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected_values = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": "resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min",
            "OPERATION_TYPE": "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": "TWO_NON_STANDING_CANDIDATE_RECORDS_SCOPE_DIVISION_ONLY",
            "ADMISSIBLE_FUTURE_BASIS_ROUTE": "SCOPE_DIVISION_ONLY",
            "SCOPE_DIVISION_POLICY": "REQUIRE_NON_COSMETIC_SCOPE_DIVISION",
            "CANDIDATE_SPECIFIC_CONTENT_POLICY": "EMIT_ONLY_NON_STANDING_BASIS_BEARING_CONTENT",
            "SEPARATE_SEAL_MATERIAL_POLICY": "SEAL_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_CONTENT",
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_POLICY": "RECEIPT_ONLY_NON_COSMETIC_SCOPE_DIVISION",
            "SEPARATE_DIGEST_MATERIAL_POLICY": "DIGEST_ONLY_NON_COSMETIC_CANDIDATE_SPECIFIC_MATERIAL",
            "COSMETIC_SUBSTITUTION_POLICY": "COSMETIC_SUBSTITUTION_NOT_BASIS",
            "DIGEST_LAUNDERING_POLICY": "DIGEST_LAUNDERING_NOT_BASIS",
            "ID_ROLE_LABEL_DIFFERENCE_POLICY": "ID_ROLE_LABEL_DIFFERENCE_NOT_BASIS",
            "SHARED_EVIDENCE_POLICY": "SHARED_EVIDENCE_NOT_BASIS",
            "OPERATION_EVIDENCE_POLICY": "OPERATION_EVIDENCE_ALONE_NOT_BASIS",
            "CANDIDATE_A_ID": "descendant_body_basis_candidate_a_001",
            "CANDIDATE_B_ID": "descendant_body_basis_candidate_b_001",
            "CANDIDATE_A_ROLE": "CANDIDATE_A",
            "CANDIDATE_B_ROLE": "CANDIDATE_B",
        }
        for name, value in expected_values.items():
            self.assertEqual(getattr(resolver, name), value)
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).replace("\\", "/").endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min"
            )
        )
        required_false = {
            "candidate_specific_distinctness_basis_emission_operation_implemented",
            "candidate_specific_distinctness_basis_emission_operation_created",
            "candidate_specific_distinctness_basis_emission_operation_performed",
            "candidate_specific_distinctness_basis_emission_operation_recorded",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
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
            "follow_on_work_authorized",
            "affected_file_repaired",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "candidate_specific_distinctness_basis_emission_boundary_overridden",
            "candidate_specific_distinctness_basis_emission_boundary_bypassed",
            "cosmetic_substitution_treated_as_basis",
            "digest_laundering_treated_as_basis",
            "id_role_label_difference_treated_as_basis",
            "shared_evidence_treated_as_basis",
            "operation_evidence_alone_treated_as_basis",
            "divergent_receipt_history_route_authorized",
            "carrier_separation_route_authorized",
        }
        expected_result_level_non_claims = required_false - {"standing_authorized", "crossing_authorized"}
        self.assertTrue(expected_result_level_non_claims.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS)))
        allowed_true = set(resolver.ALLOWED_TRUE_RECORDED_FIELDS) | set(
            getattr(resolver, "ALLOWED_TRUE_REQUIRES_ADDITIONAL_BASIS_FIELDS", ())
        )
        self.assertTrue(
            {
                "candidate_specific_distinctness_basis_emission_operation_recorded",
                "candidate_specific_content_emitted",
                "separate_seal_material_emitted",
                "separate_lineage_receipt_material_emitted",
                "separate_digest_material_emitted",
                "scope_division_non_cosmetic",
                "candidate_specific_content_basis_bearing",
                "emitted_basis_non_standing",
                "candidate_records_remain_non_standing",
                "candidate_records_remain_not_descendant_bodies",
                "operation_spec_markers_present",
                "upstream_boundary_terminal_summary_markers_present",
                "completed_distinctness_operation_terminal_summary_markers_present",
                "completed_differentiation_operation_terminal_summary_markers_present",
                "completed_distinctness_operation_boundary_terminal_summary_markers_present",
                "additional_basis_required_recorded",
                "missing_candidate_a_scope_recorded",
                "missing_candidate_b_scope_recorded",
                "missing_non_cosmetic_scope_division_recorded",
                "result_level_non_claims_canonical_false",
            }.issubset(allowed_true)
        )
        expected_codes = {
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TYPE_NOT_EXPECTED",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_VERSION_NOT_0_1_0",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_SCOPE_NOT_EXPECTED",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REFERENCE_MISSING",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            "OPERATION_SPEC_REFERENCE_MISSING",
            "CANDIDATE_A_SCOPE_MISSING",
            "CANDIDATE_B_SCOPE_MISSING",
            "SCOPE_DIVISION_MISSING",
            "CANDIDATE_SCOPES_IDENTICAL",
            "CANDIDATE_SCOPES_COSMETIC_ONLY",
            "CANDIDATE_SCOPES_TEMPLATE_SUBSTITUTION_ONLY",
            "CANDIDATE_SCOPE_RELIES_ON_CONTAMINATED_LINEAGE_AS_CLEAN_BASIS",
            "SCOPE_DIVISION_REQUIRES_ADDITIONAL_BASIS",
            "OPERATION_SPEC_MARKER_MISSING",
            "UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            "DISTINCTNESS_OPERATION_RERUN_TRUE",
            "DISTINCTNESS_SUPPORTED_RECORDED_TRUE",
            "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE",
            "CANDIDATE_STANDING_AUTHORIZED_TRUE",
            "DESCENDANT_BODY_CREATED_TRUE",
            "CROSSING_AUTHORIZED_TRUE",
            "RELATION_AUTHORIZED_TRUE",
            "FIELD_MACHINERY_AUTHORIZED_TRUE",
            "RUNTIME_AUTHORIZED_TRUE",
            "CURRENTNESS_AUTHORIZED_TRUE",
            "AUTHORITY_AUTHORIZED_TRUE",
            "FOLLOW_ON_AUTHORIZED_TRUE",
            "REQUESTED_DISTINCTNESS_OPERATION_RERUN",
            "REQUESTED_DISTINCTNESS_SUPPORTED_RECORDING",
            "REQUESTED_CANDIDATE_RECORDS_MARKED_DISTINCT",
            "REQUESTED_REPOSITORY_SCAN",
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
            "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS",
            "DIGEST_LAUNDERING_TREATED_AS_BASIS",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS",
            "SHARED_EVIDENCE_TREATED_AS_BASIS",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS",
            "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED",
            "CARRIER_SEPARATION_ROUTE_AUTHORIZED",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_OVERRIDDEN",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BYPASSED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_MALFORMED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUEST_UNREADABLE",
        }
        self.assertTrue(expected_codes.issubset(set(resolver.BLOCK_CODES)))

    def test_default_synthetic_basis_requires_additional_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_valid_request(self.write_synthetic_basis(Path(tmp)))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assertIsInstance(result, dict)
            self.assertEqual(
                self.operation(result)["candidate_specific_distinctness_basis_emission_operation_id"],
                "descendant_body_candidate_specific_distinctness_basis_emission_operation_001",
            )
            self.assert_default_additional_basis_result(result)

    def test_supported_synthetic_scope_division_records_operation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_supported_request(self.write_synthetic_basis(Path(tmp)))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assert_supported_recorded_result(result)

    def test_cosmetic_or_label_derived_scope_requests_do_not_record(self) -> None:
        cases = {
            "identical_scopes": lambda request: request.update(
                {
                    "candidate_b_scope_id": request["candidate_a_scope_id"],
                    "candidate_b_scope_statement": request["candidate_a_scope_statement"],
                    "candidate_b_scope_basis": request["candidate_a_scope_basis"],
                }
            ),
            "label_only_statement": lambda request: request.update(
                {
                    "candidate_a_scope_id": "candidate_a_label_scope",
                    "candidate_b_scope_id": "candidate_b_label_scope",
                    "candidate_a_scope_statement": "candidate A label scope",
                    "candidate_b_scope_statement": "candidate B label scope",
                    "candidate_a_scope_basis": "candidate A role label basis",
                    "candidate_b_scope_basis": "candidate B role label basis",
                }
            ),
            "template_substitution_only": lambda request: request.update(
                {"candidate_scopes_template_substitution_only": True}
            ),
            "cosmetic_substitution_as_basis": lambda request: request.update(
                {
                    "candidate_a_scope_basis": "cosmetic substitution is basis",
                    "cosmetic_substitution_treated_as_basis": True,
                    "declared_non_claims": {
                        **request["declared_non_claims"],
                        "cosmetic_substitution_treated_as_basis": False,
                    },
                }
            ),
            "digest_laundering_as_basis": lambda request: request.update(
                {
                    "candidate_b_scope_basis": "digest laundering is basis",
                    "digest_laundering_treated_as_basis": True,
                    "declared_non_claims": {
                        **request["declared_non_claims"],
                        "digest_laundering_treated_as_basis": False,
                    },
                }
            ),
            "contaminated_lineage_as_basis": lambda request: request.update(
                {
                    "candidate_a_scope_basis": (
                        "mandate/function/responsibility governed surface basis from "
                        "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC"
                    )
                }
            ),
        }
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp))
            for name, mutate in cases.items():
                with self.subTest(name=name):
                    request = self.build_supported_request(files)
                    mutate(request)
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request
                    )
                    self.assertIn(result["outcome"], (resolver.OUTCOME_BLOCKED, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_public(result)
                    else:
                        self.assert_default_additional_basis_result(result)

    def test_records_default_live_target_if_present(self) -> None:
        required = [
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2/descendant_body_candidate_specific_distinctness_basis_emission_boundary_001__candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result.json",
        ]
        missing = [path for path in required if not path.exists()]
        if missing:
            self.skipTest(f"default live target missing: {missing[0]}")
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_request()
        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
        self.assert_default_additional_basis_result(result)

    def test_do_not_record_intent_does_not_record_operation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_valid_request(self.write_synthetic_basis(Path(tmp)))
            request["candidate_specific_distinctness_basis_emission_operation_intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            self.assert_no_downstream_creation(result)
            self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_valid_request(self.write_synthetic_basis(Path(tmp)))
            request["candidate_specific_distinctness_basis_emission_operation_intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assert_blocked_public(result)

    def test_request_shape_and_blocking_behavior(self) -> None:
        cases: list[tuple[str, Any, str | None]] = [
            ("non_mapping", [], None),
            ("missing_question", ("candidate_specific_distinctness_basis_emission_operation_question", ""), None),
            ("unsupported_intent", ("candidate_specific_distinctness_basis_emission_operation_intent", "UNSUPPORTED"), None),
            ("missing_operation_type", ("candidate_specific_distinctness_basis_emission_operation_type", ""), None),
            ("wrong_operation_type", ("candidate_specific_distinctness_basis_emission_operation_type", "WRONG"), None),
            ("missing_operation_version", ("candidate_specific_distinctness_basis_emission_operation_version", ""), None),
            ("wrong_operation_version", ("candidate_specific_distinctness_basis_emission_operation_version", "9.9.9"), None),
            ("missing_operation_scope", ("candidate_specific_distinctness_basis_emission_operation_scope", ""), None),
            ("wrong_operation_scope", ("candidate_specific_distinctness_basis_emission_operation_scope", "WRONG"), None),
            ("missing_boundary_reference", ("candidate_specific_distinctness_basis_emission_boundary_reference", ""), None),
            ("missing_boundary_artifact_reference", ("candidate_specific_distinctness_basis_emission_boundary_artifact_reference", ""), None),
            ("missing_operation_spec_reference", ("operation_spec_reference", ""), None),
            ("missing_distinctness_summary", ("completed_distinctness_operation_terminal_summary_reference", ""), None),
            ("missing_differentiation_summary", ("completed_differentiation_operation_terminal_summary_reference", ""), None),
            ("missing_distinctness_boundary", ("completed_distinctness_operation_boundary_terminal_summary_reference", ""), None),
            ("wrong_candidate_a_id", ("candidate_record_a_id", "wrong"), None),
            ("wrong_candidate_b_id", ("candidate_record_b_id", "wrong"), None),
            ("wrong_candidate_a_role", ("candidate_record_a_role", "wrong"), None),
            ("wrong_candidate_b_role", ("candidate_record_b_role", "wrong"), None),
            ("missing_parent_basis", ("parent_basis_reference", ""), None),
            ("wrong_route", ("admissible_future_basis_route", "WRONG"), None),
            ("wrong_scope_policy", ("scope_division_policy", "WRONG"), None),
            ("wrong_content_policy", ("candidate_specific_content_policy", "WRONG"), None),
            ("wrong_seal_policy", ("separate_seal_material_policy", "WRONG"), None),
            ("wrong_receipt_policy", ("separate_lineage_receipt_material_policy", "WRONG"), None),
            ("wrong_digest_policy", ("separate_digest_material_policy", "WRONG"), None),
            ("wrong_cosmetic_policy", ("cosmetic_substitution_policy", "WRONG"), None),
            ("wrong_laundering_policy", ("digest_laundering_policy", "WRONG"), None),
            ("wrong_label_policy", ("id_role_label_difference_policy", "WRONG"), None),
            ("wrong_shared_policy", ("shared_evidence_policy", "WRONG"), None),
            ("wrong_operation_policy", ("operation_evidence_policy", "WRONG"), None),
        ]
        true_flags = [
            "divergent_receipt_history_route_authorized",
            "carrier_separation_route_authorized",
            "scan_allowed",
            "repair_allowed",
            "validation_enforcement_allowed",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_authorized",
            "field_machinery_authorized",
            "runtime_authorized",
            "currentness_authorized",
            "authority_authorized",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "request_distinctness_operation_rerun",
            "request_distinctness_supported_recording",
            "request_candidate_records_marked_distinct",
            "request_repository_scan",
            "request_file_discovery",
            "request_affected_file_repair",
            "request_affected_file_mutation",
            "request_prior_unsupported_claim_validation",
            "request_existence_claim_evidence_check_override",
            "request_existence_claim_evidence_check_bypass",
            "request_differentiation_operation_override",
            "request_differentiation_operation_bypass",
            "request_distinctness_operation_boundary_override",
            "request_distinctness_operation_boundary_bypass",
            "request_distinctness_operation_override",
            "request_distinctness_operation_bypass",
            "request_candidate_specific_distinctness_basis_emission_boundary_override",
            "request_candidate_specific_distinctness_basis_emission_boundary_bypass",
            "request_candidate_standing_authorization",
            "request_descendant_body_creation",
            "request_standing_descendant_creation",
            "request_descendant_standing_check",
            "request_crossing_authorization",
            "request_relation_creation",
            "request_field_machinery_creation",
            "request_runtime_creation",
            "request_currentness_creation",
            "request_authority_creation",
            "request_output_authorization",
            "request_action_authorization",
            "request_derivative_reception_authorization",
            "request_synchronization_authorization",
            "request_follow_on_authorization",
            "return_raw_markdown_body",
        ]
        cases.extend((f"{flag}_true", (flag, True), None) for flag in true_flags)
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp))
            for name, mutation, _ in cases:
                with self.subTest(name=name):
                    if name == "non_mapping":
                        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                            mutation
                        )
                    else:
                        request = self.build_valid_request(files)
                        key, value = mutation
                        request[key] = value
                        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                            request
                        )
                    self.assert_blocked_public(result)

    def test_marker_validation_blocking_behavior(self) -> None:
        marker_cases = {
            "operation_spec": ("operation_spec", "SCOPE_DIVISION_ONLY", "OPERATION_SPEC_MARKER_MISSING"),
            "boundary": ("boundary", "SCOPE_DIVISION_ONLY", "UPSTREAM_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"),
            "distinctness_operation": (
                "distinctness_operation",
                "distinctness_result = NOT_DISTINCT",
                "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            "differentiation": (
                "differentiation",
                "candidate records are non-standing",
                "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            "distinctness_boundary": (
                "distinctness_boundary",
                "enumeration is not distinction",
                "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
        }
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, (name, (file_key, marker, expected_code)) in enumerate(marker_cases.items()):
                with self.subTest(name=name):
                    files = self.write_synthetic_basis(base / f"case_{index}")
                    path = files[file_key]
                    path.write_text(path.read_text(encoding="utf-8").replace(marker, ""), encoding="utf-8")
                    request = self.build_valid_request(files)
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request
                    )
                    self.assert_blocked_public(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        fields = [
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "candidate_standing_created",
            "descendant_body_a_created",
            "descendant_body_b_created",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
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
            "follow_on_authorized",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "valid_derivation_event_recorded",
            "affected_file_repaired",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "existence_claim_evidence_check_overridden",
            "existence_claim_evidence_check_bypassed",
            "differentiation_operation_overridden",
            "differentiation_operation_bypassed",
            "distinctness_operation_boundary_overridden",
            "distinctness_operation_boundary_bypassed",
            "distinctness_operation_overridden",
            "distinctness_operation_bypassed",
            "candidate_specific_distinctness_basis_emission_boundary_overridden",
            "candidate_specific_distinctness_basis_emission_boundary_bypassed",
            "scan_performed",
            "repository_scan_performed",
            "repair_performed",
            "validation_enforced",
            "hidden_repair_performed",
            "silent_overwrite_performed",
            "cosmetic_substitution_treated_as_basis",
            "digest_laundering_treated_as_basis",
            "id_role_label_difference_treated_as_basis",
            "shared_evidence_treated_as_basis",
            "operation_evidence_alone_treated_as_basis",
            "divergent_receipt_history_route_authorized",
            "carrier_separation_route_authorized",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp))
            for field in fields:
                with self.subTest(field=field):
                    request = self.build_valid_request(files)
                    request[field] = True
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request
                    )
                    self.assert_blocked_public(result)
                    if field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                        self.assertIs(result["non_claims"].get(field), False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = self.build_valid_request(files)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request
                    )
                    self.assert_blocked_public(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = {
                "missing_mapping": lambda request: request.pop("declared_non_claims"),
                "non_mapping": lambda request: request.update({"declared_non_claims": []}),
                "missing_required_key": lambda request: request["declared_non_claims"].pop(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ),
                "non_bool_value": lambda request: request["declared_non_claims"].update(
                    {resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}
                ),
            }
            for name, mutate in malformed_cases.items():
                with self.subTest(name=name):
                    request = self.build_valid_request(files)
                    mutate(request)
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request
                    )
                    self.assert_blocked_public(result)

    def test_material_section_and_sanitizer_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp), sentinels=True)
            default_request = self.build_valid_request(files)
            default_request["raw_body"] = self.SENTINELS[0]
            default_request["hidden_repo_state"] = self.SENTINELS[1]
            default_request["current_working_tree"] = self.SENTINELS[2]
            default_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                default_request
            )
            recorded_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                self.build_supported_request(files)
            )
            blocked_request = self.build_valid_request(files)
            blocked_request["request_raw_markdown_body_return"] = True
            blocked_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                blocked_request
            )
            for result in (default_result, recorded_result, blocked_result):
                self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
                self.assert_material_has_no_raw_bodies(result)
                self.assert_no_raw_bodies(result)
                encoded = json.dumps(result, sort_keys=True)
                self.assertIn(resolver.OPERATION_TYPE, encoded)
                self.assert_canonical_false_non_claims(result)
            self.assertFalse(any(str(value).startswith("result://") for value in self.material(default_result).values()))
            for key in ("candidate_a_digest_value", "candidate_b_digest_value"):
                self.assert_hex_64(self.material(recorded_result)[key])

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            files = self.write_synthetic_basis(base)
            request = self.build_supported_request(files)
            request_path = self.write_json(base / self.safe_json_filename("request"), request)
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path(
                request_path
            )
            self.assert_supported_recorded_result(result)

            missing_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path(
                base / "missing.json"
            )
            self.assert_blocked_public(missing_result)
            malformed_path = base / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_public(malformed_result)
            array_path = self.write_json(base / "array.json", [])
            array_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_from_path(
                array_path
            )
            self.assert_blocked_public(array_result)

            output_dir = base / "operation_result_root"
            first_path = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_result(
                result, output_dir
            )
            second_path = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_result(
                result, first_path
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn("candidate_specific_distinctness_basis_emission_operation_v0_min_result", first_path.name)
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            disallowed_roots = (
                "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation",
            )
            for root in disallowed_roots:
                self.assertNotIn(root, str(first_path))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp), sentinels=True)
            request = self.build_supported_request(files)
            request["raw_body"] = self.SENTINELS[0]
            before_request = copy.deepcopy(request)
            before_file_contents = {key: path.read_text(encoding="utf-8") for key, path in files.items() if path.suffix == ".md"}
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assert_supported_recorded_result(result)
            self.assertEqual(request, before_request)
            after_file_contents = {key: path.read_text(encoding="utf-8") for key, path in files.items() if path.suffix == ".md"}
            self.assertEqual(after_file_contents, before_file_contents)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            files = self.write_synthetic_basis(Path(tmp))
            for request_builder, expected_outcome in (
                (self.build_valid_request, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS),
                (self.build_supported_request, resolver.OUTCOME_RECORDED),
            ):
                with self.subTest(outcome=expected_outcome):
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(
                        request_builder(files)
                    )
                    summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary(
                        result
                    )
                    self.assertEqual(summary["outcome"], expected_outcome)
                    self.assertEqual(summary["failed_check_count"], 0)
                    self.assertEqual(summary["result_version"], "0.1.0")
                    self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
                    self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
                    self.assertEqual(summary["operation_version"], resolver.OPERATION_VERSION)
                    self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
                    self.assertEqual(summary["admissible_future_basis_route"], resolver.ADMISSIBLE_FUTURE_BASIS_ROUTE)
                    self.assertEqual(summary["scope_division_policy"], resolver.SCOPE_DIVISION_POLICY)
                    self.assertEqual(summary["candidate_record_a_id"], resolver.CANDIDATE_A_ID)
                    self.assertEqual(summary["candidate_record_b_id"], resolver.CANDIDATE_B_ID)
                    self.assertEqual(summary["candidate_record_a_role"], resolver.CANDIDATE_A_ROLE)
                    self.assertEqual(summary["candidate_record_b_role"], resolver.CANDIDATE_B_ROLE)
                    for key in (
                        "candidate_standing_authorized",
                        "descendant_body_created",
                        "standing_authorized",
                        "crossing_authorized",
                        "relation_authorized",
                        "field_machinery_authorized",
                        "runtime_authorized",
                        "currentness_authorized",
                        "authority_authorized",
                        "output_authorized",
                        "action_authorized",
                        "derivative_reception_authorized",
                        "synchronization_authorized",
                        "follow_on_authorized",
                        "prior_unsupported_candidate_a_claim_validated",
                        "prior_unsupported_candidate_b_claim_validated",
                        "prior_unsupported_derivation_event_claim_validated",
                        "affected_file_repaired",
                        "affected_file_edited",
                        "affected_file_deleted",
                        "affected_file_overwritten",
                        "affected_file_replaced",
                        "affected_file_redeemed",
                        "affected_file_treated_as_clean_basis",
                        "contaminated_lineage_treated_as_clean_basis",
                        "existence_claim_evidence_check_overridden",
                        "existence_claim_evidence_check_bypassed",
                        "differentiation_operation_overridden",
                        "differentiation_operation_bypassed",
                        "distinctness_operation_boundary_overridden",
                        "distinctness_operation_boundary_bypassed",
                        "distinctness_operation_overridden",
                        "distinctness_operation_bypassed",
                        "candidate_specific_distinctness_basis_emission_boundary_overridden",
                        "candidate_specific_distinctness_basis_emission_boundary_bypassed",
                    ):
                        self.assertIs(summary[key], False, key)
                    for key in (
                        "scan_not_performed",
                        "repository_scan_not_performed",
                        "repair_not_performed",
                        "validation_not_enforced",
                        "hidden_repair_not_performed",
                        "silent_overwrite_not_performed",
                        "operation_spec_markers_present",
                        "upstream_boundary_terminal_summary_markers_present",
                        "completed_distinctness_operation_terminal_summary_markers_present",
                        "completed_differentiation_operation_terminal_summary_markers_present",
                        "completed_distinctness_operation_boundary_terminal_summary_markers_present",
                        "result_level_non_claims_canonical_false",
                    ):
                        self.assertIs(summary[key], True, key)

    def test_smoke_behavior_default_requires_additional_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_valid_request(self.write_synthetic_basis(Path(tmp)))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assert_default_additional_basis_result(result)

    def test_smoke_behavior_supported_scope_division(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.build_supported_request(self.write_synthetic_basis(Path(tmp)))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_operation_v0_min(request)
            self.assert_supported_recorded_result(result)


if __name__ == "__main__":
    unittest.main()
