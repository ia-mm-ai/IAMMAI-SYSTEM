"""Tests for the bounded carrier lifecycle boundary resolver.

This suite audits lifecycle posture only. It does not create registry state,
persistence, currentness, distributed standing, synchronization, full body
transfer, or physical carrier execution.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_carrier_lifecycle_boundary as lifecycle  # noqa: E402


TOP_LEVEL_SECTIONS = {
    "carrier_lifecycle_metadata",
    "declared_lifecycle_question",
    "selected_carrier",
    "prior_lifecycle_status",
    "requested_lifecycle_status",
    "lifecycle_basis",
    "related_carrier_evidence",
    "lifecycle_transition",
    "lifecycle_checks",
    "lifecycle_statement",
    "lifecycle_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "carrier_lifecycle_summary",
}

SUPPORTED_STATUSES = [
    "CARRIER_CANDIDATE",
    "CARRIER_DECLARED_FOR_EXPERIMENT",
    "CARRIER_ACTIVE_FOR_OPERATION",
    "CARRIER_HOLDING_EVIDENCE",
    "CARRIER_RETURNED_EVIDENCE",
    "CARRIER_REFUSED_OR_BLOCKED",
    "CARRIER_UNAVAILABLE",
    "CARRIER_STALE",
    "CARRIER_CORRUPTED",
    "CARRIER_WITHDRAWN",
    "CARRIER_REPLACED",
    "CARRIER_REINTRODUCTION_CANDIDATE",
    "CARRIER_REINTRODUCED",
    "CARRIER_RETIRED",
    "CARRIER_LIFECYCLE_BLOCKED",
]

SUPPORTED_OUTCOMES = {
    "CARRIER_LIFECYCLE_STATUS_RECORDED",
    "CARRIER_LIFECYCLE_STATUS_NOT_RECORDED",
    "CARRIER_LIFECYCLE_STATUS_BLOCKED",
}


def _non_claims() -> dict[str, bool]:
    return copy.deepcopy(lifecycle.REQUIRED_NON_CLAIMS)


def _related_evidence() -> list[dict[str, object]]:
    return [
        {
            "evidence_id": "carrier_C_returned_blocked_receipt_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "RECEIPT_BLOCK",
            "basis": "Carrier C returned blocked receipt evidence remains visible.",
            "evidence_remains_evidence": True,
        },
        {
            "evidence_id": "carrier_B_C_visible_divergence_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
            "basis": "B/C divergence remains visible and unresolved.",
            "visible_divergence_preserved": True,
        },
        {
            "evidence_id": "carrier_C_currentness_participation_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
            "basis": "Carrier C currentness posture remains participation only.",
            "currentness_created": False,
        },
    ]


def _valid_request(
    *,
    status: str = "CARRIER_REFUSED_OR_BLOCKED",
    intent: str = "RECORD_CARRIER_LIFECYCLE_STATUS",
    prior: str | None = None,
    transition_basis: object | None = None,
    related_evidence: object | None = None,
) -> dict[str, object]:
    request: dict[str, object] = {
        "lifecycle_request_id": "carrier_C_lifecycle_refused_or_blocked_001",
        "lifecycle_question": "What lifecycle posture may be recorded for Carrier C?",
        "lifecycle_intent": intent,
        "selected_carrier": {
            "carrier_id": "carrier_C_additional_physical_candidate",
            "carrier_label": "Carrier C",
            "carrier_identity_preserved": True,
            "lifecycle_participant_not_body_participant": True,
        },
        "requested_lifecycle_status": status,
        "lifecycle_basis": {
            "lifecycle_basis_id": "carrier_C_returned_blocked_receipt_basis",
            "basis": "Carrier C returned blocked receipt evidence is preserved as evidence only.",
            "selected_evidence_refs": [
                "carrier_C_returned_blocked_receipt_evidence",
                "carrier_B_C_visible_divergence_evidence",
                "carrier_C_currentness_participation_evidence",
            ],
            "carrier_convenience_used": False,
            "latest_file_currentness": False,
            "prior_evidence_erased": False,
        },
        "related_carrier_evidence": _related_evidence()
        if related_evidence is None
        else related_evidence,
        "visible_refusal_basis": {
            "visible_refusal_preserved": True,
            "basis": "Carrier C blocked receipt remains visible.",
        },
        "visible_divergence_basis": {
            "visible_divergence_preserved": True,
            "basis": "B/C divergence remains visible.",
        },
        "visible_corruption_basis": {
            "visible_corruption_preserved": True,
            "basis": "No corruption is hidden by lifecycle status.",
        },
        "visible_staleness_basis": {
            "visible_staleness_preserved": True,
            "basis": "No staleness is hidden by lifecycle status.",
        },
        "selected_experiment_basis": {
            "basis_id": "additional_physical_carrier_experiment_boundary",
            "does_not_create_lifecycle_registry": True,
        },
        "selected_relation_basis": {
            "basis_id": "carrier_B_C_divergence_bounded_relation",
            "relation_remains_downstream": True,
        },
        "selected_currentness_basis": {
            "basis_id": "carrier_C_currentness_participation",
            "participation_only": True,
        },
        "selected_admission_basis": {
            "basis_id": "carrier_C_returned_blocked_evidence_admission",
            "admission_as_evidence_only": True,
        },
        "declared_non_claims": _non_claims(),
    }
    if prior is not None:
        request["prior_lifecycle_status"] = prior
    if transition_basis is not None:
        request["transition_basis"] = transition_basis
        request["lifecycle_transition"] = {
            "prior_lifecycle_status": prior,
            "requested_lifecycle_status": status,
            "transition_basis": transition_basis,
        }
    return request


class CarrierLifecycleBoundaryTests(unittest.TestCase):
    def assert_bounded_shape(self, result: dict[str, object]) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertIn(result["outcome"], SUPPORTED_OUTCOMES)

    def assert_all_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in lifecycle.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_block_code(self, request: object, expected_code: str) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(request)  # type: ignore[arg-type]
        self.assert_bounded_shape(result)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_BLOCKED", result["outcome"])
        self.assertEqual(expected_code, result["block"]["block_code"])
        self.assert_all_non_claims_false(result)

    def test_successful_lifecycle_status_recording(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())

        self.assert_bounded_shape(result)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["carrier_lifecycle_summary"]["failed_check_count"])

        statement = result["lifecycle_statement"]
        self.assertIs(statement["carrier_lifecycle_status_recorded"], True)
        self.assertIs(statement["carrier_identity_preserved"], True)
        self.assertIs(statement["requested_lifecycle_status_preserved"], True)
        self.assertIs(statement["lifecycle_basis_preserved"], True)
        self.assertIs(statement["prior_evidence_erased"], False)
        self.assertIs(statement["source_replaced"], False)
        self.assertIs(statement["currentness_created"], False)
        self.assertIs(statement["authority_created"], False)
        self.assertIs(statement["permission_created"], False)
        self.assertIs(statement["carrier_hierarchy_created"], False)
        self.assertIs(statement["distributed_standing_created"], False)
        self.assertIs(statement["carrier_registry_created"], False)
        self.assertIs(statement["repository_synchronization_authorized"], False)
        self.assertIs(statement["full_body_transfer_authorized"], False)
        self.assertIs(statement["continuation_authorized"], False)
        self.assertIs(statement["distributed_operation_authorized"], False)

    def test_metadata(self) -> None:
        metadata = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())[
            "carrier_lifecycle_metadata"
        ]

        self.assertTrue(metadata["carrier_lifecycle_result_id"])
        self.assertTrue(metadata["carrier_lifecycle_result_type"])
        self.assertEqual("0.1.0", metadata["carrier_lifecycle_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual("resolve_carrier_lifecycle_boundary", metadata["resolver_module"])

    def test_declared_lifecycle_question(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        question = result["declared_lifecycle_question"]

        self.assertEqual(
            "carrier_C_lifecycle_refused_or_blocked_001",
            question["lifecycle_request_id"],
        )
        self.assertEqual(
            "What lifecycle posture may be recorded for Carrier C?",
            question["lifecycle_question"],
        )
        self.assertEqual("RECORD_CARRIER_LIFECYCLE_STATUS", question["lifecycle_intent"])
        self.assertIsInstance(question["declared_non_claims"], dict)
        self.assertIs(question["lifecycle_is_not_registry"], True)
        self.assertIs(question["lifecycle_is_not_currentness"], True)
        self.assertIs(question["lifecycle_is_not_distributed_standing"], True)
        self.assertEqual(
            "carrier_C_additional_physical_candidate",
            result["selected_carrier"]["selected_carrier_id"],
        )
        self.assertEqual(
            "CARRIER_REFUSED_OR_BLOCKED",
            result["requested_lifecycle_status"]["requested_lifecycle_status"],
        )

    def test_selected_carrier(self) -> None:
        selected = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())[
            "selected_carrier"
        ]

        self.assertEqual("carrier_C_additional_physical_candidate", selected["selected_carrier_id"])
        self.assertEqual("Carrier C", selected["raw_selected_carrier"]["carrier_label"])
        self.assertIs(selected["carrier_identity_declared"], True)
        self.assertIs(selected["lifecycle_participant_not_body_participant"], True)
        self.assertIs(selected["lifecycle_status_does_not_make_carrier_current"], True)
        self.assertIs(selected["lifecycle_status_does_not_create_carrier_hierarchy"], True)

    def test_prior_lifecycle_status(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(
                status="CARRIER_REFUSED_OR_BLOCKED",
                prior="CARRIER_ACTIVE_FOR_OPERATION",
                transition_basis={"basis": "Carrier C returned blocked receipt."},
            )
        )

        prior = result["prior_lifecycle_status"]
        statement = result["lifecycle_statement"]
        self.assertEqual("CARRIER_ACTIVE_FOR_OPERATION", prior["prior_lifecycle_status"])
        self.assertIs(prior["prior_lifecycle_status_preserved"], True)
        self.assertIs(statement["prior_lifecycle_status_preserved"], True)
        self.assertIs(statement["prior_evidence_erased"], False)
        self.assertIs(statement["currentness_created"], False)
        self.assertIs(statement["carrier_registry_created"], False)

    def test_requested_lifecycle_status(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        requested = result["requested_lifecycle_status"]
        non_meaning = result["lifecycle_non_meaning"]

        self.assertEqual("CARRIER_REFUSED_OR_BLOCKED", requested["requested_lifecycle_status"])
        self.assertIs(requested["requested_lifecycle_status_supported"], True)
        self.assertIs(non_meaning["does_not_mean_currentness"], True)
        self.assertIs(non_meaning["does_not_mean_authority"], True)
        self.assertIs(non_meaning["does_not_mean_carrier_registry"], True)
        self.assertIs(non_meaning["does_not_mean_distributed_standing"], True)

    def test_lifecycle_basis(self) -> None:
        basis = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())[
            "lifecycle_basis"
        ]

        self.assertIs(basis["lifecycle_basis_declared"], True)
        self.assertIs(basis["lifecycle_basis_preserved"], True)
        self.assertIn("selected_evidence_refs", basis["raw_lifecycle_basis"])
        self.assertIs(basis["visible_refusal_preserved"], True)
        self.assertIs(basis["visible_divergence_preserved"], True)
        self.assertIs(basis["visible_corruption_preserved"], True)
        self.assertIs(basis["visible_staleness_preserved"], True)
        self.assertIs(basis["raw_lifecycle_basis"]["latest_file_currentness"], False)
        self.assertIs(basis["raw_lifecycle_basis"]["carrier_convenience_used"], False)
        self.assertIs(basis["raw_lifecycle_basis"]["prior_evidence_erased"], False)

    def test_related_carrier_evidence(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        related = result["related_carrier_evidence"]
        statement = result["lifecycle_statement"]

        self.assertEqual(
            [
                "carrier_C_returned_blocked_receipt_evidence",
                "carrier_B_C_visible_divergence_evidence",
                "carrier_C_currentness_participation_evidence",
            ],
            related["related_evidence_ids"],
        )
        self.assertIn("RECEIPT_BLOCK", related["related_evidence_outcomes"])
        self.assertEqual(
            "carrier_C_additional_physical_candidate",
            related["related_evidence_entries"][0]["carrier_id"],
        )
        self.assertIs(statement["visible_refusal_preserved"], True)
        self.assertIs(statement["visible_divergence_preserved"], True)
        self.assertIs(statement["currentness_created"], False)
        self.assertIs(statement["carrier_hierarchy_created"], False)

    def test_lifecycle_transition(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(
                status="CARRIER_REFUSED_OR_BLOCKED",
                prior="CARRIER_ACTIVE_FOR_OPERATION",
                transition_basis={"basis": "Carrier C produced visible blocked receipt."},
            )
        )
        transition = result["lifecycle_transition"]

        self.assertEqual("CARRIER_ACTIVE_FOR_OPERATION", transition["prior_lifecycle_status"])
        self.assertEqual("CARRIER_REFUSED_OR_BLOCKED", transition["requested_lifecycle_status"])
        self.assertIs(transition["transition_basis_preserved"], True)
        self.assertIs(transition["transition_supported"], True)
        self.assertIs(transition["transition_preserves_previous_status"], True)
        self.assertIs(transition["transition_preserves_new_status"], True)
        self.assertIs(transition["transition_does_not_erase_evidence"], True)
        self.assertIs(
            transition["transition_does_not_create_source_currentness_authority_permission"],
            True,
        )

    def test_lifecycle_checks(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(
                status="CARRIER_REFUSED_OR_BLOCKED",
                prior="CARRIER_ACTIVE_FOR_OPERATION",
                transition_basis={"basis": "Visible blocked receipt."},
            )
        )
        checks = result["lifecycle_checks"]
        names = {check["check_name"] for check in checks}

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True)
        self.assertEqual(0, result["carrier_lifecycle_summary"]["failed_check_count"])

        expected_names = {
            "lifecycle_question_declared",
            "lifecycle_intent_supported",
            "carrier_identity_declared",
            "requested_lifecycle_status_supported",
            "lifecycle_basis_declared",
            "transition_basis_supplied_where_required",
            "transition_supported_where_applicable",
            "prior_evidence_preserved",
            "visible_refusal_preserved_where_applicable",
            "visible_divergence_preserved_where_applicable",
            "visible_corruption_preserved_where_applicable",
            "visible_staleness_preserved_where_applicable",
            "no_evidence_erased",
            "no_refusal_hidden",
            "no_divergence_hidden",
            "no_corruption_hidden",
            "no_repair_by_overwrite",
            "no_source_replacement",
            "no_currentness",
            "no_authority",
            "no_permission",
            "no_carrier_hierarchy",
            "no_winning_carrier_selected",
            "no_losing_carrier_invalidated",
            "no_distributed_standing",
            "no_repository_synchronization",
            "no_full_body_transfer",
            "no_carrier_registry",
            "no_continuation",
            "no_distributed_operation",
            "no_latest_file_currentness",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_lifecycle_statement(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(
                status="CARRIER_STALE",
                prior="CARRIER_HOLDING_EVIDENCE",
                transition_basis={"basis": "Held evidence became stale."},
            )
        )
        statement = result["lifecycle_statement"]

        self.assertIs(statement["carrier_lifecycle_status_recorded"], True)
        self.assertIs(statement["carrier_identity_preserved"], True)
        self.assertIs(statement["requested_lifecycle_status_preserved"], True)
        self.assertIs(statement["prior_lifecycle_status_preserved"], True)
        self.assertIs(statement["lifecycle_basis_preserved"], True)
        self.assertIs(statement["transition_basis_preserved"], True)
        self.assertIs(statement["related_evidence_preserved"], True)
        self.assertIs(statement["visible_refusal_preserved"], True)
        self.assertIs(statement["visible_divergence_preserved"], True)
        self.assertIs(statement["visible_corruption_preserved"], True)
        self.assertIs(statement["visible_staleness_preserved"], True)
        for key in (
            "prior_evidence_erased",
            "source_replaced",
            "currentness_created",
            "authority_created",
            "permission_created",
            "carrier_hierarchy_created",
            "distributed_standing_created",
            "carrier_registry_created",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "continuation_authorized",
            "distributed_operation_authorized",
        ):
            self.assertIs(statement[key], False, key)

    def test_lifecycle_non_meaning(self) -> None:
        non_meaning = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())[
            "lifecycle_non_meaning"
        ]
        expected = {
            "does_not_mean_source_replacement",
            "does_not_mean_currentness",
            "does_not_mean_authority",
            "does_not_mean_permission_beyond_declared_lifecycle_review",
            "does_not_mean_carrier_hierarchy",
            "does_not_mean_carrier_priority",
            "does_not_mean_carrier_sovereignty",
            "does_not_mean_carrier_correctness",
            "does_not_mean_winning_carrier",
            "does_not_mean_losing_carrier_invalidated",
            "does_not_mean_evidence_erased",
            "does_not_mean_refusal_erased",
            "does_not_mean_divergence_resolved",
            "does_not_mean_distributed_standing",
            "does_not_mean_repository_synchronization",
            "does_not_mean_full_body_transfer",
            "does_not_mean_second_body",
            "does_not_mean_carrier_registry",
            "does_not_mean_persistence",
            "does_not_mean_signal_by_default",
            "does_not_mean_presence",
            "does_not_mean_threshold",
            "does_not_mean_truth",
            "does_not_mean_action",
            "does_not_mean_consequence",
            "does_not_mean_continuation",
            "does_not_mean_automatic_admission",
            "does_not_mean_automatic_relation",
            "does_not_mean_automatic_currentness",
            "does_not_mean_automatic_conformance",
            "does_not_mean_automatic_closure",
            "does_not_mean_distributed_operation",
        }
        for key in expected:
            self.assertIs(non_meaning[key], True, key)

    def test_what_remains_open(self) -> None:
        open_items = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())[
            "what_remains_open"
        ]
        expected = {
            "carrier_lifecycle_implementation_refinement",
            "carrier_registry_persistence_boundary",
            "standing_propagation_law",
            "cross_carrier_currentness_successor_law",
            "divergence_consequence_law",
            "distributed_standing_boundary",
            "distributed_standing",
            "persistence_registry_law",
            "presence_law",
            "threshold_law",
            "truth_law",
            "action_consequence_law",
            "generalized_vessel_relation_lifecycle",
            "body_relevance_medium",
            "signal_series_or_accumulation_logic",
            "successor_carrier_law",
            "future_self_orientation_successor_only_if_separately_justified",
            "distributed_operation_only_if_separately_declared_and_bounded",
            "open_means_not_scheduled",
            "open_means_not_authorized",
            "open_means_not_executed",
        }
        for key in expected:
            self.assertIs(open_items[key], True, key)

    def test_summary_helper(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(
                status="CARRIER_STALE",
                prior="CARRIER_HOLDING_EVIDENCE",
                transition_basis={"basis": "Held evidence became stale."},
            )
        )
        summary = lifecycle.build_carrier_lifecycle_summary(result)

        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("carrier_C_lifecycle_refused_or_blocked_001", summary["lifecycle_request_id"])
        self.assertEqual("What lifecycle posture may be recorded for Carrier C?", summary["lifecycle_question"])
        self.assertEqual("RECORD_CARRIER_LIFECYCLE_STATUS", summary["lifecycle_intent"])
        self.assertEqual("carrier_C_additional_physical_candidate", summary["selected_carrier_id"])
        self.assertEqual("CARRIER_HOLDING_EVIDENCE", summary["prior_lifecycle_status"])
        self.assertEqual("CARRIER_STALE", summary["requested_lifecycle_status"])
        self.assertIsInstance(summary["lifecycle_basis"], dict)
        self.assertIsInstance(summary["transition_basis"], dict)
        self.assertIn("carrier_C_returned_blocked_receipt_evidence", summary["related_evidence_ids"])
        self.assertIn("RECEIPT_BLOCK", summary["related_evidence_outcomes"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["lifecycle_status_recorded"], True)
        self.assertIs(summary["prior_evidence_erased"], False)
        self.assertIs(summary["visible_refusal_preserved"], True)
        self.assertIs(summary["visible_divergence_preserved"], True)
        self.assertIs(summary["visible_corruption_preserved"], True)
        self.assertIs(summary["visible_staleness_preserved"], True)
        self.assertIs(summary["no_source_currentness_authority_permission"], True)
        self.assertIs(summary["no_carrier_hierarchy"], True)
        self.assertIs(summary["no_winning_losing_carrier_collapse"], True)
        self.assertIs(summary["no_distributed_standing"], True)
        self.assertIs(summary["no_registry_sync_full_body_transfer"], True)
        self.assertIs(summary["no_continuation"], True)
        self.assertIs(summary["no_distributed_operation"], True)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        recorded = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        not_recorded = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(intent="DO_NOT_RECORD_CARRIER_LIFECYCLE_STATUS")
        )
        blocked = lifecycle.resolve_carrier_lifecycle_boundary(None)

        for result in (recorded, not_recorded, blocked):
            self.assert_all_non_claims_false(result)

    def test_supported_statuses_record(self) -> None:
        for status in SUPPORTED_STATUSES:
            with self.subTest(status=status):
                result = lifecycle.resolve_carrier_lifecycle_boundary(
                    _valid_request(status=status)
                )
                self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])
                self.assertEqual(status, result["requested_lifecycle_status"]["requested_lifecycle_status"])

    def test_supported_transitions_record(self) -> None:
        transitions = [
            ("CARRIER_CANDIDATE", "CARRIER_DECLARED_FOR_EXPERIMENT"),
            ("CARRIER_DECLARED_FOR_EXPERIMENT", "CARRIER_ACTIVE_FOR_OPERATION"),
            ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_RETURNED_EVIDENCE"),
            ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_REFUSED_OR_BLOCKED"),
            ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_UNAVAILABLE"),
            ("CARRIER_HOLDING_EVIDENCE", "CARRIER_STALE"),
            ("CARRIER_HOLDING_EVIDENCE", "CARRIER_CORRUPTED"),
            ("CARRIER_STALE", "CARRIER_REINTRODUCTION_CANDIDATE"),
            ("CARRIER_UNAVAILABLE", "CARRIER_REINTRODUCTION_CANDIDATE"),
            ("CARRIER_WITHDRAWN", "CARRIER_REINTRODUCTION_CANDIDATE"),
            ("CARRIER_REINTRODUCTION_CANDIDATE", "CARRIER_REINTRODUCED"),
            ("CARRIER_ACTIVE_FOR_OPERATION", "CARRIER_WITHDRAWN"),
            ("CARRIER_DECLARED_FOR_EXPERIMENT", "CARRIER_WITHDRAWN"),
        ]
        transitions.extend((status, "CARRIER_RETIRED") for status in SUPPORTED_STATUSES)
        transitions.extend((status, "CARRIER_REPLACED") for status in SUPPORTED_STATUSES)

        for prior, requested in transitions:
            with self.subTest(prior=prior, requested=requested):
                result = lifecycle.resolve_carrier_lifecycle_boundary(
                    _valid_request(
                        status=requested,
                        prior=prior,
                        transition_basis={"basis": f"{prior} to {requested}"},
                    )
                )
                self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])
                transition = result["lifecycle_transition"]
                self.assertIs(transition["transition_basis_preserved"], True)
                self.assertIs(transition["transition_supported"], True)
                self.assertIs(transition["transition_does_not_erase_evidence"], True)
                self.assertIs(transition["transition_does_not_create_distributed_standing"], True)

    def test_request_builder_helper(self) -> None:
        request = lifecycle.build_declared_carrier_lifecycle_request(
            "carrier_lifecycle_builder_001",
            "Can Carrier C be recorded as stale?",
            "carrier_C_additional_physical_candidate",
            "CARRIER_STALE",
            {"basis": "Held evidence became stale."},
            prior_lifecycle_status="CARRIER_HOLDING_EVIDENCE",
            transition_basis={"basis": "stale transition"},
            related_carrier_evidence=_related_evidence(),
        )

        self.assertEqual("carrier_lifecycle_builder_001", request["lifecycle_request_id"])
        self.assertEqual("Can Carrier C be recorded as stale?", request["lifecycle_question"])
        self.assertEqual("carrier_C_additional_physical_candidate", request["selected_carrier"]["carrier_id"])
        self.assertEqual("CARRIER_STALE", request["requested_lifecycle_status"])
        self.assertIsInstance(request["lifecycle_basis"], dict)
        self.assertIsInstance(request["transition_basis"], dict)
        self.assertEqual(3, len(request["related_carrier_evidence"]))
        for value in request["declared_non_claims"].values():
            self.assertIs(value, False)

        result = lifecycle.resolve_carrier_lifecycle_boundary(request)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])

    def test_path_based_resolution(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "lifecycle_request.json"
            path.write_text(json.dumps(request), encoding="utf-8")

            result = lifecycle.resolve_carrier_lifecycle_boundary_from_path(path)

        self.assert_bounded_shape(result)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])
        self.assertEqual(set(TOP_LEVEL_SECTIONS), set(result.keys()))
        self.assertTrue(result["declared_lifecycle_question"]["lifecycle_request_path"])

    def test_write_behavior(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "nested" / "lifecycle_result.json"
            written = lifecycle.write_carrier_lifecycle_result(result, output_path)

            self.assertEqual(output_path, written)
            self.assertTrue(written.exists())
            loaded = json.loads(written.read_text(encoding="utf-8"))

        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded))
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", loaded["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(_valid_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            with patch.object(lifecycle, "CARRIER_LIFECYCLE_BOUNDARY_ROOT", root):
                first = lifecycle.write_carrier_lifecycle_result(result)
                second = lifecycle.write_carrier_lifecycle_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertIn("carrier_C_lifecycle_refused_or_blocked_001", first.name)
            self.assertIn("__carrier_lifecycle_result.json", first.name)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = lifecycle.resolve_carrier_lifecycle_boundary(request)
        repeated = lifecycle.resolve_carrier_lifecycle_boundary(request)

        self.assertEqual(original, request)
        self.assertEqual(original["related_carrier_evidence"], request["related_carrier_evidence"])
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", result["outcome"])
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_RECORDED", repeated["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            written = lifecycle.write_carrier_lifecycle_result(
                result,
                Path(temp_dir) / "result.json",
            )
            self.assertTrue(written.exists())
        self.assertEqual(original, request)

    def test_not_recorded_readable_request(self) -> None:
        request = _valid_request(intent="DO_NOT_RECORD_CARRIER_LIFECYCLE_STATUS")
        request["not_recorded_reason"] = "manual review did not record lifecycle status"

        result = lifecycle.resolve_carrier_lifecycle_boundary(request)

        self.assertEqual("CARRIER_LIFECYCLE_STATUS_NOT_RECORDED", result["outcome"])
        self.assertIs(result["lifecycle_statement"]["carrier_lifecycle_status_recorded"], False)
        self.assertEqual(
            "manual review did not record lifecycle status",
            result["lifecycle_statement"]["not_recorded_reason"],
        )
        self.assertIs(result["lifecycle_statement"]["currentness_created"], False)
        self.assertIs(result["lifecycle_statement"]["distributed_standing_created"], False)

    def test_explicit_block_intent(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary(
            _valid_request(intent="BLOCK_CARRIER_LIFECYCLE_STATUS")
        )

        self.assertEqual("CARRIER_LIFECYCLE_STATUS_BLOCKED", result["outcome"])
        self.assertEqual("LIFECYCLE_REQUEST_EXPLICITLY_BLOCKED", result["block"]["block_code"])
        self.assertIs(result["lifecycle_statement"]["carrier_lifecycle_status_recorded"], False)

    def test_blocking_missing_request(self) -> None:
        result = lifecycle.resolve_carrier_lifecycle_boundary()

        self.assertEqual("CARRIER_LIFECYCLE_STATUS_BLOCKED", result["outcome"])
        self.assertEqual("LIFECYCLE_QUESTION_UNDECLARED", result["block"]["block_code"])

    def test_blocking_malformed_request(self) -> None:
        self.assert_block_code(["not", "a", "mapping"], "DECLARED_LIFECYCLE_REQUEST_MALFORMED")

    def test_blocking_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.json"
            missing_result = lifecycle.resolve_carrier_lifecycle_boundary_from_path(missing)
            self.assertEqual(
                "DECLARED_LIFECYCLE_REQUEST_UNREADABLE",
                missing_result["block"]["block_code"],
            )

            malformed = Path(temp_dir) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            malformed_result = lifecycle.resolve_carrier_lifecycle_boundary_from_path(malformed)
            self.assertEqual(
                "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
                malformed_result["block"]["block_code"],
            )

            array_path = Path(temp_dir) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = lifecycle.resolve_carrier_lifecycle_boundary_from_path(array_path)
            self.assertEqual(
                "DECLARED_LIFECYCLE_REQUEST_MALFORMED",
                array_result["block"]["block_code"],
            )

    def test_blocking_lifecycle_question_intent_and_carrier_identity(self) -> None:
        request = _valid_request()
        request["lifecycle_question"] = ""
        self.assert_block_code(request, "LIFECYCLE_QUESTION_UNDECLARED")

        request = _valid_request()
        request["lifecycle_intent"] = "UNSUPPORTED_INTENT"
        self.assert_block_code(request, "LIFECYCLE_INTENT_UNSUPPORTED")

        request = _valid_request()
        request["selected_carrier"] = {}
        self.assert_block_code(request, "CARRIER_IDENTITY_MISSING")

    def test_blocking_status_and_basis(self) -> None:
        request = _valid_request(status="CARRIER_SOVEREIGN")
        self.assert_block_code(request, "LIFECYCLE_STATUS_UNSUPPORTED")

        request = _valid_request()
        request["lifecycle_basis"] = {}
        self.assert_block_code(request, "LIFECYCLE_BASIS_MISSING")

    def test_blocking_transition_basis_and_unsupported_transition(self) -> None:
        request = _valid_request(status="CARRIER_REINTRODUCED", prior="CARRIER_HOLDING_EVIDENCE")
        self.assert_block_code(request, "LIFECYCLE_TRANSITION_BASIS_MISSING")

        request = _valid_request(
            status="CARRIER_REINTRODUCED",
            prior="CARRIER_HOLDING_EVIDENCE",
            transition_basis={"basis": "unsupported jump"},
        )
        self.assert_block_code(request, "LIFECYCLE_TRANSITION_UNSUPPORTED")

    def test_blocking_related_evidence_malformed(self) -> None:
        self.assert_block_code(
            _valid_request(related_evidence=["not a mapping"]),
            "RELATED_EVIDENCE_MALFORMED",
        )

    def test_blocking_erasure_and_hidden_visibility(self) -> None:
        cases = [
            ("lifecycle_erases_evidence", "LIFECYCLE_ERASES_EVIDENCE"),
            ("lifecycle_hides_refusal", "LIFECYCLE_HIDES_REFUSAL"),
            ("lifecycle_hides_divergence", "LIFECYCLE_HIDES_DIVERGENCE"),
            ("lifecycle_hides_corruption", "LIFECYCLE_HIDES_CORRUPTION"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, code)

    def test_blocking_repair_and_mutation_replay_merge(self) -> None:
        request = _valid_request()
        request["repaired_by_overwrite"] = True
        self.assert_block_code(request, "LIFECYCLE_REPAIRS_BY_OVERWRITE")

        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_blocking_source_currentness_authority_permission_collapse(self) -> None:
        cases = [
            ("source_replaced", "LIFECYCLE_REPLACES_SOURCE"),
            ("currentness_created", "LIFECYCLE_CREATES_CURRENTNESS"),
            ("authority_created", "LIFECYCLE_CREATES_AUTHORITY"),
            ("permission_created", "LIFECYCLE_CREATES_PERMISSION"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, code)

    def test_blocking_hierarchy_winner_loser(self) -> None:
        cases = [
            ("carrier_hierarchy_created", "LIFECYCLE_CREATES_CARRIER_HIERARCHY"),
            ("winning_carrier_selected", "LIFECYCLE_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "LIFECYCLE_INVALIDATES_LOSING_CARRIER"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, code)

    def test_blocking_distributed_standing_sync_registry_continuation_operation(self) -> None:
        cases = [
            ("distributed_standing_created", "LIFECYCLE_CREATES_DISTRIBUTED_STANDING"),
            ("repository_synchronization_authorized", "LIFECYCLE_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "LIFECYCLE_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("carrier_registry_created", "LIFECYCLE_CREATES_CARRIER_REGISTRY"),
            ("continuation_authorized", "LIFECYCLE_AUTHORIZES_CONTINUATION"),
            ("distributed_operation_authorized", "LIFECYCLE_AUTHORIZES_DISTRIBUTED_OPERATION"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, code)

    def test_blocking_latest_file_currentness_and_recency_fraud(self) -> None:
        for flag in ("latest_file_currentness", "recency_fraud"):
            with self.subTest(flag=flag):
                request = _valid_request()
                request[flag] = True
                self.assert_block_code(request, "LATEST_FILE_CURRENTNESS")

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        request = _valid_request()
        del request["declared_non_claims"]["carrier_lifecycle_created_registry"]
        result = lifecycle.resolve_carrier_lifecycle_boundary(request)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_BLOCKED", result["outcome"])
        self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", result["block"]["block_code"])
        self.assert_all_non_claims_false(result)

        request = _valid_request()
        request["declared_non_claims"]["carrier_lifecycle_created_registry"] = True
        result = lifecycle.resolve_carrier_lifecycle_boundary(request)
        self.assertEqual("CARRIER_LIFECYCLE_STATUS_BLOCKED", result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"LIFECYCLE_CREATES_CARRIER_REGISTRY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assert_all_non_claims_false(result)


if __name__ == "__main__":
    unittest.main()
