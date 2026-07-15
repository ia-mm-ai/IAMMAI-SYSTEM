"""Bounded tests for distributed operation eligibility boundary.

These tests verify that eligibility reviews one declared matter only. The
resolver may decide whether the matter is eligible for future admission or
authority review, requires additional basis, is not eligible, or is blocked.
It must not admit, authorize, execute, synchronize, transfer, continue, decide
authority or carrier roles, create consequence, or schedule follow-on work.
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

import resolve_distributed_operation_eligibility_boundary as resolver


OUTCOME_ELIGIBLE = "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW"
OUTCOME_NOT_ELIGIBLE = "DISTRIBUTED_OPERATION_MATTER_NOT_ELIGIBLE_FOR_REVIEW"
OUTCOME_ADDITIONAL = "DISTRIBUTED_OPERATION_MATTER_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "DISTRIBUTED_OPERATION_ELIGIBILITY_BLOCKED"

MATTER_OUTCOME_DECLARED = "DISTRIBUTED_OPERATION_MATTER_DECLARED"
MATTER_INTENT_DECLARE = "DECLARE_DISTRIBUTED_OPERATION_MATTER"

REQUIRED_NON_CLAIMS = (
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "source_body_authority_decided",
    "carrier_roles_defined",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replaced",
    "authority_created",
    "permission_created",
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
    "self_orientation_successor_scheduled",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

MATTER_NON_CLAIMS = REQUIRED_NON_CLAIMS + ("eligibility_decided",)

TOP_LEVEL_SECTIONS = (
    "distributed_operation_eligibility_metadata",
    "declared_eligibility_question",
    "selected_matter_declaration",
    "selected_operation_candidate",
    "selected_operation_matter",
    "eligibility_basis",
    "eligibility_checks",
    "eligibility_statement",
    "eligibility_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_operation_eligibility_summary",
)


def eligibility_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def matter_non_claims() -> dict[str, bool]:
    return {key: False for key in MATTER_NON_CLAIMS}


def operation_candidate_section() -> dict:
    return {
        "operation_candidate_id": "distributed_operation_candidate_001",
        "declared_operation_question": (
            "Should this bounded distributed operation candidate be reviewed "
            "for future eligibility?"
        ),
        "candidate_visible_as_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
        "candidate_not_eligible_by_declaration": True,
        "candidate_not_scheduled_for_operation": True,
    }


def operation_matter_section() -> dict:
    return {
        "operation_matter_id": "distributed_operation_matter_001",
        "operation_candidate_id": "distributed_operation_candidate_001",
        "relation_to_operation_candidate": "declares one bounded matter for the selected candidate",
        "declared_matter_question": "Has one distributed operation candidate been declared as a bounded matter?",
        "declared_matter_scope": {
            "one_bounded_matter_only": True,
            "candidate_count": 1,
        },
        "one_bounded_matter_only": True,
        "matter_declaration_is_not_eligibility": True,
        "matter_declaration_is_not_admission": True,
        "matter_declaration_is_not_operation": True,
        "matter_declaration_is_not_execution": True,
        "matter_declaration_is_not_permission": True,
    }


def operation_purpose_section() -> dict:
    return {
        "declared_operation_purpose": (
            "Review whether one declared matter is sufficiently bounded for "
            "a future admission or authority boundary."
        ),
        "purpose_is_not_permission": True,
        "purpose_is_not_operation_plan": True,
        "purpose_is_not_output_authorization": True,
        "purpose_is_not_follow_on_work_authorization": True,
    }


def selected_operation_basis_value() -> dict:
    return {
        "source_body_basis": {
            "basis_id": "source_body_basis_001",
            "basis_type": "current_source_body_line",
            "source_body_basis_present": True,
        },
        "current_body_conformance_v4_closure_basis": {
            "basis_id": "current_body_conformance_v4_closure_001",
            "outcome": "CURRENT_BODY_CONFORMANCE_V4_CLOSED",
            "operation_authorized": False,
        },
        "current_self_orientation_v9_basis": {
            "basis_id": "current_self_orientation_v9_001",
            "outcome": "CURRENT_SELF_ORIENTATION_V9_RECORDED",
            "operation_authorized": False,
        },
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_boundary_conformance_closure_001",
            "outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED",
            "operation_authorized": False,
        },
        "reference_grounding": {
            "read_only_reference_grounding": True,
        },
        "basis_is_not_permission": True,
        "basis_is_not_admission": True,
        "basis_is_not_operation_plan": True,
        "basis_is_not_synchronization_plan": True,
        "basis_is_not_full_body_transfer_plan": True,
        "basis_is_not_final_governance": True,
    }


def selected_carrier_context_value() -> dict:
    return {
        "carrier_b_success_evidence_context_only": True,
        "carrier_c_block_evidence_context_only": True,
        "b_c_divergence_visible_context_only": True,
        "refusal_and_blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible": True,
        "selected_carriers_are_context_not_operational_participants": True,
        "no_current_carrier_selected": True,
        "no_winning_carrier_selected": True,
        "no_losing_carrier_invalidated": True,
        "no_carrier_currentness_created": True,
        "carriers": [
            {"carrier_id": "Carrier B", "posture": "success evidence only"},
            {"carrier_id": "Carrier C", "posture": "block evidence only"},
        ],
    }


def proposed_affected_surfaces_value() -> list[str]:
    return [
        "distributed_operation_matter_declaration",
        "current_body_conformance_v4_closure",
        "distributed_standing_boundary_conformance_closure",
    ]


def proposed_output_family_value() -> list[str]:
    return ["DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_RESULT"]


def eligibility_review_request_value() -> dict:
    return {
        "requested_future_eligibility_review": True,
        "eligibility_not_decided": True,
        "eligibility_review_not_scheduled": True,
        "eligibility_review_not_authorized_by_declaration": True,
        "eligibility_boundary_remains_open": True,
        "declaration_is_only_prerequisite_visibility": True,
    }


def refusal_abort_awareness_value() -> dict:
    return {
        "operation_may_later_be_blocked": True,
        "eligibility_may_fail": True,
        "carrier_refusal_must_remain_visible": True,
        "future_admission_must_include_abort_refusal_conditions": True,
        "no_operation_without_later_refusal_abort_boundary": True,
        "abort_refusal_is_not_late_cleanup": True,
        "refusal_abort_awareness_is_not_abort_mechanism": True,
        "refusal_abort_awareness_is_not_admission": True,
        "refusal_abort_awareness_is_not_operation": True,
    }


def selected_matter_declaration(**overrides: object) -> dict:
    statement = {
        "distributed_operation_matter_declared": True,
        "operation_candidate_preserved": True,
        "operation_matter_preserved": True,
        "operation_purpose_preserved": True,
        "proposed_operation_kind_preserved": True,
        "selected_operation_basis_preserved": True,
        "selected_carrier_context_preserved": True,
        "proposed_affected_surfaces_preserved": True,
        "proposed_output_family_preserved": True,
        "eligibility_review_request_preserved": True,
        "refusal_abort_awareness_preserved": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "eligibility_decided": False,
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
        "divergence_resolved": False,
        "evidence_erased": False,
        "refusal_erased": False,
        "blocked_attempt_erased": False,
        "projection_mismatch_hidden": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "failed_check_count": 0,
    }
    summary = {
        "outcome": MATTER_OUTCOME_DECLARED,
        "matter_declaration_request_id": "distributed_operation_matter_declaration_request_001",
        "matter_declaration_question": "Has one distributed operation candidate been declared as a bounded matter?",
        "matter_declaration_intent": MATTER_INTENT_DECLARE,
        "operation_candidate_id": "distributed_operation_candidate_001",
        "operation_matter_id": "distributed_operation_matter_001",
        "operation_question": operation_candidate_section()["declared_operation_question"],
        "operation_purpose": operation_purpose_section()["declared_operation_purpose"],
        "proposed_operation_kind": "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
        "passed_check_count": 45,
        "failed_check_count": 0,
        "distributed_operation_matter_declared": True,
        "operation_candidate_preserved": True,
        "operation_matter_preserved": True,
        "operation_purpose_preserved": True,
        "proposed_operation_kind_preserved": True,
        "selected_operation_basis_preserved": True,
        "selected_carrier_context_preserved": True,
        "proposed_affected_surfaces_preserved": True,
        "proposed_output_family_preserved": True,
        "eligibility_review_request_preserved": True,
        "refusal_abort_awareness_preserved": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "eligibility_decided": False,
        "no_sync_full_body_transfer_second_body": True,
        "no_continuation_distributed_operation": True,
        "no_carrier_currentness_current_winning_losing_carrier": True,
        "no_source_authority_permission_truth_action_consequence": True,
        "no_public_readiness_final_completion_follow_on_work": True,
        "key_non_claims": matter_non_claims(),
    }
    matter = {
        "distributed_operation_matter_declaration_metadata": {
            "distributed_operation_matter_declaration_result_id": "distributed_operation_matter_declaration_result_001",
            "distributed_operation_matter_declaration_result_type": "distributed_operation_matter_declaration_result",
            "distributed_operation_matter_declaration_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_operation_matter_declaration",
        },
        "declared_matter_question": {
            "matter_declaration_request_id": "distributed_operation_matter_declaration_request_001",
            "matter_declaration_question": "Has one distributed operation candidate been declared as a bounded matter?",
            "matter_declaration_intent": MATTER_INTENT_DECLARE,
            "declared_non_claims": matter_non_claims(),
        },
        "operation_candidate": operation_candidate_section(),
        "operation_matter": operation_matter_section(),
        "operation_purpose": operation_purpose_section(),
        "proposed_operation_kind": {
            "proposed_operation_kind": "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
            "kind_is_supported": True,
            "kind_is_candidate_kind_only": True,
            "kind_is_not_authorization": True,
            "kind_is_not_admission": True,
            "kind_is_not_execution": True,
            "kind_is_not_operation": True,
        },
        "selected_operation_basis": {
            "selected_operation_basis": selected_operation_basis_value(),
            **selected_operation_basis_value(),
        },
        "selected_carrier_context": {
            "selected_carrier_context": selected_carrier_context_value(),
            **selected_carrier_context_value(),
        },
        "proposed_affected_surfaces": {
            "proposed_affected_surfaces": proposed_affected_surfaces_value(),
            "declared_affected_surfaces": proposed_affected_surfaces_value(),
            "affected_surfaces_are_proposed_only": True,
            "no_surface_is_mutated": True,
            "no_surface_is_synchronized": True,
            "no_surface_is_transferred": True,
            "no_surface_is_executed": True,
            "no_output_is_emitted_by_declaration": True,
        },
        "proposed_output_family": {
            "proposed_output_family": proposed_output_family_value(),
            "declared_proposed_output_family": proposed_output_family_value(),
            "output_family_is_named_only": True,
            "output_family_is_not_authorized": True,
            "output_family_is_not_emitted": True,
            "output_family_does_not_create_consequence": True,
            "output_family_does_not_authorize_future_outputs": True,
        },
        "eligibility_review_request": {
            "eligibility_review_request": eligibility_review_request_value(),
            **eligibility_review_request_value(),
        },
        "refusal_abort_awareness": {
            "refusal_abort_awareness": refusal_abort_awareness_value(),
            **refusal_abort_awareness_value(),
        },
        "matter_declaration_checks": [
            {
                "check_name": "matter declaration checks passed",
                "passed": True,
                "expected_posture": "matter declared without operation",
                "actual_posture": "matter declared without operation",
                "block_code": None,
            }
        ],
        "matter_declaration_statement": statement,
        "non_claims": matter_non_claims(),
        "outcome": MATTER_OUTCOME_DECLARED,
        "block": {"code": None, "reason": None},
        "distributed_operation_matter_declaration_summary": summary,
    }
    for key, value in overrides.items():
        matter[key] = value
    return matter


def eligibility_basis_value() -> dict:
    basis = selected_operation_basis_value()
    return {
        "eligibility_basis_id": "distributed_operation_eligibility_basis_001",
        "selected_matter_declaration_id": "distributed_operation_matter_declaration_result_001",
        "selected_operation_candidate_identity": "distributed_operation_candidate_001",
        "selected_operation_question": operation_candidate_section()["declared_operation_question"],
        "selected_operation_purpose": operation_purpose_section()["declared_operation_purpose"],
        "selected_proposed_operation_kind": "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
        "selected_operation_basis": basis,
        "selected_carrier_context": selected_carrier_context_value(),
        "selected_proposed_affected_surfaces": proposed_affected_surfaces_value(),
        "selected_proposed_output_family": proposed_output_family_value(),
        "selected_eligibility_review_request": eligibility_review_request_value(),
        "selected_refusal_abort_awareness": refusal_abort_awareness_value(),
        "current_body_conformance_v4_closure_basis": basis["current_body_conformance_v4_closure_basis"],
        "current_self_orientation_v9_basis": basis["current_self_orientation_v9_basis"],
        "distributed_standing_basis": basis["distributed_standing_basis"],
        "source_body_basis": basis["source_body_basis"],
        "eligibility_basis_is_not_permission": True,
        "eligibility_basis_is_not_admission": True,
        "eligibility_basis_is_not_operation_plan": True,
        "eligibility_basis_is_not_synchronization_plan": True,
        "eligibility_basis_is_not_full_body_transfer_plan": True,
    }


def valid_eligibility_request(
    *,
    selected_matter: dict | None = None,
    intent: str = "RECORD_DISTRIBUTED_OPERATION_ELIGIBILITY",
    requested_outcome: str = OUTCOME_ELIGIBLE,
    additional_basis_context: dict | None = None,
    not_eligible_reason: str | None = None,
) -> dict:
    matter = selected_matter if selected_matter is not None else selected_matter_declaration()
    request = {
        "eligibility_request_id": "distributed_operation_eligibility_request_001",
        "eligibility_question": "Is the declared distributed operation matter eligible for future admission/authority review?",
        "eligibility_intent": intent,
        "selected_matter_declaration": matter,
        "selected_matter_declaration_id": "distributed_operation_matter_declaration_result_001",
        "selected_matter_declaration_outcome": MATTER_OUTCOME_DECLARED,
        "expected_selected_matter_declaration_outcome": MATTER_OUTCOME_DECLARED,
        "eligibility_basis": eligibility_basis_value(),
        "requested_eligibility_outcome": requested_outcome,
        "declared_non_claims": eligibility_non_claims(),
    }
    if additional_basis_context is not None:
        request["additional_basis_context"] = additional_basis_context
    if not_eligible_reason is not None:
        request["not_eligible_reason"] = not_eligible_reason
    return request


def failed_codes(result: dict) -> set[str | None]:
    codes: set[str | None] = set()
    for check in result.get("eligibility_checks", []):
        if not check.get("passed"):
            codes.add(check.get("block_code") or check.get("failure_code"))
    block = result.get("block", {})
    if block.get("code"):
        codes.add(block["code"])
    if block.get("block_code"):
        codes.add(block["block_code"])
    return codes


class DistributedOperationEligibilityBoundaryTests(unittest.TestCase):
    def resolve(self, request: object | None = None) -> dict:
        if request is None:
            request = valid_eligibility_request()
        return resolver.resolve_distributed_operation_eligibility_boundary(
            declared_eligibility_request=request
        )

    def assert_blocked_with(self, result: dict, expected_code: str | set[str]) -> None:
        self.assertEqual(OUTCOME_BLOCKED, result["outcome"])
        codes = failed_codes(result)
        if isinstance(expected_code, set):
            self.assertTrue(codes & expected_code, codes)
        else:
            self.assertIn(expected_code, codes)
        self.assertFalse(
            result["eligibility_statement"].get("distributed_operation_matter_eligible_for_review")
        )

    def assert_required_non_claims_false(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_operation_collapse(self, statement: dict) -> None:
        for key in (
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "source_body_authority_decided",
            "carrier_roles_defined",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
            "carrier_currentness_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "source_replaced",
            "authority_created",
            "permission_created",
            "truth_created",
            "action_authorized",
            "consequence_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            if key in statement:
                self.assertIs(statement[key], False, key)

    def test_successful_eligible_for_review_from_mapping(self) -> None:
        request = valid_eligibility_request()
        original_request = copy.deepcopy(request)

        result = self.resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(OUTCOME_ELIGIBLE, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["distributed_operation_eligibility_summary"]["failed_check_count"])

        statement = result["eligibility_statement"]
        self.assertIs(statement["distributed_operation_matter_eligible_for_review"], True)
        self.assertIs(statement["selected_matter_declaration_preserved"], True)
        self.assertIs(statement["selected_matter_declaration_declared"], True)
        self.assertIs(statement["selected_matter_declaration_failed_check_count_zero"], True)
        self.assertIs(statement["operation_candidate_preserved"], True)
        self.assertIs(statement["operation_matter_preserved"], True)
        self.assertIs(statement["operation_purpose_preserved"], True)
        self.assertIs(statement["proposed_operation_kind_preserved"], True)
        self.assertIs(statement["selected_operation_basis_preserved"], True)
        self.assertIs(statement["proposed_affected_surfaces_preserved"], True)
        self.assertIs(statement["proposed_output_family_preserved"], True)
        self.assertIs(statement["eligibility_review_request_preserved"], True)
        self.assertIs(statement["refusal_abort_awareness_preserved"], True)
        self.assertIs(statement["future_admission_authority_review_may_be_considered"], True)
        self.assert_no_operation_collapse(statement)
        self.assertEqual(original_request, request)

    def test_metadata_and_declared_eligibility_question(self) -> None:
        result = self.resolve()
        metadata = result["distributed_operation_eligibility_metadata"]
        for key in (
            "distributed_operation_eligibility_result_id",
            "distributed_operation_eligibility_result_type",
            "distributed_operation_eligibility_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["distributed_operation_eligibility_result_version"])
        self.assertEqual(
            "resolve_distributed_operation_eligibility_boundary",
            metadata["resolver_module"],
        )

        question = result["declared_eligibility_question"]
        self.assertEqual(
            "distributed_operation_eligibility_request_001",
            question["eligibility_request_id"],
        )
        self.assertEqual(
            "Is the declared distributed operation matter eligible for future admission/authority review?",
            question["eligibility_question"],
        )
        self.assertEqual("RECORD_DISTRIBUTED_OPERATION_ELIGIBILITY", question["eligibility_intent"])
        self.assertEqual(
            "distributed_operation_matter_declaration_result_001",
            question["selected_matter_declaration_id"],
        )
        self.assertEqual(MATTER_OUTCOME_DECLARED, question["selected_matter_declaration_outcome"])
        for key in (
            "eligibility_is_not_admission",
            "eligibility_is_not_authorization",
            "eligibility_is_not_execution",
            "eligibility_is_not_operation",
            "eligibility_is_not_synchronization",
            "eligibility_is_not_full_body_transfer",
            "eligibility_is_not_continuation",
            "eligibility_is_not_permission",
        ):
            self.assertIs(question[key], True, key)

    def test_selected_matter_candidate_matter_and_basis_sections(self) -> None:
        result = self.resolve()

        matter = result["selected_matter_declaration"]
        self.assertEqual("distributed_operation_matter_declaration_result_001", matter["selected_matter_declaration_id"])
        self.assertEqual(MATTER_OUTCOME_DECLARED, matter["selected_matter_declaration_outcome"])
        self.assertIs(matter["selected_matter_declaration_is_declared"], True)
        self.assertIs(matter["selected_matter_declaration_failed_check_count_zero"], True)
        self.assertIs(matter["selected_matter_declaration_remains_declaration_only"], True)
        self.assertIs(matter["selected_matter_declaration_did_not_admit_operation"], True)
        self.assertIs(matter["selected_matter_declaration_did_not_authorize_operation"], True)
        self.assertIs(matter["selected_matter_declaration_did_not_execute_operation"], True)
        self.assertIs(matter["selected_matter_declaration_not_mutated"], True)

        candidate = result["selected_operation_candidate"]
        self.assertEqual("distributed_operation_candidate_001", candidate["operation_candidate_id"])
        self.assertTrue(candidate["selected_operation_question"])
        for key in (
            "candidate_remains_candidate_only",
            "candidate_not_admitted",
            "candidate_not_authorized",
            "candidate_not_executed",
            "candidate_not_eligible_by_declaration",
            "eligibility_does_not_make_candidate_operation",
        ):
            self.assertIs(candidate[key], True, key)

        operation_matter = result["selected_operation_matter"]
        self.assertEqual("distributed_operation_matter_001", operation_matter["operation_matter_id"])
        self.assertEqual(
            "distributed_operation_matter_declaration_result_001",
            operation_matter["selected_matter_id"],
        )
        self.assertEqual(MATTER_OUTCOME_DECLARED, operation_matter["matter_declaration_outcome"])
        for key in (
            "matter_remains_declaration_only",
            "matter_not_upgraded_into_admission",
            "matter_not_upgraded_into_authorization",
            "matter_not_upgraded_into_operation",
        ):
            self.assertIs(operation_matter[key], True, key)

        basis = result["eligibility_basis"]
        self.assertIn("selected_matter_declaration_result", basis)
        self.assertEqual("distributed_operation_matter_declaration_result_001", basis["selected_matter_identity"])
        self.assertEqual("distributed_operation_candidate_001", basis["selected_operation_candidate_identity"])
        self.assertTrue(basis["selected_operation_question"])
        self.assertTrue(basis["selected_operation_purpose"])
        self.assertEqual(
            "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
            basis["selected_proposed_operation_kind"],
        )
        self.assertTrue(basis["selected_operation_basis"])
        self.assertTrue(basis["selected_carrier_context"])
        self.assertTrue(basis["selected_proposed_affected_surfaces"])
        self.assertTrue(basis["selected_proposed_output_family"])
        self.assertTrue(basis["selected_eligibility_review_request"])
        self.assertTrue(basis["selected_refusal_abort_awareness"])
        for key in (
            "current_body_conformance_v4_closure_basis",
            "current_self_orientation_v9_basis",
            "distributed_standing_basis",
            "source_body_basis",
        ):
            self.assertTrue(basis[key], key)
        for key in (
            "eligibility_basis_is_not_permission",
            "eligibility_basis_is_not_admission",
            "eligibility_basis_is_not_operation_plan",
            "eligibility_basis_is_not_synchronization_plan",
            "eligibility_basis_is_not_full_body_transfer_plan",
        ):
            self.assertIs(basis[key], True, key)

    def test_checks_non_meaning_open_summary_and_nonclaims(self) -> None:
        result = self.resolve()
        checks = result["eligibility_checks"]
        self.assertTrue(checks)
        required_check_names = {
            "eligibility question declared",
            "eligibility intent supported",
            "selected matter declaration present",
            "selected matter declaration outcome declared",
            "selected matter declaration outcome is declared",
            "selected matter declaration failed check count zero",
            "operation candidate preserved",
            "operation matter preserved",
            "operation purpose preserved",
            "proposed operation kind preserved and supported",
            "selected operation basis preserved",
            "proposed affected surfaces preserved",
            "proposed output family preserved",
            "eligibility review request preserved",
            "refusal abort awareness preserved",
            "operation not admitted",
            "operation not authorized",
            "operation not executed",
            "no repository synchronization authorized",
            "no full body transfer authorized",
            "no second body created",
            "no continuation authorized",
            "no distributed operation authorized",
            "no source-body authority decided",
            "no carrier roles defined",
            "no mutation replay or merge",
            "eligibility non-claims remain false",
        }
        self.assertTrue(required_check_names.issubset({check["check_name"] for check in checks}))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertEqual(0, result["distributed_operation_eligibility_summary"]["failed_check_count"])

        non_meaning = result["eligibility_non_meaning"]
        for key in (
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "source_body_authority_decided",
            "carrier_roles_decided",
            "synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
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
            "public_launch_readiness_created",
            "final_completion_claimed",
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
            "follow_on_work_authorized",
            "self_orientation_successor_scheduled",
        ):
            self.assertIs(non_meaning[key], True, key)
            self.assertIs(non_meaning[f"does_not_mean_{key}"], True, key)

        remains_open = result["what_remains_open"]
        for key in (
            "source_body_operational_authority_boundary",
            "carrier_operational_role_boundary",
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
            self.assertEqual("open_not_scheduled_not_authorized_not_executed", remains_open[key])
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

        summary = resolver.build_distributed_operation_eligibility_summary(result)
        self.assertEqual(OUTCOME_ELIGIBLE, summary["outcome"])
        self.assertEqual("distributed_operation_eligibility_request_001", summary["eligibility_request_id"])
        self.assertEqual("distributed_operation_candidate_001", summary["operation_candidate_id"])
        self.assertEqual("distributed_operation_matter_001", summary["operation_matter_id"])
        self.assertIs(summary["matter_eligible_for_review"], True)
        self.assertIs(summary["matter_not_eligible"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["future_admission_authority_review_may_be_considered"], True)
        self.assertIs(summary["operation_admitted"], False)
        self.assertIs(summary["operation_authorized"], False)
        self.assertIs(summary["operation_executed"], False)
        self.assertIs(summary["source_body_authority_decided"], False)
        self.assertIs(summary["carrier_roles_defined"], False)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation_distributed_operation"], True)
        self.assertIs(summary["no_source_authority_permission_truth_action_consequence"], True)
        self.assertIs(summary["no_public_readiness_final_completion_follow_on_work"], True)
        for value in summary["key_non_claims"].values():
            self.assertIs(value, False)
        self.assert_required_non_claims_false(result)

    def test_additional_basis_required_result(self) -> None:
        context = {
            "source_body_operational_authority_basis_insufficient": True,
            "carrier_role_basis_insufficient": True,
            "refusal_abort_law_insufficient": True,
            "additional_basis_reason": "authority and refusal boundaries remain future work",
        }
        result = self.resolve(
            valid_eligibility_request(
                requested_outcome=OUTCOME_ADDITIONAL,
                additional_basis_context=context,
            )
        )

        self.assertEqual(OUTCOME_ADDITIONAL, result["outcome"])
        additional = result["additional_basis_required"]
        self.assertIs(additional["additional_basis_required"], True)
        self.assertEqual(context, additional["additional_basis_context"])
        self.assertIs(additional["additional_basis_not_scheduled"], True)
        self.assertIs(additional["additional_basis_not_authorized"], True)
        self.assertIs(additional["additional_basis_not_executed"], True)
        self.assertIs(result["eligibility_statement"]["selected_matter_declaration_preserved"], True)
        self.assertIs(
            result["eligibility_statement"][
                "distributed_operation_matter_requires_additional_basis"
            ],
            True,
        )
        self.assertIs(result["eligibility_statement"]["operation_admitted"], False)
        self.assertIs(result["eligibility_statement"]["operation_authorized"], False)
        self.assertIs(result["eligibility_statement"]["operation_executed"], False)
        self.assertIsNone(result["block"]["block_code"])

    def test_not_eligible_readable_matter(self) -> None:
        result = self.resolve(
            valid_eligibility_request(
                requested_outcome=OUTCOME_NOT_ELIGIBLE,
                not_eligible_reason="candidate remains too broad for bounded review",
            )
        )

        self.assertEqual(OUTCOME_NOT_ELIGIBLE, result["outcome"])
        statement = result["eligibility_statement"]
        self.assertIs(statement["distributed_operation_matter_not_eligible_for_review"], True)
        self.assertEqual(
            "candidate remains too broad for bounded review",
            statement["not_eligible_reason"],
        )
        self.assertIs(statement["selected_matter_declaration_preserved"], True)
        self.assert_no_operation_collapse(statement)
        self.assertIsNone(result["block"]["block_code"])

    def test_request_builder_helper(self) -> None:
        matter = selected_matter_declaration()
        basis = eligibility_basis_value()

        request = resolver.build_declared_distributed_operation_eligibility_request(
            "eligibility_request_from_builder_001",
            "Is the selected matter eligible for future admission or authority review?",
            matter,
            basis,
            selected_matter_declaration_path="matter-result.json",
            selected_matter_declaration_id="distributed_operation_matter_declaration_result_001",
            selected_matter_declaration_outcome=MATTER_OUTCOME_DECLARED,
            requested_eligibility_outcome=OUTCOME_ELIGIBLE,
            not_eligible_reason=None,
        )

        self.assertEqual("eligibility_request_from_builder_001", request["eligibility_request_id"])
        self.assertEqual(
            "Is the selected matter eligible for future admission or authority review?",
            request["eligibility_question"],
        )
        self.assertEqual(matter, request["selected_matter_declaration"])
        self.assertEqual(basis, request["eligibility_basis"])
        self.assertEqual("matter-result.json", request["selected_matter_declaration_path"])
        self.assertEqual("distributed_operation_matter_declaration_result_001", request["selected_matter_declaration_id"])
        self.assertEqual(MATTER_OUTCOME_DECLARED, request["selected_matter_declaration_outcome"])
        self.assertEqual(OUTCOME_ELIGIBLE, request["requested_eligibility_outcome"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        with tempfile.TemporaryDirectory() as tmp:
            matter_path = Path(tmp) / "matter-result.json"
            matter_path.write_text(json.dumps(matter), encoding="utf-8")
            request["selected_matter_declaration_path"] = str(matter_path)
            result = self.resolve(request)
        self.assertEqual(OUTCOME_ELIGIBLE, result["outcome"])

        request_with_additional = resolver.build_declared_distributed_operation_eligibility_request(
            "eligibility_request_from_builder_002",
            "Is more basis required before eligibility can be judged?",
            matter,
            basis,
            requested_eligibility_outcome=OUTCOME_ADDITIONAL,
            additional_basis_context={"refusal_abort_law_insufficient": True},
        )
        self.assertEqual(
            {"refusal_abort_law_insufficient": True},
            request_with_additional["additional_basis_context"],
        )

    def test_path_based_selected_matter_declaration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            matter_path = Path(tmp) / "selected_matter.json"
            matter_path.write_text(json.dumps(selected_matter_declaration()), encoding="utf-8")
            request = valid_eligibility_request()
            request.pop("selected_matter_declaration")
            request["selected_matter_declaration_path"] = str(matter_path)

            result = self.resolve(request)

        self.assertEqual(OUTCOME_ELIGIBLE, result["outcome"])
        selected = result["selected_matter_declaration"]
        self.assertEqual(str(matter_path), selected["selected_matter_declaration_path"])
        self.assertEqual("distributed_operation_matter_declaration_result_001", selected["selected_matter_declaration_id"])
        self.assertEqual(MATTER_OUTCOME_DECLARED, selected["selected_matter_declaration_outcome"])

    def test_path_based_eligibility_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eligibility_request.json"
            request = valid_eligibility_request()
            path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolver.resolve_distributed_operation_eligibility_boundary_from_path(path)
            mapping_result = self.resolve(request)

        self.assertEqual(OUTCOME_ELIGIBLE, path_result["outcome"])
        self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))
        self.assertEqual(
            str(path),
            path_result["declared_eligibility_question"]["declared_eligibility_request_path"],
        )

    def test_write_behavior_and_default_output_path(self) -> None:
        result = self.resolve()
        self.assertEqual(
            "integrity_host_v0_min_coexistence_distributed_operation_eligibility_boundary",
            resolver.DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_ROOT.name,
        )
        self.assertNotEqual(
            "integrity_host_v0_min_coexistence_distributed_operation_matter_declaration",
            resolver.DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_ROOT.name,
        )

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "eligibility.json"
            written = resolver.write_distributed_operation_eligibility_result(result, output_path)
            self.assertEqual(output_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            root = Path(tmp) / "default-root"
            with patch.object(resolver, "DISTRIBUTED_OPERATION_ELIGIBILITY_BOUNDARY_ROOT", root):
                first = resolver.write_distributed_operation_eligibility_result(result)
                second = resolver.write_distributed_operation_eligibility_result(result)
            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertIn("__distributed_operation_eligibility_result", first.name)
            self.assertIn("_001", second.stem)

    def test_non_mutation_posture(self) -> None:
        request = valid_eligibility_request()
        selected_matter = request["selected_matter_declaration"]
        request_before = copy.deepcopy(request)
        matter_before = copy.deepcopy(selected_matter)

        first = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request_before, request)
        self.assertEqual(matter_before, selected_matter)
        self.assertEqual(OUTCOME_ELIGIBLE, first["outcome"])
        self.assertEqual(OUTCOME_ELIGIBLE, second["outcome"])

        with tempfile.TemporaryDirectory() as tmp:
            matter_path = Path(tmp) / "selected_matter.json"
            before_text = json.dumps(selected_matter, sort_keys=True)
            matter_path.write_text(before_text, encoding="utf-8")
            path_request = valid_eligibility_request()
            path_request.pop("selected_matter_declaration")
            path_request["selected_matter_declaration_path"] = str(matter_path)
            self.resolve(path_request)
            self.assertEqual(before_text, matter_path.read_text(encoding="utf-8"))

            output_path = Path(tmp) / "eligibility-result.json"
            resolver.write_distributed_operation_eligibility_result(first, output_path)
            self.assertEqual(before_text, matter_path.read_text(encoding="utf-8"))

    def test_blocking_explicit_missing_malformed_and_request_path_cases(self) -> None:
        blocked = self.resolve(
            valid_eligibility_request(intent="BLOCK_DISTRIBUTED_OPERATION_ELIGIBILITY")
        )
        self.assert_blocked_with(blocked, "ELIGIBILITY_REQUEST_EXPLICITLY_BLOCKED")

        missing = resolver.resolve_distributed_operation_eligibility_boundary()
        self.assert_blocked_with(missing, "ELIGIBILITY_QUESTION_UNDECLARED")

        malformed = self.resolve(["not", "a", "mapping"])
        self.assert_blocked_with(malformed, "DECLARED_ELIGIBILITY_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as tmp:
            missing_path = Path(tmp) / "missing.json"
            unreadable = resolver.resolve_distributed_operation_eligibility_boundary_from_path(
                missing_path
            )
            self.assert_blocked_with(unreadable, "DECLARED_ELIGIBILITY_REQUEST_UNREADABLE")

            malformed_path = Path(tmp) / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed_json = resolver.resolve_distributed_operation_eligibility_boundary_from_path(
                malformed_path
            )
            self.assert_blocked_with(malformed_json, "DECLARED_ELIGIBILITY_REQUEST_MALFORMED")

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_operation_eligibility_boundary_from_path(
                array_path
            )
            self.assert_blocked_with(array_result, "DECLARED_ELIGIBILITY_REQUEST_MALFORMED")

    def test_selected_matter_path_unreadable_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_path = Path(tmp) / "missing_matter.json"
            request = valid_eligibility_request()
            request.pop("selected_matter_declaration")
            request["selected_matter_declaration_path"] = str(missing_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_MATTER_DECLARATION_UNREADABLE",
            )

            malformed_path = Path(tmp) / "malformed_matter.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            request["selected_matter_declaration_path"] = str(malformed_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_MATTER_DECLARATION_MALFORMED",
            )

            array_path = Path(tmp) / "array_matter.json"
            array_path.write_text("[]", encoding="utf-8")
            request["selected_matter_declaration_path"] = str(array_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_MATTER_DECLARATION_MALFORMED",
            )

    def test_selected_matter_outcome_and_failed_checks_block(self) -> None:
        missing_outcome = selected_matter_declaration()
        missing_outcome.pop("outcome")
        missing_outcome["distributed_operation_matter_declaration_summary"].pop("outcome")
        request = valid_eligibility_request(selected_matter=missing_outcome)
        request.pop("selected_matter_declaration_outcome")
        self.assert_blocked_with(
            self.resolve(request),
            "SELECTED_MATTER_DECLARATION_OUTCOME_MISSING",
        )

        wrong_outcome = selected_matter_declaration(outcome="DISTRIBUTED_OPERATION_MATTER_NOT_DECLARED")
        self.assert_blocked_with(
            self.resolve(valid_eligibility_request(selected_matter=wrong_outcome)),
            "SELECTED_MATTER_DECLARATION_NOT_DECLARED",
        )

        failed = selected_matter_declaration()
        failed["distributed_operation_matter_declaration_summary"]["failed_check_count"] = 1
        failed["matter_declaration_statement"]["failed_check_count"] = 1
        failed["matter_declaration_checks"].append(
            {
                "check_name": "failed matter check",
                "passed": False,
                "expected_posture": "no failed checks",
                "actual_posture": "failed check present",
                "block_code": "EXAMPLE_FAILED_CHECK",
            }
        )
        self.assert_blocked_with(
            self.resolve(valid_eligibility_request(selected_matter=failed)),
            "SELECTED_MATTER_DECLARATION_HAS_FAILED_CHECKS",
        )

    def test_missing_selected_matter_sections_block(self) -> None:
        cases = [
            ("operation_candidate", "OPERATION_CANDIDATE_MISSING"),
            ("operation_matter", "OPERATION_MATTER_MISSING"),
            ("operation_purpose", "OPERATION_PURPOSE_MISSING"),
            ("proposed_operation_kind", "OPERATION_KIND_MISSING_OR_UNSUPPORTED"),
            ("selected_operation_basis", "SELECTED_OPERATION_BASIS_MISSING"),
            ("proposed_affected_surfaces", "PROPOSED_AFFECTED_SURFACES_MISSING"),
            ("proposed_output_family", "PROPOSED_OUTPUT_FAMILY_MISSING"),
            ("eligibility_review_request", "ELIGIBILITY_REVIEW_REQUEST_MISSING"),
            ("refusal_abort_awareness", "REFUSAL_ABORT_AWARENESS_MISSING"),
        ]
        for key, code in cases:
            with self.subTest(key=key):
                matter = selected_matter_declaration()
                matter.pop(key)
                summary_key = {
                    "operation_candidate": "operation_candidate_id",
                    "operation_matter": "operation_matter_id",
                    "operation_purpose": "operation_purpose",
                    "proposed_operation_kind": "proposed_operation_kind",
                }.get(key)
                if summary_key:
                    matter["distributed_operation_matter_declaration_summary"].pop(
                        summary_key,
                        None,
                    )
                request = valid_eligibility_request(selected_matter=matter)
                self.assert_blocked_with(self.resolve(request), code)

        malformed_carrier = selected_matter_declaration()
        malformed_carrier["selected_carrier_context"] = "malformed carrier context"
        self.assert_blocked_with(
            self.resolve(valid_eligibility_request(selected_matter=malformed_carrier)),
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        )

    def test_matter_declaration_collapse_flags_block(self) -> None:
        cases = [
            ("operation_admitted", True, "MATTER_DECLARATION_ADMITTED_OPERATION"),
            ("operation_authorized", True, "MATTER_DECLARATION_AUTHORIZED_OPERATION"),
            ("operation_executed", True, "MATTER_DECLARATION_EXECUTED_OPERATION"),
        ]
        for field, value, code in cases:
            with self.subTest(field=field):
                matter = selected_matter_declaration()
                matter["matter_declaration_statement"][field] = value
                matter["non_claims"][field] = value
                self.assert_blocked_with(
                    self.resolve(valid_eligibility_request(selected_matter=matter)),
                    code,
                )

    def test_eligibility_collapse_flags_block(self) -> None:
        cases = [
            ("operation_admitted", "ELIGIBILITY_ADMITS_OPERATION"),
            ("operation_authorized", "ELIGIBILITY_AUTHORIZES_OPERATION"),
            ("operation_executed", "ELIGIBILITY_EXECUTES_OPERATION"),
            ("source_body_authority_decided", "ELIGIBILITY_DECIDES_SOURCE_BODY_AUTHORITY"),
            ("carrier_roles_defined", "ELIGIBILITY_DEFINES_CARRIER_OPERATIONAL_ROLES"),
            ("repository_synchronization_authorized", "ELIGIBILITY_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "ELIGIBILITY_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "ELIGIBILITY_CREATES_SECOND_BODY"),
            ("continuation_authorized", "ELIGIBILITY_AUTHORIZES_CONTINUATION"),
            ("carrier_currentness_created", "ELIGIBILITY_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "ELIGIBILITY_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "ELIGIBILITY_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "ELIGIBILITY_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "ELIGIBILITY_REPLACES_SOURCE"),
            ("authority_created", "ELIGIBILITY_CREATES_AUTHORITY"),
            ("permission_created", "ELIGIBILITY_CREATES_PERMISSION"),
            ("truth_created", "ELIGIBILITY_CREATES_TRUTH_OR_ACTION"),
            ("action_authorized", "ELIGIBILITY_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "ELIGIBILITY_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "ELIGIBILITY_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
            ("blocked_attempt_erased", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
            ("projection_mismatch_hidden", "ELIGIBILITY_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "ELIGIBILITY_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "ELIGIBILITY_SCHEDULES_FOLLOW_ON_WORK"),
        ]
        for field, code in cases:
            with self.subTest(field=field):
                request = valid_eligibility_request()
                request["declared_non_claims"][field] = True
                self.assert_blocked_with(self.resolve(request), code)

    def test_mutation_replay_merge_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = valid_eligibility_request()
                request["declared_non_claims"][field] = True
                self.assert_blocked_with(
                    self.resolve(request),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = valid_eligibility_request()
        missing["declared_non_claims"].pop("self_orientation_successor_scheduled")
        self.assert_blocked_with(
            self.resolve(missing),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

        flipped_non_specific = valid_eligibility_request()
        flipped_non_specific["declared_non_claims"]["self_orientation_successor_scheduled"] = True
        self.assert_blocked_with(
            self.resolve(flipped_non_specific),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

        matter_missing = selected_matter_declaration()
        matter_missing["non_claims"].pop("self_orientation_successor_scheduled")
        matter_missing["declared_matter_question"]["declared_non_claims"].pop(
            "self_orientation_successor_scheduled"
        )
        self.assert_blocked_with(
            self.resolve(valid_eligibility_request(selected_matter=matter_missing)),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    def test_nonclaims_for_all_outcomes(self) -> None:
        eligible = self.resolve()
        not_eligible = self.resolve(
            valid_eligibility_request(
                requested_outcome=OUTCOME_NOT_ELIGIBLE,
                not_eligible_reason="not eligible by bounded request",
            )
        )
        additional = self.resolve(
            valid_eligibility_request(
                requested_outcome=OUTCOME_ADDITIONAL,
                additional_basis_context={"carrier_role_basis_insufficient": True},
            )
        )
        blocked = self.resolve(
            valid_eligibility_request(intent="BLOCK_DISTRIBUTED_OPERATION_ELIGIBILITY")
        )

        for result in (eligible, not_eligible, additional, blocked):
            with self.subTest(outcome=result["outcome"]):
                self.assertIn(
                    result["outcome"],
                    {
                        OUTCOME_ELIGIBLE,
                        OUTCOME_NOT_ELIGIBLE,
                        OUTCOME_ADDITIONAL,
                        OUTCOME_BLOCKED,
                    },
                )
                self.assert_required_non_claims_false(result)


if __name__ == "__main__":
    unittest.main()
