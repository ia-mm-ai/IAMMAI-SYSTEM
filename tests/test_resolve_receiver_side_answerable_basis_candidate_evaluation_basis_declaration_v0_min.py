"""Bounded tests for one structural evaluation-basis declaration resolver.

The suite supplies only temporary synthetic declaration fixtures.  It verifies
readiness for later supply, never calls the evaluation-operation resolver, and
asserts that declaration, basis, and candidate bodies remain omitted.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min as resolver

try:
    import resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2 as operation_v2
except ImportError:  # The declaration resolver itself remains the test target.
    operation_v2 = None


class ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinTests(unittest.TestCase):
    """Verify structural readiness without evaluation, admission, or derivation."""

    BASIS_ITEM_SENTINEL = "SYNTHETIC_DECLARATION_BASIS_ITEM_MUST_NOT_RETURN"
    BASIS_REFERENCE_SENTINEL = "SYNTHETIC_DECLARATION_BASIS_REFERENCE_MUST_NOT_RETURN"
    CANDIDATE_SENTINEL = "SYNTHETIC_DECLARATION_CANDIDATE_MUST_NOT_RETURN"
    STATEMENT_SENTINEL = "SYNTHETIC_DECLARATION_STATEMENT_MUST_NOT_RETURN"
    NON_MEANING_SENTINEL = "SYNTHETIC_DECLARATION_NON_MEANING_MUST_NOT_RETURN"

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        prefix = f"{index:03d}_" if index is not None else ""
        return f"{prefix}{safe}.json"

    def _clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def _write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"synthetic file path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_markdown(path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n")

    def _synthetic_governing_specification(self) -> str:
        markers = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Basis Declaration V0 Minimum Specification",
            resolver.SELECTED_EVALUATION_OPERATION_ID,
            resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            resolver.SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
            resolver.SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
            resolver.CANDIDATE_ID,
            resolver.CANDIDATE_TYPE,
            resolver.CANDIDATE_SCOPE,
            resolver.SELECTED_RECEPTION_OPERATION_ID,
            resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "ready for supply is not operation admission",
            "supply is not resolver acceptance",
            "no invocation or retry created",
            "separately prepared",
            "separately supplied is distinct from supplied to declaration resolver",
            "source-body authorship explicitly declared",
            "resolver-generated basis prohibited",
            "repository access is not basis",
            "candidate material is not basis",
            "preparer reference is not identity or authority",
            "evaluator reference is not authority or standing",
            "all eight records required",
            "partial declaration not complete",
            "ready for supply only after complete structural and non-claim validation",
            "support posture is not SATISFIED",
            "contradiction posture is not NOT_SATISFIED",
            "unresolved posture is not INDETERMINATE",
            "free-form text cannot choose result",
            "only existing operation resolver may derive results",
            "no retroactive validation",
            "no repair",
            "no scan",
            "no discovery",
            "no validation enforcement",
            "Eight-Dimension Declaration",
            "Required Non-Claims",
            "declaration_ready_means_operation_admitted = false",
        ]
        for marker_class in resolver.DECLARATION_SPEC_MARKER_CLASSES.values():
            markers.extend(marker_class)
        markers.extend(resolver.EVALUATION_DIMENSION_IDS)
        markers.extend(resolver.ALLOWED_DIMENSION_RECORD_KEYS)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_waiting_summary(self) -> str:
        markers = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Operation Terminal Summary V0",
            resolver.SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
            "operation_result = REQUIRES_EVALUATION_BASIS",
            "all eight dimensions",
            "NOT_EVALUATED",
        ]
        for marker_class in resolver.WAITING_SUMMARY_MARKER_CLASSES.values():
            markers.extend(marker_class)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_waiting_artifact(self) -> dict[str, object]:
        operation = {
            "receiver_side_answerable_basis_candidate_evaluation_operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_evaluation_operation_type": resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_operation_result": resolver.SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
            "receiver_side_answerable_basis_candidate_evaluation_operation_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded": True,
            "evaluation_basis_supplied": False,
            "evaluation_basis_complete": False,
            "receiver_side_answerable_basis_candidate_evaluated": False,
            "candidate_evaluation_operation_exhausted": False,
            "second_candidate_evaluated": False,
            "repeated_evaluation_permission_created": False,
            "reusable_route_created": False,
            "dimension_completion_route_created": False,
            "receiver_attestation_created": False,
            "receiver_answerable_receipt_present": False,
            "presence_supported": False,
            "follow_on_work_authorized": False,
        }
        dimensions = {
            dimension_id: {
                "dimension_result": "NOT_EVALUATED",
                "dimension_evaluated": False,
                "dimension_established": False,
            }
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS
        }
        return {
            "outcome": resolver.SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "receiver_side_answerable_basis_candidate_evaluation_operation": operation,
            "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions": dimensions,
            "upstream_basis": {
                "selected_candidate_identity": {
                    "candidate_id": resolver.CANDIDATE_ID,
                    "candidate_type": resolver.CANDIDATE_TYPE,
                    "candidate_scope": resolver.CANDIDATE_SCOPE,
                    "reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
                },
                "selected_boundary_identity": {"boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID},
            },
        }

    def _fixture_paths(self, root: Path) -> dict[str, Path]:
        specification = self._write_markdown(
            root / resolver.GOVERNING_DECLARATION_SPEC_RELATIVE_PATH,
            self._synthetic_governing_specification(),
        )
        summary = self._write_markdown(
            root / resolver.WAITING_OPERATION_TERMINAL_SUMMARY_RELATIVE_PATH,
            self._synthetic_waiting_summary(),
        )
        artifact = self._write_json(
            root / resolver.WAITING_OPERATION_RESULT_RELATIVE_PATH,
            self._synthetic_waiting_artifact(),
        )
        return {"specification": specification, "summary": summary, "artifact": artifact}

    def _declaration_non_claims(self) -> dict[str, bool]:
        return {key: False for key in resolver.DECLARATION_REQUIRED_FALSE_NON_CLAIMS}

    def _dimension_non_claims(self) -> dict[str, bool]:
        return {key: False for key in resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS}

    def _dimension_record(self, dimension_id: str) -> dict[str, object]:
        rule = resolver.DIMENSION_RULES[dimension_id]
        return {
            "dimension_id": dimension_id,
            "selected_candidate_id": resolver.CANDIDATE_ID,
            "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "basis_supplied": True,
            "basis_items": [{"opaque_item": self.BASIS_ITEM_SENTINEL, "candidate": self.CANDIDATE_SENTINEL}],
            "basis_references": [{"opaque_reference": self.BASIS_REFERENCE_SENTINEL}],
            "explicit_support_postures": {key: True for key in rule["support"]},
            "explicit_contradiction_postures": {key: False for key in rule["contradiction"]},
            "unresolved_postures": {key: False for key in rule["unresolved"]},
            "evaluator_reference": "synthetic-bounded-preparer-reference",
            "basis_non_claims": self._dimension_non_claims(),
        }

    def _complete_material(self, *, source_body_authored: bool = False) -> dict[str, object]:
        return {
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id": resolver.DECLARATION_ID,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type": resolver.DECLARATION_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version": resolver.DECLARATION_VERSION,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope": resolver.DECLARATION_SCOPE,
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "selected_candidate_evaluation_operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "selected_candidate_evaluation_operation_type": resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            "selected_candidate_evaluation_operation_waiting_result_required": resolver.SELECTED_EVALUATION_OPERATION_WAITING_RESULT_REQUIRED,
            "selected_candidate_evaluation_operation_waiting_outcome_required": resolver.SELECTED_EVALUATION_OPERATION_WAITING_OUTCOME_REQUIRED,
            "declaration_origin_reference": "synthetic-declaration-origin",
            "preparer_reference": "synthetic-preparer-reference",
            "preparer_role_declaration": "synthetic-preparer-role",
            "source_body_authored": source_body_authored,
            "preparation_timestamp": "2026-07-28T00:00:00Z",
            "dimension_basis_records": {
                dimension_id: self._dimension_record(dimension_id)
                for dimension_id in resolver.EVALUATION_DIMENSION_IDS
            },
            "declaration_non_claims": self._declaration_non_claims(),
            "declaration_statement": {"opaque_statement": self.STATEMENT_SENTINEL},
            "declaration_non_meaning": {"opaque_non_meaning": self.NON_MEANING_SENTINEL},
        }

    def _base_request(self, material: dict[str, object] | None = None) -> dict[str, object]:
        return resolver.build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request(
            declaration_material=material,
            declaration_material_supplied=material is not None,
        )

    def _resolve_synthetic(self, root: Path, request: dict[str, object] | None = None) -> dict[str, object]:
        self._fixture_paths(root)
        with patch.object(resolver, "REPO_ROOT", root):
            return resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min(request)

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def failed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("failed_check_count")
        self.assertIsInstance(value, int)
        return value

    def passed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("passed_check_count")
        self.assertIsInstance(value, int)
        return value

    def declaration(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration")
        self.assertIsInstance(value, dict)
        return value

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_blocked_public(self, result: dict[str, object], expected: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected is not None:
            self.assertEqual(code, expected)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_no_dimension_result(result)
        self.assert_no_operation_invocation(result)

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        checks = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, dict)
            for key in ("block_code", "failure_code"):
                if key in check:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def assert_declaration_non_claims(self, value: object) -> None:
        self.assertIsInstance(value, dict)
        for key in resolver.DECLARATION_REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, value)
            self.assertIs(value[key], False)

    def assert_dimension_non_claims(self, value: object) -> None:
        self.assertIsInstance(value, dict)
        for key in resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, value)
            self.assertIs(value[key], False)

    def assert_no_dimension_result(self, result: dict[str, object]) -> None:
        detail = result.get("declaration_result_detail")
        self.assertIsInstance(detail, dict)
        self.assertIs(detail.get("dimension_result_exists"), False)
        serialized = json.dumps(result, sort_keys=True, ensure_ascii=True)
        self.assertNotIn('"dimension_result"', serialized)
        self.assertNotIn('"dimension_results"', serialized)

    def assert_no_operation_invocation(self, result: dict[str, object]) -> None:
        detail = result.get("declaration_result_detail")
        self.assertIsInstance(detail, dict)
        self.assertIs(detail.get("operation_invocation_exists"), False)
        statement = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_statement")
        self.assertIsInstance(statement, dict)
        self.assertIs(statement.get("operation_not_invoked"), True)

    def assert_material_omitted(self, result: dict[str, object]) -> None:
        metadata = result.get("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material")
        self.assertIsInstance(metadata, dict)
        for key in (
            "complete_declaration_material_omitted_from_result",
            "complete_basis_items_omitted_from_result",
            "complete_basis_references_omitted_from_result",
            "candidate_material_omitted_from_result",
        ):
            self.assertIs(metadata.get(key), True)
        serialized = json.dumps(result, sort_keys=True, ensure_ascii=True)
        for sentinel in (
            self.BASIS_ITEM_SENTINEL,
            self.BASIS_REFERENCE_SENTINEL,
            self.CANDIDATE_SENTINEL,
            self.STATEMENT_SENTINEL,
            self.NON_MEANING_SENTINEL,
        ):
            self.assertNotIn(sentinel, serialized)
        self.assertNotIn('"basis_items"', serialized)
        self.assertNotIn('"basis_references"', serialized)
        self.assertNotIn('"candidate_material"', serialized)

    def assert_declaration_has_no_wrapper_fields(self, result: dict[str, object]) -> None:
        declaration = self.declaration(result)
        for key in (
            "outcome",
            "block",
            "non_claims",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_checks",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_summary",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_metadata",
        ):
            self.assertNotIn(key, declaration)

    def assert_standing_locks(self, result: dict[str, object]) -> None:
        declaration = self.declaration(result)
        for key in (
            "evaluation_basis_declaration_separately_supplied",
            "evaluation_basis_declaration_admitted_by_operation",
            "evaluation_basis_declaration_resolver_generated",
            "evaluation_basis_declaration_candidate_material_reused_as_basis",
            "evaluation_basis_declaration_repository_access_treated_as_basis",
        ):
            self.assertIs(declaration.get(key), False)
        self.assert_canonical_non_claims(result)
        self.assert_no_dimension_result(result)
        self.assert_no_operation_invocation(result)

    def test_public_api_constants_and_non_claim_contracts(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min",
        )
        self.assertEqual(resolver.DECLARATION_ID, "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001")
        self.assertEqual(resolver.DECLARATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.DECLARATION_SCOPE,
            "DECLARE_BOUNDED_EVALUATION_BASIS_FOR_ONE_SELECTED_CANDIDATE_ACROSS_EIGHT_DIMENSIONS_ONLY",
        )
        self.assertEqual(len(resolver.EVALUATION_DIMENSION_IDS), 8)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), {
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_REQUIRES_DECLARATION_MATERIAL,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        })
        self.assertEqual(set(resolver.DECLARATION_RESULT_FAMILY), {
            resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
            resolver.DECLARATION_RESULT_REQUIRES_DECLARATION_MATERIAL,
            resolver.DECLARATION_RESULT_NOT_EVALUATED,
        })
        self.assertEqual(set(resolver.SUPPORTED_INTENTS), {
            resolver.INTENT_RECORD,
            resolver.INTENT_DO_NOT_RECORD,
            resolver.INTENT_BLOCK,
        })
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min"))
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_001__"
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result.json",
        )
        for name in (
            "MAX_SERIALIZED_DECLARATION_SIZE",
            "MAX_BASIS_ITEMS_PER_DIMENSION",
            "MAX_BASIS_REFERENCES_PER_DIMENSION",
            "MAX_SERIALIZED_DIMENSION_RECORD_SIZE",
            "MAX_DECLARATION_STATEMENT_SIZE",
            "MAX_DECLARATION_NON_MEANING_SIZE",
            "MAX_ORIGIN_REFERENCE_LENGTH",
            "MAX_PREPARER_REFERENCE_LENGTH",
            "MAX_PREPARER_ROLE_LENGTH",
            "MAX_PREPARATION_TIMESTAMP_LENGTH",
            "MAX_EVALUATOR_REFERENCE_LENGTH",
        ):
            self.assertIsInstance(getattr(resolver, name), int)
            self.assertGreater(getattr(resolver, name), 0)
        self.assert_declaration_non_claims(self._declaration_non_claims())
        self.assert_dimension_non_claims(self._dimension_non_claims())
        self.assertTrue(set(resolver.PROHIBITED_REQUEST_FLAGS.values()).issubset(resolver.BLOCK_CODES))
        self.assertNotEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_candidate_evaluation"],
            resolver.PROHIBITED_REQUEST_FLAGS["request_candidate_sufficiency"],
        )
        self.assertNotEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_attestation_creation"],
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_answerable_receipt_creation"],
        )
        if operation_v2 is not None:
            self.assertTrue(
                set(operation_v2.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS).issubset(
                    resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS
                )
            )

    def test_default_synthetic_waiting_and_optional_live_waiting(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = self._resolve_synthetic(Path(temporary), self._base_request())
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_DECLARATION_MATERIAL)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        declaration = self.declaration(result)
        self.assertIs(declaration["receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded"], True)
        self.assertIs(declaration["declaration_material_supplied"], False)
        self.assertIs(declaration["declaration_material_received"], False)
        self.assertIs(declaration["declaration_material_recorded"], False)
        self.assertIs(declaration["evaluation_basis_declaration_complete"], False)
        self.assertIs(declaration["evaluation_basis_declaration_ready_for_supply"], False)
        self.assertEqual(declaration["dimension_record_count"], 0)
        self.assertTrue(result["missing_or_incomplete_declaration_material"])
        self.assert_standing_locks(result)
        self.assert_declaration_has_no_wrapper_fields(result)

        required_paths = (
            REPO_ROOT / resolver.GOVERNING_DECLARATION_SPEC_RELATIVE_PATH,
            REPO_ROOT / resolver.WAITING_OPERATION_TERMINAL_SUMMARY_RELATIVE_PATH,
            REPO_ROOT / resolver.WAITING_OPERATION_RESULT_RELATIVE_PATH,
        )
        if all(path.is_file() for path in required_paths):
            live_result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min()
            self.assertEqual(live_result["outcome"], resolver.OUTCOME_REQUIRES_DECLARATION_MATERIAL)
            self.assertEqual(self.failed_check_count(live_result), 0)
            self.assert_standing_locks(live_result)

    def test_complete_declaration_is_ready_for_supply_and_omits_material(self) -> None:
        material = self._complete_material(source_body_authored=False)
        original_material = self._clone(material)
        request = self._base_request(material)
        original_request = self._clone(request)
        with tempfile.TemporaryDirectory() as temporary:
            result = self._resolve_synthetic(Path(temporary), request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        declaration = self.declaration(result)
        self.assertEqual(
            declaration["receiver_side_answerable_basis_candidate_evaluation_basis_declaration_result"],
            resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
        )
        for key in (
            "declaration_material_supplied",
            "declaration_material_received",
            "declaration_material_recorded",
            "evaluation_basis_declaration_complete",
            "all_eight_dimension_records_present",
            "all_dimension_records_structurally_bounded",
            "all_dimension_records_reference_selected_candidate",
            "all_dimension_records_reference_selected_boundary",
            "all_dimension_records_reference_selected_operation",
            "all_dimension_records_non_result_preclaiming",
            "all_dimension_records_non_claims_false",
            "evaluation_basis_declaration_ready_for_supply",
            "evaluation_basis_declaration_separately_prepared",
        ):
            self.assertIs(declaration[key], True)
        self.assertEqual(declaration["dimension_record_count"], 8)
        self.assertEqual(declaration["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assert_standing_locks(result)
        self.assert_material_omitted(result)
        self.assert_declaration_has_no_wrapper_fields(result)
        self.assertEqual(material, original_material)
        self.assertEqual(request, original_request)
        summary = resolver.build_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_summary(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(summary["dimension_record_count"], 8)
        self.assertIs(summary["declaration_material_postures"]["evaluation_basis_declaration_separately_supplied"], False)
        self.assertIs(summary["declaration_material_postures"]["evaluation_basis_declaration_admitted_by_operation"], False)

    def test_source_body_authored_and_rule_inputs_remain_non_results(self) -> None:
        for source_body_authored in (False, True):
            with self.subTest(source_body_authored=source_body_authored):
                material = self._complete_material(source_body_authored=source_body_authored)
                first_dimension = resolver.EVALUATION_DIMENSION_IDS[0]
                record = material["dimension_basis_records"][first_dimension]
                rule = resolver.DIMENSION_RULES[first_dimension]
                record["explicit_support_postures"] = {key: True for key in rule["support"]}
                record["explicit_contradiction_postures"] = {key: True for key in rule["contradiction"]}
                record["unresolved_postures"] = {key: True for key in rule["unresolved"]}
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                self.assertIs(
                    result["receiver_side_answerable_basis_candidate_evaluation_basis_declaration_material"]
                    ["source_body_authored_declared_value"],
                    source_body_authored,
                )
                self.assert_standing_locks(result)
        invalid_values = (1, 0, None, "true", "false", [], {})
        for value in invalid_values:
            with self.subTest(invalid_source_body_authored=repr(value)):
                material = self._complete_material()
                material["source_body_authored"] = value
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, "DECLARATION_FIELD_MALFORMED")
        for posture_name in ("explicit_support_postures", "explicit_contradiction_postures", "unresolved_postures"):
            for value in (1, 0, None, "true", "false", [], {}):
                with self.subTest(posture=posture_name, value=repr(value)):
                    material = self._complete_material()
                    dimension_id = resolver.EVALUATION_DIMENSION_IDS[0]
                    mapping = material["dimension_basis_records"][dimension_id][posture_name]
                    key = next(iter(mapping))
                    mapping[key] = value
                    with tempfile.TemporaryDirectory() as temporary:
                        result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                    self.assert_blocked_public(result, "DIMENSION_RECORD_MALFORMED")

    def test_partial_material_and_declaration_field_absence_wait(self) -> None:
        variants: list[tuple[str, dict[str, object]]] = []
        zero = self._complete_material()
        zero["dimension_basis_records"] = {}
        variants.append(("zero_records", zero))
        one = self._complete_material()
        first = resolver.EVALUATION_DIMENSION_IDS[0]
        one["dimension_basis_records"] = {first: one["dimension_basis_records"][first]}
        variants.append(("one_record", one))
        seven = self._complete_material()
        seven["dimension_basis_records"].pop(resolver.EVALUATION_DIMENSION_IDS[-1])
        variants.append(("seven_records", seven))
        for dimension_id in resolver.EVALUATION_DIMENSION_IDS:
            missing_dimension = self._complete_material()
            missing_dimension["dimension_basis_records"].pop(dimension_id)
            variants.append((f"missing_{dimension_id}", missing_dimension))
        for field in (
            "declaration_origin_reference",
            "preparer_reference",
            "preparer_role_declaration",
            "source_body_authored",
            "preparation_timestamp",
            "declaration_non_claims",
            "declaration_statement",
            "declaration_non_meaning",
        ):
            material = self._complete_material()
            material.pop(field)
            variants.append((f"missing_{field}", material))
        for name, material in variants:
            with self.subTest(name=name):
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_DECLARATION_MATERIAL)
                self.assertEqual(self.failed_check_count(result), 0)
                self.assertIs(self.declaration(result)["evaluation_basis_declaration_ready_for_supply"], False)
                self.assertTrue(result["missing_or_incomplete_declaration_material"])
                self.assert_standing_locks(result)

    def test_malformed_unknown_identity_and_dimension_record_cases_block(self) -> None:
        material_cases: dict[str, tuple[callable, str | None]] = {
            "unknown": (lambda material: material.__setitem__("unrecognized_field", True), "DECLARATION_TOP_LEVEL_FIELD_UNKNOWN"),
            "result_preclaim": (lambda material: material.__setitem__("dimension_result", "SATISFIED"), "DECLARATION_RESULT_PRECLAIMED"),
            "aggregate_preclaim": (lambda material: material.__setitem__("candidate_sufficiency", True), "AGGREGATE_RESULT_PRECLAIMED"),
            "wrong_declaration_id": (lambda material: material.__setitem__("receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id", "wrong"), "DECLARATION_SELECTED_IDENTITY_MISMATCH"),
            "wrong_operation": (lambda material: material.__setitem__("selected_candidate_evaluation_operation_id", "wrong"), "DECLARATION_SELECTED_IDENTITY_MISMATCH"),
            "wrong_candidate": (lambda material: material.__setitem__("receiver_side_answerable_basis_candidate_id", "wrong"), "DECLARATION_SELECTED_IDENTITY_MISMATCH"),
            "wrong_boundary": (lambda material: material.__setitem__("selected_candidate_evaluation_boundary_id", "wrong"), "DECLARATION_SELECTED_IDENTITY_MISMATCH"),
            "malformed_statement": (lambda material: material.__setitem__("declaration_statement", []), "DECLARATION_FIELD_MALFORMED"),
            "malformed_non_claims": (lambda material: material.__setitem__("declaration_non_claims", None), "DECLARATION_NON_CLAIM_MISSING_OR_FLIPPED"),
        }
        dimension_id = resolver.EVALUATION_DIMENSION_IDS[0]
        dimension_cases: dict[str, tuple[callable, str]] = {
            "record_not_mapping": (lambda material: material["dimension_basis_records"].__setitem__(dimension_id, []), "DIMENSION_RECORD_MALFORMED"),
            "unknown_key": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("unknown", True), "DIMENSION_RECORD_UNKNOWN"),
            "wrong_dimension_id": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("dimension_id", "wrong"), "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH"),
            "wrong_record_candidate": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("selected_candidate_id", "wrong"), "DIMENSION_RECORD_SELECTED_IDENTITY_MISMATCH"),
            "basis_not_supplied": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("basis_supplied", False), "DIMENSION_RECORD_MALFORMED"),
            "items_not_list": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("basis_items", {}), "DIMENSION_RECORD_MALFORMED"),
            "references_not_list": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("basis_references", {}), "DIMENSION_RECORD_MALFORMED"),
            "empty_evaluator": (lambda material: material["dimension_basis_records"][dimension_id].__setitem__("evaluator_reference", ""), "DIMENSION_RECORD_MALFORMED"),
            "basis_nonclaim_true": (lambda material: material["dimension_basis_records"][dimension_id]["basis_non_claims"].__setitem__(resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS[0], True), "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED"),
        }
        for name, (mutate, expected) in material_cases.items():
            with self.subTest(material_case=name):
                material = self._complete_material()
                mutate(material)
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, expected)
        for name, (mutate, expected) in dimension_cases.items():
            with self.subTest(dimension_case=name):
                material = self._complete_material()
                mutate(material)
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, expected)

        identity_fields = (
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_id",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_type",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_version",
            "receiver_side_answerable_basis_candidate_evaluation_basis_declaration_scope",
            "selected_candidate_evaluation_operation_id",
            "selected_candidate_evaluation_operation_type",
            "selected_candidate_evaluation_operation_waiting_result_required",
            "selected_candidate_evaluation_operation_waiting_outcome_required",
            "receiver_side_answerable_basis_candidate_id",
            "receiver_side_answerable_basis_candidate_type",
            "receiver_side_answerable_basis_candidate_scope",
            "selected_candidate_reception_operation_id",
            "selected_candidate_evaluation_boundary_id",
        )
        for field in identity_fields:
            with self.subTest(identity_field=field):
                material = self._complete_material()
                material[field] = "wrong-selected-identity"
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, "DECLARATION_SELECTED_IDENTITY_MISMATCH")

    def test_declaration_and_dimension_non_claims_exact_false(self) -> None:
        for key in resolver.DECLARATION_REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(declaration_non_claim=key):
                material = self._complete_material()
                material["declaration_non_claims"][key] = True
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, "DECLARATION_NON_CLAIM_MISSING_OR_FLIPPED")
        for key in resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(dimension_non_claim=key):
                material = self._complete_material()
                material["dimension_basis_records"][resolver.EVALUATION_DIMENSION_IDS[0]]["basis_non_claims"][key] = True
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED")
        for malformed in (None, {}, {resolver.DECLARATION_REQUIRED_FALSE_NON_CLAIMS[0]: False}):
            with self.subTest(declared_non_claims=repr(malformed)):
                request = self._base_request()
                request["declared_non_claims"] = malformed
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), request)
                self.assert_blocked_public(result, "NON_CLAIM_MISSING_OR_FLIPPED")
        for key in resolver.DECLARATION_REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(declared_non_claim=key):
                request = self._base_request()
                request["declared_non_claims"][key] = True
                with tempfile.TemporaryDirectory() as temporary:
                    result = self._resolve_synthetic(Path(temporary), request)
                self.assert_blocked_public(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_request_intents_prohibited_flags_and_preclaims_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            base = self._base_request(self._complete_material())
            not_recorded = self._resolve_synthetic(root / "not_recorded", dict(base, intent=resolver.INTENT_DO_NOT_RECORD))
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(self.declaration(not_recorded)["receiver_side_answerable_basis_candidate_evaluation_basis_declaration_recorded"], False)
            self.assert_standing_locks(not_recorded)
            explicit = self._resolve_synthetic(root / "explicit", dict(base, intent=resolver.INTENT_BLOCK))
            self.assert_blocked_public(explicit, "EXPLICIT_BLOCK_REQUESTED")
            malformed_requests = (
                ("not_mapping", []),
                ("unsupported", dict(base, intent="UNSUPPORTED")),
                ("wrong_request_identity", dict(base, receiver_side_answerable_basis_candidate_id="wrong")),
                ("material_when_unsupplied", dict(base, declaration_material_supplied=False)),
            )
            for index, (name, request) in enumerate(malformed_requests):
                with self.subTest(request=name):
                    result = self._resolve_synthetic(root / self.safe_json_filename(name, index), request)
                    self.assert_blocked_public(result)
            for flag, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(prohibited=flag):
                    request = self._clone(base)
                    request[flag] = True
                    result = self._resolve_synthetic(root / f"prohibited_{flag}", request)
                    self.assert_blocked_public(result, code)
            for key in resolver.RESULT_PRECLAIM_FIELDS | resolver.AGGREGATE_PRECLAIM_FIELDS:
                with self.subTest(preclaim=key):
                    request = self._clone(base)
                    request[key] = True
                    result = self._resolve_synthetic(root / f"preclaim_{key}", request)
                    expected = "AGGREGATE_RESULT_PRECLAIMED" if key in resolver.AGGREGATE_PRECLAIM_FIELDS else "RESULT_POSTURE_PRECLAIMED"
                    self.assert_blocked_public(result, expected)

    def test_upstream_validation_and_size_limits_block(self) -> None:
        upstream_cases: dict[str, tuple[str, callable, str]] = {
            "missing_spec": ("specification", lambda value: None, "DECLARATION_SPEC_REFERENCE_MISSING"),
            "broken_spec_marker": ("specification", lambda value: "broken", "DECLARATION_SPEC_MARKER_MISSING"),
            "missing_summary": ("summary", lambda value: None, "WAITING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING"),
            "broken_summary_marker": ("summary", lambda value: "broken", "WAITING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING"),
            "missing_artifact": ("artifact", lambda value: None, "WAITING_OPERATION_RESULT_REFERENCE_MISSING"),
            "malformed_artifact": ("artifact", lambda value: "{", "WAITING_OPERATION_RESULT_NOT_PARSEABLE"),
            "array_artifact": ("artifact", lambda value: [], "WAITING_OPERATION_RESULT_NOT_MAPPING"),
            "wrong_waiting_outcome": ("artifact", lambda value: self._alter_artifact(value, "outcome", "wrong"), "REQUEST_VALUE_MISMATCH"),
            "basis_already_supplied": ("artifact", lambda value: self._alter_operation(value, "evaluation_basis_supplied", True), "REQUEST_VALUE_MISMATCH"),
            "dimension_evaluated": ("artifact", lambda value: self._alter_dimension(value, "dimension_result", "SATISFIED"), "REQUEST_VALUE_MISMATCH"),
        }
        for index, (name, (part, mutate, expected)) in enumerate(upstream_cases.items()):
            with self.subTest(upstream=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                paths = self._fixture_paths(root)
                target = paths[part]
                altered = mutate(target.read_text(encoding="utf-8") if part != "artifact" else json.loads(target.read_text(encoding="utf-8")))
                if altered is None:
                    target.unlink()
                elif part == "artifact":
                    if isinstance(altered, str):
                        self._write_markdown(target, altered)
                    else:
                        self._write_json(target, altered)
                else:
                    self._write_markdown(target, altered)
                with patch.object(resolver, "REPO_ROOT", root):
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min(self._base_request())
                self.assert_blocked_public(result, expected)
        oversized_material = self._complete_material()
        oversized_material["declaration_statement"] = {"text": "x" * resolver.MAX_SERIALIZED_DECLARATION_SIZE}
        oversized_record = self._complete_material()
        oversized_record["dimension_basis_records"][resolver.EVALUATION_DIMENSION_IDS[0]]["basis_items"] = [
            {"text": "x" * resolver.MAX_SERIALIZED_DIMENSION_RECORD_SIZE}
        ]
        too_many_items = self._complete_material()
        too_many_items["dimension_basis_records"][resolver.EVALUATION_DIMENSION_IDS[0]]["basis_items"] = [
            {} for _ in range(resolver.MAX_BASIS_ITEMS_PER_DIMENSION + 1)
        ]
        too_many_references = self._complete_material()
        too_many_references["dimension_basis_records"][resolver.EVALUATION_DIMENSION_IDS[0]]["basis_references"] = [
            {} for _ in range(resolver.MAX_BASIS_REFERENCES_PER_DIMENSION + 1)
        ]
        oversized_statement = self._complete_material()
        oversized_statement["declaration_statement"] = {"text": "x" * resolver.MAX_DECLARATION_STATEMENT_SIZE}
        oversized_non_meaning = self._complete_material()
        oversized_non_meaning["declaration_non_meaning"] = {"text": "x" * resolver.MAX_DECLARATION_NON_MEANING_SIZE}
        oversized_origin = self._complete_material()
        oversized_origin["declaration_origin_reference"] = "x" * (resolver.MAX_ORIGIN_REFERENCE_LENGTH + 1)
        oversized_preparer = self._complete_material()
        oversized_preparer["preparer_reference"] = "x" * (resolver.MAX_PREPARER_REFERENCE_LENGTH + 1)
        oversized_role = self._complete_material()
        oversized_role["preparer_role_declaration"] = "x" * (resolver.MAX_PREPARER_ROLE_LENGTH + 1)
        oversized_timestamp = self._complete_material()
        oversized_timestamp["preparation_timestamp"] = "x" * (resolver.MAX_PREPARATION_TIMESTAMP_LENGTH + 1)
        oversized_evaluator = self._complete_material()
        oversized_evaluator["dimension_basis_records"][resolver.EVALUATION_DIMENSION_IDS[0]]["evaluator_reference"] = "x" * (resolver.MAX_EVALUATOR_REFERENCE_LENGTH + 1)
        for name, material, expected in (
            ("oversized_material", oversized_material, "DECLARATION_MATERIAL_OVERSIZED"),
            ("oversized_record", oversized_record, "DIMENSION_RECORD_OVERSIZED"),
            ("too_many_items", too_many_items, "DIMENSION_RECORD_MALFORMED"),
            ("too_many_references", too_many_references, "DIMENSION_RECORD_MALFORMED"),
            ("oversized_statement", oversized_statement, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_non_meaning", oversized_non_meaning, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_origin", oversized_origin, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_preparer", oversized_preparer, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_role", oversized_role, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_timestamp", oversized_timestamp, "DECLARATION_FIELD_MALFORMED"),
            ("oversized_evaluator", oversized_evaluator, "DIMENSION_RECORD_MALFORMED"),
        ):
            with self.subTest(limit=name), tempfile.TemporaryDirectory() as temporary:
                result = self._resolve_synthetic(Path(temporary), self._base_request(material))
                self.assert_blocked_public(result, expected)

    def _alter_artifact(self, artifact: object, key: str, value: object) -> object:
        self.assertIsInstance(artifact, dict)
        artifact[key] = value
        return artifact

    def _alter_operation(self, artifact: object, key: str, value: object) -> object:
        self.assertIsInstance(artifact, dict)
        operation = artifact["receiver_side_answerable_basis_candidate_evaluation_operation"]
        self.assertIsInstance(operation, dict)
        operation[key] = value
        return artifact

    def _alter_dimension(self, artifact: object, key: str, value: object) -> object:
        self.assertIsInstance(artifact, dict)
        dimensions = artifact["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]
        self.assertIsInstance(dimensions, dict)
        dimensions[resolver.EVALUATION_DIMENSION_IDS[0]][key] = value
        return artifact

    def test_from_path_write_and_non_mutation(self) -> None:
        material = self._complete_material(source_body_authored=True)
        request = self._base_request(material)
        before_request = self._clone(request)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            request_path = self._write_json(root / "requests" / "complete.json", request)
            with patch.object(resolver, "REPO_ROOT", root):
                result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assert_material_omitted(result)
            self.assertEqual(request, before_request)
            with patch.object(resolver, "REPO_ROOT", root):
                missing = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path(root / "missing.json")
                malformed_path = self._write_markdown(root / "malformed.json", "{")
                malformed = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path(malformed_path)
                array_path = self._write_json(root / "array.json", [])
                array = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_from_path(array_path)
            for path_result in (missing, malformed, array):
                self.assert_blocked_public(path_result, "REQUEST_NOT_MAPPING")

            target = root / "written" / "declaration_result.json"
            first = resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result(result, target)
            second = resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result(result, target)
            self.assertEqual(first, target)
            self.assertEqual(second, target.with_name("declaration_result_001.json"))
            self.assertTrue(first.is_file())
            parsed = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(parsed["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(parsed["result_version"], resolver.RESULT_VERSION)
            self.assert_canonical_non_claims(parsed)
            self.assert_material_omitted(parsed)
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result(result, root / "tests" / "forbidden.json")
            malformed_result = self._clone(result)
            malformed_result["resolver_module"] = "wrong"
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBasisDeclarationV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_evaluation_basis_declaration_v0_min_result(malformed_result, root / "written" / "wrong.json")


if __name__ == "__main__":
    unittest.main()
