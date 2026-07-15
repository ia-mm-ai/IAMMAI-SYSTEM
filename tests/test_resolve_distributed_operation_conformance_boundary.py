"""Bounded tests for distributed operation conformance boundary.

These tests prove that the resolver records boundary-chain conformance only.
They do not claim executed-operation conformance, actual operation receipt,
operation closure, public readiness, final completion, reusable permission,
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

import resolve_distributed_operation_conformance_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_RECORDED"
OUTCOME_NOT_CONFORMANT = "DISTRIBUTED_OPERATION_CONFORMANCE_NOT_CONFORMANT"
OUTCOME_REQUIRES_ADDITIONAL = (
    "DISTRIBUTED_OPERATION_CONFORMANCE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_CONFORMANCE_REVIEW_BLOCKED"
RECEIPT_OUTCOME_RECORDED = (
    "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_BOUNDARY_RECORDED"
)
ACTION_OUTCOME_RECORDED = "DISTRIBUTED_ACTION_CONSEQUENCE_BOUNDARY_RECORDED"
EXECUTION_OUTCOME_RECORDED = "DISTRIBUTED_EXECUTION_EMISSION_BOUNDARY_RECORDED"

SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_CONFORMANCE_SCOPE)
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

TOP_LEVEL_SECTIONS = (
    "distributed_operation_conformance_metadata",
    "declared_conformance_question",
    "selected_receipt_exhaustion_result",
    "selected_operation_context",
    "conformance_basis",
    "conformance_scope",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "additional_basis_required",
    "not_conformant_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_operation_conformance_summary",
)

FALSE_CONFORMANCE_KEYS = (
    "actual_operation_receipt_recorded",
    "execution_receipt_recorded",
    "output_receipt_recorded",
    "action_receipt_recorded",
    "consequence_receipt_recorded",
    "executed_operation_conformance_claimed",
    "closure_claimed",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "reusable_permission_created",
    "autonomous_continuation_authorized",
    "operation_executed",
    "output_emitted",
    "action_authorized",
    "consequence_created",
)


def false_non_claims(*, boundary_recorded: bool = True) -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims["boundary_chain_conformance_recorded"] = boundary_recorded
    claims["distributed_operation_conformance_boundary_recorded"] = boundary_recorded
    return claims


def receipt_false_non_claims() -> dict[str, bool]:
    claims = {key: False for key in REQUIRED_NON_CLAIMS}
    claims.update(
        {
            "execution_receipt_recorded": False,
            "output_receipt_recorded": False,
            "action_receipt_recorded": False,
            "consequence_receipt_recorded": False,
            "receipt_treated_as_consequence": False,
            "conformance_claimed": False,
            "receipt_exhaustion_boundary_recorded": True,
            "distributed_operation_receipt_exhaustion_boundary_recorded": True,
        }
    )
    return claims


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
        "operation_question": "Did the recorded boundary chain conform?",
        "candidate_remains_candidate_only": True,
    }


def selected_operation_matter() -> dict[str, object]:
    return {
        "operation_matter_id": "operation-matter-001",
        "selected_operation_candidate_id": "operation-candidate-001",
        "operation_question": "Did the recorded boundary chain conform?",
        "matter_remains_declaration_only": True,
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
        "output_treated_as_consequence": False,
        "evidence_treated_as_consequence": False,
        "standing_treated_as_consequence": False,
        "receipt_treated_as_consequence": False,
    }


def receipt_scope() -> list[str]:
    return [
        "BOUNDARY_CHAIN_RECEIPT_ONLY",
        "NO_ACTUAL_OPERATION_RECEIPT",
        "NO_EXECUTION_RECEIPT",
        "NO_OUTPUT_RECEIPT",
        "NO_ACTION_RECEIPT",
        "NO_CONSEQUENCE_RECEIPT",
        "NO_CONFORMANCE_CLAIM",
        "NO_CLOSURE_CLAIM",
        "NO_REUSABLE_PERMISSION_REMAINS",
        "NO_AUTONOMOUS_CONTINUATION_AUTHORIZED",
        "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
        "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
    ]


def action_consequence_scope() -> list[str]:
    return [
        "NO_ACTION_AUTHORIZED_BY_BOUNDARY",
        "NO_CONSEQUENCE_CREATED_BY_BOUNDARY",
        "NO_EXECUTION_BY_ACTION_CONSEQUENCE_BOUNDARY",
        "NO_OUTPUT_EMISSION_BY_ACTION_CONSEQUENCE_BOUNDARY",
        "RECEIPT_EXHAUSTION_REQUIRED_BEFORE_CLOSURE",
        "CONFORMANCE_REQUIRED_BEFORE_CLOSURE",
        "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
    ]


def execution_emission_scope() -> list[str]:
    return [
        "NO_OPERATION_EXECUTION_BY_BOUNDARY",
        "NO_OUTPUT_EMISSION_BY_BOUNDARY",
        "NO_ACTION_AUTHORIZATION_BY_BOUNDARY",
        "NO_CONSEQUENCE_CREATION_BY_BOUNDARY",
    ]


def admission_scope() -> list[str]:
    return [
        "ONE_BOUNDED_OPERATION_CONTEXT_ONLY",
        "NO_EXECUTION_BY_ADMISSION",
        "NO_OUTPUT_EMISSION_BY_ADMISSION",
    ]


def closure_dependency() -> dict[str, object]:
    return {
        "closure_remains_future_work": True,
        "closure_requires_separate_boundary": True,
        "closure_claimed": False,
    }


def selected_operation_context_for_receipt() -> dict[str, object]:
    return {
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
        "receipt_exhaustion_boundary_recorded": True,
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
    }


def receipt_exhaustion_basis(
    context: dict[str, object] | None = None,
) -> dict[str, object]:
    selected_context = context or selected_operation_context_for_receipt()
    return {
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
        "receipt_exhaustion_scope": receipt_scope(),
        "action_consequence_scope": action_consequence_scope(),
        "execution_emission_scope": execution_emission_scope(),
        "admission_scope": admission_scope(),
        "refusal_abort_posture_basis": {"refusal_abort_preserved": True},
        "sync_non_sync_posture_basis": {"sync_non_sync_preserved": True},
        "carrier_role_basis": {"carrier_role_preserved": True},
        "source_body_authority_basis": {"source_body_authority_preserved": True},
        "non_claim_preservation_basis": {"all_required_non_claims_false": True},
        "overread_prevention_basis": {"no_layer_overread_prior_layer": True},
        "scope_preservation_basis": {"boundary_scopes_remained_bounded": True},
        "prior_boundary_preservation_basis": {"prior_boundaries_preserved": True},
        "closure_dependency": closure_dependency(),
        "operation_admitted": True,
        "one_bounded_operation_context_admitted": True,
        "receipt_exhaustion_boundary_recorded": True,
        "receipt_exhaustion_boundary_chain_accounting_only": True,
        "boundary_chain_receipt_only": True,
    }


def receipt_exhaustion_statement() -> dict[str, object]:
    statement = {
        "failed_check_count": 0,
        "distributed_operation_receipt_exhaustion_boundary_recorded": True,
        "receipt_exhaustion_boundary_recorded": True,
        "receipt_exhaustion_boundary_preserved": True,
        "receipt_exhaustion_boundary_chain_accounting_only": True,
        "boundary_chain_receipt_only": True,
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
        "actual_operation_receipt_recorded": False,
        "execution_receipt_recorded": False,
        "output_receipt_recorded": False,
        "action_receipt_recorded": False,
        "consequence_receipt_recorded": False,
        "action_authorized": False,
        "consequence_created": False,
        "operation_executed": False,
        "output_emitted": False,
        "conformance_claimed": False,
        "closure_claimed": False,
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


def selected_receipt_exhaustion_result() -> dict[str, object]:
    context = selected_operation_context_for_receipt()
    basis = receipt_exhaustion_basis(context)
    statement = receipt_exhaustion_statement()
    return {
        "distributed_receipt_exhaustion_metadata": {
            "distributed_receipt_exhaustion_result_id": (
                "receipt-exhaustion-result-001"
            ),
            "distributed_receipt_exhaustion_result_version": "0.1.0",
        },
        "outcome": RECEIPT_OUTCOME_RECORDED,
        "selected_operation_context": context,
        "receipt_exhaustion_basis": basis,
        "receipt_exhaustion_scope": {
            "selected_receipt_exhaustion_scope": receipt_scope(),
            "boundary_chain_receipt_only": True,
            "no_actual_operation_receipt": True,
            "no_execution_receipt": True,
            "no_output_receipt": True,
            "no_action_receipt": True,
            "no_consequence_receipt": True,
            "no_conformance_claim": True,
            "no_closure_claim": True,
            "no_reusable_permission_remains": True,
            "no_autonomous_continuation_authorized": True,
        },
        "receipt_exhaustion_statement": statement,
        "distributed_receipt_exhaustion_summary": {
            "outcome": RECEIPT_OUTCOME_RECORDED,
            "failed_check_count": 0,
            "receipt_exhaustion_boundary_recorded": True,
            "distributed_operation_receipt_exhaustion_boundary_recorded": True,
            "receipt_exhaustion_boundary_chain_accounting_only": True,
            "boundary_chain_receipt_only": True,
            "operation_admitted": True,
            "one_bounded_operation_context_admitted": True,
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
        },
        "non_claims": receipt_false_non_claims(),
    }


def conformance_basis(
    selected_receipt: dict[str, object] | None = None,
) -> dict[str, object]:
    selected = selected_receipt or selected_receipt_exhaustion_result()
    receipt_basis = selected["receipt_exhaustion_basis"]
    assert isinstance(receipt_basis, dict)
    return {
        "selected_receipt_exhaustion_result": selected,
        "selected_action_consequence_result": receipt_basis[
            "selected_action_consequence_result"
        ],
        "selected_execution_emission_result": receipt_basis[
            "selected_execution_emission_result"
        ],
        "selected_admission_transition_result": receipt_basis[
            "selected_admission_transition_result"
        ],
        "selected_operation_context": receipt_basis["selected_operation_context"],
        "selected_refusal_abort_result": receipt_basis["selected_refusal_abort_result"],
        "selected_sync_non_sync_result": receipt_basis["selected_sync_non_sync_result"],
        "selected_carrier_role_result": receipt_basis["selected_carrier_role_result"],
        "selected_source_body_authority_result": receipt_basis[
            "selected_source_body_authority_result"
        ],
        "selected_eligibility_result": receipt_basis["selected_eligibility_result"],
        "selected_matter_declaration": receipt_basis["selected_matter_declaration"],
        "selected_operation_candidate": receipt_basis["selected_operation_candidate"],
        "selected_operation_matter": receipt_basis["selected_operation_matter"],
        "receipt_exhaustion_scope": receipt_basis["receipt_exhaustion_scope"],
        "action_consequence_scope": receipt_basis["action_consequence_scope"],
        "execution_emission_scope": receipt_basis["execution_emission_scope"],
        "admission_scope": receipt_basis["admission_scope"],
        "refusal_abort_posture_basis": receipt_basis["refusal_abort_posture_basis"],
        "sync_non_sync_posture_basis": receipt_basis["sync_non_sync_posture_basis"],
        "carrier_role_basis": receipt_basis["carrier_role_basis"],
        "source_body_authority_basis": receipt_basis["source_body_authority_basis"],
        "non_claim_preservation_basis": receipt_basis["non_claim_preservation_basis"],
        "overread_prevention_basis": receipt_basis["overread_prevention_basis"],
        "scope_preservation_basis": receipt_basis["scope_preservation_basis"],
        "prior_boundary_preservation_basis": receipt_basis[
            "prior_boundary_preservation_basis"
        ],
        "closure_dependency": receipt_basis["closure_dependency"],
        "declared_conformance_scope": list(SUPPORTED_SCOPE),
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


def declared_request(
    *,
    selected_receipt: dict[str, object] | None = None,
    requested_outcome: str = OUTCOME_RECORDED,
    intent: str = "RECORD_DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY",
) -> dict[str, object]:
    selected = selected_receipt or selected_receipt_exhaustion_result()
    boundary_recorded = requested_outcome == OUTCOME_RECORDED
    return {
        "conformance_request_id": "conformance-request-001",
        "conformance_question": (
            "Did the recorded distributed operation boundary chain conform "
            "to its own declared limits?"
        ),
        "conformance_intent": intent,
        "selected_receipt_exhaustion_result": selected,
        "selected_receipt_exhaustion_result_id": "receipt-exhaustion-result-001",
        "selected_receipt_exhaustion_result_outcome": RECEIPT_OUTCOME_RECORDED,
        "requested_conformance_outcome": requested_outcome,
        "conformance_basis": conformance_basis(selected),
        "conformance_scope": list(SUPPORTED_SCOPE),
        "closure_dependency": closure_dependency(),
        "declared_non_claims": false_non_claims(boundary_recorded=boundary_recorded),
    }


def resolve(request: dict[str, object] | None = None) -> dict[str, object]:
    return resolver.resolve_distributed_operation_conformance_boundary(
        declared_conformance_request=request
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
    basis = request["conformance_basis"]
    assert isinstance(basis, dict)
    basis.pop(key, None)
    selected = request["selected_receipt_exhaustion_result"]
    assert isinstance(selected, dict)
    receipt_basis = selected.get("receipt_exhaustion_basis")
    if isinstance(receipt_basis, dict):
        receipt_basis.pop(key, None)
    selected_context = selected.get("selected_operation_context")
    if isinstance(selected_context, dict):
        selected_context.pop(context_key or key, None)


def set_admission_field_everywhere(
    request: dict[str, object], field: str, value: bool
) -> None:
    selected = request["selected_receipt_exhaustion_result"]
    assert isinstance(selected, dict)
    for section_name in (
        "receipt_exhaustion_statement",
        "distributed_receipt_exhaustion_summary",
        "receipt_exhaustion_basis",
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


class DistributedOperationConformanceBoundaryTests(unittest.TestCase):
    def assert_no_conformance_closure_or_overcommit(
        self, section: dict[str, object]
    ) -> None:
        for key in FALSE_CONFORMANCE_KEYS:
            self.assertIs(section[key], False, key)

    def assert_recorded_core(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        statement = result["conformance_statement"]
        self.assertTrue(statement["distributed_operation_conformance_boundary_recorded"])
        self.assertTrue(statement["boundary_chain_conformance_recorded"])
        self.assertEqual(statement["failed_check_count"], 0)
        for key in (
            "selected_receipt_exhaustion_result_preserved",
            "selected_receipt_exhaustion_result_recorded",
            "selected_receipt_exhaustion_result_failed_check_count_zero",
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
            "receipt_exhaustion_boundary_preserved",
            "receipt_exhaustion_boundary_chain_accounting_only",
            "all_required_prior_non_claims_preserved",
            "no_layer_overread_prior_layer",
            "boundary_scopes_remained_bounded",
            "closure_requires_separate_boundary",
            "conformance_scope_supported",
        ):
            self.assertTrue(statement[key], key)
        self.assert_no_conformance_closure_or_overcommit(statement)

    def test_boundary_recorded_result_shape_and_core_posture(self) -> None:
        request = declared_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assert_recorded_core(result)

        metadata = result["distributed_operation_conformance_metadata"]
        for key in (
            "distributed_operation_conformance_result_id",
            "distributed_operation_conformance_result_type",
            "distributed_operation_conformance_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["distributed_operation_conformance_result_version"], "0.1.0"
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_operation_conformance_boundary",
        )

        declared = result["declared_conformance_question"]
        self.assertEqual(
            declared["conformance_request_id"], request["conformance_request_id"]
        )
        self.assertEqual(declared["conformance_question"], request["conformance_question"])
        self.assertEqual(declared["conformance_intent"], request["conformance_intent"])
        self.assertEqual(
            declared["selected_receipt_exhaustion_result_id"],
            "receipt-exhaustion-result-001",
        )
        self.assertEqual(
            declared["selected_receipt_exhaustion_result_outcome"],
            RECEIPT_OUTCOME_RECORDED,
        )
        for key in (
            "conformance_boundary_is_not_executed_operation_conformance",
            "conformance_boundary_is_not_actual_receipt",
            "conformance_boundary_is_not_closure",
            "conformance_boundary_is_not_public_readiness",
            "conformance_boundary_is_not_final_completion",
        ):
            self.assertTrue(declared[key], key)

        selected = result["selected_receipt_exhaustion_result"]
        self.assertEqual(
            selected["selected_receipt_exhaustion_result_id"],
            "receipt-exhaustion-result-001",
        )
        self.assertEqual(
            selected["selected_receipt_exhaustion_result_outcome"],
            RECEIPT_OUTCOME_RECORDED,
        )
        self.assertTrue(selected["selected_receipt_exhaustion_result_recorded"])
        self.assertTrue(
            selected["selected_receipt_exhaustion_result_failed_check_count_zero"]
        )
        self.assertTrue(selected["selected_receipt_exhaustion_boundary_preserved"])
        self.assertTrue(
            selected[
                "selected_receipt_exhaustion_result_recorded_boundary_chain_accounting_only"
            ]
        )
        preserved_statement = selected["selected_receipt_exhaustion_result"][
            "receipt_exhaustion_statement"
        ]
        for key in (
            "actual_operation_receipt_recorded",
            "execution_receipt_recorded",
            "output_receipt_recorded",
            "action_receipt_recorded",
            "consequence_receipt_recorded",
            "conformance_claimed",
            "closure_claimed",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
            "reusable_permission_created",
            "autonomous_continuation_authorized",
        ):
            self.assertIs(preserved_statement[key], False, key)

        context = result["selected_operation_context"]
        for key in (
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
        self.assertTrue(context["receipt_exhaustion_boundary_recorded"])
        self.assertTrue(context["boundary_chain_accounting_only"])
        for key in (
            "actual_operation_receipt_recorded",
            "executed_operation_conformance_claimed",
            "closure_claimed",
            "public_launch_readiness_created",
            "final_completion_claimed",
        ):
            self.assertIs(context[key], False, key)

        basis = result["conformance_basis"]
        for key in (
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
            "receipt_exhaustion_scope",
            "action_consequence_scope",
            "execution_emission_scope",
            "admission_scope",
            "refusal_abort_posture_basis",
            "sync_non_sync_posture_basis",
            "carrier_role_basis",
            "source_body_authority_basis",
            "non_claim_preservation_basis",
            "overread_prevention_basis",
            "scope_preservation_basis",
            "prior_boundary_preservation_basis",
            "closure_dependency",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key], key)
        for key in (
            "boundary_chain_conformance_only",
            "no_executed_operation_conformance_claim",
            "no_actual_operation_receipt_claim",
            "no_conformance_as_closure",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "non_claims_must_remain_false",
            "boundary_scopes_must_remain_bounded",
            "no_layer_overread_allowed",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(basis[key], key)

    def test_scope_checks_non_meaning_open_items_non_claims_and_summary(self) -> None:
        result = resolve(declared_request())
        scope = result["conformance_scope"]

        self.assertEqual(scope["selected_conformance_scope"], list(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_conformance_scope_supported"])
        for key in (
            "boundary_chain_conformance_only",
            "no_executed_operation_conformance_claim",
            "no_actual_operation_receipt_claim",
            "no_conformance_as_closure",
            "no_public_readiness_claim",
            "no_final_completion_claim",
            "non_claims_must_remain_false",
            "boundary_scopes_must_remain_bounded",
            "no_layer_overread_allowed",
            "closure_requires_separate_boundary",
        ):
            self.assertTrue(scope[key], key)

        checks = result["conformance_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        expected_check_names = {
            "conformance question declared",
            "conformance intent supported",
            "selected receipt / exhaustion result present",
            "selected receipt / exhaustion result outcome declared",
            "selected receipt / exhaustion result outcome recorded",
            "selected receipt / exhaustion result failed check count zero",
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
            "receipt / exhaustion boundary preserved",
            "receipt / exhaustion boundary-chain accounting only",
            "no actual operation receipt claimed",
            "no execution receipt claimed",
            "no output receipt claimed",
            "no action receipt claimed",
            "no consequence receipt claimed",
            "no executed-operation conformance already claimed",
            "no closure claimed",
            "no public readiness",
            "no final completion",
            "no follow-on work",
            "no reusable permission",
            "no autonomous continuation",
            "operation unexecuted",
            "output un-emitted",
            "action unauthorized",
            "consequence uncreated",
            "all required prior non-claims false",
            "no layer overread prior layer",
            "boundary scopes remained bounded",
            "closure dependency present",
            "conformance scope supported",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_check_names.issubset({c["check_name"] for c in checks}))

        non_meaning = result["conformance_non_meaning"]
        for key in (
            "executed_operation_conformance_claimed",
            "actual_operation_receipt_recorded",
            "operation_executed",
            "output_emitted",
            "action_authorized",
            "consequence_created",
            "operation_closed",
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
        self.assertTrue(non_claims["boundary_chain_conformance_recorded"])
        for key in (
            "executed_operation_conformance_claimed",
            "actual_operation_receipt_recorded",
            "closure_claimed",
            "public_launch_readiness_created",
            "final_completion_claimed",
        ):
            self.assertFalse(non_claims[key], key)

        summary = resolver.build_distributed_operation_conformance_summary(result)
        self.assertEqual(summary["outcome"], OUTCOME_RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["conformance_request_id"], "conformance-request-001")
        self.assertEqual(
            summary["selected_receipt_exhaustion_result_id"],
            "receipt-exhaustion-result-001",
        )
        self.assertEqual(
            summary["selected_receipt_exhaustion_result_outcome"],
            RECEIPT_OUTCOME_RECORDED,
        )
        self.assertEqual(summary["selected_operation_candidate_id"], "operation-candidate-001")
        self.assertEqual(summary["selected_operation_matter_id"], "operation-matter-001")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "conformance_boundary_recorded",
            "boundary_chain_conformance_recorded",
            "selected_receipt_exhaustion_result_preserved",
            "selected_receipt_exhaustion_result_recorded",
            "selected_receipt_exhaustion_result_failed_check_count_zero",
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
            "receipt_exhaustion_boundary_preserved",
            "receipt_exhaustion_boundary_chain_accounting_only",
            "no_actual_receipt_execution_receipt_output_receipt_action_receipt_consequence_receipt",
            "no_executed_operation_conformance",
            "no_closure",
            "no_public_readiness_final_completion_follow_on_work",
            "no_reusable_permission_autonomous_continuation",
            "operation_unexecuted",
            "output_un_emitted",
            "action_unauthorized",
            "consequence_uncreated",
            "all_required_prior_non_claims_preserved",
            "no_layer_overread_prior_layer",
            "boundary_scopes_remained_bounded",
            "closure_requires_separate_boundary",
            "conformance_scope_supported",
        ):
            self.assertTrue(summary[key], key)

    def test_requires_additional_basis_and_not_conformant_outcomes(self) -> None:
        additional_request = declared_request(
            requested_outcome=OUTCOME_REQUIRES_ADDITIONAL
        )
        additional_request["additional_basis_context"] = {
            "reason": "Conformance cannot yet be bounded without closure risk.",
            "missing_basis": [
                "non-claim preservation basis too generic",
                "overread prevention basis too generic",
            ],
        }
        additional_result = resolve(additional_request)
        self.assertEqual(additional_result["outcome"], OUTCOME_REQUIRES_ADDITIONAL)
        self.assertFalse(
            additional_result["non_claims"]["boundary_chain_conformance_recorded"]
        )
        self.assertTrue(
            additional_result["selected_receipt_exhaustion_result"][
                "selected_receipt_exhaustion_result"
            ]
        )
        self.assertTrue(
            additional_result["additional_basis_required"]["additional_basis_required"]
        )
        self.assertEqual(
            additional_result["additional_basis_required"]["additional_basis_context"],
            additional_request["additional_basis_context"],
        )
        for key in (
            "additional_basis_scheduled",
            "additional_basis_authorized",
            "additional_basis_executed",
            "additional_basis_creates_closure",
            "additional_basis_creates_public_readiness",
            "additional_basis_claims_final_completion",
            "additional_basis_creates_reusable_permission",
            "additional_basis_authorizes_autonomous_continuation",
            "additional_basis_schedules_follow_on_work",
        ):
            self.assertFalse(additional_result["additional_basis_required"][key], key)
        self.assert_no_conformance_closure_or_overcommit(
            additional_result["conformance_statement"]
        )

        not_conformant_request = declared_request(
            requested_outcome=OUTCOME_NOT_CONFORMANT
        )
        not_conformant_request["not_conformant_basis"] = {
            "reason": "Layer overread prior layer.",
            "failed_conformance_reason": "receipt boundary overread as closure",
        }
        not_conformant_result = resolve(not_conformant_request)
        self.assertEqual(not_conformant_result["outcome"], OUTCOME_NOT_CONFORMANT)
        self.assertFalse(
            not_conformant_result["non_claims"]["boundary_chain_conformance_recorded"]
        )
        self.assertEqual(
            not_conformant_result["not_conformant_basis"]["not_conformant_basis"],
            not_conformant_request["not_conformant_basis"],
        )
        self.assertTrue(not_conformant_result["not_conformant_basis"]["not_conformant"])
        for key in (
            "not_conformant_erases_boundary_chain",
            "not_conformant_mutates_prior_artifacts",
            "not_conformant_authorizes_repair",
            "not_conformant_authorizes_action",
            "not_conformant_executes_operation",
            "not_conformant_closes_operation",
            "not_conformant_schedules_follow_on_work",
        ):
            self.assertFalse(not_conformant_result["not_conformant_basis"][key], key)
        self.assert_no_conformance_closure_or_overcommit(
            not_conformant_result["conformance_statement"]
        )

        overread_request = declared_request()
        overread_selected = overread_request["selected_receipt_exhaustion_result"]
        assert isinstance(overread_selected, dict)
        overread_selected["receipt_exhaustion_statement"][
            "layer_overread_prior_layer"
        ] = True
        overread_result = resolve(overread_request)
        self.assertEqual(overread_result["outcome"], OUTCOME_NOT_CONFORMANT)
        self.assertIsNone(overread_result["block"]["block_code"])

        observed = {
            resolve(declared_request())["outcome"],
            additional_result["outcome"],
            not_conformant_result["outcome"],
            resolve(None)["outcome"],
        }
        self.assertEqual(
            observed,
            {
                OUTCOME_RECORDED,
                OUTCOME_REQUIRES_ADDITIONAL,
                OUTCOME_NOT_CONFORMANT,
                OUTCOME_BLOCKED,
            },
        )

    def test_request_builder_helper_records_valid_boundary(self) -> None:
        selected = selected_receipt_exhaustion_result()
        basis = conformance_basis(selected)
        with tempfile.TemporaryDirectory() as temp_dir:
            selected_path = Path(temp_dir) / "selected_receipt.json"
            selected_path.write_text(json.dumps(selected), encoding="utf-8")
            request = resolver.build_declared_distributed_operation_conformance_request(
                "builder-request-001",
                "Did the recorded distributed operation boundary chain conform?",
                selected,
                basis,
                list(SUPPORTED_SCOPE),
                selected_receipt_exhaustion_result_path=str(selected_path),
                selected_receipt_exhaustion_result_id="receipt-exhaustion-result-001",
                selected_receipt_exhaustion_result_outcome=RECEIPT_OUTCOME_RECORDED,
                closure_dependency={"closure_dependency_id": "builder-closure"},
                additional_basis_context={"not_used_for_recorded": False},
                not_conformant_basis={"not_used_for_recorded": False},
            )

            self.assertEqual(request["conformance_request_id"], "builder-request-001")
            self.assertEqual(
                request["conformance_question"],
                "Did the recorded distributed operation boundary chain conform?",
            )
            self.assertEqual(request["selected_receipt_exhaustion_result"], selected)
            self.assertEqual(request["conformance_basis"], basis)
            self.assertEqual(request["conformance_scope"], list(SUPPORTED_SCOPE))
            self.assertEqual(
                request["selected_receipt_exhaustion_result_path"], str(selected_path)
            )
            self.assertEqual(
                request["selected_receipt_exhaustion_result_id"],
                "receipt-exhaustion-result-001",
            )
            self.assertEqual(
                request["selected_receipt_exhaustion_result_outcome"],
                RECEIPT_OUTCOME_RECORDED,
            )
            self.assertEqual(
                request["closure_dependency"],
                {"closure_dependency_id": "builder-closure"},
            )
            self.assertEqual(
                request["additional_basis_context"],
                {"not_used_for_recorded": False},
            )
            self.assertEqual(
                request["not_conformant_basis"],
                {"not_used_for_recorded": False},
            )
            for key in REQUIRED_NON_CLAIMS:
                self.assertIs(request["declared_non_claims"][key], False, key)

            valid_request = (
                resolver.build_declared_distributed_operation_conformance_request(
                    "builder-valid-request-001",
                    "Did the recorded distributed operation boundary chain conform?",
                    selected,
                    basis,
                    list(SUPPORTED_SCOPE),
                    selected_receipt_exhaustion_result_id=(
                        "receipt-exhaustion-result-001"
                    ),
                    selected_receipt_exhaustion_result_outcome=(
                        RECEIPT_OUTCOME_RECORDED
                    ),
                    closure_dependency={"closure_dependency_id": "builder-closure"},
                    additional_basis_context={"not_used_for_recorded": False},
                )
            )
            result = resolve(valid_request)
            self.assert_recorded_core(result)

    def test_path_based_selected_receipt_result_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            selected_path = temp / "selected_receipt_result.json"
            selected_path.write_text(
                json.dumps(selected_receipt_exhaustion_result()),
                encoding="utf-8",
            )

            request = declared_request()
            request.pop("selected_receipt_exhaustion_result")
            request["selected_receipt_exhaustion_result_path"] = str(selected_path)
            result = resolve(request)
            self.assert_recorded_core(result)
            selected = result["selected_receipt_exhaustion_result"]
            self.assertEqual(
                selected["selected_receipt_exhaustion_result_path"],
                str(selected_path),
            )
            self.assertEqual(
                selected["selected_receipt_exhaustion_result_id"],
                "receipt-exhaustion-result-001",
            )
            self.assertEqual(
                selected["selected_receipt_exhaustion_result_outcome"],
                RECEIPT_OUTCOME_RECORDED,
            )

            request_path = temp / "declared_conformance_request.json"
            request_path.write_text(json.dumps(declared_request()), encoding="utf-8")
            path_result = resolver.resolve_distributed_operation_conformance_boundary_from_path(
                request_path
            )
            mapping_result = resolve(declared_request())
            self.assertEqual(path_result["outcome"], OUTCOME_RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_conformance_question"][
                    "conformance_request_path"
                ],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_deduplicates(self) -> None:
        result = resolve(declared_request())
        with tempfile.TemporaryDirectory() as temp_dir:
            explicit_path = Path(temp_dir) / "nested" / "result.json"
            written = resolver.write_distributed_operation_conformance_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            with patch.object(
                resolver,
                "DISTRIBUTED_OPERATION_CONFORMANCE_BOUNDARY_ROOT",
                Path(temp_dir) / "default-root",
            ):
                first = resolver.write_distributed_operation_conformance_result(result)
                second = resolver.write_distributed_operation_conformance_result(result)
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                self.assertEqual(first.parent, Path(temp_dir) / "default-root")
                self.assertEqual(second.parent, Path(temp_dir) / "default-root")
                self.assertIn("conformance-request-001", first.name)
                self.assertTrue(second.stem.endswith("_001"))
                self.assertNotIn("distributed_operation_receipt_exhaustion", str(first))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        original_request = copy.deepcopy(request)
        original_selected = copy.deepcopy(request["selected_receipt_exhaustion_result"])
        original_basis = copy.deepcopy(request["conformance_basis"])
        original_scope = copy.deepcopy(request["conformance_scope"])

        first = resolve(request)
        second = resolve(request)
        self.assertEqual(request, original_request)
        self.assertEqual(request["selected_receipt_exhaustion_result"], original_selected)
        self.assertEqual(request["conformance_basis"], original_basis)
        self.assertEqual(request["conformance_scope"], original_scope)
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            upstream_paths = []
            for name in (
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
            resolver.write_distributed_operation_conformance_result(
                first, temp / "new" / "result.json"
            )
            after = {path: path.read_text(encoding="utf-8") for path in upstream_paths}
            self.assertEqual(before, after)

    def test_explicit_missing_and_malformed_blocks(self) -> None:
        blocked = declared_request(
            intent="BLOCK_DISTRIBUTED_OPERATION_CONFORMANCE_REVIEW"
        )
        result = resolve(blocked)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(
            result["conformance_statement"][
                "distributed_operation_conformance_boundary_recorded"
            ]
        )

        missing = resolve(None)
        self.assertEqual(missing["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(missing), "CONFORMANCE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_distributed_operation_conformance_boundary(
            declared_conformance_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(malformed), "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            unreadable = resolver.resolve_distributed_operation_conformance_boundary_from_path(
                temp / "missing.json"
            )
            self.assertEqual(
                block_code(unreadable), "DECLARED_CONFORMANCE_REQUEST_UNREADABLE"
            )

            bad_json = temp / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = resolver.resolve_distributed_operation_conformance_boundary_from_path(
                bad_json
            )
            self.assertEqual(block_code(bad), "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

            array_json = temp / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = (
                resolver.resolve_distributed_operation_conformance_boundary_from_path(
                    array_json
                )
            )
            self.assertEqual(
                block_code(array_result), "DECLARED_CONFORMANCE_REQUEST_MALFORMED"
            )

            request = declared_request()
            request.pop("selected_receipt_exhaustion_result")
            request["selected_receipt_exhaustion_result_path"] = str(
                temp / "missing-selected.json"
            )
            self.assertEqual(
                block_code(resolve(request)), "RECEIPT_EXHAUSTION_RESULT_UNREADABLE"
            )

            malformed_selected_path = temp / "malformed-selected.json"
            malformed_selected_path.write_text("{bad", encoding="utf-8")
            request["selected_receipt_exhaustion_result_path"] = str(
                malformed_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "RECEIPT_EXHAUSTION_RESULT_MALFORMED"
            )

            array_selected_path = temp / "array-selected.json"
            array_selected_path.write_text("[]", encoding="utf-8")
            request["selected_receipt_exhaustion_result_path"] = str(
                array_selected_path
            )
            self.assertEqual(
                block_code(resolve(request)), "RECEIPT_EXHAUSTION_RESULT_MALFORMED"
            )

    def test_selected_receipt_result_issue_blocks(self) -> None:
        cases = (
            (("outcome",), None, "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING"),
            (
                ("outcome",),
                "DISTRIBUTED_OPERATION_RECEIPT_EXHAUSTION_NOT_READY",
                "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED",
            ),
            (
                ("receipt_exhaustion_statement", "failed_check_count"),
                1,
                "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS",
            ),
        )
        for path, value, expected_code in cases:
            selected = selected_receipt_exhaustion_result()
            if value is None:
                delete_path(selected, path)
                delete_path(selected, ("distributed_receipt_exhaustion_summary", "outcome"))
            else:
                set_path(selected, path, value)
                if path[-1] == "outcome":
                    selected["distributed_receipt_exhaustion_summary"]["outcome"] = value
                if path[-1] == "failed_check_count":
                    selected["distributed_receipt_exhaustion_summary"][
                        "failed_check_count"
                    ] = value
            request = declared_request(selected_receipt=selected)
            if value is None:
                request.pop("selected_receipt_exhaustion_result_outcome")
            elif path[-1] == "outcome":
                request["selected_receipt_exhaustion_result_outcome"] = value
            result = resolve(request)
            self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
            self.assertEqual(block_code(result), expected_code, expected_code)

    def test_missing_required_basis_blocks(self) -> None:
        missing_cases = (
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
        selected = request["selected_receipt_exhaustion_result"]
        assert isinstance(selected, dict)
        selected["selected_operation_context"] = {}
        receipt_basis = selected["receipt_exhaustion_basis"]
        assert isinstance(receipt_basis, dict)
        receipt_basis.pop("selected_operation_context", None)
        conf_basis = request["conformance_basis"]
        assert isinstance(conf_basis, dict)
        conf_basis.pop("selected_operation_context", None)
        self.assertEqual(
            block_code(resolve(request)), "ADMITTED_OPERATION_CONTEXT_MISSING"
        )

        request = declared_request()
        request.pop("conformance_scope")
        request["conformance_basis"].pop("declared_conformance_scope")
        self.assertEqual(block_code(resolve(request)), "CONFORMANCE_SCOPE_MISSING")

        request = declared_request()
        request.pop("closure_dependency", None)
        request["conformance_basis"].pop("closure_dependency", None)
        selected = request["selected_receipt_exhaustion_result"]
        assert isinstance(selected, dict)
        selected["receipt_exhaustion_basis"].pop("closure_dependency", None)
        selected["selected_operation_context"].pop("closure_dependency", None)
        self.assertEqual(block_code(resolve(request)), "CLOSURE_DEPENDENCY_MISSING")

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

    def test_unsupported_conformance_scope_blocks(self) -> None:
        request = declared_request()
        request["conformance_scope"] = list(SUPPORTED_SCOPE) + ["UNSUPPORTED_SCOPE"]
        result = resolve(request)
        self.assertEqual(result["outcome"], OUTCOME_BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_CONFORMANCE_SCOPE")

    def test_conformance_collapse_flags_block(self) -> None:
        cases = (
            (
                "executed_operation_conformance_claimed",
                "CONFORMANCE_REVIEW_CLAIMS_EXECUTED_OPERATION_CONFORMANCE",
            ),
            (
                "actual_operation_receipt_recorded",
                "CONFORMANCE_REVIEW_CLAIMS_ACTUAL_OPERATION_RECEIPT",
            ),
            ("closure_claimed", "CONFORMANCE_REVIEW_CLAIMS_CLOSURE"),
            (
                "public_launch_readiness_created",
                "CONFORMANCE_REVIEW_CREATES_PUBLIC_READINESS",
            ),
            (
                "final_completion_claimed",
                "CONFORMANCE_REVIEW_CLAIMS_FINAL_COMPLETION",
            ),
            (
                "follow_on_work_authorized",
                "CONFORMANCE_REVIEW_SCHEDULES_FOLLOW_ON_WORK",
            ),
            (
                "reusable_permission_created",
                "CONFORMANCE_REVIEW_CREATES_REUSABLE_PERMISSION",
            ),
            (
                "autonomous_continuation_authorized",
                "CONFORMANCE_REVIEW_AUTHORIZES_AUTONOMOUS_CONTINUATION",
            ),
            ("action_authorized", "CONFORMANCE_REVIEW_AUTHORIZES_ACTION"),
            ("consequence_created", "CONFORMANCE_REVIEW_CREATES_CONSEQUENCE"),
            ("operation_executed", "CONFORMANCE_REVIEW_EXECUTES_OPERATION"),
            ("output_emitted", "CONFORMANCE_REVIEW_EMITS_OUTPUT"),
            (
                "repository_synchronization_authorized",
                "CONFORMANCE_REVIEW_AUTHORIZES_SYNCHRONIZATION",
            ),
            (
                "non_synchronized_operation_authorized",
                "CONFORMANCE_REVIEW_AUTHORIZES_NON_SYNCHRONIZED_OPERATION",
            ),
            (
                "full_body_transfer_authorized",
                "CONFORMANCE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "CONFORMANCE_REVIEW_CREATES_SECOND_BODY"),
            ("refusal_abort_erased", "CONFORMANCE_REVIEW_ERASES_REFUSAL_ABORT"),
            ("evidence_erased", "CONFORMANCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "CONFORMANCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("blocked_attempt_erased", "CONFORMANCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            (
                "projection_mismatch_hidden",
                "CONFORMANCE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL",
            ),
            ("divergence_resolved", "CONFORMANCE_REVIEW_RESOLVES_DIVERGENCE"),
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
                "CONFORMANCE_REVIEW_AUTHORIZES_ACTION",
            },
        )


if __name__ == "__main__":
    unittest.main()
