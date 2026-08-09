"""Adversarial proof for the current-line FIRST_CROSSING_BOUNDARY V2 resolver."""

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

import resolve_first_crossing_boundary_v0_min_v2 as resolver


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


def _all_code_names(function: object) -> set[str]:
    pending = [function.__code__]  # type: ignore[attr-defined]
    names: set[str] = set()
    while pending:
        code = pending.pop()
        names.update(code.co_names)
        pending.extend(
            item for item in code.co_consts if isinstance(item, types.CodeType)
        )
    return names


class FirstCrossingBoundaryV0MinV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict[str, object]:
        return resolver.build_declared_first_crossing_boundary_v0_min_v2_request()

    def resolve(self, envelope: object) -> dict[str, object]:
        return resolver.resolve_first_crossing_boundary_v0_min_v2(envelope)

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
        self.assertFalse(block["requires_descendant_body_creation"])
        if issue_path is not None:
            self.assertEqual(block["issue_path"], issue_path)
        self.assert_no_positive_boundary_consequence(result)
        return result

    def assert_requires(
        self,
        envelope: object,
        missing_path: str,
    ) -> dict[str, object]:
        result = self.resolve(envelope)
        self.assertEqual(
            result["outcome"],
            resolver.OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
        )
        self.assertFalse(result["block"]["blocked"])
        self.assertTrue(result["block"]["requires_descendant_body_creation"])
        review = result["ordinary_descendant_body_creation_basis_review"]
        self.assertEqual(review["missing_paths"], [missing_path])
        self.assertFalse(
            review["requires_descendant_body_creation_creates_retry_permission"]
        )
        self.assertFalse(
            review["requires_descendant_body_creation_creates_successor_permission"]
        )
        self.assert_no_positive_boundary_consequence(result)
        return result

    def assert_no_positive_boundary_consequence(
        self, result: dict[str, object]
    ) -> None:
        boundary = result["first_crossing_boundary"]
        for field in resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS:
            self.assertIs(boundary[field], False)
        self.assertNotEqual(
            boundary["first_crossing_boundary_result"],
            resolver.BOUNDARY_RESULT_ALLOWED,
        )

    def test_manifest_identity_classification_and_outcome_lock(self) -> None:
        envelope = self.canonical()
        self.assertEqual(set(envelope), resolver.EXECUTABLE_ROOT_KEYS)
        self.assertEqual(len(envelope), 5)
        self.assertEqual(len(resolver.CONTROL_PATHS), 3)
        self.assertEqual(len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS), 102)
        self.assertEqual(
            len(resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS), 8
        )
        self.assertEqual(len(resolver.SOURCE_OPERATION_NON_CLAIM_PATHS), 10)
        self.assertEqual(len(resolver.TARGET_LOCAL_NON_CLAIM_PATHS), 66)
        self.assertEqual(len(resolver.REQUIRED_NON_CLAIM_PATHS), 76)
        self.assertEqual(len(resolver.ALL_REQUIRED_PATHS), 189)

        explicit_lists = (
            tuple(resolver.CONTROL_PATHS),
            tuple(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS),
            tuple(resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS),
            tuple(resolver.SOURCE_OPERATION_NON_CLAIM_PATHS),
            tuple(resolver.TARGET_LOCAL_NON_CLAIM_PATHS),
        )
        for paths in explicit_lists:
            self.assertEqual(len(paths), len(set(paths)))
        for index, paths in enumerate(explicit_lists):
            for other in explicit_lists[index + 1 :]:
                self.assertFalse(set(paths) & set(other))

        event_paths = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        self.assertEqual(set(event_paths), resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)
        self.assertEqual(len(event_paths), 102)
        expected_required = (
            resolver.CONTROL_PATHS
            | set(event_paths)
            | resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS
            | resolver.SOURCE_OPERATION_NON_CLAIM_PATHS
            | resolver.TARGET_LOCAL_NON_CLAIM_PATHS
        )
        self.assertEqual(expected_required, resolver.ALL_REQUIRED_PATHS)

        parent_paths: set[str] = set()
        for path in expected_required:
            parts = path.split(".")
            parent_paths.update(".".join(parts[:end]) for end in range(1, len(parts)))
        self.assertFalse(parent_paths & resolver.ALL_REQUIRED_PATHS)

        self.assertEqual(
            resolver.OUTCOME_FAMILY,
            (
                "FIRST_CROSSING_BOUNDARY_BLOCKED",
                "FIRST_CROSSING_BOUNDARY_REQUIRES_DESCENDANT_BODY_CREATION",
                "FIRST_CROSSING_BOUNDARY_ALLOWED",
            ),
        )
        self.assertNotIn("FIRST_CROSSING_BOUNDARY_NOT_RECORDED", resolver.OUTCOME_FAMILY)
        self.assertEqual(resolver.BOUNDARY_ID, "first_crossing_boundary_001")
        self.assertNotIn("first_crossing_boundary_002", repr(vars(resolver)))
        self.assertEqual(
            resolver.CURRENT_SOURCE_RESULT_SHA256,
            "4adc2e5b6557a29cb37fe682e4fef8af2832ed88625622e3ec5a986a93e27767",
        )
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS)
        )
        self.assertNotIn(
            "first_crossing_boundary_result",
            resolver.TARGET_LOCAL_NON_CLAIM_KEYS,
        )

    def test_canonical_allowed_pair_topology_and_downstream_restraint(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        result = self.resolve(envelope)
        self.assertEqual(envelope, before)
        self.assertEqual(result["outcome"], resolver.OUTCOME_ALLOWED)
        self.assertEqual(result["failed_check_count"], 0)

        boundary = result["first_crossing_boundary"]
        self.assertEqual(
            boundary["first_crossing_boundary_result"],
            resolver.BOUNDARY_RESULT_ALLOWED,
        )
        true_boolean_fields = {
            key for key, value in boundary.items() if type(value) is bool and value
        }
        self.assertEqual(
            true_boolean_fields,
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS),
        )
        for field in resolver.TARGET_LOCAL_NON_CLAIM_KEYS:
            self.assertIs(boundary[field], False)
        self.assertTrue(
            all(value is False for value in result["target_local_non_claims"].values())
        )
        self.assertTrue(
            all(
                value is False
                for value in result["source_operation_non_claims"].values()
            )
        )

        subject = result["descendant_body_subject"]
        self.assertEqual(
            subject["descendant_body_a"]["descendant_body_id"],
            "descendant_body_a_001",
        )
        self.assertEqual(
            subject["descendant_body_b"]["descendant_body_id"],
            "descendant_body_b_001",
        )
        self.assertEqual(
            subject["pair"]["descendant_body_pair_scope"],
            "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY",
        )
        self.assertTrue(subject["one_pair_preserved_boundary_condition"])
        self.assertTrue(subject["pair"]["complete_pair_preserved"])
        self.assertTrue(subject["pair"]["descendant_bodies_remain_sibling"])
        self.assertFalse(subject["bodies_merged"])
        self.assertFalse(subject["per_body_boundary_decisions_created"])
        self.assertFalse(subject["bodies_ranked"])
        self.assertFalse(subject["coupling_created"])
        self.assertNotIn("first_crossing_boundary_result", subject["descendant_body_a"])
        self.assertNotIn("first_crossing_boundary_result", subject["descendant_body_b"])

        source = result["source_binding"]["source"]
        self.assertEqual(
            source["selected_surface_semantic_owner"],
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        )
        self.assertTrue(source["source_custody_preserved"])
        self.assertTrue(source["source_lineage_preserved"])
        self.assertTrue(source["source_rank_preserved"])
        self.assertTrue(source["source_scope_preserved"])

        stop = result["downstream_stopping_point"]
        self.assertEqual(stop["next_separately_bounded_rank"], "FIRST_CROSSING_OPERATION")
        self.assertEqual(
            stop["admissible_future_route"],
            "FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY",
        )
        for key, value in stop.items():
            if type(value) is bool:
                self.assertIs(value, False, key)
        for forbidden in (
            "first_crossing_authorized",
            "crossing_authorized",
            "first_crossing_performed",
            "crossing_performed",
            "standing_descendant_created",
            "standing_created",
            "relation_created",
            "currentness_created",
            "authority_created",
            "presence_established",
            "identity_created",
            "coupling_created",
            "runtime_created",
        ):
            self.assertIs(boundary[forbidden], False)

    def test_all_ordinary_omissions_require_and_all_contradictions_block(self) -> None:
        for path in sorted(resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS):
            with self.subTest(posture="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_requires(envelope, path)

        for path in sorted(resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS):
            with self.subTest(posture="contradictory", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

        boolean_path = (
            "ordinary_descendant_body_creation_basis.descendant_body_created"
        )
        for malformed in ("true", 1, None):
            with self.subTest(posture="malformed", value=malformed):
                envelope = self.canonical()
                _set_path(envelope, boolean_path, malformed)
                self.assert_blocked(envelope, issue_path=boolean_path)

        envelope = self.canonical()
        envelope["ordinary_descendant_body_creation_basis"]["unsupported"] = True
        self.assert_blocked(
            envelope,
            issue_path="ordinary_descendant_body_creation_basis.unsupported",
        )
        envelope = self.canonical()
        envelope["ordinary_descendant_body_creation_basis"] = []
        self.assert_blocked(
            envelope,
            issue_path="ordinary_descendant_body_creation_basis",
        )

    def test_every_event_leaf_is_required_and_representative_bindings_are_exact(self) -> None:
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(posture="missing", path=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, issue_path=path)

        mutation_paths = (
            "constitutional_event_key.target.boundary_id",
            "constitutional_event_key.target.boundary_contract_sha256",
            "constitutional_event_key.current_creation_result.result_reference",
            "constitutional_event_key.current_creation_result.result_sha256",
            "constitutional_event_key.operation.operation_id",
            "constitutional_event_key.operation_event.fresh_operation_request_id",
            "constitutional_event_key.operation_event.operation_request_result_sha256",
            "constitutional_event_key.operation_contract.operation_contract_sha256",
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
            "constitutional_event_key.historical_first_crossing.result_sha256",
            "constitutional_event_key.historical_first_crossing.outcome",
            "constitutional_event_key.historical_first_crossing.boundary_result",
            "constitutional_event_key.non_claim_attribution.source_operation.owner",
            "constitutional_event_key.non_claim_attribution.source_family.owner",
            "constitutional_event_key.non_claim_attribution.target_local.owner",
        )
        self.assertTrue(set(mutation_paths) <= resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)
        for path in mutation_paths:
            with self.subTest(posture="changed", path=path):
                envelope = self.canonical()
                _set_path(envelope, path, _wrong_value(_get_path(envelope, path)))
                self.assert_blocked(envelope, issue_path=path)

    def test_source_and_target_non_claim_maps_are_closed_and_false(self) -> None:
        map_cases = (
            (
                "source_operation",
                resolver.SOURCE_OPERATION_NON_CLAIM_KEYS,
                resolver.SOURCE_OPERATION_NON_CLAIM_PATHS,
            ),
            (
                "target_local",
                resolver.TARGET_LOCAL_NON_CLAIM_KEYS,
                resolver.TARGET_LOCAL_NON_CLAIM_PATHS,
            ),
        )
        for map_name, keys, paths in map_cases:
            map_path = f"required_non_claims.{map_name}"
            self.assertEqual(
                paths,
                {f"{map_path}.{key}" for key in keys},
            )
            envelope = self.canonical()
            _remove_path(envelope, map_path)
            self.assert_blocked(envelope, issue_path=map_path)

            envelope = self.canonical()
            _set_path(envelope, map_path, [])
            self.assert_blocked(envelope, issue_path=map_path)

            envelope = self.canonical()
            envelope["required_non_claims"][map_name]["unsupported"] = False
            self.assert_blocked(envelope, issue_path=f"{map_path}.unsupported")

            representative_path = f"{map_path}.{keys[0]}"
            envelope = self.canonical()
            _set_path(envelope, representative_path, 0)
            self.assert_blocked(envelope, issue_path=representative_path)

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

        self.assertIn(
            "automatic_successor_created",
            resolver.SOURCE_OPERATION_NON_CLAIM_KEYS,
        )
        self.assertNotIn(
            "automatic_successor_created",
            resolver.TARGET_LOCAL_NON_CLAIM_KEYS,
        )
        self.assertEqual(
            set(resolver.EXPECTED_REQUIRED_NON_CLAIMS["target_local"]),
            set(resolver.TARGET_LOCAL_NON_CLAIM_KEYS),
        )
        self.assertFalse(
            set(resolver.POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
            & set(resolver.EXPECTED_REQUIRED_NON_CLAIMS["target_local"])
        )
        self.assertNotIn(
            "first_crossing_boundary_result",
            resolver.EXPECTED_REQUIRED_NON_CLAIMS["target_local"],
        )

    def test_unsupported_input_control_and_precedence(self) -> None:
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
        ordinary["ordinary_descendant_body_creation_basis"]["unsupported"] = True
        unsupported_cases.append(
            ("ordinary_descendant_body_creation_basis.unsupported", ordinary)
        )

        source_nc = self.canonical()
        source_nc["required_non_claims"]["source_operation"]["unsupported"] = False
        unsupported_cases.append(
            ("required_non_claims.source_operation.unsupported", source_nc)
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
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "crossing",
            "invocation",
            "execution",
            "artifact_existence_claim",
            "standing_claim",
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
        for control_path in ("intent", "boundary_question"):
            envelope = self.canonical()
            _set_path(envelope, control_path, "CHANGED")
            self.assert_blocked(envelope, issue_path=control_path)

        ordinary_path = sorted(
            resolver.ORDINARY_DESCENDANT_BODY_CREATION_BASIS_PATHS
        )[0]
        event_path = sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)[0]
        source_nc_path = sorted(resolver.SOURCE_OPERATION_NON_CLAIM_PATHS)[0]

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        _remove_path(envelope, event_path)
        self.assert_blocked(envelope, issue_path=event_path)

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        _set_path(envelope, source_nc_path, True)
        self.assert_blocked(envelope, issue_path=source_nc_path)

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        envelope["intent"] = "CHANGED"
        self.assert_blocked(envelope, issue_path="intent")

        envelope = self.canonical()
        _remove_path(envelope, ordinary_path)
        self.assert_requires(envelope, ordinary_path)
        self.assertEqual(self.resolve(self.canonical())["outcome"], resolver.OUTCOME_ALLOWED)

    def test_deterministic_rerender_historical_current_lock_and_purity(self) -> None:
        envelope = self.canonical()
        before = deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(envelope)
        self.assertEqual(first, second)
        self.assertEqual(envelope, before)
        event = first["current_boundary_event"]
        self.assertEqual(event["persistent_boundary_id"], "first_crossing_boundary_001")
        self.assertTrue(event["same_identity_same_binding_is_deterministic_rerender"])
        self.assertFalse(event["resolver_call_count_is_event_count"])
        self.assertFalse(event["sibling_event_identity_allocated"])

        changed = self.canonical()
        changed_path = "constitutional_event_key.operation_event.fresh_operation_request_id"
        _set_path(changed, changed_path, "descendant_body_creation_operation_request_002")
        self.assert_blocked(changed, issue_path=changed_path)

        history = first["freshness_and_history"]
        self.assertEqual(
            history["historical_first_crossing"]["result_sha256"],
            "cf9c7fe38465ea6d6e27ac7728004f5bf73851352f333c56284debf8b89d93f6",
        )
        self.assertEqual(
            history["historical_first_crossing"]["outcome"],
            resolver.OUTCOME_ALLOWED,
        )
        self.assertEqual(
            history["historical_first_crossing"]["boundary_result"],
            resolver.BOUNDARY_RESULT_ALLOWED,
        )
        for key in (
            "result_is_current_permission",
            "result_is_current_source",
            "result_is_current_event",
            "result_replayed",
            "success_treated_as_fresh_permission",
        ):
            self.assertIs(history["historical_first_crossing"][key], False)
        self.assertEqual(
            first["current_creation_result_binding"]["result_reference"],
            resolver.CURRENT_SOURCE_RESULT_REFERENCE,
        )
        self.assertEqual(
            first["current_creation_result_binding"]["result_sha256"],
            resolver.CURRENT_SOURCE_RESULT_SHA256,
        )

        forbidden_calls = {
            "resolve_descendant_body_creation_operation_v0_min_v2",
            "resolve_first_crossing_boundary_v0_min",
            "resolve_first_crossing_operation_v0_min",
        }
        self.assertFalse(
            forbidden_calls
            & _all_code_names(resolver.resolve_first_crossing_boundary_v0_min_v2)
        )
        self.assertFalse(
            forbidden_calls
            & _all_code_names(
                resolver.build_declared_first_crossing_boundary_v0_min_v2_request
            )
        )

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
            pure_request = resolver.build_declared_first_crossing_boundary_v0_min_v2_request()
            self.assertEqual(self.resolve(pure_request), first)


if __name__ == "__main__":
    unittest.main()
