"""Adversarial proof for the current-line RELATION_OPERATION V3 resolver."""

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

import resolve_relation_operation_v0_min_v3 as resolver


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


class RelationOperationV0MinV3Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_relation_operation_v0_min_v3_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_relation_operation_v0_min_v3(envelope)

    def assert_no_positive_operation(self, result: dict[str, object]) -> None:
        operation = result["relation_operation"]
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
        self.assertFalse(block["not_recorded"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_operation(result)
        return result

    def assert_requires(
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

    def assert_not_recorded(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_boundary_allowance"])
        self.assertTrue(result["block"]["not_recorded"])
        self.assertEqual(
            result["ordinary_relation_support_review"]["posture"],
            "NOT_SUPPORTED",
        )
        self.assert_no_positive_operation(result)
        return result

    def assert_recorded(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(
            result["relation_operation"]["relation_result"],
            resolver.RESULT_SUPPORTED,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertEqual(result["failed_check_count"], 0)
        return result

    def test_manifest_exactness_disjointness_and_outcome_lock(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 158)
        self.assertEqual(len(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS), 7)
        self.assertEqual(len(resolver.ORDINARY_RELATION_SUPPORT_BASIS_PATHS), 1)
        self.assertEqual(len(resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS), 8)
        self.assertEqual(len(resolver.OPERATION_LOCAL_NON_CLAIM_PATHS), 68)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 76)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 245)

        event_paths = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            event_paths,
            tuple(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS),
            tuple(resolver.ORDINARY_RELATION_SUPPORT_BASIS_PATHS),
            tuple(resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS),
            tuple(resolver.OPERATION_LOCAL_NON_CLAIM_PATHS),
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
            "operation_question",
            *event_paths,
            *resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS,
            *resolver.ORDINARY_RELATION_SUPPORT_BASIS_PATHS,
            *resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS,
            *resolver.OPERATION_LOCAL_NON_CLAIM_PATHS,
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
                "RELATION_OPERATION_BLOCKED",
                "RELATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE",
                "RELATION_OPERATION_NOT_RECORDED",
                "RELATION_OPERATION_RECORDED",
            ),
        )
        self.assertEqual(len(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS), 11)
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        )

    def test_canonical_positive_result_and_exact_operation_fields(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.assert_recorded(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.3.0")

        operation = result["relation_operation"]
        true_operation_fields = {
            key for key, value in operation.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_operation_fields, set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
        )
        self.assertIs(operation["relation_created"], True)
        self.assertEqual(operation["operation_id"], "relation_operation_001")
        self.assertEqual(operation["relation_id"], "relation_001")
        self.assertEqual(operation["relation_object_cardinality"], 1)
        for field in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(operation[field], False, field)
        self.assertNotIn("relation_object_recorded", operation)
        self.assertNotIn("relation_retained", operation)
        self.assertNotIn("relation_occurrence_established", operation)
        self.assertNotIn("relation_002", repr(result))

        relation = result["relation_operation_material"]["relation_evaluation"]
        self.assertEqual(relation["relation_id"], "relation_001")
        self.assertEqual(relation["relation_object_cardinality"], 1)
        self.assertIs(relation["relation_supported"], True)
        self.assertIs(relation["relation_authorized"], True)
        self.assertIs(relation["relation_created"], True)
        self.assertIs(relation["relation_operation_performed"], True)
        self.assertIs(relation["relation_recorded"], True)

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

    def test_current_source_corruption_and_allowance_contradiction_block(self) -> None:
        event_paths = (
            "constitutional_event_key.current_boundary_result.result_reference",
            "constitutional_event_key.current_boundary_result.result_sha256",
            "constitutional_event_key.current_boundary_result.result_version",
            "constitutional_event_key.current_boundary_result.resolver_module",
            "constitutional_event_key.current_boundary_result.blocked",
            "constitutional_event_key.operation_event.current_boundary_result_reference",
            "constitutional_event_key.operation_event.current_boundary_result_sha256",
        )
        for path in event_paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        allowance_paths = (
            "ordinary_operation_basis.source_outcome",
            "ordinary_operation_basis.source_boundary_result",
            "ordinary_operation_basis.relation_operation_consideration_allowed",
            "ordinary_operation_basis.first_crossing_operation_referenced",
            "ordinary_operation_basis.first_crossing_a_referenced",
            "ordinary_operation_basis.first_crossing_b_referenced",
            "ordinary_operation_basis.first_crossing_pair_referenced",
        )
        for path in allowance_paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

    def test_each_allowance_omission_requires_boundary_allowance(self) -> None:
        for path in sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS):
            with self.subTest(path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.assert_requires(envelope, path)
                review = result["ordinary_boundary_allowance_review"]
                self.assertFalse(
                    review["requires_boundary_allowance_creates_retry_permission"]
                )
                self.assertFalse(
                    review["requires_boundary_allowance_creates_successor_permission"]
                )

    def test_relation_support_postures(self) -> None:
        path = "ordinary_operation_basis.relation_support_found"
        envelope = self.canonical()
        _remove_path(envelope, path)
        self.assert_not_recorded(envelope)
        for value in (False, None, "true", 1, {}, []):
            with self.subTest(value=value):
                envelope = self.canonical()
                _set_path(envelope, path, value)
                self.assert_not_recorded(envelope)
        self.assert_recorded(self.canonical())

    def test_source_boundary_non_claim_map_is_exact_false(self) -> None:
        envelope = self.canonical()
        del envelope["required_non_claims"]["source_boundary"]
        self.assert_blocked(
            envelope, issue_path="required_non_claims.source_boundary"
        )
        for key in resolver.SOURCE_BOUNDARY_NON_CLAIM_KEYS:
            path = f"required_non_claims.source_boundary.{key}"
            with self.subTest(case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)
            with self.subTest(case="true", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, True)
                self.assert_blocked(envelope, issue_path=path)
        for value in (None, "false", 0, []):
            with self.subTest(case="non_mapping", value=value):
                envelope = self.canonical()
                envelope["required_non_claims"]["source_boundary"] = value
                self.assert_blocked(
                    envelope, issue_path="required_non_claims.source_boundary"
                )
        envelope = self.canonical()
        envelope["required_non_claims"]["source_boundary"] = {}
        self.assert_blocked(envelope)
        envelope = self.canonical()
        envelope["required_non_claims"]["source_boundary"]["unknown"] = False
        self.assert_blocked(
            envelope, issue_path="required_non_claims.source_boundary.unknown"
        )

    def test_operation_local_non_claim_map_is_exact_false(self) -> None:
        envelope = self.canonical()
        del envelope["required_non_claims"]["operation_local"]
        self.assert_blocked(
            envelope, issue_path="required_non_claims.operation_local"
        )
        for key in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS:
            path = f"required_non_claims.operation_local.{key}"
            with self.subTest(case="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)
            with self.subTest(case="true", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, True)
                self.assert_blocked(envelope, issue_path=path)
        for value in (None, "false", 0, []):
            with self.subTest(case="non_mapping", value=value):
                envelope = self.canonical()
                envelope["required_non_claims"]["operation_local"] = value
                self.assert_blocked(
                    envelope, issue_path="required_non_claims.operation_local"
                )
        envelope = self.canonical()
        envelope["required_non_claims"]["operation_local"] = {}
        self.assert_blocked(envelope)
        envelope = self.canonical()
        envelope["required_non_claims"]["operation_local"]["unknown"] = False
        self.assert_blocked(
            envelope, issue_path="required_non_claims.operation_local.unknown"
        )
        self.assertEqual(
            set(self.canonical()["required_non_claims"]["operation_local"]),
            set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS),
        )
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
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
            "relation_object",
            "occurrence",
            "invocation",
            "execution",
            "success",
            "successor",
        ):
            with self.subTest(root=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, issue_path=key)

        envelope = self.canonical()
        envelope["constitutional_event_key"]["unknown"] = {"value": False}
        self.assert_blocked(
            envelope, issue_path="constitutional_event_key.unknown"
        )
        envelope = self.canonical()
        envelope["constitutional_event_key"]["relation"]["unknown"] = False
        self.assert_blocked(
            envelope, issue_path="constitutional_event_key.relation.unknown"
        )
        envelope = self.canonical()
        envelope["ordinary_operation_basis"]["unknown"] = False
        self.assert_blocked(
            envelope, issue_path="ordinary_operation_basis.unknown"
        )

        for key in tuple(resolver.EXECUTABLE_ROOT_KEYS):
            with self.subTest(missing_root=key):
                envelope = self.canonical()
                del envelope[key]
                self.assert_blocked(envelope, issue_path=key)

    def test_validation_precedence(self) -> None:
        allowance_path = "ordinary_operation_basis.source_outcome"

        envelope = self.canonical()
        envelope["intent"] = "DO_NOT_RECORD_RELATION_OPERATION"
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
        self.assert_requires(envelope, allowance_path)

        envelope = self.canonical()
        _set_path(
            envelope, "ordinary_operation_basis.relation_support_found", False
        )
        self.assert_not_recorded(envelope)
        self.assert_recorded(self.canonical())

    def test_relation_identity_pair_topology_and_coupling_restraint(self) -> None:
        result = self.assert_recorded(self.canonical())
        identity = result["persistent_relation_identity"]
        self.assertEqual(identity["relation_id"], "relation_001")
        self.assertEqual(identity["relation_object_cardinality"], 1)
        self.assertIs(identity["identity_allocation_is_relation_existence"], False)

        subject = result["relation_subject"]
        a = subject["first_crossing_a"]
        b = subject["first_crossing_b"]
        pair = subject["pair"]
        self.assertEqual(a["first_crossing_id"], "first_crossing_a_001")
        self.assertEqual(b["first_crossing_id"], "first_crossing_b_001")
        self.assertNotEqual(a["first_crossing_id"], b["first_crossing_id"])
        self.assertEqual(pair["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        for key in (
            "complete_pair_preserved",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "candidate_basis_non_hierarchy_preserved",
            "motion_does_not_erase_regulation",
            "regulation_not_sovereign_over_motion",
            "one_shared_crossing_operation_event",
        ):
            self.assertIs(pair[key], True, key)
        self.assertIs(pair["separate_crossing_occurrences_created"], False)
        self.assertIs(pair["source_semantic_owner_transferred"], False)

        material = result["relation_operation_material"]["relation_pair_evaluation"]
        for field in (
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "source_semantic_owner_transferred",
        ):
            self.assertIs(material[field], False, field)
        operation = result["relation_operation"]
        for field in (
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
        ):
            self.assertIs(operation[field], False, field)

        serialized = repr(result).casefold()
        for forbidden in (
            "relation_002",
            "a_to_b",
            "b_to_a",
            "sender_receiver",
            "source_receiver",
            "relation_retained",
        ):
            self.assertNotIn(forbidden, serialized)

    def test_historical_current_separation_and_route_correction(self) -> None:
        result = self.assert_recorded(self.canonical())
        current = result["current_boundary_result_binding"]
        self.assertEqual(current["result_reference"], resolver.CURRENT_BOUNDARY_RESULT_REFERENCE)
        self.assertEqual(current["result_sha256"], resolver.CURRENT_BOUNDARY_RESULT_SHA256)

        history = result["freshness_and_history"]
        historical = history["historical_operation"]
        self.assertEqual(historical["historical_operation_id"], "relation_operation_001")
        self.assertEqual(
            historical["result_sha256"],
            "0e0b8d5ee6bbc01f77cd6e42463e62e4d10019475efa06359046c364acba9bae",
        )
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
            "success_treated_as_fresh_permission",
        ):
            self.assertIs(historical[key], False, key)
        self.assertNotEqual(
            historical["result_reference"], current["result_reference"]
        )

        bridge = result["reversibility_bridge"]
        self.assertEqual(bridge["boundary_id"], "relation_reversibility_boundary_001")
        self.assertEqual(bridge["boundary_type"], "RELATION_REVERSIBILITY_BOUNDARY")
        self.assertEqual(bridge["boundary_version"], "0.1.0")
        self.assertEqual(
            bridge["boundary_contract_sha256"],
            "422a9ce767c9273a5c898d1d9d7da6d57a0ba7c5da4ac54ed3be9995ae2d8bd3",
        )
        direct_key = (
            "direct_relation_operation_to_presence_boundary_without_"
            "reversibility_boundary_consideration"
        )
        self.assertIs(bridge[direct_key], False)
        self.assertEqual(
            result["relation_operation"]["admissible_future_route"],
            "RELATION_OPERATION_THEN_RELATION_REVERSIBILITY_BOUNDARY_ONLY",
        )
        self.assertNotIn(
            "RELATION_OPERATION_THEN_PRESENCE_BOUNDARY_ONLY", repr(result)
        )
        self.assertNotIn("newly", repr(result).casefold())
        self.assertNotIn("inserted", repr(result).casefold())

        stop = result["downstream_stopping_point"]
        self.assertEqual(
            stop,
            {
                "admissible_future_route": (
                    "RELATION_OPERATION_THEN_RELATION_REVERSIBILITY_BOUNDARY_ONLY"
                ),
                "next_separately_bounded_rank": "RELATION_REVERSIBILITY_BOUNDARY",
            },
        )
        keys = _all_mapping_keys(result)
        for absent in (
            "relation_reversibility_result",
            "relation_lapse_result",
            "presence_boundary_result",
            "presence_result",
        ):
            self.assertNotIn(absent, keys)
        operation = result["relation_operation"]
        for field in (
            "direct_relation_to_presence",
            "presence_established",
            "standing_created",
            "currentness_created",
            "authority_created",
            "identity_created",
            "runtime_created",
            "api_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(operation[field], False, field)

    def test_deterministic_rerender_changed_binding_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        self.assertEqual(
            first["current_relation_operation_event"],
            second["current_relation_operation_event"],
        )
        self.assertNotIn("sibling_relation", repr(first))
        self.assertNotIn("relation_002", repr(first))

        changed = self.canonical()
        path = "constitutional_event_key.operation_event.relation_id"
        _set_path(changed, path, "relation_002")
        self.assert_blocked(changed, issue_path=path)

        names = _all_code_names(
            resolver.resolve_relation_operation_v0_min_v3,
            resolver.build_declared_relation_operation_v0_min_v3_request,
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
            "resolve_relation_boundary_v0_min_v2",
            "resolve_relation_operation_v0_min",
            "resolve_relation_reversibility_boundary_v0_min",
            "resolve_relation_lapse_boundary_v0_min",
            "resolve_relation_lapse_operation_v0_min",
            "resolve_presence_boundary_v0_min",
            "resolve_presence_operation_v0_min",
        ):
            self.assertNotIn(forbidden, vars(resolver))

        with mock.patch("builtins.open", side_effect=AssertionError("I/O")):
            self.assertEqual(
                self.resolve(self.canonical())["outcome"],
                resolver.OUTCOME_RECORDED,
            )


if __name__ == "__main__":
    unittest.main()
