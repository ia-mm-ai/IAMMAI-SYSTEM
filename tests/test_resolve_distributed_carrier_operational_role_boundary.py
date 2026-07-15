"""Bounded tests for distributed carrier operational role boundary.

These tests verify that carrier operational role review records carrier role
shapes as bounded context only. The resolver may record role basis, return not
sufficient, require additional basis, or block. It must not activate carrier
roles, assign live operation, create carrier authority/currentness, select
carriers, create hierarchy, admit, authorize, execute, synchronize, transfer a
body, create consequence, create public readiness, claim final completion, or
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

import resolve_distributed_carrier_operational_role_boundary as resolver


OUTCOME_RECORDED = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_RECORDED"
OUTCOME_NOT_SUFFICIENT = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS_NOT_SUFFICIENT"
OUTCOME_ADDITIONAL = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REVIEW_BLOCKED"
AUTHORITY_OUTCOME = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
ELIGIBILITY_OUTCOME = "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW"

TOP_LEVEL_SECTIONS = (
    "distributed_carrier_operational_role_metadata",
    "declared_role_question",
    "selected_source_body_authority_result",
    "selected_operation_matter",
    "carrier_role_basis",
    "carrier_role_shapes",
    "role_checks",
    "role_statement",
    "role_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_carrier_operational_role_summary",
)

ROLE_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS.keys())
AUTHORITY_NON_CLAIMS = tuple(resolver.SOURCE_BODY_AUTHORITY_NON_CLAIM_FIELDS)
SUPPORTED_ROLE_SHAPES = tuple(sorted(resolver.SUPPORTED_CARRIER_ROLE_SHAPES))


def false_claims(keys: tuple[str, ...]) -> dict[str, bool]:
    return {key: False for key in keys}


def operation_candidate() -> dict:
    return {
        "operation_candidate_id": "distributed_operation_candidate_001",
        "declared_operation_question": (
            "What carrier role shapes may be recognized as bounded context "
            "before any future operation admission?"
        ),
        "candidate_remains_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
    }


def operation_matter() -> dict:
    return {
        "operation_matter_id": "distributed_operation_matter_001",
        "selected_matter_id": "distributed_operation_matter_declaration_result_001",
        "matter_declaration_outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
        "matter_remains_declaration_only": True,
        "matter_not_upgraded_into_admission": True,
        "matter_not_upgraded_into_authorization": True,
        "matter_not_upgraded_into_operation": True,
    }


def operation_purpose() -> dict:
    return {
        "declared_operation_purpose": (
            "Review carrier role shapes as bounded context only for future "
            "admission / transition review."
        ),
        "purpose_is_not_permission": True,
        "purpose_is_not_operation_plan": True,
        "purpose_is_not_follow_on_work_authorization": True,
    }


def selected_matter_declaration() -> dict:
    return {
        "distributed_operation_matter_declaration_metadata": {
            "distributed_operation_matter_declaration_result_id": (
                "distributed_operation_matter_declaration_result_001"
            ),
            "resolver_module": "resolve_distributed_operation_matter_declaration",
        },
        "operation_candidate": operation_candidate(),
        "operation_matter": operation_matter(),
        "operation_purpose": operation_purpose(),
        "matter_declaration_statement": {
            "distributed_operation_matter_declared": True,
            "operation_candidate_preserved": True,
            "operation_matter_preserved": True,
            "operation_purpose_preserved": True,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "failed_check_count": 0,
        },
        "non_claims": {
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "continuation_authorized": False,
            "distributed_operation_authorized": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "source_replaced": False,
            "authority_created": False,
            "permission_created": False,
            "truth_created": False,
            "action_authorized": False,
            "consequence_created": False,
            "evidence_erased": False,
            "refusal_erased": False,
            "public_launch_readiness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
        },
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
    }


def selected_eligibility_result() -> dict:
    return {
        "distributed_operation_eligibility_metadata": {
            "distributed_operation_eligibility_result_id": (
                "distributed_operation_eligibility_result_001"
            ),
            "resolver_module": "resolve_distributed_operation_eligibility_boundary",
        },
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": operation_candidate(),
        "selected_operation_matter": operation_matter(),
        "eligibility_basis": {
            "selected_matter_declaration_result": selected_matter_declaration(),
            "selected_operation_candidate_identity": "distributed_operation_candidate_001",
            "selected_operation_question": operation_candidate()[
                "declared_operation_question"
            ],
            "selected_operation_purpose": operation_purpose()[
                "declared_operation_purpose"
            ],
            "selected_proposed_operation_kind": (
                "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE"
            ),
        },
        "eligibility_statement": {
            "distributed_operation_matter_eligible_for_review": True,
            "operation_candidate_preserved": True,
            "operation_matter_preserved": True,
            "operation_purpose_preserved": True,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "source_body_authority_decided": False,
            "carrier_roles_defined": False,
            "failed_check_count": 0,
        },
        "non_claims": {
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "source_body_authority_decided": False,
            "carrier_roles_defined": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "continuation_authorized": False,
            "distributed_operation_authorized": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "source_replaced": False,
            "authority_created": False,
            "permission_created": False,
            "truth_created": False,
            "action_authorized": False,
            "consequence_created": False,
            "evidence_erased": False,
            "refusal_erased": False,
            "public_launch_readiness_created": False,
            "final_completion_claimed": False,
            "follow_on_work_authorized": False,
        },
        "outcome": ELIGIBILITY_OUTCOME,
        "distributed_operation_eligibility_summary": {
            "outcome": ELIGIBILITY_OUTCOME,
            "operation_candidate_id": "distributed_operation_candidate_001",
            "operation_matter_id": "distributed_operation_matter_001",
            "operation_question": operation_candidate()["declared_operation_question"],
            "operation_purpose": operation_purpose()["declared_operation_purpose"],
            "proposed_operation_kind": (
                "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE"
            ),
            "failed_check_count": 0,
        },
    }


def carrier_context() -> dict:
    return {
        "carrier_b_success_context": {
            "carrier_id": "Carrier B",
            "success_is_evidence_context_only": True,
        },
        "carrier_c_block_context": {
            "carrier_id": "Carrier C",
            "block_is_evidence_context_only": True,
        },
        "b_c_divergence_context": {"divergence_visible": True},
        "refusal_blocked_attempt_context": {
            "refusal_visible": True,
            "blocked_attempts_visible": True,
        },
        "projection_mismatch_context": {"projection_mismatch_visible": True},
        "carrier_b_success_becomes_winner": False,
        "carrier_c_block_becomes_loser": False,
        "b_c_divergence_hidden": False,
        "refusal_hidden": False,
        "blocked_attempt_hidden": False,
        "projection_mismatch_hidden": False,
        "carrier_becomes_authority": False,
        "carrier_becomes_source": False,
        "carrier_becomes_current": False,
        "carrier_hierarchy_created": False,
    }


def source_body_authority_basis() -> dict:
    return {
        "source_body_authority_basis_id": "source_body_authority_basis_001",
        "source_body_lineage_basis": {
            "lineage_id": "source_body_lineage_001",
            "lineage_is_source_body_reference_only": True,
        },
        "source_body_authority_reference": {
            "authority_reference_id": "source_body_authority_reference_001",
            "authority_reference_is_not_authority_grant": True,
        },
        "selected_carrier_context": carrier_context(),
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_boundary_001",
            "distributed_standing_becomes_authority": False,
        },
        "source_body_authority_basis_is_not_authority_grant": True,
        "source_body_authority_basis_is_not_permission": True,
        "source_body_authority_basis_is_not_operation_admission": True,
        "source_body_authority_basis_is_not_operation_authorization": True,
        "source_body_authority_basis_is_not_execution": True,
    }


def selected_source_body_authority_result(**overrides: object) -> dict:
    result = {
        "source_body_operational_authority_metadata": {
            "source_body_operational_authority_result_id": (
                "source_body_operational_authority_result_001"
            ),
            "source_body_operational_authority_result_type": (
                "source_body_operational_authority_boundary_result"
            ),
            "source_body_operational_authority_result_version": "0.1.0",
            "resolver_module": "resolve_source_body_operational_authority_boundary",
        },
        "selected_eligibility_result": {
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_eligibility_result_id": "distributed_operation_eligibility_result_001",
            "selected_eligibility_result_outcome": ELIGIBILITY_OUTCOME,
            "selected_eligibility_result_failed_check_count_zero": True,
        },
        "selected_operation_matter": {
            "selected_eligibility_result": selected_eligibility_result(),
            "selected_matter_declaration": selected_matter_declaration(),
            "selected_operation_candidate": operation_candidate(),
            "selected_operation_matter": operation_matter(),
            "selected_operation_question": operation_candidate()[
                "declared_operation_question"
            ],
            "selected_operation_purpose": operation_purpose()[
                "declared_operation_purpose"
            ],
            "proposed_operation_kind": (
                "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE"
            ),
            "selected_operation_candidate_id": "distributed_operation_candidate_001",
            "selected_operation_matter_id": "distributed_operation_matter_001",
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
        },
        "source_body_authority_basis": source_body_authority_basis(),
        "authority_checks": [
            {
                "check_name": "source-body authority checks passed",
                "passed": True,
                "expected_posture": "basis recorded without authority grant",
                "actual_posture": "basis recorded without authority grant",
                "block_code": None,
                "failure_code": None,
            }
        ],
        "authority_statement": {
            "source_body_operational_authority_basis_recorded": True,
            "selected_eligibility_result_preserved": True,
            "selected_eligibility_result_eligible": True,
            "selected_eligibility_result_failed_check_count_zero": True,
            "selected_matter_declaration_preserved": True,
            "selected_operation_candidate_preserved": True,
            "selected_operation_matter_preserved": True,
            "source_body_lineage_basis_preserved": True,
            "source_body_authority_reference_preserved": True,
            "future_admission_transition_review_may_be_considered": True,
            "authority_granted": False,
            "authority_created": False,
            "permission_created": False,
            "operation_admitted": False,
            "operation_authorized": False,
            "operation_executed": False,
            "carrier_roles_defined": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "continuation_authorized": False,
            "distributed_operation_authorized": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "source_replaced": False,
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
            "failed_check_count": 0,
        },
        "non_claims": false_claims(AUTHORITY_NON_CLAIMS),
        "outcome": AUTHORITY_OUTCOME,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "source_body_operational_authority_summary": {
            "outcome": AUTHORITY_OUTCOME,
            "authority_request_id": "source_body_authority_request_001",
            "selected_eligibility_result_id": "distributed_operation_eligibility_result_001",
            "selected_operation_candidate_id": "distributed_operation_candidate_001",
            "selected_operation_matter_id": "distributed_operation_matter_001",
            "passed_check_count": 42,
            "failed_check_count": 0,
            "source_body_operational_authority_basis_recorded": True,
        },
    }
    for key, value in overrides.items():
        result[key] = value
    return result


def carrier_role_basis() -> dict:
    return {
        "source_body_authority_basis": source_body_authority_basis(),
        "source_body_lineage_basis": source_body_authority_basis()[
            "source_body_lineage_basis"
        ],
        "selected_carrier_context": carrier_context(),
        "carrier_b_success_context": carrier_context()["carrier_b_success_context"],
        "carrier_c_block_context": carrier_context()["carrier_c_block_context"],
        "b_c_divergence_context": carrier_context()["b_c_divergence_context"],
        "refusal_blocked_attempt_context": carrier_context()[
            "refusal_blocked_attempt_context"
        ],
        "projection_mismatch_context": carrier_context()["projection_mismatch_context"],
        "distributed_standing_basis": source_body_authority_basis()[
            "distributed_standing_basis"
        ],
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


def valid_role_request(
    *,
    authority_result: dict | None = None,
    basis: dict | None = None,
    role_shapes: list[str] | dict | None = None,
    intent: str = "RECORD_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS",
    requested_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: dict | None = None,
    not_sufficient_reason: str | None = None,
) -> dict:
    return {
        "role_request_id": "distributed_carrier_role_request_001",
        "role_question": (
            "What carrier role shapes may be recognized as bounded context "
            "before any future operation admission?"
        ),
        "role_intent": intent,
        "selected_source_body_authority_result": (
            authority_result if authority_result is not None else selected_source_body_authority_result()
        ),
        "carrier_role_basis": basis if basis is not None else carrier_role_basis(),
        "carrier_role_shapes": (
            role_shapes if role_shapes is not None else list(SUPPORTED_ROLE_SHAPES)
        ),
        "selected_source_body_authority_result_id": (
            "source_body_operational_authority_result_001"
        ),
        "selected_source_body_authority_result_outcome": AUTHORITY_OUTCOME,
        "expected_selected_authority_outcome": AUTHORITY_OUTCOME,
        "requested_role_outcome": requested_outcome,
        "selected_carrier_context": carrier_context(),
        "additional_basis_context": additional_basis_context,
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": false_claims(ROLE_NON_CLAIMS),
    }


def resolve(request: dict | None = None) -> dict:
    return resolver.resolve_distributed_carrier_operational_role_boundary(
        declared_role_request=request if request is not None else valid_role_request()
    )


class DistributedCarrierOperationalRoleBoundaryTests(unittest.TestCase):
    def assert_false_non_claims(self, result: dict) -> None:
        self.assertEqual(set(ROLE_NON_CLAIMS), set(result["non_claims"]))
        for key in ROLE_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

    def assert_no_role_or_operation_collapse(self, result: dict) -> None:
        statement = result["role_statement"]
        summary = result["distributed_carrier_operational_role_summary"]
        for key in (
            "carrier_roles_activated",
            "carrier_roles_assigned_for_operation",
            "carrier_authority_created",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
            "consequence_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(statement[key], False, key)
        self.assertIs(summary["carrier_roles_activated"], False)
        self.assertIs(summary["carrier_roles_assigned_for_operation"], False)
        self.assertIs(summary["carrier_authority_created"], False)
        self.assertIs(summary["carrier_currentness_created"], False)
        self.assertIs(summary["current_carrier_selected"], False)
        self.assertIs(summary["winning_carrier_selected"], False)
        self.assertIs(summary["losing_carrier_invalidated"], False)
        self.assertIs(summary["carrier_hierarchy_created"], False)
        self.assertIs(summary["operation_admitted"], False)
        self.assertIs(summary["operation_authorized"], False)
        self.assertIs(summary["operation_executed"], False)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation_distributed_operation"], True)
        self.assertIs(
            summary["no_consequence_public_readiness_final_completion_follow_on_work"],
            True,
        )

    def assert_block_code(self, request: dict, code: str) -> None:
        result = resolve(request)
        self.assertEqual(OUTCOME_BLOCKED, result["outcome"])
        self.assertEqual(code, result["block"]["block_code"])
        self.assert_false_non_claims(result)

    def test_successful_carrier_role_basis_recorded_result(self) -> None:
        request = valid_role_request()
        result = resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(OUTCOME_RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["distributed_carrier_operational_role_summary"]["failed_check_count"])

        metadata = result["distributed_carrier_operational_role_metadata"]
        self.assertTrue(metadata["distributed_carrier_operational_role_result_id"])
        self.assertTrue(metadata["distributed_carrier_operational_role_result_type"])
        self.assertEqual("0.1.0", metadata["distributed_carrier_operational_role_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            "resolve_distributed_carrier_operational_role_boundary",
            metadata["resolver_module"],
        )

        question = result["declared_role_question"]
        self.assertEqual("distributed_carrier_role_request_001", question["role_request_id"])
        self.assertEqual(request["role_question"], question["role_question"])
        self.assertEqual(
            "RECORD_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BASIS",
            question["role_intent"],
        )
        self.assertEqual(
            "source_body_operational_authority_result_001",
            question["selected_source_body_authority_result_id"],
        )
        self.assertEqual(
            AUTHORITY_OUTCOME,
            question["selected_source_body_authority_result_outcome"],
        )
        for key in (
            "role_boundary_is_not_role_activation",
            "role_boundary_is_not_carrier_authority",
            "role_boundary_is_not_carrier_currentness",
            "role_boundary_is_not_admission",
            "role_boundary_is_not_authorization",
            "role_boundary_is_not_execution",
        ):
            self.assertIs(question[key], True, key)

        selected_authority = result["selected_source_body_authority_result"]
        self.assertEqual(
            "source_body_operational_authority_result_001",
            selected_authority["selected_source_body_authority_result_id"],
        )
        self.assertEqual(
            AUTHORITY_OUTCOME,
            selected_authority["selected_source_body_authority_result_outcome"],
        )
        self.assertIs(
            selected_authority["selected_source_body_authority_result_outcome_is_recorded"],
            True,
        )
        self.assertIs(
            selected_authority[
                "selected_source_body_authority_result_failed_check_count_zero"
            ],
            True,
        )
        for key in (
            "selected_source_body_authority_result_remains_authority_basis_only",
            "selected_source_body_authority_result_did_not_grant_authority",
            "selected_source_body_authority_result_did_not_create_authority",
            "selected_source_body_authority_result_did_not_create_permission",
            "selected_source_body_authority_result_did_not_define_carrier_roles",
            "selected_source_body_authority_result_did_not_admit_operation",
            "selected_source_body_authority_result_did_not_authorize_operation",
            "selected_source_body_authority_result_did_not_execute_operation",
        ):
            self.assertIs(selected_authority[key], True, key)

        selected_matter = result["selected_operation_matter"]
        self.assertIn("selected_source_body_authority_result", selected_matter)
        self.assertIn("selected_eligibility_result", selected_matter)
        self.assertIn("selected_matter_declaration", selected_matter)
        self.assertEqual(
            "distributed_operation_candidate_001",
            selected_matter["selected_operation_candidate_id"],
        )
        self.assertEqual(
            "distributed_operation_matter_001",
            selected_matter["selected_operation_matter_id"],
        )
        self.assertTrue(selected_matter["selected_operation_question"])
        self.assertTrue(selected_matter["selected_operation_purpose"])
        self.assertTrue(selected_matter["proposed_operation_kind"])
        self.assertIs(selected_matter["source_body_authority_basis_remains_basis_only"], True)
        self.assertIs(selected_matter["matter_remains_declaration_only"], True)
        self.assertIs(selected_matter["candidate_remains_candidate_only"], True)
        self.assertIs(selected_matter["eligibility_remains_eligibility_only"], True)
        self.assertIs(selected_matter["operation_admitted"], False)
        self.assertIs(selected_matter["operation_authorized"], False)
        self.assertIs(selected_matter["operation_executed"], False)

        role_basis = result["carrier_role_basis"]
        self.assertTrue(role_basis["source_body_authority_basis"])
        self.assertTrue(role_basis["source_body_lineage_basis"])
        self.assertTrue(role_basis["selected_carrier_context"])
        self.assertTrue(role_basis["carrier_b_success_context"])
        self.assertTrue(role_basis["carrier_c_block_context"])
        self.assertTrue(role_basis["b_c_divergence_context"])
        self.assertTrue(role_basis["refusal_blocked_attempt_context"])
        self.assertTrue(role_basis["projection_mismatch_context"])
        self.assertTrue(role_basis["distributed_standing_basis"])
        self.assertIs(role_basis["distributed_standing_basis_is_basis_only"], True)
        for key in (
            "carrier_context_is_not_authority",
            "carrier_context_is_not_currentness",
            "carrier_context_is_not_source_replacement",
            "carrier_context_is_not_winner_loser_selection",
            "carrier_context_is_not_hierarchy",
            "carrier_context_is_not_operation_admission",
            "carrier_context_is_not_operation_authorization",
            "carrier_context_is_not_execution",
            "carrier_context_is_not_synchronization",
            "carrier_context_is_not_full_body_transfer",
            "carrier_context_is_not_continuation",
            "carrier_context_is_not_consequence",
        ):
            self.assertIs(role_basis[key], True, key)

        role_shapes = result["carrier_role_shapes"]
        self.assertEqual(set(SUPPORTED_ROLE_SHAPES), set(role_shapes["selected_carrier_role_shapes"]))
        self.assertEqual([], role_shapes["unsupported_carrier_role_shapes"])
        self.assertIs(role_shapes["all_selected_shapes_supported"], True)
        self.assertIs(role_shapes["role_shapes_are_context_only"], True)
        self.assertIs(role_shapes["role_shapes_are_not_active_operational_roles"], True)
        self.assertIs(role_shapes["role_shapes_do_not_create_authority"], True)
        self.assertIs(role_shapes["role_shapes_do_not_create_permission"], True)
        self.assertIs(role_shapes["role_shapes_do_not_select_current_carrier"], True)
        self.assertIs(role_shapes["role_shapes_do_not_select_winning_carrier"], True)
        self.assertIs(role_shapes["role_shapes_do_not_invalidate_losing_carrier"], True)
        self.assertIs(role_shapes["role_shapes_do_not_make_any_carrier_source"], True)
        self.assertIs(role_shapes["future_operational_role_requires_admission"], True)
        self.assertIs(role_shapes["role_activation_is_impossible_here"], True)

        check_names = {check["check_name"] for check in result["role_checks"]}
        for check in result["role_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertIs(check["passed"], True, check["check_name"])
        for expected_name in (
            "role question declared",
            "role intent supported",
            "selected source-body authority result present",
            "selected source-body authority result outcome declared",
            "selected source-body authority result outcome recorded",
            "selected source-body authority result failed check count zero",
            "selected eligibility result preserved",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "source-body authority basis remains basis only",
            "source-body authority result did not grant authority",
            "source-body authority result did not create authority",
            "source-body authority result did not create permission",
            "source-body authority result did not define carrier roles",
            "source-body authority result did not admit operation",
            "source-body authority result did not authorize operation",
            "source-body authority result did not execute operation",
            "selected carrier context present or explicitly not required",
            "selected carrier context parseable",
            "all selected carrier role shapes supported",
            "Carrier B success does not become winner role",
            "Carrier C block does not become loser role",
            "B/C divergence remains visible",
            "refusal and blocked attempts remain visible",
            "projection mismatch remains visible where supplied",
            "no carrier becomes authority",
            "no carrier becomes source",
            "no carrier becomes current",
            "no carrier hierarchy created",
            "no operation admitted",
            "no operation authorized",
            "no operation executed",
            "no repository synchronization authorized",
            "no full body transfer authorized",
            "no second body created",
            "no continuation authorized",
            "no distributed operation authorized",
            "no consequence created",
            "no public readiness/final completion/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false",
        ):
            self.assertIn(expected_name, check_names)

        additional = result["additional_basis_required"]
        self.assertIs(additional["additional_basis_required"], False)
        self.assertIs(additional["additional_basis_not_scheduled"], True)
        self.assertIs(additional["additional_basis_not_authorized"], True)
        self.assertIs(additional["additional_basis_not_executed"], True)

        statement = result["role_statement"]
        self.assertIs(statement["distributed_carrier_operational_role_basis_recorded"], True)
        self.assertIs(statement["selected_source_body_authority_result_preserved"], True)
        self.assertIs(statement["selected_source_body_authority_result_recorded"], True)
        self.assertIs(
            statement["selected_source_body_authority_result_failed_check_count_zero"],
            True,
        )
        self.assertIs(statement["selected_eligibility_result_preserved"], True)
        self.assertIs(statement["selected_matter_declaration_preserved"], True)
        self.assertIs(statement["selected_operation_candidate_preserved"], True)
        self.assertIs(statement["selected_operation_matter_preserved"], True)
        self.assertIs(statement["source_body_authority_basis_preserved"], True)
        self.assertIs(statement["carrier_role_shapes_preserved"], True)
        self.assertIs(statement["carrier_context_preserved"], True)
        self.assertIs(statement["carrier_role_shapes_supported"], True)
        self.assertIs(
            statement["future_admission_transition_may_later_review_role_activation"],
            True,
        )
        self.assert_no_role_or_operation_collapse(result)

        non_meaning = result["role_non_meaning"]
        for key in (
            "carrier_role_activated",
            "carrier_role_assigned_for_live_operation",
            "carrier_authority_created",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "source_replaced_by_carrier",
            "authority_created",
            "permission_created",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
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
            self.assertIs(non_meaning[key], True, key)

        remains_open = result["what_remains_open"]
        for key in (
            "synchronization_non_synchronization_boundary",
            "distributed_operation_admission_transition_authority",
            "distributed_refusal_and_abort_law",
            "distributed_execution_emission_boundary",
            "distributed_action_consequence_boundary",
            "distributed_operation_receipt_exhaustion",
            "distributed_operation_conformance",
            "distributed_operation_closure",
            "distributed_operation_itself",
            "repository_synchronization",
            "full_body_transfer",
            "second_body_creation",
            "current_self_orientation_v10",
            "public_launch_readiness",
            "final_governance",
            "final_continuity_completion",
            "final_system_identity",
        ):
            self.assertIn(key, remains_open)
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

        summary = resolver.build_distributed_carrier_operational_role_summary(result)
        self.assertEqual(OUTCOME_RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("distributed_carrier_role_request_001", summary["role_request_id"])
        self.assertEqual(request["role_question"], summary["role_question"])
        self.assertEqual(request["role_intent"], summary["role_intent"])
        self.assertEqual(
            "source_body_operational_authority_result_001",
            summary["selected_source_body_authority_result_id"],
        )
        self.assertEqual(AUTHORITY_OUTCOME, summary["selected_source_body_authority_result_outcome"])
        self.assertEqual("distributed_operation_candidate_001", summary["selected_operation_candidate_id"])
        self.assertEqual("distributed_operation_matter_001", summary["selected_operation_matter_id"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["distributed_carrier_operational_role_basis_recorded"], True)
        self.assertIs(summary["role_basis_not_sufficient"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["carrier_role_shapes_supported"], True)
        self.assertIs(
            summary["future_admission_transition_may_later_review_role_activation"],
            True,
        )
        self.assert_false_non_claims(result)

    def test_supported_role_shapes_and_unsupported_shape_block(self) -> None:
        for shape in SUPPORTED_ROLE_SHAPES:
            with self.subTest(shape=shape):
                request = valid_role_request(role_shapes=[shape])
                result = resolve(request)
                self.assertEqual(OUTCOME_RECORDED, result["outcome"])
                self.assertEqual([shape], result["carrier_role_shapes"]["selected_carrier_role_shapes"])
                self.assertIs(result["carrier_role_shapes"]["all_selected_shapes_supported"], True)
                self.assert_no_role_or_operation_collapse(result)

        request = valid_role_request(role_shapes=["ACTIVE_OPERATIONAL_CARRIER"])
        self.assert_block_code(request, "UNSUPPORTED_CARRIER_ROLE_SHAPE")

    def test_carrier_context_preservation(self) -> None:
        result = resolve()
        context = result["carrier_role_basis"]["selected_carrier_context"]
        self.assertIs(context["carrier_b_success_context"]["success_is_evidence_context_only"], True)
        self.assertIs(context["carrier_c_block_context"]["block_is_evidence_context_only"], True)
        self.assertIs(context["b_c_divergence_context"]["divergence_visible"], True)
        self.assertIs(context["refusal_blocked_attempt_context"]["refusal_visible"], True)
        self.assertIs(context["refusal_blocked_attempt_context"]["blocked_attempts_visible"], True)
        self.assertIs(context["projection_mismatch_context"]["projection_mismatch_visible"], True)

        checks = {check["check_name"]: check for check in result["role_checks"]}
        for name in (
            "Carrier B success does not become winner role",
            "Carrier C block does not become loser role",
            "B/C divergence remains visible",
            "refusal and blocked attempts remain visible",
            "projection mismatch remains visible where supplied",
            "no carrier becomes authority",
            "no carrier becomes source",
            "no carrier becomes current",
            "no carrier hierarchy created",
        ):
            self.assertIs(checks[name]["passed"], True, name)

    def test_requires_additional_basis_and_not_sufficient_results(self) -> None:
        additional_context = {
            "reason": "selected carrier evidence identities need sharper role basis",
            "selected_carrier_context_too_generic": True,
            "selected_carrier_evidence_identities_insufficiently_specific": True,
            "role_shapes_incomplete": True,
            "carrier_b_success_and_carrier_c_block_need_clearer_classification": True,
            "divergence_context_needs_stronger_role_preservation": True,
            "refusal_block_context_needs_stronger_role_preservation": True,
            "projection_mismatch_context_needs_stronger_role_preservation": True,
            "admission_transition_boundary_cannot_yet_inspect_role_activation_safely": True,
        }
        additional_result = resolve(
            valid_role_request(
                requested_outcome=OUTCOME_ADDITIONAL,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(OUTCOME_ADDITIONAL, additional_result["outcome"])
        self.assertIs(additional_result["role_statement"]["selected_source_body_authority_result_preserved"], True)
        self.assertEqual(
            additional_context,
            additional_result["additional_basis_required"]["additional_basis_context"],
        )
        self.assertIs(additional_result["additional_basis_required"]["additional_basis_required"], True)
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_not_scheduled"], True)
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_not_authorized"], True)
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_not_executed"], True)
        self.assert_no_role_or_operation_collapse(additional_result)
        self.assert_false_non_claims(additional_result)

        not_sufficient_reason = (
            "carrier context would imply authority if accepted as role basis"
        )
        not_sufficient_result = resolve(
            valid_role_request(
                requested_outcome=OUTCOME_NOT_SUFFICIENT,
                not_sufficient_reason=not_sufficient_reason,
            )
        )
        self.assertEqual(OUTCOME_NOT_SUFFICIENT, not_sufficient_result["outcome"])
        self.assertIs(not_sufficient_result["role_statement"]["selected_source_body_authority_result_preserved"], True)
        self.assertEqual(
            not_sufficient_reason,
            not_sufficient_result["role_statement"]["not_sufficient_reason"],
        )
        self.assert_no_role_or_operation_collapse(not_sufficient_result)
        self.assert_false_non_claims(not_sufficient_result)

    def test_result_level_non_claims_for_all_outcome_families(self) -> None:
        results = [
            resolve(valid_role_request()),
            resolve(valid_role_request(requested_outcome=OUTCOME_NOT_SUFFICIENT)),
            resolve(
                valid_role_request(
                    requested_outcome=OUTCOME_ADDITIONAL,
                    additional_basis_context={"reason": "role basis incomplete"},
                )
            ),
            resolver.resolve_distributed_carrier_operational_role_boundary(),
        ]
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assert_false_non_claims(result)

    def test_request_builder_helper(self) -> None:
        authority = selected_source_body_authority_result()
        basis = carrier_role_basis()
        context = carrier_context()
        additional_context = {"reason": "role relation needs clearer classification"}
        request = resolver.build_declared_distributed_carrier_operational_role_request(
            "role_request_from_helper_001",
            "What carrier role shapes may be recognized as bounded context?",
            authority,
            basis,
            ["SOURCE_BODY_REFERENCE_CONTEXT", "FUTURE_OPERATIONAL_ROLE_REQUIRES_ADMISSION"],
            selected_source_body_authority_result_id=(
                "source_body_operational_authority_result_001"
            ),
            selected_source_body_authority_result_outcome=AUTHORITY_OUTCOME,
            requested_role_outcome=OUTCOME_RECORDED,
            selected_carrier_context=context,
            additional_basis_context=additional_context,
            not_sufficient_reason="not used for recorded request",
        )
        self.assertEqual("role_request_from_helper_001", request["role_request_id"])
        self.assertIn("carrier_role_basis", request)
        self.assertEqual(
            ["SOURCE_BODY_REFERENCE_CONTEXT", "FUTURE_OPERATIONAL_ROLE_REQUIRES_ADMISSION"],
            request["carrier_role_shapes"],
        )
        self.assertEqual(context, request["selected_carrier_context"])
        self.assertEqual(additional_context, request["additional_basis_context"])
        for key in ROLE_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        request["additional_basis_context"] = None
        request["not_sufficient_reason"] = None
        result = resolve(request)
        self.assertEqual(OUTCOME_RECORDED, result["outcome"])

    def test_path_based_selected_source_body_authority_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            authority_path = Path(tmp) / "selected_authority.json"
            authority = selected_source_body_authority_result()
            authority_path.write_text(json.dumps(authority), encoding="utf-8")

            request = valid_role_request(authority_result=None)
            request.pop("selected_source_body_authority_result")
            request["selected_source_body_authority_result_path"] = str(authority_path)
            result = resolve(request)

            self.assertEqual(OUTCOME_RECORDED, result["outcome"])
            selected = result["selected_source_body_authority_result"]
            self.assertEqual(str(authority_path), selected["selected_source_body_authority_result_path"])
            self.assertEqual(
                "source_body_operational_authority_result_001",
                selected["selected_source_body_authority_result_id"],
            )
            self.assertEqual(AUTHORITY_OUTCOME, selected["selected_source_body_authority_result_outcome"])

    def test_path_based_role_request_and_write_helpers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = valid_role_request()
            request_path = tmp_path / "role_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolver.resolve_distributed_carrier_operational_role_boundary_from_path(
                request_path
            )
            mapping_result = resolve(request)
            self.assertEqual(OUTCOME_RECORDED, path_result["outcome"])
            self.assertEqual(set(TOP_LEVEL_SECTIONS), set(path_result.keys()))
            self.assertEqual(
                mapping_result["outcome"],
                path_result["outcome"],
            )
            self.assertEqual(
                str(request_path),
                path_result["declared_role_question"]["role_request_path"],
            )

            output_path = tmp_path / "nested" / "role_result.json"
            written_path = resolver.write_distributed_carrier_operational_role_result(
                path_result, output_path
            )
            self.assertEqual(output_path, written_path)
            parsed = json.loads(written_path.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            root = tmp_path / "default_role_root"
            with patch.object(
                resolver, "DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_BOUNDARY_ROOT", root
            ):
                first = resolver.write_distributed_carrier_operational_role_result(path_result)
                second = resolver.write_distributed_carrier_operational_role_result(path_result)
            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertNotIn(
                "integrity_host_v0_min_coexistence_source_body_operational_authority_boundary",
                str(first),
            )
            self.assertTrue(first.name.endswith(".json"))

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            authority_path = Path(tmp) / "authority.json"
            authority = selected_source_body_authority_result()
            authority_path.write_text(json.dumps(authority, sort_keys=True), encoding="utf-8")
            before_file = authority_path.read_text(encoding="utf-8")

            request = valid_role_request(authority_result=authority)
            request["selected_source_body_authority_result_path"] = str(authority_path)
            request_before = copy.deepcopy(request)
            authority_before = copy.deepcopy(authority)
            basis_before = copy.deepcopy(request["carrier_role_basis"])
            shapes_before = copy.deepcopy(request["carrier_role_shapes"])
            context_before = copy.deepcopy(request["selected_carrier_context"])

            first = resolve(request)
            second = resolve(request)

            self.assertEqual(request_before, request)
            self.assertEqual(authority_before, authority)
            self.assertEqual(basis_before, request["carrier_role_basis"])
            self.assertEqual(shapes_before, request["carrier_role_shapes"])
            self.assertEqual(context_before, request["selected_carrier_context"])
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(before_file, authority_path.read_text(encoding="utf-8"))

            output_path = Path(tmp) / "role_result.json"
            resolver.write_distributed_carrier_operational_role_result(first, output_path)
            self.assertEqual(before_file, authority_path.read_text(encoding="utf-8"))

    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        blocked = resolve(
            valid_role_request(
                intent="BLOCK_DISTRIBUTED_CARRIER_OPERATIONAL_ROLE_REVIEW"
            )
        )
        self.assertEqual(OUTCOME_BLOCKED, blocked["outcome"])
        self.assertEqual(
            "ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
            blocked["block"]["block_code"],
        )
        self.assertIs(blocked["role_statement"]["distributed_carrier_operational_role_basis_recorded"], False)

        missing = resolver.resolve_distributed_carrier_operational_role_boundary()
        self.assertEqual(OUTCOME_BLOCKED, missing["outcome"])
        self.assertEqual("ROLE_QUESTION_UNDECLARED", missing["block"]["block_code"])

        malformed = resolver.resolve_distributed_carrier_operational_role_boundary(
            declared_role_request=["not", "a", "mapping"]
        )
        self.assertEqual(OUTCOME_BLOCKED, malformed["outcome"])
        self.assertEqual("DECLARED_ROLE_REQUEST_MALFORMED", malformed["block"]["block_code"])

    def test_role_request_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_distributed_carrier_operational_role_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(OUTCOME_BLOCKED, missing["outcome"])
            self.assertEqual("DECLARED_ROLE_REQUEST_UNREADABLE", missing["block"]["block_code"])

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_distributed_carrier_operational_role_boundary_from_path(
                malformed_path
            )
            self.assertEqual(OUTCOME_BLOCKED, malformed["outcome"])
            self.assertEqual("DECLARED_ROLE_REQUEST_MALFORMED", malformed["block"]["block_code"])

            array_path = tmp_path / "array.json"
            array_path.write_text(json.dumps([valid_role_request()]), encoding="utf-8")
            array_result = resolver.resolve_distributed_carrier_operational_role_boundary_from_path(
                array_path
            )
            self.assertEqual(OUTCOME_BLOCKED, array_result["outcome"])
            self.assertEqual("DECLARED_ROLE_REQUEST_MALFORMED", array_result["block"]["block_code"])

    def test_selected_source_body_authority_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = valid_role_request()
            request.pop("selected_source_body_authority_result")
            request["selected_source_body_authority_result_path"] = str(
                tmp_path / "missing_authority.json"
            )
            self.assert_block_code(request, "SOURCE_BODY_AUTHORITY_RESULT_UNREADABLE")

            malformed_path = tmp_path / "malformed_authority.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            request["selected_source_body_authority_result_path"] = str(malformed_path)
            self.assert_block_code(request, "SOURCE_BODY_AUTHORITY_RESULT_MALFORMED")

            array_path = tmp_path / "array_authority.json"
            array_path.write_text(json.dumps([selected_source_body_authority_result()]), encoding="utf-8")
            request["selected_source_body_authority_result_path"] = str(array_path)
            self.assert_block_code(request, "SOURCE_BODY_AUTHORITY_RESULT_MALFORMED")

    def test_selected_source_body_authority_result_issue_blocks(self) -> None:
        missing_outcome = selected_source_body_authority_result()
        missing_outcome.pop("outcome")
        missing_outcome["source_body_operational_authority_summary"].pop("outcome")
        self.assert_block_code(
            valid_role_request(authority_result=missing_outcome),
            "SOURCE_BODY_AUTHORITY_RESULT_OUTCOME_MISSING",
        )

        wrong_outcome = selected_source_body_authority_result()
        wrong_outcome["outcome"] = "SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW_BLOCKED"
        wrong_outcome["source_body_operational_authority_summary"]["outcome"] = (
            "SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW_BLOCKED"
        )
        self.assert_block_code(
            valid_role_request(authority_result=wrong_outcome),
            "SOURCE_BODY_AUTHORITY_RESULT_NOT_RECORDED",
        )

        failed = selected_source_body_authority_result()
        failed["source_body_operational_authority_summary"]["failed_check_count"] = 1
        self.assert_block_code(
            valid_role_request(authority_result=failed),
            "SOURCE_BODY_AUTHORITY_RESULT_HAS_FAILED_CHECKS",
        )

    def test_missing_required_selected_basis_blocks(self) -> None:
        cases: list[tuple[str, dict]] = []

        missing_eligibility = selected_source_body_authority_result()
        missing_eligibility.pop("selected_eligibility_result")
        missing_eligibility["selected_operation_matter"].pop("selected_eligibility_result")
        cases.append(("SELECTED_ELIGIBILITY_RESULT_MISSING", missing_eligibility))

        missing_declaration = selected_source_body_authority_result()
        missing_declaration["selected_operation_matter"].pop("selected_matter_declaration")
        missing_declaration["selected_eligibility_result"]["selected_eligibility_result"].pop(
            "selected_matter_declaration"
        )
        missing_declaration["selected_eligibility_result"]["selected_eligibility_result"][
            "eligibility_basis"
        ].pop("selected_matter_declaration_result")
        cases.append(("SELECTED_MATTER_DECLARATION_MISSING", missing_declaration))

        missing_candidate = selected_source_body_authority_result()
        missing_candidate["selected_operation_matter"].pop("selected_operation_candidate")
        missing_candidate["selected_eligibility_result"]["selected_eligibility_result"].pop(
            "selected_operation_candidate"
        )
        missing_candidate["selected_eligibility_result"]["selected_eligibility_result"][
            "eligibility_basis"
        ].pop("selected_operation_candidate_identity")
        cases.append(("SELECTED_OPERATION_CANDIDATE_MISSING", missing_candidate))

        missing_matter = selected_source_body_authority_result()
        missing_matter["selected_operation_matter"].pop("selected_operation_matter")
        missing_matter["selected_eligibility_result"]["selected_eligibility_result"].pop(
            "selected_operation_matter"
        )
        cases.append(("SELECTED_OPERATION_MATTER_MISSING", missing_matter))

        for expected_code, authority in cases:
            with self.subTest(expected_code=expected_code):
                self.assert_block_code(
                    valid_role_request(authority_result=authority),
                    expected_code,
                )

        missing_basis_authority = selected_source_body_authority_result()
        missing_basis_authority.pop("source_body_authority_basis")
        basis_without_source = carrier_role_basis()
        basis_without_source.pop("source_body_authority_basis")
        request = valid_role_request(
            authority_result=missing_basis_authority,
            basis=basis_without_source,
        )
        request.pop("source_body_authority_basis", None)
        self.assert_block_code(request, "SOURCE_BODY_AUTHORITY_BASIS_MISSING")

    def test_carrier_context_malformed_blocks(self) -> None:
        request = valid_role_request()
        request["selected_carrier_context"] = "not a mapping or sequence"
        request["carrier_role_basis"]["selected_carrier_context"] = None
        self.assert_block_code(request, "SELECTED_CARRIER_CONTEXT_MALFORMED")

    def test_role_collapse_flags_block(self) -> None:
        collapse_cases = (
            ("carrier_role_activated", "ROLE_REVIEW_ACTIVATES_CARRIER_ROLE"),
            ("carrier_role_assigned_for_operation", "ROLE_REVIEW_ASSIGNS_LIVE_OPERATION"),
            ("carrier_authority_created", "ROLE_REVIEW_CREATES_CARRIER_AUTHORITY"),
            ("carrier_currentness_created", "ROLE_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "ROLE_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "ROLE_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "ROLE_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("carrier_hierarchy_created", "ROLE_REVIEW_CREATES_CARRIER_HIERARCHY"),
            ("source_replaced", "ROLE_REVIEW_REPLACES_SOURCE"),
            ("operation_admitted", "ROLE_REVIEW_ADMITS_OPERATION"),
            ("operation_authorized", "ROLE_REVIEW_AUTHORIZES_OPERATION"),
            ("operation_executed", "ROLE_REVIEW_EXECUTES_OPERATION"),
            (
                "repository_synchronization_authorized",
                "ROLE_REVIEW_AUTHORIZES_REPOSITORY_SYNC",
            ),
            ("full_body_transfer_authorized", "ROLE_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "ROLE_REVIEW_CREATES_SECOND_BODY"),
            ("continuation_authorized", "ROLE_REVIEW_AUTHORIZES_CONTINUATION"),
            ("truth_created", "ROLE_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("action_authorized", "ROLE_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "ROLE_REVIEW_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "ROLE_REVIEW_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "ROLE_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "ROLE_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "ROLE_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "ROLE_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for field, expected_code in collapse_cases:
            with self.subTest(field=field):
                request = valid_role_request()
                request[field] = True
                request["carrier_role_shapes"] = ["UNSUPPORTED_ROLE_SHAPE_FOR_TRIGGER"]
                self.assert_block_code(request, expected_code)

    def test_mutation_replay_merge_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = valid_role_request()
                request[field] = True
                request["carrier_role_shapes"] = ["UNSUPPORTED_ROLE_SHAPE_FOR_TRIGGER"]
                self.assert_block_code(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = valid_role_request()
        missing["declared_non_claims"].pop("carrier_role_activated")
        self.assert_block_code(missing, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = valid_role_request()
        flipped["declared_non_claims"]["carrier_role_activated"] = True
        result = resolve(flipped)
        self.assertEqual(OUTCOME_BLOCKED, result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "ROLE_REVIEW_ACTIVATES_CARRIER_ROLE"},
        )


if __name__ == "__main__":
    unittest.main()
