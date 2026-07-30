"""Tests for one exact receiver-attestation operation basis supply.

Clean branches consume the standing supply specification and DECLARED
declaration artifact. Negative cases use isolated temporary copies only. The
suite does not read capture evidence, admit basis, execute the operation, or
write a repository supply artifact.
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

import resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min as resolver


PREFIX = resolver.PREFIX
STATE_KEY = PREFIX
CHECKS_KEY = f"{PREFIX}_checks"
SUMMARY_KEY = f"{PREFIX}_summary"
STATEMENT_KEY = f"{PREFIX}_statement"
NON_MEANING_KEY = f"{PREFIX}_non_meaning"

SPECIFICATION_RELATIVE_PATH = resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
DECLARATION_ARTIFACT_RELATIVE_PATH = (
    resolver.SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH
)
SOURCE_RELATIVE_PATH = Path(
    "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min.py"
)
TEST_RELATIVE_PATH = Path(
    "tests/test_resolve_receiver_side_answerable_basis_receiver_attestation_"
    "operation_basis_supply_v0_min.py"
)
OUTPUT_RELATIVE_ROOT = resolver.OUTPUT_ROOT.relative_to(REPOSITORY_ROOT)

PRESERVED_RELATIVE_PATHS = (
    SPECIFICATION_RELATIVE_PATH,
    SOURCE_RELATIVE_PATH,
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "BASIS_DECLARATION_V0_MIN_SPEC.md"
    ),
    Path(
        "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
        "operation_basis_declaration_v0_min.py"
    ),
    Path(
        "tests/test_resolve_receiver_side_answerable_basis_receiver_"
        "attestation_operation_basis_declaration_v0_min.py"
    ),
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "BASIS_DECLARATION_V0_MIN_TERMINAL_SUMMARY.md"
    ),
    DECLARATION_ARTIFACT_RELATIVE_PATH,
)

SUPPLY_BRANCH_TRUE_FIELDS = (
    "supply_recorded",
    "supply_result_recorded",
    "supply_exhausted",
)

DECLARATION_REQUIRED_TRUE_FIELDS = (
    "basis_declaration_selected",
    "specification_markers_validated",
    "selected_preparation_artifact_validated",
    "declaration_candidate_received",
    "exact_21_field_candidate_validated",
    "declaration_recorded",
    "declaration_result_recorded",
    "declaration_exhausted",
    "receiver_attestation_operation_basis_declaration_recorded",
    "receiver_attestation_operation_basis_declared",
    *resolver.UPSTREAM_DECLARATION_OMISSION_FIELDS,
)

DECLARATION_REQUIRED_FALSE_FIELDS = tuple(
    dict.fromkeys(
        (
            "receiver_attestation_operation_basis_supplied",
            "receiver_attestation_operation_basis_admitted",
            "receiver_attestation_operation_executed",
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
            "custody_created",
            "provenance_created",
            "physical_validity_created",
            *resolver.UPSTREAM_DECLARATION_FALSE_NON_CLAIMS,
        )
    )
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


class _DuplicateJsonKeyError(ValueError):
    """Raised by the independent strict test loader."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


class ReceiverAttestationOperationBasisSupplyTests(unittest.TestCase):
    """Exercise exact supply, separation, digest, and writer locks."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_hashes = {
            relative: cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        cls.output_root_existed = resolver.OUTPUT_ROOT.exists()

    @classmethod
    def tearDownClass(cls) -> None:
        current = {
            relative: cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        if current != cls.preserved_hashes:
            raise AssertionError(
                "receiver-attestation supply lineage changed during tests"
            )
        if resolver.OUTPUT_ROOT.exists() != cls.output_root_existed:
            raise AssertionError("repository supply artifact root changed")

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

    def _load_strict_json(self, path: Path) -> dict[str, Any]:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_json_keys,
            parse_constant=lambda item: (_ for _ in ()).throw(
                ValueError(item)
            ),
        )
        self.assertIsInstance(value, dict)
        return copy.deepcopy(value)

    def declaration_artifact(self) -> dict[str, Any]:
        return self._load_strict_json(
            REPOSITORY_ROOT / DECLARATION_ARTIFACT_RELATIVE_PATH
        )

    def declared_basis(self) -> dict[str, Any]:
        value = self.declaration_artifact().get(
            "declared_receiver_attestation_operation_basis"
        )
        self.assertIsInstance(value, dict)
        return copy.deepcopy(value)

    def canonical_request(
        self,
        *,
        selected: bool = True,
        **overrides: Any,
    ) -> dict[str, Any]:
        return resolver.build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(
            basis_supply_selected=selected,
            **copy.deepcopy(overrides),
        )

    def invoke(self, request: Any = None) -> dict[str, Any]:
        return resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min(
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

    def assert_check_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        self.assertEqual(
            result.get("failed_check_count"),
            sum(item.get("passed") is False for item in checks),
        )
        self.assertEqual(
            result.get("passed_check_count"),
            sum(item.get("passed") is True for item in checks),
        )

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

    def assert_canonical_false_non_claims(
        self,
        result: Mapping[str, Any],
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, Mapping)
        self.assertEqual(
            set(non_claims),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(type(non_claims[field]), bool)
            self.assertIs(non_claims[field], False)
            self.assertIs(self.state(result)[field], False)

    def assert_omission_posture(self, result: Mapping[str, Any]) -> None:
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, Mapping)
        self.assertEqual(
            set(omission),
            set(resolver.RESULT_OMISSION_FIELDS),
        )
        for field in resolver.RESULT_OMISSION_FIELDS:
            self.assertIs(omission[field], True)
            self.assertIs(self.state(result)[field], True)

    def assert_downstream_false(self, result: Mapping[str, Any]) -> None:
        state = self.state(result)
        for field in resolver.EXTRA_REQUIRED_FALSE_POSTURES:
            self.assertIn(field, state)
            self.assertIs(type(state[field]), bool)
            self.assertIs(state[field], False)
        self.assert_canonical_false_non_claims(result)
        self.assert_omission_posture(result)

    def assert_no_complete_material(self, result: Mapping[str, Any]) -> None:
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

    def assert_supplied(self, result: Mapping[str, Any]) -> dict[str, Any]:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_SUPPLIED)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("supply_result"),
            resolver.SUPPLY_RESULT_SUPPLIED,
        )
        for field in SUPPLY_BRANCH_TRUE_FIELDS:
            self.assertIs(state.get(field), True)
        self.assertIs(state.get(resolver.REQUEST_SELECTION_FIELD), True)
        self.assertIs(state.get("supply_basis_received"), True)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_supply_recorded"
            ),
            True,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_declared"),
            True,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_supplied"),
            True,
        )
        basis = result.get(resolver.SUPPLIED_BASIS_SECTION)
        self.assertIsInstance(basis, dict)
        self.assertEqual(basis, self.declared_basis())
        self.assert_downstream_false(result)
        self.assert_no_complete_material(result)
        return basis

    def assert_not_supplied(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_SUPPLIED)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("supply_result"),
            resolver.SUPPLY_RESULT_NOT_SUPPLIED,
        )
        for field in SUPPLY_BRANCH_TRUE_FIELDS:
            self.assertIs(state.get(field), True)
        self.assertIs(state.get(resolver.REQUEST_SELECTION_FIELD), False)
        self.assertIs(state.get("supply_basis_received"), True)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_supply_recorded"
            ),
            False,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_declared"),
            True,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_supplied"),
            False,
        )
        self.assertNotIn(resolver.SUPPLIED_BASIS_SECTION, result)
        self.assert_downstream_false(result)
        self.assert_no_complete_material(result)

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        state = self.state(result)
        self.assertEqual(
            state.get("supply_result"),
            resolver.SUPPLY_RESULT_NOT_EVALUATED,
        )
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), True)
        self.assertIsInstance(block.get("code"), str)
        self.assertTrue(block.get("code"))
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(block.get("code"), expected_code)
        self.assertIs(state.get("supply_recorded"), False)
        self.assertIs(state.get("supply_result_recorded"), False)
        self.assertIs(state.get("supply_exhausted"), False)
        self.assertIs(
            state.get(
                "receiver_attestation_operation_basis_supply_recorded"
            ),
            False,
        )
        self.assertIs(
            state.get("receiver_attestation_operation_basis_supplied"),
            False,
        )
        self.assertNotIn(resolver.SUPPLIED_BASIS_SECTION, result)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        self.assert_downstream_false(result)
        self.assert_check_counts(result)
        self.assert_all_emitted_codes_public(result)

    @contextmanager
    def isolated_inputs(
        self,
    ) -> Iterator[tuple[Path, Path, Path]]:
        with tempfile.TemporaryDirectory(dir=self.root) as directory:
            isolated_root = Path(directory)
            specification = isolated_root / SPECIFICATION_RELATIVE_PATH
            artifact = isolated_root / DECLARATION_ARTIFACT_RELATIVE_PATH
            specification.parent.mkdir(parents=True, exist_ok=True)
            artifact.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(
                REPOSITORY_ROOT / SPECIFICATION_RELATIVE_PATH,
                specification,
            )
            shutil.copy2(
                REPOSITORY_ROOT / DECLARATION_ARTIFACT_RELATIVE_PATH,
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
                    "SELECTED_DECLARATION_ARTIFACT_PATH",
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
            artifact = self._load_strict_json(artifact_path)
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
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError
        ):
            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                result,
                output,
            )
        self.assertFalse(output.exists())

    def test_01_public_api_and_constant_contract(self) -> None:
        public_callables = (
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min_request",
            "build_declared_receiver_side_answerable_basis_receiver_"
            "attestation_operation_basis_supply_v0_min_request",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min_from_path",
            "build_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min_summary",
            "write_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min_result",
        )
        for name in public_callables:
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(
            issubclass(
                resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError,
                Exception,
            )
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_supply_v0_min",
        )
        self.assertEqual(
            resolver.SUPPLY_ID,
            "receiver_side_answerable_basis_receiver_attestation_operation_"
            "basis_supply_001",
        )
        self.assertEqual(
            resolver.SUPPLY_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
            "BASIS_SUPPLY",
        )
        self.assertEqual(resolver.SUPPLY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.SUPPLY_SCOPE,
            "SUPPLY_ONE_EXACT_DECLARED_RECEIVER_ATTESTATION_OPERATION_BASIS_"
            "TO_ONE_SELECTED_OPERATION_ONLY",
        )
        self.assertEqual(resolver.DECLARATION_ID, resolver.SELECTED_DECLARATION_ID)
        self.assertEqual(
            resolver.SELECTED_PREPARATION_ID,
            "receiver_side_answerable_basis_receiver_attestation_operation_"
            "basis_declaration_preparation_001",
        )
        self.assertEqual(
            resolver.SELECTED_PREPARATION_REQUEST_ID,
            "receiver_side_answerable_basis_receiver_attestation_operation_"
            "basis_declaration_preparation_request_001",
        )
        self.assertEqual(
            resolver.OPERATION_ID,
            "receiver_side_answerable_basis_receiver_attestation_operation_001",
        )
        self.assertEqual(
            resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_001",
        )
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            SPECIFICATION_RELATIVE_PATH,
        )
        self.assertEqual(
            resolver.SELECTED_DECLARATION_ARTIFACT_RELATIVE_PATH,
            DECLARATION_ARTIFACT_RELATIVE_PATH,
        )
        self.assertEqual(resolver.CANDIDATE_DIGEST_ALGORITHM, "SHA-256")
        self.assertEqual(
            resolver.EXPECTED_CANDIDATE_SHA256,
            "8e1bf1eba4e2916078f83ad2afe1f66d8d4c4dfd7b7955674a20b5ed730f2165",
        )
        self.assertEqual(len(resolver.CANDIDATE_FIELDS), 21)
        self.assertEqual(len(resolver.REQUIRED_BASIS_NON_CLAIMS), 39)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_SUPPLIED,
                resolver.OUTCOME_NOT_SUPPLIED,
                resolver.OUTCOME_BLOCKED,
            },
        )
        self.assertEqual(
            set(resolver.SUPPLY_RESULT_FAMILY),
            {
                resolver.SUPPLY_RESULT_SUPPLIED,
                resolver.SUPPLY_RESULT_NOT_SUPPLIED,
                resolver.SUPPLY_RESULT_NOT_EVALUATED,
            },
        )
        self.assertFalse(resolver.OUTPUT_ROOT.exists())

    def test_02_canonical_request_builder_schema_and_values(self) -> None:
        request = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
        )
        expected_keys = {
            resolver.REQUEST_SELECTION_FIELD,
            "declared_non_claims",
            "supply_id",
            "supply_type",
            "supply_version",
            "supply_scope",
            "selected_declaration_id",
            "selected_declaration_type",
            "selected_declaration_version",
            "selected_declaration_scope",
            "selected_preparation_id",
            "selected_preparation_request_id",
            "selected_receiver_attestation_operation_id",
            "selected_receiver_attestation_operation_type",
            "selected_receiver_attestation_operation_version",
            "selected_receiver_attestation_operation_scope",
            "receiver_side_answerable_basis_candidate_id",
            "receiver_side_answerable_basis_candidate_type",
            "receiver_side_answerable_basis_candidate_scope",
            "governing_supply_specification_path",
            "selected_declaration_artifact_path",
            *resolver.PROHIBITED_INPUT_FLAGS,
        }
        self.assertIsInstance(request, dict)
        self.assertEqual(set(request), expected_keys)
        self.assertIs(request[resolver.REQUEST_SELECTION_FIELD], True)
        self.assertEqual(request["supply_id"], resolver.SUPPLY_ID)
        self.assertEqual(
            request["selected_declaration_id"],
            resolver.DECLARATION_ID,
        )
        self.assertEqual(
            request["selected_receiver_attestation_operation_id"],
            resolver.OPERATION_ID,
        )
        self.assertEqual(
            request["governing_supply_specification_path"],
            str(SPECIFICATION_RELATIVE_PATH),
        )
        self.assertEqual(
            request["selected_declaration_artifact_path"],
            str(DECLARATION_ARTIFACT_RELATIVE_PATH),
        )
        self.assertTrue(
            all(
                request[field] is False
                for field in resolver.PROHIBITED_INPUT_FLAGS
            )
        )
        self.assertEqual(
            set(request["declared_non_claims"]),
            set(resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                type(value) is bool and value is False
                for value in request["declared_non_claims"].values()
            )
        )
        for prohibited_payload in (
            "declared_receiver_attestation_operation_basis",
            "replacement_declared_basis",
            "candidate_sha256",
            "trace_integrity_postures",
            "supply_outcome",
            "supply_result",
            "operation_outcome",
            "operation_result",
            "complete_declaration_artifact",
            "raw_source_body",
        ):
            self.assertNotIn(prohibited_payload, request)

    def test_03_request_builders_are_independent_and_deterministic(self) -> None:
        first = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
        )
        second = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request()
        )
        declared = self.canonical_request()
        self.assertEqual(first, second)
        self.assertEqual(first, declared)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"],
            second["declared_non_claims"],
        )
        first["declared_non_claims"][
            resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        first["supply_id"] = "mutated"
        self.assertEqual(
            second,
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(),
        )
        false_request = self.canonical_request(selected=False)
        self.assertIs(false_request[resolver.REQUEST_SELECTION_FIELD], False)
        visible = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_request(
                basis_supply_selected=None
            )
        )
        self.assertIsNone(visible[resolver.REQUEST_SELECTION_FIELD])

    def test_04_declared_builder_keeps_overrides_and_input_immutable(
        self,
    ) -> None:
        overrides = {
            "unknown_visible_override": {"nested": [1, 2, 3]},
        }
        before = copy.deepcopy(overrides)
        request = self.canonical_request(**overrides)
        self.assertEqual(overrides, before)
        self.assertEqual(
            request["unknown_visible_override"],
            overrides["unknown_visible_override"],
        )
        self.assertIsNot(
            request["unknown_visible_override"],
            overrides["unknown_visible_override"],
        )
        self.assert_blocked(
            self.invoke(request),
            "REQUEST_FIELD_UNKNOWN",
        )

        wrong = self.canonical_request(supply_id="wrong")
        wrong_before = copy.deepcopy(wrong)
        self.assert_blocked(
            self.invoke(wrong),
            "SUPPLY_IDENTITY_MISMATCH",
        )
        self.assertEqual(wrong, wrong_before)

    def test_05_canonical_supplied_branch(self) -> None:
        result = self.invoke(self.canonical_request())
        basis = self.assert_supplied(result)
        self.assertEqual(len(basis), 21)
        self.assertGreater(result["passed_check_count"], 0)
        self.assertEqual(
            result["supply_decision"],
            {
                "caller_selected_result": False,
                "code": "BASIS_SUPPLIED",
                "precedence": "BLOCKED_THEN_NOT_SUPPLIED_THEN_SUPPLIED",
                "reason": "exact declared basis supplied",
            },
        )
        self.assertIs(
            self.state(result)[
                "receiver_attestation_operation_basis_admission_gate_passed"
            ],
            False,
        )

    def test_06_supplied_basis_is_exact_and_separate(self) -> None:
        declaration = self.declaration_artifact()
        declaration_before = copy.deepcopy(declaration)
        result = self.invoke(self.canonical_request())
        basis = self.assert_supplied(result)
        expected = declaration[
            "declared_receiver_attestation_operation_basis"
        ]
        self.assertEqual(basis, expected)
        self.assertIsNot(basis, expected)
        self.assertEqual(set(basis), set(resolver.CANDIDATE_FIELDS))
        self.assertEqual(
            basis["trace_integrity_postures"],
            dict(resolver.EXPECTED_TRACE_INTEGRITY_POSTURES),
        )
        self.assertEqual(
            basis["ambiguity_postures"],
            dict(resolver.EXPECTED_AMBIGUITY_POSTURES),
        )
        self.assertEqual(
            basis["contradiction_postures"],
            dict(resolver.EXPECTED_CONTRADICTION_POSTURES),
        )
        self.assertEqual(
            basis["unresolved_postures"],
            dict(resolver.EXPECTED_UNRESOLVED_POSTURES),
        )
        self.assertEqual(
            basis["non_conversion_statement"],
            resolver.NON_CONVERSION_STATEMENT,
        )
        self.assertEqual(
            set(basis["basis_non_claims"]),
            set(resolver.REQUIRED_BASIS_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                type(value) is bool and value is False
                for value in basis["basis_non_claims"].values()
            )
        )
        self.assertEqual(declaration, declaration_before)

    def test_07_declared_basis_digest_contract_is_independent(self) -> None:
        basis = self.declared_basis()
        canonical = json.dumps(
            basis,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        digest = hashlib.sha256(canonical).hexdigest()
        self.assertEqual(digest, resolver.EXPECTED_CANDIDATE_SHA256)
        result = self.invoke(self.canonical_request())
        self.assert_supplied(result)
        detail = result["declared_basis_digest"]
        self.assertEqual(
            detail["declared_basis_digest_algorithm"],
            "SHA-256",
        )
        self.assertEqual(detail["declared_basis_sha256"], digest)
        self.assertIs(
            detail["declared_basis_digest_correspondence_validated"],
            True,
        )
        self.assertIs(detail["caller_supplied_digest_used"], False)
        self.assertIs(detail["digest_is_correspondence_only"], True)

    def test_08_stale_open_list_is_disclosed_and_preserved(self) -> None:
        artifact = self.declaration_artifact()
        before = copy.deepcopy(artifact)
        open_items = artifact["what_remains_open"]
        for item in resolver.STALE_OPEN_LIST_ENTRIES:
            self.assertIn(item, open_items)
        result = self.invoke(self.canonical_request())
        self.assert_supplied(result)
        detail = result[
            "declaration_artifact_stale_open_list_validation"
        ]
        self.assertEqual(
            detail["declaration_artifact_stale_open_list_entries"],
            list(resolver.STALE_OPEN_LIST_ENTRIES),
        )
        self.assertIs(
            detail[
                "declaration_artifact_stale_open_list_entries_disclosed"
            ],
            True,
        )
        self.assertIs(
            detail[
                "declaration_artifact_stale_open_list_entries_preserved"
            ],
            True,
        )
        self.assertIs(
            detail[
                "declaration_artifact_stale_open_list_entries_not_used_as_supply_block"
            ],
            True,
        )
        self.assertIs(
            detail["declaration_artifact_stale_open_list_repaired"],
            False,
        )
        self.assertIs(
            detail["declaration_artifact_stale_open_list_normalized"],
            False,
        )
        state = self.state(result)
        for field in (
            "receiver_attestation_operation_basis_supply_debt_created",
            "receiver_attestation_operation_basis_supply_obligation_created",
            "automatic_receiver_attestation_operation_basis_supply_retry_created",
        ):
            self.assertIs(state[field], False)
        self.assertEqual(self.declaration_artifact(), before)

    def test_09_lawful_not_supplied_branch(self) -> None:
        result = self.invoke(self.canonical_request(selected=False))
        self.assert_not_supplied(result)
        state = self.state(result)
        self.assertEqual(state["decision_code"], "BASIS_NOT_SUPPLIED")
        self.assertEqual(
            state["decision_reason"],
            "exact declared basis supply not selected",
        )
        non_meaning = result[NON_MEANING_KEY]
        self.assertIs(non_meaning["supply_does_not_admit_basis"], True)
        self.assertNotIn("receiver_attestation_not_recorded", result)
        self.assertNotIn("receiver_attestation_indeterminate", result)

    def test_10_canonical_blocked_and_structural_precedence(self) -> None:
        self.assert_blocked(self.invoke([]), "REQUEST_NOT_MAPPING")
        unknown = self.canonical_request(selected=False)
        unknown["unknown"] = True
        self.assert_blocked(
            self.invoke(unknown),
            "REQUEST_FIELD_UNKNOWN",
        )

    def test_11_request_missing_unknown_identity_and_path_matrix(self) -> None:
        canonical = self.canonical_request()
        missing = copy.deepcopy(canonical)
        missing.pop("supply_id")
        self.assert_blocked(
            self.invoke(missing),
            "REQUEST_FIELD_MISSING",
        )
        unknown = copy.deepcopy(canonical)
        unknown["unknown"] = False
        self.assert_blocked(
            self.invoke(unknown),
            "REQUEST_FIELD_UNKNOWN",
        )
        cases = (
            ("supply_id", "wrong", "SUPPLY_IDENTITY_MISMATCH"),
            ("supply_type", "wrong", "SUPPLY_IDENTITY_MISMATCH"),
            ("supply_version", "9.9.9", "SUPPLY_IDENTITY_MISMATCH"),
            ("supply_scope", "wrong", "SUPPLY_IDENTITY_MISMATCH"),
            (
                "selected_declaration_id",
                "wrong",
                "DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_declaration_type",
                "wrong",
                "DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_declaration_version",
                "wrong",
                "DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_declaration_scope",
                "wrong",
                "DECLARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_preparation_id",
                "wrong",
                "PREPARATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_preparation_request_id",
                "wrong",
                "PREPARATION_REQUEST_IDENTITY_MISMATCH",
            ),
            (
                "selected_receiver_attestation_operation_id",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "selected_receiver_attestation_operation_type",
                "wrong",
                "SELECTED_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "receiver_side_answerable_basis_candidate_id",
                "wrong",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "receiver_side_answerable_basis_candidate_type",
                "wrong",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "governing_supply_specification_path",
                "wrong",
                "GOVERNING_SPECIFICATION_PATH_MISMATCH",
            ),
            (
                "selected_declaration_artifact_path",
                "wrong",
                "DECLARATION_ARTIFACT_PATH_MISMATCH",
            ),
        )
        for field, value, code in cases:
            with self.subTest(field=field):
                request = copy.deepcopy(canonical)
                request[field] = value
                self.assert_blocked(self.invoke(request), code)

    def test_12_supply_selection_requires_exact_builtin_boolean(self) -> None:
        for value in (None, 0, 1, "true", [], {}):
            with self.subTest(value=repr(value)):
                request = self.canonical_request()
                request[resolver.REQUEST_SELECTION_FIELD] = value
                self.assert_blocked(
                    self.invoke(request),
                    "SUPPLY_SELECTION_INVALID",
                )

    def test_13_every_prohibited_input_true_blocks(self) -> None:
        for field, expected_code in resolver.PROHIBITED_INPUT_FLAGS.items():
            with self.subTest(field=field):
                request = self.canonical_request()
                request[field] = True
                self.assert_blocked(
                    self.invoke(request),
                    expected_code,
                )

    def test_14_prohibited_inputs_require_exact_false(self) -> None:
        representative = (
            "replacement_declared_basis_supplied",
            "candidate_digest_supplied",
            "basis_posture_maps_supplied",
            "supply_outcome_selected_by_caller",
            "operation_result_selected_by_caller",
            "declaration_replay_requested",
            "evidence_reevaluation_requested",
            "archive_rehash_requested",
            "bounded_capture_read_requested",
            "basis_admission_preclaimed",
            "operation_execution_preclaimed",
            "receiver_attestation_preclaimed",
            "receiver_answerable_receipt_preclaimed",
            "presence_preclaimed",
            "repair_requested",
            "stale_open_list_repair_requested",
            "stale_open_list_normalization_requested",
            "complete_declaration_artifact_embedded",
            "archive_bytes_embedded",
            "recorded_signal_body_embedded",
        )
        for field in representative:
            for value in (None, 0, 1, "false", [], {}):
                with self.subTest(field=field, value=repr(value)):
                    request = self.canonical_request()
                    request[field] = value
                    self.assert_blocked(
                        self.invoke(request),
                        "REQUEST_VALUE_MISMATCH",
                    )

    def test_15_request_non_claim_shape_and_type_failures(self) -> None:
        canonical = self.canonical_request()
        first = resolver.REQUEST_REQUIRED_FALSE_NON_CLAIMS[0]
        cases: list[tuple[str, Any]] = []
        flipped = copy.deepcopy(canonical)
        flipped["declared_non_claims"][first] = True
        cases.append(("flipped", flipped))
        missing = copy.deepcopy(canonical)
        missing["declared_non_claims"].pop(first)
        cases.append(("missing", missing))
        additional = copy.deepcopy(canonical)
        additional["declared_non_claims"]["unknown"] = False
        cases.append(("additional", additional))
        for value in (None, 0, 1, "false", [], {}):
            wrong = copy.deepcopy(canonical)
            wrong["declared_non_claims"][first] = value
            cases.append((f"wrong_{type(value).__name__}_{value!r}", wrong))
        cases.extend(
            (
                ("mapping_none", {**canonical, "declared_non_claims": None}),
                ("mapping_list", {**canonical, "declared_non_claims": []}),
            )
        )
        for name, request in cases:
            with self.subTest(case=name):
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )

    def test_16_specification_exact_markers_pass(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_supplied(result)
        detail = result["specification_marker_validation"]
        self.assertIs(detail["specification_markers_validated"], True)
        self.assertEqual(
            set(detail["marker_status"]),
            set(resolver.SPECIFICATION_MARKER_CLASSES),
        )
        self.assertTrue(all(detail["marker_status"].values()))

    def test_17_each_specification_marker_class_is_required(self) -> None:
        for marker_class, markers in resolver.SPECIFICATION_MARKER_CLASSES.items():
            with self.subTest(marker_class=marker_class):
                with self.isolated_inputs() as (_, spec_path, _):
                    text = spec_path.read_text(encoding="utf-8")
                    marker = markers[0]
                    self.assertIn(marker, text)
                    self._write_text(
                        spec_path,
                        text.replace(marker, f"REMOVED_{marker_class.upper()}"),
                    )
                    self.assert_blocked(
                        self.invoke(self.canonical_request()),
                        "SPECIFICATION_MARKER_MISSING",
                    )

    def test_18_specification_missing_and_non_file_block(self) -> None:
        with self.isolated_inputs() as (_, spec_path, _):
            spec_path.unlink()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "SPECIFICATION_NOT_AVAILABLE",
            )
        with self.isolated_inputs() as (_, spec_path, _):
            spec_path.unlink()
            spec_path.mkdir()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "SPECIFICATION_NOT_AVAILABLE",
            )

    def test_19_declaration_artifact_file_and_json_failures(self) -> None:
        with self.isolated_inputs() as (_, _, artifact_path):
            artifact_path.unlink()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_NOT_AVAILABLE",
            )
        with self.isolated_inputs() as (_, _, artifact_path):
            artifact_path.unlink()
            artifact_path.mkdir()
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_NOT_AVAILABLE",
            )
        with self.isolated_inputs() as (_, _, artifact_path):
            self._write_text(artifact_path, "{")
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_NOT_PARSEABLE",
            )
        with self.isolated_inputs() as (_, _, artifact_path):
            self._write_text(
                artifact_path,
                '{"resolver_module":"a","resolver_module":"b"}',
            )
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_NOT_PARSEABLE",
            )
        with self.isolated_inputs() as (_, _, artifact_path):
            self._write_text(artifact_path, "[]\n")
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_NOT_MAPPING",
            )

    def test_20_declaration_root_metadata_is_exact(self) -> None:
        cases = (
            (
                "resolver_module",
                "wrong",
                "DECLARATION_ARTIFACT_METADATA_MISMATCH",
            ),
            (
                "result_version",
                "9.9.9",
                "DECLARATION_ARTIFACT_METADATA_MISMATCH",
            ),
            (
                "failed_check_count",
                1,
                "DECLARATION_ARTIFACT_FAILED_CHECKS_PRESENT",
            ),
            (
                "passed_check_count",
                54,
                "DECLARATION_ARTIFACT_METADATA_MISMATCH",
            ),
            (
                "outcome",
                "wrong",
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
        )
        for field, value, code in cases:
            with self.subTest(field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field, value=value: artifact.__setitem__(
                        field,
                        value,
                    ),
                    code,
                )
        for field in ("failed_check_count", "passed_check_count"):
            with self.subTest(field=f"{field}_bool"):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact.__setitem__(
                        field,
                        True,
                    ),
                    (
                        "DECLARATION_ARTIFACT_FAILED_CHECKS_PRESENT"
                        if field == "failed_check_count"
                        else "DECLARATION_ARTIFACT_METADATA_MISMATCH"
                    ),
                )

    def test_21_declaration_identity_locations_are_exact(self) -> None:
        metadata_key = f"{resolver.DECLARATION_PREFIX}_metadata"
        state_key = resolver.DECLARATION_PREFIX
        request_key = f"declared_{resolver.DECLARATION_PREFIX}_request"
        identity_key = (
            "selected_declaration_preparation_request_operation_candidate_identity"
        )
        summary_key = f"{resolver.DECLARATION_PREFIX}_summary"
        cases = (
            (metadata_key, "declaration_id"),
            (metadata_key, "declaration_type"),
            (identity_key, "selected_preparation_id"),
            (identity_key, "selected_preparation_request_id"),
            (identity_key, "selected_operation_id"),
            (identity_key, "selected_candidate_id"),
            (identity_key, "governing_specification_path"),
            (state_key, "selected_preparation_id"),
            (state_key, "selected_preparation_request_id"),
            (state_key, "selected_receiver_attestation_operation_id"),
            (request_key, "selected_preparation_id"),
            (request_key, "selected_preparation_request_id"),
            (request_key, "selected_receiver_attestation_operation_id"),
            (summary_key, "selected_operation_id"),
            (summary_key, "selected_candidate_id"),
        )
        for section, field in cases:
            with self.subTest(section=section, field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, section=section, field=field: artifact[
                        section
                    ].__setitem__(field, "wrong"),
                    "DECLARATION_ARTIFACT_IDENTITY_MISMATCH"
                    if section != summary_key
                    else "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_22_declaration_decision_and_block_are_exact(self) -> None:
        state_key = resolver.DECLARATION_PREFIX
        decision_key = "declaration_decision"
        cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None], str],
            ...,
        ] = (
            (
                "declaration_result",
                lambda artifact: artifact[state_key].__setitem__(
                    "declaration_result",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "state_decision_code",
                lambda artifact: artifact[state_key].__setitem__(
                    "decision_code",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "state_decision_reason",
                lambda artifact: artifact[state_key].__setitem__(
                    "decision_reason",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "decision_code",
                lambda artifact: artifact[decision_key].__setitem__(
                    "code",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "decision_reason",
                lambda artifact: artifact[decision_key].__setitem__(
                    "reason",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "caller_selected",
                lambda artifact: artifact[decision_key].__setitem__(
                    "caller_selected_result",
                    True,
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "precedence",
                lambda artifact: artifact[decision_key].__setitem__(
                    "precedence",
                    "wrong",
                ),
                "DECLARATION_ARTIFACT_NOT_DECLARED",
            ),
            (
                "blocked",
                lambda artifact: artifact["block"].__setitem__(
                    "blocked",
                    True,
                ),
                "DECLARATION_ARTIFACT_BLOCKED",
            ),
            (
                "block_code",
                lambda artifact: artifact["block"].__setitem__(
                    "code",
                    "UPSTREAM_BLOCK",
                ),
                "DECLARATION_ARTIFACT_BLOCKED",
            ),
        )
        for name, mutator, code in cases:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutator, code)

    def test_23_declaration_required_true_postures_are_exact(self) -> None:
        state_key = resolver.DECLARATION_PREFIX
        for field in DECLARATION_REQUIRED_TRUE_FIELDS:
            with self.subTest(field=field, value=False):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact[state_key].__setitem__(
                        field,
                        False,
                    ),
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )
        representative = DECLARATION_REQUIRED_TRUE_FIELDS[0]
        for name, value in (
            ("missing", object()),
            ("null", None),
            ("integer", 1),
            ("string", "true"),
        ):
            with self.subTest(field=representative, case=name):
                if name == "missing":
                    mutator = lambda artifact: artifact[state_key].pop(
                        representative
                    )
                else:
                    mutator = lambda artifact, value=value: artifact[
                        state_key
                    ].__setitem__(representative, value)
                self.assert_artifact_mutation_blocks(
                    mutator,
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_24_declaration_required_false_postures_are_exact(self) -> None:
        state_key = resolver.DECLARATION_PREFIX
        for field in DECLARATION_REQUIRED_FALSE_FIELDS:
            with self.subTest(field=field, value=True):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact[state_key].__setitem__(
                        field,
                        True,
                    ),
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )
        representative = DECLARATION_REQUIRED_FALSE_FIELDS[0]
        for name, value in (
            ("missing", object()),
            ("null", None),
            ("integer", 0),
            ("string", "false"),
        ):
            with self.subTest(field=representative, case=name):
                if name == "missing":
                    mutator = lambda artifact: artifact[state_key].pop(
                        representative
                    )
                else:
                    mutator = lambda artifact, value=value: artifact[
                        state_key
                    ].__setitem__(representative, value)
                self.assert_artifact_mutation_blocks(
                    mutator,
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )

    def test_25_historically_sensitive_false_locks_are_exact(self) -> None:
        state_key = resolver.DECLARATION_PREFIX
        for field in SENSITIVE_FALSE_FIELDS:
            with self.subTest(location="state", field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact[state_key].__setitem__(
                        field,
                        True,
                    ),
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )
            with self.subTest(location="non_claims", field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact[
                        "non_claims"
                    ].__setitem__(field, True),
                    "DECLARATION_ARTIFACT_NON_CLAIM_NOT_FALSE",
                )

    def test_26_declaration_validation_summary_nonclaims_and_omission(
        self,
    ) -> None:
        candidate_validation = "prepared_candidate_validation"
        for field in (
            "exact_21_field_candidate_validated",
            "candidate_received_from_selected_preparation_artifact",
            "candidate_references_validated",
            "evaluator_reference_validated",
            "candidate_posture_maps_validated",
            "non_conversion_statement_validated",
            "basis_non_claims_validated",
            "complete_source_material_omitted",
        ):
            with self.subTest(section=candidate_validation, field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, field=field: artifact[
                        candidate_validation
                    ].__setitem__(field, False),
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )
        for section, field in (
            ("specification_marker_validation", "specification_markers_validated"),
            (
                "selected_preparation_artifact_validation",
                "preparation_artifact_validated",
            ),
        ):
            with self.subTest(section=section, field=field):
                self.assert_artifact_mutation_blocks(
                    lambda artifact, section=section, field=field: artifact[
                        section
                    ].__setitem__(field, False),
                    "DECLARATION_ARTIFACT_POSTURE_INVALID",
                )
        first_nonclaim = resolver.UPSTREAM_DECLARATION_FALSE_NON_CLAIMS[0]
        for name, mutator in (
            (
                "nonclaim_missing",
                lambda artifact: artifact["non_claims"].pop(first_nonclaim),
            ),
            (
                "nonclaim_extra",
                lambda artifact: artifact["non_claims"].__setitem__(
                    "unknown",
                    False,
                ),
            ),
            (
                "nonclaim_true",
                lambda artifact: artifact["non_claims"].__setitem__(
                    first_nonclaim,
                    True,
                ),
            ),
            (
                "omission_missing",
                lambda artifact: artifact["omission_posture"].pop(
                    resolver.UPSTREAM_DECLARATION_OMISSION_FIELDS[0]
                ),
            ),
            (
                "omission_false",
                lambda artifact: artifact["omission_posture"].__setitem__(
                    resolver.UPSTREAM_DECLARATION_OMISSION_FIELDS[0],
                    False,
                ),
            ),
        ):
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(
                    mutator,
                    (
                        "DECLARATION_ARTIFACT_NON_CLAIM_NOT_FALSE"
                        if name.startswith("nonclaim")
                        else "DECLARATION_ARTIFACT_OMISSION_INVALID"
                    ),
                )

    def test_27_declared_basis_schema_references_and_evaluator_are_exact(
        self,
    ) -> None:
        basis_key = "declared_receiver_attestation_operation_basis"
        first = resolver.CANDIDATE_FIELDS[0]
        cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None], str],
            ...,
        ] = (
            (
                "missing_basis",
                lambda artifact: artifact.pop(basis_key),
                "DECLARED_BASIS_MISSING",
            ),
            (
                "basis_list",
                lambda artifact: artifact.__setitem__(basis_key, []),
                "DECLARED_BASIS_MISSING",
            ),
            (
                "missing_field",
                lambda artifact: artifact[basis_key].pop(first),
                "DECLARED_BASIS_SCHEMA_MISMATCH",
            ),
            (
                "extra_field",
                lambda artifact: artifact[basis_key].__setitem__(
                    "unknown",
                    False,
                ),
                "DECLARED_BASIS_SCHEMA_MISMATCH",
            ),
            (
                "reference",
                lambda artifact: artifact[basis_key].__setitem__(
                    "expected_archive_sha256",
                    "0" * 64,
                ),
                "DECLARED_BASIS_REFERENCE_MISMATCH",
            ),
            (
                "evaluator",
                lambda artifact: artifact[basis_key].__setitem__(
                    "evaluator_reference",
                    "wrong",
                ),
                "DECLARED_BASIS_EVALUATOR_REFERENCE_MISMATCH",
            ),
        )
        for name, mutator, code in cases:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutator, code)

    def test_28_declared_basis_posture_maps_are_exact(self) -> None:
        basis_key = "declared_receiver_attestation_operation_basis"
        expected_maps = {
            "trace_integrity_postures": resolver.EXPECTED_TRACE_INTEGRITY_POSTURES,
            "ambiguity_postures": resolver.EXPECTED_AMBIGUITY_POSTURES,
            "contradiction_postures": (
                resolver.EXPECTED_CONTRADICTION_POSTURES
            ),
            "unresolved_postures": resolver.EXPECTED_UNRESOLVED_POSTURES,
        }
        for map_name, expected in expected_maps.items():
            first = next(iter(expected))
            flipped = not expected[first]
            cases = (
                (
                    "missing",
                    lambda artifact, map_name=map_name, first=first: artifact[
                        basis_key
                    ][map_name].pop(first),
                ),
                (
                    "extra",
                    lambda artifact, map_name=map_name: artifact[basis_key][
                        map_name
                    ].__setitem__("unknown", False),
                ),
                (
                    "flipped",
                    lambda artifact, map_name=map_name, first=first, flipped=flipped: artifact[
                        basis_key
                    ][map_name].__setitem__(first, flipped),
                ),
                (
                    "integer",
                    lambda artifact, map_name=map_name, first=first: artifact[
                        basis_key
                    ][map_name].__setitem__(first, 1),
                ),
            )
            for case_name, mutator in cases:
                with self.subTest(map=map_name, case=case_name):
                    self.assert_artifact_mutation_blocks(
                        mutator,
                        "DECLARED_BASIS_POSTURE_MISMATCH",
                    )

    def test_29_non_conversion_and_basis_nonclaims_are_exact(self) -> None:
        basis_key = "declared_receiver_attestation_operation_basis"
        first = resolver.REQUIRED_BASIS_NON_CLAIMS[0]
        cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None], str],
            ...,
        ] = (
            (
                "nonconversion",
                lambda artifact: artifact[basis_key].__setitem__(
                    "non_conversion_statement",
                    resolver.NON_CONVERSION_STATEMENT + " ",
                ),
                "DECLARED_BASIS_NON_CONVERSION_MISMATCH",
            ),
            (
                "nonclaim_missing",
                lambda artifact: artifact[basis_key]["basis_non_claims"].pop(
                    first
                ),
                "DECLARED_BASIS_NON_CLAIM_MISMATCH",
            ),
            (
                "nonclaim_extra",
                lambda artifact: artifact[basis_key][
                    "basis_non_claims"
                ].__setitem__("unknown", False),
                "DECLARED_BASIS_NON_CLAIM_MISMATCH",
            ),
            (
                "nonclaim_true",
                lambda artifact: artifact[basis_key][
                    "basis_non_claims"
                ].__setitem__(first, True),
                "DECLARED_BASIS_NON_CLAIM_MISMATCH",
            ),
            (
                "nonclaim_zero",
                lambda artifact: artifact[basis_key][
                    "basis_non_claims"
                ].__setitem__(first, 0),
                "DECLARED_BASIS_NON_CLAIM_MISMATCH",
            ),
        )
        for name, mutator, code in cases:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutator, code)

    def test_30_declaration_digest_metadata_and_fixed_digest_are_exact(
        self,
    ) -> None:
        digest_key = "candidate_digest"
        cases: tuple[
            tuple[str, Callable[[dict[str, Any]], None], str],
            ...,
        ] = (
            (
                "algorithm",
                lambda artifact: artifact[digest_key].__setitem__(
                    "candidate_digest_algorithm",
                    "MD5",
                ),
                "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
            ),
            (
                "sha",
                lambda artifact: artifact[digest_key].__setitem__(
                    "candidate_sha256",
                    "0" * 64,
                ),
                "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
            ),
            (
                "caller_digest",
                lambda artifact: artifact[digest_key].__setitem__(
                    "caller_supplied_digest_used",
                    True,
                ),
                "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
            ),
            (
                "correspondence",
                lambda artifact: artifact[digest_key].__setitem__(
                    "digest_is_correspondence_only",
                    False,
                ),
                "DECLARED_BASIS_DIGEST_METADATA_MISMATCH",
            ),
            (
                "basis_changed",
                lambda artifact: artifact[
                    "declared_receiver_attestation_operation_basis"
                ].__setitem__(
                    "non_conversion_statement",
                    resolver.NON_CONVERSION_STATEMENT + " ",
                ),
                "DECLARED_BASIS_NON_CONVERSION_MISMATCH",
            ),
        )
        for name, mutator, code in cases:
            with self.subTest(case=name):
                self.assert_artifact_mutation_blocks(mutator, code)

        def change_basis_and_digest(artifact: dict[str, Any]) -> None:
            artifact["declared_receiver_attestation_operation_basis"][
                "expected_archive_sha256"
            ] = "0" * 64
            changed = artifact[
                "declared_receiver_attestation_operation_basis"
            ]
            candidate_sha = hashlib.sha256(
                json.dumps(
                    changed,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            artifact["candidate_digest"]["candidate_sha256"] = candidate_sha
            artifact["prepared_candidate_validation"][
                "candidate_sha256"
            ] = candidate_sha
            artifact[f"{resolver.DECLARATION_PREFIX}_summary"][
                "candidate_sha256"
            ] = candidate_sha
            artifact[resolver.DECLARATION_PREFIX][
                "candidate_sha256"
            ] = candidate_sha

        self.assert_artifact_mutation_blocks(
            change_basis_and_digest,
            "DECLARATION_ARTIFACT_POSTURE_INVALID",
        )

    def test_31_stale_entries_do_not_mask_structural_corruption(self) -> None:
        with self.isolated_inputs() as (_, _, artifact_path):
            artifact = self._load_strict_json(artifact_path)
            artifact["what_remains_open"].append("another stale note")
            self._write_json(artifact_path, artifact)
            self.assert_supplied(self.invoke(self.canonical_request()))
        with self.isolated_inputs() as (_, _, artifact_path):
            artifact = self._load_strict_json(artifact_path)
            self.assertIn(
                "declaration test",
                artifact["what_remains_open"],
            )
            artifact["resolver_module"] = "wrong"
            self._write_json(artifact_path, artifact)
            self.assert_blocked(
                self.invoke(self.canonical_request()),
                "DECLARATION_ARTIFACT_METADATA_MISMATCH",
            )

    def test_32_result_structure_is_exact_for_every_branch(self) -> None:
        supplied = self.invoke(self.canonical_request())
        not_supplied = self.invoke(self.canonical_request(selected=False))
        blocked_request = self.canonical_request()
        blocked_request["unknown"] = True
        blocked = self.invoke(blocked_request)
        for name, result in (
            ("supplied", supplied),
            ("not_supplied", not_supplied),
            ("blocked", blocked),
        ):
            with self.subTest(branch=name):
                expected = set(resolver.RESULT_BASE_SECTIONS)
                if name == "supplied":
                    expected.add(resolver.SUPPLIED_BASIS_SECTION)
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
        self.assert_supplied(supplied)
        self.assert_not_supplied(not_supplied)
        self.assert_blocked(blocked, "REQUEST_FIELD_UNKNOWN")

    def test_33_from_path_contract_and_strict_json(self) -> None:
        request = self.canonical_request()
        request_path = self._write_json(
            self.root / "requests" / "supplied.json",
            request,
        )
        before = request_path.read_bytes()
        direct = self.invoke(request)
        from_path = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
            request_path
        )
        self.assertEqual(from_path, direct)
        self.assertEqual(request_path.read_bytes(), before)

        duplicate = self._write_text(
            self.root / "requests" / "duplicate.json",
            '{"supply_id":"a","supply_id":"b"}',
        )
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
                duplicate
            ),
            "REQUEST_PATH_NOT_PARSEABLE",
        )
        malformed = self._write_text(
            self.root / "requests" / "malformed.json",
            "{",
        )
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
                malformed
            ),
            "REQUEST_PATH_NOT_PARSEABLE",
        )
        array = self._write_text(
            self.root / "requests" / "array.json",
            "[]\n",
        )
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
                array
            ),
            "REQUEST_NOT_MAPPING",
        )
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
                self.root / "requests" / "missing.json"
            ),
            "REQUEST_PATH_NOT_AVAILABLE",
        )
        directory = self.root / "requests" / "directory"
        directory.mkdir()
        self.assert_blocked(
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_from_path(
                directory
            ),
            "REQUEST_PATH_NOT_AVAILABLE",
        )

    def test_34_resolution_summary_and_input_are_deterministic(self) -> None:
        supplied_request = self.canonical_request()
        supplied_before = copy.deepcopy(supplied_request)
        supplied_first = self.invoke(supplied_request)
        supplied_second = self.invoke(supplied_request)
        self.assertEqual(supplied_first, supplied_second)
        self.assertEqual(supplied_request, supplied_before)

        not_request = self.canonical_request(selected=False)
        not_before = copy.deepcopy(not_request)
        not_first = self.invoke(not_request)
        not_second = self.invoke(not_request)
        self.assertEqual(not_first, not_second)
        self.assertEqual(not_request, not_before)

        blocked_request = self.canonical_request()
        blocked_request["unknown"] = {"visible": True}
        blocked_before = copy.deepcopy(blocked_request)
        blocked_first = self.invoke(blocked_request)
        blocked_second = self.invoke(blocked_request)
        self.assertEqual(blocked_first, blocked_second)
        self.assertEqual(blocked_request, blocked_before)

        supplied_first["supply_decision"]["reason"] = "mutated"
        supplied_first[resolver.SUPPLIED_BASIS_SECTION][
            "basis_non_claims"
        ]["identity_created"] = True
        self.assertNotEqual(supplied_first, supplied_second)
        self.assertEqual(
            self.invoke(supplied_request),
            supplied_second,
        )

        summary_one = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
                supplied_second
            )
        )
        summary_two = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
                supplied_second
            )
        )
        self.assertEqual(summary_one, summary_two)
        summary_one["decision_reason"] = "mutated"
        self.assertNotEqual(summary_one, summary_two)
        self.assertEqual(
            supplied_second[SUMMARY_KEY],
            summary_two,
        )

    def test_35_summary_builder_reports_compact_exact_posture(self) -> None:
        results = (
            self.invoke(self.canonical_request()),
            self.invoke(self.canonical_request(selected=False)),
            self.invoke({"unknown": True}),
        )
        required_keys = {
            "resolver_module",
            "result_version",
            "supply_id",
            "supply_type",
            "supply_version",
            "supply_scope",
            "selected_declaration_id",
            "selected_preparation_id",
            "selected_preparation_request_id",
            "selected_operation_id",
            "selected_candidate_id",
            "governing_specification_path",
            "selected_declaration_artifact_path",
            "outcome",
            "supply_result",
            "failed_check_count",
            "passed_check_count",
            "blocked",
            "decision_code",
            "decision_reason",
            "basis_supply_selected",
            "specification_markers_validated",
            "declaration_artifact_validated",
            "stale_open_list_entries_disclosed",
            "stale_open_list_entries_preserved",
            "stale_open_list_entries_not_used_as_sole_block",
            "exact_21_field_declared_basis_validated",
            "declared_basis_digest_algorithm",
            "declared_basis_sha256",
            "declared_basis_digest_correspondence_validated",
            "declared_basis_posture_maps_validated",
            "non_conversion_statement_validated",
            "basis_non_claims_validated",
            "supply_recorded",
            "supply_result_recorded",
            "supply_exhausted",
            "supply_basis_received",
            "operation_basis_declared",
            "operation_basis_supplied",
            "operation_basis_admitted",
            "operation_executed",
            "operation_result_recorded",
            "result_level_non_claims_canonical_false",
            "complete_material_omitted",
        }
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                summary = (
                    resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(summary, result[SUMMARY_KEY])
                self.assertEqual(set(summary), required_keys)
                self.assertNotIn(
                    resolver.SUPPLIED_BASIS_SECTION,
                    summary,
                )
                self.assertIs(
                    summary["operation_basis_admitted"],
                    False,
                )
                self.assertIs(summary["operation_executed"], False)
                self.assertIs(summary["operation_result_recorded"], False)
                self.assertIs(
                    summary["result_level_non_claims_canonical_false"],
                    True,
                )
                self.assertIs(summary["complete_material_omitted"], True)
        with self.assertRaises(
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError
        ):
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_summary(
                []
            )

    def test_36_writer_writes_every_valid_branch_exactly(self) -> None:
        results = (
            ("supplied", self.invoke(self.canonical_request())),
            (
                "not_supplied",
                self.invoke(self.canonical_request(selected=False)),
            ),
            ("blocked", self.invoke({"unknown": True})),
        )
        for name, result in results:
            with self.subTest(branch=name):
                output = self.root / "writer" / name / "result.json"
                written = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                    result,
                    output,
                )
                self.assertEqual(written, output)
                self.assertTrue(output.is_file())
                text = output.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"))
                self.assertFalse(text.endswith("\n\n"))
                self.assertEqual(
                    text,
                    json.dumps(
                        result,
                        indent=2,
                        sort_keys=True,
                        ensure_ascii=True,
                        allow_nan=False,
                    )
                    + "\n",
                )
                self.assertEqual(json.loads(text), result)
        self.assertFalse(resolver.OUTPUT_ROOT.exists())

    def test_37_writer_never_overwrites_and_uses_stable_suffix(self) -> None:
        result = self.invoke(self.canonical_request())
        with patch.object(resolver, "OUTPUT_ROOT", self.root / OUTPUT_RELATIVE_ROOT):
            first = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                result
            )
            first_before = first.read_bytes()
            second = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                result
            )
            third = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                result
            )
        self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
        expected_stem = Path(resolver.OUTPUT_FILENAME).stem
        self.assertEqual(
            second.name,
            f"{expected_stem}_001.json",
        )
        self.assertEqual(
            third.name,
            f"{expected_stem}_002.json",
        )
        self.assertEqual(first.read_bytes(), first_before)
        self.assertNotEqual(first, second)
        self.assertNotEqual(second, third)

        unrelated = self._write_text(
            self.root / "unrelated.txt",
            "unchanged",
        )
        explicit = self.root / "existing" / "result.json"
        explicit.parent.mkdir(parents=True)
        explicit.write_text("existing", encoding="utf-8")
        written = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
            result,
            explicit,
        )
        self.assertEqual(explicit.read_text(encoding="utf-8"), "existing")
        self.assertEqual(written.name, "result_001.json")
        self.assertEqual(unrelated.read_text(encoding="utf-8"), "unchanged")

    def test_38_writer_refuses_branch_and_wrapper_inconsistency(self) -> None:
        supplied = self.invoke(self.canonical_request())
        not_supplied = self.invoke(self.canonical_request(selected=False))
        blocked = self.invoke({"unknown": True})
        cases: list[tuple[str, Any]] = [
            ("non_mapping", []),
        ]
        wrong_module = copy.deepcopy(supplied)
        wrong_module["resolver_module"] = "wrong"
        cases.append(("module", wrong_module))
        wrong_version = copy.deepcopy(supplied)
        wrong_version["result_version"] = "9.9.9"
        cases.append(("version", wrong_version))
        wrong_outcome = copy.deepcopy(supplied)
        wrong_outcome["outcome"] = resolver.OUTCOME_NOT_SUPPLIED
        cases.append(("outcome", wrong_outcome))
        missing_basis = copy.deepcopy(supplied)
        missing_basis.pop(resolver.SUPPLIED_BASIS_SECTION)
        cases.append(("supplied_missing_basis", missing_basis))
        not_with_basis = copy.deepcopy(not_supplied)
        not_with_basis[resolver.SUPPLIED_BASIS_SECTION] = self.declared_basis()
        cases.append(("not_with_basis", not_with_basis))
        blocked_with_basis = copy.deepcopy(blocked)
        blocked_with_basis[resolver.SUPPLIED_BASIS_SECTION] = (
            self.declared_basis()
        )
        cases.append(("blocked_with_basis", blocked_with_basis))
        for field in (
            "receiver_attestation_operation_basis_admitted",
            "receiver_attestation_operation_executed",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_recorded",
        ):
            mutated = copy.deepcopy(supplied)
            mutated[STATE_KEY][field] = True
            cases.append((field, mutated))
        stale = copy.deepcopy(supplied)
        stale["declaration_artifact_stale_open_list_validation"][
            "declaration_artifact_stale_open_list_repaired"
        ] = True
        cases.append(("stale_repair", stale))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_39_writer_refuses_basis_digest_and_posture_corruption(
        self,
    ) -> None:
        supplied = self.invoke(self.canonical_request())
        cases: list[tuple[str, dict[str, Any]]] = []
        altered_basis = copy.deepcopy(supplied)
        altered_basis[resolver.SUPPLIED_BASIS_SECTION][
            "expected_archive_sha256"
        ] = "0" * 64
        cases.append(("altered_basis", altered_basis))
        digest = copy.deepcopy(supplied)
        digest["declared_basis_digest"][
            "declared_basis_sha256"
        ] = "0" * 64
        cases.append(("digest", digest))
        algorithm = copy.deepcopy(supplied)
        algorithm["declared_basis_digest"][
            "declared_basis_digest_algorithm"
        ] = "MD5"
        cases.append(("algorithm", algorithm))
        posture = copy.deepcopy(supplied)
        posture[resolver.SUPPLIED_BASIS_SECTION][
            "trace_integrity_postures"
        ]["archive_correspondence_claimed"] = False
        cases.append(("posture", posture))
        nonconversion = copy.deepcopy(supplied)
        nonconversion[resolver.SUPPLIED_BASIS_SECTION][
            "non_conversion_statement"
        ] += " "
        cases.append(("nonconversion", nonconversion))
        basis_nonclaims = copy.deepcopy(supplied)
        basis_nonclaims[resolver.SUPPLIED_BASIS_SECTION][
            "basis_non_claims"
        ]["identity_created"] = True
        cases.append(("basis_nonclaims", basis_nonclaims))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_40_writer_refuses_nonclaims_omission_and_embedded_material(
        self,
    ) -> None:
        supplied = self.invoke(self.canonical_request())
        first_nonclaim = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        first_omission = resolver.RESULT_OMISSION_FIELDS[0]
        cases: list[tuple[str, dict[str, Any]]] = []
        missing_nonclaim = copy.deepcopy(supplied)
        missing_nonclaim["non_claims"].pop(first_nonclaim)
        cases.append(("missing_nonclaim", missing_nonclaim))
        flipped_nonclaim = copy.deepcopy(supplied)
        flipped_nonclaim["non_claims"][first_nonclaim] = True
        cases.append(("flipped_nonclaim", flipped_nonclaim))
        missing_omission = copy.deepcopy(supplied)
        missing_omission["omission_posture"].pop(first_omission)
        cases.append(("missing_omission", missing_omission))
        false_omission = copy.deepcopy(supplied)
        false_omission["omission_posture"][first_omission] = False
        cases.append(("false_omission", false_omission))
        for key, value in (
            ("complete_declaration_artifact", {"secret": True}),
            ("archive_bytes", b"archive"),
            ("text_component_bodies", "body"),
            ("recorded_signal_body", {"signal": True}),
            ("raw_source_body", "source body"),
        ):
            embedded = copy.deepcopy(supplied)
            embedded[key] = value
            cases.append((key, embedded))
        for name, value in cases:
            with self.subTest(case=name):
                self.assert_writer_refused(value, name)

    def test_41_writer_refuses_every_protected_path_family(self) -> None:
        with self.isolated_inputs() as (isolated_root, _, artifact_path):
            result = self.invoke(self.canonical_request())
            paths = (
                isolated_root / SPECIFICATION_RELATIVE_PATH,
                isolated_root / SOURCE_RELATIVE_PATH,
                isolated_root / TEST_RELATIVE_PATH,
                isolated_root / "reference/IAMMAI/must_not_write.json",
                artifact_path,
                isolated_root
                / resolver.SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH,
                isolated_root
                / resolver.SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
                isolated_root
                / resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH,
                isolated_root
                / resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
                isolated_root
                / resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
                isolated_root
                / resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
                / "must_not_write.json",
            )

            def posture(path: Path) -> tuple[bool, bool, bytes | None]:
                if not path.exists():
                    return False, False, None
                return (
                    True,
                    path.is_file(),
                    path.read_bytes() if path.is_file() else None,
                )

            before = {path: posture(path) for path in paths}
            for path in paths:
                with self.subTest(path=str(path)):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisSupplyV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min_result(
                            result,
                            path,
                        )
            after = {path: posture(path) for path in paths}
            self.assertEqual(after, before)

    def test_42_non_meaning_blocked_routes_and_open_posture(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_supplied(result)
        non_meaning = result[NON_MEANING_KEY]
        expected_non_meaning = (
            "supply_does_not_repeat_declaration",
            "supply_does_not_reread_capture_material",
            "supply_does_not_recompute_archive_correspondence",
            "supply_does_not_independently_verify_occurrence",
            "supply_does_not_admit_basis",
            "supply_does_not_satisfy_admission_gate",
            "supply_does_not_execute_operation",
            "supply_does_not_record_operation_result",
            "supply_does_not_record_receiver_attestation",
            "supply_does_not_create_receipt_or_presence",
            "supply_does_not_repair_stale_open_list",
            "supply_exhaustion_does_not_authorize_admission",
            "declared_basis_digest_is_correspondence_only",
        )
        self.assertEqual(set(non_meaning), set(expected_non_meaning))
        for field in expected_non_meaning:
            self.assertIs(non_meaning[field], True)
        self.assertEqual(
            result["blocked_routes"],
            list(resolver.BLOCKED_ROUTES),
        )
        self.assertTrue(
            {
                "declared basis directly to admitted basis",
                "basis supply directly to admission-gate success",
                "basis supply directly to operation execution",
                "basis supply directly to operation result",
                "basis supply directly to receiver-attestation recording",
                "supplied basis directly to receiver-answerable receipt or presence",
            }.issubset(result["blocked_routes"])
        )
        self.assertEqual(
            result["what_remains_open"],
            list(resolver.WHAT_REMAINS_OPEN),
        )
        for item in (
            "supply tests",
            "supply live artifact",
            "basis admission",
            "receiver-attestation operation execution",
            "receiver-attestation operation result",
            "receiver attestation",
            "receiver-answerable receipt",
            "presence re-evaluation",
            "identity",
            "custody",
            "provenance",
            "physical validity",
            "authority",
            "truth",
            "standing",
            "relation",
            "coupling",
            "FIELD machinery",
            "runtime",
            "API",
            "output",
            "action",
            "synchronization",
            "repair",
            "validation",
            "follow-on work",
        ):
            self.assertIn(item, result["what_remains_open"])
        self.assertNotIn("supply resolver", result["what_remains_open"])

    def test_43_resolver_reads_only_specification_and_declaration_artifact(
        self,
    ) -> None:
        original = resolver._read_text
        reads: list[Path] = []

        def tracked(path: Path | str) -> tuple[str | None, str | None]:
            reads.append(Path(path).resolve())
            return original(path)

        with patch.object(resolver, "_read_text", side_effect=tracked):
            self.assert_supplied(self.invoke(self.canonical_request()))
        self.assertEqual(
            reads,
            [
                resolver.GOVERNING_SPECIFICATION_PATH.resolve(),
                resolver.SELECTED_DECLARATION_ARTIFACT_PATH.resolve(),
            ],
        )
        forbidden = (
            resolver.SELECTED_PREPARATION_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_PREPARATION_REQUEST_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_WAITING_OPERATION_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
            resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH,
        )
        self.assertTrue(
            all((REPOSITORY_ROOT / path).resolve() not in reads for path in forbidden)
        )

    def test_44_preserved_inputs_and_no_repository_artifact_stay_unchanged(
        self,
    ) -> None:
        before = {
            relative: self._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        self.assert_supplied(self.invoke(self.canonical_request()))
        after = {
            relative: self._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_RELATIVE_PATHS
        }
        self.assertEqual(after, before)
        self.assertFalse(resolver.OUTPUT_ROOT.exists())

    def test_45_public_codes_and_global_state_are_stable(self) -> None:
        canonical = self.canonical_request()
        baseline = self.invoke(canonical)
        self.assert_supplied(baseline)
        for field, expected_code in resolver.PROHIBITED_INPUT_FLAGS.items():
            with self.subTest(field=field):
                request = self.canonical_request()
                request[field] = True
                result = self.invoke(request)
                self.assert_blocked(result, expected_code)
        self.assertEqual(self.invoke(canonical), baseline)
        self.assert_all_emitted_codes_public(baseline)


if __name__ == "__main__":
    unittest.main()
