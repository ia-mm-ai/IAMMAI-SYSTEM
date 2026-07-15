"""Bounded tests for the v0-min coexistence governing-transition resolver.

These tests lock the current additive transition surface in
``src/resolve_integrity_host_v0_min_coexistence_governing_transition.py``
using real source scenario runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, run-family packets,
preserved-run status packets, and current-governing packets emitted into
temporary roots.

They verify accepted and refused proposal results, proposal/result identity,
explicit checks, non-claims, write behavior, hard malformed input failures, and
read-only behavior. They do not test replay, merge, persistence architecture,
registry integration, distributed continuity, CLI behavior, or broad
governance frameworks.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder  # noqa: E402
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "result_metadata",
    "proposal",
    "current_governing_before",
    "candidate_successor",
    "current_governing_after",
    "outcome",
    "refusal",
    "checks",
    "non_claims",
}

EXPECTED_PROPOSAL_FIELDS = {
    "transition_proposal_id",
    "current_governing_source_run_path",
    "candidate_successor_source_run_path",
    "current_governing_ingress_run_path",
    "candidate_successor_ingress_run_path",
    "current_governing_comparison_artifact_path",
    "candidate_successor_comparison_artifact_path",
    "proposal_basis_ref",
    "proposed_at",
    "proposed_by_surface",
}

EXPECTED_NON_CLAIMS = {
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
    "minimum_lawful_system_completed",
    "final_system_identity_completed",
    "final_preserved_run_governance_completed",
    "final_governing_scope_completed",
    "final_governing_transition_law_completed",
}


class IntegrityHostV0MinCoexistenceGoverningTransitionTests(unittest.TestCase):
    def emit_source_run(
        self,
        temp_root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, dict[str, Any]]:
        source_root = temp_root / resolver.SOURCE_RUNS_ROOT
        run_dir = source_root / run_name
        run_dir.mkdir(parents=True, exist_ok=True)
        with mock.patch.object(scenario_runner, "_repo_root", return_value=temp_root):
            emitted = tuple(
                scenario_runner._emit_scenario(run_dir, stem, scenario_function)
                for stem, scenario_function in scenario_runner.SCENARIOS
            )
            manifest = scenario_runner._build_manifest(run_dir, emitted)
            (run_dir / "manifest.json").write_text(
                scenario_runner.snapshot_to_json(manifest),
                encoding="utf-8",
            )
        return run_dir, manifest

    def emit_ingress_run(
        self,
        temp_root: Path,
        source_run_dir: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
            manifest = ingress_runner.run_receiving_ingress_for_source_run(
                source_run_dir
            )
            output_dir = self.resolve_display_path(
                temp_root,
                manifest["ingress_run_metadata"]["output_run_directory"],
            )
            ingress_runner.write_ingress_run_manifest(
                manifest,
                output_dir / "manifest.json",
            )
        return output_dir, manifest

    def emit_comparison_artifact(
        self,
        temp_root: Path,
        source_run_dir: Path,
        ingress_run_dir: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
            comparison = comparer.compare_source_run_and_ingress_run(
                source_run_dir,
                ingress_run_dir,
            )
            output_path = (
                temp_root
                / resolver.SOURCE_INGRESS_COMPARISON_ROOT
                / f"{source_run_dir.name}__source_ingress_comparison.json"
            )
            comparer.write_comparison(comparison, output_path)
        return output_path, comparison

    def emit_authority_resolution(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
            resolution = resolver.resolve_current_execution_authority()
            output_path = resolver.write_resolution(resolution)
        return output_path, resolution

    def emit_family_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
            packet = family_builder.build_run_family_packet()
            output_path = family_builder.write_run_family_packet(packet)
        return output_path, packet

    def emit_status_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
            packet = status_builder.build_preserved_run_status_packet()
            output_path = status_builder.write_preserved_run_status_packet(packet)
        return output_path, packet

    def emit_governing_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
            packet = governing_builder.build_current_governing_packet()
            output_path = governing_builder.write_current_governing_packet(packet)
        return output_path, packet

    def build_multi_run_stack(self, temp_root: Path) -> dict[str, Any]:
        first_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000000_000000Z",
        )
        first_ingress_run, _ = self.emit_ingress_run(temp_root, first_source_run)
        first_comparison_path, _ = self.emit_comparison_artifact(
            temp_root,
            first_source_run,
            first_ingress_run,
        )

        latest_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000001_000000Z",
        )
        latest_ingress_run, _ = self.emit_ingress_run(temp_root, latest_source_run)
        latest_comparison_path, _ = self.emit_comparison_artifact(
            temp_root,
            latest_source_run,
            latest_ingress_run,
        )

        authority_path, authority = self.emit_authority_resolution(temp_root)
        family_path, family = self.emit_family_packet(temp_root)
        status_path, status = self.emit_status_packet(temp_root)
        governing_path, governing = self.emit_governing_packet(temp_root)

        current_entry = governing["current_governing_run"]
        candidates = [
            entry
            for entry in status["preserved_run_status_entries"]
            if entry["status_role"] == status_builder.ROLE_ELIGIBLE_NON_AUTHORITY
        ]
        self.assertEqual(len(candidates), 1)

        return {
            "first_source_run": first_source_run,
            "first_ingress_run": first_ingress_run,
            "first_comparison_path": first_comparison_path,
            "latest_source_run": latest_source_run,
            "latest_ingress_run": latest_ingress_run,
            "latest_comparison_path": latest_comparison_path,
            "authority_path": authority_path,
            "authority": authority,
            "family_path": family_path,
            "family": family,
            "status_path": status_path,
            "status": status,
            "governing_path": governing_path,
            "governing": governing,
            "current_entry": current_entry,
            "candidate_entry": candidates[0],
        }

    def valid_proposal(
        self,
        stack: dict[str, Any],
        proposal_id: str = "proposal_accepted",
        proposal_basis_ref: str = "bounded explicit transition test basis",
        proposed_by_surface: str = (
            "tests/test_resolve_integrity_host_v0_min_coexistence_governing_transition.py"
        ),
    ) -> dict[str, str]:
        current = stack["current_entry"]
        candidate = stack["candidate_entry"]
        return {
            "transition_proposal_id": proposal_id,
            "current_governing_source_run_path": current[
                "source_run_directory_path"
            ],
            "candidate_successor_source_run_path": candidate[
                "source_run_directory_path"
            ],
            "current_governing_ingress_run_path": current[
                "matched_ingress_run_path"
            ],
            "candidate_successor_ingress_run_path": candidate[
                "matched_ingress_run_path"
            ],
            "current_governing_comparison_artifact_path": current[
                "matched_comparison_artifact_path"
            ],
            "candidate_successor_comparison_artifact_path": candidate[
                "matched_comparison_artifact_path"
            ],
            "proposal_basis_ref": proposal_basis_ref,
            "proposed_at": "2026-04-21T00:00:00Z",
            "proposed_by_surface": proposed_by_surface,
        }

    def current_as_candidate_proposal(
        self,
        stack: dict[str, Any],
    ) -> dict[str, str]:
        proposal = self.valid_proposal(
            stack,
            proposal_id="proposal_candidate_already_current",
        )
        current = stack["current_entry"]
        proposal["candidate_successor_source_run_path"] = current[
            "source_run_directory_path"
        ]
        proposal["candidate_successor_ingress_run_path"] = current[
            "matched_ingress_run_path"
        ]
        proposal["candidate_successor_comparison_artifact_path"] = current[
            "matched_comparison_artifact_path"
        ]
        return proposal

    def resolve_transition(
        self,
        temp_root: Path,
        proposal: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            return transition_resolver.resolve_governing_transition(proposal)

    def resolve_transition_from_path(
        self,
        temp_root: Path,
        proposal_path: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            return transition_resolver.resolve_governing_transition_from_path(
                proposal_path
            )

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

    def write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        return path

    def resolve_display_path(self, repo_root: Path, value: str) -> Path:
        path = Path(value)
        if path.is_absolute():
            return path.resolve()
        return (repo_root / path).resolve()

    def json_texts(self, root: Path) -> dict[str, str]:
        return {
            str(path.relative_to(root)): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*.json"))
        }

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_result_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(result["result_metadata"], dict)
        self.assertIsInstance(result["proposal"], dict)
        self.assertIsInstance(result["current_governing_before"], dict)
        self.assertIsInstance(result["candidate_successor"], dict)
        self.assertIsInstance(result["current_governing_after"], dict)
        self.assertIsInstance(result["refusal"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_refused_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], transition_resolver.OUTCOME_REFUSED)
        self.assert_non_empty_string(result["refusal"]["refusal_code"])
        self.assert_non_empty_string(result["refusal"]["refusal_reason"])
        self.assertIsNone(result["current_governing_after"]["source_run_path"])
        self.assertIsNone(result["current_governing_after"]["ingress_run_path"])
        self.assertIsNone(
            result["current_governing_after"]["comparison_artifact_path"]
        )
        self.assert_non_claims_false(result)

    def test_real_accepted_transition_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)

            result = self.resolve_transition(temp_root, proposal)

            self.assert_result_shape(result)
            self.assertEqual(result["outcome"], transition_resolver.OUTCOME_ACCEPTED)
            self.assertIsNone(result["refusal"]["refusal_code"])
            self.assertIsNone(result["refusal"]["refusal_reason"])
            self.assertEqual(
                result["current_governing_before"]["source_run_path"],
                proposal["current_governing_source_run_path"],
            )
            self.assertEqual(
                result["candidate_successor"]["source_run_path"],
                proposal["candidate_successor_source_run_path"],
            )
            self.assertEqual(
                result["current_governing_after"]["source_run_path"],
                proposal["candidate_successor_source_run_path"],
            )
            self.assertEqual(
                result["current_governing_after"]["ingress_run_path"],
                proposal["candidate_successor_ingress_run_path"],
            )
            self.assertEqual(
                result["current_governing_after"]["comparison_artifact_path"],
                proposal["candidate_successor_comparison_artifact_path"],
            )
            self.assert_non_claims_false(result)

    def test_resolution_from_proposal_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack, proposal_id="proposal_from_path")
            proposal_path = self.write_json(temp_root / "proposal.json", proposal)

            result = self.resolve_transition_from_path(temp_root, proposal_path)

            self.assert_result_shape(result)
            self.assertEqual(result["outcome"], transition_resolver.OUTCOME_ACCEPTED)
            self.assertEqual(result["proposal"], proposal)
            self.assertEqual(
                result["current_governing_after"]["source_run_path"],
                proposal["candidate_successor_source_run_path"],
            )

    def test_metadata_and_proposal_echo(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)
            result = self.resolve_transition(temp_root, proposal)

            metadata = result["result_metadata"]
            for key in (
                "transition_result_id",
                "transition_result_type",
                "transition_result_version",
                "generated_at",
                "resolver_module",
                "result_basis_ref",
            ):
                self.assert_non_empty_string(metadata[key])
            self.assertEqual(metadata["result_basis_ref"], proposal["proposal_basis_ref"])
            for key in EXPECTED_PROPOSAL_FIELDS:
                self.assertIn(key, result["proposal"])
                self.assertEqual(result["proposal"][key], proposal[key])

    def test_current_candidate_identity_and_check_results(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)
            result = self.resolve_transition(temp_root, proposal)

            current_before = result["current_governing_before"]
            candidate = result["candidate_successor"]
            current_after = result["current_governing_after"]

            self.assertEqual(
                current_before["source_run_path"],
                proposal["current_governing_source_run_path"],
            )
            self.assertEqual(
                current_before["ingress_run_path"],
                proposal["current_governing_ingress_run_path"],
            )
            self.assertEqual(
                current_before["comparison_artifact_path"],
                proposal["current_governing_comparison_artifact_path"],
            )
            self.assertEqual(
                candidate["candidate_status_role"],
                status_builder.ROLE_ELIGIBLE_NON_AUTHORITY,
            )
            self.assertEqual(
                current_after["comparison_artifact_path"],
                candidate["comparison_artifact_path"],
            )

            self.assertGreater(len(result["checks"]), 0)
            for check in result["checks"]:
                self.assertIn("check", check)
                self.assertIn("passed", check)
                self.assertIn("required", check)
                self.assertIn("actual", check)
                self.assertIsInstance(check["check"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])

    def test_summary_helper_for_accepted_transition(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            result = self.resolve_transition(temp_root, self.valid_proposal(stack))

            summary = transition_resolver.build_governing_transition_summary(result)

            for key in (
                "transition_result_id",
                "outcome",
                "refusal_code",
                "refusal_reason",
                "current_governing_before",
                "candidate_successor",
                "current_governing_after",
                "passed_check_count",
                "failed_check_count",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(summary["outcome"], transition_resolver.OUTCOME_ACCEPTED)
            self.assertIsNone(summary["refusal_code"])
            self.assertIsNone(summary["refusal_reason"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["failed_check_count"], 0)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_refusal_candidate_already_current_governing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.current_as_candidate_proposal(stack)

            result = self.resolve_transition(temp_root, proposal)

            self.assert_refused_result(result)
            self.assertIn(
                result["refusal"]["refusal_code"],
                {
                    "CANDIDATE_ALREADY_CURRENT_GOVERNING",
                    "CANDIDATE_NOT_ELIGIBLE",
                },
            )

    def test_refusals_for_empty_basis_and_source_surface(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            missing_basis = self.valid_proposal(
                stack,
                proposal_id="proposal_missing_basis",
                proposal_basis_ref="",
            )
            basis_result = self.resolve_transition(temp_root, missing_basis)
            self.assert_refused_result(basis_result)
            self.assertEqual(
                basis_result["refusal"]["refusal_code"],
                "MISSING_PROPOSAL_BASIS",
            )

            missing_surface = self.valid_proposal(
                stack,
                proposal_id="proposal_missing_surface",
                proposed_by_surface="",
            )
            surface_result = self.resolve_transition(temp_root, missing_surface)
            self.assert_refused_result(surface_result)
            self.assertEqual(
                surface_result["refusal"]["refusal_code"],
                "MISSING_PROPOSAL_SOURCE_SURFACE",
            )

    def test_refusal_candidate_not_eligible_from_status_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)

            status_packet = self.read_json(stack["status_path"])
            for entry in status_packet["preserved_run_status_entries"]:
                if entry["status_role"] == status_builder.ROLE_ELIGIBLE_NON_AUTHORITY:
                    entry["status_role"] = status_builder.ROLE_INELIGIBLE
                    entry["candidate_eligible"] = False
                    entry["status_reason"] = "TEMP_TEST_CANDIDATE_NOT_ELIGIBLE"
                    entry["ineligibility_reasons"] = [
                        "temporary test made candidate ineligible"
                    ]
            self.write_json(stack["status_path"], status_packet)

            result = self.resolve_transition(temp_root, proposal)

            self.assert_refused_result(result)
            self.assertEqual(result["refusal"]["refusal_code"], "CANDIDATE_NOT_ELIGIBLE")

    def test_canonical_execution_line_mismatch_fails_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)

            family = self.read_json(stack["family_path"])
            family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            self.write_json(stack["family_path"], family)

            with self.assertRaises(
                transition_resolver.GoverningTransitionResolutionError
            ):
                self.resolve_transition(temp_root, proposal)

    def test_latest_inference_shortcuts_are_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            latest_emitted = self.valid_proposal(
                stack,
                proposal_id="proposal_latest_emitted",
                proposal_basis_ref="latest emitted recency shortcut",
            )
            latest_emitted_result = self.resolve_transition(temp_root, latest_emitted)
            self.assert_refused_result(latest_emitted_result)
            self.assertEqual(
                latest_emitted_result["refusal"]["refusal_code"],
                "LATEST_EMITTED_INFERENCE_REFUSED",
            )

            latest_eligible = self.valid_proposal(
                stack,
                proposal_id="proposal_latest_eligible",
                proposal_basis_ref="latest eligible recency shortcut",
            )
            latest_eligible_result = self.resolve_transition(temp_root, latest_eligible)
            self.assert_refused_result(latest_eligible_result)
            self.assertEqual(
                latest_eligible_result["refusal"]["refusal_code"],
                "LATEST_ELIGIBLE_INFERENCE_REFUSED",
            )

    def test_hard_malformed_proposal_failures(self) -> None:
        with self.assertRaises(transition_resolver.GoverningTransitionResolutionError):
            transition_resolver.resolve_governing_transition(["not", "a", "mapping"])  # type: ignore[arg-type]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)

            missing = dict(proposal)
            del missing["proposal_basis_ref"]
            with self.assertRaises(
                transition_resolver.GoverningTransitionResolutionError
            ):
                self.resolve_transition(temp_root, missing)

            wrong_type = dict(proposal)
            wrong_type["proposed_at"] = 123  # type: ignore[assignment]
            with self.assertRaises(
                transition_resolver.GoverningTransitionResolutionError
            ):
                self.resolve_transition(temp_root, wrong_type)

            with self.assertRaises(
                transition_resolver.GoverningTransitionResolutionError
            ):
                self.resolve_transition_from_path(temp_root, temp_root / "missing.json")

            non_object_path = temp_root / "proposal-list.json"
            non_object_path.write_text("[1, 2, 3]\n", encoding="utf-8")
            with self.assertRaises(
                transition_resolver.GoverningTransitionResolutionError
            ):
                self.resolve_transition_from_path(temp_root, non_object_path)

    def test_hard_artifact_correspondence_failures(self) -> None:
        cases = (
            (
                "authority",
                "authority_path",
                lambda payload: payload.pop("authority_decision", None),
            ),
            (
                "family",
                "family_path",
                lambda payload: payload.pop("canonical_execution_line", None),
            ),
            (
                "status",
                "status_path",
                lambda payload: payload.pop("preserved_run_status_entries", None),
            ),
            (
                "governing",
                "governing_path",
                lambda payload: payload.pop("current_governing_run", None),
            ),
        )
        for label, path_key, mutate in cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    proposal = self.valid_proposal(stack)
                    artifact = self.read_json(stack[path_key])
                    mutate(artifact)
                    self.write_json(stack[path_key], artifact)

                    with self.assertRaises(
                        transition_resolver.GoverningTransitionResolutionError
                    ):
                        self.resolve_transition(temp_root, proposal)

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            result = self.resolve_transition(temp_root, self.valid_proposal(stack))
            output_path = temp_root / "nested" / "transition" / "result.json"

            with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
                written = transition_resolver.write_governing_transition_result(
                    result,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    transition_resolver.GoverningTransitionResolutionError
                ):
                    transition_resolver.write_governing_transition_result(
                        result,
                        output_path,
                    )

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            result = self.resolve_transition(temp_root, self.valid_proposal(stack))

            with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
                first = transition_resolver.write_governing_transition_result(result)
                first_text = first.read_text(encoding="utf-8")
                second = transition_resolver.write_governing_transition_result(result)

            self.assertEqual(
                first,
                temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT
                / "proposal_accepted__governing_transition_result.json",
            )
            self.assertEqual(
                second,
                temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT
                / "proposal_accepted__governing_transition_result_001.json",
            )
            self.assertEqual(first.read_text(encoding="utf-8"), first_text)
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            proposal = self.valid_proposal(stack)

            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root / transition_resolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / transition_resolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root / transition_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root / transition_resolver.CURRENT_GOVERNING_PACKET_ROOT,
            }
            before = {
                label: self.json_texts(root)
                for label, root in roots.items()
            }

            first = self.resolve_transition(temp_root, proposal)
            after_first = {
                label: self.json_texts(root)
                for label, root in roots.items()
            }
            second = self.resolve_transition(temp_root, proposal)
            after_second = {
                label: self.json_texts(root)
                for label, root in roots.items()
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["proposal"], second["proposal"])
            self.assertEqual(first["current_governing_before"], second["current_governing_before"])
            self.assertEqual(first["candidate_successor"], second["candidate_successor"])
            self.assertEqual(first["current_governing_after"], second["current_governing_after"])
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(first["refusal"], second["refusal"])
            self.assertEqual(first["checks"], second["checks"])
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
