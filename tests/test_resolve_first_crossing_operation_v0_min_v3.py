"""Adversarial proof for the current-line FIRST_CROSSING_OPERATION V3 resolver."""

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

import resolve_first_crossing_operation_v0_min_v3 as resolver


def _parts(path: str) -> list[str]:
    return path.split(".")


def _remove_path(value: dict[str, object], path: str) -> None:
    parts = _parts(path)
    current = value
    for part in parts[:-1]:
        current = current[part]  # type: ignore[assignment,index]
    del current[parts[-1]]


def _set_path(value: dict[str, object], path: str, replacement: object) -> None:
    parts = _parts(path)
    current = value
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


class FirstCrossingOperationV0MinV3Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_first_crossing_operation_v0_min_v3_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_first_crossing_operation_v0_min_v3(envelope)

    def assert_no_positive_operation(self, result: dict[str, object]) -> None:
        operation = result["first_crossing_operation"]
        for field in resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS:
            self.assertIs(operation[field], False, field)
        self.assertIsNone(result["first_crossing_operation_material"])

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
        self.assertFalse(block["requires_boundary_allowance"])
        self.assertFalse(block["not_recorded"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_operation(result)
        return result

    def assert_requires(
        self,
        envelope: object,
        missing_path: str,
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(
            result["outcome"], resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_boundary_allowance"])
        review = result["ordinary_boundary_allowance_review"]
        self.assertEqual(review["missing_paths"], [missing_path])
        self.assertFalse(
            review["requires_boundary_allowance_creates_retry_permission"]
        )
        self.assertFalse(
            review["requires_boundary_allowance_creates_successor_permission"]
        )
        self.assert_no_positive_operation(result)
        return result

    def assert_not_recorded(self, envelope: object) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(result["outcome"], resolver.OUTCOME_NOT_RECORDED)
        self.assertFalse(result["block"]["blocked"])
        self.assertFalse(result["block"]["requires_boundary_allowance"])
        self.assertTrue(result["block"]["not_recorded"])
        operation = result["first_crossing_operation"]
        self.assertEqual(operation["first_crossing_result"], resolver.RESULT_NOT_SUPPORTED)
        self.assert_no_positive_operation(result)
        review = result["ordinary_first_crossing_support_review"]
        for key, value in review.items():
            if key.startswith("not_recorded_creates_"):
                self.assertIs(value, False, key)
        stop = result["downstream_stopping_point"]
        self.assertFalse(stop["relation_boundary_invoked"])
        self.assertFalse(stop["automatic_successor_created"])
        return result

    def test_manifest_identity_classification_and_outcome_lock(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 114)
        self.assertEqual(len(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS), 7)
        self.assertEqual(len(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS), 1)
        self.assertEqual(len(resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS), 9)
        self.assertEqual(len(resolver.OPERATION_LOCAL_NON_CLAIM_PATHS), 62)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 71)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 196)

        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            resolver._leaf_paths(
                resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
                "constitutional_event_key",
            ),
            tuple(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS),
            tuple(resolver.ORDINARY_FIRST_CROSSING_BASIS_PATHS),
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

        parent_paths: set[str] = set()
        for path in resolver.ALL_REQUIRED_PATHS:
            parts = path.split(".")
            parent_paths.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parent_paths & resolver.ALL_REQUIRED_PATHS)

        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "FIRST_CROSSING_OPERATION_BLOCKED",
                "FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE",
                "FIRST_CROSSING_OPERATION_NOT_RECORDED",
                "FIRST_CROSSING_OPERATION_RECORDED",
            ),
        )
        self.assertEqual(resolver.OPERATION_ID, "first_crossing_operation_001")
        self.assertNotIn("first_crossing_operation_002", repr(vars(resolver)))
        self.assertEqual(
            resolver.CURRENT_BOUNDARY_RESULT_SHA256,
            "bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1",
        )
        self.assertEqual(len(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS), 14)
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        )
        self.assertNotIn(
            "automatic_successor_created", resolver.OPERATION_LOCAL_NON_CLAIM_KEYS
        )
        self.assertNotIn(
            "relation_boundary_invoked", resolver.OPERATION_LOCAL_NON_CLAIM_KEYS
        )

    def test_canonical_recorded_material_occurrence_and_stopping_point(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.resolve(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(result["failed_check_count"], 0)

        operation = result["first_crossing_operation"]
        self.assertEqual(operation["first_crossing_result"], resolver.RESULT_SUPPORTED)
        true_operation_fields = {
            key for key, value in operation.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_operation_fields, set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
        )
        for field in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(operation[field], False, field)

        material = result["first_crossing_operation_material"]
        self.assertEqual(
            set(material),
            {
                "first_crossing_a_evaluation",
                "first_crossing_b_evaluation",
                "first_crossing_pair_evaluation",
            },
        )
        a = material["first_crossing_a_evaluation"]
        b = material["first_crossing_b_evaluation"]
        pair = material["first_crossing_pair_evaluation"]
        expected_a_identity = {
            "first_crossing_id": "first_crossing_a_001",
            "descendant_body_id": "descendant_body_a_001",
            "candidate_standing_source_id": "descendant_body_basis_candidate_a_001",
            "candidate_role": "CANDIDATE_A",
            "candidate_standing_label": "CANDIDATE_A_STANDING",
            "candidate_basis_id": (
                "descendant_body_basis_candidate_a_001__"
                "motion_side_admissible_variation_basis"
            ),
            "candidate_basis_label": (
                "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
            ),
            "candidate_basis_scope": "Motion-side admissible variation",
        }
        expected_b_identity = {
            "first_crossing_id": "first_crossing_b_001",
            "descendant_body_id": "descendant_body_b_001",
            "candidate_standing_source_id": "descendant_body_basis_candidate_b_001",
            "candidate_role": "CANDIDATE_B",
            "candidate_standing_label": "CANDIDATE_B_STANDING",
            "candidate_basis_id": (
                "descendant_body_basis_candidate_b_001__"
                "regulation_side_admissibility_bounds_basis"
            ),
            "candidate_basis_label": (
                "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
            ),
            "candidate_basis_scope": "Regulation-side admissibility bounds",
        }
        for key, value in expected_a_identity.items():
            self.assertEqual(a[key], value)
        for key, value in expected_b_identity.items():
            self.assertEqual(b[key], value)
        self.assertNotEqual(a["first_crossing_id"], b["first_crossing_id"])
        self.assertNotEqual(a["descendant_body_id"], b["descendant_body_id"])

        positive_body_fields = (
            "descendant_body_created",
            "first_crossing_supported",
            "first_crossing_authorized",
            "crossing_authorized",
            "first_crossing_performed",
            "crossing_performed",
            "first_crossing_recorded",
        )
        for body in (a, b):
            for field in positive_body_fields:
                self.assertIs(body[field], True, field)
            self.assertIs(body["descendant_body_is_first_crossing"], False)
            for field in (
                "relation_created",
                "coupling_created",
                "presence_established",
                "identity_created",
            ):
                self.assertIs(body[field], False, field)

        expected_pair_true = {
            "both_first_crossings_supported",
            "both_first_crossings_authorized",
            "both_first_crossings_performed",
            "both_first_crossings_recorded",
            "first_crossing_a_recorded",
            "first_crossing_b_recorded",
            "crossing_authorized",
            "crossing_performed",
            "descendant_bodies_remain_sibling",
            "descendant_body_non_hierarchy_preserved",
            "candidate_standing_non_hierarchy_preserved",
            "motion_does_not_erase_regulation",
            "regulation_not_sovereign_over_motion",
        }
        self.assertEqual(pair["first_crossing_pair_scope"], resolver.FIRST_CROSSING_PAIR_SCOPE)
        self.assertEqual(
            {key for key, value in pair.items() if type(value) is bool and value},
            expected_pair_true,
        )
        for field in (
            "relation_created",
            "coupling_assigned",
            "coupling_created",
            "third_candidate_created",
            "third_model_admitted",
            "presence_established",
            "identity_created",
            "standing_descendant_created",
            "descendant_standing_check_performed",
            "follow_on_authorized",
        ):
            self.assertIs(pair[field], False, field)

        event = result["current_operation_event"]
        self.assertEqual(event["persistent_operation_id"], resolver.OPERATION_ID)
        self.assertTrue(event["one_shared_operation_event"])
        self.assertFalse(event["separate_operation_occurrences_created"])
        self.assertFalse(event["sibling_event_identity_allocated"])
        subject = result["descendant_body_subject"]
        self.assertFalse(subject["bodies_merged"])
        self.assertFalse(subject["bodies_ranked"])
        self.assertFalse(subject["coupling_created"])
        self.assertFalse(subject["source_semantic_owner_transferred"])
        self.assertEqual(
            result["source_binding"]["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )

        self.assertTrue(operation["first_crossing_authorized"])
        self.assertTrue(operation["crossing_authorized"])
        self.assertTrue(operation["first_crossing_performed"])
        self.assertTrue(operation["crossing_performed"])
        self.assertTrue(operation["first_crossing_result_recorded"])
        self.assertTrue(operation["first_crossing_a_recorded"])
        self.assertTrue(operation["first_crossing_b_recorded"])
        self.assertNotIn("crossing_occurrence_established", operation)
        self.assertNotIn("operation_occurrence_established", operation)

        stop = result["downstream_stopping_point"]
        self.assertEqual(stop["next_separately_bounded_rank"], "RELATION_BOUNDARY")
        self.assertEqual(stop["admissible_future_route"], resolver.ADMISSIBLE_FUTURE_ROUTE)
        for key, value in stop.items():
            if type(value) is bool:
                self.assertIs(value, False, key)
        for field in (
            "standing_descendant_created",
            "standing_created",
            "descendant_standing_check_performed",
            "relation_created",
            "currentness_created",
            "authority_created",
            "presence_established",
            "identity_created",
            "coupling_created",
            "runtime_created",
            "api_created",
            "output_authorized",
            "action_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(operation[field], False, field)

    def test_ordinary_allowance_and_support_allocations(self) -> None:
        for path in sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS):
            with self.subTest(posture="allowance_missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_requires(envelope, path)

        for path in sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS):
            with self.subTest(posture="allowance_contradictory", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        bool_path = (
            "ordinary_operation_basis.first_crossing_operation_consideration_allowed"
        )
        for malformed in ("true", 1, None):
            with self.subTest(posture="allowance_malformed", value=malformed):
                envelope = self.canonical()
                _set_path(envelope, bool_path, malformed)
                self.assert_blocked(envelope, issue_path=bool_path)

        support_path = "ordinary_operation_basis.first_crossing_support_found"
        missing = self.canonical()
        _remove_path(missing, support_path)
        self.assert_not_recorded(missing)
        for unsupported in (False, None, "true", 1, {}, []):
            with self.subTest(posture="support_not_exact_true", value=unsupported):
                envelope = self.canonical()
                _set_path(envelope, support_path, unsupported)
                self.assert_not_recorded(envelope)
        self.assertEqual(self.resolve(self.canonical())["outcome"], resolver.OUTCOME_RECORDED)

        self.assertEqual(resolver._derive_pair_support(True), (True, True))
        for unsupported in (False, None, "true", 1, {}, []):
            self.assertEqual(resolver._derive_pair_support(unsupported), (False, False))
        self.assertEqual(
            set(resolver.EXPECTED_ORDINARY_BOUNDARY_ALLOWANCE)
            | {"first_crossing_support_found"},
            set(self.canonical()["ordinary_operation_basis"]),
        )
        self.assertNotIn(
            "first_crossing_a_supported",
            self.canonical()["ordinary_operation_basis"],
        )
        self.assertNotIn(
            "first_crossing_b_supported",
            self.canonical()["ordinary_operation_basis"],
        )

    def test_every_event_leaf_required_and_representative_mutations_block(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(posture="event_missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

        mutation_paths = (
            "constitutional_event_key.target.operation_id",
            "constitutional_event_key.target.operation_contract_sha256",
            "constitutional_event_key.current_boundary_result.result_reference",
            "constitutional_event_key.current_boundary_result.result_sha256",
            "constitutional_event_key.current_boundary_result.blocked",
            "constitutional_event_key.boundary.boundary_id",
            "constitutional_event_key.boundary.boundary_contract_sha256",
            "constitutional_event_key.creation_operation.operation_id",
            "constitutional_event_key.creation_operation_event.fresh_operation_request_id",
            "constitutional_event_key.descendant_body_a.descendant_body_id",
            "constitutional_event_key.descendant_body_a.candidate_basis_id",
            "constitutional_event_key.descendant_body_b.descendant_body_id",
            "constitutional_event_key.descendant_body_b.candidate_basis_id",
            "constitutional_event_key.pair.complete_pair_preserved",
            "constitutional_event_key.pair.descendant_bodies_remain_sibling",
            "constitutional_event_key.source.selected_surface_semantic_owner",
            "constitutional_event_key.source_applicability.source_applicability_id",
            "constitutional_event_key.source_applicability.source_applicability_outcome",
            "constitutional_event_key.freshness.fresh_operation_request_identity_declared",
            "constitutional_event_key.freshness.historical_operation_result_replayed",
            "constitutional_event_key.historical_operation.result_sha256",
            "constitutional_event_key.historical_operation.outcome",
            "constitutional_event_key.historical_operation.first_crossing_result",
            "constitutional_event_key.non_claim_attribution.source_boundary.owner",
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

        historical_substitution = self.canonical()
        current_path = "constitutional_event_key.current_boundary_result.result_reference"
        historical_path = "constitutional_event_key.historical_operation.result_reference"
        _set_path(
            historical_substitution,
            current_path,
            _get_path(historical_substitution, historical_path),
        )
        self.assert_blocked(historical_substitution, issue_path=current_path)

        historical_cannot_supply_support = self.canonical()
        _remove_path(
            historical_cannot_supply_support,
            "ordinary_operation_basis.first_crossing_support_found",
        )
        self.assert_not_recorded(historical_cannot_supply_support)

    def test_non_claim_maps_are_closed_exact_and_false(self) -> None:
        map_cases = (
            (
                "source_boundary",
                resolver.SOURCE_BOUNDARY_NON_CLAIM_KEYS,
                resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS,
            ),
            (
                "operation_local",
                resolver.OPERATION_LOCAL_NON_CLAIM_KEYS,
                resolver.OPERATION_LOCAL_NON_CLAIM_PATHS,
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

        self.assertEqual(
            set(self.canonical()["required_non_claims"]["operation_local"]),
            set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS),
        )
        self.assertFalse(
            set(resolver.POSITIVE_OPERATION_BOOLEAN_FIELDS)
            & set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        )
        self.assertNotIn(
            "automatic_successor_created", resolver.OPERATION_LOCAL_NON_CLAIM_KEYS
        )

    def test_unsupported_input_and_precedence(self) -> None:
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
        ordinary["ordinary_operation_basis"]["unsupported"] = True
        unsupported_cases.append(("ordinary_operation_basis.unsupported", ordinary))

        source_nc = self.canonical()
        source_nc["required_non_claims"]["source_boundary"]["unsupported"] = False
        unsupported_cases.append(
            ("required_non_claims.source_boundary.unsupported", source_nc)
        )

        local_nc = self.canonical()
        local_nc["required_non_claims"]["operation_local"]["unsupported"] = False
        unsupported_cases.append(
            ("required_non_claims.operation_local.unsupported", local_nc)
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
            "occurrence",
            "crossing_selector",
            "invocation",
            "execution",
            "success_selector",
            "standing",
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
        for control_path in ("intent", "operation_question"):
            envelope = self.canonical()
            _set_path(envelope, control_path, "CHANGED")
            self.assert_blocked(envelope, issue_path=control_path)

        allowance_path = sorted(resolver.ORDINARY_BOUNDARY_ALLOWANCE_PATHS)[0]
        event_path = sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)[0]
        non_claim_path = sorted(resolver.SOURCE_BOUNDARY_NON_CLAIM_PATHS)[0]
        support_path = "ordinary_operation_basis.first_crossing_support_found"

        envelope = self.canonical()
        envelope["intent"] = "CHANGED"
        _remove_path(envelope, allowance_path)
        _set_path(envelope, support_path, False)
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        _remove_path(envelope, event_path)
        _remove_path(envelope, allowance_path)
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        _set_path(envelope, non_claim_path, True)
        _remove_path(envelope, allowance_path)
        self.assert_blocked(envelope, issue_path=non_claim_path)

        envelope = self.canonical()
        _remove_path(envelope, allowance_path)
        _set_path(envelope, support_path, False)
        self.assert_requires(envelope, allowance_path)

        envelope = self.canonical()
        _set_path(envelope, support_path, False)
        self.assert_not_recorded(envelope)
        self.assertEqual(self.resolve(self.canonical())["outcome"], resolver.OUTCOME_RECORDED)

    def test_deterministic_rerender_historical_lock_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)

        event = first["current_operation_event"]
        self.assertEqual(event["persistent_operation_id"], resolver.OPERATION_ID)
        self.assertTrue(event["same_identity_same_binding_is_deterministic_rerender"])
        self.assertFalse(event["resolver_call_count_is_event_count"])
        self.assertFalse(event["sibling_event_identity_allocated"])

        changed = self.canonical()
        changed_path = (
            "constitutional_event_key.operation_event."
            "fresh_creation_operation_request_id"
        )
        _set_path(changed, changed_path, "descendant_body_creation_operation_request_002")
        self.assert_blocked(changed, issue_path=changed_path)

        history = first["freshness_and_history"]
        historical = history["historical_operation"]
        self.assertEqual(historical["historical_operation_id"], resolver.OPERATION_ID)
        self.assertEqual(
            historical["result_sha256"],
            "8b66349ff6d75670d91f4e9b202d0a4210dfb8d47065258a1103600d8dd99871",
        )
        self.assertEqual(historical["outcome"], resolver.OUTCOME_RECORDED)
        self.assertEqual(historical["first_crossing_result"], resolver.RESULT_SUPPORTED)
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_occurrence",
            "result_replayed",
            "success_treated_as_fresh_permission",
        ):
            self.assertIs(historical[key], False, key)
        self.assertEqual(
            first["current_boundary_result_binding"]["result_reference"],
            resolver.CURRENT_BOUNDARY_RESULT_REFERENCE,
        )
        self.assertEqual(
            first["current_boundary_result_binding"]["result_sha256"],
            resolver.CURRENT_BOUNDARY_RESULT_SHA256,
        )

        inspected_functions = (
            resolver.build_declared_first_crossing_operation_v0_min_v3_request,
            resolver.resolve_first_crossing_operation_v0_min_v3,
            resolver._control_review,
            resolver._validate_exact_mapping,
            resolver._ordinary_review,
            resolver._build_result,
            resolver._operation_object,
            resolver._operation_material,
            resolver._body_material,
            resolver._derive_pair_support,
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
            "resolve_first_crossing_boundary_v0_min_v2",
            "resolve_first_crossing_operation_v0_min_v2",
            "resolve_relation_boundary",
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
            pure_request = resolver.build_declared_first_crossing_operation_v0_min_v3_request()
            self.assertEqual(self.resolve(pure_request), first)


if __name__ == "__main__":
    unittest.main()
