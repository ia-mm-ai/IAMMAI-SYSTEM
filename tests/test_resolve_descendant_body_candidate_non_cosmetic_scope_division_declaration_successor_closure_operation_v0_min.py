"""Bounded tests for the successor closure operation resolver.

Closure is limited to the prior additional-basis gap and remains separate from
scope declaration, standing, emission, distinctness, body creation, and all
downstream behavior.
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

import resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min as resolver


class SuccessorClosureOperationTests(unittest.TestCase):
    """Verify one bounded prior-gap closure operation result only."""

    OPERATION_KEY = "descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation"
    CHECKS_KEY = "successor_closure_operation_checks"
    SUMMARY_KEY = "successor_closure_operation_summary"
    WRAPPER_FIELDS = ("outcome", "block", CHECKS_KEY, "non_claims", SUMMARY_KEY, "successor_closure_operation_metadata")

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, root: Path, name: str, content: str) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def spec_text(self) -> str:
        return "\n".join((
            "# Descendant Body Candidate Non-Cosmetic Scope Division Declaration Successor Closure Operation V0 Minimum Specification",
            resolver.OPERATION_TYPE, resolver.OPERATION_ID, resolver.OPERATION_SCOPE,
            resolver.PRIOR_OPERATION_OUTCOME_REQUIRED, "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration", "failed_check_count = 0", "passed_check_count = 96",
            resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, resolver.TARGET_PRIMARY_MATERIAL_VERSION, resolver.TARGET_PRIMARY_MATERIAL_DATE, resolver.TARGET_PRIMARY_MATERIAL_AUTHOR, resolver.TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, resolver.TARGET_PREDECESSOR_MATERIAL_FILENAME, resolver.TARGET_PREDECESSOR_MATERIAL_ROLE,
            resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, resolver.UPSTREAM_AUDIT_RESULT_REQUIRED, "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false",
            resolver.UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "SHA-256", resolver.UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, resolver.UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED, "audit_result_changed = false",
            "Gap closure is not standing", "Gap closure is not standing basis", "Gap closure is not scope declaration", "Gap closure is not basis-bearing scope division declaration", "Gap closure is not candidate-specific basis emission", "Gap closure is not distinctness support", "Gap closure is not candidate standing", "Gap closure is not descendant-body creation", "Gap closure is not relation", "Gap closure is not runtime", "Gap closure is not currentness", "Gap closure is not authority", "Gap closure is not coupling", "Gap closure is not presence", "Gap closure is not identity", "Accepted basis remains non-standing",
            "Candidate A and Candidate B remain sibling non-standing candidate records", "Neither ranks above the other", "Regulation may not become sovereign over Motion", "Motion may not erase Regulation", "Coupling remains unassigned", "Coupling must not be treated as third candidate", "Coupling must not be treated as third model", "Coupling must not be created by successor closure", "No third candidate is admitted", "No third model is admitted",
            "V1 predecessor reference remains lineage only", "V2 receipt does not erase V1", "No orphaned state", "No silent reset", "No overwrite", "Contaminated lineage remains preserved",
            resolver.ADMISSIBLE_FUTURE_ROUTE, "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED", "Only after a future successor closure records PRIOR_ADDITIONAL_BASIS_GAP_CLOSED may a separately bounded candidate-specific distinctness basis emission successor be considered", "No later operation is authorized by this specification alone",
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
            "direct successor closure permission to closure completion", "direct gap closure to standing conversion", "direct gap closure to standing basis conversion", "direct gap closure to candidate A scope declaration", "direct gap closure to candidate B scope declaration", "direct gap closure to basis-bearing scope division declaration", "direct audit result to closure without digest/custody", "repository scan route",
            "This operation spec defines only a future successor closure operation shape", "Successor closure permission is not successor closure completion", "Open means not scheduled, not authorized, and not executed",
        ))

    def prior_text(self) -> str:
        return "\n".join((resolver.PRIOR_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 96", "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration"))

    def receipt_text(self) -> str:
        return "\n".join((resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED, resolver.TARGET_PRIMARY_MATERIAL_FILENAME, resolver.TARGET_PRIMARY_MATERIAL_VERSION, resolver.TARGET_PRIMARY_MATERIAL_DATE, resolver.TARGET_PRIMARY_MATERIAL_AUTHOR, resolver.TARGET_PRIMARY_MATERIAL_SIGNATURE_ROLE, resolver.TARGET_PREDECESSOR_MATERIAL_FILENAME, resolver.TARGET_PREDECESSOR_MATERIAL_ROLE))

    def audit_text(self) -> str:
        return "\n".join((resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 83", "audit_result = SATISFIES_MISSING_BASIS_REQUIREMENTS", "declaration_accepted_as_basis = true", "missing_or_insufficient_audit_criteria = []", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false"))

    def digest_text(self) -> str:
        return "\n".join((resolver.UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 88", "SHA-256", resolver.UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, resolver.UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED, "audit_result_changed = false", "declaration_admitted_as_standing_basis = false", "candidate_a_scope_declared = false", "candidate_b_scope_declared = false", "basis_bearing_scope_division_declared = false", "basis_gap_closed = false"))

    def marker_paths(self, root: Path) -> dict[str, Path]:
        return {
            "operation_spec_reference": self.write_markdown(root, "successor_spec.md", self.spec_text()),
            "prior_operation_terminal_summary_reference": self.write_markdown(root, "prior.md", self.prior_text()),
            "receipt_operation_terminal_summary_reference": self.write_markdown(root, "receipt.md", self.receipt_text()),
            "audit_operation_terminal_summary_reference": self.write_markdown(root, "audit.md", self.audit_text()),
            "digest_custody_operation_terminal_summary_reference": self.write_markdown(root, "digest.md", self.digest_text()),
            "existence_claim_evidence_check_terminal_summary_reference": self.write_markdown(root, "existence.md", "UNSUPPORTED\ndescendant_body_basis_candidate_a_created = true\ndescendant_body_basis_candidate_b_created = true\ndescendant_body_basis_derivation_event_recorded = true"),
            "distinctness_operation_terminal_summary_reference": self.write_markdown(root, "distinctness.md", "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT\nNOT_DISTINCT\ndistinctness_supported = false\ncandidate_record_count_compared = 2"),
            "basis_emission_operation_terminal_summary_reference": self.write_markdown(root, "emission.md", "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS\nREQUIRES_ADDITIONAL_BASIS\ncandidate_specific_content_emitted = false\nseparate_seal_material_emitted = false\nseparate_lineage_receipt_material_emitted = false\nseparate_digest_material_emitted = false"),
            "scope_division_declaration_boundary_terminal_summary_reference": self.write_markdown(root, "boundary.md", "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED\nRECORDED\nfuture_scope_declaration_operation_shape_allowed = true\ncandidate_a_scope_not_declared = true\ncandidate_b_scope_not_declared = true\nbasis_bearing_scope_division_not_declared = true\nscope_label_laundering_not_allowed = true"),
        }

    def valid_request(self, paths: dict[str, Path]) -> dict[str, object]:
        return resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_request(**{key: str(value) for key, value in paths.items()})

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get(self.CHECKS_KEY)
        self.assertIsInstance(value, list)
        return value

    def summary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(self.SUMMARY_KEY)
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def failed_count(self, result: dict[str, object]) -> int:
        return sum(check.get("passed") is False for check in self.checks(result))

    def assert_public_codes(self, result: dict[str, object]) -> None:
        for check in self.checks(result):
            for key in ("block_code", "failure_code"):
                if key in check:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        operation = self.operation(result)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
            self.assertIs(operation[key], False, key)

    def assert_closed(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_CLOSED)
        self.assertEqual(self.failed_count(result), 0)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(self.block_code(result))
        self.assert_non_claims_false(result)

    def assert_requires_upstream_basis(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_UPSTREAM_BASIS)
        self.assertIs(result["block"]["blocked"], False)
        self.assertTrue(result["closure_result_detail"]["missing_or_insufficient_upstream_basis"])
        self.assertIs(self.operation(result)["prior_additional_basis_gap_closed"], False)
        self.assert_non_claims_false(result)

    def assert_blocked(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertGreater(self.failed_count(result), 0)
        self.assertIn(self.block_code(result), resolver.BLOCK_CODES)
        self.assert_public_codes(result)
        self.assert_non_claims_false(result)

    def assert_operation_not_wrapper(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in self.WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def test_public_api_and_constants(self) -> None:
        for name in (
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min",
            "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_from_path",
            "write_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_result",
            "build_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_summary",
            "build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min")
        self.assertEqual(resolver.OPERATION_ID, "descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(resolver.OPERATION_SCOPE, "CLOSE_PRIOR_ADDITIONAL_BASIS_GAP_FROM_RECEIVED_AUDITED_DIGEST_SEALED_AUTHORED_DECLARATION_ONLY")
        self.assertEqual(resolver.PRIOR_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION")
        self.assertEqual(resolver.PRIOR_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED")
        self.assertEqual(resolver.UPSTREAM_RECEIPT_STATUS_REQUIRED, "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY")
        self.assertEqual(resolver.UPSTREAM_AUDIT_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION")
        self.assertEqual(resolver.UPSTREAM_AUDIT_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS")
        self.assertEqual(resolver.UPSTREAM_AUDIT_RESULT_REQUIRED, "SATISFIES_MISSING_BASIS_REQUIREMENTS")
        self.assertIs(resolver.UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED, True)
        self.assertEqual(resolver.UPSTREAM_DIGEST_CUSTODY_OPERATION_TYPE, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION")
        self.assertEqual(resolver.UPSTREAM_DIGEST_CUSTODY_OPERATION_OUTCOME_REQUIRED, "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_RECORDED")
        self.assertEqual(resolver.UPSTREAM_DIGEST_ALGORITHM_REQUIRED, "SHA-256")
        self.assertEqual(resolver.UPSTREAM_PRIMARY_MATERIAL_DIGEST_SHA256_REQUIRED, "1ca450ea9762f2b2782b7edf3a1a08df3f292abbbd3aec78aa2890384b720dd0")
        self.assertEqual(resolver.UPSTREAM_PRIMARY_MATERIAL_CUSTODY_POSTURE_REQUIRED, "LOCAL_OPERATOR_HELD_SIGNED_SOURCE_ARTIFACT")
        self.assertTrue(set((resolver.OUTCOME_CLOSED, resolver.OUTCOME_REQUIRES_UPSTREAM_BASIS, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED)).issubset(resolver.OUTCOME_FAMILY))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min"))
        for code in ("UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT", "PROHIBITED_GAP_CLOSURE_TO_STANDING_REQUESTED", "PROHIBITED_SCOPE_DECLARATION_REQUESTED", "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED", "WRITE_REFUSED"):
            self.assertIn(code, resolver.BLOCK_CODES)

    def test_synthetic_closed_result_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths = self.marker_paths(Path(directory))
            request = self.valid_request(paths)
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)
            self.assert_closed(result)
            self.assertEqual(result["result_version"], "0.1.0")
            self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
            operation = self.operation(result)
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                self.assertIs(operation[key], True, key)
            self.assertEqual(operation["successor_closure_result"], "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED")
            self.assert_operation_not_wrapper(result)
            summary = resolver.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_summary(result)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_CLOSED)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(summary["successor_closure_result"], "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED")
            self.assertEqual(summary["missing_or_insufficient_upstream_basis"], [])
            self.assertTrue(summary["prior_operation_terminal_summary_markers_present"])
            self.assertTrue(summary["digest_custody_operation_terminal_summary_markers_present"])

    def test_default_live_result_if_available(self) -> None:
        request = resolver.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_request()
        result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)
        if result["outcome"] == resolver.OUTCOME_REQUIRES_UPSTREAM_BASIS:
            self.skipTest("default upstream summaries are unavailable or insufficient")
        self.assert_closed(result)

    def test_missing_upstream_basis_requires_upstream_basis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            paths["digest_custody_operation_terminal_summary_reference"].write_text("missing digest basis", encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(self.valid_request(paths))
            self.assert_requires_upstream_basis(result)
            self.assertIn("digest_custody_operation_terminal_summary_markers_present", result["closure_result_detail"]["missing_or_insufficient_upstream_basis"])
            missing_reference = self.valid_request(paths)
            missing_reference["receipt_operation_terminal_summary_reference"] = str(root / "absent-receipt.md")
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(missing_reference)
            self.assert_requires_upstream_basis(result)
            self.assertIn("receipt_operation_terminal_summary_markers_present", result["closure_result_detail"]["missing_or_insufficient_upstream_basis"])

    def test_marker_classes_require_upstream_basis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            originals = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            for index, (field, path) in enumerate(paths.items()):
                with self.subTest(field=field):
                    path.write_text("missing marker class", encoding="utf-8")
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(self.valid_request(paths))
                    if field == "operation_spec_reference":
                        self.assert_blocked(result)
                    else:
                        self.assert_requires_upstream_basis(result)
                    self.assertTrue(self.safe_json_filename(field, index).endswith(".json"))
                    path.write_text(originals[field], encoding="utf-8")

    def test_prohibited_request_flags_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = self.valid_request(self.marker_paths(Path(directory)))
            for flag in resolver.PROHIBITED_REQUEST_FLAGS:
                with self.subTest(flag=flag):
                    request = copy.deepcopy(base)
                    request[flag] = True
                    result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)
                    self.assert_blocked(result)

    def test_non_claim_and_preclaim_failures_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = self.valid_request(self.marker_paths(Path(directory)))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request))
                with self.subTest(declared=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request))
            for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(preclaim=key):
                    request = copy.deepcopy(base)
                    request[key] = True
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request))
            malformed_cases = (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {key: "false" for key in resolver.REQUIRED_FALSE_NON_CLAIMS}),
            )
            for name, declared in malformed_cases:
                with self.subTest(declared_non_claims=name):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"] = declared
                    self.assert_blocked(resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request))

    def test_path_write_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = self.marker_paths(root)
            request = self.valid_request(paths)
            original_request = copy.deepcopy(request)
            original_markers = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            request_path = root / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_from_path(request_path)
            self.assert_closed(result)
            self.assertEqual(request, original_request)
            for key, path in paths.items():
                self.assertEqual(path.read_text(encoding="utf-8"), original_markers[key])
            first = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_result(result, root / "output")
            second = resolver.write_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_result(result, root / "output")
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertIn("successor_closure_operation_v0_min_result", first.name)
            self.assertIn("integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min", str(resolver.REPO_ROOT / resolver.OUTPUT_ROOT))
            written = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(written["outcome"], resolver.OUTCOME_CLOSED)
            self.assertTrue(written["descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation"]["prior_additional_basis_gap_closed"])
            for bad_path in (root / "missing.json", root / "malformed.json", root / "array.json"):
                if bad_path.name == "malformed.json":
                    bad_path.write_text("{", encoding="utf-8")
                elif bad_path.name == "array.json":
                    bad_path.write_text("[]", encoding="utf-8")
                self.assert_blocked(resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min_from_path(bad_path))

    def test_do_not_record_and_smoke_posture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths = self.marker_paths(Path(directory))
            request = self.valid_request(paths)
            result = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)
            self.assert_closed(result)
            operation = self.operation(result)
            self.assertIs(operation["declaration_admitted_as_standing_basis"], False)
            self.assertIs(operation["candidate_a_scope_declared"], False)
            self.assertIs(operation["candidate_b_scope_declared"], False)
            self.assertIs(operation["basis_bearing_scope_division_declared"], False)
            self.assertIs(operation["presence_established"], False)
            self.assertIs(operation["identity_created"], False)
            self.assertIs(operation["follow_on_authorized"], False)
            request["intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = resolver.resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_successor_closure_operation_v0_min(request)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(self.operation(not_recorded)["prior_additional_basis_gap_closed"], False)
            self.assert_non_claims_false(not_recorded)


if __name__ == "__main__":
    unittest.main()
