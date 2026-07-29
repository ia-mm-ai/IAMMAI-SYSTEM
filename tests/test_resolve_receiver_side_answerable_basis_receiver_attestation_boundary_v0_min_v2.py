"""Tests for the corrected v2 receiver-attestation consideration boundary.

V1 remains preserved failed lineage.  This suite exercises only the additive
v2 resolver and proves that its seven corrected upstream false locks require
exact Boolean false at the canonical operation-posture location.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping, Sequence
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2 as resolver
from resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2 import (
    BOUNDARY_RESULT_ALLOWED,
    BOUNDARY_RESULT_NOT_ALLOWED,
    BOUNDARY_RESULT_NOT_EVALUATED,
    CORRECTED_UPSTREAM_FALSE_POSTURES,
    OUTCOME_ALLOWED,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_ALLOWED,
    REQUIRED_UPSTREAM_FALSE_POSTURES,
    RESOLVER_MODULE,
    RESULT_VERSION,
    ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error,
    build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request,
    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request,
    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary,
    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2,
    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_from_path,
    write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result,
)


V1_RESOLVER_PATH = REPO_ROOT / (
    "src/resolve_receiver_side_answerable_basis_"
    "receiver_attestation_boundary_v0_min.py"
)
V2_RESOLVER_PATH = REPO_ROOT / (
    "src/resolve_receiver_side_answerable_basis_"
    "receiver_attestation_boundary_v0_min_v2.py"
)
V1_TEST_PATH = REPO_ROOT / (
    "tests/test_resolve_receiver_side_answerable_basis_"
    "receiver_attestation_boundary_v0_min.py"
)
SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPEC_RELATIVE_PATH
UPSTREAM_ARTIFACT_PATH = (
    REPO_ROOT / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
)
OPERATION_KEY = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation"
)
DIMENSIONS_KEY = (
    "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
)
EXACT_CORRECTED_FALSE_LOCKS = (
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "affected_file_repaired",
    "repository_scan_performed",
    "file_discovery_performed",
    "validation_enforced",
)


class ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Tests(
    unittest.TestCase
):
    """Verify preserved v1 behavior and the exact v2 false-lock correction."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = (
            V1_RESOLVER_PATH,
            V2_RESOLVER_PATH,
            V1_TEST_PATH,
            SPECIFICATION_PATH,
            UPSTREAM_ARTIFACT_PATH,
        )
        for path in cls._preserved_paths:
            if not path.is_file():
                raise AssertionError(f"required preserved input is missing: {path}")
        cls._preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in cls._preserved_paths
        }
        cls._specification_text = SPECIFICATION_PATH.read_text(encoding="utf-8")
        cls._upstream_artifact = json.loads(
            UPSTREAM_ARTIFACT_PATH.read_text(encoding="utf-8")
        )
        if not isinstance(cls._upstream_artifact, dict):
            raise AssertionError("canonical upstream artifact is not a mapping")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected_hash in cls._preserved_hashes.items():
            actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual_hash != expected_hash:
                raise AssertionError(f"preserved input changed: {path}")

    def canonical_request(self, **overrides: object) -> dict[str, object]:
        return (
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(
                **copy.deepcopy(overrides)
            )
        )

    def live_artifact(self) -> dict[str, object]:
        return copy.deepcopy(self._upstream_artifact)

    def operation(self, artifact: dict[str, object]) -> dict[str, object]:
        operation = artifact.get(OPERATION_KEY)
        self.assertIsInstance(operation, dict)
        return operation

    def dimensions(self, artifact: dict[str, object]) -> dict[str, object]:
        dimensions = artifact.get(DIMENSIONS_KEY)
        self.assertIsInstance(dimensions, dict)
        return dimensions

    def boundary(self, result: Mapping[str, object]) -> dict[str, object]:
        boundary = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary"
        )
        self.assertIsInstance(boundary, dict)
        return boundary

    def upstream(self, result: Mapping[str, object]) -> dict[str, object]:
        upstream = result.get("upstream_basis")
        self.assertIsInstance(upstream, dict)
        return upstream

    def checks(self, result: Mapping[str, object]) -> list[dict[str, object]]:
        checks = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary_checks"
        )
        self.assertIsInstance(checks, list)
        self.assertTrue(all(isinstance(check, dict) for check in checks))
        return checks

    def block_code(self, result: Mapping[str, object]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("code") or block.get("block_code")
        self.assertTrue(code is None or isinstance(code, str))
        return code

    def write_text(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(
            path.is_dir(),
            f"fixture path collision: JSON target is a directory: {path}",
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

    def install_fixture(
        self,
        root: Path,
        *,
        artifact: object | None = None,
        specification_text: str | None = None,
        include_artifact: bool = True,
        include_specification: bool = True,
    ) -> None:
        if include_specification:
            self.write_text(
                root / resolver.GOVERNING_SPEC_RELATIVE_PATH,
                (
                    self._specification_text
                    if specification_text is None
                    else specification_text
                ),
            )
        if include_artifact:
            self.write_json(
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH,
                self.live_artifact() if artifact is None else artifact,
            )

    def invoke(
        self,
        request: object | None = None,
        *,
        root: Path | None = None,
    ) -> dict[str, object]:
        supplied = copy.deepcopy(request)
        before = copy.deepcopy(supplied)
        if root is None:
            result = (
                resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2(
                        supplied
                    )
                )
        self.assertEqual(supplied, before)
        self.assertIsInstance(result, dict)
        return result

    def resolve_fixture(
        self,
        *,
        request: dict[str, object] | None = None,
        artifact: object | None = None,
        specification_text: str | None = None,
        include_artifact: bool = True,
        include_specification: bool = True,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(
                root,
                artifact=artifact,
                specification_text=specification_text,
                include_artifact=include_artifact,
                include_specification=include_specification,
            )
            return self.invoke(
                self.canonical_request() if request is None else request,
                root=root,
            )

    def assert_non_claims_false(
        self, result: Mapping[str, object]
    ) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(
            set(non_claims),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        boundary = self.boundary(result)
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[field], False, field)
            self.assertIs(boundary[field], False, field)

    def assert_no_complete_material(
        self, result: Mapping[str, object]
    ) -> None:
        upstream = self.upstream(result)
        self.assertIs(upstream["complete_operation_artifact_omitted"], True)
        self.assertIs(upstream["complete_sufficiency_basis_omitted"], True)
        self.assertIs(upstream["complete_capture_signal_data_omitted"], True)

        forbidden_keys = {
            "complete_sufficiency_operation_artifact",
            "sufficiency_basis_records",
            "basis_items",
            "basis_references",
            DIMENSIONS_KEY,
            "capture_signal_data",
            "signal_samples",
            "raw_signal_data",
            "complete_capture_material",
        }

        def visit(value: object) -> None:
            if isinstance(value, Mapping):
                self.assertTrue(
                    forbidden_keys.isdisjoint(value),
                    forbidden_keys.intersection(value),
                )
                for nested in value.values():
                    visit(nested)
            elif isinstance(value, Sequence) and not isinstance(
                value, (str, bytes, bytearray)
            ):
                for nested in value:
                    visit(nested)

        visit(result)

    def assert_public_codes(self, result: Mapping[str, object]) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for key in ("failure_code", "block_code"):
                if key in check:
                    self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_blocked(
        self,
        result: Mapping[str, object],
        expected_code: str | None = None,
    ) -> None:
        self.assertEqual(result.get("resolver_module"), RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), RESULT_VERSION)
        self.assertEqual(result.get("outcome"), OUTCOME_BLOCKED)
        self.assertEqual(
            self.boundary(result).get("receiver_attestation_boundary_result"),
            BOUNDARY_RESULT_NOT_EVALUATED,
        )
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        for field in (
            "receiver_attestation_boundary_recorded",
            "receiver_attestation_boundary_result_recorded",
            "receiver_attestation_consideration_allowed",
            "receiver_attestation_consideration_not_allowed",
            "receiver_attestation_boundary_exhausted",
        ):
            self.assertIs(self.boundary(result)[field], False, field)
        self.assert_non_claims_false(result)
        self.assert_no_complete_material(result)
        self.assert_public_codes(result)

    def assert_completed(
        self,
        result: Mapping[str, object],
        *,
        outcome: str,
        boundary_result: str,
        allowed: bool,
    ) -> None:
        self.assertEqual(result.get("resolver_module"), RESOLVER_MODULE)
        self.assertEqual(result.get("result_version"), RESULT_VERSION)
        self.assertEqual(result.get("outcome"), outcome)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["receiver_attestation_boundary_result"],
            boundary_result,
        )
        self.assertIs(boundary["receiver_attestation_boundary_recorded"], True)
        self.assertIs(
            boundary["receiver_attestation_boundary_result_recorded"], True
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_allowed"], allowed
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_not_allowed"],
            not allowed,
        )
        self.assertIs(boundary["receiver_attestation_boundary_exhausted"], True)
        self.assertIs(
            boundary["selected_candidate_sufficiency_operation_validated"],
            True,
        )
        self.assertIs(boundary["selected_candidate_sufficient"], True)
        self.assert_non_claims_false(result)
        self.assert_no_complete_material(result)

    def assert_corrected_audit(
        self,
        result: Mapping[str, object],
        *,
        false_field: str | None = None,
    ) -> None:
        upstream = self.upstream(result)
        self.assertEqual(
            tuple(upstream["required_upstream_false_lock_fields"]),
            REQUIRED_UPSTREAM_FALSE_POSTURES,
        )
        self.assertEqual(
            tuple(upstream["corrected_upstream_false_lock_fields"]),
            EXACT_CORRECTED_FALSE_LOCKS,
        )
        validation = upstream["corrected_upstream_false_lock_validation"]
        self.assertIsInstance(validation, dict)
        self.assertEqual(set(validation), set(EXACT_CORRECTED_FALSE_LOCKS))
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            self.assertIs(
                validation[field],
                field != false_field,
                field,
            )

    def assert_single_canonical_operation_change(
        self,
        before: dict[str, object],
        after: dict[str, object],
        field: str,
        *,
        removed: bool = False,
    ) -> None:
        self.assertEqual(
            {key: value for key, value in before.items() if key != OPERATION_KEY},
            {key: value for key, value in after.items() if key != OPERATION_KEY},
        )
        before_operation = self.operation(before)
        after_operation = self.operation(after)
        if removed:
            self.assertEqual(
                set(before_operation).difference(after_operation),
                {field},
            )
            self.assertEqual(
                {
                    key: value
                    for key, value in before_operation.items()
                    if key != field
                },
                after_operation,
            )
        else:
            self.assertEqual(set(before_operation), set(after_operation))
            self.assertEqual(
                {
                    key: value
                    for key, value in before_operation.items()
                    if key != field
                },
                {
                    key: value
                    for key, value in after_operation.items()
                    if key != field
                },
            )

    def test_public_surface_metadata_and_canonical_request(self) -> None:
        for public_value in (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request,
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request,
            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2,
            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_from_path,
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary,
            write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result,
        ):
            self.assertTrue(callable(public_value))
        self.assertTrue(
            issubclass(
                ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error,
                Exception,
            )
        )
        self.assertEqual(
            RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_"
            "receiver_attestation_boundary_v0_min_v2",
        )
        self.assertEqual(RESULT_VERSION, "0.2.0")
        self.assertEqual(
            resolver.BOUNDARY_ID,
            "receiver_side_answerable_basis_receiver_attestation_boundary_001",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY",
        )
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.BOUNDARY_SCOPE,
            "CONSIDER_RECEIVER_ATTESTATION_FOR_ONE_SUFFICIENT_"
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY",
        )
        self.assertEqual(
            resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_001",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
            "receiver_side_answerable_basis_"
            "candidate_sufficiency_operation_001",
        )
        self.assertEqual(
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_SUFFICIENT",
        )
        self.assertEqual(
            resolver.GOVERNING_SPEC_RELATIVE_PATH,
            Path(
                "spec/RECEIVER_SIDE_ANSWERABLE_BASIS_"
                "RECEIVER_ATTESTATION_BOUNDARY_V0_MIN_SPEC.md"
            ),
        )
        self.assertEqual(
            resolver.BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH,
            Path(
                "artifacts/actual_receiver_attestation_capture/"
                "receiver_attestation_capture_001"
            ),
        )
        self.assertEqual(
            CORRECTED_UPSTREAM_FALSE_POSTURES,
            EXACT_CORRECTED_FALSE_LOCKS,
        )
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            self.assertEqual(
                REQUIRED_UPSTREAM_FALSE_POSTURES.count(field),
                1,
                field,
            )
        request = self.canonical_request()
        self.assertEqual(
            request,
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(),
        )
        self.assertEqual(request["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(
            request["selected_candidate_sufficiency_operation_id"],
            resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
        )
        self.assertEqual(
            request["selected_candidate_sufficiency_operation_result_required"],
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
        )
        self.assertEqual(
            request["governing_receiver_attestation_boundary_specification_path"],
            str(resolver.GOVERNING_SPEC_RELATIVE_PATH),
        )
        self.assertEqual(
            request["bounded_existing_material_path"],
            str(resolver.BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH),
        )

    def test_canonical_allowed_branch_and_v2_audit(self) -> None:
        result = self.invoke()
        self.assert_completed(
            result,
            outcome=OUTCOME_ALLOWED,
            boundary_result=BOUNDARY_RESULT_ALLOWED,
            allowed=True,
        )
        summary = result[
            "receiver_side_answerable_basis_receiver_attestation_boundary_summary"
        ]
        self.assertIs(summary["eight_dimensions_validated"], True)
        self.assertIs(summary["upstream_false_locks_validated"], True)
        self.assert_corrected_audit(result)
        full_validation = self.upstream(result)["false_lock_validation"]
        self.assertTrue(all(full_validation.values()))

    def test_canonical_not_allowed_branch_and_v2_audit(self) -> None:
        request = self.canonical_request(
            bounded_material_selected_for_consideration=False
        )
        self.assertEqual(
            request["bounded_material_selection_posture"],
            resolver.BOUNDED_MATERIAL_NOT_SELECTED,
        )
        self.assertIsNone(request["bounded_existing_material_path"])
        result = self.invoke(request)
        self.assert_completed(
            result,
            outcome=OUTCOME_NOT_ALLOWED,
            boundary_result=BOUNDARY_RESULT_NOT_ALLOWED,
            allowed=False,
        )
        self.assert_corrected_audit(result)
        for field in (
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "presence_established",
            "identity_created",
            "standing_created",
            "authority_created",
            "truth_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(self.boundary(result)[field], False, field)

    def test_corrected_false_locks_true_block_with_isolation(self) -> None:
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            with self.subTest(field=field):
                before = self.live_artifact()
                artifact = copy.deepcopy(before)
                self.operation(artifact)[field] = True
                self.assert_single_canonical_operation_change(
                    before,
                    artifact,
                    field,
                )
                result = self.resolve_fixture(artifact=artifact)
                self.assert_blocked(
                    result,
                    "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                )
                self.assert_corrected_audit(result, false_field=field)
                full_validation = self.upstream(result)[
                    "false_lock_validation"
                ]
                self.assertEqual(
                    {key for key, valid in full_validation.items() if not valid},
                    {field},
                )

    def test_corrected_false_locks_missing_block(self) -> None:
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            with self.subTest(field=field):
                before = self.live_artifact()
                artifact = copy.deepcopy(before)
                self.operation(artifact).pop(field)
                self.assert_single_canonical_operation_change(
                    before,
                    artifact,
                    field,
                    removed=True,
                )
                result = self.resolve_fixture(artifact=artifact)
                self.assert_blocked(
                    result,
                    "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                )
                self.assert_corrected_audit(result, false_field=field)

    def test_corrected_false_locks_require_exact_boolean_false(self) -> None:
        wrong_values = (None, "false", 0, [], {})
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            for wrong_value in wrong_values:
                with self.subTest(field=field, value=repr(wrong_value)):
                    before = self.live_artifact()
                    artifact = copy.deepcopy(before)
                    self.operation(artifact)[field] = copy.deepcopy(
                        wrong_value
                    )
                    self.assert_single_canonical_operation_change(
                        before,
                        artifact,
                        field,
                    )
                    result = self.resolve_fixture(artifact=artifact)
                    self.assert_blocked(
                        result,
                        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                    )
                    self.assert_corrected_audit(result, false_field=field)

    def test_corrected_false_locks_wrong_location_does_not_substitute(self) -> None:
        for field in EXACT_CORRECTED_FALSE_LOCKS:
            with self.subTest(field=field):
                artifact = self.live_artifact()
                self.operation(artifact).pop(field)
                artifact["noncanonical_false_lock_posture"] = {field: False}
                result = self.resolve_fixture(artifact=artifact)
                self.assert_blocked(
                    result,
                    "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                )
                self.assert_corrected_audit(result, false_field=field)

    def test_complete_required_upstream_false_lock_family_blocks(self) -> None:
        self.assertTrue(
            set(EXACT_CORRECTED_FALSE_LOCKS).issubset(
                REQUIRED_UPSTREAM_FALSE_POSTURES
            )
        )
        for field in REQUIRED_UPSTREAM_FALSE_POSTURES:
            with self.subTest(field=field):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = True
                result = self.resolve_fixture(artifact=artifact)
                expected_code = (
                    "UPSTREAM_CANDIDATE_RESULT_CONFLICT"
                    if field
                    in {
                        "receiver_side_answerable_basis_candidate_insufficient",
                        "receiver_side_answerable_basis_candidate_indeterminate",
                    }
                    else "UPSTREAM_FALSE_LOCK_NOT_FALSE"
                )
                self.assert_blocked(result, expected_code)

    def test_preserved_request_blocking_contract(self) -> None:
        cases: list[tuple[str, object, str]] = [
            ("non_mapping", [], "REQUEST_NOT_MAPPING"),
            (
                "unsupported_intent",
                self.canonical_request(intent="UNSUPPORTED"),
                "UNSUPPORTED_INTENT",
            ),
            (
                "explicit_block",
                self.canonical_request(intent=resolver.INTENT_BLOCK),
                "EXPLICIT_BLOCK_REQUESTED",
            ),
            (
                "unknown_field",
                self.canonical_request(unknown_field=True),
                "REQUEST_UNKNOWN_FIELD",
            ),
            (
                "result_preclaim",
                self.canonical_request(outcome=OUTCOME_ALLOWED),
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                "prohibited_downstream",
                self.canonical_request(request_follow_on_authorization=True),
                "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            ),
        ]
        missing = self.canonical_request()
        missing.pop("boundary_scope")
        cases.append(("missing_field", missing, "REQUEST_FIELD_MISSING"))
        for label, request, expected_code in cases:
            with self.subTest(case=label):
                self.assert_blocked(self.invoke(request), expected_code)

    def test_preserved_specification_and_upstream_file_contract(self) -> None:
        self.assert_blocked(
            self.resolve_fixture(include_specification=False),
            "RECEIVER_ATTESTATION_BOUNDARY_SPEC_REFERENCE_MISSING",
        )
        changed_specification = self._specification_text.replace(
            "Candidate sufficient is not receiver attestation.",
            "",
        )
        self.assertNotEqual(changed_specification, self._specification_text)
        self.assert_blocked(
            self.resolve_fixture(specification_text=changed_specification),
            "RECEIVER_ATTESTATION_BOUNDARY_SPEC_MARKER_MISSING",
        )
        self.assert_blocked(
            self.resolve_fixture(include_artifact=False),
            "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_REFERENCE_MISSING",
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(root)
            artifact_path = (
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
            )
            self.write_text(artifact_path, "{")
            self.assert_blocked(
                self.invoke(self.canonical_request(), root=root),
                "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_PARSEABLE",
            )

        artifact = self.live_artifact()
        artifact["resolver_module"] = "other"
        self.assert_blocked(
            self.resolve_fixture(artifact=artifact),
            "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
        )

    def test_preserved_operation_and_dimension_blocking_contract(self) -> None:
        operation_cases = (
            (
                "candidate_result_not_sufficient",
                "operation_result",
                "OTHER",
                "UPSTREAM_OPERATION_RESULT_MISMATCH",
            ),
            (
                "operation_not_recorded",
                "candidate_sufficiency_operation_recorded",
                False,
                "UPSTREAM_OPERATION_NOT_RECORDED",
            ),
            (
                "operation_not_exhausted",
                "candidate_sufficiency_operation_exhausted",
                False,
                "UPSTREAM_OPERATION_NOT_EXHAUSTED",
            ),
        )
        for label, field, value, expected_code in operation_cases:
            with self.subTest(operation_case=label):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = value
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

        first_dimension = resolver.REQUIRED_DIMENSION_IDS[0]
        dimension_cases: list[tuple[str, dict[str, object], str]] = []

        artifact = self.live_artifact()
        self.dimensions(artifact).pop(first_dimension)
        dimension_cases.append(
            ("missing", artifact, "UPSTREAM_DIMENSION_SET_MISMATCH")
        )

        artifact = self.live_artifact()
        self.dimensions(artifact)["additional"] = copy.deepcopy(
            self.dimensions(artifact)[first_dimension]
        )
        dimension_cases.append(
            ("additional", artifact, "UPSTREAM_DIMENSION_SET_MISMATCH")
        )

        for label, key, value, expected_code in (
            (
                "not_satisfied",
                "dimension_result",
                "INDETERMINATE",
                "UPSTREAM_DIMENSION_NOT_SATISFIED",
            ),
            (
                "not_evaluated",
                "dimension_evaluated",
                False,
                "UPSTREAM_DIMENSION_NOT_EVALUATED",
            ),
            (
                "not_established",
                "dimension_established",
                False,
                "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
            ),
        ):
            artifact = self.live_artifact()
            entry = self.dimensions(artifact)[first_dimension]
            self.assertIsInstance(entry, dict)
            entry[key] = value
            dimension_cases.append((label, artifact, expected_code))

        for label, artifact, expected_code in dimension_cases:
            with self.subTest(dimension_case=label):
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

    def test_summaries_are_v2_deterministic_and_material_omitting(self) -> None:
        corrected_artifact = self.live_artifact()
        corrected_field = EXACT_CORRECTED_FALSE_LOCKS[0]
        self.operation(corrected_artifact)[corrected_field] = True
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    bounded_material_selected_for_consideration=False
                )
            ),
            self.resolve_fixture(artifact=corrected_artifact),
        )
        expected = (
            (OUTCOME_ALLOWED, BOUNDARY_RESULT_ALLOWED, True),
            (OUTCOME_NOT_ALLOWED, BOUNDARY_RESULT_NOT_ALLOWED, True),
            (OUTCOME_BLOCKED, BOUNDARY_RESULT_NOT_EVALUATED, False),
        )
        for result, (
            expected_outcome,
            expected_boundary_result,
            expected_recorded,
        ) in zip(results, expected, strict=True):
            with self.subTest(outcome=expected_outcome):
                before = copy.deepcopy(result)
                first = (
                    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary(
                        result
                    )
                )
                second = (
                    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary(
                        result
                    )
                )
                self.assertEqual(first, second)
                self.assertEqual(result, before)
                self.assertEqual(first["resolver_module"], RESOLVER_MODULE)
                self.assertEqual(first["result_version"], RESULT_VERSION)
                self.assertEqual(first["outcome"], expected_outcome)
                self.assertEqual(
                    first["boundary_result"],
                    expected_boundary_result,
                )
                self.assertIs(
                    first["receiver_attestation_boundary_recorded"],
                    expected_recorded,
                )
                self.assertIs(
                    first["receiver_attestation_boundary_exhausted"],
                    expected_recorded,
                )
                corrected_validation = self.upstream(result)[
                    "corrected_upstream_false_lock_validation"
                ]
                self.assertEqual(
                    first["upstream_false_locks_validated"],
                    all(corrected_validation.values())
                    and all(
                        self.upstream(result)["false_lock_validation"].values()
                    ),
                )
                self.assertIs(
                    first["complete_operation_artifact_omitted"], True
                )
                self.assertIs(
                    first["complete_sufficiency_basis_omitted"], True
                )
                self.assertIs(
                    first["complete_capture_signal_data_omitted"], True
                )

    def test_from_path_contract_preserves_v2_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.install_fixture(root)
            request = self.canonical_request()
            request_path = self.write_json(root / "request.json", request)
            with patch.object(resolver, "REPO_ROOT", root):
                direct = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2(
                        request
                    )
                )
                from_path = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_from_path(
                        request_path
                    )
                )
            self.assertEqual(from_path, direct)
            self.assert_completed(
                from_path,
                outcome=OUTCOME_ALLOWED,
                boundary_result=BOUNDARY_RESULT_ALLOWED,
                allowed=True,
            )

            malformed_path = self.write_text(root / "malformed.json", "{")
            non_mapping_path = self.write_json(root / "non_mapping.json", [])
            missing_path = root / "missing.json"
            for label, path in (
                ("malformed", malformed_path),
                ("non_mapping", non_mapping_path),
                ("missing", missing_path),
            ):
                with self.subTest(path_case=label):
                    with patch.object(resolver, "REPO_ROOT", root):
                        result = (
                            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_from_path(
                                path
                            )
                        )
                    self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_writer_valid_branches_suffix_and_distinct_v2_family(self) -> None:
        corrected_artifact = self.live_artifact()
        self.operation(corrected_artifact)[
            EXACT_CORRECTED_FALSE_LOCKS[0]
        ] = True
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    bounded_material_selected_for_consideration=False
                )
            ),
            self.resolve_fixture(artifact=corrected_artifact),
        )
        self.assertEqual(
            resolver.OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_receiver_side_answerable_"
            "basis_receiver_attestation_boundary_v0_min_v2",
        )
        self.assertNotEqual(
            resolver.OUTPUT_ROOT.name,
            "integrity_host_v0_min_coexistence_receiver_side_answerable_"
            "basis_receiver_attestation_boundary_v0_min",
        )
        self.assertIn("_v0_min_v2_result.json", resolver.OUTPUT_FILENAME)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, result in enumerate(results):
                with self.subTest(outcome=result["outcome"]):
                    target = (
                        root
                        / f"branch_{index}"
                        / resolver.OUTPUT_FILENAME
                    )
                    written = (
                        write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
                            result,
                            target,
                        )
                    )
                    self.assertIsInstance(written, Path)
                    self.assertEqual(written, target)
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

            target = root / "suffix" / resolver.OUTPUT_FILENAME
            first = (
                write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
                    results[0],
                    target,
                )
            )
            first_bytes = first.read_bytes()
            second = (
                write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
                    results[0],
                    target,
                )
            )
            self.assertEqual(second.name, first.stem + "_001" + first.suffix)
            self.assertEqual(first.read_bytes(), first_bytes)

    def test_writer_refusals_and_protected_paths(self) -> None:
        allowed = self.invoke()
        not_allowed = self.invoke(
            self.canonical_request(
                bounded_material_selected_for_consideration=False
            )
        )
        invalid_results: list[tuple[str, object]] = [("non_mapping", [])]

        wrong_module = copy.deepcopy(allowed)
        wrong_module["resolver_module"] = (
            "resolve_receiver_side_answerable_basis_"
            "receiver_attestation_boundary_v0_min"
        )
        invalid_results.append(("v1_module", wrong_module))

        wrong_version = copy.deepcopy(allowed)
        wrong_version["result_version"] = "0.1.0"
        invalid_results.append(("v1_version", wrong_version))

        missing_non_claim = copy.deepcopy(allowed)
        missing_non_claim["non_claims"].pop(
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        )
        invalid_results.append(("missing_non_claim", missing_non_claim))

        flipped_non_claim = copy.deepcopy(allowed)
        flipped_non_claim["non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        invalid_results.append(("flipped_non_claim", flipped_non_claim))

        inconsistent_allowed = copy.deepcopy(allowed)
        self.boundary(inconsistent_allowed)[
            "receiver_attestation_consideration_allowed"
        ] = False
        invalid_results.append(("inconsistent_allowed", inconsistent_allowed))

        inconsistent_not_allowed = copy.deepcopy(not_allowed)
        self.boundary(inconsistent_not_allowed)[
            "receiver_attestation_consideration_not_allowed"
        ] = False
        invalid_results.append(
            ("inconsistent_not_allowed", inconsistent_not_allowed)
        )

        for label, key in (
            (
                "complete_upstream",
                "complete_sufficiency_operation_artifact",
            ),
            ("complete_basis", "sufficiency_basis_records"),
            ("capture_signal", "capture_signal_data"),
        ):
            changed = copy.deepcopy(allowed)
            changed[key] = {"forbidden": True}
            invalid_results.append((label, changed))

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, invalid in invalid_results:
                with self.subTest(refusal=label):
                    with self.assertRaises(
                        ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error
                    ):
                        write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
                            invalid,
                            root / label / resolver.OUTPUT_FILENAME,
                        )

            temporary_capture = (
                root / resolver.BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH
            )
            temporary_upstream = (
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
            )
            protected_targets = (
                root / "spec" / resolver.OUTPUT_FILENAME,
                root / "src" / resolver.OUTPUT_FILENAME,
                root / "tests" / resolver.OUTPUT_FILENAME,
                root / "reference" / resolver.OUTPUT_FILENAME,
                temporary_upstream.parent / resolver.OUTPUT_FILENAME,
                temporary_capture / resolver.OUTPUT_FILENAME,
            )
            with (
                patch.object(resolver, "REPO_ROOT", root),
                patch.object(
                    resolver,
                    "BOUNDED_CAPTURE_MATERIAL_PATH",
                    temporary_capture,
                ),
                patch.object(
                    resolver,
                    "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_PATH",
                    temporary_upstream,
                ),
            ):
                for target in protected_targets:
                    with self.subTest(protected_path=str(target)):
                        with self.assertRaises(
                            ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinV2Error
                        ):
                            write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_result(
                                allowed,
                                target,
                            )
                        self.assertFalse(target.exists())

    def test_determinism_immutability_and_preserved_hashes(self) -> None:
        first = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
        second = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(
            first["declared_non_claims"],
            second["declared_non_claims"],
        )
        first["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        third = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request()
        )
        self.assertIs(
            third["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        first_result = self.invoke(request)
        second_result = self.invoke(request)
        self.assertEqual(first_result, second_result)
        self.assertEqual(request, request_before)

        result_before = copy.deepcopy(first_result)
        first_summary = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary(
                first_result
            )
        )
        second_summary = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_summary(
                first_result
            )
        )
        self.assertEqual(first_summary, second_summary)
        self.assertEqual(first_result, result_before)

        unknown = (
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_v2_request(
                unknown_override="retained_for_validation"
            )
        )
        self.assertEqual(
            unknown["unknown_override"],
            "retained_for_validation",
        )
        self.assert_blocked(
            self.invoke(unknown),
            "REQUEST_UNKNOWN_FIELD",
        )

        for path, expected_hash in self._preserved_hashes.items():
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                expected_hash,
                str(path),
            )


if __name__ == "__main__":
    unittest.main()
