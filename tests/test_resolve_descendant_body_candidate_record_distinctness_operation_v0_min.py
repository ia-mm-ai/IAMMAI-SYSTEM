"""Tests for the descendant-body candidate-record distinctness operation resolver.

This suite keeps the operation bounded: default current basis is NOT_DISTINCT,
synthetic supported basis requires separate candidate-specific content, seal,
lineage receipt, and digest evidence, and distinctness support never authorizes
standing, descendant bodies, crossing, relation, runtime, authority, repair, or
follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_record_distinctness_operation_v0_min as resolver


class DescendantBodyCandidateRecordDistinctnessOperationTests(unittest.TestCase):
    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def _write_text(self, path: Path, content: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def _write_json(self, path: Path, content: dict[str, Any]) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(content, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def replace_all_key_values(self, value: Any, key: str, replacement: Any) -> None:
        if isinstance(value, dict):
            if key in value:
                value[key] = replacement
            for child in value.values():
                self.replace_all_key_values(child, key, replacement)
        elif isinstance(value, list):
            for child in value:
                self.replace_all_key_values(child, key, replacement)

    def operation_spec_text(self) -> str:
        return "\n".join(
            [
                "# Descendant Body Candidate Record Distinctness Operation V0 Minimum Specification",
                "This file defines one future descendant-body candidate-record distinctness operation.",
                "This file does not implement the operation.",
                "This file does not perform the operation.",
                "distinctness_operation_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
                "distinctness_operation_scope = TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
                "distinctness_evidence_policy = REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
                "cosmetic_difference_policy = ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
                "shared_evidence_policy = SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
                "not_distinct_policy = RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
                "DISTINCTNESS_SUPPORTED",
                "NOT_DISTINCT",
                "Success requires candidate-specific content plus separate seal material, separate lineage receipt material, and separate digest material.",
                "No implementation exists in this spec.",
                "distinctness_operation_implemented = false",
                "distinctness_supported = false",
                "candidate_records_distinct = false",
                "candidate_standing_authorized = false",
            ]
        )

    def boundary_summary_text(self) -> str:
        return "\n".join(
            [
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",
                "failed_check_count = 0",
                "passed_check_count = 135",
                "result_version = 0.2.0",
                "boundary_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY",
                "future_distinctness_operation_type = DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
                "future_distinctness_operation_scope = TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
                "distinctness_evidence_policy = REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
                "cosmetic_difference_policy = ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
                "shared_evidence_policy = SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
                "not_distinct_policy = RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
                "distinctness_not_supported = true",
                "candidate_records_not_distinct = true",
                "enumeration_not_treated_as_distinction = true",
                "id_and_role_difference_alone_not_treated_as_distinctness = true",
                "shared_evidence_reference_alone_not_treated_as_distinctness = true",
            ]
        )

    def boundary_artifact(self) -> dict[str, Any]:
        return {
            "outcome": "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",
            "descendant_body_candidate_record_distinctness_operation_boundary_metadata": {
                "result_version": "0.2.0",
            },
            "descendant_body_candidate_record_distinctness_operation_boundary_summary": {
                "failed_check_count": 0,
                "result_version": "0.2.0",
                "boundary_type": "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY",
                "future_distinctness_operation_type": "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
                "future_distinctness_operation_scope": "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
                "distinctness_evidence_policy": "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
                "cosmetic_difference_policy": "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
                "shared_evidence_policy": "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
                "not_distinct_policy": "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
            },
            "descendant_body_candidate_record_distinctness_operation_boundary": {
                "boundary_type": "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY",
                "future_distinctness_operation_type": "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
                "future_distinctness_operation_scope": "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
                "distinctness_evidence_policy": "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
                "cosmetic_difference_policy": "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
                "shared_evidence_policy": "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
                "not_distinct_policy": "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
                "completed_operation_emitted_two_candidate_records": True,
                "completed_operation_did_not_prove_distinctness_beyond_id_and_role": True,
                "distinctness_operation_not_created": True,
                "distinctness_result_not_recorded": True,
                "distinctness_not_supported": True,
                "candidate_records_not_distinct": True,
                "enumeration_not_treated_as_distinction": True,
                "id_and_role_difference_alone_not_treated_as_distinctness": True,
                "shared_evidence_reference_alone_not_treated_as_distinctness": True,
                "candidate_standing_authorized": False,
                "descendant_body_created": False,
                "crossing_authorized": False,
                "relation_authorized": False,
                "follow_on_authorized": False,
            },
        }

    def source_artifact(self) -> dict[str, Any]:
        return {
            "outcome": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
            "descendant_body_differentiation_operation_summary": {
                "failed_check_count": 0,
            },
            "descendant_body_differentiation_operation": {
                "operation_type": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
                "operation_scope": "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
                "candidate_record_count_emitted": 2,
                "exactly_two_candidate_records_emitted": True,
                "candidate_records_have_operation_evidence": True,
                "candidate_records_non_standing": True,
                "candidate_records_do_not_inherit_from_contaminated_lineage": True,
                "descendant_body_a_created": False,
                "descendant_body_b_created": False,
                "standing_descendant_created": False,
                "first_crossing_authorized": False,
                "relation_created": False,
                "runtime_created": False,
                "currentness_created": False,
                "authority_created": False,
                "follow_on_work_authorized": False,
            },
            "descendant_body_differentiation_candidate_records": [
                {
                    "candidate_record_id": resolver.CANDIDATE_A_ID,
                    "candidate_role": resolver.CANDIDATE_A_ROLE,
                    "candidate_record_created_by_operation": True,
                    "candidate_record_standing": False,
                    "descendant_body_created": False,
                    "inherited_from_contaminated_lineage": False,
                    "prior_unsupported_claim_validated": False,
                },
                {
                    "candidate_record_id": resolver.CANDIDATE_B_ID,
                    "candidate_role": resolver.CANDIDATE_B_ROLE,
                    "candidate_record_created_by_operation": True,
                    "candidate_record_standing": False,
                    "descendant_body_created": False,
                    "inherited_from_contaminated_lineage": False,
                    "prior_unsupported_claim_validated": False,
                },
            ],
        }

    def make_basis(self, root: Path) -> dict[str, Path]:
        paths = {
            "operation_spec": self._write_text(
                root / "basis" / "operation_spec.md", self.operation_spec_text()
            ),
            "boundary_summary": self._write_text(
                root / "basis" / "boundary_summary.md", self.boundary_summary_text()
            ),
            "boundary_artifact": self._write_json(
                root / "basis" / "boundary_artifact.json", self.boundary_artifact()
            ),
            "source_artifact": self._write_json(
                root / "basis" / "source_artifact.json", self.source_artifact()
            ),
        }
        return paths

    def make_materials(
        self,
        root: Path,
        *,
        content_a: str = "candidate A material: local anchor alpha beyond labels",
        content_b: str = "candidate B material: local anchor beta beyond labels",
        seal_a: str = "seal-alpha",
        seal_b: str = "seal-beta",
        lineage_a: str = "lineage receipt alpha",
        lineage_b: str = "lineage receipt beta",
        digest_a: str = "digest-alpha",
        digest_b: str = "digest-beta",
        same_file: bool = False,
    ) -> dict[str, str]:
        material_root = root / "materials"
        if same_file:
            same = self._write_text(material_root / "same.txt", content_a)
            return {
                "candidate_record_a_content_reference": str(same),
                "candidate_record_b_content_reference": str(same),
                "candidate_record_a_seal_reference": str(same),
                "candidate_record_b_seal_reference": str(same),
                "candidate_record_a_lineage_receipt_reference": str(same),
                "candidate_record_b_lineage_receipt_reference": str(same),
                "candidate_record_a_digest_reference": str(same),
                "candidate_record_b_digest_reference": str(same),
            }
        content_a_path = self._write_text(material_root / "content_a.txt", content_a)
        content_b_path = self._write_text(material_root / "content_b.txt", content_b)
        seal_a_path = self._write_text(material_root / "seal_a.txt", seal_a)
        seal_b_path = self._write_text(material_root / "seal_b.txt", seal_b)
        lineage_a_path = self._write_text(material_root / "lineage_a.txt", lineage_a)
        lineage_b_path = self._write_text(material_root / "lineage_b.txt", lineage_b)
        return {
            "candidate_record_a_content_reference": str(content_a_path),
            "candidate_record_b_content_reference": str(content_b_path),
            "candidate_record_a_seal_reference": str(seal_a_path),
            "candidate_record_b_seal_reference": str(seal_b_path),
            "candidate_record_a_lineage_receipt_reference": str(lineage_a_path),
            "candidate_record_b_lineage_receipt_reference": str(lineage_b_path),
            "candidate_record_a_digest_reference": digest_a,
            "candidate_record_b_digest_reference": digest_b,
        }

    def valid_request(self, root: Path, *, with_materials: bool = False, **overrides: Any) -> dict[str, Any]:
        basis = self.make_basis(root)
        request = resolver.build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request(
            operation_spec_reference=str(basis["operation_spec"]),
            distinctness_boundary_terminal_summary_reference=str(basis["boundary_summary"]),
            distinctness_boundary_artifact_reference=str(basis["boundary_artifact"]),
            candidate_record_source_operation_reference=str(basis["source_artifact"]),
            candidate_record_source_operation_artifact_reference=str(basis["source_artifact"]),
        )
        if with_materials:
            request.update(self.make_materials(root))
        request.update(overrides)
        return request

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("code") or block.get("block_code")

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("descendant_body_candidate_record_distinctness_operation_checks", [])
        self.assertIsInstance(checks, list)
        return checks

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

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_downstream_authorization(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def operation(self, result: dict[str, Any]) -> dict[str, Any]:
        operation = result["descendant_body_candidate_record_distinctness_operation"]
        self.assertIsInstance(operation, dict)
        return operation

    def comparison(self, result: dict[str, Any]) -> dict[str, Any]:
        comparison = result["descendant_body_candidate_record_distinctness_comparison"]
        self.assertIsInstance(comparison, dict)
        return comparison

    def assert_operation_not_wrapper(self, operation: dict[str, Any]) -> None:
        forbidden = {
            "outcome",
            "block",
            "descendant_body_candidate_record_distinctness_operation_checks",
            "non_claims",
            "descendant_body_candidate_record_distinctness_operation_summary",
            "descendant_body_candidate_record_distinctness_operation_metadata",
            "descendant_body_candidate_record_distinctness_comparison",
        }
        self.assertTrue(forbidden.isdisjoint(operation))

    def assert_no_downstream_authorization(self, result: dict[str, Any]) -> None:
        operation = self.operation(result)
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
        ):
            self.assertIs(operation.get(key), False, key)

    def assert_no_raw_material_bodies(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        forbidden_strings = [
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        ]
        for forbidden in forbidden_strings:
            self.assertNotIn(forbidden, serialized)
        comparison = self.comparison(result)
        for key in comparison:
            lowered = key.lower()
            self.assertNotIn("body", lowered)
            self.assertNotIn("raw", lowered)
        self.assertIn(resolver.OPERATION_TYPE, serialized)

    def assert_default_not_distinct_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_DISTINCT)
        summary = resolver.build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(result)
        self.assertEqual(summary["distinctness_result"], resolver.DISTINCTNESS_RESULT_NOT_DISTINCT)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(operation["distinctness_operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["distinctness_operation_version"], "0.1.0")
        self.assertEqual(operation["distinctness_operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["distinctness_result"], resolver.DISTINCTNESS_RESULT_NOT_DISTINCT)
        self.assertIs(operation["distinctness_operation_recorded"], True)
        self.assertIs(operation["distinctness_result_recorded"], True)
        self.assertIs(operation["candidate_records_compared"], True)
        self.assertEqual(operation["candidate_record_count_compared"], 2)
        self.assertIs(operation["candidate_ids_distinct"], True)
        self.assertIs(operation["candidate_roles_distinct"], True)
        self.assertIs(operation["id_and_role_difference_only"], True)
        self.assertIs(operation["candidate_specific_content_present"], False)
        self.assertIs(operation["candidate_specific_content_distinct"], False)
        self.assertIs(operation["separate_seal_material_present"], False)
        self.assertIs(operation["separate_seal_material_distinct"], False)
        self.assertIs(operation["separate_lineage_receipt_material_present"], False)
        self.assertIs(operation["separate_lineage_receipt_material_distinct"], False)
        self.assertIs(operation["separate_digest_material_present"], False)
        self.assertIs(operation["separate_digest_material_distinct"], False)
        self.assertIs(operation["shared_evidence_reference_treated_as_distinctness"], False)
        self.assertIs(operation["cosmetic_difference_treated_as_distinctness"], False)
        self.assertIs(operation["enumeration_treated_as_distinction"], False)
        self.assertIs(operation["operation_evidence_alone_treated_as_distinctness"], False)
        self.assertIs(operation["distinctness_supported"], False)
        reason = str(operation["not_distinct_reason"])
        for phrase in (
            "missing candidate-specific content",
            "missing separate seal material",
            "missing separate lineage receipt material",
            "missing separate digest material",
        ):
            self.assertIn(phrase, reason)
        self.assert_no_downstream_authorization(result)
        self.assert_canonical_false_non_claims(result)

    def assert_supported_result(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        summary = resolver.build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(result)
        self.assertEqual(summary["distinctness_result"], resolver.DISTINCTNESS_RESULT_SUPPORTED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertIs(operation["distinctness_supported"], True)
        if "candidate_records_distinct" in operation:
            self.assertIs(operation["candidate_records_distinct"], True)
        for key in (
            "candidate_specific_content_present",
            "candidate_specific_content_compared",
            "candidate_specific_content_distinct",
            "separate_seal_material_present",
            "separate_seal_material_distinct",
            "separate_lineage_receipt_material_present",
            "separate_lineage_receipt_material_distinct",
            "separate_digest_material_present",
            "separate_digest_material_distinct",
        ):
            self.assertIs(operation[key], True, key)
        self.assertIs(operation["id_and_role_difference_only"], False)
        self.assertIs(operation["shared_evidence_reference_treated_as_distinctness"], False)
        self.assertIs(operation["cosmetic_difference_treated_as_distinctness"], False)
        self.assertIs(operation["enumeration_treated_as_distinction"], False)
        self.assertIs(operation["operation_evidence_alone_treated_as_distinctness"], False)
        self.assert_no_downstream_authorization(result)
        self.assert_canonical_false_non_claims(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_record_distinctness_operation_v0_min",
            "resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path",
            "write_descendant_body_candidate_record_distinctness_operation_v0_min_result",
            "build_descendant_body_candidate_record_distinctness_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected_constants = (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_NOT_DISTINCT",
            "OUTCOME_BLOCKED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_FAMILY",
            "DISTINCTNESS_RESULT_SUPPORTED",
            "DISTINCTNESS_RESULT_NOT_DISTINCT",
            "DISTINCTNESS_RESULT_REQUIRES_ADDITIONAL_BASIS",
            "DISTINCTNESS_RESULT_BLOCKED",
            "DISTINCTNESS_RESULT_NOT_RECORDED",
            "DISTINCTNESS_RESULT_FAMILY",
            "OPERATION_TYPE",
            "OPERATION_SCOPE",
            "DISTINCTNESS_EVIDENCE_POLICY",
            "COSMETIC_DIFFERENCE_POLICY",
            "SHARED_EVIDENCE_POLICY",
            "NOT_DISTINCT_POLICY",
            "FAILURE_VISIBILITY_POLICY",
            "CANDIDATE_A_ID",
            "CANDIDATE_B_ID",
            "CANDIDATE_A_ROLE",
            "CANDIDATE_B_ROLE",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        )
        for name in expected_constants:
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_record_distinctness_operation_v0_min")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION")
        self.assertEqual(resolver.OPERATION_SCOPE, "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY")
        self.assertEqual(resolver.DISTINCTNESS_EVIDENCE_POLICY, "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE")
        self.assertEqual(resolver.COSMETIC_DIFFERENCE_POLICY, "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT")
        self.assertEqual(resolver.SHARED_EVIDENCE_POLICY, "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT")
        self.assertEqual(resolver.NOT_DISTINCT_POLICY, "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS")
        self.assertEqual(resolver.FAILURE_VISIBILITY_POLICY, "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL")
        self.assertEqual(resolver.CANDIDATE_A_ID, "descendant_body_basis_candidate_a_001")
        self.assertEqual(resolver.CANDIDATE_B_ID, "descendant_body_basis_candidate_b_001")
        self.assertEqual(resolver.CANDIDATE_A_ROLE, "CANDIDATE_A")
        self.assertEqual(resolver.CANDIDATE_B_ROLE, "CANDIDATE_B")
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_DISTINCT,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        for value in (
            resolver.DISTINCTNESS_RESULT_SUPPORTED,
            resolver.DISTINCTNESS_RESULT_NOT_DISTINCT,
            resolver.DISTINCTNESS_RESULT_REQUIRES_ADDITIONAL_BASIS,
            resolver.DISTINCTNESS_RESULT_BLOCKED,
            resolver.DISTINCTNESS_RESULT_NOT_RECORDED,
        ):
            self.assertIn(value, resolver.DISTINCTNESS_RESULT_FAMILY)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_v0_min"))
        for key in (
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_authorized",
            "field_machinery_authorized",
            "runtime_authorized",
            "api_created",
            "currentness_authorized",
            "authority_authorized",
            "standing_created",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "affected_file_repaired",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "enumeration_treated_as_distinction",
            "id_and_role_difference_treated_as_distinctness",
            "shared_evidence_reference_treated_as_distinctness",
            "operation_evidence_alone_treated_as_distinctness",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "descendant_body_candidate_record_distinctness_operation_recorded",
            "distinctness_operation_recorded",
            "distinctness_result_recorded",
            "candidate_records_compared",
            "candidate_specific_content_present",
            "candidate_specific_content_compared",
            "candidate_specific_content_distinct",
            "separate_seal_material_present",
            "separate_seal_material_distinct",
            "separate_lineage_receipt_material_present",
            "separate_lineage_receipt_material_distinct",
            "separate_digest_material_present",
            "separate_digest_material_distinct",
            "distinctness_supported",
            "not_distinct_recorded",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for code in (
            "DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
            "DISTINCTNESS_OPERATION_VERSION_NOT_0_1_0",
            "SOURCE_OPERATION_ARTIFACT_REFERENCE_MISSING",
            "OPERATION_SPEC_MARKER_MISSING",
            "DISTINCTNESS_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "DISTINCTNESS_BOUNDARY_ARTIFACT_MARKER_MISSING",
            "SOURCE_OPERATION_ARTIFACT_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_MALFORMED",
            "DECLARED_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUEST_UNREADABLE",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_synthetic_basis_records_not_distinct(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(
                self.valid_request(Path(tmp))
            )
        self.assertIsInstance(result, dict)
        self.assert_default_not_distinct_result(result)
        for section in (
            "descendant_body_candidate_record_distinctness_operation_metadata",
            "declared_descendant_body_candidate_record_distinctness_operation_question",
            "upstream_basis",
            "distinctness_operation_basis",
            "descendant_body_candidate_record_distinctness_operation",
            "descendant_body_candidate_record_distinctness_comparison",
            "descendant_body_candidate_record_distinctness_operation_checks",
            "descendant_body_candidate_record_distinctness_operation_statement",
            "descendant_body_candidate_record_distinctness_operation_non_meaning",
            "additional_basis_required",
            "not_recorded_basis",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "descendant_body_candidate_record_distinctness_operation_summary",
        ):
            self.assertIn(section, result)
        operation = self.operation(result)
        self.assertEqual(operation["distinctness_operation_id"], resolver.DEFAULT_OPERATION_ID)
        for marker_key in (
            "source_operation_artifact_markers_present",
            "distinctness_boundary_terminal_summary_markers_present",
            "distinctness_boundary_artifact_markers_present",
            "operation_spec_markers_present",
        ):
            self.assertIs(operation[marker_key], True)
        self.assert_operation_not_wrapper(operation)
        comparison = self.comparison(result)
        self.assertEqual(comparison["candidate_a_id"], operation["candidate_record_a_id"])
        self.assertEqual(comparison["candidate_b_id"], operation["candidate_record_b_id"])
        self.assertEqual(comparison["candidate_a_role"], operation["candidate_record_a_role"])
        self.assertEqual(comparison["candidate_b_role"], operation["candidate_record_b_role"])
        self.assertIs(comparison["id_and_role_difference_only"], True)
        self.assertIs(comparison["distinctness_supported"], False)
        self.assertEqual(comparison["not_distinct_reason"], operation["not_distinct_reason"])
        for key in (
            "candidate_specific_content_hash_a",
            "candidate_specific_content_hash_b",
            "separate_seal_material_hash_a",
            "separate_seal_material_hash_b",
            "separate_lineage_receipt_material_hash_a",
            "separate_lineage_receipt_material_hash_b",
        ):
            self.assertIsNone(comparison[key])
        self.assert_no_raw_material_bodies(result)

    def test_supported_synthetic_basis_records_distinctness_supported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(Path(tmp), with_materials=True)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assert_supported_result(result)
        comparison = self.comparison(result)
        for key in (
            "candidate_specific_content_hash_a",
            "candidate_specific_content_hash_b",
            "separate_seal_material_hash_a",
            "separate_seal_material_hash_b",
            "separate_lineage_receipt_material_hash_a",
            "separate_lineage_receipt_material_hash_b",
        ):
            self.assertIsInstance(comparison[key], str)
            self.assertEqual(len(comparison[key]), 64)
        self.assertEqual(comparison["separate_digest_material_value_a"], "digest-alpha")
        self.assertEqual(comparison["separate_digest_material_value_b"], "digest-beta")
        self.assert_no_raw_material_bodies(result)

    def test_identical_or_cosmetic_only_material_records_not_distinct(self) -> None:
        cases = {
            "cosmetic_content_only": {
                "content_a": f"{resolver.CANDIDATE_A_ID} {resolver.CANDIDATE_A_ROLE}",
                "content_b": f"{resolver.CANDIDATE_B_ID} {resolver.CANDIDATE_B_ROLE}",
            },
            "identical_content": {"content_a": "same candidate content", "content_b": "same candidate content"},
            "identical_seal": {"seal_a": "same-seal", "seal_b": "same-seal"},
            "identical_lineage": {"lineage_a": "same-lineage", "lineage_b": "same-lineage"},
            "identical_digest": {"digest_a": "same-digest", "digest_b": "same-digest"},
            "same_file_all_references": {"same_file": True},
            "operation_evidence_only": {"with_materials": False},
        }
        for name, options in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                request = self.valid_request(root, with_materials=options.pop("with_materials", True))
                if options:
                    request.update(self.make_materials(root, **options))
                result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                self.assertIn(result["outcome"], {resolver.OUTCOME_NOT_DISTINCT, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS})
                operation = self.operation(result)
                self.assertNotEqual(operation["distinctness_result"], resolver.DISTINCTNESS_RESULT_SUPPORTED)
                self.assertIs(operation["distinctness_supported"], False)
                self.assert_no_downstream_authorization(result)
                self.assertIs(operation["enumeration_treated_as_distinction"], False)
                self.assertIs(operation["id_and_role_difference_only"] is True or operation["id_and_role_difference_only"] is False, True)
                self.assertIs(operation["shared_evidence_reference_treated_as_distinctness"], False)
                self.assertIs(operation["operation_evidence_alone_treated_as_distinctness"], False)
                self.assertTrue(operation["not_distinct_reason"])

    def test_records_default_live_target_if_present(self) -> None:
        required = [
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2/descendant_body_candidate_record_distinctness_operation_boundary_001__descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2_result.json",
            REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min/descendant_body_differentiation_operation_001__descendant_body_differentiation_operation_v0_min_result.json",
        ]
        if not all(path.exists() for path in required):
            self.skipTest("default live basis files are not all present")
        request = resolver.build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request()
        result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assert_default_not_distinct_result(result)

    def test_do_not_record_intent_does_not_record_distinctness_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(
                Path(tmp),
                descendant_body_candidate_record_distinctness_operation_intent=(
                    "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
                ),
            )
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(operation["distinctness_result"], resolver.DISTINCTNESS_RESULT_NOT_RECORDED)
        self.assertIs(operation["distinctness_operation_recorded"], False)
        self.assertIs(operation["distinctness_result_recorded"], False)
        self.assertIs(operation["distinctness_supported"], False)
        self.assert_no_downstream_authorization(result)
        self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(
                Path(tmp),
                descendant_body_candidate_record_distinctness_operation_intent=(
                    "BLOCK_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION"
                ),
            )
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assert_blocked_with_public_code(result)
        self.assertEqual(self.operation(result)["distinctness_result"], resolver.DISTINCTNESS_RESULT_BLOCKED)

    def test_request_shape_and_blocking_behavior(self) -> None:
        cases: list[tuple[str, Any]] = [("non_mapping", "not-a-mapping")]
        with tempfile.TemporaryDirectory() as tmp:
            base = self.valid_request(Path(tmp))
            mutation_cases: list[tuple[str, dict[str, Any]]] = [
                ("missing_question", {"descendant_body_candidate_record_distinctness_operation_question": ""}),
                ("unsupported_intent", {"descendant_body_candidate_record_distinctness_operation_intent": "NOPE"}),
                ("missing_operation_type", {"distinctness_operation_type": ""}),
                ("wrong_operation_type", {"distinctness_operation_type": "WRONG"}),
                ("missing_operation_version", {"distinctness_operation_version": ""}),
                ("wrong_operation_version", {"distinctness_operation_version": "9.9.9"}),
                ("missing_operation_scope", {"distinctness_operation_scope": ""}),
                ("wrong_operation_scope", {"distinctness_operation_scope": "WRONG"}),
                ("missing_source_operation_reference", {"candidate_record_source_operation_reference": ""}),
                ("missing_source_operation_artifact_reference", {"candidate_record_source_operation_artifact_reference": ""}),
                ("wrong_candidate_a_id", {"candidate_record_a_id": "wrong"}),
                ("wrong_candidate_b_id", {"candidate_record_b_id": "wrong"}),
                ("wrong_candidate_a_role", {"candidate_record_a_role": "WRONG"}),
                ("wrong_candidate_b_role", {"candidate_record_b_role": "WRONG"}),
                ("wrong_candidate_record_count", {"candidate_record_count_required": 3}),
                ("missing_operation_spec_reference", {"operation_spec_reference": ""}),
                ("missing_boundary_summary_reference", {"distinctness_boundary_terminal_summary_reference": ""}),
                ("missing_boundary_artifact_reference", {"distinctness_boundary_artifact_reference": ""}),
                ("wrong_distinctness_evidence_policy", {"distinctness_evidence_policy": "WRONG"}),
                ("wrong_cosmetic_policy", {"cosmetic_difference_policy": "WRONG"}),
                ("wrong_shared_policy", {"shared_evidence_policy": "WRONG"}),
                ("wrong_not_distinct_policy", {"not_distinct_policy": "WRONG"}),
                ("wrong_failure_visibility_policy", {"failure_visibility_policy": "WRONG"}),
            ]
            boolean_cases = [
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
                "enumeration_treated_as_distinction",
                "id_and_role_difference_treated_as_distinctness",
                "shared_evidence_reference_treated_as_distinctness",
                "operation_evidence_alone_treated_as_distinctness",
            ]
            mutation_cases.extend((key, {key: True}) for key in boolean_cases)
            requested_cases = {
                "request_repository_scan": {"request_repository_scan": True},
                "request_file_discovery": {"request_file_discovery": True, "requested_file_discovery": True},
                "request_affected_file_repair": {"request_affected_file_repair": True, "requested_affected_file_repair": True},
                "request_affected_file_mutation": {"request_affected_file_mutation": True, "requested_affected_file_mutation": True},
                "request_prior_unsupported_claim_validation": {"request_prior_unsupported_claim_validation": True, "requested_prior_unsupported_claim_validation": True},
                "request_existence_claim_evidence_check_override": {"request_existence_claim_evidence_check_override": True, "requested_existence_claim_evidence_check_override": True},
                "request_existence_claim_evidence_check_bypass": {"request_existence_claim_evidence_check_bypass": True, "requested_existence_claim_evidence_check_bypass": True},
                "request_differentiation_operation_override": {"request_differentiation_operation_override": True, "requested_differentiation_operation_override": True},
                "request_differentiation_operation_bypass": {"request_differentiation_operation_bypass": True, "requested_differentiation_operation_bypass": True},
                "request_distinctness_boundary_override": {"request_distinctness_boundary_override": True, "requested_distinctness_boundary_override": True},
                "request_distinctness_boundary_bypass": {"request_distinctness_boundary_bypass": True, "requested_distinctness_boundary_bypass": True},
                "request_candidate_standing_authorization": {"request_candidate_standing_authorization": True, "requested_candidate_standing_authorization": True},
                "request_descendant_body_creation": {"request_descendant_body_creation": True, "requested_descendant_body_creation": True},
                "request_standing_descendant_creation": {"request_standing_descendant_creation": True, "requested_standing_descendant_creation": True},
                "request_descendant_standing_check": {"request_descendant_standing_check": True, "requested_descendant_standing_check": True},
                "request_crossing_authorization": {"request_crossing_authorization": True, "requested_crossing_authorization": True},
                "request_relation_creation": {"request_relation_creation": True, "requested_relation_creation": True},
                "request_field_machinery_creation": {"request_field_machinery_creation": True, "requested_field_machinery_creation": True},
                "request_runtime_creation": {"request_runtime_creation": True, "requested_runtime_creation": True},
                "request_currentness_creation": {"request_currentness_creation": True, "requested_currentness_creation": True},
                "request_authority_creation": {"request_authority_creation": True, "requested_authority_creation": True},
                "request_output_authorization": {"request_output_authorization": True, "requested_output_authorization": True},
                "request_action_authorization": {"request_action_authorization": True, "requested_action_authorization": True},
                "request_derivative_reception_authorization": {"request_derivative_reception_authorization": True, "requested_derivative_reception_authorization": True},
                "request_synchronization_authorization": {"request_synchronization_authorization": True, "requested_synchronization_authorization": True},
                "request_follow_on_authorization": {"request_follow_on_authorization": True, "requested_follow_on_authorization": True},
                "return_raw_markdown_body": {"return_raw_markdown_body": True, "requested_raw_markdown_body_return": True},
            }
            mutation_cases.extend(requested_cases.items())
            for name, mutation in mutation_cases:
                request = copy.deepcopy(base)
                request.update(mutation)
                cases.append((name, request))
            for name, request in cases:
                with self.subTest(name=name):
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)

    def test_marker_validation_blocking_behavior(self) -> None:
        def mutate_boundary_artifact(data: dict[str, Any], key: str, value: Any) -> None:
            self.replace_all_key_values(data, key, value)

        def mutate_source(data: dict[str, Any], key: str, value: Any) -> None:
            self.replace_all_key_values(data, key, value)
            if key == "candidate_record_count_emitted":
                self.replace_all_key_values(data, "exactly_two_candidate_records_emitted", False)
            if key == "exactly_two_candidate_records_emitted":
                self.replace_all_key_values(data, "candidate_record_count_emitted", 1)

        cases: list[tuple[str, str, Any, Any]] = [
            ("operation_spec_marker", "operation_spec_text", "DISTINCTNESS_SUPPORTED", ""),
            ("boundary_summary_marker", "boundary_summary_text", "passed_check_count = 135", ""),
            ("boundary_outcome", "boundary_artifact", "outcome", "WRONG"),
            ("boundary_failed_check", "boundary_artifact", "failed_check_count", 1),
            ("boundary_result_version", "boundary_artifact", "result_version", "9.9.9"),
            ("boundary_type", "boundary_artifact", "boundary_type", "WRONG"),
            ("boundary_future_type", "boundary_artifact", "future_distinctness_operation_type", "WRONG"),
            ("boundary_scope", "boundary_artifact", "future_distinctness_operation_scope", "WRONG"),
            ("boundary_evidence_policy", "boundary_artifact", "distinctness_evidence_policy", "WRONG"),
            ("boundary_cosmetic_policy", "boundary_artifact", "cosmetic_difference_policy", "WRONG"),
            ("boundary_shared_policy", "boundary_artifact", "shared_evidence_policy", "WRONG"),
            ("boundary_not_distinct_policy", "boundary_artifact", "not_distinct_policy", "WRONG"),
            ("boundary_emitted_two", "boundary_artifact", "completed_operation_emitted_two_candidate_records", False),
            ("boundary_did_not_prove", "boundary_artifact", "completed_operation_did_not_prove_distinctness_beyond_id_and_role", False),
            ("boundary_distinctness_not_supported", "boundary_artifact", "distinctness_not_supported", False),
            ("boundary_candidates_not_distinct", "boundary_artifact", "candidate_records_not_distinct", False),
            ("boundary_enumeration", "boundary_artifact", "enumeration_not_treated_as_distinction", False),
            ("boundary_id_role", "boundary_artifact", "id_and_role_difference_alone_not_treated_as_distinctness", False),
            ("boundary_shared", "boundary_artifact", "shared_evidence_reference_alone_not_treated_as_distinctness", False),
            ("source_outcome", "source_artifact", "outcome", "WRONG"),
            ("source_failed_check", "source_artifact", "failed_check_count", 1),
            ("source_operation_type", "source_artifact", "operation_type", "WRONG"),
            ("source_operation_scope", "source_artifact", "operation_scope", "WRONG"),
            ("source_candidate_count", "source_artifact", "candidate_record_count_emitted", 1),
            ("source_exactly_two", "source_artifact", "exactly_two_candidate_records_emitted", False),
            ("source_operation_evidence", "source_artifact", "candidate_records_have_operation_evidence", False),
            ("source_non_standing", "source_artifact", "candidate_records_non_standing", False),
            ("source_not_contaminated", "source_artifact", "candidate_records_do_not_inherit_from_contaminated_lineage", False),
            ("source_body_a", "source_artifact", "descendant_body_a_created", True),
            ("source_body_b", "source_artifact", "descendant_body_b_created", True),
            ("source_standing", "source_artifact", "standing_descendant_created", True),
            ("source_crossing", "source_artifact", "first_crossing_authorized", True),
            ("source_relation", "source_artifact", "relation_created", True),
        ]
        candidate_cases = [
            ("remove_candidate_a", 0, None),
            ("remove_candidate_b", 1, None),
            ("candidate_a_role", 0, ("candidate_role", "WRONG")),
            ("candidate_b_role", 1, ("candidate_role", "WRONG")),
            ("candidate_created", 0, ("candidate_record_created_by_operation", False)),
            ("candidate_standing", 0, ("candidate_record_standing", True)),
            ("candidate_descendant_body", 0, ("descendant_body_created", True)),
            ("candidate_contaminated", 0, ("inherited_from_contaminated_lineage", True)),
            ("candidate_prior_validated", 0, ("prior_unsupported_claim_validated", True)),
        ]
        for name, target, key, value in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                basis = self.make_basis(root)
                if target == "operation_spec_text":
                    text = basis["operation_spec"].read_text(encoding="utf-8").replace(key, value)
                    basis["operation_spec"].write_text(text, encoding="utf-8")
                elif target == "boundary_summary_text":
                    text = basis["boundary_summary"].read_text(encoding="utf-8").replace(key, value)
                    basis["boundary_summary"].write_text(text, encoding="utf-8")
                elif target == "boundary_artifact":
                    data = self.boundary_artifact()
                    mutate_boundary_artifact(data, key, value)
                    self._write_json(basis["boundary_artifact"], data)
                elif target == "source_artifact":
                    data = self.source_artifact()
                    mutate_source(data, key, value)
                    self._write_json(basis["source_artifact"], data)
                request = resolver.build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request(
                    operation_spec_reference=str(basis["operation_spec"]),
                    distinctness_boundary_terminal_summary_reference=str(basis["boundary_summary"]),
                    distinctness_boundary_artifact_reference=str(basis["boundary_artifact"]),
                    candidate_record_source_operation_reference=str(basis["source_artifact"]),
                    candidate_record_source_operation_artifact_reference=str(basis["source_artifact"]),
                )
                result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                self.assert_blocked_with_public_code(result)
                self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        for name, index, mutation in candidate_cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                basis = self.make_basis(root)
                data = self.source_artifact()
                records = data["descendant_body_differentiation_candidate_records"]
                if mutation is None:
                    records.pop(index)
                else:
                    records[index][mutation[0]] = mutation[1]
                self._write_json(basis["source_artifact"], data)
                request = resolver.build_declared_descendant_body_candidate_record_distinctness_operation_v0_min_request(
                    operation_spec_reference=str(basis["operation_spec"]),
                    distinctness_boundary_terminal_summary_reference=str(basis["boundary_summary"]),
                    distinctness_boundary_artifact_reference=str(basis["boundary_artifact"]),
                    candidate_record_source_operation_reference=str(basis["source_artifact"]),
                    candidate_record_source_operation_artifact_reference=str(basis["source_artifact"]),
                )
                result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                self.assert_blocked_with_public_code(result)

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED",
            "descendant_body_created": "DESCENDANT_BODY_CREATED",
            "standing_authorized": "STANDING_AUTHORIZED",
            "crossing_authorized": "CROSSING_AUTHORIZED",
            "relation_authorized": "RELATION_AUTHORIZED",
            "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED",
            "runtime_authorized": "RUNTIME_AUTHORIZED",
            "api_created": "API_CREATED",
            "currentness_authorized": "CURRENTNESS_AUTHORIZED",
            "authority_authorized": "AUTHORITY_AUTHORIZED",
            "standing_created": "STANDING_CREATED",
            "output_authorized": "OUTPUT_AUTHORIZED",
            "action_authorized": "ACTION_AUTHORIZED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
            "follow_on_authorized": "FOLLOW_ON_AUTHORIZED",
            "prior_unsupported_candidate_a_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
            "prior_unsupported_candidate_b_claim_validated": "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
            "prior_unsupported_derivation_event_claim_validated": "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
            "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
            "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
            "affected_file_edited": "AFFECTED_FILE_EDITED",
            "affected_file_deleted": "AFFECTED_FILE_DELETED",
            "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
            "affected_file_replaced": "AFFECTED_FILE_REPLACED",
            "affected_file_redeemed": "AFFECTED_FILE_REDEEMED",
            "affected_file_treated_as_clean_basis": "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
            "contaminated_lineage_treated_as_clean_basis": "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
            "existence_claim_evidence_check_overridden": "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
            "existence_claim_evidence_check_bypassed": "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
            "differentiation_operation_overridden": "DIFFERENTIATION_OPERATION_OVERRIDDEN",
            "differentiation_operation_bypassed": "DIFFERENTIATION_OPERATION_BYPASSED",
            "distinctness_boundary_overridden": "DISTINCTNESS_BOUNDARY_OVERRIDDEN",
            "distinctness_boundary_bypassed": "DISTINCTNESS_BOUNDARY_BYPASSED",
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "repair_performed": "REPAIR_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
            "enumeration_treated_as_distinction": "ENUMERATION_TREATED_AS_DISTINCTION",
            "id_and_role_difference_treated_as_distinctness": "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
            "shared_evidence_reference_treated_as_distinctness": "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
            "operation_evidence_alone_treated_as_distinctness": "OPERATION_EVIDENCE_ALONE_TREATED_AS_DISTINCTNESS",
        }
        for key, expected_code in cases.items():
            with self.subTest(key=key), tempfile.TemporaryDirectory() as tmp:
                request = self.valid_request(Path(tmp))
                request[key] = True
                result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                self.assert_blocked_with_public_code(result)
                emitted = {
                    check.get("block_code") or check.get("failure_code")
                    for check in self.checks(result)
                    if check.get("passed") is not True
                }
                self.assertIn(expected_code, emitted)
                self.assertIs(result["non_claims"].get(key), False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = self.valid_request(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_canonical_false_non_claims(result)
            malformed_cases = {
                "missing": None,
                "non_mapping": "not-a-map",
                "missing_key": "missing_key",
                "non_bool": "non_bool",
            }
            for name in malformed_cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base)
                    if name == "missing":
                        request.pop("declared_non_claims")
                    elif name == "non_mapping":
                        request["declared_non_claims"] = []
                    elif name == "missing_key":
                        request["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
                    elif name == "non_bool":
                        request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = "false"
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)

    def test_comparison_section_and_sanitizer_behavior(self) -> None:
        sentinel_text = "RAW_MARKDOWN_BODY_MUST_NOT_RETURN HIDDEN_REPO_STATE_MUST_NOT_RETURN CURRENT_WORKING_TREE_MUST_NOT_RETURN"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request = self.valid_request(root, with_materials=True)
            request.update(
                self.make_materials(
                    root,
                    content_a=f"A private content {sentinel_text}",
                    content_b="B private content distinct",
                    seal_a=f"A seal {sentinel_text}",
                    seal_b="B seal distinct",
                    lineage_a=f"A lineage {sentinel_text}",
                    lineage_b="B lineage distinct",
                )
            )
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assert_supported_result(result)
        comparison = self.comparison(result)
        self.assertEqual(comparison["not_distinct_reason"], self.operation(result)["not_distinct_reason"])
        self.assert_no_raw_material_bodies(result)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request = self.valid_request(root)
            request_path = root / "request.json"
            self._write_json(request_path, request)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path(request_path)
            self.assert_default_not_distinct_result(result)

            missing = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path(root / "missing.json")
            self.assert_blocked_with_public_code(missing)
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path(malformed_path)
            self.assert_blocked_with_public_code(malformed)
            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array_result)

            output_root = root / "writes" / "descendant_body_candidate_record_distinctness_operation_v0_min"
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_descendant_body_candidate_record_distinctness_operation_v0_min_result(result)
                second = resolver.write_descendant_body_candidate_record_distinctness_operation_v0_min_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            with first.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_NOT_DISTINCT)
            self.assertIn("descendant_body_candidate_record_distinctness_operation_v0_min_result", first.name)
            prohibited_parts = {
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary_v0_min",
                "source-transfer",
                "source-receipt",
                "public-api",
                "participant-facing-interface",
                "distributed-network",
                "runtime-hosting",
                "runtime-loop",
                "daemon",
            }
            self.assertTrue(prohibited_parts.isdisjoint(set(first.parts)))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request = self.valid_request(root, with_materials=True)
            original_request = copy.deepcopy(request)
            basis_paths = [
                Path(request["operation_spec_reference"]),
                Path(request["distinctness_boundary_terminal_summary_reference"]),
                Path(request["distinctness_boundary_artifact_reference"]),
                Path(request["candidate_record_source_operation_artifact_reference"]),
                Path(request["candidate_record_a_content_reference"]),
                Path(request["candidate_record_b_content_reference"]),
                Path(request["candidate_record_a_seal_reference"]),
                Path(request["candidate_record_b_seal_reference"]),
                Path(request["candidate_record_a_lineage_receipt_reference"]),
                Path(request["candidate_record_b_lineage_receipt_reference"]),
            ]
            before_contents = {path: path.read_text(encoding="utf-8") for path in basis_paths}
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
            self.assert_supported_result(result)
            self.assertEqual(request, original_request)
            for path, before in before_contents.items():
                self.assertEqual(path.read_text(encoding="utf-8"), before)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            not_distinct = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(
                self.valid_request(Path(tmp) / "not_distinct")
            )
            supported = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(
                self.valid_request(Path(tmp) / "supported", with_materials=True)
            )
        for result, supported_expected in ((not_distinct, False), (supported, True)):
            with self.subTest(outcome=result["outcome"]):
                summary = resolver.build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(result)
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(summary["failed_check_count"], 0)
                self.assertEqual(summary["result_version"], "0.1.0")
                self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
                self.assertEqual(summary["operation_id"], resolver.DEFAULT_OPERATION_ID)
                self.assertEqual(summary["distinctness_operation_type"], resolver.OPERATION_TYPE)
                self.assertEqual(summary["distinctness_operation_version"], "0.1.0")
                self.assertEqual(summary["distinctness_operation_scope"], resolver.OPERATION_SCOPE)
                self.assertEqual(summary["distinctness_evidence_policy"], resolver.DISTINCTNESS_EVIDENCE_POLICY)
                self.assertEqual(summary["cosmetic_difference_policy"], resolver.COSMETIC_DIFFERENCE_POLICY)
                self.assertEqual(summary["shared_evidence_policy"], resolver.SHARED_EVIDENCE_POLICY)
                self.assertEqual(summary["not_distinct_policy"], resolver.NOT_DISTINCT_POLICY)
                self.assertEqual(summary["failure_visibility_policy"], resolver.FAILURE_VISIBILITY_POLICY)
                self.assertEqual(summary["candidate_record_count_compared"], 2)
                self.assertIs(summary["candidate_ids_distinct"], True)
                self.assertIs(summary["candidate_roles_distinct"], True)
                self.assertIs(summary["id_and_role_difference_only"], not supported_expected)
                self.assertIs(summary["candidate_specific_content_present"], supported_expected)
                self.assertIs(summary["candidate_specific_content_distinct"], supported_expected)
                self.assertIs(summary["separate_seal_material_present"], supported_expected)
                self.assertIs(summary["separate_seal_material_distinct"], supported_expected)
                self.assertIs(summary["separate_lineage_receipt_material_present"], supported_expected)
                self.assertIs(summary["separate_lineage_receipt_material_distinct"], supported_expected)
                self.assertIs(summary["separate_digest_material_present"], supported_expected)
                self.assertIs(summary["separate_digest_material_distinct"], supported_expected)
                self.assertIs(summary["shared_evidence_reference_treated_as_distinctness"], False)
                self.assertIs(summary["cosmetic_difference_treated_as_distinctness"], False)
                self.assertIs(summary["enumeration_treated_as_distinction"], False)
                self.assertIs(summary["operation_evidence_alone_treated_as_distinctness"], False)
                self.assertIs(summary["distinctness_supported"], supported_expected)
                self.assertIs(summary["candidate_standing_authorized"], False)
                self.assertIs(summary["descendant_body_created"], False)
                self.assertIs(summary["standing_authorized"], False)
                self.assertIs(summary["crossing_authorized"], False)
                self.assertIs(summary["relation_authorized"], False)
                self.assertIs(summary["runtime_authorized"], False)
                self.assertIs(summary["currentness_authorized"], False)
                self.assertIs(summary["authority_authorized"], False)
                self.assertIs(summary["output_authorized"], False)
                self.assertIs(summary["action_authorized"], False)
                self.assertIs(summary["derivative_reception_authorized"], False)
                self.assertIs(summary["synchronization_authorized"], False)
                self.assertIs(summary["follow_on_authorized"], False)
                self.assertIs(summary["affected_file_repaired"], False)
                self.assertIs(summary["affected_file_treated_as_clean_basis"], False)
                self.assertIs(summary["contaminated_lineage_treated_as_clean_basis"], False)
                self.assertIs(summary["existence_claim_evidence_check_overridden"], False)
                self.assertIs(summary["existence_claim_evidence_check_bypassed"], False)
                self.assertIs(summary["differentiation_operation_overridden"], False)
                self.assertIs(summary["differentiation_operation_bypassed"], False)
                self.assertIs(summary["distinctness_boundary_overridden"], False)
                self.assertIs(summary["distinctness_boundary_bypassed"], False)
                self.assertIs(summary["scan_performed"], False)
                self.assertIs(summary["repository_scan_performed"], False)
                self.assertIs(summary["repair_performed"], False)
                self.assertIs(summary["validation_enforced"], False)
                self.assertIs(summary["hidden_repair_performed"], False)
                self.assertIs(summary["silent_overwrite_performed"], False)
                self.assertIs(summary["operation_spec_markers_present"], True)
                self.assertIs(summary["source_operation_artifact_markers_present"], True)
                self.assertIs(summary["distinctness_boundary_terminal_summary_markers_present"], True)
                self.assertIs(summary["distinctness_boundary_artifact_markers_present"], True)
                self.assertIs(summary["result_level_non_claims_canonical_false"], True)

    def test_smoke_behavior_default_not_distinct(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(Path(tmp))
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
            summary = resolver.build_descendant_body_candidate_record_distinctness_operation_v0_min_summary(result)
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_DISTINCT)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_default_not_distinct_result(result)
        self.assert_operation_not_wrapper(self.operation(result))

    def test_smoke_behavior_supported_synthetic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(Path(tmp), with_materials=True)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_v0_min(request)
        self.assert_supported_result(result)


if __name__ == "__main__":
    unittest.main()
