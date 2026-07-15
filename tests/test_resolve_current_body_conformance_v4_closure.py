"""Bounded tests for current-body conformance v4 closure.

These tests audit one surface only: closure of meaning for a selected
conformant current-body conformance v4 result. Closure must not create current
self-orientation v10, authorize continuation or operation, synchronize
repositories, transfer the body, create a second body, create permission or
authority, create truth/action, claim final completion, create public readiness,
schedule follow-on work, mutate selected v4/v9/v8 surfaces, or erase the prior
not-conformant v4 lineage.
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

import resolve_current_body_conformance_v4_closure as resolver  # noqa: E402


CLOSED = "CURRENT_BODY_CONFORMANCE_V4_CLOSED"
NOT_CLOSED = "CURRENT_BODY_CONFORMANCE_V4_NOT_CLOSED"
BLOCKED = "CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BLOCKED"
CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_CONFORMANT"
NOT_CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_NOT_CONFORMANT"
V9_RECORDED = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
OUTCOME_FAMILY = {CLOSED, NOT_CLOSED, BLOCKED}

V4_ID = "current_body_conformance_v4_for_current_self_orientation_v9_001"
V9_ID = "current_self_orientation_v9_after_distributed_standing_boundary_conformance_closure_001"
REQUEST_ID = "current_body_conformance_v4_closure_001"

TOP_LEVEL_SECTIONS = {
    "current_body_conformance_v4_closure_metadata",
    "declared_closure_question",
    "selected_current_body_conformance_v4",
    "selected_v4_closure_basis",
    "v4_conformance_meaning",
    "v4_conformance_non_meaning",
    "lineage_preservation",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "current_body_conformance_v4_closure_summary",
}

V4_NON_MEANING_KEYS = {
    "v4_conformance_is_not_current_self_orientation_v10",
    "v4_conformance_is_not_continuation",
    "v4_conformance_is_not_operation",
    "v4_conformance_is_not_repository_synchronization",
    "v4_conformance_is_not_full_body_transfer",
    "v4_conformance_is_not_second_body_creation",
    "v4_conformance_is_not_final_completion",
    "v4_conformance_is_not_final_governance",
    "v4_conformance_is_not_final_continuity_completion",
    "v4_conformance_is_not_final_system_identity",
    "v4_conformance_is_not_public_launch_readiness",
    "v4_conformance_is_not_permission",
    "v4_conformance_is_not_authority",
    "v4_conformance_is_not_truth_action",
    "v4_conformance_is_not_follow_on_work_authorization",
}

CLOSURE_NON_MEANING_KEYS = {
    "not_current_self_orientation_v10",
    "not_continuation",
    "not_operation",
    "not_repository_synchronization",
    "not_full_body_transfer",
    "not_second_body",
    "not_distributed_standing_implementation",
    "not_distributed_operation",
    "not_final_completion",
    "not_final_governance",
    "not_final_continuity_completion",
    "not_final_system_identity",
    "not_public_launch_readiness",
    "not_permission",
    "not_authority",
    "not_truth",
    "not_action",
    "not_currentness",
    "not_carrier_currentness",
    "not_current_carrier_selected",
    "not_winning_carrier_selected",
    "not_losing_carrier_invalidated",
    "not_source_replacement",
    "not_divergence_resolution",
    "not_evidence_erasure",
    "not_refusal_erasure",
    "not_blocked_attempt_erasure",
    "not_projection_mismatch_erasure",
    "not_mutation_of_v9",
    "not_mutation_of_v8",
    "not_mutation_of_v4_conformance_artifact",
    "not_mutation_of_prior_not_conformant_v4_artifact",
    "not_erasure_of_prior_not_conformant_v4_lineage",
    "not_follow_on_work_authorization",
}

OPEN_KEYS = {
    "future_self_orientation_successor_beyond_v9",
    "current_self_orientation_v10_only_if_separately_declared_and_bounded",
    "distributed_standing_implementation",
    "distributed_operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body_creation",
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_implementation_beyond_boundary_recording",
    "truth_law",
    "action_consequence_law",
    "presence_law",
    "threshold_law",
    "body_relevance_medium",
    "signal_series_or_accumulation_logic",
    "public_launch_readiness",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}


def required_non_claims() -> dict[str, bool]:
    return {key: False for key in resolver.REQUIRED_NON_CLAIMS}


def selected_v9() -> dict:
    return {
        "current_self_orientation_v9_metadata": {
            "current_self_orientation_v9_result_id": V9_ID,
            "current_self_orientation_v9_result_type": "current_self_orientation_v9_result",
            "resolver_module": "resolve_current_self_orientation_v9",
        },
        "outcome": V9_RECORDED,
        "current_self_orientation_v9_summary": {
            "current_self_orientation_v9_result_id": V9_ID,
            "outcome": V9_RECORDED,
            "failed_check_count": 0,
        },
        "non_claims": {
            "permission_created": False,
            "continuation_authorized": False,
            "distributed_operation_authorized": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "truth_created": False,
            "action_authorized": False,
            "follow_on_work_authorized": False,
            "self_orientation_successor_scheduled": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
        },
    }


def v4_statement() -> dict:
    return {
        "current_body_conformance_v4_conformant": True,
        "selected_v9_preserved": True,
        "selected_v9_identity_preserved": True,
        "selected_v9_outcome_preserved": True,
        "selected_v9_is_current_self_orientation_v9": True,
        "selected_v9_recorded": True,
        "selected_v9_failed_check_count_zero": True,
        "v9_orientation_conformant": True,
        "basis_preservation_conformant": True,
        "non_claim_conformant": True,
        "conformance_did_not_mutate_v9": True,
        "conformance_did_not_authorize_continuation": True,
        "conformance_did_not_authorize_operation": True,
        "conformance_did_not_create_permission": True,
        "conformance_did_not_claim_final_completion": True,
        "conformance_did_not_schedule_follow_on_work": True,
        "conformance_did_not_create_v10": True,
        "conformance_did_not_create_closure": True,
    }


def selected_v4(
    *,
    outcome: str = CONFORMANT,
    failed_check_count: int = 0,
    statement_changes: dict | None = None,
    summary_changes: dict | None = None,
    include_v9: bool = True,
    include_identity: bool = True,
    include_outcome: bool = True,
) -> dict:
    statement = v4_statement()
    if statement_changes:
        statement.update(statement_changes)
    summary = {
        **statement,
        "outcome": outcome,
        "current_body_conformance_v4_result_id": V4_ID,
        "selected_v9_id": V9_ID,
        "selected_v9_outcome": V9_RECORDED,
        "passed_check_count": 42,
        "failed_check_count": failed_check_count,
    }
    if summary_changes:
        summary.update(summary_changes)
    result = {
        "current_body_conformance_v4_metadata": {
            "current_body_conformance_v4_result_id": V4_ID,
            "current_body_conformance_v4_result_type": "current_body_conformance_v4_result",
            "current_body_conformance_v4_result_version": "0.1.0",
            "resolver_module": "resolve_current_body_conformance_v4",
        },
        "conformance_statement": statement,
        "current_body_conformance_v4_summary": summary,
        "v9_orientation_conformance": {"v9_orientation_conformant": statement["v9_orientation_conformant"]},
        "basis_preservation_conformance": {
            "basis_preservation_conformant": statement["basis_preservation_conformant"]
        },
        "non_claim_conformance": {"non_claim_conformant": statement["non_claim_conformant"]},
        "conformance_checks": [
            {
                "check_name": "synthetic v4 conformance check",
                "passed": failed_check_count == 0,
                "expected_posture": True,
                "actual_posture": failed_check_count == 0,
                "failure_code": None if failed_check_count == 0 else "SYNTHETIC_FAILURE",
            }
        ],
    }
    if include_outcome:
        result["outcome"] = outcome
    if include_v9:
        result["selected_current_self_orientation_v9"] = selected_v9()
    if not include_identity:
        result["current_body_conformance_v4_metadata"].pop(
            "current_body_conformance_v4_result_id", None
        )
        result["current_body_conformance_v4_summary"].pop(
            "current_body_conformance_v4_result_id", None
        )
    if not include_outcome:
        result["current_body_conformance_v4_summary"].pop("outcome", None)
    return result


def prior_not_conformant_v4() -> dict:
    prior = selected_v4(outcome=NOT_CONFORMANT, failed_check_count=1)
    prior["conformance_statement"]["current_body_conformance_v4_conformant"] = False
    prior["conformance_statement"]["basis_preservation_conformant"] = False
    prior["current_body_conformance_v4_summary"]["current_body_conformance_v4_conformant"] = False
    prior["current_body_conformance_v4_summary"]["basis_preservation_conformant"] = False
    return prior


def closure_basis() -> dict:
    return {
        "selected_v4_closure_basis_id": "current_body_conformance_v4_closure_basis_001",
        "v8_remains_prior_lineage": True,
        "v9_remains_selected_orientation": True,
        "current_body_conformance_v3_closure_basis_preserved": True,
        "distributed_standing_boundary_conformance_closure_basis_preserved": True,
        "basis_is_not_permission": True,
        "basis_is_not_operation": True,
        "basis_is_not_continuation": True,
        "basis_is_not_final_completion": True,
    }


def valid_request(
    *,
    v4: dict | None = None,
    intent: str = "RECORD_CURRENT_BODY_CONFORMANCE_V4_CLOSURE",
    selected_current_body_conformance_v4_path: str | None = None,
    include_selected_id: bool = True,
    include_selected_outcome: bool = True,
) -> dict:
    selected = selected_v4() if v4 is None else v4
    request = resolver.build_declared_current_body_conformance_v4_closure_request(
        REQUEST_ID,
        "What does current-body conformance v4 mean and not mean?",
        copy.deepcopy(selected),
        closure_basis(),
        closure_intent=intent,
        selected_current_body_conformance_v4_path=selected_current_body_conformance_v4_path,
        selected_current_body_conformance_v4_id=V4_ID if include_selected_id else None,
        selected_current_body_conformance_v4_outcome=(
            CONFORMANT if include_selected_outcome else None
        ),
        expected_selected_v4_outcome=CONFORMANT,
        selected_current_self_orientation_v9=selected_v9(),
        prior_not_conformant_v4_result=prior_not_conformant_v4(),
    )
    request.update(
        {
            "selected_prior_self_orientation_v8": {"id": "current_self_orientation_v8_001"},
            "current_body_conformance_v3_closure_basis": {
                "id": "current_body_conformance_v3_closure_001"
            },
            "distributed_standing_boundary_conformance_closure_basis": {
                "id": "distributed_standing_boundary_conformance_closure_001"
            },
            "closure_scope": "current-body conformance v4 closure only",
        }
    )
    return request


def resolve_request(request: dict) -> dict:
    return resolver.resolve_current_body_conformance_v4_closure(
        declared_closure_request=request
    )


def failure_codes(result: dict) -> set[str]:
    codes = {
        check.get("failure_code")
        for check in result.get("closure_checks", [])
        if not check.get("passed") and check.get("failure_code")
    }
    block = result.get("block", {})
    if isinstance(block, dict) and block.get("block_code"):
        codes.add(block["block_code"])
    return codes


def with_statement_change(changes: dict) -> dict:
    v4 = selected_v4()
    v4["conformance_statement"].update(changes)
    v4["current_body_conformance_v4_summary"].update(changes)
    return v4


class CurrentBodyConformanceV4ClosureTests(unittest.TestCase):
    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertClosed(self, result: dict) -> None:
        self.assertEqual(CLOSED, result["outcome"])
        self.assertIsNone(result["block"].get("block_code"))
        self.assertIsNone(result["block"].get("block_reason"))
        self.assertEqual(
            0,
            result["current_body_conformance_v4_closure_summary"]["failed_check_count"],
        )
        self.assertTrue(result["closure_statement"]["current_body_conformance_v4_closed"])

    def assertCode(self, result: dict, code: str) -> None:
        self.assertIn(code, failure_codes(result))

    def assertResultNonClaimsFalse(self, result: dict) -> None:
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_v4_closure_from_mapping(self) -> None:
        result = resolve_request(valid_request())

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertOutcomeFamily(result)
        self.assertClosed(result)

        statement = result["closure_statement"]
        for key in (
            "selected_v4_preserved",
            "selected_v4_identity_preserved",
            "selected_v4_outcome_preserved",
            "selected_v4_is_current_body_conformance_v4",
            "selected_v4_conformant",
            "selected_v4_failed_check_count_zero",
            "selected_v9_preserved",
            "selected_v9_recorded",
            "v9_orientation_conformant",
            "basis_preservation_conformant",
            "non_claim_conformant",
            "v4_conformance_meaning_preserved",
            "v4_conformance_non_meaning_preserved",
            "lineage_preservation_passed",
            "closure_did_not_create_v10",
            "closure_did_not_authorize_continuation",
            "closure_did_not_authorize_operation",
            "closure_did_not_authorize_repository_sync",
            "closure_did_not_authorize_full_body_transfer",
            "closure_did_not_create_second_body",
            "closure_did_not_create_permission",
            "closure_did_not_claim_final_completion",
            "closure_did_not_create_public_readiness",
            "closure_did_not_schedule_follow_on_work",
            "closure_did_not_mutate_v4",
            "closure_did_not_mutate_v9",
            "closure_did_not_erase_prior_not_conformant_result",
        ):
            self.assertTrue(statement[key], key)

    def test_metadata_declared_question_and_selected_v4_sections(self) -> None:
        result = resolve_request(valid_request())
        metadata = result["current_body_conformance_v4_closure_metadata"]
        declared = result["declared_closure_question"]
        selected = result["selected_current_body_conformance_v4"]

        for key in (
            "current_body_conformance_v4_closure_result_id",
            "current_body_conformance_v4_closure_result_type",
            "current_body_conformance_v4_closure_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["current_body_conformance_v4_closure_result_version"])
        self.assertEqual("resolve_current_body_conformance_v4_closure", metadata["resolver_module"])

        self.assertEqual(REQUEST_ID, declared["closure_request_id"])
        self.assertIn("current-body conformance v4", declared["closure_question"])
        self.assertEqual("RECORD_CURRENT_BODY_CONFORMANCE_V4_CLOSURE", declared["closure_intent"])
        self.assertTrue(declared["closure_is_not_permission"])
        self.assertTrue(declared["closure_is_not_continuation"])
        self.assertTrue(declared["closure_is_not_operation"])
        self.assertTrue(declared["closure_is_not_final_completion"])
        self.assertTrue(declared["closure_is_not_current_self_orientation_v10"])
        self.assertTrue(declared["closure_does_not_mutate_what_it_closes"])

        self.assertEqual(V4_ID, selected["selected_current_body_conformance_v4_id"])
        self.assertEqual(CONFORMANT, selected["selected_current_body_conformance_v4_outcome"])
        self.assertIsNone(selected["selected_current_body_conformance_v4_path"])
        self.assertEqual(
            "current_body_conformance_v4_result",
            selected["selected_current_body_conformance_v4_result_type"],
        )
        self.assertTrue(selected["selected_v4_is_current_body_conformance_v4"])
        self.assertTrue(selected["selected_v4_conformant"])
        self.assertTrue(selected["selected_v4_failed_check_count_zero"])
        self.assertTrue(selected["selected_v4_not_mutated"])

    def test_meaning_non_meaning_lineage_and_open_sections(self) -> None:
        result = resolve_request(valid_request())
        meaning = result["v4_conformance_meaning"]
        lineage = result["lineage_preservation"]

        for key in (
            "selected_v9_preserved",
            "selected_v9_identity_preserved",
            "selected_v9_outcome_preserved",
            "selected_v9_is_current_self_orientation_v9",
            "selected_v9_recorded",
            "selected_v9_failed_check_count_zero",
            "v9_orientation_conformant",
            "basis_preservation_conformant",
            "non_claim_conformant",
            "conformance_did_not_mutate_v9",
            "conformance_did_not_authorize_continuation",
            "conformance_did_not_authorize_operation",
            "conformance_did_not_create_permission",
            "conformance_did_not_claim_final_completion",
            "conformance_did_not_schedule_follow_on_work",
            "v4_conformance_can_be_relied_on_as_conformance_not_permission",
            "v4_conformance_may_be_preserved_as_closed_meaning_only",
        ):
            self.assertTrue(meaning[key], key)
        self.assertEqual(V9_ID, meaning["selected_v9_id"])
        self.assertEqual(V9_RECORDED, meaning["selected_v9_outcome"])

        for key in V4_NON_MEANING_KEYS:
            self.assertTrue(result["v4_conformance_non_meaning"][key], key)

        for key in (
            "v8_remains_prior_lineage",
            "v9_remains_selected_orientation",
            "current_body_conformance_v3_closure_remains_basis",
            "distributed_standing_boundary_conformance_closure_remains_closed_meaning_basis",
            "prior_not_conformant_v4_result_remains_visible",
            "closure_does_not_erase_failed_or_not_conformant_attempts",
            "closure_does_not_hide_refusal_blocked_attempts_or_projection_mismatch",
            "closure_does_not_mutate_v4_v9_v8_or_prior_artifacts",
        ):
            self.assertTrue(lineage[key], key)
        self.assertEqual(
            NOT_CONFORMANT,
            lineage["prior_not_conformant_v4_result"]["outcome"],
        )

        for key in CLOSURE_NON_MEANING_KEYS:
            self.assertTrue(result["closure_non_meaning"][key], key)
        for key in OPEN_KEYS:
            self.assertIn(key, result["what_remains_open"])
        self.assertTrue(result["what_remains_open"]["open_means_not_scheduled"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])
        self.assertTrue(result["what_remains_open"]["open_means_not_executed"])

    def test_closure_checks_summary_and_non_claims(self) -> None:
        result = resolve_request(valid_request())

        for check in result["closure_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])

        check_names = {check["check_name"] for check in result["closure_checks"]}
        for expected in (
            "closure question declared",
            "closure intent supported",
            "selected v4 artifact present",
            "selected v4 artifact identity present",
            "selected v4 artifact outcome present",
            "selected v4 artifact readable or parseable",
            "selected v4 artifact is current-body conformance v4 result",
            "selected v4 outcome is conformant",
            "selected v4 failed check count is zero",
            "selected v9 preserved",
            "selected v9 recorded",
            "selected v9 failed check count zero",
            "v9 orientation conformant",
            "basis preservation conformant",
            "non-claim conformant",
            "conformance did not mutate v9",
            "conformance did not authorize continuation",
            "conformance did not authorize operation",
            "conformance did not create permission",
            "conformance did not claim final completion",
            "conformance did not schedule follow-on work",
            "v8 remains prior lineage where exposed",
            "v9 remains selected orientation",
            "current-body conformance v3 closure remains basis where exposed",
            "distributed standing boundary conformance closure remains closed meaning basis",
            "closure does not erase failed or not-conformant attempts",
            "closure does not create current self-orientation v10",
            "closure does not authorize continuation",
            "closure does not authorize operation",
            "closure does not authorize repository synchronization",
            "closure does not authorize full body transfer",
            "closure does not create second body",
            "closure does not create permission",
            "closure does not create authority",
            "closure does not create truth or action",
            "closure does not claim final completion",
            "closure does not create public readiness",
            "closure does not schedule follow-on work",
            "closure does not schedule self-orientation successor",
            "closure does not mutate v4",
            "closure does not mutate v9",
            "closure does not mutate v8",
            "closure does not erase prior not-conformant result",
            "no mutation replay or merge",
            "required non-claims remain false",
        ):
            self.assertIn(expected, check_names)

        summary = resolver.build_current_body_conformance_v4_closure_summary(result)
        for key in (
            "outcome",
            "block_code",
            "block_reason",
            "closure_request_id",
            "closure_question",
            "closure_intent",
            "selected_v4_id",
            "selected_v4_outcome",
            "selected_v9_id",
            "selected_v9_outcome",
            "passed_check_count",
            "failed_check_count",
            "current_body_conformance_v4_closed",
            "selected_v4_preserved",
            "selected_v4_identity_preserved",
            "selected_v4_outcome_preserved",
            "selected_v4_is_current_body_conformance_v4",
            "selected_v4_conformant",
            "selected_v4_failed_check_count_zero",
            "selected_v9_preserved",
            "selected_v9_recorded",
            "v9_orientation_conformant",
            "basis_preservation_conformant",
            "non_claim_conformant",
            "v4_conformance_meaning_preserved",
            "v4_conformance_non_meaning_preserved",
            "lineage_preservation_passed",
            "closure_did_not_create_v10",
            "closure_did_not_authorize_continuation",
            "closure_did_not_authorize_operation",
            "closure_did_not_authorize_repository_sync",
            "closure_did_not_authorize_full_body_transfer",
            "closure_did_not_create_second_body",
            "closure_did_not_create_permission",
            "closure_did_not_claim_final_completion",
            "closure_did_not_create_public_readiness",
            "closure_did_not_schedule_follow_on_work",
            "closure_did_not_mutate_v4",
            "closure_did_not_mutate_v9",
            "closure_did_not_erase_prior_not_conformant_result",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(CLOSED, summary["outcome"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["current_body_conformance_v4_closed"])
        self.assertResultNonClaimsFalse(result)

    def test_result_level_non_claims_for_closed_not_closed_and_blocked(self) -> None:
        closed = resolve_request(valid_request())
        not_closed = resolve_request(valid_request(v4=selected_v4(failed_check_count=1)))
        blocked = resolver.resolve_current_body_conformance_v4_closure()

        self.assertEqual(CLOSED, closed["outcome"])
        self.assertEqual(NOT_CLOSED, not_closed["outcome"])
        self.assertEqual(BLOCKED, blocked["outcome"])
        for result in (closed, not_closed, blocked):
            self.assertOutcomeFamily(result)
            self.assertResultNonClaimsFalse(result)

    def test_request_builder_helper(self) -> None:
        request = resolver.build_declared_current_body_conformance_v4_closure_request(
            "current_body_conformance_v4_closure_helper_001",
            "What does current-body conformance v4 mean and not mean?",
            selected_v4(),
            closure_basis(),
            selected_current_body_conformance_v4_path="/tmp/selected_v4.json",
            selected_current_body_conformance_v4_id=V4_ID,
            selected_current_body_conformance_v4_outcome=CONFORMANT,
            selected_current_self_orientation_v9=selected_v9(),
            prior_not_conformant_v4_result=prior_not_conformant_v4(),
        )

        self.assertEqual(
            "current_body_conformance_v4_closure_helper_001",
            request["closure_request_id"],
        )
        self.assertIn("current-body conformance v4", request["closure_question"])
        self.assertEqual(selected_v4(), request["selected_current_body_conformance_v4"])
        self.assertEqual(closure_basis(), request["selected_v4_closure_basis"])
        self.assertEqual("/tmp/selected_v4.json", request["selected_current_body_conformance_v4_path"])
        self.assertEqual(V4_ID, request["selected_current_body_conformance_v4_id"])
        self.assertEqual(CONFORMANT, request["selected_current_body_conformance_v4_outcome"])
        self.assertEqual(CONFORMANT, request["expected_selected_v4_outcome"])
        self.assertEqual(selected_v9(), request["selected_current_self_orientation_v9"])
        self.assertEqual(prior_not_conformant_v4(), request["prior_not_conformant_v4_result"])
        self.assertEqual(required_non_claims(), request["declared_non_claims"])

        request.update(valid_request())
        request["closure_request_id"] = "current_body_conformance_v4_closure_helper_001"
        request["selected_current_body_conformance_v4_path"] = None
        self.assertClosed(resolve_request(request))

    def test_path_based_selected_v4_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "selected_v4.json"
            path.write_text(json.dumps(selected_v4()), encoding="utf-8")
            request = valid_request(selected_current_body_conformance_v4_path=str(path))

            result = resolve_request(request)

            self.assertClosed(result)
            selected = result["selected_current_body_conformance_v4"]
            self.assertEqual(str(path), selected["selected_current_body_conformance_v4_path"])
            self.assertEqual(V4_ID, selected["selected_current_body_conformance_v4_id"])
            self.assertEqual(CONFORMANT, selected["selected_current_body_conformance_v4_outcome"])

    def test_path_based_closure_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "closure_request.json"
            path.write_text(json.dumps(valid_request()), encoding="utf-8")

            result = resolver.resolve_current_body_conformance_v4_closure_from_path(path)

            self.assertClosed(result)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
            self.assertEqual(str(path), result["declared_closure_question"]["declared_closure_request_path"])

    def test_write_behavior_and_default_output_path(self) -> None:
        result = resolve_request(valid_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "closure.json"
            written = resolver.write_current_body_conformance_v4_closure_result(result, explicit)
            self.assertEqual(explicit, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            with patch.object(
                resolver,
                "CURRENT_BODY_CONFORMANCE_V4_CLOSURE_ROOT",
                Path(tmp) / "current_body_conformance_v4_closure_root",
            ):
                first = resolver.write_current_body_conformance_v4_closure_result(result)
                second = resolver.write_current_body_conformance_v4_closure_result(result)
                self.assertEqual(
                    Path(tmp) / "current_body_conformance_v4_closure_root",
                    first.parent,
                )
                self.assertIn("current_body_conformance_v4_closure", str(first.parent))
                self.assertTrue(first.name.endswith("__current_body_conformance_v4_closure_result.json"))
                self.assertTrue(second.name.endswith("_001.json"))
                self.assertNotEqual(first, second)

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        request_before = copy.deepcopy(request)
        selected_v4_before = copy.deepcopy(request["selected_current_body_conformance_v4"])
        selected_v9_before = copy.deepcopy(request["selected_current_self_orientation_v9"])
        prior_before = copy.deepcopy(request["prior_not_conformant_v4_result"])

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(request_before, request)
        self.assertEqual(selected_v4_before, request["selected_current_body_conformance_v4"])
        self.assertEqual(selected_v9_before, request["selected_current_self_orientation_v9"])
        self.assertEqual(prior_before, request["prior_not_conformant_v4_result"])
        self.assertEqual(
            selected_v4_before,
            first["selected_current_body_conformance_v4"][
                "selected_current_body_conformance_v4_result"
            ],
        )
        self.assertEqual(
            selected_v4_before,
            second["selected_current_body_conformance_v4"][
                "selected_current_body_conformance_v4_result"
            ],
        )

        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_v4.json"
            selected_path.write_text(json.dumps(selected_v4_before, sort_keys=True), encoding="utf-8")
            before_text = selected_path.read_text(encoding="utf-8")
            resolver.write_current_body_conformance_v4_closure_result(
                first, Path(tmp) / "out" / "closure.json"
            )
            self.assertEqual(before_text, selected_path.read_text(encoding="utf-8"))

    def test_not_closed_readable_selected_v4(self) -> None:
        failed_v4 = selected_v4(failed_check_count=1)
        result = resolve_request(valid_request(v4=failed_v4))
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertGreater(
            result["current_body_conformance_v4_closure_summary"]["failed_check_count"],
            0,
        )
        self.assertCode(result, "CURRENT_BODY_CONFORMANCE_V4_HAS_FAILED_CHECKS")
        self.assertTrue(result["selected_current_body_conformance_v4"]["selected_v4_preserved"])
        self.assertEqual(failed_v4, valid_request(v4=failed_v4)["selected_current_body_conformance_v4"])

        continuation_v4 = with_statement_change(
            {
                "conformance_did_not_authorize_continuation": False,
                "conformance_authorized_continuation": True,
            }
        )
        result = resolve_request(valid_request(v4=continuation_v4))
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertCode(result, "CONFORMANCE_AUTHORIZED_CONTINUATION")

    def test_blocking_intent_missing_and_malformed_request(self) -> None:
        explicit = resolve_request(
            valid_request(intent="BLOCK_CURRENT_BODY_CONFORMANCE_V4_CLOSURE")
        )
        self.assertEqual(BLOCKED, explicit["outcome"])
        self.assertCode(explicit, "CLOSURE_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(explicit["closure_statement"]["current_body_conformance_v4_closed"])

        missing = resolver.resolve_current_body_conformance_v4_closure()
        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertCode(missing, "CLOSURE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_current_body_conformance_v4_closure(
            declared_closure_request=[]
        )
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertCode(malformed, "DECLARED_CLOSURE_REQUEST_MALFORMED")

    def test_path_unreadable_and_malformed_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_request = resolver.resolve_current_body_conformance_v4_closure_from_path(
                tmp_path / "missing_request.json"
            )
            self.assertEqual(BLOCKED, missing_request["outcome"])
            self.assertCode(missing_request, "DECLARED_CLOSURE_REQUEST_UNREADABLE")

            bad_request_path = tmp_path / "bad_request.json"
            bad_request_path.write_text("{bad json", encoding="utf-8")
            bad_request = resolver.resolve_current_body_conformance_v4_closure_from_path(
                bad_request_path
            )
            self.assertEqual(BLOCKED, bad_request["outcome"])
            self.assertCode(bad_request, "DECLARED_CLOSURE_REQUEST_UNREADABLE")

            array_request_path = tmp_path / "array_request.json"
            array_request_path.write_text("[]", encoding="utf-8")
            array_request = resolver.resolve_current_body_conformance_v4_closure_from_path(
                array_request_path
            )
            self.assertEqual(BLOCKED, array_request["outcome"])
            self.assertCode(array_request, "DECLARED_CLOSURE_REQUEST_MALFORMED")

            request = valid_request(
                selected_current_body_conformance_v4_path=str(tmp_path / "missing_v4.json")
            )
            selected_missing = resolve_request(request)
            self.assertEqual(BLOCKED, selected_missing["outcome"])
            self.assertCode(selected_missing, "CURRENT_BODY_CONFORMANCE_V4_UNREADABLE")

            bad_v4_path = tmp_path / "bad_v4.json"
            bad_v4_path.write_text("{bad json", encoding="utf-8")
            selected_bad = resolve_request(
                valid_request(selected_current_body_conformance_v4_path=str(bad_v4_path))
            )
            self.assertEqual(BLOCKED, selected_bad["outcome"])
            self.assertCode(selected_bad, "CURRENT_BODY_CONFORMANCE_V4_UNREADABLE")

            array_v4_path = tmp_path / "array_v4.json"
            array_v4_path.write_text("[]", encoding="utf-8")
            selected_array = resolve_request(
                valid_request(selected_current_body_conformance_v4_path=str(array_v4_path))
            )
            self.assertEqual(BLOCKED, selected_array["outcome"])
            self.assertCode(selected_array, "CURRENT_BODY_CONFORMANCE_V4_MALFORMED")

    def test_selected_v4_identity_outcome_and_failed_checks(self) -> None:
        missing_id = selected_v4(include_identity=False)
        result = resolve_request(
            valid_request(v4=missing_id, include_selected_id=False)
        )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertCode(result, "CURRENT_BODY_CONFORMANCE_V4_IDENTITY_MISSING")

        missing_outcome = selected_v4(include_outcome=False)
        result = resolve_request(
            valid_request(
                v4=missing_outcome,
                include_selected_outcome=False,
            )
        )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertCode(result, "CURRENT_BODY_CONFORMANCE_V4_OUTCOME_MISSING")

        not_conformant = selected_v4(outcome=NOT_CONFORMANT)
        result = resolve_request(valid_request(v4=not_conformant))
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertCode(result, "CURRENT_BODY_CONFORMANCE_V4_NOT_CONFORMANT")

        failed = selected_v4(failed_check_count=1)
        result = resolve_request(valid_request(v4=failed))
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertCode(result, "CURRENT_BODY_CONFORMANCE_V4_HAS_FAILED_CHECKS")

    def test_not_closed_selected_v9_and_conformance_meaning_issues(self) -> None:
        cases = [
            ("CURRENT_SELF_ORIENTATION_V9_MISSING", {"selected_v9_preserved": False}),
            ("CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED", {"selected_v9_recorded": False}),
            (
                "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS",
                {"selected_v9_failed_check_count_zero": False},
            ),
            (
                "V9_ORIENTATION_CONFORMANCE_MISSING_OR_FALSE",
                {"v9_orientation_conformant": False},
            ),
            (
                "BASIS_PRESERVATION_CONFORMANCE_MISSING_OR_FALSE",
                {"basis_preservation_conformant": False},
            ),
            ("NON_CLAIM_CONFORMANCE_MISSING_OR_FALSE", {"non_claim_conformant": False}),
        ]
        for code, changes in cases:
            with self.subTest(code=code):
                v4 = with_statement_change(changes)
                request = valid_request(v4=v4)
                if code == "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS":
                    request["selected_current_self_orientation_v9"][
                        "current_self_orientation_v9_summary"
                    ]["failed_check_count"] = 1
                result = resolve_request(request)
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertCode(result, code)

    def test_not_closed_v4_conformance_expansion(self) -> None:
        cases = [
            ("CONFORMANCE_MUTATED_V9", "conformance_did_not_mutate_v9"),
            (
                "CONFORMANCE_AUTHORIZED_CONTINUATION",
                "conformance_did_not_authorize_continuation",
            ),
            ("CONFORMANCE_AUTHORIZED_OPERATION", "conformance_did_not_authorize_operation"),
            ("CONFORMANCE_CREATED_PERMISSION", "conformance_did_not_create_permission"),
            (
                "CONFORMANCE_CLAIMED_FINAL_COMPLETION",
                "conformance_did_not_claim_final_completion",
            ),
            (
                "CONFORMANCE_SCHEDULED_FOLLOW_ON_WORK",
                "conformance_did_not_schedule_follow_on_work",
            ),
        ]
        for code, key in cases:
            with self.subTest(code=code):
                v4 = with_statement_change({key: False})
                result = resolve_request(valid_request(v4=v4))
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertCode(result, code)

    def test_closure_collapse_flags(self) -> None:
        cases = [
            ("CLOSURE_CREATES_CURRENT_SELF_ORIENTATION_V10", "current_self_orientation_v10_created"),
            ("CLOSURE_AUTHORIZES_CONTINUATION", "closure_authorized_continuation"),
            ("CLOSURE_AUTHORIZES_OPERATION", "closure_authorized_operation"),
            ("CLOSURE_AUTHORIZES_REPOSITORY_SYNC", "repository_synchronization_authorized"),
            ("CLOSURE_AUTHORIZES_FULL_BODY_TRANSFER", "full_body_transfer_authorized"),
            ("CLOSURE_CREATES_SECOND_BODY", "second_body_created"),
            ("CLOSURE_CREATES_PERMISSION", "permission_created"),
            ("CLOSURE_CREATES_AUTHORITY", "authority_created"),
            ("CLOSURE_CREATES_TRUTH_OR_ACTION", "truth_created"),
            ("CLOSURE_CLAIMS_FINAL_COMPLETION", "closure_claimed_final_completion"),
            ("CLOSURE_CREATES_PUBLIC_READINESS", "public_launch_readiness_created"),
            ("CLOSURE_SCHEDULES_FOLLOW_ON_WORK", "follow_on_work_authorized"),
            ("CLOSURE_MUTATES_V4", "closure_mutated_v4"),
            ("CLOSURE_MUTATES_V9", "closure_mutated_v9"),
            ("CLOSURE_MUTATES_V8", "closure_mutated_v8"),
            (
                "CLOSURE_ERASES_PRIOR_NOT_CONFORMANT_RESULT",
                "closure_erased_not_conformant_result",
            ),
        ]
        for code, key in cases:
            with self.subTest(code=code, key=key):
                request = valid_request()
                request["selected_v4_closure_basis"][key] = True
                result = resolve_request(request)
                self.assertEqual(BLOCKED, result["outcome"])
                self.assertCode(result, code)

    def test_mutation_replay_merge_flags(self) -> None:
        for key in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(key=key):
                request = valid_request()
                request["selected_v4_closure_basis"][key] = True
                result = resolve_request(request)
                self.assertEqual(BLOCKED, result["outcome"])
                self.assertCode(result, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped(self) -> None:
        missing = valid_request()
        del missing["declared_non_claims"]["currentness_created"]
        result = resolve_request(missing)
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertCode(result, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = valid_request()
        flipped["declared_non_claims"]["currentness_created"] = True
        result = resolve_request(flipped)
        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertCode(result, "NON_CLAIM_MISSING_OR_FLIPPED")


if __name__ == "__main__":
    unittest.main()
