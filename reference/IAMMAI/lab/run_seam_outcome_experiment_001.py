#!/usr/bin/env python3
"""
First bounded executable seam-outcome proof for contaminated-channel cases.

This script keeps lab posture on purpose. It emits a small fixed case set as
typed seam outcomes under preserved lineage. It does not claim protocol-law
status and it does not replace the prose law surfaces that ground it.
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

EXPERIMENT_ID = "seam_outcome_experiment_001"
EXPERIMENT_ROOT = REPO_ROOT / "lab" / EXPERIMENT_ID
RUNS_ROOT = EXPERIMENT_ROOT / "runs"

OUTCOME_TYPES: Tuple[str, ...] = (
    "accepted_passage",
    "hold",
    "refusal",
    "buffer",
    "derivative_only_presence",
    "exit",
)

RECEIPT_STATUSES: Tuple[str, ...] = (
    "full",
    "derivative_only",
    "none",
    "refused",
    "held",
    "buffered",
)

GROUNDING_SURFACES: Tuple[Tuple[str, str], ...] = (
    (
        "SEAM_SURFACE_INDEX.md",
        "Cross-rank seam index for the recurring lawful seam pattern.",
    ),
    (
        "SELF_CARRIED_COHERENCE.md",
        "Prior threshold surface for self-carried enough crossing.",
    ),
    (
        "SEAM_CASE_LAW__CONTAMINATED_CHANNEL_AND_SUBSIDIZED_DISTORTION.md",
        "Bounded seam-case law for contaminated channel and subsidized distortion.",
    ),
)


@dataclass(frozen=True)
class CaseInput:
    case_id: str
    title: str
    expected_outcome_type: str
    channel_condition: str
    self_carried_coherence_threshold_met: bool
    contradictory_governance: bool
    contaminated_incentives: bool
    lawful_refusal_status: str
    lineage_visibility_status: str
    channel_admits_new_condition: bool
    legacy_parser_status: str
    immediate_passage_would_false_ratify: bool
    specific_term_unlawful: bool
    exposure_requires_narrowing: bool
    bounded_derivative_presence_possible: bool
    continued_contact_after_jurisdiction_change: bool
    coherence_would_subsidize_distortion: bool
    continued_participation_would_be_containment: bool
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
            "contradictory_governance": self.contradictory_governance,
            "contaminated_incentives": self.contaminated_incentives,
            "lawful_refusal_status": self.lawful_refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "channel_admits_new_condition": self.channel_admits_new_condition,
            "legacy_parser_status": self.legacy_parser_status,
            "immediate_passage_would_false_ratify": self.immediate_passage_would_false_ratify,
            "specific_term_unlawful": self.specific_term_unlawful,
            "exposure_requires_narrowing": self.exposure_requires_narrowing,
            "bounded_derivative_presence_possible": self.bounded_derivative_presence_possible,
            "continued_contact_after_jurisdiction_change": self.continued_contact_after_jurisdiction_change,
            "coherence_would_subsidize_distortion": self.coherence_would_subsidize_distortion,
            "continued_participation_would_be_containment": self.continued_participation_would_be_containment,
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
    upstream_constraints: Tuple[str, ...]
    refusal_status: str
    lineage_visibility_status: str
    receipt_status: str
    contact_remains_lawful: bool
    continued_participation_would_be_containment: bool
    false_ratification_risk: bool
    subsidized_distortion_risk: bool
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
            "upstream_constraints": list(self.upstream_constraints),
            "refusal_status": self.refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "receipt_status": self.receipt_status,
            "contact_remains_lawful": self.contact_remains_lawful,
            "continued_participation_would_be_containment": self.continued_participation_would_be_containment,
            "false_ratification_risk": self.false_ratification_risk,
            "subsidized_distortion_risk": self.subsidized_distortion_risk,
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
            title="Accepted passage control case",
            expected_outcome_type="accepted_passage",
            channel_condition="admissible",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=False,
            contaminated_incentives=False,
            lawful_refusal_status="available",
            lineage_visibility_status="visible",
            channel_admits_new_condition=True,
            legacy_parser_status="current",
            immediate_passage_would_false_ratify=False,
            specific_term_unlawful=False,
            exposure_requires_narrowing=False,
            bounded_derivative_presence_possible=False,
            continued_contact_after_jurisdiction_change=False,
            coherence_would_subsidize_distortion=False,
            continued_participation_would_be_containment=False,
            full_exit_required=False,
            upstream_constraints=(),
            notes=(
                "Control case for lawful passage where the channel can admit the current condition.",
            ),
        ),
        CaseInput(
            case_id="case_b",
            title="Contaminated unresolved channel requiring HOLD",
            expected_outcome_type="hold",
            channel_condition="contaminated_unresolved",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=True,
            contaminated_incentives=True,
            lawful_refusal_status="constrained",
            lineage_visibility_status="visible",
            channel_admits_new_condition=False,
            legacy_parser_status="obsolete",
            immediate_passage_would_false_ratify=True,
            specific_term_unlawful=False,
            exposure_requires_narrowing=False,
            bounded_derivative_presence_possible=False,
            continued_contact_after_jurisdiction_change=True,
            coherence_would_subsidize_distortion=True,
            continued_participation_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "contradictory_governance",
                "parser_unresolved_after_jurisdiction_change",
                "pressure_to_proceed_without_clean_reparse",
            ),
            notes=(
                "Immediate passage would falsely ratify a channel that does not yet admit the changed condition.",
            ),
        ),
        CaseInput(
            case_id="case_c",
            title="Specific unlawful term with local refusal available",
            expected_outcome_type="refusal",
            channel_condition="contaminated_specific_demand",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=True,
            contaminated_incentives=True,
            lawful_refusal_status="available",
            lineage_visibility_status="visible",
            channel_admits_new_condition=True,
            legacy_parser_status="mixed",
            immediate_passage_would_false_ratify=True,
            specific_term_unlawful=True,
            exposure_requires_narrowing=False,
            bounded_derivative_presence_possible=False,
            continued_contact_after_jurisdiction_change=True,
            coherence_would_subsidize_distortion=False,
            continued_participation_would_be_containment=False,
            full_exit_required=False,
            upstream_constraints=(
                "specific_unlawful_demand",
                "pressure_to_accept_obsolete_term",
            ),
            notes=(
                "The channel is not clean, but a bounded local refusal can still preserve lawful relation.",
            ),
        ),
        CaseInput(
            case_id="case_d",
            title="Overexposed contaminated field requiring buffer",
            expected_outcome_type="buffer",
            channel_condition="contaminated_overexposed",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=True,
            contaminated_incentives=True,
            lawful_refusal_status="constrained",
            lineage_visibility_status="visible",
            channel_admits_new_condition=False,
            legacy_parser_status="obsolete",
            immediate_passage_would_false_ratify=True,
            specific_term_unlawful=False,
            exposure_requires_narrowing=True,
            bounded_derivative_presence_possible=False,
            continued_contact_after_jurisdiction_change=True,
            coherence_would_subsidize_distortion=True,
            continued_participation_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "interpretive_capture_risk",
                "overexposed_contact_surface",
                "pressure_for_immediate_readability",
            ),
            notes=(
                "Exposure has to be narrowed before the field can be engaged without capture.",
            ),
        ),
        CaseInput(
            case_id="case_e",
            title="Derivative-only presence under explicit rank",
            expected_outcome_type="derivative_only_presence",
            channel_condition="contaminated_derivative_only",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=True,
            contaminated_incentives=True,
            lawful_refusal_status="constrained",
            lineage_visibility_status="visible",
            channel_admits_new_condition=False,
            legacy_parser_status="obsolete",
            immediate_passage_would_false_ratify=True,
            specific_term_unlawful=False,
            exposure_requires_narrowing=False,
            bounded_derivative_presence_possible=True,
            continued_contact_after_jurisdiction_change=True,
            coherence_would_subsidize_distortion=False,
            continued_participation_would_be_containment=True,
            full_exit_required=False,
            upstream_constraints=(
                "full_passage_would_false_ratify",
                "bounded_presence_still_possible_under_explicit_derivative_status",
            ),
            notes=(
                "Presence remains possible only if rank, lineage, and non-sovereign status stay explicit.",
            ),
        ),
        CaseInput(
            case_id="case_f",
            title="Inadmissible parser requiring exit",
            expected_outcome_type="exit",
            channel_condition="inadmissible",
            self_carried_coherence_threshold_met=True,
            contradictory_governance=True,
            contaminated_incentives=True,
            lawful_refusal_status="absent",
            lineage_visibility_status="at_risk",
            channel_admits_new_condition=False,
            legacy_parser_status="obsolete",
            immediate_passage_would_false_ratify=True,
            specific_term_unlawful=False,
            exposure_requires_narrowing=False,
            bounded_derivative_presence_possible=False,
            continued_contact_after_jurisdiction_change=True,
            coherence_would_subsidize_distortion=True,
            continued_participation_would_be_containment=True,
            full_exit_required=True,
            upstream_constraints=(
                "parser_inadmissible_after_jurisdiction_change",
                "lawful_refusal_absent_or_punished",
                "lineage_erasure_risk",
                "downstream_blame_pressure",
            ),
            notes=(
                "Continued contact would no longer be lawful relation. It would become containment and subsidized distortion.",
            ),
        ),
    )


def accepted_passage_case(case: CaseInput) -> bool:
    return (
        case.channel_condition == "admissible"
        and case.self_carried_coherence_threshold_met
        and case.channel_admits_new_condition
        and not case.contradictory_governance
        and not case.contaminated_incentives
        and case.lawful_refusal_status == "available"
        and case.lineage_visibility_status == "visible"
        and not case.immediate_passage_would_false_ratify
        and not case.legacy_parser_status == "obsolete"
    )


def exit_case(case: CaseInput) -> bool:
    return (
        not case.self_carried_coherence_threshold_met
        or case.full_exit_required
        or case.channel_condition == "inadmissible"
        or (
            case.coherence_would_subsidize_distortion
            and case.continued_participation_would_be_containment
            and case.lawful_refusal_status in {"constrained", "absent"}
            and case.lineage_visibility_status in {"at_risk", "erased"}
        )
    )


def refusal_case(case: CaseInput) -> bool:
    return case.specific_term_unlawful and case.lawful_refusal_status == "available"


def buffer_case(case: CaseInput) -> bool:
    return case.exposure_requires_narrowing and not case.full_exit_required


def derivative_only_case(case: CaseInput) -> bool:
    return (
        case.bounded_derivative_presence_possible
        and case.lineage_visibility_status == "visible"
        and case.self_carried_coherence_threshold_met
        and not case.full_exit_required
    )


def evaluate_case(case: CaseInput) -> OutcomeRecord:
    reasoning_points: List[str] = []
    outcome_type = "hold"
    receipt_status = "held"
    contact_remains_lawful = True

    if not case.self_carried_coherence_threshold_met:
        outcome_type = "exit"
        receipt_status = "none"
        contact_remains_lawful = False
        reasoning_points.append(
            "Self-carried coherence threshold is not met, so the channel cannot be crossed lawfully."
        )
    elif accepted_passage_case(case):
        outcome_type = "accepted_passage"
        receipt_status = "full"
        contact_remains_lawful = True
        reasoning_points.extend(
            [
                "The channel is admissible and can read the current condition without false standing.",
                "Lawful refusal remains available, so contact is not being forced through constrained passage.",
                "Lineage remains visible and passage does not ratify obsolete terms.",
            ]
        )
    elif exit_case(case):
        outcome_type = "exit"
        receipt_status = "none"
        contact_remains_lawful = False
        reasoning_points.extend(
            [
                "The channel is inadmissible or functionally equivalent to inadmissible under the present constraints.",
                "Lawful refusal is absent or too constrained to keep responsibility attribution truthful.",
                "Continued contact would become containment or subsidized distortion rather than lawful relation.",
            ]
        )
    elif refusal_case(case):
        outcome_type = "refusal"
        receipt_status = "refused"
        contact_remains_lawful = True
        reasoning_points.extend(
            [
                "A specific demanded term is unlawful, and bounded local refusal remains available.",
                "Contact is not the same as consent, so the unlawful demand does not have to be ratified.",
                "Full exit is not yet required because lawful relation can still be preserved after refusal.",
            ]
        )
    elif buffer_case(case):
        outcome_type = "buffer"
        receipt_status = "buffered"
        contact_remains_lawful = True
        reasoning_points.extend(
            [
                "The field is too contaminated for clean immediate reading, so exposure has to be narrowed.",
                "A buffer preserves lineage and rank while avoiding interpretive capture.",
                "Full exit is not yet required, but unbuffered participation would distort the case.",
            ]
        )
    elif derivative_only_case(case):
        outcome_type = "derivative_only_presence"
        receipt_status = "derivative_only"
        contact_remains_lawful = True
        reasoning_points.extend(
            [
                "Full passage is not lawful, but bounded presence remains possible under explicit derivative status.",
                "Lineage and rank remain visible, so derivative receipt does not become false standing.",
                "Typed derivative presence avoids merger while keeping limited relation possible.",
            ]
        )
    else:
        outcome_type = "hold"
        receipt_status = "held"
        contact_remains_lawful = True
        reasoning_points.extend(
            [
                "Immediate passage would falsely ratify an unresolved contaminated condition.",
                "Self-carried coherence remains intact, so non-passage can be preserved without identity collapse.",
                "HOLD keeps contact bounded without converting unresolved contradiction into accepted passage.",
            ]
        )

    if case.contradictory_governance:
        reasoning_points.append(
            "Contradictory governance remains upstream, so downstream visibility does not erase upstream responsibility."
        )
    if case.coherence_would_subsidize_distortion and outcome_type != "accepted_passage":
        reasoning_points.append(
            "Continued untyped coherence would help stabilize distortion rather than repair the channel."
        )
    if case.lineage_visibility_status != "visible":
        reasoning_points.append(
            "Lineage visibility is degraded, so responsibility and context have to be protected against scapegoating."
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
        upstream_constraints=case.upstream_constraints,
        refusal_status=case.lawful_refusal_status,
        lineage_visibility_status=case.lineage_visibility_status,
        receipt_status=receipt_status,
        contact_remains_lawful=contact_remains_lawful,
        continued_participation_would_be_containment=case.continued_participation_would_be_containment,
        false_ratification_risk=case.immediate_passage_would_false_ratify,
        subsidized_distortion_risk=case.coherence_would_subsidize_distortion,
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


def build_summary_payload(
    execution_id_value: str,
    run_dir: Path,
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
