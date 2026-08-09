"""Adversarial tests for the bounded descendant-body-creation operation request."""

from __future__ import annotations

import builtins
import copy
import inspect
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_descendant_body_creation_operation_request_v0_min as resolver


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


def _get_path(value: dict, path: str):
    current = value
    for part in path.split("."):
        current = current[part]
    return current


class DescendantBodyCreationOperationRequestTests(unittest.TestCase):
    maxDiff = None

    def canonical(self) -> dict:
        return resolver.build_descendant_body_creation_operation_request_v0_min_envelope()

    def resolve(self, envelope):
        return resolver.resolve_descendant_body_creation_operation_request_v0_min(
            envelope
        )

    def assert_blocked(self, envelope, expected_code: str | None = None) -> dict:
        result = self.resolve(envelope)
        self.assertEqual(resolver.OUTCOME_BLOCKED, result["outcome"])
        self.assertTrue(result["block"]["blocked"])
        self.assertIn(result["block"]["code"], resolver.BLOCK_CODES)
        if expected_code is not None:
            self.assertEqual(expected_code, result["block"]["code"])
        for check in result["descendant_body_creation_operation_request_checks"]:
            if check["failure_code"] is not None:
                self.assertIn(check["failure_code"], resolver.BLOCK_CODES)
        return result

    def test_manifest_is_complete_exact_and_pairwise_disjoint(self) -> None:
        self.assertEqual(
            {"$::mapping_cardinality", "intent", "request_question"},
            set(resolver.CONTROL_PATHS),
        )
        self.assertEqual(148, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        self.assertEqual(
            {
                f"ordinary_request_basis.{key}"
                for key in resolver.EXPECTED_ORDINARY_REQUEST_BASIS
            },
            set(resolver.ORDINARY_REQUEST_BASIS_PATHS),
        )
        self.assertEqual(11, len(resolver.ORDINARY_REQUEST_BASIS_PATHS))
        self.assertEqual(
            {"required_non_claims.operation_request_local"},
            set(resolver.REQUIRED_NON_CLAIM_OWNER_PATHS),
        )
        self.assertEqual(50, len(resolver.LOCAL_NON_CLAIM_KEYS))
        self.assertEqual(
            {"required_non_claims.operation_request_local"}
            | {
                f"required_non_claims.operation_request_local.{key}"
                for key in resolver.LOCAL_NON_CLAIM_KEYS
            },
            set(resolver.REQUIRED_NON_CLAIM_PATHS),
        )
        self.assertEqual(
            {
                "intent",
                "request_question",
                "constitutional_event_key",
                "ordinary_request_basis",
                "required_non_claims",
            },
            set(resolver.EXECUTABLE_ROOT_KEYS),
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
        self.assertEqual({1}, set(memberships.values()))
        self.assertEqual(
            (
                resolver.OUTCOME_BLOCKED,
                resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                resolver.OUTCOME_NOT_RECORDED,
                resolver.OUTCOME_RECORDED,
            ),
            resolver.OUTCOMES,
        )

    def test_canonical_envelope_records_only_the_fresh_request(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        result = self.resolve(envelope)

        self.assertEqual(before, envelope)
        self.assertEqual(resolver.OUTCOME_RECORDED, result["outcome"])
        self.assertFalse(result["block"]["blocked"])
        request = result["descendant_body_creation_operation_request"]
        for field in resolver.POSITIVE_REQUEST_FIELDS:
            with self.subTest(field=field):
                self.assertIs(True, request[field])
        self.assertEqual(resolver.OPERATION_REQUEST_ID, request["operation_request_id"])
        self.assertEqual(
            resolver.OPERATION_ID,
            result["persistent_operation_target"]["operation_id"],
        )
        self.assertNotIn("descendant_body_creation_operation_002", repr(result))

        boundary = result["current_precursor_boundary"]
        self.assertEqual(
            resolver.CURRENT_BOUNDARY_RESULT_REFERENCE, boundary["result_reference"]
        )
        self.assertEqual(
            resolver.CURRENT_BOUNDARY_RESULT_SHA256, boundary["result_sha256"]
        )
        self.assertEqual(
            "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
            boundary["boundary_result"],
        )
        contract = result["operation_contract"]
        self.assertEqual(
            resolver.OPERATION_CONTRACT_REFERENCE,
            contract["operation_contract_reference"],
        )
        self.assertEqual(
            resolver.OPERATION_CONTRACT_SHA256,
            contract["operation_contract_sha256"],
        )
        selected = result["selected_source_complete_pair"]
        self.assertTrue(selected["complete_pair_preserved"])
        self.assertTrue(selected["candidate_records_remain_sibling"])
        self.assertEqual(
            "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
            selected["selected_surface_semantic_owner"],
        )
        self.assertEqual(
            resolver.SOURCE_DECLARED_MATTER_USE,
            result["source_applicability"]["source_declared_matter_use"],
        )
        self.assertEqual(
            resolver.TARGET_ROUTE, result["declared_use"]["target_route"]
        )
        freshness = result["historical_and_freshness_posture"]["freshness"]
        self.assertTrue(freshness["fresh_operation_request_identity_declared"])
        self.assertFalse(freshness["historical_operation_result_is_current_permission"])
        self.assertFalse(freshness["historical_operation_occurrence_reused"])

        self.assertEqual(set(resolver.LOCAL_NON_CLAIM_KEYS), set(result["non_claims"]))
        self.assertTrue(all(value is False for value in result["non_claims"].values()))
        for field in (
            "operation_request_admitted",
            "operation_authorized",
            "operation_performed",
            "operation_occurrence_established",
            "operation_result_created",
            "invocation_authorized",
            "execution_performed",
            "descendant_body_created",
            "standing_created",
            "presence_established",
            "authority_created",
            "runtime_created",
            "automatic_successor_created",
        ):
            self.assertIs(False, result["non_claims"][field], field)
        self.assertEqual(
            resolver.LATER_OPEN_RANK,
            result["what_remains_open"]["only_later_rank"],
        )
        self.assertFalse(result["what_remains_open"]["later_rank_invoked"])

    def test_exact_negative_intent_does_not_record_or_create_retry(self) -> None:
        envelope = self.canonical()
        envelope["intent"] = resolver.INTENT_DO_NOT_RECORD
        result = self.resolve(envelope)
        self.assertEqual(resolver.OUTCOME_NOT_RECORDED, result["outcome"])
        self.assertFalse(
            result["descendant_body_creation_operation_request"][
                "descendant_body_creation_operation_request_recorded"
            ]
        )
        for field in (
            "operation_request_reused",
            "request_reuse_permission_created",
            "repeat_permission_created",
            "continuation_permission_created",
            "follow_on_permission_created",
            "automatic_successor_created",
        ):
            self.assertIs(False, result["non_claims"][field], field)

    def test_all_eleven_ordinary_fields_distinguish_absence_and_invalidity(self) -> None:
        expected = resolver.EXPECTED_ORDINARY_REQUEST_BASIS
        self.assertEqual(11, len(expected))
        for key, canonical_value in expected.items():
            path = f"ordinary_request_basis.{key}"
            with self.subTest(key=key, posture="absent"):
                envelope = self.canonical()
                _remove_path(envelope, path)
                result = self.resolve(envelope)
                self.assertEqual(
                    resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS, result["outcome"]
                )
                self.assertEqual([path], result["ordinary_request_basis_review"]["missing_paths"])
                self.assertEqual(
                    resolver.REQUIREMENT_CODE_ORDINARY_ABSENT,
                    result["block"]["requirement_code"],
                )

            invalid_values = (
                (False, 1) if canonical_value is True else (f"{canonical_value}_WRONG", False)
            )
            for invalid_value in invalid_values:
                with self.subTest(key=key, posture="invalid", value=invalid_value):
                    envelope = self.canonical()
                    _set_path(envelope, path, invalid_value)
                    self.assert_blocked(
                        envelope, "ORDINARY_REQUEST_BASIS_INVALID"
                    )

    def test_every_event_leaf_is_required_and_representative_mutations_block(self) -> None:
        self.assertEqual(148, len(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS))
        for path in sorted(resolver.CONSTITUTIONAL_EVENT_KEY_PATHS):
            with self.subTest(path=path, posture="removed"):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

        mutations = {
            "constitutional_event_key.operation_request.operation_request_id": (
                "descendant_body_creation_operation_request_002"
            ),
            "constitutional_event_key.operation.operation_id": (
                "descendant_body_creation_operation_002"
            ),
            "constitutional_event_key.current_request.request_id": "historical_request",
            "constitutional_event_key.current_request_admission.request_admission_id": (
                "substituted_admission"
            ),
            "constitutional_event_key.actual_consumption.actual_consumption_id": (
                "substituted_consumption"
            ),
            "constitutional_event_key.actual_consumption.basis_exhausted": False,
            "constitutional_event_key.current_boundary.result_reference": (
                "artifacts/historical_result.json"
            ),
            "constitutional_event_key.current_boundary.result_sha256": "0" * 64,
            "constitutional_event_key.current_boundary.outcome": "BLOCKED",
            "constitutional_event_key.current_boundary.boundary_result": "SUPPORTED",
            "constitutional_event_key.operation_contract.operation_contract_reference": (
                "spec/SUBSTITUTED.md"
            ),
            "constitutional_event_key.operation_contract.operation_contract_sha256": (
                "1" * 64
            ),
            "constitutional_event_key.selected_surface.candidate_a_record_id": "candidate_a_002",
            "constitutional_event_key.selected_surface.candidate_a_basis_id": "basis_a_002",
            "constitutional_event_key.selected_surface.candidate_b_record_id": "candidate_b_002",
            "constitutional_event_key.selected_surface.candidate_b_basis_id": "basis_b_002",
            "constitutional_event_key.selected_surface.complete_pair_preserved": False,
            "constitutional_event_key.selected_surface.selected_surface_semantic_owner": (
                "DESCENDANT_BODY_CREATION_OPERATION_REQUEST"
            ),
            "constitutional_event_key.source_applicability.source_applicability_id": (
                "source_applicability_002"
            ),
            "constitutional_event_key.source_applicability.source_route": "WIDENED_ROUTE",
            "constitutional_event_key.declared_use.target_route": "WIDENED_ROUTE",
            "constitutional_event_key.freshness.historical_operation_result_replayed": True,
            "constitutional_event_key.historical_operation.result_sha256": "2" * 64,
            "constitutional_event_key.historical_operation.operation_result": "CURRENT_PERMISSION",
            "constitutional_event_key.non_claim_attribution.operation_request_local.owner": (
                "DESCENDANT_BODY_CREATION_OPERATION"
            ),
        }
        for path, replacement in mutations.items():
            with self.subTest(path=path, posture="mutated"):
                envelope = self.canonical()
                _set_path(envelope, path, replacement)
                self.assert_blocked(
                    envelope, "CONSTITUTIONAL_EVENT_KEY_INVALID"
                )

    def test_local_non_claim_map_is_exact_false_and_path_roles_do_not_collapse(self) -> None:
        expected_keys = set(resolver.LOCAL_NON_CLAIM_KEYS)
        self.assertEqual(50, len(expected_keys))
        self.assertEqual(
            expected_keys,
            set(
                self.canonical()["required_non_claims"]["operation_request_local"]
            ),
        )

        envelope = self.canonical()
        del envelope["required_non_claims"]["operation_request_local"]
        self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        envelope = self.canonical()
        envelope["required_non_claims"]["operation_request_local"] = []
        self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        for key in sorted(expected_keys):
            path = f"required_non_claims.operation_request_local.{key}"
            with self.subTest(key=key, posture="missing"):
                envelope = self.canonical()
                _remove_path(envelope, path)
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")
            with self.subTest(key=key, posture="true"):
                envelope = self.canonical()
                _set_path(envelope, path, True)
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        for replacement in (0, "false", None):
            with self.subTest(posture="non_boolean", value=replacement):
                envelope = self.canonical()
                _set_path(
                    envelope,
                    "required_non_claims.operation_request_local.operation_performed",
                    replacement,
                )
                self.assert_blocked(envelope, "REQUIRED_NON_CLAIM_INVALID")

        event_path = (
            "constitutional_event_key.freshness."
            "historical_operation_result_replayed"
        )
        local_path = (
            "required_non_claims.operation_request_local."
            "historical_operation_result_replayed"
        )
        self.assertIn(event_path, resolver.CONSTITUTIONAL_EVENT_KEY_PATHS)
        self.assertIn(local_path, resolver.REQUIRED_NON_CLAIM_PATHS)
        self.assertNotEqual(event_path, local_path)
        self.assertTrue(
            resolver.CONSTITUTIONAL_EVENT_KEY_PATHS.isdisjoint(
                resolver.REQUIRED_NON_CLAIM_PATHS
            )
        )
        for path in (event_path, local_path):
            with self.subTest(path=path, posture="independent_contradiction"):
                envelope = self.canonical()
                _set_path(envelope, path, True)
                self.assert_blocked(envelope)

    def test_unsupported_inputs_and_terminal_precedence_are_exact(self) -> None:
        for key in (
            "outcome",
            "result",
            "checks",
            "block",
            "summary",
            "metadata",
            "receipt",
            "invocation",
            "execution",
            "operation_occurrence",
        ):
            with self.subTest(location="root", key=key):
                envelope = self.canonical()
                envelope[key] = True
                self.assert_blocked(envelope, "UNSUPPORTED_INPUT")

        nested_extras = (
            ("constitutional_event_key", "unsupported_section"),
            ("constitutional_event_key.operation", "unsupported_leaf"),
            ("ordinary_request_basis", "unsupported_basis"),
            ("required_non_claims", "source_family"),
            ("required_non_claims.operation_request_local", "unsupported_non_claim"),
        )
        for parent, key in nested_extras:
            with self.subTest(location=parent, key=key):
                envelope = self.canonical()
                _get_path(envelope, parent)[key] = False
                self.assert_blocked(envelope)

        self.assert_blocked(None, "REQUEST_NOT_MAPPING")
        for missing_control in ("intent", "request_question"):
            with self.subTest(missing_control=missing_control):
                envelope = self.canonical()
                del envelope[missing_control]
                self.assert_blocked(envelope, "CONTROL_INVALID")

        blocking_plus_missing = self.canonical()
        del blocking_plus_missing["constitutional_event_key"]["operation"]["operation_id"]
        del blocking_plus_missing["ordinary_request_basis"]["source_outcome"]
        self.assertEqual(
            resolver.OUTCOME_BLOCKED, self.resolve(blocking_plus_missing)["outcome"]
        )

        non_claim_plus_missing = self.canonical()
        non_claim_plus_missing["required_non_claims"]["operation_request_local"][
            "operation_performed"
        ] = True
        del non_claim_plus_missing["ordinary_request_basis"]["source_outcome"]
        self.assertEqual(
            resolver.OUTCOME_BLOCKED, self.resolve(non_claim_plus_missing)["outcome"]
        )

        control_plus_missing = self.canonical()
        control_plus_missing["intent"] = "UNSUPPORTED"
        del control_plus_missing["ordinary_request_basis"]["source_outcome"]
        self.assertEqual(
            resolver.OUTCOME_BLOCKED, self.resolve(control_plus_missing)["outcome"]
        )

        negative_missing = self.canonical()
        negative_missing["intent"] = resolver.INTENT_DO_NOT_RECORD
        del negative_missing["ordinary_request_basis"]["source_outcome"]
        self.assertEqual(
            resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            self.resolve(negative_missing)["outcome"],
        )

    def test_same_event_rerender_and_historical_current_lock(self) -> None:
        envelope = self.canonical()
        first = self.resolve(envelope)
        second = self.resolve(copy.deepcopy(envelope))
        self.assertEqual(first, second)
        self.assertNotIn("event_count", first)
        self.assertFalse(first["non_claims"]["resolver_call_count_treated_as_event_count"])

        changed_binding = self.canonical()
        changed_binding["constitutional_event_key"]["current_boundary"][
            "result_sha256"
        ] = "0" * 64
        self.assert_blocked(changed_binding, "CONSTITUTIONAL_EVENT_KEY_INVALID")

        sibling = self.canonical()
        sibling["constitutional_event_key"]["operation_request"][
            "operation_request_id"
        ] = "descendant_body_creation_operation_request_002"
        self.assert_blocked(sibling, "CONSTITUTIONAL_EVENT_KEY_INVALID")

        historical_reference = self.canonical()["constitutional_event_key"][
            "historical_operation"
        ]["result_reference"]
        historical_substitution = self.canonical()
        historical_substitution["constitutional_event_key"]["current_boundary"][
            "result_reference"
        ] = historical_reference
        self.assert_blocked(
            historical_substitution, "CONSTITUTIONAL_EVENT_KEY_INVALID"
        )

        freshness = first["historical_and_freshness_posture"]["freshness"]
        self.assertFalse(freshness["historical_operation_result_is_current_permission"])
        self.assertFalse(freshness["historical_operation_result_is_current_request"])
        self.assertFalse(freshness["historical_operation_result_is_current_occurrence"])
        self.assertFalse(freshness["historical_operation_occurrence_reused"])
        self.assertEqual(
            resolver.OPERATION_ID,
            first["historical_and_freshness_posture"]
            ["historical_operation_evidence_only"]["historical_operation_id"],
        )

    def test_resolver_is_pure_deterministic_and_has_no_external_runtime(self) -> None:
        envelope = self.canonical()
        before = copy.deepcopy(envelope)
        with patch.object(builtins, "open", side_effect=AssertionError("filesystem access")):
            first = self.resolve(envelope)
            second = self.resolve(envelope)
        self.assertEqual(before, envelope)
        self.assertEqual(first, second)

        source = inspect.getsource(resolver)
        for forbidden_import in (
            "import hashlib",
            "import os",
            "import pathlib",
            "import subprocess",
            "import time",
            "import datetime",
            "import importlib",
        ):
            with self.subTest(forbidden_import=forbidden_import):
                self.assertNotIn(forbidden_import, source)
        for forbidden_call in (
            "resolve_descendant_body_creation_boundary_v0_min_v3(",
            "resolve_descendant_body_creation_operation_v0_min(",
            "subprocess.",
            "Path(",
            "open(",
        ):
            with self.subTest(forbidden_call=forbidden_call):
                self.assertNotIn(forbidden_call, source)


if __name__ == "__main__":
    unittest.main()
