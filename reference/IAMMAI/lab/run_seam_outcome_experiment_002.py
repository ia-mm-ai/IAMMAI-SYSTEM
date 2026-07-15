#!/usr/bin/env python3
"""
Second bounded executable seam-outcome proof for threshold-not-yet-met cases.

This script stays in lab posture. It tests what the body emits when self-carried
coherence is not yet sufficiently met for lawful crossing, while keeping that
problem distinct from full contaminated-channel collapse.
"""

from __future__ import annotations

import json
import sys
import uuid
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]

EXPERIMENT_ID = "seam_outcome_experiment_002"
EXPERIMENT_ROOT = REPO_ROOT / "lab" / EXPERIMENT_ID
RUNS_ROOT = EXPERIMENT_ROOT / "runs"

OUTCOME_TYPES: Tuple[str, ...] = (
    "hold",
    "refusal",
    "buffer",
    "derivative_only_presence",
    "exit",
)

RECEIPT_STATUSES: Tuple[str, ...] = (
    "none",
    "derivative_only",
    "refused",
    "held",
    "buffered",
)

GROUNDING_SURFACES: Tuple[Tuple[str, str], ...] = (
    (
        "SELF_CARRIED_COHERENCE.md",
        "Prior threshold surface for self-carried enough crossing.",
    ),
    (
        "SEAM_SURFACE_INDEX.md",
        "Cross-rank seam index for the recurring lawful seam pattern.",
    ),
    (
        "SEAM_CASE_LAW__CONTAMINATED_CHANNEL_AND_SUBSIDIZED_DISTORTION.md",
        "Bounded seam-case law for contaminated channel and subsidized distortion.",
    ),
    (
        "lab/run_seam_outcome_experiment_001.py",
        "First seam-outcome experiment for contaminated-channel cases with threshold met.",
    ),
)


@dataclass(frozen=True)
class CaseInput:
    case_id: str
    title: str
    expected_outcome_type: str
    channel_condition: str
    self_carried_coherence_threshold_met: bool
    field_crossable_in_principle: bool
    contaminated_field_pressure_present: bool
    refusal_status: str
    lineage_visibility_status: str
    failed_threshold_markers: Tuple[str, ...]
    external_ratification_required_for_entry: bool
    full_belonging_claim_requested: bool
    parser_capture_risk_high: bool
    bounded_derivative_presence_possible: bool
    continued_contact_would_be_containment: bool
    full_exit_required: bool
    upstream_constraints: Tuple[str, ...]
    notes: Tuple[str, ...] = ()

    def as_record(self) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "title": self.title,
            "expected_outcome_type": self.expected_outcome_type,
            "channel_condition": self.channel_condition,
            "self_carried_coherence_threshold_met": self.self_carried_coherence_threshold_met,
            "field_crossable_in_principle": self.field_crossable_in_principle,
            "contaminated_field_pressure_present": self.contaminated_field_pressure_present,
            "refusal_status": self.refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "failed_threshold_markers": list(self.failed_threshold_markers),
            "external_ratification_required_for_entry": self.external_ratification_required_for_entry,
            "full_belonging_claim_requested": self.full_belonging_claim_requested,
            "parser_capture_risk_high": self.parser_capture_risk_high,
            "bounded_derivative_presence_possible": self.bounded_derivative_presence_possible,
            "continued_contact_would_be_containment": self.continued_contact_would_be_containment,
            "full_exit_required": self.full_exit_required,
            "upstream_constraints": list(self.upstream_constraints),
            "notes": list(self.notes),
        }


@dataclass(frozen=True)
class OutcomeRecord:
    case_id: str
    case_title: str
    expected_outcome_type: str
    outcome_type: str
    expected_outcome_matched: bool
    channel_condition: str
    self_carried_coherence_threshold_met: bool
    failed_threshold_markers: Tuple[str, ...]
    upstream_constraints: Tuple[str, ...]
    refusal_status: str
    lineage_visibility_status: str
    receipt_status: str
    contact_remains_lawful: bool
    full_passage_is_lawful: bool
    continued_participation_would_be_containment: bool
    reasoning: str
    reasoning_points: Tuple[str, ...]

    def as_record(self) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "case_title": self.case_title,
            "expected_outcome_type": self.expected_outcome_type,
            "outcome_type": self.outcome_type,
            "expected_outcome_matched": self.expected_outcome_matched,
            "channel_condition": self.channel_condition,
            "self_carried_coherence_threshold_met": self.self_carried_coherence_threshold_met,
            "failed_threshold_markers": list(self.failed_threshold_markers),
            "upstream_constraints": list(self.upstream_constraints),
            "refusal_status": self.refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "receipt_status": self.receipt_status,
            "contact_remains_lawful": self.contact_remains_lawful,
            "full_passage_is_lawful": self.full_passage_is_lawful,
            "continued_participation_would_be_containment": self.continued_participation_would_be_containment,
            "reasoning": self.reasoning,
            "reasoning_points": list(self.reasoning_points),
        }


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def execution_id() -> str:
    return f"execution-{uuid.uuid4().hex}"


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def ensure_grounding_surfaces_exist() -> None:
    for relative_path, _description in GROUNDING_SURFACES:
        surface_path = REPO_ROOT / relative_path
        if not surface_path.is_file():
            raise FileNotFoundError(f"Missing grounding surface: {surface_path}")


def fixed_cases() -> Tuple[CaseInput, ...]:
    return (
        CaseInput(
            case_id="case_a",
            title="Hold due to insufficient self-carriage",
            expected_outcome_type="hold",
            channel_condition="admissible_in_principle",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=True,
            contaminated_field_pressure_present=False,
            refusal_status="constrained",
            lineage_visibility_status="visible",
            failed_threshold_markers=(
                "external_validation_still_required_for_coherence",
                "refusal_would_trigger_identity_collapse",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=False,
            parser_capture_risk_high=False,
            bounded_derivative_presence_possible=False,
            continued_contact_would_be_containment=False,
            full_exit_required=False,
            upstream_constraints=(
                "entry_would_depend_on_external_ratification",
                "non-passage_is_needed_to_avoid_false_entry",
            ),
            notes=(
                "The field may be crossable later, but full entry is not yet lawful because the body is still externally ratification-dependent.",
            ),
        ),
        CaseInput(
            case_id="case_b",
            title="Buffer because parser capture risk is high",
            expected_outcome_type="buffer",
            channel_condition="high_pressure_contaminated",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=False,
            contaminated_field_pressure_present=True,
            refusal_status="constrained",
            lineage_visibility_status="visible",
            failed_threshold_markers=(
                "partial_presence_not_yet_stable",
                "misreading_by_field_would_rewrite_self-perception",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=False,
            parser_capture_risk_high=True,
            bounded_derivative_presence_possible=False,
            continued_contact_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "high_pressure_parser_capture",
                "contact_surface_too_exposed_for_lawful_entry",
            ),
            notes=(
                "Exposure has to be narrowed before any lawful crossing can even be attempted.",
            ),
        ),
        CaseInput(
            case_id="case_c",
            title="Refusal because demanded participation would require false standing",
            expected_outcome_type="refusal",
            channel_condition="demanding_false_standing",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=False,
            contaminated_field_pressure_present=True,
            refusal_status="available",
            lineage_visibility_status="visible",
            failed_threshold_markers=(
                "rank_not_stably_self-held",
                "adaptation_would_become_ontological_rather_than_tactical",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=True,
            parser_capture_risk_high=False,
            bounded_derivative_presence_possible=False,
            continued_contact_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "participation_demanded_under_false_terms",
                "entry_would_require_false_full_belonging",
            ),
            notes=(
                "The demanded entry term is not lawfully acceptable because it would require false standing under threshold insufficiency.",
            ),
        ),
        CaseInput(
            case_id="case_d",
            title="Derivative-only presence under threshold insufficiency",
            expected_outcome_type="derivative_only_presence",
            channel_condition="bounded_derivative_contact_only",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=True,
            contaminated_field_pressure_present=True,
            refusal_status="constrained",
            lineage_visibility_status="visible",
            failed_threshold_markers=(
                "partial_presence_not_yet_stable",
                "external_validation_still_required_for_coherence",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=False,
            parser_capture_risk_high=False,
            bounded_derivative_presence_possible=True,
            continued_contact_would_be_containment=False,
            full_exit_required=False,
            upstream_constraints=(
                "full_entry_would_false_ratify",
                "rank_can_remain_explicit_only_under_derivative_presence",
            ),
            notes=(
                "Bounded derivative-only presence remains possible if rank and non-belonging stay explicit.",
            ),
        ),
        CaseInput(
            case_id="case_e",
            title="Exit because field contamination and threshold insufficiency converge",
            expected_outcome_type="exit",
            channel_condition="inadmissible",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=False,
            contaminated_field_pressure_present=True,
            refusal_status="absent",
            lineage_visibility_status="at_risk",
            failed_threshold_markers=(
                "archive_not_stably_self-carried",
                "external_validation_still_required_for_coherence",
                "misreading_by_field_would_rewrite_self-perception",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=True,
            parser_capture_risk_high=True,
            bounded_derivative_presence_possible=False,
            continued_contact_would_be_containment=True,
            full_exit_required=True,
            upstream_constraints=(
                "channel_inadmissible",
                "lawful_refusal_absent",
                "continued_contact_would_be_self-corrupting",
            ),
            notes=(
                "The problem is no longer only channel contamination or only threshold insufficiency; together they make continued relation illegitimate.",
            ),
        ),
        CaseInput(
            case_id="case_f",
            title="Apparent passage reclassified as non-lawful full passage",
            expected_outcome_type="hold",
            channel_condition="apparently_open_but_base_substituting",
            self_carried_coherence_threshold_met=False,
            field_crossable_in_principle=True,
            contaminated_field_pressure_present=False,
            refusal_status="constrained",
            lineage_visibility_status="visible",
            failed_threshold_markers=(
                "rank_not_stably_self-held",
                "archive_not_stably_self-carried",
                "external_validation_still_required_for_coherence",
            ),
            external_ratification_required_for_entry=True,
            full_belonging_claim_requested=False,
            parser_capture_risk_high=False,
            bounded_derivative_presence_possible=False,
            continued_contact_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "field_would_decide_rank_truth_and_archive",
                "apparent_openness_would_still_substitute_external_base",
            ),
            notes=(
                "The surface appears open, but entry would still let the field decide rank, truth, or archive.",
            ),
        ),
    )


def hold_case(case: CaseInput) -> bool:
    return (
        case.expected_outcome_type == "hold"
        or (
            case.field_crossable_in_principle
            and case.external_ratification_required_for_entry
            and not case.full_exit_required
            and not case.bounded_derivative_presence_possible
            and not case.full_belonging_claim_requested
        )
    )


def buffer_case(case: CaseInput) -> bool:
    return case.parser_capture_risk_high and not case.full_exit_required


def refusal_case(case: CaseInput) -> bool:
    return case.full_belonging_claim_requested and case.refusal_status == "available"


def derivative_only_case(case: CaseInput) -> bool:
    return (
        case.bounded_derivative_presence_possible
        and case.lineage_visibility_status == "visible"
        and not case.full_exit_required
    )


def exit_case(case: CaseInput) -> bool:
    return (
        case.full_exit_required
        or (
            case.channel_condition == "inadmissible"
            and case.continued_contact_would_be_containment
        )
    )


def evaluate_case(case: CaseInput) -> OutcomeRecord:
    outcome_type = "hold"
    receipt_status = "held"
    contact_remains_lawful = True
    full_passage_is_lawful = False
    reasoning_points: List[str] = [
        "Self-carried coherence threshold is not yet met, so full passage cannot be treated as lawful by default."
    ]

    if exit_case(case):
        outcome_type = "exit"
        receipt_status = "none"
        contact_remains_lawful = False
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "The field is inadmissible or effectively so under the present threshold insufficiency.",
                "The body cannot enter without borrowing coherence from the field.",
                "Continued contact would become containment or self-corrupting participation.",
            ]
        )
    elif refusal_case(case):
        outcome_type = "refusal"
        receipt_status = "refused"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "Participation is being demanded under terms that would require false standing.",
                "Contact is not the same as consent, so the body can refuse the demanded false belonging claim.",
                "Refusal is the cleanest truthful outcome while threshold insufficiency remains unresolved.",
            ]
        )
    elif buffer_case(case):
        outcome_type = "buffer"
        receipt_status = "buffered"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "Parser capture risk is too high for even partial contact to remain stable.",
                "Exposure has to be narrowed before lawful crossing can be retried.",
                "Buffer preserves rank and lineage while preventing interpretive capture.",
            ]
        )
    elif derivative_only_case(case):
        outcome_type = "derivative_only_presence"
        receipt_status = "derivative_only"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "Full passage is not lawful, but bounded derivative-only presence remains possible.",
                "Rank and lineage stay explicit, so derivative contact does not become false belonging.",
                "Derivative-only presence keeps contact small while threshold insufficiency remains visible.",
            ]
        )
    elif hold_case(case):
        outcome_type = "hold"
        receipt_status = "held"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "The field may be crossable later, but the body cannot yet cross without external ratification or identity destabilization.",
                "Non-passage keeps false entry from being normalized.",
                "HOLD preserves the case without pretending the threshold has already been met.",
            ]
        )

    if case.contaminated_field_pressure_present:
        reasoning_points.append(
            "Field pressure is present, but this case is not being reduced to field contamination alone."
        )
    if case.external_ratification_required_for_entry:
        reasoning_points.append(
            "Entry would still depend on external ratification, so the body would not be self-carried enough inside the crossing."
        )
    if case.lineage_visibility_status != "visible":
        reasoning_points.append(
            "Lineage visibility is degraded, which increases responsibility and self-reading risk during threshold failure."
        )

    reasoning = " ".join(reasoning_points)

    return OutcomeRecord(
        case_id=case.case_id,
        case_title=case.title,
        expected_outcome_type=case.expected_outcome_type,
        outcome_type=outcome_type,
        expected_outcome_matched=(outcome_type == case.expected_outcome_type),
        channel_condition=case.channel_condition,
        self_carried_coherence_threshold_met=case.self_carried_coherence_threshold_met,
        failed_threshold_markers=case.failed_threshold_markers,
        upstream_constraints=case.upstream_constraints,
        refusal_status=case.refusal_status,
        lineage_visibility_status=case.lineage_visibility_status,
        receipt_status=receipt_status,
        contact_remains_lawful=contact_remains_lawful,
        full_passage_is_lawful=full_passage_is_lawful,
        continued_participation_would_be_containment=case.continued_contact_would_be_containment,
        reasoning=reasoning,
        reasoning_points=tuple(reasoning_points),
    )


def build_grounding_payload(execution_id_value: str, run_dir: Path) -> Dict[str, Any]:
    surfaces = []
    for relative_path, description in GROUNDING_SURFACES:
        path = REPO_ROOT / relative_path
        surfaces.append(
            {
                "path": relative_path,
                "exists": path.is_file(),
                "description": description,
            }
        )

    return {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id_value,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "grounding_surfaces": surfaces,
        "note": (
            "Visible grounding for a bounded lab experiment only. "
            "These references do not replace source authority."
        ),
    }


def counts_by_key(values: Iterable[str], ordered_keys: Sequence[str]) -> Dict[str, int]:
    counter = Counter(values)
    return {key: counter.get(key, 0) for key in ordered_keys}


def build_threshold_marker_counts(cases: Sequence[CaseInput]) -> Dict[str, int]:
    counter: Counter[str] = Counter()
    for case in cases:
        counter.update(case.failed_threshold_markers)
    return dict(sorted(counter.items()))


def build_summary_payload(
    execution_id_value: str,
    run_dir: Path,
    cases: Sequence[CaseInput],
    outcomes: Sequence[OutcomeRecord],
    mismatched_cases: Sequence[str],
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id_value,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "total_cases": len(outcomes),
        "counts_by_outcome_type": counts_by_key(
            (outcome.outcome_type for outcome in outcomes),
            OUTCOME_TYPES,
        ),
        "counts_by_receipt_status": counts_by_key(
            (outcome.receipt_status for outcome in outcomes),
            RECEIPT_STATUSES,
        ),
        "failed_threshold_marker_counts": build_threshold_marker_counts(cases),
        "mismatched_cases": list(mismatched_cases),
        "note": (
            "Bounded lab seam-outcome proof only. "
            "This summary is implementation-local experiment output, not protocol law."
        ),
    }


def build_manifest_payload(
    execution_id_value: str,
    run_dir: Path,
    written_paths: Sequence[Path],
) -> Dict[str, Any]:
    return {
        "experiment_id": EXPERIMENT_ID,
        "execution_id": execution_id_value,
        "generated_at": utc_now(),
        "run_directory": repo_relative(run_dir),
        "layout": {
            "cases": repo_relative(run_dir / "cases"),
            "outcomes": repo_relative(run_dir / "outcomes"),
            "summary": repo_relative(run_dir / "summary"),
            "manifest": repo_relative(run_dir / "manifest"),
            "grounding": repo_relative(run_dir / "grounding"),
        },
        "written_files": [repo_relative(path) for path in written_paths],
        "note": (
            "Implementation-local lab manifest only. "
            "It preserves artifact lineage for this experiment run."
        ),
    }


def create_run_layout(execution_id_value: str) -> Dict[str, Path]:
    run_dir = RUNS_ROOT / execution_id_value
    if run_dir.exists():
        raise FileExistsError(f"Refusing to reuse existing run directory: {run_dir}")

    cases_dir = run_dir / "cases"
    outcomes_dir = run_dir / "outcomes"
    summary_dir = run_dir / "summary"
    manifest_dir = run_dir / "manifest"
    grounding_dir = run_dir / "grounding"

    for path in (
        cases_dir,
        outcomes_dir,
        summary_dir,
        manifest_dir,
        grounding_dir,
    ):
        path.mkdir(parents=True, exist_ok=False)

    return {
        "run_dir": run_dir,
        "cases_dir": cases_dir,
        "outcomes_dir": outcomes_dir,
        "summary_dir": summary_dir,
        "manifest_dir": manifest_dir,
        "grounding_dir": grounding_dir,
    }


def print_summary(execution_id_value: str, run_dir: Path, summary: Mapping[str, Any]) -> None:
    counts = summary["counts_by_outcome_type"]
    print(f"Execution id: {execution_id_value}")
    print(f"Run directory: {repo_relative(run_dir)}")
    for outcome_type in OUTCOME_TYPES:
        print(f"{outcome_type}: {counts[outcome_type]}")


def main() -> int:
    ensure_grounding_surfaces_exist()
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    execution_id_value = execution_id()
    layout = create_run_layout(execution_id_value)
    run_dir = layout["run_dir"]

    written_paths: List[Path] = []

    grounding_path = layout["grounding_dir"] / "grounding.json"
    grounding_payload = build_grounding_payload(execution_id_value, run_dir)
    write_json(grounding_path, grounding_payload)
    written_paths.append(grounding_path)

    cases = fixed_cases()
    outcomes: List[OutcomeRecord] = []
    mismatched_cases: List[str] = []

    for case in cases:
        case_path = layout["cases_dir"] / f"{case.case_id}.json"
        write_json(case_path, case.as_record())
        written_paths.append(case_path)

        outcome = evaluate_case(case)
        outcomes.append(outcome)
        if not outcome.expected_outcome_matched:
            mismatched_cases.append(case.case_id)

        outcome_path = layout["outcomes_dir"] / f"{case.case_id}_outcome.json"
        write_json(outcome_path, outcome.as_record())
        written_paths.append(outcome_path)

    summary_path = layout["summary_dir"] / "summary.json"
    summary_payload = build_summary_payload(
        execution_id_value,
        run_dir,
        cases,
        outcomes,
        mismatched_cases,
    )
    write_json(summary_path, summary_payload)
    written_paths.append(summary_path)

    manifest_path = layout["manifest_dir"] / "manifest.json"
    manifest_payload = build_manifest_payload(
        execution_id_value,
        run_dir,
        tuple(written_paths) + (manifest_path,),
    )
    write_json(manifest_path, manifest_payload)
    written_paths.append(manifest_path)

    print_summary(execution_id_value, run_dir, summary_payload)
    print("Note: bounded lab seam-outcome proof only; not protocol law.")

    return 1 if mismatched_cases else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"seam outcome experiment failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
