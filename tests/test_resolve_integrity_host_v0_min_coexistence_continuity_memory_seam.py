"""Bounded tests for the v0-min continuity-memory seam resolver.

This suite exercises the closure seam implemented in
``resolve_integrity_host_v0_min_coexistence_continuity_memory_seam``. It builds
real local upstream artifacts through received-derivative action permission,
then verifies that seam closure remains additive, lineage-preserving, and
explicitly anti-collapse. It does not test replay, merge, registry,
persistence, final governance, or continuity-completion behavior.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
TESTS_ROOT = REPO_ROOT / "tests"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(TESTS_ROOT) not in sys.path:
    sys.path.insert(0, str(TESTS_ROOT))


import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_builder
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer
import resolve_current_integrity_host_v0_min_coexistence_effective_family as effective_resolver
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as authority_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_application as application_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_delivery as delivery_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_export as export_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_handoff as handoff_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_readout as readout_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_current_work_input as work_input_resolver
import resolve_integrity_host_v0_min_coexistence_current_work_operation_v2 as operation_resolver
import resolve_integrity_host_v0_min_coexistence_effective_family_consumption as consumption_resolver
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner
import test_resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_harness


TOP_LEVEL = {
    "continuity_memory_seam_metadata",
    "selected_action_permission_result",
    "selected_participation_result",
    "selected_receipt_result",
    "selected_transfer_result",
    "selected_source_surface",
    "closure_posture",
    "checks",
    "outcome",
    "block",
    "continuity_memory_seam_summary",
    "non_claims",
}

REQUIRED_CONTEXT_PATHS = (
    *action_harness.REQUIRED_CONTEXT_PATHS,
    "spec/CONTINUITY_MEMORY_SEAM_V0_CLOSURE_SPEC.md",
    "src/resolve_integrity_host_v0_min_coexistence_continuity_memory_seam.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission.py",
)


def read_json(path: Path | str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object at {path}")
    return value


def write_json(path: Path | str, value: Mapping[str, Any]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
    return target


def copied(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def tree_digest(root: Path) -> dict[str, str]:
    digests: dict[str, str] = {}
    if not root.exists():
        return digests
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digests[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


class ContinuityMemorySeamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        for relative_path in REQUIRED_CONTEXT_PATHS:
            path = REPO_ROOT / relative_path
            if not path.is_file():
                raise AssertionError(f"required context file is missing: {relative_path}")
            path.read_text(encoding="utf-8")

    def build_stack(self, temp_root: Path) -> dict[str, Any]:
        helper = action_harness.ReceivedDerivativeActionPermissionTests(
            methodName="run",
        )
        stack = helper.build_stack(temp_root)

        transfer_path = temp_root / "artifacts" / "seam_lineage" / "transfer.json"
        with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
            transfer = transfer_resolver.resolve_continuity_transfer_unit_from_path(
                stack["open_path"],
                helper.transfer_request(
                    transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                    action_harness.DERIVATIVE_FIELDS,
                ),
                stack["derivation_touch_path"],
            )
            written_transfer_path = transfer_resolver.write_continuity_transfer_unit_result(
                transfer,
                transfer_path,
            )
        self.assertEqual(transfer_resolver.OUTCOME_TRANSFERRED, transfer["outcome"])

        receipt_path = temp_root / "artifacts" / "seam_lineage" / "receipt.json"
        with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
            receipt = receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                written_transfer_path,
                helper.receipt_request(
                    receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
                    action_harness.DERIVATIVE_FIELDS,
                    basis="bounded acceptance for continuity-memory seam tests",
                ),
            )
            written_receipt_path = receipt_resolver.write_continuity_transfer_receipt_result(
                receipt,
                receipt_path,
            )
        self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, receipt["outcome"])

        participation_path = (
            temp_root / "artifacts" / "seam_lineage" / "participation.json"
        )
        with mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
            participation = (
                participation_resolver.resolve_received_derivative_participation_from_path(
                    written_receipt_path,
                    helper.participation_request(
                        participation_resolver.PARTICIPANT_CLASS_LOCAL_DERIVATION,
                        participation_resolver.USE_CLASS_DERIVATIVE,
                        action_harness.DERIVATIVE_FIELDS,
                        basis="bounded derivative participation for continuity-memory seam",
                    ),
                )
            )
            written_participation_path = (
                participation_resolver.write_received_derivative_participation_result(
                    participation,
                    participation_path,
                )
            )
        self.assertEqual(
            participation_resolver.OUTCOME_PARTICIPATED,
            participation["outcome"],
        )

        action_path = temp_root / "artifacts" / "seam_lineage" / "action.json"
        with mock.patch.object(action_resolver, "_repo_root", return_value=temp_root):
            action = action_resolver.resolve_received_derivative_action_permission_from_path(
                written_participation_path,
                helper.action_request(),
            )
            written_action_path = (
                action_resolver.write_received_derivative_action_permission_result(
                    action,
                    action_path,
                )
            )
        self.assertEqual(action_resolver.OUTCOME_ACTION_PERMITTED, action["outcome"])
        stack["derivative_transfer"] = transfer
        stack["derivative_transfer_path"] = written_transfer_path
        stack["derivative_receipt"] = receipt
        stack["derivative_receipt_path"] = written_receipt_path
        stack["derivative_participation"] = participation
        stack["derivative_participation_path"] = written_participation_path
        stack["action_permission"] = action
        stack["action_permission_path"] = written_action_path
        return stack

    def resolve_seam(
        self,
        temp_root: Path,
        action_permission: Mapping[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
            return seam_resolver.resolve_continuity_memory_seam(action_permission)

    def assert_top_level(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(TOP_LEVEL, set(result))

    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assert_top_level(result)
        self.assertEqual(seam_resolver.OUTCOME_BLOCKED, result["outcome"])
        self.assertIsInstance(result["block"], dict)
        self.assertEqual(code, result["block"]["block_code"])
        self.assertIsInstance(result["block"]["block_reason"], str)
        self.assertTrue(result["block"]["block_reason"])

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        required_false = {
            "replayed_into_live_host",
            "merged_into_local_state",
            "continuity_completed",
            "standing_upgraded",
            "source_replaced",
            "overwrite_style_correction",
            "latest_file_currentness",
            "recency_fraud",
            "standing_memory_collapsed_with_interpretation",
            "final_continuity_memory_seam_completed",
        }
        self.assertTrue(required_false.issubset(non_claims))
        for claim_name, value in non_claims.items():
            if isinstance(value, bool):
                self.assertFalse(value, claim_name)

    def assert_seam_closed(self, result: Mapping[str, Any]) -> None:
        self.assert_top_level(result)
        self.assertEqual(seam_resolver.OUTCOME_SEAM_CLOSED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assert_non_claims_false(result)
        posture = result["closure_posture"]
        self.assertIsInstance(posture, dict)
        for key in (
            "preserved_lineage_without_overwrite",
            "correction_by_successor_not_edit",
            "currentness_without_recency_fraud",
            "derivative_carry_without_source_collapse",
            "standing_memory_distinct_from_interpretation_surfaces",
        ):
            self.assertIs(posture.get(key), True, key)
        checks = result["checks"]
        self.assertIsInstance(checks, list)
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertIsInstance(check.get("check_name"), str)
            self.assertIsInstance(check.get("passed"), bool)
        self.assertTrue(all(check["passed"] for check in checks))

    def test_closes_real_seam_and_preserves_metadata_lineage_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            result = self.resolve_seam(temp_root, stack["action_permission"])
            self.assert_seam_closed(result)

            metadata = result["continuity_memory_seam_metadata"]
            for key in (
                "continuity_memory_seam_result_id",
                "continuity_memory_seam_result_type",
                "continuity_memory_seam_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assertIsInstance(metadata.get(key), str)
                self.assertTrue(metadata[key])

            selected_action = result["selected_action_permission_result"]
            action_metadata = stack["action_permission"][
                "received_derivative_action_permission_metadata"
            ]
            self.assertEqual(
                action_metadata["received_derivative_action_permission_result_id"],
                selected_action["selected_action_permission_result_id"],
            )
            self.assertEqual(
                action_metadata["received_derivative_action_permission_result_type"],
                selected_action["selected_action_permission_result_type"],
            )
            self.assertEqual(
                action_resolver.OUTCOME_ACTION_PERMITTED,
                selected_action["selected_action_permission_result_outcome"],
            )
            self.assertEqual(
                action_resolver.ACTOR_CLASS_LOCAL_EMISSION,
                selected_action["actor_class"],
            )
            self.assertEqual(
                action_resolver.ACTION_CLASS_DERIVATIVE_EMISSION,
                selected_action["action_class"],
            )
            self.assertTrue(selected_action["action_basis"])

            selected_participation = result["selected_participation_result"]
            selected_receipt = result["selected_receipt_result"]
            selected_transfer = result["selected_transfer_result"]
            selected_source = result["selected_source_surface"]
            self.assertEqual(
                stack["derivative_participation"][
                    "received_derivative_participation_metadata"
                ]["received_derivative_participation_result_id"],
                selected_participation["selected_participation_result_id"],
            )
            self.assertTrue(selected_participation["selected_participation_result_path"])
            self.assertEqual(
                stack["derivative_receipt"]["continuity_transfer_receipt_metadata"][
                    "continuity_transfer_receipt_result_id"
                ],
                selected_receipt["selected_receipt_result_id"],
            )
            self.assertTrue(selected_receipt["selected_receipt_result_path"])
            self.assertEqual(
                stack["derivative_transfer"]["continuity_transfer_metadata"][
                    "continuity_transfer_result_id"
                ],
                selected_transfer["selected_transfer_result_id"],
            )
            self.assertTrue(selected_transfer["selected_transfer_result_path"])
            self.assertEqual(
                stack["open"]["what_remains_open_metadata"][
                    "what_remains_open_result_id"
                ],
                selected_source["selected_source_surface_id"],
            )
            self.assertTrue(selected_source["selected_source_surface_path"])
            self.assertEqual(
                "what_remains_open",
                selected_source["selected_source_surface_family"],
            )
            self.assertEqual(
                open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                selected_source["selected_source_surface_outcome"],
            )
            self.assertIsInstance(
                selected_source["selected_source_surface_effective_references"],
                dict,
            )

            check_names = {check["check_name"] for check in result["checks"]}
            self.assertIn(
                "lineage_reference_artifacts_correspond_to_selected_identities",
                check_names,
            )
            self.assertIn("rank_currentness_is_explicit", check_names)
            self.assertIn("successor_relation_posture_is_explicit", check_names)
            self.assertIn(
                "standing_memory_is_distinct_from_interpretation_and_action_surfaces",
                check_names,
            )
            self.assertIn("seam_does_not_use_latest_file_inference", check_names)
            self.assertIn("seam_does_not_use_overwrite_style_correction", check_names)

            summary = seam_resolver.build_continuity_memory_seam_summary(result)
            self.assertEqual(seam_resolver.OUTCOME_SEAM_CLOSED, summary["outcome"])
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(
                selected_action["selected_action_permission_result_id"],
                summary["selected_action_permission_result_id"],
            )
            self.assertEqual(
                selected_participation["selected_participation_result_id"],
                summary["selected_participation_result_id"],
            )
            self.assertEqual(
                selected_receipt["selected_receipt_result_id"],
                summary["selected_receipt_result_id"],
            )
            self.assertEqual(
                selected_transfer["selected_transfer_result_id"],
                summary["selected_transfer_result_id"],
            )
            self.assertEqual(
                selected_source["selected_source_surface_id"],
                summary["selected_source_surface_id"],
            )
            self.assertEqual(0, summary["failed_check_count"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(result["closure_posture"], summary["closure_posture"])
            self.assertIsInstance(summary["key_non_claims"], dict)

    def test_explicit_path_resolution_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            direct = self.resolve_seam(temp_root, stack["action_permission"])
            with mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                from_path = seam_resolver.resolve_continuity_memory_seam_from_path(
                    stack["action_permission_path"],
                )
            self.assert_seam_closed(direct)
            self.assert_seam_closed(from_path)
            self.assertEqual(
                direct["selected_action_permission_result"][
                    "selected_action_permission_result_id"
                ],
                from_path["selected_action_permission_result"][
                    "selected_action_permission_result_id"
                ],
            )
            self.assertEqual(
                "provided_mapping",
                direct["selected_action_permission_result"][
                    "selected_action_permission_result_path"
                ],
            )
            self.assertNotEqual(
                direct["selected_action_permission_result"][
                    "selected_action_permission_result_path"
                ],
                from_path["selected_action_permission_result"][
                    "selected_action_permission_result_path"
                ],
            )

            explicit_path = temp_root / "written" / "nested" / "seam.json"
            written = seam_resolver.write_continuity_memory_seam_result(
                from_path,
                explicit_path,
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.is_file())
            self.assertEqual(TOP_LEVEL, set(read_json(written)))
            with self.assertRaises(FileExistsError):
                seam_resolver.write_continuity_memory_seam_result(
                    from_path,
                    explicit_path,
                )

            default_root = temp_root / "default_seam"
            with mock.patch.object(
                seam_resolver,
                "CONTINUITY_MEMORY_SEAM_ROOT",
                Path("default_seam"),
            ), mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                first = seam_resolver.write_continuity_memory_seam_result(from_path)
                second = seam_resolver.write_continuity_memory_seam_result(from_path)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertEqual(default_root, first.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__continuity_memory_seam_result.json"))
            self.assertIn("_001", second.stem)

    def test_blocks_no_admissible_non_permitted_and_out_of_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(
                seam_resolver,
                "RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT",
                Path("missing_actions"),
            ), mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                no_action = seam_resolver.resolve_continuity_memory_seam()
            self.assert_block(no_action, "NO_ADMISSIBLE_ACTION_PERMISSION_RESULT")

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            blocked = copied(stack["action_permission"])
            blocked["outcome"] = action_resolver.OUTCOME_REFUSED
            self.assert_block(
                self.resolve_seam(temp_root, blocked),
                "SELECTED_ACTION_PERMISSION_RESULT_BLOCKED",
            )

            pending = copied(stack["action_permission"])
            pending["outcome"] = "PENDING"
            self.assert_block(
                self.resolve_seam(temp_root, pending),
                "SELECTED_ACTION_PERMISSION_RESULT_NOT_PERMITTED",
            )

            self.assert_block(
                self.resolve_seam(
                    temp_root,
                    {"outcome": action_resolver.OUTCOME_ACTION_PERMITTED},
                ),
                "SELECTED_ACTION_PERMISSION_RESULT_OUT_OF_SCOPE",
            )

            action_root = temp_root / "actions"
            refused = copied(stack["action_permission"])
            refused["outcome"] = action_resolver.OUTCOME_REFUSED
            write_json(action_root / "refused.json", refused)
            with mock.patch.object(
                seam_resolver,
                "RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT",
                Path("actions"),
            ), mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                no_eligible = seam_resolver.resolve_continuity_memory_seam()
            self.assert_block(no_eligible, "NO_ADMISSIBLE_ACTION_PERMISSION_RESULT")

    def test_blocks_shortcuts_invariants_and_lineage_misuse(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            latest = copied(stack["action_permission"])
            latest["action_permission_request"]["action_basis"] = (
                "use latest file inference for closure"
            )
            self.assert_block(
                self.resolve_seam(temp_root, latest),
                "LATEST_FILE_INFERENCE_REFUSED",
            )

            recency = copied(stack["action_permission"])
            recency["action_permission_request"]["action_basis"] = "newest file wins"
            self.assert_block(
                self.resolve_seam(temp_root, recency),
                "RECENCY_FRAUD_REFUSED",
            )

            overwrite = copied(stack["action_permission"])
            overwrite["action_permission_request"]["action_basis"] = (
                "overwrite the prior preserved surface"
            )
            self.assert_block(
                self.resolve_seam(temp_root, overwrite),
                "OVERWRITE_STYLE_CORRECTION_REFUSED",
            )

            stale = copied(stack["action_permission"])
            stale["action_permission_request"]["action_basis"] = (
                "use stale prior-family fallback"
            )
            self.assert_block(
                self.resolve_seam(temp_root, stale),
                "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
            )

            source_replacement = copied(stack["action_permission"])
            source_replacement["non_claims"]["source_replaced"] = True
            self.assert_block(
                self.resolve_seam(temp_root, source_replacement),
                "SOURCE_REPLACEMENT_REFUSED",
            )

            collapsed_payload = copied(stack["action_permission"])
            collapsed_payload["action_permission_payload"]["source_remains_source"] = False
            self.assert_block(
                self.resolve_seam(temp_root, collapsed_payload),
                "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
            )

            collapsed_memory = copied(stack["action_permission"])
            collapsed_memory["non_claims"][
                "standing_memory_collapsed_with_interpretation"
            ] = True
            self.assert_block(
                self.resolve_seam(temp_root, collapsed_memory),
                "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
            )

            missing_lineage = copied(stack["action_permission"])
            missing_lineage["selected_participation_result"][
                "selected_participation_result_id"
            ] = ""
            self.assert_block(
                self.resolve_seam(temp_root, missing_lineage),
                "LINEAGE_REFERENCE_MISSING",
            )

    def test_hard_malformed_failures(self) -> None:
        with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
            seam_resolver.resolve_continuity_memory_seam("not a mapping")  # type: ignore[arg-type]

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            malformed_action = {
                "received_derivative_action_permission_metadata": {
                    "received_derivative_action_permission_result_id": "x",
                    "received_derivative_action_permission_result_type": "type",
                    "received_derivative_action_permission_result_version": "0",
                },
                "outcome": action_resolver.OUTCOME_ACTION_PERMITTED,
            }
            with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
                self.resolve_seam(temp_root, malformed_action)

            malformed_path = temp_root / "bad" / "action.json"
            malformed_path.parent.mkdir(parents=True, exist_ok=True)
            malformed_path.write_text("{not-json", encoding="utf-8")
            with mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
                    seam_resolver.resolve_continuity_memory_seam_from_path(
                        malformed_path,
                    )

            bad_lineage = copied(stack["action_permission"])
            bad_participation_path = temp_root / "bad" / "participation.json"
            bad_participation_path.write_text("{not-json", encoding="utf-8")
            bad_lineage["selected_participation_result"][
                "selected_participation_result_path"
            ] = str(bad_participation_path)
            with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
                self.resolve_seam(temp_root, bad_lineage)

            bad_effective = copied(stack["action_permission"])
            bad_effective["selected_source_surface"][
                "selected_source_surface_effective_references"
            ]["effective_status_packet_path"] = 123
            with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
                self.resolve_seam(temp_root, bad_effective)

            root_file = temp_root / "action_root_file"
            root_file.write_text("not a directory", encoding="utf-8")
            with mock.patch.object(
                seam_resolver,
                "RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT",
                Path("action_root_file"),
            ), mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(seam_resolver.ContinuityMemorySeamError):
                    seam_resolver.resolve_continuity_memory_seam()

    def test_multiple_closure_tip_conflict_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            action_root = temp_root / "actions"
            first = copied(stack["action_permission"])
            second = copied(stack["action_permission"])
            second["action_permission_request"]["action_class"] = (
                action_resolver.ACTION_CLASS_BOUNDED_SURFACE_INVOCATION
            )
            write_json(action_root / "a.json", first)
            write_json(action_root / "b.json", second)
            with mock.patch.object(
                seam_resolver,
                "RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT",
                Path("actions"),
            ), mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
                conflict = seam_resolver.resolve_continuity_memory_seam()
            self.assert_block(
                conflict,
                "MULTIPLE_CLOSURE_TIPS_CONFLICT_UNRESOLVED",
            )

            before_tree = tree_digest(temp_root)
            before_action = copied(stack["action_permission"])
            first_result = self.resolve_seam(temp_root, stack["action_permission"])
            second_result = self.resolve_seam(temp_root, stack["action_permission"])
            self.assert_seam_closed(first_result)
            self.assert_seam_closed(second_result)
            self.assertEqual(before_tree, tree_digest(temp_root))
            self.assertEqual(before_action, stack["action_permission"])


if __name__ == "__main__":
    unittest.main()
