"""Adversarial proof for bounded descendant-body boundary request formation.

The suite proves formation of request ``_001`` only.  It does not admit the
request, consume its referenced standing basis, authorize consideration,
invoke a boundary or operation, or create descendant-body standing.
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

import resolve_descendant_body_creation_boundary_request_v0_min as resolver


DELETE = object()


def _request() -> dict:
    return (
        resolver
        .build_declared_descendant_body_creation_boundary_request_v0_min_request()
    )


def _change(value: dict, path: tuple[str, ...], replacement=DELETE) -> dict:
    changed = copy.deepcopy(value)
    cursor = changed
    for key in path[:-1]:
        cursor = cursor[key]
    if replacement is DELETE:
        del cursor[path[-1]]
    else:
        cursor[path[-1]] = replacement
    return changed


class DescendantBodyCreationBoundaryRequestResolverTests(unittest.TestCase):
    maxDiff = None

    def assert_terminal(self, result: dict, outcome: str) -> None:
        self.assertEqual(result["outcome"], outcome)
        self.assertIn(result["outcome"], resolver.OUTCOME_FAMILY)
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        for check in result["checks"]:
            code = check["failure_code"]
            self.assertTrue(code is None or code in resolver.BLOCK_CODES)
        self.assertEqual(
            result["non_claims"],
            {key: False for key in resolver.REQUIRED_FALSE_NON_CLAIMS},
        )

    def assert_blocked(self, supplied: object) -> dict:
        result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            supplied
        )
        self.assert_terminal(result, resolver.OUTCOME_BLOCKED)
        self.assertTrue(result["block"]["blocked"])
        self.assertIsNone(result["recorded_request_object"])
        return result

    def test_public_contract_and_exact_canonical_builder(self) -> None:
        self.assertEqual(resolver.RESULT_VERSION, "0.1.0")
        self.assertEqual(
            resolver.RESOLVER_MODULE,
            "resolve_descendant_body_creation_boundary_request_v0_min",
        )
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_RECORDED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_NOT_RECORDED",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_REQUIRES_ADDITIONAL_BASIS",
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_BLOCKED",
            ),
        )
        supplied = _request()
        self.assertEqual(set(supplied), resolver.ENVELOPE_KEYS)
        request_object = supplied["request_object"]
        self.assertEqual(set(request_object), resolver.REQUEST_OBJECT_KEYS)
        self.assertEqual(
            request_object["request_id"],
            "descendant_body_creation_boundary_request_001",
        )
        self.assertEqual(
            request_object["request_type"],
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST",
        )
        self.assertEqual(request_object["request_version"], "0.1.0")
        self.assertEqual(
            request_object["request_scope"],
            "ONE_FRESH_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_"
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONLY",
        )
        self.assertEqual(
            request_object["request_intent"],
            "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST",
        )
        self.assertEqual(request_object["request_question"], resolver.REQUEST_QUESTION)
        self.assertEqual(
            request_object["declared_matter_use"],
            "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY",
        )

    def test_exact_request_records_without_rank_collapse(self) -> None:
        supplied = _request()
        result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            supplied
        )
        self.assert_terminal(result, resolver.OUTCOME_RECORDED)
        recorded = result["recorded_request_object"]
        self.assertEqual(recorded, supplied["request_object"])
        self.assertIsNot(recorded, supplied["request_object"])
        self.assertEqual(set(recorded), resolver.REQUEST_OBJECT_KEYS)
        self.assertNotEqual(
            recorded["request_id"], recorded["target_boundary"]["target_boundary_id"]
        )
        historical = supplied["historical_completed_lineage"]
        self.assertNotIn(recorded["request_id"], historical.values())
        self.assertEqual(
            {key for key, value in result["request_formation"].items() if value},
            set(resolver.ALLOWED_TRUE_RECORDED_FIELDS),
        )
        self.assertTrue(result["review_exhausted"])
        for key in (
            "request_admission_performed",
            "basis_consumption_performed",
            "consumption_token_closed",
            "boundary_consideration_performed",
            "invocation_performed",
            "execution_performed",
        ):
            self.assertIs(result[key], False)

    def test_target_contract_and_declared_use_are_exact(self) -> None:
        expected_target = {
            "target_boundary_id": "descendant_body_creation_boundary_001",
            "target_boundary_type": "DESCENDANT_BODY_CREATION_BOUNDARY",
            "target_boundary_version": "0.1.0",
            "target_boundary_scope": (
                "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY"
            ),
            "target_boundary_contract_reference": (
                "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_SPEC.md"
            ),
            "target_boundary_contract_content_identity": (
                "0b66c2419a1fe4e480192755858268aab0d7f8d109822a99fcf83e3d785be273"
            ),
            "target_boundary_admissible_future_route": (
                "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_"
                "DESCENDANT_BODY_CREATION_OPERATION_ONLY"
            ),
        }
        self.assertEqual(_request()["request_object"]["target_boundary"], expected_target)
        for key in expected_target:
            with self.subTest(target_field=key):
                supplied = _change(
                    _request(),
                    ("request_object", "target_boundary", key),
                    "INCOMPATIBLE_EXACT_TARGET",
                )
                result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
                    supplied
                )
                self.assert_terminal(result, resolver.OUTCOME_NOT_RECORDED)

        incompatible_use = _change(
            _request(),
            ("request_object", "declared_matter_use"),
            "ANOTHER_COMPLETE_BOUNDED_USE",
        )
        result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            incompatible_use
        )
        self.assert_terminal(result, resolver.OUTCOME_NOT_RECORDED)

    def test_exact_admission_identity_reference_and_use_are_required(self) -> None:
        basis = _request()["request_object"]["intended_admitted_standing_basis"]
        expected = {
            "standing_basis_admission_id": (
                "matter_bound_selected_surface_standing_basis_admission_001"
            ),
            "standing_basis_admission_type": (
                "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
            ),
            "standing_basis_admission_version": "0.1.0",
            "standing_basis_admission_scope": (
                "ONE_SELECTED_SURFACE_ONE_EXPLICIT_DOWNSTREAM_MATTER_USE_"
                "ONE_EXACT_FAMILY_OWNED_STANDING_BASIS_ONLY"
            ),
            "standing_basis_admission_outcome": (
                "SELECTED_SURFACE_STANDING_BASIS_ADMITTED"
            ),
            "standing_basis_admission_failed_check_count": 0,
            "standing_basis_admission_review_exhausted": True,
            "standing_basis_admission_reference": (
                "artifacts/matter_bound_selected_surface_standing_basis_admission_"
                "v0_min/matter_bound_selected_surface_standing_basis_admission_001__"
                "matter_bound_selected_surface_standing_basis_admission_v0_min_"
                "result.json"
            ),
            "standing_basis_admission_content_identity": (
                "e53cb86c1b76eec212bbd90c1247da7adc0cd4c4cc26da82b4a3edd2c4aa639f"
            ),
            "standing_basis_admission_declared_use": resolver.DECLARED_MATTER_USE,
        }
        for key, value in expected.items():
            self.assertEqual(basis[key], value)
            with self.subTest(admission_field=key):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "intended_admitted_standing_basis", key),
                        "FALSELY_ATTRIBUTED_ADMISSION",
                    )
                )

        multiple = _change(
            _request(),
            ("request_object", "intended_admitted_standing_basis"),
            [basis, basis],
        )
        self.assert_blocked(multiple)

    def test_selected_surface_remains_one_exact_complete_pair(self) -> None:
        selected = _request()["request_object"]["intended_admitted_standing_basis"][
            "selected_surface"
        ]
        self.assertEqual(
            selected,
            {
                "selected_surface_identity": (
                    "descendant_body_candidate_standing_operation_001"
                ),
                "selected_surface_type": (
                    "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
                ),
                "selected_surface_version": "0.1.0",
                "selected_surface_scope": (
                    "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
                ),
                "selected_surface_reference": (
                    "artifacts/integrity_host_v0_min_coexistence_"
                    "descendant_body_candidate_standing_operation_v0_min/"
                    "descendant_body_candidate_standing_operation_001__"
                    "candidate_standing_operation_v0_min_result.json"
                ),
                "selected_surface_content_identity": (
                    "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
                ),
                "complete_pair_preserved": True,
                "source_family": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
                "source_family_semantic_owner": (
                    "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
                ),
                "candidate_record_ids": [
                    "descendant_body_basis_candidate_a_001",
                    "descendant_body_basis_candidate_b_001",
                ],
                "candidate_basis_ids": [
                    "descendant_body_basis_candidate_a_001__"
                    "motion_side_admissible_variation_basis",
                    "descendant_body_basis_candidate_b_001__"
                    "regulation_side_admissibility_bounds_basis",
                ],
            },
        )
        hostile = (
            ("selected_surface_identity", "SUBSTITUTED_SURFACE"),
            ("selected_surface_type", "NORMALIZED_STANDING_SURFACE"),
            ("selected_surface_version", "latest"),
            ("selected_surface_scope", "WIDENED_SCOPE"),
            ("selected_surface_reference", "latest.json"),
            ("selected_surface_content_identity", "runtime-hash"),
            ("complete_pair_preserved", False),
            ("source_family", "GENERIC_STANDING_FAMILY"),
            ("source_family_semantic_owner", "REQUEST_RESOLVER"),
            ("candidate_record_ids", [selected["candidate_record_ids"][0]]),
            ("candidate_record_ids", [selected["candidate_record_ids"][1]]),
            ("candidate_basis_ids", [selected["candidate_basis_ids"][0]]),
            ("candidate_basis_ids", [selected["candidate_basis_ids"][1]]),
        )
        for key, value in hostile:
            with self.subTest(selected_surface_mutation=key, value=value):
                self.assert_blocked(
                    _change(
                        _request(),
                        (
                            "request_object",
                            "intended_admitted_standing_basis",
                            "selected_surface",
                            key,
                        ),
                        value,
                    )
                )

    def test_source_owned_contract_applicability_and_binding_are_exact(self) -> None:
        basis = _request()["request_object"]["intended_admitted_standing_basis"]
        expected = {
            "source_standing_contract_reference": (
                "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
            ),
            "source_standing_contract_content_identity": (
                "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
            ),
            "source_standing_result": "CANDIDATE_STANDING_SUPPORTED",
            "source_applicability_artifact_reference": (
                "artifacts/descendant_body_candidate_standing_effect_"
                "applicability_boundary_v0_min_v2/descendant_body_candidate_"
                "standing_effect_applicability_boundary_001__descendant_body_"
                "candidate_standing_effect_applicability_boundary_v0_min_v2_"
                "result.json"
            ),
            "source_applicability_boundary_id": (
                "descendant_body_candidate_standing_effect_applicability_boundary_001"
            ),
            "source_applicability_outcome": (
                "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
            ),
            "source_route": resolver.DECLARED_MATTER_USE,
        }
        for key, value in expected.items():
            self.assertEqual(basis[key], value)
            with self.subTest(source_field=key):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "intended_admitted_standing_basis", key),
                        "SEMANTICALLY_REINTERPRETED_SOURCE",
                    )
                )

        canonical_admission = (
            resolver._admission
            .build_declared_matter_bound_selected_surface_standing_basis_admission_v0_min_request()
        )
        self.assertEqual(
            basis["source_applicability_result"],
            canonical_admission["source_applicability_result"],
        )
        self.assertEqual(
            basis["admission_level_binding"],
            canonical_admission["admission_level_binding"],
        )

    def test_lineage_custody_rank_scope_and_binding_mutation_block(self) -> None:
        hostile_paths = (
            (
                "source_applicability_result",
                "source_lineage",
            ),
            (
                "source_applicability_result",
                "source_custody",
            ),
            (
                "source_applicability_result",
                "source_rank",
            ),
            (
                "source_applicability_result",
                "source_scope",
            ),
            ("source_applicability_result", "source_binding"),
            ("source_applicability_result", "cross_object_binding"),
            ("admission_level_binding", "source_lineage"),
            ("admission_level_binding", "source_custody"),
            ("admission_level_binding", "source_rank"),
            ("admission_level_binding", "source_scope"),
        )
        for suffix in hostile_paths:
            with self.subTest(carried_material=suffix):
                self.assert_blocked(
                    _change(
                        _request(),
                        (
                            "request_object",
                            "intended_admitted_standing_basis",
                            *suffix,
                        ),
                        {"normalized": True},
                    )
                )

        for suffix in hostile_paths:
            with self.subTest(missing_carried_material=suffix):
                supplied = _change(
                    _request(),
                    (
                        "request_object",
                        "intended_admitted_standing_basis",
                        *suffix,
                    ),
                )
                result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
                    supplied
                )
                self.assert_terminal(
                    result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                )

    def test_basis_reference_posture_blocks_consumption_and_reuse(self) -> None:
        expected = {
            "admitted_standing_basis_referenced": True,
            "admitted_standing_basis_intended_for_later_separate_consumption_review": True,
            "admitted_standing_basis_consumed": False,
            "admitted_standing_basis_exhausted": False,
            "consumption_token_closed": False,
            "consumption_authorized": False,
            "basis_reuse_permission_created": False,
        }
        self.assertEqual(
            _request()["request_object"]["basis_reference_posture"], expected
        )
        for key, value in expected.items():
            with self.subTest(reference_posture=key):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "basis_reference_posture", key),
                        not value,
                    )
                )

    def test_freshness_is_structural_and_historical_lineage_is_locked(self) -> None:
        freshness = {
            "fresh_request_identity_declared": True,
            "request_identity_distinct_from_target_boundary": True,
            "request_identity_distinct_from_historical_completed_lineage": True,
            "historical_request_identity_reused": False,
            "historical_request_material_reused": False,
            "historical_request_reopened": False,
            "historical_request_mutated": False,
            "historical_request_replayed": False,
            "historical_standing_basis_substituted": False,
            "historical_success_treated_as_fresh_permission": False,
        }
        supplied = _request()
        self.assertEqual(supplied["request_object"]["freshness_and_non_replay"], freshness)
        self.assertEqual(
            supplied["historical_completed_lineage"],
            {
                "historical_boundary_result_reference": (
                    "artifacts/integrity_host_v0_min_coexistence_"
                    "descendant_body_creation_boundary_v0_min/"
                    "descendant_body_creation_boundary_001__"
                    "descendant_body_creation_boundary_v0_min_result.json"
                ),
                "historical_boundary_result_content_identity": (
                    "9598594605e6ae20040cfea67cd6bff74263246aaa3139d0b356eef90b3752c0"
                ),
                "historical_boundary_outcome": (
                    "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"
                ),
                "historical_boundary_result": (
                    "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"
                ),
            },
        )
        for key, value in freshness.items():
            with self.subTest(freshness_field=key):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "freshness_and_non_replay", key),
                        not value,
                    )
                )
        for key in supplied["historical_completed_lineage"]:
            with self.subTest(historical_lock=key):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("historical_completed_lineage", key),
                        "REUSED_OR_REOPENED_HISTORY",
                    )
                )

        for reused_identity in (
            resolver.TARGET_BOUNDARY_ID,
            resolver.HISTORICAL_BOUNDARY_RESULT,
        ):
            with self.subTest(reused_identity=reused_identity):
                self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "request_id"),
                        reused_identity,
                    )
                )
        historical_substitution = _change(
            _request(),
            ("request_object",),
            _request()["historical_completed_lineage"],
        )
        self.assert_blocked(historical_substitution)

    def test_missing_exact_basis_requires_additional_basis(self) -> None:
        paths = (
            ("request_object", "request_id"),
            ("request_object", "target_boundary", "target_boundary_contract_reference"),
            (
                "request_object",
                "target_boundary",
                "target_boundary_contract_content_identity",
            ),
            (
                "request_object",
                "intended_admitted_standing_basis",
                "standing_basis_admission_reference",
            ),
            (
                "request_object",
                "intended_admitted_standing_basis",
                "standing_basis_admission_content_identity",
            ),
            (
                "request_object",
                "intended_admitted_standing_basis",
                "selected_surface",
                "selected_surface_content_identity",
            ),
            (
                "request_object",
                "intended_admitted_standing_basis",
                "admission_level_binding",
            ),
            ("request_object", "declared_non_claims", "request_admitted"),
            ("historical_completed_lineage", "historical_boundary_result_reference"),
        )
        for path in paths:
            with self.subTest(missing=path):
                result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
                    _change(_request(), path)
                )
                self.assert_terminal(
                    result, resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
                )

        self.assert_terminal(
            resolver.resolve_descendant_body_creation_boundary_request_v0_min(None),
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        )

    def test_malformed_ambiguous_and_mixed_schema_inputs_block(self) -> None:
        cases = (
            [],
            _change(_request(), ("request_object",), []),
            _change(_request(), ("request_object", "request_id"), [resolver.REQUEST_ID]),
            _change(
                _request(),
                ("request_object", "target_boundary"),
                [
                    _request()["request_object"]["target_boundary"],
                    _request()["request_object"]["target_boundary"],
                ],
            ),
        )
        for case in cases:
            with self.subTest(case=type(case).__name__):
                self.assert_blocked(case)

        unknown_request_field = _request()
        unknown_request_field["request_object"]["timestamp"] = "2026-08-09"
        self.assert_blocked(unknown_request_field)
        unknown_envelope_field = _request()
        unknown_envelope_field["latest_repository_selection"] = True
        self.assert_blocked(unknown_envelope_field)
        admission_claim = _request()
        admission_claim["request_object"]["request_admitted"] = True
        self.assert_blocked(admission_claim)

    def test_every_required_non_claim_is_present_false_and_flips_block(self) -> None:
        supplied = _request()
        declared = supplied["request_object"]["declared_non_claims"]
        self.assertEqual(set(declared), set(resolver.REQUIRED_FALSE_NON_CLAIMS))
        self.assertTrue(all(value is False for value in declared.values()))
        self.assertEqual(len(declared), len(resolver.REQUIRED_FALSE_NON_CLAIMS))

        for key in resolver.REQUIRED_FALSE_NON_CLAIMS:
            with self.subTest(flipped_non_claim=key):
                result = self.assert_blocked(
                    _change(
                        _request(),
                        ("request_object", "declared_non_claims", key),
                        True,
                    )
                )
                self.assertIs(result["non_claims"][key], False)
                self.assertTrue(
                    all(value is False for value in result["non_claims"].values())
                )

        extra = _request()
        extra["request_object"]["declared_non_claims"]["generic_permission"] = False
        self.assert_blocked(extra)

    def test_request_object_and_resolver_result_remain_distinct(self) -> None:
        result = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            _request()
        )
        request_object = result["recorded_request_object"]
        forbidden = {
            "outcome",
            "block",
            "checks",
            "summary",
            "metadata",
            "admission_decision",
            "consumption_result",
            "boundary_result",
            "authorization_token",
            "invocation_token",
            "operation_result",
            "receipt",
        }
        self.assertTrue(forbidden.isdisjoint(request_object))
        self.assertIn("outcome", result)
        self.assertIn("checks", result)
        self.assertIn("block", result)
        self.assertEqual(set(request_object), resolver.REQUEST_OBJECT_KEYS)

    def test_resolution_is_deterministic_and_does_not_mutate_input(self) -> None:
        supplied = _request()
        before = copy.deepcopy(supplied)
        first = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            supplied
        )
        second = resolver.resolve_descendant_body_creation_boundary_request_v0_min(
            supplied
        )
        self.assertEqual(supplied, before)
        self.assertEqual(first, second)
        first["recorded_request_object"]["request_id"] = "MUTATED_RESULT_COPY"
        self.assertEqual(supplied, before)

    def test_resolver_is_filesystem_hash_write_and_upstream_resolver_free(self) -> None:
        source = inspect.getsource(resolver)
        forbidden_source_fragments = (
            "pathlib",
            "glob(",
            "os.walk",
            "os.listdir",
            "hashlib",
            "sha256(",
            "json.dump",
            "write_text",
            "write_bytes",
            "resolve_descendant_body_creation_boundary_v0_min(",
            "generic_request_framework",
            "cross_family_request_adapter",
            "workflow_engine",
        )
        for fragment in forbidden_source_fragments:
            with self.subTest(forbidden_source=fragment):
                self.assertNotIn(fragment, source.lower())

        supplied = _request()
        with patch("builtins.open", side_effect=AssertionError("filesystem access")):
            with patch.object(
                hashlib,
                "sha256",
                side_effect=AssertionError("runtime hashing"),
            ):
                with patch.object(
                    resolver._admission,
                    "resolve_matter_bound_selected_surface_standing_basis_admission_v0_min",
                    side_effect=AssertionError("admission resolver invoked"),
                ):
                    with patch.object(
                        resolver._admission._source,
                        "resolve_descendant_body_candidate_standing_effect_"
                        "applicability_boundary_v0_min_v2",
                        side_effect=AssertionError("applicability resolver invoked"),
                    ):
                        result = (
                            resolver
                            .resolve_descendant_body_creation_boundary_request_v0_min(
                                supplied
                            )
                        )
        self.assert_terminal(result, resolver.OUTCOME_RECORDED)


if __name__ == "__main__":
    unittest.main()
