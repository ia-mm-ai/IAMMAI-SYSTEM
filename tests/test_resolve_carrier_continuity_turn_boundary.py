"""Tests for the bounded carrier continuity-turn boundary resolver.

This suite audits turn/pass/lineage posture only. It does not exercise a
generic continuity subsystem, registry implementation, persistence backend,
currentness successor law, distributed standing, synchronization, full body
transfer, workflow, or physical carrier behavior.
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

import resolve_carrier_continuity_turn_boundary as boundary


TOP_LEVEL_SECTIONS = (
    "carrier_continuity_turn_metadata",
    "declared_continuity_turn_question",
    "selected_artifact",
    "turn_kind",
    "turn_basis",
    "predecessor_successor_relation",
    "projection_correspondence",
    "blocked_or_refusal_turns",
    "related_carrier_evidence",
    "continuity_turn_checks",
    "continuity_turn_statement",
    "continuity_turn_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "carrier_continuity_turn_summary",
)

SUPPORTED_TURN_KINDS = (
    "EXPERIMENT_DECLARATION_TURN",
    "PHYSICAL_RECEIPT_ATTEMPT_TURN",
    "RETURNED_EVIDENCE_TURN",
    "ADMISSION_AS_EVIDENCE_TURN",
    "DIVERGENCE_RECORDING_TURN",
    "CURRENTNESS_PARTICIPATION_TURN",
    "RELATION_RECOGNITION_TURN",
    "RELATION_CONFORMANCE_TURN",
    "RELATION_CLOSURE_TURN",
    "LIFECYCLE_STATUS_TURN",
    "REGISTRY_PERSISTENCE_REFERENCE_TURN",
    "STANDING_PROPAGATION_TURN",
    "PROJECTION_SUCCESSOR_TURN",
    "CONFORMANCE_SUCCESSOR_TURN",
    "CLOSURE_SUCCESSOR_TURN",
    "BLOCKED_TURN",
)

REQUIRED_NON_CLAIMS = tuple(boundary.REQUIRED_NON_CLAIMS)


def required_non_claims() -> dict[str, bool]:
    return copy.deepcopy(boundary.REQUIRED_NON_CLAIMS)


def selected_artifact() -> dict[str, object]:
    return {
        "artifact_id": "standing_propagation_v2_result_001",
        "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        "artifact_type": "standing_propagation_boundary_v2_result",
        "selected_artifact_outcome_required": True,
    }


def predecessor_artifact() -> dict[str, object]:
    return {
        "artifact_id": "standing_propagation_v1_result_001",
        "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        "artifact_type": "standing_propagation_boundary_result",
    }


def successor_artifact() -> dict[str, object]:
    return {
        "artifact_id": "standing_propagation_v2_result_001",
        "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        "artifact_type": "standing_propagation_boundary_v2_result",
    }


def projection_correspondence() -> dict[str, object]:
    return {
        "projection_correspondence_status": (
            "PROJECTION_MISMATCH_PRESERVED_AND_SUCCESSOR_PROJECTED"
        ),
        "projection_mismatch_present": True,
        "projection_mismatch_visible": True,
        "summary_under_projected_detailed_basis": True,
        "detailed_basis_distinguished_from_summary": True,
        "detailed_basis_reference": {
            "artifact_id": "standing_propagation_v1_result_001",
            "section": "standing_propagation_basis",
            "preserved_nested_refusal": True,
            "preserved_nested_divergence": True,
            "preserved_receipt_refusal_return_admission_posture": True,
        },
        "summary_projection_reference": {
            "artifact_id": "standing_propagation_v1_result_001",
            "section": "standing_propagation_summary",
            "visible_refusal_preserved": False,
            "visible_divergence_preserved": False,
            "receipt_refusal_return_admission_posture_preserved": False,
        },
        "successor_projection_corrected_future_projection": True,
        "summary_overrode_detailed_basis": False,
        "predecessor_mutated_or_erased": False,
    }


def blocked_or_refusal_turns() -> list[dict[str, object]]:
    return [
        {
            "turn_id": "carrier_c_blocked_receipt_attempt_turn",
            "turn_kind": "PHYSICAL_RECEIPT_ATTEMPT_TURN",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CARRIED_SURFACE_RECEIPT_BLOCKED",
            "description": "visible refusal and divergence preserved",
        },
        {
            "turn_id": "standing_propagation_v1_projection_mismatch_turn",
            "turn_kind": "PROJECTION_SUCCESSOR_TURN",
            "outcome": "PROJECTION_MISMATCH_VISIBLE",
            "description": "summary under-projected detailed refusal divergence",
        },
        {
            "turn_id": "registry_persistence_v1_projection_mismatch_turn",
            "turn_kind": "PROJECTION_SUCCESSOR_TURN",
            "outcome": "PROJECTION_MISMATCH_VISIBLE",
            "description": "summary under-projected lifecycle reference",
        },
    ]


def related_carrier_evidence() -> list[dict[str, object]]:
    return [
        {
            "evidence_id": "carrier_b_successful_receipt_evidence",
            "carrier_id": "carrier_B_receiving_context",
            "outcome": "CARRIED_SURFACE_RECEIVED",
        },
        {
            "evidence_id": "carrier_c_blocked_receipt_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CARRIED_SURFACE_RECEIPT_BLOCKED",
        },
        {
            "evidence_id": "carrier_b_carrier_c_divergence_evidence",
            "carrier_id": "carrier_B__carrier_C",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
        },
        {
            "evidence_id": "carrier_c_currentness_participation_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
        },
        {
            "evidence_id": "carrier_c_lifecycle_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
            "status": "CARRIER_REFUSED_OR_BLOCKED",
        },
        {
            "evidence_id": "carrier_c_registry_persistence_v2_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
        },
        {
            "evidence_id": "standing_propagation_v1_reference",
            "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        },
        {
            "evidence_id": "standing_propagation_v2_reference",
            "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        },
    ]


def valid_request(
    *,
    turn_kind: str = "PROJECTION_SUCCESSOR_TURN",
    include_successor: bool = True,
) -> dict[str, object]:
    request: dict[str, object] = {
        "continuity_turn_request_id": "carrier_continuity_turn_projection_successor_001",
        "continuity_turn_question": (
            "How is carrier-related continuity preserved across turns without "
            "flattening or overwrite?"
        ),
        "continuity_turn_intent": "RECORD_CARRIER_CONTINUITY_TURN",
        "selected_artifact": selected_artifact(),
        "turn_kind": turn_kind,
        "turn_basis": {
            "turn_basis_id": "standing_propagation_v2_projection_successor_basis",
            "turn_basis_statement": (
                "standing propagation v2 succeeds standing propagation v1 by "
                "truthful projection of nested refusal, divergence, and "
                "receipt/refusal/return/admission posture"
            ),
            "successor_correction_is_prospective_and_additive": True,
            "does_not_mutate_predecessor": True,
        },
        "selected_carrier_ids": [
            "carrier_A_source_context",
            "carrier_B_receiving_context",
            "carrier_C_additional_physical_candidate",
        ],
        "selected_surface_or_artifact_id": "standing_propagation_v2_result_001",
        "source_basis_id": "source_standing_surface_basis",
        "carried_basis_id": "standing_surface_carried_basis",
        "receipt_or_refusal_basis_id": "carrier_c_blocked_receipt_basis",
        "admission_basis_id": "carrier_c_returned_blocked_evidence_admission_basis",
        "divergence_basis_id": "carrier_b_c_divergence_basis",
        "currentness_participation_basis_id": "carrier_c_currentness_participation_basis",
        "relation_basis_id": "carrier_b_c_relation_basis",
        "conformance_basis_id": "carrier_b_c_relation_conformance_basis",
        "closure_basis_id": "carrier_b_c_relation_closure_basis",
        "lifecycle_basis_id": "carrier_c_lifecycle_refused_or_blocked_basis",
        "registry_persistence_basis_id": "carrier_c_lifecycle_registry_persistence_v2_basis",
        "standing_propagation_basis_id": "standing_propagation_v2_basis",
        "detailed_basis_reference": {
            "artifact_id": "standing_propagation_v1_result_001",
            "section": "standing_propagation_basis",
        },
        "summary_projection_reference": {
            "artifact_id": "standing_propagation_v1_result_001",
            "section": "standing_propagation_summary",
        },
        "projection_correspondence": projection_correspondence(),
        "blocked_or_refusal_turns": blocked_or_refusal_turns(),
        "related_carrier_evidence": related_carrier_evidence(),
        "declared_non_claims": required_non_claims(),
    }
    if include_successor:
        request["predecessor_artifact"] = predecessor_artifact()
        request["successor_artifact"] = successor_artifact()
        request["successor_relation"] = {
            "successor_relation_claimed": True,
            "successor_relation_type": "SUCCESSOR_BY_PROJECTION",
            "predecessor_artifact_id": "standing_propagation_v1_result_001",
            "successor_artifact_id": "standing_propagation_v2_result_001",
            "successor_is_additive": True,
            "successor_does_not_overwrite_predecessor": True,
        }
        request["successor_reason"] = (
            "v2 projects nested refusal, divergence, and "
            "receipt/refusal/return/admission posture truthfully without "
            "mutating v1"
        )
    return request


def minimal_record_request(turn_kind: str) -> dict[str, object]:
    include_successor = turn_kind in {
        "PROJECTION_SUCCESSOR_TURN",
        "CONFORMANCE_SUCCESSOR_TURN",
        "CLOSURE_SUCCESSOR_TURN",
    }
    request = valid_request(turn_kind=turn_kind, include_successor=include_successor)
    request["continuity_turn_request_id"] = f"{turn_kind.lower()}_001"
    request["projection_correspondence"] = {
        "projection_correspondence_status": "NOT_APPLICABLE"
    }
    request["detailed_basis_reference"] = None
    request["summary_projection_reference"] = None
    request["blocked_or_refusal_turns"] = []
    request["related_carrier_evidence"] = []
    if not include_successor:
        request.pop("predecessor_artifact", None)
        request.pop("successor_artifact", None)
        request.pop("successor_relation", None)
        request.pop("successor_reason", None)
    return request


class CarrierContinuityTurnBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict[str, object]) -> dict[str, object]:
        return boundary.resolve_carrier_continuity_turn_boundary(
            declared_continuity_turn_request=request
        )

    def recorded_result(self) -> dict[str, object]:
        result = self.resolve(valid_request())
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        return result

    def assert_block(self, request: dict[str, object], code: str) -> dict[str, object]:
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        return result

    def assert_required_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_successful_projection_successor_turn_recording(self) -> None:
        result = self.recorded_result()

        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["carrier_continuity_turn_summary"]["failed_check_count"])

        statement = result["continuity_turn_statement"]
        self.assertIs(statement["carrier_continuity_turn_recorded"], True)
        self.assertIs(statement["selected_artifact_preserved"], True)
        self.assertIs(statement["selected_artifact_outcome_preserved"], True)
        self.assertIs(statement["turn_kind_preserved"], True)
        self.assertIs(statement["turn_basis_preserved"], True)
        self.assertIs(statement["predecessor_preserved"], True)
        self.assertIs(statement["successor_relation_preserved"], True)
        self.assertIs(statement["successor_reason_preserved"], True)
        self.assertIs(statement["projection_correspondence_preserved"], True)
        self.assertIs(statement["projection_mismatch_visible"], True)
        self.assertIs(statement["blocked_attempts_preserved"], True)
        self.assertIs(statement["refusal_preserved"], True)
        self.assertIs(statement["divergence_preserved"], True)
        self.assertIs(statement["detailed_basis_distinguished_from_summary"], True)
        self.assertIs(statement["summary_overrode_detailed_basis"], False)
        self.assertIs(statement["predecessor_mutated_or_erased"], False)
        self.assertIs(statement["latest_turn_currentness"], False)
        self.assertIs(statement["latest_file_currentness"], False)
        self.assertIs(statement["currentness_created"], False)
        self.assertIs(statement["authority_created"], False)
        self.assertIs(statement["permission_created"], False)
        self.assertIs(statement["source_replaced"], False)
        self.assertIs(statement["evidence_erased"], False)
        self.assertIs(statement["carrier_hierarchy_created"], False)
        self.assertIs(statement["distributed_standing_created"], False)
        self.assertIs(statement["repository_synchronization_authorized"], False)
        self.assertIs(statement["full_body_transfer_authorized"], False)
        self.assertIs(statement["second_body_created"], False)
        self.assertIs(statement["continuation_authorized"], False)
        self.assertIs(statement["distributed_operation_authorized"], False)

    def test_metadata(self) -> None:
        metadata = self.recorded_result()["carrier_continuity_turn_metadata"]
        for key in (
            "carrier_continuity_turn_result_id",
            "carrier_continuity_turn_result_type",
            "carrier_continuity_turn_result_version",
            "generated_at",
            "resolver_module",
            "selected_artifact_id",
            "selected_turn_kind",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["carrier_continuity_turn_result_version"])
        self.assertEqual(
            "resolve_carrier_continuity_turn_boundary",
            metadata["resolver_module"],
        )

    def test_declared_question_and_selected_artifact_and_turn_kind(self) -> None:
        result = self.recorded_result()
        question = result["declared_continuity_turn_question"]
        selected = result["selected_artifact"]
        kind = result["turn_kind"]

        self.assertEqual(
            "carrier_continuity_turn_projection_successor_001",
            question["continuity_turn_request_id"],
        )
        self.assertIn("How is carrier-related continuity", question["continuity_turn_question"])
        self.assertEqual("RECORD_CARRIER_CONTINUITY_TURN", question["continuity_turn_intent"])
        self.assertIn("authority_created", question["declared_non_claims"])
        self.assertIs(question["turn_is_not_authority"], True)
        self.assertIs(question["latest_turn_is_not_currentness"], True)
        self.assertIs(question["successor_is_not_overwrite"], True)
        self.assertIs(question["summary_is_not_artifact_body"], True)
        self.assertIs(question["distributed_standing_not_created"], True)

        self.assertEqual("standing_propagation_v2_result_001", selected["selected_artifact_id"])
        self.assertEqual(
            "STANDING_PROPAGATION_POSTURE_RECORDED",
            selected["selected_artifact_outcome"],
        )
        self.assertEqual(
            "standing_propagation_boundary_v2_result",
            selected["selected_artifact_type_or_class"],
        )
        self.assertIs(selected["selected_artifact_remains_evidence_or_reference"], True)
        self.assertIs(selected["selected_artifact_is_not_currentness"], True)
        self.assertIs(selected["selected_artifact_is_not_distributed_standing"], True)

        self.assertEqual("PROJECTION_SUCCESSOR_TURN", kind["turn_kind"])
        self.assertIs(kind["turn_kind_supported"], True)
        self.assertIs(kind["turn_kind_is_not_currentness"], True)
        self.assertIs(kind["turn_kind_is_not_authority"], True)

    def test_turn_basis_preserves_declared_dimensions(self) -> None:
        basis = self.recorded_result()["turn_basis"]
        dimensions = basis["continuity_turn_dimensions"]
        self.assertIs(basis["turn_basis_declared"], True)
        self.assertIs(basis["turn_basis_preserved"], True)
        self.assertIs(basis["turn_basis_does_not_authorize_continuation"], True)
        self.assertEqual(
            [
                "carrier_A_source_context",
                "carrier_B_receiving_context",
                "carrier_C_additional_physical_candidate",
            ],
            dimensions["selected_carrier_ids"],
        )
        for key in (
            "selected_surface_or_artifact_id",
            "source_basis_id",
            "carried_basis_id",
            "receipt_or_refusal_basis_id",
            "admission_basis_id",
            "divergence_basis_id",
            "currentness_participation_basis_id",
            "relation_basis_id",
            "conformance_basis_id",
            "closure_basis_id",
            "lifecycle_basis_id",
            "registry_persistence_basis_id",
            "standing_propagation_basis_id",
            "detailed_basis_reference",
            "summary_projection_reference",
        ):
            self.assertTrue(dimensions[key], key)

    def test_predecessor_successor_relation(self) -> None:
        relation = self.recorded_result()["predecessor_successor_relation"]
        self.assertEqual(
            "standing_propagation_v1_result_001",
            relation["predecessor_artifact_id"],
        )
        self.assertEqual(
            "standing_propagation_v2_result_001",
            relation["successor_artifact_id"],
        )
        self.assertIs(relation["successor_relation_claimed"], True)
        self.assertIs(relation["successor_relation_declared"], True)
        self.assertTrue(relation["successor_reason"])
        self.assertIs(relation["successor_does_not_overwrite_predecessor"], True)
        self.assertIs(relation["successor_does_not_invalidate_predecessor"], True)

    def test_projection_correspondence(self) -> None:
        projection = self.recorded_result()["projection_correspondence"]
        self.assertIs(projection["projection_correspondence_preserved"], True)
        self.assertEqual(
            "PROJECTION_MISMATCH_PRESERVED_AND_SUCCESSOR_PROJECTED",
            projection["projection_correspondence_status"],
        )
        self.assertIs(projection["projection_mismatch_applicable"], True)
        self.assertIs(projection["projection_mismatch_visible"], True)
        self.assertIs(projection["detailed_basis_distinguished_from_summary"], True)
        self.assertIs(projection["summary_overrode_detailed_basis"], False)
        self.assertEqual(
            "standing_propagation_basis",
            projection["detailed_basis_reference"]["section"],
        )
        self.assertEqual(
            "standing_propagation_summary",
            projection["summary_projection_reference"]["section"],
        )

    def test_blocked_refusal_turns_and_related_evidence(self) -> None:
        result = self.recorded_result()
        blocked = result["blocked_or_refusal_turns"]
        related = result["related_carrier_evidence"]
        self.assertIs(blocked["blocked_attempts_preserved"], True)
        self.assertIs(blocked["refusal_preserved"], True)
        self.assertIs(blocked["divergence_preserved"], True)
        self.assertIs(blocked["blocked_turn_does_not_invalidate_body"], True)
        self.assertIs(blocked["success_does_not_erase_refusal"], True)

        ids = set(related["related_carrier_evidence_ids"])
        self.assertIn("carrier_b_successful_receipt_evidence", ids)
        self.assertIn("carrier_c_blocked_receipt_evidence", ids)
        self.assertIn("carrier_b_carrier_c_divergence_evidence", ids)
        self.assertIn("carrier_c_lifecycle_evidence", ids)
        self.assertIn("carrier_c_registry_persistence_v2_evidence", ids)
        self.assertIn("standing_propagation_v2_reference", ids)
        self.assertIn("CARRIER_DIVERGENCE_RECORDED", related["related_carrier_evidence_outcomes"])
        carriers = {
            entry.get("carrier_id")
            for entry in related["related_carrier_evidence_entries"]
            if entry.get("carrier_id")
        }
        self.assertIn("carrier_B_receiving_context", carriers)
        self.assertIn("carrier_C_additional_physical_candidate", carriers)
        self.assertIs(related["evidence_remains_evidence"], True)
        self.assertIs(related["related_evidence_does_not_create_currentness"], True)
        self.assertIs(related["related_evidence_does_not_create_distributed_standing"], True)

    def test_continuity_turn_checks(self) -> None:
        checks = self.recorded_result()["continuity_turn_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"], check["check_name"])

        check_names = {check["check_name"] for check in checks}
        expected_names = {
            "continuity_turn_question_declared",
            "continuity_turn_intent_supported",
            "selected_artifact_present",
            "selected_artifact_identity_present",
            "selected_artifact_outcome_preserved_where_required",
            "turn_kind_supported",
            "turn_basis_declared",
            "predecessor_preserved_where_required",
            "successor_relation_preserved_where_claimed",
            "successor_reason_preserved_where_claimed",
            "projection_mismatch_visible_where_applicable",
            "blocked_attempt_visible_where_applicable",
            "refusal_visible_where_applicable",
            "divergence_visible_where_applicable",
            "detailed_basis_distinguishable_from_summary_projection",
            "summary_does_not_override_detailed_basis",
            "predecessor_not_mutated_or_erased",
            "latest_turn_not_currentness",
            "latest_file_not_currentness",
            "no_currentness",
            "no_authority",
            "no_permission",
            "no_source_replacement",
            "no_evidence_erasure",
            "no_carrier_hierarchy",
            "no_current_carrier_selected",
            "no_winning_carrier_selected",
            "no_losing_carrier_invalidated",
            "no_distributed_standing",
            "no_repository_synchronization",
            "no_full_body_transfer",
            "no_second_body",
            "no_continuation",
            "no_distributed_operation",
            "no_mutation_replay_or_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_names.issubset(check_names))

    def test_non_meaning_and_open_items(self) -> None:
        result = self.recorded_result()
        non_meaning = result["continuity_turn_non_meaning"]
        for key in (
            "does_not_mean_currentness",
            "does_not_mean_authority",
            "does_not_mean_permission",
            "does_not_mean_distributed_standing",
            "does_not_mean_source_replacement",
            "does_not_mean_carrier_hierarchy",
            "does_not_mean_carrier_priority",
            "does_not_mean_carrier_sovereignty",
            "does_not_mean_workflow_authorization",
            "does_not_mean_continuation",
            "does_not_mean_action",
            "does_not_mean_consequence",
            "does_not_mean_truth",
            "does_not_mean_final_governance",
            "does_not_mean_final_system_identity",
            "does_not_mean_automatic_successor",
            "does_not_mean_patch_permission",
            "does_not_mean_overwrite_permission",
            "does_not_mean_evidence_erasure",
            "does_not_mean_summary_authority",
            "does_not_mean_registry_authority",
            "does_not_mean_latest_file_currentness",
            "does_not_mean_latest_turn_currentness",
            "does_not_mean_distributed_operation",
            "does_not_mean_repository_synchronization",
            "does_not_mean_full_body_transfer",
            "does_not_mean_second_body",
            "does_not_mean_standing_propagation_implementation",
            "does_not_mean_currentness_successor_law",
            "does_not_mean_distributed_standing_prerequisite_completion",
        ):
            self.assertIs(non_meaning[key], True, key)

        open_items = result["what_remains_open"]
        for key in (
            "carrier_continuity_turn_implementation_refinement",
            "cross_carrier_currentness_successor_law",
            "divergence_consequence_law",
            "distributed_standing_boundary",
            "distributed_standing",
            "carrier_registry_implementation",
            "persistence_implementation",
            "standing_propagation_implementation_beyond_boundary_recording",
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
        ):
            self.assertIs(open_items[key], True, key)

    def test_summary_helper(self) -> None:
        result = self.recorded_result()
        summary = boundary.build_carrier_continuity_turn_summary(result)
        self.assertEqual(result["carrier_continuity_turn_summary"], summary)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            "carrier_continuity_turn_projection_successor_001",
            summary["continuity_turn_request_id"],
        )
        self.assertEqual("standing_propagation_v2_result_001", summary["selected_artifact_id"])
        self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", summary["selected_artifact_outcome"])
        self.assertEqual("PROJECTION_SUCCESSOR_TURN", summary["turn_kind"])
        self.assertEqual(
            "standing_propagation_v1_result_001",
            summary["predecessor_artifact_id"],
        )
        self.assertEqual(
            "standing_propagation_v2_result_001",
            summary["successor_artifact_id"],
        )
        self.assertTrue(summary["successor_relation"])
        self.assertTrue(summary["successor_reason"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["continuity_turn_recorded"], True)
        self.assertIs(summary["projection_mismatch_visible"], True)
        self.assertIs(summary["blocked_attempts_preserved"], True)
        self.assertIs(summary["refusal_preserved"], True)
        self.assertIs(summary["divergence_preserved"], True)
        self.assertIs(summary["detailed_basis_distinguished_from_summary"], True)
        self.assertIs(summary["summary_overrode_detailed_basis"], False)
        self.assertIs(summary["predecessor_mutated_or_erased"], False)
        self.assertIs(summary["no_currentness_authority_permission_source_replacement"], True)
        self.assertIs(summary["no_evidence_erasure"], True)
        self.assertIs(summary["no_carrier_hierarchy"], True)
        self.assertIs(summary["no_current_winning_losing_carrier_collapse"], True)
        self.assertIs(summary["no_distributed_standing"], True)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation"], True)
        self.assertIs(summary["no_distributed_operation"], True)
        self.assertIs(summary["no_latest_turn_file_currentness"], True)
        self.assertEqual(set(REQUIRED_NON_CLAIMS), set(summary["key_non_claims"]))

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        recorded = self.recorded_result()
        self.assert_required_non_claims_false(recorded)

        not_recorded_request = valid_request()
        not_recorded_request["continuity_turn_intent"] = "DO_NOT_RECORD_CARRIER_CONTINUITY_TURN"
        not_recorded = self.resolve(not_recorded_request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_NOT_RECORDED, not_recorded["outcome"])
        self.assert_required_non_claims_false(not_recorded)

        blocked_request = valid_request()
        blocked_request["currentness_created"] = True
        blocked = self.resolve(blocked_request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_BLOCKED, blocked["outcome"])
        self.assert_required_non_claims_false(blocked)

    def test_supported_turn_kinds_can_record(self) -> None:
        for turn_kind in SUPPORTED_TURN_KINDS:
            with self.subTest(turn_kind=turn_kind):
                result = self.resolve(minimal_record_request(turn_kind))
                self.assertEqual(
                    boundary.CARRIER_CONTINUITY_TURN_RECORDED,
                    result["outcome"],
                    result["block"],
                )

    def test_request_builder_helper(self) -> None:
        request = boundary.build_declared_carrier_continuity_turn_request(
            "helper_continuity_turn_001",
            "How is carrier-related continuity preserved across turns without flattening or overwrite?",
            selected_artifact(),
            "PROJECTION_SUCCESSOR_TURN",
            {"turn_basis_id": "helper_turn_basis"},
            predecessor_artifact=predecessor_artifact(),
            successor_artifact=successor_artifact(),
            successor_reason="helper preserves successor reason",
            projection_correspondence=projection_correspondence(),
            blocked_or_refusal_turns=blocked_or_refusal_turns(),
            related_carrier_evidence=related_carrier_evidence(),
        )
        request["detailed_basis_reference"] = {"section": "standing_propagation_basis"}
        request["summary_projection_reference"] = {"section": "standing_propagation_summary"}
        self.assertEqual("helper_continuity_turn_001", request["continuity_turn_request_id"])
        self.assertEqual("PROJECTION_SUCCESSOR_TURN", request["turn_kind"])
        self.assertEqual(selected_artifact(), request["selected_artifact"])
        self.assertEqual(predecessor_artifact(), request["predecessor_artifact"])
        self.assertEqual(successor_artifact(), request["successor_artifact"])
        self.assertEqual(required_non_claims(), request["declared_non_claims"])

        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        self.assertEqual(0, result["carrier_continuity_turn_summary"]["failed_check_count"])

    def test_path_based_resolution(self) -> None:
        request = valid_request()
        mapping_result = self.resolve(request)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "request.json"
            path.write_text(json.dumps(request), encoding="utf-8")
            path_result = boundary.resolve_carrier_continuity_turn_boundary_from_path(path)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, path_result["outcome"])
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertTrue(
            path_result["declared_continuity_turn_question"]["request_path"].endswith(
                "request.json"
            )
        )

    def test_write_behavior_and_default_output_root(self) -> None:
        result = self.recorded_result()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            explicit_path = tmp_path / "nested" / "result.json"
            written = boundary.write_carrier_continuity_turn_result(result, explicit_path)
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(boundary, "CARRIER_CONTINUITY_TURN_BOUNDARY_ROOT", tmp_path):
                first = boundary.write_carrier_continuity_turn_result(result)
                second = boundary.write_carrier_continuity_turn_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(tmp_path, first.parent)
            self.assertEqual(tmp_path, second.parent)
            self.assertIn("__carrier_continuity_turn_result.json", first.name)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        original = copy.deepcopy(request)
        selected_original = copy.deepcopy(request["selected_artifact"])
        predecessor_original = copy.deepcopy(request["predecessor_artifact"])
        successor_original = copy.deepcopy(request["successor_artifact"])
        related_original = copy.deepcopy(request["related_carrier_evidence"])

        first = self.resolve(request)
        second = self.resolve(request)
        self.assertEqual(original, request)
        self.assertEqual(selected_original, request["selected_artifact"])
        self.assertEqual(predecessor_original, request["predecessor_artifact"])
        self.assertEqual(successor_original, request["successor_artifact"])
        self.assertEqual(related_original, request["related_carrier_evidence"])
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "additive" / "result.json"
            boundary.write_carrier_continuity_turn_result(first, output)
            self.assertTrue(output.exists())
            self.assertEqual([output], list((Path(tmp) / "additive").iterdir()))

    def test_not_recorded_and_explicit_block_intents(self) -> None:
        request = valid_request()
        request["continuity_turn_intent"] = "DO_NOT_RECORD_CARRIER_CONTINUITY_TURN"
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_NOT_RECORDED, result["outcome"])
        self.assertIs(result["continuity_turn_statement"]["carrier_continuity_turn_recorded"], False)
        self.assertTrue(result["continuity_turn_statement"]["not_recorded_reason"])
        self.assertIs(result["continuity_turn_statement"]["currentness_created"], False)
        self.assertIs(result["continuity_turn_statement"]["distributed_operation_authorized"], False)

        block_request = valid_request()
        block_request["continuity_turn_intent"] = "BLOCK_CARRIER_CONTINUITY_TURN"
        blocked = self.resolve(block_request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_BLOCKED, blocked["outcome"])
        self.assertEqual(
            "CARRIER_CONTINUITY_TURN_REQUEST_EXPLICITLY_BLOCKED",
            blocked["block"]["block_code"],
        )
        self.assertIs(blocked["continuity_turn_statement"]["carrier_continuity_turn_recorded"], False)

    def test_missing_and_malformed_request_blocks(self) -> None:
        missing = boundary.resolve_carrier_continuity_turn_boundary()
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_BLOCKED, missing["outcome"])
        self.assertEqual("CONTINUITY_TURN_QUESTION_UNDECLARED", missing["block"]["block_code"])

        malformed = boundary.resolve_carrier_continuity_turn_boundary(
            declared_continuity_turn_request=["not", "a", "mapping"]
        )
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_BLOCKED, malformed["outcome"])
        self.assertEqual(
            "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
            malformed["block"]["block_code"],
        )

    def test_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = boundary.resolve_carrier_continuity_turn_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(
                "DECLARED_CONTINUITY_TURN_REQUEST_UNREADABLE",
                missing["block"]["block_code"],
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = boundary.resolve_carrier_continuity_turn_boundary_from_path(
                malformed_path
            )
            self.assertEqual(
                "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
                malformed["block"]["block_code"],
            )

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = boundary.resolve_carrier_continuity_turn_boundary_from_path(
                array_path
            )
            self.assertEqual(
                "DECLARED_CONTINUITY_TURN_REQUEST_MALFORMED",
                array_result["block"]["block_code"],
            )

    def test_blocking_question_intent_and_selected_artifact(self) -> None:
        request = valid_request()
        request.pop("continuity_turn_question")
        self.assert_block(request, "CONTINUITY_TURN_QUESTION_UNDECLARED")

        request = valid_request()
        request["continuity_turn_intent"] = "RECORD_AS_CURRENTNESS"
        self.assert_block(request, "CONTINUITY_TURN_INTENT_UNSUPPORTED")

        request = valid_request()
        request.pop("selected_artifact")
        self.assert_block(request, "SELECTED_ARTIFACT_MISSING")

        request = valid_request()
        request["selected_artifact"] = ["malformed"]
        self.assert_block(request, "SELECTED_ARTIFACT_MALFORMED")

        request = valid_request()
        request["selected_artifact"] = {"outcome": "STANDING_PROPAGATION_POSTURE_RECORDED"}
        self.assert_block(request, "SELECTED_ARTIFACT_IDENTITY_MISSING")

        request = valid_request()
        request["selected_artifact"] = {
            "artifact_id": "standing_propagation_v2_result_001",
            "selected_artifact_outcome_required": True,
        }
        self.assert_block(request, "SELECTED_ARTIFACT_OUTCOME_MISSING")

    def test_blocking_turn_kind_and_turn_basis(self) -> None:
        request = valid_request()
        request["turn_kind"] = "UNBOUNDED_WORKFLOW_TURN"
        self.assert_block(request, "TURN_KIND_UNSUPPORTED")

        request = valid_request()
        request.pop("turn_basis")
        self.assert_block(request, "TURN_BASIS_MISSING")

    def test_blocking_predecessor_successor_issues(self) -> None:
        request = valid_request(include_successor=False)
        request["predecessor_required"] = True
        self.assert_block(request, "PREDECESSOR_REQUIRED_BUT_MISSING")

        request = valid_request(include_successor=False)
        request["successor_relation"] = {
            "successor_relation_claimed": True,
            "successor_relation_type": "SUCCESSOR_BY_PROJECTION",
        }
        request["successor_reason"] = "successor relation is claimed"
        self.assert_block(request, "SUCCESSOR_RELATION_PREDECESSOR_MISSING")

        request = valid_request()
        request.pop("successor_reason")
        self.assert_block(request, "SUCCESSOR_REASON_MISSING")

    def test_blocking_hidden_projection_blocked_refusal_and_divergence(self) -> None:
        request = valid_request()
        request["projection_correspondence"]["projection_mismatch_hidden"] = True
        self.assert_block(request, "PROJECTION_MISMATCH_HIDDEN")

        request = valid_request()
        request["blocked_attempt_hidden"] = True
        self.assert_block(request, "BLOCKED_ATTEMPT_HIDDEN")

        request = valid_request()
        request["blocked_or_refusal_turns"] = [
            {"turn_id": "carrier_c_refusal_turn", "outcome": "VISIBLE_REFUSAL"}
        ]
        request["refusal_hidden"] = True
        self.assert_block(request, "REFUSAL_HIDDEN")

        request = valid_request()
        request["blocked_or_refusal_turns"] = [
            {"turn_id": "carrier_b_c_divergence_turn", "outcome": "VISIBLE_DIVERGENCE"}
        ]
        request["divergence_hidden"] = True
        self.assert_block(request, "DIVERGENCE_HIDDEN")

    def test_blocking_summary_overwrite_and_predecessor_mutation(self) -> None:
        request = valid_request()
        request["projection_correspondence"]["summary_overrode_detailed_basis"] = True
        self.assert_block(request, "SUMMARY_OVERWRITES_DETAILED_BASIS")

        request = valid_request()
        request["predecessor_mutated"] = True
        self.assert_block(request, "PREDECESSOR_MUTATED_OR_ERASED")

        request = valid_request()
        request["successor_relation"]["successor_invalidated_predecessor"] = True
        self.assert_block(request, "PREDECESSOR_MUTATED_OR_ERASED")

    def test_blocking_latest_currentness(self) -> None:
        request = valid_request()
        request["latest_turn_currentness"] = True
        self.assert_block(request, "LATEST_TURN_CURRENTNESS")

        request = valid_request()
        request["latest_file_currentness"] = True
        self.assert_block(request, "LATEST_FILE_CURRENTNESS")

        request = valid_request()
        request["recency_fraud"] = True
        self.assert_block(request, "LATEST_FILE_CURRENTNESS")

    def test_blocking_source_currentness_authority_permission_evidence(self) -> None:
        cases = (
            ("source_replaced", "TURN_REPLACES_SOURCE"),
            ("currentness_created", "TURN_CREATES_CURRENTNESS"),
            ("authority_created", "TURN_CREATES_AUTHORITY"),
            ("permission_created", "TURN_CREATES_PERMISSION"),
            ("evidence_erased", "TURN_ERASES_EVIDENCE"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assert_block(request, code)

    def test_blocking_carrier_hierarchy_and_carrier_selection(self) -> None:
        cases = (
            ("carrier_hierarchy_created", "TURN_CREATES_CARRIER_HIERARCHY"),
            ("current_carrier_selected", "TURN_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "TURN_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "TURN_INVALIDATES_LOSING_CARRIER"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assert_block(request, code)

    def test_blocking_distributed_sync_transfer_second_body(self) -> None:
        cases = (
            ("distributed_standing_created", "TURN_CREATES_DISTRIBUTED_STANDING"),
            ("repository_synchronization_authorized", "TURN_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "TURN_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "TURN_CREATES_SECOND_BODY"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assert_block(request, code)

    def test_blocking_continuation_distributed_operation_mutation_replay_merge(self) -> None:
        cases = (
            ("continuation_authorized", "TURN_AUTHORIZES_CONTINUATION"),
            ("distributed_operation_authorized", "TURN_AUTHORIZES_DISTRIBUTED_OPERATION"),
            ("mutation_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ("replay_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ("merge_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assert_block(request, code)

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        request = valid_request()
        request["declared_non_claims"].pop("authority_created")
        result = self.assert_block(request, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertIn("authority_created", result["non_claims"]["missing_required_non_claims"])

        request = valid_request()
        request["declared_non_claims"]["authority_created"] = True
        result = boundary.resolve_carrier_continuity_turn_boundary(request)
        self.assertEqual("CARRIER_CONTINUITY_TURN_BLOCKED", result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "TURN_CREATES_AUTHORITY"},
        )
        self.assertIn("authority_created", result["non_claims"]["flipped_required_non_claims"])


if __name__ == "__main__":
    unittest.main()
