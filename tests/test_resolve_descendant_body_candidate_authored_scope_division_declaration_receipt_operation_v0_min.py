"""Executable bounds for one authored declaration metadata-only receipt operation."""

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

import resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min as resolver


class AuthoredScopeDivisionDeclarationReceiptOperationTests(unittest.TestCase):
    """Test metadata-only V2 receipt without audit, standing, or downstream work."""

    OPERATION_KEY = "descendant_body_candidate_authored_scope_division_declaration_receipt_operation"
    CHECKS_KEY = "authored_scope_division_declaration_receipt_operation_checks"
    SUMMARY_KEY = "authored_scope_division_declaration_receipt_operation_summary"
    WRAPPER_FIELDS = {
        "outcome",
        "block",
        "authored_scope_division_declaration_receipt_operation_checks",
        "non_claims",
        "authored_scope_division_declaration_receipt_operation_summary",
        "authored_scope_division_declaration_receipt_operation_metadata",
    }

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic markdown path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def write_material_bytes(self, path: Path, payload: bytes) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic material path is a directory: {path}")
        path.write_bytes(payload)
        return path

    def valid_operation_spec_text(self) -> str:
        false_posture = "\n".join(f"{key} = false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS)
        return "\n".join(
            (
                "# Descendant Body Candidate Authored Scope Division Declaration Receipt Operation V0 Minimum Specification",
                resolver.OPERATION_TYPE,
                resolver.OPERATION_ID,
                resolver.OPERATION_SCOPE,
                resolver.UPSTREAM_BOUNDARY_TYPE,
                resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
                resolver.ADMISSIBLE_FUTURE_ROUTE,
                resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME,
                resolver.RECEIVED_MATERIAL_EXPECTED_TITLE,
                resolver.RECEIVED_MATERIAL_EXPECTED_VERSION,
                resolver.RECEIVED_MATERIAL_EXPECTED_DATE,
                resolver.RECEIVED_MATERIAL_EXPECTED_AUTHOR,
                resolver.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
                resolver.RECEIVED_MATERIAL_EXPECTED_PREDECESSOR,
                resolver.RECEIVED_MATERIAL_PREDECESSOR_ROLE,
                "contribution map; contribution-map",
                "sibling non-monarchy; sibling-non-monarchy",
                "receipt-sealing posture; receipt-sealing",
                "coupling-not-assigned",
                "no-third-model",
                "lineage constraints; lineage-constraints",
                "Receipt is not audit",
                "Receipt metadata is not audit result",
                "Digest is not truth",
                "Hash is not standing",
                "Custody is not standing",
                "Transcription is not standing",
                "Signature is authorship attestation only",
                "V2 receipt does not erase V1",
                "Coupling is assigned to neither candidate",
                "No third candidate",
                "No third model",
                "No third candidate, third model, or standing body is admitted",
                "No third candidate, third model, or standing body is admitted",
                "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_RECORDED",
                "failed_check_count = 0",
                "passed_check_count = 84",
                "future_receipt_operation_type = DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION",
                "external_declaration_role = PROPOSED_AUTHORED_AUDIT_MATERIAL",
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                "passed_check_count = 96",
                "missing non-cosmetic candidate A scope declaration",
                "missing non-cosmetic candidate B scope declaration",
                "missing basis-bearing scope division declaration",
                "does not close that gap",
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
                "UNSUPPORTED",
                "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
                "direct PDF ingestion as standing basis",
                "direct receipt-to-audit-completion conversion",
                "direct receipt-to-audit-completion, standing, scope-declaration conversion",
                "direct receipt-to-standing conversion",
                "direct digest-to-truth",
                "direct hash-to-standing",
                "direct custody-to-standing",
                "direct transcription-to-standing",
                "direct signature-to-standing",
                "direct declaration-to-scope-standing",
                "direct coupling instantiation",
                "third-candidate",
                "third-model",
                "repository scan",
                "affected-file repair",
                "prior unsupported-claim validation",
                "This operation spec defines only a future receipt operation shape",
                "The prior operation line remains at REQUIRES_ADDITIONAL_BASIS until receipt, audit, and any successor closure are separately bounded and passed.",
                false_posture,
            )
        )

    def valid_receipt_boundary_summary_text(self) -> str:
        return "\n".join(
            (
                resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
                "failed_check_count = 0",
                "passed_check_count = 84",
                "future_receipt_operation_type = DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION",
                "external_declaration_role = PROPOSED_AUTHORED_AUDIT_MATERIAL",
            )
        )

    def valid_scope_division_operation_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                "failed_check_count = 0",
                "passed_check_count = 96",
                "missing non-cosmetic candidate A scope declaration",
                "missing non-cosmetic candidate B scope declaration",
                "missing basis-bearing scope division declaration",
            )
        )

    def valid_existence_claim_evidence_check_summary_text(self) -> str:
        return "\n".join(
            (
                "UNSUPPORTED",
                "descendant_body_basis_candidate_a_created = true",
                "descendant_body_basis_candidate_b_created = true",
                "descendant_body_basis_derivation_event_recorded = true",
            )
        )

    def valid_differentiation_operation_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
                "exactly two result-contained non-standing candidate records",
                "candidate records remain non-standing",
                "candidate records are not descendant bodies",
                "crossing_authorized = false",
                "relation_created = false",
            )
        )

    def valid_distinctness_operation_summary_text(self) -> str:
        return "\n".join(
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                "NOT_DISTINCT",
                "distinctness_supported = false",
                "candidate_record_count_compared = 2",
            )
        )

    def valid_basis_emission_operation_summary_text(self) -> str:
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

    def valid_scope_division_declaration_boundary_summary_text(self) -> str:
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

    def make_synthetic_request(self, root: Path) -> tuple[dict[str, object], dict[str, Path]]:
        paths = {
            "operation_spec_reference": root / "operation_spec.md",
            "receipt_boundary_terminal_summary_reference": root / "receipt_boundary.md",
            "scope_division_declaration_operation_terminal_summary_reference": root / "scope_operation.md",
            "existence_claim_evidence_check_terminal_summary_reference": root / "evidence_check.md",
            "differentiation_operation_terminal_summary_reference": root / "differentiation.md",
            "distinctness_operation_terminal_summary_reference": root / "distinctness.md",
            "basis_emission_operation_terminal_summary_reference": root / "basis_emission.md",
            "scope_division_declaration_boundary_terminal_summary_reference": root / "scope_boundary.md",
        }
        content = {
            "operation_spec_reference": self.valid_operation_spec_text(),
            "receipt_boundary_terminal_summary_reference": self.valid_receipt_boundary_summary_text(),
            "scope_division_declaration_operation_terminal_summary_reference": self.valid_scope_division_operation_summary_text(),
            "existence_claim_evidence_check_terminal_summary_reference": self.valid_existence_claim_evidence_check_summary_text(),
            "differentiation_operation_terminal_summary_reference": self.valid_differentiation_operation_summary_text(),
            "distinctness_operation_terminal_summary_reference": self.valid_distinctness_operation_summary_text(),
            "basis_emission_operation_terminal_summary_reference": self.valid_basis_emission_operation_summary_text(),
            "scope_division_declaration_boundary_terminal_summary_reference": self.valid_scope_division_declaration_boundary_summary_text(),
        }
        for key, path in paths.items():
            self.write_markdown(path, content[key])
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request(
            **{key: str(path) for key, path in paths.items()}
        )
        return request, paths

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def failed_check_count(self, result: dict[str, object]) -> int:
        summary = result.get(self.SUMMARY_KEY)
        if isinstance(summary, dict):
            return int(summary.get("failed_check_count", 0))
        return 0

    def passed_check_count(self, result: dict[str, object]) -> int:
        summary = result.get(self.SUMMARY_KEY)
        if isinstance(summary, dict):
            return int(summary.get("passed_check_count", 0))
        return 0

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def assert_recorded_not_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))
        self.assertEqual(self.failed_check_count(result), 0)

    def assert_blocked_with_public_code(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_false_non_claims(result)

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        checks = result.get(self.CHECKS_KEY)
        self.assertIsInstance(checks, list)
        for check in checks:
            if not isinstance(check, dict):
                continue
            for key in ("block_code", "failure_code"):
                value = check.get(key)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_operation_has_no_wrapper_fields(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        self.assertFalse(self.WRAPPER_FIELDS.intersection(operation), self.WRAPPER_FIELDS.intersection(operation))

    def assert_non_authorizing_posture(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in (
            "audit_performed",
            "declaration_admitted_as_standing_basis",
            "digest_treated_as_standing",
            "hash_treated_as_standing",
            "custody_treated_as_standing",
            "transcription_treated_as_standing",
            "signature_treated_as_scope_standing",
            "signature_treated_as_candidate_specific_basis_emission",
            "signature_treated_as_distinctness_support",
            "motion_regulation_division_audited",
            "motion_regulation_division_accepted",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "candidate_specific_distinctness_basis_emission_operation_rerun",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
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
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(operation.get(key), False, key)

    def assert_no_raw_body_returned(self, result: dict[str, object], sentinels: tuple[str, ...]) -> None:
        serialized = json.dumps(result, ensure_ascii=True, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min",
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path",
            "write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_result",
            "build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min")
        self.assertEqual(resolver.OPERATION_ID, "descendant_body_candidate_authored_scope_division_declaration_receipt_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "EXTERNAL_AUTHORED_DECLARATION_METADATA_RECEIPT_FOR_AUDIT_ONLY")
        self.assertEqual(resolver.UPSTREAM_BOUNDARY_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY")
        self.assertEqual(resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_BOUNDARY_RECORDED")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "RECEIPT_THEN_AUDIT_ONLY")
        self.assertEqual(resolver.RECEIVED_MATERIAL_TYPE, "EXTERNAL_AUTHORED_SIGNED_DECLARATION")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_TITLE, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_VERSION, "v2")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_DATE, "10 July 2026")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_AUTHOR, "Marko Markota")
        self.assertIs(resolver.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_PRESENT, True)
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE, "AUTHORSHIP_ATTESTATION_ONLY")
        self.assertEqual(resolver.RECEIVED_MATERIAL_EXPECTED_PREDECESSOR, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1")
        self.assertEqual(resolver.RECEIVED_MATERIAL_PREDECESSOR_ROLE, "REFERENCED_PREDECESSOR_ONLY")
        self.assertIn(resolver.OUTCOME_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_BLOCKED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_NOT_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min"))
        for code in (
            "REQUEST_NOT_MAPPING",
            "OPERATION_SPEC_MARKER_MISSING",
            "MATERIAL_METADATA_MISSING_OR_INVALID",
            "DIGEST_REQUEST_MISSING_MATERIAL_PATH",
            "DIGEST_ALGORITHM_UNSUPPORTED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "REQUESTED_RAW_MATERIAL_BODY_RETURN",
            "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_synthetic_metadata_only_request_records_receipt_operation_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            self.assertEqual(result["authored_scope_division_declaration_receipt_operation_metadata"]["result_version"], "0.1.0")
            self.assertEqual(result["authored_scope_division_declaration_receipt_operation_metadata"]["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertGreater(self.passed_check_count(result), 0)
            expected_sections = {
                "authored_scope_division_declaration_receipt_operation_metadata",
                "declared_authored_scope_division_declaration_receipt_operation_basis",
                "upstream_basis",
                self.OPERATION_KEY,
                self.CHECKS_KEY,
                "authored_scope_division_declaration_receipt_operation_statement",
                "authored_scope_division_declaration_receipt_operation_non_meaning",
                "receipt_metadata",
                "permitted_future_route",
                "blocked_routes",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                self.SUMMARY_KEY,
            }
            self.assertTrue(expected_sections.issubset(result))
            operation = self.operation(result)
            for key, value in (
                ("operation_id", resolver.OPERATION_ID),
                ("operation_type", resolver.OPERATION_TYPE),
                ("operation_version", resolver.OPERATION_VERSION),
                ("operation_scope", resolver.OPERATION_SCOPE),
                ("upstream_boundary_type", resolver.UPSTREAM_BOUNDARY_TYPE),
                ("upstream_boundary_outcome_required", resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED),
                ("admissible_future_route", resolver.ADMISSIBLE_FUTURE_ROUTE),
                ("received_material_type", resolver.RECEIVED_MATERIAL_TYPE),
                ("received_material_filename", resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME),
                ("received_material_title", resolver.RECEIVED_MATERIAL_EXPECTED_TITLE),
                ("received_material_version", resolver.RECEIVED_MATERIAL_EXPECTED_VERSION),
                ("received_material_date", resolver.RECEIVED_MATERIAL_EXPECTED_DATE),
                ("received_material_author", resolver.RECEIVED_MATERIAL_EXPECTED_AUTHOR),
                ("received_material_signature_present", True),
                ("received_material_signature_role", resolver.RECEIVED_MATERIAL_EXPECTED_SIGNATURE_ROLE),
                ("received_material_predecessor", resolver.RECEIVED_MATERIAL_EXPECTED_PREDECESSOR),
                ("received_material_predecessor_role", resolver.RECEIVED_MATERIAL_PREDECESSOR_ROLE),
            ):
                self.assertEqual(operation[key], value)
            for key in (
                "receipt_operation_recorded",
                "receipt_performed",
                "contribution_map_present",
                "sibling_non_monarchy_present",
                "receipt_sealing_posture_present",
                "coupling_not_assigned_present",
                "no_third_model_present",
                "lineage_constraints_present",
                "for_audit_only",
                "target_operation_spec_markers_present",
                "receipt_boundary_terminal_summary_markers_present",
                "scope_division_declaration_operation_terminal_summary_markers_present",
                "existence_claim_evidence_check_terminal_summary_markers_present",
                "differentiation_operation_terminal_summary_markers_present",
                "distinctness_operation_terminal_summary_markers_present",
                "basis_emission_operation_terminal_summary_markers_present",
                "scope_division_declaration_boundary_terminal_summary_markers_present",
            ):
                self.assertIs(operation[key], True, key)
            for key in ("material_path_recorded", "digest_recorded", "custody_posture_recorded", "text_extraction_posture_recorded"):
                self.assertIs(operation[key], False, key)
            self.assert_non_authorizing_posture(result)
            self.assert_canonical_false_non_claims(result)
            self.assert_operation_has_no_wrapper_fields(result)
            self.assertIn("later separately bounded audit", " ".join(result["permitted_future_route"]))
            blocked = " ".join(result["blocked_routes"])
            for marker in ("receipt", "digest", "hash", "custody", "transcription", "signature", "declaration", "coupling", "third-model"):
                self.assertIn(marker, blocked)
            self.assertIn("authored declaration audit operation", result["what_remains_open"])

    def test_default_live_repo_target_records_metadata_only_receipt_if_present(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request()
        paths = [request["operation_spec_reference"]] + [request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS]
        if not all((REPO_ROOT / str(path)).is_file() for path in paths):
            self.skipTest("default receipt-operation references are not all present")
        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
        self.assert_recorded_not_blocked(result)
        operation = self.operation(result)
        self.assertIs(operation["receipt_operation_recorded"], True)
        self.assertIs(operation["receipt_performed"], True)
        self.assertIs(operation["audit_performed"], False)
        self.assertIs(operation["material_path_recorded"], False)
        self.assertIs(operation["digest_recorded"], False)
        self.assertIs(operation["custody_posture_recorded"], False)
        self.assertIs(operation["text_extraction_posture_recorded"], False)
        self.assert_non_authorizing_posture(result)
        self.assert_canonical_false_non_claims(result)

    def test_digest_computation_records_sha256_metadata_only(self) -> None:
        material = b"authored declaration v2 test bytes"
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, _ = self.make_synthetic_request(root)
            material_path = self.write_material_bytes(root / "material.pdf", material)
            request.update(
                {
                    "material_path": str(material_path),
                    "request_digest_computation": True,
                    "digest_algorithm": "SHA-256",
                    "digest_scope": resolver.DIGEST_SCOPE,
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            metadata = result["receipt_metadata"]
            self.assertIs(metadata["digest_recorded"], True)
            self.assertEqual(metadata["digest_algorithm"], "SHA-256")
            self.assertEqual(metadata["digest_scope"], resolver.DIGEST_SCOPE)
            self.assertEqual(metadata["digest_value"], hashlib.sha256(material).hexdigest())
            self.assertIs(metadata["material_path_recorded"], True)
            self.assert_non_authorizing_posture(result)
            self.assert_no_raw_body_returned(result, (material.decode("ascii"),))

    def test_supplied_digest_metadata_without_computation_is_metadata_only(self) -> None:
        supplied = "a" * 64
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            request.update(
                {
                    "request_digest_computation": False,
                    "digest_algorithm": "SHA-256",
                    "digest_scope": resolver.DIGEST_SCOPE,
                    "digest_value": supplied,
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            operation = self.operation(result)
            self.assertIs(operation["digest_recorded"], True)
            self.assertEqual(operation["digest_value"], supplied)
            self.assertEqual(operation["digest_algorithm"], "SHA-256")
            self.assertEqual(operation["digest_scope"], resolver.DIGEST_SCOPE)
            self.assert_non_authorizing_posture(result)

            bad_algorithm = copy.deepcopy(request)
            bad_algorithm["digest_algorithm"] = "SHA-1"
            bad_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(bad_algorithm)
            self.assert_blocked_with_public_code(bad_result)
            self.assertIn(self.block_code(bad_result), {"DIGEST_ALGORITHM_UNSUPPORTED", "MATERIAL_METADATA_MISSING_OR_INVALID"})

            missing_path = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_request(
                **{key: str(path) for key, path in self.make_synthetic_request(Path(temp_dir) / "missing")[1].items()},
                request_digest_computation=True,
                digest_algorithm="SHA-256",
                material_path=None,
            )
            missing_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(missing_path)
            self.assert_blocked_with_public_code(missing_result)
            self.assertIn(self.block_code(missing_result), {"DIGEST_REQUEST_MISSING_MATERIAL_PATH", "MATERIAL_METADATA_MISSING_OR_INVALID"})

    def test_custody_and_text_extraction_posture_are_metadata_only(self) -> None:
        cases = (
            ("CUSTODY_RECORDED_FOR_AUDIT_ONLY", "TRANSCRIPTION_NOT_PERFORMED"),
            ("CUSTODY_NOT_RECORDED", "TEXT_EXTRACTED_FOR_AUDIT_ONLY"),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            for index, (custody, text_posture) in enumerate(cases):
                with self.subTest(custody=custody, text_posture=text_posture):
                    request, _ = self.make_synthetic_request(Path(temp_dir) / str(index))
                    request["custody_posture"] = custody
                    request["text_extraction_posture"] = text_posture
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
                    self.assert_recorded_not_blocked(result)
                    metadata = result["receipt_metadata"]
                    self.assertIs(metadata["custody_posture_recorded"], True)
                    self.assertEqual(metadata["custody_posture"], custody)
                    self.assertIs(metadata["text_extraction_posture_recorded"], True)
                    self.assertEqual(metadata["text_extraction_posture"], text_posture)
                    self.assert_non_authorizing_posture(result)
                    self.assert_no_raw_body_returned(result, ("RAW_MATERIAL_BODY_MUST_NOT_RETURN",))

    def test_do_not_record_intent_does_not_record_operation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            request["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(result["block"]["blocked"], False)
            operation = self.operation(result)
            self.assertIs(operation["receipt_operation_recorded"], False)
            self.assertIs(operation["receipt_performed"], False)
            self.assert_non_authorizing_posture(result)
            self.assert_canonical_false_non_claims(result)

    def test_explicit_block_intent_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            request["intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_blocked_with_public_code(result)
            self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")
            operation = self.operation(result)
            self.assertIs(operation["receipt_operation_recorded"], False)
            self.assertIs(operation["receipt_performed"], False)
            self.assert_non_authorizing_posture(result)

    def test_request_shape_and_exact_field_blocking(self) -> None:
        non_mapping = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min([])
        self.assert_blocked_with_public_code(non_mapping)
        cases = (
            ("unsupported_intent", lambda request: request.__setitem__("intent", "UNSUPPORTED")),
            ("missing_operation_id", lambda request: request.pop("operation_id")),
            ("wrong_operation_id", lambda request: request.__setitem__("operation_id", "wrong")),
            ("missing_operation_type", lambda request: request.pop("operation_type")),
            ("wrong_operation_type", lambda request: request.__setitem__("operation_type", "wrong")),
            ("missing_operation_version", lambda request: request.pop("operation_version")),
            ("wrong_operation_version", lambda request: request.__setitem__("operation_version", "wrong")),
            ("missing_operation_scope", lambda request: request.pop("operation_scope")),
            ("wrong_operation_scope", lambda request: request.__setitem__("operation_scope", "wrong")),
            ("wrong_upstream_type", lambda request: request.__setitem__("upstream_boundary_type", "wrong")),
            ("wrong_upstream_outcome", lambda request: request.__setitem__("upstream_boundary_outcome_required", "wrong")),
            ("wrong_future_route", lambda request: request.__setitem__("admissible_future_route", "wrong")),
            ("missing_operation_spec", lambda request: request.pop("operation_spec_reference")),
            ("missing_upstream_reference", lambda request: request.pop("receipt_boundary_terminal_summary_reference")),
            ("wrong_material_type", lambda request: request.__setitem__("received_material_type", "wrong")),
            ("wrong_filename", lambda request: request.__setitem__("received_material_filename", "wrong")),
            ("wrong_title", lambda request: request.__setitem__("received_material_title", "wrong")),
            ("wrong_version", lambda request: request.__setitem__("received_material_version", "wrong")),
            ("wrong_date", lambda request: request.__setitem__("received_material_date", "wrong")),
            ("wrong_author", lambda request: request.__setitem__("received_material_author", "wrong")),
            ("signature_false", lambda request: request.__setitem__("received_material_signature_present", False)),
            ("wrong_signature_role", lambda request: request.__setitem__("received_material_signature_role", "wrong")),
            ("wrong_predecessor", lambda request: request.__setitem__("received_material_predecessor", "wrong")),
            ("wrong_predecessor_role", lambda request: request.__setitem__("received_material_predecessor_role", "wrong")),
            ("contribution_map_false", lambda request: request.__setitem__("contribution_map_present", False)),
            ("sibling_non_monarchy_false", lambda request: request.__setitem__("sibling_non_monarchy_present", False)),
            ("receipt_sealing_false", lambda request: request.__setitem__("receipt_sealing_posture_present", False)),
            ("coupling_not_assigned_false", lambda request: request.__setitem__("coupling_not_assigned_present", False)),
            ("no_third_model_false", lambda request: request.__setitem__("no_third_model_present", False)),
            ("lineage_constraints_false", lambda request: request.__setitem__("lineage_constraints_present", False)),
            ("for_audit_only_false", lambda request: request.__setitem__("for_audit_only", False)),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            for name, mutate in cases:
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    mutate(malformed)
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_non_authorizing_posture(result)

    def test_marker_validation_blocking_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, paths = self.make_synthetic_request(root)
            fields = tuple(paths)
            for index, field in enumerate(fields):
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    path = paths[field]
                    original = path.read_text(encoding="utf-8")
                    path.write_text("marker class intentionally absent", encoding="utf-8")
                    try:
                        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    finally:
                        path.write_text(original, encoding="utf-8")
                    self.assert_blocked_with_public_code(result)
                    self.assert_non_authorizing_posture(result)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            for field in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_non_authorizing_posture(result)

    def test_required_false_top_level_posture_blocks(self) -> None:
        fields = (
            "receipt_operation_recorded",
            "audit_performed",
            "declaration_admitted_as_standing_basis",
            "digest_treated_as_standing",
            "hash_treated_as_standing",
            "custody_treated_as_standing",
            "transcription_treated_as_standing",
            "signature_treated_as_scope_standing",
            "signature_treated_as_candidate_specific_basis_emission",
            "signature_treated_as_distinctness_support",
            "authored_scope_claim_accepted_as_standing",
            "motion_scope_accepted_as_standing",
            "regulation_scope_accepted_as_standing",
            "motion_regulation_division_audited",
            "motion_regulation_division_accepted",
            "sibling_non_monarchy_audited",
            "sibling_non_monarchy_accepted",
            "coupling_not_assigned_audited",
            "coupling_not_assigned_accepted",
            "no_third_model_audited",
            "no_third_model_accepted",
            "lineage_constraints_audited",
            "lineage_constraints_accepted",
            "candidate_a_scope_declared",
            "candidate_b_scope_declared",
            "basis_bearing_scope_division_declared",
            "candidate_specific_content_emitted",
            "separate_seal_material_emitted",
            "separate_lineage_receipt_material_emitted",
            "separate_digest_material_emitted",
            "candidate_specific_distinctness_basis_emission_operation_rerun",
            "distinctness_operation_rerun",
            "distinctness_supported_recorded",
            "candidate_records_marked_distinct",
            "candidate_records_distinct",
            "candidate_standing_authorized",
            "descendant_body_created",
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
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
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
            "direct_receipt_to_audit_completion_conversion",
            "direct_receipt_to_standing_conversion",
            "direct_receipt_to_scope_declaration_conversion",
            "direct_receipt_to_candidate_specific_basis_emission_conversion",
            "direct_receipt_to_distinctness_support_conversion",
            "direct_digest_to_truth_conversion",
            "direct_hash_to_standing_conversion",
            "direct_custody_to_standing_conversion",
            "direct_transcription_to_standing_conversion",
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
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            for field in fields:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_non_authorizing_posture(result)

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_authorizing_posture(result)

            for name, malformed_non_claims in (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            ):
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"] = malformed_non_claims
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(malformed)
                    self.assert_blocked_with_public_code(result)
                    self.assert_canonical_false_non_claims(result)

    def test_sanitizer_behavior(self) -> None:
        sentinels = (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, paths = self.make_synthetic_request(root)
            paths["operation_spec_reference"].write_text(
                paths["operation_spec_reference"].read_text(encoding="utf-8")
                + "\nRAW_MARKDOWN_BODY_MUST_NOT_RETURN\nHIDDEN_REPO_STATE_MUST_NOT_RETURN\n",
                encoding="utf-8",
            )
            material_path = self.write_material_bytes(root / "material.pdf", b"RAW_MATERIAL_BODY_MUST_NOT_RETURN")
            request.update(
                {
                    "material_path": str(material_path),
                    "request_digest_computation": True,
                    "digest_algorithm": "SHA-256",
                    "raw_material_body": "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
                    "raw_markdown_body": "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
                    "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                    "current_working_tree": "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            self.assert_no_raw_body_returned(result, sentinels)
            self.assertEqual(self.operation(result)["received_material_filename"], resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME)
            self.assertIs(self.operation(result)["digest_recorded"], True)

            raw_request = copy.deepcopy(request)
            raw_request["return_raw_material_body"] = True
            raw_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(raw_request)
            self.assert_blocked_with_public_code(raw_result)
            markdown_request = copy.deepcopy(request)
            markdown_request["return_raw_markdown_body"] = True
            markdown_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(markdown_request)
            self.assert_blocked_with_public_code(markdown_result)

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, _ = self.make_synthetic_request(root / "inputs")
            request_path = root / self.safe_json_filename("valid request")
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(request_path)
            self.assert_recorded_not_blocked(result)

            missing = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(root / "missing.json")
            self.assert_blocked_with_public_code(missing)
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(malformed_path)
            self.assert_blocked_with_public_code(malformed)
            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_from_path(array_path)
            self.assert_blocked_with_public_code(array)

            output_path = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_result(
                result, root / "output"
            )
            self.assertTrue(output_path.is_file())
            self.assertIsInstance(json.loads(output_path.read_text(encoding="utf-8")), dict)
            second_output_path = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_result(
                result, root / "output"
            )
            self.assertNotEqual(output_path, second_output_path)
            self.assertTrue(second_output_path.is_file())
            self.assertIn("authored_scope_division_declaration_receipt_operation_v0_min_result", output_path.name)
            self.assertIn(
                "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min",
                str(resolver.OUTPUT_ROOT),
            )
            forbidden_roots = (
                "receipt_boundary",
                "basis_emission",
                "distinctness",
                "differentiation",
                "runtime",
                "daemon",
                "api",
                "externalization",
            )
            self.assertFalse(any(root_name in str(output_path) for root_name in forbidden_roots))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, paths = self.make_synthetic_request(root)
            request.update(
                {
                    "custody_posture": "CUSTODY_NOT_RECORDED",
                    "text_extraction_posture": "TEXT_EXTRACTED_FOR_AUDIT_ONLY",
                    "raw_material_body": "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
                }
            )
            before_request = copy.deepcopy(request)
            before_files = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            self.assertEqual(request, before_request)
            self.assertEqual({key: path.read_text(encoding="utf-8") for key, path in paths.items()}, before_files)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            self.assert_recorded_not_blocked(result)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_summary(result)
            for key, value in (
                ("outcome", resolver.OUTCOME_RECORDED),
                ("result_version", resolver.RESULT_VERSION),
                ("resolver_module", resolver.RESOLVER_MODULE),
                ("operation_id", resolver.OPERATION_ID),
                ("operation_type", resolver.OPERATION_TYPE),
                ("operation_version", resolver.OPERATION_VERSION),
                ("operation_scope", resolver.OPERATION_SCOPE),
                ("upstream_boundary_type", resolver.UPSTREAM_BOUNDARY_TYPE),
                ("upstream_boundary_outcome_required", resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED),
                ("admissible_future_route", resolver.ADMISSIBLE_FUTURE_ROUTE),
                ("received_material_type", resolver.RECEIVED_MATERIAL_TYPE),
                ("received_material_filename", resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME),
                ("receipt_operation_recorded", True),
                ("receipt_performed", True),
                ("audit_performed", False),
                ("declaration_admitted_as_standing_basis", False),
                ("digest_recorded", False),
                ("material_path_recorded", False),
                ("custody_posture_recorded", False),
                ("text_extraction_posture_recorded", False),
            ):
                self.assertEqual(summary[key], value)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertTrue(summary["selected_target_spec_path"])
            self.assertTrue(summary["completed_receipt_boundary_terminal_summary_path"])
            self.assertTrue(summary["completed_scope_division_operation_terminal_summary_path"])
            self.assertIs(summary["result_level_non_claims_canonical_false"], True)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS[-8:]:
                self.assertIs(summary[key], True, key)

    def test_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_synthetic_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min(request)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            operation = self.operation(result)
            self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(operation["received_material_filename"], resolver.RECEIVED_MATERIAL_EXPECTED_FILENAME)
            self.assertIs(operation["receipt_operation_recorded"], True)
            self.assertIs(operation["receipt_performed"], True)
            self.assertIs(operation["audit_performed"], False)
            self.assert_non_authorizing_posture(result)
            self.assert_operation_has_no_wrapper_fields(result)
            self.assert_canonical_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
