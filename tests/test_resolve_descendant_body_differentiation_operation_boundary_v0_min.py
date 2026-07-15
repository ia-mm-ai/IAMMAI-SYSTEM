"""Tests for the descendant-body differentiation operation boundary resolver.

This suite exercises one boundary resolver only. It verifies that the resolver
records a DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY object while not
creating or performing the future operation, not creating candidate records or
descendant bodies, not validating prior unsupported claims, not repairing the
contaminated lineage, not scanning or discovering files, and not authorizing
standing, crossing, relation, FIELD machinery, runtime, currentness, authority,
output, action, derivative reception, synchronization, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_differentiation_operation_boundary_v0_min as resolver


BOUNDARY_SPEC_MARKERS = {
    "title": "Descendant Body Differentiation Operation Boundary V0 Minimum Specification",
    "defines_boundary": (
        "This file defines one boundary for a future descendant-body "
        "differentiation operation."
    ),
    "does_not_perform": "This file does not perform the operation.",
    "candidate_evidence": (
        "candidate records must include evidence supporting their creation by "
        "that operation"
    ),
    "no_inherited_candidate": "The future operation must not inherit candidate existence",
    "boundary_created": "boundary_created = true",
    "operation_not_created": "operation_created = false",
    "candidate_records_not_created": "candidate_records_created = false",
    "candidate_a_not_created": "descendant_body_basis_candidate_a_created = false",
    "candidate_b_not_created": "descendant_body_basis_candidate_b_created = false",
    "valid_derivation_not_recorded": "valid_derivation_event_recorded = false",
}

CONTAMINATED_MARKERS = {
    "candidate_a": "descendant_body_basis_candidate_a_created = true",
    "candidate_b": "descendant_body_basis_candidate_b_created = true",
    "derivation_recorded": "descendant_body_basis_derivation_event_recorded = true",
}

EVIDENCE_SUMMARY_MARKERS = {
    "recorded": "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
    "contaminated": "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
    "candidate_a": "descendant_body_basis_candidate_a_created = UNSUPPORTED",
    "candidate_b": "descendant_body_basis_candidate_b_created = UNSUPPORTED",
    "derivation": "descendant_body_basis_derivation_event_recorded = UNSUPPORTED",
    "not_clean": "Contaminated lineage is not clean basis",
}

WRAPPER_FIELDS = {
    "outcome",
    "block",
    "descendant_body_differentiation_operation_boundary_checks",
    "non_claims",
    "descendant_body_differentiation_operation_boundary_summary",
    "descendant_body_differentiation_operation_boundary_metadata",
}

NO_OVERREACH_KEYS = (
    "operation_created",
    "operation_performed",
    "operation_recorded",
    "differentiation_performed",
    "candidate_records_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
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
    "evidence_check_overridden",
    "evidence_check_bypassed",
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
    "follow_on_work_authorized",
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)

DEFAULT_LIVE_PATHS = (
    REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_V0_MIN_SPEC.md",
    REPO_ROOT / "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
    REPO_ROOT / "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md",
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min"
    / "existence_claim_evidence_check_001__existence_claim_evidence_check_v0_min_result.json",
)


class DescendantBodyDifferentiationOperationBoundaryTests(unittest.TestCase):
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
        self.assertFalse(path.is_dir(), f"fixture path collision at directory {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def _marker_text(
        self,
        title: str,
        markers: Mapping[str, str],
        *,
        remove_marker: str | None = None,
        extra: str = "",
    ) -> str:
        lines = [f"# {title}", ""]
        for key, marker in markers.items():
            if key == remove_marker:
                lines.append(f"- removed marker {key}")
            else:
                lines.append(f"- {marker}")
        if extra:
            lines.extend(["", extra])
        return "\n".join(lines) + "\n"

    def evidence_artifact(self, **overrides: Any) -> dict[str, Any]:
        artifact: dict[str, Any] = {
            "outcome": "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
            "existence_claim_evidence_check_summary": {
                "file_level_outcome": (
                    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS"
                ),
                "failed_check_count": 0,
                "detected_claim_count": 3,
                "unsupported_claim_count": 3,
                "evidence_supported_claim_count": 0,
            },
            "existence_claim_evidence_check_per_claim_outcomes": [
                {
                    "claim_key": "descendant_body_basis_candidate_a_created",
                    "per_claim_outcome": "UNSUPPORTED",
                },
                {
                    "claim_key": "descendant_body_basis_candidate_b_created",
                    "per_claim_outcome": "UNSUPPORTED",
                },
                {
                    "claim_key": "descendant_body_basis_derivation_event_recorded",
                    "per_claim_outcome": "UNSUPPORTED",
                },
            ],
        }
        for key, value in overrides.items():
            if key == "file_level_outcome":
                artifact["existence_claim_evidence_check_summary"][key] = value
            elif key in {
                "failed_check_count",
                "detected_claim_count",
                "unsupported_claim_count",
                "evidence_supported_claim_count",
            }:
                artifact["existence_claim_evidence_check_summary"][key] = value
            elif key == "claim_outcome":
                artifact["existence_claim_evidence_check_per_claim_outcomes"][0][
                    "per_claim_outcome"
                ] = value
            else:
                artifact[key] = value
        return artifact

    def synthetic_basis_files(
        self,
        base: Path,
        *,
        remove: tuple[str, str] | None = None,
        artifact_overrides: Mapping[str, Any] | None = None,
        extra_text: str = "",
    ) -> dict[str, Path]:
        remove = remove or ("", "")
        artifact_overrides = dict(artifact_overrides or {})
        paths = {
            "boundary_spec_reference": base / "basis" / "boundary_spec.md",
            "contaminated_lineage_reference": base / "basis" / "contaminated_lineage.md",
            "evidence_check_terminal_summary_reference": (
                base / "basis" / "evidence_check_terminal_summary.md"
            ),
            "evidence_check_artifact_reference": (
                base / "basis" / "evidence_check_artifact.json"
            ),
        }
        self._write_text(
            paths["boundary_spec_reference"],
            self._marker_text(
                "Synthetic Boundary Spec",
                BOUNDARY_SPEC_MARKERS,
                remove_marker=remove[1] if remove[0] == "boundary" else None,
                extra=extra_text,
            ),
        )
        self._write_text(
            paths["contaminated_lineage_reference"],
            self._marker_text(
                "Synthetic Contaminated Lineage",
                CONTAMINATED_MARKERS,
                remove_marker=remove[1] if remove[0] == "contaminated" else None,
                extra=extra_text,
            ),
        )
        self._write_text(
            paths["evidence_check_terminal_summary_reference"],
            self._marker_text(
                "Synthetic Evidence Check Terminal Summary",
                EVIDENCE_SUMMARY_MARKERS,
                remove_marker=remove[1] if remove[0] == "summary" else None,
                extra=extra_text,
            ),
        )
        self._write_json(
            paths["evidence_check_artifact_reference"],
            self.evidence_artifact(**artifact_overrides),
        )
        return paths

    def valid_request(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_descendant_body_differentiation_operation_boundary_v0_min_request(
            descendant_body_differentiation_operation_boundary_id=(
                "descendant_body_differentiation_operation_boundary_001"
            ),
            standing_body_proof_basis_reference=(
                "declared-standing-body-proof-basis-before-contaminated-derivation-event"
            ),
            contaminated_lineage_reference=str(paths["contaminated_lineage_reference"]),
            evidence_requirement_boundary_reference=(
                "synthetic-existence-claim-evidence-requirement-boundary"
            ),
            evidence_check_terminal_summary_reference=str(
                paths["evidence_check_terminal_summary_reference"]
            ),
            evidence_check_artifact_reference=str(
                paths["evidence_check_artifact_reference"]
            ),
            boundary_spec_reference=str(paths["boundary_spec_reference"]),
        )

    def boundary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        boundary = result.get("descendant_body_differentiation_operation_boundary")
        self.assertIsInstance(boundary, dict)
        return boundary

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("descendant_body_differentiation_operation_boundary_checks")
        self.assertIsInstance(checks, list)
        return checks

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("descendant_body_differentiation_operation_boundary_summary")
        self.assertIsInstance(summary, dict)
        return summary

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is False)

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        return sum(1 for check in self.checks(result) if check.get("passed") is True)

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block") or {}
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

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
            self.assertIs(non_claims[key], False, key)

    def assert_boundary_object_not_wrapper(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_no_overreach(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in NO_OVERREACH_KEYS:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False, key)

    def assert_no_raw_full_markdown_body(
        self, result: Mapping[str, Any], sentinels: tuple[str, ...] = ()
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for key in ("raw_body", "full_body", "markdown_body", "hidden_repo_state"):
            self.assertNotIn(f'"{key}": "RAW_', serialized)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)
        self.assertFalse(
            result.get("future_operation_boundary_basis", {})
            .get("boundary_spec_reference", {})
            .get("raw_markdown_body_returned")
        )
        self.assertFalse(
            result.get("upstream_basis", {})
            .get("contaminated_lineage_reference", {})
            .get("raw_markdown_body_returned")
        )

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
        self.assert_boundary_object_not_wrapper(result)

    def assert_recorded_common(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_canonical_false_non_claims(result)
        self.assert_boundary_object_not_wrapper(result)
        self.assert_no_raw_full_markdown_body(result)
        self.assert_no_overreach(result)

    def assert_recorded_boundary_posture(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["future_operation_type"], resolver.FUTURE_OPERATION_TYPE)
        self.assertEqual(boundary["future_operation_scope"], resolver.FUTURE_OPERATION_SCOPE)
        self.assertEqual(
            boundary["future_candidate_record_policy"],
            resolver.FUTURE_CANDIDATE_RECORD_POLICY,
        )
        self.assertEqual(
            boundary["future_failure_visibility_policy"],
            resolver.FUTURE_FAILURE_VISIBILITY_POLICY,
        )
        for key in (
            "descendant_body_differentiation_operation_boundary_recorded",
            "boundary_created",
            "standing_body_proof_basis_reference_declared",
            "contaminated_lineage_reference_declared",
            "evidence_requirement_boundary_reference_declared",
            "evidence_check_terminal_summary_reference_declared",
            "evidence_check_artifact_reference_declared",
            "future_operation_shape_declared",
            "future_operation_type_accepted",
            "future_operation_scope_accepted",
            "future_candidate_record_policy_accepted",
            "future_failure_visibility_policy_accepted",
            "boundary_spec_markers_present",
            "contaminated_lineage_markers_present",
            "evidence_check_terminal_summary_markers_present",
            "evidence_check_artifact_markers_present",
            "contaminated_lineage_preserved",
            "prior_unsupported_claims_preserved",
            "future_operation_not_created",
            "candidate_records_not_created",
            "descendant_bodies_not_created",
        ):
            self.assertIs(boundary[key], True, key)
        shape = boundary["future_operation_shape"]
        self.assertIsInstance(shape, dict)
        self.assertEqual(shape["operation_type"], resolver.FUTURE_OPERATION_TYPE)
        self.assertEqual(shape["operation_scope"], resolver.FUTURE_OPERATION_SCOPE)
        self.assertEqual(
            shape["candidate_record_policy"], resolver.FUTURE_CANDIDATE_RECORD_POLICY
        )
        self.assertEqual(
            shape["failure_visibility_policy"],
            resolver.FUTURE_FAILURE_VISIBILITY_POLICY,
        )
        for key in (
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
            self.assertIs(shape[key], False, key)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_differentiation_operation_boundary_v0_min",
            "resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path",
            "write_descendant_body_differentiation_operation_boundary_v0_min_result",
            "build_descendant_body_differentiation_operation_boundary_v0_min_summary",
            "build_declared_descendant_body_differentiation_operation_boundary_v0_min_request",
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
            "BOUNDARY_TYPE",
            "FUTURE_OPERATION_TYPE",
            "FUTURE_OPERATION_SCOPE",
            "FUTURE_CANDIDATE_RECORD_POLICY",
            "FUTURE_FAILURE_VISIBILITY_POLICY",
            "SUPPORTED_FUTURE_OPERATION_TYPE_VALUES",
            "SUPPORTED_FUTURE_OPERATION_SCOPE_VALUES",
            "SUPPORTED_FUTURE_CANDIDATE_RECORD_POLICY_VALUES",
            "SUPPORTED_FUTURE_FAILURE_VISIBILITY_POLICY_VALUES",
            "FUTURE_OPERATION_OUTCOME_FAMILY",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_differentiation_operation_boundary_v0_min",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY",
        )
        self.assertEqual(
            resolver.FUTURE_OPERATION_TYPE,
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
        )
        self.assertEqual(
            resolver.FUTURE_OPERATION_SCOPE,
            "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
        )
        self.assertEqual(
            resolver.FUTURE_CANDIDATE_RECORD_POLICY,
            "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS",
        )
        self.assertEqual(
            resolver.FUTURE_FAILURE_VISIBILITY_POLICY,
            "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL",
        )
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_descendant_body_"
                "differentiation_operation_boundary_v0_min"
            )
        )
        for outcome in (
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_NOT_RECORDED",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_BLOCKED",
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        for outcome in (
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCKED",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_NOT_RECORDED",
        ):
            self.assertIn(outcome, resolver.FUTURE_OPERATION_OUTCOME_FAMILY)
        for key in (
            "operation_created",
            "operation_performed",
            "operation_recorded",
            "differentiation_performed",
            "candidate_records_created",
            "descendant_body_basis_candidate_a_created",
            "descendant_body_basis_candidate_b_created",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "valid_derivation_event_recorded",
            "affected_file_repaired",
            "affected_file_treated_as_clean_basis",
            "contaminated_lineage_treated_as_clean_basis",
            "evidence_check_overridden",
            "evidence_check_bypassed",
            "standing_descendant_created",
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
            "scan_performed",
            "repository_scan_performed",
            "repair_performed",
            "validation_enforced",
            "hidden_repair_performed",
            "silent_overwrite_performed",
        ):
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "descendant_body_differentiation_operation_boundary_recorded",
            "boundary_created",
            "standing_body_proof_basis_reference_declared",
            "contaminated_lineage_reference_declared",
            "evidence_requirement_boundary_reference_declared",
            "evidence_check_terminal_summary_reference_declared",
            "evidence_check_artifact_reference_declared",
            "future_operation_shape_declared",
            "future_operation_type_accepted",
            "future_operation_scope_accepted",
            "future_candidate_record_policy_accepted",
            "future_failure_visibility_policy_accepted",
            "boundary_spec_markers_present",
            "contaminated_lineage_markers_present",
            "evidence_check_terminal_summary_markers_present",
            "evidence_check_artifact_markers_present",
            "contaminated_lineage_preserved",
            "prior_unsupported_claims_preserved",
            "future_operation_not_created",
            "candidate_records_not_created",
            "descendant_bodies_not_created",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for code in (
            "STANDING_BODY_PROOF_BASIS_REFERENCE_MISSING",
            "CONTAMINATED_LINEAGE_REFERENCE_MISSING",
            "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING",
            "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING",
            "BOUNDARY_SPEC_REFERENCE_MISSING",
            "FUTURE_OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
            "FUTURE_OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
            "FUTURE_CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
            "FUTURE_FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
            "FUTURE_OPERATION_SHAPE_MISSING",
            "SCAN_ALLOWED_TRUE",
            "REPAIR_ALLOWED_TRUE",
            "VALIDATION_ENFORCEMENT_ALLOWED_TRUE",
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
            "CONTAMINATED_LINEAGE_MARKER_MISSING",
            "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING",
            "OPERATION_CREATED",
            "OPERATION_PERFORMED",
            "OPERATION_RECORDED",
            "DIFFERENTIATION_PERFORMED",
            "CANDIDATE_RECORDS_CREATED",
            "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
            "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
            "PRIOR_UNSUPPORTED_CANDIDATE_A_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_CANDIDATE_B_CLAIM_VALIDATED",
            "PRIOR_UNSUPPORTED_DERIVATION_EVENT_CLAIM_VALIDATED",
            "VALID_DERIVATION_EVENT_RECORDED",
            "AFFECTED_FILE_REPAIRED",
            "AFFECTED_FILE_TREATED_AS_CLEAN_BASIS",
            "CONTAMINATED_LINEAGE_TREATED_AS_CLEAN_BASIS",
            "EVIDENCE_CHECK_OVERRIDDEN",
            "EVIDENCE_CHECK_BYPASSED",
            "FIRST_CROSSING_AUTHORIZED",
            "RELATION_CREATED",
            "FIELD_MACHINERY_CREATED",
            "RUNTIME_CREATED",
            "CURRENTNESS_CREATED",
            "AUTHORITY_CREATED",
            "STANDING_CREATED",
            "FOLLOW_ON_WORK_AUTHORIZED",
            "SCAN_PERFORMED",
            "REPOSITORY_SCAN_PERFORMED",
            "REPAIR_PERFORMED",
            "VALIDATION_ENFORCED",
            "HIDDEN_REPAIR_PERFORMED",
            "SILENT_OVERWRITE_PERFORMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES, code)

    def test_records_boundary_from_synthetic_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.synthetic_basis_files(Path(tmp))
            request = self.valid_request(paths)
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )

        self.assert_recorded_common(result)
        self.assertEqual(
            self.boundary(result)["boundary_id"],
            "descendant_body_differentiation_operation_boundary_001",
        )
        for section in (
            "descendant_body_differentiation_operation_boundary_metadata",
            "declared_descendant_body_differentiation_operation_boundary_question",
            "upstream_basis",
            "future_operation_boundary_basis",
            "descendant_body_differentiation_operation_boundary",
            "descendant_body_differentiation_operation_boundary_checks",
            "descendant_body_differentiation_operation_boundary_statement",
            "descendant_body_differentiation_operation_boundary_non_meaning",
            "additional_basis_required",
            "not_recorded_basis",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "descendant_body_differentiation_operation_boundary_summary",
        ):
            self.assertIn(section, result)
        self.assert_recorded_boundary_posture(result)
        self.assert_canonical_false_non_claims(result)

    def test_records_default_live_target_if_present(self) -> None:
        missing = [str(path) for path in DEFAULT_LIVE_PATHS if not path.exists()]
        if missing:
            self.skipTest(f"default live basis missing: {missing}")
        request = resolver.build_declared_descendant_body_differentiation_operation_boundary_v0_min_request()
        result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
            request
        )
        self.assert_recorded_common(result)
        self.assert_recorded_boundary_posture(result)
        self.assert_no_overreach(result)
        self.assert_canonical_false_non_claims(result)

    def test_do_not_record_intent_does_not_create_positive_boundary_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(self.synthetic_basis_files(Path(tmp)))
            request[
                "descendant_body_differentiation_operation_boundary_intent"
            ] = "DO_NOT_RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assert_not_blocked(result)
        boundary = self.boundary(result)
        self.assertIs(boundary["descendant_body_differentiation_operation_boundary_recorded"], False)
        self.assertIs(boundary["boundary_created"], False)
        self.assert_no_overreach(result)
        self.assert_canonical_false_non_claims(result)

    def test_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(self.synthetic_basis_files(Path(tmp)))
            request[
                "descendant_body_differentiation_operation_boundary_intent"
            ] = "BLOCK_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY"
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )
        self.assert_blocked_with_public_code(
            result,
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_BLOCK_REQUESTED",
        )

    def test_request_shape_and_blocking_behavior(self) -> None:
        direct_non_mapping = (
            resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                ["not", "mapping"]
            )
        )
        self.assert_blocked_with_public_code(
            direct_non_mapping,
            "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_REQUEST_MALFORMED",
        )

        cases: list[tuple[str, str | None, Any, str | None]] = [
            ("missing_question", "descendant_body_differentiation_operation_boundary_question", None, "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_QUESTION_UNDECLARED"),
            ("unsupported_intent", "descendant_body_differentiation_operation_boundary_intent", "UNSUPPORTED", "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_INTENT_UNSUPPORTED"),
            ("missing_standing_basis", "standing_body_proof_basis_reference", None, "STANDING_BODY_PROOF_BASIS_REFERENCE_MISSING"),
            ("missing_contaminated_lineage", "contaminated_lineage_reference", None, "CONTAMINATED_LINEAGE_REFERENCE_MISSING"),
            ("missing_evidence_requirement", "evidence_requirement_boundary_reference", None, "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING"),
            ("missing_summary", "evidence_check_terminal_summary_reference", None, "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING"),
            ("missing_artifact", "evidence_check_artifact_reference", None, "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING"),
            ("missing_boundary_spec", "boundary_spec_reference", None, "BOUNDARY_SPEC_REFERENCE_MISSING"),
            ("missing_future_type", "future_operation_type", None, "FUTURE_OPERATION_TYPE_MISSING"),
            ("wrong_future_type", "future_operation_type", "WRONG", "FUTURE_OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"),
            ("missing_future_scope", "future_operation_scope", None, "FUTURE_OPERATION_SCOPE_MISSING"),
            ("wrong_future_scope", "future_operation_scope", "WRONG", "FUTURE_OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"),
            ("missing_candidate_policy", "future_candidate_record_policy", None, "FUTURE_CANDIDATE_RECORD_POLICY_MISSING"),
            ("wrong_candidate_policy", "future_candidate_record_policy", "WRONG", "FUTURE_CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED"),
            ("missing_failure_policy", "future_failure_visibility_policy", None, "FUTURE_FAILURE_VISIBILITY_POLICY_MISSING"),
            ("wrong_failure_policy", "future_failure_visibility_policy", "WRONG", "FUTURE_FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK"),
            ("missing_future_shape", "future_operation_shape", None, "FUTURE_OPERATION_SHAPE_MISSING"),
            ("malformed_future_shape", "future_operation_shape", "not-a-shape", "FUTURE_OPERATION_SHAPE_MALFORMED"),
            ("scan_allowed", "scan_allowed", True, "SCAN_ALLOWED_TRUE"),
            ("repair_allowed", "repair_allowed", True, "REPAIR_ALLOWED_TRUE"),
            ("validation_allowed", "validation_enforcement_allowed", True, "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
            ("standing_authorized", "standing_authorized", True, "STANDING_AUTHORIZED_TRUE"),
            ("crossing_authorized", "crossing_authorized", True, "CROSSING_AUTHORIZED_TRUE"),
            ("relation_authorized", "relation_authorized", True, "RELATION_AUTHORIZED_TRUE"),
            ("field_machinery_authorized", "field_machinery_authorized", True, "FIELD_MACHINERY_AUTHORIZED_TRUE"),
            ("runtime_authorized", "runtime_authorized", True, "RUNTIME_AUTHORIZED_TRUE"),
            ("currentness_authorized", "currentness_authorized", True, "CURRENTNESS_AUTHORIZED_TRUE"),
            ("authority_authorized", "authority_authorized", True, "AUTHORITY_AUTHORIZED_TRUE"),
            ("output_authorized", "output_authorized", True, "OUTPUT_AUTHORIZED_TRUE"),
            ("action_authorized", "action_authorized", True, "ACTION_AUTHORIZED_TRUE"),
            ("derivative_reception_authorized", "derivative_reception_authorized", True, "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE"),
            ("synchronization_authorized", "synchronization_authorized", True, "SYNCHRONIZATION_AUTHORIZED_TRUE"),
            ("follow_on_authorized", "follow_on_authorized", True, "FOLLOW_ON_AUTHORIZED_TRUE"),
        ]
        requested_cases = [
            ("request_repository_scan", "requested_repository_scan", "REQUESTED_REPOSITORY_SCAN"),
            ("request_file_discovery", "requested_file_discovery", "REQUESTED_FILE_DISCOVERY"),
            ("request_affected_file_repair", "requested_affected_file_repair", "REQUESTED_AFFECTED_FILE_REPAIR"),
            ("request_affected_file_mutation", "requested_affected_file_mutation", "REQUESTED_AFFECTED_FILE_MUTATION"),
            ("request_prior_unsupported_claim_validation", "requested_prior_unsupported_claim_validation", "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION"),
            ("request_evidence_check_override", "requested_evidence_check_override", "REQUESTED_EVIDENCE_CHECK_OVERRIDE"),
            ("request_evidence_check_bypass", "requested_evidence_check_bypass", "REQUESTED_EVIDENCE_CHECK_BYPASS"),
            ("request_operation_creation", "requested_operation_creation", "REQUESTED_OPERATION_CREATION"),
            ("request_operation_performance", "requested_operation_performance", "REQUESTED_OPERATION_PERFORMANCE"),
            ("request_candidate_record_creation", "requested_candidate_record_creation", "REQUESTED_CANDIDATE_RECORD_CREATION"),
            ("request_descendant_body_creation", "requested_descendant_body_creation", "REQUESTED_DESCENDANT_BODY_CREATION"),
            ("request_standing_authorization", "requested_standing_authorization", "REQUESTED_STANDING_AUTHORIZATION"),
            ("request_crossing_authorization", "requested_crossing_authorization", "REQUESTED_CROSSING_AUTHORIZATION"),
            ("request_relation_creation", "requested_relation_creation", "REQUESTED_RELATION_CREATION"),
            ("request_field_machinery_creation", "requested_field_machinery_creation", "REQUESTED_FIELD_MACHINERY_CREATION"),
            ("request_runtime_creation", "requested_runtime_creation", "REQUESTED_RUNTIME_CREATION"),
            ("request_currentness_creation", "requested_currentness_creation", "REQUESTED_CURRENTNESS_CREATION"),
            ("request_authority_creation", "requested_authority_creation", "REQUESTED_AUTHORITY_CREATION"),
            ("request_output_authorization", "requested_output_authorization", "REQUESTED_OUTPUT_AUTHORIZATION"),
            ("request_action_authorization", "requested_action_authorization", "REQUESTED_ACTION_AUTHORIZATION"),
            ("request_derivative_reception_authorization", "requested_derivative_reception_authorization", "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION"),
            ("request_synchronization_authorization", "requested_synchronization_authorization", "REQUESTED_SYNCHRONIZATION_AUTHORIZATION"),
            ("request_follow_on_authorization", "requested_follow_on_authorization", "REQUESTED_FOLLOW_ON_AUTHORIZATION"),
            ("return_raw_markdown_body", "return_raw_markdown_body", "REQUESTED_RAW_MARKDOWN_BODY_RETURN"),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            paths = self.synthetic_basis_files(Path(tmp))
            for index, (name, key, value, expected_code) in enumerate(cases):
                with self.subTest(name=name):
                    request = self.valid_request(paths)
                    if value is None and key is not None:
                        request.pop(key, None)
                    elif key is not None:
                        request[key] = value
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result, expected_code)
            for index, (prompt_name, resolver_name, expected_code) in enumerate(
                requested_cases
            ):
                with self.subTest(name=prompt_name, file=self.safe_json_filename(prompt_name, index)):
                    request = self.valid_request(paths)
                    request[prompt_name] = True
                    request[resolver_name] = True
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result, expected_code)

    def test_marker_validation_blocking_behavior(self) -> None:
        marker_cases = [
            ("boundary_marker", ("boundary", "does_not_perform"), {}, "BOUNDARY_SPEC_MARKER_MISSING"),
            ("contaminated_marker", ("contaminated", "candidate_a"), {}, "CONTAMINATED_LINEAGE_MARKER_MISSING"),
            ("summary_marker", ("summary", "candidate_a"), {}, "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("artifact_outcome", ("", ""), {"outcome": "WRONG"}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_file_level_outcome", ("", ""), {"file_level_outcome": "WRONG"}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_failed_count", ("", ""), {"failed_check_count": 1}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_detected_count", ("", ""), {"detected_claim_count": 2}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_unsupported_count", ("", ""), {"unsupported_claim_count": 2}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_supported_count", ("", ""), {"evidence_supported_claim_count": 1}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("artifact_claim_outcome", ("", ""), {"claim_outcome": "EVIDENCE_SUPPORTED"}, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for index, (name, remove, overrides, expected_code) in enumerate(marker_cases):
                with self.subTest(name=name, file=self.safe_json_filename(name, index)):
                    paths = self.synthetic_basis_files(
                        base / self.safe_json_filename(name, index).removesuffix(".json"),
                        remove=remove,
                        artifact_overrides=overrides,
                    )
                    request = self.valid_request(paths)
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result, expected_code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        false_cases = {
            "operation_created": "OPERATION_CREATED",
            "operation_performed": "OPERATION_PERFORMED",
            "operation_recorded": "OPERATION_RECORDED",
            "differentiation_performed": "DIFFERENTIATION_PERFORMED",
            "candidate_records_created": "CANDIDATE_RECORDS_CREATED",
            "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
            "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
            "descendant_body_basis_candidate_a_created": "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
            "descendant_body_basis_candidate_b_created": "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
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
            "evidence_check_overridden": "EVIDENCE_CHECK_OVERRIDDEN",
            "evidence_check_bypassed": "EVIDENCE_CHECK_BYPASSED",
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
            "output_authorized": "OUTPUT_AUTHORIZED",
            "action_authorized": "ACTION_AUTHORIZED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "synchronization_authorized": "SYNCHRONIZATION_AUTHORIZED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "repair_performed": "REPAIR_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
        }
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.synthetic_basis_files(Path(tmp))
            for key, expected_code in false_cases.items():
                with self.subTest(key=key):
                    request = self.valid_request(paths)
                    request[key] = True
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    emitted_codes = {
                        check.get("block_code") or check.get("failure_code")
                        for check in self.checks(result)
                    }
                    self.assertIn(expected_code, emitted_codes)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.boundary(result)[key], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.synthetic_basis_files(Path(tmp))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = self.valid_request(paths)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assertIs(self.boundary(result)[key], False)

            malformed_cases = [
                ("missing_mapping", None),
                ("non_mapping", []),
                ("missing_key", "missing_key"),
                ("non_bool", "non_bool"),
            ]
            for name, mode in malformed_cases:
                with self.subTest(name=name):
                    request = self.valid_request(paths)
                    if mode is None:
                        request.pop("declared_non_claims", None)
                    elif mode == []:
                        request["declared_non_claims"] = []
                    elif mode == "missing_key":
                        request["declared_non_claims"].pop(
                            resolver.REQUIRED_FALSE_NON_CLAIMS[0], None
                        )
                    elif mode == "non_bool":
                        request["declared_non_claims"][
                            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                        ] = "false"
                    result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                        request
                    )
                    self.assert_blocked_with_public_code(
                        result, "NON_CLAIM_MISSING_OR_FLIPPED"
                    )

    def test_raw_markdown_body_containment(self) -> None:
        sentinels = (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        extra = "\n".join(sentinels)
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.synthetic_basis_files(Path(tmp), extra_text=extra)
            request = self.valid_request(paths)
            original = copy.deepcopy(request)
            request["raw_body"] = sentinels[0]
            request["hidden_repo_state"] = sentinels[1]
            request["future_operation_shape"]["hidden_repo_state"] = sentinels[2]
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        if result["outcome"] == resolver.OUTCOME_BLOCKED:
            self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_no_raw_full_markdown_body(result, sentinels)
        serialized = json.dumps(result, sort_keys=True)
        self.assertIn(resolver.BOUNDARY_TYPE, serialized)
        self.assertIn(resolver.FUTURE_OPERATION_TYPE, serialized)
        self.assert_canonical_false_non_claims(result)
        self.assert_no_overreach(result)
        self.assertEqual(
            original["descendant_body_differentiation_operation_boundary_id"],
            request["descendant_body_differentiation_operation_boundary_id"],
        )

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            paths = self.synthetic_basis_files(base)
            request = self.valid_request(paths)
            request_path = base / "requests" / "valid_request.json"
            self._write_json(request_path, request)
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path(
                request_path
            )
            self.assert_recorded_common(result)

            missing_result = (
                resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path(
                    base / "missing" / "request.json"
                )
            )
            self.assert_blocked_with_public_code(missing_result)

            malformed_path = base / "requests" / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path(
                    malformed_path
                )
            )
            self.assert_blocked_with_public_code(malformed_result)

            array_path = base / "requests" / "array.json"
            self._write_json(array_path, [])
            array_result = (
                resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min_from_path(
                    array_path
                )
            )
            self.assert_blocked_with_public_code(array_result)

            output_root = base / "writes" / "descendant_body_differentiation_operation_boundary_v0_min"
            first_path = resolver.write_descendant_body_differentiation_operation_boundary_v0_min_result(
                result, output_root
            )
            second_path = resolver.write_descendant_body_differentiation_operation_boundary_v0_min_result(
                result, output_root
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn(
                "descendant_body_differentiation_operation_boundary_v0_min_result",
                first_path.name,
            )
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_roots = (
                "integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min",
                "integrity_host_v0_min_coexistence_existence_claim_evidence_requirement_boundary_v0_min",
                "integrity_host_v0_min_coexistence_descendant_body_basis",
                "integrity_host_v0_min_coexistence_local_relevance_medium",
                "integrity_host_v0_min_coexistence_source_transfer",
                "integrity_host_v0_min_coexistence_source_receipt",
                "integrity_host_v0_min_coexistence_public_api",
                "integrity_host_v0_min_coexistence_participant_facing_interface",
                "integrity_host_v0_min_coexistence_distributed_network",
                "integrity_host_v0_min_coexistence_runtime_hosting",
                "integrity_host_v0_min_coexistence_runtime_loop",
                "integrity_host_v0_min_coexistence_daemon",
            )
            path_text = str(first_path)
            for forbidden in forbidden_roots:
                self.assertNotIn(forbidden, path_text)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            paths = self.synthetic_basis_files(base, extra_text="HIDDEN_PAYLOAD")
            request = self.valid_request(paths)
            request["declared_non_claims"] = dict(request["declared_non_claims"])
            request["future_operation_shape"] = dict(request["future_operation_shape"])
            before_request = copy.deepcopy(request)
            before_files = {
                key: path.read_text(encoding="utf-8")
                if path.suffix != ".json"
                else path.read_text(encoding="utf-8")
                for key, path in paths.items()
            }
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )
            after_files = {
                key: path.read_text(encoding="utf-8")
                if path.suffix != ".json"
                else path.read_text(encoding="utf-8")
                for key, path in paths.items()
            }
        self.assert_recorded_common(result)
        self.assertEqual(request, before_request)
        self.assertEqual(before_files, after_files)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                self.valid_request(self.synthetic_basis_files(Path(tmp)))
            )
        self.assert_recorded_common(result)
        summary = self.summary(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            summary["boundary_id"],
            "descendant_body_differentiation_operation_boundary_001",
        )
        self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(summary["future_operation_type"], resolver.FUTURE_OPERATION_TYPE)
        self.assertEqual(summary["future_operation_scope"], resolver.FUTURE_OPERATION_SCOPE)
        self.assertEqual(
            summary["future_candidate_record_policy"],
            resolver.FUTURE_CANDIDATE_RECORD_POLICY,
        )
        self.assertEqual(
            summary["future_failure_visibility_policy"],
            resolver.FUTURE_FAILURE_VISIBILITY_POLICY,
        )
        for key in (
            "boundary_recorded",
            "boundary_created",
            "operation_created_false",
            "operation_performed_false",
            "operation_recorded_false",
            "candidate_records_created_false",
            "descendant_bodies_created_false",
            "prior_unsupported_claims_validated_false",
            "affected_file_repaired_false",
            "affected_file_edited_false",
            "affected_file_deleted_false",
            "affected_file_overwritten_false",
            "affected_file_replaced_false",
            "affected_file_redeemed_false",
            "affected_file_treated_as_clean_basis_false",
            "contaminated_lineage_treated_as_clean_basis_false",
            "evidence_check_overridden_false",
            "evidence_check_bypassed_false",
            "scan_allowed_false",
            "repair_allowed_false",
            "validation_enforcement_allowed_false",
            "standing_authorized_false",
            "crossing_authorized_false",
            "relation_authorized_false",
            "field_machinery_authorized_false",
            "runtime_authorized_false",
            "currentness_authorized_false",
            "authority_authorized_false",
            "output_authorized_false",
            "action_authorized_false",
            "derivative_reception_authorized_false",
            "synchronization_authorized_false",
            "follow_on_authorized_false",
            "scan_not_performed",
            "repository_scan_not_performed",
            "repair_not_performed",
            "validation_not_enforced",
            "hidden_repair_not_performed",
            "silent_overwrite_not_performed",
            "boundary_spec_markers_present",
            "contaminated_lineage_markers_present",
            "evidence_check_terminal_summary_markers_present",
            "evidence_check_artifact_markers_present",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIs(summary[key], True, key)

    def test_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request = self.valid_request(self.synthetic_basis_files(Path(tmp)))
            result = resolver.resolve_descendant_body_differentiation_operation_boundary_v0_min(
                request
            )
            summary = resolver.build_descendant_body_differentiation_operation_boundary_v0_min_summary(
                result
            )
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["boundary_type"],
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY",
        )
        self.assertEqual(
            boundary["future_operation_type"],
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
        )
        self.assertEqual(
            boundary["future_operation_scope"],
            "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
        )
        self.assertEqual(
            boundary["future_candidate_record_policy"],
            "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS",
        )
        self.assertEqual(
            boundary["future_failure_visibility_policy"],
            "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL",
        )
        self.assert_recorded_boundary_posture(result)
        self.assert_no_overreach(result)
        self.assert_boundary_object_not_wrapper(result)
        self.assert_canonical_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
