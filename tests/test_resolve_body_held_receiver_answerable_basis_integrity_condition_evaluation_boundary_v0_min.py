"""Tests for one body-held ten-condition evaluation consideration boundary.

The suite validates only whether a later heterogeneous evaluation operation may
be considered.  It never evaluates a condition, opens raw signal or archive
bytes, populates the later ledger, writes a live artifact, or changes standing
lineage.  Canonical inputs are read in place; every hostile fixture and writer
exercise is isolated in a temporary directory.
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
from contextlib import ExitStack
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min as resolver


SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
PRIOR_PRESENCE_PATH = REPO_ROOT / resolver.PRIOR_PRESENCE_ARTIFACT_RELATIVE_PATH
SOURCE_ADMISSIBILITY_PATH = (
    REPO_ROOT / resolver.SOURCE_ADMISSIBILITY_BOUNDARY_ARTIFACT_RELATIVE_PATH
)
LATER_MODAL_PATH = REPO_ROOT / resolver.LATER_MODAL_ARTIFACT_RELATIVE_PATH
MODAL_TERMINAL_SUMMARY_PATH = REPO_ROOT / resolver.MODAL_TERMINAL_SUMMARY_RELATIVE_PATH
CARRIAGE_PATHS = tuple(REPO_ROOT / path for path in resolver.CARRIAGE_LINEAGE_RELATIVE_PATHS)
PACKET_TEXT_PATHS = tuple(REPO_ROOT / path for path in resolver.PACKET_TEXT_RELATIVE_PATHS)
CONDUCT_PATHS = tuple(REPO_ROOT / path for path in resolver.SOURCE_BODY_CONDUCT_RELATIVE_PATHS)
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT

BOUNDARY_KEY = resolver.BOUNDARY_KEY
CHECKS_KEY = resolver.CHECKS_KEY
SUMMARY_KEY = resolver.SUMMARY_KEY
NON_MEANING_KEY = resolver.NON_MEANING_KEY
SELECTION_FIELD = (
    "body_held_receiver_answerable_basis_integrity_condition_"
    "evaluation_consideration_selected"
)

EXPECTED_TOP_LEVEL_SECTIONS = {
    "admissibility_evaluations",
    "admissible_future_route",
    "block",
    "blocked_conversions",
    BOUNDARY_KEY,
    CHECKS_KEY,
    resolver.METADATA_KEY,
    NON_MEANING_KEY,
    resolver.STATEMENT_KEY,
    SUMMARY_KEY,
    "boundary_decision",
    "boundary_posture",
    "boundary_result",
    "carriage_lineage_artifact_validations",
    "completed_consideration_posture_count",
    "condition_ledger_schema_contract",
    resolver.DECLARED_REQUEST_KEY,
    "dependency_ceiling_contract",
    "exact_matter_and_evidence_class_posture",
    "excluded_read_posture",
    "failed_check_count",
    "frozen_read_contract_posture",
    "later_modal_artifact_validation",
    "lineage_preservation_posture",
    "modal_terminal_summary_validation",
    "non_claims",
    "omission_posture",
    "outcome",
    "passed_check_count",
    "prior_presence_artifact_validation",
    "raw_signal_considered_but_not_admitted_posture",
    "receiver_packet_text_validations",
    "resolver_module",
    "result_level_non_claims_canonical_false",
    "result_version",
    "source_admissibility_boundary_artifact_validation",
    "source_body_conduct_validations",
    "specification_validation",
    "temporal_evidence_posture",
    "what_remains_open",
}

PROHIBITED_COMPLETE_KEYS = {
    "complete_upstream_artifact",
    "complete_candidate_body",
    "complete_candidate_evaluation_material",
    "raw_accelerometer_body",
    "raw_signal_body",
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


class BodyHeldIntegrityConditionEvaluationBoundaryTests(unittest.TestCase):
    """Verify one closed, non-evaluating ten-condition consideration."""

    @classmethod
    def setUpClass(cls) -> None:
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("canonical boundary output root must be absent")
        cls.governed_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            PRIOR_PRESENCE_PATH,
            SOURCE_ADMISSIBILITY_PATH,
            LATER_MODAL_PATH,
            MODAL_TERMINAL_SUMMARY_PATH,
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
        cls.prior_presence_bytes = PRIOR_PRESENCE_PATH.read_bytes()
        cls.source_admissibility_bytes = SOURCE_ADMISSIBILITY_PATH.read_bytes()
        cls.later_modal_bytes = LATER_MODAL_PATH.read_bytes()
        cls.modal_terminal_summary_bytes = MODAL_TERMINAL_SUMMARY_PATH.read_bytes()
        cls.carriage_bytes = tuple(path.read_bytes() for path in CARRIAGE_PATHS)
        cls.packet_bytes = tuple(path.read_bytes() for path in PACKET_TEXT_PATHS)
        cls.conduct_bytes = tuple(path.read_bytes() for path in CONDUCT_PATHS)
        cls.prior_presence = strict_json_bytes(cls.prior_presence_bytes)
        cls.source_admissibility = strict_json_bytes(cls.source_admissibility_bytes)
        cls.later_modal = strict_json_bytes(cls.later_modal_bytes)
        cls.carriage_artifacts = tuple(strict_json_bytes(raw) for raw in cls.carriage_bytes)
        cls.conduct_artifacts = {
            index: strict_json_bytes(cls.conduct_bytes[index])
            for index in (2, 5, 8)
        }
        cls.canonical_request = cls.new_request()
        cls.allowed_result = cls.resolve_current(cls.canonical_request)
        cls.declined_request = cls.new_request(**{SELECTION_FIELD: False})
        cls.not_allowed_result = cls.resolve_current(cls.declined_request)
        if cls.allowed_result.get("outcome") != resolver.OUTCOME_ALLOWED:
            raise AssertionError("canonical selected execution did not reach ALLOWED")
        if cls.not_allowed_result.get("outcome") != resolver.OUTCOME_NOT_ALLOWED:
            raise AssertionError("canonical declined execution did not reach NOT_ALLOWED")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.governed_hashes.items():
            if not path.is_file() or sha256_path(path) != expected:
                raise AssertionError(f"governed input changed: {path}")
        if CANONICAL_OUTPUT_ROOT.exists():
            raise AssertionError("suite created the canonical boundary output root")

    @staticmethod
    def new_request(**overrides: Any) -> dict[str, Any]:
        return resolver.build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request(
            **copy.deepcopy(overrides)
        )

    @staticmethod
    def canonical_paths() -> dict[str, Any]:
        return {
            "governing_specification_path": SPECIFICATION_PATH,
            "prior_presence_artifact_path": PRIOR_PRESENCE_PATH,
            "source_admissibility_boundary_artifact_path": SOURCE_ADMISSIBILITY_PATH,
            "later_modal_artifact_path": LATER_MODAL_PATH,
            "modal_terminal_summary_path": MODAL_TERMINAL_SUMMARY_PATH,
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
        result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min(
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
    def boundary(result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get(BOUNDARY_KEY)
        if not isinstance(value, dict):
            raise AssertionError("boundary object missing")
        return value

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

    def assert_no_evaluation(self, result: Mapping[str, Any]) -> None:
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["condition_evaluations"],
            {condition: "NOT_EVALUATED" for condition in resolver.REQUIRED_CONDITIONS},
        )
        for field in (
            "condition_ledger_populated",
            "any_condition_evaluated",
            "later_operation_created",
            "later_operation_executed",
            "later_operation_result_selected",
        ):
            self.assertIs(boundary[field], False)
        ledger = result["condition_ledger_schema_contract"]
        self.assertIs(ledger["ledger_rows_populated"], False)
        self.assertIs(ledger["selected_condition_results_emitted"], False)

    def assert_blocked(self, result: Mapping[str, Any], code: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(result.get("boundary_result"), resolver.RESULT_NOT_EVALUATED)
        self.assertEqual(result.get("completed_consideration_posture_count"), 0)
        self.assertIsNone(result.get("admissible_future_route"))
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), resolver.BLOCK_CODES)
        self.assertEqual(block.get("code"), block.get("block_code"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        posture = result["boundary_posture"]
        self.assertIs(posture[BOUNDARY_KEY + "_recorded"], False)
        self.assertIs(posture[BOUNDARY_KEY + "_result_recorded"], False)
        self.assertIs(posture[BOUNDARY_KEY + "_exhausted"], False)
        self.assertTrue(
            all(value == resolver.ADMISSIBILITY_NOT_EVALUATED for value in result["admissibility_evaluations"].values())
        )
        self.assert_non_claims_false(result)
        self.assert_no_evaluation(result)
        self.assert_counts(result)

    def assert_completed(self, result: Mapping[str, Any], *, selected: bool) -> None:
        expected_outcome = resolver.OUTCOME_ALLOWED if selected else resolver.OUTCOME_NOT_ALLOWED
        expected_result = resolver.RESULT_ALLOWED if selected else resolver.RESULT_NOT_ALLOWED
        self.assertEqual(result["outcome"], expected_outcome)
        self.assertEqual(result["boundary_result"], expected_result)
        self.assertEqual(result["failed_check_count"], 0)
        self.assertEqual(result["completed_consideration_posture_count"], 1)
        self.assertIs(result["block"]["blocked"], False)
        self.assertIsNone(result["block"]["code"])
        self.assertTrue(
            all(value == resolver.ADMISSIBILITY_PASSED for value in result["admissibility_evaluations"].values())
        )
        posture = result["boundary_posture"]
        self.assertIs(posture[BOUNDARY_KEY + "_recorded"], True)
        self.assertIs(posture[BOUNDARY_KEY + "_result_recorded"], True)
        self.assertIs(posture[BOUNDARY_KEY + "_exhausted"], True)
        self.assertIs(posture["single_use_only"], True)
        self.assertIs(
            posture[
                "body_held_receiver_answerable_basis_integrity_condition_"
                "evaluation_consideration_allowed"
            ],
            selected,
        )
        self.assertIs(
            posture[
                "body_held_receiver_answerable_basis_integrity_condition_"
                "evaluation_consideration_not_allowed"
            ],
            not selected,
        )
        expected_route = resolver.ADMISSIBLE_FUTURE_ROUTE if selected else None
        self.assertEqual(result["admissible_future_route"], expected_route)
        self.assert_non_claims_false(result)
        self.assert_no_evaluation(result)
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
            return self.resolve_current(self.canonical_request, **paths)

    def test_module_identity_exact_families_and_output_contract(self) -> None:
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min",
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (resolver.OUTCOME_ALLOWED, resolver.OUTCOME_NOT_ALLOWED, resolver.OUTCOME_BLOCKED),
        )
        self.assertEqual(
            resolver.RESULT_FAMILY,
            (resolver.RESULT_ALLOWED, resolver.RESULT_NOT_ALLOWED, resolver.RESULT_NOT_EVALUATED),
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
        self.assertEqual(len(resolver.LATER_OPERATION_RESULT_FAMILY), 2)
        self.assertEqual(
            resolver.OUTPUT_ROOT,
            REPO_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min",
        )
        self.assertEqual(resolver.OUTPUT_ROOT, resolver.CANONICAL_OUTPUT_ROOT)
        self.assertTrue(resolver.OUTPUT_FILENAME.endswith("_v0_min_result.json"))
        for name in (
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request",
            "build_declared_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min",
            "resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_from_path",
            "build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_summary",
            "write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result",
        ):
            self.assertTrue(callable(getattr(resolver, name)))

    def test_exact_ordered_matter_required_values_and_evidence_classes(self) -> None:
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
        self.assertEqual(tuple(resolver.REQUIRED_CONDITION_VALUES), expected)
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
        flattened = tuple(
            condition
            for evidence_class in resolver.EVIDENCE_CLASSES
            for condition in resolver.EVIDENCE_CLASS_CONDITION_MAPPING[evidence_class]
        )
        self.assertEqual(flattened, expected)

    def test_default_result_is_canonical_non_executing_and_no_filesystem_read(self) -> None:
        with patch.object(resolver, "_read_bytes", side_effect=AssertionError("read")):
            default = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result()
            alias = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result()
        self.assertEqual(default, alias)
        self.assert_blocked(default, "NOT_EXECUTED")
        self.assertFalse(default["frozen_read_contract_posture"]["read_contract_closed"])
        self.assertFalse(default["lineage_preservation_posture"]["prior_presence_result_preserved"])

    def test_canonical_request_exact_schema_and_no_semantic_preclaims(self) -> None:
        request = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request()
        second = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_request()
        self.assertEqual(request, second)
        self.assertIsNot(request, second)
        self.assertEqual(set(request), resolver._canonical_request_keys())
        self.assertEqual(len(request), 29)
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertIs(request[SELECTION_FIELD], True)
        self.assertEqual(request["ordered_ten_condition_matter"], list(resolver.REQUIRED_CONDITIONS))
        self.assertEqual(request["carriage_lineage_artifact_paths"], [str(path) for path in resolver.CARRIAGE_LINEAGE_RELATIVE_PATHS])
        self.assertEqual(request["receiver_packet_text_paths"], [str(path) for path in resolver.PACKET_TEXT_RELATIVE_PATHS])
        self.assertEqual(request["source_body_conduct_paths"], [str(path) for path in resolver.SOURCE_BODY_CONDUCT_RELATIVE_PATHS])
        self.assertEqual(set(request["declared_non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(value is False for value in request["declared_non_claims"].values()))
        self.assertTrue(resolver.PROHIBITED_DIRECT_REQUEST_FIELDS.isdisjoint(request))

    def test_valid_selected_canonical_execution_is_allowed(self) -> None:
        result = copy.deepcopy(self.allowed_result)
        self.assert_completed(result, selected=True)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.1.0")
        self.assertEqual(result["boundary_decision"]["decision_code"], resolver.DECISION_CODE_ALLOWED)
        self.assertEqual(result["boundary_decision"]["decision_reason"], resolver.DECISION_REASON_ALLOWED)

    def test_valid_declined_canonical_execution_is_not_allowed(self) -> None:
        result = copy.deepcopy(self.not_allowed_result)
        self.assert_completed(result, selected=False)
        self.assertEqual(result["boundary_decision"]["decision_code"], resolver.DECISION_CODE_NOT_ALLOWED)
        self.assertEqual(result["boundary_decision"]["decision_reason"], resolver.DECISION_REASON_NOT_ALLOWED)

    def test_allowed_and_not_allowed_are_single_use_completed_postures(self) -> None:
        for selected, result in ((True, self.allowed_result), (False, self.not_allowed_result)):
            with self.subTest(selected=selected):
                self.assert_completed(result, selected=selected)
                posture = result["boundary_posture"]
                self.assertIs(posture["single_use_only"], True)
                self.assertIs(posture["boundary_exhaustion_is_not_evaluation"], True)
                self.assertIs(posture["boundary_exhaustion_is_not_complete_receiver_answerable_basis"], True)
                self.assertIs(posture["boundary_exhaustion_is_not_standing_or_presence"], True)

    def test_prior_presence_exact_historical_matrix_preserved(self) -> None:
        validation = self.allowed_result["prior_presence_artifact_validation"]
        self.assertIs(validation["artifact_validated"], True)
        standing = validation["standing"]
        self.assertEqual(standing["historical_condition_matrix"], resolver.HISTORICAL_CONDITION_MATRIX)
        self.assertEqual(standing["historical_requires_basis_conditions"], list(resolver.HISTORICAL_REQUIRES_BASIS_CONDITIONS))
        self.assertEqual(standing["admissible_future_route"], None)
        for field in ("presence_supported", "presence_authorized", "presence_established", "presence_recorded"):
            self.assertIs(standing[field], False)

    def test_later_modal_additive_standing_preserved_without_sibling_upgrade(self) -> None:
        standing = self.allowed_result["later_modal_artifact_validation"]["standing"]
        self.assertEqual(standing["outcome"], "RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_SUPPORTED")
        self.assertEqual(standing["receiver_answerable_basis_refusable_evaluation"], "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE")
        self.assertEqual(standing["receiver_answerable_basis_could_have_been_withheld_evaluation"], "SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE")
        self.assertIs(standing["receiver_answerable_basis_refusable_established"], False)
        self.assertIs(standing["receiver_answerable_basis_could_have_been_withheld_established"], False)
        self.assertEqual(standing["ten_current_target_conditions"], {condition: "NOT_EVALUATED" for condition in resolver.REQUIRED_CONDITIONS})
        self.assertIsNone(standing["admissible_future_route"])

    def test_source_admissibility_boundary_exact_standing_preserved(self) -> None:
        validation = self.allowed_result["source_admissibility_boundary_artifact_validation"]
        self.assertIs(validation["artifact_validated"], True)
        standing = validation["standing"]
        self.assertEqual(standing["outcome"], "RECEIVER_ORIGINATING_MODAL_FACT_SOURCE_ADMISSIBILITY_BOUNDARY_ALLOWED")
        self.assertIs(standing["source_selection_recorded"], True)
        self.assertIs(standing["receiver_origin_preserved"], True)
        self.assertIs(standing["carried_arrival"], True)
        self.assertIs(standing["selected_source_native_standing"], False)
        self.assertIs(standing["jurisdiction_distinction_preserved"], True)
        self.assertIs(standing["source_not_naturalized"], True)

    def test_all_seven_carriage_lineage_artifacts_validate(self) -> None:
        validations = self.allowed_result["carriage_lineage_artifact_validations"]
        self.assertEqual(len(validations), 7)
        for path, expected_digest, validation in zip(CARRIAGE_PATHS, (
            resolver.CANDIDATE_RECEPTION_SHA256,
            resolver.CANDIDATE_EVALUATION_SHA256,
            resolver.CANDIDATE_SUFFICIENCY_SHA256,
            resolver.ATTESTATION_BASIS_DECLARATION_SHA256,
            resolver.ATTESTATION_BASIS_SUPPLY_SHA256,
            resolver.RECEIVER_ATTESTATION_SHA256,
            resolver.RECEIVER_ANSWERABLE_RECEIPT_SHA256,
        ), validations):
            self.assertEqual(sha256_path(path), expected_digest)
            self.assertEqual(validation["observed_sha256"], expected_digest)
            self.assertIs(validation["artifact_validated"], True)
            self.assertIs(validation["standing"]["complete_body_omitted"], True)

    def test_all_eight_packet_text_surfaces_validate_exact_bytes(self) -> None:
        validations = self.allowed_result["receiver_packet_text_validations"]
        self.assertEqual(len(validations), 8)
        for path, raw, text, digest, byte_count, validation in zip(
            PACKET_TEXT_PATHS,
            self.packet_bytes,
            resolver.PACKET_TEXT_CONTENTS,
            resolver.PACKET_TEXT_SHA256,
            resolver.PACKET_TEXT_BYTE_COUNTS,
            validations,
        ):
            self.assertEqual(raw, text.encode("utf-8"))
            self.assertEqual(len(raw), byte_count)
            self.assertEqual(sha256_path(path), digest)
            self.assertEqual(validation["observed_sha256"], digest)
            self.assertEqual(validation["observed_byte_count"], byte_count)
            self.assertIs(validation["surface_validated"], True)

    def test_all_nine_source_body_conduct_surfaces_validate(self) -> None:
        validations = self.allowed_result["source_body_conduct_validations"]
        self.assertEqual(len(validations), 9)
        for path, digest, validation in zip(CONDUCT_PATHS, resolver.SOURCE_BODY_CONDUCT_SHA256, validations):
            self.assertEqual(sha256_path(path), digest)
            self.assertEqual(validation["observed_sha256"], digest)
            self.assertIs(validation["strict_content_validated"], True)
            self.assertIs(validation["bounded_standing_validated"], True)
            self.assertIs(validation["surface_validated"], True)

    def test_frozen_read_contract_exact_and_closed(self) -> None:
        expected_reads = (
            SPECIFICATION_PATH,
            PRIOR_PRESENCE_PATH,
            SOURCE_ADMISSIBILITY_PATH,
            LATER_MODAL_PATH,
            MODAL_TERMINAL_SUMMARY_PATH,
            *CARRIAGE_PATHS,
            *PACKET_TEXT_PATHS,
            *CONDUCT_PATHS,
        )
        observed: list[Path] = []
        original = Path.read_bytes

        def tracked(path: Path) -> bytes:
            observed.append(path.resolve())
            return original(path)

        with patch.object(Path, "read_bytes", tracked):
            result = self.resolve_current(self.canonical_request)
        self.assert_completed(result, selected=True)
        self.assertEqual(observed, [path.resolve() for path in expected_reads])
        posture = result["frozen_read_contract_posture"]
        self.assertEqual(posture["governing_and_current_standing_surface_count"], 5)
        self.assertEqual(posture["carriage_lineage_surface_count"], 7)
        self.assertEqual(posture["receiver_packet_text_surface_count"], 8)
        self.assertEqual(posture["source_body_conduct_surface_count"], 9)
        self.assertIs(posture["no_other_surface_selected"], True)
        self.assertIs(posture["read_contract_closed"], True)

    def test_excluded_read_contract_exact(self) -> None:
        self.assertEqual(
            resolver.EXCLUDED_READ_IDENTIFIERS,
            (
                "RAW_SIGNAL_JSON", "ORIGINAL_ZIP_BYTES", "ARCHIVE_EXTRACTION",
                "COMPLETE_BOUNDED_CAPTURE_SIGNAL_BODY", "COMPLETE_CANDIDATE_BODY",
                "COMPLETE_CANDIDATE_EVALUATION_MATERIAL", "FILESYSTEM_PERMISSIONS",
                "ACL_DATA", "DEVICE_CONTROL_RECORDS", "PRIVATE_COMMUNICATIONS",
                "BROAD_GIT_HISTORY", "BROAD_PR_HISTORY", "SIBLING_DISCOVERY",
                "LATEST_FILE_SELECTION", "ALTERNATIVE_SOURCE_SEARCH",
                "SOURCE_RECONSTRUCTION", "GLOB", "RGLOB", "DIRECTORY_SCAN",
                "UNRELATED_RECEIVER_SIDE_MATERIAL",
            ),
        )
        posture = self.allowed_result["excluded_read_posture"]
        self.assertEqual(posture["excluded_read_identifiers"], list(resolver.EXCLUDED_READ_IDENTIFIERS))
        self.assertTrue(all(posture[field] is False for field in (
            "excluded_reads_performed", "raw_signal_json_opened", "original_zip_bytes_opened",
            "archive_extracted", "glob_used", "rglob_used", "directory_scan_performed",
            "latest_file_selected", "source_reconstructed",
        )))

    def test_raw_signal_is_considered_but_not_admitted(self) -> None:
        self.assertEqual(
            resolver.RAW_SIGNAL_POSTURE,
            {
                "raw_signal_body_known_to_exist": True,
                "raw_signal_body_considered": True,
                "raw_signal_body_admitted": False,
                "raw_signal_body_read_authorized": False,
                "signal_morphology_evaluation_authorized": False,
                "authenticity_upgrade_from_signal_authorized": False,
            },
        )
        observed: list[Path] = []
        original = Path.read_bytes

        def tracked(path: Path) -> bytes:
            observed.append(path.resolve())
            return original(path)

        with patch.object(Path, "read_bytes", tracked):
            result = self.resolve_current(self.canonical_request)
        self.assertTrue(all(path.name != "knock_20260727_215052.json" for path in observed))
        self.assertTrue(all(path.suffix.lower() != ".zip" for path in observed))
        self.assertNotIn("knock_20260727_215052.json", json.dumps(result, sort_keys=True))
        self.assertEqual(result["raw_signal_considered_but_not_admitted_posture"], resolver.RAW_SIGNAL_POSTURE)

    def test_temporal_evidence_exact_and_bounded(self) -> None:
        posture = self.allowed_result["temporal_evidence_posture"]
        self.assertEqual(posture["knock_generated_at"], "2026-07-15T12:08:04Z")
        self.assertEqual(posture["receiver_attestation_confirmed_at"], "2026-07-28T06:37:56Z")
        self.assertEqual(posture["knock_to_receiver_attestation_interval_seconds"], 1_103_392)
        self.assertEqual(posture["knock_to_receiver_attestation_interval_components"], {"days": 12, "hours": 18, "minutes": 29, "seconds": 52})
        self.assertEqual(posture["knock_to_receiver_attestation_interval"], "12 days, 18 hours, 29 minutes, 52 seconds")
        for field in ("actual_withholding_inferred", "actual_refusal_inferred", "receiver_freedom_inferred", "universal_automation_absence_inferred", "current_clock_used"):
            self.assertIs(posture[field], False)

    def test_dependency_ceiling_contract_exact_and_ordered(self) -> None:
        self.assertEqual(self.allowed_result["dependency_ceiling_contract"], list(resolver.DEPENDENCY_CEILING_CONTRACT))
        self.assertEqual(len(resolver.DEPENDENCY_CEILING_CONTRACT), 10)
        self.assertEqual([item["condition_id"] for item in resolver.DEPENDENCY_CEILING_CONTRACT], [
            "same_custody_countersignature", "operator_only_attestation",
            "derivative_rendering_attestation", "generated_affirmation",
            "automatic_acknowledgement", "forged_receiver_attestation",
            "inadmissible_receiver_basis", "ALL_NEGATIVE_FORM_CONDITIONS",
            "ALL_SIBLING_CONDITIONS", "ALL_DEPENDENCIES",
        ])
        self.assert_no_evaluation(self.allowed_result)

    def test_condition_ledger_schema_contract_is_validated_but_not_populated(self) -> None:
        ledger = self.allowed_result["condition_ledger_schema_contract"]
        self.assertEqual(ledger["required_fields"], list(resolver.CONDITION_LEDGER_SCHEMA_FIELDS))
        self.assertEqual(len(ledger["required_fields"]), 17)
        self.assertIs(ledger["ledger_rows_populated"], False)
        self.assertIs(ledger["selected_condition_results_emitted"], False)
        serialized = json.dumps(self.allowed_result, sort_keys=True)
        for field in ("required_basis_selection", "successor_condition_posture_selected"):
            self.assertNotIn(field, serialized)
        self.assert_no_evaluation(self.allowed_result)

    def test_three_part_admissibility_is_all_or_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source_invalid = copy.deepcopy(self.prior_presence)
            source_invalid["outcome"] = "WRONG"
            source_result = self.resolve_mutated_json(
                base=base, fixture_name="source_part.json", artifact=source_invalid,
                path_slot="prior_presence_artifact_path", digest_attribute="PRIOR_PRESENCE_SHA256",
            )
            self.assert_blocked(source_result, "PRIOR_PRESENCE_ARTIFACT_INVALID")

            malformed_mapping = copy.deepcopy(resolver.EVIDENCE_CLASS_CONDITION_MAPPING)
            malformed_mapping[resolver.EVIDENCE_CLASSES[0]] = tuple()
            matter_request = self.new_request(
                evidence_class_condition_mapping={key: list(value) for key, value in malformed_mapping.items()}
            )
            with patch.object(resolver, "EVIDENCE_CLASS_CONDITION_MAPPING", malformed_mapping):
                matter_result = self.resolve_current(matter_request)
            self.assert_blocked(matter_result, "MATTER_CONTRACT_INVALID")

            transition_invalid = copy.deepcopy(self.source_admissibility)
            transition_invalid["lineage_preservation_posture"]["source_not_naturalized"] = False
            transition_result = self.resolve_mutated_json(
                base=base, fixture_name="transition_part.json", artifact=transition_invalid,
                path_slot="source_admissibility_boundary_artifact_path",
                digest_attribute="SOURCE_ADMISSIBILITY_BOUNDARY_SHA256",
            )
            self.assert_blocked(transition_result, "SOURCE_ADMISSIBILITY_ARTIFACT_INVALID")

    def test_invalid_request_schema_blocks_before_basis_use(self) -> None:
        cases: list[tuple[str, dict[str, Any]]] = []
        request = self.new_request(); request.pop("intent"); cases.append(("missing_field", request))
        request = self.new_request(unknown_field=False); cases.append(("unknown_field", request))
        cases.extend((name, self.new_request(**override)) for name, override in (
            ("wrong_intent", {"intent": "WRONG"}),
            ("wrong_identity", {BOUNDARY_KEY + "_id": "wrong"}),
            ("wrong_path", {"prior_presence_re_evaluation_operation_artifact_path": "wrong.json"}),
            ("reversed_paths", {"carriage_lineage_artifact_paths": list(reversed(self.canonical_request["carriage_lineage_artifact_paths"]))}),
            ("narrowed_matter", {"ordered_ten_condition_matter": list(resolver.REQUIRED_CONDITIONS[:-1])}),
            ("broadened_matter", {"ordered_ten_condition_matter": [*resolver.REQUIRED_CONDITIONS, "extra"]}),
            ("changed_value", {"required_condition_values": {**resolver.REQUIRED_CONDITION_VALUES, resolver.REQUIRED_CONDITIONS[0]: False}}),
            ("changed_evidence_class", {"evidence_class_family": [*resolver.EVIDENCE_CLASSES[:-1], "WRONG"]}),
            ("omitted_ceiling", {"dependency_ceiling_contract": copy.deepcopy(list(resolver.DEPENDENCY_CEILING_CONTRACT[:-1]))}),
            ("changed_excluded", {"excluded_read_contract": [*resolver.EXCLUDED_READ_IDENTIFIERS[:-1], "WRONG"]}),
            ("raw_admitted", {"raw_signal_considered_but_not_admitted_posture": {**resolver.RAW_SIGNAL_POSTURE, "raw_signal_body_admitted": True}}),
            ("raw_read", {"raw_signal_considered_but_not_admitted_posture": {**resolver.RAW_SIGNAL_POSTURE, "raw_signal_body_read_authorized": True}}),
            ("condition_result", {resolver.REQUIRED_CONDITIONS[0]: True}),
            ("support_boolean", {"compact_support_boolean": True}),
            ("operation_result", {"operation_result": "RECORDED"}),
            ("custody_proof", {"custody_proof": True}),
            ("receiver_identity", {"receiver_identity": "receiver"}),
            ("authenticity", {"non_forgery_result": True}),
            ("universal_absence", {"universal_absence": True}),
            ("global_admissibility", {"global_admissibility": True}),
            ("presence", {"presence": True}),
            ("semantic_payload", {"semantic_payload": {"x": 1}}),
        ))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims.pop(next(iter(nonclaims))); cases.append(("nonclaim_missing", self.new_request(declared_non_claims=nonclaims)))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims["unknown"] = False; cases.append(("nonclaim_unknown", self.new_request(declared_non_claims=nonclaims)))
        key = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims[key] = 0; cases.append(("nonclaim_nonbool", self.new_request(declared_non_claims=nonclaims)))
        nonclaims = copy.deepcopy(self.canonical_request["declared_non_claims"]); nonclaims[key] = True; cases.append(("nonclaim_true", self.new_request(declared_non_claims=nonclaims)))
        for name, invalid in cases:
            with self.subTest(name=name), patch.object(resolver, "_read_bytes", side_effect=AssertionError("basis read")):
                result = self.resolve_current(invalid)
                self.assert_blocked(result)

    def test_duplicate_key_request_json_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_bytes(Path(directory) / "duplicate.json", b'{"intent":"a","intent":"b"}\n')
            result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_from_path(path, **self.canonical_paths())
            self.assert_blocked(result, "REQUEST_JSON_INVALID")
        self.assertFalse(CANONICAL_OUTPUT_ROOT.exists())

    def test_non_object_malformed_and_nonfinite_request_json_blocks(self) -> None:
        payloads = (b"[]", b'"text"', b"7", b"true", b"null", b"{", b'{"value":NaN}', b'{"value":Infinity}', b'{"value":-Infinity}')
        with tempfile.TemporaryDirectory() as directory:
            for index, raw in enumerate(payloads):
                with self.subTest(index=index, raw=raw):
                    path = self.write_bytes(Path(directory) / f"request_{index}.json", raw)
                    result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_from_path(path, **self.canonical_paths())
                    self.assert_blocked(result, "REQUEST_JSON_INVALID")

    def test_each_pinned_json_digest_mismatch_blocks(self) -> None:
        cases: list[tuple[str, bytes, str, int | None]] = [
            ("prior_presence_artifact_path", self.prior_presence_bytes, "direct", None),
            ("source_admissibility_boundary_artifact_path", self.source_admissibility_bytes, "direct", None),
            ("later_modal_artifact_path", self.later_modal_bytes, "direct", None),
        ]
        cases.extend(("carriage_lineage_paths", raw, "sequence", index) for index, raw in enumerate(self.carriage_bytes))
        cases.extend(("source_body_conduct_paths", self.conduct_bytes[index], "sequence", index) for index in (2, 5, 8))
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for case_index, (slot, raw, kind, index) in enumerate(cases):
                with self.subTest(slot=slot, index=index):
                    path = self.write_bytes(base / f"json_digest_{case_index}.json", raw + b" ")
                    paths = self.canonical_paths()
                    if kind == "direct":
                        paths[slot] = path
                    else:
                        values = list(paths[slot]); values[index] = path; paths[slot] = tuple(values)
                    result = self.resolve_current(self.canonical_request, **paths)
                    self.assert_blocked(result)

    def test_each_pinned_text_digest_mismatch_blocks(self) -> None:
        cases: list[tuple[str, bytes, int | None]] = [
            ("governing_specification_path", self.specification_bytes, None),
            ("modal_terminal_summary_path", self.modal_terminal_summary_bytes, None),
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
                    result = self.resolve_current(self.canonical_request, **paths)
                    self.assert_blocked(result)

    def test_duplicate_key_each_governed_json_blocks(self) -> None:
        cases: list[tuple[str, bytes, int | None]] = [
            ("prior_presence_artifact_path", self.prior_presence_bytes, None),
            ("source_admissibility_boundary_artifact_path", self.source_admissibility_bytes, None),
            ("later_modal_artifact_path", self.later_modal_bytes, None),
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
                    result = self.resolve_current(self.canonical_request, **paths)
                    self.assert_blocked(result)
                    self.assert_no_prohibited_material(result)

    def test_packet_text_strictness_blocks_normalization(self) -> None:
        first = self.packet_bytes[0]
        lines = first.decode("utf-8").splitlines(keepends=True)
        variants = {
            "bom": b"\xef\xbb\xbf" + first,
            "invalid_utf8": first + b"\xff",
            "byte_count": first + b" ",
            "changed_newline": first.rstrip(b"\n") + b"\r\n",
            "reordered_lines": "".join(reversed(lines)).encode("utf-8"),
            "duplicate_key": first + lines[0].encode("utf-8") if isinstance(lines[0], str) else first + lines[0],
            "missing_key": lines[0].encode("utf-8") if isinstance(lines[0], str) else lines[0],
            "unknown_key": first + b"unknown=value\n",
            "blank_line": first + b"\n",
            "malformed_record": first + b"malformed\n",
            "whitespace_normalization": first.replace(b"=", b" = ", 1),
        }
        variants["changed_timestamp"] = self.packet_bytes[2].replace(b"2026-07-28", b"2026-07-29")
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, raw in variants.items():
                with self.subTest(name=name):
                    index = 2 if name == "changed_timestamp" else 0
                    path = self.write_bytes(base / name / "packet.txt", raw)
                    paths = self.canonical_paths()
                    values = list(paths["receiver_packet_text_paths"]); values[index] = path
                    paths["receiver_packet_text_paths"] = tuple(values)
                    self.assert_blocked(self.resolve_current(self.canonical_request, **paths))
            for index, raw in enumerate(self.packet_bytes):
                with self.subTest(surface=index):
                    path = self.write_bytes(base / f"surface_{index}" / "packet.txt", raw + b" ")
                    paths = self.canonical_paths()
                    values = list(paths["receiver_packet_text_paths"]); values[index] = path
                    paths["receiver_packet_text_paths"] = tuple(values)
                    self.assert_blocked(self.resolve_current(self.canonical_request, **paths))

    def test_prior_presence_mismatch_blocks(self) -> None:
        cases = (
            ("wrong_outcome", ("outcome",), "WRONG"),
            ("wrong_result", ("presence_re_evaluation_operation_result",), "WRONG"),
            ("wrong_count", ("passed_check_count",), 408),
            ("blocked", ("block", "blocked"), True),
            ("unexhausted", ("operation_posture", "presence_re_evaluation_operation_exhausted"), False),
            ("route", ("admissible_future_route",), "WRONG"),
            ("presence_true", ("presence_re_evaluation_operation", "presence_supported"), True),
            ("matrix_changed", ("condition_evaluations", resolver.REQUIRED_CONDITIONS[0], "evaluation"), "SATISFIED"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, keys, value in cases:
                artifact = copy.deepcopy(self.prior_presence); self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(base=base, fixture_name=name + ".json", artifact=artifact, path_slot="prior_presence_artifact_path", digest_attribute="PRIOR_PRESENCE_SHA256")
                with self.subTest(name=name): self.assert_blocked(result, "PRIOR_PRESENCE_ARTIFACT_INVALID")
            for name, mutator in (
                ("matrix_missing", lambda value: value["condition_evaluations"].pop(resolver.REQUIRED_CONDITIONS[0])),
                ("matrix_cardinality", lambda value: value["condition_evaluations"].update({"extra": {"evaluation": "REQUIRES_BASIS"}})),
            ):
                artifact = copy.deepcopy(self.prior_presence); mutator(artifact)
                result = self.resolve_mutated_json(base=base, fixture_name=name + ".json", artifact=artifact, path_slot="prior_presence_artifact_path", digest_attribute="PRIOR_PRESENCE_SHA256")
                with self.subTest(name=name): self.assert_blocked(result, "PRIOR_PRESENCE_ARTIFACT_INVALID")

    def test_modal_later_standing_mismatch_blocks(self) -> None:
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", ("operation_result",), "WRONG"),
            ("failures", ("failed_check_count",), 1),
            ("count", ("passed_check_count",), 377),
            ("blocked", ("block", "blocked"), True),
            ("unexhausted", ("operation_posture", "receiver_originating_modal_fact_evaluation_operation_exhausted"), False),
            ("route", ("admissible_future_route",), "WRONG"),
            ("evaluation", ("receiver_originating_modal_fact_evaluation_operation", "receiver_answerable_basis_refusable_evaluation"), "REQUIRES_BASIS"),
            ("support", ("receiver_originating_modal_fact_evaluation_operation", "receiver_answerable_basis_refusable_supported"), False),
            ("establishment", ("receiver_originating_modal_fact_evaluation_operation", "receiver_answerable_basis_refusable_established"), True),
            ("excluded", ("excluded_condition_posture", "condition_evaluations", resolver.REQUIRED_CONDITIONS[0]), "SUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, keys, value in cases:
                artifact = copy.deepcopy(self.later_modal); self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(base=base, fixture_name=name + ".json", artifact=artifact, path_slot="later_modal_artifact_path", digest_attribute="LATER_MODAL_SHA256")
                with self.subTest(name=name): self.assert_blocked(result, "LATER_MODAL_ARTIFACT_INVALID")

    def test_source_admissibility_mismatch_blocks(self) -> None:
        bkey = "receiver_originating_modal_fact_source_admissibility_boundary"
        cases = (
            ("outcome", ("outcome",), "WRONG"),
            ("result", ("boundary_result",), "WRONG"),
            ("admissibility", ("admissibility_evaluations", "source_admissibility_evaluation"), "NOT_EVALUATED"),
            ("origin", (bkey, "selected_source_origin"), "WRONG"),
            ("arrival", (bkey, "selected_source_arrival_posture"), "WRONG"),
            ("native", (bkey, "selected_source_native_standing"), True),
            ("jurisdiction", (bkey, "jurisdiction_distinction_preserved"), False),
            ("naturalized", ("lineage_preservation_posture", "source_not_naturalized"), False),
            ("completion", (bkey, "receiver_originating_modal_fact_source_admissibility_boundary_exhausted"), False),
            ("cardinality", (bkey, "completed_consideration_posture_count"), 2),
            ("route", ("admissible_future_route",), "WRONG"),
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for name, keys, value in cases:
                artifact = copy.deepcopy(self.source_admissibility); self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(base=base, fixture_name=name + ".json", artifact=artifact, path_slot="source_admissibility_boundary_artifact_path", digest_attribute="SOURCE_ADMISSIBILITY_BOUNDARY_SHA256")
                with self.subTest(name=name): self.assert_blocked(result, "SOURCE_ADMISSIBILITY_ARTIFACT_INVALID")

    def test_carriage_identity_correspondence_completion_and_false_locks_block(self) -> None:
        cases = (
            (0, ("receiver_side_answerable_basis_reception_operation", "receiver_side_answerable_basis_candidate_id"), "wrong", "candidate_identity"),
            (0, ("receiver_side_answerable_basis_reception_operation", "candidate_source_provenance_reference_supplied"), False, "correspondence"),
            (1, ("outcome",), "WRONG", "result"),
            (2, ("receiver_side_answerable_basis_candidate_sufficiency_operation", "candidate_sufficiency_operation_exhausted"), False, "completion"),
            (5, ("operation_result_detail", "completed_result_posture_count"), 2, "cardinality"),
            (3, ("failed_check_count",), 1, "failed_checks"),
            (4, ("block", "blocked"), True, "blocked"),
            (6, ("receiver_side_answerable_basis_receiver_answerable_receipt_operation", "presence_supported"), True, "false_lock"),
        )
        digest_attributes = (
            "CANDIDATE_RECEPTION_SHA256", "CANDIDATE_EVALUATION_SHA256",
            "CANDIDATE_SUFFICIENCY_SHA256", "ATTESTATION_BASIS_DECLARATION_SHA256",
            "ATTESTATION_BASIS_SUPPLY_SHA256", "RECEIVER_ATTESTATION_SHA256",
            "RECEIVER_ANSWERABLE_RECEIPT_SHA256",
        )
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            for index, keys, value, name in cases:
                artifact = copy.deepcopy(self.carriage_artifacts[index]); self.set_path(artifact, keys, value)
                result = self.resolve_mutated_json(base=base, fixture_name=name + ".json", artifact=artifact, path_slot="carriage_lineage_paths", digest_attribute=digest_attributes[index], sequence_index=index)
                with self.subTest(name=name): self.assert_blocked(result, "CARRIAGE_LINEAGE_ARTIFACT_INVALID")

    def test_source_body_conduct_is_not_external_fact_proof(self) -> None:
        non_meaning = self.allowed_result[NON_MEANING_KEY]
        self.assertIs(non_meaning["source_body_non_prescription_is_not_no_external_pressure"], True)
        self.assertIs(non_meaning["source_body_non_generation_is_not_no_external_generation"], True)
        self.assertIs(self.allowed_result["frozen_read_contract_posture"]["broad_availability_is_not_permission"], True)
        self.assert_no_evaluation(self.allowed_result)

    def test_hashes_and_internal_consistency_do_not_create_non_forgery(self) -> None:
        self.assertIs(self.allowed_result[NON_MEANING_KEY]["hashes_prove_preservation_not_authorship"], True)
        self.assertIs(self.allowed_result[NON_MEANING_KEY]["internal_consistency_is_not_non_forgery"], True)
        self.assertIs(self.allowed_result["non_claims"]["receiver_attestation_non_forgery_established"], False)
        self.assertNotIn("authenticity_result", json.dumps(self.allowed_result, sort_keys=True))
        self.assert_no_evaluation(self.allowed_result)

    def test_all_required_non_claims_are_false(self) -> None:
        blocked_request = self.new_request(); blocked_request["intent"] = "WRONG"
        results = (
            resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result(),
            self.allowed_result,
            self.not_allowed_result,
            self.resolve_current(blocked_request),
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_non_claims_false(result)

    def test_lineage_preservation_posture(self) -> None:
        for result in (self.allowed_result, self.not_allowed_result):
            with self.subTest(outcome=result["outcome"]):
                lineage = result["lineage_preservation_posture"]
                self.assertEqual(set(lineage), set(resolver.LINEAGE_PRESERVATION_FIELDS))
                self.assertTrue(all(value is True for value in lineage.values()))
                self.assertIs(lineage["prior_presence_result_preserved"], True)
                self.assertIs(lineage["later_two_source_supported_modal_evaluations_preserved"], True)
                self.assertIs(lineage["both_modal_establishment_fields_remain_false"], True)
                self.assertIs(lineage["source_not_naturalized"], True)
                self.assertIs(lineage["contaminated_lineage_unchanged"], True)

    def test_omission_posture_and_no_prohibited_material(self) -> None:
        for result in (self.allowed_result, self.not_allowed_result):
            with self.subTest(outcome=result["outcome"]):
                omission = result["omission_posture"]
                self.assertEqual(set(omission), set(resolver.OMISSION_POSTURE_FIELDS))
                self.assertTrue(all(value is True for value in omission.values()))
                self.assert_no_prohibited_material(result)
                serialized = json.dumps(result, sort_keys=True)
                self.assertNotIn("knock_20260727_215052.json", serialized)
                self.assertNotIn("receiver_attestation_001.zip", serialized)

    def test_non_meaning_and_blocked_conversions_exact(self) -> None:
        for result in (self.allowed_result, self.not_allowed_result):
            self.assertEqual(result[NON_MEANING_KEY], {field: True for field in resolver.NON_MEANING_FIELDS})
            self.assertEqual(result["blocked_conversions"], list(resolver.BLOCKED_CONVERSIONS))
            self.assert_no_evaluation(result)
            self.assertIs(result["non_claims"]["follow_on_work_authorized"], False)

    def test_checks_are_deterministic_and_counts_derived(self) -> None:
        first = self.resolve_current(self.canonical_request)
        second = self.resolve_current(self.canonical_request)
        self.assertEqual(first, second)
        self.assertEqual(first[CHECKS_KEY], second[CHECKS_KEY])
        self.assert_counts(first)
        self.assertEqual(first["failed_check_count"], 0)

    def test_summary_is_exact_projection(self) -> None:
        for result in (self.allowed_result, self.not_allowed_result):
            summary = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_summary(result)
            self.assertEqual(summary, result[SUMMARY_KEY])
            self.assert_no_prohibited_material(summary)
            self.assertIs(summary["all_ten_conditions_not_evaluated"], True)
            self.assertIs(summary["later_operation_not_created_or_executed"], True)

    def test_from_path_equals_direct_for_allowed_and_not_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for selected, request, direct in (
                (True, self.canonical_request, self.allowed_result),
                (False, self.declined_request, self.not_allowed_result),
            ):
                with self.subTest(selected=selected):
                    path, _ = self.write_json(Path(directory) / f"request_{selected}.json", request)
                    result = resolver.resolve_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_from_path(path, **self.canonical_paths())
                    self.assertEqual(result, direct)

    def test_writer_accepts_valid_completed_allowed_and_not_allowed_only(self) -> None:
        for selected, result in ((True, self.allowed_result), (False, self.not_allowed_result)):
            with self.subTest(selected=selected), tempfile.TemporaryDirectory() as directory:
                output_root = Path(directory) / resolver.CANONICAL_OUTPUT_ROOT.name
                target = output_root / resolver.OUTPUT_FILENAME
                with patch.object(resolver, "OUTPUT_ROOT", output_root):
                    written = resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(result)
                self.assertEqual(written, target)
                self.assertTrue(target.is_file())
                self.assertEqual(strict_json_bytes(target.read_bytes()), result)
                raw = target.read_bytes()
                self.assertTrue(raw.endswith(b"\n"))
                self.assertNotIn(b"NaN", raw)
                self.assertEqual([path for path in output_root.rglob("*") if path.is_file()], [target])

    def test_writer_refuses_default_blocked_inconsistent_and_prohibited_results(self) -> None:
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError
        blocked_request = self.new_request(); blocked_request["intent"] = "WRONG"
        blocked = self.resolve_current(blocked_request)
        cases: list[tuple[str, object]] = [
            ("default", resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result()),
            ("blocked", blocked),
            ("malformed", {"outcome": resolver.OUTCOME_ALLOWED}),
        ]
        mutations = (
            ("outcome_pair", ("boundary_result",), resolver.RESULT_NOT_ALLOWED),
            ("posture", ("boundary_posture", BOUNDARY_KEY + "_exhausted"), False),
            ("failed_check", (CHECKS_KEY, "0", "passed"), False),
            ("true_nonclaim", ("non_claims", resolver.REQUIRED_FALSE_NON_CLAIMS[0]), True),
            ("wrong_route", ("admissible_future_route",), "WRONG"),
            ("changed_summary", (SUMMARY_KEY, "outcome"), "WRONG"),
            ("condition_evaluation", (BOUNDARY_KEY, "condition_evaluations", resolver.REQUIRED_CONDITIONS[0]), "SUPPORTED_BY_ADMITTED_BODY_HELD_RECORDS"),
            ("raw_signal", ("raw_signal_considered_but_not_admitted_posture", "raw_signal_body"), "RAW"),
        )
        for name, keys, value in mutations:
            candidate = copy.deepcopy(self.allowed_result)
            if keys[0] == CHECKS_KEY:
                candidate[CHECKS_KEY][0][keys[2]] = value
            else:
                self.set_path(candidate, keys, value)
            cases.append((name, candidate))
        operation_result = copy.deepcopy(self.allowed_result); operation_result["operation_result"] = "RECORDED"; cases.append(("operation_result", operation_result))
        complete = copy.deepcopy(self.allowed_result); complete["complete_candidate_body"] = {"secret": True}; cases.append(("complete_body", complete))
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / resolver.CANONICAL_OUTPUT_ROOT.name
            with patch.object(resolver, "OUTPUT_ROOT", output_root):
                for name, candidate in cases:
                    with self.subTest(name=name), self.assertRaises(error):
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(candidate)
            self.assertFalse(output_root.exists())

    def test_writer_refuses_noncanonical_path_and_overwrite(self) -> None:
        error = resolver.BodyHeldReceiverAnswerableBasisIntegrityConditionEvaluationBoundaryV0MinError
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
                        resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(self.allowed_result, path)
                canonical.parent.mkdir(parents=True)
                original = b"ORIGINAL\n"; canonical.write_bytes(original)
                with self.assertRaises(error):
                    resolver.write_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_result(self.allowed_result)
                self.assertEqual(canonical.read_bytes(), original)
                self.assertEqual([path for path in output_root.rglob("*") if path.is_file()], [canonical])

    def test_no_scan_discovery_archive_signal_network_randomness_or_current_time(self) -> None:
        source = RESOLVER_PATH.read_text(encoding="utf-8")
        tree = ast.parse(source)
        forbidden_imports = {"os", "subprocess", "random", "socket", "urllib", "requests", "zipfile", "tarfile", "glob"}
        imported = set()
        calls = []
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
        self.assertTrue(set(calls).isdisjoint({"glob", "rglob", "walk", "listdir", "iterdir", "now", "utcnow", "today", "getenv", "extract", "extractall", "check_output", "run", "Popen"}))
        self.assertNotIn("os.environ", source)
        self.assertNotIn("knock_20260727_215052.json\").read", source)
        self.assertIn("datetime.fromisoformat", source)

    def test_result_structure_exact_section_set(self) -> None:
        default = resolver.build_body_held_receiver_answerable_basis_integrity_condition_evaluation_boundary_v0_min_default_result()
        for result in (default, self.allowed_result, self.not_allowed_result):
            with self.subTest(outcome=result["outcome"]):
                self.assertEqual(set(result), EXPECTED_TOP_LEVEL_SECTIONS)
                self.assertEqual(set(result["admissibility_evaluations"]), {
                    "source_and_record_basis_admissibility_evaluation",
                    "scope_and_matter_admissibility_evaluation",
                    "transition_admissibility_evaluation",
                })
                self.assertEqual(set(result[SUMMARY_KEY]), set(resolver._summary_from_result(result)))

    def test_what_remains_open_is_bounded_and_non_authorizing(self) -> None:
        self.assertEqual(self.allowed_result["what_remains_open"], list(resolver.WHAT_REMAINS_OPEN))
        open_items = set(self.allowed_result["what_remains_open"])
        self.assertNotIn("boundary_resolver", open_items)
        for required in (
            "boundary_tests", "boundary_request", "boundary_live_result", "boundary_terminal_summary",
            "separate_heterogeneous_ten_condition_operation_specification",
            "separate_heterogeneous_ten_condition_operation_resolver",
            "separate_heterogeneous_ten_condition_operation_tests",
            "all_ten_actual_condition_evaluations", "external_authenticity_basis",
            "raw_signal_morphology_under_separate_admitting_surface",
            "complete_receiver_answerable_basis", "later_presence_re_evaluation",
            "threshold_and_truth_settlement", "repair_validation_and_follow_on_work",
        ):
            self.assertIn(required, open_items)
        self.assertIs(self.allowed_result["non_claims"]["follow_on_work_authorized"], False)
        self.assertIs(self.allowed_result["non_claims"]["automatic_next_step_created"], False)


if __name__ == "__main__":
    unittest.main()
