"""Tests for one bounded receiver-attestation basis preparation request.

The suite validates request recording without performing preparation. Exact
copies of the governing specification and waiting artifact are mutated only
inside temporary directories; repository lineage remains read-only.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

import resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min as resolver


PREFIX = resolver.PREFIX
STATE_KEY = PREFIX
CHECKS_KEY = f"{PREFIX}_checks"
SUMMARY_KEY = f"{PREFIX}_summary"
METADATA_KEY = f"{PREFIX}_metadata"
DECLARED_KEY = f"declared_{PREFIX}"

OPERATION_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation"
)
OPERATION_SUMMARY_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation_summary"
)

PRESERVED_PATHS = (
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "BASIS_DECLARATION_PREPARATION_REQUEST_V0_MIN_SPEC.md"
    ),
    Path(
        "src/resolve_receiver_side_answerable_basis_receiver_attestation_"
        "operation_basis_declaration_preparation_request_v0_min.py"
    ),
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
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_"
        "V0_MIN_WAITING_TERMINAL_SUMMARY.md"
    ),
    resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH,
    Path(
        "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY_"
        "V0_MIN_V2_TERMINAL_SUMMARY.md"
    ),
    resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
)

NON_CONVERSION_FALSE_FIELDS = tuple(
    dict.fromkeys(
        (
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
            *resolver.REQUIRED_FALSE_NON_CLAIMS,
        )
    )
)

OMISSION_FIELDS = (
    "complete_waiting_artifact_omitted",
    "complete_upstream_boundary_artifact_omitted",
    "complete_candidate_sufficiency_artifact_omitted",
    "complete_candidate_sufficiency_basis_omitted",
    "complete_operation_basis_omitted",
    "archive_bytes_omitted",
    "text_component_bodies_omitted",
    "recorded_signal_body_omitted",
)

_MISSING = object()


class ReceiverAttestationOperationBasisDeclarationPreparationRequestTests(
    unittest.TestCase
):
    """Exercise exact request, upstream, branch, summary, and writer locks."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_hashes = {
            str(path): cls._sha256(REPOSITORY_ROOT / path)
            for path in PRESERVED_PATHS
        }

    @classmethod
    def tearDownClass(cls) -> None:
        current = {
            str(path): cls._sha256(REPOSITORY_ROOT / path)
            for path in PRESERVED_PATHS
        }
        if current != cls.preserved_hashes:
            raise AssertionError(
                "governing preparation-request lineage changed during tests"
            )

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    @staticmethod
    def _clone(value: Any) -> Any:
        return copy.deepcopy(value)

    def _write_json(self, path: Path, value: Any) -> Path:
        self.assertFalse(
            path.is_dir(),
            "fixture path collision: JSON target is an existing directory",
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                value,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n",
            encoding="utf-8",
        )
        return path

    def _write_text(self, path: Path, value: str) -> Path:
        self.assertFalse(
            path.is_dir(),
            "fixture path collision: text target is an existing directory",
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
        return path

    def _copy_fixture(self, root: Path, relative: Path) -> Path:
        source = REPOSITORY_ROOT / relative
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return target

    def fixture_root(self, root: Path) -> None:
        self._copy_fixture(
            root,
            resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
        )
        self._copy_fixture(
            root,
            resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH,
        )

    def canonical_request(
        self,
        *,
        selected: bool = True,
        **overrides: Any,
    ) -> dict[str, Any]:
        return resolver.build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request(
            basis_declaration_preparation_selected=selected,
            **overrides,
        )

    def invoke(
        self,
        request: Any = None,
        *,
        root: Path | None = None,
    ) -> dict[str, Any]:
        if root is None:
            return resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min(
                request
            )
        with patch.object(resolver, "REPO_ROOT", root):
            return resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min(
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
            for key in ("failure_code", "block_code"):
                if check.get(key) is not None:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

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
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIs(type(non_claims[key]), bool)
                self.assertIs(non_claims[key], False)
                self.assertIs(type(state[key]), bool)
                self.assertIs(state[key], False)

    def assert_non_conversion_false(
        self,
        result: Mapping[str, Any],
    ) -> None:
        state = self.state(result)
        for key in NON_CONVERSION_FALSE_FIELDS:
            with self.subTest(non_conversion_field=key):
                self.assertIn(key, state)
                self.assertIs(type(state[key]), bool)
                self.assertIs(state[key], False)
        for key in OMISSION_FIELDS:
            self.assertIs(state.get(key), True)
        self.assert_canonical_false_non_claims(result)

    def assert_material_omitted(
        self,
        result: Mapping[str, Any],
    ) -> None:
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
        state = self.state(result)
        for field in OMISSION_FIELDS:
            self.assertIs(state[field], True)

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
        state = self.state(result)
        self.assertEqual(
            state.get("request_result"),
            resolver.REQUEST_RESULT_NOT_EVALUATED,
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
        self.assertIs(state.get("preparation_request_recorded"), False)
        self.assertIs(
            state.get("preparation_request_result_recorded"),
            False,
        )
        self.assertIs(state.get("preparation_request_exhausted"), False)
        self.assertIs(
            state.get("basis_declaration_preparation_requested"),
            False,
        )
        self.assert_non_conversion_false(result)
        self.assert_all_emitted_codes_public(result)

    def assert_recorded(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(result.get("resolver_module"), resolver.RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), resolver.RESULT_VERSION)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("request_result"),
            resolver.REQUEST_RESULT_RECORDED,
        )
        self.assertIs(state.get("basis_declaration_preparation_selected"), True)
        self.assertIs(state.get("preparation_request_recorded"), True)
        self.assertIs(
            state.get("preparation_request_result_recorded"),
            True,
        )
        self.assertIs(state.get("preparation_request_exhausted"), True)
        self.assertIs(
            state.get("basis_declaration_preparation_requested"),
            True,
        )
        self.assert_non_conversion_false(result)
        self.assert_material_omitted(result)

    def assert_not_recorded(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_RECORDED)
        self.assert_not_blocked(result)
        state = self.state(result)
        self.assertEqual(
            state.get("request_result"),
            resolver.REQUEST_RESULT_NOT_RECORDED,
        )
        self.assertIs(
            state.get("basis_declaration_preparation_selected"),
            False,
        )
        self.assertIs(state.get("preparation_request_recorded"), False)
        self.assertIs(
            state.get("preparation_request_result_recorded"),
            True,
        )
        self.assertIs(state.get("preparation_request_exhausted"), True)
        self.assertIs(
            state.get("basis_declaration_preparation_requested"),
            False,
        )
        self.assert_non_conversion_false(result)
        self.assert_material_omitted(result)

    @staticmethod
    def _set_path(
        value: dict[str, Any],
        path: tuple[str, ...],
        replacement: Any,
    ) -> None:
        current = value
        for key in path[:-1]:
            nested = current[key]
            if not isinstance(nested, dict):
                raise AssertionError(f"non-mapping fixture path: {path!r}")
            current = nested
        if replacement is _MISSING:
            current.pop(path[-1], None)
        else:
            current[path[-1]] = replacement

    def _resolve_waiting_variant(
        self,
        root: Path,
        artifact: Any,
    ) -> dict[str, Any]:
        self._write_json(
            root / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH,
            artifact,
        )
        return self.invoke(self.canonical_request(), root=root)

    def _assert_summary_contract(
        self,
        result: Mapping[str, Any],
        *,
        outcome: str,
        request_result: str,
        selected: bool,
        blocked: bool,
    ) -> None:
        summary = resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_summary(
            result
        )
        self.assertEqual(summary, self.summary(result))
        expected = {
            "resolver_module": resolver.RESOLVER_MODULE,
            "result_version": resolver.RESULT_VERSION,
            "preparation_request_id": resolver.PREPARATION_REQUEST_ID,
            "preparation_request_type": resolver.PREPARATION_REQUEST_TYPE,
            "preparation_request_version": resolver.PREPARATION_REQUEST_VERSION,
            "preparation_request_scope": resolver.PREPARATION_REQUEST_SCOPE,
            "selected_operation_id": resolver.OPERATION_ID,
            "selected_candidate_id": resolver.CANDIDATE_ID,
            "selected_waiting_artifact_path": str(
                resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
            ),
            "outcome": outcome,
            "request_result": request_result,
            "blocked": blocked,
            "request_selection": selected,
        }
        for key, value in expected.items():
            self.assertEqual(summary.get(key), value)
        self.assertEqual(
            summary.get("failed_check_count"),
            result.get("failed_check_count"),
        )
        self.assertEqual(
            summary.get("passed_check_count"),
            result.get("passed_check_count"),
        )
        self.assertIs(
            summary.get("result_level_non_claims_canonical_false"),
            True,
        )
        for key in (
            "requested_21_field_schema_validated",
            "bounded_future_references_validated",
            "posture_key_families_validated",
            "non_conversion_statement_validated",
        ):
            self.assertIs(summary.get(key), True)
        self.assertIs(
            summary.get("specification_markers_validated"),
            None if blocked else True,
        )
        self.assertIs(
            summary.get("waiting_artifact_validated"),
            None if blocked else True,
        )
        branch_posture = {
            resolver.OUTCOME_RECORDED: (True, True, True, True),
            resolver.OUTCOME_NOT_RECORDED: (False, True, True, False),
            resolver.OUTCOME_BLOCKED: (False, False, False, False),
        }[outcome]
        for key, value in zip(
            (
                "preparation_request_recorded",
                "preparation_request_result_recorded",
                "preparation_request_exhausted",
                "basis_declaration_preparation_requested",
            ),
            branch_posture,
        ):
            self.assertIs(summary.get(key), value)
        for key in (
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
        ):
            self.assertIs(summary.get(key), False)
        self.assertIs(summary.get("complete_material_omitted"), True)
        self.assertEqual(
            summary.get("governing_paths"),
            {
                "governing_preparation_request_specification_path": str(
                    resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
                ),
                "selected_waiting_operation_artifact_path": str(
                    resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
                ),
            },
        )

    def test_01_public_api_and_constant_contract(self) -> None:
        public = (
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request,
            resolver.build_declared_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request,
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min,
            resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path,
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_summary,
            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result,
            resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError,
        )
        for value in public:
            self.assertTrue(callable(value))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_receiver_attestation_"
            "operation_basis_declaration_preparation_request_v0_min",
        )
        self.assertEqual(len(resolver.REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES), 21)
        self.assertEqual(len(set(resolver.REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES)), 21)
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_BLOCKED,
            },
        )
        self.assertEqual(
            set(resolver.REQUEST_RESULT_FAMILY),
            {
                resolver.REQUEST_RESULT_RECORDED,
                resolver.REQUEST_RESULT_NOT_RECORDED,
                resolver.REQUEST_RESULT_NOT_EVALUATED,
            },
        )
        self.assertTrue(set(resolver.PROHIBITED_REQUEST_FLAGS))
        self.assertTrue(set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(
            set(resolver.SPECIFICATION_SECTION_12_FALSE_NON_CLAIMS).issubset(
                resolver.REQUIRED_FALSE_NON_CLAIMS
            )
        )
        self.assertTrue(set(resolver.BLOCK_CODES))

    def test_02_canonical_builders_are_exact_and_independent(self) -> None:
        first = resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_request()
        second = self.canonical_request()
        third = self.canonical_request()
        self.assertEqual(first, second)
        self.assertEqual(second, third)
        self.assertIsNot(second, third)
        self.assertEqual(set(second), resolver._request_allowed_keys())
        self.assertEqual(
            tuple(second["requested_declaration_candidate_field_names"]),
            resolver.REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES,
        )
        self.assertEqual(
            second["bounded_future_references"],
            dict(resolver.BOUNDED_FUTURE_REFERENCES),
        )
        self.assertEqual(
            second["requested_posture_key_families"],
            {
                key: list(value)
                for key, value in resolver.REQUESTED_POSTURE_KEY_FAMILIES.items()
            },
        )
        second["bounded_future_references"]["expected_archive_sha256"] = "x"
        second["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        self.assertEqual(
            third["bounded_future_references"]["expected_archive_sha256"],
            resolver.EXPECTED_ARCHIVE_SHA256,
        )
        self.assertIs(
            third["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )
        declared = self.canonical_request(unknown_override="visible")
        self.assertEqual(declared["unknown_override"], "visible")

    def test_03_canonical_recorded_branch(self) -> None:
        request = self.canonical_request()
        before = self._clone(request)
        result = self.invoke(request)
        self.assertEqual(request, before)
        self.assert_recorded(result)
        state = self.state(result)
        for key in (
            "specification_markers_validated",
            "waiting_artifact_validated",
            "requested_declaration_candidate_schema_validated",
            "bounded_future_references_validated",
            "requested_posture_key_families_validated",
            "non_conversion_statement_validated",
        ):
            self.assertIs(state[key], True)
        self.assertEqual(set(result), resolver.RESULT_SECTIONS)
        self.assertIsInstance(result[METADATA_KEY], dict)
        self.assertIsInstance(result[DECLARED_KEY], dict)

    def test_04_lawful_not_recorded_branch(self) -> None:
        request = self.canonical_request(selected=False)
        result = self.invoke(request)
        self.assert_not_recorded(result)
        non_meaning = result[f"{PREFIX}_non_meaning"]
        for key in (
            "not_recorded_is_not_preparer_refusal_or_preparation_failure",
            "not_recorded_is_not_basis_invalidity",
            "not_recorded_is_not_receiver_attestation_failure",
            "not_recorded_is_not_candidate_insufficiency",
        ):
            self.assertIs(non_meaning[key], True)

    def test_05_request_mapping_shape_intent_and_unknown_fields(self) -> None:
        for value in ([], "request", 1, False):
            with self.subTest(non_mapping=repr(value)):
                self.assert_blocked(
                    self.invoke(value),
                    "REQUEST_NOT_MAPPING",
                )
        canonical = self.canonical_request()
        for key in tuple(canonical):
            request = self._clone(canonical)
            request.pop(key)
            with self.subTest(missing=key):
                self.assert_blocked(
                    self.invoke(request),
                    "REQUEST_FIELD_MISSING",
                )
        unknown = self.canonical_request(unknown_top_level_field=True)
        self.assert_blocked(
            self.invoke(unknown),
            "REQUEST_FIELD_UNKNOWN",
        )
        unsupported = self.canonical_request(intent="UNSUPPORTED")
        self.assert_blocked(
            self.invoke(unsupported),
            "UNSUPPORTED_INTENT",
        )
        explicit = self.canonical_request(intent=resolver.INTENT_BLOCK)
        self.assert_blocked(
            self.invoke(explicit),
            "EXPLICIT_BLOCK_REQUESTED",
        )

    def test_06_request_identity_and_exact_path_matrix(self) -> None:
        expected = resolver._expected_request_values()
        for field in expected:
            request = self.canonical_request(**{field: "wrong"})
            if field.startswith("preparation_request_"):
                code = "PREPARATION_REQUEST_IDENTITY_MISMATCH"
            elif field.startswith("selected_receiver_attestation_operation_"):
                code = "SELECTED_OPERATION_IDENTITY_MISMATCH"
            elif "candidate_" in field:
                code = "SELECTED_CANDIDATE_IDENTITY_MISMATCH"
            elif field == "governing_preparation_request_specification_path":
                code = "GOVERNING_SPECIFICATION_PATH_MISMATCH"
            else:
                code = "WAITING_ARTIFACT_PATH_MISMATCH"
            with self.subTest(identity=field):
                self.assert_blocked(self.invoke(request), code)

    def test_07_request_selection_requires_exact_boolean(self) -> None:
        for value in (None, 0, 1, "false", "true", [], {}):
            request = self.canonical_request()
            request["basis_declaration_preparation_selected"] = value
            with self.subTest(selection=repr(value)):
                self.assert_blocked(
                    self.invoke(request),
                    "REQUEST_SELECTION_NOT_BOOLEAN",
                )
        self.assert_recorded(self.invoke(self.canonical_request(selected=True)))
        self.assert_not_recorded(
            self.invoke(self.canonical_request(selected=False))
        )

    def test_08_requested_21_field_schema_is_exact_and_ordered(self) -> None:
        canonical = list(resolver.REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES)
        cases: dict[str, tuple[Any, str]] = {
            "missing": (
                canonical[:-1],
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "unknown": (
                canonical + ["unknown_field"],
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "duplicate": (
                canonical + [canonical[-1]],
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "altered": (
                [*canonical[:-1], "altered_field"],
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "reordered": (
                list(reversed(canonical)),
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "mapping": (
                {key: False for key in canonical},
                "REQUEST_PAYLOAD_CONTAINS_COMPLETED_BASIS_OR_SOURCE_MATERIAL",
            ),
            "string": (
                ",".join(canonical),
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
            "none": (
                None,
                "REQUESTED_DECLARATION_CANDIDATE_SCHEMA_MISMATCH",
            ),
        }
        for name, (value, expected_code) in cases.items():
            request = self.canonical_request()
            request["requested_declaration_candidate_field_names"] = value
            with self.subTest(schema=name):
                self.assert_blocked(
                    self.invoke(request),
                    expected_code,
                )
        self.assert_recorded(
            self.invoke(
                self.canonical_request(
                    requested_declaration_candidate_field_names=canonical
                )
            )
        )

    def test_09_completed_basis_values_and_result_preclaims_block(self) -> None:
        payload_cases = (
            ("operation_basis", {"basis_items": []}),
            ("completed_operation_basis_values", {"value": True}),
            ("archive_bytes", "embedded"),
            ("attestation_statement_body", "complete body"),
            ("recorded_signal_body", {"samples": []}),
        )
        for key, payload in payload_cases:
            references = dict(resolver.BOUNDED_FUTURE_REFERENCES)
            references[key] = payload
            request = self.canonical_request(
                bounded_future_references=references
            )
            with self.subTest(completed_payload=key):
                self.assert_blocked(
                    self.invoke(request),
                    "REQUEST_PAYLOAD_CONTAINS_COMPLETED_BASIS_OR_SOURCE_MATERIAL",
                )
        for key in sorted(resolver.RESULT_PRECLAIM_FIELDS):
            request = self.canonical_request(**{key: True})
            with self.subTest(result_preclaim=key):
                self.assert_blocked(self.invoke(request))

    def test_10_bounded_future_reference_family_is_exact(self) -> None:
        canonical = dict(resolver.BOUNDED_FUTURE_REFERENCES)
        cases: list[tuple[str, Any]] = []
        missing = self._clone(canonical)
        missing.pop(next(iter(missing)))
        cases.append(("missing", missing))
        cases.append(("extra", {**canonical, "extra_reference": "x"}))
        cases.append(("non_mapping", list(canonical.values())))
        for key in canonical:
            altered = self._clone(canonical)
            altered[key] = None if key == "expected_archive_sha256" else "alternate"
            cases.append((f"altered_{key}", altered))
        for name, value in cases:
            request = self.canonical_request(
                bounded_future_references=value
            )
            with self.subTest(reference_case=name):
                self.assert_blocked(
                    self.invoke(request),
                    "BOUNDED_FUTURE_REFERENCE_FAMILY_MISMATCH",
                )

    def test_11_reference_contract_does_not_claim_capture_validation(self) -> None:
        result = self.invoke(self.canonical_request())
        self.assert_recorded(result)
        validation = result["bounded_future_reference_validation"]
        self.assertIs(validation["bounded_future_references_validated"], True)
        for key in (
            "capture_file_existence_validated",
            "archive_hash_computed",
            "timestamp_parsed",
            "recorded_signal_inspected",
        ):
            self.assertIs(validation[key], False)
        statement = result[f"{PREFIX}_statement"]
        self.assertIs(
            statement[
                "source_body_preparation_is_not_independent_verification"
            ],
            True,
        )
        state = self.state(result)
        for key in (
            "identity_created",
            "authority_created",
            "truth_created",
            "standing_created",
            "presence_established",
        ):
            self.assertIs(state[key], False)

    def test_12_posture_key_families_are_names_only_and_exact(self) -> None:
        canonical = {
            key: list(value)
            for key, value in resolver.REQUESTED_POSTURE_KEY_FAMILIES.items()
        }
        cases: list[tuple[str, Any]] = []
        missing_family = self._clone(canonical)
        missing_family.pop(next(iter(missing_family)))
        cases.append(("missing_family", missing_family))
        cases.append(("extra_family", {**canonical, "extra": []}))
        cases.append(("non_mapping", []))
        for family, names in canonical.items():
            missing = self._clone(canonical)
            missing[family] = names[:-1]
            cases.append((f"missing_key_{family}", missing))
            extra = self._clone(canonical)
            extra[family] = names + ["extra_key"]
            cases.append((f"extra_key_{family}", extra))
            altered = self._clone(canonical)
            altered[family] = [*names[:-1], "altered_key"]
            cases.append((f"altered_key_{family}", altered))
            duplicate = self._clone(canonical)
            duplicate[family] = names + [names[-1]]
            cases.append((f"duplicate_key_{family}", duplicate))
            reordered = self._clone(canonical)
            reordered[family] = list(reversed(names))
            cases.append((f"reordered_{family}", reordered))
            string_value = self._clone(canonical)
            string_value[family] = ",".join(names)
            cases.append((f"string_{family}", string_value))
        for posture in (False, True, None):
            completed = {
                family: {key: posture for key in names}
                for family, names in canonical.items()
            }
            cases.append((f"completed_map_{posture!r}", completed))
        mixed = {
            family: {
                key: index % 2 == 0
                for index, key in enumerate(names)
            }
            for family, names in canonical.items()
        }
        cases.append(("completed_map_mixed", mixed))
        for name, value in cases:
            request = self.canonical_request(
                requested_posture_key_families=value
            )
            with self.subTest(posture_case=name):
                self.assert_blocked(
                    self.invoke(request),
                    "REQUESTED_POSTURE_KEY_FAMILY_MISMATCH",
                )

    def test_13_non_conversion_sentence_is_exact(self) -> None:
        exact = resolver.CANONICAL_NON_CONVERSION_STATEMENT
        cases = (
            exact[:-1],
            exact.capitalize(),
            exact.replace("identity, ", ""),
            exact + " Appended clause.",
            None,
            ["not", "a", "string"],
            (
                "Trace admission does not prove identity, authority, "
                "truth, or standing."
            ),
        )
        for value in cases:
            request = self.canonical_request(
                requested_non_conversion_statement=value
            )
            with self.subTest(non_conversion=repr(value)):
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CONVERSION_STATEMENT_MISMATCH",
                )
        self.assert_recorded(
            self.invoke(
                self.canonical_request(
                    requested_non_conversion_statement=exact
                )
            )
        )

    def test_14_every_prohibited_request_flag_true_blocks(self) -> None:
        for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
            request = self.canonical_request(**{field: True})
            with self.subTest(prohibited_flag=field):
                self.assert_blocked(self.invoke(request), expected_code)

    def test_15_prohibited_request_flags_require_exact_false(self) -> None:
        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            for value in (None, 0, "false", []):
                request = self.canonical_request()
                request[field] = value
                with self.subTest(flag=field, value=repr(value)):
                    self.assert_blocked(
                        self.invoke(request),
                        "REQUEST_VALUE_MISMATCH",
                    )

    def test_16_every_request_non_claim_true_blocks(self) -> None:
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            non_claims = {
                key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS
            }
            non_claims[field] = True
            request = self.canonical_request(
                declared_non_claims=non_claims
            )
            with self.subTest(non_claim=field):
                result = self.invoke(request)
                self.assert_blocked(
                    result,
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
                self.assertIs(result["non_claims"][field], False)

    def test_17_request_non_claim_shape_and_types_are_exact(self) -> None:
        canonical = {
            key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS
        }
        representative = resolver.REQUIRED_FALSE_NON_CLAIMS[:4]
        cases: list[tuple[str, Any]] = []
        for field, value in zip(
            representative,
            (None, 0, "false", _MISSING),
        ):
            changed = self._clone(canonical)
            if value is _MISSING:
                changed.pop(field)
            else:
                changed[field] = value
            cases.append((f"{field}_{value!r}", changed))
        cases.extend(
            (
                ("unknown", {**canonical, "unknown_non_claim": False}),
                ("none", None),
                ("sequence", list(canonical)),
            )
        )
        for name, value in cases:
            request = self.canonical_request()
            request["declared_non_claims"] = value
            with self.subTest(non_claim_case=name):
                self.assert_blocked(
                    self.invoke(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )

    def test_18_specification_exact_markers_and_each_class(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            spec_path = root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            canonical = spec_path.read_text(encoding="utf-8")
            self.assert_recorded(
                self.invoke(self.canonical_request(), root=root)
            )
            for marker_class, markers in (
                resolver.PREPARATION_REQUEST_SPEC_MARKER_CLASSES.items()
            ):
                for index, marker in enumerate(markers):
                    self.assertIn(marker, canonical)
                    changed = canonical.replace(
                        marker,
                        (
                            f"REMOVED_{marker_class.upper()}_"
                            f"MARKER_{index:03d}"
                        ),
                    )
                    self._write_text(spec_path, changed)
                    with self.subTest(
                        marker_class=marker_class,
                        marker_index=index,
                    ):
                        self.assert_blocked(
                            self.invoke(
                                self.canonical_request(),
                                root=root,
                            ),
                            "PREPARATION_REQUEST_SPECIFICATION_MARKER_MISSING",
                        )
                    self._write_text(spec_path, canonical)

    def test_19_each_requested_schema_marker_is_required_by_spec(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            spec_path = root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            canonical = spec_path.read_text(encoding="utf-8")
            for index, marker in enumerate(
                resolver.REQUESTED_DECLARATION_CANDIDATE_FIELD_NAMES
            ):
                self.assertIn(marker, canonical)
                changed = canonical.replace(
                    marker,
                    f"removed_schema_marker_{index:02d}",
                )
                self._write_text(spec_path, changed)
                with self.subTest(schema_marker=marker):
                    self.assert_blocked(
                        self.invoke(self.canonical_request(), root=root),
                        "PREPARATION_REQUEST_SPECIFICATION_MARKER_MISSING",
                    )
                self._write_text(spec_path, canonical)

    def test_20_specification_missing_and_non_file_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_fixture(
                root,
                resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH,
            )
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "PREPARATION_REQUEST_SPECIFICATION_REFERENCE_MISSING",
            )
            spec_path = root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            spec_path.mkdir(parents=True)
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "PREPARATION_REQUEST_SPECIFICATION_REFERENCE_MISSING",
            )

    def test_21_waiting_metadata_identity_outcome_and_null_result(self) -> None:
        live_path = (
            REPOSITORY_ROOT
            / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        )
        canonical = json.loads(live_path.read_text(encoding="utf-8"))
        identity_paths = (
            (OPERATION_KEY, "operation_id"),
            (OPERATION_KEY, "operation_type"),
            (OPERATION_KEY, "operation_version"),
            (OPERATION_KEY, "operation_scope"),
            (
                OPERATION_KEY,
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_id",
            ),
            (
                OPERATION_KEY,
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_type",
            ),
            (
                OPERATION_KEY,
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_version",
            ),
            (
                OPERATION_KEY,
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_scope",
            ),
            (OPERATION_KEY, "receiver_side_answerable_basis_candidate_id"),
            (OPERATION_KEY, "receiver_side_answerable_basis_candidate_type"),
            (OPERATION_KEY, "receiver_side_answerable_basis_candidate_scope"),
            (OPERATION_KEY, "selected_receiver_attestation_boundary_id"),
            ("selected_operation_and_candidate_identity", "operation_id"),
            ("selected_operation_and_candidate_identity", "operation_type"),
            ("selected_operation_and_candidate_identity", "operation_version"),
            ("selected_operation_and_candidate_identity", "operation_scope"),
            (
                "selected_operation_and_candidate_identity",
                "selected_candidate_id",
            ),
            (
                "selected_operation_and_candidate_identity",
                "selected_candidate_type",
            ),
            (
                "selected_operation_and_candidate_identity",
                "selected_candidate_scope",
            ),
            (
                "selected_operation_and_candidate_identity",
                "selected_boundary_id",
            ),
        )
        result_paths = (
            (OPERATION_KEY, "receiver_attestation_operation_result"),
            (OPERATION_SUMMARY_KEY, "operation_result"),
            ("operation_result_detail", "operation_result"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            self.assert_recorded(
                self._resolve_waiting_variant(root, canonical)
            )
            metadata_cases = (
                (("resolver_module",), "wrong", "WAITING_ARTIFACT_METADATA_MISMATCH"),
                (("result_version",), "9", "WAITING_ARTIFACT_METADATA_MISMATCH"),
                (("failed_check_count",), 1, "WAITING_ARTIFACT_FAILED_CHECKS_PRESENT"),
            )
            for path, value, code in metadata_cases:
                changed = self._clone(canonical)
                self._set_path(changed, path, value)
                with self.subTest(waiting_metadata=path):
                    self.assert_blocked(
                        self._resolve_waiting_variant(root, changed),
                        code,
                    )
            for path in identity_paths:
                changed = self._clone(canonical)
                self._set_path(changed, path, "wrong")
                with self.subTest(waiting_identity=path):
                    self.assert_blocked(
                        self._resolve_waiting_variant(root, changed),
                        "WAITING_ARTIFACT_IDENTITY_MISMATCH",
                    )
            changed = self._clone(canonical)
            changed["outcome"] = "NOT_WAITING"
            self.assert_blocked(
                self._resolve_waiting_variant(root, changed),
                "WAITING_ARTIFACT_NOT_WAITING",
            )
            for path in result_paths:
                for value in ("result", _MISSING):
                    changed = self._clone(canonical)
                    self._set_path(changed, path, value)
                    with self.subTest(operation_result=path, value=repr(value)):
                        self.assert_blocked(
                            self._resolve_waiting_variant(root, changed),
                            "WAITING_ARTIFACT_OPERATION_RESULT_PRESENT",
                        )

    def test_22_waiting_false_fields_require_exact_boolean_false(self) -> None:
        live_path = (
            REPOSITORY_ROOT
            / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        )
        canonical = json.loads(live_path.read_text(encoding="utf-8"))
        false_paths: list[tuple[tuple[str, ...], str]] = [
            (
                ("supplied_operation_basis_admission_metadata", "basis_supplied"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                ("supplied_operation_basis_admission_metadata", "basis_admitted"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                (OPERATION_KEY, "operation_basis_supplied"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                (OPERATION_KEY, "operation_basis_admitted"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                (OPERATION_SUMMARY_KEY, "basis_supplied"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (
                (OPERATION_SUMMARY_KEY, "basis_admitted"),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            ),
            (("block", "blocked"), "WAITING_ARTIFACT_BLOCKED"),
            ((OPERATION_SUMMARY_KEY, "blocked"), "WAITING_ARTIFACT_BLOCKED"),
        ]
        operation_false = (
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
        )
        summary_false = (
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
        )
        false_paths.extend(
            (
                (OPERATION_KEY, field),
                "WAITING_ARTIFACT_OPERATION_ALREADY_RECORDED_DECIDED_OR_EXHAUSTED",
            )
            for field in operation_false
        )
        false_paths.extend(
            (
                (OPERATION_SUMMARY_KEY, field),
                "WAITING_ARTIFACT_OPERATION_ALREADY_RECORDED_DECIDED_OR_EXHAUSTED",
            )
            for field in summary_false
        )
        false_paths.extend(
            (("non_claims", field), "WAITING_ARTIFACT_NON_CLAIM_NOT_FALSE")
            for field in resolver.WAITING_REQUIRED_FALSE_NON_CLAIMS
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for path, code in false_paths:
                for value in (True, None, 0, "false", _MISSING):
                    changed = self._clone(canonical)
                    self._set_path(changed, path, value)
                    with self.subTest(
                        waiting_false_path=path,
                        value=repr(value),
                    ):
                        self.assert_blocked(
                            self._resolve_waiting_variant(root, changed),
                            code,
                        )
            changed = self._clone(canonical)
            changed["metadata"] = {"basis_supplied": False}
            self._set_path(
                changed,
                (
                    "supplied_operation_basis_admission_metadata",
                    "basis_supplied",
                ),
                _MISSING,
            )
            self.assert_blocked(
                self._resolve_waiting_variant(root, changed),
                "WAITING_ARTIFACT_BASIS_ALREADY_SUPPLIED_OR_ADMITTED",
            )
            for field, value in (
                ("code", "BLOCKED"),
                ("block_code", "BLOCKED"),
                ("reason", "blocked"),
            ):
                changed = self._clone(canonical)
                changed["block"][field] = value
                with self.subTest(waiting_block_companion=field):
                    self.assert_blocked(
                        self._resolve_waiting_variant(root, changed),
                        "WAITING_ARTIFACT_BLOCKED",
                    )

    def test_23_waiting_true_fields_require_exact_boolean_true(self) -> None:
        live_path = (
            REPOSITORY_ROOT
            / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        )
        canonical = json.loads(live_path.read_text(encoding="utf-8"))
        true_paths: list[tuple[tuple[str, ...], str]] = [
            (
                (OPERATION_SUMMARY_KEY, "upstream_boundary_validated"),
                "WAITING_ARTIFACT_UPSTREAM_BOUNDARY_NOT_VALIDATED",
            ),
            (
                ("upstream_boundary_basis", "upstream_boundary_validated"),
                "WAITING_ARTIFACT_UPSTREAM_BOUNDARY_NOT_VALIDATED",
            ),
            (
                (
                    OPERATION_KEY,
                    "selected_receiver_attestation_boundary_validated",
                ),
                "WAITING_ARTIFACT_UPSTREAM_BOUNDARY_NOT_VALIDATED",
            ),
            (
                (
                    OPERATION_SUMMARY_KEY,
                    "result_level_non_claims_canonical_false",
                ),
                "WAITING_ARTIFACT_NON_CLAIM_NOT_FALSE",
            ),
        ]
        for field in (
            "complete_upstream_boundary_artifact_omitted",
            "complete_candidate_sufficiency_artifact_omitted",
            "complete_candidate_sufficiency_basis_omitted",
            "complete_operation_basis_omitted",
            "archive_bytes_omitted",
            "text_component_bodies_omitted",
            "recorded_signal_body_omitted",
        ):
            true_paths.append(
                (
                    (OPERATION_SUMMARY_KEY, field),
                    "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
                )
            )
        true_paths.extend(
            (
                (
                    (
                        "supplied_operation_basis_admission_metadata",
                        "complete_operation_basis_omitted",
                    ),
                    "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
                ),
                (
                    (
                        "bounded_component_validation",
                        "archive_bytes_omitted",
                    ),
                    "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
                ),
                (
                    (
                        "bounded_component_validation",
                        "text_component_bodies_omitted",
                    ),
                    "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
                ),
                (
                    (
                        "bounded_component_validation",
                        "recorded_signal_body_omitted",
                    ),
                    "WAITING_ARTIFACT_OMISSION_POSTURE_INVALID",
                ),
            )
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for path, code in true_paths:
                for value in (False, None, 1, "true", _MISSING):
                    changed = self._clone(canonical)
                    self._set_path(changed, path, value)
                    with self.subTest(
                        waiting_true_path=path,
                        value=repr(value),
                    ):
                        self.assert_blocked(
                            self._resolve_waiting_variant(root, changed),
                            code,
                        )

    def test_24_waiting_artifact_file_and_json_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_fixture(
                root,
                resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            )
            waiting_path = (
                root / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
            )
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "SELECTED_WAITING_ARTIFACT_REFERENCE_MISSING",
            )
            waiting_path.mkdir(parents=True)
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "SELECTED_WAITING_ARTIFACT_REFERENCE_MISSING",
            )
        malformed_cases = {
            "malformed": "{",
            "duplicate": '{"resolver_module":"a","resolver_module":"b"}\n',
        }
        for name, text in malformed_cases.items():
            with tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                self._copy_fixture(
                    root,
                    resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
                )
                waiting_path = (
                    root / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
                )
                self._write_text(waiting_path, text)
                with self.subTest(waiting_json=name):
                    self.assert_blocked(
                        self.invoke(self.canonical_request(), root=root),
                        "SELECTED_WAITING_ARTIFACT_NOT_PARSEABLE",
                    )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._copy_fixture(
                root,
                resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            )
            self._write_json(
                root / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH,
                [],
            )
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "SELECTED_WAITING_ARTIFACT_NOT_MAPPING",
            )

    def test_25_waiting_nonclaims_each_flip_and_sensitive_locks(self) -> None:
        live_path = (
            REPOSITORY_ROOT
            / resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH
        )
        canonical = json.loads(live_path.read_text(encoding="utf-8"))
        sensitive = {
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        }
        self.assertTrue(
            sensitive.issubset(resolver.WAITING_REQUIRED_FALSE_NON_CLAIMS)
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for field in resolver.WAITING_REQUIRED_FALSE_NON_CLAIMS:
                changed = self._clone(canonical)
                changed["non_claims"][field] = True
                with self.subTest(waiting_non_claim=field):
                    self.assert_blocked(
                        self._resolve_waiting_variant(root, changed),
                        "WAITING_ARTIFACT_NON_CLAIM_NOT_FALSE",
                    )

    def test_26_from_path_contract_duplicate_and_override_visibility(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            recorded_path = self._write_json(
                root / "requests/recorded.json",
                self.canonical_request(),
            )
            not_recorded_path = self._write_json(
                root / "requests/not_recorded.json",
                self.canonical_request(selected=False),
            )
            unknown_path = self._write_json(
                root / "requests/unknown.json",
                self.canonical_request(unknown_override="visible"),
            )
            malformed_path = self._write_text(
                root / "requests/malformed.json",
                "{",
            )
            duplicate_path = self._write_text(
                root / "requests/duplicate.json",
                '{"intent":"a","intent":"b"}\n',
            )
            array_path = self._write_json(
                root / "requests/array.json",
                [],
            )
            missing_path = root / "requests/missing.json"
            with patch.object(resolver, "REPO_ROOT", root):
                recorded = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    recorded_path
                )
                not_recorded = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    not_recorded_path
                )
                unknown = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    unknown_path
                )
                malformed = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    malformed_path
                )
                duplicate = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    duplicate_path
                )
                array = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    array_path
                )
                missing = resolver.resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_from_path(
                    missing_path
                )
            self.assert_recorded(recorded)
            self.assert_not_recorded(not_recorded)
            self.assert_blocked(unknown, "REQUEST_FIELD_UNKNOWN")
            for result in (malformed, duplicate, array, missing):
                self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_27_determinism_and_nested_input_immutability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            request = self.canonical_request()
            before = self._clone(request)
            first = self.invoke(request, root=root)
            second = self.invoke(request, root=root)
            third = self.invoke(self._clone(request), root=root)
            self.assertEqual(first, second)
            self.assertEqual(second, third)
            self.assertEqual(request, before)
            for key in (
                "requested_declaration_candidate_field_names",
                "bounded_future_references",
                "requested_posture_key_families",
                "declared_non_claims",
            ):
                self.assertEqual(request[key], before[key])
            summary_before = self._clone(first)
            resolver.build_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_summary(
                first
            )
            self.assertEqual(first, summary_before)

    def test_28_summaries_are_exact_for_all_three_branches(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            recorded = self.invoke(self.canonical_request(), root=root)
            not_recorded = self.invoke(
                self.canonical_request(selected=False),
                root=root,
            )
            blocked = self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK),
                root=root,
            )
        cases = (
            (
                recorded,
                resolver.OUTCOME_RECORDED,
                resolver.REQUEST_RESULT_RECORDED,
                True,
                False,
            ),
            (
                not_recorded,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.REQUEST_RESULT_NOT_RECORDED,
                False,
                False,
            ),
            (
                blocked,
                resolver.OUTCOME_BLOCKED,
                resolver.REQUEST_RESULT_NOT_EVALUATED,
                True,
                True,
            ),
        )
        for result, outcome, request_result, selected, blocked_value in cases:
            with self.subTest(summary_branch=outcome):
                before = self._clone(result)
                self._assert_summary_contract(
                    result,
                    outcome=outcome,
                    request_result=request_result,
                    selected=selected,
                    blocked=blocked_value,
                )
                self.assertEqual(result, before)
                self.assert_material_omitted(result)

    def test_29_writer_writes_all_branches_and_suffixes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            results = (
                self.invoke(self.canonical_request(), root=root),
                self.invoke(
                    self.canonical_request(selected=False),
                    root=root,
                ),
                self.invoke(
                    self.canonical_request(intent=resolver.INTENT_BLOCK),
                    root=root,
                ),
            )
            output_root = root / "writer"
            for index, result in enumerate(results):
                target = output_root / str(index) / resolver.OUTPUT_FILENAME
                before = self._clone(result)
                written = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                    result,
                    target,
                )
                self.assertEqual(result, before)
                self.assertEqual(written, target)
                text = written.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"))
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
            target = output_root / "repeat" / resolver.OUTPUT_FILENAME
            first = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                results[0],
                target,
            )
            original = first.read_bytes()
            second = resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                results[0],
                target,
            )
            self.assertEqual(first, target)
            self.assertEqual(
                second.name,
                f"{target.stem}_001{target.suffix}",
            )
            self.assertEqual(first.read_bytes(), original)

    def test_30_writer_refuses_malformed_and_inconsistent_results(self) -> None:
        error = resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            recorded = self.invoke(self.canonical_request(), root=root)
            not_recorded = self.invoke(
                self.canonical_request(selected=False),
                root=root,
            )
            blocked = self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK),
                root=root,
            )
            malformed: list[tuple[str, Any]] = [
                ("non_mapping", []),
            ]
            wrong_module = self._clone(recorded)
            wrong_module["resolver_module"] = "wrong"
            malformed.append(("wrong_module", wrong_module))
            wrong_version = self._clone(recorded)
            wrong_version["result_version"] = "9"
            malformed.append(("wrong_version", wrong_version))
            wrong_pair = self._clone(recorded)
            wrong_pair["outcome"] = resolver.OUTCOME_NOT_RECORDED
            malformed.append(("wrong_outcome_result_pair", wrong_pair))
            wrong_block = self._clone(recorded)
            wrong_block["block"]["blocked"] = True
            malformed.append(("wrong_block_posture", wrong_block))
            for name, source, field in (
                ("recorded", recorded, "preparation_request_recorded"),
                (
                    "not_recorded",
                    not_recorded,
                    "preparation_request_result_recorded",
                ),
                ("blocked", blocked, "preparation_request_exhausted"),
            ):
                changed = self._clone(source)
                changed[STATE_KEY][field] = not changed[STATE_KEY][field]
                malformed.append((f"inconsistent_{name}", changed))
            missing_non_claim = self._clone(recorded)
            missing_non_claim["non_claims"].pop(
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            )
            malformed.append(("missing_non_claim", missing_non_claim))
            flipped_non_claim = self._clone(recorded)
            flipped_non_claim["non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ] = True
            malformed.append(("flipped_non_claim", flipped_non_claim))
            for name, value in malformed:
                with self.subTest(writer_refusal=name):
                    with self.assertRaises(error):
                        resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                            value,
                            root / "refused" / name / resolver.OUTPUT_FILENAME,
                        )

    def test_31_writer_refuses_embedded_complete_material(self) -> None:
        error = resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError
        result = self.invoke(self.canonical_request())
        complete_material = (
            ("complete_waiting_artifact", {"full": "waiting"}),
            ("complete_upstream_boundary_artifact", {"full": "upstream"}),
            ("complete_candidate_sufficiency_artifact", {"full": "candidate"}),
            ("complete_candidate_sufficiency_basis", {"full": "basis"}),
            ("archive_bytes", b"archive"),
            ("attestation_statement_body", "complete text"),
            ("recorded_signal_body", {"samples": []}),
            ("completed_operation_basis_values", {"basis": True}),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, payload in complete_material:
                changed = self._clone(result)
                changed[METADATA_KEY][name] = payload
                with self.subTest(embedded=name):
                    with self.assertRaises(error):
                        resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                            changed,
                            root / name / resolver.OUTPUT_FILENAME,
                        )

    def test_32_writer_refuses_protected_and_incompatible_paths(self) -> None:
        error = resolver.ReceiverSideAnswerableBasisReceiverAttestationOperationBasisDeclarationPreparationRequestV0MinError
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            result = self.invoke(self.canonical_request(), root=root)
            protected = (
                Path("src") / resolver.OUTPUT_FILENAME,
                Path("spec") / resolver.OUTPUT_FILENAME,
                Path("tests") / resolver.OUTPUT_FILENAME,
                Path("reference") / resolver.OUTPUT_FILENAME,
                resolver.SELECTED_WAITING_ARTIFACT_RELATIVE_PATH.parent
                / resolver.OUTPUT_FILENAME,
                resolver.SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH.parent
                / resolver.OUTPUT_FILENAME,
                resolver.SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH.parent
                / resolver.OUTPUT_FILENAME,
                resolver.BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
                / resolver.OUTPUT_FILENAME,
            )
            with patch.object(resolver, "REPO_ROOT", root):
                for path in protected:
                    with self.subTest(protected_path=str(path)):
                        with self.assertRaises(error):
                            resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                                result,
                                path,
                            )
            parent_file = root / "incompatible_parent"
            parent_file.write_text("not a directory", encoding="utf-8")
            with self.assertRaises(error):
                resolver.write_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_preparation_request_v0_min_result(
                    result,
                    parent_file / resolver.OUTPUT_FILENAME,
                )

    def test_33_result_distinctions_and_no_downstream_conversion(self) -> None:
        results = (
            self.invoke(self.canonical_request()),
            self.invoke(self.canonical_request(selected=False)),
            self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK)
            ),
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_non_conversion_false(result)
                statement = result[f"{PREFIX}_statement"]
                for key in (
                    "request_records_request_posture_only",
                    "request_is_not_preparation_completion",
                    "preparation_is_not_declaration",
                    "declaration_is_not_operation_supply",
                    "operation_supply_is_not_operation_result",
                    "source_body_preparation_is_not_independent_verification",
                    "request_exhaustion_is_not_preparation_completion",
                    "request_exhaustion_is_not_next_step_authorization",
                    "open_does_not_mean_next",
                ):
                    self.assertIs(statement[key], True)
                non_meaning = result[f"{PREFIX}_non_meaning"]
                for value in non_meaning.values():
                    self.assertIs(type(value), bool)
                    self.assertIs(value, True)
                detail = result["request_result_detail"]
                for key in (
                    "basis_declaration_preparation_started",
                    "basis_declaration_preparation_completed",
                    "operation_basis_prepared",
                    "operation_basis_declared",
                    "operation_basis_supplied",
                    "operation_basis_admitted",
                    "receiver_attestation_operation_executed",
                    "receiver_attestation_operation_result_exists",
                ):
                    self.assertIs(detail[key], False)


if __name__ == "__main__":
    unittest.main()
