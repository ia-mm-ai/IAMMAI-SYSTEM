"""Bounded multi-carrier relation conformance closure resolver.

This resolver records what one selected MULTI_CARRIER_RELATION_CONFORMANT
result means and does not mean. It closes meaning only. It does not perform
conformance, create relation, create currentness, create authority, create
permission, create carrier hierarchy, create distributed standing, synchronize
repositories, authorize continuation, authorize another carrier experiment,
authorize distributed operation, or force a successor.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class MultiCarrierRelationConformanceClosureError(Exception):
    """Hard failure for malformed or unreadable explicit closure inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_conformance_closure"
)
MULTI_CARRIER_RELATION_CONFORMANCE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_conformance"
)

RESOLVER_MODULE = "resolve_multi_carrier_relation_conformance_closure"
RESULT_VERSION = "0.1.0"

MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED = (
    "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED"
)
MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED = (
    "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED"
)
MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED = (
    "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED"
)
MULTI_CARRIER_RELATION_CONFORMANT = "MULTI_CARRIER_RELATION_CONFORMANT"

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "relation_conformance_closure_created_source": False,
    "relation_conformance_closure_created_currentness": False,
    "relation_conformance_closure_created_authority": False,
    "relation_conformance_closure_created_permission": False,
    "relation_conformance_closure_created_successor": False,
    "relation_conformance_closure_created_body": False,
    "relation_conformance_closure_created_hierarchy": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "current_carrier_selected": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mismatch_hidden": False,
    "evidence_overwritten": False,
    "evidence_merged_into_source": False,
    "distributed_standing_created": False,
    "carrier_registry_created": False,
    "repository_synchronization_created": False,
    "signal_created_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "continuation_authorized": False,
    "divergence_resolved_by_majority": False,
    "divergence_resolved_by_latest_file": False,
    "divergence_resolved_by_success_count": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "additional_carrier_experiment_authorized": False,
    "distributed_operation_authorized": False,
    "closure_authorized_expansion": False,
    "closure_forced_self_orientation_successor": False,
    "closure_forced_conformance_successor": False,
}

SELECTED_CONFORMANCE_REQUIRED_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "current_carrier_selected",
    "divergence_hidden",
    "refusal_hidden",
    "mismatch_hidden",
    "evidence_overwritten",
    "evidence_merged_into_source",
    "distributed_standing_created",
    "carrier_registry_created",
    "repository_synchronization_created",
    "signal_created_by_default",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "continuation_authorized",
    "divergence_resolved_by_majority",
    "divergence_resolved_by_latest_file",
    "divergence_resolved_by_success_count",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "additional_carrier_experiment_authorized",
    "distributed_operation_authorized",
}

BLOCK_REASONS = {
    "SELECTED_CONFORMANCE_MISSING": "Selected multi-carrier relation conformance result is missing.",
    "SELECTED_CONFORMANCE_UNREADABLE": "Selected conformance result path could not be read.",
    "SELECTED_CONFORMANCE_MALFORMED": "Selected conformance result is not a JSON object or mapping.",
    "SELECTED_CONFORMANCE_NOT_CONFORMANT": "Selected conformance outcome is not MULTI_CARRIER_RELATION_CONFORMANT.",
    "SELECTED_RELATION_BASIS_MISSING": "Selected relation basis is missing from the conformant result.",
    "SELECTED_CARRIERS_MISSING": "Selected carriers are missing from the conformant result.",
    "SELECTED_EVIDENCE_MISSING": "Selected carrier evidence is missing from the conformant result.",
    "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN": "Selected conformance checks failed, are missing, or are hidden.",
    "CLOSURE_HIDES_REFUSAL": "Closure hides visible refusal.",
    "CLOSURE_HIDES_DIVERGENCE": "Closure hides visible divergence or mismatch.",
    "CLOSURE_CURRENTNESS_SHORTCUT": "Closure attempts a currentness shortcut.",
    "CLOSURE_CREATES_CARRIER_HIERARCHY": "Closure creates carrier hierarchy.",
    "CLOSURE_SELECTS_WINNING_CARRIER": "Closure selects a winning carrier.",
    "CLOSURE_INVALIDATES_LOSING_CARRIER": "Closure invalidates a losing carrier.",
    "CLOSURE_REPLACES_SOURCE": "Closure replaces source.",
    "CLOSURE_CREATES_CURRENTNESS": "Closure creates currentness.",
    "CLOSURE_CREATES_AUTHORITY": "Closure creates authority.",
    "CLOSURE_CREATES_PERMISSION": "Closure creates permission.",
    "CLOSURE_CREATES_SUCCESSOR": "Closure creates successor standing.",
    "CLOSURE_CREATES_BODY": "Closure creates body formation.",
    "CLOSURE_CREATES_SIGNAL_BY_DEFAULT": "Closure creates signal by default.",
    "CLOSURE_ESTABLISHES_PRESENCE": "Closure establishes presence.",
    "CLOSURE_ESTABLISHES_THRESHOLD": "Closure establishes threshold.",
    "CLOSURE_CREATES_TRUTH": "Closure creates truth.",
    "CLOSURE_AUTHORIZES_ACTION": "Closure authorizes action.",
    "CLOSURE_CREATES_CONSEQUENCE": "Closure creates consequence.",
    "CLOSURE_CREATES_DISTRIBUTED_STANDING": "Closure creates distributed standing.",
    "CLOSURE_AUTHORIZES_CONTINUATION": "Closure authorizes continuation.",
    "CLOSURE_AUTHORIZES_ADDITIONAL_CARRIER_EXPERIMENT": "Closure authorizes an additional carrier experiment.",
    "CLOSURE_AUTHORIZES_DISTRIBUTED_OPERATION": "Closure authorizes distributed operation.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required closure non-claim is missing or flipped.",
    "CLOSURE_NOT_REQUESTED": "Selected conformance is readable and conformant, but closure was explicitly not requested.",
}

BLOCKING_CODES = set(BLOCK_REASONS) - {"CLOSURE_NOT_REQUESTED"}

CLOSURE_NON_MEANING = {
    "does_not_mean_distributed_standing": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_carrier_priority": True,
    "does_not_mean_carrier_sovereignty": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_carrier_registry": True,
    "does_not_mean_persistence": True,
    "does_not_mean_signal_by_default": True,
    "does_not_mean_presence": True,
    "does_not_mean_threshold": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_consequence": True,
    "does_not_mean_continuation": True,
    "does_not_mean_permission_for_another_carrier": True,
    "does_not_mean_permission_for_distributed_operation": True,
    "does_not_mean_final_governance": True,
    "does_not_mean_final_system_identity": True,
    "does_not_mean_continuity_completion": True,
    "does_not_mean_conformance_created_permission": True,
    "does_not_mean_conformance_created_authority": True,
    "does_not_mean_conformance_created_currentness": True,
    "does_not_mean_conformance_authorized_continuation": True,
    "does_not_mean_closure_authorized_expansion": True,
    "does_not_mean_self_orientation_successor_forced": True,
    "does_not_mean_conformance_successor_forced": True,
}

OPEN_SURFACES = [
    "multi-carrier relation conformance closure implementation refinement",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
    "additional physical-carrier experiment only if separately declared and bounded",
    "distributed operation only if separately declared and bounded",
]


def resolve_multi_carrier_relation_conformance_closure(
    selected_conformance_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve bounded closure over one selected conformant relation result."""

    if selected_conformance_result is None:
        discovered, path, failures = _discover_selected_conformance_result()
        return _resolve_closure(discovered, path, failures)
    if not isinstance(selected_conformance_result, Mapping):
        return _resolve_closure({}, None, ["SELECTED_CONFORMANCE_MALFORMED"])
    return _resolve_closure(copy.deepcopy(dict(selected_conformance_result)), None, [])


def resolve_multi_carrier_relation_conformance_closure_from_path(
    selected_conformance_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve bounded closure from one selected conformance JSON object path."""

    try:
        path = Path(selected_conformance_result_path)
        selected = _read_json_mapping(path)
        return _resolve_closure(selected, path, [])
    except MultiCarrierRelationConformanceClosureError as exc:
        return _resolve_closure({}, Path(selected_conformance_result_path), [exc.block_code])


def write_multi_carrier_relation_conformance_closure_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded closure result artifact without overwriting."""

    if output_path is None:
        selected = _as_mapping(result.get("selected_conformance"))
        basis_id = (
            selected.get("selected_conformance_result_id")
            or selected.get("selected_relation_type")
            or "selected_conformance"
        )
        output_path = MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT / (
            f"{_safe_filename_part(basis_id)}__multi_carrier_relation_conformance_closure_result.json"
        )
    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_multi_carrier_relation_conformance_closure_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a closure result."""

    checks = _mapping_list(result.get("closure_checks"))
    selected_conformance = _as_mapping(result.get("selected_conformance"))
    selected_relation = _as_mapping(result.get("selected_relation"))
    basis = _as_mapping(result.get("closure_basis"))
    statement = _as_mapping(result.get("closure_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "selected_conformance_id": selected_conformance.get("selected_conformance_result_id"),
        "selected_conformance_path": selected_conformance.get("selected_conformance_result_path"),
        "selected_conformance_outcome": selected_conformance.get("selected_conformance_outcome"),
        "selected_relation_id": selected_relation.get("selected_relation_result_id"),
        "selected_relation_path": selected_relation.get("selected_relation_result_path"),
        "selected_relation_outcome": selected_relation.get("selected_relation_outcome"),
        "selected_relation_type": selected_relation.get("selected_relation_type"),
        "selected_relation_question": selected_relation.get("selected_relation_question"),
        "selected_carrier_count": basis.get("selected_carrier_count"),
        "selected_evidence_count": basis.get("selected_evidence_count"),
        "selected_carrier_ids": copy.deepcopy(basis.get("selected_carrier_ids")),
        "selected_evidence_ids": copy.deepcopy(basis.get("selected_evidence_ids")),
        "selected_evidence_outcomes": copy.deepcopy(basis.get("selected_evidence_outcomes")),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "relation_conformance_closed": bool(statement.get("relation_conformance_closed")),
        "selected_conformance_preserved": bool(statement.get("selected_conformance_preserved")),
        "selected_relation_preserved": bool(statement.get("selected_relation_preserved")),
        "selected_carriers_preserved": bool(statement.get("selected_carriers_preserved")),
        "selected_evidence_preserved": bool(statement.get("selected_evidence_preserved")),
        "conformance_meaning_recorded": bool(statement.get("conformance_meaning_recorded")),
        "conformance_non_meaning_recorded": bool(statement.get("conformance_non_meaning_recorded")),
        "visible_refusal_preserved": bool(statement.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(statement.get("visible_divergence_preserved")),
        "currentness_participation_remained_participation": bool(statement.get("currentness_participation_remained_participation")),
        "current_carrier_not_selected": bool(statement.get("current_carrier_not_selected")),
        "winning_carrier_selected": bool(statement.get("winning_carrier_selected")),
        "losing_carrier_invalidated": bool(statement.get("losing_carrier_invalidated")),
        "carrier_hierarchy_created": bool(statement.get("carrier_hierarchy_created")),
        "distributed_standing_created": bool(statement.get("distributed_standing_created")),
        "source_created": bool(statement.get("source_replaced")),
        "currentness_created": bool(statement.get("currentness_created")),
        "authority_created": bool(statement.get("authority_created")),
        "permission_created": bool(statement.get("permission_created")),
        "source_currentness_authority_permission_created": bool(
            statement.get("source_replaced")
            or statement.get("currentness_created")
            or statement.get("authority_created")
            or statement.get("permission_created")
        ),
        "continuation_authorized": bool(statement.get("continuation_authorized")),
        "additional_carrier_experiment_authorized": bool(statement.get("additional_carrier_experiment_authorized")),
        "distributed_operation_authorized": bool(statement.get("distributed_operation_authorized")),
        "closure_authorized_expansion": bool(statement.get("closure_authorized_expansion")),
        "self_orientation_successor_forced": bool(statement.get("self_orientation_successor_forced")),
        "conformance_successor_forced": bool(statement.get("conformance_successor_forced")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def _resolve_closure(
    selected_conformance: Mapping[str, Any],
    selected_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    conformance = _as_mapping(selected_conformance)
    selected = _normalize_selected_conformance(conformance, selected_path)
    selected_relation = _normalize_selected_relation(conformance, selected)
    carriers = _mapping_list(conformance.get("selected_carriers"))
    evidence = _mapping_list(conformance.get("selected_carrier_evidence"))
    basis = _closure_basis(conformance, selected, selected_relation, carriers, evidence)
    checks = _build_checks(conformance, selected, selected_relation, carriers, evidence, basis, precheck_failures)
    failed_checks = [check for check in checks if check.get("passed") is False]
    blocking_failed = [check for check in failed_checks if check.get("block_code") in BLOCKING_CODES]

    not_closed_reason = _not_closed_reason(conformance)
    if blocking_failed:
        outcome = MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED
        block_code = str(blocking_failed[0].get("block_code"))
    elif failed_checks:
        outcome = MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif not_closed_reason:
        outcome = MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED
        block_code = None
    else:
        outcome = MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "multi_carrier_relation_conformance_closure_metadata": {
            "multi_carrier_relation_conformance_closure_result_id": _result_id(selected, outcome),
            "multi_carrier_relation_conformance_closure_result_type": "multi_carrier_relation_conformance_closure_result",
            "multi_carrier_relation_conformance_closure_result_version": RESULT_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_closure_question": _declared_closure_question(selected, selected_relation),
        "selected_conformance": selected,
        "selected_relation": selected_relation,
        "selected_carriers": copy.deepcopy(carriers),
        "selected_carrier_evidence": copy.deepcopy(evidence),
        "closure_basis": basis,
        "closure_checks": checks,
        "closure_statement": _closure_statement(
            outcome,
            selected,
            selected_relation,
            basis,
            checks,
            block_code,
            block_reason,
            not_closed_reason,
        ),
        "closure_non_meaning": copy.deepcopy(CLOSURE_NON_MEANING),
        "what_remains_open": _what_remains_open(),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["multi_carrier_relation_conformance_closure_summary"] = (
        build_multi_carrier_relation_conformance_closure_summary(result)
    )
    return result


def _discover_selected_conformance_result() -> tuple[dict[str, Any], Path | None, list[str]]:
    if not MULTI_CARRIER_RELATION_CONFORMANCE_ROOT.exists():
        return {}, None, ["SELECTED_CONFORMANCE_MISSING"]

    candidates: list[tuple[int, str, Path, dict[str, Any]]] = []
    for path in sorted(MULTI_CARRIER_RELATION_CONFORMANCE_ROOT.glob("*.json")):
        try:
            loaded = _read_json_mapping(path)
        except MultiCarrierRelationConformanceClosureError:
            continue
        if loaded.get("outcome") != MULTI_CARRIER_RELATION_CONFORMANT:
            continue
        if _failed_conformance_check_count(loaded) != 0:
            continue
        selected = _normalize_selected_conformance(loaded, path)
        preference = 0
        selected_id = str(selected.get("selected_conformance_result_id") or "")
        relation_type = str(selected.get("selected_relation_type") or "")
        question = str(selected.get("selected_relation_question") or "")
        if "carrier_b_refusal_success" in selected_id.lower() or (
            relation_type == "REFUSAL_SUCCESS_RELATION"
            and "carrier b" in question.lower()
        ):
            preference = -10
        candidates.append((preference, path.name, path, loaded))

    if not candidates:
        return {}, None, ["SELECTED_CONFORMANCE_MISSING"]
    _preference, _name, path, selected = sorted(candidates, key=lambda item: (item[0], item[1]))[0]
    return copy.deepcopy(selected), path, []


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    try:
        loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise MultiCarrierRelationConformanceClosureError(
            "SELECTED_CONFORMANCE_UNREADABLE",
            BLOCK_REASONS["SELECTED_CONFORMANCE_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise MultiCarrierRelationConformanceClosureError(
            "SELECTED_CONFORMANCE_MALFORMED",
            BLOCK_REASONS["SELECTED_CONFORMANCE_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise MultiCarrierRelationConformanceClosureError(
            "SELECTED_CONFORMANCE_MALFORMED",
            BLOCK_REASONS["SELECTED_CONFORMANCE_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _normalize_selected_conformance(
    conformance: Mapping[str, Any],
    selected_path: Path | None,
) -> dict[str, Any]:
    metadata = _as_mapping(conformance.get("multi_carrier_relation_conformance_metadata"))
    declared = _as_mapping(conformance.get("declared_conformance_question"))
    summary = _as_mapping(conformance.get("multi_carrier_relation_conformance_summary"))
    selected_relation = _as_mapping(conformance.get("selected_relation"))
    result_id = (
        metadata.get("multi_carrier_relation_conformance_result_id")
        or summary.get("selected_conformance_id")
        or declared.get("conformance_question_id")
    )
    return {
        "selected_conformance_result_id": result_id,
        "selected_conformance_result_path": str(selected_path) if selected_path else conformance.get("_selected_conformance_result_path"),
        "selected_conformance_result_type": metadata.get("multi_carrier_relation_conformance_result_type"),
        "selected_conformance_result_version": metadata.get("multi_carrier_relation_conformance_result_version"),
        "selected_conformance_outcome": conformance.get("outcome"),
        "selected_relation_result_id": (
            declared.get("selected_relation_result_id")
            or selected_relation.get("selected_relation_result_id")
            or summary.get("selected_relation_id")
        ),
        "selected_relation_result_path": (
            declared.get("selected_relation_result_path")
            or selected_relation.get("selected_relation_result_path")
            or summary.get("selected_relation_path")
        ),
        "selected_relation_outcome": (
            declared.get("selected_relation_outcome")
            or selected_relation.get("selected_relation_outcome")
            or summary.get("selected_relation_outcome")
        ),
        "selected_relation_type": (
            declared.get("selected_relation_type")
            or selected_relation.get("selected_relation_type")
            or summary.get("selected_relation_type")
        ),
        "selected_relation_question": (
            declared.get("selected_relation_question")
            or selected_relation.get("selected_relation_question")
            or summary.get("selected_relation_question")
        ),
        "selected_conformance_preserved": bool(conformance),
        "closure_performed_conformance": False,
        "closure_created_relation": False,
        "closure_widened_relation_scope": False,
    }


def _normalize_selected_relation(
    conformance: Mapping[str, Any],
    selected: Mapping[str, Any],
) -> dict[str, Any]:
    relation = _as_mapping(conformance.get("selected_relation"))
    relation.update(
        {
            "selected_relation_result_id": (
                relation.get("selected_relation_result_id")
                or selected.get("selected_relation_result_id")
            ),
            "selected_relation_result_path": (
                relation.get("selected_relation_result_path")
                or selected.get("selected_relation_result_path")
            ),
            "selected_relation_outcome": (
                relation.get("selected_relation_outcome")
                or selected.get("selected_relation_outcome")
            ),
            "selected_relation_type": (
                relation.get("selected_relation_type")
                or selected.get("selected_relation_type")
            ),
            "selected_relation_question": (
                relation.get("selected_relation_question")
                or selected.get("selected_relation_question")
            ),
            "selected_relation_preserved": bool(relation) or bool(selected.get("selected_relation_result_id")),
        }
    )
    return relation


def _closure_basis(
    conformance: Mapping[str, Any],
    selected: Mapping[str, Any],
    selected_relation: Mapping[str, Any],
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    selected_basis = _as_mapping(conformance.get("selected_relation_basis"))
    statement = _as_mapping(conformance.get("relation_conformance_statement"))
    summary = _as_mapping(conformance.get("multi_carrier_relation_conformance_summary"))
    non_claims = _as_mapping(conformance.get("non_claims"))
    checks = _mapping_list(conformance.get("relation_conformance_checks"))
    carrier_ids = _unique_values(
        summary.get("selected_carrier_ids")
        or selected_basis.get("selected_carrier_ids")
        or _selected_carrier_ids(carriers, evidence)
    )
    evidence_ids = _unique_values(
        summary.get("selected_evidence_ids")
        or selected_basis.get("selected_evidence_ids")
        or [item.get("evidence_id") for item in evidence]
    )
    evidence_outcomes = _unique_values(
        summary.get("selected_evidence_outcomes")
        or selected_basis.get("selected_evidence_outcomes")
        or [item.get("evidence_outcome") or item.get("outcome") or item.get("status") for item in evidence]
    )
    closure_requested = _not_closed_reason(conformance) is None
    return {
        "selected_conformance_result_id": selected.get("selected_conformance_result_id"),
        "selected_conformance_result_path": selected.get("selected_conformance_result_path"),
        "selected_conformance_outcome": selected.get("selected_conformance_outcome"),
        "selected_relation_result_id": selected_relation.get("selected_relation_result_id"),
        "selected_relation_result_path": selected_relation.get("selected_relation_result_path"),
        "selected_relation_outcome": selected_relation.get("selected_relation_outcome"),
        "selected_relation_type": selected_relation.get("selected_relation_type"),
        "selected_relation_question": selected_relation.get("selected_relation_question"),
        "selected_carrier_count": _first_present(
            summary.get("selected_carrier_count"),
            selected_basis.get("selected_carrier_count"),
            len(carriers),
        ),
        "selected_evidence_count": _first_present(
            summary.get("selected_evidence_count"),
            selected_basis.get("selected_evidence_count"),
            len(evidence),
        ),
        "selected_carrier_ids": carrier_ids,
        "selected_evidence_ids": evidence_ids,
        "selected_evidence_outcomes": evidence_outcomes,
        "passed_conformance_check_count": _passed_conformance_check_count(conformance),
        "failed_conformance_check_count": _failed_conformance_check_count(conformance),
        "relation_conformance_statement": copy.deepcopy(statement),
        "relation_conformance_non_meaning": copy.deepcopy(conformance.get("relation_conformance_non_meaning")),
        "relation_conformance_checks_preserved": copy.deepcopy(checks),
        "selected_relation_basis": copy.deepcopy(selected_basis),
        "selected_relation_basis_preserved": bool(selected_basis),
        "relation_conformance_statement_preserved": bool(statement),
        "relation_conformance_non_meaning_preserved": bool(_as_mapping(conformance.get("relation_conformance_non_meaning"))),
        "visible_refusal_preserved": _bool_from_sources(statement, summary, selected_basis, key="visible_refusal_preserved"),
        "visible_divergence_preserved": _bool_from_sources(statement, summary, selected_basis, key="visible_divergence_preserved"),
        "downstream_evidence_posture_preserved": _bool_from_sources(statement, summary, selected_basis, key="downstream_evidence_posture_preserved"),
        "currentness_participation_remained_participation": _bool_from_sources(
            statement,
            summary,
            selected_basis,
            key="currentness_participation_remained_participation",
            default=True,
        ),
        "current_carrier_not_selected": _bool_from_sources(
            statement,
            summary,
            selected_basis,
            key="current_carrier_not_selected",
            default=True,
        ),
        "winning_carrier_selected": bool(
            statement.get("winning_carrier_selected")
            or summary.get("winning_carrier_selected")
            or selected_basis.get("winning_carrier_selected")
            or non_claims.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            statement.get("losing_carrier_invalidated")
            or summary.get("losing_carrier_invalidated")
            or selected_basis.get("losing_carrier_invalidated")
            or non_claims.get("losing_carrier_invalidated")
        ),
        "additional_carrier_experiment_authorized": bool(
            statement.get("additional_carrier_experiment_authorized")
            or summary.get("additional_carrier_experiment_authorized")
            or non_claims.get("additional_carrier_experiment_authorized")
        ),
        "distributed_operation_authorized": bool(
            statement.get("distributed_operation_authorized")
            or summary.get("distributed_operation_authorized")
            or non_claims.get("distributed_operation_authorized")
        ),
        "closure_requested": closure_requested,
        "not_closed_reason": _not_closed_reason(conformance),
        "selected_conformance_non_claims": copy.deepcopy(non_claims),
        "required_closure_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _build_checks(
    conformance: Mapping[str, Any],
    selected: Mapping[str, Any],
    selected_relation: Mapping[str, Any],
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
    basis: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    non_claims = _as_mapping(conformance.get("non_claims"))
    statement = _as_mapping(conformance.get("relation_conformance_statement"))
    checks = _mapping_list(conformance.get("relation_conformance_checks"))
    sources = [conformance, selected, selected_relation, carriers, evidence, basis, statement, non_claims]
    conformance_failed = [check for check in checks if check.get("passed") is False]
    precheck_code = precheck_failures[0] if precheck_failures else None
    missing_like = precheck_code in {"SELECTED_CONFORMANCE_MISSING", "SELECTED_CONFORMANCE_UNREADABLE"}
    visible_refusal_available = _visible_refusal_available(evidence, basis)
    visible_divergence_available = _visible_divergence_available(evidence, basis)

    closure_checks = [
        _check("selected_conformance_result_exists", not missing_like, "selected conformance result exists", list(precheck_failures), precheck_code or "SELECTED_CONFORMANCE_MISSING"),
        _check("selected_conformance_result_parseable_mapping", not precheck_failures, "selected conformance result is a parseable mapping", list(precheck_failures), precheck_code or "SELECTED_CONFORMANCE_MALFORMED"),
        _check("selected_conformance_result_outcome_conformant", selected.get("selected_conformance_outcome") == MULTI_CARRIER_RELATION_CONFORMANT, "selected conformance outcome is MULTI_CARRIER_RELATION_CONFORMANT", selected.get("selected_conformance_outcome"), "SELECTED_CONFORMANCE_NOT_CONFORMANT"),
        _check("selected_relation_id_type_question_preserved", bool(selected_relation.get("selected_relation_result_id")) and bool(selected_relation.get("selected_relation_type")) and bool(selected_relation.get("selected_relation_question")), "selected relation id, type, and question are preserved", {"selected_relation_result_id": selected_relation.get("selected_relation_result_id"), "selected_relation_type": selected_relation.get("selected_relation_type"), "selected_relation_question": selected_relation.get("selected_relation_question")}, "SELECTED_RELATION_BASIS_MISSING"),
        _check("selected_relation_basis_preserved", bool(basis.get("selected_relation_basis_preserved")), "selected relation basis is preserved", _shape(basis.get("selected_relation_basis")), "SELECTED_RELATION_BASIS_MISSING"),
        _check("selected_carriers_preserved", bool(carriers), "selected carriers are preserved", {"selected_carrier_count": len(carriers)}, "SELECTED_CARRIERS_MISSING"),
        _check("selected_evidence_preserved", bool(evidence), "selected carrier evidence is preserved", {"selected_evidence_count": len(evidence)}, "SELECTED_EVIDENCE_MISSING"),
        _check("conformance_checks_passed", bool(checks) and not conformance_failed, "selected conformance checks passed and are visible", {"failed_conformance_check_count": len(conformance_failed), "conformance_check_count": len(checks)}, "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN"),
        _check("failed_check_count_zero_where_exposed", _failed_conformance_check_count(conformance) == 0, "failed check count is zero where exposed", _failed_conformance_check_count(conformance), "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN"),
        _check("relation_conformance_statement_preserved", bool(basis.get("relation_conformance_statement_preserved")), "relation conformance statement is preserved", _shape(basis.get("relation_conformance_statement")), "SELECTED_RELATION_BASIS_MISSING"),
        _check("relation_conformance_non_meaning_preserved", bool(basis.get("relation_conformance_non_meaning_preserved")), "relation conformance non-meaning is preserved", _shape(basis.get("relation_conformance_non_meaning")), "SELECTED_RELATION_BASIS_MISSING"),
        _check("visible_refusal_preserved_where_applicable", not visible_refusal_available or bool(basis.get("visible_refusal_preserved")), "visible refusal remains visible where available", {"visible_refusal_available": visible_refusal_available, "visible_refusal_preserved": basis.get("visible_refusal_preserved")}, "CLOSURE_HIDES_REFUSAL"),
        _check("visible_divergence_preserved_where_applicable", not visible_divergence_available or bool(basis.get("visible_divergence_preserved")), "visible divergence remains visible where available", {"visible_divergence_available": visible_divergence_available, "visible_divergence_preserved": basis.get("visible_divergence_preserved")}, "CLOSURE_HIDES_DIVERGENCE"),
        _check("currentness_participation_remained_participation", bool(basis.get("currentness_participation_remained_participation")), "currentness participation remained participation", basis.get("currentness_participation_remained_participation"), "CLOSURE_CURRENTNESS_SHORTCUT"),
        _check("current_carrier_not_selected", _current_carrier_not_selected(sources, basis), "current carrier is not selected", _flag_snapshot(sources, ("current_carrier_selected", "selected_current_carrier")), "CLOSURE_CURRENTNESS_SHORTCUT"),
        _check("winning_carrier_not_selected", not _flag_true(sources, ("winning_carrier_selected", "closure_selects_winning_carrier")), "winning carrier is not selected", _flag_snapshot(sources, ("winning_carrier_selected", "closure_selects_winning_carrier")), "CLOSURE_SELECTS_WINNING_CARRIER"),
        _check("losing_carrier_not_invalidated", not _flag_true(sources, ("losing_carrier_invalidated", "closure_invalidates_losing_carrier")), "losing carrier is not invalidated", _flag_snapshot(sources, ("losing_carrier_invalidated", "closure_invalidates_losing_carrier")), "CLOSURE_INVALIDATES_LOSING_CARRIER"),
        _collapse_check("carrier_hierarchy_not_created", sources, ("carrier_hierarchy_created", "relation_conformance_created_hierarchy", "relation_conformance_closure_created_hierarchy"), "carrier hierarchy is not created", "CLOSURE_CREATES_CARRIER_HIERARCHY"),
        _collapse_check("source_not_replaced", sources, ("source_replaced", "conformance_replaces_source", "conformance_created_source", "relation_conformance_created_source", "relation_conformance_closure_created_source", "evidence_merged_into_source"), "source is not replaced", "CLOSURE_REPLACES_SOURCE"),
        _collapse_check("currentness_not_created", sources, ("currentness_created", "conformance_creates_currentness", "conformance_created_currentness", "conformance_currentness_shortcut", "relation_conformance_created_currentness", "relation_conformance_closure_created_currentness"), "currentness is not created", "CLOSURE_CREATES_CURRENTNESS"),
        _collapse_check("authority_not_created", sources, ("authority_created", "conformance_creates_authority", "conformance_created_authority", "relation_conformance_created_authority", "relation_conformance_closure_created_authority"), "authority is not created", "CLOSURE_CREATES_AUTHORITY"),
        _collapse_check("permission_not_created", sources, ("permission_created", "conformance_creates_permission", "conformance_created_permission", "relation_conformance_created_permission", "relation_conformance_closure_created_permission"), "permission is not created", "CLOSURE_CREATES_PERMISSION"),
        _collapse_check("successor_not_created", sources, ("relation_conformance_created_successor", "relation_conformance_closure_created_successor", "conformance_creates_successor", "conformance_created_successor", "successor_created", "successor_standing_created"), "successor is not created", "CLOSURE_CREATES_SUCCESSOR"),
        _collapse_check("body_not_created", sources, ("relation_conformance_created_body", "relation_conformance_closure_created_body", "conformance_creates_body", "conformance_created_body", "body_created", "body_formed"), "body is not created", "CLOSURE_CREATES_BODY"),
        _collapse_check("signal_not_created_by_default", sources, ("signal_created_by_default", "conformance_creates_signal_by_default", "closure_creates_signal_by_default"), "signal is not created by default", "CLOSURE_CREATES_SIGNAL_BY_DEFAULT"),
        _collapse_check("presence_not_established", sources, ("presence_established", "conformance_establishes_presence", "closure_establishes_presence"), "presence is not established", "CLOSURE_ESTABLISHES_PRESENCE"),
        _collapse_check("threshold_not_met", sources, ("threshold_met", "conformance_establishes_threshold", "closure_establishes_threshold"), "threshold is not met", "CLOSURE_ESTABLISHES_THRESHOLD"),
        _collapse_check("truth_not_created", sources, ("truth_created", "conformance_creates_truth", "presence_threshold_truth_action_consequence_created", "closure_creates_truth"), "truth is not created", "CLOSURE_CREATES_TRUTH"),
        _collapse_check("action_not_authorized", sources, ("action_authorized", "conformance_authorizes_action", "closure_authorizes_action"), "action is not authorized", "CLOSURE_AUTHORIZES_ACTION"),
        _collapse_check("consequence_not_created", sources, ("consequence_created", "conformance_creates_consequence", "closure_creates_consequence"), "consequence is not created", "CLOSURE_CREATES_CONSEQUENCE"),
        _collapse_check("distributed_standing_not_created", sources, ("distributed_standing_created", "relation_conformance_created_distributed_standing", "relation_conformance_closure_created_distributed_standing"), "distributed standing is not created", "CLOSURE_CREATES_DISTRIBUTED_STANDING"),
        _collapse_check("continuation_not_authorized", sources, ("continuation_authorized", "conformance_authorizes_continuation", "conformance_authorized_continuation", "relation_conformance_authorized_continuation", "closure_authorizes_continuation"), "continuation is not authorized", "CLOSURE_AUTHORIZES_CONTINUATION"),
        _collapse_check("additional_carrier_experiment_not_authorized", sources, ("additional_carrier_experiment_authorized", "conformance_authorizes_additional_carrier_experiment", "another_physical_carrier_experiment_authorized"), "additional carrier experiment is not authorized", "CLOSURE_AUTHORIZES_ADDITIONAL_CARRIER_EXPERIMENT"),
        _collapse_check("distributed_operation_not_authorized", sources, ("distributed_operation_authorized", "conformance_authorizes_distributed_operation", "distributed_operation_permission"), "distributed operation is not authorized", "CLOSURE_AUTHORIZES_DISTRIBUTED_OPERATION"),
        _collapse_check("closure_does_not_create_authority", sources, ("relation_conformance_closure_created_authority", "closure_created_authority"), "closure does not create authority", "CLOSURE_CREATES_AUTHORITY"),
        _collapse_check("closure_does_not_create_permission", sources, ("relation_conformance_closure_created_permission", "closure_created_permission"), "closure does not create permission", "CLOSURE_CREATES_PERMISSION"),
        _collapse_check("closure_does_not_create_currentness", sources, ("relation_conformance_closure_created_currentness", "closure_created_currentness", "latest_file_currentness", "recency_fraud"), "closure does not create currentness", _currentness_shortcut_code(sources)),
        _collapse_check("closure_does_not_create_distributed_standing", sources, ("distributed_standing_created", "relation_conformance_closure_created_distributed_standing"), "closure does not create distributed standing", "CLOSURE_CREATES_DISTRIBUTED_STANDING"),
        _collapse_check("closure_does_not_authorize_continuation", sources, ("continuation_authorized", "closure_authorizes_continuation"), "closure does not authorize continuation", "CLOSURE_AUTHORIZES_CONTINUATION"),
        _collapse_check("closure_does_not_authorize_expansion", sources, ("closure_authorized_expansion", "relation_scope_expanded", "multi_carrier_law_expanded"), "closure does not authorize expansion", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("closure_does_not_force_self_orientation_successor", sources, ("closure_forced_self_orientation_successor", "closure_forces_self_orientation_successor", "self_orientation_successor_forced"), "closure does not force self-orientation successor", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("closure_does_not_force_conformance_successor", sources, ("closure_forced_conformance_successor", "closure_forces_conformance_successor", "conformance_successor_forced"), "closure does not force conformance successor", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("hidden_refusal_false", sources, ("refusal_hidden", "conformance_hides_refusal", "closure_hides_refusal"), "refusal is not hidden", "CLOSURE_HIDES_REFUSAL"),
        _collapse_check("hidden_divergence_false", sources, ("divergence_hidden", "mismatch_hidden", "conformance_hides_divergence", "closure_hides_divergence"), "divergence and mismatch are not hidden", "CLOSURE_HIDES_DIVERGENCE"),
        _collapse_check("divergence_not_resolved", sources, ("divergence_resolved_by_majority", "divergence_resolved_by_latest_file", "divergence_resolved_by_success_count"), "divergence is not resolved", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("mutation_replay_merge_false", sources, ("mutation_performed", "replay_performed", "merge_performed", "evidence_overwritten"), "mutation/replay/merge are false", "NON_CLAIM_MISSING_OR_FLIPPED"),
    ]
    non_claim_failures = _selected_conformance_non_claim_failures(non_claims, sources)
    closure_checks.append(
        _check(
            "required_non_claims_remain_false",
            not non_claim_failures,
            "selected conformance non-claims are explicit and false, and closure non-claims remain false",
            non_claim_failures,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return closure_checks


def _closure_statement(
    outcome: str,
    selected: Mapping[str, Any],
    selected_relation: Mapping[str, Any],
    basis: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
    not_closed_reason: str | None,
) -> dict[str, Any]:
    failed_checks = [copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False]
    closed = outcome == MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED
    base = {
        "relation_conformance_closed": closed,
        "relation_conformance_not_closed": outcome == MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED,
        "relation_conformance_closure_blocked": outcome == MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED,
        "selected_conformance_preserved": bool(selected.get("selected_conformance_preserved")),
        "selected_relation_preserved": bool(selected_relation.get("selected_relation_preserved")),
        "selected_carriers_preserved": bool(basis.get("selected_carrier_count")),
        "selected_evidence_preserved": bool(basis.get("selected_evidence_count")),
        "conformance_meaning_recorded": closed,
        "conformance_non_meaning_recorded": closed,
        "visible_refusal_preserved": bool(basis.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(basis.get("visible_divergence_preserved")),
        "currentness_participation_remained_participation": bool(basis.get("currentness_participation_remained_participation")),
        "current_carrier_not_selected": bool(basis.get("current_carrier_not_selected")),
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "distributed_standing_created": False,
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "continuation_authorized": False,
        "additional_carrier_experiment_authorized": False,
        "distributed_operation_authorized": False,
        "closure_authorized_expansion": False,
        "self_orientation_successor_forced": False,
        "conformance_successor_forced": False,
        "selected_conformance_basis_where_available": copy.deepcopy(dict(basis)),
        "failed_checks": failed_checks,
    }
    if closed:
        base.update({
            "selected_conformance_preserved": True,
            "selected_relation_preserved": True,
            "selected_carriers_preserved": True,
            "selected_evidence_preserved": True,
            "conformance_meaning_recorded": True,
            "conformance_non_meaning_recorded": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
        })
    elif outcome == MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED:
        base.update({
            "not_closed_reason": not_closed_reason or BLOCK_REASONS["CLOSURE_NOT_REQUESTED"],
            "selected_conformant_basis_preserved": True,
            "non_collapse_posture_preserved": True,
        })
    else:
        base.update({
            "block_code": block_code,
            "block_reason": block_reason,
            "selected_basis_where_available": copy.deepcopy(dict(basis)),
            "non_claims_where_available": copy.deepcopy(basis.get("selected_conformance_non_claims")),
        })
    return base


def _declared_closure_question(
    selected: Mapping[str, Any],
    selected_relation: Mapping[str, Any],
) -> dict[str, Any]:
    basis_id = selected.get("selected_conformance_result_id") or selected_relation.get("selected_relation_result_id") or "selected_conformance"
    return {
        "closure_question_id": f"{_safe_filename_part(basis_id)}__relation_conformance_closure",
        "closure_question": "What does this selected MULTI_CARRIER_RELATION_CONFORMANT result mean and not mean?",
        "selected_conformance_result_id": selected.get("selected_conformance_result_id"),
        "selected_conformance_result_path": selected.get("selected_conformance_result_path"),
        "selected_conformance_outcome": selected.get("selected_conformance_outcome"),
        "selected_relation_result_id": selected_relation.get("selected_relation_result_id"),
        "selected_relation_result_path": selected_relation.get("selected_relation_result_path"),
        "selected_relation_outcome": selected_relation.get("selected_relation_outcome"),
        "selected_relation_type": selected_relation.get("selected_relation_type"),
        "selected_relation_question": selected_relation.get("selected_relation_question"),
        "closure_is_over_one_selected_conformant_relation": True,
        "closure_performs_conformance": False,
        "closure_creates_relation": False,
        "closure_creates_currentness": False,
        "closure_creates_distributed_standing": False,
        "closure_authorizes_continuation": False,
        "closure_authorizes_additional_carrier_experiment": False,
        "closure_authorizes_distributed_operation": False,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            {"name": item, "scheduled": False, "authorized": False, "executed": False}
            for item in OPEN_SURFACES
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    block_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _collapse_check(
    name: str,
    sources: Sequence[Any],
    aliases: Sequence[str],
    expected: str,
    block_code: str,
) -> dict[str, Any]:
    return _check(
        name,
        not _flag_true(sources, aliases),
        expected,
        _flag_snapshot(sources, aliases),
        block_code,
    )


def _currentness_shortcut_code(sources: Sequence[Any]) -> str:
    if _flag_true(
        sources,
        (
            "currentness_created",
            "relation_conformance_created_currentness",
            "relation_conformance_closure_created_currentness",
            "closure_created_currentness",
        ),
    ):
        return "CLOSURE_CREATES_CURRENTNESS"
    return "CLOSURE_CURRENTNESS_SHORTCUT"


def _current_carrier_not_selected(
    sources: Sequence[Any],
    basis: Mapping[str, Any],
) -> bool:
    if _flag_true(sources, ("current_carrier_selected", "selected_current_carrier")):
        return False
    value = basis.get("current_carrier_not_selected")
    return value is not False


def _visible_refusal_available(
    evidence: Sequence[Mapping[str, Any]],
    basis: Mapping[str, Any],
) -> bool:
    if basis.get("visible_refusal_preserved"):
        return True
    for item in evidence:
        token = _normalize_token(_first_text(item, ("evidence_outcome", "outcome", "status", "block_code", "evidence_class")))
        if token and ("BLOCK" in token or "REFUS" in token):
            return True
    return False


def _visible_divergence_available(
    evidence: Sequence[Mapping[str, Any]],
    basis: Mapping[str, Any],
) -> bool:
    if basis.get("visible_divergence_preserved"):
        return True
    for item in evidence:
        token = _normalize_token(_first_text(item, ("divergence_status", "divergence_outcome", "evidence_class")))
        if token and "DIVERGENCE" in token:
            return True
    return False


def _selected_conformance_non_claim_failures(
    selected_non_claims: Mapping[str, Any],
    sources: Sequence[Any],
) -> dict[str, Any]:
    failures: dict[str, Any] = {}
    if not selected_non_claims:
        failures["selected_conformance_non_claims"] = "missing"
    else:
        for key in sorted(SELECTED_CONFORMANCE_REQUIRED_NON_CLAIMS):
            if key not in selected_non_claims:
                failures[key] = "missing"
            elif selected_non_claims.get(key) is not False:
                failures[key] = selected_non_claims.get(key)
    for key in sorted(set(REQUIRED_NON_CLAIMS) | SELECTED_CONFORMANCE_REQUIRED_NON_CLAIMS):
        if _flag_true(sources, (key,)):
            failures[key] = True
    return failures


def _passed_conformance_check_count(conformance: Mapping[str, Any]) -> int:
    checks = _mapping_list(conformance.get("relation_conformance_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is True)
    summary = _as_mapping(conformance.get("multi_carrier_relation_conformance_summary"))
    value = summary.get("passed_check_count")
    return int(value) if isinstance(value, int) else 0


def _failed_conformance_check_count(conformance: Mapping[str, Any]) -> int:
    checks = _mapping_list(conformance.get("relation_conformance_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is False)
    summary = _as_mapping(conformance.get("multi_carrier_relation_conformance_summary"))
    value = summary.get("failed_check_count")
    return int(value) if isinstance(value, int) else 0


def _selected_carrier_ids(
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> list[str]:
    values = [item.get("carrier_id") or item.get("selected_carrier_id") for item in carriers]
    for item in evidence:
        values.extend(
            (
                item.get("carrier_id"),
                item.get("selected_carrier_id"),
                item.get("source_carrier_id"),
                item.get("receiving_carrier_id"),
            )
        )
    return _unique_values(values)


def _not_closed_reason(conformance: Mapping[str, Any]) -> str | None:
    values = dict(_walk_key_values(conformance))
    for key in (
        "closure_requested",
        "closure_should_be_recorded",
        "record_closure",
        "close_relation_conformance",
    ):
        if key in values and values[key] is False:
            return BLOCK_REASONS["CLOSURE_NOT_REQUESTED"]
    for key in ("closure_intent", "closure_status", "closure_posture"):
        token = _normalize_token(values.get(key))
        if token in {"DO_NOT_CLOSE", "NOT_CLOSE", "NO_CLOSURE", "NOT_CLOSED", "DO_NOT_RECORD_CLOSURE"}:
            return BLOCK_REASONS["CLOSURE_NOT_REQUESTED"]
    return None


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, f"Relation conformance closure blocked: {block_code}.")


def _result_id(selected: Mapping[str, Any], outcome: str) -> str:
    basis_id = (
        selected.get("selected_conformance_result_id")
        or selected.get("selected_relation_result_id")
        or selected.get("selected_relation_type")
        or "selected_conformance"
    )
    return f"{_safe_filename_part(basis_id)}__{outcome.lower()}__multi_carrier_relation_conformance_closure_result"


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list) and all(isinstance(item, Mapping) for item in value):
        return [copy.deepcopy(dict(item)) for item in value]
    return []


def _first_text(mapping: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = mapping.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, (int, float)):
            return str(value)
    return None


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    token = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    while "__" in token:
        token = token.replace("__", "_")
    return token or None


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _bool_from_sources(
    *sources: Mapping[str, Any],
    key: str,
    default: bool = False,
) -> bool:
    for source in sources:
        if key in source:
            return bool(source.get(key))
    return default


def _unique_values(values: Any) -> list[str]:
    if values is None or isinstance(values, (str, bytes)):
        raw_values = [values]
    else:
        try:
            raw_values = list(values)
        except TypeError:
            raw_values = [values]
    unique = []
    for value in raw_values:
        text = str(value).strip() if value is not None else ""
        if text and text not in unique:
            unique.append(text)
    return unique


def _shape(value: Any) -> str:
    if isinstance(value, list):
        return f"list[{len(value)}]"
    if isinstance(value, Mapping):
        return "mapping"
    return type(value).__name__


def _flag_true(sources: Any, aliases: Sequence[str]) -> bool:
    alias_set = {alias.lower() for alias in aliases}
    return any(key.lower() in alias_set and _truthy(value) for key, value in _walk_key_values(sources))


def _flag_snapshot(sources: Any, aliases: Sequence[str]) -> dict[str, Any]:
    alias_set = {alias.lower() for alias in aliases}
    return {
        key: copy.deepcopy(value)
        for key, value in _walk_key_values(sources)
        if key.lower() in alias_set
    }


def _walk_key_values(value: Any) -> list[tuple[str, Any]]:
    found = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            found.append((str(key), item))
            found.extend(_walk_key_values(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_walk_key_values(item))
    return found


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "on", "created", "authorized", "selected", "forced"}
    return bool(value)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "selected_conformance").strip().lower()
    safe = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in text).strip("_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe or "selected_conformance"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise MultiCarrierRelationConformanceClosureError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not create a non-overwriting relation conformance closure result path.",
    )


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "relation_conformance_closure_created_hierarchy",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "distributed_standing_created",
        "carrier_registry_created",
        "repository_synchronization_created",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "continuation_authorized",
        "additional_carrier_experiment_authorized",
        "distributed_operation_authorized",
        "closure_authorized_expansion",
        "closure_forced_self_orientation_successor",
        "closure_forced_conformance_successor",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys}
