"""Dedicated adversarial tests for the V3 descendant-body-creation boundary."""

from __future__ import annotations

import builtins
import copy
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_creation_boundary_v0_min_v3 as resolver


def _remove_path(value: dict, path: str) -> None:
    parts = path.split(".")
    current = value
    for part in parts[:-1]:
        current = current[part]
    del current[parts[-1]]


def _set_path(value: dict, path: str, replacement) -> None:
    parts = path.split(".")
    current = value
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = replacement


class DescendantBodyCreationBoundaryV3Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict:
        return resolver.build_descendant_body_creation_boundary_v0_min_v3_envelope()

    def resolve(self, envelope):
        return resolver.resolve_descendant_body_creation_boundary_v0_min_v3(envelope)

    def assert_blocked(self, envelope, expected_code: str | None = None) -> dict:
        result = self.resolve(envelope)
        self.assertEqual(resolver.OUTCOME_BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(expected_code, result["block"]["code"])
        for check in result["descendant_body_creation_boundary_checks"]:
            if check["failure_code"] is not None:
                self.assertIn(check["failure_code"], resolver.BLOCK_CODES)
        return result

    def test_manifest_is_complete_exact_and_pairwise_disjoint(self) -> None:
        self.assertEqual(
            {"$::mapping_cardinality", "intent", "declared_current_question"},
            set(resolver.CONTROL_PATHS),
        )
        self.assertEqual(139, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        self.assertEqual(
            {
                f"ordinary_candidate_standing_basis.{key}"
                for key in (
                    "source_outcome",
                    "source_standing_result",
                    "candidate_standing_supported",
                    "candidate_standing_authorized",
                    "candidate_standing_created",
                    "candidate_a_standing_created",
                    "candidate_b_standing_created",
                    "candidate_standing_effect_applicability_recorded",
                    "candidate_standing_effect_applicable_to_declared_use",
                    "declared_use_exactly_matches_source_route",
                    "source_family_semantic_ownership_preserved",
                )
            },
            set(resolver.ORDINARY_CANDIDATE_STANDING_BASIS_PATHS),
        )
        expected_owner_paths = {
            f"required_non_claims.{owner}"
            for owner in (
                "request_formation_declared",
                "request_formation_result",
                "request_admission",
                "pre_consumption",
                "standing_basis_admission",
                "source_applicability",
                "source_family",
                "actual_consumption",
                "target_local",
            )
        }
        self.assertEqual(
            expected_owner_paths, set(resolver.REQUIRED_NON_CLAIM_OWNER_PATHS)
        )

        class_names = tuple(resolver.CLASS_PATHS)
        for index, left_name in enumerate(class_names):
            for right_name in class_names[index + 1 :]:
                with self.subTest(left=left_name, right=right_name):
                    self.assertTrue(
                        resolver.CLASS_PATHS[left_name].isdisjoint(
                            resolver.CLASS_PATHS[right_name]
                        )
                    )
        self.assertEqual(
            resolver.ALL_REQUIRED_PATHS,
            frozenset().union(*resolver.CLASS_PATHS.values()),
        )
        memberships = {
            path: sum(path in paths for paths in resolver.CLASS_PATHS.values())
            for path in resolver.ALL_REQUIRED_PATHS
        }
        self.assertTrue(memberships)
        self.assertEqual({1}, set(memberships.values()))

        broad_containers = {
            "constitutional_event_key",
            "constitutional_event_key.selected_surface",
            "ordinary_candidate_standing_basis",
            "required_non_claims",
        }
        self.assertTrue(broad_containers.isdisjoint(resolver.ALL_REQUIRED_PATHS))
        self.assertTrue(
            all(
                path.startswith("constitutional_event_key.")
                for path in resolver.CONSTITUTIONAL_EVENT_KEY_PATHS
            )
        )
        self.assertTrue(
            all(
                not path.startswith("required_non_claims.")
                for path in resolver.CONSTITUTIONAL_EVENT_KEY_PATHS
            )
        )

    def test_canonical_envelope_records_only_allowed_consideration(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        result = self.resolve(envelope)
        self.assertEqual(before, envelope)
        self.assertEqual(resolver.OUTCOME_ALLOWED, result["outcome"])
        self.assertEqual(
            resolver.BOUNDARY_RESULT_ALLOWED,
            result["descendant_body_creation_boundary_result"],
        )
        boundary = result["descendant_body_creation_boundary"]
        for field in resolver.POSITIVE_BOUNDARY_FIELDS:
            with self.subTest(field=field):
                self.assertIs(True, boundary[field])
        self.assertEqual(
            set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS), set(result["non_claims"])
        )
        self.assertEqual(73, len(result["non_claims"]))
        self.assertTrue(all(value is False for value in result["non_claims"].values()))
        self.assertTrue(result["descendant_body_creation_boundary"][
            "result_level_non_claims_canonical_false"
        ])

        self.assertEqual(
            "descendant_body_creation_boundary_request_001",
            result["selected_request_formation_result"]["request_id"],
        )
        self.assertEqual(
            "descendant_body_creation_boundary_request_admission_001",
            result["selected_request_admission_result"]["request_admission_id"],
        )
        consumption = result["selected_actual_consumption_result"]
        self.assertEqual(
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_request_001",
            consumption["request_consumption_request_id"],
        )
        self.assertEqual(
            "b50484a89aeb06e4e903b66e1a48d00f77cd12575a99af55c33ebcbe01f1abd5",
            consumption["result_sha256"],
        )
        for field in (
            "basis_consumed",
            "basis_exhausted",
            "one_shot_consumption_preserved",
            "one_shot_availability_closed",
            "consumption_token_closed",
            "selected_surface_complete_pair_preserved",
            "source_family_semantic_ownership_preserved",
        ):
            self.assertIs(True, consumption[field], field)
        self.assertEqual(
            "matter_bound_selected_surface_standing_basis_admission_001",
            result["selected_standing_basis_admission_result"][
                "standing_basis_admission_id"
            ],
        )
        self.assertTrue(result["selected_surface_binding"]["complete_pair_preserved"])
        self.assertEqual(
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
            result["selected_surface_binding"]["selected_surface_semantic_owner"],
        )
        self.assertEqual(
            "descendant_body_candidate_standing_effect_applicability_boundary_001",
            result["selected_source_applicability_binding"][
                "source_applicability_boundary_id"
            ],
        )
        self.assertEqual(
            resolver.DECLARED_MATTER_USE,
            result["selected_source_applicability_binding"]["declared_matter_use"],
        )
        self.assertEqual(
            resolver.BOUNDARY_ID,
            result["selected_target_boundary_binding"]["boundary_id"],
        )
        self.assertTrue(
            result["freshness_and_non_replay_posture"]["current"][
                "fresh_request_identity_declared"
            ]
        )
        self.assertFalse(
            result["freshness_and_non_replay_posture"][
                "historical_success_is_fresh_permission"
            ]
        )
        self.assertEqual(
            "9598594605e6ae20040cfea67cd6bff74263246aaa3139d0b356eef90b3752c0",
            result["freshness_and_non_replay_posture"][
                "historical_target_evidence_only"
            ]["result_sha256"],
        )
        self.assertEqual(
            set(resolver.EXPECTED_NON_CLAIM_KEYS),
            set(result["attributed_required_non_claims"]),
        )

    def test_fifteen_v3_deterministic_probes(self) -> None:
        probes = (
            (
                "constitutional_event_key.selected_surface.selected_surface_identity",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.selected_surface.selected_surface_result_reference",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.selected_surface.source_standing_contract_reference",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "ordinary_candidate_standing_basis.source_outcome",
                resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            ),
            (
                "ordinary_candidate_standing_basis.candidate_standing_supported",
                resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            ),
            (
                "constitutional_event_key.selected_surface.candidate_a_record_id",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.selected_surface.complete_pair_preserved",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.source_applicability.source_applicability_boundary_id",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.source_applicability."
                "source_applicability_result_reference",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "ordinary_candidate_standing_basis."
                "candidate_standing_effect_applicable_to_declared_use",
                resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            ),
            (
                "constitutional_event_key.source_applicability.declared_matter_use",
                resolver.OUTCOME_BLOCKED,
            ),
            ("constitutional_event_key.target.boundary_id", resolver.OUTCOME_BLOCKED),
            (
                "constitutional_event_key.target.boundary_scope",
                resolver.OUTCOME_BLOCKED,
            ),
            (
                "constitutional_event_key.target.target_boundary_contract_reference",
                resolver.OUTCOME_BLOCKED,
            ),
            ("intent", resolver.OUTCOME_BLOCKED),
        )
        self.assertEqual(15, len(probes))
        observed = []
        for path, expected_outcome in probes:
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                outcome = self.resolve(envelope)["outcome"]
                observed.append(outcome)
                self.assertEqual(expected_outcome, outcome)
        self.assertEqual(15, len(observed))

    def test_all_ordinary_members_distinguish_absence_from_invalid_presence(self) -> None:
        expected = resolver.EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS
        self.assertEqual(11, len(expected))
        for key, canonical_value in expected.items():
            path = f"ordinary_candidate_standing_basis.{key}"
            with self.subTest(key=key, posture="omitted"):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.resolve(envelope)
                self.assertEqual(
                    resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
                    result["outcome"],
                )
                self.assertEqual(
                    "CANDIDATE_STANDING_BASIS_ABSENT",
                    result["block"]["requirement_code"],
                )

            invalid_values = (
                ("WRONG_LITERAL", False)
                if isinstance(canonical_value, str)
                else (False, "true")
            )
            for invalid in invalid_values:
                with self.subTest(key=key, posture="invalid", invalid=invalid):
                    envelope = self.canonical()
                    _set_path(envelope, path, invalid)
                    self.assert_blocked(
                        envelope,
                        "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
                    )

        envelope = self.canonical()
        del envelope["ordinary_candidate_standing_basis"]["source_outcome"]
        del envelope["ordinary_candidate_standing_basis"][
            "candidate_standing_created"
        ]
        self.assertEqual(
            resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            self.resolve(envelope)["outcome"],
        )
        envelope = self.canonical()
        del envelope["ordinary_candidate_standing_basis"]
        self.assertEqual(
            resolver.OUTCOME_REQUIRES_CANDIDATE_STANDING,
            self.resolve(envelope)["outcome"],
        )

    def test_every_event_key_leaf_is_required_and_invalid_substitution_blocks(self) -> None:
        self.assertEqual(139, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(path=path, posture="missing"):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

        representative_mutations = {
            "constitutional_event_key.selected_surface.candidate_a_record_id": "candidate_a_substitute",
            "constitutional_event_key.selected_surface.candidate_a_basis_id": "candidate_a_basis_substitute",
            "constitutional_event_key.selected_surface.candidate_b_record_id": "candidate_b_substitute",
            "constitutional_event_key.selected_surface.candidate_b_basis_id": "candidate_b_basis_substitute",
            "constitutional_event_key.selected_surface.selected_surface_identity": "sibling_surface",
            "constitutional_event_key.selected_surface.selected_surface_family": "OTHER_FAMILY",
            "constitutional_event_key.selected_surface.selected_surface_semantic_owner": "OTHER_OWNER",
            "constitutional_event_key.selected_surface.complete_pair_preserved": False,
            "constitutional_event_key.selected_surface.candidate_records_remain_sibling": False,
            "constitutional_event_key.selected_surface.candidate_record_non_hierarchy_preserved": False,
            "constitutional_event_key.selected_surface.candidate_basis_non_hierarchy_preserved": False,
            "constitutional_event_key.selected_surface.source_custody_preserved": False,
            "constitutional_event_key.selected_surface.source_lineage_preserved": False,
            "constitutional_event_key.selected_surface.source_rank_preserved": False,
            "constitutional_event_key.selected_surface.source_scope_preserved": False,
            "constitutional_event_key.source_applicability.source_applicability_boundary_id": "other_applicability",
            "constitutional_event_key.source_applicability.source_applicability_outcome": "OTHER_OUTCOME",
            "constitutional_event_key.source_applicability.admissible_future_route": "WIDENED_ROUTE",
            "constitutional_event_key.target.boundary_id": "other_target",
            "constitutional_event_key.target.target_boundary_contract_sha256": "0" * 64,
        }
        for path, value in representative_mutations.items():
            with self.subTest(path=path, posture="substituted"):
                envelope = self.canonical()
                _set_path(envelope, path, value)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

    def test_required_non_claim_maps_are_exact_false_and_owner_separated(self) -> None:
        self.assertEqual(9, len(resolver.EXPECTED_NON_CLAIM_KEYS))
        self.assertEqual(73, len(resolver.TARGET_LOCAL_NON_CLAIM_KEYS))
        for owner, keys in resolver.EXPECTED_NON_CLAIM_KEYS.items():
            first_key = keys[0]
            with self.subTest(owner=owner, defect="missing_map"):
                envelope = self.canonical()
                del envelope["required_non_claims"][owner]
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(owner=owner, defect="missing_key"):
                envelope = self.canonical()
                del envelope["required_non_claims"][owner][first_key]
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(owner=owner, defect="extra_key"):
                envelope = self.canonical()
                envelope["required_non_claims"][owner]["unsupported_extra"] = False
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(owner=owner, defect="non_boolean"):
                envelope = self.canonical()
                envelope["required_non_claims"][owner][first_key] = 0
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(owner=owner, defect="true"):
                envelope = self.canonical()
                envelope["required_non_claims"][owner][first_key] = True
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        canonical_maps = self.canonical()["required_non_claims"]
        self.assertEqual(set(resolver.EXPECTED_NON_CLAIM_KEYS), set(canonical_maps))
        for owner, source_map in canonical_maps.items():
            with self.subTest(owner=owner, defect="separation"):
                self.assertEqual(
                    set(resolver.EXPECTED_NON_CLAIM_KEYS[owner]), set(source_map)
                )
                self.assertTrue(all(value is False for value in source_map.values()))
        event_paths = resolver.CONSTITUTIONAL_EVENT_KEY_PATHS
        self.assertTrue(
            all(
                f"required_non_claims.{owner}.{key}" not in event_paths
                for owner, keys in resolver.EXPECTED_NON_CLAIM_KEYS.items()
                for key in keys
            )
        )
        for owner in resolver.EXPECTED_NON_CLAIM_KEYS:
            self.assertIn(
                f"constitutional_event_key.non_claim_attribution.{owner}.owner",
                event_paths,
            )

    def test_control_unsupported_input_and_precedence(self) -> None:
        for envelope in (None, [], "not-a-mapping"):
            with self.subTest(non_mapping=type(envelope).__name__):
                self.assert_blocked(envelope, "REQUEST_NOT_MAPPING")

        mutations = (
            ("missing_intent", lambda value: value.pop("intent")),
            ("wrong_intent", lambda value: value.__setitem__("intent", "BLOCK_DESCENDANT_BODY_CREATION_BOUNDARY")),
            ("historical_negative_intent", lambda value: value.__setitem__("intent", "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_BOUNDARY")),
            ("missing_question", lambda value: value.pop("declared_current_question")),
            ("changed_question", lambda value: value.__setitem__("declared_current_question", resolver.DECLARED_CURRENT_QUESTION + " changed")),
            ("caller_outcome", lambda value: value.__setitem__("outcome", resolver.OUTCOME_ALLOWED)),
            ("unknown_root", lambda value: value.__setitem__("unknown", False)),
            ("unknown_event", lambda value: value["constitutional_event_key"]["target"].__setitem__("unknown", False)),
            ("unknown_ordinary", lambda value: value["ordinary_candidate_standing_basis"].__setitem__("unknown", True)),
            ("unknown_nonclaim_owner", lambda value: value["required_non_claims"].__setitem__("unknown_owner", {})),
            ("unknown_nonclaim_key", lambda value: value["required_non_claims"]["target_local"].__setitem__("unknown", False)),
        )
        for name, mutate in mutations:
            with self.subTest(name=name):
                envelope = self.canonical()
                mutate(envelope)
                self.assert_blocked(envelope)

        compound_cases = []
        envelope = self.canonical()
        del envelope["ordinary_candidate_standing_basis"]["source_outcome"]
        del envelope["constitutional_event_key"]["target"]["boundary_id"]
        compound_cases.append((envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"))
        envelope = self.canonical()
        del envelope["ordinary_candidate_standing_basis"]["source_outcome"]
        envelope["required_non_claims"]["target_local"]["runtime_created"] = True
        compound_cases.append((envelope, "REQUIRED_NON_CLAIM_INVALID"))
        envelope = self.canonical()
        del envelope["ordinary_candidate_standing_basis"]["source_outcome"]
        envelope["intent"] = "WRONG"
        compound_cases.append((envelope, "CONTROL_INVALID"))
        for envelope, code in compound_cases:
            with self.subTest(precedence=code):
                self.assert_blocked(envelope, code)

        self.assertEqual(
            resolver.OUTCOME_ALLOWED, self.resolve(self.canonical())["outcome"]
        )

    def test_same_event_closure_history_and_downstream_restraint(self) -> None:
        envelope = self.canonical()
        first = self.resolve(envelope)
        second = self.resolve(copy.deepcopy(envelope))
        self.assertEqual(first, second)
        self.assertFalse(
            first["current_consideration_event_binding"][
                "resolver_call_count_is_event_count"
            ]
        )
        self.assertTrue(
            first["current_consideration_event_binding"][
                "same_exact_binding_is_same_event"
            ]
        )
        self.assertNotIn("call_count", first)
        self.assertNotIn("event_count", first)

        closure_mutations = {
            "constitutional_event_key.actual_consumption.basis_consumed": False,
            "constitutional_event_key.actual_consumption.basis_exhausted": False,
            "constitutional_event_key.actual_consumption.one_shot_availability_closed": False,
            "constitutional_event_key.actual_consumption.consumption_token_closed": False,
            "constitutional_event_key.actual_consumption.consumed_request_basis_recorded": False,
            "constitutional_event_key.actual_consumption.outcome": "OTHER_OUTCOME",
            "constitutional_event_key.actual_consumption.result_sha256": "0" * 64,
        }
        for path, value in closure_mutations.items():
            with self.subTest(closure=path):
                changed = self.canonical()
                _set_path(changed, path, value)
                self.assert_blocked(changed, "CONSTITUTIONAL_EVENT_KEY_INVALID")

        event_mutations = {
            "constitutional_event_key.request.request_id": "descendant_body_creation_boundary_request_002",
            "constitutional_event_key.request.result_sha256": "1" * 64,
            "constitutional_event_key.historical_target.result_sha256": "2" * 64,
            "constitutional_event_key.historical_target.result_reference": (
                resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY["actual_consumption"][
                    "result_reference"
                ]
            ),
            "constitutional_event_key.actual_consumption.result_reference": (
                resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY["historical_target"][
                    "result_reference"
                ]
            ),
        }
        for path, value in event_mutations.items():
            with self.subTest(event=path):
                changed = self.canonical()
                _set_path(changed, path, value)
                self.assert_blocked(changed, "CONSTITUTIONAL_EVENT_KEY_INVALID")
        changed = self.canonical()
        del changed["constitutional_event_key"]["actual_consumption"]
        self.assert_blocked(changed, "CONSTITUTIONAL_EVENT_KEY_INVALID")

        downstream_false = (
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
            "source_applicability_created",
            "authority_created",
            "runtime_created",
        )
        for field in downstream_false:
            with self.subTest(downstream=field):
                self.assertIs(False, first["non_claims"][field])
        self.assertEqual(
            ["DESCENDANT_BODY_CREATION_OPERATION"],
            first["what_remains_open"]["open_items"],
        )
        self.assertFalse(first["what_remains_open"]["open_means_authorized"])
        self.assertFalse(first["what_remains_open"]["open_means_executed"])

    def test_purity_no_runtime_io_persistence_or_upstream_execution(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        with patch.object(
            builtins,
            "open",
            side_effect=AssertionError("resolver attempted filesystem access"),
        ):
            result = self.resolve(envelope)
            rebuilt = resolver.build_descendant_body_creation_boundary_v0_min_v3_envelope()
        self.assertEqual(before, envelope)
        self.assertEqual(before, rebuilt)
        self.assertEqual(resolver.OUTCOME_ALLOWED, result["outcome"])
        json.dumps(result, sort_keys=True)

        resolver_names = set(
            resolver.resolve_descendant_body_creation_boundary_v0_min_v3.__code__.co_names
        )
        module_symbols = set(vars(resolver))
        forbidden_names = {
            "open",
            "Path",
            "hashlib",
            "glob",
            "os",
            "subprocess",
            "socket",
            "requests",
            "write",
            "dump",
            "git",
        }
        self.assertTrue(forbidden_names.isdisjoint(resolver_names))
        self.assertTrue(forbidden_names.isdisjoint(module_symbols))
        self.assertFalse(
            any(name.startswith("write_") for name in module_symbols)
        )
        self.assertFalse(
            any(name.endswith("_from_path") for name in module_symbols)
        )
        self.assertFalse(
            any("operation_v0_min" in name and name.startswith("resolve_")
                for name in resolver_names)
        )
        self.assertEqual(
            {
                "intent",
                "declared_current_question",
                "constitutional_event_key",
                "ordinary_candidate_standing_basis",
                "required_non_claims",
            },
            set(rebuilt),
        )
        self.assertNotIn("$::mapping_cardinality", rebuilt)
        self.assertNotIn("outcome", rebuilt)


if __name__ == "__main__":
    unittest.main()
