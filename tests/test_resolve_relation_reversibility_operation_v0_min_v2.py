"""Adversarial proof for the current-line reversibility-operation V2 resolver."""

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

import resolve_relation_reversibility_operation_v0_min_v2 as resolver


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


class RelationReversibilityOperationV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_relation_reversibility_operation_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_relation_reversibility_operation_v0_min_v2(envelope)

    def assert_no_positive_operation(self, result: dict[str, object]) -> None:
        operation = result["relation_reversibility_operation"]
        for field in resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS:
            self.assertIs(operation[field], False, field)

    def assert_blocked(
        self, envelope: object, *, issue_path: str | None = None
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_BLOCKED)
        block = result["block"]
        self.assertTrue(block["blocked"])
        self.assertIn(block["code"], resolver.BLOCK_CODES)
        self.assertFalse(block["requires_boundary_allowance"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_operation(result)
        return result

    def assert_requires_allowance(
        self, envelope: object, missing_path: str
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(
            result["outcome"], resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_boundary_allowance"])
        self.assertEqual(
            result["ordinary_boundary_allowance_review"]["missing_paths"],
            [missing_path],
        )
        self.assert_no_positive_operation(result)
        return result

    def assert_recorded(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            result["relation_reversibility_operation"][
                "relation_reversibility_result"
            ],
            resolver.RESULT_SUPPORTED,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_boundary_allowance"])
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
            for case, replacement in (("missing", None), ("true", True), ("typed", 0)):
                with self.subTest(map_name=map_name, case=case, path=path):
                    envelope = self.canonical()
                    if case == "missing":
                        _remove_path(envelope, path)
                    else:
                        _set_path(envelope, path, replacement)
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
        self.assertEqual(
            set(envelope),
            {
                "intent",
                "operation_question",
                "constitutional_event_key",
                "ordinary_boundary_allowance",
                "required_non_claims",
            },
        )
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 228)
        self.assertEqual(len(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS), 6)
        self.assertEqual(len(resolver.ORDINARY_REVERSIBILITY_SUPPORT_BASIS), 0)
        self.assertEqual(
            len(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS), 8
        )
        self.assertEqual(
            len(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS), 68
        )
        self.assertEqual(
            len(resolver.SOURCE_BOUNDARY_LOCAL_NON_CLAIM_PATHS), 86
        )
        self.assertEqual(
            len(resolver.SOURCE_BOUNDARY_REQUIRED_NON_CLAIM_PATHS), 162
        )
        self.assertEqual(len(resolver.OPERATION_LOCAL_NON_CLAIM_PATHS), 96)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 258)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 495)

        event_paths = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            event_paths,
            tuple(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS),
            tuple(resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS),
            tuple(resolver.SOURCE_BOUNDARY_LOCAL_NON_CLAIM_PATHS),
            tuple(resolver.OPERATION_LOCAL_NON_CLAIM_PATHS),
        )
        for paths in explicit_lists:
            self.assertEqual(len(paths), len(set(paths)))
        class_sets = tuple(resolver.CLASS_PATHS.values())
        self.assertEqual(sum(map(len, class_sets)), len(resolver.ALL_REQUIRED_PATHS))
        for index, paths in enumerate(class_sets):
            for other in class_sets[index + 1 :]:
                self.assertFalse(paths & other)
        self.assertEqual(
            frozenset().union(*class_sets), resolver.ALL_REQUIRED_PATHS
        )

        parents: set[str] = set()
        for path in resolver.ALL_REQUIRED_PATHS:
            parts = path.split(".")
            parents.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parents & resolver.ALL_REQUIRED_PATHS)

        operation_additions = {
            path
            for path in event_paths
            if path.startswith("constitutional_event_key.current_boundary_result.")
            or path.startswith("constitutional_event_key.operation_event.")
            or path.startswith("constitutional_event_key.operation_freshness.")
            or path.startswith("constitutional_event_key.historical_operation.")
            or path
            == "constitutional_event_key.non_claim_attribution.operation_local.owner"
        }
        self.assertEqual(len(operation_additions), 46)
        self.assertEqual(len(set(event_paths) - operation_additions), 182)
        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "RELATION_REVERSIBILITY_OPERATION_BLOCKED",
                "RELATION_REVERSIBILITY_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE",
                "RELATION_REVERSIBILITY_OPERATION_RECORDED",
            ),
        )
        self.assertEqual(len(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS), 11)
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        )

    def test_canonical_recorded_result_and_exact_positive_fields(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.assert_recorded(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.2.0")

        operation = result["relation_reversibility_operation"]
        true_fields = {
            key for key, value in operation.items() if type(value) is bool and value
        }
        self.assertEqual(true_fields, set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS))
        self.assertEqual(len(true_fields), 11)
        self.assertIs(operation["relation_record_confirmed_as_historical_only"], True)
        self.assertNotIn("relation_reversibility_created", operation)
        for field in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(operation[field], False, field)

        checks = result["relation_reversibility_operation_checks"]
        self.assertEqual(
            {check["classification"] for check in checks},
            {
                "CONTROL",
                "CONSTITUTIONAL_EVENT_KEY",
                "REQUIRED_NON_CLAIM",
                "ORDINARY_BOUNDARY_ALLOWANCE",
            },
        )
        self.assertEqual(result["passed_check_count"], len(checks))
        self.assertEqual(result["failed_check_count"], 0)

    def test_every_event_key_leaf_omission_blocks(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

    def test_every_event_group_has_strict_mutation_coverage(self) -> None:
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

    def test_current_source_corruption_always_blocks(self) -> None:
        paths = tuple(
            f"constitutional_event_key.current_boundary_result.{key}"
            for key in (
                "result_reference",
                "result_sha256",
                "result_version",
                "resolver_module",
                "blocked",
                "block_code",
                "block_issue_path",
                "requires_relation",
            )
        )
        for path in paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        for path in (
            "ordinary_boundary_allowance.source_outcome",
            "ordinary_boundary_allowance.source_boundary_result",
        ):
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

    def test_each_allowance_omission_requires_boundary_allowance(self) -> None:
        for path in sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS):
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.assert_requires_allowance(envelope, path)
                review = result["ordinary_boundary_allowance_review"]
                self.assertEqual(review["ordinary_reversibility_support_input_count"], 0)
                self.assertFalse(review["requires_allowance_creates_retry_permission"])
                self.assertFalse(
                    review["requires_allowance_creates_successor_permission"]
                )

    def test_every_allowance_malformed_or_false_value_blocks(self) -> None:
        for path in sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS):
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

    def test_no_caller_support_preclaim_is_accepted(self) -> None:
        self.assertFalse(resolver.ORDINARY_REVERSIBILITY_SUPPORT_BASIS_PATHS)
        support_names = (
            "relation_reversibility_supported",
            "relation_reversibility_support_found",
            "reversibility_support_present",
            "historical_confirmation_present",
        )
        for name in support_names:
            for value in (True, False):
                with self.subTest(location="root", name=name, value=value):
                    envelope = self.canonical()
                    envelope[name] = value
                    self.assert_blocked(envelope, issue_path=name)
                with self.subTest(location="event", name=name, value=value):
                    envelope = self.canonical()
                    envelope["constitutional_event_key"]["operation_event"][name] = value
                    self.assert_blocked(
                        envelope,
                        issue_path=f"constitutional_event_key.operation_event.{name}",
                    )
                with self.subTest(location="allowance", name=name, value=value):
                    envelope = self.canonical()
                    envelope["ordinary_boundary_allowance"][name] = value
                    self.assert_blocked(
                        envelope,
                        issue_path=f"ordinary_boundary_allowance.{name}",
                    )

    def test_persistent_identity_pair_source_and_creation_binding(self) -> None:
        mutations = {
            "constitutional_event_key.operation_event.persistent_operation_id": (
                "relation_reversibility_operation_002"
            ),
            "constitutional_event_key.operation_event.relation_reversibility_id": (
                "relation_reversibility_002"
            ),
            "constitutional_event_key.operation_event.relation_id": "relation_002",
            "constitutional_event_key.relation.relation_object_cardinality": 2,
            "constitutional_event_key.pair.topology": "DIRECTIONAL",
        }
        for path, value in mutations.items():
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, value)
                self.assert_blocked(envelope, issue_path=path)

        lineage_paths = (
            "constitutional_event_key.first_crossing_a.first_crossing_id",
            "constitutional_event_key.first_crossing_b.first_crossing_id",
            "constitutional_event_key.first_crossing_a.descendant_body_id",
            "constitutional_event_key.first_crossing_b.descendant_body_id",
            "constitutional_event_key.first_crossing_a.candidate_standing_source_id",
            "constitutional_event_key.first_crossing_b.candidate_standing_source_id",
            "constitutional_event_key.first_crossing_a.candidate_basis_id",
            "constitutional_event_key.first_crossing_b.candidate_basis_id",
            "constitutional_event_key.pair.complete_pair_preserved",
            "constitutional_event_key.source.selected_surface_semantic_owner",
            "constitutional_event_key.creation_operation.operation_id",
            "constitutional_event_key.creation_event.fresh_operation_request_id",
        )
        for path in lineage_paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

    def test_all_four_non_claim_maps_are_exact_false(self) -> None:
        for map_name, keys in (
            (
                "source_relation_boundary",
                resolver.SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS,
            ),
            (
                "source_relation_operation",
                resolver.SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS,
            ),
            ("boundary_local", resolver.BOUNDARY_LOCAL_NON_CLAIM_KEYS),
            ("operation_local", resolver.OPERATION_LOCAL_NON_CLAIM_KEYS),
        ):
            with self.subTest(map_name=map_name):
                self.assert_exact_false_map(map_name, keys)
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        )

    def test_closed_shape_and_unsupported_caller_fields_block(self) -> None:
        for value in (None, [], "request"):
            with self.subTest(non_mapping=value):
                self.assert_blocked(value)

        for key in (
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "receipt",
            "artifact",
            "support",
            "reversibility_support",
            "relation_reversibility_supported",
            "lapse_route",
            "presence_route",
            "success",
            "occurrence",
            "invocation",
            "execution",
            "successor_selector",
            "branch_selector",
        ):
            with self.subTest(root=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, issue_path=key)

        nested = (
            ("constitutional_event_key", "unknown"),
            ("ordinary_boundary_allowance", "unknown"),
            ("required_non_claims", "unknown"),
        )
        for root, key in nested:
            with self.subTest(root=root):
                envelope = self.canonical()
                envelope[root][key] = {}
                self.assert_blocked(envelope, issue_path=f"{root}.{key}")

        for key in tuple(resolver.EXECUTABLE_ROOT_KEYS):
            with self.subTest(missing_root=key):
                envelope = self.canonical()
                del envelope[key]
                self.assert_blocked(envelope, issue_path=key)

    def test_validation_precedence(self) -> None:
        allowance_path = "ordinary_boundary_allowance.source_outcome"

        envelope = self.canonical()
        envelope["intent"] = "DO_NOT_RECORD_RELATION_REVERSIBILITY_OPERATION"
        _remove_path(envelope, allowance_path)
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        event_path = "constitutional_event_key.relation.relation_id"
        _remove_path(envelope, event_path)
        _remove_path(envelope, allowance_path)
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        non_claim_path = "required_non_claims.operation_local.runtime_created"
        _set_path(envelope, non_claim_path, True)
        _remove_path(envelope, allowance_path)
        self.assert_blocked(envelope, issue_path=non_claim_path)

        envelope = self.canonical()
        _remove_path(envelope, allowance_path)
        self.assert_requires_allowance(envelope, allowance_path)
        self.assert_recorded(self.canonical())

    def test_deterministic_rerender_changed_binding_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["current_relation_reversibility_operation_event"],
            second["current_relation_reversibility_operation_event"],
        )
        self.assertIs(
            first["current_relation_reversibility_operation_event"]
            ["resolver_call_count_is_event_count"],
            False,
        )
        self.assertNotIn("sibling_operation", repr(first))
        self.assertNotIn("relation_reversibility_operation_002", repr(first))

        changed = self.canonical()
        path = "constitutional_event_key.operation_event.relation_id"
        _set_path(changed, path, "relation_002")
        self.assert_blocked(changed, issue_path=path)

        names = _all_code_names(
            resolver.resolve_relation_reversibility_operation_v0_min_v2,
            resolver.build_declared_relation_reversibility_operation_v0_min_v2_request,
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
            "resolve_relation_reversibility_boundary_v0_min_v2",
            "resolve_relation_reversibility_operation_v0_min",
            "resolve_relation_lapse_boundary_v0_min",
            "resolve_relation_lapse_operation_v0_min",
            "resolve_presence_boundary_v0_min",
            "resolve_presence_operation_v0_min",
        ):
            self.assertNotIn(forbidden, vars(resolver))

        with mock.patch("builtins.open", side_effect=AssertionError("I/O")):
            self.assertEqual(
                self.resolve(self.canonical())["outcome"], resolver.OUTCOME_RECORDED
            )

    def test_relation_persistence_historical_only_and_destructive_restraint(self) -> None:
        result = self.assert_recorded(self.canonical())
        operation = result["relation_reversibility_operation"]
        persistence = result["relation_reversibility_operation_material"][
            "relation_record_persistence"
        ]
        self.assertEqual(operation["relation_id"], "relation_001")
        self.assertEqual(operation["relation_object_cardinality"], 1)
        self.assertEqual(operation["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        self.assertIs(persistence["relation_occurrence_remains_addressable"], True)
        self.assertIs(operation["relation_record_confirmed_as_historical_only"], True)
        for field in (
            "relation_record_is_living_relation_state",
            "living_relation_state_created",
            "living_relation_state_lapsed",
            "living_relation_state_dissolved",
            "relation_lapse_authorized",
            "relation_lapse_performed",
            "relation_dissolution_authorized",
            "relation_dissolution_performed",
            "relation_reversed",
            "relation_terminated",
            "relation_erased",
            "relation_mutated",
            "relation_invalidated",
            "relation_punished",
            "relation_teardown_created",
            "historical_receipt_preservation_authorized",
            "historical_receipt_preserved",
            "currentness_created",
        ):
            self.assertIs(operation[field], False, field)
        self.assertNotIn("relation_002", repr(result))

    def test_pair_coupling_and_downstream_non_conversion(self) -> None:
        result = self.assert_recorded(self.canonical())
        operation = result["relation_reversibility_operation"]
        pair = result["relation_subject"]["pair"]
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
        for field in (
            "separate_crossing_occurrences_created",
            "source_semantic_owner_transferred",
        ):
            self.assertIs(pair[field], False, field)

        false_fields = (
            "coupling_assigned_to_relation",
            "coupling_assigned_to_first_crossing_a",
            "coupling_assigned_to_first_crossing_b",
            "coupling_assigned_to_descendant_body_a",
            "coupling_assigned_to_descendant_body_b",
            "coupling_assigned_to_candidate_a",
            "coupling_assigned_to_candidate_b",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "standing_descendant_created",
            "standing_created",
            "descendant_standing_check_performed",
            "currentness_created",
            "authority_created",
            "presence_boundary_authorized",
            "presence_established",
            "identity_created",
            "runtime_created",
            "api_created",
            "output_authorized",
            "action_authorized",
            "derivative_reception_authorized",
            "synchronization_authorized",
            "follow_on_authorized",
            "follow_on_work_authorized",
        )
        for field in false_fields:
            self.assertIs(operation[field], False, field)
        source = result["source_binding"]
        self.assertEqual(
            source["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        for field in (
            "source_custody_preserved",
            "source_lineage_preserved",
            "source_rank_preserved",
            "source_scope_preserved",
        ):
            self.assertIs(source[field], True, field)

    def test_historical_current_separation_route_and_future_identifiers(self) -> None:
        result = self.assert_recorded(self.canonical())
        current = result["current_relation_reversibility_boundary_result_binding"]
        self.assertEqual(current["result_reference"], resolver.CURRENT_BOUNDARY_RESULT_REFERENCE)
        self.assertEqual(current["result_sha256"], resolver.CURRENT_BOUNDARY_RESULT_SHA256)
        self.assertEqual(current["result_version"], "0.2.0")
        self.assertEqual(
            current["resolver_module"],
            "resolve_relation_reversibility_boundary_v0_min_v2",
        )

        history = result["operation_freshness_and_history"]
        historical = history["historical_operation"]
        self.assertEqual(historical["historical_operation_id"], resolver.OPERATION_ID)
        self.assertEqual(
            historical["result_sha256"],
            "d59c4ce570acdf15a06199827d3e6a1432804f708949e73f6c4efab6ee278fbb",
        )
        self.assertEqual(historical["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(historical["operation_result"], resolver.RESULT_SUPPORTED)
        self.assertEqual(historical["relation_id"], "relation_001")
        self.assertEqual(
            historical["relation_reversibility_id"], "relation_reversibility_001"
        )
        self.assertEqual(historical["immediate_next_rank"], "RELATION_LAPSE_BOUNDARY")
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
        ):
            self.assertIs(historical[key], False, key)
        self.assertNotEqual(historical["result_reference"], current["result_reference"])

        stop = result["downstream_stopping_point"]
        self.assertEqual(stop["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        self.assertEqual(stop["relation_lapse_boundary_consideration"], "OPEN_ONLY")
        self.assertEqual(stop["presence_boundary_consideration"], "OPEN_ONLY")
        self.assertEqual(
            stop["historical_realized_immediate_successor"], "RELATION_LAPSE_BOUNDARY"
        )
        self.assertEqual(
            stop["historical_realized_route"],
            "RELATION_REVERSIBILITY_OPERATION -> RELATION_LAPSE_BOUNDARY -> "
            "RELATION_LAPSE_OPERATION -> PRESENCE_BOUNDARY",
        )
        for field in (
            "current_branch_selected",
            "branch_choice_created",
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
        self.assertEqual(
            future["relation_lapse_scope"],
            "RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY",
        )
        self.assertEqual(future["relation_dissolution_id"], "relation_dissolution_001")
        self.assertEqual(
            future["relation_dissolution_scope"],
            "RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY",
        )
        keys = _all_mapping_keys(result)
        for absent in (
            "relation_lapse_occurrence",
            "relation_dissolution_occurrence",
            "relation_lapse_result",
            "presence_boundary_result",
            "branch_choice_event",
        ):
            self.assertNotIn(absent, keys)


if __name__ == "__main__":
    unittest.main()
