"""Tests for the v2 candidate-specific distinctness basis emission boundary.

V1 remains preserved lineage: its synthetic posture stood, while the default
live target skipped on brittle completed-differentiation marker acceptance.
This v2 suite verifies the successor resolver accepts equivalent completed
differentiation terminal-summary posture without authorizing emission,
standing, descendant bodies, crossing, relation, runtime, authority, repair,
scan, validation enforcement, raw Markdown return, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2 as resolver


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

DISTINCTNESS_BOUNDARY_MARKERS = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_BOUNDARY_RECORDED",
    "enumeration is not distinction",
    "id and role difference alone are not distinctness",
    "shared evidence reference alone is not distinctness",
    "distinctness support requires separate candidate-specific evidence",
    "candidate standing is not authorized",
)

ACCEPTED_DIFFERENTIATION_VARIANTS = {
    "exact_original_style": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "operation result emitted",
        "exactly two result-contained non-standing candidate records",
        "candidate records are operation-evidenced",
        "candidate records are not descendant bodies",
        "candidate records remain non-standing",
        "standing descendants not created",
        "first crossing not authorized",
        "relation not created",
    ),
    "key_value_equivalent": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
        "operation_result_created = true",
        "candidate_record_count_emitted = 2",
        "exactly_two_candidate_records_emitted = true",
        "candidate_records_have_operation_evidence = true",
        "candidate_records_non_standing = true",
        "descendant_body_a_created = false",
        "descendant_body_b_created = false",
        "standing_descendant_created = false",
        "first_crossing_authorized = false",
        "relation_created = false",
    ),
    "repo_native_prose_equivalent": (
        "completed descendant-body differentiation operation line",
        "completed operation result",
        "emitted exactly two result-contained non-standing candidate records",
        "candidate records are result-contained",
        "candidate records are operation-evidenced",
        "candidate records are non-standing",
        "candidate records are not descendant bodies",
        "descendant bodies not created",
        "standing descendants not created",
        "first crossing not authorized",
        "relation not created",
    ),
}

REJECTED_DIFFERENTIATION_VARIANTS = {
    "only_word_differentiation": ("differentiation",),
    "only_word_candidate": ("candidate",),
    "id_role_only_without_non_standing": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
        "operation_result_created = true",
        "candidate ids and roles were enumerated",
        "candidate id and role labels differ",
    ),
    "operation_outcome_without_non_standing": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "operation result emitted",
        "candidate_record_count_emitted = 2",
        "candidate_records_have_operation_evidence = true",
        "candidate records are not descendant bodies",
        "standing descendants not created",
        "first crossing not authorized",
        "relation not created",
    ),
    "non_standing_without_exactly_two": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "operation result emitted",
        "candidate_records_have_operation_evidence = true",
        "candidate_records_non_standing = true",
        "candidate records are not descendant bodies",
        "standing descendants not created",
        "first crossing not authorized",
        "relation not created",
    ),
    "exactly_two_without_not_descendant_body": (
        "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
        "operation result emitted",
        "candidate_record_count_emitted = 2",
        "candidate_records_have_operation_evidence = true",
        "candidate_records_non_standing = true",
        "standing_descendant_created = false",
        "first_crossing_authorized = false",
        "relation_created = false",
    ),
    "crossing_authorized": ACCEPTED_DIFFERENTIATION_VARIANTS["key_value_equivalent"]
    + ("first_crossing_authorized = true",),
    "relation_created": ACCEPTED_DIFFERENTIATION_VARIANTS["key_value_equivalent"] + ("relation_created = true",),
    "descendant_bodies_created": ACCEPTED_DIFFERENTIATION_VARIANTS["key_value_equivalent"]
    + ("descendant_body_created = true",),
    "standing_descendants_created": ACCEPTED_DIFFERENTIATION_VARIANTS["key_value_equivalent"]
    + ("standing_descendant_created = true",),
}

RAW_SENTINELS = (
    "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
    "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
)

WRAPPER_KEYS = (
    "outcome",
    "block",
    "candidate_specific_distinctness_basis_emission_boundary_checks",
    "non_claims",
    "candidate_specific_distinctness_basis_emission_boundary_summary",
    "candidate_specific_distinctness_basis_emission_boundary_metadata",
)

REQUIRED_TOP_LEVEL_SECTIONS = (
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
)


class CandidateSpecificDistinctnessBasisEmissionBoundaryV2Tests(unittest.TestCase):
    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, lines: tuple[str, ...], extra: tuple[str, ...] = ()) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines + extra) + "\n", encoding="utf-8")
        return path

    def basis_paths(
        self,
        base: Path,
        *,
        differentiation_lines: tuple[str, ...] = ACCEPTED_DIFFERENTIATION_VARIANTS["exact_original_style"],
        boundary_spec_lines: tuple[str, ...] = BOUNDARY_SPEC_MARKERS,
        distinctness_operation_lines: tuple[str, ...] = DISTINCTNESS_OPERATION_MARKERS,
        distinctness_boundary_lines: tuple[str, ...] = DISTINCTNESS_BOUNDARY_MARKERS,
        sentinels: tuple[str, ...] = (),
    ) -> dict[str, Path]:
        extra = tuple(f"non-authoritative note: {sentinel}" for sentinel in sentinels)
        basis = base / "synthetic_basis"
        return {
            "boundary_spec": self.write_markdown(
                basis / "candidate_specific_distinctness_basis_emission_boundary_spec.md",
                boundary_spec_lines,
                extra,
            ),
            "completed_distinctness": self.write_markdown(
                basis / "candidate_record_distinctness_operation_terminal_summary.md",
                distinctness_operation_lines,
                extra,
            ),
            "completed_differentiation": self.write_markdown(
                basis / "descendant_body_differentiation_operation_terminal_summary.md",
                differentiation_lines,
                extra,
            ),
            "completed_boundary": self.write_markdown(
                basis / "candidate_record_distinctness_operation_boundary_terminal_summary.md",
                distinctness_boundary_lines,
                extra,
            ),
        }

    def build_valid_request(
        self,
        base: Path,
        *,
        differentiation_lines: tuple[str, ...] = ACCEPTED_DIFFERENTIATION_VARIANTS["exact_original_style"],
        boundary_spec_lines: tuple[str, ...] = BOUNDARY_SPEC_MARKERS,
        distinctness_operation_lines: tuple[str, ...] = DISTINCTNESS_OPERATION_MARKERS,
        distinctness_boundary_lines: tuple[str, ...] = DISTINCTNESS_BOUNDARY_MARKERS,
        sentinels: tuple[str, ...] = (),
    ) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = self.basis_paths(
            base,
            differentiation_lines=differentiation_lines,
            boundary_spec_lines=boundary_spec_lines,
            distinctness_operation_lines=distinctness_operation_lines,
            distinctness_boundary_lines=distinctness_boundary_lines,
            sentinels=sentinels,
        )
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_request(
            boundary_spec_reference=str(paths["boundary_spec"]),
            completed_distinctness_operation_terminal_summary_reference=str(paths["completed_distinctness"]),
            completed_differentiation_operation_terminal_summary_reference=str(paths["completed_differentiation"]),
            completed_distinctness_operation_boundary_terminal_summary_reference=str(paths["completed_boundary"]),
        )
        return request, paths

    def resolve(self, request: Any) -> dict[str, Any]:
        return resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2(
            request
        )

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        boundary = result.get("descendant_body_candidate_specific_distinctness_basis_emission_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        summary = resolver.build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_summary(
            result
        )
        self.assertIsInstance(summary, dict)
        return summary

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
        code = self.block_code(result)
        if code:
            codes.add(str(code))
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value:
                    codes.add(str(value))
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
        self.assert_no_forbidden_final_posture(result)

    def assert_canonical_false_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIs(type(non_claims[key]), bool, key)

    def assert_boundary_not_wrapper(self, boundary: dict[str, Any]) -> None:
        for key in WRAPPER_KEYS:
            self.assertNotIn(key, boundary)

    def assert_no_raw_full_markdown_body_returned(self, result: dict[str, Any]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in RAW_SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def assert_no_forbidden_final_posture(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for field in (
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
        ):
            self.assertIs(boundary.get(field), True, field)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsNot(boundary.get(field), True, field)

    def assert_recorded_boundary_core(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_canonical_false_non_claims(result)
        for key in REQUIRED_TOP_LEVEL_SECTIONS:
            self.assertIn(key, result)
        metadata = result["candidate_specific_distinctness_basis_emission_boundary_metadata"]
        self.assertEqual(metadata["result_version"], "0.2.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
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

    def request_case_result(
        self,
        base: Path,
        mutator: Callable[[dict[str, Any]], Any],
    ) -> dict[str, Any]:
        request, _paths = self.build_valid_request(base)
        maybe_request = mutator(request)
        return self.resolve(maybe_request if maybe_request is not None else request)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2",
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_from_path",
            "write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result",
            "build_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_summary",
            "build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_request",
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
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2",
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
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_RECORDED",
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_BLOCKED",
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_NOT_RECORDED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2"
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
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for key in (
            "candidate_specific_distinctness_basis_emission_boundary_recorded",
            "boundary_created",
            "upstream_distinctness_operation_result_is_not_distinct",
            "not_distinct_preserved_as_clean_result",
            "scope_division_route_allowed_for_future_operation_shape",
            "future_emission_operation_not_created",
            "completed_differentiation_operation_terminal_summary_markers_present",
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
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "UPSTREAM_DISTINCTNESS_OPERATION_RESULT_NOT_NOT_DISTINCT",
            "NOT_DISTINCT_NOT_PRESERVED_AS_CLEAN_RESULT",
            "CANDIDATE_SPECIFIC_CONTENT_MISSING_UPSTREAM_NOT_TRUE",
            "SEPARATE_SEAL_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
            "SEPARATE_DIGEST_MATERIAL_MISSING_UPSTREAM_NOT_TRUE",
            "SCOPE_DIVISION_ROUTE_NOT_ALLOWED",
            "DIVERGENT_RECEIPT_HISTORY_ROUTE_AUTHORIZED_TRUE",
            "CARRIER_SEPARATION_ROUTE_AUTHORIZED_TRUE",
            "COSMETIC_SUBSTITUTION_TREATED_AS_BASIS_TRUE",
            "DIGEST_LAUNDERING_TREATED_AS_BASIS_TRUE",
            "ID_ROLE_LABEL_DIFFERENCE_TREATED_AS_BASIS_TRUE",
            "SHARED_EVIDENCE_TREATED_AS_BASIS_TRUE",
            "OPERATION_EVIDENCE_ALONE_TREATED_AS_BASIS_TRUE",
            "FUTURE_EMISSION_OPERATION_CREATED_TRUE",
            "CANDIDATE_SPECIFIC_CONTENT_EMITTED_TRUE",
            "SEPARATE_SEAL_MATERIAL_EMITTED_TRUE",
            "SEPARATE_LINEAGE_RECEIPT_MATERIAL_EMITTED_TRUE",
            "SEPARATE_DIGEST_MATERIAL_EMITTED_TRUE",
            "DISTINCTNESS_OPERATION_RERUN_TRUE",
            "DISTINCTNESS_SUPPORTED_RECORDED_TRUE",
            "CANDIDATE_RECORDS_MARKED_DISTINCT_TRUE",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            "CANDIDATE_STANDING_AUTHORIZED_TRUE",
            "DESCENDANT_BODY_CREATED_TRUE",
            "CROSSING_AUTHORIZED_TRUE",
            "RELATION_AUTHORIZED_TRUE",
            "FIELD_MACHINERY_AUTHORIZED_TRUE",
            "RUNTIME_CREATED_TRUE",
            "CURRENTNESS_CREATED_TRUE",
            "AUTHORITY_CREATED_TRUE",
            "FOLLOW_ON_AUTHORIZED_TRUE",
            "REQUESTED_EMISSION_OPERATION_DEFINITION",
            "REQUESTED_CANDIDATE_SPECIFIC_CONTENT_EMISSION",
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
            "BOUNDARY_SPEC_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_MALFORMED",
            "DECLARED_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY_REQUEST_UNREADABLE",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_synthetic_basis_records_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = self.resolve(request)
            self.assertIsInstance(result, dict)
            self.assertEqual(
                self.boundary(result)["candidate_specific_distinctness_basis_emission_boundary_id"],
                resolver.DEFAULT_BOUNDARY_ID,
            )
            self.assert_recorded_boundary_core(result)

    def test_v2_accepts_equivalent_differentiation_terminal_summary_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, (name, lines) in enumerate(ACCEPTED_DIFFERENTIATION_VARIANTS.items()):
                with self.subTest(name=name):
                    case_base = base / self.safe_json_filename(name, index).removesuffix(".json")
                    request, _paths = self.build_valid_request(case_base, differentiation_lines=lines)
                    result = self.resolve(request)
                    self.assert_recorded_boundary_core(result)
                    self.assertIs(
                        self.boundary(result)["completed_differentiation_operation_terminal_summary_markers_present"],
                        True,
                    )

    def test_v2_rejects_insufficient_differentiation_terminal_summary_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, (name, lines) in enumerate(REJECTED_DIFFERENTIATION_VARIANTS.items()):
                with self.subTest(name=name):
                    case_base = base / self.safe_json_filename(name, index).removesuffix(".json")
                    request, _paths = self.build_valid_request(case_base, differentiation_lines=lines)
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result),
                        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
                    )

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
        request = resolver.build_declared_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_request()
        result = self.resolve(request)
        self.assert_recorded_boundary_core(result)

    def test_do_not_record_intent_does_not_record_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            request["candidate_specific_distinctness_basis_emission_boundary_intent"] = resolver.INTENT_DO_NOT_RECORD
            result = self.resolve(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            boundary = self.boundary(result)
            self.assertIs(boundary["candidate_specific_distinctness_basis_emission_boundary_recorded"], False)
            self.assertIs(boundary["boundary_created"], False)
            self.assert_no_forbidden_final_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            request["candidate_specific_distinctness_basis_emission_boundary_intent"] = resolver.INTENT_BLOCK
            result = self.resolve(request)
            self.assert_blocked_with_public_code(result)

    def test_request_shape_and_blocking_behavior(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], Any]]] = [
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
            base = Path(tmp)
            for index, (name, mutator) in enumerate(cases):
                with self.subTest(name=name):
                    result = self.request_case_result(base / self.safe_json_filename(name, index).removesuffix(".json"), mutator)
                    self.assert_blocked_with_public_code(result)

    def test_marker_validation_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            marker_cases = (
                (
                    "boundary_spec_marker_removed",
                    {"boundary_spec_lines": tuple(["removed required title"] + list(BOUNDARY_SPEC_MARKERS[1:]))},
                    "BOUNDARY_SPEC_MARKER_MISSING",
                ),
                (
                    "completed_distinctness_marker_removed",
                    {"distinctness_operation_lines": tuple(["removed distinctness outcome"] + list(DISTINCTNESS_OPERATION_MARKERS[1:]))},
                    "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
                ),
                (
                    "completed_boundary_marker_removed",
                    {"distinctness_boundary_lines": tuple(["removed boundary outcome"] + list(DISTINCTNESS_BOUNDARY_MARKERS[1:]))},
                    "COMPLETED_DISTINCTNESS_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
                ),
            )
            for index, (name, kwargs, expected_code) in enumerate(marker_cases):
                with self.subTest(name=name):
                    request, _paths = self.build_valid_request(
                        base / self.safe_json_filename(name, index).removesuffix(".json"),
                        **kwargs,
                    )
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
            for index, (name, lines) in enumerate(REJECTED_DIFFERENTIATION_VARIANTS.items(), start=20):
                with self.subTest(name=name):
                    request, _paths = self.build_valid_request(
                        base / self.safe_json_filename(name, index).removesuffix(".json"),
                        differentiation_lines=lines,
                    )
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(
                        self.block_code(result),
                        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
                    )

    def test_required_false_top_level_posture_blocks(self) -> None:
        representative_fields = (
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
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_authorized",
            "field_machinery_authorized",
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
        )
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, field in enumerate(representative_fields):
                with self.subTest(field=field):
                    request, _paths = self.build_valid_request(base / self.safe_json_filename(field, index).removesuffix(".json"))
                    request[field] = True
                    result = self.resolve(request)
                    self.assert_blocked_with_public_code(result)
                    if field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                        self.assertIs(result["non_claims"].get(field), False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp) / "canonicalization")
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    mutated = copy.deepcopy(request)
                    mutated["declared_non_claims"][key] = True
                    result = self.resolve(mutated)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = (
                ("missing_declared_non_claims", lambda req: req.pop("declared_non_claims")),
                ("non_mapping_declared_non_claims", lambda req: req.__setitem__("declared_non_claims", [])),
                (
                    "missing_required_non_claim",
                    lambda req: req["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0]),
                ),
                (
                    "non_bool_required_non_claim",
                    lambda req: req["declared_non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], "false"),
                ),
            )
            for name, mutator in malformed_cases:
                with self.subTest(name=name):
                    mutated = copy.deepcopy(request)
                    mutator(mutated)
                    result = self.resolve(mutated)
                    self.assert_blocked_with_public_code(result)

    def test_sanitizer_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp) / "recorded", sentinels=RAW_SENTINELS)
            request["raw_markdown_body"] = RAW_SENTINELS[0]
            request["hidden_repo_state"] = RAW_SENTINELS[1]
            request["current_working_tree_snapshot"] = RAW_SENTINELS[2]
            recorded = self.resolve(request)
            self.assert_recorded_boundary_core(recorded)
            self.assert_no_raw_full_markdown_body_returned(recorded)
            blocked_request = copy.deepcopy(request)
            blocked_request["return_raw_markdown_body"] = True
            blocked = self.resolve(blocked_request)
            self.assert_blocked_with_public_code(blocked)
            self.assert_no_raw_full_markdown_body_returned(blocked)
            serialized = json.dumps(recorded, sort_keys=True)
            self.assertIn(resolver.BOUNDARY_TYPE, serialized)
            self.assertIn(resolver.FUTURE_EMISSION_OPERATION_TYPE, serialized)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            request, _paths = self.build_valid_request(base / "path_case")
            request_path = base / "request.json"
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_from_path(
                request_path
            )
            self.assert_recorded_boundary_core(result)
            missing = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_from_path(
                base / "missing.json"
            )
            self.assert_blocked_with_public_code(missing)
            malformed_path = base / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(malformed)
            array_path = base / "array.json"
            array_path.write_text("[]\n", encoding="utf-8")
            array_result = resolver.resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_from_path(
                array_path
            )
            self.assert_blocked_with_public_code(array_result)
            output_root = base / "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2"
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result(
                    result
                )
                second = resolver.write_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result(
                    result
                )
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("candidate_specific_distinctness_basis_emission_boundary_v0_min_v2_result", first.name)
            json.loads(first.read_text(encoding="utf-8"))
            json.loads(second.read_text(encoding="utf-8"))
            forbidden_roots = {
                "integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_boundary_v0_min_v2",
                "integrity_host_v0_min_coexistence_descendant_body_candidate_record_distinctness_operation_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_v0_min",
            }
            self.assertTrue(output_root.name.endswith("_v2"))
            self.assertNotIn(output_root.name, forbidden_roots)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, paths = self.build_valid_request(Path(tmp) / "non_mutation", sentinels=RAW_SENTINELS)
            request["raw_markdown_body"] = RAW_SENTINELS[0]
            before_request = copy.deepcopy(request)
            before_contents = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = self.resolve(request)
            self.assert_recorded_boundary_core(result)
            self.assertEqual(request, before_request)
            after_contents = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            self.assertEqual(after_contents, before_contents)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = self.resolve(request)
            self.assert_recorded_boundary_core(result)
            summary = self.summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.2.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            for field in (
                "candidate_specific_distinctness_basis_emission_boundary_id",
                "boundary_type",
                "boundary_version",
                "future_emission_operation_type",
                "admissible_future_basis_route",
                "rupture_class_blocked",
                "upstream_distinctness_operation_result",
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
                "api_not_created",
                "currentness_not_created",
                "authority_not_created",
                "standing_not_created",
                "output_not_authorized",
                "action_not_authorized",
                "derivative_reception_not_authorized",
                "synchronization_not_authorized",
                "follow_on_not_authorized",
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
                self.assertIn(field, summary)
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            self.assertIs(summary["prior_unsupported_claims_validated"], False)

    def test_smoke_behavior_default_boundary_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request, _paths = self.build_valid_request(Path(tmp))
            result = self.resolve(request)
            summary = self.summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.2.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_descendant_body_candidate_specific_distinctness_basis_emission_boundary_v0_min_v2",
            )
            boundary = self.boundary(result)
            self.assertEqual(
                boundary["candidate_specific_distinctness_basis_emission_boundary_type"],
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_BOUNDARY",
            )
            self.assertEqual(boundary["candidate_specific_distinctness_basis_emission_boundary_version"], "0.1.0")
            self.assertEqual(
                boundary["future_emission_operation_type"],
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION",
            )
            self.assertEqual(boundary["admissible_future_basis_route"], "SCOPE_DIVISION_ONLY")
            self.assertEqual(
                boundary["rupture_class_blocked"],
                "COSMETIC_DIFFERENCE_CRYPTOGRAPHICALLY_DRESSED_AS_DISTINCTNESS",
            )
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
