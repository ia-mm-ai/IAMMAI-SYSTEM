"""Focused V3 tests for branch-relative candidate-evaluation open state.

V2 remains the preserved evaluation implementation.  These tests prove V3
changes only the result-relative ``what_remains_open`` posture.
"""

from __future__ import annotations

import copy
import hashlib
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

import resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2 as v2
import resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3 as v3


COMPLETE_REQUEST_PATH = (
    REPO_ROOT
    / "artifacts/source_body_supplied_receiver_side_answerable_basis_candidate_evaluation_operation_001"
    / "receiver_side_answerable_basis_candidate_evaluation_operation_001__resolver_request.json"
)
V2_WAITING_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"
    / "receiver_side_answerable_basis_candidate_evaluation_operation_001__receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json"
)
V2_COMPLETE_ARTIFACT_PATH = V2_WAITING_ARTIFACT_PATH.with_name(
    V2_WAITING_ARTIFACT_PATH.stem + "_001" + V2_WAITING_ARTIFACT_PATH.suffix
)


class ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Tests(unittest.TestCase):
    """Verify V3 preserves V2 evaluation semantics and closes stale open items."""

    V2_SYNCED_GLOBALS = (
        "REPO_ROOT",
        "RESULT_VERSION",
        "RESOLVER_MODULE",
        "MAX_BASIS_ITEMS_PER_DIMENSION",
        "MAX_BASIS_REFERENCES_PER_DIMENSION",
        "MAX_SERIALIZED_DIMENSION_BASIS_RECORD_SIZE",
        "MAX_SERIALIZED_EVALUATION_REQUEST_SIZE",
    )
    WAITING_OPEN = (
        "separately supplied eight-dimension evaluation basis",
        "actual candidate evaluation",
        "dimension-specific derived results",
        "candidate-sufficiency boundary, if separately selected after completed evaluation",
        "receiver-attestation boundary, only after later lawful basis",
        "receiver-answerable-receipt boundary, only after later lawful basis",
        "presence re-evaluation, only after later lawful basis",
        "identity",
        "relation",
        "coupling",
        "FIELD machinery",
        "runtime",
        "API",
        "authority",
        "standing",
        "output",
        "action",
        "synchronization",
        "follow-on work",
    )
    COMPLETED_OPEN = (
        "candidate-sufficiency boundary, if separately selected",
        "receiver-attestation boundary, only after later lawful basis",
        "receiver-answerable-receipt boundary, only after later lawful basis",
        "presence re-evaluation, only after later lawful basis",
        "identity",
        "relation",
        "coupling",
        "FIELD machinery",
        "runtime",
        "API",
        "authority",
        "standing",
        "output",
        "action",
        "synchronization",
        "follow-on work",
    )
    COMPLETED_WORK = (
        "separately supplied eight-dimension evaluation basis",
        "actual candidate evaluation",
        "dimension-specific derived results",
        "evaluation-basis completion",
        "operation admission",
        "operation exhaustion",
        "later dimension completion",
        "automatic re-evaluation",
        "same-candidate retry",
    )

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = (
            REPO_ROOT / "src/resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2.py",
            V2_WAITING_ARTIFACT_PATH,
            V2_COMPLETE_ARTIFACT_PATH,
            COMPLETE_REQUEST_PATH,
        )
        cls._preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in cls._preserved_paths
        }

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls._preserved_hashes.items():
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                raise AssertionError(f"preserved input changed: {path}")

    def clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result["receiver_side_answerable_basis_candidate_evaluation_operation"]
        self.assertIsInstance(value, dict)
        return value

    def failed_check_count(self, result: dict[str, object]) -> int:
        return result["failed_check_count"]

    def open_items(self, result: dict[str, object]) -> list[str]:
        value = result["what_remains_open"]
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, str) for item in value))
        return value

    def dimension_results(self, result: dict[str, object]) -> dict[str, str]:
        dimensions = result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]
        self.assertIsInstance(dimensions, dict)
        return {key: value["dimension_result"] for key, value in dimensions.items()}

    def load_complete_request(self) -> dict[str, object]:
        return json.loads(COMPLETE_REQUEST_PATH.read_text(encoding="utf-8"))

    def safe_output_path(self, root: Path, name: str) -> Path:
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in name)
        return root / (safe.strip("._-") or "result") / v3.OUTPUT_FILENAME

    def _write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir())
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")

    def _synthetic_boundary_artifact(self) -> dict[str, object]:
        boundary = {
            "boundary_id": v3.SELECTED_EVALUATION_BOUNDARY_ID,
            "boundary_type": v3.PRIOR_EVALUATION_BOUNDARY_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_result_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_result": v3.PRIOR_EVALUATION_BOUNDARY_RESULT_REQUIRED,
            "receiver_side_answerable_basis_candidate_evaluation_consideration_allowed": True,
            "selected_candidate_reception_result_referenced": True,
            "selected_candidate_material_referenced": True,
        }
        for key in (
            "receiver_side_answerable_basis_candidate_evaluated",
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "receiver_attestation_created",
            "receiver_attestation_supported",
            "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "second_candidate_received",
            "second_candidate_evaluated",
            "repeated_evaluation_permission_created",
            "reusable_route_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            boundary[key] = False
        return {
            "outcome": v3.PRIOR_EVALUATION_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "receiver_side_answerable_basis_candidate_evaluation_boundary": boundary,
            "receiver_side_answerable_basis_candidate_evaluation_dimensions": {
                dimension_id: {"evaluation_status": v3.DIMENSION_RESULT_NOT_EVALUATED, "established": False}
                for dimension_id in v3.EVALUATION_DIMENSION_IDS
            },
        }

    def _synthetic_reception_artifact(self) -> dict[str, object]:
        return {
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED",
            "failed_check_count": 0,
            "receiver_side_answerable_basis_reception_operation": {
                "receiver_side_answerable_basis_reception_operation_id": v3.SELECTED_RECEPTION_OPERATION_ID,
                "receiver_side_answerable_basis_candidate_id": v3.CANDIDATE_ID,
                "receiver_side_answerable_basis_candidate_type": v3.CANDIDATE_TYPE,
                "receiver_side_answerable_basis_candidate_scope": v3.CANDIDATE_SCOPE,
                "candidate_material_supplied": True,
                "candidate_material_received": True,
                "candidate_material_recorded": True,
                "candidate_material_preserved": True,
                "receiver_side_answerable_basis_candidate_received": True,
                "receiver_side_answerable_basis_candidate_recorded": True,
                "receiver_side_answerable_basis_candidate_evaluated": False,
            },
        }

    def _fixture_root(self, root: Path) -> None:
        spec_markers = [marker for group in v3.V2_SPEC_MARKER_CLASSES.values() for marker in group]
        summary_markers = [marker for group in v3.BOUNDARY_SUMMARY_MARKER_CLASSES.values() for marker in group]
        self._write_text(root / v3.GOVERNING_V2_OPERATION_SPEC_RELATIVE_PATH, "\n".join(spec_markers) + "\n")
        self._write_text(root / v3.EVALUATION_BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH, "\n".join(summary_markers) + "\n")
        self._write_json(root / v3.SELECTED_EVALUATION_BOUNDARY_RESULT_RELATIVE_PATH, self._synthetic_boundary_artifact())
        self._write_json(root / v3.SELECTED_CANDIDATE_RECEPTION_RESULT_RELATIVE_PATH, self._synthetic_reception_artifact())

    def synthetic_request(self) -> dict[str, object]:
        records: dict[str, object] = {}
        for dimension_id in v3.EVALUATION_DIMENSION_IDS:
            rules = v3.DIMENSION_RULES[dimension_id]
            records[dimension_id] = {
                "dimension_id": dimension_id,
                "selected_candidate_id": v3.CANDIDATE_ID,
                "selected_candidate_reception_operation_id": v3.SELECTED_RECEPTION_OPERATION_ID,
                "selected_candidate_evaluation_boundary_id": v3.SELECTED_EVALUATION_BOUNDARY_ID,
                "basis_supplied": True,
                "basis_items": [{"opaque": "synthetic basis item"}],
                "basis_references": [{"opaque": "synthetic basis reference"}],
                "explicit_support_postures": {key: True for key in rules["required_support_postures"]},
                "explicit_contradiction_postures": {key: False for key in rules["recognized_contradiction_postures"]},
                "unresolved_postures": {key: False for key in rules["recognized_unresolved_postures"]},
                "evaluator_reference": "synthetic-bounded-evaluator-reference",
                "basis_non_claims": {key: False for key in v3.DIMENSION_BASIS_REQUIRED_FALSE_NON_CLAIMS},
            }
        return v3.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request(
            evaluation_basis_supplied=True,
            dimension_basis_records=records,
        )

    def v2_globals(self) -> dict[str, object]:
        return {name: getattr(v2, name) for name in self.V2_SYNCED_GLOBALS}

    def assert_v2_globals_restored(self, before: dict[str, object]) -> None:
        self.assertEqual(self.v2_globals(), before)

    def invoke(self, request: dict[str, object] | None = None, root: Path | None = None) -> dict[str, object]:
        before_globals = self.v2_globals()
        supplied = self.clone(request) if request is not None else None
        before_request = self.clone(supplied)
        if root is None:
            result = v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3(supplied)
        else:
            with patch.object(v3, "REPO_ROOT", root):
                result = v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3(supplied)
        self.assert_v2_globals_restored(before_globals)
        self.assertEqual(supplied, before_request)
        return result

    def assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in v3.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_downstream_locks_false(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for key in v3.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation[key], False, key)

    def assert_waiting_work_open(self, result: dict[str, object]) -> None:
        self.assertEqual(tuple(self.open_items(result)), self.WAITING_OPEN)

    def assert_completed_work_not_open(self, result: dict[str, object]) -> None:
        open_items = self.open_items(result)
        for item in self.COMPLETED_WORK:
            self.assertNotIn(item, open_items)
        self.assertEqual(tuple(open_items), self.COMPLETED_OPEN)

    def assert_open_invariants(self, result: dict[str, object]) -> None:
        open_items = self.open_items(result)
        operation = self.operation(result)
        self.assertEqual(result["permitted_future_route"], v3.ADMISSIBLE_FUTURE_ROUTE)
        for item in open_items:
            lowered = item.lower()
            self.assertNotIn("scheduled", lowered)
            self.assertNotIn("authorized", lowered)
            self.assertNotIn("obligation", lowered)
            self.assertNotIn("automatic", lowered)
            self.assertNotIn("reusable", lowered)
        if operation["candidate_evaluation_operation_exhausted"] is True:
            self.assert_completed_work_not_open(result)

    def assert_material_omitted(self, result: dict[str, object]) -> None:
        forbidden = {"candidate_material", "candidate_packet", "basis_items", "basis_references"}

        def walk(value: object) -> None:
            if isinstance(value, dict):
                self.assertFalse(forbidden.intersection(value))
                for nested in value.values():
                    walk(nested)
            elif isinstance(value, list):
                for nested in value:
                    walk(nested)

        walk(result)
        basis = result["receiver_side_answerable_basis_candidate_evaluation_operation_basis"]
        self.assertEqual(set(basis), set(v3.EVALUATION_DIMENSION_IDS))
        self.assertTrue(all(entry["complete_supplied_basis_omitted_from_operation_result"] for entry in basis.values()))

    def test_public_api_and_static_identity_are_preserved(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_from_path",
            "write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result",
            "build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_summary",
            "build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request",
            "build_declared_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request",
        ):
            self.assertTrue(callable(getattr(v3, name)))
        self.assertEqual(v3.RESULT_VERSION, "0.2.0")
        self.assertEqual(v3.RESOLVER_MODULE, "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3")
        for name in (
            "OPERATION_ID", "OPERATION_TYPE", "OPERATION_VERSION", "OPERATION_SCOPE",
            "ADMISSIBLE_FUTURE_ROUTE", "EVALUATION_DIMENSION_IDS", "OUTCOME_FAMILY",
            "OPERATION_RESULT_FAMILY", "SUPPORTED_INTENTS", "PROHIBITED_REQUEST_FLAGS",
            "BLOCK_CODES", "REQUIRED_FALSE_NON_CLAIMS",
        ):
            self.assertEqual(getattr(v3, name), getattr(v2, name), name)
        self.assertNotEqual(v3.OUTPUT_ROOT, v2.OUTPUT_ROOT)
        self.assertNotEqual(v3.OUTPUT_FILENAME, v2.OUTPUT_FILENAME)

    def test_default_waiting_branch_reports_only_waiting_work(self) -> None:
        result = self.invoke()
        operation = self.operation(result)
        self.assertEqual(result["outcome"], v3.OUTCOME_REQUIRES_EVALUATION_BASIS)
        self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], v3.OPERATION_RESULT_REQUIRES_EVALUATION_BASIS)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertIs(operation["evaluation_basis_supplied"], False)
        self.assertIs(operation["evaluation_basis_complete"], False)
        self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], False)
        self.assertIs(operation["candidate_evaluation_operation_exhausted"], False)
        self.assertTrue(all(value == v3.DIMENSION_RESULT_NOT_EVALUATED for value in self.dimension_results(result).values()))
        self.assert_non_claims_false(result)
        self.assert_downstream_locks_false(result)
        self.assert_waiting_work_open(result)
        self.assert_open_invariants(result)

    def test_live_complete_request_matches_v2_and_closes_completed_work(self) -> None:
        request = self.load_complete_request()
        result = self.invoke(request)
        operation = self.operation(result)
        v2_complete = json.loads(V2_COMPLETE_ARTIFACT_PATH.read_text(encoding="utf-8"))
        v2_operation = v2_complete["receiver_side_answerable_basis_candidate_evaluation_operation"]
        self.assertEqual(result["outcome"], v3.OUTCOME_RECORDED)
        self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], v3.OPERATION_RESULT_EVALUATED)
        self.assertEqual(result["result_version"], v3.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], v3.RESOLVER_MODULE)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertEqual(self.dimension_results(result), {
            key: v3.DIMENSION_RESULT_SATISFIED for key in v3.EVALUATION_DIMENSION_IDS
        })
        self.assertTrue(all(entry["dimension_evaluated"] for entry in result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"].values()))
        self.assertTrue(all(entry["dimension_established"] for entry in result["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"].values()))
        for key in (
            "receiver_side_answerable_basis_candidate_evaluated",
            "receiver_side_answerable_basis_candidate_all_dimensions_satisfied",
            "candidate_evaluation_operation_exhausted",
        ):
            self.assertIs(operation[key], True)
            self.assertEqual(operation[key], v2_operation[key])
        self.assert_non_claims_false(result)
        self.assert_downstream_locks_false(result)
        self.assert_completed_work_not_open(result)
        self.assert_open_invariants(result)
        self.assert_material_omitted(result)

    def test_static_and_derived_properties_separate_by_branch(self) -> None:
        waiting = self.invoke()
        completed = self.invoke(self.load_complete_request())
        waiting_operation = self.operation(waiting)
        completed_operation = self.operation(completed)
        self.assertEqual(waiting["blocked_routes"], completed["blocked_routes"])
        self.assertEqual(tuple(waiting["non_claims"]), tuple(completed["non_claims"]))
        self.assertEqual(waiting["permitted_future_route"], completed["permitted_future_route"])
        self.assertEqual(tuple(self.dimension_results(waiting)), tuple(self.dimension_results(completed)))
        self.assertEqual(waiting["upstream_basis"]["governing_paths"], completed["upstream_basis"]["governing_paths"])
        self.assertNotEqual(waiting["missing_or_inconsistent_evaluation_basis"], completed["missing_or_inconsistent_evaluation_basis"])
        self.assertNotEqual(self.dimension_results(waiting), self.dimension_results(completed))
        self.assertNotEqual(waiting_operation["candidate_evaluation_operation_exhausted"], completed_operation["candidate_evaluation_operation_exhausted"])
        self.assertNotEqual(self.open_items(waiting), self.open_items(completed))

    def test_completed_not_satisfied_and_indeterminate_branches_remain_exhausted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_root(root)
            first = v3.EVALUATION_DIMENSION_IDS[0]
            rule = v3.DIMENSION_RULES[first]
            cases = (
                ("not_satisfied", "explicit_contradiction_postures", rule["recognized_contradiction_postures"][0], v3.DIMENSION_RESULT_NOT_SATISFIED),
                ("indeterminate", "unresolved_postures", rule["recognized_unresolved_postures"][0], v3.DIMENSION_RESULT_INDETERMINATE),
            )
            for name, field, key, expected in cases:
                with self.subTest(name=name):
                    request = self.synthetic_request()
                    request["dimension_basis_records"][first][field][key] = True
                    result = self.invoke(request, root)
                    operation = self.operation(result)
                    self.assertEqual(result["outcome"], v3.OUTCOME_RECORDED)
                    self.assertIn(expected, self.dimension_results(result).values())
                    self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], True)
                    self.assertIs(operation["candidate_evaluation_operation_exhausted"], True)
                    self.assert_completed_work_not_open(result)
                    self.assert_downstream_locks_false(result)
                    if expected == v3.DIMENSION_RESULT_NOT_SATISFIED:
                        self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_not_satisfied"], True)
                        self.assertIs(operation["receiver_side_answerable_basis_candidate_insufficient"], False)
                    else:
                        self.assertIs(operation["receiver_side_answerable_basis_candidate_any_dimension_indeterminate"], True)
                        self.assertIs(operation["receiver_side_answerable_basis_candidate_indeterminate"], False)

    def test_blocked_not_recorded_and_v2_global_restoration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_root(root)
            blocked_request = self.synthetic_request()
            prohibited = next(iter(v3.PROHIBITED_REQUEST_FLAGS))
            blocked_request[prohibited] = True
            blocked = self.invoke(blocked_request, root)
            blocked_operation = self.operation(blocked)
            self.assertEqual(blocked["outcome"], v3.OUTCOME_BLOCKED)
            self.assertGreater(self.failed_check_count(blocked), 0)
            self.assertIn(blocked["block"]["code"], v3.BLOCK_CODES)
            self.assertIs(blocked_operation["receiver_side_answerable_basis_candidate_evaluated"], False)
            self.assertIs(blocked_operation["candidate_evaluation_operation_exhausted"], False)
            self.assertNotIn("actual candidate evaluation", self.open_items(blocked))
            self.assert_open_invariants(blocked)
            self.assert_downstream_locks_false(blocked)

            not_recorded_request = v3.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request(intent=v3.INTENT_DO_NOT_RECORD)
            not_recorded = self.invoke(not_recorded_request, root)
            operation = self.operation(not_recorded)
            self.assertEqual(not_recorded["outcome"], v3.OUTCOME_NOT_RECORDED)
            self.assertEqual(operation["receiver_side_answerable_basis_candidate_evaluation_operation_result"], v3.OPERATION_RESULT_NOT_EVALUATED)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluation_operation_recorded"], False)
            self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], False)
            self.assertIs(operation["candidate_evaluation_operation_exhausted"], False)
            self.assert_waiting_work_open(not_recorded)

            before = self.v2_globals()
            with patch.object(v2, "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2", side_effect=RuntimeError("synthetic failure")):
                with patch.object(v3, "REPO_ROOT", root):
                    with self.assertRaisesRegex(RuntimeError, "synthetic failure"):
                        v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3(self.synthetic_request())
            self.assert_v2_globals_restored(before)

    def test_from_path_summary_write_and_material_omission(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._fixture_root(root)
            complete_request = self.synthetic_request()
            complete_path = self._write_json(root / "requests" / "complete.json", complete_request)
            before = self.v2_globals()
            with patch.object(v3, "REPO_ROOT", root):
                complete = v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_from_path(complete_path)
            self.assert_v2_globals_restored(before)
            self.assert_completed_work_not_open(complete)
            self.assert_material_omitted(complete)

            waiting_path = self._write_json(root / "requests" / "waiting.json", v3.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_request())
            with patch.object(v3, "REPO_ROOT", root):
                waiting = v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_from_path(waiting_path)
            self.assert_waiting_work_open(waiting)
            for path in (root / "requests" / "missing.json", self._write_text(root / "requests" / "bad.json", "{"), self._write_json(root / "requests" / "array.json", [])):
                with self.subTest(path=path.name):
                    with patch.object(v3, "REPO_ROOT", root):
                        result = v3.resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_from_path(path)
                    self.assertEqual(result["outcome"], v3.OUTCOME_BLOCKED)

            for result in (waiting, complete):
                summary = v3.build_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_summary(result)
                self.assertEqual(summary["result_version"], v3.RESULT_VERSION)
                self.assertEqual(summary["resolver_module"], v3.RESOLVER_MODULE)
                self.assertEqual(summary["operation_id"], v3.OPERATION_ID)
                self.assertNotIn("what_remains_open", summary)

            blocked_request = self.synthetic_request()
            blocked_request[next(iter(v3.PROHIBITED_REQUEST_FLAGS))] = True
            blocked = self.invoke(blocked_request, root)
            waiting_output = v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(waiting, self.safe_output_path(root, "waiting"))
            output = v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(complete, self.safe_output_path(root, "complete"))
            blocked_output = v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(blocked, self.safe_output_path(root, "blocked"))
            suffix = v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(complete, self.safe_output_path(root, "complete"))
            self.assertTrue(waiting_output.is_file())
            self.assertTrue(blocked_output.is_file())
            self.assertEqual(output.name, v3.OUTPUT_FILENAME)
            self.assertEqual(suffix.name, output.stem + "_001" + output.suffix)
            parsed = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(parsed["resolver_module"], v3.RESOLVER_MODULE)
            self.assertEqual(parsed["result_version"], v3.RESULT_VERSION)
            self.assert_completed_work_not_open(parsed)
            self.assert_non_claims_false(parsed)
            self.assert_material_omitted(parsed)
            with self.assertRaises(v3.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error):
                v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(complete, root / "spec" / "forbidden.json")
            for field, value in (("resolver_module", "wrong"), ("result_version", "wrong"), ("outcome", "wrong")):
                with self.subTest(field=field):
                    malformed = self.clone(complete)
                    malformed[field] = value
                    with self.assertRaises(v3.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error):
                        v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(malformed, self.safe_output_path(root, field))
            malformed = self.clone(complete)
            malformed["non_claims"][v3.REQUIRED_FALSE_NON_CLAIMS[0]] = True
            with self.assertRaises(v3.ReceiverSideAnswerableBasisCandidateEvaluationOperationV0MinV3Error):
                v3.write_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result(malformed, self.safe_output_path(root, "non_claims"))


if __name__ == "__main__":
    unittest.main()
