"""Tests for bounded distributed operation matter declaration.

This suite proves that the resolver declares one operation candidate as one
bounded matter for possible future eligibility review only. It does not decide
eligibility, admit operation, authorize operation, execute operation,
synchronize repositories, transfer the full body, create a second body,
authorize continuation, create consequence, create public readiness, schedule
follow-on work, or mutate upstream artifacts.
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

import resolve_distributed_operation_matter_declaration as resolver


TOP_LEVEL_SECTIONS = {
    "distributed_operation_matter_declaration_metadata",
    "declared_matter_question",
    "operation_candidate",
    "operation_matter",
    "operation_purpose",
    "proposed_operation_kind",
    "selected_operation_basis",
    "selected_carrier_context",
    "proposed_affected_surfaces",
    "proposed_output_family",
    "eligibility_review_request",
    "refusal_abort_awareness",
    "matter_declaration_checks",
    "matter_declaration_statement",
    "matter_declaration_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_operation_matter_declaration_summary",
}

SUPPORTED_KINDS = (
    "DISTRIBUTED_READINESS_REVIEW_CANDIDATE",
    "DISTRIBUTED_ARTIFACT_RECEIPT_REVIEW_CANDIDATE",
    "DISTRIBUTED_CARRIER_STATUS_REVIEW_CANDIDATE",
    "DISTRIBUTED_BOUNDARY_CONFORMANCE_REVIEW_CANDIDATE",
    "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
)

REQUIRED_NON_CLAIMS = (
    "operation_admitted",
    "operation_authorized",
    "operation_executed",
    "eligibility_decided",
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


def operation_candidate() -> dict:
    return {
        "operation_candidate_id": "distributed_operation_candidate_001",
        "declared_operation_question": (
            "May this candidate be reviewed for distributed operation eligibility?"
        ),
        "candidate_visible_as_candidate_only": True,
        "candidate_not_admitted": True,
        "candidate_not_authorized": True,
        "candidate_not_executed": True,
        "candidate_not_eligible_by_declaration": True,
        "candidate_not_scheduled_for_operation": True,
    }


def operation_matter() -> dict:
    return {
        "operation_matter_id": "distributed_operation_matter_001",
        "operation_candidate_id": "distributed_operation_candidate_001",
        "relation_to_operation_candidate": "declares one bounded candidate matter",
        "declared_matter_scope": {
            "scope_id": "distributed_operation_matter_scope_001",
            "one_bounded_matter_only": True,
        },
        "matter_declaration_is_not_eligibility": True,
        "matter_declaration_is_not_admission": True,
        "matter_declaration_is_not_operation": True,
        "matter_declaration_is_not_execution": True,
        "matter_declaration_is_not_permission": True,
    }


def operation_purpose() -> dict:
    return {
        "declared_operation_purpose": (
            "Make one candidate visible for a later bounded eligibility boundary."
        ),
        "purpose_is_not_permission": True,
        "purpose_is_not_operation_plan": True,
        "purpose_is_not_output_authorization": True,
        "purpose_is_not_follow_on_work_authorization": True,
    }


def selected_operation_basis() -> dict:
    return {
        "source_body_basis": {
            "basis_id": "source_body_basis_001",
            "source_body_lineage_preserved": True,
        },
        "current_body_conformance_v4_closure_basis": {
            "basis_id": "current_body_conformance_v4_closure_basis_001",
            "outcome": "CURRENT_BODY_CONFORMANCE_V4_CLOSED",
            "closure_is_not_operation": True,
        },
        "current_self_orientation_v9_basis": {
            "basis_id": "current_self_orientation_v9_basis_001",
            "outcome": "CURRENT_SELF_ORIENTATION_V9_RECORDED",
            "v9_did_not_authorize_operation": True,
        },
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_basis_001",
            "outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED",
            "distributed_standing_did_not_authorize_operation": True,
        },
        "reference_grounding": [
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            "reference/IAMMAI/RANKED_SURFACE_INDEX.md",
        ],
        "basis_is_not_permission_set": True,
        "basis_is_not_operation_plan": True,
        "basis_is_not_synchronization_plan": True,
        "basis_is_not_full_body_transfer_plan": True,
        "basis_is_not_final_governance": True,
    }


def selected_carrier_context() -> dict:
    return {
        "carrier_b_success_as_evidence_context_only": True,
        "carrier_c_block_as_evidence_context_only": True,
        "b_c_divergence_as_visible_context_only": True,
        "refusal_and_blocked_attempts_remain_visible": True,
        "projection_mismatch_remains_visible_where_supplied": True,
        "selected_carriers_are_context_not_operational_participants": True,
        "no_current_carrier_selected": True,
        "no_winning_carrier_selected": True,
        "no_losing_carrier_invalidated": True,
        "no_carrier_currentness_created": True,
    }


def eligibility_review_request() -> dict:
    return {
        "request_for_future_eligibility_review": True,
        "eligibility_is_not_decided": True,
        "eligibility_review_is_not_scheduled": True,
        "eligibility_review_is_not_authorized_by_declaration": True,
        "eligibility_boundary_remains_open": True,
    }


def refusal_abort_awareness() -> dict:
    return {
        "awareness_that_operation_may_later_be_blocked": True,
        "awareness_that_eligibility_may_fail": True,
        "awareness_that_carrier_refusal_must_remain_visible": True,
        "awareness_that_operation_admission_must_include_abort_refusal_conditions": True,
        "awareness_that_no_operation_may_proceed_without_later_refusal_abort_boundary": True,
        "awareness_that_abort_refusal_is_part_of_operation_law": True,
        "refusal_abort_awareness_is_not_abort_mechanism_by_itself": True,
        "refusal_abort_awareness_is_not_admission": True,
        "refusal_abort_awareness_is_not_operation": True,
    }


def valid_request(
    *,
    intent: str = "DECLARE_DISTRIBUTED_OPERATION_MATTER",
    kind: str = "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
    include_carrier_context: bool = True,
) -> dict:
    basis = selected_operation_basis()
    request = resolver.build_declared_distributed_operation_matter_request(
        "distributed_operation_matter_declaration_request_001",
        "Has one distributed operation candidate been declared as a bounded matter?",
        operation_candidate(),
        operation_matter(),
        operation_purpose(),
        kind,
        basis,
        [
            "spec/DISTRIBUTED_OPERATION_MATTER_DECLARATION_V0_MIN_SPEC.md",
            "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_v4_closure/",
        ],
        ["DISTRIBUTED_OPERATION_MATTER_DECLARATION_RESULT"],
        eligibility_review_request(),
        refusal_abort_awareness(),
        intent,
        selected_carrier_context=(
            selected_carrier_context() if include_carrier_context else None
        ),
    )
    request["matter_scope"] = {
        "scope_id": "distributed_operation_matter_scope_001",
        "one_bounded_matter_only": True,
    }
    request["current_self_orientation_v9_basis"] = basis["current_self_orientation_v9_basis"]
    request["reference_grounding"] = basis["reference_grounding"]
    return request


def resolve_request(request: dict | None = None) -> dict:
    return resolver.resolve_distributed_operation_matter_declaration(
        declared_matter_request=valid_request() if request is None else request
    )


def failed_codes(result: dict) -> set:
    return {
        check.get("block_code")
        for check in result["matter_declaration_checks"]
        if check.get("passed") is not True and check.get("block_code")
    }


class DistributedOperationMatterDeclarationTests(unittest.TestCase):
    def assertDeclared(self, result: dict) -> None:
        self.assertEqual("DISTRIBUTED_OPERATION_MATTER_DECLARED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["distributed_operation_matter_declaration_summary"]["failed_check_count"])
        self.assertTrue(result["matter_declaration_statement"]["distributed_operation_matter_declared"])

    def assertBlockedWith(self, result: dict, code: str | set[str]) -> None:
        self.assertEqual("DISTRIBUTED_OPERATION_MATTER_DECLARATION_BLOCKED", result["outcome"])
        if isinstance(code, set):
            self.assertIn(result["block"]["block_code"], code)
        else:
            self.assertEqual(code, result["block"]["block_code"])
        self.assertFalse(result["matter_declaration_statement"]["distributed_operation_matter_declared"])

    def assertAllResultNonClaimsFalse(self, result: dict) -> None:
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_matter_declaration_from_mapping(self) -> None:
        request = valid_request()
        request_before = copy.deepcopy(request)

        result = resolve_request(request)

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertDeclared(result)
        summary = result["distributed_operation_matter_declaration_summary"]
        statement = result["matter_declaration_statement"]
        self.assertEqual(42, summary["passed_check_count"])
        self.assertEqual(0, summary["failed_check_count"])
        for key in (
            "operation_candidate_preserved",
            "operation_matter_preserved",
            "operation_purpose_preserved",
            "proposed_operation_kind_preserved",
            "selected_operation_basis_preserved",
            "selected_carrier_context_preserved",
            "proposed_affected_surfaces_preserved",
            "proposed_output_family_preserved",
            "eligibility_review_request_preserved",
            "refusal_abort_awareness_preserved",
        ):
            self.assertIs(statement[key], True, key)
        for key in (
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "eligibility_decided",
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
            self.assertIs(statement[key], False, key)
        self.assertEqual(request_before, request)

    def test_metadata_and_declared_matter_question(self) -> None:
        result = resolve_request()
        metadata = result["distributed_operation_matter_declaration_metadata"]
        for key in (
            "distributed_operation_matter_declaration_result_id",
            "distributed_operation_matter_declaration_result_type",
            "distributed_operation_matter_declaration_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["distributed_operation_matter_declaration_result_version"])
        self.assertEqual("resolve_distributed_operation_matter_declaration", metadata["resolver_module"])

        declared = result["declared_matter_question"]
        self.assertEqual(
            "distributed_operation_matter_declaration_request_001",
            declared["matter_declaration_request_id"],
        )
        self.assertEqual(
            "Has one distributed operation candidate been declared as a bounded matter?",
            declared["matter_declaration_question"],
        )
        self.assertEqual("DECLARE_DISTRIBUTED_OPERATION_MATTER", declared["matter_declaration_intent"])
        for key in (
            "matter_declaration_is_not_eligibility",
            "matter_declaration_is_not_admission",
            "matter_declaration_is_not_operation",
            "matter_declaration_is_not_execution",
            "matter_declaration_is_not_synchronization",
            "matter_declaration_is_not_full_body_transfer",
            "matter_declaration_is_not_continuation",
            "matter_declaration_is_not_permission",
            "matter_declaration_does_not_mutate_upstream_artifacts",
        ):
            self.assertIs(declared[key], True, key)

    def test_operation_candidate_matter_and_purpose_sections(self) -> None:
        result = resolve_request()
        candidate = result["operation_candidate"]
        self.assertEqual("distributed_operation_candidate_001", candidate["operation_candidate_id"])
        self.assertEqual(
            "May this candidate be reviewed for distributed operation eligibility?",
            candidate["declared_operation_question"],
        )
        for key in (
            "candidate_visible_as_candidate_only",
            "candidate_not_admitted",
            "candidate_not_authorized",
            "candidate_not_executed",
            "candidate_not_eligible_by_declaration",
            "candidate_not_scheduled_for_operation",
        ):
            self.assertIs(candidate[key], True, key)

        matter = result["operation_matter"]
        self.assertEqual("distributed_operation_matter_001", matter["operation_matter_id"])
        self.assertEqual("distributed_operation_candidate_001", matter["operation_candidate_id"])
        self.assertTrue(matter["declared_matter_scope"]["one_bounded_matter_only"])
        for key in (
            "matter_is_one_bounded_matter_only",
            "matter_declaration_is_not_eligibility",
            "matter_declaration_is_not_admission",
            "matter_declaration_is_not_operation",
            "matter_declaration_is_not_execution",
            "matter_declaration_is_not_permission",
        ):
            self.assertIs(matter[key], True, key)

        purpose = result["operation_purpose"]
        self.assertIn("later bounded eligibility boundary", purpose["declared_operation_purpose"])
        for key in (
            "purpose_is_not_permission",
            "purpose_is_not_operation_plan",
            "purpose_is_not_output_authorization",
            "purpose_is_not_follow_on_work_authorization",
        ):
            self.assertIs(purpose[key], True, key)

    def test_supported_operation_kinds_and_unspecified_kind_blocks(self) -> None:
        for kind in SUPPORTED_KINDS:
            with self.subTest(kind=kind):
                result = resolve_request(valid_request(kind=kind))
                self.assertDeclared(result)
                kind_section = result["proposed_operation_kind"]
                self.assertEqual(kind, kind_section["proposed_operation_kind"])
                self.assertIs(kind_section["kind_supported"], True)
                for key in (
                    "kind_is_candidate_kind_only",
                    "kind_is_not_authorization",
                    "kind_is_not_admission",
                    "kind_is_not_execution",
                    "kind_is_not_operation",
                ):
                    self.assertIs(kind_section[key], True, key)

        blocked = resolve_request(
            valid_request(kind="DISTRIBUTED_OPERATION_KIND_UNSPECIFIED_BLOCKED")
        )
        self.assertBlockedWith(blocked, "OPERATION_KIND_UNSUPPORTED")

    def test_selected_operation_basis_and_carrier_context(self) -> None:
        result = resolve_request()
        basis = result["selected_operation_basis"]
        self.assertEqual("source_body_basis_001", basis["selected_source_body_basis"]["basis_id"])
        self.assertEqual(
            "CURRENT_BODY_CONFORMANCE_V4_CLOSED",
            basis["current_body_conformance_v4_closure_basis"]["outcome"],
        )
        self.assertEqual(
            "CURRENT_SELF_ORIENTATION_V9_RECORDED",
            basis["current_self_orientation_v9_basis"]["outcome"],
        )
        self.assertEqual(
            "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED",
            basis["distributed_standing_basis"]["outcome"],
        )
        self.assertTrue(basis["read_only_reference_grounding"])
        for key in (
            "basis_is_not_permission_set",
            "basis_is_not_operation_plan",
            "basis_is_not_synchronization_plan",
            "basis_is_not_full_body_transfer_plan",
            "basis_is_not_final_governance",
        ):
            self.assertIs(basis[key], True, key)

        carrier = result["selected_carrier_context"]
        self.assertIs(carrier["selected_carrier_context_supplied"], True)
        self.assertIs(carrier["selected_carrier_context_preserved"], True)
        for key in (
            "carrier_b_success_as_evidence_context_only",
            "carrier_c_block_as_evidence_context_only",
            "b_c_divergence_as_visible_context_only",
            "refusal_and_blocked_attempts_remain_visible",
            "projection_mismatch_remains_visible_where_supplied",
            "selected_carriers_are_context_not_operational_participants",
            "no_current_carrier_selected",
            "no_winning_carrier_selected",
            "no_losing_carrier_invalidated",
            "no_carrier_currentness_created",
        ):
            self.assertIs(carrier[key], True, key)

    def test_carrier_context_can_be_omitted(self) -> None:
        result = resolve_request(valid_request(include_carrier_context=False))
        self.assertDeclared(result)
        self.assertIs(result["selected_carrier_context"]["selected_carrier_context_supplied"], False)
        self.assertIs(result["selected_carrier_context"]["selected_carrier_context_preserved"], False)
        self.assertIs(
            result["matter_declaration_statement"]["selected_carrier_context_preserved"],
            False,
        )

    def test_surfaces_output_eligibility_and_refusal_abort_awareness(self) -> None:
        result = resolve_request()
        surfaces = result["proposed_affected_surfaces"]
        self.assertTrue(surfaces["declared_affected_surfaces"])
        for key in (
            "affected_surfaces_are_proposed_only",
            "no_surface_is_mutated",
            "no_surface_is_synchronized",
            "no_surface_is_transferred",
            "no_surface_is_executed",
            "no_output_is_emitted_by_declaration",
        ):
            self.assertIs(surfaces[key], True, key)

        output = result["proposed_output_family"]
        self.assertEqual(
            ["DISTRIBUTED_OPERATION_MATTER_DECLARATION_RESULT"],
            output["declared_proposed_output_family"],
        )
        for key in (
            "output_family_is_named_only",
            "output_family_is_not_authorized",
            "output_family_is_not_emitted",
            "output_family_does_not_create_consequence",
            "output_family_does_not_authorize_future_outputs",
        ):
            self.assertIs(output[key], True, key)

        eligibility = result["eligibility_review_request"]
        for key in (
            "request_for_future_eligibility_review",
            "eligibility_is_not_decided",
            "eligibility_review_is_not_scheduled",
            "eligibility_review_is_not_authorized_by_declaration",
            "eligibility_boundary_remains_open",
            "declaration_is_only_prerequisite_visibility",
        ):
            self.assertIs(eligibility[key], True, key)

        awareness = result["refusal_abort_awareness"]
        for key in (
            "awareness_that_operation_may_later_be_blocked",
            "awareness_that_eligibility_may_fail",
            "awareness_that_carrier_refusal_must_remain_visible",
            "awareness_that_operation_admission_must_include_abort_refusal_conditions",
            "awareness_that_no_operation_may_proceed_without_later_refusal_abort_boundary",
            "awareness_that_abort_refusal_is_part_of_operation_law",
            "refusal_abort_awareness_is_not_abort_mechanism_by_itself",
            "refusal_abort_awareness_is_not_admission",
            "refusal_abort_awareness_is_not_operation",
        ):
            self.assertIs(awareness[key], True, key)

    def test_matter_declaration_checks(self) -> None:
        result = resolve_request()
        checks = result["matter_declaration_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"], check["check_name"])

        names = {check["check_name"] for check in checks}
        expected_names = {
            "matter declaration question declared",
            "matter declaration intent supported",
            "operation candidate id present",
            "operation matter id present",
            "operation question present",
            "operation purpose present",
            "proposed operation kind supported",
            "source-body basis present",
            "current body orientation conformance basis present",
            "distributed standing or v4 closure basis present where claimed",
            "selected carrier context parseable where supplied",
            "proposed affected surfaces present",
            "proposed output family present",
            "eligibility review request present",
            "refusal abort awareness present",
            "declaration does not admit operation",
            "declaration does not authorize operation",
            "declaration does not execute operation",
            "declaration does not authorize repository synchronization",
            "declaration does not authorize full body transfer",
            "declaration does not create second body",
            "declaration does not authorize continuation",
            "declaration does not create carrier currentness",
            "declaration does not select current carrier",
            "declaration does not select winning carrier",
            "declaration does not invalidate losing carrier",
            "declaration does not replace source",
            "declaration does not create authority",
            "declaration does not create permission",
            "declaration does not create truth",
            "declaration does not authorize action",
            "declaration does not create consequence",
            "declaration does not resolve divergence",
            "declaration does not erase evidence",
            "declaration does not erase refusal",
            "declaration does not create public readiness",
            "declaration does not claim final completion",
            "declaration does not schedule follow-on work",
            "declaration does not schedule self-orientation successor",
            "no mutation replay or merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_statement_non_meaning_open_surfaces_summary_and_nonclaims(self) -> None:
        result = resolve_request()
        statement = result["matter_declaration_statement"]
        summary = resolver.build_distributed_operation_matter_declaration_summary(result)
        self.assertEqual(result["distributed_operation_matter_declaration_summary"], summary)
        for key in (
            "distributed_operation_matter_declared",
            "operation_candidate_preserved",
            "operation_matter_preserved",
            "operation_purpose_preserved",
            "proposed_operation_kind_preserved",
            "selected_operation_basis_preserved",
            "selected_carrier_context_preserved",
            "proposed_affected_surfaces_preserved",
            "proposed_output_family_preserved",
            "eligibility_review_request_preserved",
            "refusal_abort_awareness_preserved",
        ):
            self.assertIs(statement[key], True, key)
            self.assertIs(summary[key], True, key)
        for key in (
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "eligibility_decided",
        ):
            self.assertIs(summary[key], False, key)
        for key in (
            "no_sync_full_body_transfer_second_body",
            "no_continuation_distributed_operation",
            "no_carrier_currentness_current_winning_losing_carrier",
            "no_source_authority_permission_truth_action_consequence",
            "no_public_readiness_final_completion_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)

        non_meaning = result["matter_declaration_non_meaning"]
        for key in (
            "operation_eligible",
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "operation_conformed",
            "operation_closed",
            "repository_synchronization",
            "full_body_transfer",
            "second_body",
            "continuation",
            "distributed_operation",
            "carrier_currentness",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "source_replacement",
            "authority",
            "permission",
            "truth",
            "action",
            "consequence",
            "divergence_resolution",
            "evidence_erasure",
            "public_launch_readiness",
            "final_completion",
            "final_governance",
            "final_continuity_completion",
            "final_system_identity",
            "follow_on_work_authorization",
            "current_self_orientation_v10",
        ):
            self.assertIs(non_meaning[key], True, key)
            self.assertIs(non_meaning[f"does_not_mean_{key}"], True, key)

        open_items = result["what_remains_open"]
        for key in (
            "distributed_operation_eligibility_boundary",
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
            self.assertEqual("open_not_scheduled_not_authorized_not_executed", open_items[key])
        self.assertIs(open_items["open_means_not_scheduled"], True)
        self.assertIs(open_items["open_means_not_authorized"], True)
        self.assertIs(open_items["open_means_not_executed"], True)
        self.assertAllResultNonClaimsFalse(result)

    def test_nonclaims_for_declared_not_declared_and_blocked(self) -> None:
        declared = resolve_request()
        not_declared = resolve_request(
            valid_request(intent="DO_NOT_DECLARE_DISTRIBUTED_OPERATION_MATTER")
        )
        blocked = resolver.resolve_distributed_operation_matter_declaration()
        for result in (declared, not_declared, blocked):
            with self.subTest(outcome=result["outcome"]):
                self.assertIn(result["outcome"], resolver.SUPPORTED_OUTCOMES)
                self.assertAllResultNonClaimsFalse(result)

    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        request = valid_request()
        self.assertEqual(
            "distributed_operation_matter_declaration_request_001",
            request["matter_declaration_request_id"],
        )
        self.assertEqual(
            "Has one distributed operation candidate been declared as a bounded matter?",
            request["matter_declaration_question"],
        )
        self.assertEqual(operation_candidate(), request["operation_candidate"])
        self.assertEqual(operation_matter(), request["operation_matter"])
        self.assertEqual(operation_purpose(), request["operation_purpose"])
        self.assertEqual(
            "DISTRIBUTED_OPERATION_ELIGIBILITY_REVIEW_CANDIDATE",
            request["proposed_operation_kind"],
        )
        self.assertTrue(request["selected_operation_basis"])
        self.assertTrue(request["proposed_affected_surfaces"])
        self.assertTrue(request["proposed_output_family"])
        self.assertTrue(request["eligibility_review_request"])
        self.assertTrue(request["refusal_abort_awareness"])
        self.assertTrue(request["selected_carrier_context"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)
        self.assertDeclared(resolve_request(request))

    def test_path_based_matter_request(self) -> None:
        request = valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "declared_matter_request.json"
            path.write_text(json.dumps(request), encoding="utf-8")
            result = resolver.resolve_distributed_operation_matter_declaration_from_path(path)

        self.assertDeclared(result)
        self.assertEqual(
            set(resolve_request(request)),
            set(result),
        )
        self.assertTrue(result["declared_matter_question"]["declared_matter_request_path"])

    def test_write_behavior_and_default_output_path(self) -> None:
        result = resolve_request()
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "matter_result.json"
            written = resolver.write_distributed_operation_matter_declaration_result(
                result,
                explicit,
            )
            self.assertEqual(explicit, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            root = Path(tmp) / "bounded_default_root"
            with patch.object(
                resolver,
                "DISTRIBUTED_OPERATION_MATTER_DECLARATION_ROOT",
                root,
            ):
                first = resolver.write_distributed_operation_matter_declaration_result(result)
                second = resolver.write_distributed_operation_matter_declaration_result(result)
            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__distributed_operation_matter_declaration_result.json"))
            self.assertIn("_001", second.stem)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        before = copy.deepcopy(request)
        candidate_before = copy.deepcopy(request["operation_candidate"])
        matter_before = copy.deepcopy(request["operation_matter"])
        basis_before = copy.deepcopy(request["selected_operation_basis"])
        carrier_before = copy.deepcopy(request["selected_carrier_context"])

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(before, request)
        self.assertEqual(candidate_before, request["operation_candidate"])
        self.assertEqual(matter_before, request["operation_matter"])
        self.assertEqual(basis_before, request["selected_operation_basis"])
        self.assertEqual(carrier_before, request["selected_carrier_context"])
        self.assertDeclared(first)
        self.assertDeclared(second)
        with tempfile.TemporaryDirectory() as tmp:
            written = resolver.write_distributed_operation_matter_declaration_result(
                first,
                Path(tmp) / "additive_result.json",
            )
            self.assertTrue(written.exists())
        self.assertEqual(before, request)

    def test_not_declared_readable_request(self) -> None:
        request = valid_request(intent="DO_NOT_DECLARE_DISTRIBUTED_OPERATION_MATTER")
        request["not_declared_reason"] = "Matter declaration intentionally not recorded."
        result = resolve_request(request)

        self.assertEqual("DISTRIBUTED_OPERATION_MATTER_NOT_DECLARED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertFalse(result["matter_declaration_statement"]["distributed_operation_matter_declared"])
        self.assertEqual(
            "Matter declaration intentionally not recorded.",
            result["matter_declaration_statement"]["not_declared_reason"],
        )
        for key in (
            "operation_admitted",
            "operation_authorized",
            "operation_executed",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "follow_on_work_authorized",
        ):
            self.assertIs(result["matter_declaration_statement"][key], False, key)

    def test_blocking_explicit_missing_malformed_and_path_cases(self) -> None:
        blocked = valid_request(intent="BLOCK_DISTRIBUTED_OPERATION_MATTER_DECLARATION")
        result = resolve_request(blocked)
        self.assertBlockedWith(result, "MATTER_DECLARATION_REQUEST_EXPLICITLY_BLOCKED")

        self.assertBlockedWith(
            resolver.resolve_distributed_operation_matter_declaration(),
            "MATTER_DECLARATION_QUESTION_UNDECLARED",
        )
        self.assertBlockedWith(
            resolver.resolve_distributed_operation_matter_declaration("not a mapping"),
            {
                "DECLARED_MATTER_REQUEST_MALFORMED",
                "DECLARED_MATTER_DECLARATION_REQUEST_MALFORMED",
            },
        )

        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            malformed = Path(tmp) / "malformed.json"
            array = Path(tmp) / "array.json"
            malformed.write_text("{not valid json", encoding="utf-8")
            array.write_text("[]", encoding="utf-8")

            self.assertBlockedWith(
                resolver.resolve_distributed_operation_matter_declaration_from_path(missing),
                {
                    "DECLARED_MATTER_REQUEST_UNREADABLE",
                    "DECLARED_MATTER_DECLARATION_REQUEST_UNREADABLE",
                },
            )
            self.assertBlockedWith(
                resolver.resolve_distributed_operation_matter_declaration_from_path(malformed),
                {
                    "DECLARED_MATTER_REQUEST_MALFORMED",
                    "DECLARED_MATTER_DECLARATION_REQUEST_MALFORMED",
                },
            )
            self.assertBlockedWith(
                resolver.resolve_distributed_operation_matter_declaration_from_path(array),
                {
                    "DECLARED_MATTER_REQUEST_MALFORMED",
                    "DECLARED_MATTER_DECLARATION_REQUEST_MALFORMED",
                },
            )

    def test_blocking_required_declaration_fields(self) -> None:
        def remove_candidate_id(request: dict) -> None:
            request["operation_candidate"].pop("operation_candidate_id", None)
            request["operation_candidate"].pop("candidate_id", None)
            request["operation_candidate"].pop("id", None)

        def remove_matter_id(request: dict) -> None:
            request["operation_matter"].pop("operation_matter_id", None)
            request["operation_matter"].pop("matter_id", None)
            request["operation_matter"].pop("id", None)

        def remove_operation_question(request: dict) -> None:
            request.pop("operation_question", None)
            request["operation_candidate"].pop("declared_operation_question", None)
            request["operation_candidate"].pop("operation_question", None)
            request["operation_matter"].pop("declared_operation_question", None)
            request["operation_matter"].pop("operation_question", None)

        def remove_source_basis(request: dict) -> None:
            request.pop("source_body_basis", None)
            request["selected_operation_basis"].pop("source_body_basis", None)
            request["selected_operation_basis"].pop("selected_source_body_basis", None)
            request["selected_operation_basis"].pop("source_body_lineage", None)

        def remove_current_body_basis(request: dict) -> None:
            request.pop("current_body_conformance_v4_closure_basis", None)
            request.pop("current_self_orientation_v9_basis", None)
            for key in (
                "current_body_orientation_conformance_basis",
                "selected_current_body_orientation_conformance_basis",
                "current_body_conformance_v4_closure_basis",
                "current_self_orientation_v9_basis",
            ):
                request["selected_operation_basis"].pop(key, None)

        def remove_distributed_or_v4_basis(request: dict) -> None:
            request.pop("distributed_standing_basis", None)
            request.pop("current_body_conformance_v4_closure_basis", None)
            for key in (
                "distributed_standing_basis",
                "selected_distributed_standing_basis",
                "current_body_conformance_v4_closure_basis",
                "distributed_standing_or_v4_closure_basis",
            ):
                request["selected_operation_basis"].pop(key, None)

        cases = (
            ("matter question", lambda r: r.pop("matter_declaration_question", None), "MATTER_DECLARATION_QUESTION_UNDECLARED"),
            ("candidate id", remove_candidate_id, "OPERATION_CANDIDATE_ID_MISSING"),
            ("matter id", remove_matter_id, "OPERATION_MATTER_ID_MISSING"),
            ("operation question", remove_operation_question, "OPERATION_QUESTION_MISSING"),
            ("operation purpose", lambda r: r.__setitem__("operation_purpose", ""), "OPERATION_PURPOSE_MISSING"),
            ("operation kind", lambda r: r.__setitem__("proposed_operation_kind", "UNSUPPORTED_OPERATION_KIND"), "OPERATION_KIND_UNSUPPORTED"),
            ("source basis", remove_source_basis, "SOURCE_BODY_BASIS_MISSING"),
            ("current body basis", remove_current_body_basis, "CURRENT_BODY_ORIENTATION_CONFORMANCE_BASIS_MISSING"),
            ("distributed or v4 basis", remove_distributed_or_v4_basis, "DISTRIBUTED_STANDING_OR_V4_CLOSURE_BASIS_MISSING"),
            ("affected surfaces", lambda r: r.__setitem__("proposed_affected_surfaces", []), "PROPOSED_AFFECTED_SURFACES_MISSING"),
            ("output family", lambda r: r.__setitem__("proposed_output_family", []), "PROPOSED_OUTPUT_FAMILY_MISSING"),
            ("eligibility review", lambda r: r.__setitem__("eligibility_review_request", {}), "ELIGIBILITY_REVIEW_REQUEST_MISSING"),
            ("refusal abort", lambda r: r.__setitem__("refusal_abort_awareness", {}), "REFUSAL_ABORT_AWARENESS_MISSING"),
        )
        for label, mutate, code in cases:
            with self.subTest(label=label):
                request = valid_request()
                mutate(request)
                self.assertBlockedWith(resolve_request(request), code)

    def test_malformed_carrier_context_blocks(self) -> None:
        request = valid_request()
        request["selected_carrier_context"] = "carrier context must not be a string"
        self.assertBlockedWith(
            resolve_request(request),
            "SELECTED_CARRIER_CONTEXT_MALFORMED",
        )

    def test_blocking_operation_collapse_flags(self) -> None:
        cases = (
            ("operation_admitted", "DECLARATION_ADMITS_OPERATION"),
            ("operation_authorized", "DECLARATION_AUTHORIZES_OPERATION"),
            ("distributed_operation_authorized", "DECLARATION_AUTHORIZES_OPERATION"),
            ("operation_executed", "DECLARATION_EXECUTES_OPERATION"),
            ("repository_synchronization_authorized", "DECLARATION_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "DECLARATION_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "DECLARATION_CREATES_SECOND_BODY"),
            ("continuation_authorized", "DECLARATION_AUTHORIZES_CONTINUATION"),
            ("carrier_currentness_created", "DECLARATION_CREATES_CARRIER_CURRENTNESS"),
            ("current_carrier_selected", "DECLARATION_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "DECLARATION_SELECTS_WINNING_CARRIER"),
            ("losing_carrier_invalidated", "DECLARATION_INVALIDATES_LOSING_CARRIER"),
            ("source_replaced", "DECLARATION_REPLACES_SOURCE"),
            ("authority_created", "DECLARATION_CREATES_AUTHORITY"),
            ("permission_created", "DECLARATION_CREATES_PERMISSION"),
            ("truth_created", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
            ("action_authorized", "DECLARATION_CREATES_TRUTH_OR_ACTION"),
            ("consequence_created", "DECLARATION_CREATES_CONSEQUENCE"),
            ("divergence_resolved", "DECLARATION_RESOLVES_DIVERGENCE"),
            ("evidence_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
            ("refusal_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
            ("blocked_attempt_erased", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
            ("projection_mismatch_hidden", "DECLARATION_ERASES_EVIDENCE_OR_REFUSAL"),
            ("public_launch_readiness_created", "DECLARATION_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "DECLARATION_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "DECLARATION_SCHEDULES_FOLLOW_ON_WORK"),
            ("self_orientation_successor_scheduled", "DECLARATION_SCHEDULES_FOLLOW_ON_WORK"),
        )
        for field, code in cases:
            with self.subTest(field=field):
                request = valid_request()
                request[field] = True
                result = resolve_request(request)
                self.assertBlockedWith(result, code)

    def test_mutation_replay_merge_blocks(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = valid_request()
                request[field] = True
                result = resolve_request(request)
                self.assertBlockedWith(result, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = valid_request()
        missing["declared_non_claims"].pop("operation_admitted")
        self.assertBlockedWith(resolve_request(missing), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = valid_request()
        flipped["declared_non_claims"]["permission_created"] = True
        self.assertBlockedWith(
            resolve_request(flipped),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "DECLARATION_CREATES_PERMISSION"},
        )


if __name__ == "__main__":
    unittest.main()
