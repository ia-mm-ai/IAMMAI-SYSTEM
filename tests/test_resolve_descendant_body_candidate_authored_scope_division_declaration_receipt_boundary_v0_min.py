"""Tests for the authored scope-division declaration receipt boundary only.

The boundary records one future receipt-then-audit shape while keeping the
external declaration proposed-only, the signature attestation-only, coupling
unassigned, and every receipt, audit, standing, and downstream posture false.
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

import resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min as resolver


class AuthoredScopeDivisionDeclarationReceiptBoundaryTests(unittest.TestCase):
    """Bounded executable coverage for the receipt boundary resolver."""

    BOUNDARY_KEY = "descendant_body_candidate_authored_scope_division_declaration_receipt_boundary"
    CHECKS_KEY = "authored_scope_division_declaration_receipt_boundary_checks"
    SUMMARY_KEY = "authored_scope_division_declaration_receipt_boundary_summary"
    SENTINELS = (
        "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
        "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
        "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
    )

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
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

    def _write_json(self, path: Path, value: object) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def _boundary_spec_text(self, hostile: bool = False) -> str:
        lines: list[str] = []
        for _, markers in resolver.BOUNDARY_SPEC_MARKER_CLASSES:
            lines.extend(markers)
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(dict.fromkeys(lines)) + "\n"

    def _completed_operation_text(self, hostile: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "failed_check_count = 0",
            "passed_check_count = 96",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _evidence_check_text(self, hostile: bool = False) -> str:
        lines = [
            "UNSUPPORTED",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _differentiation_text(self, hostile: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
            "exactly two result-contained non-standing candidate records",
            "candidate records remain non-standing",
            "candidate records are not descendant bodies",
            "crossing_authorized = false",
            "relation_created = false",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _distinctness_text(self, hostile: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
            "NOT_DISTINCT",
            "distinctness_supported = false",
            "candidate_record_count_compared = 2",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _basis_emission_text(self, hostile: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
            "REQUIRES_ADDITIONAL_BASIS",
            "candidate_specific_content_emitted = false",
            "separate_seal_material_emitted = false",
            "separate_lineage_receipt_material_emitted = false",
            "separate_digest_material_emitted = false",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _scope_boundary_text(self, hostile: bool = False) -> str:
        lines = [
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
            "RECORDED",
            "future_scope_declaration_operation_shape_allowed = true",
            "candidate_a_scope_not_declared = true",
            "candidate_b_scope_not_declared = true",
            "basis_bearing_scope_division_not_declared = true",
            "scope_label_laundering_not_allowed = true",
        ]
        if hostile:
            lines.extend(self.SENTINELS)
        return "\n".join(lines) + "\n"

    def _synthetic_files(self, directory: Path, hostile: bool = False) -> dict[str, Path]:
        return {
            "boundary_spec_reference": self._write_text(
                directory / "boundary-spec.md", self._boundary_spec_text(hostile)
            ),
            "completed_operation_terminal_summary_reference": self._write_text(
                directory / "operation-summary.md", self._completed_operation_text(hostile)
            ),
            "existence_claim_evidence_check_terminal_summary_reference": self._write_text(
                directory / "evidence-summary.md", self._evidence_check_text(hostile)
            ),
            "differentiation_operation_terminal_summary_reference": self._write_text(
                directory / "differentiation-summary.md", self._differentiation_text(hostile)
            ),
            "distinctness_operation_terminal_summary_reference": self._write_text(
                directory / "distinctness-summary.md", self._distinctness_text(hostile)
            ),
            "basis_emission_operation_terminal_summary_reference": self._write_text(
                directory / "basis-emission-summary.md", self._basis_emission_text(hostile)
            ),
            "scope_division_declaration_boundary_terminal_summary_reference": self._write_text(
                directory / "scope-boundary-summary.md", self._scope_boundary_text(hostile)
            ),
        }

    def _valid_request(self, files: dict[str, Path]) -> dict[str, object]:
        return resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_request(
            **{key: str(path) for key, path in files.items()}
        )

    def _boundary(self, result: dict[str, object]) -> dict[str, object]:
        boundary = result.get(self.BOUNDARY_KEY)
        self.assertIsInstance(boundary, dict)
        return boundary

    def _checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        checks = result.get(self.CHECKS_KEY)
        self.assertIsInstance(checks, list)
        self.assertTrue(all(isinstance(check, dict) for check in checks))
        return checks

    def passed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is True for check in self._checks(result))

    def failed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is False for check in self._checks(result))

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_recorded(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_public_codes(self, result: dict[str, object]) -> None:
        for check in self._checks(result):
            for key in ("block_code", "failure_code"):
                if check.get(key) is not None:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_refusal_posture(self, result: dict[str, object]) -> None:
        boundary = self._boundary(result)
        for key in (
            "receipt_performed",
            "audit_performed",
            "declaration_admitted_as_standing_basis",
            "external_declaration_hash_recorded",
            "external_declaration_custody_recorded",
            "signature_treated_as_scope_standing",
            "signature_treated_as_candidate_specific_basis_emission",
            "signature_treated_as_distinctness_support",
            "authored_scope_claim_accepted_as_standing",
            "motion_scope_accepted_as_standing",
            "regulation_scope_accepted_as_standing",
            "motion_regulation_division_audited",
            "motion_regulation_division_accepted",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
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
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "repair_performed",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        ):
            self.assertIs(boundary.get(key), False, key)

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_public_codes(result)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)

    def assert_wrapper_separation(self, result: dict[str, object]) -> None:
        boundary = self._boundary(result)
        for key in (
            "outcome",
            "block",
            self.CHECKS_KEY,
            "non_claims",
            self.SUMMARY_KEY,
            "authored_scope_division_declaration_receipt_boundary_metadata",
        ):
            self.assertNotIn(key, boundary)

    def assert_no_raw_bodies(self, result: dict[str, object]) -> None:
        serialized = json.dumps(result, ensure_ascii=True, sort_keys=True)
        for sentinel in self.SENTINELS:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min",
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path",
            "write_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_result",
            "build_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_summary",
            "build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min")
        self.assertEqual(resolver.BOUNDARY_ID, "descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.BOUNDARY_SCOPE, "EXTERNAL_AUTHORED_DECLARATION_RECEIPT_FOR_AUDIT_ONLY")
        self.assertEqual(resolver.FUTURE_RECEIPT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION")
        self.assertEqual(resolver.FUTURE_AUDIT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "RECEIPT_THEN_AUDIT_ONLY")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_STATUS, "EXISTS_OUTSIDE_REPO")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_ROLE, "PROPOSED_AUTHORED_AUDIT_MATERIAL")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_AUTHOR, "Marko Markota")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_SIGNATURE_ROLE, "AUTHORSHIP_ATTESTATION_ONLY")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_SCOPE_CLAIM_A, "Motion-side admissible variation")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_SCOPE_CLAIM_B, "Regulation-side admissibility bounds")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_COUPLING_CLAIM, "COUPLING_NOT_ASSIGNED_NOT_CREATED")
        self.assertEqual(resolver.EXTERNAL_DECLARATION_LINEAGE_CLAIM, "LINEAGE_REQUIRED_NO_ORPHANED_STATE_NO_SILENT_RESET_NO_OVERWRITE")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min"
        ))
        self.assertTrue({
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "BOUNDARY_SPEC_REFERENCE_MISSING",
            "BOUNDARY_SPEC_MARKER_MISSING",
            "COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_RECEIPT_OR_AUDIT_REQUESTED",
            "PROHIBITED_DECLARATION_CONVERSION_REQUESTED",
            "PROHIBITED_SIGNATURE_CONVERSION_REQUESTED",
            "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        }.issubset(resolver.BLOCK_CODES))

    def test_default_synthetic_request_records_boundary_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(
                self._valid_request(self._synthetic_files(Path(temporary_directory)))
            )
        self.assert_recorded(result)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assertEqual(result["authored_scope_division_declaration_receipt_boundary_metadata"]["result_version"], "0.1.0")
        self.assertEqual(result["authored_scope_division_declaration_receipt_boundary_metadata"]["resolver_module"], resolver.RESOLVER_MODULE)
        boundary = self._boundary(result)
        for key, value in {
            "authored_scope_division_declaration_receipt_boundary_id": resolver.BOUNDARY_ID,
            "authored_scope_division_declaration_receipt_boundary_type": resolver.BOUNDARY_TYPE,
            "authored_scope_division_declaration_receipt_boundary_version": resolver.BOUNDARY_VERSION,
            "authored_scope_division_declaration_receipt_boundary_scope": resolver.BOUNDARY_SCOPE,
            "future_receipt_operation_type": resolver.FUTURE_RECEIPT_OPERATION_TYPE,
            "future_audit_operation_type": resolver.FUTURE_AUDIT_OPERATION_TYPE,
            "admissible_future_route": resolver.ADMISSIBLE_FUTURE_ROUTE,
            "external_declaration_status": resolver.EXTERNAL_DECLARATION_STATUS,
            "external_declaration_role": resolver.EXTERNAL_DECLARATION_ROLE,
            "external_declaration_author": resolver.EXTERNAL_DECLARATION_AUTHOR,
            "external_declaration_signature_role": resolver.EXTERNAL_DECLARATION_SIGNATURE_ROLE,
            "external_declaration_scope_claim_candidate_a": resolver.EXTERNAL_DECLARATION_SCOPE_CLAIM_A,
            "external_declaration_scope_claim_candidate_b": resolver.EXTERNAL_DECLARATION_SCOPE_CLAIM_B,
            "external_declaration_coupling_claim": resolver.EXTERNAL_DECLARATION_COUPLING_CLAIM,
            "external_declaration_lineage_claim": resolver.EXTERNAL_DECLARATION_LINEAGE_CLAIM,
        }.items():
            self.assertEqual(boundary[key], value, key)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_wrapper_separation(result)
        for key in (
            "authored_scope_division_declaration_receipt_boundary_metadata",
            "declared_authored_scope_division_declaration_receipt_boundary_basis",
            "upstream_basis",
            self.BOUNDARY_KEY,
            self.CHECKS_KEY,
            "authored_scope_division_declaration_receipt_boundary_statement",
            "authored_scope_division_declaration_receipt_boundary_non_meaning",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            self.SUMMARY_KEY,
        ):
            self.assertIn(key, result)
        self.assertIn("future receipt operation", " ".join(result["permitted_future_route"]))
        self.assertIn("direct PDF", " ".join(result["blocked_routes"]))

    def test_default_live_repo_target_records_boundary_if_present(self) -> None:
        paths = (
            resolver.DEFAULT_BOUNDARY_SPEC_REFERENCE,
            resolver.DEFAULT_COMPLETED_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
            resolver.DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        )
        if not all((REPO_ROOT / path).is_file() for path in paths):
            self.skipTest("not all default receipt-boundary files are present")
        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min()
        self.assert_recorded(result)
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS[-7:]:
            self.assertIs(self._boundary(result)[key], True, key)

    def test_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._synthetic_files(Path(temporary_directory))
            do_not_record = self._valid_request(files)
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(do_not_record)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            self.assertIs(self._boundary(result)["authored_scope_division_declaration_receipt_boundary_recorded"], False)
            self.assert_refusal_posture(result)
            self.assert_canonical_non_claims(result)
            blocked = self._valid_request(files)
            blocked["intent"] = resolver.INTENT_BLOCK
            blocked_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(blocked)
        self.assert_blocked(blocked_result)
        self.assertEqual(self.block_code(blocked_result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_exact_field_blocking(self) -> None:
        cases = {
            "unsupported_intent": ("intent", "OTHER"),
            "missing_id": ("authored_scope_division_declaration_receipt_boundary_id", None),
            "wrong_id": ("authored_scope_division_declaration_receipt_boundary_id", "other"),
            "missing_type": ("authored_scope_division_declaration_receipt_boundary_type", None),
            "wrong_type": ("authored_scope_division_declaration_receipt_boundary_type", "other"),
            "missing_version": ("authored_scope_division_declaration_receipt_boundary_version", None),
            "wrong_version": ("authored_scope_division_declaration_receipt_boundary_version", "9.9.9"),
            "missing_scope": ("authored_scope_division_declaration_receipt_boundary_scope", None),
            "wrong_scope": ("authored_scope_division_declaration_receipt_boundary_scope", "other"),
            "receipt_type": ("future_receipt_operation_type", "other"),
            "audit_type": ("future_audit_operation_type", "other"),
            "route": ("admissible_future_route", "other"),
            "status": ("external_declaration_status", "other"),
            "role": ("external_declaration_role", "other"),
            "author": ("external_declaration_author", "other"),
            "signed": ("external_declaration_signed", False),
            "signature_role": ("external_declaration_signature_role", "other"),
            "scope_a": ("external_declaration_scope_claim_candidate_a", "other"),
            "scope_b": ("external_declaration_scope_claim_candidate_b", "other"),
            "coupling": ("external_declaration_coupling_claim", "other"),
            "lineage": ("external_declaration_lineage_claim", "other"),
            "missing_spec": ("boundary_spec_reference", ""),
            "missing_upstream": ("completed_operation_terminal_summary_reference", ""),
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._synthetic_files(Path(temporary_directory))
            for name, (field, value) in cases.items():
                with self.subTest(name=name):
                    request = self._valid_request(files)
                    request[field] = value
                    self.assert_blocked(
                        resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
                    )
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(["not", "mapping"])
            )

    def test_marker_validation_blocking_behavior(self) -> None:
        targets = (
            ("boundary_spec_reference", "BOUNDARY_SPEC_MARKER_MISSING"),
            ("completed_operation_terminal_summary_reference", "COMPLETED_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("existence_claim_evidence_check_terminal_summary_reference", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("differentiation_operation_terminal_summary_reference", "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("distinctness_operation_terminal_summary_reference", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("basis_emission_operation_terminal_summary_reference", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            ("scope_division_declaration_boundary_terminal_summary_reference", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING"),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            for index, (field, expected) in enumerate(targets):
                with self.subTest(field=field):
                    files = self._synthetic_files(
                        Path(temporary_directory) / self.safe_json_filename(field, index).replace(".json", "")
                    )
                    self._write_text(files[field], "required posture intentionally absent\n")
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(
                        self._valid_request(files)
                    )
                    self.assert_blocked(result)
                    self.assertEqual(self.block_code(result), expected)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._synthetic_files(Path(temporary_directory))
            for field in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(field=field):
                    request = self._valid_request(files)
                    request[field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
                    self.assert_blocked(result)

    def test_required_false_top_level_posture_and_non_claim_canonicalization(self) -> None:
        representative = (
            "receipt_performed",
            "audit_performed",
            "declaration_admitted_as_standing_basis",
            "external_declaration_hash_recorded",
            "external_declaration_custody_recorded",
            "signature_treated_as_scope_standing",
            "signature_treated_as_candidate_specific_basis_emission",
            "signature_treated_as_distinctness_support",
            "authored_scope_claim_accepted_as_standing",
            "motion_scope_accepted_as_standing",
            "regulation_scope_accepted_as_standing",
            "motion_regulation_division_audited",
            "motion_regulation_division_accepted",
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "distinctness_supported_recorded",
            "candidate_standing_authorized",
            "descendant_body_created",
            "standing_authorized",
            "crossing_authorized",
            "relation_created",
            "runtime_created",
            "api_created",
            "currentness_created",
            "authority_created",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "affected_file_repaired",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
            "direct_pdf_ingestion_as_standing_basis",
            "direct_signature_to_standing_conversion",
            "direct_signature_to_distinctness_support_conversion",
            "direct_signature_to_candidate_specific_basis_emission_conversion",
            "direct_declaration_to_scope_standing_conversion",
            "direct_declaration_to_candidate_records_distinct_conversion",
            "direct_declaration_to_descendant_body_creation",
            "direct_declaration_to_relation_creation",
            "direct_declaration_to_runtime_creation",
            "direct_declaration_to_authority_currentness_creation",
            "direct_declaration_to_follow_on_work",
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            files = self._synthetic_files(Path(temporary_directory))
            clean = self._valid_request(files)
            for field in representative:
                with self.subTest(top_level=field):
                    request = copy.deepcopy(clean)
                    request[field] = True
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][field], False)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=field):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"][field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][field], False)
            for malformed in (None, [], {}, {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}):
                with self.subTest(malformed=type(malformed).__name__):
                    request = copy.deepcopy(clean)
                    request["declared_non_claims"] = malformed
                    self.assert_blocked(
                        resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
                    )

    def test_sanitizer_path_write_non_mutation_summary_and_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            files = self._synthetic_files(directory / "basis", hostile=True)
            request = self._valid_request(files)
            request["raw_markdown_body"] = self.SENTINELS[0]
            request["hidden_repo_state"] = self.SENTINELS[1]
            request["current_working_tree"] = self.SENTINELS[2]
            request_before = copy.deepcopy(request)
            contents_before = {key: path.read_text(encoding="utf-8") for key, path in files.items()}
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min(request)
            self.assert_recorded(result)
            self.assert_no_raw_bodies(result)
            self.assertEqual(request, request_before)
            for key, original in contents_before.items():
                self.assertEqual(files[key].read_text(encoding="utf-8"), original, key)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
            self.assertIs(summary["authored_scope_division_declaration_receipt_boundary_recorded"], True)
            self.assertIs(summary["receipt_performed"], False)
            self.assertIs(summary["audit_performed"], False)
            self.assertIs(summary["target_boundary_spec_markers_present"], True)
            request_path = self._write_json(directory / "request.json", self._valid_request(files))
            from_path = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path(request_path)
            self.assert_recorded(from_path)
            first = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_result(
                from_path, directory / "output"
            )
            second = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_result(
                from_path, directory / "output"
            )
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("authored_scope_division_declaration_receipt_boundary_v0_min_result", first.name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min",
                str(resolver.OUTPUT_ROOT),
            )
            malformed = directory / "malformed.json"
            self._write_text(malformed, "{")
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path(malformed)
            )
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path(directory / "missing.json")
            )
            self.assert_blocked(
                resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_boundary_v0_min_from_path(
                    self._write_json(directory / "array.json", [])
                )
            )
        self.assert_refusal_posture(result)
        self.assert_canonical_non_claims(result)
        self.assert_wrapper_separation(result)


if __name__ == "__main__":
    unittest.main()
