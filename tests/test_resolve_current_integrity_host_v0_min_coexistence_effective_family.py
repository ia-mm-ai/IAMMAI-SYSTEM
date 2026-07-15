"""Bounded tests for the v0-min effective-family resolver.

These tests lock the current behavior of
``src/resolve_current_integrity_host_v0_min_coexistence_effective_family.py``.
They use real local source runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, run-family packets, preserved-run
status packets, current-governing packets, governing-transition results,
governing re-resolution results, and successor-adoption results emitted into
temporary roots.

The suite verifies effective-family selection only. It does not test replay,
merge, persistence architecture, registry integration, distributed continuity,
CLI behavior, or broad governance frameworks.
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
import resolve_current_integrity_host_v0_min_coexistence_effective_family as effective_resolver  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "resolution_metadata",
    "canonical_execution_line",
    "prior_current_family",
    "selected_adoption_result",
    "effective_family",
    "resolution_basis",
    "checks",
    "outcome",
    "non_effective_preserved_families",
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
    "final_effective_family_resolution_completed",
}

EFFECTIVE_REFERENCE_KEYS = {
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
}

PRIOR_REFERENCE_KEYS = {
    "prior_authority_artifact_path",
    "prior_family_packet_path",
    "prior_status_packet_path",
    "prior_current_governing_packet_path",
}


class IntegrityHostV0MinCoexistenceEffectiveFamilyTests(unittest.TestCase):
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

    def emit_adoption_result_from_object(
        self,
        temp_root: Path,
        reresolution_result: dict[str, Any],
        *,
        write_artifact: bool = True,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            result = adoption_resolver.resolve_governing_successor_adoption(
                reresolution_result
            )
            path = (
                adoption_resolver.write_governing_successor_adoption_result(result)
                if write_artifact
                else None
            )
        return path, result

    def emit_adoption_result_from_path(
        self,
        temp_root: Path,
        reresolution_path: Path,
        *,
        write_artifact: bool = True,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            result = adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_path
            )
            path = (
                adoption_resolver.write_governing_successor_adoption_result(result)
                if write_artifact
                else None
            )
        return path, result

    def build_multi_run_stack(
        self,
        temp_root: Path,
        *,
        write_transition_artifact: bool = True,
        emit_reresolution: bool = True,
        emit_adoption: bool = True,
        write_adoption_artifact: bool = True,
        adoption_from_path: bool = True,
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
            self.assertIsNotNone(transition_path)
            reresolution_path, reresolution_result = (
                self.emit_reresolution_result_from_path(temp_root, transition_path)
            )
            self.assertEqual(
                reresolution_result["outcome"],
                reresolver.OUTCOME_SUCCESSOR_EMITTED,
            )

        adoption_path = None
        adoption_result = None
        if emit_adoption:
            self.assertIsNotNone(reresolution_result)
            if adoption_from_path:
                self.assertIsNotNone(reresolution_path)
                adoption_path, adoption_result = self.emit_adoption_result_from_path(
                    temp_root,
                    reresolution_path,
                    write_artifact=write_adoption_artifact,
                )
            else:
                adoption_path, adoption_result = self.emit_adoption_result_from_object(
                    temp_root,
                    reresolution_result,
                    write_artifact=write_adoption_artifact,
                )
            self.assertEqual(adoption_result["outcome"], adoption_resolver.OUTCOME_ADOPTED)

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
            "adoption_path": adoption_path,
            "adoption_result": adoption_result,
        }

    def valid_proposal(
        self,
        current: dict[str, Any],
        candidate: dict[str, Any],
    ) -> dict[str, str]:
        return {
            "transition_proposal_id": "proposal_accepted_for_effective_family",
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
            "proposal_basis_ref": "bounded explicit effective-family test basis",
            "proposed_at": "2026-04-21T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_current_integrity_host_v0_min_coexistence_effective_family.py"
            ),
        }

    def resolve_effective_default(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            return effective_resolver.resolve_effective_current_family()

    def resolve_effective_object(
        self,
        temp_root: Path,
        adoption_result: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            return effective_resolver.resolve_effective_current_family(adoption_result)

    def resolve_effective_from_path(
        self,
        temp_root: Path,
        adoption_path: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            return effective_resolver.resolve_effective_current_family_from_path(
                adoption_path
            )

    def emit_blocked_adoption_result(
        self,
        temp_root: Path,
        *,
        write_artifact: bool,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            result = adoption_resolver.resolve_governing_successor_adoption()
            self.assertEqual(result["outcome"], adoption_resolver.OUTCOME_BLOCKED)
            path = (
                adoption_resolver.write_governing_successor_adoption_result(result)
                if write_artifact
                else None
            )
        return path, result

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

    def assert_paths_same(self, temp_root: Path, left: str | Path, right: str | Path) -> None:
        self.assertEqual(
            self.resolve_display_path(temp_root, left),
            self.resolve_display_path(temp_root, right),
        )

    def assert_result_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(result["resolution_metadata"], dict)
        self.assertIsInstance(result["canonical_execution_line"], dict)
        self.assertIsInstance(result["prior_current_family"], dict)
        self.assertTrue(
            result["selected_adoption_result"] is None
            or isinstance(result["selected_adoption_result"], dict)
        )
        self.assertIsInstance(result["effective_family"], dict)
        self.assertIsInstance(result["resolution_basis"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["non_effective_preserved_families"], dict)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_adopted_effective_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(
            result["outcome"],
            effective_resolver.OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
        )
        self.assertIsInstance(result["selected_adoption_result"], dict)
        self.assertEqual(set(result["effective_family"]), EFFECTIVE_REFERENCE_KEYS)
        for value in result["effective_family"].values():
            self.assert_non_empty_string(value)
        self.assert_non_claims_false(result)

    def assert_current_effective_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], effective_resolver.OUTCOME_CURRENT_FAMILY_EFFECTIVE)
        self.assertEqual(set(result["effective_family"]), EFFECTIVE_REFERENCE_KEYS)
        for value in result["effective_family"].values():
            self.assert_non_empty_string(value)
        self.assert_non_claims_false(result)

    def assert_current_family_paths(
        self,
        temp_root: Path,
        result: dict[str, Any],
        stack: dict[str, Any],
    ) -> None:
        prior = result["prior_current_family"]
        self.assertEqual(set(prior), PRIOR_REFERENCE_KEYS)
        expected = {
            "prior_authority_artifact_path": stack["authority_path"],
            "prior_family_packet_path": stack["family_path"],
            "prior_status_packet_path": stack["status_path"],
            "prior_current_governing_packet_path": stack["governing_path"],
        }
        for key, expected_path in expected.items():
            self.assert_non_empty_string(prior[key])
            self.assert_paths_same(temp_root, prior[key], expected_path)

    def assert_effective_paths_match_current(
        self,
        temp_root: Path,
        result: dict[str, Any],
        stack: dict[str, Any],
    ) -> None:
        expected = {
            "effective_authority_artifact_path": stack["authority_path"],
            "effective_family_packet_path": stack["family_path"],
            "effective_status_packet_path": stack["status_path"],
            "effective_current_governing_packet_path": stack["governing_path"],
            "effective_source_run_path": stack["current_entry"][
                "source_run_directory_path"
            ],
            "effective_ingress_run_path": stack["current_entry"][
                "matched_ingress_run_path"
            ],
        }
        for key, expected_path in expected.items():
            self.assert_paths_same(temp_root, result["effective_family"][key], expected_path)

    def assert_effective_paths_match_adopted(
        self,
        temp_root: Path,
        result: dict[str, Any],
        adoption: dict[str, Any],
        stack: dict[str, Any],
    ) -> None:
        key_pairs = (
            ("effective_authority_artifact_path", "adopted_authority_artifact_path"),
            ("effective_family_packet_path", "adopted_family_packet_path"),
            ("effective_status_packet_path", "adopted_status_packet_path"),
            (
                "effective_current_governing_packet_path",
                "adopted_current_governing_packet_path",
            ),
        )
        for effective_key, adopted_key in key_pairs:
            self.assert_paths_same(
                temp_root,
                result["effective_family"][effective_key],
                adoption["adopted_family_references"][adopted_key],
            )
        self.assert_paths_same(
            temp_root,
            result["effective_family"]["effective_source_run_path"],
            stack["candidate_entry"]["source_run_directory_path"],
        )
        self.assert_paths_same(
            temp_root,
            result["effective_family"]["effective_ingress_run_path"],
            stack["candidate_entry"]["matched_ingress_run_path"],
        )

    def assert_under_effective_root(self, temp_root: Path, path: Path) -> None:
        root = (temp_root / effective_resolver.EFFECTIVE_FAMILY_RESOLUTION_ROOT).resolve()
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            self.fail(f"{path} was not written under {root}: {exc}")

    def parse_effective_family_files(
        self,
        temp_root: Path,
        result: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        parsed: dict[str, dict[str, Any]] = {}
        path_keys = (
            "effective_authority_artifact_path",
            "effective_family_packet_path",
            "effective_status_packet_path",
            "effective_current_governing_packet_path",
        )
        for key in path_keys:
            path = self.resolve_display_path(temp_root, result["effective_family"][key])
            self.assertTrue(path.is_file(), key)
            parsed[key] = self.read_json(path)
        return parsed

    def test_real_effective_family_resolution_with_adopted_successor_present(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_effective_default(temp_root)

            self.assert_adopted_effective_result(result)
            self.assert_current_family_paths(temp_root, result, stack)
            self.assert_effective_paths_match_adopted(
                temp_root,
                result,
                stack["adoption_result"],
                stack,
            )
            selected = result["selected_adoption_result"]
            self.assert_paths_same(
                temp_root,
                selected["adoption_result_artifact_path"],
                stack["adoption_path"],
            )
            self.assertEqual(
                selected["adoption_result_id"],
                stack["adoption_result"]["adoption_metadata"]["adoption_result_id"],
            )
            self.assertEqual(selected["outcome"], adoption_resolver.OUTCOME_ADOPTED)
            self.assertEqual(
                result["resolution_basis"]["basis"],
                effective_resolver.BASIS_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
            )

    def test_effective_family_from_path_and_object(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            object_result = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )
            path_result = self.resolve_effective_from_path(
                temp_root,
                stack["adoption_path"],
            )

            self.assert_adopted_effective_result(object_result)
            self.assert_adopted_effective_result(path_result)
            self.assertIsNone(
                object_result["selected_adoption_result"][
                    "adoption_result_artifact_path"
                ]
            )
            self.assert_paths_same(
                temp_root,
                path_result["selected_adoption_result"][
                    "adoption_result_artifact_path"
                ],
                stack["adoption_path"],
            )
            self.assertEqual(object_result["outcome"], path_result["outcome"])
            self.assertEqual(
                object_result["effective_family"],
                path_result["effective_family"],
            )

    def test_no_adopted_successor_available_keeps_current_family_effective(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                emit_adoption=False,
            )

            result = self.resolve_effective_default(temp_root)

            self.assert_current_effective_result(result)
            self.assertIsNone(result["selected_adoption_result"])
            self.assert_effective_paths_match_current(temp_root, result, stack)
            self.assertEqual(
                result["resolution_basis"]["basis"],
                effective_resolver.BASIS_CURRENT_FAMILY_REMAINS_EFFECTIVE,
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_transition_artifact=False,
                emit_reresolution=False,
                emit_adoption=False,
            )
            _, blocked_adoption = self.emit_blocked_adoption_result(
                temp_root,
                write_artifact=True,
            )

            default_result = self.resolve_effective_default(temp_root)
            object_result = self.resolve_effective_object(temp_root, blocked_adoption)

            self.assert_current_effective_result(default_result)
            self.assertIsNone(default_result["selected_adoption_result"])
            self.assert_effective_paths_match_current(temp_root, default_result, stack)
            self.assert_current_effective_result(object_result)
            self.assertEqual(
                object_result["selected_adoption_result"]["outcome"],
                adoption_resolver.OUTCOME_BLOCKED,
            )
            self.assertIsNotNone(
                object_result["non_effective_preserved_families"][
                    "adopted_successor_family_not_effective"
                ]
            )

    def test_resolution_metadata_canonical_line_and_prior_family(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )

            metadata = result["resolution_metadata"]
            for key in (
                "effective_family_resolution_id",
                "effective_family_resolution_type",
                "effective_family_resolution_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty_string(metadata[key])
            canonical = result["canonical_execution_line"]
            self.assertEqual(
                canonical["core_execution_file"],
                resolver.CORE_EXECUTION_FILE,
            )
            self.assertIsInstance(canonical["derivative_support_scope"], list)
            self.assertGreater(len(canonical["derivative_support_scope"]), 0)
            self.assertIsInstance(canonical["lineage_predecessor_files"], list)
            self.assertGreater(len(canonical["lineage_predecessor_files"]), 0)
            self.assertNotIn(
                canonical["core_execution_file"],
                canonical["lineage_predecessor_files"],
            )
            self.assert_current_family_paths(temp_root, result, stack)

    def test_checks_summary_helper_and_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )

            self.assert_adopted_effective_result(result)
            self.assertGreater(len(result["checks"]), 0)
            for check in result["checks"]:
                self.assertIn("check", check)
                self.assertIn("passed", check)
                self.assertIn("required", check)
                self.assertIn("actual", check)
                self.assertIsInstance(check["check"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])

            summary = effective_resolver.build_effective_family_summary(result)
            for key in (
                "effective_family_resolution_id",
                "outcome",
                "selected_adoption_result_id",
                "effective_authority_artifact_path",
                "effective_family_packet_path",
                "effective_status_packet_path",
                "effective_current_governing_packet_path",
                "effective_source_run_path",
                "effective_ingress_run_path",
                "prior_current_family",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(
                summary["outcome"],
                effective_resolver.OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
            )
            self.assertEqual(
                summary["selected_adoption_result_id"],
                stack["adoption_result"]["adoption_metadata"]["adoption_result_id"],
            )
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_non_effective_preserved_families_and_adopted_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )

            self.assert_adopted_effective_result(result)
            non_effective = result["non_effective_preserved_families"]
            self.assertTrue(non_effective["prior_current_family_remains_preserved"])
            self.assertTrue(
                non_effective["preserved_non_governing_runs_remain_preserved"]
            )
            self.assert_paths_same(
                temp_root,
                non_effective["prior_current_governing_run_remains_visible"][
                    "source_run_directory_path"
                ],
                stack["current_entry"]["source_run_directory_path"],
            )

            parsed = self.parse_effective_family_files(temp_root, result)
            effective_status = parsed["effective_status_packet_path"]
            effective_governing = parsed["effective_current_governing_packet_path"]
            prior_source = stack["current_entry"]["source_run_directory_path"]
            successor_source = stack["candidate_entry"]["source_run_directory_path"]

            prior_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, prior_source)
            ]
            successor_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
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
            self.assert_paths_same(
                temp_root,
                effective_governing["current_governing_run"][
                    "source_run_directory_path"
                ],
                successor_source,
            )
            non_governing_sources = {
                self.resolve_display_path(temp_root, entry["source_run_directory_path"])
                for entry in effective_governing["preserved_non_governing_runs"]
            }
            self.assertIn(
                self.resolve_display_path(temp_root, prior_source),
                non_governing_sources,
            )
            counts = effective_status["aggregate_status_counts"]
            self.assertGreaterEqual(counts["preserved_run_count"], 2)
            self.assertEqual(counts["current_authority_run_count"], 1)
            self.assertIn("preserved_ineligible_count", counts)
            self.assertGreaterEqual(counts["preserved_eligible_non_authority_count"], 1)

    def test_current_family_non_effective_section_when_blocked_adoption_provided(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_transition_artifact=False,
                emit_reresolution=False,
                emit_adoption=False,
            )
            _, blocked_adoption = self.emit_blocked_adoption_result(
                temp_root,
                write_artifact=False,
            )

            result = self.resolve_effective_object(temp_root, blocked_adoption)

            self.assert_current_effective_result(result)
            self.assert_effective_paths_match_current(temp_root, result, stack)
            non_effective = result["non_effective_preserved_families"]
            self.assertTrue(non_effective["prior_current_family_is_effective"])
            self.assertIsInstance(
                non_effective["adopted_successor_family_not_effective"],
                dict,
            )
            self.assertEqual(
                non_effective["adopted_successor_family_not_effective"]["outcome"],
                adoption_resolver.OUTCOME_BLOCKED,
            )
            self.assertTrue(
                non_effective["preserved_non_governing_runs_remain_preserved"]
            )
            self.assertIsInstance(non_effective["preserved_non_governing_runs"], list)

    def test_malformed_adoption_artifact_and_references_fail_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            path = temp_root / "malformed_adoption.json"
            path.write_text("[1, 2, 3]\n", encoding="utf-8")
            with self.assertRaises(effective_resolver.EffectiveFamilyResolutionError):
                self.resolve_effective_from_path(temp_root, path)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            adoption = self.copy_payload(stack["adoption_result"])
            adoption["adopted_family_references"]["adopted_status_packet_path"] = (
                "artifacts/missing_adopted_status_packet.json"
            )

            with self.assertRaises(effective_resolver.EffectiveFamilyResolutionError):
                self.resolve_effective_object(temp_root, adoption)

    def test_current_artifact_malformed_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(effective_resolver.EffectiveFamilyResolutionError):
                    effective_resolver.resolve_effective_current_family()

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
                        effective_resolver.EffectiveFamilyResolutionError
                    ):
                        self.resolve_effective_object(
                            temp_root,
                            stack["adoption_result"],
                        )

    def test_mismatch_between_current_and_adopted_family_fails_clearly(self) -> None:
        cases = (
            (
                "canonical_core_mismatch",
                "adopted_family_packet_path",
                lambda payload, stack: payload["canonical_execution_line"].__setitem__(
                    "core_execution_file",
                    "src/not_the_current_core.py",
                ),
            ),
            (
                "selected_successor_reference_mismatch",
                "adoption_result",
                lambda payload, stack: payload["selected_successor_family"].__setitem__(
                    "successor_family_packet_path",
                    "artifacts/not_the_selected_successor_family.json",
                ),
            ),
            (
                "adoption_non_claim_shortcut",
                "adoption_result",
                lambda payload, stack: payload["non_claims"].__setitem__(
                    "continuity_completed",
                    True,
                ),
            ),
            (
                "adopted_family_non_claim_shortcut",
                "adopted_status_packet_path",
                lambda payload, stack: payload["non_claims"].__setitem__(
                    "standing_upgraded",
                    True,
                ),
            ),
        )
        for label, target, mutate in cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(temp_root)
                    adoption = self.copy_payload(stack["adoption_result"])
                    if target == "adoption_result":
                        mutate(adoption, stack)
                    else:
                        artifact_path = self.resolve_display_path(
                            temp_root,
                            adoption["adopted_family_references"][target],
                        )
                        artifact = self.read_json(artifact_path)
                        mutate(artifact, stack)
                        self.write_json(artifact_path, artifact)

                    with self.assertRaises(
                        effective_resolver.EffectiveFamilyResolutionError
                    ):
                        self.resolve_effective_object(temp_root, adoption)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root
                / effective_resolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / effective_resolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root
                / effective_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root
                / effective_resolver.CURRENT_GOVERNING_PACKET_ROOT,
                "transition": temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT,
                "reresolution": temp_root / reresolver.GOVERNING_RERESOLUTION_ROOT,
                "adoption": temp_root
                / effective_resolver.GOVERNING_SUCCESSOR_ADOPTION_ROOT,
            }
            before = {label: self.json_texts(root) for label, root in roots.items()}

            first = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )
            after_first = {
                label: self.json_texts(root) for label, root in roots.items()
            }
            second = self.resolve_effective_from_path(temp_root, stack["adoption_path"])
            after_second = {
                label: self.json_texts(root) for label, root in roots.items()
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(first["canonical_execution_line"], second["canonical_execution_line"])
            self.assertEqual(first["prior_current_family"], second["prior_current_family"])
            self.assertEqual(first["effective_family"], second["effective_family"])
            self.assertEqual(first["non_effective_preserved_families"], second["non_effective_preserved_families"])
            self.assertEqual(first["non_claims"], second["non_claims"])

    def test_write_behavior_and_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            result = self.resolve_effective_object(
                temp_root,
                stack["adoption_result"],
            )
            output_path = temp_root / "nested" / "effective" / "result.json"

            with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
                written = effective_resolver.write_effective_family_resolution(
                    result,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    effective_resolver.EffectiveFamilyResolutionError
                ):
                    effective_resolver.write_effective_family_resolution(
                        result,
                        output_path,
                    )

            with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
                default_path = effective_resolver.write_effective_family_resolution(
                    result
                )
                with self.assertRaises(
                    effective_resolver.EffectiveFamilyResolutionError
                ):
                    effective_resolver.write_effective_family_resolution(result)

            self.assertTrue(default_path.exists())
            self.assertEqual(default_path.name, "current_effective_family_resolution.json")
            self.assert_under_effective_root(temp_root, default_path)
            default_parsed = self.read_json(default_path)
            self.assertEqual(set(default_parsed), EXPECTED_TOP_LEVEL_KEYS)


if __name__ == "__main__":
    unittest.main()
