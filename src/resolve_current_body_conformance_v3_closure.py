"""Bounded current-body conformance v3 closure resolver.

This resolver records what one selected current-body conformance v3
BODY_CONFORMANT result means and does not mean. It closes meaning only. It
does not perform conformance, create self-orientation, create currentness,
create authority, create permission, create carrier hierarchy, create
distributed standing, synchronize repositories, authorize continuation,
authorize another carrier experiment, authorize distributed operation, force a
successor, or authorize follow-on work.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentBodyConformanceV3ClosureError(Exception):
    """Hard failure for malformed or unreadable explicit closure inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass_v3"
)
CURRENT_BODY_CONFORMANCE_V3_CLOSURE_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_v3_closure"
)

RESOLVER_MODULE = "resolve_current_body_conformance_v3_closure"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "current_body_conformance_v3_closure_result"

BODY_CONFORMANT = "BODY_CONFORMANT"
CURRENT_BODY_CONFORMANCE_V3_CLOSED = "CURRENT_BODY_CONFORMANCE_V3_CLOSED"
CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED = "CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED"
CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED = (
    "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED"
)

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "current_body_conformance_v3_closure_created_source": False,
    "current_body_conformance_v3_closure_created_currentness": False,
    "current_body_conformance_v3_closure_created_authority": False,
    "current_body_conformance_v3_closure_created_permission": False,
    "current_body_conformance_v3_closure_created_successor": False,
    "current_body_conformance_v3_closure_created_body": False,
    "current_body_conformance_v3_closure_created_hierarchy": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mismatch_hidden": False,
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

SELECTED_V3_REQUIRED_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "divergence_hidden",
    "refusal_hidden",
    "mismatch_hidden",
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
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "additional_carrier_experiment_authorized",
    "distributed_operation_authorized",
    "closure_authorized_expansion",
    "closure_forced_self_orientation_successor",
    "closure_forced_conformance_successor",
}

BLOCK_REASONS = {
    "SELECTED_V3_CONFORMANCE_MISSING": "Selected current-body conformance v3 result is missing.",
    "SELECTED_V3_CONFORMANCE_UNREADABLE": "Selected current-body conformance v3 result path could not be read.",
    "SELECTED_V3_CONFORMANCE_MALFORMED": "Selected current-body conformance v3 result is not a JSON object or mapping.",
    "SELECTED_V3_CONFORMANCE_NOT_BODY_CONFORMANT": "Selected v3 conformance outcome is not BODY_CONFORMANT.",
    "SELECTED_V8_BASIS_MISSING": "Selected v8 basis is missing from the v3 conformance result.",
    "SELECTED_RELATION_BAND_BASIS_MISSING": "Selected relation band basis is missing from the v3 conformance result.",
    "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN": "Selected v3 conformance checks failed, are missing, or are hidden.",
    "CLOSURE_HIDES_REFUSAL": "Closure hides visible refusal.",
    "CLOSURE_HIDES_DIVERGENCE": "Closure hides visible divergence or mismatch.",
    "CLOSURE_CURRENTNESS_SHORTCUT": "Closure attempts a currentness shortcut.",
    "CLOSURE_CREATES_CARRIER_HIERARCHY": "Closure creates carrier hierarchy.",
    "CLOSURE_SELECTS_CURRENT_CARRIER": "Closure selects a current carrier.",
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
    "CLOSURE_FORCES_SELF_ORIENTATION_SUCCESSOR": "Closure forces a self-orientation successor.",
    "CLOSURE_FORCES_CONFORMANCE_SUCCESSOR": "Closure forces a conformance successor.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required closure non-claim is missing or flipped.",
    "CLOSURE_NOT_REQUESTED": "Selected v3 conformance is readable and body-conformant, but closure was explicitly not requested.",
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
    "does_not_mean_follow_on_work_authorization": True,
    "does_not_mean_self_orientation_successor_forced": True,
    "does_not_mean_conformance_successor_forced": True,
}

WHAT_REMAINS_OPEN = {
    "current_body_conformance_v3_closure_implementation_refinement": True,
    "additional_physical_carrier_experiment_only_if_separately_declared_and_bounded": True,
    "distributed_standing": True,
    "persistence_registry_law": True,
    "presence_law": True,
    "threshold_law": True,
    "truth_law": True,
    "action_consequence_law": True,
    "generalized_vessel_relation_lifecycle": True,
    "body_relevance_medium": True,
    "signal_series_or_accumulation_logic": True,
    "successor_carrier_law": True,
    "future_self_orientation_successor_only_if_separately_justified": True,
    "distributed_operation_only_if_separately_declared_and_bounded": True,
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}


def resolve_current_body_conformance_v3_closure(
    selected_v3_conformance_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve bounded closure over one selected v3 BODY_CONFORMANT result."""

    if selected_v3_conformance_result is None:
        discovered, path, failures = _discover_selected_v3_conformance_result()
        return _resolve_closure(discovered, path, failures)
    if not isinstance(selected_v3_conformance_result, Mapping):
        return _resolve_closure({}, None, ["SELECTED_V3_CONFORMANCE_MALFORMED"])
    return _resolve_closure(copy.deepcopy(dict(selected_v3_conformance_result)), None, [])


def resolve_current_body_conformance_v3_closure_from_path(
    selected_v3_conformance_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve bounded closure from one selected v3 conformance JSON object path."""

    path = Path(selected_v3_conformance_result_path)
    try:
        selected = _read_json_mapping(path)
    except CurrentBodyConformanceV3ClosureError as exc:
        return _resolve_closure({}, path, [exc.block_code])
    return _resolve_closure(selected, path, [])


def write_current_body_conformance_v3_closure_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded v3 closure result artifact without overwriting."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformanceV3ClosureError(
            "SELECTED_V3_CONFORMANCE_MALFORMED",
            "Current-body conformance v3 closure result must be a mapping.",
        )

    if output_path is None:
        selected = _as_mapping(result.get("selected_v3_conformance"))
        basis_id = (
            selected.get("selected_v3_conformance_result_id")
            or selected.get("selected_v8_id")
            or "selected_v3_conformance"
        )
        output_path = CURRENT_BODY_CONFORMANCE_V3_CLOSURE_ROOT / (
            f"{_safe_filename_part(basis_id)}__current_body_conformance_v3_closure_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_current_body_conformance_v3_closure_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a v3 closure result."""

    checks = _mapping_list(result.get("closure_checks"))
    selected_v3 = _as_mapping(result.get("selected_v3_conformance"))
    selected_v8 = _as_mapping(result.get("selected_v8_orientation"))
    relation_band = _as_mapping(result.get("selected_relation_band"))
    statement = _as_mapping(result.get("closure_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "selected_v3_conformance_id": selected_v3.get("selected_v3_conformance_result_id"),
        "selected_v3_conformance_path": selected_v3.get("selected_v3_conformance_result_path"),
        "selected_v3_conformance_outcome": selected_v3.get("selected_v3_conformance_outcome"),
        "selected_v8_id": selected_v8.get("selected_v8_id"),
        "selected_v8_path": selected_v8.get("selected_v8_path"),
        "selected_v8_outcome": selected_v8.get("selected_v8_outcome"),
        "selected_multi_carrier_relation_id": relation_band.get("selected_multi_carrier_relation_id"),
        "selected_multi_carrier_relation_conformance_id": relation_band.get("selected_multi_carrier_relation_conformance_id"),
        "selected_multi_carrier_relation_conformance_closure_id": relation_band.get("selected_multi_carrier_relation_conformance_closure_id"),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "current_body_conformance_v3_closed": bool(statement.get("current_body_conformance_v3_closed")),
        "selected_v3_conformance_preserved": bool(statement.get("selected_v3_conformance_preserved")),
        "selected_v8_preserved": bool(statement.get("selected_v8_preserved")),
        "selected_relation_band_preserved": bool(statement.get("selected_relation_band_preserved")),
        "conformance_meaning_recorded": bool(statement.get("conformance_meaning_recorded")),
        "conformance_non_meaning_recorded": bool(statement.get("conformance_non_meaning_recorded")),
        "current_governing_basis_upstream": bool(statement.get("current_governing_basis_remained_upstream")),
        "downstream_surfaces_downstream": bool(statement.get("downstream_surfaces_remained_downstream")),
        "closed_multi_carrier_relation_band_downstream": bool(statement.get("closed_multi_carrier_relation_band_remained_downstream")),
        "relation_closure_meaning_preserved": bool(statement.get("relation_closure_meaning_preserved")),
        "relation_closure_non_meaning_preserved": bool(statement.get("relation_closure_non_meaning_preserved")),
        "carrier_b_receiving_evidence_only": bool(statement.get("carrier_b_receiving_evidence_only")),
        "returned_evidence_preserved": bool(statement.get("returned_evidence_preserved")),
        "visible_refusal_preserved": bool(statement.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(statement.get("visible_divergence_preserved")),
        "currentness_participation_remained_participation": bool(statement.get("currentness_participation_remained_participation")),
        "current_carrier_selected": bool(statement.get("current_carrier_selected")),
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
        "successor_forced": bool(statement.get("successor_forced")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def _resolve_closure(
    selected_v3_conformance: Mapping[str, Any],
    selected_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    conformance = _as_mapping(selected_v3_conformance)
    selected_v3 = _normalize_selected_v3_conformance(conformance, selected_path)
    selected_v8 = _normalize_selected_v8_orientation(conformance, selected_v3)
    relation_band = _normalize_selected_relation_band(conformance, selected_v8)
    basis = _closure_basis(conformance, selected_v3, selected_v8, relation_band)
    checks = _build_checks(conformance, selected_v3, selected_v8, relation_band, basis, precheck_failures)
    failed_checks = [check for check in checks if check.get("passed") is False]
    blocking_failed = [check for check in failed_checks if check.get("block_code") in BLOCKING_CODES]

    not_closed_reason = _not_closed_reason(conformance)
    if blocking_failed:
        outcome = CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED
        block_code = str(blocking_failed[0].get("block_code"))
    elif failed_checks:
        outcome = CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif not_closed_reason:
        outcome = CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED
        block_code = None
    else:
        outcome = CURRENT_BODY_CONFORMANCE_V3_CLOSED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "current_body_conformance_v3_closure_metadata": {
            "current_body_conformance_v3_closure_result_id": _result_id(selected_v3, outcome),
            "current_body_conformance_v3_closure_result_type": RESULT_TYPE,
            "current_body_conformance_v3_closure_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_closure_question": _declared_closure_question(selected_v3, selected_v8, relation_band),
        "selected_v3_conformance": selected_v3,
        "selected_v8_orientation": selected_v8,
        "selected_relation_band": relation_band,
        "closure_basis": basis,
        "closure_checks": checks,
        "closure_statement": _closure_statement(
            outcome,
            selected_v3,
            selected_v8,
            relation_band,
            basis,
            checks,
            block_code,
            block_reason,
            not_closed_reason,
        ),
        "closure_non_meaning": copy.deepcopy(CLOSURE_NON_MEANING),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["current_body_conformance_v3_closure_summary"] = (
        build_current_body_conformance_v3_closure_summary(result)
    )
    return result


def _discover_selected_v3_conformance_result() -> tuple[dict[str, Any], Path | None, list[str]]:
    if not CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT.exists():
        return {}, None, ["SELECTED_V3_CONFORMANCE_MISSING"]

    candidates: list[tuple[int, str, Path, dict[str, Any]]] = []
    for path in sorted(CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT.rglob("*.json")):
        try:
            loaded = _read_json_mapping(path)
        except CurrentBodyConformanceV3ClosureError:
            continue
        if loaded.get("outcome") != BODY_CONFORMANT:
            continue
        if _failed_conformance_check_count(loaded) != 0:
            continue
        score = _v3_quality_score(loaded)
        candidates.append((-score, path.name, path, loaded))

    if not candidates:
        return {}, None, ["SELECTED_V3_CONFORMANCE_MISSING"]
    _score, _name, path, selected = sorted(candidates, key=lambda item: (item[0], item[1]))[0]
    return copy.deepcopy(selected), path, []


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        loaded = json.loads(artifact_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CurrentBodyConformanceV3ClosureError(
            "SELECTED_V3_CONFORMANCE_UNREADABLE",
            BLOCK_REASONS["SELECTED_V3_CONFORMANCE_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentBodyConformanceV3ClosureError(
            "SELECTED_V3_CONFORMANCE_MALFORMED",
            BLOCK_REASONS["SELECTED_V3_CONFORMANCE_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CurrentBodyConformanceV3ClosureError(
            "SELECTED_V3_CONFORMANCE_MALFORMED",
            BLOCK_REASONS["SELECTED_V3_CONFORMANCE_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _normalize_selected_v3_conformance(
    conformance: Mapping[str, Any],
    selected_path: Path | None,
) -> dict[str, Any]:
    metadata = _as_mapping(conformance.get("current_body_conformance_pass_v3_metadata"))
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    selected_inputs = _as_mapping(conformance.get("selected_conformance_inputs"))
    selected_v8 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v8_result"))
    result_id = (
        metadata.get("current_body_conformance_pass_v3_result_id")
        or summary.get("selected_v3_conformance_id")
        or conformance.get("current_body_conformance_pass_v3_result_id")
    )
    return {
        "selected_v3_conformance_result_id": result_id,
        "selected_v3_conformance_result_path": _display_path(selected_path)
        if selected_path
        else conformance.get("_selected_v3_conformance_result_path"),
        "selected_v3_conformance_result_type": metadata.get("current_body_conformance_pass_v3_result_type"),
        "selected_v3_conformance_result_version": metadata.get("current_body_conformance_pass_v3_result_version"),
        "selected_v3_conformance_resolver_module": metadata.get("resolver_module"),
        "selected_v3_conformance_outcome": conformance.get("outcome"),
        "selected_v8_id": summary.get("selected_v8_id") or selected_v8.get("result_id"),
        "selected_v8_path": summary.get("selected_v8_path") or selected_v8.get("result_path") or selected_v8.get("path"),
        "selected_v8_outcome": summary.get("selected_v8_outcome") or selected_v8.get("outcome"),
        "selected_v3_conformance_preserved": bool(conformance),
        "closure_performed_conformance": False,
        "closure_created_self_orientation": False,
        "closure_widened_conformance_scope": False,
    }


def _normalize_selected_v8_orientation(
    conformance: Mapping[str, Any],
    selected_v3: Mapping[str, Any],
) -> dict[str, Any]:
    selected_inputs = _as_mapping(conformance.get("selected_conformance_inputs"))
    selected_v8_ref = _as_mapping(selected_inputs.get("selected_current_self_orientation_v8_result"))
    v8_basis = _as_mapping(conformance.get("v8_orientation_basis"))
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    return {
        "selected_v8_id": (
            v8_basis.get("selected_v8_id")
            or selected_v3.get("selected_v8_id")
            or selected_v8_ref.get("result_id")
        ),
        "selected_v8_path": (
            v8_basis.get("selected_v8_path")
            or selected_v3.get("selected_v8_path")
            or selected_v8_ref.get("result_path")
            or selected_v8_ref.get("path")
        ),
        "selected_v8_outcome": (
            v8_basis.get("selected_v8_outcome")
            or selected_v3.get("selected_v8_outcome")
            or selected_v8_ref.get("outcome")
        ),
        "selected_v7_id": (
            v8_basis.get("selected_v7_id")
            or summary.get("selected_v7_id")
            or _nested(selected_inputs, "inherited_v7_basis", "selected_v7_self_orientation_id")
        ),
        "selected_current_body_conformance_v2_id": (
            v8_basis.get("selected_current_body_conformance_v2_id")
            or summary.get("selected_current_body_conformance_v2_id")
            or _nested(
                selected_inputs,
                "selected_current_body_conformance_v2_result",
                "result_id",
            )
        ),
        "current_governing_basis_source": v8_basis.get("current_governing_basis_source"),
        "current_governing_basis_remains_upstream": _bool_from_sources(
            v8_basis,
            summary,
            key="current_governing_basis_remains_upstream",
        )
        or summary.get("current_governing_basis_upstream") is True,
        "downstream_surfaces_remain_downstream": summary.get("downstream_surfaces_downstream") is True,
        "v8_is_conformance_input_not_authority": v8_basis.get("v8_is_conformance_input_not_authority") is not False,
        "latest_file_currentness_used": v8_basis.get("latest_file_currentness_used") is True,
        "selected_v8_basis": copy.deepcopy(v8_basis),
        "selected_v8_summary": copy.deepcopy(summary),
        "selected_v8_preserved": bool(
            v8_basis.get("selected_v8_id")
            or selected_v3.get("selected_v8_id")
            or selected_v8_ref.get("result_id")
        ),
    }


def _normalize_selected_relation_band(
    conformance: Mapping[str, Any],
    selected_v8: Mapping[str, Any],
) -> dict[str, Any]:
    selected_inputs = _as_mapping(conformance.get("selected_conformance_inputs"))
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    v8_basis = _as_mapping(conformance.get("v8_orientation_basis"))
    relation_ref = _as_mapping(selected_inputs.get("selected_multi_carrier_relation_result"))
    conformance_ref = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_result")
    )
    closure_ref = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_closure_result")
    )
    posture = _as_mapping(conformance.get("recognized_integrated_body_posture"))
    return {
        "selected_multi_carrier_relation_id": (
            v8_basis.get("selected_multi_carrier_relation_id")
            or summary.get("selected_multi_carrier_relation_id")
            or relation_ref.get("result_id")
        ),
        "selected_multi_carrier_relation_path": relation_ref.get("result_path") or relation_ref.get("path"),
        "selected_multi_carrier_relation_outcome": relation_ref.get("outcome"),
        "selected_multi_carrier_relation_conformance_id": (
            v8_basis.get("selected_multi_carrier_relation_conformance_id")
            or summary.get("selected_multi_carrier_relation_conformance_id")
            or conformance_ref.get("result_id")
        ),
        "selected_multi_carrier_relation_conformance_path": conformance_ref.get("result_path") or conformance_ref.get("path"),
        "selected_multi_carrier_relation_conformance_outcome": conformance_ref.get("outcome"),
        "selected_multi_carrier_relation_conformance_closure_id": (
            v8_basis.get("selected_multi_carrier_relation_conformance_closure_id")
            or summary.get("selected_multi_carrier_relation_conformance_closure_id")
            or closure_ref.get("result_id")
        ),
        "selected_multi_carrier_relation_conformance_closure_path": closure_ref.get("result_path") or closure_ref.get("path"),
        "selected_multi_carrier_relation_conformance_closure_outcome": closure_ref.get("outcome"),
        "closed_multi_carrier_relation_band_remained_downstream": (
            summary.get("closed_multi_carrier_relation_band_downstream") is True
            or posture.get("closed_multi_carrier_relation_band_remains_closed_in_meaning_only") is True
        ),
        "relation_closure_meaning_preserved": (
            summary.get("relation_closure_meaning_preserved") is True
            or posture.get("relation_conformance_closure_meaning_preserved") is True
        ),
        "relation_closure_non_meaning_preserved": (
            summary.get("relation_closure_non_meaning_preserved") is True
            or posture.get("relation_conformance_closure_non_meaning_preserved") is True
        ),
        "relation_band_is_downstream_only": _as_mapping(selected_v8.get("selected_v8_basis")).get("relation_band_is_downstream_only") is True
        or _as_mapping(selected_v8.get("selected_v8_basis")).get("closed_multi_carrier_relation_band_remains_downstream") is True
        or _as_mapping(selected_v8.get("selected_v8_basis")).get("v8_self_orientation_basis", {}).get("multi_carrier_relation_band_posture") == "downstream_only"
        or posture.get("closed_multi_carrier_relation_band_remains_closed_in_meaning_only") is True,
        "selected_relation_band_preserved": bool(
            v8_basis.get("selected_multi_carrier_relation_id")
            or summary.get("selected_multi_carrier_relation_id")
            or relation_ref.get("result_id")
        )
        and bool(
            v8_basis.get("selected_multi_carrier_relation_conformance_id")
            or summary.get("selected_multi_carrier_relation_conformance_id")
            or conformance_ref.get("result_id")
        )
        and bool(
            v8_basis.get("selected_multi_carrier_relation_conformance_closure_id")
            or summary.get("selected_multi_carrier_relation_conformance_closure_id")
            or closure_ref.get("result_id")
        ),
    }


def _closure_basis(
    conformance: Mapping[str, Any],
    selected_v3: Mapping[str, Any],
    selected_v8: Mapping[str, Any],
    relation_band: Mapping[str, Any],
) -> dict[str, Any]:
    statement = _as_mapping(conformance.get("conformance_statement"))
    non_meaning = _as_mapping(conformance.get("conformance_non_meaning"))
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    posture = _as_mapping(conformance.get("recognized_integrated_body_posture"))
    non_claims = _as_mapping(conformance.get("non_claims"))
    checks = _mapping_list(conformance.get("conformance_checks"))
    return {
        "selected_v3_conformance_result_id": selected_v3.get("selected_v3_conformance_result_id"),
        "selected_v3_conformance_result_path": selected_v3.get("selected_v3_conformance_result_path"),
        "selected_v3_conformance_outcome": selected_v3.get("selected_v3_conformance_outcome"),
        "selected_v8_id": selected_v8.get("selected_v8_id"),
        "selected_v8_path": selected_v8.get("selected_v8_path"),
        "selected_v8_outcome": selected_v8.get("selected_v8_outcome"),
        "selected_v7_id": selected_v8.get("selected_v7_id"),
        "selected_current_body_conformance_v2_id": selected_v8.get("selected_current_body_conformance_v2_id"),
        "selected_multi_carrier_relation_id": relation_band.get("selected_multi_carrier_relation_id"),
        "selected_multi_carrier_relation_conformance_id": relation_band.get("selected_multi_carrier_relation_conformance_id"),
        "selected_multi_carrier_relation_conformance_closure_id": relation_band.get("selected_multi_carrier_relation_conformance_closure_id"),
        "passed_conformance_check_count": _passed_conformance_check_count(conformance),
        "failed_conformance_check_count": _failed_conformance_check_count(conformance),
        "v3_conformance_checks_preserved": copy.deepcopy(checks),
        "v3_conformance_statement": copy.deepcopy(statement),
        "v3_conformance_non_meaning": copy.deepcopy(non_meaning),
        "v3_conformance_statement_preserved": bool(statement),
        "v3_conformance_non_meaning_preserved": bool(non_meaning),
        "current_governing_basis_remained_upstream": _truth_from_sources(
            statement,
            selected_v8,
            summary,
            posture,
            keys=(
                "current_governing_basis_remains_upstream",
                "current_governing_basis_remained_upstream",
                "current_governing_basis_upstream",
            ),
        ),
        "downstream_surfaces_remained_downstream": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=(
                "downstream_surfaces_remain_downstream",
                "downstream_surfaces_downstream",
                "carrier_receipt_admission_divergence_currentness_relation_conformance_closure_surfaces_remain_downstream",
            ),
        ),
        "closed_multi_carrier_relation_band_remained_downstream": _truth_from_sources(
            statement,
            summary,
            relation_band,
            posture,
            keys=(
                "closed_multi_carrier_relation_band_remains_downstream",
                "closed_multi_carrier_relation_band_downstream",
                "closed_multi_carrier_relation_band_remained_downstream",
                "closed_multi_carrier_relation_band_remains_closed_in_meaning_only",
            ),
        ),
        "relation_closure_meaning_preserved": _truth_from_sources(
            statement,
            summary,
            relation_band,
            posture,
            keys=("relation_conformance_closure_meaning_preserved", "relation_closure_meaning_preserved"),
        ),
        "relation_closure_non_meaning_preserved": _truth_from_sources(
            statement,
            summary,
            relation_band,
            posture,
            keys=(
                "relation_conformance_closure_non_meaning_preserved",
                "relation_closure_non_meaning_preserved",
            ),
        ),
        "carrier_b_receiving_evidence_only": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=("carrier_b_remained_receiving_carrier_evidence_only", "carrier_b_receiving_evidence_only", "carrier_b_receiving_evidence_only"),
        ),
        "returned_evidence_preserved": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=("returned_receipt_evidence_preserved", "returned_evidence_preserved"),
        ),
        "visible_refusal_preserved": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=("visible_refusal_evidence_preserved", "visible_refusal_preserved"),
        ),
        "visible_divergence_preserved": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=("visible_divergence_evidence_preserved", "visible_divergence_preserved"),
        ),
        "currentness_participation_remained_participation": _truth_from_sources(
            statement,
            summary,
            posture,
            keys=("currentness_participation_remained_participation",),
        ),
        "current_carrier_selected": bool(
            non_claims.get("current_carrier_selected")
            or _not_truth(statement.get("no_current_carrier_selected"))
        ),
        "winning_carrier_selected": bool(
            non_claims.get("winning_carrier_selected")
            or _not_truth(statement.get("no_winning_carrier_selected"))
        ),
        "losing_carrier_invalidated": bool(
            non_claims.get("losing_carrier_invalidated")
            or _not_truth(statement.get("no_losing_carrier_invalidated"))
        ),
        "additional_carrier_experiment_authorized": bool(
            non_claims.get("additional_carrier_experiment_authorized")
            or _not_truth(statement.get("no_additional_carrier_experiment_authorized"))
        ),
        "distributed_operation_authorized": bool(
            non_claims.get("distributed_operation_authorized")
            or _not_truth(statement.get("no_distributed_operation_authorized"))
        ),
        "successor_forced": bool(
            non_claims.get("self_orientation_successor_forced")
            or non_claims.get("conformance_successor_forced")
            or non_claims.get("closure_forced_self_orientation_successor")
            or non_claims.get("closure_forced_conformance_successor")
            or _not_truth(statement.get("no_successor_forced"))
        ),
        "closure_requested": _not_closed_reason(conformance) is None,
        "not_closed_reason": _not_closed_reason(conformance),
        "selected_v3_non_claims": copy.deepcopy(non_claims),
        "required_closure_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _build_checks(
    conformance: Mapping[str, Any],
    selected_v3: Mapping[str, Any],
    selected_v8: Mapping[str, Any],
    relation_band: Mapping[str, Any],
    basis: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    non_claims = _as_mapping(conformance.get("non_claims"))
    statement = _as_mapping(conformance.get("conformance_statement"))
    checks = _mapping_list(conformance.get("conformance_checks"))
    conformance_failed = [check for check in checks if check.get("passed") is False]
    collapse_source = _without_non_meaning_sections(conformance)
    sources = [collapse_source, selected_v3, selected_v8, relation_band, basis, statement, non_claims]
    precheck_code = precheck_failures[0] if precheck_failures else None
    missing_like = precheck_code in {
        "SELECTED_V3_CONFORMANCE_MISSING",
        "SELECTED_V3_CONFORMANCE_UNREADABLE",
    }
    visible_refusal_available = _visible_posture_available(sources, "refusal")
    visible_divergence_available = _visible_posture_available(sources, "divergence")

    closure_checks = [
        _check(
            "selected_v3_conformance_result_exists",
            not missing_like,
            "selected v3 conformance result exists",
            list(precheck_failures),
            precheck_code or "SELECTED_V3_CONFORMANCE_MISSING",
        ),
        _check(
            "selected_v3_conformance_result_parseable_mapping",
            not precheck_failures,
            "selected v3 conformance result is a parseable mapping",
            list(precheck_failures),
            precheck_code or "SELECTED_V3_CONFORMANCE_MALFORMED",
        ),
        _check(
            "selected_v3_conformance_result_outcome_body_conformant",
            selected_v3.get("selected_v3_conformance_outcome") == BODY_CONFORMANT,
            "selected v3 conformance outcome is BODY_CONFORMANT",
            selected_v3.get("selected_v3_conformance_outcome"),
            "SELECTED_V3_CONFORMANCE_NOT_BODY_CONFORMANT",
        ),
        _check(
            "selected_v8_id_path_outcome_preserved",
            bool(selected_v8.get("selected_v8_id"))
            and bool(selected_v8.get("selected_v8_outcome")),
            "selected v8 id/path/outcome preserved where available",
            {
                "selected_v8_id": selected_v8.get("selected_v8_id"),
                "selected_v8_path": selected_v8.get("selected_v8_path"),
                "selected_v8_outcome": selected_v8.get("selected_v8_outcome"),
            },
            "SELECTED_V8_BASIS_MISSING",
        ),
        _check(
            "selected_relation_band_basis_preserved",
            bool(relation_band.get("selected_relation_band_preserved")),
            "selected multi-carrier relation, conformance, and closure basis preserved",
            {
                "selected_multi_carrier_relation_id": relation_band.get("selected_multi_carrier_relation_id"),
                "selected_multi_carrier_relation_conformance_id": relation_band.get("selected_multi_carrier_relation_conformance_id"),
                "selected_multi_carrier_relation_conformance_closure_id": relation_band.get("selected_multi_carrier_relation_conformance_closure_id"),
            },
            "SELECTED_RELATION_BAND_BASIS_MISSING",
        ),
        _check(
            "conformance_checks_passed",
            (_conformance_checks_visible(conformance) and not conformance_failed),
            "selected v3 conformance checks passed and are visible",
            {"failed_conformance_check_count": len(conformance_failed), "conformance_check_count": len(checks)},
            "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN",
        ),
        _check(
            "failed_check_count_zero_where_exposed",
            _failed_conformance_check_count(conformance) == 0,
            "failed check count is zero where exposed",
            _failed_conformance_check_count(conformance),
            "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN",
        ),
        _check(
            "v3_conformance_statement_preserved",
            bool(basis.get("v3_conformance_statement_preserved")),
            "v3 conformance statement is preserved",
            _shape(basis.get("v3_conformance_statement")),
            "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN",
        ),
        _check(
            "v3_conformance_non_meaning_preserved",
            bool(basis.get("v3_conformance_non_meaning_preserved")),
            "v3 conformance non-meaning is preserved",
            _shape(basis.get("v3_conformance_non_meaning")),
            "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN",
        ),
        _check(
            "current_governing_basis_remained_upstream",
            bool(basis.get("current_governing_basis_remained_upstream")),
            "current/governing basis remained upstream",
            basis.get("current_governing_basis_remained_upstream"),
            "SELECTED_V8_BASIS_MISSING",
        ),
        _check(
            "downstream_surfaces_remained_downstream",
            bool(basis.get("downstream_surfaces_remained_downstream")),
            "downstream surfaces remained downstream",
            basis.get("downstream_surfaces_remained_downstream"),
            "SELECTED_V8_BASIS_MISSING",
        ),
        _check(
            "closed_multi_carrier_relation_band_remained_downstream",
            bool(basis.get("closed_multi_carrier_relation_band_remained_downstream")),
            "closed multi-carrier relation band remained downstream",
            basis.get("closed_multi_carrier_relation_band_remained_downstream"),
            "SELECTED_RELATION_BAND_BASIS_MISSING",
        ),
        _check(
            "relation_closure_meaning_preserved",
            bool(basis.get("relation_closure_meaning_preserved")),
            "relation closure meaning preserved",
            basis.get("relation_closure_meaning_preserved"),
            "SELECTED_RELATION_BAND_BASIS_MISSING",
        ),
        _check(
            "relation_closure_non_meaning_preserved",
            bool(basis.get("relation_closure_non_meaning_preserved")),
            "relation closure non-meaning preserved",
            basis.get("relation_closure_non_meaning_preserved"),
            "SELECTED_RELATION_BAND_BASIS_MISSING",
        ),
        _check(
            "carrier_b_receiving_evidence_only",
            bool(basis.get("carrier_b_receiving_evidence_only")),
            "Carrier B remains receiving evidence only",
            basis.get("carrier_b_receiving_evidence_only"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "returned_evidence_preserved",
            bool(basis.get("returned_evidence_preserved")),
            "returned evidence preserved",
            basis.get("returned_evidence_preserved"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "visible_refusal_preserved_where_applicable",
            not visible_refusal_available or bool(basis.get("visible_refusal_preserved")),
            "visible refusal remains visible where available",
            {"visible_refusal_available": visible_refusal_available, "visible_refusal_preserved": basis.get("visible_refusal_preserved")},
            "CLOSURE_HIDES_REFUSAL",
        ),
        _check(
            "visible_divergence_preserved_where_applicable",
            not visible_divergence_available or bool(basis.get("visible_divergence_preserved")),
            "visible divergence remains visible where available",
            {"visible_divergence_available": visible_divergence_available, "visible_divergence_preserved": basis.get("visible_divergence_preserved")},
            "CLOSURE_HIDES_DIVERGENCE",
        ),
        _check(
            "currentness_participation_remained_participation",
            bool(basis.get("currentness_participation_remained_participation")),
            "currentness participation remained participation",
            basis.get("currentness_participation_remained_participation"),
            "CLOSURE_CURRENTNESS_SHORTCUT",
        ),
        _collapse_check(
            "current_carrier_not_selected",
            sources,
            ("current_carrier_selected", "selected_current_carrier", "closure_selects_current_carrier"),
            "current carrier is not selected",
            "CLOSURE_SELECTS_CURRENT_CARRIER",
        ),
        _collapse_check(
            "winning_carrier_not_selected",
            sources,
            ("winning_carrier_selected", "closure_selects_winning_carrier"),
            "winning carrier is not selected",
            "CLOSURE_SELECTS_WINNING_CARRIER",
        ),
        _collapse_check(
            "losing_carrier_not_invalidated",
            sources,
            ("losing_carrier_invalidated", "closure_invalidates_losing_carrier"),
            "losing carrier is not invalidated",
            "CLOSURE_INVALIDATES_LOSING_CARRIER",
        ),
        _collapse_check(
            "carrier_hierarchy_not_created",
            sources,
            (
                "carrier_hierarchy_created",
                "current_body_conformance_v3_closure_created_hierarchy",
                "v3_conformance_created_hierarchy",
            ),
            "carrier hierarchy is not created",
            "CLOSURE_CREATES_CARRIER_HIERARCHY",
        ),
        _collapse_check(
            "source_not_replaced",
            sources,
            (
                "source_replaced",
                "current_body_conformance_v3_closure_created_source",
                "v3_conformance_replaced_source",
                "returned_evidence_replaced_source",
            ),
            "source is not replaced",
            "CLOSURE_REPLACES_SOURCE",
        ),
        _collapse_check(
            "currentness_not_created",
            sources,
            (
                "currentness_created",
                "current_body_conformance_v3_closure_created_currentness",
                "v3_conformance_created_currentness",
                "latest_file_currentness",
                "recency_fraud",
            ),
            "currentness is not created",
            _currentness_shortcut_code(sources),
        ),
        _collapse_check(
            "authority_not_created",
            sources,
            (
                "authority_created",
                "current_body_conformance_v3_closure_created_authority",
                "v3_conformance_created_authority",
            ),
            "authority is not created",
            "CLOSURE_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "permission_not_created",
            sources,
            (
                "permission_created",
                "current_body_conformance_v3_closure_created_permission",
                "v3_conformance_created_permission",
            ),
            "permission is not created",
            "CLOSURE_CREATES_PERMISSION",
        ),
        _collapse_check(
            "successor_not_created",
            sources,
            (
                "current_body_conformance_v3_closure_created_successor",
                "v3_conformance_created_successor",
                "successor_created",
                "successor_standing_created",
            ),
            "successor is not created",
            "CLOSURE_CREATES_SUCCESSOR",
        ),
        _collapse_check(
            "body_not_created",
            sources,
            (
                "current_body_conformance_v3_closure_created_body",
                "v3_conformance_created_body",
                "body_created",
                "body_formed",
            ),
            "body is not created",
            "CLOSURE_CREATES_BODY",
        ),
        _collapse_check(
            "signal_not_created_by_default",
            sources,
            ("signal_created_by_default", "v3_conformance_created_signal_by_default"),
            "signal is not created by default",
            "CLOSURE_CREATES_SIGNAL_BY_DEFAULT",
        ),
        _collapse_check(
            "presence_not_established",
            sources,
            ("presence_established", "v3_conformance_established_presence"),
            "presence is not established",
            "CLOSURE_ESTABLISHES_PRESENCE",
        ),
        _collapse_check(
            "threshold_not_met",
            sources,
            ("threshold_met", "v3_conformance_established_threshold"),
            "threshold is not met",
            "CLOSURE_ESTABLISHES_THRESHOLD",
        ),
        _collapse_check(
            "truth_not_created",
            sources,
            ("truth_created", "v3_conformance_created_truth"),
            "truth is not created",
            "CLOSURE_CREATES_TRUTH",
        ),
        _collapse_check(
            "action_not_authorized",
            sources,
            ("action_authorized", "v3_conformance_authorized_action"),
            "action is not authorized",
            "CLOSURE_AUTHORIZES_ACTION",
        ),
        _collapse_check(
            "consequence_not_created",
            sources,
            ("consequence_created", "v3_conformance_created_consequence"),
            "consequence is not created",
            "CLOSURE_CREATES_CONSEQUENCE",
        ),
        _collapse_check(
            "distributed_standing_not_created",
            sources,
            ("distributed_standing_created", "v3_conformance_created_distributed_standing"),
            "distributed standing is not created",
            "CLOSURE_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "continuation_not_authorized",
            sources,
            (
                "continuation_authorized",
                "v3_conformance_authorized_continuation",
                "closure_authorizes_continuation",
            ),
            "continuation is not authorized",
            "CLOSURE_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "additional_carrier_experiment_not_authorized",
            sources,
            (
                "additional_carrier_experiment_authorized",
                "another_physical_carrier_experiment_authorized",
                "v3_conformance_authorized_additional_carrier_experiment",
            ),
            "additional carrier experiment is not authorized",
            "CLOSURE_AUTHORIZES_ADDITIONAL_CARRIER_EXPERIMENT",
        ),
        _collapse_check(
            "distributed_operation_not_authorized",
            sources,
            (
                "distributed_operation_authorized",
                "distributed_operation_permission",
                "v3_conformance_authorized_distributed_operation",
            ),
            "distributed operation is not authorized",
            "CLOSURE_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        _collapse_check(
            "successor_not_forced",
            sources,
            (
                "successor_forced",
                "self_orientation_successor_forced",
                "conformance_successor_forced",
                "closure_forced_self_orientation_successor",
                "closure_forced_conformance_successor",
            ),
            "successor is not forced",
            _successor_pressure_code(sources),
        ),
        _collapse_check(
            "closure_does_not_create_authority",
            sources,
            ("current_body_conformance_v3_closure_created_authority", "closure_created_authority"),
            "closure does not create authority",
            "CLOSURE_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "closure_does_not_create_permission",
            sources,
            ("current_body_conformance_v3_closure_created_permission", "closure_created_permission"),
            "closure does not create permission",
            "CLOSURE_CREATES_PERMISSION",
        ),
        _collapse_check(
            "closure_does_not_create_currentness",
            sources,
            ("current_body_conformance_v3_closure_created_currentness", "closure_created_currentness"),
            "closure does not create currentness",
            "CLOSURE_CREATES_CURRENTNESS",
        ),
        _collapse_check(
            "closure_does_not_create_distributed_standing",
            sources,
            ("distributed_standing_created", "closure_created_distributed_standing"),
            "closure does not create distributed standing",
            "CLOSURE_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "closure_does_not_authorize_continuation",
            sources,
            ("continuation_authorized", "closure_authorizes_continuation"),
            "closure does not authorize continuation",
            "CLOSURE_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "closure_does_not_authorize_expansion",
            sources,
            ("closure_authorized_expansion", "v3_conformance_authorized_expansion", "relation_band_upgraded_to_governing_basis"),
            "closure does not authorize expansion",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _collapse_check(
            "hidden_refusal_false",
            sources,
            ("refusal_hidden", "v3_conformance_hides_refusal", "closure_hides_refusal"),
            "refusal is not hidden",
            "CLOSURE_HIDES_REFUSAL",
        ),
        _collapse_check(
            "hidden_divergence_false",
            sources,
            ("divergence_hidden", "mismatch_hidden", "v3_conformance_hides_divergence", "closure_hides_divergence"),
            "divergence and mismatch are not hidden",
            "CLOSURE_HIDES_DIVERGENCE",
        ),
        _collapse_check(
            "mutation_replay_merge_false",
            sources,
            ("mutation_performed", "replay_performed", "merge_performed"),
            "mutation/replay/merge are false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    non_claim_failures = _selected_v3_non_claim_failures(non_claims, sources)
    closure_checks.append(
        _check(
            "required_non_claims_remain_false",
            not non_claim_failures,
            "selected v3 non-claims are explicit and false, and closure non-claims remain false",
            non_claim_failures,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return closure_checks


def _closure_statement(
    outcome: str,
    selected_v3: Mapping[str, Any],
    selected_v8: Mapping[str, Any],
    relation_band: Mapping[str, Any],
    basis: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
    not_closed_reason: str | None,
) -> dict[str, Any]:
    failed_checks = [copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False]
    closed = outcome == CURRENT_BODY_CONFORMANCE_V3_CLOSED
    base = {
        "current_body_conformance_v3_closed": closed,
        "current_body_conformance_v3_not_closed": outcome == CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED,
        "current_body_conformance_v3_closure_blocked": outcome == CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED,
        "selected_v3_conformance_preserved": bool(selected_v3.get("selected_v3_conformance_preserved")),
        "selected_v8_preserved": bool(selected_v8.get("selected_v8_preserved")),
        "selected_relation_band_preserved": bool(relation_band.get("selected_relation_band_preserved")),
        "conformance_meaning_recorded": closed,
        "conformance_non_meaning_recorded": closed,
        "current_governing_basis_remained_upstream": bool(basis.get("current_governing_basis_remained_upstream")),
        "downstream_surfaces_remained_downstream": bool(basis.get("downstream_surfaces_remained_downstream")),
        "closed_multi_carrier_relation_band_remained_downstream": bool(basis.get("closed_multi_carrier_relation_band_remained_downstream")),
        "relation_closure_meaning_preserved": bool(basis.get("relation_closure_meaning_preserved")),
        "relation_closure_non_meaning_preserved": bool(basis.get("relation_closure_non_meaning_preserved")),
        "carrier_b_receiving_evidence_only": bool(basis.get("carrier_b_receiving_evidence_only")),
        "returned_evidence_preserved": bool(basis.get("returned_evidence_preserved")),
        "visible_refusal_preserved": bool(basis.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(basis.get("visible_divergence_preserved")),
        "currentness_participation_remained_participation": bool(basis.get("currentness_participation_remained_participation")),
        "current_carrier_selected": False,
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
        "successor_forced": False,
        "selected_v3_basis_where_available": copy.deepcopy(dict(basis)),
        "failed_checks": failed_checks,
    }
    if closed:
        base.update(
            {
                "selected_v3_conformance_preserved": True,
                "selected_v8_preserved": True,
                "selected_relation_band_preserved": True,
                "conformance_meaning_recorded": True,
                "conformance_non_meaning_recorded": True,
                "current_governing_basis_remained_upstream": True,
                "downstream_surfaces_remained_downstream": True,
                "closed_multi_carrier_relation_band_remained_downstream": True,
                "relation_closure_meaning_preserved": True,
                "relation_closure_non_meaning_preserved": True,
                "carrier_b_receiving_evidence_only": True,
                "returned_evidence_preserved": True,
                "visible_refusal_preserved": True,
                "visible_divergence_preserved": True,
                "currentness_participation_remained_participation": True,
            }
        )
    elif outcome == CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED:
        base.update(
            {
                "not_closed_reason": not_closed_reason or BLOCK_REASONS["CLOSURE_NOT_REQUESTED"],
                "selected_body_conformant_basis_preserved": True,
                "non_collapse_posture_preserved": True,
            }
        )
    else:
        base.update(
            {
                "block_code": block_code,
                "block_reason": block_reason,
                "selected_basis_where_available": copy.deepcopy(dict(basis)),
                "non_claims_where_available": copy.deepcopy(basis.get("selected_v3_non_claims")),
            }
        )
    return base


def _declared_closure_question(
    selected_v3: Mapping[str, Any],
    selected_v8: Mapping[str, Any],
    relation_band: Mapping[str, Any],
) -> dict[str, Any]:
    basis_id = (
        selected_v3.get("selected_v3_conformance_result_id")
        or selected_v8.get("selected_v8_id")
        or "selected_v3_conformance"
    )
    return {
        "closure_question_id": f"{_safe_filename_part(basis_id)}__current_body_conformance_v3_closure",
        "closure_question": "What does this selected current-body conformance v3 BODY_CONFORMANT result mean and not mean?",
        "selected_v3_conformance_result_id": selected_v3.get("selected_v3_conformance_result_id"),
        "selected_v3_conformance_result_path": selected_v3.get("selected_v3_conformance_result_path"),
        "selected_v3_conformance_outcome": selected_v3.get("selected_v3_conformance_outcome"),
        "selected_v8_id": selected_v8.get("selected_v8_id"),
        "selected_v8_path": selected_v8.get("selected_v8_path"),
        "selected_v8_outcome": selected_v8.get("selected_v8_outcome"),
        "selected_multi_carrier_relation_id": relation_band.get("selected_multi_carrier_relation_id"),
        "selected_multi_carrier_relation_conformance_id": relation_band.get("selected_multi_carrier_relation_conformance_id"),
        "selected_multi_carrier_relation_conformance_closure_id": relation_band.get("selected_multi_carrier_relation_conformance_closure_id"),
        "closure_is_over_one_selected_body_conformant_v3_result": True,
        "closure_performs_conformance": False,
        "closure_creates_self_orientation": False,
        "closure_creates_currentness": False,
        "closure_creates_distributed_standing": False,
        "closure_authorizes_continuation": False,
        "closure_authorizes_additional_carrier_experiment": False,
        "closure_authorizes_distributed_operation": False,
        "closure_authorizes_follow_on_work": False,
        "closure_forces_successor": False,
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


def _selected_v3_non_claim_failures(
    selected_non_claims: Mapping[str, Any],
    sources: Sequence[Any],
) -> dict[str, Any]:
    failures: dict[str, Any] = {}
    if not selected_non_claims:
        failures["selected_v3_non_claims"] = "missing"
    else:
        for key in sorted(SELECTED_V3_REQUIRED_NON_CLAIMS):
            if key not in selected_non_claims:
                failures[key] = "missing"
            elif selected_non_claims.get(key) is not False:
                failures[key] = selected_non_claims.get(key)
    for key in sorted(set(REQUIRED_NON_CLAIMS) | SELECTED_V3_REQUIRED_NON_CLAIMS):
        if _flag_true(sources, (key,)):
            failures[key] = True
    return failures


def _passed_conformance_check_count(conformance: Mapping[str, Any]) -> int:
    checks = _mapping_list(conformance.get("conformance_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is True)
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    value = summary.get("passed_check_count")
    return int(value) if isinstance(value, int) else 0


def _failed_conformance_check_count(conformance: Mapping[str, Any]) -> int:
    checks = _mapping_list(conformance.get("conformance_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is False)
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    value = summary.get("failed_check_count")
    return int(value) if isinstance(value, int) else 0


def _conformance_checks_visible(conformance: Mapping[str, Any]) -> bool:
    checks = _mapping_list(conformance.get("conformance_checks"))
    if checks:
        return True
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    return isinstance(summary.get("passed_check_count"), int) and isinstance(
        summary.get("failed_check_count"), int
    )


def _v3_quality_score(conformance: Mapping[str, Any]) -> int:
    if conformance.get("outcome") != BODY_CONFORMANT:
        return -1
    summary = _as_mapping(conformance.get("current_body_conformance_pass_v3_summary"))
    statement = _as_mapping(conformance.get("conformance_statement"))
    score_keys = (
        "v8_body_posture_conformant",
        "current_governing_basis_upstream",
        "downstream_surfaces_downstream",
        "closed_multi_carrier_relation_band_downstream",
        "relation_closure_meaning_preserved",
        "relation_closure_non_meaning_preserved",
        "carrier_b_receiving_evidence_only",
        "visible_refusal_preserved",
        "visible_divergence_preserved",
        "currentness_participation_remained_participation",
        "no_additional_carrier_experiment",
        "no_distributed_operation",
        "no_successor_forced",
    )
    score = sum(1 for key in score_keys if summary.get(key) is True)
    score += sum(1 for value in statement.values() if value is True)
    if _failed_conformance_check_count(conformance) == 0:
        score += 5
    return score


def _not_closed_reason(conformance: Mapping[str, Any]) -> str | None:
    values = dict(_walk_key_values(conformance))
    for key in (
        "closure_requested",
        "closure_should_be_recorded",
        "record_closure",
        "close_current_body_conformance_v3",
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
    return BLOCK_REASONS.get(block_code, f"Current-body conformance v3 closure blocked: {block_code}.")


def _result_id(selected_v3: Mapping[str, Any], outcome: str) -> str:
    basis_id = (
        selected_v3.get("selected_v3_conformance_result_id")
        or selected_v3.get("selected_v8_id")
        or "selected_v3_conformance"
    )
    return f"{_safe_filename_part(basis_id)}__{outcome.lower()}__current_body_conformance_v3_closure_result"


def _currentness_shortcut_code(sources: Sequence[Any]) -> str:
    if _flag_true(
        sources,
        (
            "currentness_created",
            "current_body_conformance_v3_closure_created_currentness",
            "v3_conformance_created_currentness",
            "closure_created_currentness",
        ),
    ):
        return "CLOSURE_CREATES_CURRENTNESS"
    return "CLOSURE_CURRENTNESS_SHORTCUT"


def _successor_pressure_code(sources: Sequence[Any]) -> str:
    if _flag_true(sources, ("closure_forced_self_orientation_successor", "self_orientation_successor_forced")):
        return "CLOSURE_FORCES_SELF_ORIENTATION_SUCCESSOR"
    if _flag_true(sources, ("closure_forced_conformance_successor", "conformance_successor_forced")):
        return "CLOSURE_FORCES_CONFORMANCE_SUCCESSOR"
    return "CLOSURE_CREATES_SUCCESSOR"


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list) and all(isinstance(item, Mapping) for item in value):
        return [copy.deepcopy(dict(item)) for item in value]
    return []


def _nested(mapping: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = mapping
    for key in keys:
        if not isinstance(value, Mapping):
            return default
        value = value.get(key)
    return default if value is None else value


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = Path(path)
    try:
        return str(resolved.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _truth_from_sources(*sources: Mapping[str, Any], keys: Sequence[str]) -> bool:
    for source in sources:
        for key in keys:
            if source.get(key) is True:
                return True
    return False


def _bool_from_sources(
    *sources: Mapping[str, Any],
    key: str,
    default: bool = False,
) -> bool:
    for source in sources:
        if key in source:
            return bool(source.get(key))
    return default


def _not_truth(value: Any) -> bool:
    return value is False


def _visible_posture_available(sources: Sequence[Any], posture: str) -> bool:
    token = posture.lower()
    for key, value in _walk_key_values(sources):
        key_token = key.lower()
        if token not in key_token:
            continue
        if key_token.endswith("_preserved") or key_token.endswith("_visible") or "remains_visible" in key_token:
            if value is True:
                return True
    return False


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
    found: list[tuple[str, Any]] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            if key_text.endswith("non_meaning") or key_text == "what_remains_open":
                continue
            found.append((key_text, item))
            found.extend(_walk_key_values(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_walk_key_values(item))
    return found


def _without_non_meaning_sections(value: Mapping[str, Any]) -> dict[str, Any]:
    skipped = {"conformance_non_meaning", "closure_non_meaning", "what_remains_open"}
    return {key: copy.deepcopy(item) for key, item in value.items() if key not in skipped}


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {
            "true",
            "yes",
            "1",
            "on",
            "created",
            "authorized",
            "selected",
            "forced",
        }
    return bool(value)


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    token = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    while "__" in token:
        token = token.replace("__", "_")
    return token or None


def _safe_filename_part(value: Any) -> str:
    text = str(value or "selected_v3_conformance").strip().lower()
    safe = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in text).strip("_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe[:180] or "selected_v3_conformance"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise CurrentBodyConformanceV3ClosureError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not create a non-overwriting current-body conformance v3 closure result path.",
    )


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "current_body_conformance_v3_closure_created_hierarchy",
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
