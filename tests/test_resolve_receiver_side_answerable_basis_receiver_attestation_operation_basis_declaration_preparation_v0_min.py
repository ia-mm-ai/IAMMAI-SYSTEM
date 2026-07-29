"""Tests for one bounded receiver-attestation basis preparation.

The suite copies only the exact governing specification, upstream artifacts,
and bounded capture components into temporary roots. It proves preparation of
one 21-field candidate without declaration, supply, admission, or execution.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import stat
import sys
import tempfile
import unittest
from collections.abc import Mapping, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min as resolver


PREFIX = resolver.PREFIX
STATE_KEY = PREFIX
CHECKS_KEY = f"{PREFIX}_checks"
SUMMARY_KEY = f"{PREFIX}_summary"
STATEMENT_KEY = f"{PREFIX}_statement"

PREPARATION_SPEC_RELATIVE_PATH = (
    resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
)
PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH = (
    resolver.SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
)
BOUNDARY_ARTIFACT_RELATIVE_PATH = (
    resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
OUTPUT_RELATIVE_ROOT = resolver.OUTPUT_ROOT.relative_to(REPOSITORY_ROOT)

FIXTURE_FILE_RELATIVE_PATHS = (
    PREPARATION_SPEC_RELATIVE_PATH,
    PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
    BOUNDARY_ARTIFACT_RELATIVE_PATH,
    Path(resolver.BOUNDED_SOURCE_REFERENCES["preserved_archive_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["archive_hash_record_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["attestation_statement_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["attestation_timestamp_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["capture_method_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["capture_only_statement_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["freely_given_statement_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["knock_reference_path"]),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["receiver_label_path"]),
    Path(
        resolver.BOUNDED_SOURCE_REFERENCES[
            "receiver_working_directory_path"
        ]
    ),
    Path(resolver.BOUNDED_SOURCE_REFERENCES["recorded_signal_path"]),
)

PRESERVED_RELATIVE_PATHS = (
    PREPARATION_SPEC_RELATIVE_PATH,
    Path(
        "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
        "operation_basis_declaration_preparation_v0_min.py"
    ),
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "BASIS_DECLARATION_PREPARATION_REQUEST_V0_MIN_SPEC.md"
    ),
    Path(
        "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
        "operation_basis_declaration_preparation_request_v0_min.py"
    ),
    Path(
        "tests/test_resolve_receiver_side_answerable_basis_receiver_"
        "attestation_operation_basis_declaration_preparation_request_"
        "v0_min.py"
    ),
    PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "V0_MIN_SPEC.md"
    ),
    Path(
        "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
        "operation_v0_min.py"
    ),
    Path(
        "tests/test_resolve_receiver_side_answerable_basis_receiver_"
        "attestation_operation_v0_min.py"
    ),
    BOUNDARY_ARTIFACT_RELATIVE_PATH,
    *FIXTURE_FILE_RELATIVE_PATHS[3:],
)

PREPARATION_REQUEST_STATE_KEY = resolver.PREPARATION_REQUEST_PREFIX
PREPARATION_REQUEST_DECLARED_KEY = (
    f"declared_{resolver.PREPARATION_REQUEST_PREFIX}"
)
PREPARATION_REQUEST_SUMMARY_KEY = (
    f"{resolver.PREPARATION_REQUEST_PREFIX}_summary"
)
BOUNDARY_STATE_KEY = resolver.BOUNDARY_PREFIX
BOUNDARY_SUMMARY_KEY = f"{resolver.BOUNDARY_PREFIX}_summary"

DOWNSTREAM_FALSE_FIELDS = (
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
    "receiver_answerable_receipt_present",
    "presence_established",
    "identity_created",
    "authority_created",
    "truth_created",
    "standing_created",
    "follow_on_authorized",
)

_MISSING = object()


class ReceiverAttestationOperationBasisDeclarationPreparationTests(
    unittest.TestCase
):
    """Exercise exact preparation, evidence, separation, and writer locks."""

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
                "receiver-attestation preparation lineage changed during tests"
            )

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        for relative in FIXTURE_FILE_RELATIVE_PATHS:
            self._copy_fixture(relative)

        self.path_patchers = (
            patch.object(resolver, "REPO_ROOT", self.root),
            patch.object(
                resolver,
                "GOVERNING_SPECIFICATION_PATH",
                self.root / PREPARATION_SPEC_RELATIVE_PATH,
            ),
            patch.object(
                resolver,
                "SELECTED_PREPARATION_REQUEST_ARTIFACT_PATH",
                self.root / PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
            ),
            patch.object(
                resolver,
                "SELECTED_BOUNDARY_ARTIFACT_PATH",
                self.root / BOUNDARY_ARTIFACT_RELATIVE_PATH,
            ),
            patch.object(
                resolver,
                "BOUNDED_CAPTURE_DIRECTORY_PATH",
                self.root / resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH,
            ),
            patch.object(
                resolver,
                "OUTPUT_ROOT",
                self.root / OUTPUT_RELATIVE_ROOT,
            ),
        )
        for path_patcher in self.path_patchers:
            path_patcher.start()
            self.addCleanup(path_patcher.stop)

        self.fixture_hashes = {
            relative: self._sha256(self.root / relative)
            for relative in FIXTURE_FILE_RELATIVE_PATHS
        }

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def _copy_fixture(self, relative: Path) -> Path:
        source = REPOSITORY_ROOT / relative
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return target

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

    @contextmanager
    def _unreadable(self, path: Path) -> Iterator[None]:
        original_mode = stat.S_IMODE(path.stat().st_mode)
        path.chmod(0)
        try:
            yield
        finally:
            path.chmod(original_mode)

    def specification_path(self) -> Path:
        return self.root / PREPARATION_SPEC_RELATIVE_PATH

    def preparation_request_artifact_path(self) -> Path:
        return self.root / PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH

    def boundary_artifact_path(self) -> Path:
        return self.root / BOUNDARY_ARTIFACT_RELATIVE_PATH

    def bounded_path(self, field: str) -> Path:
        value = resolver.BOUNDED_SOURCE_REFERENCES[field]
        return self.root / value

    def canonical_request(
        self,
        *,
        selected: bool = True,
        **overrides: Any,
    ) -> dict[str, Any]:
        return resolver.build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request(
            basis_declaration_preparation_selected=selected,
            **copy.deepcopy(overrides),
        )

    def invoke(self, request: Any = None) -> dict[str, Any]:
        return resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min(
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

    def block_code(self, result: Mapping[str, Any]) -> Any:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        return block.get("code") or block.get("block_code")

    def assert_all_emitted_codes_public(
        self,
        result: Mapping[str, Any],
    ) -> None:
        checks = result.get(CHECKS_KEY)
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, Mapping)
            self.assertIs(type(check.get("passed")), bool)
            for field in ("failure_code", "block_code"):
                code = check.get(field)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_false_non_claims(
        self,
        result: Mapping[str, Any],
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(
            tuple(non_claims),
            resolver.REQUIRED_FALSE_NON_CLAIMS,
        )
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
        self.assertEqual(tuple(omission), resolver.RESULT_OMISSION_FIELDS)
        state = self.state(result)
        for field in resolver.RESULT_OMISSION_FIELDS:
            self.assertIs(omission[field], True)
            self.assertIs(state[field], True)

        forbidden = resolver.FORBIDDEN_PAYLOAD_KEYS

        def walk(value: Any) -> None:
            if isinstance(value, Mapping):
                self.assertTrue(set(value).isdisjoint(forbidden))
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

    def assert_downstream_false(
        self,
        result: Mapping[str, Any],
    ) -> None:
        state = self.state(result)
        for field in DOWNSTREAM_FALSE_FIELDS:
            self.assertIn(field, state)
            self.assertIs(type(state[field]), bool)
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
        self.assert_all_emitted_codes_public(result)

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            self.state(result).get("preparation_result"),
            resolver.PREPARATION_RESULT_NOT_EVALUATED,
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
        state = self.state(result)
        for field in (
            "preparation_recorded",
            "preparation_result_recorded",
            "preparation_exhausted",
            "basis_declaration_preparation_started",
            "basis_declaration_preparation_completed",
            "receiver_attestation_operation_basis_declaration_"
            "candidate_prepared",
            "receiver_attestation_operation_basis_prepared",
        ):
            self.assertIs(state.get(field), False)
        self.assertIsNone(result.get("prepared_declaration_candidate"))
        self.assert_downstream_false(result)
        self.assert_all_emitted_codes_public(result)

    def assert_not_prepared(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_PREPARED)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("preparation_result"),
            resolver.PREPARATION_RESULT_NOT_PREPARED,
        )
        for field in (
            "preparation_recorded",
            "preparation_result_recorded",
            "preparation_exhausted",
            "basis_declaration_preparation_started",
            "basis_declaration_preparation_completed",
        ):
            self.assertIs(state.get(field), True)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_declaration_"
                "candidate_prepared"
            ),
            False,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_prepared"),
            False,
        )
        decision = result.get("preparation_decision")
        self.assertIsInstance(decision, Mapping)
        self.assertIn(decision.get("code"), resolver.NOT_PREPARED_CODES)
        self.assertIsInstance(decision.get("reason"), str)
        self.assertTrue(decision.get("reason"))
        if expected_code is not None:
            self.assertEqual(decision.get("code"), expected_code)
        self.assertIsNone(result.get("prepared_declaration_candidate"))
        self.assert_downstream_false(result)

    def assert_candidate_exact(
        self,
        result: Mapping[str, Any],
    ) -> dict[str, Any]:
        candidate = result.get("prepared_declaration_candidate")
        self.assertIsInstance(candidate, dict)
        self.assertEqual(tuple(candidate), resolver.CANDIDATE_FIELDS)
        self.assertEqual(len(candidate), 21)
        for field, expected in resolver.BOUNDED_SOURCE_REFERENCES.items():
            self.assertEqual(candidate[field], expected)

        evaluator = candidate["evaluator_reference"]
        self.assertIsInstance(evaluator, str)
        self.assertEqual(
            evaluator.split(":"),
            [
                resolver.RESOLVER_MODULE,
                resolver.PREPARATION_ID,
                resolver.PREPARATION_RESULT_PREPARED,
            ],
        )
        posture_families = {
            "trace_integrity_postures": (
                resolver.TRACE_INTEGRITY_POSTURE_KEYS
            ),
            "ambiguity_postures": resolver.AMBIGUITY_POSTURE_KEYS,
            "contradiction_postures": resolver.CONTRADICTION_POSTURE_KEYS,
            "unresolved_postures": resolver.UNRESOLVED_POSTURE_KEYS,
        }
        for family, fields in posture_families.items():
            posture = candidate[family]
            self.assertIsInstance(posture, dict)
            self.assertEqual(tuple(posture), fields)
            for field in fields:
                self.assertIs(type(posture[field]), bool)

        trace = candidate["trace_integrity_postures"]
        self.assertTrue(all(trace[field] is True for field in trace))
        for family in (
            "ambiguity_postures",
            "contradiction_postures",
            "unresolved_postures",
        ):
            self.assertTrue(
                all(value is False for value in candidate[family].values())
            )
        self.assertEqual(
            candidate["non_conversion_statement"],
            resolver.NON_CONVERSION_STATEMENT,
        )
        basis_non_claims = candidate["basis_non_claims"]
        self.assertEqual(
            tuple(basis_non_claims),
            resolver.REQUIRED_BASIS_NON_CLAIMS,
        )
        self.assertNotIn("receiver_attestation_recorded", basis_non_claims)
        self.assertTrue(
            all(value is False for value in basis_non_claims.values())
        )
        return candidate

    def assert_prepared(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_PREPARED)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("preparation_result"),
            resolver.PREPARATION_RESULT_PREPARED,
        )
        for field in (
            "preparation_recorded",
            "preparation_result_recorded",
            "preparation_exhausted",
            "basis_declaration_preparation_started",
            "basis_declaration_preparation_completed",
            "receiver_attestation_operation_basis_declaration_"
            "candidate_prepared",
            "receiver_attestation_operation_basis_prepared",
        ):
            self.assertIs(state.get(field), True)
        self.assert_candidate_exact(result)
        self.assert_downstream_false(result)

    def preparation_request_artifact(self) -> dict[str, Any]:
        return self._load_json(self.preparation_request_artifact_path())

    def write_preparation_request_artifact(
        self,
        value: Any,
    ) -> Path:
        return self._write_json(
            self.preparation_request_artifact_path(),
            value,
        )

    def boundary_artifact(self) -> dict[str, Any]:
        return self._load_json(self.boundary_artifact_path())

    def write_boundary_artifact(self, value: Any) -> Path:
        return self._write_json(self.boundary_artifact_path(), value)

    def assert_fixture_files_unchanged(self) -> None:
        current = {
            relative: self._sha256(self.root / relative)
            for relative in FIXTURE_FILE_RELATIVE_PATHS
        }
        self.assertEqual(current, self.fixture_hashes)

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
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError
        ):
            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
                result,
                output,
            )
        self.assertFalse(output.exists())

    def test_01_public_api_and_constant_contract(self) -> None:
        public_callables = (
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_v0_min_request",
            "build_declared_receiver_side_answerable_basis_receiver_"
            "attestation_operation_basis_declaration_preparation_"
            "v0_min_request",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_v0_min_from_path",
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_v0_min_summary",
            "write_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_v0_min_result",
        )
        for name in public_callables:
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(
            issubclass(
                resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError,
                Exception,
            )
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(len(resolver.CANDIDATE_FIELDS), 21)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_PREPARED,
                resolver.OUTCOME_NOT_PREPARED,
                resolver.OUTCOME_BLOCKED,
            },
        )

    def test_02_canonical_builders_are_exact_and_independent(self) -> None:
        first = resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_request()
        second = self.canonical_request()
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["bounded_source_references"],
            second["bounded_source_references"],
        )
        self.assertIsNot(
            first["declared_non_claims"],
            second["declared_non_claims"],
        )
        self.assertIs(
            first[resolver.REQUEST_SELECTION_FIELD],
            True,
        )
        self.assertEqual(
            first["bounded_source_references"],
            dict(resolver.BOUNDED_SOURCE_REFERENCES),
        )
        self.assertTrue(
            all(
                value is False
                for value in first["declared_non_claims"].values()
            )
        )
        override = self.canonical_request(unknown_override="visible")
        self.assertEqual(override["unknown_override"], "visible")

    def test_03_canonical_prepared_branch(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_prepared(result)
        candidate = self.assert_candidate_exact(result)
        archive = result["archive_correspondence_metadata"]
        self.assertEqual(
            archive["computed_sha256"],
            resolver.EXPECTED_ARCHIVE_SHA256,
        )
        self.assertEqual(
            archive["hash_record_sha256"],
            resolver.EXPECTED_ARCHIVE_SHA256,
        )
        self.assertIs(archive["correspondence_validated"], True)
        self.assertIs(
            candidate["trace_integrity_postures"][
                "archive_correspondence_claimed"
            ],
            True,
        )

    def test_04_lawful_selection_false_not_prepared_branch(self) -> None:
        result = self.invoke(self.canonical_request(selected=False))
        self.assert_not_prepared(result, "PREPARATION_NOT_SELECTED")
        state = self.state(result)
        self.assertIs(
            state[resolver.REQUEST_SELECTION_FIELD],
            False,
        )
        non_meaning = result[f"{PREFIX}_non_meaning"]
        self.assertIs(
            non_meaning["not_prepared_is_not_operation_not_recorded"],
            True,
        )
        self.assertIs(
            non_meaning["not_prepared_is_not_operation_indeterminate"],
            True,
        )
        serialized = json.dumps(result, sort_keys=True)
        for prohibited_meaning in (
            "receiver_refusal",
            "fabricated_trace",
            "candidate_insufficiency",
        ):
            self.assertNotIn(prohibited_meaning, serialized)

    def test_05_request_mapping_shape_intent_and_unknown_fields(self) -> None:
        canonical = self.canonical_request()
        missing = copy.deepcopy(canonical)
        missing.pop("preparation_id")
        unknown = copy.deepcopy(canonical)
        unknown["unknown_top_level_field"] = True
        unsupported = copy.deepcopy(canonical)
        unsupported["intent"] = "UNSUPPORTED"
        explicit_block = copy.deepcopy(canonical)
        explicit_block["intent"] = resolver.INTENT_BLOCK
        cases = (
            ("none_defaults", None, None),
            ("non_mapping_list", [], "REQUEST_NOT_MAPPING"),
            ("non_mapping_string", "request", "REQUEST_NOT_MAPPING"),
            ("missing", missing, "REQUEST_FIELD_MISSING"),
            ("unknown", unknown, "REQUEST_FIELD_UNKNOWN"),
            ("unsupported", unsupported, "UNSUPPORTED_INTENT"),
            (
                "explicit_block",
                explicit_block,
                "EXPLICIT_BLOCK_REQUESTED",
            ),
        )
        for name, request, code in cases:
            with self.subTest(case=name):
                result = self.invoke(request)
                if code is None:
                    self.assert_prepared(result)
                else:
                    self.assert_blocked(result, code)

    def test_06_request_identity_and_exact_path_matrix(self) -> None:
        expectations = {
            "preparation_id": "PREPARATION_IDENTITY_MISMATCH",
            "preparation_type": "PREPARATION_IDENTITY_MISMATCH",
            "preparation_version": "PREPARATION_IDENTITY_MISMATCH",
            "preparation_scope": "PREPARATION_IDENTITY_MISMATCH",
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
            "governing_preparation_specification_path": (
                "GOVERNING_SPECIFICATION_PATH_MISMATCH"
            ),
            "selected_preparation_request_artifact_path": (
                "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            ),
        }
        for field, code in expectations.items():
            with self.subTest(field=field):
                request = self.canonical_request()
                request[field] = f"wrong_{field}"
                self.assert_blocked(self.invoke(request), code)

    def test_07_request_selection_requires_exact_boolean(self) -> None:
        for value in (None, 0, 1, "false", "true", [], {}):
            with self.subTest(value=repr(value)):
                request = self.canonical_request()
                request[resolver.REQUEST_SELECTION_FIELD] = value
                self.assert_blocked(
                    self.invoke(request),
                    "PREPARATION_SELECTION_INVALID",
                )

    def test_08_each_bounded_reference_is_exact(self) -> None:
        for field in resolver.BOUNDED_SOURCE_REFERENCES:
            with self.subTest(reference=field):
                request = self.canonical_request()
                request["bounded_source_references"][field] = (
                    f"alternate/{field}"
                )
                self.assert_blocked(
                    self.invoke(request),
                    "BOUNDED_SOURCE_REFERENCE_MISMATCH",
                )

    def test_09_bounded_reference_shape_and_alternate_paths_block(self) -> None:
        canonical_references = dict(resolver.BOUNDED_SOURCE_REFERENCES)
        missing = copy.deepcopy(canonical_references)
        missing.pop(next(iter(missing)))
        additional = copy.deepcopy(canonical_references)
        additional["additional_reference"] = "artifact.json"
        traversal = copy.deepcopy(canonical_references)
        traversal["preserved_archive_path"] = (
            "../receiver_attestation_001.zip"
        )
        sibling = copy.deepcopy(canonical_references)
        sibling["preserved_archive_path"] = (
            str(Path(canonical_references["preserved_archive_path"]).with_name(
                "sibling.zip"
            ))
        )
        normalized = copy.deepcopy(canonical_references)
        normalized["preserved_archive_path"] = (
            str(
                Path(canonical_references["preserved_archive_path"]).parent
                / ".."
                / "original_zip"
                / "receiver_attestation_001.zip"
            )
        )
        cases = (
            ("missing", missing),
            ("additional", additional),
            ("non_mapping", []),
            ("null", None),
            ("traversal", traversal),
            ("sibling", sibling),
            ("normalized_alternate", normalized),
        )
        for name, references in cases:
            with self.subTest(case=name):
                request = self.canonical_request()
                request["bounded_source_references"] = references
                self.assert_blocked(
                    self.invoke(request),
                    "BOUNDED_SOURCE_REFERENCE_MISMATCH",
                )

        caller_fields = (
            "computed_archive_sha256",
            "parsed_attestation_timestamp",
            "prepared_declaration_candidate",
            "trace_integrity_postures",
            "ambiguity_postures",
            "contradiction_postures",
            "unresolved_postures",
        )
        for field in caller_fields:
            with self.subTest(caller_field=field):
                self.assert_blocked(
                    self.invoke(
                        self.canonical_request(**{field: "caller supplied"})
                    ),
                    "REQUEST_FIELD_UNKNOWN",
                )

    def test_10_every_exposed_prohibited_input_true_blocks(self) -> None:
        for field, expected_code in resolver.PROHIBITED_INPUT_FLAGS.items():
            with self.subTest(prohibited_input=field):
                request = self.canonical_request()
                request[field] = True
                self.assert_blocked(self.invoke(request), expected_code)

    def test_11_prohibited_inputs_require_exact_false(self) -> None:
        representative_fields = (
            "request_prepared_declaration_candidate",
            "request_caller_selected_posture_maps",
            "request_preparation_result",
            "request_operation_result",
            "request_source_body_embedding",
            "request_basis_declaration",
            "request_basis_supply",
            "request_basis_admission",
            "request_operation_execution",
            "request_receiver_attestation_recording",
            "request_receiver_answerable_receipt_creation",
            "request_presence_establishment",
            "request_identity_creation",
            "request_authority_creation",
            "request_truth_creation",
            "request_standing_creation",
            "request_relation_creation",
            "request_coupling_creation",
            "request_output_authorization",
            "request_action_authorization",
            "request_synchronization_authorization",
            "request_follow_on_authorization",
            "request_repeated_preparation_permission_creation",
            "request_reusable_preparation_route_creation",
            "request_same_preparation_rerun",
            "request_automatic_retry",
            "request_preparation_debt_creation",
            "request_preparation_obligation_creation",
            "request_scheduled_action",
            "request_repository_scan",
            "request_file_discovery",
            "request_affected_file_repair",
            "request_validation_enforcement",
            "request_prior_unsupported_claim_validation",
        )
        for field in representative_fields:
            self.assertIn(field, resolver.PROHIBITED_INPUT_FLAGS)
            for value in (None, 0, "false", []):
                with self.subTest(field=field, value=repr(value)):
                    request = self.canonical_request()
                    request[field] = value
                    self.assert_blocked(
                        self.invoke(request),
                        "REQUEST_VALUE_MISMATCH",
                    )

        additional_prohibited_routes = (
            "request_archive_bytes",
            "request_complete_text_component_body",
            "request_recorded_signal_body",
            "request_runtime_creation",
            "request_api_creation",
            "request_globbing",
            "request_sibling_discovery",
            "request_fallback_search",
            "request_contaminated_lineage_validation",
        )
        for field in additional_prohibited_routes:
            with self.subTest(additional_route=field):
                self.assert_blocked(
                    self.invoke(self.canonical_request(**{field: True})),
                    "REQUEST_FIELD_UNKNOWN",
                )

    def test_12_every_request_non_claim_true_blocks(self) -> None:
        for field in resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                request = self.canonical_request()
                request["declared_non_claims"][field] = True
                result = self.invoke(request)
                self.assert_blocked(
                    result,
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
                self.assertIs(self.state(result).get(field), False)

    def test_13_request_non_claim_shape_and_types_are_exact(self) -> None:
        canonical = self.canonical_request()["declared_non_claims"]
        first = next(iter(canonical))
        variants: list[tuple[str, Any]] = []
        for value in (None, 0, "false"):
            altered = copy.deepcopy(canonical)
            altered[first] = value
            variants.append((f"value_{value!r}", altered))
        missing = copy.deepcopy(canonical)
        missing.pop(first)
        variants.append(("missing", missing))
        additional = copy.deepcopy(canonical)
        additional["unknown_non_claim"] = False
        variants.append(("additional", additional))
        variants.extend((("null_mapping", None), ("list_mapping", [])))
        for name, non_claims in variants:
            with self.subTest(case=name):
                request = self.canonical_request()
                request["declared_non_claims"] = non_claims
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )

    def test_14_specification_exact_markers_pass(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_prepared(result)
        validation = result["specification_marker_validation"]
        self.assertIs(validation["specification_markers_validated"], True)
        self.assertTrue(all(validation["marker_status"].values()))
        self.assertIs(
            validation["complete_specification_body_omitted"],
            True,
        )

    def test_15_each_specification_marker_class_is_required(self) -> None:
        original = self.specification_path().read_text(encoding="utf-8")
        for marker_class, markers in (
            resolver.SPECIFICATION_MARKER_CLASSES.items()
        ):
            marker = markers[0]
            self.assertIn(marker, original)
            with self.subTest(marker_class=marker_class):
                altered = original.replace(
                    marker,
                    f"REMOVED_{marker_class}",
                )
                self._write_text(self.specification_path(), altered)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SPECIFICATION_MARKER_MISSING",
                )
                self._write_text(self.specification_path(), original)

    def test_16_each_candidate_and_posture_spec_marker_is_required(self) -> None:
        original = self.specification_path().read_text(encoding="utf-8")
        marker_fields = (
            *resolver.CANDIDATE_FIELDS,
            *resolver.TRACE_INTEGRITY_POSTURE_KEYS,
            *resolver.AMBIGUITY_POSTURE_KEYS,
            *resolver.CONTRADICTION_POSTURE_KEYS,
            *resolver.UNRESOLVED_POSTURE_KEYS,
        )
        for index, marker in enumerate(marker_fields):
            self.assertIn(marker, original)
            with self.subTest(index=index, marker=marker):
                altered = original.replace(
                    marker,
                    f"removed_marker_{index}",
                )
                self._write_text(self.specification_path(), altered)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SPECIFICATION_MARKER_MISSING",
                )
                self._write_text(self.specification_path(), original)

    def test_17_each_basis_non_claim_spec_marker_is_required(self) -> None:
        original = self.specification_path().read_text(encoding="utf-8")
        for index, marker in enumerate(resolver.REQUIRED_BASIS_NON_CLAIMS):
            self.assertIn(marker, original)
            with self.subTest(index=index, marker=marker):
                altered = original.replace(
                    marker,
                    f"removed_basis_non_claim_{index}",
                )
                self._write_text(self.specification_path(), altered)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SPECIFICATION_MARKER_MISSING",
                )
                self._write_text(self.specification_path(), original)

    def test_18_specification_missing_non_file_and_malformed_block(self) -> None:
        path = self.specification_path()
        original = path.read_text(encoding="utf-8")
        path.unlink()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SPECIFICATION_NOT_AVAILABLE",
        )
        path.mkdir()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SPECIFICATION_NOT_AVAILABLE",
        )
        path.rmdir()
        self._write_text(path, "not the governing specification\n")
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SPECIFICATION_MARKER_MISSING",
        )
        self._write_text(path, original)
        self.assert_prepared(self.invoke(self.canonical_request()))

    def test_19_preparation_request_metadata_and_identity_matrix(self) -> None:
        original = self.preparation_request_artifact()
        metadata_cases = (
            ("resolver_module", "wrong", "PREPARATION_REQUEST_ARTIFACT_METADATA_MISMATCH"),
            ("result_version", "9.9.9", "PREPARATION_REQUEST_ARTIFACT_METADATA_MISMATCH"),
            ("failed_check_count", 1, "PREPARATION_REQUEST_ARTIFACT_FAILED_CHECKS_PRESENT"),
            ("outcome", "NOT_RECORDED", "PREPARATION_REQUEST_ARTIFACT_METADATA_MISMATCH"),
        )
        for field, value, code in metadata_cases:
            with self.subTest(metadata=field):
                artifact = copy.deepcopy(original)
                artifact[field] = value
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(self.invoke(self.canonical_request()), code)
                self.write_preparation_request_artifact(original)

        identity_fields = (
            "preparation_request_id",
            "preparation_request_type",
            "preparation_request_version",
            "preparation_request_scope",
            "selected_receiver_attestation_operation_id",
            "receiver_side_answerable_basis_candidate_id",
        )
        for field in identity_fields:
            for section in (
                PREPARATION_REQUEST_STATE_KEY,
                PREPARATION_REQUEST_DECLARED_KEY,
            ):
                with self.subTest(identity=field, section=section):
                    artifact = copy.deepcopy(original)
                    artifact[section][field] = f"wrong_{field}"
                    self.write_preparation_request_artifact(artifact)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "PREPARATION_REQUEST_ARTIFACT_IDENTITY_MISMATCH",
                    )
                    self.write_preparation_request_artifact(original)

    def test_20_preparation_request_recorded_and_block_posture_matrix(
        self,
    ) -> None:
        original = self.preparation_request_artifact()
        cases = (
            (
                PREPARATION_REQUEST_STATE_KEY,
                "request_result",
                "NOT_RECORDED",
                "PREPARATION_REQUEST_ARTIFACT_NOT_RECORDED",
            ),
            (
                PREPARATION_REQUEST_SUMMARY_KEY,
                "request_result",
                "NOT_RECORDED",
                "PREPARATION_REQUEST_ARTIFACT_NOT_RECORDED",
            ),
            (
                PREPARATION_REQUEST_SUMMARY_KEY,
                "request_selection",
                False,
                "PREPARATION_REQUEST_ARTIFACT_NOT_RECORDED",
            ),
            (
                "block",
                "blocked",
                True,
                "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
            ),
            (
                "block",
                "code",
                "EXPLICIT_BLOCK_REQUESTED",
                "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
            ),
            (
                "block",
                "block_code",
                "EXPLICIT_BLOCK_REQUESTED",
                "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
            ),
            (
                "block",
                "reason",
                "blocked",
                "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
            ),
            (
                PREPARATION_REQUEST_SUMMARY_KEY,
                "blocked",
                True,
                "PREPARATION_REQUEST_ARTIFACT_BLOCKED",
            ),
        )
        for section, field, value, code in cases:
            with self.subTest(section=section, field=field):
                artifact = copy.deepcopy(original)
                artifact[section][field] = value
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(self.invoke(self.canonical_request()), code)
                self.write_preparation_request_artifact(original)

    def test_21_preparation_request_required_true_postures_are_exact(
        self,
    ) -> None:
        original = self.preparation_request_artifact()
        true_fields = (
            "preparation_request_recorded",
            "preparation_request_result_recorded",
            "preparation_request_exhausted",
            "basis_declaration_preparation_requested",
        )
        wrong_values = (False, None, 1, "true", _MISSING)
        for field in true_fields:
            for value in wrong_values:
                with self.subTest(field=field, value=repr(value)):
                    artifact = copy.deepcopy(original)
                    state = artifact[PREPARATION_REQUEST_STATE_KEY]
                    if value is _MISSING:
                        state.pop(field)
                    else:
                        state[field] = value
                    self.write_preparation_request_artifact(artifact)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "PREPARATION_REQUEST_ARTIFACT_POSTURE_INVALID",
                    )
                    self.write_preparation_request_artifact(original)

    def test_22_preparation_request_required_false_postures_are_exact(
        self,
    ) -> None:
        original = self.preparation_request_artifact()
        false_fields = (
            "basis_declaration_preparation_started",
            "basis_declaration_preparation_completed",
            "receiver_attestation_operation_basis_prepared",
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
        for field in false_fields:
            with self.subTest(field=field, value=True):
                artifact = copy.deepcopy(original)
                artifact[PREPARATION_REQUEST_STATE_KEY][field] = True
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "PREPARATION_REQUEST_ARTIFACT_POSTURE_INVALID",
                )
                self.write_preparation_request_artifact(original)

        representative = (
            "basis_declaration_preparation_started",
            "receiver_attestation_operation_basis_prepared",
            "receiver_attestation_recorded",
        )
        for field in representative:
            for value in (None, 0, "false", _MISSING):
                with self.subTest(field=field, value=repr(value)):
                    artifact = copy.deepcopy(original)
                    state = artifact[PREPARATION_REQUEST_STATE_KEY]
                    if value is _MISSING:
                        state.pop(field)
                        artifact["noncanonical_posture"] = {field: False}
                    else:
                        state[field] = value
                    self.write_preparation_request_artifact(artifact)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "PREPARATION_REQUEST_ARTIFACT_POSTURE_INVALID",
                    )
                    self.write_preparation_request_artifact(original)

    def test_23_preparation_request_summary_locks_and_omission_are_exact(
        self,
    ) -> None:
        original = self.preparation_request_artifact()
        cases = (
            (
                "result_level_non_claims_canonical_false",
                False,
                "PREPARATION_REQUEST_ARTIFACT_NON_CLAIM_NOT_FALSE",
            ),
            (
                "result_level_non_claims_canonical_false",
                1,
                "PREPARATION_REQUEST_ARTIFACT_NON_CLAIM_NOT_FALSE",
            ),
            (
                "complete_material_omitted",
                False,
                "PREPARATION_REQUEST_ARTIFACT_OMISSION_INVALID",
            ),
            (
                "complete_material_omitted",
                1,
                "PREPARATION_REQUEST_ARTIFACT_OMISSION_INVALID",
            ),
        )
        for field, value, code in cases:
            with self.subTest(field=field, value=repr(value)):
                artifact = copy.deepcopy(original)
                artifact[PREPARATION_REQUEST_SUMMARY_KEY][field] = value
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(self.invoke(self.canonical_request()), code)
                self.write_preparation_request_artifact(original)

        omission_fields = (
            "complete_waiting_artifact_omitted",
            "complete_upstream_boundary_artifact_omitted",
            "complete_candidate_sufficiency_artifact_omitted",
            "complete_candidate_sufficiency_basis_omitted",
            "complete_operation_basis_omitted",
            "archive_bytes_omitted",
            "text_component_bodies_omitted",
            "recorded_signal_body_omitted",
        )
        for field in omission_fields:
            with self.subTest(omission=field):
                artifact = copy.deepcopy(original)
                artifact[PREPARATION_REQUEST_STATE_KEY][field] = False
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "PREPARATION_REQUEST_ARTIFACT_OMISSION_INVALID",
                )
                self.write_preparation_request_artifact(original)

    def test_24_each_preparation_request_non_claim_flip_blocks(self) -> None:
        original = self.preparation_request_artifact()
        self.assertEqual(
            set(original["non_claims"]),
            set(resolver.UPSTREAM_REQUEST_FALSE_NON_CLAIMS),
        )
        for field in resolver.UPSTREAM_REQUEST_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                artifact = copy.deepcopy(original)
                artifact["non_claims"][field] = True
                self.write_preparation_request_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "PREPARATION_REQUEST_ARTIFACT_NON_CLAIM_NOT_FALSE",
                )
                self.write_preparation_request_artifact(original)

        sensitive = (
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        )
        for field in sensitive:
            self.assertIn(field, resolver.UPSTREAM_REQUEST_FALSE_NON_CLAIMS)

    def test_25_preparation_request_artifact_file_and_json_failures(
        self,
    ) -> None:
        path = self.preparation_request_artifact_path()
        original_text = path.read_text(encoding="utf-8")
        cases = (
            (
                "malformed",
                "{",
                "PREPARATION_REQUEST_ARTIFACT_NOT_PARSEABLE",
            ),
            (
                "duplicate",
                '{"resolver_module":"a","resolver_module":"b"}',
                "PREPARATION_REQUEST_ARTIFACT_NOT_PARSEABLE",
            ),
            (
                "non_mapping",
                "[]",
                "PREPARATION_REQUEST_ARTIFACT_NOT_MAPPING",
            ),
        )
        for name, text, code in cases:
            with self.subTest(case=name):
                self._write_text(path, text)
                self.assert_blocked(self.invoke(self.canonical_request()), code)
                self._write_text(path, original_text)

        path.unlink()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "PREPARATION_REQUEST_ARTIFACT_NOT_AVAILABLE",
        )
        path.mkdir()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "PREPARATION_REQUEST_ARTIFACT_NOT_AVAILABLE",
        )
        path.rmdir()
        self._write_text(path, original_text)

    def test_26_selected_boundary_metadata_identity_and_outcome_matrix(
        self,
    ) -> None:
        original = self.boundary_artifact()
        metadata_cases = (
            ("resolver_module", "wrong"),
            ("result_version", "9.9.9"),
            ("failed_check_count", 1),
            ("outcome", "BLOCKED"),
        )
        for field, value in metadata_cases:
            with self.subTest(metadata=field):
                artifact = copy.deepcopy(original)
                artifact[field] = value
                self.write_boundary_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                )
                self.write_boundary_artifact(original)

        identity_fields = (
            "boundary_id",
            "boundary_type",
            "boundary_version",
            "boundary_scope",
            "receiver_side_answerable_basis_candidate_id",
            "selected_candidate_sufficiency_operation_id",
            "selected_candidate_sufficiency_operation_result_required",
        )
        for field in identity_fields:
            with self.subTest(identity=field):
                artifact = copy.deepcopy(original)
                artifact[BOUNDARY_STATE_KEY][field] = f"wrong_{field}"
                self.write_boundary_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
                )
                self.write_boundary_artifact(original)

    def test_27_selected_boundary_standing_posture_matrix(self) -> None:
        original = self.boundary_artifact()
        state_expectations = {
            "receiver_attestation_boundary_result": (
                resolver.SELECTED_BOUNDARY_RESULT
            ),
            "receiver_attestation_boundary_recorded": True,
            "receiver_attestation_boundary_result_recorded": True,
            "receiver_attestation_consideration_allowed": True,
            "receiver_attestation_consideration_not_allowed": False,
            "receiver_attestation_boundary_exhausted": True,
            "bounded_material_selected_for_consideration": True,
        }
        for field, expected in state_expectations.items():
            with self.subTest(state_posture=field):
                artifact = copy.deepcopy(original)
                artifact[BOUNDARY_STATE_KEY][field] = (
                    not expected if type(expected) is bool else "wrong"
                )
                self.write_boundary_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SELECTED_BOUNDARY_POSTURE_INVALID",
                )
                self.write_boundary_artifact(original)

        summary_true_fields = (
            "specification_markers_validated",
            "selected_operation_validated",
            "eight_dimensions_validated",
            "upstream_false_locks_validated",
            "result_level_non_claims_canonical_false",
            "complete_operation_artifact_omitted",
            "complete_sufficiency_basis_omitted",
            "complete_capture_signal_data_omitted",
        )
        for field in summary_true_fields:
            for value in (False, None, 1, "true", _MISSING):
                with self.subTest(summary_posture=field, value=repr(value)):
                    artifact = copy.deepcopy(original)
                    summary = artifact[BOUNDARY_SUMMARY_KEY]
                    if value is _MISSING:
                        summary.pop(field)
                    else:
                        summary[field] = value
                    self.write_boundary_artifact(artifact)
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "SELECTED_BOUNDARY_POSTURE_INVALID",
                    )
                    self.write_boundary_artifact(original)

        blocked_artifact = copy.deepcopy(original)
        blocked_artifact["outcome"] = "BLOCKED"
        blocked_artifact["block"] = {
            "blocked": True,
            "code": "EXPLICIT_BLOCK_REQUESTED",
            "block_code": "EXPLICIT_BLOCK_REQUESTED",
            "reason": "blocked",
        }
        self.write_boundary_artifact(blocked_artifact)
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SELECTED_BOUNDARY_METADATA_MISMATCH",
        )
        self.write_boundary_artifact(original)

    def test_28_each_selected_boundary_false_lock_flip_blocks(self) -> None:
        original = self.boundary_artifact()
        self.assertEqual(
            set(original["non_claims"]),
            set(resolver.REQUIRED_UPSTREAM_FALSE_POSTURES),
        )
        for field in resolver.REQUIRED_UPSTREAM_FALSE_POSTURES:
            with self.subTest(false_lock=field):
                artifact = copy.deepcopy(original)
                artifact["non_claims"][field] = True
                self.write_boundary_artifact(artifact)
                self.assert_blocked(
                    self.invoke(self.canonical_request()),
                    "SELECTED_BOUNDARY_NON_CLAIM_NOT_FALSE",
                )
                self.write_boundary_artifact(original)

        sensitive = (
            "receiver_attestation_recorded",
            "receiver_answerable_receipt_present",
            "presence_established",
            "identity_created",
            "authority_created",
            "truth_created",
            "standing_created",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        )
        for field in sensitive:
            self.assertIn(field, resolver.REQUIRED_UPSTREAM_FALSE_POSTURES)

    def test_29_selected_boundary_artifact_file_and_json_failures(
        self,
    ) -> None:
        path = self.boundary_artifact_path()
        original_text = path.read_text(encoding="utf-8")
        cases = (
            ("malformed", "{", "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE"),
            (
                "duplicate",
                '{"resolver_module":"a","resolver_module":"b"}',
                "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            ),
            ("non_mapping", "[]", "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING"),
        )
        for name, text, code in cases:
            with self.subTest(case=name):
                self._write_text(path, text)
                self.assert_blocked(self.invoke(self.canonical_request()), code)
                self._write_text(path, original_text)

        path.unlink()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SELECTED_BOUNDARY_ARTIFACT_NOT_AVAILABLE",
        )
        path.mkdir()
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "SELECTED_BOUNDARY_ARTIFACT_NOT_AVAILABLE",
        )
        path.rmdir()
        self._write_text(path, original_text)

    def test_30_archive_and_hash_record_availability_not_prepared(
        self,
    ) -> None:
        archive = self.bounded_path("preserved_archive_path")
        hash_record = self.bounded_path("archive_hash_record_path")
        archive.unlink()
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "BOUNDED_COMPONENT_ABSENT",
        )
        self._copy_fixture(
            Path(resolver.BOUNDED_SOURCE_REFERENCES["preserved_archive_path"])
        )

        hash_record.unlink()
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "BOUNDED_COMPONENT_ABSENT",
        )
        self._copy_fixture(
            Path(
                resolver.BOUNDED_SOURCE_REFERENCES[
                    "archive_hash_record_path"
                ]
            )
        )

        with self._unreadable(archive):
            result = self.invoke(self.canonical_request())
        if result.get("outcome") == resolver.OUTCOME_PREPARED:
            self.skipTest("filesystem does not enforce unreadable file mode")
        self.assert_not_prepared(result, "BOUNDED_COMPONENT_UNREADABLE")

    def test_31_archive_hash_grammar_and_correspondence_not_prepared(
        self,
    ) -> None:
        hash_record = self.bounded_path("archive_hash_record_path")
        original_hash_record = hash_record.read_text(encoding="utf-8")
        self._write_text(hash_record, "not a bounded sha256 record\n")
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "ARCHIVE_HASH_RECORD_MALFORMED",
        )

        self._write_text(
            hash_record,
            ("0" * 64) + "  receiver_attestation_001.zip\n",
        )
        mismatch = self.invoke(self.canonical_request())
        self.assert_not_prepared(mismatch, "ARCHIVE_HASH_MISMATCH")
        posture = mismatch["bounded_path_and_file_evaluation"]
        self.assertIs(
            posture["contradiction_postures"][
                "archive_correspondence_contradicted"
            ],
            True,
        )

        self._write_text(hash_record, original_hash_record)
        archive = self.bounded_path("preserved_archive_path")
        archive.write_bytes(archive.read_bytes() + b"changed")
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "ARCHIVE_HASH_MISMATCH",
        )

    def test_32_patched_expected_hash_mismatch_is_not_prepared(self) -> None:
        with patch.object(resolver, "EXPECTED_ARCHIVE_SHA256", "0" * 64):
            result = self.invoke(self.canonical_request())
        self.assert_not_prepared(result, "ARCHIVE_HASH_MISMATCH")
        archive = result["archive_correspondence_metadata"]
        self.assertNotEqual(
            archive["computed_sha256"],
            archive["expected_sha256"],
        )
        self.assertIs(archive["correspondence_validated"], False)
        self.assertIs(archive["correspondence_contradicted"], True)

    def test_33_each_text_component_absent_or_empty_is_not_prepared(
        self,
    ) -> None:
        for field in resolver.TEXT_COMPONENT_FIELDS:
            relative = Path(resolver.BOUNDED_SOURCE_REFERENCES[field])
            path = self.root / relative
            original = path.read_bytes()
            with self.subTest(field=field, condition="absent"):
                path.unlink()
                self.assert_not_prepared(
                    self.invoke(self.canonical_request()),
                    "BOUNDED_COMPONENT_ABSENT",
                )
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(original)
            with self.subTest(field=field, condition="empty"):
                self._write_text(path, " \n")
                self.assert_not_prepared(
                    self.invoke(self.canonical_request()),
                    "TEXT_COMPONENT_INVALID",
                )
                path.write_bytes(original)

    def test_34_unreadable_text_and_invalid_timestamp_are_not_prepared(
        self,
    ) -> None:
        text_path = self.bounded_path("attestation_statement_path")
        with self._unreadable(text_path):
            unreadable = self.invoke(self.canonical_request())
        if unreadable.get("outcome") == resolver.OUTCOME_PREPARED:
            self.skipTest("filesystem does not enforce unreadable file mode")
        self.assert_not_prepared(
            unreadable,
            "BOUNDED_COMPONENT_UNREADABLE",
        )

        timestamp = self.bounded_path("attestation_timestamp_path")
        for value in (
            "not-a-timestamp\n",
            "attested_at=2026-07-27T21:50:52+02:00\n",
            "attested_at=2026-99-99T99:99:99Z\n",
        ):
            with self.subTest(timestamp=value.strip()):
                self._write_text(timestamp, value)
                result = self.invoke(self.canonical_request())
                self.assert_not_prepared(result, "TIMESTAMP_INVALID")
                posture = result["bounded_path_and_file_evaluation"]
                self.assertIs(
                    posture["ambiguity_postures"][
                        "timestamp_interpretation_ambiguous"
                    ],
                    True,
                )
                self.assertIs(
                    posture["ambiguity_postures"][
                        "material_trace_ambiguity_present"
                    ],
                    True,
                )

    def test_35_recorded_signal_file_and_json_failures_not_prepared(
        self,
    ) -> None:
        signal = self.bounded_path("recorded_signal_path")
        original = signal.read_text(encoding="utf-8")
        signal.unlink()
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "BOUNDED_COMPONENT_ABSENT",
        )
        self._write_text(signal, original)

        cases = (
            ("malformed", "{"),
            (
                "duplicate",
                '{"recorded_at":"a","recorded_at":"b"}',
            ),
            ("non_mapping", "[]"),
        )
        for name, text in cases:
            with self.subTest(case=name):
                self._write_text(signal, text)
                self.assert_not_prepared(
                    self.invoke(self.canonical_request()),
                    "RECORDED_SIGNAL_INVALID",
                )
                self._write_text(signal, original)

        with self._unreadable(signal):
            unreadable = self.invoke(self.canonical_request())
        if unreadable.get("outcome") == resolver.OUTCOME_PREPARED:
            self.skipTest("filesystem does not enforce unreadable file mode")
        self.assert_not_prepared(
            unreadable,
            "BOUNDED_COMPONENT_UNREADABLE",
        )

    def test_36_recorded_signal_minimum_structure_is_exact(self) -> None:
        signal_path = self.bounded_path("recorded_signal_path")
        canonical = json.loads(signal_path.read_text(encoding="utf-8"))
        for field in resolver._SIGNAL_REQUIRED_KEYS:
            with self.subTest(missing=field):
                value = copy.deepcopy(canonical)
                value.pop(field)
                self._write_json(signal_path, value)
                self.assert_not_prepared(
                    self.invoke(self.canonical_request()),
                    "RECORDED_SIGNAL_INVALID",
                )

        invalid_values = {
            "recorded_at": "",
            "duration_s": "1",
            "sample_rate_hz": "1000",
            "units": "",
            "device": [],
            "samples": [],
        }
        for field, value in invalid_values.items():
            with self.subTest(invalid=field):
                altered = copy.deepcopy(canonical)
                altered[field] = value
                self._write_json(signal_path, altered)
                self.assert_not_prepared(
                    self.invoke(self.canonical_request()),
                    "RECORDED_SIGNAL_INVALID",
                )
        self._write_json(signal_path, canonical)

    def test_37_unconstructable_candidate_is_not_prepared(self) -> None:
        expanded_fields = (*resolver.CANDIDATE_FIELDS, "required_extra_field")
        with patch.object(resolver, "CANDIDATE_FIELDS", expanded_fields):
            result = self.invoke(self.canonical_request())
        self.assert_not_prepared(
            result,
            "CANDIDATE_NOT_TRUTHFULLY_PREPARABLE",
        )

    def test_38_structural_invalidity_is_distinct_from_negative_evidence(
        self,
    ) -> None:
        changed_path = self.canonical_request()
        changed_path["bounded_source_references"][
            "recorded_signal_path"
        ] = "alternate/signal.json"
        self.assert_blocked(
            self.invoke(changed_path),
            "BOUNDED_SOURCE_REFERENCE_MISMATCH",
        )

        signal_path = self.bounded_path("recorded_signal_path")
        signal_path.unlink()
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "BOUNDED_COMPONENT_ABSENT",
        )
        self._copy_fixture(
            Path(resolver.BOUNDED_SOURCE_REFERENCES["recorded_signal_path"])
        )

        self.assert_blocked(
            self.invoke(
                self.canonical_request(
                    computed_archive_sha256=resolver.EXPECTED_ARCHIVE_SHA256
                )
            ),
            "REQUEST_FIELD_UNKNOWN",
        )
        archive = self.bounded_path("preserved_archive_path")
        archive.write_bytes(archive.read_bytes() + b"mismatch")
        self.assert_not_prepared(
            self.invoke(self.canonical_request()),
            "ARCHIVE_HASH_MISMATCH",
        )

        malformed_upstream = self.preparation_request_artifact_path()
        self._write_text(malformed_upstream, "{")
        self.assert_blocked(
            self.invoke(self.canonical_request()),
            "PREPARATION_REQUEST_ARTIFACT_NOT_PARSEABLE",
        )

    def test_39_ambiguity_is_preserved_and_not_forced_false(self) -> None:
        timestamp = self.bounded_path("attestation_timestamp_path")
        self._write_text(timestamp, "ambiguous timestamp\n")
        result = self.invoke(self.canonical_request())
        self.assert_not_prepared(result, "TIMESTAMP_INVALID")
        posture = result["bounded_path_and_file_evaluation"]
        self.assertIs(
            posture["ambiguity_postures"][
                "timestamp_interpretation_ambiguous"
            ],
            True,
        )
        self.assertIs(
            posture["unresolved_postures"][
                "trace_integrity_materially_unresolved"
            ],
            True,
        )

    def test_40_writer_refuses_candidate_shape_and_identity_mutations(
        self,
    ) -> None:
        prepared = self.invoke(self.canonical_request())
        self.assert_prepared(prepared)
        candidate = prepared["prepared_declaration_candidate"]
        self.assertIsInstance(candidate, dict)
        cases: list[tuple[str, Any]] = []

        missing = copy.deepcopy(prepared)
        missing["prepared_declaration_candidate"].pop(
            resolver.CANDIDATE_FIELDS[0]
        )
        cases.append(("missing_candidate_field", missing))

        additional = copy.deepcopy(prepared)
        additional["prepared_declaration_candidate"]["additional"] = False
        cases.append(("additional_candidate_field", additional))

        altered_path = copy.deepcopy(prepared)
        altered_path["prepared_declaration_candidate"][
            "preserved_archive_path"
        ] = "alternate/archive.zip"
        cases.append(("altered_canonical_path", altered_path))

        altered_hash = copy.deepcopy(prepared)
        altered_hash["prepared_declaration_candidate"][
            "expected_archive_sha256"
        ] = "0" * 64
        cases.append(("altered_expected_hash", altered_hash))

        empty_evaluator = copy.deepcopy(prepared)
        empty_evaluator["prepared_declaration_candidate"][
            "evaluator_reference"
        ] = ""
        cases.append(("empty_evaluator", empty_evaluator))

        missing_resolver = copy.deepcopy(prepared)
        missing_resolver["prepared_declaration_candidate"][
            "evaluator_reference"
        ] = (
            resolver.PREPARATION_ID
            + ":"
            + resolver.PREPARATION_RESULT_PREPARED
        )
        cases.append(("evaluator_missing_resolver", missing_resolver))

        for name, result in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(result, name)

    def test_41_writer_refuses_candidate_posture_map_mutations(self) -> None:
        prepared = self.invoke(self.canonical_request())
        families = (
            "trace_integrity_postures",
            "ambiguity_postures",
            "contradiction_postures",
            "unresolved_postures",
        )
        cases: list[tuple[str, dict[str, Any]]] = []
        missing_family = copy.deepcopy(prepared)
        missing_family["prepared_declaration_candidate"].pop(families[0])
        cases.append(("missing_posture_family", missing_family))

        additional_family = copy.deepcopy(prepared)
        additional_family["prepared_declaration_candidate"][
            "additional_posture_family"
        ] = {}
        cases.append(("additional_posture_family", additional_family))

        for family in families:
            posture = prepared["prepared_declaration_candidate"][family]
            key = next(iter(posture))
            missing_key = copy.deepcopy(prepared)
            missing_key["prepared_declaration_candidate"][family].pop(key)
            cases.append((f"{family}_missing_key", missing_key))

            additional_key = copy.deepcopy(prepared)
            additional_key["prepared_declaration_candidate"][family][
                "additional_key"
            ] = False
            cases.append((f"{family}_additional_key", additional_key))

            wrong_type = copy.deepcopy(prepared)
            wrong_type["prepared_declaration_candidate"][family][key] = 1
            cases.append((f"{family}_wrong_type", wrong_type))

        for name, result in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(result, name)

    def test_42_writer_refuses_candidate_nonconversion_and_nonclaims(
        self,
    ) -> None:
        prepared = self.invoke(self.canonical_request())
        first_non_claim = resolver.REQUIRED_BASIS_NON_CLAIMS[0]
        cases: list[tuple[str, dict[str, Any]]] = []

        altered_statement = copy.deepcopy(prepared)
        altered_statement["prepared_declaration_candidate"][
            "non_conversion_statement"
        ] = "altered"
        cases.append(("altered_non_conversion", altered_statement))

        missing = copy.deepcopy(prepared)
        missing["prepared_declaration_candidate"]["basis_non_claims"].pop(
            first_non_claim
        )
        cases.append(("missing_basis_non_claim", missing))

        additional = copy.deepcopy(prepared)
        additional["prepared_declaration_candidate"]["basis_non_claims"][
            "additional_non_claim"
        ] = False
        cases.append(("additional_basis_non_claim", additional))

        flipped = copy.deepcopy(prepared)
        flipped["prepared_declaration_candidate"]["basis_non_claims"][
            first_non_claim
        ] = True
        cases.append(("flipped_basis_non_claim", flipped))

        string_false = copy.deepcopy(prepared)
        string_false["prepared_declaration_candidate"]["basis_non_claims"][
            first_non_claim
        ] = "false"
        cases.append(("string_false_basis_non_claim", string_false))

        operation_result_field = copy.deepcopy(prepared)
        operation_result_field["prepared_declaration_candidate"][
            "basis_non_claims"
        ]["receiver_attestation_recorded"] = False
        cases.append(
            ("receiver_attestation_recorded_in_basis", operation_result_field)
        )

        for name, result in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(result, name)

    def test_43_omission_and_nonclaims_hold_across_all_branches(self) -> None:
        branches = (
            self.invoke(self.canonical_request()),
            self.invoke(self.canonical_request(selected=False)),
            self.invoke(self.canonical_request(unknown_field=True)),
        )
        for result in branches:
            with self.subTest(outcome=result["outcome"]):
                self.assert_canonical_false_non_claims(result)
                self.assert_omission_posture(result)
                serialized = json.dumps(result, sort_keys=True)
                for path_field in resolver.TEXT_COMPONENT_FIELDS:
                    body = self.bounded_path(path_field).read_text(
                        encoding="utf-8"
                    )
                    self.assertNotIn(body, serialized)
                self.assertNotIn(
                    self.bounded_path("recorded_signal_path").read_text(
                        encoding="utf-8"
                    ),
                    serialized,
                )

    def test_44_from_path_strict_json_and_override_visibility(self) -> None:
        parent = self.root / "requests"
        canonical_path = self._write_json(
            parent / "canonical.json",
            self.canonical_request(),
        )
        canonical = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_from_path(
            canonical_path
        )
        self.assert_prepared(canonical)

        selection_false_path = self._write_json(
            parent / "selection_false.json",
            self.canonical_request(selected=False),
        )
        self.assert_not_prepared(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_from_path(
                selection_false_path
            ),
            "PREPARATION_NOT_SELECTED",
        )

        malformed = self._write_text(parent / "malformed.json", "{")
        duplicate = self._write_text(
            parent / "duplicate.json",
            '{"intent":"a","intent":"b"}',
        )
        non_mapping = self._write_text(parent / "array.json", "[]")
        missing = parent / "missing.json"
        for name, path in (
            ("malformed", malformed),
            ("duplicate", duplicate),
            ("non_mapping", non_mapping),
            ("missing", missing),
        ):
            with self.subTest(case=name):
                self.assert_blocked(
                    resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_from_path(
                        path
                    ),
                    "REQUEST_NOT_MAPPING",
                )

        unknown_request = self.canonical_request(visible_override="visible")
        unknown_path = self._write_json(
            parent / "unknown.json",
            unknown_request,
        )
        self.assertEqual(unknown_request["visible_override"], "visible")
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_from_path(
                unknown_path
            ),
            "REQUEST_FIELD_UNKNOWN",
        )

    def test_45_determinism_input_immutability_and_source_stability(
        self,
    ) -> None:
        request = self.canonical_request()
        original_request = copy.deepcopy(request)
        fixture_before = {
            relative: (self.root / relative).read_bytes()
            for relative in FIXTURE_FILE_RELATIVE_PATHS
        }
        first = self.invoke(request)
        second = self.invoke(copy.deepcopy(request))
        self.assertEqual(first, second)
        self.assertEqual(request, original_request)
        self.assertEqual(
            request["bounded_source_references"],
            original_request["bounded_source_references"],
        )
        self.assertEqual(
            request["declared_non_claims"],
            original_request["declared_non_claims"],
        )
        fixture_after = {
            relative: (self.root / relative).read_bytes()
            for relative in FIXTURE_FILE_RELATIVE_PATHS
        }
        self.assertEqual(fixture_before, fixture_after)
        self.assert_fixture_files_unchanged()

        result_before = copy.deepcopy(first)
        summary = resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_summary(
            first
        )
        self.assertEqual(first, result_before)
        self.assertEqual(summary, first[SUMMARY_KEY])

    def test_46_summary_values_for_prepared_not_prepared_and_blocked(
        self,
    ) -> None:
        results = (
            (
                "prepared",
                self.invoke(self.canonical_request()),
                resolver.PREPARATION_RESULT_PREPARED,
                False,
                True,
                True,
            ),
            (
                "not_prepared",
                self.invoke(self.canonical_request(selected=False)),
                resolver.PREPARATION_RESULT_NOT_PREPARED,
                False,
                False,
                True,
            ),
            (
                "blocked",
                self.invoke(self.canonical_request(unknown=True)),
                resolver.PREPARATION_RESULT_NOT_EVALUATED,
                True,
                False,
                False,
            ),
        )
        for (
            name,
            result,
            preparation_result,
            blocked,
            candidate_prepared,
            completed,
        ) in results:
            with self.subTest(branch=name):
                summary = self.summary(result)
                self.assertEqual(
                    summary,
                    resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_summary(
                        result
                    ),
                )
                self.assertEqual(
                    summary["resolver_module"],
                    resolver.RESOLVER_MODULE,
                )
                self.assertEqual(
                    summary["result_version"],
                    resolver.RESULT_VERSION,
                )
                self.assertEqual(
                    summary["preparation_id"],
                    resolver.PREPARATION_ID,
                )
                self.assertEqual(
                    summary["preparation_type"],
                    resolver.PREPARATION_TYPE,
                )
                self.assertEqual(
                    summary["preparation_scope"],
                    resolver.PREPARATION_SCOPE,
                )
                self.assertEqual(
                    summary["selected_preparation_request_id"],
                    resolver.SELECTED_PREPARATION_REQUEST_ID,
                )
                self.assertEqual(
                    summary["selected_operation_id"],
                    resolver.OPERATION_ID,
                )
                self.assertEqual(
                    summary["selected_candidate_id"],
                    resolver.CANDIDATE_ID,
                )
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(
                    summary["preparation_result"],
                    preparation_result,
                )
                self.assertEqual(
                    summary["failed_check_count"],
                    result["failed_check_count"],
                )
                self.assertEqual(
                    summary["passed_check_count"],
                    result["passed_check_count"],
                )
                self.assertIs(summary["blocked"], blocked)
                self.assertIs(
                    summary["complete_21_field_candidate_prepared"],
                    candidate_prepared,
                )
                self.assertIs(summary["preparation_recorded"], completed)
                self.assertIs(
                    summary["preparation_result_recorded"],
                    completed,
                )
                self.assertIs(summary["preparation_exhausted"], completed)
                self.assertIs(
                    summary["basis_declaration_preparation_started"],
                    completed,
                )
                self.assertIs(
                    summary["basis_declaration_preparation_completed"],
                    completed,
                )
                self.assertIs(summary["operation_basis_declared"], False)
                self.assertIs(summary["operation_basis_supplied"], False)
                self.assertIs(summary["operation_basis_admitted"], False)
                self.assertIs(summary["operation_recorded"], False)
                self.assertIs(summary["operation_result_recorded"], False)
                self.assertIs(
                    summary["result_level_non_claims_canonical_false"],
                    True,
                )
                self.assertIs(summary["complete_material_omitted"], True)
                self.assertNotIn("prepared_declaration_candidate", summary)
                self.assertNotIn("text_component_metadata", summary)

        prepared_summary = self.summary(results[0][1])
        self.assertIs(
            prepared_summary["specification_markers_validated"],
            True,
        )
        self.assertIs(
            prepared_summary["preparation_request_artifact_validated"],
            True,
        )
        self.assertIs(
            prepared_summary["selected_boundary_reference_validated"],
            True,
        )
        self.assertIs(prepared_summary["bounded_paths_validated"], True)
        self.assertIs(
            prepared_summary["required_bounded_components_available"],
            True,
        )
        self.assertIs(
            prepared_summary["archive_hash_record_validated"],
            True,
        )
        self.assertEqual(
            prepared_summary["computed_archive_sha256"],
            resolver.EXPECTED_ARCHIVE_SHA256,
        )
        self.assertIs(
            prepared_summary["archive_correspondence_validated"],
            True,
        )
        self.assertIs(
            prepared_summary["required_text_components_validated"],
            True,
        )
        self.assertIs(prepared_summary["timestamp_validated"], True)
        self.assertIs(
            prepared_summary["recorded_signal_artifact_validated"],
            True,
        )

    def test_47_writer_writes_all_branches_with_exact_json(self) -> None:
        branches = (
            ("prepared", self.invoke(self.canonical_request())),
            (
                "not_prepared",
                self.invoke(self.canonical_request(selected=False)),
            ),
            (
                "blocked",
                self.invoke(self.canonical_request(unknown=True)),
            ),
        )
        for name, result in branches:
            with self.subTest(branch=name):
                output = self.safe_case_path(
                    self.root / "writer_valid",
                    name,
                )
                before = copy.deepcopy(result)
                written = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
                    result,
                    output,
                )
                self.assertIsInstance(written, Path)
                self.assertEqual(written, output)
                expected_text = (
                    json.dumps(
                        result,
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=True,
                        allow_nan=False,
                    )
                    + "\n"
                )
                self.assertEqual(
                    written.read_text(encoding="utf-8"),
                    expected_text,
                )
                self.assertEqual(
                    json.loads(written.read_text(encoding="utf-8")),
                    result,
                )
                self.assertEqual(result, before)

    def test_48_writer_never_overwrites_and_uses_stable_suffix(self) -> None:
        result = self.invoke(self.canonical_request())
        requested = self.root / "suffix" / resolver.OUTPUT_FILENAME
        first = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
            result,
            requested,
        )
        first_bytes = first.read_bytes()
        second = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
            result,
            requested,
        )
        self.assertEqual(first, requested)
        self.assertEqual(first.read_bytes(), first_bytes)
        self.assertNotEqual(first, second)
        self.assertEqual(
            second.name,
            f"{requested.stem}_001{requested.suffix}",
        )
        self.assertEqual(
            json.loads(second.read_text(encoding="utf-8")),
            result,
        )

    def test_49_writer_refuses_wrapper_and_branch_inconsistency(self) -> None:
        prepared = self.invoke(self.canonical_request())
        not_prepared = self.invoke(self.canonical_request(selected=False))
        blocked = self.invoke(self.canonical_request(unknown=True))
        cases: list[tuple[str, Any]] = [
            ("non_mapping", []),
        ]

        wrong_module = copy.deepcopy(prepared)
        wrong_module["resolver_module"] = "wrong"
        cases.append(("wrong_module", wrong_module))

        wrong_version = copy.deepcopy(prepared)
        wrong_version["result_version"] = "9.9.9"
        cases.append(("wrong_version", wrong_version))

        wrong_pair = copy.deepcopy(prepared)
        wrong_pair[STATE_KEY][
            "preparation_result"
        ] = resolver.PREPARATION_RESULT_NOT_PREPARED
        cases.append(("wrong_outcome_result_pair", wrong_pair))

        blocked_posture = copy.deepcopy(prepared)
        blocked_posture["block"]["blocked"] = True
        cases.append(("prepared_blocked_posture", blocked_posture))

        prepared_state = copy.deepcopy(prepared)
        prepared_state[STATE_KEY]["preparation_recorded"] = False
        cases.append(("prepared_state", prepared_state))

        no_candidate = copy.deepcopy(prepared)
        no_candidate["prepared_declaration_candidate"] = None
        cases.append(("prepared_without_candidate", no_candidate))

        not_prepared_candidate = copy.deepcopy(not_prepared)
        not_prepared_candidate["prepared_declaration_candidate"] = copy.deepcopy(
            prepared["prepared_declaration_candidate"]
        )
        cases.append(
            ("not_prepared_with_candidate", not_prepared_candidate)
        )

        blocked_candidate = copy.deepcopy(blocked)
        blocked_candidate["prepared_declaration_candidate"] = copy.deepcopy(
            prepared["prepared_declaration_candidate"]
        )
        cases.append(("blocked_with_candidate", blocked_candidate))

        not_prepared_state = copy.deepcopy(not_prepared)
        not_prepared_state[STATE_KEY][
            "receiver_attestation_operation_basis_prepared"
        ] = True
        cases.append(("not_prepared_state", not_prepared_state))

        blocked_state = copy.deepcopy(blocked)
        blocked_state[STATE_KEY]["preparation_recorded"] = True
        cases.append(("blocked_state", blocked_state))

        flipped_result_non_claim = copy.deepcopy(prepared)
        first_non_claim = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        flipped_result_non_claim["non_claims"][first_non_claim] = True
        cases.append(
            ("flipped_result_non_claim", flipped_result_non_claim)
        )

        missing_result_non_claim = copy.deepcopy(prepared)
        missing_result_non_claim["non_claims"].pop(first_non_claim)
        cases.append(
            ("missing_result_non_claim", missing_result_non_claim)
        )

        basis_declared = copy.deepcopy(prepared)
        basis_declared[STATE_KEY][
            "receiver_attestation_operation_basis_declared"
        ] = True
        cases.append(("basis_declared", basis_declared))

        basis_supplied = copy.deepcopy(prepared)
        basis_supplied[STATE_KEY][
            "receiver_attestation_operation_basis_supplied"
        ] = True
        cases.append(("basis_supplied", basis_supplied))

        basis_admitted = copy.deepcopy(prepared)
        basis_admitted[STATE_KEY][
            "receiver_attestation_operation_basis_admitted"
        ] = True
        cases.append(("basis_admitted", basis_admitted))

        operation_executed = copy.deepcopy(prepared)
        operation_executed[STATE_KEY][
            "receiver_attestation_operation_recorded"
        ] = True
        cases.append(("operation_executed", operation_executed))

        for name, result in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(result, name)

    def test_50_writer_refuses_embedded_complete_material(self) -> None:
        prepared = self.invoke(self.canonical_request())
        payloads: dict[str, Any] = {
            "complete_preparation_request_artifact": {"full": True},
            "complete_waiting_operation_artifact": {"full": True},
            "complete_upstream_boundary_artifact": {"full": True},
            "complete_candidate_sufficiency_artifact": {"full": True},
            "complete_candidate_sufficiency_basis": {"full": True},
            "archive_bytes": "raw archive bytes",
            "text_component_bodies": {"statement": "full body"},
            "recorded_signal_body": {"samples": [1, 2, 3]},
        }
        for field, payload in payloads.items():
            with self.subTest(payload=field):
                result = copy.deepcopy(prepared)
                result[STATEMENT_KEY][field] = payload
                self.assert_writer_refused(result, field)

    def test_51_writer_refuses_protected_and_incompatible_paths(self) -> None:
        result = self.invoke(self.canonical_request())
        protected_paths = (
            self.root / "spec" / "result.json",
            self.root / "src" / "result.json",
            self.root / "tests" / "result.json",
            self.root / "reference" / "result.json",
            (
                self.root
                / PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH
            ).parent
            / "result.json",
            (
                self.root / BOUNDARY_ARTIFACT_RELATIVE_PATH
            ).parent
            / "result.json",
            (
                self.root
                / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH
            ).parent
            / "result.json",
            (
                self.root
                / resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
            ).parent
            / "result.json",
            (
                self.root / resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            )
            / "result.json",
        )
        for output in protected_paths:
            with self.subTest(output=str(output)):
                with self.assertRaises(
                    resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError
                ):
                    resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
                        result,
                        output,
                    )
                self.assertFalse(output.exists())

        parent_file = self.root / "incompatible_parent"
        parent_file.write_text("not a directory", encoding="utf-8")
        with self.assertRaises(
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationV0MinError
        ):
            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_v0_min_result(
                result,
                parent_file / "result.json",
            )

    def test_52_preparation_is_candidate_only_and_single_use_posture(
        self,
    ) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_prepared(result)
        state = self.state(result)
        self.assertIs(
            state[
                "receiver_attestation_operation_basis_declaration_"
                "candidate_prepared"
            ],
            True,
        )
        for field in DOWNSTREAM_FALSE_FIELDS:
            self.assertIs(state[field], False)
        for field in (
            "repeated_receiver_attestation_operation_basis_declaration_"
            "preparation_permission_created",
            "reusable_receiver_attestation_operation_basis_declaration_"
            "preparation_route_created",
            "same_receiver_attestation_operation_basis_declaration_"
            "preparation_rerun_authorized",
            "automatic_receiver_attestation_operation_basis_declaration_"
            "preparation_retry_created",
            "receiver_attestation_operation_basis_declaration_"
            "preparation_debt_created",
            "receiver_attestation_operation_basis_declaration_"
            "preparation_obligation_created",
        ):
            self.assertIs(state[field], False)
        statement = result[STATEMENT_KEY]
        self.assertIs(
            statement["prepared_candidate_is_not_declared_basis"],
            True,
        )
        self.assertIs(
            statement["declared_basis_is_not_supplied_basis"],
            True,
        )
        self.assertIs(
            statement["supplied_basis_is_not_admitted_basis"],
            True,
        )
        self.assertIs(
            statement["admitted_basis_is_not_operation_execution"],
            True,
        )


if __name__ == "__main__":
    unittest.main()
