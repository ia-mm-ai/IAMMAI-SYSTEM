"""Tests for the additive v2 standing-effect applicability result envelope.

V1 remains preserved implementation lineage. This suite independently proves
that the unchanged boundary decision law now emits the exact source-owned
structures required by Section 12, without creating or reinterpreting standing.
"""

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

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2 as resolver


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

MANDATORY_EXACT_RESULT_KEYS = frozenset(
    {
        "standing_effect_locations",
        "source_operation",
        "candidate_pair",
        "candidate_standing_operation_material",
        "standing_pair_evaluation",
        "cross_object_binding",
        "source_lineage",
        "source_custody",
        "source_rank",
        "source_scope",
    }
)


def _request(use: str = resolver.ADMISSIBLE_FUTURE_ROUTE) -> dict[str, object]:
    return resolver.build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_request(
        use
    )


def _resolve(request: object) -> dict[str, object]:
    return resolver.resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2(
        request
    )


class DescendantBodyCandidateStandingEffectApplicabilityBoundaryV0MinV2Tests(
    unittest.TestCase
):
    def assertCanonicalNonClaims(self, result: dict[str, object]) -> None:
        source_non_claims = result["source_family_non_claims"]
        self.assertEqual(EXPECTED_SOURCE_NON_CLAIMS, frozenset(source_non_claims))
        self.assertEqual(68, len(source_non_claims))
        self.assertTrue(all(value is False for value in source_non_claims.values()))

        non_claims = result["non_claims"]
        self.assertEqual(EXPECTED_BOUNDARY_NON_CLAIMS, frozenset(non_claims))
        self.assertEqual(41, len(non_claims))
        self.assertTrue(all(value is False for value in non_claims.values()))

    def assertRecorded(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_RECORDED, result["outcome"])
        self.assertIs(result["block"]["blocked"], False)
        self.assertIs(result["boundary"]["review_exhausted"], True)
        self.assertIs(
            result["applicability"]["lawful_terminal_outcome_recorded"], True
        )
        self.assertCanonicalNonClaims(result)

    def assertNotApplicable(self, result: dict[str, object]) -> None:
        self.assertEqual(resolver.OUTCOME_NOT_APPLICABLE, result["outcome"])
        self.assertIs(result["block"]["blocked"], False)
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

    def assertSection12Result(
        self, result: dict[str, object], request: dict[str, object]
    ) -> None:
        self.assertTrue(MANDATORY_EXACT_RESULT_KEYS.issubset(result))
        source = result["source_binding"]
        contract = request["source_standing_contract"]
        artifact = request["source_artifact"]
        operation = request["source_operation"]
        pair = request["candidate_pair"]
        material = request["candidate_standing_operation_material"]

        self.assertEqual(
            contract["source_standing_contract_version"],
            source["source_standing_contract_version"],
        )
        self.assertEqual(
            contract["source_standing_contract_content_identity"],
            source["source_standing_contract_content_identity"],
        )
        self.assertEqual(
            request["standing_effect_locations"], result["standing_effect_locations"]
        )

        self.assertEqual(operation, result["source_operation"])
        for key in (
            "candidate_standing_operation_type",
            "candidate_standing_operation_version",
            "candidate_standing_operation_scope",
            "candidate_standing_supported",
            "candidate_standing_authorized",
            "candidate_standing_created",
            "candidate_a_standing_created",
            "candidate_b_standing_created",
            "basis_pair_scope",
        ):
            self.assertEqual(operation[key], source[key], key)

        self.assertEqual(artifact["source_outcome"], source["source_outcome"])
        self.assertEqual(
            artifact["source_failed_check_count"], source["source_failed_check_count"]
        )
        self.assertEqual(
            artifact["source_passed_check_count"], source["source_passed_check_count"]
        )
        self.assertEqual(0, source["source_failed_check_count"])
        self.assertEqual(176, source["source_passed_check_count"])
        local_passed = sum(check["passed"] is True for check in result["checks"])
        local_failed = sum(check["passed"] is False for check in result["checks"])
        self.assertNotEqual(source["source_passed_check_count"], local_passed)
        self.assertNotEqual(
            (source["source_passed_check_count"], source["source_failed_check_count"]),
            (local_passed, local_failed),
        )

        self.assertEqual(pair, result["candidate_pair"])
        self.assertEqual(
            pair["candidate_a"]["candidate_role"], source["candidate_a_role"]
        )
        self.assertEqual(
            pair["candidate_a"]["candidate_basis_label"],
            source["candidate_a_basis_label"],
        )
        self.assertEqual(
            pair["candidate_b"]["candidate_role"], source["candidate_b_role"]
        )
        self.assertEqual(
            pair["candidate_b"]["candidate_basis_label"],
            source["candidate_b_basis_label"],
        )

        self.assertEqual(material, result["candidate_standing_operation_material"])
        self.assertEqual(
            material["candidate_a_standing_evaluation"],
            result["candidate_standing_operation_material"][
                "candidate_a_standing_evaluation"
            ],
        )
        self.assertEqual(
            material["candidate_b_standing_evaluation"],
            result["candidate_standing_operation_material"][
                "candidate_b_standing_evaluation"
            ],
        )
        self.assertEqual(
            material["standing_pair_evaluation"], result["standing_pair_evaluation"]
        )

        standing_pair = result["standing_pair_evaluation"]
        for key in (
            "both_candidate_standings_supported",
            "both_candidate_standings_authorized",
            "both_candidate_standings_created",
            "candidate_standing_evaluated",
            "candidate_records_remain_sibling",
            "candidate_record_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
            "regulation_not_sovereign_over_motion",
            "motion_does_not_erase_regulation",
        ):
            self.assertIs(standing_pair[key], True, key)
        for key in (
            "coupling_assigned",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "descendant_body_created",
            "relation_created",
            "presence_established",
            "identity_created",
            "follow_on_authorized",
        ):
            self.assertIs(standing_pair[key], False, key)

        for key in (
            "cross_object_binding",
            "source_lineage",
            "source_custody",
            "source_rank",
            "source_scope",
        ):
            self.assertEqual(request[key], result[key], key)

        self.assertIs(source["source_standing_created"], True)
        self.assertIs(source["candidate_standing_created"], True)
        self.assertIs(result["applicability"]["standing_created"], False)
        self.assertIs(source["complete_pair_preserved"], True)
        self.assertIs(source["source_custody_preserved"], True)
        self.assertIs(source["source_rank_preserved"], True)
        self.assertIs(source["source_lineage_preserved"], True)
        self.assertIs(
            result["source_custody"]["source_custody_preserved"], True
        )
        self.assertIs(result["source_rank"]["rank_upgraded"], False)
        self.assertEqual(
            result["source_scope"]["admissible_future_route"],
            result["applicability"]["admissible_future_route"],
        )

    def test_public_constants_and_canonical_source_envelope(self) -> None:
        self.assertEqual("0.2.0", resolver.RESULT_VERSION)
        self.assertEqual(
            "resolve_descendant_body_candidate_standing_effect_applicability_"
            "boundary_v0_min_v2",
            resolver.RESOLVER_MODULE,
        )
        self.assertEqual("0.1.0", resolver.BOUNDARY_VERSION)
        self.assertEqual(
            "descendant_body_candidate_standing_effect_applicability_boundary_001",
            resolver.BOUNDARY_ID,
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
        self.assertEqual(
            EXPECTED_SOURCE_NON_CLAIMS,
            frozenset(resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS),
        )
        self.assertEqual(
            EXPECTED_BOUNDARY_NON_CLAIMS,
            frozenset(resolver.REQUIRED_FALSE_NON_CLAIMS),
        )

        request = _request()
        self.assertEqual(
            "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3",
            request["source_standing_contract"][
                "source_standing_contract_content_identity"
            ],
        )
        self.assertEqual(176, request["source_artifact"]["source_passed_check_count"])
        self.assertEqual(0, request["source_artifact"]["source_failed_check_count"])
        self.assertEqual(
            {
                "candidate_a_standing_evaluation",
                "candidate_b_standing_evaluation",
                "standing_pair_evaluation",
            },
            set(request["candidate_standing_operation_material"]),
        )

    def test_positive_result_preserves_complete_section_12_envelope(self) -> None:
        request = _request()
        result = _resolve(request)
        self.assertRecorded(result)
        self.assertEqual("0.2.0", result["result_version"])
        self.assertEqual(resolver.RESOLVER_MODULE, result["resolver_module"])
        self.assertEqual("0.1.0", result["boundary"][
            "descendant_body_candidate_standing_effect_applicability_boundary_version"
        ])
        self.assertSection12Result(result, request)
        self.assertEqual(22, sum(check["passed"] is True for check in result["checks"]))
        self.assertEqual(0, sum(check["passed"] is False for check in result["checks"]))

        applicability = result["applicability"]
        self.assertIs(
            applicability["candidate_standing_effect_applicability_recorded"], True
        )
        self.assertIs(
            applicability["candidate_standing_effect_applicable_to_declared_use"],
            True,
        )
        self.assertIs(applicability["declared_use_exactly_matches_source_route"], True)
        self.assertIs(applicability["source_family_semantic_ownership_preserved"], True)
        for key in (
            "descendant_body_creation_authorized",
            "descendant_body_creation_executed",
            "correspondence_applicability_created",
            "selected_surface_standing_basis_admission_created",
            "downstream_authorization_created",
        ):
            self.assertIs(applicability[key], False, key)

    def test_complete_nonmatching_uses_preserve_source_and_are_not_applicable(self) -> None:
        for use in (
            "correspondence",
            "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION",
            "ARBITRARY_COMPLETE_ROUTE",
            "DESCENDANT_BODY_CREATION_BOUNDARY",
            resolver.ADMISSIBLE_FUTURE_ROUTE + "_PLUS_ANOTHER_USE",
        ):
            with self.subTest(use=use):
                request = _request(use)
                result = _resolve(request)
                self.assertNotApplicable(result)
                self.assertSection12Result(result, request)
                self.assertIs(
                    result["applicability"][
                        "candidate_standing_effect_applicability_recorded"
                    ],
                    False,
                )
                self.assertIs(result["applicability"]["standing_created"], False)

    def test_missing_bounded_basis_preserves_only_previously_validated_material(self) -> None:
        cases = (
            ("source_family", None),
            ("source_standing_contract", "source_standing_contract_reference"),
            ("source_artifact", "source_artifact_reference"),
            ("source_lineage", None),
            ("source_custody", None),
            ("source_rank", None),
            ("source_scope", None),
            ("admissible_future_route", None),
            ("declared_downstream_matter_use", None),
            ("cross_object_binding", None),
        )
        for section, key in cases:
            with self.subTest(missing=(section, key)):
                request = _request()
                if key is None:
                    del request[section]
                else:
                    del request[section][key]
                self.assertAdditional(_resolve(request))

        request = _request()
        request["no_standing_change_declaration"]["standing_creation_requested"] = (
            True
        )
        result = _resolve(request)
        self.assertBlocked(result)
        self.assertTrue(MANDATORY_EXACT_RESULT_KEYS.issubset(result))

    def test_source_contract_artifact_and_operation_mismatches_block(self) -> None:
        cases = (
            ("source_family", None, "OTHER_FAMILY"),
            ("source_family_semantic_owner", None, "CALLER"),
            (
                "source_standing_contract",
                "source_standing_contract_reference",
                "spec/other.md",
            ),
            (
                "source_standing_contract",
                "source_standing_contract_content_identity",
                "0" * 64,
            ),
            ("source_artifact", "source_artifact_content_identity", "1" * 64),
            ("source_artifact", "source_outcome", "OTHER_OUTCOME"),
            ("source_artifact", "source_failed_check_count", 1),
            ("source_artifact", "source_passed_check_count", 175),
            ("source_operation", "candidate_standing_operation_type", "OTHER_TYPE"),
            ("source_operation", "candidate_standing_operation_scope", "WIDER_SCOPE"),
            ("source_operation", "candidate_standing_supported", False),
            ("source_operation", "candidate_standing_authorized", False),
            ("source_operation", "candidate_standing_created", False),
            ("source_operation", "candidate_standing_created", 1),
        )
        for section, key, value in cases:
            with self.subTest(case=(section, key, value)):
                request = _request()
                if key is None:
                    request[section] = value
                else:
                    request[section][key] = value
                self.assertBlocked(_resolve(request))

        request = _request()
        request["standing_effect_locations"][0] = "caller.effect"
        self.assertBlocked(_resolve(request))

    def test_pair_material_split_hierarchy_and_ranking_remain_blocked(self) -> None:
        cases: list[tuple[str, dict[str, object]]] = []
        for member in ("candidate_a", "candidate_b"):
            request = _request()
            del request["candidate_pair"][member]
            cases.append((f"missing_{member}", request))
            request = _request()
            request["candidate_pair"][member]["candidate_standing_created"] = False
            cases.append((f"standing_false_{member}", request))

        request = _request()
        request["candidate_pair"]["candidate_a"]["candidate_record_id"] = (
            resolver.CANDIDATE_B_RECORD_ID
        )
        cases.append(("candidate_a_appropriates_b", request))

        for key, value in (
            ("candidate_records_remain_sibling", False),
            ("candidate_record_non_hierarchy_preserved", False),
            ("candidate_basis_non_hierarchy_preserved", False),
            ("regulation_not_sovereign_over_motion", False),
            ("motion_does_not_erase_regulation", False),
            ("coupling_assigned", True),
            ("third_candidate_created", True),
            ("descendant_body_created", True),
        ):
            request = _request()
            request["candidate_standing_operation_material"][
                "standing_pair_evaluation"
            ][key] = value
            cases.append((f"pair_{key}", request))

        for field in (
            "candidate_pair_split_requested",
            "candidate_pair_ranking_requested",
            "candidate_singleton_reuse_requested",
        ):
            request = _request()
            request["no_standing_change_declaration"][field] = True
            cases.append((field, request))

        for label, request in cases:
            with self.subTest(case=label):
                self.assertBlocked(_resolve(request))

    def test_complete_candidate_evaluations_are_exact(self) -> None:
        for section in (
            "candidate_a_standing_evaluation",
            "candidate_b_standing_evaluation",
            "standing_pair_evaluation",
        ):
            request = _request()
            del request["candidate_standing_operation_material"][section]
            with self.subTest(missing=section):
                self.assertBlocked(_resolve(request))

        for section in (
            "candidate_a_standing_evaluation",
            "candidate_b_standing_evaluation",
        ):
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
                request = _request()
                request["candidate_standing_operation_material"][section][key] = value
                with self.subTest(section=section, key=key):
                    self.assertBlocked(_resolve(request))

    def test_lineage_custody_rank_scope_and_binding_are_exact(self) -> None:
        cases = (
            ("source_lineage", 0, "spec/other.md"),
            ("source_custody", "custody_transferred", True),
            ("source_custody", "source_artifact_content_identity", "2" * 64),
            ("source_rank", "rank_upgraded", True),
            ("source_rank", "candidate_record_non_hierarchy_preserved", False),
            ("source_scope", "admissible_future_route", "WIDER_ROUTE"),
            ("source_scope", "basis_pair_scope", "SINGLETON_SCOPE"),
            ("cross_object_binding", "source_family", "OTHER_FAMILY"),
            ("cross_object_binding", "admissible_future_route", "WIDER_ROUTE"),
            ("cross_object_binding", "complete_pair_preserved", False),
        )
        for section, key, value in cases:
            with self.subTest(case=(section, key)):
                request = _request()
                request[section][key] = value
                self.assertBlocked(_resolve(request))

        for ids in (
            [resolver.CANDIDATE_A_RECORD_ID],
            [resolver.CANDIDATE_B_RECORD_ID],
            [resolver.CANDIDATE_B_RECORD_ID, resolver.CANDIDATE_A_RECORD_ID],
        ):
            request = _request()
            request["cross_object_binding"]["candidate_record_ids"] = ids
            with self.subTest(candidate_ids=ids):
                self.assertBlocked(_resolve(request))

    def test_source_and_boundary_non_claims_remain_exact_and_false(self) -> None:
        request = _request()
        del request["source_family_non_claims"][
            resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS[0]
        ]
        self.assertAdditional(_resolve(request))

        request = _request()
        request["source_family_non_claims"]["invented_non_claim"] = False
        self.assertBlocked(_resolve(request))

        for key in resolver.SOURCE_REQUIRED_FALSE_NON_CLAIMS:
            request = _request()
            request["source_family_non_claims"][key] = True
            with self.subTest(source_non_claim=key):
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["source_family_non_claims"][key], False)

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            request = _request()
            request["declared_non_claims"][key] = True
            with self.subTest(boundary_non_claim=key):
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["non_claims"][key], False)

    def test_route_equality_and_all_standing_change_requests_remain_closed(self) -> None:
        request = _request("DESCENDANT_BODY_CREATION_BOUNDARY_ONLY")
        self.assertNotApplicable(_resolve(request))

        request = _request("correspondence")
        request["declared_use_exactly_matches_source_route"] = True
        self.assertBlocked(_resolve(request))

        request = _request()
        request["admissible_future_route"] = "WIDENED_ROUTE"
        self.assertBlocked(_resolve(request))

        for field in resolver.NO_STANDING_CHANGE_FIELDS:
            request = _request()
            request["no_standing_change_declaration"][field] = True
            with self.subTest(overreach=field):
                result = _resolve(request)
                self.assertBlocked(result)
                self.assertIs(result["non_claims"]["standing_created"], False)
                self.assertIs(
                    result["non_claims"]["downstream_authorization_created"], False
                )

    def test_all_four_outcomes_remain_public_and_canonical(self) -> None:
        recorded = _resolve(_request())
        not_applicable = _resolve(_request("correspondence"))
        request = _request()
        del request["source_lineage"]
        additional = _resolve(request)
        blocked = _resolve(None)
        results = (recorded, not_applicable, additional, blocked)

        self.assertEqual(set(resolver.OUTCOMES), {item["outcome"] for item in results})
        for result in results:
            self.assertEqual("0.2.0", result["result_version"])
            self.assertEqual(resolver.RESOLVER_MODULE, result["resolver_module"])
            self.assertIs(result["boundary"]["review_exhausted"], True)
            self.assertCanonicalNonClaims(result)
            for check in result["checks"]:
                if check["failure_code"] is not None:
                    self.assertIn(check["failure_code"], resolver.STOP_CODES)
                if check["block_code"] is not None:
                    self.assertIn(check["block_code"], resolver.BLOCK_CODES)

    def test_exact_structures_are_copied_without_normalization_or_aliasing(self) -> None:
        request = _request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(first, second)
        self.assertEqual(before, request)
        self.assertSection12Result(first, before)

        request["source_custody"]["custody_transferred"] = "changed-after-call"
        request["source_lineage"][0] = "changed-after-call"
        request["candidate_standing_operation_material"][
            "standing_pair_evaluation"
        ]["candidate_records_remain_sibling"] = "changed-after-call"
        self.assertEqual(before["source_custody"], first["source_custody"])
        self.assertEqual(before["source_lineage"], first["source_lineage"])
        self.assertEqual(
            before["candidate_standing_operation_material"],
            first["candidate_standing_operation_material"],
        )

        first["source_custody"]["custody_transferred"] = "changed-result"
        first["source_lineage"][0] = "changed-result"
        first["standing_pair_evaluation"][
            "candidate_records_remain_sibling"
        ] = "changed-result"
        self.assertEqual("changed-after-call", request["source_custody"]["custody_transferred"])
        self.assertEqual("changed-after-call", request["source_lineage"][0])
        self.assertEqual(
            "changed-after-call",
            request["candidate_standing_operation_material"][
                "standing_pair_evaluation"
            ]["candidate_records_remain_sibling"],
        )

        third = _resolve(before)
        self.assertEqual(second, third)

    def test_only_section_12_contract_metadata_is_promoted_to_result(self) -> None:
        request = _request()
        result = _resolve(request)
        self.assertRecorded(result)
        self.assertSection12Result(result, request)
        source = result["source_binding"]
        for optional_input_only_field in (
            "source_standing_contract_identity",
            "source_standing_contract_type",
            "source_result_version",
            "source_resolver_module",
        ):
            self.assertNotIn(optional_input_only_field, source)

    def test_resolver_has_no_filesystem_hashing_persistence_or_generic_machinery(self) -> None:
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
        self.assertSection12Result(result, request)
        for key in (
            "operation_created",
            "runtime_created",
            "standing_created",
            "standing_renewed",
            "standing_extended",
            "standing_transferred",
            "standing_reinterpreted",
            "downstream_authorization_created",
            "generic_cross_family_standing_adapter_created",
            "registry_created",
            "catalogue_created",
            "ontology_created",
        ):
            self.assertIs(result["non_claims"][key], False, key)


if __name__ == "__main__":
    unittest.main()
