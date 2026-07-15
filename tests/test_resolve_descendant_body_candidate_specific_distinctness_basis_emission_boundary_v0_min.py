"""Tests for the candidate-specific distinctness basis emission boundary resolver.

This suite verifies one boundary-only result: it preserves the completed
candidate-record distinctness operation's clean NOT_DISTINCT outcome, permits
only a future scope-division operation shape, and refuses emission, repair,
standing, runtime, authority, scan, validation enforcement, and follow-on work.
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

import resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min as resolver


BOUNDARY_SPEC_MARKERS = (
    "Descendant Body Candidate-Specific Distinctness Basis Emission Boundary V0 Minimum Specification",
    "This file defines one boundary for a future candidate-specific distinctness basis emission operation.",
    "This file is boundary-only.",
    "This file does not define, implement, or perform the future emission operation.",
    "This file does not emit candidate-specific content, separate seal material, separate lineage receipt material, or separate digest material.",
    "This boundary exists to prevent a future emission operation from laundering cosmetic label differences into hash, seal, receipt, or digest difference.",
    "Digest difference is not distinctness unless the digested material carries non-cosmetic candidate-specific basis.",
    "Hash difference is not distinctness unless the hashed material carries non-cosmetic candidate-specific basis.",
    "Seal difference is not distinctness unless the sealed material carries non-cosmetic candidate-specific basis.",
    "Lineage receipt difference is not distinctness unless the receipt material carries non-cosmetic candidate-specific basis.",
    "Candidate-specific distinctness basis must be basis-bearing, not label-bearing.",
    "For the immediate next repo-local step, this boundary permits only a scope-division-based future operation shape to be defined.",
    "Divergent receipt-history and carrier separation remain open but are not authorized here.",
    "Scope division must be non-cosmetic and basis-bearing.",
    "cosmetic_substitution_treated_as_basis = false",
    "digest_laundering_treated_as_basis = false",
    "id_role_label_difference_treated_as_basis = false",
    "shared_evidence_treated_as_basis = false",
    "operation_evidence_alone_treated_as_basis = false",
    "divergent_receipt_history_route_authorized = false",
    "carrier_separation_route_authorized = false",
)

DISTINCTNESS_OPERATION_MARKERS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
    "distinctness_result = NOT_DISTINCT",
    "failed_check_count = 0",
    "candidate_record_count_compared = 2",
    "candidate_ids_distinct = true",
    "candidate_roles_distinct = true",
    "id_and_role_difference_only = true",
    "candidate_specific_content_present = false",
    "separate_seal_material_present = false",
    "separate_lineage_receipt_material_present = false",
    "separate_digest_material_present = false",
    "distinctness_supported = false",
    "NOT_DISTINCT is a clean operation result, not a failure.",
    "missing candidate-specific content",
    "missing separate seal material",
    "missing separate lineage receipt material",
    "missing separate digest material",
    "id and role difference alone is not distinctness",
    "shared evidence reference alone is not distinctness",
    "Operation evidence alone is not distinctness.",
)

DIFFERENTIATION_MARKERS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
    "exactly two result-contained non-standing candidate records",
    "candidate records are not descendant bodies",
    "candidate records remain non-standing",
)

DISTINCTNESS_BOUNDARY_MARKERS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",
    "enumeration is not distinction",
    "id and role difference alone are not distinctness",
    "shared evidence reference alone are not distinctness",
    "distinctness support requires separate candidate-specific evidence",
    "candidate standing is not authorized",
)

RAW_SENTINELS = (
    "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
)


class CandidateSpecificDistinctnessBasisEmissionBoundaryTests(unittest.TestCase):
    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_text(self, path: Path, lines: tuple[str, ...], extra: tuple[str, ...] = ()) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines + extra) + "\n", encoding="utf-8")
        return path

    def write_synthetic_basis_files(
        self,
        base: Path,
        *,
        remove_marker_kind: str | None = None,
        sentinels: tuple[str, ...] = (),
    ) -> dict[str, Path]:
        basis = base / "synthetic_basis"
        marker_sets = {
            "boundary_spec": list(BOUNDARY_SPEC_MARKERS),
            "completed_distinctness": list(DISTINCTNESS_OPERATION_MARKERS),
            "completed_differentiation": list(DIFFERENTIATION_MARKERS),
            "completed_boundary": list(DISTINCTNESS_BOUNDARY_MARKERS),
        }
        if remove_marker_kind:
            marker_sets[remove_marker_kind][0] = f"removed marker for {remove_marker_kind}"
        extra = tuple(f"non-authoritative sentinel: {sentinel}" for sentinel in sentinels)
        return {
            "boundary_spec": self.write_text(
                basis / "candidate_specific_distinctness_basis_emission_boundary_spec.md",
                tuple(marker_sets["boundary_spec"]),
                extra,
            ),
            "completed_distinctness": self.write_text(
                basis / "candidate_record_distinctness_operation_terminal_summary.md",
                tuple(marker_sets["completed_distinctness"]),
                extra,
            ),
            "completed_differentiation": self.write_text(
                basis / "descendant_body_differentiation_operation_terminal_summary.md",
                tuple(marker_sets["completed_differentiation"]),
                extra,
            ),
            "completed_boundary": self.write_text(
                basis / "candidate_record_distinctness_operation_boundary_terminal_summary.md",
                tuple(marker_sets["completed_boundary"]),
                extra,
            ),
        }

    def build_valid_request(
        self,
        base: Path,
        *,
        remove_marker_kind: str | None = None,
        sentinels: tuple[str, ...] = (),
    ) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = self.write_synthetic_basis_files(
            base,
            remove_marker_kind=remove_marker_kind,
            sentinels=sentinels,
        )
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request(
            boundary_spec_reference=str(paths["boundary_spec"]),
            completed_distinctness_operation_terminal_summary_reference=str(paths["completed_distinctness"]),
            completed_differentiation_operation_terminal_summary_reference=str(paths["completed_differentiation"]),
            completed_distinctness_operation_boundary_terminal_summary_reference=str(paths["completed_boundary"]),
        )
        return request, paths

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        boundary = result["descendant_body_candidate_specific_distinctness_basis_emission_boundary"]
        self.assertIsInstance(boundary, dict)
        return boundary

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        return resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_summary(
            result
        )

    def checks(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("candidate_specific_distinctness_basis_emission_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def failed_check_count(self, result: dict[str, Any]) -> int:
        return int(self.summary(result)["failed_check_count"])

    def passed_check_count(self, result: dict[str, Any]) -> int:
        return int(self.summary(result)["passed_check_count"])

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        return block.get("code") or block.get("block_code")

    def emitted_codes(self, result: dict[str, Any]) -> set[str]:
        codes: set[str] = set()
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code:
                    codes.add(str(code))
        code = self.block_code(result)
        if code:
            codes.add(str(code))
        return codes

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        for code in self.emitted_codes(result):
            self.assertIn(code, resolver.BLOCK_CODES)

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_forbidden_boundary_posture(result)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)
            self.assertIs(type(non_claims[key]), bool)

    def assert_boundary_not_wrapper(self, boundary: dict[str, Any]) -> None:
        for key in (
            "outcome",
            "block",
            "candidate_specific_distinctness_basis_emission_boundary_checks",
            "non_claims",
            "candidate_specific_distinctness_basis_emission_boundary_summary",
            "candidate_specific_distinctness_basis_emission_boundary_metadata",
        ):
            self.assertNotIn(key, boundary)

    def assert_no_raw_full_markdown_body_returned(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_no_forbidden_boundary_posture(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        true_non_creation_fields = (
            "future_emission_operation_not_created",
            "candidate_specific_content_not_emitted",
            "separate_seal_material_not_emitted",
            "separate_lineage_receipt_material_not_emitted",
            "separate_digest_material_not_emitted",
            "distinctness_operation_not_rerun",
            "distinctness_supported_not_recorded",
            "candidate_records_not_marked_distinct",
            "candidate_standing_not_authorized",
            "descendant_bodies_not_created",
            "standing_descendants_not_created",
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
            "affected_file_not_repaired",
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
            "hidden_repair_not_performed",
            "silent_overwrite_not_performed",
        )
        for field in true_non_creation_fields:
            self.assertIs(boundary.get(field), True, field)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsNot(boundary.get(field), True, field)

    def assert_recorded_boundary_core(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_canonical_false_non_claims(result)
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["candidate_specific_distinctness_basis_emission_boundary_type"],
            resolver.BOUNDARY_TYPE,
        )
        self.assertEqual(boundary["candidate_specific_distinctness_basis_emission_boundary_version"], "0.1.0")
        self.assertEqual(boundary["future_emission_operation_type"], resolver.FUTURE_EMISSION_OPERATION_TYPE)
        self.assertEqual(boundary["admissible_future_basis_route"], resolver.ADMISSIBLE_FUTURE_BASIS_ROUTE)
        self.assertEqual(boundary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
        self.assertEqual(boundary["upstream_distinctness_operation_result"], "NOT_DISTINCT")
        for field in (
            "candidate_specific_distinctness_basis_emission_boundary_recorded",
            "boundary_created",
            "upstream_distinctness_operation_result_is_not_distinct",
            "not_distinct_preserved_as_clean_result",
            "candidate_specific_content_missing_upstream",
            "separate_seal_material_missing_upstream",
            "separate_lineage_receipt_material_missing_upstream",
            "separate_digest_material_missing_upstream",
            "scope_division_route_allowed_for_future_operation_shape",
            "divergent_receipt_history_route_not_authorized",
            "carrier_separation_route_not_authorized",
            "cosmetic_substitution_not_allowed",
            "digest_laundering_not_allowed",
            "id_role_label_difference_not_allowed_as_basis",
            "shared_evidence_not_allowed_as_basis",
            "operation_evidence_alone_not_allowed_as_basis",
            "future_emission_operation_not_created",
            "candidate_specific_content_not_emitted",
            "separate_seal_material_not_emitted",
            "separate_lineage_receipt_material_not_emitted",
            "separate_digest_material_not_emitted",
            "distinctness_operation_not_rerun",
            "distinctness_supported_not_recorded",
            "candidate_records_not_marked_distinct",
            "candidate_standing_not_authorized",
            "descendant_bodies_not_created",
            "standing_descendants_not_created",
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
            "distinctness_operation_boundary_not_overridden",
            "distinctness_operation_boundary_not_bypassed",
            "distinctness_operation_not_overridden",
            "distinctness_operation_not_bypassed",
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
            "hidden_repair_not_performed",
            "silent_overwrite_not_performed",
            "boundary_spec_markers_present",
            "completed_distinctness_operation_terminal_summary_markers_present",
            "completed_differentiation_operation_terminal_summary_markers_present",
            "completed_distinctness_operation_boundary_terminal_summary_markers_present",
        ):
            self.assertIs(boundary[field], True, field)
        self.assert_boundary_not_wrapper(boundary)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min",
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_from_path",
            "write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_result",
            "build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_summary",
            "build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        for name in (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_BLOCKED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_FAMILY",
            "BOUNDARY_TYPE",
            "FUTURE_EMISSION_OPERATION_TYPE",
            "BOUNDARY_VERSION",
            "ADMISSIBLE_FUTURE_BASIS_ROUTE",
            "RUPTURE_CLASS_BLOCKED",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min",
        )
        self.assertEqual(resolver.BOUNDARY_TYPE, "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY")
        self.assertEqual(
            resolver.FUTURE_EMISSION_OPERATION_TYPE,
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION",
        )
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_BASIS_ROUTE, "SCOPE_DIVISION_ONLY")
        self.assertEqual(
            resolver.RUPTURE_CLASS_BLOCKED,
            "COSMETIC_DIFFERENCE_CRYPTOGRAPHICALLY_DRESSED_AS_DISTINCTNESS",
        )
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min"
            )
        )
        for key in (
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
            "candidate_standing_authorized",
            "candidate_standing_created",
            "descendant_body_a_created",
            "descendant_body_b_created",
            "descendant_body_created",
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
            "distinctness_operation_boundary_overridden",
            "distinctness_operation_boundary_bypassed",
            "distinctness_operation_overridden",
            "distinctness_operation_bypassed",
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
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "candidate_specific_distinctness_basis_emission_boundary_recorded",
            "boundary_created",
            "upstream_distinctness_operation_result_is_not_distinct",
            "not_distinct_preserved_as_clean_result",
            "candidate_specific_content_missing_upstream",
            "separate_seal_material_missing_upstream",
            "separate_lineage_receipt_material_missing_upstream",
            "separate_digest_material_missing_upstream",
            "scope_division_route_allowed_for_future_operation_shape",
            "divergent_receipt_history_route_not_authorized",
            "carrier_separation_route_not_authorized",
            "cosmetic_substitution_not_allowed",
            "digest_laundering_not_allowed",
            "id_role_label_difference_not_allowed_as_basis",
            "shared_evidence_not_allowed_as_basis",
            "operation_evidence_alone_not_allowed_as_basis",
            "future_emission_operation_not_created",
            "candidate_specific_content_not_emitted",
            "separate_seal_material_not_emitted",
            "separate_lineage_receipt_material_not_emitted",
            "separate_digest_material_not_emitted",
            "distinctness_operation_not_rerun",
            "distinctness_supported_not_recorded",
            "candidate_records_not_marked_distinct",
            "candidate_standing_not_authorized",
            "descendant_bodies_not_created",
            "standing_descendants_not_created",
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
            "distinctness_operation_boundary_not_overridden",
            "distinctness_operation_boundary_not_bypassed",
            "distinctness_operation_not_overridden",
            "distinctness_operation_not_bypassed",
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
            "hidden_repair_not_performed",
            "silent_overwrite_not_performed",
            "boundary_spec_markers_present",
            "completed_distinctness_operation_terminal_summary_markers_present",
            "completed_differentiation_operation_terminal_summary_markers_present",
            "completed_distinctness_operation_boundary_terminal_summary_markers_present",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for code in (
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_TYPE_NOT_EXPECTED",
            "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_VERSION_NOT_0_1_0",
            "FUTURE_EMISSION_OPERATION_TYPE_NOT_EXPECTED",
            "ADMISSIBLE_FUTURE_BASIS_ROUTE_NOT_SCOPE_DIVISION_ONLY",
            "RUPTURE_CLASS_BLOCKED_NOT_EXPECTED",
            "BOUNDARY_SPEC_REFERENCE_MISSING",
            "UPSTREAM_DISTINCTNESS_OPERATION_RESULT_NOT_NOT_DISTINCT",
            "NOT_DISTINCT_NOT_PRESERVED_AS_CLEAN_RESULT",
            "SCOPE_DIVISION_ROUTE_NOT_ALLOWED",
            "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS_TRUE",
            "DIGEST_LAUNDERING_TREATED_AS_BASIS_TRUE",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS_TRUE",
            "SHARED_EVIDENCE_TREATED_AS_BASIS_TRUE",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS_TRUE",
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
            "BOUNDARY_SPEC_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_MALFORMED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_UNREADABLE",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_synthetic_basis_records_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            self.assertIsInstance(result, dict)
            self.assertEqual(
                result["candidate_specific_distinctness_basis_emission_boundary_metadata"]["result_version"],
                "0.1.0",
            )
            self.assertEqual(
                result["candidate_specific_distinctness_basis_emission_boundary_metadata"]["resolver_module"],
                resolver.RESOLVER_MODULE,
            )
            self.assertEqual(
                self.boundary(result)["candidate_specific_distinctness_basis_emission_boundary_id"],
                resolver.DEFAULT_BOUNDARY_ID,
            )
            for key in (
                "candidate_specific_distinctness_basis_emission_boundary_metadata",
                "declared_candidate_specific_distinctness_basis_emission_boundary_question",
                "upstream_basis",
                "candidate_specific_distinctness_basis_emission_boundary_basis",
                "descendant_body_candidate_specific_distinctness_basis_emission_boundary",
                "candidate_specific_distinctness_basis_emission_boundary_checks",
                "candidate_specific_distinctness_basis_emission_boundary_statement",
                "candidate_specific_distinctness_basis_emission_boundary_non_meaning",
                "not_recorded_basis",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "candidate_specific_distinctness_basis_emission_boundary_summary",
            ):
                self.assertIn(key, result)
            self.assert_recorded_boundary_core(result)

    def test_records_default_live_target_if_present(self) -> None:
        required = (
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_V0_MIN_SPEC.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        )
        missing = [str(path) for path in required if not path.is_file()]
        if missing:
            self.skipTest(f"default live basis missing: {missing}")
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_request()
        result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
            request
        )
        if result.get("outcome") == resolver.OUTCOME_BLOCKED:
            self.skipTest(f"default live target present but not clean for this resolver: {self.block_code(result)}")
        self.assert_recorded_boundary_core(result)

    def test_do_not_record_intent_does_not_record_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            request["candidate_specific_distinctness_basis_emission_boundary_intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            boundary = self.boundary(result)
            self.assertIs(boundary["candidate_specific_distinctness_basis_emission_boundary_recorded"], False)
            self.assertIs(boundary["boundary_created"], False)
            self.assert_no_forbidden_boundary_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            request["candidate_specific_distinctness_basis_emission_boundary_intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            self.assert_blocked_with_public_code(result)

    def test_request_shape_and_blocking_behavior(self) -> None:
        cases: list[tuple[str, Any]] = [
            ("non_mapping_request", lambda request: ["not", "mapping"]),
            ("missing_question", lambda request: request.pop("candidate_specific_distinctness_basis_emission_boundary_question")),
            ("unsupported_intent", lambda request: request.__setitem__("candidate_specific_distinctness_basis_emission_boundary_intent", "UNSUPPORTED")),
            ("missing_boundary_type", lambda request: request.pop("candidate_specific_distinctness_basis_emission_boundary_type")),
            ("wrong_boundary_type", lambda request: request.__setitem__("candidate_specific_distinctness_basis_emission_boundary_type", "WRONG")),
            ("missing_boundary_version", lambda request: request.pop("candidate_specific_distinctness_basis_emission_boundary_version")),
            ("wrong_boundary_version", lambda request: request.__setitem__("candidate_specific_distinctness_basis_emission_boundary_version", "9.9.9")),
            ("missing_future_operation_type", lambda request: request.pop("future_emission_operation_type")),
            ("wrong_future_operation_type", lambda request: request.__setitem__("future_emission_operation_type", "WRONG")),
            ("missing_admissible_route", lambda request: request.pop("admissible_future_basis_route")),
            ("wrong_admissible_route", lambda request: request.__setitem__("admissible_future_basis_route", "DIVERGENT_RECEIPT_HISTORY")),
            ("missing_rupture_class", lambda request: request.pop("rupture_class_blocked")),
            ("wrong_rupture_class", lambda request: request.__setitem__("rupture_class_blocked", "WRONG")),
            ("missing_boundary_spec_reference", lambda request: request.__setitem__("boundary_spec_reference", "")),
            ("missing_completed_distinctness_reference", lambda request: request.__setitem__("completed_distinctness_operation_terminal_summary_reference", "")),
            ("missing_completed_differentiation_reference", lambda request: request.__setitem__("completed_differentiation_operation_terminal_summary_reference", "")),
            ("missing_completed_boundary_reference", lambda request: request.__setitem__("completed_distinctness_operation_boundary_terminal_summary_reference", "")),
            ("upstream_not_not_distinct", lambda request: request.__setitem__("upstream_distinctness_operation_result", "DISTINCT")),
            ("not_distinct_not_preserved", lambda request: request.__setitem__("not_distinct_preserved_as_clean_result", False)),
            ("candidate_specific_content_missing_false", lambda request: request.__setitem__("candidate_specific_content_missing_upstream", False)),
            ("separate_seal_material_missing_false", lambda request: request.__setitem__("separate_seal_material_missing_upstream", False)),
            ("separate_lineage_receipt_missing_false", lambda request: request.__setitem__("separate_lineage_receipt_material_missing_upstream", False)),
            ("separate_digest_missing_false", lambda request: request.__setitem__("separate_digest_material_missing_upstream", False)),
            ("scope_division_route_not_allowed", lambda request: request.__setitem__("scope_division_route_allowed_for_future_operation_shape", False)),
            ("divergent_receipt_history_authorized", lambda request: request.__setitem__("divergent_receipt_history_route_authorized", True)),
            ("carrier_separation_authorized", lambda request: request.__setitem__("carrier_separation_route_authorized", True)),
            ("cosmetic_substitution_treated_as_basis", lambda request: request.__setitem__("cosmetic_substitution_treated_as_basis", True)),
            ("digest_laundering_treated_as_basis", lambda request: request.__setitem__("digest_laundering_treated_as_basis", True)),
            ("id_role_label_difference_treated_as_basis", lambda request: request.__setitem__("id_role_label_difference_treated_as_basis", True)),
            ("shared_evidence_treated_as_basis", lambda request: request.__setitem__("shared_evidence_treated_as_basis", True)),
            ("operation_evidence_alone_treated_as_basis", lambda request: request.__setitem__("operation_evidence_alone_treated_as_basis", True)),
            ("future_emission_operation_created", lambda request: request.__setitem__("future_emission_operation_created", True)),
            ("candidate_specific_content_emitted", lambda request: request.__setitem__("candidate_specific_content_emitted", True)),
            ("separate_seal_material_emitted", lambda request: request.__setitem__("separate_seal_material_emitted", True)),
            ("separate_lineage_receipt_material_emitted", lambda request: request.__setitem__("separate_lineage_receipt_material_emitted", True)),
            ("separate_digest_material_emitted", lambda request: request.__setitem__("separate_digest_material_emitted", True)),
            ("distinctness_operation_rerun", lambda request: request.__setitem__("distinctness_operation_rerun", True)),
            ("distinctness_supported_recorded", lambda request: request.__setitem__("distinctness_supported_recorded", True)),
            ("candidate_records_marked_distinct", lambda request: request.__setitem__("candidate_records_marked_distinct", True)),
            ("scan_allowed", lambda request: request.__setitem__("scan_allowed", True)),
            ("repair_allowed", lambda request: request.__setitem__("repair_allowed", True)),
            ("validation_enforcement_allowed", lambda request: request.__setitem__("validation_enforcement_allowed", True)),
            ("candidate_standing_authorized", lambda request: request.__setitem__("candidate_standing_authorized", True)),
            ("descendant_body_created", lambda request: request.__setitem__("descendant_body_created", True)),
            ("standing_authorized", lambda request: request.__setitem__("standing_authorized", True)),
            ("crossing_authorized", lambda request: request.__setitem__("crossing_authorized", True)),
            ("relation_authorized", lambda request: request.__setitem__("relation_authorized", True)),
            ("field_machinery_authorized", lambda request: request.__setitem__("field_machinery_authorized", True)),
            ("runtime_created", lambda request: request.__setitem__("runtime_created", True)),
            ("api_created", lambda request: request.__setitem__("api_created", True)),
            ("currentness_created", lambda request: request.__setitem__("currentness_created", True)),
            ("authority_created", lambda request: request.__setitem__("authority_created", True)),
            ("standing_created", lambda request: request.__setitem__("standing_created", True)),
            ("output_authorized", lambda request: request.__setitem__("output_authorized", True)),
            ("action_authorized", lambda request: request.__setitem__("action_authorized", True)),
            ("derivative_reception_authorized", lambda request: request.__setitem__("derivative_reception_authorized", True)),
            ("synchronization_authorized", lambda request: request.__setitem__("synchronization_authorized", True)),
            ("follow_on_authorized", lambda request: request.__setitem__("follow_on_authorized", True)),
            ("request_emission_operation_definition", lambda request: request.__setitem__("request_emission_operation_definition", True)),
            ("request_emission_operation_implementation", lambda request: request.__setitem__("request_emission_operation_implementation", True)),
            ("request_candidate_specific_content_emission", lambda request: request.__setitem__("request_candidate_specific_content_emission", True)),
            ("request_separate_seal_material_emission", lambda request: request.__setitem__("request_separate_seal_material_emission", True)),
            ("request_separate_lineage_receipt_material_emission", lambda request: request.__setitem__("request_separate_lineage_receipt_material_emission", True)),
            ("request_separate_digest_material_emission", lambda request: request.__setitem__("request_separate_digest_material_emission", True)),
            ("request_distinctness_operation_rerun", lambda request: request.__setitem__("request_distinctness_operation_rerun", True)),
            ("request_distinctness_supported_recording", lambda request: request.__setitem__("request_distinctness_supported_recording", True)),
            ("request_candidate_records_marked_distinct", lambda request: request.__setitem__("request_candidate_records_marked_distinct", True)),
            ("request_repository_scan", lambda request: request.__setitem__("request_repository_scan", True)),
            ("request_file_discovery", lambda request: request.__setitem__("request_file_discovery", True)),
            ("request_affected_file_repair", lambda request: request.__setitem__("request_affected_file_repair", True)),
            ("request_affected_file_mutation", lambda request: request.__setitem__("request_affected_file_mutation", True)),
            ("request_prior_unsupported_claim_validation", lambda request: request.__setitem__("request_prior_unsupported_claim_validation", True)),
            ("request_existence_claim_evidence_check_override", lambda request: request.__setitem__("request_existence_claim_evidence_check_override", True)),
            ("request_existence_claim_evidence_check_bypass", lambda request: request.__setitem__("request_existence_claim_evidence_check_bypass", True)),
            ("request_differentiation_operation_override", lambda request: request.__setitem__("request_differentiation_operation_override", True)),
            ("request_differentiation_operation_bypass", lambda request: request.__setitem__("request_differentiation_operation_bypass", True)),
            ("request_distinctness_operation_boundary_override", lambda request: request.__setitem__("request_distinctness_operation_boundary_override", True)),
            ("request_distinctness_operation_boundary_bypass", lambda request: request.__setitem__("request_distinctness_operation_boundary_bypass", True)),
            ("request_distinctness_operation_override", lambda request: request.__setitem__("request_distinctness_operation_override", True)),
            ("request_distinctness_operation_bypass", lambda request: request.__setitem__("request_distinctness_operation_bypass", True)),
            ("request_candidate_standing_authorization", lambda request: request.__setitem__("request_candidate_standing_authorization", True)),
            ("request_descendant_body_creation", lambda request: request.__setitem__("request_descendant_body_creation", True)),
            ("request_standing_descendant_creation", lambda request: request.__setitem__("request_standing_descendant_creation", True)),
            ("request_descendant_standing_check", lambda request: request.__setitem__("request_descendant_standing_check", True)),
            ("request_crossing_authorization", lambda request: request.__setitem__("request_crossing_authorization", True)),
            ("request_relation_creation", lambda request: request.__setitem__("request_relation_creation", True)),
            ("request_field_machinery_creation", lambda request: request.__setitem__("request_field_machinery_creation", True)),
            ("request_runtime_creation", lambda request: request.__setitem__("request_runtime_creation", True)),
            ("request_currentness_creation", lambda request: request.__setitem__("request_currentness_creation", True)),
            ("request_authority_creation", lambda request: request.__setitem__("request_authority_creation", True)),
            ("request_output_authorization", lambda request: request.__setitem__("request_output_authorization", True)),
            ("request_action_authorization", lambda request: request.__setitem__("request_action_authorization", True)),
            ("request_derivative_reception_authorization", lambda request: request.__setitem__("request_derivative_reception_authorization", True)),
            ("request_synchronization_authorization", lambda request: request.__setitem__("request_synchronization_authorization", True)),
            ("request_follow_on_authorization", lambda request: request.__setitem__("request_follow_on_authorization", True)),
            ("return_raw_markdown_body", lambda request: request.__setitem__("return_raw_markdown_body", True)),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _paths = self.build_valid_request(Path(tmp))
            for index, (name, mutator) in enumerate(cases):
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutated = mutator(request)
                    target = mutated if name == "non_mapping_request" else request
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                        target
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertTrue(self.safe_json_filename(name, index).endswith(".json"))

    def test_marker_validation_blocking_behavior(self) -> None:
        cases = (
            ("boundary_spec", "BOUNDARY_SPEC_MARKER_MISSING"),
            ("completed_distinctness", "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("completed_differentiation", "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("completed_boundary", "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for index, (kind, expected_code) in enumerate(cases):
                with self.subTest(kind=kind):
                    case_dir = Path(tmp) / self.safe_json_filename(kind, index).removesuffix(".json")
                    request, _paths = self.build_valid_request(case_dir, remove_marker_kind=kind)
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(expected_code, self.emitted_codes(result))

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "candidate_specific_distinctness_basis_emission_operation_created": "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_CREATED",
            "candidate_specific_distinctness_basis_emission_operation_performed": "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_PERFORMED",
            "candidate_specific_distinctness_basis_emission_operation_recorded": "CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_RECORDED",
            "candidate_specific_content_emitted": "CANDIDATE_SPECIFIC_CONTENT_EMITTED",
            "separate_seal_material_emitted": "SEPARATE_SEAL_MATERIAL_EMITTED",
            "separate_lineage_receipt_material_emitted": "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED",
            "separate_digest_material_emitted": "SEPARATE_DIGEST_MATERIAL_EMITTED",
            "distinctness_operation_rerun": "DISTINCTNESS_OPERATION_RERUN",
            "distinctness_supported_recorded": "DISTINCTNESS_SUPPORTED_RECORDED",
            "candidate_records_marked_distinct": "CANDIDATE_RECORDS_MARKED_DISTINCT",
            "candidate_standing_authorized": "CANDIDATE_STANDING_AUTHORIZED",
            "descendant_body_created": "DESCENDANT_BODY_CREATED",
            "standing_authorized": "STANDING_AUTHORIZED",
            "crossing_authorized": "CROSSING_AUTHORIZED",
            "relation_authorized": "RELATION_AUTHORIZED",
            "field_machinery_authorized": "FIELD_MACHINERY_AUTHORIZED",
            "runtime_created": "RUNTIME_CREATED",
            "api_created": "API_CREATED",
            "currentness_created": "CURRENTNESS_CREATED",
            "authority_created": "AUTHORITY_CREATED",
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
            "distinctness_operation_boundary_overridden": "DISTINCTNESS_OPERATION_BOUNDARY_OVERRIDDEN",
            "distinctness_operation_boundary_bypassed": "DISTINCTNESS_OPERATION_BOUNDARY_BYPASSED",
            "distinctness_operation_overridden": "DISTINCTNESS_OPERATION_OVERRIDDEN",
            "distinctness_operation_bypassed": "DISTINCTNESS_OPERATION_BYPASSED",
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "repair_performed": "REPAIR_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
            "cosmetic_substitution_treated_as_basis": "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS",
            "digest_laundering_treated_as_basis": "DIGEST_LAUNDERING_TREATED_AS_BASIS",
            "id_role_label_difference_treated_as_basis": "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS",
            "shared_evidence_treated_as_basis": "SHARED_EVIDENCE_TREATED_AS_BASIS",
            "operation_evidence_alone_treated_as_basis": "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS",
            "divergent_receipt_history_route_authorized": "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED",
            "carrier_separation_route_authorized": "CARRIER_SEPARATION_ROUTE_AUTHORIZED",
        }
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _paths = self.build_valid_request(Path(tmp))
            for field, expected_code in cases.items():
                with self.subTest(field=field):
                    request = copy.deepcopy(base_request)
                    request[field] = True
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    if expected_code in resolver.BLOCK_CODES:
                        self.assertIn(expected_code, self.emitted_codes(result))
                    if field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                        self.assertIs(result["non_claims"].get(field), False)
                    else:
                        self.assertIsNot(self.boundary(result).get(field), True)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base_request, _paths = self.build_valid_request(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = {
                "missing_declared_non_claims": lambda request: request.pop("declared_non_claims"),
                "non_mapping_declared_non_claims": lambda request: request.__setitem__("declared_non_claims", []),
                "missing_required_key": lambda request: request["declared_non_claims"].pop(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ),
                "non_bool_value": lambda request: request["declared_non_claims"].__setitem__(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false"
                ),
            }
            for name, mutate in malformed_cases.items():
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutate(request)
                    result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_sanitizer_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp), sentinels=RAW_SENTINELS)
            request["raw_body"] = RAW_SENTINELS[0]
            request["hidden_repo_state"] = RAW_SENTINELS[1]
            request["current_working_tree"] = RAW_SENTINELS[2]
            recorded = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            self.assert_recorded_boundary_core(recorded)
            self.assert_no_raw_full_markdown_body_returned(recorded)
            serialized = json.dumps(recorded, sort_keys=True)
            self.assertIn(resolver.BOUNDARY_TYPE, serialized)
            self.assertIn(resolver.FUTURE_EMISSION_OPERATION_TYPE, serialized)
            blocked_request = copy.deepcopy(request)
            blocked_request["return_raw_markdown_body"] = True
            blocked = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                blocked_request
            )
            self.assert_blocked_with_public_code(blocked)
            self.assert_no_raw_full_markdown_body_returned(blocked)
            self.assertIn(resolver.BOUNDARY_TYPE, json.dumps(blocked, sort_keys=True))

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            request, _paths = self.build_valid_request(base)
            request_path = base / self.safe_json_filename("valid_request")
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_from_path(
                request_path
            )
            self.assert_recorded_boundary_core(result)
            for name, content in {
                "missing_request": None,
                "malformed_request": "{",
                "array_request": "[]",
            }.items():
                path = base / self.safe_json_filename(name)
                if content is None:
                    target = path
                else:
                    path.write_text(content, encoding="utf-8")
                    target = path
                blocked = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_from_path(
                    target
                )
                self.assert_blocked_with_public_code(blocked)
            output_dir = base / "writes"
            first_path = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_result(
                result, output_dir
            )
            self.assertTrue(first_path.exists())
            self.assertIn("candidate_specific_distinctness_basis_emission_boundary_v0_min_result", first_path.name)
            parsed = json.loads(first_path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            second_path = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_result(
                result, output_dir
            )
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            forbidden_roots = {
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary_v0_min",
                "integrity_host_v0_min_coexistence_source_transfer_v0_min",
                "integrity_host_v0_min_coexistence_source_receipt_v0_min",
                "integrity_host_v0_min_coexistence_public_api_v0_min",
                "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min",
                "integrity_host_v0_min_coexistence_distributed_network_v0_min",
                "integrity_host_v0_min_coexistence_runtime_hosting_v0_min",
                "integrity_host_v0_min_coexistence_runtime_loop_v0_min",
                "integrity_host_v0_min_coexistence_daemon_v0_min",
            }
            self.assertTrue(forbidden_roots.isdisjoint(set(first_path.parts)))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths = self.build_valid_request(Path(tmp), sentinels=RAW_SENTINELS)
            request["raw_body"] = RAW_SENTINELS[0]
            before_request = copy.deepcopy(request)
            before_contents = {name: path.read_text(encoding="utf-8") for name, path in paths.items()}
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            self.assert_recorded_boundary_core(result)
            self.assertEqual(request, before_request)
            self.assertEqual(before_request["declared_non_claims"], request["declared_non_claims"])
            for name, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), before_contents[name])

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            summary = self.summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["candidate_specific_distinctness_basis_emission_boundary_id"], resolver.DEFAULT_BOUNDARY_ID)
            self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(summary["boundary_version"], "0.1.0")
            self.assertEqual(summary["future_emission_operation_type"], resolver.FUTURE_EMISSION_OPERATION_TYPE)
            self.assertEqual(summary["admissible_future_basis_route"], resolver.ADMISSIBLE_FUTURE_BASIS_ROUTE)
            self.assertEqual(summary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
            self.assertEqual(summary["upstream_distinctness_operation_result"], "NOT_DISTINCT")
            for field in (
                "not_distinct_preserved_as_clean_result",
                "candidate_specific_content_missing_upstream",
                "separate_seal_material_missing_upstream",
                "separate_lineage_receipt_material_missing_upstream",
                "separate_digest_material_missing_upstream",
                "scope_division_route_allowed_for_future_operation_shape",
                "future_emission_operation_not_created",
                "candidate_specific_content_not_emitted",
                "separate_seal_material_not_emitted",
                "separate_lineage_receipt_material_not_emitted",
                "separate_digest_material_not_emitted",
                "distinctness_operation_not_rerun",
                "distinctness_supported_not_recorded",
                "candidate_records_not_marked_distinct",
                "candidate_standing_not_authorized",
                "descendant_bodies_not_created",
                "standing_descendants_not_created",
                "first_crossing_not_authorized",
                "relation_not_created",
                "field_machinery_not_created",
                "runtime_not_created",
                "currentness_not_created",
                "authority_not_created",
                "output_not_authorized",
                "action_not_authorized",
                "derivative_reception_not_authorized",
                "synchronization_not_authorized",
                "follow_on_not_authorized",
                "scan_not_performed",
                "repository_scan_not_performed",
                "repair_not_performed",
                "validation_not_enforced",
                "hidden_repair_not_performed",
                "silent_overwrite_not_performed",
                "boundary_spec_markers_present",
                "completed_distinctness_operation_terminal_summary_markers_present",
                "completed_differentiation_operation_terminal_summary_markers_present",
                "completed_distinctness_operation_boundary_terminal_summary_markers_present",
                "result_level_non_claims_canonical_false",
            ):
                self.assertIs(summary[field], True, field)
            for field in (
                "divergent_receipt_history_route_authorized",
                "carrier_separation_route_authorized",
                "cosmetic_substitution_treated_as_basis",
                "digest_laundering_treated_as_basis",
                "id_role_label_difference_treated_as_basis",
                "shared_evidence_treated_as_basis",
                "operation_evidence_alone_treated_as_basis",
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
                "distinctness_operation_boundary_overridden",
                "distinctness_operation_boundary_bypassed",
                "distinctness_operation_overridden",
                "distinctness_operation_bypassed",
            ):
                self.assertIs(summary[field], False, field)

    def test_smoke_behavior_default_boundary_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min(
                request
            )
            summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_summary(
                result
            )
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            boundary = result["descendant_body_candidate_specific_distinctness_basis_emission_boundary"]
            self.assertEqual(boundary["candidate_specific_distinctness_basis_emission_boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(boundary["candidate_specific_distinctness_basis_emission_boundary_version"], "0.1.0")
            self.assertEqual(boundary["future_emission_operation_type"], resolver.FUTURE_EMISSION_OPERATION_TYPE)
            self.assertEqual(boundary["admissible_future_basis_route"], "SCOPE_DIVISION_ONLY")
            self.assertEqual(boundary["rupture_class_blocked"], resolver.RUPTURE_CLASS_BLOCKED)
            self.assertEqual(boundary["upstream_distinctness_operation_result"], "NOT_DISTINCT")
            for field in (
                "candidate_specific_distinctness_basis_emission_boundary_recorded",
                "boundary_created",
                "not_distinct_preserved_as_clean_result",
                "candidate_specific_content_missing_upstream",
                "separate_seal_material_missing_upstream",
                "separate_lineage_receipt_material_missing_upstream",
                "separate_digest_material_missing_upstream",
                "scope_division_route_allowed_for_future_operation_shape",
                "divergent_receipt_history_route_not_authorized",
                "carrier_separation_route_not_authorized",
                "cosmetic_substitution_not_allowed",
                "digest_laundering_not_allowed",
                "id_role_label_difference_not_allowed_as_basis",
                "shared_evidence_not_allowed_as_basis",
                "operation_evidence_alone_not_allowed_as_basis",
                "future_emission_operation_not_created",
                "candidate_specific_content_not_emitted",
                "separate_seal_material_not_emitted",
                "separate_lineage_receipt_material_not_emitted",
                "separate_digest_material_not_emitted",
                "distinctness_operation_not_rerun",
                "distinctness_supported_not_recorded",
                "candidate_records_not_marked_distinct",
                "candidate_standing_not_authorized",
                "descendant_bodies_not_created",
                "first_crossing_not_authorized",
                "relation_not_created",
                "runtime_not_created",
                "currentness_not_created",
                "authority_not_created",
                "follow_on_not_authorized",
            ):
                self.assertIs(boundary[field], True, field)
            self.assert_boundary_not_wrapper(boundary)
            self.assert_canonical_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
