"""Bounded tests for the V2 eight-dimension candidate-evaluation operation.

The suite uses synthetic upstream sources only.  It never supplies a live
candidate basis, and it verifies that candidate and complete-basis bodies do
not escape through the resolver result or temporary written output.
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

import resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2 as resolver


class ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Tests(unittest.TestCase):
    """Verify one atomic, material-omitting operation surface."""

    CANDIDATE_SENTINEL = "SYNTHETIC_CANDIDATE_BODY_MUST_NOT_RETURN"
    BASIS_ITEM_SENTINEL = "SYNTHETIC_BASIS_ITEM_MUST_NOT_RETURN"
    BASIS_REFERENCE_SENTINEL = "SYNTHETIC_BASIS_REFERENCE_MUST_NOT_RETURN"

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in str(name))
        safe = safe.strip("._-") or "case"
        prefix = f"{index:03d}_" if index is not None else ""
        return f"{prefix}{safe}.json"

    def _write_markdown(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture path is a directory: {path}")
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_markdown(path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n")

    def _synthetic_operation_specification(self) -> str:
        markers: list[str] = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Operation V0 Minimum V2 Specification",
            "predecessor specification remains preserved lineage",
            "same constitutional operation identity",
            "no live evaluation",
            "candidate sufficiency is the immediate separate downstream question",
            "no direct attestation, receipt, or presence route",
            "complete eight-dimension basis before any evaluation",
            "partial evaluation may not stand",
            "incomplete bounded basis may produce REQUIRES_EVALUATION_BASIS",
            "all eight dimensions remain NOT_EVALUATED when the gate does not pass",
            "complete required support and no contradiction or unresolved posture -> SATISFIED",
            "recognized contradiction -> NOT_SATISFIED",
            "otherwise -> INDETERMINATE",
            "caller-supplied result labels are not accepted",
            "BLOCKED first",
            "REQUIRES_EVALUATION_BASIS second",
            "EVALUATION_INDETERMINATE when any dimension is INDETERMINATE",
            "EVALUATED when all eight complete and none is INDETERMINATE",
            "operation exhausts after one complete evaluation",
            "no rerun",
            "no later dimension completion",
            "no repeated permission",
            "no reusable route",
            "all dimensions satisfied is not candidate sufficiency",
            "any dimension not satisfied is not candidate insufficiency",
            "dimension-level indeterminacy is not candidate-level indeterminacy",
            "evaluation is not attestation",
            "evaluation is not answerable receipt",
            "evaluation is not presence",
            "contaminated lineage remains unchanged",
            "no retroactive validation",
            "no repair, scan, discovery, mutation, or validation enforcement",
        ]
        for marker_class in resolver.V2_SPEC_MARKER_CLASSES.values():
            markers.extend(marker_class)
        markers.extend(resolver.EVALUATION_DIMENSION_IDS)
        markers.extend(resolver.DIMENSION_RESULT_FAMILY)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_boundary_terminal_summary(self) -> str:
        markers = [
            "# Receiver-Side Answerable Basis Candidate Evaluation Boundary Terminal Summary V0",
            resolver.PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED,
            resolver.PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED,
            "candidate_structural_correspondence = NOT_EVALUATED",
        ]
        for marker_class in resolver.BOUNDARY_SUMMARY_MARKER_CLASSES.values():
            markers.extend(marker_class)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _synthetic_boundary_artifact(self) -> dict[str, object]:
        boundary = {
            "boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "boundary_type": resolver.PRIOR_EVALUATION_BOUNDARY_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_result": resolver.PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED,
            "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed": True,
            "selected_candidate_reception_result_referenced": True,
            "selected_candidate_material_referenced": True,
            "receiver_side_answerable_basis_candidate_evaluated": False,
            "receiver_side_answerable_basis_candidate_sufficient": False,
            "receiver_side_answerable_basis_candidate_insufficient": False,
            "receiver_side_answerable_basis_candidate_indeterminate": False,
            "receiver_attestation_created": False,
            "receiver_attestation_supported": False,
            "receiver_answerable_receipt_present": False,
            "receiver_answerable_basis_custody_distinct": False,
            "receiver_answerable_basis_refusable": False,
            "receiver_answerable_basis_could_have_been_withheld": False,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
            "second_candidate_received": False,
            "second_candidate_evaluated": False,
            "repeated_evaluation_permission_created": False,
            "reusable_route_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        }
        dimensions = {
            dimension_id: {
                "evaluation_status": resolver.DIMENSION_RESULT_NOT_EVALUATED,
                "established": False,
            }
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS
        }
        return {
            "outcome": resolver.PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "receiver_side_answerable_basis_candidate_evaluation_boundary": boundary,
            "receiver_side_answerable_basis_candidate_evaluation_dimensions": dimensions,
        }

    def _synthetic_candidate_payload(self) -> dict[str, object]:
        return {
            "candidate_body": self.CANDIDATE_SENTINEL,
            "nested": {"values": [1, {"opaque": [True, "packet"]}]},
        }

    def _synthetic_reception_artifact(self) -> dict[str, object]:
        operation = {
            "receiver_side_answerable_basis_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "candidate_material_supplied": True,
            "candidate_material_received": True,
            "candidate_material_recorded": True,
            "candidate_material_preserved": True,
            "receiver_side_answerable_basis_candidate_received": True,
            "receiver_side_answerable_basis_candidate_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluated": False,
        }
        return {
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED",
            "failed_check_count": 0,
            "receiver_side_answerable_basis_reception_operation": operation,
            "receiver_side_answerable_basis_reception_operation_material": {
                "supplied_candidate_material_record": {
                    "candidate_material": self._synthetic_candidate_payload(),
                    "candidate_material_supplied": True,
                    "candidate_material_received": True,
                    "candidate_material_recorded": True,
                    "candidate_material_preserved": True,
                }
            },
        }

    def _fixture_paths(self, root: Path) -> dict[str, Path]:
        spec = self._write_markdown(root / resolver.GOVERNING_V2_OPERATION_SPEC_RELATIVE_PATH, self._synthetic_operation_specification())
        summary = self._write_markdown(root / resolver.EVALUATION_BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH, self._synthetic_boundary_terminal_summary())
        boundary = self._write_json(root / resolver.SELECTED_EVALUATION_BOUNDARY_RESULT_RELATIVE_PATH, self._synthetic_boundary_artifact())
        reception = self._write_json(root / resolver.SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH, self._synthetic_reception_artifact())
        return {"spec": spec, "summary": summary, "boundary": boundary, "reception": reception}

    def _base_request(self) -> dict[str, object]:
        return resolver.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request()

    def _dimension_record(self, dimension_id: str) -> dict[str, object]:
        rule = resolver.DIMENSION_RULES[dimension_id]
        return {
            "dimension_id": dimension_id,
            "selected_candidate_id": resolver.CANDIDATE_ID,
            "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "basis_supplied": True,
            "basis_items": [{"opaque": self.BASIS_ITEM_SENTINEL}],
            "basis_references": [{"opaque": self.BASIS_REFERENCE_SENTINEL}],
            "explicit_support_postures": {key: True for key in rule["required_support_postures"]},
            "explicit_contradiction_postures": {key: False for key in rule["recognized_contradiction_postures"]},
            "unresolved_postures": {key: False for key in rule["recognized_unresolved_postures"]},
            "evaluator_reference": "synthetic-bounded-evaluator-reference",
            "basis_non_claims": {key: False for key in resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS},
        }

    def _complete_request(self) -> dict[str, object]:
        request = self._base_request()
        request["evaluation_basis_supplied"] = True
        request["dimension_basis_records"] = {
            dimension_id: self._dimension_record(dimension_id)
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS
        }
        return request

    def _one_not_satisfied_request(self, dimension_id: str) -> dict[str, object]:
        request = self._complete_request()
        rule = resolver.DIMENSION_RULES[dimension_id]
        request["dimension_basis_records"][dimension_id]["explicit_contradiction_postures"][
            rule["recognized_contradiction_postures"][0]
        ] = True
        return request

    def _one_indeterminate_request(self, dimension_id: str) -> dict[str, object]:
        request = self._complete_request()
        rule = resolver.DIMENSION_RULES[dimension_id]
        request["dimension_basis_records"][dimension_id]["unresolved_postures"][
            rule["recognized_unresolved_postures"][0]
        ] = True
        return request

    def _clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def _resolve_synthetic(self, root: Path, request: dict[str, object] | None = None) -> dict[str, object]:
        with patch.object(resolver, "REPO_ROOT", root):
            return resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2(
                self._base_request() if request is None else request
            )

    def _resolve_synthetic_from_path(self, root: Path, path: Path) -> dict[str, object]:
        with patch.object(resolver, "REPO_ROOT", root):
            return resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_from_path(path)

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        return (block.get("code") or block.get("block_code")) if isinstance(block, dict) else None

    def failed_check_count(self, result: dict[str, object]) -> int:
        return result["failed_check_count"]

    def passed_check_count(self, result: dict[str, object]) -> int:
        return result["passed_check_count"]

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        checks = result["receiver_side_answerable_basis_candidate_evaluation_operation_checks"]
        self.assertIsInstance(checks, list)
        for check in checks:
            if isinstance(check, dict):
                for code_key in ("block_code", "failure_code"):
                    if code_key in check:
                        self.assertIn(check[code_key], resolver.BLOCK_CODES)

    def assert_blocked_public(self, result: dict[str, object], expected: str | None = None) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected is not None:
            self.assertEqual(code, expected)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)
        self.assert_every_dimension_not_evaluated(result)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_dimension_basis_non_claims(self, record: dict[str, object]) -> None:
        non_claims = record["basis_non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)

    def assert_every_dimension_not_evaluated(self, result: dict[str, object]) -> None:
        dimensions = result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]
        self.assertEqual(tuple(dimensions), resolver.EVALUATION_DIMENSION_IDS)
        for dimension in dimensions.values():
            self.assertEqual(dimension["dimension_result"], resolver.DIMENSION_RESULT_NOT_EVALUATED)
            self.assertIs(dimension["dimension_evaluated"], False)
            self.assertIs(dimension["dimension_established"], False)
            self.assertIs(dimension["basis_referenced"], False)

    def assert_all_eight_evaluated(self, result: dict[str, object]) -> None:
        dimensions = result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]
        self.assertEqual(tuple(dimensions), resolver.EVALUATION_DIMENSION_IDS)
        for dimension in dimensions.values():
            self.assertIs(dimension["dimension_evaluated"], True)
            self.assertIs(dimension["basis_referenced"], True)
            self.assertEqual(dimension["missing_or_inconsistent_dimension_basis"], [])

    def _contains_forbidden_material_key(self, value: object) -> bool:
        if isinstance(value, dict):
            return any(
                key in {"candidate_material", "candidate_packet", "basis_items", "basis_references"}
                or self._contains_forbidden_material_key(nested)
                for key, nested in value.items()
            )
        if isinstance(value, list):
            return any(self._contains_forbidden_material_key(item) for item in value)
        return False

    def assert_complete_basis_omitted(self, result: dict[str, object]) -> None:
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in (self.CANDIDATE_SENTINEL, self.BASIS_ITEM_SENTINEL, self.BASIS_REFERENCE_SENTINEL):
            self.assertNotIn(sentinel, serialized)
        self.assertFalse(self._contains_forbidden_material_key(result))

    def assert_operation_wrapper_separation(self, result: dict[str, object]) -> None:
        operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
        for key in (
            "outcome",
            "block",
            "non_claims",
            "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
            "receiver_side_answerable_basis_candidate_evaluation_operation_summary",
            "receiver_side_answerable_basis_candidate_evaluation_operation_metadata",
            "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions",
        ):
            self.assertNotIn(key, operation)

    def assert_downstream_false(self, result: dict[str, object]) -> None:
        operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation[key], False, key)

    def test_public_api_constants_block_codes_and_flags(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_from_path",
            "write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result",
            "build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_summary",
            "build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request",
            "build_declared_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2")
        self.assertEqual(resolver.OPERATION_ID, "receiver_side_answerable_basis_candidate_evaluation_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "EVALUATE_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ACROSS_EIGHT_SEPARATE_DIMENSIONS_ONLY",
        )
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_THEN_CANDIDATE_SUFFICIENCY_BOUNDARY_ONLY",
        )
        self.assertEqual(resolver.CANDIDATE_ID, "receiver_side_answerable_basis_candidate_001")
        self.assertEqual(resolver.CANDIDATE_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE")
        self.assertEqual(resolver.CANDIDATE_SCOPE, "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY")
        self.assertEqual(resolver.SELECTED_RECEPTION_OPERATION_ID, "receiver_side_answerable_basis_reception_operation_001")
        self.assertEqual(resolver.SELECTED_EVALUATION_BOUNDARY_ID, "receiver_side_answerable_basis_candidate_evaluation_boundary_001")
        self.assertEqual(len(resolver.EVALUATION_DIMENSION_IDS), 8)
        self.assertEqual(resolver.DIMENSION_RESULT_FAMILY, ("SATISFIED", "NOT_SATISFIED", "INDETERMINATE", "NOT_EVALUATED"))
        self.assertIn(resolver.OUTCOME_REQUIRES_EVALUATION_BASIS, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OPERATION_RESULT_EVALUATED, resolver.OPERATION_RESULT_FAMILY)
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"))
        self.assertEqual(resolver.OUTPUT_FILENAME, "receiver_side_answerable_basis_candidate_evaluation_operation_001__receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json")
        for name in (
            "MAX_BASIS_ITEMS_PER_DIMENSION",
            "MAX_BASIS_REFERENCES_PER_DIMENSION",
            "MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE",
            "MAX_SERIALIZED_EVALUATION_REQUEST_SIZE",
        ):
            self.assertIsInstance(getattr(resolver, name), int)
            self.assertGreater(getattr(resolver, name), 0)
        self.assertIn("PROHIBITED_RECEIVER_ATTESTATION_REQUESTED", resolver.BLOCK_CODES)
        self.assertIn("PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED", resolver.BLOCK_CODES)
        required_codes = (
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "V2_OPERATION_SPEC_REFERENCE_MISSING",
            "V2_OPERATION_SPEC_MARKER_MISSING", "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", "EVALUATION_BOUNDARY_RESULT_REFERENCE_MISSING",
            "EVALUATION_BOUNDARY_RESULT_NOT_PARSEABLE", "EVALUATION_BOUNDARY_RESULT_NOT_MAPPING",
            "CANDIDATE_RECEPTION_RESULT_REFERENCE_MISSING", "CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE",
            "CANDIDATE_RECEPTION_RESULT_NOT_MAPPING", "REQUEST_VALUE_MISMATCH", "EVALUATION_BASIS_NOT_MAPPING",
            "EVALUATION_BASIS_OVERSIZED", "DIMENSION_BASIS_RECORD_MISSING", "DIMENSION_BASIS_RECORD_MALFORMED",
            "DIMENSION_BASIS_RECORD_OVERSIZED", "UNKNOWN_DIMENSION_BASIS_RECORD",
            "DIMENSION_BASIS_SELECTED_CANDIDATE_MISMATCH", "DIMENSION_BASIS_SELECTED_RECEPTION_OPERATION_MISMATCH",
            "DIMENSION_BASIS_SELECTED_BOUNDARY_MISMATCH", "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            "DIMENSION_RESULT_PRECLAIMED", "AGGREGATE_RESULT_PRECLAIMED", "PARTIAL_EVALUATION_REQUESTED",
            "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED", "RESULT_POSTURE_PRECLAIMED",
            "NON_CLAIM_MISSING_OR_FLIPPED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        )
        for code in required_codes:
            self.assertIn(code, resolver.BLOCK_CODES)
        self.assertNotEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_attestation_creation"],
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_answerable_receipt_creation"],
        )
        for field, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
            self.assertIn(code, resolver.BLOCK_CODES, field)
        for field in (
            "request_candidate_sufficiency",
            "request_candidate_insufficiency",
            "request_candidate_indeterminacy",
        ):
            self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS[field], "PROHIBITED_CANDIDATE_SUFFICIENCY_REQUESTED")

    def test_synthetic_and_live_default_waiting_results(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            result = self._resolve_synthetic(root)
            self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_EVALUATION_BASIS)
            operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
            self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], resolver.OPERATION_RESULT_REQUIRES_EVALUATION_BASIS)
            self.assertEqual(self.failed_check_count(result), 0)
            self.assertGreater(self.passed_check_count(result), 0)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluation_operation_recorded"], True)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded"], True)
            self.assertIs(operation["evaluation_basis_supplied"], False)
            self.assertIs(operation["evaluation_basis_complete"], False)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], False)
            self.assertIs(operation["candidate_evaluation_operation_exhausted"], False)
            self.assertTrue(result["missing_or_inconsistent_evaluation_basis"])
            self.assertIs(result["block"]["blocked"], False)
            self.assert_every_dimension_not_evaluated(result)
            self.assert_canonical_non_claims(result)
            self.assert_downstream_false(result)
            self.assert_complete_basis_omitted(result)
        required_paths = (
            resolver.GOVERNING_V2_OPERATION_SPEC_PATH,
            resolver.EVALUATION_BOUNDARY_TERMINAL_SUMMARY_PATH,
            resolver.SELECTED_EVALUATION_BOUNDARY_RESULT_PATH,
            resolver.SELECTED_CANDIDATE_RECEPTION_RESULT_PATH,
        )
        if not all(path.is_file() for path in required_paths):
            self.skipTest("selected repository upstream sources are unavailable")
        live = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2()
        self.assertEqual(live["outcome"], resolver.OUTCOME_REQUIRES_EVALUATION_BASIS)
        self.assertEqual(live["failed_check_count"], 0)
        self.assert_every_dimension_not_evaluated(live)
        self.assertIs(live["receiver_side_answerable_basis_candidate_evaluation_operation"]["receiver_side_answerable_basis_candidate_evaluated"], False)
        self.assertIs(live["receiver_side_answerable_basis_candidate_evaluation_operation"]["candidate_evaluation_operation_exhausted"], False)
        self.assert_canonical_non_claims(live)

    def test_atomic_gate_waits_for_missing_records_without_partial_evaluation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            cases = {
                "zero": {},
                "one_missing": {key: self._dimension_record(key) for key in resolver.EVALUATION_DIMENSION_IDS[:-1]},
                "seven": {key: self._dimension_record(key) for key in resolver.EVALUATION_DIMENSION_IDS[:7]},
            }
            for name, records in cases.items():
                with self.subTest(name=name):
                    request = self._base_request()
                    request["evaluation_basis_supplied"] = True
                    request["dimension_basis_records"] = records
                    result = self._resolve_synthetic(root, request)
                    self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_EVALUATION_BASIS)
                    self.assertEqual(result["failed_check_count"], 0)
                    self.assertTrue(result["missing_or_inconsistent_evaluation_basis"])
                    self.assert_every_dimension_not_evaluated(result)
                    operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], False)
                    self.assertIs(operation["candidate_evaluation_operation_exhausted"], False)

    def test_malformed_records_and_size_limits_block_before_evaluation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            first = resolver.EVALUATION_DIMENSION_IDS[0]
            cases: list[tuple[str, object, str | None]] = [
                ("not_mapping", [], "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("unknown_key", {**self._dimension_record(first), "unknown": True}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("key_mismatch", {**self._dimension_record(first), "dimension_id": "other"}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("candidate_mismatch", {**self._dimension_record(first), "selected_candidate_id": "other"}, "DIMENSION_BASIS_SELECTED_CANDIDATE_MISMATCH"),
                ("reception_mismatch", {**self._dimension_record(first), "selected_candidate_reception_operation_id": "other"}, "DIMENSION_BASIS_SELECTED_RECEPTION_OPERATION_MISMATCH"),
                ("boundary_mismatch", {**self._dimension_record(first), "selected_candidate_evaluation_boundary_id": "other"}, "DIMENSION_BASIS_SELECTED_BOUNDARY_MISMATCH"),
                ("items_not_list", {**self._dimension_record(first), "basis_items": "bad"}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("references_not_list", {**self._dimension_record(first), "basis_references": "bad"}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("support_not_mapping", {**self._dimension_record(first), "explicit_support_postures": []}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("contradiction_not_mapping", {**self._dimension_record(first), "explicit_contradiction_postures": []}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("unresolved_not_mapping", {**self._dimension_record(first), "unresolved_postures": []}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("empty_evaluator", {**self._dimension_record(first), "evaluator_reference": ""}, "DIMENSION_BASIS_RECORD_MALFORMED"),
                ("non_claims_missing", {**self._dimension_record(first), "basis_non_claims": {}}, "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED"),
            ]
            for name, altered, expected in cases:
                with self.subTest(name=name):
                    request = self._complete_request()
                    request["dimension_basis_records"][first] = altered
                    self.assert_blocked_public(self._resolve_synthetic(root, request), expected)
            request = self._complete_request()
            request["dimension_basis_records"]["unknown_dimension"] = self._dimension_record(first)
            self.assert_blocked_public(self._resolve_synthetic(root, request), "UNKNOWN_DIMENSION_BASIS_RECORD")
            request = self._complete_request()
            request["dimension_basis_records"][first]["basis_non_claims"][resolver.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS[0]] = True
            self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED")
            request = self._complete_request()
            request["dimension_basis_records"][first]["basis_items"] = list(range(resolver.MAX_BASIS_ITEMS_PER_DIMENSION + 1))
            self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_BASIS_RECORD_OVERSIZED")
            request = self._complete_request()
            request["dimension_basis_records"][first]["basis_references"] = list(range(resolver.MAX_BASIS_REFERENCES_PER_DIMENSION + 1))
            self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_BASIS_RECORD_OVERSIZED")
            request = self._complete_request()
            request["dimension_basis_records"][first]["basis_items"] = ["x" * resolver.MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE]
            self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_BASIS_RECORD_OVERSIZED")

    def test_boolean_enforcement_preclaims_and_free_form_opacity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            first = resolver.EVALUATION_DIMENSION_IDS[0]
            for field, key in (
                ("explicit_support_postures", resolver.DIMENSION_RULES[first]["required_support_postures"][0]),
                ("explicit_contradiction_postures", resolver.DIMENSION_RULES[first]["recognized_contradiction_postures"][0]),
                ("unresolved_postures", resolver.DIMENSION_RULES[first]["recognized_unresolved_postures"][0]),
            ):
                for invalid in (1, 0, None, "true", "false", [], {}):
                    with self.subTest(field=field, invalid=repr(invalid)):
                        request = self._complete_request()
                        request["dimension_basis_records"][first][field][key] = invalid
                        self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_BASIS_RECORD_MALFORMED")
            for key in ("dimension_result", "requested_dimension_result"):
                request = self._complete_request()
                request["dimension_basis_records"][first][key] = resolver.DIMENSION_RESULT_SATISFIED
                self.assert_blocked_public(self._resolve_synthetic(root, request), "DIMENSION_RESULT_PRECLAIMED")
            request = self._complete_request()
            request["dimension_basis_records"][first]["candidate_sufficiency_preclaimed"] = True
            self.assert_blocked_public(self._resolve_synthetic(root, request), "AGGREGATE_RESULT_PRECLAIMED")
            opaque_one = self._complete_request()
            opaque_two = self._complete_request()
            opaque_two["dimension_basis_records"][first]["basis_items"] = ["SATISFIED attestation custody presence authority standing"]
            opaque_two["dimension_basis_records"][first]["basis_references"] = [{"claim": "presence authority"}]
            first_result = self._resolve_synthetic(root, opaque_one)
            second_result = self._resolve_synthetic(root, opaque_two)
            self.assertEqual(
                first_result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][first]["dimension_result"],
                second_result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][first]["dimension_result"],
            )

    def test_completed_all_satisfied_and_not_satisfied_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            request = self._complete_request()
            original = self._clone(request)
            result = self._resolve_synthetic(root, request)
            self.assertEqual(request, original)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(result["failed_check_count"], 0)
            operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
            self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], resolver.OPERATION_RESULT_EVALUATED)
            self.assert_all_eight_evaluated(result)
            for dimension in result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"].values():
                self.assertEqual(dimension["dimension_result"], resolver.DIMENSION_RESULT_SATISFIED)
                self.assertIs(dimension["dimension_established"], True)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], True)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_all_dimensions_satisfied"], True)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_not_satisfied"], False)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_indeterminate"], False)
            self.assertIs(operation["candidate_evaluation_operation_exhausted"], True)
            self.assert_downstream_false(result)
            self.assert_canonical_non_claims(result)
            self.assert_complete_basis_omitted(result)
            self.assert_operation_wrapper_separation(result)
            basis = result["receiver_side_answerable_basis_candidate_evaluation_operation_basis"]
            self.assertEqual(tuple(basis), resolver.EVALUATION_DIMENSION_IDS)
            expected_basis_metadata = {
                "dimension_id", "selected_candidate_id", "selected_candidate_reception_operation_id",
                "selected_candidate_evaluation_boundary_id", "basis_supplied", "basis_item_count",
                "basis_reference_count", "evaluator_reference_supplied", "support_posture_key_names",
                "contradiction_posture_key_names", "unresolved_posture_key_names",
                "basis_non_claims_validated", "complete_supplied_basis_omitted_from_operation_result",
            }
            for entry in basis.values():
                self.assertEqual(set(entry), expected_basis_metadata)
                self.assertEqual(entry["basis_item_count"], 1)
                self.assertEqual(entry["basis_reference_count"], 1)
                self.assertIs(entry["basis_non_claims_validated"], True)
                self.assertIs(entry["complete_supplied_basis_omitted_from_operation_result"], True)
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS:
                with self.subTest(dimension_id=dimension_id):
                    not_satisfied = self._resolve_synthetic(root, self._one_not_satisfied_request(dimension_id))
                    operation = not_satisfied["receiver_side_answerable_basis_candidate_evaluation_operation"]
                    self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], resolver.OPERATION_RESULT_EVALUATED)
                    self.assert_all_eight_evaluated(not_satisfied)
                    selected = not_satisfied["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][dimension_id]
                    self.assertEqual(selected["dimension_result"], resolver.DIMENSION_RESULT_NOT_SATISFIED)
                    self.assertIs(selected["dimension_established"], False)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_not_satisfied"], True)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_all_dimensions_satisfied"], False)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_indeterminate"], False)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_insufficient"], False)
                    self.assertIs(operation["candidate_evaluation_operation_exhausted"], True)

    def test_indeterminate_precedence_and_dimension_object_shape(self) -> None:
        expected_shape = {
            "dimension_id", "dimension_label", "dimension_result", "dimension_evaluated",
            "dimension_established", "basis_referenced", "missing_or_inconsistent_dimension_basis",
            "non_conversion_statement",
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS:
                with self.subTest(dimension_id=dimension_id):
                    result = self._resolve_synthetic(root, self._one_indeterminate_request(dimension_id))
                    operation = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
                    self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], resolver.OPERATION_RESULT_INDETERMINATE)
                    self.assert_all_eight_evaluated(result)
                    self.assertEqual(result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][dimension_id]["dimension_result"], resolver.DIMENSION_RESULT_INDETERMINATE)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_indeterminate"], True)
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_indeterminate"], False)
                    self.assertIs(operation["candidate_evaluation_operation_exhausted"], True)
            mixed = self._one_not_satisfied_request(resolver.EVALUATION_DIMENSION_IDS[0])
            other = resolver.EVALUATION_DIMENSION_IDS[1]
            mixed["dimension_basis_records"][other]["unresolved_postures"][resolver.DIMENSION_RULES[other]["recognized_unresolved_postures"][0]] = True
            mixed_result = self._resolve_synthetic(root, mixed)
            self.assertEqual(
                mixed_result["receiver_side_answerable_basis_candidate_evaluation_operation"]["receiver_side_answerable_basis_candidate_evaluation_operation_result"],
                resolver.OPERATION_RESULT_INDETERMINATE,
            )
            dimensions = mixed_result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]
            self.assertEqual(len(dimensions), 8)
            for dimension in dimensions.values():
                self.assertEqual(set(dimension), expected_shape)
            self.assert_complete_basis_omitted(mixed_result)

    def test_prohibited_non_claim_result_preclaim_and_intent_controls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for field, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=field):
                    request = self._base_request()
                    request[field] = True
                    self.assert_blocked_public(self._resolve_synthetic(root, request), code)
            for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=field):
                    request = self._base_request()
                    request["declared_non_claims"][field] = True
                    self.assert_blocked_public(self._resolve_synthetic(root, request), "NON_CLAIM_MISSING_OR_FLIPPED")
            for field, value in (
                ("receiver_side_answerable_basis_candidate_evaluation_operation_recorded", True),
                ("receiver_side_answerable_basis_candidate_evaluation_operation_result", resolver.OPERATION_RESULT_NOT_EVALUATED),
                ("receiver_side_answerable_basis_candidate_evaluated", True),
                ("receiver_side_answerable_basis_candidate_all_dimensions_satisfied", True),
                ("candidate_evaluation_operation_exhausted", True),
                ("dimension_results", {"x": "SATISFIED"}),
                ("dimension_evaluated", True),
                ("dimension_established", True),
                ("receiver_attestation_created", True),
            ):
                with self.subTest(preclaim=field):
                    request = self._base_request()
                    request[field] = value
                    self.assert_blocked_public(self._resolve_synthetic(root, request))
            do_not_record = self._base_request()
            do_not_record["intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = self._resolve_synthetic(root, do_not_record)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_every_dimension_not_evaluated(not_recorded)
            explicit_block = self._base_request()
            explicit_block["intent"] = resolver.INTENT_BLOCK
            self.assert_blocked_public(self._resolve_synthetic(root, explicit_block), "EXPLICIT_BLOCK_REQUESTED")

    def test_upstream_validation_and_request_shape_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = self._fixture_paths(root)

            def fresh() -> dict[str, Path]:
                return self._fixture_paths(root)

            paths["spec"].unlink()
            self.assert_blocked_public(self._resolve_synthetic(root), "V2_OPERATION_SPEC_REFERENCE_MISSING")
            paths = fresh()
            paths["summary"].unlink()
            self.assert_blocked_public(self._resolve_synthetic(root), "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING")
            paths = fresh()
            self._write_markdown(paths["summary"], "broken")
            self.assert_blocked_public(self._resolve_synthetic(root), "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING")
            paths = fresh()
            self._write_json(paths["boundary"], [])
            self.assert_blocked_public(self._resolve_synthetic(root), "EVALUATION_BOUNDARY_RESULT_NOT_MAPPING")
            paths = fresh()
            malformed_boundary = self._synthetic_boundary_artifact()
            malformed_boundary["receiver_side_answerable_basis_candidate_evaluation_boundary"][
                "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"
            ] = False
            self._write_json(paths["boundary"], malformed_boundary)
            self.assert_blocked_public(self._resolve_synthetic(root), "REQUEST_VALUE_MISMATCH")
            paths = fresh()
            malformed_dimension = self._synthetic_boundary_artifact()
            malformed_dimension["receiver_side_answerable_basis_candidate_evaluation_dimensions"][
                resolver.EVALUATION_DIMENSION_IDS[0]
            ]["evaluation_status"] = resolver.DIMENSION_RESULT_SATISFIED
            self._write_json(paths["boundary"], malformed_dimension)
            self.assert_blocked_public(self._resolve_synthetic(root), "REQUEST_VALUE_MISMATCH")
            paths = fresh()
            self._write_json(paths["reception"], [])
            self.assert_blocked_public(self._resolve_synthetic(root), "CANDIDATE_RECEPTION_RESULT_NOT_MAPPING")
            paths = fresh()
            malformed_reception = self._synthetic_reception_artifact()
            malformed_reception["receiver_side_answerable_basis_reception_operation"]["candidate_material_preserved"] = False
            self._write_json(paths["reception"], malformed_reception)
            self.assert_blocked_public(self._resolve_synthetic(root), "REQUEST_VALUE_MISMATCH")
            self.assert_blocked_public(
                self._resolve_synthetic(root, {"intent": "unsupported"}),
                "UNSUPPORTED_INTENT",
            )
            wrong_operation = self._base_request()
            wrong_operation["operation_id"] = "other"
            self.assert_blocked_public(self._resolve_synthetic(root, wrong_operation), "REQUEST_VALUE_MISMATCH")
            alternate = self._base_request()
            alternate["alternate_candidate_id"] = "other"
            self.assert_blocked_public(self._resolve_synthetic(root, alternate), "SECOND_CANDIDATE_OR_EVALUATION_REQUESTED")
            self.assert_blocked_public(
                resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2([]),
                "REQUEST_NOT_MAPPING",
            )

    def test_declared_non_claim_forms_boolean_boundaries_and_total_size(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_paths(root)
            for value in ({}, None, 0, "false"):
                with self.subTest(non_claims=repr(value)):
                    request = self._base_request()
                    request["declared_non_claims"] = value
                    self.assert_blocked_public(self._resolve_synthetic(root, request), "NON_CLAIM_MISSING_OR_FLIPPED")
            request = self._base_request()
            request["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])
            self.assert_blocked_public(self._resolve_synthetic(root, request), "NON_CLAIM_MISSING_OR_FLIPPED")
            first = resolver.EVALUATION_DIMENSION_IDS[0]
            for value in (True, False):
                with self.subTest(basis_supplied=value):
                    request = self._complete_request()
                    request["dimension_basis_records"][first]["basis_supplied"] = value
                    result = self._resolve_synthetic(root, request)
                    if value is True:
                        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    else:
                        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_EVALUATION_BASIS)
                        self.assert_every_dimension_not_evaluated(result)
            for invalid in (1, 0, None, "true", []):
                with self.subTest(invalid_basis_supplied=repr(invalid)):
                    request = self._complete_request()
                    request["dimension_basis_records"][first]["basis_supplied"] = invalid
                    self.assertEqual(self._resolve_synthetic(root, request)["outcome"], resolver.OUTCOME_REQUIRES_EVALUATION_BASIS)
            request = self._complete_request()
            for dimension_id in resolver.EVALUATION_DIMENSION_IDS:
                request["dimension_basis_records"][dimension_id]["basis_items"] = list(
                    range(resolver.MAX_BASIS_ITEMS_PER_DIMENSION)
                )
            self.assertEqual(self._resolve_synthetic(root, request)["outcome"], resolver.OUTCOME_RECORDED)
            request = self._complete_request()
            with patch.object(resolver, "MAX_SERIALIZED_EVALUATION_REQUEST_SIZE", 64):
                self.assert_blocked_public(self._resolve_synthetic(root, request), "EVALUATION_BASIS_OVERSIZED")

    def test_upstream_request_path_summary_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = self._fixture_paths(root)
            request = self._complete_request()
            request_path = self._write_json(root / self.safe_json_filename("request"), request)
            result = self._resolve_synthetic_from_path(root, request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            summary = resolver.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_summary(result)
            for key in (
                "outcome", "failed_check_count", "passed_check_count", "result_version", "resolver_module",
                "operation_id", "operation_result", "governing_paths", "selected_boundary_identity",
                "selected_candidate_identity", "atomic_gate_postures", "dimension_results",
                "dimension_evaluated", "dimension_established", "candidate_aggregate_postures",
                "candidate_evaluation_operation_exhausted", "missing_evaluation_basis", "marker_validation",
            ):
                self.assertIn(key, summary)
            output_dir = root / "outputs"
            output = resolver.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result(
                result, output_dir / resolver.OUTPUT_FILENAME
            )
            self.assertEqual(output.name, resolver.OUTPUT_FILENAME)
            parsed = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(parsed["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(parsed["result_version"], resolver.RESULT_VERSION)
            self.assert_canonical_non_claims(parsed)
            self.assert_complete_basis_omitted(parsed)
            suffix = resolver.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result(
                result, output_dir / resolver.OUTPUT_FILENAME
            )
            self.assertEqual(suffix.name, output.stem + "_001" + output.suffix)
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error):
                resolver.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result(result, root / "spec" / "forbidden.json")
            malformed = self._clone(result)
            malformed["resolver_module"] = "wrong"
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV2Error):
                resolver.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result(malformed, output_dir / "wrong.json")
            broken_boundary = self._synthetic_boundary_artifact()
            broken_boundary["outcome"] = "wrong"
            self._write_json(paths["boundary"], broken_boundary)
            self.assert_blocked_public(self._resolve_synthetic(root), "REQUEST_VALUE_MISMATCH")
            self._write_markdown(paths["spec"], "broken")
            self.assert_blocked_public(self._resolve_synthetic(root), "V2_OPERATION_SPEC_MARKER_MISSING")
            self._write_markdown(paths["spec"], self._synthetic_operation_specification())
            self._write_markdown(paths["summary"], "broken")
            self.assert_blocked_public(self._resolve_synthetic(root), "EVALUATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING")
            malformed_path = self._write_markdown(root / "malformed-request.json", "{")
            self.assert_blocked_public(self._resolve_synthetic_from_path(root, malformed_path), "REQUEST_NOT_MAPPING")
            array_path = self._write_json(root / "array-request.json", [])
            self.assert_blocked_public(self._resolve_synthetic_from_path(root, array_path), "REQUEST_NOT_MAPPING")
            self.assert_blocked_public(self._resolve_synthetic_from_path(root, root / "missing-request.json"), "REQUEST_NOT_MAPPING")


if __name__ == "__main__":
    unittest.main()
