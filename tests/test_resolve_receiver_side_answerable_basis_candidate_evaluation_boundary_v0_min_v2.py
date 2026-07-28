"""Bounded tests for the standalone receiver-side candidate-evaluation boundary v2.

The v1 resolver remains preserved lineage.  These tests exercise the selected
v2 line, especially its explicit separation of prior reception-operation locks
from current evaluation-boundary locks.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min as predecessor
import resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2 as resolver


class ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Tests(unittest.TestCase):
    """Verify one bounded v2 consideration result and its refusal posture."""

    ROUTE_LOCKS = (
        "prior_second_candidate_received",
        "prior_repeated_reception_permission_created",
        "prior_reusable_route_created",
        "second_candidate_received",
        "repeated_evaluation_permission_created",
        "reusable_route_created",
    )
    DIMENSION_IDS = (
        "candidate_structural_correspondence",
        "declared_provenance_posture",
        "receiver_authorship_posture",
        "separate_custody_posture",
        "refusability_posture",
        "could_have_been_withheld_posture",
        "prior_knock_correspondence_posture",
        "capture_record_posture",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in str(name))
        safe = safe.strip("._-") or "case"
        prefix = f"{index:03d}_" if index is not None else ""
        return f"{prefix}{safe}.json"

    def _write_text(self, path: Path, value: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.assertFalse(path.is_dir(), f"temporary fixture path is a directory: {path}")
        path.write_text(value, encoding="utf-8")
        return path

    def _write_json(self, path: Path, value: object) -> Path:
        return self._write_text(path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n")

    def _synthetic_specification(self) -> str:
        markers = []
        for _, marker_class in resolver.BOUNDARY_SPEC_MARKER_CLASSES:
            markers.extend(marker_class)
        return "\n".join(dict.fromkeys(markers)) + "\n"

    def _candidate_payload(self) -> dict[str, object]:
        return {
            "opaque_payload_sentinel": "CANDIDATE_CONTENT_MUST_NOT_BE_COPIED",
            "nested": {"list": [1, True, {"depth": ["opaque", 3]}]},
            "provenance_body": "LONG_DECLARED_PROVENANCE_BODY_MUST_NOT_BE_COPIED",
        }

    def _synthetic_artifact(self, candidate_material: object | None = None) -> dict[str, object]:
        candidate_material = self._candidate_payload() if candidate_material is None else candidate_material
        operation = {
            "receiver_side_answerable_basis_reception_operation_id": resolver.SELECTED_RECEPTION_OPERATION_ID,
            "receiver_side_answerable_basis_reception_operation_type": resolver.PRIOR_RECEPTION_OPERATION_TYPE,
            "receiver_side_answerable_basis_reception_operation_result": resolver.PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED,
            "receiver_side_answerable_basis_reception_operation_recorded": True,
            "receiver_side_answerable_basis_reception_operation_result_recorded": True,
            "receiver_side_answerable_basis_candidate_id": resolver.CANDIDATE_ID,
            "receiver_side_answerable_basis_candidate_type": resolver.CANDIDATE_TYPE,
            "receiver_side_answerable_basis_candidate_scope": resolver.CANDIDATE_SCOPE,
            "candidate_material_supplied": True,
            "candidate_material_received": True,
            "candidate_material_recorded": True,
            "candidate_material_preserved": True,
            "candidate_source_provenance_reference_supplied": True,
            "receiver_side_answerable_basis_candidate_received": True,
            "receiver_side_answerable_basis_candidate_recorded": True,
            "receiver_side_answerable_basis_candidate_evaluated": False,
            "prior_receiver_side_answerable_basis_reception_boundary_referenced": True,
            "second_candidate_received": False,
            "repeated_reception_permission_created": False,
            "reusable_route_created": False,
            "receiver_attestation_created": False,
            "receiver_attestation_supported": False,
            "receiver_answerable_receipt_present": False,
            "receiver_answerable_basis_custody_distinct": False,
            "receiver_answerable_basis_refusable": False,
            "receiver_answerable_basis_could_have_been_withheld": False,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        }
        return {
            "outcome": resolver.PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count": 0,
            "non_claims": {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
            "what_remains_open": [
                "actual receiver-side answerable-basis candidate material",
                "actual candidate reception",
            ],
            "receiver_side_answerable_basis_reception_operation": operation,
            "receiver_side_answerable_basis_reception_operation_material": {
                "supplied_candidate_material_record": {
                    "candidate_material": copy.deepcopy(candidate_material),
                    "candidate_material_supplied": True,
                    "candidate_material_received": True,
                    "candidate_material_recorded": True,
                    "candidate_material_preserved": True,
                }
            },
        }

    def _base_request(self, specification_path: Path, artifact_path: Path) -> dict[str, object]:
        return resolver.build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request(
            governing_boundary_specification_path=specification_path,
            selected_successful_candidate_reception_artifact_path=artifact_path,
        )

    def _declared_request(self, specification_path: Path, artifact_path: Path) -> dict[str, object]:
        return resolver.build_declared_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request(
            governing_boundary_specification_path=specification_path,
            selected_successful_candidate_reception_artifact_path=artifact_path,
        )

    def _fixture_paths(self, directory: Path) -> tuple[Path, Path]:
        specification_path = self._write_text(directory / "governing.md", self._synthetic_specification())
        artifact_path = self._write_json(directory / "selected-artifact.json", self._synthetic_artifact())
        return specification_path, artifact_path

    def block_code(self, result: dict[str, object]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        return block.get("code") or block.get("block_code")

    def failed_check_count(self, result: dict[str, object]) -> int | None:
        count = result.get("failed_check_count")
        if isinstance(count, int):
            return count
        summary = result.get("receiver_side_answerable_basis_candidate_evaluation_boundary_summary", {})
        return summary.get("failed_check_count") if isinstance(summary, dict) else None

    def passed_check_count(self, result: dict[str, object]) -> int | None:
        count = result.get("passed_check_count")
        if isinstance(count, int):
            return count
        summary = result.get("receiver_side_answerable_basis_candidate_evaluation_boundary_summary", {})
        return summary.get("passed_check_count") if isinstance(summary, dict) else None

    def assert_not_blocked(self, result: dict[str, object]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block.get("blocked"), False)
        self.assertIsNone(block.get("code"))
        self.assertIsNone(block.get("block_code"))

    def assert_blocked_public(self, result: dict[str, object], expected_code: str | None = None) -> None:
        self.assertEqual(result.get("outcome"), resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIn(code, resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(code, expected_code)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_all_emitted_codes_public(self, result: dict[str, object]) -> None:
        checks = result.get("receiver_side_answerable_basis_candidate_evaluation_boundary_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            if isinstance(check, dict):
                for key in ("block_code", "failure_code"):
                    if key in check:
                        self.assertIn(check[key], resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_boundary_has_no_wrapper_fields(self, result: dict[str, object]) -> None:
        boundary = result["receiver_side_answerable_basis_candidate_evaluation_boundary"]
        self.assertIsInstance(boundary, dict)
        for key in (
            "outcome", "block", "receiver_side_answerable_basis_candidate_evaluation_boundary_checks",
            "non_claims", "receiver_side_answerable_basis_candidate_evaluation_boundary_summary",
            "receiver_side_answerable_basis_candidate_evaluation_boundary_metadata",
            "selected_receiver_side_answerable_basis_candidate_basis",
            "receiver_side_answerable_basis_candidate_evaluation_dimensions",
        ):
            self.assertNotIn(key, boundary)

    def assert_candidate_material_absent(self, result: dict[str, object], payload: object | None = None) -> None:
        serialized = json.dumps(result, sort_keys=True)
        self.assertNotIn('"candidate_material":', serialized)
        self.assertNotIn("CANDIDATE_CONTENT_MUST_NOT_BE_COPIED", serialized)
        self.assertNotIn("LONG_DECLARED_PROVENANCE_BODY_MUST_NOT_BE_COPIED", serialized)
        if payload is not None:
            self.assertFalse(self._contains_value(result, payload))

    def _contains_value(self, value: object, expected: object) -> bool:
        if value == expected:
            return True
        if isinstance(value, dict):
            return any(self._contains_value(item, expected) for item in value.values())
        if isinstance(value, (list, tuple)):
            return any(self._contains_value(item, expected) for item in value)
        return False

    def assert_dimensions_not_evaluated(self, result: dict[str, object]) -> None:
        dimensions = result["receiver_side_answerable_basis_candidate_evaluation_dimensions"]
        self.assertEqual(tuple(dimensions), self.DIMENSION_IDS)
        for identifier, value in dimensions.items():
            self.assertEqual(set(value), {"dimension_id", "dimension_label", "evaluation_status", "established", "non_conversion_statement"})
            self.assertEqual(value["dimension_id"], identifier)
            self.assertEqual(value["evaluation_status"], resolver.BOUNDARY_RESULT_NOT_EVALUATED)
            self.assertIs(value["established"], False)

    def assert_route_locks(self, result: dict[str, object]) -> None:
        basis = result["selected_receiver_side_answerable_basis_candidate_basis"]
        boundary = result["receiver_side_answerable_basis_candidate_evaluation_boundary"]
        summary = result["receiver_side_answerable_basis_candidate_evaluation_boundary_summary"]
        for key in self.ROUTE_LOCKS[:3]:
            self.assertIn(key, basis)
            self.assertIs(basis[key], False)
        for key in self.ROUTE_LOCKS[3:]:
            self.assertIn(key, boundary)
            self.assertIs(boundary[key], False)
        self.assertNotIn("repeated_reception_permission_created", boundary)
        self.assertNotIn("repeated_reception_permission_created", summary)
        for key in self.ROUTE_LOCKS:
            self.assertIn(key, summary)
            self.assertIs(summary[key], False)

    def assert_refusal_posture(self, result: dict[str, object]) -> None:
        boundary = result["receiver_side_answerable_basis_candidate_evaluation_boundary"]
        for key in (
            "receiver_side_answerable_basis_candidate_evaluated",
            "receiver_side_answerable_basis_candidate_sufficient",
            "receiver_side_answerable_basis_candidate_insufficient",
            "receiver_side_answerable_basis_candidate_indeterminate",
            "receiver_attestation_created", "receiver_answerable_receipt_present",
            "receiver_answerable_basis_custody_distinct", "receiver_answerable_basis_refusable",
            "receiver_answerable_basis_could_have_been_withheld", "presence_supported",
            "presence_authorized", "presence_established", "presence_recorded",
        ):
            self.assertIs(boundary[key], False, key)
        self.assert_canonical_non_claims(result)

    def _allowed_result(self, directory: Path, payload: object | None = None) -> tuple[dict[str, object], dict[str, object], Path, Path]:
        specification_path = self._write_text(directory / "governing.md", self._synthetic_specification())
        artifact = self._synthetic_artifact(payload)
        artifact_path = self._write_json(directory / "selected.json", artifact)
        request = self._base_request(specification_path, artifact_path)
        return resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request), artifact, specification_path, artifact_path

    def test_public_api_constants_and_predecessor_posture(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2",
            "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path",
            "write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result",
            "build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_summary",
            "build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request",
            "build_declared_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.2.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2")
        self.assertEqual(resolver.BOUNDARY_ID, "receiver_side_answerable_basis_candidate_evaluation_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_EVALUATION_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(resolver.BOUNDARY_SCOPE, "CONSIDER_EVALUATION_OF_ONE_RECORDED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY")
        self.assertEqual(resolver.PRIOR_RECEPTION_OPERATION_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION")
        self.assertEqual(resolver.PRIOR_RECEPTION_OPERATION_OUTCOME_REQUIRED, "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_RECORDED")
        self.assertEqual(resolver.PRIOR_RECEPTION_OPERATION_RESULT_REQUIRED, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEIVED")
        self.assertEqual(resolver.PRIOR_FAILED_CHECK_COUNT_REQUIRED, 0)
        self.assertEqual(resolver.CANDIDATE_ID, "receiver_side_answerable_basis_candidate_001")
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith("receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2"))
        self.assertEqual(resolver.OUTPUT_FILENAME, "receiver_side_answerable_basis_candidate_evaluation_boundary_001__receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result.json")
        self.assertTrue((SRC_ROOT / "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min.py").is_file())
        self.assertTrue((SRC_ROOT / "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2.py").is_file())
        self.assertNotEqual(predecessor.__file__, resolver.__file__)
        self.assertEqual(resolver.BOUNDARY_VERSION, predecessor.BOUNDARY_VERSION)
        self.assertEqual(set(resolver.OUTCOME_FAMILY), set(predecessor.OUTCOME_FAMILY))

    def test_public_block_codes_and_prohibited_flags(self) -> None:
        required_codes = {
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "BOUNDARY_SPEC_REFERENCE_MISSING",
            "BOUNDARY_SPEC_MARKER_MISSING", "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_PARSEABLE",
            "SELECTED_CANDIDATE_RECEPTION_RESULT_NOT_MAPPING", "NON_CLAIM_MISSING_OR_FLIPPED",
            "RESULT_POSTURE_PRECLAIMED", "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
            "PROHIBITED_CANDIDATE_RESULT_REQUESTED", "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
            "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED", "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        }
        self.assertTrue(required_codes.issubset(resolver.BLOCK_CODES))
        self.assertTrue(set(resolver.PROHIBITED_REQUEST_FLAGS.values()).issubset(resolver.BLOCK_CODES))
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_candidate_evaluation"], "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED")
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_candidate_sufficiency"], "PROHIBITED_CANDIDATE_RESULT_REQUESTED")
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_attestation_creation"], "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED")
        self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_answerable_receipt_creation"], "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED")
        self.assertNotEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_attestation_creation"],
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_answerable_receipt_creation"],
        )

    def test_synthetic_allowed_result_structure_route_locks_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result, _, _, _ = self._allowed_result(Path(temporary))
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_boundary_has_no_wrapper_fields(result)
        self.assert_canonical_non_claims(result)
        self.assert_refusal_posture(result)
        self.assert_dimensions_not_evaluated(result)
        self.assert_route_locks(result)
        self.assertEqual(result["missing_or_inconsistent_recorded_candidate_basis"], [])
        boundary = result["receiver_side_answerable_basis_candidate_evaluation_boundary"]
        self.assertEqual(boundary["receiver_side_answerable_basis_candidate_evaluation_boundary_result"], resolver.BOUNDARY_RESULT_ALLOWED)
        self.assertIs(boundary["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"], True)
        self.assertIs(boundary["selected_candidate_reception_result_referenced"], True)
        self.assertIs(boundary["selected_candidate_material_referenced"], True)
        for key in (
            "receiver_side_answerable_basis_candidate_evaluation_boundary_metadata",
            "declared_receiver_side_answerable_basis_candidate_evaluation_boundary_basis", "upstream_basis",
            "receiver_side_answerable_basis_candidate_evaluation_boundary", "selected_receiver_side_answerable_basis_candidate_basis",
            "receiver_side_answerable_basis_candidate_evaluation_dimensions", "receiver_side_answerable_basis_candidate_evaluation_boundary_checks",
            "receiver_side_answerable_basis_candidate_evaluation_boundary_statement", "receiver_side_answerable_basis_candidate_evaluation_boundary_non_meaning",
            "boundary_result_detail", "permitted_future_route", "blocked_routes", "what_remains_open",
            "missing_or_inconsistent_recorded_candidate_basis", "non_claims", "outcome", "block",
            "receiver_side_answerable_basis_candidate_evaluation_boundary_summary", "resolver_module", "result_version",
        ):
            self.assertIn(key, result)

    def test_default_live_result_when_selected_inputs_exist(self) -> None:
        if not resolver.GOVERNING_BOUNDARY_SPEC_PATH.is_file() or not resolver.SELECTED_CANDIDATE_RECEPTION_RESULT_PATH.is_file():
            self.skipTest("default governing specification or selected artifact is unavailable")
        result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2()
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assert_dimensions_not_evaluated(result)
        self.assert_route_locks(result)
        self.assert_refusal_posture(result)
        self.assert_candidate_material_absent(result)

    def test_candidate_material_is_structural_only_and_stale_entries_are_bounded(self) -> None:
        payload = self._candidate_payload()
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            result, source_artifact, specification_path, artifact_path = self._allowed_result(directory, payload)
            self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
            self.assert_candidate_material_absent(result, payload)
            basis = result["selected_receiver_side_answerable_basis_candidate_basis"]
            self.assertIs(basis["candidate_material_present"], True)
            self.assertIs(basis["complete_candidate_material_omitted_from_boundary_result"], True)
            self.assertIs(basis["stale_open_list_exception_recognized"], True)
            self.assertNotIn("actual receiver-side answerable-basis candidate material", result["what_remains_open"])
            self.assertNotIn("actual candidate reception", result["what_remains_open"])
            self.assertEqual(source_artifact, self._synthetic_artifact(payload))

            altered = copy.deepcopy(source_artifact)
            altered["receiver_side_answerable_basis_reception_operation"]["candidate_material_preserved"] = False
            altered_path = self._write_json(directory / "inconsistent.json", altered)
            inconsistent = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
                self._base_request(specification_path, altered_path)
            )
            for index, material in enumerate(("opaque", 7, True, ["opaque", {"nested": True}], {"nested": [1, 2, 3]})):
                with self.subTest(material_type=type(material).__name__):
                    material_result, _, _, _ = self._allowed_result(directory / f"material_{index}", material)
                    self.assertEqual(material_result["outcome"], resolver.OUTCOME_ALLOWED)
                    self.assert_dimensions_not_evaluated(material_result)
        self.assertEqual(inconsistent["outcome"], resolver.OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS)
        self.assertIn("candidate_material_preserved", inconsistent["missing_or_inconsistent_recorded_candidate_basis"])
        self.assertIs(inconsistent["receiver_side_answerable_basis_candidate_evaluation_boundary"]["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"], False)

    def test_missing_malformed_and_inconsistent_upstream_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            specification_path = self._write_text(directory / "governing.md", self._synthetic_specification())
            missing = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
                self._base_request(specification_path, directory / "missing.json")
            )
            self.assertEqual(missing["outcome"], resolver.OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS)
            self.assertEqual(self.failed_check_count(missing), 0)
            self.assertTrue(missing["missing_or_inconsistent_recorded_candidate_basis"])
            self.assert_canonical_non_claims(missing)

            for index, malformed in enumerate(("{", [], "not a mapping", None)):
                path = directory / self.safe_json_filename("malformed", index)
                if isinstance(malformed, str) and malformed == "{":
                    self._write_text(path, malformed)
                else:
                    self._write_json(path, malformed)
                result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(self._base_request(specification_path, path))
                self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
                self.assert_blocked_public(result)

            cases = {
                "outcome": lambda artifact: artifact.__setitem__("outcome", "WRONG"),
                "operation_id": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_reception_operation_id", "wrong"),
                "operation_type": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_reception_operation_type", "wrong"),
                "operation_result": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_reception_operation_result", "wrong"),
                "operation_recorded": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_reception_operation_recorded", False),
                "result_recorded": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_reception_operation_result_recorded", False),
                "candidate_id": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_id", "wrong"),
                "candidate_type": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_type", "wrong"),
                "candidate_scope": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_scope", "wrong"),
                "material_supplied": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("candidate_material_supplied", False),
                "material_received": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("candidate_material_received", False),
                "material_recorded": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("candidate_material_recorded", False),
                "material_preserved": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("candidate_material_preserved", False),
                "provenance": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("candidate_source_provenance_reference_supplied", False),
                "candidate_received": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_received", False),
                "candidate_recorded": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_recorded", False),
                "candidate_evaluated": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_side_answerable_basis_candidate_evaluated", True),
                "prior_boundary": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("prior_receiver_side_answerable_basis_reception_boundary_referenced", False),
                "failed_checks": lambda artifact: artifact.__setitem__("failed_check_count", 1),
                "second_candidate": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("second_candidate_received", True),
                "repeated_reception": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("repeated_reception_permission_created", True),
                "reusable_route": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("reusable_route_created", True),
                "attestation_created": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_attestation_created", True),
                "attestation_supported": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_attestation_supported", True),
                "answerable_receipt": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_answerable_receipt_present", True),
                "custody": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_answerable_basis_custody_distinct", True),
                "refusable": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_answerable_basis_refusable", True),
                "withheld": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("receiver_answerable_basis_could_have_been_withheld", True),
                "presence": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("presence_recorded", True),
                "follow_on": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation"].__setitem__("follow_on_work_authorized", True),
                "material_missing": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation_material"]["supplied_candidate_material_record"].pop("candidate_material"),
                "material_null": lambda artifact: artifact["receiver_side_answerable_basis_reception_operation_material"]["supplied_candidate_material_record"].__setitem__("candidate_material", None),
            }
            for index, (name, mutate) in enumerate(cases.items()):
                with self.subTest(name=name):
                    artifact = self._synthetic_artifact()
                    mutate(artifact)
                    artifact_path = self._write_json(directory / self.safe_json_filename(name, index), artifact)
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(self._base_request(specification_path, artifact_path))
                    self.assertIn(result["outcome"], (resolver.OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS, resolver.OUTCOME_BLOCKED))
                    self.assertIs(result["receiver_side_answerable_basis_candidate_evaluation_boundary"]["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"], False)
                    self.assert_refusal_posture(result)
                    self.assert_all_emitted_codes_public(result)

    def test_request_intents_markers_and_shape_refuse_expansion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            specification_path, artifact_path = self._fixture_paths(directory)
            base = self._base_request(specification_path, artifact_path)
            not_recorded = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
                dict(base, intent=resolver.INTENT_DO_NOT_RECORD)
            )
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(not_recorded["receiver_side_answerable_basis_candidate_evaluation_boundary"]["receiver_side_answerable_basis_candidate_evaluation_boundary_recorded"], False)
            self.assert_refusal_posture(not_recorded)
            explicit_block = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
                dict(base, intent=resolver.INTENT_BLOCK)
            )
            self.assert_blocked_public(explicit_block, "EXPLICIT_BLOCK_REQUESTED")

            invalid_requests = [
                ("not_mapping", []),
                ("unsupported", dict(base, intent="UNSUPPORTED")),
                ("wrong_id", dict(base, boundary_id="wrong")),
                ("alternate_candidate", dict(base, alternate_candidate="not allowed")),
                ("candidate_material_input", dict(base, candidate_material={"not": "allowed"})),
            ]
            for name, request in invalid_requests:
                with self.subTest(name=name):
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result)

            broken_specification = self._synthetic_specification().replace("Receiver-Side Answerable Basis Candidate Evaluation Boundary V0 Minimum Specification", "missing", 1)
            broken_path = self._write_text(directory / "broken.md", broken_specification)
            result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(self._base_request(broken_path, artifact_path))
            self.assert_blocked_public(result, "BOUNDARY_SPEC_MARKER_MISSING")
            missing_spec = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(self._base_request(directory / "missing.md", artifact_path))
            self.assert_blocked_public(missing_spec, "BOUNDARY_SPEC_REFERENCE_MISSING")

    def test_prohibited_flags_non_claims_and_preclaims_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            specification_path, artifact_path = self._fixture_paths(Path(temporary))
            base = self._base_request(specification_path, artifact_path)
            for flag, expected_code in resolver.PROHIBITED_REQUEST_FLAGS.items():
                with self.subTest(flag=flag):
                    request = copy.deepcopy(base)
                    request[flag] = True
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result, expected_code)
                    self.assertGreater(self.failed_check_count(result), 0)
                    self.assert_refusal_posture(result)
            for field in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
                with self.subTest(preclaim=field):
                    request = copy.deepcopy(base)
                    request[field] = True
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result, "RESULT_POSTURE_PRECLAIMED")
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result, "NON_CLAIM_MISSING_OR_FLIPPED")
            malformed_non_claims = (None, [], {"missing": False})
            for value in malformed_non_claims:
                with self.subTest(malformed_non_claims=repr(value)):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"] = value
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result, "NON_CLAIM_MISSING_OR_FLIPPED")
            first_non_claim = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
            for value in (None, 0, "", "false"):
                with self.subTest(non_boolean_non_claim=repr(value)):
                    request = copy.deepcopy(base)
                    request["declared_non_claims"][first_non_claim] = value
                    result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(request)
                    self.assert_blocked_public(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_from_path_write_nonmutation_and_predecessor_comparison(self) -> None:
        predecessor_path = SRC_ROOT / "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min.py"
        v2_path = SRC_ROOT / "resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2.py"
        predecessor_before, v2_before = predecessor_path.read_bytes(), v2_path.read_bytes()
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            specification_path, artifact_path = self._fixture_paths(directory)
            request = self._declared_request(specification_path, artifact_path)
            request_before = copy.deepcopy(request)
            artifact_before = artifact_path.read_bytes()
            specification_before = specification_path.read_bytes()
            request_path = self._write_json(directory / "request.json", request)
            result = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertEqual(request, request_before)
            self.assertEqual(artifact_path.read_bytes(), artifact_before)
            self.assertEqual(specification_path.read_bytes(), specification_before)
            missing_request = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path(directory / "missing-request.json")
            self.assert_blocked_public(missing_request, "REQUEST_PATH_UNREADABLE")
            malformed_request_path = self._write_text(directory / "malformed-request.json", "{")
            malformed_request = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path(malformed_request_path)
            self.assert_blocked_public(malformed_request, "REQUEST_JSON_INVALID")
            list_request_path = self._write_json(directory / "list-request.json", [])
            list_request = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_from_path(list_request_path)
            self.assert_blocked_public(list_request, "REQUEST_NOT_MAPPING")

            output = directory / "out" / resolver.OUTPUT_FILENAME
            first = resolver.write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result(result, output)
            second = resolver.write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result(result, output)
            self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(second.name, output.with_name(f"{output.stem}_001{output.suffix}").name)
            written = json.loads(first.read_text(encoding="utf-8"))
            self.assertEqual(written["resolver_module"], resolver.RESOLVER_MODULE)
            self.assertEqual(written["result_version"], resolver.RESULT_VERSION)
            self.assert_candidate_material_absent(written)
            self.assert_canonical_non_claims(written)

            requires = resolver.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2(
                self._base_request(specification_path, directory / "missing.json")
            )
            self.assertEqual(requires["outcome"], resolver.OUTCOME_REQUIRES_RECORDED_CANDIDATE_BASIS)
            written_requires = resolver.write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result(requires, directory / "out" / "requires.json")
            self.assertTrue(written_requires.is_file())

            for malformed in ({}, {"resolver_module": "wrong", "result_version": resolver.RESULT_VERSION, "outcome": resolver.OUTCOME_ALLOWED, "non_claims": {}}, dict(result, candidate_material={"copied": True})):
                with self.subTest(malformed=repr(malformed)[:40]):
                    with self.assertRaises(resolver.ReceiverSideAnswerableBasisCandidateEvaluationBoundaryV0MinV2Error):
                        resolver.write_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_v2_result(malformed, directory / "out" / "refused.json")

            predecessor_result = predecessor.resolve_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min(
                predecessor.build_receiver_side_answerable_basis_candidate_evaluation_boundary_v0_min_request(
                    governing_boundary_specification_path=specification_path,
                    selected_successful_candidate_reception_artifact_path=artifact_path,
                )
            )
            self.assertEqual(predecessor_result["outcome"], result["outcome"])
            self.assertIs(
                predecessor_result["receiver_side_answerable_basis_candidate_evaluation_boundary"]["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"],
                result["receiver_side_answerable_basis_candidate_evaluation_boundary"]["receiver_side_answerable_basis_candidate_evaluation_consideration_allowed"],
            )
        self.assertEqual(predecessor_path.read_bytes(), predecessor_before)
        self.assertEqual(v2_path.read_bytes(), v2_before)


if __name__ == "__main__":
    unittest.main()
