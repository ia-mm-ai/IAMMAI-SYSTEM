"""Bounded tests for the v0-min governing successor-adoption v2 resolver.

These tests lock the narrow successor-adoption v2 surface in
``src/resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py``
using real source scenario runs, receiving-ingress runs, source-to-ingress
comparisons, authority resolutions, run-family packets, preserved-run status
packets, current-governing packets, governing-transition results, and
governing re-resolution artifacts emitted into temporary roots.

They specifically verify that v2 accepts the actual emitted re-resolution
artifact shape, where the selected transition-result section is named
``selected_transition_result``. They also lock the bounded compatibility alias
``selected_reresolution_result`` and the clear failure when neither field is
present. The suite does not test replay, merge, persistence architecture,
registry integration, distributed continuity, CLI behavior, or broad governance
frameworks.
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
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "adoption_metadata",
    "prior_current_family",
    "selected_reresolution_result",
    "selected_successor_family",
    "checks",
    "outcome",
    "block",
    "adopted_family_references",
    "adoption_summary",
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
    "final_governing_successor_adoption_completed",
}

ADOPTED_REFERENCE_KEYS = {
    "adopted_authority_artifact_path",
    "adopted_family_packet_path",
    "adopted_status_packet_path",
    "adopted_current_governing_packet_path",
}

SUCCESSOR_REFERENCE_KEYS = {
    "successor_authority_artifact_path",
    "successor_family_packet_path",
    "successor_status_packet_path",
    "successor_current_governing_packet_path",
}


class IntegrityHostV0MinCoexistenceGoverningSuccessorAdoptionV2Tests(
    unittest.TestCase
):
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
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            result = transition_resolver.resolve_governing_transition(proposal)
            path = (
                transition_resolver.write_governing_transition_result(result)
                if write_artifact
                else None
            )
        return path, result

    def emit_reresolution_result_from_object(
        self,
        temp_root: Path,
        transition_result: dict[str, Any],
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            result = reresolver.resolve_governing_reresolution(transition_result)
        output_path = self.reresolution_result_path(temp_root, result)
        result = self.current_shape_reresolution_result(result)
        self.write_json(output_path, result)
        return output_path, result

    def emit_reresolution_result_from_path(
        self,
        temp_root: Path,
        transition_path: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            result = reresolver.resolve_governing_reresolution_from_path(
                transition_path
            )
        output_path = self.reresolution_result_path(temp_root, result)
        result = self.current_shape_reresolution_result(result)
        self.write_json(output_path, result)
        return output_path, result

    def build_multi_run_stack(
        self,
        temp_root: Path,
        *,
        write_transition_artifact: bool = True,
        emit_reresolution: bool = True,
        reresolution_from_path: bool = True,
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

        proposal = self.valid_proposal(current_entry, candidates[0])
        transition_path, transition_result = self.emit_transition_result(
            temp_root,
            proposal,
            write_artifact=write_transition_artifact,
        )
        self.assertEqual(
            transition_result["outcome"],
            transition_resolver.OUTCOME_ACCEPTED,
        )

        reresolution_path = None
        reresolution_result = None
        if emit_reresolution:
            if reresolution_from_path:
                self.assertIsNotNone(transition_path)
                reresolution_path, reresolution_result = (
                    self.emit_reresolution_result_from_path(
                        temp_root,
                        transition_path,
                    )
                )
            else:
                reresolution_path, reresolution_result = (
                    self.emit_reresolution_result_from_object(
                        temp_root,
                        transition_result,
                    )
                )
            self.assertEqual(
                reresolution_result["outcome"],
                reresolver.OUTCOME_SUCCESSOR_EMITTED,
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
            "reresolution_path": reresolution_path,
            "reresolution_result": reresolution_result,
        }

    def valid_proposal(
        self,
        current: dict[str, Any],
        candidate: dict[str, Any],
    ) -> dict[str, str]:
        return {
            "transition_proposal_id": "proposal_accepted_for_adoption",
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
            "proposal_basis_ref": "bounded explicit adoption test transition basis",
            "proposed_at": "2026-04-21T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py"
            ),
        }

    def resolve_adoption_default(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            return adoption_resolver.resolve_governing_successor_adoption()

    def resolve_adoption_object(
        self,
        temp_root: Path,
        reresolution_result: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            return adoption_resolver.resolve_governing_successor_adoption(
                reresolution_result
            )

    def resolve_adoption_from_path(
        self,
        temp_root: Path,
        reresolution_path: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            return adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_path
            )

    def reresolution_result_path(
        self,
        temp_root: Path,
        result: dict[str, Any],
    ) -> Path:
        run_dir = self.resolve_display_path(
            temp_root,
            result["input_references"]["reresolution_run_directory_path"],
        )
        candidates = sorted(run_dir.glob("*_result.json"))
        self.assertEqual(len(candidates), 1)
        return candidates[0]

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

    def current_shape_reresolution_result(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        result = self.copy_payload(payload)
        self.assertIn("selected_transition_result", result)
        self.assertNotIn("selected_reresolution_result", result)
        selected = result["selected_transition_result"]
        self.assertTrue(selected is None or isinstance(selected, dict))
        return result

    def alias_shape_reresolution_result(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        result = self.copy_payload(payload)
        selected = result.pop("selected_transition_result")
        self.assertIsInstance(selected, dict)
        result["selected_reresolution_result"] = selected
        return result

    def missing_selected_section_reresolution_result(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        result = self.copy_payload(payload)
        result.pop("selected_transition_result", None)
        result.pop("selected_reresolution_result", None)
        return result

    def copy_payload(self, payload: Any) -> Any:
        return json.loads(json.dumps(payload, sort_keys=True))

    def resolve_display_path(self, repo_root: Path, value: str | Path) -> Path:
        path = Path(value)
        if path.is_absolute():
            return path.resolve()
        return (repo_root / path).resolve()

    def json_texts(self, root: Path) -> dict[str, str]:
        if not root.exists():
            return {}
        return {
            str(path.relative_to(root)): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*.json"))
        }

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_result_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(result["adoption_metadata"], dict)
        self.assertIsInstance(result["prior_current_family"], dict)
        self.assertIsInstance(result["selected_reresolution_result"], dict)
        self.assertIsInstance(result["selected_successor_family"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertIsInstance(result["adopted_family_references"], dict)
        self.assertIsInstance(result["adoption_summary"], dict)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_adopted_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], adoption_resolver.OUTCOME_ADOPTED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(set(result["adopted_family_references"]), ADOPTED_REFERENCE_KEYS)
        self.assertEqual(set(result["selected_successor_family"]), SUCCESSOR_REFERENCE_KEYS)
        for value in result["adopted_family_references"].values():
            self.assert_non_empty_string(value)
        for value in result["selected_successor_family"].values():
            self.assert_non_empty_string(value)
        self.assert_non_claims_false(result)

    def assert_blocked_result(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
    ) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], adoption_resolver.OUTCOME_BLOCKED)
        self.assert_non_empty_string(result["block"]["block_code"])
        self.assert_non_empty_string(result["block"]["block_reason"])
        if expected_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_code)
        for value in result["adopted_family_references"].values():
            self.assertIsNone(value)
        self.assert_non_claims_false(result)

    def assert_paths_same(self, temp_root: Path, left: str | Path, right: str | Path) -> None:
        self.assertEqual(
            self.resolve_display_path(temp_root, left),
            self.resolve_display_path(temp_root, right),
        )

    def assert_under_adoption_root(self, temp_root: Path, path: Path) -> None:
        root = (
            temp_root / adoption_resolver.GOVERNING_SUCCESSOR_ADOPTION_ROOT
        ).resolve()
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            self.fail(f"{path} was not written under {root}: {exc}")

    def assert_current_family_paths(
        self,
        temp_root: Path,
        result: dict[str, Any],
        stack: dict[str, Any],
    ) -> None:
        prior = result["prior_current_family"]
        expected = {
            "prior_authority_artifact_path": stack["authority_path"],
            "prior_family_packet_path": stack["family_path"],
            "prior_status_packet_path": stack["status_path"],
            "prior_current_governing_packet_path": stack["governing_path"],
        }
        for key, expected_path in expected.items():
            self.assert_non_empty_string(prior[key])
            self.assert_paths_same(temp_root, prior[key], expected_path)

    def assert_successor_family_files(
        self,
        temp_root: Path,
        references: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        parsed: dict[str, dict[str, Any]] = {}
        for key, display_path in references.items():
            self.assert_non_empty_string(display_path)
            path = self.resolve_display_path(temp_root, display_path)
            self.assertTrue(path.exists(), key)
            self.assertTrue(path.is_file(), key)
            parsed[key] = self.read_json(path)
        return parsed

    def test_real_accepted_successor_adoption_default_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            self.assertIn("selected_transition_result", stack["reresolution_result"])
            self.assertNotIn(
                "selected_reresolution_result",
                stack["reresolution_result"],
            )
            self.assertIsInstance(
                stack["reresolution_result"]["selected_transition_result"],
                dict,
            )

            result = self.resolve_adoption_default(temp_root)

            self.assert_adopted_result(result)
            metadata = result["adoption_metadata"]
            for key in (
                "adoption_result_id",
                "adoption_result_type",
                "adoption_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty_string(metadata[key])

            self.assert_current_family_paths(temp_root, result, stack)
            selected = result["selected_reresolution_result"]
            self.assert_paths_same(
                temp_root,
                selected["reresolution_result_artifact_path"],
                stack["reresolution_path"],
            )
            self.assertEqual(
                selected["reresolution_id"],
                stack["reresolution_result"]["reresolution_metadata"][
                    "reresolution_id"
                ],
            )
            self.assertEqual(selected["outcome"], reresolver.OUTCOME_SUCCESSOR_EMITTED)
            self.assert_paths_same(
                temp_root,
                selected["selected_transition_result_artifact_path"],
                stack["transition_path"],
            )

            for successor_key, result_key in (
                ("successor_authority_artifact_path", "successor_authority_artifact_path"),
                ("successor_family_packet_path", "successor_family_packet_path"),
                ("successor_status_packet_path", "successor_status_packet_path"),
                ("successor_current_governing_packet_path", "successor_governing_packet_path"),
            ):
                self.assert_paths_same(
                    temp_root,
                    result["selected_successor_family"][successor_key],
                    stack["reresolution_result"]["successor_artifacts"][result_key],
                )

            summary = result["adoption_summary"]
            self.assertTrue(summary["successor_family_adopted"])
            self.assertEqual(
                summary["prior_governing_source_run_path"],
                stack["current_entry"]["source_run_directory_path"],
            )
            self.assertEqual(
                summary["new_governing_source_run_path"],
                stack["candidate_entry"]["source_run_directory_path"],
            )

    def test_canonical_selected_transition_result_field_supported_without_alias(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            reresolution = self.copy_payload(stack["reresolution_result"])

            self.assertIn("selected_transition_result", reresolution)
            self.assertIsInstance(reresolution["selected_transition_result"], dict)
            self.assertNotIn("selected_reresolution_result", reresolution)

            result = self.resolve_adoption_object(temp_root, reresolution)

            self.assert_adopted_result(result)
            self.assertEqual(result["outcome"], adoption_resolver.OUTCOME_ADOPTED)

    def test_backward_compatible_selected_reresolution_alias_supported(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            alias_reresolution = self.alias_shape_reresolution_result(
                stack["reresolution_result"]
            )
            alias_path = temp_root / "alias_shape_reresolution_result.json"
            self.write_json(alias_path, alias_reresolution)

            result = self.resolve_adoption_from_path(temp_root, alias_path)

            self.assert_adopted_result(result)
            self.assertEqual(result["outcome"], adoption_resolver.OUTCOME_ADOPTED)
            self.assert_paths_same(
                temp_root,
                result["selected_reresolution_result"][
                    "reresolution_result_artifact_path"
                ],
                alias_path,
            )

    def test_missing_selected_transition_result_fields_fail_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            malformed = self.missing_selected_section_reresolution_result(
                stack["reresolution_result"]
            )
            malformed_path = temp_root / "missing_selected_result_section.json"
            self.write_json(malformed_path, malformed)

            with self.assertRaises(
                adoption_resolver.GoverningSuccessorAdoptionError
            ):
                self.resolve_adoption_from_path(temp_root, malformed_path)

    def test_accepted_adoption_from_path_and_object(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            object_result = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            path_result = self.resolve_adoption_from_path(
                temp_root,
                stack["reresolution_path"],
            )

            self.assert_adopted_result(object_result)
            self.assert_adopted_result(path_result)
            self.assertIsNone(
                object_result["selected_reresolution_result"][
                    "reresolution_result_artifact_path"
                ]
            )
            self.assert_paths_same(
                temp_root,
                path_result["selected_reresolution_result"][
                    "reresolution_result_artifact_path"
                ],
                stack["reresolution_path"],
            )
            self.assertEqual(
                object_result["adoption_summary"]["new_governing_source_run_path"],
                path_result["adoption_summary"]["new_governing_source_run_path"],
            )
            self.assertEqual(
                object_result["selected_reresolution_result"]["reresolution_id"],
                path_result["selected_reresolution_result"]["reresolution_id"],
            )

    def test_checks_and_summary_helper_for_adopted_result(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            self.assert_adopted_result(result)
            self.assertGreater(len(result["checks"]), 0)
            for check in result["checks"]:
                self.assertIn("check", check)
                self.assertIn("passed", check)
                self.assertIn("required", check)
                self.assertIn("actual", check)
                self.assertIsInstance(check["check"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])

            summary = adoption_resolver.build_governing_successor_adoption_summary(
                result
            )
            for key in (
                "adoption_result_id",
                "outcome",
                "block_code",
                "block_reason",
                "selected_reresolution_result_id",
                "prior_governing_source_run_path",
                "new_governing_source_run_path",
                "adopted_family_references",
                "passed_check_count",
                "failed_check_count",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(summary["outcome"], adoption_resolver.OUTCOME_ADOPTED)
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["failed_check_count"], 0)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_adopted_family_references_and_successor_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            self.assert_adopted_result(result)

            for adopted_key, successor_key in (
                ("adopted_authority_artifact_path", "successor_authority_artifact_path"),
                ("adopted_family_packet_path", "successor_family_packet_path"),
                ("adopted_status_packet_path", "successor_status_packet_path"),
                ("adopted_current_governing_packet_path", "successor_current_governing_packet_path"),
            ):
                self.assert_paths_same(
                    temp_root,
                    result["adopted_family_references"][adopted_key],
                    result["selected_successor_family"][successor_key],
                )
                self.assertNotEqual(
                    self.resolve_display_path(
                        temp_root,
                        result["adopted_family_references"][adopted_key],
                    ),
                    self.resolve_display_path(
                        temp_root,
                        result["prior_current_family"][
                            adopted_key.replace("adopted_", "prior_").replace(
                                "authority_artifact_path",
                                "authority_artifact_path",
                            ).replace(
                                "family_packet_path",
                                "family_packet_path",
                            ).replace(
                                "status_packet_path",
                                "status_packet_path",
                            ).replace(
                                "current_governing_packet_path",
                                "current_governing_packet_path",
                            )
                        ],
                    ),
                )

            parsed = self.assert_successor_family_files(
                temp_root,
                result["selected_successor_family"],
            )
            successor_status = parsed["successor_status_packet_path"]
            successor_governing = parsed["successor_current_governing_packet_path"]
            prior_source = stack["current_entry"]["source_run_directory_path"]
            successor_source = stack["candidate_entry"]["source_run_directory_path"]

            prior_entries = [
                entry
                for entry in successor_status["preserved_run_status_entries"]
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, prior_source)
            ]
            successor_entries = [
                entry
                for entry in successor_status["preserved_run_status_entries"]
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

            current = successor_governing["current_governing_run"]
            self.assert_paths_same(
                temp_root,
                current["source_run_directory_path"],
                successor_source,
            )
            non_governing_sources = {
                self.resolve_display_path(temp_root, entry["source_run_directory_path"])
                for entry in successor_governing["preserved_non_governing_runs"]
            }
            self.assertIn(
                self.resolve_display_path(temp_root, prior_source),
                non_governing_sources,
            )

            counts = successor_status["aggregate_status_counts"]
            self.assertGreaterEqual(counts["preserved_run_count"], 2)
            self.assertEqual(counts["current_authority_run_count"], 1)
            self.assertIn("preserved_ineligible_count", counts)
            self.assertGreaterEqual(counts["preserved_eligible_non_authority_count"], 1)

    def test_blocked_no_successor_projection_available_or_only_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(
                temp_root,
                write_transition_artifact=False,
                emit_reresolution=False,
            )

            result = self.resolve_adoption_default(temp_root)

            self.assert_blocked_result(result, "NO_SUCCESSOR_PROJECTION_AVAILABLE")
            self.assertIsNone(result["selected_reresolution_result"]["reresolution_id"])

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_multi_run_stack(
                temp_root,
                write_transition_artifact=False,
                emit_reresolution=False,
            )
            with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
                blocked_reresolution = reresolver.resolve_governing_reresolution()
            self.assertEqual(blocked_reresolution["outcome"], reresolver.OUTCOME_BLOCKED)
            blocked_path = self.reresolution_result_path(temp_root, blocked_reresolution)
            blocked_reresolution = self.current_shape_reresolution_result(
                blocked_reresolution
            )
            self.write_json(blocked_path, blocked_reresolution)

            result = self.resolve_adoption_default(temp_root)

            self.assert_blocked_result(result, "NO_SUCCESSOR_PROJECTION_AVAILABLE")
            self.assertIsNone(result["selected_reresolution_result"]["reresolution_id"])

    def test_blocked_successor_family_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            reresolution = self.copy_payload(stack["reresolution_result"])
            missing_path = self.resolve_display_path(
                temp_root,
                reresolution["successor_artifacts"][
                    "successor_status_packet_path"
                ],
            )
            missing_path.unlink()

            result = self.resolve_adoption_object(temp_root, reresolution)

            self.assert_blocked_result(result, "SUCCESSOR_FAMILY_UNREADABLE")

    def test_blocked_successor_family_correspondence_failures(self) -> None:
        cases = (
            (
                "canonical",
                "successor_family_packet_path",
                lambda payload, stack: payload["canonical_execution_line"].__setitem__(
                    "core_execution_file",
                    "src/not_the_current_core.py",
                ),
                "CANONICAL_EXECUTION_LINE_MISMATCH",
            ),
            (
                "prior_non_authority",
                "successor_status_packet_path",
                lambda payload, stack: [
                    entry.update(
                        {
                            "status_role": status_builder.ROLE_INELIGIBLE,
                            "candidate_eligible": False,
                            "ineligibility_reasons": [
                                "temp test removes prior non-authority preservation"
                            ],
                        }
                    )
                    for entry in payload["preserved_run_status_entries"]
                    if entry["source_run_directory_path"]
                    == stack["current_entry"]["source_run_directory_path"]
                ],
                "SUCCESSOR_FAMILY_DOES_NOT_PRESERVE_PRIOR_GOVERNING_AS_NON_AUTHORITY",
            ),
            (
                "path_mismatch",
                "successor_artifacts",
                lambda payload, stack: payload.__setitem__(
                    "successor_family_packet_path",
                    "artifacts/not_the_named_successor_family.json",
                ),
                "SUCCESSOR_FAMILY_UNREADABLE",
            ),
        )
        for label, target, mutate, expected_code in cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    reresolution = self.copy_payload(stack["reresolution_result"])
                    if target == "successor_artifacts":
                        mutate(reresolution["successor_artifacts"], stack)
                    else:
                        artifact_path = self.resolve_display_path(
                            temp_root,
                            reresolution["successor_artifacts"][target],
                        )
                        artifact = self.read_json(artifact_path)
                        mutate(artifact, stack)
                        self.write_json(artifact_path, artifact)

                    result = self.resolve_adoption_object(temp_root, reresolution)

                    self.assert_blocked_result(result, expected_code)

    def test_non_claim_shortcuts_fail_clearly(self) -> None:
        cases = (
            "replayed_into_live_host",
            "merged_into_local_state",
            "continuity_completed",
            "standing_upgraded",
        )
        for non_claim_key in cases:
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    reresolution = self.copy_payload(stack["reresolution_result"])
                    reresolution["non_claims"][non_claim_key] = True

                    with self.assertRaises(
                        adoption_resolver.GoverningSuccessorAdoptionError
                    ):
                        self.resolve_adoption_object(temp_root, reresolution)

    def test_multiple_successor_family_conflict_blocks_without_arbitration(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            conflict = self.copy_payload(stack["reresolution_result"])
            conflict["reresolution_metadata"]["reresolution_id"] = (
                "conflicting_successor_projection__governing_reresolution"
            )
            conflict["successor_projection_summary"][
                "new_governing_source_run_path"
            ] = stack["current_entry"]["source_run_directory_path"]
            conflict_path = (
                temp_root
                / adoption_resolver.GOVERNING_RERESOLUTION_ROOT
                / "conflicting_successor_projection__governing_reresolution_result.json"
            )
            self.write_json(conflict_path, conflict)

            result = self.resolve_adoption_default(temp_root)

            self.assert_blocked_result(
                result,
                "MULTIPLE_SUCCESSOR_FAMILIES_CONFLICT_UNRESOLVED",
            )

    def test_hard_malformed_artifact_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    adoption_resolver.GoverningSuccessorAdoptionError
                ):
                    adoption_resolver.resolve_governing_successor_adoption()

        malformed_reresolution_cases = (
            ("non_mapping_input", "not a mapping"),
            ("missing_metadata", {"outcome": reresolver.OUTCOME_SUCCESSOR_EMITTED}),
        )
        for label, payload in malformed_reresolution_cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    self.build_multi_run_stack(
                        temp_root,
                        emit_reresolution=False,
                    )
                    with self.assertRaises(
                        adoption_resolver.GoverningSuccessorAdoptionError
                    ):
                        with mock.patch.object(
                            adoption_resolver,
                            "_repo_root",
                            return_value=temp_root,
                        ):
                            adoption_resolver.resolve_governing_successor_adoption(
                                payload  # type: ignore[arg-type]
                            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            path = temp_root / "malformed_reresolution.json"
            path.write_text("[1, 2, 3]\n", encoding="utf-8")
            with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    adoption_resolver.GoverningSuccessorAdoptionError
                ):
                    adoption_resolver.resolve_governing_successor_adoption_from_path(
                        path
                    )

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
                        adoption_resolver.GoverningSuccessorAdoptionError
                    ):
                        self.resolve_adoption_object(
                            temp_root,
                            stack["reresolution_result"],
                        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            reresolution = self.copy_payload(stack["reresolution_result"])
            successor_path = self.resolve_display_path(
                temp_root,
                reresolution["successor_artifacts"][
                    "successor_authority_artifact_path"
                ],
            )
            successor_path.write_text("{not valid json\n", encoding="utf-8")

            with self.assertRaises(adoption_resolver.GoverningSuccessorAdoptionError):
                self.resolve_adoption_object(temp_root, reresolution)

    def test_write_behavior_and_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            result = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            output_path = temp_root / "nested" / "adoption" / "result.json"

            with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
                written = adoption_resolver.write_governing_successor_adoption_result(
                    result,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    adoption_resolver.GoverningSuccessorAdoptionError
                ):
                    adoption_resolver.write_governing_successor_adoption_result(
                        result,
                        output_path,
                    )

            with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
                default_first = (
                    adoption_resolver.write_governing_successor_adoption_result(
                        result
                    )
                )
                default_second = (
                    adoption_resolver.write_governing_successor_adoption_result(
                        result
                    )
                )

            self.assertTrue(default_first.exists())
            self.assertTrue(default_second.exists())
            self.assertNotEqual(default_first, default_second)
            self.assert_under_adoption_root(temp_root, default_first)
            self.assert_under_adoption_root(temp_root, default_second)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root / adoption_resolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / adoption_resolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root / adoption_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root / adoption_resolver.CURRENT_GOVERNING_PACKET_ROOT,
                "transition": temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT,
                "reresolution": temp_root
                / adoption_resolver.GOVERNING_RERESOLUTION_ROOT,
            }
            before = {label: self.json_texts(root) for label, root in roots.items()}

            first = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            after_first = {
                label: self.json_texts(root) for label, root in roots.items()
            }
            second = self.resolve_adoption_object(
                temp_root,
                stack["reresolution_result"],
            )
            after_second = {
                label: self.json_texts(root) for label, root in roots.items()
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(
                first["selected_reresolution_result"],
                second["selected_reresolution_result"],
            )
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(first["block"], second["block"])
            self.assertEqual(first["adopted_family_references"], second["adopted_family_references"])
            self.assertEqual(first["adoption_summary"], second["adoption_summary"])
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
