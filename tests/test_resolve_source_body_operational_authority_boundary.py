"""Bounded tests for source-body operational authority boundary.

These tests verify that source-body operational authority basis review checks
one eligible distributed operation matter only. The resolver may record
sufficient source-body authority basis, return not sufficient, require
additional basis, or block. It must not grant authority, create permission,
admit, authorize, execute, define carrier roles, synchronize repositories,
transfer a body, create consequence, create public readiness, claim final
completion, or schedule follow-on work.
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

import resolve_source_body_operational_authority_boundary as resolver


OUTCOME_RECORDED = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
OUTCOME_NOT_SUFFICIENT = "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_NOT_SUFFICIENT"
OUTCOME_ADDITIONAL = "SOURCE_BODY_OPERATIONAL_AUTHORITY_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW_BLOCKED"
ELIGIBILITY_OUTCOME = "DISTRIBUTED_OPERATION_MATTER_ELIGIBLE_FOR_REVIEW"

TOP_LEVEL_SECTIONS = (
    "source_body_operational_authority_metadata",
    "declared_authority_question",
    "selected_eligibility_result",
    "selected_operation_matter",
    "source_body_authority_basis",
    "authority_checks",
    "authority_statement",
    "authority_non_meaning",
    "additional_basis_required",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "source_body_operational_authority_summary",
)

AUTHORITY_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS.keys())

ELIGIBILITY_NON_CLAIMS = AUTHORITY_NON_CLAIMS + (
    "source_body_authority_decided",
    "authority_created",
)

MATTER_NON_CLAIMS = (
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
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
    "evidence_erased",
    "refusal_erased",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "eligibility_decided",
)


def false_claims(keys: tuple[str, ...]) -> dict[str, bool]:
    return {key: False for key in keys}


def operation_candidate() -> dict:
    return {
        "operation_candidate_id": "distributed_operation_candidate_001",
        "declared_operation_question": (
            "Should this eligible matter proceed toward future admission / "
            "transition review?"
        ),
        "candidate_remains_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
        "candidate_not_eligible_by_declaration": True,
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
            "Review whether source-body lineage and authority reference are "
            "sufficient for later admission / transition review."
        ),
        "purpose_is_not_permission": True,
        "purpose_is_not_operation_plan": True,
        "purpose_is_not_output_authorization": True,
        "purpose_is_not_follow_on_work_authorization": True,
    }


def refusal_abort_awareness() -> dict:
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


def selected_operation_basis() -> dict:
    return {
        "source_body_basis": {"basis_id": "source_body_basis_001"},
        "current_body_conformance_v4_closure_basis": {
            "basis_id": "current_body_conformance_v4_closure_001",
            "operation_authorized": False,
        },
        "current_self_orientation_v9_basis": {
            "basis_id": "current_self_orientation_v9_001",
            "operation_authorized": False,
        },
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_boundary_001",
            "distributed_standing_becomes_authority": False,
        },
        "basis_is_not_permission": True,
        "basis_is_not_operation_plan": True,
        "basis_is_not_synchronization_plan": True,
        "basis_is_not_full_body_transfer_plan": True,
    }


def carrier_context() -> dict:
    return {
        "carrier_b_success_evidence_context_only": True,
        "carrier_c_block_evidence_context_only": True,
        "b_c_divergence_visible_context_only": True,
        "carrier_becomes_authority": False,
        "registry_becomes_authority": False,
        "currentness_successor_becomes_authority": False,
        "selected_carriers_are_context_not_operational_participants": True,
        "no_current_carrier_selected": True,
        "no_winning_carrier_selected": True,
        "no_losing_carrier_invalidated": True,
    }


def selected_matter_declaration() -> dict:
    statement = {
        "distributed_operation_matter_declared": True,
        "operation_candidate_preserved": True,
        "operation_matter_preserved": True,
        "operation_purpose_preserved": True,
        "eligibility_review_request_preserved": True,
        "refusal_abort_awareness_preserved": True,
        "operation_admitted": False,
        "operation_authorized": False,
        "operation_executed": False,
        "authority_created": False,
        "permission_created": False,
        "consequence_created": False,
        "failed_check_count": 0,
    }
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
        "refusal_abort_awareness": refusal_abort_awareness(),
        "matter_declaration_statement": statement,
        "distributed_operation_matter_declaration_summary": {
            "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
            "failed_check_count": 0,
            "operation_candidate_id": "distributed_operation_candidate_001",
            "operation_matter_id": "distributed_operation_matter_001",
        },
        "non_claims": false_claims(MATTER_NON_CLAIMS),
        "outcome": "DISTRIBUTED_OPERATION_MATTER_DECLARED",
    }


def eligibility_basis() -> dict:
    basis = selected_operation_basis()
    return {
        "selected_matter_declaration_result": selected_matter_declaration(),
        "selected_matter_identity": "distributed_operation_matter_declaration_result_001",
        "selected_operation_candidate_identity": "distributed_operation_candidate_001",
        "selected_operation_question": operation_candidate()["declared_operation_question"],
        "selected_operation_purpose": operation_purpose()["declared_operation_purpose"],
        "selected_proposed_operation_kind": "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
        "selected_operation_basis": basis,
        "selected_carrier_context": carrier_context(),
        "selected_proposed_affected_surfaces": [
            "source_body_authority_basis",
            "eligible_distributed_operation_matter",
        ],
        "selected_proposed_output_family": [
            "SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS_RECORDED"
        ],
        "selected_eligibility_review_request": {
            "future_admission_authority_review_only": True,
            "eligibility_does_not_grant_authority": True,
        },
        "selected_refusal_abort_awareness": refusal_abort_awareness(),
        "current_body_conformance_v4_closure_basis": basis[
            "current_body_conformance_v4_closure_basis"
        ],
        "current_self_orientation_v9_basis": basis["current_self_orientation_v9_basis"],
        "distributed_standing_basis": basis["distributed_standing_basis"],
        "source_body_basis": basis["source_body_basis"],
        "eligibility_basis_is_not_permission": True,
        "eligibility_basis_is_not_admission": True,
        "eligibility_basis_is_not_operation_plan": True,
        "eligibility_basis_is_not_synchronization_plan": True,
        "eligibility_basis_is_not_full_body_transfer_plan": True,
    }


def selected_eligibility_result(**overrides: object) -> dict:
    statement = {
        "distributed_operation_matter_eligible_for_review": True,
        "selected_matter_declaration_preserved": True,
        "selected_matter_declaration_declared": True,
        "selected_matter_declaration_failed_check_count_zero": True,
        "operation_candidate_preserved": True,
        "operation_matter_preserved": True,
        "operation_purpose_preserved": True,
        "proposed_operation_kind_preserved": True,
        "selected_operation_basis_preserved": True,
        "proposed_affected_surfaces_preserved": True,
        "proposed_output_family_preserved": True,
        "eligibility_review_request_preserved": True,
        "refusal_abort_awareness_preserved": True,
        "future_admission_authority_review_may_be_considered": True,
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
        "consequence_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "failed_check_count": 0,
    }
    result = {
        "distributed_operation_eligibility_metadata": {
            "distributed_operation_eligibility_result_id": (
                "distributed_operation_eligibility_result_001"
            ),
            "distributed_operation_eligibility_result_type": (
                "distributed_operation_eligibility_result"
            ),
            "distributed_operation_eligibility_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_operation_eligibility_boundary",
        },
        "declared_eligibility_question": {
            "eligibility_request_id": "distributed_operation_eligibility_request_001",
            "eligibility_question": (
                "Is the declared distributed operation matter eligible for "
                "future admission/authority review?"
            ),
            "eligibility_intent": "RECORD_DISTRIBUTED_OPERATION_ELIGIBILITY",
        },
        "selected_matter_declaration": selected_matter_declaration(),
        "selected_operation_candidate": operation_candidate(),
        "selected_operation_matter": operation_matter(),
        "operation_purpose": operation_purpose(),
        "eligibility_basis": eligibility_basis(),
        "eligibility_checks": [
            {
                "check_name": "eligibility checks passed",
                "passed": True,
                "expected_posture": "eligible without admission",
                "actual_posture": "eligible without admission",
                "block_code": None,
            }
        ],
        "eligibility_statement": statement,
        "non_claims": false_claims(ELIGIBILITY_NON_CLAIMS),
        "outcome": ELIGIBILITY_OUTCOME,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "distributed_operation_eligibility_summary": {
            "outcome": ELIGIBILITY_OUTCOME,
            "eligibility_request_id": "distributed_operation_eligibility_request_001",
            "selected_matter_declaration_id": (
                "distributed_operation_matter_declaration_result_001"
            ),
            "selected_matter_declaration_outcome": (
                "DISTRIBUTED_OPERATION_MATTER_DECLARED"
            ),
            "operation_candidate_id": "distributed_operation_candidate_001",
            "operation_matter_id": "distributed_operation_matter_001",
            "operation_question": operation_candidate()["declared_operation_question"],
            "operation_purpose": operation_purpose()["declared_operation_purpose"],
            "proposed_operation_kind": "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
            "passed_check_count": 37,
            "failed_check_count": 0,
            "selected_matter_declaration_preserved": True,
            "selected_matter_declaration_declared": True,
            "selected_matter_declaration_failed_check_count_zero": True,
            "operation_candidate_preserved": True,
            "operation_matter_preserved": True,
            "operation_purpose_preserved": True,
            "eligibility_review_request_preserved": True,
            "refusal_abort_awareness_preserved": True,
            "future_admission_authority_review_may_be_considered": True,
        },
    }
    for key, value in overrides.items():
        result[key] = value
    return result


def source_body_authority_basis() -> dict:
    return {
        "source_body_lineage_basis": {
            "lineage_id": "source_body_lineage_001",
            "lineage_is_source_body_reference_only": True,
        },
        "source_body_authority_reference": {
            "authority_reference_id": "source_body_authority_reference_001",
            "authority_reference_is_not_authority_grant": True,
        },
        "operational_authority_origin": "source_body_lineage_reference_only",
        "current_body_conformance_v4_closure_basis": {
            "basis_id": "current_body_conformance_v4_closure_001",
            "operation_authorized": False,
        },
        "current_self_orientation_v9_basis": {
            "basis_id": "current_self_orientation_v9_001",
            "operation_authorized": False,
        },
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_basis_001",
            "distributed_standing_becomes_authority": False,
        },
        "divergence_consequence_basis": {
            "basis_id": "cross_carrier_divergence_consequence_001",
            "caution_context_only": True,
        },
        "refusal_abort_awareness": refusal_abort_awareness(),
        "selected_carrier_context": carrier_context(),
        "carrier_becomes_authority": False,
        "registry_becomes_authority": False,
        "lifecycle_posture_becomes_authority": False,
        "currentness_successor_becomes_authority": False,
        "distributed_standing_posture_becomes_authority": False,
        "eligibility_result_becomes_authority": False,
        "successful_receipt_count_becomes_authority": False,
        "majority_authority": False,
        "latest_file_authority": False,
        "latest_turn_authority": False,
        "current_turn_authority": False,
        "source_body_authority_basis_is_not_authority_grant": True,
        "source_body_authority_basis_is_not_permission": True,
        "source_body_authority_basis_is_not_operation_admission": True,
        "source_body_authority_basis_is_not_operation_authorization": True,
        "source_body_authority_basis_is_not_execution": True,
    }


def valid_authority_request(
    *,
    eligibility: dict | None = None,
    basis: dict | None = None,
    intent: str = "RECORD_SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS",
    requested_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: dict | None = None,
    not_sufficient_reason: str | None = None,
) -> dict:
    request = {
        "authority_request_id": "source_body_authority_request_001",
        "authority_question": (
            "Does the eligible distributed operation matter have sufficient "
            "source-body authority basis for future admission / transition review?"
        ),
        "authority_intent": intent,
        "selected_eligibility_result": eligibility
        if eligibility is not None
        else selected_eligibility_result(),
        "selected_eligibility_result_id": "distributed_operation_eligibility_result_001",
        "selected_eligibility_result_outcome": ELIGIBILITY_OUTCOME,
        "expected_selected_eligibility_outcome": ELIGIBILITY_OUTCOME,
        "source_body_authority_basis": basis
        if basis is not None
        else source_body_authority_basis(),
        "requested_authority_outcome": requested_outcome,
        "declared_non_claims": false_claims(AUTHORITY_NON_CLAIMS),
    }
    if additional_basis_context is not None:
        request["additional_basis_context"] = additional_basis_context
    if not_sufficient_reason is not None:
        request["not_sufficient_reason"] = not_sufficient_reason
    return request


def failed_codes(result: dict) -> set[str]:
    codes: set[str] = set()
    for check in result.get("authority_checks", []):
        if not check.get("passed"):
            code = check.get("block_code") or check.get("failure_code")
            if code:
                codes.add(code)
    block = result.get("block", {})
    for key in ("block_code", "code"):
        if block.get(key):
            codes.add(block[key])
    return codes


class SourceBodyOperationalAuthorityBoundaryTests(unittest.TestCase):
    def resolve(self, request: object | None = None) -> dict:
        if request is None:
            request = valid_authority_request()
        return resolver.resolve_source_body_operational_authority_boundary(
            declared_authority_request=request
        )

    def assert_blocked_with(self, result: dict, expected_code: str | set[str]) -> None:
        self.assertEqual(OUTCOME_BLOCKED, result["outcome"])
        codes = failed_codes(result)
        if isinstance(expected_code, set):
            self.assertTrue(codes & expected_code, codes)
        else:
            self.assertIn(expected_code, codes)
        self.assertFalse(
            result["authority_statement"].get(
                "source_body_operational_authority_basis_recorded"
            )
        )

    def assert_required_non_claims_false(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in AUTHORITY_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_authority_or_operation_collapse(self, statement: dict) -> None:
        for key in AUTHORITY_NON_CLAIMS:
            if key in statement:
                self.assertIs(statement[key], False, key)

    def test_successful_authority_basis_recorded_from_mapping(self) -> None:
        request = valid_authority_request()
        original_request = copy.deepcopy(request)
        result = self.resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(OUTCOME_RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["source_body_operational_authority_summary"]["failed_check_count"])

        statement = result["authority_statement"]
        self.assertIs(statement["source_body_operational_authority_basis_recorded"], True)
        self.assertIs(statement["selected_eligibility_result_preserved"], True)
        self.assertIs(statement["selected_eligibility_result_eligible"], True)
        self.assertIs(statement["selected_eligibility_result_failed_check_count_zero"], True)
        self.assertIs(statement["selected_matter_declaration_preserved"], True)
        self.assertIs(statement["selected_operation_candidate_preserved"], True)
        self.assertIs(statement["selected_operation_matter_preserved"], True)
        self.assertIs(statement["source_body_lineage_basis_preserved"], True)
        self.assertIs(statement["source_body_authority_reference_preserved"], True)
        self.assertIs(statement["current_body_conformance_v4_closure_basis_preserved"], True)
        self.assertIs(statement["current_self_orientation_v9_basis_preserved"], True)
        self.assertIs(statement["refusal_abort_awareness_preserved"], True)
        self.assertIs(statement["future_admission_transition_review_may_be_considered"], True)
        self.assert_no_authority_or_operation_collapse(statement)
        self.assertEqual(original_request, request)

    def test_metadata_declared_question_selected_sections_and_basis(self) -> None:
        result = self.resolve()
        metadata = result["source_body_operational_authority_metadata"]
        for key in (
            "source_body_operational_authority_result_id",
            "source_body_operational_authority_result_type",
            "source_body_operational_authority_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["source_body_operational_authority_result_version"])
        self.assertEqual("resolve_source_body_operational_authority_boundary", metadata["resolver_module"])

        question = result["declared_authority_question"]
        self.assertEqual("source_body_authority_request_001", question["authority_request_id"])
        self.assertEqual(
            "RECORD_SOURCE_BODY_OPERATIONAL_AUTHORITY_BASIS",
            question["authority_intent"],
        )
        self.assertEqual(
            "distributed_operation_eligibility_result_001",
            question["selected_eligibility_result_id"],
        )
        self.assertEqual(ELIGIBILITY_OUTCOME, question["selected_eligibility_result_outcome"])
        for key in (
            "authority_is_not_authority_grant",
            "authority_is_not_permission",
            "authority_is_not_admission",
            "authority_is_not_authorization",
            "authority_is_not_execution",
            "authority_is_not_operation",
            "authority_is_not_synchronization",
            "authority_is_not_full_body_transfer",
            "authority_is_not_continuation",
            "authority_is_not_carrier_role_definition",
        ):
            self.assertIs(question[key], True, key)

        selected = result["selected_eligibility_result"]
        self.assertEqual("distributed_operation_eligibility_result_001", selected["selected_eligibility_result_id"])
        self.assertEqual(ELIGIBILITY_OUTCOME, selected["selected_eligibility_result_outcome"])
        self.assertIs(selected["selected_eligibility_result_outcome_is_eligible"], True)
        self.assertIs(selected["selected_eligibility_result_failed_check_count_zero"], True)
        self.assertIs(selected["selected_eligibility_result_remains_eligibility_only"], True)
        self.assertIs(selected["selected_eligibility_result_did_not_admit_operation"], True)
        self.assertIs(selected["selected_eligibility_result_did_not_authorize_operation"], True)
        self.assertIs(selected["selected_eligibility_result_did_not_execute_operation"], True)
        self.assertIs(selected["selected_eligibility_result_did_not_decide_source_body_authority"], True)
        self.assertIs(selected["selected_eligibility_result_did_not_define_carrier_roles"], True)

        matter = result["selected_operation_matter"]
        self.assertTrue(matter["selected_eligibility_result"])
        self.assertTrue(matter["selected_matter_declaration"])
        self.assertEqual(
            "distributed_operation_candidate_001",
            matter["selected_operation_candidate"]["operation_candidate_id"],
        )
        self.assertEqual(
            "distributed_operation_matter_001",
            matter["selected_operation_matter"]["operation_matter_id"],
        )
        self.assertTrue(matter["selected_operation_question"])
        self.assertTrue(matter["selected_operation_purpose"])
        self.assertEqual(
            "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
            matter["proposed_operation_kind"],
        )
        self.assertIs(matter["matter_remains_declaration_only"], True)
        self.assertIs(matter["candidate_remains_candidate_only"], True)
        self.assertIs(matter["eligibility_remains_eligibility_only"], True)
        self.assertIs(matter["operation_admitted"], False)
        self.assertIs(matter["operation_authorized"], False)
        self.assertIs(matter["operation_executed"], False)

        basis = result["source_body_authority_basis"]
        self.assertTrue(basis["source_body_lineage_basis"])
        self.assertTrue(basis["source_body_authority_reference"])
        self.assertEqual("source_body_lineage_reference_only", basis["operational_authority_origin"])
        self.assertIs(basis["operational_authority_origin_is_source_body_lineage_reference_only"], True)
        self.assertTrue(basis["current_body_conformance_v4_closure_basis"])
        self.assertTrue(basis["current_self_orientation_v9_basis"])
        self.assertTrue(basis["distributed_standing_basis"])
        self.assertIs(basis["distributed_standing_basis_is_basis_only"], True)
        self.assertTrue(basis["divergence_consequence_basis"])
        self.assertIs(basis["divergence_consequence_basis_is_caution_context_only"], True)
        self.assertTrue(basis["refusal_abort_awareness"])
        self.assertTrue(basis["selected_carrier_context"])
        self.assertIs(basis["selected_carrier_context_is_context_only"], True)
        for key in (
            "source_body_authority_basis_is_not_authority_grant",
            "source_body_authority_basis_is_not_permission",
            "source_body_authority_basis_is_not_operation_admission",
            "source_body_authority_basis_is_not_operation_authorization",
            "source_body_authority_basis_is_not_execution",
            "source_body_authority_basis_is_not_carrier_authority",
            "source_body_authority_basis_is_not_registry_authority",
            "source_body_authority_basis_is_not_currentness_authority",
            "source_body_authority_basis_is_not_distributed_standing_authority",
        ):
            self.assertIs(basis[key], True, key)

    def test_checks_non_meaning_open_nonclaims_and_summary(self) -> None:
        result = self.resolve()
        checks = result["authority_checks"]
        required_check_names = {
            "authority question declared",
            "authority intent supported",
            "selected eligibility result present",
            "selected eligibility result outcome declared",
            "selected eligibility result outcome eligible",
            "selected eligibility result failed check count zero",
            "selected matter declaration preserved",
            "selected operation candidate preserved",
            "selected operation matter preserved",
            "selected operation purpose preserved",
            "eligibility review request preserved",
            "refusal/abort awareness preserved",
            "source-body lineage basis present",
            "source-body authority reference present",
            "current-body conformance v4 closure basis present",
            "current self-orientation v9 basis present",
            "distributed standing basis remains basis only where supplied",
            "carrier context remains context only where supplied",
            "no carrier becomes authority",
            "no registry becomes authority",
            "no lifecycle posture becomes authority",
            "no currentness successor becomes authority",
            "no distributed standing posture becomes authority",
            "no eligibility result becomes authority",
            "no successful receipt count becomes authority",
            "no majority/latest-file/current-turn authority",
            "no operation admitted",
            "no operation authorized",
            "no operation executed",
            "no carrier roles defined",
            "no repository synchronization authorized",
            "no full body transfer authorized",
            "no second body created",
            "no continuation authorized",
            "no distributed operation authorized",
            "no source-body authority replaced",
            "no permission created",
            "no truth/action created",
            "no consequence created",
            "no public readiness/final completion/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(required_check_names.issubset({check["check_name"] for check in checks}))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
        self.assertTrue(all(check["passed"] for check in checks))

        non_meaning = result["authority_non_meaning"]
        for key in (
            "authority_granted",
            "authority_created",
            "permission_created",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "carrier_roles_defined",
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
            "truth_action_created",
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
        ):
            self.assertIs(non_meaning[key], True, key)
            self.assertIs(non_meaning[f"does_not_mean_{key}"], True, key)

        remains_open = result["what_remains_open"]
        for key in (
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
            self.assertIs(remains_open[key], True, key)
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

        summary = resolver.build_source_body_operational_authority_summary(result)
        self.assertEqual(OUTCOME_RECORDED, summary["outcome"])
        self.assertEqual("source_body_authority_request_001", summary["authority_request_id"])
        self.assertEqual("distributed_operation_eligibility_result_001", summary["selected_eligibility_result_id"])
        self.assertEqual("distributed_operation_candidate_001", summary["selected_operation_candidate_id"])
        self.assertEqual("distributed_operation_matter_001", summary["selected_operation_matter_id"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["source_body_operational_authority_basis_recorded"], True)
        self.assertIs(summary["authority_basis_not_sufficient"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertIs(summary["selected_eligibility_result_preserved"], True)
        self.assertIs(summary["selected_eligibility_result_eligible"], True)
        self.assertIs(summary["selected_eligibility_result_failed_check_count_zero"], True)
        self.assertIs(summary["selected_matter_declaration_preserved"], True)
        self.assertIs(summary["selected_operation_candidate_preserved"], True)
        self.assertIs(summary["selected_operation_matter_preserved"], True)
        self.assertIs(summary["source_body_lineage_basis_preserved"], True)
        self.assertIs(summary["source_body_authority_reference_preserved"], True)
        self.assertIs(summary["current_body_conformance_v4_closure_basis_preserved"], True)
        self.assertIs(summary["current_self_orientation_v9_basis_preserved"], True)
        self.assertIs(summary["refusal_abort_awareness_preserved"], True)
        self.assertIs(summary["future_admission_transition_review_may_be_considered"], True)
        self.assertIs(summary["authority_granted"], False)
        self.assertIs(summary["authority_created"], False)
        self.assertIs(summary["permission_created"], False)
        self.assertIs(summary["operation_admitted"], False)
        self.assertIs(summary["operation_authorized"], False)
        self.assertIs(summary["operation_executed"], False)
        self.assertIs(summary["carrier_roles_defined"], False)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation_distributed_operation"], True)
        self.assertIs(summary["no_source_replacement_truth_action_consequence"], True)
        self.assertIs(summary["no_public_readiness_final_completion_follow_on_work"], True)
        for value in summary["key_non_claims"].values():
            self.assertIs(value, False)
        self.assert_required_non_claims_false(result)

    def test_additional_basis_required_result(self) -> None:
        context = {
            "source_body_authority_reference_too_generic": True,
            "source_body_lineage_basis_insufficiently_specific": True,
            "operation_purpose_requires_stronger_source_body_authorization_surface": True,
            "proposed_affected_surfaces_require_additional_authority_basis": True,
            "proposed_output_family_requires_additional_authority_basis": True,
            "carrier_context_creates_authority_ambiguity": True,
            "refusal_abort_awareness_needs_authority_specific_binding": True,
            "admission_transition_boundary_cannot_yet_inspect_authority_safely": True,
            "reason": "source-body authority reference needs tighter binding",
        }
        result = self.resolve(
            valid_authority_request(
                requested_outcome=OUTCOME_ADDITIONAL,
                additional_basis_context=context,
            )
        )

        self.assertEqual(OUTCOME_ADDITIONAL, result["outcome"])
        additional = result["additional_basis_required"]
        self.assertIs(additional["additional_basis_required"], True)
        self.assertEqual(context, additional["additional_basis_context"])
        self.assertEqual(context["reason"], additional["additional_basis_reason"])
        for key, value in context.items():
            if isinstance(value, bool):
                self.assertIs(additional[key], value, key)
        self.assertIs(additional["additional_basis_not_scheduled"], True)
        self.assertIs(additional["additional_basis_not_authorized"], True)
        self.assertIs(additional["additional_basis_not_executed"], True)
        statement = result["authority_statement"]
        self.assertIs(statement["source_body_operational_authority_requires_additional_basis"], True)
        self.assertIs(statement["selected_eligibility_result_preserved"], True)
        self.assertIs(statement["missing_basis_not_scheduled"], True)
        self.assertIs(statement["missing_basis_not_authorized"], True)
        self.assertIs(statement["missing_basis_not_executed"], True)
        self.assert_no_authority_or_operation_collapse(statement)

    def test_authority_basis_not_sufficient_result(self) -> None:
        reason = (
            "authority reference is only registry/currentness/distributed-standing "
            "or carrier evidence and cannot support later admission review"
        )
        result = self.resolve(
            valid_authority_request(
                requested_outcome=OUTCOME_NOT_SUFFICIENT,
                not_sufficient_reason=reason,
            )
        )

        self.assertEqual(OUTCOME_NOT_SUFFICIENT, result["outcome"])
        statement = result["authority_statement"]
        self.assertIs(statement["authority_basis_not_sufficient"], True)
        self.assertEqual(reason, statement["not_sufficient_reason"])
        self.assertIs(statement["selected_eligibility_result_preserved"], True)
        self.assert_no_authority_or_operation_collapse(statement)
        self.assertIsNone(result["block"]["block_code"])

    def test_request_builder_helper(self) -> None:
        eligibility = selected_eligibility_result()
        basis = source_body_authority_basis()
        request = resolver.build_declared_source_body_operational_authority_request(
            "source_body_authority_request_from_builder_001",
            "Does this eligible matter have source-body authority basis?",
            eligibility,
            basis,
            selected_eligibility_result_path="eligibility-result.json",
            selected_eligibility_result_id="distributed_operation_eligibility_result_001",
            selected_eligibility_result_outcome=ELIGIBILITY_OUTCOME,
            requested_authority_outcome=OUTCOME_RECORDED,
        )

        self.assertEqual(
            "source_body_authority_request_from_builder_001",
            request["authority_request_id"],
        )
        self.assertEqual(
            "Does this eligible matter have source-body authority basis?",
            request["authority_question"],
        )
        self.assertEqual(eligibility, request["selected_eligibility_result"])
        self.assertEqual(basis, request["source_body_authority_basis"])
        self.assertEqual("eligibility-result.json", request["selected_eligibility_result_path"])
        self.assertEqual(
            "distributed_operation_eligibility_result_001",
            request["selected_eligibility_result_id"],
        )
        self.assertEqual(ELIGIBILITY_OUTCOME, request["selected_eligibility_result_outcome"])
        self.assertEqual(OUTCOME_RECORDED, request["requested_authority_outcome"])
        for key in AUTHORITY_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eligibility-result.json"
            path.write_text(json.dumps(eligibility), encoding="utf-8")
            request["selected_eligibility_result_path"] = str(path)
            result = self.resolve(request)
        self.assertEqual(OUTCOME_RECORDED, result["outcome"])

        additional = resolver.build_declared_source_body_operational_authority_request(
            "source_body_authority_request_from_builder_002",
            "Is additional authority basis needed?",
            eligibility,
            basis,
            requested_authority_outcome=OUTCOME_ADDITIONAL,
            additional_basis_context={"carrier_context_creates_authority_ambiguity": True},
            not_sufficient_reason="not used for additional basis",
        )
        self.assertEqual(
            {"carrier_context_creates_authority_ambiguity": True},
            additional["additional_basis_context"],
        )
        self.assertEqual("not used for additional basis", additional["not_sufficient_reason"])

    def test_path_based_selected_eligibility_and_authority_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            eligibility_path = Path(tmp) / "selected_eligibility.json"
            eligibility_path.write_text(
                json.dumps(selected_eligibility_result()), encoding="utf-8"
            )
            request = valid_authority_request()
            request.pop("selected_eligibility_result")
            request["selected_eligibility_result_path"] = str(eligibility_path)
            result = self.resolve(request)

            self.assertEqual(OUTCOME_RECORDED, result["outcome"])
            selected = result["selected_eligibility_result"]
            self.assertEqual(str(eligibility_path), selected["selected_eligibility_result_path"])
            self.assertEqual(
                "distributed_operation_eligibility_result_001",
                selected["selected_eligibility_result_id"],
            )
            self.assertEqual(ELIGIBILITY_OUTCOME, selected["selected_eligibility_result_outcome"])

            authority_path = Path(tmp) / "authority_request.json"
            path_request = valid_authority_request()
            authority_path.write_text(json.dumps(path_request), encoding="utf-8")
            path_result = resolver.resolve_source_body_operational_authority_boundary_from_path(
                authority_path
            )
            mapping_result = self.resolve(path_request)

        self.assertEqual(OUTCOME_RECORDED, path_result["outcome"])
        self.assertEqual(set(mapping_result.keys()), set(path_result.keys()))
        self.assertEqual(
            str(authority_path),
            path_result["declared_authority_question"]["authority_request_path"],
        )

    def test_write_behavior_default_output_path_and_non_mutation(self) -> None:
        request = valid_authority_request()
        eligibility = request["selected_eligibility_result"]
        basis = request["source_body_authority_basis"]
        request_before = copy.deepcopy(request)
        eligibility_before = copy.deepcopy(eligibility)
        basis_before = copy.deepcopy(basis)
        result = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request_before, request)
        self.assertEqual(eligibility_before, eligibility)
        self.assertEqual(basis_before, basis)
        self.assertEqual(OUTCOME_RECORDED, second["outcome"])
        self.assertEqual(
            "integrity_host_v0_min_coexistence_source_body_operational_authority_boundary",
            resolver.SOURCE_BODY_OPERATIONAL_AUTHORITY_BOUNDARY_ROOT.name,
        )
        self.assertNotEqual(
            "integrity_host_v0_min_coexistence_distributed_operation_eligibility_boundary",
            resolver.SOURCE_BODY_OPERATIONAL_AUTHORITY_BOUNDARY_ROOT.name,
        )

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "authority.json"
            written = resolver.write_source_body_operational_authority_result(
                result, output_path
            )
            self.assertEqual(output_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            eligibility_path = Path(tmp) / "selected_eligibility.json"
            before_text = json.dumps(eligibility, sort_keys=True)
            eligibility_path.write_text(before_text, encoding="utf-8")
            path_request = valid_authority_request()
            path_request.pop("selected_eligibility_result")
            path_request["selected_eligibility_result_path"] = str(eligibility_path)
            self.resolve(path_request)
            self.assertEqual(before_text, eligibility_path.read_text(encoding="utf-8"))

            root = Path(tmp) / "default-root"
            with patch.object(resolver, "SOURCE_BODY_OPERATIONAL_AUTHORITY_BOUNDARY_ROOT", root):
                first = resolver.write_source_body_operational_authority_result(result)
                duplicate = resolver.write_source_body_operational_authority_result(result)
            self.assertEqual(root, first.parent)
            self.assertEqual(root, duplicate.parent)
            self.assertNotEqual(first, duplicate)
            self.assertIn("__source_body_operational_authority_result", first.name)
            self.assertIn("_001", duplicate.stem)

    def test_blocking_explicit_missing_malformed_and_authority_request_paths(self) -> None:
        blocked = self.resolve(
            valid_authority_request(intent="BLOCK_SOURCE_BODY_OPERATIONAL_AUTHORITY_REVIEW")
        )
        self.assert_blocked_with(blocked, "AUTHORITY_REQUEST_EXPLICITLY_BLOCKED")

        missing = resolver.resolve_source_body_operational_authority_boundary()
        self.assert_blocked_with(missing, "AUTHORITY_QUESTION_UNDECLARED")

        malformed = self.resolve(["not", "a", "mapping"])
        self.assert_blocked_with(malformed, "DECLARED_AUTHORITY_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as tmp:
            missing_path = Path(tmp) / "missing.json"
            unreadable = resolver.resolve_source_body_operational_authority_boundary_from_path(
                missing_path
            )
            self.assert_blocked_with(unreadable, "DECLARED_AUTHORITY_REQUEST_UNREADABLE")

            malformed_path = Path(tmp) / "malformed.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            malformed_json = resolver.resolve_source_body_operational_authority_boundary_from_path(
                malformed_path
            )
            self.assert_blocked_with(malformed_json, "DECLARED_AUTHORITY_REQUEST_MALFORMED")

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_source_body_operational_authority_boundary_from_path(
                array_path
            )
            self.assert_blocked_with(array_result, "DECLARED_AUTHORITY_REQUEST_MALFORMED")

    def test_blocking_selected_eligibility_path_and_identity_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_path = Path(tmp) / "missing_eligibility.json"
            request = valid_authority_request()
            request.pop("selected_eligibility_result")
            request["selected_eligibility_result_path"] = str(missing_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_ELIGIBILITY_RESULT_UNREADABLE",
            )

            malformed_path = Path(tmp) / "malformed_eligibility.json"
            malformed_path.write_text("{not valid json", encoding="utf-8")
            request["selected_eligibility_result_path"] = str(malformed_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_ELIGIBILITY_RESULT_MALFORMED",
            )

            array_path = Path(tmp) / "array_eligibility.json"
            array_path.write_text("[]", encoding="utf-8")
            request["selected_eligibility_result_path"] = str(array_path)
            self.assert_blocked_with(
                self.resolve(request),
                "SELECTED_ELIGIBILITY_RESULT_MALFORMED",
            )

        no_outcome = selected_eligibility_result()
        no_outcome.pop("outcome")
        no_outcome["distributed_operation_eligibility_summary"].pop("outcome")
        self.assert_blocked_with(
            self.resolve(valid_authority_request(eligibility=no_outcome)),
            "SELECTED_ELIGIBILITY_RESULT_OUTCOME_MISSING",
        )

        not_eligible = selected_eligibility_result(outcome="DISTRIBUTED_OPERATION_MATTER_NOT_ELIGIBLE_FOR_REVIEW")
        not_eligible["distributed_operation_eligibility_summary"]["outcome"] = (
            "DISTRIBUTED_OPERATION_MATTER_NOT_ELIGIBLE_FOR_REVIEW"
        )
        self.assert_blocked_with(
            self.resolve(valid_authority_request(eligibility=not_eligible)),
            "SELECTED_ELIGIBILITY_RESULT_NOT_ELIGIBLE",
        )

        failed = selected_eligibility_result()
        failed["distributed_operation_eligibility_summary"]["failed_check_count"] = 1
        self.assert_blocked_with(
            self.resolve(valid_authority_request(eligibility=failed)),
            "SELECTED_ELIGIBILITY_RESULT_HAS_FAILED_CHECKS",
        )

    def test_blocking_missing_required_basis(self) -> None:
        cases: list[tuple[str, callable[[dict], None]]] = []

        def missing_matter(request: dict) -> None:
            eligibility = request["selected_eligibility_result"]
            eligibility.pop("selected_matter_declaration", None)
            eligibility["eligibility_basis"].pop("selected_matter_declaration_result", None)
            eligibility["eligibility_basis"].pop("selected_matter_declaration", None)

        def missing_candidate(request: dict) -> None:
            eligibility = request["selected_eligibility_result"]
            eligibility.pop("selected_operation_candidate", None)
            eligibility["selected_matter_declaration"].pop("operation_candidate", None)
            eligibility["eligibility_basis"].pop("selected_operation_candidate", None)
            eligibility["eligibility_basis"].pop("selected_operation_candidate_identity", None)

        def missing_operation_matter(request: dict) -> None:
            eligibility = request["selected_eligibility_result"]
            eligibility.pop("selected_operation_matter", None)
            eligibility["selected_matter_declaration"].pop("operation_matter", None)
            eligibility["eligibility_basis"].pop("selected_operation_matter", None)

        def missing_lineage(request: dict) -> None:
            request.pop("source_body_lineage_basis", None)
            request["source_body_authority_basis"].pop("source_body_lineage_basis", None)
            request["source_body_authority_basis"].pop("source_body_basis", None)
            request["selected_eligibility_result"]["eligibility_basis"].pop("source_body_basis", None)

        def missing_reference(request: dict) -> None:
            request.pop("source_body_authority_reference", None)
            request["source_body_authority_basis"].pop("source_body_authority_reference", None)
            request["source_body_authority_basis"].pop("authority_reference", None)

        def missing_v4(request: dict) -> None:
            request.pop("current_body_conformance_v4_closure_basis", None)
            request["source_body_authority_basis"].pop("current_body_conformance_v4_closure_basis", None)
            request["selected_eligibility_result"]["eligibility_basis"].pop("current_body_conformance_v4_closure_basis", None)

        def missing_v9(request: dict) -> None:
            request.pop("current_self_orientation_v9_basis", None)
            request["source_body_authority_basis"].pop("current_self_orientation_v9_basis", None)
            request["selected_eligibility_result"]["eligibility_basis"].pop("current_self_orientation_v9_basis", None)

        def missing_refusal(request: dict) -> None:
            request.pop("refusal_abort_awareness", None)
            request["source_body_authority_basis"].pop("refusal_abort_awareness", None)
            eligibility = request["selected_eligibility_result"]
            eligibility.pop("refusal_abort_awareness", None)
            eligibility["eligibility_basis"].pop("selected_refusal_abort_awareness", None)
            eligibility["eligibility_basis"].pop("refusal_abort_awareness", None)
            eligibility["selected_matter_declaration"].pop("refusal_abort_awareness", None)

        cases.extend(
            [
                ("SELECTED_MATTER_DECLARATION_MISSING", missing_matter),
                ("SELECTED_OPERATION_CANDIDATE_MISSING", missing_candidate),
                ("SELECTED_OPERATION_MATTER_MISSING", missing_operation_matter),
                ("SOURCE_BODY_LINEAGE_BASIS_MISSING", missing_lineage),
                ("SOURCE_BODY_AUTHORITY_REFERENCE_MISSING", missing_reference),
                ("CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BASIS_MISSING", missing_v4),
                ("CURRENT_SELF_ORIENTATION_V9_BASIS_MISSING", missing_v9),
                ("REFUSAL_ABORT_AWARENESS_MISSING", missing_refusal),
            ]
        )
        for expected_code, mutate in cases:
            with self.subTest(expected_code=expected_code):
                request = valid_authority_request()
                mutate(request)
                self.assert_blocked_with(self.resolve(request), expected_code)

    def test_blocking_authority_review_collapse_flags(self) -> None:
        cases = (
            ("authority_granted", "AUTHORITY_REVIEW_GRANTS_AUTHORITY"),
            ("authority_created", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("permission_created", "AUTHORITY_REVIEW_CREATES_PERMISSION"),
            ("operation_admitted", "AUTHORITY_REVIEW_ADMITS_OPERATION"),
            ("operation_authorized", "AUTHORITY_REVIEW_AUTHORIZES_OPERATION"),
            ("operation_executed", "AUTHORITY_REVIEW_EXECUTES_OPERATION"),
            ("carrier_roles_defined", "AUTHORITY_REVIEW_DEFINES_CARRIER_ROLES"),
            ("repository_synchronization_authorized", "AUTHORITY_REVIEW_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "AUTHORITY_REVIEW_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "AUTHORITY_REVIEW_CREATES_SECOND_BODY"),
            ("continuation_authorized", "AUTHORITY_REVIEW_AUTHORIZES_CONTINUATION"),
            ("carrier_currentness_created", "AUTHORITY_REVIEW_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "AUTHORITY_REVIEW_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "AUTHORITY_REVIEW_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "AUTHORITY_REVIEW_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "AUTHORITY_REVIEW_REPLACES_SOURCE"),
            ("truth_created", "AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("action_authorized", "AUTHORITY_REVIEW_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "AUTHORITY_REVIEW_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "AUTHORITY_REVIEW_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "AUTHORITY_REVIEW_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "AUTHORITY_REVIEW_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "AUTHORITY_REVIEW_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "AUTHORITY_REVIEW_SCHEDULES_FOLLOW_ON_WORK"),
            ("carrier_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("registry_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("lifecycle_posture_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("currentness_successor_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("distributed_standing_posture_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("eligibility_result_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("successful_receipt_count_becomes_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("majority_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("latest_file_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
            ("current_turn_authority", "AUTHORITY_REVIEW_CREATES_AUTHORITY"),
        )
        for field, expected_code in cases:
            with self.subTest(field=field):
                request = valid_authority_request()
                request[field] = True
                if field in request["declared_non_claims"]:
                    request["declared_non_claims"][field] = True
                else:
                    request["source_body_authority_basis"][field] = True
                self.assert_blocked_with(self.resolve(request), expected_code)

    def test_blocking_mutation_replay_merge_and_nonclaim_missing_or_flipped(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = valid_authority_request()
                request[field] = True
                self.assert_blocked_with(
                    self.resolve(request),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing = valid_authority_request()
        missing["declared_non_claims"].pop("authority_granted")
        self.assert_blocked_with(missing_result := self.resolve(missing), "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertEqual(OUTCOME_BLOCKED, missing_result["outcome"])

        flipped = valid_authority_request()
        flipped["declared_non_claims"]["authority_granted"] = True
        self.assert_blocked_with(
            self.resolve(flipped),
            {"AUTHORITY_REVIEW_GRANTS_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_non_claims_false_for_all_outcome_families(self) -> None:
        results = [
            self.resolve(valid_authority_request()),
            self.resolve(
                valid_authority_request(
                    requested_outcome=OUTCOME_NOT_SUFFICIENT,
                    not_sufficient_reason="not sufficient",
                )
            ),
            self.resolve(
                valid_authority_request(
                    requested_outcome=OUTCOME_ADDITIONAL,
                    additional_basis_context={"reason": "additional basis required"},
                )
            ),
            resolver.resolve_source_body_operational_authority_boundary(),
        ]
        self.assertEqual(
            {
                OUTCOME_RECORDED,
                OUTCOME_NOT_SUFFICIENT,
                OUTCOME_ADDITIONAL,
                OUTCOME_BLOCKED,
            },
            {result["outcome"] for result in results},
        )
        for result in results:
            self.assert_required_non_claims_false(result)


if __name__ == "__main__":
    unittest.main()
