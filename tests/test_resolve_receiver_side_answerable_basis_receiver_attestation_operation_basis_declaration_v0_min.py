"""Tests for one exact receiver-attestation operation basis declaration.

Clean branches use the standing declaration specification and PREPARED
artifact. Negative cases copy only those two inputs into isolated temporary
roots. The suite does not read capture evidence or create downstream standing.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min as resolver


PREFIX = resolver.PREFIX
STATE_KEY = PREFIX
CHECKS_KEY = f"{PREFIX}_checks"
SUMMARY_KEY = f"{PREFIX}_summary"
STATEMENT_KEY = f"{PREFIX}_statement"
NON_MEANING_KEY = f"{PREFIX}_non_meaning"

SPECIFICATION_RELATIVE_PATH = (
    resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
)
PREPARATION_ARTIFACT_RELATIVE_PATH = (
    resolver.SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH
)
SOURCE_RELATIVE_PATH = Path(
    "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_declaration_v0_min.py"
)
TEST_RELATIVE_PATH = Path(
    "tests/test_resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_declaration_v0_min.py"
)
OUTPUT_RELATIVE_ROOT = resolver.OUTPUT_ROOT.relative_to(REPOSITORY_ROOT)

PRESERVED_RELATIVE_PATHS = (
    SPECIFICATION_RELATIVE_PATH,
    SOURCE_RELATIVE_PATH,
    PREPARATION_ARTIFACT_RELATIVE_PATH,
)

BRANCH_TRUE_FIELDS = (
    "declaration_recorded",
    "declaration_result_recorded",
    "declaration_exhausted",
)

OPERATION_FALSE_FIELDS = (
    "receiver_attestation_operation_basis_supplied",
    "receiver_attestation_operation_basis_admitted",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_executed",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
    "receiver_attestation_recorded",
    "receiver_attestation_not_recorded",
    "receiver_attestation_indeterminate",
)

PREPARATION_REQUIRED_TRUE_FIELDS = (
    "basis_declaration_preparation_selected",
    "specification_markers_validated",
    "preparation_request_artifact_validated",
    "selected_boundary_reference_validated",
    "bounded_paths_validated",
    "required_bounded_components_available",
    "archive_hash_record_validated",
    "archive_correspondence_validated",
    "required_text_components_validated",
    "timestamp_validated",
    "recorded_signal_artifact_validated",
    "complete_21_field_candidate_prepared",
    "preparation_recorded",
    "preparation_result_recorded",
    "preparation_exhausted",
    "basis_declaration_preparation_started",
    "basis_declaration_preparation_completed",
    "receiver_attestation_operation_basis_declaration_candidate_prepared",
    "receiver_attestation_operation_basis_prepared",
)

PREPARATION_REQUIRED_FALSE_FIELDS = (
    "receiver_attestation_operation_basis_declared",
    "receiver_attestation_operation_basis_supplied",
    "receiver_attestation_operation_basis_admitted",
    "receiver_attestation_operation_recorded",
    "receiver_attestation_operation_result_recorded",
    "receiver_attestation_operation_exhausted",
    "receiver_attestation_decided",
    "receiver_attestation_recorded",
    "receiver_attestation_not_recorded",
    "receiver_attestation_indeterminate",
)

SENSITIVE_FALSE_FIELDS = (
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)

PREPARATION_SUMMARY_TRUE_FIELDS = (
    "preparation_selection",
    "specification_markers_validated",
    "preparation_request_artifact_validated",
    "selected_boundary_reference_validated",
    "bounded_paths_validated",
    "required_bounded_components_available",
    "archive_hash_record_validated",
    "archive_correspondence_validated",
    "required_text_components_validated",
    "timestamp_validated",
    "recorded_signal_artifact_validated",
    "complete_21_field_candidate_prepared",
    "preparation_recorded",
    "preparation_result_recorded",
    "preparation_exhausted",
    "basis_declaration_preparation_started",
    "basis_declaration_preparation_completed",
    "declaration_candidate_prepared",
    "operation_basis_prepared",
    "result_level_non_claims_canonical_false",
    "complete_material_omitted",
)

PREPARATION_SUMMARY_FALSE_FIELDS = (
    "archive_correspondence_contradicted",
    "timestamp_ambiguous",
    "operation_basis_declared",
    "operation_basis_supplied",
    "operation_basis_admitted",
    "operation_recorded",
    "operation_result_recorded",
    "operation_exhausted",
    "receiver_attestation_recorded",
)


class ReceiverAttestationOperationBasisDeclarationTests(
    unittest.TestCase
):
    """Exercise exact declaration, separation, digest, and writer locks."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_hashes = {
            relative: cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }

    @classmethod
    def tearDownClass(cls) -> None:
        current = {
            relative: cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        if current != cls.preserved_hashes:
            raise AssertionError(
                "receiver-attestation declaration lineage changed during tests"
            )

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def _write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(
            path.is_dir(),
            f"fixture path collision: text target is a directory: {path}",
        )
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: Any) -> Path:
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

    def _load_json(self, path: Path) -> dict[str, Any]:
        value = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(value, dict)
        return copy.deepcopy(value)

    def preparation_artifact(self) -> dict[str, Any]:
        return self._load_json(
            REPOSITORY_ROOT / PREPARATION_ARTIFACT_RELATIVE_PATH
        )

    def prepared_candidate(self) -> dict[str, Any]:
        candidate = self.preparation_artifact().get(
            "prepared_declaration_candidate"
        )
        self.assertIsInstance(candidate, dict)
        return copy.deepcopy(candidate)

    def canonical_request(
        self,
        *,
        selected: bool = True,
        **overrides: Any,
    ) -> dict[str, Any]:
        return resolver.build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request(
            basis_declaration_selected=selected,
            **copy.deepcopy(overrides),
        )

    def invoke(self, request: Any = None) -> dict[str, Any]:
        return resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min(
            request
        )

    def state(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(STATE_KEY)
        self.assertIsInstance(value, dict)
        return value

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(SUMMARY_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result.get(CHECKS_KEY)
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def assert_all_emitted_codes_public(
        self,
        result: Mapping[str, Any],
    ) -> None:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        for field in ("code", "block_code"):
            code = block.get(field)
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            self.assertIs(type(check.get("passed")), bool)
            for field in ("failure_code", "block_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_check_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        self.assertEqual(
            result.get("failed_check_count"),
            sum(item["passed"] is False for item in checks),
        )
        self.assertEqual(
            result.get("passed_check_count"),
            sum(item["passed"] is True for item in checks),
        )

    def assert_canonical_false_non_claims(
        self,
        result: Mapping[str, Any],
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        state = self.state(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(type(non_claims[field]), bool)
            self.assertIs(non_claims[field], False)
            self.assertIs(type(state[field]), bool)
            self.assertIs(state[field], False)

    def assert_omission_posture(
        self,
        result: Mapping[str, Any],
    ) -> None:
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, dict)
        self.assertEqual(set(omission), set(resolver.RESULT_OMISSION_FIELDS))
        state = self.state(result)
        for field in resolver.RESULT_OMISSION_FIELDS:
            self.assertIs(omission[field], True)
            self.assertIs(state[field], True)

        def walk(value: Any) -> None:
            if isinstance(value, Mapping):
                self.assertTrue(
                    set(value).isdisjoint(resolver.FORBIDDEN_PAYLOAD_KEYS)
                )
                for nested in value.values():
                    walk(nested)
            elif isinstance(value, Sequence) and not isinstance(
                value,
                (str, bytes, bytearray),
            ):
                for nested in value:
                    walk(nested)
            self.assertNotIsInstance(value, (bytes, bytearray))

        walk(result)

    def assert_operation_false(
        self,
        result: Mapping[str, Any],
    ) -> None:
        state = self.state(result)
        for field in OPERATION_FALSE_FIELDS:
            self.assertIn(field, state)
            self.assertIs(type(state[field]), bool)
            self.assertIs(state[field], False)
        for field in resolver.EXTRA_REQUIRED_FALSE_POSTURES:
            self.assertIs(state[field], False)
        self.assert_canonical_false_non_claims(result)
        self.assert_omission_posture(result)

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assert_check_counts(result)
        self.assert_all_emitted_codes_public(result)

    def assert_declared(self, result: Mapping[str, Any]) -> dict[str, Any]:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_DECLARED)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("declaration_result"),
            resolver.DECLARATION_RESULT_DECLARED,
        )
        for field in BRANCH_TRUE_FIELDS:
            self.assertIs(state.get(field), True)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_declaration_recorded"
            ),
            True,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_declared"),
            True,
        )
        basis = result.get(resolver.DECLARED_BASIS_SECTION)
        self.assertIsInstance(basis, dict)
        self.assertEqual(basis, self.prepared_candidate())
        self.assertEqual(len(basis), 21)
        self.assertEqual(set(basis), set(resolver.CANDIDATE_FIELDS))
        self.assert_operation_false(result)
        return basis

    def assert_not_declared(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_DECLARED)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("declaration_result"),
            resolver.DECLARATION_RESULT_NOT_DECLARED,
        )
        for field in BRANCH_TRUE_FIELDS:
            self.assertIs(state.get(field), True)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_declaration_recorded"
            ),
            False,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_declared"),
            False,
        )
        self.assertNotIn(resolver.DECLARED_BASIS_SECTION, result)
        decision = result.get("declaration_decision")
        self.assertIsInstance(decision, Mapping)
        self.assertEqual(decision.get("code"), "DECLARATION_NOT_SELECTED")
        self.assertIn("not selected", decision.get("reason", ""))
        self.assert_operation_false(result)

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        state = self.state(result)
        self.assertEqual(
            state.get("declaration_result"),
            resolver.DECLARATION_RESULT_NOT_EVALUATED,
        )
        for field in BRANCH_TRUE_FIELDS:
            self.assertIs(state.get(field), False)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_declaration_recorded"
            ),
            False,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_declared"),
            False,
        )
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(block.get("code"), expected_code)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        self.assertNotIn(resolver.DECLARED_BASIS_SECTION, result)
        self.assert_operation_false(result)
        self.assert_check_counts(result)
        self.assert_all_emitted_codes_public(result)

    @contextmanager
    def isolated_inputs(
        self,
    ) -> Iterator[tuple[Path, Path, Path]]:
        with tempfile.TemporaryDirectory(dir=self.root) as directory:
            isolated_root = Path(directory)
            specification = isolated_root / SPECIFICATION_RELATIVE_PATH
            artifact = isolated_root / PREPARATION_ARTIFACT_RELATIVE_PATH
            specification.parent.mkdir(parents=True, exist_ok=True)
            artifact.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(
                REPOSITORY_ROOT / SPECIFICATION_RELATIVE_PATH,
                specification,
            )
            shutil.copy2(
                REPOSITORY_ROOT / PREPARATION_ARTIFACT_RELATIVE_PATH,
                artifact,
            )
            with (
                patch.object(resolver, "REPO_ROOT", isolated_root),
                patch.object(
                    resolver,
                    "GOVERNING_SPECIFICATION_PATH",
                    specification,
                ),
                patch.object(
                    resolver,
                    "SELECTED_PREPARATION_ARTIFACT_PATH",
                    artifact,
                ),
                patch.object(
                    resolver,
                    "OUTPUT_ROOT",
                    isolated_root / OUTPUT_RELATIVE_ROOT,
                ),
            ):
                yield isolated_root, specification, artifact

    def assert_artifact_mutation_blocks(
        self,
        mutator: Callable[[dict[str, Any]], None],
        expected_code: str,
        *,
        selected: bool = True,
    ) -> None:
        with self.isolated_inputs() as (_, _, artifact_path):
            artifact = self._load_json(artifact_path)
            mutator(artifact)
            self._write_json(artifact_path, artifact)
            self.assert_blocked(
                self.invoke(self.canonical_request(selected=selected)),
                expected_code,
            )

    def safe_case_path(
        self,
        parent: Path,
        case_name: str,
        filename: str = "result.json",
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
        return parent / (safe.strip("._-") or "case") / filename

    def assert_writer_refused(
        self,
        result: Any,
        case_name: str,
    ) -> None:
        output = self.safe_case_path(
            self.root / "writer_refusals",
            case_name,
        )
        with self.assertRaises(
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError
        ):
            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
                result,
                output,
            )
        self.assertFalse(output.exists())

    def assert_preserved_sources_unchanged(self) -> None:
        current = {
            relative: self._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        self.assertEqual(current, self.preserved_hashes)

    def test_01_public_api_and_constant_contract(self) -> None:
        public_callables = (
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min_request",
            "build_declared_receiver_side_answerable_basis_receiver_"
            "attestation_operation_basis_declaration_v0_min_request",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min_from_path",
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min_summary",
            "write_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min_result",
        )
        for name in public_callables:
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(
            issubclass(
                resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError,
                Exception,
            )
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_v0_min",
        )
        self.assertEqual(len(resolver.CANDIDATE_FIELDS), 21)
        self.assertEqual(len(resolver.REQUIRED_BASIS_NON_CLAIMS), 39)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_DECLARED,
                resolver.OUTCOME_NOT_DECLARED,
                resolver.OUTCOME_BLOCKED,
            },
        )
        self.assertEqual(
            set(resolver.DECLARATION_RESULT_FAMILY),
            {
                resolver.DECLARATION_RESULT_DECLARED,
                resolver.DECLARATION_RESULT_NOT_DECLARED,
                resolver.DECLARATION_RESULT_NOT_EVALUATED,
            },
        )

    def test_02_canonical_request_builder_schema_and_values(self) -> None:
        request = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        expected_keys = {
            resolver.REQUEST_SELECTION_FIELD,
            "declared_non_claims",
            "declaration_id",
            "declaration_type",
            "declaration_version",
            "declaration_scope",
            "selected_preparation_id",
            "selected_preparation_type",
            "selected_preparation_version",
            "selected_preparation_scope",
            "selected_preparation_request_id",
            "selected_preparation_request_type",
            "selected_preparation_request_version",
            "selected_preparation_request_scope",
            "selected_receiver_attestation_operation_id",
            "selected_receiver_attestation_operation_type",
            "selected_receiver_attestation_operation_version",
            "selected_receiver_attestation_operation_scope",
            "receiver_side_answerable_basis_candidate_id",
            "receiver_side_answerable_basis_candidate_type",
            "receiver_side_answerable_basis_candidate_scope",
            "governing_declaration_specification_path",
            "selected_preparation_artifact_path",
            *resolver.PROHIBITED_INPUT_FLAGS,
        }
        self.assertEqual(set(request), expected_keys)
        self.assertIs(request[resolver.REQUEST_SELECTION_FIELD], True)
        self.assertEqual(
            request["governing_declaration_specification_path"],
            str(SPECIFICATION_RELATIVE_PATH),
        )
        self.assertEqual(
            request["selected_preparation_artifact_path"],
            str(PREPARATION_ARTIFACT_RELATIVE_PATH),
        )
        self.assertTrue(
            all(request[field] is False for field in resolver.PROHIBITED_INPUT_FLAGS)
        )
        self.assertEqual(
            set(request["declared_non_claims"]),
            set(resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(value is False for value in request["declared_non_claims"].values())
        )
        for prohibited_payload in (
            "prepared_declaration_candidate",
            "candidate_sha256",
            "trace_integrity_postures",
            "raw_source_body",
        ):
            self.assertNotIn(prohibited_payload, request)

    def test_03_canonical_request_builders_are_independent(self) -> None:
        first = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        second = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"],
            second["declared_non_claims"],
        )
        first["declared_non_claims"][
            resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        first[resolver.REQUEST_SELECTION_FIELD] = False
        third = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_request()
        )
        self.assertIs(third[resolver.REQUEST_SELECTION_FIELD], True)
        self.assertTrue(
            all(value is False for value in third["declared_non_claims"].values())
        )

    def test_04_declared_request_builder_keeps_visible_overrides(self) -> None:
        supplied = {"nested": ["unchanged"]}
        supplied_before = copy.deepcopy(supplied)
        false_request = self.canonical_request(selected=False)
        self.assertIs(false_request[resolver.REQUEST_SELECTION_FIELD], False)
        self.assert_not_declared(self.invoke(false_request))

        unknown = self.canonical_request(unknown_override=supplied)
        self.assertEqual(unknown["unknown_override"], supplied)
        self.assert_blocked(self.invoke(unknown), "REQUEST_FIELD_UNKNOWN")
        self.assertEqual(supplied, supplied_before)

        wrong = self.canonical_request(declaration_id="wrong")
        self.assertEqual(wrong["declaration_id"], "wrong")
        self.assert_blocked(
            self.invoke(wrong),
            "DECLARATION_IDENTITY_MISMATCH",
        )
        prohibited = self.canonical_request(candidate_digest_supplied=True)
        self.assertIs(prohibited["candidate_digest_supplied"], True)
        self.assert_blocked(
            self.invoke(prohibited),
            "PROHIBITED_CALLER_DIGEST",
        )
        false_like = self.canonical_request(selected=0)
        self.assertIs(type(false_like[resolver.REQUEST_SELECTION_FIELD]), int)
        self.assert_blocked(
            self.invoke(false_like),
            "DECLARATION_SELECTION_INVALID",
        )

    def test_05_canonical_declared_branch(self) -> None:
        result = self.invoke(self.canonical_request())
        basis = self.assert_declared(result)
        state = self.state(result)
        self.assertIs(state[resolver.REQUEST_SELECTION_FIELD], True)
        self.assertIs(state["specification_markers_validated"], True)
        self.assertIs(state["selected_preparation_artifact_validated"], True)
        self.assertIs(state["exact_21_field_candidate_validated"], True)
        self.assertEqual(
            result["declaration_decision"]["code"],
            "BASIS_DECLARED",
        )
        self.assertEqual(basis, self.prepared_candidate())

    def test_06_declared_basis_is_a_safe_deep_copy(self) -> None:
        upstream_before = self.preparation_artifact()
        result = self.invoke(self.canonical_request())
        basis = self.assert_declared(result)
        basis["trace_integrity_postures"][
            "archive_correspondence_claimed"
        ] = False
        basis["basis_non_claims"]["identity_created"] = True
        self.assertEqual(self.preparation_artifact(), upstream_before)
        next_result = self.invoke(self.canonical_request())
        next_basis = self.assert_declared(next_result)
        self.assertIs(
            next_basis["trace_integrity_postures"][
                "archive_correspondence_claimed"
            ],
            True,
        )
        self.assertIs(
            next_basis["basis_non_claims"]["identity_created"],
            False,
        )

    def test_07_canonical_not_declared_branch(self) -> None:
        result = self.invoke(self.canonical_request(selected=False))
        self.assert_not_declared(result)
        state = self.state(result)
        self.assertIs(state[resolver.REQUEST_SELECTION_FIELD], False)
        self.assertIs(state["receiver_attestation_recorded"], False)
        self.assertIs(state["receiver_attestation_not_recorded"], False)
        self.assertIs(state["receiver_attestation_indeterminate"], False)

    def test_08_canonical_blocked_branch(self) -> None:
        request = self.canonical_request()
        request["unknown_field"] = True
        result = self.invoke(request)
        self.assert_blocked(result, "REQUEST_FIELD_UNKNOWN")
        self.assertEqual(
            self.state(result)["declaration_result"],
            "NOT_EVALUATED",
        )

    def test_09_structural_invalidity_precedes_selection(self) -> None:
        invalid_false = self.canonical_request(selected=False)
        invalid_false.pop("declaration_id")
        self.assert_blocked(
            self.invoke(invalid_false),
            "REQUEST_FIELD_MISSING",
        )
        self.assert_not_declared(
            self.invoke(self.canonical_request(selected=False))
        )
        self.assert_declared(self.invoke(self.canonical_request(selected=True)))
        caller_result = self.canonical_request(
            declaration_result_selected_by_caller=True,
        )
        self.assert_blocked(
            self.invoke(caller_result),
            "PROHIBITED_RESULT_PRECLAIM",
        )

    def test_10_prepared_candidate_is_not_supplied_basis(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        state = self.state(result)
        self.assertIs(
            state["receiver_attestation_operation_basis_supplied"],
            False,
        )
        self.assertIs(
            result[STATEMENT_KEY]["declared_basis_is_not_supplied_basis"],
            True,
        )
        self.assertIn(
            "prepared candidate directly to supplied basis",
            result["blocked_routes"],
        )

    def test_11_declared_basis_is_not_admitted_basis(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        self.assertIs(
            self.state(result)[
                "receiver_attestation_operation_basis_admitted"
            ],
            False,
        )
        self.assertIs(
            result[STATEMENT_KEY]["supplied_basis_is_not_admitted_basis"],
            True,
        )

    def test_12_declaration_does_not_execute_operation(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        state = self.state(result)
        for field in (
            "receiver_attestation_operation_executed",
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
        ):
            self.assertIs(state[field], False)
        self.assertIs(
            result[NON_MEANING_KEY]["declaration_does_not_execute_operation"],
            True,
        )

    def test_13_selection_requires_exact_builtin_boolean(self) -> None:
        for value in (None, 0, 1, "false", "true", [], {}, ()):
            with self.subTest(value=repr(value)):
                request = self.canonical_request()
                request[resolver.REQUEST_SELECTION_FIELD] = value
                self.assert_blocked(
                    self.invoke(request),
                    "DECLARATION_SELECTION_INVALID",
                )
        self.assert_not_declared(
            self.invoke(self.canonical_request(selected=False))
        )
        self.assert_declared(self.invoke(self.canonical_request(selected=True)))

    def test_14_request_mapping_missing_and_unknown_failures(self) -> None:
        self.assert_declared(self.invoke(None))
        for value in ([], "request", 1):
            with self.subTest(non_mapping=repr(value)):
                self.assert_blocked(
                    self.invoke(value),
                    "REQUEST_NOT_MAPPING",
                )
        missing = self.canonical_request()
        missing.pop("declaration_scope")
        self.assert_blocked(self.invoke(missing), "REQUEST_FIELD_MISSING")
        unknown = self.canonical_request()
        unknown["candidate"] = {}
        self.assert_blocked(self.invoke(unknown), "REQUEST_FIELD_UNKNOWN")

    def test_15_request_identity_and_path_failure_matrix(self) -> None:
        expectations = {
            "declaration_id": "DECLARATION_IDENTITY_MISMATCH",
            "declaration_type": "DECLARATION_IDENTITY_MISMATCH",
            "declaration_version": "DECLARATION_IDENTITY_MISMATCH",
            "declaration_scope": "DECLARATION_IDENTITY_MISMATCH",
            "selected_preparation_id": "PREPARATION_IDENTITY_MISMATCH",
            "selected_preparation_type": "PREPARATION_IDENTITY_MISMATCH",
            "selected_preparation_version": "PREPARATION_IDENTITY_MISMATCH",
            "selected_preparation_scope": "PREPARATION_IDENTITY_MISMATCH",
            "selected_preparation_request_id": (
                "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            ),
            "selected_preparation_request_type": (
                "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            ),
            "selected_preparation_request_version": (
                "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            ),
            "selected_preparation_request_scope": (
                "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            ),
            "selected_receiver_attestation_operation_id": (
                "SELECTED_OPERATION_IDENTITY_MISMATCH"
            ),
            "selected_receiver_attestation_operation_type": (
                "SELECTED_OPERATION_IDENTITY_MISMATCH"
            ),
            "selected_receiver_attestation_operation_version": (
                "SELECTED_OPERATION_IDENTITY_MISMATCH"
            ),
            "selected_receiver_attestation_operation_scope": (
                "SELECTED_OPERATION_IDENTITY_MISMATCH"
            ),
            "receiver_side_answerable_basis_candidate_id": (
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
            ),
            "receiver_side_answerable_basis_candidate_type": (
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
            ),
            "receiver_side_answerable_basis_candidate_scope": (
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
            ),
            "governing_declaration_specification_path": (
                "GOVERNING_SPECIFICATION_PATH_MISMATCH"
            ),
            "selected_preparation_artifact_path": (
                "PREPARATION_IDENTITY_MISMATCH"
            ),
        }
        for field, code in expectations.items():
            with self.subTest(field=field):
                request = self.canonical_request()
                request[field] = f"wrong_{field}"
                self.assert_blocked(self.invoke(request), code)

    def test_16_every_prohibited_input_true_blocks(self) -> None:
        for field, expected_code in resolver.PROHIBITED_INPUT_FLAGS.items():
            with self.subTest(field=field):
                request = self.canonical_request()
                request[field] = True
                self.assert_blocked(self.invoke(request), expected_code)

    def test_17_prohibited_inputs_require_exact_false(self) -> None:
        representative = (
            "replacement_candidate_supplied",
            "candidate_digest_supplied",
            "candidate_posture_maps_supplied",
            "declaration_result_selected_by_caller",
            "preparation_replay_requested",
            "basis_supply_preclaimed",
            "receiver_attestation_preclaimed",
            "identity_preclaimed",
            "custody_preclaimed",
            "provenance_preclaimed",
            "authority_preclaimed",
            "truth_preclaimed",
            "repeat_permission_requested",
            "repository_scan_requested",
            "archive_bytes_embedded",
        )
        for field in representative:
            self.assertIn(field, resolver.PROHIBITED_INPUT_FLAGS)
            for value in (0, "false", None):
                with self.subTest(field=field, value=repr(value)):
                    request = self.canonical_request()
                    request[field] = value
                    self.assert_blocked(
                        self.invoke(request),
                        "REQUEST_VALUE_MISMATCH",
                    )

    def test_18_request_non_claims_canonical_mapping_passes(self) -> None:
        request = self.canonical_request()
        non_claims = request["declared_non_claims"]
        self.assertEqual(
            set(non_claims),
            set(resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS),
        )
        for field in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(type(non_claims[field]), bool)
            self.assertIs(non_claims[field], False)
        self.assert_declared(self.invoke(request))

    def test_19_request_non_claim_shape_and_type_failures(self) -> None:
        canonical = self.canonical_request()["declared_non_claims"]
        first = next(iter(canonical))
        variants: list[tuple[str, Any]] = []
        missing = copy.deepcopy(canonical)
        missing.pop(first)
        variants.append(("missing", missing))
        additional = copy.deepcopy(canonical)
        additional["unknown_non_claim"] = False
        variants.append(("additional", additional))
        for value in (True, 0, "false", None):
            altered = copy.deepcopy(canonical)
            altered[first] = value
            variants.append((f"value_{value!r}", altered))
        variants.extend((("sequence", []), ("null", None)))
        for name, value in variants:
            with self.subTest(case=name):
                request = self.canonical_request()
                request["declared_non_claims"] = value
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )

    def test_20_specification_exact_markers_pass(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        validation = result["specification_marker_validation"]
        self.assertIs(validation["specification_markers_validated"], True)
        self.assertTrue(all(validation["marker_status"].values()))
        self.assertEqual(
            set(validation["marker_status"]),
            set(resolver.SPECIFICATION_MARKER_CLASSES),
        )
        self.assertIs(validation["complete_specification_body_omitted"], True)

    def test_21_each_specification_marker_class_is_required(self) -> None:
        for marker_class, markers in resolver.SPECIFICATION_MARKER_CLASSES.items():
            with self.subTest(marker_class=marker_class):
                with self.isolated_inputs() as (_, specification, _):
                    original = specification.read_text(encoding="utf-8")
                    marker = markers[0]
                    self.assertIn(marker, original)
                    altered = original.replace(
                        marker,
                        f"REMOVED_{marker_class}",
                    )
                    self._write_text(specification, altered)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "SPECIFICATION_MARKER_MISSING",
                    )

    def test_22_candidate_posture_and_nonclaim_markers_are_exact(self) -> None:
        markers = (
            *resolver.CANDIDATE_FIELDS,
            *resolver.TRACE_INTEGRITY_POSTURE_KEYS,
            *resolver.AMBIGUITY_POSTURE_KEYS,
            *resolver.CONTRADICTION_POSTURE_KEYS,
            *resolver.UNRESOLVED_POSTURE_KEYS,
            *resolver.REQUIRED_BASIS_NON_CLAIMS,
        )
        for index, marker in enumerate(markers):
            with self.subTest(index=index, marker=marker):
                with self.isolated_inputs() as (_, specification, _):
                    original = specification.read_text(encoding="utf-8")
                    self.assertIn(marker, original)
                    self._write_text(
                        specification,
                        original.replace(marker, f"REMOVED_MARKER_{index}"),
                    )
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "SPECIFICATION_MARKER_MISSING",
                    )

    def test_23_specification_missing_and_non_file_block(self) -> None:
        with self.isolated_inputs() as (_, specification, _):
            specification.unlink()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "SPECIFICATION_NOT_AVAILABLE",
            )
        with self.isolated_inputs() as (_, specification, _):
            specification.unlink()
            specification.mkdir()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "SPECIFICATION_NOT_AVAILABLE",
            )

    def test_24_preparation_artifact_file_and_json_failures(self) -> None:
        cases = (
            ("missing", None, "PREPARATION_ARTIFACT_NOT_AVAILABLE"),
            ("directory", "directory", "PREPARATION_ARTIFACT_NOT_AVAILABLE"),
            ("malformed", "{", "PREPARATION_ARTIFACT_NOT_PARSEABLE"),
            (
                "duplicate",
                '{"x": 1, "x": 2}\n',
                "PREPARATION_ARTIFACT_NOT_PARSEABLE",
            ),
            ("array", "[]\n", "PREPARATION_ARTIFACT_NOT_MAPPING"),
        )
        for name, replacement, expected in cases:
            with self.subTest(case=name):
                with self.isolated_inputs() as (_, _, artifact):
                    artifact.unlink()
                    if replacement == "directory":
                        artifact.mkdir()
                    elif replacement is not None:
                        self._write_text(artifact, replacement)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        expected,
                    )

    def test_25_preparation_artifact_root_metadata_is_exact(self) -> None:
        cases = (
            (
                "resolver_module",
                "wrong",
                "PREPARATION_ARTIFACT_METADATA_MISMATCH",
            ),
            (
                "result_version",
                "9.9.9",
                "PREPARATION_ARTIFACT_METADATA_MISMATCH",
            ),
            (
                "failed_check_count",
                1,
                "PREPARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
            ),
            (
                "failed_check_count",
                False,
                "PREPARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
            ),
        )
        for field, value, code in cases:
            with self.subTest(field=field, value=repr(value)):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field, v=value: artifact.__setitem__(
                        f, v
                    ),
                    code,
                )

    def test_26_preparation_metadata_identity_is_exact(self) -> None:
        metadata_key = f"{resolver.PREPARATION_PREFIX}_metadata"
        for field in (
            "preparation_id",
            "preparation_type",
            "preparation_version",
            "preparation_scope",
        ):
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        metadata_key
                    ].__setitem__(f, f"wrong_{f}"),
                    "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
                )

    def test_27_preparation_selected_identity_is_exact(self) -> None:
        identity_key = (
            "selected_preparation_request_operation_candidate_identity"
        )
        fields = (
            "selected_preparation_request_id",
            "selected_preparation_request_type",
            "selected_preparation_request_version",
            "selected_preparation_request_scope",
            "selected_operation_id",
            "selected_operation_type",
            "selected_operation_version",
            "selected_operation_scope",
            "selected_candidate_id",
            "selected_candidate_type",
            "selected_candidate_scope",
        )
        for field in fields:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        identity_key
                    ].__setitem__(f, f"wrong_{f}"),
                    "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
                )

    def test_28_preparation_state_identity_is_exact(self) -> None:
        fields = (
            "preparation_id",
            "preparation_type",
            "preparation_version",
            "preparation_scope",
            "selected_preparation_request_id",
            "selected_receiver_attestation_operation_id",
            "receiver_side_answerable_basis_candidate_id",
        )
        for field in fields:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        resolver.PREPARATION_PREFIX
                    ].__setitem__(f, f"wrong_{f}"),
                    "PREPARATION_ARTIFACT_IDENTITY_MISMATCH",
                )

    def test_29_preparation_outcome_decision_and_block_are_exact(self) -> None:
        mutations = (
            (
                "outcome",
                lambda artifact: artifact.__setitem__("outcome", "wrong"),
                "PREPARATION_ARTIFACT_NOT_PREPARED",
            ),
            (
                "preparation_result",
                lambda artifact: artifact[
                    resolver.PREPARATION_PREFIX
                ].__setitem__("preparation_result", "wrong"),
                "PREPARATION_ARTIFACT_NOT_PREPARED",
            ),
            (
                "state_decision",
                lambda artifact: artifact[
                    resolver.PREPARATION_PREFIX
                ].__setitem__("decision_code", "wrong"),
                "PREPARATION_ARTIFACT_NOT_PREPARED",
            ),
            (
                "decision_code",
                lambda artifact: artifact[
                    "preparation_decision"
                ].__setitem__("code", "wrong"),
                "PREPARATION_ARTIFACT_NOT_PREPARED",
            ),
            (
                "caller_selected",
                lambda artifact: artifact[
                    "preparation_decision"
                ].__setitem__("caller_selected_result", True),
                "PREPARATION_ARTIFACT_NOT_PREPARED",
            ),
            (
                "blocked",
                lambda artifact: artifact["block"].__setitem__(
                    "blocked", True
                ),
                "PREPARATION_ARTIFACT_BLOCKED",
            ),
            (
                "blocked_wrong_type",
                lambda artifact: artifact["block"].__setitem__(
                    "blocked", 0
                ),
                "PREPARATION_ARTIFACT_BLOCKED",
            ),
        )
        for name, mutation, code in mutations:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutation, code)

    def test_30_preparation_required_true_state_postures_are_exact(self) -> None:
        for field in PREPARATION_REQUIRED_TRUE_FIELDS:
            for value in (False, 1):
                with self.subTest(field=field, value=repr(value)):
                    self.assert_artifact_mutation_blocks(
                        lambda artifact, f=field, v=value: artifact[
                            resolver.PREPARATION_PREFIX
                        ].__setitem__(f, v),
                        "PREPARATION_ARTIFACT_POSTURE_INVALID",
                    )

    def test_31_preparation_required_false_state_postures_are_exact(self) -> None:
        for field in PREPARATION_REQUIRED_FALSE_FIELDS:
            for value in (True, 0):
                with self.subTest(field=field, value=repr(value)):
                    self.assert_artifact_mutation_blocks(
                        lambda artifact, f=field, v=value: artifact[
                            resolver.PREPARATION_PREFIX
                        ].__setitem__(f, v),
                        "PREPARATION_ARTIFACT_POSTURE_INVALID",
                    )

    def test_32_preparation_summary_true_postures_are_exact(self) -> None:
        summary_key = f"{resolver.PREPARATION_PREFIX}_summary"
        for field in PREPARATION_SUMMARY_TRUE_FIELDS:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        summary_key
                    ].__setitem__(f, False),
                    "PREPARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_33_preparation_summary_false_postures_are_exact(self) -> None:
        summary_key = f"{resolver.PREPARATION_PREFIX}_summary"
        for field in PREPARATION_SUMMARY_FALSE_FIELDS:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        summary_key
                    ].__setitem__(f, True),
                    "PREPARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_34_preparation_validation_sections_are_exact(self) -> None:
        locations = (
            (
                "specification_marker_validation",
                "specification_markers_validated",
            ),
            (
                "preparation_request_artifact_validation",
                "preparation_request_artifact_validated",
            ),
            (
                "selected_boundary_reference_validation",
                "selected_boundary_reference_validated",
            ),
            ("bounded_path_and_file_evaluation", "bounded_paths_validated"),
            (
                "bounded_path_and_file_evaluation",
                "required_bounded_components_available",
            ),
            (
                "bounded_path_and_file_evaluation",
                "complete_21_field_candidate_preparable",
            ),
        )
        for section, field in locations:
            with self.subTest(section=section, field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, s=section, f=field: artifact[
                        s
                    ].__setitem__(f, False),
                    "PREPARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_35_historically_sensitive_false_locks_are_exact(self) -> None:
        for field in SENSITIVE_FALSE_FIELDS:
            for location in (resolver.PREPARATION_PREFIX, "non_claims"):
                with self.subTest(field=field, location=location):
                    expected = (
                        "PREPARATION_ARTIFACT_POSTURE_INVALID"
                        if location == resolver.PREPARATION_PREFIX
                        else "PREPARATION_ARTIFACT_NON_CLAIM_NOT_FALSE"
                    )
                    self.assert_artifact_mutation_blocks(
                        lambda artifact, f=field, where=location: artifact[
                            where
                        ].__setitem__(f, True),
                        expected,
                    )
        self.assert_artifact_mutation_blocks(
            lambda artifact: artifact["non_claims"].__setitem__(
                "validation_enforced", 0
            ),
            "PREPARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
        )

    def test_36_preparation_artifact_non_claims_are_exact(self) -> None:
        canonical = self.preparation_artifact()["non_claims"]
        first = next(iter(canonical))

        def mutate_missing(artifact: dict[str, Any]) -> None:
            artifact["non_claims"].pop(first)

        def mutate_additional(artifact: dict[str, Any]) -> None:
            artifact["non_claims"]["additional"] = False

        mutations: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
            ("missing", mutate_missing),
            ("additional", mutate_additional),
            (
                "true",
                lambda artifact: artifact["non_claims"].__setitem__(
                    first, True
                ),
            ),
            (
                "integer",
                lambda artifact: artifact["non_claims"].__setitem__(
                    first, 0
                ),
            ),
            (
                "string",
                lambda artifact: artifact["non_claims"].__setitem__(
                    first, "false"
                ),
            ),
            (
                "null",
                lambda artifact: artifact["non_claims"].__setitem__(
                    first, None
                ),
            ),
            (
                "wrong_container",
                lambda artifact: artifact.__setitem__("non_claims", []),
            ),
        )
        for name, mutation in mutations:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(
                    mutation,
                    (
                        "PREPARATION_ARTIFACT_NOT_MAPPING"
                        if name == "wrong_container"
                        else "PREPARATION_ARTIFACT_NON_CLAIM_NOT_FALSE"
                    ),
                )

    def test_37_preparation_artifact_omission_is_exact(self) -> None:
        first = resolver.UPSTREAM_OMISSION_FIELDS[0]

        def remove(artifact: dict[str, Any]) -> None:
            artifact["omission_posture"].pop(first)

        def add(artifact: dict[str, Any]) -> None:
            artifact["omission_posture"]["additional"] = True

        mutations = (
            ("missing", remove),
            ("additional", add),
            (
                "false",
                lambda artifact: artifact["omission_posture"].__setitem__(
                    first, False
                ),
            ),
            (
                "wrong_type",
                lambda artifact: artifact["omission_posture"].__setitem__(
                    first, 1
                ),
            ),
        )
        for name, mutation in mutations:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(
                    mutation,
                    "PREPARATION_ARTIFACT_OMISSION_INVALID",
                )

    def test_38_exact_prepared_candidate_schema_and_source(self) -> None:
        artifact = self.preparation_artifact()
        prepared = artifact["prepared_declaration_candidate"]
        result = self.invoke(self.canonical_request())
        declared = self.assert_declared(result)
        self.assertEqual(declared, prepared)
        self.assertEqual(tuple(declared), tuple(prepared))
        self.assertEqual(len(declared), 21)
        self.assertEqual(set(declared), set(resolver.CANDIDATE_FIELDS))
        request = self.canonical_request(
            prepared_declaration_candidate=prepared
        )
        self.assert_blocked(self.invoke(request), "REQUEST_FIELD_UNKNOWN")
        replacement = self.canonical_request(
            replacement_candidate_supplied=True
        )
        self.assert_blocked(
            self.invoke(replacement),
            "PROHIBITED_CALLER_CANDIDATE",
        )

    def test_39_prepared_candidate_shape_and_container_failures(self) -> None:
        first = resolver.CANDIDATE_FIELDS[0]

        def remove(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"].pop(first)

        def add(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"]["additional"] = False

        mutations = (
            ("missing_field", remove, "PREPARED_CANDIDATE_SCHEMA_MISMATCH"),
            ("added_field", add, "PREPARED_CANDIDATE_SCHEMA_MISMATCH"),
            (
                "list",
                lambda artifact: artifact.__setitem__(
                    "prepared_declaration_candidate", []
                ),
                "PREPARED_CANDIDATE_MISSING",
            ),
            (
                "null",
                lambda artifact: artifact.__setitem__(
                    "prepared_declaration_candidate", None
                ),
                "PREPARED_CANDIDATE_MISSING",
            ),
        )
        for name, mutation, code in mutations:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutation, code)

    def test_40_candidate_references_and_evaluator_are_exact(self) -> None:
        reference_cases = (
            "selected_receiver_attestation_boundary_artifact_path",
            "bounded_capture_directory_path",
            "expected_archive_sha256",
            "preserved_archive_path",
            "recorded_signal_path",
        )
        for field in reference_cases:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, f=field: artifact[
                        "prepared_declaration_candidate"
                    ].__setitem__(f, f"alternate/{f}"),
                    "PREPARED_CANDIDATE_REFERENCE_MISMATCH",
                )
        self.assert_artifact_mutation_blocks(
            lambda artifact: artifact[
                "prepared_declaration_candidate"
            ].__setitem__(
                "bounded_capture_directory_path",
                str(
                    Path(
                        resolver.EXACT_CANDIDATE_REFERENCES[
                            "bounded_capture_directory_path"
                        ]
                    )
                    / ".."
                    / Path(
                        resolver.EXACT_CANDIDATE_REFERENCES[
                            "bounded_capture_directory_path"
                        ]
                    ).name
                ),
            ),
            "PREPARED_CANDIDATE_REFERENCE_MISMATCH",
        )
        self.assert_artifact_mutation_blocks(
            lambda artifact: artifact[
                "prepared_declaration_candidate"
            ].__setitem__("evaluator_reference", "alternate"),
            "PREPARED_CANDIDATE_EVALUATOR_REFERENCE_MISMATCH",
        )

    def assert_posture_map_failures(self, family: str) -> None:
        expected = dict(
            {
                "trace_integrity_postures": (
                    resolver.EXPECTED_TRACE_INTEGRITY_POSTURES
                ),
                "ambiguity_postures": resolver.EXPECTED_AMBIGUITY_POSTURES,
                "contradiction_postures": (
                    resolver.EXPECTED_CONTRADICTION_POSTURES
                ),
                "unresolved_postures": resolver.EXPECTED_UNRESOLVED_POSTURES,
            }[family]
        )
        first = next(iter(expected))

        def remove_family(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"].pop(family)

        def add_candidate_field(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"][
                "additional_posture_map"
            ] = {}

        def remove_key(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"][family].pop(first)

        def add_key(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"][family][
                "additional"
            ] = False

        variants = (
            (
                "missing_family",
                remove_family,
                "PREPARED_CANDIDATE_SCHEMA_MISMATCH",
            ),
            (
                "additional_candidate_field",
                add_candidate_field,
                "PREPARED_CANDIDATE_SCHEMA_MISMATCH",
            ),
            (
                "missing_key",
                remove_key,
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "additional_key",
                add_key,
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "wrong_boolean",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ][family].__setitem__(first, not expected[first]),
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "integer",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ][family].__setitem__(first, int(expected[first])),
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "string",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ][family].__setitem__(first, str(expected[first]).lower()),
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "null",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ][family].__setitem__(first, None),
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
            (
                "wrong_container",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ].__setitem__(family, []),
                "PREPARED_CANDIDATE_POSTURE_MISMATCH",
            ),
        )
        for name, mutation, code in variants:
            with self.subTest(family=family, case=name):
                self.assert_artifact_mutation_blocks(mutation, code)

    def test_41_trace_integrity_posture_map_is_exact(self) -> None:
        self.assert_posture_map_failures("trace_integrity_postures")

    def test_42_ambiguity_posture_map_is_exact(self) -> None:
        self.assert_posture_map_failures("ambiguity_postures")

    def test_43_contradiction_posture_map_is_exact(self) -> None:
        self.assert_posture_map_failures("contradiction_postures")

    def test_44_unresolved_posture_map_is_exact(self) -> None:
        self.assert_posture_map_failures("unresolved_postures")

    def test_45_non_conversion_statement_is_exact(self) -> None:
        candidate = self.prepared_candidate()
        self.assertEqual(
            candidate["non_conversion_statement"],
            resolver.NON_CONVERSION_STATEMENT,
        )
        variants = (
            resolver.NON_CONVERSION_STATEMENT[:-1],
            resolver.NON_CONVERSION_STATEMENT + " ",
            resolver.NON_CONVERSION_STATEMENT.capitalize(),
            resolver.NON_CONVERSION_STATEMENT.replace(
                "standing.", "standing"
            ),
            None,
        )
        for value in variants:
            with self.subTest(value=repr(value)):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, v=value: artifact[
                        "prepared_declaration_candidate"
                    ].__setitem__("non_conversion_statement", v),
                    "PREPARED_CANDIDATE_NON_CONVERSION_MISMATCH",
                )

    def test_46_basis_non_claims_are_exact(self) -> None:
        canonical = self.prepared_candidate()["basis_non_claims"]
        self.assertEqual(len(canonical), 39)
        self.assertEqual(set(canonical), set(resolver.REQUIRED_BASIS_NON_CLAIMS))
        self.assertNotIn("receiver_attestation_recorded", canonical)
        first = resolver.REQUIRED_BASIS_NON_CLAIMS[0]

        def remove(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"][
                "basis_non_claims"
            ].pop(first)

        def add(artifact: dict[str, Any]) -> None:
            artifact["prepared_declaration_candidate"]["basis_non_claims"][
                "additional"
            ] = False

        variants = (
            ("missing", remove),
            ("additional", add),
            (
                "declaration_key",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ]["basis_non_claims"].__setitem__(
                    "receiver_attestation_recorded", False
                ),
            ),
            (
                "true",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ]["basis_non_claims"].__setitem__(first, True),
            ),
            (
                "integer",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ]["basis_non_claims"].__setitem__(first, 0),
            ),
            (
                "string",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ]["basis_non_claims"].__setitem__(first, "false"),
            ),
            (
                "null",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ]["basis_non_claims"].__setitem__(first, None),
            ),
            (
                "container",
                lambda artifact: artifact[
                    "prepared_declaration_candidate"
                ].__setitem__("basis_non_claims", []),
            ),
        )
        for name, mutation in variants:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(
                    mutation,
                    "PREPARED_CANDIDATE_NON_CLAIM_MISMATCH",
                )

    def test_47_candidate_digest_is_canonical_and_correspondence_only(
        self,
    ) -> None:
        candidate = self.prepared_candidate()
        rendered = json.dumps(
            candidate,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        expected = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
        first = self.invoke(self.canonical_request())
        second = self.invoke(self.canonical_request())
        for result in (first, second):
            self.assert_declared(result)
            digest = result["candidate_digest"]
            self.assertEqual(
                digest["candidate_digest_algorithm"],
                "SHA-256",
            )
            self.assertEqual(digest["candidate_sha256"], expected)
            self.assertRegex(digest["candidate_sha256"], r"^[0-9a-f]{64}$")
            self.assertIs(digest["caller_supplied_digest_used"], False)
            self.assertIs(digest["digest_is_correspondence_only"], True)
            state = self.state(result)
            for field in (
                "identity_created",
                "custody_created",
                "provenance_created",
                "physical_validity_created",
                "authority_created",
                "truth_created",
                "presence_established",
                "standing_created",
            ):
                self.assertIs(state[field], False)
        self.assertEqual(
            first["candidate_digest"],
            second["candidate_digest"],
        )
        supplied = self.canonical_request(candidate_digest_supplied=True)
        self.assert_blocked(
            self.invoke(supplied),
            "PROHIBITED_CALLER_DIGEST",
        )
        self.assert_artifact_mutation_blocks(
            lambda artifact: artifact[
                "prepared_declaration_candidate"
            ].__setitem__("expected_archive_sha256", "0" * 64),
            "PREPARED_CANDIDATE_REFERENCE_MISMATCH",
        )

    def test_48_result_structure_is_exact_for_every_branch(self) -> None:
        declared = self.invoke(self.canonical_request())
        not_declared = self.invoke(self.canonical_request(selected=False))
        blocked_request = self.canonical_request()
        blocked_request["unknown"] = True
        blocked = self.invoke(blocked_request)
        for name, result in (
            ("declared", declared),
            ("not_declared", not_declared),
            ("blocked", blocked),
        ):
            with self.subTest(branch=name):
                expected = set(resolver.RESULT_BASE_SECTIONS)
                if name == "declared":
                    expected.add(resolver.DECLARED_BASIS_SECTION)
                self.assertEqual(set(result), expected)
                self.assert_check_counts(result)
                self.assert_canonical_false_non_claims(result)
                self.assert_omission_posture(result)
                self.assertEqual(
                    result["what_remains_open"],
                    list(resolver.WHAT_REMAINS_OPEN),
                )
                self.assertEqual(
                    result["blocked_routes"],
                    list(resolver.BLOCKED_ROUTES),
                )
        self.assert_declared(declared)
        self.assert_not_declared(not_declared)
        self.assert_blocked(blocked, "REQUEST_FIELD_UNKNOWN")

    def test_49_determinism_input_and_result_immutability(self) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        artifact_before = self.preparation_artifact()
        first = self.invoke(request)
        second = self.invoke(request)
        self.assertEqual(first, second)
        self.assertEqual(request, request_before)
        self.assertEqual(self.preparation_artifact(), artifact_before)
        first["declaration_decision"]["reason"] = "mutated"
        first[resolver.DECLARED_BASIS_SECTION]["basis_non_claims"][
            "identity_created"
        ] = True
        self.assertNotEqual(first, second)
        self.assertEqual(request, request_before)
        self.assertEqual(self.preparation_artifact(), artifact_before)
        third = self.invoke(request)
        self.assertEqual(third, second)
        self.assertEqual(
            self.checks(third),
            self.checks(second),
        )

    def test_50_from_path_contract_and_strict_json(self) -> None:
        canonical = self.canonical_request()
        declared_path = self._write_json(
            self.root / "requests" / "declared.json",
            canonical,
        )
        declared_before = declared_path.read_bytes()
        self.assert_declared(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_from_path(
                declared_path
            )
        )
        self.assertEqual(declared_path.read_bytes(), declared_before)

        not_declared_path = self._write_json(
            self.root / "requests" / "not_declared.json",
            self.canonical_request(selected=False),
        )
        self.assert_not_declared(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_from_path(
                not_declared_path
            )
        )

        malformed = self._write_text(
            self.root / "requests" / "malformed.json",
            "{",
        )
        duplicate = self._write_text(
            self.root / "requests" / "duplicate.json",
            '{"declaration_id": "a", "declaration_id": "b"}\n',
        )
        array = self._write_text(
            self.root / "requests" / "array.json",
            "[]\n",
        )
        cases = (
            (
                malformed,
                "REQUEST_PATH_NOT_PARSEABLE",
            ),
            (
                duplicate,
                "REQUEST_PATH_NOT_PARSEABLE",
            ),
            (
                array,
                "REQUEST_NOT_MAPPING",
            ),
            (
                self.root / "requests" / "missing.json",
                "REQUEST_PATH_NOT_AVAILABLE",
            ),
        )
        for path, code in cases:
            with self.subTest(path=path.name):
                self.assert_blocked(
                    resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_from_path(
                        path
                    ),
                    code,
                )

    def test_51_summary_builder_canonical_declared_content(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        first = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
                result
            )
        )
        second = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
                result
            )
        )
        self.assertEqual(first, second)
        self.assertEqual(first, result[SUMMARY_KEY])
        expected_fields = (
            "resolver_module",
            "result_version",
            "declaration_id",
            "declaration_type",
            "declaration_version",
            "declaration_scope",
            "selected_preparation_id",
            "selected_preparation_request_id",
            "selected_operation_id",
            "selected_candidate_id",
            "governing_specification_path",
            "selected_preparation_artifact_path",
            "outcome",
            "declaration_result",
            "failed_check_count",
            "passed_check_count",
            "blocked",
            "decision_code",
            "decision_reason",
            "declaration_selection",
            "specification_markers_validated",
            "preparation_artifact_validated",
            "exact_21_field_candidate_validated",
            "candidate_digest_algorithm",
            "candidate_sha256",
            "candidate_posture_maps_validated",
            "non_conversion_statement_validated",
            "basis_non_claims_validated",
            "declaration_recorded",
            "declaration_result_recorded",
            "declaration_exhausted",
            "declaration_candidate_received",
            "operation_basis_declared",
            "operation_basis_supplied",
            "operation_basis_admitted",
            "operation_executed",
            "operation_result_recorded",
            "result_level_non_claims_canonical_false",
            "complete_material_omitted",
        )
        self.assertEqual(set(first), set(expected_fields))
        self.assertNotIn(resolver.DECLARED_BASIS_SECTION, first)
        self.assertEqual(first["candidate_sha256"], result["candidate_digest"]["candidate_sha256"])
        self.assertIs(first["operation_basis_supplied"], False)
        self.assertIs(first["operation_basis_admitted"], False)
        self.assertIs(first["operation_executed"], False)

    def test_52_summary_builder_covers_not_declared_and_blocked(self) -> None:
        blocked_request = self.canonical_request()
        blocked_request["unknown"] = True
        cases = (
            self.invoke(self.canonical_request(selected=False)),
            self.invoke(blocked_request),
        )
        for result in cases:
            with self.subTest(outcome=result["outcome"]):
                summary = (
                    resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(summary, result[SUMMARY_KEY])
                self.assertNotIn(resolver.DECLARED_BASIS_SECTION, summary)
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(
                    summary["declaration_result"],
                    self.state(result)["declaration_result"],
                )

    def test_53_summary_rejects_non_mapping_and_writer_rejects_corruption(
        self,
    ) -> None:
        for value in (None, [], "result"):
            with self.subTest(value=repr(value)):
                with self.assertRaises(
                    resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError
                ):
                    resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
                        value
                    )
        canonical = self.invoke(self.canonical_request())
        mutations = (
            ("module", "resolver_module", "wrong"),
            ("version", "result_version", "wrong"),
        )
        for name, field, value in mutations:
            with self.subTest(case=name):
                altered = copy.deepcopy(canonical)
                altered[field] = value
                summary = (
                    resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_summary(
                        altered
                    )
                )
                self.assertEqual(summary[field], value)
                self.assert_writer_refused(altered, f"summary_{name}")

    def test_54_writer_writes_every_valid_branch_exactly(self) -> None:
        blocked_request = self.canonical_request()
        blocked_request["unknown"] = True
        results = (
            self.invoke(self.canonical_request()),
            self.invoke(self.canonical_request(selected=False)),
            self.invoke(blocked_request),
        )
        for index, result in enumerate(results):
            with self.subTest(outcome=result["outcome"]):
                before = copy.deepcopy(result)
                target = (
                    self.root
                    / "writer"
                    / str(index)
                    / "nested"
                    / "result.json"
                )
                written = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
                    result,
                    target,
                )
                self.assertEqual(written, target)
                self.assertTrue(target.is_file())
                data = target.read_bytes()
                self.assertTrue(data.endswith(b"\n"))
                self.assertFalse(data.endswith(b"\n\n"))
                self.assertEqual(
                    data.decode("utf-8"),
                    json.dumps(
                        result,
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=True,
                        allow_nan=False,
                    )
                    + "\n",
                )
                loaded = json.loads(data.decode("utf-8"))
                self.assertIsInstance(loaded, dict)
                self.assertEqual(loaded, result)
                self.assertEqual(result, before)

    def test_55_writer_never_overwrites_and_uses_stable_suffix(self) -> None:
        result = self.invoke(self.canonical_request())
        target = self.root / "suffix" / "result.json"
        first = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
            result,
            target,
        )
        first_bytes = first.read_bytes()
        second = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
            result,
            target,
        )
        third = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
            result,
            target,
        )
        self.assertEqual(first, target)
        self.assertEqual(second, target.with_name("result_001.json"))
        self.assertEqual(third, target.with_name("result_002.json"))
        self.assertEqual(first.read_bytes(), first_bytes)
        self.assertEqual(json.loads(second.read_text()), result)
        self.assertEqual(json.loads(third.read_text()), result)

    def test_56_writer_refuses_branch_and_wrapper_inconsistency(self) -> None:
        declared = self.invoke(self.canonical_request())
        not_declared = self.invoke(self.canonical_request(selected=False))
        blocked_request = self.canonical_request()
        blocked_request["unknown"] = True
        blocked = self.invoke(blocked_request)

        cases: list[tuple[str, Any]] = [("non_mapping", [])]
        wrong_module = copy.deepcopy(declared)
        wrong_module["resolver_module"] = "wrong"
        cases.append(("wrong_module", wrong_module))
        wrong_version = copy.deepcopy(declared)
        wrong_version["result_version"] = "wrong"
        cases.append(("wrong_version", wrong_version))
        no_basis = copy.deepcopy(declared)
        no_basis.pop(resolver.DECLARED_BASIS_SECTION)
        cases.append(("declared_without_basis", no_basis))
        not_with_basis = copy.deepcopy(not_declared)
        not_with_basis[resolver.DECLARED_BASIS_SECTION] = self.prepared_candidate()
        cases.append(("not_declared_with_basis", not_with_basis))
        blocked_with_basis = copy.deepcopy(blocked)
        blocked_with_basis[resolver.DECLARED_BASIS_SECTION] = self.prepared_candidate()
        cases.append(("blocked_with_basis", blocked_with_basis))

        state_mutations = (
            (
                "declared_basis_false",
                declared,
                "receiver_attestation_operation_basis_declared",
                False,
            ),
            (
                "not_declared_basis_true",
                not_declared,
                "receiver_attestation_operation_basis_declared",
                True,
            ),
            (
                "blocked_recorded_true",
                blocked,
                "declaration_recorded",
                True,
            ),
            (
                "declared_result_wrong",
                declared,
                "declaration_result",
                resolver.DECLARATION_RESULT_NOT_DECLARED,
            ),
            (
                "declared_exhaustion_false",
                declared,
                "declaration_exhausted",
                False,
            ),
            (
                "basis_supplied_true",
                declared,
                "receiver_attestation_operation_basis_supplied",
                True,
            ),
            (
                "basis_admitted_true",
                declared,
                "receiver_attestation_operation_basis_admitted",
                True,
            ),
            (
                "operation_recorded_true",
                declared,
                "receiver_attestation_operation_recorded",
                True,
            ),
            (
                "operation_result_true",
                declared,
                "receiver_attestation_operation_result_recorded",
                True,
            ),
            (
                "attestation_true",
                declared,
                "receiver_attestation_recorded",
                True,
            ),
        )
        for name, source, field, value in state_mutations:
            altered = copy.deepcopy(source)
            altered[STATE_KEY][field] = value
            cases.append((name, altered))

        wrong_block = copy.deepcopy(declared)
        wrong_block["block"]["blocked"] = True
        cases.append(("wrong_block", wrong_block))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_57_writer_refuses_candidate_digest_and_posture_corruption(
        self,
    ) -> None:
        declared = self.invoke(self.canonical_request())
        cases: list[tuple[str, dict[str, Any]]] = []
        altered_basis = copy.deepcopy(declared)
        altered_basis[resolver.DECLARED_BASIS_SECTION][
            "expected_archive_sha256"
        ] = "0" * 64
        cases.append(("altered_basis", altered_basis))
        malformed_algorithm = copy.deepcopy(declared)
        malformed_algorithm["candidate_digest"][
            "candidate_digest_algorithm"
        ] = "MD5"
        cases.append(("algorithm", malformed_algorithm))
        digest_mismatch = copy.deepcopy(declared)
        digest_mismatch["candidate_digest"]["candidate_sha256"] = "0" * 64
        cases.append(("digest", digest_mismatch))
        state_digest = copy.deepcopy(declared)
        state_digest[STATE_KEY]["candidate_sha256"] = "0" * 64
        cases.append(("state_digest", state_digest))
        posture = copy.deepcopy(declared)
        posture[resolver.DECLARED_BASIS_SECTION][
            "trace_integrity_postures"
        ]["archive_correspondence_claimed"] = False
        cases.append(("posture", posture))
        nonconversion = copy.deepcopy(declared)
        nonconversion[resolver.DECLARED_BASIS_SECTION][
            "non_conversion_statement"
        ] += " "
        cases.append(("nonconversion", nonconversion))
        basis_nonclaims = copy.deepcopy(declared)
        basis_nonclaims[resolver.DECLARED_BASIS_SECTION][
            "basis_non_claims"
        ]["identity_created"] = True
        cases.append(("basis_nonclaims", basis_nonclaims))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_58_writer_refuses_nonclaims_omission_and_embedded_material(
        self,
    ) -> None:
        declared = self.invoke(self.canonical_request())
        first_nonclaim = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        first_omission = resolver.RESULT_OMISSION_FIELDS[0]
        cases: list[tuple[str, dict[str, Any]]] = []
        missing_nonclaim = copy.deepcopy(declared)
        missing_nonclaim["non_claims"].pop(first_nonclaim)
        cases.append(("missing_nonclaim", missing_nonclaim))
        flipped_nonclaim = copy.deepcopy(declared)
        flipped_nonclaim["non_claims"][first_nonclaim] = True
        cases.append(("flipped_nonclaim", flipped_nonclaim))
        missing_omission = copy.deepcopy(declared)
        missing_omission["omission_posture"].pop(first_omission)
        cases.append(("missing_omission", missing_omission))
        false_omission = copy.deepcopy(declared)
        false_omission["omission_posture"][first_omission] = False
        cases.append(("false_omission", false_omission))
        for key, value in (
            ("complete_preparation_artifact", {"secret": True}),
            ("archive_bytes", b"archive"),
            ("text_component_bodies", "body"),
            ("recorded_signal_body", {"signal": True}),
        ):
            embedded = copy.deepcopy(declared)
            embedded[key] = value
            cases.append((key, embedded))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_59_writer_refuses_every_protected_path_family(self) -> None:
        result = self.invoke(self.canonical_request())
        paths = (
            REPOSITORY_ROOT / SPECIFICATION_RELATIVE_PATH,
            REPOSITORY_ROOT / SOURCE_RELATIVE_PATH,
            REPOSITORY_ROOT / TEST_RELATIVE_PATH,
            REPOSITORY_ROOT / "reference/IAMMAI/must_not_write.json",
            REPOSITORY_ROOT / PREPARATION_ARTIFACT_RELATIVE_PATH,
            REPOSITORY_ROOT
            / resolver.SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
            REPOSITORY_ROOT
            / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH,
            REPOSITORY_ROOT / resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            REPOSITORY_ROOT
            / resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
            (
                REPOSITORY_ROOT
                / resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
            ).parent
            / "candidate_sufficiency_basis.json",
            REPOSITORY_ROOT
            / resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            / "must_not_write.json",
        )
        def path_posture(path: Path) -> tuple[bool, bool, int | None, int | None]:
            if not path.exists():
                return False, False, None, None
            status = path.stat()
            return True, path.is_file(), status.st_size, status.st_mtime_ns

        before = {path: path_posture(path) for path in paths}
        for path in paths:
            with self.subTest(path=str(path)):
                with self.assertRaises(
                    resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationV0MinError
                ):
                    resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
                        result,
                        path,
                    )
        after = {path: path_posture(path) for path in paths}
        self.assertEqual(after, before)

    def test_60_declaration_reads_no_evidence_or_upstream_siblings(self) -> None:
        original = resolver._read_text
        observed: list[Path] = []

        def tracked(value: Path | str) -> tuple[str | None, str | None]:
            path = resolver._as_repo_path(value).resolve(strict=False)
            observed.append(path)
            return original(value)

        with patch.object(resolver, "_read_text", side_effect=tracked):
            result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        expected = [
            (REPOSITORY_ROOT / SPECIFICATION_RELATIVE_PATH).resolve(),
            (REPOSITORY_ROOT / PREPARATION_ARTIFACT_RELATIVE_PATH).resolve(),
        ]
        self.assertEqual(observed, expected)
        forbidden = (
            resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH,
            resolver.SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
        )
        for relative in forbidden:
            forbidden_path = (REPOSITORY_ROOT / relative).resolve()
            self.assertNotIn(forbidden_path, observed)

    def test_61_source_specification_and_artifact_stay_unchanged(self) -> None:
        before = copy.deepcopy(self.preserved_hashes)
        self.assert_declared(self.invoke(self.canonical_request()))
        self.assert_not_declared(
            self.invoke(self.canonical_request(selected=False))
        )
        output = self.root / "stability" / "result.json"
        resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min_result(
            self.invoke(self.canonical_request()),
            output,
        )
        self.assert_preserved_sources_unchanged()
        self.assertEqual(before, self.preserved_hashes)

    def test_62_declaration_exhaustion_authorizes_no_supply(self) -> None:
        for result in (
            self.invoke(self.canonical_request()),
            self.invoke(self.canonical_request(selected=False)),
        ):
            with self.subTest(outcome=result["outcome"]):
                state = self.state(result)
                self.assertIs(state["declaration_exhausted"], True)
                self.assertIs(
                    state["receiver_attestation_operation_basis_supplied"],
                    False,
                )
                self.assertIs(
                    state["receiver_attestation_operation_basis_admitted"],
                    False,
                )
                self.assertIs(
                    result[NON_MEANING_KEY][
                        "declaration_exhaustion_does_not_authorize_supply"
                    ],
                    True,
                )
                for field in (
                    "repeated_receiver_attestation_operation_basis_"
                    "declaration_permission_created",
                    "reusable_receiver_attestation_operation_basis_"
                    "declaration_route_created",
                    "same_receiver_attestation_operation_basis_declaration_"
                    "rerun_authorized",
                    "automatic_receiver_attestation_operation_basis_"
                    "declaration_retry_created",
                ):
                    self.assertIs(state[field], False)

    def test_63_open_does_not_mean_next(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_declared(result)
        self.assertIs(result[STATEMENT_KEY]["open_does_not_mean_next"], True)
        self.assertEqual(
            result["what_remains_open"],
            list(resolver.WHAT_REMAINS_OPEN),
        )
        state = self.state(result)
        for field in (
            "follow_on_authorized",
            "follow_on_work_authorized",
            "receiver_attestation_operation_basis_supplied",
            "receiver_attestation_operation_basis_admitted",
            "receiver_attestation_operation_recorded",
        ):
            self.assertIs(state[field], False)

    def test_64_public_codes_checks_and_global_state_are_stable(self) -> None:
        canonical_request = self.canonical_request()
        canonical_nonclaims = copy.deepcopy(
            canonical_request["declared_non_claims"]
        )
        first = self.invoke(canonical_request)
        self.assert_declared(first)
        for field in resolver.PROHIBITED_INPUT_FLAGS:
            request = self.canonical_request()
            request[field] = True
            result = self.invoke(request)
            self.assert_blocked(
                result,
                resolver.PROHIBITED_INPUT_FLAGS[field],
            )
        second_request = self.canonical_request()
        second = self.invoke(second_request)
        self.assert_declared(second)
        self.assertEqual(
            second_request["declared_non_claims"],
            canonical_nonclaims,
        )
        self.assertEqual(first, second)
        self.assert_all_emitted_codes_public(second)
        self.assert_check_counts(second)


if __name__ == "__main__":
    unittest.main()
