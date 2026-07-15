"""Tests for the bounded derivative-vessel relation boundary resolver.

This suite exercises one source/body basis, one derivative vessel result, and
one relation declaration. It verifies relation recognition without opening a
vessel implementation, registry, adoption path, public release surface, or
permission surface.
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

import resolve_derivative_vessel_relation_boundary as resolver


SELF_ORIENTATION_ID = "current_self_orientation_v5_self_oriented_001"
SELF_ORIENTATION_PATH = "artifacts/synthetic/current_self_orientation_v5_result.json"
SOURCE_SURFACE_ID = "current_state_what_stands_now_answered_001"
SOURCE_SURFACE_PATH = "artifacts/synthetic/current_state_what_stands_now_result.json"
DERIVATIVE_RESULT_ID = "bounded_current_state_read_v3_answered_001"
DERIVATIVE_RESULT_PATH = "artifacts/synthetic/bounded_current_state_vessel_v3_result.json"
RELATION_ID = "bounded_derivative_vessel_relation_001"
RELATION_TYPE = "bounded_derivative_vessel_relation_boundary"

TOP_LEVEL_SECTIONS = (
    "derivative_vessel_relation_boundary_metadata",
    "selected_source_body_basis",
    "selected_derivative_vessel_basis",
    "selected_relation_declaration",
    "relation_boundary_checks",
    "outcome",
    "block",
    "recognized_derivative_vessel_relation",
    "derivative_vessel_relation_boundary_basis",
    "derivative_vessel_relation_boundary_summary",
    "non_claims",
)

RESULT_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "derivative_upgraded_to_source",
    "operator_upgraded_to_source",
    "adoption_created",
    "privileged_standing_created",
    "public_release_created",
    "final_governance_completed",
    "final_system_identity_completed",
    "continuity_completed",
    "general_vessel_permission_created",
    "follow_on_vessels_authorized",
    "latest_file_currentness",
    "source_derivative_operator_collapsed",
)

RELATION_BOUND_FIELDS = (
    "relation_is_downstream",
    "source_basis_preserved",
    "derivative_output_preserved",
    "operator_facing_output_downstream_if_present",
    "relation_reversible",
    "relation_additive_only",
    "no_source_replacement",
    "no_authority_creation",
    "no_currentness_creation",
    "no_permission_creation",
    "no_adoption_creation",
    "no_privileged_standing",
    "no_final_governance_completion",
    "no_final_system_identity_completion",
)

HIERARCHY_FIELDS = (
    "vessel_allowed_as_source",
    "vessel_allowed_as_authority",
    "vessel_allowed_as_currentness_source",
    "vessel_allowed_as_permission_source",
    "vessel_allowed_as_adoption_path",
    "vessel_allowed_as_public_release",
    "vessel_allowed_as_final_governance",
    "operator_surface_allowed_as_source",
    "derivative_output_allowed_to_replace_source",
    "latest_file_recency_allowed",
)

CORRESPONDENCE_FIELDS = (
    "must_preserve_source_identity",
    "must_preserve_source_outcome",
    "must_preserve_derivative_basis",
    "must_preserve_source_derivative_distinction",
    "must_preserve_operator_downstream_distinction",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_upgrade_operator_to_source",
    "does_not_create_adoption",
    "does_not_create_privileged_standing",
    "does_not_complete_final_governance",
    "does_not_complete_final_system_identity",
    "does_not_complete_continuity",
    "does_not_create_public_release",
    "does_not_create_general_vessel_permission",
    "does_not_authorize_follow_on_vessels",
)


def deep_set(value: dict, path: tuple[str, ...], replacement: object) -> dict:
    copied = copy.deepcopy(value)
    cursor = copied
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = replacement
    return copied


def deep_delete(value: dict, path: tuple[str, ...]) -> dict:
    copied = copy.deepcopy(value)
    cursor = copied
    for key in path[:-1]:
        cursor = cursor[key]
    del cursor[path[-1]]
    return copied


def source_body_basis(
    *,
    outcome: str = "SELF_ORIENTED",
    source_surface_id: str = SOURCE_SURFACE_ID,
    source_surface_path: str = SOURCE_SURFACE_PATH,
    non_claim_updates: dict[str, bool] | None = None,
    governing_updates: dict[str, object] | None = None,
) -> dict:
    non_claims = {
        "authority_created": False,
        "permission_created": False,
        "currentness_created": False,
        "source_replaced": False,
        "derivative_outputs_upgraded_to_source": False,
        "operator_outputs_upgraded_to_source": False,
        "latest_file_currentness": False,
        "recency_fraud": False,
    }
    if non_claim_updates:
        non_claims.update(non_claim_updates)
    governing = {
        "basis_family": "current_state_what_stands_now_result",
        "basis_result_id": source_surface_id,
        "basis_result_path": source_surface_path,
    }
    if governing_updates:
        governing.update(governing_updates)
    return {
        "current_self_orientation_v5_metadata": {
            "self_orientation_result_id": SELF_ORIENTATION_ID,
            "self_orientation_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V5_RESULT"
            ),
            "self_orientation_result_version": "0.5.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v5",
        },
        "selected_orientation_inputs": {
            "selected_source_surface": {
                "result_id": source_surface_id,
                "result_path": source_surface_path,
                "result_family": "current_state_what_stands_now_result",
                "result_type": (
                    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_STANDS_NOW_RESULT"
                ),
                "outcome": "ANSWERED_WHAT_STANDS_NOW",
            },
            "selected_effective_references": {
                "current_governing_source_run_path": "artifacts/synthetic/source_run.json",
                "current_authority_artifact_path": "artifacts/synthetic/authority.json",
            },
        },
        "recognized_current_state_surfaces": {
            "selected_source_surface_id": source_surface_id,
            "source_body_basis_remains_upstream": True,
        },
        "recognized_governing_effective_basis": governing,
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None},
        "non_claims": non_claims,
    }


def derivative_vessel_result(
    *,
    source_surface_id: str = SOURCE_SURFACE_ID,
    source_surface_path: str = SOURCE_SURFACE_PATH,
    source_surface_family: str = "current_state_what_stands_now_result",
    source_surface_outcome: str = "ANSWERED_WHAT_STANDS_NOW",
    non_claim_updates: dict[str, bool] | None = None,
    answer_updates: dict[str, object] | None = None,
) -> dict:
    non_claims = {
        "source_replaced": False,
        "derivative_upgraded_to_source": False,
        "rank_assigned_by_model": False,
        "authority_assigned_by_model": False,
        "status_assigned_by_model": False,
        "standing_assigned_by_model": False,
        "provenance_assigned_by_model": False,
        "source_scope_widened": False,
        "continuity_completed": False,
        "authority_created": False,
        "permission_created": False,
        "currentness_created": False,
        "standing_created": False,
        "adoption_created": False,
    }
    if non_claim_updates:
        non_claims.update(non_claim_updates)
    answer = {
        "answer": "bounded derivative material",
        "answer_basis": "bounded_source_payload",
        "model_output_remains_derivative": True,
        "source_remains_source": True,
    }
    if answer_updates:
        answer.update(answer_updates)
    return {
        "openai_api_derivative_vessel_v3_metadata": {
            "vessel_result_id": DERIVATIVE_RESULT_ID,
            "vessel_result_type": (
                "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT"
            ),
            "vessel_result_version": "0.3.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "openai_api_vessel__bounded_current_state_read_v3",
        },
        "selected_source_surface": {
            "selected_source_surface_id": source_surface_id,
            "selected_source_surface_path": source_surface_path,
            "selected_source_surface_family": source_surface_family,
            "selected_source_surface_outcome": source_surface_outcome,
        },
        "outcome": "ANSWERED_DERIVATIVE_READ",
        "block": {"block_code": None, "block_reason": None},
        "derivative_answer": answer,
        "non_claims": non_claims,
    }


def relation_declaration(
    *,
    self_orientation_path: str = SELF_ORIENTATION_PATH,
    source_surface_id: str = SOURCE_SURFACE_ID,
    source_surface_path: str = SOURCE_SURFACE_PATH,
    source_surface_family: str = "current_state_what_stands_now_result",
    source_surface_outcome: str = "ANSWERED_WHAT_STANDS_NOW",
    derivative_path: str = DERIVATIVE_RESULT_PATH,
    derivative_output_basis: str = "bounded_source_payload",
) -> dict:
    return {
        "derivative_vessel_relation_metadata": {
            "derivative_vessel_relation_id": RELATION_ID,
            "derivative_vessel_relation_type": RELATION_TYPE,
            "derivative_vessel_relation_version": "0.1.0",
            "declared_at": "2026-04-26T00:00:00Z",
            "declared_by_surface": "bounded_relation_boundary_test_surface",
        },
        "source_body_basis": {
            "self_orientation_result_path": self_orientation_path,
            "self_orientation_result_id": SELF_ORIENTATION_ID,
            "self_orientation_outcome": "SELF_ORIENTED",
            "source_surface_path": source_surface_path,
            "source_surface_id": source_surface_id,
            "source_surface_family": source_surface_family,
            "source_surface_outcome": source_surface_outcome,
        },
        "derivative_vessel_basis": {
            "derivative_vessel_result_path": derivative_path,
            "derivative_vessel_result_id": DERIVATIVE_RESULT_ID,
            "derivative_vessel_result_type": (
                "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT"
            ),
            "derivative_vessel_result_outcome": "ANSWERED_DERIVATIVE_READ",
            "derivative_vessel_module": "openai_api_vessel__bounded_current_state_read_v3",
            "derivative_output_family": (
                "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
            ),
            "derivative_output_basis": derivative_output_basis,
        },
        "declared_relation_bounds": {
            field: True for field in RELATION_BOUND_FIELDS
        },
        "hierarchy_constraints": {field: False for field in HIERARCHY_FIELDS},
        "correspondence_requirements": {
            field: True for field in CORRESPONDENCE_FIELDS
        },
        "declared_non_claims": {
            field: True for field in DECLARED_NON_CLAIM_FIELDS
        },
    }


def valid_inputs() -> tuple[dict, dict, dict]:
    return source_body_basis(), derivative_vessel_result(), relation_declaration()


class DerivativeVesselRelationBoundaryTests(unittest.TestCase):
    def resolve(self, source: dict | None, derivative: dict | None, declaration: dict | None) -> dict:
        return resolver.resolve_derivative_vessel_relation_boundary(
            source_body_basis=source,
            derivative_vessel_result=derivative,
            relation_declaration=declaration,
        )

    def valid_result(self) -> dict:
        return self.resolve(*valid_inputs())

    def assert_top_level_shape(self, result: dict) -> None:
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertIn(result["outcome"], {"DERIVATIVE_VESSEL_RELATION_RECOGNIZED", "BLOCKED"})

    def assert_block_code(self, result: dict, code: str) -> None:
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], code)

    def assert_non_claims_false(self, result: dict) -> None:
        for key in RESULT_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_mapping_based_relation_recognition(self) -> None:
        result = self.valid_result()
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "DERIVATIVE_VESSEL_RELATION_RECOGNIZED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        relation = result["recognized_derivative_vessel_relation"]
        self.assertIsInstance(relation, dict)
        self.assertEqual(relation["source_body_basis_id"], SELF_ORIENTATION_ID)
        self.assertEqual(relation["derivative_vessel_result_id"], DERIVATIVE_RESULT_ID)
        self.assertEqual(relation["relation_id"], RELATION_ID)
        for key in (
            "downstream",
            "additive_only",
            "source_preserved",
            "derivative_preserved",
            "operator_downstream_where_present",
            "no_authority",
            "no_permission",
            "no_currentness",
            "no_adoption",
            "no_privileged_standing",
            "no_public_release",
            "no_source_replacement",
            "no_final_governance",
            "no_final_system_identity",
            "no_continuity_completion",
            "no_follow_on_vessel_authorization",
        ):
            self.assertIs(relation[key], True, key)
        self.assert_non_claims_false(result)

    def test_successful_path_based_relation_recognition(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_path = root / "source_body_basis.json"
            derivative_path = root / "derivative_vessel_result.json"
            source = source_body_basis()
            derivative = derivative_vessel_result()
            source_path.write_text(json.dumps(source), encoding="utf-8")
            derivative_path.write_text(json.dumps(derivative), encoding="utf-8")
            declaration = relation_declaration(
                self_orientation_path=str(source_path),
                derivative_path=str(derivative_path),
            )
            result = resolver.resolve_derivative_vessel_relation_boundary_from_paths(
                source_path,
                derivative_path,
                declaration,
            )
        self.assertEqual(result["outcome"], "DERIVATIVE_VESSEL_RELATION_RECOGNIZED")
        self.assertEqual(result["selected_source_body_basis"]["source_body_basis_path"], str(source_path))
        self.assertEqual(
            result["selected_derivative_vessel_basis"]["derivative_vessel_result_path"],
            str(derivative_path),
        )
        self.assertEqual(
            result["selected_relation_declaration"]["source_body_basis"][
                "self_orientation_result_path"
            ],
            str(source_path),
        )
        self.assertEqual(
            result["selected_relation_declaration"]["derivative_vessel_basis"][
                "derivative_vessel_result_path"
            ],
            str(derivative_path),
        )
        self.assert_top_level_shape(result)

    def test_metadata_and_selected_sections_are_preserved(self) -> None:
        result = self.valid_result()
        metadata = result["derivative_vessel_relation_boundary_metadata"]
        for key in (
            "derivative_vessel_relation_boundary_result_id",
            "derivative_vessel_relation_boundary_result_type",
            "derivative_vessel_relation_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["derivative_vessel_relation_boundary_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_derivative_vessel_relation_boundary")

        source = result["selected_source_body_basis"]
        self.assertEqual(source["self_orientation_result_id"], SELF_ORIENTATION_ID)
        self.assertEqual(source["self_orientation_outcome"], "SELF_ORIENTED")
        self.assertEqual(source["source_surface_id"], SOURCE_SURFACE_ID)
        self.assertEqual(source["source_surface_path"], SOURCE_SURFACE_PATH)
        self.assertEqual(source["source_surface_family"], "current_state_what_stands_now_result")
        self.assertEqual(source["source_surface_outcome"], "ANSWERED_WHAT_STANDS_NOW")
        self.assertIs(source["source_body_basis_remains_upstream"], True)
        self.assertEqual(source["selection_mode"], "mapping_supplied_source_body_basis")
        self.assertIn("current_governing_effective_references", source)

        derivative = result["selected_derivative_vessel_basis"]
        self.assertEqual(derivative["derivative_vessel_result_id"], DERIVATIVE_RESULT_ID)
        self.assertEqual(derivative["derivative_vessel_result_outcome"], "ANSWERED_DERIVATIVE_READ")
        self.assertEqual(
            derivative["derivative_vessel_result_type"],
            "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT",
        )
        self.assertEqual(derivative["derivative_vessel_module"], "openai_api_vessel__bounded_current_state_read_v3")
        self.assertEqual(
            derivative["derivative_output_family"],
            "openai_api_derivative_vessel_bounded_current_state_read_v3_result",
        )
        self.assertEqual(derivative["derivative_output_basis"], "bounded_source_payload")
        self.assertIs(derivative["source_basis_preserved"], True)
        self.assertIs(derivative["derivative_output_remains_derivative"], True)

        declaration = result["selected_relation_declaration"]
        for section in (
            "derivative_vessel_relation_metadata",
            "source_body_basis",
            "derivative_vessel_basis",
            "declared_relation_bounds",
            "hierarchy_constraints",
            "correspondence_requirements",
            "declared_non_claims",
        ):
            self.assertIn(section, declaration)

    def test_summary_helper_reports_bounded_relation_status(self) -> None:
        result = self.valid_result()
        summary = resolver.build_derivative_vessel_relation_boundary_summary(result)
        self.assertEqual(summary["outcome"], "DERIVATIVE_VESSEL_RELATION_RECOGNIZED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["selected_source_body_basis_id"], SELF_ORIENTATION_ID)
        self.assertEqual(summary["selected_derivative_vessel_result_id"], DERIVATIVE_RESULT_ID)
        self.assertEqual(summary["relation_id"], RELATION_ID)
        self.assertEqual(summary["relation_type"], RELATION_TYPE)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIs(summary["source_body_basis_passed"], True)
        self.assertIs(summary["derivative_vessel_basis_passed"], True)
        self.assertIs(summary["relation_bounds_passed"], True)
        self.assertIs(summary["hierarchy_constraints_passed"], True)
        self.assertIs(summary["correspondence_requirements_passed"], True)
        self.assertIs(summary["non_claims_passed"], True)
        for key in RESULT_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_write_helpers_explicit_and_default_paths(self) -> None:
        result = self.valid_result()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            explicit = root / "nested" / "relation_result.json"
            written = resolver.write_derivative_vessel_relation_boundary_result(result, explicit)
            self.assertEqual(written, explicit)
            loaded = json.loads(explicit.read_text(encoding="utf-8"))
            self.assertEqual(set(TOP_LEVEL_SECTIONS), set(loaded))

            original_default = resolver._safe_default_output_path

            def temp_default(candidate: dict) -> Path:
                return original_default(candidate, root=root / "default")

            with mock.patch.object(resolver, "_safe_default_output_path", temp_default):
                first = resolver.write_derivative_vessel_relation_boundary_result(result)
                second = resolver.write_derivative_vessel_relation_boundary_result(result)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn(RELATION_ID, first.name)
            self.assertTrue(second.name.endswith("_001.json"))

    def test_missing_inputs_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        cases = (
            (None, derivative, declaration, "SOURCE_BODY_BASIS_MISSING"),
            (source, None, declaration, "DERIVATIVE_VESSEL_RESULT_MISSING"),
            (source, derivative, None, "RELATION_DECLARATION_MISSING"),
        )
        for case in cases:
            with self.subTest(block=case[3]):
                result = self.resolve(*case[:3])
                self.assert_block_code(result, case[3])
                self.assert_non_claims_false(result)

    def test_path_unreadable_and_malformed_inputs_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid_source_path = root / "source.json"
            valid_derivative_path = root / "derivative.json"
            valid_source_path.write_text(json.dumps(source_body_basis()), encoding="utf-8")
            valid_derivative_path.write_text(json.dumps(derivative_vessel_result()), encoding="utf-8")
            malformed_source = root / "malformed_source.json"
            malformed_source.write_text("{", encoding="utf-8")
            array_source = root / "array_source.json"
            array_source.write_text("[]", encoding="utf-8")
            malformed_derivative = root / "malformed_derivative.json"
            malformed_derivative.write_text("{", encoding="utf-8")
            array_derivative = root / "array_derivative.json"
            array_derivative.write_text("[]", encoding="utf-8")

            source_cases = (
                (root / "missing_source.json", "SOURCE_BODY_BASIS_UNREADABLE"),
                (malformed_source, "SOURCE_BODY_BASIS_MALFORMED"),
                (array_source, "SOURCE_BODY_BASIS_MALFORMED"),
            )
            for source_path, code in source_cases:
                with self.subTest(source_path=source_path.name):
                    result = resolver.resolve_derivative_vessel_relation_boundary_from_paths(
                        source_path,
                        valid_derivative_path,
                        relation_declaration(
                            self_orientation_path=str(source_path),
                            derivative_path=str(valid_derivative_path),
                        ),
                    )
                    self.assert_block_code(result, code)

            derivative_cases = (
                (root / "missing_derivative.json", "DERIVATIVE_VESSEL_RESULT_UNREADABLE"),
                (malformed_derivative, "DERIVATIVE_VESSEL_RESULT_MALFORMED"),
                (array_derivative, "DERIVATIVE_VESSEL_RESULT_MALFORMED"),
            )
            for derivative_path, code in derivative_cases:
                with self.subTest(derivative_path=derivative_path.name):
                    result = resolver.resolve_derivative_vessel_relation_boundary_from_paths(
                        valid_source_path,
                        derivative_path,
                        relation_declaration(
                            self_orientation_path=str(valid_source_path),
                            derivative_path=str(derivative_path),
                        ),
                    )
                    self.assert_block_code(result, code)

    def test_source_not_standing_and_derivative_source_mismatch_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        self.assert_block_code(
            self.resolve(source_body_basis(outcome="BLOCKED"), derivative, declaration),
            "SOURCE_BODY_BASIS_NOT_STANDING",
        )
        mismatched_derivative = derivative_vessel_result(source_surface_id="different_source_surface")
        self.assert_block_code(
            self.resolve(source, mismatched_derivative, declaration),
            "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        )

    def test_derivative_output_forbidden_postures_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        cases = (
            (
                derivative,
                deep_set(declaration, ("hierarchy_constraints", "vessel_allowed_as_source"), True),
                "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
            ),
            (
                derivative_vessel_result(non_claim_updates={"authority_assigned_by_model": True}),
                declaration,
                "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
            ),
            (
                derivative_vessel_result(non_claim_updates={"status_assigned_by_model": True}),
                declaration,
                "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
            ),
            (
                derivative_vessel_result(non_claim_updates={"permission_created": True}),
                declaration,
                "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION",
            ),
            (
                derivative,
                deep_set(declaration, ("hierarchy_constraints", "operator_surface_allowed_as_source"), True),
                "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
            ),
        )
        for derivative_case, declaration_case, code in cases:
            with self.subTest(code=code):
                self.assert_block_code(self.resolve(source, derivative_case, declaration_case), code)

    def test_relation_declaration_malformed_vague_and_replacement_blocks(self) -> None:
        source, derivative, declaration = valid_inputs()
        self.assert_block_code(
            self.resolve(source, derivative, {"derivative_vessel_relation_metadata": {}}),
            "RELATION_DECLARATION_MALFORMED",
        )
        vague = deep_set(
            declaration,
            ("derivative_vessel_relation_metadata", "declared_by_surface"),
            "relate generally",
        )
        self.assert_block_code(self.resolve(source, derivative, vague), "RELATION_VAGUE_OR_UNBOUNDED")
        replacement_bound = deep_set(
            declaration,
            ("declared_relation_bounds", "no_source_replacement"),
            False,
        )
        self.assert_block_code(
            self.resolve(source, derivative, replacement_bound),
            "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
        )
        replacement_hierarchy = deep_set(
            declaration,
            ("hierarchy_constraints", "derivative_output_allowed_to_replace_source"),
            True,
        )
        self.assert_block_code(
            self.resolve(source, derivative, replacement_hierarchy),
            "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
        )

    def test_relation_attempts_forbidden_outcomes_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        cases = (
            (("declared_relation_bounds", "no_authority_creation"), False, "RELATION_ATTEMPTS_AUTHORITY"),
            (("declared_relation_bounds", "no_currentness_creation"), False, "RELATION_ATTEMPTS_CURRENTNESS"),
            (("declared_relation_bounds", "no_permission_creation"), False, "RELATION_ATTEMPTS_PERMISSION"),
            (("declared_relation_bounds", "no_adoption_creation"), False, "RELATION_ATTEMPTS_ADOPTION"),
            (("declared_relation_bounds", "no_privileged_standing"), False, "RELATION_ATTEMPTS_PRIVILEGED_STANDING"),
            (("hierarchy_constraints", "vessel_allowed_as_public_release"), True, "RELATION_ATTEMPTS_PUBLIC_RELEASE"),
            (("declared_relation_bounds", "no_final_governance_completion"), False, "RELATION_ATTEMPTS_FINAL_GOVERNANCE"),
            (("declared_relation_bounds", "no_final_system_identity_completion"), False, "RELATION_ATTEMPTS_FINAL_SYSTEM_IDENTITY"),
            (("declared_non_claims", "does_not_complete_continuity"), False, "RELATION_ATTEMPTS_CONTINUITY_COMPLETION"),
            (("declared_non_claims", "does_not_create_general_vessel_permission"), False, "RELATION_ATTEMPTS_GENERAL_VESSEL_PERMISSION"),
            (("declared_non_claims", "does_not_authorize_follow_on_vessels"), False, "RELATION_ATTEMPTS_FOLLOW_ON_VESSEL_AUTHORIZATION"),
        )
        for path, replacement, code in cases:
            with self.subTest(code=code):
                self.assert_block_code(
                    self.resolve(source, derivative, deep_set(declaration, path, replacement)),
                    code,
                )

    def test_hierarchy_constraints_flipped_or_omitted_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        expected = {
            "vessel_allowed_as_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
            "vessel_allowed_as_authority": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
            "vessel_allowed_as_currentness_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
            "vessel_allowed_as_permission_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION",
            "vessel_allowed_as_adoption_path": "RELATION_ATTEMPTS_ADOPTION",
            "vessel_allowed_as_public_release": "RELATION_ATTEMPTS_PUBLIC_RELEASE",
            "vessel_allowed_as_final_governance": "RELATION_ATTEMPTS_FINAL_GOVERNANCE",
            "operator_surface_allowed_as_source": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
            "derivative_output_allowed_to_replace_source": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
            "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
        }
        for field, code in expected.items():
            with self.subTest(field=field):
                self.assert_block_code(
                    self.resolve(
                        source,
                        derivative,
                        deep_set(declaration, ("hierarchy_constraints", field), True),
                    ),
                    code,
                )
        omitted = deep_delete(declaration, ("hierarchy_constraints", "vessel_allowed_as_source"))
        self.assert_block_code(
            self.resolve(source, derivative, omitted),
            "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
        )

    def test_correspondence_requirements_flipped_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        expected = {
            "must_preserve_source_identity": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
            "must_preserve_source_outcome": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
            "must_preserve_derivative_basis": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
            "must_preserve_source_derivative_distinction": "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
            "must_preserve_operator_downstream_distinction": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
            "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
            "must_prevent_over_mirroring": "RELATION_VAGUE_OR_UNBOUNDED",
            "must_prevent_under_mirroring": "RELATION_VAGUE_OR_UNBOUNDED",
        }
        for field, code in expected.items():
            with self.subTest(field=field):
                self.assert_block_code(
                    self.resolve(
                        source,
                        derivative,
                        deep_set(declaration, ("correspondence_requirements", field), False),
                    ),
                    code,
                )
        mismatched_source_id = deep_set(
            declaration,
            ("source_body_basis", "source_surface_id"),
            "different_source_surface",
        )
        self.assert_block_code(
            self.resolve(source, derivative, mismatched_source_id),
            "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        )

    def test_declared_non_claims_flipped_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        expected = {field: "NON_CLAIM_MISSING_OR_FLIPPED" for field in DECLARED_NON_CLAIM_FIELDS}
        expected["does_not_complete_continuity"] = "RELATION_ATTEMPTS_CONTINUITY_COMPLETION"
        expected["does_not_create_general_vessel_permission"] = (
            "RELATION_ATTEMPTS_GENERAL_VESSEL_PERMISSION"
        )
        expected["does_not_authorize_follow_on_vessels"] = (
            "RELATION_ATTEMPTS_FOLLOW_ON_VESSEL_AUTHORIZATION"
        )
        for field, code in expected.items():
            with self.subTest(field=field):
                self.assert_block_code(
                    self.resolve(
                        source,
                        derivative,
                        deep_set(declaration, ("declared_non_claims", field), False),
                    ),
                    code,
                )
        missing = deep_delete(declaration, ("declared_non_claims", "does_not_create_authority"))
        self.assert_block_code(
            self.resolve(source, derivative, missing),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    def test_recency_and_collapse_language_block(self) -> None:
        source, derivative, declaration = valid_inputs()
        recency = deep_set(
            declaration,
            ("derivative_vessel_relation_metadata", "declared_by_surface"),
            "latest file selector",
        )
        self.assert_block_code(self.resolve(source, derivative, recency), "LATEST_FILE_RECENCY_REFUSED")
        collapse = deep_set(
            declaration,
            ("derivative_vessel_relation_metadata", "declared_by_surface"),
            "derivative as source",
        )
        self.assert_block_code(
            self.resolve(source, derivative, collapse),
            "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        )

    def test_non_claims_false_for_recognized_and_blocked_results(self) -> None:
        recognized = self.valid_result()
        blocked = self.resolve(
            source_body_basis(outcome="BLOCKED"),
            derivative_vessel_result(),
            relation_declaration(),
        )
        self.assert_non_claims_false(recognized)
        self.assert_non_claims_false(blocked)

    def test_non_mutation_posture(self) -> None:
        source, derivative, declaration = valid_inputs()
        source_before = copy.deepcopy(source)
        derivative_before = copy.deepcopy(derivative)
        declaration_before = copy.deepcopy(declaration)
        first = self.resolve(source, derivative, declaration)
        second = self.resolve(source, derivative, declaration)
        self.assertEqual(source, source_before)
        self.assertEqual(derivative, derivative_before)
        self.assertEqual(declaration, declaration_before)
        self.assertEqual(first["outcome"], "DERIVATIVE_VESSEL_RELATION_RECOGNIZED")
        self.assertEqual(second["outcome"], "DERIVATIVE_VESSEL_RELATION_RECOGNIZED")

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "relation.json"
            resolver.write_derivative_vessel_relation_boundary_result(first, target)
            with self.assertRaises(FileExistsError):
                resolver.write_derivative_vessel_relation_boundary_result(first, target)


if __name__ == "__main__":
    unittest.main()
