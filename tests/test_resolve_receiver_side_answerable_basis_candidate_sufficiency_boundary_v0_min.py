"""Bounded tests for candidate-sufficiency consideration admission.

The suite treats the completed V3 evaluation as selected upstream standing only.
It proves that this boundary can admit consideration without deciding candidate
sufficiency or creating a later operation, receiver, presence, or downstream
posture.
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

import resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min as resolver


LIVE_V3_ARTIFACT_PATH = REPO_ROOT / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH
GOVERNING_SPEC_PATH = REPO_ROOT / resolver.GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH
V2_WAITING_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"
    / "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json"
)
V2_COMPLETED_ARTIFACT_PATH = V2_WAITING_ARTIFACT_PATH.with_name(
    V2_WAITING_ARTIFACT_PATH.stem + "_001" + V2_WAITING_ARTIFACT_PATH.suffix
)
V3_RESOLVER_PATH = REPO_ROOT / "src/resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3.py"
BOUNDARY_RESOLVER_PATH = REPO_ROOT / "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min.py"


EXPECTED_V3_OPEN = (
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


class ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinTests(unittest.TestCase):
    """Prove one V3-backed consideration boundary remains bounded."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = tuple(
            path
            for path in (
                GOVERNING_SPEC_PATH,
                BOUNDARY_RESOLVER_PATH,
                V3_RESOLVER_PATH,
                LIVE_V3_ARTIFACT_PATH,
                V2_WAITING_ARTIFACT_PATH,
                V2_COMPLETED_ARTIFACT_PATH,
            )
            if path.is_file()
        )
        cls._preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest() for path in cls._preserved_paths
        }

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected_digest in cls._preserved_hashes.items():
            actual_digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual_digest != expected_digest:
                raise AssertionError(f"preserved lineage changed: {path}")

    def clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def safe_temp_path(self, root: Path, name: str, filename: str = "artifact.json") -> Path:
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in name)
        return root / (safe.strip("._-") or "case") / filename

    def _write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"temporary file path is a directory: {path}")
        path.write_text(text, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("failed_check_count")
        self.assertIsInstance(value, int)
        return value

    def boundary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get("receiver_side_answerable_basis_candidate_sufficiency_boundary")
        self.assertIsInstance(value, dict)
        return value

    def boundary_result(self, result: dict[str, object]) -> str:
        value = self.boundary(result).get("candidate_sufficiency_boundary_result")
        self.assertIsInstance(value, str)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get("receiver_side_answerable_basis_candidate_sufficiency_boundary_checks")
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def assert_all_non_claims_false(self, result: dict[str, object]) -> None:
        value = result.get("non_claims")
        self.assertIsInstance(value, dict)
        self.assertEqual(set(value), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(value[field], False, field)

    def assert_candidate_sufficiency_undecided(self, result: dict[str, object]) -> None:
        boundary = self.boundary(result)
        for field in (
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "candidate_sufficiency_decided",
            "candidate_sufficiency_established",
            "candidate_insufficiency_established",
            "candidate_indeterminacy_established",
            "candidate_sufficiency_operation_created",
            "candidate_sufficiency_operation_authorized",
            "candidate_sufficiency_operation_executed",
        ):
            self.assertIs(boundary[field], False, field)

    def assert_downstream_locks_false(self, result: dict[str, object]) -> None:
        boundary = self.boundary(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(boundary[field], False, field)
        for field in (
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "repeated_candidate_sufficiency_boundary_permission_created",
            "reusable_candidate_sufficiency_route_created",
            "same_candidate_sufficiency_boundary_rerun_authorized",
            "automatic_candidate_sufficiency_boundary_retry_created",
            "candidate_sufficiency_boundary_debt_created",
            "candidate_sufficiency_boundary_obligation_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[field], False, field)

    def assert_no_complete_v3_material(self, result: dict[str, object]) -> None:
        forbidden = {
            "complete_v3_artifact",
            "selected_v3_artifact",
            "candidate_material",
            "candidate_packet",
            "capture_material",
            "basis_items",
            "basis_references",
            "receiver_side_answerable_basis_candidate_evaluation_operation_basis",
            "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
            "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions",
        }

        def walk(value: object) -> None:
            if isinstance(value, dict):
                self.assertFalse(forbidden.intersection(value), value.keys())
                for nested in value.values():
                    walk(nested)
            elif isinstance(value, list):
                for nested in value:
                    walk(nested)

        walk(result)

    def assert_blocked(self, result: dict[str, object], expected: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected is not None:
            self.assertEqual(code, expected)
        self.assertGreater(self.failed_check_count(result), 0)
        for check in self.checks(result):
            for field in ("failure_code", "block_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)
        self.assert_all_non_claims_false(result)
        self.assert_candidate_sufficiency_undecided(result)
        self.assert_downstream_locks_false(result)

    def assert_allowed(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_ALLOWED)
        self.assertEqual(self.boundary_result(result), resolver.BOUNDARY_RESULT_ALLOWED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(result.get("passed_check_count", 0), 0)
        self.assertEqual(result.get("block"), {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        })
        boundary = self.boundary(result)
        for field in (
            "candidate_sufficiency_boundary_recorded",
            "candidate_sufficiency_boundary_result_recorded",
            "candidate_sufficiency_consideration_allowed",
            "candidate_sufficiency_boundary_exhausted",
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded",
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded",
        ):
            self.assertIs(boundary[field], True, field)
        self.assert_candidate_sufficiency_undecided(result)
        self.assert_all_non_claims_false(result)
        self.assert_downstream_locks_false(result)
        self.assert_no_complete_v3_material(result)

    def selected_live_v3_artifact(self) -> dict[str, object]:
        return json.loads(LIVE_V3_ARTIFACT_PATH.read_text(encoding="utf-8"))

    def synthetic_specification(self) -> str:
        markers = (
            "# Receiver-Side Answerable Basis Candidate Sufficiency Boundary V0 Minimum Specification",
            resolver.BOUNDARY_ID,
            resolver.BOUNDARY_TYPE,
            resolver.BOUNDARY_SCOPE,
            resolver.SELECTED_EVALUATION_OPERATION_ID,
            resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            resolver.SELECTED_EVALUATION_RESULT_REQUIRED,
            "candidate evaluation operation exhausted",
            resolver.CANDIDATE_ID,
            resolver.CANDIDATE_TYPE,
            resolver.CANDIDATE_SCOPE,
            resolver.SELECTED_RECEPTION_OPERATION_ID,
            resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            *resolver.REQUIRED_DIMENSION_IDS,
            "candidate evaluation is not candidate sufficiency",
            "all dimensions satisfied is not candidate sufficiency",
            "consideration allowed is not sufficiency established",
            "boundary is not sufficiency operation",
            "single-use",
            "exhausted",
            "no repeated permission",
            "no reusable route",
            "no silent rerun",
            "no automatic retry",
            "no debt or obligation",
            "no retroactive validation",
            "no repair",
            "no repository scan",
            "no file discovery",
            "no validation enforcement",
            resolver.BOUNDARY_RESULT_ALLOWED,
            resolver.ADMISSIBLE_FUTURE_ROUTE,
        )
        return "\n".join(markers) + "\n"

    def synthetic_v3_artifact(self) -> dict[str, object]:
        operation: dict[str, object] = {
            "operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "operation_type": resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            "operation_version": resolver.SELECTED_EVALUATION_OPERATION_VERSION,
            "operation_scope": resolver.SELECTED_EVALUATION_OPERATION_SCOPE,
            "receiver_side_answerable_basis_candidate_evaluation_operation_id": resolver.SELECTED_EVALUATION_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_evaluation_operation_type": resolver.SELECTED_EVALUATION_OPERATION_TYPE,
            "receiver_side_answerable_basis_candidate_evaluation_operation_version": resolver.SELECTED_EVALUATION_OPERATION_VERSION,
            "receiver_side_answerable_basis_candidate_evaluation_operation_scope": resolver.SELECTED_EVALUATION_OPERATION_SCOPE,
            "receiver_side_answerable_basis_candidate_evaluation_operation_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_operation_result_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluation_operation_result": resolver.SELECTED_EVALUATION_RESULT_REQUIRED,
            "evaluation_basis_supplied": True,
            "evaluation_basis_complete": True,
            "all_dimension_basis_records_present": True,
            "all_dimension_basis_records_bounded": True,
            "all_dimension_basis_records_reference_selected_candidate": True,
            "all_dimension_basis_records_reference_selected_boundary": True,
            "all_dimension_basis_records_non_result_preclaiming": True,
            "all_dimension_basis_records_admissible": True,
            "receiver_side_answerable_basis_candidate_evaluated": True,
            "receiver_side_answerable_basis_candidate_all_dimensions_satisfied": True,
            "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied": False,
            "receiver_side_answerable_basis_candidate_any_dimension_indeterminate": False,
            "candidate_evaluation_operation_exhausted": True,
            "receiver_side_answerable_basis_candidate_sufficient": False,
            "receiver_side_answerable_basis_candidate_insufficient": False,
            "receiver_side_answerable_basis_candidate_indeterminate": False,
            "candidate_sufficiency_boundary_created": False,
        }
        for field in (
            "repeated_evaluation_permission_created",
            "reusable_route_created",
            "same_candidate_re_evaluation_authorized",
            "dimension_completion_route_created",
            "second_candidate_received",
            "second_candidate_evaluated",
            "receiver_attestation_created",
            "receiver_attestation_supported",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            operation[field] = False
        dimensions = {
            dimension_id: {
                "dimension_id": dimension_id,
                "dimension_result": resolver.DIMENSION_RESULT_SATISFIED,
                "dimension_evaluated": True,
                "dimension_established": True,
                "basis_referenced": True,
                "missing_or_inconsistent_dimension_basis": [],
            }
            for dimension_id in resolver.REQUIRED_DIMENSION_IDS
        }
        return {
            "resolver_module": resolver.SELECTED_V3_RESOLVER_MODULE,
            "result_version": resolver.SELECTED_V3_RESULT_VERSION,
            "outcome": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_OPERATION_RECORDED",
            "failed_check_count": 0,
            "receiver_side_answerable_basis_candidate_evaluation_operation": operation,
            "declared_receiver_side_answerable_basis_candidate_evaluation_operation_basis": {
                "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
                "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
                "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
                "selected_candidate_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
                "selected_candidate_evaluation_boundary_id": resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            },
            "receiver_side_answerable_basis_candidate_evaluation_operation_dimensions": dimensions,
            "what_remains_open": list(EXPECTED_V3_OPEN),
        }

    def fixture_root(self, root: Path, artifact: dict[str, object] | None = None, specification: str | None = None) -> None:
        self._write_text(
            root / resolver.GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH,
            self.synthetic_specification() if specification is None else specification,
        )
        self._write_json(
            root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH,
            self.clone(self.synthetic_v3_artifact() if artifact is None else artifact),
        )

    def canonical_request(self, **overrides: object) -> dict[str, object]:
        return resolver.build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request(
            **copy.deepcopy(overrides)
        )

    def invoke(
        self, request: dict[str, object] | None = None, root: Path | None = None
    ) -> dict[str, object]:
        supplied = self.clone(request) if request is not None else None
        before = self.clone(supplied)
        if root is None:
            result = resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min(supplied)
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min(supplied)
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_synthetic(self, artifact: dict[str, object] | None = None) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root, artifact=self.clone(artifact) if artifact is not None else None)
            return self.invoke(self.canonical_request(), root)

    def test_public_api_constants_and_request_contract(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min",
        )
        self.assertEqual(resolver.BOUNDARY_ID, "receiver_side_answerable_basis_candidate_sufficiency_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.BOUNDARY_SCOPE, "CONSIDER_SUFFICIENCY_OF_ONE_COMPLETEDLY_EVALUATED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY")
        self.assertEqual(resolver.OUTCOME_FAMILY, (resolver.OUTCOME_ALLOWED, resolver.OUTCOME_BLOCKED, resolver.OUTCOME_NOT_RECORDED))
        self.assertEqual(resolver.BOUNDARY_RESULT_FAMILY, (resolver.BOUNDARY_RESULT_ALLOWED, resolver.BOUNDARY_RESULT_NOT_EVALUATED))
        self.assertEqual(resolver.SUPPORTED_INTENTS, (resolver.INTENT_RECORD, resolver.INTENT_DO_NOT_RECORD, resolver.INTENT_BLOCK))
        self.assertEqual(resolver.OUTPUT_ROOT.name, "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min")
        self.assertTrue(resolver.OUTPUT_FILENAME.endswith("_result.json"))
        self.assertEqual(set(resolver.REQUIRED_DIMENSION_IDS), set(self.synthetic_v3_artifact()["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"]))
        request = self.canonical_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(request["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(request["required_dimension_results"], resolver.REQUIRED_DIMENSION_RESULTS)
        self.assertEqual(set(request["declared_non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(value is False for value in request["declared_non_claims"].values()))
        self.assertTrue(all(code in resolver.BLOCK_CODES for code in resolver.PROHIBITED_REQUEST_FLAGS.values()))
        required_codes = {
            "UPSTREAM_DIMENSION_NOT_SATISFIED",
            "UPSTREAM_DIMENSION_INDETERMINATE",
            "UPSTREAM_OPERATION_NOT_EXHAUSTED",
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            "UPSTREAM_SUFFICIENCY_BOUNDARY_ALREADY_CREATED",
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
            "RESULT_POSTURE_PRECLAIMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "WRITE_REFUSED",
        }
        self.assertTrue(required_codes.issubset(resolver.BLOCK_CODES))

    def test_default_live_v3_artifact_allows_consideration(self) -> None:
        if not GOVERNING_SPEC_PATH.is_file() or not LIVE_V3_ARTIFACT_PATH.is_file():
            self.skipTest("exact governing specification or selected V3 artifact is unavailable")
        before_specification = GOVERNING_SPEC_PATH.read_bytes()
        before_artifact = LIVE_V3_ARTIFACT_PATH.read_bytes()
        result = self.invoke()
        self.assert_allowed(result)
        self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(
            result["upstream_basis"]["governing_paths"]["selected_v3_evaluation_artifact_path"],
            str(resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH),
        )
        self.assertEqual(GOVERNING_SPEC_PATH.read_bytes(), before_specification)
        self.assertEqual(LIVE_V3_ARTIFACT_PATH.read_bytes(), before_artifact)

    def test_synthetic_allowed_result_structure_open_state_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            artifact = self.synthetic_v3_artifact()
            artifact_before = self.clone(artifact)
            specification = self.synthetic_specification()
            self.fixture_root(root, artifact=artifact, specification=specification)
            request = self.canonical_request()
            request_before = self.clone(request)
            result = self.invoke(request, root)
            self.assert_allowed(result)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(request, request_before)
            expected_sections = {
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_metadata",
                "declared_receiver_side_answerable_basis_candidate_sufficiency_boundary_basis",
                "upstream_basis",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_statement",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_non_meaning",
                "boundary_result_detail",
                "permitted_future_route",
                "blocked_routes",
                "what_remains_open",
                "non_claims",
                "outcome",
                "block",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_summary",
                "resolver_module",
                "result_version",
            }
            self.assertTrue(expected_sections.issubset(result))
            boundary = self.boundary(result)
            for wrapper_field in (
                "outcome",
                "block",
                "non_claims",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks",
                "receiver_side_answerable_basis_candidate_sufficiency_boundary_summary",
            ):
                self.assertNotIn(wrapper_field, boundary)
            self.assertEqual(tuple(result["what_remains_open"]), resolver.ALLOWED_WHAT_REMAINS_OPEN)
            self.assertNotIn("candidate-sufficiency boundary resolver", result["what_remains_open"])
            self.assertEqual(result["permitted_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
            summary = resolver.build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_summary(result)
            self.assertEqual(summary, result["receiver_side_answerable_basis_candidate_sufficiency_boundary_summary"])
            self.assertEqual(summary["boundary_result"], resolver.BOUNDARY_RESULT_ALLOWED)
            self.assertTrue(summary["atomic_gate_validated"])
            self.assertTrue(summary["eight_dimensions_validated"])
            self.assertTrue(summary["candidate_aggregate_validated"])
            self.assertTrue(summary["current_false_posture_validated"])

    def test_all_eight_dimensions_require_exact_satisfied_established_referenced_basis(self) -> None:
        mutation_cases = (
            ("missing_dimension", "UPSTREAM_DIMENSION_NOT_EVALUATED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"].pop(d)),
            ("unknown_dimension", "UPSTREAM_DIMENSION_NOT_EVALUATED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"].update({"unknown_dimension": self.clone(a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d])})),
            ("mismatched_id", "UPSTREAM_DIMENSION_ID_MISMATCH", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_id": "other"})),
            ("not_evaluated", "UPSTREAM_DIMENSION_NOT_EVALUATED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_result": resolver.DIMENSION_RESULT_NOT_EVALUATED})),
            ("not_satisfied", "UPSTREAM_DIMENSION_NOT_SATISFIED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_result": resolver.DIMENSION_RESULT_NOT_SATISFIED})),
            ("indeterminate", "UPSTREAM_DIMENSION_INDETERMINATE", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_result": resolver.DIMENSION_RESULT_INDETERMINATE})),
            ("unevaluated", "UPSTREAM_DIMENSION_NOT_EVALUATED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_evaluated": False})),
            ("unestablished", "UPSTREAM_DIMENSION_NOT_ESTABLISHED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"dimension_established": False})),
            ("unreferenced", "UPSTREAM_DIMENSION_BASIS_NOT_REFERENCED", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"basis_referenced": False})),
            ("missing_basis", "UPSTREAM_DIMENSION_BASIS_INCONSISTENT", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"missing_or_inconsistent_dimension_basis": ["missing"]})),
            ("nonlist_missing_basis", "UPSTREAM_DIMENSION_BASIS_INCONSISTENT", lambda a, d: a["receiver_side_answerable_basis_candidate_evaluation_operation_dimensions"][d].update({"missing_or_inconsistent_dimension_basis": "missing"})),
        )
        for dimension_id in resolver.REQUIRED_DIMENSION_IDS:
            for label, expected_code, mutate in mutation_cases:
                with self.subTest(dimension=dimension_id, mutation=label):
                    artifact = self.synthetic_v3_artifact()
                    mutate(artifact, dimension_id)
                    self.assert_blocked(self.resolve_synthetic(artifact), expected_code)

    def test_atomic_aggregate_identity_existing_and_open_state_locks(self) -> None:
        operation_mutations = (
            ("basis_supplied", "evaluation_basis_supplied", False, "UPSTREAM_EVALUATION_ATOMIC_GATE_INCOMPLETE"),
            ("basis_complete", "evaluation_basis_complete", False, "UPSTREAM_EVALUATION_ATOMIC_GATE_INCOMPLETE"),
            ("atomic_gate", "all_dimension_basis_records_admissible", False, "UPSTREAM_EVALUATION_ATOMIC_GATE_INCOMPLETE"),
            ("candidate_evaluated", "receiver_side_answerable_basis_candidate_evaluated", False, "UPSTREAM_CANDIDATE_NOT_EVALUATED"),
            ("all_satisfied", "receiver_side_answerable_basis_candidate_all_dimensions_satisfied", False, "UPSTREAM_ALL_DIMENSIONS_NOT_SATISFIED"),
            ("any_not_satisfied", "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied", True, "UPSTREAM_DIMENSION_NOT_SATISFIED"),
            ("any_indeterminate", "receiver_side_answerable_basis_candidate_any_dimension_indeterminate", True, "UPSTREAM_DIMENSION_INDETERMINATE"),
            ("unexhausted", "candidate_evaluation_operation_exhausted", False, "UPSTREAM_OPERATION_NOT_EXHAUSTED"),
            ("candidate_sufficient", "receiver_side_answerable_basis_candidate_sufficient", True, "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT"),
            ("candidate_insufficient", "receiver_side_answerable_basis_candidate_insufficient", True, "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT"),
            ("candidate_indeterminate", "receiver_side_answerable_basis_candidate_indeterminate", True, "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT"),
            ("boundary_created", "candidate_sufficiency_boundary_created", True, "UPSTREAM_SUFFICIENCY_BOUNDARY_ALREADY_CREATED"),
            ("attestation", "receiver_attestation_created", True, "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT"),
            ("receipt", "receiver_answerable_receipt_present", True, "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT"),
            ("presence", "presence_supported", True, "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT"),
            ("follow_on", "follow_on_work_authorized", True, "UPSTREAM_DOWNSTREAM_POSTURE_ALREADY_PRESENT"),
            ("repeated", "repeated_evaluation_permission_created", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
            ("reusable", "reusable_route_created", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
            ("same_candidate", "same_candidate_re_evaluation_authorized", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
            ("dimension_route", "dimension_completion_route_created", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
            ("second_candidate", "second_candidate_received", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
            ("second_candidate_evaluated", "second_candidate_evaluated", True, "UPSTREAM_RERUN_OR_REUSABLE_ROUTE_PRESENT"),
        )
        for label, field, value, expected_code in operation_mutations:
            with self.subTest(mutation=label):
                artifact = self.synthetic_v3_artifact()
                artifact["receiver_side_answerable_basis_candidate_evaluation_operation"][field] = value
                self.assert_blocked(self.resolve_synthetic(artifact), expected_code)
        identity_mutations = (
            ("resolver_module", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "resolver_module", "other"),
            ("result_version", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "result_version", "0.0.0"),
            ("outcome", "UPSTREAM_EVALUATION_OUTCOME_MISMATCH", "outcome", "other"),
            ("failed_checks", "UPSTREAM_EVALUATION_FAILED_CHECKS_PRESENT", "failed_check_count", 1),
            ("result", "UPSTREAM_EVALUATION_RESULT_MISMATCH", "receiver_side_answerable_basis_candidate_evaluation_operation_result", "other"),
            ("operation_id", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "operation_id", "other"),
            ("operation_type", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "operation_type", "other"),
            ("operation_version", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "operation_version", "0.0.0"),
            ("operation_scope", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "operation_scope", "other"),
            ("operation_id_alias", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "receiver_side_answerable_basis_candidate_evaluation_operation_id", "other"),
            ("operation_type_alias", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "receiver_side_answerable_basis_candidate_evaluation_operation_type", "other"),
            ("operation_version_alias", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "receiver_side_answerable_basis_candidate_evaluation_operation_version", "0.0.0"),
            ("operation_scope_alias", "SELECTED_EVALUATION_IDENTITY_MISMATCH", "receiver_side_answerable_basis_candidate_evaluation_operation_scope", "other"),
        )
        for label, expected_code, field, value in identity_mutations:
            with self.subTest(identity=label):
                artifact = self.synthetic_v3_artifact()
                target = artifact if field in {"resolver_module", "result_version", "outcome", "failed_check_count"} else artifact["receiver_side_answerable_basis_candidate_evaluation_operation"]
                target[field] = value
                self.assert_blocked(self.resolve_synthetic(artifact), expected_code)
        for field in (
            "receiver_side_answerable_basis_candidate_id",
            "receiver_side_answerable_basis_candidate_type",
            "receiver_side_answerable_basis_candidate_scope",
            "selected_candidate_reception_operation_id",
            "selected_candidate_evaluation_boundary_id",
        ):
            with self.subTest(candidate_identity=field):
                artifact = self.synthetic_v3_artifact()
                artifact["declared_receiver_side_answerable_basis_candidate_evaluation_operation_basis"][field] = "other"
                self.assert_blocked(self.resolve_synthetic(artifact), "SELECTED_CANDIDATE_IDENTITY_MISMATCH")
        for stale_open in (
            EXPECTED_V3_OPEN[1:],
            ("candidate-sufficiency boundary, if separately selected after completed evaluation", *EXPECTED_V3_OPEN[1:]),
            ("separately supplied eight-dimension evaluation basis", *EXPECTED_V3_OPEN),
            ("actual candidate evaluation", *EXPECTED_V3_OPEN),
            ("dimension-specific derived results", *EXPECTED_V3_OPEN),
            ("automatic re-evaluation", *EXPECTED_V3_OPEN),
            ("same-candidate retry", *EXPECTED_V3_OPEN),
        ):
            with self.subTest(stale_open=stale_open[0]):
                artifact = self.synthetic_v3_artifact()
                artifact["what_remains_open"] = list(stale_open)
                self.assert_blocked(self.resolve_synthetic(artifact), "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED")
        artifact = self.synthetic_v3_artifact()
        artifact["what_remains_open"] = "not-a-list"
        self.assert_blocked(self.resolve_synthetic(artifact), "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED")

    def test_request_nonclaim_prohibited_preclaim_and_intent_validation(self) -> None:
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min([]),
            "REQUEST_NOT_MAPPING",
        )
        for field, value, expected_code in (
            ("intent", "UNSUPPORTED", "UNSUPPORTED_INTENT"),
            ("boundary_id", "other", "REQUEST_VALUE_MISMATCH"),
            ("boundary_type", "other", "REQUEST_VALUE_MISMATCH"),
            ("boundary_version", "0.0.0", "REQUEST_VALUE_MISMATCH"),
            ("boundary_scope", "other", "REQUEST_VALUE_MISMATCH"),
            ("receiver_side_answerable_basis_candidate_id", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            ("selected_candidate_evaluation_operation_id", "other", "SELECTED_EVALUATION_IDENTITY_MISMATCH"),
            ("governing_sufficiency_boundary_specification_path", "other", "REQUEST_VALUE_MISMATCH"),
            ("selected_v3_evaluation_artifact_path", "other", "REQUEST_VALUE_MISMATCH"),
            ("admissible_future_route", "other", "REQUEST_VALUE_MISMATCH"),
        ):
            with self.subTest(request_field=field):
                request = self.canonical_request(**{field: value})
                self.assert_blocked(self.invoke(request), expected_code)
        request = self.canonical_request(unexpected=True)
        self.assert_blocked(self.invoke(request), "REQUEST_VALUE_MISMATCH")
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                request = self.canonical_request()
                request["declared_non_claims"][field] = True
                result = self.invoke(request)
                self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assertIs(result["non_claims"][field], False)
        for malformed in (
            {},
            {field: False for field in resolver.REQUIRED_FALSE_NON_CLAIMS[:-1]},
            None,
            0,
            "false",
        ):
            with self.subTest(malformed_non_claims=repr(malformed)):
                self.assert_blocked(
                    self.invoke(self.canonical_request(declared_non_claims=malformed)),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
        for field, code in resolver.PROHIBITED_REQUEST_FLAGS.items():
            with self.subTest(prohibited_flag=field):
                result = self.invoke(self.canonical_request(**{field: True}))
                self.assert_blocked(result, code)
                self.assertIs(self.boundary(result)["candidate_sufficiency_consideration_allowed"], False)
        boundary_preclaims = (
            ("candidate_sufficiency_boundary_recorded", True),
            ("candidate_sufficiency_boundary_result_recorded", True),
            ("candidate_sufficiency_boundary_result", resolver.BOUNDARY_RESULT_ALLOWED),
            ("candidate_sufficiency_consideration_allowed", True),
            ("candidate_sufficiency_boundary_exhausted", True),
            ("receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded", True),
            ("receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded", True),
            ("receiver_side_answerable_basis_candidate_sufficiency_boundary_result", resolver.BOUNDARY_RESULT_ALLOWED),
            *((field, True) for field in resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        for field, value in boundary_preclaims:
            with self.subTest(preclaim=field):
                self.assert_blocked(self.invoke(self.canonical_request(**{field: value})), "RESULT_POSTURE_PRECLAIMED")
        not_recorded = self.invoke(self.canonical_request(intent=resolver.INTENT_DO_NOT_RECORD))
        self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertEqual(self.boundary_result(not_recorded), resolver.BOUNDARY_RESULT_NOT_EVALUATED)
        self.assertEqual(self.failed_check_count(not_recorded), 0)
        boundary = self.boundary(not_recorded)
        for field in (
            "candidate_sufficiency_boundary_recorded",
            "candidate_sufficiency_boundary_result_recorded",
            "candidate_sufficiency_consideration_allowed",
            "candidate_sufficiency_boundary_exhausted",
        ):
            self.assertIs(boundary[field], False, field)
        self.assert_candidate_sufficiency_undecided(not_recorded)
        self.assert_downstream_locks_false(not_recorded)
        self.assert_blocked(
            self.invoke(self.canonical_request(intent=resolver.INTENT_BLOCK)), "EXPLICIT_BLOCK_REQUESTED"
        )

    def test_upstream_file_and_specification_failure_modes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request = self.canonical_request()
            self.assert_blocked(self.invoke(request, root), "SUFFICIENCY_BOUNDARY_SPEC_REFERENCE_MISSING")
            self.fixture_root(root, specification="missing markers\n")
            self.assert_blocked(self.invoke(request, root), "SUFFICIENCY_BOUNDARY_SPEC_MARKER_MISSING")
            self._write_text(root / resolver.GOVERNING_SUFFICIENCY_BOUNDARY_SPECIFICATION_RELATIVE_PATH, self.synthetic_specification())
            (root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH).unlink()
            self.assert_blocked(self.invoke(request, root), "SELECTED_V3_EVALUATION_ARTIFACT_REFERENCE_MISSING")
            self._write_text(root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH, "{")
            self.assert_blocked(self.invoke(request, root), "SELECTED_V3_EVALUATION_ARTIFACT_NOT_PARSEABLE")
            self._write_json(root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH, [])
            self.assert_blocked(self.invoke(request, root), "SELECTED_V3_EVALUATION_ARTIFACT_NOT_MAPPING")
            self._write_json(root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH, self.synthetic_v3_artifact())
            path = root / resolver.SELECTED_V3_EVALUATION_ARTIFACT_RELATIVE_PATH
            path.unlink()
            path.mkdir(parents=True)
            self.assert_blocked(self.invoke(request, root), "SELECTED_V3_EVALUATION_ARTIFACT_REFERENCE_MISSING")

    def test_from_path_summary_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory(prefix="boundary_output_") as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            request = self.canonical_request()
            request_path = self.safe_temp_path(root, "request", "request.json")
            self._write_json(request_path, request)
            with patch.object(resolver, "REPO_ROOT", root):
                allowed = resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path(request_path)
            self.assert_allowed(allowed)
            malformed_path = self.safe_temp_path(root, "malformed", "request.json")
            self._write_text(malformed_path, "{")
            with patch.object(resolver, "REPO_ROOT", root):
                self.assert_blocked(
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path(malformed_path),
                    "REQUEST_NOT_MAPPING",
                )
                self.assert_blocked(
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path(root / "missing.json"),
                    "REQUEST_NOT_MAPPING",
                )
                list_path = self.safe_temp_path(root, "list", "request.json")
                self._write_json(list_path, [])
                self.assert_blocked(
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_from_path(list_path),
                    "REQUEST_NOT_MAPPING",
                )
            blocked = self.invoke(self.canonical_request(intent=resolver.INTENT_BLOCK), root)
            not_recorded = self.invoke(self.canonical_request(intent=resolver.INTENT_DO_NOT_RECORD), root)
            for result in (allowed, blocked, not_recorded):
                summary = resolver.build_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_summary(result)
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(summary["failed_check_count"], result["failed_check_count"])
                self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
                self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
                self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
                self.assertEqual(summary["selected_candidate_id"], resolver.CANDIDATE_ID)
                self.assertEqual(summary["selected_evaluation_operation_id"], resolver.SELECTED_EVALUATION_OPERATION_ID)
                self.assertIn("atomic_gate_validated", summary)
                self.assertIn("eight_dimensions_validated", summary)
                self.assertIn("candidate_aggregate_validated", summary)
                self.assertIn("candidate_results_false", summary)
                self.assertIn("receiver_receipt_presence_downstream_false", summary)
            output_root = root / "output"
            allowed_before_write = self.clone(allowed)
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(allowed)
                second = resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(allowed)
            self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(second.name, first.stem + "_001" + first.suffix)
            self.assertTrue(first.is_file())
            persisted = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(persisted["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(persisted["result_version"], resolver.RESULT_VERSION)
            self.assert_all_non_claims_false(persisted)
            self.assert_no_complete_v3_material(persisted)
            self.assertEqual(allowed, allowed_before_write)
            blocked_path = self.safe_temp_path(root, "blocked-output", "blocked.json")
            not_recorded_path = self.safe_temp_path(root, "not-recorded-output", "not-recorded.json")
            self.assertTrue(resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(blocked, blocked_path).is_file())
            self.assertTrue(resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(not_recorded, not_recorded_path).is_file())
            for forbidden_root in ("spec", "tests", "reference", "evaluation_operation"):
                with self.subTest(forbidden_root=forbidden_root):
                    with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(
                            allowed, root / forbidden_root / "forbidden.json"
                        )
            invalid = self.clone(allowed)
            invalid["resolver_module"] = "other"
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "invalid-module"))
            invalid = self.clone(allowed)
            invalid["result_version"] = "0.0.0"
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "invalid-version"))
            invalid = self.clone(allowed)
            invalid["outcome"] = "other"
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "invalid-outcome"))
            invalid = self.clone(allowed)
            invalid["non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = True
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "invalid-non-claim"))
            invalid = self.clone(allowed)
            invalid["receiver_side_answerable_basis_candidate_sufficiency_boundary"]["candidate_sufficiency_consideration_allowed"] = False
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "invalid-allowed"))
            invalid = self.clone(allowed)
            invalid["selected_v3_artifact"] = {"forbidden": True}
            with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBoundaryV0MinError):
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min_result(invalid, self.safe_temp_path(root, "copied-material"))

    def test_non_mutation_lineage_and_smoke_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            artifact = self.synthetic_v3_artifact()
            specification = self.synthetic_specification()
            artifact_before = self.clone(artifact)
            specification_before = specification
            request = self.canonical_request()
            request_before = self.clone(request)
            self.fixture_root(root, artifact=artifact, specification=specification)
            matrix = (
                ("allowed", artifact, request, resolver.OUTCOME_ALLOWED),
                ("not_satisfied", self._mutated_artifact("receiver_side_answerable_basis_candidate_evaluation_operation", "receiver_side_answerable_basis_candidate_any_dimension_not_satisfied", True), request, resolver.OUTCOME_BLOCKED),
                ("indeterminate", self._mutated_artifact("receiver_side_answerable_basis_candidate_evaluation_operation", "receiver_side_answerable_basis_candidate_any_dimension_indeterminate", True), request, resolver.OUTCOME_BLOCKED),
                ("unexhausted", self._mutated_artifact("receiver_side_answerable_basis_candidate_evaluation_operation", "candidate_evaluation_operation_exhausted", False), request, resolver.OUTCOME_BLOCKED),
                ("candidate_result", self._mutated_artifact("receiver_side_answerable_basis_candidate_evaluation_operation", "receiver_side_answerable_basis_candidate_sufficient", True), request, resolver.OUTCOME_BLOCKED),
                ("existing_boundary", self._mutated_artifact("receiver_side_answerable_basis_candidate_evaluation_operation", "candidate_sufficiency_boundary_created", True), request, resolver.OUTCOME_BLOCKED),
                ("stale_open", self._mutated_open_artifact(), request, resolver.OUTCOME_BLOCKED),
                ("prohibited", artifact, self.canonical_request(request_candidate_sufficiency_decision=True), resolver.OUTCOME_BLOCKED),
                ("blocked_intent", artifact, self.canonical_request(intent=resolver.INTENT_BLOCK), resolver.OUTCOME_BLOCKED),
                ("not_recorded", artifact, self.canonical_request(intent=resolver.INTENT_DO_NOT_RECORD), resolver.OUTCOME_NOT_RECORDED),
            )
            for name, case_artifact, case_request, expected_outcome in matrix:
                with self.subTest(case=name):
                    case_root = root / name
                    self.fixture_root(case_root, artifact=self.clone(case_artifact), specification=specification)
                    result = self.invoke(self.clone(case_request), case_root)
                    self.assertEqual(result["outcome"], expected_outcome)
                    self.assert_all_non_claims_false(result)
                    self.assert_candidate_sufficiency_undecided(result)
                    self.assert_downstream_locks_false(result)
                    self.assert_no_complete_v3_material(result)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(specification, specification_before)
            self.assertEqual(request, request_before)

    def _mutated_artifact(self, section: str, field: str, value: object) -> dict[str, object]:
        artifact = self.synthetic_v3_artifact()
        artifact[section][field] = value
        return artifact

    def _mutated_open_artifact(self) -> dict[str, object]:
        artifact = self.synthetic_v3_artifact()
        artifact["what_remains_open"] = ["automatic re-evaluation", *EXPECTED_V3_OPEN]
        return artifact


if __name__ == "__main__":
    unittest.main()
