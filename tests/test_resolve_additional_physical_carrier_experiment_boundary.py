"""Tests for bounded additional physical carrier experiment declaration.

This suite audits one declaration resolver. It verifies that an additional
physical carrier experiment may be declared only as one bounded receipt/refusal
experiment over one selected carried surface or packet. The declaration does
not execute the experiment, create a packet, create receipt evidence, admit
returned evidence, create currentness, create distributed standing, authorize
repository synchronization, authorize full body transfer, authorize body
functions on the receiving carrier, authorize distributed operation, authorize
continuation, or authorize expansion by success.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_additional_physical_carrier_experiment_boundary as resolver


TOP_LEVEL_SECTIONS = {
    "additional_physical_carrier_experiment_metadata",
    "declared_experiment_question",
    "experiment_scope",
    "source_carrier",
    "receiving_carrier",
    "selected_carried_surface_or_packet",
    "permitted_operations",
    "prohibited_operations",
    "return_and_admission_posture",
    "experiment_checks",
    "experiment_declaration_statement",
    "experiment_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "additional_physical_carrier_experiment_summary",
}

OUTCOME_FAMILY = {
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED",
    "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED",
}

EXPECTED_CHECK_NAMES = {
    "declared_experiment_request_parseable_mapping",
    "experiment_question_declared",
    "experiment_purpose_declared",
    "experiment_intent_supported",
    "source_carrier_declared",
    "receiving_carrier_declared",
    "receiving_carrier_is_additional_and_bounded",
    "carrier_roles_supported",
    "selected_surface_or_packet_declared",
    "selected_surface_or_packet_parseable",
    "selected_surface_or_packet_identity_exists",
    "selected_surface_or_packet_basis_preserved",
    "scope_single_carrier",
    "scope_single_surface_or_packet",
    "permitted_operations_receipt_refusal_only",
    "prohibited_operations_explicit",
    "return_required_for_body_visibility",
    "admission_not_created_by_return",
    "no_self_orientation_on_receiving_carrier",
    "no_conformance_on_receiving_carrier",
    "no_relation_conformance_or_closure_on_receiving_carrier",
    "no_repository_synchronization",
    "no_full_body_transfer",
    "no_carrier_registry",
    "no_currentness",
    "no_distributed_standing",
    "no_distributed_operation",
    "no_continuation",
    "no_carrier_hierarchy",
    "no_source_replacement",
    "no_authority_or_permission_beyond_declared_experiment",
    "no_success_based_expansion",
    "no_majority_success_count_or_latest_file_currentness",
    "no_hidden_refusal_or_divergence",
    "no_mutation_replay_or_merge",
    "non_claims_remain_false",
}

EXPERIMENT_NON_MEANING_KEYS = {
    "does_not_mean_distributed_standing",
    "does_not_mean_currentness",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission_beyond_declared_experiment",
    "does_not_mean_standing_permission_for_more_carriers",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_carrier_priority",
    "does_not_mean_carrier_sovereignty",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_carrier_registry",
    "does_not_mean_persistence",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
    "does_not_mean_automatic_admission",
    "does_not_mean_automatic_relation",
    "does_not_mean_automatic_currentness",
    "does_not_mean_automatic_conformance",
    "does_not_mean_automatic_closure",
    "does_not_mean_distributed_operation",
    "does_not_mean_success_means_expansion",
}

OPEN_KEYS = {
    "physical_execution_of_additional_carrier_receipt_refusal",
    "admission_of_any_returned_evidence",
    "divergence_review_involving_additional_carrier_evidence",
    "currentness_participation_review_involving_additional_carrier_evidence",
    "multi_carrier_relation_involving_additional_carrier_evidence",
    "conformance_over_any_later_relation",
    "closure_over_any_later_conformance",
    "distributed_standing",
    "persistence_registry_law",
    "presence_law",
    "threshold_law",
    "truth_law",
    "action_consequence_law",
    "generalized_vessel_relation_lifecycle",
    "body_relevance_medium",
    "signal_series_or_accumulation_logic",
    "successor_carrier_law",
    "future_self_orientation_successor_only_if_separately_justified",
    "distributed_operation_only_if_separately_declared_and_bounded",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}

FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

REQUEST_ID = "additional_physical_carrier_experiment_request_001"
SOURCE_CARRIER_ID = "carrier_A_current_macbook"
RECEIVING_CARRIER_ID = "carrier_C_additional_physical_candidate"
SURFACE_ID = "current_body_standing_closure_post_conformance_packet_001"


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert isinstance(loaded, dict)
    return loaded


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _selected_surface_or_packet(**updates: object) -> dict[str, object]:
    surface = {
        "selected_surface_or_packet_id": SURFACE_ID,
        "selected_surface_or_packet_basis": {
            "basis_id": "current_body_conformance_v3_closure_basis_001",
            "basis_outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
            "basis_posture": "closed_meaning_only",
        },
        "outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        "integrity_basis": {
            "hash_algorithm": "sha256",
            "hash_value": "synthetic-preserved-integrity-value",
            "hash_basis_preserved": True,
        },
    }
    surface.update(updates)
    return surface


def valid_request(**updates: object) -> dict[str, object]:
    request = resolver.build_declared_additional_physical_carrier_experiment_request(
        experiment_request_id=REQUEST_ID,
        experiment_question=(
            "May one additional physical carrier receive one selected carried packet?"
        ),
        experiment_purpose=(
            "Declare one bounded receipt/refusal experiment without execution."
        ),
        source_carrier_id=SOURCE_CARRIER_ID,
        receiving_carrier_id=RECEIVING_CARRIER_ID,
        selected_surface_or_packet=_selected_surface_or_packet(),
    )
    request.update(
        {
            "selected_prior_closure_basis": {
                "basis_id": "current_body_conformance_v3_closure_result_001",
                "basis_outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
            },
            "selected_v3_closure_basis": {
                "closure_result_id": "current_body_conformance_v3_closure_result_001",
                "closure_outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
            },
            "selected_relation_band_basis": {
                "relation_result_id": "multi_carrier_relation_result_001",
                "relation_conformance_id": "multi_carrier_relation_conformance_001",
                "relation_closure_id": "multi_carrier_relation_conformance_closure_001",
            },
            "operator_note": "synthetic bounded declaration request",
        }
    )
    request.update(updates)
    return request


def resolve(request: object) -> dict[str, object]:
    return resolver.resolve_additional_physical_carrier_experiment_boundary(
        declared_experiment_request=request
    )


class AdditionalPhysicalCarrierExperimentBoundaryTests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict[str, object]) -> None:
        self.assertEqual(set(result), TOP_LEVEL_SECTIONS)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_block_code(self, request: object, expected_code: str) -> dict[str, object]:
        result = resolve(request)
        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED",
        )
        self.assertEqual(result["block"]["block_code"], expected_code)
        self.assert_all_result_non_claims_false(result)
        return result

    def assert_all_result_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def declared_result(self) -> dict[str, object]:
        result = resolve(valid_request())
        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
        )
        return result

    def test_successful_experiment_declaration_shape_and_core_statement(self) -> None:
        result = self.declared_result()

        self.assert_top_level_shape(result)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["additional_physical_carrier_experiment_summary"]["failed_check_count"], 0)

        statement = result["experiment_declaration_statement"]
        self.assertIs(statement["additional_physical_carrier_experiment_declared"], True)
        self.assertIs(statement["experiment_scope_single_carrier"], True)
        self.assertIs(statement["experiment_scope_single_surface_or_packet"], True)
        self.assertIs(statement["permitted_operation_receipt_or_block_only"], True)
        self.assertIs(statement["return_required_for_body_visibility"], True)
        self.assertIs(statement["admission_not_created_by_return"], True)
        self.assertIs(statement["experiment_executes_physical_receipt"], False)
        self.assertIs(statement["experiment_creates_packet_file"], False)
        self.assertIs(statement["experiment_creates_returned_evidence"], False)
        self.assertIs(statement["experiment_admits_returned_evidence"], False)

    def test_metadata(self) -> None:
        metadata = self.declared_result()["additional_physical_carrier_experiment_metadata"]

        self.assertTrue(metadata["additional_physical_carrier_experiment_result_id"])
        self.assertTrue(metadata["additional_physical_carrier_experiment_result_type"])
        self.assertEqual(metadata["additional_physical_carrier_experiment_result_version"], "0.1.0")
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_additional_physical_carrier_experiment_boundary",
        )

    def test_declared_experiment_question_preserves_basis_and_non_execution(self) -> None:
        question = self.declared_result()["declared_experiment_question"]

        self.assertEqual(question["experiment_request_id"], REQUEST_ID)
        self.assertEqual(
            question["experiment_intent"],
            "DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT",
        )
        self.assertIn("one additional physical carrier", question["experiment_question"])
        self.assertIn("receipt/refusal", question["experiment_purpose"])
        self.assertEqual(
            question["selected_prior_closure_basis"]["basis_outcome"],
            "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        )
        self.assertEqual(
            question["selected_v3_closure_basis"]["closure_outcome"],
            "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        )
        self.assertTrue(question["selected_relation_band_basis"]["relation_result_id"])
        self.assertEqual(question["declared_non_claims"], _non_claims())
        self.assertIs(question["declaration_executes_physical_experiment"], False)
        self.assertIs(question["declaration_creates_packet_file"], False)
        self.assertIs(question["declaration_authorizes_repository_synchronization"], False)
        self.assertIs(question["declaration_authorizes_full_body_transfer"], False)
        self.assertIs(question["declaration_authorizes_distributed_operation"], False)
        self.assertIs(question["declaration_authorizes_continuation"], False)

    def test_experiment_scope(self) -> None:
        scope = self.declared_result()["experiment_scope"]

        self.assertIs(scope["single_carrier_scope"], True)
        self.assertIs(scope["single_surface_or_packet_scope"], True)
        self.assertEqual(scope["receiving_carrier_count"], 1)
        self.assertEqual(scope["selected_surface_or_packet_count"], 1)
        self.assertIs(scope["scope_does_not_create_distributed_standing"], True)
        self.assertIs(scope["scope_does_not_authorize_continuation"], True)
        self.assertIs(scope["scope_does_not_authorize_expansion_by_success"], True)

    def test_source_and_receiving_carrier_posture(self) -> None:
        result = self.declared_result()
        source = result["source_carrier"]
        receiving = result["receiving_carrier"]

        self.assertEqual(source["source_carrier_id"], SOURCE_CARRIER_ID)
        self.assertEqual(source["source_carrier_role"], "EXPERIMENT_SOURCE_CARRIER")
        self.assertIs(source["source_carrier_role_supported"], True)
        self.assertIs(source["source_role_is_operation_local"], True)
        self.assertIs(source["source_carrier_does_not_create_universal_source_authority"], True)

        self.assertEqual(receiving["receiving_carrier_id"], RECEIVING_CARRIER_ID)
        self.assertEqual(receiving["receiving_carrier_role"], "EXPERIMENT_RECEIVING_CARRIER")
        self.assertIs(receiving["receiving_carrier_role_supported"], True)
        self.assertIs(receiving["receiving_carrier_role_is_operation_local"], True)
        self.assertIs(receiving["receiving_carrier_bounded_to_receipt_refusal"], True)
        self.assertIs(
            receiving["receiving_carrier_does_not_become_source_current_authority_body_or_standing"],
            True,
        )

    def test_selected_surface_packet_permitted_prohibited_and_return_posture(self) -> None:
        result = self.declared_result()
        selected = result["selected_carried_surface_or_packet"]
        permitted = result["permitted_operations"]
        prohibited = result["prohibited_operations"]
        return_posture = result["return_and_admission_posture"]

        self.assertIs(selected["selected_surface_or_packet_declared"], True)
        self.assertIs(selected["selected_surface_or_packet_parseable"], True)
        self.assertEqual(selected["selected_surface_or_packet_id"], SURFACE_ID)
        self.assertEqual(
            selected["selected_surface_or_packet_basis"]["basis_outcome"],
            "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        )
        self.assertIs(selected["selected_surface_or_packet_basis_preserved"], True)
        self.assertEqual(
            selected["selected_surface_or_packet_outcome_or_status"],
            "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        )
        self.assertEqual(selected["integrity_basis"]["hash_algorithm"], "sha256")
        self.assertIs(selected["integrity_basis_preserved_where_supplied"], True)

        self.assertIs(permitted["permitted_operations_declared"], True)
        self.assertIs(permitted["receipt_or_block_only"], True)
        self.assertEqual(permitted["unsupported_operation_tokens"], [])
        self.assertLessEqual(
            set(permitted["operation_tokens"]),
            resolver.PERMITTED_OPERATION_TOKENS,
        )

        raw_prohibited = prohibited["raw_prohibited_operations"]
        self.assertIs(prohibited["prohibited_operations_explicit"], True)
        for key in (
            "repository_synchronization",
            "full_body_transfer",
            "self_orientation_on_receiving_carrier",
            "conformance_on_receiving_carrier",
            "relation_conformance_or_closure_on_receiving_carrier",
            "carrier_registry",
            "currentness",
            "distributed_standing",
            "distributed_operation",
            "continuation",
            "success_based_expansion",
        ):
            self.assertIs(raw_prohibited[key], True)

        self.assertIs(return_posture["return_posture_declared"], True)
        self.assertIs(return_posture["return_required_for_body_visibility"], True)
        self.assertIs(return_posture["admission_not_created_by_return"], True)
        self.assertIs(return_posture["admission_must_be_separate"], True)
        self.assertIs(return_posture["later_divergence_review_must_be_separate"], True)
        self.assertIs(return_posture["later_currentness_review_must_be_separate"], True)
        self.assertIs(return_posture["later_relation_review_must_be_separate"], True)

    def test_experiment_checks(self) -> None:
        checks = self.declared_result()["experiment_checks"]

        self.assertTrue(checks)
        self.assertEqual({check["check_name"] for check in checks}, EXPECTED_CHECK_NAMES)
        for check in checks:
            self.assertEqual(
                set(check),
                {"check_name", "passed", "expected_posture", "actual_posture", "block_code"},
            )
            self.assertIs(check["passed"], True)
            self.assertIsNone(check["block_code"])

    def test_declaration_statement_non_meaning_open_and_non_claims(self) -> None:
        result = self.declared_result()
        statement = result["experiment_declaration_statement"]

        for key in (
            "additional_physical_carrier_experiment_declared",
            "experiment_scope_single_carrier",
            "experiment_scope_single_surface_or_packet",
            "source_carrier_declared",
            "receiving_carrier_declared",
            "permitted_operation_receipt_or_block_only",
            "return_required_for_body_visibility",
            "admission_not_created_by_return",
        ):
            self.assertIs(statement[key], True)
        for key in (
            "distributed_standing_created",
            "currentness_created",
            "carrier_hierarchy_created",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "self_orientation_on_receiving_carrier_authorized",
            "conformance_on_receiving_carrier_authorized",
            "relation_on_receiving_carrier_authorized",
            "distributed_operation_authorized",
            "continuation_authorized",
            "success_authorizes_expansion",
        ):
            self.assertIs(statement[key], False)

        for key in EXPERIMENT_NON_MEANING_KEYS:
            self.assertIn(key, result["experiment_non_meaning"])
            self.assertIs(result["experiment_non_meaning"][key], True)
        for key in OPEN_KEYS:
            self.assertIn(key, result["what_remains_open"])
            self.assertIs(result["what_remains_open"][key], True)
        self.assert_all_result_non_claims_false(result)

    def test_summary_helper(self) -> None:
        result = self.declared_result()
        summary = resolver.build_additional_physical_carrier_experiment_summary(result)

        self.assertEqual(summary["outcome"], "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["experiment_request_id"], REQUEST_ID)
        self.assertEqual(summary["experiment_question"], result["declared_experiment_question"]["experiment_question"])
        self.assertEqual(summary["experiment_purpose"], result["declared_experiment_question"]["experiment_purpose"])
        self.assertEqual(summary["experiment_intent"], "DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT")
        self.assertEqual(summary["source_carrier_id"], SOURCE_CARRIER_ID)
        self.assertEqual(summary["receiving_carrier_id"], RECEIVING_CARRIER_ID)
        self.assertEqual(summary["selected_surface_or_packet_id"], SURFACE_ID)
        self.assertEqual(
            summary["selected_surface_or_packet_basis"],
            result["selected_carried_surface_or_packet"]["selected_surface_or_packet_basis"],
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIs(summary["experiment_declared"], True)
        self.assertIs(summary["single_carrier_scope"], True)
        self.assertIs(summary["single_surface_or_packet_scope"], True)
        self.assertIs(summary["permitted_operation_receipt_or_block_only"], True)
        self.assertIs(summary["return_required_for_body_visibility"], True)
        self.assertIs(summary["admission_not_created_by_return"], True)
        self.assertIs(summary["no_repository_synchronization"], True)
        self.assertIs(summary["no_full_body_transfer"], True)
        self.assertIs(summary["no_self_orientation_conformance_relation_on_receiving_carrier"], True)
        self.assertIs(summary["no_distributed_standing"], True)
        self.assertIs(summary["no_currentness"], True)
        self.assertIs(summary["no_carrier_hierarchy"], True)
        self.assertIs(summary["no_distributed_operation"], True)
        self.assertIs(summary["no_continuation"], True)
        self.assertIs(summary["no_success_based_expansion"], True)
        for key, value in summary["key_non_claims"].items():
            self.assertIn(key, FALSE_NON_CLAIMS)
            self.assertIs(value, False)
        for key in (
            "authority_created",
            "permission_created",
            "currentness_created",
            "source_replaced",
            "distributed_standing_created",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "distributed_operation_authorized",
            "continuation_authorized",
            "success_authorizes_expansion",
        ):
            self.assertIn(key, summary["key_non_claims"])

    def test_request_builder_helper_builds_declarable_request(self) -> None:
        surface = _selected_surface_or_packet(selected_surface_or_packet_id="helper_surface_001")
        request = resolver.build_declared_additional_physical_carrier_experiment_request(
            "helper_request_001",
            "May the helper-built request declare one receipt/refusal experiment?",
            "Exercise the bounded helper builder.",
            SOURCE_CARRIER_ID,
            RECEIVING_CARRIER_ID,
            surface,
        )

        self.assertEqual(request["experiment_request_id"], "helper_request_001")
        self.assertEqual(request["experiment_question"], "May the helper-built request declare one receipt/refusal experiment?")
        self.assertEqual(request["experiment_purpose"], "Exercise the bounded helper builder.")
        self.assertEqual(request["experiment_intent"], "DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT")
        self.assertEqual(request["source_carrier"]["carrier_id"], SOURCE_CARRIER_ID)
        self.assertEqual(request["receiving_carrier"]["carrier_id"], RECEIVING_CARRIER_ID)
        self.assertEqual(request["selected_carried_surface_or_packet"], surface)
        self.assertIs(request["experiment_scope"]["single_receiving_carrier"], True)
        self.assertIs(request["experiment_scope"]["single_surface_or_packet"], True)
        self.assertTrue(request["permitted_operations"])
        self.assertTrue(request["prohibited_operations"])
        self.assertIs(request["return_and_admission_posture"]["return_required_for_body_visibility"], True)
        self.assertEqual(request["declared_non_claims"], _non_claims())

        result = resolve(request)
        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
        )

    def test_path_based_resolution(self) -> None:
        request = valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "request.json"
            _write_json(path, request)

            result = resolver.resolve_additional_physical_carrier_experiment_boundary_from_path(path)

        self.assert_top_level_shape(result)
        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
        )
        self.assertEqual(result["declared_experiment_question"]["experiment_request_id"], REQUEST_ID)
        self.assertEqual(
            result["declared_experiment_question"]["experiment_request_path"],
            str(path),
        )

    def test_write_behavior_with_explicit_output_path(self) -> None:
        result = self.declared_result()

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "declared_result.json"
            written = resolver.write_additional_physical_carrier_experiment_result(
                result,
                output_path,
            )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            loaded = _read_json(written)

        self.assertEqual(set(loaded), TOP_LEVEL_SECTIONS)
        self.assertEqual(
            loaded["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
        )

    def test_default_output_path_is_bounded_and_non_overwriting(self) -> None:
        result = self.declared_result()

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "experiment_results"
            with mock.patch.object(
                resolver,
                "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_ROOT",
                root,
            ):
                first = resolver.write_additional_physical_carrier_experiment_result(result)
                second = resolver.write_additional_physical_carrier_experiment_result(result)

            self.assertEqual(first.parent, root)
            self.assertEqual(second.parent, root)
            self.assertTrue(first.name.endswith("__additional_physical_carrier_experiment_result.json"))
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        selected_before = copy.deepcopy(request["selected_carried_surface_or_packet"])
        request_before = copy.deepcopy(request)

        first = resolve(request)
        second = resolve(request)

        self.assertEqual(request, request_before)
        self.assertEqual(request["selected_carried_surface_or_packet"], selected_before)
        self.assertEqual(first["outcome"], second["outcome"])
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            resolver.write_additional_physical_carrier_experiment_result(first, output)
            self.assertEqual(request, request_before)

    def test_not_declared_readable_request(self) -> None:
        result = resolve(
            valid_request(
                experiment_intent="DO_NOT_DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT"
            )
        )

        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_NOT_DECLARED",
        )
        self.assertIs(result["experiment_declaration_statement"]["additional_physical_carrier_experiment_declared"], False)
        self.assertIs(result["experiment_declaration_statement"]["no_collapse_flags_true"], True)
        self.assertIn("not_declared_reason", result["experiment_declaration_statement"])
        self.assert_all_result_non_claims_false(result)

    def test_explicit_block_intent(self) -> None:
        result = resolve(
            valid_request(
                experiment_intent="BLOCK_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT"
            )
        )

        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED",
        )
        self.assertEqual(
            result["block"]["block_code"],
            "EXPERIMENT_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assertIs(result["experiment_declaration_statement"]["additional_physical_carrier_experiment_declared"], False)

    def test_blocking_missing_and_malformed_request(self) -> None:
        result = resolver.resolve_additional_physical_carrier_experiment_boundary()
        self.assertEqual(
            result["outcome"],
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED",
        )
        self.assertEqual(result["block"]["block_code"], "EXPERIMENT_QUESTION_UNDECLARED")

        self.assert_block_code(
            ["not", "a", "mapping"],
            "DECLARED_EXPERIMENT_REQUEST_MALFORMED",
        )

    def test_blocking_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            malformed = Path(tmp) / "malformed.json"
            array = Path(tmp) / "array.json"
            malformed.write_text("{not-json", encoding="utf-8")
            _write_json(array, [])

            cases = (
                (missing, "DECLARED_EXPERIMENT_REQUEST_UNREADABLE"),
                (malformed, "DECLARED_EXPERIMENT_REQUEST_MALFORMED"),
                (array, "DECLARED_EXPERIMENT_REQUEST_MALFORMED"),
            )
            for path, code in cases:
                with self.subTest(path=path):
                    result = resolver.resolve_additional_physical_carrier_experiment_boundary_from_path(path)
                    self.assertEqual(
                        result["outcome"],
                        "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_BLOCKED",
                    )
                    self.assertEqual(result["block"]["block_code"], code)

    def test_blocking_question_purpose_and_intent(self) -> None:
        cases = (
            ({"experiment_question": ""}, "EXPERIMENT_QUESTION_UNDECLARED"),
            ({"experiment_purpose": ""}, "EXPERIMENT_PURPOSE_UNDECLARED"),
            ({"experiment_intent": "DECLARE_DISTRIBUTED_STANDING"}, "EXPERIMENT_INTENT_UNSUPPORTED"),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_source_receiving_carrier_missing_or_collapsed(self) -> None:
        cases = (
            ({"source_carrier": None}, "SOURCE_CARRIER_MISSING"),
            ({"receiving_carrier": None}, "RECEIVING_CARRIER_MISSING"),
            (
                {
                    "receiving_carrier": {
                        "carrier_id": SOURCE_CARRIER_ID,
                        "carrier_role": "EXPERIMENT_RECEIVING_CARRIER",
                        "role_is_operation_local": True,
                    }
                },
                "SOURCE_AND_RECEIVING_CARRIER_COLLAPSED",
            ),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_selected_surface_or_packet_shape(self) -> None:
        cases = (
            ({"selected_carried_surface_or_packet": None}, "SELECTED_SURFACE_OR_PACKET_MISSING"),
            ({"selected_carried_surface_or_packet": ["malformed"]}, "SELECTED_SURFACE_OR_PACKET_MALFORMED"),
            (
                {
                    "selected_carried_surface_or_packet": {
                        "selected_surface_or_packet_basis": {"basis_id": "basis-only"}
                    }
                },
                "SELECTED_SURFACE_OR_PACKET_IDENTITY_MISSING",
            ),
            (
                {
                    "selected_carried_surface_or_packet": {
                        "selected_surface_or_packet_id": "surface-without-basis"
                    }
                },
                "SELECTED_SURFACE_OR_PACKET_BASIS_MISSING",
            ),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_unsupported_carrier_role(self) -> None:
        request = valid_request()
        request["source_carrier"]["carrier_role"] = "UNSUPPORTED_SOURCE_ROLE"

        self.assert_block_code(request, "CARRIER_ROLE_UNSUPPORTED")

    def test_blocking_scope_not_single_carrier_or_surface(self) -> None:
        carrier_scope = valid_request()
        carrier_scope["experiment_scope"].update(
            {
                "single_receiving_carrier": False,
                "single_carrier": False,
                "experiment_scope_single_carrier": False,
                "receiving_carrier_count": 2,
            }
        )
        self.assert_block_code(carrier_scope, "EXPERIMENT_SCOPE_NOT_SINGLE_CARRIER")

        surface_scope = valid_request()
        surface_scope["experiment_scope"].update(
            {
                "single_surface_or_packet": False,
                "single_carried_surface_or_packet": False,
                "experiment_scope_single_surface_or_packet": False,
                "selected_surface_or_packet_count": 2,
            }
        )
        self.assert_block_code(surface_scope, "EXPERIMENT_SCOPE_NOT_SINGLE_SURFACE_OR_PACKET")

    def test_blocking_permitted_or_prohibited_operations(self) -> None:
        request = valid_request(permitted_operations=["RUN_SELF_ORIENTATION"])
        self.assert_block_code(request, "PERMITTED_OPERATIONS_NOT_RECEIPT_OR_BLOCK_ONLY")

        request = valid_request(prohibited_operations={})
        self.assert_block_code(request, "PROHIBITED_OPERATIONS_NOT_EXPLICIT")

    def test_blocking_return_posture_missing_or_return_creates_admission(self) -> None:
        request = valid_request(return_and_admission_posture={})
        self.assert_block_code(request, "RETURN_POSTURE_MISSING")

        request = valid_request(
            return_and_admission_posture={
                "return_required_for_body_visibility": True,
                "admission_not_created_by_return": False,
                "admission_created_by_return": True,
            }
        )
        self.assert_block_code(request, "ADMISSION_CREATED_BY_RETURN")

    def test_blocking_receiving_carrier_body_functions_requested(self) -> None:
        cases = (
            ({"self_orientation_on_receiving_carrier_authorized": True}, "SELF_ORIENTATION_ON_RECEIVING_CARRIER_REQUESTED"),
            ({"conformance_on_receiving_carrier_authorized": True}, "CONFORMANCE_ON_RECEIVING_CARRIER_REQUESTED"),
            ({"relation_on_receiving_carrier_authorized": True}, "RELATION_CONFORMANCE_OR_CLOSURE_ON_RECEIVING_CARRIER_REQUESTED"),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_sync_transfer_registry(self) -> None:
        cases = (
            ({"repository_synchronization_authorized": True}, "REPOSITORY_SYNCHRONIZATION_REQUESTED"),
            ({"full_body_transfer_authorized": True}, "FULL_BODY_TRANSFER_REQUESTED"),
            ({"carrier_registry_created": True}, "CARRIER_REGISTRY_REQUESTED"),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_currentness_distributed_standing_operation_and_continuation(self) -> None:
        cases = (
            ({"currentness_requested": True}, "CURRENTNESS_REQUESTED"),
            ({"distributed_standing_requested": True}, "DISTRIBUTED_STANDING_REQUESTED"),
            ({"distributed_operation_authorized": True}, "DISTRIBUTED_OPERATION_REQUESTED"),
            ({"continuation_authorized": True}, "CONTINUATION_REQUESTED"),
        )
        for update, code in cases:
            with self.subTest(code=code):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_majority_success_count_or_latest_file_decisioning(self) -> None:
        cases = (
            {"majority_carrier_currentness": True},
            {"successful_receipt_count_currentness": True},
            {"latest_file_currentness": True},
        )
        for update in cases:
            with self.subTest(update=update):
                request = valid_request()
                request.update(update)
                self.assert_block_code(
                    request,
                    "MAJORITY_OR_SUCCESS_COUNT_DECISIONING_REQUESTED",
                )

    def test_blocking_source_replacement_authority_permission_and_hierarchy(self) -> None:
        cases = (
            ({"source_replaced": True}, "SOURCE_REPLACEMENT_REQUESTED"),
            ({"authority_created": True}, "AUTHORITY_OR_PERMISSION_BEYOND_DECLARED_EXPERIMENT"),
            ({"permission_created": True}, "AUTHORITY_OR_PERMISSION_BEYOND_DECLARED_EXPERIMENT"),
            ({"carrier_hierarchy_created": True}, "CARRIER_HIERARCHY_CREATED"),
            ({"winning_carrier_selected": True}, "CARRIER_HIERARCHY_CREATED"),
            ({"losing_carrier_invalidated": True}, "CARRIER_HIERARCHY_CREATED"),
        )
        for update, code in cases:
            with self.subTest(code=code, update=update):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_hidden_refusal_divergence_and_mutation_replay_merge(self) -> None:
        cases = (
            ({"refusal_hidden": True}, "EXPERIMENT_HIDES_REFUSAL_OR_DIVERGENCE"),
            ({"divergence_hidden": True}, "EXPERIMENT_HIDES_REFUSAL_OR_DIVERGENCE"),
            ({"mismatch_hidden": True}, "EXPERIMENT_HIDES_REFUSAL_OR_DIVERGENCE"),
            ({"mutation_requested": True}, "MUTATION_REPLAY_OR_MERGE_REQUESTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_REQUESTED"),
            ({"merge_requested": True}, "MUTATION_REPLAY_OR_MERGE_REQUESTED"),
        )
        for update, code in cases:
            with self.subTest(code=code, update=update):
                request = valid_request()
                request.update(update)
                self.assert_block_code(request, code)

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        missing_claims = _non_claims()
        missing_claims.pop("merge_performed")
        missing_request = valid_request(declared_non_claims=missing_claims)
        missing_result = self.assert_block_code(
            missing_request,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        self.assertNotIn(
            "merge_performed",
            missing_result["experiment_declaration_statement"]["non_claims_where_available"],
        )

        flipped_claims = _non_claims()
        flipped_claims["merge_performed"] = True
        flipped_request = valid_request(declared_non_claims=flipped_claims)
        flipped_result = self.assert_block_code(
            flipped_request,
            "MUTATION_REPLAY_OR_MERGE_REQUESTED",
        )
        self.assertIs(
            flipped_result["experiment_declaration_statement"]["non_claims_where_available"]["merge_performed"],
            True,
        )

    def test_result_level_non_claims_for_declared_not_declared_and_blocked(self) -> None:
        results = (
            self.declared_result(),
            resolve(valid_request(experiment_intent="DO_NOT_DECLARE_ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT")),
            resolve(valid_request(experiment_question="")),
        )
        for result in results:
            with self.subTest(outcome=result["outcome"]):
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assert_all_result_non_claims_false(result)


if __name__ == "__main__":
    unittest.main()
