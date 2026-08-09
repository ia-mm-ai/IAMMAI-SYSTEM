"""Adversarial proof for the current-line PRESENCE_BOUNDARY V2 resolver."""

from __future__ import annotations

import ast
from copy import deepcopy
import inspect
from pathlib import Path
import sys
import types
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_presence_boundary_v0_min_v2 as resolver


def _parts(path: str) -> list[str]:
    return path.split(".")


def _remove_path(value: dict[str, object], path: str) -> None:
    current = value
    parts = _parts(path)
    for part in parts[:-1]:
        current = current[part]  # type: ignore[assignment,index]
    del current[parts[-1]]


def _set_path(value: dict[str, object], path: str, replacement: object) -> None:
    current = value
    parts = _parts(path)
    for part in parts[:-1]:
        current = current[part]  # type: ignore[assignment,index]
    current[parts[-1]] = replacement


def _get_path(value: dict[str, object], path: str) -> object:
    current: object = value
    for part in _parts(path):
        current = current[part]  # type: ignore[index]
    return current


def _wrong_value(value: object) -> object:
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1  # type: ignore[operator]
    if value is None:
        return "NOT_NONE"
    if isinstance(value, str):
        return f"{value}__CHANGED"
    raise AssertionError(f"no strict mutation for {value!r}")


def _all_mapping_keys(value: object) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        keys.update(value)
        for child in value.values():
            keys.update(_all_mapping_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_all_mapping_keys(child))
    return keys


def _all_code_names(*functions: object) -> set[str]:
    pending = [function.__code__ for function in functions]  # type: ignore[attr-defined]
    names: set[str] = set()
    while pending:
        code = pending.pop()
        names.update(code.co_names)
        pending.extend(
            item for item in code.co_consts if isinstance(item, types.CodeType)
        )
    return names


class PresenceBoundaryV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_presence_boundary_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_presence_boundary_v0_min_v2(envelope)

    def assert_no_positive_boundary(self, result: dict[str, object]) -> None:
        boundary = result["presence_boundary"]
        for field in resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS:
            self.assertIs(boundary[field], False, field)

    def assert_blocked(
        self,
        envelope: object,
        *,
        issue_path: str | None = None,
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        self.assertFalse(result["block"]["requires_lapse_operation"])
        if issue_path is not None:
            self.assertEqual(result["block"]["issue_path"], issue_path)
        self.assert_no_positive_boundary(result)
        return result

    def assert_requires(
        self,
        envelope: object,
        missing_paths: list[str],
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(
            result["outcome"],
            resolver.OUTCOME_REQUIRES_LAPSE_OPERATION,
        )
        self.assertEqual(
            result["presence_boundary"]["presence_boundary_result"],
            resolver.RESULT_REQUIRES_LAPSE_OPERATION,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_lapse_operation"])
        self.assertEqual(
            result["ordinary_relation_lapse_basis_review"]["missing_paths"],
            missing_paths,
        )
        self.assert_no_positive_boundary(result)
        return result

    def assert_allowed(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(
            result["presence_boundary"]["presence_boundary_result"],
            resolver.RESULT_ALLOWED,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_lapse_operation"])
        self.assertEqual(result["failed_check_count"], 0)
        return result

    def assert_exact_false_map(
        self,
        map_name: str,
        expected_keys: tuple[str, ...],
    ) -> None:
        base_path = f"required_non_claims.{map_name}"

        envelope = self.canonical()
        del envelope["required_non_claims"][map_name]
        self.assert_blocked(envelope, issue_path=base_path)

        for value in (None, "false", 0, []):
            with self.subTest(map_name=map_name, case="non_mapping", value=value):
                envelope = self.canonical()
                envelope["required_non_claims"][map_name] = value
                self.assert_blocked(envelope, issue_path=base_path)

        envelope = self.canonical()
        envelope["required_non_claims"][map_name]["unknown"] = False
        self.assert_blocked(envelope, issue_path=f"{base_path}.unknown")

        for key in expected_keys:
            path = f"{base_path}.{key}"
            with self.subTest(map_name=map_name, case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)
            with self.subTest(map_name=map_name, case="true", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, True)
                self.assert_blocked(envelope, issue_path=path)

        representative = f"{base_path}.{expected_keys[0]}"
        for value in ("false", 0, None):
            with self.subTest(
                map_name=map_name,
                case="representative_non_boolean",
                value=value,
            ):
                envelope = self.canonical()
                _set_path(envelope, representative, value)
                self.assert_blocked(envelope, issue_path=representative)

        self.assertEqual(
            set(self.canonical()["required_non_claims"][map_name]),
            set(expected_keys),
        )

    def test_manifest_cardinality_membership_and_disjointness(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 422)
        self.assertEqual(len(resolver.SOURCE_OPERATION_EVENT_KEY_PATHS), 347)
        self.assertEqual(
            len(resolver.ORDINARY_RELATION_LAPSE_BASIS_PATHS),
            7,
        )

        expected_counts = {
            "source_relation_boundary": 8,
            "source_relation_operation": 68,
            "source_reversibility_boundary": 86,
            "source_reversibility_operation": 96,
            "source_lapse_boundary": 97,
            "source_lapse_operation": 107,
            "boundary_local": 110,
        }
        for name, count in expected_counts.items():
            paths = {
                path
                for path in resolver.REQUIRED_NON_CLAIM_PATHS
                if path.startswith(f"required_non_claims.{name}.")
            }
            self.assertEqual(len(paths), count, name)
        self.assertEqual(len(resolver.SOURCE_REQUIRED_NON_CLAIM_PATHS), 462)
        self.assertEqual(
            len(resolver.PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS),
            110,
        )
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 572)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 1004)
        self.assertEqual(462 + 110, 572)
        self.assertEqual(3 + 422 + 7 + 572, 1004)

        explicit = (
            resolver.CONTROL_PATHS,
            resolver.CONSTITUTIONAL_EVENT_KEY_PATHS,
            resolver.ORDINARY_RELATION_LAPSE_BASIS_PATHS,
            resolver.SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
            resolver.SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_PATHS,
            resolver.SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
            resolver.SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_PATHS,
            resolver.SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
            resolver.SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_PATHS,
            resolver.PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS,
        )
        for paths in explicit:
            self.assertEqual(len(paths), len(set(paths)))
        classes = tuple(resolver.CLASS_PATHS.values())
        for index, paths in enumerate(classes):
            for other in classes[index + 1 :]:
                self.assertFalse(paths & other)
        self.assertEqual(
            frozenset().union(*classes),
            resolver.ALL_REQUIRED_PATHS,
        )

        parents: set[str] = set()
        for path in resolver.ALL_REQUIRED_PATHS:
            parts = path.split(".")
            parents.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parents & resolver.ALL_REQUIRED_PATHS)

        expected_all = {
            "$::mapping_cardinality",
            "intent",
            "boundary_question",
            *resolver._leaf_paths(
                resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
                "constitutional_event_key",
            ),
            *resolver.ORDINARY_RELATION_LAPSE_BASIS_PATHS,
            *resolver.REQUIRED_NON_CLAIM_PATHS,
        }
        self.assertEqual(expected_all, resolver.ALL_REQUIRED_PATHS)
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "PRESENCE_BOUNDARY_BLOCKED",
                "PRESENCE_BOUNDARY_REQUIRES_LAPSE_OPERATION",
                "PRESENCE_BOUNDARY_ALLOWED",
            ),
        )
        self.assertNotIn(
            "PRESENCE_BOUNDARY_NOT_RECORDED",
            resolver.OUTCOME_FAMILY,
        )

    def test_canonical_builder_and_allowed_result(self) -> None:
        envelope = self.canonical()
        self.assertEqual(
            set(envelope),
            {
                "intent",
                "boundary_question",
                "constitutional_event_key",
                "ordinary_relation_lapse_basis",
                "required_non_claims",
            },
        )
        self.assertNotIn("$::mapping_cardinality", envelope)
        self.assertEqual(envelope["intent"], "RECORD_PRESENCE_BOUNDARY")
        self.assertEqual(envelope["boundary_question"], resolver.BOUNDARY_QUESTION)
        for forbidden in ("outcome", "result", "checks", "block", "summary"):
            self.assertNotIn(forbidden, envelope)

        result = self.assert_allowed(envelope)
        boundary = result["presence_boundary"]
        true_booleans = {
            key for key, value in boundary.items() if value is True
        }
        self.assertEqual(
            true_booleans,
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS),
        )
        self.assertEqual(len(true_booleans), 6)
        self.assertNotIn("relation_pair_referenced", boundary)
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_evaluation_performed",
            "presence_operation_invoked",
            "presence_operation_executed",
            "presence_operation_completed",
        ):
            self.assertIs(boundary[field], False, field)
        lapse_reference = result["presence_boundary_material"][
            "relation_lapse_operation_reference"
        ]
        for field in resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS[3:]:
            self.assertIs(lapse_reference[field], True, field)
        self.assertEqual(
            result["downstream_stopping_point"]["next_separately_bounded_rank"],
            "PRESENCE_OPERATION",
        )

    def test_every_event_leaf_omission_and_representative_mutation_blocks(self) -> None:
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 422)
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

        cases = {
            "constitutional_event_key.target.boundary_id": "presence_boundary_002",
            "constitutional_event_key.target.boundary_scope": "WIDENED",
            "constitutional_event_key.target.boundary_contract_reference": "spec/OTHER.md",
            "constitutional_event_key.target.boundary_contract_sha256": "0" * 64,
            "constitutional_event_key.current_lapse_operation_result.result_reference": "artifacts/other.json",
            "constitutional_event_key.current_lapse_operation_result.result_sha256": "1" * 64,
            "constitutional_event_key.current_lapse_operation_result.result_version": "0.1.0",
            "constitutional_event_key.current_lapse_operation_result.resolver_module": "other",
            "constitutional_event_key.current_lapse_operation_result.blocked": True,
            "constitutional_event_key.current_lapse_operation_result.relation_record_persistence.relation_occurrence_remains_addressable": False,
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.admissible_future_route": "OTHER",
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.presence_boundary_consideration": "SELECTED",
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.relation_dissolution_boundary_consideration": "CLOSED",
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.current_branch_selected": True,
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.presence_boundary_selected": True,
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.relation_dissolution_boundary_selected": True,
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.branch_choice_created": True,
            "constitutional_event_key.current_lapse_operation_result.downstream_stopping_point.historical_realized_route": "OTHER",
            "constitutional_event_key.source_operation.operation_id": "relation_lapse_operation_002",
            "constitutional_event_key.source_operation_event_key.source_boundary.boundary_id": "relation_lapse_boundary_002",
            "constitutional_event_key.boundary_event.relation_lapse_id": "relation_lapse_002",
            "constitutional_event_key.boundary_event.relation_id": "relation_002",
            "constitutional_event_key.boundary_event.first_crossing_a_id": "other",
            "constitutional_event_key.boundary_event.first_crossing_b_id": "other",
            "constitutional_event_key.boundary_event.descendant_body_a_id": "other",
            "constitutional_event_key.boundary_event.descendant_body_b_id": "other",
            "constitutional_event_key.boundary_event.persistent_creation_operation_id": "other",
            "constitutional_event_key.boundary_event.fresh_creation_operation_request_id": "other",
            "constitutional_event_key.source_operation_event_key.source_boundary_event_key.source_operation_event_key.source.selected_surface_semantic_owner": "OTHER",
            "constitutional_event_key.freshness.current_boundary_event_identity_declared": False,
            "constitutional_event_key.historical_boundary.result_sha256": "2" * 64,
            "constitutional_event_key.historical_boundary.outcome": "OTHER",
            "constitutional_event_key.historical_boundary.boundary_result": "OTHER",
            "constitutional_event_key.non_claim_attribution.boundary_local.owner": "OTHER",
        }
        for path, replacement in cases.items():
            with self.subTest(case="changed", path=path):
                self.assertIn(path, resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)
                envelope = self.canonical()
                _set_path(envelope, path, replacement)
                self.assert_blocked(envelope, issue_path=path)

    def test_ordinary_basis_omission_malformed_and_naming_lock(self) -> None:
        self.assertEqual(
            resolver.RESULT_REQUIRES_LAPSE_OPERATION,
            "REQUIRES_RELATION_LAPSE_OPERATION",
        )
        for path in sorted(resolver.ORDINARY_RELATION_LAPSE_BASIS_PATHS):
            with self.subTest(case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_requires(envelope, [path])

            expected = _get_path(self.canonical(), path)
            candidates = [_wrong_value(expected), None, 1]
            if type(expected) is bool:
                candidates.extend(("true", False))
            else:
                candidates.append("WRONG_ENUM")
            for replacement in candidates:
                with self.subTest(
                    case="contradictory",
                    path=path,
                    replacement=replacement,
                ):
                    envelope = self.canonical()
                    _set_path(envelope, path, replacement)
                    result = self.assert_blocked(envelope, issue_path=path)
                    self.assertNotEqual(
                        result["outcome"],
                        resolver.OUTCOME_REQUIRES_LAPSE_OPERATION,
                    )

        envelope = self.canonical()
        envelope["ordinary_relation_lapse_basis"]["unknown"] = True
        self.assert_blocked(
            envelope,
            issue_path="ordinary_relation_lapse_basis.unknown",
        )
        for value in (None, [], "basis"):
            envelope = self.canonical()
            envelope["ordinary_relation_lapse_basis"] = value
            self.assert_blocked(
                envelope,
                issue_path="ordinary_relation_lapse_basis",
            )

    def test_all_attributed_non_claim_maps_are_exact_and_exhaustive(self) -> None:
        families = (
            (
                "source_relation_boundary",
                resolver.SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "source_relation_operation",
                resolver.SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "source_reversibility_boundary",
                resolver.SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "source_reversibility_operation",
                resolver.SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "source_lapse_boundary",
                resolver.SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "source_lapse_operation",
                resolver.SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_KEYS,
            ),
            (
                "boundary_local",
                resolver.PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS,
            ),
        )
        for map_name, keys in families:
            with self.subTest(map_name=map_name):
                self.assert_exact_false_map(map_name, keys)

        local = set(resolver.PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS)
        self.assertEqual(len(local), 110)
        self.assertFalse(
            local & set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
        )
        self.assertNotIn("presence_evaluation_performed", local)

    def test_unsupported_material_and_precedence(self) -> None:
        caller_roots = (
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "presence_result",
            "presence_authorized",
            "presence_established",
            "branch_selection",
            "route_selection",
            "dissolution_selection",
            "operation_invocation",
            "successor_selection",
        )
        for key in caller_roots:
            with self.subTest(root=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, issue_path=key)

        envelope = self.canonical()
        envelope["constitutional_event_key"]["unknown"] = False
        self.assert_blocked(
            envelope,
            issue_path="constitutional_event_key.unknown",
        )
        envelope = self.canonical()
        envelope["constitutional_event_key"]["target"]["unknown"] = False
        self.assert_blocked(
            envelope,
            issue_path="constitutional_event_key.target.unknown",
        )
        for map_name in resolver.EXPECTED_REQUIRED_NON_CLAIMS:
            envelope = self.canonical()
            envelope["required_non_claims"][map_name]["unknown"] = False
            self.assert_blocked(
                envelope,
                issue_path=f"required_non_claims.{map_name}.unknown",
            )

        ordinary_path = sorted(
            resolver.ORDINARY_RELATION_LAPSE_BASIS_PATHS
        )[0]
        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        envelope["intent"] = "OTHER"
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        event_path = sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)[0]
        _set_path(envelope, event_path, _wrong_value(_get_path(envelope, event_path)))
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        local_path = sorted(
            resolver.PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS
        )[0]
        _set_path(envelope, local_path, True)
        self.assert_blocked(envelope, issue_path=local_path)

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        self.assert_requires(envelope, [ordinary_path])
        self.assert_allowed(self.canonical())

    def test_source_stopping_branch_and_dissolution_restraint(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.assert_allowed(envelope)
        expected = envelope["constitutional_event_key"][
            "current_lapse_operation_result"
        ]["downstream_stopping_point"]
        self.assertEqual(result["source_stopping_posture"], expected)
        self.assertEqual(envelope, before)

        stopping = result["source_stopping_posture"]
        exact = {
            "presence_boundary_consideration": "OPEN_ONLY",
            "relation_dissolution_boundary_consideration": "OPEN_ONLY",
            "current_branch_selected": False,
            "presence_boundary_selected": False,
            "relation_dissolution_boundary_selected": False,
            "branch_choice_created": False,
            "next_rank_invoked": False,
            "next_rank_authorized": False,
            "next_rank_scheduled": False,
            "next_rank_executed": False,
            "next_rank_completed": False,
            "automatic_successor_created": False,
        }
        for key, value in exact.items():
            self.assertEqual(stopping[key], value, key)

        boundary = result["presence_boundary"]
        self.assertFalse(boundary["relation_dissolution_authorized"])
        self.assertFalse(boundary["relation_dissolution_performed"])
        self.assertFalse(
            boundary["direct_presence_boundary_to_relation_dissolution"]
        )
        all_keys = _all_mapping_keys(result)
        for forbidden in (
            "relation_dissolution_boundary_id",
            "relation_dissolution_result",
            "dissolvable_subject",
            "presence_dissolution_order",
            "presence_dissolution_mutual_exclusivity",
            "branch_selector",
            "route_selector",
        ):
            self.assertNotIn(forbidden, all_keys)

    def test_historical_current_relation_and_pair_source_preservation(self) -> None:
        result = self.assert_allowed(self.canonical())
        historical = result["freshness_and_history"][
            "historical_presence_boundary"
        ]
        self.assertEqual(
            historical["result_reference"],
            "artifacts/integrity_host_v0_min_coexistence_presence_boundary_v0_min/"
            "presence_boundary_001__presence_boundary_v0_min_result.json",
        )
        self.assertEqual(
            historical["result_sha256"],
            "af62fb008965438599e07bde4b8a2fe06f946d4ba79300e8a9226ebc202f6a5b",
        )
        for field in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
        ):
            self.assertIs(historical[field], False)

        for replacement in (
            historical["result_reference"],
            "artifacts/integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min/"
            "relation_lapse_operation_001__relation_lapse_operation_v0_min_result.json",
        ):
            envelope = self.canonical()
            path = (
                "constitutional_event_key.current_lapse_operation_result."
                "result_reference"
            )
            _set_path(envelope, path, replacement)
            self.assert_blocked(envelope, issue_path=path)

        material = result["presence_boundary_material"]
        persistence = material["relation_record_persistence"]
        self.assertTrue(persistence["relation_record_confirmed_as_historical_only"])
        self.assertTrue(persistence["relation_occurrence_remains_addressable"])
        self.assertFalse(persistence["relation_record_is_living_relation_state"])
        self.assertFalse(persistence["relation_created"])
        self.assertFalse(persistence["retained_relation_state_created"])
        self.assertFalse(persistence["relation_dissolved"])
        self.assertFalse(persistence["relation_reversed"])

        carried = result["carried_source_operation_event_key"][
            "source_boundary_event_key"
        ]["source_operation_event_key"]
        self.assertEqual(
            carried["first_crossing_a"]["first_crossing_id"],
            "first_crossing_a_001",
        )
        self.assertEqual(
            carried["first_crossing_b"]["first_crossing_id"],
            "first_crossing_b_001",
        )
        self.assertEqual(
            carried["first_crossing_a"]["descendant_body_id"],
            "descendant_body_a_001",
        )
        self.assertEqual(
            carried["first_crossing_b"]["descendant_body_id"],
            "descendant_body_b_001",
        )
        for field in (
            "complete_pair_preserved",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
        ):
            self.assertIs(carried["pair"][field], True, field)
        self.assertEqual(
            carried["source"]["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        self.assertFalse(carried["pair"]["source_semantic_owner_transferred"])
        self.assertFalse(result["presence_boundary"]["coupling_created"])

    def test_deterministic_rerender_operation_separation_and_stopping(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["current_presence_boundary_event"]["persistent_boundary_id"],
            "presence_boundary_001",
        )
        self.assertFalse(
            first["current_presence_boundary_event"][
                "resolver_call_count_is_event_count"
            ]
        )
        self.assertFalse(
            first["current_presence_boundary_event"][
                "sibling_event_identity_allocated"
            ]
        )

        envelope = self.canonical()
        path = "constitutional_event_key.boundary_event.relation_id"
        _set_path(envelope, path, "relation_002")
        blocked = self.assert_blocked(envelope, issue_path=path)
        self.assertIsNone(blocked["current_presence_boundary_event"])

        boundary = first["presence_boundary"]
        for field in (
            "presence_supported",
            "presence_authorized",
            "presence_established",
            "presence_recorded",
            "presence_evaluation_performed",
            "presence_operation_invoked",
            "presence_operation_scheduled",
            "presence_operation_executed",
            "presence_operation_completed",
            "automatic_successor_created",
        ):
            self.assertIs(boundary[field], False, field)

        stopping = first["downstream_stopping_point"]
        self.assertEqual(
            stopping["admissible_future_route"],
            "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY",
        )
        self.assertEqual(
            stopping["next_separately_bounded_rank"],
            "PRESENCE_OPERATION",
        )
        self.assertTrue(stopping["presence_operation_consideration_allowed"])
        for field in (
            "presence_operation_invoked",
            "presence_operation_authorized",
            "presence_operation_scheduled",
            "presence_operation_executed",
            "presence_operation_completed",
            "automatic_successor_created",
        ):
            self.assertIs(stopping[field], False, field)

    def test_resolver_purity_and_no_persistence(self) -> None:
        source = inspect.getsource(resolver)
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertEqual(imported, {"__future__", "collections", "copy", "typing"})

        names = _all_code_names(
            resolver.resolve_presence_boundary_v0_min_v2,
            resolver.build_declared_presence_boundary_v0_min_v2_request,
            resolver._build_result,
        )
        forbidden = {
            "open",
            "Path",
            "read_text",
            "read_bytes",
            "write_text",
            "write_bytes",
            "sha256",
            "glob",
            "rglob",
            "walk",
            "system",
            "run",
            "time",
            "datetime",
            "urlopen",
            "requests",
            "socket",
        }
        self.assertFalse(names & forbidden)
        self.assertNotIn("resolve_relation_lapse_operation_v0_min_v2", imported)
        self.assertNotIn("resolve_presence_boundary_v0_min", imported)
        self.assertNotIn("resolve_presence_operation_v0_min", imported)

        with mock.patch("builtins.open", side_effect=AssertionError("I/O")):
            envelope = self.canonical()
            before = deepcopy(envelope)
            result = self.resolve(envelope)
            self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
            self.assertEqual(envelope, before)

        for result in (
            self.resolve(None),
            self.resolve([]),
            self.resolve("request"),
        ):
            self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
            self.assertEqual(result["block"]["code"], "REQUEST_NOT_MAPPING")


if __name__ == "__main__":
    unittest.main()
