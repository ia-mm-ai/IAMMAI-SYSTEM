"""Bounded current execution-authority resolver for v0-min coexistence.

This module inspects preserved source runs, run-level receiving-ingress runs,
and source-to-ingress comparison artifacts. It resolves which preserved source
run, if any, is eligible to count as the current execution-authority run for
the present canonical core execution line:

    src/integrity_host_v0_min_coexistence_v2.py

The resolution artifact is additive engineering output only. It does not replay
source actions into a live host, merge ingress artifacts, define persistence or
registry law, complete continuity, or promote "latest emitted" into authority
without bounded eligibility checks.
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
SOURCE_INGRESS_COMPARISON_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_source_ingress_comparisons"
)
RESOLUTION_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_execution_authority"
)

RESOLUTION_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_CURRENT_EXECUTION_AUTHORITY_RESOLUTION"
)
RESOLUTION_VERSION = "0.1.0"
DECISION_RESOLVED = "CURRENT_EXECUTION_AUTHORITY_RESOLVED"
DECISION_NONE = "NO_CURRENT_EXECUTION_AUTHORITY"

CORE_EXECUTION_FILE = "src/integrity_host_v0_min_coexistence_v2.py"
DERIVATIVE_SUPPORT_SCOPE = (
    "src/integrity_host_v0_min_coexistence_snapshot.py",
    "src/run_integrity_host_v0_min_coexistence_scenarios.py",
    "src/integrity_host_v0_min_coexistence_import.py",
    "src/review_integrity_host_v0_min_coexistence_imports.py",
    "src/compare_integrity_host_v0_min_coexistence_source_and_review.py",
    "src/compare_integrity_host_v0_min_coexistence_source_and_import.py",
    "src/build_integrity_host_v0_min_coexistence_receiving_packet.py",
    "src/compare_integrity_host_v0_min_coexistence_source_and_receiving_packet.py",
    "src/validate_integrity_host_v0_min_coexistence_receiving_packet.py",
    "src/build_integrity_host_v0_min_coexistence_receiving_ingress_decision.py",
    "src/run_integrity_host_v0_min_coexistence_receiving_ingress.py",
    "src/compare_integrity_host_v0_min_coexistence_source_and_ingress_run.py",
)
LINEAGE_PREDECESSOR_FILES = (
    "src/integrity_host_v0_min.py",
    "src/integrity_host_v0_min_coexistence.py",
)

NON_CLAIM_KEYS = (
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
)


class ExecutionAuthorityResolutionError(RuntimeError):
    """Raised when current execution-authority resolution cannot proceed."""


def discover_source_run_directories(root: Path) -> list[Path]:
    """Return lexically sorted source ``run_*`` directories under ``root``."""

    return _discover_run_directories(root, "source run")


def discover_ingress_run_directories(root: Path) -> list[Path]:
    """Return lexically sorted receiving-ingress ``run_*`` directories."""

    return _discover_run_directories(root, "ingress run")


def discover_source_ingress_comparisons(root: Path) -> list[Path]:
    """Return lexically sorted source-to-ingress comparison artifacts."""

    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise ExecutionAuthorityResolutionError(
            f"Comparison root does not exist: {_display_path(root_path)}"
        )
    if not root_path.is_dir():
        raise ExecutionAuthorityResolutionError(
            f"Comparison root is not a directory: {_display_path(root_path)}"
        )

    try:
        return sorted(
            path
            for path in root_path.glob("*__source_ingress_comparison.json")
            if path.is_file()
        )
    except OSError as exc:
        raise ExecutionAuthorityResolutionError(
            f"Could not read comparison root: {_display_path(root_path)}"
        ) from exc


def resolve_current_execution_authority() -> dict[str, Any]:
    """Resolve bounded current execution authority for the canonical line."""

    source_runs = discover_source_run_directories(SOURCE_RUNS_ROOT)
    ingress_runs = discover_ingress_run_directories(INGRESS_RUNS_ROOT)
    comparison_artifacts = discover_source_ingress_comparisons(
        SOURCE_INGRESS_COMPARISON_ROOT
    )

    ingress_records = [_load_ingress_record(path) for path in ingress_runs]
    comparison_records = [
        _load_comparison_record(path) for path in comparison_artifacts
    ]

    candidate_runs = [
        _build_candidate_run(source_run, ingress_records, comparison_records)
        for source_run in source_runs
    ]
    eligible_candidates = [
        candidate for candidate in candidate_runs if candidate["eligible"] is True
    ]
    selected = eligible_candidates[-1] if eligible_candidates else None

    return {
        "resolution_metadata": {
            "resolution_type": RESOLUTION_TYPE,
            "resolution_version": RESOLUTION_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "canonical_execution_line": {
            "core_execution_file": CORE_EXECUTION_FILE,
            "derivative_support_scope": list(DERIVATIVE_SUPPORT_SCOPE),
            "lineage_predecessor_files": list(LINEAGE_PREDECESSOR_FILES),
        },
        "candidate_runs": candidate_runs,
        "authority_decision": _authority_decision(
            selected,
            candidate_count=len(candidate_runs),
            eligible_count=len(eligible_candidates),
        ),
        "forced_system_pressure_signals": {
            "canonical_execution_authority_pressure": (
                "Current authority is resolved for one explicit core execution "
                "line, not inferred from sibling host files."
            ),
            "currentness_vs_latest_emitted_pressure": (
                "Lexical latest is used only after correspondence, ingress, "
                "comparison, and non-claim checks pass."
            ),
            "preserved_run_multiplicity_pressure": {
                "source_run_count": len(source_runs),
                "ingress_run_count": len(ingress_runs),
                "source_ingress_comparison_count": len(comparison_artifacts),
            },
        },
        "non_claims": {
            "continuity_completed": False,
            "standing_upgraded": False,
            "replayed_into_live_host": False,
            "merged_into_local_state": False,
            "minimum_lawful_system_completed": False,
            "authority_resolution_is_protocol_law": False,
            "final_persistence_or_registry_law": False,
        },
    }


def write_resolution(
    resolution: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one UTF-8 JSON authority-resolution artifact."""

    if not isinstance(resolution, Mapping):
        raise ExecutionAuthorityResolutionError("Resolution must be a mapping")

    target_path = (
        _next_default_resolution_path()
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        raise ExecutionAuthorityResolutionError(
            f"Refusing to overwrite resolution artifact: {_display_path(target_path)}"
        )

    target_path.write_text(_json_text(resolution), encoding="utf-8")
    return target_path


def build_execution_authority_summary(
    resolution: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one authority resolution."""

    canonical = _require_mapping(
        resolution,
        "canonical_execution_line",
        "resolution",
    )
    candidates = _require_list(resolution, "candidate_runs", "resolution")
    decision = _require_mapping(resolution, "authority_decision", "resolution")

    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "canonical_execution_line",
        ),
        "candidate_run_count": len(candidates),
        "eligible_candidate_count": _require_int(
            decision,
            "eligible_candidate_count",
            "authority_decision",
        ),
        "selected_source_run_directory_path": decision.get(
            "selected_source_run_directory_path"
        ),
        "selected_ingress_run_directory_path": decision.get(
            "selected_ingress_run_directory_path"
        ),
        "selected_comparison_artifact_path": decision.get(
            "selected_comparison_artifact_path"
        ),
        "decision": _require_string(decision, "decision", "authority_decision"),
        "decision_reason": _require_string(
            decision,
            "decision_reason",
            "authority_decision",
        ),
    }


def main() -> None:
    """Resolve current execution authority, write JSON, and print a summary."""

    resolution = resolve_current_execution_authority()
    written = write_resolution(resolution)
    summary = build_execution_authority_summary(resolution)

    print(f"Candidate runs: {summary['candidate_run_count']}")
    print(f"Eligible candidates: {summary['eligible_candidate_count']}")
    print(
        "Selected source run: "
        f"{summary['selected_source_run_directory_path'] or '(none)'}"
    )
    print(
        "Selected ingress run: "
        f"{summary['selected_ingress_run_directory_path'] or '(none)'}"
    )
    print(f"Decision: {summary['decision']}")
    print(f"Resolution artifact: {_display_path(written)}")


def _discover_run_directories(root: Path, label: str) -> list[Path]:
    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise ExecutionAuthorityResolutionError(
            f"{label.title()} root does not exist: {_display_path(root_path)}"
        )
    if not root_path.is_dir():
        raise ExecutionAuthorityResolutionError(
            f"{label.title()} root is not a directory: {_display_path(root_path)}"
        )

    try:
        return sorted(
            path
            for path in root_path.iterdir()
            if path.is_dir() and path.name.startswith("run_")
        )
    except OSError as exc:
        raise ExecutionAuthorityResolutionError(
            f"Could not read {label} root: {_display_path(root_path)}"
        ) from exc


def _build_candidate_run(
    source_run: Path,
    ingress_records: list[dict[str, Any]],
    comparison_records: list[dict[str, Any]],
) -> dict[str, Any]:
    source_manifest = _read_source_manifest(source_run)
    source_manifest_path = source_run / "manifest.json"
    source_count = _require_int(source_manifest, "scenario_count", "source manifest")

    matching_ingress_records = [
        record
        for record in ingress_records
        if _same_path(record["source_run_directory_path"], source_run)
    ]
    matching_ingress_records.sort(key=lambda item: item["ingress_run_directory_path"])
    matching_source_comparisons = [
        record
        for record in comparison_records
        if _same_path(record["source_run_directory_path"], source_run)
    ]
    matching_pairs = _matching_ingress_comparison_pairs(
        matching_ingress_records,
        matching_source_comparisons,
    )

    if matching_pairs:
        selected_pair = matching_pairs[-1]
        ingress_record = selected_pair["ingress_record"]
        comparison_record = selected_pair["comparison_record"]
    else:
        ingress_record = matching_ingress_records[-1] if matching_ingress_records else None
        comparison_record = None

    checks = _eligibility_checks(
        source_run,
        source_manifest_path,
        source_count,
        ingress_record,
        comparison_record,
    )
    ineligibility_reasons = _ineligibility_reasons(checks)
    eligible = not ineligibility_reasons

    return {
        "source_run_directory_path": _display_path(source_run),
        "source_manifest_path": _display_path(source_manifest_path),
        "matched_ingress_run_directory_path": (
            _display_path(ingress_record["ingress_run_directory_path"])
            if ingress_record is not None
            else None
        ),
        "matched_ingress_manifest_path": (
            _display_path(ingress_record["ingress_manifest_path"])
            if ingress_record is not None
            else None
        ),
        "matched_comparison_artifact_path": (
            _display_path(comparison_record["comparison_path"])
            if comparison_record is not None
            else None
        ),
        "scenario_count": source_count,
        "matching_ingress_run_count": len(matching_ingress_records),
        "matching_comparison_artifact_count": len(matching_pairs),
        "eligibility_checks": checks,
        "eligible": eligible,
        "ineligibility_reasons": ineligibility_reasons,
    }


def _matching_ingress_comparison_pairs(
    ingress_records: list[dict[str, Any]],
    comparison_records: list[dict[str, Any]],
) -> list[dict[str, dict[str, Any]]]:
    pairs: list[dict[str, dict[str, Any]]] = []
    for comparison_record in comparison_records:
        matching_ingress = [
            record
            for record in ingress_records
            if _same_path(
                record["ingress_run_directory_path"],
                comparison_record["ingress_run_directory_path"],
            )
        ]
        if matching_ingress:
            pairs.append(
                {
                    "ingress_record": matching_ingress[-1],
                    "comparison_record": comparison_record,
                }
            )

    pairs.sort(
        key=lambda item: (
            item["comparison_record"]["comparison_path"],
            item["ingress_record"]["ingress_run_directory_path"],
        )
    )
    return pairs


def _eligibility_checks(
    source_run: Path,
    source_manifest_path: Path,
    source_count: int,
    ingress_record: Mapping[str, Any] | None,
    comparison_record: Mapping[str, Any] | None,
) -> dict[str, bool]:
    ingress_manifest = (
        _require_mapping(ingress_record, "manifest", "ingress record")
        if ingress_record is not None
        else None
    )
    comparison = (
        _require_mapping(comparison_record, "comparison", "comparison record")
        if comparison_record is not None
        else None
    )

    checks = {
        "source_run_exists": source_run.exists() and source_run.is_dir(),
        "source_manifest_exists": source_manifest_path.exists()
        and source_manifest_path.is_file(),
        "matching_ingress_run_exists": ingress_record is not None,
        "matching_comparison_artifact_exists": comparison_record is not None,
        "canonical_core_execution_file_preserved": (
            CORE_EXECUTION_FILE == "src/integrity_host_v0_min_coexistence_v2.py"
        ),
    }
    checks.update(
        _ingress_eligibility_checks(
            source_run,
            source_manifest_path,
            source_count,
            ingress_record,
            ingress_manifest,
        )
    )
    checks.update(
        _comparison_eligibility_checks(
            source_run,
            source_count,
            ingress_record,
            comparison_record,
            comparison,
        )
    )
    return checks


def _ingress_eligibility_checks(
    source_run: Path,
    source_manifest_path: Path,
    source_count: int,
    ingress_record: Mapping[str, Any] | None,
    ingress_manifest: Mapping[str, Any] | None,
) -> dict[str, bool]:
    if ingress_record is None or ingress_manifest is None:
        return {
            "ingress_source_run_matches": False,
            "ingress_source_manifest_matches": False,
            "ingress_scenario_count_matches_source": False,
            "ingress_all_packets_built": False,
            "ingress_all_packets_validated": False,
            "ingress_all_decisions_emitted": False,
            "ingress_continuity_not_completed": False,
            "ingress_standing_not_upgraded": False,
            "ingress_replay_not_performed": False,
            "ingress_merge_not_performed": False,
        }

    source = _require_mapping(ingress_manifest, "source_run", "ingress manifest")
    aggregate = _require_mapping(
        ingress_manifest,
        "aggregate_counts",
        "ingress manifest",
    )
    status = _require_mapping(ingress_manifest, "run_status", "ingress manifest")
    entries = _require_list(
        ingress_manifest,
        "scenario_ingress_entries",
        "ingress manifest",
    )

    return {
        "ingress_source_run_matches": _same_path(
            ingress_record["source_run_directory_path"],
            source_run,
        ),
        "ingress_source_manifest_matches": _same_path(
            ingress_record["source_manifest_path"],
            source_manifest_path,
        ),
        "ingress_scenario_count_matches_source": (
            _require_int(source, "source_scenario_count", "ingress.source_run")
            == source_count
            and _require_int(aggregate, "scenario_count", "ingress.aggregate_counts")
            == source_count
            and len(entries) == source_count
        ),
        "ingress_all_packets_built": (
            status.get("all_packets_built") is True
        ),
        "ingress_all_packets_validated": (
            status.get("all_packets_validated") is True
        ),
        "ingress_all_decisions_emitted": (
            status.get("all_decisions_emitted") is True
        ),
        "ingress_continuity_not_completed": (
            status.get("continuity_completed") is False
        ),
        "ingress_standing_not_upgraded": (
            status.get("standing_upgraded") is False
        ),
        "ingress_replay_not_performed": (
            status.get("replayed_into_live_host") is False
        ),
        "ingress_merge_not_performed": (
            status.get("merged_into_local_state") is False
        ),
    }


def _comparison_eligibility_checks(
    source_run: Path,
    source_count: int,
    ingress_record: Mapping[str, Any] | None,
    comparison_record: Mapping[str, Any] | None,
    comparison: Mapping[str, Any] | None,
) -> dict[str, bool]:
    if (
        ingress_record is None
        or comparison_record is None
        or comparison is None
    ):
        return {
            "comparison_source_run_matches": False,
            "comparison_ingress_run_matches": False,
            "comparison_all_matched": False,
            "comparison_mismatch_count_zero": False,
            "comparison_scenario_counts_align": False,
        }

    comparison_source = _require_mapping(
        comparison,
        "source_run",
        "comparison artifact",
    )
    comparison_ingress = _require_mapping(
        comparison,
        "ingress_run",
        "comparison artifact",
    )
    scenario_comparisons = _require_list(
        comparison,
        "scenario_comparisons",
        "comparison artifact",
    )

    return {
        "comparison_source_run_matches": _same_path(
            comparison_record["source_run_directory_path"],
            source_run,
        ),
        "comparison_ingress_run_matches": _same_path(
            comparison_record["ingress_run_directory_path"],
            ingress_record["ingress_run_directory_path"],
        ),
        "comparison_all_matched": comparison.get("all_matched") is True,
        "comparison_mismatch_count_zero": _mismatch_count(comparison) == 0,
        "comparison_scenario_counts_align": (
            _require_int(
                comparison_source,
                "source_scenario_count",
                "comparison.source_run",
            )
            == source_count
            and _require_int(
                comparison_ingress,
                "ingress_scenario_count",
                "comparison.ingress_run",
            )
            == source_count
            and len(scenario_comparisons) == source_count
        ),
    }


def _ineligibility_reasons(checks: Mapping[str, bool]) -> list[str]:
    reason_by_check = {
        "source_run_exists": "source run directory is missing",
        "source_manifest_exists": "source manifest is missing",
        "matching_ingress_run_exists": "no matching ingress run found",
        "matching_comparison_artifact_exists": (
            "no matching source-to-ingress comparison artifact found"
        ),
        "canonical_core_execution_file_preserved": (
            "canonical core execution file identity is not preserved"
        ),
        "ingress_source_run_matches": "ingress run does not point to source run",
        "ingress_source_manifest_matches": (
            "ingress run does not point to source manifest"
        ),
        "ingress_scenario_count_matches_source": (
            "ingress scenario count does not match source"
        ),
        "ingress_all_packets_built": "ingress run did not build all packets",
        "ingress_all_packets_validated": (
            "ingress run did not validate all packets"
        ),
        "ingress_all_decisions_emitted": (
            "ingress run did not emit all decisions"
        ),
        "ingress_continuity_not_completed": (
            "ingress run claims continuity completion"
        ),
        "ingress_standing_not_upgraded": (
            "ingress run claims standing upgrade"
        ),
        "ingress_replay_not_performed": (
            "ingress run claims replay into live host"
        ),
        "ingress_merge_not_performed": (
            "ingress run claims merge into local state"
        ),
        "comparison_source_run_matches": (
            "comparison artifact does not point to source run"
        ),
        "comparison_ingress_run_matches": (
            "comparison artifact does not point to ingress run"
        ),
        "comparison_all_matched": "comparison artifact did not fully match",
        "comparison_mismatch_count_zero": "comparison artifact contains mismatches",
        "comparison_scenario_counts_align": (
            "comparison scenario counts do not align"
        ),
    }
    return [
        reason_by_check.get(key, f"{key} failed")
        for key, passed in checks.items()
        if passed is not True
    ]


def _authority_decision(
    selected: Mapping[str, Any] | None,
    *,
    candidate_count: int,
    eligible_count: int,
) -> dict[str, Any]:
    if selected is None:
        return {
            "decision": DECISION_NONE,
            "decision_reason": "NO_SOURCE_RUN_MET_BOUNDED_AUTHORITY_RULE_SET",
            "candidate_run_count": candidate_count,
            "eligible_candidate_count": eligible_count,
            "selected_source_run_directory_path": None,
            "selected_ingress_run_directory_path": None,
            "selected_comparison_artifact_path": None,
            "selection_basis": (
                "No current authority is selected when no source run has matching "
                "ingress, matching source-to-ingress comparison, successful bounded "
                "ingress status, intact non-claims, and zero comparison mismatches."
            ),
        }

    return {
        "decision": DECISION_RESOLVED,
        "decision_reason": "LATEST_ELIGIBLE_SOURCE_RUN_AFTER_EXPLICIT_CHECKS",
        "candidate_run_count": candidate_count,
        "eligible_candidate_count": eligible_count,
        "selected_source_run_directory_path": selected[
            "source_run_directory_path"
        ],
        "selected_ingress_run_directory_path": selected[
            "matched_ingress_run_directory_path"
        ],
        "selected_comparison_artifact_path": selected[
            "matched_comparison_artifact_path"
        ],
        "selection_basis": (
            "The selected run is the lexically latest source run only after "
            "bounded correspondence, ingress success, non-claim, and comparison "
            "checks passed. Latest emission alone is not authority."
        ),
    }


def _load_ingress_record(ingress_run_dir: Path) -> dict[str, Any]:
    manifest = _read_ingress_manifest(ingress_run_dir)
    source = _require_mapping(manifest, "source_run", "ingress manifest")
    source_run_text = _require_string(
        source,
        "source_run_directory_path",
        "ingress.source_run",
    )
    source_manifest_text = _require_string(
        source,
        "source_manifest_path",
        "ingress.source_run",
    )

    return {
        "ingress_run_directory_path": ingress_run_dir,
        "ingress_manifest_path": ingress_run_dir / "manifest.json",
        "source_run_directory_path": _resolve_path_text(
            source_run_text,
            base_dir=ingress_run_dir,
        ),
        "source_manifest_path": _resolve_path_text(
            source_manifest_text,
            base_dir=ingress_run_dir,
        ),
        "manifest": manifest,
    }


def _load_comparison_record(comparison_path: Path) -> dict[str, Any]:
    comparison = _read_comparison_artifact(comparison_path)
    source = _require_mapping(comparison, "source_run", "comparison artifact")
    ingress = _require_mapping(comparison, "ingress_run", "comparison artifact")

    return {
        "comparison_path": comparison_path,
        "source_run_directory_path": _resolve_path_text(
            _require_string(
                source,
                "source_run_directory_path",
                "comparison.source_run",
            ),
            base_dir=comparison_path.parent,
        ),
        "ingress_run_directory_path": _resolve_path_text(
            _require_string(
                ingress,
                "ingress_run_directory_path",
                "comparison.ingress_run",
            ),
            base_dir=comparison_path.parent,
        ),
        "comparison": comparison,
    }


def _read_source_manifest(source_run_dir: Path) -> dict[str, Any]:
    manifest = _read_json_object(source_run_dir / "manifest.json", "source manifest")
    _require_string(manifest, "generated_at", "source manifest")
    _require_string(manifest, "output_directory", "source manifest")
    scenario_count = _require_int(manifest, "scenario_count", "source manifest")
    scenarios = _require_list(manifest, "scenarios", "source manifest")
    if scenario_count != len(scenarios):
        raise ExecutionAuthorityResolutionError(
            "Source manifest scenario_count does not match scenarios"
        )
    for index, entry in enumerate(scenarios):
        scenario = _require_mapping(entry, f"source manifest.scenarios[{index}]")
        _require_string(scenario, "scenario_id", f"source manifest.scenarios[{index}]")
        _require_string(
            scenario,
            "scenario_name",
            f"source manifest.scenarios[{index}]",
        )
        _require_string(
            scenario,
            "description",
            f"source manifest.scenarios[{index}]",
        )
        _require_string(scenario, "file_path", f"source manifest.scenarios[{index}]")
    return manifest


def _read_ingress_manifest(ingress_run_dir: Path) -> dict[str, Any]:
    manifest = _read_json_object(ingress_run_dir / "manifest.json", "ingress manifest")
    source = _require_mapping(manifest, "source_run", "ingress manifest")
    aggregate = _require_mapping(manifest, "aggregate_counts", "ingress manifest")
    status = _require_mapping(manifest, "run_status", "ingress manifest")
    entries = _require_list(
        manifest,
        "scenario_ingress_entries",
        "ingress manifest",
    )
    _require_mapping(manifest, "ingress_run_metadata", "ingress manifest")
    _require_string(
        source,
        "source_run_directory_path",
        "ingress manifest.source_run",
    )
    _require_string(
        source,
        "source_manifest_path",
        "ingress manifest.source_run",
    )
    source_count = _require_int(
        source,
        "source_scenario_count",
        "ingress manifest.source_run",
    )
    aggregate_count = _require_int(
        aggregate,
        "scenario_count",
        "ingress manifest.aggregate_counts",
    )
    if source_count != aggregate_count or source_count != len(entries):
        raise ExecutionAuthorityResolutionError(
            "Ingress manifest scenario counts do not align"
        )
    for key in (
        "all_packets_built",
        "all_packets_validated",
        "all_decisions_emitted",
        *NON_CLAIM_KEYS,
    ):
        _require_bool(status, key, "ingress manifest.run_status")
    return manifest


def _read_comparison_artifact(path: Path) -> dict[str, Any]:
    comparison = _read_json_object(path, "source-to-ingress comparison artifact")
    source = _require_mapping(comparison, "source_run", "comparison artifact")
    ingress = _require_mapping(comparison, "ingress_run", "comparison artifact")
    aggregate = _require_mapping(
        comparison,
        "aggregate_comparison",
        "comparison artifact",
    )
    _require_mapping(comparison, "comparison_metadata", "comparison artifact")
    _require_list(comparison, "scenario_comparisons", "comparison artifact")
    _require_bool(comparison, "all_matched", "comparison artifact")
    _require_string(source, "source_run_directory_path", "comparison.source_run")
    _require_string(source, "source_manifest_path", "comparison.source_run")
    _require_int(source, "source_scenario_count", "comparison.source_run")
    _require_string(ingress, "ingress_run_directory_path", "comparison.ingress_run")
    _require_string(ingress, "ingress_manifest_path", "comparison.ingress_run")
    _require_int(ingress, "ingress_scenario_count", "comparison.ingress_run")
    _require_bool(aggregate, "aggregate_match", "comparison.aggregate_comparison")
    _require_list(aggregate, "mismatches", "comparison.aggregate_comparison")
    return comparison


def _mismatch_count(comparison: Mapping[str, Any]) -> int:
    scenario_mismatches = 0
    for index, scenario in enumerate(
        _require_list(comparison, "scenario_comparisons", "comparison artifact")
    ):
        scenario_mapping = _require_mapping(
            scenario,
            f"comparison.scenario_comparisons[{index}]",
        )
        scenario_mismatches += len(
            _require_list(
                scenario_mapping,
                "mismatches",
                f"comparison.scenario_comparisons[{index}]",
            )
        )

    aggregate = _require_mapping(
        comparison,
        "aggregate_comparison",
        "comparison artifact",
    )
    aggregate_mismatches = len(
        _require_list(
            aggregate,
            "mismatches",
            "comparison.aggregate_comparison",
        )
    )
    return scenario_mismatches + aggregate_mismatches


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    json_path = _repo_relative_path(path)
    if not json_path.exists():
        raise ExecutionAuthorityResolutionError(
            f"{label.title()} is missing: {_display_path(json_path)}"
        )
    if not json_path.is_file():
        raise ExecutionAuthorityResolutionError(
            f"{label.title()} path is not a file: {_display_path(json_path)}"
        )
    try:
        parsed = json.loads(json_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ExecutionAuthorityResolutionError(
            f"Could not read {label}: {_display_path(json_path)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise ExecutionAuthorityResolutionError(
            f"{label.title()} is not valid JSON: {_display_path(json_path)}"
        ) from exc
    if not isinstance(parsed, dict):
        raise ExecutionAuthorityResolutionError(f"{label.title()} must be a JSON object")
    return parsed


def _resolve_path_text(path_text: str, *, base_dir: Path | None = None) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()

    candidates: list[Path] = []
    if base_dir is not None:
        candidates.append((base_dir / path).resolve())
    candidates.append((_repo_root() / path).resolve())

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[-1]


def _same_path(left: Path, right: Path) -> bool:
    return left.resolve() == right.resolve()


def _next_default_resolution_path() -> Path:
    output_root = _repo_root() / RESOLUTION_OUTPUT_ROOT
    candidate = output_root / "current_execution_authority_resolution.json"
    if not candidate.exists():
        return candidate

    for suffix in range(1, 1000):
        candidate = (
            output_root
            / f"current_execution_authority_resolution_{suffix:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise ExecutionAuthorityResolutionError(
        "Could not allocate a fresh execution-authority resolution path"
    )


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_relative_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (_repo_root() / path).resolve()


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(_repo_root()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, Path):
        return _display_path(value)
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    raise TypeError(f"Unsupported JSON value type: {type(value).__name__}")


def _require_mapping(value: Any, key: str, context: str | None = None) -> Mapping[str, Any]:
    if context is None:
        context = key
        if isinstance(value, Mapping):
            return value
    else:
        if isinstance(value, Mapping):
            item = value.get(key)
            if isinstance(item, Mapping):
                return item
            raise ExecutionAuthorityResolutionError(
                f"{context}.{key} must be an object"
            )
    raise ExecutionAuthorityResolutionError(f"{context} must be an object")


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise ExecutionAuthorityResolutionError(f"{context}.{key} must be a list")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise ExecutionAuthorityResolutionError(
            f"{context}.{key} must be a non-empty string"
        )
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ExecutionAuthorityResolutionError(f"{context}.{key} must be an integer")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise ExecutionAuthorityResolutionError(f"{context}.{key} must be a boolean")
    return value


if __name__ == "__main__":
    main()
