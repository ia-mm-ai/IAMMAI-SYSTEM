"""Tests for one bounded receiver-attestation operation resolver.

The suite preserves the governing specification, completed v2 boundary
artifact, and bounded capture package.  Every file mutation is isolated in a
temporary copy.  The tests distinguish structural blocking from lawful
waiting and the three exhausted operation-result branches.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable
from unittest.mock import patch

import resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min as resolver
from resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min import (
    AMBIGUITY_POSTURE_KEYS,
    BASIS_FIELDS,
    BLOCK_CODES,
    BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH,
    CANDIDATE_ID,
    COMPLETED_OPERATION_RESULT_FAMILY,
    COMPONENT_RELATIVE_PATHS,
    CONTRADICTION_POSTURE_KEYS,
    EXPECTED_ARCHIVE_SHA256,
    GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH,
    NON_CONVERSION_STATEMENT,
    OPERATION_ID,
    OPERATION_RESULT_INDETERMINATE,
    OPERATION_RESULT_NOT_RECORDED,
    OPERATION_RESULT_RECORDED,
    OPERATION_SCOPE,
    OPERATION_TYPE,
    OPERATION_VERSION,
    OUTCOME_BLOCKED,
    OUTCOME_FAMILY,
    OUTCOME_INDETERMINATE,
    OUTCOME_NOT_RECORDED,
    OUTCOME_RECORDED,
    OUTCOME_REQUIRES_BASIS,
    OUTPUT_FILENAME,
    OUTPUT_ROOT,
    PROHIBITED_REQUEST_FLAGS,
    REQUIRED_BASIS_NON_CLAIMS,
    REQUIRED_FALSE_NON_CLAIMS,
    REQUIRED_UPSTREAM_FALSE_POSTURES,
    RESOLVER_MODULE,
    RESULT_VERSION,
    SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
    SELECTED_BOUNDARY_ID,
    SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH,
    TEXT_COMPONENT_FIELDS,
    TRACE_INTEGRITY_POSTURE_KEYS,
    UNRESOLVED_POSTURE_KEYS,
    ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError,
    build_declared_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request,
    build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request,
    build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary,
    resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min,
    resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path,
    write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
BOUNDARY_OBJECT_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_boundary"
)
BOUNDARY_SUMMARY_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_boundary_summary"
)
OPERATION_OBJECT_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation"
)
OPERATION_SUMMARY_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation_summary"
)
CHECKS_KEY = (
    "receiver_side_answerable_basis_receiver_attestation_operation_checks"
)

PRESERVED_FIXTURE_PATHS = (
    GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH,
    SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH,
    *tuple(COMPONENT_RELATIVE_PATHS.values()),
)


class ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinTests(
    unittest.TestCase
):
    """Exercise the waiting, admitted, blocked, and writer contracts."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.preserved_hashes = {
            str(relative): cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_FIXTURE_PATHS
        }

    @classmethod
    def tearDownClass(cls) -> None:
        current = {
            str(relative): cls._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_FIXTURE_PATHS
        }
        if current != cls.preserved_hashes:
            raise AssertionError(
                "canonical specification, boundary, or capture lineage changed"
            )

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            while True:
                chunk = handle.read(65536)
                if not chunk:
                    break
                digest.update(chunk)
        return digest.hexdigest()

    def _copy_fixture_file(self, root: Path, relative: Path) -> Path:
        source = REPOSITORY_ROOT / relative
        target = root / relative
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return target

    def fixture_root(self, root: Path) -> None:
        for relative in PRESERVED_FIXTURE_PATHS:
            self._copy_fixture_file(root, relative)

    def _write_json(self, path: Path, value: Any) -> Path:
        self.assertFalse(
            path.is_dir(),
            "test fixture collision: JSON target is an existing directory",
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return path

    def _write_text(self, path: Path, value: str) -> Path:
        self.assertFalse(
            path.is_dir(),
            "test fixture collision: text target is an existing directory",
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
        return path

    def canonical_basis(self) -> dict[str, Any]:
        basis: dict[str, Any] = {
            "selected_receiver_attestation_boundary_artifact_path": str(
                SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
            ),
            "bounded_capture_directory_path": str(
                BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH
            ),
            **{
                field: str(path)
                for field, path in COMPONENT_RELATIVE_PATHS.items()
            },
            "expected_archive_sha256": EXPECTED_ARCHIVE_SHA256,
            "evaluator_reference": (
                "bounded_receiver_attestation_operation_evaluator_001"
            ),
            "trace_integrity_postures": {
                field: True for field in TRACE_INTEGRITY_POSTURE_KEYS
            },
            "ambiguity_postures": {
                field: False for field in AMBIGUITY_POSTURE_KEYS
            },
            "contradiction_postures": {
                field: False for field in CONTRADICTION_POSTURE_KEYS
            },
            "unresolved_postures": {
                field: False for field in UNRESOLVED_POSTURE_KEYS
            },
            "non_conversion_statement": NON_CONVERSION_STATEMENT,
            "basis_non_claims": {
                field: False for field in REQUIRED_BASIS_NON_CLAIMS
            },
        }
        self.assertEqual(set(basis), set(BASIS_FIELDS))
        return basis

    def request(
        self,
        basis: Any = None,
        **overrides: Any,
    ) -> dict[str, Any]:
        return (
            build_declared_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request(
                basis,
                **overrides,
            )
        )

    def invoke(
        self,
        request: Any = None,
        root: Path | None = None,
    ) -> dict[str, Any]:
        if root is None:
            return (
                resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min(
                    request
                )
            )
        with patch.object(resolver, "REPO_ROOT", root):
            return (
                resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min(
                    request
                )
            )

    def operation(self, result: dict[str, Any]) -> dict[str, Any]:
        operation = result.get(OPERATION_OBJECT_KEY)
        self.assertIsInstance(operation, dict)
        return operation

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        summary = result.get(OPERATION_SUMMARY_KEY)
        self.assertIsInstance(summary, dict)
        return summary

    def assert_public_codes(self, result: dict[str, Any]) -> None:
        for check in result.get(CHECKS_KEY, []):
            self.assertIsInstance(check, dict)
            for field in ("failure_code", "block_code"):
                if field in check:
                    self.assertIn(check[field], BLOCK_CODES)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(REQUIRED_FALSE_NON_CLAIMS))
        for field in REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=field):
                self.assertIs(non_claims[field], False)
                self.assertIs(self.operation(result)[field], False)

    def assert_not_blocked(self, result: dict[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))
        self.assertIsNone(block.get("reason"))
        self.assertEqual(result.get("failed_check_count"), 0)
        self.assert_public_codes(result)

    def assert_blocked(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("outcome"), OUTCOME_BLOCKED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        self.assertIn(block.get("code"), BLOCK_CODES)
        self.assertEqual(block.get("block_code"), block.get("code"))
        self.assertIsInstance(block.get("reason"), str)
        self.assertTrue(block.get("reason"))
        if expected_code is not None:
            self.assertEqual(block.get("code"), expected_code)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        operation = self.operation(result)
        self.assertIsNone(
            operation.get("receiver_attestation_operation_result")
        )
        for field in (
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
        ):
            self.assertIs(operation.get(field), False)
        self.assert_non_claims_false(result)
        self.assert_public_codes(result)

    def assert_completed(
        self,
        result: dict[str, Any],
        outcome: str,
        operation_result: str,
        branch_field: str,
    ) -> None:
        self.assertEqual(result.get("outcome"), outcome)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertEqual(
            operation.get("receiver_attestation_operation_result"),
            operation_result,
        )
        for field in (
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
        ):
            self.assertIs(operation.get(field), True)
        branch_fields = (
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
        )
        for field in branch_fields:
            self.assertIs(operation.get(field), field == branch_field)
        self.assert_non_claims_false(result)

    def recorded_result(self, root: Path) -> dict[str, Any]:
        return self.invoke(self.request(self.canonical_basis()), root)

    def indeterminate_result(self, root: Path) -> dict[str, Any]:
        basis = self.canonical_basis()
        basis["ambiguity_postures"][AMBIGUITY_POSTURE_KEYS[0]] = True
        return self.invoke(self.request(basis), root)

    def not_recorded_result(self, root: Path) -> dict[str, Any]:
        basis = self.canonical_basis()
        basis["contradiction_postures"][
            CONTRADICTION_POSTURE_KEYS[0]
        ] = True
        return self.invoke(self.request(basis), root)

    def test_public_surface_and_static_contract(self) -> None:
        for value in (
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request,
            build_declared_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request,
            resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min,
            resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path,
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary,
            write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result,
            ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError,
        ):
            self.assertTrue(callable(value))
        self.assertEqual(
            RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_"
            "receiver_attestation_operation_v0_min",
        )
        self.assertEqual(RESULT_VERSION, "0.1.0")
        self.assertEqual(
            OPERATION_ID,
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_001",
        )
        self.assertEqual(
            OPERATION_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_"
            "RECEIVER_ATTESTATION_OPERATION",
        )
        self.assertEqual(OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            OPERATION_SCOPE,
            "ADMIT_AND_RECORD_ONE_BOUNDED_RECEIVER_ATTESTATION_TRACE_"
            "FOR_ONE_SELECTED_SUFFICIENT_CANDIDATE_ONLY",
        )
        self.assertEqual(len(OUTCOME_FAMILY), 5)
        self.assertEqual(
            set(OUTCOME_FAMILY),
            {
                OUTCOME_RECORDED,
                OUTCOME_NOT_RECORDED,
                OUTCOME_INDETERMINATE,
                OUTCOME_REQUIRES_BASIS,
                OUTCOME_BLOCKED,
            },
        )
        self.assertEqual(
            set(COMPLETED_OPERATION_RESULT_FAMILY),
            {
                OPERATION_RESULT_RECORDED,
                OPERATION_RESULT_NOT_RECORDED,
                OPERATION_RESULT_INDETERMINATE,
            },
        )
        self.assertNotIn(
            "receiver_attestation_recorded",
            REQUIRED_FALSE_NON_CLAIMS,
        )
        self.assertNotIn(
            "receiver_attestation_recorded",
            REQUIRED_BASIS_NON_CLAIMS,
        )
        self.assertEqual(set(BASIS_FIELDS), set(self.canonical_basis()))
        self.assertEqual(
            OUTPUT_ROOT,
            REPOSITORY_ROOT
            / "artifacts/integrity_host_v0_min_coexistence_"
            "receiver_side_answerable_basis_"
            "receiver_attestation_operation_v0_min",
        )
        self.assertIn(
            "receiver_attestation_operation_v0_min_result.json",
            OUTPUT_FILENAME,
        )

    def test_canonical_waiting_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            result = self.invoke(
                build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request(),
                root,
            )
        self.assertEqual(result["outcome"], OUTCOME_REQUIRES_BASIS)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        admission = result["supplied_operation_basis_admission_metadata"]
        self.assertIs(admission["basis_supplied"], False)
        self.assertIs(admission["basis_admitted"], False)
        self.assertIsNone(
            operation["receiver_attestation_operation_result"]
        )
        for field in (
            "receiver_attestation_operation_recorded",
            "receiver_attestation_operation_result_recorded",
            "receiver_attestation_operation_exhausted",
            "receiver_attestation_decided",
            "receiver_attestation_recorded",
            "receiver_attestation_not_recorded",
            "receiver_attestation_indeterminate",
        ):
            self.assertIs(operation[field], False)
        self.assert_non_claims_false(result)

    def test_canonical_recorded_branch_and_material_omission(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            signal_path = (
                root / COMPONENT_RELATIVE_PATHS["recorded_signal_path"]
            ).resolve()
            original_read_text = Path.read_text

            def guarded_read_text(
                path: Path,
                *args: Any,
                **kwargs: Any,
            ) -> str:
                if path.resolve() == signal_path:
                    raise AssertionError("recorded-signal body was read")
                return original_read_text(path, *args, **kwargs)

            with (
                patch.object(Path, "read_text", guarded_read_text),
                patch.object(
                    Path,
                    "glob",
                    side_effect=AssertionError("filesystem glob used"),
                ),
                patch.object(
                    Path,
                    "rglob",
                    side_effect=AssertionError("filesystem rglob used"),
                ),
            ):
                result = self.recorded_result(root)

        self.assert_completed(
            result,
            OUTCOME_RECORDED,
            OPERATION_RESULT_RECORDED,
            "receiver_attestation_recorded",
        )
        admission = result["supplied_operation_basis_admission_metadata"]
        upstream = result["upstream_boundary_basis"]
        components = result["bounded_component_validation"]
        summary = self.summary(result)
        self.assertIs(admission["basis_supplied"], True)
        self.assertIs(admission["basis_admitted"], True)
        self.assertIs(upstream["upstream_boundary_validated"], True)
        self.assertIs(components["trace_paths_validated"], True)
        self.assertIs(
            components["archive_validation"][
                "correspondence_validated"
            ],
            True,
        )
        self.assertIs(components["text_components_validated"], True)
        self.assertIs(components["timestamp_validated"], True)
        self.assertIs(
            components[
                "recorded_signal_artifact_existence_validated"
            ],
            True,
        )
        self.assertIs(summary["any_ambiguity"], False)
        self.assertIs(summary["any_contradiction"], False)
        self.assertIs(summary["any_unresolved"], False)
        for field in (
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_established",
            "identity_created",
            "authority_created",
            "truth_created",
            "standing_created",
            "follow_on_authorized",
        ):
            self.assertIs(self.operation(result)[field], False)
        serialized = json.dumps(result, sort_keys=True)
        for forbidden_key in (
            '"complete_upstream_boundary_artifact":',
            '"candidate_sufficiency_artifact":',
            '"candidate_sufficiency_basis":',
            '"receiver_attestation_operation_basis":',
            '"archive_body":',
            '"attestation_statement_body":',
            '"attestation_timestamp_body":',
            '"recorded_signal_body":',
            '"signal_samples":',
        ):
            self.assertNotIn(forbidden_key, serialized)
        for omission in (
            "complete_upstream_boundary_artifact_omitted",
            "complete_candidate_sufficiency_artifact_omitted",
            "complete_candidate_sufficiency_basis_omitted",
            "complete_operation_basis_omitted",
            "archive_bytes_omitted",
            "text_component_bodies_omitted",
            "recorded_signal_body_omitted",
        ):
            self.assertIs(summary[omission], True)

    def test_indeterminate_precedence_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for family, fields in (
                ("ambiguity_postures", AMBIGUITY_POSTURE_KEYS),
                ("unresolved_postures", UNRESOLVED_POSTURE_KEYS),
            ):
                for field in fields:
                    with self.subTest(family=family, field=field):
                        basis = self.canonical_basis()
                        basis[family][field] = True
                        result = self.invoke(self.request(basis), root)
                        self.assert_completed(
                            result,
                            OUTCOME_INDETERMINATE,
                            OPERATION_RESULT_INDETERMINATE,
                            "receiver_attestation_indeterminate",
                        )
            for family, field in (
                ("ambiguity_postures", AMBIGUITY_POSTURE_KEYS[0]),
                ("unresolved_postures", UNRESOLVED_POSTURE_KEYS[0]),
            ):
                with self.subTest(precedence=family):
                    basis = self.canonical_basis()
                    basis[family][field] = True
                    basis["contradiction_postures"][
                        CONTRADICTION_POSTURE_KEYS[0]
                    ] = True
                    result = self.invoke(self.request(basis), root)
                    self.assert_completed(
                        result,
                        OUTCOME_INDETERMINATE,
                        OPERATION_RESULT_INDETERMINATE,
                        "receiver_attestation_indeterminate",
                    )

    def test_not_recorded_contradiction_matrix_and_non_meaning(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            for field in CONTRADICTION_POSTURE_KEYS:
                with self.subTest(field=field):
                    basis = self.canonical_basis()
                    basis["contradiction_postures"][field] = True
                    result = self.invoke(self.request(basis), root)
                    self.assert_completed(
                        result,
                        OUTCOME_NOT_RECORDED,
                        OPERATION_RESULT_NOT_RECORDED,
                        "receiver_attestation_not_recorded",
                    )
                    non_meaning = result[
                        "receiver_side_answerable_basis_"
                        "receiver_attestation_operation_non_meaning"
                    ]
                    for key in (
                        "not_recorded_is_not_occurrence_denial",
                        "not_recorded_is_not_receiver_dishonesty",
                        "not_recorded_is_not_candidate_insufficiency",
                        "not_recorded_is_not_trace_erasure",
                    ):
                        self.assertIs(non_meaning[key], True)
                    self.assertIs(
                        self.operation(result)["presence_established"],
                        False,
                    )
                    self.assertIs(
                        self.operation(result)["affected_file_repaired"],
                        False,
                    )

    def test_request_contract_blocking_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            cases: list[tuple[str, Any, str | None]] = [
                ("non_mapping", [], "REQUEST_NOT_MAPPING"),
                (
                    "unsupported_intent",
                    self.request(intent="UNSUPPORTED"),
                    "UNSUPPORTED_INTENT",
                ),
                (
                    "missing_field",
                    self.request(),
                    "REQUEST_FIELD_MISSING",
                ),
                (
                    "unknown_field",
                    self.request(unknown_field=True),
                    "REQUEST_UNKNOWN_FIELD",
                ),
            ]
            cases[2][1].pop("operation_id")
            mismatches = (
                ("operation_id", "other"),
                ("operation_type", "other"),
                ("operation_version", "9.9.9"),
                ("operation_scope", "other"),
                ("receiver_side_answerable_basis_candidate_id", "other"),
                ("selected_candidate_sufficiency_operation_id", "other"),
                (
                    "selected_candidate_sufficiency_operation_result_required",
                    "other",
                ),
                (
                    "governing_receiver_attestation_operation_specification_path",
                    "other",
                ),
                (
                    "selected_receiver_attestation_boundary_artifact_path",
                    "other",
                ),
                ("bounded_capture_directory_path", "other"),
            )
            for field, value in mismatches:
                cases.append(
                    (
                        "mismatch_" + field,
                        self.request(**{field: value}),
                        "REQUEST_VALUE_MISMATCH",
                    )
                )
            preclaims = (
                ("outcome", OUTCOME_RECORDED),
                ("operation_result", OPERATION_RESULT_RECORDED),
                ("receiver_attestation_operation_result", "preclaimed"),
                ("receiver_attestation_recorded", True),
                ("receiver_attestation_not_recorded", True),
                ("receiver_attestation_indeterminate", True),
                ("dimension_result", "preclaimed"),
                ("complete_archive", "embedded"),
                ("complete_signal_body", "embedded"),
            )
            for field, value in preclaims:
                cases.append(
                    (
                        "preclaim_" + field,
                        self.request(**{field: value}),
                        "RESULT_POSTURE_PRECLAIMED",
                    )
                )
            for label, request_value, code in cases:
                with self.subTest(case=label):
                    self.assert_blocked(
                        self.invoke(request_value, root),
                        code,
                    )

            for field, expected_code in PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(prohibited_flag=field):
                    result = self.invoke(
                        self.request(**{field: True}),
                        root,
                    )
                    self.assert_blocked(result, expected_code)

            for label, mutate in (
                (
                    "missing_non_claim",
                    lambda value: value["declared_non_claims"].pop(
                        REQUIRED_FALSE_NON_CLAIMS[0]
                    ),
                ),
                (
                    "flipped_non_claim",
                    lambda value: value["declared_non_claims"].__setitem__(
                        REQUIRED_FALSE_NON_CLAIMS[0],
                        True,
                    ),
                ),
            ):
                with self.subTest(case=label):
                    request_value = self.request()
                    mutate(request_value)
                    self.assert_blocked(
                        self.invoke(request_value, root),
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_specification_validation_matrix(self) -> None:
        marker_cases = (
            ("title", resolver.SPEC_MARKER_FAMILIES["title"][0]),
            (
                "operation_identity",
                resolver.SPEC_MARKER_FAMILIES["operation_identity"][0],
            ),
            (
                "upstream_boundary",
                resolver.SPEC_MARKER_FAMILIES["upstream_boundary"][0],
            ),
            (
                "capture_directory",
                str(BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH) + "/",
            ),
            ("archive_hash", EXPECTED_ARCHIVE_SHA256),
            ("basis_field", BASIS_FIELDS[0]),
            ("waiting_outcome", OUTCOME_REQUIRES_BASIS),
            ("blocked_outcome", OUTCOME_BLOCKED),
            (
                "completed_result",
                COMPLETED_OPERATION_RESULT_FAMILY[0],
            ),
            (
                "precedence",
                resolver.SPEC_MARKER_FAMILIES["precedence"][0],
            ),
            ("occurrence_artifact", "Occurrence is not artifact."),
            (
                "artifact_occurrence",
                "Artifact does not create the occurrence.",
            ),
            (
                "independent_verification",
                "Preserved trace is not independent verification.",
            ),
            (
                "recorded_receipt",
                "Receiver attestation recorded is not "
                "receiver-answerable receipt.",
            ),
            (
                "recorded_presence",
                "Receiver attestation recorded is not presence.",
            ),
            ("open_next", "Open does not mean next."),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            spec_path = (
                root / GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
            )
            canonical_text = (
                REPOSITORY_ROOT
                / GOVERNING_OPERATION_SPECIFICATION_RELATIVE_PATH
            ).read_text(encoding="utf-8")

            spec_path.unlink()
            self.assert_blocked(
                self.invoke(self.request(), root),
                "OPERATION_SPEC_REFERENCE_MISSING",
            )
            spec_path.mkdir()
            self.assert_blocked(
                self.invoke(self.request(), root),
                "OPERATION_SPEC_REFERENCE_MISSING",
            )
            shutil.rmtree(spec_path)

            for label, marker in marker_cases:
                with self.subTest(marker=label):
                    self.assertIn(marker, canonical_text)
                    self._write_text(
                        spec_path,
                        canonical_text.replace(marker, ""),
                    )
                    self.assert_blocked(
                        self.invoke(self.request(), root),
                        "OPERATION_SPEC_MARKER_MISSING",
                    )
            self._write_text(spec_path, canonical_text)

    def test_upstream_boundary_validation_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            path = root / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
            canonical = json.loads(
                (
                    REPOSITORY_ROOT
                    / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
                ).read_text(encoding="utf-8")
            )
            boundary = canonical[BOUNDARY_OBJECT_KEY]
            summary = canonical[BOUNDARY_SUMMARY_KEY]

            path.unlink()
            self.assert_blocked(
                self.invoke(self.request(), root),
                "SELECTED_BOUNDARY_ARTIFACT_REFERENCE_MISSING",
            )
            self._write_text(path, "{")
            self.assert_blocked(
                self.invoke(self.request(), root),
                "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            )
            self._write_text(
                path,
                '{"resolver_module":"a","resolver_module":"b"}\n',
            )
            self.assert_blocked(
                self.invoke(self.request(), root),
                "SELECTED_BOUNDARY_ARTIFACT_NOT_PARSEABLE",
            )
            self._write_json(path, [])
            self.assert_blocked(
                self.invoke(self.request(), root),
                "SELECTED_BOUNDARY_ARTIFACT_NOT_MAPPING",
            )

            cases: list[
                tuple[str, Callable[[dict[str, Any]], None], str]
            ] = [
                (
                    "resolver_module",
                    lambda value: value.__setitem__(
                        "resolver_module", "other"
                    ),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                ),
                (
                    "result_version",
                    lambda value: value.__setitem__(
                        "result_version", "other"
                    ),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                ),
                (
                    "failed_count_nonzero",
                    lambda value: value.__setitem__(
                        "failed_check_count", 1
                    ),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                ),
                (
                    "failed_count_wrong_type",
                    lambda value: value.__setitem__(
                        "failed_check_count", False
                    ),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                ),
                (
                    "outcome",
                    lambda value: value.__setitem__("outcome", "other"),
                    "SELECTED_BOUNDARY_METADATA_MISMATCH",
                ),
            ]
            identity_fields = (
                "boundary_id",
                "boundary_type",
                "boundary_version",
                "boundary_scope",
                "receiver_side_answerable_basis_candidate_id",
                "selected_candidate_sufficiency_operation_id",
                "selected_candidate_sufficiency_operation_result_required",
            )
            for field in identity_fields:
                cases.append(
                    (
                        "identity_" + field,
                        lambda value, field=field: value[
                            BOUNDARY_OBJECT_KEY
                        ].__setitem__(field, "other"),
                        "SELECTED_BOUNDARY_IDENTITY_MISMATCH",
                    )
                )
            boundary_postures = (
                (
                    "receiver_attestation_boundary_result",
                    "other",
                ),
                ("receiver_attestation_boundary_recorded", False),
                (
                    "receiver_attestation_boundary_result_recorded",
                    False,
                ),
                ("receiver_attestation_consideration_allowed", False),
                (
                    "receiver_attestation_consideration_not_allowed",
                    True,
                ),
                ("receiver_attestation_boundary_exhausted", False),
                ("bounded_material_selected_for_consideration", False),
            )
            for field, value in boundary_postures:
                cases.append(
                    (
                        "posture_" + field,
                        lambda artifact, field=field, value=value: artifact[
                            BOUNDARY_OBJECT_KEY
                        ].__setitem__(field, value),
                        "SELECTED_BOUNDARY_POSTURE_INVALID",
                    )
                )
            summary_postures = (
                "specification_markers_validated",
                "selected_operation_validated",
                "eight_dimensions_validated",
                "upstream_false_locks_validated",
                "result_level_non_claims_canonical_false",
                "complete_operation_artifact_omitted",
                "complete_sufficiency_basis_omitted",
                "complete_capture_signal_data_omitted",
            )
            for field in summary_postures:
                cases.append(
                    (
                        "summary_" + field,
                        lambda artifact, field=field: artifact[
                            BOUNDARY_SUMMARY_KEY
                        ].__setitem__(field, False),
                        "SELECTED_BOUNDARY_POSTURE_INVALID",
                    )
                )
            for label, mutate, code in cases:
                with self.subTest(case=label):
                    artifact = copy.deepcopy(canonical)
                    mutate(artifact)
                    self._write_json(path, artifact)
                    self.assert_blocked(
                        self.invoke(self.request(), root),
                        code,
                    )

            self.assertEqual(
                boundary["boundary_id"],
                SELECTED_BOUNDARY_ID,
            )
            self.assertIs(
                summary["result_level_non_claims_canonical_false"],
                True,
            )

    def test_every_upstream_false_lock_uses_exact_boolean_false(self) -> None:
        invalid_values = (True, None, "false", 0, 1, [], {})
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            path = root / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
            canonical = json.loads(
                (
                    REPOSITORY_ROOT
                    / SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH
                ).read_text(encoding="utf-8")
            )
            for location in (BOUNDARY_OBJECT_KEY, "non_claims"):
                for field in REQUIRED_UPSTREAM_FALSE_POSTURES:
                    for value in invalid_values:
                        with self.subTest(
                            location=location,
                            field=field,
                            value=repr(value),
                        ):
                            artifact = copy.deepcopy(canonical)
                            artifact[location][field] = copy.deepcopy(value)
                            self._write_json(path, artifact)
                            self.assert_blocked(
                                self.invoke(self.request(), root),
                                "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                            )
                    with self.subTest(
                        location=location,
                        field=field,
                        value="missing",
                    ):
                        artifact = copy.deepcopy(canonical)
                        artifact[location].pop(field)
                        self._write_json(path, artifact)
                        self.assert_blocked(
                            self.invoke(self.request(), root),
                            "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                        )

            field = REQUIRED_UPSTREAM_FALSE_POSTURES[0]
            artifact = copy.deepcopy(canonical)
            artifact[BOUNDARY_OBJECT_KEY].pop(field)
            artifact[BOUNDARY_SUMMARY_KEY][field] = False
            self._write_json(path, artifact)
            self.assert_blocked(
                self.invoke(self.request(), root),
                "UPSTREAM_FALSE_LOCK_NOT_FALSE",
            )

    def test_basis_schema_blocking_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            basis_cases: list[
                tuple[str, Any, str | None]
            ] = [
                ("non_mapping", [], "OPERATION_BASIS_NOT_MAPPING"),
            ]
            missing = self.canonical_basis()
            missing.pop(BASIS_FIELDS[0])
            basis_cases.append(
                ("missing_field", missing, "OPERATION_BASIS_FIELD_MISSING")
            )
            unknown = self.canonical_basis()
            unknown["unknown"] = False
            basis_cases.append(
                ("unknown_field", unknown, "OPERATION_BASIS_UNKNOWN_FIELD")
            )
            for field in (
                "selected_receiver_attestation_boundary_artifact_path",
                "bounded_capture_directory_path",
                next(iter(COMPONENT_RELATIVE_PATHS)),
            ):
                value = self.canonical_basis()
                value[field] = "alternate"
                basis_cases.append(
                    (
                        "alternate_" + field,
                        value,
                        "OPERATION_BASIS_PATH_MISMATCH",
                    )
                )
            wrong_hash = self.canonical_basis()
            wrong_hash["expected_archive_sha256"] = "0" * 64
            basis_cases.append(
                (
                    "alternate_hash",
                    wrong_hash,
                    "OPERATION_BASIS_HASH_MISMATCH",
                )
            )
            empty_evaluator = self.canonical_basis()
            empty_evaluator["evaluator_reference"] = ""
            basis_cases.append(
                (
                    "empty_evaluator",
                    empty_evaluator,
                    "OPERATION_BASIS_EVALUATOR_REFERENCE_INVALID",
                )
            )
            vague = self.canonical_basis()
            vague["non_conversion_statement"] = ""
            basis_cases.append(
                (
                    "empty_conversion",
                    vague,
                    "OPERATION_BASIS_NON_CONVERSION_INVALID",
                )
            )
            for smuggled in (
                "receiver_attestation_recorded",
                "operation_result",
                "complete_archive",
                "complete_signal_body",
            ):
                value = self.canonical_basis()
                value[smuggled] = True
                basis_cases.append(
                    (
                        "smuggled_" + smuggled,
                        value,
                        "OPERATION_BASIS_UNKNOWN_FIELD",
                    )
                )
            for label, basis, code in basis_cases:
                with self.subTest(case=label):
                    self.assert_blocked(
                        self.invoke(self.request(basis), root),
                        code,
                    )

            posture_families = (
                (
                    "trace_integrity_postures",
                    TRACE_INTEGRITY_POSTURE_KEYS,
                ),
                ("ambiguity_postures", AMBIGUITY_POSTURE_KEYS),
                (
                    "contradiction_postures",
                    CONTRADICTION_POSTURE_KEYS,
                ),
                ("unresolved_postures", UNRESOLVED_POSTURE_KEYS),
            )
            for family, fields in posture_families:
                malformed = self.canonical_basis()
                malformed[family] = []
                self.assert_blocked(
                    self.invoke(self.request(malformed), root),
                    "OPERATION_BASIS_POSTURE_MAP_INVALID",
                )
                missing_posture = self.canonical_basis()
                missing_posture[family].pop(fields[0])
                self.assert_blocked(
                    self.invoke(self.request(missing_posture), root),
                    "OPERATION_BASIS_POSTURE_MAP_INVALID",
                )
                additional = self.canonical_basis()
                additional[family]["extra"] = False
                self.assert_blocked(
                    self.invoke(self.request(additional), root),
                    "OPERATION_BASIS_POSTURE_MAP_INVALID",
                )
            trace_false = self.canonical_basis()
            trace_false["trace_integrity_postures"][
                TRACE_INTEGRITY_POSTURE_KEYS[0]
            ] = False
            self.assert_blocked(
                self.invoke(self.request(trace_false), root),
                "OPERATION_BASIS_TRACE_INTEGRITY_NOT_TRUE",
            )

            for label, mutate in (
                (
                    "missing_basis_non_claim",
                    lambda value: value["basis_non_claims"].pop(
                        REQUIRED_BASIS_NON_CLAIMS[0]
                    ),
                ),
                (
                    "additional_basis_non_claim",
                    lambda value: value["basis_non_claims"].__setitem__(
                        "extra", False
                    ),
                ),
                (
                    "flipped_basis_non_claim",
                    lambda value: value["basis_non_claims"].__setitem__(
                        REQUIRED_BASIS_NON_CLAIMS[0], True
                    ),
                ),
                (
                    "recorded_in_basis_non_claim",
                    lambda value: value["basis_non_claims"].__setitem__(
                        "receiver_attestation_recorded", False
                    ),
                ),
            ):
                with self.subTest(case=label):
                    value = self.canonical_basis()
                    mutate(value)
                    self.assert_blocked(
                        self.invoke(self.request(value), root),
                        "OPERATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
                    )

    def test_exact_boolean_request_and_basis_contracts(self) -> None:
        invalid_values = (None, "false", 0, 1, [], {})
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)

            for field in REQUIRED_FALSE_NON_CLAIMS:
                for invalid in invalid_values:
                    with self.subTest(
                        family="request_non_claim",
                        field=field,
                        value=repr(invalid),
                    ):
                        request = self.request()
                        request["declared_non_claims"][field] = copy.deepcopy(
                            invalid
                        )
                        self.assert_blocked(
                            self.invoke(request, root),
                            "NON_CLAIM_MISSING_OR_FLIPPED",
                        )

            for field in REQUIRED_BASIS_NON_CLAIMS:
                for invalid in invalid_values:
                    with self.subTest(
                        family="basis_non_claim",
                        field=field,
                        value=repr(invalid),
                    ):
                        basis = self.canonical_basis()
                        basis["basis_non_claims"][field] = copy.deepcopy(
                            invalid
                        )
                        self.assert_blocked(
                            self.invoke(self.request(basis), root),
                            "OPERATION_BASIS_NON_CLAIM_MISSING_OR_FLIPPED",
                        )

            posture_families = (
                (
                    "trace_integrity_postures",
                    TRACE_INTEGRITY_POSTURE_KEYS,
                ),
                ("ambiguity_postures", AMBIGUITY_POSTURE_KEYS),
                (
                    "contradiction_postures",
                    CONTRADICTION_POSTURE_KEYS,
                ),
                ("unresolved_postures", UNRESOLVED_POSTURE_KEYS),
            )
            for family, fields in posture_families:
                for field in fields:
                    for invalid in invalid_values:
                        with self.subTest(
                            family=family,
                            field=field,
                            value=repr(invalid),
                        ):
                            basis = self.canonical_basis()
                            basis[family][field] = copy.deepcopy(invalid)
                            self.assert_blocked(
                                self.invoke(self.request(basis), root),
                                "OPERATION_BASIS_POSTURE_MAP_INVALID",
                            )

    def test_bounded_component_validation_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)

            archive_relative = COMPONENT_RELATIVE_PATHS[
                "preserved_archive_path"
            ]
            hash_relative = COMPONENT_RELATIVE_PATHS[
                "archive_hash_record_path"
            ]
            signal_relative = COMPONENT_RELATIVE_PATHS[
                "recorded_signal_path"
            ]

            for label, relative in (
                ("archive_missing", archive_relative),
                ("hash_missing", hash_relative),
                ("signal_missing", signal_relative),
            ):
                with self.subTest(case=label):
                    self._copy_fixture_file(root, relative)
                    (root / relative).unlink()
                    self.assert_blocked(
                        self.recorded_result(root),
                        "BOUNDED_COMPONENT_UNAVAILABLE",
                    )
                    self._copy_fixture_file(root, relative)

            for label, relative in (
                ("archive_directory", archive_relative),
                ("hash_directory", hash_relative),
                ("signal_directory", signal_relative),
            ):
                with self.subTest(case=label):
                    target = self._copy_fixture_file(root, relative)
                    target.unlink()
                    target.mkdir()
                    self.assert_blocked(
                        self.recorded_result(root),
                        "BOUNDED_COMPONENT_UNAVAILABLE",
                    )
                    self._copy_fixture_file(root, relative)

            hash_path = self._copy_fixture_file(root, hash_relative)
            self._write_text(hash_path, "malformed\n")
            self.assert_blocked(
                self.recorded_result(root),
                "ARCHIVE_HASH_RECORD_MALFORMED",
            )
            self._write_text(
                hash_path,
                ("0" * 64) + "  receiver_attestation_001.zip\n",
            )
            self.assert_blocked(
                self.recorded_result(root),
                "ARCHIVE_HASH_MISMATCH",
            )
            self._copy_fixture_file(root, hash_relative)

            archive_path = self._copy_fixture_file(root, archive_relative)
            archive_path.write_bytes(b"changed bounded archive copy")
            self.assert_blocked(
                self.recorded_result(root),
                "ARCHIVE_HASH_MISMATCH",
            )
            self._copy_fixture_file(root, archive_relative)

            for field in TEXT_COMPONENT_FIELDS:
                relative = COMPONENT_RELATIVE_PATHS[field]
                with self.subTest(field=field, case="missing"):
                    target = self._copy_fixture_file(root, relative)
                    target.unlink()
                    self.assert_blocked(
                        self.recorded_result(root),
                        "BOUNDED_COMPONENT_UNAVAILABLE",
                    )
                    self._copy_fixture_file(root, relative)
                with self.subTest(field=field, case="directory"):
                    target = self._copy_fixture_file(root, relative)
                    target.unlink()
                    target.mkdir()
                    self.assert_blocked(
                        self.recorded_result(root),
                        "BOUNDED_COMPONENT_UNAVAILABLE",
                    )
                    self._copy_fixture_file(root, relative)
                with self.subTest(field=field, case="empty"):
                    target = self._copy_fixture_file(root, relative)
                    self._write_text(target, "")
                    result = self.recorded_result(root)
                    self.assert_completed(
                        result,
                        OUTCOME_NOT_RECORDED,
                        OPERATION_RESULT_NOT_RECORDED,
                        "receiver_attestation_not_recorded",
                    )
                    self._copy_fixture_file(root, relative)

            timestamp_relative = COMPONENT_RELATIVE_PATHS[
                "attestation_timestamp_path"
            ]
            timestamp_path = self._copy_fixture_file(
                root, timestamp_relative
            )
            for value in (
                "not-a-timestamp\n",
                "attested_at=2026-07-28T07:37:56+01:00\n",
            ):
                with self.subTest(timestamp=value.strip()):
                    self._write_text(timestamp_path, value)
                    result = self.recorded_result(root)
                    self.assert_completed(
                        result,
                        OUTCOME_NOT_RECORDED,
                        OPERATION_RESULT_NOT_RECORDED,
                        "receiver_attestation_not_recorded",
                    )
            self._copy_fixture_file(root, timestamp_relative)

    def test_summary_determinism_for_every_branch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            results = (
                self.invoke(self.request(), root),
                self.recorded_result(root),
                self.not_recorded_result(root),
                self.indeterminate_result(root),
                self.invoke(
                    self.request(intent=resolver.INTENT_BLOCK),
                    root,
                ),
            )
            for result in results:
                with self.subTest(outcome=result["outcome"]):
                    before = copy.deepcopy(result)
                    first = build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary(
                        result
                    )
                    second = build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary(
                        result
                    )
                    self.assertEqual(first, second)
                    self.assertEqual(result, before)
                    self.assertEqual(first, self.summary(result))
                    self.assertEqual(first["resolver_module"], RESOLVER_MODULE)
                    self.assertEqual(first["result_version"], RESULT_VERSION)
                    self.assertEqual(first["operation_id"], OPERATION_ID)
                    self.assertEqual(first["operation_type"], OPERATION_TYPE)
                    self.assertEqual(
                        first["operation_version"], OPERATION_VERSION
                    )
                    self.assertEqual(first["operation_scope"], OPERATION_SCOPE)
                    self.assertEqual(
                        first["selected_candidate_id"], CANDIDATE_ID
                    )
                    self.assertEqual(
                        first["selected_boundary_id"],
                        SELECTED_BOUNDARY_ID,
                    )
                    self.assertEqual(first["outcome"], result["outcome"])
                    self.assertEqual(
                        first["failed_check_count"],
                        result["failed_check_count"],
                    )
                    self.assertEqual(
                        first["passed_check_count"],
                        result["passed_check_count"],
                    )
                    self.assertIs(
                        first["result_level_non_claims_canonical_false"],
                        True,
                    )
                    self.assertEqual(
                        first["governing_paths"],
                        result["upstream_boundary_basis"][
                            "governing_paths"
                        ],
                    )
                    for key in (
                        "blocked",
                        "basis_supplied",
                        "basis_admitted",
                        "upstream_boundary_validated",
                        "trace_paths_validated",
                        "archive_correspondence_validated",
                        "text_components_validated",
                        "timestamp_validated",
                        "recorded_signal_artifact_existence_validated",
                        "any_ambiguity",
                        "any_contradiction",
                        "any_unresolved",
                        "receiver_attestation_recorded",
                        "receiver_attestation_not_recorded",
                        "receiver_attestation_indeterminate",
                        "receiver_attestation_operation_recorded",
                        "receiver_attestation_operation_exhausted",
                    ):
                        self.assertIn(key, first)

    def test_from_path_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            waiting_path = self._write_json(
                root / "requests/waiting.json",
                self.request(),
            )
            recorded_path = self._write_json(
                root / "requests/recorded.json",
                self.request(self.canonical_basis()),
            )
            with patch.object(resolver, "REPO_ROOT", root):
                waiting = resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path(
                    waiting_path
                )
                recorded = resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path(
                    recorded_path
                )
            self.assertEqual(waiting["outcome"], OUTCOME_REQUIRES_BASIS)
            self.assertEqual(recorded["outcome"], OUTCOME_RECORDED)
            self.assertEqual(waiting["resolver_module"], RESOLVER_MODULE)
            self.assertEqual(recorded["result_version"], RESULT_VERSION)

            malformed = self._write_text(
                root / "requests/malformed.json", "{"
            )
            duplicate = self._write_text(
                root / "requests/duplicate.json",
                '{"intent":"a","intent":"b"}\n',
            )
            array = self._write_json(root / "requests/array.json", [])
            missing = root / "requests/missing.json"
            for path in (malformed, duplicate, array, missing):
                with self.subTest(path=path.name):
                    with patch.object(resolver, "REPO_ROOT", root):
                        result = resolve_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_from_path(
                            path
                        )
                    self.assert_blocked(result, "REQUEST_NOT_MAPPING")
                    self.assertEqual(result["resolver_module"], RESOLVER_MODULE)
                    self.assertEqual(result["result_version"], RESULT_VERSION)

    def test_writer_valid_branches_format_and_suffix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            results = {
                "waiting": self.invoke(self.request(), root),
                "blocked": self.invoke(
                    self.request(intent=resolver.INTENT_BLOCK),
                    root,
                ),
                "recorded": self.recorded_result(root),
                "not_recorded": self.not_recorded_result(root),
                "indeterminate": self.indeterminate_result(root),
            }
            output_root = root / "outputs"
            for label, result in results.items():
                with self.subTest(branch=label):
                    target = output_root / label / OUTPUT_FILENAME
                    written = write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result(
                        result,
                        target,
                    )
                    self.assertIsInstance(written, Path)
                    self.assertEqual(written, target)
                    self.assertTrue(written.is_file())
                    text = written.read_text(encoding="utf-8")
                    self.assertTrue(text.endswith("\n"))
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

            target = output_root / "recorded" / OUTPUT_FILENAME
            original = target.read_bytes()
            suffixed = write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result(
                results["recorded"],
                target,
            )
            self.assertEqual(
                suffixed.name,
                target.stem + "_001" + target.suffix,
            )
            self.assertEqual(target.read_bytes(), original)

    def test_writer_refuses_malformed_results_and_protected_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            waiting = self.invoke(self.request(), root)
            blocked = self.invoke(
                self.request(intent=resolver.INTENT_BLOCK),
                root,
            )
            recorded = self.recorded_result(root)
            not_recorded = self.not_recorded_result(root)
            indeterminate = self.indeterminate_result(root)
            output = root / "writer_refusals"

            malformed: list[tuple[str, Any]] = [("not_mapping", [])]
            wrong_module = copy.deepcopy(recorded)
            wrong_module["resolver_module"] = "other"
            malformed.append(("wrong_module", wrong_module))
            wrong_version = copy.deepcopy(recorded)
            wrong_version["result_version"] = "other"
            malformed.append(("wrong_version", wrong_version))

            branch_results = (
                ("waiting", waiting),
                ("blocked", blocked),
                ("recorded", recorded),
                ("not_recorded", not_recorded),
                ("indeterminate", indeterminate),
            )
            for label, source in branch_results:
                value = copy.deepcopy(source)
                value[OPERATION_OBJECT_KEY][
                    "receiver_attestation_operation_exhausted"
                ] = not value[OPERATION_OBJECT_KEY][
                    "receiver_attestation_operation_exhausted"
                ]
                malformed.append(("inconsistent_" + label, value))

            multiple = copy.deepcopy(recorded)
            multiple[OPERATION_OBJECT_KEY][
                "receiver_attestation_not_recorded"
            ] = True
            malformed.append(("multiple_branches", multiple))
            missing_non_claim = copy.deepcopy(recorded)
            missing_non_claim["non_claims"].pop(
                REQUIRED_FALSE_NON_CLAIMS[0]
            )
            malformed.append(("missing_non_claim", missing_non_claim))
            flipped_non_claim = copy.deepcopy(recorded)
            flipped_non_claim["non_claims"][
                REQUIRED_FALSE_NON_CLAIMS[0]
            ] = True
            malformed.append(("flipped_non_claim", flipped_non_claim))

            complete_material = (
                (
                    "upstream",
                    "complete_upstream_boundary_artifact",
                    {"full": "artifact"},
                ),
                (
                    "basis",
                    "receiver_attestation_operation_basis",
                    {"full": "basis"},
                ),
                ("archive", "archive_bytes", b"archive"),
                (
                    "text",
                    "attestation_statement_body",
                    "complete body",
                ),
                ("signal", "recorded_signal_body", {"samples": []}),
            )
            for label, key, embedded in complete_material:
                value = copy.deepcopy(recorded)
                value[
                    "receiver_side_answerable_basis_"
                    "receiver_attestation_operation_metadata"
                ][key] = embedded
                malformed.append(("complete_" + label, value))

            for label, value in malformed:
                with self.subTest(malformed=label):
                    with self.assertRaises(
                        ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError
                    ):
                        write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result(
                            value,
                            output / label / OUTPUT_FILENAME,
                        )

            protected = (
                Path("spec") / OUTPUT_FILENAME,
                Path("src") / OUTPUT_FILENAME,
                Path("tests") / OUTPUT_FILENAME,
                Path("reference") / OUTPUT_FILENAME,
                SELECTED_BOUNDARY_ARTIFACT_RELATIVE_PATH.parent
                / OUTPUT_FILENAME,
                SELECTED_CANDIDATE_SUFFICIENCY_ARTIFACT_RELATIVE_PATH.parent
                / OUTPUT_FILENAME,
                BOUNDED_CAPTURE_DIRECTORY_RELATIVE_PATH / OUTPUT_FILENAME,
            )
            for path in protected:
                with self.subTest(protected=str(path)):
                    with (
                        patch.object(resolver, "REPO_ROOT", root),
                        self.assertRaises(
                            ReceiverSideAnswerableBasisReceiverAttestationOperationV0MinError
                        ),
                    ):
                        write_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_result(
                            recorded,
                            path,
                        )

    def test_determinism_immutability_and_declared_override_visibility(
        self,
    ) -> None:
        first = build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        second = build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"],
            second["declared_non_claims"],
        )
        first["declared_non_claims"][
            REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        third = build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_request()
        self.assertIs(
            third["declared_non_claims"][
                REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            request = self.request(self.canonical_basis())
            before = copy.deepcopy(request)
            one = self.invoke(request, root)
            two = self.invoke(copy.deepcopy(request), root)
            self.assertEqual(request, before)
            self.assertEqual(one, two)
            one_before = copy.deepcopy(one)
            build_receiver_side_answerable_basis_receiver_attestation_operation_v0_min_summary(
                one
            )
            self.assertEqual(one, one_before)

            declared = self.request(unknown_override="visible")
            self.assertEqual(declared["unknown_override"], "visible")
            self.assert_blocked(
                self.invoke(declared, root),
                "REQUEST_UNKNOWN_FIELD",
            )

        current_hashes = {
            str(relative): self._sha256(REPOSITORY_ROOT / relative)
            for relative in PRESERVED_FIXTURE_PATHS
        }
        self.assertEqual(current_hashes, self.preserved_hashes)

    def test_non_meaning_and_no_downstream_conversion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            results = (
                self.invoke(self.request(), root),
                self.recorded_result(root),
                self.not_recorded_result(root),
                self.indeterminate_result(root),
                self.invoke(
                    self.request(intent=resolver.INTENT_BLOCK),
                    root,
                ),
            )
            for result in results:
                with self.subTest(outcome=result["outcome"]):
                    statement = result[
                        "receiver_side_answerable_basis_"
                        "receiver_attestation_operation_statement"
                    ]
                    for field in (
                        "occurrence_not_created_by_source_body",
                        "artifact_does_not_create_occurrence",
                        "preserved_trace_not_independent_verification",
                        "candidate_sufficient_not_receiver_attestation",
                        "consideration_allowed_not_receiver_attestation",
                        "operation_authorization_not_operation_result",
                        "receiver_attestation_recorded_not_receiver_answerable_receipt",
                        "receiver_attestation_recorded_not_presence",
                        "receiver_attestation_recorded_not_identity_authority_truth_or_standing",
                        "open_does_not_mean_next",
                    ):
                        self.assertIs(statement[field], True)
                    non_meaning = result[
                        "receiver_side_answerable_basis_"
                        "receiver_attestation_operation_non_meaning"
                    ]
                    self.assertIs(
                        non_meaning[
                            "completed_result_is_not_downstream_authorization"
                        ],
                        True,
                    )
                    operation = self.operation(result)
                    for field in (
                        "receiver_answerable_receipt_present",
                        "presence_established",
                        "identity_created",
                        "truth_created",
                        "authority_created",
                        "standing_created",
                        "follow_on_authorized",
                        "follow_on_work_authorized",
                    ):
                        self.assertIs(operation[field], False)


if __name__ == "__main__":
    unittest.main()
