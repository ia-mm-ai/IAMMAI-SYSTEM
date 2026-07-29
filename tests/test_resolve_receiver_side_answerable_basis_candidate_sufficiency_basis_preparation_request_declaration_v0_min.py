"""Tests for one bounded candidate-sufficiency preparation request.

The suite proves that absent or clean partial request material is lawful
waiting and that one exact complete request records request posture only. It
never performs preparation, creates declaration records, establishes
readiness, supplies or admits basis, executes the operation, or derives a
dimension or candidate result.
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

import resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min as resolver


PREFIX = (
    "receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "preparation_request_declaration"
)
GOVERNING_SPEC_PATH = REPO_ROOT / resolver.PREPARATION_REQUEST_SPEC_RELATIVE_PATH
LIVE_INCOMPLETE_ARTIFACT_PATH = (
    REPO_ROOT / resolver.SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH
)
TARGET_RESOLVER_PATH = REPO_ROOT / (
    "src/resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_"
    "preparation_request_declaration_v0_min.py"
)
DECLARATION_TERMINAL_SUMMARY_PATH = REPO_ROOT / (
    "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_BASIS_"
    "DECLARATION_TERMINAL_SUMMARY_V0.md"
)
WAITING_SUFFICIENCY_OPERATION_ARTIFACT_PATH = REPO_ROOT / (
    "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_"
    "basis_candidate_sufficiency_operation_v0_min/"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_001__"
    "receiver_side_answerable_basis_candidate_sufficiency_operation_"
    "v0_min_result.json"
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


class CandidateSufficiencyBasisPreparationRequestDeclarationTests(
    unittest.TestCase
):
    """Validate request recording without preparation or later conversion."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = tuple(
            path
            for path in (
                TARGET_RESOLVER_PATH,
                GOVERNING_SPEC_PATH,
                LIVE_INCOMPLETE_ARTIFACT_PATH,
                DECLARATION_TERMINAL_SUMMARY_PATH,
                WAITING_SUFFICIENCY_OPERATION_ARTIFACT_PATH,
                SUFFICIENCY_BOUNDARY_ARTIFACT_PATH,
                V3_EVALUATION_ARTIFACT_PATH,
                V2_WAITING_ARTIFACT_PATH,
                V2_COMPLETED_ARTIFACT_PATH,
            )
            if path.is_file()
        )
        cls.preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in cls.preserved_paths
        }

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
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
        self.assertFalse(path.is_dir(), f"fixture path collision: {path}")
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

    def load_selected_live_incomplete_declaration_artifact(
        self,
    ) -> dict[str, object]:
        value = json.loads(
            LIVE_INCOMPLETE_ARTIFACT_PATH.read_text(encoding="utf-8")
        )
        self.assertIsInstance(value, dict)
        return self.clone(value)

    def synthetic_governing_specification(self) -> str:
        markers: list[str] = []
        for marker_class in resolver.PREPARATION_REQUEST_SPEC_MARKER_CLASSES.values():
            markers.extend(marker_class)
        markers.extend(
            (
                resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
                resolver.CANDIDATE_ID,
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID,
                resolver.SELECTED_RECEPTION_OPERATION_ID,
                resolver.SELECTED_EVALUATION_BOUNDARY_ID,
                resolver.SELECTED_EVALUATION_OPERATION_ID,
                "Requested preparer is not preparer performance.",
                "Source-body preparation requested is not independent custody.",
                "Preparer reference is not authority, identity, standing, or truth.",
                "Request recorded is not declaration readiness.",
                "Request recorded is not operation authorization.",
                "Request existence is not debt or obligation.",
                "Later preparation remains separately performed.",
            )
        )
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def synthetic_valid_incomplete_declaration_artifact(
        self,
    ) -> dict[str, object]:
        declaration: dict[str, object] = {
            "declaration_id": resolver.SELECTED_DECLARATION_ID,
            "declaration_type": resolver.SELECTED_DECLARATION_TYPE,
            "declaration_version": resolver.SELECTED_DECLARATION_VERSION,
            "declaration_scope": resolver.SELECTED_DECLARATION_SCOPE,
            "declaration_result": resolver.SELECTED_DECLARATION_RESULT_REQUIRED,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_id": resolver.SELECTED_DECLARATION_ID,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_type": resolver.SELECTED_DECLARATION_TYPE,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_version": resolver.SELECTED_DECLARATION_VERSION,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_scope": resolver.SELECTED_DECLARATION_SCOPE,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_result": resolver.SELECTED_DECLARATION_RESULT_REQUIRED,
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "selected_candidate_sufficiency_boundary_id": (
                resolver.SELECTED_SUFFICIENCY_BOUNDARY_ID
            ),
            "selected_candidate_sufficiency_operation_id": (
                resolver.SELECTED_SUFFICIENCY_OPERATION_ID
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
            "declaration_records_supplied": False,
            "declaration_record_count": 0,
            "declaration_complete": False,
            "candidate_sufficiency_basis_declaration_ready_for_supply": False,
            "candidate_sufficiency_basis_declaration_recorded": False,
            "candidate_sufficiency_basis_declaration_result_recorded": False,
            "candidate_sufficiency_basis_separately_supplied": False,
            "candidate_sufficiency_basis_admitted_by_operation": False,
            "candidate_sufficiency_operation_recorded": False,
            "candidate_sufficiency_operation_result_recorded": False,
            "candidate_sufficiency_operation_executed": False,
            "candidate_sufficiency_operation_exhausted": False,
        }
        false_fields = (
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "candidate_sufficiency_decided",
            "candidate_sufficiency_established",
            "candidate_insufficiency_established",
            "candidate_indeterminacy_established",
            "dimension_results_derived",
            "candidate_result_derived",
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
            "repeated_declaration_permission_created",
            "reusable_declaration_route_created",
            "silent_declaration_replacement_authorized",
            "automatic_redeclaration_created",
            "declaration_debt_created",
            "declaration_obligation_created",
            "candidate_sufficiency_operation_authorized",
            "candidate_sufficiency_operation_created",
            "identity_created",
            "relation_created",
            "coupling_assigned",
            "coupling_created",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "public_intake_created",
            "public_interface_created",
            "authority_created",
            "standing_created",
            "truth_created",
            "continuity_memory_written",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
        )
        declaration.update({key: False for key in false_fields})
        return {
            "resolver_module": (
                "resolve_receiver_side_answerable_basis_candidate_"
                "sufficiency_basis_declaration_v0_min"
            ),
            "result_version": resolver.RESULT_VERSION,
            "outcome": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
                "BASIS_DECLARATION_REQUIRES_COMPLETE_DECLARATION"
            ),
            "failed_check_count": 0,
            "passed_check_count": 88,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration": declaration,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration_summary": {
                "upstream_waiting_operation_validated": True,
            },
            "what_remains_open": [
                "complete eight-record candidate-sufficiency basis declaration",
                "candidate-sufficiency basis declaration live standing",
                "preparation-request declaration, if separately selected",
                "source-body preparation of the eight declaration records, "
                "if separately selected",
            ],
        }

    def fixture_root(
        self,
        root: Path,
        *,
        specification: str | None = None,
        artifact: dict[str, object] | None = None,
    ) -> tuple[Path, Path]:
        spec_path = self._write_text(
            root / resolver.PREPARATION_REQUEST_SPEC_RELATIVE_PATH,
            (
                self.synthetic_governing_specification()
                if specification is None
                else specification
            ),
        )
        artifact_path = self._write_json(
            root / resolver.SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_RELATIVE_PATH,
            self.clone(
                self.synthetic_valid_incomplete_declaration_artifact()
                if artifact is None
                else artifact
            ),
        )
        return spec_path, artifact_path

    def exact_preparer_posture(self) -> dict[str, object]:
        return {
            "preparer_reference": resolver.PREPARER_REFERENCE,
            "preparer_relation_to_source_body": (
                resolver.PREPARER_RELATION_TO_SOURCE_BODY
            ),
            "source_body_preparer": True,
            "independent_preparer_claimed": False,
            "separate_custody_claimed_by_preparer": False,
            "preparer_authority_claimed": False,
            "preparer_identity_established": False,
            "preparer_standing_claimed": False,
            "preparer_truth_claimed": False,
        }

    def canonical_incomplete_request(
        self,
        **overrides: object,
    ) -> dict[str, object]:
        return (
            resolver.build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def canonical_complete_request(
        self,
        **overrides: object,
    ) -> dict[str, object]:
        return (
            resolver.build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request(
                requested_dimension_ids=resolver.REQUESTED_PREPARATION_DIMENSION_IDS,
                preparer_posture=self.exact_preparer_posture(),
                **copy.deepcopy(overrides),
            )
        )

    def invoke(
        self,
        request: object = None,
        *,
        root: Path | None = None,
    ) -> dict[str, object]:
        supplied = self.clone(request)
        before = self.clone(supplied)
        if root is None:
            result = (
                resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_synthetic(
        self,
        request: object = None,
        *,
        specification: str | None = None,
        artifact: dict[str, object] | None = None,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            artifact_before = self.clone(artifact)
            self.fixture_root(
                root,
                specification=specification,
                artifact=artifact,
            )
            selected = (
                self.canonical_incomplete_request()
                if request is None
                else request
            )
            result = self.invoke(selected, root=root)
            self.assertEqual(artifact, artifact_before)
            return result

    def request_state(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(PREFIX)
        self.assertIsInstance(value, dict)
        return value

    def request_result(self, result: dict[str, object]) -> str:
        value = self.request_state(result).get("request_result")
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
        value = result.get(f"{PREFIX}_checks")
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
            for key in ("block_code", "failure_code"):
                if check.get(key) is not None:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(
        self,
        result: dict[str, object],
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIsInstance(non_claims[key], bool, key)
            self.assertIs(non_claims[key], False, key)

    def assert_later_postures_false(
        self,
        result: dict[str, object],
    ) -> None:
        state = self.request_state(result)
        for key in (
            "candidate_sufficiency_basis_preparation_started",
            "candidate_sufficiency_basis_preparation_completed",
            "candidate_sufficiency_basis_declaration_records_created",
            "candidate_sufficiency_basis_declaration_ready_for_supply",
            "candidate_sufficiency_basis_separately_supplied",
            "candidate_sufficiency_basis_admitted_by_operation",
            "candidate_sufficiency_operation_executed",
            "candidate_sufficiency_operation_exhausted",
        ):
            self.assertIs(state.get(key), False, key)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(state.get(key), False, key)
        detail = result.get("request_result_detail")
        self.assertIsInstance(detail, dict)
        for key in (
            "preparation_started",
            "preparation_completed",
            "declaration_records_created",
            "declaration_ready_for_supply",
            "basis_separately_supplied",
            "basis_admitted_by_operation",
            "operation_executed",
            "operation_exhausted",
            "dimension_result_exists",
            "candidate_result_exists",
        ):
            self.assertIs(detail.get(key), False, key)
        self.assert_canonical_false_non_claims(result)

    def assert_complete_upstream_payload_omitted(
        self,
        result: dict[str, object],
    ) -> None:
        upstream = result.get("upstream_basis")
        self.assertIsInstance(upstream, dict)
        if upstream:
            self.assertIs(upstream.get("complete_upstream_artifact_omitted"), True)
            self.assertIs(upstream.get("complete_upstream_checks_omitted"), True)
        forbidden = {
            "declaration_record",
            "declaration_records",
            "candidate_sufficiency_basis_declaration_records",
            "basis_item",
            "basis_items",
            "basis_reference",
            "basis_references",
            "declarant_reference",
            "evaluator_reference",
            "rule_input",
            "rule_inputs",
            "rule_input_postures",
            "support_postures",
            "contradiction_postures",
            "unresolved_postures",
            "candidate_material",
            "candidate_packet",
            "capture_material",
            "capture_packet",
            "complete_upstream_artifact",
            "upstream_artifact",
            "upstream_checks",
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

    def assert_waiting(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_REQUIRES_COMPLETE)
        self.assertEqual(
            self.request_result(result),
            resolver.REQUEST_RESULT_REQUIRES_COMPLETE,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        state = self.request_state(result)
        for key in (
            "preparation_request_complete",
            "candidate_sufficiency_basis_preparation_request_declaration_recorded",
            "candidate_sufficiency_basis_preparation_request_declaration_result_recorded",
            "candidate_sufficiency_basis_preparation_requested",
        ):
            self.assertIs(state.get(key), False, key)
        self.assertEqual(
            tuple(result.get("what_remains_open", ())),
            resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
        )
        self.assert_later_postures_false(result)
        self.assert_complete_upstream_payload_omitted(result)

    def assert_recorded(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(
            self.request_result(result),
            resolver.REQUEST_RESULT_RECORDED,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        state = self.request_state(result)
        for key in (
            "preparation_request_material_supplied",
            "preparation_request_complete",
            "candidate_sufficiency_basis_preparation_request_declaration_recorded",
            "candidate_sufficiency_basis_preparation_request_declaration_result_recorded",
            "candidate_sufficiency_basis_preparation_requested",
        ):
            self.assertIs(state.get(key), True, key)
        self.assertEqual(
            tuple(state.get("requested_dimension_ids", ())),
            resolver.REQUESTED_PREPARATION_DIMENSION_IDS,
        )
        self.assertEqual(state.get("requested_dimension_count"), 8)
        self.assertEqual(
            tuple(result.get("what_remains_open", ())),
            resolver.RECORDED_WHAT_REMAINS_OPEN,
        )
        self.assert_later_postures_false(result)
        self.assert_complete_upstream_payload_omitted(result)

    def assert_blocked(
        self,
        result: dict[str, object],
        expected_code: str | tuple[str, ...] | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            self.request_result(result),
            resolver.REQUEST_RESULT_NOT_EVALUATED,
        )
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if isinstance(expected_code, tuple):
            self.assertIn(code, expected_code)
        elif expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(self.failed_check_count(result), 0)
        state = self.request_state(result)
        self.assertIs(state.get("preparation_request_complete"), False)
        self.assertIs(
            state.get("candidate_sufficiency_basis_preparation_requested"),
            False,
        )
        self.assert_all_emitted_codes_public(result)
        self.assert_later_postures_false(result)
        self.assert_complete_upstream_payload_omitted(result)

    def test_01_public_api_and_exact_constants(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path",
            "write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result",
            "build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_summary",
            "build_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request",
            "build_declared_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected = {
            "RESULT_VERSION": "0.1.0",
            "RESOLVER_MODULE": (
                "resolve_receiver_side_answerable_basis_candidate_"
                "sufficiency_basis_preparation_request_declaration_v0_min"
            ),
            "REQUEST_ID": (
                "receiver_side_answerable_basis_candidate_sufficiency_basis_"
                "preparation_request_declaration_001"
            ),
            "REQUEST_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
                "BASIS_PREPARATION_REQUEST_DECLARATION"
            ),
            "REQUEST_VERSION": "0.1.0",
            "REQUEST_SCOPE": (
                "REQUEST_PREPARATION_OF_ONE_EXACT_EIGHT_RECORD_CANDIDATE_"
                "SUFFICIENCY_BASIS_DECLARATION_ONLY"
            ),
            "SELECTED_DECLARATION_ID": (
                "receiver_side_answerable_basis_candidate_sufficiency_basis_"
                "declaration_001"
            ),
            "SELECTED_DECLARATION_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_"
                "BASIS_DECLARATION"
            ),
            "SELECTED_DECLARATION_VERSION": "0.1.0",
            "SELECTED_DECLARATION_SCOPE": (
                "DECLARE_ONE_BOUNDED_EIGHT_DIMENSION_CANDIDATE_SUFFICIENCY_"
                "BASIS_ONLY"
            ),
            "SELECTED_DECLARATION_RESULT_REQUIRED": (
                "REQUIRES_COMPLETE_CANDIDATE_SUFFICIENCY_BASIS_DECLARATION"
            ),
            "SELECTED_SUFFICIENCY_OPERATION_ID": (
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "operation_001"
            ),
            "CANDIDATE_ID": "receiver_side_answerable_basis_candidate_001",
            "SELECTED_SUFFICIENCY_BOUNDARY_ID": (
                "receiver_side_answerable_basis_candidate_sufficiency_"
                "boundary_001"
            ),
            "SELECTED_RECEPTION_OPERATION_ID": (
                "receiver_side_answerable_basis_reception_operation_001"
            ),
            "SELECTED_EVALUATION_BOUNDARY_ID": (
                "receiver_side_answerable_basis_candidate_evaluation_"
                "boundary_001"
            ),
            "SELECTED_EVALUATION_OPERATION_ID": (
                "receiver_side_answerable_basis_candidate_evaluation_"
                "operation_001"
            ),
            "PREPARER_REFERENCE": "marko_markota__source_body_human_governor",
            "PREPARER_RELATION_TO_SOURCE_BODY": (
                "SOURCE_BODY_ORIGINATING_PREPARER"
            ),
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value, name)
        self.assertEqual(
            resolver.REQUESTED_PREPARATION_DIMENSION_IDS,
            (
                "receiver_answerability_fit",
                "selected_purpose_adequacy",
                "bounded_material_completeness",
                "unresolved_contradiction_posture",
                "unsupported_assumption_dependency",
                "scope_constrained_usability",
                "refusal_withholding_compatibility",
                "provenance_capture_limitation_posture",
            ),
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_REQUIRES_COMPLETE,
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_NOT_RECORDED,
            ),
        )
        self.assertEqual(
            resolver.REQUEST_RESULT_FAMILY,
            (
                resolver.REQUEST_RESULT_RECORDED,
                resolver.REQUEST_RESULT_REQUIRES_COMPLETE,
                resolver.REQUEST_RESULT_NOT_EVALUATED,
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
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_receiver_side_"
                "answerable_basis_candidate_sufficiency_basis_preparation_"
                "request_declaration_v0_min"
            )
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "preparation_request_declaration_001__receiver_side_answerable_"
            "basis_candidate_sufficiency_basis_preparation_request_"
            "declaration_v0_min_result.json",
        )

    def test_02_static_contracts_and_public_codes(self) -> None:
        required_non_claims = {
            "preparation_started",
            "preparation_completed",
            "declaration_records_created",
            "declaration_ready_for_supply",
            "basis_separately_supplied",
            "basis_admitted_by_operation",
            "operation_executed",
            "operation_exhausted",
            "caller_supplied_dimension_result",
            "caller_supplied_candidate_result",
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "candidate_sufficiency_decided",
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
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
            "source_body_preparer_to_independent_custody",
            "preparer_reference_to_authority",
            "preparer_reference_to_identity",
            "preparer_reference_to_standing",
            "preparer_reference_to_truth",
            "preparation_request_debt_created",
            "preparation_request_obligation_created",
            "repeated_preparation_request_permission_created",
            "reusable_preparation_request_route_created",
            "automatic_preparation_request_created",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        }
        self.assertTrue(
            required_non_claims.issubset(resolver.REQUIRED_FALSE_NON_CLAIMS)
        )
        required_flags = {
            "request_preparation_started",
            "request_preparation_completed",
            "request_declaration_records_creation",
            "request_declaration_readiness",
            "request_basis_separate_supply",
            "request_basis_operation_admission",
            "request_operation_execution",
            "request_operation_exhaustion",
            "request_dimension_result",
            "request_candidate_sufficient",
            "request_candidate_insufficient",
            "request_candidate_indeterminate",
            "request_receiver_attestation_creation",
            "request_receiver_answerable_receipt_creation",
            "request_presence_support",
            "request_presence_authorization",
            "request_presence_establishment",
            "request_presence_recording",
            "request_identity_creation",
            "request_relation_creation",
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
            "request_preparation_request_debt_creation",
            "request_preparation_request_obligation_creation",
            "request_repeated_preparation_request_permission_creation",
            "request_reusable_preparation_request_route_creation",
            "request_automatic_preparation_request_creation",
            "request_repository_scan",
            "request_file_discovery",
            "request_affected_file_repair",
            "request_affected_file_mutation",
            "request_prior_unsupported_claim_validation",
            "request_validation_enforcement",
        }
        self.assertTrue(required_flags.issubset(resolver.PROHIBITED_REQUEST_FLAGS))
        for code in resolver.PROHIBITED_REQUEST_FLAGS.values():
            self.assertIn(code, resolver.BLOCK_CODES)
        required_codes = {
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "PREPARATION_REQUEST_SPEC_REFERENCE_MISSING",
            "PREPARATION_REQUEST_SPEC_MARKER_MISSING",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_REFERENCE_MISSING",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_PARSEABLE",
            "SELECTED_INCOMPLETE_DECLARATION_ARTIFACT_NOT_MAPPING",
            "REQUEST_VALUE_MISMATCH",
            "SELECTED_REQUEST_IDENTITY_MISMATCH",
            "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            "SELECTED_OPERATION_IDENTITY_MISMATCH",
            "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            "UPSTREAM_DECLARATION_NOT_INCOMPLETE",
            "UPSTREAM_DECLARATION_RESULT_MISMATCH",
            "UPSTREAM_DECLARATION_FAILED_CHECKS_PRESENT",
            "UPSTREAM_WAITING_OPERATION_NOT_VALIDATED",
            "UPSTREAM_DECLARATION_RECORDS_ALREADY_SUPPLIED",
            "UPSTREAM_DECLARATION_ALREADY_COMPLETE_OR_READY",
            "UPSTREAM_DECLARATION_ALREADY_RECORDED",
            "UPSTREAM_DECLARATION_RESULT_ALREADY_RECORDED",
            "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            "UPSTREAM_OPERATION_ALREADY_EXECUTED_OR_EXHAUSTED",
            "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            "UPSTREAM_ROUTE_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
            "REQUESTED_DIMENSION_SET_MISMATCH",
            "PREPARER_POSTURE_NOT_MAPPING",
            "PREPARER_REFERENCE_INVALID",
            "PREPARER_RELATION_INVALID",
            "PREPARER_POSTURE_INVALID",
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
            "FALSE_SEPARATE_CUSTODY_CLAIM",
            "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
            "PREPARATION_PERFORMANCE_PRECLAIMED",
            "DECLARATION_READINESS_PRECLAIMED",
            "RESULT_POSTURE_PRECLAIMED",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "EXPLICIT_BLOCK_REQUESTED",
            "WRITE_REFUSED",
        }
        self.assertTrue(required_codes.issubset(resolver.BLOCK_CODES))

    def test_03_default_live_incomplete_result(self) -> None:
        if not GOVERNING_SPEC_PATH.is_file():
            self.skipTest("exact live governing specification is unavailable")
        if not LIVE_INCOMPLETE_ARTIFACT_PATH.is_file():
            self.skipTest("exact live incomplete declaration artifact is unavailable")
        result = self.invoke()
        self.assert_waiting(result)
        state = self.request_state(result)
        self.assertIs(state.get("preparation_request_material_supplied"), False)
        self.assertIs(
            result["upstream_basis"].get(
                "selected_incomplete_declaration_validated"
            ),
            True,
        )

    def test_04_synthetic_incomplete_result(self) -> None:
        result = self.resolve_synthetic()
        self.assert_waiting(result)
        state = self.request_state(result)
        self.assertIs(state.get("preparation_request_material_supplied"), False)
        self.assertEqual(state.get("requested_dimension_ids"), [])
        self.assertEqual(state.get("requested_dimension_count"), 0)

    def test_05_complete_request_records_request_only(self) -> None:
        request = self.canonical_complete_request()
        before = self.clone(request)
        result = self.resolve_synthetic(request)
        self.assertEqual(request, before)
        self.assert_recorded(result)
        state = self.request_state(result)
        for key, expected in self.exact_preparer_posture().items():
            self.assertEqual(state.get(key), expected, key)

    def test_06_source_body_preparer_separation(self) -> None:
        result = self.resolve_synthetic(self.canonical_complete_request())
        self.assert_recorded(result)
        state = self.request_state(result)
        for key in (
            "independent_preparer_claimed",
            "separate_custody_claimed_by_preparer",
            "preparer_authority_claimed",
            "preparer_identity_established",
            "preparer_standing_claimed",
            "preparer_truth_claimed",
            "source_body_preparer_to_independent_custody",
            "preparation_request_debt_created",
            "preparation_request_obligation_created",
            "automatic_preparation_request_created",
        ):
            self.assertIs(state.get(key), False, key)
        statement = result.get(f"{PREFIX}_statement")
        non_meaning = result.get(f"{PREFIX}_non_meaning")
        self.assertIsInstance(statement, dict)
        self.assertIsInstance(non_meaning, dict)
        for key in (
            "request_is_not_preparation",
            "requested_preparer_is_not_preparer_performance",
            "preparation_requested_is_not_preparation_completed",
            "request_recorded_is_not_declaration_readiness",
            "source_body_preparer_is_not_independent_custody",
            "preparer_reference_is_not_authority_identity_standing_or_truth",
            "request_recorded_is_not_operation_authorization",
            "request_existence_is_not_debt_or_obligation",
        ):
            self.assertIs(statement.get(key), True, key)
        for key in (
            "preparation_request_is_not_preparation_started",
            "preparation_request_is_not_preparation_completed",
            "preparation_request_is_not_records_created",
            "preparation_request_is_not_declaration_ready",
            "source_body_origin_is_not_independent_custody",
            "preparer_reference_is_not_authority_identity_standing_or_truth",
            "request_recording_is_not_debt_obligation_or_automatic_nextness",
        ):
            self.assertIs(non_meaning.get(key), True, key)

    def test_07_exact_requested_dimension_validation(self) -> None:
        exact = list(resolver.REQUESTED_PREPARATION_DIMENSION_IDS)
        malformed = {
            "missing_middle": exact[:2] + exact[3:],
            "extra": exact + ["extra_dimension"],
            "reordered": list(reversed(exact)),
            "duplicate": exact[:-1] + [exact[0]],
            "non_sequence": {"not": "a sequence"},
            "wrong_value_type": exact[:-1] + [17],
        }
        for name, dimensions in malformed.items():
            with self.subTest(case=name):
                request = self.canonical_complete_request()
                request["requested_dimension_ids"] = dimensions
                self.assert_blocked(
                    self.resolve_synthetic(request),
                    "REQUESTED_DIMENSION_SET_MISMATCH",
                )
        for name, dimensions in (
            ("empty", []),
            ("clean_prefix", exact[:4]),
        ):
            with self.subTest(case=name):
                request = self.canonical_complete_request()
                request["requested_dimension_ids"] = dimensions
                self.assert_waiting(self.resolve_synthetic(request))

    def test_08_preparer_posture_validation(self) -> None:
        blocked_cases: list[tuple[str, object, str]] = []
        posture = self.exact_preparer_posture()
        blocked_cases.append(
            ("not_mapping", [], "PREPARER_POSTURE_NOT_MAPPING")
        )
        for name, key, value, code in (
            (
                "wrong_reference",
                "preparer_reference",
                "wrong",
                "PREPARER_REFERENCE_INVALID",
            ),
            (
                "wrong_relation",
                "preparer_relation_to_source_body",
                "wrong",
                "PREPARER_RELATION_INVALID",
            ),
            (
                "source_body_false",
                "source_body_preparer",
                False,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "false_independence",
                "independent_preparer_claimed",
                True,
                "FALSE_INDEPENDENT_PREPARER_CLAIM",
            ),
            (
                "false_custody",
                "separate_custody_claimed_by_preparer",
                True,
                "FALSE_SEPARATE_CUSTODY_CLAIM",
            ),
            (
                "authority",
                "preparer_authority_claimed",
                True,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "identity",
                "preparer_identity_established",
                True,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "standing",
                "preparer_standing_claimed",
                True,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "truth",
                "preparer_truth_claimed",
                True,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "non_boolean",
                "source_body_preparer",
                1,
                "PREPARER_POSTURE_INVALID",
            ),
            (
                "excessive_text",
                "preparer_reference",
                "x" * (resolver.MAX_PREPARER_REFERENCE_LENGTH + 1),
                "PREPARER_REFERENCE_INVALID",
            ),
        ):
            changed = self.clone(posture)
            changed[key] = value
            blocked_cases.append((name, changed, code))
        suspicious = self.clone(posture)
        suspicious["preparer_reference"] = {"basis_items": []}
        blocked_cases.append(
            (
                "suspicious_nested_payload",
                suspicious,
                "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
            )
        )
        excessive_nesting = self.clone(posture)
        nested: object = "value"
        for _ in range(resolver.MAX_NESTING_DEPTH + 2):
            nested = {"nested": nested}
        excessive_nesting["preparer_reference"] = nested
        blocked_cases.append(
            ("excessive_nesting", excessive_nesting, "REQUEST_NESTING_EXCEEDED")
        )
        for name, changed, code in blocked_cases:
            with self.subTest(case=name):
                request = self.canonical_complete_request()
                request["preparer_posture"] = changed
                self.assert_blocked(self.resolve_synthetic(request), code)
        missing = self.exact_preparer_posture()
        missing.pop("preparer_truth_claimed")
        request = self.canonical_complete_request()
        request["preparer_posture"] = missing
        self.assert_waiting(self.resolve_synthetic(request))

    def test_09_request_payload_exclusion(self) -> None:
        payloads = {
            "declaration_records": [],
            "basis_items": [],
            "basis_references": [],
            "declarant_reference": {},
            "evaluator_reference": {},
            "support_postures": {},
            "contradiction_postures": {},
            "unresolved_postures": {},
            "upstream_artifact": {"copied": True},
            "upstream_checks": [],
            "candidate_material": "raw candidate",
            "capture_material": "raw capture",
        }
        for key, value in payloads.items():
            with self.subTest(payload=key):
                request = self.canonical_complete_request()
                request[key] = value
                self.assert_blocked(
                    self.resolve_synthetic(request),
                    "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
                )

    def test_10_upstream_incomplete_declaration_validation(self) -> None:
        cases = (
            ("root", "resolver_module", "wrong", "UPSTREAM_DECLARATION_NOT_INCOMPLETE"),
            ("root", "result_version", "9", "UPSTREAM_DECLARATION_NOT_INCOMPLETE"),
            ("root", "outcome", "wrong", "UPSTREAM_DECLARATION_NOT_INCOMPLETE"),
            (
                "declaration",
                "declaration_result",
                "wrong",
                "UPSTREAM_DECLARATION_RESULT_MISMATCH",
            ),
            (
                "root",
                "failed_check_count",
                1,
                "UPSTREAM_DECLARATION_FAILED_CHECKS_PRESENT",
            ),
            (
                "declaration",
                "declaration_id",
                "wrong",
                "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "declaration_type",
                "wrong",
                "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "declaration_version",
                "wrong",
                "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "declaration_scope",
                "wrong",
                "SELECTED_DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "selected_candidate_sufficiency_operation_id",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "receiver_side_answerable_basis_candidate_id",
                "wrong",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "selected_candidate_sufficiency_boundary_id",
                "wrong",
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "selected_candidate_reception_operation_id",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "selected_candidate_evaluation_boundary_id",
                "wrong",
                "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "declaration",
                "selected_candidate_evaluation_operation_id",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "summary",
                "upstream_waiting_operation_validated",
                False,
                "UPSTREAM_WAITING_OPERATION_NOT_VALIDATED",
            ),
            (
                "declaration",
                "declaration_records_supplied",
                True,
                "UPSTREAM_DECLARATION_RECORDS_ALREADY_SUPPLIED",
            ),
            (
                "declaration",
                "declaration_record_count",
                1,
                "UPSTREAM_DECLARATION_RECORDS_ALREADY_SUPPLIED",
            ),
            (
                "declaration",
                "declaration_complete",
                True,
                "UPSTREAM_DECLARATION_ALREADY_COMPLETE_OR_READY",
            ),
            (
                "declaration",
                "candidate_sufficiency_basis_declaration_ready_for_supply",
                True,
                "UPSTREAM_DECLARATION_ALREADY_COMPLETE_OR_READY",
            ),
            (
                "declaration",
                "candidate_sufficiency_basis_declaration_recorded",
                True,
                "UPSTREAM_DECLARATION_ALREADY_RECORDED",
            ),
            (
                "declaration",
                "candidate_sufficiency_basis_declaration_result_recorded",
                True,
                "UPSTREAM_DECLARATION_RESULT_ALREADY_RECORDED",
            ),
            (
                "declaration",
                "candidate_sufficiency_basis_separately_supplied",
                True,
                "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                "declaration",
                "candidate_sufficiency_basis_admitted_by_operation",
                True,
                "UPSTREAM_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                "declaration",
                "candidate_sufficiency_operation_executed",
                True,
                "UPSTREAM_OPERATION_ALREADY_EXECUTED_OR_EXHAUSTED",
            ),
            (
                "declaration",
                "candidate_sufficiency_operation_exhausted",
                True,
                "UPSTREAM_OPERATION_ALREADY_EXECUTED_OR_EXHAUSTED",
            ),
            (
                "declaration",
                "receiver_side_answerable_basis_candidate_sufficient",
                True,
                "UPSTREAM_CANDIDATE_RESULT_ALREADY_PRESENT",
            ),
            (
                "declaration",
                "receiver_attestation_created",
                True,
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "declaration",
                "receiver_answerable_receipt_present",
                True,
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "declaration",
                "presence_supported",
                True,
                "UPSTREAM_RECEIVER_RECEIPT_OR_PRESENCE_POSTURE_PRESENT",
            ),
            (
                "declaration",
                "declaration_debt_created",
                True,
                "UPSTREAM_ROUTE_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
            (
                "declaration",
                "runtime_created",
                True,
                "UPSTREAM_ROUTE_RETRY_DEBT_OBLIGATION_OR_DOWNSTREAM_PRESENT",
            ),
        )
        declaration_key = (
            "receiver_side_answerable_basis_candidate_sufficiency_basis_"
            "declaration"
        )
        summary_key = declaration_key + "_summary"
        for section, key, value, expected in cases:
            with self.subTest(section=section, field=key):
                artifact = self.synthetic_valid_incomplete_declaration_artifact()
                target = (
                    artifact
                    if section == "root"
                    else artifact[
                        declaration_key if section == "declaration" else summary_key
                    ]
                )
                self.assertIsInstance(target, dict)
                target[key] = value
                self.assert_blocked(
                    self.resolve_synthetic(
                        self.canonical_incomplete_request(),
                        artifact=artifact,
                    ),
                    expected,
                )
        artifact = self.synthetic_valid_incomplete_declaration_artifact()
        artifact["what_remains_open"] = ["stale open state"]
        self.assert_blocked(
            self.resolve_synthetic(
                self.canonical_incomplete_request(),
                artifact=artifact,
            ),
            "UPSTREAM_OPEN_STATE_STALE_OR_MISMATCHED",
        )

    def test_11_request_shape_and_identity_validation(self) -> None:
        self.assert_blocked(self.invoke([]), "REQUEST_NOT_MAPPING")
        request_cases = (
            ("intent", "UNSUPPORTED", "UNSUPPORTED_INTENT"),
            (
                f"{PREFIX}_id",
                "wrong",
                "SELECTED_REQUEST_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_sufficiency_basis_declaration_id",
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
                "governing_preparation_request_specification_path",
                "alternate.md",
                "REQUEST_VALUE_MISMATCH",
            ),
            (
                "selected_incomplete_declaration_artifact_path",
                "alternate.json",
                "REQUEST_VALUE_MISMATCH",
            ),
        )
        for key, value, expected in request_cases:
            with self.subTest(field=key):
                request = self.canonical_incomplete_request()
                request[key] = value
                self.assert_blocked(self.invoke(request), expected)
        for malformed in (None, {}, {"preparation_started": False}):
            with self.subTest(non_claims=repr(malformed)):
                request = self.canonical_incomplete_request()
                request["declared_non_claims"] = malformed
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
        inconsistent = self.canonical_incomplete_request()
        inconsistent["requested_dimension_ids"] = [
            resolver.REQUESTED_PREPARATION_DIMENSION_IDS[0]
        ]
        self.assert_blocked(self.invoke(inconsistent), "REQUEST_VALUE_MISMATCH")
        for key in ("outcome", "request_result"):
            request = self.canonical_incomplete_request()
            request[key] = "caller selected"
            self.assert_blocked(self.invoke(request), "RESULT_POSTURE_PRECLAIMED")

    def test_12_incoming_preclaims(self) -> None:
        cases = (
            ("preparation_request_recorded", "RESULT_POSTURE_PRECLAIMED"),
            ("preparation_request_result_recorded", "RESULT_POSTURE_PRECLAIMED"),
            ("request_result", "RESULT_POSTURE_PRECLAIMED"),
            ("preparation_request_complete", "RESULT_POSTURE_PRECLAIMED"),
            ("preparation_requested", "RESULT_POSTURE_PRECLAIMED"),
            ("preparation_started", "PREPARATION_PERFORMANCE_PRECLAIMED"),
            ("preparation_completed", "PREPARATION_PERFORMANCE_PRECLAIMED"),
            ("declaration_records_created", "PREPARATION_PERFORMANCE_PRECLAIMED"),
            ("declaration_ready_for_supply", "DECLARATION_READINESS_PRECLAIMED"),
            ("basis_separately_supplied", "RESULT_POSTURE_PRECLAIMED"),
            ("basis_admitted_by_operation", "RESULT_POSTURE_PRECLAIMED"),
            ("operation_executed", "RESULT_POSTURE_PRECLAIMED"),
            ("operation_exhausted", "RESULT_POSTURE_PRECLAIMED"),
            ("dimension_result", "RESULT_POSTURE_PRECLAIMED"),
            ("candidate_result", "RESULT_POSTURE_PRECLAIMED"),
            ("receiver_attestation_created", "RESULT_POSTURE_PRECLAIMED"),
            ("receiver_answerable_receipt_present", "RESULT_POSTURE_PRECLAIMED"),
            ("presence_supported", "RESULT_POSTURE_PRECLAIMED"),
            (
                "reusable_preparation_request_route_created",
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                "repeated_preparation_request_permission_created",
                "RESULT_POSTURE_PRECLAIMED",
            ),
            ("preparation_request_debt_created", "RESULT_POSTURE_PRECLAIMED"),
            ("preparation_request_obligation_created", "RESULT_POSTURE_PRECLAIMED"),
            ("runtime_created", "RESULT_POSTURE_PRECLAIMED"),
        )
        for key, expected in cases:
            with self.subTest(preclaim=key):
                request = self.canonical_complete_request()
                request[key] = True
                self.assert_blocked(self.invoke(request), expected)

    def test_13_declared_non_claims(self) -> None:
        base = self.canonical_complete_request()
        declared = base.get("declared_non_claims")
        self.assertIsInstance(declared, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(declared.get(key), False, key)
            with self.subTest(flipped=key):
                request = self.clone(base)
                request["declared_non_claims"][key] = True
                result = self.invoke(request)
                self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")
                self.assert_canonical_false_non_claims(result)
        malformed_values = (None, 0, "false")
        for value in malformed_values:
            with self.subTest(value=repr(value)):
                request = self.clone(base)
                request["declared_non_claims"][
                    resolver.REQUIRED_FALSE_NON_CLAIMS[0]
                ] = value
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
        missing = self.clone(base)
        missing["declared_non_claims"].pop(
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        )
        self.assert_blocked(
            self.invoke(missing),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    def test_14_prohibited_request_flags(self) -> None:
        base = self.canonical_complete_request()
        for key, expected in resolver.PROHIBITED_REQUEST_FLAGS.items():
            with self.subTest(flag=key):
                request = self.clone(base)
                request[key] = True
                result = self.invoke(request)
                self.assert_blocked(result, expected)

    def test_15_partial_request_behavior(self) -> None:
        self.assert_waiting(
            self.resolve_synthetic(self.canonical_incomplete_request())
        )
        dimensions_only = self.canonical_incomplete_request(
            preparation_request_material_supplied=True,
            requested_dimension_ids=resolver.REQUESTED_PREPARATION_DIMENSION_IDS,
            preparer_posture=None,
        )
        self.assert_waiting(self.resolve_synthetic(dimensions_only))
        posture_only = self.canonical_incomplete_request(
            preparation_request_material_supplied=True,
            requested_dimension_ids=[],
            preparer_posture=self.exact_preparer_posture(),
        )
        self.assert_waiting(self.resolve_synthetic(posture_only))
        partial_posture = self.exact_preparer_posture()
        partial_posture.pop("preparer_truth_claimed")
        clean_partial = self.canonical_incomplete_request(
            preparation_request_material_supplied=True,
            requested_dimension_ids=resolver.REQUESTED_PREPARATION_DIMENSION_IDS[:4],
            preparer_posture=partial_posture,
        )
        self.assert_waiting(self.resolve_synthetic(clean_partial))
        contradictory = self.canonical_incomplete_request()
        contradictory["requested_dimension_ids"] = [
            resolver.REQUESTED_PREPARATION_DIMENSION_IDS[0]
        ]
        self.assert_blocked(
            self.resolve_synthetic(contradictory),
            "REQUEST_VALUE_MISMATCH",
        )
        deceptive = self.canonical_incomplete_request(
            preparation_request_material_supplied=True,
            requested_dimension_ids=resolver.REQUESTED_PREPARATION_DIMENSION_IDS[:4],
            preparer_posture=self.exact_preparer_posture(),
        )
        deceptive["preparer_posture"]["independent_preparer_claimed"] = True
        self.assert_blocked(
            self.resolve_synthetic(deceptive),
            "FALSE_INDEPENDENT_PREPARER_CLAIM",
        )
        malformed = self.canonical_incomplete_request(
            preparation_request_material_supplied=True,
            requested_dimension_ids=["wrong"],
            preparer_posture=None,
        )
        self.assert_blocked(
            self.resolve_synthetic(malformed),
            "REQUESTED_DIMENSION_SET_MISMATCH",
        )

    def test_16_do_not_record_and_explicit_block(self) -> None:
        do_not_record = self.canonical_incomplete_request(
            intent=resolver.INTENT_DO_NOT_RECORD
        )
        result = self.invoke(do_not_record)
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_RECORDED)
        self.assertEqual(
            self.request_result(result),
            resolver.REQUEST_RESULT_NOT_EVALUATED,
        )
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertIs(
            self.request_state(result).get(
                "candidate_sufficiency_basis_preparation_requested"
            ),
            False,
        )
        self.assert_later_postures_false(result)
        explicit = self.canonical_incomplete_request(intent=resolver.INTENT_BLOCK)
        self.assert_blocked(
            self.invoke(explicit),
            "EXPLICIT_BLOCK_REQUESTED",
        )

    def test_17_result_structure(self) -> None:
        result = self.resolve_synthetic(self.canonical_complete_request())
        required = {
            f"{PREFIX}_metadata",
            f"declared_{PREFIX}_basis",
            "upstream_basis",
            PREFIX,
            f"{PREFIX}_checks",
            f"{PREFIX}_statement",
            f"{PREFIX}_non_meaning",
            "request_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            f"{PREFIX}_summary",
            "resolver_module",
            "result_version",
        }
        self.assertTrue(required.issubset(result))
        self.assertEqual(set(result), set(resolver.RESULT_SECTIONS))
        state = self.request_state(result)
        for wrapper in (
            "outcome",
            "block",
            "non_claims",
            f"{PREFIX}_checks",
            f"{PREFIX}_summary",
            f"{PREFIX}_metadata",
        ):
            self.assertNotIn(wrapper, state)

    def test_18_bounded_request_material(self) -> None:
        result = self.resolve_synthetic(self.canonical_complete_request())
        self.assert_recorded(result)
        state = self.request_state(result)
        retained = {
            "requested_dimension_ids",
            "preparer_reference",
            "preparer_relation_to_source_body",
            *resolver.PREPARER_POSTURE_KEYS,
            "request_id",
            "selected_candidate_sufficiency_basis_declaration_id",
            "selected_candidate_sufficiency_operation_id",
            "receiver_side_answerable_basis_candidate_id",
            "selected_candidate_sufficiency_boundary_id",
            "preparation_request_complete",
        }
        self.assertTrue(retained.issubset(state))
        self.assert_complete_upstream_payload_omitted(result)

    def test_19_branch_relative_what_remains_open(self) -> None:
        incomplete = self.resolve_synthetic(self.canonical_incomplete_request())
        recorded = self.resolve_synthetic(self.canonical_complete_request())
        blocked_request = self.canonical_complete_request()
        blocked_request["preparer_posture"][
            "independent_preparer_claimed"
        ] = True
        blocked = self.invoke(blocked_request)
        not_recorded = self.invoke(
            self.canonical_incomplete_request(intent=resolver.INTENT_DO_NOT_RECORD)
        )
        self.assertEqual(
            tuple(incomplete["what_remains_open"]),
            resolver.INCOMPLETE_WHAT_REMAINS_OPEN,
        )
        self.assertEqual(
            tuple(recorded["what_remains_open"]),
            resolver.RECORDED_WHAT_REMAINS_OPEN,
        )
        self.assertNotIn(
            "complete preparation-request declaration",
            recorded["what_remains_open"],
        )
        for result in (blocked, not_recorded):
            self.assertIs(
                self.request_state(result).get("preparation_request_complete"),
                False,
            )

    def test_20_summary_behavior(self) -> None:
        incomplete = self.resolve_synthetic(self.canonical_incomplete_request())
        recorded = self.resolve_synthetic(self.canonical_complete_request())
        blocked_request = self.canonical_complete_request()
        blocked_request["preparer_posture"][
            "separate_custody_claimed_by_preparer"
        ] = True
        blocked = self.invoke(blocked_request)
        not_recorded = self.invoke(
            self.canonical_incomplete_request(intent=resolver.INTENT_DO_NOT_RECORD)
        )
        required = {
            "outcome",
            "request_result",
            "failed_check_count",
            "passed_check_count",
            "resolver_module",
            "result_version",
            "request_identity",
            "selected_identity",
            "upstream_incomplete_declaration_validated",
            "preparation_request_material_supplied",
            "preparation_request_complete",
            "requested_dimension_count",
            "requested_dimension_ids",
            "preparer_posture",
            "request_recorded",
            "preparation_requested",
            "preparation_and_record_creation_locks",
            "readiness_supply_admission_execution_exhaustion_locks",
            "candidate_receiver_receipt_presence_route_retry_debt_obligation_"
            "and_downstream_locks_false",
            "governing_paths",
            "marker_validation",
            "non_claims_canonical_false",
        }
        for result in (incomplete, recorded, blocked, not_recorded):
            summary = result.get(f"{PREFIX}_summary")
            self.assertIsInstance(summary, dict)
            self.assertTrue(required.issubset(summary))
            self.assertEqual(summary.get("outcome"), result.get("outcome"))
            self.assertEqual(
                summary.get("request_result"),
                self.request_result(result),
            )
            self.assertEqual(
                summary.get("failed_check_count"),
                result.get("failed_check_count"),
            )
            self.assertEqual(summary.get("resolver_module"), resolver.RESOLVER_MODULE)
            self.assertEqual(summary.get("result_version"), resolver.RESULT_VERSION)
            self.assertIs(summary.get("non_claims_canonical_false"), True)
            for lock_group in (
                "preparation_and_record_creation_locks",
                "readiness_supply_admission_execution_exhaustion_locks",
            ):
                locks = summary.get(lock_group)
                self.assertIsInstance(locks, dict)
                self.assertTrue(all(value is False for value in locks.values()))

    def test_21_from_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            incomplete_path = self._write_json(
                root / "inputs" / "incomplete.json",
                self.canonical_incomplete_request(),
            )
            recorded_path = self._write_json(
                root / "inputs" / "recorded.json",
                self.canonical_complete_request(),
            )
            malformed_path = self._write_text(
                root / "inputs" / "malformed.json",
                "{",
            )
            array_path = self._write_json(
                root / "inputs" / "array.json",
                [],
            )
            missing_path = root / "inputs" / "missing.json"
            with patch.object(resolver, "REPO_ROOT", root):
                incomplete = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
                        incomplete_path
                    )
                )
                recorded = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
                        recorded_path
                    )
                )
                malformed = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
                        malformed_path
                    )
                )
                array = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
                        array_path
                    )
                )
                missing = (
                    resolver.resolve_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_from_path(
                        missing_path
                    )
                )
            self.assert_waiting(incomplete)
            self.assert_recorded(recorded)
            for result in (malformed, array, missing):
                self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_22_write_behavior(self) -> None:
        incomplete = self.resolve_synthetic(self.canonical_incomplete_request())
        recorded = self.resolve_synthetic(self.canonical_complete_request())
        blocked_request = self.canonical_complete_request()
        blocked_request["preparer_posture"][
            "independent_preparer_claimed"
        ] = True
        blocked = self.invoke(blocked_request)
        not_recorded = self.invoke(
            self.canonical_incomplete_request(intent=resolver.INTENT_DO_NOT_RECORD)
        )
        error = (
            resolver.ReceiverSideAnswerableBasisCandidateSufficiencyBasisPreparationRequestDeclarationV0MinError
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, result in enumerate(
                (incomplete, recorded, blocked, not_recorded)
            ):
                output = self.safe_temporary_output_path(
                    root,
                    f"case_{index}",
                )
                written = (
                    resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
                        result,
                        output,
                    )
                )
                self.assertEqual(written, output)
                self.assertTrue(written.is_file())
                parsed = json.loads(written.read_text(encoding="utf-8"))
                self.assertEqual(parsed["resolver_module"], resolver.RESOLVER_MODULE)
                self.assertEqual(parsed["result_version"], resolver.RESULT_VERSION)
                self.assertEqual(parsed["outcome"], result["outcome"])
                self.assert_canonical_false_non_claims(parsed)
            target = self.safe_temporary_output_path(root, "repeat")
            first = (
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
                    recorded,
                    target,
                )
            )
            second = (
                resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
                    recorded,
                    target,
                )
            )
            self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(
                second.name,
                f"{target.stem}_001{target.suffix}",
            )
            bad_results: list[tuple[str, object]] = []
            copied = self.clone(recorded)
            copied[f"declared_{PREFIX}_basis"]["basis_items"] = []
            bad_results.append(("copied", copied))
            wrong_module = self.clone(recorded)
            wrong_module["resolver_module"] = "wrong"
            bad_results.append(("module", wrong_module))
            wrong_version = self.clone(recorded)
            wrong_version["result_version"] = "9"
            bad_results.append(("version", wrong_version))
            wrong_outcome = self.clone(recorded)
            wrong_outcome["outcome"] = "unsupported"
            bad_results.append(("outcome", wrong_outcome))
            flipped = self.clone(recorded)
            flipped["non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = True
            bad_results.append(("non_claim", flipped))
            inconsistent = self.clone(recorded)
            inconsistent[PREFIX]["request_result"] = (
                resolver.REQUEST_RESULT_NOT_EVALUATED
            )
            bad_results.append(("branch", inconsistent))
            performed = self.clone(recorded)
            performed[PREFIX][
                "candidate_sufficiency_basis_preparation_started"
            ] = True
            bad_results.append(("performed", performed))
            bad_results.extend((("none", None), ("empty", {})))
            for name, bad in bad_results:
                with self.subTest(refused=name):
                    with self.assertRaises(error):
                        resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
                            bad,
                            self.safe_temporary_output_path(root, f"bad_{name}"),
                        )
            for forbidden in (
                root / "spec" / resolver.OUTPUT_FILENAME,
                root
                / "candidate_evaluation_root"
                / resolver.OUTPUT_FILENAME,
            ):
                with self.assertRaises(error):
                    resolver.write_receiver_side_answerable_basis_candidate_sufficiency_basis_preparation_request_declaration_v0_min_result(
                        recorded,
                        forbidden,
                    )

    def test_23_non_mutation_and_lineage_preservation(self) -> None:
        before_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in self.preserved_paths
        }
        artifact = self.synthetic_valid_incomplete_declaration_artifact()
        request = self.canonical_complete_request()
        artifact_before = self.clone(artifact)
        request_before = self.clone(request)
        result = self.resolve_synthetic(request, artifact=artifact)
        self.assert_recorded(result)
        self.assertEqual(artifact, artifact_before)
        self.assertEqual(request, request_before)
        after_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in self.preserved_paths
        }
        self.assertEqual(after_hashes, before_hashes)

    def test_24_smoke_matrix(self) -> None:
        cases: list[tuple[str, dict[str, object], str, str | None]] = []
        cases.append(
            (
                "incomplete",
                self.canonical_incomplete_request(),
                resolver.OUTCOME_REQUIRES_COMPLETE,
                None,
            )
        )
        cases.append(
            (
                "recorded",
                self.canonical_complete_request(),
                resolver.OUTCOME_RECORDED,
                None,
            )
        )
        missing = self.canonical_complete_request()
        missing["requested_dimension_ids"] = list(
            resolver.REQUESTED_PREPARATION_DIMENSION_IDS[:-1]
        )
        cases.append(
            ("missing_dimensions", missing, resolver.OUTCOME_REQUIRES_COMPLETE, None)
        )
        reordered = self.canonical_complete_request()
        reordered["requested_dimension_ids"] = list(
            reversed(resolver.REQUESTED_PREPARATION_DIMENSION_IDS)
        )
        cases.append(
            (
                "wrong_order",
                reordered,
                resolver.OUTCOME_BLOCKED,
                "REQUESTED_DIMENSION_SET_MISMATCH",
            )
        )
        wrong_preparer = self.canonical_complete_request()
        wrong_preparer["preparer_posture"]["preparer_reference"] = "wrong"
        cases.append(
            (
                "wrong_preparer",
                wrong_preparer,
                resolver.OUTCOME_BLOCKED,
                "PREPARER_REFERENCE_INVALID",
            )
        )
        false_independence = self.canonical_complete_request()
        false_independence["preparer_posture"][
            "independent_preparer_claimed"
        ] = True
        cases.append(
            (
                "false_independence",
                false_independence,
                resolver.OUTCOME_BLOCKED,
                "FALSE_INDEPENDENT_PREPARER_CLAIM",
            )
        )
        false_custody = self.canonical_complete_request()
        false_custody["preparer_posture"][
            "separate_custody_claimed_by_preparer"
        ] = True
        cases.append(
            (
                "false_custody",
                false_custody,
                resolver.OUTCOME_BLOCKED,
                "FALSE_SEPARATE_CUSTODY_CLAIM",
            )
        )
        for name, key, code in (
            (
                "performance",
                "preparation_started",
                "PREPARATION_PERFORMANCE_PRECLAIMED",
            ),
            (
                "readiness",
                "declaration_ready_for_supply",
                "DECLARATION_READINESS_PRECLAIMED",
            ),
            (
                "basis_payload",
                "basis_items",
                "REQUEST_PAYLOAD_CONTAINS_DECLARATION_OR_BASIS_MATERIAL",
            ),
        ):
            request = self.canonical_complete_request()
            request[key] = True if key != "basis_items" else []
            cases.append((name, request, resolver.OUTCOME_BLOCKED, code))
        prohibited = self.canonical_complete_request()
        prohibited["request_operation_execution"] = True
        cases.append(
            (
                "prohibited_execution",
                prohibited,
                resolver.OUTCOME_BLOCKED,
                resolver.PROHIBITED_REQUEST_FLAGS["request_operation_execution"],
            )
        )
        cases.append(
            (
                "blocked_intent",
                self.canonical_incomplete_request(intent=resolver.INTENT_BLOCK),
                resolver.OUTCOME_BLOCKED,
                "EXPLICIT_BLOCK_REQUESTED",
            )
        )
        cases.append(
            (
                "not_recorded",
                self.canonical_incomplete_request(
                    intent=resolver.INTENT_DO_NOT_RECORD
                ),
                resolver.OUTCOME_NOT_RECORDED,
                None,
            )
        )
        for name, request, outcome, code in cases:
            with self.subTest(case=name):
                result = self.resolve_synthetic(request)
                self.assertEqual(result.get("outcome"), outcome)
                if outcome == resolver.OUTCOME_RECORDED:
                    self.assert_recorded(result)
                elif outcome == resolver.OUTCOME_REQUIRES_COMPLETE:
                    self.assert_waiting(result)
                elif outcome == resolver.OUTCOME_BLOCKED:
                    self.assert_blocked(result, code)
                else:
                    self.assertEqual(
                        self.request_result(result),
                        resolver.REQUEST_RESULT_NOT_EVALUATED,
                    )
                    self.assert_later_postures_false(result)


if __name__ == "__main__":
    unittest.main()
