"""Adversarial V2 tests for descendant-body-creation request admission.

The governing contract is
DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_V0_MIN_V2_SPEC.  These
tests preserve the predecessor specification as lineage and prove the V2
correction: a required non-claim defect is blocked, while an ordinary
structural omission is additional basis when no blocked condition exists.
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

import resolve_descendant_body_creation_boundary_request_admission_v0_min_v2 as resolver


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


def _request_path(*suffix: str) -> tuple[str, ...]:
    return ("recorded_request_object",) + suffix


def _wrapped_request_path(*suffix: str) -> tuple[str, ...]:
    return ("source_request_result", "recorded_request_object") + suffix


class DescendantBodyCreationBoundaryRequestAdmissionV0MinV2Tests(
    unittest.TestCase
):
    def canonical(self, intent: str = resolver.INTENT_ADMIT) -> dict:
        return resolver.build_declared_descendant_body_creation_boundary_request_admission_v0_min_v2_request(
            intent
        )

    def resolve(self, envelope: object) -> dict:
        return resolver.resolve_descendant_body_creation_boundary_request_admission_v0_min_v2(
            envelope
        )

    def assert_outcome(self, result: dict, expected: str) -> None:
        self.assertEqual(result["outcome"], expected)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
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
        self.assertEqual(len(result["non_claims"]), 53)
        self.assertTrue(
            all(type(value) is bool and value is False for value in result["non_claims"].values())
        )

    def assert_blocked(self, envelope: object) -> dict:
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_REVIEW_BLOCKED)
        return result

    def assert_additional(self, envelope: object) -> dict:
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        return result

    def remove_from_both_requests(self, envelope: dict, suffix: tuple[str, ...]) -> None:
        _delete_path(envelope, _request_path(*suffix))
        _delete_path(envelope, _wrapped_request_path(*suffix))

    def test_public_contract_identity_versions_outcomes_and_builder(self) -> None:
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.REQUEST_ADMISSION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2",
        )
        self.assertEqual(
            resolver.REQUEST_ADMISSION_ID,
            "descendant_body_creation_boundary_request_admission_001",
        )
        self.assertEqual(
            resolver.REQUEST_ADMISSION_TYPE,
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION",
        )
        self.assertEqual(
            resolver.REQUEST_ADMISSION_SCOPE,
            "ONE_EXACT_RECORDED_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_ONLY",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_NOT_ADMITTED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_REQUIRES_ADDITIONAL_BASIS",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_REVIEW_BLOCKED",
            ),
        )
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.ENVELOPE_KEYS)
        self.assertEqual(len(envelope["recorded_request_object"]), 12)
        self.assertEqual(len(envelope["recorded_request_object"]["declared_non_claims"]), 52)
        self.assertEqual(len(envelope["source_request_result"]["non_claims"]), 52)
        self.assertEqual(len(envelope["declared_non_claims"]), 53)
        self.assertEqual(
            envelope["recorded_request_object"],
            envelope["source_request_result"]["recorded_request_object"],
        )
        self.assertIsNot(
            envelope["recorded_request_object"],
            envelope["source_request_result"]["recorded_request_object"],
        )

    def test_four_terminal_intents_and_positive_posture(self) -> None:
        positive = self.resolve(self.canonical())
        negative = self.resolve(self.canonical(resolver.INTENT_DO_NOT_ADMIT))
        blocked = self.resolve(self.canonical(resolver.INTENT_BLOCK))
        unsupported = self.resolve(self.canonical("ADMIT_BY_ALIAS"))

        self.assert_outcome(positive, resolver.OUTCOME_ADMITTED)
        self.assert_outcome(negative, resolver.OUTCOME_NOT_ADMITTED)
        self.assert_outcome(blocked, resolver.OUTCOME_REVIEW_BLOCKED)
        self.assert_outcome(unsupported, resolver.OUTCOME_REVIEW_BLOCKED)

        admission = positive["request_admission"]
        true_fields = {
            key for key, value in admission.items() if type(value) is bool and value
        }
        self.assertEqual(true_fields, set(resolver.ALLOWED_TRUE_ADMISSION_FIELDS))
        self.assertIs(
            admission["eligible_for_later_separate_one_shot_basis_consumption_review"],
            True,
        )
        for result in (negative, blocked, unsupported):
            self.assertTrue(
                all(
                    result["request_admission"][key] is False
                    for key in resolver.ALLOWED_TRUE_ADMISSION_FIELDS
                )
            )
            self.assertIsNone(result["admitted_request"])

    def test_positive_is_admission_only_and_basis_remains_unconsumed(self) -> None:
        result = self.resolve(self.canonical())
        self.assert_outcome(result, resolver.OUTCOME_ADMITTED)
        non_claims = result["non_claims"]
        forbidden = (
            "later_one_shot_basis_consumption_review_authorized",
            "later_one_shot_basis_consumption_review_scheduled",
            "admitted_standing_basis_consumed",
            "admitted_standing_basis_exhausted",
            "basis_consumption_performed",
            "basis_exhaustion_performed",
            "consumption_token_created",
            "consumption_token_closed",
            "consumption_authorized",
            "basis_reuse_permission_created",
            "boundary_consideration_allowed",
            "boundary_consideration_performed",
            "descendant_body_creation_operation_consideration_allowed",
            "invocation_request_admitted",
            "invocation_authorized",
            "invocation_token_created",
            "invocation_performed",
            "execution_permission_created",
            "execution_performed",
            "descendant_body_creation_authorized",
            "descendant_body_creation_executed",
            "descendant_body_creation_performed",
            "descendant_body_created",
            "runtime_created",
            "standing_created",
            "source_applicability_created",
            "authority_created",
            "follow_on_work_authorized",
        )
        for key in forbidden:
            with self.subTest(key=key):
                self.assertIs(non_claims[key], False)

        projection = result["admitted_request"]
        self.assertIs(projection["basis_reference_posture"]["admitted_standing_basis_referenced"], True)
        self.assertIs(
            projection["basis_reference_posture"][
                "admitted_standing_basis_intended_for_later_separate_consumption_review"
            ],
            True,
        )
        for key in (
            "admitted_standing_basis_consumed",
            "admitted_standing_basis_exhausted",
            "consumption_token_closed",
            "consumption_authorized",
            "basis_reuse_permission_created",
        ):
            self.assertIs(projection["basis_reference_posture"][key], False)

    def test_exact_source_result_contract_and_informational_block_code(self) -> None:
        envelope = self.canonical()
        source = envelope["source_request_result"]
        self.assertEqual(
            envelope["source_request_result_reference"],
            resolver.SOURCE_REQUEST_RESULT_REFERENCE,
        )
        self.assertEqual(
            envelope["source_request_result_content_identity"],
            resolver.SOURCE_REQUEST_RESULT_CONTENT_IDENTITY,
        )
        self.assertEqual(source["resolver_module"], "resolve_descendant_body_creation_boundary_request_v0_min")
        self.assertEqual(source["result_version"], "0.1.0")
        self.assertEqual(source["outcome"], "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_RECORDED")
        self.assertIs(source["review_exhausted"], True)
        self.assertEqual(source["passed_check_count"], 1)
        self.assertEqual(source["failed_check_count"], 0)
        self.assertEqual(
            source["checks"],
            [{"check_id": "closed_request_formation_envelope", "passed": True, "failure_code": None}],
        )
        self.assertEqual(source["block"]["code"], "REQUEST_FORMATION_RECORDED")
        self.assertIs(source["block"]["blocked"], False)
        self.assert_outcome(self.resolve(envelope), resolver.OUTCOME_ADMITTED)

        source_mutations = (
            (("source_request_result_reference",), "wrong/reference.json"),
            (("source_request_result_content_identity",), "0" * 64),
            (("source_request_result", "resolver_module"), "wrong_resolver"),
            (("source_request_result", "result_version"), "0.2.0"),
            (("source_request_result", "outcome"), "REQUEST_RECORDED"),
            (("source_request_result", "review_exhausted"), False),
            (("source_request_result", "passed_check_count"), 2),
            (("source_request_result", "failed_check_count"), 1),
            (("source_request_result", "checks"), [{"check_id": "wrong", "passed": True, "failure_code": None}]),
            (("source_request_result", "checks"), [{"check_id": "closed_request_formation_envelope", "passed": False, "failure_code": None}]),
            (("source_request_result", "checks"), [{"check_id": "closed_request_formation_envelope", "passed": True, "failure_code": "FAIL"}]),
            (("source_request_result", "block", "blocked"), True),
            (("source_request_result", "block", "code"), "BLOCKED"),
        )
        for path, replacement in source_mutations:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

        missing_sole_check = self.canonical()
        missing_sole_check["source_request_result"]["checks"] = []
        self.assert_additional(missing_sole_check)

    def test_request_identity_equality_and_binding_are_exact(self) -> None:
        request_mutations = (
            ("request_id", "descendant_body_creation_boundary_001"),
            ("request_type", "DESCENDANT_BODY_CREATION_BOUNDARY"),
            ("request_version", "0.2.0"),
            ("request_scope", "WIDENED"),
            ("request_question", "different question"),
            ("request_intent", "ADMIT_REQUEST"),
        )
        for key, replacement in request_mutations:
            with self.subTest(request_field=key):
                candidate = self.canonical()
                candidate["recorded_request_object"][key] = replacement
                self.assert_blocked(candidate)

        candidate = self.canonical()
        candidate["recorded_request_object"]["extra"] = False
        self.assert_blocked(candidate)

        binding_mutations = (
            ("request_id", "wrong_request"),
            ("source_request_result_reference", "wrong/reference.json"),
            ("source_request_result_content_identity", "f" * 64),
            ("source_request_result_outcome", "WRONG"),
            ("recorded_request_object_matches_source_result", False),
        )
        for key, replacement in binding_mutations:
            with self.subTest(binding=key):
                candidate = self.canonical()
                candidate["request_result_binding"][key] = replacement
                self.assert_blocked(candidate)

    def test_target_basis_surface_routes_and_semantic_owner_are_exact(self) -> None:
        base = ("recorded_request_object",)
        target = base + ("target_boundary",)
        basis = base + ("intended_admitted_standing_basis",)
        selected = basis + ("selected_surface",)
        mutations = (
            (target + ("target_boundary_id",), "wrong_target"),
            (target + ("target_boundary_type",), "WRONG_TARGET"),
            (target + ("target_boundary_version",), "0.2.0"),
            (target + ("target_boundary_scope",), "WIDENED"),
            (target + ("target_boundary_contract_reference",), "spec/other.md"),
            (target + ("target_boundary_contract_content_identity",), "0" * 64),
            (target + ("target_boundary_admissible_future_route",), "AUTOMATIC"),
            (basis + ("standing_basis_admission_id",), "wrong_basis"),
            (basis + ("standing_basis_admission_type",), "WRONG_BASIS"),
            (basis + ("standing_basis_admission_version",), "0.2.0"),
            (basis + ("standing_basis_admission_scope",), "WIDENED"),
            (basis + ("standing_basis_admission_outcome",), "NOT_ADMITTED"),
            (basis + ("standing_basis_admission_reference",), "wrong/reference.json"),
            (basis + ("standing_basis_admission_content_identity",), "1" * 64),
            (basis + ("standing_basis_admission_failed_check_count",), 1),
            (basis + ("standing_basis_admission_review_exhausted",), False),
            (selected + ("selected_surface_identity",), "candidate_a"),
            (selected + ("selected_surface_type",), "WRONG_SURFACE"),
            (selected + ("selected_surface_version",), "0.2.0"),
            (selected + ("selected_surface_scope",), "CANDIDATE_A_ONLY"),
            (selected + ("selected_surface_reference",), "wrong/reference.json"),
            (selected + ("selected_surface_content_identity",), "2" * 64),
            (selected + ("complete_pair_preserved",), False),
            (selected + ("source_family",), "GENERIC_STANDING"),
            (selected + ("source_family_semantic_owner",), "REQUEST_ADMISSION"),
            (base + ("declared_matter_use",), "DESCENDANT_BODY_CREATION"),
            (basis + ("standing_basis_admission_declared_use",), "CORRESPONDENCE"),
            (basis + ("source_route",), "GENERIC_DESCENDANT_BODY_USE"),
            (("admission_declared_matter_use",), "DESCENDANT_BODY_CREATION"),
        )
        for path, replacement in mutations:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

        for pair_key in ("candidate_record_ids", "candidate_basis_ids"):
            with self.subTest(pair_key=pair_key):
                candidate = self.canonical()
                candidate["recorded_request_object"]["intended_admitted_standing_basis"]["selected_surface"][pair_key].pop()
                self.assert_blocked(candidate)

    def test_basis_freshness_historical_and_overreach_claims_block(self) -> None:
        request = ("recorded_request_object",)
        posture = request + ("basis_reference_posture",)
        freshness = request + ("freshness_and_non_replay",)
        contradictory_postures = (
            (posture + ("admitted_standing_basis_referenced",), False),
            (posture + ("admitted_standing_basis_intended_for_later_separate_consumption_review",), False),
            (posture + ("admitted_standing_basis_consumed",), True),
            (posture + ("admitted_standing_basis_exhausted",), True),
            (posture + ("consumption_token_closed",), True),
            (posture + ("consumption_authorized",), True),
            (posture + ("basis_reuse_permission_created",), True),
            (freshness + ("fresh_request_identity_declared",), False),
            (freshness + ("request_identity_distinct_from_target_boundary",), False),
            (freshness + ("request_identity_distinct_from_historical_completed_lineage",), False),
            (freshness + ("historical_request_identity_reused",), True),
            (freshness + ("historical_request_material_reused",), True),
            (freshness + ("historical_request_reopened",), True),
            (freshness + ("historical_request_mutated",), True),
            (freshness + ("historical_request_replayed",), True),
            (freshness + ("historical_standing_basis_substituted",), True),
            (freshness + ("historical_success_treated_as_fresh_permission",), True),
            (("source_request_result", "historical_completed_lineage", "historical_boundary_result_reference"), "wrong/reference.json"),
            (("source_request_result", "historical_completed_lineage", "historical_boundary_result_content_identity"), "3" * 64),
            (("source_request_result", "historical_completed_lineage", "historical_boundary_outcome"), "INHERITED_ALLOWANCE"),
            (("source_request_result", "historical_completed_lineage", "historical_boundary_result"), "INVOKE"),
        )
        for path, replacement in contradictory_postures:
            with self.subTest(path=path):
                candidate = self.canonical()
                _set_path(candidate, path, replacement)
                self.assert_blocked(candidate)

        for key in (
            "admitted_standing_basis_consumed",
            "admitted_standing_basis_exhausted",
            "consumption_token_closed",
            "consumption_authorized",
            "candidate_pair_split",
            "candidate_pair_ranked",
            "candidate_a_independently_selected",
            "candidate_b_independently_selected",
            "semantic_ownership_transferred",
            "standing_created",
            "source_applicability_created",
            "authority_created",
            "boundary_consideration_allowed",
            "invocation_authorized",
            "invocation_performed",
            "descendant_body_creation_authorized",
            "descendant_body_created",
            "automatic_successor_created",
        ):
            with self.subTest(admission_non_claim=key):
                candidate = self.canonical()
                candidate["declared_non_claims"][key] = True
                self.assert_blocked(candidate)

    def test_three_non_claim_contracts_are_separate_exact_and_blocked_on_defect(self) -> None:
        envelope = self.canonical()
        request_non_claims = envelope["recorded_request_object"]["declared_non_claims"]
        wrapped_request_non_claims = envelope["source_request_result"]["recorded_request_object"]["declared_non_claims"]
        source_result_non_claims = envelope["source_request_result"]["non_claims"]
        admission_non_claims = envelope["declared_non_claims"]

        self.assertEqual(tuple(request_non_claims), resolver.SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS)
        self.assertEqual(tuple(wrapped_request_non_claims), resolver.SOURCE_REQUEST_REQUIRED_FALSE_NON_CLAIMS)
        self.assertEqual(tuple(source_result_non_claims), resolver.SOURCE_RESULT_REQUIRED_FALSE_NON_CLAIMS)
        self.assertEqual(tuple(admission_non_claims), resolver.REQUIRED_FALSE_NON_CLAIMS)
        self.assertEqual((len(request_non_claims), len(source_result_non_claims), len(admission_non_claims)), (52, 52, 53))
        self.assertIsNot(request_non_claims, wrapped_request_non_claims)
        self.assertIsNot(request_non_claims, source_result_non_claims)
        self.assertIsNot(source_result_non_claims, admission_non_claims)

        cases = (
            (("recorded_request_object", "declared_non_claims"), next(iter(request_non_claims))),
            (("source_request_result", "recorded_request_object", "declared_non_claims"), next(iter(wrapped_request_non_claims))),
            (("source_request_result", "non_claims"), next(iter(source_result_non_claims))),
            (("declared_non_claims",), next(iter(admission_non_claims))),
        )
        for map_path, key in cases:
            for defect in ("missing", "non_boolean", "true"):
                with self.subTest(map_path=map_path, key=key, defect=defect):
                    candidate = self.canonical()
                    current = candidate
                    for segment in map_path:
                        current = current[segment]
                    if defect == "missing":
                        del current[key]
                    elif defect == "non_boolean":
                        current[key] = 0
                    else:
                        current[key] = True
                    result = self.assert_blocked(candidate)
                    self.assertNotEqual(
                        result["outcome"], resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                    )

    def test_explicit_v1_collision_regression(self) -> None:
        missing_admission_non_claim = self.canonical()
        del missing_admission_non_claim["declared_non_claims"]["standing_created"]
        blocked = self.resolve(missing_admission_non_claim)

        ordinary_missing = self.canonical()
        del ordinary_missing["source_request_result_content_identity"]
        additional = self.resolve(ordinary_missing)

        missing_source_non_claim = self.canonical()
        del missing_source_non_claim["source_request_result"]["non_claims"]["standing_created"]
        source_blocked = self.resolve(missing_source_non_claim)

        self.assert_outcome(blocked, resolver.OUTCOME_REVIEW_BLOCKED)
        self.assert_outcome(additional, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assert_outcome(source_blocked, resolver.OUTCOME_REVIEW_BLOCKED)
        self.assertNotEqual(blocked["outcome"], additional["outcome"])
        self.assertNotEqual(source_blocked["outcome"], additional["outcome"])

    def test_ordinary_structural_absence_is_additional_only_without_block(self) -> None:
        simple_missing_paths = (
            ("request_admission_id",),
            ("source_request_result_reference",),
            ("source_request_result_content_identity",),
            ("request_result_binding",),
            ("source_request_result", "passed_check_count"),
            ("admission_declared_matter_use",),
            ("source_request_result", "historical_completed_lineage", "historical_boundary_result_reference"),
        )
        for path in simple_missing_paths:
            with self.subTest(path=path):
                candidate = self.canonical()
                _delete_path(candidate, path)
                self.assert_additional(candidate)

        both_request_missing = (
            ("intended_admitted_standing_basis", "admission_level_binding", "source_custody"),
            ("intended_admitted_standing_basis", "selected_surface", "complete_pair_preserved"),
            ("freshness_and_non_replay", "fresh_request_identity_declared"),
        )
        for suffix in both_request_missing:
            with self.subTest(suffix=suffix):
                candidate = self.canonical()
                self.remove_from_both_requests(candidate, suffix)
                self.assert_additional(candidate)

    def test_v2_precedence_combinations_are_single_and_deterministic(self) -> None:
        combinations = []

        ordinary_plus_nonclaim = self.canonical()
        del ordinary_plus_nonclaim["source_request_result_content_identity"]
        ordinary_plus_nonclaim["declared_non_claims"]["authority_created"] = True
        combinations.append((ordinary_plus_nonclaim, resolver.OUTCOME_REVIEW_BLOCKED))

        negative_plus_nonclaim = self.canonical(resolver.INTENT_DO_NOT_ADMIT)
        negative_plus_nonclaim["declared_non_claims"]["standing_created"] = True
        combinations.append((negative_plus_nonclaim, resolver.OUTCOME_REVIEW_BLOCKED))

        positive_plus_nonclaim = self.canonical()
        positive_plus_nonclaim["source_request_result"]["non_claims"]["standing_created"] = True
        combinations.append((positive_plus_nonclaim, resolver.OUTCOME_REVIEW_BLOCKED))

        negative_plus_missing = self.canonical(resolver.INTENT_DO_NOT_ADMIT)
        del negative_plus_missing["source_request_result_reference"]
        combinations.append((negative_plus_missing, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS))

        block_plus_missing = self.canonical(resolver.INTENT_BLOCK)
        del block_plus_missing["source_request_result_reference"]
        combinations.append((block_plus_missing, resolver.OUTCOME_REVIEW_BLOCKED))

        for candidate, expected in combinations:
            with self.subTest(expected=expected):
                first = self.resolve(candidate)
                second = self.resolve(copy.deepcopy(candidate))
                self.assert_outcome(first, expected)
                self.assertEqual(first, second)
                self.assertEqual(sum(first["outcome"] == item for item in resolver.OUTCOME_FAMILY), 1)

    def test_implicit_latest_recency_presence_and_alias_material_fail_closed(self) -> None:
        for key, value in (
            ("timestamp", "2026-08-09T00:00:00Z"),
            ("recency", "latest"),
            ("repository_presence", True),
            ("implicit_latest", True),
            ("matching_target", True),
            ("matching_matter", True),
            ("candidate_population", []),
            ("fallback_source", {}),
        ):
            with self.subTest(key=key):
                candidate = self.canonical()
                candidate[key] = value
                self.assert_blocked(candidate)

        self.assert_blocked(None)
        self.assert_blocked([])
        missing_intent = self.canonical()
        del missing_intent["request_admission_intent"]
        self.assert_blocked(missing_intent)

    def test_result_is_bounded_projection_and_preserves_source_facts(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        result = self.resolve(envelope)
        self.assert_outcome(result, resolver.OUTCOME_ADMITTED)
        self.assertEqual(envelope, before)

        admitted = result["admitted_request"]
        self.assertNotEqual(admitted, before["recorded_request_object"])
        self.assertNotIn("request_question", admitted)
        self.assertNotIn("request_intent", admitted)
        self.assertNotIn("declared_non_claims", admitted)
        self.assertNotIn("source_applicability_result", admitted)

        binding = result["source_request_result_binding"]
        self.assertNotEqual(binding, before["source_request_result"])
        for raw_key in ("recorded_request_object", "checks", "non_claims", "request_formation"):
            self.assertNotIn(raw_key, binding)
        self.assertNotIn("source_request_result", result)
        self.assertNotIn("recorded_request_object", result)

        source_request_non_claims = before["source_request_result"]["recorded_request_object"]["declared_non_claims"]
        self.assertIs(source_request_non_claims["request_admitted"], False)
        self.assertIs(source_request_non_claims["request_admission_recorded"], False)
        self.assertIs(result["request_admission"]["request_admitted"], True)
        self.assertIs(result["request_admission"]["request_admission_recorded"], True)
        self.assertIs(binding["source_request_declared_non_claims_preserved"], True)
        self.assertIs(binding["source_request_result_non_claims_preserved"], True)

    def test_pure_resolver_has_no_filesystem_hashing_or_upstream_invocation(self) -> None:
        envelope = self.canonical()
        upstream_names = (
            "resolve_descendant_body_creation_boundary_request_v0_min",
            "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
        )
        patches = []
        for module in (resolver._formation, resolver._formation._admission):
            for name in upstream_names:
                if hasattr(module, name):
                    patches.append(
                        mock.patch.object(
                            module,
                            name,
                            side_effect=AssertionError("upstream resolver invoked"),
                        )
                    )

        with mock.patch.object(
            builtins, "open", side_effect=AssertionError("filesystem access attempted")
        ), mock.patch.object(
            hashlib, "sha256", side_effect=AssertionError("runtime hashing attempted")
        ):
            for patcher in patches:
                patcher.start()
            try:
                result = self.resolve(envelope)
            finally:
                for patcher in reversed(patches):
                    patcher.stop()
        self.assert_outcome(result, resolver.OUTCOME_ADMITTED)

        function_source = inspect.getsource(
            resolver.resolve_descendant_body_creation_boundary_request_admission_v0_min_v2
        )
        for prohibited in (
            "open(",
            "Path(",
            "glob(",
            "sha256(",
            "write(",
            "dump(",
            "resolve_descendant_body_creation_boundary_request_v0_min(",
            "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min(",
            "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2(",
            "resolve_descendant_body_candidate_standing_operation_v0_min(",
            "resolve_descendant_body_creation_boundary_v0_min(",
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

    def test_result_nonclaims_are_false_for_every_outcome(self) -> None:
        cases = [
            self.canonical(),
            self.canonical(resolver.INTENT_DO_NOT_ADMIT),
            self.canonical(resolver.INTENT_BLOCK),
        ]
        additional = self.canonical()
        del additional["source_request_result_reference"]
        cases.append(additional)
        blocked = self.canonical()
        blocked["declared_non_claims"]["follow_on_work_authorized"] = True
        cases.append(blocked)

        for candidate in cases:
            with self.subTest(intent=candidate.get("request_admission_intent")):
                result = self.resolve(candidate)
                self.assert_canonical_final_non_claims(result)
                self.assertTrue(
                    all(
                        type(value) is bool
                        for value in result["request_admission"].values()
                        if type(value) is bool
                    )
                )


if __name__ == "__main__":
    unittest.main()
