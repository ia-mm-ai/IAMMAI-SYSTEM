"""Tests for one bounded receiver-answerable-receipt consideration boundary.

The suite consumes only the governing specification and exact completed
receiver-attestation operation artifact.  It does not create receipt,
presence, runtime, public, synchronization, or follow-on standing.
"""

from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest.mock import patch

import resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min as resolver


REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_PATH = (
    REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
)
SELECTED_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
)
WAITING_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.WAITING_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
)
OPERATION_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
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

BOUNDARY_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_boundary"
)
CHECKS_KEY = BOUNDARY_KEY + "_checks"
NON_MEANING_KEY = BOUNDARY_KEY + "_non_meaning"
SUMMARY_KEY = BOUNDARY_KEY + "_summary"
OPERATION_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation"
)
OPERATION_SUMMARY_KEY = OPERATION_KEY + "_summary"
OPERATION_NON_MEANING_KEY = OPERATION_KEY + "_non_meaning"

_MISSING = object()


class ReceiverAnswerableReceiptBoundaryV0MinTests(unittest.TestCase):
    """Verify consideration-only resolution and all bounded refusals."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            SELECTED_ARTIFACT_PATH,
            OPERATION_TERMINAL_SUMMARY_PATH,
            WAITING_ARTIFACT_PATH,
            SUPPLY_ARTIFACT_PATH,
        )
        for path in cls.preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input missing: {path}")
        cls.preserved_hashes = {
            path: cls.sha256(path) for path in cls.preserved_paths
        }
        cls.specification_text = SPECIFICATION_PATH.read_text(
            encoding="utf-8"
        )
        cls.selected_artifact = cls.strict_load_json(SELECTED_ARTIFACT_PATH)
        if not isinstance(cls.selected_artifact, dict):
            raise AssertionError("selected upstream artifact is not a mapping")
        cls.output_snapshot = cls.snapshot_output_root()

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            actual = cls.sha256(path)
            if actual != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if cls.snapshot_output_root() != cls.output_snapshot:
            raise AssertionError("canonical receipt-boundary output root changed")

    @staticmethod
    def sha256(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @classmethod
    def strict_load_json(cls, path: Path) -> object:
        def reject_duplicates(
            pairs: list[tuple[str, object]],
        ) -> dict[str, object]:
            value: dict[str, object] = {}
            for key, item in pairs:
                if key in value:
                    raise AssertionError(f"duplicate fixture key: {key}")
                value[key] = item
            return value

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

    def write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(
            path.is_dir(),
            f"fixture path collision: target is a directory: {path}",
        )
        path.write_text(text, encoding="utf-8")
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

    def artifact(self) -> dict[str, Any]:
        return copy.deepcopy(self.selected_artifact)

    def install_fixture(
        self,
        root: Path,
        *,
        specification_text: str | None = None,
        artifact: object = _MISSING,
    ) -> tuple[Path, Path]:
        specification_path = (
            root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
        )
        artifact_path = (
            root
            / resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
        )
        self.write_text(
            specification_path,
            (
                self.specification_text
                if specification_text is None
                else specification_text
            ),
        )
        self.write_json(
            artifact_path,
            self.artifact() if artifact is _MISSING else artifact,
        )
        return specification_path, artifact_path

    def canonical_request(self, **overrides: object) -> dict[str, Any]:
        return (
            resolver.build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request(
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
                resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_fixture(
        self,
        *,
        request: object = _MISSING,
        specification_text: str | None = None,
        artifact: object = _MISSING,
    ) -> dict[str, Any]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(
                root,
                specification_text=specification_text,
                artifact=artifact,
            )
            return self.invoke(request, root=root)

    def boundary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(BOUNDARY_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result.get(CHECKS_KEY)
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def assert_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        failed = sum(item.get("passed") is False for item in checks)
        passed = sum(item.get("passed") is True for item in checks)
        self.assertEqual(result.get("failed_check_count"), failed)
        self.assertEqual(result.get("passed_check_count"), passed)
        self.assertEqual(
            len(checks),
            result.get("failed_check_count")
            + result.get("passed_check_count"),
        )
        self.assertEqual(
            [item.get("name") for item in checks],
            list(dict.fromkeys(item.get("name") for item in checks)),
        )

    def assert_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(
            set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS)
        )
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                self.assertIs(non_claims[field], False)
                self.assertIs(self.boundary(result)[field], False)
        self.assertIs(
            result.get("result_level_non_claims_canonical_false"), True
        )

    def assert_omissions(self, result: Mapping[str, Any]) -> None:
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, dict)
        self.assertEqual(
            set(omission), set(resolver.OMISSION_POSTURE_FIELDS)
        )
        for field in resolver.OMISSION_POSTURE_FIELDS:
            with self.subTest(omission=field):
                self.assertIs(omission[field], True)
        self.assertFalse(
            resolver._contains_prohibited_complete_material(result)
        )

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            result.get("boundary_result"), resolver.RESULT_NOT_EVALUATED
        )
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        code = block.get("code")
        self.assertIsInstance(code, str)
        self.assertTrue(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertEqual(block.get("block_code"), code)
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        boundary = self.boundary(result)
        self.assertIs(
            boundary["receiver_answerable_receipt_boundary_recorded"], False
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_boundary_result_recorded"
            ],
            False,
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_consideration_allowed"
            ],
            False,
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_consideration_not_allowed"
            ],
            False,
        )
        self.assertIs(
            boundary["receiver_answerable_receipt_boundary_exhausted"],
            False,
        )
        self.assertEqual(
            result["boundary_posture"][
                "completed_consideration_posture_count"
            ],
            0,
        )
        self.assertGreater(result["failed_check_count"], 0)
        self.assert_counts(result)
        self.assert_non_claims(result)
        self.assert_omissions(result)

    def assert_completed_branch(
        self,
        result: Mapping[str, Any],
        *,
        allowed: bool,
    ) -> None:
        expected_outcome = (
            resolver.OUTCOME_ALLOWED
            if allowed
            else resolver.OUTCOME_NOT_ALLOWED
        )
        expected_result = (
            resolver.RESULT_ALLOWED
            if allowed
            else resolver.RESULT_NOT_ALLOWED
        )
        expected_code = (
            resolver.DECISION_CODE_ALLOWED
            if allowed
            else resolver.DECISION_CODE_NOT_ALLOWED
        )
        expected_reason = (
            resolver.DECISION_REASON_ALLOWED
            if allowed
            else resolver.DECISION_REASON_NOT_ALLOWED
        )
        self.assertEqual(result.get("outcome"), expected_outcome)
        self.assertEqual(result.get("boundary_result"), expected_result)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))
        decision = result.get("boundary_decision")
        self.assertIsInstance(decision, dict)
        self.assertEqual(decision.get("decision_code"), expected_code)
        self.assertEqual(decision.get("decision_reason"), expected_reason)
        self.assertIs(decision.get("selection"), allowed)
        boundary = self.boundary(result)
        self.assertIs(
            boundary["receiver_answerable_receipt_boundary_recorded"], True
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_boundary_result_recorded"
            ],
            True,
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_consideration_allowed"
            ],
            allowed,
        )
        self.assertIs(
            boundary[
                "receiver_answerable_receipt_consideration_not_allowed"
            ],
            not allowed,
        )
        self.assertIs(
            boundary["receiver_answerable_receipt_boundary_exhausted"],
            True,
        )
        self.assertEqual(
            result["boundary_posture"][
                "completed_consideration_posture_count"
            ],
            1,
        )
        self.assert_counts(result)
        self.assert_non_claims(result)
        self.assert_omissions(result)

    def test_public_api_constants_and_paths(self) -> None:
        public_api = (
            "build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request",
            "build_declared_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_from_path",
            "build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_summary",
            "write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result",
        )
        for name in public_api:
            with self.subTest(public_api=name):
                self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(
            issubclass(
                resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError,
                Exception,
            )
        )
        expected = {
            "RESOLVER_MODULE": (
                "resolve_receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_v0_min"
            ),
            "RESULT_VERSION": "0.1.0",
            "BOUNDARY_ID": (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_boundary_001"
            ),
            "BOUNDARY_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY"
            ),
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": (
                "CONSIDER_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_"
                "RECORDED_RECEIVER_ATTESTATION_RESULT_ONLY"
            ),
            "SELECTED_RECEIVER_ATTESTATION_OPERATION_ID": (
                "receiver_side_answerable_basis_"
                "receiver_attestation_operation_001"
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
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ATTESTATION_RECORDED"
            ),
            "CANDIDATE_ID": "receiver_side_answerable_basis_candidate_001",
            "CANDIDATE_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE"
            ),
            "CANDIDATE_SCOPE": (
                "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_"
                "ANSWERABLE_BASIS_CANDIDATE_ONLY"
            ),
            "ADMISSIBLE_FUTURE_ROUTE": (
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_THEN_SEPARATE_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OR_DECLARATION_ONLY"
            ),
            "OUTCOME_ALLOWED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_ALLOWED"
            ),
            "OUTCOME_NOT_ALLOWED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_NOT_ALLOWED"
            ),
            "OUTCOME_BLOCKED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_BLOCKED"
            ),
            "RESULT_ALLOWED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_ALLOWED"
            ),
            "RESULT_NOT_ALLOWED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_CONSIDERATION_NOT_ALLOWED"
            ),
            "RESULT_NOT_EVALUATED": "NOT_EVALUATED",
        }
        for name, value in expected.items():
            with self.subTest(constant=name):
                self.assertEqual(getattr(resolver, name), value)
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            Path(
                "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_BOUNDARY_V0_MIN_SPEC.md"
            ),
        )
        self.assertEqual(
            resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH,
            Path(
                "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_receiver_attestation_"
                "operation_v0_min/"
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
            "receiver_answerable_receipt_boundary_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_receiver_answerable_receipt_"
            "boundary_001__receiver_side_answerable_basis_"
            "receiver_answerable_receipt_boundary_v0_min_result.json",
        )

    def test_canonical_request_is_exact_fresh_and_independent(self) -> None:
        first = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request()
        )
        second = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_request()
        )
        self.assertIsInstance(first, dict)
        self.assertEqual(set(first), resolver._canonical_request_keys())
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"], second["declared_non_claims"]
        )
        for field, expected in resolver._identity_request_values().items():
            self.assertEqual(first[field], expected)
        self.assertIs(
            first["receiver_answerable_receipt_consideration_selected"],
            True,
        )
        self.assertEqual(
            set(first["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(
                value is False
                for value in first["declared_non_claims"].values()
            )
        )
        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(first[field], False)
        first["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        self.assertIs(
            second["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

    def test_declared_overrides_are_visible_bounded_and_deep_copied(
        self,
    ) -> None:
        false_request = self.canonical_request(
            receiver_answerable_receipt_consideration_selected=False
        )
        self.assertIs(
            false_request[
                "receiver_answerable_receipt_consideration_selected"
            ],
            False,
        )
        self.assert_completed_branch(self.invoke(false_request), allowed=False)

        unknown_source = {"nested": ["preserved"]}
        unknown = self.canonical_request(unknown_field=unknown_source)
        unknown_source["nested"].append("caller-change")
        self.assertEqual(unknown["unknown_field"], {"nested": ["preserved"]})
        self.assert_blocked(
            self.invoke(unknown), "REQUEST_UNKNOWN_FIELD"
        )

        malformed_source: list[object] = ["false"]
        malformed = self.canonical_request(
            receiver_answerable_receipt_consideration_selected=malformed_source
        )
        malformed_source.append("caller-change")
        self.assertEqual(
            malformed["receiver_answerable_receipt_consideration_selected"],
            ["false"],
        )
        self.assert_blocked(
            self.invoke(malformed), "REQUEST_BOOLEAN_REQUIRED"
        )

    def test_exact_boolean_request_matrix(self) -> None:
        canonical = self.canonical_request()
        self.assert_completed_branch(self.invoke(canonical), allowed=True)
        self.assert_completed_branch(
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_consideration_selected=False
                )
            ),
            allowed=False,
        )
        substitutes: tuple[object, ...] = (
            0,
            1,
            "true",
            "false",
            None,
            [],
            {},
            ["truthy"],
        )
        for value in substitutes:
            with self.subTest(selection_substitute=repr(value)):
                request = self.canonical_request(
                    receiver_answerable_receipt_consideration_selected=value
                )
                self.assert_blocked(
                    self.invoke(request), "REQUEST_BOOLEAN_REQUIRED"
                )

        prohibited_values = (True, *substitutes)
        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            for value in prohibited_values:
                with self.subTest(
                    prohibited_field=field, substitute=repr(value)
                ):
                    request = self.canonical_request(**{field: value})
                    self.assert_blocked(self.invoke(request))

        non_claim_values = (True, *substitutes)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            for value in non_claim_values:
                with self.subTest(
                    declared_non_claim=field, substitute=repr(value)
                ):
                    request = self.canonical_request()
                    request["declared_non_claims"][field] = copy.deepcopy(
                        value
                    )
                    self.assert_blocked(
                        self.invoke(request),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_allowed_not_allowed_and_blocked_cardinality(self) -> None:
        allowed = self.invoke()
        not_allowed = self.invoke(
            self.canonical_request(
                receiver_answerable_receipt_consideration_selected=False
            )
        )
        blocked = self.invoke(
            self.canonical_request(unknown_request_field=False)
        )
        self.assert_completed_branch(allowed, allowed=True)
        self.assert_completed_branch(not_allowed, allowed=False)
        self.assert_blocked(blocked, "REQUEST_UNKNOWN_FIELD")
        for result, expected_count in (
            (allowed, 1),
            (not_allowed, 1),
            (blocked, 0),
        ):
            boundary = self.boundary(result)
            postures = (
                boundary[
                    "receiver_answerable_receipt_consideration_allowed"
                ],
                boundary[
                    "receiver_answerable_receipt_consideration_not_allowed"
                ],
            )
            self.assertEqual(sum(value is True for value in postures), expected_count)
            self.assertFalse(all(value is True for value in postures))
        self.assertIs(
            self.boundary(blocked)[
                "receiver_answerable_receipt_boundary_result_recorded"
            ],
            False,
        )

    def test_specification_marker_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(root)
            canonical = self.invoke(root=root)
            self.assert_completed_branch(canonical, allowed=True)
            specification_path = (
                root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            )
            for family, markers in resolver.SPEC_MARKER_FAMILIES.items():
                for index, marker in enumerate(markers):
                    with self.subTest(
                        marker_family=family, marker_index=index
                    ):
                        corrupted = self.specification_text.replace(
                            marker,
                            f"REMOVED_{family}_{index}",
                        )
                        self.assertNotIn(marker, corrupted)
                        self.write_text(specification_path, corrupted)
                        result = self.invoke(root=root)
                        self.assert_blocked(
                            result,
                            "RECEIPT_BOUNDARY_SPEC_MARKER_MISSING",
                        )
            self.write_text(specification_path, self.specification_text)

    def test_upstream_json_metadata_identity_and_result_matrix(self) -> None:
        cases: tuple[
            tuple[str, tuple[str, ...], object, str],
            ...,
        ] = (
            (
                "resolver_module",
                ("resolver_module",),
                "wrong_resolver",
                "UPSTREAM_METADATA_MISMATCH",
            ),
            (
                "result_version",
                ("result_version",),
                "9.9.9",
                "UPSTREAM_METADATA_MISMATCH",
            ),
            (
                "failed_check_count",
                ("failed_check_count",),
                1,
                "UPSTREAM_FAILED_CHECKS_PRESENT",
            ),
            (
                "passed_check_count",
                ("passed_check_count",),
                159,
                "UPSTREAM_METADATA_MISMATCH",
            ),
            (
                "outcome",
                ("outcome",),
                "WRONG_OUTCOME",
                "UPSTREAM_METADATA_MISMATCH",
            ),
            (
                "blocked",
                ("block", "blocked"),
                True,
                "UPSTREAM_BLOCKED",
            ),
            (
                "operation_result",
                ("operation_result_detail", "operation_result"),
                "WRONG_RESULT",
                "UPSTREAM_RESULT_MISMATCH",
            ),
            (
                "operation_identity",
                (OPERATION_KEY, "operation_id"),
                "wrong_operation",
                "UPSTREAM_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "candidate_identity",
                (
                    OPERATION_KEY,
                    "receiver_side_answerable_basis_candidate_id",
                ),
                "wrong_candidate",
                "UPSTREAM_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "completed_result_count",
                (
                    "operation_result_detail",
                    "completed_result_posture_count",
                ),
                2,
                "UPSTREAM_RESULT_CARDINALITY_MISMATCH",
            ),
        )
        for label, path, value, code in cases:
            with self.subTest(upstream_case=label):
                artifact = self.artifact()
                self.set_path(artifact, path, value)
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact), code
                )

    @staticmethod
    def set_path(
        mapping: dict[str, Any],
        path: tuple[str, ...],
        value: object,
    ) -> None:
        selected: dict[str, Any] = mapping
        for key in path[:-1]:
            nested = selected[key]
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {path}")
            selected = nested
        selected[path[-1]] = copy.deepcopy(value)

    def test_every_required_upstream_true_posture_is_exact_true(self) -> None:
        locations = {
            "operation_basis_supplied": (OPERATION_KEY, "operation_basis_supplied"),
            "operation_basis_admitted": (OPERATION_KEY, "operation_basis_admitted"),
            "receiver_attestation_operation_recorded": (
                OPERATION_KEY,
                "receiver_attestation_operation_recorded",
            ),
            "receiver_attestation_operation_result_recorded": (
                OPERATION_KEY,
                "receiver_attestation_operation_result_recorded",
            ),
            "receiver_attestation_operation_exhausted": (
                OPERATION_KEY,
                "receiver_attestation_operation_exhausted",
            ),
            "receiver_attestation_decided": (
                OPERATION_KEY,
                "receiver_attestation_decided",
            ),
            "receiver_attestation_recorded": (
                OPERATION_KEY,
                "receiver_attestation_recorded",
            ),
            "operation_result_present": (
                OPERATION_NON_MEANING_KEY,
                "operation_result_present",
            ),
            "minimum_admission_checks_passed": (
                "bounded_component_validation",
                "minimum_admission_checks_passed",
            ),
            "archive_correspondence_validated": (
                OPERATION_SUMMARY_KEY,
                "archive_correspondence_validated",
            ),
            "text_components_validated": (
                OPERATION_SUMMARY_KEY,
                "text_components_validated",
            ),
            "timestamp_validated": (
                OPERATION_SUMMARY_KEY,
                "timestamp_validated",
            ),
            "trace_paths_validated": (
                OPERATION_SUMMARY_KEY,
                "trace_paths_validated",
            ),
            "recorded_signal_artifact_existence_validated": (
                OPERATION_SUMMARY_KEY,
                "recorded_signal_artifact_existence_validated",
            ),
            "result_level_non_claims_canonical_false": (
                OPERATION_SUMMARY_KEY,
                "result_level_non_claims_canonical_false",
            ),
        }
        self.assertEqual(
            set(locations), set(resolver.REQUIRED_UPSTREAM_TRUE_POSTURES)
        )
        for field, path in locations.items():
            for value in (False, 1):
                with self.subTest(true_posture=field, value=value):
                    artifact = self.artifact()
                    self.set_path(artifact, path, value)
                    self.assert_blocked(
                        self.resolve_fixture(artifact=artifact),
                        "UPSTREAM_TRUE_POSTURE_NOT_TRUE",
                    )

    def test_every_upstream_false_lock_rejects_true_missing_and_non_bool(
        self,
    ) -> None:
        replacements: tuple[object, ...] = (
            True,
            None,
            "false",
            0,
            1,
            [],
            {},
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, artifact_path = self.install_fixture(root)
            for field in resolver.REQUIRED_UPSTREAM_FALSE_POSTURES:
                for value in replacements:
                    with self.subTest(false_lock=field, value=repr(value)):
                        artifact = self.artifact()
                        operation = artifact[OPERATION_KEY]
                        self.assertIsInstance(operation, dict)
                        operation[field] = copy.deepcopy(value)
                        self.write_json(artifact_path, artifact)
                        self.assert_blocked(
                            self.invoke(root=root),
                            "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                        )
                with self.subTest(false_lock=field, value="missing"):
                    artifact = self.artifact()
                    operation = artifact[OPERATION_KEY]
                    self.assertIsInstance(operation, dict)
                    operation.pop(field)
                    self.write_json(artifact_path, artifact)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                    )

    def test_upstream_non_claims_must_remain_canonical_false(self) -> None:
        artifact = self.artifact()
        non_claims = artifact["non_claims"]
        self.assertIsInstance(non_claims, dict)
        non_claims[next(iter(non_claims))] = True
        self.assert_blocked(
            self.resolve_fixture(artifact=artifact),
            "UPSTREAM_NON_CLAIMS_NOT_CANONICAL_FALSE",
        )

    def test_strict_selected_upstream_json_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, artifact_path = self.install_fixture(root)
            self.write_text(artifact_path, "{")
            self.assert_blocked(
                self.invoke(root=root),
                "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_PARSEABLE",
            )
            self.write_text(
                artifact_path,
                '{"resolver_module":"one","resolver_module":"two"}\n',
            )
            self.assert_blocked(
                self.invoke(root=root),
                "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_DUPLICATE_KEYED",
            )
            self.write_json(artifact_path, [])
            self.assert_blocked(
                self.invoke(root=root),
                "SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_NOT_MAPPING",
            )

    def test_upstream_read_limit_and_no_discovery(self) -> None:
        expected_reads = {
            SPECIFICATION_PATH.resolve(),
            SELECTED_ARTIFACT_PATH.resolve(),
        }
        reads: list[Path] = []
        original_read_text = Path.read_text

        def bounded_read_text(
            path: Path,
            *args: object,
            **kwargs: object,
        ) -> str:
            resolved = Path(path).resolve()
            reads.append(resolved)
            if resolved not in expected_reads:
                raise AssertionError(f"prohibited file read: {resolved}")
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
                side_effect=AssertionError("directory listing prohibited"),
            ),
            patch(
                "os.listdir",
                side_effect=AssertionError("os.listdir prohibited"),
            ),
            patch(
                "os.scandir",
                side_effect=AssertionError("os.scandir prohibited"),
            ),
        ):
            result = self.invoke()
        self.assert_completed_branch(result, allowed=True)
        self.assertEqual(reads, [SPECIFICATION_PATH.resolve(), SELECTED_ARTIFACT_PATH.resolve()])

    def test_non_claims_omissions_non_meaning_and_routes_all_branches(
        self,
    ) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_consideration_selected=False
                )
            ),
            self.invoke(self.canonical_request(unknown_field=False)),
        )
        expected_non_meaning = resolver._non_meaning()
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_non_claims(result)
                self.assert_omissions(result)
                self.assertEqual(
                    result.get(NON_MEANING_KEY), expected_non_meaning
                )
                self.assertTrue(
                    all(
                        value is True
                        for value in result[NON_MEANING_KEY].values()
                    )
                )
                self.assertEqual(
                    result.get("blocked_routes"),
                    list(resolver.BLOCKED_ROUTES),
                )
                self.assertEqual(
                    result.get("admissible_future_route"),
                    resolver.ADMISSIBLE_FUTURE_ROUTE,
                )
                serialized = json.dumps(result, sort_keys=True)
                for forbidden in (
                    "archive_body",
                    "archive_bytes",
                    "hash_record_body",
                    "text_component_bodies",
                    "recorded_signal_body",
                    "capture_signal_data",
                    "signal_samples",
                    "raw_signal_data",
                    "sufficiency_basis_records",
                ):
                    self.assertNotIn(f'"{forbidden}"', serialized)
        request = self.canonical_request()
        self.assertIs(
            request["request_contaminated_lineage_validation"], False
        )

    def test_determinism_immutability_checks_and_live_artifact_stability(
        self,
    ) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        first = self.invoke(request)
        second = self.invoke(request)
        self.assertEqual(first, second)
        self.assertEqual(request, request_before)
        first_summary = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_summary(
                first
            )
        )
        second_summary = (
            resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_summary(
                copy.deepcopy(first)
            )
        )
        self.assertEqual(first_summary, second_summary)
        self.assert_counts(first)
        self.assertEqual(first["failed_check_count"], 0)
        self.assertEqual(
            self.sha256(SELECTED_ARTIFACT_PATH),
            self.preserved_hashes[SELECTED_ARTIFACT_PATH],
        )
        serialized = json.dumps(first, sort_keys=True)
        for unstable_key in (
            '"created_at"',
            '"updated_at"',
            '"run_id"',
            '"random_seed"',
            '"environment"',
        ):
            self.assertNotIn(unstable_key, serialized)

        artifact = self.artifact()
        artifact_before = copy.deepcopy(artifact)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, artifact_path = self.install_fixture(root, artifact=artifact)
            self.assert_completed_branch(
                self.invoke(request, root=root), allowed=True
            )
            self.assertEqual(artifact, artifact_before)
            self.assertEqual(
                json.loads(artifact_path.read_text(encoding="utf-8")),
                artifact_before,
            )

    def test_summary_contract_for_every_branch(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_consideration_selected=False
                )
            ),
            self.invoke(self.canonical_request(unknown_field=False)),
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                summary = (
                    resolver.build_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(summary, result[SUMMARY_KEY])
                self.assertEqual(
                    summary["resolver_module"], resolver.RESOLVER_MODULE
                )
                self.assertEqual(
                    summary["result_version"], resolver.RESULT_VERSION
                )
                self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
                self.assertEqual(
                    summary["selected_receiver_attestation_operation_id"],
                    resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ID,
                )
                self.assertEqual(
                    summary["selected_candidate_id"], resolver.CANDIDATE_ID
                )
                self.assertEqual(
                    summary["specification_path"],
                    str(resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH),
                )
                self.assertEqual(
                    summary["selected_upstream_artifact_path"],
                    str(
                        resolver.SELECTED_RECEIVER_ATTESTATION_OPERATION_ARTIFACT_RELATIVE_PATH
                    ),
                )
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(
                    summary["boundary_result"], result["boundary_result"]
                )
                self.assertEqual(
                    summary["boundary_type"], resolver.BOUNDARY_TYPE
                )
                self.assertEqual(
                    summary["boundary_version"], resolver.BOUNDARY_VERSION
                )
                self.assertEqual(
                    summary["boundary_scope"], resolver.BOUNDARY_SCOPE
                )
                self.assertEqual(
                    summary["failed_check_count"],
                    result["failed_check_count"],
                )
                self.assertEqual(
                    summary["passed_check_count"],
                    result["passed_check_count"],
                )
                block = result["block"]
                decision = result["boundary_decision"]
                boundary = self.boundary(result)
                specification = result["specification_validation"]
                upstream = result["upstream_artifact_validation"]
                self.assertIs(summary["blocked"], block["blocked"])
                self.assertEqual(
                    summary["decision_code"], decision["decision_code"]
                )
                self.assertEqual(
                    summary["decision_reason"], decision["decision_reason"]
                )
                self.assertIs(
                    summary["selection"],
                    boundary[
                        "receiver_answerable_receipt_consideration_selected"
                    ],
                )
                self.assertIs(
                    summary["specification_validated"],
                    specification["specification_validated"],
                )
                self.assertIs(
                    summary["upstream_artifact_validated"],
                    upstream["artifact_validated"],
                )
                self.assertIs(
                    summary["exact_recorded_result_validated"],
                    upstream["exact_recorded_result_validated"],
                )
                self.assertIs(
                    summary["result_cardinality_validated"],
                    upstream["result_cardinality_validated"],
                )
                self.assertIs(
                    summary["upstream_false_locks_validated"],
                    upstream["upstream_false_locks_validated"],
                )
                self.assertIs(
                    summary["operation_completed_and_exhausted"],
                    upstream["operation_completed_and_exhausted"],
                )
                self.assertIs(
                    summary["receiver_attestation_recorded"],
                    upstream["receiver_attestation_recorded"],
                )
                self.assertIs(
                    summary["boundary_recorded"],
                    boundary[
                        "receiver_answerable_receipt_boundary_recorded"
                    ],
                )
                self.assertIs(
                    summary["boundary_result_recorded"],
                    boundary[
                        "receiver_answerable_receipt_boundary_result_recorded"
                    ],
                )
                self.assertIs(
                    summary["boundary_exhausted"],
                    boundary[
                        "receiver_answerable_receipt_boundary_exhausted"
                    ],
                )
                self.assertIs(
                    summary["consideration_allowed"],
                    boundary[
                        "receiver_answerable_receipt_consideration_allowed"
                    ],
                )
                self.assertIs(
                    summary["consideration_not_allowed"],
                    boundary[
                        "receiver_answerable_receipt_consideration_not_allowed"
                    ],
                )
                self.assertTrue(summary["receipt_absent"])
                self.assertTrue(summary["receipt_operation_absent"])
                self.assertTrue(summary["presence_absent"])
                self.assertTrue(
                    summary["downstream_non_claims_canonical_false"]
                )
                self.assertTrue(
                    summary["complete_material_omission_posture"]
                )
                self.assertEqual(
                    summary["admissible_future_route"],
                    resolver.ADMISSIBLE_FUTURE_ROUTE,
                )
                self.assertNotIn("checks", summary)
                self.assertFalse(
                    resolver._contains_prohibited_complete_material(summary)
                )

    def test_from_path_strict_json_and_request_immutability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(root)
            request = self.canonical_request()
            request_path = self.write_json(root / "request.json", request)
            request_bytes = request_path.read_bytes()
            with patch.object(resolver, "REPO_ROOT", root):
                direct = (
                    resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min(
                        request
                    )
                )
                from_path = (
                    resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_from_path(
                        request_path
                    )
                )
            self.assertEqual(from_path, direct)
            self.assertEqual(request_path.read_bytes(), request_bytes)

            malformed = self.write_text(root / "malformed.json", "{")
            duplicate = self.write_text(
                root / "duplicate.json",
                '{"intent":"one","intent":"two"}\n',
            )
            array = self.write_json(root / "array.json", [])
            invalid_utf8 = root / "invalid_utf8.json"
            invalid_utf8.write_bytes(b"\xff\xfe")
            missing = root / "missing.json"
            for label, path in (
                ("malformed", malformed),
                ("duplicate", duplicate),
                ("array", array),
                ("invalid_utf8", invalid_utf8),
                ("missing", missing),
            ):
                with self.subTest(request_path_case=label):
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError
                    ):
                        resolver.resolve_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_from_path(
                            path
                        )

    def assert_written_json(
        self,
        path: Path,
        result: Mapping[str, Any],
    ) -> None:
        text = path.read_text(encoding="utf-8")
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

    def test_writer_valid_branches_suffix_and_no_overwrite(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    receiver_answerable_receipt_consideration_selected=False
                )
            ),
            self.invoke(self.canonical_request(unknown_field=False)),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                first = (
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                        results[0]
                    )
                )
                first_bytes = first.read_bytes()
                second = (
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                        results[0]
                    )
                )
            self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(
                second.name,
                Path(resolver.OUTPUT_FILENAME).stem
                + "_001"
                + Path(resolver.OUTPUT_FILENAME).suffix,
            )
            self.assertEqual(first.read_bytes(), first_bytes)
            self.assert_written_json(first, results[0])
            self.assert_written_json(second, results[0])

            for index, result in enumerate(results[1:], start=1):
                target = (
                    root
                    / f"explicit_{index}"
                    / resolver.OUTPUT_FILENAME
                )
                written = (
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                        result,
                        target,
                    )
                )
                self.assertEqual(written, target)
                self.assert_written_json(written, result)
                before = written.read_bytes()
                with self.assertRaises(
                    resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError
                ):
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                        result,
                        target,
                    )
                self.assertEqual(written.read_bytes(), before)

    def test_writer_refusal_matrix(self) -> None:
        allowed = self.invoke()
        not_allowed = self.invoke(
            self.canonical_request(
                receiver_answerable_receipt_consideration_selected=False
            )
        )
        blocked = self.invoke(self.canonical_request(unknown_field=False))
        invalid: list[tuple[str, object]] = [("non_mapping", [])]

        def changed(
            label: str,
            source: Mapping[str, Any],
            mutation: Callable[[dict[str, Any]], None],
        ) -> None:
            value = copy.deepcopy(source)
            mutation(value)
            invalid.append((label, value))

        changed(
            "malformed_branch",
            allowed,
            lambda value: value["boundary_posture"].pop(
                "completed_consideration_posture_count"
            ),
        )
        changed(
            "inconsistent_outcome",
            allowed,
            lambda value: value.__setitem__(
                "outcome", resolver.OUTCOME_NOT_ALLOWED
            ),
        )
        changed(
            "inconsistent_result",
            allowed,
            lambda value: value.__setitem__(
                "boundary_result", resolver.RESULT_NOT_ALLOWED
            ),
        )
        changed(
            "wrong_counts",
            allowed,
            lambda value: value.__setitem__("passed_check_count", 0),
        )
        changed(
            "wrong_boundary_identity",
            allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "boundary_id", "wrong"
            ),
        )
        changed(
            "allowed_without_allowed_posture",
            allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "receiver_answerable_receipt_consideration_allowed",
                False,
            ),
        )
        changed(
            "not_allowed_without_not_allowed_posture",
            not_allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "receiver_answerable_receipt_consideration_not_allowed",
                False,
            ),
        )
        changed(
            "blocked_records_result",
            blocked,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "receiver_answerable_receipt_boundary_result_recorded",
                True,
            ),
        )
        changed(
            "non_claim_true",
            allowed,
            lambda value: value["non_claims"].__setitem__(
                resolver.REQUIRED_FALSE_NON_CLAIMS[0], True
            ),
        )
        changed(
            "omission_false",
            allowed,
            lambda value: value["omission_posture"].__setitem__(
                resolver.OMISSION_POSTURE_FIELDS[0], False
            ),
        )
        changed(
            "complete_material",
            allowed,
            lambda value: value.__setitem__(
                "complete_upstream_artifact", {"forbidden": True}
            ),
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, result in invalid:
                with self.subTest(writer_refusal=label):
                    target = root / label / resolver.OUTPUT_FILENAME
                    with self.assertRaises(
                        resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError
                    ):
                        resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                            result,
                            target,
                        )
                    self.assertFalse(target.exists())

    def test_writer_protected_path_refusal(self) -> None:
        result = self.invoke()
        protected = (
            SELECTED_ARTIFACT_PATH,
            WAITING_ARTIFACT_PATH,
            SUPPLY_ARTIFACT_PATH,
            REPO_ROOT
            / "artifacts/actual_receiver_attestation_capture/"
            "receiver_attestation_capture_001/original_zip/"
            "receiver_attestation_001.zip",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_v0_min/protected.json",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_receiver_attestation_"
            "boundary_v0_min_v2/protected.json",
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            Path(__file__).resolve(),
            REPO_ROOT / "reference/IAMMAI/protected.json",
            REPO_ROOT / "artifacts/not_the_exact_output_family/result.json",
        )
        for target in protected:
            with self.subTest(protected_path=str(target)):
                existed = target.exists()
                before = target.read_bytes() if target.is_file() else None
                with self.assertRaises(
                    resolver.ReceiverSideAnswerableBasisReceiverAnswerableReceiptBoundaryV0MinError
                ):
                    resolver.write_receiver_side_answerable_basis_receiver_answerable_receipt_boundary_v0_min_result(
                        result,
                        target,
                    )
                self.assertEqual(target.exists(), existed)
                if before is not None:
                    self.assertEqual(target.read_bytes(), before)

    def test_preserved_hashes_and_output_root_state(self) -> None:
        for path, expected in self.preserved_hashes.items():
            with self.subTest(preserved_path=str(path)):
                self.assertEqual(self.sha256(path), expected)
        self.assertEqual(self.snapshot_output_root(), self.output_snapshot)


if __name__ == "__main__":
    unittest.main()
