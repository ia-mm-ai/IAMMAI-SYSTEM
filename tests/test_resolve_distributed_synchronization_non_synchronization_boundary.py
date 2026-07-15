"""Bounded tests for distributed synchronization / non-synchronization review.

These tests prove that the resolver records sync/non-sync boundary posture only.
They do not authorize synchronization, non-synchronized operation, merge, replay,
full body transfer, second-body creation, operation, consequence, or follow-on work.
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

import resolve_distributed_synchronization_non_synchronization_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL = "DISTRIBUTED_SYNC_NON_SYNC_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_SYNC_NON_SYNC_REVIEW_BLOCKED"

ROLE_OUTCOME_RECORDED = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED"
AUTHORITY_OUTCOME_RECORDED = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
ELIGIBILITY_OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_ELIGIBILITY_RECORDED"

SUPPORTED_SYNC_NON_SYNC_POSTURES = tuple(sorted(resolver.SUPPORTED_SYNC_NON_SYNC_POSTURES))
SUPPORTED_CARRIER_ROLE_SHAPES = tuple(sorted(resolver.SUPPORTED_CARRIER_ROLE_SHAPES))
SYNC_NON_SYNC_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS.keys())

ROLE_RESULT_NON_CLAIMS = (
    "carrier_role_activated",
    "carrier_roles_activated",
    "carrier_role_assigned_for_operation",
    "carrier_roles_assigned_for_operation",
    "carrier_authority_created",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "source_replaced",
    "authority_created",
    "permission_created",
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "divergence_resolved",
    "evidence_erased",
    "refusal_erased",
    "blocked_attempt_erased",
    "projection_mismatch_hidden",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

TOP_LEVEL_SECTIONS = (
    "distributed_sync_non_sync_metadata",
    "declared_sync_non_sync_question",
    "selected_carrier_role_result",
    "selected_operation_matter",
    "sync_non_sync_basis",
    "sync_non_sync_postures",
    "sync_non_sync_checks",
    "sync_non_sync_statement",
    "sync_non_sync_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_sync_non_sync_summary",
)


def false_claims(keys: tuple[str, ...]) -> dict[str, bool]:
    return {key: False for key in keys}


def selected_operation_candidate() -> dict[str, object]:
    return {
        "operation_candidate_id": "operation-candidate-001",
        "operation_question": "Should this eligible distributed matter be reviewed later?",
        "operation_purpose": "Preserve a bounded future admission question.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": "Should this eligible distributed matter be reviewed later?",
        "operation_purpose": "Preserve a bounded future admission question.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "matter_remains_declaration_only": True,
    }


def selected_matter_declaration() -> dict[str, object]:
    return {
        "distributed_operation_matter_declaration_result_id": "matter-declaration-result-001",
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARATION_RECORDED",
        "matter_remains_declaration_only": True,
    }


def selected_eligibility_result() -> dict[str, object]:
    return {
        "distributed_operation_eligibility_result_id": "eligibility-result-001",
        "outcome": ELIGIBILITY_OUTCOME_RECORDED,
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "eligibility_remains_eligibility_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def source_body_authority_basis() -> dict[str, object]:
    return {
        "source_body_authority_basis_id": "source-body-authority-basis-001",
        "source_body_lineage_basis": {
            "lineage_basis_id": "source-body-lineage-001",
            "source_body_remains_source_body": True,
        },
        "authority_basis_is_basis_only": True,
        "authority_granted": False,
        "authority_created": False,
        "permission_created": False,
    }


def selected_source_body_authority_result() -> dict[str, object]:
    return {
        "source_body_operational_authority_result_id": "source-authority-result-001",
        "outcome": AUTHORITY_OUTCOME_RECORDED,
        "failed_check_count": "0",
        "source_body_authority_basis": source_body_authority_basis(),
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "source_body_authority_result_remains_authority_basis_only": True,
        "authority_granted": False,
        "authority_created": False,
        "permission_created": False,
        "carrier_roles_defined": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "non_claims": {
            "authority_granted": False,
            "authority_created": False,
            "permission_created": False,
            "carrier_roles_defined": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
        },
        "distributed_source_body_operational_authority_summary": {
            "outcome": AUTHORITY_OUTCOME_RECORDED,
            "failed_check_count": 0,
        },
    }


def selected_carrier_context() -> list[dict[str, object]]:
    return [
        {
            "carrier_id": "carrier-b",
            "carrier_context_kind": "EVIDENCE_CARRIER_CONTEXT",
            "carrier_success_context": True,
            "carrier_context_is_not_authority": True,
            "carrier_context_is_not_currentness": True,
            "carrier_context_is_not_source_replacement": True,
            "carrier_context_is_not_winner_loser_selection": True,
        },
        {
            "carrier_id": "carrier-c",
            "carrier_context_kind": "BLOCKED_OR_REFUSAL_CARRIER_CONTEXT",
            "carrier_block_context": True,
            "carrier_context_is_not_authority": True,
            "carrier_context_is_not_currentness": True,
            "carrier_context_is_not_source_replacement": True,
            "carrier_context_is_not_winner_loser_selection": True,
        },
    ]


def carrier_b_success_context() -> dict[str, object]:
    return {
        "carrier_id": "carrier-b",
        "success_remains_evidence_context_only": True,
        "success_does_not_select_winner": True,
    }


def carrier_c_block_context() -> dict[str, object]:
    return {
        "carrier_id": "carrier-c",
        "block_remains_evidence_context_only": True,
        "block_does_not_invalidate_loser": True,
    }


def b_c_divergence_context() -> dict[str, object]:
    return {
        "divergence_context_id": "b-c-divergence-001",
        "b_c_divergence_remains_visible": True,
        "divergence_resolved": False,
    }


def refusal_blocked_attempt_context() -> dict[str, object]:
    return {
        "refusal_block_context_id": "refusal-block-001",
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
    }


def projection_mismatch_context() -> dict[str, object]:
    return {
        "projection_mismatch_context_id": "projection-mismatch-001",
        "projection_mismatch_remains_visible": True,
    }


def distributed_standing_basis() -> dict[str, object]:
    return {
        "distributed_standing_basis_id": "distributed-standing-basis-001",
        "distributed_standing_basis_remains_basis_only": True,
        "distributed_standing_does_not_create_authority": True,
    }


def carrier_role_basis() -> dict[str, object]:
    return {
        "source_body_authority_basis": source_body_authority_basis(),
        "source_body_lineage_basis": source_body_authority_basis()["source_body_lineage_basis"],
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": carrier_b_success_context(),
        "carrier_c_block_context": carrier_c_block_context(),
        "b_c_divergence_context": b_c_divergence_context(),
        "refusal_blocked_attempt_context": refusal_blocked_attempt_context(),
        "projection_mismatch_context": projection_mismatch_context(),
        "distributed_standing_basis": distributed_standing_basis(),
        "carrier_context_is_not_authority": True,
        "carrier_context_is_not_currentness": True,
        "carrier_context_is_not_source_replacement": True,
        "carrier_context_is_not_winner_loser_selection": True,
        "carrier_context_is_not_hierarchy": True,
        "carrier_context_is_not_operation_admission": True,
        "carrier_context_is_not_operation_authorization": True,
        "carrier_context_is_not_execution": True,
        "carrier_context_is_not_synchronization": True,
        "carrier_context_is_not_full_body_transfer": True,
        "carrier_context_is_not_continuation": True,
        "carrier_context_is_not_consequence": True,
    }


def carrier_role_shapes_section() -> dict[str, object]:
    return {
        "selected_carrier_role_shapes": list(SUPPORTED_CARRIER_ROLE_SHAPES),
        "all_selected_shapes_supported": True,
        "role_shapes_are_context_only": True,
        "role_shapes_are_not_active_operational_roles": True,
        "role_shapes_do_not_create_authority": True,
        "role_shapes_do_not_create_permission": True,
        "role_shapes_do_not_select_current_winning_losing_carrier": True,
        "role_shapes_do_not_make_carrier_source": True,
        "future_operational_role_requires_admission": True,
    }


def selected_carrier_role_result(**overrides: object) -> dict[str, object]:
    statement = {
        "distributed_carrier_operational_role_basis_recorded": True,
        "selected_source_body_authority_result_preserved": True,
        "selected_source_body_authority_result_recorded": True,
        "selected_source_body_authority_result_failed_check_count_zero": True,
        "selected_eligibility_result_preserved": True,
        "selected_matter_declaration_preserved": True,
        "selected_operation_candidate_preserved": True,
        "selected_operation_matter_preserved": True,
        "carrier_role_basis_preserved": True,
        "carrier_role_shapes_preserved": True,
        "carrier_context_preserved": True,
        "carrier_role_shapes_supported": True,
        "carrier_roles_activated": False,
        "carrier_roles_assigned_for_operation": False,
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "consequence_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "failed_check_count": 0,
    }
    result = {
        "distributed_carrier_operational_role_metadata": {
            "distributed_carrier_operational_role_result_id": "carrier-role-result-001",
            "distributed_carrier_operational_role_result_type": "distributed_carrier_operational_role_boundary",
        },
        "selected_source_body_authority_result": selected_source_body_authority_result(),
        "selected_operation_matter": {
            "selected_source_body_authority_result": selected_source_body_authority_result(),
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_matter_declaration": selected_matter_declaration(),
            "selected_operation_candidate": selected_operation_candidate(),
            "selected_operation_matter": selected_operation_matter(),
            "selected_operation_question": selected_operation_candidate()["operation_question"],
            "selected_operation_purpose": selected_operation_candidate()["operation_purpose"],
            "proposed_operation_kind": selected_operation_candidate()["proposed_operation_kind"],
            "carrier_role_basis_remains_role_basis_only": True,
            "carrier_roles_remain_non_active": True,
            "matter_remains_declaration_only": True,
            "candidate_remains_candidate_only": True,
            "eligibility_remains_eligibility_only": True,
            "authority_remains_basis_only": True,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
        },
        "carrier_role_basis": carrier_role_basis(),
        "carrier_role_shapes": carrier_role_shapes_section(),
        "role_checks": [
            {
                "check_name": "selected carrier role result failed check count zero",
                "passed": True,
                "expected_posture": "failed check count 0",
                "actual_posture": "0",
                "block_code": None,
                "failure_code": None,
            }
        ],
        "role_statement": statement,
        "non_claims": false_claims(ROLE_RESULT_NON_CLAIMS),
        "outcome": ROLE_OUTCOME_RECORDED,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "distributed_carrier_operational_role_summary": {
            "outcome": ROLE_OUTCOME_RECORDED,
            "role_request_id": "carrier-role-request-001",
            "selected_carrier_role_result_id": "carrier-role-result-001",
            "selected_source_body_authority_result_id": "source-authority-result-001",
            "selected_source_body_authority_result_outcome": AUTHORITY_OUTCOME_RECORDED,
            "selected_operation_candidate_id": "operation-candidate-001",
            "selected_operation_matter_id": "operation-matter-001",
            "passed_check_count": 39,
            "failed_check_count": "0",
            "distributed_carrier_operational_role_basis_recorded": True,
        },
    }
    result.update(overrides)
    return result


def sync_non_sync_basis() -> dict[str, object]:
    return {
        "carrier_role_basis": carrier_role_basis(),
        "carrier_role_shapes": carrier_role_shapes_section(),
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": carrier_b_success_context(),
        "carrier_c_block_context": carrier_c_block_context(),
        "b_c_divergence_context": b_c_divergence_context(),
        "refusal_blocked_attempt_context": refusal_blocked_attempt_context(),
        "projection_mismatch_context": projection_mismatch_context(),
        "source_body_lineage_basis": source_body_authority_basis()["source_body_lineage_basis"],
        "distributed_standing_basis": distributed_standing_basis(),
        "proposed_synchronization_posture": "NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT",
        "proposed_non_synchronization_posture": "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION",
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "sync_non_sync_basis_is_not_synchronization_authorization": True,
        "sync_non_sync_basis_is_not_non_synchronized_operation_authorization": True,
        "sync_non_sync_basis_is_not_shared_live_state": True,
        "sync_non_sync_basis_is_not_state_merge": True,
        "sync_non_sync_basis_is_not_full_body_transfer": True,
        "sync_non_sync_basis_is_not_second_body": True,
    }


def valid_request(**overrides: object) -> dict[str, object]:
    request = {
        "sync_non_sync_request_id": "sync-non-sync-request-001",
        "sync_non_sync_question": (
            "What synchronization and non-synchronization postures may be "
            "recognized before any future operation admission?"
        ),
        "sync_non_sync_intent": "RECORD_DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY",
        "selected_carrier_role_result": selected_carrier_role_result(),
        "selected_carrier_role_result_id": "carrier-role-result-001",
        "selected_carrier_role_result_outcome": ROLE_OUTCOME_RECORDED,
        "expected_selected_carrier_role_outcome": ROLE_OUTCOME_RECORDED,
        "sync_non_sync_basis": sync_non_sync_basis(),
        "sync_non_sync_postures": list(SUPPORTED_SYNC_NON_SYNC_POSTURES),
        "requested_sync_non_sync_outcome": OUTCOME_RECORDED,
        "selected_carrier_context": selected_carrier_context(),
        "proposed_synchronization_posture": "NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT",
        "proposed_non_synchronization_posture": (
            "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION"
        ),
        "declared_non_claims": false_claims(SYNC_NON_SYNC_NON_CLAIMS),
    }
    request.update(overrides)
    return request


class DistributedSynchronizationNonSynchronizationBoundaryTests(unittest.TestCase):
    """Executable boundary for sync/non-sync posture recording only."""

    def resolve(self, request: object | None = None) -> dict[str, object]:
        return resolver.resolve_distributed_synchronization_non_synchronization_boundary(
            declared_sync_non_sync_request=request
        )

    def assert_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        for key in SYNC_NON_SYNC_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_sync_or_operation_flags(self, statement: dict[str, object]) -> None:
        false_flags = (
            "repository_synchronization_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "non_synchronized_operation_authorized",
            "carrier_autonomy_authorized",
            "stale_carrier_operation_authorized",
            "carrier_role_activated",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "consequence_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        )
        for key in false_flags:
            self.assertIn(key, statement)
            self.assertIs(statement[key], False, key)

    def assert_block_code(self, request: object, expected_code: str) -> dict[str, object]:
        result = self.resolve(request)
        self.assertEqual(OUTCOME_BLOCKED, result["outcome"])
        self.assertEqual(expected_code, result["block"]["block_code"])
        self.assert_false_non_claims(result)
        return result

    def test_successful_boundary_recorded_result(self) -> None:
        result = self.resolve(valid_request())

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(OUTCOME_RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        summary = result["distributed_sync_non_sync_summary"]
        statement = result["sync_non_sync_statement"]
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(statement["distributed_sync_non_sync_boundary_recorded"], True)
        self.assertIs(statement["selected_carrier_role_result_preserved"], True)
        self.assertIs(statement["selected_carrier_role_result_recorded"], True)
        self.assertIs(statement["selected_carrier_role_result_failed_check_count_zero"], True)
        self.assertIs(statement["selected_source_body_authority_result_preserved"], True)
        self.assertIs(statement["selected_eligibility_result_preserved"], True)
        self.assertIs(statement["selected_matter_declaration_preserved"], True)
        self.assertIs(statement["selected_operation_candidate_preserved"], True)
        self.assertIs(statement["selected_operation_matter_preserved"], True)
        self.assertIs(statement["carrier_role_basis_preserved"], True)
        self.assertIs(statement["carrier_role_shapes_preserved"], True)
        self.assertIs(statement["carrier_context_preserved"], True)
        self.assertIs(statement["sync_non_sync_postures_preserved"], True)
        self.assertIs(statement["sync_non_sync_postures_supported"], True)
        self.assertIs(statement["carrier_evidence_remains_unmerged"], True)
        self.assertIs(statement["carrier_context_remains_context_only"], True)
        self.assertIs(statement["divergence_remains_visible"], True)
        self.assertIs(statement["refusal_remains_visible"], True)
        self.assertIs(statement["blocked_attempts_remain_visible"], True)
        self.assertIs(statement["projection_mismatch_remains_visible"], True)
        self.assertIs(statement["future_admission_transition_may_later_review_sync_non_sync"], True)
        self.assert_no_sync_or_operation_flags(statement)
        self.assert_false_non_claims(result)

        emitted = {result["outcome"]}
        self.assertLessEqual(
            emitted,
            {OUTCOME_RECORDED, OUTCOME_NOT_SUFFICIENT, OUTCOME_REQUIRES_ADDITIONAL, OUTCOME_BLOCKED},
        )

    def test_metadata_declared_question_selected_role_and_matter_sections(self) -> None:
        role_result = selected_carrier_role_result()
        original_role_result = copy.deepcopy(role_result)
        result = self.resolve(valid_request(selected_carrier_role_result=role_result))

        metadata = result["distributed_sync_non_sync_metadata"]
        self.assertTrue(metadata["distributed_sync_non_sync_result_id"])
        self.assertTrue(metadata["distributed_sync_non_sync_result_type"])
        self.assertEqual("0.1.0", metadata["distributed_sync_non_sync_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            "resolve_distributed_synchronization_non_synchronization_boundary",
            metadata["resolver_module"],
        )

        question = result["declared_sync_non_sync_question"]
        self.assertEqual("sync-non-sync-request-001", question["sync_non_sync_request_id"])
        self.assertIn("What synchronization", question["sync_non_sync_question"])
        self.assertEqual("RECORD_DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY", question["sync_non_sync_intent"])
        self.assertEqual("carrier-role-result-001", question["selected_carrier_role_result_id"])
        self.assertEqual(ROLE_OUTCOME_RECORDED, question["selected_carrier_role_result_outcome"])
        self.assertIs(question["sync_non_sync_boundary_is_not_synchronization_authorization"], True)
        self.assertIs(question["sync_non_sync_boundary_is_not_non_synchronized_operation_authorization"], True)
        self.assertIs(question["sync_non_sync_boundary_is_not_state_merge"], True)
        self.assertIs(question["sync_non_sync_boundary_is_not_full_body_transfer"], True)
        self.assertIs(question["sync_non_sync_boundary_is_not_second_body"], True)
        self.assertIs(question["sync_non_sync_boundary_is_not_operation_admission"], True)

        selected_role = result["selected_carrier_role_result"]
        self.assertEqual("carrier-role-result-001", selected_role["selected_carrier_role_result_id"])
        self.assertEqual(ROLE_OUTCOME_RECORDED, selected_role["selected_carrier_role_result_outcome"])
        self.assertIsNone(selected_role["selected_carrier_role_result_path"])
        self.assertIs(selected_role["selected_carrier_role_result_outcome_is_recorded"], True)
        self.assertIs(selected_role["selected_carrier_role_result_failed_check_count_zero"], True)
        self.assertIs(selected_role["selected_carrier_role_result_remains_role_basis_only"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_activate_roles"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_assign_carriers_to_operation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_admit_operation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_authorize_operation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_execute_operation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_authorize_sync"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_authorize_full_body_transfer"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_create_second_body"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_authorize_continuation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_authorize_distributed_operation"], True)
        self.assertIs(selected_role["selected_carrier_role_result_did_not_create_consequence"], True)
        self.assertEqual(original_role_result, role_result)

        matter = result["selected_operation_matter"]
        self.assertIn("selected_carrier_role_result", matter)
        self.assertIn("selected_source_body_authority_result", matter)
        self.assertIn("selected_eligibility_result", matter)
        self.assertIn("selected_matter_declaration", matter)
        self.assertEqual("operation-candidate-001", matter["selected_operation_candidate"]["operation_candidate_id"])
        self.assertEqual("operation-matter-001", matter["selected_operation_matter"]["operation_matter_id"])
        self.assertIs(matter["carrier_role_basis_remains_role_basis_only"], True)
        self.assertIs(matter["carrier_roles_remain_non_active"], True)
        self.assertIs(matter["matter_remains_declaration_only"], True)
        self.assertIs(matter["candidate_remains_candidate_only"], True)
        self.assertIs(matter["eligibility_remains_eligibility_only"], True)
        self.assertIs(matter["authority_remains_basis_only"], True)
        self.assertIs(matter["operation_admitted"], False)
        self.assertIs(matter["operation_authorized"], False)
        self.assertIs(matter["operation_executed"], False)

    def test_sync_non_sync_basis_and_supported_postures(self) -> None:
        result = self.resolve(valid_request())
        basis = result["sync_non_sync_basis"]
        postures = result["sync_non_sync_postures"]

        self.assertIn("sync_non_sync_basis", basis)
        self.assertIn("selected_carrier_role_basis", basis)
        self.assertIn("selected_carrier_role_shapes", basis)
        self.assertIn("selected_carrier_context", basis)
        self.assertIn("carrier_b_success_context", basis)
        self.assertIn("carrier_c_block_context", basis)
        self.assertIn("b_c_divergence_context", basis)
        self.assertIn("refusal_blocked_attempt_context", basis)
        self.assertIn("projection_mismatch_context", basis)
        self.assertIn("source_body_lineage_basis", basis)
        self.assertIn("distributed_standing_basis", basis)
        self.assertEqual("NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT", basis["proposed_synchronization_posture"])
        self.assertEqual(
            "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION",
            basis["proposed_non_synchronization_posture"],
        )
        self.assertIs(basis["carrier_evidence_remains_unmerged"], True)
        self.assertIs(basis["carrier_context_remains_context_only"], True)
        self.assertIs(basis["divergence_remains_visible"], True)
        self.assertIs(basis["refusal_remains_visible"], True)
        self.assertIs(basis["blocked_attempts_remain_visible"], True)
        self.assertIs(basis["projection_mismatch_remains_visible"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_synchronization_authorization"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_non_synchronized_operation_authorization"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_shared_live_state"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_state_merge"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_full_body_transfer"], True)
        self.assertIs(basis["sync_non_sync_basis_is_not_second_body"], True)

        self.assertEqual(set(SUPPORTED_SYNC_NON_SYNC_POSTURES), set(postures["selected_sync_non_sync_postures"]))
        self.assertIs(postures["all_selected_postures_supported"], True)
        self.assertIs(postures["postures_are_boundary_postures_only"], True)
        self.assertIs(postures["no_repository_synchronization_by_default"], True)
        self.assertIs(postures["no_shared_live_state_by_default"], True)
        self.assertIs(postures["no_state_merge_by_default"], True)
        self.assertIs(postures["no_full_body_transfer_by_default"], True)
        self.assertIs(postures["no_second_body_by_default"], True)
        self.assertIs(postures["carrier_evidence_remains_unmerged"], True)
        self.assertIs(postures["carrier_context_remains_context_only"], True)
        self.assertIs(postures["divergence_remains_visible"], True)
        self.assertIs(postures["refusal_remains_visible"], True)
        self.assertIs(postures["blocked_attempts_remain_visible"], True)
        self.assertIs(postures["projection_mismatch_remains_visible"], True)
        self.assertIs(postures["future_synchronization_requires_separate_boundary"], True)
        self.assertIs(postures["future_non_synchronized_operation_requires_separate_admission"], True)

        for posture in SUPPORTED_SYNC_NON_SYNC_POSTURES:
            result_for_posture = self.resolve(valid_request(sync_non_sync_postures=[posture]))
            self.assertEqual(OUTCOME_RECORDED, result_for_posture["outcome"], posture)

        self.assert_block_code(
            valid_request(sync_non_sync_postures=["UNSUPPORTED_SYNC_NON_SYNC_POSTURE"]),
            "UNSUPPORTED_SYNC_NON_SYNC_POSTURE",
        )

    def test_checks_non_meaning_open_and_non_claims(self) -> None:
        result = self.resolve(valid_request())
        checks = result["sync_non_sync_checks"]
        self.assertGreater(len(checks), 30)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertEqual(0, result["distributed_sync_non_sync_summary"]["failed_check_count"])

        check_names = {check["check_name"] for check in checks}
        expected_names = {
            "sync/non-sync question declared",
            "sync/non-sync intent supported",
            "selected carrier role result present",
            "selected carrier role result outcome declared",
            "selected carrier role result outcome recorded",
            "selected carrier role result failed check count zero",
            "selected source-body authority result preserved",
            "selected eligibility result preserved",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "carrier role basis preserved",
            "carrier role shapes preserved",
            "carrier context preserved",
            "carrier roles not activated",
            "no carrier assigned to operation",
            "no carrier authority/currentness/hierarchy created",
            "selected sync/non-sync postures supported",
            "no repository synchronization authorized",
            "no shared live state created",
            "no state merge authorized",
            "no replay authorized",
            "no full body transfer authorized",
            "no second body created",
            "no non-synchronized operation authorized",
            "no carrier autonomy authorized",
            "no stale carrier operation authorized",
            "no operation admitted",
            "no operation authorized",
            "no operation executed",
            "divergence remains visible",
            "refusal remains visible",
            "blocked attempts remain visible",
            "projection mismatch remains visible",
            "no consequence/public readiness/final completion/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertLessEqual(expected_names, check_names)

        non_meaning = result["sync_non_sync_non_meaning"]
        for key in (
            "repository_synchronization_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "non_synchronized_operation_authorized",
            "carrier_autonomy_authorized",
            "stale_carrier_operation_authorized",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "carrier_roles_activated",
            "carrier_authority_created",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "source_replaced",
            "authority_created",
            "permission_created",
            "truth_action_created",
            "consequence_created",
            "divergence_resolved",
            "evidence_erased",
            "refusal_erased",
            "blocked_attempt_erased",
            "projection_mismatch_hidden",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], True, key)

        open_section = result["what_remains_open"]
        for key in (
            "distributed_refusal_and_abort_law",
            "distributed_operation_admission_transition_authority",
            "distributed_execution_emission_boundary",
            "distributed_action_consequence_boundary",
            "distributed_operation_receipt_exhaustion",
            "distributed_operation_conformance",
            "distributed_operation_closure",
            "distributed_operation_itself",
            "repository_synchronization",
            "non_synchronized_operation",
            "full_body_transfer",
            "second_body_creation",
            "current_self_orientation_v10",
            "public_launch_readiness",
            "final_governance",
            "final_continuity_completion",
            "final_system_identity",
        ):
            self.assertIn(key, open_section)
            self.assertEqual("open_not_scheduled_not_authorized_not_executed", open_section[key], key)
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)
        self.assert_false_non_claims(result)

    def test_additional_basis_and_not_sufficient_results(self) -> None:
        additional_context = {
            "missing_basis": [
                "selected carrier evidence merge posture not explicit enough",
                "no-sync posture too generic",
                "future sync boundary requirements not specific enough",
                "non-synchronized operation refusal not explicit enough",
                "divergence/refusal preservation needs stronger basis",
                "projection mismatch preservation needs stronger basis",
                "affected-surface sync risk requires clearer classification",
                "proposed output family creates sync ambiguity",
                "admission / transition boundary cannot yet inspect sync/non-sync safely",
            ],
            "additional_basis_reason": "sync/non-sync basis needs stronger preservation detail",
        }
        result = self.resolve(
            valid_request(
                requested_sync_non_sync_outcome=OUTCOME_REQUIRES_ADDITIONAL,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(OUTCOME_REQUIRES_ADDITIONAL, result["outcome"])
        self.assertIs(result["sync_non_sync_statement"]["selected_carrier_role_result_preserved"], True)
        self.assertEqual(additional_context, result["additional_basis_required"]["additional_basis_context"])
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(result["additional_basis_required"]["additional_basis_not_scheduled"], True)
        self.assertIs(result["additional_basis_required"]["additional_basis_not_authorized"], True)
        self.assertIs(result["additional_basis_required"]["additional_basis_not_executed"], True)
        self.assert_no_sync_or_operation_flags(result["sync_non_sync_statement"])
        self.assert_false_non_claims(result)

        not_sufficient_reason = (
            "carrier context implies shared live state and cannot support future "
            "admission review without merge, transfer, second-body, or divergent-operation permission"
        )
        not_sufficient = self.resolve(
            valid_request(
                requested_sync_non_sync_outcome=OUTCOME_NOT_SUFFICIENT,
                not_sufficient_reason=not_sufficient_reason,
            )
        )
        self.assertEqual(OUTCOME_NOT_SUFFICIENT, not_sufficient["outcome"])
        self.assertIs(
            not_sufficient["sync_non_sync_statement"]["selected_carrier_role_result_preserved"],
            True,
        )
        self.assertEqual(
            not_sufficient_reason,
            not_sufficient["sync_non_sync_statement"]["not_sufficient_reason"],
        )
        self.assert_no_sync_or_operation_flags(not_sufficient["sync_non_sync_statement"])
        self.assert_false_non_claims(not_sufficient)

        recorded = self.resolve(valid_request())
        self.assertIs(recorded["additional_basis_required"]["additional_basis_required"], False)
        self.assertEqual({}, recorded["additional_basis_required"]["additional_basis_context"])
        self.assertIs(recorded["additional_basis_required"]["additional_basis_not_scheduled"], True)
        self.assertIs(recorded["additional_basis_required"]["additional_basis_not_authorized"], True)
        self.assertIs(recorded["additional_basis_required"]["additional_basis_not_executed"], True)

    def test_summary_helper_and_request_builder(self) -> None:
        result = self.resolve(valid_request())
        summary = resolver.build_distributed_synchronization_non_synchronization_summary(result)

        self.assertEqual(OUTCOME_RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("sync-non-sync-request-001", summary["sync_non_sync_request_id"])
        self.assertIn("What synchronization", summary["sync_non_sync_question"])
        self.assertEqual("RECORD_DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY", summary["sync_non_sync_intent"])
        self.assertEqual("carrier-role-result-001", summary["selected_carrier_role_result_id"])
        self.assertEqual(ROLE_OUTCOME_RECORDED, summary["selected_carrier_role_result_outcome"])
        self.assertEqual("operation-candidate-001", summary["selected_operation_candidate_id"])
        self.assertEqual("operation-matter-001", summary["selected_operation_matter_id"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["distributed_sync_non_sync_boundary_recorded"], True)
        self.assertIs(summary["sync_non_sync_basis_not_sufficient"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["selected_carrier_role_result_preserved"], True)
        self.assertIs(summary["selected_carrier_role_result_recorded"], True)
        self.assertIs(summary["selected_carrier_role_result_failed_check_count_zero"], True)
        self.assertIs(summary["selected_source_body_authority_result_preserved"], True)
        self.assertIs(summary["selected_eligibility_result_preserved"], True)
        self.assertIs(summary["selected_matter_declaration_preserved"], True)
        self.assertIs(summary["selected_operation_candidate_preserved"], True)
        self.assertIs(summary["selected_operation_matter_preserved"], True)
        self.assertIs(summary["carrier_role_basis_preserved"], True)
        self.assertIs(summary["carrier_role_shapes_preserved"], True)
        self.assertIs(summary["carrier_context_preserved"], True)
        self.assertIs(summary["sync_non_sync_postures_preserved"], True)
        self.assertIs(summary["sync_non_sync_postures_supported"], True)
        self.assertIs(summary["carrier_evidence_remains_unmerged"], True)
        self.assertIs(summary["carrier_context_remains_context_only"], True)
        self.assertIs(summary["divergence_remains_visible"], True)
        self.assertIs(summary["refusal_remains_visible"], True)
        self.assertIs(summary["blocked_attempts_remain_visible"], True)
        self.assertIs(summary["projection_mismatch_remains_visible"], True)
        self.assertIs(summary["future_admission_transition_may_later_review_sync_non_sync"], True)
        for key in (
            "repository_synchronization_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "non_synchronized_operation_authorized",
            "carrier_autonomy_authorized",
            "stale_carrier_operation_authorized",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
        ):
            self.assertIs(summary[key], False, key)
        for key in (
            "consequence_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(summary["key_non_claims"][key], False, key)

        additional_context = {"additional_basis_reason": "need clearer output-family sync posture"}
        not_sufficient_reason = "carrier role shape implies synchronization"
        built = resolver.build_declared_distributed_synchronization_non_synchronization_request(
            "builder-sync-request-001",
            "What postures may be recognized?",
            selected_carrier_role_result(),
            sync_non_sync_basis(),
            list(SUPPORTED_SYNC_NON_SYNC_POSTURES),
            selected_carrier_role_result_id="carrier-role-result-001",
            selected_carrier_role_result_outcome=ROLE_OUTCOME_RECORDED,
            requested_sync_non_sync_outcome=OUTCOME_RECORDED,
            selected_carrier_context=selected_carrier_context(),
            additional_basis_context=additional_context,
            not_sufficient_reason=not_sufficient_reason,
        )
        self.assertEqual("builder-sync-request-001", built["sync_non_sync_request_id"])
        self.assertEqual("What postures may be recognized?", built["sync_non_sync_question"])
        self.assertIn("selected_carrier_role_result", built)
        self.assertEqual(sync_non_sync_basis(), built["sync_non_sync_basis"])
        self.assertEqual(list(SUPPORTED_SYNC_NON_SYNC_POSTURES), built["sync_non_sync_postures"])
        self.assertEqual("carrier-role-result-001", built["selected_carrier_role_result_id"])
        self.assertEqual(ROLE_OUTCOME_RECORDED, built["selected_carrier_role_result_outcome"])
        self.assertEqual(OUTCOME_RECORDED, built["requested_sync_non_sync_outcome"])
        self.assertEqual(selected_carrier_context(), built["selected_carrier_context"])
        self.assertEqual(additional_context, built["additional_basis_context"])
        self.assertEqual(not_sufficient_reason, built["not_sufficient_reason"])
        for value in built["declared_non_claims"].values():
            self.assertIs(value, False)

        resolvable_built = resolver.build_declared_distributed_synchronization_non_synchronization_request(
            "builder-sync-request-002",
            "What postures may be recognized?",
            selected_carrier_role_result(),
            sync_non_sync_basis(),
            list(SUPPORTED_SYNC_NON_SYNC_POSTURES),
            selected_carrier_role_result_id="carrier-role-result-001",
            selected_carrier_role_result_outcome=ROLE_OUTCOME_RECORDED,
            requested_sync_non_sync_outcome=OUTCOME_RECORDED,
            selected_carrier_context=selected_carrier_context(),
        )
        resolved = self.resolve(resolvable_built)
        self.assertEqual(OUTCOME_RECORDED, resolved["outcome"])

    def test_path_based_selected_role_and_request_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            role_path = temp / "selected_carrier_role_result.json"
            role_path.write_text(json.dumps(selected_carrier_role_result()), encoding="utf-8")

            request = valid_request(
                selected_carrier_role_result=None,
                selected_carrier_role_result_path=str(role_path),
            )
            result = self.resolve(request)
            self.assertEqual(OUTCOME_RECORDED, result["outcome"])
            self.assertEqual(str(role_path), result["selected_carrier_role_result"]["selected_carrier_role_result_path"])
            self.assertEqual("carrier-role-result-001", result["selected_carrier_role_result"]["selected_carrier_role_result_id"])
            self.assertEqual(ROLE_OUTCOME_RECORDED, result["selected_carrier_role_result"]["selected_carrier_role_result_outcome"])

            request_path = temp / "declared_sync_non_sync_request.json"
            request_path.write_text(json.dumps(valid_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_synchronization_non_synchronization_boundary_from_path(
                request_path
            )
            mapping_result = self.resolve(valid_request())
            self.assertEqual(OUTCOME_RECORDED, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_sync_non_sync_question"]["sync_non_sync_request_path"],
            )

    def test_write_behavior_default_root_and_no_overwrite(self) -> None:
        result = self.resolve(valid_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "sync_result.json"
            written = resolver.write_distributed_synchronization_non_synchronization_result(
                result,
                explicit_path,
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

        with tempfile.TemporaryDirectory() as temp_dir:
            patched_root = Path(temp_dir) / "sync_non_sync_root"
            carrier_role_root = Path(temp_dir) / "carrier_role_root"
            with patch.object(
                resolver,
                "DISTRIBUTED_SYNCHRONIZATION_NON_SYNCHRONIZATION_BOUNDARY_ROOT",
                patched_root,
            ):
                first = resolver.write_distributed_synchronization_non_synchronization_result(result)
                second = resolver.write_distributed_synchronization_non_synchronization_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertEqual(patched_root, first.parent)
            self.assertEqual(patched_root, second.parent)
            self.assertNotEqual(carrier_role_root, first.parent)
            self.assertNotEqual(first, second)
            self.assertIn("__distributed_sync_non_sync_result", first.name)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        role_result = selected_carrier_role_result()
        basis = sync_non_sync_basis()
        postures = list(SUPPORTED_SYNC_NON_SYNC_POSTURES)
        context = selected_carrier_context()
        request = valid_request(
            selected_carrier_role_result=role_result,
            sync_non_sync_basis=basis,
            sync_non_sync_postures=postures,
            selected_carrier_context=context,
        )
        request_before = copy.deepcopy(request)
        role_before = copy.deepcopy(role_result)
        basis_before = copy.deepcopy(basis)
        postures_before = copy.deepcopy(postures)
        context_before = copy.deepcopy(context)

        first = self.resolve(request)
        second = self.resolve(request)
        self.assertEqual(OUTCOME_RECORDED, first["outcome"])
        self.assertEqual(OUTCOME_RECORDED, second["outcome"])
        self.assertEqual(request_before, request)
        self.assertEqual(role_before, role_result)
        self.assertEqual(basis_before, basis)
        self.assertEqual(postures_before, postures)
        self.assertEqual(context_before, context)

        with tempfile.TemporaryDirectory() as temp_dir:
            role_path = Path(temp_dir) / "role.json"
            authority_path = Path(temp_dir) / "authority.json"
            eligibility_path = Path(temp_dir) / "eligibility.json"
            matter_path = Path(temp_dir) / "matter.json"
            for path, payload in (
                (role_path, selected_carrier_role_result()),
                (authority_path, selected_source_body_authority_result()),
                (eligibility_path, selected_eligibility_result()),
                (matter_path, selected_matter_declaration()),
            ):
                path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            snapshots = {path: path.read_text(encoding="utf-8") for path in (role_path, authority_path, eligibility_path, matter_path)}
            with patch.object(
                resolver,
                "DISTRIBUTED_SYNCHRONIZATION_NON_SYNCHRONIZATION_BOUNDARY_ROOT",
                Path(temp_dir) / "output",
            ):
                resolver.write_distributed_synchronization_non_synchronization_result(first)
            for path, before in snapshots.items():
                self.assertEqual(before, path.read_text(encoding="utf-8"), path)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        explicit = self.assert_block_code(
            valid_request(sync_non_sync_intent="BLOCK_DISTRIBUTED_SYNC_NON_SYNC_REVIEW"),
            "SYNC_NON_SYNC_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assertIs(explicit["sync_non_sync_statement"]["distributed_sync_non_sync_boundary_recorded"], False)

        self.assert_block_code(None, "SYNC_NON_SYNC_QUESTION_UNDECLARED")
        self.assert_block_code("not-a-mapping", "DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED")
        self.assert_block_code(valid_request(sync_non_sync_question=""), "SYNC_NON_SYNC_QUESTION_UNDECLARED")
        self.assert_block_code(
            valid_request(sync_non_sync_intent="UNSUPPORTED_SYNC_INTENT"),
            "SYNC_NON_SYNC_INTENT_UNSUPPORTED",
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            missing = temp / "missing.json"
            missing_result = resolver.resolve_distributed_synchronization_non_synchronization_boundary_from_path(
                missing
            )
            self.assertEqual(OUTCOME_BLOCKED, missing_result["outcome"])
            self.assertEqual(
                "DECLARED_SYNC_NON_SYNC_REQUEST_UNREADABLE",
                missing_result["block"]["block_code"],
            )

            malformed = temp / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            malformed_result = resolver.resolve_distributed_synchronization_non_synchronization_boundary_from_path(
                malformed
            )
            self.assertEqual(OUTCOME_BLOCKED, malformed_result["outcome"])
            self.assertEqual(
                "DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED",
                malformed_result["block"]["block_code"],
            )

            array_path = temp / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_synchronization_non_synchronization_boundary_from_path(
                array_path
            )
            self.assertEqual(OUTCOME_BLOCKED, array_result["outcome"])
            self.assertEqual(
                "DECLARED_SYNC_NON_SYNC_REQUEST_MALFORMED",
                array_result["block"]["block_code"],
            )

    def test_selected_carrier_role_path_and_result_issue_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            missing = temp / "missing-role.json"
            self.assert_block_code(
                valid_request(
                    selected_carrier_role_result=None,
                    selected_carrier_role_result_path=str(missing),
                ),
                "CARRIER_ROLE_RESULT_UNREADABLE",
            )

            malformed = temp / "malformed-role.json"
            malformed.write_text("{", encoding="utf-8")
            self.assert_block_code(
                valid_request(
                    selected_carrier_role_result=None,
                    selected_carrier_role_result_path=str(malformed),
                ),
                "CARRIER_ROLE_RESULT_MALFORMED",
            )

            array_path = temp / "array-role.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assert_block_code(
                valid_request(
                    selected_carrier_role_result=None,
                    selected_carrier_role_result_path=str(array_path),
                ),
                "CARRIER_ROLE_RESULT_MALFORMED",
            )

        missing_outcome = selected_carrier_role_result()
        missing_outcome.pop("outcome", None)
        missing_outcome["distributed_carrier_operational_role_summary"].pop("outcome", None)
        self.assert_block_code(
            valid_request(selected_carrier_role_result=missing_outcome),
            "CARRIER_ROLE_RESULT_OUTCOME_MISSING",
        )

        not_recorded = selected_carrier_role_result()
        not_recorded["outcome"] = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_NOT_SUFFICIENT"
        not_recorded["distributed_carrier_operational_role_summary"]["outcome"] = (
            "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_NOT_SUFFICIENT"
        )
        self.assert_block_code(
            valid_request(selected_carrier_role_result=not_recorded),
            "CARRIER_ROLE_RESULT_NOT_RECORDED",
        )

        failed_checks = selected_carrier_role_result()
        failed_checks["role_statement"]["failed_check_count"] = "1"
        failed_checks["distributed_carrier_operational_role_summary"]["failed_check_count"] = 1
        self.assert_block_code(
            valid_request(selected_carrier_role_result=failed_checks),
            "CARRIER_ROLE_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_basis_blocks(self) -> None:
        self.assert_block_code(valid_request(selected_carrier_role_result=None), "CARRIER_ROLE_RESULT_MISSING")

        cases = (
            ("selected_source_body_authority_result", "SOURCE_BODY_AUTHORITY_RESULT_MISSING"),
            ("selected_eligibility_result", "SELECTED_ELIGIBILITY_RESULT_MISSING"),
            ("selected_matter_declaration", "SELECTED_MATTER_DECLARATION_MISSING"),
            ("selected_operation_candidate", "SELECTED_OPERATION_CANDIDATE_MISSING"),
            ("selected_operation_matter", "SELECTED_OPERATION_MATTER_MISSING"),
        )
        for key, code in cases:
            role = selected_carrier_role_result()
            if key == "selected_source_body_authority_result":
                role.pop("selected_source_body_authority_result", None)
            role["selected_operation_matter"].pop(key, None)
            role_eligibility = role["selected_operation_matter"].get("selected_eligibility_result")
            if isinstance(role_eligibility, dict):
                role_eligibility.pop(key, None)
            authority = role.get("selected_source_body_authority_result")
            if isinstance(authority, dict):
                authority_eligibility = authority.get("selected_eligibility_result")
                if isinstance(authority_eligibility, dict):
                    authority_eligibility.pop(key, None)
            with self.subTest(key=key):
                self.assert_block_code(valid_request(selected_carrier_role_result=role), code)

        request_missing_basis = valid_request()
        request_missing_basis["sync_non_sync_basis"].pop("carrier_role_basis", None)
        request_missing_basis["selected_carrier_role_result"].pop("carrier_role_basis", None)
        self.assert_block_code(request_missing_basis, "CARRIER_ROLE_BASIS_MISSING")

        request_missing_shapes = valid_request()
        request_missing_shapes["sync_non_sync_basis"].pop("carrier_role_shapes", None)
        request_missing_shapes["selected_carrier_role_result"].pop("carrier_role_shapes", None)
        self.assert_block_code(request_missing_shapes, "CARRIER_ROLE_SHAPES_MISSING")

    def test_carrier_context_and_posture_blocks(self) -> None:
        self.assert_block_code(
            valid_request(selected_carrier_context="malformed carrier context"),
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        )
        self.assert_block_code(
            valid_request(sync_non_sync_postures=["UNSUPPORTED_SYNC_NON_SYNC_POSTURE"]),
            "UNSUPPORTED_SYNC_NON_SYNC_POSTURE",
        )

    def test_sync_collapse_flags_block_with_representative_codes(self) -> None:
        collapse_cases = (
            ("repository_synchronization_authorized", "SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC"),
            ("shared_live_state_created", "SYNC_REVIEW_CREATES_SHARED_LIVE_STATE"),
            ("state_merge_authorized", "SYNC_REVIEW_AUTHORIZES_STATE_MERGE"),
            ("replay_authorized", "SYNC_REVIEW_AUTHORIZES_REPLAY"),
            ("full_body_transfer_authorized", "SYNC_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "SYNC_REVIEW_CREATES_SECOND_BODY"),
            ("non_synchronized_operation_authorized", "NON_SYNC_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION"),
            ("carrier_autonomy_authorized", "NON_SYNC_REVIEW_AUTHORIZES_CARRIER_AUTONOMY"),
            ("stale_carrier_operation_authorized", "NON_SYNC_REVIEW_AUTHORIZES_STALE_CARRIER_OPERATION"),
            ("operation_admitted", "SYNC_NON_SYNC_REVIEW_ADMITS_OPERATION"),
            ("operation_authorized", "SYNC_NON_SYNC_REVIEW_AUTHORIZES_OPERATION"),
            ("operation_executed", "SYNC_NON_SYNC_REVIEW_EXECUTES_OPERATION"),
            ("carrier_role_activated", "SYNC_NON_SYNC_REVIEW_ACTIVATES_CARRIER_ROLES"),
            ("carrier_authority_created", "SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_AUTHORITY"),
            ("carrier_currentness_created", "SYNC_NON_SYNC_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "SYNC_NON_SYNC_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "SYNC_NON_SYNC_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "SYNC_NON_SYNC_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "SYNC_NON_SYNC_REVIEW_REPLACES_SOURCE"),
            ("truth_created", "SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("action_authorized", "SYNC_NON_SYNC_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "SYNC_NON_SYNC_REVIEW_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "SYNC_NON_SYNC_REVIEW_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("blocked_attempt_erased", "SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("projection_mismatch_hidden", "SYNC_NON_SYNC_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "SYNC_NON_SYNC_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "SYNC_NON_SYNC_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "SYNC_NON_SYNC_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for flag, expected_code in collapse_cases:
            request = valid_request()
            request["declared_non_claims"][flag] = True
            with self.subTest(flag=flag):
                self.assert_block_code(request, expected_code)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            request = valid_request()
            request["declared_non_claims"][flag] = True
            with self.subTest(flag=flag):
                self.assert_block_code(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = valid_request()
        missing_non_claim["declared_non_claims"].pop("repository_synchronization_authorized")
        self.assert_block_code(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = valid_request()
        flipped_non_claim["declared_non_claims"]["repository_synchronization_authorized"] = True
        flipped = self.resolve(flipped_non_claim)
        self.assertEqual(OUTCOME_BLOCKED, flipped["outcome"])
        self.assertIn(
            flipped["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "SYNC_REVIEW_AUTHORIZES_REPOSITORY_SYNC"},
        )


if __name__ == "__main__":
    unittest.main()
