"""Executable tests for one declared-surface existence-claim evidence check.

These tests keep the target surface explicit: one Markdown file and one declared
evidence map. They verify supported and unsupported per-claim outcomes while
preserving the non-claim posture: no repository scan, no file discovery, no
repair, no validation enforcement, no descendant body, no runtime, no authority,
no currentness, no standing, and no follow-on work.
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

import resolve_existence_claim_evidence_check_v0_min as resolver


CLAIM_KEYS = (
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
    "descendant_body_basis_derivation_event_recorded",
)
_DELETE = object()


class ExistenceClaimEvidenceCheckV0MinTests(unittest.TestCase):
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

    def _write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def write_synthetic_markdown(
        self,
        base: Path,
        name: str = "target.md",
        claims: tuple[str, ...] = CLAIM_KEYS,
        extra_lines: tuple[str, ...] = (),
    ) -> Path:
        lines = ["# Synthetic Existence Claim Target", ""]
        for claim_key in claims:
            lines.append(f"- `{claim_key} = true`")
        lines.extend(
            [
                "",
                "- `continuation_created = false`",
                "- `runtime_created = false`",
                "- `descendant_body_a_not_created = true`",
                "- `participant_output_not_authorized = true`",
                "- `result_level_non_claims_canonical_false = true`",
                "",
                "This target preserves false posture and explanatory non-claims.",
            ]
        )
        lines.extend(extra_lines)
        return self._write_text(base / name, "\n".join(lines) + "\n")

    def valid_request(
        self,
        target_path: Path,
        evidence_map: Mapping[str, Any] | list[Mapping[str, Any]] | None = None,
    ) -> dict[str, Any]:
        return resolver.build_declared_existence_claim_evidence_check_v0_min_request(
            target_surface_path=target_path,
            evidence_map={} if evidence_map is None else evidence_map,
        )

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block") or {}
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        checks = result.get("existence_claim_evidence_check_checks")
        self.assertIsInstance(checks, list)
        return checks

    def check_object(self, result: Mapping[str, Any]) -> dict[str, Any]:
        check = result.get("existence_claim_evidence_check")
        self.assertIsInstance(check, dict)
        return check

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        summary = result.get("existence_claim_evidence_check_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def per_claim_by_key(self, result: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
        outcomes = result.get("existence_claim_evidence_check_per_claim_outcomes")
        self.assertIsInstance(outcomes, list)
        return {
            str(item.get("claim_key")): item
            for item in outcomes
            if isinstance(item, dict)
        }

    def detected_claim_keys(self, result: Mapping[str, Any]) -> set[str]:
        detected = result.get("detected_existence_claims")
        self.assertIsInstance(detected, list)
        return {
            str(item.get("claim_key"))
            for item in detected
            if isinstance(item, dict)
        }

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return int(self.summary(result).get("failed_check_count", -1))

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return int(self.summary(result).get("passed_check_count", -1))

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        if block is None:
            return
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES, check)

    def assert_canonical_false_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIsInstance(non_claims[key], bool)
            self.assertIs(non_claims[key], False)

    def assert_blocked_with_public_code(
        self, result: Mapping[str, Any], expected_code: str | None = None
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_overreach(result)

    def assert_check_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        check = self.check_object(result)
        for key in (
            "outcome",
            "block",
            "existence_claim_evidence_check_checks",
            "non_claims",
            "existence_claim_evidence_check_summary",
            "existence_claim_evidence_check_metadata",
        ):
            self.assertNotIn(key, check)

    def assert_no_raw_full_markdown_body(
        self, result: Mapping[str, Any], sentinels: tuple[str, ...] = ()
    ) -> None:
        self.assertFalse(
            result.get("target_surface_basis", {}).get("raw_markdown_body_returned")
        )
        self.assertFalse(
            result.get("declared_evidence_map_basis", {}).get(
                "raw_evidence_map_returned"
            )
        )
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)
        for claim in result.get("detected_existence_claims", []):
            snippet = claim.get("raw_claim_snippet")
            self.assertIsInstance(snippet, str)
            self.assertNotIn("\n", snippet)

    def assert_no_overreach(self, result: Mapping[str, Any]) -> None:
        check = self.check_object(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, check)
            self.assertIs(check[key], False, key)

    def assert_recorded_common(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(
            self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE
        )
        self.assert_canonical_false_non_claims(result)
        self.assert_no_overreach(result)
        self.assert_check_object_not_wrapper(result)

    def _supported_evidence_map(self) -> dict[str, dict[str, str]]:
        kinds = (
            "operation_evidence",
            "resolver_evidence",
            "emitted_artifact_evidence",
        )
        return {
            claim_key: {
                "evidence_kind": kinds[index],
                "evidence_reference": f"artifact://bounded-evidence/{claim_key}",
            }
            for index, claim_key in enumerate(CLAIM_KEYS)
        }

    def _supported_evidence_list(self) -> list[dict[str, str]]:
        return [
            {
                "claim_key": claim_key,
                "evidence_kind": "test_evidence",
                "evidence_reference": f"test://bounded-evidence/{claim_key}",
            }
            for claim_key in CLAIM_KEYS
        ]

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_existence_claim_evidence_check_v0_min",
            "resolve_existence_claim_evidence_check_v0_min_from_path",
            "write_existence_claim_evidence_check_v0_min_result",
            "build_existence_claim_evidence_check_v0_min_summary",
            "build_declared_existence_claim_evidence_check_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

        for name in (
            "RESULT_VERSION",
            "RESOLVER_MODULE",
            "OUTCOME_RECORDED",
            "OUTCOME_NOT_RECORDED",
            "OUTCOME_REQUIRES_ADDITIONAL_BASIS",
            "OUTCOME_BLOCKED",
            "OUTCOME_FAMILY",
            "PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED",
            "PER_CLAIM_OUTCOME_UNSUPPORTED",
            "PER_CLAIM_OUTCOME_CLAIM_NOT_APPLICABLE",
            "PER_CLAIM_OUTCOME_CLAIM_CHECK_BLOCKED",
            "PER_CLAIM_OUTCOME_FAMILY",
            "FILE_OUTCOME_CLEAN",
            "FILE_OUTCOME_CONTAMINATED_CLASS",
            "FILE_OUTCOME_BLOCKED",
            "FILE_OUTCOME_FAMILY",
            "OUTPUT_ROOT",
            "CHECK_TYPE",
            "CHECK_SCOPE",
            "TARGET_SURFACE_KIND",
            "SUPPORTED_CHECK_TYPE_VALUES",
            "SUPPORTED_CHECK_SCOPE_VALUES",
            "SUPPORTED_TARGET_SURFACE_KIND_VALUES",
            "SUPPORTED_EVIDENCE_KINDS",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_existence_claim_evidence_check_v0_min",
        )
        self.assertEqual(resolver.CHECK_TYPE, "EXISTENCE_CLAIM_EVIDENCE_CHECK")
        self.assertEqual(resolver.CHECK_SCOPE, "DECLARED_SURFACE_ONLY")
        self.assertEqual(resolver.TARGET_SURFACE_KIND, "MARKDOWN")
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/"
                "integrity_host_v0_min_coexistence_"
                "existence_claim_evidence_check_v0_min"
            )
        )

        for outcome in (
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_NOT_RECORDED",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUIRES_ADDITIONAL_BASIS",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        for outcome in (
            "EVIDENCE_SUPPORTED",
            "UNSUPPORTED",
            "CLAIM_NOT_APPLICABLE",
            "CLAIM_CHECK_BLOCKED",
        ):
            self.assertIn(outcome, resolver.PER_CLAIM_OUTCOME_FAMILY)
        for outcome in (
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_CLEAN",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCKED",
        ):
            self.assertIn(outcome, resolver.FILE_OUTCOME_FAMILY)

        for kind in (
            "operation_evidence",
            "resolver_evidence",
            "test_evidence",
            "emitted_artifact_evidence",
            "terminal_summary_evidence",
            "prior_standing_basis_evidence",
            "bounded_operator_attested_evidence",
            "negative_seam_case_contamination_evidence",
        ):
            self.assertIn(kind, resolver.SUPPORTED_EVIDENCE_KINDS)

        for key in (
            "resolver_created",
            "test_created",
            "artifact_created",
            "scan_performed",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
            "target_surface_repaired",
            "target_surface_edited",
            "target_surface_deleted",
            "target_surface_overwritten",
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
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)

        for key in (
            "existence_claim_evidence_check_recorded",
            "target_surface_declared",
            "target_surface_readable",
            "target_surface_kind_is_markdown",
            "evidence_map_declared",
            "contaminated_lineage_policy_preserved",
            "detected_claims_extracted",
            "per_claim_outcomes_recorded",
            "file_level_outcome_recorded",
            "unsupported_claims_preserved",
            "contaminated_class_preserved",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)

        for code in (
            "TARGET_SURFACE_PATH_MISSING",
            "TARGET_SURFACE_UNREADABLE",
            "TARGET_SURFACE_KIND_NOT_MARKDOWN",
            "EVIDENCE_MAP_MISSING",
            "EVIDENCE_MAP_MALFORMED",
            "CHECK_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_CHECK",
            "CHECK_SCOPE_NOT_DECLARED_SURFACE_ONLY",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            "FOLLOW_ON_AUTHORIZED_TRUE",
            "REQUESTED_REPOSITORY_SCAN",
            "REQUESTED_FILE_DISCOVERY",
            "REQUESTED_TARGET_REPAIR",
            "REQUESTED_TARGET_MUTATION",
            "REQUESTED_VALIDATION_ENFORCEMENT",
            "REQUESTED_RAW_TARGET_BODY_RETURN",
            "SCAN_PERFORMED",
            "REPOSITORY_SCAN_PERFORMED",
            "FILE_DISCOVERY_PERFORMED",
            "VALIDATION_ENFORCED",
            "TARGET_SURFACE_REPAIRED",
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
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_records_contaminated_class_from_synthetic_target_with_empty_evidence_map(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(Path(tmp))
            request = self.valid_request(target, {})
            result = resolver.resolve_existence_claim_evidence_check_v0_min(request)

        self.assert_recorded_common(result)
        self.assertEqual(
            self.check_object(result)["file_level_outcome"],
            resolver.FILE_OUTCOME_CONTAMINATED_CLASS,
        )
        for section in (
            "existence_claim_evidence_check_metadata",
            "declared_existence_claim_evidence_check_question",
            "target_surface_basis",
            "declared_evidence_map_basis",
            "existence_claim_evidence_check",
            "detected_existence_claims",
            "existence_claim_evidence_check_per_claim_outcomes",
            "existence_claim_evidence_check_checks",
            "existence_claim_evidence_check_statement",
            "existence_claim_evidence_check_non_meaning",
            "additional_basis_required",
            "not_recorded_basis",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "existence_claim_evidence_check_summary",
        ):
            self.assertIn(section, result)

        check = self.check_object(result)
        self.assertEqual(check["check_type"], resolver.CHECK_TYPE)
        self.assertEqual(check["check_scope"], resolver.CHECK_SCOPE)
        self.assertEqual(check["target_surface_kind"], resolver.TARGET_SURFACE_KIND)
        self.assertTrue(check["existence_claim_evidence_check_recorded"])
        self.assertTrue(check["target_surface_declared"])
        self.assertTrue(check["target_surface_readable"])
        self.assertTrue(check["target_surface_kind_is_markdown"])
        self.assertTrue(check["evidence_map_declared"])
        self.assertGreaterEqual(check["detected_claim_count"], 3)
        self.assertGreaterEqual(check["unsupported_claim_count"], 3)
        self.assertEqual(check["evidence_supported_claim_count"], 0)
        self.assertTrue(check["contaminated_class_preserved"])
        self.assertTrue(check["unsupported_claims_preserved"])

        outcomes = self.per_claim_by_key(result)
        for claim_key in CLAIM_KEYS:
            self.assertIn(claim_key, outcomes)
            self.assertEqual(
                outcomes[claim_key]["per_claim_outcome"],
                resolver.PER_CLAIM_OUTCOME_UNSUPPORTED,
            )

        detected = self.detected_claim_keys(result)
        self.assertNotIn("continuation_created", detected)
        self.assertNotIn("runtime_created", detected)
        self.assertNotIn("descendant_body_a_created", detected)
        self.assertNotIn("output_authorized", detected)
        self.assertNotIn("result_level_non_claims_canonical_false", detected)
        self.assert_no_raw_full_markdown_body(result)

    def test_records_clean_result_with_adequate_declared_evidence(self) -> None:
        evidence_cases: tuple[tuple[str, Mapping[str, Any] | list[Mapping[str, Any]]], ...] = (
            ("mapping", self._supported_evidence_map()),
            ("list", self._supported_evidence_list()),
        )
        for style, evidence_map in evidence_cases:
            with self.subTest(style=style):
                with tempfile.TemporaryDirectory() as tmp:
                    target = self.write_synthetic_markdown(
                        Path(tmp), claims=CLAIM_KEYS, extra_lines=()
                    )
                    request = self.valid_request(target, evidence_map)
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                self.assert_recorded_common(result)
                check = self.check_object(result)
                self.assertEqual(check["file_level_outcome"], resolver.FILE_OUTCOME_CLEAN)
                self.assertEqual(check["detected_claim_count"], 3)
                self.assertEqual(check["evidence_supported_claim_count"], 3)
                self.assertEqual(check["unsupported_claim_count"], 0)
                for claim_key, outcome in self.per_claim_by_key(result).items():
                    if claim_key in CLAIM_KEYS:
                        self.assertEqual(
                            outcome["per_claim_outcome"],
                            resolver.PER_CLAIM_OUTCOME_EVIDENCE_SUPPORTED,
                        )

    def test_negative_seam_case_contamination_evidence_does_not_support_truth(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(
                Path(tmp), claims=("claim_alpha_created",)
            )
            request = self.valid_request(
                target,
                {
                    "claim_alpha_created": {
                        "evidence_kind": "negative_seam_case_contamination_evidence",
                        "evidence_reference": (
                            "spec/"
                            "SEAM_CASE_LAW__CO_AGENCY_AUTHORIZATION_"
                            "UNSUPPORTED_EXISTENCE_CLAIM_V0.md"
                        ),
                    }
                },
            )
            result = resolver.resolve_existence_claim_evidence_check_v0_min(request)

        self.assert_recorded_common(result)
        self.assertEqual(
            self.check_object(result)["file_level_outcome"],
            resolver.FILE_OUTCOME_CONTAMINATED_CLASS,
        )
        outcome = self.per_claim_by_key(result)["claim_alpha_created"]
        self.assertEqual(
            outcome["per_claim_outcome"], resolver.PER_CLAIM_OUTCOME_UNSUPPORTED
        )
        self.assertIn("NEGATIVE", str(outcome.get("unsupported_reason")))

    def test_insufficient_evidence_references_do_not_support_truth(self) -> None:
        references = (
            "file existence",
            "latest-file posture",
            "repo-local availability",
            "Codex execution",
            "summary text",
            "operator authorization",
            "derivative rendering",
            "later convergence",
        )
        for reference in references:
            with self.subTest(reference=reference):
                with tempfile.TemporaryDirectory() as tmp:
                    target = self.write_synthetic_markdown(
                        Path(tmp), claims=("claim_alpha_created",)
                    )
                    request = self.valid_request(
                        target,
                        {
                            "claim_alpha_created": {
                                "evidence_kind": "operation_evidence",
                                "evidence_reference": reference,
                            }
                        },
                    )
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                self.assert_recorded_common(result)
                self.assertEqual(
                    self.check_object(result)["file_level_outcome"],
                    resolver.FILE_OUTCOME_CONTAMINATED_CLASS,
                )
                self.assertEqual(
                    self.per_claim_by_key(result)["claim_alpha_created"][
                        "per_claim_outcome"
                    ],
                    resolver.PER_CLAIM_OUTCOME_UNSUPPORTED,
                )

    def test_claim_detection_pattern_coverage(self) -> None:
        expected = {
            "claim_alpha_created",
            "claim_beta_recorded",
            "claim_gamma_performed",
            "claim_delta_authorized",
            "claim_epsilon_occurred",
            "claim_zeta_exists",
            "claim_eta_standing_created",
            "claim_theta_currentness_created",
            "claim_iota_authority_created",
        }
        text = "\n".join(
            [
                "# Claim Detection Coverage",
                "claim_alpha_created = true",
                "`claim_beta_recorded = true`",
                "- `claim_gamma_performed = true`",
                "- claim_delta_authorized = true",
                "claim_epsilon_occurred = true",
                "claim_zeta_exists = true",
                "claim_eta_standing_created = true",
                "claim_theta_currentness_created = true",
                "claim_iota_authority_created = true",
                "claim_alpha_created = false",
                "claim_beta_not_created = true",
                "claim_gamma_not_authorized = true",
                "canonical_false_posture = true",
                "explanatory text without direct assignment",
                "",
            ]
        )
        with tempfile.TemporaryDirectory() as tmp:
            target = self._write_text(Path(tmp) / "patterns.md", text)
            result = resolver.resolve_existence_claim_evidence_check_v0_min(
                self.valid_request(target, {})
            )

        self.assert_recorded_common(result)
        self.assertEqual(expected, self.detected_claim_keys(result))
        for outcome in self.per_claim_by_key(result).values():
            self.assertEqual(
                outcome["per_claim_outcome"], resolver.PER_CLAIM_OUTCOME_UNSUPPORTED
            )

    def test_records_default_live_target_if_present(self) -> None:
        default_target = (
            REPO_ROOT / "spec" / "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md"
        )
        if not default_target.exists():
            self.skipTest("default live target is not present")
        result = resolver.resolve_existence_claim_evidence_check_v0_min(
            resolver.build_declared_existence_claim_evidence_check_v0_min_request()
        )
        self.assert_recorded_common(result)
        check = self.check_object(result)
        self.assertEqual(
            check["file_level_outcome"], resolver.FILE_OUTCOME_CONTAMINATED_CLASS
        )
        self.assertGreaterEqual(check["detected_claim_count"], 3)
        self.assertGreaterEqual(check["unsupported_claim_count"], 3)
        for claim_key in CLAIM_KEYS:
            self.assertEqual(
                self.per_claim_by_key(result)[claim_key]["per_claim_outcome"],
                resolver.PER_CLAIM_OUTCOME_UNSUPPORTED,
            )

    def test_request_shape_and_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            target = self.write_synthetic_markdown(base)
            valid = self.valid_request(target, {})
            missing_target = base / "missing.md"
            cases: list[tuple[str, Any, str]] = [
                (
                    "non_mapping_request",
                    [],
                    "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
                )
            ]
            mutation_cases: list[tuple[str, dict[str, Any], str]] = []

            def mutated(name: str, patch: dict[str, Any], code: str) -> None:
                request = copy.deepcopy(valid)
                for key, value in patch.items():
                    if value is _DELETE:
                        request.pop(key, None)
                    else:
                        request[key] = value
                mutation_cases.append((name, request, code))

            _DELETE = object()
            mutated(
                "missing_question",
                {"existence_claim_evidence_check_question": ""},
                "EXISTENCE_CLAIM_EVIDENCE_CHECK_QUESTION_UNDECLARED",
            )
            mutated(
                "unsupported_intent",
                {"existence_claim_evidence_check_intent": "unsupported"},
                "EXISTENCE_CLAIM_EVIDENCE_CHECK_INTENT_UNSUPPORTED",
            )
            mutated(
                "explicit_block_intent",
                {"existence_claim_evidence_check_intent": resolver.INTENT_BLOCK},
                "EXISTENCE_CLAIM_EVIDENCE_CHECK_BLOCK_REQUESTED",
            )
            mutated(
                "missing_target_path",
                {"target_surface_path": ""},
                "TARGET_SURFACE_PATH_MISSING",
            )
            mutated(
                "unreadable_target_path",
                {"target_surface_path": str(missing_target)},
                "TARGET_SURFACE_UNREADABLE",
            )
            mutated(
                "missing_target_kind",
                {"target_surface_kind": ""},
                "TARGET_SURFACE_KIND_MISSING",
            )
            mutated(
                "wrong_target_kind",
                {"target_surface_kind": "TEXT"},
                "TARGET_SURFACE_KIND_NOT_MARKDOWN",
            )
            mutated("missing_evidence_map", {"evidence_map": _DELETE}, "EVIDENCE_MAP_MISSING")
            mutated(
                "malformed_evidence_map",
                {"evidence_map": "not-a-map"},
                "EVIDENCE_MAP_MALFORMED",
            )
            mutated(
                "missing_contaminated_policy",
                {"contaminated_lineage_policy": ""},
                "CONTAMINATED_LINEAGE_POLICY_MISSING",
            )
            mutated("missing_check_type", {"check_type": ""}, "CHECK_TYPE_MISSING")
            mutated(
                "wrong_check_type",
                {"check_type": "OTHER_CHECK"},
                "CHECK_TYPE_NOT_EXISTENCE_CLAIM_EVIDENCE_CHECK",
            )
            mutated("missing_check_scope", {"check_scope": ""}, "CHECK_SCOPE_MISSING")
            mutated(
                "wrong_check_scope",
                {"check_scope": "REPOSITORY"},
                "CHECK_SCOPE_NOT_DECLARED_SURFACE_ONLY",
            )
            mutated("scan_allowed", {"scan_allowed": True}, "SCAN_ALLOWED_TRUE")
            mutated("repair_allowed", {"repair_allowed": True}, "REPAIR_ALLOWED_TRUE")
            mutated(
                "validation_enforcement_allowed",
                {"validation_enforcement_allowed": True},
                "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
            )
            mutated(
                "follow_on_authorized",
                {"follow_on_authorized": True},
                "FOLLOW_ON_AUTHORIZED_TRUE",
            )
            mutated(
                "requested_repository_scan",
                {"requested_repository_scan": True},
                "REQUESTED_REPOSITORY_SCAN",
            )
            mutated(
                "requested_file_discovery",
                {"requested_file_discovery": True},
                "REQUESTED_FILE_DISCOVERY",
            )
            mutated(
                "requested_target_repair",
                {"requested_target_repair": True},
                "REQUESTED_TARGET_REPAIR",
            )
            mutated(
                "requested_target_mutation",
                {"requested_target_mutation": True},
                "REQUESTED_TARGET_MUTATION",
            )
            mutated(
                "requested_validation_enforcement",
                {"requested_validation_enforcement": True},
                "REQUESTED_VALIDATION_ENFORCEMENT",
            )
            mutated(
                "return_raw_target_body",
                {"return_raw_target_body": True},
                "REQUESTED_RAW_TARGET_BODY_RETURN",
            )
            cases.extend(mutation_cases)

            for name, request, code in cases:
                with self.subTest(name=name):
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result, code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "file_discovery_performed": "FILE_DISCOVERY_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "target_surface_repaired": "TARGET_SURFACE_REPAIRED",
            "target_surface_edited": "TARGET_SURFACE_EDITED",
            "target_surface_deleted": "TARGET_SURFACE_DELETED",
            "target_surface_overwritten": "TARGET_SURFACE_OVERWRITTEN",
            "unsupported_existence_claims_validated": (
                "UNSUPPORTED_EXISTENCE_CLAIMS_VALIDATED"
            ),
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
            "repo_presence_treated_as_standing": (
                "REPO_PRESENCE_TREATED_AS_STANDING"
            ),
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
            target = self.write_synthetic_markdown(Path(tmp))
            valid = self.valid_request(target, {})
            for key, expected_code in cases.items():
                with self.subTest(key=key):
                    request = copy.deepcopy(valid)
                    request[key] = True
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result, expected_code)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.check_object(result)[key], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(Path(tmp))
            valid = self.valid_request(target, {})
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(valid)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.check_object(result)[key], False)

            malformed_cases = (
                ("missing_mapping", {"declared_non_claims": _DELETE}),
                ("non_mapping", {"declared_non_claims": []}),
                (
                    "missing_key",
                    {
                        "declared_non_claims": {
                            key: False
                            for key in resolver.REQUIRED_FALSE_NON_CLAIMS
                            if key != resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                        }
                    },
                ),
                (
                    "non_bool_value",
                    {
                        "declared_non_claims": {
                            **{key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
                            resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false",
                        }
                    },
                ),
            )
            for name, patch in malformed_cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(valid)
                    for key, value in patch.items():
                        if value is _DELETE:
                            request.pop(key, None)
                        else:
                            request[key] = value
                    result = resolver.resolve_existence_claim_evidence_check_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)

    def test_raw_markdown_body_containment(self) -> None:
        sentinels = (
            "RAW_TARGET_MARKDOWN_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(
                Path(tmp),
                extra_lines=tuple(f"Sensitive paragraph: {sentinel}" for sentinel in sentinels),
            )
            request = self.valid_request(target, {})
            request["raw_body"] = sentinels[0]
            request["hidden_repo_state"] = sentinels[1]
            request["current_working_tree"] = sentinels[2]
            original = copy.deepcopy(request)
            result = resolver.resolve_existence_claim_evidence_check_v0_min(request)

        self.assertEqual(request, original)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assert_blocked_with_public_code(result)
        else:
            self.assert_recorded_common(result)
        self.assert_no_raw_full_markdown_body(result, sentinels)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.CHECK_TYPE, serialized)
        self.assertIn(resolver.RESOLVER_MODULE, serialized)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            target = self.write_synthetic_markdown(base)
            request = self.valid_request(target, self._supported_evidence_map())
            request_path = self._write_json(base / "request.json", request)
            result = resolver.resolve_existence_claim_evidence_check_v0_min_from_path(
                request_path
            )
            self.assert_recorded_common(result)

            missing_result = resolver.resolve_existence_claim_evidence_check_v0_min_from_path(
                base / "missing_request.json"
            )
            self.assert_blocked_with_public_code(
                missing_result,
                "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_UNREADABLE",
            )
            malformed_path = self._write_text(base / "malformed.json", "{")
            malformed_result = (
                resolver.resolve_existence_claim_evidence_check_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(
                malformed_result,
                "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_UNREADABLE",
            )
            array_path = self._write_json(base / "array.json", [])
            array_result = (
                resolver.resolve_existence_claim_evidence_check_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(
                array_result,
                "DECLARED_EXISTENCE_CLAIM_EVIDENCE_CHECK_REQUEST_MALFORMED",
            )

            output_root = (
                base
                / "writes"
                / "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min"
            )
            first = resolver.write_existence_claim_evidence_check_v0_min_result(
                result, output_root
            )
            second = resolver.write_existence_claim_evidence_check_v0_min_result(
                result, output_root
            )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("existence_claim_evidence_check_v0_min_result", first.name)
            self.assertIn(
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min",
                str(first.parent),
            )
            for path in (first, second):
                with path.open("r", encoding="utf-8") as handle:
                    parsed = json.load(handle)
                self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)

            forbidden_parts = {
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary_v0_min",
                "descendant_body",
                "seam_case",
                "local_relevance_medium",
                "source_transfer",
                "source_receipt",
                "public_api",
                "participant_facing_interface",
                "distributed_network",
                "runtime_hosting",
                "runtime_loop",
                "daemon",
            }
            self.assertTrue(forbidden_parts.isdisjoint(set(first.parts)))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(Path(tmp))
            evidence_map = self._supported_evidence_map()
            request = self.valid_request(target, evidence_map)
            request["hostile_payload"] = {
                "raw_body": "RAW_TARGET_MARKDOWN_BODY_MUST_NOT_RETURN",
                "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            }
            before_request = copy.deepcopy(request)
            before_text = target.read_text(encoding="utf-8")
            result = resolver.resolve_existence_claim_evidence_check_v0_min(request)
            after_text = target.read_text(encoding="utf-8")

        self.assert_recorded_common(result)
        self.assertEqual(request, before_request)
        self.assertEqual(after_text, before_text)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = self.write_synthetic_markdown(Path(tmp))
            request = self.valid_request(target, {})
            result = resolver.resolve_existence_claim_evidence_check_v0_min(request)

        self.assert_recorded_common(result)
        summary = self.summary(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            summary["file_level_outcome"], resolver.FILE_OUTCOME_CONTAMINATED_CLASS
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["check_id"], resolver.DEFAULT_CHECK_ID)
        self.assertGreaterEqual(summary["detected_claim_count"], 3)
        self.assertGreaterEqual(summary["unsupported_claim_count"], 3)
        self.assertEqual(summary["evidence_supported_claim_count"], 0)
        self.assertGreaterEqual(
            summary["per_claim_outcome_counts"][
                resolver.PER_CLAIM_OUTCOME_UNSUPPORTED
            ],
            3,
        )
        for key in (
            "check_recorded",
            "target_surface_declared",
            "target_surface_readable",
            "evidence_map_declared",
            "scan_allowed_false",
            "repair_allowed_false",
            "validation_enforcement_allowed_false",
            "follow_on_authorized_false",
            "scan_not_performed",
            "repository_scan_not_performed",
            "file_discovery_not_performed",
            "validation_not_enforced",
            "target_surface_not_repaired",
            "target_surface_not_edited",
            "target_surface_not_deleted",
            "target_surface_not_overwritten",
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
