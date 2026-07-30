"""Tests for one bounded receiver-answerable-receipt operation.

The suite admits only the exact completed receipt boundary and the exact
recorded receiver-attestation operation selected by that boundary.  All
mutations are temporary or in-memory.  No capture body, standing artifact,
receipt-operation live result, presence route, or downstream permission is
created.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from unittest.mock import patch

import resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min as resolver


REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_PATH = (
    REPO_ROOT / resolver.GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
)
BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
)
BOUNDARY_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_V0_MIN_TERMINAL_SUMMARY.md"
)
ATTESTATION_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
)
WAITING_ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.ORIGINAL_WAITING_RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
)
SUPPLY_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_supply_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_"
    "basis_supply_001__receiver_side_answerable_basis_"
    "receiver_attestation_operation_basis_supply_v0_min_result.json"
)
RESOLVER_PATH = Path(resolver.__file__).resolve()
CANONICAL_OUTPUT_ROOT = resolver.OUTPUT_ROOT

OPERATION_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
)
CHECKS_KEY = OPERATION_KEY + "_checks"
STATEMENT_KEY = OPERATION_KEY + "_statement"
NON_MEANING_KEY = OPERATION_KEY + "_non_meaning"
SUMMARY_KEY = OPERATION_KEY + "_summary"
BOUNDARY_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_boundary"
)
BOUNDARY_SUMMARY_KEY = BOUNDARY_KEY + "_summary"
ATTESTATION_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation"
)
ATTESTATION_SUMMARY_KEY = ATTESTATION_KEY + "_summary"

_MISSING = object()
_DELETE = object()
INVALID_BOOLEAN_VALUES = (
    0,
    1,
    "true",
    "false",
    None,
    [],
    {},
    "non-empty",
)


class ReceiverAnswerableReceiptOperationV0MinTests(unittest.TestCase):
    """Verify one atomic receipt operation and every bounded refusal."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            BOUNDARY_ARTIFACT_PATH,
            BOUNDARY_TERMINAL_SUMMARY_PATH,
            ATTESTATION_ARTIFACT_PATH,
            ATTESTATION_TERMINAL_SUMMARY_PATH,
            WAITING_ATTESTATION_ARTIFACT_PATH,
            SUPPLY_ARTIFACT_PATH,
        )
        for path in cls.preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input missing: {path}")
        cls.preserved_hashes = {
            path: cls.sha256(path) for path in cls.preserved_paths
        }
        cls.specification_text = SPECIFICATION_PATH.read_text(encoding="utf-8")
        cls.boundary_artifact = cls.strict_load_json(BOUNDARY_ARTIFACT_PATH)
        cls.attestation_artifact = cls.strict_load_json(
            ATTESTATION_ARTIFACT_PATH
        )
        if not isinstance(cls.boundary_artifact, dict):
            raise AssertionError("receipt-boundary artifact is not a mapping")
        if not isinstance(cls.attestation_artifact, dict):
            raise AssertionError("attestation artifact is not a mapping")
        cls.output_snapshot = cls.snapshot_output_root()

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            if cls.sha256(path) != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if cls.snapshot_output_root() != cls.output_snapshot:
            raise AssertionError("canonical receipt-operation output root changed")

    @staticmethod
    def sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            while True:
                chunk = handle.read(65536)
                if not chunk:
                    break
                digest.update(chunk)
        return digest.hexdigest()

    @staticmethod
    def strict_load_json(path: Path) -> object:
        def reject_duplicates(
            pairs: list[tuple[str, object]],
        ) -> dict[str, object]:
            result: dict[str, object] = {}
            for key, value in pairs:
                if key in result:
                    raise AssertionError(f"duplicate fixture key: {key}")
                result[key] = value
            return result

        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicates,
        )

    @classmethod
    def snapshot_output_root(cls) -> object:
        root = CANONICAL_OUTPUT_ROOT
        if not root.exists():
            return None
        entries: list[tuple[str, str, str | None]] = []
        for path in sorted(root.rglob("*")):
            relative = str(path.relative_to(root))
            if path.is_file():
                entries.append(("file", relative, cls.sha256(path)))
            elif path.is_dir():
                entries.append(("dir", relative, None))
            else:
                entries.append(("other", relative, None))
        return tuple(entries)

    def write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(
            path.is_dir(),
            f"temporary fixture file path is a directory: {path}",
        )
        path.write_text(value, encoding="utf-8")
        return path

    def write_json(self, path: Path, value: object) -> Path:
        return self.write_text(
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

    def copy_fixture_root(self, root: Path) -> None:
        for relative in (
            resolver.GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH,
            resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH,
        ):
            source = REPO_ROOT / relative
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def canonical_request(self, **overrides: object) -> dict[str, Any]:
        return (
            resolver.build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def invoke(
        self,
        request: object = _MISSING,
        *,
        root: Path | None = None,
    ) -> dict[str, Any]:
        supplied = (
            self.canonical_request()
            if request is _MISSING
            else copy.deepcopy(request)
        )
        before = copy.deepcopy(supplied)
        if root is None:
            result = (
                resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_with_mocked_artifacts(
        self,
        *,
        request: object = _MISSING,
        boundary: object = _MISSING,
        attestation: object = _MISSING,
        boundary_error: str | None = None,
        attestation_error: str | None = None,
    ) -> dict[str, Any]:
        boundary_value = (
            self.boundary_artifact if boundary is _MISSING else boundary
        )
        attestation_value = (
            self.attestation_artifact
            if attestation is _MISSING
            else attestation
        )

        def fake_read_json(path: Path | str) -> tuple[object | None, str | None]:
            value = str(path)
            if value == str(
                resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH
            ):
                return boundary_value, boundary_error
            if value == str(
                resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
            ):
                return attestation_value, attestation_error
            raise AssertionError(f"unexpected JSON read: {path}")

        with patch.object(resolver, "_read_json", side_effect=fake_read_json):
            return self.invoke(request)

    def operation(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result.get(CHECKS_KEY)
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(SUMMARY_KEY)
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        code = block.get("code")
        return code if isinstance(code, str) else block.get("block_code")

    def assert_public_codes(self, result: Mapping[str, Any]) -> None:
        for check in self.checks(result):
            for field in ("failure_code", "block_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        passed = sum(check.get("passed") is True for check in checks)
        failed = sum(check.get("passed") is False for check in checks)
        self.assertEqual(result.get("passed_check_count"), passed)
        self.assertEqual(result.get("failed_check_count"), failed)
        self.assertEqual(len(checks), passed + failed)

    def assert_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(
            set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS)
        )
        operation = self.operation(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[field], False)
            self.assertIs(operation[field], False)
        self.assertIs(
            result.get("result_level_non_claims_canonical_false"), True
        )

    def assert_omission_posture(self, result: Mapping[str, Any]) -> None:
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, dict)
        self.assertEqual(
            set(omission), set(resolver.OMISSION_POSTURE_FIELDS)
        )
        for field in resolver.OMISSION_POSTURE_FIELDS:
            self.assertIs(omission[field], True)
        self.assertFalse(resolver._contains_prohibited_complete_material(result))

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            result.get("operation_result"), resolver.RESULT_NOT_EVALUATED
        )
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertIs(block.get("blocked"), True)
        code = self.block_code(result)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(block.get("code"), block.get("block_code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        operation = self.operation(result)
        self.assertIs(operation["operation_basis_admitted"], False)
        for field in (
            "receiver_answerable_receipt_operation_recorded",
            "receiver_answerable_receipt_operation_result_recorded",
            "receiver_answerable_receipt_operation_exhausted",
            "receiver_answerable_receipt_decided",
            "receiver_answerable_receipt_recorded",
            "receiver_answerable_receipt_not_recorded",
            "receiver_answerable_receipt_indeterminate",
            "receiver_answerable_receipt_present",
        ):
            self.assertIs(operation[field], False)
        self.assertEqual(operation["completed_result_posture_count"], 0)
        self.assert_counts(result)
        self.assert_public_codes(result)
        self.assert_non_claims(result)
        self.assert_omission_posture(result)

    def assert_completed(
        self,
        result: Mapping[str, Any],
        *,
        outcome: str,
        operation_result: str,
        selected_branch: str,
        receipt_present: bool,
        decision_code: str,
        decision_reason: str,
    ) -> None:
        self.assertEqual(result.get("outcome"), outcome)
        self.assertEqual(result.get("operation_result"), operation_result)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, Mapping)
        self.assertEqual(
            dict(block),
            {
                "blocked": False,
                "code": None,
                "block_code": None,
                "reason": None,
            },
        )
        operation = self.operation(result)
        self.assertIs(operation["operation_basis_supplied"], True)
        self.assertIs(operation["operation_basis_admitted"], True)
        for field in (
            "receiver_answerable_receipt_operation_recorded",
            "receiver_answerable_receipt_operation_result_recorded",
            "receiver_answerable_receipt_operation_exhausted",
            "receiver_answerable_receipt_decided",
        ):
            self.assertIs(operation[field], True)
        branch_fields = (
            "receiver_answerable_receipt_recorded",
            "receiver_answerable_receipt_not_recorded",
            "receiver_answerable_receipt_indeterminate",
        )
        for field in branch_fields:
            self.assertIs(operation[field], field == selected_branch)
        self.assertIs(
            operation["receiver_answerable_receipt_present"],
            receipt_present,
        )
        self.assertEqual(operation["completed_result_posture_count"], 1)
        decision = result["operation_decision"]
        self.assertEqual(decision["decision_code"], decision_code)
        self.assertEqual(decision["decision_reason"], decision_reason)
        self.assert_counts(result)
        self.assert_public_codes(result)
        self.assert_non_claims(result)
        self.assert_omission_posture(result)

    def mutate_path(
        self,
        value: dict[str, Any],
        path: tuple[str, ...],
        replacement: object,
    ) -> None:
        target: dict[str, Any] = value
        for field in path[:-1]:
            nested = target[field]
            self.assertIsInstance(nested, dict)
            target = nested
        if replacement is _DELETE:
            target.pop(path[-1])
        else:
            target[path[-1]] = copy.deepcopy(replacement)

    def compact_validation_states(
        self,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        request = self.canonical_request()
        checks: list[dict[str, Any]] = []
        boundary_code, _, boundary = resolver._validate_boundary_artifact(
            request, checks
        )
        attestation_code, _, attestation = (
            resolver._validate_attestation_artifact(request, checks)
        )
        self.assertIsNone(boundary_code)
        self.assertIsNone(attestation_code)
        self.assertIs(boundary["artifact_validated"], True)
        self.assertIs(attestation["artifact_validated"], True)
        return boundary, attestation

    def test_public_api_constants_and_exact_paths(self) -> None:
        for name in (
            "build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request",
            "build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_from_path",
            "build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_summary",
            "write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result",
            "ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        expected = {
            "RESOLVER_MODULE": (
                "resolve_receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min"
            ),
            "RESULT_VERSION": "0.1.0",
            "OPERATION_ID": (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_001"
            ),
            "OPERATION_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
            ),
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": (
                "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
                "RECEIVER_ATTESTATION_RESULT_ONLY"
            ),
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ID": (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_001"
            ),
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
            ),
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_VERSION": "0.1.0",
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_SCOPE": (
                "CONSIDER_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
                "RECEIVER_ATTESTATION_RESULT_ONLY"
            ),
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_OUTCOME_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ALLOWED"
            ),
            "UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_RESULT_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_ALLOWED"
            ),
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ID": (
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_001"
            ),
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ATTESTATION_OPERATION"
            ),
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_VERSION": "0.1.0",
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_SCOPE": (
                "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
                "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
            ),
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_RESULT_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
            ),
            "CANDIDATE_ID": "receiver_side_answerable_basis_candidate_001",
            "CANDIDATE_TYPE": "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE",
            "CANDIDATE_SCOPE": (
                "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_"
                "BASIS_CANDIDATE_ONLY"
            ),
            "ADMISSIBLE_FUTURE_ROUTE": (
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_THEN_SEPARATE_"
                "PRESENCE_RE_EVALUATION_BOUNDARY_ONLY_IF_"
                "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
            ),
        }
        for name, value in expected.items():
            self.assertEqual(getattr(resolver, name), value)
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_INDETERMINATE,
                resolver.OUTCOME_BLOCKED,
            ),
        )
        self.assertEqual(
            resolver.RESULT_FAMILY,
            (
                resolver.RESULT_RECORDED,
                resolver.RESULT_NOT_RECORDED,
                resolver.RESULT_INDETERMINATE,
                resolver.RESULT_NOT_EVALUATED,
            ),
        )
        self.assertEqual(
            resolver.GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH,
            Path(
                "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_SPEC.md"
            ),
        )
        self.assertEqual(
            resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH,
            Path(
                "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_v0_min/"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_001__"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_v0_min_result.json"
            ),
        )
        self.assertEqual(
            resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH,
            Path(
                "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_"
                "receiver_attestation_operation_v0_min/"
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_001__receiver_side_answerable_basis_"
                "receiver_attestation_operation_v0_min_result_001.json"
            ),
        )
        self.assertEqual(
            resolver.OUTPUT_ROOT,
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_001__"
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_v0_min_result.json",
        )

    def test_canonical_request_and_declared_override_visibility(self) -> None:
        first = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request()
        )
        second = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request()
        )
        self.assertIsInstance(first, dict)
        self.assertEqual(set(first), resolver._request_keys())
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"], second["declared_non_claims"]
        )
        self.assertEqual(
            {
                field: first[field]
                for field in resolver.DECISION_INPUT_FIELDS
            },
            dict(resolver.CANONICAL_DECISION_INPUTS),
        )
        self.assertTrue(
            all(first[field] is False for field in resolver.PROHIBITED_REQUEST_FLAGS)
        )
        self.assertEqual(
            set(first["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                first["declared_non_claims"][field] is False
                for field in resolver.REQUIRED_FALSE_NON_CLAIMS
            )
        )
        first["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        third = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_request()
        )
        self.assertIs(
            third["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

        branch_overrides = (
            (
                {"receiver_answerable_receipt_recording_selected": False},
                resolver.OUTCOME_NOT_RECORDED,
            ),
            (
                {"receipt_recording_ambiguity_present": True},
                resolver.OUTCOME_INDETERMINATE,
            ),
            (
                {"receipt_recording_unresolved": True},
                resolver.OUTCOME_INDETERMINATE,
            ),
            (
                {"receipt_recording_contradiction_present": True},
                resolver.OUTCOME_NOT_RECORDED,
            ),
        )
        for overrides, outcome in branch_overrides:
            with self.subTest(overrides=overrides):
                request = self.canonical_request(**overrides)
                self.assertEqual(
                    {field: request[field] for field in overrides}, overrides
                )
                self.assertEqual(self.invoke(request)["outcome"], outcome)

        unknown = self.canonical_request(unknown_override={"visible": True})
        self.assertEqual(unknown["unknown_override"], {"visible": True})
        self.assert_blocked(
            self.invoke(unknown), "REQUEST_UNKNOWN_FIELD"
        )
        malformed = self.canonical_request(operation_id=None)
        self.assertIsNone(malformed["operation_id"])
        self.assert_blocked(
            self.invoke(malformed), "REQUEST_VALUE_MISMATCH"
        )

    def test_exact_boolean_request_matrix(self) -> None:
        for field in resolver.DECISION_INPUT_FIELDS:
            for valid in (True, False):
                with self.subTest(field=field, valid=valid):
                    result = self.invoke(self.canonical_request(**{field: valid}))
                    self.assertNotEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
            for index, invalid in enumerate(INVALID_BOOLEAN_VALUES):
                with self.subTest(field=field, invalid=index):
                    result = self.invoke(
                        self.canonical_request(**{field: invalid})
                    )
                    self.assert_blocked(result, "REQUEST_BOOLEAN_INVALID")

        for field, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
            with self.subTest(prohibited=field, value=True):
                self.assert_blocked(
                    self.invoke(self.canonical_request(**{field: True})),
                    expected_code,
                )
            for index, invalid in enumerate(INVALID_BOOLEAN_VALUES):
                with self.subTest(prohibited=field, invalid=index):
                    self.assert_blocked(
                        self.invoke(
                            self.canonical_request(**{field: invalid})
                        ),
                        "REQUEST_BOOLEAN_INVALID",
                    )

        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            request = self.canonical_request()
            request["declared_non_claims"][field] = True
            with self.subTest(non_claim=field, value=True):
                self.assert_blocked(
                    self.invoke(request), "NON_CLAIM_MISSING_OR_FLIPPED"
                )
            for index, invalid in enumerate(INVALID_BOOLEAN_VALUES):
                request = self.canonical_request()
                request["declared_non_claims"][field] = copy.deepcopy(invalid)
                with self.subTest(non_claim=field, invalid=index):
                    self.assert_blocked(
                        self.invoke(request),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )
            request = self.canonical_request()
            request["declared_non_claims"].pop(field)
            with self.subTest(non_claim=field, missing=True):
                self.assert_blocked(
                    self.invoke(request), "NON_CLAIM_MISSING_OR_FLIPPED"
                )

    def test_recorded_not_recorded_indeterminate_and_blocked_branches(
        self,
    ) -> None:
        recorded_reason = (
            "exact allowed receipt boundary and exact recorded receiver "
            "attestation admitted and one receiver-answerable receipt recorded"
        )
        not_recorded_reason = (
            "bounded receipt operation completed without recording a "
            "receiver-answerable receipt"
        )
        indeterminate_reason = (
            "bounded receipt operation could not lawfully determine whether "
            "a receiver-answerable receipt should be recorded"
        )
        cases = (
            (
                "recorded",
                self.canonical_request(),
                resolver.OUTCOME_RECORDED,
                resolver.RESULT_RECORDED,
                "receiver_answerable_receipt_recorded",
                True,
                "RECEIVER_ANSWERABLE_RECEIPT_RECORDED",
                recorded_reason,
            ),
            (
                "not_selected",
                self.canonical_request(
                    receiver_answerable_receipt_recording_selected=False
                ),
                resolver.OUTCOME_NOT_RECORDED,
                resolver.RESULT_NOT_RECORDED,
                "receiver_answerable_receipt_not_recorded",
                False,
                "RECEIVER_ANSWERABLE_RECEIPT_NOT_RECORDED",
                not_recorded_reason,
            ),
            (
                "contradiction",
                self.canonical_request(
                    receipt_recording_contradiction_present=True
                ),
                resolver.OUTCOME_NOT_RECORDED,
                resolver.RESULT_NOT_RECORDED,
                "receiver_answerable_receipt_not_recorded",
                False,
                "RECEIVER_ANSWERABLE_RECEIPT_NOT_RECORDED",
                not_recorded_reason,
            ),
            (
                "ambiguity",
                self.canonical_request(
                    receipt_recording_ambiguity_present=True
                ),
                resolver.OUTCOME_INDETERMINATE,
                resolver.RESULT_INDETERMINATE,
                "receiver_answerable_receipt_indeterminate",
                False,
                "RECEIVER_ANSWERABLE_RECEIPT_INDETERMINATE",
                indeterminate_reason,
            ),
            (
                "unresolved",
                self.canonical_request(receipt_recording_unresolved=True),
                resolver.OUTCOME_INDETERMINATE,
                resolver.RESULT_INDETERMINATE,
                "receiver_answerable_receipt_indeterminate",
                False,
                "RECEIVER_ANSWERABLE_RECEIPT_INDETERMINATE",
                indeterminate_reason,
            ),
        )
        for (
            label,
            request,
            outcome,
            operation_result,
            branch,
            present,
            code,
            reason,
        ) in cases:
            with self.subTest(branch=label):
                self.assert_completed(
                    self.invoke(request),
                    outcome=outcome,
                    operation_result=operation_result,
                    selected_branch=branch,
                    receipt_present=present,
                    decision_code=code,
                    decision_reason=reason,
                )

        blocked = self.invoke(
            self.canonical_request(intent=resolver.INTENT_BLOCK)
        )
        self.assert_blocked(blocked, "EXPLICIT_BLOCK_REQUESTED")
        malformed = self.canonical_request()
        malformed.pop("operation_id")
        self.assert_blocked(
            self.invoke(malformed), "REQUEST_FIELD_MISSING"
        )

    def test_precedence_and_completed_branch_cardinality(self) -> None:
        cases = (
            (
                "ambiguity_over_all",
                {
                    "receipt_recording_ambiguity_present": True,
                    "receipt_recording_unresolved": False,
                    "receipt_recording_contradiction_present": True,
                    "receiver_answerable_receipt_recording_selected": False,
                },
                resolver.OUTCOME_INDETERMINATE,
            ),
            (
                "unresolved_over_all",
                {
                    "receipt_recording_ambiguity_present": False,
                    "receipt_recording_unresolved": True,
                    "receipt_recording_contradiction_present": True,
                    "receiver_answerable_receipt_recording_selected": False,
                },
                resolver.OUTCOME_INDETERMINATE,
            ),
            (
                "contradiction_over_recorded",
                {"receipt_recording_contradiction_present": True},
                resolver.OUTCOME_NOT_RECORDED,
            ),
            (
                "false_selection_over_recorded",
                {"receiver_answerable_receipt_recording_selected": False},
                resolver.OUTCOME_NOT_RECORDED,
            ),
            (
                "blocked_over_decision_inputs",
                {
                    "intent": resolver.INTENT_BLOCK,
                    "receipt_recording_ambiguity_present": True,
                    "receipt_recording_unresolved": True,
                    "receipt_recording_contradiction_present": True,
                    "receiver_answerable_receipt_recording_selected": False,
                },
                resolver.OUTCOME_BLOCKED,
            ),
        )
        for label, overrides, expected in cases:
            with self.subTest(case=label):
                result = self.invoke(self.canonical_request(**overrides))
                self.assertEqual(result["outcome"], expected)
                operation = self.operation(result)
                completed = [
                    operation["receiver_answerable_receipt_recorded"],
                    operation["receiver_answerable_receipt_not_recorded"],
                    operation["receiver_answerable_receipt_indeterminate"],
                ]
                expected_count = 0 if expected == resolver.OUTCOME_BLOCKED else 1
                self.assertEqual(sum(value is True for value in completed), expected_count)
                self.assertEqual(
                    operation["completed_result_posture_count"],
                    expected_count,
                )

    def test_specification_validation_matrix_and_required_distinctions(
        self,
    ) -> None:
        required_distinctions = (
            "receiver attestation recorded is not receiver-answerable receipt",
            "receipt consideration allowed is not receipt",
            "Basis admission is not receipt.",
            "receiver-answerable receipt is not presence",
            "Answerability is not custody proof.",
            "Receipt is not custody proof, provenance proof, or "
            "physical-validity proof.",
            "presence re-evaluation boundary",
            "All contaminated lineage remains unchanged.",
            "Open does not mean next.",
        )
        for marker in required_distinctions:
            self.assertIn(marker, self.specification_text)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.copy_fixture_root(root)
            spec_path = (
                root / resolver.GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
            )
            spec_path.unlink()
            self.assert_blocked(
                self.invoke(root=root), "OPERATION_SPEC_REFERENCE_MISSING"
            )
            spec_path.mkdir()
            self.assert_blocked(
                self.invoke(root=root), "OPERATION_SPEC_REFERENCE_MISSING"
            )
            spec_path.rmdir()

            for family, markers in resolver.SPEC_MARKER_FAMILIES.items():
                marker = markers[0]
                with self.subTest(marker_family=family):
                    self.assertIn(marker, self.specification_text)
                    self.write_text(
                        spec_path,
                        self.specification_text.replace(marker, ""),
                    )
                    result = self.invoke(root=root)
                    self.assert_blocked(
                        result, "OPERATION_SPEC_MARKER_MISSING"
                    )
                    self.write_text(spec_path, self.specification_text)

    def test_strict_artifact_json_loading_and_atomic_path_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.copy_fixture_root(root)
            canonical = self.invoke(root=root)
            self.assertEqual(canonical["outcome"], resolver.OUTCOME_RECORDED)
            self.assertIs(
                canonical["atomic_operation_basis_posture"][
                    "operation_basis_supplied"
                ],
                True,
            )
            self.assertIs(
                canonical["atomic_operation_basis_posture"][
                    "operation_basis_admitted"
                ],
                True,
            )

            for label, relative, code in (
                (
                    "boundary",
                    resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH,
                    "RECEIPT_BOUNDARY",
                ),
                (
                    "attestation",
                    resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH,
                    "RECEIVER_ATTESTATION",
                ),
            ):
                path = root / relative
                canonical_bytes = path.read_bytes()
                format_cases = (
                    ("malformed", "{", f"{code}_ARTIFACT_NOT_PARSEABLE"),
                    (
                        "duplicate",
                        '{"resolver_module":"a","resolver_module":"b"}\n',
                        f"{code}_ARTIFACT_NOT_PARSEABLE",
                    ),
                    ("array", "[]\n", f"{code}_ARTIFACT_NOT_MAPPING"),
                )
                for case, text, expected_code in format_cases:
                    with self.subTest(artifact=label, case=case):
                        self.write_text(path, text)
                        self.assert_blocked(
                            self.invoke(root=root), expected_code
                        )
                        path.write_bytes(canonical_bytes)
                with self.subTest(artifact=label, case="missing"):
                    path.unlink()
                    expected_code = f"{code}_ARTIFACT_REFERENCE_MISSING"
                    result = self.invoke(root=root)
                    self.assert_blocked(result, expected_code)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(canonical_bytes)

            one_wrong = self.canonical_request(
                upstream_receiver_answerable_receipt_boundary_artifact_path=(
                    "missing.json"
                )
            )
            result = self.invoke(one_wrong, root=root)
            self.assert_blocked(result, "REQUEST_VALUE_MISMATCH")
            self.assertIs(
                result["atomic_operation_basis_posture"][
                    "operation_basis_supplied"
                ],
                False,
            )
            both_supplied_one_invalid = self.resolve_with_mocked_artifacts(
                boundary=[]
            )
            self.assert_blocked(
                both_supplied_one_invalid,
                "RECEIPT_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )
            self.assertIs(
                both_supplied_one_invalid["atomic_operation_basis_posture"][
                    "operation_basis_supplied"
                ],
                True,
            )
            self.assertIs(
                both_supplied_one_invalid["atomic_operation_basis_posture"][
                    "operation_basis_admitted"
                ],
                False,
            )
        self.assertNotIn(
            "REQUIRES_OPERATION_BASIS",
            " ".join(resolver.OUTCOME_FAMILY),
        )

    def test_receipt_boundary_artifact_validation_matrix(self) -> None:
        cases: list[tuple[str, tuple[str, ...], object, str]] = [
            (
                "wrong_resolver",
                ("resolver_module",),
                "other",
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "wrong_version",
                ("result_version",),
                "9.9.9",
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "wrong_outcome",
                ("outcome",),
                "other",
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "wrong_result",
                ("boundary_result",),
                "other",
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "failed_checks",
                ("failed_check_count",),
                1,
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "wrong_passed_checks",
                ("passed_check_count",),
                172,
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "blocked",
                ("block", "blocked"),
                True,
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "boundary_id",
                (BOUNDARY_KEY, "boundary_id"),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "boundary_type",
                (BOUNDARY_KEY, "boundary_type"),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "boundary_version",
                (BOUNDARY_KEY, "boundary_version"),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "boundary_scope",
                (BOUNDARY_KEY, "boundary_scope"),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selection",
                ("boundary_decision", "selection"),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "decision_code",
                ("boundary_decision", "decision_code"),
                "other",
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "decision_reason",
                ("boundary_decision", "decision_reason"),
                "other",
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "cardinality",
                ("boundary_posture", "completed_consideration_posture_count"),
                2,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "boundary_not_recorded",
                (
                    "boundary_posture",
                    "receiver_answerable_receipt_boundary_recorded",
                ),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "boundary_result_not_recorded",
                (
                    "boundary_posture",
                    "receiver_answerable_receipt_boundary_result_recorded",
                ),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "boundary_not_exhausted",
                (
                    "boundary_posture",
                    "receiver_answerable_receipt_boundary_exhausted",
                ),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "consideration_not_allowed",
                (
                    "boundary_posture",
                    "receiver_answerable_receipt_consideration_not_allowed",
                ),
                True,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "receipt_not_absent",
                (BOUNDARY_SUMMARY_KEY, "receipt_absent"),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "receipt_operation_not_absent",
                (BOUNDARY_SUMMARY_KEY, "receipt_operation_absent"),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "presence_not_absent",
                (BOUNDARY_SUMMARY_KEY, "presence_absent"),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "downstream_nonclaims_not_validated",
                (
                    BOUNDARY_SUMMARY_KEY,
                    "downstream_non_claims_canonical_false",
                ),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "result_nonclaims_not_validated",
                ("result_level_non_claims_canonical_false",),
                False,
                "RECEIPT_BOUNDARY_METADATA_MISMATCH",
            ),
            (
                "omission_not_validated",
                (
                    BOUNDARY_SUMMARY_KEY,
                    "complete_material_omission_posture",
                ),
                False,
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
            (
                "selected_operation_id",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_receiver_attestation_operation_id",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_operation_type",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_receiver_attestation_operation_type",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_operation_version",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_receiver_attestation_operation_version",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_operation_scope",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_receiver_attestation_operation_scope",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_id",
                (
                    "selected_operation_and_candidate_identity",
                    "receiver_side_answerable_basis_candidate_id",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_type",
                (
                    "selected_operation_and_candidate_identity",
                    "receiver_side_answerable_basis_candidate_type",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_scope",
                (
                    "selected_operation_and_candidate_identity",
                    "receiver_side_answerable_basis_candidate_scope",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "selected_artifact_path",
                (
                    "receiver_side_answerable_basis_"
                    "receiver_answerable_receipt_boundary_metadata",
                    "selected_upstream_artifact_path",
                ),
                "other",
                "RECEIPT_BOUNDARY_IDENTITY_MISMATCH",
            ),
            (
                "future_route",
                (BOUNDARY_KEY, "admissible_future_route"),
                "other",
                "RECEIPT_BOUNDARY_POSTURE_INVALID",
            ),
        ]
        for label, path, replacement, code in cases:
            with self.subTest(case=label):
                artifact = copy.deepcopy(self.boundary_artifact)
                self.mutate_path(artifact, path, replacement)
                self.assert_blocked(
                    self.resolve_with_mocked_artifacts(boundary=artifact),
                    code,
                )

    def test_every_receipt_boundary_false_lock_is_exact_false(self) -> None:
        invalid_values = (True, None, "false", 0, [], {})
        for location in ("non_claims", BOUNDARY_KEY):
            for field in resolver.BOUNDARY_REQUIRED_FALSE_LOCKS:
                for index, invalid in enumerate(invalid_values):
                    with self.subTest(
                        location=location, field=field, invalid=index
                    ):
                        artifact = copy.deepcopy(self.boundary_artifact)
                        self.mutate_path(
                            artifact, (location, field), invalid
                        )
                        self.assert_blocked(
                            self.resolve_with_mocked_artifacts(
                                boundary=artifact
                            ),
                            "RECEIPT_BOUNDARY_FALSE_LOCK_NOT_FALSE",
                        )
                with self.subTest(
                    location=location, field=field, missing=True
                ):
                    artifact = copy.deepcopy(self.boundary_artifact)
                    self.mutate_path(
                        artifact, (location, field), _DELETE
                    )
                    self.assert_blocked(
                        self.resolve_with_mocked_artifacts(
                            boundary=artifact
                        ),
                        "RECEIPT_BOUNDARY_FALSE_LOCK_NOT_FALSE",
                    )

    def test_receiver_attestation_artifact_validation_matrix(self) -> None:
        cases: list[tuple[str, tuple[str, ...], object, str]] = [
            (
                "wrong_resolver",
                ("resolver_module",),
                "other",
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "wrong_version",
                ("result_version",),
                "other",
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "wrong_outcome",
                ("outcome",),
                "other",
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "failed_checks",
                ("failed_check_count",),
                1,
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "wrong_passed_checks",
                ("passed_check_count",),
                159,
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "blocked",
                ("block", "blocked"),
                True,
                "RECEIVER_ATTESTATION_METADATA_MISMATCH",
            ),
            (
                "operation_id",
                (ATTESTATION_KEY, "operation_id"),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_type",
                (ATTESTATION_KEY, "operation_type"),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_version",
                (ATTESTATION_KEY, "operation_version"),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_scope",
                (ATTESTATION_KEY, "operation_scope"),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_result",
                (ATTESTATION_KEY, "receiver_attestation_operation_result"),
                "other",
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "basis_supplied",
                (ATTESTATION_KEY, "operation_basis_supplied"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "basis_admitted",
                (ATTESTATION_KEY, "operation_basis_admitted"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "operation_not_recorded",
                (
                    ATTESTATION_KEY,
                    "receiver_attestation_operation_recorded",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "result_not_recorded",
                (
                    ATTESTATION_KEY,
                    "receiver_attestation_operation_result_recorded",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "not_exhausted",
                (
                    ATTESTATION_KEY,
                    "receiver_attestation_operation_exhausted",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "not_decided",
                (ATTESTATION_KEY, "receiver_attestation_decided"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "not_recorded",
                (ATTESTATION_KEY, "receiver_attestation_recorded"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "negative_result_true",
                (ATTESTATION_KEY, "receiver_attestation_not_recorded"),
                True,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "indeterminate_true",
                (ATTESTATION_KEY, "receiver_attestation_indeterminate"),
                True,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "cardinality",
                ("operation_result_detail", "completed_result_posture_count"),
                2,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "result_present",
                (ATTESTATION_KEY + "_non_meaning", "operation_result_present"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "minimum_checks",
                ("bounded_component_validation", "minimum_admission_checks_passed"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "archive_correspondence",
                (
                    "bounded_component_validation",
                    "archive_validation",
                    "correspondence_validated",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "text_components",
                ("bounded_component_validation", "text_components_validated"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "timestamp",
                ("bounded_component_validation", "timestamp_validated"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "trace_paths",
                ("bounded_component_validation", "trace_paths_validated"),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "signal_existence",
                (
                    "bounded_component_validation",
                    "recorded_signal_artifact_existence_validated",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "result_nonclaims",
                (
                    ATTESTATION_SUMMARY_KEY,
                    "result_level_non_claims_canonical_false",
                ),
                False,
                "RECEIVER_ATTESTATION_POSTURE_INVALID",
            ),
            (
                "candidate_id",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_candidate_id",
                ),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "candidate_type",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_candidate_type",
                ),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
            (
                "candidate_scope",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_candidate_scope",
                ),
                "other",
                "RECEIVER_ATTESTATION_IDENTITY_MISMATCH",
            ),
        ]
        for label, path, replacement, code in cases:
            with self.subTest(case=label):
                artifact = copy.deepcopy(self.attestation_artifact)
                self.mutate_path(artifact, path, replacement)
                self.assert_blocked(
                    self.resolve_with_mocked_artifacts(
                        attestation=artifact
                    ),
                    code,
                )

    def test_every_receiver_attestation_false_lock_is_exact_false(
        self,
    ) -> None:
        invalid_values = (True, None, "false", 0, [], {})
        for location in ("non_claims", ATTESTATION_KEY):
            for field in resolver.ATTESTATION_REQUIRED_FALSE_LOCKS:
                for index, invalid in enumerate(invalid_values):
                    with self.subTest(
                        location=location, field=field, invalid=index
                    ):
                        artifact = copy.deepcopy(self.attestation_artifact)
                        self.mutate_path(
                            artifact, (location, field), invalid
                        )
                        self.assert_blocked(
                            self.resolve_with_mocked_artifacts(
                                attestation=artifact
                            ),
                            "RECEIVER_ATTESTATION_FALSE_LOCK_NOT_FALSE",
                        )
                with self.subTest(
                    location=location, field=field, missing=True
                ):
                    artifact = copy.deepcopy(self.attestation_artifact)
                    self.mutate_path(
                        artifact, (location, field), _DELETE
                    )
                    self.assert_blocked(
                        self.resolve_with_mocked_artifacts(
                            attestation=artifact
                        ),
                        "RECEIVER_ATTESTATION_FALSE_LOCK_NOT_FALSE",
                    )

    def test_cross_artifact_correspondence_and_atomic_admission_matrix(
        self,
    ) -> None:
        clean_boundary, clean_attestation = self.compact_validation_states()
        cases = (
            (
                "operation_id",
                "boundary",
                (
                    "selected_operation_identity",
                    "selected_receiver_attestation_operation_id",
                ),
            ),
            (
                "operation_type",
                "boundary",
                (
                    "selected_operation_identity",
                    "selected_receiver_attestation_operation_type",
                ),
            ),
            (
                "operation_version",
                "boundary",
                (
                    "selected_operation_identity",
                    "selected_receiver_attestation_operation_version",
                ),
            ),
            (
                "operation_scope",
                "boundary",
                (
                    "selected_operation_identity",
                    "selected_receiver_attestation_operation_scope",
                ),
            ),
            (
                "candidate_id",
                "attestation",
                (
                    "selected_candidate_identity",
                    "receiver_side_answerable_basis_candidate_id",
                ),
            ),
            (
                "candidate_type",
                "attestation",
                (
                    "selected_candidate_identity",
                    "receiver_side_answerable_basis_candidate_type",
                ),
            ),
            (
                "candidate_scope",
                "attestation",
                (
                    "selected_candidate_identity",
                    "receiver_side_answerable_basis_candidate_scope",
                ),
            ),
            (
                "attestation_result",
                "attestation",
                ("operation_result",),
            ),
            (
                "attestation_path",
                "boundary",
                ("selected_upstream_artifact_path",),
            ),
            (
                "boundary_allowed",
                "boundary",
                ("boundary_allowed_validated",),
            ),
            (
                "attestation_recorded",
                "attestation",
                ("receiver_attestation_recorded",),
            ),
            (
                "boundary_cardinality",
                "boundary",
                ("completed_consideration_posture_count",),
            ),
            (
                "attestation_cardinality",
                "attestation",
                ("completed_result_posture_count",),
            ),
            (
                "boundary_completion",
                "boundary",
                ("boundary_completion_validated",),
            ),
            (
                "attestation_exhaustion",
                "attestation",
                ("operation_completed_and_exhausted",),
            ),
            (
                "boundary_false_locks",
                "boundary",
                ("upstream_false_locks_validated",),
            ),
            (
                "attestation_false_locks",
                "attestation",
                ("upstream_false_locks_validated",),
            ),
        )
        for label, target_name, path in cases:
            with self.subTest(case=label):
                boundary = copy.deepcopy(clean_boundary)
                attestation = copy.deepcopy(clean_attestation)
                target = boundary if target_name == "boundary" else attestation
                current: object = target
                for field in path:
                    self.assertIsInstance(current, dict)
                    current = current[field]
                replacement: object
                if type(current) is bool:
                    replacement = not current
                elif type(current) is int:
                    replacement = current + 1
                else:
                    replacement = "mismatch"
                self.mutate_path(target, path, replacement)
                with (
                    patch.object(
                        resolver,
                        "_validate_boundary_artifact",
                        return_value=(None, None, boundary),
                    ),
                    patch.object(
                        resolver,
                        "_validate_attestation_artifact",
                        return_value=(None, None, attestation),
                    ),
                ):
                    result = self.invoke()
                self.assert_blocked(
                    result, "UPSTREAM_CORRESPONDENCE_MISMATCH"
                )
                self.assertIs(
                    result["atomic_operation_basis_posture"][
                        "operation_basis_supplied"
                    ],
                    True,
                )
                self.assertIs(
                    result["atomic_operation_basis_posture"][
                        "operation_basis_admitted"
                    ],
                    False,
                )

        with (
            patch.object(
                resolver,
                "_validate_boundary_artifact",
                return_value=(None, None, clean_boundary),
            ),
            patch.object(
                resolver,
                "_validate_attestation_artifact",
                return_value=(None, None, clean_attestation),
            ),
        ):
            recorded = self.invoke()
        self.assertEqual(recorded["outcome"], resolver.OUTCOME_RECORDED)
        self.assertIs(
            recorded["atomic_operation_basis_posture"][
                "basis_admission_is_not_receipt"
            ],
            True,
        )

    def test_request_schema_preclaims_nonclaims_and_public_codes(self) -> None:
        cases: list[tuple[str, object, str]] = [
            ("non_mapping", [], "REQUEST_NOT_MAPPING"),
            (
                "unsupported_intent",
                self.canonical_request(intent="UNSUPPORTED"),
                "UNSUPPORTED_INTENT",
            ),
            (
                "explicit_block",
                self.canonical_request(intent=resolver.INTENT_BLOCK),
                "EXPLICIT_BLOCK_REQUESTED",
            ),
            (
                "unknown",
                self.canonical_request(unknown=True),
                "REQUEST_UNKNOWN_FIELD",
            ),
        ]
        missing = self.canonical_request()
        missing.pop("operation_scope")
        cases.append(("missing", missing, "REQUEST_FIELD_MISSING"))
        for field in (
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "governing_receiver_answerable_receipt_operation_specification_path",
            "upstream_receiver_answerable_receipt_boundary_artifact_path",
            "selected_receiver_attestation_operation_artifact_path",
            "upstream_receiver_answerable_receipt_boundary_id",
            "selected_receiver_attestation_operation_id",
            "receiver_side_answerable_basis_candidate_id",
            "admissible_future_route",
        ):
            cases.append(
                (
                    "mismatch_" + field,
                    self.canonical_request(**{field: "other"}),
                    "REQUEST_VALUE_MISMATCH",
                )
            )
        for field, value in (
            ("outcome", resolver.OUTCOME_RECORDED),
            ("operation_result", resolver.RESULT_RECORDED),
            ("completed_result_posture_count", 1),
            ("receiver_answerable_receipt_recorded", True),
            ("receiver_answerable_receipt_present", True),
            ("complete_receipt_boundary_artifact", {}),
            ("archive_bytes", "embedded"),
            ("recorded_signal_body", {}),
        ):
            cases.append(
                (
                    "preclaim_" + field,
                    self.canonical_request(**{field: value}),
                    "RESULT_POSTURE_PRECLAIMED",
                )
            )
        for label, request, code in cases:
            with self.subTest(case=label):
                self.assert_blocked(self.invoke(request), code)

    def test_read_limits_no_discovery_and_no_source_body_reads(self) -> None:
        original_read_text = Path.read_text
        allowed = (
            SPECIFICATION_PATH.resolve(),
            BOUNDARY_ARTIFACT_PATH.resolve(),
            ATTESTATION_ARTIFACT_PATH.resolve(),
        )
        opened: list[Path] = []

        def bounded_read_text(
            path: Path, *args: object, **kwargs: object
        ) -> str:
            resolved = Path(path).resolve()
            if resolved not in allowed:
                raise AssertionError(f"prohibited read: {resolved}")
            opened.append(resolved)
            return original_read_text(path, *args, **kwargs)

        with (
            patch.object(Path, "read_text", bounded_read_text),
            patch.object(
                Path,
                "glob",
                side_effect=AssertionError("glob prohibited"),
            ),
            patch.object(
                Path,
                "rglob",
                side_effect=AssertionError("rglob prohibited"),
            ),
            patch.object(
                Path,
                "iterdir",
                side_effect=AssertionError("iterdir prohibited"),
            ),
            patch(
                "os.listdir",
                side_effect=AssertionError("os.listdir prohibited"),
            ),
        ):
            result = self.invoke()
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(opened, list(allowed))
        prohibited_fragments = (
            "actual_receiver_attestation_capture",
            "candidate_sufficiency",
            "receiver_attestation_boundary",
            "original_zip",
            ".sha256",
            "attestation_statement.txt",
            "knock_20260727_215052.json",
        )
        for path in opened:
            for fragment in prohibited_fragments:
                self.assertNotIn(fragment, str(path))

    def test_from_path_strict_json_and_request_immutability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request = self.canonical_request()
            request_path = self.write_json(root / "request.json", request)
            before_hash = self.sha256(request_path)
            direct = self.invoke(request)
            from_path = (
                resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_from_path(
                    request_path
                )
            )
            self.assertEqual(from_path, direct)
            self.assertEqual(self.sha256(request_path), before_hash)

            duplicate = self.write_text(
                root / "duplicate.json",
                '{"intent":"a","intent":"b"}\n',
            )
            malformed = self.write_text(root / "malformed.json", "{")
            array = self.write_json(root / "array.json", [])
            invalid_utf8 = root / "invalid_utf8.json"
            invalid_utf8.write_bytes(b"\xff")
            missing = root / "missing.json"
            for path in (
                duplicate,
                malformed,
                array,
                invalid_utf8,
                missing,
            ):
                with self.subTest(path=path.name):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError
                    ):
                        resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_from_path(
                            path
                        )

    def test_nonclaims_omissions_nonmeaning_and_blocked_routes(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_recording_selected=False
                )
            ),
            self.invoke(
                self.canonical_request(
                    receipt_recording_ambiguity_present=True
                )
            ),
            self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK)
            ),
        )
        expected_statement = {
            "occurrence_is_not_trace",
            "trace_is_not_candidate_reception",
            "candidate_sufficiency_is_not_receiver_attestation",
            "receiver_attestation_recorded_is_not_receipt",
            "receipt_consideration_allowed_is_not_receipt",
            "receipt_boundary_is_not_receipt_operation",
            "operation_request_is_not_operation_result",
            "operation_basis_admission_is_not_receipt",
            "receipt_recorded_is_not_independent_occurrence_verification",
            "receipt_recorded_is_not_identity_proof",
            "receipt_recorded_is_not_custody_proof",
            "receipt_recorded_is_not_provenance_proof",
            "receipt_recorded_is_not_physical_validity_proof",
            "receipt_is_not_presence",
            "operation_exhaustion_is_not_presence_re_evaluation",
            "completed_operation_is_not_downstream_authorization",
            "open_does_not_mean_next",
        }
        expected_non_meaning = {
            "not_recorded_is_not_attestation_falsity",
            "not_recorded_is_not_receiver_dishonesty",
            "not_recorded_is_not_occurrence_denial",
            "not_recorded_is_not_candidate_insufficiency",
            "not_recorded_is_not_boundary_failure",
            "not_recorded_is_not_presence_denial",
            "not_recorded_is_not_refusal",
            "not_recorded_is_not_debt_or_obligation",
            "indeterminate_does_not_create_retry",
            "indeterminate_does_not_create_debt",
            "indeterminate_does_not_create_obligation",
            "indeterminate_does_not_create_scheduled_work",
            "indeterminate_does_not_create_automatic_next",
        }
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_non_claims(result)
                self.assert_omission_posture(result)
                statement = result[STATEMENT_KEY]
                self.assertEqual(set(statement), expected_statement)
                self.assertTrue(all(statement[field] is True for field in statement))
                non_meaning = result[NON_MEANING_KEY]
                self.assertTrue(
                    all(
                        non_meaning[field] is True
                        for field in expected_non_meaning
                    )
                )
                self.assertEqual(
                    result["blocked_routes"], list(resolver.BLOCKED_ROUTES)
                )
                self.assertEqual(
                    result["admissible_future_route"],
                    resolver.ADMISSIBLE_FUTURE_ROUTE,
                )
                serialized = json.dumps(result, sort_keys=True)
                self.assertNotIn("signal_samples", serialized)
                self.assertNotIn("raw_signal_data", serialized)

    def test_summary_determinism_and_exact_compact_posture(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_recording_selected=False
                )
            ),
            self.invoke(
                self.canonical_request(
                    receipt_recording_unresolved=True
                )
            ),
            self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK)
            ),
        )
        required_summary_fields = (
            "resolver_module",
            "result_version",
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "specification_path",
            "receipt_boundary_artifact_path",
            "receiver_attestation_artifact_path",
            "upstream_boundary_id",
            "selected_attestation_operation_id",
            "selected_candidate_id",
            "outcome",
            "operation_result",
            "failed_check_count",
            "passed_check_count",
            "blocked",
            "decision_code",
            "decision_reason",
            "operation_basis_supplied",
            "operation_basis_admitted",
            "specification_validated",
            "receipt_boundary_artifact_validated",
            "receiver_attestation_artifact_validated",
            "upstream_correspondence_validated",
            "boundary_allowed_validated",
            "attestation_recorded_validated",
            "boundary_cardinality_validated",
            "attestation_cardinality_validated",
            "receiver_answerable_receipt_operation_recorded",
            "receiver_answerable_receipt_operation_result_recorded",
            "receiver_answerable_receipt_operation_exhausted",
            "receiver_answerable_receipt_decided",
            "receiver_answerable_receipt_recorded",
            "receiver_answerable_receipt_not_recorded",
            "receiver_answerable_receipt_indeterminate",
            "receiver_answerable_receipt_present",
            "completed_result_posture_count",
            "receipt_support_absent",
            "presence_re_evaluation_absent",
            "presence_absent",
            "identity_absent",
            "custody_proof_absent",
            "provenance_proof_absent",
            "physical_validity_proof_absent",
            "downstream_non_claims_canonical_false",
            "result_level_non_claims_canonical_false",
            "complete_material_omission_posture",
            "admissible_future_route",
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                before = copy.deepcopy(result)
                first = (
                    resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_summary(
                        result
                    )
                )
                second = (
                    resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(first, second)
                self.assertEqual(first, self.summary(result))
                self.assertEqual(result, before)
                self.assertEqual(set(first), set(required_summary_fields))
                self.assertEqual(first["resolver_module"], resolver.RESOLVER_MODULE)
                self.assertEqual(first["result_version"], resolver.RESULT_VERSION)
                self.assertEqual(first["operation_id"], resolver.OPERATION_ID)
                self.assertEqual(first["outcome"], result["outcome"])
                self.assertEqual(
                    first["operation_result"], result["operation_result"]
                )
                self.assertEqual(
                    first["failed_check_count"], result["failed_check_count"]
                )
                self.assertEqual(
                    first["passed_check_count"], result["passed_check_count"]
                )
                self.assertNotIn("checks", first)
                self.assertFalse(
                    resolver._contains_prohibited_complete_material(first)
                )

    def test_determinism_immutability_and_environment_independence(self) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        boundary_before = copy.deepcopy(self.boundary_artifact)
        attestation_before = copy.deepcopy(self.attestation_artifact)

        first = self.resolve_with_mocked_artifacts(
            request=request,
            boundary=self.boundary_artifact,
            attestation=self.attestation_artifact,
        )
        second = self.resolve_with_mocked_artifacts(
            request=copy.deepcopy(request),
            boundary=self.boundary_artifact,
            attestation=self.attestation_artifact,
        )
        with patch.dict(
            os.environ,
            {"RECEIPT_OPERATION_TEST_SENTINEL": "must_not_appear"},
            clear=True,
        ):
            third = self.resolve_with_mocked_artifacts(
                request=copy.deepcopy(request),
                boundary=self.boundary_artifact,
                attestation=self.attestation_artifact,
            )
        self.assertEqual(first, second)
        self.assertEqual(first, third)
        self.assertEqual(request, request_before)
        self.assertEqual(self.boundary_artifact, boundary_before)
        self.assertEqual(self.attestation_artifact, attestation_before)
        self.assertNotIn(
            "RECEIPT_OPERATION_TEST_SENTINEL",
            json.dumps(first, sort_keys=True),
        )
        self.assertNotIn("generated_at", json.dumps(first, sort_keys=True))
        self.assertNotIn("resolved_at", json.dumps(first, sort_keys=True))
        self.assertEqual(
            [check["check"] for check in self.checks(first)],
            [check["check"] for check in self.checks(second)],
        )
        self.assert_counts(first)

    def test_writer_valid_branches_format_suffix_and_no_overwrite(self) -> None:
        results = {
            "recorded": self.invoke(),
            "not_recorded": self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_recording_selected=False
                )
            ),
            "indeterminate": self.invoke(
                self.canonical_request(
                    receipt_recording_ambiguity_present=True
                )
            ),
            "blocked": self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK)
            ),
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = (
                root
                / "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min"
            )
            with (
                patch.object(resolver, "REPO_ROOT", root),
                patch.object(resolver, "OUTPUT_ROOT", output_root),
            ):
                for label, result in results.items():
                    with self.subTest(branch=label):
                        target = output_root / label / resolver.OUTPUT_FILENAME
                        written = (
                            resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
                                result, target
                            )
                        )
                        self.assertEqual(written, target)
                        text = written.read_text(encoding="utf-8")
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
                        with self.assertRaises(
                            resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError
                        ):
                            resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
                                result, target
                            )

                default_paths = [
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
                        results["recorded"]
                    )
                    for _ in range(3)
                ]
                self.assertEqual(
                    [path.name for path in default_paths],
                    [
                        resolver.OUTPUT_FILENAME,
                        Path(resolver.OUTPUT_FILENAME).stem
                        + "_001"
                        + Path(resolver.OUTPUT_FILENAME).suffix,
                        Path(resolver.OUTPUT_FILENAME).stem
                        + "_002"
                        + Path(resolver.OUTPUT_FILENAME).suffix,
                    ],
                )
                self.assertEqual(
                    len({path.resolve() for path in default_paths}), 3
                )

    def test_writer_refusal_matrix_and_protected_paths(self) -> None:
        recorded = self.invoke()
        not_recorded = self.invoke(
            self.canonical_request(
                receiver_answerable_receipt_recording_selected=False
            )
        )
        indeterminate = self.invoke(
            self.canonical_request(receipt_recording_unresolved=True)
        )
        blocked = self.invoke(
            self.canonical_request(intent=resolver.INTENT_BLOCK)
        )
        malformed: list[tuple[str, object]] = [("non_mapping", [])]

        def add_mutation(
            label: str,
            source: Mapping[str, Any],
            path: tuple[str, ...],
            replacement: object,
        ) -> None:
            value = copy.deepcopy(dict(source))
            self.mutate_path(value, path, replacement)
            malformed.append((label, value))

        add_mutation(
            "wrong_operation_id",
            recorded,
            (OPERATION_KEY, "operation_id"),
            "other",
        )
        add_mutation(
            "wrong_spec_path",
            recorded,
            (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_metadata",
                "specification_path",
            ),
            "other",
        )
        add_mutation(
            "wrong_boundary_path",
            recorded,
            (
                "receiver_answerable_receipt_boundary_validation",
                "artifact_path",
            ),
            "other",
        )
        add_mutation(
            "wrong_attestation_path",
            recorded,
            (
                "receiver_attestation_operation_validation",
                "artifact_path",
            ),
            "other",
        )
        add_mutation(
            "wrong_outcome",
            recorded,
            ("outcome",),
            resolver.OUTCOME_NOT_RECORDED,
        )
        add_mutation(
            "wrong_operation_result",
            recorded,
            ("operation_result",),
            resolver.RESULT_NOT_RECORDED,
        )
        add_mutation(
            "wrong_count",
            recorded,
            ("passed_check_count",),
            recorded["passed_check_count"] + 1,
        )
        add_mutation(
            "recorded_branch_missing",
            recorded,
            (OPERATION_KEY, "receiver_answerable_receipt_recorded"),
            False,
        )
        add_mutation(
            "recorded_present_false",
            recorded,
            (OPERATION_KEY, "receiver_answerable_receipt_present"),
            False,
        )
        add_mutation(
            "not_recorded_branch_missing",
            not_recorded,
            (OPERATION_KEY, "receiver_answerable_receipt_not_recorded"),
            False,
        )
        add_mutation(
            "not_recorded_present_true",
            not_recorded,
            (OPERATION_KEY, "receiver_answerable_receipt_present"),
            True,
        )
        add_mutation(
            "indeterminate_branch_missing",
            indeterminate,
            (OPERATION_KEY, "receiver_answerable_receipt_indeterminate"),
            False,
        )
        add_mutation(
            "indeterminate_present_true",
            indeterminate,
            (OPERATION_KEY, "receiver_answerable_receipt_present"),
            True,
        )
        add_mutation(
            "blocked_operation_recorded",
            blocked,
            (OPERATION_KEY, "receiver_answerable_receipt_operation_recorded"),
            True,
        )
        add_mutation(
            "blocked_present",
            blocked,
            (OPERATION_KEY, "receiver_answerable_receipt_present"),
            True,
        )
        add_mutation(
            "nonclaim_true",
            recorded,
            ("non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0]),
            True,
        )
        add_mutation(
            "omission_false",
            recorded,
            ("omission_posture", resolver.OMISSION_POSTURE_FIELDS[0]),
            False,
        )
        add_mutation(
            "wrong_future_route",
            recorded,
            ("admissible_future_route",),
            "other",
        )
        complete = copy.deepcopy(recorded)
        complete[
            "receiver_side_answerable_basis_"
            "receiver_answerable_receipt_operation_metadata"
        ]["recorded_signal_body"] = {"samples": [1]}
        malformed.append(("complete_material", complete))

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = (
                root
                / "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min"
            )
            with (
                patch.object(resolver, "REPO_ROOT", root),
                patch.object(resolver, "OUTPUT_ROOT", output_root),
            ):
                for label, value in malformed:
                    with self.subTest(malformed=label):
                        with self.assertRaises(
                            resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError
                        ):
                            resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
                                value,
                                output_root / label / resolver.OUTPUT_FILENAME,
                            )

                protected = (
                    Path("spec") / resolver.OUTPUT_FILENAME,
                    Path("src") / resolver.OUTPUT_FILENAME,
                    Path("tests") / resolver.OUTPUT_FILENAME,
                    Path("reference/IAMMAI") / resolver.OUTPUT_FILENAME,
                    resolver.UPSTREAM_RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ARTIFACT_RELATIVE_PATH,
                    resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH,
                    resolver.ORIGINAL_WAITING_RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
                    Path(
                        "artifacts/integrity_host_v0_min_coexistence_"
                        "receiver_side_answerable_basis_"
                        "receiver_answerable_receipt_boundary_v0_min/"
                        "protected.json"
                    ),
                    Path(
                        "artifacts/integrity_host_v0_min_coexistence_"
                        "receiver_side_answerable_basis_"
                        "receiver_attestation_operation_basis_supply_v0_min/"
                        "protected.json"
                    ),
                    Path(
                        "artifacts/actual_receiver_attestation_capture/"
                        "receiver_attestation_capture_001/protected.json"
                    ),
                    Path(
                        "artifacts/integrity_host_v0_min_coexistence_"
                        "receiver_side_answerable_basis_"
                        "candidate_sufficiency_operation_v0_min/"
                        "protected.json"
                    ),
                    Path(
                        "artifacts/integrity_host_v0_min_coexistence_"
                        "receiver_side_answerable_basis_"
                        "receiver_attestation_boundary_v0_min_v2/"
                        "protected.json"
                    ),
                    Path("artifacts/contaminated_lineage/protected.json"),
                    Path("artifacts/outside_exact_operation_family/result.json"),
                )
                for target in protected:
                    with self.subTest(protected=str(target)):
                        with self.assertRaises(
                            resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptOperationV0MinError
                        ):
                            resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result(
                                recorded, target
                            )
                        self.assertFalse((root / target).exists())

    def test_preserved_hashes_and_no_live_output_change(self) -> None:
        for path, expected in self.preserved_hashes.items():
            with self.subTest(path=str(path)):
                self.assertEqual(self.sha256(path), expected)
        self.assertEqual(self.snapshot_output_root(), self.output_snapshot)


if __name__ == "__main__":
    unittest.main()
