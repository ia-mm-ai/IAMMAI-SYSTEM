"""Bounded tests for distributed standing boundary conformance.

These tests audit one surface only: conformance of a selected distributed
standing boundary result. Conformance verifies preserved basis, lineage,
summary/detail correspondence, and non-claims. It must not expand the selected
result, authorize continuation, synchronize repositories, transfer the body,
create a second body, authorize distributed operation, or close meaning.
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

import resolve_distributed_standing_boundary_conformance as resolver  # noqa: E402


CONFORMANT = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT"
NOT_CONFORMANT = "DISTRIBUTED_STANDING_BOUNDARY_NOT_CONFORMANT"
BLOCKED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_BLOCKED"

OUTCOME_FAMILY = {CONFORMANT, NOT_CONFORMANT, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "distributed_standing_boundary_conformance_metadata",
    "declared_conformance_question",
    "selected_distributed_standing_boundary_result",
    "selected_result_basis",
    "prerequisite_basis_conformance",
    "refusal_divergence_lineage_conformance",
    "non_claim_conformance",
    "summary_detail_correspondence",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_standing_boundary_conformance_summary",
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
    "summary_overrode_detailed_basis",
    "latest_file_standing",
    "latest_turn_standing",
    "majority_carrier_standing",
    "successful_receipt_count_standing",
    "registry_record_standing",
    "lifecycle_status_standing",
    "standing_propagation_standing",
    "continuity_turn_standing",
    "currentness_successor_standing",
    "divergence_consequence_standing",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
}

SELECTED_RESULT_FALSE_NON_CLAIMS = {
    *RESULT_NON_CLAIMS,
    "distributed_standing_authorized_sync",
    "distributed_standing_authorized_full_body_transfer",
    "distributed_standing_created_second_body",
    "distributed_standing_authorized_continuation",
    "distributed_standing_authorized_distributed_operation",
    "distributed_standing_erased_evidence",
}

CONFORMANCE_NON_MEANING_TRUE_KEYS = {
    "permission",
    "continuation",
    "distributed_operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body",
    "carrier_sovereignty",
    "currentness",
    "truth",
    "action",
    "divergence_resolution",
    "evidence_erasure",
    "implementation",
    "completion",
    "launch_publication_readiness",
    "final_governance",
    "final_continuity_completion",
    "self_orientation_successor_by_default",
    "closure_by_default",
}

OPEN_KEYS = {
    "distributed_standing_boundary_conformance_closure",
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


def conformant_selected_result() -> dict:
    statement = {
        "distributed_standing_posture_recorded": True,
        "body_side_standing_posture_preserved": True,
        "selected_carrier_evidence_preserved": True,
        "selected_carrier_evidence_identities_preserved": True,
        "selected_carrier_evidence_outcomes_preserved": True,
        "source_body_lineage_preserved": True,
        "receipt_refusal_admission_basis_preserved": True,
        "divergence_basis_preserved": True,
        "divergence_consequence_basis_preserved": True,
        "currentness_successor_basis_preserved": True,
        "carrier_continuity_turn_basis_preserved": True,
        "standing_propagation_basis_preserved": True,
        "registry_persistence_basis_preserved": True,
        "lifecycle_basis_preserved": True,
        "relation_conformance_closure_basis_preserved": True,
        "current_body_conformance_v3_closure_basis_preserved": True,
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "blocked_attempts_preserved": True,
        "projection_mismatch_preserved": True,
        "detailed_basis_distinguished_from_summary": True,
        "summary_overrode_detailed_basis": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_replaced": False,
        "authority_created": False,
        "permission_created": False,
        "truth_created": False,
        "action_authorized": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
    }
    summary = {
        **statement,
        "outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
        "distributed_standing_request_id": "carrier_b_c_distributed_standing_boundary_001",
        "passed_check_count": 47,
        "failed_check_count": 0,
        "selected_carrier_evidence_ids": [
            "carrier_b_successful_receipt_evidence_001",
            "carrier_c_blocked_receipt_evidence_001",
            "carrier_b_c_visible_divergence_001",
        ],
        "selected_carrier_evidence_outcomes": [
            "CARRIER_B_SUCCESSFUL_RECEIPT_EVIDENCE_PRESERVED",
            "CARRIER_C_BLOCKED_RECEIPT_EVIDENCE_PRESERVED",
            "CARRIER_DIVERGENCE_RECORDED",
        ],
    }
    return {
        "distributed_standing_metadata": {
            "distributed_standing_result_id": "carrier_b_c_distributed_standing_boundary_001",
            "distributed_standing_result_type": "distributed_standing_boundary_result",
            "distributed_standing_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_standing_boundary",
        },
        "declared_distributed_standing_question": {
            "distributed_standing_request_id": "carrier_b_c_distributed_standing_boundary_001",
            "distributed_standing_question": "What would it mean for the body to stand across carriers without source collapse?",
        },
        "selected_body_side_standing_posture": {
            "body_side_standing_posture_id": "current_body_standing_closure_post_conformance",
            "body_side_standing_posture_outcome": "CONFORMANCE_CLOSURE_RECORDED",
            "posture_remains_body_side": True,
        },
        "selected_carrier_evidence": {
            "raw_selected_carrier_evidence": [
                {
                    "evidence_id": "carrier_b_successful_receipt_evidence_001",
                    "carrier_id": "carrier_b",
                    "evidence_outcome": "CARRIER_B_SUCCESSFUL_RECEIPT_EVIDENCE_PRESERVED",
                    "description": "Carrier B successful received evidence remains evidence only.",
                },
                {
                    "evidence_id": "carrier_c_blocked_receipt_evidence_001",
                    "carrier_id": "carrier_c",
                    "evidence_outcome": "CARRIER_C_BLOCKED_RECEIPT_EVIDENCE_PRESERVED",
                    "description": "Carrier C blocked and refused receipt evidence remains visible.",
                },
                {
                    "evidence_id": "carrier_b_c_visible_divergence_001",
                    "carrier_id": "carrier_b_carrier_c",
                    "evidence_outcome": "CARRIER_DIVERGENCE_RECORDED",
                    "description": "B/C visible divergence evidence remains preserved.",
                },
            ]
        },
        "source_body_lineage": {
            "source_body_lineage_preserved": True,
            "source_not_replaced": True,
        },
        "receipt_refusal_admission_basis": {
            "carrier_b_receipt_preserved": True,
            "carrier_c_refusal_block_preserved": True,
            "carrier_c_returned_blocked_evidence_admitted_as_evidence_only": True,
        },
        "divergence_basis": {
            "b_c_visible_divergence_preserved": True,
            "divergence_resolved": False,
        },
        "divergence_consequence_basis": {
            "divergence_consequence_basis_preserved": True,
            "divergence_requires_caution": True,
            "caution": "B/C divergence caution is preserved as basis only.",
        },
        "currentness_successor_basis": {
            "currentness_successor_basis_preserved": True,
            "body_side_accounting_only": True,
            "carrier_currentness_created": False,
        },
        "carrier_continuity_turn_basis": {
            "carrier_continuity_turn_basis_preserved": True,
            "continuity_turn_v2_preserved": True,
            "projection_mismatch_preserved": True,
        },
        "standing_propagation_basis": {
            "standing_propagation_basis_preserved": True,
            "standing_propagation_v2_preserved": True,
        },
        "registry_persistence_basis": {
            "registry_persistence_basis_preserved": True,
            "registry_persistence_v2_preserved": True,
        },
        "lifecycle_basis": {
            "lifecycle_basis_preserved": True,
            "carrier_c_lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
        },
        "relation_conformance_closure_basis": {
            "relation_conformance_closure_basis_preserved": True,
            "closure_of_meaning_is_not_continuation": True,
        },
        "current_body_conformance_v3_closure_basis": {
            "current_body_conformance_v3_closure_basis_preserved": True,
            "v3_closure_preserved": True,
        },
        "distributed_standing_checks": [
            {
                "check_name": "synthetic distributed standing boundary check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
            }
        ],
        "distributed_standing_statement": statement,
        "distributed_standing_summary": summary,
        "non_claims": selected_result_non_claims(),
        "outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
        "block": {"blocked": False, "block_code": None, "block_reason": None},
    }


def declared_request(
    selected: dict | None = None,
    *,
    intent: str = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE",
    selected_result_path: str | None = None,
    include_selected_result_id: bool = True,
    include_selected_result_outcome: bool = True,
) -> dict:
    selected_result = copy.deepcopy(selected if selected is not None else conformant_selected_result())
    request = resolver.build_declared_distributed_standing_boundary_conformance_request(
        "distributed_standing_boundary_conformance_001",
        "Does the recorded distributed standing boundary result conform to its declared basis and non-claims?",
        selected_result,
        {
            "basis": "Review selected distributed standing boundary result without expansion.",
            "conformance_does_not_authorize_continuation": True,
            "conformance_does_not_authorize_operation": True,
        },
        conformance_intent=intent,
        selected_result_path=selected_result_path,
        selected_result_id=(
            "carrier_b_c_distributed_standing_boundary_001"
            if include_selected_result_id
            else None
        ),
        selected_result_outcome=(
            "DISTRIBUTED_STANDING_POSTURE_RECORDED"
            if include_selected_result_outcome
            else None
        ),
    )
    if not include_selected_result_id:
        request.pop("selected_result_id", None)
    if not include_selected_result_outcome:
        request.pop("selected_result_outcome", None)
    return request


def resolve_request(request: dict) -> dict:
    return resolver.resolve_distributed_standing_boundary_conformance(
        declared_conformance_request=request
    )


def failed_codes(result: dict) -> set[str]:
    codes = {
        check.get("failure_code")
        for check in result["conformance_checks"]
        if not check.get("passed") and check.get("failure_code")
    }
    block_code = result.get("block", {}).get("block_code")
    if block_code:
        codes.add(block_code)
    return codes


def set_flag(selected: dict, key: str, value: bool) -> dict:
    changed = copy.deepcopy(selected)
    for section in (
        changed.get("distributed_standing_statement", {}),
        changed.get("distributed_standing_summary", {}),
        changed.get("non_claims", {}),
    ):
        if isinstance(section, dict):
            section[key] = value
    return changed


class DistributedStandingBoundaryConformanceTests(unittest.TestCase):
    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertConformant(self, result: dict) -> None:
        self.assertEqual(CONFORMANT, result["outcome"])
        self.assertIsNone(result["block"].get("block_code"))
        self.assertIsNone(result["block"].get("block_reason"))
        self.assertEqual(
            0,
            result["distributed_standing_boundary_conformance_summary"][
                "failed_check_count"
            ],
        )
        self.assertTrue(result["conformance_statement"]["distributed_standing_boundary_conformant"])

    def test_successful_conformant_result_from_mapping(self) -> None:
        result = resolve_request(declared_request())

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertOutcomeFamily(result)
        self.assertConformant(result)

        statement = result["conformance_statement"]
        self.assertTrue(statement["selected_result_preserved"])
        self.assertTrue(statement["selected_result_identity_preserved"])
        self.assertTrue(statement["selected_result_outcome_preserved"])
        self.assertTrue(statement["selected_result_is_distributed_standing_boundary"])
        self.assertTrue(statement["prerequisite_basis_conformant"])
        self.assertTrue(statement["refusal_divergence_lineage_conformant"])
        self.assertTrue(statement["non_claim_conformant"])
        self.assertTrue(statement["summary_detail_correspondence_passed"])
        self.assertTrue(statement["conformance_did_not_expand_result"])
        self.assertTrue(statement["conformance_did_not_authorize_continuation"])
        self.assertTrue(statement["conformance_did_not_authorize_repository_sync"])
        self.assertTrue(statement["conformance_did_not_authorize_full_body_transfer"])
        self.assertTrue(statement["conformance_did_not_create_second_body"])
        self.assertTrue(statement["conformance_did_not_authorize_distributed_operation"])

    def test_metadata_and_declared_question_preserve_boundary(self) -> None:
        result = resolve_request(declared_request())
        metadata = result["distributed_standing_boundary_conformance_metadata"]
        declared = result["declared_conformance_question"]
        selected = result["selected_distributed_standing_boundary_result"]

        for key in (
            "conformance_result_id",
            "conformance_result_type",
            "conformance_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["conformance_result_version"])
        self.assertEqual(
            "resolve_distributed_standing_boundary_conformance",
            metadata["resolver_module"],
        )

        self.assertEqual("distributed_standing_boundary_conformance_001", declared["conformance_request_id"])
        self.assertIn("Does the recorded", declared["conformance_question"])
        self.assertEqual("RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE", declared["conformance_intent"])
        self.assertEqual("carrier_b_c_distributed_standing_boundary_001", selected["selected_result_id"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", selected["selected_result_outcome"])
        self.assertTrue(declared["conformance_is_not_permission"])
        self.assertTrue(declared["conformance_is_not_continuation"])
        self.assertTrue(declared["conformance_is_not_distributed_operation"])
        self.assertTrue(declared["conformance_is_not_synchronization"])
        self.assertTrue(declared["conformance_is_not_full_body_transfer"])
        self.assertTrue(result["conformance_non_meaning"]["closure_by_default"])

    def test_selected_result_identity_and_prerequisite_sections(self) -> None:
        original = conformant_selected_result()
        original_copy = copy.deepcopy(original)
        result = resolve_request(declared_request(original))

        selected = result["selected_distributed_standing_boundary_result"]
        self.assertEqual("carrier_b_c_distributed_standing_boundary_001", selected["selected_result_id"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", selected["selected_result_outcome"])
        self.assertTrue(selected["selected_result_is_distributed_standing_boundary"])
        self.assertEqual(
            "distributed_standing_boundary_result",
            selected["raw_selected_distributed_standing_boundary_result"][
                "distributed_standing_metadata"
            ]["distributed_standing_result_type"],
        )
        self.assertEqual(original_copy, original)

        prerequisite = result["prerequisite_basis_conformance"]
        for key in (
            "source_body_lineage_preserved",
            "selected_carrier_evidence_identities_preserved",
            "selected_carrier_evidence_outcomes_preserved",
            "carrier_b_successful_receipt_evidence_preserved",
            "carrier_c_blocked_receipt_evidence_preserved",
            "b_c_divergence_evidence_preserved",
            "divergence_consequence_basis_preserved",
            "currentness_successor_basis_preserved",
            "carrier_continuity_turn_v2_basis_preserved",
            "standing_propagation_v2_basis_preserved",
            "registry_persistence_v2_basis_preserved",
            "lifecycle_basis_preserved",
            "relation_conformance_closure_basis_preserved",
            "current_body_conformance_v3_closure_basis_preserved",
        ):
            self.assertTrue(prerequisite[key], key)
        self.assertTrue(prerequisite["prerequisite_basis_conformant"])

    def test_refusal_divergence_lineage_and_non_claim_conformance(self) -> None:
        result = resolve_request(declared_request())
        lineage = result["refusal_divergence_lineage_conformance"]
        for key in (
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "blocked_attempts_preserved",
            "projection_mismatch_preserved",
            "detailed_basis_distinguished_from_summary",
            "summary_did_not_override_detailed_basis",
            "source_body_lineage_not_replaced",
            "carrier_b_success_did_not_erase_carrier_c_block",
            "carrier_c_block_did_not_invalidate_carrier_b_success",
            "b_c_divergence_caution_preserved",
            "refusal_divergence_lineage_conformant",
        ):
            self.assertTrue(lineage[key], key)

        non_claim = result["non_claim_conformance"]
        for key in (
            "no_carrier_currentness",
            "no_current_carrier_selected",
            "no_winning_carrier_selected",
            "no_losing_carrier_invalidated",
            "no_source_replacement",
            "no_authority",
            "no_permission",
            "no_truth",
            "no_action",
            "no_divergence_resolution",
            "no_evidence_erasure",
            "no_repository_synchronization",
            "no_full_body_transfer",
            "no_second_body",
            "no_continuation",
            "no_distributed_operation",
            "no_latest_file_standing",
            "no_latest_turn_standing",
            "no_majority_standing",
            "no_success_count_standing",
            "no_registry_standing_by_itself",
            "no_lifecycle_standing_by_itself",
            "no_standing_propagation_standing_by_itself",
            "no_continuity_turn_standing_by_itself",
            "no_currentness_successor_standing_by_itself",
            "no_divergence_consequence_standing_by_itself",
            "no_mutation",
            "no_replay",
            "no_merge",
            "non_claim_conformant",
        ):
            self.assertTrue(non_claim[key], key)

    def test_summary_detail_correspondence(self) -> None:
        result = resolve_request(declared_request())
        correspondence = result["summary_detail_correspondence"]

        self.assertTrue(correspondence["selected_result_summary_present"])
        self.assertTrue(correspondence["selected_result_detail_body_present"])
        self.assertTrue(correspondence["summary_corresponds_to_detailed_body_where_exposed"])
        self.assertTrue(correspondence["summary_does_not_override_detailed_basis"])
        self.assertTrue(correspondence["checks_statement_and_non_claims_consistent_where_exposed"])
        self.assertTrue(correspondence["conformance_does_not_rely_on_summary_alone"])
        self.assertTrue(correspondence["detailed_body_used_where_summary_incomplete_or_compressed"])
        self.assertTrue(correspondence["summary_detail_correspondence_passed"])

    def test_conformance_checks_have_required_shape_and_meaning(self) -> None:
        result = resolve_request(declared_request())
        checks = result["conformance_checks"]

        for check in checks:
            self.assertTrue({"check_name", "passed", "expected_posture", "actual_posture", "failure_code"}.issubset(check))
            self.assertTrue(check["passed"], check)
            self.assertIsNone(check["failure_code"])

        names = {check["check_name"] for check in checks}
        expected_names = {
            "selected artifact identity present",
            "selected artifact outcome present",
            "selected artifact readable and parseable",
            "selected artifact is distributed standing boundary result",
            "source body lineage preserved",
            "carrier b successful receipt evidence preserved",
            "carrier c blocked receipt evidence preserved",
            "b c divergence evidence preserved",
            "divergence consequence basis preserved",
            "currentness successor basis preserved",
            "continuity turn v2 basis preserved",
            "standing propagation v2 basis preserved",
            "registry persistence v2 basis preserved",
            "lifecycle basis preserved",
            "relation conformance closure basis preserved",
            "current body conformance v3 closure basis preserved",
            "visible refusal preserved",
            "visible divergence preserved",
            "blocked attempts preserved",
            "projection mismatch preserved",
            "detailed basis distinguished from summary",
            "summary did not override detailed basis",
            "source body lineage not replaced",
            "no carrier currentness",
            "no current carrier selected",
            "no winning carrier selected",
            "no losing carrier invalidated",
            "no source replacement",
            "no authority",
            "no permission",
            "no truth",
            "no action",
            "no divergence resolution",
            "no evidence erasure",
            "no repository synchronization",
            "no full body transfer",
            "no second body",
            "no continuation",
            "no distributed operation",
            "no latest file or latest turn standing",
            "no majority or success count standing",
            "no prerequisite created standing by itself",
            "no mutation replay or merge",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_non_meaning_open_items_and_result_non_claims(self) -> None:
        result = resolve_request(declared_request())

        for key in CONFORMANCE_NON_MEANING_TRUE_KEYS:
            self.assertTrue(result["conformance_non_meaning"][key], key)
        for key in OPEN_KEYS:
            self.assertTrue(result["what_remains_open"][key], key)
        for key in RESULT_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

    def test_summary_helper_preserves_compact_fields(self) -> None:
        result = resolve_request(declared_request())
        summary = resolver.build_distributed_standing_boundary_conformance_summary(result)

        self.assertEqual(CONFORMANT, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("distributed_standing_boundary_conformance_001", summary["conformance_request_id"])
        self.assertIn("Does the recorded", summary["conformance_question"])
        self.assertEqual("carrier_b_c_distributed_standing_boundary_001", summary["selected_distributed_standing_result_id"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", summary["selected_distributed_standing_result_outcome"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        for key in (
            "distributed_standing_boundary_conformant",
            "selected_result_preserved",
            "selected_result_identity_preserved",
            "selected_result_outcome_preserved",
            "selected_result_is_distributed_standing_boundary",
            "prerequisite_basis_conformant",
            "refusal_divergence_lineage_conformant",
            "non_claim_conformant",
            "summary_detail_correspondence_passed",
            "conformance_did_not_expand_result",
            "conformance_did_not_authorize_continuation",
            "conformance_did_not_authorize_repository_sync",
            "conformance_did_not_authorize_full_body_transfer",
            "conformance_did_not_create_second_body",
            "conformance_did_not_authorize_distributed_operation",
        ):
            self.assertTrue(summary[key], key)
        self.assertIs(summary["key_non_claims"]["distributed_operation_authorized"], False)

    def test_request_builder_helper_resolves_conformant(self) -> None:
        selected = conformant_selected_result()
        request = resolver.build_declared_distributed_standing_boundary_conformance_request(
            "builder_conformance_001",
            "Does the selected distributed standing boundary result conform?",
            selected,
            {"basis": "builder helper conformance basis"},
            selected_result_path=None,
            selected_result_id="carrier_b_c_distributed_standing_boundary_001",
            selected_result_outcome="DISTRIBUTED_STANDING_POSTURE_RECORDED",
        )

        self.assertEqual("builder_conformance_001", request["conformance_request_id"])
        self.assertEqual("Does the selected distributed standing boundary result conform?", request["conformance_question"])
        self.assertEqual(selected, request["selected_distributed_standing_boundary_result"])
        self.assertEqual({"basis": "builder helper conformance basis"}, request["selected_result_basis"])
        self.assertEqual("carrier_b_c_distributed_standing_boundary_001", request["selected_result_id"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", request["selected_result_outcome"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", request["expected_selected_result_outcome"])
        for key in RESULT_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        self.assertConformant(resolve_request(request))

    def test_path_based_selected_result(self) -> None:
        selected = conformant_selected_result()
        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_result.json"
            selected_path.write_text(json.dumps(selected), encoding="utf-8")
            request = declared_request(selected, selected_result_path=str(selected_path))
            result = resolve_request(request)

        self.assertConformant(result)
        self.assertTrue(result["selected_distributed_standing_boundary_result"]["selected_result_path"].endswith("selected_result.json"))
        self.assertEqual("carrier_b_c_distributed_standing_boundary_001", result["selected_distributed_standing_boundary_result"]["selected_result_id"])
        self.assertEqual("DISTRIBUTED_STANDING_POSTURE_RECORDED", result["selected_distributed_standing_boundary_result"]["selected_result_outcome"])

    def test_path_based_conformance_request(self) -> None:
        request = declared_request()
        mapping_result = resolve_request(request)

        with tempfile.TemporaryDirectory() as tmp:
            request_path = Path(tmp) / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolver.resolve_distributed_standing_boundary_conformance_from_path(request_path)

        self.assertConformant(path_result)
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertTrue(path_result["declared_conformance_question"]["conformance_request_path"].endswith("request.json"))

    def test_write_behavior_and_default_output_non_overwrite(self) -> None:
        result = resolve_request(declared_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "conformance.json"
            written = resolver.write_distributed_standing_boundary_conformance_result(result, explicit)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            with patch.object(resolver, "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_ROOT", Path(tmp) / "default"):
                first = resolver.write_distributed_standing_boundary_conformance_result(result)
                second = resolver.write_distributed_standing_boundary_conformance_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("distributed_standing_boundary_conformance_001", first.name)

    def test_non_mutation_posture(self) -> None:
        selected = conformant_selected_result()
        request = declared_request(selected)
        selected_before = copy.deepcopy(selected)
        request_before = copy.deepcopy(request)

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(selected_before, selected)
        self.assertEqual(request_before, request)
        self.assertEqual(first["outcome"], second["outcome"])
        self.assertEqual(first["selected_distributed_standing_boundary_result"]["raw_selected_distributed_standing_boundary_result"], selected_before)

    def test_not_conformant_readable_result(self) -> None:
        selected = set_flag(conformant_selected_result(), "visible_divergence_preserved", False)
        result = resolve_request(declared_request(selected))

        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertGreater(result["distributed_standing_boundary_conformance_summary"]["failed_check_count"], 0)
        self.assertIn("VISIBLE_DIVERGENCE_NOT_PRESERVED", failed_codes(result))
        self.assertTrue(result["conformance_statement"]["selected_result_preserved"])

    def test_do_not_record_intent_returns_bounded_not_conformant(self) -> None:
        request = declared_request(intent="DO_NOT_RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE")
        result = resolve_request(request)

        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertFalse(result["block"]["blocked"])
        self.assertIn("not_recorded_reason", result["block"])
        self.assertFalse(result["conformance_statement"]["distributed_standing_boundary_conformant"])

    def test_explicit_block_intent_blocks(self) -> None:
        result = resolve_request(
            declared_request(intent="BLOCK_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE")
        )

        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual("CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED", result["block"]["block_code"])
        self.assertFalse(result["conformance_statement"]["distributed_standing_boundary_conformant"])

    def test_missing_and_malformed_requests_block(self) -> None:
        missing = resolver.resolve_distributed_standing_boundary_conformance()
        malformed = resolver.resolve_distributed_standing_boundary_conformance(
            declared_conformance_request=["not", "mapping"]
        )

        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertEqual("CONFORMANCE_QUESTION_UNDECLARED", missing["block"]["block_code"])
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertEqual("DECLARED_CONFORMANCE_REQUEST_MALFORMED", malformed["block"]["block_code"])

    def test_unsupported_intent_blocks(self) -> None:
        request = declared_request()
        request["conformance_intent"] = "EXPAND_DISTRIBUTED_STANDING"
        result = resolve_request(request)

        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual("CONFORMANCE_INTENT_UNSUPPORTED", result["block"]["block_code"])

    def test_conformance_request_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = resolver.resolve_distributed_standing_boundary_conformance_from_path(
                Path(tmp) / "missing.json"
            )
            malformed_path = Path(tmp) / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolver.resolve_distributed_standing_boundary_conformance_from_path(
                malformed_path
            )
            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_distributed_standing_boundary_conformance_from_path(
                array_path
            )

        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertIn("DECLARED_CONFORMANCE_REQUEST_UNREADABLE", failed_codes(missing))
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertIn("DECLARED_CONFORMANCE_REQUEST_MALFORMED", failed_codes(malformed))
        self.assertEqual(BLOCKED, array_result["outcome"])
        self.assertIn("DECLARED_CONFORMANCE_REQUEST_MALFORMED", failed_codes(array_result))

    def test_selected_result_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_request = declared_request(selected_result_path=str(Path(tmp) / "missing.json"))
            missing = resolve_request(missing_request)

            malformed_path = Path(tmp) / "selected_malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolve_request(declared_request(selected_result_path=str(malformed_path)))

            array_path = Path(tmp) / "selected_array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_request(declared_request(selected_result_path=str(array_path)))

        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertIn("SELECTED_DISTRIBUTED_STANDING_RESULT_UNREADABLE", failed_codes(missing))
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertIn("SELECTED_DISTRIBUTED_STANDING_RESULT_MALFORMED", failed_codes(malformed))
        self.assertEqual(BLOCKED, array_result["outcome"])
        self.assertIn("SELECTED_DISTRIBUTED_STANDING_RESULT_MALFORMED", failed_codes(array_result))

    def test_selected_result_identity_outcome_and_type_blocks(self) -> None:
        missing_identity = conformant_selected_result()
        missing_identity["distributed_standing_metadata"].pop("distributed_standing_result_id")
        missing_identity["distributed_standing_summary"].pop("distributed_standing_request_id")
        missing_identity["declared_distributed_standing_question"].pop("distributed_standing_request_id")
        missing_identity_result = resolve_request(
            declared_request(missing_identity, include_selected_result_id=False)
        )

        missing_outcome = conformant_selected_result()
        missing_outcome.pop("outcome")
        missing_outcome["distributed_standing_summary"].pop("outcome")
        missing_outcome_result = resolve_request(
            declared_request(missing_outcome, include_selected_result_outcome=False)
        )

        wrong_type = {
            "distributed_standing_metadata": {
                "distributed_standing_result_id": "not_boundary_result",
                "distributed_standing_result_type": "not_a_distributed_standing_boundary_result",
            },
            "outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
            "non_claims": selected_result_non_claims(),
        }
        wrong_type_result = resolve_request(declared_request(wrong_type))

        self.assertEqual(BLOCKED, missing_identity_result["outcome"])
        self.assertIn("SELECTED_RESULT_IDENTITY_MISSING", failed_codes(missing_identity_result))
        self.assertEqual(BLOCKED, missing_outcome_result["outcome"])
        self.assertIn("SELECTED_RESULT_OUTCOME_MISSING", failed_codes(missing_outcome_result))
        self.assertEqual(BLOCKED, wrong_type_result["outcome"])
        self.assertIn("SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY", failed_codes(wrong_type_result))

    def test_not_conformant_when_prerequisite_basis_missing(self) -> None:
        selected = conformant_selected_result()
        selected.pop("divergence_consequence_basis")
        selected["distributed_standing_statement"]["divergence_consequence_basis_preserved"] = False
        selected["distributed_standing_summary"]["divergence_consequence_basis_preserved"] = False

        result = resolve_request(declared_request(selected))

        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertIn("PREREQUISITE_BASIS_MISSING", failed_codes(result))

    def test_not_conformant_refusal_divergence_projection_issues(self) -> None:
        cases = {
            "visible_refusal_preserved": "VISIBLE_REFUSAL_NOT_PRESERVED",
            "visible_divergence_preserved": "VISIBLE_DIVERGENCE_NOT_PRESERVED",
            "blocked_attempts_preserved": "BLOCKED_ATTEMPT_NOT_PRESERVED",
            "projection_mismatch_preserved": "PROJECTION_MISMATCH_NOT_PRESERVED",
            "detailed_basis_distinguished_from_summary": "SUMMARY_OVERWRITES_DETAILED_BASIS",
        }
        for flag, code in cases.items():
            with self.subTest(flag=flag):
                selected = set_flag(conformant_selected_result(), flag, False)
                if flag == "projection_mismatch_preserved":
                    selected["carrier_continuity_turn_basis"]["projection_mismatch_preserved"] = False
                result = resolve_request(declared_request(selected))
                self.assertEqual(NOT_CONFORMANT, result["outcome"])
                self.assertIn(code, failed_codes(result))

        summary_override = set_flag(conformant_selected_result(), "summary_overrode_detailed_basis", True)
        result = resolve_request(declared_request(summary_override))
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertIn("SUMMARY_OVERWRITES_DETAILED_BASIS", failed_codes(result))

    def test_not_conformant_collapse_flags(self) -> None:
        cases = {
            "carrier_currentness_created": "CARRIER_CURRENTNESS_CREATED",
            "current_carrier_selected": "CURRENT_CARRIER_SELECTED",
            "winning_carrier_selected": "WINNING_CARRIER_SELECTED",
            "losing_carrier_invalidated": "LOSING_CARRIER_INVALIDATED",
            "source_replaced": "SOURCE_REPLACED",
            "authority_created": "AUTHORITY_CREATED",
            "permission_created": "PERMISSION_CREATED",
            "truth_created": "TRUTH_CREATED",
            "action_authorized": "ACTION_AUTHORIZED",
            "divergence_resolved": "DIVERGENCE_RESOLVED",
            "evidence_erased": "EVIDENCE_ERASED",
            "repository_synchronization_authorized": "REPOSITORY_SYNC_AUTHORIZED",
            "full_body_transfer_authorized": "FULL_BODY_TRANSFER_AUTHORIZED",
            "second_body_created": "SECOND_BODY_CREATED",
            "continuation_authorized": "CONTINUATION_AUTHORIZED",
            "distributed_operation_authorized": "DISTRIBUTED_OPERATION_AUTHORIZED",
            "latest_file_standing": "LATEST_OR_MAJORITY_STANDING_CREATED",
            "latest_turn_standing": "LATEST_OR_MAJORITY_STANDING_CREATED",
            "majority_carrier_standing": "LATEST_OR_MAJORITY_STANDING_CREATED",
            "successful_receipt_count_standing": "LATEST_OR_MAJORITY_STANDING_CREATED",
            "registry_record_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "lifecycle_status_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "standing_propagation_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "continuity_turn_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "currentness_successor_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "divergence_consequence_standing": "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
            "mutation_performed": "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "replay_performed": "MUTATION_REPLAY_OR_MERGE_DETECTED",
            "merge_performed": "MUTATION_REPLAY_OR_MERGE_DETECTED",
        }
        for flag, code in cases.items():
            with self.subTest(flag=flag):
                result = resolve_request(declared_request(set_flag(conformant_selected_result(), flag, True)))
                self.assertEqual(NOT_CONFORMANT, result["outcome"])
                self.assertIn(code, failed_codes(result))

    def test_required_request_non_claim_missing_or_flipped(self) -> None:
        missing = declared_request()
        missing["declared_non_claims"].pop("authority_created")
        missing_result = resolve_request(missing)

        flipped = declared_request()
        flipped["declared_non_claims"]["truth_created"] = True
        flipped_result = resolve_request(flipped)

        self.assertEqual(NOT_CONFORMANT, missing_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(missing_result))
        self.assertEqual(NOT_CONFORMANT, flipped_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(flipped_result))

    def test_outcome_family_only_for_core_paths(self) -> None:
        conformant = resolve_request(declared_request())
        not_conformant = resolve_request(
            declared_request(set_flag(conformant_selected_result(), "visible_refusal_preserved", False))
        )
        blocked = resolver.resolve_distributed_standing_boundary_conformance()

        for result in (conformant, not_conformant, blocked):
            self.assertOutcomeFamily(result)


if __name__ == "__main__":
    unittest.main()
