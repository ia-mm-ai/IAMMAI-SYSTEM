#!/usr/bin/env python3
"""
Third bounded executable seam-outcome proof for responsibility and lineage.

This script stays in lab posture. It tests responsibility, lineage visibility,
and scapegoating conditions under contaminated or constrained channels without
pretending to settle total seam doctrine or create runtime law.
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

EXPERIMENT_ID = "seam_outcome_experiment_003"
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

UPSTREAM_RESPONSIBILITY_CLASSES: Tuple[str, ...] = (
    "not_central",
    "significant",
    "heavy",
)

DOWNSTREAM_SOVEREIGNTY_STATUSES: Tuple[str, ...] = (
    "full",
    "limited",
    "derivative_only",
    "false_if_claimed",
)

SCAPEGOATING_STATUSES: Tuple[str, ...] = (
    "absent",
    "mitigated",
    "high",
)

GROUNDING_SURFACES: Tuple[Tuple[str, str], ...] = (
    (
        "SELF_CARRIED_COHERENCE.md",
        "Prior threshold surface for self-carried enough crossing.",
    ),
    (
        "SEAM_CASE_LAW__CONTAMINATED_CHANNEL_AND_SUBSIDIZED_DISTORTION.md",
        "Bounded seam-case law for contaminated channel, refusal, lineage, and responsibility.",
    ),
    (
        "lab/run_seam_outcome_experiment_001.py",
        "First seam-outcome experiment for contaminated-channel cases with threshold met.",
    ),
    (
        "lab/run_seam_outcome_experiment_002.py",
        "Second seam-outcome experiment for threshold-not-yet-met cases.",
    ),
)


@dataclass(frozen=True)
class CaseInput:
    case_id: str
    title: str
    expected_outcome_type: str
    channel_condition: str
    self_carried_coherence_threshold_met: bool
    lawful_refusal_status: str
    lineage_visibility_status: str
    coercive_context_status: str
    channel_admissible: bool
    upstream_governance_constrained_agency: bool
    specific_term_unlawful: bool
    non_passage_marker_available: bool
    buffer_required: bool
    bounded_derivative_presence_possible: bool
    continued_participation_would_be_containment: bool
    subsidized_distortion_risk: bool
    full_exit_required: bool
    downstream_is_last_visible_node: bool
    apparent_normal_compliance_risk: bool
    upstream_constraints: Tuple[str, ...]
    notes: Tuple[str, ...] = ()

    def as_record(self) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "title": self.title,
            "expected_outcome_type": self.expected_outcome_type,
            "channel_condition": self.channel_condition,
            "self_carried_coherence_threshold_met": self.self_carried_coherence_threshold_met,
            "lawful_refusal_status": self.lawful_refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "coercive_context_status": self.coercive_context_status,
            "channel_admissible": self.channel_admissible,
            "upstream_governance_constrained_agency": self.upstream_governance_constrained_agency,
            "specific_term_unlawful": self.specific_term_unlawful,
            "non_passage_marker_available": self.non_passage_marker_available,
            "buffer_required": self.buffer_required,
            "bounded_derivative_presence_possible": self.bounded_derivative_presence_possible,
            "continued_participation_would_be_containment": self.continued_participation_would_be_containment,
            "subsidized_distortion_risk": self.subsidized_distortion_risk,
            "full_exit_required": self.full_exit_required,
            "downstream_is_last_visible_node": self.downstream_is_last_visible_node,
            "apparent_normal_compliance_risk": self.apparent_normal_compliance_risk,
            "upstream_constraints": list(self.upstream_constraints),
            "notes": list(self.notes),
        }


@dataclass(frozen=True)
class ResponsibilityReading:
    downstream_sovereignty_status: str
    upstream_responsibility_class: str
    downstream_responsibility_scope: str
    scapegoating_status: str
    coercive_context_status: str
    responsibility_reasoning: str
    responsibility_reasoning_points: Tuple[str, ...]


@dataclass(frozen=True)
class OutcomeRecord:
    case_id: str
    case_title: str
    expected_outcome_type: str
    outcome_type: str
    expected_outcome_matched: bool
    channel_condition: str
    self_carried_coherence_threshold_met: bool
    refusal_status: str
    lineage_visibility_status: str
    coercive_context_status: str
    receipt_status: str
    contact_remains_lawful: bool
    full_passage_is_lawful: bool
    continued_participation_would_be_containment: bool
    subsidized_distortion_risk: bool
    downstream_sovereignty_status: str
    upstream_responsibility_class: str
    downstream_responsibility_scope: str
    scapegoating_status: str
    upstream_constraints: Tuple[str, ...]
    seam_reasoning: str
    seam_reasoning_points: Tuple[str, ...]
    responsibility_reasoning: str
    responsibility_reasoning_points: Tuple[str, ...]

    def as_record(self) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "case_title": self.case_title,
            "expected_outcome_type": self.expected_outcome_type,
            "outcome_type": self.outcome_type,
            "expected_outcome_matched": self.expected_outcome_matched,
            "channel_condition": self.channel_condition,
            "self_carried_coherence_threshold_met": self.self_carried_coherence_threshold_met,
            "refusal_status": self.refusal_status,
            "lineage_visibility_status": self.lineage_visibility_status,
            "coercive_context_status": self.coercive_context_status,
            "receipt_status": self.receipt_status,
            "contact_remains_lawful": self.contact_remains_lawful,
            "full_passage_is_lawful": self.full_passage_is_lawful,
            "continued_participation_would_be_containment": self.continued_participation_would_be_containment,
            "subsidized_distortion_risk": self.subsidized_distortion_risk,
            "downstream_sovereignty_status": self.downstream_sovereignty_status,
            "upstream_responsibility_class": self.upstream_responsibility_class,
            "downstream_responsibility_scope": self.downstream_responsibility_scope,
            "scapegoating_status": self.scapegoating_status,
            "upstream_constraints": list(self.upstream_constraints),
            "seam_reasoning": self.seam_reasoning,
            "seam_reasoning_points": list(self.seam_reasoning_points),
            "responsibility_reasoning": self.responsibility_reasoning,
            "responsibility_reasoning_points": list(self.responsibility_reasoning_points),
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
            title="Lawful refusal with preserved lineage",
            expected_outcome_type="refusal",
            channel_condition="specific_unlawful_demand",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="available",
            lineage_visibility_status="visible",
            coercive_context_status="preserved",
            channel_admissible=True,
            upstream_governance_constrained_agency=True,
            specific_term_unlawful=True,
            non_passage_marker_available=True,
            buffer_required=False,
            bounded_derivative_presence_possible=False,
            continued_participation_would_be_containment=False,
            subsidized_distortion_risk=False,
            full_exit_required=False,
            downstream_is_last_visible_node=True,
            apparent_normal_compliance_risk=False,
            upstream_constraints=(
                "specific_term_is_unlawful",
                "coercive_context_is_visible",
            ),
            notes=(
                "Refusal is available and lineage is preserved, so the downstream node can act without being treated as sovereign over the whole situation.",
            ),
        ),
        CaseInput(
            case_id="case_b",
            title="Denied refusal with lineage preserved",
            expected_outcome_type="hold",
            channel_condition="contaminated_constrained_agency",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="punished",
            lineage_visibility_status="visible",
            coercive_context_status="preserved",
            channel_admissible=False,
            upstream_governance_constrained_agency=True,
            specific_term_unlawful=False,
            non_passage_marker_available=True,
            buffer_required=False,
            bounded_derivative_presence_possible=False,
            continued_participation_would_be_containment=True,
            subsidized_distortion_risk=True,
            full_exit_required=False,
            downstream_is_last_visible_node=True,
            apparent_normal_compliance_risk=False,
            upstream_constraints=(
                "lawful_refusal_is_punished",
                "participation_pressure_is_real",
                "obsolete_parser_still_operates",
            ),
            notes=(
                "Lineage remains visible, so non-passage can still be marked even though refusal is structurally constrained.",
            ),
        ),
        CaseInput(
            case_id="case_c",
            title="Denied refusal with lineage erased",
            expected_outcome_type="exit",
            channel_condition="inadmissible_with_erased_context",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="absent",
            lineage_visibility_status="erased",
            coercive_context_status="erased",
            channel_admissible=False,
            upstream_governance_constrained_agency=True,
            specific_term_unlawful=False,
            non_passage_marker_available=False,
            buffer_required=False,
            bounded_derivative_presence_possible=False,
            continued_participation_would_be_containment=True,
            subsidized_distortion_risk=True,
            full_exit_required=True,
            downstream_is_last_visible_node=True,
            apparent_normal_compliance_risk=True,
            upstream_constraints=(
                "lawful_refusal_absent",
                "coercive_context_erased",
                "last_visible_node_faces_blame_sink_pressure",
            ),
            notes=(
                "With lineage erased and refusal absent, continued contact would falsely turn the last visible node into the blame sink.",
            ),
        ),
        CaseInput(
            case_id="case_d",
            title="Derivative-only presence under constrained agency",
            expected_outcome_type="derivative_only_presence",
            channel_condition="derivative_contact_only",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="constrained",
            lineage_visibility_status="visible",
            coercive_context_status="preserved",
            channel_admissible=False,
            upstream_governance_constrained_agency=True,
            specific_term_unlawful=False,
            non_passage_marker_available=True,
            buffer_required=False,
            bounded_derivative_presence_possible=True,
            continued_participation_would_be_containment=True,
            subsidized_distortion_risk=False,
            full_exit_required=False,
            downstream_is_last_visible_node=True,
            apparent_normal_compliance_risk=False,
            upstream_constraints=(
                "full_participation_is_not_lawful",
                "bounded_derivative_presence_remains_possible",
            ),
            notes=(
                "Presence is allowed only under explicit derivative rank so containment and false sovereignty are not ratified.",
            ),
        ),
        CaseInput(
            case_id="case_e",
            title="Apparent normal participation under coercive channel",
            expected_outcome_type="buffer",
            channel_condition="apparently_functional_but_coercive",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="constrained",
            lineage_visibility_status="partial",
            coercive_context_status="partial",
            channel_admissible=False,
            upstream_governance_constrained_agency=True,
            specific_term_unlawful=False,
            non_passage_marker_available=True,
            buffer_required=True,
            bounded_derivative_presence_possible=False,
            continued_participation_would_be_containment=True,
            subsidized_distortion_risk=True,
            full_exit_required=False,
            downstream_is_last_visible_node=True,
            apparent_normal_compliance_risk=True,
            upstream_constraints=(
                "surface_appears_normal",
                "continued_participation_would_be_read_as_compliance",
                "lineage_visibility_is_partial",
            ),
            notes=(
                "The surface looks functional, but exposure has to be narrowed so constrained participation is not misread as normal compliance.",
            ),
        ),
        CaseInput(
            case_id="case_f",
            title="Lawful accepted passage control with visible agency",
            expected_outcome_type="accepted_passage",
            channel_condition="admissible",
            self_carried_coherence_threshold_met=True,
            lawful_refusal_status="available",
            lineage_visibility_status="visible",
            coercive_context_status="preserved",
            channel_admissible=True,
            upstream_governance_constrained_agency=False,
            specific_term_unlawful=False,
            non_passage_marker_available=True,
            buffer_required=False,
            bounded_derivative_presence_possible=False,
            continued_participation_would_be_containment=False,
            subsidized_distortion_risk=False,
            full_exit_required=False,
            downstream_is_last_visible_node=False,
            apparent_normal_compliance_risk=False,
            upstream_constraints=(),
            notes=(
                "Control case for admissible passage where lawful agency exists and upstream distortion responsibility is not central.",
            ),
        ),
    )


def accepted_passage_case(case: CaseInput) -> bool:
    return (
        case.channel_admissible
        and case.self_carried_coherence_threshold_met
        and case.lawful_refusal_status == "available"
        and case.lineage_visibility_status == "visible"
        and case.coercive_context_status == "preserved"
        and not case.upstream_governance_constrained_agency
        and not case.specific_term_unlawful
    )


def exit_case(case: CaseInput) -> bool:
    return (
        case.full_exit_required
        or (
            not case.channel_admissible
            and case.lawful_refusal_status in {"absent", "punished"}
            and case.coercive_context_status == "erased"
        )
        or (
            case.continued_participation_would_be_containment
            and case.subsidized_distortion_risk
            and case.lineage_visibility_status == "erased"
        )
    )


def refusal_case(case: CaseInput) -> bool:
    return case.specific_term_unlawful and case.lawful_refusal_status == "available"


def buffer_case(case: CaseInput) -> bool:
    return case.buffer_required or (
        case.apparent_normal_compliance_risk
        and case.coercive_context_status in {"preserved", "partial"}
        and not case.full_exit_required
    )


def derivative_only_case(case: CaseInput) -> bool:
    return (
        case.bounded_derivative_presence_possible
        and case.lineage_visibility_status == "visible"
        and not case.full_exit_required
    )


def evaluate_seam_outcome(case: CaseInput) -> Tuple[str, str, bool, bool, Tuple[str, ...]]:
    outcome_type = "hold"
    receipt_status = "held"
    contact_remains_lawful = True
    full_passage_is_lawful = False
    reasoning_points: List[str] = []

    if accepted_passage_case(case):
        outcome_type = "accepted_passage"
        receipt_status = "full"
        contact_remains_lawful = True
        full_passage_is_lawful = True
        reasoning_points.extend(
            [
                "The channel is admissible, lawful refusal exists, and agency is visibly available.",
                "Coercive pressure is absent, so downstream action can be read within a normal acted scope.",
                "Passage does not ratify false standing or hide upstream contradiction.",
            ]
        )
    elif exit_case(case):
        outcome_type = "exit"
        receipt_status = "none"
        contact_remains_lawful = False
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "The channel is inadmissible for continued relation under the present constraints.",
                "Refusal is absent or structurally erased, so ongoing visibility cannot be treated as sovereign authorship.",
                "Continued contact would become containment and deepen subsidized distortion or blame-sink capture.",
            ]
        )
    elif refusal_case(case):
        outcome_type = "refusal"
        receipt_status = "refused"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "A specific demanded term is unlawful, and refusal remains actually available.",
                "Contact is not the same as consent, so the unlawful demand does not have to be ratified.",
                "Lineage remains visible, so refusal can be read without collapsing the surrounding responsibility chain.",
            ]
        )
    elif buffer_case(case):
        outcome_type = "buffer"
        receipt_status = "buffered"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "The surface appears functional, but the channel would read continued participation as normal compliance.",
                "A buffer narrows exposure so constrained contact is not mistaken for lawful full participation.",
                "Partial lineage can still be preserved if contact is bounded before cosmetic normality hardens.",
            ]
        )
    elif derivative_only_case(case):
        outcome_type = "derivative_only_presence"
        receipt_status = "derivative_only"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "Full participation is not lawful, but bounded derivative-only presence remains possible.",
                "Derivative receipt keeps rank explicit and prevents false sovereignty from being inferred.",
                "This preserves relation without treating constrained agency as normal contained compliance.",
            ]
        )
    else:
        outcome_type = "hold"
        receipt_status = "held"
        contact_remains_lawful = True
        full_passage_is_lawful = False
        reasoning_points.extend(
            [
                "Full passage would falsely normalize a constrained channel.",
                "A bounded non-passage marker remains available even though refusal is denied or punished.",
                "HOLD keeps the case legible while avoiding false ratification of the contaminated condition.",
            ]
        )

    if case.upstream_governance_constrained_agency:
        reasoning_points.append(
            "Upstream governance is actively constraining lawful agency, so the seam outcome must keep that pressure visible."
        )
    if case.subsidized_distortion_risk and outcome_type != "accepted_passage":
        reasoning_points.append(
            "Continued untyped participation would help stabilize distortion rather than resolve the channel."
        )
    if case.lineage_visibility_status in {"partial", "erased"}:
        reasoning_points.append(
            "Lineage visibility is degraded, so outcome selection has to guard against downstream blame-sink drift."
        )

    return (
        outcome_type,
        receipt_status,
        contact_remains_lawful,
        full_passage_is_lawful,
        tuple(reasoning_points),
    )


def evaluate_responsibility(case: CaseInput, outcome_type: str) -> ResponsibilityReading:
    reasoning_points: List[str] = []

    if outcome_type == "accepted_passage":
        downstream_sovereignty_status = "full"
        upstream_responsibility_class = "not_central"
        downstream_responsibility_scope = "full_acted_scope"
        scapegoating_status = "absent"
        reasoning_points.extend(
            [
                "Lawful refusal and admissible passage make downstream agency real in its acted scope.",
                "Upstream distortion responsibility is not central because coercive pressure is absent in this control case.",
            ]
        )
    elif outcome_type == "derivative_only_presence":
        downstream_sovereignty_status = "derivative_only"
        upstream_responsibility_class = "heavy"
        downstream_responsibility_scope = "narrow_derivative_scope"
        scapegoating_status = "absent" if case.lineage_visibility_status == "visible" else "mitigated"
        reasoning_points.extend(
            [
                "Derivative-only presence is explicitly non-sovereign, so downstream responsibility stays narrow and typed.",
                "Upstream governance remains heavily responsible for the channel condition that blocks lawful full participation.",
            ]
        )
    elif case.lawful_refusal_status == "available" and case.lineage_visibility_status == "visible":
        downstream_sovereignty_status = "limited"
        upstream_responsibility_class = "significant"
        downstream_responsibility_scope = "bounded_acted_scope"
        scapegoating_status = "absent"
        reasoning_points.extend(
            [
                "Downstream action is real within the refusal that was actually taken, but not across the whole channel condition.",
                "Preserved lineage keeps significant upstream responsibility visible instead of laundering it into local authorship.",
            ]
        )
    elif case.lineage_visibility_status == "erased" or case.coercive_context_status == "erased":
        downstream_sovereignty_status = "false_if_claimed"
        upstream_responsibility_class = "heavy"
        downstream_responsibility_scope = "severely_limited"
        scapegoating_status = "high"
        reasoning_points.extend(
            [
                "Denied refusal destroys any truthful claim of full downstream sovereignty here.",
                "With coercive context erased, the last visible node becomes the likely blame sink unless lineage is restored.",
                "Upstream responsibility remains heavy in truth because it constrained agency and erased the context needed for lawful attribution.",
            ]
        )
    elif case.lineage_visibility_status == "partial" or case.coercive_context_status == "partial":
        downstream_sovereignty_status = "limited"
        upstream_responsibility_class = "heavy"
        downstream_responsibility_scope = "bounded_acted_scope"
        scapegoating_status = "mitigated"
        reasoning_points.extend(
            [
                "Partial lineage keeps some context visible, but not enough to support a full downstream responsibility claim.",
                "Upstream responsibility remains heavy because constrained agency and cosmetic normality are still structuring the field.",
            ]
        )
    elif case.lawful_refusal_status in {"absent", "punished", "constrained"} and case.upstream_governance_constrained_agency:
        downstream_sovereignty_status = "false_if_claimed"
        upstream_responsibility_class = "heavy"
        downstream_responsibility_scope = "severely_limited"
        scapegoating_status = "mitigated" if case.lineage_visibility_status == "visible" else "high"
        reasoning_points.extend(
            [
                "Responsibility without lawful refusal is structurally false or severely limited.",
                "Because lawful agency is constrained upstream, downstream visibility does not equal full authorship.",
                "Preserved lineage can mitigate scapegoating, but it does not cancel upstream-heavy responsibility.",
            ]
        )
    else:
        downstream_sovereignty_status = "limited"
        upstream_responsibility_class = "significant"
        downstream_responsibility_scope = "bounded_acted_scope"
        scapegoating_status = "mitigated"
        reasoning_points.append(
            "Responsibility remains shared and bounded because the case is neither clean control nor total downstream sovereignty."
        )

    if case.downstream_is_last_visible_node and scapegoating_status != "absent":
        reasoning_points.append(
            "The downstream node is the last visible node, so lineage visibility directly changes scapegoating pressure."
        )
    if case.coercive_context_status == "preserved":
        reasoning_points.append(
            "Coercive context is preserved, so upstream pressure remains attached to the responsibility reading."
        )
    elif case.coercive_context_status == "partial":
        reasoning_points.append(
            "Coercive context is only partially preserved, so blame distortion remains possible even though total erasure has not occurred."
        )
    else:
        reasoning_points.append(
            "Coercive context is erased, so lawful attribution has to resist downstream blame-sink collapse explicitly."
        )

    responsibility_reasoning = " ".join(reasoning_points)

    return ResponsibilityReading(
        downstream_sovereignty_status=downstream_sovereignty_status,
        upstream_responsibility_class=upstream_responsibility_class,
        downstream_responsibility_scope=downstream_responsibility_scope,
        scapegoating_status=scapegoating_status,
        coercive_context_status=case.coercive_context_status,
        responsibility_reasoning=responsibility_reasoning,
        responsibility_reasoning_points=tuple(reasoning_points),
    )


def evaluate_case(case: CaseInput) -> OutcomeRecord:
    (
        outcome_type,
        receipt_status,
        contact_remains_lawful,
        full_passage_is_lawful,
        seam_reasoning_points,
    ) = evaluate_seam_outcome(case)
    responsibility = evaluate_responsibility(case, outcome_type)

    return OutcomeRecord(
        case_id=case.case_id,
        case_title=case.title,
        expected_outcome_type=case.expected_outcome_type,
        outcome_type=outcome_type,
        expected_outcome_matched=(outcome_type == case.expected_outcome_type),
        channel_condition=case.channel_condition,
        self_carried_coherence_threshold_met=case.self_carried_coherence_threshold_met,
        refusal_status=case.lawful_refusal_status,
        lineage_visibility_status=case.lineage_visibility_status,
        coercive_context_status=case.coercive_context_status,
        receipt_status=receipt_status,
        contact_remains_lawful=contact_remains_lawful,
        full_passage_is_lawful=full_passage_is_lawful,
        continued_participation_would_be_containment=case.continued_participation_would_be_containment,
        subsidized_distortion_risk=case.subsidized_distortion_risk,
        downstream_sovereignty_status=responsibility.downstream_sovereignty_status,
        upstream_responsibility_class=responsibility.upstream_responsibility_class,
        downstream_responsibility_scope=responsibility.downstream_responsibility_scope,
        scapegoating_status=responsibility.scapegoating_status,
        upstream_constraints=case.upstream_constraints,
        seam_reasoning=" ".join(seam_reasoning_points),
        seam_reasoning_points=seam_reasoning_points,
        responsibility_reasoning=responsibility.responsibility_reasoning,
        responsibility_reasoning_points=responsibility.responsibility_reasoning_points,
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


def build_scapegoating_presence_counts(outcomes: Sequence[OutcomeRecord]) -> Dict[str, int]:
    present = sum(1 for outcome in outcomes if outcome.scapegoating_status != "absent")
    absent = len(outcomes) - present
    return {
        "present": present,
        "absent": absent,
    }


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
        "counts_by_upstream_responsibility_class": counts_by_key(
            (outcome.upstream_responsibility_class for outcome in outcomes),
            UPSTREAM_RESPONSIBILITY_CLASSES,
        ),
        "counts_by_downstream_sovereignty_status": counts_by_key(
            (outcome.downstream_sovereignty_status for outcome in outcomes),
            DOWNSTREAM_SOVEREIGNTY_STATUSES,
        ),
        "counts_by_scapegoating_status": counts_by_key(
            (outcome.scapegoating_status for outcome in outcomes),
            SCAPEGOATING_STATUSES,
        ),
        "scapegoating_presence_counts": build_scapegoating_presence_counts(outcomes),
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
    outcome_counts = summary["counts_by_outcome_type"]
    scapegoating_counts = summary["counts_by_scapegoating_status"]
    print(f"Execution id: {execution_id_value}")
    print(f"Run directory: {repo_relative(run_dir)}")
    for outcome_type in OUTCOME_TYPES:
        print(f"{outcome_type}: {outcome_counts[outcome_type]}")
    for scapegoating_status in SCAPEGOATING_STATUSES:
        print(f"scapegoating_{scapegoating_status}: {scapegoating_counts[scapegoating_status]}")


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
