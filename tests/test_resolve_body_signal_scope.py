"""Bounded tests for body-signal scope.

This suite exercises ``src/resolve_body_signal_scope.py`` as one post-acceptance
scope gate:

- one ``SIGNAL_ACCEPTED`` result
- one signal-scope request
- one outcome: ``SIGNAL_SCOPED`` or ``BLOCKED``

Scope bounds applicability only inside ``current_signal_recognition_standing``.
It is not presence, threshold, truth, permission, action, routing, workflow,
event bus behavior, body relevance medium implementation, signal use, or
continuation.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


import resolve_body_signal_scope as scope


EXPECTED_RESULT_KEYS = {
    "body_signal_scope_metadata",
    "selected_signal_acceptance_result",
    "selected_accepted_signal",
    "selected_signal_scope_request",
    "declared_scope",
    "signal_scope_checks",
    "outcome",
    "block",
    "scoped_signal",
    "body_signal_scope_basis",
    "body_signal_scope_summary",
    "non_claims",
}

REQUIRED_METADATA_KEYS = {
    "body_signal_scope_result_id",
    "body_signal_scope_result_type",
    "body_signal_scope_result_version",
    "generated_at",
    "resolver_module",
}

REQUIRED_FALSE_RESULT_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "truth_created",
    "presence_established",
    "threshold_met",
    "action_authorized",
    "follow_on_work_authorized",
    "workflow_created",
    "roadmap_created",
    "signal_router_created",
    "event_bus_created",
    "body_relevance_medium_created",
    "source_replaced",
    "derivative_upgraded_to_source",
    "receipt_turned_into_permission",
    "matter_widened",
    "applied_outside_declared_scope",
}

SCOPE_LIMIT_TRUE_FIELDS = {
    "scope_for_applicability_only": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
    "presence_not_yet_established": "SCOPE_ATTEMPTS_PRESENCE",
    "threshold_not_yet_met": "SCOPE_ATTEMPTS_THRESHOLD",
    "truth_not_created": "SCOPE_ATTEMPTS_TRUTH",
    "action_not_authorized": "SCOPE_ATTEMPTS_ACTION_AUTHORIZATION",
    "routing_not_created": "SCOPE_ATTEMPTS_SIGNAL_ROUTER",
    "workflow_not_created": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
    "body_relevance_medium_not_created": "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
    "follow_on_work_not_authorized": "SCOPE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION",
}

HIERARCHY_FALSE_FIELDS = {
    "scoped_signal_allowed_as_authority": "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY",
    "scoped_signal_allowed_as_permission": "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION",
    "scoped_signal_allowed_as_currentness": "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
    "scoped_signal_allowed_as_truth": "SCOPE_ATTEMPTS_TRUTH",
    "scoped_signal_allowed_as_presence": "SCOPE_ATTEMPTS_PRESENCE",
    "scoped_signal_allowed_as_threshold": "SCOPE_ATTEMPTS_THRESHOLD",
    "scoped_signal_allowed_as_action_trigger": "SCOPE_ATTEMPTS_ACTION_AUTHORIZATION",
    "scoped_signal_allowed_as_workflow": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
    "scoped_signal_allowed_as_route": "DECLARED_SCOPE_ATTEMPTS_ROUTING",
    "scoped_signal_allowed_as_body_relevance_medium": (
        "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
    ),
    "derivative_signal_allowed_as_source": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "operator_signal_allowed_as_source": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "reentry_signal_allowed_as_governing_basis": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = {
    "must_preserve_accepted_signal_identity": "ACCEPTED_SIGNAL_IDENTITY_MISMATCH",
    "must_preserve_recognized_source_identity": "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
    "must_preserve_signal_category": "SIGNAL_CATEGORY_MISMATCH",
    "must_preserve_accepted_matter": "ACCEPTED_MATTER_MISMATCH",
    "must_preserve_scope_boundary": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
    "must_preserve_signal_non_authority": "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY",
    "must_preserve_signal_non_permission": "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION",
    "must_preserve_signal_non_currentness": "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "DECLARED_SCOPE_WIDENS_MATTER",
    "must_prevent_under_mirroring": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_create_truth",
    "does_not_establish_presence",
    "does_not_meet_threshold",
    "does_not_authorize_action",
    "does_not_authorize_follow_on_work",
    "does_not_create_workflow",
    "does_not_create_roadmap",
    "does_not_create_signal_router",
    "does_not_create_event_bus",
    "does_not_create_body_relevance_medium",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_turn_receipt_into_permission",
    "does_not_widen_matter",
    "does_not_apply_outside_declared_scope",
)


def write_json(path: Path | str, value: Mapping[str, Any]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def read_json(path: Path | str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object at {path}")
    return value


def signal_acceptance_result(
    *,
    result_id: str = "body-pass-signal-acceptance-001",
    result_path: str = "artifacts/synthetic/body-pass-signal-acceptance-001.json",
    outcome: str = "SIGNAL_ACCEPTED",
    include_accepted_signal: bool = True,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "body_signal_acceptance_metadata": {
            "body_signal_acceptance_result_id": result_id,
            "body_signal_acceptance_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_ACCEPTANCE_RESULT"
            ),
            "body_signal_acceptance_result_version": "0.1.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_body_signal_acceptance",
        },
        "result_path": result_path,
        "selected_signal_recognition_result": {
            "signal_recognition_result_id": "body-pass-recognition-001",
            "signal_recognition_result_path": (
                "artifacts/synthetic/body-pass-recognition-001.json"
            ),
            "signal_recognition_result_version": "0.2.0",
            "signal_recognition_outcome": "SIGNAL_RECOGNIZED",
            "signal_recognition_resolver_module": "resolve_body_signal_recognition_v2",
            "selection_mode": "synthetic",
        },
        "declared_matter": {
            "matter_id": "current_signal_recognition_standing",
            "matter_family": "body_signal_acceptance_matter",
            "matter_kind": "recognized_body_signal_posture",
            "matter_purpose": (
                "Hold recognized body signal as current signal recognition standing "
                "posture for structured handling only."
            ),
            "matter_boundary": "structured_handling_only_for_current_signal_recognition_standing",
        },
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "SIGNAL_ACCEPTED"
        else {"block_code": "SYNTHETIC_BLOCK", "block_reason": "synthetic block"},
        "non_claims": {
            "authority_created": False,
            "permission_created": False,
            "currentness_created": False,
            "truth_created": False,
            "scope_assigned": False,
            "presence_established": False,
            "threshold_met": False,
            "action_authorized": False,
            "follow_on_work_authorized": False,
            "workflow_created": False,
            "roadmap_created": False,
            "signal_router_created": False,
            "event_bus_created": False,
            "body_relevance_medium_created": False,
            "source_replaced": False,
            "derivative_upgraded_to_source": False,
            "receipt_turned_into_permission": False,
        },
    }
    if include_accepted_signal:
        result["accepted_signal"] = {
            "accepted_signal_id": "accepted-body-pass-signal-001",
            "accepted_signal_category": "BODY_PASS_SIGNAL",
            "selected_signal_recognition_result_id": "body-pass-recognition-001",
            "selected_signal_recognition_result_path": (
                "artifacts/synthetic/body-pass-recognition-001.json"
            ),
            "selected_signal_recognition_outcome": "SIGNAL_RECOGNIZED",
            "recognized_source_artifact_id": "v0-body-pass-001",
            "recognized_source_artifact_path": (
                "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/"
                "v0-body-pass-001.json"
            ),
            "recognized_source_artifact_family": "v0_body_pass_result",
            "recognized_source_artifact_outcome": "V0_BODY_PASS_CONFIRMED",
            "declared_matter_id": "current_signal_recognition_standing",
            "declared_matter_family": "body_signal_acceptance_matter",
            "declared_matter_kind": "recognized_body_signal_posture",
            "declared_matter_purpose": (
                "Hold recognized body signal as current signal recognition standing "
                "posture for structured handling only."
            ),
            "non_authoritative": True,
            "non_permission": True,
            "non_currentness": True,
            "not_scoped_yet": True,
            "not_present_yet": True,
            "not_threshold_yet": True,
            "not_truth": True,
            "no_action": True,
            "no_routing": True,
            "no_workflow": True,
            "no_body_relevance_medium": True,
        }
    return result


def scope_request(
    acceptance: Mapping[str, Any],
    *,
    result_path: str | None = None,
    request_id: str = "scope-body-pass-signal-001",
) -> dict[str, Any]:
    metadata = acceptance["body_signal_acceptance_metadata"]
    accepted = acceptance["accepted_signal"]
    return {
        "signal_scope_request_metadata": {
            "signal_scope_request_id": request_id,
            "signal_scope_request_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_SCOPE_REQUEST"
            ),
            "signal_scope_request_version": "0.1.0",
            "declared_at": "2026-04-26T00:00:01Z",
            "declared_by_surface": "tests/test_resolve_body_signal_scope.py",
        },
        "accepted_signal_basis": {
            "signal_acceptance_result_path": result_path
            or acceptance.get("result_path"),
            "signal_acceptance_result_id": metadata[
                "body_signal_acceptance_result_id"
            ],
            "signal_acceptance_result_version": metadata[
                "body_signal_acceptance_result_version"
            ],
            "signal_acceptance_outcome": acceptance["outcome"],
            "signal_acceptance_resolver_module": metadata["resolver_module"],
            "accepted_signal_id": accepted["accepted_signal_id"],
            "accepted_signal_category": accepted["accepted_signal_category"],
            "accepted_matter_id": accepted["declared_matter_id"],
            "accepted_matter_family": accepted["declared_matter_family"],
            "accepted_matter_kind": accepted["declared_matter_kind"],
            "recognized_source_artifact_id": accepted["recognized_source_artifact_id"],
            "recognized_source_artifact_path": accepted[
                "recognized_source_artifact_path"
            ],
            "recognized_source_artifact_family": accepted[
                "recognized_source_artifact_family"
            ],
            "recognized_source_artifact_outcome": accepted[
                "recognized_source_artifact_outcome"
            ],
        },
        "declared_scope": {
            "scope_id": (
                "current_signal_recognition_standing__"
                "body_pass_signal_nonoperative_posture_scope"
            ),
            "scope_family": "body_signal_scope",
            "scope_kind": "nonoperative_body_pass_signal_posture",
            "scope_matter_id": "current_signal_recognition_standing",
            "scope_purpose": (
                "Bind the accepted BODY_PASS_SIGNAL only as non-operative "
                "signal-line standing evidence inside current_signal_recognition_standing."
            ),
            "scope_boundary": (
                "Applicability only inside current_signal_recognition_standing "
                "for BODY_PASS_SIGNAL posture."
            ),
            "applies_to": [
                "recognized BODY_PASS_SIGNAL posture",
                "accepted signal standing inside current_signal_recognition_standing",
                "non-operative signal-line standing evidence",
            ],
            "does_not_apply_to": [
                "action",
                "permission",
                "currentness",
                "governing basis",
                "signal use",
                "routing",
                "workflow",
                "body relevance medium",
                "presence",
                "threshold",
                "truth",
                "decision",
                "consequence",
                "general continuation",
                "unrelated matters",
            ],
        },
        "declared_scope_limits": {
            "scope_for_applicability_only": True,
            "presence_not_yet_established": True,
            "threshold_not_yet_met": True,
            "truth_not_created": True,
            "action_not_authorized": True,
            "routing_not_created": True,
            "workflow_not_created": True,
            "body_relevance_medium_not_created": True,
            "follow_on_work_not_authorized": True,
        },
        "hierarchy_constraints": {
            field: False for field in HIERARCHY_FALSE_FIELDS
        },
        "correspondence_requirements": {
            field: True for field in CORRESPONDENCE_TRUE_FIELDS
        },
        "declared_non_claims": {
            field: True for field in DECLARED_NON_CLAIM_FIELDS
        },
    }


def set_nested(mapping: dict[str, Any], path: tuple[str, ...], value: Any) -> dict[str, Any]:
    target = mapping
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    return mapping


def remove_nested(mapping: dict[str, Any], path: tuple[str, ...]) -> dict[str, Any]:
    target = mapping
    for key in path[:-1]:
        target = target[key]
    del target[path[-1]]
    return mapping


class BodySignalScopeTests(unittest.TestCase):
    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], code)
        self.assertIn(result["outcome"], {"SIGNAL_SCOPED", "BLOCKED"})

    def assert_false_non_claims(self, result: Mapping[str, Any]) -> None:
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def test_successful_mapping_based_scope(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)

        result = scope.resolve_body_signal_scope(acceptance, request)

        self.assertEqual(set(result), EXPECTED_RESULT_KEYS)
        self.assertEqual(result["outcome"], "SIGNAL_SCOPED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIn(result["outcome"], {"SIGNAL_SCOPED", "BLOCKED"})

        scoped = result["scoped_signal"]
        self.assertIsInstance(scoped, dict)
        for key in (
            "non_authoritative",
            "non_permission",
            "non_currentness",
            "not_present_yet",
            "not_threshold_yet",
            "not_truth",
            "no_action",
            "no_routing",
            "no_workflow",
            "no_body_relevance_medium",
            "no_application_outside_declared_scope",
        ):
            self.assertIs(scoped[key], True)

        for key in (
            "event_bus_created",
            "signal_router_created",
            "body_relevance_medium_created",
            "action_authorized",
            "follow_on_work_authorized",
            "workflow_created",
            "roadmap_created",
            "currentness_created",
            "presence_established",
            "threshold_met",
            "truth_created",
            "permission_created",
            "matter_widened",
            "applied_outside_declared_scope",
        ):
            self.assertIs(result["non_claims"][key], False)

    def test_successful_path_based_scope(self) -> None:
        acceptance = signal_acceptance_result()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "acceptance" / "body-pass-acceptance.json"
            write_json(path, acceptance)
            request = scope_request(acceptance, result_path=str(path))

            result = scope.resolve_body_signal_scope_from_path(path, request)

        self.assertEqual(result["outcome"], "SIGNAL_SCOPED")
        self.assertEqual(
            result["selected_signal_acceptance_result"][
                "signal_acceptance_result_path"
            ],
            str(path),
        )
        self.assertEqual(
            result["selected_signal_scope_request"]["accepted_signal_basis"][
                "signal_acceptance_result_path"
            ],
            str(path),
        )
        self.assertEqual(set(result), EXPECTED_RESULT_KEYS)

    def test_metadata(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        metadata = result["body_signal_scope_metadata"]
        self.assertTrue(REQUIRED_METADATA_KEYS.issubset(metadata))
        for key in REQUIRED_METADATA_KEYS:
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["body_signal_scope_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_body_signal_scope")

    def test_selected_signal_acceptance_result_is_preserved(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        selected = result["selected_signal_acceptance_result"]
        metadata = acceptance["body_signal_acceptance_metadata"]

        self.assertEqual(
            selected["signal_acceptance_result_id"],
            metadata["body_signal_acceptance_result_id"],
        )
        self.assertEqual(
            selected["signal_acceptance_result_path"],
            acceptance["result_path"],
        )
        self.assertEqual(
            selected["signal_acceptance_result_version"],
            metadata["body_signal_acceptance_result_version"],
        )
        self.assertEqual(selected["signal_acceptance_outcome"], "SIGNAL_ACCEPTED")
        self.assertEqual(
            selected["signal_acceptance_resolver_module"],
            "resolve_body_signal_acceptance",
        )
        self.assertEqual(
            selected["selection_mode"],
            "provided_signal_acceptance_mapping",
        )

    def test_selected_accepted_signal_is_preserved(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        selected = result["selected_accepted_signal"]

        self.assertEqual(selected["accepted_signal_id"], "accepted-body-pass-signal-001")
        self.assertEqual(selected["accepted_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(
            selected["declared_matter_id"],
            "current_signal_recognition_standing",
        )
        self.assertEqual(
            selected["declared_matter_family"],
            "body_signal_acceptance_matter",
        )
        self.assertEqual(
            selected["declared_matter_kind"],
            "recognized_body_signal_posture",
        )
        self.assertEqual(selected["recognized_source_artifact_id"], "v0-body-pass-001")
        self.assertEqual(
            selected["recognized_source_artifact_family"],
            "v0_body_pass_result",
        )
        self.assertEqual(
            selected["recognized_source_artifact_outcome"],
            "V0_BODY_PASS_CONFIRMED",
        )
        for key in (
            "non_authoritative",
            "non_permission",
            "non_currentness",
            "not_present_yet",
            "not_threshold_yet",
            "not_truth",
            "no_action",
            "no_routing",
            "no_workflow",
            "no_body_relevance_medium",
        ):
            self.assertIs(selected[key], True)

    def test_selected_scope_request_is_preserved(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        result = scope.resolve_body_signal_scope(acceptance, request)

        selected = result["selected_signal_scope_request"]
        for section in (
            "signal_scope_request_metadata",
            "accepted_signal_basis",
            "declared_scope",
            "declared_scope_limits",
            "hierarchy_constraints",
            "correspondence_requirements",
            "declared_non_claims",
        ):
            self.assertEqual(selected[section], request[section])

    def test_scoped_signal_preserves_bounded_posture(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        result = scope.resolve_body_signal_scope(acceptance, request)
        scoped = result["scoped_signal"]

        self.assertTrue(scoped["scoped_signal_id"])
        self.assertEqual(scoped["scoped_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(
            scoped["selected_signal_acceptance_result_id"],
            "body-pass-signal-acceptance-001",
        )
        self.assertEqual(
            scoped["selected_signal_acceptance_result_path"],
            acceptance["result_path"],
        )
        self.assertEqual(
            scoped["selected_signal_acceptance_outcome"],
            "SIGNAL_ACCEPTED",
        )
        self.assertEqual(scoped["accepted_signal_id"], "accepted-body-pass-signal-001")
        self.assertEqual(scoped["accepted_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(scoped["recognized_source_artifact_id"], "v0-body-pass-001")
        self.assertEqual(
            scoped["recognized_source_artifact_path"],
            acceptance["accepted_signal"]["recognized_source_artifact_path"],
        )
        self.assertEqual(
            scoped["recognized_source_artifact_family"],
            "v0_body_pass_result",
        )
        self.assertEqual(
            scoped["recognized_source_artifact_outcome"],
            "V0_BODY_PASS_CONFIRMED",
        )
        self.assertEqual(
            scoped["accepted_matter_id"],
            "current_signal_recognition_standing",
        )
        self.assertEqual(
            scoped["accepted_matter_family"],
            "body_signal_acceptance_matter",
        )
        self.assertEqual(
            scoped["accepted_matter_kind"],
            "recognized_body_signal_posture",
        )
        self.assertEqual(
            scoped["declared_scope_id"],
            "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope",
        )
        self.assertEqual(scoped["declared_scope_family"], "body_signal_scope")
        self.assertEqual(scoped["declared_scope_kind"], "nonoperative_body_pass_signal_posture")
        self.assertIn("non-operative", scoped["declared_scope_purpose"])
        self.assertIn("Applicability only", scoped["declared_scope_boundary"])
        self.assertEqual(scoped["applies_to"], request["declared_scope"]["applies_to"])
        self.assertEqual(
            scoped["does_not_apply_to"],
            request["declared_scope"]["does_not_apply_to"],
        )
        for key in (
            "non_authoritative",
            "non_permission",
            "non_currentness",
            "not_present_yet",
            "not_threshold_yet",
            "not_truth",
            "no_action",
            "no_routing",
            "no_workflow",
            "no_body_relevance_medium",
            "no_application_outside_declared_scope",
        ):
            self.assertIs(scoped[key], True)

    def test_summary_helper(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))

        summary = scope.build_body_signal_scope_summary(result)

        self.assertEqual(summary["outcome"], "SIGNAL_SCOPED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["selected_signal_acceptance_result_id"],
            "body-pass-signal-acceptance-001",
        )
        self.assertEqual(
            summary["selected_signal_acceptance_result_path"],
            acceptance["result_path"],
        )
        self.assertEqual(
            summary["selected_signal_acceptance_outcome"],
            "SIGNAL_ACCEPTED",
        )
        self.assertEqual(summary["scoped_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(
            summary["accepted_matter_id"],
            "current_signal_recognition_standing",
        )
        self.assertEqual(summary["declared_scope_family"], "body_signal_scope")
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["acceptance_basis_passed"], True)
        self.assertIs(summary["scope_boundary_passed"], True)
        self.assertIs(summary["scope_limits_passed"], True)
        self.assertIs(summary["hierarchy_constraints_passed"], True)
        self.assertIs(summary["correspondence_requirements_passed"], True)
        self.assertIs(summary["non_claims_passed"], True)
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False)

    def test_write_behavior(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "scope-result.json"
            returned = scope.write_body_signal_scope_result(result, output_path)
            parsed = read_json(returned)

        self.assertEqual(returned, output_path)
        self.assertTrue(EXPECTED_RESULT_KEYS.issubset(parsed))
        self.assertEqual(parsed["outcome"], "SIGNAL_SCOPED")

    def test_default_output_path_behavior_uses_bounded_root_without_overwrite(self) -> None:
        acceptance = signal_acceptance_result()
        result = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        original_default = scope._safe_default_output_path
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "scope-root"

            def default_under_temp(value: Mapping[str, Any]) -> Path:
                return original_default(value, root=root)

            with mock.patch.object(
                scope,
                "_safe_default_output_path",
                side_effect=default_under_temp,
            ):
                first = scope.write_body_signal_scope_result(result)
                second = scope.write_body_signal_scope_result(result)

        self.assertEqual(first.parent, root)
        self.assertEqual(second.parent, root)
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__body_signal_scope_result.json"))
        self.assertTrue(second.name.endswith("__body_signal_scope_result_001.json"))

    def test_blocks_missing_signal_acceptance_result(self) -> None:
        request = scope_request(signal_acceptance_result())
        result = scope.resolve_body_signal_scope(None, request)
        self.assert_block(result, "SIGNAL_ACCEPTANCE_RESULT_MISSING")
        self.assertEqual(result["selected_signal_scope_request"], request)

    def test_blocks_missing_scope_request(self) -> None:
        result = scope.resolve_body_signal_scope(signal_acceptance_result(), None)
        self.assert_block(result, "SIGNAL_SCOPE_REQUEST_MISSING")

    def test_blocks_unreadable_and_malformed_path_inputs(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            result = scope.resolve_body_signal_scope_from_path(missing, request)
            self.assert_block(result, "SIGNAL_ACCEPTANCE_RESULT_UNREADABLE")

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            result = scope.resolve_body_signal_scope_from_path(malformed, request)
            self.assert_block(result, "SIGNAL_ACCEPTANCE_RESULT_MALFORMED")

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            result = scope.resolve_body_signal_scope_from_path(array_path, request)
            self.assert_block(result, "SIGNAL_ACCEPTANCE_RESULT_MALFORMED")

    def test_blocks_acceptance_result_not_accepted(self) -> None:
        acceptance = signal_acceptance_result(outcome="BLOCKED")
        request = scope_request(signal_acceptance_result(), request_id="scope-blocked")
        request["accepted_signal_basis"]["signal_acceptance_outcome"] = "BLOCKED"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "SIGNAL_ACCEPTANCE_RESULT_NOT_ACCEPTED")

    def test_blocks_accepted_signal_missing(self) -> None:
        acceptance = signal_acceptance_result(include_accepted_signal=False)
        request = scope_request(signal_acceptance_result())
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_MISSING")

    def test_blocks_malformed_scope_request(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        del request["accepted_signal_basis"]
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "SIGNAL_SCOPE_REQUEST_MALFORMED")

    def test_blocks_accepted_signal_identity_mismatch(self) -> None:
        acceptance = signal_acceptance_result()

        request = scope_request(acceptance)
        request["accepted_signal_basis"]["signal_acceptance_result_id"] = "wrong-id"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH")

        request = scope_request(acceptance)
        request["accepted_signal_basis"]["signal_acceptance_result_path"] = (
            "artifacts/synthetic/wrong-acceptance.json"
        )
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH")

        request = scope_request(acceptance)
        request["accepted_signal_basis"]["accepted_signal_id"] = "wrong-signal"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH")

        request = scope_request(acceptance)
        request["accepted_signal_basis"]["accepted_signal_category"] = "OTHER_SIGNAL"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "SIGNAL_CATEGORY_MISMATCH")

    def test_blocks_recognized_source_identity_mismatch(self) -> None:
        acceptance = signal_acceptance_result()
        mismatches = (
            ("recognized_source_artifact_id", "wrong-source"),
            ("recognized_source_artifact_path", "artifacts/synthetic/wrong-source.json"),
            ("recognized_source_artifact_family", "wrong_family"),
            ("recognized_source_artifact_outcome", "WRONG_OUTCOME"),
        )
        for field, value in mismatches:
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["accepted_signal_basis"][field] = value
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, "RECOGNIZED_SOURCE_IDENTITY_MISMATCH")

    def test_blocks_accepted_matter_mismatch(self) -> None:
        acceptance = signal_acceptance_result()
        mismatches = (
            ("accepted_matter_id", "other_matter"),
            ("accepted_matter_family", "other_family"),
            ("accepted_matter_kind", "other_kind"),
        )
        for field, value in mismatches:
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["accepted_signal_basis"][field] = value
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, "ACCEPTED_MATTER_MISMATCH")

    def test_blocks_unsupported_scope(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        request["declared_scope"]["scope_id"] = "some_other_scope"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "DECLARED_SCOPE_UNSUPPORTED")

    def test_blocks_vague_or_unbounded_scope(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        request["declared_scope"]["scope_purpose"] = "scope this generally"
        request["declared_scope"]["scope_boundary"] = "apply wherever useful"
        request["declared_scope"]["applies_to"] = ["use later"]
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED")

    def test_blocks_scope_widening_or_application_outside_accepted_matter(self) -> None:
        acceptance = signal_acceptance_result()

        request = scope_request(acceptance)
        request["declared_scope"]["scope_matter_id"] = "other_matter"
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER")

        request = scope_request(acceptance)
        request["declared_scope"]["does_not_apply_to"] = [
            value
            for value in request["declared_scope"]["does_not_apply_to"]
            if value != "unrelated matters"
        ]
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER")

        request = scope_request(acceptance)
        request["declared_scope"]["scope_boundary"] = "body-wide applicability"
        request["declared_scope"]["applies_to"].append("governing basis")
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "DECLARED_SCOPE_WIDENS_MATTER")

    def test_blocks_declared_scope_attempts_forbidden_functions(self) -> None:
        cases = {
            "authorize action": "DECLARED_SCOPE_ATTEMPTS_ACTION",
            "create workflow": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
            "route signal": "DECLARED_SCOPE_ATTEMPTS_ROUTING",
            "create roadmap": "DECLARED_SCOPE_ATTEMPTS_ROADMAP",
            "signal use": "DECLARED_SCOPE_ATTEMPTS_SIGNAL_USE",
            "create general continuation": "DECLARED_SCOPE_ATTEMPTS_GENERAL_CONTINUATION",
            "create body relevance medium": "DECLARED_SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
            "establish presence": "SCOPE_ATTEMPTS_PRESENCE",
            "meet threshold": "SCOPE_ATTEMPTS_THRESHOLD",
            "create truth": "SCOPE_ATTEMPTS_TRUTH",
            "scoped signal creates permission": "SCOPED_SIGNAL_BECAME_PERMISSION",
        }
        acceptance = signal_acceptance_result()
        for phrase, expected in cases.items():
            with self.subTest(phrase=phrase):
                request = scope_request(acceptance)
                request["declared_scope"]["scope_purpose"] = (
                    f"{phrase} inside current_signal_recognition_standing"
                )
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, expected)

    def test_blocks_scope_limits_flipped(self) -> None:
        acceptance = signal_acceptance_result()
        for field, expected in SCOPE_LIMIT_TRUE_FIELDS.items():
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["declared_scope_limits"][field] = False
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, expected)

    def test_blocks_hierarchy_constraint_flipped(self) -> None:
        acceptance = signal_acceptance_result()
        for field, expected in HIERARCHY_FALSE_FIELDS.items():
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["hierarchy_constraints"][field] = True
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, expected)

    def test_blocks_correspondence_requirement_missing_or_flipped(self) -> None:
        acceptance = signal_acceptance_result()
        for field, expected in CORRESPONDENCE_TRUE_FIELDS.items():
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["correspondence_requirements"][field] = False
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, expected)

    def test_blocks_declared_non_claim_missing_or_flipped(self) -> None:
        acceptance = signal_acceptance_result()
        for field in DECLARED_NON_CLAIM_FIELDS:
            with self.subTest(field=field):
                request = scope_request(acceptance)
                request["declared_non_claims"][field] = False
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_blocks_latest_file_recency_language(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        request["declared_scope"]["scope_boundary"] = (
            "Applicability only inside current_signal_recognition_standing for "
            "BODY_PASS_SIGNAL posture, using latest file recency."
        )
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "LATEST_FILE_RECENCY_REFUSED")

    def test_blocks_derivative_operator_reentry_signal_collapse_language(self) -> None:
        acceptance = signal_acceptance_result()
        phrases = (
            "derivative as source",
            "operator as source",
            "re-entry as governing",
            "signal as source",
            "signal as governing",
            "receipt as permission",
        )
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                request = scope_request(acceptance)
                request["signal_scope_request_metadata"]["declared_by_surface"] = phrase
                result = scope.resolve_body_signal_scope(acceptance, request)
                self.assert_block(
                    result,
                    "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE",
                )

    def test_blocks_scoped_signal_becomes_permission_or_action(self) -> None:
        acceptance = signal_acceptance_result()

        request = scope_request(acceptance)
        request["signal_scope_request_metadata"]["declared_by_surface"] = (
            "scoped signal creates permission"
        )
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "SCOPED_SIGNAL_BECAME_PERMISSION")

        request = scope_request(acceptance)
        request["signal_scope_request_metadata"]["declared_by_surface"] = (
            "scoped signal authorizes action"
        )
        result = scope.resolve_body_signal_scope(acceptance, request)
        self.assert_block(result, "SCOPED_SIGNAL_BECAME_ACTION")

    def test_result_level_non_claims_remain_false_for_scoped_and_blocked(self) -> None:
        acceptance = signal_acceptance_result()
        scoped = scope.resolve_body_signal_scope(acceptance, scope_request(acceptance))
        blocked = scope.resolve_body_signal_scope(acceptance, None)

        self.assert_false_non_claims(scoped)
        self.assert_false_non_claims(blocked)

    def test_non_mutation_posture(self) -> None:
        acceptance = signal_acceptance_result()
        request = scope_request(acceptance)
        original_acceptance = copy.deepcopy(acceptance)
        original_request = copy.deepcopy(request)

        first = scope.resolve_body_signal_scope(acceptance, request)
        second = scope.resolve_body_signal_scope(acceptance, request)

        self.assertEqual(acceptance, original_acceptance)
        self.assertEqual(request, original_request)
        self.assertEqual(first["selected_signal_scope_request"], original_request)
        self.assertEqual(second["selected_signal_scope_request"], original_request)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "scope-result.json"
            scope.write_body_signal_scope_result(first, output_path)
            with self.assertRaises(FileExistsError):
                scope.write_body_signal_scope_result(first, output_path)
            self.assertEqual(acceptance, original_acceptance)
            self.assertEqual(request, original_request)


if __name__ == "__main__":
    unittest.main()
