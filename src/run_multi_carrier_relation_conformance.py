"""Bounded multi-carrier relation conformance runner.

This runner tests one selected recognized multi-carrier relation for bounded
coherence. It does not create relation, currentness, authority, permission,
carrier hierarchy, distributed standing, synchronization, truth, action,
consequence, continuation, closure, or permission for another carrier.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class MultiCarrierRelationConformanceError(Exception):
    """Hard failure for malformed or unreadable explicit conformance inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


MULTI_CARRIER_RELATION_CONFORMANCE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_conformance"
)
MULTI_CARRIER_RELATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary"
)

RESOLVER_MODULE = "run_multi_carrier_relation_conformance"
RESULT_VERSION = "0.1.0"

MULTI_CARRIER_RELATION_CONFORMANT = "MULTI_CARRIER_RELATION_CONFORMANT"
MULTI_CARRIER_RELATION_NONCONFORMANT = "MULTI_CARRIER_RELATION_NONCONFORMANT"
MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED = (
    "MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED"
)
MULTI_CARRIER_RELATION_RECOGNIZED = "MULTI_CARRIER_RELATION_RECOGNIZED"

SUPPORTED_RELATION_TYPES = {
    "SOURCE_RECEIVER_RELATION",
    "RECEIPT_RETURN_RELATION",
    "ADMITTED_EVIDENCE_RELATION",
    "REFUSAL_SUCCESS_RELATION",
    "DIVERGENCE_BOUNDED_RELATION",
    "CURRENTNESS_PARTICIPATION_RELATION",
    "ROLE_EMISSION_RELATION",
    "CARRIER_EVIDENCE_SET_RELATION",
    "NO_MULTI_CARRIER_RELATION",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "relation_conformance_created_source": False,
    "relation_conformance_created_currentness": False,
    "relation_conformance_created_authority": False,
    "relation_conformance_created_permission": False,
    "relation_conformance_created_successor": False,
    "relation_conformance_created_body": False,
    "relation_conformance_created_hierarchy": False,
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
}

RELATION_BOUNDARY_NON_CLAIM_KEYS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "carrier_relation_created_source",
    "carrier_relation_created_currentness",
    "carrier_relation_created_authority",
    "carrier_relation_created_permission",
    "carrier_relation_created_successor",
    "carrier_relation_created_body",
    "carrier_relation_created_hierarchy",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
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
}

BLOCK_REASONS = {
    "SELECTED_RELATION_MISSING": "Selected multi-carrier relation result is missing.",
    "SELECTED_RELATION_MALFORMED": "Selected relation result is not a JSON object or mapping.",
    "SELECTED_RELATION_NOT_RECOGNIZED": "Selected relation outcome is not MULTI_CARRIER_RELATION_RECOGNIZED.",
    "RELATION_TYPE_UNSUPPORTED": "Selected relation type is unsupported.",
    "SELECTED_CARRIERS_MISSING": "Selected carriers are missing from the relation result.",
    "SELECTED_EVIDENCE_MISSING": "Selected carrier evidence is missing from the relation result.",
    "EVIDENCE_IDENTITY_MISSING": "Selected evidence identity is missing.",
    "EVIDENCE_OUTCOME_MISSING": "Selected evidence outcome is missing.",
    "RELATION_CHECKS_FAILED_OR_HIDDEN": "Selected relation checks failed, are missing, or are hidden.",
    "CONFORMANCE_HIDES_REFUSAL": "Relation conformance hides visible refusal.",
    "CONFORMANCE_HIDES_DIVERGENCE": "Relation conformance hides visible divergence.",
    "CONFORMANCE_CURRENTNESS_SHORTCUT": "Relation conformance attempts a currentness shortcut.",
    "CONFORMANCE_CREATES_CARRIER_HIERARCHY": "Relation conformance creates carrier hierarchy.",
    "CONFORMANCE_SELECTS_WINNING_CARRIER": "Relation conformance selects a winning carrier.",
    "CONFORMANCE_INVALIDATES_LOSING_CARRIER": "Relation conformance invalidates a losing carrier.",
    "CONFORMANCE_REPLACES_SOURCE": "Relation conformance replaces source.",
    "CONFORMANCE_CREATES_CURRENTNESS": "Relation conformance creates currentness.",
    "CONFORMANCE_CREATES_AUTHORITY": "Relation conformance creates authority.",
    "CONFORMANCE_CREATES_PERMISSION": "Relation conformance creates permission.",
    "CONFORMANCE_CREATES_SUCCESSOR": "Relation conformance creates successor standing.",
    "CONFORMANCE_CREATES_BODY": "Relation conformance creates body formation.",
    "CONFORMANCE_CREATES_SIGNAL_BY_DEFAULT": "Relation conformance creates signal by default.",
    "CONFORMANCE_ESTABLISHES_PRESENCE": "Relation conformance establishes presence.",
    "CONFORMANCE_ESTABLISHES_THRESHOLD": "Relation conformance establishes threshold.",
    "CONFORMANCE_CREATES_TRUTH": "Relation conformance creates truth.",
    "CONFORMANCE_AUTHORIZES_ACTION": "Relation conformance authorizes action.",
    "CONFORMANCE_CREATES_CONSEQUENCE": "Relation conformance creates consequence.",
    "CONFORMANCE_CREATES_DISTRIBUTED_STANDING": "Relation conformance creates distributed standing.",
    "CONFORMANCE_AUTHORIZES_CONTINUATION": "Relation conformance authorizes continuation.",
    "CONFORMANCE_RESOLVES_DIVERGENCE_BY_MAJORITY": "Relation conformance resolves divergence by majority.",
    "CONFORMANCE_RESOLVES_DIVERGENCE_BY_LATEST_FILE": "Relation conformance resolves divergence by latest file.",
    "CONFORMANCE_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT": "Relation conformance resolves divergence by success count.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required relation conformance non-claim is missing or flipped.",
    "RELATION_CONFORMANCE_REQUIREMENT_FAILED": "Selected relation is readable but does not satisfy a bounded conformance requirement.",
}

BLOCKING_CODES = set(BLOCK_REASONS) - {"RELATION_CONFORMANCE_REQUIREMENT_FAILED"}

CONFORMANCE_NON_MEANING = {
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
}

OPEN_SURFACES = [
    "multi-carrier relation conformance implementation refinement",
    "multi-carrier relation closure",
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
]


def run_multi_carrier_relation_conformance(
    selected_relation_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run bounded conformance over one selected recognized relation result."""

    if selected_relation_result is None:
        discovered, path, failures = _discover_selected_relation_result()
        return _run_conformance(discovered, path, failures)
    if not isinstance(selected_relation_result, Mapping):
        return _run_conformance({}, None, ["SELECTED_RELATION_MALFORMED"])
    return _run_conformance(copy.deepcopy(dict(selected_relation_result)), None, [])


def run_multi_carrier_relation_conformance_from_path(
    selected_relation_result_path: Path | str,
) -> dict[str, Any]:
    """Run bounded relation conformance from one JSON object path."""

    try:
        path = Path(selected_relation_result_path)
        selected = _read_json_mapping(path)
        return _run_conformance(selected, path, [])
    except MultiCarrierRelationConformanceError as exc:
        return _run_conformance({}, Path(selected_relation_result_path), [exc.block_code])


def write_multi_carrier_relation_conformance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded conformance result artifact without overwriting."""

    if output_path is None:
        selected = _as_mapping(result.get("selected_relation"))
        basis_id = (
            selected.get("selected_relation_result_id")
            or selected.get("selected_relation_type")
            or "multi_carrier_relation"
        )
        output_path = MULTI_CARRIER_RELATION_CONFORMANCE_ROOT / (
            f"{_safe_filename_part(basis_id)}__multi_carrier_relation_conformance_result.json"
        )
    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return target


def build_multi_carrier_relation_conformance_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a relation conformance result."""

    checks = _mapping_list(result.get("relation_conformance_checks"))
    selected = _as_mapping(result.get("selected_relation"))
    basis = _as_mapping(result.get("selected_relation_basis"))
    statement = _as_mapping(result.get("relation_conformance_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "selected_relation_id": selected.get("selected_relation_result_id"),
        "selected_relation_path": selected.get("selected_relation_result_path"),
        "selected_relation_outcome": selected.get("selected_relation_outcome"),
        "selected_relation_type": selected.get("selected_relation_type"),
        "selected_relation_question": selected.get("selected_relation_question"),
        "selected_carrier_count": basis.get("selected_carrier_count"),
        "selected_evidence_count": basis.get("selected_evidence_count"),
        "selected_carrier_ids": copy.deepcopy(basis.get("selected_carrier_ids")),
        "selected_evidence_ids": copy.deepcopy(basis.get("selected_evidence_ids")),
        "selected_evidence_outcomes": copy.deepcopy(basis.get("selected_evidence_outcomes")),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "relation_conformant": bool(statement.get("relation_conformant")),
        "selected_relation_preserved": bool(statement.get("selected_relation_preserved")),
        "selected_carriers_preserved": bool(statement.get("selected_carriers_preserved")),
        "selected_evidence_preserved": bool(statement.get("selected_evidence_preserved")),
        "carrier_roles_preserved": bool(statement.get("carrier_roles_preserved")),
        "local_outcomes_preserved": bool(statement.get("local_outcomes_preserved")),
        "visible_refusal_preserved": bool(statement.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(statement.get("visible_divergence_preserved")),
        "downstream_evidence_posture_preserved": bool(statement.get("downstream_evidence_posture_preserved")),
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
        "presence_threshold_truth_action_consequence_created": bool(statement.get("presence_threshold_truth_action_consequence_created")),
        "continuation_authorized": bool(statement.get("continuation_authorized")),
        "additional_carrier_experiment_authorized": bool(statement.get("additional_carrier_experiment_authorized")),
        "distributed_operation_authorized": bool(statement.get("distributed_operation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def _run_conformance(
    selected_relation: Mapping[str, Any],
    selected_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    selected_relation = _as_mapping(selected_relation)
    selected = _normalize_selected_relation(selected_relation, selected_path)
    carriers = _mapping_list(selected_relation.get("selected_carriers"))
    evidence = _mapping_list(selected_relation.get("selected_carrier_evidence"))
    basis = _selected_relation_basis(selected_relation, selected, carriers, evidence)
    checks = _build_checks(selected_relation, selected, carriers, evidence, basis, precheck_failures)
    failed_checks = [check for check in checks if check.get("passed") is False]
    blocking_failed = [check for check in failed_checks if check.get("block_code") in BLOCKING_CODES]

    if blocking_failed:
        outcome = MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED
        block_code = str(blocking_failed[0].get("block_code"))
    elif failed_checks:
        outcome = MULTI_CARRIER_RELATION_NONCONFORMANT
        block_code = None
    else:
        outcome = MULTI_CARRIER_RELATION_CONFORMANT
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "multi_carrier_relation_conformance_metadata": {
            "multi_carrier_relation_conformance_result_id": _result_id(selected, outcome),
            "multi_carrier_relation_conformance_result_type": "multi_carrier_relation_conformance_result",
            "multi_carrier_relation_conformance_result_version": RESULT_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_conformance_question": _declared_conformance_question(selected),
        "selected_relation": selected,
        "selected_relation_basis": basis,
        "selected_carriers": copy.deepcopy(carriers),
        "selected_carrier_evidence": copy.deepcopy(evidence),
        "relation_conformance_checks": checks,
        "relation_conformance_statement": _relation_conformance_statement(
            outcome,
            selected,
            basis,
            checks,
            block_code,
            block_reason,
        ),
        "relation_conformance_non_meaning": copy.deepcopy(CONFORMANCE_NON_MEANING),
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
    result["multi_carrier_relation_conformance_summary"] = (
        build_multi_carrier_relation_conformance_summary(result)
    )
    return result


def _discover_selected_relation_result() -> tuple[dict[str, Any], Path | None, list[str]]:
    if not MULTI_CARRIER_RELATION_BOUNDARY_ROOT.exists():
        return {}, None, ["SELECTED_RELATION_MISSING"]

    candidates: list[tuple[int, str, Path, dict[str, Any]]] = []
    for path in sorted(MULTI_CARRIER_RELATION_BOUNDARY_ROOT.glob("*.json")):
        try:
            loaded = _read_json_mapping(path)
        except MultiCarrierRelationConformanceError:
            continue
        if loaded.get("outcome") != MULTI_CARRIER_RELATION_RECOGNIZED:
            continue
        failed_count = _failed_relation_check_count(loaded)
        if failed_count != 0:
            continue
        selected = _normalize_selected_relation(loaded, path)
        preference = 0
        request_id = str(selected.get("relation_request_id") or selected.get("selected_relation_result_id") or "")
        relation_type = str(selected.get("selected_relation_type") or "")
        question = str(selected.get("selected_relation_question") or "")
        if "carrier_b_refusal_success" in request_id.lower() or (
            relation_type == "REFUSAL_SUCCESS_RELATION"
            and "carrier b" in question.lower()
        ):
            preference = -10
        candidates.append((preference, path.name, path, loaded))

    if not candidates:
        return {}, None, ["SELECTED_RELATION_MISSING"]
    _preference, _name, path, selected = sorted(candidates, key=lambda item: (item[0], item[1]))[0]
    return copy.deepcopy(selected), path, []


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    try:
        loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise MultiCarrierRelationConformanceError(
            "SELECTED_RELATION_MISSING",
            BLOCK_REASONS["SELECTED_RELATION_MISSING"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise MultiCarrierRelationConformanceError(
            "SELECTED_RELATION_MALFORMED",
            BLOCK_REASONS["SELECTED_RELATION_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise MultiCarrierRelationConformanceError(
            "SELECTED_RELATION_MALFORMED",
            BLOCK_REASONS["SELECTED_RELATION_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _normalize_selected_relation(
    relation: Mapping[str, Any],
    selected_path: Path | None,
) -> dict[str, Any]:
    metadata = _as_mapping(relation.get("multi_carrier_relation_metadata"))
    question = _as_mapping(relation.get("declared_relation_question"))
    relation_result = _as_mapping(relation.get("relation_result"))
    summary = _as_mapping(relation.get("multi_carrier_relation_summary"))
    basis = _as_mapping(relation.get("relation_basis"))
    result_id = (
        metadata.get("multi_carrier_relation_result_id")
        or summary.get("selected_relation_id")
        or summary.get("relation_request_id")
        or question.get("relation_request_id")
    )
    relation_type = (
        question.get("relation_type")
        or relation_result.get("relation_type")
        or basis.get("relation_type")
        or summary.get("relation_type")
    )
    relation_question = question.get("relation_question") or basis.get("relation_question") or summary.get("relation_question")
    return {
        "selected_relation_result_id": result_id,
        "selected_relation_result_path": str(selected_path) if selected_path else relation.get("_selected_relation_result_path"),
        "selected_relation_result_type": metadata.get("multi_carrier_relation_result_type"),
        "selected_relation_result_version": metadata.get("multi_carrier_relation_result_version"),
        "selected_relation_outcome": relation.get("outcome"),
        "selected_relation_type": _normalize_token(relation_type) or relation_type,
        "selected_relation_question": relation_question,
        "relation_request_id": question.get("relation_request_id") or summary.get("relation_request_id"),
        "selected_relation_preserved": bool(relation),
        "relation_created_by_conformance": False,
        "relation_scope_widened_by_conformance": False,
    }


def _selected_relation_basis(
    relation: Mapping[str, Any],
    selected: Mapping[str, Any],
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    relation_result = _as_mapping(relation.get("relation_result"))
    relation_basis = _as_mapping(relation.get("relation_basis"))
    summary = _as_mapping(relation.get("multi_carrier_relation_summary"))
    non_claims = _as_mapping(relation.get("non_claims"))
    checks = _mapping_list(relation.get("relation_checks"))
    carrier_ids = _unique_values(
        summary.get("selected_carrier_ids")
        or relation_result.get("selected_carrier_ids")
        or relation_basis.get("selected_carrier_ids")
        or _selected_carrier_ids(carriers, evidence)
    )
    evidence_ids = _unique_values(
        summary.get("selected_evidence_ids")
        or relation_result.get("selected_evidence_ids")
        or relation_basis.get("selected_evidence_ids")
        or [item.get("evidence_id") for item in evidence]
    )
    evidence_outcomes = _unique_values(
        summary.get("selected_evidence_outcomes")
        or relation_result.get("selected_evidence_outcomes")
        or relation_basis.get("selected_evidence_outcomes")
        or [item.get("evidence_outcome") for item in evidence]
    )
    relation_evidence = (
        relation_result.get("relation_evidence")
        or _as_mapping(relation_basis.get("relation_detection")).get("relation_evidence")
    )
    return {
        "selected_relation_result_id": selected.get("selected_relation_result_id"),
        "selected_relation_result_path": selected.get("selected_relation_result_path"),
        "selected_relation_outcome": selected.get("selected_relation_outcome"),
        "selected_relation_type": selected.get("selected_relation_type"),
        "selected_relation_question": selected.get("selected_relation_question"),
        "selected_carrier_count": _first_present(
            summary.get("selected_carrier_count"),
            relation_result.get("selected_carrier_count"),
            relation_basis.get("selected_carrier_count"),
            len(carriers),
        ),
        "selected_evidence_count": _first_present(
            summary.get("selected_evidence_count"),
            relation_result.get("selected_evidence_count"),
            relation_basis.get("selected_evidence_count"),
            len(evidence),
        ),
        "selected_carrier_ids": carrier_ids,
        "selected_evidence_ids": evidence_ids,
        "selected_evidence_outcomes": evidence_outcomes,
        "relation_evidence": copy.deepcopy(relation_evidence),
        "selected_relation_basis": copy.deepcopy(relation_basis),
        "relation_checks_preserved": copy.deepcopy(checks),
        "passed_relation_check_count": _passed_relation_check_count(relation),
        "failed_relation_check_count": _failed_relation_check_count(relation),
        "visible_refusal_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="visible_refusal_preserved",
        ),
        "visible_divergence_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="visible_divergence_preserved",
        ),
        "downstream_evidence_posture_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="downstream_evidence_posture_preserved",
        ),
        "current_carrier_not_selected": _bool_from_sources(
            relation_result,
            summary,
            key="current_carrier_not_selected",
            default=True,
        ),
        "winning_carrier_selected": bool(
            relation_result.get("winning_carrier_selected")
            or summary.get("winning_carrier_selected")
            or non_claims.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            relation_result.get("losing_carrier_invalidated")
            or summary.get("losing_carrier_invalidated")
            or non_claims.get("losing_carrier_invalidated")
        ),
        "carrier_roles_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="carrier_roles_preserved",
            default=True,
        ),
        "evidence_identities_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="evidence_identities_preserved",
            default=True,
        ),
        "local_outcomes_preserved": _bool_from_sources(
            relation_result,
            summary,
            key="local_outcomes_preserved",
            default=True,
        ),
        "currentness_participation_remained_participation": _currentness_participation_remained_participation(evidence),
        "selected_relation_non_claims": copy.deepcopy(non_claims),
        "required_conformance_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }


def _build_checks(
    relation: Mapping[str, Any],
    selected: Mapping[str, Any],
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
    basis: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    sources = [relation, selected, carriers, evidence, basis, _as_mapping(relation.get("non_claims"))]
    relation_checks = _mapping_list(relation.get("relation_checks"))
    relation_type = selected.get("selected_relation_type")
    relation_outcome = selected.get("selected_relation_outcome")
    evidence_ids = [item.get("evidence_id") for item in evidence]
    evidence_outcomes = [item.get("evidence_outcome") or item.get("outcome") or item.get("status") for item in evidence]
    relation_check_failures = [check for check in relation_checks if check.get("passed") is False]
    relation_checks_hidden = not relation_checks or bool(relation_check_failures)
    visible_refusal_available = _visible_refusal_available(evidence, basis)
    visible_divergence_available = _visible_divergence_available(evidence, basis)

    checks = [
        _check("selected_relation_result_exists", bool(relation) and "SELECTED_RELATION_MISSING" not in precheck_failures, "selected relation result exists", list(precheck_failures), precheck_failures[0] if precheck_failures else "SELECTED_RELATION_MISSING"),
        _check("selected_relation_result_parseable_mapping", not precheck_failures, "selected relation result is a parseable mapping", list(precheck_failures), precheck_failures[0] if precheck_failures else "SELECTED_RELATION_MALFORMED"),
        _check("selected_relation_result_outcome_recognized", relation_outcome == MULTI_CARRIER_RELATION_RECOGNIZED, "selected relation outcome is MULTI_CARRIER_RELATION_RECOGNIZED", relation_outcome, "SELECTED_RELATION_NOT_RECOGNIZED"),
        _check("selected_relation_type_supported", relation_type in SUPPORTED_RELATION_TYPES, "selected relation type is supported", relation_type, "RELATION_TYPE_UNSUPPORTED"),
        _check("selected_relation_question_declared", bool(str(selected.get("selected_relation_question") or "").strip()), "selected relation question is declared", selected.get("selected_relation_question"), "RELATION_CONFORMANCE_REQUIREMENT_FAILED"),
        _check("selected_carriers_preserved", bool(carriers), "selected carriers are preserved", {"selected_carrier_count": len(carriers)}, "SELECTED_CARRIERS_MISSING"),
        _check("selected_carrier_evidence_preserved", bool(evidence), "selected carrier evidence is preserved", {"selected_evidence_count": len(evidence)}, "SELECTED_EVIDENCE_MISSING"),
        _check("selected_evidence_identities_preserved", bool(evidence) and all(_first_text(item, ("evidence_id", "id", "selected_evidence_id")) for item in evidence), "selected evidence identities are preserved", evidence_ids, "EVIDENCE_IDENTITY_MISSING"),
        _check("selected_evidence_outcomes_preserved", bool(evidence) and all(value is not None and str(value).strip() for value in evidence_outcomes), "selected evidence outcomes are preserved", evidence_outcomes, "EVIDENCE_OUTCOME_MISSING"),
        _check("carrier_roles_preserved", bool(basis.get("carrier_roles_preserved")), "carrier roles remain bounded and operation-local", basis.get("carrier_roles_preserved"), "RELATION_CONFORMANCE_REQUIREMENT_FAILED"),
        _check("local_outcomes_preserved", bool(basis.get("local_outcomes_preserved")), "local outcomes remain local", basis.get("local_outcomes_preserved"), "RELATION_CONFORMANCE_REQUIREMENT_FAILED"),
        _check("relation_basis_preserved", bool(basis.get("selected_relation_basis")), "selected relation basis is preserved", _shape(basis.get("selected_relation_basis")), "RELATION_CONFORMANCE_REQUIREMENT_FAILED"),
        _check("relation_checks_passed_or_preserved", not relation_checks_hidden, "selected relation checks passed and are visible", {"failed_relation_check_count": len(relation_check_failures), "relation_check_count": len(relation_checks)}, "RELATION_CHECKS_FAILED_OR_HIDDEN"),
        _check("downstream_evidence_posture_preserved", bool(basis.get("downstream_evidence_posture_preserved")), "downstream evidence posture is preserved", basis.get("downstream_evidence_posture_preserved"), "RELATION_CONFORMANCE_REQUIREMENT_FAILED"),
        _check("visible_refusal_preserved_where_applicable", not visible_refusal_available or bool(basis.get("visible_refusal_preserved")), "visible refusal remains visible where available", {"visible_refusal_available": visible_refusal_available, "visible_refusal_preserved": basis.get("visible_refusal_preserved")}, "CONFORMANCE_HIDES_REFUSAL"),
        _check("visible_divergence_preserved_where_applicable", not visible_divergence_available or bool(basis.get("visible_divergence_preserved")), "visible divergence remains visible where available", {"visible_divergence_available": visible_divergence_available, "visible_divergence_preserved": basis.get("visible_divergence_preserved")}, "CONFORMANCE_HIDES_DIVERGENCE"),
        _check("currentness_participation_remained_participation", bool(basis.get("currentness_participation_remained_participation")), "currentness participation remains participation only where applicable", basis.get("currentness_participation_remained_participation"), "CONFORMANCE_CURRENTNESS_SHORTCUT"),
        _check("current_carrier_not_selected", _current_carrier_not_selected(sources, basis), "current carrier is not selected", _flag_snapshot(sources, ("current_carrier_selected", "current_carrier_not_selected")), "CONFORMANCE_CURRENTNESS_SHORTCUT"),
        _check("winning_carrier_not_selected", not _flag_true(sources, ("winning_carrier_selected", "relation_selects_winning_carrier")), "winning carrier is not selected", _flag_snapshot(sources, ("winning_carrier_selected", "relation_selects_winning_carrier")), "CONFORMANCE_SELECTS_WINNING_CARRIER"),
        _check("losing_carrier_not_invalidated", not _flag_true(sources, ("losing_carrier_invalidated", "relation_invalidates_losing_carrier")), "losing carrier is not invalidated", _flag_snapshot(sources, ("losing_carrier_invalidated", "relation_invalidates_losing_carrier")), "CONFORMANCE_INVALIDATES_LOSING_CARRIER"),
        _collapse_check("carrier_hierarchy_not_created", sources, ("carrier_hierarchy_created", "carrier_relation_created_hierarchy", "relation_conformance_created_hierarchy"), "carrier hierarchy is not created", "CONFORMANCE_CREATES_CARRIER_HIERARCHY"),
        _collapse_check("source_not_replaced", sources, ("source_replaced", "carrier_relation_created_source", "relation_conformance_created_source", "evidence_merged_into_source"), "source is not replaced", "CONFORMANCE_REPLACES_SOURCE"),
        _collapse_check("currentness_not_created", sources, ("currentness_created", "carrier_relation_created_currentness", "relation_conformance_created_currentness", "latest_file_currentness", "currentness_from_relation_conformance"), "currentness is not created", _currentness_shortcut_code(sources)),
        _collapse_check("authority_not_created", sources, ("authority_created", "carrier_relation_created_authority", "relation_conformance_created_authority"), "authority is not created", "CONFORMANCE_CREATES_AUTHORITY"),
        _collapse_check("permission_not_created", sources, ("permission_created", "carrier_relation_created_permission", "relation_conformance_created_permission"), "permission is not created", "CONFORMANCE_CREATES_PERMISSION"),
        _collapse_check("successor_not_created", sources, ("carrier_relation_created_successor", "relation_conformance_created_successor", "successor_created", "successor_standing_created"), "successor is not created", "CONFORMANCE_CREATES_SUCCESSOR"),
        _collapse_check("body_not_created", sources, ("carrier_relation_created_body", "relation_conformance_created_body", "body_created", "body_formed"), "body is not created", "CONFORMANCE_CREATES_BODY"),
        _collapse_check("signal_not_created_by_default", sources, ("signal_created_by_default", "relation_creates_signal_by_default"), "signal is not created by default", "CONFORMANCE_CREATES_SIGNAL_BY_DEFAULT"),
        _collapse_check("presence_not_established", sources, ("presence_established", "relation_establishes_presence"), "presence is not established", "CONFORMANCE_ESTABLISHES_PRESENCE"),
        _collapse_check("threshold_not_met", sources, ("threshold_met", "relation_establishes_threshold"), "threshold is not met", "CONFORMANCE_ESTABLISHES_THRESHOLD"),
        _collapse_check("truth_not_created", sources, ("truth_created", "relation_creates_truth"), "truth is not created", "CONFORMANCE_CREATES_TRUTH"),
        _collapse_check("action_not_authorized", sources, ("action_authorized", "relation_authorizes_action"), "action is not authorized", "CONFORMANCE_AUTHORIZES_ACTION"),
        _collapse_check("consequence_not_created", sources, ("consequence_created", "relation_creates_consequence"), "consequence is not created", "CONFORMANCE_CREATES_CONSEQUENCE"),
        _collapse_check("distributed_standing_not_created", sources, ("distributed_standing_created", "relation_creates_distributed_standing"), "distributed standing is not created", "CONFORMANCE_CREATES_DISTRIBUTED_STANDING"),
        _collapse_check("continuation_not_authorized", sources, ("continuation_authorized", "relation_authorizes_continuation"), "continuation is not authorized", "CONFORMANCE_AUTHORIZES_CONTINUATION"),
        _collapse_check("divergence_not_resolved_by_majority_latest_success_count", sources, ("divergence_resolved_by_majority", "divergence_resolved_by_latest_file", "divergence_resolved_by_success_count"), "divergence is not resolved by majority/latest/success count", _divergence_resolution_code(sources)),
        _collapse_check("latest_file_currentness_false", sources, ("latest_file_currentness", "latest_file_recency_currentness"), "latest-file currentness is false", "CONFORMANCE_CURRENTNESS_SHORTCUT"),
        _collapse_check("recency_fraud_false", sources, ("recency_fraud", "recency_currentness"), "recency fraud is false", "CONFORMANCE_CURRENTNESS_SHORTCUT"),
        _collapse_check("mutation_replay_merge_false", sources, ("mutation_performed", "replay_performed", "merge_performed", "evidence_overwritten"), "mutation/replay/merge are false", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("additional_carrier_experiment_not_authorized", sources, ("additional_carrier_experiment_authorized", "another_physical_carrier_experiment_authorized"), "additional carrier experiment is not authorized", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _collapse_check("distributed_operation_not_authorized", sources, ("distributed_operation_authorized", "distributed_operation_permission"), "distributed operation is not authorized", "NON_CLAIM_MISSING_OR_FLIPPED"),
    ]
    non_claim_failures = _selected_relation_non_claim_failures(_as_mapping(relation.get("non_claims")), sources)
    checks.append(
        _check(
            "required_non_claims_remain_false",
            not non_claim_failures,
            "selected relation non-claims are explicit and false, and conformance non-claims remain false",
            non_claim_failures,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _relation_conformance_statement(
    outcome: str,
    selected: Mapping[str, Any],
    basis: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    failed_checks = [copy.deepcopy(dict(check)) for check in checks if check.get("passed") is False]
    conformant = outcome == MULTI_CARRIER_RELATION_CONFORMANT
    base = {
        "relation_conformant": conformant,
        "relation_nonconformant": outcome == MULTI_CARRIER_RELATION_NONCONFORMANT,
        "relation_conformance_blocked": outcome == MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED,
        "selected_relation_preserved": bool(selected.get("selected_relation_preserved")),
        "selected_carriers_preserved": bool(basis.get("selected_carrier_count")),
        "selected_evidence_preserved": bool(basis.get("selected_evidence_count")),
        "carrier_roles_preserved": bool(basis.get("carrier_roles_preserved")),
        "local_outcomes_preserved": bool(basis.get("local_outcomes_preserved")),
        "visible_refusal_preserved": bool(basis.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(basis.get("visible_divergence_preserved")),
        "downstream_evidence_posture_preserved": bool(basis.get("downstream_evidence_posture_preserved")),
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
        "presence_threshold_truth_action_consequence_created": False,
        "continuation_authorized": False,
        "additional_carrier_experiment_authorized": False,
        "distributed_operation_authorized": False,
        "selected_relation_basis_where_available": copy.deepcopy(dict(basis)),
        "failed_checks": failed_checks,
    }
    if conformant:
        base.update({
            "selected_relation_preserved": True,
            "selected_carriers_preserved": True,
            "selected_evidence_preserved": True,
            "carrier_roles_preserved": True,
            "local_outcomes_preserved": True,
            "downstream_evidence_posture_preserved": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
        })
    elif outcome == MULTI_CARRIER_RELATION_NONCONFORMANT:
        base.update({
            "nonconformance_reason": "selected recognized relation is readable but does not satisfy all bounded conformance checks",
            "non_collapse_posture_preserved": True,
        })
    else:
        base.update({
            "block_code": block_code,
            "block_reason": block_reason,
            "selected_basis_where_available": copy.deepcopy(dict(basis)),
            "non_claims_where_available": copy.deepcopy(basis.get("selected_relation_non_claims")),
        })
    return base


def _declared_conformance_question(selected: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "conformance_question_id": f"{_safe_filename_part(selected.get('selected_relation_result_id') or selected.get('selected_relation_type') or 'selected_relation')}__relation_conformance",
        "conformance_question": "Does this selected recognized multi-carrier relation cohere without collapse?",
        "selected_relation_result_id": selected.get("selected_relation_result_id"),
        "selected_relation_result_path": selected.get("selected_relation_result_path"),
        "selected_relation_outcome": selected.get("selected_relation_outcome"),
        "selected_relation_type": selected.get("selected_relation_type"),
        "selected_relation_question": selected.get("selected_relation_question"),
        "conformance_creates_relation": False,
        "conformance_creates_currentness": False,
        "conformance_creates_distributed_standing": False,
        "conformance_authorizes_continuation": False,
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
    if _flag_true(sources, ("currentness_created", "carrier_relation_created_currentness", "relation_conformance_created_currentness")):
        return "CONFORMANCE_CREATES_CURRENTNESS"
    return "CONFORMANCE_CURRENTNESS_SHORTCUT"


def _divergence_resolution_code(sources: Sequence[Any]) -> str:
    if _flag_true(sources, ("divergence_resolved_by_latest_file",)):
        return "CONFORMANCE_RESOLVES_DIVERGENCE_BY_LATEST_FILE"
    if _flag_true(sources, ("divergence_resolved_by_success_count",)):
        return "CONFORMANCE_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT"
    return "CONFORMANCE_RESOLVES_DIVERGENCE_BY_MAJORITY"


def _current_carrier_not_selected(
    sources: Sequence[Any],
    basis: Mapping[str, Any],
) -> bool:
    if _flag_true(sources, ("current_carrier_selected", "selected_current_carrier")):
        return False
    value = basis.get("current_carrier_not_selected")
    return value is not False


def _currentness_participation_remained_participation(
    evidence: Sequence[Mapping[str, Any]],
) -> bool:
    statuses = [
        _first_text(item, ("currentness_participation_status", "currentness_status", "participation_status"))
        for item in evidence
    ]
    visible = [status for status in statuses if status]
    if not visible:
        return True
    return all("CURRENTNESS_PARTICIPATION" in (_normalize_token(status) or "") for status in visible)


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


def _selected_relation_non_claim_failures(
    relation_non_claims: Mapping[str, Any],
    sources: Sequence[Any],
) -> dict[str, Any]:
    failures: dict[str, Any] = {}
    if not relation_non_claims:
        failures["selected_relation_non_claims"] = "missing"
    else:
        for key in sorted(RELATION_BOUNDARY_NON_CLAIM_KEYS):
            if key in relation_non_claims and relation_non_claims.get(key) is not False:
                failures[key] = relation_non_claims.get(key)
    for key in sorted(REQUIRED_NON_CLAIMS):
        if _flag_true(sources, (key,)):
            failures[key] = True
    return failures


def _passed_relation_check_count(relation: Mapping[str, Any]) -> int:
    checks = _mapping_list(relation.get("relation_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is True)
    summary = _as_mapping(relation.get("multi_carrier_relation_summary"))
    value = summary.get("passed_check_count")
    return int(value) if isinstance(value, int) else 0


def _failed_relation_check_count(relation: Mapping[str, Any]) -> int:
    checks = _mapping_list(relation.get("relation_checks"))
    if checks:
        return sum(1 for check in checks if check.get("passed") is False)
    summary = _as_mapping(relation.get("multi_carrier_relation_summary"))
    value = summary.get("failed_check_count")
    return int(value) if isinstance(value, int) else 0


def _selected_carrier_ids(
    carriers: Sequence[Mapping[str, Any]],
    evidence: Sequence[Mapping[str, Any]],
) -> list[str]:
    values = [item.get("carrier_id") or item.get("selected_carrier_id") for item in carriers]
    for item in evidence:
        values.extend((
            item.get("carrier_id"),
            item.get("selected_carrier_id"),
            item.get("source_carrier_id"),
            item.get("receiving_carrier_id"),
        ))
    return _unique_values(values)


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, f"Relation conformance blocked: {block_code}.")


def _result_id(selected: Mapping[str, Any], outcome: str) -> str:
    basis_id = (
        selected.get("selected_relation_result_id")
        or selected.get("relation_request_id")
        or selected.get("selected_relation_type")
        or "multi_carrier_relation"
    )
    return f"{_safe_filename_part(basis_id)}__{outcome.lower()}__multi_carrier_relation_conformance_result"


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
        return value.strip().lower() in {"true", "yes", "1", "on", "created", "authorized", "selected"}
    return bool(value)


def _safe_filename_part(value: Any) -> str:
    text = str(value or "multi_carrier_relation").strip().lower()
    safe = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in text).strip("_")
    while "__" in safe:
        safe = safe.replace("__", "_")
    return safe or "multi_carrier_relation"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.parent / f"{path.stem}_{index:03d}{path.suffix}"
        if not candidate.exists():
            return candidate
    raise MultiCarrierRelationConformanceError(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not create a non-overwriting relation conformance result path.",
    )


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "relation_conformance_created_hierarchy",
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
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: copy.deepcopy(non_claims.get(key)) for key in keys}
