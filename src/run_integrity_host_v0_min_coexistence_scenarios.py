"""Bounded scenario runner for the v0-min coexistence successor host.

This script emits a small fixed set of JSON scenario artifacts from the
current in-memory coexistence host and snapshot/export layer. It exists to make
the runnable mechanism inspectable as local engineering output.

The emitted artifacts are not protocol law, registry state, persistence
architecture, replay input, distributed synchronization, or a CLI framework.
Each scenario uses a fresh host and preserves the full exported snapshot rather
than reducing the trace to summaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from integrity_host_v0_min_coexistence_snapshot import build_snapshot, snapshot_to_json
from integrity_host_v0_min_coexistence_v2 import (
    ConformanceResult,
    IntegrityHostV0MinCoexistenceV2,
)


ARTIFACT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")


@dataclass(frozen=True)
class ScenarioResult:
    """Internal scenario result before artifact writing."""

    scenario_id: str
    scenario_name: str
    description: str
    host: IntegrityHostV0MinCoexistenceV2
    action_results: tuple[dict[str, object], ...]


@dataclass(frozen=True)
class EmittedScenario:
    """Manifest-facing description of one emitted scenario artifact."""

    scenario_id: str
    scenario_name: str
    description: str
    artifact_path: Path


ScenarioFunction = Callable[[], ScenarioResult]


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _utc_path_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _make_output_dir() -> Path:
    base_dir = _repo_root() / ARTIFACT_ROOT
    base_dir.mkdir(parents=True, exist_ok=True)

    stem = f"run_{_utc_path_stamp()}"
    candidate = base_dir / stem
    if not candidate.exists():
        candidate.mkdir(parents=False, exist_ok=False)
        return candidate

    for suffix in range(1, 1000):
        candidate = base_dir / f"{stem}_{suffix:03d}"
        if not candidate.exists():
            candidate.mkdir(parents=False, exist_ok=False)
            return candidate

    raise RuntimeError("Could not allocate a fresh scenario artifact directory")


def _write_json(path: Path, payload: dict[str, object]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite existing artifact: {path}")
    path.write_text(snapshot_to_json(payload), encoding="utf-8")
    return path


def _record_action(
    actions: list[dict[str, object]],
    label: str,
    result: ConformanceResult,
    *,
    expected_accepted: bool,
) -> ConformanceResult:
    if result.accepted is not expected_accepted:
        outcome = "accepted" if expected_accepted else "refused"
        raise RuntimeError(f"{label} was expected to be {outcome}")

    actions.append(
        {
            "label": label,
            "accepted": result.accepted,
            "state_changed": result.state_changed,
            "record_id": result.record_id,
            "object_id": result.object_id,
            "successor_object_id": result.successor_object_id,
            "refusal_code": (
                result.refusal_code.value if result.refusal_code is not None else None
            ),
        }
    )
    return result


def _require_object_id(result: ConformanceResult, label: str) -> str:
    if result.object_id is None:
        raise RuntimeError(f"{label} did not return an object id")
    return result.object_id


def _require_successor_id(result: ConformanceResult, label: str) -> str:
    if result.successor_object_id is None:
        raise RuntimeError(f"{label} did not return a successor object id")
    return result.successor_object_id


def scenario_lawful_distinct_matter_coexistence() -> ScenarioResult:
    actions: list[dict[str, object]] = []
    host = IntegrityHostV0MinCoexistenceV2("scenario-lawful-coexistence")

    create_a = _record_action(
        actions,
        "create object A",
        host.create_object("matter-a", "payload-a", basis_ref="create-a"),
        expected_accepted=True,
    )
    object_a = _require_object_id(create_a, "create object A")

    create_b = _record_action(
        actions,
        "create object B with explicit cohost basis",
        host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-b",
            cohost_basis_by_open_object_id={object_a: "cohost-a-b"},
        ),
        expected_accepted=True,
    )
    object_b = _require_object_id(create_b, "create object B")

    _record_action(
        actions,
        "present object A",
        host.present(object_a, "occurrence-a", "present-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "stand object A",
        host.stand(object_a, "threshold-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "present object B",
        host.present(object_b, "occurrence-b", "present-b"),
        expected_accepted=True,
    )

    return ScenarioResult(
        scenario_id="lawful_distinct_matter_coexistence",
        scenario_name="Lawful Distinct-Matter Coexistence",
        description=(
            "Creates two distinct-matter open objects with explicit pairwise "
            "cohost marking, then moves them independently through presentation."
        ),
        host=host,
        action_results=tuple(actions),
    )


def scenario_refused_missing_coexistence_basis() -> ScenarioResult:
    actions: list[dict[str, object]] = []
    host = IntegrityHostV0MinCoexistenceV2("scenario-missing-cohost-basis")

    create_a = _record_action(
        actions,
        "create object A",
        host.create_object("matter-a", "payload-a", basis_ref="create-a"),
        expected_accepted=True,
    )
    _require_object_id(create_a, "create object A")

    _record_action(
        actions,
        "attempt object B without required cohost basis",
        host.create_object("matter-b", "payload-b", basis_ref="create-b"),
        expected_accepted=False,
    )

    return ScenarioResult(
        scenario_id="refused_missing_coexistence_basis",
        scenario_name="Refused Missing Coexistence Basis",
        description=(
            "Shows that distinct matter strings alone do not authorize "
            "unresolved coexistence without explicit relation basis."
        ),
        host=host,
        action_results=tuple(actions),
    )


def scenario_evolve_under_coexistence() -> ScenarioResult:
    actions: list[dict[str, object]] = []
    host = IntegrityHostV0MinCoexistenceV2("scenario-evolve-under-coexistence")

    create_a = _record_action(
        actions,
        "create object A",
        host.create_object("matter-a", "payload-a", basis_ref="create-a"),
        expected_accepted=True,
    )
    object_a = _require_object_id(create_a, "create object A")

    create_b = _record_action(
        actions,
        "create object B with explicit cohost basis",
        host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-b",
            cohost_basis_by_open_object_id={object_a: "cohost-a-b"},
        ),
        expected_accepted=True,
    )
    object_b = _require_object_id(create_b, "create object B")

    _record_action(
        actions,
        "present object A",
        host.present(object_a, "occurrence-a", "present-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "stand object A",
        host.stand(object_a, "threshold-a"),
        expected_accepted=True,
    )
    evolve_a = _record_action(
        actions,
        "evolve object A with cohost basis for object B",
        host.evolve(
            object_a,
            "payload-a-successor",
            "evolve-a",
            cohost_basis_by_open_object_id={object_b: "cohost-successor-a-b"},
        ),
        expected_accepted=True,
    )
    _require_successor_id(evolve_a, "evolve object A")

    return ScenarioResult(
        scenario_id="evolve_under_coexistence",
        scenario_name="EVOLVE Under Coexistence",
        description=(
            "Moves one cohosted object to standing and evolves it while "
            "preserving predecessor/successor lineage and relation marking "
            "against the remaining open object."
        ),
        host=host,
        action_results=tuple(actions),
    )


def scenario_hold_blocks_one_target_while_another_proceeds() -> ScenarioResult:
    actions: list[dict[str, object]] = []
    host = IntegrityHostV0MinCoexistenceV2("scenario-target-specific-hold")

    create_a = _record_action(
        actions,
        "create object A",
        host.create_object("matter-a", "payload-a", basis_ref="create-a"),
        expected_accepted=True,
    )
    object_a = _require_object_id(create_a, "create object A")

    create_b = _record_action(
        actions,
        "create object B with explicit cohost basis",
        host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-b",
            cohost_basis_by_open_object_id={object_a: "cohost-a-b"},
        ),
        expected_accepted=True,
    )
    object_b = _require_object_id(create_b, "create object B")

    _record_action(
        actions,
        "present object A",
        host.present(object_a, "occurrence-a", "present-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "present object B",
        host.present(object_b, "occurrence-b", "present-b"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "set HOLD on object A",
        host.set_hold(object_a, "hold-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "attempt STAND on held object A",
        host.stand(object_a, "threshold-a"),
        expected_accepted=False,
    )
    _record_action(
        actions,
        "stand unheld object B",
        host.stand(object_b, "threshold-b"),
        expected_accepted=True,
    )

    return ScenarioResult(
        scenario_id="hold_blocks_one_target_while_another_proceeds",
        scenario_name="HOLD Blocks One Target While Another Proceeds",
        description=(
            "Demonstrates target-specific HOLD: the held object refuses "
            "standing while the unrelated cohosted object can still stand."
        ),
        host=host,
        action_results=tuple(actions),
    )


def scenario_same_matter_post_resolution_refusal() -> ScenarioResult:
    actions: list[dict[str, object]] = []
    host = IntegrityHostV0MinCoexistenceV2("scenario-same-matter-post-resolution")

    create_a = _record_action(
        actions,
        "create object A",
        host.create_object("matter-a", "payload-a", basis_ref="create-a"),
        expected_accepted=True,
    )
    object_a = _require_object_id(create_a, "create object A")

    _record_action(
        actions,
        "present object A",
        host.present(object_a, "occurrence-a", "present-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "stand object A",
        host.stand(object_a, "threshold-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "finalize object A",
        host.finalize(object_a, "finalize-a"),
        expected_accepted=True,
    )
    _record_action(
        actions,
        "attempt fresh same-matter creation after FINALIZE",
        host.create_object("matter-a", "payload-a-fresh", basis_ref="create-a-fresh"),
        expected_accepted=False,
    )

    return ScenarioResult(
        scenario_id="same_matter_post_resolution_refusal",
        scenario_name="Same-Matter Post-Resolution Refusal",
        description=(
            "Shows that fresh same-matter creation after FINALIZE is refused "
            "because this slice keeps EVOLVE as the only same-matter successor path."
        ),
        host=host,
        action_results=tuple(actions),
    )


SCENARIOS: tuple[tuple[str, ScenarioFunction], ...] = (
    ("01_lawful_distinct_matter_coexistence", scenario_lawful_distinct_matter_coexistence),
    ("02_refused_missing_coexistence_basis", scenario_refused_missing_coexistence_basis),
    ("03_evolve_under_coexistence", scenario_evolve_under_coexistence),
    (
        "04_hold_blocks_one_target_while_another_proceeds",
        scenario_hold_blocks_one_target_while_another_proceeds,
    ),
    ("05_same_matter_post_resolution_refusal", scenario_same_matter_post_resolution_refusal),
)


def _build_scenario_artifact(result: ScenarioResult) -> dict[str, object]:
    accepted_count = sum(1 for action in result.action_results if action["accepted"])
    refused_count = len(result.action_results) - accepted_count

    return {
        "scenario": {
            "scenario_id": result.scenario_id,
            "scenario_name": result.scenario_name,
            "description": result.description,
            "generated_at": _utc_timestamp(),
            "accepted_action_count": accepted_count,
            "refused_action_count": refused_count,
            "action_results": list(result.action_results),
        },
        "snapshot": build_snapshot(result.host),
    }


def _emit_scenario(
    output_dir: Path,
    file_stem: str,
    scenario_function: ScenarioFunction,
) -> EmittedScenario:
    try:
        result = scenario_function()
    except Exception as exc:
        raise RuntimeError(f"Scenario failed: {file_stem}") from exc

    artifact_path = output_dir / f"{file_stem}.json"
    _write_json(artifact_path, _build_scenario_artifact(result))
    return EmittedScenario(
        scenario_id=result.scenario_id,
        scenario_name=result.scenario_name,
        description=result.description,
        artifact_path=artifact_path,
    )


def _build_manifest(
    output_dir: Path,
    emitted_scenarios: tuple[EmittedScenario, ...],
) -> dict[str, object]:
    return {
        "generated_at": _utc_timestamp(),
        "output_directory": _display_path(output_dir),
        "scenario_count": len(emitted_scenarios),
        "scenarios": [
            {
                "scenario_id": scenario.scenario_id,
                "scenario_name": scenario.scenario_name,
                "description": scenario.description,
                "file_path": _display_path(scenario.artifact_path),
            }
            for scenario in emitted_scenarios
        ],
    }


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    root = _repo_root()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return resolved.as_posix()


def main() -> None:
    output_dir = _make_output_dir()
    emitted = tuple(
        _emit_scenario(output_dir, file_stem, scenario_function)
        for file_stem, scenario_function in SCENARIOS
    )

    manifest_path = output_dir / "manifest.json"
    _write_json(manifest_path, _build_manifest(output_dir, emitted))

    print(f"Output directory: {_display_path(output_dir)}")
    print(f"Scenarios emitted: {len(emitted)}")
    for scenario in emitted:
        print(f"- {scenario.scenario_id}: {_display_path(scenario.artifact_path)}")
    print(f"Manifest: {_display_path(manifest_path)}")


if __name__ == "__main__":
    main()
