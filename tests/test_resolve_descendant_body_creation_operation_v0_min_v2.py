"""Adversarial tests for the current-line descendant-body-creation operation V2."""

from __future__ import annotations

import builtins
import copy
import hashlib
import os
import subprocess
import sys
import time
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_creation_operation_request_v0_min as request_resolver
import resolve_descendant_body_creation_operation_v0_min_v2 as resolver


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


class DescendantBodyCreationOperationV2Tests(unittest.TestCase):
    maxDiff = None

    def canonical(self, support=True) -> dict:
        return resolver.build_declared_descendant_body_creation_operation_v0_min_v2_request(
            descendant_body_creation_support_evidence_present=support
        )

    def resolve(self, envelope):
        return resolver.resolve_descendant_body_creation_operation_v0_min_v2(envelope)

    def assert_blocked(self, envelope, code: str | None = None) -> dict:
        result = self.resolve(envelope)
        self.assertEqual(resolver.OUTCOME_BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        if code is not None:
            self.assertEqual(code, result["block"]["code"])
        self.assertFalse(
            any(
                result["descendant_body_creation_operation"][field]
                for field in resolver.POSITIVE_OPERATION_FIELDS
            )
        )
        self.assertEqual({}, result["descendant_body_creation_material"])
        return result

    def test_manifest_is_exact_complete_disjoint_and_non_inheriting(self) -> None:
        envelope = self.canonical()
        self.assertEqual(
            {
                "intent",
                "operation_question",
                "constitutional_event_key",
                "ordinary_operation_basis",
                "required_non_claims",
            },
            set(envelope),
        )
        self.assertEqual(3, len(resolver.CONTROL_PATHS))
        self.assertEqual(179, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        self.assertEqual(1, len(resolver.ORDINARY_OPERATION_BASIS_PATHS))
        self.assertEqual(65, len(resolver.REQUIRED_NON_CLAIM_PATHS))
        self.assertEqual(248, len(resolver.ALL_REQUIRED_PATHS))
        self.assertEqual(65, len(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS))
        self.assertEqual(
            {
                "ordinary_operation_basis."
                "descendant_body_creation_support_evidence_present"
            },
            set(resolver.ORDINARY_OPERATION_BASIS_PATHS),
        )

        event_list = resolver._leaf_paths(
            resolver.EXPECTED_CONSTITUTIONAL_EVENT_KEY,
            "constitutional_event_key",
        )
        non_claim_list = tuple(
            f"required_non_claims.operation_local.{key}"
            for key in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS
        )
        self.assertEqual(len(event_list), len(set(event_list)))
        self.assertEqual(len(non_claim_list), len(set(non_claim_list)))
        self.assertEqual(set(event_list), set(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        self.assertEqual(set(non_claim_list), set(resolver.REQUIRED_NON_CLAIM_PATHS))

        class_names = tuple(resolver.CLASS_PATHS)
        for index, left_name in enumerate(class_names):
            for right_name in class_names[index + 1 :]:
                with self.subTest(left=left_name, right=right_name):
                    self.assertTrue(
                        resolver.CLASS_PATHS[left_name].isdisjoint(
                            resolver.CLASS_PATHS[right_name]
                        )
                    )
        memberships = {
            path: sum(path in paths for paths in resolver.CLASS_PATHS.values())
            for path in resolver.ALL_REQUIRED_PATHS
        }
        self.assertEqual({1}, set(memberships.values()))
        self.assertEqual(
            resolver.ALL_REQUIRED_PATHS,
            frozenset().union(*resolver.CLASS_PATHS.values()),
        )
        for container_path in (
            "constitutional_event_key",
            "constitutional_event_key.operation_request_result",
            "required_non_claims",
            "required_non_claims.operation_local",
            "ordinary_operation_basis",
        ):
            self.assertNotIn(container_path, resolver.ALL_REQUIRED_PATHS)
        self.assertEqual(
            (
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
                resolver.OUTCOME_NOT_CREATED,
                resolver.OUTCOME_CREATED,
            ),
            resolver.OUTCOME_FAMILY,
        )
        self.assertFalse(hasattr(resolver, "OUTCOME_NOT_RECORDED"))

    def test_canonical_created_occurrence_and_exact_material(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        result = self.resolve(envelope)
        self.assertEqual(before, envelope)
        self.assertEqual(resolver.OUTCOME_CREATED, result["outcome"])
        self.assertFalse(result["block"]["blocked"])

        operation = result["descendant_body_creation_operation"]
        self.assertEqual(resolver.RESULT_SUPPORTED, operation["descendant_body_creation_result"])
        self.assertEqual(13, len(resolver.POSITIVE_OPERATION_FIELDS))
        self.assertEqual(
            set(resolver.POSITIVE_OPERATION_FIELDS),
            {key for key, value in operation.items() if value is True},
        )
        for field in resolver.POSITIVE_OPERATION_FIELDS:
            self.assertIs(True, operation[field], field)
        for invented in (
            "operation_review_allowed",
            "operation_occurrence_established",
            "operation_result_created",
        ):
            self.assertNotIn(invented, operation)

        expected_a = {
            "descendant_body_id": "descendant_body_a_001",
            "candidate_standing_source_id": "descendant_body_basis_candidate_a_001",
            "candidate_role": "CANDIDATE_A",
            "candidate_standing_label": "CANDIDATE_A_STANDING",
            "candidate_basis_id": (
                "descendant_body_basis_candidate_a_001__motion_side_admissible_"
                "variation_basis"
            ),
            "candidate_basis_label": (
                "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
            ),
            "candidate_basis_scope": "Motion-side admissible variation",
            "candidate_standing_created": True,
            "candidate_standing_is_descendant_body": False,
            "descendant_body_creation_supported": True,
            "descendant_body_creation_authorized": True,
            "descendant_body_created": True,
            "standing_descendant_created": False,
            "descendant_body_is_standing_descendant": False,
            "crossing_authorized": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
        }
        expected_b = {
            "descendant_body_id": "descendant_body_b_001",
            "candidate_standing_source_id": "descendant_body_basis_candidate_b_001",
            "candidate_role": "CANDIDATE_B",
            "candidate_standing_label": "CANDIDATE_B_STANDING",
            "candidate_basis_id": (
                "descendant_body_basis_candidate_b_001__regulation_side_"
                "admissibility_bounds_basis"
            ),
            "candidate_basis_label": (
                "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
            ),
            "candidate_basis_scope": "Regulation-side admissibility bounds",
            "candidate_standing_created": True,
            "candidate_standing_is_descendant_body": False,
            "descendant_body_creation_supported": True,
            "descendant_body_creation_authorized": True,
            "descendant_body_created": True,
            "standing_descendant_created": False,
            "descendant_body_is_standing_descendant": False,
            "crossing_authorized": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
        }
        expected_pair = {
            "both_descendant_body_creations_supported": True,
            "both_descendant_body_creations_authorized": True,
            "both_descendant_bodies_created": True,
            "descendant_body_a_created": True,
            "descendant_body_b_created": True,
            "descendant_body_created": True,
            "descendant_bodies_remain_sibling": True,
            "descendant_body_non_hierarchy_preserved": True,
            "candidate_standing_non_hierarchy_preserved": True,
            "candidate_basis_non_hierarchy_preserved": True,
            "regulation_not_sovereign_over_motion": True,
            "motion_does_not_erase_regulation": True,
            "standing_descendant_created": False,
            "descendant_standing_check_performed": False,
            "crossing_authorized": False,
            "first_crossing_authorized": False,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "relation_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
        }
        material = result["descendant_body_creation_material"]
        self.assertEqual(expected_a, material["descendant_body_a"])
        self.assertEqual(expected_b, material["descendant_body_b"])
        self.assertEqual(expected_pair, material["pair_result"])
        self.assertNotEqual(material["descendant_body_a"], material["descendant_body_b"])

        occurrence_facts = (
            result["outcome"] == resolver.OUTCOME_CREATED,
            operation["descendant_body_creation_operation_recorded"],
            operation["descendant_body_creation_evaluation_performed"],
            operation["descendant_body_creation_result_recorded"],
            operation["descendant_body_creation_performed"],
        )
        self.assertEqual((True, True, True, True, True), occurrence_facts)
        self.assertTrue(material["descendant_body_a"]["candidate_standing_created"])
        self.assertTrue(material["descendant_body_b"]["candidate_standing_created"])
        self.assertEqual(
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
            result["selected_candidate_source"]["selected_surface_semantic_owner"],
        )

        self.assertEqual(
            set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS),
            set(result["operation_local_non_claims"]),
        )
        self.assertTrue(
            all(value is False for value in result["operation_local_non_claims"].values())
        )
        stop = result["downstream_stopping_point"]
        self.assertEqual(resolver.ADMISSIBLE_FUTURE_ROUTE, stop["admissible_future_route"])
        self.assertEqual("FIRST_CROSSING_BOUNDARY", stop["next_separately_bounded_rank"])
        for key, value in stop.items():
            if isinstance(value, bool):
                self.assertIs(False, value, key)

    def test_ordinary_support_exact_boolean_law(self) -> None:
        cases = (
            (False, "false"),
            (None, "none"),
            ("true", "string"),
            (1, "integer"),
            ({}, "mapping"),
            ([], "list"),
        )
        for value, label in cases:
            with self.subTest(label=label):
                result = self.resolve(self.canonical(value))
                self.assertEqual(resolver.OUTCOME_NOT_CREATED, result["outcome"])
                operation = result["descendant_body_creation_operation"]
                self.assertEqual(
                    resolver.RESULT_NOT_SUPPORTED,
                    operation["descendant_body_creation_result"],
                )
                self.assertTrue(
                    all(operation[field] is False for field in resolver.POSITIVE_OPERATION_FIELDS)
                )
                self.assertEqual({}, result["descendant_body_creation_material"])
                self.assertFalse(
                    result["ordinary_operation_basis_review"][
                        "not_created_creates_retry_or_successor_permission"
                    ]
                )

        envelope = self.canonical()
        del envelope["ordinary_operation_basis"][
            "descendant_body_creation_support_evidence_present"
        ]
        self.assertEqual(resolver.OUTCOME_NOT_CREATED, self.resolve(envelope)["outcome"])
        self.assertEqual(resolver.OUTCOME_CREATED, self.resolve(self.canonical(True))["outcome"])

    def test_every_event_leaf_is_required_and_representative_mutations_block(self) -> None:
        self.assertEqual(179, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(absent=path):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

        representative_paths = (
            "constitutional_event_key.operation_request_result."
            "descendant_body_creation_operation_request.operation_request_id",
            "constitutional_event_key.operation_request_result.result_reference",
            "constitutional_event_key.operation_request_result.result_sha256",
            "constitutional_event_key.operation_request_result.outcome",
            "constitutional_event_key.operation_request_result.passed_check_count",
            "constitutional_event_key.operation_request_result.failed_check_count",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "operation.operation_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_request.request_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_request_admission.request_admission_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "actual_consumption.actual_consumption_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "actual_consumption.basis_consumed",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "actual_consumption.basis_exhausted",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.result_reference",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.result_sha256",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.outcome",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.boundary_result",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.review_terminal",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.review_exhausted",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "operation_contract.operation_contract_reference",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "operation_contract.operation_contract_sha256",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.candidate_a_record_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.candidate_a_basis_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.candidate_b_record_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.candidate_b_basis_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.complete_pair_preserved",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "selected_surface.selected_surface_semantic_owner",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "source_applicability.source_applicability_id",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "source_applicability.source_applicability_outcome",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "source_applicability.source_route",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "declared_use.target_route",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "freshness.historical_operation_result_is_current_permission",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "historical_operation.result_sha256",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "historical_operation.outcome",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "historical_operation.operation_result",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "non_claim_attribution.source_family.owner",
        )
        for path in representative_paths:
            with self.subTest(mutated=path):
                envelope = self.canonical()
                current = envelope
                for part in path.split("."):
                    current = current[part]
                replacement = (
                    not current
                    if type(current) is bool
                    else current + 1
                    if type(current) is int
                    else "CHANGED"
                )
                _set_path(envelope, path, replacement)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

    def test_allowance_restraint_unsupported_input_and_precedence(self) -> None:
        allowance_paths = (
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.result_reference",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.result_sha256",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.outcome",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.boundary_result",
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_boundary.blocked",
        )
        observed = set()
        for path in allowance_paths:
            with self.subTest(path=path):
                envelope = self.canonical()
                if path.endswith("result_reference"):
                    _remove_path(envelope, path)
                elif path.endswith("blocked"):
                    _set_path(envelope, path, True)
                else:
                    _set_path(envelope, path, "CHANGED")
                result = self.assert_blocked(envelope)
                observed.add(result["outcome"])
        self.assertEqual({resolver.OUTCOME_BLOCKED}, observed)
        self.assertIn(resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE, resolver.OUTCOME_FAMILY)
        self.assertNotIn(resolver.OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE, observed)

        unsupported = (
            ("root", lambda e: e.__setitem__("outcome", "CALLER_SELECTED")),
            (
                "event",
                lambda e: e["constitutional_event_key"].__setitem__("extra", False),
            ),
            (
                "nested_event",
                lambda e: e["constitutional_event_key"]["operation_request_result"]
                .__setitem__("extra", False),
            ),
            (
                "ordinary",
                lambda e: e["ordinary_operation_basis"].__setitem__("extra", False),
            ),
            (
                "non_claim_owner",
                lambda e: e["required_non_claims"].__setitem__("extra", {}),
            ),
            (
                "non_claim",
                lambda e: e["required_non_claims"]["operation_local"]
                .__setitem__("extra", False),
            ),
        )
        for label, mutation in unsupported:
            with self.subTest(unsupported=label):
                envelope = self.canonical()
                mutation(envelope)
                self.assert_blocked(envelope)

        for key in (
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "artifact",
            "occurrence",
            "successor",
            "execution_selector",
            "terminal_selector",
        ):
            with self.subTest(caller_selected=key):
                envelope = self.canonical()
                envelope[key] = False
                self.assert_blocked(envelope, "UNSUPPORTED_INPUT")

        precedence_cases = (
            ("event", lambda e: _set_path(e, allowance_paths[2], "CHANGED")),
            (
                "non_claim",
                lambda e: e["required_non_claims"]["operation_local"]
                .__setitem__("standing_descendant_created", True),
            ),
            ("control", lambda e: e.__setitem__("intent", "CHANGED")),
        )
        for label, mutation in precedence_cases:
            with self.subTest(precedence=label):
                envelope = self.canonical()
                del envelope["ordinary_operation_basis"][
                    "descendant_body_creation_support_evidence_present"
                ]
                mutation(envelope)
                self.assert_blocked(envelope)
        self.assertEqual(
            resolver.OUTCOME_NOT_CREATED,
            self.resolve(
                {
                    **self.canonical(),
                    "ordinary_operation_basis": {},
                }
            )["outcome"],
        )

    def test_all_operation_local_non_claim_defects_block(self) -> None:
        expected_keys = set(resolver.OPERATION_LOCAL_NON_CLAIM_KEYS)
        self.assertEqual(
            expected_keys,
            set(self.canonical()["required_non_claims"]["operation_local"]),
        )
        self.assertTrue(
            expected_keys.isdisjoint(resolver.POSITIVE_OPERATION_FIELDS)
        )
        self.assertNotIn("source_applicability_created", expected_keys)
        self.assertNotIn("automatic_successor_created", expected_keys)

        envelope = self.canonical()
        del envelope["required_non_claims"]["operation_local"]
        self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        envelope = self.canonical()
        envelope["required_non_claims"]["operation_local"] = []
        self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        envelope = self.canonical()
        envelope["required_non_claims"]["operation_local"]["extra"] = False
        self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        first_key = resolver.OPERATION_LOCAL_NON_CLAIM_KEYS[0]
        for value in (None, 0, "false", [], {}):
            with self.subTest(non_boolean=value):
                envelope = self.canonical()
                envelope["required_non_claims"]["operation_local"][first_key] = value
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        for key in resolver.OPERATION_LOCAL_NON_CLAIM_KEYS:
            with self.subTest(absent=key):
                envelope = self.canonical()
                del envelope["required_non_claims"]["operation_local"][key]
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(true=key):
                envelope = self.canonical()
                envelope["required_non_claims"]["operation_local"][key] = True
                result = self.assert_blocked(
                    envelope, "REQUIRED_NON_CLAIM_INVALID"
                )
                self.assertTrue(
                    all(
                        value is False
                        for value in result["operation_local_non_claims"].values()
                    )
                )

    def test_deterministic_rerender_history_separation_and_purity(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        first = self.resolve(envelope)
        second = self.resolve(copy.deepcopy(envelope))
        self.assertEqual(first, second)
        self.assertEqual(before, envelope)
        event = first["current_operation_event"]
        self.assertEqual(resolver.OPERATION_ID, event["persistent_operation_id"])
        self.assertEqual(resolver.OPERATION_REQUEST_ID, event["fresh_operation_request_id"])
        self.assertTrue(event["same_identity_same_binding_is_deterministic_rerender"])
        self.assertFalse(event["resolver_call_count_is_event_count"])

        sibling = self.canonical()
        _set_path(
            sibling,
            "constitutional_event_key.operation_request_result."
            "descendant_body_creation_operation_request.operation_request_id",
            "descendant_body_creation_operation_request_002",
        )
        self.assert_blocked(sibling)

        changed_binding = self.canonical()
        _set_path(
            changed_binding,
            "constitutional_event_key.operation_request_result.constitutional_event_binding."
            "current_request.request_id",
            "descendant_body_creation_boundary_request_002",
        )
        self.assert_blocked(changed_binding)

        historical = first["freshness_and_history"]
        self.assertEqual(
            "8a19e961d1a27ed0ce9898d545b3e2f790a3cd16ac1ebb09177dfd3b07bc7d15",
            historical["historical_operation_evidence_only"]["result_sha256"],
        )
        self.assertFalse(
            historical["freshness"]["historical_operation_result_is_current_permission"]
        )
        self.assertFalse(historical["freshness"]["historical_operation_occurrence_reused"])
        self.assertEqual(
            resolver.OUTCOME_NOT_CREATED,
            self.resolve(self.canonical(False))["outcome"],
        )

        with (
            patch.object(builtins, "open", side_effect=AssertionError("filesystem read")),
            patch.object(Path, "read_text", side_effect=AssertionError("filesystem read")),
            patch.object(Path, "write_text", side_effect=AssertionError("persistence")),
            patch.object(hashlib, "sha256", side_effect=AssertionError("runtime sha")),
            patch.object(os, "walk", side_effect=AssertionError("repository scan")),
            patch.object(subprocess, "run", side_effect=AssertionError("git/process")),
            patch.object(time, "time", side_effect=AssertionError("timestamp")),
            patch.object(
                request_resolver,
                "resolve_descendant_body_creation_operation_request_v0_min",
                side_effect=AssertionError("upstream resolver"),
            ),
        ):
            pure_result = self.resolve(copy.deepcopy(envelope))
        self.assertEqual(first, pure_result)
        self.assertNotIn("artifact_written", pure_result)
        self.assertNotIn("output_path", pure_result)


if __name__ == "__main__":
    unittest.main()

