"""Bounded tests for distributed operation receipt / exhaustion boundary.

These tests prove that the resolver records boundary-chain receipt /
exhaustion accounting only. They do not claim actual operation receipt,
execution receipt, output receipt, action receipt, consequence receipt,
conformance, closure, public readiness, final completion, reusable permission,
autonomous continuation, action, consequence, execution, emission,
synchronization, full body transfer, second body, or follow-on work.
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

import resolve_distributed_operation_receipt_exhaustion_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_RECORDED"
OUTCOME_NOT_READY = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_NOT_READY"
OUTCOME_REQUIRES_ADDITIONAL = (
    "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REVIEW_BLOCKED"
ACTION_OUTCOME_RECORDED = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
EXECUTION_OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_RECEIPT_EXHAUSTION_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_receipt_exhaustion_metadata",
    "declared_receipt_exhaustion_question",
    "selected_action_consequence_result",
    "selected_operation_context",
    "receipt_exhaustion_basis",
    "receipt_exhaustion_scope",
    "receipt_exhaustion_checks",
    "receipt_exhaustion_statement",
    "receipt_exhaustion_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_receipt_exhaustion_summary",
)

FALSE_RECEIPT_EXHAUSTION_KEYS = (
    "actual_operation_receipt_recorded",
    "execution_receipt_recorded",
    "output_receipt_recorded",
    "action_receipt_recorded",
    "consequence_receipt_recorded",
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
    "receipt_treated_as_consequence",
    "conformance_claimed",
    "closure_claimed",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "reusable_permission_created",
    "autonomous_continuation_authorized",
    "repository_synchronization_authorized",
    "shared_live_state_created",
    "state_merge_authorized",
    "replay_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "non_synchronized_operation_authorized",
    "carrier_autonomy_authorized",
    "stale_carrier_operation_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)


def false_non_claims(*, boundary_recorded: bool = True) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["receipt_exhaustion_boundary_recorded"] = boundary_recorded
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
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "one_bounded_operation_context_only": True,
        "action_consequence_boundary_recorded": True,
        "receipt_exhaustion_accounting_only": True,
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
            "What receipt / exhaustion boundary accounting may be recognized?"
        ),
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": (
            "What receipt / exhaustion boundary accounting may be recognized?"
        ),
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


def conformance_dependency() -> dict[str, object]:
    return {
        "conformance_remains_future_work": True,
        "conformance_requires_separate_boundary": True,
        "conformance_claimed": False,
    }


def closure_dependency() -> dict[str, object]:
    return {
        "closure_remains_future_work": True,
        "closure_requires_separate_boundary": True,
        "closure_claimed": False,
    }


def selected_execution_emission_result() -> dict[str, object]:
    return {
        "distributed_execution_emission_metadata": {
            "distributed_execution_emission_result_id": "execution-emission-result-001",
        },
        "outcome": EXECUTION_OUTCOME_RECORDED,
        "execution_emission_statement": {
            "failed_check_count": 0,
            "distributed_execution_emission_boundary_recorded": True,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
            "operation_executed": False,
            "output_emitted": False,
            "action_authorized": False,
            "consequence_created": False,
        },
    }


def selected_operation_context_for_action(
    selected_execution: dict[str, object],
) -> dict[str, object]:
    return {
        "selected_execution_emission_result": selected_execution,
        "selected_admission_transition_result": selected_admission_transition_result(),
        "selected_admitted_operation_context": admitted_operation_context(),
        "selected_refusal_abort_result": selected_refusal_abort_result(),
        "selected_sync_non_sync_result": selected_sync_non_sync_result(),
        "selected_carrier_role_result": selected_carrier_role_result(),
        "selected_source_body_authority_result": selected_source_body_authority_result(),
        "selected_eligibility_result": selected_eligibility_result(),
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": selected_operation_candidate(),
        "selected_operation_matter": selected_operation_matter(),
        "selected_action_consequence_scope": [
            "NO_ACTION_AUTHORIZED_BY_BOUNDARY",
            "NO_CONSEQUENCE_CREATED_BY_BOUNDARY",
            "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
            "CONFORMANCE_REQUIRED_BEFORE_CLOSURE",
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
        ],
        "proposed_output_family": proposed_output_family(),
        "receipt_exhaustion_requirement": receipt_exhaustion_requirement(),
        "action_consequence_separation_requirement": (
            action_consequence_separation_requirement()
        ),
        "conformance_dependency": conformance_dependency(),
        "closure_dependency": closure_dependency(),
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "action_consequence_boundary_recorded": True,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
    }


def action_consequence_basis(
    selected_execution: dict[str, object],
    context: dict[str, object],
) -> dict[str, object]:
    return {
        "selected_execution_emission_result": selected_execution,
        "selected_admission_transition_result": context[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": context["selected_admitted_operation_context"],
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
        "selected_action_consequence_scope": context[
            "selected_action_consequence_scope"
        ],
        "proposed_output_family": context["proposed_output_family"],
        "receipt_exhaustion_requirement": context["receipt_exhaustion_requirement"],
        "action_consequence_separation_requirement": context[
            "action_consequence_separation_requirement"
        ],
        "conformance_dependency": context["conformance_dependency"],
        "closure_dependency": context["closure_dependency"],
        "output_family_is_not_consequence": True,
        "carrier_evidence_is_not_consequence": True,
        "standing_is_not_consequence": True,
        "receipt_is_not_consequence": True,
    }


def action_consequence_statement() -> dict[str, object]:
    statement = {
        "failed_check_count": 0,
        "distributed_action_consequence_boundary_recorded": True,
        "action_consequence_boundary_recorded": True,
        "selected_execution_emission_result_preserved": True,
        "selected_admission_transition_result_preserved": True,
        "selected_admitted_operation_context_preserved": True,
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
        "receipt_exhaustion_requirement_present": True,
        "action_consequence_separation_present": True,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
        "output_treated_as_consequence": False,
        "evidence_treated_as_consequence": False,
        "standing_treated_as_consequence": False,
        "receipt_treated_as_consequence": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }
    return statement


def selected_action_consequence_result(
    selected_execution: dict[str, object] | None = None,
) -> dict[str, object]:
    selected = selected_execution or selected_execution_emission_result()
    context = selected_operation_context_for_action(selected)
    basis = action_consequence_basis(selected, context)
    return {
        "distributed_action_consequence_metadata": {
            "distributed_action_consequence_result_id": (
                "action-consequence-result-001"
            ),
            "distributed_action_consequence_result_version": "0.1.0",
        },
        "outcome": ACTION_OUTCOME_RECORDED,
        "selected_operation_context": context,
        "action_consequence_basis": basis,
        "action_consequence_statement": action_consequence_statement(),
        "distributed_action_consequence_summary": {
            "outcome": ACTION_OUTCOME_RECORDED,
            "failed_check_count": 0,
            "distributed_action_consequence_boundary_recorded": True,
            "selected_execution_emission_result_preserved": True,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
            "action_consequence_boundary_preserved": True,
            "action_authorized": False,
            "consequence_created": False,
            "operation_executed": False,
            "output_emitted": False,
            "output_treated_as_consequence": False,
            "evidence_treated_as_consequence": False,
            "standing_treated_as_consequence": False,
            "receipt_treated_as_consequence": False,
        },
        "non_claims": {
            "action_authorized": False,
            "consequence_created": False,
            "operation_executed": False,
            "output_emitted": False,
            "output_treated_as_consequence": False,
            "evidence_treated_as_consequence": False,
            "standing_treated_as_consequence": False,
            "receipt_treated_as_consequence": False,
            "public_launch_readiness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
            "reusable_permission_created": False,
            "autonomous_continuation_authorized": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
        },
    }


def receipt_exhaustion_basis(
    selected_action: dict[str, object] | None = None,
) -> dict[str, object]:
    selected = selected_action or selected_action_consequence_result()
    action_basis = selected["action_consequence_basis"]
    assert isinstance(action_basis, dict)
    return {
        "selected_action_consequence_result": selected,
        "selected_execution_emission_result": action_basis[
            "selected_execution_emission_result"
        ],
        "selected_admission_transition_result": action_basis[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": action_basis["selected_operation_context"],
        "selected_refusal_abort_result": action_basis["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": action_basis["selected_sync_non_sync_result"],
        "selected_carrier_role_result": action_basis["selected_carrier_role_result"],
        "selected_source_body_authority_result": action_basis[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": action_basis["selected_eligibility_result"],
        "selected_matter_declaration": action_basis["selected_matter_declaration"],
        "selected_operation_candidate": action_basis["selected_operation_candidate"],
        "selected_operation_matter": action_basis["selected_operation_matter"],
        "selected_action_consequence_scope": action_basis[
            "selected_action_consequence_scope"
        ],
        "proposed_output_family": action_basis["proposed_output_family"],
        "receipt_exhaustion_requirement": action_basis[
            "receipt_exhaustion_requirement"
        ],
        "action_consequence_separation_requirement": action_basis[
            "action_consequence_separation_requirement"
        ],
        "conformance_dependency": action_basis["conformance_dependency"],
        "closure_dependency": action_basis["closure_dependency"],
        "unperformed_non_consequential_posture": {
            "operation_executed": False,
            "output_emitted": False,
            "action_authorized": False,
            "consequence_created": False,
        },
        "exhaustion_accounting_posture": {
            "boundary_chain_receipt_only": True,
            "no_reusable_permission_remains": True,
            "future_execution_requires_fresh_receipt_exhaustion": True,
        },
        "declared_receipt_exhaustion_scope": list(SUPPORTED_SCOPE),
    }


def declared_request(
    *,
    selected_action: dict[str, object] | None = None,
    requested_outcome: str = OUTCOME_RECORDED,
    intent: str = "RECORD_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY",
) -> dict[str, object]:
    selected = selected_action or selected_action_consequence_result()
    boundary_recorded = requested_outcome == OUTCOME_RECORDED
    return {
        "receipt_exhaustion_request_id": "receipt-exhaustion-request-001",
        "receipt_exhaustion_question": (
            "What receipt / exhaustion boundary accounting may be recognized "
            "for the distributed operation boundary chain?"
        ),
        "receipt_exhaustion_intent": intent,
        "selected_action_consequence_result": selected,
        "selected_action_consequence_result_id": "action-consequence-result-001",
        "selected_action_consequence_result_outcome": ACTION_OUTCOME_RECORDED,
        "requested_receipt_exhaustion_outcome": requested_outcome,
        "receipt_exhaustion_basis": receipt_exhaustion_basis(selected),
        "receipt_exhaustion_scope": list(SUPPORTED_SCOPE),
        "conformance_dependency": conformance_dependency(),
        "closure_dependency": closure_dependency(),
        "declared_non_claims": false_non_claims(
            boundary_recorded=boundary_recorded
        ),
    }


def resolve(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_distributed_operation_receipt_exhaustion_boundary(
        declared_receipt_exhaustion_request=request
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


def remove_selected_basis_everywhere(
    request: dict[str, object],
    key: str,
    *,
    context_key: str | None = None,
) -> None:
    basis = request["receipt_exhaustion_basis"]
    assert isinstance(basis, dict)
    basis.pop(key, None)
    selected = request["selected_action_consequence_result"]
    assert isinstance(selected, dict)
    action_basis = selected.get("action_consequence_basis")
    if isinstance(action_basis, dict):
        action_basis.pop(key, None)
    selected_context = selected.get("selected_operation_context")
    if isinstance(selected_context, dict):
        selected_context.pop(context_key or key, None)


class DistributedOperationReceiptExhaustionBoundaryTests(unittest.TestCase):
    def assert_no_receipt_conformance_closure_or_overcommit(
        self, section: dict[str, object]
    ) -> None:
        for key in FALSE_RECEIPT_EXHAUSTION_KEYS:
            self.assertIs(section[key], False, key)

    def assert_recorded_core(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        statement = result["receipt_exhaustion_statement"]
        self.assertTrue(
            statement["distributed_operation_receipt_exhaustion_boundary_recorded"]
        )
        self.assertTrue(statement["receipt_exhaustion_boundary_recorded"])
        self.assertEqual(statement["failed_check_count"], 0)
        for key in (
            "selected_action_consequence_result_preserved",
            "selected_action_consequence_result_recorded",
            "selected_action_consequence_result_failed_check_count_zero",
            "selected_execution_emission_result_preserved",
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
            "action_consequence_boundary_preserved",
            "receipt_exhaustion_requirement_present",
            "conformance_dependency_present",
            "closure_dependency_present",
            "receipt_exhaustion_scope_supported",
            "boundary_chain_receipt_only",
        ):
            self.assertTrue(statement[key], key)
        self.assertFalse(statement["action_authorized"])
        self.assertFalse(statement["consequence_created"])
        self.assertFalse(statement["operation_executed"])
        self.assertFalse(statement["output_emitted"])
        self.assertFalse(statement["output_treated_as_consequence"])
        self.assertFalse(statement["evidence_treated_as_consequence"])
        self.assertFalse(statement["standing_treated_as_consequence"])
        self.assertFalse(statement["receipt_treated_as_consequence"])
        self.assertFalse(statement["actual_operation_receipt_recorded"])
        self.assertFalse(statement["execution_receipt_recorded"])
        self.assertFalse(statement["output_receipt_recorded"])
        self.assertFalse(statement["action_receipt_recorded"])
        self.assertFalse(statement["consequence_receipt_recorded"])
        self.assertFalse(statement["conformance_claimed"])
        self.assertFalse(statement["closure_claimed"])
        self.assertFalse(statement["public_launch_readiness_created"])
        self.assertFalse(statement["final_completion_claimed"])
        self.assertFalse(statement["follow_on_work_authorized"])
        self.assertFalse(statement["reusable_permission_created"])
        self.assertFalse(statement["autonomous_continuation_authorized"])

    def test_boundary_recorded_result_shape_and_core_posture(self) -> None:
        request = declared_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_core(result)

        metadata = result["distributed_receipt_exhaustion_metadata"]
        for key in (
            "distributed_receipt_exhaustion_result_id",
            "distributed_receipt_exhaustion_result_type",
            "distributed_receipt_exhaustion_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["distributed_receipt_exhaustion_result_version"], "0.1.0"
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_operation_receipt_exhaustion_boundary",
        )

        declared = result["declared_receipt_exhaustion_question"]
        self.assertEqual(
            declared["receipt_exhaustion_request_id"],
            request["receipt_exhaustion_request_id"],
        )
        self.assertEqual(
            declared["receipt_exhaustion_question"],
            request["receipt_exhaustion_question"],
        )
        self.assertEqual(
            declared["receipt_exhaustion_intent"],
            request["receipt_exhaustion_intent"],
        )
        self.assertEqual(
            declared["selected_action_consequence_result_id"],
            "action-consequence-result-001",
        )
        self.assertEqual(
            declared["selected_action_consequence_result_outcome"],
            ACTION_OUTCOME_RECORDED,
        )
        for key in (
            "receipt_exhaustion_boundary_is_not_actual_receipt",
            "receipt_exhaustion_boundary_is_not_conformance",
            "receipt_exhaustion_boundary_is_not_closure",
            "receipt_exhaustion_boundary_is_not_public_readiness",
            "receipt_exhaustion_boundary_is_not_final_completion",
        ):
            self.assertTrue(declared[key], key)

        selected = result["selected_action_consequence_result"]
        self.assertEqual(
            selected["selected_action_consequence_result_id"],
            "action-consequence-result-001",
        )
        self.assertEqual(
            selected["selected_action_consequence_result_outcome"],
            ACTION_OUTCOME_RECORDED,
        )
        self.assertTrue(selected["selected_action_consequence_result_recorded"])
        self.assertTrue(
            selected["selected_action_consequence_result_failed_check_count_zero"]
        )
        self.assertTrue(selected["selected_action_consequence_boundary_preserved"])
        for key in (
            "selected_action_consequence_result_did_not_authorize_action",
            "selected_action_consequence_result_did_not_create_consequence",
            "selected_action_consequence_result_did_not_execute_operation",
            "selected_action_consequence_result_did_not_emit_output",
        ):
            self.assertTrue(selected[key], key)
        preserved_statement = selected["selected_action_consequence_result"][
            "action_consequence_statement"
        ]
        for key in (
            "output_treated_as_consequence",
            "evidence_treated_as_consequence",
            "standing_treated_as_consequence",
            "receipt_treated_as_consequence",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(preserved_statement[key], False, key)

        context = result["selected_operation_context"]
        for key in (
            "selected_action_consequence_result",
            "selected_execution_emission_result",
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
        ):
            self.assertIn(key, context)
            self.assertTrue(context[key], key)
        self.assertTrue(context["operation_admitted"])
        self.assertTrue(context["one_bounded_operation_context_admitted"])
        self.assertTrue(context["action_consequence_boundary_recorded"])
        for key in (
            "action_authorized",
            "consequence_created",
            "operation_executed",
            "output_emitted",
            "actual_operation_receipt_recorded",
            "conformance_claimed",
            "closure_claimed",
        ):
            self.assertIs(context[key], False, key)

        basis = result["receipt_exhaustion_basis"]
        for key in (
            "selected_action_consequence_result",
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
            "selected_action_consequence_scope",
            "proposed_output_family",
            "receipt_exhaustion_requirement",
            "action_consequence_separation_requirement",
            "conformance_dependency",
            "closure_dependency",
            "unperformed_non_consequential_posture",
            "exhaustion_accounting_posture",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "boundary_chain_receipt_only",
            "no_actual_operation_receipt",
            "no_execution_receipt",
            "no_output_receipt",
            "no_action_receipt",
            "no_consequence_receipt",
            "no_conformance_claim",
            "no_closure_claim",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "no_reusable_permission_remains",
            "no_autonomous_continuation_authorized",
            "future_execution_requires_fresh_receipt_exhaustion",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(basis[key], key)

    def test_scope_checks_non_meaning_open_items_non_claims_and_summary(self) -> None:
        result = resolve(declared_request())
        scope = result["receipt_exhaustion_scope"]

        self.assertEqual(scope["selected_receipt_exhaustion_scope"], list(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_receipt_exhaustion_scope_supported"])
        for key in (
            "boundary_chain_receipt_only",
            "no_actual_operation_receipt",
            "no_execution_receipt",
            "no_output_receipt",
            "no_action_receipt",
            "no_consequence_receipt",
            "no_conformance_claim",
            "no_closure_claim",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "no_reusable_permission_remains",
            "no_autonomous_continuation_authorized",
            "future_execution_requires_fresh_receipt_exhaustion",
            "conformance_requires_separate_boundary",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(scope[key], key)

        checks = result["receipt_exhaustion_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        expected_check_names = {
            "receipt / exhaustion question declared",
            "receipt / exhaustion intent supported",
            "selected action / consequence result present",
            "selected action / consequence result outcome declared",
            "selected action / consequence result outcome recorded",
            "selected action / consequence result failed check count zero",
            "selected execution / emission result preserved",
            "selected admission / transition result preserved",
            "selected admitted operation context preserved",
            "operation admitted true",
            "one bounded operation context admitted true",
            "selected refusal / abort result preserved",
            "selected sync/non-sync result preserved",
            "selected carrier role result preserved",
            "selected source-body authority result preserved",
            "selected eligibility result preserved",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "action / consequence boundary preserved",
            "action unauthorized",
            "consequence uncreated",
            "operation unexecuted",
            "output un-emitted",
            "output / evidence / standing / receipt non-consequence",
            "receipt / exhaustion requirement present",
            "conformance dependency present",
            "closure dependency present",
            "receipt / exhaustion scope supported",
            "no actual operation receipt claimed",
            "no execution receipt claimed",
            "no output receipt claimed",
            "no action receipt claimed",
            "no consequence receipt claimed",
            "no conformance claimed",
            "no closure claimed",
            "no public readiness / final completion / follow-on work claimed",
            "no reusable permission created",
            "no autonomous continuation authorized",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_check_names.issubset({c["check_name"] for c in checks}))

        non_meaning = result["receipt_exhaustion_non_meaning"]
        for key in (
            "actual_operation_receipt_recorded",
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
            "execution_receipt_recorded",
            "output_receipt_recorded",
            "action_receipt_recorded",
            "consequence_receipt_recorded",
            "receipt_treated_as_consequence",
            "conformance_achieved",
            "closure_achieved",
            "public_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "reusable_permission_created",
            "autonomous_continuation_authorized",
            "repository_synchronization_authorized",
            "non_synchronized_operation_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "divergence_resolved",
            "evidence_erased",
            "refusal_erased",
            "blocked_attempt_erased",
            "projection_mismatch_hidden",
        ):
            self.assertTrue(non_meaning[key], key)

        open_items = result["what_remains_open"]
        for key in (
            "distributed_operation_conformance",
            "distributed_operation_closure",
            "distributed_operation_itself",
            "actual_operation_execution",
            "actual_output_emission",
            "action_authorization",
            "consequence_creation",
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
        self.assertTrue(non_claims["receipt_exhaustion_boundary_recorded"])
        for key in (
            "actual_operation_receipt_recorded",
            "execution_receipt_recorded",
            "output_receipt_recorded",
            "action_receipt_recorded",
            "consequence_receipt_recorded",
            "conformance_claimed",
            "closure_claimed",
        ):
            self.assertFalse(non_claims[key], key)

        summary = resolver.build_distributed_operation_receipt_exhaustion_summary(
            result
        )
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(
            summary["receipt_exhaustion_request_id"],
            "receipt-exhaustion-request-001",
        )
        self.assertEqual(
            summary["selected_action_consequence_result_id"],
            "action-consequence-result-001",
        )
        self.assertEqual(
            summary["selected_action_consequence_result_outcome"],
            ACTION_OUTCOME_RECORDED,
        )
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "receipt_exhaustion_boundary_recorded",
            "selected_action_consequence_result_preserved",
            "selected_action_consequence_result_recorded",
            "selected_action_consequence_result_failed_check_count_zero",
            "selected_execution_emission_result_preserved",
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
            "action_consequence_boundary_preserved",
            "action_unauthorized",
            "consequence_uncreated",
            "operation_unexecuted",
            "output_un_emitted",
            "output_evidence_standing_receipt_non_consequence",
            "receipt_exhaustion_requirement_present",
            "conformance_dependency_present",
            "closure_dependency_present",
            "receipt_exhaustion_scope_supported",
            "boundary_chain_receipt_only",
            "no_actual_operation_receipt_execution_receipt_output_receipt_action_receipt_consequence_receipt",
            "no_conformance_closure",
            "no_public_readiness_final_completion_follow_on_work",
            "no_reusable_permission_autonomous_continuation",
        ):
            self.assertTrue(summary[key], key)

    def test_requires_additional_basis_and_not_ready_outcomes(self) -> None:
        additional_request = declared_request(
            requested_outcome=OUTCOME_REQUIRES_ADDITIONAL
        )
        additional_request["additional_basis_context"] = {
            "reason": "Receipt / exhaustion cannot yet be bounded without closure risk.",
            "missing_basis": [
                "boundary-chain receipt posture too generic",
                "non-reusable permission posture not explicit enough",
            ],
        }
        additional_result = resolve(additional_request)
        self.assertEqual(additional_result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertFalse(
            additional_result["non_claims"]["receipt_exhaustion_boundary_recorded"]
        )
        self.assertTrue(
            additional_result["selected_action_consequence_result"][
                "selected_action_consequence_result"
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
        for key in (
            "additional_basis_scheduled",
            "additional_basis_authorized",
            "additional_basis_executed",
            "additional_basis_creates_reusable_permission",
            "additional_basis_authorizes_autonomous_continuation",
            "additional_basis_creates_public_readiness",
            "additional_basis_claims_final_completion",
            "additional_basis_schedules_follow_on_work",
        ):
            self.assertFalse(additional_result["additional_basis_required"][key], key)
        self.assert_no_receipt_conformance_closure_or_overcommit(
            additional_result["receipt_exhaustion_statement"]
        )

        not_ready_request = declared_request(requested_outcome=OUTCOME_NOT_READY)
        not_ready_request["not_ready_reason"] = (
            "Selected action / consequence context lacks sufficient receipt / "
            "exhaustion basis."
        )
        not_ready_result = resolve(not_ready_request)
        self.assertEqual(not_ready_result["outcome"], OUTCOME_NOT_READY)
        self.assertFalse(
            not_ready_result["non_claims"]["receipt_exhaustion_boundary_recorded"]
        )
        self.assertEqual(
            not_ready_result["receipt_exhaustion_statement"]["not_ready_reason"],
            not_ready_request["not_ready_reason"],
        )
        self.assertTrue(
            not_ready_result["selected_action_consequence_result"][
                "selected_action_consequence_result"
            ]
        )
        self.assert_no_receipt_conformance_closure_or_overcommit(
            not_ready_result["receipt_exhaustion_statement"]
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
        selected = selected_action_consequence_result()
        basis = receipt_exhaustion_basis(selected)
        request = (
            resolver.build_declared_distributed_operation_receipt_exhaustion_request(
                "builder-request-001",
                "What receipt / exhaustion boundary accounting may be recognized?",
                selected,
                basis,
                list(SUPPORTED_SCOPE),
                selected_action_consequence_result_id="action-consequence-result-001",
                selected_action_consequence_result_outcome=ACTION_OUTCOME_RECORDED,
                conformance_dependency={"conformance_dependency_id": "builder-conf"},
                closure_dependency={"closure_dependency_id": "builder-closure"},
                additional_basis_context={"not_used_for_recorded": False},
                not_ready_reason="not used for recorded",
            )
        )

        self.assertEqual(request["receipt_exhaustion_request_id"], "builder-request-001")
        self.assertEqual(
            request["receipt_exhaustion_question"],
            "What receipt / exhaustion boundary accounting may be recognized?",
        )
        self.assertEqual(request["selected_action_consequence_result"], selected)
        self.assertEqual(request["receipt_exhaustion_basis"], basis)
        self.assertEqual(request["receipt_exhaustion_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(
            request["selected_action_consequence_result_id"],
            "action-consequence-result-001",
        )
        self.assertEqual(
            request["selected_action_consequence_result_outcome"],
            ACTION_OUTCOME_RECORDED,
        )
        self.assertEqual(
            request["conformance_dependency"],
            {"conformance_dependency_id": "builder-conf"},
        )
        self.assertEqual(
            request["closure_dependency"],
            {"closure_dependency_id": "builder-closure"},
        )
        self.assertEqual(
            request["additional_basis_context"],
            {"not_used_for_recorded": False},
        )
        self.assertEqual(request["not_ready_reason"], "not used for recorded")
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve(request)
        self.assert_recorded_core(result)

    def test_path_based_selected_action_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            selected_path = temp / "selected_action_result.json"
            selected_path.write_text(
                json.dumps(selected_action_consequence_result()),
                encoding="utf-8",
            )

            request = declared_request()
            request.pop("selected_action_consequence_result")
            request["selected_action_consequence_result_path"] = str(selected_path)
            result = resolve(request)
            self.assert_recorded_core(result)
            selected = result["selected_action_consequence_result"]
            self.assertEqual(
                selected["selected_action_consequence_result_path"],
                str(selected_path),
            )
            self.assertEqual(
                selected["selected_action_consequence_result_id"],
                "action-consequence-result-001",
            )
            self.assertEqual(
                selected["selected_action_consequence_result_outcome"],
                ACTION_OUTCOME_RECORDED,
            )

            request_path = temp / "declared_receipt_exhaustion_request.json"
            request_path.write_text(json.dumps(declared_request()), encoding="utf-8")
            path_result = (
                resolver.resolve_distributed_operation_receipt_exhaustion_boundary_from_path(
                    request_path
                )
            )
            mapping_result = resolve(declared_request())
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_receipt_exhaustion_question"][
                    "receipt_exhaustion_request_path"
                ],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_deduplicates(self) -> None:
        result = resolve(declared_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "result.json"
            written = resolver.write_distributed_operation_receipt_exhaustion_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT",
                Path(temp_dir) / "default-root",
            ):
                first = resolver.write_distributed_operation_receipt_exhaustion_result(
                    result
                )
                second = resolver.write_distributed_operation_receipt_exhaustion_result(
                    result
                )
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, Path(temp_dir) / "default-root")
                self.assertEqual(second.parent, Path(temp_dir) / "default-root")
                self.assertIn("receipt-exhaustion-request-001", first.name)
                self.assertTrue(second.stem.endswith("_001"))
                self.assertNotIn("distributed_action_consequence_boundary", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        original_request = copy.deepcopy(request)
        original_selected = copy.deepcopy(request["selected_action_consequence_result"])
        original_basis = copy.deepcopy(request["receipt_exhaustion_basis"])
        original_scope = copy.deepcopy(request["receipt_exhaustion_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_action_consequence_result"], original_selected)
        self.assertEqual(request["receipt_exhaustion_basis"], original_basis)
        self.assertEqual(request["receipt_exhaustion_scope"], original_scope)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            upstream_paths = []
            for name in (
                "selected_action_consequence.json",
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
            resolver.write_distributed_operation_receipt_exhaustion_result(
                first, temp / "new" / "result.json"
            )
            after = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            self.assertEqual(before, after)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        blocked = declared_request(
            intent="BLOCK_DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_REVIEW"
        )
        result = resolve(blocked)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(
            block_code(result), "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        )
        self.assertFalse(
            result["receipt_exhaustion_statement"][
                "distributed_operation_receipt_exhaustion_boundary_recorded"
            ]
        )

        missing = resolve(None)
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing), "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_operation_receipt_exhaustion_boundary(
            declared_receipt_exhaustion_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(
            block_code(malformed), "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            unreadable = (
                resolver.resolve_distributed_operation_receipt_exhaustion_boundary_from_path(
                    temp / "missing.json"
                )
            )
            self.assertEqual(
                block_code(unreadable),
                "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE",
            )

            bad_json = temp / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = (
                resolver.resolve_distributed_operation_receipt_exhaustion_boundary_from_path(
                    bad_json
                )
            )
            self.assertEqual(
                block_code(bad), "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"
            )

            array_json = temp / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_distributed_operation_receipt_exhaustion_boundary_from_path(
                    array_json
                )
            )
            self.assertEqual(
                block_code(array_result),
                "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            )

            request = declared_request()
            request.pop("selected_action_consequence_result")
            request["selected_action_consequence_result_path"] = str(
                temp / "missing-selected.json"
            )
            self.assertEqual(
                block_code(resolve(request)), "ACTION_CONSEQUENCE_RESULT_UNREADABLE"
            )

            malformed_selected_path = temp / "malformed-selected.json"
            malformed_selected_path.write_text("{bad", encoding="utf-8")
            request["selected_action_consequence_result_path"] = str(
                malformed_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "ACTION_CONSEQUENCE_RESULT_MALFORMED"
            )

            array_selected_path = temp / "array-selected.json"
            array_selected_path.write_text("[]", encoding="utf-8")
            request["selected_action_consequence_result_path"] = str(
                array_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "ACTION_CONSEQUENCE_RESULT_MALFORMED"
            )

    def test_selected_action_result_issue_blocks(self) -> None:
        cases = (
            (("outcome",), None, "ACTION_CONSEQUENCE_RESULT_OUTCOME_MISSING"),
            (
                ("outcome",),
                "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_NOT_READY",
                "ACTION_CONSEQUENCE_RESULT_NOT_RECORDED",
            ),
            (
                ("action_consequence_statement", "failed_check_count"),
                1,
                "ACTION_CONSEQUENCE_RESULT_HAS_FAILED_CHECKS",
            ),
        )
        for path, value, expected_code in cases:
            selected = selected_action_consequence_result()
            if value is None:
                delete_path(selected, path)
                delete_path(selected, ("distributed_action_consequence_summary", "outcome"))
            else:
                set_path(selected, path, value)
                if path[-1] == "outcome":
                    selected["distributed_action_consequence_summary"]["outcome"] = value
                if path[-1] == "failed_check_count":
                    selected["distributed_action_consequence_summary"][
                        "failed_check_count"
                    ] = value
            request = declared_request(selected_action=selected)
            if value is None:
                request.pop("selected_action_consequence_result_outcome")
            elif path[-1] == "outcome":
                request["selected_action_consequence_result_outcome"] = value
            result = resolve(request)
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code, expected_code)

    def test_missing_required_basis_blocks(self) -> None:
        missing_cases = (
            ("selected_execution_emission_result", "EXECUTION_EMISSION_RESULT_MISSING"),
            (
                "selected_admission_transition_result",
                "ADMISSION_TRANSITION_RESULT_MISSING",
            ),
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
            remove_selected_basis_everywhere(request, key)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

        request = declared_request()
        selected = request["selected_action_consequence_result"]
        assert isinstance(selected, dict)
        selected["selected_operation_context"] = {}
        action_basis = selected["action_consequence_basis"]
        assert isinstance(action_basis, dict)
        action_basis.pop("selected_operation_context", None)
        receipt_basis = request["receipt_exhaustion_basis"]
        assert isinstance(receipt_basis, dict)
        receipt_basis.pop("selected_operation_context", None)
        self.assertEqual(
            block_code(resolve(request)), "ADMITTED_OPERATION_CONTEXT_MISSING"
        )

        for key, expected_code in (
            ("conformance_dependency", "CONFORMANCE_DEPENDENCY_MISSING"),
            ("closure_dependency", "CLOSURE_DEPENDENCY_MISSING"),
        ):
            request = declared_request()
            request.pop(key, None)
            request["receipt_exhaustion_basis"].pop(key, None)
            selected = request["selected_action_consequence_result"]
            assert isinstance(selected, dict)
            selected["action_consequence_basis"].pop(key, None)
            selected["selected_operation_context"].pop(key, None)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, expected_code)

        request = declared_request()
        request.pop("receipt_exhaustion_scope")
        request["receipt_exhaustion_basis"].pop("declared_receipt_exhaustion_scope")
        self.assertEqual(
            block_code(resolve(request)), "RECEIPT_EXHAUSTION_SCOPE_MISSING"
        )

    def test_operation_context_not_admitted_blocks(self) -> None:
        for field, expected_code in (
            ("operation_admitted", "OPERATION_NOT_ADMITTED"),
            (
                "one_bounded_operation_context_admitted",
                "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
            ),
        ):
            request = declared_request()
            selected = request["selected_action_consequence_result"]
            assert isinstance(selected, dict)
            selected["action_consequence_statement"][field] = False
            selected["distributed_action_consequence_summary"][field] = False
            selected_context = selected["selected_operation_context"]
            assert isinstance(selected_context, dict)
            admitted_context = selected_context["selected_admitted_operation_context"]
            assert isinstance(admitted_context, dict)
            admitted_context[field] = False
            if field == "one_bounded_operation_context_admitted":
                admitted_context["one_bounded_operation_context_only"] = False
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, field)

    def test_unsupported_receipt_exhaustion_scope_blocks(self) -> None:
        request = declared_request()
        request["receipt_exhaustion_scope"] = list(SUPPORTED_SCOPE) + [
            "UNSUPPORTED_SCOPE"
        ]
        result = resolve(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE")

    def test_receipt_exhaustion_collapse_flags_block(self) -> None:
        cases = (
            (
                "actual_operation_receipt_recorded",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
            ),
            (
                "execution_receipt_recorded",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_EXECUTION_RECEIPT",
            ),
            (
                "output_receipt_recorded",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_OUTPUT_RECEIPT",
            ),
            (
                "action_receipt_recorded",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_ACTION_RECEIPT",
            ),
            (
                "consequence_receipt_recorded",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONSEQUENCE_RECEIPT",
            ),
            (
                "conformance_claimed",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CONFORMANCE",
            ),
            ("closure_claimed", "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_CLOSURE"),
            (
                "receipt_treated_as_consequence",
                "RECEIPT_EXHAUSTION_REVIEW_TREATS_RECEIPT_AS_CONSEQUENCE",
            ),
            ("action_authorized", "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "RECEIPT_EXHAUSTION_REVIEW_CREATES_CONSEQUENCE"),
            ("operation_executed", "RECEIPT_EXHAUSTION_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "RECEIPT_EXHAUSTION_REVIEW_EMITS_OUTPUT"),
            (
                "repository_synchronization_authorized",
                "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_SYNCHRONIZATION",
            ),
            (
                "non_synchronized_operation_authorized",
                "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
            ),
            (
                "full_body_transfer_authorized",
                "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "RECEIPT_EXHAUSTION_REVIEW_CREATES_SECOND_BODY"),
            (
                "public_launch_readiness_created",
                "RECEIPT_EXHAUSTION_REVIEW_CREATES_PUBLIC_READINESS",
            ),
            (
                "final_completion_claimed",
                "RECEIPT_EXHAUSTION_REVIEW_CLAIMS_FINAL_COMPLETION",
            ),
            (
                "follow_on_work_authorized",
                "RECEIPT_EXHAUSTION_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            ),
            (
                "reusable_permission_created",
                "RECEIPT_EXHAUSTION_REVIEW_CREATES_REUSABLE_PERMISSION",
            ),
            (
                "autonomous_continuation_authorized",
                "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            ),
            (
                "refusal_abort_erased",
                "RECEIPT_EXHAUSTION_REVIEW_ERASES_REFUSAL_ABORT",
            ),
            (
                "evidence_erased",
                "RECEIPT_EXHAUSTION_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
            ),
            ("divergence_resolved", "RECEIPT_EXHAUSTION_REVIEW_RESOLVES_DIVERGENCE"),
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
                "RECEIPT_EXHAUSTION_REVIEW_AUTHORIZES_ACTION",
            },
        )


if __name__ == "__main__":
    unittest.main()
