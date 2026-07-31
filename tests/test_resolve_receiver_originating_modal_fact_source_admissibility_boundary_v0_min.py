"""Tests for one receiver-originating source-admissibility boundary.

The suite keeps source existence, source admissibility, source authority, and
native standing distinct.  Canonical inputs are read in place; every corrupt
input and every writer exercise is isolated under a temporary directory.  No
live boundary artifact or downstream modal-fact evaluation is created.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from collections.abc import Callable, Mapping
from contextlib import ExitStack
from pathlib import Path
from typing import Any
from unittest.mock import patch

import resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min as resolver


REPO_ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
PRIOR_PATH = REPO_ROOT / resolver.PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
DECLARATION_PATH = REPO_ROOT / resolver.DECLARATION_SURFACE_RELATIVE_PATH
CANDIDATE_PATH = REPO_ROOT / resolver.CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
ATTESTATION_PATH = REPO_ROOT / resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
RECEIPT_PATH = REPO_ROOT / resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
ARCHIVE_PATH = REPO_ROOT / resolver.DECLARATION_ARCHIVE_RELATIVE_PATH
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

BOUNDARY_KEY = "receiver_originating_modal_fact_source_admissibility_boundary"
CHECKS_KEY = BOUNDARY_KEY + "_checks"
SUMMARY_KEY = BOUNDARY_KEY + "_summary"
NON_MEANING_KEY = BOUNDARY_KEY + "_non_meaning"
PRIOR_KEY = "presence_re_evaluation_operation"
CANDIDATE_KEY = "receiver_side_answerable_basis_candidate_sufficiency_operation"
ATTESTATION_KEY = "receiver_side_answerable_basis_receiver_attestation_operation"
RECEIPT_KEY = "receiver_side_answerable_basis_receiver_answerable_receipt_operation"

INVALID_BOOLEAN_VALUES = (0, 1, "true", "false", None, [], {}, "non-empty")
PROHIBITED_COMPLETE_KEYS = (
    "complete_prior_operation_artifact",
    "complete_candidate_sufficiency_artifact",
    "complete_candidate_sufficiency_material",
    "complete_receiver_attestation_artifact",
    "complete_receiver_answerable_receipt_artifact",
    "complete_declaration_body",
    "declaration_body",
    "declaration_content",
    "semantic_payload",
    "sufficiency_basis_records",
    "bounded_capture_signal_bodies",
    "archive_bytes",
    "alternative_declarations",
    "alternative_artifacts",
    "unrelated_receiver_side_material",
)


class ReceiverOriginatingSourceAdmissibilityBoundaryTests(unittest.TestCase):
    """Verify the exact source, matter, transition, and refusal boundary."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.terminal_summary_paths = (
            REPO_ROOT / "spec/PRESENCE_RE_EVALUATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
            REPO_ROOT / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
            REPO_ROOT / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
        )
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            DECLARATION_PATH,
            PRIOR_PATH,
            CANDIDATE_PATH,
            ATTESTATION_PATH,
            RECEIPT_PATH,
            *cls.terminal_summary_paths,
        )
        for path in cls.preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input missing: {path}")
        cls.preserved_hashes = {
            path: cls.sha256(path) for path in cls.preserved_paths
        }
        cls.specification_text = SPECIFICATION_PATH.read_text(encoding="utf-8")
        cls.declaration_bytes = DECLARATION_PATH.read_bytes()
        cls.prior_bytes = PRIOR_PATH.read_bytes()
        cls.candidate_bytes = CANDIDATE_PATH.read_bytes()
        cls.attestation_bytes = ATTESTATION_PATH.read_bytes()
        cls.receipt_bytes = RECEIPT_PATH.read_bytes()
        cls.prior_artifact = cls.strict_load_json_bytes(cls.prior_bytes)
        cls.candidate_artifact = cls.strict_load_json_bytes(cls.candidate_bytes)
        cls.attestation_artifact = cls.strict_load_json_bytes(cls.attestation_bytes)
        cls.receipt_artifact = cls.strict_load_json_bytes(cls.receipt_bytes)
        for name in (
            "prior_artifact",
            "candidate_artifact",
            "attestation_artifact",
            "receipt_artifact",
        ):
            if not isinstance(getattr(cls, name), dict):
                raise AssertionError(f"{name} is not a mapping")
        cls.output_snapshot = cls.snapshot_output_root()

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            if cls.sha256(path) != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if cls.snapshot_output_root() != cls.output_snapshot:
            raise AssertionError("canonical source-admissibility output root changed")

    @staticmethod
    def sha256(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def digest_bytes(value: bytes) -> str:
        return hashlib.sha256(value).hexdigest()

    @staticmethod
    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
        value: dict[str, object] = {}
        for key, item in pairs:
            if key in value:
                raise AssertionError(f"duplicate fixture key: {key}")
            value[key] = item
        return value

    @classmethod
    def strict_load_json_bytes(cls, value: bytes) -> object:
        return json.loads(
            value.decode("utf-8", errors="strict"),
            object_pairs_hook=cls.reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AssertionError(f"non-finite fixture value: {value}")
            ),
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

    @staticmethod
    def safe_name(value: object) -> str:
        safe = "".join(ch if ch.isalnum() else "_" for ch in str(value))
        return safe.strip("_") or "case"

    def write_bytes(self, path: Path, value: bytes) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"fixture path collision: {path}")
        path.write_bytes(value)
        return path

    def write_text(self, path: Path, value: str) -> Path:
        return self.write_bytes(path, value.encode("utf-8"))

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
    def set_path(mapping: dict[str, Any], keys: tuple[str, ...], value: object) -> None:
        selected = mapping
        for key in keys[:-1]:
            nested = selected[key]
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {keys}")
            selected = nested
        selected[keys[-1]] = copy.deepcopy(value)

    def request(self, **overrides: object) -> dict[str, Any]:
        return resolver.build_declared_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request(
            **copy.deepcopy(overrides)
        )

    def resolve(self, request: object | None = None) -> dict[str, Any]:
        supplied = self.request() if request is None else copy.deepcopy(request)
        before = copy.deepcopy(supplied)
        result = resolver.resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min(
            supplied
        )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_with_path_patch(
        self,
        *,
        path_constant: str,
        path: Path,
        raw: bytes,
        digest_constant: str | None = None,
        trust_digest: bool = False,
        declaration_identity: bool = False,
        request_overrides: Mapping[str, object] | None = None,
    ) -> dict[str, Any]:
        self.write_bytes(path, raw)
        with ExitStack() as stack:
            stack.enter_context(patch.object(resolver, path_constant, path))
            if digest_constant is not None and trust_digest:
                stack.enter_context(
                    patch.object(resolver, digest_constant, self.digest_bytes(raw))
                )
            if declaration_identity:
                stack.enter_context(patch.object(resolver, "DECLARATION_BYTE_COUNT", len(raw)))
                stack.enter_context(
                    patch.object(resolver, "DECLARATION_SHA256", self.digest_bytes(raw))
                )
            request = self.request(**dict(request_overrides or {}))
            return self.resolve(request)

    def resolve_with_json_artifact(
        self,
        *,
        path_constant: str,
        digest_constant: str,
        path: Path,
        artifact: object,
    ) -> dict[str, Any]:
        raw = (
            json.dumps(
                artifact,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
        return self.resolve_with_path_patch(
            path_constant=path_constant,
            path=path,
            raw=raw,
            digest_constant=digest_constant,
            trust_digest=True,
        )

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
        for item in checks:
            self.assertIs(type(item.get("passed")), bool)
            for field in ("block_code", "failure_code"):
                if field in item:
                    self.assertIn(item[field], resolver.BLOCK_CODES)

    def assert_non_claims_and_omission(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(type(value) is bool and value is False for value in non_claims.values()))
        self.assertIs(result.get("result_level_non_claims_canonical_false"), True)
        omission = result.get("omission_posture")
        self.assertIsInstance(omission, dict)
        self.assertEqual(set(omission), set(resolver.OMISSION_POSTURE_FIELDS))
        self.assertTrue(all(type(value) is bool and value is True for value in omission.values()))
        self.assertFalse(resolver._contains_prohibited_complete_material(result))

    def assert_blocked(self, result: Mapping[str, Any], code: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(result.get("boundary_result"), resolver.RESULT_NOT_EVALUATED)
        self.assertEqual(result.get("completed_consideration_posture_count"), 0)
        self.assertIsNone(result.get("admissible_future_route"))
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        boundary = self.boundary(result)
        for field in (
            "receiver_originating_modal_fact_source_admissibility_boundary_recorded",
            "receiver_originating_modal_fact_source_admissibility_boundary_result_recorded",
            "receiver_originating_modal_fact_evaluation_consideration_allowed",
            "receiver_originating_modal_fact_evaluation_consideration_not_allowed",
            "receiver_originating_modal_fact_source_admissibility_boundary_exhausted",
            "source_selection_recorded",
        ):
            self.assertIs(boundary.get(field), False)
        self.assertEqual(
            set(result.get("admissibility_evaluations", {}).values()),
            {resolver.ADMISSIBILITY_NOT_EVALUATED},
        )
        self.assertNotIn(
            resolver.ADMISSIBILITY_NOT_PASSED,
            result.get("admissibility_evaluations", {}).values(),
        )
        self.assert_counts(result)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        self.assert_non_claims_and_omission(result)

    def assert_completed(
        self,
        result: Mapping[str, Any],
        *,
        allowed: bool,
    ) -> None:
        expected_outcome = resolver.OUTCOME_ALLOWED if allowed else resolver.OUTCOME_NOT_ALLOWED
        expected_result = resolver.RESULT_ALLOWED if allowed else resolver.RESULT_NOT_ALLOWED
        expected_code = resolver.DECISION_CODE_ALLOWED if allowed else resolver.DECISION_CODE_NOT_ALLOWED
        expected_reason = resolver.DECISION_REASON_ALLOWED if allowed else resolver.DECISION_REASON_NOT_ALLOWED
        self.assertEqual(result.get("outcome"), expected_outcome)
        self.assertEqual(result.get("boundary_result"), expected_result)
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assertEqual(result.get("completed_consideration_posture_count"), 1)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertEqual(
            result.get("boundary_decision"),
            {
                "decision_code": expected_code,
                "decision_reason": expected_reason,
                "selection": allowed,
            },
        )
        self.assertEqual(
            set(result.get("admissibility_evaluations", {}).values()),
            {resolver.ADMISSIBILITY_PASSED},
        )
        boundary = self.boundary(result)
        self.assertIs(boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_recorded"), True)
        self.assertIs(boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_result_recorded"), True)
        self.assertIs(boundary.get("receiver_originating_modal_fact_source_admissibility_boundary_exhausted"), True)
        self.assertIs(boundary.get("source_selection_recorded"), True)
        self.assertIs(boundary.get("receiver_originating_modal_fact_evaluation_consideration_allowed"), allowed)
        self.assertIs(boundary.get("receiver_originating_modal_fact_evaluation_consideration_not_allowed"), not allowed)
        expected_route = resolver.ADMISSIBLE_FUTURE_ROUTE if allowed else None
        self.assertEqual(result.get("admissible_future_route"), expected_route)
        self.assertEqual(boundary.get("admissible_future_route"), expected_route)
        self.assert_counts(result)
        self.assert_non_claims_and_omission(result)

    def branches(self) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        return (
            self.resolve(),
            self.resolve(self.request(receiver_originating_modal_fact_evaluation_consideration_selected=False)),
            self.resolve(self.request(unexpected=True)),
        )

    def test_public_api_constants_and_exact_paths(self) -> None:
        for name in (
            "build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request",
            "build_declared_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request",
            "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min",
            "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_from_path",
            "build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary",
            "write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertTrue(issubclass(resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError, Exception))
        expected_scalars = {
            "RESOLVER_MODULE": "resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min",
            "RESULT_VERSION": "0.1.0",
            "BOUNDARY_ID": "receiver_originating_modal_fact_source_admissibility_boundary_001",
            "BOUNDARY_TYPE": "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY",
            "BOUNDARY_VERSION": "0.1.0",
            "BOUNDARY_SCOPE": "CONSIDER_ONE_EXACT_RECEIVER_ORIGINATING_DECLARATION_AS_SOURCE_FOR_TWO_RECEIVER_ALLOCATED_MODAL_FACTS_ONLY",
            "SELECTED_SOURCE_CLASS": "RECEIVER_ORIGINATING_DECLARATION_SOURCE",
            "SELECTED_RELATION_CLASS": "RECEIVER_ALLOCATED_MODAL_FACT_EVALUATION_RELATION",
            "SELECTED_MATTER_CLASS": "RECEIVER_ANSWERABLE_BASIS_REFUSABILITY_AND_WITHHOLDABILITY_ONLY",
            "SELECTED_SOURCE_ORIGIN": "RECEIVER_ORIGINATING",
            "SELECTED_SOURCE_PROVENANCE_POSTURE": "DECLARED_RECEIVER_CUSTODY_REFERENCE_ONLY",
            "SELECTED_SOURCE_ARRIVAL_POSTURE": "CARRIED_ARRIVAL",
            "DECLARATION_ARCHIVE_MEMBER": "receiver_attestation_001/freely_given_statement.txt",
            "DECLARATION_BYTE_COUNT": 207,
            "DECLARATION_SHA256": "9c1aeb888cd182fdbce789e1bb191f5778712f82483d7eca1334800dac4dd3eb",
            "DECLARATION_ARCHIVE_SHA256": "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c",
            "DECLARATION_CANDIDATE_ID": "receiver_side_answerable_basis_candidate_001",
            "DECLARATION_PROVENANCE_REFERENCE": "declared://receiver-custody/IAMMAI-RECEIVER/receiver_attestation_001",
            "DECLARATION_RECEIPT_BUNDLE": "receiver_attestation_001",
            "DECLARATION_RECEIVER_LABEL": "Mario",
            "PRIOR_OPERATION_SHA256": "fa3f05965de18382b48a37d54abeb04ed4e3d4383b8e75c11ccaa1ca07c15776",
            "CANDIDATE_SUFFICIENCY_SHA256": "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4",
            "RECEIVER_ATTESTATION_SHA256": "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9",
            "RECEIVER_ANSWERABLE_RECEIPT_SHA256": "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb",
            "OUTCOME_ALLOWED": "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED",
            "OUTCOME_NOT_ALLOWED": "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_NOT_ALLOWED",
            "OUTCOME_BLOCKED": "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_BLOCKED",
            "RESULT_ALLOWED": "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_ALLOWED",
            "RESULT_NOT_ALLOWED": "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_CONSIDERATION_NOT_ALLOWED",
            "RESULT_NOT_EVALUATED": "NOT_EVALUATED",
            "ADMISSIBILITY_PASSED": "PASSED",
            "ADMISSIBILITY_NOT_PASSED": "NOT_PASSED",
            "ADMISSIBILITY_NOT_EVALUATED": "NOT_EVALUATED",
            "ADMISSIBLE_FUTURE_ROUTE": "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_THEN_SEPARATE_RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_ONLY",
            "OUTPUT_FILENAME": "receiver_originating_modal_fact_source_admissibility_boundary_001__receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result.json",
        }
        for name, expected in expected_scalars.items():
            with self.subTest(constant=name):
                self.assertEqual(getattr(resolver, name), expected)
        self.assertEqual(
            resolver.REQUIRED_MATTER_TUPLE,
            (
                "receiver_answerable_basis_refusable",
                "receiver_answerable_basis_could_have_been_withheld",
            ),
        )
        expected_paths = {
            "GOVERNING_SPECIFICATION_RELATIVE_PATH": "spec/RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_V0_MIN_SPEC.md",
            "PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH": "artifacts/integrity_host_v0_min_coexistence_presence_re_evaluation_operation_v0_min/presence_re_evaluation_operation_001__presence_re_evaluation_operation_v0_min_result.json",
            "DECLARATION_SURFACE_RELATIVE_PATH": "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/freely_given_statement.txt",
            "DECLARATION_ARCHIVE_RELATIVE_PATH": "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/original_zip/receiver_attestation_001.zip",
            "CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH": "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/receiver_side_answerable_basis_candidate_sufficiency_operation_001__receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result_001.json",
            "RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH": "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_operation_v0_min/receiver_side_answerable_basis_receiver_attestation_operation_001__receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result_001.json",
            "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH": "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min/receiver_side_answerable_basis_receiver_answerable_receipt_operation_001__receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result.json",
        }
        for name, expected in expected_paths.items():
            with self.subTest(path_constant=name):
                self.assertEqual(str(getattr(resolver, name)), expected)
        self.assertEqual(
            resolver.CANONICAL_OUTPUT_ROOT,
            REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_fact_source_admissibility_boundary_v0_min",
        )

    def test_canonical_request_and_declared_override_contract(self) -> None:
        first = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request()
        second = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request()
        self.assertIsInstance(first, dict)
        self.assertEqual(set(first), resolver._canonical_request_keys())
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(first["declared_non_claims"], second["declared_non_claims"])
        self.assertEqual(first["selected_matter"], list(resolver.REQUIRED_MATTER_TUPLE))
        self.assertIs(first["receiver_originating_modal_fact_evaluation_consideration_selected"], True)
        self.assertEqual(set(first["declared_non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(value is False for value in first["declared_non_claims"].values()))
        serialized = json.dumps(first, sort_keys=True)
        for prohibited in (
            "declaration_body",
            "alternative_source",
            "boundary_result",
            "modal_fact_evaluation_result",
            "semantic_payload",
            "downstream_operation_result",
        ):
            self.assertNotIn(prohibited, serialized)
        first["selected_matter"].append("leak")
        first["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = True
        self.assertEqual(second, resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_request())

        nested = {"items": ["kept"]}
        declared = self.request(unknown=nested)
        self.assertEqual(declared["unknown"], nested)
        self.assertIsNot(declared["unknown"], nested)
        nested["items"].append("caller mutation")
        self.assertEqual(declared["unknown"], {"items": ["kept"]})
        self.assert_blocked(self.resolve(declared), "REQUEST_UNKNOWN_FIELD")
        self.assert_completed(
            self.resolve(self.request(receiver_originating_modal_fact_evaluation_consideration_selected=False)),
            allowed=False,
        )
        malformed = self.request(selected_matter="not-a-list")
        self.assertEqual(malformed["selected_matter"], "not-a-list")
        self.assert_blocked(self.resolve(malformed), "REQUEST_MATTER_MISMATCH")

    def test_exact_boolean_request_matrix(self) -> None:
        boolean_fields = (
            "receiver_originating_modal_fact_evaluation_consideration_selected",
            "selected_source_native_standing",
            "jurisdiction_distinction_preserved",
        )
        for field in boolean_fields:
            for value in INVALID_BOOLEAN_VALUES:
                with self.subTest(field=field, value=repr(value)):
                    result = self.resolve(
                        self.request(**{field: copy.deepcopy(value)})
                    )
                    self.assert_blocked(result)
                    expected_codes = (
                        {"REQUEST_BOOLEAN_REQUIRED"}
                        if field
                        == "receiver_originating_modal_fact_evaluation_consideration_selected"
                        else {"REQUEST_VALUE_MISMATCH"}
                    )
                    self.assertIn(result["block"]["code"], expected_codes)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            for value in INVALID_BOOLEAN_VALUES:
                request = self.request()
                request["declared_non_claims"][field] = copy.deepcopy(value)
                with self.subTest(non_claim=field, value=repr(value)):
                    self.assert_blocked(
                        self.resolve(request),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_allowed_not_allowed_blocked_branches_and_cardinality(self) -> None:
        allowed, not_allowed, blocked = self.branches()
        self.assert_completed(allowed, allowed=True)
        self.assert_completed(not_allowed, allowed=False)
        self.assert_blocked(blocked, "REQUEST_UNKNOWN_FIELD")
        validation_keys = (
            "specification_validation",
            "prior_operation_artifact_validation",
            "receiver_originating_declaration_validation",
            "candidate_sufficiency_artifact_validation",
            "receiver_attestation_artifact_validation",
            "receiver_answerable_receipt_artifact_validation",
        )
        for result in (allowed, not_allowed):
            for key in validation_keys:
                self.assertIsInstance(result[key], dict)
            self.assertIs(result["specification_validation"]["specification_validated"], True)
            self.assertIs(result["receiver_originating_declaration_validation"]["declaration_validated"], True)
            for key in validation_keys[1:2] + validation_keys[3:]:
                self.assertIs(result[key]["artifact_validated"], True)
            self.assertTrue(all(result["source_selection_and_carriage_lineage"].values()))

    def test_specification_marker_validation_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (name, marker) in enumerate(resolver.SPEC_REQUIRED_MARKERS):
                self.assertIn(marker, self.specification_text)
                path = base / f"{index:03d}_{self.safe_name(name)}.md"
                mutated = self.specification_text.replace(
                    marker, f"MISSING_{name}"
                )
                self.write_text(path, mutated)
                with self.subTest(marker=name):
                    with patch.object(resolver, "GOVERNING_SPECIFICATION_RELATIVE_PATH", path):
                        result = self.resolve(self.request())
                    self.assert_blocked(result, "SPECIFICATION_MARKER_MISSING")
                    self.assertIs(result["specification_validation"]["marker_validation"][name], False)

    def test_declaration_surface_validation_matrix(self) -> None:
        self.assert_completed(self.resolve(), allowed=True)
        canonical_lines = self.declaration_bytes.decode("utf-8").splitlines()
        cases: list[tuple[str, bytes, bool, str]] = []
        cases.append(("malformed_utf8", b"\xff\xfe", True, "DECLARATION_UTF8_INVALID"))
        cases.append(("wrong_byte_count", self.declaration_bytes + b"x", False, "DECLARATION_BYTE_COUNT_MISMATCH"))
        changed_same_length = self.declaration_bytes.replace(b"freely_given=true", b"freely_given=truf")
        cases.append(("wrong_digest", changed_same_length, False, "DECLARATION_DIGEST_MISMATCH"))
        duplicate = list(canonical_lines)
        duplicate[1] = duplicate[0]
        cases.append(("duplicate_key", ("\n".join(duplicate) + "\n").encode(), True, "DECLARATION_RECORD_DUPLICATE"))
        cases.append(("missing_key", ("\n".join(canonical_lines[:-1]) + "\n").encode(), True, "DECLARATION_RECORD_SET_MISMATCH"))
        cases.append(("additional_key", ("\n".join(canonical_lines + ["additional=false"]) + "\n").encode(), True, "DECLARATION_RECORD_SET_MISMATCH"))
        malformed = list(canonical_lines)
        malformed[0] = "malformed-line"
        cases.append(("malformed_line", ("\n".join(malformed) + "\n").encode(), True, "DECLARATION_RECORD_MALFORMED"))
        for index, line in enumerate(canonical_lines):
            key, value = line.split("=", 1)
            wrong = list(canonical_lines)
            wrong[index] = key + "=" + ("wrong" if key != "confirmed_by_receiver_at" else "2026-07-28T06:37:57Z")
            cases.append(("wrong_value_" + key, ("\n".join(wrong) + "\n").encode(), True, "DECLARATION_RECORD_SET_MISMATCH"))
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, raw, trust, expected_code) in enumerate(cases):
                with self.subTest(declaration_case=label):
                    result = self.resolve_with_path_patch(
                        path_constant="DECLARATION_SURFACE_RELATIVE_PATH",
                        path=base / f"{index:03d}_{self.safe_name(label)}.txt",
                        raw=raw,
                        digest_constant="DECLARATION_SHA256",
                        trust_digest=trust,
                        declaration_identity=trust,
                    )
                    self.assert_blocked(result, expected_code)

    def test_declaration_identity_request_refusals_and_compact_output(self) -> None:
        cases = {
            "selected_receiver_originating_declaration_surface_path": "alternative/source.txt",
            "selected_receiver_originating_declaration_archive_path": "alternative/archive.zip",
            "selected_receiver_originating_declaration_archive_member": "alternative/member.txt",
            "selected_receiver_originating_declaration_byte_count": 208,
            "selected_receiver_originating_declaration_sha256": "0" * 64,
            "selected_receiver_originating_declaration_archive_sha256": "1" * 64,
            "selected_receiver_originating_declaration_candidate_id": "alternative_candidate",
            "selected_receiver_originating_declaration_source_provenance_reference": "declared://alternative",
            "selected_receiver_originating_declaration_receipt_bundle": "alternative_bundle",
            "selected_receiver_originating_declaration_receiver_label": "Alternative",
        }
        for field, value in cases.items():
            with self.subTest(identity_field=field):
                self.assert_blocked(
                    self.resolve(self.request(**{field: value})),
                    "REQUEST_VALUE_MISMATCH",
                )
        result = self.resolve()
        declaration = result["receiver_originating_declaration_validation"]
        self.assertEqual(
            declaration["matter_relevant_records"],
            {"could_have_been_refused": True, "could_have_been_withheld": True},
        )
        serialized = json.dumps(result, sort_keys=True)
        body = self.declaration_bytes.decode("utf-8")
        self.assertNotIn(body, serialized)
        summary = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(result)
        self.assertNotIn(body, json.dumps(summary, sort_keys=True))

    def test_prior_operation_artifact_validation_matrix(self) -> None:
        cases: list[tuple[str, tuple[str, ...], object]] = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            (
                "operation_result",
                ("presence_re_evaluation_operation_result",),
                "wrong",
            ),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 408),
            ("blocked", ("block", "blocked"), True),
            ("basis_not_admitted", (PRIOR_KEY, "operation_basis_admitted"), False),
            (
                "re_evaluation_not_performed",
                (PRIOR_KEY, "presence_re_evaluation_performed"),
                False,
            ),
            (
                "operation_not_exhausted",
                (PRIOR_KEY, "presence_re_evaluation_operation_exhausted"),
                False,
            ),
            (
                "wrong_completed_count",
                (PRIOR_KEY, "completed_successor_result_posture_count"),
                2,
            ),
            ("future_route", ("admissible_future_route",), "not-null"),
            (
                "receiver_attested_wrong",
                ("condition_evaluations", "receiver_attested", "evaluation"),
                "REQUIRES_BASIS",
            ),
            (
                "receipt_wrong",
                (
                    "condition_evaluations",
                    "receiver_answerable_receipt_present",
                    "evaluation",
                ),
                "REQUIRES_BASIS",
            ),
            (
                "refusable_not_requires_basis",
                (
                    "condition_evaluations",
                    "receiver_answerable_basis_refusable",
                    "evaluation",
                ),
                "SATISFIED",
            ),
            (
                "withholdable_not_requires_basis",
                (
                    "condition_evaluations",
                    "receiver_answerable_basis_could_have_been_withheld",
                    "evaluation",
                ),
                "SATISFIED",
            ),
            (
                "required_boolean_wrong_type",
                (PRIOR_KEY, "operation_basis_admitted"),
                1,
            ),
        ]
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            cases.append((field, (PRIOR_KEY, field), True))
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, keys, value) in enumerate(cases):
                artifact = copy.deepcopy(self.prior_artifact)
                self.set_path(artifact, keys, value)
                with self.subTest(prior_case=label):
                    self.assert_blocked(
                        self.resolve_with_json_artifact(
                            path_constant="PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH",
                            digest_constant="PRIOR_OPERATION_SHA256",
                            path=base / f"{index:03d}_{self.safe_name(label)}.json",
                            artifact=artifact,
                        )
                    )
            raw_cases = (
                ("malformed", b"{", "PRIOR_OPERATION_ARTIFACT_NOT_PARSEABLE"),
                (
                    "duplicate",
                    b'{"duplicate":1,"duplicate":2}',
                    "PRIOR_OPERATION_ARTIFACT_DUPLICATE_KEYED",
                ),
            )
            for offset, (label, raw, code) in enumerate(raw_cases, len(cases)):
                with self.subTest(prior_json=label):
                    result = self.resolve_with_path_patch(
                        path_constant="PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH",
                        path=base / f"{offset:03d}_{label}.json",
                        raw=raw,
                        digest_constant="PRIOR_OPERATION_SHA256",
                        trust_digest=True,
                    )
                    self.assert_blocked(result, code)
            with self.subTest(prior_case="wrong_digest"):
                result = self.resolve_with_path_patch(
                    path_constant="PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH",
                    path=base / "wrong_digest.json",
                    raw=self.prior_bytes + b"\n",
                    digest_constant="PRIOR_OPERATION_SHA256",
                    trust_digest=False,
                )
                self.assert_blocked(result, "PRIOR_OPERATION_ARTIFACT_DIGEST_MISMATCH")

    def test_candidate_sufficiency_artifact_validation_matrix(self) -> None:
        dimensions_key = (
            "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
        )
        cases = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 139),
            ("blocked", ("block", "blocked"), True),
            (
                "candidate_identity",
                (CANDIDATE_KEY, "receiver_side_answerable_basis_candidate_id"),
                "wrong",
            ),
            ("operation_result", (CANDIDATE_KEY, "operation_result"), "wrong"),
            (
                "compatibility",
                (
                    dimensions_key,
                    "refusal_withholding_compatibility",
                    "dimension_result",
                ),
                "NOT_SATISFIED",
            ),
            (
                "completion",
                ("operation_result_detail", "candidate_result_posture_count"),
                2,
            ),
            (
                "dimension_count",
                ("operation_result_detail", "evaluated_dimension_count"),
                7,
            ),
            (
                "required_boolean_wrong_type",
                (CANDIDATE_KEY, "candidate_sufficiency_operation_exhausted"),
                1,
            ),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, keys, value) in enumerate(cases):
                artifact = copy.deepcopy(self.candidate_artifact)
                self.set_path(artifact, keys, value)
                with self.subTest(candidate_case=label):
                    self.assert_blocked(
                        self.resolve_with_json_artifact(
                            path_constant="CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH",
                            digest_constant="CANDIDATE_SUFFICIENCY_SHA256",
                            path=base / f"{index:03d}_{self.safe_name(label)}.json",
                            artifact=artifact,
                        )
                    )
            for offset, (label, raw, code) in enumerate(
                (
                    ("malformed", b"{", "CANDIDATE_SUFFICIENCY_ARTIFACT_NOT_PARSEABLE"),
                    (
                        "duplicate",
                        b'{"duplicate":1,"duplicate":2}',
                        "CANDIDATE_SUFFICIENCY_ARTIFACT_DUPLICATE_KEYED",
                    ),
                ),
                len(cases),
            ):
                with self.subTest(candidate_json=label):
                    result = self.resolve_with_path_patch(
                        path_constant="CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH",
                        path=base / f"{offset:03d}_{label}.json",
                        raw=raw,
                        digest_constant="CANDIDATE_SUFFICIENCY_SHA256",
                        trust_digest=True,
                    )
                    self.assert_blocked(result, code)
            result = self.resolve_with_path_patch(
                path_constant="CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH",
                path=base / "wrong_digest.json",
                raw=self.candidate_bytes + b"\n",
                digest_constant="CANDIDATE_SUFFICIENCY_SHA256",
            )
            self.assert_blocked(result, "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH")

    def test_receiver_attestation_artifact_validation_matrix(self) -> None:
        cases = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 159),
            ("blocked", ("block", "blocked"), True),
            (
                "operation_result",
                (ATTESTATION_KEY, "receiver_attestation_operation_result"),
                "wrong",
            ),
            ("basis_admitted", (ATTESTATION_KEY, "operation_basis_admitted"), False),
            ("attestation_recorded", (ATTESTATION_KEY, "receiver_attestation_recorded"), False),
            (
                "candidate_correspondence",
                ("selected_operation_and_candidate_identity", "selected_candidate_id"),
                "wrong",
            ),
            (
                "completion",
                ("operation_result_detail", "completed_result_posture_count"),
                2,
            ),
            (
                "required_boolean_wrong_type",
                (ATTESTATION_KEY, "receiver_attestation_recorded"),
                1,
            ),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, keys, value) in enumerate(cases):
                artifact = copy.deepcopy(self.attestation_artifact)
                self.set_path(artifact, keys, value)
                with self.subTest(attestation_case=label):
                    self.assert_blocked(
                        self.resolve_with_json_artifact(
                            path_constant="RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH",
                            digest_constant="RECEIVER_ATTESTATION_SHA256",
                            path=base / f"{index:03d}_{self.safe_name(label)}.json",
                            artifact=artifact,
                        )
                    )
            for offset, (label, raw, code) in enumerate(
                (
                    ("malformed", b"{", "RECEIVER_ATTESTATION_ARTIFACT_NOT_PARSEABLE"),
                    (
                        "duplicate",
                        b'{"duplicate":1,"duplicate":2}',
                        "RECEIVER_ATTESTATION_ARTIFACT_DUPLICATE_KEYED",
                    ),
                ),
                len(cases),
            ):
                with self.subTest(attestation_json=label):
                    result = self.resolve_with_path_patch(
                        path_constant="RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH",
                        path=base / f"{offset:03d}_{label}.json",
                        raw=raw,
                        digest_constant="RECEIVER_ATTESTATION_SHA256",
                        trust_digest=True,
                    )
                    self.assert_blocked(result, code)
            result = self.resolve_with_path_patch(
                path_constant="RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH",
                path=base / "wrong_digest.json",
                raw=self.attestation_bytes + b"\n",
                digest_constant="RECEIVER_ATTESTATION_SHA256",
            )
            self.assert_blocked(result, "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH")

    def test_receiver_answerable_receipt_artifact_validation_matrix(self) -> None:
        cases = [
            ("resolver_module", ("resolver_module",), "wrong"),
            ("result_version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "wrong"),
            ("failed_count", ("failed_check_count",), 1),
            ("passed_count", ("passed_check_count",), 356),
            ("blocked", ("block", "blocked"), True),
            ("operation_result", ("operation_result",), "wrong"),
            ("receipt_present", (RECEIPT_KEY, "receiver_answerable_receipt_present"), False),
            (
                "attestation_correspondence",
                (
                    "selected_operation_and_candidate_identity",
                    "selected_attestation_operation_id",
                ),
                "wrong",
            ),
            (
                "completion",
                ("operation_result_detail", "completed_result_posture_count"),
                2,
            ),
            (
                "required_boolean_wrong_type",
                (RECEIPT_KEY, "receiver_answerable_receipt_recorded"),
                1,
            ),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (label, keys, value) in enumerate(cases):
                artifact = copy.deepcopy(self.receipt_artifact)
                self.set_path(artifact, keys, value)
                with self.subTest(receipt_case=label):
                    self.assert_blocked(
                        self.resolve_with_json_artifact(
                            path_constant="RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH",
                            digest_constant="RECEIVER_ANSWERABLE_RECEIPT_SHA256",
                            path=base / f"{index:03d}_{self.safe_name(label)}.json",
                            artifact=artifact,
                        )
                    )
            for offset, (label, raw, code) in enumerate(
                (
                    ("malformed", b"{", "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_NOT_PARSEABLE"),
                    (
                        "duplicate",
                        b'{"duplicate":1,"duplicate":2}',
                        "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DUPLICATE_KEYED",
                    ),
                ),
                len(cases),
            ):
                with self.subTest(receipt_json=label):
                    result = self.resolve_with_path_patch(
                        path_constant="RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH",
                        path=base / f"{offset:03d}_{label}.json",
                        raw=raw,
                        digest_constant="RECEIVER_ANSWERABLE_RECEIPT_SHA256",
                        trust_digest=True,
                    )
                    self.assert_blocked(result, code)
            result = self.resolve_with_path_patch(
                path_constant="RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH",
                path=base / "wrong_digest.json",
                raw=self.receipt_bytes + b"\n",
                digest_constant="RECEIVER_ANSWERABLE_RECEIPT_SHA256",
            )
            self.assert_blocked(result, "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH")

    def test_three_part_admissibility_and_non_collapse(self) -> None:
        result = self.resolve()
        self.assert_completed(result, allowed=True)
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["matter_relevant_declaration_records"],
            {"could_have_been_refused": True, "could_have_been_withheld": True},
        )
        for adjacent in (
            "freely_given",
            "prescribed_by_declaring_side",
            "attestation_words_authored_by_receiver_only",
            "confirmed_by_receiver_at",
        ):
            self.assertNotIn(adjacent, boundary["matter_relevant_declaration_records"])
        request_cases = {
            "source_class": {"selected_source_class": "wrong"},
            "relation_class": {"selected_relation_class": "wrong"},
            "matter_class": {"selected_matter_class": "wrong"},
            "matter_tuple_short": {"selected_matter": [resolver.REQUIRED_MATTER_TUPLE[0]]},
            "matter_tuple_reordered": {"selected_matter": list(reversed(resolver.REQUIRED_MATTER_TUPLE))},
            "origin_erasure": {"selected_source_origin": "NATIVE"},
            "provenance_erasure": {"selected_source_provenance_posture": "UNKNOWN"},
            "arrival_naturalized": {"selected_source_arrival_posture": "NATIVE"},
            "native_standing": {"selected_source_native_standing": True},
            "jurisdiction_collapse": {"jurisdiction_distinction_preserved": False},
        }
        for label, overrides in request_cases.items():
            with self.subTest(admissibility_case=label):
                blocked = self.resolve(self.request(**overrides))
                self.assert_blocked(blocked)
        for field in (
            "receiver_originating_declaration_authority_created",
            "receiver_originating_declaration_native_standing_created",
            "source_authority_created",
            "canon_admission_created",
            "governance_force_created",
            "truth_created",
            "standing_created",
            "receiver_answerable_basis_refusable_established",
            "receiver_answerable_basis_could_have_been_withheld_established",
            "receiver_actual_refusal_established",
            "receiver_actual_withholding_established",
            "receiver_freedom_established",
        ):
            request = self.request()
            request["declared_non_claims"][field] = True
            with self.subTest(conversion=field):
                self.assert_blocked(
                    self.resolve(request),
                    "NON_CLAIM_MISSING_OR_FLIPPED",
                )
        for weak_basis in (
            "source_exists",
            "source_readable",
            "receipt_exists",
            "source_preserved",
            "source_repeated",
            "source_convenient",
            "source_repo_local",
        ):
            with self.subTest(insufficient_alone=weak_basis):
                self.assert_blocked(
                    self.resolve(self.request(**{weak_basis: True})),
                    "REQUEST_UNKNOWN_FIELD",
                )

    def test_source_selection_lineage_nonclaims_excluded_and_non_meaning(self) -> None:
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                lineage = result["lineage_preservation_posture"]
                self.assertEqual(set(lineage), set(resolver.LINEAGE_PRESERVATION_FIELDS))
                self.assertTrue(all(type(value) is bool and value is True for value in lineage.values()))
                non_meaning = result[NON_MEANING_KEY]
                self.assertEqual(set(non_meaning), set(resolver.NON_MEANING_FIELDS))
                self.assertTrue(all(type(value) is bool and value is True for value in non_meaning.values()))
                excluded = result["excluded_condition_posture"]
                self.assertIs(excluded["excluded_condition_evaluation_performed"], False)
                self.assertIs(excluded["excluded_conditions_not_evaluated"], True)
                self.assertEqual(set(excluded["condition_evaluations"]), set(resolver.EXCLUDED_CONDITIONS))
                self.assertEqual(set(excluded["condition_evaluations"].values()), {"NOT_EVALUATED"})
                self.assertEqual(result["blocked_conversions"], list(resolver.BLOCKED_CONVERSIONS))
                self.assertEqual(result["what_remains_open"], list(resolver.WHAT_REMAINS_OPEN))
                self.assert_non_claims_and_omission(result)
                boundary = self.boundary(result)
                for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
                    self.assertIs(boundary[field], False)
                self.assertIs(boundary["selected_source_native_standing"], False)
                self.assertIs(boundary["jurisdiction_distinction_preserved"], True)

    def test_read_limits_and_no_discovery(self) -> None:
        allowed = {
            SPECIFICATION_PATH.resolve(),
            PRIOR_PATH.resolve(),
            DECLARATION_PATH.resolve(),
            CANDIDATE_PATH.resolve(),
            ATTESTATION_PATH.resolve(),
            RECEIPT_PATH.resolve(),
        }
        accessed: list[Path] = []
        original_open = Path.open

        def guarded_open(
            path: Path,
            *args: object,
            **kwargs: object,
        ) -> Any:
            resolved = path.resolve()
            accessed.append(resolved)
            if resolved not in allowed:
                raise AssertionError(f"prohibited read: {resolved}")
            return original_open(path, *args, **kwargs)

        with (
            patch.object(Path, "open", guarded_open),
            patch.object(Path, "glob", side_effect=AssertionError("glob prohibited")),
            patch.object(Path, "rglob", side_effect=AssertionError("rglob prohibited")),
            patch.object(Path, "iterdir", side_effect=AssertionError("iterdir prohibited")),
            patch.object(os, "listdir", side_effect=AssertionError("listdir prohibited")),
        ):
            result = self.resolve()
        self.assert_completed(result, allowed=True)
        self.assertEqual(accessed, [
            SPECIFICATION_PATH.resolve(),
            PRIOR_PATH.resolve(),
            DECLARATION_PATH.resolve(),
            CANDIDATE_PATH.resolve(),
            ATTESTATION_PATH.resolve(),
            RECEIPT_PATH.resolve(),
        ])
        self.assertNotIn(ARCHIVE_PATH.resolve(), accessed)
        source = RESOLVER_PATH.read_text(encoding="utf-8")
        for prohibited in (
            ".glob(",
            ".rglob(",
            ".iterdir(",
            "os.listdir(",
            "scandir(",
            "walk(",
        ):
            self.assertNotIn(prohibited, source)

    def test_strict_request_path_contract(self) -> None:
        request = self.request()
        direct = self.resolve(request)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            valid = self.write_json(root / "valid.json", request)
            valid_before = valid.read_bytes()
            from_path = resolver.resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_from_path(valid)
            self.assertEqual(from_path, direct)
            self.assertEqual(valid.read_bytes(), valid_before)
            paths = (
                self.write_text(root / "duplicate.json", '{"x":1,"x":2}'),
                self.write_text(root / "malformed.json", "{"),
                self.write_text(root / "array.json", "[]"),
                self.write_bytes(root / "malformed_utf8.json", b"\xff\xfe"),
                root / "missing.json",
            )
            for path in paths:
                with self.subTest(request_path=path.name):
                    with self.assertRaises(
                        resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError
                    ):
                        resolver.resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_from_path(path)
        self.assert_blocked(
            resolver.resolve_receiver_originating_modal_fact_source_admissibility_boundary_v0_min([]),
            "REQUEST_NOT_MAPPING",
        )

    def test_complete_material_containment_and_omission(self) -> None:
        declaration_body = self.declaration_bytes.decode("utf-8")
        artifact_sentinels = (
            json.dumps(self.prior_artifact, sort_keys=True),
            json.dumps(self.candidate_artifact, sort_keys=True),
            json.dumps(self.attestation_artifact, sort_keys=True),
            json.dumps(self.receipt_artifact, sort_keys=True),
        )
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                serialized = json.dumps(result, sort_keys=True)
                self.assertNotIn(declaration_body, serialized)
                for complete in artifact_sentinels:
                    self.assertNotIn(complete, serialized)
                for key in PROHIBITED_COMPLETE_KEYS:
                    self.assertNotIn(key, result)
                summary = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(result)
                summary_text = json.dumps(summary, sort_keys=True)
                self.assertNotIn(declaration_body, summary_text)
                self.assertNotIn(CHECKS_KEY, summary)
                for key in PROHIBITED_COMPLETE_KEYS:
                    self.assertNotIn(key, summary)

    def test_summary_contract_for_every_branch(self) -> None:
        for result in self.branches():
            with self.subTest(branch=result["outcome"]):
                summary = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(result)
                self.assertEqual(summary, result[SUMMARY_KEY])
                self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
                self.assertEqual(summary["result_version"], resolver.RESULT_VERSION)
                self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
                self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
                self.assertEqual(summary["boundary_version"], resolver.BOUNDARY_VERSION)
                self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
                self.assertEqual(summary["selected_source_class"], resolver.SELECTED_SOURCE_CLASS)
                self.assertEqual(summary["selected_relation_class"], resolver.SELECTED_RELATION_CLASS)
                self.assertEqual(summary["selected_matter_class"], resolver.SELECTED_MATTER_CLASS)
                self.assertEqual(summary["selected_matter"], list(resolver.REQUIRED_MATTER_TUPLE))
                self.assertEqual(summary["selected_source_origin"], resolver.SELECTED_SOURCE_ORIGIN)
                self.assertEqual(summary["selected_source_arrival_posture"], resolver.SELECTED_SOURCE_ARRIVAL_POSTURE)
                self.assertIs(summary["selected_source_native_standing"], False)
                self.assertEqual(summary["declaration_sha256"], resolver.DECLARATION_SHA256)
                self.assertEqual(summary["outcome"], result["outcome"])
                self.assertEqual(summary["boundary_result"], result["boundary_result"])
                self.assertEqual(summary["failed_check_count"], result["failed_check_count"])
                self.assertEqual(summary["passed_check_count"], result["passed_check_count"])
                self.assertEqual(summary["decision_code"], result["boundary_decision"]["decision_code"])
                self.assertEqual(summary["decision_reason"], result["boundary_decision"]["decision_reason"])
                self.assertEqual(summary["source_admissibility_evaluation"], result["admissibility_evaluations"]["source_admissibility_evaluation"])
                self.assertEqual(summary["scope_and_matter_admissibility_evaluation"], result["admissibility_evaluations"]["scope_and_matter_admissibility_evaluation"])
                self.assertEqual(summary["transition_admissibility_evaluation"], result["admissibility_evaluations"]["transition_admissibility_evaluation"])
                self.assertIs(summary["receiver_origin_preserved"], True)
                self.assertIs(summary["jurisdiction_preserved"], True)
                self.assertIs(summary["source_not_naturalized"], True)
                self.assertIs(summary["modal_fact_truth_authority_standing_presence_absent"], True)
                self.assertIs(summary["result_level_non_claims_canonical_false"], True)
                self.assertIs(summary["complete_material_omission_posture"], True)
                self.assertNotIn(CHECKS_KEY, summary)
                self.assertNotIn("non_claims", summary)
        with self.assertRaises(
            resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError
        ):
            resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary({})

    def test_determinism_immutability_and_check_accounting(self) -> None:
        request = self.request()
        before = copy.deepcopy(request)
        artifacts_before = (
            copy.deepcopy(self.prior_artifact),
            copy.deepcopy(self.candidate_artifact),
            copy.deepcopy(self.attestation_artifact),
            copy.deepcopy(self.receipt_artifact),
        )
        first = self.resolve(request)
        second = self.resolve(copy.deepcopy(request))
        self.assertEqual(first, second)
        self.assertEqual(request, before)
        self.assertEqual(
            artifacts_before,
            (
                self.prior_artifact,
                self.candidate_artifact,
                self.attestation_artifact,
                self.receipt_artifact,
            ),
        )
        first_summary = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(first)
        second_summary = resolver.build_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_summary(second)
        self.assertEqual(first_summary, second_summary)
        self.assertEqual(
            [item["name"] for item in self.checks(first)],
            [item["name"] for item in self.checks(second)],
        )
        self.assert_counts(first)
        serialized = json.dumps(first, sort_keys=True)
        for prohibited in (
            "generated_at",
            "timestamp_generated",
            "random_seed",
            "environment_value",
            "execution_order",
        ):
            self.assertNotIn(prohibited, serialized)

    def assert_written_json(self, path: Path, result: Mapping[str, Any]) -> None:
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

    def test_writer_valid_branches_format_suffix_and_no_overwrite(self) -> None:
        results = self.branches()
        with tempfile.TemporaryDirectory() as temporary:
            output_root = Path(temporary) / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = [
                    resolver.write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(result)
                    for result in results
                ]
                expected_names = (
                    resolver.OUTPUT_FILENAME,
                    Path(resolver.OUTPUT_FILENAME).stem + "_001.json",
                    Path(resolver.OUTPUT_FILENAME).stem + "_002.json",
                )
                self.assertEqual(tuple(path.name for path in written), expected_names)
                for path, result in zip(written, results):
                    self.assert_written_json(path, result)
                first_before = written[0].read_bytes()
                fourth = resolver.write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(results[0])
                self.assertEqual(fourth.name, Path(resolver.OUTPUT_FILENAME).stem + "_003.json")
                self.assertEqual(written[0].read_bytes(), first_before)

                explicit = output_root / "explicit.json"
                self.write_text(explicit, "existing\n")
                explicit_before = explicit.read_bytes()
                with self.assertRaises(
                    resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError
                ):
                    resolver.write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(
                        results[0], explicit
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

        changed("wrong_identity", allowed, lambda value: value["receiver_originating_modal_fact_source_admissibility_boundary_metadata"].__setitem__("boundary_id", "wrong"))
        changed("wrong_path", allowed, lambda value: value["receiver_originating_modal_fact_source_admissibility_boundary_metadata"].__setitem__("declaration_surface_path", "wrong"))
        changed("wrong_digest", allowed, lambda value: value["receiver_originating_declaration_validation"].__setitem__("observed_sha256", "0" * 64))
        changed("wrong_class", allowed, lambda value: value[BOUNDARY_KEY].__setitem__("selected_source_class", "wrong"))
        changed("wrong_matter", allowed, lambda value: value[BOUNDARY_KEY].__setitem__("selected_matter", []))
        changed("wrong_count", allowed, lambda value: value.__setitem__("passed_check_count", 0))
        changed("wrong_outcome", allowed, lambda value: value.__setitem__("outcome", resolver.OUTCOME_NOT_ALLOWED))
        changed("wrong_result", allowed, lambda value: value.__setitem__("boundary_result", resolver.RESULT_NOT_ALLOWED))
        changed("allowed_without_route", allowed, lambda value: value.__setitem__("admissible_future_route", None))
        changed("not_allowed_with_route", not_allowed, lambda value: value.__setitem__("admissible_future_route", resolver.ADMISSIBLE_FUTURE_ROUTE))
        changed("blocked_completed", blocked, lambda value: value["boundary_posture"].__setitem__("receiver_originating_modal_fact_source_admissibility_boundary_recorded", True))
        changed("completed_not_passed", allowed, lambda value: value["admissibility_evaluations"].__setitem__("source_admissibility_evaluation", resolver.ADMISSIBILITY_NOT_PASSED))
        changed("non_claim_true", allowed, lambda value: value["non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], True))
        changed("omission_false", allowed, lambda value: value["omission_posture"].__setitem__(resolver.OMISSION_POSTURE_FIELDS[0], False))
        changed("lineage_false", allowed, lambda value: value["lineage_preservation_posture"].__setitem__(resolver.LINEAGE_PRESERVATION_FIELDS[0], False))
        changed("naturalized", allowed, lambda value: value[BOUNDARY_KEY].__setitem__("selected_source_native_standing", True))
        changed("jurisdiction_collapsed", allowed, lambda value: value[BOUNDARY_KEY].__setitem__("jurisdiction_distinction_preserved", False))
        changed("complete_declaration", allowed, lambda value: value.__setitem__("complete_declaration_body", self.declaration_bytes.decode("utf-8")))
        changed("complete_upstream", allowed, lambda value: value.__setitem__("complete_prior_operation_artifact", self.prior_artifact))
        with tempfile.TemporaryDirectory() as temporary:
            output_root = Path(temporary) / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for label, result in invalid:
                    with self.subTest(writer_refusal=label):
                        target = output_root / (self.safe_name(label) + ".json")
                        with self.assertRaises(
                            resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError
                        ):
                            resolver.write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(
                                result, target
                            )
                        self.assertFalse(target.exists())

    def test_writer_protected_paths_and_exact_output_family(self) -> None:
        result = self.resolve()
        protected = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            Path(__file__).resolve(),
            DECLARATION_PATH,
            ARCHIVE_PATH,
            PRIOR_PATH,
            CANDIDATE_PATH,
            ATTESTATION_PATH,
            RECEIPT_PATH,
            REPO_ROOT / "reference/IAMMAI/protected.json",
            REPO_ROOT / "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/protected.json",
            REPO_ROOT / "artifacts/contaminated_lineage/protected.json",
            REPO_ROOT / "artifacts/bounded_capture_signal_body/protected.json",
            REPO_ROOT / "artifacts/outside_exact_boundary_family/result.json",
        )
        for target in protected:
            with self.subTest(protected_path=str(target)):
                existed = target.exists()
                before = target.read_bytes() if target.is_file() else None
                with self.assertRaises(
                    resolver.ReceiverOriginatingModalFactSourceAdmissibilityBoundaryV0MinError
                ):
                    resolver.write_receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result(
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
