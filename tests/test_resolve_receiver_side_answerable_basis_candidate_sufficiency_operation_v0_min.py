"""Bounded tests for one receiver-side candidate-sufficiency operation.

The suite proves that absent sufficiency basis is lawful waiting, while one
complete eight-record basis is admitted atomically and yields exactly one
resolver-derived candidate result.  Complete basis and upstream material stay
omitted, completed operations exhaust, and no attestation, receipt, presence,
rerun, repair, or downstream standing is created.
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

import resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min as resolver


GOVERNING_SPEC_PATH = (
    REPO_ROOT / resolver.GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH
)
LIVE_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / resolver.SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
OPERATION_RESOLVER_PATH = (
    REPO_ROOT
    / "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min.py"
)
BOUNDARY_RESOLVER_PATH = (
    REPO_ROOT
    / "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min.py"
)
BOUNDARY_TEST_PATH = (
    REPO_ROOT
    / "tests/test_resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min.py"
)
BOUNDARY_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
V3_RESOLVER_PATH = (
    REPO_ROOT
    / "src/resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3.py"
)
V3_TEST_PATH = (
    REPO_ROOT
    / "tests/test_resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3.py"
)
V3_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3"
    / "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3_result.json"
)
V2_WAITING_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2"
    / "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v2_result.json"
)
V2_COMPLETED_ARTIFACT_PATH = V2_WAITING_ARTIFACT_PATH.with_name(
    V2_WAITING_ARTIFACT_PATH.stem + "_001" + V2_WAITING_ARTIFACT_PATH.suffix
)


class ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinTests(
    unittest.TestCase
):
    """Prove one selected candidate receives only one bounded result posture."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = tuple(
            path
            for path in (
                GOVERNING_SPEC_PATH,
                OPERATION_RESOLVER_PATH,
                LIVE_BOUNDARY_ARTIFACT_PATH,
                BOUNDARY_RESOLVER_PATH,
                BOUNDARY_TEST_PATH,
                BOUNDARY_TERMINAL_SUMMARY_PATH,
                V3_RESOLVER_PATH,
                V3_TEST_PATH,
                V3_ARTIFACT_PATH,
                V2_WAITING_ARTIFACT_PATH,
                V2_COMPLETED_ARTIFACT_PATH,
            )
            if path.is_file()
        )
        cls._preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in cls._preserved_paths
        }

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls._preserved_hashes.items():
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                raise AssertionError(f"preserved lineage changed: {path}")

    def clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def safe_temporary_output_path(
        self, root: Path, name: str, filename: str | None = None
    ) -> Path:
        safe = "".join(
            character if character.isalnum() or character in "._-" else "_"
            for character in str(name)
        )
        safe = safe.strip("._-") or "case"
        return root / safe / (filename or resolver.OUTPUT_FILENAME)

    def _write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"temporary file path is a directory: {path}")
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(
            path, json.dumps(value, indent=2, sort_keys=True) + "\n"
        )

    def load_live_selected_sufficiency_boundary_artifact(
        self,
    ) -> dict[str, object]:
        value = json.loads(LIVE_BOUNDARY_ARTIFACT_PATH.read_text(encoding="utf-8"))
        self.assertIsInstance(value, dict)
        return value

    def synthetic_governing_operation_specification(self) -> str:
        markers = (
            *resolver.SPEC_MARKERS,
            "receiver_side_answerable_basis_candidate_sufficiency_operation_version = 0.1.0",
            resolver.CANDIDATE_ID,
            resolver.CANDIDATE_TYPE,
            resolver.CANDIDATE_SCOPE,
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
            "atomic sufficiency-basis gate",
            "exactly one record for each dimension",
            "separately supplied bounded sufficiency basis",
            "evaluation basis is not sufficiency basis",
            resolver.OPERATION_RESULT_REQUIRES_BASIS,
            "INDETERMINATE takes precedence over INSUFFICIENT",
            "INSUFFICIENT takes precedence over SUFFICIENT",
            "Partial evaluation does not stand",
            "Candidate sufficient is not receiver attestation, receiver answerable receipt, or presence support",
            "Candidate insufficient is not rejection of the candidate's existence",
            "Candidate indeterminate is not candidate insufficiency",
            "single-use",
            "operation exhaustion",
            "no repeated permission",
            "no reusable route",
            "no automatic retry",
            "no debt",
            "no obligation",
            "no follow-on authorization",
        )
        return "\n".join(markers) + "\n"

    def synthetic_valid_boundary_artifact(self) -> dict[str, object]:
        boundary: dict[str, object] = {
            "boundary_id": resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
            "boundary_type": resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
            "boundary_version": resolver.SELECTED_SUFFICIENCY_BOUNDARY_VERSION,
            "boundary_scope": resolver.SELECTED_SUFFICIENCY_BOUNDARY_SCOPE,
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_id": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_type": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_version": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_VERSION
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_scope": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_SCOPE
            ),
            "candidate_sufficiency_boundary_result": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_result": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "selected_candidate_reception_operation_id": (
                resolver.SELECTED_RECEPTION_OPERATION_ID
            ),
            "selected_candidate_evaluation_boundary_id": (
                resolver.SELECTED_EVALUATION_BOUNDARY_ID
            ),
            "selected_candidate_evaluation_operation_id": (
                resolver.SELECTED_EVALUATION_OPERATION_ID
            ),
            "admissible_future_route": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_ADMISSIBLE_FUTURE_ROUTE
            ),
            "candidate_sufficiency_boundary_recorded": True,
            "candidate_sufficiency_boundary_result_recorded": True,
            "candidate_sufficiency_consideration_allowed": True,
            "candidate_sufficiency_boundary_exhausted": True,
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded": (
                True
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded": (
                True
            ),
        }
        for field in (
            *resolver.REQUIRED_UPSTREAM_CANDIDATE_FALSE_POSTURES,
            *resolver.REQUIRED_UPSTREAM_OPERATION_FALSE_POSTURES,
            *resolver.REQUIRED_UPSTREAM_RECEIVER_FALSE_POSTURES,
            *resolver.REQUIRED_UPSTREAM_REPEAT_FALSE_POSTURES,
        ):
            boundary[field] = False
        summary = {
            "atomic_gate_validated": True,
            "eight_dimensions_validated": True,
            "candidate_aggregate_validated": True,
            "exhaustion_validated": True,
            "current_false_posture_validated": True,
            "candidate_results_false": True,
            "receiver_receipt_presence_downstream_false": True,
            "repeated_reusable_rerun_false": True,
        }
        return {
            "resolver_module": resolver.SELECTED_SUFFICIENCY_BOUNDARY_RESOLVER_MODULE,
            "result_version": resolver.RESULT_VERSION,
            "outcome": resolver.SELECTED_SUFFICIENCY_BOUNDARY_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "passed_check_count": 98,
            "receiver_side_answerable_basis_candidate_sufficiency_boundary": (
                boundary
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_summary": (
                summary
            ),
            "what_remains_open": list(resolver.EXPECTED_UPSTREAM_WHAT_REMAINS_OPEN),
        }

    def fixture_root(
        self,
        root: Path,
        *,
        boundary_artifact: dict[str, object] | None = None,
        specification: str | None = None,
    ) -> None:
        self._write_text(
            root / resolver.GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH,
            (
                self.synthetic_governing_operation_specification()
                if specification is None
                else specification
            ),
        )
        self._write_json(
            root / resolver.SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            self.clone(
                self.synthetic_valid_boundary_artifact()
                if boundary_artifact is None
                else boundary_artifact
            ),
        )

    def canonical_waiting_request(self, **overrides: object) -> dict[str, object]:
        return (
            resolver.build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def valid_sufficiency_basis_records(self) -> dict[str, dict[str, object]]:
        records: dict[str, dict[str, object]] = {}
        for dimension_id in resolver.SUFFICIENCY_DIMENSION_IDS:
            keys = resolver.DIMENSION_RULE_KEYS[dimension_id]
            records[dimension_id] = {
                "dimension_id": dimension_id,
                "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
                "selected_candidate_sufficiency_boundary_id": (
                    resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID
                ),
                "basis_items": [
                    {
                        "basis_item_id": dimension_id + "_item_001",
                        "bounded_posture": "synthetic support input",
                    }
                ],
                "basis_references": [
                    {
                        "basis_reference_id": dimension_id + "_reference_001",
                        "selected_candidate_id": resolver.CANDIDATE_ID,
                    }
                ],
                "evaluator_reference": {
                    "evaluator_reference_id": "bounded_synthetic_evaluator",
                    "scope": "test-only declared rule-input evaluation",
                },
                "support_postures": {keys["support"]: True},
                "contradiction_postures": {keys["contradiction"]: False},
                "unresolved_postures": {keys["unresolved"]: False},
                "basis_non_claims": {
                    field: False for field in resolver.REQUIRED_BASIS_NON_CLAIMS
                },
                "non_conversion_statement": (
                    resolver.DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
                ),
            }
        return records

    def set_dimension_posture(
        self,
        records: dict[str, dict[str, object]],
        dimension_id: str,
        *,
        support: bool | None = None,
        contradiction: bool | None = None,
        unresolved: bool | None = None,
    ) -> dict[str, dict[str, object]]:
        changed = self.clone(records)
        keys = resolver.DIMENSION_RULE_KEYS[dimension_id]
        if support is not None:
            changed[dimension_id]["support_postures"][keys["support"]] = support
        if contradiction is not None:
            changed[dimension_id]["contradiction_postures"][
                keys["contradiction"]
            ] = contradiction
        if unresolved is not None:
            changed[dimension_id]["unresolved_postures"][
                keys["unresolved"]
            ] = unresolved
        return changed

    def request_with_records(
        self, records: dict[str, dict[str, object]], **overrides: object
    ) -> dict[str, object]:
        return (
            resolver.build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request(
                sufficiency_basis_records=self.clone(records),
                **copy.deepcopy(overrides),
            )
        )

    def sufficient_request(self) -> dict[str, object]:
        return self.request_with_records(self.valid_sufficiency_basis_records())

    def insufficient_request(
        self, *, missing_support: bool = False
    ) -> dict[str, object]:
        records = self.valid_sufficiency_basis_records()
        dimension_id = resolver.SUFFICIENCY_DIMENSION_IDS[0]
        records = self.set_dimension_posture(
            records,
            dimension_id,
            support=False if missing_support else None,
            contradiction=False if missing_support else True,
        )
        return self.request_with_records(records)

    def indeterminate_request(self) -> dict[str, object]:
        records = self.set_dimension_posture(
            self.valid_sufficiency_basis_records(),
            resolver.SUFFICIENCY_DIMENSION_IDS[0],
            unresolved=True,
        )
        return self.request_with_records(records)

    def invoke(
        self,
        request: dict[str, object] | None = None,
        root: Path | None = None,
    ) -> dict[str, object]:
        supplied = self.clone(request) if request is not None else None
        before = self.clone(supplied)
        if root is None:
            result = (
                resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_synthetic(
        self,
        request: dict[str, object] | None = None,
        *,
        boundary_artifact: dict[str, object] | None = None,
        specification: str | None = None,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(
                root,
                boundary_artifact=self.clone(boundary_artifact)
                if boundary_artifact is not None
                else None,
                specification=specification,
            )
            return self.invoke(
                self.canonical_waiting_request() if request is None else request,
                root,
            )

    def operation(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_operation"
        )
        self.assertIsInstance(value, dict)
        return value

    def operation_result(self, result: dict[str, object]) -> str:
        value = self.operation(result).get("operation_result")
        self.assertIsInstance(value, str)
        return value

    def failed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("failed_check_count")
        self.assertIsInstance(value, int)
        self.assertNotIsInstance(value, bool)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_operation_checks"
        )
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(entry, dict) for entry in value))
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        value = block.get("code") or block.get("block_code")
        self.assertTrue(value is None or isinstance(value, str))
        return value

    def candidate_result_postures(
        self, result: dict[str, object]
    ) -> dict[str, bool]:
        operation = self.operation(result)
        return {
            field: operation[field]
            for field in (
                "receiver_side_answerable_basis_candidate_sufficient",
                "receiver_side_answerable_basis_candidate_insufficient",
                "receiver_side_answerable_basis_candidate_indeterminate",
                "candidate_sufficiency_decided",
                "candidate_sufficiency_established",
                "candidate_insufficiency_established",
                "candidate_indeterminacy_established",
            )
        }

    def dimension_results(self, result: dict[str, object]) -> dict[str, str]:
        dimensions = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
        )
        self.assertIsInstance(dimensions, dict)
        self.assertEqual(tuple(dimensions), resolver.SUFFICIENCY_DIMENSION_IDS)
        return {
            dimension_id: dimensions[dimension_id]["dimension_result"]
            for dimension_id in resolver.SUFFICIENCY_DIMENSION_IDS
        }

    def assert_required_non_claims_false(
        self, result: dict[str, object]
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(field, non_claims)
            self.assertIs(non_claims[field], False, field)
            self.assertIsInstance(non_claims[field], bool)

    def assert_required_basis_non_claims_false(
        self, records: dict[str, dict[str, object]]
    ) -> None:
        for dimension_id in resolver.SUFFICIENCY_DIMENSION_IDS:
            non_claims = records[dimension_id]["basis_non_claims"]
            self.assertIsInstance(non_claims, dict)
            self.assertEqual(
                set(non_claims), set(resolver.REQUIRED_BASIS_NON_CLAIMS)
            )
            for field in resolver.REQUIRED_BASIS_NON_CLAIMS:
                self.assertIs(non_claims[field], False, f"{dimension_id}.{field}")

    def assert_downstream_locks_false(self, result: dict[str, object]) -> None:
        operation = self.operation(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(operation[field], False, field)
        for field in (
            "receiver_attestation_created",
            "receiver_attestation_supported",
            "receiver_attestation_boundary_created",
            "receiver_answerable_receipt_present",
            "receiver_answerable_receipt_boundary_created",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_re_evaluation_boundary_created",
            "identity_created",
            "relation_created",
            "coupling_assigned",
            "coupling_created",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "public_interface_created",
            "public_intake_created",
            "authority_created",
            "standing_created",
            "truth_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(operation[field], False, field)

    def assert_completed_result_mutually_exclusive(
        self, result: dict[str, object], expected_true_field: str
    ) -> None:
        postures = self.candidate_result_postures(result)
        result_fields = (
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
        )
        self.assertEqual(
            [field for field in result_fields if postures[field] is True],
            [expected_true_field],
        )
        self.assertIs(postures["candidate_sufficiency_decided"], True)
        operation = self.operation(result)
        self.assertIs(operation["candidate_sufficiency_operation_recorded"], True)
        self.assertIs(
            operation["candidate_sufficiency_operation_result_recorded"], True
        )
        self.assertIs(operation["candidate_sufficiency_operation_exhausted"], True)

    def assert_no_partial_result_stands(self, result: dict[str, object]) -> None:
        postures = self.candidate_result_postures(result)
        self.assertTrue(all(value is False for value in postures.values()))
        operation = self.operation(result)
        self.assertIs(operation["candidate_sufficiency_operation_recorded"], False)
        self.assertIs(
            operation["candidate_sufficiency_operation_result_recorded"], False
        )
        self.assertIs(operation["candidate_sufficiency_operation_exhausted"], False)
        self.assertIs(operation["partial_evaluation_recorded"], False)
        self.assertTrue(
            all(
                value == resolver.DIMENSION_RESULT_NOT_EVALUATED
                for value in self.dimension_results(result).values()
            )
        )

    def assert_complete_material_omitted(
        self, result: dict[str, object]
    ) -> None:
        forbidden_keys = {
            "basis_items",
            "basis_references",
            "evaluator_reference",
            "candidate_material",
            "raw_candidate_material",
            "candidate_packet",
            "capture_material",
            "complete_capture_data",
            "raw_samples",
            "zip_bytes",
            "complete_boundary_artifact",
            "selected_boundary_artifact",
            "complete_upstream_checks",
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_checks",
            "receiver_side_answerable_basis_candidate_evaluation_operation_checks",
            "receiver_side_answerable_basis_candidate_evaluation_operation_basis",
        }

        def walk(value: object) -> None:
            if isinstance(value, dict):
                self.assertFalse(forbidden_keys.intersection(value), value.keys())
                for nested in value.values():
                    walk(nested)
            elif isinstance(value, list):
                for nested in value:
                    walk(nested)

        walk(result)
        upstream = result["upstream_basis"]
        self.assertIs(upstream["complete_boundary_artifact_omitted"], True)
        self.assertIs(upstream["complete_upstream_checks_omitted"], True)
        basis = result[
            "receiver_side_answerable_basis_candidate_sufficiency_operation_basis"
        ]
        self.assertIs(basis["complete_supplied_basis_omitted"], True)
        metadata = basis["dimension_basis_metadata"]
        if metadata:
            self.assertEqual(set(metadata), set(resolver.SUFFICIENCY_DIMENSION_IDS))
            expected_metadata_fields = {
                "dimension_id",
                "receiver_side_answerable_basis_candidate_id",
                "selected_candidate_sufficiency_boundary_id",
                "basis_items_count",
                "basis_references_count",
                "evaluator_reference_supplied",
                "support_key",
                "contradiction_key",
                "unresolved_key",
                "basis_non_claims_validated",
                "non_conversion_statement_validated",
                "complete_supplied_basis_omitted",
            }
            for dimension_id, entry in metadata.items():
                self.assertEqual(set(entry), expected_metadata_fields, dimension_id)
                self.assertIs(entry["complete_supplied_basis_omitted"], True)

    def assert_all_emitted_codes_public(
        self, result: dict[str, object]
    ) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for field in ("failure_code", "block_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_blocked(
        self, result: dict[str, object], expected_code: str | None = None
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_required_non_claims_false(result)
        self.assert_no_partial_result_stands(result)
        self.assert_downstream_locks_false(result)
        self.assert_complete_material_omitted(result)

    def assert_waiting(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_BASIS)
        self.assertEqual(
            self.operation_result(result), resolver.OPERATION_RESULT_REQUIRES_BASIS
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertEqual(
            result["block"],
            {
                "blocked": False,
                "code": None,
                "block_code": None,
                "reason": None,
            },
        )
        operation = self.operation(result)
        self.assertIs(operation["sufficiency_basis_supplied"], False)
        self.assertIs(operation["sufficiency_basis_complete"], False)
        self.assertIs(operation["atomic_sufficiency_basis_gate_passed"], False)
        self.assert_no_partial_result_stands(result)
        self.assert_required_non_claims_false(result)
        self.assert_downstream_locks_false(result)
        self.assert_complete_material_omitted(result)
        self.assertEqual(
            tuple(result["what_remains_open"]), resolver.WAITING_WHAT_REMAINS_OPEN
        )

    def assert_recorded(
        self,
        result: dict[str, object],
        operation_result: str,
        candidate_field: str,
    ) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.operation_result(result), operation_result)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(result["passed_check_count"], 0)
        self.assertIs(result["block"]["blocked"], False)
        operation = self.operation(result)
        self.assertIs(operation["sufficiency_basis_supplied"], True)
        self.assertIs(operation["sufficiency_basis_complete"], True)
        self.assertIs(operation["atomic_sufficiency_basis_gate_passed"], True)
        self.assert_completed_result_mutually_exclusive(result, candidate_field)
        self.assert_required_non_claims_false(result)
        self.assert_downstream_locks_false(result)
        self.assert_complete_material_omitted(result)

    def test_public_api_constants_and_static_contract(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
        )
        self.assertEqual(
            resolver.OPERATION_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_operation_001",
        )
        self.assertEqual(
            resolver.OPERATION_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION",
        )
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_"
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_boundary_001",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_RESULT_REQUIRED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
            "CONSIDERATION_ALLOWED",
        )
        self.assertEqual(
            resolver.CANDIDATE_ID, "receiver_side_answerable_basis_candidate_001"
        )
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "CANDIDATE_SUFFICIENCY_OPERATION_THEN_RECEIVER_ATTESTATION_BOUNDARY_"
            "ONLY_IF_CANDIDATE_SUFFICIENT",
        )
        expected_dimensions = (
            "receiver_answerability_fit",
            "selected_purpose_adequacy",
            "bounded_material_completeness",
            "unresolved_contradiction_posture",
            "unsupported_assumption_dependency",
            "scope_constrained_usability",
            "refusal_withholding_compatibility",
            "provenance_capture_limitation_posture",
        )
        self.assertEqual(resolver.SUFFICIENCY_DIMENSION_IDS, expected_dimensions)
        self.assertEqual(tuple(resolver.DIMENSION_LABELS), expected_dimensions)
        self.assertEqual(tuple(resolver.DIMENSION_RULE_KEYS), expected_dimensions)
        self.assertEqual(
            tuple(resolver.DIMENSION_NON_CONVERSION_STATEMENTS),
            expected_dimensions,
        )
        for dimension_id in expected_dimensions:
            self.assertEqual(
                set(resolver.DIMENSION_RULE_KEYS[dimension_id]),
                {"support", "contradiction", "unresolved"},
            )
            self.assertTrue(resolver.DIMENSION_LABELS[dimension_id])
            self.assertTrue(
                resolver.DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
            )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_REQUIRES_BASIS,
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_NOT_RECORDED,
            ),
        )
        self.assertEqual(
            resolver.OPERATION_RESULT_FAMILY,
            (
                resolver.OPERATION_RESULT_SUFFICIENT,
                resolver.OPERATION_RESULT_INSUFFICIENT,
                resolver.OPERATION_RESULT_INDETERMINATE,
                resolver.OPERATION_RESULT_REQUIRES_BASIS,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
        )
        self.assertEqual(
            resolver.DIMENSION_RESULT_FAMILY,
            (
                resolver.DIMENSION_RESULT_SATISFIED,
                resolver.DIMENSION_RESULT_NOT_SATISFIED,
                resolver.DIMENSION_RESULT_INDETERMINATE,
                resolver.DIMENSION_RESULT_NOT_EVALUATED,
            ),
        )
        self.assertEqual(
            resolver.SUPPORTED_INTENTS,
            (
                resolver.INTENT_RECORD,
                resolver.INTENT_DO_NOT_RECORD,
                resolver.INTENT_BLOCK,
            ),
        )
        self.assertEqual(
            resolver.OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
            "receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result.json",
        )

    def test_contract_nonclaims_prohibited_flags_and_public_codes(self) -> None:
        expected_basis_non_claims = (
            "caller_supplied_dimension_result",
            "caller_supplied_candidate_result",
            "evaluator_reference_to_authority",
            "evaluator_reference_to_identity",
            "evaluator_reference_to_standing",
            "evaluator_reference_to_truth",
            "basis_items_to_established_truth",
            "basis_references_to_verified_provenance",
            "candidate_sufficiency_to_receiver_attestation",
            "candidate_sufficiency_to_receiver_answerable_receipt",
            "candidate_sufficiency_to_presence_support",
            "candidate_sufficiency_to_downstream_authorization",
        )
        self.assertEqual(
            resolver.REQUIRED_BASIS_NON_CLAIMS, expected_basis_non_claims
        )
        required_locks = {
            "repeated_candidate_sufficiency_operation_permission_created",
            "reusable_candidate_sufficiency_operation_route_created",
            "same_candidate_sufficiency_operation_rerun_authorized",
            "automatic_candidate_sufficiency_operation_retry_created",
            "candidate_sufficiency_operation_debt_created",
            "candidate_sufficiency_operation_obligation_created",
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "identity_created",
            "relation_created",
            "coupling_created",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "authority_created",
            "standing_created",
            "truth_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        }
        self.assertTrue(
            required_locks.issubset(set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        )
        self.assertTrue(resolver.PROHIBITED_REQUEST_FLAGS)
        self.assertTrue(
            all(
                code in resolver.BLOCK_CODES
                for code in resolver.PROHIBITED_REQUEST_FLAGS.values()
            )
        )
        expected_public_codes = {
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "SUFFICIENCY_OPERATION_SPEC_REFERENCE_MISSING",
            "SUFFICIENCY_OPERATION_SPEC_MARKER_MISSING",
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            "UPSTREAM_BOUNDARY_NOT_ALLOWED",
            "UPSTREAM_BOUNDARY_RESULT_MISMATCH",
            "UPSTREAM_BOUNDARY_FAILED_CHECKS_PRESENT",
            "UPSTREAM_BOUNDARY_NOT_RECORDED",
            "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED",
            "UPSTREAM_CONSIDERATION_NOT_ALLOWED",
            "UPSTREAM_BOUNDARY_NOT_EXHAUSTED",
            "UPSTREAM_BOUNDARY_VALIDATION_INCOMPLETE",
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            "UPSTREAM_OPERATION_POSTURE_ALREADY_PRESENT",
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT",
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
            "SUFFICIENCY_BASIS_NOT_MAPPING",
            "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH",
            "SUFFICIENCY_BASIS_RECORD_NOT_MAPPING",
            "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH",
            "SUFFICIENCY_BASIS_ITEMS_INVALID",
            "SUFFICIENCY_BASIS_REFERENCES_INVALID",
            "SUFFICIENCY_BASIS_EVALUATOR_REFERENCE_INVALID",
            "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID",
            "SUFFICIENCY_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            "SUFFICIENCY_BASIS_NON_CONVERSION_STATEMENT_MISMATCH",
            "SUFFICIENCY_BASIS_RESULT_PRECLAIMED",
            "RESULT_POSTURE_PRECLAIMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        }
        self.assertTrue(expected_public_codes.issubset(resolver.BLOCK_CODES))

    def test_default_live_and_synthetic_waiting_results(self) -> None:
        if not GOVERNING_SPEC_PATH.is_file() or not LIVE_BOUNDARY_ARTIFACT_PATH.is_file():
            self.skipTest(
                "exact governing specification or selected boundary artifact unavailable"
            )
        before_spec = GOVERNING_SPEC_PATH.read_bytes()
        before_artifact = LIVE_BOUNDARY_ARTIFACT_PATH.read_bytes()
        live = self.invoke()
        self.assert_waiting(live)
        self.assertEqual(live["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(live["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(GOVERNING_SPEC_PATH.read_bytes(), before_spec)
        self.assertEqual(LIVE_BOUNDARY_ARTIFACT_PATH.read_bytes(), before_artifact)

        synthetic = self.resolve_synthetic(self.canonical_waiting_request())
        self.assert_waiting(synthetic)
        basis = synthetic[
            "receiver_side_answerable_basis_candidate_sufficiency_operation_basis"
        ]
        self.assertIs(basis["sufficiency_basis_supplied"], False)
        self.assertIs(basis["sufficiency_basis_complete"], False)
        self.assertIs(basis["atomic_sufficiency_basis_gate_passed"], False)

    def test_supported_basis_derives_candidate_sufficient(self) -> None:
        records = self.valid_sufficiency_basis_records()
        records_before = self.clone(records)
        self.assert_required_basis_non_claims_false(records)
        result = self.resolve_synthetic(self.request_with_records(records))
        self.assertEqual(records, records_before)
        self.assert_recorded(
            result,
            resolver.OPERATION_RESULT_SUFFICIENT,
            "receiver_side_answerable_basis_candidate_sufficient",
        )
        dimensions = result[
            "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
        ]
        self.assertTrue(
            all(
                entry["dimension_result"] == resolver.DIMENSION_RESULT_SATISFIED
                and entry["dimension_evaluated"] is True
                and entry["dimension_established"] is True
                and entry["basis_referenced"] is True
                and entry["result_derived_from_rule_inputs"] is True
                for entry in dimensions.values()
            )
        )
        self.assertEqual(
            tuple(result["what_remains_open"]),
            resolver.SUFFICIENT_WHAT_REMAINS_OPEN,
        )
        self.assertIn(
            "receiver-attestation boundary, if separately selected",
            result["what_remains_open"],
        )
        self.assertNotIn("receiver attestation", result["what_remains_open"])

    def test_contradiction_and_missing_support_derive_insufficient(self) -> None:
        dimension_id = resolver.SUFFICIENCY_DIMENSION_IDS[0]
        for label, request in (
            ("contradiction", self.insufficient_request()),
            ("missing_support", self.insufficient_request(missing_support=True)),
        ):
            with self.subTest(case=label):
                result = self.resolve_synthetic(request)
                self.assert_recorded(
                    result,
                    resolver.OPERATION_RESULT_INSUFFICIENT,
                    "receiver_side_answerable_basis_candidate_insufficient",
                )
                self.assertEqual(
                    self.dimension_results(result)[dimension_id],
                    resolver.DIMENSION_RESULT_NOT_SATISFIED,
                )
                self.assertIs(
                    self.operation(result)["candidate_insufficiency_established"],
                    True,
                )
                self.assertEqual(
                    tuple(result["what_remains_open"]),
                    resolver.NON_SUFFICIENT_WHAT_REMAINS_OPEN,
                )
                serialized = json.dumps(result, sort_keys=True)
                for forbidden_posture in (
                    "candidate_deleted",
                    "candidate_erased",
                    "candidate_invalidated",
                    "candidate_rejected",
                    "candidate_repaired",
                ):
                    self.assertNotIn(forbidden_posture, serialized)
                self.assertNotIn(
                    "receiver-attestation boundary, if separately selected",
                    result["what_remains_open"],
                )
                self.assertTrue(
                    result[
                        "receiver_side_answerable_basis_candidate_sufficiency_operation_non_meaning"
                    ]["candidate_insufficient_is_not_candidate_existence_rejection"]
                )

    def test_unresolved_derives_indeterminate_without_retry(self) -> None:
        dimension_id = resolver.SUFFICIENCY_DIMENSION_IDS[0]
        result = self.resolve_synthetic(self.indeterminate_request())
        self.assert_recorded(
            result,
            resolver.OPERATION_RESULT_INDETERMINATE,
            "receiver_side_answerable_basis_candidate_indeterminate",
        )
        self.assertEqual(
            self.dimension_results(result)[dimension_id],
            resolver.DIMENSION_RESULT_INDETERMINATE,
        )
        self.assertIs(
            self.operation(result)["candidate_indeterminacy_established"], True
        )
        self.assertIs(
            self.operation(result)[
                "automatic_candidate_sufficiency_operation_retry_created"
            ],
            False,
        )
        self.assertEqual(
            tuple(result["what_remains_open"]),
            resolver.NON_SUFFICIENT_WHAT_REMAINS_OPEN,
        )
        self.assertTrue(
            result[
                "receiver_side_answerable_basis_candidate_sufficiency_operation_non_meaning"
            ]["candidate_indeterminate_is_not_candidate_insufficiency"]
        )

    def test_candidate_result_precedence_is_exact(self) -> None:
        first, second = resolver.SUFFICIENCY_DIMENSION_IDS[:2]
        records = self.set_dimension_posture(
            self.valid_sufficiency_basis_records(), first, contradiction=True
        )
        records = self.set_dimension_posture(records, second, unresolved=True)
        result = self.resolve_synthetic(self.request_with_records(records))
        self.assert_recorded(
            result,
            resolver.OPERATION_RESULT_INDETERMINATE,
            "receiver_side_answerable_basis_candidate_indeterminate",
        )
        self.assertEqual(
            self.dimension_results(result)[first],
            resolver.DIMENSION_RESULT_NOT_SATISFIED,
        )
        self.assertEqual(
            self.dimension_results(result)[second],
            resolver.DIMENSION_RESULT_INDETERMINATE,
        )

        one_not_satisfied = self.resolve_synthetic(self.insufficient_request())
        self.assertEqual(
            self.operation_result(one_not_satisfied),
            resolver.OPERATION_RESULT_INSUFFICIENT,
        )
        all_satisfied = self.resolve_synthetic(self.sufficient_request())
        self.assertEqual(
            self.operation_result(all_satisfied),
            resolver.OPERATION_RESULT_SUFFICIENT,
        )
        self.assertTrue(
            all(
                value == resolver.DIMENSION_RESULT_SATISFIED
                for value in self.dimension_results(all_satisfied).values()
            )
        )

    def test_exact_eight_record_atomic_gate_and_malformed_basis(self) -> None:
        dimension_id = resolver.SUFFICIENCY_DIMENSION_IDS[0]
        keys = resolver.DIMENSION_RULE_KEYS[dimension_id]

        def mutate_records(label: str) -> object:
            records: object = self.valid_sufficiency_basis_records()
            if label == "missing_records":
                records.pop(dimension_id)
            elif label == "extra_dimension":
                records["unknown_dimension"] = self.clone(records[dimension_id])
            elif label == "wrong_enclosing_key":
                records["wrong_dimension"] = records.pop(dimension_id)
            elif label == "mismatched_dimension_id":
                records[dimension_id]["dimension_id"] = "other"
            elif label == "record_not_mapping":
                records[dimension_id] = []
            elif label == "wrong_candidate_id":
                records[dimension_id][
                    "receiver_side_answerable_basis_candidate_id"
                ] = "other"
            elif label == "wrong_boundary_id":
                records[dimension_id][
                    "selected_candidate_sufficiency_boundary_id"
                ] = "other"
            elif label == "empty_basis_items":
                records[dimension_id]["basis_items"] = []
            elif label == "basis_items_not_sequence":
                records[dimension_id]["basis_items"] = "not-a-sequence"
            elif label == "invalid_basis_item":
                records[dimension_id]["basis_items"] = ["not-a-mapping"]
            elif label == "excessive_basis_items":
                records[dimension_id]["basis_items"] = [
                    {"index": index}
                    for index in range(resolver.MAX_SEQUENCE_ITEMS + 1)
                ]
            elif label == "excessive_text":
                records[dimension_id]["basis_items"] = [
                    {"text": "x" * (resolver.MAX_TEXT_LENGTH + 1)}
                ]
            elif label == "empty_basis_references":
                records[dimension_id]["basis_references"] = []
            elif label == "invalid_basis_reference":
                records[dimension_id]["basis_references"] = [None]
            elif label == "invalid_evaluator_reference":
                records[dimension_id]["evaluator_reference"] = ""
            elif label == "missing_support_map":
                records[dimension_id].pop("support_postures")
            elif label == "extra_support_key":
                records[dimension_id]["support_postures"]["extra"] = False
            elif label == "non_boolean_support":
                records[dimension_id]["support_postures"][keys["support"]] = 1
            elif label == "missing_contradiction_map":
                records[dimension_id].pop("contradiction_postures")
            elif label == "extra_contradiction_key":
                records[dimension_id]["contradiction_postures"]["extra"] = False
            elif label == "non_boolean_contradiction":
                records[dimension_id]["contradiction_postures"][
                    keys["contradiction"]
                ] = "false"
            elif label == "missing_unresolved_map":
                records[dimension_id].pop("unresolved_postures")
            elif label == "extra_unresolved_key":
                records[dimension_id]["unresolved_postures"]["extra"] = False
            elif label == "non_boolean_unresolved":
                records[dimension_id]["unresolved_postures"][
                    keys["unresolved"]
                ] = None
            elif label == "missing_basis_nonclaim":
                records[dimension_id]["basis_non_claims"].pop(
                    resolver.REQUIRED_BASIS_NON_CLAIMS[0]
                )
            elif label == "flipped_basis_nonclaim":
                records[dimension_id]["basis_non_claims"][
                    resolver.REQUIRED_BASIS_NON_CLAIMS[0]
                ] = True
            elif label == "wrong_non_conversion":
                records[dimension_id]["non_conversion_statement"] = "other"
            elif label == "caller_dimension_result":
                records[dimension_id]["dimension_result"] = (
                    resolver.DIMENSION_RESULT_SATISFIED
                )
            elif label == "caller_candidate_result":
                records[dimension_id]["candidate_result"] = (
                    resolver.OPERATION_RESULT_SUFFICIENT
                )
            elif label == "operation_result_preclaim":
                records[dimension_id]["operation_result"] = (
                    resolver.OPERATION_RESULT_SUFFICIENT
                )
            elif label == "receiver_preclaim":
                records[dimension_id]["receiver_attestation_created"] = True
            elif label == "receipt_preclaim":
                records[dimension_id]["receiver_answerable_receipt_present"] = True
            elif label == "presence_preclaim":
                records[dimension_id]["presence_supported"] = True
            elif label == "downstream_preclaim":
                records[dimension_id]["authority_created"] = True
            return records

        cases = (
            ("records_not_mapping", "SUFFICIENCY_BASIS_NOT_MAPPING"),
            ("missing_records", "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH"),
            ("extra_dimension", "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH"),
            ("wrong_enclosing_key", "SUFFICIENCY_BASIS_DIMENSION_SET_MISMATCH"),
            ("mismatched_dimension_id", "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH"),
            ("record_not_mapping", "SUFFICIENCY_BASIS_RECORD_NOT_MAPPING"),
            ("wrong_candidate_id", "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH"),
            ("wrong_boundary_id", "SUFFICIENCY_BASIS_RECORD_IDENTITY_MISMATCH"),
            ("empty_basis_items", "SUFFICIENCY_BASIS_ITEMS_INVALID"),
            ("basis_items_not_sequence", "SUFFICIENCY_BASIS_ITEMS_INVALID"),
            ("invalid_basis_item", "SUFFICIENCY_BASIS_ITEMS_INVALID"),
            ("excessive_basis_items", "SUFFICIENCY_BASIS_ITEMS_INVALID"),
            ("excessive_text", "SUFFICIENCY_BASIS_ITEMS_INVALID"),
            ("empty_basis_references", "SUFFICIENCY_BASIS_REFERENCES_INVALID"),
            ("invalid_basis_reference", "SUFFICIENCY_BASIS_REFERENCES_INVALID"),
            (
                "invalid_evaluator_reference",
                "SUFFICIENCY_BASIS_EVALUATOR_REFERENCE_INVALID",
            ),
            ("missing_support_map", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("extra_support_key", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("non_boolean_support", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("missing_contradiction_map", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("extra_contradiction_key", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("non_boolean_contradiction", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("missing_unresolved_map", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("extra_unresolved_key", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            ("non_boolean_unresolved", "SUFFICIENCY_BASIS_RULE_INPUTS_INVALID"),
            (
                "missing_basis_nonclaim",
                "SUFFICIENCY_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "flipped_basis_nonclaim",
                "SUFFICIENCY_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "wrong_non_conversion",
                "SUFFICIENCY_BASIS_NON_CONVERSION_STATEMENT_MISMATCH",
            ),
            ("caller_dimension_result", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("caller_candidate_result", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("operation_result_preclaim", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("receiver_preclaim", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("receipt_preclaim", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("presence_preclaim", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
            ("downstream_preclaim", "SUFFICIENCY_BASIS_RESULT_PRECLAIMED"),
        )
        for label, expected_code in cases:
            with self.subTest(case=label):
                if label == "records_not_mapping":
                    request = self.canonical_waiting_request(
                        sufficiency_basis_supplied=True,
                        sufficiency_basis_records=[],
                    )
                else:
                    request = self.request_with_records(mutate_records(label))
                self.assert_blocked(
                    self.resolve_synthetic(request), expected_code
                )

        self.assert_waiting(
            self.resolve_synthetic(self.canonical_waiting_request())
        )

    def test_upstream_boundary_validation_matrix(self) -> None:
        boundary_fields = {
            "wrong_boundary_id": ("boundary_id", "other", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_boundary_type": ("boundary_type", "other", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_boundary_version": ("boundary_version", "0.0.0", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_boundary_scope": ("boundary_scope", "other", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_candidate_id": ("receiver_side_answerable_basis_candidate_id", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_candidate_type": ("receiver_side_answerable_basis_candidate_type", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_candidate_scope": ("receiver_side_answerable_basis_candidate_scope", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_reception_id": ("selected_candidate_reception_operation_id", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_evaluation_boundary_id": ("selected_candidate_evaluation_boundary_id", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_evaluation_operation_id": ("selected_candidate_evaluation_operation_id", "other", "SELECTED_CANDIDATE_IDENTITY_MISMATCH"),
            "wrong_boundary_result": ("candidate_sufficiency_boundary_result", "other", "UPSTREAM_BOUNDARY_RESULT_MISMATCH"),
            "boundary_not_recorded": ("candidate_sufficiency_boundary_recorded", False, "UPSTREAM_BOUNDARY_NOT_RECORDED"),
            "boundary_result_not_recorded": ("candidate_sufficiency_boundary_result_recorded", False, "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED"),
            "consideration_not_allowed": ("candidate_sufficiency_consideration_allowed", False, "UPSTREAM_CONSIDERATION_NOT_ALLOWED"),
            "boundary_not_exhausted": ("candidate_sufficiency_boundary_exhausted", False, "UPSTREAM_BOUNDARY_NOT_EXHAUSTED"),
            "alias_boundary_not_recorded": ("receiver_side_answerable_basis_candidate_sufficiency_boundary_recorded", False, "UPSTREAM_BOUNDARY_NOT_RECORDED"),
            "alias_result_not_recorded": ("receiver_side_answerable_basis_candidate_sufficiency_boundary_result_recorded", False, "UPSTREAM_BOUNDARY_RESULT_NOT_RECORDED"),
            "candidate_result_present": ("receiver_side_answerable_basis_candidate_sufficient", True, "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT"),
            "operation_posture_present": ("candidate_sufficiency_operation_created", True, "UPSTREAM_OPERATION_POSTURE_ALREADY_PRESENT"),
            "attestation_present": ("receiver_attestation_created", True, "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT"),
            "receipt_present": ("receiver_answerable_receipt_present", True, "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT"),
            "presence_present": ("presence_supported", True, "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT"),
            "rerun_present": ("same_candidate_sufficiency_boundary_rerun_authorized", True, "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT"),
            "retry_present": ("automatic_candidate_sufficiency_boundary_retry_created", True, "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT"),
            "debt_present": ("candidate_sufficiency_boundary_debt_created", True, "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT"),
            "obligation_present": ("candidate_sufficiency_boundary_obligation_created", True, "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT"),
            "follow_on_present": ("follow_on_work_authorized", True, "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_FOLLOW_ON_PRESENT"),
        }
        top_level_cases = {
            "wrong_resolver": ("resolver_module", "other", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_result_version": ("result_version", "0.0.0", "SELECTED_BOUNDARY_IDENTITY_MISMATCH"),
            "wrong_outcome": ("outcome", "other", "UPSTREAM_BOUNDARY_NOT_ALLOWED"),
            "failed_checks": ("failed_check_count", 1, "UPSTREAM_BOUNDARY_FAILED_CHECKS_PRESENT"),
        }
        for label, (field, value, code) in top_level_cases.items():
            with self.subTest(case=label):
                artifact = self.synthetic_valid_boundary_artifact()
                artifact[field] = value
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_waiting_request(),
                        boundary_artifact=artifact,
                    ),
                    code,
                )
        for label, (field, value, code) in boundary_fields.items():
            with self.subTest(case=label):
                artifact = self.synthetic_valid_boundary_artifact()
                artifact[
                    "receiver_side_answerable_basis_candidate_sufficiency_boundary"
                ][field] = value
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_waiting_request(),
                        boundary_artifact=artifact,
                    ),
                    code,
                )
        for summary_field in (
            "atomic_gate_validated",
            "eight_dimensions_validated",
            "candidate_aggregate_validated",
            "exhaustion_validated",
            "current_false_posture_validated",
            "candidate_results_false",
            "receiver_receipt_presence_downstream_false",
            "repeated_reusable_rerun_false",
        ):
            with self.subTest(summary_field=summary_field):
                artifact = self.synthetic_valid_boundary_artifact()
                artifact[
                    "receiver_side_answerable_basis_candidate_sufficiency_boundary_summary"
                ][summary_field] = False
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_waiting_request(),
                        boundary_artifact=artifact,
                    ),
                    "UPSTREAM_BOUNDARY_VALIDATION_INCOMPLETE",
                )
        artifact = self.synthetic_valid_boundary_artifact()
        artifact["what_remains_open"] = list(
            resolver.EXPECTED_UPSTREAM_WHAT_REMAINS_OPEN[1:]
        )
        self.assert_blocked(
            self.resolve_synthetic(
                self.canonical_waiting_request(), boundary_artifact=artifact
            ),
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        )

    def test_request_validation_and_top_level_preclaims(self) -> None:
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min(
                []
            ),
            "REQUEST_NOT_MAPPING",
        )
        request_cases = (
            ("intent", "UNSUPPORTED", "UNSUPPORTED_INTENT"),
            ("operation_id", "other", "SELECTED_OPERATION_IDENTITY_MISMATCH"),
            ("operation_type", "other", "SELECTED_OPERATION_IDENTITY_MISMATCH"),
            ("operation_version", "0.0.0", "SELECTED_OPERATION_IDENTITY_MISMATCH"),
            ("operation_scope", "other", "SELECTED_OPERATION_IDENTITY_MISMATCH"),
            (
                "receiver_side_answerable_basis_candidate_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_evaluation_operation_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_sufficiency_boundary_id",
                "other",
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "governing_sufficiency_operation_specification_path",
                "other",
                "REQUEST_VALUE_MISMATCH",
            ),
            (
                "selected_sufficiency_boundary_artifact_path",
                "other",
                "REQUEST_VALUE_MISMATCH",
            ),
            ("admissible_future_route", "other", "REQUEST_VALUE_MISMATCH"),
            ("sufficiency_basis_supplied", "true", "REQUEST_VALUE_MISMATCH"),
        )
        for field, value, expected_code in request_cases:
            with self.subTest(field=field):
                request = self.canonical_waiting_request(**{field: value})
                self.assert_blocked(
                    self.resolve_synthetic(request), expected_code
                )
        inconsistent = self.canonical_waiting_request()
        inconsistent["sufficiency_basis_records"] = (
            self.valid_sufficiency_basis_records()
        )
        self.assert_blocked(
            self.resolve_synthetic(inconsistent), "REQUEST_VALUE_MISMATCH"
        )
        for field, value in (
            ("outcome", resolver.OUTCOME_RECORDED),
            ("operation_result", resolver.OPERATION_RESULT_SUFFICIENT),
            (
                "candidate_sufficiency_operation_result",
                resolver.OPERATION_RESULT_SUFFICIENT,
            ),
            ("candidate_sufficiency_operation_recorded", True),
            ("candidate_sufficiency_operation_result_recorded", True),
            ("candidate_sufficiency_operation_exhausted", True),
            ("receiver_side_answerable_basis_candidate_sufficient", True),
            ("receiver_side_answerable_basis_candidate_insufficient", True),
            ("receiver_side_answerable_basis_candidate_indeterminate", True),
            ("candidate_sufficiency_decided", True),
            ("candidate_sufficiency_established", True),
            ("candidate_insufficiency_established", True),
            ("candidate_indeterminacy_established", True),
            ("dimension_results", {}),
            ("selected_boundary_artifact", {}),
            ("complete_boundary_artifact", {}),
        ):
            with self.subTest(preclaim=field):
                request = self.canonical_waiting_request(**{field: value})
                self.assert_blocked(
                    self.resolve_synthetic(request), "RESULT_POSTURE_PRECLAIMED"
                )
        for field in (
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "identity_created",
            "authority_created",
            "standing_created",
            "truth_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_work_authorized",
        ):
            with self.subTest(unknown_result_preclaim=field):
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_waiting_request(**{field: True})
                    ),
                    "REQUEST_VALUE_MISMATCH",
                )

    def test_declared_nonclaims_canonicalization(self) -> None:
        canonical = self.canonical_waiting_request()
        self.assertEqual(
            set(canonical["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                canonical["declared_non_claims"][field] is False
                for field in resolver.REQUIRED_FALSE_NON_CLAIMS
            )
        )
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped=field):
                request = self.canonical_waiting_request()
                request["declared_non_claims"][field] = True
                result = self.resolve_synthetic(request)
                self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assertIs(result["non_claims"][field], False)
        first = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        malformed_values: list[object] = [
            {
                field: False
                for field in resolver.REQUIRED_FALSE_NON_CLAIMS
                if field != first
            },
            None,
            0,
            "false",
        ]
        for value in malformed_values:
            with self.subTest(malformed=repr(value)):
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_waiting_request(
                            declared_non_claims=value
                        )
                    ),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )

    def test_every_prohibited_request_flag_blocks_without_leakage(self) -> None:
        for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
            with self.subTest(flag=field):
                request = self.canonical_waiting_request(**{field: True})
                result = self.resolve_synthetic(request)
                self.assert_blocked(result, expected_code)

    def test_do_not_record_and_explicit_block(self) -> None:
        not_recorded = self.invoke(
            self.canonical_waiting_request(intent=resolver.INTENT_DO_NOT_RECORD)
        )
        self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertEqual(
            self.operation_result(not_recorded),
            resolver.OPERATION_RESULT_NOT_EVALUATED,
        )
        self.assertEqual(self.failed_check_count(not_recorded), 0)
        self.assert_no_partial_result_stands(not_recorded)
        self.assert_required_non_claims_false(not_recorded)
        self.assert_downstream_locks_false(not_recorded)
        self.assertEqual(
            tuple(not_recorded["what_remains_open"]),
            resolver.INCOMPLETE_BRANCH_WHAT_REMAINS_OPEN,
        )
        blocked = self.invoke(
            self.canonical_waiting_request(intent=resolver.INTENT_BLOCK)
        )
        self.assert_blocked(blocked, "EXPLICIT_BLOCK_REQUESTED")

    def test_result_structure_bounded_basis_and_official_values(self) -> None:
        records = self.valid_sufficiency_basis_records()
        sentinels = (
            "COMPLETE_BASIS_ITEM_MUST_NOT_RETURN",
            "COMPLETE_BASIS_REFERENCE_MUST_NOT_RETURN",
            "EVALUATOR_REFERENCE_CONTENT_MUST_NOT_RETURN",
        )
        first = resolver.SUFFICIENCY_DIMENSION_IDS[0]
        records[first]["basis_items"][0]["sentinel"] = sentinels[0]
        records[first]["basis_references"][0]["sentinel"] = sentinels[1]
        records[first]["evaluator_reference"]["sentinel"] = sentinels[2]
        result = self.resolve_synthetic(self.request_with_records(records))
        self.assert_recorded(
            result,
            resolver.OPERATION_RESULT_SUFFICIENT,
            "receiver_side_answerable_basis_candidate_sufficient",
        )
        self.assertEqual(set(result), set(resolver.RESULT_SECTIONS))
        operation = self.operation(result)
        for wrapper_field in (
            "outcome",
            "block",
            "non_claims",
            "receiver_side_answerable_basis_candidate_sufficiency_operation_checks",
            "receiver_side_answerable_basis_candidate_sufficiency_operation_summary",
            "receiver_side_answerable_basis_candidate_sufficiency_operation_metadata",
        ):
            self.assertNotIn(wrapper_field, operation)
        self.assertEqual(operation["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(operation["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(operation["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(operation["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertEqual(
            operation["receiver_side_answerable_basis_candidate_id"],
            resolver.CANDIDATE_ID,
        )
        self.assertEqual(
            operation["selected_candidate_sufficiency_boundary_id"],
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
        )
        serialized = json.dumps(result, sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)
        for official in (
            resolver.OPERATION_ID,
            resolver.OPERATION_TYPE,
            resolver.CANDIDATE_ID,
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
            resolver.OPERATION_RESULT_SUFFICIENT,
            resolver.RESOLVER_MODULE,
        ):
            self.assertIn(official, serialized)

    def test_branch_relative_open_state_and_summary_behavior(self) -> None:
        results = (
            (
                self.resolve_synthetic(self.canonical_waiting_request()),
                resolver.WAITING_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(self.sufficient_request()),
                resolver.SUFFICIENT_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(self.insufficient_request()),
                resolver.NON_SUFFICIENT_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(self.indeterminate_request()),
                resolver.NON_SUFFICIENT_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(
                    self.canonical_waiting_request(intent=resolver.INTENT_BLOCK)
                ),
                resolver.INCOMPLETE_BRANCH_WHAT_REMAINS_OPEN,
            ),
            (
                self.invoke(
                    self.canonical_waiting_request(
                        intent=resolver.INTENT_DO_NOT_RECORD
                    )
                ),
                resolver.INCOMPLETE_BRANCH_WHAT_REMAINS_OPEN,
            ),
        )
        completed_work = (
            "separately supplied eight-dimension candidate-sufficiency basis",
            "actual candidate-sufficiency evaluation",
            "candidate-sufficiency result",
            "candidate-sufficiency operation admission",
            "candidate-sufficiency operation exhaustion",
            "automatic retry",
            "operation rerun",
        )
        for result, expected_open in results:
            with self.subTest(outcome=result["outcome"]):
                self.assertEqual(tuple(result["what_remains_open"]), expected_open)
                summary = (
                    resolver.build_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(
                    summary,
                    result[
                        "receiver_side_answerable_basis_candidate_sufficiency_operation_summary"
                    ],
                )
                for field in (
                    "outcome",
                    "operation_result",
                    "failed_check_count",
                    "passed_check_count",
                    "resolver_module",
                    "result_version",
                    "operation_id",
                    "operation_type",
                    "operation_version",
                    "operation_scope",
                    "selected_candidate_id",
                    "selected_boundary_id",
                    "upstream_boundary_validated",
                    "atomic_sufficiency_basis_gate_passed",
                    "dimension_results",
                    "candidate_result_postures",
                    "candidate_sufficiency_operation_exhausted",
                    "governing_paths",
                    "marker_validation",
                    "complete_supplied_basis_omitted",
                    "complete_boundary_artifact_omitted",
                ):
                    self.assertIn(field, summary)
                if result["outcome"] == resolver.OUTCOME_RECORDED:
                    for item in completed_work:
                        self.assertNotIn(item, result["what_remains_open"])

    def test_specification_and_boundary_file_failure_modes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request = self.canonical_waiting_request()
            self.assert_blocked(
                self.invoke(request, root),
                "SUFFICIENCY_OPERATION_SPEC_REFERENCE_MISSING",
            )
            self.fixture_root(root, specification="missing required markers\n")
            self.assert_blocked(
                self.invoke(request, root),
                "SUFFICIENCY_OPERATION_SPEC_MARKER_MISSING",
            )
            self._write_text(
                root
                / resolver.GOVERNING_SUFFICIENCY_OPERATION_SPECIFICATION_RELATIVE_PATH,
                self.synthetic_governing_operation_specification(),
            )
            boundary_path = (
                root / resolver.SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH
            )
            boundary_path.unlink()
            self.assert_blocked(
                self.invoke(request, root),
                "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            )
            self._write_text(boundary_path, "{")
            self.assert_blocked(
                self.invoke(request, root),
                "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            )
            self._write_json(boundary_path, [])
            self.assert_blocked(
                self.invoke(request, root),
                "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )
            self._write_json(boundary_path, {})
            self.assert_blocked(
                self.invoke(request, root),
                "SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )

    def test_from_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            waiting_path = self._write_json(
                root / "requests" / "waiting.json",
                self.canonical_waiting_request(),
            )
            sufficient_path = self._write_json(
                root / "requests" / "sufficient.json",
                self.sufficient_request(),
            )
            with patch.object(resolver, "REPO_ROOT", root):
                waiting = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_from_path(
                        waiting_path
                    )
                )
                sufficient = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_from_path(
                        sufficient_path
                    )
                )
            self.assert_waiting(waiting)
            self.assert_recorded(
                sufficient,
                resolver.OPERATION_RESULT_SUFFICIENT,
                "receiver_side_answerable_basis_candidate_sufficient",
            )
            malformed = self._write_text(root / "requests" / "malformed.json", "{")
            array = self._write_json(root / "requests" / "array.json", [])
            for path in (malformed, array, root / "requests" / "missing.json"):
                with self.subTest(path=path.name):
                    with patch.object(resolver, "REPO_ROOT", root):
                        result = (
                            resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_from_path(
                                path
                            )
                        )
                    self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_write_behavior_and_validation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="bounded_operation_output_") as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            waiting = self.invoke(self.canonical_waiting_request(), root)
            sufficient = self.invoke(self.sufficient_request(), root)
            insufficient = self.invoke(self.insufficient_request(), root)
            indeterminate = self.invoke(self.indeterminate_request(), root)
            blocked = self.invoke(
                self.canonical_waiting_request(intent=resolver.INTENT_BLOCK), root
            )
            not_recorded = self.invoke(
                self.canonical_waiting_request(intent=resolver.INTENT_DO_NOT_RECORD),
                root,
            )
            output_root = root / "operation_outputs"
            result_by_name = {
                "waiting": waiting,
                "sufficient": sufficient,
                "insufficient": insufficient,
                "indeterminate": indeterminate,
                "blocked": blocked,
                "not_recorded": not_recorded,
            }
            written: dict[str, Path] = {}
            for name, result in result_by_name.items():
                with self.subTest(write=name):
                    path = self.safe_temporary_output_path(output_root, name)
                    written[name] = (
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
                            result, path
                        )
                    )
                    self.assertTrue(written[name].is_file())
                    parsed = json.loads(
                        written[name].read_text(encoding="utf-8")
                    )
                    self.assertEqual(parsed["resolver_module"], resolver.RESOLVER_MODULE)
                    self.assertEqual(parsed["result_version"], resolver.RESULT_VERSION)
                    self.assertEqual(parsed["outcome"], result["outcome"])
                    self.assertEqual(
                        self.operation_result(parsed), self.operation_result(result)
                    )
                    self.assert_required_non_claims_false(parsed)
                    self.assert_complete_material_omitted(parsed)
            first = self.safe_temporary_output_path(output_root, "sufficient")
            suffixed = (
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
                    sufficient, first
                )
            )
            self.assertEqual(suffixed.name, first.stem + "_001" + first.suffix)

            default_root = root / "default_operation_output"
            with patch.object(resolver, "OUTPUT_ROOT", default_root):
                default_path = (
                    resolver.write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
                        waiting
                    )
                )
            self.assertEqual(default_path.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(default_path.parent, default_root)

            for forbidden_fragment in (
                "spec",
                "tests",
                "reference",
                "evaluation_operation",
                "sufficiency_boundary",
                "presence",
                "runtime",
                "api",
            ):
                with self.subTest(forbidden=forbidden_fragment):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
                            sufficient,
                            root / forbidden_fragment / resolver.OUTPUT_FILENAME,
                        )

            malformed_results: list[tuple[str, object]] = []
            malformed_results.append(("not_mapping", []))
            wrong_module = self.clone(sufficient)
            wrong_module["resolver_module"] = "other"
            malformed_results.append(("wrong_module", wrong_module))
            wrong_version = self.clone(sufficient)
            wrong_version["result_version"] = "0.0.0"
            malformed_results.append(("wrong_version", wrong_version))
            wrong_outcome = self.clone(sufficient)
            wrong_outcome["outcome"] = "other"
            malformed_results.append(("wrong_outcome", wrong_outcome))
            missing_section = self.clone(sufficient)
            missing_section.pop("operation_result_detail")
            malformed_results.append(("missing_section", missing_section))
            branch_mismatch = self.clone(sufficient)
            branch_mismatch["outcome"] = resolver.OUTCOME_REQUIRES_BASIS
            malformed_results.append(("branch_mismatch", branch_mismatch))
            multiple_postures = self.clone(sufficient)
            multiple_postures[
                "receiver_side_answerable_basis_candidate_sufficiency_operation"
            ]["receiver_side_answerable_basis_candidate_insufficient"] = True
            malformed_results.append(("multiple_postures", multiple_postures))
            exhaustion_mismatch = self.clone(sufficient)
            exhaustion_mismatch[
                "receiver_side_answerable_basis_candidate_sufficiency_operation"
            ]["candidate_sufficiency_operation_exhausted"] = False
            malformed_results.append(("exhaustion_mismatch", exhaustion_mismatch))
            flipped_nonclaim = self.clone(sufficient)
            flipped_nonclaim["non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ] = True
            malformed_results.append(("flipped_nonclaim", flipped_nonclaim))
            complete_basis = self.clone(sufficient)
            complete_basis[
                "declared_receiver_side_answerable_basis_candidate_sufficiency_operation_basis"
            ]["basis_items"] = [{"forbidden": True}]
            malformed_results.append(("complete_basis", complete_basis))
            complete_boundary = self.clone(sufficient)
            complete_boundary["upstream_basis"]["complete_boundary_artifact"] = {
                "forbidden": True
            }
            malformed_results.append(("complete_boundary", complete_boundary))
            for name, malformed_result in malformed_results:
                with self.subTest(refused=name):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisCandidateSufficiencyOperationV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result(
                            malformed_result,
                            self.safe_temporary_output_path(
                                output_root, "refused_" + name
                            ),
                        )

    def test_non_mutation_and_lineage_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            specification = self.synthetic_governing_operation_specification()
            artifact = self.synthetic_valid_boundary_artifact()
            records = self.valid_sufficiency_basis_records()
            request = self.request_with_records(records)
            specification_before = specification
            artifact_before = self.clone(artifact)
            records_before = self.clone(records)
            request_before = self.clone(request)
            self.fixture_root(
                root,
                specification=specification,
                boundary_artifact=artifact,
            )
            result = self.invoke(request, root)
            self.assert_recorded(
                result,
                resolver.OPERATION_RESULT_SUFFICIENT,
                "receiver_side_answerable_basis_candidate_sufficient",
            )
            self.assertEqual(specification, specification_before)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(records, records_before)
            self.assertEqual(request, request_before)
            on_disk_artifact = json.loads(
                (
                    root
                    / resolver.SELECTED_SUFFICIENCY_BOUNDARY_ARTIFACT_RELATIVE_PATH
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(on_disk_artifact, artifact_before)
        for path, expected in self._preserved_hashes.items():
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                expected,
                str(path),
            )

    def test_smoke_matrix_all_branches_and_locks(self) -> None:
        malformed = self.sufficient_request()
        malformed["sufficiency_basis_records"].pop(
            resolver.SUFFICIENCY_DIMENSION_IDS[0]
        )
        preclaimed = self.canonical_waiting_request(
            operation_result=resolver.OPERATION_RESULT_SUFFICIENT
        )
        prohibited_field = next(iter(resolver.PROHIBITED_REQUEST_FLAGS))
        prohibited = self.canonical_waiting_request(**{prohibited_field: True})
        precedence_records = self.set_dimension_posture(
            self.valid_sufficiency_basis_records(),
            resolver.SUFFICIENCY_DIMENSION_IDS[0],
            contradiction=True,
        )
        precedence_records = self.set_dimension_posture(
            precedence_records,
            resolver.SUFFICIENCY_DIMENSION_IDS[1],
            unresolved=True,
        )
        matrix = (
            (
                "waiting",
                self.canonical_waiting_request(),
                resolver.OUTCOME_REQUIRES_BASIS,
                resolver.OPERATION_RESULT_REQUIRES_BASIS,
            ),
            (
                "sufficient",
                self.sufficient_request(),
                resolver.OUTCOME_RECORDED,
                resolver.OPERATION_RESULT_SUFFICIENT,
            ),
            (
                "insufficient_contradiction",
                self.insufficient_request(),
                resolver.OUTCOME_RECORDED,
                resolver.OPERATION_RESULT_INSUFFICIENT,
            ),
            (
                "insufficient_missing_support",
                self.insufficient_request(missing_support=True),
                resolver.OUTCOME_RECORDED,
                resolver.OPERATION_RESULT_INSUFFICIENT,
            ),
            (
                "indeterminate",
                self.indeterminate_request(),
                resolver.OUTCOME_RECORDED,
                resolver.OPERATION_RESULT_INDETERMINATE,
            ),
            (
                "indeterminate_precedence",
                self.request_with_records(precedence_records),
                resolver.OUTCOME_RECORDED,
                resolver.OPERATION_RESULT_INDETERMINATE,
            ),
            (
                "malformed_basis",
                malformed,
                resolver.OUTCOME_BLOCKED,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
            (
                "preclaimed_result",
                preclaimed,
                resolver.OUTCOME_BLOCKED,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
            (
                "prohibited_downstream",
                prohibited,
                resolver.OUTCOME_BLOCKED,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
            (
                "blocked_intent",
                self.canonical_waiting_request(intent=resolver.INTENT_BLOCK),
                resolver.OUTCOME_BLOCKED,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
            (
                "not_recorded",
                self.canonical_waiting_request(intent=resolver.INTENT_DO_NOT_RECORD),
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OPERATION_RESULT_NOT_EVALUATED,
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for name, request, expected_outcome, expected_result in matrix:
                with self.subTest(case=name):
                    result = self.invoke(request, root)
                    self.assertEqual(result["outcome"], expected_outcome)
                    self.assertEqual(self.operation_result(result), expected_result)
                    self.assert_required_non_claims_false(result)
                    self.assert_downstream_locks_false(result)
                    self.assert_complete_material_omitted(result)
                    if expected_outcome == resolver.OUTCOME_RECORDED:
                        postures = self.candidate_result_postures(result)
                        self.assertEqual(
                            sum(
                                postures[field] is True
                                for field in (
                                    "receiver_side_answerable_basis_candidate_sufficient",
                                    "receiver_side_answerable_basis_candidate_insufficient",
                                    "receiver_side_answerable_basis_candidate_indeterminate",
                                )
                            ),
                            1,
                        )
                        self.assertIs(
                            self.operation(result)[
                                "candidate_sufficiency_operation_exhausted"
                            ],
                            True,
                        )
                    else:
                        self.assert_no_partial_result_stands(result)


if __name__ == "__main__":
    unittest.main()
