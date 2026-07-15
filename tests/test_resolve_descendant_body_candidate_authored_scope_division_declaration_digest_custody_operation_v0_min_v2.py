"""Bounded v2 tests for digest/custody scalar false-posture preservation.

The v2 resolver delegates v1 material and blocking semantics.  These tests
exercise that delegation with explicit synthetic files and verify that v2
keeps false non-claims and raw-return route flags as literal booleans.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2 as resolver


class DigestCustodyOperationV2Tests(unittest.TestCase):
    """Verify v2 keeps the one bounded digest/custody operation non-standing."""

    ROUTE_FALSE_KEYS = (
        "raw_pdf_returned",
        "raw_extracted_text_returned",
        "raw_pdf_return_route",
        "raw_extracted_text_return_route",
        "copy_pdf_into_repo_route",
    )
    OPERATION_WRAPPER_FIELDS = (
        "outcome",
        "block",
        "authored_scope_division_declaration_digest_custody_operation_checks",
        "non_claims",
        "authored_scope_division_declaration_digest_custody_operation_summary",
        "authored_scope_division_declaration_digest_custody_operation_metadata",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, root: Path, name: str, text: str) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_material(self, root: Path, name: str, content: bytes) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def expected_sha256(self, content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()

    def digest_spec_text(self) -> str:
        return "\n".join(
            (
                "# Descendant Body Candidate Authored Scope Division Declaration Digest Custody Operation V0 Minimum Specification",
                resolver.OPERATION_TYPE,
                resolver.OPERATION_ID,
                resolver.OPERATION_SCOPE,
                resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
                resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED,
                resolver.TARGET_PRIMARY_MATERIAL_FILENAME,
                resolver.TARGET_PRIMARY_MATERIAL_VERSION,
                resolver.TARGET_PRIMARY_MATERIAL_DATE,
                resolver.TARGET_PRIMARY_MATERIAL_AUTHOR,
                resolver.TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE,
                resolver.TARGET_PREDECESSOR_MATERIAL_FILENAME,
                resolver.TARGET_PREDECESSOR_MATERIAL_ROLE,
                resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED,
                resolver.UPSTREAM_AUDIT_RESULT_REQUIRED,
                "declaration_accepted_as_basis = true",
                "declaration_admitted_as_standing_basis = false",
                "candidate_a_scope_declared = false",
                "candidate_b_scope_declared = false",
                "basis_bearing_scope_division_declared = false",
                "basis_gap_closed = false",
                "Digest/custody permission is not digest/custody completion.",
                "Digest is not truth.",
                "Hash is not standing.",
                "Custody is not standing.",
                "File identity is not standing.",
                "Hash, custody, and file identity are not standing.",
                "File custody is not audit result, accepted basis, standing basis, scope declaration, or basis-gap closure.",
                "Digest/custody result is not standing, scope declaration, basis-gap closure, candidate-specific basis emission, distinctness support, candidate standing, descendant-body creation, relation, runtime, coupling, or follow-on authorization.",
                "Accepted basis remains non-standing.",
                resolver.ADMISSIBLE_FUTURE_ROUTE,
                "A future digest/custody resolver may compute SHA-256 for a supplied V2 declaration file.",
                "It may optionally compute SHA-256 for a supplied V1 predecessor file.",
                "It must not return PDF bytes or raw extracted text and must preserve digest, hash, and custody as non-standing.",
                "failed_check_count = 0",
                "passed_check_count = 91",
                "digest_recorded = false",
                "custody_posture_recorded = false",
                "text_extraction_posture_recorded = false",
                "passed_check_count = 83",
                "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS",
                "an empty missing-criteria list",
                "false standing, scope-declaration, and basis-gap-closure postures",
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                "missing non-cosmetic candidate A scope declaration",
                "missing non-cosmetic candidate B scope declaration",
                "missing basis-bearing scope division declaration",
                "does not close the gap",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct digest permission to digest completion; direct custody permission to custody completion",
                "direct digest result to truth; hash result to standing; custody posture or file identity to standing",
                "direct digest/custody to audit result, accepted basis, standing basis, scope declaration, basis-gap closure",
                "raw PDF return, raw extracted-text return, and copy-PDF-into-repo routes",
                "repository scan, affected-file repair, and prior unsupported-claim validation routes",
                "This operation spec defines only a future digest/custody operation shape",
                "Open means not scheduled, not authorized, and not executed.",
            )
        )

    def receipt_summary_text(self) -> str:
        return "\n".join(
            (
                resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
                "failed_check_count = 0",
                "passed_check_count = 91",
                resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED,
                resolver.TARGET_PRIMARY_MATERIAL_FILENAME,
                resolver.TARGET_PRIMARY_MATERIAL_VERSION,
                resolver.TARGET_PRIMARY_MATERIAL_DATE,
                resolver.TARGET_PRIMARY_MATERIAL_AUTHOR,
                resolver.TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE,
                resolver.TARGET_PREDECESSOR_MATERIAL_FILENAME,
                resolver.TARGET_PREDECESSOR_MATERIAL_ROLE,
                "digest_recorded = false",
                "custody_posture_recorded = false",
                "text_extraction_posture_recorded = false",
            )
        )

    def audit_summary_text(self) -> str:
        return "\n".join(
            (
                resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED,
                "failed_check_count = 0",
                "passed_check_count = 83",
                "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS",
                "declaration_accepted_as_basis = true",
                "missing_or_insufficient_audit_criteria = []",
                "Accepted basis is not standing basis.",
                "Candidate A scope, Candidate B scope, and basis-bearing scope division were not declared as standing. The basis gap was not closed.",
                "declaration_admitted_as_standing_basis = false",
                "candidate_a_scope_declared = false",
                "candidate_b_scope_declared = false",
                "basis_bearing_scope_division_declared = false",
                "basis_gap_closed = false",
            )
        )

    def scope_operation_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                "missing non-cosmetic candidate A scope declaration",
                "missing non-cosmetic candidate B scope declaration",
                "missing basis-bearing scope division declaration",
                "does not close the gap",
            )
        )

    def existence_summary_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        )

    def distinctness_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                "NOT_DISTINCT",
                "distinctness_supported = false",
                "candidate_record_count_compared = 2",
            )
        )

    def basis_emission_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                "REQUIRES_ADDITIONAL_BASIS",
                "candidate_specific_content_emitted = false",
                "separate_seal_material_emitted = false",
                "separate_lineage_receipt_material_emitted = false",
                "separate_digest_material_emitted = false",
            )
        )

    def boundary_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
                "RECORDED",
                "future_scope_declaration_operation_shape_allowed = true",
                "candidate_a_scope_not_declared = true",
                "candidate_b_scope_not_declared = true",
                "basis_bearing_scope_division_not_declared = true",
                "scope_label_laundering_not_allowed = true",
            )
        )

    def synthetic_marker_paths(self, root: Path) -> dict[str, Path]:
        return {
            "operation_spec_reference": self.write_markdown(root, "digest_spec.md", self.digest_spec_text()),
            "receipt_operation_terminal_summary_reference": self.write_markdown(root, "receipt.md", self.receipt_summary_text()),
            "audit_operation_terminal_summary_reference": self.write_markdown(root, "audit.md", self.audit_summary_text()),
            "scope_division_declaration_operation_terminal_summary_reference": self.write_markdown(root, "scope_operation.md", self.scope_operation_summary_text()),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(root, "existence.md", self.existence_summary_text()),
            "distinctness_operation_terminal_summary_reference": self.write_markdown(root, "distinctness.md", self.distinctness_summary_text()),
            "basis_emission_operation_terminal_summary_reference": self.write_markdown(root, "basis_emission.md", self.basis_emission_summary_text()),
            "scope_division_declaration_boundary_terminal_summary_reference": self.write_markdown(root, "boundary.md", self.boundary_summary_text()),
        }

    def valid_request(
        self,
        paths: dict[str, Path],
        primary_material: Path | None = None,
        predecessor_material: Path | None = None,
    ) -> dict[str, object]:
        overrides: dict[str, object] = {key: str(path) for key, path in paths.items()}
        if primary_material is not None:
            overrides["primary_material_path"] = str(primary_material)
        if predecessor_material is not None:
            overrides["predecessor_material_path"] = str(predecessor_material)
        return resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_request(**overrides)

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation")
        self.assertIsInstance(value, dict)
        return value

    def summary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("authored_scope_division_declaration_digest_custody_operation_summary")
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get("authored_scope_division_declaration_digest_custody_operation_checks")
        self.assertIsInstance(value, list)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def passed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is True for check in self.checks(result))

    def failed_check_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is False for check in self.checks(result))

    def assert_public_codes(self, result: dict[str, object]) -> None:
        for check in self.checks(result):
            for field in ("block_code", "failure_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_recorded_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(self.block_code(result))

    def assert_requires_material_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_MATERIAL)
        self.assertEqual(self.failed_check_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(self.block_code(result))

    def assert_blocked_public(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_false_postures(result)

    def assert_false_postures(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        operation = self.operation(result)
        summary = self.summary(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)
            self.assertIn(key, summary)
            self.assertIs(summary[key], False, key)
        for key in self.ROUTE_FALSE_KEYS:
            self.assertIn(key, operation)
            self.assertIs(operation[key], False, key)
            self.assertIn(key, summary)
            self.assertIs(summary[key], False, key)

    def assert_no_false_redaction(self, result: dict[str, object]) -> None:
        self.assert_false_postures(result)
        for mapping in (result["non_claims"], self.operation(result), self.summary(result)):
            for key in (*resolver.REQUIRED_FALSE_NON_CLAIMS, *self.ROUTE_FALSE_KEYS):
                if key in mapping:
                    self.assertNotIsInstance(mapping[key], str, key)

    def assert_operation_not_wrapper(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in self.OPERATION_WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def assert_no_raw_content(self, result: dict[str, object], *sentinels: str) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def assert_v2_identity(self, result: dict[str, object]) -> None:
        self.assertEqual(result["result_version"], "0.2.0")
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        metadata = result["authored_scope_division_declaration_digest_custody_operation_metadata"]
        self.assertEqual(metadata["result_version"], "0.2.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(self.summary(result)["result_version"], "0.2.0")
        self.assertEqual(self.summary(result)["resolver_module"], resolver.RESOLVER_MODULE)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2",
            "resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_from_path",
            "write_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result",
            "build_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_summary",
            "build_declared_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2")
        self.assertEqual(resolver.OPERATION_ID, "descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "EXACT_AUTHORED_DECLARATION_FILE_DIGEST_AND_CUSTODY_POSTURE_ONLY")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED, "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY")
        self.assertEqual(resolver.UPSTREAM_AUDIT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION")
        self.assertEqual(resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS")
        self.assertEqual(resolver.UPSTREAM_AUDIT_RESULT_REQUIRED, "SATISFIES_MISSING_BASIS_REQUIREMENTS")
        self.assertIs(resolver.UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED, True)
        self.assertEqual(resolver.TARGET_PRIMARY_MATERIAL_FILENAME, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf")
        self.assertEqual(resolver.DIGEST_ALGORITHM_ALLOWED, "SHA-256")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "DIGEST_CUSTODY_THEN_SUCCESSOR_CLOSURE_ONLY")
        self.assertTrue(set((resolver.OUTCOME_RECORDED, resolver.OUTCOME_REQUIRES_MATERIAL, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED)).issubset(resolver.OUTCOME_FAMILY))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2"))
        for code in (
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "DIGEST_CUSTODY_OPERATION_SPEC_REFERENCE_MISSING",
            "DIGEST_CUSTODY_OPERATION_SPEC_MARKER_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
            "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
            "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", "MATERIAL_REFERENCE_MISSING",
            "MATERIAL_REFERENCE_INVALID", "MATERIAL_FILE_NOT_FOUND", "MATERIAL_REFERENCE_NOT_FILE",
            "MATERIAL_FILENAME_MISMATCH", "DIGEST_ALGORITHM_UNSUPPORTED", "CUSTODY_POSTURE_MISSING_OR_UNSUPPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED", "PROHIBITED_DIGEST_TO_TRUTH_REQUESTED",
            "PROHIBITED_HASH_OR_CUSTODY_TO_STANDING_REQUESTED",
            "PROHIBITED_DIGEST_CUSTODY_TO_AUDIT_OR_ACCEPTED_BASIS_REQUESTED",
            "PROHIBITED_SCOPE_OR_BASIS_GAP_CLOSURE_REQUESTED", "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
            "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "REQUESTED_RAW_PDF_RETURN",
            "REQUESTED_RAW_EXTRACTED_TEXT_RETURN", "REQUESTED_PDF_COPY_INTO_REPO", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_requires_material_with_synthetic_markers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request = self.valid_request(self.synthetic_marker_paths(Path(directory)))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
            self.assert_requires_material_not_blocked(result)
            self.assert_v2_identity(result)
            operation = self.operation(result)
            for key in (
                "digest_custody_operation_recorded", "digest_computed", "digest_recorded", "custody_posture_recorded",
                "primary_material_digest_recorded", "predecessor_material_digest_recorded",
            ):
                self.assertIs(operation[key], False, key)
            self.assert_no_false_redaction(result)
            self.assert_operation_not_wrapper(result)

    def test_v2_material_records_exact_digest_and_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            content = b"V2 signed declaration test bytes\n"
            primary = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, content)
            request = self.valid_request(paths, primary)
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
            self.assert_recorded_not_blocked(result)
            self.assert_v2_identity(result)
            operation = self.operation(result)
            self.assertEqual(operation["digest_algorithm"], "SHA-256")
            self.assertEqual(operation["primary_material_digest_sha256"], self.expected_sha256(content))
            self.assertIsNone(operation["predecessor_material_digest_sha256"])
            self.assertEqual(operation["primary_material_custody_posture"], "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT")
            self.assertIsNone(operation["predecessor_material_custody_posture"])
            for key in (
                "digest_custody_operation_recorded", "digest_computed", "digest_recorded", "custody_posture_recorded",
                "primary_material_digest_recorded", "primary_material_custody_recorded",
            ):
                self.assertIs(operation[key], True, key)
            self.assertIs(operation["predecessor_material_digest_recorded"], False)
            self.assertIs(operation["predecessor_material_custody_recorded"], False)
            self.assertIs(result["material_identity"]["pdf_ingested"], False)
            self.assertIs(result["material_identity"]["pdf_copied_to_repo"], False)
            self.assertIs(result["material_identity"]["text_extracted"], False)
            self.assert_no_false_redaction(result)
            self.assert_operation_not_wrapper(result)
            self.assert_no_raw_content(result, content.decode("ascii"))

    def test_v2_and_v1_materials_record_optional_predecessor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            primary_content = b"V2 signed declaration test bytes\n"
            predecessor_content = b"V1 predecessor declaration test bytes\n"
            primary = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, primary_content)
            predecessor = self.write_material(root, resolver.TARGET_PREDECESSOR_MATERIAL_FILENAME, predecessor_content)
            request = self.valid_request(paths, primary, predecessor)
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
            self.assert_recorded_not_blocked(result)
            operation = self.operation(result)
            self.assertEqual(operation["primary_material_digest_sha256"], self.expected_sha256(primary_content))
            self.assertEqual(operation["predecessor_material_digest_sha256"], self.expected_sha256(predecessor_content))
            self.assertEqual(operation["primary_material_custody_posture"], "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT")
            self.assertEqual(operation["predecessor_material_custody_posture"], "LOCAL_OPERATOR_HELD_PREDECESSOR_SOURCE_ARTIFACT")
            self.assertIs(operation["predecessor_material_digest_recorded"], True)
            self.assertIs(operation["predecessor_material_custody_recorded"], True)
            self.assert_no_false_redaction(result)
            self.assert_no_raw_content(result, primary_content.decode("ascii"), predecessor_content.decode("ascii"))

    def test_material_validation_blocks_or_requires_material(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            valid = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, b"valid\n")
            wrong_name = self.write_material(root, "wrong.pdf", b"wrong\n")
            directory_path = root / "material-directory"
            directory_path.mkdir()
            cases = (
                ("missing_primary", {}, resolver.OUTCOME_REQUIRES_MATERIAL),
                ("missing_file", {"primary_material_path": str(root / "missing.pdf")}, resolver.OUTCOME_BLOCKED),
                ("directory", {"primary_material_path": str(directory_path)}, resolver.OUTCOME_BLOCKED),
                ("wrong_basename", {"primary_material_path": str(wrong_name)}, resolver.OUTCOME_BLOCKED),
                ("unsupported_algorithm", {"primary_material_path": str(valid), "digest_algorithm": "SHA-1"}, resolver.OUTCOME_BLOCKED),
                ("missing_custody", {"primary_material_path": str(valid), "primary_material_custody_posture": None}, resolver.OUTCOME_BLOCKED),
                ("unsupported_custody", {"primary_material_path": str(valid), "primary_material_custody_posture": "UNBOUNDED"}, resolver.OUTCOME_BLOCKED),
                ("missing_predecessor", {"primary_material_path": str(valid), "predecessor_material_path": str(root / "missing-v1")}, resolver.OUTCOME_BLOCKED),
                ("directory_predecessor", {"primary_material_path": str(valid), "predecessor_material_path": str(directory_path)}, resolver.OUTCOME_BLOCKED),
            )
            for index, (name, overrides, expected) in enumerate(cases):
                with self.subTest(name=name):
                    request = self.valid_request(paths)
                    request.update(overrides)
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    if expected == resolver.OUTCOME_REQUIRES_MATERIAL:
                        self.assert_requires_material_not_blocked(result)
                    else:
                        self.assert_blocked_public(result)
                    self.assert_v2_identity(result)
                    self.assert_no_false_redaction(result)
                    self.assertTrue(self.safe_json_filename(name, index).endswith(".json"))

    def test_marker_validation_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            texts = {
                "operation_spec_reference": self.digest_spec_text(),
                "receipt_operation_terminal_summary_reference": self.receipt_summary_text(),
                "audit_operation_terminal_summary_reference": self.audit_summary_text(),
                "scope_division_declaration_operation_terminal_summary_reference": self.scope_operation_summary_text(),
                "existence_claim_evidence_check_terminal_summary_reference": self.existence_summary_text(),
                "distinctness_operation_terminal_summary_reference": self.distinctness_summary_text(),
                "basis_emission_operation_terminal_summary_reference": self.basis_emission_summary_text(),
                "scope_division_declaration_boundary_terminal_summary_reference": self.boundary_summary_text(),
            }
            for index, (field, text) in enumerate(texts.items()):
                with self.subTest(field=field):
                    paths[field].write_text("missing marker posture", encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(self.valid_request(paths))
                    self.assert_blocked_public(result)
                    self.assertTrue(self.safe_json_filename(field, index).endswith(".json"))
                    paths[field].write_text(text, encoding="utf-8")

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths = self.synthetic_marker_paths(Path(directory))
            base = self.valid_request(paths)
            for flag in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(flag=flag):
                    request = copy.deepcopy(base)
                    request[flag] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    self.assert_blocked_public(result)
                    self.assert_v2_identity(result)

    def test_top_level_and_declared_non_claim_failures_canonicalize(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            primary = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, b"valid\n")
            base = self.valid_request(paths, primary)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    self.assert_blocked_public(result)
                with self.subTest(declared_non_claim=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    self.assert_blocked_public(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(preclaimed_output_posture=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    self.assert_blocked_public(result)
            malformed_cases = (
                ("missing_mapping", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            )
            for name, declared in malformed_cases:
                with self.subTest(declared_non_claims=name):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"] = declared
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
                    self.assert_blocked_public(result)

    def test_sanitizer_regression_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            primary_content = b"V2 signed declaration test bytes\n"
            primary = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, primary_content)
            request = self.valid_request(paths, primary)
            request.update(
                {
                    "raw_pdf_body": "RAW_PDF_BODY_MUST_NOT_RETURN",
                    "raw_extracted_text": "RAW_EXTRACTED_TEXT_MUST_NOT_RETURN",
                    "pdf_bytes": b"RAW_PDF_BYTES_MUST_NOT_RETURN",
                }
            )
            original_request = copy.deepcopy(request)
            marker_contents = {name: path.read_text(encoding="utf-8") for name, path in paths.items()}
            material_before = primary.read_bytes()
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2(request)
            self.assertEqual(request, original_request)
            self.assertEqual(primary.read_bytes(), material_before)
            for name, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), marker_contents[name])
            self.assert_no_false_redaction(result)
            self.assert_no_raw_content(result, "RAW_PDF_BODY_MUST_NOT_RETURN", "RAW_EXTRACTED_TEXT_MUST_NOT_RETURN", "RAW_PDF_BYTES_MUST_NOT_RETURN")
            declared = result["declared_authored_scope_division_declaration_digest_custody_operation_basis"]
            self.assertEqual(declared["raw_pdf_body"], "[REDACTED_SENSITIVE_BODY]")
            self.assertEqual(declared["raw_extracted_text"], "[REDACTED_SENSITIVE_BODY]")
            self.assertEqual(declared["pdf_bytes"], "[REDACTED_BINARY_CONTENT]")

    def test_path_write_and_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.synthetic_marker_paths(root)
            content = b"V2 signed declaration test bytes\n"
            primary = self.write_material(root, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, content)
            request = self.valid_request(paths, primary)
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_from_path(request_path)
            self.assert_recorded_not_blocked(result)
            self.assertEqual(self.operation(result)["primary_material_digest_sha256"], self.expected_sha256(content))
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["primary_material_digest_sha256"], self.expected_sha256(content))
            self.assertIsNone(summary["predecessor_material_digest_sha256"])
            self.assertIs(summary["primary_material_digest_recorded"], True)
            self.assertIs(summary["predecessor_material_digest_recorded"], False)
            for key in self.ROUTE_FALSE_KEYS:
                self.assertIs(summary[key], False, key)
            output = root / "output"
            first = resolver.write_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result(result, output)
            second = resolver.write_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("authored_scope_division_declaration_digest_custody_operation_v0_min_v2_result", first.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2", str(resolver.REPO_ROOT / resolver.OUTPUT_ROOT))
            written = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(written["result_version"], "0.2.0")
            self.assertEqual(written["resolver_module"], resolver.RESOLVER_MODULE)
            written_operation = written["descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation"]
            written_summary = written["authored_scope_division_declaration_digest_custody_operation_summary"]
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                self.assertIs(written["non_claims"][key], False, key)
                self.assertIs(written_operation[key], False, key)
                self.assertIs(written_summary[key], False, key)
            for key in self.ROUTE_FALSE_KEYS:
                self.assertIs(written_summary[key], False, key)
            for bad_path in (root / "missing.json", root / "malformed.json", root / "array.json"):
                if bad_path.name == "malformed.json":
                    bad_path.write_text("{", encoding="utf-8")
                elif bad_path.name == "array.json":
                    bad_path.write_text("[]", encoding="utf-8")
                bad = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_digest_custody_operation_v0_min_v2_from_path(bad_path)
                self.assert_blocked_public(bad)


if __name__ == "__main__":
    unittest.main()
