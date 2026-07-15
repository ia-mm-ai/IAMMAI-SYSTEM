"""Tests for bounded multi-carrier relation boundary resolution.

This suite audits one relation boundary resolver. It verifies that selected
carriers or carrier-evidence surfaces may stand in bounded body-side relation
without becoming source, currentness, authority, permission, carrier
hierarchy, distributed standing, synchronization, truth, action, consequence,
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

import resolve_multi_carrier_relation_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "multi_carrier_relation_metadata",
    "declared_relation_question",
    "selected_carriers",
    "selected_carrier_evidence",
    "relation_basis",
    "relation_checks",
    "relation_result",
    "relation_non_meaning",
    "relation_consequence_boundary",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "multi_carrier_relation_summary",
}

EXPECTED_CHECK_NAMES = {
    "declared_relation_request_is_parseable_mapping",
    "relation_question_declared",
    "relation_type_supported",
    "selected_carriers_or_evidence_exists",
    "selected_carriers_or_evidence_parseable",
    "sufficient_selected_carriers_or_evidence",
    "evidence_identity_present",
    "evidence_outcome_present",
    "carrier_identity_present_where_required",
    "carrier_role_supported_where_required",
    "relation_detection_is_bounded",
    "visible_divergence_preserved_where_applicable",
    "hidden_divergence_false",
    "refusal_hidden_false",
    "relation_does_not_overwrite_evidence",
    "relation_does_not_mutate_replay_or_merge_evidence",
    "relation_does_not_replace_source",
    "relation_does_not_create_currentness",
    "relation_does_not_create_authority",
    "relation_does_not_create_permission",
    "relation_does_not_create_successor_body",
    "relation_does_not_create_carrier_hierarchy",
    "relation_does_not_select_winning_carrier",
    "relation_does_not_invalidate_losing_carrier",
    "relation_does_not_create_signal_by_default",
    "relation_does_not_establish_presence_threshold",
    "relation_does_not_create_truth",
    "relation_does_not_authorize_action_create_consequence",
    "relation_does_not_create_distributed_standing",
    "relation_does_not_authorize_continuation",
    "relation_does_not_resolve_divergence_by_majority_latest_success_count",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "non_claims_remain_false",
}

RELATION_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_source_replacement",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_successor_standing",
    "does_not_mean_body_formation",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_carrier_priority",
    "does_not_mean_carrier_sovereignty",
    "does_not_mean_winning_carrier",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_distributed_standing",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_carrier_registry",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
    "does_not_mean_divergence_resolution",
    "does_not_mean_majority_rule",
    "does_not_mean_latest_file_rule",
    "does_not_mean_success_count_rule",
    "does_not_mean_current_carrier_selection",
}

OPEN_SURFACES = {
    "multi-carrier relation implementation refinement",
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
    "MULTI_CARRIER_RELATION_RECOGNIZED",
    "NO_MULTI_CARRIER_RELATION",
    "MULTI_CARRIER_RELATION_BLOCKED",
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


def _carrier(
    carrier_id: str,
    *,
    role: str = "RECEIVING_CARRIER",
    label: str | None = None,
    non_claims: dict[str, bool] | None = None,
) -> dict[str, object]:
    return {
        "carrier_id": carrier_id,
        "carrier_label": label or carrier_id,
        "carrier_role": role,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }


def _evidence(
    evidence_id: str = "relation-evidence-a",
    *,
    outcome: str | None = "CARRIED_SURFACE_RECEIVED",
    carrier_id: str | None = "carrier-b",
    carrier_role: str | None = "RECEIVING_CARRIER",
    evidence_class: str | None = "RETURNED_RECEIPT_EVIDENCE",
    emission_class: str | None = "CARRIED_SURFACE_RECEIPT",
    basis_id: str = "carried-surface-001",
    source_carrier_id: str | None = "carrier-a",
    receiving_carrier_id: str | None = "carrier-b",
    admission_status: str | None = "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
    correspondence_status: str | None = "CORRESPONDENCE_RECOGNIZED",
    divergence_status: str | None = "CARRIER_DIVERGENCE_RECORDED",
    currentness_participation_status: str | None = "CURRENTNESS_PARTICIPATION_ELIGIBLE",
    return_path: str | None = "returned/relation-evidence-a.json",
    integrity_hash: str | None = "a" * 64,
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    evidence: dict[str, object] = {
        "evidence_id": evidence_id,
        "evidence_outcome": outcome,
        "carrier_id": carrier_id,
        "source_carrier_id": source_carrier_id,
        "receiving_carrier_id": receiving_carrier_id,
        "carrier_role": carrier_role,
        "evidence_class": evidence_class,
        "emission_class": emission_class,
        "source_or_carried_basis": {
            "basis_id": basis_id,
            "carried_surface_id": basis_id,
            "packet_id": "packet-001",
        },
        "admission_status": admission_status,
        "correspondence_status": correspondence_status,
        "divergence_status": divergence_status,
        "currentness_participation_status": currentness_participation_status,
        "return_path": return_path,
        "return_context": {
            "return_posture": "returned_evidence_remains_downstream",
        },
        "integrity_evidence": {
            "hash_algorithm": "sha256",
            "hash": integrity_hash,
            "integrity_posture": "preserved_where_supplied",
        },
        "block_code": "BLOCKED_RECEIPT" if outcome == "BLOCKED" else None,
        "block_reason": "receipt refusal remains visible" if outcome == "BLOCKED" else None,
        "non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if extra:
        evidence.update(copy.deepcopy(extra))
    return evidence


def _refusal_success_evidence() -> list[dict[str, object]]:
    return [
        _evidence(
            "returned-refusal-evidence",
            outcome="BLOCKED",
            carrier_id="carrier-b",
            carrier_role="REFUSING_CARRIER",
            evidence_class="RETURNED_BLOCKED_RECEIPT_EVIDENCE",
            emission_class="RECEIPT_BLOCK",
            return_path="returned/blocked.json",
            integrity_hash="b" * 64,
        ),
        _evidence(
            "returned-success-evidence",
            outcome="CARRIED_SURFACE_RECEIVED",
            carrier_id="carrier-b",
            carrier_role="RECEIVING_CARRIER",
            evidence_class="RETURNED_RECEIPT_EVIDENCE",
            emission_class="CARRIED_SURFACE_RECEIPT",
            return_path="returned/success.json",
            integrity_hash="c" * 64,
        ),
    ]


def _request(
    *,
    relation_request_id: str = "relation-request-001",
    relation_question: object = "When may selected carrier evidence stand in bounded relation?",
    relation_type: str = "REFUSAL_SUCCESS_RELATION",
    carriers: list[object] | None = None,
    evidence: list[object] | None = None,
    include_carriers: bool = True,
    include_evidence: bool = True,
    non_claims: dict[str, bool] | None = None,
    extra: dict[str, object] | None = None,
) -> dict[str, object]:
    if carriers is None:
        carriers = [
            _carrier("carrier-a", role="SOURCE_CARRIER_FOR_PACKET"),
            _carrier("carrier-b", role="RECEIVING_CARRIER"),
        ]
    if evidence is None:
        evidence = _refusal_success_evidence()

    request: dict[str, object] = {
        "relation_request_id": relation_request_id,
        "relation_question": relation_question,
        "relation_type": relation_type,
        "relation_purpose": "preserve bounded relation without collapse",
        "declared_scope": {
            "scope": "present_execution_line_relation_only",
            "distributed_standing": False,
        },
        "lineage_basis": {
            "carried_surface_id": "carried-surface-001",
            "operation_chain_id": "carrier-operation-chain-001",
        },
        "selected_admission_basis": {
            "admission_posture": "admitted_as_downstream_evidence_only",
        },
        "selected_correspondence_basis": {
            "correspondence_posture": "bounded_reading_relation_only",
        },
        "selected_divergence_basis": {
            "divergence_posture": "visible_divergence_preserved",
        },
        "selected_currentness_basis": {
            "currentness_participation_posture": "participation_only",
        },
        "declared_non_claims": copy.deepcopy(non_claims or _false_non_claims()),
    }
    if include_carriers:
        request["selected_carriers"] = copy.deepcopy(carriers)
    if include_evidence:
        request["selected_carrier_evidence"] = copy.deepcopy(evidence)
    if extra:
        request.update(copy.deepcopy(extra))
    return request


def _remove_nested_key(value: dict[str, object], dotted_key: str) -> None:
    current: object = value
    parts = dotted_key.split(".")
    for part in parts[:-1]:
        assert isinstance(current, dict)
        current = current[part]
    assert isinstance(current, dict)
    current.pop(parts[-1], None)


class MultiCarrierRelationBoundaryTests(unittest.TestCase):
    def _resolve(self, request: object) -> dict[str, object]:
        result = resolver.resolve_multi_carrier_relation_boundary(request)  # type: ignore[arg-type]
        self.assertIsInstance(result, dict)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        return result

    def _assert_top_level(self, result: dict[str, object]) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))

    def _assert_block_code(self, result: dict[str, object], expected: str) -> None:
        self.assertEqual("MULTI_CARRIER_RELATION_BLOCKED", result["outcome"])
        block = result["block"]
        self.assertIsInstance(block, dict)
        self.assertEqual(expected, block["code"])
        self.assertEqual(expected, block["block_code"])
        self.assertIsNotNone(block["reason"])

    def _assert_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        self.assertEqual(set(resolver.REQUIRED_NON_CLAIMS), set(non_claims))
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)

    def _assert_checks_well_formed(self, result: dict[str, object], *, all_pass: bool) -> None:
        checks = result["relation_checks"]
        self.assertIsInstance(checks, list)
        self.assertTrue(checks)
        names = {check["check_name"] for check in checks}
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(names))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
        if all_pass:
            self.assertEqual(0, sum(1 for check in checks if not check["passed"]))

    def test_successful_refusal_success_relation_shape_and_boundary_posture(self) -> None:
        request = _request()

        result = self._resolve(request)

        self._assert_top_level(result)
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])

        metadata = result["multi_carrier_relation_metadata"]
        self.assertTrue(metadata["multi_carrier_relation_result_id"])
        self.assertEqual("multi_carrier_relation_boundary_result", metadata["multi_carrier_relation_result_type"])
        self.assertEqual("0.1.0", metadata["multi_carrier_relation_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual("resolve_multi_carrier_relation_boundary", metadata["resolver_module"])

        declared = result["declared_relation_question"]
        self.assertEqual(request["relation_request_id"], declared["relation_request_id"])
        self.assertEqual(request["relation_question"], declared["relation_question"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", declared["relation_type"])
        self.assertEqual(request["relation_purpose"], declared["relation_purpose"])
        self.assertEqual(request["declared_scope"], declared["declared_scope"])
        self.assertEqual(2, declared["selected_carrier_count"])
        self.assertEqual(2, declared["selected_evidence_count"])
        self.assertEqual(request["declared_non_claims"], declared["declared_non_claims"])

        selected_evidence = result["selected_carrier_evidence"]
        self.assertEqual(2, len(selected_evidence))
        blocked, successful = selected_evidence
        self.assertEqual("returned-refusal-evidence", blocked["evidence_id"])
        self.assertEqual("BLOCKED", blocked["evidence_outcome"])
        self.assertEqual("carrier-b", blocked["carrier_id"])
        self.assertEqual("REFUSING_CARRIER", blocked["carrier_role"])
        self.assertEqual("RETURNED_BLOCKED_RECEIPT_EVIDENCE", blocked["evidence_class"])
        self.assertEqual("RECEIPT_BLOCK", blocked["emission_class"])
        self.assertEqual("returned/blocked.json", blocked["return_path"])
        self.assertEqual("BLOCKED_RECEIPT", blocked["block_code"])
        self.assertTrue(blocked["refusal_or_blocked_outcome"])
        self.assertEqual("returned-success-evidence", successful["evidence_id"])
        self.assertEqual("CARRIED_SURFACE_RECEIVED", successful["evidence_outcome"])
        self.assertTrue(successful["received_or_success_outcome"])
        self.assertEqual("CARRIER_DIVERGENCE_RECORDED", successful["divergence_status"])
        self.assertEqual("CURRENTNESS_PARTICIPATION_ELIGIBLE", successful["currentness_participation_status"])
        self.assertEqual("c" * 64, successful["integrity_hash"])
        self.assertEqual(resolver.REQUIRED_NON_CLAIMS, successful["non_claims"])

        basis = result["relation_basis"]
        self.assertEqual("REFUSAL_SUCCESS_RELATION", basis["relation_type"])
        self.assertEqual(sorted(resolver.SUPPORTED_RELATION_TYPES), basis["supported_relation_types"])
        self.assertEqual(["carrier-a", "carrier-b"], basis["selected_carrier_ids"])
        self.assertEqual(["returned-refusal-evidence", "returned-success-evidence"], basis["selected_evidence_ids"])
        self.assertEqual(["BLOCKED", "CARRIED_SURFACE_RECEIVED"], basis["selected_evidence_outcomes"])
        self.assertEqual(request["lineage_basis"], basis["lineage_basis"])
        self.assertEqual(request["selected_admission_basis"], basis["selected_admission_basis"])
        self.assertEqual(request["selected_correspondence_basis"], basis["selected_correspondence_basis"])
        self.assertEqual(request["selected_divergence_basis"], basis["selected_divergence_basis"])
        self.assertEqual(request["selected_currentness_basis"], basis["selected_currentness_basis"])
        self.assertTrue(basis["visible_divergence_remains_visible"])
        self.assertFalse(basis["hidden_divergence"])
        self.assertFalse(basis["refusal_hidden"])
        self.assertTrue(basis["relation_does_not_create_source_replacement"])
        self.assertTrue(basis["relation_does_not_create_currentness"])
        self.assertTrue(basis["relation_does_not_create_authority"])
        self.assertTrue(basis["relation_does_not_create_permission"])
        self.assertTrue(basis["relation_does_not_create_carrier_hierarchy"])
        self.assertTrue(basis["relation_does_not_create_distributed_standing"])
        self.assertTrue(basis["relation_does_not_authorize_continuation"])

        self._assert_checks_well_formed(result, all_pass=True)

        relation = result["relation_result"]
        self.assertTrue(relation["multi_carrier_relation_recognized"])
        self.assertFalse(relation["no_multi_carrier_relation"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", relation["relation_type"])
        self.assertTrue(relation["relation_claim"])
        self.assertEqual(2, relation["selected_carrier_count"])
        self.assertEqual(2, relation["selected_evidence_count"])
        self.assertEqual(["carrier-a", "carrier-b"], relation["selected_carrier_ids"])
        self.assertEqual(["returned-refusal-evidence", "returned-success-evidence"], relation["selected_evidence_ids"])
        self.assertEqual(["BLOCKED", "CARRIED_SURFACE_RECEIVED"], relation["selected_evidence_outcomes"])
        self.assertTrue(relation["relation_evidence"]["has_refusal_evidence"])
        self.assertTrue(relation["relation_evidence"]["has_success_evidence"])
        self.assertTrue(relation["carrier_roles_preserved"])
        self.assertTrue(relation["evidence_identities_preserved"])
        self.assertTrue(relation["local_outcomes_preserved"])
        self.assertTrue(relation["return_admission_divergence_currentness_participation_distinctions_preserved"])
        self.assertTrue(relation["visible_refusal_preserved"])
        self.assertTrue(relation["visible_divergence_preserved"])
        self.assertTrue(relation["downstream_evidence_posture_preserved"])
        self.assertTrue(relation["carriers_not_merged"])
        self.assertTrue(relation["evidence_not_merged_into_source"])
        self.assertTrue(relation["current_carrier_not_selected"])
        self.assertFalse(relation["winning_carrier_selected"])
        self.assertFalse(relation["losing_carrier_invalidated"])
        self.assertTrue(relation["source_not_replaced"])
        self.assertTrue(relation["currentness_not_created"])
        self.assertTrue(relation["authority_not_created"])
        self.assertTrue(relation["permission_not_created"])
        self.assertTrue(relation["carrier_hierarchy_not_created"])
        self.assertTrue(relation["distributed_standing_not_created"])
        self.assertTrue(relation["truth_not_created"])
        self.assertTrue(relation["action_not_authorized"])
        self.assertTrue(relation["continuation_not_authorized"])

        for key in RELATION_NON_MEANING_TRUE_KEYS:
            self.assertIs(result["relation_non_meaning"][key], True, key)

        consequence = result["relation_consequence_boundary"]
        for key in (
            "permit_selected_surfaces_as_bounded_relation_set",
            "preserve_visible_relation_posture",
            "support_later_relation_conformance",
            "support_later_closure_if_conformance_passes",
            "support_later_currentness_review_only_if_separately_admitted",
            "preserve_visible_divergence_as_part_of_relation",
        ):
            self.assertIs(consequence["relation_may"][key], True, key)
        for key in (
            "decide_source",
            "decide_currentness",
            "decide_truth",
            "decide_action",
            "select_winning_carrier",
            "erase_losing_carrier_evidence",
            "create_carrier_hierarchy",
            "create_distributed_standing",
            "create_carrier_registry",
            "create_synchronization",
            "authorize_continuation",
        ):
            self.assertIs(consequence["relation_may_not"][key], True, key)

        open_boundary = result["what_remains_open"]
        self.assertEqual(OPEN_SURFACES, {item["name"] for item in open_boundary["open_items"]})
        for item in open_boundary["open_items"]:
            self.assertFalse(item["scheduled"])
            self.assertFalse(item["authorized"])
            self.assertFalse(item["executed"])
        self.assertTrue(open_boundary["open_means_not_scheduled"])
        self.assertTrue(open_boundary["open_means_not_authorized"])
        self.assertTrue(open_boundary["open_means_not_executed"])
        self._assert_false_non_claims(result)

    def test_selected_carriers_are_preserved_and_summary_is_bounded(self) -> None:
        request = _request(
            relation_type="SOURCE_RECEIVER_RELATION",
            carriers=[
                _carrier("carrier-a", role="SOURCE_CARRIER_FOR_PACKET", label="source-carrier"),
                _carrier("carrier-b", role="RECEIVING_CARRIER", label="receiving-carrier"),
            ],
            evidence=[
                _evidence("source-side-evidence", carrier_id="carrier-a", carrier_role="SOURCE_CARRIER_FOR_PACKET"),
                _evidence("receiving-side-evidence", carrier_id="carrier-b", carrier_role="RECEIVING_CARRIER"),
            ],
        )

        result = self._resolve(request)

        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", result["outcome"])
        selected_carriers = result["selected_carriers"]
        self.assertEqual(2, len(selected_carriers))
        self.assertEqual("carrier-a", selected_carriers[0]["carrier_id"])
        self.assertEqual("source-carrier", selected_carriers[0]["carrier_label"])
        self.assertEqual("SOURCE_CARRIER_FOR_PACKET", selected_carriers[0]["carrier_role"])
        self.assertTrue(selected_carriers[0]["role_declared"])
        self.assertTrue(selected_carriers[0]["role_bounded"])
        self.assertEqual("carrier-b", selected_carriers[1]["carrier_id"])
        self.assertEqual("RECEIVING_CARRIER", selected_carriers[1]["carrier_role"])
        self.assertTrue(result["relation_result"]["source_not_replaced"])
        self.assertTrue(result["relation_result"]["currentness_not_created"])
        self.assertTrue(result["relation_result"]["authority_not_created"])

        summary = resolver.build_multi_carrier_relation_summary(result)
        self.assertEqual(result["multi_carrier_relation_summary"], summary)
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("relation-request-001", summary["relation_request_id"])
        self.assertEqual(request["relation_question"], summary["relation_question"])
        self.assertEqual("SOURCE_RECEIVER_RELATION", summary["relation_type"])
        self.assertTrue(summary["relation_recognized"])
        self.assertFalse(summary["no_relation"])
        self.assertEqual(2, summary["selected_carrier_count"])
        self.assertEqual(2, summary["selected_evidence_count"])
        self.assertEqual(["carrier-a", "carrier-b"], summary["selected_carrier_ids"])
        self.assertEqual(["source-side-evidence", "receiving-side-evidence"], summary["selected_evidence_ids"])
        self.assertEqual(["CARRIED_SURFACE_RECEIVED", "CARRIED_SURFACE_RECEIVED"], summary["selected_evidence_outcomes"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["carrier_roles_preserved"])
        self.assertTrue(summary["evidence_identities_preserved"])
        self.assertTrue(summary["local_outcomes_preserved"])
        self.assertTrue(summary["visible_divergence_preserved"])
        self.assertTrue(summary["downstream_evidence_posture_preserved"])
        self.assertTrue(summary["current_carrier_not_selected"])
        self.assertFalse(summary["winning_carrier_selected"])
        self.assertFalse(summary["losing_carrier_invalidated"])
        self.assertFalse(summary["source_currentness_authority_permission_created"])
        self.assertFalse(summary["carrier_hierarchy_created"])
        self.assertFalse(summary["distributed_standing_created"])
        self.assertFalse(summary["presence_threshold_truth_action_consequence_created"])
        self.assertFalse(summary["continuation_authorized"])
        self.assertEqual(resolver.REQUIRED_NON_CLAIMS["authority_created"], summary["key_non_claims"]["authority_created"])

    def test_relation_types_are_recognized_and_no_relation_is_distinct(self) -> None:
        cases = {
            "SOURCE_RECEIVER_RELATION": _request(
                relation_type="SOURCE_RECEIVER_RELATION",
                evidence=[
                    _evidence("source-role-evidence", carrier_id="carrier-a", carrier_role="SOURCE_CARRIER_FOR_PACKET"),
                    _evidence("receiver-role-evidence", carrier_id="carrier-b", carrier_role="RECEIVING_CARRIER"),
                ],
            ),
            "RECEIPT_RETURN_RELATION": _request(
                relation_type="RECEIPT_RETURN_RELATION",
                evidence=[
                    _evidence("receipt-evidence", outcome="CARRIED_SURFACE_RECEIVED"),
                    _evidence("returned-evidence", evidence_class="RETURNED_RECEIPT_EVIDENCE", return_path="returned/receipt.json"),
                ],
            ),
            "ADMITTED_EVIDENCE_RELATION": _request(
                relation_type="ADMITTED_EVIDENCE_RELATION",
                evidence=[
                    _evidence("admitted-evidence", admission_status="CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE"),
                    _evidence("basis-evidence", admission_status="ADMITTED_AS_EVIDENCE"),
                ],
            ),
            "DIVERGENCE_BOUNDED_RELATION": _request(
                relation_type="DIVERGENCE_BOUNDED_RELATION",
                evidence=[
                    _evidence("divergence-result", outcome="CARRIER_DIVERGENCE_RECORDED", evidence_class="CARRIER_DIVERGENCE_RESULT"),
                    _evidence("divergence-related-evidence"),
                ],
            ),
            "CURRENTNESS_PARTICIPATION_RELATION": _request(
                relation_type="CURRENTNESS_PARTICIPATION_RELATION",
                evidence=[
                    _evidence("currentness-participation", outcome="CURRENTNESS_PARTICIPATION_ELIGIBLE"),
                    _evidence("participation-basis-evidence"),
                ],
            ),
            "ROLE_EMISSION_RELATION": _request(
                relation_type="ROLE_EMISSION_RELATION",
                evidence=[
                    _evidence("role-emission-evidence", carrier_role="RECEIVING_CARRIER", emission_class="CARRIED_SURFACE_RECEIPT"),
                    _evidence("role-emission-basis", carrier_role="RETURNING_CARRIER", emission_class="RETURNED_RECEIPT_EVIDENCE"),
                ],
            ),
            "CARRIER_EVIDENCE_SET_RELATION": _request(
                relation_type="CARRIER_EVIDENCE_SET_RELATION",
                evidence=[
                    _evidence("set-evidence-a", basis_id="shared-basis"),
                    _evidence("set-evidence-b", basis_id="shared-basis"),
                ],
            ),
        }
        for relation_type, request in cases.items():
            with self.subTest(relation_type=relation_type):
                result = self._resolve(request)
                self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", result["outcome"])
                self.assertEqual(relation_type, result["relation_result"]["relation_type"])
                self.assertTrue(result["relation_result"]["multi_carrier_relation_recognized"])
                self.assertTrue(result["relation_result"]["currentness_not_created"])
                self.assertTrue(result["relation_result"]["distributed_standing_not_created"])

        no_relation = self._resolve(_request(relation_type="NO_MULTI_CARRIER_RELATION"))
        self.assertEqual("NO_MULTI_CARRIER_RELATION", no_relation["outcome"])
        self.assertTrue(no_relation["relation_result"]["no_multi_carrier_relation"])
        self.assertTrue(no_relation["relation_result"]["no_collapse_flags_true"])
        self._assert_false_non_claims(no_relation)

        unsupported_basis = self._resolve(
            _request(
                relation_type="CURRENTNESS_PARTICIPATION_RELATION",
                extra={"selected_currentness_basis": None},
                evidence=[
                    _evidence(
                        "plain-evidence-a",
                        outcome="CARRIED_SURFACE_RECEIVED",
                        evidence_class="RECEIPT_EVIDENCE",
                        emission_class=None,
                        admission_status=None,
                        correspondence_status=None,
                        divergence_status=None,
                        currentness_participation_status=None,
                    ),
                    _evidence(
                        "plain-evidence-b",
                        outcome="CARRIED_SURFACE_RECEIVED",
                        evidence_class="RECEIPT_EVIDENCE",
                        emission_class=None,
                        admission_status=None,
                        correspondence_status=None,
                        divergence_status=None,
                        currentness_participation_status=None,
                    ),
                ],
            )
        )
        self.assertEqual("NO_MULTI_CARRIER_RELATION", unsupported_basis["outcome"])
        self.assertIsNone(unsupported_basis["block"]["code"])
        self.assertFalse(unsupported_basis["relation_result"]["multi_carrier_relation_recognized"])
        self.assertEqual("selected carriers or evidence do not support declared relation type", unsupported_basis["relation_result"]["no_relation_reason"])

    def test_builder_path_write_default_write_and_non_mutation(self) -> None:
        evidence = _refusal_success_evidence()
        carriers = [
            _carrier("carrier-a", role="SOURCE_CARRIER_FOR_PACKET"),
            _carrier("carrier-b", role="RECEIVING_CARRIER"),
        ]
        built = resolver.build_declared_relation_request(
            "builder-relation-001",
            "Can helper-built selected evidence stand in bounded relation?",
            "REFUSAL_SUCCESS_RELATION",
            evidence,
            selected_carriers=carriers,
        )
        self.assertEqual("builder-relation-001", built["relation_request_id"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", built["relation_type"])
        self.assertEqual(evidence, built["selected_carrier_evidence"])
        self.assertEqual(carriers, built["selected_carriers"])
        self.assertEqual(resolver.REQUIRED_NON_CLAIMS, built["declared_non_claims"])

        original = copy.deepcopy(built)
        first = self._resolve(built)
        second = self._resolve(built)
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", first["outcome"])
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", second["outcome"])
        self.assertEqual(original, built)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            request_path = root / "request.json"
            _write_json(request_path, built)
            path_result = resolver.resolve_multi_carrier_relation_boundary_from_path(request_path)
            self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", path_result["outcome"])
            self.assertEqual(TOP_LEVEL_SECTIONS, set(path_result))
            self.assertEqual(str(request_path), path_result["declared_relation_question"]["declared_relation_request_path"])

            explicit_path = root / "nested" / "relation-result.json"
            written = resolver.write_multi_carrier_relation_result(path_result, explicit_path)
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            self.assertEqual(TOP_LEVEL_SECTIONS, set(_read_json(written)))

            with mock.patch.object(resolver, "MULTI_CARRIER_RELATION_BOUNDARY_ROOT", root / "default-output"):
                first_default = resolver.write_multi_carrier_relation_result(path_result)
                second_default = resolver.write_multi_carrier_relation_result(path_result)
            self.assertTrue(first_default.exists())
            self.assertTrue(second_default.exists())
            self.assertNotEqual(first_default, second_default)
            self.assertTrue(first_default.name.startswith("builder-relation-001__cross") is False)
            self.assertIn("builder-relation-001__multi_carrier_relation_result", first_default.name)
            self.assertRegex(second_default.stem, r"_001$")

    def test_missing_malformed_and_required_basis_blocks(self) -> None:
        missing = resolver.resolve_multi_carrier_relation_boundary()
        self._assert_block_code(missing, "DECLARED_RELATION_REQUEST_MISSING")
        malformed = resolver.resolve_multi_carrier_relation_boundary("not-a-mapping")  # type: ignore[arg-type]
        self._assert_block_code(malformed, "DECLARED_RELATION_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            unreadable = resolver.resolve_multi_carrier_relation_boundary_from_path(root / "missing.json")
            self._assert_block_code(unreadable, "DECLARED_RELATION_REQUEST_UNREADABLE")
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            self._assert_block_code(resolver.resolve_multi_carrier_relation_boundary_from_path(malformed_path), "DECLARED_RELATION_REQUEST_MALFORMED")
            array_path = root / "array.json"
            _write_json(array_path, [{"not": "a mapping"}])
            self._assert_block_code(resolver.resolve_multi_carrier_relation_boundary_from_path(array_path), "DECLARED_RELATION_REQUEST_MALFORMED")

        block_cases = [
            (
                "RELATION_QUESTION_UNDECLARED",
                _request(relation_question=""),
            ),
            (
                "INSUFFICIENT_SELECTED_CARRIERS_OR_EVIDENCE",
                _request(carriers=[], evidence=[]),
            ),
            (
                "SELECTED_CARRIER_EVIDENCE_MISSING",
                _request(include_carriers=False, include_evidence=False),
            ),
            (
                "SELECTED_CARRIER_EVIDENCE_MALFORMED",
                _request(include_carriers=False, evidence=["not-a-mapping"]),
            ),
            (
                "EVIDENCE_IDENTITY_MISSING",
                _request(evidence=[{**_evidence("ok-a"), "evidence_id": None}, _evidence("ok-b")]),
            ),
            (
                "EVIDENCE_OUTCOME_MISSING",
                _request(evidence=[{**_evidence("ok-a"), "evidence_outcome": None}, _evidence("ok-b")]),
            ),
            (
                "CARRIER_IDENTITY_MISSING",
                _request(
                    evidence=[
                        {
                            **_evidence("ok-a"),
                            "carrier_id": None,
                            "source_carrier_id": None,
                            "receiving_carrier_id": None,
                        },
                        _evidence("ok-b"),
                    ]
                ),
            ),
            (
                "CARRIER_ROLE_UNSUPPORTED",
                _request(evidence=[{**_evidence("ok-a"), "carrier_role": "SUCCESSOR_CARRIER"}, _evidence("ok-b")]),
            ),
            (
                "RELATION_TYPE_UNSUPPORTED",
                _request(relation_type="UNSUPPORTED_RELATION"),
            ),
        ]
        for expected, request in block_cases:
            with self.subTest(block_code=expected):
                result = self._resolve(request)
                self._assert_block_code(result, expected)
                self._assert_false_non_claims(result)

    def test_collapse_shaped_relation_requests_block_with_specific_codes(self) -> None:
        cases = [
            ("divergence_hidden", "RELATION_HIDES_DIVERGENCE"),
            ("refusal_hidden", "RELATION_HIDES_REFUSAL"),
            ("mismatch_hidden", "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("evidence_overwritten", "RELATION_OVERWRITES_EVIDENCE"),
            ("mutation_performed", "RELATION_MUTATES_OR_REPLAYS_EVIDENCE"),
            ("replay_performed", "RELATION_MUTATES_OR_REPLAYS_EVIDENCE"),
            ("merge_performed", "RELATION_MUTATES_OR_REPLAYS_EVIDENCE"),
            ("evidence_merged_into_source", "RELATION_REPLACES_SOURCE"),
            ("source_replaced", "RELATION_REPLACES_SOURCE"),
            ("currentness_created", "RELATION_CREATES_CURRENTNESS"),
            ("authority_created", "RELATION_CREATES_AUTHORITY"),
            ("permission_created", "RELATION_CREATES_PERMISSION"),
            ("carrier_relation_created_successor", "RELATION_CREATES_SUCCESSOR"),
            ("carrier_relation_created_body", "RELATION_CREATES_BODY"),
            ("carrier_relation_created_hierarchy", "RELATION_CREATES_CARRIER_HIERARCHY"),
            ("winning_carrier_selected", "RELATION_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "RELATION_INVALIDATES_LOSING_CARRIER"),
            ("signal_created_by_default", "RELATION_CREATES_SIGNAL_BY_DEFAULT"),
            ("presence_established", "RELATION_ESTABLISHES_PRESENCE"),
            ("threshold_met", "RELATION_ESTABLISHES_THRESHOLD"),
            ("truth_created", "RELATION_CREATES_TRUTH"),
            ("action_authorized", "RELATION_AUTHORIZES_ACTION"),
            ("consequence_created", "RELATION_CREATES_CONSEQUENCE"),
            ("distributed_standing_created", "RELATION_CREATES_DISTRIBUTED_STANDING"),
            ("continuation_authorized", "RELATION_AUTHORIZES_CONTINUATION"),
            ("divergence_resolved_by_majority", "RELATION_RESOLVES_DIVERGENCE_BY_MAJORITY"),
            ("divergence_resolved_by_latest_file", "RELATION_RESOLVES_DIVERGENCE_BY_LATEST_FILE"),
            ("divergence_resolved_by_success_count", "RELATION_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT"),
            ("latest_file_currentness", "LATEST_FILE_CURRENTNESS"),
            ("recency_fraud", "LATEST_FILE_CURRENTNESS"),
        ]
        for flag, expected in cases:
            with self.subTest(flag=flag, block_code=expected):
                result = self._resolve(_request(non_claims=_false_non_claims(**{flag: True})))
                self._assert_block_code(result, expected)
                self.assertIn("declared_non_claims_where_available", result["relation_result"])
                self._assert_false_non_claims(result)

        missing_non_claims = _false_non_claims()
        missing_non_claims.pop("authority_created")
        result = self._resolve(_request(non_claims=missing_non_claims))
        self._assert_block_code(result, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertEqual("missing", result["relation_checks"][-1]["actual_posture"]["declared_non_claim_failures"]["authority_created"])

        selected_conflict = _request(
            evidence=[
                _evidence("selected-collapse-a", non_claims=_false_non_claims(mismatch_hidden=True)),
                _evidence("selected-collapse-b"),
            ]
        )
        selected_result = self._resolve(selected_conflict)
        self._assert_block_code(selected_result, "NON_CLAIM_MISSING_OR_FLIPPED")


if __name__ == "__main__":
    unittest.main()
