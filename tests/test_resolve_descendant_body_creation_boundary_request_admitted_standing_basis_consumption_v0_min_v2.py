"""Tests for the additive V2 admitted-standing-basis consumption resolver.

The V1 constitutional articulation remains preserved.  These tests exercise
the V2 executable articulation only: one exact caller-supplied consumption
identity, one closed event binding, blocked-first terminal allocation, and
deterministic re-rendering of one constitutional event.
"""

from __future__ import annotations

import copy
import hashlib
import inspect
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2 as applicability  # noqa: E402
import resolve_descendant_body_creation_boundary_request_admission_v0_min_v2 as request_admission  # noqa: E402
import resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2 as pre_consumption  # noqa: E402
import resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2 as resolver  # noqa: E402
import resolve_descendant_body_creation_boundary_request_v0_min as request_formation  # noqa: E402
import resolve_matter_bound_selected_surface_standing_basis_admission_v0_min as standing_basis  # noqa: E402


V1_SPEC = (
    REPO_ROOT
    / "spec"
    / "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_V0_MIN_SPEC.md"
)
V2_SPEC = (
    REPO_ROOT
    / "spec"
    / "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_V0_MIN_V2_SPEC.md"
)


def _canonical(intent: str = resolver.INTENT_RECORD) -> dict:
    return resolver.build_declared_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2_request(
        request_consumption_intent=intent
    )


def _resolve(envelope: object) -> dict:
    return resolver.resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_v0_min_v2(
        envelope
    )


def _parent_and_key(root: dict, path: tuple[str, ...]) -> tuple[dict, str]:
    current = root
    for key in path[:-1]:
        current = current[key]
    return current, path[-1]


def _delete(root: dict, path: tuple[str, ...]) -> None:
    parent, key = _parent_and_key(root, path)
    del parent[key]


def _replace(root: dict, path: tuple[str, ...], value: object) -> None:
    parent, key = _parent_and_key(root, path)
    parent[key] = value


class DescendantBodyCreationBoundaryRequestAdmittedStandingBasisConsumptionV2Tests(
    unittest.TestCase
):
    maxDiff = None

    def assert_public_codes(self, result: dict) -> None:
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        for check in result["checks"]:
            code = check["failure_code"]
            if code is not None:
                self.assertIn(code, resolver.BLOCK_CODES)

    def assert_canonical_non_claims(self, result: dict) -> None:
        self.assertEqual(result["non_claims"], resolver.CANONICAL_NON_CLAIMS)
        self.assertEqual(
            set(result["non_claims"]), set(resolver.REQUIRED_FALSE_NON_CLAIMS)
        )
        self.assertTrue(
            all(type(value) is bool and value is False for value in result["non_claims"].values())
        )

    def assert_outcome(self, result: dict, outcome: str) -> None:
        self.assertEqual(result["outcome"], outcome)
        self.assertEqual(result["consumption_result"]["outcome"], outcome)
        self.assertTrue(result["review_exhausted"])
        self.assert_public_codes(result)
        self.assert_canonical_non_claims(result)

    def test_public_contract_versions_and_closed_builder(self) -> None:
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(resolver.CONSUMPTION_VERSION, "0.1.0")
        self.assertEqual(
            resolver.CONSUMPTION_TYPE,
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION",
        )
        self.assertEqual(
            resolver.GOVERNING_SPECIFICATION,
            "spec/DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION_V0_MIN_V2_SPEC.md",
        )
        self.assertEqual(
            resolver.DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID,
            "descendant_body_creation_boundary_request_admitted_standing_basis_consumption_request_001",
        )
        self.assertEqual(
            set(resolver.OUTCOME_FAMILY),
            {
                resolver.OUTCOME_CONSUMED,
                resolver.OUTCOME_NOT_CONSUMED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_BLOCKED,
            },
        )

        first = _canonical()
        second = _canonical()
        self.assertEqual(set(first), resolver.ENVELOPE_KEYS)
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        first["declared_non_claims"]["runtime_created"] = True
        self.assertFalse(second["declared_non_claims"]["runtime_created"])
        self.assertEqual(
            first["selected_consumption_boundary_result"]["checks"],
            list(resolver.PRE_CONSUMPTION_SUPPORTING_CHECK_RECORDS),
        )

    def test_positive_consumption_and_exact_downstream_refusals(self) -> None:
        result = _resolve(_canonical())
        self.assert_outcome(result, resolver.OUTCOME_CONSUMED)
        self.assertEqual(set(result), resolver.RESULT_KEYS)
        self.assertEqual(
            result["declared_request_consumption_question"][
                "request_consumption_request_id"
            ],
            resolver.DEFAULT_REQUEST_CONSUMPTION_REQUEST_ID,
        )

        consumption = result["consumption_result"]
        for key in resolver.ALLOWED_TRUE_CONSUMED_FIELDS:
            self.assertIs(consumption[key], True, key)
        self.assertIs(result["non_claims"]["consumption_token_created"], False)
        for key in (
            "boundary_consideration_allowed",
            "boundary_consideration_performed",
            "invocation_request_admitted",
            "invocation_authorized",
            "invocation_performed",
            "execution_permission_created",
            "execution_performed",
            "descendant_body_creation_authorized",
            "descendant_body_creation_executed",
            "descendant_body_creation_performed",
            "descendant_body_created",
            "standing_created",
            "standing_renewed",
            "standing_extended",
            "source_applicability_created",
            "authority_created",
            "runtime_created",
            "basis_reuse_permission_created",
            "request_reuse_permission_created",
            "repeat_permission_created",
            "continuation_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(result["non_claims"][key], False, key)

        predecessor = result["selected_consumption_boundary_result"]
        self.assertFalse(
            predecessor["one_shot_consumption_posture"]["basis_consumed"]
        )
        self.assertFalse(
            predecessor["one_shot_consumption_posture"]["basis_exhausted"]
        )
        self.assertTrue(consumption["basis_consumed"])
        self.assertTrue(consumption["basis_exhausted"])
        self.assertTrue(consumption["consumption_token_closed"])

    def test_exact_negative_and_control_outcomes(self) -> None:
        negative = _resolve(_canonical(resolver.INTENT_DO_NOT_RECORD))
        self.assert_outcome(negative, resolver.OUTCOME_NOT_CONSUMED)
        for key in resolver.ALLOWED_TRUE_CONSUMED_FIELDS:
            self.assertIs(negative["consumption_result"][key], False, key)

        for intent in (resolver.INTENT_BLOCK, "UNSUPPORTED", "", 7, None):
            with self.subTest(intent=intent):
                blocked = _resolve(_canonical(intent))
                self.assert_outcome(blocked, resolver.OUTCOME_BLOCKED)

        for malformed in (None, [], "request", 1, True):
            with self.subTest(malformed=malformed):
                self.assert_outcome(_resolve(malformed), resolver.OUTCOME_BLOCKED)

    def test_caller_outcome_selection_and_undefined_refusal_fields_block(self) -> None:
        for key in (
            "requested_terminal_outcome",
            "requested_request_consumption_outcome",
            "requested_consumption_outcome",
            "requested_outcome",
            "desired_outcome",
            "expected_outcome",
            "caller_selected_outcome",
        ):
            envelope = _canonical()
            envelope[key] = resolver.OUTCOME_CONSUMED
            with self.subTest(outcome_key=key):
                result = _resolve(envelope)
                self.assert_outcome(result, resolver.OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["code"], resolver.CODE_OUTCOME_SELECTION)

        for key in (
            "not_consumed_basis",
            "lawful_refusal_basis",
            "refusal_basis",
            "refusal_object",
            "refusal_reason",
            "not_consumed_reason",
            "reason_for_not_consuming",
            "free_text_refusal",
        ):
            envelope = _canonical(resolver.INTENT_DO_NOT_RECORD)
            envelope[key] = "caller-supplied refusal"
            with self.subTest(refusal_key=key):
                result = _resolve(envelope)
                self.assert_outcome(result, resolver.OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["code"], resolver.CODE_REFUSAL_FIELD)

    def test_actual_consumption_identity_is_exact_fresh_and_non_colliding(self) -> None:
        canonical = _canonical()
        collisions = {
            request_formation.REQUEST_ID,
            request_admission.REQUEST_ADMISSION_ID,
            pre_consumption.DEFAULT_CONSUMPTION_BOUNDARY_REQUEST_ID,
            standing_basis.BOUNDARY_ID,
            request_formation.SELECTED_SURFACE_IDENTITY,
            request_formation.SOURCE_APPLICABILITY_BOUNDARY_ID,
            request_formation.TARGET_BOUNDARY_ID,
            resolver.REQUEST_RESULT_CONTENT_IDENTITY,
            resolver.REQUEST_ADMISSION_RESULT_CONTENT_IDENTITY,
            resolver.STANDING_BASIS_ADMISSION_RESULT_CONTENT_IDENTITY,
            request_formation.SELECTED_SURFACE_CONTENT_IDENTITY,
            request_formation.TARGET_BOUNDARY_CONTRACT_CONTENT_IDENTITY,
            request_formation.HISTORICAL_BOUNDARY_RESULT_CONTENT_IDENTITY,
        }
        for value in collisions:
            envelope = copy.deepcopy(canonical)
            envelope["request_consumption_request_id"] = value
            with self.subTest(collision=value):
                result = _resolve(envelope)
                self.assert_outcome(result, resolver.OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["code"], resolver.CODE_IDENTITY_COLLISION)

        for value in ("sibling_consumption_request_002", "", " ", None, 1, []):
            envelope = copy.deepcopy(canonical)
            envelope["request_consumption_request_id"] = value
            with self.subTest(invalid_identity=value):
                self.assert_outcome(_resolve(envelope), resolver.OUTCOME_BLOCKED)

    def test_every_event_family_requires_exact_closed_material(self) -> None:
        representative_paths = (
            ("request_consumption_request_id",),
            ("declared_request_consumption_question", "request_consumption_type"),
            ("declared_request_consumption_question", "request_consumption_version"),
            ("declared_request_consumption_question", "request_consumption_question"),
            ("declared_request_consumption_question", "request_consumption_scope_family"),
            ("selected_consumption_boundary_result", "result_reference"),
            ("selected_consumption_boundary_result", "consumption_boundary_request_id"),
            ("selected_consumption_boundary_result", "passed_check_count"),
            ("selected_consumption_boundary_result", "failed_check_count"),
            ("selected_consumption_boundary_result", "review_exhausted"),
            ("selected_consumption_boundary_result", "one_shot_consumption_posture"),
            ("selected_request_formation_result", "result_reference"),
            ("selected_request_formation_result", "result_content_identity"),
            ("selected_request_formation_result", "outcome"),
            ("selected_request_formation_result", "recorded_request_object"),
            ("selected_request_admission_result", "result_reference"),
            ("selected_request_admission_result", "result_content_identity"),
            ("selected_request_admission_result", "request_admission_id"),
            ("selected_request_admission_result", "request_admitted"),
            ("selected_standing_basis_admission_result", "result_reference"),
            ("selected_standing_basis_admission_result", "result_content_identity"),
            ("selected_standing_basis_admission_result", "standing_basis_admission_id"),
            ("selected_surface_binding", "selected_surface_identity"),
            ("selected_surface_binding", "selected_surface_reference"),
            ("selected_surface_binding", "selected_surface_content_identity"),
            ("selected_surface_binding", "complete_pair_preserved"),
            ("selected_surface_binding", "source_lineage"),
            ("selected_surface_binding", "source_custody"),
            ("selected_surface_binding", "source_rank"),
            ("selected_surface_binding", "source_scope"),
            ("selected_source_applicability_binding", "source_applicability_boundary_id"),
            ("selected_source_applicability_binding", "source_applicability_outcome"),
            ("selected_source_applicability_binding", "admissible_future_route"),
            ("selected_target_boundary_binding", "target_boundary_id"),
            ("selected_target_boundary_binding", "target_boundary_contract_reference"),
            ("selected_target_boundary_binding", "target_boundary_contract_content_identity"),
            ("freshness_and_non_replay_posture", "request_freshness", "fresh_request_identity_declared"),
            ("freshness_and_non_replay_posture", "request_freshness", "historical_request_replayed"),
            ("one_shot_availability_posture", "one_future_consumption_review_only"),
        )
        for path in representative_paths:
            envelope = _canonical()
            _delete(envelope, path)
            with self.subTest(path=".".join(path)):
                self.assert_outcome(_resolve(envelope), resolver.OUTCOME_BLOCKED)

        list_members = (
            ("declared_request_consumption_question", "request_consumption_scope_family"),
            ("selected_surface_binding", "candidate_record_ids"),
            ("selected_surface_binding", "candidate_basis_ids"),
            ("selected_surface_binding", "source_lineage"),
        )
        for path in list_members:
            envelope = _canonical()
            parent, key = _parent_and_key(envelope, path)
            parent[key].pop()
            with self.subTest(truncated_list=".".join(path)):
                self.assert_outcome(_resolve(envelope), resolver.OUTCOME_BLOCKED)

    def test_substitution_pair_semantic_owner_route_and_replay_are_blocked(self) -> None:
        mutations = (
            (("selected_request_formation_result", "result_reference"), "substituted"),
            (("selected_request_admission_result", "request_admission_id"), "substituted"),
            (("selected_consumption_boundary_result", "consumption_boundary_request_id"), "substituted"),
            (("selected_standing_basis_admission_result", "standing_basis_admission_id"), "substituted"),
            (("selected_surface_binding", "selected_surface_identity"), "substituted"),
            (("selected_surface_binding", "complete_pair_preserved"), False),
            (("selected_surface_binding", "source_family"), "OTHER_FAMILY"),
            (("selected_surface_binding", "source_family_semantic_owner"), "GENERIC_RESOLVER"),
            (("selected_source_applicability_binding", "admissible_future_route"), "WIDENED_ROUTE"),
            (("selected_target_boundary_binding", "target_boundary_id"), "substituted"),
            (("freshness_and_non_replay_posture", "request_freshness", "historical_request_replayed"), True),
            (("freshness_and_non_replay_posture", "request_freshness", "historical_standing_basis_substituted"), True),
            (("one_shot_availability_posture", "one_future_consumption_review_only"), False),
        )
        for path, value in mutations:
            envelope = _canonical()
            _replace(envelope, path, value)
            with self.subTest(path=".".join(path), value=value):
                self.assert_outcome(_resolve(envelope), resolver.OUTCOME_BLOCKED)

        for key in (
            "candidate_a_independently_selected",
            "candidate_b_independently_selected",
            "candidate_pair_split",
            "candidate_pair_ranked",
            "semantic_ownership_transferred",
            "source_route_widened",
        ):
            envelope = _canonical()
            envelope["declared_non_claims"][key] = True
            with self.subTest(local_overreach=key):
                self.assert_outcome(_resolve(envelope), resolver.OUTCOME_BLOCKED)

    def test_all_source_non_claim_contracts_are_separate_exact_and_false(self) -> None:
        envelope = _canonical()
        self.assertEqual(len(resolver.NON_CLAIM_CONTRACTS), 8)
        maps = []
        for path, required in resolver.NON_CLAIM_CONTRACTS:
            current = envelope
            for key in path:
                current = current[key]
            maps.append(current)
            self.assertEqual(set(current), set(required), path)
            self.assertTrue(all(type(value) is bool and not value for value in current.values()))
        self.assertEqual(len({id(mapping) for mapping in maps}), len(maps))

        for path, required in resolver.NON_CLAIM_CONTRACTS:
            for defect in ("missing", "true", "non_boolean", "extra"):
                candidate = _canonical()
                current = candidate
                for key in path:
                    current = current[key]
                first = required[0]
                if defect == "missing":
                    del current[first]
                elif defect == "true":
                    current[first] = True
                elif defect == "non_boolean":
                    current[first] = 0
                else:
                    current["unknown_non_claim"] = False
                with self.subTest(path=".".join(path), defect=defect):
                    self.assert_outcome(_resolve(candidate), resolver.OUTCOME_BLOCKED)

    def test_missing_ordinary_basis_is_additional_and_invalid_basis_is_blocked(self) -> None:
        missing = _canonical()
        del missing["selected_consumption_boundary_result"]["checks"]
        result = _resolve(missing)
        self.assert_outcome(result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(result["block"]["code"], resolver.CODE_ADDITIONAL_BASIS)

        malformed_values = (None, {}, [], "checks")
        for value in malformed_values:
            envelope = _canonical()
            envelope["selected_consumption_boundary_result"]["checks"] = value
            with self.subTest(value=value):
                result = _resolve(envelope)
                self.assert_outcome(result, resolver.OUTCOME_BLOCKED)
                self.assertEqual(result["block"]["code"], resolver.CODE_ORDINARY_BASIS_INVALID)

        changed = _canonical()
        changed["selected_consumption_boundary_result"]["checks"][0]["passed"] = False
        result = _resolve(changed)
        self.assert_outcome(result, resolver.OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["code"], resolver.CODE_ORDINARY_BASIS_INVALID)

    def test_blocked_first_precedence_and_required_regressions(self) -> None:
        # Regression A: ordinary basis alone absent is additional basis.
        ordinary_only = _canonical()
        del ordinary_only["selected_consumption_boundary_result"]["checks"]
        self.assert_outcome(
            _resolve(ordinary_only), resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
        )

        # Regression B: any event-key defect dominates the same ordinary absence.
        event_and_ordinary = _canonical()
        del event_and_ordinary["selected_consumption_boundary_result"]["checks"]
        del event_and_ordinary["selected_target_boundary_binding"]["target_boundary_id"]
        self.assert_outcome(_resolve(event_and_ordinary), resolver.OUTCOME_BLOCKED)

        blocked_intent_and_ordinary = _canonical(resolver.INTENT_BLOCK)
        del blocked_intent_and_ordinary["selected_consumption_boundary_result"]["checks"]
        self.assert_outcome(_resolve(blocked_intent_and_ordinary), resolver.OUTCOME_BLOCKED)

        negative_and_ordinary = _canonical(resolver.INTENT_DO_NOT_RECORD)
        del negative_and_ordinary["selected_consumption_boundary_result"]["checks"]
        self.assert_outcome(
            _resolve(negative_and_ordinary),
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        )

    def test_same_event_is_deterministic_rerendering_not_event_multiplicity(self) -> None:
        envelope = _canonical()
        before = copy.deepcopy(envelope)
        first = _resolve(envelope)
        second = _resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["consumption_result"]["request_consumption_request_id"],
            second["consumption_result"]["request_consumption_request_id"],
        )
        self.assertFalse(first["non_claims"]["basis_consumed_twice"])
        self.assertFalse(first["non_claims"]["basis_exhausted_twice"])
        self.assertFalse(first["non_claims"]["second_consumption_created"])
        self.assertFalse(first["non_claims"]["replay_performed"])
        self.assertFalse(first["non_claims"]["distinct_consumption_attempt_authorized"])

        sibling = _canonical()
        sibling["request_consumption_request_id"] = (
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_request_002"
        )
        self.assert_outcome(_resolve(sibling), resolver.OUTCOME_BLOCKED)

    def test_result_projection_is_bounded_and_wrapper_is_not_consumption_object(self) -> None:
        result = _resolve(_canonical())
        consumption = result["consumption_result"]
        self.assertNotIn("checks", consumption)
        self.assertNotIn("block", consumption)
        self.assertNotIn("non_claims", consumption)
        self.assertNotIn("metadata", consumption)
        self.assertNotIn("what_remains_open", consumption)
        self.assertNotIn("selected_consumption_boundary_result", consumption)
        self.assertFalse(result["block"]["blocked"])
        self.assertEqual(result["failed_check_count"], 0)
        self.assertEqual(result["passed_check_count"], 3)
        self.assertEqual({item["check_id"] for item in result["checks"]}, resolver.CHECK_IDS)

        blocked = _resolve({})
        self.assert_outcome(blocked, resolver.OUTCOME_BLOCKED)
        for section in (
            "selected_consumption_boundary_result",
            "selected_request_formation_result",
            "selected_request_admission_result",
            "selected_standing_basis_admission_result",
            "selected_surface_binding",
            "selected_source_applicability_binding",
            "selected_target_boundary_binding",
            "freshness_and_non_replay_posture",
            "one_shot_availability_posture",
        ):
            self.assertIsNone(blocked[section])

    def test_resolver_is_pure_in_memory_and_does_not_resolve_upstream(self) -> None:
        upstream_calls = (
            patch.object(
                pre_consumption,
                "resolve_descendant_body_creation_boundary_request_admitted_standing_basis_consumption_boundary_v0_min_v2",
                side_effect=AssertionError("pre-consumption resolver invoked"),
            ),
            patch.object(
                request_formation,
                "resolve_descendant_body_creation_boundary_request_v0_min",
                side_effect=AssertionError("request-formation resolver invoked"),
            ),
            patch.object(
                request_admission,
                "resolve_descendant_body_creation_boundary_request_admission_v0_min_v2",
                side_effect=AssertionError("request-admission resolver invoked"),
            ),
            patch.object(
                standing_basis,
                "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
                side_effect=AssertionError("standing-basis resolver invoked"),
            ),
            patch.object(
                applicability,
                "resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2",
                side_effect=AssertionError("applicability resolver invoked"),
            ),
        )
        with patch("builtins.open", side_effect=AssertionError("filesystem access")), patch.object(
            hashlib, "sha256", side_effect=AssertionError("hashing invoked")
        ), upstream_calls[0], upstream_calls[1], upstream_calls[2], upstream_calls[3], upstream_calls[4]:
            envelope = _canonical()
            self.assert_outcome(_resolve(envelope), resolver.OUTCOME_CONSUMED)

        source = inspect.getsource(resolver)
        for forbidden in (
            "import os",
            "import json",
            "import hashlib",
            "from pathlib",
            "datetime",
            "glob(",
            "open(",
            "sha256(",
            "json.dump(",
        ):
            self.assertNotIn(forbidden, source)

    def test_v1_lineage_is_preserved_and_v2_is_the_governing_articulation(self) -> None:
        self.assertTrue(V1_SPEC.is_file())
        self.assertTrue(V2_SPEC.is_file())
        self.assertEqual(
            hashlib.sha256(V1_SPEC.read_bytes()).hexdigest(),
            "dce16ef3f84db2c4ba869d0114ac86d0a3c1036d67474d2a7909bfb1e5e6572f",
        )
        self.assertEqual(
            hashlib.sha256(V2_SPEC.read_bytes()).hexdigest(),
            "cd35cdbcd6f71ef3e74b17c52b0b66cd394f101639cb6cd2c6510e413ff79cb4",
        )
        self.assertIn(
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION",
            V2_SPEC.read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
