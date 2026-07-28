"""Tests for one bounded candidate-sufficiency basis declaration resolver.

Absent or clean partial declaration material remains lawful waiting. Exactly
eight structurally valid records may become ready for later separate supply
only. The suite never supplies or admits basis, executes the waiting operation,
derives a result, or writes a permanent fixture or artifact.
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

import resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min as resolver


GOVERNING_SPEC_PATH = (
    REPO_ROOT / resolver.GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH
)
LIVE_WAITING_ARTIFACT_PATH = (
    REPO_ROOT / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
)
DECLARATION_RESOLVER_PATH = REPO_ROOT / (
    "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_"
    "basis_declaration_v0_min.py"
)
WAITING_OPERATION_SPEC_PATH = REPO_ROOT / (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
    "OPERATION_V0_MIN_SPEC.md"
)
WAITING_OPERATION_RESOLVER_PATH = REPO_ROOT / (
    "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_"
    "operation_v0_min.py"
)
WAITING_OPERATION_TEST_PATH = REPO_ROOT / (
    "tests/test_resolve_receiver_side_answerable_basis_candidate_"
    "sufficiency_operation_v0_min.py"
)
WAITING_OPERATION_SUMMARY_PATH = REPO_ROOT / (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
    "OPERATION_TERMINAL_SUMMARY_V0.md"
)
SUFFICIENCY_BOUNDARY_ARTIFACT_PATH = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_boundary_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_boundary_"
    "v0_min_result.json"
)
V3_EVALUATION_ARTIFACT_PATH = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_evaluation_operation_v0_min_v3/"
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_"
    "v0_min_v3_result.json"
)
V2_WAITING_ARTIFACT_PATH = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_evaluation_operation_v0_min_v2/"
    "receiver_side_answerable_basis_candidate_evaluation_operation_001__"
    "receiver_side_answerable_basis_candidate_evaluation_operation_"
    "v0_min_v2_result.json"
)
V2_COMPLETED_ARTIFACT_PATH = V2_WAITING_ARTIFACT_PATH.with_name(
    V2_WAITING_ARTIFACT_PATH.stem
    + "_001"
    + V2_WAITING_ARTIFACT_PATH.suffix
)


class ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinTests(
    unittest.TestCase
):
    """Prove declaration readiness without supply, admission, or evaluation."""

    BASIS_ITEM_SENTINEL = "COMPLETE_SUFFICIENCY_BASIS_ITEM_MUST_NOT_RETURN"
    BASIS_REFERENCE_SENTINEL = (
        "COMPLETE_SUFFICIENCY_BASIS_REFERENCE_MUST_NOT_RETURN"
    )
    DECLARANT_SENTINEL = "DECLARANT_REFERENCE_CONTENT_MUST_NOT_RETURN"
    EVALUATOR_SENTINEL = "EVALUATOR_REFERENCE_CONTENT_MUST_NOT_RETURN"
    CANDIDATE_SENTINEL = "RAW_CANDIDATE_MATERIAL_MUST_NOT_RETURN"
    CAPTURE_SENTINEL = "CAPTURE_MATERIAL_MUST_NOT_RETURN"

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = tuple(
            path
            for path in (
                GOVERNING_SPEC_PATH,
                DECLARATION_RESOLVER_PATH,
                WAITING_OPERATION_SPEC_PATH,
                WAITING_OPERATION_RESOLVER_PATH,
                WAITING_OPERATION_TEST_PATH,
                WAITING_OPERATION_SUMMARY_PATH,
                LIVE_WAITING_ARTIFACT_PATH,
                SUFFICIENCY_BOUNDARY_ARTIFACT_PATH,
                V3_EVALUATION_ARTIFACT_PATH,
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
        self,
        root: Path,
        case_name: str,
        filename: str | None = None,
    ) -> Path:
        safe = str(case_name).replace("/", "_").replace("\\", "_")
        safe = safe.replace(" ", "_")
        safe = "".join(
            character
            if character.isalnum() or character in "._-"
            else "_"
            for character in safe
        )
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        return root / safe / (filename or resolver.OUTPUT_FILENAME)

    def _write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(
            path.is_dir(),
            f"temporary file path is a directory: {path}",
        )
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(
            path,
            json.dumps(
                value,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n",
        )

    def load_selected_live_waiting_operation_artifact(
        self,
    ) -> dict[str, object]:
        value = json.loads(
            LIVE_WAITING_ARTIFACT_PATH.read_text(encoding="utf-8")
        )
        self.assertIsInstance(value, dict)
        return self.clone(value)

    def synthetic_governing_declaration_specification(self) -> str:
        markers: list[str] = [
            "# Receiver-Side Answerable Basis Candidate Sufficiency Basis "
            "Declaration V0 Minimum Specification",
            resolver.DECLARATION_ID,
            resolver.DECLARATION_TYPE,
            resolver.DECLARATION_VERSION,
            resolver.DECLARATION_SCOPE,
            resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
            resolver.SELECTED_SUFFICIENCY_OPERATION_TYPE,
            resolver.SELECTED_SUFFICIENCY_OPERATION_VERSION,
            resolver.SELECTED_SUFFICIENCY_OPERATION_SCOPE,
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
            resolver.CANDIDATE_ID,
            resolver.CANDIDATE_TYPE,
            resolver.CANDIDATE_SCOPE,
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
            resolver.SELECTED_RECEPTION_OPERATION_ID,
            resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            resolver.SELECTED_EVALUATION_OPERATION_ID,
            "Declaration is not operation supply.",
            "Preparation is not admission.",
            "Basis record is not dimension result.",
            "Support posture declared is not SATISFIED.",
            "Contradiction posture declared is not NOT_SATISFIED.",
            "Unresolved posture declared is not INDETERMINATE.",
            "Eight records complete is not candidate sufficient.",
            "Complete declaration is not candidate sufficient.",
            "Source-body authorship is not independent custody.",
            "Declaration readiness is not operation authorization.",
            "Later separate supply remains required.",
            "source_body_authored",
            "independent_preparer_claimed",
            "separate_custody_claimed_by_preparer",
        ]
        for marker_class in resolver.DECLARATION_SPEC_MARKER_CLASSES.values():
            markers.extend(marker_class)
        markers.extend(resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS)
        for dimension_id in resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS:
            markers.extend(
                resolver.DIMENSION_RULE_KEYS[dimension_id].values()
            )
            markers.append(
                resolver.DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
            )
        markers.extend(resolver.OUTCOME_FAMILY)
        markers.extend(resolver.DECLARATION_RESULT_FAMILY)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def synthetic_valid_waiting_operation_artifact(
        self,
    ) -> dict[str, object]:
        operation: dict[str, object] = {
            "operation_id": resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
            "operation_type": resolver.SELECTED_SUFFICIENCY_OPERATION_TYPE,
            "operation_version": resolver.SELECTED_SUFFICIENCY_OPERATION_VERSION,
            "operation_scope": resolver.SELECTED_SUFFICIENCY_OPERATION_SCOPE,
            "receiver_side_answerable_basis_candidate_sufficiency_operation_id": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_ID
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_operation_type": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_TYPE
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_operation_version": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_VERSION
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_operation_scope": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_SCOPE
            ),
            "operation_result": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
            ),
            "candidate_sufficiency_operation_result": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_operation_result": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED
            ),
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": (
                resolver.CANDIDATE_TYPE
            ),
            "receiver_side_answerable_basis_candidate_scope": (
                resolver.CANDIDATE_SCOPE
            ),
            "selected_candidate_reception_operation_id": (
                resolver.SELECTED_RECEPTION_OPERATION_ID
            ),
            "selected_candidate_evaluation_boundary_id": (
                resolver.SELECTED_EVALUATION_BOUNDARY_ID
            ),
            "selected_candidate_evaluation_operation_id": (
                resolver.SELECTED_EVALUATION_OPERATION_ID
            ),
            "selected_candidate_sufficiency_boundary_id": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID
            ),
            "selected_candidate_sufficiency_boundary_type": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE
            ),
            "sufficiency_basis_supplied": False,
            "sufficiency_basis_complete": False,
            "atomic_sufficiency_basis_gate_passed": False,
            "candidate_sufficiency_operation_recorded": False,
            "candidate_sufficiency_operation_result_recorded": False,
            "candidate_sufficiency_operation_exhausted": False,
        }
        for field in (
            *resolver.UPSTREAM_CANDIDATE_FALSE_POSTURES,
            *resolver.UPSTREAM_RECEIVER_FALSE_POSTURES,
            *resolver.UPSTREAM_REPEAT_AND_DOWNSTREAM_FALSE_POSTURES,
        ):
            operation[field] = False
        dimensions = {
            dimension_id: {
                "dimension_id": dimension_id,
                "dimension_result": "NOT_EVALUATED",
                "dimension_evaluated": False,
                "dimension_established": False,
            }
            for dimension_id in resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS
        }
        non_claims = {
            field: False
            for field in resolver.UPSTREAM_REPEAT_AND_DOWNSTREAM_FALSE_POSTURES
        }
        return {
            "resolver_module": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE
            ),
            "result_version": resolver.RESULT_VERSION,
            "outcome": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_OUTCOME_REQUIRED
            ),
            "failed_check_count": 0,
            "passed_check_count": 133,
            "receiver_side_answerable_basis_candidate_sufficiency_operation": (
                operation
            ),
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_dimensions": dimensions,
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_summary": {
                "upstream_boundary_validated": True,
                "sufficiency_basis_supplied": False,
                "sufficiency_basis_complete": False,
                "atomic_sufficiency_basis_gate_passed": False,
            },
            "non_claims": non_claims,
            "what_remains_open": list(resolver.WAITING_WHAT_REMAINS_OPEN),
        }

    def fixture_root(
        self,
        root: Path,
        *,
        specification: str | None = None,
        waiting_artifact: dict[str, object] | None = None,
    ) -> tuple[Path, Path]:
        spec_path = self._write_text(
            root / resolver.GOVERNING_DECLARATION_SPECIFICATION_RELATIVE_PATH,
            (
                self.synthetic_governing_declaration_specification()
                if specification is None
                else specification
            ),
        )
        artifact_path = self._write_json(
            root / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH,
            self.clone(
                self.synthetic_valid_waiting_operation_artifact()
                if waiting_artifact is None
                else waiting_artifact
            ),
        )
        return spec_path, artifact_path

    def canonical_incomplete_request(
        self,
        **overrides: object,
    ) -> dict[str, object]:
        return (
            resolver.build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def valid_declaration_records(
        self,
        *,
        source_body_authored: bool = True,
    ) -> dict[str, dict[str, object]]:
        records: dict[str, dict[str, object]] = {}
        for dimension_id in resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS:
            keys = resolver.DIMENSION_RULE_KEYS[dimension_id]
            records[dimension_id] = {
                "dimension_id": dimension_id,
                "receiver_side_answerable_basis_candidate_id": (
                    resolver.CANDIDATE_ID
                ),
                "selected_candidate_sufficiency_boundary_id": (
                    resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID
                ),
                "selected_candidate_sufficiency_operation_id": (
                    resolver.SELECTED_SUFFICIENCY_OPERATION_ID
                ),
                "basis_items": [
                    {
                        "basis_item_id": dimension_id + "_item_001",
                        "bounded_input": self.BASIS_ITEM_SENTINEL,
                        "candidate_material": self.CANDIDATE_SENTINEL,
                    }
                ],
                "basis_references": [
                    {
                        "basis_reference_id": dimension_id + "_reference_001",
                        "bounded_reference": self.BASIS_REFERENCE_SENTINEL,
                        "capture_material": self.CAPTURE_SENTINEL,
                    }
                ],
                "declarant_reference": {
                    "declarant_reference_id": "bounded_declarant",
                    "content": self.DECLARANT_SENTINEL,
                },
                "evaluator_reference": {
                    "evaluator_reference_id": "bounded_evaluator",
                    "content": self.EVALUATOR_SENTINEL,
                },
                "support_postures": {keys["support"]: True},
                "contradiction_postures": {keys["contradiction"]: False},
                "unresolved_postures": {keys["unresolved"]: False},
                "basis_non_claims": {
                    key: False for key in resolver.REQUIRED_BASIS_NON_CLAIMS
                },
                "non_conversion_statement": (
                    resolver.DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
                ),
                "source_body_authored": source_body_authored,
                "independent_preparer_claimed": False,
                "separate_custody_claimed_by_preparer": False,
            }
        return records

    def accepted_source_body_authored_records(
        self,
    ) -> dict[str, dict[str, object]]:
        return self.valid_declaration_records(source_body_authored=True)

    def request_with_records(
        self,
        records: dict[str, dict[str, object]],
        **overrides: object,
    ) -> dict[str, object]:
        return (
            resolver.build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request(
                self.clone(records),
                **copy.deepcopy(overrides),
            )
        )

    def invoke(
        self,
        request: dict[str, object] | None = None,
        *,
        root: Path | None = None,
    ) -> dict[str, object]:
        supplied = self.clone(request) if request is not None else None
        before = self.clone(supplied)
        if root is None:
            result = (
                resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min(
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
        specification: str | None = None,
        waiting_artifact: dict[str, object] | None = None,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(
                root,
                specification=specification,
                waiting_artifact=waiting_artifact,
            )
            return self.invoke(
                (
                    self.canonical_incomplete_request()
                    if request is None
                    else request
                ),
                root=root,
            )

    def declaration(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration"
        )
        self.assertIsInstance(value, dict)
        return value

    def declaration_result(self, result: dict[str, object]) -> str:
        value = self.declaration(result).get("declaration_result")
        self.assertIsInstance(value, str)
        return value

    def failed_check_count(self, result: dict[str, object]) -> int:
        value = result.get("failed_check_count")
        self.assertIsInstance(value, int)
        self.assertNotIsInstance(value, bool)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        value = block.get("code") or block.get("block_code")
        self.assertTrue(value is None or isinstance(value, str))
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_checks"
        )
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))

    def assert_all_emitted_codes_public(
        self,
        result: dict[str, object],
    ) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for field in ("block_code", "failure_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_required_false_non_claims(
        self,
        result: dict[str, object],
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
            self.assertIsInstance(non_claims[key], bool)

    def assert_required_basis_non_claims(
        self,
        records: dict[str, dict[str, object]],
    ) -> None:
        for dimension_id in resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS:
            non_claims = records[dimension_id]["basis_non_claims"]
            self.assertIsInstance(non_claims, dict)
            self.assertEqual(
                set(non_claims),
                set(resolver.REQUIRED_BASIS_NON_CLAIMS),
            )
            for key in resolver.REQUIRED_BASIS_NON_CLAIMS:
                self.assertIs(non_claims[key], False, f"{dimension_id}.{key}")

    def assert_supply_result_and_downstream_locks(
        self,
        result: dict[str, object],
    ) -> None:
        declaration = self.declaration(result)
        for key in (
            "candidate_sufficiency_basis_separately_supplied",
            "candidate_sufficiency_basis_admitted_by_operation",
            "candidate_sufficiency_operation_executed",
            "candidate_sufficiency_operation_exhausted",
            "dimension_results_derived",
            "candidate_result_derived",
        ):
            self.assertIs(declaration.get(key), False, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(declaration.get(key), False, key)
        detail = result.get("declaration_result_detail")
        self.assertIsInstance(detail, dict)
        for key in (
            "candidate_sufficiency_basis_separately_supplied",
            "candidate_sufficiency_basis_admitted_by_operation",
            "candidate_sufficiency_operation_executed",
            "candidate_sufficiency_operation_exhausted",
            "dimension_result_exists",
            "candidate_result_exists",
        ):
            self.assertIs(detail.get(key), False, key)
        self.assert_required_false_non_claims(result)

    def assert_complete_declaration_material_omitted(
        self,
        result: dict[str, object],
    ) -> None:
        records = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_records"
        )
        self.assertIsInstance(records, dict)
        for key in (
            "complete_declaration_content_omitted",
            "complete_basis_items_omitted",
            "complete_basis_references_omitted",
            "declarant_reference_content_omitted",
            "evaluator_reference_content_omitted",
            "raw_candidate_material_omitted",
            "capture_material_omitted",
        ):
            self.assertIs(records.get(key), True, key)

        forbidden_keys = {
            "basis_items",
            "basis_references",
            "declarant_reference",
            "evaluator_reference",
            "candidate_material",
            "candidate_packet",
            "raw_candidate_material",
            "capture_material",
            "raw_samples",
            "zip_bytes",
            "selected_waiting_operation_artifact",
            "waiting_operation_artifact_content",
            "upstream_checks",
            "receiver_side_answerable_basis_candidate_sufficiency_operation",
            "receiver_side_answerable_basis_candidate_sufficiency_operation_checks",
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
        serialized = json.dumps(result, sort_keys=True, ensure_ascii=True)
        for sentinel in (
            self.BASIS_ITEM_SENTINEL,
            self.BASIS_REFERENCE_SENTINEL,
            self.DECLARANT_SENTINEL,
            self.EVALUATOR_SENTINEL,
            self.CANDIDATE_SENTINEL,
            self.CAPTURE_SENTINEL,
        ):
            self.assertNotIn(sentinel, serialized)

    def assert_declaration_has_no_wrapper_fields(
        self,
        result: dict[str, object],
    ) -> None:
        declaration = self.declaration(result)
        for key in (
            "outcome",
            "block",
            "non_claims",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_checks",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_summary",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_metadata",
        ):
            self.assertNotIn(key, declaration)

    def assert_blocked(
        self,
        result: dict[str, object],
        expected_code: str | tuple[str, ...] | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            self.declaration_result(result),
            resolver.DECLARATION_RESULT_NOT_EVALUATED,
        )
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if isinstance(expected_code, tuple):
            self.assertIn(code, expected_code)
        elif expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        declaration = self.declaration(result)
        self.assertIs(
            declaration.get(
                "candidate_sufficiency_basis_declaration_ready_for_supply"
            ),
            False,
        )
        self.assert_supply_result_and_downstream_locks(result)
        self.assert_complete_declaration_material_omitted(result)

    def assert_incomplete(
        self,
        result: dict[str, object],
        expected_count: int,
    ) -> None:
        self.assertEqual(
            result.get("outcome"),
            resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION,
        )
        self.assertEqual(
            self.declaration_result(result),
            resolver.DECLARATION_RESULT_REQUIRES_COMPLETE,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        declaration = self.declaration(result)
        self.assertEqual(declaration.get("declaration_record_count"), expected_count)
        for key in (
            "declaration_complete",
            "candidate_sufficiency_basis_declaration_recorded",
            "candidate_sufficiency_basis_declaration_result_recorded",
            "candidate_sufficiency_basis_declaration_ready_for_supply",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_recorded",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_result_recorded",
        ):
            self.assertIs(declaration.get(key), False, key)
        self.assertEqual(
            tuple(result.get("what_remains_open", ())),
            resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
        )
        self.assert_supply_result_and_downstream_locks(result)
        self.assert_complete_declaration_material_omitted(result)

    def assert_ready(
        self,
        result: dict[str, object],
        *,
        source_body_count: int,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(
            self.declaration_result(result),
            resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        declaration = self.declaration(result)
        self.assertEqual(
            declaration.get("declaration_record_count"),
            len(resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS),
        )
        for key in (
            "declaration_complete",
            "candidate_sufficiency_basis_declaration_recorded",
            "candidate_sufficiency_basis_declaration_result_recorded",
            "candidate_sufficiency_basis_declaration_ready_for_supply",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_recorded",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_result_recorded",
        ):
            self.assertIs(declaration.get(key), True, key)
        self.assertEqual(
            tuple(result.get("what_remains_open", ())),
            resolver.READY_WHAT_REMAINS_OPEN,
        )
        summary = result.get(
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_summary"
        )
        self.assertIsInstance(summary, dict)
        self.assertEqual(
            summary["authorship_posture_counts"]["source_body_authored"],
            source_body_count,
        )
        self.assertEqual(
            summary["authorship_posture_counts"]["non_source_body_authored"],
            len(resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS)
            - source_body_count,
        )
        self.assert_supply_result_and_downstream_locks(result)
        self.assert_complete_declaration_material_omitted(result)

    def test_public_api_and_exact_constants(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)), name)
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_"
            "basis_declaration_v0_min",
        )
        self.assertEqual(
            resolver.DECLARATION_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "basis_declaration_001",
        )
        self.assertEqual(
            resolver.DECLARATION_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
            "BASIS_DECLARATION",
        )
        self.assertEqual(resolver.DECLARATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.DECLARATION_SCOPE,
            "DECLARE_ONE_BOUNDED_EIGHT_DIMENSION_CANDIDATE_SUFFICIENCY_"
            "BASIS_ONLY",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_001",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
            "REQUIRES_SUFFICIENCY_BASIS",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_VERSION,
            "0.1.0",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_SCOPE,
            "DECIDE_SUFFICIENCY_POSTURE_OF_ONE_SELECTED_RECEIVER_SIDE_"
            "ANSWERABLE_BASIS_CANDIDATE_ONLY",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_v0_min",
        )
        self.assertEqual(
            resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_001",
        )
        self.assertEqual(
            resolver.CANDIDATE_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE",
        )
        self.assertEqual(
            resolver.CANDIDATE_SCOPE,
            "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_"
            "CANDIDATE_ONLY",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "boundary_001",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_BOUNDARY_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BOUNDARY",
        )
        self.assertEqual(
            resolver.SELECTED_RECEPTION_OPERATION_ID,
            "receiver_side_answerable_basis_reception_operation_001",
        )
        self.assertEqual(
            resolver.SELECTED_EVALUATION_BOUNDARY_ID,
            "receiver_side_answerable_basis_candidate_evaluation_boundary_001",
        )
        self.assertEqual(
            resolver.SELECTED_EVALUATION_OPERATION_ID,
            "receiver_side_answerable_basis_candidate_evaluation_"
            "operation_001",
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
        self.assertEqual(
            resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS,
            expected_dimensions,
        )
        self.assertEqual(tuple(resolver.DIMENSION_LABELS), expected_dimensions)
        self.assertEqual(tuple(resolver.DIMENSION_RULE_KEYS), expected_dimensions)
        self.assertEqual(
            tuple(resolver.DIMENSION_NON_CONVERSION_STATEMENTS),
            expected_dimensions,
        )
        expected_labels = {
            "receiver_answerability_fit": "receiver-answerability fit",
            "selected_purpose_adequacy": "selected-purpose adequacy",
            "bounded_material_completeness": (
                "bounded material completeness"
            ),
            "unresolved_contradiction_posture": (
                "unresolved contradiction posture"
            ),
            "unsupported_assumption_dependency": (
                "unsupported assumption dependency"
            ),
            "scope_constrained_usability": "scope-constrained usability",
            "refusal_withholding_compatibility": (
                "refusal and withholding compatibility"
            ),
            "provenance_capture_limitation_posture": (
                "provenance and capture limitation posture"
            ),
        }
        expected_rules = {
            "receiver_answerability_fit": {
                "support": "bounded_receiver_answerability_fit_supported",
                "contradiction": (
                    "bounded_receiver_answerability_fit_contradicted"
                ),
                "unresolved": (
                    "bounded_receiver_answerability_fit_unresolved"
                ),
            },
            "selected_purpose_adequacy": {
                "support": "selected_purpose_adequacy_supported",
                "contradiction": "selected_purpose_adequacy_contradicted",
                "unresolved": "selected_purpose_adequacy_unresolved",
            },
            "bounded_material_completeness": {
                "support": (
                    "bounded_material_complete_for_selected_purpose"
                ),
                "contradiction": (
                    "bounded_material_incomplete_for_selected_purpose"
                ),
                "unresolved": "bounded_material_completeness_unresolved",
            },
            "unresolved_contradiction_posture": {
                "support": (
                    "no_unresolved_material_contradiction_for_selected_purpose"
                ),
                "contradiction": (
                    "material_contradiction_present_for_selected_purpose"
                ),
                "unresolved": (
                    "material_contradiction_posture_unresolved"
                ),
            },
            "unsupported_assumption_dependency": {
                "support": (
                    "no_required_unsupported_assumption_dependency"
                ),
                "contradiction": (
                    "required_unsupported_assumption_dependency_present"
                ),
                "unresolved": (
                    "unsupported_assumption_dependency_unresolved"
                ),
            },
            "scope_constrained_usability": {
                "support": "usable_within_selected_scope",
                "contradiction": "not_usable_within_selected_scope",
                "unresolved": "scope_constrained_usability_unresolved",
            },
            "refusal_withholding_compatibility": {
                "support": (
                    "compatible_with_recorded_refusal_and_withholding_postures"
                ),
                "contradiction": (
                    "incompatible_with_recorded_refusal_or_withholding_posture"
                ),
                "unresolved": (
                    "refusal_withholding_compatibility_unresolved"
                ),
            },
            "provenance_capture_limitation_posture": {
                "support": (
                    "provenance_and_capture_limitations_bounded_and_preserved"
                ),
                "contradiction": (
                    "provenance_or_capture_limitation_materially_contradicts_"
                    "selected_use"
                ),
                "unresolved": (
                    "provenance_capture_limitation_posture_unresolved"
                ),
            },
        }
        expected_non_conversion = {
            "receiver_answerability_fit": (
                "receiver-answerability fit is not attestation, receipt, "
                "or presence."
            ),
            "selected_purpose_adequacy": (
                "selected-purpose adequacy is bounded-purpose posture only, "
                "not truth or standing."
            ),
            "bounded_material_completeness": (
                "bounded completeness is not unrestricted completeness or "
                "candidate truth."
            ),
            "unresolved_contradiction_posture": (
                "no unresolved material contradiction is not verified truth."
            ),
            "unsupported_assumption_dependency": (
                "absence of a required unsupported assumption dependency is "
                "not authority or standing."
            ),
            "scope_constrained_usability": (
                "scoped usability is not general usability, output "
                "authorization, or action authorization."
            ),
            "refusal_withholding_compatibility": (
                "refusal and withholding compatibility is not consent, "
                "attestation, or receipt."
            ),
            "provenance_capture_limitation_posture": (
                "bounded provenance and capture limitations are not verified "
                "provenance, physical validity, or presence."
            ),
        }
        self.assertEqual(dict(resolver.DIMENSION_LABELS), expected_labels)
        self.assertEqual(
            {
                key: dict(value)
                for key, value in resolver.DIMENSION_RULE_KEYS.items()
            },
            expected_rules,
        )
        self.assertEqual(
            dict(resolver.DIMENSION_NON_CONVERSION_STATEMENTS),
            expected_non_conversion,
        )
        for dimension_id in expected_dimensions:
            self.assertTrue(resolver.DIMENSION_LABELS[dimension_id])
            self.assertEqual(
                set(resolver.DIMENSION_RULE_KEYS[dimension_id]),
                {"support", "contradiction", "unresolved"},
            )
            self.assertTrue(
                resolver.DIMENSION_NON_CONVERSION_STATEMENTS[dimension_id]
            )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION,
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_NOT_RECORDED,
            ),
        )
        self.assertEqual(
            resolver.DECLARATION_RESULT_FAMILY,
            (
                resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
                resolver.DECLARATION_RESULT_REQUIRES_COMPLETE,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
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
            "integrity_host_v0_min_coexistence_receiver_side_answerable_"
            "basis_candidate_sufficiency_basis_declaration_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_001__receiver_side_answerable_basis_candidate_"
            "sufficiency_basis_declaration_v0_min_result.json",
        )

    def test_static_contracts_nonclaims_flags_and_public_codes(self) -> None:
        expected_basis_non_claims = (
            "caller_supplied_dimension_result",
            "caller_supplied_candidate_result",
            "evaluator_reference_to_authority",
            "evaluator_reference_to_identity",
            "evaluator_reference_to_standing",
            "evaluator_reference_to_truth",
            "declarant_reference_to_authority",
            "declarant_reference_to_identity",
            "declarant_reference_to_standing",
            "declarant_reference_to_truth",
            "basis_items_to_established_truth",
            "basis_references_to_verified_provenance",
            "source_body_authorship_to_independent_custody",
            "declaration_readiness_to_operation_authorization",
        )
        self.assertEqual(
            resolver.REQUIRED_BASIS_NON_CLAIMS,
            expected_basis_non_claims,
        )
        required_declaration_locks = {
            "caller_supplied_dimension_result",
            "caller_supplied_candidate_result",
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "candidate_sufficiency_decided",
            "candidate_sufficiency_established",
            "candidate_insufficiency_established",
            "candidate_indeterminacy_established",
            "candidate_sufficiency_basis_separately_supplied",
            "candidate_sufficiency_basis_admitted_by_operation",
            "candidate_sufficiency_operation_created",
            "candidate_sufficiency_operation_authorized",
            "candidate_sufficiency_operation_recorded",
            "candidate_sufficiency_operation_result_recorded",
            "candidate_sufficiency_operation_executed",
            "candidate_sufficiency_operation_exhausted",
            "partial_dimension_evaluation_recorded",
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
            "continuity_memory_written",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "evaluator_reference_to_authority",
            "evaluator_reference_to_identity",
            "evaluator_reference_to_standing",
            "evaluator_reference_to_truth",
            "declarant_reference_to_authority",
            "declarant_reference_to_identity",
            "declarant_reference_to_standing",
            "declarant_reference_to_truth",
            "basis_items_to_established_truth",
            "basis_references_to_verified_provenance",
            "source_body_authorship_to_independent_custody",
            "declaration_readiness_to_operation_authorization",
            "repeated_declaration_permission_created",
            "reusable_declaration_route_created",
            "silent_declaration_replacement_authorized",
            "automatic_redeclaration_created",
            "declaration_debt_created",
            "declaration_obligation_created",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        }
        self.assertEqual(
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
            required_declaration_locks,
        )
        required_prohibited_flags = {
            "request_declaration_result_preclaim",
            "request_declaration_ready_for_supply_preclaim",
            "request_basis_separate_supply",
            "request_basis_operation_admission",
            "request_operation_execution",
            "request_operation_exhaustion",
            "request_dimension_result",
            "request_candidate_sufficient",
            "request_candidate_insufficient",
            "request_candidate_indeterminate",
            "request_receiver_attestation_creation",
            "request_receiver_attestation_support",
            "request_receiver_answerable_receipt_creation",
            "request_presence_support",
            "request_presence_authorization",
            "request_presence_establishment",
            "request_presence_recording",
            "request_identity_creation",
            "request_relation_creation",
            "request_coupling_assignment",
            "request_coupling_creation",
            "request_field_machinery_creation",
            "request_runtime_creation",
            "request_api_creation",
            "request_authority_creation",
            "request_standing_creation",
            "request_truth_creation",
            "request_output_authorization",
            "request_action_authorization",
            "request_synchronization_authorization",
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
            "request_repeated_declaration_permission_creation",
            "request_reusable_declaration_route_creation",
            "request_silent_declaration_replacement",
            "request_automatic_redeclaration",
            "request_declaration_debt_creation",
            "request_declaration_obligation_creation",
            "request_repository_scan",
            "request_file_discovery",
            "request_affected_file_repair",
            "request_affected_file_mutation",
            "request_prior_unsupported_claim_validation",
            "request_validation_enforcement",
        }
        self.assertEqual(
            set(resolver.PROHIBITED_REQUEST_FLAGS),
            required_prohibited_flags,
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
            "DECLARATION_SPEC_REFERENCE_MISSING",
            "DECLARATION_SPEC_MARKER_MISSING",
            "SELECTED_WAITING_OPERATION_ARTIFACT_REFERENCE_MISSING",
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_PARSEABLE",
            "SELECTED_WAITING_OPERATION_ARTIFACT_NOT_MAPPING",
            "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            "UPSTREAM_OPERATION_NOT_WAITING_FOR_BASIS",
            "UPSTREAM_OPERATION_RESULT_MISMATCH",
            "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
            "UPSTREAM_BOUNDARY_NOT_VALIDATED",
            "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_COMPLETE",
            "UPSTREAM_ATOMIC_GATE_ALREADY_PASSED",
            "UPSTREAM_OPERATION_ALREADY_RECORDED",
            "UPSTREAM_OPERATION_RESULT_ALREADY_RECORDED",
            "UPSTREAM_OPERATION_ALREADY_EXHAUSTED",
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
            "DECLARATION_RECORDS_NOT_MAPPING",
            "DECLARATION_DIMENSION_SET_MISMATCH",
            "DECLARATION_RECORD_NOT_MAPPING",
            "DECLARATION_RECORD_IDENTITY_MISMATCH",
            "DECLARATION_BASIS_ITEMS_INVALID",
            "DECLARATION_BASIS_REFERENCES_INVALID",
            "DECLARANT_REFERENCE_INVALID",
            "EVALUATOR_REFERENCE_INVALID",
            "DECLARATION_RULE_INPUTS_INVALID",
            "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            "DECLARATION_NON_CONVERSION_STATEMENT_MISMATCH",
            "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
            "FALSE_SEPARATE_CUSTODY_CLAIM",
            "DECLARATION_RESULT_PRECLAIMED",
            "RESULT_POSTURE_PRECLAIMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        }
        self.assertTrue(expected_public_codes.issubset(resolver.BLOCK_CODES))

    def test_default_live_incomplete_result(self) -> None:
        if not GOVERNING_SPEC_PATH.is_file() or not LIVE_WAITING_ARTIFACT_PATH.is_file():
            self.skipTest(
                "exact live specification or waiting-operation artifact unavailable"
            )
        before_spec = GOVERNING_SPEC_PATH.read_bytes()
        before_artifact = LIVE_WAITING_ARTIFACT_PATH.read_bytes()
        loaded = self.load_selected_live_waiting_operation_artifact()
        loaded_before = self.clone(loaded)
        result = self.invoke()
        self.assert_incomplete(result, 0)
        self.assertIs(
            self.declaration(result).get("declaration_records_supplied"),
            False,
        )
        self.assertEqual(loaded, loaded_before)
        self.assertEqual(GOVERNING_SPEC_PATH.read_bytes(), before_spec)
        self.assertEqual(LIVE_WAITING_ARTIFACT_PATH.read_bytes(), before_artifact)

    def test_synthetic_incomplete_result(self) -> None:
        artifact = self.synthetic_valid_waiting_operation_artifact()
        artifact_before = self.clone(artifact)
        result = self.resolve_synthetic(
            self.canonical_incomplete_request(),
            waiting_artifact=artifact,
        )
        self.assert_incomplete(result, 0)
        self.assertEqual(artifact, artifact_before)
        self.assertIs(
            result["upstream_basis"]["waiting_posture_validation"][
                "all_eight_dimensions_not_evaluated"
            ],
            True,
        )

    def test_complete_source_body_declaration_is_ready_only_for_supply(self) -> None:
        records = self.accepted_source_body_authored_records()
        records_before = self.clone(records)
        request = self.request_with_records(records)
        request_before = self.clone(request)
        self.assert_required_basis_non_claims(records)
        result = self.resolve_synthetic(request)
        self.assert_ready(result, source_body_count=8)
        self.assertEqual(records, records_before)
        self.assertEqual(request, request_before)
        self.assert_declaration_has_no_wrapper_fields(result)
        records_section = result[
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_records"
        ]
        self.assertEqual(
            tuple(records_section["declaration_record_ids"]),
            resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS,
        )
        self.assertEqual(records_section["missing_declaration_record_ids"], [])

    def test_source_body_authorship_separation(self) -> None:
        result = self.resolve_synthetic(
            self.request_with_records(
                self.accepted_source_body_authored_records()
            )
        )
        self.assert_ready(result, source_body_count=8)
        statement = result[
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_statement"
        ]
        non_meaning = result[
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_non_meaning"
        ]
        self.assertIs(
            statement["source_body_authorship_not_independent_custody"],
            True,
        )
        self.assertIs(
            non_meaning["source_body_authorship_is_not_independent_custody"],
            True,
        )
        declaration = self.declaration(result)
        for key in (
            "source_body_authorship_to_independent_custody",
            "authority_created",
            "identity_created",
            "standing_created",
            "truth_created",
            "basis_references_to_verified_provenance",
            "receiver_side_answerable_basis_candidate_sufficient",
        ):
            self.assertIs(declaration[key], False, key)
        summaries = result[
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_records"
        ]["record_summaries"]
        for summary in summaries.values():
            self.assertIs(summary["source_body_authored"], True)
            self.assertIs(summary["independent_preparer_claimed"], False)
            self.assertIs(
                summary["separate_custody_claimed_by_preparer"],
                False,
            )

    def test_non_source_body_preparer_posture_is_bounded(self) -> None:
        records = self.valid_declaration_records(source_body_authored=False)
        records[resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]][
            "basis_references"
        ][0]["repository_path"] = "synthetic/separate/declaration.json"
        result = self.resolve_synthetic(self.request_with_records(records))
        self.assert_ready(result, source_body_count=0)
        declaration = self.declaration(result)
        for key in (
            "source_body_authorship_to_independent_custody",
            "evaluator_reference_to_authority",
            "evaluator_reference_to_identity",
            "evaluator_reference_to_standing",
            "evaluator_reference_to_truth",
            "declarant_reference_to_authority",
            "declarant_reference_to_identity",
            "declarant_reference_to_standing",
            "declarant_reference_to_truth",
            "basis_references_to_verified_provenance",
        ):
            self.assertIs(declaration[key], False, key)

    def test_partial_declaration_behavior(self) -> None:
        variants: list[
            tuple[str, dict[str, object], int]
        ] = [
            ("not_supplied", self.canonical_incomplete_request(), 0),
            (
                "zero_records",
                self.request_with_records({}),
                0,
            ),
        ]
        complete = self.valid_declaration_records()
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        one = {first: self.clone(complete[first])}
        variants.append(("one_record", self.request_with_records(one), 1))
        seven = self.clone(complete)
        seven.pop(resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[-1])
        variants.append(("seven_records", self.request_with_records(seven), 7))
        for name, request, count in variants:
            with self.subTest(case=name):
                result = self.resolve_synthetic(request)
                self.assert_incomplete(result, count)

        inconsistent = self.canonical_incomplete_request()
        inconsistent["declaration_records_supplied"] = True
        inconsistent["declaration_records"] = None
        self.assert_blocked(
            self.resolve_synthetic(inconsistent),
            "DECLARATION_RECORDS_NOT_MAPPING",
        )

    def test_exact_eight_record_validation_matrix(self) -> None:
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        keys = resolver.DIMENSION_RULE_KEYS[first]

        def mutate(label: str) -> object:
            records: object = self.valid_declaration_records()
            record = records[first]
            if label == "missing_dimension":
                records.pop(first)
            elif label == "extra_dimension":
                records["unknown_dimension"] = self.clone(record)
            elif label == "wrong_enclosing_key":
                records["wrong_dimension"] = records.pop(first)
            elif label == "mismatched_dimension_id":
                record["dimension_id"] = "wrong"
            elif label == "record_not_mapping":
                records[first] = []
            elif label == "wrong_candidate_id":
                record["receiver_side_answerable_basis_candidate_id"] = "wrong"
            elif label == "wrong_boundary_id":
                record["selected_candidate_sufficiency_boundary_id"] = "wrong"
            elif label == "wrong_operation_id":
                record["selected_candidate_sufficiency_operation_id"] = "wrong"
            elif label == "empty_basis_items":
                record["basis_items"] = []
            elif label == "basis_items_not_sequence":
                record["basis_items"] = {}
            elif label == "invalid_basis_item":
                record["basis_items"] = ["not-a-mapping"]
            elif label == "excessive_basis_item_count":
                record["basis_items"] = [
                    {"index": index}
                    for index in range(resolver.MAX_SEQUENCE_ITEMS + 1)
                ]
            elif label == "excessive_text_length":
                record["basis_items"] = [
                    {"text": "x" * (resolver.MAX_TEXT_LENGTH + 1)}
                ]
            elif label == "empty_basis_references":
                record["basis_references"] = []
            elif label == "invalid_basis_reference":
                record["basis_references"] = [None]
            elif label == "invalid_declarant_reference":
                record["declarant_reference"] = {}
            elif label == "invalid_evaluator_reference":
                record["evaluator_reference"] = []
            elif label == "missing_support_map":
                record.pop("support_postures")
            elif label == "extra_support_key":
                record["support_postures"]["extra"] = False
            elif label == "non_boolean_support":
                record["support_postures"][keys["support"]] = 1
            elif label == "missing_contradiction_map":
                record.pop("contradiction_postures")
            elif label == "extra_contradiction_key":
                record["contradiction_postures"]["extra"] = False
            elif label == "non_boolean_contradiction":
                record["contradiction_postures"][keys["contradiction"]] = "false"
            elif label == "missing_unresolved_map":
                record.pop("unresolved_postures")
            elif label == "extra_unresolved_key":
                record["unresolved_postures"]["extra"] = False
            elif label == "non_boolean_unresolved":
                record["unresolved_postures"][keys["unresolved"]] = None
            elif label == "missing_basis_nonclaim":
                record["basis_non_claims"].pop(
                    resolver.REQUIRED_BASIS_NON_CLAIMS[0]
                )
            elif label == "flipped_basis_nonclaim":
                record["basis_non_claims"][
                    resolver.REQUIRED_BASIS_NON_CLAIMS[0]
                ] = True
            elif label == "wrong_non_conversion_statement":
                record["non_conversion_statement"] = "wrong"
            elif label == "non_boolean_source_body_authored":
                record["source_body_authored"] = "true"
            elif label == "non_boolean_independent_preparer_claimed":
                record["independent_preparer_claimed"] = 0
            elif label == "non_boolean_separate_custody_claimed":
                record["separate_custody_claimed_by_preparer"] = None
            return records

        cases = (
            ("missing_dimension", None),
            ("extra_dimension", "DECLARATION_DIMENSION_SET_MISMATCH"),
            ("wrong_enclosing_key", "DECLARATION_DIMENSION_SET_MISMATCH"),
            ("mismatched_dimension_id", "DECLARATION_RECORD_IDENTITY_MISMATCH"),
            ("record_not_mapping", "DECLARATION_RECORD_NOT_MAPPING"),
            ("wrong_candidate_id", "DECLARATION_RECORD_IDENTITY_MISMATCH"),
            ("wrong_boundary_id", "DECLARATION_RECORD_IDENTITY_MISMATCH"),
            ("wrong_operation_id", "DECLARATION_RECORD_IDENTITY_MISMATCH"),
            ("empty_basis_items", "DECLARATION_BASIS_ITEMS_INVALID"),
            ("basis_items_not_sequence", "DECLARATION_BASIS_ITEMS_INVALID"),
            ("invalid_basis_item", "DECLARATION_BASIS_ITEMS_INVALID"),
            (
                "excessive_basis_item_count",
                (
                    "REQUEST_VALUE_MISMATCH",
                    "DECLARATION_RECORDS_NOT_MAPPING",
                    "DECLARATION_RECORD_NOT_MAPPING",
                    "DECLARATION_BASIS_ITEMS_INVALID",
                ),
            ),
            (
                "excessive_text_length",
                (
                    "REQUEST_VALUE_MISMATCH",
                    "DECLARATION_RECORDS_NOT_MAPPING",
                    "DECLARATION_RECORD_NOT_MAPPING",
                    "DECLARATION_BASIS_ITEMS_INVALID",
                ),
            ),
            ("empty_basis_references", "DECLARATION_BASIS_REFERENCES_INVALID"),
            ("invalid_basis_reference", "DECLARATION_BASIS_REFERENCES_INVALID"),
            ("invalid_declarant_reference", "DECLARANT_REFERENCE_INVALID"),
            ("invalid_evaluator_reference", "EVALUATOR_REFERENCE_INVALID"),
            ("missing_support_map", "DECLARATION_RECORD_NOT_MAPPING"),
            ("extra_support_key", "DECLARATION_RULE_INPUTS_INVALID"),
            ("non_boolean_support", "DECLARATION_RULE_INPUTS_INVALID"),
            ("missing_contradiction_map", "DECLARATION_RECORD_NOT_MAPPING"),
            ("extra_contradiction_key", "DECLARATION_RULE_INPUTS_INVALID"),
            ("non_boolean_contradiction", "DECLARATION_RULE_INPUTS_INVALID"),
            ("missing_unresolved_map", "DECLARATION_RECORD_NOT_MAPPING"),
            ("extra_unresolved_key", "DECLARATION_RULE_INPUTS_INVALID"),
            ("non_boolean_unresolved", "DECLARATION_RULE_INPUTS_INVALID"),
            (
                "missing_basis_nonclaim",
                "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "flipped_basis_nonclaim",
                "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            (
                "wrong_non_conversion_statement",
                "DECLARATION_NON_CONVERSION_STATEMENT_MISMATCH",
            ),
            (
                "non_boolean_source_body_authored",
                "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
            ),
            (
                "non_boolean_independent_preparer_claimed",
                "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
            ),
            (
                "non_boolean_separate_custody_claimed",
                "DECLARATION_AUTHORSHIP_POSTURE_INVALID",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for label, expected_code in cases:
                with self.subTest(case=label):
                    result = self.invoke(
                        self.request_with_records(mutate(label)),
                        root=root,
                    )
                    if label == "missing_dimension":
                        self.assert_incomplete(result, 7)
                    else:
                        self.assert_blocked(result, expected_code)

    def test_false_independence_and_custody_claims_block(self) -> None:
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        cases: list[tuple[str, dict[str, dict[str, object]], str]] = []

        independent = self.valid_declaration_records()
        independent[first]["independent_preparer_claimed"] = True
        cases.append(
            (
                "source_body_independence",
                independent,
                "FALSE_INDEPENDENT_PREPARER_CLAIM",
            )
        )
        custody = self.valid_declaration_records()
        custody[first]["separate_custody_claimed_by_preparer"] = True
        cases.append(
            (
                "source_body_custody",
                custody,
                "FALSE_SEPARATE_CUSTODY_CLAIM",
            )
        )
        non_source_independent = self.valid_declaration_records(
            source_body_authored=False
        )
        non_source_independent[first]["independent_preparer_claimed"] = True
        cases.append(
            (
                "non_source_independence",
                non_source_independent,
                "FALSE_INDEPENDENT_PREPARER_CLAIM",
            )
        )
        repository_custody = self.valid_declaration_records(
            source_body_authored=False
        )
        repository_custody[first]["basis_references"][0][
            "repository_path"
        ] = "synthetic/declaration.json"
        repository_custody[first][
            "separate_custody_claimed_by_preparer"
        ] = True
        cases.append(
            (
                "repository_path_custody",
                repository_custody,
                "FALSE_SEPARATE_CUSTODY_CLAIM",
            )
        )
        separate_file_custody = self.valid_declaration_records(
            source_body_authored=False
        )
        separate_file_custody[first]["basis_references"][0][
            "separate_file_exists"
        ] = True
        separate_file_custody[first][
            "separate_custody_claimed_by_preparer"
        ] = True
        cases.append(
            (
                "separate_file_custody",
                separate_file_custody,
                "FALSE_SEPARATE_CUSTODY_CLAIM",
            )
        )
        reference_independence = self.valid_declaration_records(
            source_body_authored=False
        )
        reference_independence[first]["declarant_reference"][
            "independence_basis"
        ] = "reference-only"
        reference_independence[first]["evaluator_reference"][
            "independence_basis"
        ] = "reference-only"
        reference_independence[first]["independent_preparer_claimed"] = True
        cases.append(
            (
                "reference_independence",
                reference_independence,
                "FALSE_INDEPENDENT_PREPARER_CLAIM",
            )
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for label, records, expected in cases:
                with self.subTest(case=label):
                    self.assert_blocked(
                        self.invoke(self.request_with_records(records), root=root),
                        expected,
                    )

    def test_rule_input_declarations_do_not_become_results(self) -> None:
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        keys = resolver.DIMENSION_RULE_KEYS[first]
        combinations = (
            (True, False, False),
            (False, False, False),
            (True, True, False),
            (True, False, True),
            (False, True, True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for support, contradiction, unresolved in combinations:
                with self.subTest(
                    support=support,
                    contradiction=contradiction,
                    unresolved=unresolved,
                ):
                    records = self.valid_declaration_records()
                    records[first]["support_postures"][keys["support"]] = support
                    records[first]["contradiction_postures"][
                        keys["contradiction"]
                    ] = contradiction
                    records[first]["unresolved_postures"][
                        keys["unresolved"]
                    ] = unresolved
                    result = self.invoke(
                        self.request_with_records(records),
                        root=root,
                    )
                    self.assert_ready(result, source_body_count=8)
                    serialized = json.dumps(
                        result,
                        sort_keys=True,
                        ensure_ascii=True,
                    )
                    for result_label in (
                        '"SATISFIED"',
                        '"NOT_SATISFIED"',
                        '"INDETERMINATE"',
                    ):
                        self.assertNotIn(result_label, serialized)

    def test_upstream_waiting_operation_validation_matrix(self) -> None:
        first_dimension = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]

        def change_root(
            artifact: dict[str, object],
            field: str,
            value: object,
        ) -> None:
            artifact[field] = value

        def change_operation(
            artifact: dict[str, object],
            field: str,
            value: object,
        ) -> None:
            artifact[
                "receiver_side_answerable_basis_candidate_sufficiency_operation"
            ][field] = value

        def change_summary(
            artifact: dict[str, object],
            field: str,
            value: object,
        ) -> None:
            artifact[
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "operation_summary"
            ][field] = value

        def change_dimension(
            artifact: dict[str, object],
            field: str,
            value: object,
        ) -> None:
            artifact[
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "operation_dimensions"
            ][first_dimension][field] = value

        cases: list[
            tuple[
                str,
                callable,
                str,
            ]
        ] = [
            (
                "wrong_resolver",
                lambda artifact: change_root(
                    artifact, "resolver_module", "wrong"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_result_version",
                lambda artifact: change_root(
                    artifact, "result_version", "0.0.0"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_outcome",
                lambda artifact: change_root(artifact, "outcome", "wrong"),
                "UPSTREAM_OPERATION_NOT_WAITING_FOR_BASIS",
            ),
            (
                "failed_checks",
                lambda artifact: change_root(
                    artifact, "failed_check_count", 1
                ),
                "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
            ),
            (
                "wrong_operation_result",
                lambda artifact: change_operation(
                    artifact, "operation_result", "wrong"
                ),
                "UPSTREAM_OPERATION_RESULT_MISMATCH",
            ),
            (
                "wrong_operation_id",
                lambda artifact: change_operation(
                    artifact, "operation_id", "wrong"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_operation_type",
                lambda artifact: change_operation(
                    artifact, "operation_type", "wrong"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_operation_version",
                lambda artifact: change_operation(
                    artifact, "operation_version", "0.0.0"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_operation_scope",
                lambda artifact: change_operation(
                    artifact, "operation_scope", "wrong"
                ),
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "wrong_candidate_identity",
                lambda artifact: change_operation(
                    artifact,
                    "receiver_side_answerable_basis_candidate_id",
                    "wrong",
                ),
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "wrong_boundary_identity",
                lambda artifact: change_operation(
                    artifact,
                    "selected_candidate_sufficiency_boundary_id",
                    "wrong",
                ),
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "boundary_not_validated",
                lambda artifact: change_summary(
                    artifact, "upstream_boundary_validated", False
                ),
                "UPSTREAM_BOUNDARY_NOT_VALIDATED",
            ),
            (
                "basis_supplied",
                lambda artifact: change_operation(
                    artifact, "sufficiency_basis_supplied", True
                ),
                "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_COMPLETE",
            ),
            (
                "basis_complete",
                lambda artifact: change_operation(
                    artifact, "sufficiency_basis_complete", True
                ),
                "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_COMPLETE",
            ),
            (
                "atomic_gate_passed",
                lambda artifact: change_operation(
                    artifact, "atomic_sufficiency_basis_gate_passed", True
                ),
                "UPSTREAM_ATOMIC_GATE_ALREADY_PASSED",
            ),
            (
                "operation_recorded",
                lambda artifact: change_operation(
                    artifact, "candidate_sufficiency_operation_recorded", True
                ),
                "UPSTREAM_OPERATION_ALREADY_RECORDED",
            ),
            (
                "operation_result_recorded",
                lambda artifact: change_operation(
                    artifact,
                    "candidate_sufficiency_operation_result_recorded",
                    True,
                ),
                "UPSTREAM_OPERATION_RESULT_ALREADY_RECORDED",
            ),
            (
                "operation_exhausted",
                lambda artifact: change_operation(
                    artifact, "candidate_sufficiency_operation_exhausted", True
                ),
                "UPSTREAM_OPERATION_ALREADY_EXHAUSTED",
            ),
            (
                "candidate_result_present",
                lambda artifact: change_operation(
                    artifact,
                    "receiver_side_answerable_basis_candidate_sufficient",
                    True,
                ),
                "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            ),
            (
                "dimension_evaluated",
                lambda artifact: change_dimension(
                    artifact, "dimension_evaluated", True
                ),
                "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            ),
            (
                "dimension_established",
                lambda artifact: change_dimension(
                    artifact, "dimension_established", True
                ),
                "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            ),
            (
                "dimension_result_present",
                lambda artifact: change_dimension(
                    artifact, "dimension_result", "SATISFIED"
                ),
                "UPSTREAM_DIMENSION_ALREADY_EVALUATED",
            ),
            (
                "receiver_posture_present",
                lambda artifact: change_operation(
                    artifact, "receiver_attestation_created", True
                ),
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "receipt_posture_present",
                lambda artifact: change_operation(
                    artifact, "receiver_answerable_receipt_present", True
                ),
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "presence_posture_present",
                lambda artifact: change_operation(
                    artifact, "presence_supported", True
                ),
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "rerun_posture_present",
                lambda artifact: change_operation(
                    artifact,
                    "same_candidate_sufficiency_operation_rerun_authorized",
                    True,
                ),
                "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "retry_posture_present",
                lambda artifact: change_operation(
                    artifact,
                    "automatic_candidate_sufficiency_operation_retry_created",
                    True,
                ),
                "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "debt_posture_present",
                lambda artifact: change_operation(
                    artifact,
                    "candidate_sufficiency_operation_debt_created",
                    True,
                ),
                "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "obligation_posture_present",
                lambda artifact: change_operation(
                    artifact,
                    "candidate_sufficiency_operation_obligation_created",
                    True,
                ),
                "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "downstream_posture_present",
                lambda artifact: change_operation(
                    artifact, "authority_created", True
                ),
                "UPSTREAM_RERUN_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "stale_open_state",
                lambda artifact: artifact.__setitem__(
                    "what_remains_open",
                    list(resolver.WAITING_WHAT_REMAINS_OPEN[1:]),
                ),
                "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
            ),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            specification = self.synthetic_governing_declaration_specification()
            request = self.canonical_incomplete_request()
            for label, mutate, expected in cases:
                with self.subTest(case=label):
                    case_root = root / label
                    artifact = self.synthetic_valid_waiting_operation_artifact()
                    mutate(artifact)
                    self.fixture_root(
                        case_root,
                        specification=specification,
                        waiting_artifact=artifact,
                    )
                    self.assert_blocked(
                        self.invoke(request, root=case_root),
                        expected,
                    )

    def test_request_validation_and_preclaims(self) -> None:
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min(
                []
            ),
            "REQUEST_NOT_MAPPING",
        )
        request_cases = (
            ("intent", "UNSUPPORTED", "UNSUPPORTED_INTENT"),
            (
                "receiver_side_answerable_basis_candidate_sufficiency_basis_"
                "declaration_id",
                "wrong",
                "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_sufficiency_operation_id",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "receiver_side_answerable_basis_candidate_id",
                "wrong",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_sufficiency_boundary_id",
                "wrong",
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "governing_declaration_specification_path",
                "alternate/spec.md",
                "REQUEST_VALUE_MISMATCH",
            ),
            (
                "selected_waiting_operation_artifact_path",
                "alternate/artifact.json",
                "REQUEST_VALUE_MISMATCH",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for field, value, expected in request_cases:
                with self.subTest(field=field):
                    request = self.canonical_incomplete_request()
                    request[field] = value
                    self.assert_blocked(
                        self.invoke(request, root=root),
                        expected,
                    )

            malformed_nonclaims = self.canonical_incomplete_request()
            malformed_nonclaims["declared_non_claims"] = None
            self.assert_blocked(
                self.invoke(malformed_nonclaims, root=root),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
            inconsistent = self.canonical_incomplete_request()
            inconsistent["declaration_records"] = (
                self.valid_declaration_records()
            )
            self.assert_blocked(
                self.invoke(inconsistent, root=root),
                "REQUEST_VALUE_MISMATCH",
            )
            copied_artifact = self.canonical_incomplete_request()
            copied_artifact["selected_waiting_operation_artifact"] = (
                self.synthetic_valid_waiting_operation_artifact()
            )
            self.assert_blocked(
                self.invoke(copied_artifact, root=root),
                "REQUEST_VALUE_MISMATCH",
            )
            for field, value, expected in (
                ("outcome", resolver.OUTCOME_RECORDED, "DECLARATION_RESULT_PRECLAIMED"),
                (
                    "declaration_result",
                    resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
                    "DECLARATION_RESULT_PRECLAIMED",
                ),
                (
                    "dimension_result",
                    "SATISFIED",
                    "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
                ),
                (
                    "candidate_result",
                    "candidate_sufficient",
                    "PROHIBITED_DIMENSION_OR_CANDIDATE_RESULT_REQUESTED",
                ),
            ):
                with self.subTest(caller_preclaim=field):
                    request = self.canonical_incomplete_request()
                    request[field] = value
                    self.assert_blocked(
                        self.invoke(request, root=root),
                        expected,
                    )

    def test_incoming_record_preclaims_block(self) -> None:
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        categories = (
            (
                resolver.DECLARATION_RESULT_PRECLAIM_FIELDS,
                "DECLARATION_RESULT_PRECLAIMED",
            ),
            (
                resolver.SUPPLY_EXECUTION_PRECLAIM_FIELDS,
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                resolver.DIMENSION_CANDIDATE_PRECLAIM_FIELDS,
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                resolver.RECEIVER_PRESENCE_PRECLAIM_FIELDS,
                "PROHIBITED_RECEIVER_RECEIPT_OR_PRESENCE_REQUESTED",
            ),
            (
                resolver.DOWNSTREAM_PRECLAIM_FIELDS,
                "PROHIBITED_DOWNSTREAM_CONVERSION_REQUESTED",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for fields, expected in categories:
                for field in fields:
                    with self.subTest(field=field):
                        records = self.valid_declaration_records()
                        records[first][field] = True
                        self.assert_blocked(
                            self.invoke(
                                self.request_with_records(records),
                                root=root,
                            ),
                            expected,
                        )

    def test_declaration_level_nonclaims_canonicalization(self) -> None:
        canonical = self.canonical_incomplete_request()
        self.assertEqual(
            set(canonical["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                canonical["declared_non_claims"][key] is False
                for key in resolver.REQUIRED_FALSE_NON_CLAIMS
            )
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(flipped=key):
                    request = self.canonical_incomplete_request()
                    request["declared_non_claims"][key] = True
                    result = self.invoke(request, root=root)
                    self.assert_blocked(
                        result,
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )
                    self.assertIs(result["non_claims"][key], False)
            first = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            for label, value in (
                ("missing", object()),
                ("none", None),
                ("zero", 0),
                ("string_false", "false"),
            ):
                with self.subTest(malformed=label):
                    request = self.canonical_incomplete_request()
                    if label == "missing":
                        request["declared_non_claims"].pop(first)
                    else:
                        request["declared_non_claims"][first] = value
                    self.assert_blocked(
                        self.invoke(request, root=root),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_basis_record_nonclaims_canonicalization(self) -> None:
        first_dimension = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for key in resolver.REQUIRED_BASIS_NON_CLAIMS:
                for label, value in (
                    ("missing", object()),
                    ("true", True),
                    ("none", None),
                    ("zero", 0),
                    ("string_false", "false"),
                ):
                    with self.subTest(key=key, malformed=label):
                        records = self.valid_declaration_records()
                        non_claims = records[first_dimension][
                            "basis_non_claims"
                        ]
                        if label == "missing":
                            non_claims.pop(key)
                        else:
                            non_claims[key] = value
                        self.assert_blocked(
                            self.invoke(
                                self.request_with_records(records),
                                root=root,
                            ),
                            "DECLARATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
                        )

    def test_every_prohibited_request_flag_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=field):
                    request = self.canonical_incomplete_request()
                    request[field] = True
                    result = self.invoke(request, root=root)
                    self.assert_blocked(result, expected_code)

    def test_do_not_record_and_explicit_block(self) -> None:
        not_recorded = self.resolve_synthetic(
            self.canonical_incomplete_request(
                intent=resolver.INTENT_DO_NOT_RECORD
            )
        )
        self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertEqual(
            self.declaration_result(not_recorded),
            resolver.DECLARATION_RESULT_NOT_EVALUATED,
        )
        self.assertEqual(self.failed_check_count(not_recorded), 0)
        declaration = self.declaration(not_recorded)
        self.assertIs(
            declaration[
                "candidate_sufficiency_basis_declaration_recorded"
            ],
            False,
        )
        self.assertIs(
            declaration[
                "candidate_sufficiency_basis_declaration_result_recorded"
            ],
            False,
        )
        self.assertIs(
            declaration[
                "candidate_sufficiency_basis_declaration_ready_for_supply"
            ],
            False,
        )
        self.assert_supply_result_and_downstream_locks(not_recorded)

        blocked = self.resolve_synthetic(
            self.canonical_incomplete_request(intent=resolver.INTENT_BLOCK)
        )
        self.assert_blocked(blocked, "EXPLICIT_BLOCK_REQUESTED")

    def test_result_structure_and_declaration_wrapper_separation(self) -> None:
        result = self.resolve_synthetic(
            self.request_with_records(self.valid_declaration_records())
        )
        self.assert_ready(result, source_body_count=8)
        self.assertEqual(set(result), set(resolver.RESULT_SECTIONS))
        self.assert_declaration_has_no_wrapper_fields(result)
        for section in (
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_metadata",
            "declared_receiver_side_answerable_basis_candidate_sufficiency_"
            "basis_declaration_basis",
            "upstream_basis",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_records",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_checks",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_statement",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_non_meaning",
            "declaration_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_summary",
            "resolver_module",
            "result_version",
        ):
            self.assertIn(section, result)

    def test_bounded_declaration_material_omission_and_summary_shape(self) -> None:
        result = self.resolve_synthetic(
            self.request_with_records(self.valid_declaration_records())
        )
        self.assert_ready(result, source_body_count=8)
        summaries = result[
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_records"
        ]["record_summaries"]
        expected_fields = {
            "dimension_id",
            "basis_item_count",
            "basis_reference_count",
            "declarant_reference_supplied",
            "evaluator_reference_supplied",
            "support_key_names",
            "contradiction_key_names",
            "unresolved_key_names",
            "basis_non_claims_validated",
            "receiver_side_answerable_basis_candidate_id",
            "selected_candidate_sufficiency_boundary_id",
            "selected_candidate_sufficiency_operation_id",
            "source_body_authored",
            "independent_preparer_claimed",
            "separate_custody_claimed_by_preparer",
            "complete_declaration_record_omitted",
        }
        self.assertEqual(
            tuple(summaries),
            resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS,
        )
        for dimension_id, summary in summaries.items():
            self.assertEqual(set(summary), expected_fields, dimension_id)
            self.assertEqual(summary["basis_item_count"], 1)
            self.assertEqual(summary["basis_reference_count"], 1)
            self.assertIs(summary["declarant_reference_supplied"], True)
            self.assertIs(summary["evaluator_reference_supplied"], True)
            self.assertIs(summary["basis_non_claims_validated"], True)
            self.assertIs(summary["complete_declaration_record_omitted"], True)
        self.assert_complete_declaration_material_omitted(result)

    def test_branch_relative_open_state_and_summary_behavior(self) -> None:
        results = (
            (
                self.resolve_synthetic(self.canonical_incomplete_request()),
                resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION,
                resolver.DECLARATION_RESULT_REQUIRES_COMPLETE,
                resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(
                    self.request_with_records(
                        self.valid_declaration_records()
                    )
                ),
                resolver.OUTCOME_RECORDED,
                resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
                resolver.READY_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(
                    self.canonical_incomplete_request(
                        intent=resolver.INTENT_BLOCK
                    )
                ),
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
                resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
            ),
            (
                self.resolve_synthetic(
                    self.canonical_incomplete_request(
                        intent=resolver.INTENT_DO_NOT_RECORD
                    )
                ),
                resolver.OUTCOME_NOT_RECORDED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
                resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
            ),
        )
        required_summary_fields = {
            "outcome",
            "declaration_result",
            "failed_check_count",
            "passed_check_count",
            "resolver_module",
            "result_version",
            "declaration_identity",
            "selected_identity",
            "upstream_waiting_operation_validated",
            "declaration_records_supplied",
            "declaration_complete",
            "declaration_record_count",
            "declaration_dimension_ids",
            "declaration_ready_for_supply",
            "supply_admission_execution_exhaustion_postures",
            "authorship_posture_counts",
            "candidate_receiver_receipt_presence_route_and_downstream_locks_false",
            "complete_declaration_content_omitted",
            "governing_paths",
            "marker_validation",
            "non_claims_canonical_false",
        }
        for result, outcome, declaration_result, expected_open in results:
            with self.subTest(outcome=outcome):
                self.assertEqual(result["outcome"], outcome)
                self.assertEqual(
                    self.declaration_result(result),
                    declaration_result,
                )
                self.assertEqual(
                    tuple(result["what_remains_open"]),
                    expected_open,
                )
                summary = (
                    resolver.build_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(
                    summary,
                    result[
                        "receiver_side_answerable_basis_candidate_"
                        "sufficiency_basis_declaration_summary"
                    ],
                )
                self.assertTrue(required_summary_fields.issubset(summary))
                self.assertTrue(
                    all(
                        value is False
                        for value in summary[
                            "supply_admission_execution_exhaustion_postures"
                        ].values()
                    )
                )
                if outcome == resolver.OUTCOME_RECORDED:
                    self.assertNotIn(
                        "complete eight-record candidate-sufficiency basis "
                        "declaration",
                        result["what_remains_open"],
                    )
                else:
                    self.assertIs(
                        self.declaration(result)["declaration_complete"],
                        False,
                    )

    def test_from_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            incomplete_path = self._write_json(
                root / "requests" / "incomplete.json",
                self.canonical_incomplete_request(),
            )
            ready_path = self._write_json(
                root / "requests" / "ready.json",
                self.request_with_records(self.valid_declaration_records()),
            )
            with patch.object(resolver, "REPO_ROOT", root):
                incomplete = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_from_path(
                        incomplete_path
                    )
                )
                ready = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_from_path(
                        ready_path
                    )
                )
            self.assert_incomplete(incomplete, 0)
            self.assert_ready(ready, source_body_count=8)
            malformed_path = self._write_text(
                root / "requests" / "malformed.json",
                "{",
            )
            array_path = self._write_json(
                root / "requests" / "array.json",
                [],
            )
            for path in (
                malformed_path,
                array_path,
                root / "requests" / "missing.json",
            ):
                with self.subTest(path=path.name):
                    with patch.object(resolver, "REPO_ROOT", root):
                        result = (
                            resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_from_path(
                                path
                            )
                        )
                    self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_write_behavior_and_validation(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="bounded_sufficiency_declaration_"
        ) as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            incomplete = self.invoke(
                self.canonical_incomplete_request(),
                root=root,
            )
            ready = self.invoke(
                self.request_with_records(self.valid_declaration_records()),
                root=root,
            )
            blocked = self.invoke(
                self.canonical_incomplete_request(intent=resolver.INTENT_BLOCK),
                root=root,
            )
            not_recorded = self.invoke(
                self.canonical_incomplete_request(
                    intent=resolver.INTENT_DO_NOT_RECORD
                ),
                root=root,
            )
            outputs = root / "outputs"
            for name, result in (
                ("incomplete", incomplete),
                ("ready", ready),
                ("blocked", blocked),
                ("not_recorded", not_recorded),
            ):
                with self.subTest(write=name):
                    target = self.safe_temporary_output_path(outputs, name)
                    written = (
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
                            result,
                            target,
                        )
                    )
                    self.assertEqual(written, target)
                    self.assertTrue(written.is_file())
                    parsed = json.loads(written.read_text(encoding="utf-8"))
                    self.assertEqual(
                        parsed["resolver_module"],
                        resolver.RESOLVER_MODULE,
                    )
                    self.assertEqual(
                        parsed["result_version"],
                        resolver.RESULT_VERSION,
                    )
                    self.assertEqual(parsed["outcome"], result["outcome"])
                    self.assertEqual(
                        self.declaration_result(parsed),
                        self.declaration_result(result),
                    )
                    self.assert_required_false_non_claims(parsed)
                    self.assert_supply_result_and_downstream_locks(parsed)
                    self.assert_complete_declaration_material_omitted(parsed)

            ready_target = self.safe_temporary_output_path(outputs, "ready")
            suffixed = (
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
                    ready,
                    ready_target,
                )
            )
            self.assertEqual(
                suffixed.name,
                ready_target.stem + "_001" + ready_target.suffix,
            )
            default_output_root = root / (
                "integrity_host_v0_min_coexistence_receiver_side_answerable_"
                "basis_candidate_sufficiency_basis_declaration_v0_min"
            )
            with patch.object(resolver, "OUTPUT_ROOT", default_output_root):
                default_written = (
                    resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
                        incomplete
                    )
                )
            self.assertEqual(default_written.parent, default_output_root)
            self.assertEqual(default_written.name, resolver.OUTPUT_FILENAME)

            forbidden_paths = (
                root / "tests" / resolver.OUTPUT_FILENAME,
                root / "spec" / resolver.OUTPUT_FILENAME,
                root
                / (
                    "integrity_host_v0_min_coexistence_receiver_side_"
                    "answerable_basis_candidate_sufficiency_operation_v0_min"
                )
                / resolver.OUTPUT_FILENAME,
                root
                / (
                    "integrity_host_v0_min_coexistence_receiver_side_"
                    "answerable_basis_candidate_sufficiency_boundary_v0_min"
                )
                / resolver.OUTPUT_FILENAME,
                root
                / (
                    "integrity_host_v0_min_coexistence_receiver_side_"
                    "answerable_basis_candidate_evaluation_operation_v0_min_v3"
                )
                / resolver.OUTPUT_FILENAME,
                root / "runtime" / resolver.OUTPUT_FILENAME,
                root / "api" / resolver.OUTPUT_FILENAME,
                root / "presence" / resolver.OUTPUT_FILENAME,
            )
            for path in forbidden_paths:
                with self.subTest(forbidden=path.parent.name):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
                            ready,
                            path,
                        )

            malformed_results: list[tuple[str, object]] = [("not_mapping", [])]
            wrong_module = self.clone(ready)
            wrong_module["resolver_module"] = "wrong"
            malformed_results.append(("wrong_module", wrong_module))
            wrong_version = self.clone(ready)
            wrong_version["result_version"] = "0.0.0"
            malformed_results.append(("wrong_version", wrong_version))
            wrong_outcome = self.clone(ready)
            wrong_outcome["outcome"] = "unsupported"
            malformed_results.append(("wrong_outcome", wrong_outcome))
            missing_section = self.clone(ready)
            missing_section.pop("declaration_result_detail")
            malformed_results.append(("missing_section", missing_section))
            branch_mismatch = self.clone(ready)
            branch_mismatch["outcome"] = (
                resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION
            )
            malformed_results.append(("branch_mismatch", branch_mismatch))
            flipped_nonclaim = self.clone(ready)
            flipped_nonclaim["non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ] = True
            malformed_results.append(("flipped_nonclaim", flipped_nonclaim))
            copied_material = self.clone(ready)
            copied_material[
                "declared_receiver_side_answerable_basis_candidate_"
                "sufficiency_basis_declaration_basis"
            ]["basis_items"] = [{"forbidden": True}]
            malformed_results.append(("copied_material", copied_material))
            copied_waiting = self.clone(ready)
            copied_waiting["upstream_basis"][
                "selected_waiting_operation_artifact"
            ] = self.synthetic_valid_waiting_operation_artifact()
            malformed_results.append(("copied_waiting", copied_waiting))
            record_count_mismatch = self.clone(ready)
            record_count_mismatch[
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "basis_declaration_records"
            ]["declaration_record_count"] = 7
            malformed_results.append(
                ("record_count_mismatch", record_count_mismatch)
            )
            readiness_mismatch = self.clone(ready)
            readiness_mismatch[
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "basis_declaration"
            ]["candidate_sufficiency_basis_declaration_ready_for_supply"] = False
            malformed_results.append(("readiness_mismatch", readiness_mismatch))
            for name, malformed in malformed_results:
                with self.subTest(refused=name):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBasisDeclarationV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_declaration_v0_min_result(
                            malformed,
                            self.safe_temporary_output_path(
                                outputs,
                                "refused_" + name,
                            ),
                        )

    def test_non_mutation_and_lineage_preservation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            specification = self.synthetic_governing_declaration_specification()
            artifact = self.synthetic_valid_waiting_operation_artifact()
            records = self.valid_declaration_records()
            request = self.request_with_records(records)
            specification_before = specification
            artifact_before = self.clone(artifact)
            records_before = self.clone(records)
            request_before = self.clone(request)
            self.fixture_root(
                root,
                specification=specification,
                waiting_artifact=artifact,
            )
            result = self.invoke(request, root=root)
            self.assert_ready(result, source_body_count=8)
            self.assertEqual(specification, specification_before)
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(records, records_before)
            self.assertEqual(request, request_before)
            on_disk_artifact = json.loads(
                (
                    root
                    / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
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
        first = resolver.SUFFICIENCY_DECLARATION_DIMENSION_IDS[0]
        partial = self.valid_declaration_records()
        partial.pop(first)
        malformed = self.valid_declaration_records()
        malformed[first]["basis_items"] = []
        false_independence = self.valid_declaration_records()
        false_independence[first]["independent_preparer_claimed"] = True
        false_custody = self.valid_declaration_records()
        false_custody[first][
            "separate_custody_claimed_by_preparer"
        ] = True
        preclaim = self.canonical_incomplete_request()
        preclaim["declaration_result"] = (
            resolver.DECLARATION_RESULT_READY_FOR_SUPPLY
        )
        separate_supply = self.canonical_incomplete_request()
        separate_supply["request_basis_separate_supply"] = True
        matrix = (
            (
                "incomplete",
                self.canonical_incomplete_request(),
                resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION,
                resolver.DECLARATION_RESULT_REQUIRES_COMPLETE,
            ),
            (
                "ready_source_body",
                self.request_with_records(self.valid_declaration_records()),
                resolver.OUTCOME_RECORDED,
                resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
            ),
            (
                "ready_non_source_body",
                self.request_with_records(
                    self.valid_declaration_records(
                        source_body_authored=False
                    )
                ),
                resolver.OUTCOME_RECORDED,
                resolver.DECLARATION_RESULT_READY_FOR_SUPPLY,
            ),
            (
                "partial",
                self.request_with_records(partial),
                resolver.OUTCOME_REQUIRES_COMPLETE_DECLARATION,
                resolver.DECLARATION_RESULT_REQUIRES_COMPLETE,
            ),
            (
                "malformed",
                self.request_with_records(malformed),
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "false_independence",
                self.request_with_records(false_independence),
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "false_custody",
                self.request_with_records(false_custody),
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "result_preclaim",
                preclaim,
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "separate_supply",
                separate_supply,
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "blocked_intent",
                self.canonical_incomplete_request(intent=resolver.INTENT_BLOCK),
                resolver.OUTCOME_BLOCKED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
            (
                "not_recorded",
                self.canonical_incomplete_request(
                    intent=resolver.INTENT_DO_NOT_RECORD
                ),
                resolver.OUTCOME_NOT_RECORDED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for name, request, expected_outcome, expected_result in matrix:
                with self.subTest(case=name):
                    result = self.invoke(request, root=root)
                    self.assertEqual(result["outcome"], expected_outcome)
                    self.assertEqual(
                        self.declaration_result(result),
                        expected_result,
                    )
                    self.assert_supply_result_and_downstream_locks(result)
                    self.assert_complete_declaration_material_omitted(result)
                    self.assert_all_emitted_codes_public(result)
                    ready = expected_outcome == resolver.OUTCOME_RECORDED
                    self.assertIs(
                        self.declaration(result)[
                            "candidate_sufficiency_basis_declaration_"
                            "ready_for_supply"
                        ],
                        ready,
                    )


if __name__ == "__main__":
    unittest.main()
