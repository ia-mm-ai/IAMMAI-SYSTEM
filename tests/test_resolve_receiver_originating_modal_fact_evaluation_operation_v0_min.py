"""Bounded tests for one receiver-originating modal-fact evaluation.

The suite admits only the exact standing source and carriage lineage. Mutated
fixtures remain temporary, branch-only postures use deterministic internal
helpers, and writer tests never touch the canonical repository output root.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_originating_modal_fact_evaluation_operation_v0_min as resolver


SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
BOUNDARY_PATH = REPO_ROOT / resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH
DECLARATION_PATH = REPO_ROOT / resolver.DECLARATION_SURFACE_RELATIVE_PATH
CANDIDATE_PATH = REPO_ROOT / resolver.CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
ATTESTATION_PATH = REPO_ROOT / resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
RECEIPT_PATH = REPO_ROOT / resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

OPERATION_KEY = "receiver_originating_modal_fact_evaluation_operation"
CHECKS_KEY = OPERATION_KEY + "_checks"
SUMMARY_KEY = OPERATION_KEY + "_summary"
NON_MEANING_KEY = OPERATION_KEY + "_non_meaning"
BOUNDARY_KEY = "receiver_originating_modal_fact_source_admissibility_boundary"
CANDIDATE_KEY = "receiver_side_answerable_basis_candidate_sufficiency_operation"
ATTESTATION_KEY = "receiver_side_answerable_basis_receiver_attestation_operation"
RECEIPT_KEY = (
    "receiver_side_answerable_basis_receiver_answerable_receipt_operation"
)

EXPECTED_TARGETS = (
    "receiver_answerable_basis_refusable",
    "receiver_answerable_basis_could_have_been_withheld",
)
EXPECTED_EXCLUDED = (
    "receiver_answerable_basis_custody_distinct",
    "receiver_answerable_basis_controlled_by_declaring_side",
    "repo_local_execution_only",
    "operator_only_attestation",
    "derivative_rendering_attestation",
    "same_custody_countersignature",
    "automatic_acknowledgement",
    "generated_affirmation",
    "forged_receiver_attestation",
    "inadmissible_receiver_basis",
)
EXPECTED_DECLARATION_RECORDS = (
    "freely_given=true",
    "could_have_been_refused=true",
    "could_have_been_withheld=true",
    "prescribed_by_declaring_side=false",
    "attestation_words_authored_by_receiver_only=true",
    "confirmed_by_receiver_at=2026-07-28T06:37:56Z",
)


class ReceiverOriginatingModalFactEvaluationOperationTests(unittest.TestCase):
    """Verify one exact two-condition source-support operation only."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            BOUNDARY_PATH,
            DECLARATION_PATH,
            CANDIDATE_PATH,
            ATTESTATION_PATH,
            RECEIPT_PATH,
            REPO_ROOT
            / "spec/RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_V0_MIN_SPEC.md",
            REPO_ROOT
            / "spec/RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_V0_MIN_TERMINAL_SUMMARY.md",
            REPO_ROOT / "spec/PRESENCE_RE_EVALUATION_OPERATION_V0_MIN_SPEC.md",
            REPO_ROOT
            / "spec/PRESENCE_RE_EVALUATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
            REPO_ROOT
            / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENCY_OPERATION_TERMINAL_SUMMARY_V0.md",
            REPO_ROOT
            / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
            REPO_ROOT
            / "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ANSWERABLE_RECEIPT_OPERATION_V0_MIN_TERMINAL_SUMMARY.md",
        )
        for path in cls.preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input missing: {path}")
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("canonical evaluation output root must be absent")
        cls.preserved_hashes = {
            path: cls.sha256(path) for path in cls.preserved_paths
        }
        cls.specification_bytes = SPECIFICATION_PATH.read_bytes()
        cls.boundary_bytes = BOUNDARY_PATH.read_bytes()
        cls.declaration_bytes = DECLARATION_PATH.read_bytes()
        cls.candidate_bytes = CANDIDATE_PATH.read_bytes()
        cls.attestation_bytes = ATTESTATION_PATH.read_bytes()
        cls.receipt_bytes = RECEIPT_PATH.read_bytes()
        cls.boundary_artifact = cls.strict_json(cls.boundary_bytes)
        cls.candidate_artifact = cls.strict_json(cls.candidate_bytes)
        cls.attestation_artifact = cls.strict_json(cls.attestation_bytes)
        cls.receipt_artifact = cls.strict_json(cls.receipt_bytes)
        for name in (
            "boundary_artifact",
            "candidate_artifact",
            "attestation_artifact",
            "receipt_artifact",
        ):
            if not isinstance(getattr(cls, name), dict):
                raise AssertionError(f"{name} is not a mapping")
        cls.canonical_request = (
            resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_request()
        )
        cls.canonical_supported_result = cls.resolve_direct(
            cls.canonical_request
        )
        if (
            cls.canonical_supported_result.get("outcome")
            != resolver.OUTCOME_SUPPORTED
        ):
            raise AssertionError(
                "exact standing basis did not produce the supported branch"
            )

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.preserved_hashes.items():
            if cls.sha256(path) != expected:
                raise AssertionError(f"preserved input changed: {path}")
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("test suite created a canonical live artifact root")

    @staticmethod
    def sha256(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def reject_duplicate_keys(
        pairs: list[tuple[str, object]],
    ) -> dict[str, object]:
        value: dict[str, object] = {}
        for key, item in pairs:
            if key in value:
                raise AssertionError(f"duplicate fixture key: {key}")
            value[key] = item
        return value

    @classmethod
    def strict_json(cls, raw: bytes) -> object:
        return json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=cls.reject_duplicate_keys,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AssertionError(f"non-finite fixture value: {value}")
            ),
        )

    @staticmethod
    def write_bytes(path: Path, raw: bytes) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            raise AssertionError(f"fixture path collision: {path}")
        path.write_bytes(raw)
        return path

    @classmethod
    def write_json(cls, path: Path, value: object) -> Path:
        return cls.write_bytes(
            path,
            (
                json.dumps(
                    value,
                    indent=2,
                    sort_keys=True,
                    ensure_ascii=True,
                    allow_nan=False,
                )
                + "\n"
            ).encode("utf-8"),
        )

    @staticmethod
    def set_path(
        mapping: dict[str, Any],
        keys: tuple[str, ...],
        value: object,
    ) -> None:
        selected = mapping
        for key in keys[:-1]:
            nested = selected.get(key)
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {keys}")
            selected = nested
        selected[keys[-1]] = copy.deepcopy(value)

    @classmethod
    def resolve_direct(
        cls,
        request: object | None = None,
        **path_overrides: Path,
    ) -> dict[str, Any]:
        supplied = (
            copy.deepcopy(cls.canonical_request)
            if request is None and hasattr(cls, "canonical_request")
            else copy.deepcopy(request)
        )
        if supplied is None:
            supplied = (
                resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_request()
            )
        before = copy.deepcopy(supplied)
        paths = {
            "governing_specification_path": SPECIFICATION_PATH,
            "boundary_artifact_path": BOUNDARY_PATH,
            "declaration_surface_path": DECLARATION_PATH,
            "candidate_sufficiency_artifact_path": CANDIDATE_PATH,
            "receiver_attestation_artifact_path": ATTESTATION_PATH,
            "receiver_answerable_receipt_artifact_path": RECEIPT_PATH,
        }
        paths.update(path_overrides)
        result = (
            resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min(
                supplied,
                **paths,
            )
        )
        if supplied != before:
            raise AssertionError("resolver mutated the supplied request")
        if not isinstance(result, dict):
            raise AssertionError("resolver result is not a mapping")
        return result

    def supported_result(self) -> dict[str, Any]:
        return copy.deepcopy(self.canonical_supported_result)

    def operation(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(OPERATION_KEY)
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result.get(CHECKS_KEY)
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def assert_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        passed = sum(item.get("passed") is True for item in checks)
        failed = sum(item.get("passed") is False for item in checks)
        self.assertEqual(result.get("passed_check_count"), passed)
        self.assertEqual(result.get("failed_check_count"), failed)
        self.assertEqual(len(checks), passed + failed)
        for item in checks:
            self.assertIs(type(item.get("passed")), bool)
            for key in ("block_code", "failure_code"):
                if key in item:
                    self.assertIn(item[key], resolver.BLOCK_CODES)

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(
            all(type(value) is bool and value is False for value in non_claims.values())
        )
        self.assertIs(result.get("result_level_non_claims_canonical_false"), True)

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            result.get("operation_result"),
            resolver.OPERATION_RESULT_NOT_EVALUATED,
        )
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        operation = self.operation(result)
        self.assertIs(operation.get("operation_basis_admitted"), False)
        self.assertIs(
            operation.get(
                "receiver_originating_modal_fact_evaluation_performed"
            ),
            False,
        )
        self.assertEqual(
            operation.get("completed_modal_fact_evaluation_result_posture_count"),
            0,
        )
        for target in EXPECTED_TARGETS:
            self.assertEqual(
                result["target_condition_evaluations"][target]["evaluation"],
                resolver.TARGET_EVALUATION_NOT_EVALUATED,
            )
            self.assertIs(operation.get(target + "_supported"), False)
        self.assertIsNone(result.get("admissible_future_route"))
        self.assert_counts(result)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        self.assert_non_claims_false(result)

    def assert_completed(
        self,
        result: Mapping[str, Any],
        outcome: str,
        operation_result: str,
    ) -> None:
        self.assertEqual(result.get("outcome"), outcome)
        self.assertEqual(result.get("operation_result"), operation_result)
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assertIs(result.get("block", {}).get("blocked"), False)
        operation = self.operation(result)
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "receiver_originating_modal_fact_evaluation_performed",
            "receiver_originating_modal_fact_evaluation_result_decided",
            "receiver_originating_modal_fact_evaluation_result_recorded",
            "receiver_originating_modal_fact_evaluation_operation_recorded",
            "receiver_originating_modal_fact_evaluation_operation_result_recorded",
            "receiver_originating_modal_fact_evaluation_operation_exhausted",
        ):
            self.assertIs(operation.get(field), True)
        self.assertEqual(
            operation.get("completed_modal_fact_evaluation_result_posture_count"),
            1,
        )
        self.assertEqual(
            result.get("completed_modal_fact_evaluation_result_posture_count"),
            1,
        )
        self.assertIsNone(result.get("admissible_future_route"))
        self.assert_counts(result)
        self.assert_non_claims_false(result)

    def branch_result(self, evaluations: Mapping[str, str]) -> dict[str, Any]:
        base = self.supported_result()
        outcome = resolver._outcome_from_evaluations(evaluations)
        checks: list[dict[str, Any]] = []
        if outcome in {
            resolver.OUTCOME_SUPPORTED,
            resolver.OUTCOME_REQUIRES_BASIS,
            resolver.OUTCOME_INDETERMINATE,
        }:
            resolver._append_completed_checks(checks, outcome, evaluations)
        return resolver._build_result(
            copy.deepcopy(self.canonical_request),
            outcome,
            checks,
            request_validated=True,
            specification_validation=base["specification_validation"],
            boundary_validation=base["boundary_artifact_validation"],
            declaration_validation=base[
                "receiver_originating_declaration_validation"
            ],
            candidate_validation=base[
                "candidate_sufficiency_artifact_validation"
            ],
            attestation_validation=base[
                "receiver_attestation_artifact_validation"
            ],
            receipt_validation=base[
                "receiver_answerable_receipt_artifact_validation"
            ],
            atomic_basis=base["atomic_operation_basis_posture"],
            evaluations=evaluations,
        )

    def resolve_mutated_json(
        self,
        root: Path,
        *,
        label: str,
        source: Mapping[str, Any],
        mutation_path: tuple[str, ...],
        value: object,
        resolver_path_argument: str,
    ) -> dict[str, Any]:
        artifact = copy.deepcopy(dict(source))
        self.set_path(artifact, mutation_path, value)
        path = self.write_json(root / label / "artifact.json", artifact)
        return self.resolve_direct(**{resolver_path_argument: path})

    def test_module_identity_and_exact_families(self) -> None:
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_originating_modal_fact_evaluation_operation_v0_min",
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            (resolver.OPERATION_ID, resolver.OPERATION_TYPE, resolver.OPERATION_VERSION),
            (
                "receiver_originating_modal_fact_evaluation_operation_001",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION",
                "0.1.0",
            ),
        )
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "EVALUATE_ONE_EXACT_RECEIVER_ORIGINATING_DECLARATION_FOR_TWO_RECEIVER_ALLOCATED_MODAL_FACTS_ONLY",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_REQUIRES_BASIS",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_INDETERMINATE",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_BLOCKED",
            ),
        )
        self.assertEqual(
            resolver.OPERATION_RESULT_FAMILY,
            (
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_SUPPORTED",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_REQUIRES_BASIS",
                "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_INDETERMINATE",
                "NOT_EVALUATED",
            ),
        )
        self.assertEqual(
            resolver.TARGET_CONDITION_EVALUATION_FAMILY,
            (
                "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE",
                "REQUIRES_BASIS",
                "INDETERMINATE",
                "NOT_EVALUATED",
            ),
        )
        self.assertEqual(resolver.TARGET_CONDITIONS, EXPECTED_TARGETS)
        self.assertEqual(resolver.EXCLUDED_CONDITIONS, EXPECTED_EXCLUDED)
        self.assertEqual(
            str(resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH),
            "artifacts/integrity_host_v0_min_coexistence_receiver_originating_modal_fact_source_admissibility_boundary_v0_min/receiver_originating_modal_fact_source_admissibility_boundary_001__receiver_originating_modal_fact_source_admissibility_boundary_v0_min_result.json",
        )
        self.assertEqual(
            str(resolver.DECLARATION_SURFACE_RELATIVE_PATH),
            "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/extracted/receiver_attestation_001/freely_given_statement.txt",
        )
        self.assertEqual(
            str(resolver.CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH),
            "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min/receiver_side_answerable_basis_candidate_sufficiency_operation_001__receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min_result_001.json",
        )
        self.assertEqual(
            str(resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH),
            "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_attestation_operation_v0_min/receiver_side_answerable_basis_receiver_attestation_operation_001__receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result_001.json",
        )
        self.assertEqual(
            str(resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH),
            "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min/receiver_side_answerable_basis_receiver_answerable_receipt_operation_001__receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min_result.json",
        )
        self.assertEqual(
            str(resolver.DECLARATION_ARCHIVE_RELATIVE_PATH),
            "artifacts/actual_receiver_attestation_capture/receiver_attestation_capture_001/original_zip/receiver_attestation_001.zip",
        )
        self.assertEqual(
            resolver.DECLARATION_ARCHIVE_MEMBER,
            "receiver_attestation_001/freely_given_statement.txt",
        )
        self.assertEqual(
            resolver.BOUNDARY_SHA256,
            "f24795566eb369ad935e2212aba83ef68bfd1661363cc94da2f53498cc2935ac",
        )
        self.assertEqual(
            resolver.DECLARATION_SHA256,
            "9c1aeb888cd182fdbce789e1bb191f5778712f82483d7eca1334800dac4dd3eb",
        )
        self.assertEqual(
            resolver.DECLARATION_ARCHIVE_SHA256,
            "a45a621c5c6c2f37daefd7e896f32cdb50bff21ab69ec9281912049bd326724c",
        )
        self.assertEqual(
            resolver.CANDIDATE_SUFFICIENCY_SHA256,
            "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4",
        )
        self.assertEqual(
            resolver.RECEIVER_ATTESTATION_SHA256,
            "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9",
        )
        self.assertEqual(
            resolver.RECEIVER_ANSWERABLE_RECEIPT_SHA256,
            "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb",
        )
        self.assertEqual(resolver.SELECTED_SOURCE_CLASS, "RECEIVER_ORIGINATING_DECLARATION_SOURCE")
        self.assertEqual(resolver.SELECTED_RELATION_CLASS, "RECEIVER_ALLOCATED_MODAL_FACT_EVALUATION_RELATION")
        self.assertEqual(resolver.SELECTED_MATTER_CLASS, "RECEIVER_ANSWERABLE_BASIS_REFUSABILITY_AND_WITHHOLDABILITY_ONLY")
        self.assertEqual(resolver.SELECTED_SOURCE_ORIGIN, "RECEIVER_ORIGINATING")
        self.assertEqual(
            resolver.SELECTED_SOURCE_PROVENANCE_POSTURE,
            "DECLARED_RECEIVER_CUSTODY_REFERENCE_ONLY",
        )
        self.assertEqual(resolver.SELECTED_SOURCE_ARRIVAL_POSTURE, "CARRIED_ARRIVAL")
        self.assertEqual(resolver.OUTPUT_ROOT, resolver.CANONICAL_OUTPUT_ROOT)
        self.assertEqual(
            resolver.OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_receiver_originating_modal_fact_evaluation_operation_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_originating_modal_fact_evaluation_operation_001__receiver_originating_modal_fact_evaluation_operation_v0_min_result.json",
        )

    def test_default_result_is_canonical_and_non_executing(self) -> None:
        with (
            patch.object(Path, "read_bytes", side_effect=AssertionError("read")),
            patch.object(Path, "read_text", side_effect=AssertionError("read")),
        ):
            result = (
                resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_default_result()
            )
        self.assertIsNone(result.get("outcome"))
        self.assertEqual(
            result.get("operation_result"),
            resolver.OPERATION_RESULT_NOT_EVALUATED,
        )
        operation = self.operation(result)
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "receiver_originating_modal_fact_evaluation_performed",
            "receiver_originating_modal_fact_evaluation_result_decided",
            "receiver_originating_modal_fact_evaluation_result_recorded",
            "receiver_originating_modal_fact_evaluation_operation_recorded",
            "receiver_originating_modal_fact_evaluation_operation_result_recorded",
            "receiver_originating_modal_fact_evaluation_operation_exhausted",
        ):
            self.assertIs(operation.get(field), False)
        self.assertEqual(result.get("completed_modal_fact_evaluation_result_posture_count"), 0)
        for target in EXPECTED_TARGETS:
            self.assertEqual(result["target_condition_evaluations"][target]["evaluation"], "NOT_EVALUATED")
            self.assertIs(operation.get(target + "_supported"), False)
        self.assertEqual(set(result["excluded_condition_posture"]["condition_evaluations"].values()), {"NOT_EVALUATED"})
        self.assertIs(result["excluded_condition_posture"]["excluded_condition_evaluation_performed"], False)
        self.assertIsNone(result.get("admissible_future_route"))
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assert_non_claims_false(result)
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_canonical_request_is_exact_and_contains_no_semantic_preclaim(self) -> None:
        request = resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_request()
        self.assertEqual(set(request), resolver._canonical_request_keys())
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["selected_matter"], list(EXPECTED_TARGETS))
        self.assertIs(type(request["selected_matter"]), list)
        self.assertIs(request["receiver_originating_modal_fact_evaluation_execution_selected"], True)
        expected_paths = {
            "governing_receiver_originating_modal_fact_evaluation_operation_specification_path": str(
                resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
            ),
            "receiver_originating_modal_fact_source_admissibility_boundary_artifact_path": str(
                resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH
            ),
            "selected_receiver_originating_declaration_surface_path": str(
                resolver.DECLARATION_SURFACE_RELATIVE_PATH
            ),
            "selected_candidate_sufficiency_operation_artifact_path": str(
                resolver.CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
            ),
            "selected_receiver_attestation_operation_artifact_path": str(
                resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
            ),
            "selected_receiver_answerable_receipt_operation_artifact_path": str(
                resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
            ),
            "selected_receiver_originating_declaration_archive_path": str(
                resolver.DECLARATION_ARCHIVE_RELATIVE_PATH
            ),
        }
        for field, expected in expected_paths.items():
            self.assertEqual(request[field], expected)
            self.assertIs(type(request[field]), str)
        self.assertEqual(
            request["selected_receiver_originating_declaration_archive_member"],
            resolver.DECLARATION_ARCHIVE_MEMBER,
        )
        self.assertEqual(request["selected_receiver_originating_declaration_byte_count"], 207)
        self.assertIs(type(request["selected_receiver_originating_declaration_byte_count"]), int)
        self.assertEqual(
            request["selected_receiver_originating_declaration_sha256"],
            resolver.DECLARATION_SHA256,
        )
        self.assertEqual(
            request["selected_receiver_originating_declaration_archive_sha256"],
            resolver.DECLARATION_ARCHIVE_SHA256,
        )
        self.assertEqual(request["selected_receiver_originating_declaration_candidate_id"], "receiver_side_answerable_basis_candidate_001")
        self.assertEqual(request["selected_receiver_originating_declaration_source_provenance_reference"], "declared://receiver-custody/IAMMAI-RECEIVER/receiver_attestation_001")
        self.assertEqual(request["selected_receiver_originating_declaration_receipt_bundle"], "receiver_attestation_001")
        self.assertEqual(request["selected_receiver_originating_declaration_receiver_label"], "Mario")
        self.assertEqual(request["selected_source_class"], resolver.SELECTED_SOURCE_CLASS)
        self.assertEqual(request["selected_relation_class"], resolver.SELECTED_RELATION_CLASS)
        self.assertEqual(request["selected_matter_class"], resolver.SELECTED_MATTER_CLASS)
        self.assertEqual(request["selected_source_origin"], resolver.SELECTED_SOURCE_ORIGIN)
        self.assertEqual(
            request["selected_source_provenance_posture"],
            resolver.SELECTED_SOURCE_PROVENANCE_POSTURE,
        )
        self.assertEqual(
            request["selected_source_arrival_posture"],
            resolver.SELECTED_SOURCE_ARRIVAL_POSTURE,
        )
        self.assertIs(request["selected_source_native_standing"], False)
        self.assertIs(request["jurisdiction_distinction_preserved"], True)
        self.assertEqual(set(request["declared_non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(value is False for value in request["declared_non_claims"].values()))
        for field in resolver.PROHIBITED_DIRECT_REQUEST_FIELDS | {
            "receiver_actual_refusal_established",
            "receiver_actual_withholding_established",
            "receiver_freedom_established",
            "excluded_condition_values",
            "output",
            "action",
            "follow_on_authorized",
        }:
            self.assertNotIn(field, request)

    def test_valid_canonical_execution_is_supported(self) -> None:
        result = self.resolve_direct(copy.deepcopy(self.canonical_request))
        self.assert_completed(result, resolver.OUTCOME_SUPPORTED, resolver.OPERATION_RESULT_SUPPORTED)
        operation = self.operation(result)
        for target in EXPECTED_TARGETS:
            self.assertEqual(result["target_condition_evaluations"][target]["evaluation"], resolver.TARGET_EVALUATION_SUPPORTED)
            self.assertIs(operation[target + "_supported"], True)
        self.assertEqual(operation["missing_or_insufficient_modal_fact_basis"], [])
        self.assertEqual(operation["indeterminate_modal_fact_conditions"], [])
        atomic = result["atomic_operation_basis_posture"]
        self.assertTrue(all(value is True for value in atomic.values()))
        for key in (
            "boundary_artifact_validation",
            "candidate_sufficiency_artifact_validation",
            "receiver_attestation_artifact_validation",
            "receiver_answerable_receipt_artifact_validation",
        ):
            validation = result[key]
            self.assertIs(validation["artifact_validated"], True)
            self.assertEqual(validation["expected_sha256"], validation["observed_sha256"])
        declaration = result["receiver_originating_declaration_validation"]
        self.assertIs(declaration["declaration_validated"], True)
        self.assertEqual(declaration["expected_sha256"], declaration["observed_sha256"])
        self.assertEqual(
            declaration["declaration_surface_path"],
            str(resolver.DECLARATION_SURFACE_RELATIVE_PATH),
        )
        self.assertEqual(
            declaration["declaration_archive_path"],
            str(resolver.DECLARATION_ARCHIVE_RELATIVE_PATH),
        )
        self.assertEqual(
            declaration["declaration_archive_member"],
            resolver.DECLARATION_ARCHIVE_MEMBER,
        )
        self.assertEqual(declaration["expected_byte_count"], resolver.DECLARATION_BYTE_COUNT)
        self.assertEqual(
            declaration["archive_sha256_identity"],
            resolver.DECLARATION_ARCHIVE_SHA256,
        )
        self.assertEqual(declaration["candidate_id"], resolver.DECLARATION_CANDIDATE_ID)
        self.assertEqual(
            declaration["source_provenance_reference"],
            resolver.DECLARATION_PROVENANCE_REFERENCE,
        )
        self.assertEqual(declaration["receipt_bundle"], resolver.DECLARATION_RECEIPT_BUNDLE)
        self.assertEqual(declaration["receiver_label"], resolver.DECLARATION_RECEIVER_LABEL)
        for field, expected in (
            ("selected_source_class", resolver.SELECTED_SOURCE_CLASS),
            ("selected_relation_class", resolver.SELECTED_RELATION_CLASS),
            ("selected_matter_class", resolver.SELECTED_MATTER_CLASS),
            ("selected_source_origin", resolver.SELECTED_SOURCE_ORIGIN),
            (
                "selected_source_provenance_posture",
                resolver.SELECTED_SOURCE_PROVENANCE_POSTURE,
            ),
            ("selected_source_arrival_posture", resolver.SELECTED_SOURCE_ARRIVAL_POSTURE),
        ):
            self.assertEqual(operation[field], expected)
        self.assertIs(operation["selected_source_native_standing"], False)
        self.assertIs(operation["jurisdiction_distinction_preserved"], True)
        self.assertIs(result["specification_validation"]["specification_validated"], True)

    def test_supported_result_does_not_establish_modal_fact_or_presence(self) -> None:
        result = self.supported_result()
        operation = self.operation(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                self.assertIs(result["non_claims"][field], False)
                self.assertIs(operation[field], False)
        for field in (
            "receiver_answerable_basis_refusable_established",
            "receiver_answerable_basis_could_have_been_withheld_established",
            "receiver_actual_refusal_established",
            "receiver_actual_withholding_established",
            "receiver_freedom_established",
            "receiver_originating_declaration_truth_created",
            "receiver_originating_declaration_authority_created",
            "source_authority_created",
            "canon_admission_created",
            "governance_force_created",
            "truth_created",
            "standing_created",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(operation[field], False)
        self.assertIs(result["result_level_non_claims_canonical_false"], True)

    def test_supported_result_preserves_source_origin_and_jurisdiction(self) -> None:
        result = self.supported_result()
        lineage = result["lineage_preservation_posture"]
        self.assertEqual(set(lineage), set(resolver.LINEAGE_PRESERVATION_FIELDS))
        self.assertTrue(all(value is True for value in lineage.values()))
        source = result["source_selection_and_carriage_lineage"]
        self.assertIs(source["receiver_origin_validated"], True)
        self.assertIs(source["declared_provenance_posture_validated"], True)
        self.assertIs(source["carried_arrival_validated"], True)
        self.assertIs(source["non_native_standing_validated"], True)
        self.assertIs(source["jurisdiction_distinction_validated"], True)

    def test_supported_result_preserves_prior_presence_without_revision(self) -> None:
        prior = self.supported_result()["prior_presence_preservation_posture"]
        self.assertEqual(prior["prior_outcome"], resolver.PRIOR_PRESENCE_OUTCOME)
        self.assertEqual(prior["prior_operation_result"], resolver.PRIOR_PRESENCE_RESULT)
        self.assertIs(prior["prior_operation_exhausted"], True)
        self.assertIsNone(prior["prior_admissible_future_route"])
        evaluations = prior["condition_evaluations"]
        self.assertEqual(evaluations["receiver_attested"], "SATISFIED")
        self.assertEqual(evaluations["receiver_answerable_receipt_present"], "SATISFIED")
        for field in resolver.PRIOR_REQUIRES_BASIS_CONDITIONS:
            self.assertEqual(evaluations[field], "REQUIRES_BASIS")
        self.assertIs(prior["all_twelve_prior_requires_basis_conditions_historically_legible"], True)
        for field in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded"):
            self.assertIs(prior[field], False)

    def test_only_two_declaration_records_affect_target_evaluation(self) -> None:
        result = self.supported_result()
        declaration = result["receiver_originating_declaration_validation"]
        self.assertIs(declaration["exact_six_unique_records_validated"], True)
        self.assertEqual(
            declaration["matter_relevant_records"],
            {"could_have_been_refused": True, "could_have_been_withheld": True},
        )
        self.assertEqual(set(result["target_condition_evaluations"]), set(EXPECTED_TARGETS))
        self.assertEqual(
            {
                item["matter_relevant_declaration_record"]
                for item in result["target_condition_evaluations"].values()
            },
            {"could_have_been_refused", "could_have_been_withheld"},
        )
        serialized = json.dumps(result, sort_keys=True)
        for record in (
            "freely_given=true",
            "prescribed_by_declaring_side=false",
            "attestation_words_authored_by_receiver_only=true",
            "confirmed_by_receiver_at=2026-07-28T06:37:56Z",
        ):
            self.assertNotIn(record, serialized)

    def test_all_excluded_conditions_remain_not_evaluated(self) -> None:
        result = self.supported_result()
        excluded = result["excluded_condition_posture"]
        self.assertEqual(set(excluded["condition_evaluations"]), set(EXPECTED_EXCLUDED))
        self.assertEqual(set(excluded["condition_evaluations"].values()), {"NOT_EVALUATED"})
        self.assertIs(excluded["excluded_condition_evaluation_performed"], False)
        self.assertIs(excluded["excluded_conditions_not_evaluated"], True)
        self.assertNotIn("excluded_condition_evidence_bodies", result)
        self.assertFalse(resolver._contains_prohibited_complete_material(result))

    def test_invalid_request_schema_blocks_before_evaluation(self) -> None:
        def mutate(label: str, change: Callable[[dict[str, Any]], None]) -> tuple[str, dict[str, Any]]:
            request = copy.deepcopy(self.canonical_request)
            change(request)
            return label, request

        cases = (
            mutate("missing", lambda value: value.pop("intent")),
            mutate("unknown", lambda value: value.__setitem__("unknown", False)),
            mutate("intent", lambda value: value.__setitem__("intent", "WRONG")),
            mutate("identity", lambda value: value.__setitem__("receiver_originating_modal_fact_evaluation_operation_id", "wrong")),
            mutate("path", lambda value: value.__setitem__("receiver_originating_modal_fact_source_admissibility_boundary_artifact_path", "wrong")),
            mutate("source_class", lambda value: value.__setitem__("selected_source_class", "wrong")),
            mutate("matter_class", lambda value: value.__setitem__("selected_matter_class", "wrong")),
            mutate("matter_order", lambda value: value.__setitem__("selected_matter", list(reversed(EXPECTED_TARGETS)))),
            mutate("selection_type", lambda value: value.__setitem__("receiver_originating_modal_fact_evaluation_execution_selected", 1)),
            mutate("nonclaim_missing", lambda value: value["declared_non_claims"].pop(resolver.REQUIRED_FALSE_NON_CLAIMS[0])),
            mutate("nonclaim_unknown", lambda value: value["declared_non_claims"].__setitem__("unknown", False)),
            mutate("nonclaim_type", lambda value: value["declared_non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], 0)),
            mutate("nonclaim_true", lambda value: value["declared_non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], True)),
            mutate("outcome", lambda value: value.__setitem__("outcome", resolver.OUTCOME_SUPPORTED)),
            mutate("evaluation", lambda value: value.__setitem__(EXPECTED_TARGETS[0], resolver.TARGET_EVALUATION_SUPPORTED)),
            mutate("support", lambda value: value.__setitem__(EXPECTED_TARGETS[0] + "_supported", True)),
            mutate("presence", lambda value: value.__setitem__("presence_supported", True)),
            mutate("semantic", lambda value: value.__setitem__("semantic_payload", {"value": True})),
        )
        for label, request in cases:
            with self.subTest(case=label):
                result = self.resolve_direct(request)
                self.assert_blocked(result)

    def test_duplicate_key_request_json_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = self.write_bytes(
                Path(temporary) / "duplicate.json",
                b'{"intent":"one","intent":"two"}',
            )
            result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(path)
            self.assert_blocked(result, "REQUEST_PATH_DUPLICATE_KEYED")
            self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_non_object_request_json_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, value in enumerate(([], "request", 7, True, None)):
                with self.subTest(value=repr(value)):
                    path = self.write_bytes(
                        root / f"case_{index}.json",
                        json.dumps(value).encode("utf-8"),
                    )
                    result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(path)
                    self.assert_blocked(result, "REQUEST_PATH_NOT_MAPPING")

    def test_duplicate_key_governed_json_blocks(self) -> None:
        duplicate = b'{"duplicate":"BODY_SENTINEL","duplicate":"BODY_SENTINEL"}'
        parsed, error = resolver._parse_json_bytes(duplicate)
        self.assertIsNone(parsed)
        self.assertEqual(error, "duplicate_key")
        cases = (
            ("boundary", "boundary_artifact_path", "BOUNDARY_ARTIFACT_DIGEST_MISMATCH"),
            ("candidate", "candidate_sufficiency_artifact_path", "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH"),
            ("attestation", "receiver_attestation_artifact_path", "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH"),
            ("receipt", "receiver_answerable_receipt_artifact_path", "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, argument, code in cases:
                with self.subTest(artifact=label):
                    path = self.write_bytes(root / label / "duplicate.json", duplicate)
                    result = self.resolve_direct(**{argument: path})
                    self.assert_blocked(result, code)
                    self.assertNotIn("BODY_SENTINEL", json.dumps(result, sort_keys=True))

    def test_digest_mismatch_blocks_each_governed_file(self) -> None:
        spec_mutation = self.specification_bytes.replace(
            b"# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum Specification",
            b"# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum SpecificatioN",
            1,
        )
        declaration_mutation = bytearray(self.declaration_bytes)
        declaration_mutation[0] = ord("F")
        cases = (
            ("specification", "governing_specification_path", spec_mutation, "SPECIFICATION_MARKER_MISSING"),
            ("boundary", "boundary_artifact_path", self.boundary_bytes + b" ", "BOUNDARY_ARTIFACT_DIGEST_MISMATCH"),
            ("declaration", "declaration_surface_path", bytes(declaration_mutation), "DECLARATION_DIGEST_MISMATCH"),
            ("candidate", "candidate_sufficiency_artifact_path", self.candidate_bytes + b" ", "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH"),
            ("attestation", "receiver_attestation_artifact_path", self.attestation_bytes + b" ", "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH"),
            ("receipt", "receiver_answerable_receipt_artifact_path", self.receipt_bytes + b" ", "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, argument, raw, code in cases:
                with self.subTest(file=label):
                    path = self.write_bytes(root / label / "mutated", raw)
                    result = self.resolve_direct(**{argument: path})
                    self.assert_blocked(result, code)

    def test_declaration_requires_exact_207_byte_six_record_utf8_surface(self) -> None:
        text = self.declaration_bytes.decode("utf-8")
        records = text.splitlines()
        mutations = (
            ("wrong_count", self.declaration_bytes + b"x"),
            ("invalid_utf8", b"\xff" + self.declaration_bytes[1:]),
            ("bom", b"\xef\xbb\xbf" + self.declaration_bytes),
            ("duplicate", ("\n".join(records[:-1] + [records[1]]) + "\n").encode()),
            ("missing", ("\n".join(records[:-1]) + "\n").encode()),
            ("unknown", text.replace("freely_given", "unknown_record", 1).encode()),
            ("blank", text.replace(records[2], "", 1).encode()),
            ("malformed", text.replace("freely_given=true", "freely_given", 1).encode()),
            ("timestamp", text.replace("2026-07-28T06:37:56Z", "2026-07-28T06:37:57Z", 1).encode()),
            ("boolean", text.replace("could_have_been_refused=true", "could_have_been_refused=false", 1).encode()),
            ("whitespace", text.replace("freely_given=true", "freely_given =true", 1).encode()),
            ("ordering", ("\n".join(reversed(records)) + "\n").encode()),
            ("matter_key", text.replace("could_have_been_refused", "could_have_been_declined", 1).encode()),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, raw in mutations:
                with self.subTest(declaration=label):
                    path = self.write_bytes(root / label / "statement.txt", raw)
                    result = self.resolve_direct(declaration_surface_path=path)
                    self.assert_blocked(result)
                    self.assertIn(
                        result["block"]["code"],
                        {"DECLARATION_BYTE_COUNT_MISMATCH", "DECLARATION_DIGEST_MISMATCH"},
                    )

    def test_boundary_mismatch_blocks(self) -> None:
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", ("boundary_result",), "WRONG"),
            ("failed", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("selection", (BOUNDARY_KEY + "_summary", "selection"), False),
            ("source_selection", (BOUNDARY_KEY, "source_selection_recorded"), False),
            ("admissibility", (BOUNDARY_KEY, "source_admissibility_evaluation"), "NOT_PASSED"),
            ("exhausted", (BOUNDARY_KEY, BOUNDARY_KEY + "_exhausted"), False),
            ("cardinality", (BOUNDARY_KEY, "completed_consideration_posture_count"), 2),
            ("source_class", (BOUNDARY_KEY, "selected_source_class"), "WRONG"),
            ("relation", (BOUNDARY_KEY, "selected_relation_class"), "WRONG"),
            ("matter", (BOUNDARY_KEY, "selected_matter_class"), "WRONG"),
            ("origin", (BOUNDARY_KEY, "selected_source_origin"), "WRONG"),
            ("native", (BOUNDARY_KEY, "selected_source_native_standing"), True),
            ("jurisdiction", (BOUNDARY_KEY, "jurisdiction_distinction_preserved"), False),
            ("naturalized", (BOUNDARY_KEY + "_summary", "source_not_naturalized"), False),
            ("route", (BOUNDARY_KEY, "admissible_future_route"), "WRONG"),
            ("false_lock", (BOUNDARY_KEY, resolver.BOUNDARY_FALSE_LOCKS[0]), True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, path, value in cases:
                with self.subTest(boundary=label):
                    result = self.resolve_mutated_json(
                        root,
                        label=label,
                        source=self.boundary_artifact,
                        mutation_path=path,
                        value=value,
                        resolver_path_argument="boundary_artifact_path",
                    )
                    self.assert_blocked(result, "BOUNDARY_ARTIFACT_DIGEST_MISMATCH")

    def test_candidate_sufficiency_mismatch_blocks(self) -> None:
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", (CANDIDATE_KEY, "operation_result"), "WRONG"),
            ("candidate", (CANDIDATE_KEY, "receiver_side_answerable_basis_candidate_id"), "wrong"),
            ("compatibility", (CANDIDATE_KEY + "_dimensions", "refusal_withholding_compatibility", "dimension_result"), "NOT_SATISFIED"),
            ("failed", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("exhausted", (CANDIDATE_KEY, "candidate_sufficiency_operation_exhausted"), False),
            ("result_count", ("operation_result_detail", "candidate_result_posture_count"), 2),
            ("dimension_count", ("operation_result_detail", "evaluated_dimension_count"), 7),
            ("false_lock", ("non_claims", next(iter(self.candidate_artifact["non_claims"]))), True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, path, value in cases:
                with self.subTest(candidate=label):
                    result = self.resolve_mutated_json(
                        root,
                        label=label,
                        source=self.candidate_artifact,
                        mutation_path=path,
                        value=value,
                        resolver_path_argument="candidate_sufficiency_artifact_path",
                    )
                    self.assert_blocked(result, "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH")

    def test_receiver_attestation_mismatch_blocks(self) -> None:
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", (ATTESTATION_KEY, "receiver_attestation_operation_result"), "WRONG"),
            ("candidate", (ATTESTATION_KEY, "receiver_side_answerable_basis_candidate_id"), "wrong"),
            ("basis", (ATTESTATION_KEY, "operation_basis_admitted"), False),
            ("recorded", (ATTESTATION_KEY, "receiver_attestation_recorded"), False),
            ("failed", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("exhausted", (ATTESTATION_KEY, "receiver_attestation_operation_exhausted"), False),
            ("cardinality", ("operation_result_detail", "completed_result_posture_count"), 2),
            ("false_lock", ("non_claims", next(iter(self.attestation_artifact["non_claims"]))), True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, path, value in cases:
                with self.subTest(attestation=label):
                    result = self.resolve_mutated_json(
                        root,
                        label=label,
                        source=self.attestation_artifact,
                        mutation_path=path,
                        value=value,
                        resolver_path_argument="receiver_attestation_artifact_path",
                    )
                    self.assert_blocked(result, "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH")

    def test_receiver_answerable_receipt_mismatch_blocks(self) -> None:
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", (RECEIPT_KEY, "receiver_answerable_receipt_operation_result"), "WRONG"),
            ("candidate", (RECEIPT_KEY, "receiver_side_answerable_basis_candidate_id"), "wrong"),
            ("attestation", (RECEIPT_KEY, "selected_receiver_attestation_operation_id"), "wrong"),
            ("present", (RECEIPT_KEY, "receiver_answerable_receipt_present"), False),
            ("recorded", (RECEIPT_KEY, "receiver_answerable_receipt_recorded"), False),
            ("failed", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("exhausted", (RECEIPT_KEY, "receiver_answerable_receipt_operation_exhausted"), False),
            ("cardinality", (RECEIPT_KEY, "completed_result_posture_count"), 2),
            ("false_lock", ("non_claims", next(iter(self.receipt_artifact["non_claims"]))), True),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, path, value in cases:
                with self.subTest(receipt=label):
                    result = self.resolve_mutated_json(
                        root,
                        label=label,
                        source=self.receipt_artifact,
                        mutation_path=path,
                        value=value,
                        resolver_path_argument="receiver_answerable_receipt_artifact_path",
                    )
                    self.assert_blocked(result, "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH")

    def test_atomic_basis_is_all_or_nothing(self) -> None:
        arguments = (
            "governing_specification_path",
            "boundary_artifact_path",
            "declaration_surface_path",
            "candidate_sufficiency_artifact_path",
            "receiver_attestation_artifact_path",
            "receiver_answerable_receipt_artifact_path",
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for argument in arguments:
                with self.subTest(missing=argument):
                    result = self.resolve_direct(**{argument: root / argument / "missing"})
                    self.assert_blocked(result)
                    self.assertIs(result["atomic_operation_basis_posture"]["operation_basis_admitted"], False)
                    self.assertEqual(
                        {
                            result["target_condition_evaluations"][target]["evaluation"]
                            for target in EXPECTED_TARGETS
                        },
                        {resolver.TARGET_EVALUATION_NOT_EVALUATED},
                    )

    def test_target_evaluation_precedence(self) -> None:
        s = resolver.TARGET_EVALUATION_SUPPORTED
        r = resolver.TARGET_EVALUATION_REQUIRES_BASIS
        i = resolver.TARGET_EVALUATION_INDETERMINATE
        cases = (
            ((s, s), resolver.OUTCOME_SUPPORTED),
            ((s, r), resolver.OUTCOME_REQUIRES_BASIS),
            ((r, r), resolver.OUTCOME_REQUIRES_BASIS),
            ((s, i), resolver.OUTCOME_INDETERMINATE),
            ((r, i), resolver.OUTCOME_INDETERMINATE),
            ((i, i), resolver.OUTCOME_INDETERMINATE),
            ((s, "UNEXPECTED"), resolver.OUTCOME_BLOCKED),
        )
        for values, expected in cases:
            evaluations = dict(zip(EXPECTED_TARGETS, values))
            with self.subTest(evaluations=values):
                self.assertEqual(resolver._outcome_from_evaluations(evaluations), expected)

    def test_requires_basis_branch_is_completed_not_failed(self) -> None:
        evaluations = {
            EXPECTED_TARGETS[0]: resolver.TARGET_EVALUATION_SUPPORTED,
            EXPECTED_TARGETS[1]: resolver.TARGET_EVALUATION_REQUIRES_BASIS,
        }
        result = self.branch_result(evaluations)
        self.assert_completed(result, resolver.OUTCOME_REQUIRES_BASIS, resolver.OPERATION_RESULT_REQUIRES_BASIS)
        operation = self.operation(result)
        self.assertEqual(operation["missing_or_insufficient_modal_fact_basis"], [EXPECTED_TARGETS[1]])
        self.assertIs(operation[EXPECTED_TARGETS[0] + "_supported"], True)
        self.assertIs(operation[EXPECTED_TARGETS[1] + "_supported"], False)
        self.assertEqual(operation["indeterminate_modal_fact_conditions"], [])
        self.assertIsNone(result["admissible_future_route"])

    def test_indeterminate_branch_is_completed_not_failed(self) -> None:
        evaluations = {
            EXPECTED_TARGETS[0]: resolver.TARGET_EVALUATION_SUPPORTED,
            EXPECTED_TARGETS[1]: resolver.TARGET_EVALUATION_INDETERMINATE,
        }
        result = self.branch_result(evaluations)
        self.assert_completed(result, resolver.OUTCOME_INDETERMINATE, resolver.OPERATION_RESULT_INDETERMINATE)
        operation = self.operation(result)
        self.assertEqual(operation["indeterminate_modal_fact_conditions"], [EXPECTED_TARGETS[1]])
        self.assertIs(operation[EXPECTED_TARGETS[0] + "_supported"], True)
        self.assertIs(operation[EXPECTED_TARGETS[1] + "_supported"], False)
        self.assertNotEqual(result["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertIsNone(result["admissible_future_route"])

    def test_checks_are_deterministic_and_counts_are_derived(self) -> None:
        first = self.resolve_direct(copy.deepcopy(self.canonical_request))
        second = self.resolve_direct(copy.deepcopy(self.canonical_request))
        self.assertEqual(first, second)
        self.assertEqual(first[CHECKS_KEY], second[CHECKS_KEY])
        self.assert_counts(first)
        self.assertEqual(first["failed_check_count"], 0)
        self.assertGreater(first["passed_check_count"], 0)

    def test_summary_is_exact_projection_of_result(self) -> None:
        result = self.supported_result()
        summary = resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_summary(result)
        self.assertEqual(summary, result[SUMMARY_KEY])
        self.assertNotIn(CHECKS_KEY, summary)
        self.assertNotIn("non_claims", summary)
        self.assertFalse(resolver._contains_prohibited_complete_material(summary))
        self.assertNotIn(self.declaration_bytes.decode("utf-8"), json.dumps(summary, sort_keys=True))

    def test_result_omission_posture_and_no_prohibited_material(self) -> None:
        result = self.supported_result()
        omission = result["omission_posture"]
        self.assertEqual(
            set(omission),
            {*resolver.OMISSION_POSTURE_FIELDS, "complete_material_omission_posture"},
        )
        self.assertTrue(all(value is True for value in omission.values()))
        self.assertFalse(resolver._contains_prohibited_complete_material(result))
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn(self.declaration_bytes.decode("utf-8"), serialized)
        for artifact in (
            self.boundary_artifact,
            self.candidate_artifact,
            self.attestation_artifact,
            self.receipt_artifact,
        ):
            self.assertNotIn(json.dumps(artifact, sort_keys=True), serialized)

    def test_from_path_matches_direct_resolution(self) -> None:
        request = copy.deepcopy(self.canonical_request)
        direct = self.resolve_direct(request)
        with tempfile.TemporaryDirectory() as temporary:
            path = self.write_json(Path(temporary) / "request.json", request)
            before = path.read_bytes()
            from_path = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(
                path,
                governing_specification_path=SPECIFICATION_PATH,
                boundary_artifact_path=BOUNDARY_PATH,
                declaration_surface_path=DECLARATION_PATH,
                candidate_sufficiency_artifact_path=CANDIDATE_PATH,
                receiver_attestation_artifact_path=ATTESTATION_PATH,
                receiver_answerable_receipt_artifact_path=RECEIPT_PATH,
            )
            self.assertEqual(from_path, direct)
            self.assertEqual(path.read_bytes(), before)

    def test_from_path_missing_or_malformed_request_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "directory"
            directory.mkdir()
            cases = (
                (root / "missing.json", "REQUEST_PATH_MISSING"),
                (directory, "REQUEST_PATH_MISSING"),
                (self.write_bytes(root / "malformed.json", b"{"), "REQUEST_PATH_NOT_PARSEABLE"),
                (self.write_bytes(root / "duplicate.json", b'{"x":1,"x":2}'), "REQUEST_PATH_DUPLICATE_KEYED"),
                (self.write_bytes(root / "array.json", b"[]"), "REQUEST_PATH_NOT_MAPPING"),
                (self.write_bytes(root / "nan.json", b'{"value":NaN}'), "REQUEST_PATH_NOT_PARSEABLE"),
            )
            for path, code in cases:
                with self.subTest(path=path.name):
                    result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(path)
                    self.assert_blocked(result, code)

    def assert_written_json(self, path: Path, result: Mapping[str, Any]) -> None:
        text = path.read_text(encoding="utf-8")
        self.assertEqual(
            text,
            json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n",
        )
        self.assertEqual(json.loads(text), result)

    def test_writer_accepts_only_valid_completed_result(self) -> None:
        result = self.supported_result()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.OUTPUT_ROOT_NAME
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                path = resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(result)
            self.assertEqual(path, output_root / resolver.OUTPUT_FILENAME)
            self.assert_written_json(path, result)
            self.assertEqual(tuple(output_root.iterdir()), (path,))
            self.assertEqual(tuple(root.iterdir()), (output_root,))
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_writer_refuses_default_blocked_or_inconsistent_result(self) -> None:
        valid = self.supported_result()
        blocked = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min([])
        invalid: list[tuple[str, object]] = [
            ("default", resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_default_result()),
            ("non_mapping", []),
            ("malformed", {}),
        ]

        def changed(label: str, mutation: Callable[[dict[str, Any]], None], source: Mapping[str, Any] = valid) -> None:
            value = copy.deepcopy(dict(source))
            mutation(value)
            invalid.append((label, value))

        changed("missing_section", lambda value: value.pop("operation_posture"))
        changed("extra_section", lambda value: value.__setitem__("extra", False))
        changed("outcome_result", lambda value: value.__setitem__("operation_result", resolver.OPERATION_RESULT_INDETERMINATE))
        changed("branch", lambda value: value[OPERATION_KEY].__setitem__("operation_basis_admitted", False))
        changed("summary", lambda value: value[SUMMARY_KEY].__setitem__("outcome", "WRONG"))
        changed("failed_check", lambda value: value[CHECKS_KEY][0].__setitem__("passed", False))
        changed("nonclaim", lambda value: value["non_claims"].__setitem__(resolver.REQUIRED_FALSE_NON_CLAIMS[0], True))
        changed("support", lambda value: value["target_support_posture"].__setitem__(EXPECTED_TARGETS[0] + "_supported", False))
        changed("route", lambda value: value.__setitem__("admissible_future_route", "AUTOMATIC"))
        changed("complete_material", lambda value: value.__setitem__("complete_declaration_body", "body"))
        changed("blocked_inconsistent", lambda value: value[OPERATION_KEY].__setitem__("operation_basis_admitted", True), blocked)
        with tempfile.TemporaryDirectory() as temporary:
            output_root = Path(temporary) / resolver.OUTPUT_ROOT_NAME
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for label, result in invalid:
                    with self.subTest(result=label):
                        with self.assertRaises(resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError):
                            resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(result)
                        self.assertFalse(output_root.exists())

    def test_writer_refuses_noncanonical_path_and_overwrite(self) -> None:
        result = self.supported_result()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output_root = root / resolver.OUTPUT_ROOT_NAME
            canonical = output_root / resolver.OUTPUT_FILENAME
            refused = (
                output_root / "alternate.json",
                root / "sibling" / resolver.OUTPUT_FILENAME,
                output_root / ".." / "outside.json",
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for path in refused:
                    with self.subTest(path=str(path)):
                        with self.assertRaises(resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError):
                            resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(result, path)
                        self.assertFalse(path.resolve().exists())
                written = resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(result)
                before = written.read_bytes()
                with self.assertRaises(resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError):
                    resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(result)
                self.assertEqual(written, canonical)
                self.assertEqual(written.read_bytes(), before)
                self.assertEqual(tuple(output_root.iterdir()), (canonical,))

    def test_no_scan_discovery_network_randomness_or_timestamp_generation(self) -> None:
        source = RESOLVER_PATH.read_text(encoding="utf-8")
        tree = ast.parse(source)
        prohibited_modules = {
            "datetime",
            "glob",
            "os",
            "random",
            "requests",
            "socket",
            "subprocess",
            "time",
            "urllib",
            "zipfile",
        }
        imported: set[str] = set()
        called_attributes: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                called_attributes.add(node.func.attr)
        self.assertFalse(imported.intersection(prohibited_modules))
        self.assertFalse(
            called_attributes.intersection(
                {"glob", "rglob", "iterdir", "listdir", "scandir", "walk", "getenv", "extract", "extractall"}
            )
        )
        for token in (
            "select_latest",
            "archive.read(",
            "normalize_source",
            "repair_artifact",
        ):
            self.assertNotIn(token, source)

    def test_result_structure_and_exact_section_set(self) -> None:
        result = self.supported_result()
        self.assertEqual(set(result), set(resolver.RESULT_SECTIONS))
        self.assertEqual(result["operation_result"], result["receiver_originating_modal_fact_evaluation_operation_result"])
        self.assertEqual(result[SUMMARY_KEY]["outcome"], result["outcome"])
        self.assertEqual(result[SUMMARY_KEY]["operation_result"], result["operation_result"])
        self.assertEqual(result[SUMMARY_KEY]["failed_check_count"], result["failed_check_count"])
        self.assertEqual(result[SUMMARY_KEY]["passed_check_count"], result["passed_check_count"])
        self.assertTrue(resolver._result_valid_for_write(result))

    def test_non_meaning_and_blocked_conversion_posture(self) -> None:
        result = self.supported_result()
        non_meaning = result[NON_MEANING_KEY]
        self.assertEqual(set(non_meaning), set(resolver.NON_MEANING_FIELDS))
        self.assertTrue(all(value is True for value in non_meaning.values()))
        self.assertEqual(result["blocked_conversions"], list(resolver.BLOCKED_CONVERSIONS))
        self.assertEqual(tuple(result["blocked_conversions"]), resolver.BLOCKED_CONVERSIONS)
        self.assertIsNone(result["admissible_future_route"])
        self.assert_non_claims_false(result)

    def test_what_remains_open_is_bounded_and_non_authorizing(self) -> None:
        result = self.supported_result()
        open_items = result["what_remains_open"]
        self.assertIsInstance(open_items, list)
        self.assertNotIn("receiver-originating modal-fact evaluation operation resolver", open_items)
        for item in (
            "receiver-originating modal-fact evaluation operation tests",
            "receiver-originating modal-fact evaluation operation request",
            "receiver-originating modal-fact evaluation operation live result",
            "receiver-originating modal-fact evaluation operation terminal summary",
            "later presence re-evaluation",
            "threshold",
            "truth settlement",
            "FIELD machinery",
            "follow-on work",
        ):
            self.assertIn(item, open_items)
        self.assertIs(result[NON_MEANING_KEY]["open_does_not_mean_next"], True)
        self.assertIsNone(result["admissible_future_route"])
        for field in (
            "scheduled_presence_re_evaluation_created",
            "automatic_next_step_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(result["non_claims"][field], False)


if __name__ == "__main__":
    unittest.main()
