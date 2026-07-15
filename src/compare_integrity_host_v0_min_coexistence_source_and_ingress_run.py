"""Bounded source-to-ingress-run comparison for v0-min coexistence artifacts.

This runner compares one emitted source scenario run with one run-level
receiving-ingress output. It checks that the ingress run points back to the
selected source run, compares load-bearing scenario and aggregate counts, and
preserves bounded visibility of receiving status, validation, decisions,
refusals, HOLD, coexistence, and lineage-relevant counts where they are exposed.

The comparison artifact is additive engineering output only. It does not replay
source actions into a host, merge ingress artifacts, define persistence or
registry law, complete continuity, or become a generic diff engine.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
INGRESS_RUNS_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiving_ingress_runs"
)
COMPARISON_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_source_ingress_comparisons"
)

COMPARISON_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SOURCE_INGRESS_RUN_COMPARISON"
COMPARISON_VERSION = "0.1.0"

BASE_COUNT_KEYS = (
    "object_count",
    "open_object_count",
    "coexistence_relation_count",
    "hold_count",
    "transition_record_count",
    "refusal_count",
    "accepted_action_count",
    "refused_action_count",
)

LINEAGE_COUNT_KEYS = (
    "resolved_object_count",
    "successor_object_count",
    "evolve_record_count",
)

COUNT_KEYS = (*BASE_COUNT_KEYS, *LINEAGE_COUNT_KEYS)

NON_CLAIM_KEYS = (
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
)


def find_latest_source_run_directory(root: Path) -> Path:
    """Return the lexically latest source ``run_*`` directory under ``root``."""

    return _find_latest_run_directory(root, "source")


def find_latest_ingress_run_directory(root: Path) -> Path:
    """Return the lexically latest ingress ``run_*`` directory under ``root``."""

    return _find_latest_run_directory(root, "ingress")


def read_source_manifest(run_dir: Path) -> dict[str, Any]:
    """Read and validate the bounded source run manifest."""

    run_path = _repo_relative_path(run_dir)
    manifest_path = run_path / "manifest.json"
    manifest = _read_json_object(manifest_path, "source manifest")
    _validate_source_manifest(manifest)
    return manifest


def read_ingress_manifest(run_dir: Path) -> dict[str, Any]:
    """Read and validate the bounded receiving-ingress run manifest."""

    run_path = _repo_relative_path(run_dir)
    manifest_path = run_path / "manifest.json"
    manifest = _read_json_object(manifest_path, "ingress manifest")
    _validate_ingress_manifest(manifest)
    return manifest


def compare_source_run_and_ingress_run(
    source_run_dir: Path,
    ingress_run_dir: Path,
) -> dict[str, Any]:
    """Compare one source run with one corresponding receiving-ingress run."""

    source_run_path = _repo_relative_path(source_run_dir)
    ingress_run_path = _repo_relative_path(ingress_run_dir)
    source_manifest = read_source_manifest(source_run_path)
    ingress_manifest = read_ingress_manifest(ingress_run_path)

    _verify_source_ingress_correspondence(
        source_run_path,
        source_manifest,
        ingress_run_path,
        ingress_manifest,
    )

    scenario_comparisons = _scenario_comparisons(
        source_manifest,
        ingress_manifest,
        source_run_path,
        ingress_run_path,
    )
    aggregate_comparison = _aggregate_comparison(
        source_manifest,
        ingress_manifest,
        scenario_comparisons,
    )
    all_matched = aggregate_comparison["aggregate_match"] and all(
        comparison["matched"] for comparison in scenario_comparisons
    )

    return {
        "comparison_metadata": {
            "comparison_type": COMPARISON_TYPE,
            "comparison_version": COMPARISON_VERSION,
            "generated_at": _utc_timestamp(),
            "comparator_module": __name__,
        },
        "source_run": {
            "source_run_directory_path": _display_path(source_run_path),
            "source_manifest_path": _display_path(source_run_path / "manifest.json"),
            "source_scenario_count": _require_int(
                source_manifest,
                "scenario_count",
                "source manifest",
            ),
        },
        "ingress_run": {
            "ingress_run_directory_path": _display_path(ingress_run_path),
            "ingress_manifest_path": _display_path(ingress_run_path / "manifest.json"),
            "ingress_scenario_count": _require_int(
                _require_mapping(
                    ingress_manifest,
                    "aggregate_counts",
                    "ingress manifest",
                ),
                "scenario_count",
                "ingress manifest.aggregate_counts",
            ),
            "source_run_directory_path_recorded": _require_string(
                _require_mapping(
                    ingress_manifest,
                    "source_run",
                    "ingress manifest",
                ),
                "source_run_directory_path",
                "ingress manifest.source_run",
            ),
        },
        "scenario_comparisons": scenario_comparisons,
        "aggregate_comparison": aggregate_comparison,
        "all_matched": all_matched,
    }


def write_comparison(comparison: dict[str, Any], output_path: Path) -> Path:
    """Write one UTF-8 JSON source-to-ingress comparison without overwriting."""

    path = _repo_relative_path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite comparison artifact: {_display_path(path)}")
    path.write_text(_json_text(comparison), encoding="utf-8")
    return path


def main() -> None:
    """Compare the latest source run and latest ingress run."""

    source_run_dir = find_latest_source_run_directory(SOURCE_RUNS_ROOT)
    ingress_run_dir = find_latest_ingress_run_directory(INGRESS_RUNS_ROOT)
    comparison = compare_source_run_and_ingress_run(source_run_dir, ingress_run_dir)
    output_path = _next_comparison_output_path(source_run_dir)
    written = write_comparison(comparison, output_path)

    print(f"Source run: {_display_path(source_run_dir)}")
    print(f"Ingress run: {_display_path(ingress_run_dir)}")
    print(f"Scenarios compared: {comparison['source_run']['source_scenario_count']}")
    print(f"Mismatches: {_mismatch_count(comparison)}")
    print(f"All matched: {comparison['all_matched']}")
    print(f"Comparison artifact: {_display_path(written)}")


def _find_latest_run_directory(root: Path, label: str) -> Path:
    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise RuntimeError(f"{label.title()} run root does not exist: {_display_path(root_path)}")
    if not root_path.is_dir():
        raise RuntimeError(f"{label.title()} run root is not a directory: {_display_path(root_path)}")

    run_dirs = sorted(
        path
        for path in root_path.iterdir()
        if path.is_dir() and path.name.startswith("run_")
    )
    if not run_dirs:
        raise RuntimeError(f"No {label} run directories found under: {_display_path(root_path)}")
    return run_dirs[-1]


def _verify_source_ingress_correspondence(
    source_run_path: Path,
    source_manifest: Mapping[str, Any],
    ingress_run_path: Path,
    ingress_manifest: Mapping[str, Any],
) -> None:
    ingress_source = _require_mapping(
        ingress_manifest,
        "source_run",
        "ingress manifest",
    )
    recorded_source_run = _require_string(
        ingress_source,
        "source_run_directory_path",
        "ingress manifest.source_run",
    )
    recorded_source_manifest = _require_string(
        ingress_source,
        "source_manifest_path",
        "ingress manifest.source_run",
    )

    if not _path_text_matches(
        recorded_source_run,
        source_run_path,
        base_dir=ingress_run_path,
    ):
        raise RuntimeError("Ingress run does not reference the selected source run")
    if not _path_text_matches(
        recorded_source_manifest,
        source_run_path / "manifest.json",
        base_dir=ingress_run_path,
    ):
        raise RuntimeError("Ingress run does not reference the selected source manifest")

    source_count = _require_int(source_manifest, "scenario_count", "source manifest")
    ingress_source_count = _require_int(
        ingress_source,
        "source_scenario_count",
        "ingress manifest.source_run",
    )
    if source_count != ingress_source_count:
        raise RuntimeError("Ingress source scenario count does not match source manifest")


def _scenario_comparisons(
    source_manifest: Mapping[str, Any],
    ingress_manifest: Mapping[str, Any],
    source_run_path: Path,
    ingress_run_path: Path,
) -> list[dict[str, Any]]:
    source_scenarios = _scenario_entries(source_manifest, "source manifest")
    ingress_entries = _ingress_entries_by_id(ingress_manifest)
    source_ids = {
        _require_string(item, "scenario_id", "source manifest.scenarios[]")
        for item in source_scenarios
    }
    ingress_ids = set(ingress_entries)
    if source_ids != ingress_ids:
        raise RuntimeError(
            "Source and ingress scenario coverage do not match: "
            f"source={sorted(source_ids)}, ingress={sorted(ingress_ids)}"
        )

    comparisons: list[dict[str, Any]] = []
    for index, source_entry in enumerate(source_scenarios):
        context = f"source manifest.scenarios[{index}]"
        scenario_id = _require_string(source_entry, "scenario_id", context)
        source_artifact_path = _resolve_path_text(
            _require_string(source_entry, "file_path", context),
            base_dir=source_run_path,
        )
        source_artifact = _read_source_artifact(source_artifact_path)
        _validate_source_entry_matches_artifact(source_entry, source_artifact)
        comparisons.append(
            _compare_scenario(
                source_entry,
                source_artifact,
                source_artifact_path,
                ingress_entries[scenario_id],
                ingress_run_path,
            )
        )
    return comparisons


def _compare_scenario(
    source_entry: Mapping[str, Any],
    source_artifact: Mapping[str, Any],
    source_artifact_path: Path,
    ingress_entry: Mapping[str, Any],
    ingress_run_path: Path,
) -> dict[str, Any]:
    mismatches: list[str] = []
    source_scenario = _require_mapping(
        source_artifact,
        "scenario",
        "source artifact",
    )
    source_id = _require_string(source_scenario, "scenario_id", "source artifact.scenario")
    source_name = _require_string(
        source_scenario,
        "scenario_name",
        "source artifact.scenario",
    )
    source_description = _require_string(
        source_scenario,
        "description",
        "source artifact.scenario",
    )

    if _require_string(ingress_entry, "scenario_id", "ingress entry") != source_id:
        mismatches.append("scenario_id mismatch")
    if _require_string(ingress_entry, "scenario_name", "ingress entry") != source_name:
        mismatches.append("scenario_name mismatch")
    if _require_string(ingress_entry, "description", "ingress entry") != source_description:
        mismatches.append("description mismatch")
    if _require_string(source_entry, "description", "source manifest entry") != source_description:
        mismatches.append("source manifest description mismatch")

    source_counts = _source_counts(source_artifact)
    ingress_decision_path = _resolve_path_text(
        _require_string(
            ingress_entry,
            "ingress_decision_path",
            "ingress entry",
        ),
        base_dir=ingress_run_path,
    )
    ingress_decision_artifact = _read_json_object(
        ingress_decision_path,
        "ingress decision artifact",
    )
    ingress_counts = _ingress_counts(ingress_entry, ingress_decision_artifact)
    count_comparison = _compare_counts(
        source_counts,
        ingress_counts,
        COUNT_KEYS,
        mismatches,
    )
    visibility_comparison = _visibility_comparison(
        source_artifact_path,
        source_counts,
        ingress_entry,
        ingress_run_path,
        ingress_decision_artifact,
        mismatches,
    )
    non_claim_comparison = _non_claim_comparison(
        ingress_entry,
        ingress_decision_artifact,
        mismatches,
    )

    return {
        "scenario_id": source_id,
        "scenario_name": source_name,
        "source_artifact_path": _display_path(source_artifact_path),
        "ingress_receiving_packet_path": _require_string(
            ingress_entry,
            "receiving_packet_path",
            "ingress entry",
        ),
        "ingress_decision_path": _require_string(
            ingress_entry,
            "ingress_decision_path",
            "ingress entry",
        ),
        "matched": not mismatches,
        "mismatches": mismatches,
        "counts": count_comparison,
        "visibility": visibility_comparison,
        "non_claims": non_claim_comparison,
    }


def _aggregate_comparison(
    source_manifest: Mapping[str, Any],
    ingress_manifest: Mapping[str, Any],
    scenario_comparisons: list[dict[str, Any]],
) -> dict[str, Any]:
    ingress_aggregate = _require_mapping(
        ingress_manifest,
        "aggregate_counts",
        "ingress manifest",
    )
    source_totals = {
        "scenario_count": _require_int(source_manifest, "scenario_count", "source manifest")
    }
    ingress_totals = {
        "scenario_count": _require_int(
            ingress_aggregate,
            "scenario_count",
            "ingress manifest.aggregate_counts",
        )
    }

    for key in COUNT_KEYS:
        source_totals[key] = sum(
            _require_int(comparison["counts"][key], "source", f"{key} comparison")
            for comparison in scenario_comparisons
        )
        ingress_totals[key] = sum(
            _require_int(comparison["counts"][key], "ingress", f"{key} comparison")
            for comparison in scenario_comparisons
        )

    aggregate_fields = (
        "validation_passed_scenario_count",
        "validation_failed_scenario_count",
        "ingress_accepted_scenario_count",
        "ingress_rejected_scenario_count",
    )
    for key in aggregate_fields:
        ingress_totals[key] = _require_int(
            ingress_aggregate,
            key,
            "ingress manifest.aggregate_counts",
        )

    mismatches: list[str] = []
    count_comparison = _compare_counts(
        source_totals,
        ingress_totals,
        ("scenario_count", *COUNT_KEYS),
        mismatches,
    )
    for key in BASE_COUNT_KEYS:
        aggregate_value = _require_int(
            ingress_aggregate,
            key,
            "ingress manifest.aggregate_counts",
        )
        if aggregate_value != ingress_totals[key]:
            mismatches.append(
                f"ingress aggregate {key} mismatch: "
                f"manifest={aggregate_value}, entries={ingress_totals[key]}"
            )

    counts_match = all(item["matched"] for item in count_comparison.values())
    run_status = _run_status_comparison(ingress_manifest, mismatches)
    aggregate_match = counts_match and run_status["matched"] and not mismatches

    return {
        "source_totals": source_totals,
        "ingress_totals": ingress_totals,
        "counts_match": counts_match,
        "run_status": run_status,
        "aggregate_match": aggregate_match,
        "mismatches": mismatches,
        "counts": count_comparison,
    }


def _source_counts(source_artifact: Mapping[str, Any]) -> dict[str, int]:
    scenario = _require_mapping(source_artifact, "scenario", "source artifact")
    snapshot = _require_mapping(source_artifact, "snapshot", "source artifact")
    host = _require_mapping(snapshot, "host", "source artifact.snapshot")
    objects = _require_list(snapshot, "objects", "source artifact.snapshot")
    relations = _require_list(
        snapshot,
        "coexistence_relations",
        "source artifact.snapshot",
    )
    holds = _require_list(snapshot, "holds", "source artifact.snapshot")
    records = _require_list(snapshot, "transition_records", "source artifact.snapshot")

    return {
        "object_count": len(objects),
        "open_object_count": len(
            _require_list(host, "open_object_ids", "source artifact.snapshot.host")
        ),
        "coexistence_relation_count": len(relations),
        "hold_count": len(holds),
        "transition_record_count": len(records),
        "refusal_count": sum(1 for record in records if not _record_accepted(record)),
        "accepted_action_count": _require_int(
            scenario,
            "accepted_action_count",
            "source artifact.scenario",
        ),
        "refused_action_count": _require_int(
            scenario,
            "refused_action_count",
            "source artifact.scenario",
        ),
        "resolved_object_count": sum(
            1 for obj in objects if _optional_field(obj, "resolution_type") is not None
        ),
        "successor_object_count": sum(
            1
            for obj in objects
            if _optional_field(obj, "predecessor_object_id") is not None
        ),
        "evolve_record_count": sum(
            1 for record in records if _string_field(record, "action_type") == "EVOLVE"
        ),
    }


def _ingress_counts(
    ingress_entry: Mapping[str, Any],
    ingress_decision_artifact: Mapping[str, Any],
) -> dict[str, int]:
    receiving_packet = _require_mapping(
        ingress_decision_artifact,
        "receiving_packet",
        "ingress decision artifact",
    )
    imported_packet = _require_mapping(
        receiving_packet,
        "imported_packet",
        "ingress decision artifact.receiving_packet",
    )
    objects = _require_list(
        imported_packet,
        "objects",
        "ingress decision artifact.receiving_packet.imported_packet",
    )
    records = _require_list(
        imported_packet,
        "transition_records",
        "ingress decision artifact.receiving_packet.imported_packet",
    )

    return {
        "object_count": _require_int(ingress_entry, "object_count", "ingress entry"),
        "open_object_count": _require_int(
            ingress_entry,
            "open_object_count",
            "ingress entry",
        ),
        "coexistence_relation_count": _require_int(
            ingress_entry,
            "coexistence_relation_count",
            "ingress entry",
        ),
        "hold_count": _require_int(ingress_entry, "hold_count", "ingress entry"),
        "transition_record_count": _require_int(
            ingress_entry,
            "transition_record_count",
            "ingress entry",
        ),
        "refusal_count": _require_int(ingress_entry, "refusal_count", "ingress entry"),
        "accepted_action_count": _require_int(
            ingress_entry,
            "accepted_action_count",
            "ingress entry",
        ),
        "refused_action_count": _require_int(
            ingress_entry,
            "refused_action_count",
            "ingress entry",
        ),
        "resolved_object_count": sum(
            1 for obj in objects if _optional_field(obj, "resolution_type") is not None
        ),
        "successor_object_count": sum(
            1
            for obj in objects
            if _optional_field(obj, "predecessor_object_id") is not None
        ),
        "evolve_record_count": sum(
            1 for record in records if _string_field(record, "action_type") == "EVOLVE"
        ),
    }


def _compare_counts(
    source_counts: Mapping[str, Any],
    ingress_counts: Mapping[str, Any],
    keys: tuple[str, ...],
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    compared: dict[str, dict[str, Any]] = {}
    for key in keys:
        source_value = _require_plain_int(source_counts.get(key), f"source.{key}")
        if key not in ingress_counts:
            raise RuntimeError(f"Ingress count is missing: {key}")
        ingress_value = _require_plain_int(ingress_counts[key], f"ingress.{key}")
        matched = source_value == ingress_value
        if not matched:
            mismatches.append(
                f"{key} mismatch: source={source_value}, ingress={ingress_value}"
            )
        compared[key] = {
            "source": source_value,
            "ingress": ingress_value,
            "matched": matched,
        }
    return compared


def _visibility_comparison(
    source_artifact_path: Path,
    source_counts: Mapping[str, int],
    ingress_entry: Mapping[str, Any],
    ingress_run_path: Path,
    ingress_decision_artifact: Mapping[str, Any],
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    packet_path = _resolve_path_text(
        _require_string(ingress_entry, "receiving_packet_path", "ingress entry"),
        base_dir=ingress_run_path,
    )
    decision_path = _resolve_path_text(
        _require_string(ingress_entry, "ingress_decision_path", "ingress entry"),
        base_dir=ingress_run_path,
    )
    validation_summary = _require_mapping(
        ingress_entry,
        "validation_summary",
        "ingress entry",
    )
    ingress_decision_summary = _require_mapping(
        ingress_entry,
        "ingress_decision_summary",
        "ingress entry",
    )
    receiving_status = _require_mapping(
        ingress_entry,
        "receiving_status",
        "ingress entry",
    )
    validation_result = _require_mapping(
        ingress_decision_artifact,
        "validation_result",
        "ingress decision artifact",
    )
    visibility_checks = _require_mapping(
        validation_result,
        "visibility_checks",
        "ingress decision artifact.validation_result",
    )

    checks = {
        "source_artifact_path_visible": _path_text_matches(
            _require_string(ingress_entry, "source_artifact_path", "ingress entry"),
            source_artifact_path,
            base_dir=ingress_run_path,
        ),
        "receiving_packet_path_present": packet_path.exists(),
        "ingress_decision_path_present": decision_path.exists(),
        "validation_summary_present": bool(validation_summary),
        "ingress_decision_summary_present": bool(ingress_decision_summary),
        "receiving_status_present": bool(receiving_status),
        "refusal_visibility_preserved": (
            source_counts["refusal_count"] == 0
            or _require_int(
                validation_summary,
                "refusal_count",
                "ingress entry.validation_summary",
            )
            > 0
        ),
        "lineage_visibility_preserved": (
            source_counts["successor_object_count"] == 0
            and source_counts["evolve_record_count"] == 0
        )
        or _lineage_visibility_check_matches(visibility_checks),
    }

    compared: dict[str, dict[str, Any]] = {}
    for key, matched in checks.items():
        if not matched:
            mismatches.append(f"{key} failed")
        compared[key] = {
            "matched": matched,
        }
    return compared


def _lineage_visibility_check_matches(visibility_checks: Mapping[str, Any]) -> bool:
    lineage = _require_mapping(
        visibility_checks,
        "predecessor_successor_lineage_visible",
        "visibility_checks",
    )
    return lineage.get("matched") is True and (
        _plain_int_or_zero(lineage.get("object_lineage_count")) > 0
        or _plain_int_or_zero(lineage.get("evolve_record_lineage_count")) > 0
    )


def _non_claim_comparison(
    ingress_entry: Mapping[str, Any],
    ingress_decision_artifact: Mapping[str, Any],
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    entry_status = _require_mapping(ingress_entry, "receiving_status", "ingress entry")
    decision_status = _require_mapping(
        ingress_decision_artifact,
        "receiving_status_carry_forward",
        "ingress decision artifact",
    )
    ingress_decision = _require_mapping(
        ingress_decision_artifact,
        "ingress_decision",
        "ingress decision artifact",
    )
    run_values = {
        "continuity_completed": False,
        "standing_upgraded": False,
        "replayed_into_live_host": False,
        "merged_into_local_state": False,
    }

    compared: dict[str, dict[str, Any]] = {}
    for key, expected in run_values.items():
        actual_values = {
            "receiving_status": entry_status.get(key),
            "decision_status": decision_status.get(key),
        }
        if key in ingress_decision:
            actual_values["ingress_decision"] = ingress_decision.get(key)
        matched = all(value is expected for value in actual_values.values())
        if not matched:
            mismatches.append(f"{key} non-claim mismatch")
        compared[key] = {
            "expected": expected,
            "actual": actual_values,
            "matched": matched,
        }
    return compared


def _run_status_comparison(
    ingress_manifest: Mapping[str, Any],
    mismatches: list[str],
) -> dict[str, Any]:
    run_status = _require_mapping(ingress_manifest, "run_status", "ingress manifest")
    expected = {
        "all_packets_built": True,
        "all_packets_validated": True,
        "all_decisions_emitted": True,
        "continuity_completed": False,
        "standing_upgraded": False,
        "replayed_into_live_host": False,
        "merged_into_local_state": False,
    }
    checks: dict[str, dict[str, Any]] = {}
    for key, expected_value in expected.items():
        actual = run_status.get(key)
        matched = actual is expected_value
        if not matched:
            mismatches.append(f"run_status.{key} mismatch")
        checks[key] = {
            "expected": expected_value,
            "actual": actual,
            "matched": matched,
        }
    return {
        "matched": all(item["matched"] for item in checks.values()),
        "checks": checks,
    }


def _read_source_artifact(path: Path) -> dict[str, Any]:
    artifact = _read_json_object(path, "source scenario artifact")
    scenario = _require_mapping(artifact, "scenario", "source artifact")
    snapshot = _require_mapping(artifact, "snapshot", "source artifact")
    _require_string(scenario, "scenario_id", "source artifact.scenario")
    _require_string(scenario, "scenario_name", "source artifact.scenario")
    _require_string(scenario, "description", "source artifact.scenario")
    _require_int(scenario, "accepted_action_count", "source artifact.scenario")
    _require_int(scenario, "refused_action_count", "source artifact.scenario")
    _require_list(scenario, "action_results", "source artifact.scenario")
    _require_mapping(snapshot, "host", "source artifact.snapshot")
    _require_list(snapshot, "objects", "source artifact.snapshot")
    _require_list(snapshot, "coexistence_relations", "source artifact.snapshot")
    _require_list(snapshot, "holds", "source artifact.snapshot")
    _require_list(snapshot, "transition_records", "source artifact.snapshot")
    return artifact


def _validate_source_entry_matches_artifact(
    source_entry: Mapping[str, Any],
    source_artifact: Mapping[str, Any],
) -> None:
    scenario = _require_mapping(source_artifact, "scenario", "source artifact")
    if _require_string(source_entry, "scenario_id", "source manifest entry") != _require_string(
        scenario,
        "scenario_id",
        "source artifact.scenario",
    ):
        raise RuntimeError("Source manifest/artifact scenario id mismatch")
    if _require_string(source_entry, "scenario_name", "source manifest entry") != _require_string(
        scenario,
        "scenario_name",
        "source artifact.scenario",
    ):
        raise RuntimeError("Source manifest/artifact scenario name mismatch")


def _validate_source_manifest(manifest: Mapping[str, Any]) -> None:
    _require_string(manifest, "generated_at", "source manifest")
    _require_string(manifest, "output_directory", "source manifest")
    scenario_count = _require_int(manifest, "scenario_count", "source manifest")
    scenarios = _require_list(manifest, "scenarios", "source manifest")
    if scenario_count != len(scenarios):
        raise RuntimeError("Malformed source manifest: scenario_count does not match scenarios")
    _validate_scenario_entries(scenarios, "source manifest")


def _validate_ingress_manifest(manifest: Mapping[str, Any]) -> None:
    _require_mapping(manifest, "ingress_run_metadata", "ingress manifest")
    source_run = _require_mapping(manifest, "source_run", "ingress manifest")
    entries = _require_list(manifest, "scenario_ingress_entries", "ingress manifest")
    aggregate = _require_mapping(manifest, "aggregate_counts", "ingress manifest")
    run_status = _require_mapping(manifest, "run_status", "ingress manifest")

    _require_string(source_run, "source_run_directory_path", "ingress manifest.source_run")
    _require_string(source_run, "source_manifest_path", "ingress manifest.source_run")
    _require_int(source_run, "source_scenario_count", "ingress manifest.source_run")
    _require_string(source_run, "source_generated_at", "ingress manifest.source_run")

    if _require_int(aggregate, "scenario_count", "ingress manifest.aggregate_counts") != len(entries):
        raise RuntimeError("Malformed ingress manifest: scenario_count does not match entries")

    for key in (*BASE_COUNT_KEYS, "scenario_count"):
        _require_int(aggregate, key, "ingress manifest.aggregate_counts")
    for key in (
        "validation_passed_scenario_count",
        "validation_failed_scenario_count",
        "ingress_accepted_scenario_count",
        "ingress_rejected_scenario_count",
    ):
        _require_int(aggregate, key, "ingress manifest.aggregate_counts")
    for key in (
        "all_packets_built",
        "all_packets_validated",
        "all_decisions_emitted",
        *NON_CLAIM_KEYS,
    ):
        _require_bool(run_status, key, "ingress manifest.run_status")

    _validate_ingress_entries(entries)


def _validate_scenario_entries(entries: list[Any], context: str) -> None:
    seen_ids: set[str] = set()
    for index, item in enumerate(entries):
        entry = _require_mapping(item, f"{context}.scenarios[{index}]")
        scenario_id = _require_string(entry, "scenario_id", f"{context}.scenarios[{index}]")
        if scenario_id in seen_ids:
            raise RuntimeError(f"Duplicate scenario id in {context}: {scenario_id}")
        seen_ids.add(scenario_id)
        _require_string(entry, "scenario_name", f"{context}.scenarios[{index}]")
        _require_string(entry, "description", f"{context}.scenarios[{index}]")
        _require_string(entry, "file_path", f"{context}.scenarios[{index}]")


def _validate_ingress_entries(entries: list[Any]) -> None:
    seen_ids: set[str] = set()
    for index, item in enumerate(entries):
        entry = _require_mapping(item, f"ingress manifest.entries[{index}]")
        scenario_id = _require_string(
            entry,
            "scenario_id",
            f"ingress manifest.entries[{index}]",
        )
        if scenario_id in seen_ids:
            raise RuntimeError(f"Duplicate ingress scenario id: {scenario_id}")
        seen_ids.add(scenario_id)
        for key in (
            "scenario_name",
            "description",
            "source_artifact_path",
            "receiving_packet_path",
            "ingress_decision_path",
            "ingress_decision",
            "ingress_decision_reason",
        ):
            _require_string(entry, key, f"ingress manifest.entries[{index}]")
        _require_bool(entry, "validation_passed", f"ingress manifest.entries[{index}]")
        for key in BASE_COUNT_KEYS:
            _require_int(entry, key, f"ingress manifest.entries[{index}]")
        _require_mapping(entry, "receiving_status", f"ingress manifest.entries[{index}]")
        _require_mapping(entry, "validation_summary", f"ingress manifest.entries[{index}]")
        _require_mapping(
            entry,
            "ingress_decision_summary",
            f"ingress manifest.entries[{index}]",
        )


def _scenario_entries(
    manifest: Mapping[str, Any],
    context: str,
) -> tuple[Mapping[str, Any], ...]:
    entries = _require_list(manifest, "scenarios", context)
    return tuple(_require_mapping(item, f"{context}.scenarios[]") for item in entries)


def _ingress_entries_by_id(manifest: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    entries = _require_list(manifest, "scenario_ingress_entries", "ingress manifest")
    by_id: dict[str, Mapping[str, Any]] = {}
    for item in entries:
        entry = _require_mapping(item, "ingress manifest.scenario_ingress_entries[]")
        scenario_id = _require_string(
            entry,
            "scenario_id",
            "ingress manifest.scenario_ingress_entries[]",
        )
        if scenario_id in by_id:
            raise RuntimeError(f"Duplicate ingress scenario id: {scenario_id}")
        by_id[scenario_id] = entry
    return by_id


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_relative_path(path)
    if not file_path.exists():
        raise RuntimeError(f"{label.title()} is missing: {_display_path(file_path)}")
    if not file_path.is_file():
        raise RuntimeError(f"{label.title()} path is not a file: {_display_path(file_path)}")
    try:
        parsed = json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{label.title()} is not valid JSON: {_display_path(file_path)}") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError(f"{label.title()} must be a JSON object")
    return parsed


def _next_comparison_output_path(source_run_dir: Path) -> Path:
    return (
        _repo_root()
        / COMPARISON_OUTPUT_ROOT
        / f"{_repo_relative_path(source_run_dir).name}__source_ingress_comparison.json"
    )


def _mismatch_count(comparison: Mapping[str, Any]) -> int:
    aggregate = _require_mapping(comparison, "aggregate_comparison", "comparison")
    scenario_comparisons = _require_list(
        comparison,
        "scenario_comparisons",
        "comparison",
    )
    return len(_require_list(aggregate, "mismatches", "aggregate comparison")) + sum(
        len(_require_list(item, "mismatches", "scenario comparison"))
        for item in scenario_comparisons
        if isinstance(item, Mapping)
    )


def _record_accepted(value: Any) -> bool:
    mapping = _require_mapping(value, "source artifact.snapshot.transition_records[]")
    return _require_bool(mapping, "accepted", "source artifact.snapshot.transition_records[]")


def _optional_field(value: Any, key: str) -> Any:
    mapping = _require_mapping(value, "object")
    return mapping.get(key)


def _string_field(value: Any, key: str) -> str:
    mapping = _require_mapping(value, "mapping")
    return _require_string(mapping, key, "mapping")


def _plain_int_or_zero(value: Any) -> int:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return 0


def _require_mapping(value: Any, context_or_key: str, context: str | None = None) -> Mapping[str, Any]:
    if context is None:
        if not isinstance(value, Mapping):
            raise RuntimeError(f"Malformed {context_or_key}: expected object")
        return value
    if not isinstance(value, Mapping):
        raise RuntimeError(f"Malformed {context}: expected object")
    item = value.get(context_or_key)
    if not isinstance(item, Mapping):
        raise RuntimeError(f"Malformed {context}: {context_or_key} must be an object")
    return item


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or value == "":
        raise RuntimeError(f"Malformed {context}: {key} must be a non-empty string")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be an integer")
    return value


def _require_plain_int(value: Any, context: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: expected integer")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be boolean")
    return value


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise RuntimeError(f"Malformed {context}: {key} must be a list")
    return value


def _resolve_path_text(path_text: str, *, base_dir: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()

    candidates = (
        (_repo_root() / path).resolve(),
        (Path.cwd() / path).resolve(),
        (base_dir / path).resolve(),
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def _path_text_matches(path_text: str, expected: Path, *, base_dir: Path) -> bool:
    expected_path = expected.resolve()
    resolved = _resolve_path_text(path_text, base_dir=base_dir)
    if resolved == expected_path:
        return True
    normalized = Path(path_text).as_posix()
    expected_text = expected_path.as_posix()
    return expected_text == normalized or expected_text.endswith(f"/{normalized}")


def _repo_relative_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (_repo_root() / path).resolve()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _display_path(path: Path) -> str:
    resolved = Path(path).resolve()
    root = _repo_root()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return resolved.as_posix()


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_ready(item) for item in value]
    if isinstance(value, tuple):
        return [_json_ready(item) for item in value]
    if isinstance(value, set):
        return sorted((_json_ready(item) for item in value), key=repr)
    if isinstance(value, Path):
        return _display_path(value)
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    return str(value)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    main()
