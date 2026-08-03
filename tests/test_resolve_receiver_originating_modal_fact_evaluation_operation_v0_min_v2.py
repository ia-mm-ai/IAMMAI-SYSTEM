"""Current-state tests for the completed receiver-originating modal-fact evaluation operation line.

V1 is the preserved pre-live witness; v2 is the additive post-live witness.
Both remain append-only lineage, and v2 does not import, execute, invalidate, or
replace v1. The canonical artifact is read-only, current-state re-execution is
deterministic, supported source evaluation remains non-establishment, no future
route is created, and open does not mean next.
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


V2_TEST_PATH = Path(__file__).resolve()
V1_TEST_PATH = REPO_ROOT / (
    "tests/test_resolve_receiver_originating_modal_fact_evaluation_"
    "operation_v0_min.py"
)
SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPECIFICATION_RELATIVE_PATH
RESOLVER_PATH = Path(resolver.__file__).resolve()
TERMINAL_SUMMARY_PATH = REPO_ROOT / (
    "spec/RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_"
    "V0_MIN_TERMINAL_SUMMARY.md"
)
BOUNDARY_PATH = REPO_ROOT / resolver.BOUNDARY_ARTIFACT_RELATIVE_PATH
DECLARATION_PATH = REPO_ROOT / resolver.DECLARATION_SURFACE_RELATIVE_PATH
CANDIDATE_PATH = REPO_ROOT / resolver.CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH
ATTESTATION_PATH = REPO_ROOT / resolver.RECEIVER_ATTESTATION_ARTIFACT_RELATIVE_PATH
RECEIPT_PATH = REPO_ROOT / resolver.RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_RELATIVE_PATH
CANONICAL_OUTPUT_ROOT = resolver.CANONICAL_OUTPUT_ROOT
LIVE_ARTIFACT_PATH = CANONICAL_OUTPUT_ROOT / resolver.OUTPUT_FILENAME

EXPECTED_LIVE_SHA256 = (
    "5138294e3c9d5f776676afb580b786fc1d6a5518527add7808789be3a744ba57"
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
EXPECTED_DECLARATION_RECORDS = {
    "freely_given": "true",
    "could_have_been_refused": "true",
    "could_have_been_withheld": "true",
    "prescribed_by_declaring_side": "false",
    "attestation_words_authored_by_receiver_only": "true",
    "confirmed_by_receiver_at": "2026-07-28T06:37:56Z",
}
OPERATION_KEY = "receiver_originating_modal_fact_evaluation_operation"
CHECKS_KEY = OPERATION_KEY + "_checks"
SUMMARY_KEY = OPERATION_KEY + "_summary"
NON_MEANING_KEY = OPERATION_KEY + "_non_meaning"


class DuplicateJsonKeyError(ValueError):
    """Raised by the independent strict JSON loader on duplicate keys."""


def reject_duplicate_json_keys(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ReceiverOriginatingModalFactEvaluationOperationCurrentStateTests(
    unittest.TestCase
):
    """Validate the standing post-live operation without changing it."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.protected_paths = (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            V1_TEST_PATH,
            TERMINAL_SUMMARY_PATH,
            LIVE_ARTIFACT_PATH,
            BOUNDARY_PATH,
            DECLARATION_PATH,
            CANDIDATE_PATH,
            ATTESTATION_PATH,
            RECEIPT_PATH,
        )
        for path in cls.protected_paths:
            if not path.is_file():
                raise AssertionError(f"required current-state file missing: {path}")
        if not CANONICAL_OUTPUT_ROOT.is_dir():
            raise AssertionError("canonical output root is not a directory")
        cls.protected_hashes = {path: sha256(path) for path in cls.protected_paths}
        if cls.protected_hashes[LIVE_ARTIFACT_PATH] != EXPECTED_LIVE_SHA256:
            raise AssertionError("canonical live artifact digest mismatch")
        cls.output_root_stat = cls.directory_stat(CANONICAL_OUTPUT_ROOT)
        cls.live_bytes = LIVE_ARTIFACT_PATH.read_bytes()
        cls.live_artifact = strict_json_bytes(cls.live_bytes)
        cls.specification_bytes = SPECIFICATION_PATH.read_bytes()
        cls.boundary_bytes = BOUNDARY_PATH.read_bytes()
        cls.declaration_bytes = DECLARATION_PATH.read_bytes()
        cls.candidate_bytes = CANDIDATE_PATH.read_bytes()
        cls.attestation_bytes = ATTESTATION_PATH.read_bytes()
        cls.receipt_bytes = RECEIPT_PATH.read_bytes()
        cls.canonical_request = (
            resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_request()
        )
        cls.current_result = cls.resolve_current(cls.canonical_request)
        if cls.current_result != cls.live_artifact:
            raise AssertionError("current resolver result differs from live artifact")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls.protected_hashes.items():
            if not path.is_file() or sha256(path) != expected:
                raise AssertionError(f"protected current-state file changed: {path}")
        if cls.directory_stat(CANONICAL_OUTPUT_ROOT) != cls.output_root_stat:
            raise AssertionError("canonical output directory changed")

    @staticmethod
    def directory_stat(path: Path) -> tuple[int, int, int, int]:
        status = path.stat()
        return (status.st_mode, status.st_size, status.st_mtime_ns, status.st_ctime_ns)

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

    @classmethod
    def resolve_current(
        cls,
        request: object | None = None,
        **path_overrides: Path,
    ) -> dict[str, Any]:
        supplied = (
            resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_request()
            if request is None
            else copy.deepcopy(request)
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

    def operation(self, result: Mapping[str, Any]) -> dict[str, Any]:
        operation = result.get(OPERATION_KEY)
        self.assertIsInstance(operation, dict)
        return operation

    def checks(self, result: Mapping[str, Any]) -> list[dict[str, Any]]:
        checks = result.get(CHECKS_KEY)
        self.assertIsInstance(checks, list)
        self.assertTrue(all(isinstance(check, dict) for check in checks))
        return checks

    def assert_counts(self, result: Mapping[str, Any]) -> None:
        checks = self.checks(result)
        passed = sum(check.get("passed") is True for check in checks)
        failed = sum(check.get("passed") is False for check in checks)
        self.assertEqual(result.get("passed_check_count"), passed)
        self.assertEqual(result.get("failed_check_count"), failed)
        self.assertEqual(len(checks), passed + failed)

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
        self.assertEqual(block.get("code"), block.get("block_code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if code is not None:
            self.assertEqual(block.get("code"), code)
        operation = self.operation(result)
        self.assertIs(operation["operation_basis_admitted"], False)
        self.assertIs(
            operation["receiver_originating_modal_fact_evaluation_performed"],
            False,
        )
        self.assertEqual(
            operation["completed_modal_fact_evaluation_result_posture_count"],
            0,
        )
        for target in EXPECTED_TARGETS:
            self.assertEqual(
                result["target_condition_evaluations"][target]["evaluation"],
                resolver.TARGET_EVALUATION_NOT_EVALUATED,
            )
            self.assertIs(operation[target + "_supported"], False)
        self.assertIsNone(result["admissible_future_route"])
        self.assert_counts(result)
        self.assertGreater(result["failed_check_count"], 0)
        self.assertTrue(all(value is False for value in result["non_claims"].values()))

    def assert_completed(
        self,
        result: Mapping[str, Any],
        outcome: str,
        operation_result: str,
    ) -> None:
        self.assertEqual(result["outcome"], outcome)
        self.assertEqual(result["operation_result"], operation_result)
        self.assertEqual(result["failed_check_count"], 0)
        self.assertIs(result["block"]["blocked"], False)
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
            self.assertIs(operation[field], True)
        self.assertEqual(result["completed_modal_fact_evaluation_result_posture_count"], 1)
        self.assertIsNone(result["admissible_future_route"])
        self.assertTrue(all(value is False for value in result["non_claims"].values()))

    def branch_result(self, evaluations: Mapping[str, str]) -> dict[str, Any]:
        outcome = resolver._outcome_from_evaluations(evaluations)
        checks: list[dict[str, Any]] = []
        if outcome in {
            resolver.OUTCOME_SUPPORTED,
            resolver.OUTCOME_REQUIRES_BASIS,
            resolver.OUTCOME_INDETERMINATE,
        }:
            resolver._append_completed_checks(checks, outcome, evaluations)
        base = self.live_artifact
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
            candidate_validation=base["candidate_sufficiency_artifact_validation"],
            attestation_validation=base["receiver_attestation_artifact_validation"],
            receipt_validation=base[
                "receiver_answerable_receipt_artifact_validation"
            ],
            atomic_basis=base["atomic_operation_basis_posture"],
            evaluations=evaluations,
        )

    @staticmethod
    def recursive_keys(value: Any) -> set[str]:
        keys: set[str] = set()
        if isinstance(value, Mapping):
            for key, item in value.items():
                keys.add(str(key))
                keys.update(
                    ReceiverOriginatingModalFactEvaluationOperationCurrentStateTests.recursive_keys(
                        item
                    )
                )
        elif isinstance(value, list):
            for item in value:
                keys.update(
                    ReceiverOriginatingModalFactEvaluationOperationCurrentStateTests.recursive_keys(
                        item
                    )
                )
        return keys

    def test_current_state_required_files_exist(self) -> None:
        for path in (
            SPECIFICATION_PATH,
            RESOLVER_PATH,
            V1_TEST_PATH,
            TERMINAL_SUMMARY_PATH,
            LIVE_ARTIFACT_PATH,
        ):
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())
        self.assertTrue(CANONICAL_OUTPUT_ROOT.is_dir())
        self.assertTrue(LIVE_ARTIFACT_PATH.is_file())

    def test_v1_and_v2_are_additive_lineage(self) -> None:
        self.assertTrue(V1_TEST_PATH.is_file())
        self.assertNotEqual(V1_TEST_PATH.resolve(), V2_TEST_PATH.resolve())
        self.assertEqual(sha256(V1_TEST_PATH), self.protected_hashes[V1_TEST_PATH])
        source = V2_TEST_PATH.read_text(encoding="utf-8")
        module = ast.parse(source)
        imported_modules = {
            node.module
            for node in ast.walk(module)
            if isinstance(node, ast.ImportFrom) and node.module
        }
        imported_modules.update(
            alias.name
            for node in ast.walk(module)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
        self.assertNotIn("test_resolve_receiver_originating_modal_fact_evaluation_operation_v0_min", imported_modules)
        self.assertIn("V1 is the preserved pre-live witness", source)
        self.assertIn("v2 is the additive post-live witness", source)
        self.assertIn("Both remain append-only lineage", source)
        self.assertIn("does not import, execute, invalidate, or\nreplace v1", source)

    def test_canonical_live_artifact_digest(self) -> None:
        self.assertEqual(sha256(LIVE_ARTIFACT_PATH), EXPECTED_LIVE_SHA256)

    def test_canonical_live_artifact_is_strict_duplicate_key_free_json(self) -> None:
        artifact = strict_json_bytes(LIVE_ARTIFACT_PATH.read_bytes())
        self.assertIsInstance(artifact, dict)
        with self.assertRaises(DuplicateJsonKeyError):
            strict_json_bytes(b'{"duplicate":1,"duplicate":2}')
        with self.assertRaises(ValueError):
            strict_json_bytes(b'{"non_finite":NaN}')

    def test_canonical_live_artifact_exact_supported_standing(self) -> None:
        artifact = self.live_artifact
        self.assertEqual(
            artifact["resolver_module"],
            "resolve_receiver_originating_modal_fact_evaluation_operation_v0_min",
        )
        self.assertEqual(artifact["result_version"], "0.1.0")
        self.assertEqual(artifact["outcome"], resolver.OUTCOME_SUPPORTED)
        self.assertEqual(
            artifact["operation_result"], resolver.OPERATION_RESULT_SUPPORTED
        )
        self.assertEqual(artifact["passed_check_count"], 378)
        self.assertEqual(artifact["failed_check_count"], 0)
        self.assertEqual(
            artifact["completed_modal_fact_evaluation_result_posture_count"], 1
        )
        self.assertEqual(
            artifact["block"],
            {"blocked": False, "code": None, "block_code": None, "reason": None},
        )
        operation = self.operation(artifact)
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
            self.assertIs(operation[field], True)
        self.assertIsNone(artifact["admissible_future_route"])

    def test_canonical_live_artifact_target_support_without_establishment(self) -> None:
        artifact = self.live_artifact
        operation = self.operation(artifact)
        for target in EXPECTED_TARGETS:
            entry = artifact["target_condition_evaluations"][target]
            self.assertEqual(entry["evaluation"], resolver.TARGET_EVALUATION_SUPPORTED)
            self.assertIs(entry["modal_fact_established"], False)
            self.assertIs(entry["source_support_only"], True)
            self.assertIs(operation[target + "_supported"], True)
            self.assertIs(operation[target + "_established"], False)
        posture = artifact["target_support_posture"]
        self.assertIs(posture["support_is_matter_bound"], True)
        self.assertIs(posture["support_is_source_relation_bound"], True)
        self.assertIs(posture["support_is_not_reality_wide_establishment"], True)

    def test_supported_result_preserves_all_non_claims_false(self) -> None:
        non_claims = self.live_artifact["non_claims"]
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(
            all(type(value) is bool and value is False for value in non_claims.values())
        )
        self.assertIs(
            self.live_artifact["result_level_non_claims_canonical_false"], True
        )
        required = {
            "receiver_actual_refusal_established",
            "receiver_actual_withholding_established",
            "receiver_freedom_established",
            "receiver_originating_declaration_truth_created",
            "receiver_originating_declaration_authority_created",
            "receiver_originating_declaration_native_standing_created",
            "source_authority_created",
            "canon_admission_created",
            "governance_force_created",
            "truth_created",
            "standing_created",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "identity_created",
            "custody_created",
            "custody_proven",
            "provenance_created",
            "provenance_proven",
            "physical_validity_created",
            "physical_validity_proven",
            "relation_created",
            "coupling_created",
            "field_machinery_created",
            "runtime_created",
            "api_created",
            "public_interface_created",
            "public_intake_created",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "repeated_receiver_originating_modal_fact_evaluation_operation_permission_created",
            "reusable_receiver_originating_modal_fact_evaluation_operation_route_created",
            "same_receiver_originating_modal_fact_evaluation_operation_rerun_authorized",
            "automatic_receiver_originating_modal_fact_evaluation_operation_retry_created",
            "receiver_originating_modal_fact_evaluation_operation_debt_created",
            "receiver_originating_modal_fact_evaluation_operation_obligation_created",
            "scheduled_receiver_originating_modal_fact_evaluation_created",
            "scheduled_presence_re_evaluation_created",
            "automatic_next_step_created",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
        }
        self.assertTrue(required.issubset(non_claims))
        self.assertTrue(all(non_claims[field] is False for field in required))

    def test_all_excluded_conditions_remain_not_evaluated(self) -> None:
        excluded = self.live_artifact["excluded_condition_posture"]
        self.assertEqual(
            excluded["condition_evaluations"],
            {field: resolver.TARGET_EVALUATION_NOT_EVALUATED for field in EXPECTED_EXCLUDED},
        )
        self.assertIs(excluded["excluded_condition_evaluation_performed"], False)
        self.assertIs(excluded["excluded_conditions_not_evaluated"], True)
        keys = self.recursive_keys(self.live_artifact)
        self.assertNotIn("excluded_condition_evidence_body", keys)
        self.assertNotIn("excluded_condition_evidence_bodies", keys)

    def test_prior_presence_standing_is_preserved(self) -> None:
        prior = self.live_artifact["prior_presence_preservation_posture"]
        self.assertEqual(prior["prior_outcome"], resolver.PRIOR_PRESENCE_OUTCOME)
        self.assertEqual(prior["prior_operation_result"], resolver.PRIOR_PRESENCE_RESULT)
        self.assertIs(prior["prior_operation_exhausted"], True)
        self.assertIsNone(prior["prior_admissible_future_route"])
        evaluations = prior["condition_evaluations"]
        self.assertEqual(evaluations["receiver_attested"], "SATISFIED")
        self.assertEqual(evaluations["receiver_answerable_receipt_present"], "SATISFIED")
        for condition in resolver.PRIOR_REQUIRES_BASIS_CONDITIONS:
            self.assertEqual(evaluations[condition], "REQUIRES_BASIS")
        self.assertIs(
            prior["all_twelve_prior_requires_basis_conditions_historically_legible"],
            True,
        )
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
        ):
            self.assertIs(prior[field], False)
        for target in EXPECTED_TARGETS:
            self.assertEqual(evaluations[target], "REQUIRES_BASIS")
            self.assertEqual(
                self.live_artifact["target_condition_evaluations"][target]["evaluation"],
                resolver.TARGET_EVALUATION_SUPPORTED,
            )

    def test_source_origin_jurisdiction_and_non_naturalization_preserved(self) -> None:
        lineage = self.live_artifact["lineage_preservation_posture"]
        self.assertEqual(set(lineage), set(resolver.LINEAGE_PRESERVATION_FIELDS))
        self.assertTrue(all(value is True for value in lineage.values()))
        source = self.live_artifact["source_selection_and_carriage_lineage"]
        for field in (
            "receiver_origin_validated",
            "declared_provenance_posture_validated",
            "carried_arrival_validated",
            "non_native_standing_validated",
            "jurisdiction_distinction_validated",
            "candidate_correspondence_validated",
            "receiver_attestation_correspondence_validated",
            "receiver_answerable_receipt_correspondence_validated",
        ):
            self.assertIs(source[field], True)

    def test_exact_source_identity_and_six_record_surface(self) -> None:
        raw = DECLARATION_PATH.read_bytes()
        self.assertEqual(len(raw), 207)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), resolver.DECLARATION_SHA256)
        self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
        text = raw.decode("utf-8", errors="strict")
        lines = text.splitlines()
        self.assertEqual(len(lines), 6)
        self.assertTrue(all(line and "=" in line for line in lines))
        records: dict[str, str] = {}
        for line in lines:
            key, value = line.split("=", 1)
            self.assertNotIn(key, records)
            records[key] = value
        self.assertEqual(records, EXPECTED_DECLARATION_RECORDS)
        validation = self.live_artifact["receiver_originating_declaration_validation"]
        self.assertIs(validation["strict_utf8_validated"], True)
        self.assertIs(validation["bom_absent"], True)
        self.assertIs(validation["exact_six_unique_records_validated"], True)
        self.assertEqual(validation["expected_byte_count"], 207)
        self.assertEqual(validation["observed_byte_count"], 207)
        self.assertEqual(
            validation["archive_sha256_identity"], resolver.DECLARATION_ARCHIVE_SHA256
        )
        self.assertEqual(validation["candidate_id"], resolver.DECLARATION_CANDIDATE_ID)
        self.assertEqual(
            validation["source_provenance_reference"],
            resolver.DECLARATION_PROVENANCE_REFERENCE,
        )
        self.assertEqual(validation["receipt_bundle"], resolver.DECLARATION_RECEIPT_BUNDLE)
        self.assertEqual(validation["receiver_label"], "Mario")
        self.assertEqual(
            validation["matter_relevant_records"],
            {"could_have_been_refused": True, "could_have_been_withheld": True},
        )
        operation = self.operation(self.live_artifact)
        self.assertEqual(operation["selected_source_class"], resolver.SELECTED_SOURCE_CLASS)
        self.assertEqual(operation["selected_relation_class"], resolver.SELECTED_RELATION_CLASS)
        self.assertEqual(operation["selected_matter_class"], resolver.SELECTED_MATTER_CLASS)
        self.assertEqual(operation["selected_source_origin"], resolver.SELECTED_SOURCE_ORIGIN)
        self.assertEqual(
            operation["selected_source_provenance_posture"],
            resolver.SELECTED_SOURCE_PROVENANCE_POSTURE,
        )
        self.assertEqual(
            operation["selected_source_arrival_posture"],
            resolver.SELECTED_SOURCE_ARRIVAL_POSTURE,
        )
        self.assertIs(operation["selected_source_native_standing"], False)
        self.assertIs(operation["jurisdiction_distinction_preserved"], True)

    def test_atomic_basis_validations_and_upstream_digests(self) -> None:
        atomic = self.live_artifact["atomic_operation_basis_posture"]
        self.assertTrue(all(value is True for value in atomic.values()))
        self.assertIs(atomic["all_six_governed_files_validated"], True)
        self.assertIs(atomic["canonical_request_validated"], True)
        self.assertIs(atomic["partial_basis_cannot_produce_completed_result"], True)
        validations = (
            (
                "boundary_artifact_validation",
                "f24795566eb369ad935e2212aba83ef68bfd1661363cc94da2f53498cc2935ac",
            ),
            (
                "candidate_sufficiency_artifact_validation",
                "7271d8cb62ce75fd4c5a42e09775d481edf62dae813790d16f8361c0e06509f4",
            ),
            (
                "receiver_attestation_artifact_validation",
                "175821764f0f284311c21968994473ad6157148fae360102540a9e1a237533e9",
            ),
            (
                "receiver_answerable_receipt_artifact_validation",
                "a80c4d99b3b4d33f9b267989a4696e088e10f25845b536d0b188e1554973dfcb",
            ),
        )
        for section, digest in validations:
            validation = self.live_artifact[section]
            self.assertIs(validation["artifact_validated"], True)
            self.assertEqual(validation["expected_sha256"], digest)
            self.assertEqual(validation["observed_sha256"], digest)
        declaration = self.live_artifact["receiver_originating_declaration_validation"]
        self.assertEqual(declaration["expected_sha256"], resolver.DECLARATION_SHA256)
        self.assertEqual(declaration["observed_sha256"], resolver.DECLARATION_SHA256)
        self.assertIs(
            self.live_artifact["specification_validation"]["specification_validated"],
            True,
        )

    def test_terminal_summary_matches_live_standing(self) -> None:
        text = TERMINAL_SUMMARY_PATH.read_text(encoding="utf-8")
        markers = (
            "terminal_status = RECEIVER_ORIGINATING_MODAL_FACT_EVALUATION_OPERATION_COMPLETED_SUPPORTED",
            "passed_check_count = 378",
            "failed_check_count = 0",
            EXPECTED_LIVE_SHA256,
            "receiver_answerable_basis_refusable = SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE",
            "receiver_answerable_basis_could_have_been_withheld = SUPPORTED_BY_ADMITTED_RECEIVER_ORIGINATING_SOURCE",
            "receiver_answerable_basis_refusable_supported = true",
            "receiver_answerable_basis_could_have_been_withheld_supported = true",
            "receiver_answerable_basis_refusable_established = false",
            "receiver_answerable_basis_could_have_been_withheld_established = false",
            "excluded_conditions_not_evaluated = true",
            "prior_presence_requires_basis_result_preserved",
            "admissible_future_route = null",
            "operation tests are completed",
            "operation live result is recorded",
            "Open does not mean selected, authorized, scheduled, required, automatic, or next.",
        )
        for marker in markers:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_resolver_reexecution_matches_canonical_live_artifact(self) -> None:
        result = self.resolve_current(copy.deepcopy(self.canonical_request))
        self.assertEqual(result, self.live_artifact)
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), self.live_bytes)

    def test_resolver_reexecution_is_deterministic(self) -> None:
        first = self.resolve_current(copy.deepcopy(self.canonical_request))
        second = self.resolve_current(copy.deepcopy(self.canonical_request))
        self.assertEqual(first, second)
        self.assertEqual(first, self.live_artifact)
        self.assertEqual(first[CHECKS_KEY], second[CHECKS_KEY])

    def test_summary_projection_matches_live_artifact(self) -> None:
        summary = (
            resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_summary(
                self.live_artifact
            )
        )
        self.assertEqual(summary, self.live_artifact[SUMMARY_KEY])
        self.assertNotIn(CHECKS_KEY, summary)
        self.assertNotIn("non_claims", summary)

    def test_canonical_writer_refuses_overwrite_of_standing_live_artifact(self) -> None:
        before_bytes = LIVE_ARTIFACT_PATH.read_bytes()
        before_digest = sha256(LIVE_ARTIFACT_PATH)
        before_directory = self.directory_stat(CANONICAL_OUTPUT_ROOT)
        with (
            patch.object(Path, "open", autospec=True) as open_mock,
            patch.object(Path, "mkdir", autospec=True) as mkdir_mock,
        ):
            with self.assertRaises(
                resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError
            ):
                resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(
                    self.live_artifact
                )
            open_mock.assert_not_called()
            mkdir_mock.assert_not_called()
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), before_bytes)
        self.assertEqual(sha256(LIVE_ARTIFACT_PATH), before_digest)
        self.assertEqual(self.directory_stat(CANONICAL_OUTPUT_ROOT), before_directory)

    def test_writer_refuses_noncanonical_paths_and_inconsistent_results(self) -> None:
        valid = copy.deepcopy(self.live_artifact)
        blocked = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min(
            []
        )
        invalid: list[tuple[str, object]] = [
            (
                "default",
                resolver.build_receiver_originating_modal_fact_evaluation_operation_v0_min_default_result(),
            ),
        ]

        def changed(label: str, change: Callable[[dict[str, Any]], None]) -> None:
            value = copy.deepcopy(valid)
            change(value)
            invalid.append((label, value))

        changed(
            "outcome_result",
            lambda value: value.__setitem__(
                "operation_result", resolver.OPERATION_RESULT_INDETERMINATE
            ),
        )
        changed(
            "failed_check",
            lambda value: value[CHECKS_KEY][0].__setitem__("passed", False),
        )
        changed(
            "true_nonclaim",
            lambda value: value["non_claims"].__setitem__(
                resolver.REQUIRED_FALSE_NON_CLAIMS[0], True
            ),
        )
        changed(
            "support_mismatch",
            lambda value: value["target_support_posture"].__setitem__(
                EXPECTED_TARGETS[0] + "_supported", False
            ),
        )
        changed(
            "future_route",
            lambda value: value.__setitem__("admissible_future_route", "AUTOMATIC"),
        )
        changed(
            "summary",
            lambda value: value[SUMMARY_KEY].__setitem__("outcome", "WRONG"),
        )
        changed(
            "prohibited_material",
            lambda value: value.__setitem__("complete_declaration_body", "body"),
        )
        refused_paths = (
            CANONICAL_OUTPUT_ROOT / "alternate.json",
            CANONICAL_OUTPUT_ROOT.parent / "sibling" / resolver.OUTPUT_FILENAME,
            CANONICAL_OUTPUT_ROOT / ".." / "outside.json",
        )
        before_bytes = LIVE_ARTIFACT_PATH.read_bytes()
        before_directory = self.directory_stat(CANONICAL_OUTPUT_ROOT)
        with (
            patch.object(Path, "open", autospec=True) as open_mock,
            patch.object(Path, "mkdir", autospec=True) as mkdir_mock,
        ):
            for label, result in (*invalid, ("blocked", blocked)):
                with self.subTest(result=label):
                    with self.assertRaises(
                        resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError
                    ):
                        resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(
                            result
                        )
            for path in refused_paths:
                with self.subTest(path=str(path)):
                    with self.assertRaises(
                        resolver.ReceiverOriginatingModalFactEvaluationOperationV0MinError
                    ):
                        resolver.write_receiver_originating_modal_fact_evaluation_operation_v0_min_result(
                            valid,
                            path,
                        )
            open_mock.assert_not_called()
            mkdir_mock.assert_not_called()
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), before_bytes)
        self.assertEqual(self.directory_stat(CANONICAL_OUTPUT_ROOT), before_directory)

    def test_from_path_matches_direct_current_state_resolution(self) -> None:
        request = copy.deepcopy(self.canonical_request)
        with tempfile.TemporaryDirectory() as temporary:
            path = self.write_json(Path(temporary) / "request.json", request)
            before = path.read_bytes()
            result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(
                path,
                governing_specification_path=SPECIFICATION_PATH,
                boundary_artifact_path=BOUNDARY_PATH,
                declaration_surface_path=DECLARATION_PATH,
                candidate_sufficiency_artifact_path=CANDIDATE_PATH,
                receiver_attestation_artifact_path=ATTESTATION_PATH,
                receiver_answerable_receipt_artifact_path=RECEIPT_PATH,
            )
            self.assertEqual(result, self.live_artifact)
            self.assertEqual(path.read_bytes(), before)

    def test_invalid_request_and_duplicate_key_request_still_block(self) -> None:
        def mutated(change: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
            value = copy.deepcopy(self.canonical_request)
            change(value)
            return value

        mapping_cases = (
            ("missing", mutated(lambda value: value.pop("intent"))),
            ("unknown", mutated(lambda value: value.__setitem__("unknown", False))),
            ("intent", mutated(lambda value: value.__setitem__("intent", "WRONG"))),
            (
                "path",
                mutated(
                    lambda value: value.__setitem__(
                        "receiver_originating_modal_fact_source_admissibility_boundary_artifact_path",
                        "wrong",
                    )
                ),
            ),
            (
                "source",
                mutated(
                    lambda value: value.__setitem__("selected_source_class", "WRONG")
                ),
            ),
            (
                "matter_order",
                mutated(
                    lambda value: value.__setitem__(
                        "selected_matter", list(reversed(EXPECTED_TARGETS))
                    )
                ),
            ),
            (
                "true_nonclaim",
                mutated(
                    lambda value: value["declared_non_claims"].__setitem__(
                        resolver.REQUIRED_FALSE_NON_CLAIMS[0], True
                    )
                ),
            ),
            (
                "semantic_preclaim",
                mutated(
                    lambda value: value.__setitem__(
                        "receiver_answerable_basis_refusable_supported", True
                    )
                ),
            ),
        )
        raw_cases = (
            ("duplicate", b'{"intent":"one","intent":"two"}'),
            ("malformed", b"{"),
            ("non_object", b"[]"),
            ("non_finite", b'{"value":NaN}'),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, request in mapping_cases:
                with self.subTest(request=label):
                    path = self.write_json(root / label / "request.json", request)
                    result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(
                        path,
                        governing_specification_path=SPECIFICATION_PATH,
                        boundary_artifact_path=BOUNDARY_PATH,
                        declaration_surface_path=DECLARATION_PATH,
                        candidate_sufficiency_artifact_path=CANDIDATE_PATH,
                        receiver_attestation_artifact_path=ATTESTATION_PATH,
                        receiver_answerable_receipt_artifact_path=RECEIPT_PATH,
                    )
                    self.assert_blocked(result)
            for label, raw in raw_cases:
                with self.subTest(request=label):
                    path = self.write_bytes(root / label / "request.json", raw)
                    result = resolver.resolve_receiver_originating_modal_fact_evaluation_operation_v0_min_from_path(
                        path
                    )
                    self.assert_blocked(result)
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), self.live_bytes)

    def test_temporary_governed_artifact_mutations_block(self) -> None:
        declaration = bytearray(self.declaration_bytes)
        declaration[0] = ord("F")
        cases = (
            (
                "specification",
                "governing_specification_path",
                self.specification_bytes.replace(
                    b"# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum Specification",
                    b"# Receiver-Originating Modal Fact Evaluation Operation V0 Minimum SpecificatioN",
                    1,
                ),
                "SPECIFICATION_MARKER_MISSING",
            ),
            (
                "boundary",
                "boundary_artifact_path",
                self.boundary_bytes + b" ",
                "BOUNDARY_ARTIFACT_DIGEST_MISMATCH",
            ),
            (
                "declaration",
                "declaration_surface_path",
                bytes(declaration),
                "DECLARATION_DIGEST_MISMATCH",
            ),
            (
                "candidate",
                "candidate_sufficiency_artifact_path",
                self.candidate_bytes + b" ",
                "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH",
            ),
            (
                "attestation",
                "receiver_attestation_artifact_path",
                self.attestation_bytes + b" ",
                "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH",
            ),
            (
                "receipt",
                "receiver_answerable_receipt_artifact_path",
                self.receipt_bytes + b" ",
                "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, argument, raw, code in cases:
                with self.subTest(file=label):
                    path = self.write_bytes(root / label / "mutated", raw)
                    result = self.resolve_current(**{argument: path})
                    self.assert_blocked(result, code)
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), self.live_bytes)

    def test_duplicate_key_temporary_governed_json_blocks(self) -> None:
        duplicate = b'{"duplicate":"BODY_SENTINEL","duplicate":"BODY_SENTINEL"}'
        with self.assertRaises(DuplicateJsonKeyError):
            strict_json_bytes(duplicate)
        parsed, error = resolver._parse_json_bytes(duplicate)
        self.assertIsNone(parsed)
        self.assertEqual(error, "duplicate_key")
        cases = (
            ("boundary", "boundary_artifact_path", "BOUNDARY_ARTIFACT_DIGEST_MISMATCH"),
            (
                "candidate",
                "candidate_sufficiency_artifact_path",
                "CANDIDATE_SUFFICIENCY_ARTIFACT_DIGEST_MISMATCH",
            ),
            (
                "attestation",
                "receiver_attestation_artifact_path",
                "RECEIVER_ATTESTATION_ARTIFACT_DIGEST_MISMATCH",
            ),
            (
                "receipt",
                "receiver_answerable_receipt_artifact_path",
                "RECEIVER_ANSWERABLE_RECEIPT_ARTIFACT_DIGEST_MISMATCH",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, argument, code in cases:
                with self.subTest(artifact=label):
                    path = self.write_bytes(root / label / "duplicate.json", duplicate)
                    result = self.resolve_current(**{argument: path})
                    self.assert_blocked(result, code)
                    self.assertNotIn("BODY_SENTINEL", json.dumps(result, sort_keys=True))

    def test_declaration_strictness_remains_enforced(self) -> None:
        text = self.declaration_bytes.decode("utf-8")
        records = text.splitlines()
        mutations = (
            ("wrong_count", self.declaration_bytes + b"x"),
            ("invalid_utf8", b"\xff" + self.declaration_bytes[1:]),
            ("bom", b"\xef\xbb\xbf" + self.declaration_bytes),
            (
                "duplicate",
                ("\n".join(records[:-1] + [records[1]]) + "\n").encode(),
            ),
            ("missing", ("\n".join(records[:-1]) + "\n").encode()),
            ("unknown", text.replace("freely_given", "unknown_record", 1).encode()),
            ("malformed", text.replace("freely_given=true", "freely_given", 1).encode()),
            (
                "timestamp",
                text.replace("2026-07-28T06:37:56Z", "2026-07-28T06:37:57Z", 1).encode(),
            ),
            (
                "matter_value",
                text.replace("could_have_been_refused=true", "could_have_been_refused=false", 1).encode(),
            ),
            (
                "whitespace",
                text.replace("freely_given=true", "freely_given =true", 1).encode(),
            ),
            ("ordering", ("\n".join(reversed(records)) + "\n").encode()),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, raw in mutations:
                with self.subTest(declaration=label):
                    path = self.write_bytes(root / label / "statement.txt", raw)
                    result = self.resolve_current(declaration_surface_path=path)
                    self.assert_blocked(result)
                    self.assertIn(
                        result["block"]["code"],
                        {
                            "DECLARATION_BYTE_COUNT_MISMATCH",
                            "DECLARATION_DIGEST_MISMATCH",
                        },
                    )

    def test_outcome_precedence_and_completed_non_supported_branches(self) -> None:
        supported = resolver.TARGET_EVALUATION_SUPPORTED
        requires = resolver.TARGET_EVALUATION_REQUIRES_BASIS
        indeterminate = resolver.TARGET_EVALUATION_INDETERMINATE
        cases = (
            ((supported, supported), resolver.OUTCOME_SUPPORTED),
            ((supported, requires), resolver.OUTCOME_REQUIRES_BASIS),
            ((requires, requires), resolver.OUTCOME_REQUIRES_BASIS),
            ((supported, indeterminate), resolver.OUTCOME_INDETERMINATE),
            ((requires, indeterminate), resolver.OUTCOME_INDETERMINATE),
            ((indeterminate, indeterminate), resolver.OUTCOME_INDETERMINATE),
            ((supported, "UNEXPECTED"), resolver.OUTCOME_BLOCKED),
        )
        for values, expected in cases:
            evaluations = dict(zip(EXPECTED_TARGETS, values))
            with self.subTest(evaluations=values):
                self.assertEqual(resolver._outcome_from_evaluations(evaluations), expected)
        requires_result = self.branch_result(
            {
                EXPECTED_TARGETS[0]: supported,
                EXPECTED_TARGETS[1]: requires,
            }
        )
        self.assert_completed(
            requires_result,
            resolver.OUTCOME_REQUIRES_BASIS,
            resolver.OPERATION_RESULT_REQUIRES_BASIS,
        )
        indeterminate_result = self.branch_result(
            {
                EXPECTED_TARGETS[0]: supported,
                EXPECTED_TARGETS[1]: indeterminate,
            }
        )
        self.assert_completed(
            indeterminate_result,
            resolver.OUTCOME_INDETERMINATE,
            resolver.OPERATION_RESULT_INDETERMINATE,
        )
        for result in (requires_result, indeterminate_result):
            self.assertIsNone(result["admissible_future_route"])
            for field in (
                "presence_supported",
                "presence_authorized",
                "presence_established",
                "presence_recorded",
                "receiver_originating_modal_fact_evaluation_operation_debt_created",
                "receiver_originating_modal_fact_evaluation_operation_obligation_created",
            ):
                self.assertIs(result["non_claims"][field], False)

    def test_checks_and_counts_are_deterministic(self) -> None:
        checks = self.checks(self.live_artifact)
        self.assertEqual(len(checks), 378)
        self.assertEqual(sum(check["passed"] is True for check in checks), 378)
        self.assertEqual(sum(check["passed"] is False for check in checks), 0)
        rerun = self.resolve_current(copy.deepcopy(self.canonical_request))
        self.assertEqual(rerun[CHECKS_KEY], checks)
        self.assert_counts(self.live_artifact)
        self.assert_counts(rerun)

    def test_result_structure_and_omission_posture(self) -> None:
        self.assertEqual(set(self.live_artifact), set(resolver.RESULT_SECTIONS))
        omission = self.live_artifact["omission_posture"]
        self.assertEqual(
            set(omission),
            {*resolver.OMISSION_POSTURE_FIELDS, "complete_material_omission_posture"},
        )
        self.assertTrue(all(value is True for value in omission.values()))
        self.assertFalse(resolver._contains_prohibited_complete_material(self.live_artifact))
        serialized = json.dumps(self.live_artifact, sort_keys=True)
        self.assertNotIn(self.declaration_bytes.decode("utf-8"), serialized)

    def test_non_meaning_and_blocked_conversion_posture(self) -> None:
        non_meaning = self.live_artifact[NON_MEANING_KEY]
        self.assertEqual(set(non_meaning), set(resolver.NON_MEANING_FIELDS))
        self.assertTrue(all(value is True for value in non_meaning.values()))
        self.assertEqual(
            self.live_artifact["blocked_conversions"],
            list(resolver.BLOCKED_CONVERSIONS),
        )
        self.assertEqual(
            tuple(self.live_artifact["blocked_conversions"]),
            resolver.BLOCKED_CONVERSIONS,
        )
        self.assertIsNone(self.live_artifact["admissible_future_route"])

    def test_current_what_remains_open_is_historically_bounded(self) -> None:
        historical = self.live_artifact["what_remains_open"]
        self.assertIn("receiver-originating modal-fact evaluation operation tests", historical)
        self.assertIn("receiver-originating modal-fact evaluation operation request", historical)
        self.assertIn("receiver-originating modal-fact evaluation operation live result", historical)
        self.assertIn("receiver-originating modal-fact evaluation operation terminal summary", historical)
        terminal = TERMINAL_SUMMARY_PATH.read_text(encoding="utf-8")
        for marker in (
            "operation tests are completed",
            "canonical request posture is completed",
            "operation live result is recorded",
            "terminal summary is completed by this file",
            "The earlier live-result open list remains historically truthful",
            "The operation specification, resolver, tests, canonical request posture, live result, and this terminal summary are not open.",
            "Open does not mean selected, authorized, scheduled, required, automatic, or next.",
        ):
            self.assertIn(marker, terminal)
        for field in (
            "scheduled_receiver_originating_modal_fact_evaluation_created",
            "scheduled_presence_re_evaluation_created",
            "automatic_next_step_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(self.live_artifact["non_claims"][field], False)

    def test_no_scan_discovery_network_randomness_or_current_time(self) -> None:
        prohibited_modules = {
            "datetime",
            "glob",
            "importlib",
            "os",
            "random",
            "requests",
            "socket",
            "subprocess",
            "time",
            "urllib",
            "zipfile",
        }
        prohibited_calls = {
            "extract",
            "extractall",
            "getenv",
            "glob",
            "iterdir",
            "listdir",
            "normalize",
            "repair",
            "rglob",
            "scandir",
        }
        for path in (RESOLVER_PATH, V2_TEST_PATH):
            with self.subTest(path=path.name):
                tree = ast.parse(path.read_text(encoding="utf-8"))
                imported: set[str] = set()
                called: set[str] = set()
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        imported.update(alias.name.split(".")[0] for alias in node.names)
                    elif isinstance(node, ast.ImportFrom) and node.module:
                        imported.add(node.module.split(".")[0])
                    elif isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Attribute):
                            called.add(node.func.attr)
                        elif isinstance(node.func, ast.Name):
                            called.add(node.func.id)
                self.assertFalse(imported.intersection(prohibited_modules))
                self.assertFalse(called.intersection(prohibited_calls))

    def test_suite_does_not_modify_current_repository_standing(self) -> None:
        for path, expected in self.protected_hashes.items():
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())
                self.assertEqual(sha256(path), expected)
        self.assertEqual(self.directory_stat(CANONICAL_OUTPUT_ROOT), self.output_root_stat)
        self.assertEqual(LIVE_ARTIFACT_PATH.read_bytes(), self.live_bytes)


if __name__ == "__main__":
    unittest.main()
