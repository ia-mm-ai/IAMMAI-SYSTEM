"""Tests for the carrier continuity-turn boundary v2 successor resolver.

This suite audits truthful recursive projection for turn/pass/lineage posture
only. V1 stands as lineage. These tests do not exercise a generic continuity
subsystem, registry implementation, currentness successor law, distributed
standing, synchronization, full body transfer, workflow, or physical carrier
behavior.
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

import resolve_carrier_continuity_turn_boundary_v2 as boundary


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

SUCCESSOR_TURN_KINDS = {
    "PROJECTION_SUCCESSOR_TURN",
    "CONFORMANCE_SUCCESSOR_TURN",
    "CLOSURE_SUCCESSOR_TURN",
}

REQUIRED_NON_CLAIMS = tuple(boundary.REQUIRED_NON_CLAIMS)
V1_OUTPUT_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_carrier_continuity_turn_boundary"
)


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


def successor_relation() -> dict[str, object]:
    return {
        "successor_relation_claimed": True,
        "successor_relation_type": "SUCCESSOR_BY_PROJECTION",
        "predecessor_artifact_id": "standing_propagation_v1_result_001",
        "successor_artifact_id": "standing_propagation_v2_result_001",
        "successor_is_additive": True,
        "successor_does_not_overwrite_predecessor": True,
        "successor_does_not_invalidate_predecessor": True,
    }


def successor_reason() -> str:
    return (
        "v2 projects projection mismatch, blocked/refusal turns, and "
        "divergence preservation truthfully without mutating v1"
    )


def projection_correspondence() -> dict[str, object]:
    return {
        "projection_correspondence_status": "SUCCESSOR_PROJECTION_OVER_MISMATCH",
        "projection_mismatch_present": True,
        "predecessor_projection_mismatch_visible": True,
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
            "projection_mismatch_visible": False,
        },
        "successor_projection_corrected_future_projection": True,
        "summary_overrode_detailed_basis": False,
        "predecessor_mutated_or_erased": False,
    }


def blocked_or_refusal_turns() -> list[dict[str, object]]:
    return [
        {
            "turn_id": "carrier_c_physical_receipt_attempt_blocked",
            "turn_kind": "PHYSICAL_RECEIPT_ATTEMPT_TURN",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "outcome": "BLOCKED",
            "refusal_preserved": True,
            "blocked_attempts_preserved": True,
        },
        {
            "turn_id": "carrier_c_registry_persistence_v1_projection_mismatch",
            "turn_kind": "PROJECTION_SUCCESSOR_TURN",
            "outcome": "PROJECTION_MISMATCH_VISIBLE",
            "projection_mismatch_visible": True,
            "description": "registry persistence v1 summary under-projected lifecycle reference",
        },
        {
            "turn_id": "carrier_c_standing_propagation_v1_projection_mismatch",
            "turn_kind": "PROJECTION_SUCCESSOR_TURN",
            "outcome": "PROJECTION_MISMATCH_VISIBLE",
            "projection_mismatch_visible": True,
            "description": "standing propagation v1 summary under-projected refusal divergence",
        },
    ]


def related_carrier_evidence() -> list[dict[str, object]]:
    return [
        {
            "evidence_id": "carrier_c_blocked_receipt_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_role": "blocked_refusal_evidence",
            "outcome": "BLOCKED",
        },
        {
            "evidence_id": "carrier_b_carrier_c_divergence_evidence",
            "carrier_id": "carrier_B__carrier_C",
            "evidence_class": "visible_divergence_evidence",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
        },
    ]


def full_related_carrier_evidence() -> list[dict[str, object]]:
    return [
        {
            "evidence_id": "carrier_b_successful_receipt_evidence",
            "carrier_id": "carrier_B_receiving_context",
            "outcome": "CARRIED_SURFACE_RECEIVED",
        },
        *related_carrier_evidence(),
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


def detailed_turn_basis() -> dict[str, object]:
    return {
        "turn_basis_id": "standing_propagation_v2_projection_successor_basis",
        "turn_basis_statement": (
            "standing propagation v2 succeeds standing propagation v1 by truthful "
            "recursive projection of nested projection mismatch, blocked refusal, "
            "and divergence posture"
        ),
        "projection_mismatch_visible": True,
        "blocked_attempts_preserved": True,
        "refusal_preserved": True,
        "divergence_preserved": True,
        "detailed_basis_distinguished_from_summary": True,
        "summary_overrode_detailed_basis": False,
        "predecessor_mutated_or_erased": False,
        "detailed_basis_path_or_section": "standing_propagation_basis",
        "summary_projection_path_or_section": "standing_propagation_summary",
    }


def minimal_turn_basis() -> dict[str, object]:
    return {
        "turn_basis_id": "minimal_turn_basis",
        "detailed_basis_path_or_section": "detailed_basis",
        "summary_projection_path_or_section": "summary_projection",
    }


def valid_request(
    *,
    turn_kind: str = "PROJECTION_SUCCESSOR_TURN",
    include_successor: bool = True,
    turn_basis: dict[str, object] | None = None,
    projection: dict[str, object] | None = None,
    blocked_turns: list[dict[str, object]] | None = None,
    related_evidence: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    request: dict[str, object] = {
        "continuity_turn_request_id": "carrier_continuity_turn_v2_projection_successor_001",
        "continuity_turn_question": (
            "How is carrier-related continuity preserved across turns without "
            "flattening or overwrite?"
        ),
        "continuity_turn_intent": "RECORD_CARRIER_CONTINUITY_TURN",
        "selected_artifact": selected_artifact(),
        "turn_kind": turn_kind,
        "turn_basis": copy.deepcopy(turn_basis if turn_basis is not None else detailed_turn_basis()),
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
        "projection_correspondence": copy.deepcopy(
            projection if projection is not None else projection_correspondence()
        ),
        "blocked_or_refusal_turns": copy.deepcopy(
            blocked_turns if blocked_turns is not None else blocked_or_refusal_turns()
        ),
        "related_carrier_evidence": copy.deepcopy(
            related_evidence if related_evidence is not None else full_related_carrier_evidence()
        ),
        "declared_non_claims": required_non_claims(),
    }
    if include_successor:
        request["predecessor_artifact"] = predecessor_artifact()
        request["successor_artifact"] = successor_artifact()
        request["successor_relation"] = successor_relation()
        request["successor_reason"] = successor_reason()
    return request


def minimal_record_request(turn_kind: str) -> dict[str, object]:
    include_successor = turn_kind in SUCCESSOR_TURN_KINDS
    request = valid_request(
        turn_kind=turn_kind,
        include_successor=include_successor,
        turn_basis={"turn_basis_id": f"{turn_kind.lower()}_basis"},
        projection={"projection_correspondence_status": "NOT_APPLICABLE"},
        blocked_turns=[],
        related_evidence=[],
    )
    request["continuity_turn_request_id"] = f"{turn_kind.lower()}_v2_001"
    request["detailed_basis_reference"] = None
    request["summary_projection_reference"] = None
    if not include_successor:
        request.pop("predecessor_artifact", None)
        request.pop("successor_artifact", None)
        request.pop("successor_relation", None)
        request.pop("successor_reason", None)
    return request


def live_shape_request() -> dict[str, object]:
    return valid_request(
        turn_basis=detailed_turn_basis(),
        projection=projection_correspondence(),
        blocked_turns=blocked_or_refusal_turns(),
        related_evidence=related_carrier_evidence(),
    )


class CarrierContinuityTurnBoundaryV2Tests(unittest.TestCase):
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

    def assert_no_collapse(self, statement: dict[str, object]) -> None:
        for key in (
            "latest_turn_currentness",
            "latest_file_currentness",
            "currentness_created",
            "authority_created",
            "permission_created",
            "source_replaced",
            "evidence_erased",
            "carrier_hierarchy_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "distributed_standing_created",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
            "summary_overrode_detailed_basis",
            "predecessor_mutated_or_erased",
        ):
            self.assertIs(statement[key], False, key)

    def test_successful_v2_projection_successor_turn_recording(self) -> None:
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
        self.assert_no_collapse(statement)

    def test_metadata_and_successor_lineage(self) -> None:
        metadata = self.recorded_result()["carrier_continuity_turn_metadata"]
        for key in (
            "carrier_continuity_turn_result_id",
            "carrier_continuity_turn_result_type",
            "carrier_continuity_turn_result_version",
            "generated_at",
            "resolver_module",
            "successor_of_module",
            "selected_artifact_id",
            "selected_turn_kind",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.2.0", metadata["carrier_continuity_turn_result_version"])
        self.assertEqual(
            "resolve_carrier_continuity_turn_boundary_v2",
            metadata["resolver_module"],
        )
        self.assertEqual(
            "resolve_carrier_continuity_turn_boundary",
            metadata["successor_of_module"],
        )

    def test_v2_projection_from_nested_turn_basis(self) -> None:
        request = valid_request(
            turn_basis=detailed_turn_basis(),
            projection={"projection_correspondence_status": "NOT_APPLICABLE"},
            blocked_turns=[],
            related_evidence=[],
        )
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        statement = result["continuity_turn_statement"]
        summary = result["carrier_continuity_turn_summary"]
        for key in (
            "projection_mismatch_visible",
            "blocked_attempts_preserved",
            "refusal_preserved",
            "divergence_preserved",
            "detailed_basis_distinguished_from_summary",
        ):
            self.assertIs(statement[key], True, key)
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["summary_overrode_detailed_basis"], False)
        self.assertIs(summary["predecessor_mutated_or_erased"], False)

    def test_v2_projection_from_projection_correspondence(self) -> None:
        request = valid_request(
            turn_basis={"turn_basis_id": "projection_correspondence_only_basis"},
            projection=projection_correspondence(),
            blocked_turns=[],
            related_evidence=[],
        )
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        summary = result["carrier_continuity_turn_summary"]
        self.assertIs(summary["projection_mismatch_visible"], True)
        self.assertIs(summary["detailed_basis_distinguished_from_summary"], True)
        self.assertIs(summary["summary_overrode_detailed_basis"], False)
        self.assertIs(summary["predecessor_mutated_or_erased"], False)

    def test_v2_projection_from_blocked_refusal_turns(self) -> None:
        request = valid_request(
            turn_basis=minimal_turn_basis(),
            projection={"projection_correspondence_status": "NOT_APPLICABLE"},
            blocked_turns=blocked_or_refusal_turns(),
            related_evidence=[],
        )
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        statement = result["continuity_turn_statement"]
        summary = result["carrier_continuity_turn_summary"]
        self.assertIs(summary["blocked_attempts_preserved"], True)
        self.assertIs(summary["refusal_preserved"], True)
        self.assertIs(summary["projection_mismatch_visible"], True)
        self.assertIs(statement["blocked_attempts_preserved"], True)
        self.assertIs(statement["refusal_preserved"], True)
        self.assertIs(statement["projection_mismatch_visible"], True)

    def test_v2_projection_from_related_carrier_evidence(self) -> None:
        request = valid_request(
            turn_basis={"turn_basis_id": "related_evidence_only_basis"},
            projection={"projection_correspondence_status": "NOT_APPLICABLE"},
            blocked_turns=[],
            related_evidence=related_carrier_evidence(),
        )
        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        summary = result["carrier_continuity_turn_summary"]
        statement = result["continuity_turn_statement"]
        self.assertIs(summary["refusal_preserved"], True)
        self.assertIs(summary["divergence_preserved"], True)
        self.assertIs(statement["refusal_preserved"], True)
        self.assertIs(statement["divergence_preserved"], True)

    def test_regression_for_live_v1_mismatch_shape(self) -> None:
        result = self.resolve(live_shape_request())
        summary = result["carrier_continuity_turn_summary"]
        for key in (
            "projection_mismatch_visible",
            "blocked_attempts_preserved",
            "refusal_preserved",
            "divergence_preserved",
            "detailed_basis_distinguished_from_summary",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["summary_overrode_detailed_basis"], False)
        self.assertIs(summary["predecessor_mutated_or_erased"], False)

        live_artifact = (
            V1_OUTPUT_ROOT
            / "carrier_c_standing_propagation_v2_projection_successor_turn_001__carrier_continuity_turn_result.json"
        )
        if live_artifact.exists():
            live_summary = boundary.build_carrier_continuity_turn_summary(
                json.loads(live_artifact.read_text(encoding="utf-8"))
            )
            self.assertIs(live_summary["projection_mismatch_visible"], True)
            self.assertIs(live_summary["blocked_attempts_preserved"], True)
            self.assertIs(live_summary["refusal_preserved"], True)
            self.assertIs(live_summary["divergence_preserved"], True)
            self.assertIs(live_summary["detailed_basis_distinguished_from_summary"], True)
            self.assertIs(live_summary["summary_overrode_detailed_basis"], False)
            self.assertIs(live_summary["predecessor_mutated_or_erased"], False)

    def test_declared_question_selected_artifact_and_relation(self) -> None:
        result = self.recorded_result()
        question = result["declared_continuity_turn_question"]
        selected = result["selected_artifact"]
        relation = result["predecessor_successor_relation"]

        self.assertEqual(
            "carrier_continuity_turn_v2_projection_successor_001",
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

        self.assertEqual("standing_propagation_v1_result_001", relation["predecessor_artifact_id"])
        self.assertEqual("standing_propagation_v2_result_001", relation["successor_artifact_id"])
        self.assertIs(relation["successor_relation_claimed"], True)
        self.assertIs(relation["successor_relation_declared"], True)
        self.assertIs(relation["successor_does_not_overwrite_predecessor"], True)
        self.assertIs(relation["successor_does_not_invalidate_predecessor"], True)

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

    def test_statement_non_meaning_and_open_items(self) -> None:
        result = self.recorded_result()
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
        self.assert_no_collapse(statement)

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
            "carrier_continuity_turn_v2_projection_successor_001",
            summary["continuity_turn_request_id"],
        )
        self.assertEqual("standing_propagation_v2_result_001", summary["selected_artifact_id"])
        self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", summary["selected_artifact_outcome"])
        self.assertEqual("PROJECTION_SUCCESSOR_TURN", summary["turn_kind"])
        self.assertEqual("standing_propagation_v1_result_001", summary["predecessor_artifact_id"])
        self.assertEqual("standing_propagation_v2_result_001", summary["successor_artifact_id"])
        self.assertTrue(summary["successor_relation"])
        self.assertTrue(summary["successor_reason"])
        self.assertEqual("SUCCESSOR_PROJECTION_OVER_MISMATCH", summary["projection_correspondence_status"])
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
        self.assertEqual(
            "resolve_carrier_continuity_turn_boundary",
            summary["successor_of_module"],
        )

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        self.assert_required_non_claims_false(self.recorded_result())

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
            "helper_continuity_turn_v2_001",
            "How is carrier-related continuity preserved across turns without flattening or overwrite?",
            selected_artifact(),
            "PROJECTION_SUCCESSOR_TURN",
            detailed_turn_basis(),
            predecessor_artifact=predecessor_artifact(),
            successor_artifact=successor_artifact(),
            successor_reason=successor_reason(),
            projection_correspondence=projection_correspondence(),
            blocked_or_refusal_turns=blocked_or_refusal_turns(),
            related_carrier_evidence=related_carrier_evidence(),
        )
        self.assertEqual("helper_continuity_turn_v2_001", request["continuity_turn_request_id"])
        self.assertEqual("PROJECTION_SUCCESSOR_TURN", request["turn_kind"])
        self.assertEqual(selected_artifact(), request["selected_artifact"])
        self.assertEqual(predecessor_artifact(), request["predecessor_artifact"])
        self.assertEqual(successor_artifact(), request["successor_artifact"])
        self.assertEqual(required_non_claims(), request["declared_non_claims"])

        result = self.resolve(request)
        self.assertEqual(boundary.CARRIER_CONTINUITY_TURN_RECORDED, result["outcome"])
        summary = result["carrier_continuity_turn_summary"]
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["projection_mismatch_visible"], True)
        self.assertIs(summary["blocked_attempts_preserved"], True)
        self.assertIs(summary["refusal_preserved"], True)
        self.assertIs(summary["divergence_preserved"], True)

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

    def test_write_behavior_and_default_v2_output_root(self) -> None:
        result = self.recorded_result()
        self.assertNotEqual(V1_OUTPUT_ROOT, boundary.CARRIER_CONTINUITY_TURN_BOUNDARY_ROOT)
        self.assertIn("_v2", str(boundary.CARRIER_CONTINUITY_TURN_BOUNDARY_ROOT))
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
            self.assertIn("__carrier_continuity_turn_v2_result.json", first.name)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        original = copy.deepcopy(request)
        selected_original = copy.deepcopy(request["selected_artifact"])
        predecessor_original = copy.deepcopy(request["predecessor_artifact"])
        successor_original = copy.deepcopy(request["successor_artifact"])
        related_original = copy.deepcopy(request["related_carrier_evidence"])

        live_artifact = (
            V1_OUTPUT_ROOT
            / "carrier_c_standing_propagation_v2_projection_successor_turn_001__carrier_continuity_turn_result.json"
        )
        live_before = live_artifact.read_text(encoding="utf-8") if live_artifact.exists() else None

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

        if live_before is not None:
            self.assertEqual(live_before, live_artifact.read_text(encoding="utf-8"))

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
        request["turn_kind"] = "STANDING_PROPAGATION_TURN"
        self.assert_block(request, "PREDECESSOR_REQUIRED_BUT_MISSING")

        request = valid_request(include_successor=False)
        request["turn_kind"] = "STANDING_PROPAGATION_TURN"
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
