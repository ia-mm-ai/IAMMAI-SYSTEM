"""Tests for bounded cross-carrier currentness participation resolution.

This suite audits one currentness boundary resolver. It verifies that selected
carrier evidence may be marked eligible or excluded for later body-side current
posture assessment without becoming currentness, source, authority,
permission, successor, body, truth, action, carrier hierarchy,
multi-carrier law, distributed standing, or continuation.
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

import resolve_cross_carrier_currentness_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "cross_carrier_currentness_metadata",
    "declared_currentness_question",
    "selected_body_current_posture",
    "selected_carrier_evidence",
    "carrier_evidence_status",
    "currentness_basis",
    "currentness_checks",
    "currentness_participation_result",
    "currentness_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "cross_carrier_currentness_summary",
}

EXPECTED_CHECK_NAMES = {
    "declared_currentness_request_is_parseable_mapping",
    "currentness_question_declared",
    "selected_body_current_posture_declared",
    "participation_intent_supported",
    "selected_carrier_evidence_exists",
    "selected_carrier_evidence_parseable",
    "evidence_identity_present",
    "evidence_outcome_present",
    "carrier_identity_present_where_required",
    "admission_status_known_where_required",
    "admission_status_not_unknown_where_required",
    "divergence_status_known_where_required",
    "divergence_status_not_unknown_or_unresolved_where_required",
    "hidden_divergence_false",
    "refusal_hidden_false",
    "lineage_basis_preserved_where_supplied",
    "carrier_does_not_create_currentness",
    "carrier_evidence_does_not_become_current",
    "currentness_not_derived_from_carrier_emission",
    "currentness_not_derived_from_latest_file",
    "currentness_not_derived_from_newest_timestamp",
    "currentness_not_derived_from_local_copy",
    "currentness_not_derived_from_possession",
    "currentness_not_derived_from_return",
    "currentness_not_derived_from_receipt",
    "currentness_not_derived_from_admission",
    "currentness_not_derived_from_correspondence",
    "currentness_not_derived_from_divergence",
    "currentness_not_derived_from_majority_carriers",
    "currentness_not_derived_from_carrier_count",
    "currentness_not_derived_from_successful_receipt_count",
    "currentness_not_derived_from_successful_admission_count",
    "currentness_not_derived_from_carrier_availability",
    "currentness_not_derived_from_carrier_label",
    "currentness_not_derived_from_convenience",
    "no_winning_carrier_selected",
    "no_losing_carrier_invalidated",
    "no_carrier_hierarchy_created",
    "source_not_replaced",
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
    "carrier_relation_not_created",
    "multi_carrier_law_not_created",
    "distributed_standing_not_created",
    "continuation_not_authorized",
    "mutation_replay_merge_not_performed",
    "non_claims_remain_false",
}

CURRENTNESS_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_carrier_currentness",
    "does_not_mean_evidence_currentness",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor",
    "does_not_mean_body",
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
    "does_not_mean_winning_carrier",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_divergence_resolved",
    "does_not_mean_majority_rule",
    "does_not_mean_latest_file_rule",
    "does_not_mean_successful_receipt_count_rule",
    "does_not_mean_successful_admission_count_rule",
}

OPEN_SURFACES = {
    "cross-carrier currentness implementation refinement",
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
    "CURRENTNESS_PARTICIPATION_ELIGIBLE",
    "CURRENTNESS_PARTICIPATION_EXCLUDED",
    "CURRENTNESS_PARTICIPATION_BLOCKED",
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


def _body_posture(
    posture_id: str = "body-current-posture-001",
) -> dict[str, object]:
    return {
        "body_current_posture_id": posture_id,
        "body_current_posture_label": "v7-integrated-current-body-posture",
        "outcome": "CONFORMANCE_CLOSURE_RECORDED",
        "body_side_posture_declared": True,
        "body_side_current_posture_is_not_carrier_created": True,
    }


def _evidence(
    evidence_id: str = "carrier-currentness-evidence-001",
    *,
    outcome: str | None = "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
    carrier_id: str | None = "carrier-b",
    carrier_role: str = "RECEIVING_CARRIER",
    emission_class: str = "CARRIED_SURFACE_RECEIPT",
    admission_status: str | None = "ADMITTED_AS_EVIDENCE",
    correspondence_status: str | None = "CORRESPONDENCE_RECOGNIZED",
    divergence_status: str | None = "VISIBLE_DIVERGENCE_RECORDED",
    visible_divergence: bool = True,
    return_path: str = "returned/carrier-currentness-evidence-001.json",
    integrity_hash: str = "c" * 64,
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    evidence: dict[str, object] = {
        "evidence_id": evidence_id,
        "evidence_outcome": outcome,
        "carrier_id": carrier_id,
        "carrier_role": carrier_role,
        "emission_class": emission_class,
        "source_or_carried_basis": {
            "basis_id": "source-carried-basis-001",
            "basis_posture": "downstream_carried_evidence_only",
        },
        "admission_status": admission_status,
        "correspondence_status": correspondence_status,
        "divergence_status": divergence_status,
        "visible_divergence": visible_divergence,
        "return_path": return_path,
        "return_context": {
            "return_posture": "returned_to_body_line_not_currentness",
        },
        "integrity_evidence": {
            "hash_algorithm": "sha256",
            "hash": integrity_hash,
            "integrity_posture": "preserved_where_supplied",
        },
        "block_code": None,
        "block_reason": None,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if outcome is None:
        evidence.pop("evidence_outcome")
    if carrier_id is None:
        evidence.pop("carrier_id")
    if admission_status is None:
        evidence.pop("admission_status")
    if divergence_status is None:
        evidence.pop("divergence_status")
    if extra:
        evidence.update(copy.deepcopy(extra))
    return evidence


def _request(
    *,
    currentness_request_id: str = "currentness-request-001",
    currentness_question: object = (
        "May selected carrier evidence participate in body-side current posture?"
    ),
    participation_intent: object = "EVALUATE_PARTICIPATION",
    selected_body_current_posture: object | None = None,
    selected_carrier_evidence: object | None = None,
    include_body_posture: bool = True,
    include_evidence: bool = True,
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    if selected_body_current_posture is None:
        selected_body_current_posture = _body_posture()
    if selected_carrier_evidence is None:
        selected_carrier_evidence = [_evidence()]

    request: dict[str, object] = {
        "currentness_request_id": currentness_request_id,
        "currentness_question": currentness_question,
        "currentness_purpose": (
            "Evaluate carrier evidence for participation only, not currentness."
        ),
        "declared_scope": "cross_carrier_currentness_boundary_test",
        "participation_intent": participation_intent,
        "currentness_basis": {
            "currentness_basis_id": "currentness-basis-001",
            "admission_status_required": True,
            "divergence_status_required": True,
            "currentness_participation_is_not_currentness_creation": True,
        },
        "lineage_basis": {
            "lineage_basis_id": "lineage-basis-001",
            "lineage_preserved": True,
        },
        "selected_admission_basis": {
            "admission_status": "ADMITTED_AS_EVIDENCE",
            "admission_posture": "downstream_evidence_only",
        },
        "selected_correspondence_basis": {
            "correspondence_status": "CORRESPONDENCE_RECOGNIZED",
            "correspondence_posture": "not_currentness",
        },
        "selected_divergence_basis": {
            "divergence_status": "VISIBLE_DIVERGENCE_RECORDED",
            "visible_divergence": True,
            "divergence_posture": "visible_mismatch_not_resolution",
        },
        "declared_non_claims": copy.deepcopy(
            non_claims if non_claims is not None else _false_non_claims()
        ),
    }
    if include_body_posture:
        request["selected_body_current_posture"] = copy.deepcopy(
            selected_body_current_posture
        )
    if include_evidence:
        request["selected_carrier_evidence"] = copy.deepcopy(
            selected_carrier_evidence
        )
    if extra:
        request.update(copy.deepcopy(extra))
    return request


class CrossCarrierCurrentnessBoundaryTests(unittest.TestCase):
    def assertBlocked(self, result: dict, code: str) -> None:
        self.assertEqual("CURRENTNESS_PARTICIPATION_BLOCKED", result["outcome"])
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
        for check in result["currentness_checks"]:
            with self.subTest(check=check.get("check_name")):
                self.assertIn("check_name", check)
                self.assertIn("passed", check)
                self.assertIn("expected_posture", check)
                self.assertIn("actual_posture", check)
                self.assertIn("block_code", check)

    def assertSummaryNoCollapse(self, summary: dict) -> None:
        for key in (
            "carrier_evidence_became_current",
            "currentness_created_by_carrier",
            "source_created",
            "authority_created",
            "permission_created",
            "carrier_hierarchy_created",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "multi_carrier_law_created",
            "distributed_standing_created",
            "presence_created",
            "threshold_created",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "continuation_authorized",
        ):
            with self.subTest(summary_key=key):
                self.assertIs(summary[key], False)

    def _eligible_result(self) -> dict:
        return resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request()
        )

    def test_successful_currentness_participation_eligibility(self) -> None:
        result = self._eligible_result()

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertOutcomeFamily(result)
        self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])

        participation = result["currentness_participation_result"]
        self.assertIs(participation["currentness_participation_eligible"], True)
        self.assertIs(participation["selected_evidence_may_participate"], True)
        self.assertIs(participation["participation_is_not_currentness_creation"], True)
        self.assertIs(participation["carrier_evidence_became_current"], False)
        self.assertIs(participation["currentness_created_by_carrier"], False)

    def test_metadata_declared_question_and_body_posture(self) -> None:
        result = self._eligible_result()
        metadata = result["cross_carrier_currentness_metadata"]
        question = result["declared_currentness_question"]
        posture = result["selected_body_current_posture"]

        for key in (
            "cross_carrier_currentness_result_id",
            "cross_carrier_currentness_result_type",
            "cross_carrier_currentness_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["cross_carrier_currentness_result_version"])
        self.assertEqual(
            "resolve_cross_carrier_currentness_boundary",
            metadata["resolver_module"],
        )

        self.assertEqual("currentness-request-001", question["currentness_request_id"])
        self.assertEqual(
            "May selected carrier evidence participate in body-side current posture?",
            question["currentness_question"],
        )
        self.assertEqual(
            "Evaluate carrier evidence for participation only, not currentness.",
            question["currentness_purpose"],
        )
        self.assertEqual("EVALUATE_PARTICIPATION", question["participation_intent"])
        self.assertEqual(
            "cross_carrier_currentness_boundary_test",
            question["declared_scope"],
        )
        self.assertEqual(1, question["selected_evidence_count"])
        self.assertIsInstance(question["declared_non_claims"], dict)

        self.assertEqual("body-current-posture-001", posture["body_current_posture_id"])
        self.assertEqual(
            "v7-integrated-current-body-posture",
            posture["body_current_posture_label"],
        )
        self.assertEqual(
            "CONFORMANCE_CLOSURE_RECORDED",
            posture["body_current_posture_outcome"],
        )
        self.assertIs(posture["body_current_posture_declared"], True)
        self.assertIs(
            posture["raw_body_current_posture"][
                "body_side_current_posture_is_not_carrier_created"
            ],
            True,
        )

    def test_selected_evidence_status_and_currentness_basis(self) -> None:
        result = self._eligible_result()
        selected = result["selected_carrier_evidence"]
        status = result["carrier_evidence_status"]
        basis = result["currentness_basis"]

        self.assertEqual(1, len(selected))
        evidence = selected[0]
        self.assertEqual("carrier-currentness-evidence-001", evidence["evidence_id"])
        self.assertEqual(
            "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
            evidence["evidence_outcome"],
        )
        self.assertEqual("carrier-b", evidence["carrier_id"])
        self.assertEqual("RECEIVING_CARRIER", evidence["carrier_role"])
        self.assertEqual("CARRIED_SURFACE_RECEIPT", evidence["emission_class"])
        self.assertTrue(evidence["source_or_carried_basis"])
        self.assertEqual("ADMITTED_AS_EVIDENCE", evidence["admission_status"])
        self.assertEqual("CORRESPONDENCE_RECOGNIZED", evidence["correspondence_status"])
        self.assertEqual("VISIBLE_DIVERGENCE_RECORDED", evidence["divergence_status"])
        self.assertEqual(
            "returned/carrier-currentness-evidence-001.json",
            evidence["return_path"],
        )
        self.assertTrue(evidence["return_context"])
        self.assertEqual("c" * 64, evidence["integrity_hash"])
        self.assertIn("block_code", evidence)
        self.assertIn("block_reason", evidence)
        self.assertIsInstance(evidence["non_claims"], dict)

        self.assertEqual(1, status["selected_evidence_count"])
        self.assertEqual(
            ["carrier-currentness-evidence-001"],
            status["selected_evidence_ids"],
        )
        self.assertEqual(
            ["CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE"],
            status["selected_evidence_outcomes"],
        )
        self.assertEqual(["carrier-b"], status["selected_carrier_ids"])
        self.assertEqual(["ADMITTED_AS_EVIDENCE"], status["admission_statuses"])
        self.assertEqual(
            ["VISIBLE_DIVERGENCE_RECORDED"],
            status["divergence_statuses"],
        )
        self.assertIs(status["selected_evidence_remains_downstream"], True)
        self.assertIs(status["carrier_held_does_not_mean_current"], True)
        self.assertIs(status["carrier_admitted_as_evidence_does_not_mean_current"], True)

        self.assertEqual(
            "May selected carrier evidence participate in body-side current posture?",
            basis["currentness_question"],
        )
        self.assertIs(basis["selected_body_current_posture_declared"], True)
        self.assertEqual(
            ["carrier-currentness-evidence-001"],
            basis["selected_evidence_ids"],
        )
        self.assertEqual(["carrier-b"], basis["selected_carrier_ids"])
        self.assertIs(basis["admission_status_required"], True)
        self.assertIs(basis["divergence_status_required"], True)
        self.assertEqual(["ADMITTED_AS_EVIDENCE"], basis["admission_statuses"])
        self.assertEqual(
            ["VISIBLE_DIVERGENCE_RECORDED"],
            basis["divergence_statuses"],
        )
        self.assertIs(basis["hidden_divergence"], False)
        self.assertIs(basis["refusal_hidden"], False)
        for key in (
            "latest_file",
            "newest_timestamp",
            "local_copy",
            "possession",
            "return",
            "receipt",
            "admission",
            "correspondence",
            "divergence",
            "majority_carriers",
            "successful_receipt_count",
            "successful_admission_count",
            "carrier_availability",
            "carrier_label",
        ):
            with self.subTest(currentness_not_derived_from=key):
                self.assertIs(basis["currentness_not_derived_from"][key], True)

    def test_checks_participation_result_non_meaning_open_and_summary(self) -> None:
        result = self._eligible_result()
        self.assertChecksWellFormed(result)

        check_names = {check["check_name"] for check in result["currentness_checks"]}
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(check_names))
        self.assertEqual(
            0,
            sum(1 for check in result["currentness_checks"] if check["passed"] is False),
        )
        self.assertTrue(all(check["passed"] for check in result["currentness_checks"]))

        participation = result["currentness_participation_result"]
        self.assertIs(participation["currentness_participation_eligible"], True)
        self.assertIs(participation["selected_evidence_may_participate"], True)
        self.assertIs(participation["participation_is_not_currentness_creation"], True)
        self.assertIs(participation["body_side_current_posture_declared"], True)
        self.assertIs(participation["selected_carrier_evidence_preserved"], True)
        self.assertIs(participation["selected_evidence_remains_downstream"], True)
        self.assertIs(participation["admission_status_preserved"], True)
        self.assertIs(participation["correspondence_status_preserved"], True)
        self.assertIs(participation["divergence_status_preserved"], True)
        self.assertIs(participation["visible_divergence_preserved"], True)
        self.assertIs(participation["hidden_divergence"], False)
        self.assertIs(participation["carrier_evidence_became_current"], False)
        self.assertIs(participation["currentness_created_by_carrier"], False)
        self.assertIs(participation["source_not_replaced"], True)
        self.assertIs(participation["authority_not_created"], True)
        self.assertIs(participation["permission_not_created"], True)
        self.assertIs(participation["successor_not_created"], True)
        self.assertIs(participation["body_not_created"], True)
        self.assertIs(participation["carrier_hierarchy_not_created"], True)
        self.assertIs(participation["winning_carrier_selected"], False)
        self.assertIs(participation["losing_carrier_invalidated"], False)
        self.assertIs(participation["multi_carrier_law_not_created"], True)
        self.assertIs(participation["distributed_standing_not_created"], True)
        self.assertIs(
            participation["presence_threshold_truth_action_consequence_not_created"],
            True,
        )
        self.assertIs(participation["continuation_not_authorized"], True)

        for key in CURRENTNESS_NON_MEANING_TRUE_KEYS:
            with self.subTest(non_meaning=key):
                self.assertIs(result["currentness_non_meaning"][key], True)

        open_section = result["what_remains_open"]
        open_items = {item["item"] for item in open_section["open_items"]}
        self.assertTrue(OPEN_SURFACES.issubset(open_items))
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)
        for item in open_section["open_items"]:
            self.assertIs(item["scheduled"], False)
            self.assertIs(item["authorized"], False)
            self.assertIs(item["executed"], False)

        summary = resolver.build_cross_carrier_currentness_summary(result)
        self.assertEqual(result["cross_carrier_currentness_summary"], summary)
        self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("currentness-request-001", summary["currentness_request_id"])
        self.assertEqual(
            "May selected carrier evidence participate in body-side current posture?",
            summary["currentness_question"],
        )
        self.assertEqual("EVALUATE_PARTICIPATION", summary["participation_intent"])
        self.assertEqual(
            "body-current-posture-001",
            summary["selected_body_current_posture_id"],
        )
        self.assertEqual(1, summary["selected_evidence_count"])
        self.assertEqual(
            ["carrier-currentness-evidence-001"],
            summary["selected_evidence_ids"],
        )
        self.assertEqual(
            ["CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE"],
            summary["selected_evidence_outcomes"],
        )
        self.assertEqual(["carrier-b"], summary["selected_carrier_ids"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["participation_eligible"], True)
        self.assertIs(summary["participation_excluded"], False)
        self.assertSummaryNoCollapse(summary)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_for_eligible_excluded_and_blocked(self) -> None:
        eligible = self._eligible_result()
        excluded = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                participation_intent="EXCLUDE_FROM_CURRENTNESS_PARTICIPATION"
            )
        )
        blocked = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(extra={"latest_file_currentness": True})
        )

        for result in (eligible, excluded, blocked):
            with self.subTest(outcome=result["outcome"]):
                self.assertOutcomeFamily(result)
                self.assertNonClaimsFalse(result)

    def test_currentness_participation_excluded(self) -> None:
        result = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                participation_intent="EXCLUDE_FROM_CURRENTNESS_PARTICIPATION",
                extra={"exclusion_reason": "excluded for this declared question only"},
            )
        )

        self.assertEqual("CURRENTNESS_PARTICIPATION_EXCLUDED", result["outcome"])
        participation = result["currentness_participation_result"]
        self.assertIs(participation["currentness_participation_eligible"], False)
        self.assertIs(participation["currentness_participation_excluded"], True)
        self.assertIs(participation["selected_evidence_preserved"], True)
        self.assertEqual(
            "excluded for this declared question only",
            participation["exclusion_reason"],
        )
        self.assertSummaryNoCollapse(result["cross_carrier_currentness_summary"])

    def test_explicit_block_intent(self) -> None:
        result = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                participation_intent="BLOCK_CURRENTNESS_PARTICIPATION"
            )
        )

        self.assertBlocked(result, "BLOCK_CURRENTNESS_PARTICIPATION_REQUESTED")
        self.assertIs(
            result["currentness_participation_result"][
                "currentness_participation_eligible"
            ],
            False,
        )
        self.assertIs(
            result["currentness_participation_result"]["selected_evidence_may_participate"],
            False,
        )

    def test_builder_path_write_default_write_and_non_mutation(self) -> None:
        posture = _body_posture("builder-body-posture")
        evidence = [_evidence("builder-evidence")]
        request = resolver.build_declared_currentness_request(
            "builder-currentness-request",
            "May builder evidence participate?",
            posture,
            evidence,
        )

        self.assertEqual(
            "builder-currentness-request",
            request["currentness_request_id"],
        )
        self.assertEqual(
            "May builder evidence participate?",
            request["currentness_question"],
        )
        self.assertEqual(posture, request["selected_body_current_posture"])
        self.assertEqual(evidence, request["selected_carrier_evidence"])
        self.assertEqual("EVALUATE_PARTICIPATION", request["participation_intent"])
        self.assertEqual(_false_non_claims(), request["declared_non_claims"])

        original_request = copy.deepcopy(request)
        original_evidence = copy.deepcopy(evidence)
        result = resolver.resolve_cross_carrier_currentness_boundary(request)
        self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", result["outcome"])
        self.assertEqual(original_request, request)
        self.assertEqual(original_evidence, evidence)
        second_result = resolver.resolve_cross_carrier_currentness_boundary(request)
        self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", second_result["outcome"])
        self.assertEqual(original_request, request)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            request_path = temp_path / "request.json"
            _write_json(request_path, request)
            path_result = resolver.resolve_cross_carrier_currentness_boundary_from_path(
                request_path
            )
            self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", path_result["outcome"])
            self.assertTopLevelShape(path_result)
            self.assertEqual(
                str(request_path),
                path_result["declared_currentness_question"][
                    "declared_currentness_request_path"
                ],
            )
            self.assertEqual(set(result.keys()), set(path_result.keys()))

            explicit_output = temp_path / "nested" / "result.json"
            written = resolver.write_cross_carrier_currentness_result(
                result,
                explicit_output,
            )
            self.assertEqual(explicit_output, written)
            parsed = _read_json(written)
            self.assertTopLevelShape(parsed)

            with mock.patch.object(
                resolver,
                "CROSS_CARRIER_CURRENTNESS_BOUNDARY_ROOT",
                temp_path / "default-root",
            ):
                first = resolver.write_cross_carrier_currentness_result(result)
                second = resolver.write_cross_carrier_currentness_result(result)
            self.assertEqual(temp_path / "default-root", first.parent)
            self.assertEqual(temp_path / "default-root", second.parent)
            self.assertTrue(str(first).endswith("__cross_carrier_currentness_result.json"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("_001", second.stem)

            resolver.write_cross_carrier_currentness_result(result, temp_path / "again.json")
            self.assertEqual(original_request, request)

    def test_missing_malformed_path_and_basis_blocks(self) -> None:
        self.assertBlocked(
            resolver.resolve_cross_carrier_currentness_boundary(),
            "DECLARED_CURRENTNESS_REQUEST_MISSING",
        )
        self.assertBlocked(
            resolver.resolve_cross_carrier_currentness_boundary(
                declared_currentness_request=["not", "a", "mapping"]  # type: ignore[arg-type]
            ),
            "DECLARED_CURRENTNESS_REQUEST_MALFORMED",
        )

        blank_question = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(currentness_question="")
        )
        self.assertBlocked(blank_question, "CURRENTNESS_QUESTION_UNDECLARED")

        no_posture = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(include_body_posture=False)
        )
        self.assertBlocked(no_posture, "BODY_CURRENT_POSTURE_UNDECLARED")

        no_evidence = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(include_evidence=False)
        )
        self.assertBlocked(no_evidence, "SELECTED_CARRIER_EVIDENCE_MISSING")

        empty_evidence = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(selected_carrier_evidence=[])
        )
        self.assertBlocked(empty_evidence, "SELECTED_CARRIER_EVIDENCE_MISSING")

        malformed_evidence = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                selected_carrier_evidence=[_evidence("valid"), "bad"]
            )
        )
        self.assertBlocked(malformed_evidence, "SELECTED_CARRIER_EVIDENCE_MALFORMED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            unreadable = resolver.resolve_cross_carrier_currentness_boundary_from_path(
                temp_path / "missing.json"
            )
            self.assertBlocked(unreadable, "DECLARED_CURRENTNESS_REQUEST_UNREADABLE")

            bad_json = temp_path / "bad.json"
            bad_json.write_text("{bad json", encoding="utf-8")
            bad_result = resolver.resolve_cross_carrier_currentness_boundary_from_path(
                bad_json
            )
            self.assertBlocked(bad_result, "DECLARED_CURRENTNESS_REQUEST_MALFORMED")

            array_json = temp_path / "array.json"
            _write_json(array_json, ["not", "object"])
            array_result = resolver.resolve_cross_carrier_currentness_boundary_from_path(
                array_json
            )
            self.assertBlocked(array_result, "DECLARED_CURRENTNESS_REQUEST_MALFORMED")

    def test_blocking_selected_evidence_required_fields(self) -> None:
        cases = (
            ("EVIDENCE_IDENTITY_MISSING", _evidence("")),
            ("EVIDENCE_OUTCOME_MISSING", _evidence("missing-outcome", outcome=None)),
            ("CARRIER_IDENTITY_MISSING", _evidence("missing-carrier", carrier_id=None)),
            (
                "ADMISSION_STATUS_UNKNOWN",
                _evidence("missing-admission", admission_status=None),
            ),
            (
                "DIVERGENCE_STATUS_UNKNOWN",
                _evidence("missing-divergence", divergence_status=None),
            ),
            (
                "DIVERGENCE_STATUS_UNKNOWN",
                _evidence("unknown-divergence", divergence_status="UNKNOWN"),
            ),
        )

        for expected_code, evidence in cases:
            with self.subTest(block=expected_code):
                result = resolver.resolve_cross_carrier_currentness_boundary(
                    declared_currentness_request=_request(
                        selected_carrier_evidence=[evidence]
                    )
                )
                self.assertBlocked(result, expected_code)

    def test_blocking_hidden_divergence_and_unsupported_intent(self) -> None:
        hidden = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(extra={"divergence_hidden": True})
        )
        self.assertBlocked(hidden, "HIDDEN_DIVERGENCE_BLOCKS_CURRENTNESS")

        evidence_hidden = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                selected_carrier_evidence=[
                    _evidence("hidden-evidence", extra={"hidden_divergence": True})
                ]
            )
        )
        self.assertBlocked(evidence_hidden, "HIDDEN_DIVERGENCE_BLOCKS_CURRENTNESS")

        unsupported = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                participation_intent="SELECT_CURRENT_CARRIER"
            )
        )
        self.assertBlocked(unsupported, "PARTICIPATION_INTENT_UNSUPPORTED")

    def test_blocking_currentness_shortcuts(self) -> None:
        cases = (
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS"),
            ({"newest_timestamp_currentness": True}, "NEWEST_TIMESTAMP_CURRENTNESS"),
            ({"local_copy_currentness": True}, "LOCAL_COPY_CURRENTNESS"),
            ({"possession_currentness": True}, "POSSESSION_CURRENTNESS"),
            ({"return_currentness": True}, "RETURN_CURRENTNESS"),
            ({"receipt_currentness": True}, "RECEIPT_CURRENTNESS"),
            ({"admission_currentness": True}, "ADMISSION_CURRENTNESS"),
            ({"correspondence_currentness": True}, "CORRESPONDENCE_CURRENTNESS"),
            ({"divergence_currentness": True}, "DIVERGENCE_CURRENTNESS"),
            ({"majority_carrier_currentness": True}, "MAJORITY_CARRIER_CURRENTNESS"),
            (
                {"successful_receipt_count_currentness": True},
                "SUCCESSFUL_RECEIPT_COUNT_CURRENTNESS",
            ),
            (
                {"successful_admission_count_currentness": True},
                "SUCCESSFUL_ADMISSION_COUNT_CURRENTNESS",
            ),
            ({"carrier_availability_currentness": True}, "CARRIER_AVAILABILITY_CURRENTNESS"),
            ({"carrier_label_currentness": True}, "CARRIER_LABEL_CURRENTNESS"),
        )

        for update, code in cases:
            with self.subTest(update=update):
                result = resolver.resolve_cross_carrier_currentness_boundary(
                    declared_currentness_request=_request(extra=update)
                )
                self.assertBlocked(result, code)
                self.assertNonClaimsFalse(result)

    def test_blocking_winning_losing_hierarchy_and_structural_collapse(self) -> None:
        cases = (
            ({"winning_carrier_selected": True}, "WINNING_CARRIER_SELECTED"),
            ({"losing_carrier_invalidated": True}, "LOSING_CARRIER_INVALIDATED"),
            ({"carrier_hierarchy_created": True}, "CARRIER_HIERARCHY_CREATED"),
            ({"source_replaced": True}, "CURRENTNESS_REPLACES_SOURCE"),
            ({"authority_created": True}, "CURRENTNESS_CREATES_AUTHORITY"),
            ({"permission_created": True}, "CURRENTNESS_CREATES_PERMISSION"),
            ({"currentness_creates_successor": True}, "CURRENTNESS_CREATES_SUCCESSOR"),
            ({"currentness_creates_body": True}, "CURRENTNESS_CREATES_BODY"),
            (
                {"signal_created_by_default": True},
                "CURRENTNESS_CREATES_SIGNAL_BY_DEFAULT",
            ),
            ({"presence_established": True}, "CURRENTNESS_ESTABLISHES_PRESENCE"),
            ({"threshold_met": True}, "CURRENTNESS_ESTABLISHES_THRESHOLD"),
            ({"truth_created": True}, "CURRENTNESS_CREATES_TRUTH"),
            ({"action_authorized": True}, "CURRENTNESS_AUTHORIZES_ACTION"),
            ({"consequence_created": True}, "CURRENTNESS_CREATES_CONSEQUENCE"),
            (
                {"multi_carrier_law_created": True},
                "CURRENTNESS_CREATES_MULTI_CARRIER_LAW",
            ),
            (
                {"distributed_standing_created": True},
                "CURRENTNESS_CREATES_DISTRIBUTED_STANDING",
            ),
            ({"continuation_authorized": True}, "CURRENTNESS_AUTHORIZES_CONTINUATION"),
            ({"refusal_hidden": True}, "CURRENTNESS_HIDES_REFUSAL"),
            (
                {"mutation_performed": True},
                "CURRENTNESS_MUTATES_OR_REPLAYS_EVIDENCE",
            ),
            ({"replay_performed": True}, "CURRENTNESS_MUTATES_OR_REPLAYS_EVIDENCE"),
            ({"merge_performed": True}, "CURRENTNESS_MUTATES_OR_REPLAYS_EVIDENCE"),
        )

        for update, code in cases:
            with self.subTest(update=update):
                result = resolver.resolve_cross_carrier_currentness_boundary(
                    declared_currentness_request=_request(extra=update)
                )
                self.assertBlocked(result, code)
                self.assertNonClaimsFalse(result)

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        missing_non_claim = _false_non_claims()
        missing_non_claim.pop("authority_created")
        missing = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(non_claims=missing_non_claim)
        )
        self.assertBlocked(missing, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertNonClaimsFalse(missing)

        flipped = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                non_claims=_false_non_claims(authority_created=True)
            )
        )
        self.assertIn(
            flipped["block"]["code"],
            {"CURRENTNESS_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertEqual("CURRENTNESS_PARTICIPATION_BLOCKED", flipped["outcome"])
        self.assertNonClaimsFalse(flipped)

        selected_flipped = resolver.resolve_cross_carrier_currentness_boundary(
            declared_currentness_request=_request(
                selected_carrier_evidence=[
                    _evidence(
                        "selected-flipped",
                        non_claims=_false_non_claims(authority_created=True),
                    )
                ]
            )
        )
        self.assertEqual("CURRENTNESS_PARTICIPATION_BLOCKED", selected_flipped["outcome"])
        self.assertIn(
            selected_flipped["block"]["code"],
            {"CURRENTNESS_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertNonClaimsFalse(selected_flipped)


if __name__ == "__main__":
    unittest.main()
