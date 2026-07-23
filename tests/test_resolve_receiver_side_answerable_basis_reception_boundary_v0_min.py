"""Executable boundary tests for receiver-side answerable-basis consideration.

The suite creates only temporary synthetic Markdown and JSON fixtures.  It
proves that the resolver can record candidate-reception consideration after a
clean presence waiting posture, without receiving or evaluating a candidate or
creating attestation, presence, runtime, public, or downstream behavior.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_receiver_side_answerable_basis_reception_boundary_v0_min as resolver


class ReceiverSideAnswerableBasisReceptionBoundaryV0MinTests(unittest.TestCase):
    """Keep the boundary local, read-only, and candidate-material-free."""

    WRAPPER_FIELDS = (
        "outcome",
        "block",
        "receiver_side_answerable_basis_reception_boundary_checks",
        "non_claims",
        "receiver_side_answerable_basis_reception_boundary_summary",
        "receiver_side_answerable_basis_reception_boundary_metadata",
        "receiver_side_answerable_basis_reception_boundary_material",
    )
    FALSE_BOUNDARY_FIELDS = (
        "receiver_side_answerable_basis_candidate_received",
        "receiver_side_answerable_basis_candidate_recorded",
        "receiver_side_answerable_basis_candidate_evaluated",
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
        "reusable_route_created",
        "repeated_reception_permission_created",
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
        "repository_scan_performed",
        "file_discovery_performed",
        "repair_performed",
        "validation_enforced",
    )

    def safe_json_filename(self, name: str, index: int | None = None) -> str:
        safe = str(name).replace("/", "_").replace("\\", "_").replace(" ", "_")
        safe = "".join(character if character.isalnum() or character in "._-" else "_" for character in safe)
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

    def boundary_spec_text(self) -> str:
        lines = ["# Receiver-Side Answerable Basis Reception Boundary V0 Minimum Specification"]
        for _, markers in resolver.TARGET_SPEC_MARKER_CLASSES:
            lines.extend(markers)
        return "\n".join(lines) + "\n"

    def presence_operation_terminal_summary_text(self) -> str:
        lines = ["# Presence Operation Terminal Summary V0"]
        for _, markers in resolver.PRESENCE_WAITING_MARKER_CLASSES:
            lines.extend(markers)
        lines.append("presence waiting basis remains insufficient")
        return "\n".join(lines) + "\n"

    def presence_boundary_terminal_summary_text(self) -> str:
        return "# Presence Boundary Terminal Summary V0\nPRESENCE_BOUNDARY_ALLOWED\nPRESENCE_OPERATION_CONSIDERATION_ALLOWED\n"

    def relation_lapse_operation_terminal_summary_text(self) -> str:
        return "# Relation Lapse Operation Terminal Summary V0\nRELATION_LAPSE_OPERATION_RECORDED\nRELATION_LAPSE_SUPPORTED\n"

    def existence_claim_evidence_check_terminal_summary_text(self) -> str:
        return (
            "# Existence Claim Evidence Check Terminal Summary V0\n"
            "UNSUPPORTED\n"
            "descendant_body_basis_candidate_a_created = true\n"
            "descendant_body_basis_candidate_b_created = true\n"
            "descendant_body_basis_derivation_event_recorded = true\n"
        )

    def build_valid_synthetic_request(self, base: Path) -> tuple[dict[str, Any], dict[str, Path]]:
        paths = {
            "target_boundary_spec_path": self.write_markdown(
                base / "target" / "receiver_side_answerable_basis_reception_boundary.md",
                self.boundary_spec_text(),
            ),
            "presence_operation_terminal_summary_path": self.write_markdown(
                base / "presence" / "presence_operation_terminal_summary.md",
                self.presence_operation_terminal_summary_text(),
            ),
            "presence_boundary_terminal_summary_path": self.write_markdown(
                base / "presence" / "presence_boundary_terminal_summary.md",
                self.presence_boundary_terminal_summary_text(),
            ),
            "relation_lapse_operation_terminal_summary_path": self.write_markdown(
                base / "relation" / "relation_lapse_operation_terminal_summary.md",
                self.relation_lapse_operation_terminal_summary_text(),
            ),
            "existence_claim_evidence_check_terminal_summary_path": self.write_markdown(
                base / "existence" / "existence_claim_evidence_check_terminal_summary.md",
                self.existence_claim_evidence_check_terminal_summary_text(),
            ),
        }
        request = resolver.build_receiver_side_answerable_basis_reception_boundary_v0_min_request(
            **{key: str(value) for key, value in paths.items()}
        )
        return request, paths

    def boundary(self, result: dict[str, Any]) -> dict[str, Any]:
        value = result.get("receiver_side_answerable_basis_reception_boundary")
        self.assertIsInstance(value, dict)
        return value

    def summary(self, result: dict[str, Any]) -> dict[str, Any]:
        value = result.get("receiver_side_answerable_basis_reception_boundary_summary")
        self.assertIsInstance(value, dict)
        return value

    def block_code(self, result: dict[str, Any]) -> str | None:
        block = result.get("block")
        if not isinstance(block, dict):
            return None
        value = block.get("code") or block.get("block_code")
        return value if isinstance(value, str) else None

    def assert_allowed_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block["blocked"], False)
        self.assertIsNone(block["code"])
        self.assertIsNone(block["block_code"])
        self.assertIsNone(block["reason"])

    def assert_requires_not_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS)
        block = result.get("block")
        self.assertIsInstance(block, dict)
        self.assertIs(block["blocked"], False)
        self.assertIsNone(block["code"])
        self.assertIsNone(block["block_code"])

    def assert_blocked_with_public_code(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        code = self.block_code(result)
        self.assertIsNotNone(code)
        self.assertIn(code, resolver.BLOCK_CODES)
        self.assertGreater(self.summary(result)["failed_check_count"], 0)
        self.assert_all_emitted_codes_public(result)
        self.assert_canonical_non_claims(result)

    def assert_all_emitted_codes_public(self, result: dict[str, Any]) -> None:
        checks = result.get("receiver_side_answerable_basis_reception_boundary_checks", [])
        self.assertIsInstance(checks, list)
        for check in checks:
            self.assertIsInstance(check, dict)
            for key in ("block_code", "failure_code"):
                code = check.get(key)
                if code is not None:
                    self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict[str, Any]) -> None:
        non_claims = result.get("non_claims")
        self.assertIsInstance(non_claims, dict)
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_boundary_has_no_wrapper_fields(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in self.WRAPPER_FIELDS:
            self.assertNotIn(key, boundary)

    def assert_final_false_posture(self, result: dict[str, Any]) -> None:
        boundary = self.boundary(result)
        for key in self.FALSE_BOUNDARY_FIELDS:
            self.assertIs(boundary[key], False, key)
        self.assert_canonical_non_claims(result)

    def assert_allowed_boundary(self, result: dict[str, Any]) -> None:
        self.assert_allowed_not_blocked(result)
        self.assertEqual(self.summary(result)["failed_check_count"], 0)
        boundary = self.boundary(result)
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            boundary["receiver_side_answerable_basis_reception_boundary_result"],
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED",
        )
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
            self.assertIs(boundary[key], True, key)
        self.assert_final_false_posture(result)
        self.assert_boundary_has_no_wrapper_fields(result)

    def test_01_public_api_constants_and_default_request(self) -> None:
        for name in (
            "resolve_receiver_side_answerable_basis_reception_boundary_v0_min",
            "resolve_receiver_side_answerable_basis_reception_boundary_v0_min_from_path",
            "write_receiver_side_answerable_basis_reception_boundary_v0_min_result",
            "build_receiver_side_answerable_basis_reception_boundary_v0_min_summary",
            "build_receiver_side_answerable_basis_reception_boundary_v0_min_request",
            "build_declared_receiver_side_answerable_basis_reception_boundary_v0_min_request",
        ):
            self.assertTrue(callable(getattr(resolver, name)))
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.RESOLVER_MODULE, "resolve_receiver_side_answerable_basis_reception_boundary_v0_min")
        self.assertEqual(resolver.BOUNDARY_ID, "receiver_side_answerable_basis_reception_boundary_001")
        self.assertEqual(resolver.BOUNDARY_TYPE, "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY")
        self.assertEqual(resolver.BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.BOUNDARY_SCOPE,
            "CONSIDER_ONE_RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_AFTER_PRESENCE_REQUIRES_RECEIVER_ATTESTATION_ONLY",
        )
        self.assertEqual(resolver.PRIOR_PRESENCE_OPERATION_TYPE, "PRESENCE_OPERATION")
        self.assertEqual(
            resolver.PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED,
            "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION",
        )
        self.assertEqual(resolver.PRIOR_PRESENCE_RESULT_REQUIRED, "REQUIRES_RECEIVER_ATTESTATION")
        for name in (
            "PRIOR_PRESENCE_OPERATION_RECORDED_REQUIRED",
            "PRIOR_PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION_REQUIRED",
            "PRIOR_RECEIVER_ATTESTATION_REQUIRED",
            "PRIOR_RECEIVER_ANSWERABLE_BASIS_REQUIRED",
            "PRIOR_REPO_LOCAL_EXECUTION_ONLY_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), True)
        for name in (
            "PRIOR_PRESENCE_SUPPORTED_REQUIRED",
            "PRIOR_PRESENCE_AUTHORIZED_REQUIRED",
            "PRIOR_PRESENCE_ESTABLISHED_REQUIRED",
            "PRIOR_PRESENCE_RECORDED_REQUIRED",
            "PRIOR_RECEIVER_ATTESTED_REQUIRED",
            "PRIOR_RECEIVER_ANSWERABLE_RECEIPT_PRESENT_REQUIRED",
            "PRIOR_RECEIVER_ANSWERABLE_BASIS_CUSTODY_DISTINCT_REQUIRED",
            "PRIOR_RECEIVER_ANSWERABLE_BASIS_REFUSABLE_REQUIRED",
            "PRIOR_RECEIVER_ANSWERABLE_BASIS_COULD_HAVE_BEEN_WITHHELD_REQUIRED",
            "PRIOR_OPERATOR_ONLY_ATTESTATION_ADMISSIBLE_REQUIRED",
            "PRIOR_DERIVATIVE_RENDERING_ADMISSIBLE_REQUIRED",
            "PRIOR_SAME_CUSTODY_COUNTERSIGNATURE_ADMISSIBLE_REQUIRED",
            "PRIOR_AUTOMATIC_ACKNOWLEDGEMENT_ADMISSIBLE_REQUIRED",
            "PRIOR_GENERATED_AFFIRMATION_ADMISSIBLE_REQUIRED",
        ):
            self.assertIs(getattr(resolver, name), False)
        self.assertEqual(
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_BOUNDARY_THEN_RECEIVER_SIDE_ANSWERABLE_BASIS_RECEPTION_OPERATION_ONLY",
        )
        self.assertIn(resolver.OUTCOME_ALLOWED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_BLOCKED, resolver.OUTCOME_FAMILY)
        self.assertIn(resolver.OUTCOME_NOT_RECORDED, resolver.OUTCOME_FAMILY)
        self.assertTrue(
            str(resolver.OUTPUT_ROOT).endswith(
                "artifacts/integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_boundary_v0_min"
            )
        )
        for code in (
            "REQUEST_NOT_MAPPING",
            "UNSUPPORTED_INTENT",
            "PRESENCE_WAITING_BASIS_MISSING_OR_INSUFFICIENT",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "PROHIBITED_CANDIDATE_RECEPTION_REQUESTED",
            "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
            "WRITE_REFUSED",
        ):
            self.assertIn(code, resolver.BLOCK_CODES)
        request = resolver.build_receiver_side_answerable_basis_reception_boundary_v0_min_request()
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
            self.assertIs(request[key], False)

    def test_02_synthetic_allowed_result_and_wrapper_separation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
        self.assert_allowed_boundary(result)
        expected_sections = {
            "receiver_side_answerable_basis_reception_boundary_metadata",
            "declared_receiver_side_answerable_basis_reception_boundary_basis",
            "upstream_basis",
            "receiver_side_answerable_basis_reception_boundary",
            "receiver_side_answerable_basis_reception_boundary_material",
            "receiver_side_answerable_basis_reception_boundary_checks",
            "receiver_side_answerable_basis_reception_boundary_statement",
            "receiver_side_answerable_basis_reception_boundary_non_meaning",
            "boundary_result_detail",
            "permitted_future_route",
            "blocked_routes",
            "what_remains_open",
            "non_claims",
            "outcome",
            "block",
            "receiver_side_answerable_basis_reception_boundary_summary",
        }
        self.assertTrue(expected_sections.issubset(result))
        self.assertEqual(result["result_version"], resolver.RESULT_VERSION)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["boundary_result_detail"]["missing_or_insufficient_presence_waiting_basis"], [])

    def test_03_boundary_material_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
        material = result["receiver_side_answerable_basis_reception_boundary_material"]
        self.assertEqual(
            set(material),
            {
                "prior_presence_operation_reference",
                "receiver_side_answerable_basis_reception_boundary_reference",
                "receiver_side_answerable_basis_reception_boundary_evaluation",
            },
        )
        prior = material["prior_presence_operation_reference"]
        self.assertEqual(prior["prior_presence_operation_type"], resolver.PRIOR_PRESENCE_OPERATION_TYPE)
        self.assertEqual(prior["prior_presence_operation_outcome"], resolver.PRIOR_PRESENCE_OPERATION_OUTCOME_REQUIRED)
        self.assertEqual(prior["prior_presence_result"], resolver.PRIOR_PRESENCE_RESULT_REQUIRED)
        self.assertIs(prior["prior_presence_operation_recorded"], True)
        self.assertIs(prior["prior_presence_supported"], False)
        self.assertIs(prior["prior_receiver_answerable_basis_custody_distinct"], False)
        reference = material["receiver_side_answerable_basis_reception_boundary_reference"]
        self.assertEqual(reference["receiver_side_answerable_basis_reception_boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(reference["receiver_side_answerable_basis_reception_boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(reference["receiver_side_answerable_basis_reception_boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(reference["receiver_side_answerable_basis_reception_boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(reference["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        evaluation = material["receiver_side_answerable_basis_reception_boundary_evaluation"]
        for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS[2:]:
            self.assertIs(evaluation[key], True)
        for key in self.FALSE_BOUNDARY_FIELDS:
            if key in evaluation:
                self.assertIs(evaluation[key], False, key)

    def test_04_default_live_repo_target_if_present(self) -> None:
        request = resolver.build_receiver_side_answerable_basis_reception_boundary_v0_min_request()
        required_paths = [
            request["target_boundary_spec_path"],
            request["presence_operation_terminal_summary_path"],
            request["presence_boundary_terminal_summary_path"],
            request["relation_lapse_operation_terminal_summary_path"],
            request["existence_claim_evidence_check_terminal_summary_path"],
        ]
        if not all(Path(path).is_file() for path in required_paths):
            self.skipTest("required default target or upstream terminal summary is absent")
        result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
        self.assert_allowed_boundary(result)
        self.assertTrue(all(all(values.values()) for values in result["upstream_basis"].get("upstream_marker_classes", {}).values()))

    def test_05_missing_or_corrupt_upstream_basis_is_not_allowed(self) -> None:
        cases = (
            ("presence_missing", "presence_operation_terminal_summary_path", None, None),
            (
                "presence_outcome",
                "presence_operation_terminal_summary_path",
                "PRESENCE_OPERATION_REQUIRES_RECEIVER_ATTESTATION",
                "PRESENCE_OPERATION_WRONG",
            ),
            (
                "presence_boundary",
                "presence_boundary_terminal_summary_path",
                "PRESENCE_BOUNDARY_ALLOWED",
                "PRESENCE_BOUNDARY_WRONG",
            ),
            (
                "relation_lapse",
                "relation_lapse_operation_terminal_summary_path",
                "RELATION_LAPSE_OPERATION_RECORDED",
                "RELATION_LAPSE_WRONG",
            ),
            ("existence", "existence_claim_evidence_check_terminal_summary_path", "UNSUPPORTED", "NOT_SUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for index, (name, path_key, marker, replacement) in enumerate(cases):
                with self.subTest(name=name):
                    request, paths = self.build_valid_synthetic_request(base / name)
                    if replacement is None:
                        request[path_key] = str(base / "missing" / self.safe_json_filename(name, index))
                    else:
                        path = paths[path_key]
                        path.write_text(path.read_text(encoding="utf-8").replace(marker, replacement), encoding="utf-8")
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS, resolver.OUTCOME_BLOCKED),
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_with_public_code(result)
                    else:
                        self.assert_requires_not_blocked(result)
                        self.assert_canonical_non_claims(result)
                    self.assert_final_false_posture(result)

    def test_06_do_not_record_and_explicit_block_intents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            not_recorded_request = copy.deepcopy(request)
            not_recorded_request["intent"] = resolver.INTENT_DO_NOT_RECORD
            not_recorded = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(not_recorded_request)
            self.assertEqual(not_recorded["outcome"], resolver.OUTCOME_NOT_RECORDED)
            self.assertIs(not_recorded["block"]["blocked"], False)
            for key in resolver.ALLOWED_TRUE_ALLOWED_FIELDS:
                self.assertIs(self.boundary(not_recorded)[key], False, key)
            self.assert_final_false_posture(not_recorded)
            blocked_request = copy.deepcopy(request)
            blocked_request["intent"] = resolver.INTENT_BLOCK
            blocked = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(blocked_request)
        self.assert_blocked_with_public_code(blocked)
        self.assertEqual(self.block_code(blocked), "EXPLICIT_BLOCK_REQUESTED")
        self.assert_final_false_posture(blocked)

    def test_07_request_shape_and_exact_value_blocking(self) -> None:
        self.assert_blocked_with_public_code(
            resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(["not", "a", "mapping"])
        )
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            cases: dict[str, Any] = {
                "unsupported_intent": "UNSUPPORTED",
                "boundary_id": "wrong-boundary",
                "boundary_type": "WRONG",
                "boundary_version": "9.9.9",
                "boundary_scope": "WRONG_SCOPE",
                "prior_presence_operation_type": "WRONG",
                "prior_presence_operation_outcome_required": "WRONG",
                "prior_presence_result_required": "WRONG",
                "prior_presence_operation_recorded_required": False,
                "prior_presence_supported_required": True,
                "prior_receiver_attested_required": True,
                "prior_operator_only_attestation_admissible_required": True,
                "admissible_future_route": "WRONG_ROUTE",
            }
            for name, value in cases.items():
                with self.subTest(name=name):
                    altered = copy.deepcopy(request)
                    if name == "unsupported_intent":
                        altered["intent"] = value
                    else:
                        altered[name] = value
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(altered)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_false_posture(result)

    def test_08_marker_validation_behavior(self) -> None:
        cases = (
            ("target_spec", "target_boundary_spec_path", "Receiver-Side Answerable Basis Reception Boundary V0 Minimum Specification"),
            ("presence_operation", "presence_operation_terminal_summary_path", "receiver_attestation_required = true"),
            ("presence_boundary", "presence_boundary_terminal_summary_path", "PRESENCE_BOUNDARY_ALLOWED"),
            ("relation_lapse", "relation_lapse_operation_terminal_summary_path", "RELATION_LAPSE_SUPPORTED"),
            ("existence", "existence_claim_evidence_check_terminal_summary_path", "UNSUPPORTED"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            for name, path_key, marker in cases:
                with self.subTest(name=name):
                    request, paths = self.build_valid_synthetic_request(base / name)
                    path = paths[path_key]
                    path.write_text(path.read_text(encoding="utf-8").replace(marker, "BROKEN_MARKER"), encoding="utf-8")
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
                    self.assertIn(
                        result["outcome"],
                        (resolver.OUTCOME_REQUIRES_PRESENCE_WAITING_BASIS, resolver.OUTCOME_BLOCKED),
                    )
                    if result["outcome"] == resolver.OUTCOME_BLOCKED:
                        self.assert_blocked_with_public_code(result)
                    else:
                        self.assert_requires_not_blocked(result)
                    self.assert_final_false_posture(result)

    def test_09_prohibited_request_flags_block(self) -> None:
        expected_flags = (
            "request_receiver_side_answerable_basis_candidate_reception",
            "request_receiver_side_answerable_basis_candidate_recording",
            "request_receiver_side_answerable_basis_candidate_evaluation",
            "request_receiver_attestation_creation",
            "request_receiver_attestation_support",
            "request_receiver_answerable_receipt_creation",
            "request_custody_distinctness_decision",
            "request_refusability_decision",
            "request_could_have_been_withheld_decision",
            "request_presence_support",
            "request_presence_authorization",
            "request_presence_establishment",
            "request_presence_recording",
            "request_identity_creation",
            "request_relation_creation",
            "request_coupling_assignment",
            "request_coupling_creation",
            "request_field_machinery_creation",
            "request_runtime_creation",
            "request_api_creation",
            "request_public_interface_creation",
            "request_public_intake_creation",
            "request_mailbox_creation",
            "request_listener_creation",
            "request_queue_creation",
            "request_endpoint_creation",
            "request_shared_intake_lane_creation",
            "request_reusable_route_creation",
            "request_repeated_reception_permission_creation",
            "request_currentness_creation",
            "request_authority_creation",
            "request_standing_creation",
            "request_truth_creation",
            "request_continuity_memory_write",
            "request_output_authorization",
            "request_action_authorization",
            "request_derivative_reception_authorization",
            "request_synchronization_authorization",
            "request_follow_on_authorization",
            "request_follow_on_work_authorization",
            "request_repository_scan",
            "request_file_discovery",
            "request_affected_file_repair",
            "request_affected_file_mutation",
            "request_prior_unsupported_claim_validation",
            "request_validation_enforcement",
        )
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for flag in expected_flags:
                with self.subTest(flag=flag):
                    self.assertIn(flag, resolver.PROHIBITED_REQUEST_FLAGS)
                    altered = copy.deepcopy(request)
                    altered[flag] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(altered)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_false_posture(result)
                    if flag in ("request_follow_on_authorization", "request_follow_on_work_authorization"):
                        self.assertEqual(self.block_code(result), "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED")

    def test_10_required_false_posture_and_non_claim_canonicalization(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(top_level=key):
                    altered = copy.deepcopy(request)
                    altered[key] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(altered)
                    self.assert_blocked_with_public_code(result)
                    self.assert_final_false_posture(result)
            for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
                with self.subTest(non_claim=key):
                    altered = copy.deepcopy(request)
                    altered["declared_non_claims"][key] = True
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(altered)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_final_false_posture(result)
            for name, value in (
                ("missing", None),
                ("non_mapping", []),
                ("missing_key", {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS[1:]}),
                ("non_bool", {**request["declared_non_claims"], resolver.REQUIRED_FALSE_NON_CLAIMS[0]: "false"}),
            ):
                with self.subTest(declared_non_claims=name):
                    altered = copy.deepcopy(request)
                    if name == "missing":
                        altered.pop("declared_non_claims")
                    else:
                        altered["declared_non_claims"] = value
                    result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(altered)
                    self.assert_blocked_with_public_code(result)
                    self.assertEqual(self.block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")
                    self.assert_final_false_posture(result)

    def test_11_path_write_and_non_mutation_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            request, paths = self.build_valid_synthetic_request(base / "basis")
            original_request = copy.deepcopy(request)
            original_texts = {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
            request_path = base / "request" / self.safe_json_filename("valid request")
            request_path.parent.mkdir(parents=True, exist_ok=True)
            request_path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min_from_path(request_path)
            self.assert_allowed_boundary(result)
            self.assertEqual(request, original_request)
            self.assertEqual({key: path.read_text(encoding="utf-8") for key, path in paths.items()}, original_texts)
            malformed = base / "request" / self.safe_json_filename("malformed")
            malformed.write_text("{", encoding="utf-8")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min_from_path(malformed)
            )
            array_path = base / "request" / self.safe_json_filename("array")
            array_path.write_text("[]", encoding="utf-8")
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min_from_path(array_path)
            )
            self.assert_blocked_with_public_code(
                resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min_from_path(
                    base / "request" / self.safe_json_filename("missing")
                )
            )
            output = resolver.write_receiver_side_answerable_basis_reception_boundary_v0_min_result(
                result, base / "output" / resolver.OUTPUT_FILENAME
            )
            output_second = resolver.write_receiver_side_answerable_basis_reception_boundary_v0_min_result(
                result, base / "output" / resolver.OUTPUT_FILENAME
            )
            self.assertTrue(output.exists())
            self.assertTrue(output_second.exists())
            self.assertNotEqual(output, output_second)
            self.assertIn("receiver_side_answerable_basis_reception_boundary_v0_min_result", output.name)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertIn(
                "integrity_host_v0_min_coexistence_receiver_side_answerable_basis_reception_boundary_v0_min",
                str(resolver.OUTPUT_ROOT),
            )

    def test_12_summary_and_direct_smoke_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            original = copy.deepcopy(request)
            result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
        summary = resolver.build_receiver_side_answerable_basis_reception_boundary_v0_min_summary(result)
        self.assertEqual(request, original)
        self.assertEqual(summary["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["result_version"], "0.1.0")
        self.assertEqual(summary["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(summary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(summary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(summary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(summary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            summary["receiver_side_answerable_basis_reception_boundary_result"],
            "RECEIVER_SIDE_ANSWERABLE_BASIS_CANDIDATE_RECEPTION_CONSIDERATION_ALLOWED",
        )
        self.assertIs(summary["receiver_side_answerable_basis_candidate_reception_consideration_allowed"], True)
        self.assertIs(summary["prior_presence_operation_referenced"], True)
        self.assertIs(summary["presence_requires_receiver_attestation_referenced"], True)
        self.assertIs(summary["receiver_answerable_basis_requirement_referenced"], True)
        self.assertEqual(summary["missing_or_insufficient_presence_waiting_basis"], [])
        for key in self.FALSE_BOUNDARY_FIELDS:
            self.assertIs(summary[key], False, key)

    def test_13_missing_presence_summary_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            request, _ = self.build_valid_synthetic_request(Path(temporary))
            request["presence_operation_terminal_summary_path"] = str(Path(temporary) / "missing.md")
            result = resolver.resolve_receiver_side_answerable_basis_reception_boundary_v0_min(request)
        self.assert_requires_not_blocked(result)
        summary = self.summary(result)
        self.assertTrue(summary["missing_or_insufficient_presence_waiting_basis"])
        self.assertIs(summary["receiver_side_answerable_basis_candidate_reception_consideration_allowed"], False)
        self.assert_final_false_posture(result)


if __name__ == "__main__":
    unittest.main()
