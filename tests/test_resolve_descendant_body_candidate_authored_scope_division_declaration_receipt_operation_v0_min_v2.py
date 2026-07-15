"""V2 tests for metadata-only authored declaration receipt.

V1 remains preserved lineage. This successor suite verifies only the v2
top-level required-false posture blocking repair and preserved receipt bounds.
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

import resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2 as resolver


class AuthoredScopeDivisionDeclarationReceiptOperationV2Tests(unittest.TestCase):
    """Bounded v2 verification without audit, standing, or source-body return."""

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
        return f"{index:03d}_{safe}.json" if index is not None else f"{safe}.json"

    def write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture path collision: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def write_bytes(self, path: Path, content: bytes) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture path collision: {path}")
        path.write_bytes(content)
        return path

    def operation_spec_text(self) -> str:
        false_postures = "\n".join(f"{key} = false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS)
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
                "contribution map contribution-map sibling non-monarchy sibling-non-monarchy",
                "receipt-sealing posture receipt-sealing coupling-not-assigned no-third-model lineage constraints lineage-constraints",
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
                "direct digest-to-truth",
                "hash-to-standing custody-to-standing transcription-to-standing signature-to-standing",
                "direct declaration-to-scope-standing",
                "direct coupling instantiation",
                "third-candidate third-model repository scan affected-file repair prior unsupported-claim validation",
                "This operation spec defines only a future receipt operation shape",
                "The prior operation line remains at REQUIRES_ADDITIONAL_BASIS until receipt, audit, and any successor closure are separately bounded and passed.",
                false_postures,
            )
        )

    def fixture_texts(self) -> dict[str, str]:
        return {
            "operation_spec_reference": self.operation_spec_text(),
            "receipt_boundary_terminal_summary_reference": "\n".join(
                (
                    resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED,
                    "failed_check_count = 0",
                    "passed_check_count = 84",
                    "future_receipt_operation_type = DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION",
                    "external_declaration_role = PROPOSED_AUTHORED_AUDIT_MATERIAL",
                )
            ),
            "scope_division_declaration_operation_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                    "failed_check_count = 0",
                    "passed_check_count = 96",
                    "missing non-cosmetic candidate A scope declaration",
                    "missing non-cosmetic candidate B scope declaration",
                    "missing basis-bearing scope division declaration",
                )
            ),
            "existence_claim_evidence_check_terminal_summary_reference": "\n".join(
                (
                    "UNSUPPORTED",
                    "descendant_body_basis_candidate_a_created = true",
                    "descendant_body_basis_candidate_b_created = true",
                    "descendant_body_basis_derivation_event_recorded = true",
                )
            ),
            "differentiation_operation_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",
                    "exactly two result-contained non-standing candidate records",
                    "candidate records remain non-standing",
                    "candidate records are not descendant bodies",
                    "crossing_authorized = false",
                    "relation_created = false",
                )
            ),
            "distinctness_operation_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                    "NOT_DISTINCT",
                    "distinctness_supported = false",
                    "candidate_record_count_compared = 2",
                )
            ),
            "basis_emission_operation_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",
                    "REQUIRES_ADDITIONAL_BASIS",
                    "candidate_specific_content_emitted = false",
                    "separate_seal_material_emitted = false",
                    "separate_lineage_receipt_material_emitted = false",
                    "separate_digest_material_emitted = false",
                )
            ),
            "scope_division_declaration_boundary_terminal_summary_reference": "\n".join(
                (
                    "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
                    "RECORDED",
                    "future_scope_declaration_operation_shape_allowed = true",
                    "candidate_a_scope_not_declared = true",
                    "candidate_b_scope_not_declared = true",
                    "basis_bearing_scope_division_not_declared = true",
                    "scope_label_laundering_not_allowed = true",
                )
            ),
        }

    def make_request(self, root: Path) -> tuple[dict[str, object], dict[str, Path]]:
        texts = self.fixture_texts()
        paths = {key: root / f"{index:02d}_{key}.md" for index, key in enumerate(texts)}
        for key, text in texts.items():
            self.write_text(paths[key], text)
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_request(
            **{key: str(path) for key, path in paths.items()}
        )
        return request, paths

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_count(self, result: dict[str, object]) -> int:
        summary = result.get(self.SUMMARY_KEY)
        return int(summary.get("failed_check_count", 0)) if isinstance(summary, dict) else 0

    def passed_count(self, result: dict[str, object]) -> int:
        summary = result.get(self.SUMMARY_KEY)
        return int(summary.get("passed_check_count", 0)) if isinstance(summary, dict) else 0

    def assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims.get(key), False, key)

    def assert_recorded(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_count(result), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_count(result), 0)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        checks = result.get(self.CHECKS_KEY)
        self.assertIsInstance(checks, list)
        for check in checks:
            if isinstance(check, dict):
                for code_key in ("block_code", "failure_code"):
                    code = check.get(code_key)
                    if code is not None:
                        self.assertIn(code, resolver.BLOCK_CODES)
        self.assert_non_claims_false(result)

    def assert_no_wrapper_fields(self, result: dict[str, object]) -> None:
        self.assertFalse(self.WRAPPER_FIELDS.intersection(self.operation(result)))

    def assert_non_authorizing(self, result: dict[str, object]) -> None:
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

    def assert_no_raw_return(self, result: dict[str, object], sentinels: tuple[str, ...]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def test_public_api_and_constants_v2(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2",
            "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_from_path",
            "write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_result",
            "build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_summary",
            "build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2")
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
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {resolver.OUTCOME_RECORDED, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED})
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2"))
        self.assertNotEqual(str(resolver.OUTPUT_ROOT), str(REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min"))
        self.assertIn("PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED", resolver.BLOCK_CODES)

    def test_default_synthetic_metadata_only_request_records_receipt_operation_only_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            self.assertGreater(self.passed_count(result), 0)
            metadata = result["authored_scope_division_declaration_receipt_operation_metadata"]
            self.assertEqual(metadata["result_version"], "0.2.0")
            self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)
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
                ("received_material_status", "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY"),
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
            self.assert_non_authorizing(result)
            self.assert_non_claims_false(result)
            self.assert_no_wrapper_fields(result)
            self.assertIn("later separately bounded audit", " ".join(result["permitted_future_route"]))
            self.assertIn("authored declaration audit operation", result["what_remains_open"])

    def test_default_live_target_records_metadata_only_receipt_v2(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_request()
        references = [request["operation_spec_reference"]] + [request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS]
        if not all((REPO_ROOT / str(reference)).is_file() for reference in references):
            self.skipTest("default target files are unavailable")
        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
        self.assert_recorded(result)
        self.assertEqual(result[self.SUMMARY_KEY]["result_version"], "0.2.0")
        self.assertEqual(result[self.SUMMARY_KEY]["resolver_module"], resolver.RESOLVER_MODULE)
        operation = self.operation(result)
        self.assertIs(operation["receipt_operation_recorded"], True)
        self.assertIs(operation["receipt_performed"], True)
        self.assertIs(operation["audit_performed"], False)
        self.assertIs(operation["material_path_recorded"], False)
        self.assertIs(operation["digest_recorded"], False)
        self.assert_non_authorizing(result)
        self.assert_non_claims_false(result)

    def test_digest_computation_records_sha256_metadata_only_v2(self) -> None:
        payload = b"v2 authored declaration receipt bytes"
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, _ = self.make_request(root)
            material = self.write_bytes(root / "material.pdf", payload)
            request.update(
                {
                    "material_path": str(material),
                    "request_digest_computation": True,
                    "digest_algorithm": "SHA-256",
                    "digest_scope": resolver.DIGEST_SCOPE,
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            metadata = result["receipt_metadata"]
            self.assertIs(metadata["digest_recorded"], True)
            self.assertEqual(metadata["digest_algorithm"], "SHA-256")
            self.assertEqual(metadata["digest_scope"], resolver.DIGEST_SCOPE)
            self.assertEqual(metadata["digest_value"], hashlib.sha256(payload).hexdigest())
            self.assertIs(metadata["material_path_recorded"], True)
            self.assert_non_authorizing(result)
            self.assert_no_raw_return(result, (payload.decode("ascii"),))

    def test_supplied_digest_metadata_without_computation_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            request.update(
                {
                    "digest_value": "f" * 64,
                    "digest_algorithm": "SHA-256",
                    "digest_scope": resolver.DIGEST_SCOPE,
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            operation = self.operation(result)
            self.assertIs(operation["digest_recorded"], True)
            self.assertEqual(operation["digest_value"], "f" * 64)
            self.assertEqual(operation["digest_scope"], resolver.DIGEST_SCOPE)
            self.assert_non_authorizing(result)

            unsupported = copy.deepcopy(request)
            unsupported["digest_algorithm"] = "SHA-1"
            unsupported_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(unsupported)
            self.assert_blocked(unsupported_result)

            missing_material = copy.deepcopy(request)
            missing_material.update({"request_digest_computation": True, "digest_value": None, "material_path": None})
            missing_result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(missing_material)
            self.assert_blocked(missing_result)

    def test_custody_and_text_extraction_posture_metadata_only_v2(self) -> None:
        cases = (
            ("CUSTODY_RECORDED_FOR_AUDIT_ONLY", "TRANSCRIPTION_NOT_PERFORMED"),
            ("CUSTODY_NOT_RECORDED", "TEXT_EXTRACTED_FOR_AUDIT_ONLY"),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            for index, (custody, extraction) in enumerate(cases):
                with self.subTest(custody=custody, extraction=extraction):
                    request, _ = self.make_request(Path(temp_dir) / str(index))
                    request["custody_posture"] = custody
                    request["text_extraction_posture"] = extraction
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
                    self.assert_recorded(result)
                    metadata = result["receipt_metadata"]
                    self.assertIs(metadata["custody_posture_recorded"], True)
                    self.assertEqual(metadata["custody_posture"], custody)
                    self.assertIs(metadata["text_extraction_posture_recorded"], True)
                    self.assertEqual(metadata["text_extraction_posture"], extraction)
                    self.assert_non_authorizing(result)

    def test_do_not_record_intent_does_not_record_operation_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            request["intent"] = resolver.INTENT_DO_NOT_RECORD
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(result["block"]["blocked"], False)
            self.assertIs(self.operation(result)["receipt_operation_recorded"], False)
            self.assertIs(self.operation(result)["receipt_performed"], False)
            self.assert_non_authorizing(result)
            self.assert_non_claims_false(result)

    def test_explicit_block_intent_blocks_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            request["intent"] = resolver.INTENT_BLOCK
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_blocked(result)
            self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")
            self.assert_non_authorizing(result)

    def test_request_shape_and_exact_field_blocking_v2(self) -> None:
        self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2([]))
        cases = (
            ("unsupported_intent", lambda request: request.__setitem__("intent", "unsupported")),
            ("missing_operation_id", lambda request: request.pop("operation_id")),
            ("wrong_operation_type", lambda request: request.__setitem__("operation_type", "wrong")),
            ("wrong_operation_version", lambda request: request.__setitem__("operation_version", "wrong")),
            ("wrong_operation_scope", lambda request: request.__setitem__("operation_scope", "wrong")),
            ("wrong_boundary_type", lambda request: request.__setitem__("upstream_boundary_type", "wrong")),
            ("wrong_boundary_outcome", lambda request: request.__setitem__("upstream_boundary_outcome_required", "wrong")),
            ("wrong_route", lambda request: request.__setitem__("admissible_future_route", "wrong")),
            ("missing_operation_spec", lambda request: request.pop("operation_spec_reference")),
            ("missing_boundary_summary", lambda request: request.pop("receipt_boundary_terminal_summary_reference")),
            ("wrong_material_type", lambda request: request.__setitem__("received_material_type", "wrong")),
            ("wrong_filename", lambda request: request.__setitem__("received_material_filename", "wrong")),
            ("wrong_title", lambda request: request.__setitem__("received_material_title", "wrong")),
            ("wrong_version", lambda request: request.__setitem__("received_material_version", "wrong")),
            ("wrong_date", lambda request: request.__setitem__("received_material_date", "wrong")),
            ("wrong_author", lambda request: request.__setitem__("received_material_author", "wrong")),
            ("signature_false", lambda request: request.__setitem__("received_material_signature_present", False)),
            ("wrong_predecessor", lambda request: request.__setitem__("received_material_predecessor", "wrong")),
            ("contribution_false", lambda request: request.__setitem__("contribution_map_present", False)),
            ("sibling_false", lambda request: request.__setitem__("sibling_non_monarchy_present", False)),
            ("sealing_false", lambda request: request.__setitem__("receipt_sealing_posture_present", False)),
            ("coupling_false", lambda request: request.__setitem__("coupling_not_assigned_present", False)),
            ("third_model_false", lambda request: request.__setitem__("no_third_model_present", False)),
            ("lineage_false", lambda request: request.__setitem__("lineage_constraints_present", False)),
            ("audit_only_false", lambda request: request.__setitem__("for_audit_only", False)),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            for name, mutate in cases:
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    mutate(malformed)
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(malformed)
                    self.assert_blocked(result)
                    self.assert_non_authorizing(result)

    def test_marker_validation_blocking_behavior_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, paths = self.make_request(Path(temp_dir))
            for field, path in paths.items():
                with self.subTest(field=field):
                    original = path.read_text(encoding="utf-8")
                    path.write_text("required marker class removed", encoding="utf-8")
                    try:
                        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(copy.deepcopy(request))
                    finally:
                        path.write_text(original, encoding="utf-8")
                    self.assert_blocked(result)
                    self.assert_non_authorizing(result)

    def test_prohibited_request_flags_block_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            for field in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(malformed)
                    self.assert_blocked(result)
                    self.assert_non_authorizing(result)

    def test_required_false_top_level_posture_blocks_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    malformed = copy.deepcopy(request)
                    malformed[key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(malformed)
                    self.assert_blocked(result)
                    self.assertEqual(self.block_code(result), "PROHIBITED_TOP_LEVEL_POSTURE_REQUESTED")
                    self.assert_non_authorizing(result)

    def test_required_false_non_claim_canonicalization_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(malformed)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][key], False)
                    self.assert_non_authorizing(result)
            for name, malformed_non_claims in (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            ):
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"] = malformed_non_claims
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(malformed)
                    self.assert_blocked(result)
                    self.assert_non_claims_false(result)

    def test_sanitizer_behavior_v2(self) -> None:
        sentinels = (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, paths = self.make_request(root)
            paths["operation_spec_reference"].write_text(
                paths["operation_spec_reference"].read_text(encoding="utf-8")
                + "\nRAW_MARKDOWN_BODY_MUST_NOT_RETURN\n",
                encoding="utf-8",
            )
            material = self.write_bytes(root / "material.pdf", b"RAW_MATERIAL_BODY_MUST_NOT_RETURN")
            request.update(
                {
                    "material_path": str(material),
                    "request_digest_computation": True,
                    "digest_algorithm": "SHA-256",
                    "raw_material_body": "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
                    "raw_markdown_body": "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
                    "hidden_repo_state": "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
                    "current_working_tree": "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
                }
            )
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            self.assert_no_raw_return(result, sentinels)
            self.assertIs(self.operation(result)["digest_recorded"], True)

            raw_material = copy.deepcopy(request)
            raw_material["return_raw_material_body"] = True
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(raw_material))
            raw_markdown = copy.deepcopy(request)
            raw_markdown["return_raw_markdown_body"] = True
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(raw_markdown))

    def test_path_and_write_behavior_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, _ = self.make_request(root / "inputs")
            request_path = root / self.safe_json_filename("valid request")
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_from_path(request_path)
            self.assert_recorded(result)
            output = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_result(result, root / "output")
            self.assertTrue(output.is_file())
            self.assertIsInstance(json.loads(output.read_text(encoding="utf-8")), dict)
            second = resolver.write_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_result(result, root / "output")
            self.assertNotEqual(output, second)
            self.assertTrue(second.is_file())
            self.assertIn("authored_scope_division_declaration_receipt_operation_v0_min_v2_result", output.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2", str(resolver.OUTPUT_ROOT))

    def test_non_mutation_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request, paths = self.make_request(root)
            request.update(
                {
                    "custody_posture": "CUSTODY_NOT_RECORDED",
                    "text_extraction_posture": "TEXT_EXTRACTED_FOR_AUDIT_ONLY",
                    "direct_signature_to_standing_conversion": False,
                    "raw_material_body": "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
                }
            )
            before_request = copy.deepcopy(request)
            before_files = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            self.assertEqual(request, before_request)
            self.assertEqual({key: path.read_text(encoding="utf-8") for key, path in paths.items()}, before_files)

    def test_summary_behavior_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            self.assert_recorded(result)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_summary(result)
            for key, value in (
                ("outcome", resolver.OUTCOME_RECORDED),
                ("result_version", "0.2.0"),
                ("resolver_module", resolver.RESOLVER_MODULE),
                ("operation_id", resolver.OPERATION_ID),
                ("operation_type", resolver.OPERATION_TYPE),
                ("operation_version", resolver.OPERATION_VERSION),
                ("operation_scope", resolver.OPERATION_SCOPE),
                ("upstream_boundary_type", resolver.UPSTREAM_BOUNDARY_TYPE),
                ("upstream_boundary_outcome_required", resolver.UPSTREAM_BOUNDARY_OUTCOME_REQUIRED),
                ("admissible_future_route", resolver.ADMISSIBLE_FUTURE_ROUTE),
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

    def test_smoke_behavior_v2(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            request, _ = self.make_request(Path(temp_dir))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2(request)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_receipt_operation_v0_min_v2_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.2.0")
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
            self.assert_non_authorizing(result)
            self.assert_no_wrapper_fields(result)
            self.assert_non_claims_false(result)


if __name__ == "__main__":
    unittest.main()
