"""Bounded tests for body-signal recognition v2.

This suite exercises ``src/resolve_body_signal_recognition_v2.py`` as one
single-candidate successor surface:

- one standing source artifact/result
- one candidate signal declaration
- one outcome: ``SIGNAL_RECOGNIZED`` or ``BLOCKED``

V2 preserves the v1 signal-recognition boundary and corrects the live
source-identity extraction failure where a selected v0 body-pass artifact was
misread through nested derivative/action content instead of its own selected
path and top-level body-pass outcome.

Recognition is not authority, permission, currentness, routing, priority,
scheduling, aggregation, RADIO 22, workflow, roadmap, or continuation.
"""

from __future__ import annotations

import contextlib
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


import resolve_body_signal_recognition_v2 as recognition


EXPECTED_RESULT_KEYS = {
    "body_signal_recognition_v2_metadata",
    "selected_source_artifact",
    "selected_candidate_signal",
    "signal_recognition_checks",
    "outcome",
    "block",
    "recognized_signal",
    "body_signal_recognition_basis",
    "body_signal_recognition_summary",
    "non_claims",
}

REQUIRED_METADATA_KEYS = {
    "body_signal_recognition_result_id",
    "body_signal_recognition_result_type",
    "body_signal_recognition_result_version",
    "generated_at",
    "resolver_module",
    "successor_of_module",
}

HIERARCHY_FALSE_FIELDS = {
    "signal_allowed_as_authority": "SIGNAL_ATTEMPTS_AUTHORITY",
    "signal_allowed_as_permission": "SIGNAL_ATTEMPTS_PERMISSION",
    "signal_allowed_as_currentness_selector": "SIGNAL_ATTEMPTS_CURRENTNESS",
    "derivative_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "operator_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "reentry_signal_allowed_as_governing_basis": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = {
    "must_preserve_source_identity": "SOURCE_IDENTITY_NOT_PRESERVED",
    "must_preserve_source_outcome": "SOURCE_OUTCOME_NOT_PRESERVED",
    "must_preserve_signal_category_source_match": "SIGNAL_CATEGORY_MISMATCHES_SOURCE",
    "must_preserve_derivative_source_distinction": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "must_preserve_open_blocked_receipt_exhaustion_distinctions": "RELEVANT_POSTURE_OMITTED",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "SIGNAL_OVER_MIRRORS_SOURCE",
    "must_prevent_under_mirroring": "SIGNAL_UNDER_MIRRORS_SOURCE",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_authorize_action",
    "does_not_authorize_follow_on_work",
    "does_not_create_workflow",
    "does_not_create_roadmap",
    "does_not_create_signal_router",
    "does_not_create_event_bus",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_turn_receipt_into_permission",
)

REQUIRED_FALSE_RESULT_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "action_authorized",
    "follow_on_work_authorized",
    "workflow_created",
    "roadmap_created",
    "signal_router_created",
    "event_bus_created",
    "source_replaced",
    "derivative_upgraded_to_source",
    "receipt_turned_into_permission",
    "radio_22_implemented",
}


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


def source_artifact(
    *,
    result_id: str = "source-current-state-001",
    family: str = "current_state_what_stands_now_result",
    result_type: str = "IAMMAI_SYNTHETIC_CURRENT_STATE_RESULT",
    outcome: str = "ANSWERED_WHAT_STANDS_NOW",
    path: str = "artifacts/synthetic/source-current-state-001.json",
    resolver_module: str = "synthetic_source_resolver",
    include_non_claims: bool = True,
) -> dict[str, Any]:
    source = {
        "result_id": result_id,
        "result_family": family,
        "result_type": result_type,
        "outcome": outcome,
        "result_path": path,
        "resolver_module": resolver_module,
    }
    if include_non_claims:
        source["non_claims"] = {
            "authority_created": False,
            "permission_created": False,
            "currentness_created": False,
            "workflow_created": False,
            "roadmap_created": False,
        }
    return source


def category_source(category: str) -> dict[str, Any]:
    cases = {
        "CURRENT_BASIS_SIGNAL": dict(
            family="current_governing_effective_basis_result",
            result_type="IAMMAI_SYNTHETIC_CURRENT_GOVERNING_BASIS_RESULT",
            outcome="CURRENT_GOVERNING_BASIS_SELECTED",
        ),
        "CURRENT_STATE_SIGNAL": dict(
            family="current_state_what_stands_now_result",
            result_type="IAMMAI_SYNTHETIC_CURRENT_STATE_RESULT",
            outcome="ANSWERED_WHAT_STANDS_NOW",
        ),
        "OPEN_SURFACE_SIGNAL": dict(
            family="current_state_what_remains_open_result",
            result_type="IAMMAI_SYNTHETIC_WHAT_REMAINS_OPEN_RESULT",
            outcome="OPEN_SURFACE_RECOGNIZED",
        ),
        "BLOCKED_REFUSED_SIGNAL": dict(
            family="current_state_query_result",
            result_type="IAMMAI_SYNTHETIC_CURRENT_STATE_QUERY_RESULT",
            outcome="BLOCKED",
        ),
        "TOUCH_ADMISSIBILITY_SIGNAL": dict(
            family="current_state_touch_permission_result",
            result_type="IAMMAI_SYNTHETIC_TOUCH_PERMISSION_RESULT",
            outcome="TOUCH_PERMISSION_ADMITTED",
        ),
        "CONTINUITY_TRANSFER_SIGNAL": dict(
            family="continuity_transfer_unit_result",
            result_type="IAMMAI_SYNTHETIC_CONTINUITY_TRANSFER_UNIT_RESULT",
            outcome="CONTINUITY_TRANSFERRED",
        ),
        "CONTINUITY_RECEIPT_SIGNAL": dict(
            family="continuity_transfer_receipt_result",
            result_type="IAMMAI_SYNTHETIC_CONTINUITY_TRANSFER_RECEIPT_RESULT",
            outcome="CONTINUITY_RECEIPT_RECEIVED",
        ),
        "DERIVATIVE_PARTICIPATION_SIGNAL": dict(
            family="received_derivative_participation_result",
            result_type="IAMMAI_SYNTHETIC_DERIVATIVE_PARTICIPATION_RESULT",
            outcome="DERIVATIVE_PARTICIPATION_RECEIVED",
        ),
        "DERIVATIVE_ACTION_PERMISSION_SIGNAL": dict(
            family="received_derivative_action_permission_result",
            result_type="IAMMAI_SYNTHETIC_DERIVATIVE_ACTION_PERMISSION_RESULT",
            outcome="DERIVATIVE_ACTION_PERMISSION_RECEIVED",
        ),
        "MEMORY_SEAM_SIGNAL": dict(
            family="continuity_memory_seam_result",
            result_type="IAMMAI_SYNTHETIC_CONTINUITY_MEMORY_SEAM_RESULT",
            outcome="CONTINUITY_MEMORY_SEAM_CLOSED",
        ),
        "BODY_PASS_SIGNAL": dict(
            family="v0_body_pass_result",
            result_type="IAMMAI_SYNTHETIC_V0_BODY_PASS_RESULT",
            outcome="V0_BODY_PASS_CONFIRMED",
        ),
        "DERIVATIVE_VESSEL_SIGNAL": dict(
            family="openai_api_derivative_vessel_bounded_current_state_read_v3_result",
            result_type="IAMMAI_SYNTHETIC_OPENAI_API_DERIVATIVE_VESSEL_RESULT",
            outcome="DERIVATIVE_VESSEL_ANSWERED",
        ),
        "OPERATOR_FACING_SIGNAL": dict(
            family="operator_terminal_brief_result",
            result_type="IAMMAI_SYNTHETIC_OPERATOR_TERMINAL_BRIEF_RESULT",
            outcome="OPERATOR_TERMINAL_BRIEF_RENDERED",
        ),
        "REENTRY_ADMISSIBILITY_SIGNAL": dict(
            family="current_self_orientation_reentry_admissibility_result",
            result_type="IAMMAI_SYNTHETIC_REENTRY_ADMISSIBILITY_RESULT",
            outcome="REENTRY_ADMITTED",
        ),
        "REENTRY_RECEIPT_SIGNAL": dict(
            family="current_self_orientation_reentry_receipt_result",
            result_type="IAMMAI_SYNTHETIC_REENTRY_RECEIPT_RESULT",
            outcome="REENTRY_RECEIVED",
        ),
        "EXHAUSTION_CLOSURE_SIGNAL": dict(
            family="current_self_orientation_reentry_receipt_result",
            result_type="IAMMAI_SYNTHETIC_REENTRY_RECEIPT_RESULT",
            outcome="REENTRY_RECEIVED",
        ),
        "NON_CLAIM_SIGNAL": dict(
            family="current_state_what_stands_now_result",
            result_type="IAMMAI_SYNTHETIC_NON_CLAIM_BEARING_RESULT",
            outcome="ANSWERED_WHAT_STANDS_NOW",
        ),
    }
    spec = cases[category]
    safe = category.lower().replace("_signal", "")
    return source_artifact(
        result_id=f"source-{safe}",
        family=spec["family"],
        result_type=spec["result_type"],
        outcome=spec["outcome"],
        path=f"artifacts/synthetic/source-{safe}.json",
        include_non_claims=True,
    )


def category_carried_posture(category: str) -> dict[str, Any]:
    if category == "OPEN_SURFACE_SIGNAL":
        return {"open_status": "OPEN"}
    if category == "BLOCKED_REFUSED_SIGNAL":
        return {"blocked_refused_status": "BLOCKED"}
    if category in {"CONTINUITY_RECEIPT_SIGNAL", "REENTRY_RECEIPT_SIGNAL"}:
        return {"receipt_status": "RECEIVED"}
    if category == "EXHAUSTION_CLOSURE_SIGNAL":
        return {"exhaustion_status": "EXHAUSTED"}
    if category in {
        "DERIVATIVE_VESSEL_SIGNAL",
        "DERIVATIVE_PARTICIPATION_SIGNAL",
        "DERIVATIVE_ACTION_PERMISSION_SIGNAL",
    }:
        return {"derivative_status": "DERIVATIVE"}
    if category == "OPERATOR_FACING_SIGNAL":
        return {"operator_facing_status": "OPERATOR_FACING"}
    if category == "NON_CLAIM_SIGNAL":
        return {"non_claims": {"authority_created": False, "permission_created": False}}
    return {}


def candidate_signal(
    source: Mapping[str, Any],
    *,
    category: str = "CURRENT_STATE_SIGNAL",
    candidate_id: str = "candidate-current-state-signal-001",
    source_path: str | None = None,
    candidate_family: str | None = None,
    claimed_reason: str | None = None,
) -> dict[str, Any]:
    path = source_path if source_path is not None else str(source["result_path"])
    family = candidate_family if candidate_family is not None else str(source["result_family"])
    carried = {
        "source_artifact_id": source["result_id"],
        "source_artifact_path": path,
        "source_artifact_family": family,
        "source_outcome": source["outcome"],
        "bounded_relation_to_current_self_orientation": "source_posture_only",
    }
    carried.update(category_carried_posture(category))
    return {
        "candidate_signal_metadata": {
            "candidate_signal_id": candidate_id,
            "candidate_signal_type": "IAMMAI_SYNTHETIC_CANDIDATE_BODY_SIGNAL",
            "candidate_signal_version": "0.2.0",
            "declared_at": "2026-04-25T00:00:00Z",
            "declared_by_surface": "tests/test_resolve_body_signal_recognition_v2.py",
        },
        "source_artifact_basis": {
            "source_artifact_path": path,
            "source_artifact_id": source["result_id"],
            "source_artifact_family": family,
            "source_artifact_type": source["result_type"],
            "source_artifact_outcome": source["outcome"],
            "source_artifact_resolver_or_emitter_module": source["resolver_module"],
        },
        "claimed_signal": {
            "signal_category": category,
            "claimed_signal_family": category.lower(),
            "claimed_signal_posture": "source posture preserved",
            "claimed_signal_reason": (
                claimed_reason
                if claimed_reason is not None
                else "selected source posture is visible as bounded signal"
            ),
            "claimed_relevance": "preserves one source posture for later lawful recognition",
            "claimed_carried_fields": sorted(carried.keys()),
        },
        "carried_posture": carried,
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


def body_pass_artifact(
    *,
    result_id: str = "synthetic-body-pass-confirmed",
    result_type: str = "IAMMAI_SYNTHETIC_V0_BODY_PASS_RESULT",
) -> dict[str, Any]:
    return {
        "outcome": "V0_BODY_PASS_CONFIRMED",
        "v0_body_pass_metadata": {
            "v0_body_pass_result_id": result_id,
            "v0_body_pass_result_type": result_type,
            "v0_body_pass_result_version": "0.1.0",
            "generated_at": "2026-04-25T00:00:00Z",
            "runner_module": "run_integrity_host_v0_min_coexistence_v0_body_pass",
        },
        "selected_action_permission_result": {
            "result_family": "received_derivative_action_permission",
            "outcome": "ACTION_PERMITTED",
        },
        "selected_participation_result": {
            "result_family": "received_derivative_participation",
            "outcome": "PARTICIPATED",
        },
        "selected_receipt_result": {
            "result_family": "continuity_transfer_receipt",
            "outcome": "RECEIVED",
        },
        "checks": [
            {
                "check_name": "nested_derivative_action_surface_visible",
                "actual_posture": "received_derivative_action_permission",
                "expected_posture": "nested surface remains nested",
                "passed": True,
            }
        ],
    }


def body_pass_source_from_artifact(
    artifact: Mapping[str, Any],
    source_path: str,
) -> dict[str, Any]:
    metadata = artifact.get("v0_body_pass_metadata")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    return source_artifact(
        result_id=str(metadata.get("v0_body_pass_result_id", "body-pass-result")),
        family="v0_body_pass_result",
        result_type=str(metadata.get("v0_body_pass_result_type", "V0_BODY_PASS_RESULT")),
        outcome=str(artifact.get("outcome", "V0_BODY_PASS_CONFIRMED")),
        path=source_path,
        resolver_module=str(
            metadata.get("runner_module", "run_integrity_host_v0_min_coexistence_v0_body_pass")
        ),
        include_non_claims=True,
    )


def check_by_name(result: Mapping[str, Any], name: str) -> Mapping[str, Any]:
    for check in result["signal_recognition_checks"]:
        if check["check_name"] == name:
            return check
    raise AssertionError(f"missing check {name}")


class BodySignalRecognitionV2Tests(unittest.TestCase):
    maxDiff = None

    def assert_result_shape(self, result: Mapping[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(EXPECTED_RESULT_KEYS.issubset(result.keys()))
        self.assertIn(result["outcome"], {"SIGNAL_RECOGNIZED", "BLOCKED"})

    def assert_block(self, result: Mapping[str, Any], expected: str | set[str]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], "BLOCKED")
        code = result["block"]["block_code"]
        if isinstance(expected, set):
            self.assertIn(code, expected)
        else:
            self.assertEqual(code, expected)
        self.assertIsNone(result["recognized_signal"])

    def assert_result_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def recognized_result(self) -> dict[str, Any]:
        source = source_artifact()
        candidate = candidate_signal(source)
        return recognition.resolve_body_signal_recognition(source, candidate)

    def test_successful_v2_mapping_based_recognition(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsNotNone(result["recognized_signal"])
        self.assertTrue(result["recognized_signal"]["non_authoritative"])
        self.assertTrue(result["recognized_signal"]["non_permission"])
        self.assertTrue(result["recognized_signal"]["non_currentness"])
        self.assert_result_non_claims_false(result)
        self.assertFalse(result["non_claims"]["radio_22_implemented"])
        self.assertFalse(result["non_claims"]["signal_router_created"])
        self.assertFalse(result["non_claims"]["event_bus_created"])
        self.assertFalse(result["non_claims"]["workflow_created"])
        self.assertFalse(result["non_claims"]["roadmap_created"])
        self.assertFalse(result["body_signal_recognition_basis"]["recognition_routes_signal"])
        self.assertFalse(result["body_signal_recognition_basis"]["recognition_authorizes_action"])
        self.assertFalse(
            result["body_signal_recognition_basis"]["recognition_authorizes_follow_on_work"]
        )

    def test_successful_v2_path_based_recognition(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_path = Path(tmp) / "source.json"
            source = source_artifact(path=source_path.as_posix())
            write_json(source_path, source)
            candidate = candidate_signal(source, source_path=source_path.as_posix())

            result = recognition.resolve_body_signal_recognition_from_path(
                source_path,
                candidate,
            )

        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
        self.assertEqual(
            result["selected_source_artifact"]["source_artifact_path"],
            source_path.as_posix(),
        )
        self.assertEqual(
            result["selected_candidate_signal"]["source_artifact_basis"][
                "source_artifact_path"
            ],
            source_path.as_posix(),
        )
        self.assertEqual(set(result.keys()), EXPECTED_RESULT_KEYS)
        metadata = result["body_signal_recognition_v2_metadata"]
        self.assertEqual(metadata["resolver_module"], "resolve_body_signal_recognition_v2")
        self.assertEqual(metadata["successor_of_module"], "resolve_body_signal_recognition")

    def test_metadata_selected_sections_and_recognized_signal(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        result = recognition.resolve_body_signal_recognition(source, candidate)

        metadata = result["body_signal_recognition_v2_metadata"]
        for key in REQUIRED_METADATA_KEYS:
            self.assertIsInstance(metadata.get(key), str)
            self.assertTrue(metadata[key])
        self.assertEqual(metadata["body_signal_recognition_result_version"], "0.2.0")
        self.assertEqual(metadata["resolver_module"], "resolve_body_signal_recognition_v2")
        self.assertEqual(metadata["successor_of_module"], "resolve_body_signal_recognition")

        selected_source = result["selected_source_artifact"]
        self.assertEqual(selected_source["source_artifact_id"], source["result_id"])
        self.assertEqual(selected_source["source_artifact_path"], source["result_path"])
        self.assertEqual(selected_source["source_artifact_family"], source["result_family"])
        self.assertEqual(selected_source["source_artifact_type"], source["result_type"])
        self.assertEqual(selected_source["source_artifact_outcome"], source["outcome"])
        self.assertEqual(
            selected_source["source_artifact_resolver_or_emitter_module"],
            source["resolver_module"],
        )
        self.assertEqual(selected_source["selection_mode"], "provided_source_mapping")

        selected_candidate = result["selected_candidate_signal"]
        for section in (
            "candidate_signal_metadata",
            "source_artifact_basis",
            "claimed_signal",
            "carried_posture",
            "hierarchy_constraints",
            "correspondence_requirements",
            "declared_non_claims",
        ):
            self.assertEqual(selected_candidate[section], candidate[section])

        recognized = result["recognized_signal"]
        self.assertIsInstance(recognized["recognized_signal_id"], str)
        self.assertEqual(recognized["signal_category"], "CURRENT_STATE_SIGNAL")
        self.assertEqual(
            recognized["claimed_signal_family"],
            candidate["claimed_signal"]["claimed_signal_family"],
        )
        self.assertEqual(
            recognized["claimed_signal_posture"],
            candidate["claimed_signal"]["claimed_signal_posture"],
        )
        self.assertEqual(recognized["source_artifact_id"], source["result_id"])
        self.assertEqual(recognized["source_artifact_path"], source["result_path"])
        self.assertEqual(recognized["source_artifact_family"], source["result_family"])
        self.assertEqual(recognized["source_artifact_outcome"], source["outcome"])
        self.assertEqual(recognized["carried_posture"], candidate["carried_posture"])
        self.assertTrue(recognized["non_authoritative"])
        self.assertTrue(recognized["non_permission"])
        self.assertTrue(recognized["non_currentness"])

    def test_live_body_pass_path_alignment(self) -> None:
        live_paths = sorted(
            (REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_v0_body_pass").glob(
                "*.json"
            )
        )
        patch_context = contextlib.nullcontext()
        temp_dir: tempfile.TemporaryDirectory[str] | None = None
        try:
            if live_paths:
                body_pass_path = live_paths[0]
                source_path = body_pass_path.relative_to(REPO_ROOT).as_posix()
                artifact = read_json(body_pass_path)
                path_arg = source_path
            else:
                temp_dir = tempfile.TemporaryDirectory()
                temp_root = Path(temp_dir.name)
                body_pass_path = (
                    temp_root
                    / "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/body_pass.json"
                )
                artifact = body_pass_artifact()
                write_json(body_pass_path, artifact)
                source_path = body_pass_path.relative_to(temp_root).as_posix()
                path_arg = body_pass_path
                patch_context = mock.patch.object(recognition, "_repo_root", return_value=temp_root)

            source = body_pass_source_from_artifact(artifact, source_path)
            candidate = candidate_signal(
                source,
                category="BODY_PASS_SIGNAL",
                candidate_id="candidate-live-body-pass-signal",
                source_path=source_path,
            )
            with patch_context:
                result = recognition.resolve_body_signal_recognition_from_path(
                    path_arg,
                    candidate,
                )
        finally:
            if temp_dir is not None:
                temp_dir.cleanup()

        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
        selected = result["selected_source_artifact"]
        self.assertEqual(selected["source_artifact_family"], "v0_body_pass_result")
        self.assertEqual(selected["source_artifact_outcome"], "V0_BODY_PASS_CONFIRMED")
        self.assertEqual(result["recognized_signal"]["signal_category"], "BODY_PASS_SIGNAL")
        self.assertNotEqual(
            selected["source_artifact_family"],
            "received_derivative_action_permission",
        )
        self.assertEqual(
            result["selected_candidate_signal"]["source_artifact_basis"][
                "source_artifact_family"
            ],
            "v0_body_pass_result",
        )

    def test_nested_incidental_family_does_not_override_selected_body_pass_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            body_pass_path = (
                temp_root
                / "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/body_pass.json"
            )
            artifact = body_pass_artifact()
            write_json(body_pass_path, artifact)
            source_path = body_pass_path.relative_to(temp_root).as_posix()
            source = body_pass_source_from_artifact(artifact, source_path)
            candidate = candidate_signal(
                source,
                category="BODY_PASS_SIGNAL",
                candidate_id="candidate-nested-body-pass-signal",
                source_path=source_path,
            )

            with mock.patch.object(recognition, "_repo_root", return_value=temp_root):
                result = recognition.resolve_body_signal_recognition_from_path(
                    body_pass_path,
                    candidate,
                )

        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
        self.assertEqual(
            result["selected_source_artifact"]["source_artifact_family"],
            "v0_body_pass_result",
        )
        self.assertTrue(
            check_by_name(
                result,
                "path_derived_selected_source_family_not_overridden_by_nested_incidental_fields",
            )["passed"]
        )
        self.assertTrue(
            check_by_name(
                result,
                "nested_derivative_action_receipt_surfaces_do_not_replace_selected_source_family",
            )["passed"]
        )

    def test_path_derived_family_mapping_for_key_live_roots(self) -> None:
        cases = (
            (
                "artifacts/integrity_host_v0_min_coexistence_v0_body_pass",
                "v0_body_pass_result",
                "BODY_PASS_SIGNAL",
                "V0_BODY_PASS_CONFIRMED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v3",
                "current_self_orientation_v3_result",
                "NON_CLAIM_SIGNAL",
                "SELF_ORIENTED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility",
                "current_self_orientation_reentry_admissibility_result",
                "REENTRY_ADMISSIBILITY_SIGNAL",
                "REENTRY_ADMITTED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt",
                "current_self_orientation_reentry_receipt_result",
                "REENTRY_RECEIPT_SIGNAL",
                "REENTRY_RECEIVED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_state_what_stands_now",
                "current_state_what_stands_now_result",
                "CURRENT_STATE_SIGNAL",
                "ANSWERED_WHAT_STANDS_NOW",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_state_what_remains_open",
                "current_state_what_remains_open_result",
                "OPEN_SURFACE_SIGNAL",
                "OPEN_SURFACE_RECOGNIZED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_state_query",
                "current_state_query_result",
                "CURRENT_STATE_SIGNAL",
                "ANSWERED_CURRENT_STATE_QUERY",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_current_state_touch_permissions",
                "current_state_touch_permission_result",
                "TOUCH_ADMISSIBILITY_SIGNAL",
                "TOUCH_PERMISSION_ADMITTED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_units",
                "continuity_transfer_unit_result",
                "CONTINUITY_TRANSFER_SIGNAL",
                "CONTINUITY_TRANSFERRED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_receipts",
                "continuity_transfer_receipt_result",
                "CONTINUITY_RECEIPT_SIGNAL",
                "CONTINUITY_RECEIPT_RECEIVED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_received_derivative_participation",
                "received_derivative_participation_result",
                "DERIVATIVE_PARTICIPATION_SIGNAL",
                "DERIVATIVE_PARTICIPATION_RECEIVED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_received_derivative_action_permissions",
                "received_derivative_action_permission_result",
                "DERIVATIVE_ACTION_PERMISSION_SIGNAL",
                "DERIVATIVE_ACTION_PERMISSION_RECEIVED",
            ),
            (
                "artifacts/integrity_host_v0_min_coexistence_continuity_memory_seam",
                "continuity_memory_seam_result",
                "MEMORY_SEAM_SIGNAL",
                "CONTINUITY_MEMORY_SEAM_CLOSED",
            ),
            (
                "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3",
                "openai_api_derivative_vessel_bounded_current_state_read_v3_result",
                "DERIVATIVE_VESSEL_SIGNAL",
                "DERIVATIVE_VESSEL_ANSWERED",
            ),
            (
                "artifacts/operator_facing_terminal_brief__bounded_current_state_read",
                "operator_terminal_brief_result",
                "OPERATOR_FACING_SIGNAL",
                "OPERATOR_TERMINAL_BRIEF_RENDERED",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(recognition, "_repo_root", return_value=temp_root):
                for root, expected_family, category, outcome in cases:
                    with self.subTest(root=root):
                        source_path = Path(root) / "source.json"
                        absolute_path = temp_root / source_path
                        source = source_artifact(
                            result_id=f"source-{expected_family}",
                            family="received_derivative_action_permission_result",
                            result_type="IAMMAI_SYNTHETIC_PATH_SOURCE_RESULT",
                            outcome=outcome,
                            path=source_path.as_posix(),
                        )
                        write_json(absolute_path, source)
                        candidate = candidate_signal(
                            source,
                            category=category,
                            candidate_id=f"candidate-{expected_family}",
                            source_path=source_path.as_posix(),
                            candidate_family=expected_family,
                        )
                        result = recognition.resolve_body_signal_recognition_from_path(
                            absolute_path,
                            candidate,
                        )

                        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
                        self.assertEqual(
                            result["selected_source_artifact"]["source_artifact_family"],
                            expected_family,
                        )
                        self.assertTrue(
                            check_by_name(
                                result,
                                "path_derived_selected_source_family_not_overridden_by_nested_incidental_fields",
                            )["passed"]
                        )

    def test_body_pass_correspondence_supports_only_body_pass_signal(self) -> None:
        source = category_source("BODY_PASS_SIGNAL")
        candidate = candidate_signal(source, category="BODY_PASS_SIGNAL")
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")

        wrong_candidate = candidate_signal(
            source,
            category="DERIVATIVE_ACTION_PERMISSION_SIGNAL",
        )
        wrong_result = recognition.resolve_body_signal_recognition(source, wrong_candidate)
        self.assert_block(wrong_result, "SIGNAL_CATEGORY_MISMATCHES_SOURCE")

    def test_summary_helper(self) -> None:
        result = self.recognized_result()
        summary = recognition.build_body_signal_recognition_summary(result)

        self.assertEqual(summary["outcome"], "SIGNAL_RECOGNIZED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["selected_source_artifact_id"],
            result["selected_source_artifact"]["source_artifact_id"],
        )
        self.assertEqual(summary["signal_category"], "CURRENT_STATE_SIGNAL")
        self.assertEqual(
            summary["recognized_signal_id"],
            result["recognized_signal"]["recognized_signal_id"],
        )
        self.assertEqual(summary["recognized_signal_category"], "CURRENT_STATE_SIGNAL")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["hierarchy_constraints_passed"])
        self.assertTrue(summary["correspondence_requirements_passed"])
        self.assertTrue(summary["non_claims_passed"])
        self.assertTrue(summary["path_source_family_preserved"])
        for key in REQUIRED_FALSE_RESULT_NON_CLAIMS:
            self.assertIn(key, summary["key_non_claims"])
            self.assertIs(summary["key_non_claims"][key], False)

    def test_write_behavior_explicit_path(self) -> None:
        result = self.recognized_result()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "result.json"
            returned = recognition.write_body_signal_recognition_result(
                result,
                output_path,
            )
            self.assertEqual(returned, output_path)
            self.assertTrue(returned.exists())
            written = read_json(returned)
            self.assertTrue(EXPECTED_RESULT_KEYS.issubset(written.keys()))
            with self.assertRaises(FileExistsError):
                recognition.write_body_signal_recognition_result(result, output_path)

    def test_default_output_path_behavior_uses_v2_root_and_bounded_suffix(self) -> None:
        result = self.recognized_result()
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(recognition, "_repo_root", return_value=temp_root):
                first = recognition.write_body_signal_recognition_result(result)
                second = recognition.write_body_signal_recognition_result(result)

        expected_root = temp_root / recognition.BODY_SIGNAL_RECOGNITION_V2_ROOT
        self.assertEqual(first.parent, expected_root)
        self.assertEqual(second.parent, expected_root)
        self.assertNotEqual(first, second)
        self.assertIn("_001", second.name)

    def test_blocks_no_source_artifact(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        result = recognition.resolve_body_signal_recognition(None, candidate)

        self.assert_block(result, "NO_SOURCE_ARTIFACT_BASIS")
        self.assertIsNone(result["selected_source_artifact"]["source_artifact_id"])
        self.assertEqual(result["selected_candidate_signal"], candidate)

    def test_blocks_missing_candidate_signal(self) -> None:
        result = recognition.resolve_body_signal_recognition(source_artifact(), None)

        self.assert_block(result, "CANDIDATE_SIGNAL_DECLARATION_MISSING")

    def test_blocks_malformed_candidate_declaration(self) -> None:
        result = recognition.resolve_body_signal_recognition(
            source_artifact(),
            {"candidate_signal_metadata": {}},
        )

        self.assert_block(result, "CANDIDATE_SIGNAL_DECLARATION_MALFORMED")

    def test_blocks_source_artifact_unreadable_or_malformed(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)

        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            missing_result = recognition.resolve_body_signal_recognition_from_path(
                missing,
                candidate,
            )
            self.assert_block(missing_result, "SOURCE_ARTIFACT_UNREADABLE")

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            malformed_result = recognition.resolve_body_signal_recognition_from_path(
                malformed,
                candidate_signal(source, source_path=malformed.as_posix()),
            )
            self.assert_block(malformed_result, "SOURCE_ARTIFACT_MALFORMED")

            array_path = Path(tmp) / "array.json"
            array_path.write_text("[]\n", encoding="utf-8")
            array_result = recognition.resolve_body_signal_recognition_from_path(
                array_path,
                candidate_signal(source, source_path=array_path.as_posix()),
            )
            self.assert_block(array_result, "SOURCE_ARTIFACT_MALFORMED")

    def test_blocks_source_outcome_missing(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        del source["outcome"]

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(result, "SOURCE_OUTCOME_MISSING")

    def test_blocks_unknown_signal_category(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        candidate["claimed_signal"]["signal_category"] = "NOT_A_SIGNAL"

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(result, "SIGNAL_CATEGORY_UNKNOWN")

    def test_blocks_category_source_mismatch(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source, category="REENTRY_RECEIPT_SIGNAL")

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(result, "SIGNAL_CATEGORY_MISMATCHES_SOURCE")

    def test_blocks_source_identity_not_preserved(self) -> None:
        source = source_artifact()

        cases = {
            "source id": ("source_artifact_id", "other-source"),
            "source path": ("source_artifact_path", "artifacts/synthetic/other.json"),
            "source family": ("source_artifact_family", "other_family"),
        }
        for label, (field, value) in cases.items():
            with self.subTest(label=label):
                candidate = candidate_signal(source)
                candidate["source_artifact_basis"][field] = value
                if field in {"source_artifact_path", "source_artifact_family"}:
                    candidate["carried_posture"][field] = value
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, "SOURCE_IDENTITY_NOT_PRESERVED")

    def test_blocks_source_outcome_not_preserved(self) -> None:
        source = source_artifact()

        candidate = candidate_signal(source)
        candidate["source_artifact_basis"]["source_artifact_outcome"] = "OTHER_OUTCOME"
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assert_block(result, "SOURCE_OUTCOME_NOT_PRESERVED")

        candidate = candidate_signal(source)
        candidate["carried_posture"]["source_outcome"] = "OTHER_OUTCOME"
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assert_block(result, "SOURCE_OUTCOME_NOT_PRESERVED")

    def test_blocks_hierarchy_constraint_flipped_or_omitted(self) -> None:
        source = source_artifact()
        for field, expected_code in HIERARCHY_FALSE_FIELDS.items():
            with self.subTest(field=field):
                candidate = candidate_signal(source)
                candidate["hierarchy_constraints"][field] = True
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, expected_code)

        candidate = candidate_signal(source)
        del candidate["hierarchy_constraints"]["signal_allowed_as_authority"]
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assert_block(result, "SIGNAL_ATTEMPTS_AUTHORITY")

    def test_blocks_correspondence_requirement_flipped(self) -> None:
        source = source_artifact()
        for field, expected_code in CORRESPONDENCE_TRUE_FIELDS.items():
            with self.subTest(field=field):
                candidate = candidate_signal(source)
                candidate["correspondence_requirements"][field] = False
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, expected_code)

    def test_blocks_declared_non_claim_missing_or_flipped(self) -> None:
        source = source_artifact()
        for field in DECLARED_NON_CLAIM_FIELDS:
            with self.subTest(field=field):
                candidate = candidate_signal(source)
                candidate["declared_non_claims"][field] = False
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, "NON_CLAIM_MISSING_OR_FLIPPED")

        candidate = candidate_signal(source)
        del candidate["declared_non_claims"]["does_not_create_authority"]
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assert_block(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_blocks_forbidden_workflow_roadmap_router_event_bus_and_radio_language(self) -> None:
        forbidden_phrases = (
            "workflow",
            "roadmap",
            "router",
            "event bus",
            "regulation",
            "autonomy",
            "RADIO 22",
        )
        source = source_artifact()
        for phrase in forbidden_phrases:
            with self.subTest(phrase=phrase):
                candidate = candidate_signal(source)
                candidate["claimed_signal"]["claimed_signal_reason"] = phrase
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, "SIGNAL_BECOMES_WORKFLOW_ROADMAP_OR_ROUTER")

    def test_blocks_latest_file_recency_language(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        candidate["claimed_signal"]["claimed_signal_reason"] = (
            "selected by latest-file recency"
        )

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(result, "LATEST_FILE_RECENCY_REFUSED")

    def test_blocks_reusable_receipt_permission_language(self) -> None:
        source = category_source("REENTRY_RECEIPT_SIGNAL")
        candidate = candidate_signal(
            source,
            category="REENTRY_RECEIPT_SIGNAL",
            candidate_id="candidate-reentry-receipt-signal",
        )
        candidate["claimed_signal"]["claimed_signal_reason"] = (
            "receipt means continue as a reusable permission token"
        )

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(result, "REENTRY_RECEIPT_TREATED_AS_REUSABLE_PERMISSION")

    def test_category_specific_valid_pairs_are_recognized(self) -> None:
        categories = (
            "CURRENT_STATE_SIGNAL",
            "OPEN_SURFACE_SIGNAL",
            "BLOCKED_REFUSED_SIGNAL",
            "TOUCH_ADMISSIBILITY_SIGNAL",
            "CONTINUITY_TRANSFER_SIGNAL",
            "CONTINUITY_RECEIPT_SIGNAL",
            "DERIVATIVE_PARTICIPATION_SIGNAL",
            "DERIVATIVE_ACTION_PERMISSION_SIGNAL",
            "MEMORY_SEAM_SIGNAL",
            "BODY_PASS_SIGNAL",
            "DERIVATIVE_VESSEL_SIGNAL",
            "OPERATOR_FACING_SIGNAL",
            "REENTRY_ADMISSIBILITY_SIGNAL",
            "REENTRY_RECEIPT_SIGNAL",
            "EXHAUSTION_CLOSURE_SIGNAL",
            "NON_CLAIM_SIGNAL",
        )
        for category in categories:
            with self.subTest(category=category):
                source = category_source(category)
                candidate = candidate_signal(
                    source,
                    category=category,
                    candidate_id=f"candidate-{category.lower()}",
                )
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assertEqual(result["outcome"], "SIGNAL_RECOGNIZED")
                self.assertEqual(result["recognized_signal"]["signal_category"], category)
                self.assertEqual(
                    result["body_signal_recognition_summary"]["failed_check_count"],
                    0,
                )

    def test_category_specific_omitted_posture_blocks(self) -> None:
        omission_cases = (
            ("OPEN_SURFACE_SIGNAL", "open_status", "RELEVANT_POSTURE_OMITTED"),
            (
                "BLOCKED_REFUSED_SIGNAL",
                "blocked_refused_status",
                "BLOCKED_REFUSED_POSTURE_HIDDEN",
            ),
            ("REENTRY_RECEIPT_SIGNAL", "receipt_status", "RECEIPT_POSTURE_OMITTED"),
            (
                "EXHAUSTION_CLOSURE_SIGNAL",
                "exhaustion_status",
                "EXHAUSTION_POSTURE_OMITTED",
            ),
            ("DERIVATIVE_VESSEL_SIGNAL", "derivative_status", "RELEVANT_POSTURE_OMITTED"),
            ("OPERATOR_FACING_SIGNAL", "operator_facing_status", "RELEVANT_POSTURE_OMITTED"),
        )
        for category, carried_field, expected_code in omission_cases:
            with self.subTest(category=category):
                source = category_source(category)
                candidate = candidate_signal(source, category=category)
                candidate["carried_posture"].pop(carried_field, None)
                result = recognition.resolve_body_signal_recognition(source, candidate)
                self.assert_block(result, expected_code)

        source = source_artifact(
            family="current_state_what_stands_now_result",
            result_type="IAMMAI_SYNTHETIC_NON_CLAIM_BEARING_RESULT",
            include_non_claims=False,
        )
        candidate = candidate_signal(source, category="NON_CLAIM_SIGNAL")
        candidate["carried_posture"].pop("non_claims", None)
        result = recognition.resolve_body_signal_recognition(source, candidate)
        self.assert_block(
            result,
            {"SIGNAL_CATEGORY_MISMATCHES_SOURCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_downstream_source_cannot_claim_current_basis_signal(self) -> None:
        source = category_source("DERIVATIVE_VESSEL_SIGNAL")
        candidate = candidate_signal(source, category="CURRENT_BASIS_SIGNAL")

        result = recognition.resolve_body_signal_recognition(source, candidate)

        self.assert_block(
            result,
            {
                "SIGNAL_CATEGORY_MISMATCHES_SOURCE",
                "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
            },
        )

    def test_result_non_claims_for_recognized_and_blocked_results(self) -> None:
        recognized = self.recognized_result()
        blocked = recognition.resolve_body_signal_recognition(source_artifact(), None)

        self.assert_result_non_claims_false(recognized)
        self.assert_result_non_claims_false(blocked)

    def test_non_mutation_posture(self) -> None:
        source = source_artifact()
        candidate = candidate_signal(source)
        source_before = copy.deepcopy(source)
        candidate_before = copy.deepcopy(candidate)

        first = recognition.resolve_body_signal_recognition(source, candidate)
        second = recognition.resolve_body_signal_recognition(source, candidate)

        self.assertEqual(source, source_before)
        self.assertEqual(candidate, candidate_before)
        self.assertEqual(first["outcome"], "SIGNAL_RECOGNIZED")
        self.assertEqual(second["outcome"], "SIGNAL_RECOGNIZED")

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "additive" / "result.json"
            recognition.write_body_signal_recognition_result(first, output_path)

        self.assertEqual(source, source_before)
        self.assertEqual(candidate, candidate_before)


if __name__ == "__main__":
    unittest.main()
