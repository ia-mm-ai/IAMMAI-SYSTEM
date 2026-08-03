"""Tests for the additive no-partial-ledger successor correction.

The suite consumes the exact completed v1 operation artifact, validates its
ten-row standing, and exercises one v2 append only.  Mutation and writer
fixtures remain in temporary directories; no live v2 artifact is created.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Callable
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2 as resolver


SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
V1_ARTIFACT_PATH = REPO_ROOT / resolver.PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

EXPECTED_REQUEST_KEYS = {
    "intent",
    "successor_id",
    "successor_type",
    "successor_version",
    "successor_scope",
    "governing_specification_path",
    "governing_specification_sha256",
    "prior_operation_artifact_path",
    "prior_operation_artifact_sha256",
    "prior_operation_id",
    "prior_operation_type",
    "prior_operation_version",
    "prior_operation_scope",
    "selected_matter_class",
    "contradiction_id",
    "contradictory_field_path",
    "prior_field_value",
    "successor_field_value",
    "correction_reason",
    "one_field_difference_contract",
    "required_v1_standing_contract",
    "unaffected_standing_preservation_contract",
    "declared_non_claims",
}

EXPECTED_ONE_FIELD_DIFFERENCE_KEYS = {
    "field_path",
    "prior_value",
    "successor_value",
    "correction_reason",
    "prior_value_preserved_as_historical",
    "successor_value_appended",
}


class DuplicateJsonKeyError(ValueError):
    """Raised by the suite's independent strict JSON parser."""


def reject_duplicate_json_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKeyError(key)
        result[key] = value
    return result


def reject_non_finite_json(value: str) -> Any:
    raise ValueError(value)


def strict_json_bytes(raw: bytes) -> dict[str, Any]:
    value = json.loads(
        raw.decode("utf-8", errors="strict"),
        object_pairs_hook=reject_duplicate_json_keys,
        parse_constant=reject_non_finite_json,
    )
    if not isinstance(value, dict):
        raise AssertionError("strict JSON root is not a mapping")
    return value


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_value_digest(value: Any) -> str:
    raw = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return sha256_bytes(raw)


class BodyHeldIntegrityConditionEvaluationOperationV2Tests(unittest.TestCase):
    """Verify one additive successor correction and no wider semantic change."""

    @classmethod
    def setUpClass(cls) -> None:
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("canonical v2 output root must be absent")
        for path in (SPECIFICATION_PATH, V1_ARTIFACT_PATH, RESOLVER_PATH):
            if not path.is_file():
                raise AssertionError(f"required governed surface missing: {path}")
        cls.specification_bytes = SPECIFICATION_PATH.read_bytes()
        cls.v1_bytes = V1_ARTIFACT_PATH.read_bytes()
        cls.resolver_bytes = RESOLVER_PATH.read_bytes()
        cls.governed_hashes = {
            SPECIFICATION_PATH: sha256_bytes(cls.specification_bytes),
            V1_ARTIFACT_PATH: sha256_bytes(cls.v1_bytes),
            RESOLVER_PATH: sha256_bytes(cls.resolver_bytes),
        }
        cls.v1_artifact = strict_json_bytes(cls.v1_bytes)
        cls.canonical_request = cls.new_request()
        cls.recorded_result = cls.resolve_current(cls.canonical_request)
        if cls.recorded_result.get("outcome") != resolver.OUTCOME_RECORDED:
            raise AssertionError("canonical v2 execution did not reach SUCCESSOR_RECORDED")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.governed_hashes.items():
            if not path.is_file() or sha256_bytes(path.read_bytes()) != expected:
                raise AssertionError(f"governed surface changed: {path}")
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("suite created the canonical v2 output root")

    @staticmethod
    def new_request(**overrides: Any) -> dict[str, Any]:
        return resolver.build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request(
            **copy.deepcopy(overrides)
        )

    @classmethod
    def resolve_current(
        cls,
        request: object | None = None,
        **path_overrides: Any,
    ) -> dict[str, Any]:
        supplied = cls.new_request() if request is None else copy.deepcopy(request)
        before = copy.deepcopy(supplied)
        paths: dict[str, Any] = {
            "governing_specification_path": SPECIFICATION_PATH,
            "prior_operation_artifact_path": V1_ARTIFACT_PATH,
        }
        paths.update(path_overrides)
        result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
            supplied,
            **paths,
        )
        if supplied != before:
            raise AssertionError("resolver mutated the supplied request")
        if not isinstance(result, dict):
            raise AssertionError("resolver result is not a mapping")
        return result

    @staticmethod
    def write_bytes(path: Path, raw: bytes) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            raise AssertionError(f"fixture path collision: {path}")
        path.write_bytes(raw)
        return path

    @classmethod
    def write_json(cls, path: Path, value: object) -> tuple[Path, bytes]:
        raw = (
            json.dumps(
                value,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            + "\n"
        ).encode("utf-8")
        return cls.write_bytes(path, raw), raw

    @staticmethod
    def set_path(mapping: dict[str, Any], keys: tuple[str, ...], value: Any) -> None:
        selected = mapping
        for key in keys[:-1]:
            nested = selected.get(key)
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {keys}")
            selected = nested
        selected[keys[-1]] = copy.deepcopy(value)

    @staticmethod
    def delete_path(mapping: dict[str, Any], keys: tuple[str, ...]) -> None:
        selected = mapping
        for key in keys[:-1]:
            nested = selected.get(key)
            if not isinstance(nested, dict):
                raise AssertionError(f"fixture path is not a mapping: {keys}")
            selected = nested
        del selected[keys[-1]]

    def resolve_mutated_artifact(
        self,
        base: Path,
        name: str,
        mutate: Callable[[dict[str, Any]], None],
    ) -> dict[str, Any]:
        artifact = copy.deepcopy(self.v1_artifact)
        mutate(artifact)
        path, raw = self.write_json(base / name / "v1.json", artifact)
        digest = sha256_bytes(raw)
        with patch.object(resolver, "PRIOR_OPERATION_ARTIFACT_SHA256", digest):
            request = self.new_request()
            return self.resolve_current(
                request,
                prior_operation_artifact_path=path,
            )

    @staticmethod
    def checks(result: Mapping[str, Any]) -> list[dict[str, Any]]:
        checks = result.get(resolver.CHECKS_KEY)
        if not isinstance(checks, list) or not all(
            isinstance(item, dict) for item in checks
        ):
            raise AssertionError("successor check list is missing or malformed")
        return checks

    def assert_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        passed = sum(item.get("passed") is True for item in checks)
        failed = sum(item.get("passed") is False for item in checks)
        self.assertEqual(result.get("passed_check_count"), passed)
        self.assertEqual(result.get("failed_check_count"), failed)
        self.assertEqual(len(checks), passed + failed)
        for item in checks:
            self.assertEqual(
                set(item),
                {"check_id", "passed", "block_code", "failure_code", "expected"},
            )
            self.assertIs(type(item["passed"]), bool)
            if item["passed"]:
                self.assertIsNone(item["block_code"])
                self.assertIsNone(item["failure_code"])
            else:
                self.assertIn(item["block_code"], resolver.BLOCK_CODES)
                self.assertIn(item["failure_code"], resolver.BLOCK_CODES)

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(
            all(type(value) is bool and value is False for value in non_claims.values())
        )
        self.assertIs(result.get("result_level_non_claims_canonical_false"), True)

    def assert_blocked(self, result: Mapping[str, Any], code: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            result.get("successor_result"),
            resolver.SUCCESSOR_RESULT_NOT_EVALUATED,
        )
        self.assertEqual(result.get("completed_successor_result_posture_count"), 0)
        self.assertIsNone(result.get("admissible_future_route"))
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("code"), block.get("block_code"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        posture = result["successor_posture"]
        for field in (
            "successor_basis_supplied",
            "successor_basis_admitted",
            "contradiction_evaluated",
            "successor_correction_recorded",
            "successor_exhausted",
            "corrected_field_selected",
        ):
            self.assertIs(posture[field], False)
        self.assertEqual(posture["completed_successor_result_posture_count"], 0)
        self.assertIsNone(posture["admissible_future_route"])
        correction = result["correction_posture"]
        self.assertIsNone(correction["prior_no_partial_ledger_standing"])
        self.assertIsNone(correction["successor_no_partial_ledger_standing"])
        self.assertIs(correction["no_partial_ledger_standing_corrected"], False)
        self.assertIs(
            result[resolver.SUCCESSOR_KEY]["successor_no_partial_ledger_standing"],
            None,
        )
        self.assert_non_claims_false(result)
        self.assert_counts(result)

    def assert_recorded(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(
            result.get("successor_result"), resolver.SUCCESSOR_RESULT_RECORDED
        )
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assertEqual(result.get("completed_successor_result_posture_count"), 1)
        self.assertIsNone(result.get("admissible_future_route"))
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["reason"])
        posture = result["successor_posture"]
        for field in (
            "successor_basis_supplied",
            "successor_basis_admitted",
            "contradiction_evaluated",
            "successor_correction_recorded",
            "successor_exhausted",
            "corrected_field_selected",
            "no_second_semantic_change",
        ):
            self.assertIs(posture[field], True)
        self.assertEqual(posture["completed_successor_result_posture_count"], 1)
        self.assertIsNone(posture["admissible_future_route"])
        self.assert_non_claims_false(result)
        self.assert_counts(result)
        self.assertTrue(all(item["passed"] for item in self.checks(result)))

    def test_module_identity_constants_digests_and_public_api(self) -> None:
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2",
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(
            resolver.SUCCESSOR_ID,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001_v2",
        )
        self.assertEqual(
            resolver.SUCCESSOR_TYPE,
            "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_OPERATION_SUCCESSOR",
        )
        self.assertEqual(resolver.SUCCESSOR_VERSION, "0.2.0")
        self.assertEqual(
            resolver.SUCCESSOR_SCOPE,
            "RECORD_ONE_ADDITIVE_SUCCESSOR_CORRECTING_NO_PARTIAL_LEDGER_STANDING_ONLY",
        )
        self.assertEqual(
            resolver.PRIOR_OPERATION_ID,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001",
        )
        self.assertEqual(
            resolver.SELECTED_MATTER_CLASS,
            "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_REMAINING_TEN_INTEGRITY_CONDITIONS_ONLY",
        )
        self.assertEqual(
            str(resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH),
            "spec/BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_OPERATION_V0_MIN_SPEC.md",
        )
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION_SHA256,
            "3600cc9cf91c4938952b289119aeafbab53831e5e060d3d0e8abff357f4ba3dc",
        )
        self.assertEqual(
            str(resolver.PRIOR_OPERATION_ARTIFACT_RELATIVE_PATH),
            "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min/body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001__body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result.json",
        )
        self.assertEqual(
            resolver.PRIOR_OPERATION_ARTIFACT_SHA256,
            "18da6cf8f9250445d4708c7dce0ed8327d8d0577643f793f422a0281f9a6abef",
        )
        self.assertEqual(
            resolver.CANONICAL_OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001_v2__body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result.json",
        )
        self.assertEqual(
            resolver.CONTRADICTION_ID,
            "V1_NO_PARTIAL_LEDGER_STANDING_FALSE_WITH_COMPLETE_TEN_ROW_LEDGER",
        )
        self.assertEqual(
            resolver.CONTRADICTORY_FIELD_PATH,
            "operation_posture.no_partial_ledger_standing",
        )
        self.assertEqual(
            resolver.CORRECTION_REASON,
            "THE_COMPLETED_OPERATION_RECORDED_EXACTLY_TEN_ORDERED_ROWS_WITH_NO_PARTIAL_LEDGER_STANDING",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (resolver.OUTCOME_RECORDED, resolver.OUTCOME_BLOCKED),
        )
        self.assertEqual(
            resolver.SUCCESSOR_RESULT_FAMILY,
            (resolver.SUCCESSOR_RESULT_RECORDED, resolver.SUCCESSOR_RESULT_NOT_EVALUATED),
        )
        self.assertIsNone(resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(sha256_bytes(self.v1_bytes), resolver.PRIOR_OPERATION_ARTIFACT_SHA256)
        self.assertEqual(
            sha256_bytes(self.specification_bytes),
            resolver.GOVERNING_SPECIFICATION_SHA256,
        )
        for name in (
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request",
            "build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_from_path",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary",
            "write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

    def test_default_result_is_pure_deterministic_and_independent(self) -> None:
        with patch.object(
            resolver,
            "_read_bytes",
            side_effect=AssertionError("default performed a filesystem read"),
        ):
            first = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()
            second = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()
        self.assert_blocked(first, "NOT_EXECUTED")
        self.assertEqual(first["passed_check_count"], 0)
        self.assertEqual(first["failed_check_count"], 1)
        self.assertEqual(first, second)
        first["successor_posture"]["successor_basis_supplied"] = True
        self.assertIs(second["successor_posture"]["successor_basis_supplied"], False)
        third = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()
        self.assertEqual(second, third)

    def test_canonical_request_exact_schema_contracts_and_independence(self) -> None:
        first = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request()
        second = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_request()
        self.assertEqual(set(first), EXPECTED_REQUEST_KEYS)
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertEqual(first["intent"], resolver.INTENT_RECORD)
        self.assertEqual(first["successor_id"], resolver.SUCCESSOR_ID)
        self.assertEqual(first["successor_type"], resolver.SUCCESSOR_TYPE)
        self.assertEqual(first["successor_version"], resolver.SUCCESSOR_VERSION)
        self.assertEqual(first["successor_scope"], resolver.SUCCESSOR_SCOPE)
        self.assertEqual(
            first["one_field_difference_contract"],
            resolver.ONE_FIELD_DIFFERENCE_CONTRACT,
        )
        self.assertEqual(
            first["required_v1_standing_contract"],
            resolver.REQUIRED_V1_STANDING_CONTRACT,
        )
        self.assertEqual(
            first["unaffected_standing_preservation_contract"],
            resolver.UNAFFECTED_STANDING_PRESERVATION_CONTRACT,
        )
        self.assertEqual(first["declared_non_claims"], resolver._canonical_non_claims())
        first["one_field_difference_contract"]["successor_value"] = False
        self.assertIs(second["one_field_difference_contract"]["successor_value"], True)
        canonical_before = copy.deepcopy(self.canonical_request)
        declared = self.new_request(
            intent=resolver.INTENT_RECORD,
            declared_non_claims=resolver._canonical_non_claims(),
        )
        self.assertEqual(declared, canonical_before)
        self.assertEqual(self.canonical_request, canonical_before)

    def test_canonical_successor_records_exactly_one_correction(self) -> None:
        result = self.recorded_result
        self.assert_recorded(result)
        correction = result["correction_posture"]
        expected = {
            "contradiction_id": resolver.CONTRADICTION_ID,
            "contradictory_field_path": resolver.CONTRADICTORY_FIELD_PATH,
            "prior_no_partial_ledger_standing": False,
            "successor_no_partial_ledger_standing": True,
            "no_partial_ledger_standing_corrected": True,
            "prior_operation_result_preserved": True,
            "prior_operation_artifact_preserved": True,
            "prior_operation_artifact_overwritten": False,
            "prior_operation_posture_overwritten": False,
            "successor_is_additive": True,
            "correction_scope_stayed_one_field_only": True,
            "v1_operation_remains_recorded": True,
            "v1_operation_remains_exhausted": True,
            "v1_matrix_remains_complete": True,
        }
        self.assertEqual(correction, expected)
        difference = result["exact_one_field_difference"]
        self.assertEqual(set(difference), EXPECTED_ONE_FIELD_DIFFERENCE_KEYS)
        self.assertEqual(difference, resolver.ONE_FIELD_DIFFERENCE_CONTRACT)
        self.assertEqual(difference["field_path"], resolver.CONTRADICTORY_FIELD_PATH)
        self.assertIs(difference["prior_value"], False)
        self.assertIs(difference["successor_value"], True)
        self.assertEqual(difference["correction_reason"], resolver.CORRECTION_REASON)
        self.assertIs(difference["prior_value_preserved_as_historical"], True)
        self.assertIs(difference["successor_value_appended"], True)
        self.assertIs(result["non_claims"]["v1_operation_failed"], False)
        self.assertIs(result["non_claims"]["v1_operation_invalidated"], False)
        self.assertIs(result["non_claims"]["repair_performed"], False)

    def test_v1_identity_completion_admissibility_and_contradiction(self) -> None:
        artifact = self.v1_artifact
        self.assertEqual(artifact["resolver_module"], resolver.PRIOR_RESOLVER_MODULE)
        self.assertEqual(artifact["result_version"], resolver.PRIOR_RESULT_VERSION)
        self.assertEqual(artifact["outcome"], resolver.PRIOR_OUTCOME_RECORDED)
        self.assertEqual(artifact["operation_result"], resolver.PRIOR_OUTCOME_RECORDED)
        self.assertEqual(artifact["passed_check_count"], 182)
        self.assertEqual(artifact["failed_check_count"], 0)
        self.assertIs(artifact["block"]["blocked"], False)
        posture = artifact["operation_posture"]
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "evaluation_performed",
            "heterogeneous_condition_matrix_recorded",
            "operation_exhausted",
        ):
            self.assertIs(posture[field], True)
        self.assertEqual(posture["completed_operation_result_posture_count"], 1)
        self.assertEqual(artifact["completed_operation_result_posture_count"], 1)
        self.assertIsNone(artifact["admissible_future_route"])
        self.assertEqual(
            artifact["operation_admissibility_evaluations"],
            resolver.EXPECTED_OPERATION_ADMISSIBILITY,
        )
        validation = self.recorded_result["prior_v1_artifact_validation"]
        for field in (
            "artifact_validated",
            "identity_and_recorded_result_validated",
            "check_counts_validated",
            "completion_and_null_route_validated",
            "three_admissibility_evaluations_validated",
            "aggregate_matrix_validated",
            "ten_row_ledger_validated",
            "result_no_partial_ledger_check_validated",
            "contradictory_false_field_validated",
        ):
            self.assertIs(validation[field], True)
        self.assertIs(posture["no_partial_ledger_standing"], False)
        matching = [
            item
            for item in artifact[
                "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_checks"
            ]
            if item.get("check_id") == "result.no_partial_ledger"
        ]
        self.assertEqual(len(matching), 1)
        self.assertIs(matching[0]["passed"], True)
        self.assertIsNone(matching[0]["failure_code"])
        self.assertIsNone(matching[0]["block_code"])
        contradiction = self.recorded_result["contradiction_validation"]
        self.assertEqual(contradiction["contradiction_scope"], resolver.CONTRADICTION_SCOPE)
        self.assertIs(contradiction["contradiction_validated"], True)
        affect_fields = {
            key: value
            for key, value in contradiction.items()
            if key.startswith("contradiction_affects_")
        }
        self.assertTrue(affect_fields)
        self.assertTrue(all(value is False for value in affect_fields.values()))

    def test_complete_ten_row_matrix_is_exact_and_unchanged(self) -> None:
        ledger = self.v1_artifact["condition_ledger"]
        self.assertIsInstance(ledger, list)
        self.assertEqual(len(ledger), 10)
        self.assertEqual(
            [row["condition_id"] for row in ledger],
            list(resolver.ORDERED_TEN_CONDITION_MATTER),
        )
        self.assertEqual(len({row["condition_id"] for row in ledger}), 10)
        self.assertTrue(
            all(set(row) == set(resolver.CONDITION_LEDGER_SCHEMA_FIELDS) for row in ledger)
        )
        self.assertTrue(
            all(tuple(row) == resolver.SERIALIZED_LEDGER_SCHEMA_FIELDS for row in ledger)
        )
        self.assertEqual(
            self.v1_artifact["condition_ledger_schema_contract"][
                "required_fields_in_order"
            ],
            list(resolver.CONDITION_LEDGER_SCHEMA_FIELDS),
        )
        self.assertTrue(all(row["prior_posture_preserved"] is True for row in ledger))
        self.assertTrue(all(row["no_overwrite"] is True for row in ledger))
        self.assertEqual(
            self.v1_artifact["aggregate_matrix_posture"],
            resolver.EXPECTED_AGGREGATE_MATRIX_POSTURE,
        )
        self.assertEqual(
            self.v1_artifact["condition_evaluations"],
            resolver.EXPECTED_CONDITION_EVALUATIONS,
        )
        supported = [
            row
            for row in ledger
            if row["evaluation_posture"]
            == "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS"
        ]
        requires = [
            row for row in ledger if row["evaluation_posture"] == "REQUIRES_BASIS"
        ]
        self.assertEqual(len(supported), 9)
        self.assertEqual(len(requires), 1)
        self.assertEqual(requires[0]["condition_id"], "forged_receiver_attestation")
        self.assertEqual(
            requires[0]["required_basis_class"], "EXTERNAL_AUTHENTICITY_BASIS"
        )

    def test_unaffected_standing_digests_and_compact_omission(self) -> None:
        preservation = self.recorded_result["unaffected_standing_preservation"]
        self.assertEqual(
            preservation["section_sha256"], resolver.UNAFFECTED_SECTION_SHA256
        )
        self.assertEqual(
            preservation["observed_section_sha256"],
            resolver.UNAFFECTED_SECTION_SHA256,
        )
        for section, expected in resolver.UNAFFECTED_SECTION_SHA256.items():
            with self.subTest(section=section):
                self.assertEqual(canonical_value_digest(self.v1_artifact[section]), expected)
        projected = copy.deepcopy(self.v1_artifact["operation_posture"])
        del projected["no_partial_ledger_standing"]
        self.assertEqual(
            canonical_value_digest(projected),
            resolver.OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256,
        )
        self.assertEqual(
            preservation["observed_operation_posture_except_contradiction_sha256"],
            resolver.OPERATION_POSTURE_EXCEPT_CONTRADICTION_SHA256,
        )
        self.assertIs(preservation["all_unaffected_sections_exactly_equivalent"], True)
        for key in (
            "condition_ledger",
            "aggregate_matrix_posture",
            "condition_evaluations",
        ):
            self.assertNotIn(key, self.recorded_result)
        self.assertIs(preservation["complete_v1_body_omitted"], True)
        self.assertIs(preservation["full_ledger_omitted"], True)
        self.assertFalse(resolver._contains_complete_v1_material(self.recorded_result))
        self.assertEqual(
            self.v1_artifact["raw_signal_posture"], resolver.EXPECTED_RAW_SIGNAL_POSTURE
        )
        self.assertIsNone(self.v1_artifact["admissible_future_route"])
        self.assertEqual(
            self.recorded_result["blocked_conversions"],
            list(resolver.BLOCKED_CONVERSIONS),
        )

    def test_artifact_strict_json_and_digest_failures_block_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            cases = (
                (
                    "wrong_digest",
                    self.v1_bytes + b" ",
                    "V1_ARTIFACT_DIGEST_MISMATCH",
                ),
                ("malformed", b'{"resolver_module":', "V1_ARTIFACT_JSON_INVALID"),
                (
                    "duplicate",
                    b'{"resolver_module":"a","resolver_module":"b"}\n',
                    "V1_ARTIFACT_JSON_INVALID",
                ),
                ("array", b"[]\n", "V1_ARTIFACT_JSON_INVALID"),
                ("nonfinite", b'{"value":NaN}\n', "V1_ARTIFACT_JSON_INVALID"),
            )
            for name, raw, code in cases:
                path = self.write_bytes(base / name / "v1.json", raw)
                result = self.resolve_current(prior_operation_artifact_path=path)
                with self.subTest(name=name):
                    self.assert_blocked(result, code)
            missing = base / "missing" / "v1.json"
            self.assert_blocked(
                self.resolve_current(prior_operation_artifact_path=missing),
                "V1_ARTIFACT_MISSING_OR_UNREADABLE",
            )

    def test_v1_identity_completion_and_route_mutations_block(self) -> None:
        cases: tuple[
            tuple[str, tuple[str, ...], Any], ...
        ] = (
            ("resolver", ("resolver_module",), "WRONG"),
            ("version", ("result_version",), "9.9.9"),
            ("outcome", ("outcome",), "WRONG"),
            ("operation_result", ("operation_result",), "WRONG"),
            ("passed_count", ("passed_check_count",), 181),
            ("failed_count", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("basis_supplied", ("operation_posture", "operation_basis_supplied"), False),
            ("basis_admitted", ("operation_posture", "operation_basis_admitted"), False),
            ("evaluation", ("operation_posture", "evaluation_performed"), False),
            ("matrix", ("operation_posture", "heterogeneous_condition_matrix_recorded"), False),
            ("exhausted", ("operation_posture", "operation_exhausted"), False),
            (
                "posture_count",
                ("operation_posture", "completed_operation_result_posture_count"),
                0,
            ),
            ("top_count", ("completed_operation_result_posture_count",), 0),
            ("route", ("admissible_future_route",), "WRONG"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, keys, value in cases:
                def mutate(
                    artifact: dict[str, Any],
                    selected_keys: tuple[str, ...] = keys,
                    selected_value: Any = value,
                ) -> None:
                    self.set_path(artifact, selected_keys, selected_value)

                with self.subTest(name=name):
                    self.assert_blocked(
                        self.resolve_mutated_artifact(base, name, mutate)
                    )

    def test_aggregate_ledger_and_row_mutations_block(self) -> None:
        mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []

        def add(name: str, mutation: Callable[[dict[str, Any]], None]) -> None:
            mutations.append((name, mutation))

        add(
            "aggregate_count",
            lambda value: value["aggregate_matrix_posture"].__setitem__(
                "ordered_condition_count", 9
            ),
        )
        add("ledger_nine", lambda value: value["condition_ledger"].pop())
        add(
            "ledger_eleven",
            lambda value: value["condition_ledger"].append(
                copy.deepcopy(value["condition_ledger"][-1])
            ),
        )
        add("missing_row", lambda value: value["condition_ledger"].pop(0))
        add(
            "duplicate_row",
            lambda value: value["condition_ledger"].__setitem__(
                1, copy.deepcopy(value["condition_ledger"][0])
            ),
        )
        add(
            "unknown_condition",
            lambda value: value["condition_ledger"][0].__setitem__(
                "condition_id", "unknown_condition"
            ),
        )

        def reorder(value: dict[str, Any]) -> None:
            value["condition_ledger"][0], value["condition_ledger"][1] = (
                value["condition_ledger"][1],
                value["condition_ledger"][0],
            )

        add("reordered", reorder)
        add(
            "missing_field",
            lambda value: value["condition_ledger"][0].pop("limitation"),
        )
        add(
            "extra_field",
            lambda value: value["condition_ledger"][0].__setitem__("extra", False),
        )
        add(
            "malformed_row",
            lambda value: value["condition_ledger"].__setitem__(0, []),
        )
        add(
            "prior_not_preserved",
            lambda value: value["condition_ledger"][0].__setitem__(
                "prior_posture_preserved", False
            ),
        )
        add(
            "overwrite",
            lambda value: value["condition_ledger"][0].__setitem__(
                "no_overwrite", False
            ),
        )
        add(
            "forgery_supported",
            lambda value: value["condition_ledger"][8].__setitem__(
                "evaluation_posture", "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS"
            ),
        )
        add(
            "forgery_basis",
            lambda value: value["condition_ledger"][8].__setitem__(
                "required_basis_class", "NONE"
            ),
        )

        def second_requires(value: dict[str, Any]) -> None:
            value["condition_ledger"][0]["evaluation_posture"] = "REQUIRES_BASIS"
            value["condition_ledger"][0][
                "required_basis_class"
            ] = "EXTERNAL_AUTHENTICITY_BASIS"

        add("second_requires_basis", second_requires)
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, mutate in mutations:
                with self.subTest(name=name):
                    self.assert_blocked(
                        self.resolve_mutated_artifact(base, name, mutate)
                    )

    def test_exact_check_contradiction_and_unaffected_mutations_block(self) -> None:
        checks_key = (
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_checks"
        )

        def remove_check(value: dict[str, Any]) -> None:
            value[checks_key] = [
                item
                for item in value[checks_key]
                if item.get("check_id") != "result.no_partial_ledger"
            ]

        def duplicate_check(value: dict[str, Any]) -> None:
            selected = next(
                item
                for item in value[checks_key]
                if item.get("check_id") == "result.no_partial_ledger"
            )
            value[checks_key].append(copy.deepcopy(selected))

        def fail_check(value: dict[str, Any]) -> None:
            selected = next(
                item
                for item in value[checks_key]
                if item.get("check_id") == "result.no_partial_ledger"
            )
            selected["passed"] = False
            selected["failure_code"] = "WRONG"
            selected["block_code"] = "WRONG"

        def missing_contradiction(value: dict[str, Any]) -> None:
            del value["operation_posture"]["no_partial_ledger_standing"]

        def malformed_contradiction(value: dict[str, Any]) -> None:
            value["operation_posture"]["no_partial_ledger_standing"] = "false"

        def already_true(value: dict[str, Any]) -> None:
            value["operation_posture"]["no_partial_ledger_standing"] = True

        def changed_temporal(value: dict[str, Any]) -> None:
            value["temporal_evidence_posture"]["knock_to_receiver_attestation_interval_seconds"] += 1

        def changed_other_posture(value: dict[str, Any]) -> None:
            value["operation_posture"]["no_overwrite"] = False

        cases = (
            ("missing_check", remove_check, "V1_NO_PARTIAL_LEDGER_CHECK_INVALID"),
            ("duplicate_check", duplicate_check, "V1_NO_PARTIAL_LEDGER_CHECK_INVALID"),
            ("failed_check", fail_check, "V1_NO_PARTIAL_LEDGER_CHECK_INVALID"),
            ("missing_contradiction", missing_contradiction, "V1_CONTRADICTORY_FIELD_INVALID"),
            ("malformed_contradiction", malformed_contradiction, "V1_CONTRADICTORY_FIELD_INVALID"),
            ("already_true", already_true, "NO_CORRECTION_MATTER_REMAINS"),
            ("unaffected_section", changed_temporal, "V1_UNAFFECTED_STANDING_CHANGED"),
            ("other_posture", changed_other_posture, "V1_UNAFFECTED_STANDING_CHANGED"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, mutate, code in cases:
                result = self.resolve_mutated_artifact(base, name, mutate)
                with self.subTest(name=name):
                    self.assert_blocked(result, code)

    def test_request_mutations_and_all_true_nonclaims_block_before_reads(self) -> None:
        mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []

        def change(field: str, value: Any) -> Callable[[dict[str, Any]], None]:
            return lambda request: request.__setitem__(field, copy.deepcopy(value))

        mutations.extend(
            (
                ("unknown", change("unknown_field", True)),
                ("intent", change("intent", "WRONG")),
                ("successor_id", change("successor_id", "WRONG")),
                ("successor_type", change("successor_type", "WRONG")),
                ("successor_version", change("successor_version", "9.9.9")),
                ("successor_scope", change("successor_scope", "WRONG")),
                ("spec_path", change("governing_specification_path", "wrong.md")),
                ("spec_digest", change("governing_specification_sha256", "0" * 64)),
                ("v1_path", change("prior_operation_artifact_path", "wrong.json")),
                ("v1_digest", change("prior_operation_artifact_sha256", "0" * 64)),
                ("contradiction", change("contradiction_id", "WRONG")),
                ("field_path", change("contradictory_field_path", "wrong.field")),
                ("prior_value", change("prior_field_value", True)),
                ("successor_value", change("successor_field_value", False)),
                ("reason", change("correction_reason", "WRONG")),
                ("second_difference", change("second_correction", {"field": "x"})),
                ("full_v1", change("complete_v1_result", self.v1_artifact)),
                ("ledger", change("condition_ledger", [])),
                ("aggregate", change("aggregate_matrix_posture", {})),
                ("condition_selection", change("condition_result_selection", {})),
                ("evidence", change("evidence_change", {})),
                ("payload", change("semantic_payload", {})),
                ("downstream", change("downstream_standing", True)),
                ("future_route", change("future_route", "WRONG")),
            )
        )

        def missing(request: dict[str, Any]) -> None:
            del request["intent"]

        mutations.insert(0, ("missing", missing))
        for name, mutate in mutations:
            request = copy.deepcopy(self.canonical_request)
            mutate(request)
            before = copy.deepcopy(request)
            with self.subTest(name=name), patch.object(
                resolver,
                "_read_bytes",
                side_effect=AssertionError("invalid request reached governed reads"),
            ):
                result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
                    request
                )
                self.assert_blocked(result)
            self.assertEqual(request, before)

        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            request = copy.deepcopy(self.canonical_request)
            request["declared_non_claims"][field] = True
            before = copy.deepcopy(request)
            with self.subTest(nonclaim=field), patch.object(
                resolver,
                "_read_bytes",
                side_effect=AssertionError("flipped non-claim reached governed reads"),
            ):
                result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2(
                    request
                )
                self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")
            self.assertEqual(request, before)

    def test_from_path_strict_behavior_and_direct_equivalence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            valid_path, _ = self.write_json(base / "valid" / "request.json", self.canonical_request)
            result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_from_path(
                valid_path,
                governing_specification_path=SPECIFICATION_PATH,
                prior_operation_artifact_path=V1_ARTIFACT_PATH,
            )
            self.assertEqual(result, self.recorded_result)
            cases = (
                ("malformed", b'{"intent":', "REQUEST_JSON_INVALID"),
                ("duplicate", b'{"intent":"a","intent":"b"}\n', "REQUEST_JSON_INVALID"),
                ("array", b"[]\n", "REQUEST_JSON_INVALID"),
                ("nonfinite", b'{"value":Infinity}\n', "REQUEST_JSON_INVALID"),
                ("schema", b'{"intent":"WRONG"}\n', "REQUEST_FIELD_MISSING"),
            )
            for name, raw, code in cases:
                path = self.write_bytes(base / name / "request.json", raw)
                value = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_from_path(
                    path,
                    governing_specification_path=SPECIFICATION_PATH,
                    prior_operation_artifact_path=V1_ARTIFACT_PATH,
                )
                with self.subTest(name=name):
                    self.assert_blocked(value, code)
            self.assert_blocked(
                resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_from_path(
                    base / "missing" / "request.json"
                ),
                "REQUEST_JSON_INVALID",
            )

    def test_summary_projection_is_compact_deterministic_and_strict(self) -> None:
        before = copy.deepcopy(self.recorded_result)
        first = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
            self.recorded_result
        )
        second = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
            self.recorded_result
        )
        self.assertEqual(first, second)
        self.assertEqual(first, self.recorded_result[resolver.SUMMARY_KEY])
        self.assertEqual(first["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(first["successor_result"], resolver.SUCCESSOR_RESULT_RECORDED)
        self.assertEqual(first["successor_id"], resolver.SUCCESSOR_ID)
        self.assertEqual(first["successor_type"], resolver.SUCCESSOR_TYPE)
        self.assertEqual(first["successor_version"], resolver.SUCCESSOR_VERSION)
        self.assertEqual(first["successor_scope"], resolver.SUCCESSOR_SCOPE)
        self.assertEqual(first["contradiction_id"], resolver.CONTRADICTION_ID)
        self.assertEqual(first["contradictory_field_path"], resolver.CONTRADICTORY_FIELD_PATH)
        self.assertIs(first["prior_no_partial_ledger_standing"], False)
        self.assertIs(first["successor_no_partial_ledger_standing"], True)
        self.assertIs(first["successor_correction_recorded"], True)
        self.assertIs(first["v1_operation_remains_recorded"], True)
        self.assertIs(first["v1_matrix_remains_complete"], True)
        self.assertEqual(first["passed_check_count"], self.recorded_result["passed_check_count"])
        self.assertEqual(first["failed_check_count"], 0)
        self.assertIs(first["result_level_non_claims_canonical_false"], True)
        self.assertIsNone(first["admissible_future_route"])
        self.assertIs(first["open_is_not_next"], True)
        self.assertEqual(self.recorded_result, before)
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error
        candidates: list[object] = [{}, {"outcome": resolver.OUTCOME_RECORDED}]
        blocked_as_recorded = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()
        blocked_as_recorded["outcome"] = resolver.OUTCOME_RECORDED
        candidates.append(blocked_as_recorded)
        altered = copy.deepcopy(self.recorded_result)
        altered["correction_posture"]["successor_no_partial_ledger_standing"] = False
        candidates.append(altered)
        incomplete = copy.deepcopy(self.recorded_result)
        del incomplete["correction_posture"]
        candidates.append(incomplete)
        for candidate in candidates:
            with self.subTest(candidate_type=type(candidate).__name__), self.assertRaises(error):
                resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
                    candidate  # type: ignore[arg-type]
                )

    def test_writer_accepts_only_canonical_completed_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            output_root = base / resolver.CANONICAL_OUTPUT_ROOT.name
            target = output_root / resolver.OUTPUT_FILENAME
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result(
                    self.recorded_result
                )
            self.assertEqual(written, target)
            self.assertTrue(target.is_file())
            raw = target.read_bytes()
            self.assertTrue(raw.endswith(b"\n"))
            self.assertNotIn(b"NaN", raw)
            self.assertEqual(strict_json_bytes(raw), self.recorded_result)
            self.assertEqual(
                [path for path in output_root.rglob("*") if path.is_file()],
                [target],
            )
            self.assertEqual(
                [path for path in base.iterdir() if path.is_dir()],
                [output_root],
            )

    def test_writer_refuses_overwrite_paths_and_semantic_tampering(self) -> None:
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinV2Error
        default = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_default_result()
        invalid_request = copy.deepcopy(self.canonical_request)
        invalid_request["intent"] = "WRONG"
        blocked = self.resolve_current(invalid_request)
        candidates: list[tuple[str, object]] = [
            ("default", default),
            ("blocked", blocked),
            ("malformed", {"outcome": resolver.OUTCOME_RECORDED}),
        ]
        mutations = (
            ("not_evaluated", ("successor_result",), "NOT_EVALUATED"),
            ("route", ("admissible_future_route",), "WRONG"),
            (
                "correction",
                ("correction_posture", "successor_no_partial_ledger_standing"),
                False,
            ),
            (
                "difference",
                ("exact_one_field_difference", "successor_value"),
                False,
            ),
            (
                "true_nonclaim",
                ("non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0]),
                True,
            ),
        )
        for name, keys, value in mutations:
            candidate = copy.deepcopy(self.recorded_result)
            self.set_path(candidate, keys, value)
            candidates.append((name, candidate))
        failed = copy.deepcopy(self.recorded_result)
        failed[resolver.CHECKS_KEY][0]["passed"] = False
        candidates.append(("failed_check", failed))
        complete = copy.deepcopy(self.recorded_result)
        complete["correction_posture"]["condition_ledger"] = copy.deepcopy(
            self.v1_artifact["condition_ledger"]
        )
        candidates.append(("complete_v1_material", complete))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            output_root = base / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for name, candidate in candidates:
                    with self.subTest(name=name), self.assertRaises(error):
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result(
                            candidate  # type: ignore[arg-type]
                        )
                for path in (
                    output_root / "alternate.json",
                    base / "outside" / resolver.OUTPUT_FILENAME,
                    output_root / ".." / "escape.json",
                ):
                    with self.subTest(path=path), self.assertRaises(error):
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result(
                            self.recorded_result,
                            path,
                        )
                canonical = output_root / resolver.OUTPUT_FILENAME
                canonical.parent.mkdir(parents=True)
                original = b"ORIGINAL\n"
                canonical.write_bytes(original)
                with self.assertRaises(error):
                    resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_result(
                        self.recorded_result
                    )
                self.assertEqual(canonical.read_bytes(), original)
                self.assertEqual(
                    [path for path in output_root.rglob("*") if path.is_file()],
                    [canonical],
                )

    def test_static_safety_no_discovery_network_archive_clock_or_v1_import(self) -> None:
        source = self.resolver_bytes.decode("utf-8", errors="strict")
        tree = ast.parse(source)
        forbidden_imports = {
            "os",
            "subprocess",
            "random",
            "secrets",
            "socket",
            "urllib",
            "requests",
            "http",
            "zipfile",
            "tarfile",
            "glob",
            "datetime",
            "time",
        }
        imported: set[str] = set()
        calls: list[tuple[str, str]] = []
        imported_modules: list[str] = []
        path_assignments: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported.add(alias.name.split(".")[0])
                    imported_modules.append(alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
                imported_modules.append(node.module)
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.append((node.func.id, ""))
                elif isinstance(node.func, ast.Attribute):
                    calls.append((node.func.attr, ast.unparse(node.func.value)))
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if isinstance(target, ast.Name) and target.id.endswith("PATH"):
                        path_assignments.add(target.id)
        self.assertTrue(imported.isdisjoint(forbidden_imports))
        self.assertFalse(
            any(
                "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min"
                == module
                for module in imported_modules
            )
        )
        forbidden_calls = {
            "glob",
            "rglob",
            "walk",
            "listdir",
            "scandir",
            "iterdir",
            "now",
            "utcnow",
            "today",
            "time",
            "getenv",
            "extract",
            "extractall",
            "check_output",
            "run",
            "Popen",
            "system",
        }
        self.assertTrue({name for name, _ in calls}.isdisjoint(forbidden_calls))
        open_calls = [owner for name, owner in calls if name == "open"]
        self.assertEqual(open_calls, ["target"])
        self.assertTrue(
            all("RAW_SIGNAL" not in name and "ZIP" not in name for name in path_assignments)
        )
        self.assertNotIn("os.environ", source)
        self.assertNotIn("subprocess", source)

    def test_determinism_input_and_governed_surfaces_preserved(self) -> None:
        request = copy.deepcopy(self.canonical_request)
        before = copy.deepcopy(request)
        first = self.resolve_current(request)
        second = self.resolve_current(request)
        self.assertEqual(first, second)
        self.assertEqual(request, before)
        self.assertEqual(
            resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
                first
            ),
            resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_v2_summary(
                second
            ),
        )
        self.assertEqual(SPECIFICATION_PATH.read_bytes(), self.specification_bytes)
        self.assertEqual(V1_ARTIFACT_PATH.read_bytes(), self.v1_bytes)
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())


if __name__ == "__main__":
    unittest.main()
