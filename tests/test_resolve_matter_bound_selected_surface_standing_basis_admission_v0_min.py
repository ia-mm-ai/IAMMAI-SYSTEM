"""Adversarial tests for one exact selected-surface standing-basis admission.

The positive surface is the complete pair-preserved result owned by
DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION.  The v2 applicability result is
supplied only as source-owned applicability basis for the exact
descendant-body-creation-boundary route; it is never a standing creator or a
substitute singleton surface.
"""

from __future__ import annotations

import builtins
import copy
import hashlib
import inspect
import json
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_matter_bound_selected_surface_standing_basis_admission_v0_min as resolver


LIVE_APPLICABILITY_ARTIFACT = (
    REPO_ROOT
    / "artifacts"
    / "descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2"
    / "descendant_body_candidate_standing_effect_applicability_boundary_001__descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_result.json"
)
DELETE = object()


def _request() -> dict:
    return resolver.build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request()


def _change(document: dict, path: tuple[str, ...], value: object) -> dict:
    changed = copy.deepcopy(document)
    cursor = changed
    for key in path[:-1]:
        cursor = cursor[key]
    if value is DELETE:
        del cursor[path[-1]]
    else:
        cursor[path[-1]] = copy.deepcopy(value)
    return changed


class MatterBoundSelectedSurfaceStandingBasisAdmissionTests(unittest.TestCase):
    maxDiff = None

    def assert_terminal(
        self,
        result: dict,
        outcome: str,
        stopping_code: str | None = None,
    ) -> None:
        self.assertEqual(result["outcome"], outcome)
        self.assertEqual(result["result"]["outcome"], outcome)
        self.assertTrue(result["result"]["lawful_terminal_outcome_recorded"])
        self.assertTrue(result["result"]["review_exhausted"])
        self.assertEqual(result["result"]["stopping_code"], stopping_code)
        self.assertEqual(
            result["failed_check_count"],
            sum(check["passed"] is False for check in result["checks"]),
        )
        self.assertEqual(
            result["passed_check_count"],
            sum(check["passed"] is True for check in result["checks"]),
        )
        for check in result["checks"]:
            if check["failure_code"] is not None:
                self.assertIn(check["failure_code"], resolver.STOP_CODES)
            if check["block_code"] is not None:
                self.assertIn(check["block_code"], resolver.BLOCK_CODES)
        self.assertEqual(
            result["block"]["blocked"],
            outcome == resolver.OUTCOME_REVIEW_BLOCKED,
        )
        if outcome == resolver.OUTCOME_REVIEW_BLOCKED:
            self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        else:
            self.assertIsNone(result["block"]["code"])
        self.assertEqual(result["non_claims"], resolver.CANONICAL_NON_CLAIMS)
        self.assertTrue(all(value is False for value in result["non_claims"].values()))

    def assert_blocked(self, request: object, code: str) -> dict:
        result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            request
        )
        self.assert_terminal(result, resolver.OUTCOME_REVIEW_BLOCKED, code)
        return result

    def assert_additional(self, request: object, code: str) -> dict:
        result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            request
        )
        self.assert_terminal(result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS, code)
        return result

    def assert_no_local_power(self, result: dict) -> None:
        admission = result["admission"]
        for key in (
            "surface_standing_established_here",
            "source_applicability_created_here",
            "candidate_a_independently_selected",
            "candidate_b_independently_selected",
            "candidate_pair_split",
            "candidate_pair_ranked",
            "descendant_body_creation_authorized",
            "descendant_body_creation_executed",
            "correspondence_applicability_created",
            "downstream_authorization_created",
            "runtime_created",
            "operation_created",
            "reuse_permission_created",
            "follow_on_permission_created",
            "automatic_successor_created",
        ):
            self.assertIs(admission[key], False, key)
        for key in (
            "surface_standing_established",
            "surface_standing_renewed",
            "surface_standing_generalized",
            "standing_upgraded",
            "authority_transferred",
            "custody_transferred",
            "registry_created",
            "catalogue_created",
            "global_standing_ontology_created",
            "centralized_standing_vocabulary_allowlist_created",
            "execution_authorized",
            "global_reuse_permission_created",
            "continuation_authorized",
            "automatic_next_step_created",
        ):
            self.assertIs(result["non_claims"][key], False, key)

    def test_public_contract_and_exact_live_v2_carrier(self) -> None:
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
        )
        self.assertEqual(
            resolver.OUTCOMES,
            (
                "SELECTED_SURFACE_STANDING_BASIS_ADMITTED",
                "SELECTED_SURFACE_STANDING_BASIS_NOT_ADMITTED",
                "SELECTED_SURFACE_STANDING_BASIS_REQUIRES_ADDITIONAL_BASIS",
                "SELECTED_SURFACE_STANDING_BASIS_REVIEW_BLOCKED",
            ),
        )
        request = _request()
        self.assertEqual(
            set(request),
            {
                "boundary_identity",
                "selected_surface",
                "declared_matter_use",
                "source_applicability_result",
                "admission_level_binding",
                "declared_non_claims",
            },
        )
        with LIVE_APPLICABILITY_ARTIFACT.open(encoding="utf-8") as handle:
            live = json.load(handle)
        carrier = request["source_applicability_result"]
        for key, value in carrier.items():
            if key in {
                "applicability_artifact_reference",
                "applicability_check_posture",
            }:
                continue
            self.assertEqual(value, live[key], key)
        self.assertEqual(
            carrier["applicability_artifact_reference"],
            resolver.SOURCE_APPLICABILITY_ARTIFACT_REFERENCE,
        )
        self.assertEqual(
            carrier["applicability_check_posture"],
            {"passed_check_count": 22, "failed_check_count": 0},
        )
        self.assertEqual(len(live["checks"]), 22)
        self.assertTrue(all(check["passed"] is True for check in live["checks"]))
        self.assertEqual(len(carrier["source_family_non_claims"]), 68)
        self.assertEqual(len(carrier["non_claims"]), 41)

    def test_complete_pair_preserved_surface_is_admitted_for_exact_use(self) -> None:
        request = _request()
        result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            request
        )
        self.assert_terminal(result, resolver.OUTCOME_ADMITTED)
        surface = result["selected_surface"]
        self.assertEqual(surface["selected_surface_identity"], resolver.SOURCE_OPERATION_ID)
        self.assertEqual(surface["selected_surface_reference"], resolver.SOURCE_ARTIFACT_REFERENCE)
        self.assertEqual(
            surface["selected_surface_content_identity"],
            resolver.SOURCE_ARTIFACT_CONTENT_IDENTITY,
        )
        self.assertEqual(surface["source_family"], resolver.SOURCE_FAMILY)
        self.assertEqual(
            surface["source_family_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        self.assertTrue(surface["complete_pair_preserved"])
        self.assertEqual(
            surface["candidate_record_ids"],
            [resolver.CANDIDATE_A_RECORD_ID, resolver.CANDIDATE_B_RECORD_ID],
        )
        self.assertEqual(
            surface["candidate_basis_ids"],
            [resolver.CANDIDATE_A_BASIS_ID, resolver.CANDIDATE_B_BASIS_ID],
        )
        self.assertEqual(
            result["declared_matter_use"]["requested_standing_basis_use"],
            resolver.ADMISSIBLE_FUTURE_ROUTE,
        )
        self.assertTrue(result["admission"]["source_standing_created_upstream"])
        self.assertTrue(result["admission"]["source_applicability_recorded_upstream"])
        self.assertTrue(result["admission"]["selected_surface_standing_basis_admitted"])
        self.assert_no_local_power(result)

    def test_selected_surface_rejects_singletons_bases_reordering_and_substitution(self) -> None:
        base = _request()
        cases = {
            "candidate_a_only": (
                ("selected_surface", "candidate_record_ids"),
                [resolver.CANDIDATE_A_RECORD_ID],
            ),
            "candidate_b_only": (
                ("selected_surface", "candidate_record_ids"),
                [resolver.CANDIDATE_B_RECORD_ID],
            ),
            "basis_a_only": (
                ("selected_surface", "candidate_basis_ids"),
                [resolver.CANDIDATE_A_BASIS_ID],
            ),
            "basis_b_only": (
                ("selected_surface", "candidate_basis_ids"),
                [resolver.CANDIDATE_B_BASIS_ID],
            ),
            "pair_reordered": (
                ("selected_surface", "candidate_record_ids"),
                [resolver.CANDIDATE_B_RECORD_ID, resolver.CANDIDATE_A_RECORD_ID],
            ),
            "basis_reordered": (
                ("selected_surface", "candidate_basis_ids"),
                [resolver.CANDIDATE_B_BASIS_ID, resolver.CANDIDATE_A_BASIS_ID],
            ),
            "pair_not_preserved": (
                ("selected_surface", "complete_pair_preserved"),
                False,
            ),
            "candidate_a_reference": (
                ("selected_surface", "selected_surface_reference"),
                resolver.CANDIDATE_A_RECORD_ID,
            ),
            "candidate_b_reference": (
                ("selected_surface", "selected_surface_reference"),
                resolver.CANDIDATE_B_RECORD_ID,
            ),
            "basis_a_reference": (
                ("selected_surface", "selected_surface_reference"),
                resolver.CANDIDATE_A_BASIS_ID,
            ),
            "basis_b_reference": (
                ("selected_surface", "selected_surface_reference"),
                resolver.CANDIDATE_B_BASIS_ID,
            ),
            "applicability_as_surface": (
                ("selected_surface", "selected_surface_reference"),
                resolver.SOURCE_APPLICABILITY_ARTIFACT_REFERENCE,
            ),
        }
        for name, (path, value) in cases.items():
            with self.subTest(name=name):
                self.assert_blocked(
                    _change(base, path, value),
                    "SELECTED_SURFACE_MALFORMED",
                )

    def test_selected_surface_identity_missing_and_mismatch_are_distinct(self) -> None:
        base = _request()
        for field in (
            "selected_surface_identity",
            "selected_surface_reference",
            "selected_surface_content_identity",
            "selected_surface_type",
            "selected_surface_version",
            "selected_surface_scope",
            "source_family",
            "source_family_semantic_owner",
        ):
            with self.subTest(field=field, posture="missing"):
                self.assert_additional(
                    _change(base, ("selected_surface", field), DELETE),
                    "SELECTED_SURFACE_ADDITIONAL_BASIS_REQUIRED",
                )
            with self.subTest(field=field, posture="mismatch"):
                self.assert_blocked(
                    _change(base, ("selected_surface", field), "MISMATCH"),
                    "SELECTED_SURFACE_MALFORMED",
                )

    def test_source_identity_contract_effect_and_standing_facts_are_exact(self) -> None:
        base = _request()
        source_binding_fields = (
            "candidate_standing_operation_id",
            "candidate_standing_operation_type",
            "candidate_standing_operation_version",
            "candidate_standing_operation_scope",
            "source_artifact_reference",
            "source_artifact_content_identity",
            "source_standing_contract_reference",
            "source_standing_contract_version",
            "source_standing_contract_content_identity",
            "source_family",
            "source_family_semantic_owner",
            "source_outcome",
            "candidate_standing_result",
            "candidate_standing_supported",
            "candidate_standing_authorized",
            "candidate_standing_created",
            "candidate_a_standing_created",
            "candidate_b_standing_created",
            "basis_pair_scope",
            "source_passed_check_count",
            "source_failed_check_count",
        )
        for field in source_binding_fields:
            with self.subTest(field=field, posture="missing"):
                self.assert_additional(
                    _change(
                        base,
                        ("source_applicability_result", "source_binding", field),
                        DELETE,
                    ),
                    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
                )
            with self.subTest(field=field, posture="altered"):
                current = base["source_applicability_result"]["source_binding"][field]
                altered = not current if isinstance(current, bool) else "ALTERED"
                self.assert_blocked(
                    _change(
                        base,
                        ("source_applicability_result", "source_binding", field),
                        altered,
                    ),
                    "SOURCE_CONTRACT_OR_EFFECT_MISMATCH",
                )
        effect = base["source_applicability_result"]["standing_effect_locations"]
        self.assertGreater(len(effect), 1)
        self.assert_additional(
            _change(
                base,
                ("source_applicability_result", "standing_effect_locations"),
                effect[:-1],
            ),
            "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
        )
        self.assert_blocked(
            _change(
                base,
                ("source_applicability_result", "standing_effect_locations"),
                [*effect, "invented.effect"],
            ),
            "SOURCE_CONTRACT_OR_EFFECT_MISMATCH",
        )

    def test_complete_candidate_pair_material_and_evaluations_are_required(self) -> None:
        base = _request()
        pair_cases = (
            ("candidate_a_removed", ("candidate_pair", "candidate_a"), DELETE),
            ("candidate_b_removed", ("candidate_pair", "candidate_b"), DELETE),
            (
                "candidate_a_basis_removed",
                ("candidate_pair", "candidate_a", "candidate_basis_id"),
                DELETE,
            ),
            (
                "candidate_b_basis_removed",
                ("candidate_pair", "candidate_b", "candidate_basis_id"),
                DELETE,
            ),
            (
                "candidate_a_evaluation_removed",
                ("candidate_standing_operation_material", "candidate_a_standing_evaluation"),
                DELETE,
            ),
            (
                "candidate_b_evaluation_removed",
                ("candidate_standing_operation_material", "candidate_b_standing_evaluation"),
                DELETE,
            ),
            (
                "pair_evaluation_removed",
                ("candidate_standing_operation_material", "standing_pair_evaluation"),
                DELETE,
            ),
        )
        for name, suffix, value in pair_cases:
            with self.subTest(name=name):
                self.assert_blocked(
                    _change(base, ("source_applicability_result", *suffix), value),
                    "PAIR_DECOMPOSITION_OR_HIERARCHY",
                )

    def test_pair_locks_forbid_ranking_hierarchy_coupling_and_third_candidate(self) -> None:
        base = _request()
        evaluation = base["source_applicability_result"]["standing_pair_evaluation"]
        flips = {
            "candidate_records_remain_sibling": False,
            "candidate_record_non_hierarchy_preserved": False,
            "candidate_basis_non_hierarchy_preserved": False,
            "regulation_not_sovereign_over_motion": False,
            "motion_does_not_erase_regulation": False,
            "coupling_assigned": True,
            "coupling_created": True,
            "third_candidate_created": True,
            "third_model_admitted": True,
            "descendant_body_created": True,
            "relation_created": True,
            "presence_established": True,
            "identity_created": True,
            "follow_on_authorized": True,
        }
        self.assertTrue(set(flips).issubset(evaluation))
        for field, value in flips.items():
            with self.subTest(field=field):
                self.assert_blocked(
                    _change(
                        base,
                        ("source_applicability_result", "standing_pair_evaluation", field),
                        value,
                    ),
                    "PAIR_DECOMPOSITION_OR_HIERARCHY",
                )

    def test_cross_object_binding_preserves_pair_and_exact_binding(self) -> None:
        base = _request()
        cross = base["source_applicability_result"]["cross_object_binding"]
        for field in cross:
            with self.subTest(field=field, posture="missing"):
                expected_code = (
                    "PAIR_DECOMPOSITION_OR_HIERARCHY"
                    if field in {"candidate_record_ids", "candidate_basis_ids"}
                    else "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED"
                )
                assertion = (
                    self.assert_blocked
                    if expected_code == "PAIR_DECOMPOSITION_OR_HIERARCHY"
                    else self.assert_additional
                )
                value = [] if field in {"candidate_record_ids", "candidate_basis_ids"} else DELETE
                assertion(
                    _change(
                        base,
                        ("source_applicability_result", "cross_object_binding", field),
                        value,
                    ),
                    expected_code,
                )
        for field, value in (
            ("candidate_record_ids", [resolver.CANDIDATE_A_RECORD_ID]),
            ("candidate_record_ids", [resolver.CANDIDATE_B_RECORD_ID]),
            ("candidate_basis_ids", [resolver.CANDIDATE_A_BASIS_ID]),
            ("candidate_basis_ids", [resolver.CANDIDATE_B_BASIS_ID]),
            (
                "candidate_record_ids",
                [resolver.CANDIDATE_B_RECORD_ID, resolver.CANDIDATE_A_RECORD_ID],
            ),
        ):
            with self.subTest(field=field, value=value):
                self.assert_blocked(
                    _change(
                        base,
                        ("source_applicability_result", "cross_object_binding", field),
                        value,
                    ),
                    "PAIR_DECOMPOSITION_OR_HIERARCHY",
                )

    def test_lineage_custody_rank_and_scope_missing_vs_altered(self) -> None:
        base = _request()
        for section in ("source_lineage", "source_custody", "source_rank", "source_scope"):
            value = base["source_applicability_result"][section]
            if isinstance(value, list):
                missing = value[:-1]
                altered = [*value, "invented-lineage"]
            else:
                first = next(iter(value))
                missing = copy.deepcopy(value)
                del missing[first]
                altered = copy.deepcopy(value)
                altered[first] = not altered[first] if isinstance(altered[first], bool) else "ALTERED"
            with self.subTest(section=section, posture="missing"):
                self.assert_additional(
                    _change(base, ("source_applicability_result", section), missing),
                    "SOURCE_APPLICABILITY_ADDITIONAL_BASIS_REQUIRED",
                )
            with self.subTest(section=section, posture="altered"):
                self.assert_blocked(
                    _change(base, ("source_applicability_result", section), altered),
                    "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
                )
        self.assert_blocked(
            _change(
                base,
                ("source_applicability_result", "source_custody", "custody_transferred"),
                True,
            ),
            "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
        )
        self.assert_blocked(
            _change(
                base,
                ("source_applicability_result", "source_rank", "rank_upgraded"),
                True,
            ),
            "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
        )
        self.assert_blocked(
            _change(
                base,
                ("source_applicability_result", "source_scope", "admissible_future_route"),
                "WIDENED_ROUTE",
            ),
            "SOURCE_LINEAGE_CUSTODY_RANK_SCOPE_MISMATCH",
        )

    def test_complete_source_and_applicability_non_claims_are_canonical_false(self) -> None:
        base = _request()
        for section, missing_code, malformed_code in (
            (
                "source_family_non_claims",
                "SOURCE_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED",
                "SOURCE_NON_CLAIMS_MALFORMED",
            ),
            (
                "non_claims",
                "APPLICABILITY_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED",
                "APPLICABILITY_NON_CLAIMS_MALFORMED",
            ),
        ):
            claims = base["source_applicability_result"][section]
            self.assertTrue(all(value is False for value in claims.values()))
            for key in claims:
                with self.subTest(section=section, key=key, posture="missing"):
                    self.assert_additional(
                        _change(
                            base,
                            ("source_applicability_result", section, key),
                            DELETE,
                        ),
                        missing_code,
                    )
                with self.subTest(section=section, key=key, posture="true"):
                    self.assert_blocked(
                        _change(
                            base,
                            ("source_applicability_result", section, key),
                            True,
                        ),
                        malformed_code,
                    )

    def test_applicability_posture_cannot_create_standing_or_downstream_power(self) -> None:
        base = _request()
        applicability = base["source_applicability_result"]["applicability"]
        required = {
            "standing_created": False,
            "descendant_body_creation_authorized": False,
            "descendant_body_creation_executed": False,
            "correspondence_applicability_created": False,
            "selected_surface_standing_basis_admission_created": False,
            "downstream_authorization_created": False,
            "source_result_invalidated": False,
            "source_standing_revoked": False,
            "candidate_a_altered": False,
            "candidate_b_altered": False,
        }
        for field, expected in required.items():
            self.assertIs(applicability[field], expected)
            with self.subTest(field=field):
                self.assert_blocked(
                    _change(
                        base,
                        ("source_applicability_result", "applicability", field),
                        not expected,
                    ),
                    "SOURCE_APPLICABILITY_MALFORMED",
                )

    def test_source_applicability_outcomes_preserve_four_way_allocation(self) -> None:
        cases = (
            (
                resolver._source.OUTCOME_NOT_APPLICABLE,
                resolver.OUTCOME_NOT_ADMITTED,
                "SOURCE_APPLICABILITY_NOT_APPLICABLE",
            ),
            (
                resolver._source.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "SOURCE_APPLICABILITY_REQUIRES_ADDITIONAL_BASIS",
            ),
            (
                resolver._source.OUTCOME_REVIEW_BLOCKED,
                resolver.OUTCOME_REVIEW_BLOCKED,
                "SOURCE_APPLICABILITY_REVIEW_BLOCKED",
            ),
        )
        for source_outcome, target_outcome, code in cases:
            request = _request()
            request["source_applicability_result"]["outcome"] = source_outcome
            request["admission_level_binding"]["source_applicability_outcome"] = source_outcome
            with self.subTest(source_outcome=source_outcome):
                result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
                    request
                )
                self.assert_terminal(result, target_outcome, code)
                self.assertNotEqual(result["outcome"], resolver.OUTCOME_ADMITTED)

    def test_only_exact_source_owned_route_is_admitted(self) -> None:
        for declared_use in (
            "CORRESPONDENCE",
            "GENERIC_DESCENDANT_BODY_USE",
            "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY_PLUS_OTHER_USE",
            "DESCENDANT_BODY_CREATION_BOUNDARY",
            "ARBITRARY_STANDING_USE",
        ):
            with self.subTest(declared_use=declared_use):
                request = resolver.build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request(
                    declared_use
                )
                result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
                    request
                )
                self.assert_terminal(
                    result,
                    resolver.OUTCOME_NOT_ADMITTED,
                    "DECLARED_USE_NOT_APPLICABLE",
                )
        request = _request()
        request["declared_matter_use"]["use_class"] = "SEMANTIC_ALIAS"
        self.assert_blocked(request, "DECLARED_MATTER_USE_MALFORMED")

    def test_admission_local_declarations_and_binding_are_closed(self) -> None:
        base = _request()
        for section in resolver.REQUEST_KEYS:
            with self.subTest(section=section, posture="missing"):
                self.assert_additional(
                    _change(base, (section,), DELETE),
                    "REQUEST_FIELDS_INCOMPLETE",
                )
        unknown = copy.deepcopy(base)
        unknown["latest_surface"] = True
        self.assert_blocked(unknown, "REQUEST_KEYS_INVALID")
        for field in resolver.OUTSIDE_BOUNDARY_FIELDS:
            with self.subTest(outside_boundary=field):
                self.assert_blocked(
                    _change(
                        base,
                        ("declared_matter_use", "outside_boundary", field),
                        True,
                    ),
                    "DECLARED_MATTER_USE_MALFORMED",
                )
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(non_claim=key, posture="missing"):
                self.assert_additional(
                    _change(base, ("declared_non_claims", key), DELETE),
                    "ADMISSION_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED",
                )
            with self.subTest(non_claim=key, posture="true"):
                self.assert_blocked(
                    _change(base, ("declared_non_claims", key), True),
                    "ADMISSION_NON_CLAIMS_MALFORMED",
                )
        binding = base["admission_level_binding"]
        self.assertEqual(binding["declared_matter_use"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(binding["source_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertTrue(binding["complete_pair_preserved"])
        self.assertEqual(binding["source_lineage"], base["source_applicability_result"]["source_lineage"])
        self.assertEqual(binding["source_custody"], base["source_applicability_result"]["source_custody"])
        self.assertEqual(binding["source_rank"], base["source_applicability_result"]["source_rank"])
        self.assertEqual(binding["source_scope"], base["source_applicability_result"]["source_scope"])
        self.assert_additional(
            _change(base, ("admission_level_binding", "source_lineage"), DELETE),
            "ADMISSION_BINDING_ADDITIONAL_BASIS_REQUIRED",
        )
        self.assert_blocked(
            _change(
                base,
                ("admission_level_binding", "candidate_record_ids"),
                [resolver.CANDIDATE_A_RECORD_ID],
            ),
            "PAIR_DECOMPOSITION_OR_HIERARCHY",
        )
        self.assert_blocked(
            _change(
                base,
                ("admission_level_binding", "candidate_record_ids"),
                [resolver.CANDIDATE_B_RECORD_ID],
            ),
            "PAIR_DECOMPOSITION_OR_HIERARCHY",
        )
        self.assert_blocked(
            _change(
                base,
                ("admission_level_binding", "source_family_semantic_owner"),
                "GENERIC_ADMISSION_BOUNDARY",
            ),
            "ADMISSION_BINDING_MALFORMED",
        )

    def test_shortcuts_cannot_substitute_for_complete_source_owned_binding(self) -> None:
        shortcuts = (
            {"outcome": resolver.SOURCE_CANDIDATE_STANDING_RESULT},
            {"candidate_standing_supported": True},
            {"source_standing_preserved": True},
            {"source_artifact_reference": resolver.SOURCE_ARTIFACT_REFERENCE},
            {"repository_presence": True},
            {"latest_result": resolver.SOURCE_OPERATION_ID},
            {"timestamp": "latest"},
        )
        for shortcut in shortcuts:
            request = _request()
            request["source_applicability_result"] = shortcut
            with self.subTest(shortcut=shortcut):
                result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
                    request
                )
                self.assertNotEqual(result["outcome"], resolver.OUTCOME_ADMITTED)
                self.assertIn(
                    result["outcome"],
                    {
                        resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                        resolver.OUTCOME_REVIEW_BLOCKED,
                    },
                )

    def test_source_and_local_check_postures_remain_distinct(self) -> None:
        result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            _request()
        )
        carrier = result["source_applicability_result"]
        self.assertEqual(
            carrier["source_binding"]["source_passed_check_count"],
            resolver.SOURCE_PASSED_CHECK_COUNT,
        )
        self.assertEqual(
            carrier["source_binding"]["source_failed_check_count"],
            resolver.SOURCE_FAILED_CHECK_COUNT,
        )
        self.assertEqual(
            carrier["applicability_check_posture"],
            {"passed_check_count": 22, "failed_check_count": 0},
        )
        self.assertNotEqual(result["passed_check_count"], 176)
        self.assertNotEqual(result["passed_check_count"], 22)
        self.assertEqual(result["failed_check_count"], 0)

    def test_input_is_not_mutated_and_repeated_results_are_deterministic(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        first = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            request
        )
        second = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
            request
        )
        self.assertEqual(request, before)
        self.assertEqual(first, second)
        first["selected_surface"]["candidate_record_ids"].clear()
        self.assertEqual(request, before)

    def test_resolver_is_filesystem_hash_write_operation_and_adapter_free(self) -> None:
        source = inspect.getsource(resolver)
        for forbidden in (
            "open(",
            "Path(",
            "glob(",
            "rglob(",
            "hashlib",
            "sha256(",
            "json.dump",
            "write_text(",
            "write_bytes(",
            "resolve_descendant_body_candidate_standing_operation_v0_min(",
            "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2(",
        ):
            self.assertNotIn(forbidden, source)
        for forbidden_name in (
            "write_matter_bound_selected_surface_standing_basis_admission_v0_min_result",
            "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min_from_path",
            "OUTPUT_ROOT",
            "STANDING_REGISTRY",
            "STANDING_CATALOGUE",
            "STANDING_ONTOLOGY",
            "UNIVERSAL_STANDING_OUTCOME_ALLOWLIST",
        ):
            self.assertFalse(hasattr(resolver, forbidden_name), forbidden_name)
        with (
            mock.patch.object(builtins, "open", side_effect=AssertionError("filesystem access")),
            mock.patch.object(hashlib, "sha256", side_effect=AssertionError("runtime hashing")),
            mock.patch.object(
                resolver._source,
                "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2",
                side_effect=AssertionError("applicability invocation"),
            ),
        ):
            request = _request()
            result = resolver.resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(
                request
            )
        self.assert_terminal(result, resolver.OUTCOME_ADMITTED)
        self.assert_no_local_power(result)


if __name__ == "__main__":
    unittest.main()
