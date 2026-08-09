"""Adversarial proof for the current-line RELATION_BOUNDARY V2 resolver."""

from __future__ import annotations

import builtins
import hashlib
import os
from copy import deepcopy
from pathlib import Path
import subprocess
import sys
import time
import types
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_relation_boundary_v0_min_v2 as resolver


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


class RelationBoundaryV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_relation_boundary_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_relation_boundary_v0_min_v2(envelope)

    def assert_no_positive_boundary(self, result: dict[str, object]) -> None:
        boundary = result["relation_boundary"]
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
        block = result["block"]
        self.assertTrue(block["blocked"])
        self.assertIn(block["code"], resolver.BLOCK_CODES)
        self.assertFalse(block["requires_first_crossing"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_boundary(result)
        return result

    def assert_requires(
        self,
        envelope: object,
        missing_path: str,
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(
            result["outcome"], resolver.OUTCOME_REQUIRES_FIRST_CROSSING
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_first_crossing"])
        self.assertIsNone(result["block"]["code"])
        review = result["ordinary_first_crossing_basis_review"]
        self.assertEqual(review["missing_paths"], [missing_path])
        self.assertFalse(review["requires_first_crossing_creates_retry_permission"])
        self.assertFalse(
            review["requires_first_crossing_creates_successor_permission"]
        )
        self.assert_no_positive_boundary(result)
        return result

    def assert_allowed(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_first_crossing"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["issue_path"])
        self.assertEqual(result["failed_check_count"], 0)
        return result

    def test_manifest_identity_classification_and_outcome_lock(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 143)
        self.assertEqual(len(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS), 9)
        self.assertEqual(
            len(resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_PATHS), 8
        )
        self.assertEqual(len(resolver.TARGET_LOCAL_NON_CLAIM_PATHS), 71)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 79)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 234)

        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            resolver._leaf_paths(
                resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
                "constitutional_event_key",
            ),
            tuple(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS),
            tuple(resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_PATHS),
            tuple(resolver.TARGET_LOCAL_NON_CLAIM_PATHS),
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

        parent_paths: set[str] = set()
        for path in resolver.ALL_REQUIRED_PATHS:
            parts = path.split(".")
            parent_paths.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parent_paths & resolver.ALL_REQUIRED_PATHS)

        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "RELATION_BOUNDARY_BLOCKED",
                "RELATION_BOUNDARY_REQUIRES_FIRST_CROSSING",
                "RELATION_BOUNDARY_ALLOWED",
            ),
        )
        self.assertNotIn("RELATION_BOUNDARY_NOT_RECORDED", resolver.OUTCOME_FAMILY)
        self.assertEqual(resolver.BOUNDARY_ID, "relation_boundary_001")
        self.assertNotIn("relation_boundary_002", repr(vars(resolver)))
        self.assertEqual(
            resolver.CURRENT_CROSSING_RESULT_REFERENCE,
            "artifacts/first_crossing_operation_v0_min_v3/"
            "first_crossing_operation_001__first_crossing_operation_v0_min_v3_result.json",
        )
        self.assertEqual(
            resolver.CURRENT_CROSSING_RESULT_SHA256,
            "bb5a7a745f0db7a223a84fd0574cc7dc1b7975d6fba909803e73602f430cbd14",
        )
        self.assertEqual(len(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS), 7)
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS)
        )
        self.assertNotIn("relation_boundary_result", resolver.TARGET_LOCAL_NON_CLAIM_KEYS)
        self.assertNotIn("coupling_authorized", resolver.TARGET_LOCAL_NON_CLAIM_KEYS)
        self.assertNotIn(
            "automatic_successor_created", resolver.TARGET_LOCAL_NON_CLAIM_KEYS
        )

    def test_canonical_allowed_pair_topology_and_boundary_restraint(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.assert_allowed(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["resolver_module"], resolver.RESOLVER_MODULE)
        self.assertEqual(result["result_version"], "0.2.0")

        boundary = result["relation_boundary"]
        self.assertEqual(boundary["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(boundary["boundary_type"], resolver.BOUNDARY_TYPE)
        self.assertEqual(boundary["boundary_version"], resolver.BOUNDARY_VERSION)
        self.assertEqual(boundary["boundary_scope"], resolver.BOUNDARY_SCOPE)
        self.assertEqual(
            boundary["relation_boundary_result"],
            resolver.RESULT_OPERATION_CONSIDERATION_ALLOWED,
        )
        true_boundary_fields = {
            key for key, value in boundary.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_boundary_fields, set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
        )
        for field in resolver.TARGET_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(boundary[field], False, field)
        self.assertNotIn("relation_001", repr(result))

        subject = result["relation_side_subject"]
        self.assertEqual(subject["topology"], "PAIR_SCOPED_NON_DIRECTIONAL")
        a = subject["first_crossing_a"]
        b = subject["first_crossing_b"]
        pair = subject["pair"]
        self.assertEqual(a["first_crossing_id"], "first_crossing_a_001")
        self.assertEqual(b["first_crossing_id"], "first_crossing_b_001")
        self.assertNotEqual(a["first_crossing_id"], b["first_crossing_id"])
        self.assertNotEqual(a["descendant_body_id"], b["descendant_body_id"])
        self.assertEqual(
            pair["first_crossing_pair_scope"],
            "SEPARATE_FIRST_CROSSING_RECORDS_ONLY",
        )
        self.assertEqual(
            pair["descendant_body_pair_scope"],
            "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
        )
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

        all_keys = _all_mapping_keys(result)
        for forbidden in (
            "a_to_b_relation",
            "b_to_a_relation",
            "symmetry_created",
            "bidirectionality_created",
            "source_receiver_roles_created",
            "sender_receiver_roles_created",
            "crossings_merged",
            "crossings_ranked",
            "third_participant_created",
        ):
            self.assertNotIn(forbidden, all_keys)
        self.assertEqual(
            result["source_binding"]["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        self.assertFalse(pair["source_semantic_owner_transferred"])

        for field in (
            "relation_authorized",
            "relation_created",
            "relation_operation_performed",
            "coupling_created",
            "standing_descendant_created",
            "standing_created",
            "currentness_created",
            "authority_created",
            "presence_established",
            "identity_created",
            "runtime_created",
            "api_created",
            "output_authorized",
            "action_authorized",
            "synchronization_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(boundary[field], False, field)

    def test_every_event_leaf_required_and_representative_corruption_blocks(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(posture="event_missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

        mutation_paths = (
            "constitutional_event_key.target.boundary_id",
            "constitutional_event_key.target.boundary_contract_sha256",
            "constitutional_event_key.current_crossing_result.result_reference",
            "constitutional_event_key.current_crossing_result.result_sha256",
            "constitutional_event_key.current_crossing_result.result_version",
            "constitutional_event_key.current_crossing_result.resolver_module",
            "constitutional_event_key.crossing_operation.operation_id",
            "constitutional_event_key.crossing_operation.operation_contract_sha256",
            "constitutional_event_key.first_crossing_boundary.boundary_id",
            "constitutional_event_key.crossing_operation_event.persistent_boundary_id",
            "constitutional_event_key.creation_operation.operation_id",
            "constitutional_event_key.creation_operation_event.fresh_operation_request_id",
            "constitutional_event_key.relation_boundary_event.persistent_relation_boundary_id",
            "constitutional_event_key.first_crossing_a.first_crossing_id",
            "constitutional_event_key.first_crossing_b.first_crossing_id",
            "constitutional_event_key.first_crossing_a.descendant_body_id",
            "constitutional_event_key.first_crossing_b.descendant_body_id",
            "constitutional_event_key.first_crossing_a.candidate_basis_id",
            "constitutional_event_key.first_crossing_b.candidate_basis_id",
            "constitutional_event_key.pair.complete_pair_preserved",
            "constitutional_event_key.pair.descendant_bodies_remain_sibling",
            "constitutional_event_key.pair.one_shared_crossing_operation_event",
            "constitutional_event_key.source.selected_surface_semantic_owner",
            "constitutional_event_key.source_applicability.source_applicability_id",
            "constitutional_event_key.source_applicability.source_applicability_outcome",
            "constitutional_event_key.source_stopping.automatic_successor_created",
            "constitutional_event_key.freshness.current_crossing_result_identity_declared",
            "constitutional_event_key.freshness.historical_relation_result_replayed",
            "constitutional_event_key.historical_relation.result_sha256",
            "constitutional_event_key.historical_relation.outcome",
            "constitutional_event_key.historical_relation.boundary_result",
            "constitutional_event_key.non_claim_attribution.source_crossing_operation.owner",
            "constitutional_event_key.non_claim_attribution.source_creation_operation.owner",
            "constitutional_event_key.non_claim_attribution.source_family.owner",
            "constitutional_event_key.non_claim_attribution.target_local.owner",
        )
        self.assertTrue(set(mutation_paths) <= resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)
        for path in mutation_paths:
            with self.subTest(posture="event_changed", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        corruption_cases = (
            ("ordinary_first_crossing_basis.source_outcome", "WRONG_OUTCOME"),
            (
                "ordinary_first_crossing_basis.source_operation_result",
                "WRONG_RESULT",
            ),
            ("ordinary_first_crossing_basis.crossing_performed", False),
            ("constitutional_event_key.current_crossing_result.blocked", True),
            ("constitutional_event_key.current_crossing_result.not_recorded", True),
            (
                "constitutional_event_key.current_crossing_result.requires_boundary_allowance",
                True,
            ),
            ("ordinary_first_crossing_basis.first_crossing_a_recorded", False),
        )
        for path, replacement in corruption_cases:
            with self.subTest(posture="pinned_source_corruption", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, replacement)
                result = self.assert_blocked(envelope, issue_path=path)
                self.assertNotEqual(
                    result["outcome"], resolver.OUTCOME_REQUIRES_FIRST_CROSSING
                )

        historical_substitution = self.canonical()
        current_path = (
            "constitutional_event_key.current_crossing_result.result_reference"
        )
        historical_path = (
            "constitutional_event_key.historical_relation.result_reference"
        )
        _set_path(
            historical_substitution,
            current_path,
            _get_path(historical_substitution, historical_path),
        )
        self.assert_blocked(historical_substitution, issue_path=current_path)

    def test_ordinary_predecessor_omissions_require_and_contradictions_block(self) -> None:
        for path in sorted(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS):
            with self.subTest(posture="ordinary_missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_requires(envelope, path)

        for path in sorted(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS):
            with self.subTest(posture="ordinary_wrong", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        bool_path = "ordinary_first_crossing_basis.first_crossing_supported"
        for malformed in (None, "true", 1, {}, []):
            with self.subTest(posture="ordinary_malformed", value=malformed):
                envelope = self.canonical()
                _set_path(envelope, bool_path, malformed)
                self.assert_blocked(envelope, issue_path=bool_path)
        self.assertEqual(self.assert_allowed(self.canonical())["outcome"], resolver.OUTCOME_ALLOWED)

    def test_non_claim_maps_are_closed_exact_false_and_owned(self) -> None:
        map_cases = (
            (
                "source_crossing_operation",
                resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_KEYS,
                resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_PATHS,
            ),
            (
                "target_local",
                resolver.TARGET_LOCAL_NON_CLAIM_KEYS,
                resolver.TARGET_LOCAL_NON_CLAIM_PATHS,
            ),
        )
        for map_name, keys, paths in map_cases:
            map_path = f"required_non_claims.{map_name}"
            self.assertEqual(paths, {f"{map_path}.{key}" for key in keys})

            envelope = self.canonical()
            _remove_path(envelope, map_path)
            self.assert_blocked(envelope, issue_path=map_path)

            envelope = self.canonical()
            _set_path(envelope, map_path, [])
            self.assert_blocked(envelope, issue_path=map_path)

            envelope = self.canonical()
            envelope["required_non_claims"][map_name]["unsupported"] = False
            self.assert_blocked(envelope, issue_path=f"{map_path}.unsupported")

            representative = f"{map_path}.{keys[0]}"
            envelope = self.canonical()
            _set_path(envelope, representative, 0)
            self.assert_blocked(envelope, issue_path=representative)

            for key in keys:
                path = f"{map_path}.{key}"
                with self.subTest(map=map_name, posture="missing", key=key):
                    envelope = self.canonical()
                    _remove_path(envelope, path)
                    self.assert_blocked(envelope, issue_path=path)
                with self.subTest(map=map_name, posture="true", key=key):
                    envelope = self.canonical()
                    _set_path(envelope, path, True)
                    self.assert_blocked(envelope, issue_path=path)

        canonical = self.canonical()["required_non_claims"]
        self.assertEqual(
            set(canonical["source_crossing_operation"]),
            set(resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_KEYS),
        )
        self.assertEqual(
            set(canonical["target_local"]),
            set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS),
        )
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(canonical["target_local"])
        )
        self.assertNotIn("relation_boundary_result", canonical["target_local"])
        self.assertNotIn("coupling_authorized", canonical["target_local"])
        allowed = self.assert_allowed(self.canonical())
        self.assertEqual(
            set(allowed["source_crossing_operation_non_claims"]),
            set(resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_KEYS),
        )
        self.assertEqual(
            set(allowed["target_local_non_claims"]),
            set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS),
        )

    def test_unsupported_input_precedence_history_and_downstream_restraint(self) -> None:
        unsupported_cases: list[tuple[str, object]] = []

        root = self.canonical()
        root["unsupported"] = True
        unsupported_cases.append(("unsupported", root))

        event_section = self.canonical()
        event_section["constitutional_event_key"]["unsupported"] = {}
        unsupported_cases.append(("constitutional_event_key.unsupported", event_section))

        event_leaf = self.canonical()
        event_leaf["constitutional_event_key"]["target"]["unsupported"] = True
        unsupported_cases.append(
            ("constitutional_event_key.target.unsupported", event_leaf)
        )

        ordinary = self.canonical()
        ordinary["ordinary_first_crossing_basis"]["unsupported"] = True
        unsupported_cases.append(
            ("ordinary_first_crossing_basis.unsupported", ordinary)
        )

        source_nc = self.canonical()
        source_nc["required_non_claims"]["source_crossing_operation"][
            "unsupported"
        ] = False
        unsupported_cases.append(
            ("required_non_claims.source_crossing_operation.unsupported", source_nc)
        )

        target_nc = self.canonical()
        target_nc["required_non_claims"]["target_local"]["unsupported"] = False
        unsupported_cases.append(
            ("required_non_claims.target_local.unsupported", target_nc)
        )

        for issue_path, envelope in unsupported_cases:
            with self.subTest(issue_path=issue_path):
                self.assert_blocked(envelope, issue_path=issue_path)

        for caller_key in (
            "outcome",
            "result",
            "check",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "artifact",
            "relation",
            "coupling",
            "standing",
            "occurrence",
            "invocation",
            "execution",
            "success",
            "successor_selector",
        ):
            with self.subTest(caller_key=caller_key):
                envelope = self.canonical()
                envelope[caller_key] = True
                self.assert_blocked(envelope, issue_path=caller_key)

        self.assert_blocked([], issue_path="$::mapping_cardinality")
        for root_key in resolver.EXECUTABLE_ROOT_KEYS:
            with self.subTest(missing_root=root_key):
                envelope = self.canonical()
                del envelope[root_key]
                self.assert_blocked(envelope, issue_path=root_key)

        ordinary_path = sorted(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS)[0]
        event_path = sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)[0]
        non_claim_path = sorted(
            resolver.SOURCE_CROSSING_OPERATION_NON_CLAIM_PATHS
        )[0]

        envelope = self.canonical()
        envelope["intent"] = "CHANGED"
        _remove_path(envelope, ordinary_path)
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        _remove_path(envelope, event_path)
        _remove_path(envelope, ordinary_path)
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        _set_path(envelope, non_claim_path, True)
        _remove_path(envelope, ordinary_path)
        self.assert_blocked(envelope, issue_path=non_claim_path)

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        self.assert_requires(envelope, ordinary_path)
        allowed = self.assert_allowed(self.canonical())

        history = allowed["freshness_and_history"]
        historical = history["historical_relation"]
        self.assertEqual(historical["boundary_id"], resolver.BOUNDARY_ID)
        self.assertEqual(
            historical["result_reference"], resolver.HISTORICAL_RELATION_RESULT_REFERENCE
        )
        self.assertEqual(
            historical["result_sha256"], resolver.HISTORICAL_RELATION_RESULT_SHA256
        )
        self.assertEqual(historical["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(
            historical["boundary_result"],
            resolver.RESULT_OPERATION_CONSIDERATION_ALLOWED,
        )
        for field in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_event",
            "result_replayed",
        ):
            self.assertIs(historical[field], False, field)
        self.assertEqual(
            allowed["current_crossing_result_binding"]["result_reference"],
            resolver.CURRENT_CROSSING_RESULT_REFERENCE,
        )

        stop = allowed["downstream_stopping_point"]
        self.assertEqual(stop["next_separately_bounded_rank"], "RELATION_OPERATION")
        self.assertEqual(
            stop["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE
        )
        for key, value in stop.items():
            if type(value) is bool:
                self.assertIs(value, False, key)
        self.assertFalse(stop["relation_operation_invoked"])
        self.assertFalse(stop["relation_operation_authorized"])
        self.assertFalse(stop["relation_operation_performed"])
        self.assertFalse(stop["relation_created"])
        self.assertFalse(stop["coupling_created"])
        self.assertFalse(stop["automatic_successor_created"])

    def test_deterministic_rerender_changed_binding_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)

        event = first["current_relation_boundary_event"]
        self.assertEqual(event["persistent_relation_boundary_id"], resolver.BOUNDARY_ID)
        self.assertTrue(event["same_identity_same_binding_is_deterministic_rerender"])
        self.assertFalse(event["resolver_call_count_is_event_count"])
        self.assertFalse(event["sibling_event_identity_allocated"])

        changed_path = (
            "constitutional_event_key.relation_boundary_event."
            "fresh_creation_operation_request_id"
        )
        changed = self.canonical()
        _set_path(changed, changed_path, "descendant_body_creation_operation_request_002")
        self.assert_blocked(changed, issue_path=changed_path)

        inspected_functions = (
            resolver.build_declared_relation_boundary_v0_min_v2_request,
            resolver.resolve_relation_boundary_v0_min_v2,
            resolver._control_review,
            resolver._validate_exact_mapping,
            resolver._ordinary_review,
            resolver._build_result,
            resolver._boundary_object,
        )
        names = _all_code_names(*inspected_functions)
        forbidden_names = {
            "open",
            "read_text",
            "read_bytes",
            "write_text",
            "write_bytes",
            "iterdir",
            "glob",
            "rglob",
            "exists",
            "walk",
            "run",
            "sha256",
            "time",
            "resolve_first_crossing_operation_v0_min_v3",
            "resolve_relation_boundary_v0_min",
            "resolve_relation_operation",
        }
        self.assertFalse(names & forbidden_names)

        def forbidden(*args: object, **kwargs: object) -> object:
            raise AssertionError("resolver attempted an impure operation")

        with (
            mock.patch.object(builtins, "open", side_effect=forbidden),
            mock.patch.object(Path, "read_text", side_effect=forbidden),
            mock.patch.object(Path, "read_bytes", side_effect=forbidden),
            mock.patch.object(Path, "write_text", side_effect=forbidden),
            mock.patch.object(Path, "write_bytes", side_effect=forbidden),
            mock.patch.object(Path, "iterdir", side_effect=forbidden),
            mock.patch.object(Path, "glob", side_effect=forbidden),
            mock.patch.object(Path, "rglob", side_effect=forbidden),
            mock.patch.object(Path, "exists", side_effect=forbidden),
            mock.patch.object(os, "walk", side_effect=forbidden),
            mock.patch.object(subprocess, "run", side_effect=forbidden),
            mock.patch.object(hashlib, "sha256", side_effect=forbidden),
            mock.patch.object(time, "time", side_effect=forbidden),
        ):
            pure_request = resolver.build_declared_relation_boundary_v0_min_v2_request()
            self.assertEqual(self.resolve(pure_request), first)


if __name__ == "__main__":
    unittest.main()
