"""Bounded tests for one receiver-side answerable-basis reception operation.

The suite uses only temporary synthetic source fixtures. It proves that one
explicit candidate can be preserved as opaque material, while missing material
waits lawfully and every conversion beyond reception remains blocked.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_reception_operation_v0_min as resolver


class ReceiverSideAnswerableBasisReceptionOperationV0MinTests(unittest.TestCase):
    """Keep candidate reception singular, opaque, and non-converting."""

    WRAPPER_FIELDS = (
        "outcome",
        "block",
        "receiver_side_answerable_basis_reception_operation_checks",
        "non_claims",
        "receiver_side_answerable_basis_reception_operation_summary",
        "receiver_side_answerable_basis_reception_operation_metadata",
        "receiver_side_answerable_basis_reception_operation_material",
    )
    MATERIAL_KEYS = (
        "prior_receiver_side_answerable_basis_reception_boundary_reference",
        "supplied_candidate_material_record",
        "receiver_side_answerable_basis_reception_operation_evaluation",
    )
    SUPPLIED_RECORD_KEYS = (
        "receiver_side_answerable_basis_candidate_id",
        "receiver_side_answerable_basis_candidate_type",
        "receiver_side_answerable_basis_candidate_scope",
        "candidate_material_supplied",
        "candidate_material",
        "candidate_source_provenance_reference_supplied",
        "candidate_source_provenance_reference",
        "candidate_material_received",
        "candidate_material_recorded",
        "candidate_material_preserved",
    )
    DOWNSTREAM_FALSE_FIELDS = (
        "second_candidate_received",
        "repeated_reception_permission_created",
        "reusable_route_created",
        "receiver_attestation_created",
        "receiver_attestation_supported",
        "receiver_answerable_receipt_present",
        "receiver_answerable_basis_custody_distinct",
        "receiver_answerable_basis_refusable",
        "receiver_answerable_basis_could_have_been_withheld",
        "presence_supported",
        "presence_authorized",
        "presence_established",
        "presence_recorded",
        "identity_created",
        "relation_created",
        "coupling_assigned",
        "coupling_created",
        "field_machinery_created",
        "runtime_created",
        "api_created",
        "public_interface_created",
        "public_intake_created",
        "mailbox_created",
        "listener_created",
        "queue_created",
        "endpoint_created",
        "shared_intake_lane_created",
        "currentness_created",
        "authority_created",
        "standing_created",
        "truth_created",
        "continuity_memory_written",
        "output_authorized",
        "action_authorized",
        "derivative_reception_authorized",
        "synchronization_authorized",
        "follow_on_authorized",
        "follow_on_work_authorized",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in safe)
        while "__" in safe:
            safe = safe.replace("__", "_")
        safe = safe.strip("._-") or "case"
        if index is not None:
            safe = f"{index:03d}_{safe}"
        return f"{safe}.json"

    def write_markdown(self, path: Path, text: str) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=True)
            handle.write("\n")
        return path

    def valid_operation_specification_text(self) -> str:
        lines = ["# Receiver-Side Answerable Basis Reception Operation V0 Minimum Specification"]
        for _, markers in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.extend(markers)
        lines.extend(
            (
                "candidate received false",
                "candidate recorded false",
                "candidate evaluated false",
                "source reference is not source identity",
                "source reference is not authority",
                "source reference is not standing",
                "source reference is not custody distinction",
                "unsupported prior claims",
            )
        )
        return "\n".join(dict.fromkeys(lines)) + "\n"

    def valid_boundary_terminal_summary_text(self) -> str:
        lines = ["# Receiver-Side Answerable Basis Reception Boundary Terminal Summary V0"]
        for _, markers in resolver.RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_CLASSES:
            lines.extend(markers)
        lines.extend(
            (
                "receiver_attestation_supported = false",
                "follow_on_authorized = false",
            )
        )
        return "\n".join(dict.fromkeys(lines)) + "\n"

    def build_base_request(self, base: Path, **overrides: Any) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = {
            "target_operation_spec_path": self.write_markdown(
                base / "operation" / "operation_spec.md", self.valid_operation_specification_text()
            ),
            "reception_boundary_terminal_summary_path": self.write_markdown(
                base / "boundary" / "boundary_summary.md", self.valid_boundary_terminal_summary_text()
            ),
        }
        request = resolver.build_receiver_side_answerable_basis_reception_operation_v0_min_request(
            **{key: str(value) for key, value in paths.items()}, **overrides
        )
        return request, paths

    def build_supplied_candidate_request(
        self, base: Path, payload: Any | None = None, **overrides: Any
    ) -> tuple[dict[str, Any], dict[str, Path]]:
        if payload is None:
            payload = {
                "opaque": ["candidate", {"nested": [1, False, {"token": "keep"}]}],
                "metadata": {"ordinal": 1},
            }
        return self.build_base_request(
            base,
            candidate_material_supplied=True,
            candidate_material=payload,
            candidate_source_provenance_reference_supplied=True,
            candidate_source_provenance_reference="declared://receiver-side-candidate",
            **overrides,
        )

    def operation(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get("receiver_side_answerable_basis_reception_operation")
        self.assertIsInstance(value, dict)
        return value

    def material(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get("receiver_side_answerable_basis_reception_operation_material")
        self.assertIsInstance(value, dict)
        return value

    def summary(self, result: Mapping[str, Any]) -> dict[str, Any]:
        value = result.get("receiver_side_answerable_basis_reception_operation_summary")
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: Mapping[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, Mapping):
            return None
        code = block.get("code") or block.get("block_code")
        return code if isinstance(code, str) else None

    def failed_check_count(self, result: Mapping[str, Any]) -> int:
        value = result.get("failed_check_count")
        return value if isinstance(value, int) else self.summary(result)["failed_check_count"]

    def passed_check_count(self, result: Mapping[str, Any]) -> int:
        value = result.get("passed_check_count")
        return value if isinstance(value, int) else self.summary(result)["passed_check_count"]

    def assert_not_blocked(self, result: Mapping[str, Any]) -> None:
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block["blocked"], False)
        self.assertIsNone(block["code"])
        self.assertIsNone(block["block_code"])

    def assert_all_emitted_codes_public(self, result: Mapping[str, Any]) -> None:
        checks = result.get("receiver_side_answerable_basis_reception_operation_checks")
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, dict)
            for field in ("block_code", "failure_code"):
                value = check.get(field)
                if value is not None:
                    self.assertIn(value, resolver.BLOCK_CODES)

    def assert_blocked_with_public_code(self, result: Mapping[str, Any], code: str | None = None) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        observed = self.block_code(result)
        self.assertIsNotNone(observed)
        self.assertIn(observed, resolver.BLOCK_CODES)
        if code is not None:
            self.assertEqual(observed, code)
        self.assertGreater(self.failed_check_count(result), 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_canonical_non_claims(self, result: Mapping[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_operation_has_no_wrapper_fields(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in self.WRAPPER_FIELDS:
            self.assertNotIn(key, operation)

    def assert_material_shape(self, result: Mapping[str, Any]) -> None:
        material = self.material(result)
        self.assertEqual(tuple(material), self.MATERIAL_KEYS)
        supplied = material["supplied_candidate_material_record"]
        self.assertIsInstance(supplied, dict)
        self.assertEqual(tuple(supplied), self.SUPPLIED_RECORD_KEYS)
        forbidden = {
            "meaning",
            "truth",
            "attestation",
            "identity",
            "custody",
            "standing",
            "presence",
        }
        self.assertFalse(forbidden.intersection(supplied))

    def assert_downstream_false(self, result: Mapping[str, Any]) -> None:
        operation = self.operation(result)
        for key in self.DOWNSTREAM_FALSE_FIELDS:
            self.assertIs(operation[key], False, key)
        self.assert_canonical_non_claims(result)
        self.assert_operation_has_no_wrapper_fields(result)
        self.assertNotIn("receiver_side_answerable_basis_reception_operation_material", operation)

    def assert_marker_classes_true(self, result: Mapping[str, Any]) -> None:
        marker_classes = []
        for key, value in result.get("upstream_basis", {}).items():
            if key.endswith("_marker_classes"):
                self.assertIsInstance(value, dict)
                marker_classes.append(value)
        self.assertTrue(marker_classes)
        for status in marker_classes:
            self.assertTrue(all(status.values()), status)

    def test_01_public_api_constants_block_codes_and_flags(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_reception_operation_v0_min",
            "resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path",
            "write_receiver_side_answerable_basis_reception_operation_v0_min_result",
            "build_receiver_side_answerable_basis_reception_operation_v0_min_summary",
            "build_receiver_side_answerable_basis_reception_operation_v0_min_request",
            "build_declared_receiver_side_answerable_basis_reception_operation_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_receiver_side_answerable_basis_reception_operation_v0_min")
        self.assertEqual(resolver.OPERATION_ID, "receiver_side_answerable_basis_reception_operation_001")
        self.assertEqual(resolver.OPERATION_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION")
        self.assertEqual(resolver.OPERATION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.OPERATION_SCOPE,
            "RECEIVE_ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_AS_CANDIDATE_MATERIAL_ONLY",
        )
        self.assertEqual(resolver.PRIOR_BOUNDARY_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY")
        self.assertEqual(
            resolver.PRIOR_BOUNDARY_OUTCOME_REQUIRED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_ALLOWED",
        )
        self.assertEqual(
            resolver.PRIOR_BOUNDARY_RESULT_REQUIRED,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED",
        )
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_THEN_CANDIDATE_EVALUATION_BOUNDARY_ONLY",
        )
        self.assertEqual(resolver.CANDIDATE_ID, "receiver_side_answerable_basis_candidate_001")
        self.assertEqual(resolver.CANDIDATE_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE")
        self.assertEqual(
            resolver.CANDIDATE_SCOPE,
            "ONE_SEPARATELY_SUPPLIED_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_ONLY",
        )
        self.assertTrue(resolver.PRIOR_BOUNDARY_RECORDED_REQUIRED)
        self.assertTrue(resolver.PRIOR_BOUNDARY_RESULT_RECORDED_REQUIRED)
        self.assertFalse(resolver.PRIOR_CANDIDATE_RECEIVED_REQUIRED)
        self.assertFalse(resolver.PRIOR_CANDIDATE_RECORDED_REQUIRED)
        self.assertFalse(resolver.PRIOR_CANDIDATE_EVALUATED_REQUIRED)
        self.assertTrue(set(resolver.OUTCOME_FAMILY).issuperset({
            resolver.OUTCOME_RECORDED,
            resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL,
            resolver.OUTCOME_BLOCKED,
            resolver.OUTCOME_NOT_RECORDED,
        }))
        self.assertTrue(set(resolver.SUPPORTED_INTENTS).issuperset({
            resolver.INTENT_RECORD, resolver.INTENT_DO_NOT_RECORD, resolver.INTENT_BLOCK
        }))
        self.assertTrue(str(resolver.OUTPUT_ROOT).endswith(
            "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_operation_v0_min"
        ))
        self.assertEqual(
            resolver.OUTPUT_FILENAME,
            "receiver_side_answerable_basis_reception_operation_001__receiver_side_answerable_basis_reception_operation_v0_min_result.json",
        )
        required_codes = {
            "REQUEST_NOT_MAPPING", "UNSUPPORTED_INTENT", "OPERATION_SPEC_REFERENCE_MISSING",
            "OPERATION_SPEC_MARKER_MISSING", "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", "REQUEST_VALUE_MISMATCH",
            "NON_CLAIM_MISSING_OR_FLIPPED", "CANDIDATE_MATERIAL_NOT_JSON_COMPATIBLE",
            "CANDIDATE_MATERIAL_INCOMPLETE", "CANDIDATE_SOURCE_PROVENANCE_REFERENCE_MISSING",
            "MULTIPLE_CANDIDATES_REQUESTED", "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
            "PROHIBITED_ANSWERABLE_BASIS_SUFFICIENCY_REQUESTED",
            "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
            "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
            "PROHIBITED_SECOND_CANDIDATE_REQUESTED", "RESULT_POSTURE_PRECLAIMED",
            "EXPLICIT_BLOCK_REQUESTED", "WRITE_REFUSED",
        }
        self.assertTrue(required_codes.issubset(resolver.BLOCK_CODES))
        expected_flags = {
            "request_candidate_evaluation": "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED",
            "request_answerable_basis_sufficiency": "PROHIBITED_ANSWERABLE_BASIS_SUFFICIENCY_REQUESTED",
            "request_receiver_attestation_creation": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
            "request_receiver_attestation_support": "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED",
            "request_receiver_answerable_receipt_creation": "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED",
            "request_custody_distinctness_decision": "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED",
            "request_refusability_decision": "PROHIBITED_REFUSABILITY_DECISION_REQUESTED",
            "request_could_have_been_withheld_decision": "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED",
            "request_second_candidate_reception": "PROHIBITED_SECOND_CANDIDATE_REQUESTED",
            "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
        }
        for key, code in expected_flags.items():
            self.assertEqual(resolver.PROHIBITED_REQUEST_FLAGS[key], code)
        self.assertNotEqual(
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_attestation_creation"],
            resolver.PROHIBITED_REQUEST_FLAGS["request_receiver_answerable_receipt_creation"],
        )

    def test_02_synthetic_missing_candidate_result_structure_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_base_request(Path(temporary))
            result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assertGreater(self.passed_check_count(result), 0)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        self.assertTrue(operation["receiver_side_answerable_basis_reception_operation_recorded"])
        self.assertTrue(operation["receiver_side_answerable_basis_reception_operation_result_recorded"])
        self.assertEqual(
            operation["receiver_side_answerable_basis_reception_operation_result"],
            "REQUIRES_CANDIDATE_MATERIAL",
        )
        for key in (
            "candidate_material_supplied", "candidate_material_received", "candidate_material_recorded",
            "candidate_material_preserved", "candidate_source_provenance_reference_supplied",
            "receiver_side_answerable_basis_candidate_received",
            "receiver_side_answerable_basis_candidate_recorded",
            "receiver_side_answerable_basis_candidate_evaluated",
        ):
            self.assertIs(operation[key], False, key)
        self.assertTrue(operation["prior_receiver_side_answerable_basis_reception_boundary_referenced"])
        self.assertTrue(result["missing_or_insufficient_candidate_material"])
        self.assert_material_shape(result)
        supplied = self.material(result)["supplied_candidate_material_record"]
        self.assertIsNone(supplied["candidate_material"])
        self.assertIsNone(supplied["candidate_source_provenance_reference"])
        self.assert_downstream_false(result)
        self.assert_marker_classes_true(result)
        summary = resolver.build_receiver_side_answerable_basis_reception_operation_v0_min_summary(result)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["missing_or_insufficient_candidate_material"])

    def test_03_default_live_repo_result_if_available(self) -> None:
        target = REPO_ROOT / resolver.DEFAULT_OPERATION_SPEC_REFERENCE
        boundary = REPO_ROOT / resolver.DEFAULT_RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
        if not target.is_file() or not boundary.is_file():
            self.skipTest("default upstream files are unavailable")
        result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min()
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        self.assertTrue(self.operation(result)["prior_receiver_side_answerable_basis_reception_boundary_referenced"])
        self.assertTrue(result["missing_or_insufficient_candidate_material"])
        self.assert_downstream_false(result)

    def test_04_successful_candidate_reception_preserves_material_by_deep_copy(self) -> None:
        payload = {"outer": [{"nested": [1, {"keep": "exact"}]}], "flag": False}
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_supplied_candidate_request(Path(temporary), payload)
            original_request = copy.deepcopy(request)
            original_payload = copy.deepcopy(payload)
            result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(self.failed_check_count(result), 0)
        self.assert_not_blocked(result)
        operation = self.operation(result)
        for key in resolver.ALLOWED_TRUE_RECORDED_FIELDS:
            self.assertIs(operation[key], True, key)
        self.assertIs(operation["receiver_side_answerable_basis_candidate_evaluated"], False)
        emitted = self.material(result)["supplied_candidate_material_record"]["candidate_material"]
        self.assertEqual(emitted, original_payload)
        self.assertIsNot(emitted, payload)
        payload["outer"][0]["nested"][1]["keep"] = "changed-input"
        self.assertEqual(emitted, original_payload)
        emitted["outer"][0]["nested"][1]["keep"] = "changed-result"
        self.assertEqual(request, original_request)
        self.assert_downstream_false(result)
        self.assert_material_shape(result)

    def test_05_candidate_json_compatibility_and_completeness(self) -> None:
        valid_values = ("opaque", 7, True, ["x", 1], {"x": [False, {"y": 2}]})
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, value in enumerate(valid_values):
                with self.subTest(valid_type=type(value).__name__):
                    request, _ = self.build_supplied_candidate_request(base / f"valid_{index}", value)
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
                    self.assertEqual(self.failed_check_count(result), 0)
            invalid_values = (set(["x"]), b"bytes", object(), lambda: None)
            circular: list[Any] = []
            circular.append(circular)
            for index, value in enumerate((*invalid_values, circular)):
                with self.subTest(invalid_type=type(value).__name__):
                    request, _ = self.build_supplied_candidate_request(base / f"invalid_{index}", value)
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(
                        result, "CANDIDATE_MATERIAL_NOT_JSON_COMPATIBLE"
                    )
        completeness_cases: tuple[tuple[str, Any], ...] = (
            ("candidate_material_supplied_false", {"candidate_material_supplied": False}),
            ("candidate_material_missing", {"candidate_material": None}),
            ("candidate_material_empty_string", {"candidate_material": ""}),
            ("candidate_material_empty_list", {"candidate_material": []}),
            ("candidate_material_empty_mapping", {"candidate_material": {}}),
            ("provenance_supplied_false", {"candidate_source_provenance_reference_supplied": False}),
            ("provenance_missing", {"candidate_source_provenance_reference": None}),
            ("provenance_empty", {"candidate_source_provenance_reference": ""}),
        )
        with tempfile.TemporaryDirectory() as temporary:
            for index, (name, mutation) in enumerate(completeness_cases):
                with self.subTest(case=name):
                    request, _ = self.build_supplied_candidate_request(Path(temporary) / f"missing_{index}")
                    request.update(mutation)
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL, resolver.OUTCOME_BLOCKED),
                    )
                    self.assertIs(
                        self.operation(result)["receiver_side_answerable_basis_candidate_received"], False
                    )
                    self.assert_downstream_false(result)

    def test_06_multiple_evaluation_sufficiency_and_preclaim_routes_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            requests: list[tuple[str, dict[str, Any], str]] = []
            request, _ = self.build_supplied_candidate_request(base / "second_flag")
            request["request_second_candidate_reception"] = True
            requests.append(("second_flag", request, "PROHIBITED_SECOND_CANDIDATE_REQUESTED"))
            request, _ = self.build_supplied_candidate_request(base / "second_shape")
            request["second_candidate_material"] = {"not": "allowed"}
            requests.append(("second_shape", request, "MULTIPLE_CANDIDATES_REQUESTED"))
            request, _ = self.build_supplied_candidate_request(base / "evaluation")
            request["request_candidate_evaluation"] = True
            requests.append(("evaluation", request, "PROHIBITED_CANDIDATE_EVALUATION_REQUESTED"))
            request, _ = self.build_supplied_candidate_request(base / "sufficiency")
            request["request_answerable_basis_sufficiency"] = True
            requests.append(("sufficiency", request, "PROHIBITED_ANSWERABLE_BASIS_SUFFICIENCY_REQUESTED"))
            for field in (
                "receiver_side_answerable_basis_reception_operation_recorded",
                "receiver_side_answerable_basis_reception_operation_result_recorded",
                "candidate_material_received",
                "candidate_material_recorded",
                "candidate_material_preserved",
                "receiver_side_answerable_basis_candidate_received",
                "receiver_side_answerable_basis_candidate_recorded",
                "prior_receiver_side_answerable_basis_reception_boundary_referenced",
                "receiver_side_answerable_basis_candidate_evaluated",
            ):
                request, _ = self.build_supplied_candidate_request(base / self.safe_json_filename(field))
                request[field] = True
                requests.append((field, request, "RESULT_POSTURE_PRECLAIMED"))
            for name, request, code in requests:
                with self.subTest(case=name):
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, code)
                    self.assertIs(
                        self.operation(result)["receiver_side_answerable_basis_candidate_received"], False
                    )
                    self.assert_downstream_false(result)

    def test_07_attestation_receipt_custody_and_presence_routes_are_distinct_and_blocked(self) -> None:
        cases = (
            ("attestation", "request_receiver_attestation_creation", "PROHIBITED_RECEIVER_ATTESTATION_REQUESTED"),
            ("receipt", "request_receiver_answerable_receipt_creation", "PROHIBITED_RECEIVER_ANSWERABLE_RECEIPT_REQUESTED"),
            ("custody", "request_custody_distinctness_decision", "PROHIBITED_CUSTODY_DISTINCTNESS_DECISION_REQUESTED"),
            ("refusability", "request_refusability_decision", "PROHIBITED_REFUSABILITY_DECISION_REQUESTED"),
            ("withholding", "request_could_have_been_withheld_decision", "PROHIBITED_COULD_HAVE_BEEN_WITHHELD_DECISION_REQUESTED"),
            ("presence_support", "request_presence_support", "PROHIBITED_PRESENCE_REQUESTED"),
            ("presence_authorization", "request_presence_authorization", "PROHIBITED_PRESENCE_REQUESTED"),
            ("presence_establishment", "request_presence_establishment", "PROHIBITED_PRESENCE_REQUESTED"),
            ("presence_recording", "request_presence_recording", "PROHIBITED_PRESENCE_REQUESTED"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            for index, (name, flag, code) in enumerate(cases):
                with self.subTest(case=name):
                    request, _ = self.build_supplied_candidate_request(Path(temporary) / f"case_{index}")
                    request[flag] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, code)
                    self.assertIs(self.operation(result)["receiver_attestation_created"], False)
                    self.assertIs(self.operation(result)["receiver_answerable_receipt_present"], False)
                    self.assert_downstream_false(result)

    def test_08_all_prohibited_flags_and_required_non_claims_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, flag in enumerate(resolver.PROHIBITED_REQUEST_FLAGS):
                with self.subTest(prohibited_flag=flag):
                    request, _ = self.build_supplied_candidate_request(base / f"flag_{index}")
                    request[flag] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, resolver.PROHIBITED_REQUEST_FLAGS[flag])
                    self.assertIs(
                        self.operation(result)["receiver_side_answerable_basis_candidate_received"], False
                    )
            for index, key in enumerate(resolver.REQUIRED_FALSE_NON_CLAIMS):
                with self.subTest(non_claim=key):
                    request, _ = self.build_base_request(base / f"non_claim_{index}")
                    request["declared_non_claims"][key] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, "NON_CLAIM_MISSING_OR_FLIPPED")
            malformed_cases = (
                ("absent", None), ("non_mapping", []),
                ("missing_key", "missing_key"), ("none", None), ("zero", 0), ("string", "false"),
            )
            for index, (name, value) in enumerate(malformed_cases):
                with self.subTest(declared_non_claims=name):
                    request, _ = self.build_base_request(base / f"malformed_{index}")
                    if name == "absent":
                        request.pop("declared_non_claims")
                    elif name == "non_mapping":
                        request["declared_non_claims"] = value
                    else:
                        request["declared_non_claims"][resolver.REQUIRED_FALSE_NON_CLAIMS[0]] = value
                    result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
                    self.assert_blocked_with_public_code(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_09_request_intents_identifiers_and_marker_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min([]),
                "REQUEST_NOT_MAPPING",
            )
            request, _ = self.build_base_request(base / "unsupported", intent="UNSUPPORTED")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                "UNSUPPORTED_INTENT",
            )
            for index, key in enumerate((
                "operation_id", "operation_type", "operation_version", "operation_scope",
                "prior_receiver_side_answerable_basis_reception_boundary_type",
                "prior_receiver_side_answerable_basis_reception_boundary_outcome_required",
                "prior_receiver_side_answerable_basis_reception_boundary_result_required",
                "receiver_side_answerable_basis_candidate_id",
                "receiver_side_answerable_basis_candidate_type",
                "receiver_side_answerable_basis_candidate_scope", "admissible_future_route",
            )):
                with self.subTest(identifier=key):
                    request, _ = self.build_base_request(base / f"identifier_{index}")
                    request[key] = "wrong"
                    self.assert_blocked_with_public_code(
                        resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                        "REQUEST_VALUE_MISMATCH",
                    )
            request, _ = self.build_supplied_candidate_request(base / "do_not", intent=resolver.INTENT_DO_NOT_RECORD)
            result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
            self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assert_not_blocked(result)
            self.assertIs(self.operation(result)["receiver_side_answerable_basis_reception_operation_recorded"], False)
            self.assertIs(self.operation(result)["receiver_side_answerable_basis_candidate_received"], False)
            self.assert_downstream_false(result)
            request, _ = self.build_base_request(base / "explicit", intent=resolver.INTENT_BLOCK)
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                "EXPLICIT_BLOCK_REQUESTED",
            )
            for index, (class_name, markers) in enumerate(resolver.TARGET_SPEC_MARKER_CLASSES):
                with self.subTest(spec_marker_class=class_name):
                    request, paths = self.build_base_request(base / f"spec_marker_{index}")
                    text = paths["target_operation_spec_path"].read_text(encoding="utf-8")
                    paths["target_operation_spec_path"].write_text(text.replace(markers[0], ""), encoding="utf-8")
                    self.assert_blocked_with_public_code(
                        resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                        "OPERATION_SPEC_MARKER_MISSING",
                    )
            for index, (class_name, markers) in enumerate(resolver.RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_CLASSES):
                with self.subTest(boundary_marker_class=class_name):
                    request, paths = self.build_base_request(base / f"boundary_marker_{index}")
                    text = paths["reception_boundary_terminal_summary_path"].read_text(encoding="utf-8")
                    paths["reception_boundary_terminal_summary_path"].write_text(text.replace(markers[0], ""), encoding="utf-8")
                    self.assert_blocked_with_public_code(
                        resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                        "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
                    )
            request, _ = self.build_base_request(base / "missing_spec")
            request["target_operation_spec_path"] = str(base / "missing" / "operation.md")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                "OPERATION_SPEC_REFERENCE_MISSING",
            )
            request, _ = self.build_base_request(base / "missing_boundary")
            request["reception_boundary_terminal_summary_path"] = str(base / "missing" / "boundary.md")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request),
                "RECEPTION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
            )

    def test_10_from_path_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, _ = self.build_base_request(base / "request")
            request_path = self.write_json(base / "request" / "declared.json", request)
            result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path(request_path)
            self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_CANDIDATE_MATERIAL)
            self.assertEqual(self.failed_check_count(result), 0)
            missing = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path(
                base / "request" / "missing.json"
            )
            self.assert_blocked_with_public_code(missing, "REQUEST_PATH_UNREADABLE")
            malformed = base / "request" / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path(malformed),
                "REQUEST_JSON_INVALID",
            )
            array_path = self.write_json(base / "request" / "array.json", [])
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min_from_path(array_path),
                "REQUEST_NOT_MAPPING",
            )
            output = base / "output" / resolver.OUTPUT_FILENAME
            first = resolver.write_receiver_side_answerable_basis_reception_operation_v0_min_result(result, output)
            second = resolver.write_receiver_side_answerable_basis_reception_operation_v0_min_result(result, output)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertEqual(first.name, resolver.OUTPUT_FILENAME)
            self.assertEqual(second.name, output.with_name(f"{output.stem}_001{output.suffix}").name)
            self.assertEqual(json.loads(first.read_text(encoding="utf-8"))["outcome"], result["outcome"])
            self.assertIn("receiver_side_answerable_basis_reception_operation_v0_min", str(resolver.OUTPUT_ROOT))
            forbidden_roots = ("boundary", "presence", "relation", "descendant", "runtime", "daemon", "FIELD")
            self.assertFalse(any(part in forbidden_roots for part in first.parts[:-2]))

    def test_11_non_mutation_and_smoke(self) -> None:
        payload = {"nested": [1, {"value": "opaque"}]}
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_supplied_candidate_request(base, payload)
            request_before = copy.deepcopy(request)
            payload_before = copy.deepcopy(payload)
            source_before = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            resolver_before = (SRC_ROOT / "resolve_receiver_side_answerable_basis_reception_operation_v0_min.py").read_text(
                encoding="utf-8"
            )
            result = resolver.resolve_receiver_side_answerable_basis_reception_operation_v0_min(request)
            summary = resolver.build_receiver_side_answerable_basis_reception_operation_v0_min_summary(result)
            self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(summary["outcome"], resolver.OUTCOME_RECORDED)
            self.assertEqual(request, request_before)
            self.assertEqual(payload, payload_before)
            self.assertEqual(
                {key: path.read_text(encoding="utf-8") for key, path in paths.items()}, source_before
            )
            self.assertEqual(
                (SRC_ROOT / "resolve_receiver_side_answerable_basis_reception_operation_v0_min.py").read_text(
                    encoding="utf-8"
                ),
                resolver_before,
            )
            self.assert_material_shape(result)
            self.assert_downstream_false(result)


if __name__ == "__main__":
    unittest.main()
