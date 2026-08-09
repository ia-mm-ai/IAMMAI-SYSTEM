"""Adversarial proof for the current-line relation-lapse-boundary V2 resolver."""

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

import resolve_relation_lapse_boundary_v0_min_v2 as resolver


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


class RelationLapseBoundaryV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_relation_lapse_boundary_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_relation_lapse_boundary_v0_min_v2(envelope)

    def assert_no_positive_boundary(self, result: dict[str, object]) -> None:
        boundary = result["relation_lapse_boundary"]
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
        self.assertFalse(block["requires_reversibility"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_boundary(result)
        return result

    def assert_requires(
        self, envelope: object, missing_path: str
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_REQUIRES_REVERSIBILITY)
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_reversibility"])
        self.assertEqual(
            result["ordinary_reversibility_basis_review"]["missing_paths"],
            [missing_path],
        )
        self.assert_no_positive_boundary(result)
        return result

    def assert_allowed(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(
            result["relation_lapse_boundary"]["relation_lapse_boundary_result"],
            resolver.RESULT_ALLOWED,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_reversibility"])
        self.assertEqual(result["failed_check_count"], 0)
        return result

    def assert_exact_false_map(
        self, map_name: str, expected_keys: tuple[str, ...]
    ) -> None:
        base_path = f"required_non_claims.{map_name}"
        envelope = self.canonical()
        del envelope["required_non_claims"][map_name]
        self.assert_blocked(envelope, issue_path=base_path)

        for key in expected_keys:
            path = f"{base_path}.{key}"
            for case, replacement in (("true", True), ("non_boolean", 0)):
                with self.subTest(map_name=map_name, case=case, path=path):
                    envelope = self.canonical()
                    _set_path(envelope, path, replacement)
                    self.assert_blocked(envelope, issue_path=path)
            with self.subTest(map_name=map_name, case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
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
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 287)
        self.assertEqual(len(resolver.SOURCE_OPERATION_EVENT_KEY_PATHS), 228)
        self.assertTrue(
            all(
                path.startswith(
                    "constitutional_event_key.source_operation_event_key."
                )
                for path in resolver.SOURCE_OPERATION_EVENT_KEY_PATHS
            )
        )
        self.assertEqual(len(resolver.ORDINARY_REVERSIBILITY_BASIS_PATHS), 10)
        self.assertEqual(
            len(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS), 8
        )
        self.assertEqual(
            len(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS), 68
        )
        self.assertEqual(
            len(resolver.SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_PATHS), 86
        )
        self.assertEqual(
            len(resolver.SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_PATHS), 96
        )
        self.assertEqual(len(resolver.SOURCE_REQUIRED_NON_CLAIM_PATHS), 258)
        self.assertEqual(len(resolver.BOUNDARY_LOCAL_NON_CLAIM_PATHS), 97)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 355)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 655)

        event_paths = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            event_paths,
            tuple(resolver.ORDINARY_REVERSIBILITY_BASIS_PATHS),
            tuple(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_PATHS),
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
            *resolver.ORDINARY_REVERSIBILITY_BASIS_PATHS,
            *resolver.REQUIRED_NON_CLAIM_PATHS,
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
                "RELATION_LAPSE_BOUNDARY_BLOCKED",
                "RELATION_LAPSE_BOUNDARY_REQUIRES_REVERSIBILITY",
                "RELATION_LAPSE_BOUNDARY_ALLOWED",
            ),
        )
        self.assertEqual(len(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS), 6)
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS)
        )

    def test_target_control_canonical_positive_and_check_observability(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        self.assertEqual(envelope["intent"], "RECORD_RELATION_LAPSE_BOUNDARY")
        for forbidden in (
            "selected_branch",
            "selected_route",
            "branch_choice",
            "route_choice",
            "operator_branch_selection",
            "selection_result",
            "selector_result",
        ):
            self.assertNotIn(forbidden, _all_mapping_keys(envelope))

        result = self.assert_allowed(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.2.0")
        boundary = result["relation_lapse_boundary"]
        true_boundary_fields = {
            key for key, value in boundary.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_boundary_fields, set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
        )
        self.assertEqual(boundary["boundary_id"], "relation_lapse_boundary_001")
        self.assertEqual(boundary["boundary_type"], "RELATION_LAPSE_BOUNDARY")
        self.assertEqual(boundary["relation_reversibility_operation_id"], "relation_reversibility_operation_001")
        self.assertEqual(boundary["relation_reversibility_id"], "relation_reversibility_001")
        self.assertEqual(boundary["relation_id"], "relation_001")
        self.assertEqual(boundary["relation_object_cardinality"], 1)
        self.assertEqual(boundary["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        for field in resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(boundary[field], False, field)
        for field in (
            "relation_lapse_supported",
            "relation_lapse_authorized",
            "relation_lapse_performed",
            "relation_lapse_recorded",
        ):
            self.assertIs(boundary[field], False, field)
        self.assertNotIn("relation_lapse_boundary_002", repr(result))

        checks = result["relation_lapse_boundary_checks"]
        self.assertEqual(
            result["passed_check_count"],
            sum(item["passed"] is True for item in checks),
        )
        self.assertEqual(
            result["failed_check_count"],
            sum(item["passed"] is False for item in checks),
        )
        self.assertTrue(
            {
                "CONTROL",
                "CONSTITUTIONAL_EVENT_KEY",
                "REQUIRED_NON_CLAIM",
                "ORDINARY_REVERSIBILITY_BASIS",
                "BOUNDARY_RESULT",
                "STOPPING_POINT",
            }
            <= {item["classification"] for item in checks}
        )
        self.assertTrue(
            all(value is False for value in result["operator_target_posture"].values() if type(value) is bool)
        )

    def test_every_event_key_omission_and_each_major_group_mutation_blocks(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(case="omission", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

        for subsection in resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY:
            paths = sorted(
                path
                for path in resolver.CONSTITUTIONAL_EVENT_KEY_PATHS
                if path.startswith(f"constitutional_event_key.{subsection}.")
            )
            self.assertTrue(paths, subsection)
            path = paths[0]
            with self.subTest(case="target_group_mutation", subsection=subsection):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        source = resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY[
            "source_operation_event_key"
        ]
        for subsection in source:
            paths = sorted(
                path
                for path in resolver.SOURCE_OPERATION_EVENT_KEY_PATHS
                if path.startswith(
                    f"constitutional_event_key.source_operation_event_key.{subsection}."
                )
            )
            self.assertTrue(paths, subsection)
            path = paths[0]
            with self.subTest(case="source_group_mutation", subsection=subsection):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

    def test_current_source_identity_lineage_and_history_corruption_blocks(self) -> None:
        paths = (
            "constitutional_event_key.current_operation_result.result_reference",
            "constitutional_event_key.current_operation_result.result_sha256",
            "constitutional_event_key.current_operation_result.result_version",
            "constitutional_event_key.current_operation_result.resolver_module",
            "constitutional_event_key.current_operation_result.blocked",
            "constitutional_event_key.current_operation_result.block_code",
            "constitutional_event_key.current_operation_result.block_issue_path",
            "constitutional_event_key.current_operation_result.requires_boundary_allowance",
            "constitutional_event_key.target.boundary_id",
            "constitutional_event_key.source_operation.operation_id",
            "constitutional_event_key.boundary_event.relation_reversibility_id",
            "constitutional_event_key.boundary_event.relation_id",
            "constitutional_event_key.source_operation_event_key.relation.relation_object_cardinality",
            "constitutional_event_key.source_operation_event_key.pair.topology",
            "constitutional_event_key.source_operation_event_key.first_crossing_a.first_crossing_id",
            "constitutional_event_key.source_operation_event_key.first_crossing_b.first_crossing_id",
            "constitutional_event_key.source_operation_event_key.first_crossing_a.descendant_body_id",
            "constitutional_event_key.source_operation_event_key.first_crossing_b.descendant_body_id",
            "constitutional_event_key.source_operation_event_key.creation_operation.operation_id",
            "constitutional_event_key.source_operation_event_key.creation_event.fresh_operation_request_id",
        )
        for path in paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        envelope = self.canonical()
        path = "constitutional_event_key.target.boundary_id"
        _set_path(envelope, path, "relation_lapse_boundary_002")
        self.assert_blocked(envelope, issue_path=path)

        envelope = self.canonical()
        path = "constitutional_event_key.current_operation_result.result_reference"
        _set_path(envelope, path, resolver.HISTORICAL_LAPSE_BOUNDARY_RESULT_REFERENCE)
        self.assert_blocked(envelope, issue_path=path)

        envelope = self.canonical()
        envelope["constitutional_event_key"]["unknown"] = False
        self.assert_blocked(envelope, issue_path="constitutional_event_key.unknown")

    def test_operator_selection_and_closed_shape_adversaries_block(self) -> None:
        self.assert_blocked(None)
        self.assert_blocked([])
        self.assert_blocked("request")
        for intent in (
            None,
            "RECORD_PRESENCE_BOUNDARY",
            "PRESENCE_BOUNDARY",
            "SELECT_BRANCH",
            "RELATION_LAPSE_BOUNDARY_ALLOWED",
            "DO_NOT_RECORD_RELATION_LAPSE_BOUNDARY",
            "BLOCK_RELATION_LAPSE_BOUNDARY",
        ):
            with self.subTest(intent=intent):
                envelope = self.canonical()
                envelope["intent"] = intent
                self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        del envelope["intent"]
        self.assert_blocked(envelope, issue_path="intent")
        envelope = self.canonical()
        envelope["boundary_question"] += " changed"
        self.assert_blocked(envelope, issue_path="boundary_question")

        for key in (
            "selected_branch",
            "selected_route",
            "branch_choice",
            "route_choice",
            "operator_branch_selection",
            "selection_result",
            "selector_result",
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "artifact",
            "success",
            "automatic_successor",
        ):
            with self.subTest(extra_root=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, issue_path=key)

        for key in resolver.EXECUTABLE_ROOT_KEYS:
            with self.subTest(missing_root=key):
                envelope = self.canonical()
                del envelope[key]
                self.assert_blocked(envelope, issue_path=key)

    def test_each_ordinary_omission_requires_and_every_malformed_value_blocks(self) -> None:
        for path in sorted(resolver.ORDINARY_REVERSIBILITY_BASIS_PATHS):
            with self.subTest(case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.assert_requires(envelope, path)
                review = result["ordinary_reversibility_basis_review"]
                self.assertFalse(
                    review["requires_reversibility_creates_retry_permission"]
                )
                self.assertFalse(
                    review["requires_reversibility_creates_successor_permission"]
                )

            expected = _get_path(self.canonical(), path)
            values = (
                (False, None, "true", 1, {}, [])
                if type(expected) is bool
                else (_wrong_value(expected), None, True, 1, {}, [])
            )
            for value in values:
                with self.subTest(case="malformed", path=path, value=value):
                    envelope = self.canonical()
                    _set_path(envelope, path, value)
                    self.assert_blocked(envelope, issue_path=path)

        for value in (None, "basis", 0, []):
            envelope = self.canonical()
            envelope["ordinary_reversibility_basis"] = value
            self.assert_blocked(
                envelope, issue_path="ordinary_reversibility_basis"
            )
        envelope = self.canonical()
        envelope["ordinary_reversibility_basis"]["unknown"] = True
        self.assert_blocked(
            envelope, issue_path="ordinary_reversibility_basis.unknown"
        )
        for trace_name in (
            "relation_reversibility_operation_recorded",
            "relation_reversibility_evaluation_performed",
            "relation_reversibility_result_recorded",
        ):
            self.assertNotIn(
                f"ordinary_reversibility_basis.{trace_name}",
                resolver.ORDINARY_REVERSIBILITY_BASIS_PATHS,
            )

    def test_all_source_non_claim_maps_are_exact_false(self) -> None:
        self.assert_exact_false_map(
            "source_relation_boundary",
            resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS,
        )
        self.assert_exact_false_map(
            "source_relation_operation",
            resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS,
        )
        self.assert_exact_false_map(
            "source_reversibility_boundary",
            resolver.SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_KEYS,
        )
        self.assert_exact_false_map(
            "source_reversibility_operation",
            resolver.SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_KEYS,
        )
        self.assertEqual(
            8 + 68 + 86 + 96,
            len(resolver.SOURCE_REQUIRED_NON_CLAIM_PATHS),
        )

    def test_boundary_local_non_claim_map_and_totals_are_exact_false(self) -> None:
        self.assert_exact_false_map(
            "boundary_local", resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS
        )
        self.assertEqual(
            258 + 97,
            len(resolver.REQUIRED_NON_CLAIM_PATHS),
        )
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS)
        )
        self.assertTrue(
            all(
                value is False
                for section in self.canonical()["required_non_claims"].values()
                for value in section.values()
            )
        )

    def test_validation_precedence(self) -> None:
        basis_path = "ordinary_reversibility_basis.source_outcome"

        envelope = self.canonical()
        envelope["intent"] = "RECORD_PRESENCE_BOUNDARY"
        _remove_path(envelope, basis_path)
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        event_path = "constitutional_event_key.boundary_event.relation_id"
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

    def test_relation_pair_source_lapse_dissolution_presence_and_coupling_restraint(self) -> None:
        result = self.assert_allowed(self.canonical())
        persistence = result["relation_lapse_boundary_material"][
            "relation_record_persistence"
        ]
        self.assertEqual(persistence["relation_id"], "relation_001")
        self.assertEqual(persistence["relation_object_cardinality"], 1)
        self.assertEqual(persistence["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        self.assertIs(persistence["relation_occurrence_remains_addressable"], True)
        for field in (
            "relation_lapsed",
            "relation_dissolved",
            "relation_reversed",
            "relation_terminated",
            "relation_erased",
            "relation_mutated",
            "relation_invalidated",
            "relation_punished",
            "relation_teardown_created",
        ):
            self.assertIs(persistence[field], False, field)

        pair = result["relation_subject"]["pair"]
        for field in (
            "complete_pair_preserved",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
            "motion_does_not_erase_regulation",
            "regulation_not_sovereign_over_motion",
        ):
            self.assertIs(pair[field], True, field)
        self.assertIs(pair["source_semantic_owner_transferred"], False)
        self.assertEqual(pair["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")

        first_a = result["relation_subject"]["first_crossing_a"]
        first_b = result["relation_subject"]["first_crossing_b"]
        self.assertEqual(first_a["candidate_role"], "CANDIDATE_A")
        self.assertEqual(first_b["candidate_role"], "CANDIDATE_B")
        self.assertEqual(
            result["source_binding"]["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        for field in (
            "source_custody_preserved",
            "source_lineage_preserved",
            "source_rank_preserved",
            "source_scope_preserved",
        ):
            self.assertIs(result["source_binding"][field], True, field)

        stage = result["relation_lapse_boundary_material"][
            "relation_lapse_boundary_evaluation"
        ]
        self.assertIs(stage["relation_lapse_operation_consideration_allowed"], True)
        for field in (
            "relation_lapse_supported",
            "relation_lapse_authorized",
            "relation_lapse_performed",
            "relation_lapse_recorded",
            "relation_dissolution_authorized",
            "relation_dissolution_performed",
            "relation_reversed",
            "relation_terminated",
            "relation_erased",
            "relation_mutated",
            "relation_invalidated",
            "relation_punished",
            "relation_teardown_created",
            "living_relation_state_created",
            "living_relation_state_lapsed",
            "living_relation_state_dissolved",
            "historical_receipt_preservation_authorized",
            "historical_receipt_preserved",
            "presence_boundary_authorized",
            "presence_established",
            "identity_created",
            "coupling_created",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(stage[field], False, field)

        boundary = result["relation_lapse_boundary"]
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
            "standing_descendant_created",
            "descendant_standing_check_performed",
            "currentness_created",
            "authority_created",
            "identity_created",
            "runtime_created",
            "api_created",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[field], False, field)
        self.assertNotIn("landlord", _all_mapping_keys(result))

    def test_historical_current_open_posture_and_stopping_point(self) -> None:
        result = self.assert_allowed(self.canonical())
        current = result["current_relation_reversibility_operation_result_binding"]
        self.assertEqual(
            current["result_reference"],
            resolver.CURRENT_REVERSIBILITY_OPERATION_RESULT_REFERENCE,
        )
        self.assertEqual(
            current["result_sha256"],
            resolver.CURRENT_REVERSIBILITY_OPERATION_RESULT_SHA256,
        )
        self.assertEqual(current["result_version"], "0.2.0")
        self.assertEqual(
            current["resolver_module"],
            "resolve_relation_reversibility_operation_v0_min_v2",
        )
        self.assertIs(current["blocked"], False)
        self.assertIsNone(current["block_code"])
        self.assertIsNone(current["block_issue_path"])
        self.assertIs(current["requires_boundary_allowance"], False)

        history = result["freshness_and_history"]
        historical = history["historical_lapse_boundary"]
        self.assertEqual(historical["historical_boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(
            historical["result_reference"],
            resolver.HISTORICAL_LAPSE_BOUNDARY_RESULT_REFERENCE,
        )
        self.assertEqual(
            historical["result_sha256"],
            resolver.HISTORICAL_LAPSE_BOUNDARY_RESULT_SHA256,
        )
        self.assertEqual(historical["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(historical["boundary_result"], resolver.RESULT_ALLOWED)
        self.assertEqual(historical["relation_id"], "relation_001")
        self.assertEqual(historical["immediate_next_rank"], "RELATION_LAPSE_OPERATION")
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
        ):
            self.assertIs(historical[key], False, key)
        self.assertNotEqual(historical["result_reference"], current["result_reference"])

        source_stop = result["completed_predecessor_open_posture"]
        self.assertEqual(source_stop["relation_lapse_boundary_consideration"], "OPEN_ONLY")
        self.assertEqual(source_stop["presence_boundary_consideration"], "OPEN_ONLY")
        for field in (
            "current_branch_selected",
            "branch_choice_created",
            "next_rank_invoked",
            "next_rank_authorized",
            "automatic_successor_created",
        ):
            self.assertIs(source_stop[field], False, field)

        event = result["current_relation_lapse_boundary_event"]
        self.assertIs(event["same_identity_same_binding_is_deterministic_rerender"], True)
        self.assertIs(event["resolver_call_count_is_event_count"], False)
        self.assertIs(event["sibling_event_identity_allocated"], False)

        stop = result["downstream_stopping_point"]
        self.assertEqual(stop["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(stop["next_separately_bounded_rank"], "RELATION_LAPSE_OPERATION")
        for field in (
            "next_rank_invoked",
            "next_rank_authorized",
            "next_rank_scheduled",
            "next_rank_executed",
            "next_rank_completed",
            "automatic_successor_created",
        ):
            self.assertIs(stop[field], False, field)

    def test_deterministic_rerender_changed_binding_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["current_relation_lapse_boundary_event"],
            second["current_relation_lapse_boundary_event"],
        )
        self.assertNotIn("sibling_boundary", repr(first))
        self.assertNotIn("relation_lapse_boundary_002", repr(first))

        changed = self.canonical()
        path = "constitutional_event_key.boundary_event.relation_id"
        _set_path(changed, path, "relation_002")
        self.assert_blocked(changed, issue_path=path)
        changed = self.canonical()
        changed["intent"] = "RECORD_PRESENCE_BOUNDARY"
        self.assert_blocked(changed, issue_path="intent")

        names = _all_code_names(
            resolver.resolve_relation_lapse_boundary_v0_min_v2,
            resolver.build_declared_relation_lapse_boundary_v0_min_v2_request,
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
            "environ",
            "network",
            "git",
        ):
            self.assertNotIn(forbidden, names)
        for forbidden in (
            "resolve_relation_reversibility_operation_v0_min_v2",
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

