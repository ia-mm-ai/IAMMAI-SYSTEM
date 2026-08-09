"""Adversarial executable proof for the V2 pre-consumption boundary.

The governing contract is
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_BOUNDARY_V0_MIN_V2_SPEC.
The tests preserve V1 as predecessor evidence and prove all three V2
corrections: the boundary owns outcome allocation, required non-claim defects
are blocked, and review identity is checked structurally without external
uniqueness discovery.
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

import resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2 as resolver


def _set_path(value: dict, path: tuple[str, ...], replacement: object) -> None:
    current = value
    for key in path[:-1]:
        current = current[key]
    current[path[-1]] = replacement


def _delete_path(value: dict, path: tuple[str, ...]) -> None:
    current = value
    for key in path[:-1]:
        current = current[key]
    del current[path[-1]]


class DescendantBodyCreationConsumptionBoundaryV0MinV2Tests(unittest.TestCase):
    def canonical(
        self,
        intent: str = resolver.INTENT_RECORD,
        request_id: str = resolver.DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID,
    ) -> dict:
        return resolver.build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2_request(
            consumption_boundary_request_id=request_id,
            consumption_boundary_intent=intent,
        )

    def resolve(self, envelope: object) -> dict:
        return resolver.resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2(
            envelope
        )

    def assert_outcome(self, result: dict, expected: str) -> None:
        self.assertEqual(result["outcome"], expected)
        self.assertIn(expected, resolver.OUTCOME_FAMILY)
        self.assertEqual(set(result), resolver.RESULT_KEYS)
        self.assertIs(result["review_exhausted"], True)
        self.assertEqual(
            result["passed_check_count"],
            sum(check["passed"] for check in result["checks"]),
        )
        self.assertEqual(
            result["failed_check_count"],
            sum(not check["passed"] for check in result["checks"]),
        )
        for check in result["checks"]:
            self.assertIn(check["check_id"], resolver.CHECK_IDS)
            if check["failure_code"] is not None:
                self.assertIn(check["failure_code"], resolver.BLOCK_CODES)
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        self.assertIs(
            result["block"]["blocked"],
            expected == resolver.OUTCOME_REVIEW_BLOCKED,
        )
        self.assert_canonical_final_non_claims(result)

    def assert_canonical_final_non_claims(self, result: dict) -> None:
        self.assertEqual(
            tuple(result["non_claims"]), resolver.REQUIRED_FALSE_NON_CLAIMS
        )
        self.assertTrue(
            all(
                type(value) is bool and value is False
                for value in result["non_claims"].values()
            )
        )

    def assert_blocked(self, envelope: object) -> dict:
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_REVIEW_BLOCKED)
        return result

    def assert_additional(self, envelope: object) -> dict:
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        return result

    def test_public_contract_identity_naming_versions_and_builder(self) -> None:
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.CONSUMPTION_BOUNDARY_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_creation_boundary_request_admitted_"
            "standing_basis_consumption_boundary_v0_min_v2",
        )
        self.assertEqual(
            resolver.CONSUMPTION_BOUNDARY_TYPE,
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
            "BASIS_CONSUMPTION_BOUNDARY",
        )
        self.assertEqual(
            resolver.CONSUMPTION_BOUNDARY_SCOPE,
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_"
            "BODY_CREATION_BOUNDARY_REQUEST_ONE_FUTURE_CONSUMPTION_REVIEW_ONLY",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
                "BASIS_CONSUMPTION_BOUNDARY_RECORDED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
                "BASIS_CONSUMPTION_BOUNDARY_NOT_RECORDED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
                "BASIS_CONSUMPTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
                "BASIS_CONSUMPTION_BOUNDARY_REVIEW_BLOCKED",
            ),
        )
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.ENVELOPE_KEYS)
        self.assertNotIn("requested_terminal_outcome", envelope)
        self.assertNotIn("requested_consumption_boundary_outcome", envelope)
        self.assertEqual(
            envelope["selected_request_formation_result"]["result_content_identity"],
            "00ae4d23b703ac57f6eecf684e8c64d8bb7ca7fb0ff418b4d6a453813ffc5ef8",
        )
        self.assertEqual(
            envelope["selected_request_admission_result"]["result_content_identity"],
            "57c3272f7a0f3f36678397162573bae0836cf77f1db11ac2bb874efa66ff778d",
        )
        self.assertEqual(
            envelope["selected_standing_basis_admission_result"][
                "result_content_identity"
            ],
            "e53cb86c1b76eec212bbd90c1247da7adc0cd4c4cc26da82b4a3edd2c4aa639f",
        )

    def test_boundary_owned_terminal_allocation_and_regression_a(self) -> None:
        positive = self.resolve(self.canonical())
        negative = self.resolve(self.canonical(resolver.INTENT_DO_NOT_RECORD))
        blocked = self.resolve(self.canonical(resolver.INTENT_BLOCK))
        unsupported = self.resolve(self.canonical("RECORD_BY_ALIAS"))

        self.assert_outcome(positive, resolver.OUTCOME_RECORDED)
        self.assert_outcome(negative, resolver.OUTCOME_NOT_RECORDED)
        self.assert_outcome(blocked, resolver.OUTCOME_REVIEW_BLOCKED)
        self.assert_outcome(unsupported, resolver.OUTCOME_REVIEW_BLOCKED)

        for alias in (
            "requested_terminal_outcome",
            "requested_consumption_boundary_outcome",
            "requested_outcome",
            "desired_outcome",
            "caller_selected_outcome",
        ):
            with self.subTest(alias=alias):
                candidate = self.canonical()
                candidate[alias] = resolver.OUTCOME_RECORDED
                result = self.assert_blocked(candidate)
                self.assertEqual(
                    result["block"]["code"], resolver.CODE_OUTCOME_SELECTION
                )
                self.assertNotIn(alias, result)
                self.assertNotIn(alias, result["consumption_boundary"])

    def test_recorded_posture_is_positive_boundary_only(self) -> None:
        result = self.resolve(self.canonical())
        self.assert_outcome(result, resolver.OUTCOME_RECORDED)
        boundary = result["consumption_boundary"]
        true_fields = {
            key for key, value in boundary.items() if type(value) is bool and value
        }
        self.assertEqual(true_fields, set(resolver.ALLOWED_TRUE_RECORDED_FIELDS))
        self.assertIs(boundary["consumption_boundary_recorded"], True)

        forbidden = (
            "admitted_standing_basis_consumed",
            "admitted_standing_basis_exhausted",
            "basis_consumption_performed",
            "basis_exhaustion_performed",
            "consumption_token_created",
            "consumption_token_closed",
            "consumption_authorized",
            "later_one_shot_basis_consumption_review_authorized",
            "later_one_shot_basis_consumption_review_scheduled",
            "boundary_consideration_allowed",
            "boundary_consideration_performed",
            "invocation_request_admitted",
            "invocation_authorized",
            "invocation_performed",
            "execution_performed",
            "descendant_body_creation_authorized",
            "descendant_body_created",
            "standing_created",
            "source_applicability_created",
            "authority_created",
        )
        for key in forbidden:
            with self.subTest(key=key):
                self.assertIs(result["non_claims"][key], False)
        one_shot = result["one_shot_consumption_posture"]
        self.assertIs(one_shot["actual_consumption_identity_created"], False)
        self.assertIs(one_shot["consumption_token_created"], False)
        self.assertIs(one_shot["basis_exhausted"], False)
        self.assertIs(one_shot["target_boundary_consideration_allowed"], False)

    def test_structural_identity_and_regression_c(self) -> None:
        local_id = "one_local_distinct_pre_consumption_review"
        self.assert_outcome(
            self.resolve(self.canonical(request_id=local_id)),
            resolver.OUTCOME_RECORDED,
        )
        for invalid in (None, "", "   ", 1, [], {}):
            with self.subTest(invalid=invalid):
                candidate = self.canonical()
                candidate["consumption_boundary_request_id"] = invalid
                self.assert_blocked(candidate)

        canonical = self.canonical()
        collisions = (
            canonical["selected_request_formation_result"][
                "recorded_request_object"
            ]["request_id"],
            canonical["selected_request_admission_result"]["request_admission"][
                "request_admission_id"
            ],
            canonical["selected_standing_basis_admission_result"]["boundary"][
                "matter_bound_selected_surface_standing_basis_admission_id"
            ],
            canonical["selected_surface_binding"]["selected_surface_identity"],
            canonical["selected_target_boundary_binding"]["target_boundary_id"],
            canonical["selected_source_applicability_binding"]["boundary"][
                "descendant_body_candidate_standing_effect_applicability_boundary_id"
            ],
            canonical["freshness_and_non_replay_posture"][
                "explicitly_supplied_historical_result_identities"
            ][0],
        )
        for collision in collisions:
            with self.subTest(collision=collision):
                self.assert_blocked(self.canonical(request_id=collision))

        for sibling_key in (
            "alternative_consumption_boundary_request_id",
            "sibling_consumption_boundary_request_id",
            "consumption_boundary_request_id_alias",
            "implicit_latest_consumption_boundary_request_id",
        ):
            with self.subTest(sibling_key=sibling_key):
                candidate = self.canonical()
                candidate[sibling_key] = "sibling_002"
                self.assert_blocked(candidate)

    def test_request_formation_and_request_admission_are_exact(self) -> None:
        formation = ("selected_request_formation_result",)
        request = formation + ("recorded_request_object",)
        admission = ("selected_request_admission_result",)
        mutations = (
            (formation + ("result_reference",), "wrong/reference.json"),
            (formation + ("result_content_identity",), "0" * 64),
            (formation + ("outcome",), "REQUEST_NOT_RECORDED"),
            (request + ("request_id",), "wrong_request"),
            (request + ("request_type",), "WRONG_REQUEST"),
            (request + ("request_version",), "0.2.0"),
            (request + ("request_scope",), "WIDENED"),
            (request + ("declared_matter_use",), "GENERIC_USE"),
            (admission + ("result_reference",), "wrong/reference.json"),
            (admission + ("result_content_identity",), "1" * 64),
            (admission + ("resolver_module",), "wrong_resolver"),
            (admission + ("result_version",), "0.2.0"),
            (admission + ("outcome",), "REQUEST_NOT_ADMITTED"),
            (
                admission + ("request_admission", "request_admission_id"),
                "wrong_admission",
            ),
            (
                admission + ("request_admission", "request_admission_type"),
                "WRONG_ADMISSION",
            ),
            (
                admission + ("request_admission", "request_admission_version"),
                "0.2.0",
            ),
            (
                admission + ("request_admission", "request_admission_scope"),
                "WIDENED",
            ),
            (
                admission + ("request_admission", "outcome"),
                "REQUEST_NOT_ADMITTED",
            ),
            (admission + ("passed_check_count",), 2),
            (admission + ("failed_check_count",), 1),
            (admission + ("review_exhausted",), False),
            (admission + ("request_admission", "request_admitted"), False),
            (
                admission
                + (
                    "request_admission",
                    "eligible_for_later_separate_one_shot_basis_consumption_review",
                ),
                False,
            ),
            (
                admission
                + (
                    "non_claims",
                    "later_one_shot_basis_consumption_review_authorized",
                ),
                True,
            ),
            (
                admission
                + (
                    "non_claims",
                    "later_one_shot_basis_consumption_review_scheduled",
                ),
                True,
            ),
        )
        for path, replacement in mutations:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

    def test_standing_surface_applicability_target_pair_and_use_are_exact(self) -> None:
        standing = ("selected_standing_basis_admission_result",)
        surface = ("selected_surface_binding",)
        applicability = ("selected_source_applicability_binding",)
        target = ("selected_target_boundary_binding",)
        mutations = (
            (standing + ("result_reference",), "wrong/reference.json"),
            (standing + ("result_content_identity",), "2" * 64),
            (standing + ("outcome",), "NOT_ADMITTED"),
            (
                standing
                + (
                    "boundary",
                    "matter_bound_selected_surface_standing_basis_admission_id",
                ),
                "wrong_basis",
            ),
            (
                standing
                + (
                    "boundary",
                    "matter_bound_selected_surface_standing_basis_admission_type",
                ),
                "WRONG_BASIS",
            ),
            (
                standing
                + (
                    "boundary",
                    "matter_bound_selected_surface_standing_basis_admission_version",
                ),
                "0.2.0",
            ),
            (
                standing
                + (
                    "boundary",
                    "matter_bound_selected_surface_standing_basis_admission_scope",
                ),
                "WIDENED",
            ),
            (standing + ("failed_check_count",), 1),
            (standing + ("review_exhausted",), False),
            (surface + ("selected_surface_identity",), "candidate_a"),
            (surface + ("selected_surface_type",), "WRONG_SURFACE"),
            (surface + ("selected_surface_version",), "0.2.0"),
            (surface + ("selected_surface_scope",), "CANDIDATE_A_ONLY"),
            (surface + ("selected_surface_content_identity",), "3" * 64),
            (surface + ("complete_pair_preserved",), False),
            (surface + ("candidate_record_ids", 0), "wrong_candidate_a"),
            (surface + ("candidate_record_ids", 1), "wrong_candidate_b"),
            (surface + ("candidate_basis_ids", 0), "wrong_basis_a"),
            (surface + ("candidate_basis_ids", 1), "wrong_basis_b"),
            (surface + ("source_family",), "GENERIC_STANDING"),
            (surface + ("source_family_semantic_owner",), "THIS_BOUNDARY"),
            (surface + ("declared_matter_use",), "GENERIC_DESCENDANT_BODY_ROUTE"),
            (applicability + ("outcome",), "NOT_APPLICABLE"),
            (
                applicability + ("applicability_artifact_reference",),
                "wrong/reference.json",
            ),
            (
                applicability
                + (
                    "boundary",
                    "descendant_body_candidate_standing_effect_applicability_boundary_id",
                ),
                "wrong_applicability",
            ),
            (
                applicability + ("applicability", "admissible_future_route"),
                "DESCENDANT_BODY_CREATION",
            ),
            (target + ("target_boundary_id",), "wrong_target"),
            (target + ("target_boundary_type",), "WRONG_TARGET"),
            (target + ("target_boundary_version",), "0.2.0"),
            (target + ("target_boundary_scope",), "WIDENED"),
            (target + ("target_boundary_contract_reference",), "spec/other.md"),
            (target + ("target_boundary_contract_content_identity",), "4" * 64),
            (
                target + ("target_boundary_admissible_future_route",),
                "DESCENDANT_BODY_CREATION",
            ),
            (target + ("declared_matter_use",), "GENERIC_DESCENDANT_BODY_ROUTE"),
            (
                standing + ("declared_matter_use", "requested_standing_basis_use"),
                "GENERIC_DESCENDANT_BODY_ROUTE",
            ),
            (
                standing + ("admission_level_binding", "source_route"),
                "GENERIC_DESCENDANT_BODY_ROUTE",
            ),
            (
                standing + ("admission_level_binding", "declared_matter_use"),
                "GENERIC_DESCENDANT_BODY_ROUTE",
            ),
        )
        for path, replacement in mutations:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

        for pair_path in (
            surface + ("candidate_record_ids",),
            surface + ("candidate_basis_ids",),
            applicability + ("cross_object_binding", "candidate_record_ids"),
            applicability + ("cross_object_binding", "candidate_basis_ids"),
        ):
            with self.subTest(pair_path=pair_path):
                candidate = self.canonical()
                current = candidate
                for key in pair_path:
                    current = current[key]
                current.pop()
                self.assert_blocked(candidate)

    def test_freshness_one_shot_replay_and_overreach_are_blocked(self) -> None:
        freshness = (
            "freshness_and_non_replay_posture",
            "request_freshness",
        )
        one_shot = ("one_shot_consumption_posture",)
        mutations = (
            (freshness + ("fresh_request_identity_declared",), False),
            (freshness + ("historical_request_identity_reused",), True),
            (freshness + ("historical_request_material_reused",), True),
            (freshness + ("historical_request_reopened",), True),
            (freshness + ("historical_request_mutated",), True),
            (freshness + ("historical_request_replayed",), True),
            (freshness + ("historical_standing_basis_substituted",), True),
            (freshness + ("historical_success_treated_as_fresh_permission",), True),
            (one_shot + ("one_future_consumption_review_only",), False),
            (one_shot + ("actual_consumption_identity_created",), True),
            (one_shot + ("consumption_token_created",), True),
            (one_shot + ("consumption_token_closed",), True),
            (one_shot + ("basis_consumed",), True),
            (one_shot + ("basis_exhausted",), True),
            (one_shot + ("target_boundary_consideration_allowed",), True),
            (one_shot + ("invocation_authorized",), True),
            (one_shot + ("execution_performed",), True),
        )
        for path, replacement in mutations:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

        for extra in (
            "actual_consumption_identity",
            "consumption_token",
            "exhaustion_result",
            "target_boundary_consideration",
            "invocation_request",
            "execution_request",
            "generic_consumption_registry",
        ):
            with self.subTest(extra=extra):
                candidate = self.canonical()
                candidate[extra] = {"created": True}
                self.assert_blocked(candidate)

    def test_six_source_non_claim_maps_remain_separate_and_exact(self) -> None:
        envelope = self.canonical()
        contracts = (
            (
                (
                    "selected_request_formation_result",
                    "recorded_request_object",
                    "declared_non_claims",
                ),
                resolver.REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS,
            ),
            (
                ("selected_request_formation_result", "non_claims"),
                resolver.REQUEST_FORMATION_REQUIRED_FALSE_NON_CLAIMS,
            ),
            (
                ("selected_request_admission_result", "non_claims"),
                resolver.REQUEST_ADMISSION_REQUIRED_FALSE_NON_CLAIMS,
            ),
            (
                ("selected_standing_basis_admission_result", "non_claims"),
                resolver.STANDING_BASIS_REQUIRED_FALSE_NON_CLAIMS,
            ),
            (
                ("selected_source_applicability_binding", "non_claims"),
                resolver.SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS,
            ),
            (
                (
                    "selected_source_applicability_binding",
                    "source_family_non_claims",
                ),
                resolver.SOURCE_FAMILY_REQUIRED_FALSE_NON_CLAIMS,
            ),
        )
        maps = []
        for path, required in contracts:
            current = envelope
            for key in path:
                current = current[key]
            maps.append(current)
            self.assertEqual(tuple(current), required)
            self.assertTrue(all(value is False for value in current.values()))
        for index, first in enumerate(maps):
            for second in maps[index + 1 :]:
                self.assertIsNot(first, second)

        for path, required in contracts:
            key = required[0]
            for defect in ("map_missing", "key_missing", "non_boolean", "true", "extra"):
                with self.subTest(path=path, defect=defect):
                    candidate = self.canonical()
                    if defect == "map_missing":
                        _delete_path(candidate, path)
                    else:
                        current = candidate
                        for segment in path:
                            current = current[segment]
                        if defect == "key_missing":
                            del current[key]
                        elif defect == "non_boolean":
                            current[key] = 0
                        elif defect == "true":
                            current[key] = True
                        else:
                            current["unknown_non_claim"] = False
                    result = self.assert_blocked(candidate)
                    self.assertNotEqual(
                        result["outcome"],
                        resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                    )

    def test_boundary_local_non_claims_and_regression_b(self) -> None:
        canonical = self.canonical()
        self.assertEqual(
            tuple(canonical["declared_non_claims"]),
            resolver.REQUIRED_FALSE_NON_CLAIMS,
        )
        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(true_key=key):
                candidate = self.canonical()
                candidate["declared_non_claims"][key] = True
                result = self.assert_blocked(candidate)
                self.assertIs(result["non_claims"][key], False)

        representative = resolver.REQUIRED_FALSE_NON_CLAIMS[0]
        for defect in ("missing", "non_boolean"):
            candidate = self.canonical()
            if defect == "missing":
                del candidate["declared_non_claims"][representative]
            else:
                candidate["declared_non_claims"][representative] = 0
            self.assert_blocked(candidate)

        missing_source_non_claim = self.canonical()
        del missing_source_non_claim["selected_source_applicability_binding"][
            "non_claims"
        ][resolver.SOURCE_APPLICABILITY_REQUIRED_FALSE_NON_CLAIMS[0]]
        self.assert_blocked(missing_source_non_claim)

        ordinary_missing = self.canonical()
        del ordinary_missing["selected_request_formation_result"][
            "result_reference"
        ]
        self.assert_additional(ordinary_missing)

    def test_ordinary_missing_basis_is_additional_when_noncontradictory(self) -> None:
        paths = (
            ("selected_request_formation_result", "result_reference"),
            ("selected_request_formation_result", "result_content_identity"),
            ("selected_request_formation_result", "historical_completed_lineage"),
            (
                "selected_standing_basis_admission_result",
                "admission_level_binding",
                "source_custody",
            ),
            (
                "selected_standing_basis_admission_result",
                "admission_level_binding",
                "source_rank",
            ),
            (
                "selected_standing_basis_admission_result",
                "admission_level_binding",
                "source_scope",
            ),
            ("selected_surface_binding", "declared_matter_use"),
            ("selected_surface_binding", "complete_pair_preserved"),
            (
                "freshness_and_non_replay_posture",
                "request_freshness",
                "fresh_request_identity_declared",
            ),
        )
        for path in paths:
            with self.subTest(path=path):
                candidate = self.canonical()
                _delete_path(candidate, path)
                self.assert_additional(candidate)

    def test_blocked_first_and_additional_before_negative_precedence(self) -> None:
        cases = []
        blocked_plus_missing = self.canonical()
        del blocked_plus_missing["selected_request_formation_result"][
            "result_reference"
        ]
        blocked_plus_missing["declared_non_claims"]["authority_created"] = True
        cases.append((blocked_plus_missing, resolver.OUTCOME_REVIEW_BLOCKED))

        negative_plus_blocked = self.canonical(resolver.INTENT_DO_NOT_RECORD)
        negative_plus_blocked["declared_non_claims"]["standing_created"] = True
        cases.append((negative_plus_blocked, resolver.OUTCOME_REVIEW_BLOCKED))

        negative_plus_missing = self.canonical(resolver.INTENT_DO_NOT_RECORD)
        del negative_plus_missing["selected_request_admission_result"][
            "result_reference"
        ]
        cases.append(
            (negative_plus_missing, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        )

        block_plus_missing = self.canonical(resolver.INTENT_BLOCK)
        del block_plus_missing["selected_request_formation_result"][
            "result_reference"
        ]
        cases.append((block_plus_missing, resolver.OUTCOME_REVIEW_BLOCKED))

        for envelope, expected in cases:
            with self.subTest(expected=expected):
                first = self.resolve(envelope)
                second = self.resolve(copy.deepcopy(envelope))
                self.assert_outcome(first, expected)
                self.assertEqual(first, second)
                self.assertEqual(
                    sum(first["outcome"] == item for item in resolver.OUTCOME_FAMILY),
                    1,
                )

    def test_result_is_bounded_canonical_and_input_is_not_mutated(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_RECORDED)
        self.assertEqual(envelope, before)
        self.assertNotIn("declared_non_claims", result["consumption_boundary"])
        self.assertNotIn("source_request_result", result)
        self.assertNotIn("recorded_request_object", result)
        self.assertNotIn("actual_consumption_identity", result)
        self.assertNotIn("consumption_token", result)
        self.assertNotIn("exhaustion_result", result)
        self.assertNotIn("requested_terminal_outcome", result)
        self.assertEqual(
            result["selected_surface_binding"]["candidate_record_ids"],
            [
                "descendant_body_basis_candidate_a_001",
                "descendant_body_basis_candidate_b_001",
            ],
        )
        self.assertIs(
            result["selected_surface_binding"]["complete_pair_preserved"], True
        )
        self.assertEqual(
            result["selected_target_boundary_binding"]["declared_matter_use"],
            "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY",
        )

        blocked = self.canonical()
        blocked["declared_non_claims"]["standing_created"] = True
        blocked_result = self.resolve(blocked)
        self.assert_outcome(blocked_result, resolver.OUTCOME_REVIEW_BLOCKED)
        self.assertIs(blocked_result["non_claims"]["standing_created"], False)
        self.assertIsNone(blocked_result["selected_request_formation_result"])

    def test_pure_resolver_and_builder_use_no_external_uniqueness_or_upstream_resolution(self) -> None:
        envelope = self.canonical()
        resolver_functions = (
            (
                resolver._request_formation,
                "resolve_descendant_body_creation_boundary_request_v0_min",
            ),
            (
                resolver._request_admission,
                "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2",
            ),
            (
                resolver._standing_basis,
                "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
            ),
            (
                resolver._applicability,
                "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2",
            ),
        )
        patches = [
            mock.patch.object(
                module,
                name,
                side_effect=AssertionError("upstream resolver invoked"),
            )
            for module, name in resolver_functions
        ]
        with mock.patch.object(
            builtins, "open", side_effect=AssertionError("filesystem accessed")
        ), mock.patch.object(
            hashlib, "sha256", side_effect=AssertionError("runtime hashing used")
        ):
            for patcher in patches:
                patcher.start()
            try:
                result = self.resolve(envelope)
                rebuilt = resolver.build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2_request()
            finally:
                for patcher in reversed(patches):
                    patcher.stop()
        self.assert_outcome(result, resolver.OUTCOME_RECORDED)
        self.assertEqual(rebuilt, envelope)

        function_source = inspect.getsource(
            resolver.resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2
        )
        for prohibited in (
            "open(",
            "Path(",
            "glob(",
            "sha256(",
            "write(",
            "dump(",
            "resolve_descendant_body_creation_boundary_request_v0_min(",
            "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2(",
            "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(",
            "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2(",
        ):
            with self.subTest(prohibited=prohibited):
                self.assertNotIn(prohibited, function_source)

        module_source = inspect.getsource(resolver)
        for prohibited_import in (
            "import os",
            "import pathlib",
            "import hashlib",
            "import json",
        ):
            self.assertNotIn(prohibited_import, module_source)
        for prohibited_framework in (
            "class GenericConsumption",
            "class ConsumptionRegistry",
            "class ConsumptionCatalogue",
            "class ConsumptionOntology",
            "class WorkflowEngine",
            "class CrossFamilyAdapter",
        ):
            self.assertNotIn(prohibited_framework, module_source)

    def test_predecessor_spec_is_preserved_and_v2_governs(self) -> None:
        v1 = (
            REPO_ROOT
            / "spec"
            / "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_BOUNDARY_V0_MIN_SPEC.md"
        )
        v2 = (
            REPO_ROOT
            / "spec"
            / "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_BOUNDARY_V0_MIN_V2_SPEC.md"
        )
        self.assertEqual(
            hashlib.sha256(v1.read_bytes()).hexdigest(),
            "c48e46f01dd344d0fcb365dea3354ea4a9dba5e70b45b5890ae3b351bd702f4c",
        )
        v2_text = v2.read_text(encoding="utf-8")
        self.assertIn("Terminal Outcome Ownership", v2_text)
        self.assertIn("Structural Identity Law", v2_text)
        self.assertIn("Required non-claim defects", v2_text)
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION,
            "spec/DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_"
            "BASIS_CONSUMPTION_BOUNDARY_V0_MIN_V2_SPEC.md",
        )


if __name__ == "__main__":
    unittest.main()
