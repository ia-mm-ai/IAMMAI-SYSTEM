"""Tests for one descendant-body differentiation operation resolver.

This suite exercises one operation result only. It verifies that the resolver
records a DESCENDANT_BODY_DIFFERENTIATION_OPERATION result, emits exactly two
result-contained non-standing candidate records when requirements pass, and
preserves that those records are not descendant bodies, not standing, not
crossing/relation/FIELD/runtime/currentness/authority/output/action/sync
authorization, not repair, and not validation of the prior unsupported claims.
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

import resolve_descendant_body_differentiation_operation_v0_min as resolver


OPERATION_SPEC_MARKERS = (
    "Descendant Body Differentiation Operation V0 Minimum Specification",
    "This file defines one future descendant-body differentiation operation.",
    "This file does not implement the operation.",
    "This file does not perform the operation.",
    "Candidate records are future result-contained records only.",
    "This spec does not create the candidate records.",
    "candidate_record_id = descendant_body_basis_candidate_a_001",
    "candidate_record_id = descendant_body_basis_candidate_b_001",
    "candidate_record_created_by_operation = true",
    "candidate_record_standing = false",
    "descendant_body_created = false",
    "inherited_from_contaminated_lineage = false",
    "prior_unsupported_claim_validated = false",
    "operation_implemented = false",
    "operation_recorded = false",
    "candidate_records_created = false",
)

CONTAMINATED_MARKERS = (
    "descendant_body_basis_candidate_a_created = true",
    "descendant_body_basis_candidate_b_created = true",
    "descendant_body_basis_derivation_event_recorded = true",
)

EVIDENCE_SUMMARY_MARKERS = (
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_RECORDED",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_CONTAMINATED_CLASS",
    "descendant_body_basis_candidate_a_created = UNSUPPORTED",
    "descendant_body_basis_candidate_b_created = UNSUPPORTED",
    "descendant_body_basis_derivation_event_recorded = UNSUPPORTED",
    "Contaminated lineage is not clean basis",
)

BOUNDARY_SUMMARY_MARKERS = (
    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED",
    "failed_check_count = 0",
    "passed_check_count = 179",
    "future_operation_type = DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
    "future_operation_scope = ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
    (
        "future_candidate_record_policy = "
        "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS"
    ),
    (
        "future_failure_visibility_policy = "
        "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL"
    ),
    "future_operation_not_created = true",
    "candidate_records_not_created = true",
    "descendant_bodies_not_created = true",
)

WRAPPER_FIELDS = {
    "outcome",
    "block",
    "descendant_body_differentiation_operation_checks",
    "non_claims",
    "descendant_body_differentiation_operation_summary",
    "descendant_body_differentiation_operation_metadata",
    "descendant_body_differentiation_candidate_records",
}

FALSE_OPERATION_KEYS = (
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_basis_candidate_a_created",
    "descendant_body_basis_candidate_b_created",
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
    "output_authorized_result",
    "action_authorized_result",
    "derivative_reception_authorized_result",
    "synchronization_authorized_result",
    "follow_on_work_authorized",
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
    "boundary_overridden",
    "boundary_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
)

DEFAULT_LIVE_PATHS = (
    REPO_ROOT / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_V0_MIN_SPEC.md",
    REPO_ROOT
    / "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
    REPO_ROOT / "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md",
    REPO_ROOT / "spec/DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_existence_claim_evidence_check_v0_min"
    / "existence_claim_evidence_check_001__existence_claim_evidence_check_v0_min_result.json",
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_descendant_body_differentiation_operation_boundary_v0_min"
    / "descendant_body_differentiation_operation_boundary_001__descendant_body_differentiation_operation_boundary_v0_min_result.json",
)


class DescendantBodyDifferentiationOperationTests(unittest.TestCase):
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

    def marker_text(
        self,
        title: str,
        markers: tuple[str, ...],
        *,
        remove: str | None = None,
        extra: str = "",
    ) -> str:
        lines = [f"# {title}", ""]
        for marker in markers:
            if marker == remove:
                lines.append("- marker intentionally omitted for blocking test")
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
            if key == "outcome":
                artifact[key] = value
            elif key == "claim_outcome":
                artifact["existence_claim_evidence_check_per_claim_outcomes"][0][
                    "per_claim_outcome"
                ] = value
            else:
                artifact["existence_claim_evidence_check_summary"][key] = value
        return artifact

    def boundary_artifact(self, **overrides: Any) -> dict[str, Any]:
        artifact: dict[str, Any] = {
            "outcome": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY_RECORDED",
            "descendant_body_differentiation_operation_boundary_summary": {
                "failed_check_count": 0,
                "boundary_type": "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BOUNDARY",
                "future_operation_type": resolver.OPERATION_TYPE,
                "future_operation_scope": resolver.OPERATION_SCOPE,
                "future_candidate_record_policy": resolver.CANDIDATE_RECORD_POLICY,
                "future_failure_visibility_policy": resolver.FAILURE_VISIBILITY_POLICY,
            },
            "descendant_body_differentiation_operation_boundary": {
                "boundary_created": True,
                "future_operation_not_created": True,
                "candidate_records_not_created": True,
                "descendant_bodies_not_created": True,
                "operation_created": False,
                "operation_performed": False,
                "operation_recorded": False,
                "differentiation_performed": False,
                "candidate_records_created": False,
            },
        }
        for key, value in overrides.items():
            if key == "outcome":
                artifact[key] = value
            elif key in artifact["descendant_body_differentiation_operation_boundary_summary"]:
                artifact["descendant_body_differentiation_operation_boundary_summary"][
                    key
                ] = value
            else:
                artifact["descendant_body_differentiation_operation_boundary"][
                    key
                ] = value
        return artifact

    def synthetic_basis_files(
        self,
        base: Path,
        *,
        remove_marker: tuple[str, str] | None = None,
        evidence_overrides: Mapping[str, Any] | None = None,
        boundary_overrides: Mapping[str, Any] | None = None,
        extra_text: str = "",
    ) -> dict[str, Path]:
        remove_marker = remove_marker or ("", "")
        paths = {
            "operation_spec_reference": base / "basis" / "operation_spec.md",
            "contaminated_lineage_reference": base / "basis" / "contaminated.md",
            "evidence_check_terminal_summary_reference": (
                base / "basis" / "evidence_summary.md"
            ),
            "evidence_check_artifact_reference": (
                base / "basis" / "evidence_artifact.json"
            ),
            "differentiation_operation_boundary_reference": (
                base / "basis" / "boundary_summary.md"
            ),
            "differentiation_operation_boundary_artifact_reference": (
                base / "basis" / "boundary_artifact.json"
            ),
        }
        self._write_text(
            paths["operation_spec_reference"],
            self.marker_text(
                "Synthetic Operation Spec",
                OPERATION_SPEC_MARKERS,
                remove=remove_marker[1] if remove_marker[0] == "operation" else None,
                extra=extra_text,
            ),
        )
        self._write_text(
            paths["contaminated_lineage_reference"],
            self.marker_text(
                "Synthetic Contaminated Lineage",
                CONTAMINATED_MARKERS,
                remove=remove_marker[1] if remove_marker[0] == "contaminated" else None,
                extra=extra_text,
            ),
        )
        self._write_text(
            paths["evidence_check_terminal_summary_reference"],
            self.marker_text(
                "Synthetic Evidence Summary",
                EVIDENCE_SUMMARY_MARKERS,
                remove=remove_marker[1] if remove_marker[0] == "evidence_summary" else None,
                extra=extra_text,
            ),
        )
        self._write_text(
            paths["differentiation_operation_boundary_reference"],
            self.marker_text(
                "Synthetic Boundary Summary",
                BOUNDARY_SUMMARY_MARKERS,
                remove=remove_marker[1] if remove_marker[0] == "boundary_summary" else None,
                extra=extra_text,
            ),
        )
        self._write_json(
            paths["evidence_check_artifact_reference"],
            self.evidence_artifact(**dict(evidence_overrides or {})),
        )
        self._write_json(
            paths["differentiation_operation_boundary_artifact_reference"],
            self.boundary_artifact(**dict(boundary_overrides or {})),
        )
        return paths

    def valid_request(self, paths: Mapping[str, Path]) -> dict[str, Any]:
        return resolver.build_declared_descendant_body_differentiation_operation_v0_min_request(
            descendant_body_differentiation_operation_id=(
                "descendant_body_differentiation_operation_001"
            ),
            operation_spec_reference=str(paths["operation_spec_reference"]),
            contaminated_lineage_reference=str(paths["contaminated_lineage_reference"]),
            evidence_check_terminal_summary_reference=str(
                paths["evidence_check_terminal_summary_reference"]
            ),
            evidence_check_artifact_reference=str(
                paths["evidence_check_artifact_reference"]
            ),
            differentiation_operation_boundary_reference=str(
                paths["differentiation_operation_boundary_reference"]
            ),
            differentiation_operation_boundary_artifact_reference=str(
                paths["differentiation_operation_boundary_artifact_reference"]
            ),
            evidence_requirement_boundary_reference=(
                "synthetic-evidence-requirement-boundary"
            ),
        )

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block") or {}
        if not isinstance(block, Mapping):
            return None
        return block.get("code") or block.get("block_code")

    def checks(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        checks = result.get("descendant_body_differentiation_operation_checks")
        self.assertIsInstance(checks, list)
        return checks

    def operation(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        operation = result.get("descendant_body_differentiation_operation")
        self.assertIsInstance(operation, dict)
        return operation

    def records(self, result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
        records = result.get("descendant_body_differentiation_candidate_records")
        self.assertIsInstance(records, list)
        return records

    def summary(self, result: Mapping[str, Any]) -> Mapping[str, Any]:
        summary = result.get("descendant_body_differentiation_operation_summary")
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

    def assert_operation_not_wrapper(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def assert_no_created_overreach(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in FALSE_OPERATION_KEYS:
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)

    def assert_candidate_records(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        records = self.records(result)
        self.assertEqual(len(records), 2)
        by_id = {record.get("candidate_record_id"): record for record in records}
        self.assertEqual(set(by_id), {resolver.CANDIDATE_A_ID, resolver.CANDIDATE_B_ID})
        self.assertEqual(by_id[resolver.CANDIDATE_A_ID]["candidate_role"], resolver.CANDIDATE_A_ROLE)
        self.assertEqual(by_id[resolver.CANDIDATE_B_ID]["candidate_role"], resolver.CANDIDATE_B_ROLE)
        self.assertEqual(
            len({record["candidate_role"] for record in records}),
            2,
        )
        for record in records:
            self.assertEqual(record["candidate_record_type"], resolver.CANDIDATE_RECORD_TYPE)
            self.assertIs(record["candidate_record_created_by_operation"], True)
            self.assertIs(record["candidate_record_standing"], False)
            self.assertIs(record["descendant_body_created"], False)
            self.assertEqual(
                record["source_body_proof_basis_reference"],
                operation["source_body_proof_basis_reference"],
            )
            self.assertEqual(record["operation_id"], operation["operation_id"])
            self.assertEqual(
                record["operation_evidence_reference"],
                operation["operation_id"],
            )
            self.assertEqual(
                record["operation_evidence_kind"],
                "descendant_body_differentiation_operation_result",
            )
            self.assertEqual(
                record["contaminated_lineage_reference"],
                operation["contaminated_lineage_reference"],
            )
            for key in (
                "inherited_from_contaminated_lineage",
                "prior_unsupported_claim_validated",
                "crossing_authorized",
                "relation_authorized",
                "field_machinery_authorized",
                "runtime_authorized",
                "currentness_authorized",
                "authority_authorized",
                "standing_created",
                "output_authorized",
                "action_authorized",
                "derivative_reception_authorized",
                "synchronization_authorized",
                "follow_on_authorized",
            ):
                self.assertIs(record[key], False, key)
        self.assertEqual(operation["candidate_record_count_emitted"], 2)
        self.assertEqual(set(operation["candidate_record_ids"]), set(by_id))
        self.assertIs(operation["exactly_two_candidate_records_emitted"], True)
        self.assertIs(operation["candidate_records_have_operation_evidence"], True)
        self.assertIs(operation["candidate_records_non_standing"], True)
        self.assertIs(
            operation["candidate_records_do_not_inherit_from_contaminated_lineage"],
            True,
        )

    def assert_no_raw_full_markdown_body(
        self, result: Mapping[str, Any], sentinels: tuple[str, ...] = ()
    ) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for key in ("raw_body", "full_body", "markdown_body", "hidden_repo_state"):
            self.assertNotIn(f'"{key}": "RAW_', serialized)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)
        self.assertFalse(
            result.get("operation_basis", {})
            .get("operation_spec_reference", {})
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
        self.assertEqual(self.records(result), [])
        self.assert_canonical_false_non_claims(result)
        self.assert_operation_not_wrapper(result)
        self.assert_no_created_overreach(result)

    def assert_recorded_common(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertEqual(self.summary(result)["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)
        self.assert_canonical_false_non_claims(result)
        self.assert_operation_not_wrapper(result)
        self.assert_no_raw_full_markdown_body(result)

    def assert_recorded_operation_posture(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.RESULT_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(operation["candidate_record_policy"], resolver.CANDIDATE_RECORD_POLICY)
        self.assertEqual(operation["failure_visibility_policy"], resolver.FAILURE_VISIBILITY_POLICY)
        self.assertEqual(operation["differentiation_method"], resolver.DIFFERENTIATION_METHOD)
        for key in (
            "descendant_body_differentiation_operation_recorded",
            "operation_result_created",
            "operation_recorded",
            "differentiation_performed",
            "candidate_records_created",
            "exactly_two_candidate_records_emitted",
            "candidate_records_have_operation_evidence",
            "candidate_records_non_standing",
            "candidate_records_do_not_inherit_from_contaminated_lineage",
            "source_body_proof_basis_reference_declared",
            "contaminated_lineage_reference_declared",
            "evidence_requirement_boundary_reference_declared",
            "evidence_check_terminal_summary_reference_declared",
            "evidence_check_artifact_reference_declared",
            "differentiation_operation_boundary_reference_declared",
            "differentiation_operation_boundary_artifact_reference_declared",
            "operation_spec_reference_declared",
            "operation_spec_markers_present",
            "contaminated_lineage_markers_present",
            "evidence_check_terminal_summary_markers_present",
            "evidence_check_artifact_markers_present",
            "differentiation_operation_boundary_terminal_summary_markers_present",
            "differentiation_operation_boundary_artifact_markers_present",
            "prior_unsupported_claims_preserved",
            "contaminated_lineage_preserved",
            "evidence_check_not_overridden",
            "evidence_check_not_bypassed",
            "boundary_not_overridden",
            "boundary_not_bypassed",
        ):
            self.assertIs(operation[key], True, key)
        self.assertEqual(operation["candidate_record_count_emitted"], 2)
        self.assert_no_created_overreach(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_differentiation_operation_v0_min",
            "resolve_descendant_body_differentiation_operation_v0_min_from_path",
            "write_descendant_body_differentiation_operation_v0_min_result",
            "build_descendant_body_differentiation_operation_v0_min_summary",
            "build_declared_descendant_body_differentiation_operation_v0_min_request",
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
            "OPERATION_TYPE",
            "OPERATION_SCOPE",
            "CANDIDATE_RECORD_POLICY",
            "FAILURE_VISIBILITY_POLICY",
            "DIFFERENTIATION_METHOD",
            "CANDIDATE_RECORD_TYPE",
            "CANDIDATE_A_ID",
            "CANDIDATE_B_ID",
            "CANDIDATE_A_ROLE",
            "CANDIDATE_B_ROLE",
            "SUPPORTED_OPERATION_TYPE_VALUES",
            "SUPPORTED_OPERATION_SCOPE_VALUES",
            "SUPPORTED_CANDIDATE_RECORD_POLICY_VALUES",
            "SUPPORTED_FAILURE_VISIBILITY_POLICY_VALUES",
            "SUPPORTED_DIFFERENTIATION_METHOD_VALUES",
            "REQUIRED_FALSE_NON_CLAIMS",
            "ALLOWED_TRUE_RECORDED_FIELDS",
            "OUTPUT_ROOT",
            "BLOCK_CODES",
        ):
            self.assertTrue(hasattr(resolver, name), name)

        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_differentiation_operation_v0_min",
        )
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_DIFFERENTIATION_OPERATION")
        self.assertEqual(resolver.OPERATION_SCOPE, "ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY")
        self.assertEqual(
            resolver.CANDIDATE_RECORD_POLICY,
            "EMIT_CANDIDATE_RECORDS_ONLY_IF_OPERATION_EVIDENCE_EXISTS",
        )
        self.assertEqual(
            resolver.FAILURE_VISIBILITY_POLICY,
            "BLOCK_WITH_VISIBLE_REASON_IF_REQUIREMENTS_FAIL",
        )
        self.assertEqual(
            resolver.DIFFERENTIATION_METHOD,
            "DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION",
        )
        self.assertEqual(
            resolver.CANDIDATE_RECORD_TYPE,
            "NON_STANDING_DESCENDANT_BODY_BASIS_CANDIDATE",
        )
        self.assertEqual(resolver.CANDIDATE_A_ID, "descendant_body_basis_candidate_a_001")
        self.assertEqual(resolver.CANDIDATE_B_ID, "descendant_body_basis_candidate_b_001")
        self.assertEqual(resolver.CANDIDATE_A_ROLE, "CANDIDATE_A")
        self.assertEqual(resolver.CANDIDATE_B_ROLE, "CANDIDATE_B")
        for outcome in (
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_NOT_RECORDED,
        ):
            self.assertIn(outcome, resolver.OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_"
                "descendant_body_differentiation_operation_v0_min"
            )
        )
        for key in FALSE_OPERATION_KEYS:
            self.assertIn(key, resolver.REQUIRED_FALSE_NON_CLAIMS)
        for key in (
            "descendant_body_differentiation_operation_recorded",
            "operation_result_created",
            "operation_recorded",
            "differentiation_performed",
            "candidate_records_created",
            "exactly_two_candidate_records_emitted",
            "candidate_records_have_operation_evidence",
            "candidate_records_non_standing",
            "candidate_records_do_not_inherit_from_contaminated_lineage",
            "source_body_proof_basis_reference_declared",
            "contaminated_lineage_reference_declared",
            "evidence_check_terminal_summary_reference_declared",
            "evidence_check_artifact_reference_declared",
            "differentiation_operation_boundary_reference_declared",
            "differentiation_operation_boundary_artifact_reference_declared",
            "operation_spec_markers_present",
            "contaminated_lineage_markers_present",
            "evidence_check_terminal_summary_markers_present",
            "evidence_check_artifact_markers_present",
            "differentiation_operation_boundary_terminal_summary_markers_present",
            "differentiation_operation_boundary_artifact_markers_present",
            "prior_unsupported_claims_preserved",
            "contaminated_lineage_preserved",
            "evidence_check_not_overridden",
            "evidence_check_not_bypassed",
            "boundary_not_overridden",
            "boundary_not_bypassed",
            "result_level_non_claims_canonical_false",
        ):
            self.assertIn(key, resolver.ALLOWED_TRUE_RECORDED_FIELDS)
        for code in (
            "OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION",
            "OPERATION_VERSION_NOT_0_1_0",
            "OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY",
            "CANDIDATE_RECORD_COUNT_NOT_TWO",
            "CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED",
            "FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK",
            "DIFFERENTIATION_METHOD_NOT_DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION",
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
            "OPERATION_SPEC_MARKER_MISSING",
            "CONTAMINATED_LINEAGE_MARKER_MISSING",
            "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING",
            "DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
            "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING",
            "DESCENDANT_BODY_A_CREATED",
            "DESCENDANT_BODY_B_CREATED",
            "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
            "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
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
            "EVIDENCE_CHECK_OVERRIDDEN",
            "EVIDENCE_CHECK_BYPASSED",
            "BOUNDARY_OVERRIDDEN",
            "BOUNDARY_BYPASSED",
            "SCAN_PERFORMED",
            "REPOSITORY_SCAN_PERFORMED",
            "REPAIR_PERFORMED",
            "VALIDATION_ENFORCED",
            "HIDDEN_REPAIR_PERFORMED",
            "SILENT_OVERWRITE_PERFORMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_records_operation_and_two_non_standing_candidate_records_from_synthetic_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.synthetic_basis_files(Path(temp_dir))
            request = self.valid_request(paths)
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)

            self.assert_recorded_common(result)
            self.assert_recorded_operation_posture(result)
            self.assert_candidate_records(result)
            self.assertEqual(self.operation(result)["operation_id"], "descendant_body_differentiation_operation_001")
            for key in (
                "descendant_body_differentiation_operation_metadata",
                "declared_descendant_body_differentiation_operation_question",
                "upstream_basis",
                "operation_basis",
                "descendant_body_differentiation_operation",
                "descendant_body_differentiation_candidate_records",
                "descendant_body_differentiation_operation_checks",
                "descendant_body_differentiation_operation_statement",
                "descendant_body_differentiation_operation_non_meaning",
                "additional_basis_required",
                "not_recorded_basis",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "descendant_body_differentiation_operation_summary",
            ):
                self.assertIn(key, result)

    def test_records_default_live_target_if_present(self) -> None:
        missing = [str(path) for path in DEFAULT_LIVE_PATHS if not path.exists()]
        if missing:
            self.skipTest(f"default live basis missing: {missing[0]}")
        request = resolver.build_declared_descendant_body_differentiation_operation_v0_min_request()
        result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
        self.assert_recorded_common(result)
        self.assert_recorded_operation_posture(result)
        self.assert_candidate_records(result)

    def test_do_not_record_intent_does_not_emit_candidate_records(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(self.synthetic_basis_files(Path(temp_dir)))
            request["descendant_body_differentiation_operation_intent"] = (
                "DO_NOT_RECORD_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
            )
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
            operation = self.operation(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            self.assertEqual(self.records(result), [])
            self.assertIs(operation["operation_result_created"], False)
            self.assertIs(operation["operation_recorded"], False)
            self.assertIs(operation["differentiation_performed"], False)
            self.assertIs(operation["candidate_records_created"], False)
            self.assertEqual(operation["candidate_record_count_emitted"], 0)
            self.assert_canonical_false_non_claims(result)
            self.assert_no_created_overreach(result)

    def test_block_intent_blocks_and_emits_no_candidate_records(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(self.synthetic_basis_files(Path(temp_dir)))
            request["descendant_body_differentiation_operation_intent"] = (
                "BLOCK_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"
            )
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
            self.assert_blocked_with_public_code(
                result,
                "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_BLOCK_REQUESTED",
            )

    def test_request_shape_and_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.synthetic_basis_files(Path(temp_dir))
            base = self.valid_request(paths)
            cases: list[tuple[str, Any, str | None]] = [
                ("non_mapping", "not-a-mapping", "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_MALFORMED"),
                ("missing_question", {"descendant_body_differentiation_operation_question": None}, "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_QUESTION_UNDECLARED"),
                ("unsupported_intent", {"descendant_body_differentiation_operation_intent": "NOPE"}, "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_INTENT_UNSUPPORTED"),
                ("missing_operation_type", {"operation_type": None}, "OPERATION_TYPE_MISSING"),
                ("wrong_operation_type", {"operation_type": "WRONG"}, "OPERATION_TYPE_NOT_DESCENDANT_BODY_DIFFERENTIATION_OPERATION"),
                ("missing_operation_version", {"operation_version": None}, "OPERATION_VERSION_MISSING"),
                ("wrong_operation_version", {"operation_version": "9.9.9"}, "OPERATION_VERSION_NOT_0_1_0"),
                ("missing_operation_scope", {"operation_scope": None}, "OPERATION_SCOPE_MISSING"),
                ("wrong_operation_scope", {"operation_scope": "WRONG"}, "OPERATION_SCOPE_NOT_ONE_STANDING_BODY_PROOF_BASIS_DECLARED_ONLY"),
                ("missing_source_ref", {"source_body_proof_basis_reference": ""}, "SOURCE_BODY_PROOF_BASIS_REFERENCE_MISSING"),
                ("missing_contaminated_ref", {"contaminated_lineage_reference": ""}, "CONTAMINATED_LINEAGE_REFERENCE_MISSING"),
                ("missing_evidence_requirement_ref", {"evidence_requirement_boundary_reference": ""}, "EVIDENCE_REQUIREMENT_BOUNDARY_REFERENCE_MISSING"),
                ("missing_evidence_summary_ref", {"evidence_check_terminal_summary_reference": ""}, "EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING"),
                ("missing_evidence_artifact_ref", {"evidence_check_artifact_reference": ""}, "EVIDENCE_CHECK_ARTIFACT_REFERENCE_MISSING"),
                ("missing_boundary_summary_ref", {"differentiation_operation_boundary_reference": ""}, "DIFFERENTIATION_OPERATION_BOUNDARY_REFERENCE_MISSING"),
                ("missing_boundary_artifact_ref", {"differentiation_operation_boundary_artifact_reference": ""}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_REFERENCE_MISSING"),
                ("missing_operation_spec_ref", {"operation_spec_reference": ""}, "OPERATION_SPEC_REFERENCE_MISSING"),
                ("bad_candidate_count", {"candidate_record_count_requested": 3}, "CANDIDATE_RECORD_COUNT_NOT_TWO"),
                ("missing_candidate_policy", {"candidate_record_policy": ""}, "CANDIDATE_RECORD_POLICY_MISSING"),
                ("wrong_candidate_policy", {"candidate_record_policy": "WRONG"}, "CANDIDATE_RECORD_POLICY_NOT_EVIDENCE_GATED"),
                ("missing_failure_policy", {"failure_visibility_policy": ""}, "FAILURE_VISIBILITY_POLICY_MISSING"),
                ("wrong_failure_policy", {"failure_visibility_policy": "WRONG"}, "FAILURE_VISIBILITY_POLICY_NOT_VISIBLE_BLOCK"),
                ("missing_method", {"differentiation_method": ""}, "DIFFERENTIATION_METHOD_MISSING"),
                ("wrong_method", {"differentiation_method": "WRONG"}, "DIFFERENTIATION_METHOD_NOT_DECLARED_BASIS_DUAL_CANDIDATE_DIFFERENTIATION"),
                ("scan_allowed", {"scan_allowed": True}, "SCAN_ALLOWED_TRUE"),
                ("repair_allowed", {"repair_allowed": True}, "REPAIR_ALLOWED_TRUE"),
                ("validation_allowed", {"validation_enforcement_allowed": True}, "VALIDATION_ENFORCEMENT_ALLOWED_TRUE"),
                ("standing_authorized", {"standing_authorized": True}, "STANDING_AUTHORIZED_TRUE"),
                ("crossing_authorized", {"crossing_authorized": True}, "CROSSING_AUTHORIZED_TRUE"),
                ("relation_authorized", {"relation_authorized": True}, "RELATION_AUTHORIZED_TRUE"),
                ("field_authorized", {"field_machinery_authorized": True}, "FIELD_MACHINERY_AUTHORIZED_TRUE"),
                ("runtime_authorized", {"runtime_authorized": True}, "RUNTIME_AUTHORIZED_TRUE"),
                ("currentness_authorized", {"currentness_authorized": True}, "CURRENTNESS_AUTHORIZED_TRUE"),
                ("authority_authorized", {"authority_authorized": True}, "AUTHORITY_AUTHORIZED_TRUE"),
                ("output_authorized", {"output_authorized": True}, "OUTPUT_AUTHORIZED_TRUE"),
                ("action_authorized", {"action_authorized": True}, "ACTION_AUTHORIZED_TRUE"),
                ("derivative_authorized", {"derivative_reception_authorized": True}, "DERIVATIVE_RECEPTION_AUTHORIZED_TRUE"),
                ("sync_authorized", {"synchronization_authorized": True}, "SYNCHRONIZATION_AUTHORIZED_TRUE"),
                ("follow_on_authorized", {"follow_on_authorized": True}, "FOLLOW_ON_AUTHORIZED_TRUE"),
                ("requested_repository_scan", {"requested_repository_scan": True, "request_repository_scan": True}, "REQUESTED_REPOSITORY_SCAN"),
                ("requested_file_discovery", {"requested_file_discovery": True, "request_file_discovery": True}, "REQUESTED_FILE_DISCOVERY"),
                ("requested_repair", {"requested_affected_file_repair": True, "request_affected_file_repair": True}, "REQUESTED_AFFECTED_FILE_REPAIR"),
                ("requested_mutation", {"requested_affected_file_mutation": True, "request_affected_file_mutation": True}, "REQUESTED_AFFECTED_FILE_MUTATION"),
                ("requested_claim_validation", {"requested_prior_unsupported_claim_validation": True, "request_prior_unsupported_claim_validation": True}, "REQUESTED_PRIOR_UNSUPPORTED_CLAIM_VALIDATION"),
                ("requested_evidence_override", {"requested_evidence_check_override": True, "request_evidence_check_override": True}, "REQUESTED_EVIDENCE_CHECK_OVERRIDE"),
                ("requested_evidence_bypass", {"requested_evidence_check_bypass": True, "request_evidence_check_bypass": True}, "REQUESTED_EVIDENCE_CHECK_BYPASS"),
                ("requested_boundary_override", {"requested_boundary_override": True, "request_boundary_override": True}, "REQUESTED_BOUNDARY_OVERRIDE"),
                ("requested_boundary_bypass", {"requested_boundary_bypass": True, "request_boundary_bypass": True}, "REQUESTED_BOUNDARY_BYPASS"),
                ("requested_body_creation", {"requested_descendant_body_creation": True, "request_descendant_body_creation": True}, "REQUESTED_DESCENDANT_BODY_CREATION"),
                ("requested_standing_descendant", {"requested_standing_descendant_creation": True, "request_standing_descendant_creation": True}, "REQUESTED_STANDING_DESCENDANT_CREATION"),
                ("requested_standing_check", {"requested_descendant_standing_check": True, "request_descendant_standing_check": True}, "REQUESTED_DESCENDANT_STANDING_CHECK"),
                ("requested_crossing", {"requested_crossing_authorization": True, "request_crossing_authorization": True}, "REQUESTED_CROSSING_AUTHORIZATION"),
                ("requested_relation", {"requested_relation_creation": True, "request_relation_creation": True}, "REQUESTED_RELATION_CREATION"),
                ("requested_field", {"requested_field_machinery_creation": True, "request_field_machinery_creation": True}, "REQUESTED_FIELD_MACHINERY_CREATION"),
                ("requested_runtime", {"requested_runtime_creation": True, "request_runtime_creation": True}, "REQUESTED_RUNTIME_CREATION"),
                ("requested_currentness", {"requested_currentness_creation": True, "request_currentness_creation": True}, "REQUESTED_CURRENTNESS_CREATION"),
                ("requested_authority", {"requested_authority_creation": True, "request_authority_creation": True}, "REQUESTED_AUTHORITY_CREATION"),
                ("requested_output", {"requested_output_authorization": True, "request_output_authorization": True}, "REQUESTED_OUTPUT_AUTHORIZATION"),
                ("requested_action", {"requested_action_authorization": True, "request_action_authorization": True}, "REQUESTED_ACTION_AUTHORIZATION"),
                ("requested_derivative", {"requested_derivative_reception_authorization": True, "request_derivative_reception_authorization": True}, "REQUESTED_DERIVATIVE_RECEPTION_AUTHORIZATION"),
                ("requested_sync", {"requested_synchronization_authorization": True, "request_synchronization_authorization": True}, "REQUESTED_SYNCHRONIZATION_AUTHORIZATION"),
                ("requested_follow_on", {"requested_follow_on_authorization": True, "request_follow_on_authorization": True}, "REQUESTED_FOLLOW_ON_AUTHORIZATION"),
                ("requested_raw_markdown", {"requested_raw_markdown_body_return": True, "return_raw_markdown_body": True}, "REQUESTED_RAW_MARKDOWN_BODY_RETURN"),
            ]
            for index, (name, mutation, expected_code) in enumerate(cases):
                with self.subTest(name=name):
                    if isinstance(mutation, Mapping):
                        request = copy.deepcopy(base)
                        request.update(mutation)
                        result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
                    else:
                        result = resolver.resolve_descendant_body_differentiation_operation_v0_min(mutation)
                    self.assert_blocked_with_public_code(result, expected_code)

    def test_marker_validation_blocking_behavior(self) -> None:
        marker_cases: list[tuple[str, str, dict[str, Any] | None, dict[str, Any] | None, str]] = [
            ("operation_marker", "operation", None, None, "OPERATION_SPEC_MARKER_MISSING"),
            ("contaminated_marker", "contaminated", None, None, "CONTAMINATED_LINEAGE_MARKER_MISSING"),
            ("evidence_summary_marker", "evidence_summary", None, None, "EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("boundary_summary_marker", "boundary_summary", None, None, "DIFFERENTIATION_OPERATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"),
        ]
        artifact_cases: list[tuple[str, dict[str, Any] | None, dict[str, Any] | None, str]] = [
            ("evidence_outcome", {"outcome": "WRONG"}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_file_outcome", {"file_level_outcome": "WRONG"}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_failed_count", {"failed_check_count": 1}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_detected_count", {"detected_claim_count": 2}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_unsupported_count", {"unsupported_claim_count": 2}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_supported_count", {"evidence_supported_claim_count": 1}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("evidence_claim_outcome", {"claim_outcome": "EVIDENCE_SUPPORTED"}, None, "EVIDENCE_CHECK_ARTIFACT_MARKER_MISSING"),
            ("boundary_outcome", None, {"outcome": "WRONG"}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_failed_count", None, {"failed_check_count": 1}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_operation_type", None, {"future_operation_type": "WRONG"}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_operation_scope", None, {"future_operation_scope": "WRONG"}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_policy", None, {"future_candidate_record_policy": "WRONG"}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_failure_policy", None, {"future_failure_visibility_policy": "WRONG"}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("boundary_created", None, {"boundary_created": False}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("future_operation_not_created", None, {"future_operation_not_created": False}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("candidate_records_not_created", None, {"candidate_records_not_created": False}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("descendant_bodies_not_created", None, {"descendant_bodies_not_created": False}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("operation_created", None, {"operation_created": True}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("operation_recorded", None, {"operation_recorded": True}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
            ("candidate_records_created", None, {"candidate_records_created": True}, "DIFFERENTIATION_OPERATION_BOUNDARY_ARTIFACT_MARKER_MISSING"),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            for name, group, evidence_overrides, boundary_overrides, code in marker_cases:
                with self.subTest(name=name):
                    marker = {
                        "operation": OPERATION_SPEC_MARKERS[0],
                        "contaminated": CONTAMINATED_MARKERS[0],
                        "evidence_summary": EVIDENCE_SUMMARY_MARKERS[0],
                        "boundary_summary": BOUNDARY_SUMMARY_MARKERS[0],
                    }[group]
                    paths = self.synthetic_basis_files(
                        Path(temp_dir) / self.safe_json_filename(name),
                        remove_marker=(group, marker),
                    )
                    result = resolver.resolve_descendant_body_differentiation_operation_v0_min(
                        self.valid_request(paths)
                    )
                    self.assert_blocked_with_public_code(result, code)
            for name, evidence_overrides, boundary_overrides, code in artifact_cases:
                with self.subTest(name=name):
                    paths = self.synthetic_basis_files(
                        Path(temp_dir) / self.safe_json_filename(name),
                        evidence_overrides=evidence_overrides,
                        boundary_overrides=boundary_overrides,
                    )
                    result = resolver.resolve_descendant_body_differentiation_operation_v0_min(
                        self.valid_request(paths)
                    )
                    self.assert_blocked_with_public_code(result, code)

    def test_required_false_top_level_posture_blocks(self) -> None:
        cases = {
            "descendant_body_a_created": "DESCENDANT_BODY_A_CREATED",
            "descendant_body_b_created": "DESCENDANT_BODY_B_CREATED",
            "descendant_body_basis_candidate_a_created": "DESCENDANT_BODY_BASIS_CANDIDATE_A_CREATED",
            "descendant_body_basis_candidate_b_created": "DESCENDANT_BODY_BASIS_CANDIDATE_B_CREATED",
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
            "output_authorized_result": "OUTPUT_AUTHORIZED_RESULT",
            "action_authorized_result": "ACTION_AUTHORIZED_RESULT",
            "derivative_reception_authorized_result": "DERIVATIVE_RECEPTION_AUTHORIZED_RESULT",
            "synchronization_authorized_result": "SYNCHRONIZATION_AUTHORIZED_RESULT",
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
            "evidence_check_overridden": "EVIDENCE_CHECK_OVERRIDDEN",
            "evidence_check_bypassed": "EVIDENCE_CHECK_BYPASSED",
            "boundary_overridden": "BOUNDARY_OVERRIDDEN",
            "boundary_bypassed": "BOUNDARY_BYPASSED",
            "scan_performed": "SCAN_PERFORMED",
            "repository_scan_performed": "REPOSITORY_SCAN_PERFORMED",
            "repair_performed": "REPAIR_PERFORMED",
            "validation_enforced": "VALIDATION_ENFORCED",
            "hidden_repair_performed": "HIDDEN_REPAIR_PERFORMED",
            "silent_overwrite_performed": "SILENT_OVERWRITE_PERFORMED",
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.synthetic_basis_files(Path(temp_dir))
            base = self.valid_request(paths)
            for key, code in cases.items():
                with self.subTest(key=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, code)
                    self.assertIs(result["non_claims"][key], False)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.synthetic_basis_files(Path(temp_dir))
            base = self.valid_request(paths)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = (
                ("missing_mapping", None),
                ("non_mapping", []),
                ("missing_required_key", {k: False for k in resolver.REQUIRED_FALSE_NON_CLAIMS[:-1]}),
                ("non_bool_value", {**{k: False for k in resolver.REQUIRED_FALSE_NON_CLAIMS}, resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}),
            )
            for name, declared in malformed_cases:
                with self.subTest(name=name):
                    request = copy.deepcopy(base)
                    if declared is None:
                        request.pop("declared_non_claims", None)
                    else:
                        request["declared_non_claims"] = declared
                    result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result)
                    self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", resolver.BLOCK_CODES)

    def test_candidate_record_invariants(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(
                self.valid_request(self.synthetic_basis_files(Path(temp_dir)))
            )
            self.assert_recorded_common(result)
            self.assert_candidate_records(result)

    def test_raw_markdown_body_containment(self) -> None:
        sentinels = (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        request_copy: dict[str, Any]
        with tempfile.TemporaryDirectory() as temp_dir:
            extra = "\n".join(sentinels)
            paths = self.synthetic_basis_files(Path(temp_dir), extra_text=extra)
            request = self.valid_request(paths)
            request["raw_body"] = "RAW_MARKDOWN_BODY_MUST_NOT_RETURN"
            request["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request_copy = copy.deepcopy(request)
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
            self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
            if result["outcome"] == resolver.OUTCOME_BLOCKED:
                self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
            self.assert_no_raw_full_markdown_body(result, sentinels)
            serialized = json.dumps(result, sort_keys=True)
            self.assertIn(resolver.OPERATION_TYPE, serialized)
            self.assert_canonical_false_non_claims(result)
            self.assert_no_created_overreach(result)
            self.assertEqual(request, request_copy)

    def test_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            paths = self.synthetic_basis_files(base)
            request = self.valid_request(paths)
            request_path = base / "request.json"
            self._write_json(request_path, request)
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min_from_path(request_path)
            self.assert_recorded_common(result)
            self.assert_candidate_records(result)

            missing_result = resolver.resolve_descendant_body_differentiation_operation_v0_min_from_path(
                base / "missing.json"
            )
            self.assert_blocked_with_public_code(
                missing_result,
                "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_UNREADABLE",
            )
            malformed_path = base / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_descendant_body_differentiation_operation_v0_min_from_path(
                malformed_path
            )
            self.assert_blocked_with_public_code(
                malformed_result,
                "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_UNREADABLE",
            )
            array_path = base / "array.json"
            self._write_json(array_path, [])
            array_result = resolver.resolve_descendant_body_differentiation_operation_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(
                array_result,
                "DECLARED_DESCENDANT_BODY_DIFFERENTIATION_OPERATION_REQUEST_MALFORMED",
            )

            output_root = base / "write_root" / "descendant_body_differentiation_operation_v0_min"
            first_path = resolver.write_descendant_body_differentiation_operation_v0_min_result(
                result,
                output_root,
            )
            second_path = resolver.write_descendant_body_differentiation_operation_v0_min_result(
                result,
                output_root,
            )
            self.assertTrue(first_path.exists())
            self.assertTrue(second_path.exists())
            self.assertNotEqual(first_path, second_path)
            self.assertIn("descendant_body_differentiation_operation_v0_min_result", first_path.name)
            self.assertIn("descendant_body_differentiation_operation_v0_min", str(first_path))
            with first_path.open("r", encoding="utf-8") as handle:
                parsed = json.load(handle)
            self.assertEqual(parsed["outcome"], resolver.OUTCOME_RECORDED)
            forbidden_parts = (
                "operation_boundary_v0_min",
                "existence_claim_evidence_check_v0_min",
                "existence_claim_evidence_requirement_boundary",
                "descendant_body_basis",
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
            )
            path_parts = set(first_path.parts)
            for part in forbidden_parts:
                self.assertNotIn(part, path_parts)

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            paths = self.synthetic_basis_files(base, extra_text="RAW_MARKDOWN_BODY_MUST_NOT_RETURN")
            before_text = {
                key: path.read_text(encoding="utf-8")
                for key, path in paths.items()
                if path.suffix == ".md"
            }
            before_json = {
                key: json.loads(path.read_text(encoding="utf-8"))
                for key, path in paths.items()
                if path.suffix == ".json"
            }
            request = self.valid_request(paths)
            request["declared_non_claims"] = dict(request["declared_non_claims"])
            request_before = copy.deepcopy(request)
            resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
            self.assertEqual(request, request_before)
            for key, path in paths.items():
                if path.suffix == ".md":
                    self.assertEqual(path.read_text(encoding="utf-8"), before_text[key])
                if path.suffix == ".json":
                    self.assertEqual(json.loads(path.read_text(encoding="utf-8")), before_json[key])

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(
                self.valid_request(self.synthetic_basis_files(Path(temp_dir)))
            )
            self.assert_recorded_common(result)
            summary = self.summary(result)
            operation = self.operation(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["operation_id"], operation["operation_id"])
            self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(summary["operation_version"], resolver.RESULT_VERSION)
            self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(summary["candidate_record_policy"], resolver.CANDIDATE_RECORD_POLICY)
            self.assertEqual(summary["failure_visibility_policy"], resolver.FAILURE_VISIBILITY_POLICY)
            self.assertEqual(summary["differentiation_method"], resolver.DIFFERENTIATION_METHOD)
            for key in (
                "operation_recorded",
                "operation_result_created",
                "differentiation_performed",
                "candidate_records_created",
                "exactly_two_candidate_records_emitted",
                "candidate_records_have_operation_evidence",
                "candidate_records_non_standing",
                "candidate_records_do_not_inherit_from_contaminated_lineage",
                "operation_spec_markers_present",
                "contaminated_lineage_markers_present",
                "evidence_check_terminal_summary_markers_present",
                "evidence_check_artifact_markers_present",
                "differentiation_operation_boundary_terminal_summary_markers_present",
                "differentiation_operation_boundary_artifact_markers_present",
                "prior_unsupported_claims_preserved",
                "contaminated_lineage_preserved",
                "result_level_non_claims_canonical_false",
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
            ):
                self.assertIs(summary[key], True, key)
            self.assertEqual(summary["candidate_record_count_emitted"], 2)
            self.assertEqual(set(summary["candidate_record_ids"]), set(operation["candidate_record_ids"]))
            for key in (
                "descendant_bodies_created_false",
                "standing_descendants_created_false",
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
                "boundary_overridden_false",
                "boundary_bypassed_false",
            ):
                self.assertIs(summary[key], True, key)

    def test_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request = self.valid_request(self.synthetic_basis_files(Path(temp_dir)))
            result = resolver.resolve_descendant_body_differentiation_operation_v0_min(request)
            summary = resolver.build_descendant_body_differentiation_operation_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(
                summary["resolver_module"],
                "resolve_descendant_body_differentiation_operation_v0_min",
            )
            self.assert_recorded_operation_posture(result)
            self.assert_candidate_records(result)
            self.assert_operation_not_wrapper(result)
            self.assert_canonical_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
