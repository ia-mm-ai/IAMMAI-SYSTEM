"""Tests for bounded cross-carrier divergence boundary resolution.

This suite audits one divergence boundary resolver. It verifies that selected
carrier-produced or carrier-admitted evidence may visibly disagree without
becoming source, currentness, authority, permission, truth, action, carrier
hierarchy, multi-carrier law, distributed standing, or continuation.
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

import resolve_cross_carrier_divergence_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "cross_carrier_divergence_metadata",
    "declared_divergence_question",
    "selected_carrier_evidence",
    "divergence_basis",
    "divergence_checks",
    "divergence_result",
    "divergence_non_meaning",
    "divergence_consequence_boundary",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "cross_carrier_divergence_summary",
}

EXPECTED_CHECK_NAMES = {
    "declared_divergence_request_is_parseable_mapping",
    "selected_evidence_exists",
    "selected_evidence_parseable",
    "sufficient_evidence_surfaces",
    "evidence_identity_present",
    "evidence_outcome_present",
    "carrier_identity_present_where_required",
    "divergence_question_declared",
    "divergence_type_supported",
    "mismatch_visible_where_required",
    "refusal_visible_where_applicable",
    "divergence_does_not_hide_mismatch",
    "divergence_does_not_hide_refusal",
    "divergence_does_not_overwrite_evidence",
    "divergence_does_not_mutate_replay_or_merge_evidence",
    "divergence_does_not_replace_source",
    "divergence_does_not_create_currentness",
    "divergence_does_not_create_authority",
    "divergence_does_not_create_permission",
    "divergence_does_not_create_successor_body",
    "divergence_does_not_create_signal_by_default",
    "divergence_does_not_establish_presence_threshold",
    "divergence_does_not_create_truth",
    "divergence_does_not_authorize_action_create_consequence",
    "divergence_does_not_create_multi_carrier_law_distributed_standing",
    "divergence_does_not_authorize_continuation",
    "divergence_does_not_resolve_by_majority_latest_success_count",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "required_non_claims_remain_false",
}

DIVERGENCE_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_source_replacement",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor_standing",
    "does_not_mean_body_formation",
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
    "does_not_mean_majority_rule",
    "does_not_mean_latest_file_rule",
    "does_not_mean_successful_receipt_count_rule",
    "does_not_mean_winning_carrier",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_body_must_resolve_now",
}

OPEN_SURFACES = {
    "cross-carrier divergence implementation refinement",
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
    "CARRIER_DIVERGENCE_RECORDED",
    "NO_CARRIER_DIVERGENCE",
    "CARRIER_DIVERGENCE_BLOCKED",
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


def _evidence(
    evidence_id: str = "carrier-evidence-a",
    *,
    outcome: str = "CARRIED_SURFACE_RECEIVED",
    carrier_id: str = "carrier-a",
    carrier_role: str = "RECEIVING_CARRIER",
    emission_class: str = "CARRIED_SURFACE_RECEIPT",
    basis_id: str = "basis-a",
    return_path: str = "returned/carrier-evidence-a.json",
    integrity_hash: str = "a" * 64,
    sequence: int = 1,
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
            "basis_id": basis_id,
            "basis_posture": "downstream_carried_evidence_only",
        },
        "return_path": return_path,
        "return_context": {
            "return_posture": "returned_to_body_line_not_admitted_by_default",
        },
        "integrity_evidence": {
            "hash_algorithm": "sha256",
            "hash": integrity_hash,
            "integrity_posture": "preserved_where_supplied",
        },
        "sequence": sequence,
        "block_code": "BLOCKED_RECEIPT" if outcome == "BLOCKED" else None,
        "block_reason": "receipt refused visibly" if outcome == "BLOCKED" else None,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if extra:
        evidence.update(copy.deepcopy(extra))
    return evidence


def _request(
    *,
    divergence_request_id: str = "divergence-request-001",
    divergence_question: object = "How may selected carrier evidence disagree?",
    divergence_type: str = "OUTCOME_DIVERGENCE",
    evidence: list[object] | None = None,
    include_evidence: bool = True,
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    if evidence is None:
        evidence = [
            _evidence(
                "carrier-evidence-blocked",
                outcome="BLOCKED",
                carrier_id="carrier-a",
                return_path="returned/blocked.json",
                integrity_hash="a" * 64,
            ),
            _evidence(
                "carrier-evidence-received",
                outcome="CARRIED_SURFACE_RECEIVED",
                carrier_id="carrier-b",
                return_path="returned/received.json",
                integrity_hash="b" * 64,
            ),
        ]
    request: dict[str, object] = {
        "divergence_request_id": divergence_request_id,
        "divergence_question": divergence_question,
        "divergence_purpose": "Preserve visible carrier evidence mismatch only.",
        "declared_scope": "cross_carrier_divergence_boundary_test",
        "divergence_type": divergence_type,
        "expected_comparison_basis": {
            "comparison_basis_id": "comparison-basis-001",
            "comparison_posture": "visible_mismatch_without_resolution",
        },
        "declared_non_claims": copy.deepcopy(
            non_claims if non_claims is not None else _false_non_claims()
        ),
    }
    if include_evidence:
        request["selected_carrier_evidence"] = copy.deepcopy(evidence)
    if extra:
        request.update(copy.deepcopy(extra))
    return request


class CrossCarrierDivergenceBoundaryTests(unittest.TestCase):
    def assertBlocked(self, result: dict, code: str) -> None:
        self.assertEqual("CARRIER_DIVERGENCE_BLOCKED", result["outcome"])
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
        for check in result["divergence_checks"]:
            with self.subTest(check=check.get("check_name")):
                self.assertIn("check_name", check)
                self.assertIn("passed", check)
                self.assertIn("expected_posture", check)
                self.assertIn("actual_posture", check)
                self.assertIn("block_code", check)

    def assertSummaryNoCollapse(self, summary: dict) -> None:
        for key in (
            "mismatch_hidden",
            "refusal_hidden",
            "source_created",
            "currentness_created",
            "authority_created",
            "permission_created",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "carrier_hierarchy_created",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "multi_carrier_law_created",
            "distributed_standing_created",
            "continuation_authorized",
        ):
            with self.subTest(summary_key=key):
                self.assertIs(summary[key], False)

    def _recorded_result(self) -> dict:
        return resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request()
        )

    def test_successful_outcome_divergence(self) -> None:
        result = self._recorded_result()

        self.assertIsInstance(result, dict)
        self.assertTopLevelShape(result)
        self.assertOutcomeFamily(result)
        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])

        divergence = result["divergence_result"]
        self.assertIs(divergence["divergence_recorded"], True)
        self.assertIs(divergence["visible_divergence"], True)
        self.assertIs(divergence["hidden_divergence"], False)
        self.assertIs(divergence["mismatch_preserved"], True)
        self.assertIs(result["non_claims"]["winning_carrier_selected"], False)
        self.assertIs(result["non_claims"]["losing_carrier_invalidated"], False)

    def test_metadata_question_selected_evidence_and_basis(self) -> None:
        result = self._recorded_result()
        metadata = result["cross_carrier_divergence_metadata"]
        question = result["declared_divergence_question"]
        selected = result["selected_carrier_evidence"]
        basis = result["divergence_basis"]

        for key in (
            "cross_carrier_divergence_result_id",
            "cross_carrier_divergence_result_type",
            "cross_carrier_divergence_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["cross_carrier_divergence_result_version"])
        self.assertEqual("resolve_cross_carrier_divergence_boundary", metadata["resolver_module"])

        self.assertEqual("divergence-request-001", question["divergence_request_id"])
        self.assertEqual(
            "How may selected carrier evidence disagree?",
            question["divergence_question"],
        )
        self.assertEqual("OUTCOME_DIVERGENCE", question["divergence_type"])
        self.assertEqual(
            "Preserve visible carrier evidence mismatch only.",
            question["divergence_purpose"],
        )
        self.assertEqual("cross_carrier_divergence_boundary_test", question["declared_scope"])
        self.assertIsInstance(question["declared_non_claims"], dict)

        self.assertEqual(2, len(selected))
        for evidence in selected:
            with self.subTest(evidence=evidence["evidence_id"]):
                self.assertTrue(evidence["evidence_id"])
                self.assertTrue(evidence["evidence_outcome"])
                self.assertTrue(evidence["carrier_id"])
                self.assertTrue(evidence["carrier_role"])
                self.assertTrue(evidence["emission_class"])
                self.assertTrue(evidence["source_or_carried_basis"])
                self.assertTrue(evidence["return_path"])
                self.assertTrue(evidence["return_context"])
                self.assertTrue(evidence["integrity_hash"])
                self.assertIn("block_code", evidence)
                self.assertIn("block_reason", evidence)
                self.assertIsInstance(evidence["non_claims"], dict)

        self.assertEqual("OUTCOME_DIVERGENCE", basis["divergence_type"])
        self.assertIn("OUTCOME_DIVERGENCE", basis["supported_divergence_types"])
        self.assertEqual(
            ["carrier-evidence-blocked", "carrier-evidence-received"],
            basis["selected_evidence_ids"],
        )
        self.assertEqual(
            ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
            basis["selected_evidence_outcomes"],
        )
        self.assertEqual(["carrier-a", "carrier-b"], basis["selected_carrier_ids"])
        self.assertEqual(
            {"comparison_basis_id": "comparison-basis-001", "comparison_posture": "visible_mismatch_without_resolution"},
            basis["expected_comparison_basis"],
        )
        self.assertIs(basis["visible_mismatch"], True)
        self.assertIs(basis["non_claims_explicit"], True)
        self.assertNonClaimsFalse(result)

    def test_checks_result_non_meaning_consequence_open_and_summary(self) -> None:
        result = self._recorded_result()
        self.assertChecksWellFormed(result)

        check_names = {check["check_name"] for check in result["divergence_checks"]}
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(check_names))
        self.assertEqual(
            0,
            sum(1 for check in result["divergence_checks"] if check["passed"] is False),
        )
        self.assertTrue(all(check["passed"] for check in result["divergence_checks"]))

        divergence = result["divergence_result"]
        self.assertEqual("OUTCOME_DIVERGENCE", divergence["divergence_type"])
        self.assertTrue(divergence["divergence_claim"])
        self.assertEqual(2, divergence["selected_evidence_count"])
        self.assertEqual(
            ["carrier-evidence-blocked", "carrier-evidence-received"],
            divergence["selected_evidence_ids"],
        )
        self.assertEqual(["BLOCKED", "CARRIED_SURFACE_RECEIVED"], divergence["selected_evidence_outcomes"])
        self.assertEqual(["carrier-a", "carrier-b"], divergence["selected_carrier_ids"])
        self.assertTrue(divergence["divergence_evidence"])
        self.assertIs(divergence["refusal_hidden"], False)
        self.assertIs(divergence["mismatch_hidden"], False)
        self.assertIs(divergence["evidence_overwritten"], False)
        self.assertIs(divergence["source_not_replaced"], True)
        self.assertIs(divergence["currentness_not_created"], True)
        self.assertIs(divergence["authority_not_created"], True)
        self.assertIs(divergence["permission_not_created"], True)
        self.assertIs(divergence["truth_not_created"], True)
        self.assertIs(divergence["action_not_authorized"], True)
        self.assertIs(divergence["carrier_hierarchy_not_created"], True)
        self.assertIs(divergence["multi_carrier_law_not_created"], True)
        self.assertIs(divergence["distributed_standing_not_created"], True)
        self.assertIs(divergence["continuation_not_authorized"], True)

        for key in DIVERGENCE_NON_MEANING_TRUE_KEYS:
            with self.subTest(non_meaning=key):
                self.assertIs(result["divergence_non_meaning"][key], True)

        consequence = result["divergence_consequence_boundary"]
        for key in (
            "prevent_downstream_reliance",
            "require_later_correspondence_review",
            "require_later_admission_review",
            "require_later_currentness_boundary_review",
            "remain_open_as_visible_divergence",
            "be_used_as_evidence_for_future_block",
        ):
            self.assertIs(consequence["divergence_may"][key], True)
        for key in (
            "decide_source",
            "decide_currentness",
            "decide_truth",
            "decide_action",
            "select_winning_carrier",
            "erase_losing_carrier_evidence",
            "create_carrier_hierarchy",
            "create_carrier_relation",
            "create_multi_carrier_law",
            "create_distributed_standing",
            "authorize_continuation",
        ):
            self.assertIs(consequence["divergence_may_not"][key], True)

        open_section = result["what_remains_open"]
        self.assertTrue(OPEN_SURFACES.issubset(set(open_section["open_surfaces"])))
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)

        summary = resolver.build_cross_carrier_divergence_summary(result)
        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("divergence-request-001", summary["divergence_request_id"])
        self.assertEqual("OUTCOME_DIVERGENCE", summary["divergence_type"])
        self.assertIs(summary["divergence_recorded"], True)
        self.assertIs(summary["no_carrier_divergence"], False)
        self.assertEqual(2, summary["selected_evidence_count"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["visible_divergence"], True)
        self.assertIs(summary["hidden_divergence"], False)
        self.assertSummaryNoCollapse(summary)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_for_recorded_no_divergence_and_blocked(self) -> None:
        recorded = self._recorded_result()
        no_divergence = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="OUTCOME_DIVERGENCE",
                evidence=[
                    _evidence("same-a", outcome="CARRIED_SURFACE_RECEIVED"),
                    _evidence("same-b", outcome="CARRIED_SURFACE_RECEIVED"),
                ],
            )
        )
        blocked = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(extra={"mismatch_hidden": True})
        )

        self.assertEqual("NO_CARRIER_DIVERGENCE", no_divergence["outcome"])
        self.assertEqual("CARRIER_DIVERGENCE_BLOCKED", blocked["outcome"])
        for result in (recorded, no_divergence, blocked):
            with self.subTest(outcome=result["outcome"]):
                self.assertNonClaimsFalse(result)

    def test_divergence_type_detection_cases(self) -> None:
        cases = (
            (
                "RECEIPT_REFUSAL_DIVERGENCE",
                [
                    _evidence("blocked", outcome="BLOCKED"),
                    _evidence("received", outcome="CARRIED_SURFACE_RECEIVED"),
                ],
            ),
            (
                "BASIS_DIVERGENCE",
                [_evidence("basis-a", basis_id="basis-a"), _evidence("basis-b", basis_id="basis-b")],
            ),
            (
                "INTEGRITY_DIVERGENCE",
                [_evidence("hash-a", integrity_hash="a" * 64), _evidence("hash-b", integrity_hash="b" * 64)],
            ),
            (
                "CARRIER_IDENTITY_DIVERGENCE",
                [_evidence("carrier-a", carrier_id="carrier-a"), _evidence("carrier-b", carrier_id="carrier-b")],
            ),
            (
                "ROLE_DIVERGENCE",
                [_evidence("role-a", carrier_role="RECEIVING_CARRIER"), _evidence("role-b", carrier_role="RETURNING_CARRIER")],
            ),
            (
                "EMISSION_CLASS_DIVERGENCE",
                [_evidence("class-a", emission_class="CARRIED_SURFACE_RECEIPT"), _evidence("class-b", emission_class="RECEIPT_BLOCK")],
            ),
            (
                "RETURN_PATH_DIVERGENCE",
                [_evidence("return-a", return_path="return/a.json"), _evidence("return-b", return_path="return/b.json")],
            ),
            (
                "STALE_OR_SEQUENCE_DIVERGENCE",
                [_evidence("sequence-a", sequence=1), _evidence("sequence-b", sequence=2)],
            ),
        )

        for divergence_type, evidence in cases:
            with self.subTest(divergence_type=divergence_type):
                result = resolver.resolve_cross_carrier_divergence_boundary(
                    declared_divergence_request=_request(
                        divergence_type=divergence_type,
                        evidence=evidence,
                    )
                )
                self.assertEqual("CARRIER_DIVERGENCE_RECORDED", result["outcome"])
                self.assertEqual(divergence_type, result["divergence_result"]["divergence_type"])
                self.assertIs(result["divergence_result"]["mismatch_preserved"], True)
                self.assertSummaryNoCollapse(result["cross_carrier_divergence_summary"])

    def test_receipt_refusal_divergence_preserves_both_sides(self) -> None:
        result = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="RECEIPT_REFUSAL_DIVERGENCE",
                evidence=[
                    _evidence("blocked", outcome="BLOCKED"),
                    _evidence("received", outcome="CARRIED_SURFACE_RECEIVED"),
                ],
            )
        )

        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", result["outcome"])
        self.assertIs(result["divergence_result"]["refusal_hidden"], False)
        self.assertIn("blocked", result["divergence_result"]["selected_evidence_ids"])
        self.assertIn("received", result["divergence_result"]["selected_evidence_ids"])
        self.assertIs(result["non_claims"]["losing_carrier_invalidated"], False)

    def test_non_claim_missing_malformed_and_no_divergence_paths(self) -> None:
        non_claim_conflict = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="NON_CLAIM_DIVERGENCE",
                evidence=[
                    _evidence("non-claim-a"),
                    _evidence("non-claim-b", non_claims=_false_non_claims(currentness_created=True)),
                ],
            )
        )
        self.assertIn(
            non_claim_conflict["outcome"],
            {"CARRIER_DIVERGENCE_RECORDED", "CARRIER_DIVERGENCE_BLOCKED"},
        )
        self.assertIs(non_claim_conflict["divergence_result"]["hidden_divergence"], False)
        self.assertNotEqual("NO_CARRIER_DIVERGENCE", non_claim_conflict["outcome"])

        missing = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="MISSING_EVIDENCE_DIVERGENCE",
                evidence=[
                    _evidence("present"),
                    _evidence(
                        "missing-placeholder",
                        outcome="MISSING",
                        extra={"missing_evidence": True, "missing_context": "carrier line absent"},
                    ),
                ],
            )
        )
        self.assertIn(
            missing["outcome"],
            {"CARRIER_DIVERGENCE_RECORDED", "CARRIER_DIVERGENCE_BLOCKED"},
        )
        self.assertIs(missing["divergence_result"]["mismatch_hidden"], False)
        self.assertIs(missing["divergence_result"]["source_not_replaced"], True)

        malformed = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="MALFORMED_EVIDENCE_DIVERGENCE",
                evidence=[
                    _evidence("present"),
                    _evidence(
                        "malformed-placeholder",
                        outcome="MALFORMED",
                        extra={
                            "malformed_evidence": True,
                            "block_reason": "visible malformed evidence",
                        },
                    ),
                ],
            )
        )
        self.assertIn(
            malformed["outcome"],
            {"CARRIER_DIVERGENCE_RECORDED", "CARRIER_DIVERGENCE_BLOCKED"},
        )
        self.assertIn("malformed-placeholder", malformed["divergence_result"]["selected_evidence_ids"])

        explicit_no_divergence = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="NO_DIVERGENCE",
                evidence=[
                    _evidence("same-a", outcome="CARRIED_SURFACE_RECEIVED", carrier_id="carrier-a"),
                    _evidence("same-b", outcome="CARRIED_SURFACE_RECEIVED", carrier_id="carrier-a"),
                ],
            )
        )
        self.assertEqual("NO_CARRIER_DIVERGENCE", explicit_no_divergence["outcome"])
        self.assertIs(explicit_no_divergence["divergence_result"]["divergence_recorded"], False)
        self.assertIs(explicit_no_divergence["divergence_result"]["no_carrier_divergence"], True)
        self.assertIs(explicit_no_divergence["divergence_result"]["selected_evidence_preserved"], True)

        positive_no_mismatch = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                divergence_type="OUTCOME_DIVERGENCE",
                evidence=[
                    _evidence("same-a", outcome="CARRIED_SURFACE_RECEIVED"),
                    _evidence("same-b", outcome="CARRIED_SURFACE_RECEIVED"),
                ],
            )
        )
        self.assertEqual("NO_CARRIER_DIVERGENCE", positive_no_mismatch["outcome"])
        self.assertIsNone(positive_no_mismatch["block"]["code"])

    def test_builder_path_write_default_write_and_non_mutation(self) -> None:
        evidence = [
            _evidence("builder-a", outcome="BLOCKED"),
            _evidence("builder-b", outcome="CARRIED_SURFACE_RECEIVED"),
        ]
        request = resolver.build_declared_divergence_request(
            "builder-request",
            "Do builder evidence outcomes diverge?",
            "OUTCOME_DIVERGENCE",
            evidence,
        )
        self.assertEqual("builder-request", request["divergence_request_id"])
        self.assertEqual("Do builder evidence outcomes diverge?", request["divergence_question"])
        self.assertEqual("OUTCOME_DIVERGENCE", request["divergence_type"])
        self.assertEqual(evidence, request["selected_carrier_evidence"])
        self.assertEqual(_false_non_claims(), request["declared_non_claims"])

        original_request = copy.deepcopy(request)
        original_evidence = copy.deepcopy(evidence)
        result = resolver.resolve_cross_carrier_divergence_boundary(request)
        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", result["outcome"])
        self.assertEqual(original_request, request)
        self.assertEqual(original_evidence, evidence)
        second_result = resolver.resolve_cross_carrier_divergence_boundary(request)
        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", second_result["outcome"])
        self.assertEqual(original_request, request)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            request_path = temp_path / "request.json"
            _write_json(request_path, request)
            path_result = resolver.resolve_cross_carrier_divergence_boundary_from_path(request_path)
            self.assertEqual("CARRIER_DIVERGENCE_RECORDED", path_result["outcome"])
            self.assertTopLevelShape(path_result)
            self.assertEqual(
                str(request_path),
                path_result["declared_divergence_question"]["declared_divergence_request_path"],
            )

            explicit_output = temp_path / "nested" / "result.json"
            written = resolver.write_cross_carrier_divergence_result(result, explicit_output)
            self.assertEqual(explicit_output, written)
            parsed = _read_json(written)
            self.assertTopLevelShape(parsed)

            with mock.patch.object(
                resolver,
                "CROSS_CARRIER_DIVERGENCE_BOUNDARY_ROOT",
                temp_path / "default-root",
            ):
                first = resolver.write_cross_carrier_divergence_result(result)
                second = resolver.write_cross_carrier_divergence_result(result)
            self.assertTrue(str(first).endswith("__cross_carrier_divergence_result.json"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("_001", second.stem)

    def test_missing_malformed_path_and_basis_blocks(self) -> None:
        missing = resolver.resolve_cross_carrier_divergence_boundary()
        self.assertBlocked(missing, "DECLARED_DIVERGENCE_REQUEST_MISSING")

        malformed = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assertBlocked(malformed, "DECLARED_DIVERGENCE_REQUEST_MALFORMED")

        no_selected = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(include_evidence=False)
        )
        self.assertBlocked(no_selected, "SELECTED_EVIDENCE_MISSING")

        malformed_evidence = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(evidence=[_evidence("valid"), "bad"])
        )
        self.assertBlocked(malformed_evidence, "SELECTED_EVIDENCE_MALFORMED")

        insufficient = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(evidence=[_evidence("only")])
        )
        self.assertBlocked(insufficient, "INSUFFICIENT_EVIDENCE_SURFACES")

        for label, evidence, code in (
            ("identity", [_evidence(""), _evidence("valid")], "EVIDENCE_IDENTITY_MISSING"),
            (
                "carrier",
                [_evidence("a", carrier_id=""), _evidence("b")],
                "CARRIER_IDENTITY_MISSING",
            ),
            (
                "outcome",
                [_evidence("a", outcome=""), _evidence("b")],
                "EVIDENCE_OUTCOME_MISSING",
            ),
        ):
            with self.subTest(missing=label):
                result = resolver.resolve_cross_carrier_divergence_boundary(
                    declared_divergence_request=_request(evidence=evidence)
                )
                self.assertBlocked(result, code)

        blank_question = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(divergence_question="")
        )
        self.assertBlocked(blank_question, "DIVERGENCE_QUESTION_UNDECLARED")

        unsupported_type = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(divergence_type="UNSUPPORTED_DIVERGENCE")
        )
        self.assertBlocked(unsupported_type, "DIVERGENCE_TYPE_UNSUPPORTED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            unreadable = resolver.resolve_cross_carrier_divergence_boundary_from_path(
                temp_path / "missing.json"
            )
            self.assertBlocked(unreadable, "DECLARED_DIVERGENCE_REQUEST_UNREADABLE")

            bad_json = temp_path / "bad.json"
            bad_json.write_text("{bad json", encoding="utf-8")
            bad_result = resolver.resolve_cross_carrier_divergence_boundary_from_path(bad_json)
            self.assertBlocked(bad_result, "DECLARED_DIVERGENCE_REQUEST_MALFORMED")

            array_json = temp_path / "array.json"
            _write_json(array_json, ["not", "object"])
            array_result = resolver.resolve_cross_carrier_divergence_boundary_from_path(array_json)
            self.assertBlocked(array_result, "DECLARED_DIVERGENCE_REQUEST_MALFORMED")

    def test_hidden_overwrite_mutation_and_collapse_blocks(self) -> None:
        cases = (
            ({"divergence_hidden": True}, "DIVERGENCE_HIDES_MISMATCH"),
            ({"mismatch_hidden": True}, "DIVERGENCE_HIDES_MISMATCH"),
            ({"refusal_hidden": True}, "DIVERGENCE_HIDES_REFUSAL"),
            ({"evidence_overwritten": True}, "DIVERGENCE_OVERWRITES_EVIDENCE"),
            ({"mutation_performed": True}, "DIVERGENCE_MUTATES_OR_REPLAYS_EVIDENCE"),
            ({"replay_performed": True}, "DIVERGENCE_MUTATES_OR_REPLAYS_EVIDENCE"),
            ({"merge_performed": True}, "DIVERGENCE_MUTATES_OR_REPLAYS_EVIDENCE"),
            ({"source_replaced": True}, "DIVERGENCE_REPLACES_SOURCE"),
            ({"currentness_created": True}, "DIVERGENCE_CREATES_CURRENTNESS"),
            ({"authority_created": True}, "DIVERGENCE_CREATES_AUTHORITY"),
            ({"permission_created": True}, "DIVERGENCE_CREATES_PERMISSION"),
            ({"successor_standing_created": True}, "DIVERGENCE_CREATES_SUCCESSOR"),
            ({"body_created": True}, "DIVERGENCE_CREATES_BODY"),
            ({"signal_created_by_default": True}, "DIVERGENCE_CREATES_SIGNAL_BY_DEFAULT"),
            ({"presence_established": True}, "DIVERGENCE_ESTABLISHES_PRESENCE"),
            ({"threshold_met": True}, "DIVERGENCE_ESTABLISHES_THRESHOLD"),
            ({"truth_created": True}, "DIVERGENCE_CREATES_TRUTH"),
            ({"action_authorized": True}, "DIVERGENCE_AUTHORIZES_ACTION"),
            ({"consequence_created": True}, "DIVERGENCE_CREATES_CONSEQUENCE"),
            ({"multi_carrier_law_created": True}, "DIVERGENCE_CREATES_MULTI_CARRIER_LAW"),
            ({"distributed_standing_created": True}, "DIVERGENCE_CREATES_DISTRIBUTED_STANDING"),
            ({"continuation_authorized": True}, "DIVERGENCE_AUTHORIZES_CONTINUATION"),
            ({"divergence_resolved_by_majority": True}, "DIVERGENCE_RESOLVES_BY_MAJORITY"),
            ({"divergence_resolved_by_latest_file": True}, "DIVERGENCE_RESOLVES_BY_LATEST_FILE"),
            ({"divergence_resolved_by_success_count": True}, "DIVERGENCE_RESOLVES_BY_SUCCESS_COUNT"),
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS"),
            ({"recency_fraud": True}, "LATEST_FILE_CURRENTNESS"),
        )

        for update, code in cases:
            with self.subTest(update=update):
                result = resolver.resolve_cross_carrier_divergence_boundary(
                    declared_divergence_request=_request(extra=update)
                )
                self.assertBlocked(result, code)
                self.assertNonClaimsFalse(result)

    def test_winning_losing_carrier_and_required_non_claim_blocks(self) -> None:
        for claim in (
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
        ):
            with self.subTest(claim=claim):
                result = resolver.resolve_cross_carrier_divergence_boundary(
                    declared_divergence_request=_request(
                        non_claims=_false_non_claims(**{claim: True})
                    )
                )
                self.assertEqual("CARRIER_DIVERGENCE_BLOCKED", result["outcome"])
                self.assertIn(
                    result["block"]["code"],
                    {
                        "NON_CLAIM_MISSING_OR_FLIPPED",
                        "DIVERGENCE_RESOLVES_BY_MAJORITY",
                    },
                )
                self.assertNonClaimsFalse(result)

        missing_claims = _false_non_claims()
        missing_claims.pop("authority_created")
        missing = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(non_claims=missing_claims)
        )
        self.assertBlocked(missing, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = resolver.resolve_cross_carrier_divergence_boundary(
            declared_divergence_request=_request(
                non_claims=_false_non_claims(authority_created=True)
            )
        )
        self.assertIn(
            flipped["block"]["code"],
            {"DIVERGENCE_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertEqual("CARRIER_DIVERGENCE_BLOCKED", flipped["outcome"])


if __name__ == "__main__":
    unittest.main()
