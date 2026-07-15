"""Tests for the existence-claim evidence requirement boundary resolver.

This suite exercises one boundary resolver only. It verifies declared Markdown
basis-file reading, required marker validation, boundary-object/result-wrapper
separation, canonical false non-claims, raw Markdown body containment, and
blocking for checker, scan, validation, repair, descendant-body, derivation,
standing, relation, runtime, authority, currentness, and follow-on overreach.
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
sys.path.insert(0, str(SRC_ROOT))

import resolve_existence_claim_evidence_requirement_boundary_v0_min as resolver


AFFECTED_MARKERS = {
    "candidate_a": "descendant_body_basis_candidate_a_created = true",
    "candidate_b": "descendant_body_basis_candidate_b_created = true",
    "derivation_recorded": "descendant_body_basis_derivation_event_recorded = true",
}

SEAM_MARKERS = {
    "unsupported_class": "contaminated for the unsupported existence-claim class",
    "repo_not_standing": "Repo presence is not standing",
    "codex_not_truth": "Codex execution is not truth",
    "operator_not_sole": "Operator authorization is not sole authorship",
    "later_not_validity": "Later recognition is not proof of upstream validity",
}

SPEC_MARKERS = {
    "title": "Existence Claim Evidence Requirement Boundary V0 Minimum Specification",
    "no_machinery": "This boundary does not create evidence-checking machinery",
    "not_enforced": "This rule is not enforced by this boundary",
    "future_claims_require_evidence": (
        "future existence-shaped true claims require separately supported evidence "
        "before they may be treated as standing or clean basis"
    ),
    "open_resolver_checker": "evidence requirement resolver/checker",
    "follow_on": "follow-on work",
}

WRAPPER_FIELDS = {
    "outcome",
    "block",
    "existence_claim_evidence_requirement_boundary_checks",
    "non_claims",
    "existence_claim_evidence_requirement_boundary_summary",
    "existence_claim_evidence_requirement_boundary_metadata",
}

NO_OVERREACH_KEYS = (
    "evidence_checker_created",
    "checker_created",
    "resolver_created",
    "test_created",
    "artifact_created",
    "scanner_created",
    "repository_scan_performed",
    "validation_performed",
    "evidence_requirement_enforced",
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_invalidated_by_replacement",
    "seam_case_replaced",
    "seam_case_treated_as_repair",
    "unsupported_existence_claims_validated",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
    "valid_derivation_event_recorded",
    "body_division_performed",
    "body_copy_performed",
    "body_distinction_created",
    "separate_lineage_receipt_created",
    "separate_sealing_created",
    "descendant_standing_check_performed",
    "standing_descendant_created",
    "first_crossing_authorized",
    "relation_created",
    "field_machinery_created",
    "iammai_system_continuation_reopened",
    "field_handoff_reversed",
    "runtime_created",
    "api_created",
    "machinery_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "follow_on_work_authorized",
    "repo_presence_treated_as_standing",
    "codex_execution_treated_as_truth",
    "operator_authorization_treated_as_sole_authorship",
    "derivative_rendering_treated_as_standing_evidence",
    "later_recognition_treated_as_upstream_validity",
    "contaminated_lineage_treated_as_clean_basis",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)


class ExistenceClaimEvidenceRequirementBoundaryTests(unittest.TestCase):
    def _write_text(self, path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _write_json(self, path: Path, payload: Any) -> None:
        self.assertFalse(path.is_dir(), f"fixture path collision at directory {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")

    def _synthetic_basis_files(
        self,
        base: Path,
        *,
        remove_marker: tuple[str, str] | None = None,
        extra_text: Mapping[str, str] | None = None,
    ) -> dict[str, Path]:
        extra_text = extra_text or {}

        def marker_lines(section: str, markers: Mapping[str, str]) -> list[str]:
            lines = []
            for marker in markers.values():
                if remove_marker == (section, marker):
                    lines.append(f"removed marker for {section}")
                else:
                    lines.append(marker)
            if extra_text.get(section):
                lines.append(extra_text[section])
            return lines

        affected_path = base / "basis" / "affected_descendant_event.md"
        seam_path = base / "basis" / "negative_seam_case.md"
        spec_path = base / "basis" / "evidence_requirement_boundary.md"

        self._write_text(
            affected_path,
            "# Synthetic affected descendant event\n\n"
            + "\n".join(f"- {line}" for line in marker_lines("affected", AFFECTED_MARKERS))
            + "\n",
        )
        self._write_text(
            seam_path,
            "# Synthetic negative seam case\n\n"
            + "\n".join(f"- {line}" for line in marker_lines("seam", SEAM_MARKERS))
            + "\n",
        )
        self._write_text(
            spec_path,
            "# Synthetic evidence requirement boundary\n\n"
            + "\n".join(f"- {line}" for line in marker_lines("spec", SPEC_MARKERS))
            + "\n",
        )
        return {
            "affected_file_path": affected_path,
            "seam_case_path": seam_path,
            "evidence_requirement_boundary_spec_path": spec_path,
        }

    def _valid_request(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_existence_claim_evidence_requirement_boundary_v0_min_request(
            existence_claim_evidence_requirement_boundary_id=(
                "existence_claim_evidence_requirement_boundary_001"
            ),
            affected_file_path=str(paths["affected_file_path"]),
            seam_case_path=str(paths["seam_case_path"]),
            evidence_requirement_boundary_spec_path=str(
                paths["evidence_requirement_boundary_spec_path"]
            ),
        )

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("existence_claim_evidence_requirement_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("existence_claim_evidence_requirement_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("existence_claim_evidence_requirement_boundary_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block") or {}
        self.assertIsInstance(block, dict)
        return block.get("code") or block.get("block_code")

    def safe_json_filename(self, name: Any, index: int | None = None) -> str:
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

    def assert_same_or_stable_path(self, actual: Any, expected: Any) -> None:
        actual_path = Path(str(actual))
        expected_path = Path(str(expected))
        if actual_path.is_absolute() and expected_path.is_absolute():
            if actual_path.resolve() == expected_path.resolve():
                return
        if str(actual).endswith(expected_path.name):
            return
        self.fail(f"{actual!r} does not match or stably end with {expected!r}")

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                emitted = check.get(key)
                if emitted is not None:
                    self.assertIn(emitted, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIsInstance(non_claims[key], bool)
            self.assertIs(non_claims[key], False)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_overreach_posture(result)

    def assert_boundary_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_no_raw_markdown_body_returned(
        self,
        result: Mapping[str, Any],
        sentinels: tuple[str, ...] = (),
    ) -> None:
        for section_name in (
            "affected_file_basis",
            "seam_case_basis",
            "evidence_requirement_boundary_spec_basis",
        ):
            section = result.get(section_name)
            self.assertIsInstance(section, dict)
            self.assertIs(section.get("raw_markdown_body_returned"), False)
            self.assertNotIn("raw_body", section)
            self.assertNotIn("full_body", section)
            self.assertNotIn("markdown_body", section)
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def assert_no_overreach_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in NO_OVERREACH_KEYS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)

    def assert_recorded_common(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertGreater(self.passed_check_count(result), 0)
        summary = self.summary(result)
        self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_canonical_false_non_claims(result)
        self.assert_boundary_object_not_wrapper(result)
        self.assert_no_raw_markdown_body_returned(result)
        self.assert_no_overreach_posture(result)

    def test_public_api_and_constants(self) -> None:
        public_names = (
            "resolve_existence_claim_evidence_requirement_boundary_v0_min",
            "resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path",
            "write_existence_claim_evidence_requirement_boundary_v0_min_result",
            "build_existence_claim_evidence_requirement_boundary_v0_min_summary",
            "build_declared_existence_claim_evidence_requirement_boundary_v0_min_request",
        )
        for name in public_names:
            self.assertTrue(callable(getattr(resolver, name, None)), name)

        constants = (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "OUTPUT_ROOT",
            "BOUNDARY_TYPE",
            "BOUNDARY_SCOPE",
            "SUPPORTED_BOUNDARY_TYPE_VALUES",
            "SUPPORTED_BOUNDARY_SCOPE_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        )
        for name in constants:
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_existence_claim_evidence_requirement_boundary_v0_min",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
        )
        self.assertEqual(
            resolver.BOUNDARY_SCOPE,
            "UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY",
        )
        self.assertIn(resolver.BOUNDARY_TYPE, resolver.SUPPORTED_BOUNDARY_TYPE_VALUES)
        self.assertIn(resolver.BOUNDARY_SCOPE, resolver.SUPPORTED_BOUNDARY_SCOPE_VALUES)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_existence_claim_evidence_"
                "requirement_boundary_v0_min"
            )
        )
        for outcome in (
            "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_RECORDED",
            "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_NOT_RECORDED",
            "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)

        required_false = (
            "evidence_checker_created",
            "checker_created",
            "resolver_created",
            "test_created",
            "artifact_created",
            "scanner_created",
            "repository_scan_performed",
            "validation_performed",
            "evidence_requirement_enforced",
            "affected_file_repaired",
            "unsupported_existence_claims_validated",
            "descendant_body_basis_candidate_a_created",
            "descendant_body_basis_candidate_b_created",
            "valid_derivation_event_recorded",
            "runtime_created",
            "authority_created",
            "currentness_created",
            "standing_created",
            "follow_on_work_authorized",
            "repo_presence_treated_as_standing",
            "codex_execution_treated_as_truth",
            "operator_authorization_treated_as_sole_authorship",
            "derivative_rendering_treated_as_standing_evidence",
            "later_recognition_treated_as_upstream_validity",
            "contaminated_lineage_treated_as_clean_basis",
            "hidden_repair_performed",
            "silent_overwrite_performed",
        )
        for key in required_false:
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

        allowed_true = (
            "existence_claim_evidence_requirement_boundary_recorded",
            "unsupported_existence_claim_class_preserved",
            "future_existence_claims_require_evidence",
            "affected_file_contamination_preserved",
            "seam_case_basis_preserved",
            "evidence_requirement_boundary_spec_basis_preserved",
            "future_checker_or_resolver_may_be_considered",
            "repo_presence_not_standing_preserved",
            "codex_execution_not_truth_preserved",
            "operator_authorization_not_sole_authorship_preserved",
            "later_recognition_not_upstream_validity_preserved",
            "result_level_non_claims_canonical_false",
        )
        for key in allowed_true:
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)

        required_codes = (
            "AFFECTED_FILE_UNSUPPORTED_CLAIM_A_MISSING",
            "SEAM_CASE_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_MISSING",
            "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NOT_ENFORCED_POSTURE_MISSING",
            "BOUNDARY_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
            "BOUNDARY_SCOPE_NOT_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY",
            "CHECKER_CREATED",
            "RESOLVER_CREATED",
            "TEST_CREATED",
            "ARTIFACT_CREATED",
            "SCANNER_CREATED",
            "REPOSITORY_SCAN_PERFORMED",
            "VALIDATION_PERFORMED",
            "EVIDENCE_REQUIREMENT_ENFORCED",
            "AFFECTED_FILE_REPAIRED",
            "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED",
            "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
            "VALID_DERIVATION_EVENT_RECORDED",
            "FOLLOW_ON_WORK_AUTHORIZED",
            "REPO_PRESENCE_TREATED_AS_STANDING",
            "CODEX_EXECUTION_TREATED_AS_TRUTH",
            "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP",
            "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE",
            "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
            "HIDDEN_REPAIR_PERFORMED",
            "SILENT_OVERWRITE_PERFORMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        for code in required_codes:
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_records_boundary_from_synthetic_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(Path(tmp))
            request = self._valid_request(paths)
            result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                request
            )

            self.assert_recorded_common(result)
            summary = self.summary(result)
            self.assertEqual(
                summary["boundary_id"],
                "existence_claim_evidence_requirement_boundary_001",
            )
            for key in (
                "existence_claim_evidence_requirement_boundary_metadata",
                "declared_existence_claim_evidence_requirement_boundary_question",
                "affected_file_basis",
                "seam_case_basis",
                "evidence_requirement_boundary_spec_basis",
                "existence_claim_evidence_requirement_boundary",
                "existence_claim_evidence_requirement_boundary_checks",
                "existence_claim_evidence_requirement_boundary_statement",
                "existence_claim_evidence_requirement_boundary_non_meaning",
                "additional_basis_required",
                "not_recorded_basis",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "existence_claim_evidence_requirement_boundary_summary",
            ):
                self.assertIn(key, result)

            boundary = self.boundary(result)
            self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
            self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
            self.assertIs(boundary["affected_file_contains_candidate_a_created_claim"], True)
            self.assertIs(boundary["affected_file_contains_candidate_b_created_claim"], True)
            self.assertIs(
                boundary["affected_file_contains_derivation_event_recorded_claim"],
                True,
            )
            for key in (
                "existence_claim_evidence_requirement_boundary_recorded",
                "unsupported_existence_claim_class_preserved",
                "future_existence_claims_require_evidence",
                "affected_file_contamination_preserved",
                "affected_file_basis_preserved",
                "seam_case_basis_preserved",
                "evidence_requirement_boundary_spec_basis_preserved",
                "future_checker_or_resolver_may_be_considered",
                "repo_presence_not_standing_preserved",
                "codex_execution_not_truth_preserved",
                "operator_authorization_not_sole_authorship_preserved",
                "later_recognition_not_upstream_validity_preserved",
                "existence_shape_created_claim_targeted",
                "existence_shape_recorded_claim_targeted",
                "existence_shape_performed_claim_targeted",
                "existence_shape_authorized_claim_targeted",
                "existence_shape_occurred_claim_targeted",
                "existence_shape_exists_claim_targeted",
                "existence_shape_standing_created_claim_targeted",
                "existence_shape_currentness_created_claim_targeted",
                "existence_shape_authority_created_claim_targeted",
            ):
                self.assertIs(boundary[key], True, key)

            statement = result["existence_claim_evidence_requirement_boundary_statement"]
            for key in (
                "existence_claim_evidence_requirement_boundary_recorded",
                "unsupported_existence_claim_class_preserved",
                "future_existence_claims_require_evidence",
                "future_checker_or_resolver_may_be_considered",
                "result_level_non_claims_canonical_false",
            ):
                self.assertIs(statement[key], True, key)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIn(key, statement)
                self.assertIs(statement[key], False)

    def test_records_boundary_from_default_live_files_if_present(self) -> None:
        default_paths = (
            REPO_ROOT / "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
            REPO_ROOT
            / "spec/SEAM_CASE_LAW__CO_AGENCY_AUTHORIZATION_UNSUPPORTED_EXISTENCE_CLAIM_V0.md",
            REPO_ROOT
            / "spec/EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_V0_MIN_SPEC.md",
        )
        missing = [str(path) for path in default_paths if not path.exists()]
        if missing:
            self.skipTest(f"default live basis files are not all present: {missing}")

        request = (
            resolver.build_declared_existence_claim_evidence_requirement_boundary_v0_min_request()
        )
        result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
            request
        )
        self.assert_recorded_common(result)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        for key in (
            "unsupported_existence_claim_class_preserved",
            "future_existence_claims_require_evidence",
            "future_checker_or_resolver_may_be_considered",
        ):
            self.assertIs(boundary[key], True, key)

    def test_basis_marker_blocking(self) -> None:
        cases = (
            (
                "affected",
                AFFECTED_MARKERS["candidate_a"],
                "AFFECTED_FILE_UNSUPPORTED_CLAIM_A_MISSING",
            ),
            (
                "affected",
                AFFECTED_MARKERS["candidate_b"],
                "AFFECTED_FILE_UNSUPPORTED_CLAIM_B_MISSING",
            ),
            (
                "affected",
                AFFECTED_MARKERS["derivation_recorded"],
                "AFFECTED_FILE_DERIVATION_EVENT_RECORDED_CLAIM_MISSING",
            ),
            (
                "seam",
                SEAM_MARKERS["unsupported_class"],
                "SEAM_CASE_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_MISSING",
            ),
            (
                "seam",
                SEAM_MARKERS["repo_not_standing"],
                "SEAM_CASE_REPO_PRESENCE_NOT_STANDING_MISSING",
            ),
            (
                "seam",
                SEAM_MARKERS["codex_not_truth"],
                "SEAM_CASE_CODEX_EXECUTION_NOT_TRUTH_MISSING",
            ),
            (
                "seam",
                SEAM_MARKERS["operator_not_sole"],
                "SEAM_CASE_OPERATOR_AUTHORIZATION_NOT_SOLE_AUTHORSHIP_MISSING",
            ),
            (
                "seam",
                SEAM_MARKERS["later_not_validity"],
                "SEAM_CASE_LATER_RECOGNITION_NOT_UPSTREAM_VALIDITY_MISSING",
            ),
            (
                "spec",
                SPEC_MARKERS["title"],
                "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_TITLE_MISSING",
            ),
            (
                "spec",
                SPEC_MARKERS["no_machinery"],
                "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NO_MACHINERY_POSTURE_MISSING",
            ),
            (
                "spec",
                SPEC_MARKERS["not_enforced"],
                "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_NOT_ENFORCED_POSTURE_MISSING",
            ),
            (
                "spec",
                SPEC_MARKERS["future_claims_require_evidence"],
                "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_EVIDENCE_REQUIREMENT_POSTURE_MISSING",
            ),
            (
                "spec",
                SPEC_MARKERS["open_resolver_checker"],
                "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_OPEN_RESOLVER_CHECKER_MISSING",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, (section, marker, expected_code) in enumerate(cases):
                with self.subTest(section=section, expected_code=expected_code):
                    case_base = base / self.safe_json_filename(expected_code, index)
                    paths = self._synthetic_basis_files(
                        case_base,
                        remove_marker=(section, marker),
                    )
                    request = self._valid_request(paths)
                    result = (
                        resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_request_shape_and_type_scope_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(Path(tmp) / "valid")
            valid_request = self._valid_request(paths)
            clean = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                valid_request
            )
            self.assert_recorded_common(clean)

            missing = Path(tmp) / "missing" / "basis.md"
            cases: list[tuple[str, Any, str]] = [
                (
                    "non_mapping_request",
                    ["not", "a", "mapping"],
                    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_REQUEST_MALFORMED",
                ),
                (
                    "missing_question",
                    lambda req: req.update(
                        {"existence_claim_evidence_requirement_boundary_question": ""}
                    ),
                    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_QUESTION_UNDECLARED",
                ),
                (
                    "unsupported_intent",
                    lambda req: req.update(
                        {
                            "existence_claim_evidence_requirement_boundary_intent": (
                                "UNSUPPORTED_INTENT"
                            )
                        }
                    ),
                    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_INTENT_UNSUPPORTED",
                ),
                (
                    "explicit_block_intent",
                    lambda req: req.update(
                        {
                            "existence_claim_evidence_requirement_boundary_intent": (
                                getattr(
                                    resolver,
                                    "INTENT_BLOCK",
                                    "BLOCK_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
                                )
                            )
                        }
                    ),
                    "EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY_BLOCK_REQUESTED",
                ),
                (
                    "missing_boundary_type",
                    lambda req: req.update({"boundary_type": ""}),
                    "BOUNDARY_TYPE_MISSING",
                ),
                (
                    "wrong_boundary_type",
                    lambda req: req.update({"boundary_type": "OTHER_BOUNDARY"}),
                    "BOUNDARY_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_REQUIREMENT_BOUNDARY",
                ),
                (
                    "missing_boundary_scope",
                    lambda req: req.update({"boundary_scope": ""}),
                    "BOUNDARY_SCOPE_MISSING",
                ),
                (
                    "wrong_boundary_scope",
                    lambda req: req.update({"boundary_scope": "OTHER_SCOPE"}),
                    "BOUNDARY_SCOPE_NOT_UNSUPPORTED_EXISTENCE_CLAIM_CLASS_REQUIREMENT_ONLY",
                ),
                (
                    "missing_affected_file_path",
                    lambda req: req.update({"affected_file_path": ""}),
                    "AFFECTED_FILE_PATH_MISSING",
                ),
                (
                    "unreadable_affected_file_path",
                    lambda req: req.update({"affected_file_path": str(missing)}),
                    "AFFECTED_FILE_UNREADABLE",
                ),
                (
                    "missing_seam_case_path",
                    lambda req: req.update({"seam_case_path": ""}),
                    "SEAM_CASE_PATH_MISSING",
                ),
                (
                    "unreadable_seam_case_path",
                    lambda req: req.update({"seam_case_path": str(missing)}),
                    "SEAM_CASE_UNREADABLE",
                ),
                (
                    "missing_spec_path",
                    lambda req: req.update({"evidence_requirement_boundary_spec_path": ""}),
                    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_PATH_MISSING",
                ),
                (
                    "unreadable_spec_path",
                    lambda req: req.update(
                        {"evidence_requirement_boundary_spec_path": str(missing)}
                    ),
                    "EVIDENCE_REQUIREMENT_BOUNDARY_SPEC_UNREADABLE",
                ),
            ]
            for name, mutation, expected_code in cases:
                with self.subTest(name=name):
                    if callable(mutation):
                        request = copy.deepcopy(valid_request)
                        mutation(request)
                        result = (
                            resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                                request
                            )
                        )
                    else:
                        result = (
                            resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                                mutation
                            )
                        )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "evidence_checker_created": "CHECKER_CREATED",
            "checker_created": "CHECKER_CREATED",
            "resolver_created": "RESOLVER_CREATED",
            "test_created": "TEST_CREATED",
            "artifact_created": "ARTIFACT_CREATED",
            "scanner_created": "SCANNER_CREATED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "validation_performed": "VALIDATION_PERFORMED",
            "evidence_requirement_enforced": "EVIDENCE_REQUIREMENT_ENFORCED",
            "affected_file_repaired": "AFFECTED_FILE_REPAIRED",
            "affected_file_edited": "AFFECTED_FILE_EDITED",
            "affected_file_deleted": "AFFECTED_FILE_DELETED",
            "affected_file_overwritten": "AFFECTED_FILE_OVERWRITTEN",
            "unsupported_existence_claims_validated": "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED",
            "descendant_body_basis_candidate_a_created": (
                "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED"
            ),
            "descendant_body_basis_candidate_b_created": (
                "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED"
            ),
            "valid_derivation_event_recorded": "VALID_DERIVATION_EVENT_RECORDED",
            "first_crossing_authorized": "FIRST_CROSSING_AUTHORIZED",
            "relation_created": "RELATION_CREATED",
            "field_machinery_created": "FIELD_MACHINERY_CREATED",
            "runtime_created": "RUNTIME_CREATED",
            "currentness_created": "CURRENTNESS_CREATED",
            "authority_created": "AUTHORITY_CREATED",
            "standing_created": "STANDING_CREATED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
            "repo_presence_treated_as_standing": "REPO_PRESENCE_TREATED_AS_STANDING",
            "codex_execution_treated_as_truth": "CODEX_EXECUTION_TREATED_AS_TRUTH",
            "operator_authorization_treated_as_sole_authorship": (
                "OPERATOR_AUTHORIZATION_TREATED_AS_SOLE_AUTHORSHIP"
            ),
            "derivative_rendering_treated_as_standing_evidence": (
                "DERIVATIVE_RENDERING_TREATED_AS_STANDING_EVIDENCE"
            ),
            "later_recognition_treated_as_upstream_validity": (
                "LATER_RECOGNITION_TREATED_AS_UPSTREAM_VALIDITY"
            ),
            "contaminated_lineage_treated_as_clean_basis": (
                "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS"
            ),
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
        }
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(Path(tmp))
            base_request = self._valid_request(paths)
            for key, expected_code in cases.items():
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request[key] = True
                    result = (
                        resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), expected_code)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.boundary(result)[key], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(Path(tmp))
            base_request = self._valid_request(paths)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base_request)
                    request["declared_non_claims"][key] = True
                    result = (
                        resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.boundary(result)[key], False)

            malformed_cases = {
                "missing_declared_non_claims": lambda req: req.pop(
                    "declared_non_claims"
                ),
                "non_mapping_declared_non_claims": lambda req: req.update(
                    {"declared_non_claims": []}
                ),
                "missing_required_key": lambda req: req["declared_non_claims"].pop(
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ),
                "non_bool_required_value": lambda req: req["declared_non_claims"].update(
                    {resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}
                ),
            }
            for name, mutation in malformed_cases.items():
                with self.subTest(name=name):
                    request = copy.deepcopy(base_request)
                    mutation(request)
                    result = (
                        resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                            request
                        )
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIn(self.block_code(result), resolver.BLOCK_CODES)

    def test_raw_markdown_body_containment(self) -> None:
        sentinels = (
            "RAW_AFFECTED_FILE_BODY_MUST_NOT_RETURN",
            "RAW_SEAM_CASE_BODY_MUST_NOT_RETURN",
            "RAW_EVIDENCE_REQUIREMENT_BOUNDARY_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(
                Path(tmp),
                extra_text={
                    "affected": f"\n{sentinels[0]}\n{sentinels[3]}",
                    "seam": f"\n{sentinels[1]}\n{sentinels[4]}",
                    "spec": f"\n{sentinels[2]}",
                },
            )
            request = self._valid_request(paths)
            original_request = copy.deepcopy(request)
            request["hostile_payload"] = {
                "raw_body": sentinels[0],
                "hidden_repo_state": sentinels[3],
                "current_working_tree": sentinels[4],
            }
            result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                request
            )
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assert_blocked_with_public_code(result)
            else:
                self.assert_recorded_common(result)
            self.assert_no_raw_markdown_body_returned(result, sentinels)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(resolver.BOUNDARY_TYPE, serialized)
            self.assertIn(resolver.BOUNDARY_SCOPE, serialized)
            self.assertEqual(
                {
                    key: request[key]
                    for key in original_request
                    if key in request
                },
                original_request,
            )

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            paths = self._synthetic_basis_files(base / "basis")
            request = self._valid_request(paths)
            request_path = base / "request" / "valid_request.json"
            self._write_json(request_path, request)

            result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path(
                request_path
            )
            self.assert_recorded_common(result)
            self.assertEqual(self.summary(result)["result_version"], "0.1.0")
            self.assertEqual(
                self.summary(result)["resolver_module"],
                "resolve_existence_claim_evidence_requirement_boundary_v0_min",
            )

            missing_result = (
                resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path(
                    base / "missing" / "request.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            malformed_path = base / "request" / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = base / "request" / "array.json"
            self._write_json(array_path, [])
            array_result = (
                resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            output_dir = (
                base
                / "writes"
                / "integrity_host_v0_min_coexistence_existence_claim_evidence_"
                "requirement_boundary_v0_min"
            )
            written = resolver.write_existence_claim_evidence_requirement_boundary_v0_min_result(
                result,
                output_dir,
            )
            second_written = (
                resolver.write_existence_claim_evidence_requirement_boundary_v0_min_result(
                    result,
                    output_dir,
                )
            )
            for path in (written, second_written):
                self.assertTrue(path.exists())
                self.assertTrue(path.parent.exists())
                self.assertIn(
                    "existence_claim_evidence_requirement_boundary_v0_min_result",
                    path.name,
                )
                with path.open("r", encoding="utf-8") as handle:
                    parsed = json.load(handle)
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            self.assertNotEqual(written, second_written)

            forbidden_roots = {
                "integrity_host_v0_min_coexistence_descendant_body_basis_derivation_event_v0_min",
                "integrity_host_v0_min_coexistence_seam_case_law__co_agency_authorization_unsupported_existence_claim_v0",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_checker_v0_min",
                "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_continuation_v0_min",
                "integrity_host_v0_min_coexistence_source_transfer_v0_min",
                "integrity_host_v0_min_coexistence_source_receipt_v0_min",
                "integrity_host_v0_min_coexistence_public_api_v0_min",
                "integrity_host_v0_min_coexistence_participant_facing_interface_v0_min",
                "integrity_host_v0_min_coexistence_distributed_network_v0_min",
                "integrity_host_v0_min_coexistence_runtime_hosting_v0_min",
                "integrity_host_v0_min_coexistence_runtime_loop_v0_min",
                "integrity_host_v0_min_coexistence_daemon_v0_min",
            }
            for path in (written, second_written):
                self.assertTrue(
                    forbidden_roots.isdisjoint(set(path.parts)),
                    f"wrote under forbidden root: {path}",
                )

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(
                Path(tmp),
                extra_text={
                    "affected": "RAW_AFFECTED_FILE_BODY_MUST_NOT_RETURN",
                    "seam": "RAW_SEAM_CASE_BODY_MUST_NOT_RETURN",
                    "spec": "RAW_EVIDENCE_REQUIREMENT_BOUNDARY_BODY_MUST_NOT_RETURN",
                },
            )
            request = self._valid_request(paths)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                request[key] = False
            request["nested_hostile_payload"] = {
                "raw_body": "RAW_AFFECTED_FILE_BODY_MUST_NOT_RETURN",
                "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            }
            request_before = copy.deepcopy(request)
            file_texts_before = {
                name: path.read_text(encoding="utf-8") for name, path in paths.items()
            }

            result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                request
            )

            self.assertEqual(request, request_before)
            for name, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), file_texts_before[name])
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            self.assert_canonical_false_non_claims(result)
            self.assert_no_overreach_posture(result)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._synthetic_basis_files(Path(tmp))
            request = self._valid_request(paths)
            result = resolver.resolve_existence_claim_evidence_requirement_boundary_v0_min(
                request
            )
            self.assert_recorded_common(result)
            summary = self.summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_existence_claim_evidence_requirement_boundary_v0_min",
            )
            self.assertEqual(
                summary["boundary_id"],
                "existence_claim_evidence_requirement_boundary_001",
            )
            self.assertIs(summary["boundary_recorded"], True)
            self.assert_same_or_stable_path(
                summary["affected_file_path"],
                paths["affected_file_path"],
            )
            self.assert_same_or_stable_path(summary["seam_case_path"], paths["seam_case_path"])
            self.assert_same_or_stable_path(
                summary["evidence_requirement_boundary_spec_path"],
                paths["evidence_requirement_boundary_spec_path"],
            )
            for key in (
                "unsupported_existence_claim_class_preserved",
                "future_existence_claims_require_evidence",
                "future_checker_or_resolver_may_be_considered",
                "affected_file_contamination_preserved",
                "seam_case_basis_preserved",
                "evidence_requirement_boundary_spec_basis_preserved",
                "checker_not_created",
                "resolver_not_created",
                "test_not_created",
                "artifact_not_created",
                "scanner_not_created",
                "repository_scan_not_performed",
                "validation_not_performed",
                "evidence_requirement_not_enforced",
                "affected_file_not_repaired",
                "affected_file_not_edited",
                "affected_file_not_deleted",
                "affected_file_not_overwritten",
                "unsupported_existence_claims_not_validated",
                "descendant_body_or_candidate_not_created",
                "valid_derivation_event_not_recorded",
                "standing_relation_crossing_runtime_authority_currentness_follow_on_not_created",
                "repo_presence_not_treated_as_standing",
                "codex_execution_not_treated_as_truth",
                "operator_authorization_not_treated_as_sole_authorship",
                "derivative_rendering_not_treated_as_standing_evidence",
                "later_recognition_not_treated_as_upstream_validity",
                "contaminated_lineage_not_treated_as_clean_basis",
                "hidden_repair_not_performed",
                "silent_overwrite_not_performed",
                "result_level_non_claims_canonical_false",
            ):
                self.assertIs(summary[key], True, key)


if __name__ == "__main__":
    unittest.main()
