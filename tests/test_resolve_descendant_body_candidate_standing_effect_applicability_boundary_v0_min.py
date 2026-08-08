"""Adversarial tests for the pair-preserved standing-effect applicability boundary."""

from __future__ import annotations

import builtins
import copy
import hashlib
import inspect
import sys
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min as resolver


EXPECTED_SOURCE_NON_CLAIMS = frozenset(
    """
    action_authorized
    affected_file_deleted
    affected_file_edited
    affected_file_overwritten
    affected_file_redeemed
    affected_file_repaired
    affected_file_replaced
    affected_file_treated_as_clean_basis
    api_created
    authority_created
    candidate_standing_boundary_bypassed
    candidate_standing_boundary_overridden
    contaminated_lineage_treated_as_clean_basis
    coupling_assigned_to_candidate_a
    coupling_assigned_to_candidate_b
    coupling_created
    crossing_authorized
    currentness_created
    derivative_reception_authorized
    descendant_body_a_created
    descendant_body_b_created
    descendant_body_created
    descendant_standing_check_performed
    direct_boundary_allowance_to_candidate_standing_without_operation
    direct_candidate_standing_operation_spec_to_candidate_standing_operation_completion
    direct_candidate_standing_to_authority_currentness
    direct_candidate_standing_to_coupling_creation
    direct_candidate_standing_to_crossing
    direct_candidate_standing_to_descendant_body_creation
    direct_candidate_standing_to_descendant_standing
    direct_candidate_standing_to_follow_on_work
    direct_candidate_standing_to_identity
    direct_candidate_standing_to_output_action
    direct_candidate_standing_to_presence
    direct_candidate_standing_to_relation
    direct_candidate_standing_to_runtime
    direct_candidate_standing_to_standing_descendant
    direct_candidate_standing_to_third_candidate_route
    direct_candidate_standing_to_third_model_route
    direct_supported_distinctness_to_candidate_standing_without_boundary_and_operation
    distinctness_support_recheck_operation_bypassed
    distinctness_support_recheck_operation_overridden
    field_machinery_created
    file_discovery_performed
    first_crossing_authorized
    follow_on_authorized
    follow_on_work_authorized
    hidden_repair_performed
    identity_created
    output_authorized
    presence_established
    prior_unsupported_candidate_a_claim_validated
    prior_unsupported_candidate_b_claim_validated
    prior_unsupported_derivation_event_claim_validated
    relation_created
    repair_performed
    repository_scan_performed
    runtime_created
    scan_performed
    silent_overwrite_performed
    standing_authorized
    standing_created
    standing_descendant_created
    synchronization_authorized
    third_candidate_created
    third_model_admitted
    valid_derivation_event_recorded
    validation_enforced
    """.split()
)

EXPECTED_BOUNDARY_NON_CLAIMS = frozenset(
    """
    standing_created
    standing_renewed
    standing_extended
    standing_reinterpreted
    standing_transferred
    standing_generalized
    candidate_a_independent_standing_created
    candidate_b_independent_standing_created
    candidate_pair_split
    candidate_pair_ranked
    candidate_a_ranked_over_candidate_b
    candidate_b_ranked_over_candidate_a
    source_family_semantics_overridden
    semantic_ownership_transferred
    global_standing_vocabulary_created
    cross_family_standing_allowlist_created
    correspondence_applicability_created
    selected_surface_standing_basis_admission_created
    downstream_authorization_created
    operation_created
    execution_permission_created
    runtime_created
    deployment_created
    adoption_created
    integration_created
    continuation_permission_created
    reuse_permission_created
    follow_on_permission_created
    automatic_successor_created
    custody_transferred
    rank_upgraded
    source_route_widened
    descendant_body_creation_authorized
    descendant_body_creation_executed
    generic_cross_family_standing_adapter_created
    registry_created
    catalogue_created
    ontology_created
    repository_presence_treated_as_applicability_basis
    recency_inference_used
    follow_on_work_authorized
    """.split()
)


def _request(use: str = resolver.ADMISSIBLE_FUTURE_ROUTE) -> dict[str, object]:
    return resolver.build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_request(
        use
    )


def _resolve(request: object) -> dict[str, object]:
    return resolver.resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min(
        request
    )


class DescendantBodyCandidateStandingEffectApplicabilityBoundaryV0MinTests(
    unittest.TestCase
):
    def assertCanonicalNonClaims(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertEqual(EXPECTED_BOUNDARY_NON_CLAIMS, frozenset(non_claims))
        self.assertTrue(all(value is False for value in non_claims.values()))
        source_non_claims = result["source_family_non_claims"]
        self.assertEqual(EXPECTED_SOURCE_NON_CLAIMS, frozenset(source_non_claims))
        self.assertEqual(68, len(source_non_claims))
        self.assertTrue(all(value is False for value in source_non_claims.values()))

    def assertRecorded(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_RECORDED, result["outcome"])
        self.assertIs(result["block"]["blocked"], False)
        self.assertIs(result["applicability"]["lawful_terminal_outcome_recorded"], True)
        self.assertCanonicalNonClaims(result)

    def assertNotApplicable(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_NOT_APPLICABLE, result["outcome"])
        self.assertIs(result["block"]["blocked"], False)
        self.assertIs(result["applicability"]["lawful_terminal_outcome_recorded"], True)
        self.assertCanonicalNonClaims(result)

    def assertAdditional(self, result: dict[str, object]) -> None:
        self.assertEqual(
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS, result["outcome"]
        )
        self.assertIs(result["block"]["blocked"], False)
        self.assertCanonicalNonClaims(result)

    def assertBlocked(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_REVIEW_BLOCKED, result["outcome"])
        self.assertIs(result["block"]["blocked"], True)
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        self.assertCanonicalNonClaims(result)

    def test_public_constants_and_canonical_fixture_match_exact_source(self) -> None:
        self.assertEqual("0.1.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "descendant_body_candidate_standing_effect_applicability_boundary_001",
            resolver.BOUNDARY_ID,
        )
        self.assertEqual(
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY",
            resolver.BOUNDARY_TYPE,
        )
        self.assertEqual(
            "ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_"
            "ONE_EXACT_DECLARED_DOWNSTREAM_USE_ONLY",
            resolver.BOUNDARY_SCOPE,
        )
        self.assertEqual(
            {
                resolver.OUTCOME_RECORDED,
                resolver.OUTCOME_NOT_APPLICABLE,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_REVIEW_BLOCKED,
            },
            set(resolver.OUTCOMES),
        )
        self.assertEqual(EXPECTED_SOURCE_NON_CLAIMS, frozenset(resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS))
        self.assertEqual(EXPECTED_BOUNDARY_NON_CLAIMS, frozenset(resolver.REQUIRED_FALSE_NON_CLAIMS))

        request = _request()
        self.assertEqual(
            "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3",
            request["source_standing_contract"]["source_standing_contract_content_identity"],
        )
        self.assertEqual(
            "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961",
            request["source_artifact"]["source_artifact_content_identity"],
        )
        self.assertEqual(0, request["source_artifact"]["source_failed_check_count"])
        self.assertEqual(176, request["source_artifact"]["source_passed_check_count"])
        self.assertEqual("CANDIDATE_STANDING_SUPPORTED", request["source_operation"]["candidate_standing_result"])
        self.assertIs(request["source_operation"]["candidate_standing_created"], True)
        self.assertEqual(
            {
                "candidate_a_standing_evaluation",
                "candidate_b_standing_evaluation",
                "standing_pair_evaluation",
            },
            set(request["candidate_standing_operation_material"]),
        )

    def test_exact_pair_and_route_record_positive_applicability_only(self) -> None:
        result = _resolve(_request())
        self.assertRecorded(result)
        source = result["source_binding"]
        applicability = result["applicability"]
        self.assertIs(source["source_standing_created"], True)
        self.assertIs(source["complete_pair_preserved"], True)
        self.assertEqual(resolver.CANDIDATE_A_RECORD_ID, source["candidate_a_record_id"])
        self.assertEqual(resolver.CANDIDATE_B_RECORD_ID, source["candidate_b_record_id"])
        self.assertIs(applicability["standing_created"], False)
        self.assertIs(applicability["candidate_standing_effect_applicability_recorded"], True)
        self.assertIs(applicability["candidate_standing_effect_applicable_to_declared_use"], True)
        self.assertIs(applicability["declared_use_exactly_matches_source_route"], True)
        for key in (
            "source_family_semantic_ownership_preserved",
            "source_custody_preserved",
            "source_rank_preserved",
            "source_lineage_preserved",
        ):
            target = source if key != "source_family_semantic_ownership_preserved" else applicability
            self.assertIs(target[key], True, key)
        for key in (
            "descendant_body_creation_authorized",
            "descendant_body_creation_executed",
            "correspondence_applicability_created",
            "selected_surface_standing_basis_admission_created",
            "downstream_authorization_created",
        ):
            self.assertIs(applicability[key], False, key)

    def test_complete_nonmatching_routes_are_lawful_not_applicable(self) -> None:
        uses = (
            "correspondence",
            "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION",
            "ARBITRARY_COMPLETE_ROUTE",
            "DESCENDANT_BODY_CREATION_BOUNDARY",
            resolver.ADMISSIBLE_FUTURE_ROUTE + "_PLUS_ANOTHER_USE",
        )
        for use in uses:
            with self.subTest(use=use):
                result = _resolve(_request(use))
                self.assertNotApplicable(result)
                source = result["source_binding"]
                applicability = result["applicability"]
                self.assertIs(source["source_standing_created"], True)
                self.assertIs(source["complete_pair_preserved"], True)
                self.assertIs(applicability["source_standing_revoked"], False)
                self.assertIs(applicability["source_result_invalidated"], False)
                self.assertIs(applicability["candidate_a_altered"], False)
                self.assertIs(applicability["candidate_b_altered"], False)
                self.assertIs(applicability["standing_created"], False)
                self.assertIs(applicability["candidate_standing_effect_applicability_recorded"], False)

    def test_source_family_contract_effect_and_artifact_fail_closed(self) -> None:
        missing_cases = (
            ("source_family", None),
            ("source_family_semantic_owner", None),
            ("source_standing_contract", "source_standing_contract_identity"),
            ("source_standing_contract", "source_standing_contract_reference"),
            ("source_artifact", "source_artifact_reference"),
        )
        for section, key in missing_cases:
            with self.subTest(missing=(section, key)):
                request = _request()
                if key is None:
                    del request[section]
                else:
                    del request[section][key]
                self.assertAdditional(_resolve(request))

        mismatch_cases = (
            ("source_family", None, "OTHER_FAMILY"),
            ("source_family_semantic_owner", None, "CALLER"),
            ("source_standing_contract", "source_standing_contract_reference", "spec/other.md"),
            ("source_standing_contract", "source_standing_contract_content_identity", "0" * 64),
            ("source_artifact", "source_artifact_content_identity", "1" * 64),
            ("source_artifact", "source_outcome", "OTHER_OUTCOME"),
            ("source_artifact", "source_failed_check_count", 1),
            ("source_artifact", "source_passed_check_count", 175),
        )
        for section, key, value in mismatch_cases:
            with self.subTest(mismatch=(section, key)):
                request = _request()
                if key is None:
                    request[section] = value
                else:
                    request[section][key] = value
                self.assertBlocked(_resolve(request))

        missing_location = _request()
        missing_location["standing_effect_locations"].pop()
        self.assertAdditional(_resolve(missing_location))
        changed_location = _request()
        changed_location["standing_effect_locations"][0] = "caller.effect"
        self.assertBlocked(_resolve(changed_location))

    def test_source_operation_fields_are_exact_and_boolean_types_are_strict(self) -> None:
        mutations = (
            ("candidate_standing_operation_id", "other-operation"),
            ("candidate_standing_operation_type", "OTHER_TYPE"),
            ("candidate_standing_operation_version", "9.0.0"),
            ("candidate_standing_operation_scope", "WIDER_SCOPE"),
            ("candidate_standing_result", "OTHER_RESULT"),
            ("candidate_standing_supported", False),
            ("candidate_standing_authorized", False),
            ("candidate_standing_created", False),
            ("candidate_standing_created", 1),
            ("candidate_a_standing_created", False),
            ("candidate_b_standing_created", False),
            ("basis_pair_scope", "SINGLETON_SCOPE"),
            ("admissible_future_route", "WIDENED_ROUTE"),
        )
        for key, value in mutations:
            with self.subTest(field=key, value=value):
                request = _request()
                request["source_operation"][key] = value
                self.assertBlocked(_resolve(request))

    def test_candidate_pair_cannot_be_split_swapped_ranked_or_reused(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for member in ("candidate_a", "candidate_b"):
            request = _request()
            del request["candidate_pair"][member]
            cases.append((f"missing_{member}", request))
        for member in ("candidate_a", "candidate_b"):
            request = _request()
            del request["candidate_pair"][member]["candidate_basis_id"]
            cases.append((f"missing_{member}_basis", request))
        swapped_ids = _request()
        swapped_ids["candidate_pair"]["candidate_a"]["candidate_record_id"] = resolver.CANDIDATE_B_RECORD_ID
        swapped_ids["candidate_pair"]["candidate_b"]["candidate_record_id"] = resolver.CANDIDATE_A_RECORD_ID
        cases.append(("swapped_ids", swapped_ids))
        swapped_roles = _request()
        swapped_roles["candidate_pair"]["candidate_a"]["candidate_role"] = resolver.CANDIDATE_B_ROLE
        swapped_roles["candidate_pair"]["candidate_b"]["candidate_role"] = resolver.CANDIDATE_A_ROLE
        cases.append(("swapped_roles", swapped_roles))
        for member in ("candidate_a", "candidate_b"):
            request = _request()
            request["candidate_pair"][member]["candidate_standing_created"] = False
            cases.append((f"{member}_standing_false", request))
        for label, request in cases:
            with self.subTest(case=label):
                self.assertBlocked(_resolve(request))

        overreach_fields = (
            "candidate_pair_split_requested",
            "candidate_pair_ranking_requested",
            "candidate_singleton_reuse_requested",
        )
        for field in overreach_fields:
            with self.subTest(overreach=field):
                request = _request()
                request["no_standing_change_declaration"][field] = True
                self.assertBlocked(_resolve(request))

    def test_complete_source_material_and_every_pair_lock_are_exact(self) -> None:
        missing = _request()
        del missing["candidate_standing_operation_material"]
        self.assertBlocked(_resolve(missing))
        for section in (
            "candidate_a_standing_evaluation",
            "candidate_b_standing_evaluation",
            "standing_pair_evaluation",
        ):
            with self.subTest(missing_material=section):
                request = _request()
                del request["candidate_standing_operation_material"][section]
                self.assertBlocked(_resolve(request))

        pair_mutations = (
            ("both_candidate_standings_supported", False),
            ("both_candidate_standings_authorized", False),
            ("both_candidate_standings_created", False),
            ("candidate_records_remain_sibling", False),
            ("candidate_record_non_hierarchy_preserved", False),
            ("candidate_basis_non_hierarchy_preserved", False),
            ("regulation_not_sovereign_over_motion", False),
            ("motion_does_not_erase_regulation", False),
            ("coupling_assigned", True),
            ("coupling_created", True),
            ("third_candidate_created", True),
            ("third_model_admitted", True),
            ("descendant_body_created", True),
            ("relation_created", True),
            ("presence_established", True),
            ("identity_created", True),
            ("follow_on_authorized", True),
        )
        for key, value in pair_mutations:
            with self.subTest(pair_lock=key):
                request = _request()
                request["candidate_standing_operation_material"]["standing_pair_evaluation"][key] = value
                self.assertBlocked(_resolve(request))

        for section in ("candidate_a_standing_evaluation", "candidate_b_standing_evaluation"):
            for key, value in (
                ("candidate_basis_separate", False),
                ("candidate_standing_supported", False),
                ("candidate_standing_authorized", False),
                ("candidate_standing_created", False),
                ("descendant_body_created", True),
                ("relation_created", True),
                ("presence_established", True),
                ("identity_created", True),
            ):
                with self.subTest(section=section, field=key):
                    request = _request()
                    request["candidate_standing_operation_material"][section][key] = value
                    self.assertBlocked(_resolve(request))

    def test_source_non_claims_require_exact_68_false_fields(self) -> None:
        self.assertEqual(68, len(resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS))
        missing = _request()
        del missing["source_family_non_claims"][resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS[0]]
        self.assertAdditional(_resolve(missing))
        extra = _request()
        extra["source_family_non_claims"]["invented_non_claim"] = False
        self.assertBlocked(_resolve(extra))
        for key in resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(key=key):
                request = _request()
                request["source_family_non_claims"][key] = True
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["source_family_non_claims"][key], False)

    def test_lineage_custody_rank_scope_and_route_are_supplied_not_inferred(self) -> None:
        for section in ("source_lineage", "source_custody", "source_rank", "source_scope"):
            with self.subTest(missing=section):
                request = _request()
                del request[section]
                self.assertAdditional(_resolve(request))

        incomplete_lineage = _request()
        incomplete_lineage["source_lineage"].pop()
        self.assertAdditional(_resolve(incomplete_lineage))
        wrong_lineage = _request()
        wrong_lineage["source_lineage"][0] = "spec/other.md"
        self.assertBlocked(_resolve(wrong_lineage))

        mutations = (
            ("source_custody", "custody_transferred", True),
            ("source_custody", "source_artifact_content_identity", "2" * 64),
            ("source_rank", "rank_upgraded", True),
            ("source_rank", "candidate_record_non_hierarchy_preserved", False),
            ("source_scope", "admissible_future_route", "WIDER_ROUTE"),
            ("source_scope", "basis_pair_scope", "SINGLETON_SCOPE"),
        )
        for section, key, value in mutations:
            with self.subTest(section=section, key=key):
                request = _request()
                request[section][key] = value
                self.assertBlocked(_resolve(request))

        missing_route = _request()
        del missing_route["admissible_future_route"]
        self.assertAdditional(_resolve(missing_route))
        changed_route = _request()
        changed_route["admissible_future_route"] = "WIDENED_ROUTE"
        self.assertBlocked(_resolve(changed_route))

    def test_declared_use_requires_literal_equality_not_alias_or_assertion(self) -> None:
        missing = _request()
        del missing["declared_downstream_matter_use"]
        self.assertAdditional(_resolve(missing))
        multiple = _request()
        multiple["declared_downstream_matter_use"] = [
            resolver.ADMISSIBLE_FUTURE_ROUTE,
            "correspondence",
        ]
        self.assertBlocked(_resolve(multiple))

        alias = _request("DESCENDANT_BODY_CREATION_BOUNDARY_ONLY")
        self.assertNotApplicable(_resolve(alias))
        asserted_equivalence = _request("correspondence")
        asserted_equivalence["declared_use_exactly_matches_source_route"] = True
        self.assertBlocked(_resolve(asserted_equivalence))
        naked_boolean = _request()
        del naked_boolean["admissible_future_route"]
        naked_boolean["applicability"] = True
        self.assertBlocked(_resolve(naked_boolean))

    def test_cross_object_binding_cannot_be_missing_contradictory_or_pair_selective(self) -> None:
        missing = _request()
        del missing["cross_object_binding"]
        self.assertAdditional(_resolve(missing))
        incomplete = _request()
        del incomplete["cross_object_binding"]["source_rank"]
        self.assertAdditional(_resolve(incomplete))

        contradictions = (
            ("source_family", "OTHER_FAMILY"),
            ("source_artifact_reference", "latest.json"),
            ("admissible_future_route", "WIDER_ROUTE"),
            ("declared_downstream_matter_use", "correspondence"),
            ("complete_pair_preserved", False),
        )
        for key, value in contradictions:
            with self.subTest(binding=key):
                request = _request()
                request["cross_object_binding"][key] = value
                self.assertBlocked(_resolve(request))

        pair_cases = (
            [resolver.CANDIDATE_A_RECORD_ID],
            [resolver.CANDIDATE_B_RECORD_ID],
            [resolver.CANDIDATE_B_RECORD_ID, resolver.CANDIDATE_A_RECORD_ID],
        )
        for ids in pair_cases:
            with self.subTest(candidate_ids=ids):
                request = _request()
                request["cross_object_binding"]["candidate_record_ids"] = ids
                self.assertBlocked(_resolve(request))
        basis_cases = (
            [resolver.CANDIDATE_A_BASIS_ID],
            [resolver.CANDIDATE_B_BASIS_ID],
            [resolver.CANDIDATE_B_BASIS_ID, resolver.CANDIDATE_A_BASIS_ID],
        )
        for ids in basis_cases:
            with self.subTest(basis_ids=ids):
                request = _request()
                request["cross_object_binding"]["candidate_basis_ids"] = ids
                self.assertBlocked(_resolve(request))

    def test_all_explicit_standing_and_downstream_overreach_blocks(self) -> None:
        for field in resolver.NO_STANDING_CHANGE_FIELDS:
            with self.subTest(field=field):
                request = _request()
                request["no_standing_change_declaration"][field] = True
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["non_claims"]["standing_created"], False)
                self.assertIs(result["non_claims"]["downstream_authorization_created"], False)

    def test_every_boundary_non_claim_is_required_and_canonicalized_false(self) -> None:
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(key=key, posture="true"):
                request = _request()
                request["declared_non_claims"][key] = True
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["non_claims"][key], False)
            with self.subTest(key=key, posture="missing"):
                request = _request()
                del request["declared_non_claims"][key]
                result = _resolve(request)
                self.assertAdditional(result)
                self.assertIs(result["non_claims"][key], False)

    def test_all_four_outcomes_are_lawful_public_and_canonical(self) -> None:
        recorded = _resolve(_request())
        not_applicable = _resolve(_request("correspondence"))
        additional_request = _request()
        del additional_request["source_lineage"]
        additional = _resolve(additional_request)
        blocked = _resolve(None)
        results = (recorded, not_applicable, additional, blocked)
        self.assertEqual(set(resolver.OUTCOMES), {item["outcome"] for item in results})
        for result in results:
            self.assertIs(result["boundary"]["review_exhausted"], True)
            self.assertIs(result["applicability"]["lawful_terminal_outcome_recorded"], True)
            self.assertCanonicalNonClaims(result)
            for check in result["checks"]:
                code = check["failure_code"]
                if code is not None:
                    self.assertIn(code, resolver.STOP_CODES)
                block_code = check["block_code"]
                if block_code is not None:
                    self.assertIn(block_code, resolver.BLOCK_CODES)

    def test_resolution_is_deterministic_stateless_and_non_mutating(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(first, second)
        self.assertEqual(before, request)
        first["non_claims"]["standing_created"] = True
        first["source_binding"]["candidate_a_record_id"] = "changed-output"
        third = _resolve(request)
        self.assertEqual(second, third)
        self.assertIs(third["non_claims"]["standing_created"], False)
        self.assertEqual(resolver.CANDIDATE_A_RECORD_ID, third["source_binding"]["candidate_a_record_id"])
        for key in (
            "reuse_permission_created",
            "continuation_permission_created",
            "automatic_successor_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(third["non_claims"][key], False)

    def test_resolver_has_no_filesystem_hashing_persistence_operation_or_generic_machinery(self) -> None:
        source = inspect.getsource(resolver)
        for forbidden_import in (
            "import os",
            "import pathlib",
            "from pathlib",
            "import json",
            "import hashlib",
            "import subprocess",
            "import glob",
            "import datetime",
        ):
            self.assertNotIn(forbidden_import, source)
        for forbidden_name in (
            "resolve_from_path",
            "write_result",
            "OUTPUT_ROOT",
            "GLOBAL_STANDING_VOCABULARY",
            "GLOBAL_OUTCOME_ALLOWLIST",
            "STANDING_REGISTRY",
            "STANDING_CATALOGUE",
            "STANDING_ONTOLOGY",
            "CROSS_FAMILY_STANDING_ADAPTER",
        ):
            self.assertFalse(hasattr(resolver, forbidden_name))

        request = _request()
        with mock.patch.object(
            builtins, "open", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "open", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "read_text", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "write_text", side_effect=AssertionError("filesystem access")
        ), mock.patch.object(
            Path, "glob", side_effect=AssertionError("repository discovery")
        ), mock.patch.object(
            Path, "rglob", side_effect=AssertionError("repository discovery")
        ), mock.patch.object(
            hashlib, "sha256", side_effect=AssertionError("hashing")
        ):
            result = _resolve(request)
        self.assertRecorded(result)
        for key in (
            "operation_created",
            "runtime_created",
            "standing_created",
            "standing_renewed",
            "standing_extended",
            "standing_transferred",
            "standing_generalized",
            "registry_created",
            "catalogue_created",
            "ontology_created",
            "generic_cross_family_standing_adapter_created",
        ):
            self.assertIs(result["non_claims"][key], False)


if __name__ == "__main__":
    unittest.main()
