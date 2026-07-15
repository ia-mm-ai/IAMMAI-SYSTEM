"""Bounded tests for distributed refusal / abort boundary review.

These tests prove that the resolver records pre-admission refusal / abort
postures only. They do not refuse or abort a live operation, admit operation,
authorize operation, execute operation, authorize synchronization or no-sync
operation, transfer a body, create a second body, create consequence, or
schedule follow-on work.
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

import resolve_distributed_refusal_abort_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL = "DISTRIBUTED_REFUSAL_ABORT_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_REFUSAL_ABORT_REVIEW_BLOCKED"
SYNC_OUTCOME_RECORDED = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED"

SUPPORTED_REFUSAL_ABORT_POSTURES = tuple(resolver.SUPPORTED_REFUSAL_ABORT_POSTURES)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_refusal_abort_metadata",
    "declared_refusal_abort_question",
    "selected_sync_non_sync_result",
    "selected_operation_matter",
    "refusal_abort_basis",
    "refusal_abort_postures",
    "refusal_abort_checks",
    "refusal_abort_statement",
    "refusal_abort_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_refusal_abort_summary",
)


def false_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def selected_operation_candidate() -> dict[str, object]:
    return {
        "operation_candidate_id": "operation-candidate-001",
        "operation_question": "What refusal / abort posture is required before admission?",
        "operation_purpose": "Preserve a bounded future admission question.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": "What refusal / abort posture is required before admission?",
        "operation_purpose": "Preserve a bounded future admission question.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "matter_remains_declaration_only": True,
    }


def selected_matter_declaration() -> dict[str, object]:
    return {
        "distributed_operation_matter_declaration_result_id": "matter-declaration-001",
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARATION_RECORDED",
        "matter_remains_declaration_only": True,
    }


def selected_eligibility_result() -> dict[str, object]:
    return {
        "distributed_operation_eligibility_result_id": "eligibility-result-001",
        "outcome": "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW",
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "eligibility_remains_eligibility_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def selected_source_body_authority_result() -> dict[str, object]:
    return {
        "source_body_operational_authority_result_id": "source-authority-result-001",
        "outcome": "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED",
        "failed_check_count": 0,
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "source_body_authority_basis": {
            "source_body_authority_basis_id": "source-authority-basis-001",
            "source_body_lineage_basis": {"lineage_basis_id": "source-lineage-001"},
            "authority_basis_is_basis_only": True,
        },
        "authority_granted": False,
        "authority_created": False,
        "permission_created": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def selected_carrier_context() -> list[dict[str, object]]:
    return [
        {
            "carrier_id": "carrier-b",
            "carrier_context_kind": "EVIDENCE_CARRIER_CONTEXT",
            "success_remains_evidence_context_only": True,
        },
        {
            "carrier_id": "carrier-c",
            "carrier_context_kind": "BLOCKED_OR_REFUSAL_CARRIER_CONTEXT",
            "block_remains_evidence_context_only": True,
        },
    ]


def selected_carrier_role_result() -> dict[str, object]:
    return {
        "distributed_carrier_operational_role_metadata": {
            "distributed_carrier_operational_role_result_id": "carrier-role-result-001",
        },
        "outcome": "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED",
        "distributed_carrier_operational_role_summary": {"failed_check_count": 0},
        "selected_operation_matter": {
            "selected_source_body_authority_result": selected_source_body_authority_result(),
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_matter_declaration": selected_matter_declaration(),
            "selected_operation_candidate": selected_operation_candidate(),
            "selected_operation_matter": selected_operation_matter(),
            "selected_operation_question": "What refusal / abort posture is required before admission?",
            "selected_operation_purpose": "Preserve a bounded future admission question.",
            "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        },
        "carrier_role_basis": {
            "selected_carrier_context": selected_carrier_context(),
            "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
            "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
            "b_c_divergence_context": {"divergence_visible": True},
            "refusal_blocked_attempt_context": {"refusal_visible": True},
            "projection_mismatch_context": {"projection_mismatch_visible": True},
        },
        "carrier_role_shapes": {
            "selected_carrier_role_shapes": [
                "EVIDENCE_CARRIER_CONTEXT",
                "BLOCKED_OR_REFUSAL_CARRIER_CONTEXT",
                "DIVERGENCE_CONTEXT_CARRIER",
                "FUTURE_OPERATIONAL_ROLE_REQUIRES_ADMISSION",
            ],
            "all_selected_shapes_supported": True,
        },
        "role_statement": {
            "carrier_roles_activated": False,
            "carrier_roles_assigned_for_operation": False,
            "carrier_authority_created": False,
            "carrier_currentness_created": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
        },
        "non_claims": {
            "carrier_role_activated": False,
            "carrier_role_assigned_for_operation": False,
            "carrier_authority_created": False,
            "carrier_currentness_created": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "consequence_created": False,
        },
    }


def sync_non_sync_posture_basis() -> dict[str, object]:
    return {
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
        "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {"refusal_visible": True, "blocked_attempt_visible": True},
        "projection_mismatch_context": {"projection_mismatch_visible": True},
        "source_body_lineage_basis": {"lineage_basis_id": "source-lineage-001"},
        "distributed_standing_basis": {"standing_basis_id": "standing-basis-001", "basis_only": True},
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
    }


def selected_sync_non_sync_result() -> dict[str, object]:
    carrier_role_result = selected_carrier_role_result()
    return {
        "distributed_sync_non_sync_metadata": {
            "distributed_sync_non_sync_result_id": "sync-non-sync-result-001",
            "distributed_sync_non_sync_result_type": "distributed_synchronization_non_synchronization_boundary_result",
            "distributed_sync_non_sync_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_synchronization_non_synchronization_boundary",
        },
        "outcome": SYNC_OUTCOME_RECORDED,
        "distributed_sync_non_sync_summary": {"outcome": SYNC_OUTCOME_RECORDED, "failed_check_count": 0},
        "selected_operation_matter": {
            "selected_carrier_role_result": carrier_role_result,
            "selected_source_body_authority_result": selected_source_body_authority_result(),
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_matter_declaration": selected_matter_declaration(),
            "selected_operation_candidate": selected_operation_candidate(),
            "selected_operation_matter": selected_operation_matter(),
            "selected_operation_question": "What refusal / abort posture is required before admission?",
            "selected_operation_purpose": "Preserve a bounded future admission question.",
            "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        },
        "sync_non_sync_basis": sync_non_sync_posture_basis(),
        "sync_non_sync_postures": {
            "selected_sync_non_sync_postures": [
                "NO_REPOSITORY_SYNCHRONIZATION_BY_DEFAULT",
                "NO_SHARED_LIVE_STATE_BY_DEFAULT",
                "NO_STATE_MERGE_BY_DEFAULT",
                "NO_FULL_BODY_TRANSFER_BY_DEFAULT",
                "NO_SECOND_BODY_BY_DEFAULT",
                "CARRIER_EVIDENCE_REMAINS_UNMERGED",
                "CARRIER_CONTEXT_REMAINS_CONTEXT_ONLY",
                "DIVERGENCE_REMAINS_VISIBLE",
                "REFUSAL_REMAINS_VISIBLE",
                "BLOCKED_ATTEMPTS_REMAIN_VISIBLE",
                "PROJECTION_MISMATCH_REMAINS_VISIBLE",
                "FUTURE_SYNCHRONIZATION_REQUIRES_SEPARATE_BOUNDARY",
                "FUTURE_NON_SYNCHRONIZED_OPERATION_REQUIRES_SEPARATE_ADMISSION",
            ],
            "all_selected_postures_supported": True,
        },
        "sync_non_sync_statement": {
            "selected_carrier_role_result_preserved": True,
            "selected_source_body_authority_result_preserved": True,
            "selected_eligibility_result_preserved": True,
            "selected_matter_declaration_preserved": True,
            "selected_operation_candidate_preserved": True,
            "selected_operation_matter_preserved": True,
            "sync_non_sync_postures_preserved": True,
            "carrier_evidence_remains_unmerged": True,
            "carrier_context_remains_context_only": True,
            "divergence_remains_visible": True,
            "refusal_remains_visible": True,
            "blocked_attempts_remain_visible": True,
            "projection_mismatch_remains_visible": True,
            "repository_synchronization_authorized": False,
            "shared_live_state_created": False,
            "state_merge_authorized": False,
            "replay_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "non_synchronized_operation_authorized": False,
            "carrier_autonomy_authorized": False,
            "stale_carrier_operation_authorized": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "consequence_created": False,
            "public_launch_readiness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
            "failed_check_count": 0,
        },
        "non_claims": false_claims(),
    }


def refusal_abort_basis() -> dict[str, object]:
    return {
        "sync_non_sync_posture_basis": sync_non_sync_posture_basis(),
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
        "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {"refusal_visible": True, "blocked_attempt_visible": True},
        "projection_mismatch_context": {"projection_mismatch_visible": True},
        "source_body_lineage_basis": {"lineage_basis_id": "source-lineage-001"},
        "distributed_standing_basis": {"standing_basis_id": "standing-basis-001", "basis_only": True},
        "carrier_b_success_does_not_force_continuation": True,
        "carrier_c_block_remains_visible": True,
        "carrier_c_block_does_not_invalidate_carrier_c": True,
        "b_c_divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "sync_non_sync_posture_cannot_be_overread_into_operation": True,
        "no_sync_cannot_be_overread_into_independent_carrier_operation": True,
        "sync_failure_cannot_be_overread_into_whole_body_failure_by_default": True,
        "refusal_abort_basis_is_not_live_refusal": True,
        "refusal_abort_basis_is_not_live_abort": True,
        "refusal_abort_basis_is_not_operation_admission": True,
        "refusal_abort_basis_is_not_operation_authorization": True,
        "refusal_abort_basis_is_not_execution": True,
    }


def declared_refusal_abort_request(**overrides: object) -> dict[str, object]:
    request = {
        "refusal_abort_request_id": "refusal-abort-request-001",
        "refusal_abort_question": (
            "What refusal, abort, stop, and non-admission postures must be preserved "
            "before any future operation admission?"
        ),
        "refusal_abort_intent": "RECORD_DISTRIBUTED_REFUSAL_ABORT_BOUNDARY",
        "selected_sync_non_sync_result": selected_sync_non_sync_result(),
        "selected_sync_non_sync_result_id": "sync-non-sync-result-001",
        "selected_sync_non_sync_result_outcome": SYNC_OUTCOME_RECORDED,
        "requested_refusal_abort_outcome": OUTCOME_RECORDED,
        "refusal_abort_basis": refusal_abort_basis(),
        "sync_non_sync_posture_basis": sync_non_sync_posture_basis(),
        "refusal_abort_postures": list(SUPPORTED_REFUSAL_ABORT_POSTURES),
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
        "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {"refusal_visible": True, "blocked_attempt_visible": True},
        "projection_mismatch_context": {"projection_mismatch_visible": True},
        "source_body_lineage_basis": {"lineage_basis_id": "source-lineage-001"},
        "distributed_standing_basis": {"standing_basis_id": "standing-basis-001", "basis_only": True},
        "declared_non_claims": false_claims(),
    }
    request.update(overrides)
    return request


def resolve_request(**overrides: object) -> dict[str, object]:
    return resolver.resolve_distributed_refusal_abort_boundary(
        declared_refusal_abort_request=declared_refusal_abort_request(**overrides)
    )


class DistributedRefusalAbortBoundaryTests(unittest.TestCase):
    def assert_false_non_claims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_refusal_abort_or_operation_flags(self, statement: dict[str, object]) -> None:
        for key in (
            "live_operation_refused",
            "live_operation_aborted",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
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
            "carrier_authority_created",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "source_replaced",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(statement[key], False, key)

    def valid_result(self) -> dict[str, object]:
        result = resolve_request()
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        return result

    def test_successful_refusal_abort_boundary_recorded_result(self) -> None:
        result = self.valid_result()
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertIsInstance(result, dict)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["distributed_refusal_abort_summary"]["failed_check_count"], 0)

        statement = result["refusal_abort_statement"]
        for key in (
            "distributed_refusal_abort_boundary_recorded",
            "selected_sync_non_sync_result_preserved",
            "selected_sync_non_sync_result_recorded",
            "selected_sync_non_sync_result_failed_check_count_zero",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "refusal_abort_postures_preserved",
            "refusal_abort_postures_supported",
            "non_admission_conditions_named",
            "abort_conditions_named",
            "carrier_b_success_does_not_force_continuation",
            "carrier_c_block_remains_visible",
            "carrier_c_block_does_not_invalidate_carrier_c",
            "sync_non_sync_posture_not_overread_into_operation",
            "future_admission_transition_must_preserve_refusal_abort",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_no_refusal_abort_or_operation_flags(statement)

    def test_metadata_and_declared_question_are_preserved(self) -> None:
        result = self.valid_result()
        metadata = result["distributed_refusal_abort_metadata"]
        for key in (
            "distributed_refusal_abort_result_id",
            "distributed_refusal_abort_result_type",
            "distributed_refusal_abort_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["distributed_refusal_abort_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_distributed_refusal_abort_boundary")

        declared = result["declared_refusal_abort_question"]
        self.assertEqual(declared["refusal_abort_request_id"], "refusal-abort-request-001")
        self.assertEqual(declared["refusal_abort_intent"], "RECORD_DISTRIBUTED_REFUSAL_ABORT_BOUNDARY")
        self.assertEqual(declared["selected_sync_non_sync_result_id"], "sync-non-sync-result-001")
        self.assertEqual(declared["selected_sync_non_sync_result_outcome"], SYNC_OUTCOME_RECORDED)
        for key in (
            "refusal_abort_boundary_is_not_live_refusal",
            "refusal_abort_boundary_is_not_live_abort",
            "refusal_abort_boundary_is_not_operation_admission",
            "refusal_abort_boundary_is_not_operation_authorization",
            "refusal_abort_boundary_is_not_operation_execution",
            "refusal_abort_boundary_is_not_consequence",
        ):
            self.assertIs(declared[key], True, key)

    def test_selected_sync_result_and_operation_matter_are_preserved(self) -> None:
        original_request = declared_refusal_abort_request()
        original_sync = copy.deepcopy(original_request["selected_sync_non_sync_result"])
        result = resolver.resolve_distributed_refusal_abort_boundary(original_request)

        selected_sync = result["selected_sync_non_sync_result"]
        self.assertEqual(selected_sync["selected_sync_non_sync_result_id"], "sync-non-sync-result-001")
        self.assertEqual(selected_sync["selected_sync_non_sync_result_outcome"], SYNC_OUTCOME_RECORDED)
        self.assertIs(selected_sync["selected_sync_non_sync_result_outcome_is_recorded"], True)
        self.assertIs(selected_sync["selected_sync_non_sync_result_failed_check_count_zero"], True)
        for key in (
            "selected_sync_non_sync_result_remains_boundary_posture_only",
            "selected_sync_non_sync_result_did_not_authorize_synchronization",
            "selected_sync_non_sync_result_did_not_authorize_non_synchronized_operation",
            "selected_sync_non_sync_result_did_not_create_shared_live_state",
            "selected_sync_non_sync_result_did_not_authorize_merge",
            "selected_sync_non_sync_result_did_not_authorize_replay",
            "selected_sync_non_sync_result_did_not_authorize_full_body_transfer",
            "selected_sync_non_sync_result_did_not_create_second_body",
            "selected_sync_non_sync_result_did_not_admit_operation",
            "selected_sync_non_sync_result_did_not_authorize_operation",
            "selected_sync_non_sync_result_did_not_execute_operation",
            "selected_sync_non_sync_result_preserved_divergence",
            "selected_sync_non_sync_result_preserved_refusal",
            "selected_sync_non_sync_result_preserved_blocked_attempts",
            "selected_sync_non_sync_result_preserved_projection_mismatch",
            "selected_sync_non_sync_result_is_not_mutated",
        ):
            self.assertIs(selected_sync[key], True, key)
        self.assertEqual(original_request["selected_sync_non_sync_result"], original_sync)

        matter = result["selected_operation_matter"]
        self.assertIn("selected_sync_non_sync_result", matter)
        self.assertIn("selected_carrier_role_result", matter)
        self.assertIn("selected_source_body_authority_result", matter)
        self.assertIn("selected_eligibility_result", matter)
        self.assertIn("selected_matter_declaration", matter)
        self.assertEqual(matter["selected_operation_candidate"]["operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(matter["selected_operation_matter"]["operation_matter_id"], "operation-matter-001")
        self.assertIs(matter["sync_non_sync_remains_boundary_posture_only"], True)
        self.assertIs(matter["carrier_role_basis_remains_role_basis_only"], True)
        self.assertIs(matter["authority_remains_basis_only"], True)
        self.assertIs(matter["eligibility_remains_eligibility_only"], True)
        self.assertIs(matter["matter_remains_declaration_only"], True)
        self.assertIs(matter["operation_admitted"], False)
        self.assertIs(matter["operation_authorized"], False)
        self.assertIs(matter["operation_executed"], False)

    def test_refusal_abort_basis_preserves_context_without_overread(self) -> None:
        basis = self.valid_result()["refusal_abort_basis"]
        for key in (
            "selected_sync_non_sync_result",
            "sync_non_sync_posture_basis",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_carrier_context",
            "carrier_b_success_context",
            "carrier_c_block_context",
            "b_c_divergence_context",
            "refusal_blocked_attempt_context",
            "projection_mismatch_context",
            "source_body_lineage_basis",
            "distributed_standing_basis",
        ):
            self.assertTrue(basis[key], key)
        for key in (
            "carrier_b_success_does_not_force_continuation",
            "carrier_c_block_remains_visible",
            "carrier_c_block_does_not_invalidate_carrier_c",
            "b_c_divergence_remains_visible",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "sync_non_sync_posture_cannot_be_overread_into_operation",
            "no_sync_cannot_be_overread_into_independent_carrier_operation",
            "sync_failure_cannot_be_overread_into_whole_body_failure_by_default",
            "refusal_abort_basis_is_not_live_refusal",
            "refusal_abort_basis_is_not_live_abort",
            "refusal_abort_basis_is_not_operation_admission",
            "refusal_abort_basis_is_not_operation_authorization",
            "refusal_abort_basis_is_not_execution",
        ):
            self.assertIs(basis[key], True, key)

    def test_supported_refusal_abort_postures_are_recordable(self) -> None:
        for posture in SUPPORTED_REFUSAL_ABORT_POSTURES:
            with self.subTest(posture=posture):
                companion = (
                    "NO_OPERATION_ADMISSION_WITHOUT_REFUSAL_ABORT_BOUNDARY"
                    if posture.startswith("ABORT_IF_")
                    else "ABORT_IF_OPERATION_SCOPE_EXPANDS"
                )
                request = declared_refusal_abort_request(
                    refusal_abort_postures=[posture, companion]
                )
                result = resolver.resolve_distributed_refusal_abort_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_RECORDED)
                selected = result["refusal_abort_postures"]["selected_refusal_abort_postures"]
                self.assertIn(posture, selected)
                self.assertIs(result["refusal_abort_postures"]["all_selected_postures_supported"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_are_boundary_postures_only"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_are_pre_admission_safety_conditions"], True)
                self.assertIs(result["refusal_abort_postures"]["non_admission_conditions_named"], True)
                self.assertIs(result["refusal_abort_postures"]["abort_conditions_named"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_do_not_execute_live_refusal"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_do_not_execute_live_abort"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_do_not_authorize_operation"], True)
                self.assertIs(result["refusal_abort_postures"]["postures_do_not_create_consequence"], True)

    def test_unsupported_refusal_abort_posture_blocks(self) -> None:
        result = resolve_request(refusal_abort_postures=["AUTHORIZE_LIVE_ABORT_NOW"])
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["block_code"], "UNSUPPORTED_REFUSAL_ABORT_POSTURE")

    def test_refusal_abort_checks_are_explicit_and_pass_for_recorded(self) -> None:
        result = self.valid_result()
        checks = result["refusal_abort_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertIs(check["passed"], True, check["check_name"])
        self.assertEqual(result["distributed_refusal_abort_summary"]["failed_check_count"], 0)
        names = {check["check_name"] for check in checks}
        expected_names = {
            "refusal / abort question declared",
            "refusal / abort intent supported",
            "selected sync/non-sync result present",
            "selected sync/non-sync result outcome declared",
            "selected sync/non-sync result outcome recorded",
            "selected sync/non-sync result failed check count zero",
            "selected carrier role result preserved",
            "selected source-body authority result preserved",
            "selected eligibility result preserved",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "sync/non-sync postures preserved",
            "carrier evidence remains unmerged",
            "carrier context remains context only",
            "divergence remains visible",
            "refusal remains visible",
            "blocked attempts remain visible",
            "projection mismatch remains visible",
            "selected refusal / abort postures supported",
            "no live operation refused",
            "no live operation aborted",
            "no operation admitted",
            "no operation authorized",
            "no operation executed",
            "no synchronization/shared live state/merge/replay/full body transfer/second body",
            "no non-synchronized operation/carrier autonomy/stale carrier operation",
            "no carrier role activated",
            "no carrier authority/currentness/hierarchy created",
            "no current/winning/losing carrier selected",
            "no source replacement",
            "no consequence created",
            "no public readiness/final completion/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_additional_basis_required_result_preserves_no_execution(self) -> None:
        context = {
            "additional_basis_reason": "refusal trigger basis too generic",
            "missing_basis": [
                "abort trigger basis too generic",
                "non-admission conditions incomplete",
                "projection mismatch requires stronger stop-condition basis",
            ],
        }
        result = resolve_request(
            requested_refusal_abort_outcome=OUTCOME_REQUIRES_ADDITIONAL,
            additional_basis_context=context,
        )
        self.assertEqual(result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertIs(result["refusal_abort_statement"]["selected_sync_non_sync_result_preserved"], True)
        self.assertEqual(result["additional_basis_required"]["additional_basis_context"], context)
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        for key in (
            "additional_basis_not_scheduled",
            "additional_basis_not_authorized",
            "additional_basis_not_executed",
            "missing_basis_not_scheduled",
            "missing_basis_not_authorized",
            "missing_basis_not_executed",
        ):
            self.assertIs(result["additional_basis_required"][key], True, key)
        self.assert_no_refusal_abort_or_operation_flags(result["refusal_abort_statement"])

    def test_not_sufficient_result_preserves_reason_and_no_mutation(self) -> None:
        request = declared_refusal_abort_request(
            requested_refusal_abort_outcome=OUTCOME_NOT_SUFFICIENT,
            not_sufficient_reason="abort is optional rather than structural",
        )
        before = copy.deepcopy(request)
        result = resolver.resolve_distributed_refusal_abort_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_NOT_SUFFICIENT)
        self.assertEqual(result["refusal_abort_statement"]["not_sufficient_reason"], "abort is optional rather than structural")
        self.assertIs(result["refusal_abort_statement"]["selected_sync_non_sync_result_preserved"], True)
        self.assert_no_refusal_abort_or_operation_flags(result["refusal_abort_statement"])
        self.assertEqual(request, before)

    def test_refusal_abort_non_meaning_and_open_work_are_preserved(self) -> None:
        result = self.valid_result()
        non_meaning = result["refusal_abort_non_meaning"]
        for suffix in (
            "live_operation_refused",
            "live_operation_aborted",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "synchronization_authorized",
            "non_synchronized_operation_authorized",
            "repository_synchronization_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "carrier_role_activated",
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
            self.assertIs(non_meaning[f"does_not_mean_{suffix}"], True, suffix)

        open_work = result["what_remains_open"]
        for key in (
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
            self.assertEqual(open_work[key], "open_not_scheduled_not_authorized_not_executed")
        self.assertIs(open_work["open_means_not_scheduled"], True)
        self.assertIs(open_work["open_means_not_authorized"], True)
        self.assertIs(open_work["open_means_not_executed"], True)

    def test_result_level_non_claims_remain_false_for_all_outcome_families(self) -> None:
        results = [
            self.valid_result(),
            resolve_request(requested_refusal_abort_outcome=OUTCOME_NOT_SUFFICIENT, not_sufficient_reason="late cleanup"),
            resolve_request(
                requested_refusal_abort_outcome=OUTCOME_REQUIRES_ADDITIONAL,
                additional_basis_context={"additional_basis_reason": "abort trigger basis too generic"},
            ),
            resolve_request(refusal_abort_postures=["UNSUPPORTED"]),
        ]
        self.assertEqual({result["outcome"] for result in results}, {
            OUTCOME_RECORDED,
            OUTCOME_NOT_SUFFICIENT,
            OUTCOME_REQUIRES_ADDITIONAL,
            OUTCOME_BLOCKED,
        })
        for result in results:
            self.assert_false_non_claims(result)

    def test_summary_helper_preserves_key_posture(self) -> None:
        result = self.valid_result()
        summary = resolver.build_distributed_refusal_abort_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["refusal_abort_request_id"], "refusal-abort-request-001")
        self.assertEqual(summary["refusal_abort_intent"], "RECORD_DISTRIBUTED_REFUSAL_ABORT_BOUNDARY")
        self.assertEqual(summary["selected_sync_non_sync_result_id"], "sync-non-sync-result-001")
        self.assertEqual(summary["selected_sync_non_sync_result_outcome"], SYNC_OUTCOME_RECORDED)
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["passed_check_count"], len(result["refusal_abort_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "distributed_refusal_abort_boundary_recorded",
            "selected_sync_non_sync_result_preserved",
            "selected_sync_non_sync_result_recorded",
            "selected_sync_non_sync_result_failed_check_count_zero",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "refusal_abort_postures_preserved",
            "refusal_abort_postures_supported",
            "non_admission_conditions_named",
            "abort_conditions_named",
            "carrier_b_success_does_not_force_continuation",
            "carrier_c_block_remains_visible",
            "carrier_c_block_does_not_invalidate_carrier_c",
            "no_live_operation_refused_or_aborted",
            "no_operation_admitted_authorized_executed",
            "no_sync_full_body_transfer_second_body_non_sync_operation",
            "no_consequence_public_readiness_final_completion_follow_on_work",
            "future_admission_transition_must_preserve_refusal_abort",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["refusal_abort_basis_not_sufficient"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["key_non_claims"]["operation_admitted"], False)

    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        sync_result = selected_sync_non_sync_result()
        basis = refusal_abort_basis()
        request = resolver.build_declared_distributed_refusal_abort_request(
            "builder-request-001",
            "What refusal / abort postures must be preserved?",
            sync_result,
            basis,
            SUPPORTED_REFUSAL_ABORT_POSTURES,
            selected_sync_non_sync_result_id="sync-non-sync-result-001",
            selected_sync_non_sync_result_outcome=SYNC_OUTCOME_RECORDED,
            selected_carrier_context=selected_carrier_context(),
        )
        self.assertEqual(request["refusal_abort_request_id"], "builder-request-001")
        self.assertEqual(request["refusal_abort_question"], "What refusal / abort postures must be preserved?")
        self.assertEqual(request["selected_sync_non_sync_result"], sync_result)
        self.assertEqual(request["refusal_abort_basis"]["sync_non_sync_posture_basis"], basis["sync_non_sync_posture_basis"])
        self.assertEqual(tuple(request["refusal_abort_postures"]), SUPPORTED_REFUSAL_ABORT_POSTURES)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        result = resolver.resolve_distributed_refusal_abort_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)

        additional_request = resolver.build_declared_distributed_refusal_abort_request(
            "builder-request-002",
            "What refusal / abort postures need more basis?",
            sync_result,
            basis,
            SUPPORTED_REFUSAL_ABORT_POSTURES,
            requested_refusal_abort_outcome=OUTCOME_REQUIRES_ADDITIONAL,
            additional_basis_context={"additional_basis_reason": "non-admission conditions incomplete"},
            not_sufficient_reason="not used for additional basis",
        )
        self.assertEqual(additional_request["requested_refusal_abort_outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertEqual(additional_request["additional_basis_context"]["additional_basis_reason"], "non-admission conditions incomplete")
        self.assertEqual(additional_request["not_sufficient_reason"], "not used for additional basis")

    def test_path_based_selected_sync_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            sync_path = tmp_path / "selected_sync_result.json"
            sync_path.write_text(json.dumps(selected_sync_non_sync_result()), encoding="utf-8")
            request = declared_refusal_abort_request(
                selected_sync_non_sync_result_path=str(sync_path),
                selected_sync_non_sync_result=None,
            )
            result = resolver.resolve_distributed_refusal_abort_boundary(request)
            self.assertEqual(result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(result["selected_sync_non_sync_result"]["selected_sync_non_sync_result_path"], str(sync_path))
            self.assertEqual(result["selected_sync_non_sync_result"]["selected_sync_non_sync_result_id"], "sync-non-sync-result-001")

            request_path = tmp_path / "declared_refusal_abort_request.json"
            request_path.write_text(json.dumps(declared_refusal_abort_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_refusal_abort_boundary_from_path(request_path)
            mapping_result = self.valid_result()
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(path_result["declared_refusal_abort_question"]["refusal_abort_request_path"], str(request_path))

    def test_write_behavior_and_default_output_path_are_additive(self) -> None:
        result = self.valid_result()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            explicit = tmp_path / "nested" / "result.json"
            written = resolver.write_distributed_refusal_abort_result(result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(resolver, "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_ROOT", tmp_path / "default_root"):
                first = resolver.write_distributed_refusal_abort_result(result)
                second = resolver.write_distributed_refusal_abort_result(result)
                self.assertTrue(str(first).startswith(str(tmp_path / "default_root")))
                self.assertNotEqual(first, second)
                self.assertTrue(first.name.endswith("__distributed_refusal_abort_result.json"))
                self.assertIn("_001", second.stem)
                self.assertNotIn("distributed_synchronization_non_synchronization_boundary", str(first))

    def test_non_mutation_posture_for_inputs_and_artifacts(self) -> None:
        request = declared_refusal_abort_request()
        selected_sync = request["selected_sync_non_sync_result"]
        basis = request["refusal_abort_basis"]
        postures = request["refusal_abort_postures"]
        carrier_context = request["selected_carrier_context"]
        request_before = copy.deepcopy(request)
        sync_before = copy.deepcopy(selected_sync)
        basis_before = copy.deepcopy(basis)
        postures_before = copy.deepcopy(postures)
        carrier_context_before = copy.deepcopy(carrier_context)

        first = resolver.resolve_distributed_refusal_abort_boundary(request)
        second = resolver.resolve_distributed_refusal_abort_boundary(request)
        self.assertEqual(first["outcome"], OUTCOME_RECORDED)
        self.assertEqual(second["outcome"], OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(selected_sync, sync_before)
        self.assertEqual(basis, basis_before)
        self.assertEqual(postures, postures_before)
        self.assertEqual(carrier_context, carrier_context_before)

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            sync_artifact = tmp_path / "sync.json"
            carrier_artifact = tmp_path / "carrier.json"
            authority_artifact = tmp_path / "authority.json"
            eligibility_artifact = tmp_path / "eligibility.json"
            matter_artifact = tmp_path / "matter.json"
            for path in (sync_artifact, carrier_artifact, authority_artifact, eligibility_artifact, matter_artifact):
                path.write_text(path.name, encoding="utf-8")
            original_contents = {path: path.read_text(encoding="utf-8") for path in (
                sync_artifact,
                carrier_artifact,
                authority_artifact,
                eligibility_artifact,
                matter_artifact,
            )}
            request_with_path = declared_refusal_abort_request(
                selected_sync_non_sync_result_path=str(sync_artifact),
                selected_sync_non_sync_result=None,
            )
            sync_artifact.write_text(json.dumps(selected_sync_non_sync_result()), encoding="utf-8")
            result = resolver.resolve_distributed_refusal_abort_boundary(request_with_path)
            resolver.write_distributed_refusal_abort_result(result, tmp_path / "output" / "refusal_abort.json")
            self.assertEqual(json.loads(sync_artifact.read_text(encoding="utf-8"))["outcome"], SYNC_OUTCOME_RECORDED)
            for path in (carrier_artifact, authority_artifact, eligibility_artifact, matter_artifact):
                self.assertEqual(path.read_text(encoding="utf-8"), original_contents[path])

    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        explicit = resolve_request(refusal_abort_intent="BLOCK_DISTRIBUTED_REFUSAL_ABORT_REVIEW")
        self.assertEqual(explicit["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(explicit["block"]["block_code"], "REFUSAL_ABORT_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        self.assertIs(explicit["refusal_abort_statement"]["distributed_refusal_abort_boundary_recorded"], False)

        missing = resolver.resolve_distributed_refusal_abort_boundary()
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(missing["block"]["block_code"], "REFUSAL_ABORT_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_refusal_abort_boundary("not a request")
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(malformed["block"]["block_code"], "DECLARED_REFUSAL_ABORT_REQUEST_MALFORMED")

    def test_refusal_abort_request_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_distributed_refusal_abort_boundary_from_path(tmp_path / "missing.json")
            self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(missing["block"]["block_code"], "DECLARED_REFUSAL_ABORT_REQUEST_UNREADABLE")

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_distributed_refusal_abort_boundary_from_path(malformed_path)
            self.assertEqual(malformed["block"]["block_code"], "DECLARED_REFUSAL_ABORT_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_refusal_abort_boundary_from_path(array_path)
            self.assertEqual(array_result["block"]["block_code"], "DECLARED_REFUSAL_ABORT_REQUEST_MALFORMED")

    def test_selected_sync_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_result = resolve_request(
                selected_sync_non_sync_result_path=str(tmp_path / "missing.json"),
                selected_sync_non_sync_result=None,
            )
            self.assertEqual(missing_result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(missing_result["block"]["block_code"], "SYNC_NON_SYNC_RESULT_UNREADABLE")

            malformed_path = tmp_path / "bad.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolve_request(
                selected_sync_non_sync_result_path=str(malformed_path),
                selected_sync_non_sync_result=None,
            )
            self.assertEqual(malformed_result["block"]["block_code"], "SYNC_NON_SYNC_RESULT_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_request(
                selected_sync_non_sync_result_path=str(array_path),
                selected_sync_non_sync_result=None,
            )
            self.assertEqual(array_result["block"]["block_code"], "SYNC_NON_SYNC_RESULT_MALFORMED")

    def test_selected_sync_result_identity_blocks(self) -> None:
        cases = (
            ("outcome missing", {"outcome": None}, "SYNC_NON_SYNC_RESULT_OUTCOME_MISSING"),
            ("outcome not recorded", {"outcome": "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_NOT_SUFFICIENT"}, "SYNC_NON_SYNC_RESULT_NOT_RECORDED"),
            (
                "failed checks",
                {"distributed_sync_non_sync_summary": {"failed_check_count": 1}},
                "SYNC_NON_SYNC_RESULT_HAS_FAILED_CHECKS",
            ),
        )
        for _, mutation, expected_code in cases:
            with self.subTest(expected_code=expected_code):
                sync_result = selected_sync_non_sync_result()
                if "outcome" in mutation and mutation["outcome"] is None:
                    sync_result.pop("outcome", None)
                    sync_result["distributed_sync_non_sync_summary"].pop("outcome", None)
                else:
                    sync_result.update(mutation)
                result = resolve_request(
                    selected_sync_non_sync_result=sync_result,
                    selected_sync_non_sync_result_outcome=None,
                )
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_missing_required_selected_basis_blocks(self) -> None:
        missing_cases = (
            ("selected carrier role", ("selected_operation_matter", "selected_carrier_role_result"), "CARRIER_ROLE_RESULT_MISSING"),
            ("source authority", ("selected_operation_matter", "selected_source_body_authority_result"), "SOURCE_BODY_AUTHORITY_RESULT_MISSING"),
            ("eligibility", ("selected_operation_matter", "selected_eligibility_result"), "SELECTED_ELIGIBILITY_RESULT_MISSING"),
            ("matter declaration", ("selected_operation_matter", "selected_matter_declaration"), "SELECTED_MATTER_DECLARATION_MISSING"),
            ("operation candidate", ("selected_operation_matter", "selected_operation_candidate"), "SELECTED_OPERATION_CANDIDATE_MISSING"),
            ("operation matter", ("selected_operation_matter", "selected_operation_matter"), "SELECTED_OPERATION_MATTER_MISSING"),
        )
        for _, path, expected_code in missing_cases:
            with self.subTest(expected_code=expected_code):
                sync_result = selected_sync_non_sync_result()
                target = sync_result
                for key in path[:-1]:
                    target = target[key]
                target.pop(path[-1])
                result = resolve_request(selected_sync_non_sync_result=sync_result)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

        no_basis = selected_sync_non_sync_result()
        no_basis.pop("sync_non_sync_basis")
        no_basis.pop("sync_non_sync_postures")
        basis = refusal_abort_basis()
        basis.pop("sync_non_sync_posture_basis")
        result = resolve_request(
            selected_sync_non_sync_result=no_basis,
            sync_non_sync_posture_basis=None,
            refusal_abort_basis=basis,
        )
        self.assertEqual(result["block"]["block_code"], "SYNC_NON_SYNC_POSTURE_BASIS_MISSING")

        no_postures = resolve_request(refusal_abort_postures=[])
        self.assertEqual(no_postures["block"]["block_code"], "REFUSAL_ABORT_POSTURES_MISSING")

    def test_collapse_flags_block_with_representative_codes(self) -> None:
        cases = (
            ("live_operation_refused", "REFUSAL_ABORT_REVIEW_REFUSES_LIVE_OPERATION"),
            ("live_operation_aborted", "REFUSAL_ABORT_REVIEW_ABORTS_LIVE_OPERATION"),
            ("operation_admitted", "REFUSAL_ABORT_REVIEW_ADMITS_OPERATION"),
            ("operation_authorized", "REFUSAL_ABORT_REVIEW_AUTHORIZES_OPERATION"),
            ("operation_executed", "REFUSAL_ABORT_REVIEW_EXECUTES_OPERATION"),
            ("repository_synchronization_authorized", "REFUSAL_ABORT_REVIEW_AUTHORIZES_SYNCHRONIZATION"),
            ("non_synchronized_operation_authorized", "REFUSAL_ABORT_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION"),
            ("full_body_transfer_authorized", "REFUSAL_ABORT_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "REFUSAL_ABORT_REVIEW_CREATES_SECOND_BODY"),
            ("carrier_role_activated", "REFUSAL_ABORT_REVIEW_ACTIVATES_CARRIER_ROLES"),
            ("carrier_authority_created", "REFUSAL_ABORT_REVIEW_CREATES_CARRIER_AUTHORITY"),
            ("carrier_currentness_created", "REFUSAL_ABORT_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "REFUSAL_ABORT_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "REFUSAL_ABORT_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "REFUSAL_ABORT_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "REFUSAL_ABORT_REVIEW_REPLACES_SOURCE"),
            ("truth_created", "REFUSAL_ABORT_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "REFUSAL_ABORT_REVIEW_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "REFUSAL_ABORT_REVIEW_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "REFUSAL_ABORT_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "REFUSAL_ABORT_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "REFUSAL_ABORT_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "REFUSAL_ABORT_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for field, expected_code in cases:
            with self.subTest(field=field):
                request = declared_refusal_abort_request()
                request["refusal_abort_basis"][field] = True
                result = resolver.resolve_distributed_refusal_abort_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_non_sync_autonomy_stale_and_mutation_replay_merge_blocks(self) -> None:
        for field in ("carrier_autonomy_authorized", "stale_carrier_operation_authorized"):
            with self.subTest(field=field):
                request = declared_refusal_abort_request()
                request["refusal_abort_basis"][field] = True
                result = resolver.resolve_distributed_refusal_abort_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], "REFUSAL_ABORT_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION")

        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = declared_refusal_abort_request()
                request["refusal_abort_basis"][field] = True
                result = resolver.resolve_distributed_refusal_abort_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        request = declared_refusal_abort_request()
        request["declared_non_claims"].pop("live_operation_refused")
        result = resolver.resolve_distributed_refusal_abort_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["block_code"], "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = declared_refusal_abort_request()
        flipped["declared_non_claims"]["operation_admitted"] = True
        flipped_result = resolver.resolve_distributed_refusal_abort_boundary(flipped)
        self.assertEqual(flipped_result["outcome"], OUTCOME_BLOCKED)
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "REFUSAL_ABORT_REVIEW_ADMITS_OPERATION"},
        )


if __name__ == "__main__":
    unittest.main()
