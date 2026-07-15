"""Bounded tests for distributed operation admission / transition authority.

These tests prove that the resolver may admit one bounded operation context for
later execution / emission review only. They do not execute operation, emit
output, authorize action, create consequence, authorize synchronization or
non-synchronized operation, transfer the body, create a second body, erase
refusal / abort, create reusable permission, authorize autonomous continuation,
or schedule follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_distributed_operation_admission_transition_authority_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED"
OUTCOME_NOT_ADMITTED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REVIEW_BLOCKED"
REFUSAL_ABORT_OUTCOME_RECORDED = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED"
SYNC_OUTCOME_RECORDED = "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED"

SUPPORTED_ADMISSION_SCOPE = tuple(resolver.SUPPORTED_ADMISSION_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_operation_admission_transition_metadata",
    "declared_admission_transition_question",
    "selected_refusal_abort_result",
    "selected_operation_matter",
    "admission_transition_basis",
    "admission_scope",
    "admission_transition_checks",
    "admission_transition_statement",
    "admission_transition_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_operation_admission_transition_summary",
)


def false_claims(*, operation_admitted: bool = False) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["operation_admitted"] = operation_admitted
    return claims


def refusal_abort_false_claims() -> dict[str, bool]:
    return {
        "live_operation_refused": False,
        "live_operation_aborted": False,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
        "carrier_autonomy_authorized": False,
        "stale_carrier_operation_authorized": False,
        "carrier_role_activated": False,
        "carrier_role_assigned_for_operation": False,
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "source_replaced": False,
        "authority_created": False,
        "permission_created": False,
        "truth_created": False,
        "action_authorized": False,
        "consequence_created": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "refusal_erased": False,
        "blocked_attempt_erased": False,
        "projection_mismatch_hidden": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "self_orientation_successor_scheduled": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }


def selected_operation_candidate() -> dict[str, object]:
    return {
        "operation_candidate_id": "operation-candidate-001",
        "operation_question": "May this bounded matter be admitted for later execution review?",
        "operation_purpose": "Preserve one bounded distributed operation context for later review.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": "May this bounded matter be admitted for later execution review?",
        "operation_purpose": "Preserve one bounded distributed operation context for later review.",
        "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        "matter_remains_declaration_only": True,
    }


def selected_matter_declaration() -> dict[str, object]:
    return {
        "distributed_operation_matter_declaration_result_id": "matter-declaration-001",
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
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


def source_body_authority_basis() -> dict[str, object]:
    return {
        "source_body_authority_basis_id": "source-authority-basis-001",
        "source_body_lineage_basis": {"lineage_basis_id": "source-lineage-001"},
        "authority_basis_is_basis_only": True,
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
        "source_body_authority_basis": source_body_authority_basis(),
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


def carrier_role_basis() -> dict[str, object]:
    return {
        "selected_carrier_context": selected_carrier_context(),
        "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
        "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {"refusal_visible": True, "blocked_attempt_visible": True},
        "projection_mismatch_context": {"projection_mismatch_visible": True},
    }


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
            "selected_operation_question": "May this bounded matter be admitted for later execution review?",
            "selected_operation_purpose": "Preserve one bounded distributed operation context.",
            "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        },
        "carrier_role_basis": carrier_role_basis(),
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
            "selected_carrier_role_result": selected_carrier_role_result(),
            "selected_source_body_authority_result": selected_source_body_authority_result(),
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_matter_declaration": selected_matter_declaration(),
            "selected_operation_candidate": selected_operation_candidate(),
            "selected_operation_matter": selected_operation_matter(),
            "selected_operation_question": "May this bounded matter be admitted for later execution review?",
            "selected_operation_purpose": "Preserve one bounded distributed operation context.",
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
            "sync_non_sync_postures_preserved": True,
            "carrier_evidence_remains_unmerged": True,
            "carrier_context_remains_context_only": True,
            "divergence_remains_visible": True,
            "refusal_remains_visible": True,
            "blocked_attempts_remain_visible": True,
            "projection_mismatch_remains_visible": True,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "failed_check_count": 0,
        },
    }


def refusal_abort_posture_basis() -> dict[str, object]:
    return {
        "selected_refusal_abort_postures": [
            "NO_OPERATION_ADMISSION_WITHOUT_REFUSAL_ABORT_BOUNDARY",
            "NO_OPERATION_ADMISSION_WHEN_REQUIRED_BASIS_MISSING",
            "NO_OPERATION_ADMISSION_WHEN_CARRIER_REFUSAL_HIDDEN",
            "NO_OPERATION_ADMISSION_WHEN_BLOCKED_ATTEMPT_HIDDEN",
            "NO_OPERATION_ADMISSION_WHEN_DIVERGENCE_HIDDEN",
            "NO_OPERATION_ADMISSION_WHEN_PROJECTION_MISMATCH_HIDDEN",
            "NO_OPERATION_ADMISSION_WHEN_SYNC_STATUS_OVERREAD",
            "NO_OPERATION_ADMISSION_WHEN_NO_SYNC_OVERREAD",
            "NO_OPERATION_ADMISSION_WHEN_CARRIER_ROLE_ACTIVATED_PREMATURELY",
            "NO_OPERATION_ADMISSION_WHEN_AUTHORITY_GRANTED_BY_IMPLICATION",
            "NO_OPERATION_ADMISSION_WHEN_CONSEQUENCE_IMPLIED",
            "ABORT_IF_OPERATION_SCOPE_EXPANDS",
            "ABORT_IF_SYNC_OR_MERGE_ATTEMPTED_WITHOUT_AUTHORITY",
            "ABORT_IF_NON_SYNC_OPERATION_ATTEMPTED_WITHOUT_ADMISSION",
            "ABORT_IF_CARRIER_AUTHORITY_OR_CURRENTNESS_CREATED",
            "ABORT_IF_WINNER_LOSER_CARRIER_SELECTION_OCCURS",
            "ABORT_IF_SOURCE_REPLACEMENT_ATTEMPTED",
            "ABORT_IF_EVIDENCE_OR_REFUSAL_ERASURE_ATTEMPTED",
            "ABORT_IF_CONSEQUENCE_CREATED_WITHOUT_ACTION_BOUNDARY",
            "FUTURE_ABORT_EXECUTION_REQUIRES_ADMITTED_OPERATION_CONTEXT",
        ],
        "all_selected_postures_supported": True,
        "postures_are_boundary_postures_only": True,
        "postures_are_pre_admission_safety_conditions": True,
        "non_admission_conditions_named": True,
        "abort_conditions_named": True,
    }


def selected_refusal_abort_result() -> dict[str, object]:
    sync_result = selected_sync_non_sync_result()
    carrier_role = selected_carrier_role_result()
    source_authority = selected_source_body_authority_result()
    eligibility = selected_eligibility_result()
    matter_declaration = selected_matter_declaration()
    operation_candidate = selected_operation_candidate()
    operation_matter = selected_operation_matter()
    return {
        "distributed_refusal_abort_metadata": {
            "distributed_refusal_abort_result_id": "refusal-abort-result-001",
            "distributed_refusal_abort_result_type": "distributed_refusal_abort_boundary_result",
            "distributed_refusal_abort_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_refusal_abort_boundary",
        },
        "outcome": REFUSAL_ABORT_OUTCOME_RECORDED,
        "distributed_refusal_abort_summary": {
            "outcome": REFUSAL_ABORT_OUTCOME_RECORDED,
            "failed_check_count": 0,
            "selected_operation_candidate_id": "operation-candidate-001",
            "selected_operation_matter_id": "operation-matter-001",
        },
        "selected_operation_matter": {
            "selected_sync_non_sync_result": sync_result,
            "selected_carrier_role_result": carrier_role,
            "selected_source_body_authority_result": source_authority,
            "selected_eligibility_result": eligibility,
            "selected_matter_declaration": matter_declaration,
            "selected_operation_candidate": operation_candidate,
            "selected_operation_matter": operation_matter,
            "selected_operation_question": "May this bounded matter be admitted for later execution review?",
            "selected_operation_purpose": "Preserve one bounded distributed operation context.",
            "proposed_operation_kind": "FUTURE_DISTRIBUTED_OPERATION_REVIEW",
        },
        "refusal_abort_basis": {
            "selected_sync_non_sync_result": sync_result,
            "selected_carrier_role_result": carrier_role,
            "selected_source_body_authority_result": source_authority,
            "selected_eligibility_result": eligibility,
            "selected_matter_declaration": matter_declaration,
            "selected_operation_candidate": operation_candidate,
            "selected_operation_matter": operation_matter,
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
        },
        "refusal_abort_postures": refusal_abort_posture_basis(),
        "refusal_abort_statement": {
            "distributed_refusal_abort_boundary_recorded": True,
            "selected_sync_non_sync_result_preserved": True,
            "selected_sync_non_sync_result_recorded": True,
            "selected_sync_non_sync_result_failed_check_count_zero": True,
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
            "refusal_abort_postures_preserved": True,
            "non_admission_conditions_named": True,
            "abort_conditions_named": True,
            "carrier_b_success_does_not_force_continuation": True,
            "carrier_c_block_remains_visible": True,
            "carrier_c_block_does_not_invalidate_carrier_c": True,
            "live_operation_refused": False,
            "live_operation_aborted": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "consequence_created": False,
            "follow_on_work_authorized": False,
            "failed_check_count": 0,
        },
        "non_claims": refusal_abort_false_claims(),
    }


def admission_transition_basis() -> dict[str, object]:
    refusal_result = selected_refusal_abort_result()
    return {
        "selected_refusal_abort_result": refusal_result,
        "selected_sync_non_sync_result": refusal_result["selected_operation_matter"]["selected_sync_non_sync_result"],
        "selected_carrier_role_result": refusal_result["selected_operation_matter"]["selected_carrier_role_result"],
        "selected_source_body_authority_result": refusal_result["selected_operation_matter"][
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": refusal_result["selected_operation_matter"]["selected_eligibility_result"],
        "selected_matter_declaration": refusal_result["selected_operation_matter"]["selected_matter_declaration"],
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "source_body_authority_basis": source_body_authority_basis(),
        "carrier_role_basis": carrier_role_basis(),
        "sync_non_sync_posture_basis": sync_non_sync_posture_basis(),
        "refusal_abort_posture_basis": refusal_abort_posture_basis(),
        "carrier_b_success_context": {"carrier_id": "carrier-b", "success_visible": True},
        "carrier_c_block_context": {"carrier_id": "carrier-c", "block_visible": True},
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {"refusal_visible": True, "blocked_attempt_visible": True},
        "projection_mismatch_context": {"projection_mismatch_visible": True},
        "operation_context_scope": {"operation_context_scope": "ONE_OPERATION_CONTEXT_ONLY"},
        "execution_emission_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed execution / emission boundary",
        },
        "action_consequence_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed action / consequence boundary",
        },
        "receipt_exhaustion_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed operation receipt / exhaustion",
        },
    }


def declared_admission_transition_request(**overrides: object) -> dict[str, object]:
    requested = overrides.get("requested_admission_transition_outcome", OUTCOME_RECORDED)
    request = {
        "admission_transition_request_id": "admission-transition-request-001",
        "admission_transition_question": (
            "May this bounded matter be admitted as one distributed operation context "
            "for later execution / emission review?"
        ),
        "admission_transition_intent": "RECORD_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY",
        "selected_refusal_abort_result": selected_refusal_abort_result(),
        "selected_refusal_abort_result_id": "refusal-abort-result-001",
        "selected_refusal_abort_result_outcome": REFUSAL_ABORT_OUTCOME_RECORDED,
        "requested_admission_transition_outcome": requested,
        "admission_transition_basis": admission_transition_basis(),
        "admission_scope": list(SUPPORTED_ADMISSION_SCOPE),
        "operation_context_scope": {"operation_context_scope": "ONE_OPERATION_CONTEXT_ONLY"},
        "execution_emission_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed execution / emission boundary",
        },
        "action_consequence_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed action / consequence boundary",
        },
        "receipt_exhaustion_successor_boundary_requirement": {
            "required": True,
            "boundary": "distributed operation receipt / exhaustion",
        },
    }
    request.update(overrides)
    if "declared_non_claims" not in overrides:
        request["declared_non_claims"] = false_claims(
            operation_admitted=request.get("requested_admission_transition_outcome") == OUTCOME_RECORDED
        )
    return request


def resolve_request(**overrides: object) -> dict[str, object]:
    return resolver.resolve_distributed_operation_admission_transition_authority_boundary(
        declared_admission_transition_request=declared_admission_transition_request(**overrides)
    )


def remove_key_everywhere(value: object, key_to_remove: str) -> None:
    if isinstance(value, dict):
        value.pop(key_to_remove, None)
        for nested in value.values():
            remove_key_everywhere(nested, key_to_remove)
    elif isinstance(value, list):
        for item in value:
            remove_key_everywhere(item, key_to_remove)


class DistributedOperationAdmissionTransitionAuthorityBoundaryTests(unittest.TestCase):
    def assert_false_non_claims(self, result: dict[str, object], *, operation_admitted: bool = False) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        self.assertIs(non_claims["operation_admitted"], operation_admitted)

    def assert_no_execution_emission_action_consequence_flags(self, statement: dict[str, object]) -> None:
        for key in (
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
            "repository_synchronization_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "non_synchronized_operation_authorized",
            "carrier_autonomy_authorized",
            "stale_carrier_operation_authorized",
            "reusable_permission_created",
            "autonomous_continuation_authorized",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(statement[key], False, key)

    def valid_result(self) -> dict[str, object]:
        result = resolve_request()
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        return result

    def test_successful_admission_transition_authority_recorded_result(self) -> None:
        result = self.valid_result()
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["distributed_operation_admission_transition_summary"]["failed_check_count"], 0)

        statement = result["admission_transition_statement"]
        for key in (
            "distributed_operation_admission_transition_authority_recorded",
            "operation_admitted",
            "one_bounded_operation_context_admitted",
            "selected_refusal_abort_result_preserved",
            "selected_refusal_abort_result_recorded",
            "selected_refusal_abort_result_failed_check_count_zero",
            "selected_sync_non_sync_result_preserved",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "refusal_abort_postures_preserved",
            "non_admission_conditions_named",
            "abort_conditions_named",
            "refusal_abort_conditions_carry_forward",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "admission_scope_one_operation_context_only",
            "execution_emission_successor_boundary_required",
            "action_consequence_successor_boundary_required",
            "receipt_exhaustion_successor_boundary_required",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_no_execution_emission_action_consequence_flags(statement)
        self.assert_false_non_claims(result, operation_admitted=True)

    def test_metadata_and_declared_question_are_preserved(self) -> None:
        result = self.valid_result()
        metadata = result["distributed_operation_admission_transition_metadata"]
        for key in (
            "distributed_operation_admission_transition_result_id",
            "distributed_operation_admission_transition_result_type",
            "distributed_operation_admission_transition_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["distributed_operation_admission_transition_result_version"], "0.1.0")
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_operation_admission_transition_authority_boundary",
        )

        declared = result["declared_admission_transition_question"]
        self.assertEqual(declared["admission_transition_request_id"], "admission-transition-request-001")
        self.assertEqual(
            declared["admission_transition_intent"],
            "RECORD_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY",
        )
        self.assertEqual(declared["selected_refusal_abort_result_id"], "refusal-abort-result-001")
        self.assertEqual(declared["selected_refusal_abort_result_outcome"], REFUSAL_ABORT_OUTCOME_RECORDED)
        for key in (
            "admission_transition_boundary_is_not_execution",
            "admission_transition_boundary_is_not_emission",
            "admission_transition_boundary_is_not_action",
            "admission_transition_boundary_is_not_consequence",
            "admission_transition_boundary_is_not_synchronization",
            "admission_transition_boundary_is_not_full_body_transfer",
            "admission_transition_boundary_is_not_second_body_creation",
            "admission_transition_boundary_is_not_reusable_permission",
            "admission_transition_boundary_is_not_autonomous_continuation",
        ):
            self.assertIs(declared[key], True, key)

    def test_selected_refusal_result_and_operation_matter_are_preserved(self) -> None:
        request = declared_admission_transition_request()
        original_refusal = copy.deepcopy(request["selected_refusal_abort_result"])
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)

        selected = result["selected_refusal_abort_result"]
        self.assertEqual(selected["selected_refusal_abort_result_id"], "refusal-abort-result-001")
        self.assertEqual(selected["selected_refusal_abort_result_outcome"], REFUSAL_ABORT_OUTCOME_RECORDED)
        self.assertIs(selected["selected_refusal_abort_result_outcome_is_recorded"], True)
        self.assertIs(selected["selected_refusal_abort_result_failed_check_count_zero"], True)
        for key in (
            "selected_refusal_abort_result_remains_boundary_posture_only",
            "selected_refusal_abort_result_did_not_refuse_live_operation",
            "selected_refusal_abort_result_did_not_abort_live_operation",
            "selected_refusal_abort_result_did_not_admit_operation",
            "selected_refusal_abort_result_did_not_authorize_operation",
            "selected_refusal_abort_result_did_not_execute_operation",
            "selected_refusal_abort_result_preserved_refusal_abort_postures",
            "selected_refusal_abort_result_preserved_non_admission_conditions",
            "selected_refusal_abort_result_preserved_abort_conditions",
            "selected_refusal_abort_result_preserved_carrier_b_success_without_forced_continuation",
            "selected_refusal_abort_result_preserved_carrier_c_block_without_invalidation",
            "selected_refusal_abort_result_preserved_divergence",
            "selected_refusal_abort_result_preserved_refusal",
            "selected_refusal_abort_result_preserved_blocked_attempts",
            "selected_refusal_abort_result_preserved_projection_mismatch",
            "selected_refusal_abort_result_is_not_mutated",
        ):
            self.assertIs(selected[key], True, key)
        self.assertEqual(request["selected_refusal_abort_result"], original_refusal)

        matter = result["selected_operation_matter"]
        for key in (
            "selected_refusal_abort_result",
            "selected_sync_non_sync_result",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_operation_candidate",
            "selected_operation_matter",
            "selected_operation_question",
            "selected_operation_purpose",
            "selected_proposed_operation_kind",
        ):
            self.assertTrue(matter[key], key)
        for key in (
            "refusal_abort_remains_boundary_posture_only",
            "sync_non_sync_remains_boundary_posture_only",
            "carrier_role_basis_remains_role_basis_only",
            "authority_remains_basis_only",
            "eligibility_remains_eligibility_only",
            "matter_remains_declaration_only",
        ):
            self.assertIs(matter[key], True, key)
        self.assertIs(matter["operation_executed"], False)
        self.assertIs(matter["output_emitted"], False)
        self.assertIs(matter["action_authorized"], False)
        self.assertIs(matter["consequence_created"], False)

    def test_admission_transition_basis_preserves_context_without_overread(self) -> None:
        basis = self.valid_result()["admission_transition_basis"]
        for key in (
            "selected_refusal_abort_result",
            "selected_sync_non_sync_result",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_operation_candidate",
            "selected_operation_matter",
            "source_body_authority_basis",
            "carrier_role_basis",
            "sync_non_sync_posture_basis",
            "refusal_abort_posture_basis",
            "carrier_b_success_context",
            "carrier_c_block_context",
            "b_c_divergence_context",
            "refusal_blocked_attempt_context",
            "projection_mismatch_context",
            "declared_admission_scope",
            "declared_operation_context_scope",
            "execution_emission_successor_boundary_requirement",
            "action_consequence_successor_boundary_requirement",
            "receipt_exhaustion_successor_boundary_requirement",
        ):
            self.assertTrue(basis[key], key)
        for key in (
            "refusal_abort_conditions_carry_forward",
            "carrier_b_success_does_not_force_continuation",
            "carrier_c_block_remains_visible",
            "carrier_c_block_does_not_invalidate_carrier_c",
            "b_c_divergence_remains_visible",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "admission_basis_is_not_execution",
            "admission_basis_is_not_emission",
            "admission_basis_is_not_action",
            "admission_basis_is_not_consequence",
            "admission_basis_is_not_synchronization",
            "admission_basis_is_not_full_body_transfer",
            "admission_basis_is_not_second_body",
            "admission_basis_is_not_reusable_permission",
            "admission_basis_is_not_autonomous_continuation",
        ):
            self.assertIs(basis[key], True, key)

    def test_supported_admission_scope_values_are_recordable(self) -> None:
        for scope in SUPPORTED_ADMISSION_SCOPE:
            with self.subTest(scope=scope):
                selected_scope = set(SUPPORTED_ADMISSION_SCOPE)
                selected_scope.add(scope)
                result = resolve_request(admission_scope=list(selected_scope))
                self.assertEqual(result["outcome"], OUTCOME_RECORDED)
                scope_section = result["admission_scope"]
                self.assertIn(scope, scope_section["selected_admission_scope"])
                self.assertIs(scope_section["all_selected_admission_scope_supported"], True)
                for key in (
                    "one_operation_context_only",
                    "no_execution_in_admission",
                    "no_emission_in_admission",
                    "no_action_in_admission",
                    "no_consequence_in_admission",
                    "no_repository_sync_in_admission",
                    "no_non_synchronized_operation_in_admission",
                    "no_full_body_transfer_in_admission",
                    "no_second_body_in_admission",
                    "refusal_abort_conditions_carry_forward",
                    "execution_emission_requires_separate_boundary",
                    "action_consequence_requires_separate_boundary",
                    "receipt_exhaustion_required_after_any_future_execution",
                    "no_reusable_permission",
                    "no_autonomous_continuation",
                ):
                    self.assertIs(scope_section[key], True, key)

    def test_unsupported_admission_scope_blocks(self) -> None:
        result = resolve_request(admission_scope=list(SUPPORTED_ADMISSION_SCOPE) + ["AUTHORIZE_EXECUTION_NOW"])
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["block_code"], "UNSUPPORTED_ADMISSION_SCOPE")

    def test_admission_transition_checks_are_explicit_and_pass_for_recorded(self) -> None:
        result = self.valid_result()
        checks = result["admission_transition_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertIs(check["passed"], True, check["check_name"])
        self.assertEqual(result["distributed_operation_admission_transition_summary"]["failed_check_count"], 0)
        names = {check["check_name"] for check in checks}
        expected_names = {
            "admission / transition question declared",
            "admission / transition intent supported",
            "selected refusal / abort result present",
            "selected refusal / abort result outcome declared",
            "selected refusal / abort result outcome recorded",
            "selected refusal / abort result failed check count zero",
            "selected sync/non-sync result preserved",
            "selected carrier role result preserved",
            "selected source-body authority result preserved",
            "selected eligibility result preserved",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "source-body authority basis preserved",
            "carrier role basis preserved",
            "sync/non-sync posture basis preserved",
            "refusal / abort posture basis preserved",
            "refusal / abort postures preserved",
            "non-admission conditions named",
            "abort conditions named",
            "refusal / abort conditions carry forward",
            "sync/non-sync postures preserved",
            "carrier evidence remains unmerged",
            "carrier context remains context only",
            "divergence remains visible",
            "refusal remains visible",
            "blocked attempts remain visible",
            "projection mismatch remains visible",
            "admission scope one operation context only",
            "selected admission scope supported",
            "operation context scope declared",
            "execution / emission successor boundary required",
            "action / consequence successor boundary required",
            "receipt / exhaustion successor boundary required",
            "no operation executed",
            "no output emitted",
            "no action authorized",
            "no consequence created",
            "no sync/shared live state/merge/replay/full body transfer/second body/non-sync operation/carrier autonomy/stale carrier operation",
            "no reusable permission created",
            "no autonomous continuation authorized",
            "no carrier role activated beyond admission scope",
            "no carrier authority/currentness/hierarchy created",
            "no current/winning/losing carrier selected",
            "no source replacement",
            "no refusal / abort erased",
            "no evidence/refusal/block/projection mismatch erased",
            "no divergence resolved",
            "no public readiness/final completion/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false except bounded operation_admitted",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_additional_basis_required_result_preserves_no_execution(self) -> None:
        context = {
            "additional_basis_reason": "admission scope too generic",
            "missing_basis": [
                "operation context scope too broad",
                "execution / emission successor boundary requirement not explicit enough",
                "admission cannot yet be bounded without reusable permission risk",
            ],
        }
        result = resolve_request(
            requested_admission_transition_outcome=OUTCOME_REQUIRES_ADDITIONAL,
            additional_basis_context=context,
        )
        self.assertEqual(result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertIs(result["admission_transition_statement"]["selected_refusal_abort_result_preserved"], True)
        self.assertEqual(result["additional_basis_required"]["additional_basis_context"], context)
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(result["admission_transition_statement"]["operation_admitted"], False)
        for key in (
            "additional_basis_not_scheduled",
            "additional_basis_not_authorized",
            "additional_basis_not_executed",
            "missing_basis_not_scheduled",
            "missing_basis_not_authorized",
            "missing_basis_not_executed",
        ):
            self.assertIs(result["additional_basis_required"][key], True, key)
        self.assert_no_execution_emission_action_consequence_flags(result["admission_transition_statement"])
        self.assert_false_non_claims(result)

    def test_not_admitted_result_preserves_reason_and_no_mutation(self) -> None:
        request = declared_admission_transition_request(
            requested_admission_transition_outcome=OUTCOME_NOT_ADMITTED,
            not_admitted_reason="admission would overread eligibility as authorization",
        )
        before = copy.deepcopy(request)
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_NOT_ADMITTED)
        self.assertEqual(
            result["admission_transition_statement"]["not_admitted_reason"],
            "admission would overread eligibility as authorization",
        )
        self.assertIs(result["admission_transition_statement"]["operation_admitted"], False)
        self.assertIs(result["admission_transition_statement"]["selected_refusal_abort_result_preserved"], True)
        self.assert_no_execution_emission_action_consequence_flags(result["admission_transition_statement"])
        self.assert_false_non_claims(result)
        self.assertEqual(request, before)

    def test_admission_transition_non_meaning_and_open_work_are_preserved(self) -> None:
        result = self.valid_result()
        non_meaning = result["admission_transition_non_meaning"]
        for suffix in (
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
            "repository_synchronization_authorized",
            "non_synchronized_operation_authorized",
            "shared_live_state_created",
            "state_merge_authorized",
            "replay_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "live_refusal_executed",
            "live_abort_executed",
            "carrier_roles_activated_beyond_admission_scope",
            "carrier_authority_created",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "source_replaced",
            "authority_newly_created",
            "reusable_permission_created",
            "autonomous_continuation_authorized",
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
            "carrier_role_activation_beyond_admission_scope",
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

    def test_result_level_non_claims_preserve_outcome_specific_admission(self) -> None:
        results = [
            self.valid_result(),
            resolve_request(
                requested_admission_transition_outcome=OUTCOME_NOT_ADMITTED,
                not_admitted_reason="admission would create reusable permission",
            ),
            resolve_request(
                requested_admission_transition_outcome=OUTCOME_REQUIRES_ADDITIONAL,
                additional_basis_context={"additional_basis_reason": "refusal / abort carry-forward basis unclear"},
            ),
            resolve_request(admission_scope=list(SUPPORTED_ADMISSION_SCOPE) + ["UNSUPPORTED"]),
        ]
        self.assertEqual(
            {result["outcome"] for result in results},
            {OUTCOME_RECORDED, OUTCOME_NOT_ADMITTED, OUTCOME_REQUIRES_ADDITIONAL, OUTCOME_BLOCKED},
        )
        for result in results:
            self.assert_false_non_claims(result, operation_admitted=result["outcome"] == OUTCOME_RECORDED)

    def test_summary_helper_preserves_key_posture(self) -> None:
        result = self.valid_result()
        summary = resolver.build_distributed_operation_admission_transition_authority_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["admission_transition_request_id"], "admission-transition-request-001")
        self.assertEqual(
            summary["admission_transition_intent"],
            "RECORD_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY",
        )
        self.assertEqual(summary["selected_refusal_abort_result_id"], "refusal-abort-result-001")
        self.assertEqual(summary["selected_refusal_abort_result_outcome"], REFUSAL_ABORT_OUTCOME_RECORDED)
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["passed_check_count"], len(result["admission_transition_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "admission_transition_authority_recorded",
            "distributed_operation_admission_transition_authority_recorded",
            "operation_admitted",
            "one_bounded_operation_context_admitted",
            "selected_refusal_abort_result_preserved",
            "selected_refusal_abort_result_recorded",
            "selected_refusal_abort_result_failed_check_count_zero",
            "selected_sync_non_sync_result_preserved",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "refusal_abort_postures_preserved",
            "non_admission_conditions_named",
            "abort_conditions_named",
            "refusal_abort_conditions_carry_forward",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "admission_scope_one_operation_context_only",
            "execution_emission_successor_boundary_required",
            "action_consequence_successor_boundary_required",
            "receipt_exhaustion_successor_boundary_required",
            "no_operation_executed_output_emitted_action_consequence",
            "no_sync_full_body_transfer_second_body_non_sync_operation",
            "no_reusable_permission_autonomous_continuation",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["not_admitted"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["key_non_claims"]["operation_admitted"], True)
        self.assertIs(summary["key_non_claims"]["operation_executed"], False)

    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        refusal_result = selected_refusal_abort_result()
        basis = admission_transition_basis()
        request = resolver.build_declared_distributed_operation_admission_transition_authority_request(
            "builder-request-001",
            "May this bounded matter be admitted?",
            refusal_result,
            basis,
            SUPPORTED_ADMISSION_SCOPE,
            selected_refusal_abort_result_id="refusal-abort-result-001",
            selected_refusal_abort_result_outcome=REFUSAL_ABORT_OUTCOME_RECORDED,
            operation_context_scope={"operation_context_scope": "ONE_OPERATION_CONTEXT_ONLY"},
        )
        self.assertEqual(request["admission_transition_request_id"], "builder-request-001")
        self.assertEqual(request["admission_transition_question"], "May this bounded matter be admitted?")
        self.assertEqual(request["selected_refusal_abort_result"], refusal_result)
        self.assertEqual(request["admission_transition_basis"]["carrier_role_basis"], basis["carrier_role_basis"])
        self.assertEqual(tuple(request["admission_scope"]), SUPPORTED_ADMISSION_SCOPE)
        self.assertEqual(request["selected_refusal_abort_result_id"], "refusal-abort-result-001")
        self.assertEqual(request["selected_refusal_abort_result_outcome"], REFUSAL_ABORT_OUTCOME_RECORDED)
        self.assertEqual(request["requested_admission_transition_outcome"], OUTCOME_RECORDED)
        self.assertIs(request["declared_non_claims"]["operation_admitted"], True)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)

        additional_request = resolver.build_declared_distributed_operation_admission_transition_authority_request(
            "builder-request-002",
            "What admission basis needs more support?",
            refusal_result,
            basis,
            SUPPORTED_ADMISSION_SCOPE,
            requested_admission_transition_outcome=OUTCOME_REQUIRES_ADDITIONAL,
            additional_basis_context={"additional_basis_reason": "operation context scope too broad"},
            not_admitted_reason="not used for additional basis",
        )
        self.assertEqual(additional_request["requested_admission_transition_outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertEqual(
            additional_request["additional_basis_context"]["additional_basis_reason"],
            "operation context scope too broad",
        )
        self.assertEqual(additional_request["not_admitted_reason"], "not used for additional basis")
        self.assertIs(additional_request["declared_non_claims"]["operation_admitted"], False)

    def test_path_based_selected_refusal_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            refusal_path = tmp_path / "selected_refusal_result.json"
            refusal_path.write_text(json.dumps(selected_refusal_abort_result()), encoding="utf-8")
            request = declared_admission_transition_request(
                selected_refusal_abort_result_path=str(refusal_path),
                selected_refusal_abort_result=None,
            )
            result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
            self.assertEqual(result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(result["selected_refusal_abort_result"]["selected_refusal_abort_result_path"], str(refusal_path))
            self.assertEqual(result["selected_refusal_abort_result"]["selected_refusal_abort_result_id"], "refusal-abort-result-001")
            self.assertEqual(
                result["selected_refusal_abort_result"]["selected_refusal_abort_result_outcome"],
                REFUSAL_ABORT_OUTCOME_RECORDED,
            )

            request_path = tmp_path / "declared_admission_transition_request.json"
            request_path.write_text(json.dumps(declared_admission_transition_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_operation_admission_transition_authority_boundary_from_path(
                request_path
            )
            mapping_result = self.valid_result()
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_admission_transition_question"]["admission_transition_request_path"],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_are_additive(self) -> None:
        result = self.valid_result()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            explicit = tmp_path / "nested" / "result.json"
            written = resolver.write_distributed_operation_admission_transition_authority_result(result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_BOUNDARY_ROOT",
                tmp_path / "default_root",
            ):
                first = resolver.write_distributed_operation_admission_transition_authority_result(result)
                second = resolver.write_distributed_operation_admission_transition_authority_result(result)
                self.assertTrue(str(first).startswith(str(tmp_path / "default_root")))
                self.assertNotEqual(first, second)
                self.assertTrue(first.name.endswith("__distributed_operation_admission_transition_result.json"))
                self.assertIn("_001", second.stem)
                self.assertNotIn("distributed_refusal_abort_boundary", str(first))

    def test_non_mutation_posture_for_inputs_and_artifacts(self) -> None:
        request = declared_admission_transition_request()
        selected_refusal = request["selected_refusal_abort_result"]
        basis = request["admission_transition_basis"]
        scope = request["admission_scope"]
        request_before = copy.deepcopy(request)
        refusal_before = copy.deepcopy(selected_refusal)
        basis_before = copy.deepcopy(basis)
        scope_before = copy.deepcopy(scope)

        first = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        second = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(first["outcome"], OUTCOME_RECORDED)
        self.assertEqual(second["outcome"], OUTCOME_RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(selected_refusal, refusal_before)
        self.assertEqual(basis, basis_before)
        self.assertEqual(scope, scope_before)

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            refusal_artifact = tmp_path / "refusal.json"
            sync_artifact = tmp_path / "sync.json"
            carrier_artifact = tmp_path / "carrier.json"
            authority_artifact = tmp_path / "authority.json"
            eligibility_artifact = tmp_path / "eligibility.json"
            matter_artifact = tmp_path / "matter.json"
            refusal_artifact.write_text(json.dumps(selected_refusal_abort_result()), encoding="utf-8")
            for path in (sync_artifact, carrier_artifact, authority_artifact, eligibility_artifact, matter_artifact):
                path.write_text(path.name, encoding="utf-8")
            original_contents = {
                path: path.read_text(encoding="utf-8")
                for path in (
                    refusal_artifact,
                    sync_artifact,
                    carrier_artifact,
                    authority_artifact,
                    eligibility_artifact,
                    matter_artifact,
                )
            }
            request_with_path = declared_admission_transition_request(
                selected_refusal_abort_result_path=str(refusal_artifact),
                selected_refusal_abort_result=None,
            )
            result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request_with_path)
            resolver.write_distributed_operation_admission_transition_authority_result(
                result,
                tmp_path / "output" / "admission.json",
            )
            for path, content in original_contents.items():
                self.assertEqual(path.read_text(encoding="utf-8"), content, path)

    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        explicit = resolve_request(
            admission_transition_intent="BLOCK_DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_REVIEW"
        )
        self.assertEqual(explicit["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(explicit["block"]["block_code"], "ADMISSION_TRANSITION_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        self.assertIs(
            explicit["admission_transition_statement"]["distributed_operation_admission_transition_authority_recorded"],
            False,
        )
        self.assertIs(explicit["admission_transition_statement"]["operation_admitted"], False)

        missing = resolver.resolve_distributed_operation_admission_transition_authority_boundary()
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(missing["block"]["block_code"], "ADMISSION_TRANSITION_QUESTION_UNDECLARED")
        self.assertIs(missing["non_claims"]["operation_admitted"], False)

        malformed = resolver.resolve_distributed_operation_admission_transition_authority_boundary("not a request")
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(malformed["block"]["block_code"], "DECLARED_ADMISSION_TRANSITION_REQUEST_MALFORMED")
        self.assertIs(malformed["non_claims"]["operation_admitted"], False)

    def test_admission_transition_request_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_distributed_operation_admission_transition_authority_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(missing["block"]["block_code"], "DECLARED_ADMISSION_TRANSITION_REQUEST_UNREADABLE")

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_distributed_operation_admission_transition_authority_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["block"]["block_code"], "DECLARED_ADMISSION_TRANSITION_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_operation_admission_transition_authority_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["block"]["block_code"], "DECLARED_ADMISSION_TRANSITION_REQUEST_MALFORMED")

    def test_selected_refusal_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_result = resolve_request(
                selected_refusal_abort_result_path=str(tmp_path / "missing.json"),
                selected_refusal_abort_result=None,
            )
            self.assertEqual(missing_result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(missing_result["block"]["block_code"], "REFUSAL_ABORT_RESULT_UNREADABLE")

            malformed_path = tmp_path / "bad.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolve_request(
                selected_refusal_abort_result_path=str(malformed_path),
                selected_refusal_abort_result=None,
            )
            self.assertEqual(malformed_result["block"]["block_code"], "REFUSAL_ABORT_RESULT_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_request(
                selected_refusal_abort_result_path=str(array_path),
                selected_refusal_abort_result=None,
            )
            self.assertEqual(array_result["block"]["block_code"], "REFUSAL_ABORT_RESULT_MALFORMED")

    def test_selected_refusal_result_identity_blocks(self) -> None:
        cases = (
            ("outcome missing", "REFUSAL_ABORT_RESULT_OUTCOME_MISSING"),
            ("outcome not recorded", "REFUSAL_ABORT_RESULT_NOT_RECORDED"),
            ("failed checks", "REFUSAL_ABORT_RESULT_HAS_FAILED_CHECKS"),
        )
        for case_name, expected_code in cases:
            with self.subTest(case_name=case_name):
                refusal_result = selected_refusal_abort_result()
                if case_name == "outcome missing":
                    refusal_result.pop("outcome", None)
                    refusal_result["distributed_refusal_abort_summary"].pop("outcome", None)
                elif case_name == "outcome not recorded":
                    refusal_result["outcome"] = "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_NOT_SUFFICIENT"
                    refusal_result["distributed_refusal_abort_summary"]["outcome"] = (
                        "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_NOT_SUFFICIENT"
                    )
                else:
                    refusal_result["distributed_refusal_abort_summary"]["failed_check_count"] = 1
                result = resolve_request(
                    selected_refusal_abort_result=refusal_result,
                    selected_refusal_abort_result_outcome=None,
                )
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)
                self.assertIs(result["non_claims"]["operation_admitted"], False)

    def test_missing_required_selected_basis_blocks(self) -> None:
        missing_cases = (
            ("selected_sync_non_sync_result", "SYNC_NON_SYNC_RESULT_MISSING"),
            ("selected_carrier_role_result", "CARRIER_ROLE_RESULT_MISSING"),
            ("selected_source_body_authority_result", "SOURCE_BODY_AUTHORITY_RESULT_MISSING"),
            ("selected_eligibility_result", "SELECTED_ELIGIBILITY_RESULT_MISSING"),
            ("selected_matter_declaration", "SELECTED_MATTER_DECLARATION_MISSING"),
            ("selected_operation_candidate", "SELECTED_OPERATION_CANDIDATE_MISSING"),
            ("selected_operation_matter", "SELECTED_OPERATION_MATTER_MISSING"),
        )
        for key_to_remove, expected_code in missing_cases:
            with self.subTest(expected_code=expected_code):
                request = declared_admission_transition_request()
                remove_key_everywhere(request["selected_refusal_abort_result"], key_to_remove)
                remove_key_everywhere(request["admission_transition_basis"], key_to_remove)
                result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

        request = declared_admission_transition_request(admission_scope=[])
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(result["block"]["block_code"], "ADMISSION_SCOPE_MISSING")

        request = declared_admission_transition_request()
        request["operation_context_scope"] = None
        request["admission_transition_basis"].pop("operation_context_scope", None)
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(result["block"]["block_code"], "OPERATION_CONTEXT_SCOPE_MISSING")

        requirement_cases = (
            (
                "execution_emission_successor_boundary_requirement",
                "EXECUTION_EMISSION_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
            ),
            (
                "action_consequence_successor_boundary_requirement",
                "ACTION_CONSEQUENCE_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
            ),
            (
                "receipt_exhaustion_successor_boundary_requirement",
                "RECEIPT_EXHAUSTION_SUCCESSOR_BOUNDARY_REQUIREMENT_MISSING",
            ),
        )
        for requirement_key, expected_code in requirement_cases:
            with self.subTest(expected_code=expected_code):
                request = declared_admission_transition_request()
                request[requirement_key] = None
                request["admission_transition_basis"].pop(requirement_key, None)
                result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_admission_collapse_flags_block_with_representative_codes(self) -> None:
        cases = (
            ("operation_executed", "ADMISSION_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "ADMISSION_REVIEW_EMITS_OUTPUT"),
            ("action_authorized", "ADMISSION_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "ADMISSION_REVIEW_CREATES_CONSEQUENCE"),
            ("repository_synchronization_authorized", "ADMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION"),
            ("replay_authorized", "ADMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION"),
            ("non_synchronized_operation_authorized", "ADMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION"),
            ("full_body_transfer_authorized", "ADMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "ADMISSION_REVIEW_CREATES_SECOND_BODY"),
            ("carrier_role_activated_beyond_scope", "ADMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE"),
            ("carrier_authority_created", "ADMISSION_REVIEW_CREATES_CARRIER_AUTHORITY"),
            ("carrier_currentness_created", "ADMISSION_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "ADMISSION_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "ADMISSION_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "ADMISSION_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "ADMISSION_REVIEW_REPLACES_SOURCE"),
            ("reusable_permission_created", "ADMISSION_REVIEW_CREATES_REUSABLE_PERMISSION"),
            ("autonomous_continuation_authorized", "ADMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION"),
            ("refusal_abort_erased", "ADMISSION_REVIEW_ERASES_REFUSAL_ABORT"),
            ("evidence_erased", "ADMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("divergence_resolved", "ADMISSION_REVIEW_RESOLVES_DIVERGENCE"),
            ("public_launch_readiness_created", "ADMISSION_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "ADMISSION_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "ADMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for field, expected_code in cases:
            with self.subTest(field=field):
                request = declared_admission_transition_request()
                request["admission_transition_basis"][field] = True
                result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)
                self.assertIs(result["non_claims"]["operation_admitted"], False)

    def test_mutation_replay_merge_and_required_non_claim_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = declared_admission_transition_request()
                request["admission_transition_basis"][field] = True
                result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
                self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["block_code"], "MUTATION_REPLAY_OR_MERGE_DETECTED")
                self.assertIs(result["non_claims"]["operation_admitted"], False)

        request = declared_admission_transition_request()
        request["declared_non_claims"].pop("operation_executed")
        result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["block_code"], "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertIs(result["non_claims"]["operation_admitted"], False)

        flipped = declared_admission_transition_request()
        flipped["declared_non_claims"]["operation_executed"] = True
        flipped_result = resolver.resolve_distributed_operation_admission_transition_authority_boundary(flipped)
        self.assertEqual(flipped_result["outcome"], OUTCOME_BLOCKED)
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "ADMISSION_REVIEW_EXECUTES_OPERATION"},
        )
        self.assertIs(flipped_result["non_claims"]["operation_admitted"], False)


if __name__ == "__main__":
    unittest.main()
