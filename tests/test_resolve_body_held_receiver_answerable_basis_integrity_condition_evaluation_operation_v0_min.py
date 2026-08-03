"""Tests for one body-held ten-condition integrity evaluation operation.

The suite consumes only the resolver's frozen admitted basis.  It verifies one
ordered heterogeneous ledger with nine supported rows and one row requiring an
external-authenticity basis.  Hostile inputs and writer exercises remain in
temporary directories; raw signal and archive bytes are never opened.
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
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min as resolver


SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
BOUNDARY_SPECIFICATION_PATH = REPO_ROOT / resolver.BOUNDARY_SPECIFICATION_RELATIVE_PATH
BOUNDARY_ARTIFACT_PATH = REPO_ROOT / resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH
BOUNDARY_TERMINAL_SUMMARY_PATH = REPO_ROOT / resolver.BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH
PRIOR_STANDING_PATHS = tuple(REPO_ROOT / path for path in resolver.PRIOR_STANDING_RELATIVE_PATHS)
CARRIAGE_PATHS = tuple(REPO_ROOT / path for path in resolver.CARRIAGE_LINEAGE_RELATIVE_PATHS)
PACKET_TEXT_PATHS = tuple(REPO_ROOT / path for path in resolver.PACKET_TEXT_RELATIVE_PATHS)
CONDUCT_PATHS = tuple(REPO_ROOT / path for path in resolver.SOURCE_BODY_CONDUCT_RELATIVE_PATHS)
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

OPERATION_KEY = resolver.OPERATION_KEY
CHECKS_KEY = resolver.CHECKS_KEY
SUMMARY_KEY = resolver.SUMMARY_KEY
NON_MEANING_KEY = resolver.NON_MEANING_KEY

EXPECTED_REQUEST_KEYS = {
    "intent",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_type",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_version",
    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_scope",
    "governing_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_specification_path",
    "governing_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_specification_sha256",
    "completed_boundary_specification_path",
    "completed_boundary_specification_sha256",
    "completed_boundary_artifact_path",
    "completed_boundary_artifact_sha256",
    "boundary_terminal_summary_path",
    "boundary_terminal_summary_sha256",
    "consumed_boundary_route",
    "prior_standing_paths",
    "prior_standing_sha256",
    "carriage_lineage_paths",
    "carriage_lineage_sha256",
    "receiver_packet_text_paths",
    "receiver_packet_text_sha256",
    "receiver_packet_text_byte_counts",
    "source_body_conduct_paths",
    "source_body_conduct_sha256",
    "selected_matter_class",
    "ordered_ten_condition_matter",
    "required_condition_values",
    "evidence_class_family",
    "evidence_class_condition_mapping",
    "condition_evaluation_family",
    "required_basis_class_family",
    "operation_result_family",
    "condition_ledger_field_order",
    "dependency_ceiling_contract",
    "frozen_read_contract",
    "excluded_read_contract",
    "raw_signal_posture",
    "temporal_evidence",
    "expected_condition_ledger",
    "expected_aggregate_matrix_posture",
    "declared_non_claims",
}

EXPECTED_TOP_LEVEL_SECTIONS = {
    "resolver_module",
    "result_version",
    "outcome",
    "operation_result",
    "failed_check_count",
    "passed_check_count",
    "completed_operation_result_posture_count",
    "admissible_future_route",
    "block",
    resolver.METADATA_KEY,
    resolver.DECLARED_REQUEST_KEY,
    "canonical_request_validation",
    "specification_validation",
    "boundary_specification_validation",
    "boundary_artifact_validation",
    "boundary_terminal_summary_validation",
    "prior_standing_validations",
    "carriage_lineage_validations",
    "receiver_packet_text_validations",
    "source_body_conduct_validations",
    "frozen_read_contract_posture",
    "excluded_read_posture",
    "raw_signal_posture",
    "temporal_evidence_posture",
    "exact_matter_and_family_posture",
    "condition_ledger_schema_contract",
    "dependency_ceiling_contract",
    "condition_evaluations",
    "condition_ledger",
    "aggregate_matrix_posture",
    "operation_admissibility_evaluations",
    "operation_posture",
    OPERATION_KEY,
    "lineage_preservation_posture",
    "omission_posture",
    "non_claims",
    "result_level_non_claims_canonical_false",
    NON_MEANING_KEY,
    "blocked_conversions",
    resolver.STATEMENT_KEY,
    CHECKS_KEY,
    "what_remains_open",
    SUMMARY_KEY,
}

PROHIBITED_COMPLETE_KEYS = {
    "complete_upstream_artifact",
    "complete_upstream_artifact_body",
    "complete_candidate_body",
    "complete_candidate_evaluation_body",
    "raw_accelerometer_body",
    "raw_signal_body",
    "raw_signal_content",
    "original_zip_bytes",
    "archive_bytes",
    "filesystem_permissions",
    "acl_data",
    "device_control_data",
    "private_communications",
    "semantic_payload",
    "sufficiency_basis_records",
}


class DuplicateJsonKeyError(ValueError):
    """Raised by the suite's independent strict JSON loader."""


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


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


class BodyHeldIntegrityConditionEvaluationOperationTests(unittest.TestCase):
    """Verify one bounded heterogeneous ten-condition operation."""

    @classmethod
    def setUpClass(cls) -> None:
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("canonical operation output root must be absent")
        cls.governed_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            BOUNDARY_SPECIFICATION_PATH,
            BOUNDARY_ARTIFACT_PATH,
            BOUNDARY_TERMINAL_SUMMARY_PATH,
            *PRIOR_STANDING_PATHS,
            *CARRIAGE_PATHS,
            *PACKET_TEXT_PATHS,
            *CONDUCT_PATHS,
        )
        cls.unique_governed_paths = tuple(dict.fromkeys(cls.governed_paths))
        for path in cls.unique_governed_paths:
            if not path.is_file():
                raise AssertionError(f"required governed input missing: {path}")
        cls.governed_hashes = {
            path: sha256_path(path) for path in cls.unique_governed_paths
        }
        cls.specification_bytes = SPECIFICATION_PATH.read_bytes()
        cls.boundary_specification_bytes = BOUNDARY_SPECIFICATION_PATH.read_bytes()
        cls.boundary_artifact_bytes = BOUNDARY_ARTIFACT_PATH.read_bytes()
        cls.boundary_terminal_summary_bytes = BOUNDARY_TERMINAL_SUMMARY_PATH.read_bytes()
        cls.prior_standing_bytes = tuple(path.read_bytes() for path in PRIOR_STANDING_PATHS)
        cls.carriage_bytes = tuple(path.read_bytes() for path in CARRIAGE_PATHS)
        cls.packet_bytes = tuple(path.read_bytes() for path in PACKET_TEXT_PATHS)
        cls.conduct_bytes = tuple(path.read_bytes() for path in CONDUCT_PATHS)
        cls.boundary_artifact = strict_json_bytes(cls.boundary_artifact_bytes)
        cls.prior_standing = tuple(strict_json_bytes(raw) for raw in cls.prior_standing_bytes[:3])
        cls.carriage_artifacts = tuple(strict_json_bytes(raw) for raw in cls.carriage_bytes)
        cls.conduct_artifacts = {
            index: strict_json_bytes(cls.conduct_bytes[index])
            for index in (2, 5, 8)
        }
        cls.canonical_request = cls.new_request()
        cls.recorded_result = cls.resolve_current(cls.canonical_request)
        if cls.recorded_result.get("outcome") != resolver.OUTCOME_RECORDED:
            raise AssertionError("canonical execution did not reach RECORDED")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.governed_hashes.items():
            if not path.is_file() or sha256_path(path) != expected:
                raise AssertionError(f"governed input changed: {path}")
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("suite created the canonical operation output root")

    @staticmethod
    def new_request(**overrides: Any) -> dict[str, Any]:
        return resolver.build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request(
            **copy.deepcopy(overrides)
        )

    @staticmethod
    def canonical_paths() -> dict[str, Any]:
        return {
            "governing_specification_path": SPECIFICATION_PATH,
            "boundary_specification_path": BOUNDARY_SPECIFICATION_PATH,
            "boundary_artifact_path": BOUNDARY_ARTIFACT_PATH,
            "boundary_terminal_summary_path": BOUNDARY_TERMINAL_SUMMARY_PATH,
            "prior_presence_artifact_path": PRIOR_STANDING_PATHS[0],
            "source_admissibility_boundary_artifact_path": PRIOR_STANDING_PATHS[1],
            "later_modal_artifact_path": PRIOR_STANDING_PATHS[2],
            "modal_terminal_summary_path": PRIOR_STANDING_PATHS[3],
            "carriage_lineage_paths": tuple(CARRIAGE_PATHS),
            "receiver_packet_text_paths": tuple(PACKET_TEXT_PATHS),
            "source_body_conduct_paths": tuple(CONDUCT_PATHS),
        }

    @classmethod
    def resolve_current(
        cls,
        request: object | None = None,
        **path_overrides: Any,
    ) -> dict[str, Any]:
        supplied = cls.new_request() if request is None else copy.deepcopy(request)
        before = copy.deepcopy(supplied)
        paths = cls.canonical_paths()
        paths.update(path_overrides)
        result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min(
            supplied,
            **paths,
        )
        if supplied != before:
            raise AssertionError("resolver mutated the request")
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
    def duplicate_top_level_key(raw: bytes) -> bytes:
        text = raw.decode("utf-8", errors="strict")
        if not text.lstrip().startswith("{"):
            raise AssertionError("duplicate-key fixture source is not an object")
        offset = text.index("{") + 1
        return (
            text[:offset]
            + '\n  "resolver_module": "DUPLICATE_FIXTURE_VALUE",'
            + text[offset:]
        ).encode("utf-8")

    @staticmethod
    def checks(result: Mapping[str, Any]) -> list[dict[str, Any]]:
        value = result.get(CHECKS_KEY)
        if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
            raise AssertionError("check list missing or malformed")
        return value

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
        self.assertEqual(result.get("operation_result"), resolver.OPERATION_RESULT_NOT_EVALUATED)
        self.assertEqual(result.get("completed_operation_result_posture_count"), 0)
        self.assertIsNone(result.get("admissible_future_route"))
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("code"), block.get("block_code"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        posture = result["operation_posture"]
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "evaluation_performed",
            "heterogeneous_condition_matrix_recorded",
            "operation_exhausted",
        ):
            self.assertIs(posture[field], False)
        self.assertEqual(
            result["condition_evaluations"],
            {condition: resolver.CONDITION_NOT_EVALUATED for condition in resolver.REQUIRED_CONDITIONS},
        )
        self.assertEqual(result["condition_ledger"], [])
        self.assertIs(result["aggregate_matrix_posture"]["condition_ledger_populated"], False)
        self.assertEqual(result["aggregate_matrix_posture"]["condition_result_count"], 0)
        self.assertTrue(
            all(
                value == resolver.ADMISSIBILITY_NOT_EVALUATED
                for value in result["operation_admissibility_evaluations"].values()
            )
        )
        self.assert_non_claims_false(result)
        self.assert_counts(result)

    def assert_recorded(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_RECORDED)
        self.assertEqual(result.get("operation_result"), resolver.OPERATION_RESULT_RECORDED)
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assertEqual(result.get("completed_operation_result_posture_count"), 1)
        self.assertIsNone(result.get("admissible_future_route"))
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(result["block"]["code"])
        posture = result["operation_posture"]
        for field in (
            "operation_basis_supplied",
            "operation_basis_admitted",
            "evaluation_performed",
            "heterogeneous_condition_matrix_recorded",
            "operation_exhausted",
        ):
            self.assertIs(posture[field], True)
        self.assertEqual(len(result["condition_ledger"]), 10)
        self.assertTrue(
            all(
                value == resolver.ADMISSIBILITY_PASSED
                for value in result["operation_admissibility_evaluations"].values()
            )
        )
        self.assert_non_claims_false(result)
        self.assert_counts(result)

    def assert_no_prohibited_material(self, result: Mapping[str, Any]) -> None:
        def visit(value: Any) -> None:
            if isinstance(value, Mapping):
                self.assertTrue(PROHIBITED_COMPLETE_KEYS.isdisjoint(value))
                for item in value.values():
                    visit(item)
            elif isinstance(value, Sequence) and not isinstance(
                value, (str, bytes, bytearray)
            ):
                for item in value:
                    visit(item)

        visit(result)
        self.assertFalse(resolver._contains_prohibited_complete_material(result))

    def resolve_mutated_json(
        self,
        *,
        base: Path,
        fixture_name: str,
        artifact: dict[str, Any],
        path_slot: str,
        digest_attribute: str,
        sequence_index: int | None = None,
        digest_sequence_index: int | None = None,
    ) -> dict[str, Any]:
        path, raw = self.write_json(base / fixture_name, artifact)
        paths = self.canonical_paths()
        if sequence_index is None:
            paths[path_slot] = path
        else:
            values = list(paths[path_slot])
            values[sequence_index] = path
            paths[path_slot] = tuple(values)
        digest = sha256_bytes(raw)
        current = getattr(resolver, digest_attribute)
        replacement: Any = digest
        if digest_sequence_index is not None:
            replacement = list(current)
            replacement[digest_sequence_index] = digest
            replacement = tuple(replacement)
        with patch.object(resolver, digest_attribute, replacement):
            request = self.new_request()
            return self.resolve_current(request, **paths)

    def resolve_mutated_text(
        self,
        *,
        base: Path,
        fixture_name: str,
        raw: bytes,
        path_slot: str,
        digest_attribute: str,
        sequence_index: int | None = None,
        digest_sequence_index: int | None = None,
    ) -> dict[str, Any]:
        path = self.write_bytes(base / fixture_name, raw)
        paths = self.canonical_paths()
        if sequence_index is None:
            paths[path_slot] = path
        else:
            values = list(paths[path_slot])
            values[sequence_index] = path
            paths[path_slot] = tuple(values)
        digest = sha256_bytes(raw)
        current = getattr(resolver, digest_attribute)
        replacement: Any = digest
        if digest_sequence_index is not None:
            replacement = list(current)
            replacement[digest_sequence_index] = digest
            replacement = tuple(replacement)
        with patch.object(resolver, digest_attribute, replacement):
            request = self.new_request()
            return self.resolve_current(request, **paths)

    def test_module_identity_families_and_output_contract(self) -> None:
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min",
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_ID,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001",
        )
        self.assertEqual(
            resolver.OPERATION_TYPE,
            "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_OPERATION",
        )
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "EVALUATE_AND_RECORD_ONE_HETEROGENEOUS_TEN_CONDITION_MATRIX_FROM_ONE_FROZEN_BODY_HELD_BASIS_ONLY",
        )
        self.assertEqual(
            resolver.SELECTED_MATTER_CLASS,
            "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_REMAINING_TEN_INTEGRITY_CONDITIONS_ONLY",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (resolver.OUTCOME_RECORDED, resolver.OUTCOME_BLOCKED),
        )
        self.assertEqual(resolver.OPERATION_RESULT_FAMILY, resolver.OUTCOME_FAMILY)
        self.assertEqual(
            resolver.RESULT_FAMILY,
            (resolver.RESULT_RECORDED, resolver.RESULT_NOT_EVALUATED),
        )
        self.assertEqual(
            resolver.CONDITION_EVALUATION_FAMILY,
            (
                "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS",
                "REQUIRES_BASIS",
                "INDETERMINATE",
                "NOT_EVALUATED",
            ),
        )
        self.assertEqual(
            resolver.REQUIRED_BASIS_CLASS_FAMILY,
            (
                "CUSTODY_DISTINCT_BASIS",
                "EXTERNAL_AUTHENTICITY_BASIS",
                "OTHER_EXACT_NAMED_BASIS",
                "NONE",
            ),
        )
        self.assertIsNone(resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(resolver.OUTPUT_ROOT, resolver.CANONICAL_OUTPUT_ROOT)
        self.assertEqual(resolver.CANONICAL_OUTPUT_ROOT.parent, REPO_ROOT / "artifacts")
        self.assertEqual(
            resolver.CANONICAL_OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min",
        )
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_001__body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result.json",
        )
        for name in (
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request",
            "build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_from_path",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_summary",
            "write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

    def test_exact_ordered_matter_values_evidence_classes_and_ledger_schema(self) -> None:
        expected = (
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
        self.assertEqual(resolver.REQUIRED_CONDITIONS, expected)
        self.assertEqual(list(resolver.REQUIRED_CONDITION_VALUES), list(expected))
        self.assertIs(resolver.REQUIRED_CONDITION_VALUES[expected[0]], True)
        self.assertTrue(
            all(resolver.REQUIRED_CONDITION_VALUES[item] is False for item in expected[1:])
        )
        self.assertEqual(
            resolver.EVIDENCE_CLASSES,
            (
                "CUSTODY_AND_CONTROL",
                "EXECUTION_AND_ATTESTATION_FORM",
                "ADVERSARIAL_INTEGRITY_AND_BOUNDED_ADMISSIBILITY",
            ),
        )
        self.assertEqual(resolver.EVIDENCE_CLASS_CONDITION_MAPPING[resolver.EVIDENCE_CLASSES[0]], expected[:2])
        self.assertEqual(resolver.EVIDENCE_CLASS_CONDITION_MAPPING[resolver.EVIDENCE_CLASSES[1]], expected[2:8])
        self.assertEqual(resolver.EVIDENCE_CLASS_CONDITION_MAPPING[resolver.EVIDENCE_CLASSES[2]], expected[8:])
        self.assertEqual(
            resolver.CONDITION_LEDGER_SCHEMA_FIELDS,
            (
                "condition_id",
                "required_value",
                "prior_condition_posture",
                "evidence_class",
                "permitted_artifact_references",
                "supporting_fields_or_bytes",
                "support_proposition",
                "limitation",
                "dependency_conditions",
                "dependency_ceiling",
                "candidate_evidence_considered_but_not_admitted",
                "evaluation_posture",
                "required_basis_class",
                "compact_support_boolean",
                "successor_condition_posture",
                "prior_posture_preserved",
                "no_overwrite",
            ),
        )

    def test_default_result_is_non_executing_and_has_no_filesystem_reads(self) -> None:
        with patch.object(resolver, "_read_bytes", side_effect=AssertionError("filesystem read")):
            result = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result()
        self.assert_blocked(result, "NOT_EXECUTED")
        self.assertEqual(result["condition_ledger"], [])
        aggregate = result["aggregate_matrix_posture"]
        self.assertEqual(aggregate["supported_by_admitted_body_held_records_count"], 0)
        self.assertEqual(aggregate["requires_basis_count"], 0)
        self.assertEqual(aggregate["not_evaluated_count"], 10)
        raw = result["raw_signal_posture"]
        self.assertIs(raw["raw_signal_body_known_to_exist"], True)
        self.assertIs(raw["raw_signal_body_considered"], True)
        for field in (
            "raw_signal_body_admitted",
            "raw_signal_body_read_authorized",
            "signal_morphology_evaluation_authorized",
            "authenticity_upgrade_from_signal_authorized",
        ):
            self.assertIs(raw[field], False)
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_canonical_request_exact_schema(self) -> None:
        request = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_request()
        self.assertEqual(set(request), EXPECTED_REQUEST_KEYS)
        self.assertEqual(request, self.canonical_request)
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["ordered_ten_condition_matter"], list(resolver.REQUIRED_CONDITIONS))
        self.assertEqual(request["required_condition_values"], resolver.REQUIRED_CONDITION_VALUES)
        self.assertEqual(request["evidence_class_family"], list(resolver.EVIDENCE_CLASSES))
        self.assertEqual(
            request["evidence_class_condition_mapping"],
            {key: list(value) for key, value in resolver.EVIDENCE_CLASS_CONDITION_MAPPING.items()},
        )
        self.assertEqual(request["condition_evaluation_family"], list(resolver.CONDITION_EVALUATION_FAMILY))
        self.assertEqual(request["required_basis_class_family"], list(resolver.REQUIRED_BASIS_CLASS_FAMILY))
        self.assertEqual(request["operation_result_family"], list(resolver.OPERATION_RESULT_FAMILY))
        self.assertEqual(request["condition_ledger_field_order"], list(resolver.CONDITION_LEDGER_SCHEMA_FIELDS))
        self.assertEqual(request["dependency_ceiling_contract"], list(resolver.DEPENDENCY_CEILING_CONTRACT))
        self.assertEqual(request["frozen_read_contract"], resolver._frozen_read_contract())
        self.assertEqual(request["excluded_read_contract"], list(resolver.EXCLUDED_READ_CONTRACT))
        self.assertEqual(request["raw_signal_posture"], resolver.RAW_SIGNAL_POSTURE)
        self.assertEqual(request["temporal_evidence"], resolver.TEMPORAL_EVIDENCE)
        self.assertEqual(request["expected_condition_ledger"], list(resolver.EXPECTED_CONDITION_LEDGER))
        self.assertEqual(request["expected_aggregate_matrix_posture"], resolver.EXPECTED_AGGREGATE_MATRIX_POSTURE)
        self.assertEqual(request["declared_non_claims"], resolver._canonical_non_claims())
        self.assertEqual(request["governing_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_specification_sha256"], resolver.GOVERNING_SPECIFICATION_SHA256)
        self.assertEqual(request["completed_boundary_artifact_sha256"], resolver.BOUNDARY_ARTIFACT_SHA256)
        self.assertEqual(request["prior_standing_sha256"], list(resolver.PRIOR_STANDING_SHA256))
        self.assertEqual(request["carriage_lineage_sha256"], list(resolver.CARRIAGE_LINEAGE_SHA256))
        self.assertEqual(request["receiver_packet_text_byte_counts"], list(resolver.PACKET_TEXT_BYTE_COUNTS))
        prohibited = resolver.PROHIBITED_DIRECT_REQUEST_FIELDS
        self.assertTrue(set(request).isdisjoint(prohibited))
        serialized = json.dumps(request, sort_keys=True)
        for key in ("raw_signal_content", "archive_bytes", "custody_proof", "receiver_identity", "non_forgery_claim", "global_admissibility", "complete_receiver_answerable_basis", "presence", "truth", "standing", "authority", "automatic_next"):
            self.assertNotIn(f'"{key}"', serialized)

    def test_valid_canonical_execution_records_operation(self) -> None:
        result = self.recorded_result
        self.assert_recorded(result)
        self.assertEqual(result["condition_ledger"], list(resolver.EXPECTED_CONDITION_LEDGER))
        self.assertEqual(result["aggregate_matrix_posture"], resolver.EXPECTED_AGGREGATE_MATRIX_POSTURE)
        self.assertEqual(result["condition_evaluations"], {row["condition_id"]: row["evaluation_posture"] for row in resolver.EXPECTED_CONDITION_LEDGER})
        operation = result[OPERATION_KEY]
        self.assertIs(operation["all_ten_conditions_evaluated"], True)
        self.assertIs(operation["condition_ledger_populated"], True)
        self.assertEqual(operation["condition_result_count"], 10)
        self.assertIsNone(operation["admissible_future_route"])

    def test_successful_ledger_has_exact_ten_rows_in_order(self) -> None:
        ledger = self.recorded_result["condition_ledger"]
        self.assertEqual(ledger, list(resolver.EXPECTED_CONDITION_LEDGER))
        self.assertEqual([row["condition_id"] for row in ledger], list(resolver.REQUIRED_CONDITIONS))
        for row in ledger:
            self.assertEqual(tuple(row), resolver.CONDITION_LEDGER_SCHEMA_FIELDS)

    def test_rows_one_through_eight_and_ten_are_supported(self) -> None:
        for index in (*range(8), 9):
            row = self.recorded_result["condition_ledger"][index]
            with self.subTest(condition=row["condition_id"]):
                self.assertEqual(row["prior_condition_posture"], resolver.CONDITION_REQUIRES_BASIS)
                self.assertEqual(row["evaluation_posture"], resolver.CONDITION_SUPPORTED)
                self.assertEqual(row["required_basis_class"], resolver.BASIS_NONE)
                self.assertIs(row["compact_support_boolean"], True)
                self.assertEqual(row["successor_condition_posture"], resolver.CONDITION_SUPPORTED)
                self.assertIs(row["prior_posture_preserved"], True)
                self.assertIs(row["no_overwrite"], True)

    def test_forgery_row_requires_external_authenticity_basis(self) -> None:
        row = self.recorded_result["condition_ledger"][8]
        expected = resolver.EXPECTED_CONDITION_LEDGER[8]
        self.assertEqual(row, expected)
        self.assertEqual(row["condition_id"], "forged_receiver_attestation")
        self.assertIs(row["required_value"], False)
        self.assertEqual(row["prior_condition_posture"], resolver.CONDITION_REQUIRES_BASIS)
        self.assertEqual(row["evidence_class"], resolver.EVIDENCE_CLASSES[2])
        self.assertEqual(row["evaluation_posture"], resolver.CONDITION_REQUIRES_BASIS)
        self.assertEqual(row["required_basis_class"], resolver.BASIS_EXTERNAL_AUTHENTICITY)
        self.assertIsNone(row["compact_support_boolean"])
        self.assertEqual(row["successor_condition_posture"], resolver.CONDITION_REQUIRES_BASIS)
        self.assertEqual(row["dependency_conditions"], ["receiver_answerable_basis_custody_distinct", "receiver-originating source relation", "preservation integrity", "candidate correspondence", "external authenticity"])
        self.assertEqual(row["dependency_ceiling"], "MAY_NOT_OUTRUN_CUSTODY_ORIGIN_PRESERVATION_CORRESPONDENCE_AND_EXTERNAL_AUTHENTICITY_BASIS")
        self.assertEqual(row["limitation"], "cryptographic receiver signature, trusted device attestation, independent witness, exclusive key control, and proof against pre-hash fabrication remain outside body custody")
        self.assertIs(row["prior_posture_preserved"], True)
        self.assertIs(row["no_overwrite"], True)

    def test_forgery_row_raw_signal_is_considered_but_not_admitted(self) -> None:
        expected = [
            "raw accelerometer signal body exists",
            "potential signal-morphology relevance recognized",
            "raw signal not admitted",
            "raw signal not read",
            "no morphology evaluation",
            "no authenticity upgrade",
        ]
        ledger = self.recorded_result["condition_ledger"]
        self.assertEqual(ledger[8]["candidate_evidence_considered_but_not_admitted"], expected)
        for index, row in enumerate(ledger):
            if index != 8:
                self.assertEqual(row["candidate_evidence_considered_but_not_admitted"], [])

    def test_aggregate_matrix_exact(self) -> None:
        ledger = self.recorded_result["condition_ledger"]
        aggregate = self.recorded_result["aggregate_matrix_posture"]
        postures = [row["evaluation_posture"] for row in ledger]
        compact = [row["compact_support_boolean"] for row in ledger]
        independently_derived = {
            "ordered_condition_count": len(ledger),
            "supported_by_admitted_body_held_records_count": postures.count(resolver.CONDITION_SUPPORTED),
            "requires_basis_count": postures.count(resolver.CONDITION_REQUIRES_BASIS),
            "indeterminate_count": postures.count(resolver.CONDITION_INDETERMINATE),
            "not_evaluated_count": postures.count(resolver.CONDITION_NOT_EVALUATED),
            "compact_support_true_count": sum(value is True for value in compact),
            "compact_support_false_count": sum(value is False for value in compact),
            "compact_support_null_count": sum(value is None for value in compact),
            "prior_posture_preserved_count": sum(row["prior_posture_preserved"] is True for row in ledger),
            "no_overwrite_count": sum(row["no_overwrite"] is True for row in ledger),
            "evidence_class_count": len({row["evidence_class"] for row in ledger}),
            "dependency_ceiling_count": len(ledger),
            "all_ten_conditions_evaluated": len(ledger) == 10 and resolver.CONDITION_NOT_EVALUATED not in postures,
            "condition_ledger_populated": len(ledger) == 10,
            "condition_result_count": len(ledger),
            "requires_basis_conditions": [row["condition_id"] for row in ledger if row["evaluation_posture"] == resolver.CONDITION_REQUIRES_BASIS],
            "requires_basis_classes": [row["required_basis_class"] for row in ledger if row["evaluation_posture"] == resolver.CONDITION_REQUIRES_BASIS],
        }
        self.assertEqual(aggregate, resolver.EXPECTED_AGGREGATE_MATRIX_POSTURE)
        self.assertEqual(aggregate, independently_derived)

    def test_row_level_requires_basis_does_not_block_operation(self) -> None:
        self.assert_recorded(self.recorded_result)
        row = self.recorded_result["condition_ledger"][8]
        self.assertEqual(row["evaluation_posture"], resolver.CONDITION_REQUIRES_BASIS)
        self.assertEqual(self.recorded_result["aggregate_matrix_posture"]["requires_basis_count"], 1)
        self.assertTrue(all(check["passed"] is True for check in self.checks(self.recorded_result)))

    def test_completed_boundary_exact_standing_consumed(self) -> None:
        artifact = self.boundary_artifact
        self.assertEqual(sha256_bytes(self.boundary_artifact_bytes), resolver.BOUNDARY_ARTIFACT_SHA256)
        self.assertEqual(artifact["outcome"], "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY_ALLOWED")
        self.assertEqual(artifact["boundary_result"], "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_CONSIDERATION_ALLOWED")
        self.assertEqual(artifact["passed_check_count"], 188)
        self.assertEqual(artifact["failed_check_count"], 0)
        self.assertIs(artifact["block"]["blocked"], False)
        self.assertIs(artifact["boundary_decision"]["selection"], True)
        self.assertEqual(artifact["boundary_decision"]["decision_code"], "BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_ALLOWED")
        posture = artifact["boundary_posture"]
        self.assertIs(posture["body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_recorded"], True)
        self.assertIs(posture["body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_result_recorded"], True)
        self.assertIs(posture["body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_exhausted"], True)
        self.assertEqual(posture["completed_consideration_posture_count"], 1)
        self.assertIs(posture["single_use_only"], True)
        self.assertTrue(all(value == resolver.ADMISSIBILITY_PASSED for value in artifact["admissibility_evaluations"].values()))
        boundary = artifact["body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary"]
        self.assertEqual(boundary["condition_evaluations"], {condition: resolver.CONDITION_NOT_EVALUATED for condition in resolver.REQUIRED_CONDITIONS})
        for field in ("condition_ledger_populated", "later_operation_result_selected", "later_operation_created", "later_operation_executed", "raw_signal_body_admitted", "raw_signal_body_read_authorized", "signal_morphology_evaluation_authorized", "authenticity_upgrade_from_signal_authorized"):
            self.assertIs(boundary[field], False)
        self.assertIs(artifact["frozen_read_contract_posture"]["read_contract_closed"], True)
        self.assertEqual(artifact["admissible_future_route"], resolver.CONSUMED_BOUNDARY_ROUTE)
        self.assertEqual(boundary["admissible_future_route"], resolver.CONSUMED_BOUNDARY_ROUTE)
        validation = self.recorded_result["boundary_artifact_validation"]
        self.assertIs(validation["strict_content_validated"], True)
        self.assertIs(validation["single_use_route_validated"], True)

    def test_boundary_terminal_summary_exact_digest_and_markers(self) -> None:
        raw = self.boundary_terminal_summary_bytes
        text = raw.decode("utf-8", errors="strict")
        self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
        self.assertEqual(sha256_bytes(raw), resolver.BOUNDARY_TERMINAL_SUMMARY_SHA256)
        for marker in (
            "# Body-Held Receiver-Answerable-Basis Integrity-Condition Evaluation Boundary V0 Minimum Terminal Summary",
            "outcome = BODY_HELD_RECEIVER_ANSWERABLE_BASIS_INTEGRITY_CONDITION_EVALUATION_BOUNDARY_ALLOWED",
            resolver.CONSUMED_BOUNDARY_ROUTE,
            "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_exhausted = true",
        ):
            self.assertIn(marker, text)
        validation = self.recorded_result["boundary_terminal_summary_validation"]
        self.assertEqual(validation["surface_path"], str(resolver.BOUNDARY_TERMINAL_SUMMARY_RELATIVE_PATH))
        self.assertEqual(validation["observed_sha256"], resolver.BOUNDARY_TERMINAL_SUMMARY_SHA256)
        self.assertIs(validation["surface_validated"], True)

    def test_prior_presence_historical_matrix_preserved(self) -> None:
        presence = self.prior_standing[0]
        self.assertEqual(presence["outcome"], "PRESENCE_RE_EVALUATION_OPERATION_REQUIRES_RECEIVER_ANSWERABLE_BASIS")
        self.assertEqual(presence["presence_re_evaluation_operation_result"], "REQUIRES_RECEIVER_ANSWERABLE_BASIS")
        self.assertEqual((presence["passed_check_count"], presence["failed_check_count"]), (409, 0))
        self.assertIsNone(presence["admissible_future_route"])
        evaluations = {key: value["evaluation"] for key, value in presence["condition_evaluations"].items()}
        self.assertEqual(evaluations, resolver.HISTORICAL_CONDITION_MATRIX)
        self.assertEqual(list(evaluations.values()).count("SATISFIED"), 2)
        self.assertEqual(list(evaluations.values()).count(resolver.CONDITION_REQUIRES_BASIS), 12)
        operation = presence["presence_re_evaluation_operation"]
        for field in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded"):
            self.assertIs(operation[field], False)
        self.assertIs(self.recorded_result["lineage_preservation_posture"]["historical_fourteen_condition_matrix_preserved"], True)
        self.assertIs(self.recorded_result["lineage_preservation_posture"]["prior_twelve_requires_basis_rows_preserved"], True)

    def test_later_modal_standing_preserved(self) -> None:
        modal = self.prior_standing[2]
        self.assertEqual(modal["outcome"], "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED")
        self.assertEqual(modal["operation_result"], "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_SUPPORTED")
        self.assertEqual((modal["passed_check_count"], modal["failed_check_count"]), (378, 0))
        self.assertIsNone(modal["admissible_future_route"])
        operation = modal["receiver_originating_modal_fact_evaluation_operation"]
        self.assertIs(operation["receiver_answerable_basis_refusable_supported"], True)
        self.assertIs(operation["receiver_answerable_basis_could_have_been_withheld_supported"], True)
        self.assertIs(operation["receiver_answerable_basis_refusable_established"], False)
        self.assertIs(operation["receiver_answerable_basis_could_have_been_withheld_established"], False)
        excluded = modal["excluded_condition_posture"]
        self.assertEqual(excluded["condition_evaluations"], {condition: resolver.CONDITION_NOT_EVALUATED for condition in resolver.REQUIRED_CONDITIONS})
        self.assertIs(self.recorded_result["lineage_preservation_posture"]["later_refusability_support_preserved"], True)
        self.assertIs(self.recorded_result["lineage_preservation_posture"]["later_withholdability_support_preserved"], True)

    def test_source_admissibility_standing_preserved(self) -> None:
        source = self.prior_standing[1]
        self.assertEqual(source["outcome"], "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED")
        self.assertEqual((source["passed_check_count"], source["failed_check_count"]), (308, 0))
        self.assertTrue(all(value == resolver.ADMISSIBILITY_PASSED for value in source["admissibility_evaluations"].values()))
        boundary = source["receiver_originating_modal_fact_source_admissibility_boundary"]
        self.assertEqual(boundary["selected_source_origin"], "RECEIVER_ORIGINATING")
        self.assertEqual(boundary["selected_source_arrival_posture"], "CARRIED_ARRIVAL")
        self.assertIs(boundary["selected_source_native_standing"], False)
        self.assertIs(boundary["jurisdiction_distinction_preserved"], True)
        lineage = source["lineage_preservation_posture"]
        self.assertIs(lineage["source_not_naturalized"], True)
        self.assertIs(lineage["jurisdiction_not_collapsed"], True)

    def test_all_seven_carriage_lineage_artifacts_validate(self) -> None:
        validations = self.recorded_result["carriage_lineage_validations"]
        self.assertEqual(len(validations), 7)
        expected_modules = (
            "resolve_receiver_side_answerable_basis_reception_operation_v0_min",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_operation_v0_min_v3",
            "resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_declaration_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_basis_supply_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min",
            "resolve_receiver_side_answerable_basis_receiver_answerable_receipt_operation_v0_min",
        )
        expected_counts = (105, 152, 140, 55, 101, 160, 357)
        for index, (path, raw, artifact, validation) in enumerate(zip(CARRIAGE_PATHS, self.carriage_bytes, self.carriage_artifacts, validations)):
            with self.subTest(index=index):
                self.assertEqual(path, REPO_ROOT / resolver.CARRIAGE_LINEAGE_RELATIVE_PATHS[index])
                self.assertEqual(sha256_bytes(raw), resolver.CARRIAGE_LINEAGE_SHA256[index])
                self.assertEqual(artifact["resolver_module"], expected_modules[index])
                self.assertEqual(artifact["passed_check_count"], expected_counts[index])
                self.assertEqual(artifact["failed_check_count"], 0)
                self.assertIs(artifact["block"]["blocked"], False)
                self.assertEqual(validation["surface_path"], str(resolver.CARRIAGE_LINEAGE_RELATIVE_PATHS[index]))
                self.assertEqual(validation["observed_sha256"], resolver.CARRIAGE_LINEAGE_SHA256[index])
                self.assertIs(validation["strict_content_validated"], True)
                self.assertIs(validation["identity_and_completion_validated"], True)
                self.assertIs(validation["correspondence_validated"], True)
                self.assertIs(validation["false_locks_validated"], True)
                self.assertIs(validation["complete_body_omitted"], True)

    def test_all_eight_packet_text_surfaces_validate_exact_bytes(self) -> None:
        validations = self.recorded_result["receiver_packet_text_validations"]
        self.assertEqual(len(validations), 8)
        for index, (path, raw, expected_text, validation) in enumerate(zip(PACKET_TEXT_PATHS, self.packet_bytes, resolver.PACKET_TEXT_CONTENTS, validations)):
            with self.subTest(index=index):
                self.assertEqual(path, REPO_ROOT / resolver.PACKET_TEXT_RELATIVE_PATHS[index])
                self.assertEqual(sha256_bytes(raw), resolver.PACKET_TEXT_SHA256[index])
                self.assertEqual(len(raw), resolver.PACKET_TEXT_BYTE_COUNTS[index])
                self.assertEqual(raw.decode("utf-8", errors="strict"), expected_text)
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
                if path.name != "attestation_statement.txt":
                    records, valid = resolver._parse_exact_records(expected_text)
                    self.assertTrue(valid)
                    self.assertEqual(len(records), len(set(records)))
                self.assertEqual(validation["observed_byte_count"], len(raw))
                self.assertIs(validation["bom_absent"], True)
                self.assertIs(validation["exact_content_validated"], True)
                self.assertIs(validation["duplicate_record_keys_absent"], True)
                self.assertIs(validation["complete_body_omitted"], True)

    def test_all_nine_source_body_conduct_surfaces_validate(self) -> None:
        validations = self.recorded_result["source_body_conduct_validations"]
        self.assertEqual(len(validations), 9)
        for index, (path, raw, validation) in enumerate(zip(CONDUCT_PATHS, self.conduct_bytes, validations)):
            with self.subTest(index=index):
                self.assertEqual(path, REPO_ROOT / resolver.SOURCE_BODY_CONDUCT_RELATIVE_PATHS[index])
                self.assertEqual(sha256_bytes(raw), resolver.SOURCE_BODY_CONDUCT_SHA256[index])
                self.assertEqual(validation["observed_sha256"], resolver.SOURCE_BODY_CONDUCT_SHA256[index])
                self.assertIs(validation["surface_validated"], True)
                self.assertIs(validation["complete_body_omitted"], True)

    def test_frozen_read_contract_exact_and_closed(self) -> None:
        request_contract = self.canonical_request["frozen_read_contract"]
        self.assertEqual(request_contract, resolver._frozen_read_contract())
        posture = self.recorded_result["frozen_read_contract_posture"]
        self.assertIs(posture["read_contract_closed"], True)
        self.assertEqual(posture["governing_and_current_standing_surface_count"], 8)
        self.assertEqual(posture["carriage_lineage_surface_count"], 7)
        self.assertEqual(posture["receiver_packet_text_surface_count"], 8)
        self.assertEqual(posture["source_body_conduct_surface_count"], 9)
        self.assertIs(posture["all_exact_surfaces_validated"], True)
        self.assertIs(posture["no_other_surface_selected"], True)
        self.assertIs(posture["filesystem_discovery_performed"], False)
        self.assertIs(posture["latest_file_selection_performed"], False)
        self.assertIs(posture["source_reconstruction_performed"], False)

    def test_excluded_read_contract_exact(self) -> None:
        self.assertEqual(self.canonical_request["excluded_read_contract"], list(resolver.EXCLUDED_READ_CONTRACT))
        posture = self.recorded_result["excluded_read_posture"]
        self.assertEqual(posture["excluded_read_contract"], list(resolver.EXCLUDED_READ_CONTRACT))
        self.assertIs(posture["excluded_read_requested"], False)
        self.assertIs(posture["excluded_read_performed"], False)
        self.assertIs(posture["raw_signal_or_archive_opened"], False)
        self.assertIs(posture["glob_rglob_scan_or_discovery_performed"], False)

    def test_raw_signal_global_posture_exact(self) -> None:
        self.assertEqual(self.recorded_result["raw_signal_posture"], resolver.RAW_SIGNAL_POSTURE)
        raw = self.recorded_result["raw_signal_posture"]
        self.assertIs(raw["raw_signal_body_known_to_exist"], True)
        self.assertIs(raw["raw_signal_body_considered"], True)
        for field in ("raw_signal_body_admitted", "raw_signal_body_read_authorized", "signal_morphology_evaluation_authorized", "authenticity_upgrade_from_signal_authorized"):
            self.assertIs(raw[field], False)
        excluded = self.recorded_result["excluded_read_posture"]
        self.assertIs(excluded["raw_signal_or_archive_opened"], False)
        self.assert_no_prohibited_material(self.recorded_result)

    def test_temporal_evidence_exact_and_bounded(self) -> None:
        expected = {
            "knock_generated_at": "2026-07-15T12:08:04Z",
            "receiver_attestation_confirmed_at": "2026-07-28T06:37:56Z",
            "knock_to_receiver_attestation_interval_seconds": 1103392,
            "knock_to_receiver_attestation_interval_components": {"days": 12, "hours": 18, "minutes": 29, "seconds": 52},
            "knock_to_receiver_attestation_interval": "12 days, 18 hours, 29 minutes, 52 seconds",
            "current_clock_used": False,
            "actual_refusal_inferred": False,
            "actual_withholding_inferred": False,
            "receiver_freedom_inferred": False,
            "universal_automation_absence_inferred": False,
        }
        self.assertEqual(resolver.TEMPORAL_EVIDENCE, expected)
        self.assertEqual(self.canonical_request["temporal_evidence"], expected)
        self.assertEqual(self.recorded_result["temporal_evidence_posture"], {**expected, "temporal_evidence_validated": True})

    def test_dependency_ceiling_contract_exact_and_ordered(self) -> None:
        expected = [
            {"condition_or_family": "same_custody_countersignature", "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT"},
            {"condition_or_family": "operator_only_attestation", "ceiling": "MAY_NOT_OUTRUN_RECEIVER_ORIGIN_AND_CUSTODY_RELATION_SUPPORT"},
            {"condition_or_family": "derivative_rendering_attestation", "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE"},
            {"condition_or_family": "generated_affirmation", "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_SOURCE_BODY_CONDUCT_AND_CARRIED_LINEAGE"},
            {"condition_or_family": "automatic_acknowledgement", "ceiling": "ABSENCE_LIMITED_TO_ADMITTED_MACHINERY_AND_CHRONOLOGY"},
            {"condition_or_family": "forged_receiver_attestation", "ceiling": "MAY_NOT_OUTRUN_CUSTODY_ORIGIN_PRESERVATION_CORRESPONDENCE_AND_EXTERNAL_AUTHENTICITY_BASIS"},
            {"condition_or_family": "inadmissible_receiver_basis", "ceiling": "MAY_NOT_OUTRUN_EXACT_ADMITTED_RELATION_AND_MATTER_SCOPE"},
            {"condition_or_family": "ALL_NEGATIVE_FORM_CONDITIONS", "ceiling": "MAY_NOT_BECOME_UNIVERSAL_ABSENCE"},
            {"condition_or_family": "ALL_SIBLING_CONDITIONS", "ceiling": "NO_SUCCESSFUL_SIBLING_MAY_SILENTLY_STRENGTHEN_ANOTHER"},
            {"condition_or_family": "ALL_DEPENDENCIES", "ceiling": "NO_DEPENDENCY_MAY_BE_BYPASSED"},
        ]
        self.assertEqual(list(resolver.DEPENDENCY_CEILING_CONTRACT), expected)
        self.assertEqual(self.recorded_result["dependency_ceiling_contract"], expected)
        self.assertIn("NO_SUCCESSFUL_SIBLING_MAY_SILENTLY_STRENGTHEN_ANOTHER", [item["ceiling"] for item in expected])

    def test_support_propositions_and_limitations_exact(self) -> None:
        self.assertEqual(self.recorded_result["condition_ledger"], list(resolver.EXPECTED_CONDITION_LEDGER))
        for actual, expected in zip(self.recorded_result["condition_ledger"], resolver.EXPECTED_CONDITION_LEDGER):
            with self.subTest(condition=actual["condition_id"]):
                for field in ("permitted_artifact_references", "supporting_fields_or_bytes", "support_proposition", "limitation", "dependency_conditions", "dependency_ceiling"):
                    self.assertEqual(actual[field], expected[field])

    def test_three_part_operation_admissibility_all_passes_or_blocks(self) -> None:
        self.assertTrue(all(value == resolver.ADMISSIBILITY_PASSED for value in self.recorded_result["operation_admissibility_evaluations"].values()))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source_path = self.write_bytes(base / "source" / "boundary.json", self.boundary_artifact_bytes + b" ")
            source = self.resolve_current(self.canonical_request, boundary_artifact_path=source_path)
            self.assert_blocked(source, "BOUNDARY_ARTIFACT_DIGEST_MISMATCH")
            matter_request = copy.deepcopy(self.canonical_request)
            matter_request["ordered_ten_condition_matter"] = matter_request["ordered_ten_condition_matter"][:-1]
            with patch.object(resolver, "_read_bytes", side_effect=AssertionError("basis read")):
                matter = self.resolve_current(matter_request)
            self.assert_blocked(matter)
            transition_artifact = copy.deepcopy(self.prior_standing[1])
            transition_artifact["lineage_preservation_posture"]["source_not_naturalized"] = False
            transition = self.resolve_mutated_json(
                base=base,
                fixture_name="transition/source.json",
                artifact=transition_artifact,
                path_slot="source_admissibility_boundary_artifact_path",
                digest_attribute="PRIOR_STANDING_SHA256",
                digest_sequence_index=1,
            )
            self.assert_blocked(transition, "PRIOR_STANDING_SURFACE_INVALID")

    def test_invalid_request_schema_blocks_before_evaluation(self) -> None:
        cases: list[tuple[str, dict[str, Any]]] = []
        request = copy.deepcopy(self.canonical_request); request.pop("intent"); cases.append(("missing_field", request))
        request = copy.deepcopy(self.canonical_request); request["unknown_field"] = False; cases.append(("unknown_field", request))
        identity_key = "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id"
        cases.extend((name, self.new_request(**override)) for name, override in (
            ("wrong_intent", {"intent": "WRONG"}),
            ("wrong_identity", {identity_key: "wrong"}),
            ("wrong_path", {"completed_boundary_artifact_path": "wrong.json"}),
            ("wrong_digest", {"completed_boundary_artifact_sha256": "0" * 64}),
            ("reordered_matter", {"ordered_ten_condition_matter": list(reversed(resolver.REQUIRED_CONDITIONS))}),
            ("narrowed_matter", {"ordered_ten_condition_matter": list(resolver.REQUIRED_CONDITIONS[:-1])}),
            ("broadened_matter", {"ordered_ten_condition_matter": [*resolver.REQUIRED_CONDITIONS, "extra"]}),
            ("changed_required_value", {"required_condition_values": {**resolver.REQUIRED_CONDITION_VALUES, resolver.REQUIRED_CONDITIONS[0]: False}}),
            ("changed_evidence_class", {"evidence_class_family": [*resolver.EVIDENCE_CLASSES[:-1], "WRONG"]}),
            ("changed_ledger_order", {"condition_ledger_field_order": list(reversed(resolver.CONDITION_LEDGER_SCHEMA_FIELDS))}),
            ("altered_row", {"expected_condition_ledger": [{**row, "evaluation_posture": "WRONG"} if index == 0 else row for index, row in enumerate(resolver.EXPECTED_CONDITION_LEDGER)]}),
            ("altered_basis_class", {"expected_condition_ledger": [{**row, "required_basis_class": "WRONG"} if index == 8 else row for index, row in enumerate(resolver.EXPECTED_CONDITION_LEDGER)]}),
            ("omitted_ceiling", {"dependency_ceiling_contract": list(resolver.DEPENDENCY_CEILING_CONTRACT[:-1])}),
            ("changed_excluded_reads", {"excluded_read_contract": [*resolver.EXCLUDED_READ_CONTRACT[:-1], "WRONG"]}),
            ("raw_admitted", {"raw_signal_posture": {**resolver.RAW_SIGNAL_POSTURE, "raw_signal_body_admitted": True}}),
            ("raw_read", {"raw_signal_posture": {**resolver.RAW_SIGNAL_POSTURE, "raw_signal_body_read_authorized": True}}),
            ("morphology", {"raw_signal_posture": {**resolver.RAW_SIGNAL_POSTURE, "signal_morphology_evaluation_authorized": True}}),
            ("authenticity_upgrade", {"raw_signal_posture": {**resolver.RAW_SIGNAL_POSTURE, "authenticity_upgrade_from_signal_authorized": True}}),
            ("semantic_payload", {"semantic_payload": {"x": 1}}),
            ("non_null_route", {"admissible_future_route": "WRONG"}),
        ))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims.pop(next(iter(nonclaims))); cases.append(("nonclaim_missing", self.new_request(declared_non_claims=nonclaims)))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims["unknown"] = False; cases.append(("nonclaim_unknown", self.new_request(declared_non_claims=nonclaims)))
        key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims[key] = 0; cases.append(("nonclaim_nonbool", self.new_request(declared_non_claims=nonclaims)))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims[key] = True; cases.append(("nonclaim_true", self.new_request(declared_non_claims=nonclaims)))
        for name, invalid in cases:
            with self.subTest(name=name), patch.object(resolver, "_read_bytes", side_effect=AssertionError("basis read")):
                self.assert_blocked(self.resolve_current(invalid))

    def test_duplicate_key_request_json_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_bytes(Path(directory) / "duplicate.json", b'{"intent":"a","intent":"b"}\n')
            result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_from_path(path, **self.canonical_paths())
            self.assert_blocked(result, "REQUEST_JSON_INVALID")
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_non_object_malformed_and_nonfinite_request_json_blocks(self) -> None:
        payloads = (b"[]", b'"text"', b"7", b"true", b"null", b"{", b'{"value":NaN}', b'{"value":Infinity}', b'{"value":-Infinity}')
        with tempfile.TemporaryDirectory() as directory:
            for index, raw in enumerate(payloads):
                with self.subTest(index=index, raw=raw):
                    path = self.write_bytes(Path(directory) / f"request_{index}.json", raw)
                    result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_from_path(path, **self.canonical_paths())
                    self.assert_blocked(result, "REQUEST_JSON_INVALID")

    def test_each_pinned_json_digest_mismatch_blocks(self) -> None:
        cases: list[tuple[str, bytes, int | None]] = [
            ("boundary_artifact_path", self.boundary_artifact_bytes, None),
            ("prior_presence_artifact_path", self.prior_standing_bytes[0], None),
            ("source_admissibility_boundary_artifact_path", self.prior_standing_bytes[1], None),
            ("later_modal_artifact_path", self.prior_standing_bytes[2], None),
        ]
        cases.extend(("carriage_lineage_paths", raw, index) for index, raw in enumerate(self.carriage_bytes))
        cases.extend(("source_body_conduct_paths", self.conduct_bytes[index], index) for index in (2, 5, 8))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for case_index, (slot, raw, index) in enumerate(cases):
                with self.subTest(slot=slot, index=index):
                    path = self.write_bytes(base / f"json_digest_{case_index}.json", raw + b" ")
                    paths = self.canonical_paths()
                    if index is None:
                        paths[slot] = path
                    else:
                        values = list(paths[slot]); values[index] = path; paths[slot] = tuple(values)
                    self.assert_blocked(self.resolve_current(self.canonical_request, **paths))

    def test_each_pinned_text_digest_mismatch_blocks(self) -> None:
        cases: list[tuple[str, bytes, int | None]] = [
            ("governing_specification_path", self.specification_bytes, None),
            ("boundary_specification_path", self.boundary_specification_bytes, None),
            ("boundary_terminal_summary_path", self.boundary_terminal_summary_bytes, None),
            ("modal_terminal_summary_path", self.prior_standing_bytes[3], None),
        ]
        cases.extend(("receiver_packet_text_paths", raw, index) for index, raw in enumerate(self.packet_bytes))
        cases.extend(("source_body_conduct_paths", self.conduct_bytes[index], index) for index in (0, 1, 3, 4, 6, 7))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for case_index, (slot, raw, index) in enumerate(cases):
                with self.subTest(slot=slot, index=index):
                    path = self.write_bytes(base / f"text_digest_{case_index}.txt", raw + b" ")
                    paths = self.canonical_paths()
                    if index is None:
                        paths[slot] = path
                    else:
                        values = list(paths[slot]); values[index] = path; paths[slot] = tuple(values)
                    self.assert_blocked(self.resolve_current(self.canonical_request, **paths))

    def test_duplicate_key_each_governed_json_blocks(self) -> None:
        cases: list[tuple[str, bytes, int | None]] = [
            ("boundary_artifact_path", self.boundary_artifact_bytes, None),
            ("prior_presence_artifact_path", self.prior_standing_bytes[0], None),
            ("source_admissibility_boundary_artifact_path", self.prior_standing_bytes[1], None),
            ("later_modal_artifact_path", self.prior_standing_bytes[2], None),
        ]
        cases.extend(("carriage_lineage_paths", raw, index) for index, raw in enumerate(self.carriage_bytes))
        cases.extend(("source_body_conduct_paths", self.conduct_bytes[index], index) for index in (2, 5, 8))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for case_index, (slot, raw, index) in enumerate(cases):
                with self.subTest(slot=slot, index=index):
                    path = self.write_bytes(base / f"duplicate_{case_index}.json", self.duplicate_top_level_key(raw))
                    paths = self.canonical_paths()
                    if index is None:
                        paths[slot] = path
                    else:
                        values = list(paths[slot]); values[index] = path; paths[slot] = tuple(values)
                    self.assert_blocked(self.resolve_current(self.canonical_request, **paths))

    def test_packet_text_strictness_blocks_normalization(self) -> None:
        first = self.packet_bytes[0]
        lines = first.decode("utf-8").splitlines(keepends=True)
        variants: list[tuple[str, int, bytes]] = [
            ("bom", 0, b"\xef\xbb\xbf" + first),
            ("invalid_utf8", 0, first + b"\xff"),
            ("byte_change", 0, first + b" "),
            ("newline_change", 0, first.rstrip(b"\n") + b"\r\n"),
            ("reorder", 0, "".join(reversed(lines)).encode("utf-8")),
            ("duplicate_key", 0, first + lines[0].encode("utf-8")),
            ("missing_key", 0, lines[0].encode("utf-8")),
            ("unknown_key", 0, first + b"unknown=value\n"),
            ("blank_line", 0, first + b"\n"),
            ("malformed", 0, first + b"malformed\n"),
            ("timestamp", 2, self.packet_bytes[2].replace(b"2026-07-28", b"2026-07-29")),
            ("whitespace", 0, first.replace(b"=", b" = ", 1)),
        ]
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, index, raw in variants:
                with self.subTest(name=name):
                    result = self.resolve_mutated_text(
                        base=base,
                        fixture_name=f"{name}/packet.txt",
                        raw=raw,
                        path_slot="receiver_packet_text_paths",
                        digest_attribute="PACKET_TEXT_SHA256",
                        sequence_index=index,
                        digest_sequence_index=index,
                    )
                    self.assert_blocked(result, "PACKET_TEXT_INVALID")

    def test_boundary_mismatch_blocks(self) -> None:
        boundary_key = "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary"
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", ("boundary_result",), "WRONG"),
            ("passed_count", ("passed_check_count",), 187),
            ("failed_count", ("failed_check_count",), 1),
            ("blocked", ("block", "blocked"), True),
            ("unexhausted", ("boundary_posture", "body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_exhausted"), False),
            ("non_single_use", ("boundary_posture", "single_use_only"), False),
            ("route", ("admissible_future_route",), "WRONG"),
            ("condition", (boundary_key, "condition_evaluations", resolver.REQUIRED_CONDITIONS[0]), resolver.CONDITION_SUPPORTED),
            ("ledger", (boundary_key, "condition_ledger_populated"), True),
            ("selected", (boundary_key, "later_operation_result_selected"), True),
            ("executed", (boundary_key, "later_operation_executed"), True),
            ("raw_signal", (boundary_key, "raw_signal_body_admitted"), True),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, keys, value in cases:
                artifact = copy.deepcopy(self.boundary_artifact)
                self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(
                    base=base,
                    fixture_name=f"{name}/boundary.json",
                    artifact=artifact,
                    path_slot="boundary_artifact_path",
                    digest_attribute="BOUNDARY_ARTIFACT_SHA256",
                )
                with self.subTest(name=name):
                    self.assert_blocked(result)

    def test_prior_standing_mismatch_blocks(self) -> None:
        cases = (
            (0, "presence_outcome", ("outcome",), "WRONG"),
            (0, "presence_route", ("admissible_future_route",), "WRONG"),
            (0, "presence_matrix", ("condition_evaluations", resolver.REQUIRED_CONDITIONS[0], "evaluation"), "SATISFIED"),
            (1, "source_origin", ("receiver_originating_modal_fact_source_admissibility_boundary", "selected_source_origin"), "WRONG"),
            (1, "source_naturalized", ("lineage_preservation_posture", "source_not_naturalized"), False),
            (1, "source_route", ("admissible_future_route",), "WRONG"),
            (2, "modal_outcome", ("outcome",), "WRONG"),
            (2, "modal_support", ("receiver_originating_modal_fact_evaluation_operation", "receiver_answerable_basis_refusable_supported"), False),
            (2, "modal_established", ("receiver_originating_modal_fact_evaluation_operation", "receiver_answerable_basis_refusable_established"), True),
        )
        slots = ("prior_presence_artifact_path", "source_admissibility_boundary_artifact_path", "later_modal_artifact_path")
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for index, name, keys, value in cases:
                artifact = copy.deepcopy(self.prior_standing[index])
                self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(
                    base=base,
                    fixture_name=f"{name}/artifact.json",
                    artifact=artifact,
                    path_slot=slots[index],
                    digest_attribute="PRIOR_STANDING_SHA256",
                    digest_sequence_index=index,
                )
                with self.subTest(name=name):
                    self.assert_blocked(result, "PRIOR_STANDING_SURFACE_INVALID")

    def test_row_contract_tampering_blocks(self) -> None:
        cases: list[tuple[str, list[dict[str, Any]]]] = []
        ledger = copy.deepcopy(list(resolver.EXPECTED_CONDITION_LEDGER)); ledger.pop(); cases.append(("missing", ledger))
        ledger = copy.deepcopy(list(resolver.EXPECTED_CONDITION_LEDGER)); ledger.append(copy.deepcopy(ledger[-1])); cases.append(("duplicate", ledger))
        ledger = copy.deepcopy(list(resolver.EXPECTED_CONDITION_LEDGER)); ledger[0]["condition_id"] = "unknown"; cases.append(("unknown", ledger))
        ledger = copy.deepcopy(list(resolver.EXPECTED_CONDITION_LEDGER)); ledger[0], ledger[1] = ledger[1], ledger[0]; cases.append(("reordered", ledger))
        mutations = (
            ("required_value", 0, "required_value", False),
            ("proposition", 0, "support_proposition", "WRONG"),
            ("limitation", 0, "limitation", "WRONG"),
            ("dependency", 1, "dependency_conditions", []),
            ("ceiling", 0, "dependency_ceiling", "WRONG"),
            ("support_posture", 0, "evaluation_posture", resolver.CONDITION_REQUIRES_BASIS),
            ("basis_class", 8, "required_basis_class", resolver.BASIS_NONE),
            ("compact", 0, "compact_support_boolean", None),
            ("successor", 0, "successor_condition_posture", resolver.CONDITION_REQUIRES_BASIS),
            ("preservation", 0, "prior_posture_preserved", False),
            ("overwrite", 0, "no_overwrite", False),
        )
        for name, index, field, value in mutations:
            ledger = copy.deepcopy(list(resolver.EXPECTED_CONDITION_LEDGER))
            ledger[index][field] = value
            cases.append((name, ledger))
        for name, ledger in cases:
            request = self.new_request(expected_condition_ledger=ledger)
            with self.subTest(name=name), patch.object(resolver, "_read_bytes", side_effect=AssertionError("basis read")):
                self.assert_blocked(self.resolve_current(request))

    def test_no_universalization_or_authenticity_conversion(self) -> None:
        non_meaning = self.recorded_result[NON_MEANING_KEY]
        for field in (
            "body_held_support_is_not_reality_wide_truth",
            "admitted_record_relative_absence_is_not_universal_absence",
            "internal_consistency_is_not_non_forgery",
            "hashes_prove_preservation_not_authorship",
            "receiver_label_is_not_receiver_identity",
            "bounded_admissibility_is_not_global_admissibility",
        ):
            self.assertIs(non_meaning[field], True)
        for field in (
            "all_ten_conditions_established_as_reality_wide_facts",
            "receiver_attestation_non_forgery_established",
            "universal_automation_absence_established",
            "global_receiver_basis_admissibility_established",
            "receiver_identity_established",
            "custody_proven",
        ):
            self.assertIs(self.recorded_result["non_claims"][field], False)

    def test_all_non_claims_false(self) -> None:
        invalid = copy.deepcopy(self.canonical_request); invalid["intent"] = "WRONG"
        results = (
            resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result(),
            self.recorded_result,
            self.resolve_current(invalid),
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_non_claims_false(result)
                operation = result[OPERATION_KEY]
                self.assertTrue(all(operation[field] is False for field in resolver.REQUIRED_FALSE_NON_CLAIMS))

    def test_successful_operation_facts_are_not_nonclaims(self) -> None:
        operation = self.recorded_result[OPERATION_KEY]
        self.assertIs(operation["all_ten_conditions_evaluated"], True)
        self.assertIs(operation["condition_ledger_populated"], True)
        self.assertEqual(operation["condition_result_count"], 10)
        self.assertTrue({"all_ten_conditions_evaluated", "condition_ledger_populated", "condition_result_count"}.isdisjoint(self.recorded_result["non_claims"]))
        self.assert_non_claims_false(self.recorded_result)

    def test_lineage_preservation_posture(self) -> None:
        self.assertEqual(
            self.recorded_result["lineage_preservation_posture"],
            {field: True for field in resolver.LINEAGE_PRESERVATION_FIELDS},
        )

    def test_omission_posture_and_no_complete_material(self) -> None:
        expected = {field: True for field in resolver.OMISSION_POSTURE_FIELDS}
        expected["complete_material_omission_posture"] = True
        self.assertEqual(self.recorded_result["omission_posture"], expected)
        self.assert_no_prohibited_material(self.recorded_result)

    def test_non_meaning_and_blocked_conversions_exact(self) -> None:
        self.assertEqual(self.recorded_result[NON_MEANING_KEY], {field: True for field in resolver.NON_MEANING_FIELDS})
        self.assertEqual(self.recorded_result["blocked_conversions"], list(resolver.BLOCKED_CONVERSIONS))

    def test_checks_deterministic_and_counts_derived(self) -> None:
        first = self.resolve_current(self.canonical_request)
        second = self.resolve_current(self.canonical_request)
        self.assertEqual(first, second)
        self.assertEqual(first[CHECKS_KEY], second[CHECKS_KEY])
        self.assertEqual(first["failed_check_count"], 0)
        self.assert_counts(first)

    def test_summary_is_exact_projection(self) -> None:
        summary = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_summary(self.recorded_result)
        self.assertEqual(summary, self.recorded_result[SUMMARY_KEY])
        self.assertEqual(summary, resolver._summary_from_result(self.recorded_result))
        self.assertEqual(summary["supported_by_admitted_body_held_records_count"], 9)
        self.assertEqual(summary["requires_basis_conditions"], ["forged_receiver_attestation"])
        self.assertIsNone(summary["admissible_future_route"])
        self.assert_no_prohibited_material(summary)

    def test_from_path_equals_direct(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path, _ = self.write_json(Path(directory) / "request.json", self.canonical_request)
            result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_from_path(path, **self.canonical_paths())
        self.assertEqual(result, self.recorded_result)

    def test_writer_accepts_only_valid_completed_recorded_result(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / resolver.CANONICAL_OUTPUT_ROOT.name
            target = output_root / resolver.OUTPUT_FILENAME
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                written = resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result(self.recorded_result)
            self.assertEqual(written, target)
            self.assertTrue(target.is_file())
            raw = target.read_bytes()
            self.assertTrue(raw.endswith(b"\n"))
            self.assertNotIn(b"NaN", raw)
            self.assertEqual(strict_json_bytes(raw), self.recorded_result)
            self.assertEqual([path for path in output_root.rglob("*") if path.is_file()], [target])

    def test_writer_refuses_invalid_results(self) -> None:
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError
        invalid_request = copy.deepcopy(self.canonical_request); invalid_request["intent"] = "WRONG"
        blocked = self.resolve_current(invalid_request)
        cases: list[tuple[str, object]] = [
            ("default", resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result()),
            ("blocked", blocked),
            ("malformed", {"outcome": resolver.OUTCOME_RECORDED}),
        ]
        mutations = (
            ("wrong_outcome", ("outcome",), resolver.OUTCOME_BLOCKED),
            ("wrong_result", ("operation_result",), resolver.OPERATION_RESULT_NOT_EVALUATED),
            ("posture", ("operation_posture", "operation_exhausted"), False),
            ("true_nonclaim", ("non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0]), True),
            ("route", ("admissible_future_route",), "WRONG"),
            ("summary", (SUMMARY_KEY, "outcome"), "WRONG"),
        )
        for name, keys, value in mutations:
            candidate = copy.deepcopy(self.recorded_result)
            self.set_path(candidate, keys, value)
            cases.append((name, candidate))
        failed_check = copy.deepcopy(self.recorded_result)
        failed_check[CHECKS_KEY][0]["passed"] = False
        cases.append(("failed_check", failed_check))
        missing_row = copy.deepcopy(self.recorded_result); missing_row["condition_ledger"].pop(); cases.append(("missing_row", missing_row))
        altered_row = copy.deepcopy(self.recorded_result); altered_row["condition_ledger"][0]["support_proposition"] = "WRONG"; cases.append(("altered_row", altered_row))
        complete = copy.deepcopy(self.recorded_result); complete["complete_candidate_body"] = {"secret": True}; cases.append(("complete_material", complete))
        raw = copy.deepcopy(self.recorded_result); raw["raw_signal_content"] = "RAW"; cases.append(("raw_signal", raw))
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for name, candidate in cases:
                    with self.subTest(name=name), self.assertRaises(error):
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result(candidate)
            self.assertFalse(output_root.exists())

    def test_writer_refuses_noncanonical_path_and_overwrite(self) -> None:
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationOperationV0MinError
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            output_root = base / resolver.CANONICAL_OUTPUT_ROOT.name
            canonical = output_root / resolver.OUTPUT_FILENAME
            paths = (
                output_root / "alternate.json",
                base / "sibling" / resolver.OUTPUT_FILENAME,
                output_root / ".." / "escape.json",
            )
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for path in paths:
                    with self.subTest(path=path), self.assertRaises(error):
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result(self.recorded_result, path)
                canonical.parent.mkdir(parents=True)
                original = b"ORIGINAL\n"
                canonical.write_bytes(original)
                with self.assertRaises(error):
                    resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_result(self.recorded_result)
                self.assertEqual(canonical.read_bytes(), original)
                self.assertEqual([path for path in output_root.rglob("*") if path.is_file()], [canonical])

    def test_no_scan_discovery_archive_signal_network_randomness_or_current_time(self) -> None:
        source = RESOLVER_PATH.read_text(encoding="utf-8")
        tree = ast.parse(source)
        forbidden_imports = {
            "os", "subprocess", "random", "secrets", "socket", "urllib",
            "requests", "http", "zipfile", "tarfile", "glob", "datetime",
        }
        imported: set[str] = set()
        calls: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.append(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    calls.append(node.func.attr)
        self.assertTrue(imported.isdisjoint(forbidden_imports))
        self.assertTrue(set(calls).isdisjoint({"glob", "rglob", "walk", "listdir", "scandir", "iterdir", "now", "utcnow", "today", "getenv", "extract", "extractall", "check_output", "run", "Popen", "system"}))
        self.assertNotIn("os.environ", source)
        self.assertNotIn("subprocess", source)

    def test_result_structure_exact(self) -> None:
        default = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_v0_min_default_result()
        for result in (default, self.recorded_result):
            with self.subTest(outcome=result["outcome"]):
                self.assertEqual(set(result), EXPECTED_TOP_LEVEL_SECTIONS)
                self.assertEqual(set(result["block"]), {"blocked", "code", "block_code", "reason"})
                self.assertEqual(set(result["operation_admissibility_evaluations"]), {
                    "operation_source_and_record_basis_admissibility_evaluation",
                    "operation_scope_and_matter_admissibility_evaluation",
                    "operation_transition_admissibility_evaluation",
                })
                self.assertEqual(set(result[SUMMARY_KEY]), set(resolver._summary_from_result(result)))
                self.assertEqual(set(result["raw_signal_posture"]), set(resolver.RAW_SIGNAL_POSTURE))
                self.assertEqual(set(result["non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
                operation = result[OPERATION_KEY]
                base_fields = {
                    "operation_id", "operation_type", "operation_version", "operation_scope",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_id",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_type",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_version",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_scope",
                    "selected_matter_class", "operation_result", "operation_basis_supplied",
                    "operation_basis_admitted", "evaluation_performed",
                    "heterogeneous_condition_matrix_recorded", "operation_exhausted",
                    "completed_operation_result_posture_count",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_recorded",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_result_recorded",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_performed",
                    "body_held_receiver_answerable_basis_integrity_condition_evaluation_operation_exhausted",
                    "condition_evaluations", "all_ten_conditions_evaluated",
                    "condition_ledger_populated", "condition_result_count",
                    "raw_signal_body_admitted", "raw_signal_body_read_authorized",
                    "signal_morphology_evaluation_authorized",
                    "authenticity_upgrade_from_signal_authorized", "admissible_future_route",
                    "operation_exhaustion_is_not_complete_receiver_answerable_basis",
                    "operation_exhaustion_is_not_presence",
                }
                self.assertEqual(set(operation), base_fields | set(resolver.REQUIRED_FALSE_NON_CLAIMS))

    def test_what_remains_open_is_bounded_and_non_authorizing(self) -> None:
        self.assertEqual(self.recorded_result["what_remains_open"], list(resolver.WHAT_REMAINS_OPEN))
        remaining = set(self.recorded_result["what_remains_open"])
        for item in (
            "operation_tests", "operation_request", "operation_live_result",
            "operation_terminal_summary", "external_authenticity_basis",
            "raw_signal_morphology_under_separate_admission",
            "complete_receiver_answerable_basis", "later_presence_re_evaluation",
            "threshold", "truth_settlement", "field_machinery", "runtime",
            "api", "public_interface", "public_intake", "follow_on_work",
        ):
            self.assertIn(item, remaining)
        self.assertNotIn("completed_boundary", remaining)
        self.assertIsNone(self.recorded_result["admissible_future_route"])
        self.assertIs(self.recorded_result["non_claims"]["follow_on_work_authorized"], False)


if __name__ == "__main__":
    unittest.main()
