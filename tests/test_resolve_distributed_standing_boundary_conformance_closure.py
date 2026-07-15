"""Bounded tests for distributed standing boundary conformance closure.

These tests audit one surface only: closure of meaning for a selected
distributed standing boundary conformance result. Closure must not re-run or
expand conformance, mutate the selected conformance result, mutate the selected
distributed standing boundary result, authorize continuation, synchronize
repositories, transfer the body, create a second body, authorize distributed
operation, create permission, create truth/action, claim final completion, or
schedule a self-orientation successor.
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

import resolve_distributed_standing_boundary_conformance_closure as resolver  # noqa: E402


CLOSED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED"
NOT_CLOSED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_NOT_CLOSED"
BLOCKED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE_BLOCKED"
CONFORMANT = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT"
OUTCOME_FAMILY = {CLOSED, NOT_CLOSED, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "distributed_standing_boundary_conformance_closure_metadata",
    "declared_closure_question",
    "selected_conformance_result",
    "selected_conformance_result_basis",
    "conformance_meaning",
    "conformance_non_meaning",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_standing_boundary_conformance_closure_summary",
}

RESULT_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "carrier_currentness_created",
    "source_replaced",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "divergence_resolved",
    "truth_created",
    "action_authorized",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "evidence_erased",
    "selected_conformance_result_mutated",
    "selected_distributed_standing_result_mutated",
    "closure_expanded_conformance",
    "closure_created_permission",
    "closure_authorized_operation",
    "closure_claimed_final_completion",
    "self_orientation_successor_scheduled",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
}

SELECTED_RESULT_FALSE_NON_CLAIMS = {
    *RESULT_NON_CLAIMS,
    "selected_result_mutated",
    "conformance_authorized_repository_sync",
    "conformance_authorized_full_body_transfer",
    "conformance_created_second_body",
    "conformance_authorized_continuation",
    "conformance_authorized_distributed_operation",
}

CONFORMANCE_NON_MEANING_KEYS = {
    "permission",
    "continuation",
    "operation",
    "distributed_operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body_creation",
    "second_body",
    "implementation",
    "final_completion",
    "final_governance",
    "final_continuity_completion",
    "self_orientation_successor_by_default",
    "closure_by_default",
}

CLOSURE_NON_MEANING_KEYS = {
    "distributed_operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body",
    "continuation",
    "implementation",
    "final_completion",
    "final_governance",
    "final_continuity_completion",
    "final_system_identity",
    "currentness",
    "carrier_currentness",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replacement",
    "authority",
    "permission",
    "truth",
    "action",
    "consequence_action_law",
    "divergence_resolution",
    "evidence_erasure",
    "refusal_erasure",
    "blocked_attempt_erasure",
    "projection_mismatch_erasure",
    "selected_conformance_result_mutation",
    "selected_distributed_standing_boundary_result_mutation",
    "implementation_readiness",
    "public_launch_readiness",
    "self_orientation_successor_by_default",
    "follow_on_work_authorization",
}

OPEN_KEYS = {
    "any_self_orientation_successor",
    "distributed_standing_implementation",
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
    "distributed_operation",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}


def selected_result_non_claims() -> dict:
    return {key: False for key in SELECTED_RESULT_FALSE_NON_CLAIMS}


def closure_non_claims() -> dict:
    return copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)


def conformant_selected_result() -> dict:
    statement = {
        "distributed_standing_boundary_conformant": True,
        "selected_result_preserved": True,
        "selected_result_identity_preserved": True,
        "selected_result_outcome_preserved": True,
        "selected_result_is_distributed_standing_boundary": True,
        "prerequisite_basis_conformant": True,
        "refusal_divergence_lineage_conformant": True,
        "non_claim_conformant": True,
        "summary_detail_correspondence_passed": True,
        "conformance_did_not_expand_result": True,
        "conformance_did_not_authorize_continuation": True,
        "conformance_did_not_authorize_repository_sync": True,
        "conformance_did_not_authorize_full_body_transfer": True,
        "conformance_did_not_create_second_body": True,
        "conformance_did_not_authorize_distributed_operation": True,
        "selected_result_mutated": False,
        "selected_distributed_standing_result_mutated": False,
        "permission_created": False,
        "continuation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "distributed_operation_authorized": False,
        "truth_created": False,
        "action_authorized": False,
    }
    summary = {
        **statement,
        "outcome": CONFORMANT,
        "conformance_request_id": "carrier_b_c_distributed_standing_boundary_conformance_001",
        "selected_distributed_standing_result_id": "carrier_b_c_distributed_standing_boundary_001",
        "selected_distributed_standing_result_outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
        "passed_check_count": 52,
        "failed_check_count": 0,
    }
    return {
        "distributed_standing_boundary_conformance_metadata": {
            "conformance_result_id": "carrier_b_c_distributed_standing_boundary_conformance_001",
            "conformance_result_type": "distributed_standing_boundary_conformance_result",
            "conformance_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_standing_boundary_conformance",
        },
        "declared_conformance_question": {
            "conformance_request_id": "carrier_b_c_distributed_standing_boundary_conformance_001",
            "conformance_question": "Does the recorded distributed standing boundary result conform to its declared basis and non-claims?",
            "conformance_intent": "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE",
        },
        "selected_distributed_standing_boundary_result": {
            "selected_result_id": "carrier_b_c_distributed_standing_boundary_001",
            "selected_result_outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
            "selected_result_preserved": True,
            "selected_result_identity_preserved": True,
            "selected_result_outcome_preserved": True,
            "selected_result_is_distributed_standing_boundary": True,
        },
        "selected_result_basis": {
            "selected_result_basis_declared": True,
            "basis": "Synthetic distributed standing boundary result basis.",
        },
        "prerequisite_basis_conformance": {
            "source_body_lineage_preserved": True,
            "selected_carrier_evidence_identities_preserved": True,
            "selected_carrier_evidence_outcomes_preserved": True,
            "carrier_b_successful_receipt_evidence_preserved": True,
            "carrier_c_blocked_receipt_evidence_preserved": True,
            "b_c_divergence_evidence_preserved": True,
            "divergence_consequence_basis_preserved": True,
            "currentness_successor_basis_preserved": True,
            "carrier_continuity_turn_v2_basis_preserved": True,
            "standing_propagation_v2_basis_preserved": True,
            "registry_persistence_v2_basis_preserved": True,
            "lifecycle_basis_preserved": True,
            "relation_conformance_closure_basis_preserved": True,
            "current_body_conformance_v3_closure_basis_preserved": True,
            "prerequisite_basis_conformant": True,
        },
        "refusal_divergence_lineage_conformance": {
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "blocked_attempts_preserved": True,
            "projection_mismatch_preserved": True,
            "detailed_basis_distinguished_from_summary": True,
            "summary_did_not_override_detailed_basis": True,
            "source_body_lineage_not_replaced": True,
            "carrier_b_success_did_not_erase_carrier_c_block": True,
            "carrier_c_block_did_not_invalidate_carrier_b_success": True,
            "b_c_divergence_caution_preserved": True,
            "refusal_divergence_lineage_conformant": True,
        },
        "non_claim_conformance": {
            "no_carrier_currentness": True,
            "no_current_carrier_selected": True,
            "no_winning_carrier_selected": True,
            "no_losing_carrier_invalidated": True,
            "no_source_replacement": True,
            "no_authority": True,
            "no_permission": True,
            "no_truth": True,
            "no_action": True,
            "no_divergence_resolution": True,
            "no_evidence_erasure": True,
            "no_repository_synchronization": True,
            "no_full_body_transfer": True,
            "no_second_body": True,
            "no_continuation": True,
            "no_distributed_operation": True,
            "no_mutation": True,
            "no_replay": True,
            "no_merge": True,
            "non_claim_conformant": True,
        },
        "summary_detail_correspondence": {
            "summary_detail_correspondence_passed": True,
            "summary_does_not_override_detailed_basis": True,
            "conformance_does_not_rely_on_summary_alone": True,
        },
        "conformance_checks": [
            {
                "check_name": "synthetic conformance check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "failure_code": None,
            }
        ],
        "conformance_statement": statement,
        "conformance_non_meaning": {
            "permission": True,
            "continuation": True,
            "operation": True,
            "distributed_operation": True,
            "repository_synchronization": True,
            "full_body_transfer": True,
            "second_body": True,
            "implementation": True,
            "final_completion": True,
            "self_orientation_successor_by_default": True,
            "closure_by_default": True,
        },
        "what_remains_open": {},
        "non_claims": selected_result_non_claims(),
        "outcome": CONFORMANT,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "distributed_standing_boundary_conformance_summary": summary,
    }


def declared_closure_request(
    selected: dict | None = None,
    *,
    intent: str = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE",
    selected_conformance_result_path: str | None = None,
    include_selected_result_id: bool = True,
    include_selected_result_outcome: bool = True,
) -> dict:
    selected_result = copy.deepcopy(selected if selected is not None else conformant_selected_result())
    request = resolver.build_declared_distributed_standing_boundary_conformance_closure_request(
        "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
        "What does distributed standing boundary conformance mean and not mean?",
        selected_result,
        {
            "basis": "Close meaning of the selected conformant result only.",
            "closure_does_not_authorize_continuation": True,
            "closure_does_not_authorize_operation": True,
            "closure_does_not_schedule_self_orientation_successor": True,
        },
        closure_intent=intent,
        selected_conformance_result_path=selected_conformance_result_path,
        selected_conformance_result_id=(
            "carrier_b_c_distributed_standing_boundary_conformance_001"
            if include_selected_result_id
            else None
        ),
        selected_conformance_result_outcome=CONFORMANT
        if include_selected_result_outcome
        else None,
    )
    if not include_selected_result_id:
        request.pop("selected_conformance_result_id", None)
    if not include_selected_result_outcome:
        request.pop("selected_conformance_result_outcome", None)
    return request


def resolve_request(request: dict) -> dict:
    return resolver.resolve_distributed_standing_boundary_conformance_closure(
        declared_closure_request=request
    )


def failed_codes(result: dict) -> set[str]:
    codes = {
        check.get("failure_code")
        for check in result["closure_checks"]
        if not check.get("passed") and check.get("failure_code")
    }
    block = result.get("block", {})
    for key in ("block_code", "first_failure_code"):
        if isinstance(block, dict) and block.get(key):
            codes.add(block[key])
    return codes


def set_statement_and_summary_flag(selected: dict, key: str, value: bool) -> dict:
    changed = copy.deepcopy(selected)
    changed["conformance_statement"][key] = value
    changed["distributed_standing_boundary_conformance_summary"][key] = value
    return changed


def set_meaning_flag(selected: dict, key: str, section_name: str, section_key: str, value: bool) -> dict:
    changed = set_statement_and_summary_flag(selected, key, value)
    changed[section_name][section_key] = value
    return changed


class DistributedStandingBoundaryConformanceClosureTests(unittest.TestCase):
    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertClosed(self, result: dict) -> None:
        self.assertEqual(CLOSED, result["outcome"])
        self.assertIsNone(result["block"].get("block_code"))
        self.assertIsNone(result["block"].get("block_reason"))
        self.assertEqual(
            0,
            result["distributed_standing_boundary_conformance_closure_summary"][
                "failed_check_count"
            ],
        )
        self.assertTrue(
            result["closure_statement"]["distributed_standing_boundary_conformance_closed"]
        )

    def assertResultNonClaimsFalse(self, result: dict) -> None:
        for key in RESULT_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_closed_result_from_mapping(self) -> None:
        result = resolve_request(declared_closure_request())

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertOutcomeFamily(result)
        self.assertClosed(result)

        statement = result["closure_statement"]
        self.assertTrue(statement["selected_conformance_result_preserved"])
        self.assertTrue(statement["selected_conformance_result_identity_preserved"])
        self.assertTrue(statement["selected_conformance_result_outcome_preserved"])
        self.assertTrue(statement["selected_conformance_result_is_conformance_result"])
        self.assertTrue(statement["selected_conformance_result_is_conformant"])
        self.assertTrue(statement["selected_conformance_result_failed_check_count_zero"])
        self.assertTrue(statement["conformance_meaning_preserved"])
        self.assertTrue(statement["conformance_non_meaning_preserved"])
        self.assertTrue(statement["closure_did_not_expand_conformance"])
        self.assertTrue(statement["closure_did_not_create_permission"])
        self.assertTrue(statement["closure_did_not_authorize_continuation"])
        self.assertTrue(statement["closure_did_not_authorize_operation"])
        self.assertTrue(statement["closure_did_not_authorize_repository_sync"])
        self.assertTrue(statement["closure_did_not_authorize_full_body_transfer"])
        self.assertTrue(statement["closure_did_not_create_second_body"])
        self.assertTrue(statement["closure_did_not_schedule_self_orientation_successor"])
        self.assertTrue(statement["closure_did_not_claim_final_completion"])

    def test_metadata_declared_question_and_selected_result_sections(self) -> None:
        result = resolve_request(declared_closure_request())
        metadata = result["distributed_standing_boundary_conformance_closure_metadata"]
        declared = result["declared_closure_question"]
        selected = result["selected_conformance_result"]

        for key in (
            "closure_result_id",
            "closure_result_type",
            "closure_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["closure_result_version"])
        self.assertEqual(
            "resolve_distributed_standing_boundary_conformance_closure",
            metadata["resolver_module"],
        )

        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            declared["closure_request_id"],
        )
        self.assertIn("What does distributed standing", declared["closure_question"])
        self.assertEqual(
            "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE",
            declared["closure_intent"],
        )
        self.assertTrue(declared["closure_is_not_continuation"])
        self.assertTrue(declared["closure_is_not_permission"])
        self.assertTrue(declared["closure_is_not_operation"])
        self.assertTrue(declared["closure_is_not_synchronization"])
        self.assertTrue(declared["closure_is_not_full_body_transfer"])
        self.assertTrue(declared["closure_is_not_second_body_creation"])
        self.assertTrue(declared["closure_is_not_implementation"])
        self.assertTrue(declared["closure_is_not_final_completion"])
        self.assertTrue(declared["closure_is_not_self_orientation_successor_by_default"])

        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_001",
            selected["selected_conformance_result_id"],
        )
        self.assertEqual(CONFORMANT, selected["selected_conformance_result_outcome"])
        self.assertIsNone(selected["selected_conformance_result_path"])
        self.assertTrue(selected["selected_conformance_result_is_conformance_result"])
        self.assertTrue(selected["selected_conformance_result_is_conformant"])
        self.assertTrue(selected["selected_conformance_result_failed_check_count_zero"])

    def test_conformance_meaning_and_non_meaning_sections(self) -> None:
        result = resolve_request(declared_closure_request())
        meaning = result["conformance_meaning"]

        for key in (
            "selected_distributed_standing_boundary_result_preserved",
            "selected_distributed_standing_boundary_result_identity_preserved",
            "selected_distributed_standing_boundary_result_outcome_preserved",
            "selected_distributed_standing_boundary_result_is_distributed_standing_boundary",
            "prerequisite_basis_conformant",
            "refusal_divergence_lineage_conformant",
            "non_claim_conformant",
            "summary_detail_correspondence_passed",
            "conformance_can_be_relied_on_as_conformance_not_permission",
            "conformance_may_be_preserved_as_closed_meaning_only",
            "conformance_meaning_preserved",
        ):
            self.assertTrue(meaning[key], key)

        for key in CONFORMANCE_NON_MEANING_KEYS:
            self.assertTrue(result["conformance_non_meaning"][key], key)

    def test_closure_checks_and_statement(self) -> None:
        result = resolve_request(declared_closure_request())
        checks = result["closure_checks"]

        for check in checks:
            self.assertTrue(
                {"check_name", "passed", "expected_posture", "actual_posture", "failure_code"}.issubset(check)
            )
            self.assertTrue(check["passed"], check)
            self.assertIsNone(check["failure_code"])

        names = {check["check_name"] for check in checks}
        expected_names = {
            "selected conformance result identity present",
            "selected conformance result outcome present",
            "selected conformance result readable and parseable",
            "selected conformance result is distributed standing boundary conformance result",
            "selected conformance result outcome is conformant",
            "selected conformance result failed check count is zero",
            "selected distributed standing boundary result preserved",
            "selected distributed standing boundary result identity preserved",
            "selected distributed standing boundary result outcome preserved",
            "selected distributed standing boundary result is distributed standing boundary",
            "prerequisite basis conformant",
            "refusal divergence lineage conformant",
            "non claim conformant",
            "summary detail correspondence passed",
            "conformance did not expand result",
            "conformance did not authorize continuation",
            "conformance did not authorize repository sync",
            "conformance did not authorize full body transfer",
            "conformance did not create second body",
            "conformance did not authorize distributed operation",
            "closure does not create new expansion",
            "closure does not mutate selected conformance result",
            "closure does not mutate selected distributed standing result",
            "closure does not create permission",
            "closure does not authorize continuation",
            "closure does not authorize operation",
            "closure does not authorize sync or full body transfer",
            "closure does not create second body",
            "closure does not create truth or action",
            "closure does not resolve divergence",
            "closure does not erase evidence",
            "closure does not claim final completion",
            "closure does not schedule self-orientation successor",
            "no mutation replay or merge",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_closure_non_meaning_and_open_items(self) -> None:
        result = resolve_request(declared_closure_request())

        for key in CLOSURE_NON_MEANING_KEYS:
            self.assertTrue(result["closure_non_meaning"][key], key)
        for key in OPEN_KEYS:
            self.assertTrue(result["what_remains_open"][key], key)

    def test_summary_helper_and_result_level_non_claims(self) -> None:
        result = resolve_request(declared_closure_request())
        summary = resolver.build_distributed_standing_boundary_conformance_closure_summary(result)

        self.assertEqual(CLOSED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            summary["closure_request_id"],
        )
        self.assertIn("What does distributed standing", summary["closure_question"])
        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_001",
            summary["selected_conformance_result_id"],
        )
        self.assertEqual(CONFORMANT, summary["selected_conformance_result_outcome"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        for key in (
            "distributed_standing_boundary_conformance_closed",
            "selected_conformance_result_preserved",
            "selected_conformance_result_identity_preserved",
            "selected_conformance_result_outcome_preserved",
            "selected_conformance_result_is_conformance_result",
            "selected_conformance_result_is_conformant",
            "selected_conformance_result_failed_check_count_zero",
            "conformance_meaning_preserved",
            "conformance_non_meaning_preserved",
            "closure_did_not_expand_conformance",
            "closure_did_not_create_permission",
            "closure_did_not_authorize_continuation",
            "closure_did_not_authorize_operation",
            "closure_did_not_authorize_repository_sync",
            "closure_did_not_authorize_full_body_transfer",
            "closure_did_not_create_second_body",
            "closure_did_not_schedule_self_orientation_successor",
            "closure_did_not_claim_final_completion",
        ):
            self.assertTrue(summary[key], key)
        self.assertIs(summary["key_non_claims"]["distributed_operation_authorized"], False)
        self.assertResultNonClaimsFalse(result)

    def test_result_non_claims_for_closed_not_closed_and_blocked(self) -> None:
        closed = resolve_request(declared_closure_request())
        not_closed = resolve_request(
            declared_closure_request(
                set_statement_and_summary_flag(
                    conformant_selected_result(),
                    "conformance_did_not_authorize_continuation",
                    False,
                )
            )
        )
        blocked = resolver.resolve_distributed_standing_boundary_conformance_closure()

        for result in (closed, not_closed, blocked):
            self.assertOutcomeFamily(result)
            self.assertResultNonClaimsFalse(result)

    def test_request_builder_helper_resolves_closed(self) -> None:
        selected = conformant_selected_result()
        request = resolver.build_declared_distributed_standing_boundary_conformance_closure_request(
            "builder_closure_001",
            "What does the selected conformant result mean?",
            selected,
            {"basis": "builder helper closure basis"},
            selected_conformance_result_path=None,
            selected_conformance_result_id="carrier_b_c_distributed_standing_boundary_conformance_001",
            selected_conformance_result_outcome=CONFORMANT,
        )

        self.assertEqual("builder_closure_001", request["closure_request_id"])
        self.assertEqual("What does the selected conformant result mean?", request["closure_question"])
        self.assertEqual(selected, request["selected_conformance_result"])
        self.assertEqual({"basis": "builder helper closure basis"}, request["selected_conformance_result_basis"])
        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_001",
            request["selected_conformance_result_id"],
        )
        self.assertEqual(CONFORMANT, request["selected_conformance_result_outcome"])
        self.assertEqual(CONFORMANT, request["expected_selected_conformance_result_outcome"])
        for key, value in closure_non_claims().items():
            self.assertIs(request["declared_non_claims"][key], value, key)

        self.assertClosed(resolve_request(request))

    def test_path_based_selected_conformance_result(self) -> None:
        selected = conformant_selected_result()
        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_conformance_result.json"
            selected_path.write_text(json.dumps(selected), encoding="utf-8")
            result = resolve_request(
                declared_closure_request(
                    selected,
                    selected_conformance_result_path=str(selected_path),
                )
            )

        self.assertClosed(result)
        selected_section = result["selected_conformance_result"]
        self.assertTrue(
            selected_section["selected_conformance_result_path"].endswith(
                "selected_conformance_result.json"
            )
        )
        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_001",
            selected_section["selected_conformance_result_id"],
        )
        self.assertEqual(CONFORMANT, selected_section["selected_conformance_result_outcome"])

    def test_path_based_closure_request(self) -> None:
        request = declared_closure_request()
        mapping_result = resolve_request(request)

        with tempfile.TemporaryDirectory() as tmp:
            request_path = Path(tmp) / "closure_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolver.resolve_distributed_standing_boundary_conformance_closure_from_path(
                request_path
            )

        self.assertClosed(path_result)
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertTrue(
            path_result["declared_closure_question"]["closure_request_path"].endswith(
                "closure_request.json"
            )
        )

    def test_write_behavior_and_default_output_non_overwrite(self) -> None:
        result = resolve_request(declared_closure_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "closure.json"
            written = resolver.write_distributed_standing_boundary_conformance_closure_result(
                result,
                explicit,
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            with patch.object(
                resolver,
                "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE_ROOT",
                Path(tmp) / "default",
            ):
                first = resolver.write_distributed_standing_boundary_conformance_closure_result(
                    result
                )
                second = resolver.write_distributed_standing_boundary_conformance_closure_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("conformance_closure_001", first.name)

    def test_non_mutation_posture(self) -> None:
        selected = conformant_selected_result()
        request = declared_closure_request(selected)
        selected_before = copy.deepcopy(selected)
        request_before = copy.deepcopy(request)

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(selected_before, selected)
        self.assertEqual(request_before, request)
        self.assertEqual(first["outcome"], second["outcome"])
        self.assertEqual(
            selected_before,
            first["selected_conformance_result"]["raw_selected_conformance_result"],
        )

    def test_not_closed_readable_result(self) -> None:
        selected = set_statement_and_summary_flag(
            conformant_selected_result(),
            "conformance_did_not_authorize_continuation",
            False,
        )
        result = resolve_request(declared_closure_request(selected))

        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertGreater(
            result["distributed_standing_boundary_conformance_closure_summary"][
                "failed_check_count"
            ],
            0,
        )
        self.assertIn("CONFORMANCE_AUTHORIZED_CONTINUATION", failed_codes(result))
        self.assertTrue(result["closure_statement"]["selected_conformance_result_preserved"])

    def test_do_not_record_intent_returns_bounded_not_closed(self) -> None:
        request = declared_closure_request(
            intent="DO_NOT_RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE"
        )
        result = resolve_request(request)

        self.assertEqual(NOT_CLOSED, result["outcome"])
        self.assertFalse(result["block"]["blocked"])
        self.assertIn("not_closed_reason", result["block"])
        self.assertFalse(
            result["closure_statement"]["distributed_standing_boundary_conformance_closed"]
        )

    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        explicit = resolve_request(
            declared_closure_request(
                intent="BLOCK_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE"
            )
        )
        missing = resolver.resolve_distributed_standing_boundary_conformance_closure()
        malformed = resolver.resolve_distributed_standing_boundary_conformance_closure(
            declared_closure_request=["not", "mapping"]
        )

        self.assertEqual(BLOCKED, explicit["outcome"])
        self.assertEqual("CLOSURE_REQUEST_EXPLICITLY_BLOCKED", explicit["block"]["block_code"])
        self.assertFalse(
            explicit["closure_statement"]["distributed_standing_boundary_conformance_closed"]
        )
        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertEqual("CLOSURE_QUESTION_UNDECLARED", missing["block"]["block_code"])
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertEqual("DECLARED_CLOSURE_REQUEST_MALFORMED", malformed["block"]["block_code"])

    def test_unsupported_intent_blocks(self) -> None:
        request = declared_closure_request()
        request["closure_intent"] = "AUTHORIZE_DISTRIBUTED_OPERATION"
        result = resolve_request(request)

        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual("CLOSURE_INTENT_UNSUPPORTED", result["block"]["block_code"])

    def test_closure_request_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = resolver.resolve_distributed_standing_boundary_conformance_closure_from_path(
                Path(tmp) / "missing.json"
            )

            malformed_path = Path(tmp) / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_distributed_standing_boundary_conformance_closure_from_path(
                malformed_path
            )

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_standing_boundary_conformance_closure_from_path(
                array_path
            )

        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertIn("DECLARED_CLOSURE_REQUEST_UNREADABLE", failed_codes(missing))
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertIn("DECLARED_CLOSURE_REQUEST_MALFORMED", failed_codes(malformed))
        self.assertEqual(BLOCKED, array_result["outcome"])
        self.assertIn("DECLARED_CLOSURE_REQUEST_MALFORMED", failed_codes(array_result))

    def test_selected_conformance_result_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_request = declared_closure_request(
                selected_conformance_result_path=str(Path(tmp) / "missing.json")
            )
            missing = resolve_request(missing_request)

            malformed_path = Path(tmp) / "selected_malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolve_request(
                declared_closure_request(
                    selected_conformance_result_path=str(malformed_path)
                )
            )

            array_path = Path(tmp) / "selected_array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_request(
                declared_closure_request(
                    selected_conformance_result_path=str(array_path)
                )
            )

        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertIn("SELECTED_CONFORMANCE_RESULT_UNREADABLE", failed_codes(missing))
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertIn("SELECTED_CONFORMANCE_RESULT_MALFORMED", failed_codes(malformed))
        self.assertEqual(BLOCKED, array_result["outcome"])
        self.assertIn("SELECTED_CONFORMANCE_RESULT_MALFORMED", failed_codes(array_result))

    def test_selected_result_identity_outcome_type_and_not_conformant(self) -> None:
        missing_identity = conformant_selected_result()
        missing_identity["distributed_standing_boundary_conformance_metadata"].pop(
            "conformance_result_id"
        )
        missing_identity["distributed_standing_boundary_conformance_summary"].pop(
            "conformance_request_id"
        )
        missing_identity["declared_conformance_question"].pop("conformance_request_id")
        missing_identity_result = resolve_request(
            declared_closure_request(
                missing_identity,
                include_selected_result_id=False,
            )
        )

        missing_outcome = conformant_selected_result()
        missing_outcome.pop("outcome")
        missing_outcome["distributed_standing_boundary_conformance_summary"].pop("outcome")
        missing_outcome_result = resolve_request(
            declared_closure_request(
                missing_outcome,
                include_selected_result_outcome=False,
            )
        )

        wrong_type = {
            "distributed_standing_boundary_conformance_metadata": {
                "conformance_result_id": "not_conformance_result",
                "conformance_result_type": "not_a_distributed_standing_boundary_conformance_result",
            },
            "outcome": CONFORMANT,
            "non_claims": selected_result_non_claims(),
        }
        wrong_type_result = resolve_request(declared_closure_request(wrong_type))

        not_conformant = conformant_selected_result()
        not_conformant["outcome"] = "DISTRIBUTED_STANDING_BOUNDARY_NOT_CONFORMANT"
        not_conformant["distributed_standing_boundary_conformance_summary"][
            "outcome"
        ] = "DISTRIBUTED_STANDING_BOUNDARY_NOT_CONFORMANT"
        not_conformant_result = resolve_request(
            declared_closure_request(
                not_conformant,
                include_selected_result_outcome=False,
            )
        )

        self.assertEqual(BLOCKED, missing_identity_result["outcome"])
        self.assertIn(
            "SELECTED_CONFORMANCE_RESULT_IDENTITY_MISSING",
            failed_codes(missing_identity_result),
        )
        self.assertEqual(BLOCKED, missing_outcome_result["outcome"])
        self.assertIn(
            "SELECTED_CONFORMANCE_RESULT_OUTCOME_MISSING",
            failed_codes(missing_outcome_result),
        )
        self.assertEqual(BLOCKED, wrong_type_result["outcome"])
        self.assertIn(
            "SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE",
            failed_codes(wrong_type_result),
        )
        self.assertEqual(NOT_CLOSED, not_conformant_result["outcome"])
        self.assertIn(
            "SELECTED_CONFORMANCE_RESULT_NOT_CONFORMANT",
            failed_codes(not_conformant_result),
        )

    def test_not_closed_failed_count_and_conformance_meaning_failures(self) -> None:
        failed_count = conformant_selected_result()
        failed_count["distributed_standing_boundary_conformance_summary"][
            "failed_check_count"
        ] = 1
        failed_count["conformance_checks"].append(
            {
                "check_name": "synthetic failed check",
                "passed": False,
                "expected_posture": True,
                "actual_posture": False,
                "failure_code": "SYNTHETIC_FAILURE",
            }
        )
        failed_count_result = resolve_request(declared_closure_request(failed_count))
        self.assertEqual(NOT_CLOSED, failed_count_result["outcome"])
        self.assertIn(
            "SELECTED_CONFORMANCE_RESULT_HAS_FAILED_CHECKS",
            failed_codes(failed_count_result),
        )

        cases = [
            (
                "prerequisite_basis_conformant",
                "prerequisite_basis_conformance",
                "prerequisite_basis_conformant",
                "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
            ),
            (
                "refusal_divergence_lineage_conformant",
                "refusal_divergence_lineage_conformance",
                "refusal_divergence_lineage_conformant",
                "REFUSAL_DIVERGENCE_LINEAGE_CONFORMANCE_MISSING_OR_FALSE",
            ),
            (
                "non_claim_conformant",
                "non_claim_conformance",
                "non_claim_conformant",
                "NON_CLAIM_CONFORMANCE_MISSING_OR_FALSE",
            ),
            (
                "summary_detail_correspondence_passed",
                "summary_detail_correspondence",
                "summary_detail_correspondence_passed",
                "SUMMARY_DETAIL_CORRESPONDENCE_MISSING_OR_FALSE",
            ),
        ]
        for key, section, section_key, code in cases:
            with self.subTest(key=key):
                selected = set_meaning_flag(
                    conformant_selected_result(),
                    key,
                    section,
                    section_key,
                    False,
                )
                result = resolve_request(declared_closure_request(selected))
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertIn(code, failed_codes(result))

    def test_not_closed_conformance_expansion_failures(self) -> None:
        cases = {
            "conformance_did_not_expand_result": "CONFORMANCE_EXPANDED_RESULT",
            "conformance_did_not_authorize_continuation": "CONFORMANCE_AUTHORIZED_CONTINUATION",
            "conformance_did_not_authorize_repository_sync": "CONFORMANCE_AUTHORIZED_REPOSITORY_SYNC",
            "conformance_did_not_authorize_full_body_transfer": "CONFORMANCE_AUTHORIZED_FULL_BODY_TRANSFER",
            "conformance_did_not_create_second_body": "CONFORMANCE_CREATED_SECOND_BODY",
            "conformance_did_not_authorize_distributed_operation": "CONFORMANCE_AUTHORIZED_DISTRIBUTED_OPERATION",
        }
        for flag, code in cases.items():
            with self.subTest(flag=flag):
                selected = set_statement_and_summary_flag(
                    conformant_selected_result(),
                    flag,
                    False,
                )
                result = resolve_request(declared_closure_request(selected))
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertIn(code, failed_codes(result))

    def test_not_closed_closure_collapse_flags(self) -> None:
        cases = {
            "closure_expanded_conformance": "CONFORMANCE_EXPANDED_RESULT",
            "closure_authorizes_continuation": "CLOSURE_AUTHORIZES_CONTINUATION",
            "closure_authorized_operation": "CLOSURE_AUTHORIZES_OPERATION",
            "repository_synchronization_authorized": "CLOSURE_AUTHORIZES_SYNC_OR_FULL_BODY_TRANSFER",
            "full_body_transfer_authorized": "CLOSURE_AUTHORIZES_SYNC_OR_FULL_BODY_TRANSFER",
            "second_body_created": "CLOSURE_CREATES_SECOND_BODY",
            "closure_mutates_selected_conformance_result": "CLOSURE_MUTATES_SELECTED_CONFORMANCE_RESULT",
            "closure_mutates_selected_distributed_standing_result": "CLOSURE_MUTATES_SELECTED_DISTRIBUTED_STANDING_RESULT",
            "truth_created": "CLOSURE_CREATES_TRUTH_OR_ACTION",
            "action_authorized": "CLOSURE_CREATES_TRUTH_OR_ACTION",
            "divergence_resolved": "CLOSURE_RESOLVES_DIVERGENCE",
            "evidence_erased": "CLOSURE_ERASES_EVIDENCE",
            "final_governance_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
            "final_continuity_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
            "final_system_identity_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
            "self_orientation_successor_scheduled": "CLOSURE_SCHEDULES_SELF_ORIENTATION_SUCCESSOR",
        }
        for flag, code in cases.items():
            with self.subTest(flag=flag):
                request = declared_closure_request()
                request[flag] = True
                result = resolve_request(request)
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertIn(code, failed_codes(result))

        permission_request = declared_closure_request()
        permission_request["closure_created_permission"] = True
        permission_result = resolve_request(permission_request)
        self.assertEqual(NOT_CLOSED, permission_result["outcome"])
        self.assertIn("CLOSURE_CREATES_PERMISSION", failed_codes(permission_result))

    def test_mutation_replay_merge_and_nonclaim_failures(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                selected = conformant_selected_result()
                selected["non_claims"][flag] = True
                result = resolve_request(declared_closure_request(selected))
                self.assertEqual(NOT_CLOSED, result["outcome"])
                self.assertIn("MUTATION_REPLAY_OR_MERGE_DETECTED", failed_codes(result))

        missing = declared_closure_request()
        missing["declared_non_claims"].pop("authority_created")
        missing_result = resolve_request(missing)

        flipped = declared_closure_request()
        flipped["declared_non_claims"]["truth_created"] = True
        flipped_result = resolve_request(flipped)

        self.assertEqual(NOT_CLOSED, missing_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(missing_result))
        self.assertEqual(NOT_CLOSED, flipped_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(flipped_result))

    def test_outcome_family_only_for_core_paths(self) -> None:
        closed = resolve_request(declared_closure_request())
        not_closed = resolve_request(
            declared_closure_request(
                set_statement_and_summary_flag(
                    conformant_selected_result(),
                    "conformance_did_not_expand_result",
                    False,
                )
            )
        )
        blocked = resolver.resolve_distributed_standing_boundary_conformance_closure()

        for result in (closed, not_closed, blocked):
            self.assertOutcomeFamily(result)


if __name__ == "__main__":
    unittest.main()
