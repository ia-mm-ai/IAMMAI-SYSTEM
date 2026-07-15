"""Bounded tests for distributed execution / emission boundary.

These tests prove that the resolver records execution / emission boundary
basis only. They do not execute operation, emit output, authorize action,
create consequence, authorize synchronization or non-synchronized operation,
transfer the body, create a second body, create reusable permission, authorize
autonomous continuation, create public readiness, claim final completion, or
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


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_distributed_execution_emission_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL = "DISTRIBUTED_EXECUTION_EMISSION_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_EXECUTION_EMISSION_REVIEW_BLOCKED"
ADMISSION_OUTCOME_RECORDED = (
    "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED"
)

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_EXECUTION_EMISSION_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_execution_emission_metadata",
    "declared_execution_emission_question",
    "selected_admission_transition_result",
    "selected_operation_context",
    "execution_emission_basis",
    "execution_emission_scope",
    "execution_emission_checks",
    "execution_emission_statement",
    "execution_emission_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_execution_emission_summary",
)


def false_non_claims(*, boundary_recorded: bool = True) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["execution_emission_boundary_recorded"] = boundary_recorded
    return claims


def selected_refusal_abort_result() -> dict[str, object]:
    return {
        "distributed_refusal_abort_boundary_metadata": {
            "distributed_refusal_abort_boundary_result_id": "refusal-abort-result-001",
        },
        "outcome": "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED",
        "refusal_abort_statement": {
            "failed_check_count": 0,
            "refusal_abort_postures_preserved": True,
            "non_admission_conditions_named": True,
            "abort_conditions_named": True,
            "refusal_abort_conditions_carry_forward": True,
            "live_operation_refused": False,
            "live_operation_aborted": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "consequence_created": False,
            "follow_on_work_authorized": False,
        },
    }


def selected_sync_non_sync_result() -> dict[str, object]:
    return {
        "distributed_sync_non_sync_boundary_result_id": "sync-non-sync-result-001",
        "outcome": "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED",
        "failed_check_count": 0,
        "sync_non_sync_postures_preserved": True,
        "repository_synchronization_authorized": False,
        "shared_live_state_created": False,
        "state_merge_authorized": False,
        "replay_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "non_synchronized_operation_authorized": False,
    }


def selected_carrier_role_result() -> dict[str, object]:
    return {
        "distributed_carrier_operational_role_metadata": {
            "distributed_carrier_operational_role_result_id": "carrier-role-result-001",
        },
        "outcome": "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED",
        "distributed_carrier_operational_role_summary": {"failed_check_count": 0},
        "carrier_role_basis": {
            "selected_carrier_context": [
                {"carrier_id": "carrier-b", "success_visible": True},
                {"carrier_id": "carrier-c", "block_visible": True},
            ],
            "carrier_evidence_remains_unmerged": True,
            "carrier_context_remains_context_only": True,
        },
        "role_statement": {
            "carrier_roles_activated": False,
            "carrier_authority_created": False,
            "carrier_currentness_created": False,
        },
    }


def selected_source_body_authority_result() -> dict[str, object]:
    return {
        "source_body_operational_authority_result_id": "source-authority-result-001",
        "outcome": "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED",
        "failed_check_count": 0,
        "authority_created": False,
        "permission_created": False,
        "operation_authorized": False,
    }


def selected_eligibility_result() -> dict[str, object]:
    return {
        "distributed_operation_eligibility_result_id": "eligibility-result-001",
        "outcome": "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW",
        "eligibility_remains_eligibility_only": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
    }


def selected_matter_declaration() -> dict[str, object]:
    return {
        "distributed_operation_matter_declaration_result_id": "matter-declaration-001",
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
        "matter_remains_declaration_only": True,
    }


def selected_operation_candidate() -> dict[str, object]:
    return {
        "operation_candidate_id": "operation-candidate-001",
        "operation_question": "What execution / emission boundary basis may be recognized?",
        "operation_purpose": "Preserve boundary readiness for later execution / emission review.",
        "proposed_operation_kind": "FUTURE_EXECUTION_EMISSION_REVIEW",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": "What execution / emission boundary basis may be recognized?",
        "operation_purpose": "Preserve boundary readiness for later execution / emission review.",
        "proposed_operation_kind": "FUTURE_EXECUTION_EMISSION_REVIEW",
        "matter_remains_declaration_only": True,
    }


def admitted_operation_context() -> dict[str, object]:
    return {
        "operation_context_id": "admitted-operation-context-001",
        "one_bounded_operation_context_only": True,
        "execution_emission_requires_separate_boundary": True,
        "action_consequence_requires_separate_boundary": True,
        "receipt_exhaustion_required_after_any_future_execution": True,
    }


def admission_transition_statement() -> dict[str, object]:
    statement = {
        "failed_check_count": 0,
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "selected_refusal_abort_result_preserved": True,
        "selected_sync_non_sync_result_preserved": True,
        "selected_carrier_role_result_preserved": True,
        "selected_source_body_authority_result_preserved": True,
        "selected_eligibility_result_preserved": True,
        "selected_matter_declaration_preserved": True,
        "selected_operation_candidate_preserved": True,
        "selected_operation_matter_preserved": True,
        "refusal_abort_conditions_carry_forward": True,
        "sync_non_sync_postures_preserved": True,
        "carrier_evidence_remains_unmerged": True,
        "carrier_context_remains_context_only": True,
        "divergence_remains_visible": True,
        "refusal_remains_visible": True,
        "blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


def selected_operation_matter_section() -> dict[str, object]:
    return {
        "selected_refusal_abort_result": selected_refusal_abort_result(),
        "selected_sync_non_sync_result": selected_sync_non_sync_result(),
        "selected_carrier_role_result": selected_carrier_role_result(),
        "selected_source_body_authority_result": selected_source_body_authority_result(),
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
    }


def selected_admission_transition_result() -> dict[str, object]:
    return {
        "distributed_operation_admission_transition_metadata": {
            "distributed_operation_admission_transition_result_id": "admission-transition-result-001",
            "distributed_operation_admission_transition_result_version": "0.1.0",
        },
        "outcome": ADMISSION_OUTCOME_RECORDED,
        "selected_operation_matter": selected_operation_matter_section(),
        "admission_transition_basis": {
            "selected_operation_context": admitted_operation_context(),
            "declared_operation_context_scope": admitted_operation_context(),
            "source_body_authority_basis": {
                "authority_basis_id": "source-body-authority-basis-001",
                "authority_basis_is_basis_only": True,
            },
            "carrier_role_basis": {
                "carrier_role_basis_id": "carrier-role-basis-001",
                "carrier_role_basis_is_basis_only": True,
            },
            "sync_non_sync_posture_basis": {
                "sync_non_sync_posture_basis_id": "sync-posture-basis-001",
                "sync_non_sync_basis_is_boundary_only": True,
            },
            "refusal_abort_posture_basis": {
                "refusal_abort_posture_basis_id": "refusal-abort-posture-basis-001",
                "refusal_abort_conditions_carry_forward": True,
            },
        },
        "admission_scope": {
            "selected_admission_scope": ["ONE_OPERATION_CONTEXT_ONLY"],
            "operation_admitted": True,
        },
        "admission_transition_statement": admission_transition_statement(),
        "distributed_operation_admission_transition_summary": {
            "outcome": ADMISSION_OUTCOME_RECORDED,
            "failed_check_count": 0,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
        },
        "non_claims": {
            **{key: False for key in REQUIRED_NON_CLAIMS},
            "operation_admitted": True,
        },
    }


def execution_emission_basis() -> dict[str, object]:
    return {
        "source_body_authority_basis": {
            "authority_basis_id": "source-body-authority-basis-001",
            "authority_basis_is_basis_only": True,
        },
        "carrier_role_basis": {
            "carrier_role_basis_id": "carrier-role-basis-001",
            "carrier_role_basis_is_basis_only": True,
        },
        "sync_non_sync_posture_basis": {
            "sync_non_sync_posture_basis_id": "sync-posture-basis-001",
            "sync_non_sync_basis_is_boundary_only": True,
        },
        "refusal_abort_posture_basis": {
            "refusal_abort_posture_basis_id": "refusal-abort-posture-basis-001",
            "refusal_abort_conditions_carry_forward": True,
        },
    }


def declared_request(
    *,
    selected_admission: dict[str, object] | None = None,
    requested_outcome: str = OUTCOME_RECORDED,
    intent: str = "RECORD_DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY",
) -> dict[str, object]:
    boundary_recorded = requested_outcome == OUTCOME_RECORDED
    return {
        "execution_emission_request_id": "execution-emission-request-001",
        "execution_emission_question": (
            "What execution / emission boundary basis may be recognized for one "
            "admitted operation context?"
        ),
        "execution_emission_intent": intent,
        "selected_admission_transition_result": selected_admission
        if selected_admission is not None
        else selected_admission_transition_result(),
        "selected_admission_transition_result_id": "admission-transition-result-001",
        "selected_admission_transition_result_outcome": ADMISSION_OUTCOME_RECORDED,
        "requested_execution_emission_outcome": requested_outcome,
        "execution_emission_basis": execution_emission_basis(),
        "execution_emission_scope": list(SUPPORTED_SCOPE),
        "proposed_execution_candidate": {
            "execution_candidate_id": "execution-candidate-001",
            "candidate_is_named_not_performed": True,
        },
        "proposed_emission_candidate": {
            "emission_candidate_id": "emission-candidate-001",
            "candidate_is_named_not_emitted": True,
        },
        "proposed_output_family": {
            "output_family_id": "bounded-output-family-001",
            "output_family_named_not_emitted": True,
        },
        "receipt_exhaustion_requirement": {
            "receipt_exhaustion_required": True,
            "requirement": "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
        },
        "action_consequence_separation_requirement": {
            "action_consequence_separation_required": True,
            "requirement": "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY",
        },
        "declared_non_claims": false_non_claims(
            boundary_recorded=boundary_recorded
        ),
    }


def resolve(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_distributed_execution_emission_boundary(
        declared_execution_emission_request=request
    )


def block_code(result: dict[str, object]) -> str | None:
    block = result.get("block", {})
    if isinstance(block, dict):
        return block.get("block_code")
    return None


def delete_path(mapping: dict[str, object], path: tuple[str, ...]) -> None:
    current: object = mapping
    for key in path[:-1]:
        if not isinstance(current, dict):
            return
        current = current.get(key)
    if isinstance(current, dict):
        current.pop(path[-1], None)


class DistributedExecutionEmissionBoundaryTests(unittest.TestCase):
    def assert_recorded_core(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        statement = result["execution_emission_statement"]
        self.assertTrue(statement["distributed_execution_emission_boundary_recorded"])
        self.assertEqual(statement["failed_check_count"], 0)
        for key in (
            "selected_admission_transition_result_preserved",
            "selected_admission_transition_result_recorded",
            "selected_admission_transition_result_failed_check_count_zero",
            "admitted_operation_context_preserved",
            "operation_admitted",
            "one_bounded_operation_context_admitted",
            "selected_refusal_abort_result_preserved",
            "selected_sync_non_sync_result_preserved",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "refusal_abort_conditions_carry_forward",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "execution_emission_scope_one_admitted_operation_context_only",
            "proposed_output_family_named",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
        ):
            self.assertTrue(statement[key], key)
        self.assertFalse(statement["proposed_output_family_emitted"])
        self.assert_no_execution_or_overcommit(statement)

    def assert_no_execution_or_overcommit(self, section: dict[str, object]) -> None:
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
            self.assertIs(section[key], False, key)

    def test_boundary_recorded_result_shape_and_core_posture(self) -> None:
        request = declared_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_core(result)

        metadata = result["distributed_execution_emission_metadata"]
        for key in (
            "distributed_execution_emission_result_id",
            "distributed_execution_emission_result_type",
            "distributed_execution_emission_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["distributed_execution_emission_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_distributed_execution_emission_boundary")

        declared = result["declared_execution_emission_question"]
        self.assertEqual(declared["execution_emission_request_id"], request["execution_emission_request_id"])
        self.assertEqual(declared["execution_emission_question"], request["execution_emission_question"])
        self.assertEqual(declared["execution_emission_intent"], request["execution_emission_intent"])
        self.assertEqual(declared["selected_admission_transition_result_id"], "admission-transition-result-001")
        self.assertEqual(declared["selected_admission_transition_result_outcome"], ADMISSION_OUTCOME_RECORDED)
        for key in (
            "execution_emission_boundary_is_not_execution",
            "execution_emission_boundary_is_not_emission",
            "execution_emission_boundary_is_not_action",
            "execution_emission_boundary_is_not_consequence",
            "execution_emission_boundary_is_not_synchronization",
            "execution_emission_boundary_is_not_full_body_transfer",
            "execution_emission_boundary_is_not_second_body_creation",
            "execution_emission_boundary_is_not_reusable_permission",
            "execution_emission_boundary_is_not_autonomous_continuation",
        ):
            self.assertTrue(declared[key])

        selected = result["selected_admission_transition_result"]
        self.assertEqual(selected["selected_admission_transition_result_id"], "admission-transition-result-001")
        self.assertEqual(selected["selected_admission_transition_result_outcome"], ADMISSION_OUTCOME_RECORDED)
        self.assertTrue(selected["selected_admission_transition_result_outcome_is_recorded"])
        self.assertTrue(selected["selected_admission_transition_result_failed_check_count_zero"])
        self.assertTrue(selected["selected_admitted_operation_context_preserved"])
        self.assertTrue(selected["operation_admitted"])
        self.assertTrue(selected["one_bounded_operation_context_admitted"])
        for key in (
            "selected_admission_transition_result_did_not_execute_operation",
            "selected_admission_transition_result_did_not_emit_output",
            "selected_admission_transition_result_did_not_authorize_action",
            "selected_admission_transition_result_did_not_create_consequence",
            "selected_admission_transition_result_did_not_authorize_sync_non_sync_transfer_second_body_reusable_permission_autonomous_continuation_public_readiness_final_completion_follow_on_work",
        ):
            self.assertTrue(selected[key])

        context = result["selected_operation_context"]
        for key in (
            "selected_admission_transition_result",
            "admitted_operation_context",
            "selected_refusal_abort_result",
            "selected_sync_non_sync_result",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_operation_candidate",
            "selected_operation_matter",
        ):
            self.assertIn(key, context)
            self.assertTrue(context[key])
        self.assertTrue(context["operation_admitted"])
        self.assertTrue(context["one_bounded_operation_context_admitted"])
        self.assertTrue(context["refusal_abort_carry_forward_preserved"])
        self.assertTrue(context["no_operation_executed_emitted_acted_or_made_consequential"])

        basis = result["execution_emission_basis"]
        for key in (
            "selected_admission_transition_result",
            "selected_admitted_operation_context",
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
            "declared_execution_emission_scope",
            "proposed_execution_candidate",
            "proposed_emission_candidate",
            "proposed_output_family",
            "receipt_exhaustion_requirement",
            "action_consequence_separation_requirement",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key])
        for key in (
            "refusal_abort_conditions_carry_forward",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "execution_emission_basis_is_not_execution",
            "execution_emission_basis_is_not_emission",
            "execution_emission_basis_is_not_action",
            "execution_emission_basis_is_not_consequence",
            "execution_emission_basis_is_not_synchronization",
            "execution_emission_basis_is_not_full_body_transfer",
            "execution_emission_basis_is_not_second_body",
            "execution_emission_basis_is_not_reusable_permission",
            "execution_emission_basis_is_not_autonomous_continuation",
        ):
            self.assertTrue(basis[key], key)

    def test_supported_scope_checks_non_meaning_open_items_and_summary(self) -> None:
        result = resolve(declared_request())
        scope = result["execution_emission_scope"]

        self.assertEqual(scope["selected_execution_emission_scope"], list(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_execution_emission_scope_supported"])
        for key in (
            "one_admitted_operation_context_only",
            "no_execution_performed_by_boundary",
            "no_output_emitted_by_boundary",
            "no_action_authorized_by_boundary",
            "no_consequence_created_by_boundary",
            "no_repository_sync_by_boundary",
            "no_non_synchronized_operation_by_boundary",
            "no_full_body_transfer_by_boundary",
            "no_second_body_by_boundary",
            "refusal_abort_conditions_remain_active",
            "receipt_exhaustion_required_before_closure",
            "action_consequence_requires_separate_boundary",
            "no_reusable_permission",
            "no_autonomous_continuation",
        ):
            self.assertTrue(scope[key], key)

        checks = result["execution_emission_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        expected_check_names = {
            "execution_emission_question_declared",
            "execution_emission_intent_supported",
            "selected_admission_transition_result_present",
            "selected_admission_transition_result_outcome_declared",
            "selected_admission_transition_result_outcome_recorded",
            "selected_admission_transition_result_failed_check_count_zero",
            "admitted_operation_context_preserved",
            "operation_admitted_true",
            "one_bounded_operation_context_admitted_true",
            "selected_refusal_abort_result_preserved",
            "selected_sync_non_sync_result_preserved",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "refusal_abort_conditions_carry_forward",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_remains_visible",
            "refusal_remains_visible",
            "blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible",
            "execution_emission_scope_one_admitted_operation_context_only",
            "proposed_output_family_named_but_not_emitted",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
            "no_operation_executed",
            "no_output_emitted",
            "no_action_authorized",
            "no_consequence_created",
            "no_sync_shared_live_state_merge_replay_full_body_transfer_second_body_non_sync_operation_carrier_autonomy_stale_carrier_operation",
            "no_reusable_permission_created",
            "no_autonomous_continuation_authorized",
            "no_public_readiness_final_completion_follow_on_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_check_names.issubset({check["check_name"] for check in checks}))

        non_meaning = result["execution_emission_non_meaning"]
        for key in (
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
            "carrier_roles_activated_beyond_admitted_context_scope",
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
            self.assertTrue(non_meaning[key], key)

        open_items = result["what_remains_open"]
        for key in (
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
            "open_means_not_scheduled",
            "open_means_not_authorized",
            "open_means_not_executed",
        ):
            self.assertTrue(open_items[key], key)

        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        self.assertTrue(non_claims["execution_emission_boundary_recorded"])
        self.assertFalse(non_claims["operation_executed"])
        self.assertFalse(non_claims["output_emitted"])

        summary = resolver.build_distributed_execution_emission_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["execution_emission_request_id"], "execution-emission-request-001")
        self.assertEqual(summary["selected_admission_transition_result_id"], "admission-transition-result-001")
        self.assertEqual(summary["selected_admission_transition_result_outcome"], ADMISSION_OUTCOME_RECORDED)
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "distributed_execution_emission_boundary_recorded",
            "selected_admission_transition_result_preserved",
            "selected_admission_transition_result_recorded",
            "selected_admission_transition_result_failed_check_count_zero",
            "admitted_operation_context_preserved",
            "operation_admitted",
            "one_bounded_operation_context_admitted",
            "selected_refusal_abort_result_preserved",
            "selected_sync_non_sync_result_preserved",
            "selected_carrier_role_result_preserved",
            "selected_source_body_authority_result_preserved",
            "selected_eligibility_result_preserved",
            "selected_matter_declaration_preserved",
            "selected_operation_candidate_preserved",
            "selected_operation_matter_preserved",
            "refusal_abort_conditions_carry_forward",
            "sync_non_sync_postures_preserved",
            "carrier_evidence_remains_unmerged",
            "carrier_context_remains_context_only",
            "divergence_refusal_blocked_attempts_projection_mismatch_visible",
            "execution_emission_scope_one_admitted_operation_context_only",
            "proposed_output_family_named_but_not_emitted",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
            "no_operation_executed_output_emitted_action_consequence",
            "no_sync_full_body_transfer_second_body_non_sync_operation",
            "no_reusable_permission_autonomous_continuation",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertTrue(summary[key], key)

    def test_requires_additional_basis_and_not_ready_outcomes(self) -> None:
        additional_request = declared_request(
            requested_outcome=OUTCOME_REQUIRES_ADDITIONAL
        )
        additional_request["additional_basis_context"] = {
            "execution_emission_scope_too_generic": True,
            "proposed_output_family_not_bounded_enough": True,
            "execution_emission_cannot_yet_be_bounded_without_consequence_risk": True,
        }
        additional_result = resolve(additional_request)
        self.assertEqual(additional_result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertFalse(additional_result["non_claims"]["execution_emission_boundary_recorded"])
        self.assertTrue(additional_result["selected_admission_transition_result"]["selected_admission_transition_result"])
        self.assertTrue(additional_result["additional_basis_required"]["additional_basis_required"])
        self.assertEqual(
            additional_result["additional_basis_required"]["additional_basis_context"],
            additional_request["additional_basis_context"],
        )
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_executed"])
        self.assert_no_execution_or_overcommit(additional_result["execution_emission_statement"])

        not_ready_request = declared_request(requested_outcome=OUTCOME_NOT_READY)
        not_ready_request["not_ready_reason"] = (
            "Admitted context lacks sufficient execution / emission basis."
        )
        not_ready_result = resolve(not_ready_request)
        self.assertEqual(not_ready_result["outcome"], OUTCOME_NOT_READY)
        self.assertFalse(not_ready_result["non_claims"]["execution_emission_boundary_recorded"])
        self.assertEqual(
            not_ready_result["execution_emission_statement"]["not_ready_reason"],
            not_ready_request["not_ready_reason"],
        )
        self.assertTrue(not_ready_result["selected_admission_transition_result"]["selected_admission_transition_result"])
        self.assert_no_execution_or_overcommit(not_ready_result["execution_emission_statement"])

        observed = {
            resolve(declared_request())["outcome"],
            additional_result["outcome"],
            not_ready_result["outcome"],
            resolve(None)["outcome"],
        }
        self.assertEqual(
            observed,
            {OUTCOME_RECORDED, OUTCOME_REQUIRES_ADDITIONAL, OUTCOME_NOT_READY, OUTCOME_BLOCKED},
        )

    def test_request_builder_helper_records_valid_boundary(self) -> None:
        selected = selected_admission_transition_result()
        basis = execution_emission_basis()
        request = resolver.build_declared_distributed_execution_emission_request(
            "builder-request-001",
            "What execution / emission boundary basis may be recognized?",
            selected,
            basis,
            list(SUPPORTED_SCOPE),
            selected_admission_transition_result_id="admission-transition-result-001",
            selected_admission_transition_result_outcome=ADMISSION_OUTCOME_RECORDED,
            proposed_execution_candidate={"execution_candidate_id": "exec-builder"},
            proposed_emission_candidate={"emission_candidate_id": "emit-builder"},
            proposed_output_family={"output_family_id": "output-builder"},
            additional_basis_context={"not_used_for_recorded": False},
        )
        request.pop("additional_basis_context")

        self.assertEqual(request["execution_emission_request_id"], "builder-request-001")
        self.assertEqual(request["execution_emission_question"], "What execution / emission boundary basis may be recognized?")
        self.assertEqual(request["selected_admission_transition_result"], selected)
        self.assertEqual(request["execution_emission_basis"], basis)
        self.assertEqual(request["execution_emission_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_admission_transition_result_id"], "admission-transition-result-001")
        self.assertEqual(request["selected_admission_transition_result_outcome"], ADMISSION_OUTCOME_RECORDED)
        self.assertEqual(request["proposed_execution_candidate"], {"execution_candidate_id": "exec-builder"})
        self.assertEqual(request["proposed_emission_candidate"], {"emission_candidate_id": "emit-builder"})
        self.assertEqual(request["proposed_output_family"], {"output_family_id": "output-builder"})
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve(request)
        self.assert_recorded_core(result)

    def test_path_based_selected_admission_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            selected_path = temp / "selected_admission_result.json"
            selected_path.write_text(
                json.dumps(selected_admission_transition_result()),
                encoding="utf-8",
            )

            request = declared_request()
            request.pop("selected_admission_transition_result")
            request["selected_admission_transition_result_path"] = str(selected_path)
            result = resolve(request)
            self.assert_recorded_core(result)
            selected = result["selected_admission_transition_result"]
            self.assertEqual(selected["selected_admission_transition_result_path"], str(selected_path))
            self.assertEqual(selected["selected_admission_transition_result_id"], "admission-transition-result-001")
            self.assertEqual(selected["selected_admission_transition_result_outcome"], ADMISSION_OUTCOME_RECORDED)

            request_path = temp / "declared_execution_emission_request.json"
            request_path.write_text(json.dumps(declared_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_execution_emission_boundary_from_path(request_path)
            mapping_result = resolve(declared_request())
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_execution_emission_question"]["execution_emission_request_path"],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_deduplicates(self) -> None:
        result = resolve(declared_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "result.json"
            written = resolver.write_distributed_execution_emission_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_ROOT",
                Path(temp_dir) / "default-root",
            ):
                first = resolver.write_distributed_execution_emission_result(result)
                second = resolver.write_distributed_execution_emission_result(result)
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, Path(temp_dir) / "default-root")
                self.assertEqual(second.parent, Path(temp_dir) / "default-root")
                self.assertIn("execution-emission-request-001", first.name)
                self.assertTrue(second.stem.endswith("_001"))
                self.assertNotIn(
                    "distributed_operation_admission_transition_authority_boundary",
                    str(first),
                )

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        original_request = copy.deepcopy(request)
        original_selected = copy.deepcopy(request["selected_admission_transition_result"])
        original_basis = copy.deepcopy(request["execution_emission_basis"])
        original_scope = copy.deepcopy(request["execution_emission_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_admission_transition_result"], original_selected)
        self.assertEqual(request["execution_emission_basis"], original_basis)
        self.assertEqual(request["execution_emission_scope"], original_scope)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            upstream_paths = []
            for name in (
                "selected_admission.json",
                "selected_refusal_abort.json",
                "selected_sync.json",
                "selected_carrier_role.json",
                "selected_authority.json",
                "selected_eligibility.json",
                "selected_matter_declaration.json",
            ):
                path = temp / name
                path.write_text(json.dumps({"name": name}), encoding="utf-8")
                upstream_paths.append(path)
            before = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            resolver.write_distributed_execution_emission_result(first, temp / "new" / "result.json")
            after = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            self.assertEqual(before, after)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        blocked = declared_request(intent="BLOCK_DISTRIBUTED_EXECUTION_EMISSION_REVIEW")
        result = resolve(blocked)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "EXECUTION_EMISSION_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(result["execution_emission_statement"]["distributed_execution_emission_boundary_recorded"])

        missing = resolve(None)
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing), "EXECUTION_EMISSION_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_execution_emission_boundary(
            declared_execution_emission_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(malformed), "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            unreadable = resolver.resolve_distributed_execution_emission_boundary_from_path(
                temp / "missing.json"
            )
            self.assertEqual(block_code(unreadable), "DECLARED_EXECUTION_EMISSION_REQUEST_UNREADABLE")

            bad_json = temp / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = resolver.resolve_distributed_execution_emission_boundary_from_path(bad_json)
            self.assertEqual(block_code(bad), "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED")

            array_json = temp / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_execution_emission_boundary_from_path(array_json)
            self.assertEqual(block_code(array_result), "DECLARED_EXECUTION_EMISSION_REQUEST_MALFORMED")

            request = declared_request()
            request.pop("selected_admission_transition_result")
            request["selected_admission_transition_result_path"] = str(temp / "missing-selected.json")
            selected_missing = resolve(request)
            self.assertEqual(block_code(selected_missing), "ADMISSION_TRANSITION_RESULT_UNREADABLE")

            malformed_selected_path = temp / "malformed-selected.json"
            malformed_selected_path.write_text("{bad", encoding="utf-8")
            request["selected_admission_transition_result_path"] = str(malformed_selected_path)
            self.assertEqual(block_code(resolve(request)), "ADMISSION_TRANSITION_RESULT_MALFORMED")

            array_selected_path = temp / "array-selected.json"
            array_selected_path.write_text("[]", encoding="utf-8")
            request["selected_admission_transition_result_path"] = str(array_selected_path)
            self.assertEqual(block_code(resolve(request)), "ADMISSION_TRANSITION_RESULT_MALFORMED")

    def test_selected_admission_result_issue_blocks(self) -> None:
        cases = (
            (
                ("outcome",),
                None,
                "ADMISSION_TRANSITION_RESULT_OUTCOME_MISSING",
            ),
            (
                ("outcome",),
                "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_NOT_ADMITTED",
                "ADMISSION_TRANSITION_RESULT_NOT_RECORDED",
            ),
            (
                ("admission_transition_statement", "failed_check_count"),
                1,
                "ADMISSION_TRANSITION_RESULT_HAS_FAILED_CHECKS",
            ),
            (
                ("admission_transition_statement", "operation_admitted"),
                False,
                "OPERATION_NOT_ADMITTED",
            ),
            (
                ("admission_transition_statement", "one_bounded_operation_context_admitted"),
                False,
                "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
            ),
        )
        for path, value, expected_code in cases:
            selected = selected_admission_transition_result()
            if value is None:
                delete_path(selected, path)
                if path[-1] == "outcome":
                    delete_path(
                        selected,
                        ("distributed_operation_admission_transition_summary", "outcome"),
                    )
            else:
                current = selected
                for key in path[:-1]:
                    current = current[key]
                current[path[-1]] = value
                if path[-1] == "failed_check_count":
                    selected["distributed_operation_admission_transition_summary"][
                        "failed_check_count"
                    ] = value
                if path[-1] == "operation_admitted":
                    selected["distributed_operation_admission_transition_summary"][
                        "operation_admitted"
                    ] = value
                    selected["non_claims"]["operation_admitted"] = value
                if path[-1] == "one_bounded_operation_context_admitted":
                    selected["distributed_operation_admission_transition_summary"][
                        "one_bounded_operation_context_admitted"
                    ] = value
            result = resolve(declared_request(selected_admission=selected))
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code)

    def test_missing_required_basis_blocks(self) -> None:
        selected_missing_cases = (
            (("admission_transition_basis", "selected_operation_context"), "ADMITTED_OPERATION_CONTEXT_MISSING"),
            (("selected_operation_matter", "selected_refusal_abort_result"), "REFUSAL_ABORT_RESULT_MISSING"),
            (("selected_operation_matter", "selected_sync_non_sync_result"), "SYNC_NON_SYNC_RESULT_MISSING"),
            (("selected_operation_matter", "selected_carrier_role_result"), "CARRIER_ROLE_RESULT_MISSING"),
            (("selected_operation_matter", "selected_source_body_authority_result"), "SOURCE_BODY_AUTHORITY_RESULT_MISSING"),
            (("selected_operation_matter", "selected_eligibility_result"), "SELECTED_ELIGIBILITY_RESULT_MISSING"),
            (("selected_operation_matter", "selected_matter_declaration"), "SELECTED_MATTER_DECLARATION_MISSING"),
            (("selected_operation_matter", "selected_operation_candidate"), "SELECTED_OPERATION_CANDIDATE_MISSING"),
            (("selected_operation_matter", "selected_operation_matter"), "SELECTED_OPERATION_MATTER_MISSING"),
        )
        for path, expected_code in selected_missing_cases:
            selected = selected_admission_transition_result()
            if expected_code == "ADMITTED_OPERATION_CONTEXT_MISSING":
                selected_section = selected["selected_operation_matter"]
                delete_path(selected, ("admission_transition_basis", "selected_operation_context"))
                delete_path(selected, ("admission_transition_basis", "declared_operation_context_scope"))
                delete_path(selected, ("admission_transition_basis", "operation_context_scope"))
                delete_path(selected, ("selected_operation_matter",))
                request = declared_request(selected_admission=selected)
                request["selected_refusal_abort_result"] = selected_section["selected_refusal_abort_result"]
                request["selected_sync_non_sync_result"] = selected_section["selected_sync_non_sync_result"]
                request["selected_carrier_role_result"] = selected_section["selected_carrier_role_result"]
                request["selected_source_body_authority_result"] = selected_section["selected_source_body_authority_result"]
                request["selected_eligibility_result"] = selected_section["selected_eligibility_result"]
                request["selected_matter_declaration"] = selected_section["selected_matter_declaration"]
                request["selected_operation_candidate"] = selected_section["selected_operation_candidate"]
                request["selected_operation_matter"] = selected_section["selected_operation_matter"]
            else:
                delete_path(selected, path)
                request = declared_request(selected_admission=selected)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

        request_missing_cases = (
            ("execution_emission_scope", "EXECUTION_EMISSION_SCOPE_MISSING"),
            ("proposed_output_family", "PROPOSED_OUTPUT_FAMILY_MISSING"),
            ("receipt_exhaustion_requirement", "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING"),
            ("action_consequence_separation_requirement", "ACTION_CONSEQUENCE_SEPARATION_REQUIREMENT_MISSING"),
        )
        for key, expected_code in request_missing_cases:
            request = declared_request()
            request.pop(key)
            request["execution_emission_basis"].pop(key, None)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

    def test_unsupported_execution_emission_scope_blocks(self) -> None:
        request = declared_request()
        request["execution_emission_scope"] = list(SUPPORTED_SCOPE) + [
            "UNSUPPORTED_SCOPE"
        ]
        result = resolve(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_EXECUTION_EMISSION_SCOPE")

    def test_execution_emission_collapse_flags_block(self) -> None:
        cases = (
            ("operation_executed", "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "EXECUTION_EMISSION_REVIEW_EMITS_OUTPUT"),
            ("action_authorized", "EXECUTION_EMISSION_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "EXECUTION_EMISSION_REVIEW_CREATES_CONSEQUENCE"),
            ("repository_synchronization_authorized", "EXECUTION_EMISSION_REVIEW_AUTHORIZES_SYNCHRONIZATION"),
            ("non_synchronized_operation_authorized", "EXECUTION_EMISSION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION"),
            ("full_body_transfer_authorized", "EXECUTION_EMISSION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "EXECUTION_EMISSION_REVIEW_CREATES_SECOND_BODY"),
            ("carrier_role_activated_beyond_scope", "EXECUTION_EMISSION_REVIEW_ACTIVATES_CARRIER_ROLES_BEYOND_SCOPE"),
            ("carrier_authority_created", "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_AUTHORITY"),
            ("carrier_currentness_created", "EXECUTION_EMISSION_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "EXECUTION_EMISSION_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "EXECUTION_EMISSION_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "EXECUTION_EMISSION_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "EXECUTION_EMISSION_REVIEW_REPLACES_SOURCE"),
            ("reusable_permission_created", "EXECUTION_EMISSION_REVIEW_CREATES_REUSABLE_PERMISSION"),
            ("autonomous_continuation_authorized", "EXECUTION_EMISSION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION"),
            ("refusal_abort_erased", "EXECUTION_EMISSION_REVIEW_ERASES_REFUSAL_ABORT"),
            ("evidence_erased", "EXECUTION_EMISSION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("divergence_resolved", "EXECUTION_EMISSION_REVIEW_RESOLVES_DIVERGENCE"),
            ("public_launch_readiness_created", "EXECUTION_EMISSION_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "EXECUTION_EMISSION_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "EXECUTION_EMISSION_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for field, expected_code in cases:
            request = declared_request()
            request[field] = True
            result = resolve(request)
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code, field)

    def test_mutation_replay_merge_and_nonclaim_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            request = declared_request()
            request[field] = True
            result = resolve(request)
            self.assertEqual(block_code(result), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_claim = declared_request()
        missing_claim["declared_non_claims"].pop("output_emitted")
        missing_result = resolve(missing_claim)
        self.assertEqual(missing_result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing_result), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_claim = declared_request()
        flipped_claim["declared_non_claims"]["operation_executed"] = True
        flipped_result = resolve(flipped_claim)
        self.assertEqual(flipped_result["outcome"], OUTCOME_BLOCKED)
        self.assertIn(
            block_code(flipped_result),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "EXECUTION_EMISSION_REVIEW_EXECUTES_OPERATION"},
        )


if __name__ == "__main__":
    unittest.main()
