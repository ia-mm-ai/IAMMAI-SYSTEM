"""Tests for bounded carrier-local emission admission boundary resolution.

This suite audits one admission boundary resolver. It verifies that emission,
return, and admission remain separate states, and that one carrier-local
emission may enter the body line only as downstream evidence without becoming
source, currentness, authority, permission, successor, body, signal, presence,
threshold, truth, action, consequence, multi-carrier law, distributed standing,
or continuation.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_carrier_local_emission_admission_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "carrier_local_emission_admission_metadata",
    "declared_admission_question",
    "selected_carrier_emission",
    "carrier_role_basis",
    "emission_basis",
    "return_basis",
    "admission_basis",
    "admission_checks",
    "admission_statement",
    "admission_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "carrier_local_emission_admission_summary",
}

EXPECTED_CHECK_NAMES = {
    "declared_admission_request_is_parseable_mapping",
    "carrier_local_emission_exists",
    "carrier_local_emission_is_mapping",
    "emission_identity_exists",
    "emission_outcome_exists",
    "emitting_carrier_exists",
    "carrier_role_exists",
    "carrier_role_is_bounded",
    "emission_class_exists",
    "emission_class_admissible",
    "admission_purpose_declared",
    "admission_intent_declared",
    "emission_not_self_admitted",
    "return_not_mistaken_for_admission",
    "possession_not_mistaken_for_admission",
    "receipt_not_mistaken_for_admission",
    "correspondence_not_mistaken_for_admission",
    "self_orientation_recognition_not_mistaken_for_admission",
    "source_not_replaced",
    "currentness_not_created",
    "authority_not_created",
    "permission_not_created",
    "successor_not_created",
    "body_not_created",
    "signal_not_created_by_default",
    "presence_not_established",
    "threshold_not_met",
    "truth_not_created",
    "action_not_authorized",
    "consequence_not_created",
    "multi_carrier_law_not_created",
    "distributed_standing_not_created",
    "continuation_not_authorized",
    "refusal_not_hidden",
    "divergence_not_hidden",
    "mutation_replay_merge_not_performed",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "non_claims_remain_false",
}

ADMISSION_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_emission",
    "does_not_mean_return",
    "does_not_mean_possession",
    "does_not_mean_receipt",
    "does_not_mean_correspondence",
    "does_not_mean_self_orientation_recognition",
    "does_not_mean_currentness",
    "does_not_mean_source",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor",
    "does_not_mean_body",
    "does_not_mean_carrier_participation_by_default",
    "does_not_mean_carrier_relation",
    "does_not_mean_multi_carrier_law",
    "does_not_mean_distributed_standing",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
    "does_not_mean_self_orientation_successor",
    "does_not_mean_conformance_successor",
}

OPEN_SURFACES = {
    "carrier-local emission admission implementation refinement",
    "cross-carrier divergence boundary",
    "cross-carrier currentness boundary",
    "multi-carrier relation law",
    "multi-carrier relation conformance",
    "multi-carrier relation closure",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
}

OUTCOME_FAMILY = {
    "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
    "CARRIER_LOCAL_EMISSION_NOT_ADMITTED",
    "CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED",
}


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert isinstance(loaded, dict)
    return loaded


def _false_non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _source_or_carried_basis() -> dict[str, object]:
    return {
        "basis_id": "source-carried-basis-001",
        "basis_outcome": "CONFORMANCE_CLOSURE_RECORDED",
        "basis_posture": "carrier_local_emission_source_basis_only",
    }


def _packet_or_surface() -> dict[str, object]:
    return {
        "selected_packet_or_surface_id": "selected-surface-001",
        "selected_packet_or_surface_outcome": "CONFORMANCE_CLOSURE_RECORDED",
        "selected_packet_or_surface_posture": "downstream_evidence_basis_only",
    }


def _receipt_or_refusal() -> dict[str, object]:
    return {
        "selected_receipt_or_refusal_id": "receipt-evidence-001",
        "selected_receipt_or_refusal_outcome": "CARRIED_SURFACE_RECEIVED",
        "visible_refusal_preserved": True,
    }


def _request(
    *,
    admission_request_id: str = "admission-request-001",
    admission_purpose: object = (
        "Admit one carrier-local receipt emission as downstream evidence only."
    ),
    admission_intent: object | None = "ADMIT_AS_EVIDENCE",
    emission_id: str | None = "carrier-emission-001",
    emission_outcome: str | None = "CARRIED_SURFACE_RECEIVED",
    emitting_carrier_id: str | None = "receiving-carrier-001",
    carrier_role: str | None = "RECEIVING_CARRIER",
    emission_class: str | None = "CARRIED_SURFACE_RECEIPT",
    emission_state: str | None = "RETURNED_TO_BODY_LINE",
    include_return: bool = True,
    return_path: str = "returned/carrier-emission-001.json",
    non_claims: dict[str, bool] | None = None,
    selected_emission: object | None = None,
    include_selected_emission: bool = True,
    include_source_basis: bool = True,
    include_selected_packet: bool = True,
    include_selected_receipt: bool = True,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    if selected_emission is None:
        selected: dict[str, object] = {}
        if emission_id is not None:
            selected["emission_id"] = emission_id
        if emission_outcome is not None:
            selected["emission_outcome"] = emission_outcome
        if emitting_carrier_id is not None:
            selected["emitting_carrier_id"] = emitting_carrier_id
        if carrier_role is not None:
            selected["carrier_role"] = carrier_role
        if emission_class is not None:
            selected["emission_class"] = emission_class
        if emission_state is not None:
            selected["emission_state"] = emission_state
        selected_emission = selected

    request: dict[str, object] = {
        "admission_request_id": admission_request_id,
        "declared_admission_question": (
            "May this carrier-local emission be admitted as body-line evidence?"
        ),
        "declared_scope": "carrier_local_emission_admission_boundary_test",
        "admission_purpose": admission_purpose,
        "carrier_role_basis": {
            "carrier_role": carrier_role,
            "carrier_role_bounded": carrier_role in resolver.ADMITTED_CARRIER_ROLES,
        },
        "emission_basis": {
            "emission_class": emission_class,
            "emission_class_admissible": (
                emission_class in resolver.ADMISSIBLE_EMISSION_CLASSES
            ),
        },
        "integrity_evidence": {
            "hash_algorithm": "sha256",
            "hash": "0" * 64,
            "integrity_posture": "preserved_where_supplied",
        },
        "declared_non_claims": copy.deepcopy(
            non_claims if non_claims is not None else _false_non_claims()
        ),
    }
    if include_selected_emission:
        request["selected_carrier_emission"] = copy.deepcopy(selected_emission)
    if admission_intent is not None:
        request["admission_intent"] = admission_intent
    if include_return:
        request["return_path"] = return_path
        request["return_basis"] = {
            "return_path": return_path,
            "return_context": {
                "returned_by": "returning-carrier-001",
                "return_posture": "returned_to_body_line_not_admitted_by_default",
            },
            "return_does_not_self_admit": True,
        }
    if include_source_basis:
        request["source_or_carried_basis"] = _source_or_carried_basis()
    if include_selected_packet:
        request["selected_packet_or_surface"] = _packet_or_surface()
    if include_selected_receipt:
        request["selected_receipt_or_refusal"] = _receipt_or_refusal()
    if extra:
        request.update(copy.deepcopy(extra))
    return request


class CarrierLocalEmissionAdmissionBoundaryTests(unittest.TestCase):
    def assertBlocked(self, result: dict, code: str) -> None:
        self.assertEqual("CARRIER_LOCAL_EMISSION_ADMISSION_BLOCKED", result["outcome"])
        self.assertEqual(code, result["block"]["code"])

    def assertTopLevelShape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))

    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertNonClaimsFalse(self, result: dict) -> None:
        for key in resolver.REQUIRED_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def assertChecksWellFormed(self, result: dict) -> None:
        for check in result["admission_checks"]:
            with self.subTest(check=check.get("check_name")):
                self.assertIn("check_name", check)
                self.assertIn("passed", check)
                self.assertIn("expected_posture", check)
                self.assertIn("actual_posture", check)
                self.assertIn("block_code", check)

    def assertNoCollapseSummary(self, summary: dict) -> None:
        collapse_keys = (
            "source_created",
            "currentness_created",
            "authority_created",
            "permission_created",
            "successor_created",
            "body_created",
            "signal_created_by_default",
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "multi_carrier_law_created",
            "distributed_standing_created",
            "continuation_authorized",
            "refusal_hidden",
            "divergence_hidden",
        )
        for key in collapse_keys:
            with self.subTest(summary_key=key):
                self.assertIs(summary[key], False)

    def _admitted_result(self) -> dict:
        return resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request()
        )

    def test_successful_admission_as_evidence(self) -> None:
        result = self._admitted_result()

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertOutcomeFamily(result)
        self.assertEqual(
            "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
            result["outcome"],
        )
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])

        statement = result["admission_statement"]
        self.assertIs(statement["carrier_local_emission_admitted_as_evidence"], True)
        self.assertIs(statement["admitted_evidence_remains_downstream"], True)
        self.assertIs(statement["source_not_replaced"], True)
        self.assertIs(statement["currentness_not_created"], True)
        self.assertIs(statement["authority_not_created"], True)
        self.assertIs(statement["permission_not_created"], True)
        self.assertIs(statement["multi_carrier_law_not_created"], True)
        self.assertIs(statement["distributed_standing_not_created"], True)
        self.assertIs(statement["continuation_not_authorized"], True)

    def test_metadata(self) -> None:
        metadata = self._admitted_result()["carrier_local_emission_admission_metadata"]

        self.assertTrue(metadata["carrier_local_emission_admission_result_id"])
        self.assertTrue(metadata["carrier_local_emission_admission_result_type"])
        self.assertEqual(
            "0.1.0",
            metadata["carrier_local_emission_admission_result_version"],
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            "resolve_carrier_local_emission_admission_boundary",
            metadata["resolver_module"],
        )

    def test_declared_question_and_selected_emission_are_preserved(self) -> None:
        result = self._admitted_result()
        question = result["declared_admission_question"]
        selected = result["selected_carrier_emission"]

        self.assertEqual("admission-request-001", question["admission_request_id"])
        self.assertEqual(
            "May this carrier-local emission be admitted as body-line evidence?",
            question["declared_admission_question"],
        )
        self.assertEqual(
            "Admit one carrier-local receipt emission as downstream evidence only.",
            question["admission_purpose"],
        )
        self.assertEqual("ADMIT_AS_EVIDENCE", question["admission_intent"])
        self.assertEqual("carrier-emission-001", question["selected_emission_reference"])
        self.assertEqual("receiving-carrier-001", question["selected_carrier_reference"])
        self.assertEqual(
            "carrier_local_emission_admission_boundary_test",
            question["declared_scope"],
        )
        self.assertIsInstance(question["declared_non_claims"], dict)

        self.assertEqual("carrier-emission-001", selected["emission_id"])
        self.assertEqual("CARRIED_SURFACE_RECEIVED", selected["emission_outcome"])
        self.assertEqual("receiving-carrier-001", selected["emitting_carrier_id"])
        self.assertEqual("RECEIVING_CARRIER", selected["carrier_role"])
        self.assertEqual("CARRIED_SURFACE_RECEIPT", selected["emission_class"])
        self.assertEqual("RETURNED_TO_BODY_LINE", selected["emission_state"])
        self.assertEqual(_source_or_carried_basis(), selected["source_or_carried_basis"])
        self.assertEqual(_packet_or_surface(), selected["selected_packet_or_surface"])
        self.assertEqual(_receipt_or_refusal(), selected["selected_receipt_or_refusal"])

    def test_basis_sections_preserve_bounded_posture(self) -> None:
        result = self._admitted_result()
        role_basis = result["carrier_role_basis"]
        emission_basis = result["emission_basis"]
        return_basis = result["return_basis"]
        admission_basis = result["admission_basis"]

        self.assertEqual("RECEIVING_CARRIER", role_basis["carrier_role"])
        self.assertIs(role_basis["carrier_role_declared"], True)
        self.assertIs(role_basis["carrier_role_bounded"], True)
        self.assertIn("RECEIVING_CARRIER", role_basis["admitted_carrier_roles"])
        self.assertEqual("RECEIVING_CARRIER", role_basis["selected_emission_carrier_role"])
        self.assertIs(
            role_basis[
                "role_does_not_create_source_currentness_authority_permission_successor_body"
            ],
            True,
        )

        self.assertEqual("CARRIED_SURFACE_RECEIPT", emission_basis["emission_class"])
        self.assertIs(emission_basis["emission_class_declared"], True)
        self.assertIs(emission_basis["emission_class_admissible"], True)
        self.assertIn(
            "SELF_ORIENTATION",
            emission_basis["not_admitted_emission_classes"],
        )
        self.assertEqual(
            "requires_declared_admission_boundary",
            emission_basis["body_line_admission_status"],
        )
        self.assertIs(
            emission_basis["emission_may_be_admitted_only_as_evidence"],
            True,
        )
        self.assertEqual(
            _packet_or_surface(),
            emission_basis["selected_packet_or_surface"],
        )
        self.assertEqual(
            _source_or_carried_basis(),
            emission_basis["source_or_carried_basis"],
        )

        self.assertIs(return_basis["return_basis_available"], True)
        self.assertEqual("returned/carrier-emission-001.json", return_basis["return_path"])
        self.assertEqual(
            "returned_to_body_line_not_admitted_by_default",
            return_basis["return_context"]["return_posture"],
        )
        self.assertIs(return_basis["return_does_not_self_admit"], True)
        self.assertIs(
            return_basis["returned_to_body_line_is_not_admitted_by_default"],
            True,
        )

        self.assertEqual(
            "Admit one carrier-local receipt emission as downstream evidence only.",
            admission_basis["admission_purpose"],
        )
        self.assertEqual("ADMIT_AS_EVIDENCE", admission_basis["admission_intent"])
        self.assertIs(admission_basis["positive_admission_requested"], True)
        self.assertIs(admission_basis["emitted_local_state_preserved"], False)
        self.assertIs(admission_basis["returned_to_body_line_state_preserved"], True)
        self.assertIs(admission_basis["admitted_as_evidence_state_requested"], True)
        self.assertIs(admission_basis["admission_is_not_currentness"], True)
        self.assertIsInstance(admission_basis["admission_non_claims"], dict)

    def test_admission_statement_preserves_distinction_and_non_collapse(self) -> None:
        statement = self._admitted_result()["admission_statement"]
        distinction = statement["emission_return_admission_distinction"]

        self.assertIs(distinction["emitted_local"], False)
        self.assertIs(distinction["returned_to_body_line"], True)
        self.assertIs(distinction["admitted_as_evidence"], True)
        self.assertIs(distinction["not_admitted"], False)
        self.assertIs(distinction["admission_blocked"], False)
        self.assertIs(statement["emitting_carrier_identity_preserved"], True)
        self.assertIs(statement["carrier_role_preserved"], True)
        self.assertIs(statement["emission_class_preserved"], True)
        self.assertIs(statement["emission_identity_preserved"], True)
        self.assertIs(statement["emission_outcome_preserved"], True)
        self.assertIs(statement["return_basis_preserved"], True)
        self.assertIs(statement["source_not_replaced"], True)
        self.assertIs(statement["currentness_not_created"], True)
        self.assertIs(statement["authority_not_created"], True)
        self.assertIs(statement["permission_not_created"], True)
        self.assertIs(statement["successor_not_created"], True)
        self.assertIs(statement["body_not_created"], True)
        self.assertIs(statement["multi_carrier_law_not_created"], True)
        self.assertIs(statement["distributed_standing_not_created"], True)
        self.assertIs(
            statement["presence_threshold_truth_action_consequence_not_created"],
            True,
        )
        self.assertIs(statement["continuation_not_authorized"], True)
        self.assertIs(statement["refusal_not_hidden"], True)
        self.assertIs(statement["divergence_not_hidden"], True)

    def test_admission_non_meaning_and_open_surfaces(self) -> None:
        result = self._admitted_result()

        for key in ADMISSION_NON_MEANING_TRUE_KEYS:
            with self.subTest(non_meaning=key):
                self.assertIs(result["admission_non_meaning"][key], True)

        open_section = result["what_remains_open"]
        self.assertTrue(OPEN_SURFACES.issubset(set(open_section["open_surfaces"])))
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)

    def test_admission_checks_and_summary(self) -> None:
        result = self._admitted_result()
        self.assertChecksWellFormed(result)
        self.assertEqual(
            EXPECTED_CHECK_NAMES,
            {check["check_name"] for check in result["admission_checks"]},
        )
        self.assertEqual(
            0,
            sum(1 for check in result["admission_checks"] if check["passed"] is False),
        )
        self.assertTrue(all(check["passed"] is True for check in result["admission_checks"]))

        summary = resolver.build_carrier_local_emission_admission_summary(result)
        self.assertEqual(result["carrier_local_emission_admission_summary"], summary)
        self.assertEqual("CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("admission-request-001", summary["admission_request_id"])
        self.assertEqual(
            "Admit one carrier-local receipt emission as downstream evidence only.",
            summary["admission_purpose"],
        )
        self.assertEqual("ADMIT_AS_EVIDENCE", summary["admission_intent"])
        self.assertEqual("carrier-emission-001", summary["selected_emission_id"])
        self.assertEqual("CARRIED_SURFACE_RECEIVED", summary["selected_emission_outcome"])
        self.assertEqual("receiving-carrier-001", summary["emitting_carrier_id"])
        self.assertEqual("RECEIVING_CARRIER", summary["carrier_role"])
        self.assertEqual("CARRIED_SURFACE_RECEIPT", summary["emission_class"])
        self.assertEqual("returned/carrier-emission-001.json", summary["return_path"])
        self.assertIs(summary["admission_as_evidence"], True)
        self.assertIs(summary["not_admitted"], False)
        self.assertEqual(len(result["admission_checks"]), summary["passed_check_count"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertNoCollapseSummary(summary)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_are_false_for_all_outcomes(self) -> None:
        admitted = self._admitted_result()
        not_admitted = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(
                admission_intent="DO_NOT_ADMIT",
                emission_state="EMITTED_LOCAL",
                include_return=False,
            )
        )
        blocked = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(
                extra={"admission_creates_currentness": True}
            )
        )

        for result in (admitted, not_admitted, blocked):
            with self.subTest(outcome=result["outcome"]):
                self.assertOutcomeFamily(result)
                self.assertNonClaimsFalse(result)

    def test_not_admitted_emitted_local_only(self) -> None:
        result = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(
                admission_intent="EMITTED_LOCAL_ONLY",
                emission_state="EMITTED_LOCAL",
                include_return=False,
            )
        )

        self.assertEqual("CARRIER_LOCAL_EMISSION_NOT_ADMITTED", result["outcome"])
        statement = result["admission_statement"]
        self.assertIs(statement["carrier_local_emission_admitted_as_evidence"], False)
        self.assertIs(statement["carrier_local_emission_preserved_without_admission"], True)
        self.assertEqual(
            "emission_preserved_as_emitted_local_without_admission",
            statement["not_admitted_reason"],
        )
        self.assertIs(statement["emission_return_admission_distinction"]["emitted_local"], True)
        self.assertNoCollapseSummary(result["carrier_local_emission_admission_summary"])

    def test_not_admitted_returned_only(self) -> None:
        result = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(admission_intent="RETURNED_ONLY")
        )

        self.assertEqual("CARRIER_LOCAL_EMISSION_NOT_ADMITTED", result["outcome"])
        statement = result["admission_statement"]
        self.assertIs(statement["carrier_local_emission_admitted_as_evidence"], False)
        self.assertIs(statement["carrier_local_emission_preserved_without_admission"], True)
        self.assertEqual(
            "returned_emission_preserved_without_admission",
            statement["not_admitted_reason"],
        )
        self.assertIs(
            statement["emission_return_admission_distinction"]["returned_to_body_line"],
            True,
        )
        self.assertIs(result["return_basis"]["return_does_not_self_admit"], True)
        self.assertNoCollapseSummary(result["carrier_local_emission_admission_summary"])

    def test_admissible_emission_classes_admit_as_evidence(self) -> None:
        for emission_class in sorted(resolver.ADMISSIBLE_EMISSION_CLASSES):
            with self.subTest(emission_class=emission_class):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(emission_class=emission_class)
                )
                self.assertEqual(
                    "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
                    result["outcome"],
                )
                self.assertEqual(emission_class, result["emission_basis"]["emission_class"])

    def test_not_admitted_emission_classes_block(self) -> None:
        for emission_class in sorted(resolver.NOT_ADMITTED_EMISSION_CLASSES):
            with self.subTest(emission_class=emission_class):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(emission_class=emission_class)
                )
                self.assertBlocked(result, "EMISSION_CLASS_UNSUPPORTED")

    def test_builder_helper_creates_valid_admission_request(self) -> None:
        request = resolver.build_declared_admission_request(
            "builder-admission-001",
            "Admit one returned carrier-local receipt as evidence only.",
            "builder-emission-001",
            "CARRIED_SURFACE_RECEIVED",
            "receiving-carrier-001",
            "RECEIVING_CARRIER",
            "CARRIED_SURFACE_RECEIPT",
            return_path="returned/builder-emission-001.json",
            selected_basis=_source_or_carried_basis(),
        )

        self.assertEqual("builder-admission-001", request["admission_request_id"])
        selected = request["selected_carrier_emission"]
        self.assertEqual("builder-emission-001", selected["emission_id"])
        self.assertEqual("CARRIED_SURFACE_RECEIVED", selected["emission_outcome"])
        self.assertEqual("receiving-carrier-001", selected["emitting_carrier_id"])
        self.assertEqual("RECEIVING_CARRIER", selected["carrier_role"])
        self.assertEqual("CARRIED_SURFACE_RECEIPT", selected["emission_class"])
        self.assertEqual("ADMIT_AS_EVIDENCE", request["admission_intent"])
        self.assertEqual("returned/builder-emission-001.json", request["return_path"])
        for value in request["declared_non_claims"].values():
            self.assertIs(value, False)

        result = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=request
        )
        self.assertEqual("CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE", result["outcome"])

    def test_path_based_resolution(self) -> None:
        request = _request()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "request.json"
            _write_json(path, request)

            path_result = resolver.resolve_carrier_local_emission_admission_boundary_from_path(path)
            mapping_result = resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=request
            )

        self.assertEqual("CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE", path_result["outcome"])
        self.assertEqual(TOP_LEVEL_SECTIONS, set(path_result.keys()))
        self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))
        self.assertTrue(
            path_result["declared_admission_question"][
                "declared_admission_request_path"
            ].endswith("request.json")
        )

    def test_write_behavior_with_explicit_path(self) -> None:
        result = self._admitted_result()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "admission-result.json"
            written = resolver.write_carrier_local_emission_admission_result(
                result,
                output_path,
            )
            loaded = _read_json(written)

        self.assertEqual(output_path, written)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded.keys()))
        self.assertEqual("CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE", loaded["outcome"])

    def test_default_write_uses_bounded_root_and_does_not_overwrite(self) -> None:
        result = self._admitted_result()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "admission-root"
            with mock.patch.object(
                resolver,
                "CARRIER_LOCAL_EMISSION_ADMISSION_BOUNDARY_ROOT",
                root,
            ):
                first = resolver.write_carrier_local_emission_admission_result(result)
                second = resolver.write_carrier_local_emission_admission_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        request = _request()
        selected_before = copy.deepcopy(request["selected_carrier_emission"])
        request_before = copy.deepcopy(request)

        first = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=request
        )
        second = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=request
        )

        self.assertEqual(request_before, request)
        self.assertEqual(selected_before, request["selected_carrier_emission"])
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            resolver.write_carrier_local_emission_admission_result(first, output_path)
            self.assertEqual(request_before, request)
            self.assertTrue(output_path.exists())

    def test_blocking_missing_and_malformed_request(self) -> None:
        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(),
            "DECLARED_ADMISSION_REQUEST_MISSING",
        )
        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=["not", "a", "mapping"]  # type: ignore[arg-type]
            ),
            "DECLARED_ADMISSION_REQUEST_MALFORMED",
        )

    def test_blocking_unreadable_or_malformed_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing = root / "missing.json"
            malformed = root / "malformed.json"
            array = root / "array.json"
            malformed.write_text("{not-json", encoding="utf-8")
            _write_json(array, [])

            self.assertBlocked(
                resolver.resolve_carrier_local_emission_admission_boundary_from_path(missing),
                "DECLARED_ADMISSION_REQUEST_UNREADABLE",
            )
            self.assertBlocked(
                resolver.resolve_carrier_local_emission_admission_boundary_from_path(malformed),
                "DECLARED_ADMISSION_REQUEST_MALFORMED",
            )
            self.assertBlocked(
                resolver.resolve_carrier_local_emission_admission_boundary_from_path(array),
                "DECLARED_ADMISSION_REQUEST_MALFORMED",
            )

    def test_blocking_missing_or_malformed_selected_emission(self) -> None:
        missing = _request(include_selected_emission=False)
        malformed = _request(selected_emission=["not", "mapping"])

        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=missing
            ),
            "CARRIER_LOCAL_EMISSION_MISSING",
        )
        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=malformed
            ),
            "CARRIER_LOCAL_EMISSION_MALFORMED",
        )

    def test_blocking_required_identity_basis(self) -> None:
        cases = (
            ("EMISSION_IDENTITY_MISSING", {"emission_id": None}),
            ("EMISSION_OUTCOME_MISSING", {"emission_outcome": None}),
            ("EMITTING_CARRIER_MISSING", {"emitting_carrier_id": None}),
            ("CARRIER_ROLE_MISSING", {"carrier_role": None}),
            ("CARRIER_ROLE_UNSUPPORTED", {"carrier_role": "UNSUPPORTED_CARRIER"}),
            ("EMISSION_CLASS_MISSING", {"emission_class": None}),
            ("EMISSION_CLASS_UNSUPPORTED", {"emission_class": "UNSUPPORTED_EMISSION"}),
        )
        for expected_code, updates in cases:
            with self.subTest(block=expected_code):
                request = _request(**updates)
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=request
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_admission_purpose_and_intent(self) -> None:
        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=_request(admission_purpose="")
            ),
            "ADMISSION_PURPOSE_UNDECLARED",
        )
        self.assertBlocked(
            resolver.resolve_carrier_local_emission_admission_boundary(
                declared_admission_request=_request(
                    admission_intent=None,
                    emission_state=None,
                    include_return=False,
                )
            ),
            "ADMISSION_INTENT_UNDECLARED",
        )

    def test_blocking_emission_self_admits_and_mistaken_admission_sources(self) -> None:
        cases = (
            ("EMISSION_SELF_ADMITTED", "carrier_emission_self_admitted"),
            ("RETURN_MISTAKEN_FOR_ADMISSION", "return_mistaken_for_admission"),
            ("POSSESSION_MISTAKEN_FOR_ADMISSION", "possession_mistaken_for_admission"),
            ("RECEIPT_MISTAKEN_FOR_ADMISSION", "receipt_mistaken_for_admission"),
            (
                "CORRESPONDENCE_MISTAKEN_FOR_ADMISSION",
                "correspondence_mistaken_for_admission",
            ),
            (
                "SELF_ORIENTATION_RECOGNITION_MISTAKEN_FOR_ADMISSION",
                "self_orientation_recognition_mistaken_for_admission",
            ),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_source_currentness_authority_permission_successor_body_collapse(self) -> None:
        cases = (
            ("ADMISSION_REPLACES_SOURCE", "admission_replaces_source"),
            ("ADMISSION_CREATES_CURRENTNESS", "admission_creates_currentness"),
            ("ADMISSION_CREATES_AUTHORITY", "admission_creates_authority"),
            ("ADMISSION_CREATES_PERMISSION", "admission_creates_permission"),
            ("ADMISSION_CREATES_SUCCESSOR", "admission_creates_successor"),
            ("ADMISSION_CREATES_BODY", "admission_creates_body"),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_signal_presence_threshold_truth_action_consequence_collapse(self) -> None:
        cases = (
            ("ADMISSION_CREATES_SIGNAL_BY_DEFAULT", "admission_creates_signal_by_default"),
            ("ADMISSION_ESTABLISHES_PRESENCE", "admission_establishes_presence"),
            ("ADMISSION_ESTABLISHES_THRESHOLD", "admission_establishes_threshold"),
            ("ADMISSION_CREATES_TRUTH", "admission_creates_truth"),
            ("ADMISSION_AUTHORIZES_ACTION", "admission_authorizes_action"),
            ("ADMISSION_CREATES_CONSEQUENCE", "admission_creates_consequence"),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_multi_carrier_distributed_continuation_collapse(self) -> None:
        cases = (
            ("ADMISSION_CREATES_MULTI_CARRIER_LAW", "multi_carrier_law_created"),
            ("ADMISSION_CREATES_DISTRIBUTED_STANDING", "distributed_standing_created"),
            ("ADMISSION_AUTHORIZES_CONTINUATION", "continuation_authorized"),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_refusal_or_divergence_hidden(self) -> None:
        cases = (
            ("ADMISSION_HIDES_REFUSAL", "refusal_hidden"),
            ("ADMISSION_HIDES_DIVERGENCE", "divergence_hidden"),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_mutation_replay_merge_and_latest_file_currentness(self) -> None:
        cases = (
            ("ADMISSION_MUTATES_OR_REPLAYS_EMISSION", "mutation_performed"),
            ("ADMISSION_MUTATES_OR_REPLAYS_EMISSION", "replay_performed"),
            ("ADMISSION_MUTATES_OR_REPLAYS_EMISSION", "merge_performed"),
            ("LATEST_FILE_CURRENTNESS", "latest_file_currentness"),
            ("LATEST_FILE_CURRENTNESS", "recency_fraud"),
        )
        for expected_code, flag in cases:
            with self.subTest(flag=flag):
                result = resolver.resolve_carrier_local_emission_admission_boundary(
                    declared_admission_request=_request(extra={flag: True})
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        missing_non_claim = _false_non_claims()
        missing_non_claim.pop("authority_created")
        flipped_non_claim = _false_non_claims(authority_created=True)

        missing_result = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(non_claims=missing_non_claim)
        )
        flipped_result = resolver.resolve_carrier_local_emission_admission_boundary(
            declared_admission_request=_request(non_claims=flipped_non_claim)
        )

        self.assertBlocked(missing_result, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertBlocked(flipped_result, "ADMISSION_CREATES_AUTHORITY")
        for result in (missing_result, flipped_result):
            self.assertIn("non_claims", result)
            self.assertNonClaimsFalse(result)


if __name__ == "__main__":
    unittest.main()
