"""Bounded tests for the v0-min coexistence governing re-resolution resolver.

These tests lock the current additive re-resolution surface in
``src/resolve_integrity_host_v0_min_coexistence_governing_reresolution.py``
using real source scenario runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, run-family packets,
preserved-run status packets, current-governing packets, and
governing-transition result artifacts emitted into temporary roots.

They verify successor projection emission, blocked re-resolution outcomes,
successor artifact family visibility, non-claims, write behavior, malformed
artifact failures, and read-only behavior. They do not test replay, merge,
persistence architecture, registry integration, distributed continuity, CLI
behavior, or broad governance frameworks.
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
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "reresolution_metadata",
    "input_references",
    "selected_transition_result",
    "checks",
    "outcome",
    "block",
    "successor_artifacts",
    "successor_projection_summary",
    "non_claims",
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
    "final_governing_reresolution_completed",
}

SUCCESSOR_ARTIFACT_KEYS = {
    "successor_authority_artifact_path",
    "successor_family_packet_path",
    "successor_status_packet_path",
    "successor_governing_packet_path",
}


class IntegrityHostV0MinCoexistenceGoverningReresolutionTests(unittest.TestCase):
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

    def emit_transition_result(
        self,
        temp_root: Path,
        proposal: dict[str, Any],
        *,
        write_artifact: bool = True,
        output_path: Path | None = None,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            result = transition_resolver.resolve_governing_transition(proposal)
            path = (
                transition_resolver.write_governing_transition_result(
                    result,
                    output_path,
                )
                if write_artifact
                else None
            )
        return path, result

    def build_multi_run_stack(
        self,
        temp_root: Path,
        *,
        write_transition_artifact: bool = True,
        proposal_id: str = "proposal_accepted",
    ) -> dict[str, Any]:
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

        proposal = self.valid_proposal(
            current_entry,
            candidates[0],
            proposal_id=proposal_id,
        )
        transition_path, transition_result = self.emit_transition_result(
            temp_root,
            proposal,
            write_artifact=write_transition_artifact,
        )
        self.assertEqual(
            transition_result["outcome"],
            transition_resolver.OUTCOME_ACCEPTED,
        )

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
            "proposal": proposal,
            "transition_path": transition_path,
            "transition_result": transition_result,
        }

    def valid_proposal(
        self,
        current: dict[str, Any],
        candidate: dict[str, Any],
        *,
        proposal_id: str = "proposal_accepted",
    ) -> dict[str, str]:
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
            "proposal_basis_ref": "bounded explicit transition test basis",
            "proposed_at": "2026-04-21T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_governing_reresolution.py"
            ),
        }

    def current_as_candidate_proposal(
        self,
        stack: dict[str, Any],
    ) -> dict[str, str]:
        current = stack["current_entry"]
        return self.valid_proposal(
            current,
            current,
            proposal_id="proposal_candidate_already_current",
        )

    def resolve_reresolution_default(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            return reresolver.resolve_governing_reresolution()

    def resolve_reresolution_object(
        self,
        temp_root: Path,
        transition_result: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            return reresolver.resolve_governing_reresolution(transition_result)

    def resolve_reresolution_from_path(
        self,
        temp_root: Path,
        transition_path: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            return reresolver.resolve_governing_reresolution_from_path(
                transition_path
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

    def copy_payload(self, payload: Any) -> Any:
        return json.loads(json.dumps(payload, sort_keys=True))

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
        self.assertIsInstance(result["reresolution_metadata"], dict)
        self.assertIsInstance(result["input_references"], dict)
        self.assertTrue(
            result["selected_transition_result"] is None
            or isinstance(result["selected_transition_result"], dict)
        )
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertIsInstance(result["successor_artifacts"], dict)
        self.assertIsInstance(result["successor_projection_summary"], dict)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_emitted_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], reresolver.OUTCOME_SUCCESSOR_EMITTED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(set(result["successor_artifacts"]), SUCCESSOR_ARTIFACT_KEYS)
        for value in result["successor_artifacts"].values():
            self.assert_non_empty_string(value)
        self.assert_non_claims_false(result)

    def assert_blocked_result(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], reresolver.OUTCOME_BLOCKED)
        self.assert_non_empty_string(result["block"]["block_code"])
        self.assert_non_empty_string(result["block"]["block_reason"])
        if expected_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_code)
        for value in result["successor_artifacts"].values():
            self.assertIsNone(value)
        self.assert_non_claims_false(result)

    def assert_paths_same(self, temp_root: Path, left: str, right: str | Path) -> None:
        self.assertEqual(
            self.resolve_display_path(temp_root, left),
            self.resolve_display_path(temp_root, str(right)),
        )

    def assert_under_reresolution_root(self, temp_root: Path, path: Path) -> None:
        root = (temp_root / reresolver.GOVERNING_RERESOLUTION_ROOT).resolve()
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            self.fail(f"{path} was not written under {root}: {exc}")

    def test_real_accepted_reresolution_default_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_reresolution_default(temp_root)

            self.assert_emitted_result(result)
            metadata = result["reresolution_metadata"]
            for key in (
                "reresolution_id",
                "reresolution_type",
                "reresolution_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty_string(metadata[key])
            refs = result["input_references"]
            for key in (
                "authority_artifact_path",
                "family_packet_path",
                "status_packet_path",
                "current_governing_packet_path",
                "selected_transition_result_artifact_path",
            ):
                self.assert_non_empty_string(refs[key])
            self.assert_paths_same(
                temp_root,
                refs["selected_transition_result_artifact_path"],
                stack["transition_path"],
            )
            selected = result["selected_transition_result"]
            self.assertIsInstance(selected, dict)
            self.assertEqual(
                selected["transition_result_id"],
                stack["transition_result"]["result_metadata"][
                    "transition_result_id"
                ],
            )
            self.assertEqual(
                selected["transition_proposal_id"],
                stack["proposal"]["transition_proposal_id"],
            )
            self.assertEqual(selected["outcome"], transition_resolver.OUTCOME_ACCEPTED)
            self.assertEqual(
                selected["candidate_successor"]["source_run_path"],
                stack["proposal"]["candidate_successor_source_run_path"],
            )
            self.assertEqual(
                result["successor_projection_summary"][
                    "new_governing_source_run_path"
                ],
                stack["proposal"]["candidate_successor_source_run_path"],
            )

    def test_accepted_reresolution_from_path_and_object(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            object_result = self.resolve_reresolution_object(
                temp_root,
                stack["transition_result"],
            )
            path_result = self.resolve_reresolution_from_path(
                temp_root,
                stack["transition_path"],
            )

            self.assert_emitted_result(object_result)
            self.assert_emitted_result(path_result)
            self.assertIsNone(
                object_result["input_references"][
                    "selected_transition_result_artifact_path"
                ]
            )
            self.assert_paths_same(
                temp_root,
                path_result["input_references"][
                    "selected_transition_result_artifact_path"
                ],
                stack["transition_path"],
            )
            self.assertEqual(
                object_result["successor_projection_summary"][
                    "new_governing_source_run_path"
                ],
                path_result["successor_projection_summary"][
                    "new_governing_source_run_path"
                ],
            )
            self.assertEqual(
                object_result["selected_transition_result"][
                    "transition_result_id"
                ],
                path_result["selected_transition_result"]["transition_result_id"],
            )

    def test_check_results_and_summary_helper_for_emitted_projection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(temp_root)

            result = self.resolve_reresolution_default(temp_root)
            self.assert_emitted_result(result)

            self.assertGreater(len(result["checks"]), 0)
            for check in result["checks"]:
                self.assertIn("check", check)
                self.assertIn("passed", check)
                self.assertIn("required", check)
                self.assertIn("actual", check)
                self.assertIsInstance(check["check"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])

            summary = reresolver.build_governing_reresolution_summary(result)
            for key in (
                "outcome",
                "block_code",
                "block_reason",
                "selected_transition_result_id",
                "prior_governing_source_run_path",
                "new_governing_source_run_path",
                "successor_artifact_paths",
                "passed_check_count",
                "failed_check_count",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(summary["outcome"], reresolver.OUTCOME_SUCCESSOR_EMITTED)
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["failed_check_count"], 0)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_successor_artifact_family_and_projection_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_reresolution_default(temp_root)
            self.assert_emitted_result(result)

            artifacts = result["successor_artifacts"]
            parsed_artifacts: dict[str, dict[str, Any]] = {}
            for key, display_path in artifacts.items():
                artifact_path = self.resolve_display_path(temp_root, display_path)
                self.assertTrue(artifact_path.exists(), key)
                self.assert_under_reresolution_root(temp_root, artifact_path)
                parsed_artifacts[key] = self.read_json(artifact_path)

            authority = parsed_artifacts["successor_authority_artifact_path"]
            family = parsed_artifacts["successor_family_packet_path"]
            status = parsed_artifacts["successor_status_packet_path"]
            governing = parsed_artifacts["successor_governing_packet_path"]
            prior_source = stack["current_entry"]["source_run_directory_path"]
            successor_source = stack["candidate_entry"]["source_run_directory_path"]

            self.assertEqual(
                authority["authority_decision"][
                    "selected_source_run_directory_path"
                ],
                successor_source,
            )
            self.assertEqual(
                family["currentness_status"][
                    "current_execution_authority_source_run_path"
                ],
                successor_source,
            )

            status_entries = status["preserved_run_status_entries"]
            prior_entries = [
                entry
                for entry in status_entries
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, prior_source)
            ]
            successor_entries = [
                entry
                for entry in status_entries
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, successor_source)
            ]
            self.assertEqual(len(prior_entries), 1)
            self.assertEqual(len(successor_entries), 1)
            self.assertEqual(
                prior_entries[0]["status_role"],
                status_builder.ROLE_ELIGIBLE_NON_AUTHORITY,
            )
            self.assertFalse(prior_entries[0]["current_authority"])
            self.assertEqual(
                successor_entries[0]["status_role"],
                status_builder.ROLE_CURRENT_AUTHORITY,
            )
            self.assertTrue(successor_entries[0]["current_authority"])

            current = governing["current_governing_run"]
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    current["source_run_directory_path"],
                ),
                self.resolve_display_path(temp_root, successor_source),
            )
            non_governing_sources = {
                self.resolve_display_path(temp_root, entry["source_run_directory_path"])
                for entry in governing["preserved_non_governing_runs"]
            }
            self.assertIn(
                self.resolve_display_path(temp_root, prior_source),
                non_governing_sources,
            )

            projection = result["successor_projection_summary"]
            self.assertNotEqual(
                projection["prior_governing_source_run_path"],
                projection["new_governing_source_run_path"],
            )
            self.assertGreaterEqual(projection["preserved_run_count"], 2)
            self.assertEqual(projection["current_authority_run_count"], 1)
            self.assertIn("preserved_ineligible_count", projection)
            self.assertGreaterEqual(
                projection["preserved_eligible_non_authority_count"],
                1,
            )

    def test_blocked_no_accepted_transition_result_or_only_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(temp_root, write_transition_artifact=False)

            result = self.resolve_reresolution_default(temp_root)

            self.assert_blocked_result(result, "NO_ACCEPTED_TRANSITION_RESULT")
            self.assertIsNone(result["selected_transition_result"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_transition_artifact=False,
            )
            refused_proposal = self.current_as_candidate_proposal(stack)
            refused_path, refused_result = self.emit_transition_result(
                temp_root,
                refused_proposal,
                write_artifact=True,
            )
            self.assertEqual(
                refused_result["outcome"],
                transition_resolver.OUTCOME_REFUSED,
            )
            self.assertIsNotNone(refused_path)

            result = self.resolve_reresolution_default(temp_root)

            self.assert_blocked_result(result, "NO_ACCEPTED_TRANSITION_RESULT")
            self.assertIsNone(result["selected_transition_result"])

    def test_blocked_accepted_result_does_not_match_current_governing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            transition = self.copy_payload(stack["transition_result"])
            transition["current_governing_before"]["source_run_path"] = stack[
                "candidate_entry"
            ]["source_run_directory_path"]

            result = self.resolve_reresolution_object(temp_root, transition)

            self.assert_blocked_result(
                result,
                "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING",
            )

    def test_blocked_canonical_execution_line_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            authority = self.read_json(stack["authority_path"])
            candidate_source = stack["candidate_entry"]["source_run_directory_path"]
            for entry in authority["candidate_runs"]:
                if entry["source_run_directory_path"] == candidate_source:
                    entry["eligibility_checks"][
                        "canonical_core_execution_file_preserved"
                    ] = False
            self.write_json(stack["authority_path"], authority)

            result = self.resolve_reresolution_object(
                temp_root,
                stack["transition_result"],
            )

            self.assert_blocked_result(result, "CANONICAL_EXECUTION_LINE_MISMATCH")

    def test_blocked_successor_not_visible_in_family_or_status(self) -> None:
        cases = (
            (
                "family",
                "family_path",
                "preserved_runs",
                "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_FAMILY",
            ),
            (
                "status",
                "status_path",
                "preserved_run_status_entries",
                "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS",
            ),
        )
        for label, path_key, list_key, expected_code in cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    candidate_source = stack["candidate_entry"][
                        "source_run_directory_path"
                    ]
                    artifact = self.read_json(stack[path_key])
                    artifact[list_key] = [
                        entry
                        for entry in artifact[list_key]
                        if entry["source_run_directory_path"] != candidate_source
                    ]
                    self.write_json(stack[path_key], artifact)

                    result = self.resolve_reresolution_object(
                        temp_root,
                        stack["transition_result"],
                    )

                    self.assert_blocked_result(result, expected_code)

    def test_blocked_replay_merge_continuity_and_standing_shortcuts(self) -> None:
        cases = (
            ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
            ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
            ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
        )
        for non_claim_key, expected_code in cases:
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    transition = self.copy_payload(stack["transition_result"])
                    transition["non_claims"][non_claim_key] = True

                    result = self.resolve_reresolution_object(temp_root, transition)

                    self.assert_blocked_result(result, expected_code)

    def test_multiple_accepted_result_conflict_blocks_without_arbitration(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            conflict = self.copy_payload(stack["transition_result"])
            current = stack["current_entry"]
            conflict["result_metadata"]["transition_result_id"] = (
                "conflicting_accepted_transition_result"
            )
            conflict["proposal"]["transition_proposal_id"] = (
                "proposal_conflicting_accepted"
            )
            conflict["candidate_successor"]["source_run_path"] = current[
                "source_run_directory_path"
            ]
            conflict["candidate_successor"]["ingress_run_path"] = current[
                "matched_ingress_run_path"
            ]
            conflict["candidate_successor"]["comparison_artifact_path"] = current[
                "matched_comparison_artifact_path"
            ]
            conflict["current_governing_after"]["source_run_path"] = current[
                "source_run_directory_path"
            ]
            conflict["current_governing_after"]["ingress_run_path"] = current[
                "matched_ingress_run_path"
            ]
            conflict["current_governing_after"]["comparison_artifact_path"] = current[
                "matched_comparison_artifact_path"
            ]
            conflict_path = (
                temp_root
                / reresolver.GOVERNING_TRANSITION_RESULT_ROOT
                / "conflicting_accepted__governing_transition_result.json"
            )
            self.write_json(conflict_path, conflict)

            result = self.resolve_reresolution_default(temp_root)

            self.assert_blocked_result(
                result,
                "MULTIPLE_ACCEPTED_RESULTS_CONFLICT_UNRESOLVED",
            )
            for value in result["successor_artifacts"].values():
                self.assertIsNone(value)

    def test_hard_malformed_artifact_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(reresolver.GoverningReresolutionError):
                    reresolver.resolve_governing_reresolution()

        malformed_transition_cases = (
            ("missing", None),
            ("non_object", [1, 2, 3]),
            ("missing_metadata", {"outcome": transition_resolver.OUTCOME_ACCEPTED}),
        )
        for label, payload in malformed_transition_cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    if payload is None:
                        path = temp_root / "missing_transition_result.json"
                    else:
                        path = temp_root / f"{label}.json"
                        path.write_text(
                            json.dumps(payload, indent=2, sort_keys=True) + "\n",
                            encoding="utf-8",
                        )
                    with mock.patch.object(
                        reresolver,
                        "_repo_root",
                        return_value=temp_root,
                    ):
                        with self.assertRaises(
                            reresolver.GoverningReresolutionError
                        ):
                            reresolver.resolve_governing_reresolution_from_path(path)

        current_artifact_cases = (
            (
                "authority",
                "authority_path",
                lambda payload: payload.pop("canonical_execution_line", None),
            ),
            (
                "family",
                "family_path",
                lambda payload: payload.pop("currentness_status", None),
            ),
            (
                "status",
                "status_path",
                lambda payload: payload.pop("aggregate_status_counts", None),
            ),
            (
                "governing",
                "governing_path",
                lambda payload: payload.pop("current_governing_run", None),
            ),
        )
        for label, path_key, mutate in current_artifact_cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    artifact = self.read_json(stack[path_key])
                    mutate(artifact)
                    self.write_json(stack[path_key], artifact)

                    with self.assertRaises(
                        reresolver.GoverningReresolutionError
                    ):
                        self.resolve_reresolution_object(
                            temp_root,
                            stack["transition_result"],
                        )

    def test_summary_helper_for_blocked_result(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(temp_root, write_transition_artifact=False)

            result = self.resolve_reresolution_default(temp_root)
            self.assert_blocked_result(result, "NO_ACCEPTED_TRANSITION_RESULT")
            summary = reresolver.build_governing_reresolution_summary(result)

            self.assertEqual(summary["outcome"], reresolver.OUTCOME_BLOCKED)
            self.assertEqual(summary["block_code"], "NO_ACCEPTED_TRANSITION_RESULT")
            self.assert_non_empty_string(summary["block_reason"])
            self.assertIsNone(summary["selected_transition_result_id"])
            self.assertGreaterEqual(summary["failed_check_count"], 1)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(temp_root)
            result = self.resolve_reresolution_default(temp_root)
            output_path = temp_root / "nested" / "reresolution" / "result.json"

            with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
                written = reresolver.write_governing_reresolution_result(
                    result,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(reresolver.GoverningReresolutionError):
                    reresolver.write_governing_reresolution_result(
                        result,
                        output_path,
                    )

            with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
                default_first = reresolver.write_governing_reresolution_result(result)
                default_second = reresolver.write_governing_reresolution_result(result)

            self.assertTrue(default_first.exists())
            self.assertTrue(default_second.exists())
            self.assertNotEqual(default_first, default_second)
            self.assert_under_reresolution_root(temp_root, default_first)
            self.assert_under_reresolution_root(temp_root, default_second)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root / reresolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / reresolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root / reresolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root / reresolver.CURRENT_GOVERNING_PACKET_ROOT,
                "transition": temp_root / reresolver.GOVERNING_TRANSITION_RESULT_ROOT,
            }
            before = {label: self.json_texts(root) for label, root in roots.items()}

            first = self.resolve_reresolution_object(
                temp_root,
                stack["transition_result"],
            )
            after_first = {
                label: self.json_texts(root) for label, root in roots.items()
            }
            second = self.resolve_reresolution_object(
                temp_root,
                stack["transition_result"],
            )
            after_second = {
                label: self.json_texts(root) for label, root in roots.items()
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["selected_transition_result"], second["selected_transition_result"])
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(first["block"], second["block"])
            self.assertEqual(first["successor_projection_summary"], second["successor_projection_summary"])
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
