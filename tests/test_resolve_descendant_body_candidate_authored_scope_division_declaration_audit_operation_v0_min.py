"""Bounded tests for the authored scope-division declaration audit operation."""

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

import resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min as resolver


class AuthoredScopeDivisionDeclarationAuditOperationTests(unittest.TestCase):
    """Exercise bounded audit evaluation without standing or raw-body return."""

    OPERATION_KEY = "descendant_body_candidate_authored_scope_division_declaration_audit_operation"
    CHECKS_KEY = "authored_scope_division_declaration_audit_operation_checks"
    SUMMARY_KEY = "authored_scope_division_declaration_audit_operation_summary"
    WRAPPER_FIELDS = {
        "outcome",
        "block",
        "authored_scope_division_declaration_audit_operation_checks",
        "non_claims",
        "authored_scope_division_declaration_audit_operation_summary",
        "authored_scope_division_declaration_audit_operation_metadata",
    }

    def safe_json_filename(self, name: object, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        return f"{index:03d}_{safe}.json" if index is not None else f"{safe}.json"

    def write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture path collision: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def audit_operation_spec_text(self) -> str:
        return "\n".join(
            (
                "# Descendant Body Candidate Authored Scope Division Declaration Audit Operation V0 Minimum Specification",
                resolver.OPERATION_TYPE,
                resolver.OPERATION_ID,
                resolver.OPERATION_SCOPE,
                resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
                resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED,
                resolver.AUDITED_MATERIAL_EXPECTED_FILENAME,
                resolver.AUDITED_MATERIAL_EXPECTED_VERSION,
                resolver.AUDITED_MATERIAL_EXPECTED_DATE,
                resolver.AUDITED_MATERIAL_EXPECTED_AUTHOR,
                resolver.AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
                resolver.AUDITED_MATERIAL_EXPECTED_PREDECESSOR,
                resolver.AUDITED_MATERIAL_PREDECESSOR_ROLE,
                *resolver.AUDIT_CRITERIA,
                "SATISFIES_MISSING_BASIS_REQUIREMENTS",
                "REQUIRES_ADDITIONAL_BASIS",
                "BLOCKED",
                "Audit permission is not audit completion",
                "Audit result is not standing",
                "Audit result is not scope declaration",
                "Audit result is not basis-gap closure",
                "Audit result is not candidate-specific basis emission",
                "Audit result is not distinctness support",
                "Audit result is not candidate standing",
                "Audit result is not descendant-body creation",
                "Audit result is not relation",
                "Audit result is not runtime",
                "Audit result is not coupling",
                "Audit result is not follow-on authorization",
                "Accepted basis is not standing basis",
                "Candidate A and Candidate B must remain sibling non-standing candidate records",
                "neither candidate may rank above the other",
                "neither may rank above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "Coupling must remain unassigned",
                "Coupling must not be treated as third candidate",
                "Coupling must not be treated as third model",
                "Coupling must not be created by audit",
                "No third candidate is admitted",
                "No third model is admitted",
                "V1 predecessor reference is lineage only",
                "V2 receipt does not erase V1",
                "No orphaned state",
                "No silent reset",
                "No overwrite",
                "failed_check_count = 0",
                "passed_check_count = 91",
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
                "direct audit permission to audit completion",
                "direct audit result to standing conversion",
                "direct audit result to scope declaration conversion",
                "direct audit result to basis-gap closure conversion",
                "direct accepted basis to standing basis conversion",
                "direct audit to candidate-specific-basis-emission conversion",
                "direct audit to distinctness-support conversion",
                "direct audit to candidate-standing conversion",
                "direct audit to descendant-body creation",
                "direct audit to relation creation",
                "direct audit to runtime creation",
                "direct audit to coupling creation",
                "direct audit to third-candidate route",
                "direct audit to third-model route",
                "direct audit to follow-on work",
                "repository scan route",
                "affected-file repair route",
                "prior unsupported claim validation route",
                "This operation spec defines only a future audit operation shape",
                "Even a future audit result satisfying missing basis requirements may only provide basis for a separately bounded successor closure operation",
                "it does not itself close the gap",
                "Open means not scheduled, not authorized, and not executed",
            )
        )

    def receipt_summary_text(self) -> str:
        return "\n".join(
            (
                resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
                "failed_check_count = 0",
                "passed_check_count = 91",
                resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED,
                resolver.AUDITED_MATERIAL_EXPECTED_FILENAME,
                resolver.AUDITED_MATERIAL_EXPECTED_VERSION,
                resolver.AUDITED_MATERIAL_EXPECTED_DATE,
                resolver.AUDITED_MATERIAL_EXPECTED_AUTHOR,
                resolver.AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
                resolver.AUDITED_MATERIAL_EXPECTED_PREDECESSOR,
                resolver.AUDITED_MATERIAL_PREDECESSOR_ROLE,
                "contribution_map_present = true",
                "sibling_non_monarchy_present = true",
                "receipt_sealing_posture_present = true",
                "coupling_not_assigned_present = true",
                "no_third_model_present = true",
                "lineage_constraints_present = true",
                "for_audit_only = true",
            )
        )

    def scope_operation_summary_text(self) -> str:
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

    def fixture_texts(self) -> dict[str, str]:
        return {
            "operation_spec_reference": self.audit_operation_spec_text(),
            "receipt_operation_terminal_summary_reference": self.receipt_summary_text(),
            "scope_division_declaration_operation_terminal_summary_reference": self.scope_operation_summary_text(),
            "existence_claim_evidence_check_terminal_summary_reference": "\n".join(("UNSUPPORTED", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true")),
            "differentiation_operation_terminal_summary_reference": "\n".join(("DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED", "exactly two result-contained non-standing candidate records", "candidate records remain non-standing", "candidate records are not descendant bodies", "crossing_authorized = false", "relation_created = false")),
            "distinctness_operation_terminal_summary_reference": "\n".join(("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT", "NOT_DISTINCT", "distinctness_supported = false", "candidate_record_count_compared = 2")),
            "basis_emission_operation_terminal_summary_reference": "\n".join(("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS", "REQUIRES_ADDITIONAL_BASIS", "candidate_specific_content_emitted = false", "separate_seal_material_emitted = false", "separate_lineage_receipt_material_emitted = false", "separate_digest_material_emitted = false")),
            "scope_division_declaration_boundary_terminal_summary_reference": "\n".join(("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED", "RECORDED", "future_scope_declaration_operation_shape_allowed = true", "candidate_a_scope_not_declared = true", "candidate_b_scope_not_declared = true", "basis_bearing_scope_division_not_declared = true", "scope_label_laundering_not_allowed = true")),
        }

    def complete_audit_fields(self) -> dict[str, object]:
        return {
            "candidate_a_scope_name": "Motion-side admissible variation",
            "candidate_a_mandate": "Motion mandate",
            "candidate_a_responsibility": ["preserve variation", "frequency", "rhythm", "phase", "amplitude", "periodicity", "latency", "no fixed values", "no targets", "no optimization", "no preferred trajectory", "no steering"],
            "candidate_b_scope_name": "Regulation-side admissibility bounds",
            "candidate_b_mandate": "Regulation mandate",
            "candidate_b_responsibility": ["preserve bounds without collapsing motion", "coherence", "stability", "persistence", "damping", "modulation", "thresholds", "ranges", "rejection conditions", "no outcome encoding", "no constants", "no deciding trajectories", "no replacing motion with control"],
            "scope_division_statement": "Candidate A governs the variation side of the parent basis. Candidate B governs the admissibility-bound side of the parent basis. Motion and Regulation do not perform the same function. Neither role may lawfully substitute for the other without freezing the system or allowing collapse.",
            "motion_regulation_difference": "Difference by mandate, function, responsibility, and governed surface.",
            "sibling_non_monarchy_statement": "Candidate A and Candidate B are sibling non-standing candidate records. Neither candidate ranks above the other. Motion is not subordinate to Regulation. Regulation is not sovereign over Motion. Motion does not override Regulation. The division is directional only in function, not hierarchical in rank.",
            "coupling_statement": "Coupling is not assigned to either candidate, not a third candidate, not a third model, not a standing body, and not created by declaration or audit. Coupling may appear later only if separately bounded.",
            "no_third_model_statement": "No third candidate and no third model are admitted.",
            "lineage_statement": "Lineage remains required. No orphaned state, no silent reset, and no overwrite are allowed. Later evolution must be additive and reference prior state. V2 does not erase V1.",
            "non_standing_preservation_statement": "The declaration is for audit and proposed basis only: no standing, no descendant-body creation, no crossing, no relation, no FIELD machinery, no runtime, no currentness, no authority, no follow-on work, no candidate-specific content emission, no seal material, no lineage receipt material, no digest material, no basis-emission operation rerun, no distinctness operation rerun, no candidate records marked distinct, and no candidate standing.",
        }

    def deficient_audit_fields(self, criterion: str) -> dict[str, object]:
        fields = self.complete_audit_fields()
        field_by_criterion = {
            "candidate_a_non_cosmetic_scope_declaration": "candidate_a_mandate",
            "candidate_b_non_cosmetic_scope_declaration": "candidate_b_mandate",
            "basis_bearing_scope_division": "scope_division_statement",
            "motion_regulation_difference_by_mandate_function_responsibility_governed_surface": "motion_regulation_difference",
            "sibling_non_monarchy": "sibling_non_monarchy_statement",
            "coupling_not_assigned": "coupling_statement",
            "no_third_model": "no_third_model_statement",
            "lineage_constraints": "lineage_statement",
            "non_standing_preservation": "non_standing_preservation_statement",
        }
        fields[field_by_criterion[criterion]] = ""
        return fields

    def make_request(self, root: Path, **overrides: object) -> tuple[dict[str, object], dict[str, Path]]:
        texts = self.fixture_texts()
        paths = {key: root / f"{index:02d}_{key}.md" for index, key in enumerate(texts)}
        for key, text in texts.items():
            self.write_markdown(paths[key], text)
        arguments: dict[str, object] = {
            **{key: str(path) for key, path in paths.items()},
            "bounded_audit_fields": self.complete_audit_fields(),
        }
        arguments.update(overrides)
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_request(
            **arguments
        )
        return request, paths

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        operation = result.get(self.OPERATION_KEY)
        self.assertIsInstance(operation, dict)
        return operation

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

    def assert_public_codes(self, result: dict[str, object]) -> None:
        checks = result.get(self.CHECKS_KEY)
        self.assertIsInstance(checks, list)
        for check in checks:
            if isinstance(check, dict):
                for key in ("block_code", "failure_code"):
                    if check.get(key) is not None:
                        self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims.get(key), False, key)

    def assert_operation_separate(self, result: dict[str, object]) -> None:
        self.assertFalse(self.WRAPPER_FIELDS.intersection(self.operation(result)))

    def assert_no_authorization(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation.get(key), False, key)

    def assert_no_raw_return(self, result: dict[str, object], sentinels: tuple[str, ...]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)

    def assert_satisfies(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS)
        self.assertEqual(self.failed_count(result), 0)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(result["block"]["code"])
        self.assert_canonical_non_claims(result)

    def assert_requires_basis(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertIs(result["block"]["blocked"], False)
        self.assert_canonical_non_claims(result)

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_count(result), 0)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_authorization(result)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min",
            "resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path",
            "write_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_result",
            "build_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min")
        self.assertEqual(resolver.OPERATION_ID, "descendant_body_candidate_authored_scope_division_declaration_audit_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "RECEIVED_AUTHORED_DECLARATION_AUDIT_FOR_MISSING_SCOPE_DIVISION_BASIS_ONLY")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED, "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_FILENAME, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_VERSION, "v2")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_DATE, "10 July 2026")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_AUTHOR, "Marko Markota")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE, "AUTHORSHIP_ATTESTATION_ONLY")
        self.assertEqual(resolver.AUDITED_MATERIAL_EXPECTED_PREDECESSOR, "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1")
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, "AUDIT_THEN_SUCCESSOR_CLOSURE_ONLY")
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS,
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min"))
        for code in (
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "AUDIT_OPERATION_SPEC_REFERENCE_MISSING", "AUDIT_OPERATION_SPEC_MARKER_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "MATERIAL_METADATA_MISSING_OR_INVALID", "AUDIT_MATERIAL_MISSING_OR_INSUFFICIENT", "NON_CLAIM_MISSING_OR_FLIPPED", "PROHIBITED_AUDIT_TO_STANDING_REQUESTED", "PROHIBITED_SCOPE_DECLARATION_REQUESTED", "PROHIBITED_BASIS_GAP_CLOSURE_REQUESTED", "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED", "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED", "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED", "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "REQUESTED_RAW_MATERIAL_BODY_RETURN", "REQUESTED_RAW_MARKDOWN_BODY_RETURN", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_default_synthetic_complete_audit_satisfies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assert_satisfies(result)
            self.assertGreater(self.passed_count(result), 0)
            operation = self.operation(result)
            for key, value in (("operation_id", resolver.OPERATION_ID), ("operation_type", resolver.OPERATION_TYPE), ("operation_version", resolver.OPERATION_VERSION), ("operation_scope", resolver.OPERATION_SCOPE), ("upstream_receipt_operation_type", resolver.UPSTREAM_RECEIPT_OPERATION_TYPE), ("upstream_receipt_operation_outcome_required", resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED), ("upstream_receipt_status_required", resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED), ("audit_result", "SATISFIES_MISSING_BASIS_REQUIREMENTS")):
                self.assertEqual(operation[key], value)
            for key in ("audit_operation_recorded", "audit_performed", "audit_result_recorded", "declaration_accepted_as_basis", *resolver.AUDITED_FIELD_BY_CRITERION.values(), *resolver.SATISFIED_FIELD_BY_CRITERION.values()):
                self.assertIs(operation[key], True, key)
            self.assert_no_authorization(result)
            self.assert_operation_separate(result)
            self.assertEqual(set(result["audit_criteria"]), set(resolver.AUDIT_CRITERIA))
            self.assertEqual(result["audit_result_detail"]["missing_or_insufficient_audit_criteria"], [])
            self.assertIn("separately bounded successor closure", " ".join(result["permitted_future_route"]))
            self.assertIn("standing", " ".join(result["blocked_routes"]))
            self.assertIn("successor operation to close additional-basis gap, if audit satisfies missing basis and if separately bounded", result["what_remains_open"])
            for key in ("target_audit_operation_spec_markers_present", *[flag for *_, flag in resolver.UPSTREAM_REQUIREMENTS]):
                self.assertIs(operation[key], True, key)

    def test_default_live_target_satisfies_if_present(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_request()
        references = [request["operation_spec_reference"]] + [request[field] for field, *_ in resolver.UPSTREAM_REQUIREMENTS]
        if not all((REPO_ROOT / str(reference)).is_file() for reference in references):
            self.skipTest("default audit target files are unavailable")
        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
        self.assert_satisfies(result)
        operation = self.operation(result)
        self.assertIs(operation["audit_operation_recorded"], True)
        self.assertIs(operation["audit_performed"], True)
        self.assertIs(operation["declaration_accepted_as_basis"], True)
        for key in (*resolver.AUDITED_FIELD_BY_CRITERION.values(), *resolver.SATISFIED_FIELD_BY_CRITERION.values()):
            self.assertIs(operation[key], True, key)
        self.assert_no_authorization(result)

    def test_missing_criteria_require_additional_basis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for index, criterion in enumerate(resolver.AUDIT_CRITERIA):
                with self.subTest(criterion=criterion):
                    request, _ = self.make_request(Path(directory) / f"{index:02d}", bounded_audit_fields=self.deficient_audit_fields(criterion))
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
                    self.assert_requires_basis(result)
                    operation = self.operation(result)
                    self.assertIs(operation["audit_operation_recorded"], True)
                    self.assertIs(operation["audit_performed"], True)
                    self.assertIs(operation["audit_result_recorded"], True)
                    self.assertEqual(operation["audit_result"], "REQUIRES_ADDITIONAL_BASIS")
                    self.assertIs(operation["declaration_accepted_as_basis"], False)
                    self.assertIs(operation[resolver.SATISFIED_FIELD_BY_CRITERION[criterion]], False)
                    self.assertIn(criterion, result["audit_result_detail"]["missing_or_insufficient_audit_criteria"])
                    self.assert_no_authorization(result)

    def test_do_not_record_intent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory), intent=resolver.INTENT_DO_NOT_RECORD)
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(result["block"]["blocked"], False)
            operation = self.operation(result)
            for key in ("audit_operation_recorded", "audit_performed", "audit_result_recorded", "declaration_accepted_as_basis"):
                self.assertIs(operation[key], False, key)
            self.assert_no_authorization(result)
            self.assert_canonical_non_claims(result)

    def test_explicit_block_intent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory), intent=resolver.INTENT_BLOCK)
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assert_blocked(result)
            self.assertEqual(self.block_code(result), "EXPLICIT_BLOCK_REQUESTED")

    def test_request_shape_and_metadata_blocking(self) -> None:
        self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min([]))
        cases = (
            ("unsupported_intent", lambda request: request.__setitem__("intent", "unsupported")),
            ("missing_operation_id", lambda request: request.pop("operation_id")),
            ("wrong_operation_type", lambda request: request.__setitem__("operation_type", "wrong")),
            ("wrong_operation_version", lambda request: request.__setitem__("operation_version", "wrong")),
            ("wrong_operation_scope", lambda request: request.__setitem__("operation_scope", "wrong")),
            ("wrong_upstream_type", lambda request: request.__setitem__("upstream_receipt_operation_type", "wrong")),
            ("wrong_upstream_outcome", lambda request: request.__setitem__("upstream_receipt_operation_outcome_required", "wrong")),
            ("wrong_upstream_status", lambda request: request.__setitem__("upstream_receipt_status_required", "wrong")),
            ("wrong_route", lambda request: request.__setitem__("admissible_future_route", "wrong")),
            ("missing_spec", lambda request: request.pop("operation_spec_reference")),
            ("missing_receipt_summary", lambda request: request.pop("receipt_operation_terminal_summary_reference")),
            ("wrong_filename", lambda request: request.__setitem__("received_material_filename", "wrong")),
            ("wrong_version", lambda request: request.__setitem__("received_material_version", "wrong")),
            ("wrong_date", lambda request: request.__setitem__("received_material_date", "wrong")),
            ("wrong_author", lambda request: request.__setitem__("received_material_author", "wrong")),
            ("wrong_signature", lambda request: request.__setitem__("received_material_signature_role", "wrong")),
            ("wrong_predecessor", lambda request: request.__setitem__("received_material_predecessor", "wrong")),
            ("contribution_false", lambda request: request.__setitem__("contribution_map_present", False)),
            ("sibling_false", lambda request: request.__setitem__("sibling_non_monarchy_present", False)),
            ("sealing_false", lambda request: request.__setitem__("receipt_sealing_posture_present", False)),
            ("coupling_false", lambda request: request.__setitem__("coupling_not_assigned_present", False)),
            ("third_false", lambda request: request.__setitem__("no_third_model_present", False)),
            ("lineage_false", lambda request: request.__setitem__("lineage_constraints_present", False)),
            ("audit_only_false", lambda request: request.__setitem__("for_audit_only", False)),
        )
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            for name, mutate in cases:
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    mutate(malformed)
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))

    def test_marker_validation_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths = self.make_request(Path(directory))
            for field, path in paths.items():
                with self.subTest(field=field):
                    original = path.read_text(encoding="utf-8")
                    path.write_text("required marker class removed", encoding="utf-8")
                    try:
                        result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(copy.deepcopy(request))
                    finally:
                        path.write_text(original, encoding="utf-8")
                    self.assert_blocked(result)

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            for field in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(field=field):
                    malformed = copy.deepcopy(request)
                    malformed[field] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))

    def test_required_false_and_result_preclaim_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(required_false=key):
                    malformed = copy.deepcopy(request)
                    malformed[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(result_preclaim=key):
                    malformed = copy.deepcopy(request)
                    malformed[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))
            malformed = copy.deepcopy(request)
            malformed["audit_result"] = "SATISFIES_MISSING_BASIS_REQUIREMENTS"
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))

    def test_required_false_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(key=key):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"][key] = True
                    result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed)
                    self.assert_blocked(result)
                    self.assertIs(result["non_claims"][key], False)
            malformed_cases = (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            )
            for name, non_claims in malformed_cases:
                with self.subTest(name=name):
                    malformed = copy.deepcopy(request)
                    malformed["declared_non_claims"] = non_claims
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(malformed))

    def test_sanitizer_behavior(self) -> None:
        sentinels = (
            "RAW_MARKDOWN_BODY_MUST_NOT_RETURN",
            "RAW_MATERIAL_BODY_MUST_NOT_RETURN",
            "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
            "CURRENT_WORKING_TREE_MUST_NOT_RETURN",
        )
        with tempfile.TemporaryDirectory() as directory:
            request, paths = self.make_request(Path(directory))
            paths["operation_spec_reference"].write_text(paths["operation_spec_reference"].read_text(encoding="utf-8") + "\nRAW_MARKDOWN_BODY_MUST_NOT_RETURN\n", encoding="utf-8")
            request["bounded_audit_fields"]["raw_material_body"] = "RAW_MATERIAL_BODY_MUST_NOT_RETURN"
            request["bounded_audit_fields"]["hidden_repo_state"] = "HIDDEN_REPO_STATE_MUST_NOT_RETURN"
            request["bounded_audit_fields"]["current_working_tree"] = "CURRENT_WORKING_TREE_MUST_NOT_RETURN"
            satisfies = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assert_satisfies(satisfies)
            self.assert_no_raw_return(satisfies, sentinels)
            requires_request = copy.deepcopy(request)
            requires_request["bounded_audit_fields"]["candidate_a_mandate"] = ""
            requires = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(requires_request)
            self.assert_requires_basis(requires)
            self.assert_no_raw_return(requires, sentinels)
            blocked_request = copy.deepcopy(request)
            blocked_request["return_raw_material_body"] = True
            blocked = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(blocked_request)
            self.assert_blocked(blocked)
            self.assert_no_raw_return(blocked, sentinels)
            not_recorded_request = copy.deepcopy(request)
            not_recorded_request["intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(not_recorded_request)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_no_raw_return(not_recorded, sentinels)
            raw_markdown = copy.deepcopy(request)
            raw_markdown["return_raw_markdown_body"] = True
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(raw_markdown))

    def test_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request, _ = self.make_request(root / "inputs")
            request_path = root / self.safe_json_filename("valid request")
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path(request_path)
            self.assert_satisfies(result)
            missing = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path(root / "missing.json")
            self.assert_blocked(missing)
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path(malformed_path))
            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked(resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path(array_path))
            output = resolver.write_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_result(result, root / "output")
            second = resolver.write_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_result(result, root / "output")
            self.assertTrue(output.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(output, second)
            self.assertIsInstance(json.loads(output.read_text(encoding="utf-8")), dict)
            self.assertIn("authored_scope_division_declaration_audit_operation_v0_min_result", output.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min", str(resolver.OUTPUT_ROOT))
            forbidden_roots = ("receipt_operation", "receipt_boundary", "basis_emission", "distinctness", "differentiation", "runtime", "daemon", "public_api", "externalization")
            self.assertFalse(any(part in output.parts for part in forbidden_roots))

    def test_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, paths = self.make_request(Path(directory))
            request["bounded_audit_fields"]["raw_material_body"] = "RAW_MATERIAL_BODY_MUST_NOT_RETURN"
            before_request = copy.deepcopy(request)
            before_files = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assert_satisfies(result)
            self.assertEqual(request, before_request)
            self.assertEqual({key: path.read_text(encoding="utf-8") for key, path in paths.items()}, before_files)

    def test_summary_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            self.assert_satisfies(result)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(summary["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(summary["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(summary["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(summary["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertEqual(summary["audit_result"], "SATISFIES_MISSING_BASIS_REQUIREMENTS")
            self.assertIs(summary["declaration_accepted_as_basis"], True)
            self.assertEqual(summary["missing_or_insufficient_audit_criteria"], [])
            for key in (*resolver.AUDITED_FIELD_BY_CRITERION.values(), *resolver.SATISFIED_FIELD_BY_CRITERION.values()):
                self.assertIs(summary[key], True, key)
            self.assertTrue(summary["selected_target_spec_path"])
            self.assertTrue(summary["completed_receipt_operation_terminal_summary_path"])
            self.assertTrue(summary["completed_scope_division_operation_terminal_summary_path"])
            requires_request = copy.deepcopy(request)
            requires_request["bounded_audit_fields"] = self.deficient_audit_fields("lineage_constraints")
            requires = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(requires_request)
            requires_summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_summary(requires)
            self.assertEqual(requires_summary["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
            self.assertFalse(requires_summary["declaration_accepted_as_basis"])
            self.assertIn("lineage_constraints", requires_summary["missing_or_insufficient_audit_criteria"])

    def test_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            request, _ = self.make_request(Path(directory))
            result = resolver.resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)
            summary = resolver.build_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_summary(result)
            self.assert_satisfies(result)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["result_version"], "0.1.0")
            self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
            operation = self.operation(result)
            self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
            self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
            self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
            self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
            self.assertIs(operation["audit_operation_recorded"], True)
            self.assertIs(operation["audit_performed"], True)
            self.assertIs(operation["audit_result_recorded"], True)
            self.assertEqual(operation["audit_result"], "SATISFIES_MISSING_BASIS_REQUIREMENTS")
            self.assertIs(operation["declaration_accepted_as_basis"], True)
            for key in (*resolver.AUDITED_FIELD_BY_CRITERION.values(), *resolver.SATISFIED_FIELD_BY_CRITERION.values()):
                self.assertIs(operation[key], True, key)
            self.assert_no_authorization(result)
            self.assert_operation_separate(result)
            self.assert_canonical_non_claims(result)


if __name__ == "__main__":
    unittest.main()
