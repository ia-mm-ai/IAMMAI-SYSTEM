"""Tests for one bounded receiver-attestation consideration boundary.

The suite treats the completed candidate-sufficiency operation as immutable
upstream standing.  It covers allowed, not-allowed, and blocked results without
creating receiver attestation, reading capture signal bodies, or writing live
artifacts.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min as resolver
from resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min import (
    ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinError,
    build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request,
    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request,
    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary,
    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min,
    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_from_path,
    write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result,
)


RESOLVER_PATH = (
    REPO_ROOT
    / "src/resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min.py"
)
SPECIFICATION_PATH = REPO_ROOT / resolver.GOVERNING_SPEC_RELATIVE_PATH
UPSTREAM_ARTIFACT_PATH = (
    REPO_ROOT / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
)
UPSTREAM_BOUNDARY_TEST_PATH = (
    REPO_ROOT
    / "tests/test_resolve_receiver_side_answerable_basis_candidate_sufficiency_boundary_v0_min.py"
)
UPSTREAM_OPERATION_TEST_PATH = (
    REPO_ROOT
    / "tests/test_resolve_receiver_side_answerable_basis_candidate_sufficiency_operation_v0_min.py"
)


class ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinTests(
    unittest.TestCase
):
    """Verify one sufficient-candidate receiver-attestation boundary only."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._preserved_paths = tuple(
            path
            for path in (
                RESOLVER_PATH,
                SPECIFICATION_PATH,
                UPSTREAM_ARTIFACT_PATH,
                UPSTREAM_BOUNDARY_TEST_PATH,
                UPSTREAM_OPERATION_TEST_PATH,
            )
            if path.is_file()
        )
        cls._preserved_hashes = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in cls._preserved_paths
        }
        cls._specification_text = SPECIFICATION_PATH.read_text(encoding="utf-8")
        cls._upstream_artifact = json.loads(
            UPSTREAM_ARTIFACT_PATH.read_text(encoding="utf-8")
        )
        if not isinstance(cls._upstream_artifact, dict):
            raise AssertionError("selected live upstream artifact is not a mapping")

    @classmethod
    def tearDownClass(cls) -> None:
        for path, expected in cls._preserved_hashes.items():
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                raise AssertionError(f"preserved lineage changed: {path}")

    def clone(self, value: object) -> object:
        return copy.deepcopy(value)

    def safe_path(
        self, root: Path, case: str, filename: str = "artifact.json"
    ) -> Path:
        safe = "".join(
            character if character.isalnum() or character in "._-" else "_"
            for character in str(case)
        )
        return root / (safe.strip("._-") or "case") / filename

    def write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"temporary file path is a directory: {path}")
        path.write_text(value, encoding="utf-8")
        return path

    def write_json(self, path: Path, value: object) -> Path:
        return self.write_text(
            path,
            json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        )

    def canonical_request(self, **overrides: object) -> dict[str, object]:
        return (
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request(
                **copy.deepcopy(overrides)
            )
        )

    def live_artifact(self) -> dict[str, object]:
        return copy.deepcopy(self._upstream_artifact)

    def operation(self, artifact: dict[str, object]) -> dict[str, object]:
        value = artifact[
            "receiver_side_answerable_basis_candidate_sufficiency_operation"
        ]
        self.assertIsInstance(value, dict)
        return value

    def dimensions(self, artifact: dict[str, object]) -> dict[str, object]:
        value = artifact[
            "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions"
        ]
        self.assertIsInstance(value, dict)
        return value

    def fixture_root(
        self,
        root: Path,
        *,
        specification: str | None = None,
        artifact: object | None = None,
        write_specification: bool = True,
        write_artifact: bool = True,
    ) -> None:
        if write_specification:
            self.write_text(
                root / resolver.GOVERNING_SPEC_RELATIVE_PATH,
                self._specification_text
                if specification is None
                else specification,
            )
        if write_artifact:
            self.write_json(
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH,
                self.live_artifact() if artifact is None else artifact,
            )

    def invoke(
        self,
        request: object | None = None,
        root: Path | None = None,
    ) -> dict[str, object]:
        supplied = copy.deepcopy(request)
        before = copy.deepcopy(supplied)
        if root is None:
            result = (
                resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min(
                    supplied
                )
            )
        else:
            with patch.object(resolver, "REPO_ROOT", root):
                result = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min(
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
        specification: str | None = None,
        artifact: object | None = None,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(
                root,
                specification=specification,
                artifact=artifact,
            )
            return self.invoke(
                self.canonical_request() if request is None else request,
                root,
            )

    def boundary(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary"
        )
        self.assertIsInstance(value, dict)
        return value

    def checks(self, result: dict[str, object]) -> list[dict[str, object]]:
        value = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary_checks"
        )
        self.assertIsInstance(value, list)
        self.assertTrue(all(isinstance(item, dict) for item in value))
        return value

    def non_meaning(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary_non_meaning"
        )
        self.assertIsInstance(value, dict)
        return value

    def statement(self, result: dict[str, object]) -> dict[str, object]:
        value = result.get(
            "receiver_side_answerable_basis_receiver_attestation_boundary_statement"
        )
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        code = block.get("code") or block.get("block_code")
        self.assertTrue(code is None or isinstance(code, str))
        return code

    def assert_all_emitted_codes_public(
        self, result: dict[str, object]
    ) -> None:
        code = self.block_code(result)
        if code is not None:
            self.assertIn(code, resolver.BLOCK_CODES)
        for check in self.checks(result):
            for field in ("failure_code", "block_code"):
                if field in check:
                    self.assertIn(check[field], resolver.BLOCK_CODES)

    def assert_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(non_claims), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        for field in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[field], False, field)
            self.assertIs(self.boundary(result)[field], False, field)

    def assert_downstream_false(self, result: dict[str, object]) -> None:
        boundary = self.boundary(result)
        for field in (
            "receiver_attestation_created",
            "receiver_attestation_supported",
            "receiver_attestation_recorded",
            "receiver_answerable_receipt_present",
            "receiver_answerable_receipt_boundary_created",
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_re_evaluation_boundary_created",
            "identity_created",
            "authority_created",
            "standing_created",
            "truth_created",
            "relation_created",
            "coupling_assigned",
            "coupling_created",
            "runtime_created",
            "api_created",
            "public_interface_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
            "repeated_receiver_attestation_boundary_permission_created",
            "reusable_receiver_attestation_route_created",
            "same_receiver_attestation_boundary_rerun_authorized",
            "automatic_receiver_attestation_boundary_retry_created",
            "receiver_attestation_boundary_debt_created",
            "receiver_attestation_boundary_obligation_created",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        ):
            self.assertIs(boundary[field], False, field)

    def assert_blocked(
        self, result: dict[str, object], expected_code: str | None = None
    ) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        self.assertEqual(
            self.boundary(result).get("receiver_attestation_boundary_result"),
            resolver.BOUNDARY_RESULT_NOT_EVALUATED,
        )
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), True)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assertGreater(result.get("failed_check_count", 0), 0)
        boundary = self.boundary(result)
        for field in (
            "receiver_attestation_boundary_recorded",
            "receiver_attestation_boundary_result_recorded",
            "receiver_attestation_consideration_allowed",
            "receiver_attestation_consideration_not_allowed",
            "receiver_attestation_boundary_exhausted",
        ):
            self.assertIs(boundary[field], False, field)
        self.assert_non_claims_false(result)
        self.assert_downstream_false(result)
        self.assert_all_emitted_codes_public(result)

    def assert_allowed(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_ALLOWED)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["receiver_attestation_boundary_result"],
            resolver.BOUNDARY_RESULT_ALLOWED,
        )
        self.assertIs(boundary["receiver_attestation_boundary_recorded"], True)
        self.assertIs(
            boundary["receiver_attestation_boundary_result_recorded"], True
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_allowed"], True
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_not_allowed"], False
        )
        self.assertIs(boundary["receiver_attestation_boundary_exhausted"], True)
        self.assert_non_claims_false(result)
        self.assert_downstream_false(result)

    def assert_not_allowed(self, result: dict[str, object]) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_NOT_ALLOWED)
        self.assertEqual(result.get("failed_check_count"), 0)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        boundary = self.boundary(result)
        self.assertEqual(
            boundary["receiver_attestation_boundary_result"],
            resolver.BOUNDARY_RESULT_NOT_ALLOWED,
        )
        self.assertIs(boundary["receiver_attestation_boundary_recorded"], True)
        self.assertIs(
            boundary["receiver_attestation_boundary_result_recorded"], True
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_allowed"], False
        )
        self.assertIs(
            boundary["receiver_attestation_consideration_not_allowed"], True
        )
        self.assertIs(boundary["receiver_attestation_boundary_exhausted"], True)
        self.assert_non_claims_false(result)
        self.assert_downstream_false(result)

    def assert_no_true_exact_key(self, value: object, key: str) -> None:
        if isinstance(value, Mapping):
            if key in value:
                self.assertIsNot(value[key], True, key)
            for nested in value.values():
                self.assert_no_true_exact_key(nested, key)
        elif isinstance(value, list):
            for nested in value:
                self.assert_no_true_exact_key(nested, key)

    def test_public_surface_constants_and_canonical_request(self) -> None:
        for value in (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request,
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request,
            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min,
            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_from_path,
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary,
            write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result,
        ):
            self.assertTrue(callable(value))
        self.assertTrue(
            issubclass(
                ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinError,
                Exception,
            )
        )
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min",
        )
        self.assertEqual(
            resolver.BOUNDARY_ID,
            "receiver_side_answerable_basis_receiver_attestation_boundary_001",
        )
        self.assertEqual(
            resolver.BOUNDARY_TYPE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEIVER_ATTESTATION_BOUNDARY",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                resolver.OUTCOME_ALLOWED,
                resolver.OUTCOME_NOT_ALLOWED,
                resolver.OUTCOME_BLOCKED,
            ),
        )
        self.assertEqual(
            resolver.BOUNDARY_RESULT_FAMILY,
            (
                resolver.BOUNDARY_RESULT_ALLOWED,
                resolver.BOUNDARY_RESULT_NOT_ALLOWED,
                resolver.BOUNDARY_RESULT_NOT_EVALUATED,
            ),
        )
        request = self.canonical_request()
        self.assertEqual(request["intent"], resolver.INTENT_RECORD)
        self.assertEqual(request["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(
            request["selected_candidate_sufficiency_operation_id"],
            resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
        )
        self.assertEqual(
            request["selected_candidate_sufficiency_operation_result_required"],
            resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
        )
        self.assertIs(
            request["bounded_material_selected_for_consideration"], True
        )
        self.assertEqual(
            request["bounded_existing_material_path"],
            str(resolver.BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH),
        )
        self.assertEqual(
            set(request["declared_non_claims"]),
            set(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertTrue(
            all(value is False for value in request["declared_non_claims"].values())
        )
        self.assertTrue(
            all(code in resolver.BLOCK_CODES for code in resolver.PROHIBITED_REQUEST_FLAGS.values())
        )
        self.assertEqual(
            json.loads(json.dumps(request, sort_keys=True)),
            request,
        )

    def test_default_live_allowed_branch_and_capture_non_conversion(self) -> None:
        specification_before = SPECIFICATION_PATH.read_bytes()
        artifact_before = UPSTREAM_ARTIFACT_PATH.read_bytes()
        result = self.invoke()
        self.assert_allowed(result)
        boundary = self.boundary(result)
        upstream = result["upstream_basis"]
        summary = result[
            "receiver_side_answerable_basis_receiver_attestation_boundary_summary"
        ]
        self.assertIs(
            boundary["bounded_material_selected_for_consideration"], True
        )
        self.assertIs(
            boundary["selected_candidate_sufficiency_operation_validated"], True
        )
        self.assertIs(summary["eight_dimensions_validated"], True)
        self.assertIs(summary["upstream_false_locks_validated"], True)
        self.assertIs(upstream["complete_operation_artifact_omitted"], True)
        self.assertIs(upstream["complete_sufficiency_basis_omitted"], True)
        self.assertIs(upstream["complete_capture_signal_data_omitted"], True)
        self.assertEqual(
            upstream["governing_paths"]["bounded_existing_material_path"],
            str(resolver.BOUNDED_CAPTURE_MATERIAL_RELATIVE_PATH),
        )
        self.assertIs(
            upstream["bounded_material_validation"][
                "path_existence_not_used_as_authority"
            ],
            True,
        )
        self.assertIs(
            upstream["bounded_material_validation"]["capture_body_not_read"],
            True,
        )
        for field in (
            "independent_custody_established",
            "verified_provenance_established",
            "physical_validity_established",
            "current_presence_established",
            "receiver_identity_established",
        ):
            self.assert_no_true_exact_key(result, field)
        for field in (
            "receiver_attestation_created",
            "receiver_answerable_receipt_present",
            "authority_created",
            "standing_created",
            "truth_created",
        ):
            self.assertIs(boundary[field], False, field)
            self.assertIs(result["non_claims"][field], False, field)
        self.assertEqual(SPECIFICATION_PATH.read_bytes(), specification_before)
        self.assertEqual(UPSTREAM_ARTIFACT_PATH.read_bytes(), artifact_before)

    def test_bounded_material_not_selected_records_not_allowed(self) -> None:
        request = self.canonical_request(
            bounded_material_selected_for_consideration=False
        )
        self.assertEqual(
            request["bounded_material_selection_posture"],
            resolver.BOUNDED_MATERIAL_NOT_SELECTED,
        )
        self.assertIsNone(request["bounded_existing_material_path"])
        result = self.invoke(request)
        self.assert_not_allowed(result)
        boundary = self.boundary(result)
        self.assertIs(
            boundary["selected_candidate_sufficiency_operation_validated"], True
        )
        self.assertIs(boundary["selected_candidate_sufficient"], True)
        non_meaning = self.non_meaning(result)
        for field in (
            "consideration_not_allowed_is_not_candidate_insufficiency",
            "consideration_not_allowed_is_not_receiver_refusal",
            "consideration_not_allowed_is_not_invalid_evidence",
            "consideration_not_allowed_is_not_failed_attestation",
            "consideration_not_allowed_is_not_receiver_absence",
        ):
            self.assertIs(non_meaning[field], True, field)

    def test_blocked_request_shape_matrix(self) -> None:
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
                self.canonical_request(unknown_top_level=True),
                "REQUEST_UNKNOWN_FIELD",
            ),
            (
                "result_posture_preclaim",
                self.canonical_request(
                    receiver_attestation_boundary_recorded=True
                ),
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                "boundary_outcome_preclaim",
                self.canonical_request(outcome=resolver.OUTCOME_ALLOWED),
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                "consideration_result_preclaim",
                self.canonical_request(
                    receiver_attestation_boundary_result=(
                        resolver.BOUNDARY_RESULT_ALLOWED
                    )
                ),
                "RESULT_POSTURE_PRECLAIMED",
            ),
            (
                "malformed_selection",
                self.canonical_request(
                    bounded_material_selected_for_consideration="yes"
                ),
                "REQUEST_VALUE_MISMATCH",
            ),
            (
                "identity_mismatch",
                self.canonical_request(boundary_id="other"),
                "REQUEST_VALUE_MISMATCH",
            ),
            (
                "prohibited_flag",
                self.canonical_request(
                    request_receiver_attestation_creation=True
                ),
                "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
            ),
        ]
        missing = self.canonical_request()
        missing.pop("boundary_scope")
        cases.append(("missing_field", missing, "REQUEST_FIELD_MISSING"))
        missing_non_claim = self.canonical_request()
        missing_non_claim["declared_non_claims"].pop(
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        )
        cases.append(
            (
                "missing_non_claim",
                missing_non_claim,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )
        flipped_non_claim = self.canonical_request()
        flipped_non_claim["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        cases.append(
            (
                "flipped_non_claim",
                flipped_non_claim,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )
        for label, request, expected_code in cases:
            with self.subTest(case=label):
                self.assert_blocked(self.invoke(request), expected_code)

    def test_specification_reference_and_marker_failures(self) -> None:
        marker_cases = (
            (
                "title",
                "# Receiver-Side Answerable Basis Receiver Attestation Boundary V0 Minimum Specification",
            ),
            (
                "boundary_identity",
                (
                    "receiver_side_answerable_basis_receiver_attestation_boundary_id = "
                    "receiver_side_answerable_basis_receiver_attestation_boundary_001"
                ),
            ),
            ("outcome_family", resolver.OUTCOME_ALLOWED),
            ("result_family", resolver.BOUNDARY_RESULT_ALLOWED),
            (
                "candidate_not_attestation",
                "Candidate sufficient is not receiver attestation.",
            ),
            (
                "blocked_not_exhausted",
                (
                    "A blocked boundary retains `NOT_EVALUATED` and does not "
                    "become exhausted."
                ),
            ),
            ("open_not_next", "Open does not mean next."),
        )
        for label, marker in marker_cases:
            with self.subTest(marker=label):
                changed = self._specification_text.replace(marker, "")
                self.assertNotEqual(changed, self._specification_text)
                result = self.resolve_fixture(specification=changed)
                self.assert_blocked(
                    result,
                    "RECEIVER_ATTESTATION_BOUNDARY_SPEC_MARKER_MISSING",
                )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root, write_specification=False)
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "RECEIVER_ATTESTATION_BOUNDARY_SPEC_REFERENCE_MISSING",
            )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec_path = root / resolver.GOVERNING_SPEC_RELATIVE_PATH
            spec_path.mkdir(parents=True)
            self.write_json(
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH,
                self.live_artifact(),
            )
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "RECEIVER_ATTESTATION_BOUNDARY_SPEC_REFERENCE_MISSING",
            )

    def test_upstream_file_metadata_and_section_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root, write_artifact=False)
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_REFERENCE_MISSING",
            )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            artifact_path = (
                root
                / resolver.SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_RELATIVE_PATH
            )
            self.write_text(artifact_path, "{")
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_PARSEABLE",
            )
            self.write_text(
                artifact_path,
                '{"resolver_module": "one", "resolver_module": "two"}\n',
            )
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "UPSTREAM_DIMENSION_DUPLICATED",
            )
            self.write_json(artifact_path, [])
            self.assert_blocked(
                self.invoke(self.canonical_request(), root),
                "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_MAPPING",
            )

        section_cases = (
            (
                "operation",
                "receiver_side_answerable_basis_candidate_sufficiency_operation",
            ),
            (
                "dimensions",
                "receiver_side_answerable_basis_candidate_sufficiency_operation_dimensions",
            ),
        )
        for label, field in section_cases:
            with self.subTest(section=label):
                artifact = self.live_artifact()
                artifact.pop(field)
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    "SELECTED_SUFFICIENCY_OPERATION_ARTIFACT_NOT_MAPPING",
                )

        top_level_cases = (
            (
                "resolver_module",
                "other",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "result_version",
                "0.0.0",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "failed_checks",
                1,
                "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
            ),
            (
                "failed_checks_wrong_type",
                False,
                "UPSTREAM_OPERATION_FAILED_CHECKS_PRESENT",
            ),
            (
                "outcome",
                "other",
                "UPSTREAM_OPERATION_OUTCOME_MISMATCH",
            ),
        )
        for label, value, expected_code in top_level_cases:
            with self.subTest(metadata=label):
                artifact = self.live_artifact()
                field = {
                    "failed_checks": "failed_check_count",
                    "failed_checks_wrong_type": "failed_check_count",
                }.get(label, label)
                artifact[field] = value
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

    def test_upstream_identity_and_sufficiency_posture_matrix(self) -> None:
        identity_cases = (
            (
                "operation_id",
                "other",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_type",
                "other",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_version",
                "0.0.0",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "operation_scope",
                "other",
                "SELECTED_SUFFICIENCY_OPERATION_IDENTITY_MISMATCH",
            ),
            (
                "receiver_side_answerable_basis_candidate_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_reception_operation_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_evaluation_boundary_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_evaluation_operation_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
            (
                "selected_candidate_sufficiency_boundary_id",
                "other",
                "SELECTED_CANDIDATE_IDENTITY_MISMATCH",
            ),
        )
        for field, value, expected_code in identity_cases:
            with self.subTest(identity=field):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = value
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

        posture_cases = (
            (
                "operation_result",
                "other",
                "UPSTREAM_OPERATION_RESULT_MISMATCH",
            ),
            (
                "candidate_sufficiency_operation_recorded",
                False,
                "UPSTREAM_OPERATION_NOT_RECORDED",
            ),
            (
                "candidate_sufficiency_operation_result_recorded",
                False,
                "UPSTREAM_OPERATION_RESULT_NOT_RECORDED",
            ),
            (
                "candidate_sufficiency_operation_exhausted",
                False,
                "UPSTREAM_OPERATION_NOT_EXHAUSTED",
            ),
            (
                "candidate_sufficiency_decided",
                False,
                "UPSTREAM_CANDIDATE_NOT_SUFFICIENT",
            ),
            (
                "candidate_sufficiency_established",
                False,
                "UPSTREAM_CANDIDATE_NOT_SUFFICIENT",
            ),
            (
                "receiver_side_answerable_basis_candidate_sufficient",
                False,
                "UPSTREAM_CANDIDATE_NOT_SUFFICIENT",
            ),
            (
                "receiver_side_answerable_basis_candidate_insufficient",
                True,
                "UPSTREAM_CANDIDATE_RESULT_CONFLICT",
            ),
            (
                "receiver_side_answerable_basis_candidate_indeterminate",
                True,
                "UPSTREAM_CANDIDATE_RESULT_CONFLICT",
            ),
            (
                "sufficiency_basis_supplied",
                False,
                "UPSTREAM_SUFFICIENCY_BASIS_INCOMPLETE",
            ),
            (
                "sufficiency_basis_complete",
                False,
                "UPSTREAM_SUFFICIENCY_BASIS_INCOMPLETE",
            ),
            (
                "atomic_sufficiency_basis_gate_passed",
                False,
                "UPSTREAM_ATOMIC_SUFFICIENCY_GATE_INCOMPLETE",
            ),
        )
        for field, value, expected_code in posture_cases:
            with self.subTest(posture=field):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = value
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

    def test_exact_eight_dimension_validation_matrix(self) -> None:
        self.assertEqual(
            resolver.REQUIRED_DIMENSION_IDS,
            (
                "receiver_answerability_fit",
                "selected_purpose_adequacy",
                "bounded_material_completeness",
                "unresolved_contradiction_posture",
                "unsupported_assumption_dependency",
                "scope_constrained_usability",
                "refusal_withholding_compatibility",
                "provenance_capture_limitation_posture",
            ),
        )
        first = resolver.REQUIRED_DIMENSION_IDS[0]
        cases: list[tuple[str, dict[str, object], str]] = []

        artifact = self.live_artifact()
        self.dimensions(artifact).pop(first)
        cases.append(("missing", artifact, "UPSTREAM_DIMENSION_SET_MISMATCH"))

        artifact = self.live_artifact()
        self.dimensions(artifact)["additional"] = copy.deepcopy(
            self.dimensions(artifact)[first]
        )
        cases.append(("additional", artifact, "UPSTREAM_DIMENSION_SET_MISMATCH"))

        artifact = self.live_artifact()
        self.dimensions(artifact)[first] = []
        cases.append(("malformed", artifact, "UPSTREAM_DIMENSION_MALFORMED"))

        for label, field, value, expected_code in (
            (
                "id",
                "dimension_id",
                "other",
                "UPSTREAM_DIMENSION_MALFORMED",
            ),
            (
                "result",
                "dimension_result",
                "INDETERMINATE",
                "UPSTREAM_DIMENSION_NOT_SATISFIED",
            ),
            (
                "evaluated",
                "dimension_evaluated",
                False,
                "UPSTREAM_DIMENSION_NOT_EVALUATED",
            ),
            (
                "established",
                "dimension_established",
                False,
                "UPSTREAM_DIMENSION_NOT_ESTABLISHED",
            ),
        ):
            artifact = self.live_artifact()
            self.dimensions(artifact)[first][field] = value
            cases.append((label, artifact, expected_code))

        for label, artifact, expected_code in cases:
            with self.subTest(dimension_case=label):
                self.assert_blocked(
                    self.resolve_fixture(artifact=artifact),
                    expected_code,
                )

    def test_every_upstream_false_lock_blocks_when_true(self) -> None:
        family_representatives = {
            "receiver_attestation": "receiver_attestation_created",
            "receiver_answerable_receipt": "receiver_answerable_receipt_present",
            "presence": "presence_supported",
            "identity_authority": "identity_created",
            "relation_coupling": "relation_created",
            "runtime_api_public": "runtime_created",
            "standing_truth": "standing_created",
            "output_action_sync_follow_on": "follow_on_work_authorized",
            "repeated_reusable": (
                "repeated_candidate_sufficiency_operation_permission_created"
            ),
            "rerun_retry": "same_candidate_sufficiency_operation_rerun_authorized",
            "debt_obligation": "candidate_sufficiency_operation_debt_created",
        }
        self.assertTrue(
            set(family_representatives.values()).issubset(
                resolver.REQUIRED_UPSTREAM_FALSE_POSTURES
            )
        )
        for field in resolver.REQUIRED_UPSTREAM_FALSE_POSTURES:
            with self.subTest(false_lock=field):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = True
                result = self.resolve_fixture(artifact=artifact)
                self.assert_blocked(result)
                if field in {
                    "receiver_side_answerable_basis_candidate_insufficient",
                    "receiver_side_answerable_basis_candidate_indeterminate",
                }:
                    self.assertEqual(
                        self.block_code(result),
                        "UPSTREAM_CANDIDATE_RESULT_CONFLICT",
                    )
                else:
                    self.assertEqual(
                        self.block_code(result),
                        "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                    )
        for field in (
            "prior_unsupported_candidate_a_claim_validated",
            "prior_unsupported_candidate_b_claim_validated",
            "prior_unsupported_derivation_event_claim_validated",
            "affected_file_repaired",
            "repository_scan_performed",
            "file_discovery_performed",
            "validation_enforced",
        ):
            with self.subTest(contaminated_or_repair_lock=field):
                artifact = self.live_artifact()
                self.operation(artifact)[field] = True
                result = self.resolve_fixture(artifact=artifact)
                self.assert_blocked(
                    result,
                    "UPSTREAM_FALSE_LOCK_NOT_FALSE",
                )

    def test_summary_non_meaning_and_route_postures(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    bounded_material_selected_for_consideration=False
                )
            ),
            self.invoke([]),
        )
        expected_outcomes = (
            resolver.OUTCOME_ALLOWED,
            resolver.OUTCOME_NOT_ALLOWED,
            resolver.OUTCOME_BLOCKED,
        )
        for result, expected_outcome in zip(
            results, expected_outcomes, strict=True
        ):
            with self.subTest(outcome=expected_outcome):
                before = copy.deepcopy(result)
                first = (
                    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary(
                        result
                    )
                )
                second = (
                    build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary(
                        result
                    )
                )
                self.assertEqual(first, second)
                self.assertEqual(result, before)
                self.assertEqual(first["outcome"], expected_outcome)
                self.assertEqual(
                    first["boundary_result"],
                    self.boundary(result)["receiver_attestation_boundary_result"],
                )
                self.assertEqual(
                    first["failed_check_count"], result["failed_check_count"]
                )
                self.assertEqual(
                    first["passed_check_count"], result["passed_check_count"]
                )
                self.assertEqual(first["boundary_id"], resolver.BOUNDARY_ID)
                self.assertEqual(first["boundary_type"], resolver.BOUNDARY_TYPE)
                self.assertEqual(first["selected_candidate_id"], resolver.CANDIDATE_ID)
                self.assertEqual(
                    first["selected_sufficiency_operation_id"],
                    resolver.SELECTED_SUFFICIENCY_OPERATION_ID,
                )
                self.assertEqual(
                    first["selected_sufficiency_operation_result_required"],
                    resolver.SELECTED_SUFFICIENCY_OPERATION_RESULT_REQUIRED,
                )
                self.assertIn(
                    "bounded_material_selected_for_consideration", first
                )
                self.assertIn("receiver_attestation_boundary_recorded", first)
                self.assertIn("receiver_attestation_boundary_exhausted", first)
                self.assertIn("specification_markers_validated", first)
                self.assertIn("selected_operation_validated", first)
                self.assertIn("eight_dimensions_validated", first)
                self.assertIn("upstream_false_locks_validated", first)
                self.assertIs(
                    first["result_level_non_claims_canonical_false"], True
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
                self.assertIsInstance(first["governing_paths"], dict)

        allowed = results[0]
        non_meaning = self.non_meaning(allowed)
        for field in (
            "candidate_sufficient_is_not_receiver_attestation",
            "captured_material_is_not_receiver_attestation",
            "consideration_allowed_is_not_receiver_attestation",
            "boundary_result_is_not_operation_execution",
            "boundary_exhaustion_is_not_downstream_authorization",
        ):
            self.assertIs(non_meaning[field], True, field)
        statement = self.statement(allowed)
        self.assertIs(statement["open_does_not_mean_next"], True)
        self.assertIs(statement["open_means_not_authorized"], True)
        self.assertEqual(
            allowed["permitted_future_route"],
            resolver.ADMISSIBLE_FUTURE_ROUTE,
        )
        self.assertIn("if separately selected", allowed["what_remains_open"][0])
        boundary = self.boundary(allowed)
        self.assertIs(boundary["standing_created"], False)
        self.assertIs(boundary["receiver_attestation_created"], False)
        self.assertIs(
            boundary["receiver_answerable_receipt_boundary_created"], False
        )
        self.assertIs(
            boundary["presence_re_evaluation_boundary_created"], False
        )
        self.assertIs(
            boundary[
                "repeated_receiver_attestation_boundary_permission_created"
            ],
            False,
        )
        self.assertIs(
            boundary["automatic_receiver_attestation_boundary_retry_created"],
            False,
        )

    def test_from_path_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture_root(root)
            request = self.canonical_request()
            request_path = self.safe_path(root, "request", "request.json")
            self.write_json(request_path, request)
            with patch.object(resolver, "REPO_ROOT", root):
                direct = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min(
                        request
                    )
                )
                from_path = (
                    resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_from_path(
                        request_path
                    )
                )
            self.assertEqual(from_path, direct)
            self.assert_allowed(from_path)

            malformed = self.safe_path(root, "malformed", "request.json")
            duplicate = self.safe_path(root, "duplicate", "request.json")
            non_mapping = self.safe_path(root, "non_mapping", "request.json")
            self.write_text(malformed, "{")
            self.write_text(duplicate, '{"intent": "one", "intent": "two"}\n')
            self.write_json(non_mapping, [])
            with patch.object(resolver, "REPO_ROOT", root):
                for label, path in (
                    ("malformed", malformed),
                    ("duplicate", duplicate),
                    ("non_mapping", non_mapping),
                    ("missing", root / "missing_request.json"),
                ):
                    with self.subTest(path_case=label):
                        result = (
                            resolve_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_from_path(
                                path
                            )
                        )
                        self.assert_blocked(result, "REQUEST_NOT_MAPPING")

    def test_writer_valid_branches_and_deterministic_suffix(self) -> None:
        results = (
            self.invoke(),
            self.invoke(
                self.canonical_request(
                    bounded_material_selected_for_consideration=False
                )
            ),
            self.invoke([]),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for index, result in enumerate(results):
                with self.subTest(outcome=result["outcome"]):
                    target = (
                        root / f"branch_{index}" / resolver.OUTPUT_FILENAME
                    )
                    written = (
                        write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result(
                            result, target
                        )
                    )
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

            allowed = results[0]
            target = root / "suffix" / resolver.OUTPUT_FILENAME
            first = (
                write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result(
                    allowed, target
                )
            )
            first_bytes = first.read_bytes()
            second = (
                write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result(
                    allowed, target
                )
            )
            self.assertEqual(second.name, first.stem + "_001" + first.suffix)
            self.assertEqual(first.read_bytes(), first_bytes)
            self.assertNotEqual(first, second)

    def test_writer_refusals_and_protected_paths(self) -> None:
        allowed = self.invoke()
        not_allowed = self.invoke(
            self.canonical_request(
                bounded_material_selected_for_consideration=False
            )
        )
        blocked = self.invoke([])
        invalid_results: list[tuple[str, object]] = [("non_mapping", [])]

        wrong_resolver = copy.deepcopy(allowed)
        wrong_resolver["resolver_module"] = "other"
        invalid_results.append(("wrong_resolver", wrong_resolver))

        wrong_version = copy.deepcopy(allowed)
        wrong_version["result_version"] = "0.0.0"
        invalid_results.append(("wrong_version", wrong_version))

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

        inconsistent_blocked = copy.deepcopy(blocked)
        self.boundary(inconsistent_blocked)[
            "receiver_attestation_boundary_exhausted"
        ] = True
        invalid_results.append(("inconsistent_blocked", inconsistent_blocked))

        for label, key in (
            (
                "complete_upstream",
                "complete_sufficiency_operation_artifact",
            ),
            ("complete_basis", "sufficiency_basis_records"),
            ("complete_capture", "capture_signal_data"),
        ):
            changed = copy.deepcopy(allowed)
            changed[key] = {"forbidden": True}
            invalid_results.append((label, changed))

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for label, value in invalid_results:
                with self.subTest(refusal=label):
                    with self.assertRaises(
                        ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinError
                    ):
                        write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result(
                            value,
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
                            ReceiverSideAnswerableBasisReceiverAttestationBoundaryV0MinError
                        ):
                            write_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_result(
                                allowed,
                                target,
                            )
                        self.assertFalse(target.exists())

    def test_builder_resolver_and_summary_determinism_and_immutability(
        self,
    ) -> None:
        first = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request()
        )
        second = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request()
        )
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertIsNot(first["declared_non_claims"], second["declared_non_claims"])
        first["declared_non_claims"][
            resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        ] = True
        third = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request()
        )
        self.assertIs(
            third["declared_non_claims"][
                resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            ],
            False,
        )

        request = self.canonical_request()
        request_before = copy.deepcopy(request)
        one = self.invoke(request)
        two = self.invoke(request)
        self.assertEqual(one, two)
        self.assertEqual(request, request_before)

        result_before = copy.deepcopy(one)
        summary_one = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary(
                one
            )
        )
        summary_two = (
            build_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_summary(
                one
            )
        )
        self.assertEqual(summary_one, summary_two)
        self.assertEqual(one, result_before)

        bounded_override = (
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request(
                bounded_material_selected_for_consideration=False
            )
        )
        self.assertIs(
            bounded_override["bounded_material_selected_for_consideration"],
            False,
        )
        self.assertEqual(
            bounded_override["bounded_material_selection_posture"],
            resolver.BOUNDED_MATERIAL_NOT_SELECTED,
        )
        unknown_override = (
            build_declared_receiver_side_answerable_basis_receiver_attestation_boundary_v0_min_request(
                unknown_override="preserved_for_validation"
            )
        )
        self.assertEqual(
            unknown_override["unknown_override"], "preserved_for_validation"
        )
        self.assert_blocked(
            self.invoke(unknown_override),
            "REQUEST_UNKNOWN_FIELD",
        )


if __name__ == "__main__":
    unittest.main()
