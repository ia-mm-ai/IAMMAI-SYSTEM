"""Tests for one bounded presence re-evaluation operation.

The suite admits only the exact completed re-evaluation boundary, historical
waiting presence result, later receiver attestation, and later
receiver-answerable receipt.  All mutations and writes are isolated under
temporary directories.  No live operation artifact or successor permission is
created.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest.mock import patch

import resolve_presence_re_evaluation_operation_v0_min as resolver


REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_PATH = (
    REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
)
BOUNDARY_ARTIFACT_PATH = (
    REPO_ROOT / resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH
)
PRIOR_PRESENCE_ARTIFACT_PATH = (
    REPO_ROOT / resolver.PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ATTESTATION_ARTIFACT_PATH = (
    REPO_ROOT / resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
)
RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH = (
    REPO_ROOT / resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
)
RESOLVER_PATH = Path(resolver.__file__).resolve()
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

BOUNDARY_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/PRESENCE_RE_EVALUATION_BOUNDARY_V0_MIN_TERMINAL_SUMMARY.md"
)
PRIOR_PRESENCE_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT / "spec/PRESENCE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
RECEIVER_ATTESTATION_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ATTESTATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
)
RECEIVER_ANSWERABLE_RECEIPT_TERMINAL_SUMMARY_PATH = (
    REPO_ROOT
    / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
    "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_TERMINAL_SUMMARY.md"
)

OPERATION_KEY = "presence_re_evaluation_operation"
CHECKS_KEY = "presence_re_evaluation_operation_checks"
SUMMARY_KEY = "presence_re_evaluation_operation_summary"
NON_MEANING_KEY = "presence_re_evaluation_operation_non_meaning"
BOUNDARY_KEY = "presence_re_evaluation_boundary"
PRIOR_OPERATION_KEY = "presence_operation"
PRIOR_SUMMARY_KEY = "presence_operation_summary"
ATTESTATION_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation"
)
ATTESTATION_SUMMARY_KEY = ATTESTATION_KEY + "_summary"
RECEIPT_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
)
RECEIPT_SUMMARY_KEY = RECEIPT_KEY + "_summary"

_MISSING = object()
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


class PresenceReEvaluationOperationV0MinTests(unittest.TestCase):
    """Verify the exact four-artifact operation and every bounded refusal."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            BOUNDARY_ARTIFACT_PATH,
            PRIOR_PRESENCE_ARTIFACT_PATH,
            RECEIVER_ATTESTATION_ARTIFACT_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH,
            BOUNDARY_TERMINAL_SUMMARY_PATH,
            PRIOR_PRESENCE_TERMINAL_SUMMARY_PATH,
            RECEIVER_ATTESTATION_TERMINAL_SUMMARY_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_TERMINAL_SUMMARY_PATH,
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
        cls.boundary_artifact = cls.strict_load_json(BOUNDARY_ARTIFACT_PATH)
        cls.prior_presence_artifact = cls.strict_load_json(
            PRIOR_PRESENCE_ARTIFACT_PATH
        )
        cls.receiver_attestation_artifact = cls.strict_load_json(
            RECEIVER_ATTESTATION_ARTIFACT_PATH
        )
        cls.receiver_answerable_receipt_artifact = cls.strict_load_json(
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH
        )
        for name in (
            "boundary_artifact",
            "prior_presence_artifact",
            "receiver_attestation_artifact",
            "receiver_answerable_receipt_artifact",
        ):
            if not isinstance(getattr(cls, name), dict):
                raise AssertionError(f"{name} is not a mapping")
        cls.output_snapshot = cls.snapshot_output_root()
        cls._cached_branches: tuple[dict[str, Any], ...] | None = None

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            actual = cls.sha256(path)
            if actual != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if cls.snapshot_output_root() != cls.output_snapshot:
            raise AssertionError(
                "canonical presence-re-evaluation-operation output root changed"
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

    @staticmethod
    def set_path(
        mapping: dict[str, Any],
        path: tuple[str, ...],
        value: object,
    ) -> None:
        selected = mapping
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
        selected = mapping
        for key in path[:-1]:
            nested = selected[key]
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {path}")
            selected = nested
        selected.pop(path[-1])

    @staticmethod
    def safe_name(value: object) -> str:
        safe = "".join(
            character if character.isalnum() else "_"
            for character in str(value)
        )
        return safe.strip("_") or "case"

    def canonical_request(self, **overrides: object) -> dict[str, Any]:
        return (
            resolver.build_declared_presence_re_evaluation_operation_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def boundary(self) -> dict[str, Any]:
        return copy.deepcopy(self.boundary_artifact)

    def prior(self) -> dict[str, Any]:
        return copy.deepcopy(self.prior_presence_artifact)

    def attestation(self) -> dict[str, Any]:
        return copy.deepcopy(self.receiver_attestation_artifact)

    def receipt(self) -> dict[str, Any]:
        return copy.deepcopy(self.receiver_answerable_receipt_artifact)

    def install_fixture(
        self,
        root: Path,
        *,
        specification_text: str | None = None,
        boundary_artifact: object = _MISSING,
        prior_artifact: object = _MISSING,
        attestation_artifact: object = _MISSING,
        receipt_artifact: object = _MISSING,
        raw_text: Mapping[str, str] | None = None,
        omit: str | None = None,
    ) -> dict[str, Path]:
        paths = {
            "specification": (
                root / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "boundary": root / resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH,
            "prior": root / resolver.PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH,
            "attestation": (
                root / resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
            ),
            "receipt": (
                root
                / resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
            ),
        }
        raw = dict(raw_text or {})
        values = {
            "boundary": (
                self.boundary()
                if boundary_artifact is _MISSING
                else boundary_artifact
            ),
            "prior": (
                self.prior() if prior_artifact is _MISSING else prior_artifact
            ),
            "attestation": (
                self.attestation()
                if attestation_artifact is _MISSING
                else attestation_artifact
            ),
            "receipt": (
                self.receipt()
                if receipt_artifact is _MISSING
                else receipt_artifact
            ),
        }
        if omit != "specification":
            self.write_text(
                paths["specification"],
                self.specification_text
                if specification_text is None
                else specification_text,
            )
        for key, value in values.items():
            if omit == key:
                continue
            if key in raw:
                self.write_text(paths[key], raw[key])
            else:
                self.write_json(paths[key], value)
        return paths

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
            result = resolver.resolve_presence_re_evaluation_operation_v0_min(
                supplied
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolver.resolve_presence_re_evaluation_operation_v0_min(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def invoke_fixture(
        self,
        root: Path,
        *,
        request: object = _MISSING,
        specification_text: str | None = None,
        boundary_artifact: object = _MISSING,
        prior_artifact: object = _MISSING,
        attestation_artifact: object = _MISSING,
        receipt_artifact: object = _MISSING,
        raw_text: Mapping[str, str] | None = None,
        omit: str | None = None,
    ) -> dict[str, Any]:
        self.install_fixture(
            root,
            specification_text=specification_text,
            boundary_artifact=boundary_artifact,
            prior_artifact=prior_artifact,
            attestation_artifact=attestation_artifact,
            receipt_artifact=receipt_artifact,
            raw_text=raw_text,
            omit=omit,
        )
        return self.invoke(request, root=root)

    def operation(
        self, result: Mapping[str, Any]
    ) -> dict[str, Any]:
        value = result.get(OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(
        self, result: Mapping[str, Any]
    ) -> list[dict[str, Any]]:
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
        self.assertTrue(
            all(type(item.get("passed")) is bool for item in checks)
        )
        for item in checks:
            for field in ("block_code", "failure_code"):
                if field in item:
                    self.assertIn(item[field], resolver.BLOCK_CODES)

    def assert_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for key, value in non_claims.items():
            with self.subTest(non_claim=key):
                self.assertIs(value, False)
        self.assertIs(
            result.get("result_level_non_claims_canonical_false"),
            True,
        )

    def assert_omission(self, result: Mapping[str, Any]) -> None:
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, dict)
        self.assertEqual(set(omission), set(resolver.OMISSION_POSTURE_FIELDS))
        self.assertTrue(all(value is True for value in omission.values()))
        self.assertFalse(resolver._contains_prohibited_complete_material(result))

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            result.get("presence_re_evaluation_operation_result"),
            resolver.RESULT_NOT_EVALUATED,
        )
        self.assertEqual(
            result.get("successor_presence_result"),
            resolver.RESULT_NOT_EVALUATED,
        )
        self.assertEqual(
            result.get("completed_successor_result_posture_count"), 0
        )
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(block.get("code"), expected_code)
        operation = self.operation(result)
        for field in (
            "operation_basis_admitted",
            "presence_re_evaluation_performed",
            "successor_presence_result_decided",
            "successor_presence_result_recorded",
            "presence_re_evaluation_operation_recorded",
            "presence_re_evaluation_operation_result_recorded",
            "presence_re_evaluation_operation_exhausted",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(operation.get(field), False)
        self.assertTrue(
            all(
                item.get("evaluation")
                == resolver.EVALUATION_NOT_EVALUATED
                for item in result.get("condition_evaluations", {}).values()
            )
        )
        self.assertIsNone(result.get("admissible_future_route"))
        self.assertGreater(result.get("failed_check_count", 0), 0)
        self.assert_counts(result)
        self.assert_non_claims(result)
        self.assert_omission(result)

    def assert_completed(
        self,
        result: Mapping[str, Any],
        outcome: str,
        operation_result: str,
    ) -> None:
        self.assertEqual(result.get("outcome"), outcome)
        self.assertEqual(
            result.get("presence_re_evaluation_operation_result"),
            operation_result,
        )
        self.assertEqual(result.get("successor_presence_result"), operation_result)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        operation = self.operation(result)
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "presence_re_evaluation_performed",
            "successor_presence_result_decided",
            "successor_presence_result_recorded",
            "presence_re_evaluation_operation_recorded",
            "presence_re_evaluation_operation_result_recorded",
            "presence_re_evaluation_operation_exhausted",
        ):
            self.assertIs(operation.get(field), True)
        self.assertEqual(
            operation.get("completed_successor_result_posture_count"), 1
        )
        self.assertEqual(
            result.get("completed_successor_result_posture_count"), 1
        )
        self.assert_counts(result)
        self.assert_non_claims(result)
        self.assert_omission(result)

    def make_supported_artifacts(
        self,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        attestation = self.attestation()
        receipt = self.receipt()
        attestation_operation = attestation[ATTESTATION_KEY]
        receipt_operation = receipt[RECEIPT_KEY]
        for field, required in resolver.CONDITION_REQUIREMENTS.items():
            if field not in {
                "receiver_attested",
                "receiver_answerable_receipt_present",
            }:
                attestation_operation[field] = required
                receipt_operation[field] = required
        return attestation, receipt

    def branches(self) -> tuple[dict[str, Any], ...]:
        cached = type(self)._cached_branches
        if cached is None:
            canonical = self.invoke()
            with tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                supported_attestation, supported_receipt = (
                    self.make_supported_artifacts()
                )
                supported = self.invoke_fixture(
                    root / "supported",
                    attestation_artifact=supported_attestation,
                    receipt_artifact=supported_receipt,
                )
                indeterminate_attestation = copy.deepcopy(
                    supported_attestation
                )
                indeterminate_receipt = copy.deepcopy(supported_receipt)
                indeterminate_attestation[ATTESTATION_KEY][
                    "receiver_answerable_basis_custody_distinct"
                ] = True
                indeterminate_receipt[RECEIPT_KEY][
                    "receiver_answerable_basis_custody_distinct"
                ] = False
                indeterminate = self.invoke_fixture(
                    root / "indeterminate",
                    attestation_artifact=indeterminate_attestation,
                    receipt_artifact=indeterminate_receipt,
                )
            blocked = self.invoke(
                self.canonical_request(intent=resolver.INTENT_BLOCK)
            )
            cached = (canonical, supported, indeterminate, blocked)
            type(self)._cached_branches = copy.deepcopy(cached)
        return tuple(copy.deepcopy(value) for value in cached)

    def assert_perishability(
        self, result: Mapping[str, Any]
    ) -> None:
        posture = result.get("perishability_posture")
        self.assertIsInstance(posture, dict)
        for field in (
            "presence_if_ever_supported_remains_perishable",
            "future_supported_presence_requires_separately_bounded_lapse_handling",
            "re_evaluation_does_not_create_durable_presence",
            "perishability_is_not_immediate_lapse",
            "lapse_consideration_is_not_lapse",
        ):
            self.assertIs(posture.get(field), True)
        for field in (
            "durable_presence_created",
            "permanent_presence_created",
            "irrevocable_presence_created",
            "immortal_presence_created",
            "self_renewing_presence_created",
            "presence_lapse_boundary_created",
            "presence_lapse_operation_created",
            "presence_lapse_result_recorded",
            "presence_lapsed",
            "presence_expired",
        ):
            self.assertIs(posture.get(field), False)

    def assert_separation(
        self, result: Mapping[str, Any]
    ) -> None:
        for key in (
            "prior_presence_posture",
            "later_receiver_side_posture",
            "successor_presence_evaluation_posture",
        ):
            self.assertIsInstance(result.get(key), dict)
            self.assertTrue(result.get(key))
        lineage = result.get("lineage_preservation_posture")
        self.assertIsInstance(lineage, dict)
        for field in (
            "prior_presence_result_preserved",
            "presence_re_evaluation_boundary_preserved",
            "receiver_attestation_result_preserved",
            "receiver_answerable_receipt_result_preserved",
            "successor_presence_result_additive",
            "successor_presence_result_time_scope_bounded",
            "contaminated_lineage_unchanged",
        ):
            self.assertIs(lineage.get(field), True)
        for field in (
            "prior_presence_operation_overwritten",
            "prior_presence_operation_invalidated",
            "prior_presence_operation_superseded",
            "successor_presence_is_retroactive_presence",
        ):
            self.assertIs(lineage.get(field), False)
        self.assertEqual(
            lineage.get("changed_condition"), resolver.CHANGED_CONDITION
        )

    def test_public_api_and_exact_constants(self) -> None:
        for name in (
            "build_presence_re_evaluation_operation_v0_min_request",
            "build_declared_presence_re_evaluation_operation_v0_min_request",
            "resolve_presence_re_evaluation_operation_v0_min",
            "resolve_presence_re_evaluation_operation_v0_min_from_path",
            "build_presence_re_evaluation_operation_v0_min_summary",
            "write_presence_re_evaluation_operation_v0_min_result",
        ):
            with self.subTest(public_api=name):
                self.assertTrue(callable(getattr(resolver, name, None)))
        self.assertTrue(
            issubclass(
                resolver.PresenceReEvaluationOperationV0MinError,
                Exception,
            )
        )
        expected = {
            "RESOLVER_MODULE": (
                "resolve_presence_re_evaluation_operation_v0_min"
            ),
            "RESULT_VERSION": "0.1.0",
            "OPERATION_ID": "presence_re_evaluation_operation_001",
            "OPERATION_TYPE": "PRESENCE_RE_EVALUATION_OPERATION",
            "OPERATION_VERSION": "0.1.0",
            "OPERATION_SCOPE": (
                "RE_EVALUATE_ONE_PRIOR_PRESENCE_RESULT_AFTER_ONE_RECORDED_"
                "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
            ),
            "BOUNDARY_ID": "presence_re_evaluation_boundary_001",
            "BOUNDARY_TYPE": "PRESENCE_RE_EVALUATION_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": (
                "CONSIDER_ONE_PRESENCE_RE_EVALUATION_AFTER_RECORDED_"
                "RECEIVER_ANSWERABLE_RECEIPT_ONLY"
            ),
            "BOUNDARY_RESOLVER_MODULE": (
                "resolve_presence_re_evaluation_boundary_v0_min"
            ),
            "BOUNDARY_RESULT_VERSION": "0.1.0",
            "BOUNDARY_OUTCOME_REQUIRED": (
                "PRESENCE_RE_EVALUATION_BOUNDARY_ALLOWED"
            ),
            "BOUNDARY_RESULT_REQUIRED": (
                "PRESENCE_RE_EVALUATION_OPERATION_CONSIDERATION_ALLOWED"
            ),
            "BOUNDARY_PASSED_CHECK_COUNT": 371,
            "BOUNDARY_COMPLETED_CONSIDERATION_POSTURE_COUNT": 1,
            "PRIOR_PRESENCE_OPERATION_ID": "presence_operation_001",
            "PRIOR_PRESENCE_OPERATION_TYPE": "PRESENCE_OPERATION",
            "PRIOR_PRESENCE_OPERATION_VERSION": "0.1.0",
            "PRIOR_PRESENCE_OPERATION_SCOPE": (
                "EVALUATE_PRESENCE_AFTER_BOUNDARY_ALLOWANCE_WITH_"
                "RECEIVER_ATTESTATION_REQUIREMENT_ONLY"
            ),
            "PRIOR_PRESENCE_RESOLVER_MODULE": (
                "resolve_presence_operation_v0_min"
            ),
            "PRIOR_PRESENCE_RESULT_VERSION": "0.1.0",
            "PRIOR_PRESENCE_OUTCOME_REQUIRED": (
                "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION"
            ),
            "PRIOR_PRESENCE_RESULT_REQUIRED": (
                "REQUIRES_RECEIVER_ATTESTATION"
            ),
            "PRIOR_PRESENCE_PASSED_CHECK_COUNT": 446,
            "RECEIVER_ATTESTATION_OPERATION_ID": (
                "receiver_side_answerable_basis_"
                "receiver_attestation_operation_001"
            ),
            "RECEIVER_ATTESTATION_OPERATION_TYPE": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ATTESTATION_OPERATION"
            ),
            "RECEIVER_ATTESTATION_OPERATION_VERSION": "0.1.0",
            "RECEIVER_ATTESTATION_OPERATION_SCOPE": (
                "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
                "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY"
            ),
            "RECEIVER_ATTESTATION_RESOLVER_MODULE": (
                "resolve_receiver_side_answerable_basis_"
                "receiver_attestation_operation_v0_min"
            ),
            "RECEIVER_ATTESTATION_RESULT_VERSION": "0.1.0",
            "RECEIVER_ATTESTATION_OUTCOME_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ATTESTATION_OPERATION_RECORDED"
            ),
            "RECEIVER_ATTESTATION_RESULT_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_RECORDED"
            ),
            "RECEIVER_ATTESTATION_PASSED_CHECK_COUNT": 160,
            "RECEIVER_ATTESTATION_COMPLETED_RESULT_POSTURE_COUNT": 1,
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
            "RECEIVER_ANSWERABLE_RECEIPT_RESOLVER_MODULE": (
                "resolve_receiver_side_answerable_basis_"
                "receiver_answerable_receipt_operation_v0_min"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_RESULT_VERSION": "0.1.0",
            "RECEIVER_ANSWERABLE_RECEIPT_OUTCOME_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_OPERATION_RECORDED"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_RESULT_REQUIRED": (
                "RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ANSWERABLE_RECEIPT_RECORDED"
            ),
            "RECEIVER_ANSWERABLE_RECEIPT_PASSED_CHECK_COUNT": 357,
            "RECEIVER_ANSWERABLE_RECEIPT_COMPLETED_RESULT_POSTURE_COUNT": 1,
        }
        for name, value in expected.items():
            with self.subTest(constant=name):
                self.assertEqual(getattr(resolver, name), value)
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "PRESENCE_RE_EVALUATION_OPERATION_SUPPORTED",
                "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS",
                "PRESENCE_RE_EVALUATION_OPERATION_INDETERMINATE",
                "PRESENCE_RE_EVALUATION_OPERATION_BLOCKED",
            ),
        )
        self.assertEqual(
            resolver.RESULT_FAMILY,
            (
                "PRESENCE_SUPPORTED",
                "REQUIRES_RECEIVER_ANSWERABLE_BASIS",
                "PRESENCE_INDETERMINATE",
                "NOT_EVALUATED",
            ),
        )
        self.assertEqual(
            resolver.EVALUATION_FAMILY,
            ("SATISFIED", "REQUIRES_BASIS", "INDETERMINATE", "NOT_EVALUATED"),
        )
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH,
            Path("spec/PRESENCE_RE_EVALUATION_OPERATION_V0_MIN_SPEC.md"),
        )
        self.assertEqual(
            resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH,
            BOUNDARY_ARTIFACT_PATH.relative_to(REPO_ROOT),
        )
        self.assertEqual(
            resolver.PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH,
            PRIOR_PRESENCE_ARTIFACT_PATH.relative_to(REPO_ROOT),
        )
        self.assertEqual(
            resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ATTESTATION_ARTIFACT_PATH.relative_to(REPO_ROOT),
        )
        self.assertEqual(
            resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH.relative_to(REPO_ROOT),
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "presence_re_evaluation_operation_001__"
            "presence_re_evaluation_operation_v0_min_result.json",
        )
        self.assertEqual(resolver.OUTPUT_ROOT, CANONICAL_OUTPUT_ROOT)

    def test_canonical_request_and_declared_override_contract(self) -> None:
        first = resolver.build_presence_re_evaluation_operation_v0_min_request()
        second = resolver.build_presence_re_evaluation_operation_v0_min_request()
        self.assertIsInstance(first, dict)
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(first["declared_non_claims"], second["declared_non_claims"])
        self.assertEqual(set(first), resolver._canonical_request_keys())
        self.assertEqual(first["intent"], resolver.INTENT_RECORD)
        self.assertEqual(first["operation_id"], resolver.OPERATION_ID)
        self.assertEqual(first["operation_type"], resolver.OPERATION_TYPE)
        self.assertEqual(first["operation_version"], resolver.OPERATION_VERSION)
        self.assertEqual(first["operation_scope"], resolver.OPERATION_SCOPE)
        self.assertIs(first["presence_re_evaluation_execution_selected"], True)
        self.assertEqual(
            set(first["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(value is False for value in first["declared_non_claims"].values())
        )
        self.assertFalse(set(first).intersection(resolver.PROHIBITED_PRECLAIM_FIELDS))
        for prohibited in (
            "outcome",
            "successor_presence_result",
            "condition_evaluations",
            "semantic_payload",
        ):
            self.assertNotIn(prohibited, first)

        nested = {"inner": [False]}
        declared = (
            resolver.build_declared_presence_re_evaluation_operation_v0_min_request(
                unknown_field=nested
            )
        )
        nested["inner"][0] = True
        self.assertEqual(declared["unknown_field"], {"inner": [False]})
        self.assert_blocked(
            self.invoke(declared), "REQUEST_UNKNOWN_FIELD"
        )
        false_selection = self.canonical_request(
            presence_re_evaluation_execution_selected=False
        )
        self.assertIs(
            false_selection["presence_re_evaluation_execution_selected"],
            False,
        )
        self.assert_blocked(
            self.invoke(false_selection), "REQUEST_VALUE_MISMATCH"
        )
        malformed = self.canonical_request(operation_id={"wrong": True})
        self.assertEqual(malformed["operation_id"], {"wrong": True})
        self.assert_blocked(
            self.invoke(malformed), "REQUEST_VALUE_MISMATCH"
        )

    def test_exact_boolean_request_matrix(self) -> None:
        canonical = self.canonical_request()
        self.assertEqual(self.invoke(canonical)["failed_check_count"], 0)
        for value in (False, *INVALID_BOOLEAN_VALUES):
            request = self.canonical_request(
                presence_re_evaluation_execution_selected=copy.deepcopy(value)
            )
            with self.subTest(selection=value):
                result = self.invoke(request)
                self.assert_blocked(result)
                if type(value) is not bool:
                    self.assertEqual(
                        result["block"]["code"], "REQUEST_BOOLEAN_REQUIRED"
                    )

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            for value in (True, *INVALID_BOOLEAN_VALUES):
                request = self.canonical_request()
                request["declared_non_claims"][key] = copy.deepcopy(value)
                with self.subTest(non_claim=key, value=repr(value)):
                    self.assert_blocked(
                        self.invoke(request), "NON_CLAIM_MISSING_OR_FLIPPED"
                    )
            request = self.canonical_request()
            self.assertIs(request["declared_non_claims"][key], False)

    def test_canonical_requires_basis_branch_and_condition_matrix(self) -> None:
        result = self.invoke()
        self.assert_completed(
            result,
            resolver.OUTCOME_REQUIRES_BASIS,
            resolver.RESULT_REQUIRES_BASIS,
        )
        self.assertEqual(
            result["operation_decision"]["decision_code"],
            resolver.DECISION_CODE_REQUIRES_BASIS,
        )
        self.assertEqual(
            result["operation_decision"]["decision_reason"],
            resolver.DECISION_REASON_REQUIRES_BASIS,
        )
        atomic = result["atomic_operation_basis_posture"]
        for field in (
            "boundary_artifact_validated",
            "prior_presence_artifact_validated",
            "receiver_attestation_artifact_validated",
            "receiver_answerable_receipt_artifact_validated",
            "all_four_exact_artifacts_validated",
            "operation_basis_admitted",
        ):
            self.assertIs(atomic[field], True)
        operation = self.operation(result)
        self.assertIs(
            operation[
                "presence_re_evaluation_operation_requires_receiver_answerable_basis"
            ],
            True,
        )
        self.assertIs(operation["receiver_answerable_basis_required"], True)
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(operation[field], False)
        self.assertTrue(
            result["missing_or_insufficient_receiver_answerable_basis"]
        )
        self.assertIsNone(result["admissible_future_route"])

        evaluations = result["condition_evaluations"]
        self.assertEqual(set(evaluations), set(resolver.CONDITION_KEYS))
        expected_fields = {
            "historical_prior_value",
            "later_compact_standing",
            "required_successor_value",
            "evaluation",
            "successor_value",
            "compact_evidence_code",
            "reason",
        }
        for field, item in evaluations.items():
            with self.subTest(condition=field):
                self.assertEqual(set(item), expected_fields)
                self.assertEqual(
                    set(item["later_compact_standing"]),
                    {
                        "receiver_attestation_value",
                        "receiver_answerable_receipt_value",
                    },
                )
                self.assertIs(
                    item["required_successor_value"],
                    resolver.CONDITION_REQUIREMENTS[field],
                )
                self.assertIsInstance(item["successor_value"], bool)
                self.assertIsInstance(item["compact_evidence_code"], str)
                self.assertTrue(item["compact_evidence_code"])
                self.assertIsInstance(item["reason"], str)
                self.assertTrue(item["reason"])
        self.assertEqual(
            evaluations["receiver_attested"]["evaluation"],
            resolver.EVALUATION_SATISFIED,
        )
        self.assertEqual(
            evaluations["receiver_answerable_receipt_present"]["evaluation"],
            resolver.EVALUATION_SATISFIED,
        )
        for field in (
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            self.assertEqual(
                evaluations[field]["evaluation"],
                resolver.EVALUATION_REQUIRES_BASIS,
            )
            self.assertIs(evaluations[field]["successor_value"], False)
            self.assertEqual(
                evaluations[field]["compact_evidence_code"],
                "EXACT_SUCCESSOR_CONDITION_NOT_ESTABLISHED",
            )
        summary = result[SUMMARY_KEY]
        counts = {
            evaluation: sum(
                item["evaluation"] == evaluation
                for item in evaluations.values()
            )
            for evaluation in resolver.EVALUATION_FAMILY
        }
        self.assertEqual(summary["condition_evaluation_counts"], counts)
        self.assert_separation(result)
        self.assert_perishability(result)

    def test_branch_mechanics_and_precedence(self) -> None:
        requires_basis, supported, indeterminate, blocked = self.branches()
        self.assert_completed(
            requires_basis,
            resolver.OUTCOME_REQUIRES_BASIS,
            resolver.RESULT_REQUIRES_BASIS,
        )
        self.assert_completed(
            supported,
            resolver.OUTCOME_SUPPORTED,
            resolver.RESULT_SUPPORTED,
        )
        supported_operation = self.operation(supported)
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(supported_operation[field], True)
        self.assertTrue(
            all(
                item["evaluation"] == resolver.EVALUATION_SATISFIED
                for item in supported["condition_evaluations"].values()
            )
        )
        self.assertEqual(
            supported["missing_or_insufficient_receiver_answerable_basis"],
            [],
        )
        self.assertEqual(
            supported["indeterminate_receiver_answerable_basis_conditions"],
            [],
        )
        self.assertEqual(
            supported["admissible_future_route"],
            resolver.SUPPORTED_FUTURE_ROUTE,
        )
        perishability = supported["perishability_posture"]
        self.assertIs(perishability["supported_presence_is_perishable"], True)
        self.assertEqual(
            perishability["supported_presence_ending_posture"],
            resolver.SUPPORTED_PRESENCE_ENDING_POSTURE,
        )
        self.assertIs(
            perishability[
                "supported_presence_silently_persists_beyond_admitted_basis"
            ],
            False,
        )

        self.assert_completed(
            indeterminate,
            resolver.OUTCOME_INDETERMINATE,
            resolver.RESULT_INDETERMINATE,
        )
        self.assertTrue(
            indeterminate[
                "indeterminate_receiver_answerable_basis_conditions"
            ]
        )
        self.assertEqual(
            indeterminate["operation_decision"]["decision_code"],
            resolver.DECISION_CODE_INDETERMINATE,
        )
        self.assertIsNone(indeterminate["admissible_future_route"])
        indeterminate_operation = self.operation(indeterminate)
        self.assertIs(
            indeterminate_operation["presence_re_evaluation_indeterminate"],
            True,
        )
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "automatic_presence_re_evaluation_operation_retry_created",
        ):
            self.assertIs(indeterminate_operation[field], False)
        self.assert_blocked(blocked, "EXPLICIT_BLOCK_REQUESTED")

        precedence_cases = (
            (
                "indeterminate_over_requires",
                [
                    resolver.EVALUATION_REQUIRES_BASIS,
                    resolver.EVALUATION_INDETERMINATE,
                    resolver.EVALUATION_SATISFIED,
                ],
                resolver.OUTCOME_INDETERMINATE,
            ),
            (
                "requires_over_satisfied",
                [
                    resolver.EVALUATION_SATISFIED,
                    resolver.EVALUATION_REQUIRES_BASIS,
                ],
                resolver.OUTCOME_REQUIRES_BASIS,
            ),
            (
                "all_satisfied",
                [resolver.EVALUATION_SATISFIED] * 2,
                resolver.OUTCOME_SUPPORTED,
            ),
        )
        for label, values, expected in precedence_cases:
            evaluations = {
                field: {
                    "evaluation": values[index % len(values)]
                }
                for index, field in enumerate(resolver.CONDITION_KEYS)
            }
            if label == "all_satisfied":
                evaluations = {
                    field: {"evaluation": resolver.EVALUATION_SATISFIED}
                    for field in resolver.CONDITION_KEYS
                }
            with self.subTest(precedence=label):
                self.assertEqual(
                    resolver._outcome_from_evaluations(evaluations),
                    expected,
                )

    def test_specification_marker_validation_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (name, marker) in enumerate(
                resolver.SPEC_REQUIRED_MARKERS
            ):
                self.assertIn(marker, self.specification_text)
                mutated = self.specification_text.replace(
                    marker, f"MISSING_{name}"
                )
                with self.subTest(specification_marker=name):
                    result = self.invoke_fixture(
                        base / f"{index:03d}_{self.safe_name(name)}",
                        specification_text=mutated,
                    )
                    self.assert_blocked(
                        result, "SPECIFICATION_MARKER_MISSING"
                    )
                    self.assertIs(
                        result["specification_validation"][
                            "marker_validation"
                        ][name],
                        False,
                    )

    def test_boundary_artifact_validation_matrix(self) -> None:
        cases: list[
            tuple[str, tuple[str, ...], object]
        ] = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("boundary_result_wrapper", ("boundary_result",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 370),
            (
                "completed_wrapper_count",
                ("completed_consideration_posture_count",),
                2,
            ),
            ("blocked", ("block", "blocked"), True),
        ]
        for field in (
            "boundary_id",
            "boundary_type",
            "boundary_version",
            "boundary_scope",
            "presence_re_evaluation_boundary_id",
            "presence_re_evaluation_boundary_type",
            "presence_re_evaluation_boundary_version",
            "presence_re_evaluation_boundary_scope",
        ):
            cases.append(
                (field, (BOUNDARY_KEY, field), "wrong")
            )
        for field, value in (
            ("presence_re_evaluation_boundary_result", "wrong"),
            ("presence_re_evaluation_boundary_recorded", False),
            ("presence_re_evaluation_boundary_result_recorded", False),
            ("presence_re_evaluation_boundary_exhausted", False),
            (
                "presence_re_evaluation_operation_consideration_allowed",
                False,
            ),
            (
                "presence_re_evaluation_operation_consideration_not_allowed",
                True,
            ),
            ("completed_consideration_posture_count", 2),
        ):
            cases.append((field, (BOUNDARY_KEY, field), value))
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, path, value) in enumerate(cases):
                artifact = self.boundary()
                self.set_path(artifact, path, value)
                with self.subTest(boundary_case=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"case_{index:03d}",
                            boundary_artifact=artifact,
                        )
                    )
            for index, value in enumerate(INVALID_BOOLEAN_VALUES):
                artifact = self.boundary()
                artifact[BOUNDARY_KEY][
                    "presence_re_evaluation_boundary_recorded"
                ] = copy.deepcopy(value)
                with self.subTest(boundary_boolean=repr(value)):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"boolean_{index:03d}",
                            boundary_artifact=artifact,
                        )
                    )
            for index, (label, text, expected) in enumerate(
                (
                    ("malformed", "{", "BOUNDARY_ARTIFACT_NOT_PARSEABLE"),
                    (
                        "duplicate",
                        '{"x": 1, "x": 2}',
                        "BOUNDARY_ARTIFACT_DUPLICATE_KEYED",
                    ),
                )
            ):
                with self.subTest(boundary_json=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"json_{index:03d}",
                            raw_text={"boundary": text},
                        ),
                        expected,
                    )

    def test_prior_presence_artifact_validation_matrix(self) -> None:
        cases: list[tuple[str, tuple[str, ...], object]] = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("summary_outcome", (PRIOR_SUMMARY_KEY, "outcome"), "wrong"),
            (
                "summary_result",
                (PRIOR_SUMMARY_KEY, "presence_result"),
                "wrong",
            ),
            (
                "failed_count",
                (PRIOR_SUMMARY_KEY, "failed_check_count"),
                1,
            ),
            (
                "passed_count",
                (PRIOR_SUMMARY_KEY, "passed_check_count"),
                445,
            ),
            ("blocked", ("block", "blocked"), True),
        ]
        for field in (
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "presence_operation_id",
            "presence_operation_type",
            "presence_operation_version",
            "presence_operation_scope",
        ):
            cases.append((field, (PRIOR_OPERATION_KEY, field), "wrong"))
        for field, value in (
            ("presence_result", "wrong"),
            ("presence_operation_recorded", False),
            ("presence_evaluation_performed", False),
            ("presence_result_recorded", False),
            ("receiver_attested", True),
            ("receiver_answerable_receipt_present", True),
            ("receiver_answerable_basis_custody_distinct", True),
            ("receiver_answerable_basis_refusable", True),
            ("receiver_answerable_basis_could_have_been_withheld", True),
            ("presence_supported", True),
            ("presence_authorized", True),
            ("presence_established", True),
            ("presence_recorded", True),
        ):
            cases.append((field, (PRIOR_OPERATION_KEY, field), value))
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, path, value) in enumerate(cases):
                artifact = self.prior()
                self.set_path(artifact, path, value)
                with self.subTest(prior_case=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"case_{index:03d}",
                            prior_artifact=artifact,
                        )
                    )
            for index, value in enumerate(INVALID_BOOLEAN_VALUES):
                artifact = self.prior()
                artifact[PRIOR_OPERATION_KEY][
                    "presence_operation_recorded"
                ] = copy.deepcopy(value)
                with self.subTest(prior_boolean=repr(value)):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"boolean_{index:03d}",
                            prior_artifact=artifact,
                        )
                    )
            for index, (label, text, expected) in enumerate(
                (
                    (
                        "malformed",
                        "{",
                        "PRIOR_PRESENCE_ARTIFACT_NOT_PARSEABLE",
                    ),
                    (
                        "duplicate",
                        '{"x": 1, "x": 2}',
                        "PRIOR_PRESENCE_ARTIFACT_DUPLICATE_KEYED",
                    ),
                )
            ):
                with self.subTest(prior_json=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"json_{index:03d}",
                            raw_text={"prior": text},
                        ),
                        expected,
                    )

    def test_receiver_attestation_artifact_validation_matrix(self) -> None:
        cases: list[tuple[str, tuple[str, ...], object]] = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 159),
            ("blocked", ("block", "blocked"), True),
        ]
        for field in (
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "receiver_side_answerable_basis_candidate_id",
            "selected_candidate_sufficiency_operation_id",
            "selected_candidate_sufficiency_operation_result_required",
        ):
            cases.append((field, (ATTESTATION_KEY, field), "wrong"))
        for field, value in (
            ("receiver_attestation_operation_result", "wrong"),
            ("operation_basis_supplied", False),
            ("operation_basis_admitted", False),
            ("receiver_attestation_decided", False),
            ("receiver_attestation_recorded", False),
            ("receiver_attestation_operation_recorded", False),
            ("receiver_attestation_operation_result_recorded", False),
            ("receiver_attestation_operation_exhausted", False),
            ("receiver_attestation_not_recorded", True),
            ("receiver_attestation_indeterminate", True),
        ):
            cases.append((field, (ATTESTATION_KEY, field), value))
        cases.append(
            (
                "completed_count",
                ("operation_result_detail", "completed_result_posture_count"),
                2,
            )
        )
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            index = 0
            for label, path, value in cases:
                artifact = self.attestation()
                self.set_path(artifact, path, value)
                with self.subTest(attestation_case=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"case_{index:03d}",
                            attestation_artifact=artifact,
                        )
                    )
                index += 1
            for field in resolver.ATTESTATION_REQUIRED_FALSE_POSTURES:
                for value in (True, "false"):
                    artifact = self.attestation()
                    artifact[ATTESTATION_KEY][field] = value
                    with self.subTest(
                        attestation_false_lock=field,
                        value=repr(value),
                    ):
                        self.assert_blocked(
                            self.invoke_fixture(
                                base / f"false_lock_{index:03d}",
                                attestation_artifact=artifact,
                            ),
                            "RECEIVER_ATTESTATION_FALSE_LOCK_MISMATCH",
                        )
                    index += 1
            for value in INVALID_BOOLEAN_VALUES:
                artifact = self.attestation()
                artifact[ATTESTATION_KEY][
                    "receiver_attestation_recorded"
                ] = copy.deepcopy(value)
                with self.subTest(attestation_boolean=repr(value)):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"boolean_{index:03d}",
                            attestation_artifact=artifact,
                        )
                    )
                index += 1
            for label, text, expected in (
                (
                    "malformed",
                    "{",
                    "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE",
                ),
                (
                    "duplicate",
                    '{"x": 1, "x": 2}',
                    "RECEIVER_ATTESTATION_ARTIFACT_DUPLICATE_KEYED",
                ),
            ):
                with self.subTest(attestation_json=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"json_{index:03d}",
                            raw_text={"attestation": text},
                        ),
                        expected,
                    )
                index += 1

    def test_receiver_answerable_receipt_artifact_validation_matrix(
        self,
    ) -> None:
        cases: list[tuple[str, tuple[str, ...], object]] = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("operation_result_wrapper", ("operation_result",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 356),
            ("blocked", ("block", "blocked"), True),
        ]
        for field in (
            "operation_id",
            "operation_type",
            "operation_version",
            "operation_scope",
            "selected_receiver_attestation_operation_id",
            "selected_receiver_attestation_operation_type",
            "selected_receiver_attestation_operation_version",
            "selected_receiver_attestation_operation_scope",
            "selected_receiver_attestation_operation_result_required",
            "receiver_side_answerable_basis_candidate_id",
        ):
            cases.append((field, (RECEIPT_KEY, field), "wrong"))
        for field, value in (
            ("receiver_answerable_receipt_operation_result", "wrong"),
            ("operation_basis_supplied", False),
            ("operation_basis_admitted", False),
            ("receiver_answerable_receipt_decided", False),
            ("receiver_answerable_receipt_recorded", False),
            ("receiver_answerable_receipt_present", False),
            ("receiver_answerable_receipt_operation_recorded", False),
            (
                "receiver_answerable_receipt_operation_result_recorded",
                False,
            ),
            ("receiver_answerable_receipt_operation_exhausted", False),
            ("receiver_answerable_receipt_not_recorded", True),
            ("receiver_answerable_receipt_indeterminate", True),
        ):
            cases.append((field, (RECEIPT_KEY, field), value))
        cases.append(
            (
                "completed_count",
                ("operation_result_detail", "completed_result_posture_count"),
                2,
            )
        )
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            index = 0
            for label, path, value in cases:
                artifact = self.receipt()
                self.set_path(artifact, path, value)
                with self.subTest(receipt_case=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"case_{index:03d}",
                            receipt_artifact=artifact,
                        )
                    )
                index += 1
            for field in resolver.RECEIPT_REQUIRED_FALSE_POSTURES:
                for value in (True, "false"):
                    artifact = self.receipt()
                    artifact[RECEIPT_KEY][field] = value
                    with self.subTest(
                        receipt_false_lock=field,
                        value=repr(value),
                    ):
                        self.assert_blocked(
                            self.invoke_fixture(
                                base / f"false_lock_{index:03d}",
                                receipt_artifact=artifact,
                            ),
                            "RECEIPT_FALSE_LOCK_MISMATCH",
                        )
                    index += 1
            for value in INVALID_BOOLEAN_VALUES:
                artifact = self.receipt()
                artifact[RECEIPT_KEY][
                    "receiver_answerable_receipt_recorded"
                ] = copy.deepcopy(value)
                with self.subTest(receipt_boolean=repr(value)):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"boolean_{index:03d}",
                            receipt_artifact=artifact,
                        )
                    )
                index += 1
            for label, text, expected in (
                ("malformed", "{", "RECEIPT_ARTIFACT_NOT_PARSEABLE"),
                (
                    "duplicate",
                    '{"x": 1, "x": 2}',
                    "RECEIPT_ARTIFACT_DUPLICATE_KEYED",
                ),
            ):
                with self.subTest(receipt_json=label):
                    self.assert_blocked(
                        self.invoke_fixture(
                            base / f"json_{index:03d}",
                            raw_text={"receipt": text},
                        ),
                        expected,
                    )
                index += 1

    def test_atomic_basis_missing_corrupt_and_partial_never_complete(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, artifact_name in enumerate(
                ("boundary", "prior", "attestation", "receipt")
            ):
                with self.subTest(missing=artifact_name):
                    result = self.invoke_fixture(
                        base / f"missing_{index:03d}",
                        omit=artifact_name,
                    )
                    self.assert_blocked(result)
                    self.assertIs(
                        result["atomic_operation_basis_posture"][
                            "operation_basis_admitted"
                        ],
                        False,
                    )
                with self.subTest(corrupt=artifact_name):
                    result = self.invoke_fixture(
                        base / f"corrupt_{index:03d}",
                        raw_text={artifact_name: "{"},
                    )
                    self.assert_blocked(result)
                    self.assertEqual(
                        result["completed_successor_result_posture_count"], 0
                    )
            non_mapping = self.invoke([])
            self.assert_blocked(non_mapping, "REQUEST_NOT_MAPPING")
            unsupported = self.invoke(
                self.canonical_request(intent="UNSUPPORTED")
            )
            self.assert_blocked(unsupported, "UNSUPPORTED_INTENT")

    def test_condition_anti_inference_and_no_recursive_noise(self) -> None:
        canonical = self.invoke()
        evaluations = canonical["condition_evaluations"]
        for field in (
            "receiver_answerable_basis_custody_distinct",
            "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld",
        ):
            item = evaluations[field]
            self.assertEqual(
                item["evaluation"], resolver.EVALUATION_REQUIRES_BASIS
            )
            self.assertIs(item["successor_value"], False)
            self.assertIsNone(
                item["later_compact_standing"][
                    "receiver_attestation_value"
                ]
            )
            self.assertIsNone(
                item["later_compact_standing"][
                    "receiver_answerable_receipt_value"
                ]
            )
            self.assertIn(
                field,
                canonical[
                    "missing_or_insufficient_receiver_answerable_basis"
                ],
            )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            attestation = self.attestation()
            receipt = self.receipt()
            for artifact in (attestation, receipt):
                artifact["unrelated_nested_claims"] = {
                    "candidate_sufficiency": {
                        "receiver_answerable_basis_custody_distinct": True,
                        "receiver_answerable_basis_refusable": True,
                        "receiver_answerable_basis_could_have_been_withheld": True,
                    },
                    "artifact_exists": True,
                    "historical_false_posture": False,
                }
            result = self.invoke_fixture(
                root,
                attestation_artifact=attestation,
                receipt_artifact=receipt,
            )
            for field in (
                "receiver_answerable_basis_custody_distinct",
                "receiver_answerable_basis_refusable",
                "receiver_answerable_basis_could_have_been_withheld",
            ):
                self.assertEqual(
                    result["condition_evaluations"][field]["evaluation"],
                    resolver.EVALUATION_REQUIRES_BASIS,
                )
        serialized = json.dumps(canonical, sort_keys=True)
        self.assertNotIn("unrelated_nested_claims", serialized)

    def test_separation_perishability_nonclaims_omission_and_lineage(
        self,
    ) -> None:
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                if result["outcome"] == resolver.OUTCOME_BLOCKED:
                    for key in (
                        "prior_presence_posture",
                        "later_receiver_side_posture",
                        "successor_presence_evaluation_posture",
                    ):
                        self.assertIsInstance(result.get(key), dict)
                else:
                    self.assert_separation(result)
                self.assert_perishability(result)
                self.assert_non_claims(result)
                self.assert_omission(result)
                operation = self.operation(result)
                for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                    self.assertIs(operation[field], False)
                for field in (
                    "affected_file_repaired",
                    "repository_scan_performed",
                    "file_discovery_performed",
                    "validation_enforced",
                    "prior_unsupported_candidate_a_claim_validated",
                    "prior_unsupported_candidate_b_claim_validated",
                    "prior_unsupported_derivation_event_claim_validated",
                ):
                    self.assertIs(operation[field], False)
                self.assertIs(
                    result["lineage_preservation_posture"][
                        "contaminated_lineage_unchanged"
                    ],
                    True,
                )

    def test_read_limits_and_no_discovery(self) -> None:
        allowed = {
            SPECIFICATION_PATH.resolve(),
            BOUNDARY_ARTIFACT_PATH.resolve(),
            PRIOR_PRESENCE_ARTIFACT_PATH.resolve(),
            RECEIVER_ATTESTATION_ARTIFACT_PATH.resolve(),
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH.resolve(),
        }
        accessed: list[Path] = []
        original_read_text = Path.read_text

        def guarded_read_text(
            path: Path, *args: object, **kwargs: object
        ) -> str:
            resolved = path.resolve()
            accessed.append(resolved)
            if resolved not in allowed:
                raise AssertionError(f"prohibited read: {resolved}")
            return original_read_text(path, *args, **kwargs)

        with (
            patch.object(Path, "read_text", guarded_read_text),
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
            patch.object(
                os,
                "listdir",
                side_effect=AssertionError("listdir prohibited"),
            ),
        ):
            result = self.invoke()
        self.assertEqual(set(accessed), allowed)
        self.assertEqual(len(accessed), 5)
        self.assertEqual(result["failed_check_count"], 0)

    def test_strict_json_and_from_path_contract(self) -> None:
        request = self.canonical_request()
        direct = self.invoke(request)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            valid_path = self.write_json(root / "valid.json", request)
            valid_before = valid_path.read_bytes()
            from_path = (
                resolver.resolve_presence_re_evaluation_operation_v0_min_from_path(
                    valid_path
                )
            )
            self.assertEqual(from_path, direct)
            self.assertEqual(valid_path.read_bytes(), valid_before)

            duplicate = self.write_text(
                root / "duplicate.json",
                '{"intent": "a", "intent": "b"}',
            )
            malformed = self.write_text(root / "malformed.json", "{")
            array = self.write_text(root / "array.json", "[]")
            malformed_utf8 = root / "malformed_utf8.json"
            malformed_utf8.write_bytes(b"\xff\xfe")
            missing = root / "missing.json"
            for path in (
                duplicate,
                malformed,
                array,
                malformed_utf8,
                missing,
            ):
                with self.subTest(request_path=path.name):
                    with self.assertRaises(
                        resolver.PresenceReEvaluationOperationV0MinError
                    ):
                        resolver.resolve_presence_re_evaluation_operation_v0_min_from_path(
                            path
                        )
        self.assert_blocked(self.invoke({"intent": "wrong"}))

    def test_non_meaning_and_blocked_routes(self) -> None:
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                self.assertEqual(
                    result["blocked_routes"], list(resolver.BLOCKED_ROUTES)
                )
                non_meaning = result[NON_MEANING_KEY]
                self.assertEqual(
                    set(non_meaning), set(resolver.NON_MEANING_FIELDS)
                )
                self.assertTrue(
                    all(value is True for value in non_meaning.values())
                )
                for field in (
                    "prior_lawful_waiting_result_is_not_error",
                    "changed_standing_is_not_silent_overwrite",
                    "boundary_is_not_re_evaluation_operation",
                    "basis_admission_is_not_successor_result_selection",
                    "receipt_is_not_presence",
                    "receipt_presence_is_not_complete_basis_satisfaction",
                    "receiver_attestation_is_not_presence",
                    "custody_distinctness_is_not_custody_proof",
                    "refusability_is_not_refusal",
                    "could_have_been_withheld_is_not_actual_withholding",
                    "successor_presence_is_not_retroactive_presence",
                    "supported_presence_is_perishable",
                    "perishability_is_not_immediate_lapse",
                    "operation_exhaustion_is_not_durable_presence",
                    "open_does_not_mean_next",
                ):
                    self.assertIs(non_meaning[field], True)

    def test_summary_determinism_compactness_and_branch_fields(self) -> None:
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                first = (
                    resolver.build_presence_re_evaluation_operation_v0_min_summary(
                        result
                    )
                )
                second = (
                    resolver.build_presence_re_evaluation_operation_v0_min_summary(
                        copy.deepcopy(result)
                    )
                )
                self.assertEqual(first, second)
                self.assertEqual(first, result[SUMMARY_KEY])
                for field in (
                    "resolver_module",
                    "result_version",
                    "operation_id",
                    "operation_type",
                    "operation_version",
                    "operation_scope",
                    "specification_path",
                    "boundary_artifact_path",
                    "prior_presence_artifact_path",
                    "receiver_attestation_artifact_path",
                    "receiver_answerable_receipt_artifact_path",
                    "outcome",
                    "operation_result",
                    "successor_presence_result",
                    "failed_check_count",
                    "passed_check_count",
                    "blocked",
                    "decision_code",
                    "decision_reason",
                    "execution_selected",
                    "specification_validated",
                    "boundary_artifact_validated",
                    "prior_presence_artifact_validated",
                    "receiver_attestation_artifact_validated",
                    "receiver_answerable_receipt_artifact_validated",
                    "operation_basis_supplied",
                    "operation_basis_admitted",
                    "presence_re_evaluation_performed",
                    "successor_presence_result_decided",
                    "successor_presence_result_recorded",
                    "presence_re_evaluation_operation_recorded",
                    "presence_re_evaluation_operation_result_recorded",
                    "presence_re_evaluation_operation_exhausted",
                    "completed_successor_result_posture_count",
                    "prior_presence_result_preserved",
                    "presence_re_evaluation_boundary_preserved",
                    "receiver_attestation_result_preserved",
                    "receiver_answerable_receipt_result_preserved",
                    "changed_condition",
                    "no_overwrite",
                    "successor_additive",
                    "successor_time_scope_bounded",
                    "no_retroactive_presence",
                    "condition_evaluation_counts",
                    "missing_or_insufficient_receiver_answerable_basis",
                    "indeterminate_receiver_answerable_basis_conditions",
                    "presence_supported",
                    "presence_authorized",
                    "presence_established",
                    "presence_recorded",
                    "requires_receiver_answerable_basis",
                    "receiver_answerable_basis_required",
                    "presence_re_evaluation_indeterminate",
                    "perishability_preserved",
                    "durable_presence_absent",
                    "lapse_route_absent",
                    "result_level_non_claims_canonical_false",
                    "complete_material_omission_posture",
                    "admissible_future_route",
                ):
                    self.assertIn(field, first)
                self.assertNotIn(CHECKS_KEY, first)
                self.assertNotIn("condition_evaluations", first)
                self.assertFalse(
                    resolver._contains_prohibited_complete_material(first)
                )
                self.assert_counts(result)

    def test_repeatability_and_loaded_artifact_immutability(self) -> None:
        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        artifacts_before = (
            self.boundary(),
            self.prior(),
            self.attestation(),
            self.receipt(),
        )
        first = self.invoke(request)
        second = self.invoke(copy.deepcopy(request))
        self.assertEqual(first, second)
        self.assertEqual(request, request_before)
        self.assertEqual(
            artifacts_before,
            (
                self.boundary(),
                self.prior(),
                self.attestation(),
                self.receipt(),
            ),
        )
        self.assertEqual(
            [item["name"] for item in self.checks(first)],
            [item["name"] for item in self.checks(second)],
        )
        serialized = json.dumps(first, sort_keys=True)
        for prohibited in (
            "timestamp_generated",
            "random_seed",
            "environment_value",
        ):
            self.assertNotIn(prohibited, serialized)

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

    def test_writer_valid_branches_format_suffix_and_no_overwrite(
        self,
    ) -> None:
        results = self.branches()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = [
                    resolver.write_presence_re_evaluation_operation_v0_min_result(
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
                    Path(resolver.OUTPUT_FILENAME).stem
                    + "_003"
                    + Path(resolver.OUTPUT_FILENAME).suffix,
                )
                self.assertEqual(
                    tuple(path.name for path in written), expected_names
                )
                for path, result in zip(written, results):
                    self.assert_written_json(path, result)
                first_before = written[0].read_bytes()
                fifth = (
                    resolver.write_presence_re_evaluation_operation_v0_min_result(
                        results[0]
                    )
                )
                self.assertTrue(fifth.name.endswith("_004.json"))
                self.assertEqual(written[0].read_bytes(), first_before)

                explicit = output_root / "explicit.json"
                self.write_text(explicit, "existing\n")
                explicit_before = explicit.read_bytes()
                with self.assertRaises(
                    resolver.PresenceReEvaluationOperationV0MinError
                ):
                    resolver.write_presence_re_evaluation_operation_v0_min_result(
                        results[0], explicit
                    )
                self.assertEqual(explicit.read_bytes(), explicit_before)

    def test_writer_refusal_matrix(self) -> None:
        requires_basis, supported, indeterminate, blocked = self.branches()
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
            requires_basis,
            lambda value: value["operation_posture"].__setitem__(
                "presence_re_evaluation_performed", False
            ),
        )
        changed(
            "wrong_identity",
            requires_basis,
            lambda value: value[
                "presence_re_evaluation_operation_metadata"
            ].__setitem__("operation_id", "wrong"),
        )
        changed(
            "wrong_path",
            requires_basis,
            lambda value: value[
                "presence_re_evaluation_operation_metadata"
            ].__setitem__("boundary_artifact_path", "wrong"),
        )
        changed(
            "wrong_outcome",
            requires_basis,
            lambda value: value.__setitem__(
                "outcome", resolver.OUTCOME_SUPPORTED
            ),
        )
        changed(
            "wrong_result",
            requires_basis,
            lambda value: value.__setitem__(
                "presence_re_evaluation_operation_result",
                resolver.RESULT_SUPPORTED,
            ),
        )
        changed(
            "wrong_counts",
            requires_basis,
            lambda value: value.__setitem__("passed_check_count", 0),
        )
        changed(
            "wrong_condition_matrix",
            requires_basis,
            lambda value: value["condition_evaluations"][
                "receiver_attested"
            ].__setitem__("evaluation", resolver.EVALUATION_REQUIRES_BASIS),
        )
        changed(
            "supported_non_satisfied",
            supported,
            lambda value: value["condition_evaluations"][
                "receiver_attested"
            ].__setitem__("evaluation", resolver.EVALUATION_REQUIRES_BASIS),
        )
        changed(
            "supported_nonempty_missing",
            supported,
            lambda value: value[
                "missing_or_insufficient_receiver_answerable_basis"
            ].append("receiver_attested"),
        )
        changed(
            "requires_empty_missing",
            requires_basis,
            lambda value: value.__setitem__(
                "missing_or_insufficient_receiver_answerable_basis", []
            ),
        )
        changed(
            "indeterminate_empty",
            indeterminate,
            lambda value: value.__setitem__(
                "indeterminate_receiver_answerable_basis_conditions", []
            ),
        )
        changed(
            "blocked_completed",
            blocked,
            lambda value: value["operation_posture"].__setitem__(
                "presence_re_evaluation_performed", True
            ),
        )
        changed(
            "non_claim_true",
            requires_basis,
            lambda value: value["non_claims"].__setitem__(
                resolver.REQUIRED_FALSE_NON_CLAIMS[0], True
            ),
        )
        changed(
            "omission_false",
            requires_basis,
            lambda value: value["omission_posture"].__setitem__(
                resolver.OMISSION_POSTURE_FIELDS[0], False
            ),
        )
        changed(
            "lineage_false",
            requires_basis,
            lambda value: value["lineage_preservation_posture"].__setitem__(
                "prior_presence_result_preserved", False
            ),
        )
        changed(
            "perishability_false",
            requires_basis,
            lambda value: value["perishability_posture"].__setitem__(
                "presence_if_ever_supported_remains_perishable", False
            ),
        )
        changed(
            "complete_material",
            requires_basis,
            lambda value: value.__setitem__(
                "complete_prior_presence_artifact", {"forbidden": True}
            ),
        )
        changed(
            "wrong_route",
            requires_basis,
            lambda value: value.__setitem__(
                "admissible_future_route", resolver.SUPPORTED_FUTURE_ROUTE
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            output_root = (
                Path(temporary) / resolver.CANONICAL_OUTPUT_ROOT.name
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for label, result in invalid:
                    with self.subTest(writer_refusal=label):
                        target = output_root / (label + ".json")
                        with self.assertRaises(
                            resolver.PresenceReEvaluationOperationV0MinError
                        ):
                            resolver.write_presence_re_evaluation_operation_v0_min_result(
                                result, target
                            )
                        self.assertFalse(target.exists())

    def test_writer_protected_paths(self) -> None:
        result = self.invoke()
        protected = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            Path(__file__).resolve(),
            BOUNDARY_ARTIFACT_PATH,
            PRIOR_PRESENCE_ARTIFACT_PATH,
            RECEIVER_ATTESTATION_ARTIFACT_PATH,
            RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_PATH,
            REPO_ROOT / "reference/IAMMAI/protected.json",
            REPO_ROOT
            / "artifacts/actual_receiver_attestation_capture/"
            "receiver_attestation_capture_001/protected.json",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_candidate_sufficiency_"
            "operation_v0_min/protected.json",
            REPO_ROOT / "artifacts/contaminated_lineage/protected.json",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "presence_operation_v0_min/protected.json",
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "presence_re_evaluation_boundary_v0_min/protected.json",
            REPO_ROOT / "artifacts/outside_exact_output_family/result.json",
        )
        for target in protected:
            with self.subTest(protected_path=str(target)):
                existed = target.exists()
                before = target.read_bytes() if target.is_file() else None
                with self.assertRaises(
                    resolver.PresenceReEvaluationOperationV0MinError
                ):
                    resolver.write_presence_re_evaluation_operation_v0_min_result(
                        result, target
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
