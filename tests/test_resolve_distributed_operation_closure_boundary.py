"""Bounded tests for distributed operation closure boundary.

These tests prove that the resolver records boundary-chain closure only.
They do not claim executed-operation closure, executed-operation conformance,
actual operation receipt, public readiness, final completion, reusable
permission, autonomous continuation, action, consequence, execution, emission,
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

import resolve_distributed_operation_closure_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY_RECORDED"
OUTCOME_NOT_CLOSED = "DISTRIBUTED_OPERATION_CLOSURE_NOT_CLOSED"
OUTCOME_REQUIRES_ADDITIONAL = (
    "DISTRIBUTED_OPERATION_CLOSURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_CLOSURE_REVIEW_BLOCKED"
CONFORMANCE_OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_RECORDED"
RECEIPT_OUTCOME_RECORDED = (
    "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_RECORDED"
)
ACTION_OUTCOME_RECORDED = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
EXECUTION_OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_CLOSURE_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_operation_closure_metadata",
    "declared_closure_question",
    "selected_conformance_result",
    "selected_operation_context",
    "closure_basis",
    "closure_scope",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "additional_basis_required",
    "not_closed_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_operation_closure_summary",
)

FALSE_CLOSURE_KEYS = (
    "executed_operation_closure_claimed",
    "executed_operation_conformance_claimed",
    "actual_operation_receipt_recorded",
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "reusable_permission_created",
    "autonomous_continuation_authorized",
)


def false_non_claims(*, boundary_recorded: bool = True) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["boundary_chain_closure_recorded"] = boundary_recorded
    claims["distributed_operation_closure_boundary_recorded"] = boundary_recorded
    return claims


def conformance_false_non_claims() -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims.update(
        {
            "actual_operation_receipt_claimed": False,
            "execution_receipt_recorded": False,
            "output_receipt_recorded": False,
            "action_receipt_recorded": False,
            "consequence_receipt_recorded": False,
            "closure_claimed": False,
            "operation_closed": False,
            "closure_achieved": False,
            "boundary_chain_conformance_recorded": True,
            "distributed_operation_conformance_boundary_recorded": True,
        }
    )
    return claims


def selected_receipt_exhaustion_result() -> dict[str, object]:
    statement = {
        "failed_check_count": 0,
        "distributed_operation_receipt_exhaustion_boundary_recorded": True,
        "receipt_exhaustion_boundary_recorded": True,
        "receipt_exhaustion_boundary_preserved": True,
        "receipt_exhaustion_boundary_chain_accounting_only": True,
        "boundary_chain_receipt_only": True,
        "actual_operation_receipt_recorded": False,
        "execution_receipt_recorded": False,
        "output_receipt_recorded": False,
        "action_receipt_recorded": False,
        "consequence_receipt_recorded": False,
        "conformance_claimed": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }
    return {
        "distributed_receipt_exhaustion_metadata": {
            "distributed_receipt_exhaustion_result_id": (
                "receipt-exhaustion-result-001"
            ),
            "distributed_receipt_exhaustion_result_version": "0.1.0",
        },
        "outcome": RECEIPT_OUTCOME_RECORDED,
        "receipt_exhaustion_statement": copy.deepcopy(statement),
        "distributed_receipt_exhaustion_summary": {
            **copy.deepcopy(statement),
            "outcome": RECEIPT_OUTCOME_RECORDED,
        },
        "non_claims": {
            "receipt_exhaustion_boundary_recorded": True,
            "distributed_operation_receipt_exhaustion_boundary_recorded": True,
            **{
                key: False
                for key in (
                    "actual_operation_receipt_recorded",
                    "execution_receipt_recorded",
                    "output_receipt_recorded",
                    "action_receipt_recorded",
                    "consequence_receipt_recorded",
                    "conformance_claimed",
                    "closure_claimed",
                    "operation_executed",
                    "output_emitted",
                    "action_authorized",
                    "consequence_created",
                    "public_launch_readiness_created",
                    "final_completion_claimed",
                    "follow_on_work_authorized",
                    "reusable_permission_created",
                    "autonomous_continuation_authorized",
                )
            },
        },
    }


def selected_action_consequence_result() -> dict[str, object]:
    return {
        "distributed_action_consequence_metadata": {
            "distributed_action_consequence_result_id": (
                "action-consequence-result-001"
            ),
        },
        "outcome": ACTION_OUTCOME_RECORDED,
        "action_consequence_boundary_recorded": True,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
        "receipt_treated_as_consequence": False,
    }


def selected_execution_emission_result() -> dict[str, object]:
    return {
        "distributed_execution_emission_metadata": {
            "distributed_execution_emission_result_id": "execution-emission-result-001",
        },
        "outcome": EXECUTION_OUTCOME_RECORDED,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }


def selected_admission_transition_result() -> dict[str, object]:
    return {
        "distributed_operation_admission_transition_result_id": (
            "admission-transition-result-001"
        ),
        "outcome": "DISTRIBUTED_OPERATION_ADMISSION_TRANSITION_AUTHORITY_RECORDED",
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }


def admitted_operation_context() -> dict[str, object]:
    return {
        "operation_context_id": "admitted-operation-context-001",
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "one_bounded_operation_context_only": True,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
    }


def selected_refusal_abort_result() -> dict[str, object]:
    return {
        "distributed_refusal_abort_boundary_result_id": "refusal-abort-result-001",
        "outcome": "DISTRIBUTED_REFUSAL_ABORT_BOUNDARY_RECORDED",
        "refusal_abort_conditions_carry_forward": True,
        "live_operation_refused": False,
        "live_operation_aborted": False,
        "refusal_abort_erased": False,
    }


def selected_sync_non_sync_result() -> dict[str, object]:
    return {
        "distributed_sync_non_sync_boundary_result_id": "sync-non-sync-result-001",
        "outcome": "DISTRIBUTED_SYNC_NON_SYNC_BOUNDARY_RECORDED",
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
        "distributed_carrier_operational_role_result_id": "carrier-role-result-001",
        "outcome": "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED",
        "carrier_role_basis": {"carrier_context_remains_context_only": True},
        "carrier_role_activated_beyond_scope": False,
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
            "Can the recorded distributed operation boundary chain be closed?"
        ),
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": (
            "Can the recorded distributed operation boundary chain be closed?"
        ),
        "matter_remains_declaration_only": True,
    }


def conformance_scope() -> dict[str, object]:
    return {
        "selected_conformance_scope": [
            "BOUNDARY_CHAIN_CONFORMANCE_ONLY",
            "NO_EXECUTED_OPERATION_CONFORMANCE_CLAIM",
            "NO_ACTUAL_OPERATION_RECEIPT_CLAIM",
            "NO_CONFORMANCE_AS_CLOSURE",
            "NO_PUBLIC_READINESS_CLAIM",
            "NO_FINAL_COMPLETION_CLAIM",
            "NON_CLAIMS_MUST_REMAIN_FALSE",
            "BOUNDARY_SCOPES_MUST_REMAIN_BOUNDED",
            "NO_LAYER_OVERREAD_ALLOWED",
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
        ],
        "boundary_chain_conformance_only": True,
        "no_executed_operation_conformance_claim": True,
        "no_actual_operation_receipt_claim": True,
        "no_conformance_as_closure": True,
        "no_public_readiness_claim": True,
        "no_final_completion_claim": True,
        "non_claims_must_remain_false": True,
        "boundary_scopes_must_remain_bounded": True,
        "no_layer_overread_allowed": True,
        "closure_requires_separate_boundary": True,
    }


def selected_operation_context_for_conformance() -> dict[str, object]:
    return {
        "selected_receipt_exhaustion_result": selected_receipt_exhaustion_result(),
        "selected_action_consequence_result": selected_action_consequence_result(),
        "selected_execution_emission_result": selected_execution_emission_result(),
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
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "conformance_boundary_recorded": True,
        "boundary_chain_conformance_only": True,
        "executed_operation_closure_claimed": False,
        "executed_operation_conformance_claimed": False,
        "actual_operation_receipt_recorded": False,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
    }


def conformance_basis(
    context: dict[str, object] | None = None,
) -> dict[str, object]:
    selected_context = context or selected_operation_context_for_conformance()
    return {
        "selected_receipt_exhaustion_result": selected_context[
            "selected_receipt_exhaustion_result"
        ],
        "selected_action_consequence_result": selected_context[
            "selected_action_consequence_result"
        ],
        "selected_execution_emission_result": selected_context[
            "selected_execution_emission_result"
        ],
        "selected_admission_transition_result": selected_context[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": selected_context[
            "selected_admitted_operation_context"
        ],
        "selected_refusal_abort_result": selected_context["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": selected_context["selected_sync_non_sync_result"],
        "selected_carrier_role_result": selected_context["selected_carrier_role_result"],
        "selected_source_body_authority_result": selected_context[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": selected_context["selected_eligibility_result"],
        "selected_matter_declaration": selected_context["selected_matter_declaration"],
        "selected_operation_candidate": selected_context["selected_operation_candidate"],
        "selected_operation_matter": selected_context["selected_operation_matter"],
        "conformance_scope": conformance_scope(),
        "receipt_exhaustion_scope": ["BOUNDARY_CHAIN_RECEIPT_ONLY"],
        "action_consequence_scope": ["NO_ACTION_AUTHORIZED_BY_BOUNDARY"],
        "execution_emission_scope": ["NO_OPERATION_EXECUTION_BY_BOUNDARY"],
        "admission_scope": ["ONE_BOUNDED_OPERATION_CONTEXT_ONLY"],
        "boundary_chain_conformance_basis": {
            "boundary_chain_conformance_recorded": True,
            "boundary_chain_conformance_only": True,
        },
        "closure_dependency": {
            "closure_requires_separate_boundary": True,
            "closure_claimed": False,
        },
        "non_claim_preservation_basis": {"all_required_non_claims_false": True},
        "overread_prevention_basis": {"no_layer_overread_prior_layer": True},
        "scope_preservation_basis": {"boundary_scopes_remained_bounded": True},
        "prior_boundary_preservation_basis": {"prior_boundaries_preserved": True},
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "boundary_chain_conformance_recorded": True,
        "distributed_operation_conformance_boundary_recorded": True,
    }


def conformance_statement() -> dict[str, object]:
    return {
        "failed_check_count": 0,
        "distributed_operation_conformance_boundary_recorded": True,
        "boundary_chain_conformance_recorded": True,
        "selected_receipt_exhaustion_result_preserved": True,
        "selected_receipt_exhaustion_result_recorded": True,
        "selected_receipt_exhaustion_result_failed_check_count_zero": True,
        "selected_action_consequence_result_preserved": True,
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
        "conformance_boundary_preserved": True,
        "executed_operation_closure_claimed": False,
        "executed_operation_conformance_claimed": False,
        "actual_operation_receipt_recorded": False,
        "operation_executed": False,
        "output_emitted": False,
        "action_authorized": False,
        "consequence_created": False,
        "closure_claimed": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "reusable_permission_created": False,
        "autonomous_continuation_authorized": False,
        "all_required_prior_non_claims_preserved": True,
        "no_layer_overread_prior_layer": True,
        "boundary_scopes_remained_bounded": True,
        "closure_requires_separate_boundary": True,
    }


def selected_conformance_result() -> dict[str, object]:
    context = selected_operation_context_for_conformance()
    basis = conformance_basis(context)
    statement = conformance_statement()
    return {
        "distributed_operation_conformance_metadata": {
            "distributed_operation_conformance_result_id": "conformance-result-001",
            "distributed_operation_conformance_result_version": "0.1.0",
        },
        "outcome": CONFORMANCE_OUTCOME_RECORDED,
        "selected_receipt_exhaustion_result": {
            "selected_receipt_exhaustion_result_id": "receipt-exhaustion-result-001",
            "selected_receipt_exhaustion_result_outcome": RECEIPT_OUTCOME_RECORDED,
            "selected_receipt_exhaustion_result": context[
                "selected_receipt_exhaustion_result"
            ],
        },
        "selected_operation_context": context,
        "conformance_basis": basis,
        "conformance_scope": conformance_scope(),
        "conformance_checks": [
            {
                "check_name": "boundary-chain conformance recorded",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
                "failure_code": None,
            }
        ],
        "conformance_statement": statement,
        "distributed_operation_conformance_summary": {
            **copy.deepcopy(statement),
            "outcome": CONFORMANCE_OUTCOME_RECORDED,
            "selected_operation_candidate_id": "operation-candidate-001",
            "selected_operation_matter_id": "operation-matter-001",
        },
        "non_claims": conformance_false_non_claims(),
    }


def closure_scope() -> list[str]:
    return list(SUPPORTED_SCOPE)


def closure_basis(
    selected_conformance: dict[str, object] | None = None,
) -> dict[str, object]:
    selected = selected_conformance or selected_conformance_result()
    selected_basis = selected["conformance_basis"]
    assert isinstance(selected_basis, dict)
    selected_scope = selected["conformance_scope"]
    assert isinstance(selected_scope, dict)
    return {
        "selected_conformance_result": selected,
        "selected_receipt_exhaustion_result": selected_basis[
            "selected_receipt_exhaustion_result"
        ],
        "selected_action_consequence_result": selected_basis[
            "selected_action_consequence_result"
        ],
        "selected_execution_emission_result": selected_basis[
            "selected_execution_emission_result"
        ],
        "selected_admission_transition_result": selected_basis[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": selected_basis["selected_operation_context"],
        "selected_refusal_abort_result": selected_basis["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": selected_basis["selected_sync_non_sync_result"],
        "selected_carrier_role_result": selected_basis["selected_carrier_role_result"],
        "selected_source_body_authority_result": selected_basis[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": selected_basis["selected_eligibility_result"],
        "selected_matter_declaration": selected_basis["selected_matter_declaration"],
        "selected_operation_candidate": selected_basis["selected_operation_candidate"],
        "selected_operation_matter": selected_basis["selected_operation_matter"],
        "conformance_scope": selected_scope,
        "receipt_exhaustion_scope": selected_basis["receipt_exhaustion_scope"],
        "action_consequence_scope": selected_basis["action_consequence_scope"],
        "execution_emission_scope": selected_basis["execution_emission_scope"],
        "admission_scope": selected_basis["admission_scope"],
        "boundary_chain_conformance_basis": selected_basis[
            "boundary_chain_conformance_basis"
        ],
        "closure_dependency": {
            "closure_dependency_satisfied_for_boundary_chain": True,
            "boundary_chain_closure_only": True,
        },
        "non_claim_preservation_basis": selected_basis[
            "non_claim_preservation_basis"
        ],
        "overread_prevention_basis": selected_basis["overread_prevention_basis"],
        "declared_closure_scope": closure_scope(),
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "boundary_chain_closure_only": True,
        "no_executed_operation_closure_claim": True,
        "no_executed_operation_conformance_claim": True,
        "no_actual_operation_receipt_claim": True,
        "no_public_readiness_claim": True,
        "no_final_completion_claim": True,
        "no_reusable_permission_created": True,
        "no_autonomous_continuation_authorized": True,
        "no_follow_on_work_authorized": True,
        "non_claims_must_remain_false": True,
        "boundary_scopes_must_remain_bounded": True,
        "no_layer_overread_allowed": True,
    }


def declared_request(
    *,
    selected_conformance: dict[str, object] | None = None,
    requested_outcome: str = OUTCOME_RECORDED,
    intent: str = "RECORD_DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY",
) -> dict[str, object]:
    selected = selected_conformance or selected_conformance_result()
    boundary_recorded = requested_outcome == OUTCOME_RECORDED
    return {
        "closure_request_id": "closure-request-001",
        "closure_question": (
            "Can the recorded distributed operation boundary chain be closed "
            "as a boundary chain only?"
        ),
        "closure_intent": intent,
        "selected_conformance_result": selected,
        "selected_conformance_result_id": "conformance-result-001",
        "selected_conformance_result_outcome": CONFORMANCE_OUTCOME_RECORDED,
        "requested_closure_outcome": requested_outcome,
        "closure_basis": closure_basis(selected),
        "closure_scope": closure_scope(),
        "declared_non_claims": false_non_claims(
            boundary_recorded=boundary_recorded
        ),
    }


def resolve(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_distributed_operation_closure_boundary(
        declared_closure_request=request
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
    request.pop(key, None)
    basis = request["closure_basis"]
    assert isinstance(basis, dict)
    basis.pop(key, None)
    selected = request["selected_conformance_result"]
    assert isinstance(selected, dict)
    conformance_basis_map = selected.get("conformance_basis")
    if isinstance(conformance_basis_map, dict):
        conformance_basis_map.pop(key, None)
    selected_context = selected.get("selected_operation_context")
    if isinstance(selected_context, dict):
        selected_context.pop(context_key or key, None)
    if key == "selected_receipt_exhaustion_result":
        selected.pop("selected_receipt_exhaustion_result", None)
    closure_basis_selected = basis.get("selected_conformance_result")
    if isinstance(closure_basis_selected, dict):
        closure_selected_context = closure_basis_selected.get("selected_operation_context")
        if isinstance(closure_selected_context, dict):
            closure_selected_context.pop(context_key or key, None)
        closure_selected_basis = closure_basis_selected.get("conformance_basis")
        if isinstance(closure_selected_basis, dict):
            closure_selected_basis.pop(key, None)
        if key == "selected_receipt_exhaustion_result":
            closure_basis_selected.pop("selected_receipt_exhaustion_result", None)


def remove_admitted_context_everywhere(request: dict[str, object]) -> None:
    request.pop("selected_operation_context", None)
    basis = request["closure_basis"]
    assert isinstance(basis, dict)
    basis.pop("selected_operation_context", None)
    selected = request["selected_conformance_result"]
    assert isinstance(selected, dict)
    selected["selected_operation_context"] = {}
    conformance_basis_map = selected.get("conformance_basis")
    if isinstance(conformance_basis_map, dict):
        conformance_basis_map.pop("selected_operation_context", None)
    closure_basis_selected = basis.get("selected_conformance_result")
    if isinstance(closure_basis_selected, dict):
        closure_basis_selected["selected_operation_context"] = {}
        selected_basis = closure_basis_selected.get("conformance_basis")
        if isinstance(selected_basis, dict):
            selected_basis.pop("selected_operation_context", None)


def set_admission_field_everywhere(
    request: dict[str, object], field: str, value: bool
) -> None:
    request[field] = value
    basis = request["closure_basis"]
    assert isinstance(basis, dict)
    basis[field] = value
    selected = request["selected_conformance_result"]
    assert isinstance(selected, dict)
    for section_name in (
        "conformance_statement",
        "distributed_operation_conformance_summary",
        "conformance_basis",
    ):
        section = selected.get(section_name)
        if isinstance(section, dict):
            section[field] = value
    selected_context = selected.get("selected_operation_context")
    if isinstance(selected_context, dict):
        selected_context[field] = value
        admitted = selected_context.get("selected_admitted_operation_context")
        if isinstance(admitted, dict):
            admitted[field] = value
            if field == "one_bounded_operation_context_admitted":
                admitted["one_bounded_operation_context_only"] = value
    basis_context = basis.get("selected_operation_context")
    if isinstance(basis_context, dict):
        basis_context[field] = value
        if field == "one_bounded_operation_context_admitted":
            basis_context["one_bounded_operation_context_only"] = value


class DistributedOperationClosureBoundaryTests(unittest.TestCase):
    def assert_no_closure_or_overcommit(self, section: dict[str, object]) -> None:
        for key in FALSE_CLOSURE_KEYS:
            self.assertIs(section[key], False, key)

    def assert_recorded_core(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        statement = result["closure_statement"]
        self.assertTrue(statement["distributed_operation_closure_boundary_recorded"])
        self.assertTrue(statement["boundary_chain_closure_recorded"])
        self.assertEqual(statement["failed_check_count"], 0)
        for key in (
            "selected_conformance_result_preserved",
            "selected_conformance_result_recorded",
            "selected_conformance_result_failed_check_count_zero",
            "selected_receipt_exhaustion_result_preserved",
            "selected_action_consequence_result_preserved",
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
            "conformance_boundary_preserved",
            "boundary_chain_conformance_recorded",
            "all_required_prior_non_claims_preserved",
            "no_layer_overread_prior_layer",
            "boundary_scopes_remained_bounded",
            "closure_scope_supported",
        ):
            self.assertTrue(statement[key], key)
        self.assert_no_closure_or_overcommit(statement)

    def test_boundary_recorded_result_shape_and_core_posture(self) -> None:
        request = declared_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_core(result)

        metadata = result["distributed_operation_closure_metadata"]
        for key in (
            "distributed_operation_closure_result_id",
            "distributed_operation_closure_result_type",
            "distributed_operation_closure_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["distributed_operation_closure_result_version"], "0.1.0"
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_operation_closure_boundary",
        )

        declared = result["declared_closure_question"]
        self.assertEqual(declared["closure_request_id"], request["closure_request_id"])
        self.assertEqual(declared["closure_question"], request["closure_question"])
        self.assertEqual(declared["closure_intent"], request["closure_intent"])
        self.assertEqual(
            declared["selected_conformance_result_id"], "conformance-result-001"
        )
        self.assertEqual(
            declared["selected_conformance_result_outcome"],
            CONFORMANCE_OUTCOME_RECORDED,
        )
        for key in (
            "closure_boundary_is_not_executed_operation_closure",
            "closure_boundary_is_not_final_completion",
            "closure_boundary_is_not_public_readiness",
            "closure_boundary_is_not_actual_receipt",
            "closure_boundary_is_not_executed_operation_conformance",
        ):
            self.assertTrue(declared[key], key)

        selected = result["selected_conformance_result"]
        self.assertEqual(
            selected["selected_conformance_result_id"], "conformance-result-001"
        )
        self.assertEqual(
            selected["selected_conformance_result_outcome"],
            CONFORMANCE_OUTCOME_RECORDED,
        )
        self.assertTrue(selected["selected_conformance_result_recorded"])
        self.assertTrue(selected["selected_conformance_result_failed_check_count_zero"])
        self.assertTrue(selected["selected_conformance_boundary_preserved"])
        self.assertTrue(
            selected[
                "selected_conformance_result_recorded_boundary_chain_conformance_only"
            ]
        )
        for key in (
            "selected_conformance_result_did_not_claim_executed_operation_conformance",
            "selected_conformance_result_did_not_claim_actual_operation_receipt",
            "selected_conformance_result_did_not_claim_closure",
            "selected_conformance_result_did_not_create_public_readiness",
            "selected_conformance_result_did_not_claim_final_completion",
            "selected_conformance_result_did_not_authorize_follow_on_work",
            "selected_conformance_result_did_not_create_reusable_permission",
            "selected_conformance_result_did_not_authorize_autonomous_continuation",
        ):
            self.assertTrue(selected[key], key)
        self.assertEqual(
            selected["selected_conformance_result"],
            request["selected_conformance_result"],
        )

        context = result["selected_operation_context"]
        for key in (
            "selected_conformance_result",
            "selected_receipt_exhaustion_result",
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
        self.assertTrue(context["conformance_boundary_recorded"])
        self.assertTrue(context["boundary_chain_conformance_only"])
        for key in (
            "executed_operation_closure_claimed",
            "executed_operation_conformance_claimed",
            "actual_operation_receipt_recorded",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
        ):
            self.assertIs(context[key], False, key)

        basis = result["closure_basis"]
        for key in (
            "selected_conformance_result",
            "selected_receipt_exhaustion_result",
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
            "conformance_scope",
            "receipt_exhaustion_scope",
            "action_consequence_scope",
            "execution_emission_scope",
            "admission_scope",
            "boundary_chain_conformance_basis",
            "closure_dependency",
            "non_claim_preservation_basis",
            "overread_prevention_basis",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "boundary_chain_closure_only",
            "no_executed_operation_closure_claim",
            "no_executed_operation_conformance_claim",
            "no_actual_operation_receipt_claim",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "no_reusable_permission_created",
            "no_autonomous_continuation_authorized",
            "no_follow_on_work_authorized",
            "non_claims_must_remain_false",
            "boundary_scopes_must_remain_bounded",
            "no_layer_overread_allowed",
        ):
            self.assertTrue(basis[key], key)

    def test_scope_checks_non_meaning_open_items_non_claims_and_summary(self) -> None:
        result = resolve(declared_request())
        scope = result["closure_scope"]

        self.assertEqual(scope["selected_closure_scope"], list(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_closure_scope_supported"])
        self.assertTrue(scope["all_selected_closure_scope_values_supported"])
        for key in (
            "boundary_chain_closure_only",
            "no_executed_operation_closure_claim",
            "no_executed_operation_conformance_claim",
            "no_actual_operation_receipt_claim",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "no_reusable_permission_created",
            "no_autonomous_continuation_authorized",
            "no_follow_on_work_authorized",
            "non_claims_must_remain_false",
            "boundary_scopes_must_remain_bounded",
            "no_layer_overread_allowed",
        ):
            self.assertTrue(scope[key], key)

        checks = result["closure_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        expected_check_names = {
            "closure question declared",
            "closure intent supported",
            "selected conformance result present",
            "selected conformance result outcome declared",
            "selected conformance result outcome recorded",
            "selected conformance result failed check count zero",
            "selected receipt / exhaustion result preserved",
            "selected action / consequence result preserved",
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
            "conformance boundary preserved",
            "boundary-chain conformance recorded",
            "no executed-operation conformance claimed",
            "no actual operation receipt claimed",
            "operation unexecuted",
            "output un-emitted",
            "action unauthorized",
            "consequence uncreated",
            "no executed-operation closure already claimed",
            "selected conformance did not claim closure",
            "no public readiness",
            "no final completion",
            "no follow-on work",
            "no reusable permission",
            "no autonomous continuation",
            "all required prior non-claims false",
            "no layer overread prior layer",
            "boundary scopes remained bounded",
            "closure scope declared",
            "closure scope supported",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_check_names.issubset({c["check_name"] for c in checks}))

        non_meaning = result["closure_non_meaning"]
        for key in (
            "executed_operation_closure_claimed",
            "executed_operation_conformance_claimed",
            "actual_operation_receipt_recorded",
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
            "final_system_completion_claimed",
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
        self.assertTrue(non_claims["boundary_chain_closure_recorded"])
        for key in (
            "executed_operation_closure_claimed",
            "executed_operation_conformance_claimed",
            "actual_operation_receipt_recorded",
            "public_launch_readiness_created",
            "final_completion_claimed",
        ):
            self.assertFalse(non_claims[key], key)

        summary = resolver.build_distributed_operation_closure_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["closure_request_id"], "closure-request-001")
        self.assertEqual(
            summary["selected_conformance_result_id"], "conformance-result-001"
        )
        self.assertEqual(
            summary["selected_conformance_result_outcome"],
            CONFORMANCE_OUTCOME_RECORDED,
        )
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "closure_boundary_recorded",
            "boundary_chain_closure_recorded",
            "selected_conformance_result_preserved",
            "selected_conformance_result_recorded",
            "selected_conformance_result_failed_check_count_zero",
            "selected_receipt_exhaustion_result_preserved",
            "selected_action_consequence_result_preserved",
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
            "conformance_boundary_preserved",
            "boundary_chain_conformance_recorded",
            "no_executed_operation_closure",
            "no_executed_operation_conformance",
            "no_actual_receipt",
            "operation_unexecuted",
            "output_un_emitted",
            "action_unauthorized",
            "consequence_uncreated",
            "no_operation_execution_emission_action_consequence",
            "no_public_readiness_final_completion_follow_on_work",
            "no_reusable_permission_autonomous_continuation",
            "all_required_prior_non_claims_preserved",
            "no_layer_overread_prior_layer",
            "boundary_scopes_remained_bounded",
            "closure_scope_supported",
        ):
            self.assertTrue(summary[key], key)

    def test_each_supported_scope_records_and_unsupported_scope_blocks(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            request = declared_request()
            request["closure_scope"] = [scope_value]
            result = resolve(request)
            self.assertEqual(result["outcome"], OUTCOME_RECORDED, scope_value)
            self.assertEqual(
                result["closure_scope"]["selected_closure_scope"], [scope_value]
            )
            self.assertTrue(
                result["closure_scope"]["all_selected_closure_scope_supported"]
            )

        request = declared_request()
        request["closure_scope"] = closure_scope() + ["UNSUPPORTED_CLOSURE_SCOPE"]
        result = resolve(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_CLOSURE_SCOPE")

    def test_requires_additional_basis_and_not_closed_outcomes(self) -> None:
        additional_request = declared_request(
            requested_outcome=OUTCOME_REQUIRES_ADDITIONAL
        )
        additional_request["additional_basis_context"] = {
            "reason": "Closure cannot yet be bounded without final-completion risk.",
            "missing_basis": [
                "boundary-chain closure basis too generic",
                "closure dependency basis too generic",
                "follow-on-work refusal basis unclear",
            ],
        }
        additional_original = copy.deepcopy(additional_request)
        additional_result = resolve(additional_request)
        self.assertEqual(additional_result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertEqual(additional_request, additional_original)
        self.assertFalse(additional_result["non_claims"]["boundary_chain_closure_recorded"])
        self.assertTrue(
            additional_result["selected_conformance_result"][
                "selected_conformance_result"
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
            "additional_basis_claims_executed_operation_closure",
            "additional_basis_claims_executed_operation_conformance",
            "additional_basis_claims_actual_operation_receipt",
            "additional_basis_creates_public_readiness",
            "additional_basis_claims_final_completion",
            "additional_basis_creates_reusable_permission",
            "additional_basis_authorizes_autonomous_continuation",
            "additional_basis_authorizes_action",
            "additional_basis_creates_consequence",
            "additional_basis_executes_operation",
            "additional_basis_emits_output",
            "additional_basis_schedules_follow_on_work",
        ):
            self.assertFalse(additional_result["additional_basis_required"][key], key)
        self.assert_no_closure_or_overcommit(additional_result["closure_statement"])

        not_closed_request = declared_request(requested_outcome=OUTCOME_NOT_CLOSED)
        not_closed_request["not_closed_basis"] = {
            "reason": "Closure would overread conformance as final completion.",
            "failed_closure_reason": "boundary chain cannot be closed as declared",
        }
        not_closed_original = copy.deepcopy(not_closed_request)
        not_closed_result = resolve(not_closed_request)
        self.assertEqual(not_closed_result["outcome"], OUTCOME_NOT_CLOSED)
        self.assertEqual(not_closed_request, not_closed_original)
        self.assertFalse(not_closed_result["non_claims"]["boundary_chain_closure_recorded"])
        self.assertEqual(
            not_closed_result["not_closed_basis"]["not_closed_basis"],
            not_closed_request["not_closed_basis"],
        )
        self.assertTrue(not_closed_result["not_closed_basis"]["not_closed"])
        for key in (
            "not_closed_erases_boundary_chain",
            "not_closed_mutates_prior_artifacts",
            "not_closed_authorizes_repair",
            "not_closed_authorizes_action",
            "not_closed_executes_operation",
            "not_closed_closes_executed_operation",
            "not_closed_completes_final_system",
            "not_closed_schedules_follow_on_work",
        ):
            self.assertFalse(not_closed_result["not_closed_basis"][key], key)
        self.assert_no_closure_or_overcommit(not_closed_result["closure_statement"])

        overread_request = declared_request()
        overread_selected = overread_request["selected_conformance_result"]
        assert isinstance(overread_selected, dict)
        overread_selected["conformance_statement"][
            "conformance_overread_as_final_completion"
        ] = True
        overread_result = resolve(overread_request)
        self.assertEqual(overread_result["outcome"], OUTCOME_NOT_CLOSED)
        self.assertIsNone(overread_result["block"]["block_code"])

        observed = {
            resolve(declared_request())["outcome"],
            additional_result["outcome"],
            not_closed_result["outcome"],
            resolve(None)["outcome"],
        }
        self.assertEqual(
            observed,
            {
                OUTCOME_RECORDED,
                OUTCOME_REQUIRES_ADDITIONAL,
                OUTCOME_NOT_CLOSED,
                OUTCOME_BLOCKED,
            },
        )

    def test_request_builder_helper_records_valid_boundary(self) -> None:
        selected = selected_conformance_result()
        basis = closure_basis(selected)
        with tempfile.TemporaryDirectory() as temp_dir:
            selected_path = Path(temp_dir) / "selected_conformance.json"
            selected_path.write_text(json.dumps(selected), encoding="utf-8")
            request = resolver.build_declared_distributed_operation_closure_request(
                "builder-request-001",
                "Can the recorded distributed operation boundary chain be closed?",
                selected,
                basis,
                closure_scope(),
                selected_conformance_result_path=str(selected_path),
                selected_conformance_result_id="conformance-result-001",
                selected_conformance_result_outcome=CONFORMANCE_OUTCOME_RECORDED,
                additional_basis_context={"not_used_for_recorded": False},
                not_closed_basis={"not_used_for_recorded": False},
            )

            self.assertEqual(request["closure_request_id"], "builder-request-001")
            self.assertEqual(
                request["closure_question"],
                "Can the recorded distributed operation boundary chain be closed?",
            )
            self.assertEqual(request["selected_conformance_result"], selected)
            self.assertEqual(request["closure_basis"], basis)
            self.assertEqual(request["closure_scope"], closure_scope())
            self.assertEqual(request["selected_conformance_result_path"], str(selected_path))
            self.assertEqual(
                request["selected_conformance_result_id"], "conformance-result-001"
            )
            self.assertEqual(
                request["selected_conformance_result_outcome"],
                CONFORMANCE_OUTCOME_RECORDED,
            )
            self.assertEqual(
                request["additional_basis_context"],
                {"not_used_for_recorded": False},
            )
            self.assertEqual(
                request["not_closed_basis"], {"not_used_for_recorded": False}
            )
            for key in REQUIRED_NON_CLAIMS:
                self.assertIs(request["declared_non_claims"][key], False, key)

            valid_request = (
                resolver.build_declared_distributed_operation_closure_request(
                    "builder-valid-request-001",
                    "Can the recorded distributed operation boundary chain be closed?",
                    selected,
                    basis,
                    closure_scope(),
                    selected_conformance_result_id="conformance-result-001",
                    selected_conformance_result_outcome=(
                        CONFORMANCE_OUTCOME_RECORDED
                    ),
                    additional_basis_context={"not_used_for_recorded": False},
                )
            )
            result = resolve(valid_request)
            self.assert_recorded_core(result)

    def test_path_based_selected_conformance_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            selected_path = temp / "selected_conformance_result.json"
            selected_path.write_text(
                json.dumps(selected_conformance_result()),
                encoding="utf-8",
            )

            request = declared_request()
            request.pop("selected_conformance_result")
            request["selected_conformance_result_path"] = str(selected_path)
            result = resolve(request)
            self.assert_recorded_core(result)
            selected = result["selected_conformance_result"]
            self.assertEqual(
                selected["selected_conformance_result_path"], str(selected_path)
            )
            self.assertEqual(
                selected["selected_conformance_result_id"], "conformance-result-001"
            )
            self.assertEqual(
                selected["selected_conformance_result_outcome"],
                CONFORMANCE_OUTCOME_RECORDED,
            )

            request_path = temp / "declared_closure_request.json"
            request_path.write_text(json.dumps(declared_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_operation_closure_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_request())
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_closure_question"]["closure_request_path"],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_deduplicates(self) -> None:
        result = resolve(declared_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "result.json"
            written = resolver.write_distributed_operation_closure_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY_ROOT",
                Path(temp_dir) / "default-root",
            ):
                first = resolver.write_distributed_operation_closure_result(result)
                second = resolver.write_distributed_operation_closure_result(result)
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, Path(temp_dir) / "default-root")
                self.assertEqual(second.parent, Path(temp_dir) / "default-root")
                self.assertIn("closure-request-001", first.name)
                self.assertTrue(second.stem.endswith("_001"))
                self.assertNotIn("distributed_operation_conformance", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        original_request = copy.deepcopy(request)
        original_selected = copy.deepcopy(request["selected_conformance_result"])
        original_basis = copy.deepcopy(request["closure_basis"])
        original_scope = copy.deepcopy(request["closure_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_conformance_result"], original_selected)
        self.assertEqual(request["closure_basis"], original_basis)
        self.assertEqual(request["closure_scope"], original_scope)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            upstream_paths = []
            for name in (
                "selected_conformance.json",
                "selected_receipt_exhaustion.json",
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
            resolver.write_distributed_operation_closure_result(
                first, temp / "new" / "result.json"
            )
            after = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            self.assertEqual(before, after)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        blocked = declared_request(
            intent="BLOCK_DISTRIBUTED_OPERATION_CLOSURE_REVIEW"
        )
        result = resolve(blocked)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "CLOSURE_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(
            result["closure_statement"]["distributed_operation_closure_boundary_recorded"]
        )

        missing = resolve(None)
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing), "CLOSURE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_operation_closure_boundary(
            declared_closure_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(malformed), "DECLARED_CLOSURE_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            unreadable = resolver.resolve_distributed_operation_closure_boundary_from_path(
                temp / "missing.json"
            )
            self.assertEqual(block_code(unreadable), "DECLARED_CLOSURE_REQUEST_UNREADABLE")

            bad_json = temp / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = resolver.resolve_distributed_operation_closure_boundary_from_path(
                bad_json
            )
            self.assertEqual(block_code(bad), "DECLARED_CLOSURE_REQUEST_MALFORMED")

            array_json = temp / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_operation_closure_boundary_from_path(
                array_json
            )
            self.assertEqual(
                block_code(array_result), "DECLARED_CLOSURE_REQUEST_MALFORMED"
            )

            request = declared_request()
            request.pop("selected_conformance_result")
            request["selected_conformance_result_path"] = str(
                temp / "missing-selected.json"
            )
            self.assertEqual(block_code(resolve(request)), "CONFORMANCE_RESULT_UNREADABLE")

            malformed_selected_path = temp / "malformed-selected.json"
            malformed_selected_path.write_text("{bad", encoding="utf-8")
            request["selected_conformance_result_path"] = str(malformed_selected_path)
            self.assertEqual(block_code(resolve(request)), "CONFORMANCE_RESULT_MALFORMED")

            array_selected_path = temp / "array-selected.json"
            array_selected_path.write_text("[]", encoding="utf-8")
            request["selected_conformance_result_path"] = str(array_selected_path)
            self.assertEqual(block_code(resolve(request)), "CONFORMANCE_RESULT_MALFORMED")

    def test_selected_conformance_result_issue_blocks(self) -> None:
        cases = (
            (("outcome",), None, "CONFORMANCE_RESULT_OUTCOME_MISSING"),
            (
                ("outcome",),
                "DISTRIBUTED_OPERATION_CONFORMANCE_NOT_CONFORMANT",
                "CONFORMANCE_RESULT_NOT_RECORDED",
            ),
            (
                ("conformance_statement", "failed_check_count"),
                1,
                "CONFORMANCE_RESULT_HAS_FAILED_CHECKS",
            ),
        )
        for path, value, expected_code in cases:
            selected = selected_conformance_result()
            if value is None:
                delete_path(selected, path)
                delete_path(
                    selected,
                    ("distributed_operation_conformance_summary", "outcome"),
                )
            else:
                set_path(selected, path, value)
                if path[-1] == "outcome":
                    selected["distributed_operation_conformance_summary"][
                        "outcome"
                    ] = value
                if path[-1] == "failed_check_count":
                    selected["distributed_operation_conformance_summary"][
                        "failed_check_count"
                    ] = value
            request = declared_request(selected_conformance=selected)
            if value is None:
                request.pop("selected_conformance_result_outcome")
            elif path[-1] == "outcome":
                request["selected_conformance_result_outcome"] = value
            result = resolve(request)
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code, expected_code)

    def test_missing_required_basis_blocks(self) -> None:
        missing_cases = (
            (
                "selected_receipt_exhaustion_result",
                "RECEIPT_EXHAUSTION_RESULT_MISSING",
            ),
            ("selected_action_consequence_result", "ACTION_CONSEQUENCE_RESULT_MISSING"),
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
        remove_admitted_context_everywhere(request)
        self.assertEqual(block_code(resolve(request)), "ADMITTED_OPERATION_CONTEXT_MISSING")

        request = declared_request()
        request.pop("closure_scope")
        closure_request_basis = request["closure_basis"]
        assert isinstance(closure_request_basis, dict)
        closure_request_basis.pop("declared_closure_scope")
        closure_request_basis.pop("closure_scope", None)
        self.assertEqual(block_code(resolve(request)), "CLOSURE_SCOPE_MISSING")

    def test_operation_context_not_admitted_blocks(self) -> None:
        for field, expected_code in (
            ("operation_admitted", "OPERATION_NOT_ADMITTED"),
            (
                "one_bounded_operation_context_admitted",
                "ONE_BOUNDED_OPERATION_CONTEXT_NOT_ADMITTED",
            ),
        ):
            request = declared_request()
            set_admission_field_everywhere(request, field, False)
            result = resolve(request)
            self.assertEqual(block_code(result), expected_code, field)

    def test_closure_collapse_flags_block(self) -> None:
        cases = (
            (
                "executed_operation_closure_claimed",
                "CLOSURE_REVIEW_CLAIMS_EXECUTED_OPERATION_CLOSURE",
            ),
            (
                "executed_operation_conformance_claimed",
                "CLOSURE_REVIEW_CLAIMS_EXECUTED_OPERATION_CONFORMANCE",
            ),
            (
                "actual_operation_receipt_recorded",
                "CLOSURE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
            ),
            (
                "public_launch_readiness_created",
                "CLOSURE_REVIEW_CREATES_PUBLIC_READINESS",
            ),
            (
                "final_completion_claimed",
                "CLOSURE_REVIEW_CLAIMS_FINAL_COMPLETION",
            ),
            (
                "follow_on_work_authorized",
                "CLOSURE_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            ),
            (
                "reusable_permission_created",
                "CLOSURE_REVIEW_CREATES_REUSABLE_PERMISSION",
            ),
            (
                "autonomous_continuation_authorized",
                "CLOSURE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            ),
            ("action_authorized", "CLOSURE_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "CLOSURE_REVIEW_CREATES_CONSEQUENCE"),
            ("operation_executed", "CLOSURE_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "CLOSURE_REVIEW_EMITS_OUTPUT"),
            (
                "repository_synchronization_authorized",
                "CLOSURE_REVIEW_AUTHORIZES_SYNCHRONIZATION",
            ),
            (
                "non_synchronized_operation_authorized",
                "CLOSURE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
            ),
            (
                "full_body_transfer_authorized",
                "CLOSURE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "CLOSURE_REVIEW_CREATES_SECOND_BODY"),
            ("refusal_abort_erased", "CLOSURE_REVIEW_ERASES_REFUSAL_ABORT"),
            ("evidence_erased", "CLOSURE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "CLOSURE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("blocked_attempt_erased", "CLOSURE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            (
                "projection_mismatch_hidden",
                "CLOSURE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
            ),
            ("divergence_resolved", "CLOSURE_REVIEW_RESOLVES_DIVERGENCE"),
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
        flipped_claim["declared_non_claims"]["carrier_authority_created"] = True
        flipped_result = resolve(flipped_claim)
        self.assertEqual(flipped_result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(flipped_result), "NON_CLAIM_MISSING_OR_FLIPPED")


if __name__ == "__main__":
    unittest.main()
