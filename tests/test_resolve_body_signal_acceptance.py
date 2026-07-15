"""Bounded tests for body-signal acceptance.

This suite exercises ``src/resolve_body_signal_acceptance.py`` as one
post-recognition acceptance gate:

- one ``SIGNAL_RECOGNIZED`` result
- one signal-acceptance request
- one outcome: ``SIGNAL_ACCEPTED`` or ``BLOCKED``

Acceptance admits a recognized signal only into
``current_signal_recognition_standing`` for structured handling. It is not
scope, presence, threshold, truth, permission, action, routing, workflow,
event bus behavior, body relevance medium implementation, or continuation.
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


import resolve_body_signal_acceptance as acceptance


EXPECTED_RESULT_KEYS = {
    "body_signal_acceptance_metadata",
    "selected_signal_recognition_result",
    "selected_recognized_signal",
    "selected_signal_acceptance_request",
    "declared_matter",
    "signal_acceptance_checks",
    "outcome",
    "block",
    "accepted_signal",
    "body_signal_acceptance_basis",
    "body_signal_acceptance_summary",
    "non_claims",
}

REQUIRED_METADATA_KEYS = {
    "body_signal_acceptance_result_id",
    "body_signal_acceptance_result_type",
    "body_signal_acceptance_result_version",
    "generated_at",
    "resolver_module",
}

REQUIRED_FALSE_RESULT_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "truth_created",
    "scope_assigned",
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
}

SCOPE_TRUE_FIELDS = {
    "acceptance_for_structured_handling_only": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "scope_not_yet_assigned": "ACCEPTANCE_ATTEMPTS_SCOPE",
    "presence_not_yet_established": "ACCEPTANCE_ATTEMPTS_PRESENCE",
    "threshold_not_yet_met": "ACCEPTANCE_ATTEMPTS_THRESHOLD",
    "truth_not_created": "ACCEPTANCE_ATTEMPTS_TRUTH",
    "action_not_authorized": "ACCEPTANCE_ATTEMPTS_ACTION_AUTHORIZATION",
    "routing_not_created": "ACCEPTANCE_ATTEMPTS_SIGNAL_ROUTER",
    "workflow_not_created": "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
    "follow_on_work_not_authorized": "ACCEPTANCE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION",
}

HIERARCHY_FALSE_FIELDS = {
    "accepted_signal_allowed_as_authority": "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY",
    "accepted_signal_allowed_as_permission": "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION",
    "accepted_signal_allowed_as_currentness": "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS",
    "accepted_signal_allowed_as_truth": "ACCEPTANCE_ATTEMPTS_TRUTH",
    "accepted_signal_allowed_as_scope": "ACCEPTANCE_ATTEMPTS_SCOPE",
    "accepted_signal_allowed_as_presence": "ACCEPTANCE_ATTEMPTS_PRESENCE",
    "accepted_signal_allowed_as_threshold": "ACCEPTANCE_ATTEMPTS_THRESHOLD",
    "accepted_signal_allowed_as_action_trigger": "ACCEPTANCE_ATTEMPTS_ACTION_AUTHORIZATION",
    "accepted_signal_allowed_as_workflow": "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
    "accepted_signal_allowed_as_route": "DECLARED_MATTER_ATTEMPTS_ROUTING",
    "accepted_signal_allowed_as_body_relevance_medium": (
        "ACCEPTANCE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
    ),
    "derivative_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "operator_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "reentry_signal_allowed_as_governing_basis": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = {
    "must_preserve_recognized_signal_identity": "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH",
    "must_preserve_recognized_source_identity": "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
    "must_preserve_signal_category": "SIGNAL_CATEGORY_MISMATCH",
    "must_preserve_signal_non_authority": "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY",
    "must_preserve_signal_non_permission": "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION",
    "must_preserve_signal_non_currentness": "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS",
    "must_preserve_matter_boundary": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "must_prevent_under_mirroring": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_create_truth",
    "does_not_create_scope",
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


def signal_recognition_result(
    *,
    result_id: str = "body-pass-signal-recognition-001",
    result_path: str = "artifacts/synthetic/body-pass-signal-recognition-001.json",
    outcome: str = "SIGNAL_RECOGNIZED",
    include_recognized_signal: bool = True,
) -> dict[str, Any]:
    source = {
        "source_artifact_id": "v0-body-pass-001",
        "source_artifact_path": (
            "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/"
            "v0-body-pass-001.json"
        ),
        "source_artifact_family": "v0_body_pass_result",
        "source_artifact_type": "IAMMAI_SYNTHETIC_V0_BODY_PASS_RESULT",
        "source_artifact_outcome": "V0_BODY_PASS_CONFIRMED",
        "resolver_or_emitter_module": "synthetic_body_pass",
        "selection_mode": "synthetic",
    }
    result: dict[str, Any] = {
        "body_signal_recognition_v2_metadata": {
            "body_signal_recognition_result_id": result_id,
            "body_signal_recognition_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_RECOGNITION_V2_RESULT"
            ),
            "body_signal_recognition_result_version": "0.2.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_body_signal_recognition_v2",
            "successor_of_module": "resolve_body_signal_recognition",
        },
        "result_path": result_path,
        "selected_source_artifact": source,
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "SIGNAL_RECOGNIZED"
        else {"block_code": "SYNTHETIC_BLOCK", "block_reason": "synthetic block"},
        "body_signal_recognition_basis": {
            "recognition_scope": "single_source_single_candidate",
            "selected_source_artifact": source,
        },
        "non_claims": {
            "authority_created": False,
            "permission_created": False,
            "currentness_created": False,
            "action_authorized": False,
            "follow_on_work_authorized": False,
            "workflow_created": False,
            "roadmap_created": False,
            "signal_router_created": False,
            "event_bus_created": False,
            "source_replaced": False,
            "derivative_upgraded_to_source": False,
            "receipt_turned_into_permission": False,
        },
    }
    if include_recognized_signal:
        result["recognized_signal"] = {
            "recognized_signal_id": "recognized-body-pass-signal-001",
            "signal_category": "BODY_PASS_SIGNAL",
            "claimed_signal_family": "body_pass_signal",
            "claimed_signal_posture": "v0 body pass confirmed",
            "source_artifact_id": source["source_artifact_id"],
            "source_artifact_path": source["source_artifact_path"],
            "source_artifact_family": source["source_artifact_family"],
            "source_artifact_outcome": source["source_artifact_outcome"],
            "carried_posture": {
                "source_outcome": source["source_artifact_outcome"],
                "source_path": source["source_artifact_path"],
                "source_id": source["source_artifact_id"],
                "source_family": source["source_artifact_family"],
            },
            "non_authoritative": True,
            "non_permission": True,
            "non_currentness": True,
        }
    return result


def acceptance_request(
    recognition: Mapping[str, Any],
    *,
    result_path: str | None = None,
    request_id: str = "accept-body-pass-signal-001",
) -> dict[str, Any]:
    metadata = recognition["body_signal_recognition_v2_metadata"]
    recognized = recognition["recognized_signal"]
    selected_source = recognition["selected_source_artifact"]
    return {
        "signal_acceptance_request_metadata": {
            "signal_acceptance_request_id": request_id,
            "signal_acceptance_request_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_ACCEPTANCE_REQUEST"
            ),
            "signal_acceptance_request_version": "0.1.0",
            "declared_at": "2026-04-26T00:00:01Z",
            "declared_by_surface": "tests/test_resolve_body_signal_acceptance.py",
        },
        "recognized_signal_basis": {
            "signal_recognition_result_path": result_path
            or recognition.get("result_path"),
            "signal_recognition_result_id": metadata[
                "body_signal_recognition_result_id"
            ],
            "signal_recognition_result_version": metadata[
                "body_signal_recognition_result_version"
            ],
            "signal_recognition_outcome": recognition["outcome"],
            "signal_recognition_resolver_module": metadata["resolver_module"],
            "recognized_signal_category": recognized["signal_category"],
            "recognized_source_artifact_id": selected_source["source_artifact_id"],
            "recognized_source_artifact_path": selected_source["source_artifact_path"],
            "recognized_source_artifact_family": selected_source[
                "source_artifact_family"
            ],
            "recognized_source_artifact_outcome": selected_source[
                "source_artifact_outcome"
            ],
        },
        "declared_matter": {
            "matter_id": "current_signal_recognition_standing",
            "matter_family": "body_signal_acceptance_matter",
            "matter_kind": "recognized_body_signal_posture",
            "matter_purpose": (
                "Hold recognized body signal as current signal recognition "
                "standing posture for structured handling only."
            ),
            "matter_boundary": (
                "Bounded to current_signal_recognition_standing structured "
                "handling only; no action, no routing, no workflow, no truth, "
                "no scope, no presence, no threshold."
            ),
        },
        "declared_acceptance_scope": {
            "acceptance_for_structured_handling_only": True,
            "scope_not_yet_assigned": True,
            "presence_not_yet_established": True,
            "threshold_not_yet_met": True,
            "truth_not_created": True,
            "action_not_authorized": True,
            "routing_not_created": True,
            "workflow_not_created": True,
            "follow_on_work_not_authorized": True,
        },
        "hierarchy_constraints": {
            "accepted_signal_allowed_as_authority": False,
            "accepted_signal_allowed_as_permission": False,
            "accepted_signal_allowed_as_currentness": False,
            "accepted_signal_allowed_as_truth": False,
            "accepted_signal_allowed_as_scope": False,
            "accepted_signal_allowed_as_presence": False,
            "accepted_signal_allowed_as_threshold": False,
            "accepted_signal_allowed_as_action_trigger": False,
            "accepted_signal_allowed_as_workflow": False,
            "accepted_signal_allowed_as_route": False,
            "accepted_signal_allowed_as_body_relevance_medium": False,
            "derivative_signal_allowed_as_source": False,
            "operator_signal_allowed_as_source": False,
            "reentry_signal_allowed_as_governing_basis": False,
            "latest_file_recency_allowed": False,
        },
        "correspondence_requirements": {
            "must_preserve_recognized_signal_identity": True,
            "must_preserve_recognized_source_identity": True,
            "must_preserve_signal_category": True,
            "must_preserve_signal_non_authority": True,
            "must_preserve_signal_non_permission": True,
            "must_preserve_signal_non_currentness": True,
            "must_preserve_matter_boundary": True,
            "must_preserve_non_claims": True,
            "must_prevent_over_mirroring": True,
            "must_prevent_under_mirroring": True,
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


class BodySignalAcceptanceTests(unittest.TestCase):
    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], code)
        self.assertIn(result["outcome"], {"SIGNAL_ACCEPTED", "BLOCKED"})

    def assert_false_non_claims(self, result: Mapping[str, Any]) -> None:
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            with self.subTest(non_claim=key):
                self.assertIn(key, result["non_claims"])
                self.assertIs(result["non_claims"][key], False)

    def test_successful_mapping_based_acceptance(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)

        result = acceptance.resolve_body_signal_acceptance(recognition, request)

        self.assertEqual(set(result), EXPECTED_RESULT_KEYS)
        self.assertEqual(result["outcome"], "SIGNAL_ACCEPTED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIn(result["outcome"], {"SIGNAL_ACCEPTED", "BLOCKED"})

        accepted = result["accepted_signal"]
        self.assertIsInstance(accepted, dict)
        for key in (
            "non_authoritative",
            "non_permission",
            "non_currentness",
            "not_scoped_yet",
            "not_present_yet",
            "not_threshold_yet",
            "not_truth",
            "no_action",
            "no_routing",
            "no_workflow",
            "no_body_relevance_medium",
        ):
            self.assertIs(accepted[key], True)

        for key in (
            "event_bus_created",
            "signal_router_created",
            "body_relevance_medium_created",
            "action_authorized",
            "follow_on_work_authorized",
            "workflow_created",
            "roadmap_created",
            "currentness_created",
            "scope_assigned",
            "presence_established",
            "threshold_met",
            "truth_created",
            "permission_created",
        ):
            self.assertIs(result["non_claims"][key], False)

    def test_successful_path_based_acceptance(self) -> None:
        recognition = signal_recognition_result()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "recognition" / "body-pass-signal.json"
            write_json(path, recognition)
            request = acceptance_request(recognition, result_path=str(path))

            result = acceptance.resolve_body_signal_acceptance_from_path(path, request)

        self.assertEqual(result["outcome"], "SIGNAL_ACCEPTED")
        self.assertEqual(
            result["selected_signal_recognition_result"][
                "signal_recognition_result_path"
            ],
            str(path),
        )
        self.assertEqual(
            result["selected_signal_acceptance_request"]["recognized_signal_basis"][
                "signal_recognition_result_path"
            ],
            str(path),
        )
        self.assertEqual(set(result), EXPECTED_RESULT_KEYS)

    def test_metadata(self) -> None:
        result = acceptance.resolve_body_signal_acceptance(
            signal_recognition_result(),
            acceptance_request(signal_recognition_result()),
        )
        metadata = result["body_signal_acceptance_metadata"]
        self.assertTrue(REQUIRED_METADATA_KEYS.issubset(metadata))
        for key in REQUIRED_METADATA_KEYS:
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["body_signal_acceptance_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_body_signal_acceptance")

    def test_selected_signal_recognition_result_is_preserved(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        selected = result["selected_signal_recognition_result"]
        metadata = recognition["body_signal_recognition_v2_metadata"]
        self.assertEqual(
            selected["signal_recognition_result_id"],
            metadata["body_signal_recognition_result_id"],
        )
        self.assertEqual(selected["signal_recognition_result_path"], recognition["result_path"])
        self.assertEqual(
            selected["signal_recognition_result_version"],
            metadata["body_signal_recognition_result_version"],
        )
        self.assertEqual(selected["signal_recognition_outcome"], "SIGNAL_RECOGNIZED")
        self.assertEqual(
            selected["signal_recognition_resolver_module"],
            "resolve_body_signal_recognition_v2",
        )
        self.assertEqual(selected["selection_mode"], "provided_signal_recognition_mapping")

    def test_selected_recognized_signal_is_preserved(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        selected = result["selected_recognized_signal"]
        self.assertEqual(selected["recognized_signal_id"], "recognized-body-pass-signal-001")
        self.assertEqual(selected["signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(selected["source_artifact_id"], "v0-body-pass-001")
        self.assertEqual(selected["source_artifact_family"], "v0_body_pass_result")
        self.assertEqual(selected["source_artifact_outcome"], "V0_BODY_PASS_CONFIRMED")
        self.assertIs(selected["non_authoritative"], True)
        self.assertIs(selected["non_permission"], True)
        self.assertIs(selected["non_currentness"], True)

    def test_selected_acceptance_request_is_preserved(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        result = acceptance.resolve_body_signal_acceptance(recognition, request)

        selected = result["selected_signal_acceptance_request"]
        for section in (
            "signal_acceptance_request_metadata",
            "recognized_signal_basis",
            "declared_matter",
            "declared_acceptance_scope",
            "hierarchy_constraints",
            "correspondence_requirements",
            "declared_non_claims",
        ):
            self.assertEqual(selected[section], request[section])

    def test_accepted_signal_preserves_bounded_posture(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        accepted = result["accepted_signal"]
        self.assertTrue(accepted["accepted_signal_id"])
        self.assertEqual(accepted["accepted_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(
            accepted["selected_signal_recognition_result_id"],
            "body-pass-signal-recognition-001",
        )
        self.assertEqual(
            accepted["selected_signal_recognition_result_path"],
            recognition["result_path"],
        )
        self.assertEqual(
            accepted["selected_signal_recognition_outcome"],
            "SIGNAL_RECOGNIZED",
        )
        self.assertEqual(accepted["recognized_source_artifact_id"], "v0-body-pass-001")
        self.assertEqual(
            accepted["recognized_source_artifact_family"],
            "v0_body_pass_result",
        )
        self.assertEqual(
            accepted["recognized_source_artifact_outcome"],
            "V0_BODY_PASS_CONFIRMED",
        )
        self.assertEqual(
            accepted["declared_matter_id"],
            "current_signal_recognition_standing",
        )
        self.assertEqual(
            accepted["declared_matter_family"],
            "body_signal_acceptance_matter",
        )
        self.assertEqual(
            accepted["declared_matter_kind"],
            "recognized_body_signal_posture",
        )
        self.assertIn("structured handling", accepted["declared_matter_purpose"])

    def test_summary_helper(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )

        summary = acceptance.build_body_signal_acceptance_summary(result)

        self.assertEqual(summary["outcome"], "SIGNAL_ACCEPTED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["selected_signal_recognition_result_id"],
            "body-pass-signal-recognition-001",
        )
        self.assertEqual(summary["accepted_signal_category"], "BODY_PASS_SIGNAL")
        self.assertEqual(
            summary["declared_matter_id"],
            "current_signal_recognition_standing",
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["recognition_basis_passed"], True)
        self.assertIs(summary["matter_boundary_passed"], True)
        self.assertIs(summary["acceptance_scope_passed"], True)
        self.assertIs(summary["hierarchy_constraints_passed"], True)
        self.assertIs(summary["correspondence_requirements_passed"], True)
        self.assertIs(summary["non_claims_passed"], True)
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False)

    def test_write_behavior(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "acceptance-result.json"
            returned = acceptance.write_body_signal_acceptance_result(result, output_path)
            parsed = read_json(returned)

        self.assertEqual(returned, output_path)
        self.assertTrue(EXPECTED_RESULT_KEYS.issubset(parsed))
        self.assertEqual(parsed["outcome"], "SIGNAL_ACCEPTED")

    def test_default_output_path_behavior_uses_bounded_root_without_overwrite(self) -> None:
        recognition = signal_recognition_result()
        result = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        original_default = acceptance._safe_default_output_path
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "acceptance-root"

            def default_under_temp(value: Mapping[str, Any]) -> Path:
                return original_default(value, root=root)

            with mock.patch.object(
                acceptance,
                "_safe_default_output_path",
                side_effect=default_under_temp,
            ):
                first = acceptance.write_body_signal_acceptance_result(result)
                second = acceptance.write_body_signal_acceptance_result(result)

        self.assertEqual(first.parent, root)
        self.assertEqual(second.parent, root)
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__body_signal_acceptance_result.json"))
        self.assertTrue(second.name.endswith("__body_signal_acceptance_result_001.json"))

    def test_blocks_missing_signal_recognition_result(self) -> None:
        request = acceptance_request(signal_recognition_result())
        result = acceptance.resolve_body_signal_acceptance(None, request)
        self.assert_block(result, "SIGNAL_RECOGNITION_RESULT_MISSING")
        self.assertEqual(result["selected_signal_acceptance_request"], request)

    def test_blocks_missing_acceptance_request(self) -> None:
        result = acceptance.resolve_body_signal_acceptance(signal_recognition_result(), None)
        self.assert_block(result, "SIGNAL_ACCEPTANCE_REQUEST_MISSING")

    def test_blocks_unreadable_and_malformed_path_inputs(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            result = acceptance.resolve_body_signal_acceptance_from_path(missing, request)
            self.assert_block(result, "SIGNAL_RECOGNITION_RESULT_UNREADABLE")

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            result = acceptance.resolve_body_signal_acceptance_from_path(malformed, request)
            self.assert_block(result, "SIGNAL_RECOGNITION_RESULT_MALFORMED")

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            result = acceptance.resolve_body_signal_acceptance_from_path(array_path, request)
            self.assert_block(result, "SIGNAL_RECOGNITION_RESULT_MALFORMED")

    def test_blocks_recognition_result_not_recognized(self) -> None:
        recognition = signal_recognition_result(outcome="BLOCKED")
        request = acceptance_request(
            signal_recognition_result(),
            request_id="accept-blocked-recognition",
        )
        request["recognized_signal_basis"]["signal_recognition_outcome"] = "BLOCKED"
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "SIGNAL_RECOGNITION_RESULT_NOT_RECOGNIZED")

    def test_blocks_recognized_signal_missing(self) -> None:
        recognition = signal_recognition_result(include_recognized_signal=False)
        request = acceptance_request(signal_recognition_result())
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "RECOGNIZED_SIGNAL_MISSING")

    def test_blocks_malformed_acceptance_request(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        del request["recognized_signal_basis"]
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED")

    def test_blocks_recognized_signal_identity_mismatch(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        request["recognized_signal_basis"]["signal_recognition_result_id"] = "wrong-id"
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH")

        request = acceptance_request(recognition)
        request["recognized_signal_basis"]["recognized_signal_category"] = "OTHER_SIGNAL"
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "SIGNAL_CATEGORY_MISMATCH")

        request = acceptance_request(recognition)
        request["recognized_signal_basis"]["signal_recognition_result_path"] = (
            "artifacts/synthetic/wrong-recognition.json"
        )
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH")

    def test_blocks_recognized_source_identity_mismatch(self) -> None:
        recognition = signal_recognition_result()
        mismatches = (
            ("recognized_source_artifact_id", "wrong-source"),
            ("recognized_source_artifact_path", "artifacts/synthetic/wrong-source.json"),
            ("recognized_source_artifact_family", "wrong_family"),
            ("recognized_source_artifact_outcome", "WRONG_OUTCOME"),
        )
        for field, value in mismatches:
            with self.subTest(field=field):
                request = acceptance_request(recognition)
                request["recognized_signal_basis"][field] = value
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, "RECOGNIZED_SOURCE_IDENTITY_MISMATCH")

    def test_blocks_unsupported_matter(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        request["declared_matter"]["matter_id"] = "some_other_matter"
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "DECLARED_MATTER_UNSUPPORTED")

    def test_blocks_vague_or_unbounded_matter(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        request["declared_matter"]["matter_purpose"] = (
            "use signal later for current signal recognition standing"
        )
        request["declared_matter"]["matter_boundary"] = "general signal handling"
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "DECLARED_MATTER_VAGUE_OR_UNBOUNDED")

    def test_blocks_matter_attempts_forbidden_functions(self) -> None:
        cases = {
            "authorize action for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_ACTION"
            ),
            "create workflow for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_WORKFLOW"
            ),
            "route signal for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_ROUTING"
            ),
            "create roadmap for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_ROADMAP"
            ),
            "create general continuation for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_GENERAL_CONTINUATION"
            ),
            "create body relevance medium for current signal recognition standing": (
                "DECLARED_MATTER_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
            ),
            "signal use for current signal recognition standing": (
                "DECLARED_MATTER_VAGUE_OR_UNBOUNDED"
            ),
            "assign scope for current signal recognition standing": (
                "ACCEPTANCE_ATTEMPTS_SCOPE"
            ),
            "establish presence for current signal recognition standing": (
                "ACCEPTANCE_ATTEMPTS_PRESENCE"
            ),
            "meet threshold for current signal recognition standing": (
                "ACCEPTANCE_ATTEMPTS_THRESHOLD"
            ),
            "create truth for current signal recognition standing": (
                "ACCEPTANCE_ATTEMPTS_TRUTH"
            ),
        }
        recognition = signal_recognition_result()
        for phrase, expected_code in cases.items():
            with self.subTest(phrase=phrase):
                request = acceptance_request(recognition)
                request["declared_matter"]["matter_purpose"] = phrase
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, expected_code)

    def test_blocks_acceptance_scope_flipped(self) -> None:
        recognition = signal_recognition_result()
        for field, expected_code in SCOPE_TRUE_FIELDS.items():
            with self.subTest(field=field):
                request = acceptance_request(recognition)
                request["declared_acceptance_scope"][field] = False
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, expected_code)

    def test_blocks_hierarchy_constraint_flipped_or_missing(self) -> None:
        recognition = signal_recognition_result()
        for field, expected_code in HIERARCHY_FALSE_FIELDS.items():
            with self.subTest(field=field, mode="flipped"):
                request = acceptance_request(recognition)
                request["hierarchy_constraints"][field] = True
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, expected_code)
            with self.subTest(field=field, mode="missing"):
                request = acceptance_request(recognition)
                del request["hierarchy_constraints"][field]
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, expected_code)

    def test_blocks_correspondence_requirement_flipped(self) -> None:
        recognition = signal_recognition_result()
        for field, expected_code in CORRESPONDENCE_TRUE_FIELDS.items():
            with self.subTest(field=field):
                request = acceptance_request(recognition)
                request["correspondence_requirements"][field] = False
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, expected_code)

    def test_blocks_declared_non_claim_missing_or_flipped(self) -> None:
        recognition = signal_recognition_result()
        for field in DECLARED_NON_CLAIM_FIELDS:
            with self.subTest(field=field, mode="flipped"):
                request = acceptance_request(recognition)
                request["declared_non_claims"][field] = False
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, "NON_CLAIM_MISSING_OR_FLIPPED")
            with self.subTest(field=field, mode="missing"):
                request = acceptance_request(recognition)
                del request["declared_non_claims"][field]
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_blocks_latest_file_recency_language(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        request["declared_matter"]["matter_purpose"] += " latest file recency decides."
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "LATEST_FILE_RECENCY_REFUSED")

    def test_blocks_derivative_operator_reentry_collapse_language(self) -> None:
        recognition = signal_recognition_result()
        cases = (
            "derivative as source",
            "operator as source",
            "re-entry as governing",
            "receipt as permission",
        )
        for phrase in cases:
            with self.subTest(phrase=phrase):
                request = acceptance_request(recognition)
                request["declared_matter"]["matter_boundary"] += f" {phrase}."
                result = acceptance.resolve_body_signal_acceptance(recognition, request)
                self.assert_block(result, "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE")

    def test_blocks_accepted_signal_becomes_permission_or_action(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        request["declared_matter"]["matter_boundary"] += (
            " accepted signal creates permission."
        )
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_BECAME_PERMISSION")

        request = acceptance_request(recognition)
        request["declared_matter"]["matter_boundary"] += (
            " accepted signal authorizes action."
        )
        result = acceptance.resolve_body_signal_acceptance(recognition, request)
        self.assert_block(result, "ACCEPTED_SIGNAL_BECAME_ACTION")

    def test_non_claims_posture_for_accepted_and_blocked_results(self) -> None:
        recognition = signal_recognition_result()
        accepted = acceptance.resolve_body_signal_acceptance(
            recognition,
            acceptance_request(recognition),
        )
        blocked = acceptance.resolve_body_signal_acceptance(None, acceptance_request(recognition))
        self.assert_false_non_claims(accepted)
        self.assert_false_non_claims(blocked)

    def test_non_mutation_posture(self) -> None:
        recognition = signal_recognition_result()
        request = acceptance_request(recognition)
        original_recognition = copy.deepcopy(recognition)
        original_request = copy.deepcopy(request)

        first = acceptance.resolve_body_signal_acceptance(recognition, request)
        second = acceptance.resolve_body_signal_acceptance(recognition, request)

        self.assertEqual(recognition, original_recognition)
        self.assertEqual(request, original_request)
        self.assertEqual(first["outcome"], "SIGNAL_ACCEPTED")
        self.assertEqual(second["outcome"], "SIGNAL_ACCEPTED")

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "acceptance.json"
            acceptance.write_body_signal_acceptance_result(first, target)
            self.assertTrue(target.exists())
            self.assertEqual(recognition, original_recognition)
            self.assertEqual(request, original_request)


if __name__ == "__main__":
    unittest.main()
