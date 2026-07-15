"""Tests for one descendant-body candidate-record distinctness boundary.

This suite verifies one boundary result only. It checks that the resolver
records the future distinctness-operation boundary without performing the
future operation, creating distinctness evidence, marking candidate records
distinct, authorizing standing, creating descendant bodies, scanning,
repairing, validating contaminated claims, or authorizing follow-on work.
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
sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min as resolver


BOUNDARY_SPEC_MARKERS = (
    "Descendant Body Candidate Record Distinctness Operation Boundary V0 Minimum Specification",
    "This file defines one boundary for a future descendant-body candidate-record distinctness operation.",
    "This file does not perform distinctness checking.",
    "The completed operation result emitted candidate records but did not prove candidate-record distinctness beyond id and role.",
    "Enumeration is not distinction.",
    "Id and role difference alone are not distinctness.",
    "Shared evidence reference alone is not distinctness.",
    "boundary_created = true",
    "distinctness_operation_created = false",
    "distinctness_supported = false",
    "candidate_records_distinct = false",
    "separate_seal_material_created = false",
    "separate_lineage_receipt_material_created = false",
    "separate_digest_material_created = false",
)

COMPLETED_OPERATION_SUMMARY_MARKERS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 161",
    "operation_id = descendant_body_differentiation_operation_001",
    "candidate_record_count_emitted = 2",
    "candidate_record_ids = descendant_body_basis_candidate_a_001, descendant_body_basis_candidate_b_001",
    "Candidate records are result-contained, non-standing, operation-evidenced records only",
    "Candidate records are not descendant bodies",
    "Candidate records are not standing descendants",
    "Candidate records are not crossing authorization",
    "The completed existence-claim evidence check line remains standing as the mechanical classification that the three prior descendant existence claims are UNSUPPORTED",
)

CONTAMINATED_LINEAGE_MARKERS = (
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "descendant_body_basis_derivation_event_recorded = true",
)

EVIDENCE_CHECK_SUMMARY_MARKERS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
    "descendant_body_basis_candidate_a_created = UNSUPPORTED",
    "descendant_body_basis_candidate_b_created = UNSUPPORTED",
    "descendant_body_basis_derivation_event_recorded = UNSUPPORTED",
    "Contaminated lineage is not clean basis",
)

WRAPPER_FIELDS = {
    "outcome",
    "block",
    "descendant_body_candidate_record_distinctness_operation_boundary_checks",
    "non_claims",
    "descendant_body_candidate_record_distinctness_operation_boundary_summary",
    "descendant_body_candidate_record_distinctness_operation_boundary_metadata",
}

AUTHORIZATION_FALSE_FIELDS = (
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
)

NEGATIVE_TRUE_FIELDS = (
    "distinctness_operation_not_created",
    "distinctness_operation_not_performed",
    "distinctness_operation_not_recorded",
    "distinctness_result_not_recorded",
    "distinctness_not_supported",
    "candidate_records_not_distinct",
    "candidate_specific_content_not_created",
    "separate_seal_material_not_created",
    "separate_lineage_receipt_material_not_created",
    "separate_digest_material_not_created",
    "candidate_standing_not_authorized",
    "candidate_standing_not_created",
    "descendant_bodies_not_created",
    "standing_descendant_not_created",
    "descendant_standing_check_not_performed",
    "first_crossing_not_authorized",
    "relation_not_created",
    "field_machinery_not_created",
    "runtime_not_created",
    "api_not_created",
    "currentness_not_created",
    "authority_not_created",
    "standing_not_created",
    "output_not_authorized",
    "action_not_authorized",
    "derivative_reception_not_authorized",
    "synchronization_not_authorized",
    "follow_on_not_authorized",
    "prior_unsupported_claims_not_validated",
    "affected_file_not_repaired",
    "affected_file_not_treated_as_clean_basis",
    "contaminated_lineage_not_treated_as_clean_basis",
    "existence_claim_evidence_check_not_overridden",
    "existence_claim_evidence_check_not_bypassed",
    "differentiation_operation_not_overridden",
    "differentiation_operation_not_bypassed",
    "scan_not_performed",
    "repository_scan_not_performed",
    "repair_not_performed",
    "validation_not_enforced",
    "hidden_repair_not_performed",
    "silent_overwrite_not_performed",
    "enumeration_not_treated_as_distinction",
    "id_and_role_difference_alone_not_treated_as_distinctness",
    "shared_evidence_reference_alone_not_treated_as_distinctness",
)

SENTINELS = (
    "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
)


class DescendantBodyCandidateRecordDistinctnessOperationBoundaryTests(
    unittest.TestCase
):
    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name)
        safe = safe.replace("/", "_").replace("\\", "_")
        safe = safe.replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def _write_text(self, path: Path, markers: tuple[str, ...], *, extra: str = "") -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        text = "\n".join(markers)
        if extra:
            text = f"{text}\n{extra}"
        path.write_text(f"{text}\n", encoding="utf-8")
        return path

    def _write_json(self, path: Path, payload: Any) -> Path:
        self.assertFalse(path.is_dir(), f"fixture path collision at {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def synthetic_completed_operation_artifact(self) -> dict[str, Any]:
        return {
            "outcome": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
            "descendant_body_differentiation_operation_summary": {
                "failed_check_count": 0
            },
            "descendant_body_differentiation_operation": {
                "operation_type": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
                "operation_scope": "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
                "candidate_record_policy": (
                    "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
                ),
                "operation_result_created": True,
                "operation_recorded": True,
                "differentiation_performed": True,
                "candidate_records_created": True,
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
            },
            "descendant_body_differentiation_candidate_records": [
                {
                    "candidate_record_id": "descendant_body_basis_candidate_a_001",
                    "candidate_role": "CANDIDATE_A",
                    "candidate_record_created_by_operation": True,
                    "candidate_record_standing": False,
                    "descendant_body_created": False,
                    "inherited_from_contaminated_lineage": False,
                    "prior_unsupported_claim_validated": False,
                },
                {
                    "candidate_record_id": "descendant_body_basis_candidate_b_001",
                    "candidate_role": "CANDIDATE_B",
                    "candidate_record_created_by_operation": True,
                    "candidate_record_standing": False,
                    "descendant_body_created": False,
                    "inherited_from_contaminated_lineage": False,
                    "prior_unsupported_claim_validated": False,
                },
            ],
        }

    def write_synthetic_basis(
        self,
        base: Path,
        *,
        remove_boundary_marker: str | None = None,
        remove_completed_summary_marker: str | None = None,
        remove_contaminated_marker: str | None = None,
        remove_evidence_marker: str | None = None,
        artifact_mutator: Any | None = None,
        extra_text: str = "",
    ) -> dict[str, Path]:
        boundary_markers = tuple(
            marker for marker in BOUNDARY_SPEC_MARKERS if marker != remove_boundary_marker
        )
        completed_summary_markers = tuple(
            marker
            for marker in COMPLETED_OPERATION_SUMMARY_MARKERS
            if marker != remove_completed_summary_marker
        )
        contaminated_markers = tuple(
            marker
            for marker in CONTAMINATED_LINEAGE_MARKERS
            if marker != remove_contaminated_marker
        )
        evidence_markers = tuple(
            marker
            for marker in EVIDENCE_CHECK_SUMMARY_MARKERS
            if marker != remove_evidence_marker
        )
        artifact = self.synthetic_completed_operation_artifact()
        if artifact_mutator is not None:
            artifact_mutator(artifact)
        paths = {
            "boundary_spec": self._write_text(
                base / "basis" / "distinctness_boundary_spec.md",
                boundary_markers,
                extra=extra_text,
            ),
            "completed_summary": self._write_text(
                base / "basis" / "completed_operation_terminal_summary.md",
                completed_summary_markers,
                extra=extra_text,
            ),
            "contaminated": self._write_text(
                base / "basis" / "contaminated_lineage.md",
                contaminated_markers,
                extra=extra_text,
            ),
            "evidence": self._write_text(
                base / "basis" / "existence_check_terminal_summary.md",
                evidence_markers,
                extra=extra_text,
            ),
            "artifact": self._write_json(
                base / "basis" / "completed_operation_artifact.json", artifact
            ),
        }
        return paths

    def valid_request(self, paths: dict[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_request(
            boundary_spec_reference=str(paths["boundary_spec"]),
            completed_operation_terminal_summary_reference=str(paths["completed_summary"]),
            completed_operation_artifact_reference=str(paths["artifact"]),
            contaminated_lineage_reference=str(paths["contaminated"]),
            existence_claim_evidence_check_terminal_summary_reference=str(paths["evidence"]),
        )

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        return result["descendant_body_candidate_record_distinctness_operation_boundary"]

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block") or {}
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get(
            "descendant_body_candidate_record_distinctness_operation_boundary_checks", []
        )
        return sum(1 for check in checks if check.get("passed") is not True)

    def passed_check_count(self, result: dict[str, Any]) -> int:
        checks = result.get(
            "descendant_body_candidate_record_distinctness_operation_boundary_checks", []
        )
        return sum(1 for check in checks if check.get("passed") is True)

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
        self.assert_no_positive_overreach(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get(
            "descendant_body_candidate_record_distinctness_operation_boundary_checks", []
        )
        for check in checks:
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIsInstance(non_claims[key], bool)

    def assert_boundary_not_wrapper(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_no_raw_markdown_body(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in SENTINELS:
            self.assertNotIn(sentinel, serialized)
        self.assertNotIn("RAW_MARKDOWN_BODY_MUST_NOT_RETURN", serialized)
        self.assertNotIn("HIDDEN_REPOSITORY_STATE_MUST_NOT_RETURN", serialized)
        self.assertNotIn("CONTAMINATED_LINEAGE_BODY_MUST_NOT_RETURN", serialized)

    def assert_no_positive_overreach(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        non_claims = result["non_claims"]
        for key in (
            "distinctness_operation_created",
            "distinctness_operation_performed",
            "distinctness_operation_recorded",
            "distinctness_result_recorded",
            "distinctness_supported",
            "candidate_records_distinct",
            "candidate_specific_content_created",
            "separate_seal_material_created",
            "separate_lineage_receipt_material_created",
            "separate_digest_material_created",
            "candidate_standing_authorized",
            "descendant_body_a_created",
            "descendant_body_b_created",
            "standing_descendant_created",
            "first_crossing_authorized",
            "relation_created",
            "runtime_created",
            "currentness_created",
            "authority_created",
            "follow_on_work_authorized",
        ):
            if key in non_claims:
                self.assertIs(non_claims[key], False)
        for key in AUTHORIZATION_FALSE_FIELDS:
            self.assertIs(boundary.get(key), False)

    def assert_recorded_boundary_posture(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(
            boundary["future_distinctness_operation_type"],
            resolver.FUTURE_DISTINCTNESS_OPERATION_TYPE,
        )
        self.assertEqual(
            boundary["future_distinctness_operation_scope"],
            resolver.FUTURE_DISTINCTNESS_OPERATION_SCOPE,
        )
        self.assertEqual(
            boundary["distinctness_evidence_policy"],
            resolver.DISTINCTNESS_EVIDENCE_POLICY,
        )
        self.assertEqual(
            boundary["cosmetic_difference_policy"],
            resolver.COSMETIC_DIFFERENCE_POLICY,
        )
        self.assertEqual(
            boundary["shared_evidence_policy"], resolver.SHARED_EVIDENCE_POLICY
        )
        self.assertEqual(boundary["not_distinct_policy"], resolver.NOT_DISTINCT_POLICY)
        self.assertEqual(
            boundary["failure_visibility_policy"], resolver.FAILURE_VISIBILITY_POLICY
        )
        self.assertIs(
            boundary[
                "descendant_body_candidate_record_distinctness_operation_boundary_recorded"
            ],
            True,
        )
        self.assertIs(boundary["boundary_created"], True)
        for key in (
            "completed_operation_terminal_summary_reference_declared",
            "completed_operation_artifact_reference_declared",
            "contaminated_lineage_reference_declared",
            "existence_claim_evidence_check_terminal_summary_reference_declared",
            "candidate_record_a_reference_declared",
            "candidate_record_b_reference_declared",
            "candidate_record_a_id_accepted",
            "candidate_record_b_id_accepted",
            "candidate_record_a_role_accepted",
            "candidate_record_b_role_accepted",
            "future_distinctness_operation_type_accepted",
            "future_distinctness_operation_scope_accepted",
            "distinctness_evidence_policy_accepted",
            "cosmetic_difference_policy_accepted",
            "shared_evidence_policy_accepted",
            "not_distinct_policy_accepted",
            "failure_visibility_policy_accepted",
            "future_operation_shape_declared",
            "boundary_spec_markers_present",
            "completed_operation_terminal_summary_markers_present",
            "completed_operation_artifact_markers_present",
            "contaminated_lineage_markers_present",
            "existence_claim_evidence_check_terminal_summary_markers_present",
            "completed_operation_emitted_two_candidate_records",
            "completed_operation_did_not_prove_distinctness_beyond_id_and_role",
        ):
            self.assertIs(boundary[key], True, key)
        for key in NEGATIVE_TRUE_FIELDS:
            self.assertIs(boundary[key], True, key)
        for key in AUTHORIZATION_FALSE_FIELDS:
            self.assertIs(boundary[key], False, key)
        self.assert_boundary_not_wrapper(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_raw_markdown_body(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min",
            "resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path",
            "write_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result",
            "build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary",
            "build_declared_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_request",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        for name in (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "BOUNDARY_TYPE",
            "FUTURE_DISTINCTNESS_OPERATION_TYPE",
            "FUTURE_DISTINCTNESS_OPERATION_SCOPE",
            "DISTINCTNESS_EVIDENCE_POLICY",
            "COSMETIC_DIFFERENCE_POLICY",
            "SHARED_EVIDENCE_POLICY",
            "NOT_DISTINCT_POLICY",
            "FAILURE_VISIBILITY_POLICY",
            "FUTURE_DISTINCTNESS_OPERATION_OUTCOME_FAMILY",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY",
        )
        self.assertEqual(
            resolver.FUTURE_DISTINCTNESS_OPERATION_TYPE,
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION",
        )
        self.assertEqual(
            resolver.FUTURE_DISTINCTNESS_OPERATION_SCOPE,
            "TWO_NON_STANDING_CANDIDATE_RECORDS_DECLARED_ONLY",
        )
        self.assertEqual(
            resolver.DISTINCTNESS_EVIDENCE_POLICY,
            "REQUIRE_SEPARATE_CANDIDATE_SPECIFIC_DISTINCTNESS_EVIDENCE",
        )
        self.assertEqual(
            resolver.COSMETIC_DIFFERENCE_POLICY,
            "ID_AND_ROLE_DIFFERENCE_ALONE_NOT_SUFFICIENT",
        )
        self.assertEqual(
            resolver.SHARED_EVIDENCE_POLICY,
            "SHARED_EVIDENCE_REFERENCE_ALONE_NOT_SUFFICIENT",
        )
        self.assertEqual(
            resolver.NOT_DISTINCT_POLICY,
            "RECORD_NOT_DISTINCT_OR_BLOCK_WHEN_DISTINCTNESS_EVIDENCE_FAILS",
        )
        self.assertEqual(
            resolver.FAILURE_VISIBILITY_POLICY,
            "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL",
        )
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_NOT_RECORDED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        for outcome in (
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_RECORDED",
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BLOCKED",
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_RECORDED",
        ):
            self.assertIn(outcome, resolver.FUTURE_DISTINCTNESS_OPERATION_OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min"
            )
        )
        required_false_keys = (
            "distinctness_operation_created",
            "distinctness_operation_performed",
            "distinctness_operation_recorded",
            "distinctness_result_recorded",
            "distinctness_supported",
            "candidate_records_distinct",
            "candidate_specific_content_created",
            "separate_seal_material_created",
            "separate_lineage_receipt_material_created",
            "separate_digest_material_created",
            "candidate_standing_authorized",
            "candidate_standing_created",
            "descendant_body_a_created",
            "descendant_body_b_created",
            "standing_descendant_created",
            "descendant_standing_check_performed",
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
            "follow_on_work_authorized",
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
            "scan_performed",
            "repository_scan_performed",
            "repair_performed",
            "validation_enforced",
            "hidden_repair_performed",
            "silent_overwrite_performed",
            "enumeration_treated_as_distinction",
            "id_and_role_difference_treated_as_distinctness",
            "shared_evidence_reference_treated_as_distinctness",
        )
        for key in required_false_keys:
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "descendant_body_candidate_record_distinctness_operation_boundary_recorded",
            "boundary_created",
            "completed_operation_terminal_summary_reference_declared",
            "completed_operation_artifact_reference_declared",
            "contaminated_lineage_reference_declared",
            "existence_claim_evidence_check_terminal_summary_reference_declared",
            "candidate_record_a_reference_declared",
            "candidate_record_b_reference_declared",
            "candidate_record_a_id_accepted",
            "candidate_record_b_id_accepted",
            "candidate_record_a_role_accepted",
            "candidate_record_b_role_accepted",
            "future_distinctness_operation_type_accepted",
            "future_distinctness_operation_scope_accepted",
            "distinctness_evidence_policy_accepted",
            "cosmetic_difference_policy_accepted",
            "shared_evidence_policy_accepted",
            "not_distinct_policy_accepted",
            "failure_visibility_policy_accepted",
            "future_operation_shape_declared",
            "boundary_spec_markers_present",
            "completed_operation_terminal_summary_markers_present",
            "completed_operation_artifact_markers_present",
            "contaminated_lineage_markers_present",
            "existence_claim_evidence_check_terminal_summary_markers_present",
            "completed_operation_emitted_two_candidate_records",
            "completed_operation_did_not_prove_distinctness_beyond_id_and_role",
            "distinctness_operation_not_created",
            "distinctness_operation_not_performed",
            "distinctness_operation_not_recorded",
            "distinctness_result_not_recorded",
            "distinctness_not_supported",
            "candidate_records_not_distinct",
            "candidate_specific_content_not_created",
            "separate_seal_material_not_created",
            "separate_lineage_receipt_material_not_created",
            "separate_digest_material_not_created",
            "enumeration_not_treated_as_distinction",
            "id_and_role_difference_alone_not_treated_as_distinctness",
            "shared_evidence_reference_alone_not_treated_as_distinctness",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for code in (
            "FUTURE_DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
            "FUTURE_DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
            "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
            "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
            "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
            "NOT_DISTINCT_POLICY_NOT_EXPECTED",
            "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
            "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            "CANDIDATE_STANDING_AUTHORIZED_TRUE",
            "DESCENDANT_BODY_CREATED_TRUE",
            "STANDING_AUTHORIZED_TRUE",
            "CROSSING_AUTHORIZED_TRUE",
            "RELATION_AUTHORIZED_TRUE",
            "FIELD_MACHINERY_AUTHORIZED_TRUE",
            "RUNTIME_AUTHORIZED_TRUE",
            "CURRENTNESS_AUTHORIZED_TRUE",
            "AUTHORITY_AUTHORIZED_TRUE",
            "OUTPUT_AUTHORIZED_TRUE",
            "ACTION_AUTHORIZED_TRUE",
            "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
            "SYNCHRONIZATION_AUTHORIZED_TRUE",
            "FOLLOW_ON_AUTHORIZED_TRUE",
            "BOUNDARY_SPEC_MARKER_MISSING",
            "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            "CONTAMINATED_LINEAGE_MARKER_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "DISTINCTNESS_OPERATION_CREATED",
            "DISTINCTNESS_OPERATION_PERFORMED",
            "DISTINCTNESS_OPERATION_RECORDED",
            "DISTINCTNESS_RESULT_RECORDED",
            "DISTINCTNESS_SUPPORTED",
            "CANDIDATE_RECORDS_DISTINCT",
            "CANDIDATE_SPECIFIC_CONTENT_CREATED",
            "SEPARATE_SEAL_MATERIAL_CREATED",
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATED",
            "SEPARATE_DIGEST_MATERIAL_CREATED",
            "CANDIDATE_STANDING_AUTHORIZED",
            "CANDIDATE_STANDING_CREATED",
            "DESCENDANT_BODY_A_CREATED",
            "DESCENDANT_BODY_B_CREATED",
            "STANDING_DESCENDANT_CREATED",
            "FIRST_CROSSING_AUTHORIZED",
            "RELATION_CREATED",
            "FIELD_MACHINERY_CREATED",
            "RUNTIME_CREATED",
            "CURRENTNESS_CREATED",
            "AUTHORITY_CREATED",
            "STANDING_CREATED",
            "FOLLOW_ON_WORK_AUTHORIZED",
            "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
            "VALID_DERIVATION_EVENT_RECORDED",
            "AFFECTED_FILE_REPAIRED",
            "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDDEN",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASSED",
            "DIFFERENTIATION_OPERATION_OVERRIDDEN",
            "DIFFERENTIATION_OPERATION_BYPASSED",
            "SCAN_PERFORMED",
            "REPOSITORY_SCAN_PERFORMED",
            "REPAIR_PERFORMED",
            "VALIDATION_ENFORCED",
            "HIDDEN_REPAIR_PERFORMED",
            "SILENT_OVERWRITE_PERFORMED",
            "ENUMERATION_TREATED_AS_DISTINCTION",
            "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
            "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_records_boundary_from_synthetic_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            request = self.valid_request(paths)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
        self.assertIsInstance(result, dict)
        self.assert_recorded_boundary_posture(result)
        summary = resolver.build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
            result
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            self.boundary(result)["boundary_id"],
            "descendant_body_candidate_record_distinctness_operation_boundary_001",
        )
        for section in (
            "descendant_body_candidate_record_distinctness_operation_boundary_metadata",
            "declared_descendant_body_candidate_record_distinctness_operation_boundary_question",
            "upstream_basis",
            "distinctness_operation_boundary_basis",
            "descendant_body_candidate_record_distinctness_operation_boundary",
            "descendant_body_candidate_record_distinctness_operation_boundary_checks",
            "descendant_body_candidate_record_distinctness_operation_boundary_statement",
            "descendant_body_candidate_record_distinctness_operation_boundary_non_meaning",
            "additional_basis_required",
            "not_recorded_basis",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "descendant_body_candidate_record_distinctness_operation_boundary_summary",
        ):
            self.assertIn(section, result)

    def test_records_default_live_target_if_present(self) -> None:
        required = (
            REPO_ROOT
            / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min"
            / "descendant_body_differentiation_operation_001__descendant_body_differentiation_operation_v0_min_result.json",
            REPO_ROOT / "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md",
        )
        if not all(path.exists() for path in required):
            self.skipTest("default live distinctness-boundary basis is not present")
        request = resolver.build_declared_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_request()
        result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
            request
        )
        if result["outcome"] != resolver.OUTCOME_RECORDED:
            self.skipTest(
                "default live distinctness-boundary basis is present but not clean"
            )
        self.assert_recorded_boundary_posture(result)

    def test_do_not_record_intent_does_not_create_positive_boundary_record(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            request = self.valid_request(paths)
            request[
                "descendant_body_candidate_record_distinctness_operation_boundary_intent"
            ] = (
                "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
            )
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertIs(
            boundary[
                "descendant_body_candidate_record_distinctness_operation_boundary_recorded"
            ],
            False,
        )
        self.assertIs(boundary["boundary_created"], False)
        self.assertIs(boundary["distinctness_operation_not_created"], True)
        self.assertIs(boundary["distinctness_not_supported"], True)
        self.assertIs(boundary["candidate_records_not_distinct"], True)
        self.assertIs(boundary["candidate_standing_authorized"], False)
        self.assertIs(boundary["descendant_body_created"], False)
        self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            request = self.valid_request(paths)
            request[
                "descendant_body_candidate_record_distinctness_operation_boundary_intent"
            ] = "BLOCK_DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY"
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
        self.assert_blocked_with_public_code(result)

    def test_request_shape_and_blocking_behavior(self) -> None:
        simple_cases: list[tuple[str, Any, str | None]] = [
            ("non_mapping", "not a mapping", None),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            for name, payload, expected_code in simple_cases:
                with self.subTest(name=name):
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        payload
                    )
                    self.assert_blocked_with_public_code(result)
                    if expected_code:
                        self.assertEqual(self.block_code(result), expected_code)

            mutation_cases: list[tuple[str, dict[str, Any], str]] = [
                (
                    "missing_question",
                    {
                        "descendant_body_candidate_record_distinctness_operation_boundary_question": ""
                    },
                    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_QUESTION_UNDECLARED",
                ),
                (
                    "unsupported_intent",
                    {
                        "descendant_body_candidate_record_distinctness_operation_boundary_intent": "UNSUPPORTED"
                    },
                    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_INTENT_UNSUPPORTED",
                ),
                (
                    "missing_completed_summary",
                    {"completed_operation_terminal_summary_reference": ""},
                    "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
                ),
                (
                    "missing_operation_artifact",
                    {"completed_operation_artifact_reference": ""},
                    "COMPLETED_OPERATION_ARTIFACT_REFERENCE_MISSING",
                ),
                (
                    "missing_contaminated_lineage",
                    {"contaminated_lineage_reference": ""},
                    "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
                ),
                (
                    "missing_evidence_summary",
                    {"existence_claim_evidence_check_terminal_summary_reference": ""},
                    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
                ),
                (
                    "missing_candidate_a_reference",
                    {"candidate_record_a_reference": ""},
                    "CANDIDATE_RECORD_A_REFERENCE_MISSING",
                ),
                (
                    "missing_candidate_b_reference",
                    {"candidate_record_b_reference": ""},
                    "CANDIDATE_RECORD_B_REFERENCE_MISSING",
                ),
                (
                    "wrong_candidate_a_id",
                    {"candidate_record_a_id": "wrong"},
                    "CANDIDATE_RECORD_A_ID_NOT_EXPECTED",
                ),
                (
                    "wrong_candidate_b_id",
                    {"candidate_record_b_id": "wrong"},
                    "CANDIDATE_RECORD_B_ID_NOT_EXPECTED",
                ),
                (
                    "wrong_candidate_a_role",
                    {"candidate_record_a_role": "WRONG"},
                    "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED",
                ),
                (
                    "wrong_candidate_b_role",
                    {"candidate_record_b_role": "WRONG"},
                    "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED",
                ),
                (
                    "missing_future_type",
                    {"future_distinctness_operation_type": None},
                    "FUTURE_DISTINCTNESS_OPERATION_TYPE_MISSING",
                ),
                (
                    "wrong_future_type",
                    {"future_distinctness_operation_type": "WRONG"},
                    "FUTURE_DISTINCTNESS_OPERATION_TYPE_NOT_EXPECTED",
                ),
                (
                    "missing_future_scope",
                    {"future_distinctness_operation_scope": None},
                    "FUTURE_DISTINCTNESS_OPERATION_SCOPE_MISSING",
                ),
                (
                    "wrong_future_scope",
                    {"future_distinctness_operation_scope": "WRONG"},
                    "FUTURE_DISTINCTNESS_OPERATION_SCOPE_NOT_EXPECTED",
                ),
                (
                    "missing_distinctness_policy",
                    {"distinctness_evidence_policy": None},
                    "DISTINCTNESS_EVIDENCE_POLICY_MISSING",
                ),
                (
                    "wrong_distinctness_policy",
                    {"distinctness_evidence_policy": "WRONG"},
                    "DISTINCTNESS_EVIDENCE_POLICY_NOT_EXPECTED",
                ),
                (
                    "missing_cosmetic_policy",
                    {"cosmetic_difference_policy": None},
                    "COSMETIC_DIFFERENCE_POLICY_MISSING",
                ),
                (
                    "wrong_cosmetic_policy",
                    {"cosmetic_difference_policy": "WRONG"},
                    "COSMETIC_DIFFERENCE_POLICY_NOT_EXPECTED",
                ),
                (
                    "missing_shared_policy",
                    {"shared_evidence_policy": None},
                    "SHARED_EVIDENCE_POLICY_MISSING",
                ),
                (
                    "wrong_shared_policy",
                    {"shared_evidence_policy": "WRONG"},
                    "SHARED_EVIDENCE_POLICY_NOT_EXPECTED",
                ),
                (
                    "missing_not_distinct_policy",
                    {"not_distinct_policy": None},
                    "NOT_DISTINCT_POLICY_MISSING",
                ),
                (
                    "wrong_not_distinct_policy",
                    {"not_distinct_policy": "WRONG"},
                    "NOT_DISTINCT_POLICY_NOT_EXPECTED",
                ),
                (
                    "missing_failure_policy",
                    {"failure_visibility_policy": None},
                    "FAILURE_VISIBILITY_POLICY_MISSING",
                ),
                (
                    "wrong_failure_policy",
                    {"failure_visibility_policy": "WRONG"},
                    "FAILURE_VISIBILITY_POLICY_NOT_EXPECTED",
                ),
                (
                    "candidate_count_not_two",
                    {"candidate_record_count_required": 3},
                    "CANDIDATE_RECORD_COUNT_REQUIRED_NOT_TWO",
                ),
                (
                    "missing_future_shape",
                    {"future_operation_shape": None},
                    "FUTURE_OPERATION_SHAPE_MISSING",
                ),
                (
                    "malformed_future_shape",
                    {"future_operation_shape": []},
                    "FUTURE_OPERATION_SHAPE_MALFORMED",
                ),
                ("scan_allowed", {"scan_allowed": True}, "SCAN_ALLOWED_TRUE"),
                ("repair_allowed", {"repair_allowed": True}, "REPAIR_ALLOWED_TRUE"),
                (
                    "validation_allowed",
                    {"validation_enforcement_allowed": True},
                    "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
                ),
                (
                    "candidate_standing_authorized",
                    {"candidate_standing_authorized": True},
                    "CANDIDATE_STANDING_AUTHORIZED_TRUE",
                ),
                (
                    "descendant_body_created",
                    {"descendant_body_created": True},
                    "DESCENDANT_BODY_CREATED_TRUE",
                ),
                (
                    "standing_authorized",
                    {"standing_authorized": True},
                    "STANDING_AUTHORIZED_TRUE",
                ),
                (
                    "crossing_authorized",
                    {"crossing_authorized": True},
                    "CROSSING_AUTHORIZED_TRUE",
                ),
                ("relation_authorized", {"relation_authorized": True}, "RELATION_AUTHORIZED_TRUE"),
                (
                    "field_machinery_authorized",
                    {"field_machinery_authorized": True},
                    "FIELD_MACHINERY_AUTHORIZED_TRUE",
                ),
                ("runtime_authorized", {"runtime_authorized": True}, "RUNTIME_AUTHORIZED_TRUE"),
                (
                    "currentness_authorized",
                    {"currentness_authorized": True},
                    "CURRENTNESS_AUTHORIZED_TRUE",
                ),
                (
                    "authority_authorized",
                    {"authority_authorized": True},
                    "AUTHORITY_AUTHORIZED_TRUE",
                ),
                ("output_authorized", {"output_authorized": True}, "OUTPUT_AUTHORIZED_TRUE"),
                ("action_authorized", {"action_authorized": True}, "ACTION_AUTHORIZED_TRUE"),
                (
                    "derivative_reception_authorized",
                    {"derivative_reception_authorized": True},
                    "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
                ),
                (
                    "synchronization_authorized",
                    {"synchronization_authorized": True},
                    "SYNCHRONIZATION_AUTHORIZED_TRUE",
                ),
                ("follow_on_authorized", {"follow_on_authorized": True}, "FOLLOW_ON_AUTHORIZED_TRUE"),
            ]
            requested_cases = (
                ("request_repository_scan", "repository_scan_requested", "REQUESTED_REPOSITORY_SCAN"),
                ("request_file_discovery", "file_discovery_requested", "REQUESTED_FILE_DISCOVERY"),
                (
                    "request_affected_file_repair",
                    "affected_file_repair_requested",
                    "REQUESTED_AFFECTED_FILE_REPAIR",
                ),
                (
                    "request_affected_file_mutation",
                    "affected_file_mutation_requested",
                    "REQUESTED_AFFECTED_FILE_MUTATION",
                ),
                (
                    "request_prior_unsupported_claim_validation",
                    "prior_unsupported_claim_validation_requested",
                    "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION",
                ),
                (
                    "request_existence_claim_evidence_check_override",
                    "existence_claim_evidence_check_override_requested",
                    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_OVERRIDE",
                ),
                (
                    "request_existence_claim_evidence_check_bypass",
                    "existence_claim_evidence_check_bypass_requested",
                    "REQUESTED_EXISTENCE_CLAIM_EVIDENCE_CHECK_BYPASS",
                ),
                (
                    "request_differentiation_operation_override",
                    "differentiation_operation_override_requested",
                    "REQUESTED_DIFFERENTIATION_OPERATION_OVERRIDE",
                ),
                (
                    "request_differentiation_operation_bypass",
                    "differentiation_operation_bypass_requested",
                    "REQUESTED_DIFFERENTIATION_OPERATION_BYPASS",
                ),
                (
                    "request_distinctness_operation_performance",
                    "distinctness_operation_performance_requested",
                    "REQUESTED_DISTINCTNESS_OPERATION_PERFORMANCE",
                ),
                (
                    "request_distinctness_result_recording",
                    "distinctness_result_recording_requested",
                    "REQUESTED_DISTINCTNESS_RESULT_RECORDING",
                ),
                (
                    "request_distinctness_evidence_creation",
                    "distinctness_evidence_creation_requested",
                    "REQUESTED_DISTINCTNESS_EVIDENCE_CREATION",
                ),
                (
                    "request_candidate_specific_content_creation",
                    "candidate_specific_content_creation_requested",
                    "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_CREATION",
                ),
                (
                    "request_separate_seal_material_creation",
                    "separate_seal_material_creation_requested",
                    "REQUESTED_SEPARATE_SEAL_MATERIAL_CREATION",
                ),
                (
                    "request_separate_lineage_receipt_material_creation",
                    "separate_lineage_receipt_material_creation_requested",
                    "REQUESTED_SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATION",
                ),
                (
                    "request_separate_digest_material_creation",
                    "separate_digest_material_creation_requested",
                    "REQUESTED_SEPARATE_DIGEST_MATERIAL_CREATION",
                ),
                (
                    "request_candidate_records_distinct",
                    "candidate_records_distinct_requested",
                    "REQUESTED_CANDIDATE_RECORDS_DISTINCT",
                ),
                (
                    "request_candidate_standing_authorization",
                    "candidate_standing_authorization_requested",
                    "REQUESTED_CANDIDATE_STANDING_AUTHORIZATION",
                ),
                (
                    "request_descendant_body_creation",
                    "descendant_body_creation_requested",
                    "REQUESTED_DESCENDANT_BODY_CREATION",
                ),
                (
                    "request_standing_descendant_creation",
                    "standing_descendant_creation_requested",
                    "REQUESTED_STANDING_DESCENDANT_CREATION",
                ),
                (
                    "request_descendant_standing_check",
                    "descendant_standing_check_requested",
                    "REQUESTED_DESCENDANT_STANDING_CHECK",
                ),
                (
                    "request_crossing_authorization",
                    "crossing_authorization_requested",
                    "REQUESTED_CROSSING_AUTHORIZATION",
                ),
                ("request_relation_creation", "relation_creation_requested", "REQUESTED_RELATION_CREATION"),
                (
                    "request_field_machinery_creation",
                    "field_machinery_creation_requested",
                    "REQUESTED_FIELD_MACHINERY_CREATION",
                ),
                ("request_runtime_creation", "runtime_creation_requested", "REQUESTED_RUNTIME_CREATION"),
                (
                    "request_currentness_creation",
                    "currentness_creation_requested",
                    "REQUESTED_CURRENTNESS_CREATION",
                ),
                (
                    "request_authority_creation",
                    "authority_creation_requested",
                    "REQUESTED_AUTHORITY_CREATION",
                ),
                (
                    "request_output_authorization",
                    "output_authorization_requested",
                    "REQUESTED_OUTPUT_AUTHORIZATION",
                ),
                (
                    "request_action_authorization",
                    "action_authorization_requested",
                    "REQUESTED_ACTION_AUTHORIZATION",
                ),
                (
                    "request_derivative_reception_authorization",
                    "derivative_reception_authorization_requested",
                    "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION",
                ),
                (
                    "request_synchronization_authorization",
                    "synchronization_authorization_requested",
                    "REQUESTED_SYNCHRONIZATION_AUTHORIZATION",
                ),
                (
                    "request_follow_on_authorization",
                    "follow_on_authorization_requested",
                    "REQUESTED_FOLLOW_ON_AUTHORIZATION",
                ),
                (
                    "return_raw_markdown_body",
                    "raw_markdown_body_return_requested",
                    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
                ),
            )
            for label, supported_key, code in requested_cases:
                mutation_cases.append((label, {label: True, supported_key: True}, code))
            mutation_cases.extend(
                [
                    (
                        "enumeration_treated_as_distinction",
                        {"enumeration_treated_as_distinction": True},
                        "ENUMERATION_TREATED_AS_DISTINCTION",
                    ),
                    (
                        "id_and_role_difference_treated_as_distinctness",
                        {"id_and_role_difference_treated_as_distinctness": True},
                        "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
                    ),
                    (
                        "shared_evidence_reference_treated_as_distinctness",
                        {"shared_evidence_reference_treated_as_distinctness": True},
                        "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
                    ),
                ]
            )
            for index, (name, mutation, expected_code) in enumerate(mutation_cases):
                with self.subTest(case=name):
                    request = self.valid_request(paths)
                    request.update(mutation)
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code, name)

    def test_marker_validation_blocking_behavior(self) -> None:
        def artifact_set(path: list[Any], value: Any):
            def mutate(artifact: dict[str, Any]) -> None:
                current: Any = artifact
                for part in path[:-1]:
                    current = current[part]
                current[path[-1]] = value

            return mutate

        def remove_record(candidate_id: str):
            def mutate(artifact: dict[str, Any]) -> None:
                artifact["descendant_body_differentiation_candidate_records"] = [
                    record
                    for record in artifact["descendant_body_differentiation_candidate_records"]
                    if record["candidate_record_id"] != candidate_id
                ]

            return mutate

        cases: list[tuple[str, dict[str, Any], str]] = [
            (
                "boundary_marker",
                {"remove_boundary_marker": BOUNDARY_SPEC_MARKERS[0]},
                "BOUNDARY_SPEC_MARKER_MISSING",
            ),
            (
                "completed_summary_marker",
                {"remove_completed_summary_marker": COMPLETED_OPERATION_SUMMARY_MARKERS[0]},
                "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
            (
                "artifact_outcome",
                {"artifact_mutator": artifact_set(["outcome"], "WRONG")},
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_failed_count",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation_summary",
                            "failed_check_count",
                        ],
                        1,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_operation_type",
                {
                    "artifact_mutator": artifact_set(
                        ["descendant_body_differentiation_operation", "operation_type"],
                        "WRONG",
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_operation_scope",
                {
                    "artifact_mutator": artifact_set(
                        ["descendant_body_differentiation_operation", "operation_scope"],
                        "WRONG",
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_policy",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_record_policy",
                        ],
                        "WRONG",
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_operation_result_created",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "operation_result_created",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_records_created",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_records_created",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_count",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_record_count_emitted",
                        ],
                        1,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_exactly_two",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "exactly_two_candidate_records_emitted",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_evidence",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_records_have_operation_evidence",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_non_standing",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_records_non_standing",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_candidate_lineage",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "candidate_records_do_not_inherit_from_contaminated_lineage",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_descendant_a",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "descendant_body_a_created",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_descendant_b",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "descendant_body_b_created",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_standing_descendant",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "standing_descendant_created",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_first_crossing",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_operation",
                            "first_crossing_authorized",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "artifact_relation",
                {
                    "artifact_mutator": artifact_set(
                        ["descendant_body_differentiation_operation", "relation_created"],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "remove_candidate_a",
                {"artifact_mutator": remove_record("descendant_body_basis_candidate_a_001")},
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "remove_candidate_b",
                {"artifact_mutator": remove_record("descendant_body_basis_candidate_b_001")},
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_a_role",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "candidate_role",
                        ],
                        "WRONG",
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_b_role",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            1,
                            "candidate_role",
                        ],
                        "WRONG",
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_created_by_operation",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "candidate_record_created_by_operation",
                        ],
                        False,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_standing",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "candidate_record_standing",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_descendant_body",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "descendant_body_created",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_contaminated_inheritance",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "inherited_from_contaminated_lineage",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "candidate_prior_claim",
                {
                    "artifact_mutator": artifact_set(
                        [
                            "descendant_body_differentiation_candidate_records",
                            0,
                            "prior_unsupported_claim_validated",
                        ],
                        True,
                    )
                },
                "COMPLETED_OPERATION_ARTIFACT_MARKER_MISSING",
            ),
            (
                "contaminated_marker",
                {"remove_contaminated_marker": CONTAMINATED_LINEAGE_MARKERS[0]},
                "CONTAMINATED_LINEAGE_MARKER_MISSING",
            ),
            (
                "evidence_marker",
                {"remove_evidence_marker": EVIDENCE_CHECK_SUMMARY_MARKERS[0]},
                "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            ),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for index, (name, kwargs, expected_code) in enumerate(cases):
                with self.subTest(case=name):
                    paths = self.write_synthetic_basis(root / self.safe_json_filename(name, index), **kwargs)
                    request = self.valid_request(paths)
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "distinctness_operation_created": "DISTINCTNESS_OPERATION_CREATED",
            "distinctness_operation_performed": "DISTINCTNESS_OPERATION_PERFORMED",
            "distinctness_operation_recorded": "DISTINCTNESS_OPERATION_RECORDED",
            "distinctness_result_recorded": "DISTINCTNESS_RESULT_RECORDED",
            "distinctness_supported": "DISTINCTNESS_SUPPORTED",
            "candidate_records_distinct": "CANDIDATE_RECORDS_DISTINCT",
            "candidate_specific_content_created": "CANDIDATE_SPECIFIC_CONTENT_CREATED",
            "separate_seal_material_created": "SEPARATE_SEAL_MATERIAL_CREATED",
            "separate_lineage_receipt_material_created": "SEPARATE_LINEAGE_RECEIPT_MATERIAL_CREATED",
            "separate_digest_material_created": "SEPARATE_DIGEST_MATERIAL_CREATED",
            "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED_TRUE",
            "candidate_standing_created": "CANDIDATE_STANDING_CREATED",
            "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
            "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
            "standing_descendant_created": "STANDING_DESCENDANT_CREATED",
            "descendant_standing_check_performed": "DESCENDANT_STANDING_CHECK_PERFORMED",
            "first_crossing_authorized": "FIRST_CROSSING_AUTHORIZED",
            "relation_created": "RELATION_CREATED",
            "field_machinery_created": "FIELD_MACHINERY_CREATED",
            "runtime_created": "RUNTIME_CREATED",
            "api_created": "API_CREATED",
            "currentness_created": "CURRENTNESS_CREATED",
            "authority_created": "AUTHORITY_CREATED",
            "standing_created": "STANDING_CREATED",
            "output_authorized": "OUTPUT_AUTHORIZED_TRUE",
            "action_authorized": "ACTION_AUTHORIZED_TRUE",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE",
            "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED_TRUE",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
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
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "repair_performed": "REPAIR_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
            "enumeration_treated_as_distinction": "ENUMERATION_TREATED_AS_DISTINCTION",
            "id_and_role_difference_treated_as_distinctness": "ID_AND_ROLE_DIFFERENCE_TREATED_AS_DISTINCTNESS",
            "shared_evidence_reference_treated_as_distinctness": "SHARED_EVIDENCE_REFERENCE_TREATED_AS_DISTINCTNESS",
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            for key, expected_code in cases.items():
                with self.subTest(key=key):
                    request = self.valid_request(paths)
                    request[key] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = self.valid_request(paths)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = (
                ("missing", lambda request: request.pop("declared_non_claims")),
                ("non_mapping", lambda request: request.update({"declared_non_claims": []})),
                (
                    "missing_key",
                    lambda request: request["declared_non_claims"].pop(
                        resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                    ),
                ),
                (
                    "non_bool",
                    lambda request: request["declared_non_claims"].update(
                        {resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}
                    ),
                ),
            )
            for name, mutate in malformed_cases:
                with self.subTest(case=name):
                    request = self.valid_request(paths)
                    mutate(request)
                    result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)

    def test_distinctness_negative_boundary_invariants(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                self.valid_request(self.write_synthetic_basis(Path(temp_dir)))
            )
        self.assert_recorded_boundary_posture(result)
        boundary = self.boundary(result)
        self.assertIs(boundary["completed_operation_emitted_two_candidate_records"], True)
        self.assertIs(
            boundary["completed_operation_did_not_prove_distinctness_beyond_id_and_role"],
            True,
        )
        for key in (
            "distinctness_supported",
            "candidate_records_distinct",
            "candidate_standing_authorized",
        ):
            self.assertIs(result["non_claims"][key], False)

    def test_raw_markdown_body_containment(self) -> None:
        extra = "\n".join(
            [
                f"raw_body: {SENTINELS[0]}",
                f"hidden_repo_state: {SENTINELS[1]}",
                f"current_working_tree: {SENTINELS[2]}",
            ]
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.write_synthetic_basis(Path(temp_dir), extra_text=extra)
            request = self.valid_request(paths)
            request["raw_body"] = SENTINELS[0]
            request_before = copy.deepcopy(request)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assert_no_raw_markdown_body(result)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.BOUNDARY_TYPE, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_positive_overreach(result)
        self.assertEqual(request, request_before)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            paths = self.write_synthetic_basis(base)
            request = self.valid_request(paths)
            request_path = self._write_json(base / "request.json", request)
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path(
                request_path
            )
            self.assert_recorded_boundary_posture(result)
            summary = resolver.build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
                result
            )
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)

            missing = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path(
                base / "missing.json"
            )
            self.assert_blocked_with_public_code(missing)
            malformed_path = base / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)
            array_path = self._write_json(base / "array.json", [])
            array_result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)

            output_dir = base / "write_output"
            output_dir.mkdir()
            first_path = resolver.write_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result(
                result, output_dir
            )
            second_path = resolver.write_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result(
                result, output_dir
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn(
                "descendant_body_candidate_record_distinctness_operation_boundary_v0_min_result",
                first_path.name,
            )
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_roots = (
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary_v0_min",
                "source_transfer",
                "source_receipt",
                "public_api",
                "participant_facing_interface",
                "distributed_network",
                "runtime_hosting",
                "runtime_loop",
                "daemon",
            )
            path_text = str(first_path)
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, path_text)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            paths = self.write_synthetic_basis(base)
            request = self.valid_request(paths)
            request["raw_body"] = SENTINELS[0]
            before_request = copy.deepcopy(request)
            before_text = {key: path.read_text(encoding="utf-8") for key, path in paths.items() if path.suffix == ".md"}
            before_artifact = json.loads(paths["artifact"].read_text(encoding="utf-8"))
            resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
            self.assertEqual(request, before_request)
            after_text = {key: path.read_text(encoding="utf-8") for key, path in paths.items() if path.suffix == ".md"}
            after_artifact = json.loads(paths["artifact"].read_text(encoding="utf-8"))
            self.assertEqual(before_text, after_text)
            self.assertEqual(before_artifact, after_artifact)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                self.valid_request(self.write_synthetic_basis(Path(temp_dir)))
            )
        summary = resolver.build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
            result
        )
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(
            summary["future_distinctness_operation_type"],
            resolver.FUTURE_DISTINCTNESS_OPERATION_TYPE,
        )
        self.assertEqual(
            summary["future_distinctness_operation_scope"],
            resolver.FUTURE_DISTINCTNESS_OPERATION_SCOPE,
        )
        self.assertEqual(
            summary["distinctness_evidence_policy"], resolver.DISTINCTNESS_EVIDENCE_POLICY
        )
        self.assertEqual(
            summary["cosmetic_difference_policy"], resolver.COSMETIC_DIFFERENCE_POLICY
        )
        self.assertEqual(summary["shared_evidence_policy"], resolver.SHARED_EVIDENCE_POLICY)
        self.assertEqual(summary["not_distinct_policy"], resolver.NOT_DISTINCT_POLICY)
        self.assertEqual(
            summary["failure_visibility_policy"], resolver.FAILURE_VISIBILITY_POLICY
        )
        self.assertIs(summary["boundary_recorded"], True)
        self.assertIs(summary["boundary_created"], True)
        self.assertIs(summary["completed_operation_emitted_two_candidate_records"], True)
        self.assertIs(
            summary["completed_operation_did_not_prove_distinctness_beyond_id_and_role"],
            True,
        )
        for key in (
            "distinctness_operation_created",
            "distinctness_operation_performed",
            "distinctness_operation_recorded",
            "distinctness_supported",
            "candidate_records_distinct",
            "candidate_specific_content_created",
            "separate_seal_material_created",
            "separate_lineage_receipt_material_created",
            "separate_digest_material_created",
            "candidate_standing_authorized",
            "descendant_body_created",
            "prior_unsupported_claims_validated",
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
            "scan_allowed",
            "repair_allowed",
            "validation_enforcement_allowed",
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
            self.assertIs(summary[key], False, key)
        for key in (
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
            "hidden_repair_not_performed",
            "silent_overwrite_not_performed",
            "boundary_spec_markers_present",
            "completed_operation_terminal_summary_markers_present",
            "completed_operation_artifact_markers_present",
            "contaminated_lineage_markers_present",
            "existence_claim_evidence_check_terminal_summary_markers_present",
            "enumeration_not_treated_as_distinction",
            "id_and_role_difference_alone_not_treated_as_distinctness",
            "shared_evidence_reference_alone_not_treated_as_distinctness",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(summary[key], True, key)

    def test_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(self.write_synthetic_basis(Path(temp_dir)))
            result = resolver.resolve_descendant_body_candidate_record_distinctness_operation_boundary_v0_min(
                request
            )
        summary = resolver.build_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_summary(
            result
        )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_recorded_boundary_posture(result)


if __name__ == "__main__":
    unittest.main()
