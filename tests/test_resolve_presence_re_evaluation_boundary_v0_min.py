"""Tests for one bounded presence re-evaluation consideration boundary.

The suite preserves the prior lawful waiting presence result and the later
receiver-answerable receipt as separate standing.  It creates no revised
presence result, re-evaluation operation, lapse route, or live artifact.
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

import resolve_presence_re_evaluation_boundary_v0_min as resolver


REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_PATH = (
    REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
)
PRIOR_ARTIFACT_PATH = (
    REPO_ROOT / resolver.PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
)
RECEIPT_ARTIFACT_PATH = (
    REPO_ROOT
    / resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
)
PRIOR_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT / "spec/PRESENCE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
RECEIPT_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
)
RECEIPT_BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_answerable_receipt_"
    "boundary_v0_min/receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_001__"
    "receiver_side_answerable_basis_"
    "receiver_answerable_receipt_boundary_v0_min_result.json"
)
RECEIVER_ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_"
    "receiver_side_answerable_basis_receiver_attestation_operation_v0_min/"
    "receiver_side_answerable_basis_receiver_attestation_operation_001__"
    "receiver_side_answerable_basis_"
    "receiver_attestation_operation_v0_min_result_001.json"
)
RESOLVER_PATH = Path(resolver.__file__).resolve()
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

BOUNDARY_KEY = "presence_re_evaluation_boundary"
CHECKS_KEY = "presence_re_evaluation_boundary_checks"
SUMMARY_KEY = "presence_re_evaluation_boundary_summary"
NON_MEANING_KEY = "presence_re_evaluation_boundary_non_meaning"
PRIOR_OPERATION_KEY = "presence_operation"
PRIOR_SUMMARY_KEY = "presence_operation_summary"
RECEIPT_OPERATION_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
)
RECEIPT_SUMMARY_KEY = RECEIPT_OPERATION_KEY + "_summary"

_MISSING = object()


class PresenceReEvaluationBoundaryV0MinTests(unittest.TestCase):
    """Verify changed-condition consideration and every bounded refusal."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            PRIOR_ARTIFACT_PATH,
            PRIOR_TERMINAL_SUMMARY_PATH,
            RECEIPT_ARTIFACT_PATH,
            RECEIPT_TERMINAL_SUMMARY_PATH,
            RECEIPT_BOUNDARY_ARTIFACT_PATH,
            RECEIVER_ATTESTATION_ARTIFACT_PATH,
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
        cls.prior_artifact = cls.strict_load_json(PRIOR_ARTIFACT_PATH)
        cls.receipt_artifact = cls.strict_load_json(RECEIPT_ARTIFACT_PATH)
        if not isinstance(cls.prior_artifact, dict):
            raise AssertionError("prior presence artifact is not a mapping")
        if not isinstance(cls.receipt_artifact, dict):
            raise AssertionError("receipt artifact is not a mapping")
        cls.output_snapshot = cls.snapshot_output_root()

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            actual = cls.sha256(path)
            if actual != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if cls.snapshot_output_root() != cls.output_snapshot:
            raise AssertionError(
                "canonical presence-re-evaluation output root changed"
            )

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

    def prior(self) -> dict[str, Any]:
        return copy.deepcopy(self.prior_artifact)

    def receipt(self) -> dict[str, Any]:
        return copy.deepcopy(self.receipt_artifact)

    def install_fixture(
        self,
        root: Path,
        *,
        specification_text: str | None = None,
        prior_artifact: object = _MISSING,
        receipt_artifact: object = _MISSING,
    ) -> tuple[Path, Path, Path]:
        specification_path = (
            root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
        )
        prior_path = (
            root / resolver.PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
        )
        receipt_path = (
            root
            / resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
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
            prior_path,
            self.prior() if prior_artifact is _MISSING else prior_artifact,
        )
        self.write_json(
            receipt_path,
            (
                self.receipt()
                if receipt_artifact is _MISSING
                else receipt_artifact
            ),
        )
        return specification_path, prior_path, receipt_path

    def canonical_request(self, **overrides: object) -> dict[str, Any]:
        return (
            resolver.build_declared_presence_re_evaluation_boundary_v0_min_request(
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
            result = resolver.resolve_presence_re_evaluation_boundary_v0_min(
                supplied
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_presence_re_evaluation_boundary_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

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

    @staticmethod
    def delete_path(
        mapping: dict[str, Any],
        path: tuple[str, ...],
    ) -> None:
        selected: dict[str, Any] = mapping
        for key in path[:-1]:
            nested = selected[key]
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {path}")
            selected = nested
        selected.pop(path[-1])

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
        self.assertEqual(len(checks), failed + passed)
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
        boundary = self.boundary(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                self.assertIs(non_claims[field], False)
                self.assertIs(boundary[field], False)
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
            boundary["presence_re_evaluation_boundary_recorded"], False
        )
        self.assertIs(
            boundary["presence_re_evaluation_boundary_result_recorded"],
            False,
        )
        self.assertIs(
            boundary[
                "presence_re_evaluation_operation_consideration_allowed"
            ],
            False,
        )
        self.assertIs(
            boundary[
                "presence_re_evaluation_operation_consideration_not_allowed"
            ],
            False,
        )
        self.assertIs(
            boundary["presence_re_evaluation_boundary_exhausted"], False
        )
        self.assertEqual(
            result["completed_consideration_posture_count"], 0
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
        self.assertEqual(
            block,
            {
                "blocked": False,
                "code": None,
                "block_code": None,
                "reason": None,
            },
        )
        decision = result.get("boundary_decision")
        self.assertIsInstance(decision, dict)
        self.assertEqual(decision.get("decision_code"), expected_code)
        self.assertEqual(decision.get("decision_reason"), expected_reason)
        self.assertIs(decision.get("selection"), allowed)
        boundary = self.boundary(result)
        self.assertIs(
            boundary["presence_re_evaluation_boundary_recorded"], True
        )
        self.assertIs(
            boundary["presence_re_evaluation_boundary_result_recorded"],
            True,
        )
        self.assertIs(
            boundary[
                "presence_re_evaluation_operation_consideration_allowed"
            ],
            allowed,
        )
        self.assertIs(
            boundary[
                "presence_re_evaluation_operation_consideration_not_allowed"
            ],
            not allowed,
        )
        self.assertIs(
            boundary["presence_re_evaluation_boundary_exhausted"], True
        )
        self.assertEqual(
            result["completed_consideration_posture_count"], 1
        )
        self.assert_counts(result)
        self.assert_non_claims(result)
        self.assert_omissions(result)

    def branches(self) -> tuple[dict[str, Any], ...]:
        return (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    presence_re_evaluation_operation_consideration_selected=(
                        False
                    )
                )
            ),
            self.invoke(self.canonical_request(unknown_field=False)),
        )

    def test_public_api_constants_and_paths(self) -> None:
        public_api = (
            "build_presence_re_evaluation_boundary_v0_min_request",
            "build_declared_presence_re_evaluation_boundary_v0_min_request",
            "resolve_presence_re_evaluation_boundary_v0_min",
            "resolve_presence_re_evaluation_boundary_v0_min_from_path",
            "build_presence_re_evaluation_boundary_v0_min_summary",
            "write_presence_re_evaluation_boundary_v0_min_result",
        )
        for name in public_api:
            with self.subTest(public_api=name):
                self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(
            issubclass(
                resolver.PresenceReEvaluationBoundaryV0MinError,
                Exception,
            )
        )
        expected = {
            "RESOLVER_MODULE": (
                "resolve_presence_re_evaluation_boundary_v0_min"
            ),
            "RESULT_VERSION": "0.1.0",
            "BOUNDARY_ID": "presence_re_evaluation_boundary_001",
            "BOUNDARY_TYPE": "PRESENCE_RE_EVALUATION_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": (
                "CONSIDER_ONE_PRESENCE_RE_EVALUATION_AFTER_RECORDED_"
                "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
            ),
            "PRIOR_PRESENCE_OPERATION_ID": "presence_operation_001",
            "PRIOR_PRESENCE_OPERATION_TYPE": "PRESENCE_OPERATION",
            "PRIOR_PRESENCE_OPERATION_VERSION": "0.1.0",
            "PRIOR_PRESENCE_OPERATION_SCOPE": (
                "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_"
                "RECEIVER_ATTESTATION_REQUIREMENT_ONLY"
            ),
            "PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED": (
                "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
            ),
            "PRIOR_PRESENCE_RESULT_REQUIRED": "REQUIRES_RECEIVER_ATTESTATION",
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID": (
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_001"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_VERSION": "0.1.0",
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_SCOPE": (
                "RECORD_ONE_RECEIVER_ANSWERABLE_RECEIPT_FOR_ONE_RECORDED_"
                "RECEIVER_ATTESTATION_RESULT_ONLY"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_OUTCOME_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
            ),
            "ADMISSIBLE_FUTURE_ROUTE": (
                "PRESENCE_RE_EVALUATION_BOUNDARY_THEN_SEPARATE_"
                "PRESENCE_RE_EVALUATION_OPERATION_ONLY"
            ),
            "OUTCOME_ALLOWED": "PRESENCE_RE_EVALUATION_BOUNDARY_ALLOWED",
            "OUTCOME_NOT_ALLOWED": (
                "PRESENCE_RE_EVALUATION_BOUNDARY_NOT_ALLOWED"
            ),
            "OUTCOME_BLOCKED": "PRESENCE_RE_EVALUATION_BOUNDARY_BLOCKED",
            "RESULT_ALLOWED": (
                "PRESENCE_RE_EVALUATION_OPERATION_CONSIDERATION_ALLOWED"
            ),
            "RESULT_NOT_ALLOWED": (
                "PRESENCE_RE_EVALUATION_OPERATION_"
                "CONSIDERATION_NOT_ALLOWED"
            ),
            "RESULT_NOT_EVALUATED": "NOT_EVALUATED",
            "DECISION_CODE_ALLOWED": (
                "PRESENCE_RE_EVALUATION_CONSIDERATION_ALLOWED"
            ),
            "DECISION_REASON_ALLOWED": (
                "prior lawful waiting presence result and later recorded "
                "receiver-answerable receipt admitted for one separate "
                "presence re-evaluation operation consideration only"
            ),
            "DECISION_CODE_NOT_ALLOWED": (
                "PRESENCE_RE_EVALUATION_CONSIDERATION_NOT_ALLOWED"
            ),
            "DECISION_REASON_NOT_ALLOWED": (
                "presence re-evaluation operation consideration not selected"
            ),
        }
        for name, value in expected.items():
            with self.subTest(constant=name):
                self.assertEqual(getattr(resolver, name), value)
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            Path("spec/PRESENCE_RE_EVALUATION_BOUNDARY_V0_MIN_SPEC.md"),
        )
        self.assertEqual(
            resolver.PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH,
            Path(
                "artifacts/integrity_host_v0_min_coexistence_"
                "presence_operation_v0_min/"
                "presence_operation_001__presence_operation_v0_min_result.json"
            ),
        )
        self.assertEqual(
            resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH,
            Path(
                "artifacts/integrity_host_v0_min_coexistence_"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min/"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_001__"
                "receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min_result.json"
            ),
        )
        self.assertEqual(
            resolver.OUTPUT_ROOT,
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "presence_re_evaluation_boundary_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "presence_re_evaluation_boundary_001__"
            "presence_re_evaluation_boundary_v0_min_result.json",
        )

    def test_canonical_request_and_declared_overrides(self) -> None:
        first = resolver.build_presence_re_evaluation_boundary_v0_min_request()
        second = resolver.build_presence_re_evaluation_boundary_v0_min_request()
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
            first[
                "presence_re_evaluation_operation_consideration_selected"
            ],
            True,
        )
        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            self.assertIs(first[field], False)
        self.assertTrue(
            all(
                value is False
                for value in first["declared_non_claims"].values()
            )
        )
        first["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        self.assertIs(
            second["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

        false_request = self.canonical_request(
            presence_re_evaluation_operation_consideration_selected=False
        )
        self.assertIs(
            false_request[
                "presence_re_evaluation_operation_consideration_selected"
            ],
            False,
        )
        self.assert_completed_branch(self.invoke(false_request), allowed=False)

        nested = {"items": ["preserved"]}
        unknown = self.canonical_request(unknown_field=nested)
        nested["items"].append("caller-change")
        self.assertEqual(unknown["unknown_field"], {"items": ["preserved"]})
        self.assert_blocked(
            self.invoke(unknown), "REQUEST_UNKNOWN_FIELD"
        )

        malformed_source: list[object] = ["false"]
        malformed = self.canonical_request(
            presence_re_evaluation_operation_consideration_selected=(
                malformed_source
            )
        )
        malformed_source.append("caller-change")
        self.assertEqual(
            malformed[
                "presence_re_evaluation_operation_consideration_selected"
            ],
            ["false"],
        )
        self.assert_blocked(
            self.invoke(malformed), "REQUEST_BOOLEAN_REQUIRED"
        )

    def test_exact_boolean_request_matrix(self) -> None:
        self.assert_completed_branch(self.invoke(), allowed=True)
        self.assert_completed_branch(
            self.invoke(
                self.canonical_request(
                    presence_re_evaluation_operation_consideration_selected=(
                        False
                    )
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
                    presence_re_evaluation_operation_consideration_selected=(
                        value
                    )
                )
                self.assert_blocked(
                    self.invoke(request), "REQUEST_BOOLEAN_REQUIRED"
                )

        for field in resolver.PROHIBITED_REQUEST_FLAGS:
            for value in (True, *substitutes):
                with self.subTest(
                    prohibited_field=field,
                    substitute=repr(value),
                ):
                    self.assert_blocked(
                        self.invoke(
                            self.canonical_request(**{field: value})
                        )
                    )

        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            for value in (True, *substitutes):
                with self.subTest(
                    declared_non_claim=field,
                    substitute=repr(value),
                ):
                    request = self.canonical_request()
                    request["declared_non_claims"][field] = copy.deepcopy(
                        value
                    )
                    self.assert_blocked(
                        self.invoke(request),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_allowed_not_allowed_blocked_and_changed_condition(self) -> None:
        allowed, not_allowed, blocked = self.branches()
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
                    "presence_re_evaluation_operation_"
                    "consideration_allowed"
                ],
                boundary[
                    "presence_re_evaluation_operation_"
                    "consideration_not_allowed"
                ],
            )
            self.assertEqual(
                sum(value is True for value in postures),
                expected_count,
            )
            self.assertFalse(all(value is True for value in postures))

        for result in (allowed, not_allowed):
            prior = result["prior_presence_artifact_validation"]
            receipt = result["receipt_operation_artifact_validation"]
            changed = result[
                "correspondence_and_changed_condition_validation"
            ]
            lineage = result["lineage_preservation_posture"]
            self.assertIs(prior["artifact_validated"], True)
            self.assertIs(receipt["artifact_validated"], True)
            self.assertIs(changed["changed_condition_validated"], True)
            self.assertIs(
                changed["prior_receiver_answerable_receipt_present"], False
            )
            self.assertIs(
                changed["later_receiver_answerable_receipt_present"], True
            )
            self.assertIs(
                changed["artifacts_remain_separate_standing"], True
            )
            self.assertIs(lineage["prior_presence_result_preserved"], True)
            self.assertIs(lineage["later_receipt_result_preserved"], True)
            self.assertIs(
                lineage["changed_standing_recorded_without_overwrite"], True
            )

    def test_specification_validation_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            specification_path, _, _ = self.install_fixture(root)
            self.assert_completed_branch(self.invoke(root=root), allowed=True)
            for name, marker in resolver.SPEC_REQUIRED_MARKERS:
                with self.subTest(specification_marker=name):
                    corrupted = self.specification_text.replace(
                        marker,
                        "REMOVED_SPECIFICATION_MARKER_" + name,
                    )
                    self.assertNotIn(marker, corrupted)
                    self.write_text(specification_path, corrupted)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "SPECIFICATION_MARKER_MISSING",
                    )
            self.write_text(specification_path, self.specification_text)

    def test_prior_presence_artifact_validation_matrix(self) -> None:
        metadata_cases = (
            ("resolver_module", ("resolver_module",), "wrong", "PRIOR_PRESENCE_METADATA_MISMATCH"),
            ("result_version", ("result_version",), "9.9.9", "PRIOR_PRESENCE_METADATA_MISMATCH"),
            ("outcome", ("outcome",), "WRONG", "PRIOR_PRESENCE_METADATA_MISMATCH"),
            ("failed_count", (PRIOR_SUMMARY_KEY, "failed_check_count"), 1, "PRIOR_PRESENCE_FAILED_CHECKS_PRESENT"),
            ("passed_count", (PRIOR_SUMMARY_KEY, "passed_check_count"), 445, "PRIOR_PRESENCE_METADATA_MISMATCH"),
            ("blocked", ("block", "blocked"), True, "PRIOR_PRESENCE_BLOCKED"),
            ("operation_id", (PRIOR_OPERATION_KEY, "operation_id"), "wrong", "PRIOR_PRESENCE_IDENTITY_MISMATCH"),
            ("operation_type", (PRIOR_OPERATION_KEY, "operation_type"), "wrong", "PRIOR_PRESENCE_IDENTITY_MISMATCH"),
            ("operation_version", (PRIOR_OPERATION_KEY, "operation_version"), "9", "PRIOR_PRESENCE_IDENTITY_MISMATCH"),
            ("operation_scope", (PRIOR_OPERATION_KEY, "operation_scope"), "wrong", "PRIOR_PRESENCE_IDENTITY_MISMATCH"),
            ("presence_result", (PRIOR_OPERATION_KEY, "presence_result"), "WRONG", "PRIOR_PRESENCE_RESULT_MISMATCH"),
        )
        true_locations = {
            field: (PRIOR_OPERATION_KEY, field)
            for field in resolver.PRIOR_TRUE_POSTURES
        }
        false_locations = {
            field: (PRIOR_OPERATION_KEY, field)
            for field in resolver.PRIOR_FALSE_POSTURES
        }
        invalid_true_values: tuple[object, ...] = (
            False,
            None,
            "true",
            0,
            1,
            [],
            {},
        )
        invalid_false_values: tuple[object, ...] = (
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
            _, prior_path, _ = self.install_fixture(root)
            self.assert_completed_branch(self.invoke(root=root), allowed=True)
            for label, path, value, code in metadata_cases:
                with self.subTest(prior_case=label):
                    artifact = self.prior()
                    self.set_path(artifact, path, value)
                    self.write_json(prior_path, artifact)
                    self.assert_blocked(self.invoke(root=root), code)
            for field, path in true_locations.items():
                for value in invalid_true_values:
                    with self.subTest(
                        prior_true_posture=field,
                        value=repr(value),
                    ):
                        artifact = self.prior()
                        self.set_path(artifact, path, value)
                        self.write_json(prior_path, artifact)
                        self.assert_blocked(
                            self.invoke(root=root),
                            "PRIOR_PRESENCE_TRUE_POSTURE_NOT_TRUE",
                        )
                with self.subTest(
                    prior_true_posture=field,
                    value="missing",
                ):
                    artifact = self.prior()
                    self.delete_path(artifact, path)
                    self.write_json(prior_path, artifact)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "PRIOR_PRESENCE_TRUE_POSTURE_NOT_TRUE",
                    )
            for field, path in false_locations.items():
                for value in invalid_false_values:
                    with self.subTest(
                        prior_false_posture=field,
                        value=repr(value),
                    ):
                        artifact = self.prior()
                        self.set_path(artifact, path, value)
                        self.write_json(prior_path, artifact)
                        self.assert_blocked(
                            self.invoke(root=root),
                            "PRIOR_PRESENCE_FALSE_POSTURE_NOT_FALSE",
                        )
                with self.subTest(
                    prior_false_posture=field,
                    value="missing",
                ):
                    artifact = self.prior()
                    self.delete_path(artifact, path)
                    self.write_json(prior_path, artifact)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "PRIOR_PRESENCE_FALSE_POSTURE_NOT_FALSE",
                    )
            self.write_text(prior_path, "{")
            self.assert_blocked(
                self.invoke(root=root),
                "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
            )
            self.write_text(
                prior_path,
                '{"resolver_module":"one","resolver_module":"two"}\n',
            )
            self.assert_blocked(
                self.invoke(root=root),
                "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
            )

    def test_receipt_artifact_validation_matrix(self) -> None:
        metadata_cases = (
            ("resolver_module", ("resolver_module",), "wrong", "RECEIPT_METADATA_MISMATCH"),
            ("result_version", ("result_version",), "9.9.9", "RECEIPT_METADATA_MISMATCH"),
            ("outcome", ("outcome",), "WRONG", "RECEIPT_METADATA_MISMATCH"),
            ("failed_count", ("failed_check_count",), 1, "RECEIPT_FAILED_CHECKS_PRESENT"),
            ("passed_count", ("passed_check_count",), 356, "RECEIPT_METADATA_MISMATCH"),
            ("blocked", ("block", "blocked"), True, "RECEIPT_BLOCKED"),
            ("operation_id", (RECEIPT_OPERATION_KEY, "operation_id"), "wrong", "RECEIPT_IDENTITY_MISMATCH"),
            ("operation_type", (RECEIPT_OPERATION_KEY, "operation_type"), "wrong", "RECEIPT_IDENTITY_MISMATCH"),
            ("operation_version", (RECEIPT_OPERATION_KEY, "operation_version"), "9", "RECEIPT_IDENTITY_MISMATCH"),
            ("operation_scope", (RECEIPT_OPERATION_KEY, "operation_scope"), "wrong", "RECEIPT_IDENTITY_MISMATCH"),
            ("operation_result", ("operation_result",), "WRONG", "RECEIPT_RESULT_MISMATCH"),
            ("result_count", (RECEIPT_OPERATION_KEY, "completed_result_posture_count"), 2, "RECEIPT_RESULT_CARDINALITY_MISMATCH"),
            ("canonical_non_claims_flag", ("result_level_non_claims_canonical_false",), False, "RECEIPT_NON_CLAIMS_NOT_CANONICAL_FALSE"),
            ("future_route", ("admissible_future_route",), "WRONG_ROUTE", "RECEIPT_FUTURE_ROUTE_MISMATCH"),
        )
        invalid_true_values: tuple[object, ...] = (
            False,
            None,
            "true",
            0,
            1,
            [],
            {},
        )
        invalid_false_values: tuple[object, ...] = (
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
            _, _, receipt_path = self.install_fixture(root)
            self.assert_completed_branch(self.invoke(root=root), allowed=True)
            for label, path, value, code in metadata_cases:
                with self.subTest(receipt_case=label):
                    artifact = self.receipt()
                    self.set_path(artifact, path, value)
                    self.write_json(receipt_path, artifact)
                    self.assert_blocked(self.invoke(root=root), code)
            for field in resolver.RECEIPT_TRUE_POSTURES:
                path = (RECEIPT_OPERATION_KEY, field)
                for value in invalid_true_values:
                    with self.subTest(
                        receipt_true_posture=field,
                        value=repr(value),
                    ):
                        artifact = self.receipt()
                        self.set_path(artifact, path, value)
                        self.write_json(receipt_path, artifact)
                        self.assert_blocked(
                            self.invoke(root=root),
                            "RECEIPT_TRUE_POSTURE_NOT_TRUE",
                        )
                with self.subTest(
                    receipt_true_posture=field,
                    value="missing",
                ):
                    artifact = self.receipt()
                    self.delete_path(artifact, path)
                    self.write_json(receipt_path, artifact)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "RECEIPT_TRUE_POSTURE_NOT_TRUE",
                    )
            for field in resolver.RECEIPT_FALSE_POSTURES:
                path = (RECEIPT_OPERATION_KEY, field)
                for value in invalid_false_values:
                    with self.subTest(
                        receipt_false_lock=field,
                        value=repr(value),
                    ):
                        artifact = self.receipt()
                        self.set_path(artifact, path, value)
                        self.write_json(receipt_path, artifact)
                        self.assert_blocked(
                            self.invoke(root=root),
                            "RECEIPT_FALSE_POSTURE_NOT_FALSE",
                        )
                with self.subTest(
                    receipt_false_lock=field,
                    value="missing",
                ):
                    artifact = self.receipt()
                    self.delete_path(artifact, path)
                    self.write_json(receipt_path, artifact)
                    self.assert_blocked(
                        self.invoke(root=root),
                        "RECEIPT_FALSE_POSTURE_NOT_FALSE",
                    )
            artifact = self.receipt()
            non_claims = artifact["non_claims"]
            self.assertIsInstance(non_claims, dict)
            non_claims[next(iter(non_claims))] = True
            self.write_json(receipt_path, artifact)
            self.assert_blocked(
                self.invoke(root=root),
                "RECEIPT_NON_CLAIMS_NOT_CANONICAL_FALSE",
            )
            self.write_text(receipt_path, "{")
            self.assert_blocked(
                self.invoke(root=root),
                "RECEIPT_ARTIFACT_NOT_PARSEABLE",
            )
            self.write_text(
                receipt_path,
                '{"resolver_module":"one","resolver_module":"two"}\n',
            )
            self.assert_blocked(
                self.invoke(root=root),
                "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
            )

    def test_changed_condition_correspondence_and_no_overwrite(self) -> None:
        prior_cases = (
            (
                "prior_receipt_present",
                (PRIOR_OPERATION_KEY, "receiver_answerable_receipt_present"),
                True,
            ),
        )
        receipt_cases = (
            (
                "later_receipt_absent",
                (RECEIPT_OPERATION_KEY, "receiver_answerable_receipt_present"),
                False,
            ),
            (
                "later_receipt_not_recorded",
                (RECEIPT_OPERATION_KEY, "receiver_answerable_receipt_recorded"),
                False,
            ),
            (
                "later_operation_unexhausted",
                (
                    RECEIPT_OPERATION_KEY,
                    "receiver_answerable_receipt_operation_exhausted",
                ),
                False,
            ),
            (
                "later_cardinality_wrong",
                (RECEIPT_OPERATION_KEY, "completed_result_posture_count"),
                0,
            ),
            (
                "later_route_wrong",
                ("admissible_future_route",),
                "WRONG_ROUTE",
            ),
            (
                "later_presence_lock_changed",
                (RECEIPT_OPERATION_KEY, "presence_supported"),
                True,
            ),
            (
                "later_identity_lock_changed",
                (RECEIPT_OPERATION_KEY, "identity_created"),
                True,
            ),
            (
                "later_custody_proof_changed",
                (RECEIPT_OPERATION_KEY, "custody_proven"),
                True,
            ),
            (
                "later_provenance_proof_changed",
                (RECEIPT_OPERATION_KEY, "provenance_proven"),
                True,
            ),
            (
                "later_physical_validity_proof_changed",
                (RECEIPT_OPERATION_KEY, "physical_validity_proven"),
                True,
            ),
            (
                "later_authority_lock_changed",
                (RECEIPT_OPERATION_KEY, "authority_created"),
                True,
            ),
            (
                "later_truth_lock_changed",
                (RECEIPT_OPERATION_KEY, "truth_created"),
                True,
            ),
            (
                "later_standing_lock_changed",
                (RECEIPT_OPERATION_KEY, "standing_created"),
                True,
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, prior_path, receipt_path = self.install_fixture(root)
            for label, path, value in prior_cases:
                with self.subTest(changed_condition=label):
                    artifact = self.prior()
                    self.set_path(artifact, path, value)
                    self.write_json(prior_path, artifact)
                    self.write_json(receipt_path, self.receipt())
                    self.assert_blocked(self.invoke(root=root))
            for label, path, value in receipt_cases:
                with self.subTest(changed_condition=label):
                    self.write_json(prior_path, self.prior())
                    artifact = self.receipt()
                    self.set_path(artifact, path, value)
                    self.write_json(receipt_path, artifact)
                    self.assert_blocked(self.invoke(root=root))

        mutation_flags = (
            "request_prior_presence_operation_overwrite",
            "request_prior_presence_operation_invalidation",
            "request_prior_presence_operation_supersession",
            "request_prior_presence_operation_repair",
            "request_prior_presence_operation_replacement",
            "request_prior_presence_operation_normalization",
        )
        for field in mutation_flags:
            with self.subTest(prior_mutation_request=field):
                self.assert_blocked(
                    self.invoke(self.canonical_request(**{field: True})),
                    "PROHIBITED_PRIOR_OPERATION_MUTATION_REQUESTED",
                )

        def contradictory_correspondence(
            request: Mapping[str, Any],
            prior: Mapping[str, Any],
            receipt: Mapping[str, Any],
            checks: list[dict[str, Any]],
        ) -> tuple[str, str, dict[str, Any]]:
            del request, prior, receipt
            resolver._add_failure(
                checks,
                "correspondence.changed_condition",
                "CHANGED_CONDITION_MISMATCH",
            )
            return (
                "CHANGED_CONDITION_MISMATCH",
                "changed condition absent or contradictory",
                resolver._empty_correspondence_validation(),
            )

        with patch.object(
            resolver,
            "_validate_correspondence",
            side_effect=contradictory_correspondence,
        ):
            result = self.invoke()
        self.assertIs(
            result["prior_presence_artifact_validation"][
                "artifact_validated"
            ],
            True,
        )
        self.assertIs(
            result["receipt_operation_artifact_validation"][
                "artifact_validated"
            ],
            True,
        )
        self.assert_blocked(result, "CHANGED_CONDITION_MISMATCH")

    def test_strict_json_and_from_path_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            request = self.canonical_request()
            request_path = self.write_json(root / "request.json", request)
            request_bytes = request_path.read_bytes()
            direct = self.invoke(request)
            from_path = (
                resolver.resolve_presence_re_evaluation_boundary_v0_min_from_path(
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
                        resolver.PresenceReEvaluationBoundaryV0MinError
                    ):
                        resolver.resolve_presence_re_evaluation_boundary_v0_min_from_path(
                            path
                        )
            self.assert_blocked(
                resolver.resolve_presence_re_evaluation_boundary_v0_min([])
            )

    def test_read_limits_and_no_discovery(self) -> None:
        expected_reads = (
            SPECIFICATION_PATH.resolve(),
            PRIOR_ARTIFACT_PATH.resolve(),
            RECEIPT_ARTIFACT_PATH.resolve(),
        )
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
                side_effect=AssertionError("iterdir prohibited"),
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
        self.assertEqual(reads, list(expected_reads))

    def test_lineage_perishability_non_claims_omissions_and_meaning(
        self,
    ) -> None:
        for result in self.branches():
            with self.subTest(outcome=result["outcome"]):
                lineage = result["lineage_preservation_posture"]
                self.assertEqual(
                    set(lineage), set(resolver.LINEAGE_POSTURE_FIELDS)
                )
                self.assertTrue(
                    all(value is True for value in lineage.values())
                )
                perishability = result["perishability_posture"]
                self.assertEqual(
                    set(perishability),
                    set(resolver.PERISHABILITY_POSTURE_FIELDS),
                )
                self.assertTrue(
                    all(value is True for value in perishability.values())
                )
                self.assert_non_claims(result)
                self.assert_omissions(result)
                boundary = self.boundary(result)
                for field in (
                    "durable_presence_created",
                    "permanent_presence_created",
                    "irrevocable_presence_created",
                    "self_renewing_presence_created",
                    "presence_lapse_boundary_created",
                    "presence_lapse_operation_created",
                    "presence_lapsed",
                    "presence_expired",
                    "prior_presence_operation_overwritten",
                    "prior_presence_operation_invalidated",
                    "prior_presence_operation_superseded",
                    "affected_file_repaired",
                ):
                    self.assertIs(boundary[field], False)
                self.assertIs(
                    boundary["presence_lapse_result_recorded"], False
                )
                self.assertIs(
                    boundary["scheduled_presence_re_evaluation_created"],
                    False,
                )
                self.assertIs(
                    boundary["scheduled_presence_lapse_created"], False
                )
                non_meaning = result[NON_MEANING_KEY]
                self.assertEqual(
                    set(non_meaning), set(resolver.NON_MEANING_FIELDS)
                )
                self.assertTrue(
                    all(value is True for value in non_meaning.values())
                )
                self.assertEqual(
                    result["blocked_routes"],
                    list(resolver.BLOCKED_ROUTES),
                )
                self.assertEqual(
                    result["admissible_future_route"],
                    resolver.ADMISSIBLE_FUTURE_ROUTE,
                )

        self.assertIs(
            self.canonical_request()[
                "request_contaminated_lineage_validation"
            ],
            False,
        )

    def test_complete_material_containment(self) -> None:
        sentinels = (
            "RAW_PRIOR_PRESENCE_ARTIFACT_MUST_NOT_RETURN",
            "RAW_RECEIPT_ARTIFACT_MUST_NOT_RETURN",
        )
        prior = self.prior()
        receipt = self.receipt()
        prior["untrusted_extra_material"] = {
            "body": sentinels[0],
        }
        receipt["untrusted_extra_material"] = {
            "body": sentinels[1],
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(
                root,
                prior_artifact=prior,
                receipt_artifact=receipt,
            )
            result = self.invoke(root=root)
        self.assert_completed_branch(result, allowed=True)
        serialized = json.dumps(result, sort_keys=True)
        summary_serialized = json.dumps(result[SUMMARY_KEY], sort_keys=True)
        for sentinel in sentinels:
            self.assertNotIn(sentinel, serialized)
            self.assertNotIn(sentinel, summary_serialized)
        self.assertNotIn(CHECKS_KEY, result[SUMMARY_KEY])
        self.assertFalse(
            resolver._contains_prohibited_complete_material(
                result[SUMMARY_KEY]
            )
        )

    def test_determinism_immutability_and_check_accounting(self) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        first = self.invoke(request)
        second = self.invoke(request)
        self.assertEqual(first, second)
        self.assertEqual(request, request_before)
        first_summary = (
            resolver.build_presence_re_evaluation_boundary_v0_min_summary(
                first
            )
        )
        second_summary = (
            resolver.build_presence_re_evaluation_boundary_v0_min_summary(
                copy.deepcopy(first)
            )
        )
        self.assertEqual(first_summary, second_summary)
        self.assert_counts(first)
        self.assertEqual(first["failed_check_count"], 0)
        serialized = json.dumps(first, sort_keys=True)
        for unstable_key in (
            '"created_at"',
            '"updated_at"',
            '"timestamp"',
            '"run_id"',
            '"random_seed"',
            '"environment"',
        ):
            self.assertNotIn(unstable_key, serialized)

        prior = self.prior()
        receipt = self.receipt()
        prior_before = copy.deepcopy(prior)
        receipt_before = copy.deepcopy(receipt)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, prior_path, receipt_path = self.install_fixture(
                root,
                prior_artifact=prior,
                receipt_artifact=receipt,
            )
            self.assert_completed_branch(
                self.invoke(request, root=root),
                allowed=True,
            )
            self.assertEqual(prior, prior_before)
            self.assertEqual(receipt, receipt_before)
            self.assertEqual(
                json.loads(prior_path.read_text(encoding="utf-8")),
                prior_before,
            )
            self.assertEqual(
                json.loads(receipt_path.read_text(encoding="utf-8")),
                receipt_before,
            )

    def test_summary_contract_for_every_branch(self) -> None:
        expected_keys = {
            "resolver_module",
            "result_version",
            "boundary_id",
            "boundary_type",
            "boundary_version",
            "boundary_scope",
            "specification_path",
            "prior_presence_artifact_path",
            "receipt_operation_artifact_path",
            "prior_presence_operation_id",
            "receipt_operation_id",
            "prior_required_presence_result",
            "required_receipt_result",
            "outcome",
            "boundary_result",
            "failed_check_count",
            "passed_check_count",
            "blocked",
            "decision_code",
            "decision_reason",
            "selection",
            "specification_validated",
            "prior_presence_artifact_validated",
            "receipt_operation_artifact_validated",
            "changed_condition_validated",
            "prior_receipt_absence_validated",
            "later_receipt_presence_validated",
            "prior_presence_result_preserved",
            "later_receipt_result_preserved",
            "no_overwrite_validated",
            "boundary_recorded",
            "boundary_result_recorded",
            "boundary_exhausted",
            "consideration_allowed",
            "consideration_not_allowed",
            "presence_re_evaluation_operation_absent",
            "revised_presence_result_absent",
            "presence_absent",
            "custody_distinctness_absent",
            "refusability_absent",
            "could_have_been_withheld_absent",
            "durable_presence_absent",
            "lapse_route_absent",
            "downstream_non_claims_canonical_false",
            "result_level_non_claims_canonical_false",
            "complete_material_omission_posture",
            "perishability_preserved",
            "admissible_future_route",
        }
        for result in self.branches():
            with self.subTest(outcome=result["outcome"]):
                summary = (
                    resolver.build_presence_re_evaluation_boundary_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(summary, result[SUMMARY_KEY])
                self.assertEqual(set(summary), expected_keys)
                self.assertEqual(
                    summary["resolver_module"], resolver.RESOLVER_MODULE
                )
                self.assertEqual(
                    summary["result_version"], resolver.RESULT_VERSION
                )
                self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
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
                    summary["specification_path"],
                    str(resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH),
                )
                self.assertEqual(
                    summary["prior_presence_artifact_path"],
                    str(
                        resolver.PRIOR_PRESENCE_OPERATION_ARTIFACT_RELATIVE_PATH
                    ),
                )
                self.assertEqual(
                    summary["receipt_operation_artifact_path"],
                    str(
                        resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ARTIFACT_RELATIVE_PATH
                    ),
                )
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(
                    summary["boundary_result"], result["boundary_result"]
                )
                self.assertEqual(
                    summary["failed_check_count"],
                    result["failed_check_count"],
                )
                self.assertEqual(
                    summary["passed_check_count"],
                    result["passed_check_count"],
                )
                boundary = self.boundary(result)
                block = result["block"]
                decision = result["boundary_decision"]
                specification = result["specification_validation"]
                prior = result["prior_presence_artifact_validation"]
                receipt = result["receipt_operation_artifact_validation"]
                correspondence = result[
                    "correspondence_and_changed_condition_validation"
                ]
                lineage = result["lineage_preservation_posture"]
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
                        "presence_re_evaluation_operation_"
                        "consideration_selected"
                    ],
                )
                self.assertIs(
                    summary["specification_validated"],
                    specification["specification_validated"],
                )
                self.assertIs(
                    summary["prior_presence_artifact_validated"],
                    prior["artifact_validated"],
                )
                self.assertIs(
                    summary["receipt_operation_artifact_validated"],
                    receipt["artifact_validated"],
                )
                self.assertIs(
                    summary["changed_condition_validated"],
                    correspondence["changed_condition_validated"],
                )
                self.assertIs(
                    summary["prior_receipt_absence_validated"],
                    (
                        correspondence[
                            "prior_receiver_answerable_receipt_present"
                        ]
                        is False
                    ),
                )
                self.assertIs(
                    summary["later_receipt_presence_validated"],
                    (
                        correspondence[
                            "later_receiver_answerable_receipt_present"
                        ]
                        is True
                    ),
                )
                self.assertIs(
                    summary["prior_presence_result_preserved"],
                    lineage["prior_presence_result_preserved"],
                )
                self.assertIs(
                    summary["later_receipt_result_preserved"],
                    lineage["later_receipt_result_preserved"],
                )
                self.assertIs(
                    summary["no_overwrite_validated"],
                    lineage["changed_standing_recorded_without_overwrite"],
                )
                self.assertIs(
                    summary["boundary_recorded"],
                    boundary["presence_re_evaluation_boundary_recorded"],
                )
                self.assertIs(
                    summary["boundary_result_recorded"],
                    boundary[
                        "presence_re_evaluation_boundary_result_recorded"
                    ],
                )
                self.assertIs(
                    summary["boundary_exhausted"],
                    boundary["presence_re_evaluation_boundary_exhausted"],
                )
                self.assertIs(
                    summary["consideration_allowed"],
                    boundary[
                        "presence_re_evaluation_operation_"
                        "consideration_allowed"
                    ],
                )
                self.assertIs(
                    summary["consideration_not_allowed"],
                    boundary[
                        "presence_re_evaluation_operation_"
                        "consideration_not_allowed"
                    ],
                )
                for absent_field in (
                    "presence_re_evaluation_operation_absent",
                    "revised_presence_result_absent",
                    "presence_absent",
                    "custody_distinctness_absent",
                    "refusability_absent",
                    "could_have_been_withheld_absent",
                    "durable_presence_absent",
                    "lapse_route_absent",
                    "downstream_non_claims_canonical_false",
                    "result_level_non_claims_canonical_false",
                    "complete_material_omission_posture",
                    "perishability_preserved",
                ):
                    self.assertIs(summary[absent_field], True)
                self.assertEqual(
                    summary["prior_presence_operation_id"],
                    resolver.PRIOR_PRESENCE_OPERATION_ID,
                )
                self.assertEqual(
                    summary["receipt_operation_id"],
                    resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_ID,
                )
                self.assertEqual(
                    summary["prior_required_presence_result"],
                    resolver.PRIOR_PRESENCE_RESULT_REQUIRED,
                )
                self.assertEqual(
                    summary["required_receipt_result"],
                    resolver.RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RESULT_REQUIRED,
                )
                self.assertEqual(
                    summary["admissible_future_route"],
                    resolver.ADMISSIBLE_FUTURE_ROUTE,
                )
                self.assertNotIn("checks", summary)
                self.assertNotIn(CHECKS_KEY, summary)
                self.assertFalse(
                    resolver._contains_prohibited_complete_material(summary)
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
        results = self.branches()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.CANONICAL_OUTPUT_ROOT.name
            with (
                patch.object(
                    resolver,
                    "CANONICAL_OUTPUT_ROOT",
                    output_root,
                ),
                patch.object(resolver, "OUTPUT_ROOT", output_root),
            ):
                written = [
                    resolver.write_presence_re_evaluation_boundary_v0_min_result(
                        result
                    )
                    for result in results
                ]
                expected_names = (
                    resolver.OUTPUT_FILENAME,
                    Path(resolver.OUTPUT_FILENAME).stem
                    + "_001"
                    + Path(resolver.OUTPUT_FILENAME).suffix,
                    Path(resolver.OUTPUT_FILENAME).stem
                    + "_002"
                    + Path(resolver.OUTPUT_FILENAME).suffix,
                )
                self.assertEqual(
                    tuple(path.name for path in written),
                    expected_names,
                )
                for path, result in zip(written, results):
                    self.assert_written_json(path, result)

                first_before = written[0].read_bytes()
                fourth = (
                    resolver.write_presence_re_evaluation_boundary_v0_min_result(
                        results[0]
                    )
                )
                self.assertEqual(
                    fourth.name,
                    Path(resolver.OUTPUT_FILENAME).stem
                    + "_003"
                    + Path(resolver.OUTPUT_FILENAME).suffix,
                )
                self.assertEqual(written[0].read_bytes(), first_before)

                explicit = output_root / "explicit_result.json"
                self.write_text(explicit, "existing\n")
                explicit_before = explicit.read_bytes()
                with self.assertRaises(
                    resolver.PresenceReEvaluationBoundaryV0MinError
                ):
                    resolver.write_presence_re_evaluation_boundary_v0_min_result(
                        results[0],
                        explicit,
                    )
                self.assertEqual(explicit.read_bytes(), explicit_before)

    def test_writer_refusal_matrix(self) -> None:
        allowed, not_allowed, blocked = self.branches()
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
            "wrong_identity",
            allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "boundary_id", "wrong"
            ),
        )
        changed(
            "wrong_path",
            allowed,
            lambda value: value[
                "presence_re_evaluation_boundary_metadata"
            ].__setitem__("prior_presence_artifact_path", "wrong"),
        )
        changed(
            "wrong_outcome",
            allowed,
            lambda value: value.__setitem__(
                "outcome", resolver.OUTCOME_NOT_ALLOWED
            ),
        )
        changed(
            "wrong_result",
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
            "allowed_without_allowed",
            allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "presence_re_evaluation_operation_consideration_allowed",
                False,
            ),
        )
        changed(
            "not_allowed_without_not_allowed",
            not_allowed,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "presence_re_evaluation_operation_"
                "consideration_not_allowed",
                False,
            ),
        )
        changed(
            "blocked_records_result",
            blocked,
            lambda value: value[BOUNDARY_KEY].__setitem__(
                "presence_re_evaluation_boundary_result_recorded",
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
            "lineage_false",
            allowed,
            lambda value: value["lineage_preservation_posture"].__setitem__(
                resolver.LINEAGE_POSTURE_FIELDS[0], False
            ),
        )
        changed(
            "perishability_false",
            allowed,
            lambda value: value["perishability_posture"].__setitem__(
                resolver.PERISHABILITY_POSTURE_FIELDS[0], False
            ),
        )
        changed(
            "complete_material",
            allowed,
            lambda value: value.__setitem__(
                "complete_prior_presence_artifact", {"forbidden": True}
            ),
        )
        changed(
            "wrong_route",
            allowed,
            lambda value: value.__setitem__(
                "admissible_future_route", "WRONG_ROUTE"
            ),
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.CANONICAL_OUTPUT_ROOT.name
            with (
                patch.object(
                    resolver,
                    "CANONICAL_OUTPUT_ROOT",
                    output_root,
                ),
                patch.object(resolver, "OUTPUT_ROOT", output_root),
            ):
                for label, result in invalid:
                    with self.subTest(writer_refusal=label):
                        target = output_root / (label + ".json")
                        with self.assertRaises(
                            resolver.PresenceReEvaluationBoundaryV0MinError
                        ):
                            resolver.write_presence_re_evaluation_boundary_v0_min_result(
                                result,
                                target,
                            )
                        self.assertFalse(target.exists())

    def test_writer_protected_path_refusal(self) -> None:
        result = self.invoke()
        protected = (
            PRIOR_ARTIFACT_PATH,
            RECEIPT_ARTIFACT_PATH,
            RECEIPT_BOUNDARY_ARTIFACT_PATH,
            RECEIVER_ATTESTATION_ARTIFACT_PATH,
            REPO_ROOT
            / "artifacts/actual_receiver_attestation_capture/"
            "receiver_attestation_capture_001/protected.json",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_v0_min/protected.json",
            REPO_ROOT / "artifacts/contaminated_lineage/protected.json",
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            Path(__file__).resolve(),
            REPO_ROOT / "reference/IAMMAI/protected.json",
            REPO_ROOT / "artifacts/outside_exact_output_family/result.json",
        )
        for target in protected:
            with self.subTest(protected_path=str(target)):
                existed = target.exists()
                before = target.read_bytes() if target.is_file() else None
                with self.assertRaises(
                    resolver.PresenceReEvaluationBoundaryV0MinError
                ):
                    resolver.write_presence_re_evaluation_boundary_v0_min_result(
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
