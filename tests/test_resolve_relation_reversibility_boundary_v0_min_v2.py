"""Adversarial proof for the current-line reversibility-boundary V2 resolver."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys
import types
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_reversibility_boundary_v0_min_v2 as resolver


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
    raise AssertionError(f"no strict mutation defined for {value!r}")


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


class RelationReversibilityBoundaryV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_relation_reversibility_boundary_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_relation_reversibility_boundary_v0_min_v2(envelope)

    def assert_no_positive_boundary(self, result: dict[str, object]) -> None:
        boundary = result["relation_reversibility_boundary"]
        for field in resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS:
            self.assertIs(boundary[field], False, field)

    def assert_blocked(
        self, envelope: object, *, issue_path: str | None = None
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block = result["block"]
        self.assertTrue(block["blocked"])
        self.assertIn(block["code"], resolver.BLOCK_CODES)
        self.assertFalse(block["requires_relation"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_boundary(result)
        return result

    def assert_requires(
        self, envelope: object, missing_path: str
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_RELATION)
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_relation"])
        self.assertEqual(
            result["ordinary_relation_basis_review"]["missing_paths"],
            [missing_path],
        )
        self.assert_no_positive_boundary(result)
        return result

    def assert_allowed(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(
            result["relation_reversibility_boundary"][
                "relation_reversibility_boundary_result"
            ],
            resolver.RESULT_ALLOWED,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_relation"])
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
            with self.subTest(map_name=map_name, case="non_boolean", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, 0)
                self.assert_blocked(envelope, issue_path=path)

        for value in (None, "false", 0, []):
            with self.subTest(map_name=map_name, case="non_mapping", value=value):
                envelope = self.canonical()
                envelope["required_non_claims"][map_name] = value
                self.assert_blocked(envelope, issue_path=base_path)

        envelope = self.canonical()
        envelope["required_non_claims"][map_name]["unknown"] = False
        self.assert_blocked(envelope, issue_path=f"{base_path}.unknown")
        self.assertEqual(
            set(self.canonical()["required_non_claims"][map_name]),
            set(expected_keys),
        )

    def test_manifest_exactness_disjointness_and_outcome_lock(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 182)
        self.assertEqual(len(resolver.ORDINARY_RELATION_BASIS_PATHS), 10)
        self.assertEqual(
            len(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS), 8
        )
        self.assertEqual(
            len(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS), 68
        )
        self.assertEqual(len(resolver.BOUNDARY_LOCAL_NON_CLAIM_PATHS), 86)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 162)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 357)

        event_paths = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            event_paths,
            tuple(resolver.ORDINARY_RELATION_BASIS_PATHS),
            tuple(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS),
            tuple(resolver.BOUNDARY_LOCAL_NON_CLAIM_PATHS),
        )
        for paths in explicit_lists:
            self.assertEqual(len(paths), len(set(paths)))
        class_sets = tuple(resolver.CLASS_PATHS.values())
        for index, paths in enumerate(class_sets):
            for other in class_sets[index + 1 :]:
                self.assertFalse(paths & other)
        self.assertEqual(
            frozenset().union(*class_sets), resolver.ALL_REQUIRED_PATHS
        )

        expected_leaves = {
            "$::mapping_cardinality",
            "intent",
            "boundary_question",
            *event_paths,
            *resolver.ORDINARY_RELATION_BASIS_PATHS,
            *resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS,
            *resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS,
            *resolver.BOUNDARY_LOCAL_NON_CLAIM_PATHS,
        }
        self.assertEqual(expected_leaves, resolver.ALL_REQUIRED_PATHS)
        parents: set[str] = set()
        for path in resolver.ALL_REQUIRED_PATHS:
            parts = path.split(".")
            parents.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parents & resolver.ALL_REQUIRED_PATHS)

        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "RELATION_REVERSIBILITY_BOUNDARY_BLOCKED",
                "RELATION_REVERSIBILITY_BOUNDARY_REQUIRES_RELATION",
                "RELATION_REVERSIBILITY_BOUNDARY_ALLOWED",
            ),
        )
        self.assertEqual(len(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS), 6)
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS)
        )

    def test_canonical_allowed_result_and_exact_boundary_fields(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.assert_allowed(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.2.0")

        boundary = result["relation_reversibility_boundary"]
        true_boundary_fields = {
            key for key, value in boundary.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_boundary_fields, set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
        )
        self.assertEqual(boundary["boundary_id"], "relation_reversibility_boundary_001")
        self.assertEqual(boundary["relation_id"], "relation_001")
        self.assertEqual(boundary["relation_object_cardinality"], 1)
        for field in resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(boundary[field], False, field)
        self.assertNotIn("relation_reversibility_supported", boundary)
        self.assertNotIn("relation_002", repr(result))

        identity = result["persistent_relation_identity"]
        self.assertEqual(identity["relation_id"], "relation_001")
        self.assertEqual(identity["relation_object_cardinality"], 1)
        self.assertEqual(
            result["relation_subject"]["pair"]["topology"],
            "PAIR_SCOPED_NON_DIRECTIONAL",
        )

    def test_every_event_key_leaf_omission_blocks(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

    def test_every_event_subsection_has_strict_mutation_coverage(self) -> None:
        for subsection in resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY:
            paths = sorted(
                path
                for path in resolver.CONSTITUTIONAL_EVENT_KEY_PATHS
                if path.startswith(f"constitutional_event_key.{subsection}.")
            )
            self.assertTrue(paths, subsection)
            path = paths[0]
            with self.subTest(subsection=subsection, path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

    def test_current_source_and_relation_identity_corruption_blocks(self) -> None:
        event_paths = (
            "constitutional_event_key.current_relation_operation_result.result_reference",
            "constitutional_event_key.current_relation_operation_result.result_sha256",
            "constitutional_event_key.current_relation_operation_result.result_version",
            "constitutional_event_key.current_relation_operation_result.resolver_module",
            "constitutional_event_key.current_relation_operation_result.blocked",
            "constitutional_event_key.current_relation_operation_result.requires_boundary_allowance",
            "constitutional_event_key.current_relation_operation_result.not_recorded",
            "constitutional_event_key.boundary_event.current_relation_operation_result_reference",
            "constitutional_event_key.boundary_event.current_relation_operation_result_sha256",
            "constitutional_event_key.relation.relation_id",
            "constitutional_event_key.relation.relation_object_cardinality",
            "constitutional_event_key.relation.relation_pair_scope",
            "constitutional_event_key.pair.topology",
        )
        for path in event_paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        envelope = self.canonical()
        _set_path(
            envelope,
            "constitutional_event_key.relation.relation_id",
            "relation_002",
        )
        self.assert_blocked(
            envelope, issue_path="constitutional_event_key.relation.relation_id"
        )

    def test_each_ordinary_omission_requires_relation(self) -> None:
        for path in sorted(resolver.ORDINARY_RELATION_BASIS_PATHS):
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.assert_requires(envelope, path)
                review = result["ordinary_relation_basis_review"]
                self.assertFalse(review["requires_relation_creates_retry_permission"])
                self.assertFalse(
                    review["requires_relation_creates_successor_permission"]
                )

    def test_every_ordinary_contradiction_blocks(self) -> None:
        for path in sorted(resolver.ORDINARY_RELATION_BASIS_PATHS):
            expected = _get_path(self.canonical(), path)
            values: tuple[object, ...]
            if type(expected) is bool:
                values = (False, None, "true", 1, {}, [])
            else:
                values = (_wrong_value(expected), None, True, 1, {}, [])
            for value in values:
                with self.subTest(path=path, value=value):
                    envelope = self.canonical()
                    _set_path(envelope, path, value)
                    self.assert_blocked(envelope, issue_path=path)

    def test_source_relation_boundary_non_claim_map_is_exact_false(self) -> None:
        self.assert_exact_false_map(
            "source_relation_boundary",
            resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS,
        )

    def test_source_relation_operation_non_claim_map_is_exact_false(self) -> None:
        self.assert_exact_false_map(
            "source_relation_operation",
            resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS,
        )

    def test_boundary_local_non_claim_map_is_exact_false(self) -> None:
        self.assert_exact_false_map(
            "boundary_local", resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS
        )
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS)
        )

    def test_closed_shape_and_caller_selected_postures_block(self) -> None:
        self.assert_blocked(None)
        self.assert_blocked([])
        self.assert_blocked("request")

        for key in (
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "artifact",
            "reversibility",
            "lapse",
            "dissolution",
            "presence",
            "success",
            "occurrence",
            "invocation",
            "execution",
            "successor_selector",
        ):
            with self.subTest(root=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, issue_path=key)

        envelope = self.canonical()
        envelope["constitutional_event_key"]["unknown"] = {"value": False}
        self.assert_blocked(envelope, issue_path="constitutional_event_key.unknown")
        envelope = self.canonical()
        envelope["constitutional_event_key"]["relation"]["unknown"] = False
        self.assert_blocked(
            envelope, issue_path="constitutional_event_key.relation.unknown"
        )
        envelope = self.canonical()
        envelope["ordinary_relation_basis"]["unknown"] = False
        self.assert_blocked(envelope, issue_path="ordinary_relation_basis.unknown")
        for map_name in (
            "source_relation_boundary",
            "source_relation_operation",
            "boundary_local",
        ):
            envelope = self.canonical()
            envelope["required_non_claims"][map_name]["unknown"] = False
            self.assert_blocked(
                envelope, issue_path=f"required_non_claims.{map_name}.unknown"
            )

        for key in tuple(resolver.EXECUTABLE_ROOT_KEYS):
            with self.subTest(missing_root=key):
                envelope = self.canonical()
                del envelope[key]
                self.assert_blocked(envelope, issue_path=key)

    def test_validation_precedence(self) -> None:
        basis_path = "ordinary_relation_basis.source_outcome"

        envelope = self.canonical()
        envelope["intent"] = "DO_NOT_RECORD_RELATION_REVERSIBILITY_BOUNDARY"
        _remove_path(envelope, basis_path)
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        event_path = "constitutional_event_key.relation.relation_id"
        _remove_path(envelope, event_path)
        _remove_path(envelope, basis_path)
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        non_claim_path = "required_non_claims.boundary_local.runtime_created"
        _set_path(envelope, non_claim_path, True)
        _remove_path(envelope, basis_path)
        self.assert_blocked(envelope, issue_path=non_claim_path)

        envelope = self.canonical()
        _remove_path(envelope, basis_path)
        self.assert_requires(envelope, basis_path)
        self.assert_allowed(self.canonical())

    def test_relation_persistence_pair_and_reversibility_stage_restraint(self) -> None:
        result = self.assert_allowed(self.canonical())
        persistence = result["relation_reversibility_boundary_material"][
            "relation_record_persistence"
        ]
        self.assertEqual(persistence["relation_id"], "relation_001")
        self.assertEqual(persistence["relation_object_cardinality"], 1)
        self.assertEqual(persistence["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        self.assertIs(persistence["relation_exists_from_current_relation_operation"], True)
        for field in (
            "relation_created_by_boundary",
            "relation_mutated",
            "relation_erased",
            "relation_invalidated",
            "relation_lapsed",
            "relation_dissolved",
            "retained_relation_state_created",
            "living_relation_state_created",
            "directional_relation_state_created",
        ):
            self.assertIs(persistence[field], False, field)
        self.assertNotIn("relation_002", repr(result))

        subject = result["relation_subject"]
        pair = subject["pair"]
        for field in (
            "complete_pair_preserved",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
            "motion_does_not_erase_regulation",
            "regulation_not_sovereign_over_motion",
            "one_shared_crossing_operation_event",
        ):
            self.assertIs(pair[field], True, field)
        self.assertIs(pair["source_semantic_owner_transferred"], False)

        stage = result["relation_reversibility_boundary_material"][
            "reversibility_stage"
        ]
        self.assertIs(stage["relation_reversibility_operation_consideration_allowed"], True)
        for field in (
            "relation_reversibility_supported",
            "relation_reversibility_authorized",
            "relation_reversibility_performed",
            "relation_reversibility_recorded",
            "relation_lapse_authorized",
            "relation_lapse_performed",
            "relation_dissolution_authorized",
            "relation_dissolution_performed",
            "presence_boundary_authorized",
            "presence_established",
        ):
            self.assertIs(stage[field], False, field)

        boundary = result["relation_reversibility_boundary"]
        for field in (
            "coupling_assigned_to_relation",
            "coupling_assigned_to_first_crossing_a",
            "coupling_assigned_to_first_crossing_b",
            "coupling_assigned_to_descendant_body_a",
            "coupling_assigned_to_descendant_body_b",
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "standing_created",
            "currentness_created",
            "authority_created",
            "presence_boundary_authorized",
            "presence_established",
            "identity_created",
            "runtime_created",
            "api_created",
            "output_authorized",
            "action_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[field], False, field)

    def test_historical_current_separation_route_and_future_restraint(self) -> None:
        result = self.assert_allowed(self.canonical())
        current = result["current_relation_operation_result_binding"]
        self.assertEqual(
            current["result_reference"],
            resolver.CURRENT_RELATION_OPERATION_RESULT_REFERENCE,
        )
        self.assertEqual(
            current["result_sha256"], resolver.CURRENT_RELATION_OPERATION_RESULT_SHA256
        )

        history = result["freshness_and_history"]
        historical = history["historical_boundary"]
        self.assertEqual(historical["historical_boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(
            historical["result_sha256"],
            "a6bbb707e77e86adaff158c46aa6e0655801e6f7c1f772ded9cfe15c38a5b3a0",
        )
        self.assertEqual(historical["immediate_next_rank"], "RELATION_REVERSIBILITY_OPERATION")
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
        ):
            self.assertIs(historical[key], False, key)
        self.assertNotEqual(historical["result_reference"], current["result_reference"])

        next_operation = result["next_relation_reversibility_operation_identity"]
        self.assertEqual(next_operation["operation_type"], "RELATION_REVERSIBILITY_OPERATION")
        self.assertEqual(
            next_operation["operation_contract_sha256"],
            "388e674004d4ee0a2191fc602c3369067d1f270aae1d576d6455f548901acd2c",
        )
        self.assertIs(next_operation["direct_boundary_to_operation_completion"], False)
        stop = result["downstream_stopping_point"]
        self.assertEqual(stop["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(stop["next_separately_bounded_rank"], "RELATION_REVERSIBILITY_OPERATION")
        for field in (
            "next_rank_invoked",
            "next_rank_authorized",
            "next_rank_scheduled",
            "next_rank_executed",
            "next_rank_completed",
            "automatic_successor_created",
        ):
            self.assertIs(stop[field], False, field)

        future = result["future_identifiers"]
        self.assertEqual(future["relation_reversibility_id"], "relation_reversibility_001")
        self.assertEqual(future["relation_lapse_id"], "relation_lapse_001")
        self.assertEqual(future["relation_dissolution_id"], "relation_dissolution_001")
        keys = _all_mapping_keys(result)
        for absent in (
            "relation_reversibility_occurrence",
            "relation_lapse_occurrence",
            "relation_dissolution_occurrence",
            "relation_reversibility_operation_result",
            "relation_lapse_result",
            "presence_boundary_result",
        ):
            self.assertNotIn(absent, keys)

    def test_deterministic_rerender_changed_binding_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["current_relation_reversibility_boundary_event"],
            second["current_relation_reversibility_boundary_event"],
        )
        self.assertNotIn("sibling_boundary", repr(first))
        self.assertNotIn("relation_reversibility_boundary_002", repr(first))

        changed = self.canonical()
        path = "constitutional_event_key.boundary_event.relation_id"
        _set_path(changed, path, "relation_002")
        self.assert_blocked(changed, issue_path=path)

        names = _all_code_names(
            resolver.resolve_relation_reversibility_boundary_v0_min_v2,
            resolver.build_declared_relation_reversibility_boundary_v0_min_v2_request,
            resolver._build_result,
        )
        for forbidden in (
            "open",
            "read_text",
            "read_bytes",
            "write_text",
            "write_bytes",
            "glob",
            "rglob",
            "iterdir",
            "stat",
            "sha256",
            "subprocess",
            "datetime",
            "time",
            "git",
        ):
            self.assertNotIn(forbidden, names)
        for forbidden in (
            "resolve_relation_operation_v0_min_v3",
            "resolve_relation_reversibility_boundary_v0_min",
            "resolve_relation_reversibility_operation_v0_min",
            "resolve_relation_lapse_boundary_v0_min",
            "resolve_relation_lapse_operation_v0_min",
            "resolve_presence_boundary_v0_min",
            "resolve_presence_operation_v0_min",
        ):
            self.assertNotIn(forbidden, vars(resolver))

        with mock.patch("builtins.open", side_effect=AssertionError("I/O")):
            self.assertEqual(
                self.resolve(self.canonical())["outcome"], resolver.OUTCOME_ALLOWED
            )


if __name__ == "__main__":
    unittest.main()
