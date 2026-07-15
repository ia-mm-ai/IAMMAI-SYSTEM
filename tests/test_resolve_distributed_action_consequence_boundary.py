"""Bounded tests for distributed action / consequence boundary.

These tests prove that the resolver records action / consequence boundary
basis only. They do not authorize action, create consequence, execute
operation, emit output, treat output/evidence/standing/receipt as consequence,
authorize synchronization or non-synchronized operation, transfer the body,
create a second body, create reusable permission, authorize autonomous
continuation, create public readiness, claim final completion, or schedule
follow-on work.
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

import resolve_distributed_action_consequence_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL = (
    "DISTRIBUTED_ACTION_CONSEQUENCE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_ACTION_CONSEQUENCE_REVIEW_BLOCKED"
EXECUTION_OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_ACTION_CONSEQUENCE_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_action_consequence_metadata",
    "declared_action_consequence_question",
    "selected_execution_emission_result",
    "selected_operation_context",
    "action_consequence_basis",
    "action_consequence_scope",
    "action_consequence_checks",
    "action_consequence_statement",
    "action_consequence_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_action_consequence_summary",
)

FALSE_ACTION_CONSEQUENCE_KEYS = (
    "action_authorized",
    "consequence_created",
    "operation_executed",
    "output_emitted",
    "output_treated_as_consequence",
    "evidence_treated_as_consequence",
    "standing_treated_as_consequence",
    "receipt_treated_as_consequence",
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
)


def false_non_claims(*, boundary_recorded: bool = True) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["action_consequence_boundary_recorded"] = boundary_recorded
    return claims


def selected_admission_transition_result() -> dict[str, object]:
    return {
        "distributed_operation_admission_transition_metadata": {
            "distributed_operation_admission_transition_result_id": (
                "admission-transition-result-001"
            ),
        },
        "outcome": "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED",
        "admission_transition_statement": {
            "failed_check_count": 0,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
            "operation_executed": False,
            "output_emitted": False,
            "action_authorized": False,
            "consequence_created": False,
        },
    }


def admitted_operation_context() -> dict[str, object]:
    return {
        "operation_context_id": "admitted-operation-context-001",
        "one_bounded_operation_context_only": True,
        "execution_emission_boundary_recorded": True,
        "action_consequence_requires_separate_boundary": True,
        "receipt_exhaustion_required_after_any_future_execution": True,
    }


def selected_refusal_abort_result() -> dict[str, object]:
    return {
        "distributed_refusal_abort_boundary_metadata": {
            "distributed_refusal_abort_boundary_result_id": "refusal-abort-result-001",
        },
        "outcome": "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED",
        "failed_check_count": 0,
        "refusal_abort_conditions_carry_forward": True,
        "live_operation_refused": False,
        "live_operation_aborted": False,
        "refusal_abort_erased": False,
    }


def selected_sync_non_sync_result() -> dict[str, object]:
    return {
        "distributed_sync_non_sync_boundary_result_id": "sync-non-sync-result-001",
        "outcome": "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED",
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
        "carrier_role_basis": {
            "carrier_evidence_remains_unmerged": True,
            "carrier_context_remains_context_only": True,
            "carrier_success_is_context_only": True,
        },
        "carrier_authority_created": False,
        "carrier_currentness_created": False,
    }


def selected_source_body_authority_result() -> dict[str, object]:
    return {
        "source_body_operational_authority_result_id": "source-authority-result-001",
        "outcome": "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED",
        "authority_created": False,
        "permission_created": False,
    }


def selected_eligibility_result() -> dict[str, object]:
    return {
        "distributed_operation_eligibility_result_id": "eligibility-result-001",
        "outcome": "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW",
        "eligibility_remains_eligibility_only": True,
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
        "operation_question": (
            "What action / consequence boundary basis may be recognized?"
        ),
        "operation_purpose": "Preserve action and consequence as separate future work.",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": (
            "What action / consequence boundary basis may be recognized?"
        ),
        "operation_purpose": "Preserve action and consequence as separate future work.",
        "matter_remains_declaration_only": True,
    }


def proposed_output_family() -> dict[str, object]:
    return {
        "output_family_id": "bounded-output-family-001",
        "output_family_named_not_emitted": True,
        "output_family_is_not_consequence": True,
    }


def receipt_exhaustion_requirement() -> dict[str, object]:
    return {
        "receipt_exhaustion_required": True,
        "requirement": "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
    }


def action_consequence_separation_requirement() -> dict[str, object]:
    return {
        "action_consequence_separation_required": True,
        "requirement": "ACTION_CONSEQUENCE_REQUIRES_SEPARATE_BOUNDARY",
    }


def selected_operation_context_section() -> dict[str, object]:
    return {
        "selected_admission_transition_result": selected_admission_transition_result(),
        "admitted_operation_context": admitted_operation_context(),
        "selected_refusal_abort_result": selected_refusal_abort_result(),
        "selected_sync_non_sync_result": selected_sync_non_sync_result(),
        "selected_carrier_role_result": selected_carrier_role_result(),
        "selected_source_body_authority_result": selected_source_body_authority_result(),
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "proposed_output_family": proposed_output_family(),
        "receipt_exhaustion_requirement": receipt_exhaustion_requirement(),
        "action_consequence_separation_requirement": (
            action_consequence_separation_requirement()
        ),
    }


def execution_emission_statement() -> dict[str, object]:
    statement = {
        "failed_check_count": 0,
        "distributed_execution_emission_boundary_recorded": True,
        "selected_admission_transition_result_preserved": True,
        "admitted_operation_context_preserved": True,
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
        "proposed_output_family_named": True,
        "proposed_output_family_emitted": False,
        "receipt_exhaustion_requirement_present": True,
        "action_consequence_separation_present": True,
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


def selected_execution_emission_result() -> dict[str, object]:
    context = selected_operation_context_section()
    basis = {
        "selected_admission_transition_result": context[
            "selected_admission_transition_result"
        ],
        "selected_admitted_operation_context": context["admitted_operation_context"],
        "selected_refusal_abort_result": context["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": context["selected_sync_non_sync_result"],
        "selected_carrier_role_result": context["selected_carrier_role_result"],
        "selected_source_body_authority_result": context[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": context["selected_eligibility_result"],
        "selected_matter_declaration": context["selected_matter_declaration"],
        "selected_operation_candidate": context["selected_operation_candidate"],
        "selected_operation_matter": context["selected_operation_matter"],
        "proposed_output_family": context["proposed_output_family"],
        "receipt_exhaustion_requirement": context["receipt_exhaustion_requirement"],
        "action_consequence_separation_requirement": context[
            "action_consequence_separation_requirement"
        ],
        "refusal_abort_carry_forward_conditions": {
            "refusal_abort_conditions_carry_forward": True,
        },
        "evidence_carrier_context_posture": {
            "carrier_evidence_is_not_consequence": True,
            "carrier_context_remains_context_only": True,
        },
    }
    statement = execution_emission_statement()
    return {
        "distributed_execution_emission_metadata": {
            "distributed_execution_emission_result_id": "execution-emission-result-001",
            "distributed_execution_emission_result_version": "0.1.0",
        },
        "outcome": EXECUTION_OUTCOME_RECORDED,
        "selected_operation_context": context,
        "execution_emission_basis": basis,
        "execution_emission_statement": statement,
        "distributed_execution_emission_summary": {
            "outcome": EXECUTION_OUTCOME_RECORDED,
            "failed_check_count": 0,
            "distributed_execution_emission_boundary_recorded": True,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
            "proposed_output_family_named": True,
            "proposed_output_family_emitted": False,
            "receipt_exhaustion_requirement_present": True,
            "action_consequence_separation_present": True,
        },
        "non_claims": {
            **{key: False for key in REQUIRED_NON_CLAIMS},
            "distributed_execution_emission_boundary_recorded": True,
        },
    }


def action_consequence_basis(
    selected_execution: dict[str, object] | None = None,
) -> dict[str, object]:
    selected = selected_execution if selected_execution is not None else (
        selected_execution_emission_result()
    )
    context = selected["selected_operation_context"]
    basis = selected["execution_emission_basis"]
    return {
        "selected_execution_emission_result": selected,
        "selected_admission_transition_result": basis[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": context["admitted_operation_context"],
        "selected_refusal_abort_result": basis["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": basis["selected_sync_non_sync_result"],
        "selected_carrier_role_result": basis["selected_carrier_role_result"],
        "selected_source_body_authority_result": basis[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": basis["selected_eligibility_result"],
        "selected_matter_declaration": basis["selected_matter_declaration"],
        "selected_operation_candidate": basis["selected_operation_candidate"],
        "selected_operation_matter": basis["selected_operation_matter"],
        "proposed_output_family": basis["proposed_output_family"],
        "receipt_exhaustion_requirement": basis["receipt_exhaustion_requirement"],
        "action_consequence_separation_requirement": basis[
            "action_consequence_separation_requirement"
        ],
        "refusal_abort_carry_forward_conditions": basis[
            "refusal_abort_carry_forward_conditions"
        ],
        "evidence_carrier_context_posture": basis["evidence_carrier_context_posture"],
        "declared_action_consequence_scope": list(SUPPORTED_SCOPE),
        "proposed_action_posture": {
            "action_posture_id": "action-posture-001",
            "action_authorized": False,
        },
        "proposed_consequence_posture": {
            "consequence_posture_id": "consequence-posture-001",
            "consequence_created": False,
        },
    }


def declared_request(
    *,
    selected_execution: dict[str, object] | None = None,
    requested_outcome: str = OUTCOME_RECORDED,
    intent: str = "RECORD_DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY",
) -> dict[str, object]:
    selected = selected_execution if selected_execution is not None else (
        selected_execution_emission_result()
    )
    boundary_recorded = requested_outcome == OUTCOME_RECORDED
    return {
        "action_consequence_request_id": "action-consequence-request-001",
        "action_consequence_question": (
            "What action / consequence boundary basis may be recognized for one "
            "admitted operation context after execution / emission boundary basis?"
        ),
        "action_consequence_intent": intent,
        "selected_execution_emission_result": selected,
        "selected_execution_emission_result_id": "execution-emission-result-001",
        "selected_execution_emission_result_outcome": EXECUTION_OUTCOME_RECORDED,
        "requested_action_consequence_outcome": requested_outcome,
        "action_consequence_basis": action_consequence_basis(selected),
        "action_consequence_scope": list(SUPPORTED_SCOPE),
        "proposed_action_posture": {
            "action_posture_id": "action-posture-001",
            "action_authorized": False,
        },
        "proposed_consequence_posture": {
            "consequence_posture_id": "consequence-posture-001",
            "consequence_created": False,
        },
        "declared_non_claims": false_non_claims(
            boundary_recorded=boundary_recorded
        ),
    }


def resolve(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_distributed_action_consequence_boundary(
        declared_action_consequence_request=request
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


def set_path(mapping: dict[str, object], path: tuple[str, ...], value: object) -> None:
    current: object = mapping
    for key in path[:-1]:
        if not isinstance(current, dict):
            return
        current = current[key]
    if isinstance(current, dict):
        current[path[-1]] = value


def remove_basis_everywhere(
    request: dict[str, object],
    basis_key: str,
    *,
    context_key: str | None = None,
    execution_basis_key: str | None = None,
) -> None:
    selected = request["selected_execution_emission_result"]
    assert isinstance(selected, dict)
    basis = request["action_consequence_basis"]
    assert isinstance(basis, dict)
    basis.pop(basis_key, None)
    selected_context = selected.get("selected_operation_context")
    if isinstance(selected_context, dict):
        selected_context.pop(context_key or basis_key, None)
    execution_basis = selected.get("execution_emission_basis")
    if isinstance(execution_basis, dict):
        execution_basis.pop(execution_basis_key or basis_key, None)


class DistributedActionConsequenceBoundaryTests(unittest.TestCase):
    def assert_no_action_consequence_or_overcommit(
        self, section: dict[str, object]
    ) -> None:
        for key in FALSE_ACTION_CONSEQUENCE_KEYS:
            self.assertIs(section[key], False, key)

    def assert_recorded_core(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        statement = result["action_consequence_statement"]
        self.assertTrue(statement["distributed_action_consequence_boundary_recorded"])
        self.assertEqual(statement["failed_check_count"], 0)
        for key in (
            "selected_execution_emission_result_preserved",
            "selected_execution_emission_result_recorded",
            "selected_execution_emission_result_failed_check_count_zero",
            "selected_admission_transition_result_preserved",
            "selected_admitted_operation_context_preserved",
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
            "proposed_output_family_named",
            "output_family_is_not_consequence",
            "carrier_evidence_is_not_consequence",
            "standing_is_not_consequence",
            "receipt_is_not_consequence",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
            "action_consequence_scope_supported",
        ):
            self.assertTrue(statement[key], key)
        self.assertFalse(statement["proposed_output_family_emitted"])
        self.assert_no_action_consequence_or_overcommit(statement)

    def test_boundary_recorded_result_shape_and_core_posture(self) -> None:
        request = declared_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_core(result)

        metadata = result["distributed_action_consequence_metadata"]
        for key in (
            "distributed_action_consequence_result_id",
            "distributed_action_consequence_result_type",
            "distributed_action_consequence_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["distributed_action_consequence_result_version"], "0.1.0"
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_action_consequence_boundary",
        )

        declared = result["declared_action_consequence_question"]
        self.assertEqual(
            declared["action_consequence_request_id"],
            request["action_consequence_request_id"],
        )
        self.assertEqual(
            declared["action_consequence_question"],
            request["action_consequence_question"],
        )
        self.assertEqual(
            declared["action_consequence_intent"],
            request["action_consequence_intent"],
        )
        self.assertEqual(
            declared["selected_execution_emission_result_id"],
            "execution-emission-result-001",
        )
        self.assertEqual(
            declared["selected_execution_emission_result_outcome"],
            EXECUTION_OUTCOME_RECORDED,
        )
        for key in (
            "action_consequence_boundary_is_not_action",
            "action_consequence_boundary_is_not_consequence",
            "action_consequence_boundary_is_not_execution",
            "action_consequence_boundary_is_not_emission",
            "action_consequence_boundary_is_not_synchronization",
            "action_consequence_boundary_is_not_full_body_transfer",
            "action_consequence_boundary_is_not_second_body",
            "action_consequence_boundary_is_not_reusable_permission",
            "action_consequence_boundary_is_not_autonomous_continuation",
        ):
            self.assertTrue(declared[key], key)

        selected = result["selected_execution_emission_result"]
        self.assertEqual(
            selected["selected_execution_emission_result_id"],
            "execution-emission-result-001",
        )
        self.assertEqual(
            selected["selected_execution_emission_result_outcome"],
            EXECUTION_OUTCOME_RECORDED,
        )
        self.assertTrue(selected["selected_execution_emission_result_outcome_is_recorded"])
        self.assertTrue(
            selected["selected_execution_emission_result_failed_check_count_zero"]
        )
        self.assertTrue(selected["selected_execution_emission_boundary_preserved"])
        for key in (
            "selected_execution_emission_result_did_not_execute_operation",
            "selected_execution_emission_result_did_not_emit_output",
            "selected_execution_emission_result_did_not_authorize_action",
            "selected_execution_emission_result_did_not_create_consequence",
            "selected_execution_emission_result_preserved_proposed_output_family_named",
            "selected_execution_emission_result_preserved_proposed_output_family_not_emitted",
            "selected_execution_emission_result_preserved_receipt_exhaustion_requirement",
            "selected_execution_emission_result_preserved_action_consequence_separation",
        ):
            self.assertTrue(selected[key], key)

        context = result["selected_operation_context"]
        for key in (
            "selected_execution_emission_result",
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
            self.assertTrue(context[key], key)
        self.assertTrue(context["operation_admitted"])
        self.assertTrue(context["one_bounded_operation_context_admitted"])
        self.assertTrue(context["execution_emission_boundary_recorded"])
        for key in (
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
        ):
            self.assertIs(context[key], False, key)

        basis = result["action_consequence_basis"]
        for key in (
            "selected_execution_emission_result",
            "selected_admission_transition_result",
            "selected_operation_context",
            "selected_refusal_abort_result",
            "selected_sync_non_sync_result",
            "selected_carrier_role_result",
            "selected_source_body_authority_result",
            "selected_eligibility_result",
            "selected_matter_declaration",
            "selected_operation_candidate",
            "selected_operation_matter",
            "proposed_output_family",
            "receipt_exhaustion_requirement",
            "action_consequence_separation_requirement",
            "refusal_abort_carry_forward_conditions",
            "evidence_carrier_context_posture",
            "declared_action_consequence_scope",
            "proposed_action_posture",
            "proposed_consequence_posture",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "output_family_is_not_consequence",
            "carrier_evidence_is_not_consequence",
            "standing_is_not_consequence",
            "receipt_is_not_consequence",
            "action_consequence_basis_is_not_action",
            "action_consequence_basis_is_not_consequence",
            "action_consequence_basis_is_not_execution",
            "action_consequence_basis_is_not_emission",
            "action_consequence_basis_is_not_receipt",
            "action_consequence_basis_is_not_closure",
            "public_readiness_remains_false",
            "final_completion_remains_false",
        ):
            self.assertTrue(basis[key], key)

    def test_scope_checks_non_meaning_open_items_non_claims_and_summary(self) -> None:
        result = resolve(declared_request())
        scope = result["action_consequence_scope"]

        self.assertEqual(scope["selected_action_consequence_scope"], list(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_action_consequence_scope_supported"])
        for key in (
            "no_action_authorized_by_boundary",
            "no_consequence_created_by_boundary",
            "no_execution_by_action_consequence_boundary",
            "no_output_emission_by_action_consequence_boundary",
            "output_family_is_not_consequence",
            "carrier_evidence_is_not_consequence",
            "standing_is_not_consequence",
            "receipt_is_not_consequence",
            "consequence_recognition_requires_separate_act",
            "receipt_exhaustion_required_before_closure",
            "conformance_required_before_closure",
            "closure_requires_separate_boundary",
            "no_reusable_permission",
            "no_autonomous_continuation",
        ):
            self.assertTrue(scope[key], key)

        checks = result["action_consequence_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        expected_check_names = {
            "action_consequence_question_declared",
            "action_consequence_intent_supported",
            "selected_execution_emission_result_present",
            "selected_execution_emission_result_outcome_declared",
            "selected_execution_emission_result_outcome_recorded",
            "selected_execution_emission_result_failed_check_count_zero",
            "selected_execution_emission_boundary_preserved",
            "selected_admission_transition_result_preserved",
            "selected_admitted_operation_context_preserved",
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
            "proposed_output_family_named_but_not_emitted",
            "proposed_output_family_not_consequence",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
            "action_consequence_scope_supported",
            "no_action_authorized",
            "no_consequence_created",
            "no_operation_executed",
            "no_output_emitted",
            "no_output_evidence_standing_receipt_treated_as_consequence",
            "no_sync_shared_live_state_merge_replay_full_body_transfer_second_body_non_sync_operation_carrier_autonomy_stale_carrier_operation",
            "no_reusable_permission_created",
            "no_autonomous_continuation_authorized",
            "no_public_readiness_final_completion_follow_on_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_check_names.issubset({c["check_name"] for c in checks}))

        non_meaning = result["action_consequence_non_meaning"]
        for key in (
            "action_authorized",
            "consequence_created",
            "operation_executed",
            "output_emitted",
            "output_treated_as_consequence",
            "evidence_treated_as_consequence",
            "standing_treated_as_consequence",
            "receipt_treated_as_consequence",
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
        self.assertTrue(non_claims["action_consequence_boundary_recorded"])
        for key in (
            "action_authorized",
            "consequence_created",
            "operation_executed",
            "output_emitted",
        ):
            self.assertFalse(non_claims[key], key)

        summary = resolver.build_distributed_action_consequence_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(
            summary["action_consequence_request_id"],
            "action-consequence-request-001",
        )
        self.assertEqual(
            summary["selected_execution_emission_result_id"],
            "execution-emission-result-001",
        )
        self.assertEqual(
            summary["selected_execution_emission_result_outcome"],
            EXECUTION_OUTCOME_RECORDED,
        )
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "distributed_action_consequence_boundary_recorded",
            "selected_execution_emission_result_preserved",
            "selected_execution_emission_result_recorded",
            "selected_execution_emission_result_failed_check_count_zero",
            "selected_admission_transition_result_preserved",
            "selected_admitted_operation_context_preserved",
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
            "proposed_output_family_named_but_not_emitted",
            "output_family_is_not_consequence",
            "carrier_evidence_is_not_consequence",
            "standing_is_not_consequence",
            "receipt_is_not_consequence",
            "receipt_exhaustion_requirement_present",
            "action_consequence_separation_present",
            "action_consequence_scope_supported",
            "no_action_consequence_execution_emission",
            "no_output_evidence_standing_receipt_consequence",
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
            "action_consequence_scope_too_generic": True,
            "output_non_consequence_posture_not_explicit_enough": True,
            "action_consequence_cannot_yet_be_bounded_without_consequence_risk": True,
        }
        additional_result = resolve(additional_request)
        self.assertEqual(additional_result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertFalse(
            additional_result["non_claims"]["action_consequence_boundary_recorded"]
        )
        self.assertTrue(
            additional_result["selected_execution_emission_result"][
                "selected_execution_emission_result"
            ]
        )
        self.assertTrue(
            additional_result["additional_basis_required"][
                "additional_basis_required"
            ]
        )
        self.assertEqual(
            additional_result["additional_basis_required"][
                "additional_basis_context"
            ],
            additional_request["additional_basis_context"],
        )
        self.assertTrue(
            additional_result["additional_basis_required"][
                "missing_basis_not_scheduled"
            ]
        )
        self.assertTrue(
            additional_result["additional_basis_required"][
                "missing_basis_not_authorized"
            ]
        )
        self.assertTrue(
            additional_result["additional_basis_required"]["missing_basis_not_executed"]
        )
        self.assert_no_action_consequence_or_overcommit(
            additional_result["action_consequence_statement"]
        )

        not_ready_request = declared_request(requested_outcome=OUTCOME_NOT_READY)
        not_ready_request["not_ready_reason"] = (
            "Selected execution / emission context lacks sufficient action / "
            "consequence basis."
        )
        not_ready_result = resolve(not_ready_request)
        self.assertEqual(not_ready_result["outcome"], OUTCOME_NOT_READY)
        self.assertFalse(
            not_ready_result["non_claims"]["action_consequence_boundary_recorded"]
        )
        self.assertEqual(
            not_ready_result["action_consequence_statement"]["not_ready_reason"],
            not_ready_request["not_ready_reason"],
        )
        self.assertTrue(
            not_ready_result["selected_execution_emission_result"][
                "selected_execution_emission_result"
            ]
        )
        self.assert_no_action_consequence_or_overcommit(
            not_ready_result["action_consequence_statement"]
        )

        observed = {
            resolve(declared_request())["outcome"],
            additional_result["outcome"],
            not_ready_result["outcome"],
            resolve(None)["outcome"],
        }
        self.assertEqual(
            observed,
            {
                OUTCOME_RECORDED,
                OUTCOME_REQUIRES_ADDITIONAL,
                OUTCOME_NOT_READY,
                OUTCOME_BLOCKED,
            },
        )

    def test_request_builder_helper_records_valid_boundary(self) -> None:
        selected = selected_execution_emission_result()
        basis = action_consequence_basis(selected)
        request = resolver.build_declared_distributed_action_consequence_request(
            "builder-request-001",
            "What action / consequence boundary basis may be recognized?",
            selected,
            basis,
            list(SUPPORTED_SCOPE),
            selected_execution_emission_result_id="execution-emission-result-001",
            selected_execution_emission_result_outcome=EXECUTION_OUTCOME_RECORDED,
            proposed_action_posture={"action_posture_id": "action-builder"},
            proposed_consequence_posture={
                "consequence_posture_id": "consequence-builder"
            },
            additional_basis_context={"not_used_for_recorded": False},
            not_ready_reason="not used for recorded",
        )
        request.pop("additional_basis_context")
        request.pop("not_ready_reason")

        self.assertEqual(request["action_consequence_request_id"], "builder-request-001")
        self.assertEqual(
            request["action_consequence_question"],
            "What action / consequence boundary basis may be recognized?",
        )
        self.assertEqual(request["selected_execution_emission_result"], selected)
        self.assertEqual(request["action_consequence_basis"], basis)
        self.assertEqual(request["action_consequence_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(
            request["selected_execution_emission_result_id"],
            "execution-emission-result-001",
        )
        self.assertEqual(
            request["selected_execution_emission_result_outcome"],
            EXECUTION_OUTCOME_RECORDED,
        )
        self.assertEqual(
            request["proposed_action_posture"],
            {"action_posture_id": "action-builder"},
        )
        self.assertEqual(
            request["proposed_consequence_posture"],
            {"consequence_posture_id": "consequence-builder"},
        )
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve(request)
        self.assert_recorded_core(result)

    def test_path_based_selected_execution_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            selected_path = temp / "selected_execution_result.json"
            selected_path.write_text(
                json.dumps(selected_execution_emission_result()),
                encoding="utf-8",
            )

            request = declared_request()
            request.pop("selected_execution_emission_result")
            request["selected_execution_emission_result_path"] = str(selected_path)
            result = resolve(request)
            self.assert_recorded_core(result)
            selected = result["selected_execution_emission_result"]
            self.assertEqual(
                selected["selected_execution_emission_result_path"],
                str(selected_path),
            )
            self.assertEqual(
                selected["selected_execution_emission_result_id"],
                "execution-emission-result-001",
            )
            self.assertEqual(
                selected["selected_execution_emission_result_outcome"],
                EXECUTION_OUTCOME_RECORDED,
            )

            request_path = temp / "declared_action_consequence_request.json"
            request_path.write_text(json.dumps(declared_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_action_consequence_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_request())
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_action_consequence_question"][
                    "action_consequence_request_path"
                ],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_deduplicates(self) -> None:
        result = resolve(declared_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "result.json"
            written = resolver.write_distributed_action_consequence_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_ROOT",
                Path(temp_dir) / "default-root",
            ):
                first = resolver.write_distributed_action_consequence_result(result)
                second = resolver.write_distributed_action_consequence_result(result)
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, Path(temp_dir) / "default-root")
                self.assertEqual(second.parent, Path(temp_dir) / "default-root")
                self.assertIn("action-consequence-request-001", first.name)
                self.assertTrue(second.stem.endswith("_001"))
                self.assertNotIn(
                    "distributed_execution_emission_boundary",
                    str(first),
                )

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        original_request = copy.deepcopy(request)
        original_selected = copy.deepcopy(request["selected_execution_emission_result"])
        original_basis = copy.deepcopy(request["action_consequence_basis"])
        original_scope = copy.deepcopy(request["action_consequence_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_execution_emission_result"], original_selected)
        self.assertEqual(request["action_consequence_basis"], original_basis)
        self.assertEqual(request["action_consequence_scope"], original_scope)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            upstream_paths = []
            for name in (
                "selected_execution_emission.json",
                "selected_admission_transition.json",
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
            resolver.write_distributed_action_consequence_result(
                first, temp / "new" / "result.json"
            )
            after = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            self.assertEqual(before, after)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        blocked = declared_request(
            intent="BLOCK_DISTRIBUTED_ACTION_CONSEQUENCE_REVIEW"
        )
        result = resolve(blocked)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(
            block_code(result), "ACTION_CONSEQUENCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        )
        self.assertFalse(
            result["action_consequence_statement"][
                "distributed_action_consequence_boundary_recorded"
            ]
        )

        missing = resolve(None)
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing), "ACTION_CONSEQUENCE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_action_consequence_boundary(
            declared_action_consequence_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(malformed), "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            unreadable = resolver.resolve_distributed_action_consequence_boundary_from_path(
                temp / "missing.json"
            )
            self.assertEqual(
                block_code(unreadable), "DECLARED_ACTION_CONSEQUENCE_REQUEST_UNREADABLE"
            )

            bad_json = temp / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = resolver.resolve_distributed_action_consequence_boundary_from_path(
                bad_json
            )
            self.assertEqual(
                block_code(bad), "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED"
            )

            array_json = temp / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_distributed_action_consequence_boundary_from_path(
                    array_json
                )
            )
            self.assertEqual(
                block_code(array_result),
                "DECLARED_ACTION_CONSEQUENCE_REQUEST_MALFORMED",
            )

            request = declared_request()
            request.pop("selected_execution_emission_result")
            request["selected_execution_emission_result_path"] = str(
                temp / "missing-selected.json"
            )
            self.assertEqual(
                block_code(resolve(request)), "EXECUTION_EMISSION_RESULT_UNREADABLE"
            )

            malformed_selected_path = temp / "malformed-selected.json"
            malformed_selected_path.write_text("{bad", encoding="utf-8")
            request["selected_execution_emission_result_path"] = str(
                malformed_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "EXECUTION_EMISSION_RESULT_MALFORMED"
            )

            array_selected_path = temp / "array-selected.json"
            array_selected_path.write_text("[]", encoding="utf-8")
            request["selected_execution_emission_result_path"] = str(
                array_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "EXECUTION_EMISSION_RESULT_MALFORMED"
            )

    def test_selected_execution_result_issue_blocks(self) -> None:
        cases = (
            (("outcome",), None, "EXECUTION_EMISSION_RESULT_OUTCOME_MISSING"),
            (
                ("outcome",),
                "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_NOT_READY",
                "EXECUTION_EMISSION_RESULT_NOT_RECORDED",
            ),
            (
                ("execution_emission_statement", "failed_check_count"),
                1,
                "EXECUTION_EMISSION_RESULT_HAS_FAILED_CHECKS",
            ),
            (
                ("execution_emission_statement", "operation_admitted"),
                False,
                "OPERATION_NOT_ADMITTED",
            ),
            (
                ("execution_emission_statement", "one_bounded_operation_context_admitted"),
                False,
                "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
            ),
        )
        for path, value, expected_code in cases:
            selected = selected_execution_emission_result()
            if value is None:
                delete_path(selected, path)
                delete_path(selected, ("distributed_execution_emission_summary", "outcome"))
            else:
                set_path(selected, path, value)
                if path[-1] == "outcome":
                    selected["distributed_execution_emission_summary"]["outcome"] = value
                if path[-1] == "failed_check_count":
                    selected["distributed_execution_emission_summary"][
                        "failed_check_count"
                    ] = value
                if path[-1] in (
                    "operation_admitted",
                    "one_bounded_operation_context_admitted",
                ):
                    selected["distributed_execution_emission_summary"][
                        path[-1]
                    ] = value
                    selected["non_claims"][path[-1]] = value
            result = resolve(declared_request(selected_execution=selected))
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code, expected_code)

    def test_missing_required_basis_blocks(self) -> None:
        missing_cases = (
            (
                "selected_admission_transition_result",
                "ADMISSION_TRANSITION_RESULT_MISSING",
            ),
            ("selected_operation_context", "ADMITTED_OPERATION_CONTEXT_MISSING"),
            ("selected_refusal_abort_result", "REFUSAL_ABORT_RESULT_MISSING"),
            ("selected_sync_non_sync_result", "SYNC_NON_SYNC_RESULT_MISSING"),
            ("selected_carrier_role_result", "CARRIER_ROLE_RESULT_MISSING"),
            (
                "selected_source_body_authority_result",
                "SOURCE_BODY_AUTHORITY_RESULT_MISSING",
            ),
            ("selected_eligibility_result", "SELECTED_ELIGIBILITY_RESULT_MISSING"),
            ("selected_matter_declaration", "SELECTED_MATTER_DECLARATION_MISSING"),
            ("selected_operation_candidate", "SELECTED_OPERATION_CANDIDATE_MISSING"),
            ("selected_operation_matter", "SELECTED_OPERATION_MATTER_MISSING"),
        )
        for key, expected_code in missing_cases:
            request = declared_request()
            if key == "selected_operation_context":
                selected = request["selected_execution_emission_result"]
                assert isinstance(selected, dict)
                selected["selected_operation_context"] = {}
                execution_basis = selected["execution_emission_basis"]
                assert isinstance(execution_basis, dict)
                execution_basis.pop("selected_admitted_operation_context", None)
                request["action_consequence_basis"].pop(key, None)
            else:
                remove_basis_everywhere(request, key)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

        request_missing_cases = (
            ("proposed_output_family", "PROPOSED_OUTPUT_FAMILY_MISSING"),
            (
                "receipt_exhaustion_requirement",
                "RECEIPT_EXHAUSTION_REQUIREMENT_MISSING",
            ),
            (
                "action_consequence_separation_requirement",
                "ACTION_CONSEQUENCE_SEPARATION_REQUIREMENT_MISSING",
            ),
        )
        for key, expected_code in request_missing_cases:
            request = declared_request()
            request.pop(key, None)
            request["action_consequence_basis"].pop(key, None)
            selected = request["selected_execution_emission_result"]
            assert isinstance(selected, dict)
            selected_context = selected["selected_operation_context"]
            assert isinstance(selected_context, dict)
            selected_context.pop(key, None)
            execution_basis = selected["execution_emission_basis"]
            assert isinstance(execution_basis, dict)
            execution_basis.pop(key, None)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

        request = declared_request()
        request.pop("action_consequence_scope")
        self.assertEqual(block_code(resolve(request)), "ACTION_CONSEQUENCE_SCOPE_MISSING")

    def test_unsupported_action_consequence_scope_blocks(self) -> None:
        request = declared_request()
        request["action_consequence_scope"] = list(SUPPORTED_SCOPE) + [
            "UNSUPPORTED_SCOPE"
        ]
        result = resolve(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_ACTION_CONSEQUENCE_SCOPE")

    def test_action_consequence_collapse_flags_block(self) -> None:
        cases = (
            ("action_authorized", "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "ACTION_CONSEQUENCE_REVIEW_CREATES_CONSEQUENCE"),
            ("operation_executed", "ACTION_CONSEQUENCE_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "ACTION_CONSEQUENCE_REVIEW_EMITS_OUTPUT"),
            (
                "output_treated_as_consequence",
                "ACTION_CONSEQUENCE_REVIEW_TREATS_OUTPUT_AS_CONSEQUENCE",
            ),
            (
                "evidence_treated_as_consequence",
                "ACTION_CONSEQUENCE_REVIEW_TREATS_EVIDENCE_AS_CONSEQUENCE",
            ),
            (
                "standing_treated_as_consequence",
                "ACTION_CONSEQUENCE_REVIEW_TREATS_STANDING_AS_CONSEQUENCE",
            ),
            (
                "receipt_treated_as_consequence",
                "ACTION_CONSEQUENCE_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE",
            ),
            (
                "repository_synchronization_authorized",
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_SYNCHRONIZATION",
            ),
            (
                "non_synchronized_operation_authorized",
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
            ),
            (
                "full_body_transfer_authorized",
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "ACTION_CONSEQUENCE_REVIEW_CREATES_SECOND_BODY"),
            (
                "public_launch_readiness_created",
                "ACTION_CONSEQUENCE_REVIEW_CREATES_PUBLIC_READINESS",
            ),
            (
                "final_completion_claimed",
                "ACTION_CONSEQUENCE_REVIEW_CLAIMS_FINAL_COMPLETION",
            ),
            (
                "follow_on_work_authorized",
                "ACTION_CONSEQUENCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            ),
            (
                "reusable_permission_created",
                "ACTION_CONSEQUENCE_REVIEW_CREATES_REUSABLE_PERMISSION",
            ),
            (
                "autonomous_continuation_authorized",
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            ),
            (
                "refusal_abort_erased",
                "ACTION_CONSEQUENCE_REVIEW_ERASES_REFUSAL_ABORT",
            ),
            (
                "evidence_erased",
                "ACTION_CONSEQUENCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
            ),
            ("divergence_resolved", "ACTION_CONSEQUENCE_REVIEW_RESOLVES_DIVERGENCE"),
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
        flipped_claim["declared_non_claims"]["action_authorized"] = True
        flipped_result = resolve(flipped_claim)
        self.assertEqual(flipped_result["outcome"], OUTCOME_BLOCKED)
        self.assertIn(
            block_code(flipped_result),
            {
                "NON_CLAIM_MISSING_OR_FLIPPED",
                "ACTION_CONSEQUENCE_REVIEW_AUTHORIZES_ACTION",
            },
        )


if __name__ == "__main__":
    unittest.main()
