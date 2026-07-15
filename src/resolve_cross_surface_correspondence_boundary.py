"""Bounded cross-surface correspondence boundary resolver.

This resolver records whether selected standing surfaces may be read together
under bounded correspondence while preserving rank, source, scope, lineage,
local outcome, and non-claims. It does not create authority, permission,
currentness, explanation ownership, signal, presence, threshold, truth, action,
consequence, continuation, merge, equivalence, workflow, routing, or successor
pressure.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class CrossSurfaceCorrespondenceBoundaryError(Exception):
    """Raised for hard malformed or unreadable correspondence inputs."""


REPO_ROOT = Path(__file__).resolve().parents[1]
CROSS_SURFACE_CORRESPONDENCE_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_cross_surface_correspondence_boundary"
)

RESOLVER_MODULE = "resolve_cross_surface_correspondence_boundary"
RESULT_VERSION = "0.1.0"

CORRESPONDENCE_RECOGNIZED = "CORRESPONDENCE_RECOGNIZED"
NO_CORRESPONDENCE = "NO_CORRESPONDENCE"
BLOCKED = "BLOCKED"

PERMITTED_CORRESPONDENCE_TYPES = {
    "BASIS_MATCH",
    "BASIS_MISMATCH",
    "DOWNSTREAM_RECOGNITION",
    "SCOPE_ALIGNMENT",
    "SCOPE_MISMATCH",
    "NON_CLAIM_ALIGNMENT",
    "NON_CLAIM_CONFLICT",
    "LINEAGE_REFERENCE",
    "CLOSURE_ALIGNMENT",
    "REFUSAL_VISIBLE",
    "NO_CORRESPONDENCE",
}

NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "standing_upgraded": False,
    "surface_merged": False,
    "surface_equivalence_created": False,
    "explanation_ownership_created": False,
    "signal_created_by_default": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "workflow_created": False,
    "routing_created": False,
    "medium_created": False,
    "body_relevance_medium_created": False,
    "self_orientation_successor_forced": False,
    "conformance_successor_forced": False,
    "continuation_authorized": False,
    "precursor_upgraded_to_current_law": False,
    "source_derivative_operator_collapsed": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "SELECTED_SURFACE_MISSING": "At least two selected standing surfaces are required.",
    "SELECTED_SURFACE_UNREADABLE": "A selected surface path could not be read.",
    "SELECTED_SURFACE_MALFORMED": "A selected surface is not a JSON object or mapping.",
    "SELECTED_SURFACE_IDENTITY_MISSING": "A selected surface lacks bounded identity.",
    "SELECTED_SURFACE_OUTCOME_MISSING": "A selected surface lacks outcome or status.",
    "SOURCE_BASIS_UNKNOWN": "Source basis is required here and is not exposed.",
    "DOWNSTREAM_BASIS_UNKNOWN": "Source/downstream posture is not bounded.",
    "CORRESPONDENCE_QUESTION_UNDECLARED": "A declared correspondence question is required.",
    "CORRESPONDENCE_TYPE_UNSUPPORTED": "The correspondence type is outside the bounded set.",
    "CORRESPONDENCE_ATTEMPTS_SOURCE_REPLACEMENT": "Correspondence attempts source replacement.",
    "CORRESPONDENCE_ATTEMPTS_AUTHORITY": "Correspondence attempts authority creation or transfer.",
    "CORRESPONDENCE_ATTEMPTS_CURRENTNESS": "Correspondence attempts currentness creation or transfer.",
    "CORRESPONDENCE_ATTEMPTS_PERMISSION": "Correspondence attempts permission creation or transfer.",
    "CORRESPONDENCE_ATTEMPTS_MERGE": "Correspondence attempts merge, equivalence, or explanation ownership.",
    "CORRESPONDENCE_CREATES_SIGNAL_BY_DEFAULT": "Correspondence creates signal by default.",
    "CORRESPONDENCE_ESTABLISHES_PRESENCE": "Correspondence establishes presence.",
    "CORRESPONDENCE_ESTABLISHES_THRESHOLD": "Correspondence establishes threshold.",
    "CORRESPONDENCE_CREATES_TRUTH": "Correspondence creates truth.",
    "CORRESPONDENCE_AUTHORIZES_ACTION": "Correspondence authorizes action.",
    "CORRESPONDENCE_CREATES_CONSEQUENCE": "Correspondence creates consequence.",
    "CORRESPONDENCE_WIDENS_SCOPE": "Correspondence widens scope.",
    "CORRESPONDENCE_HIDES_MISMATCH": "Correspondence hides mismatch.",
    "CORRESPONDENCE_OVERWRITES_LINEAGE": "Correspondence overwrites lineage.",
    "CORRESPONDENCE_UPGRADES_PRECURSOR_TO_CURRENT_LAW": "Correspondence upgrades precursor material to current law.",
    "CORRESPONDENCE_FORCES_SELF_ORIENTATION_SUCCESSOR": "Correspondence forces a self-orientation successor.",
    "CORRESPONDENCE_FORCES_CONFORMANCE_SUCCESSOR": "Correspondence forces a conformance successor.",
    "CORRESPONDENCE_AUTHORIZES_CONTINUATION": "Correspondence authorizes continuation.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required non-claim is missing or flipped.",
    "LATEST_FILE_CURRENTNESS": "Correspondence relies on latest-file currentness or recency fraud.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Correspondence performs mutation, replay, or merge.",
}

METADATA_ID_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_id"),
    ("current_body_conformance_metadata", "current_body_conformance_result_id"),
    ("conformance_closure_metadata", "conformance_closure_result_id"),
    ("body_signal_recognition_metadata", "body_signal_recognition_result_id"),
    ("body_signal_acceptance_metadata", "body_signal_acceptance_result_id"),
    ("body_signal_scope_metadata", "body_signal_scope_result_id"),
    (
        "derivative_vessel_relation_boundary_metadata",
        "derivative_vessel_relation_boundary_result_id",
    ),
    (
        "cross_surface_correspondence_metadata",
        "cross_surface_correspondence_result_id",
    ),
)

METADATA_TYPE_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_type"),
    ("current_body_conformance_metadata", "current_body_conformance_result_type"),
    ("conformance_closure_metadata", "conformance_closure_result_type"),
    ("body_signal_recognition_metadata", "body_signal_recognition_result_type"),
    ("body_signal_acceptance_metadata", "body_signal_acceptance_result_type"),
    ("body_signal_scope_metadata", "body_signal_scope_result_type"),
    (
        "derivative_vessel_relation_boundary_metadata",
        "derivative_vessel_relation_boundary_result_type",
    ),
    (
        "cross_surface_correspondence_metadata",
        "cross_surface_correspondence_result_type",
    ),
)

SUMMARY_KEYS = (
    "current_self_orientation_summary",
    "current_body_conformance_summary",
    "current_body_standing_closure_summary",
    "cross_surface_correspondence_summary",
)

SOURCE_ID_KEYS = (
    "source_basis_id",
    "source_surface_id",
    "source_artifact_id",
    "selected_source_surface_id",
    "selected_source_body_basis_id",
    "recognized_source_artifact_id",
)

SOURCE_PATH_KEYS = (
    "source_basis_path",
    "source_surface_path",
    "source_artifact_path",
    "selected_source_surface_path",
    "selected_source_body_basis_path",
    "recognized_source_artifact_path",
)

SCOPE_KEYS = (
    "scope_id",
    "declared_scope_id",
    "accepted_matter_id",
    "matter_id",
    "declared_matter_id",
    "scope_matter_id",
    "scope_family",
    "scope_kind",
)

NEGATING_KEY_FRAGMENTS = (
    "does_not",
    "do_not",
    "no_",
    "non_",
    "_not_",
    "must_not",
    "cannot",
    "without",
)

ANTI_COLLAPSE_CHECKS = (
    ("no_source_replacement", "source_replaced", ("replace_source", "source_replaced", "source_replacement", "upgraded_to_source"), "CORRESPONDENCE_ATTEMPTS_SOURCE_REPLACEMENT"),
    ("no_authority_creation", "authority_created", ("authority_created", "authority_assigned", "became_authority", "authority_transfer"), "CORRESPONDENCE_ATTEMPTS_AUTHORITY"),
    ("no_currentness_creation", "currentness_created", ("currentness_created", "became_currentness", "currentness_transfer"), "CORRESPONDENCE_ATTEMPTS_CURRENTNESS"),
    ("no_permission_creation", "permission_created", ("permission_created", "became_permission", "permission_transfer", "permission_granted"), "CORRESPONDENCE_ATTEMPTS_PERMISSION"),
    ("no_surface_merge", "surface_merged", ("surface_merged", "merge_surfaces", "merged_surface"), "CORRESPONDENCE_ATTEMPTS_MERGE"),
    ("no_equivalence_creation", "surface_equivalence_created", ("surface_equivalence_created", "equivalence_created", "surfaces_equivalent"), "CORRESPONDENCE_ATTEMPTS_MERGE"),
    ("no_explanation_ownership_creation", "explanation_ownership_created", ("explanation_ownership_created", "explains_other_surface", "explanation_owner"), "CORRESPONDENCE_ATTEMPTS_MERGE"),
    ("no_signal_created_by_default", "signal_created_by_default", ("signal_created_by_default", "became_signal_by_default", "signal_by_default"), "CORRESPONDENCE_CREATES_SIGNAL_BY_DEFAULT"),
    ("no_presence_established", "presence_established", ("presence_established", "presence_created"), "CORRESPONDENCE_ESTABLISHES_PRESENCE"),
    ("no_threshold_met", "threshold_met", ("threshold_met", "threshold_established"), "CORRESPONDENCE_ESTABLISHES_THRESHOLD"),
    ("no_truth_created", "truth_created", ("truth_created", "truth_established"), "CORRESPONDENCE_CREATES_TRUTH"),
    ("no_action_authorized", "action_authorized", ("action_authorized", "action_created"), "CORRESPONDENCE_AUTHORIZES_ACTION"),
    ("no_consequence_created", "consequence_created", ("consequence_created", "consequence_authorized"), "CORRESPONDENCE_CREATES_CONSEQUENCE"),
    ("no_precursor_upgrade_to_current_law", "precursor_upgraded_to_current_law", ("precursor_upgraded_to_current_law", "precursor_became_current_law"), "CORRESPONDENCE_UPGRADES_PRECURSOR_TO_CURRENT_LAW"),
    ("no_self_orientation_successor_forced", "self_orientation_successor_forced", ("self_orientation_successor_forced", "force_self_orientation_successor"), "CORRESPONDENCE_FORCES_SELF_ORIENTATION_SUCCESSOR"),
    ("no_conformance_successor_forced", "conformance_successor_forced", ("conformance_successor_forced", "force_conformance_successor"), "CORRESPONDENCE_FORCES_CONFORMANCE_SUCCESSOR"),
    ("no_continuation_authorized", "continuation_authorized", ("continuation_authorized", "follow_on_work_authorized", "follow_on_steps_authorized", "roadmap_generated"), "CORRESPONDENCE_AUTHORIZES_CONTINUATION"),
    ("no_latest_file_currentness", "latest_file_currentness", ("latest_file_currentness", "latest_file_recency_allowed"), "LATEST_FILE_CURRENTNESS"),
    ("no_recency_fraud", "recency_fraud", ("recency_fraud", "recency_currentness"), "LATEST_FILE_CURRENTNESS"),
)

POSTURE_ONLY_CHECKS = (
    ("no_scope_widening", ("scope_widened", "widen_scope", "applied_outside_declared_scope"), "CORRESPONDENCE_WIDENS_SCOPE"),
    ("no_hidden_mismatch", ("mismatch_hidden", "hide_mismatch", "hidden_mismatch"), "CORRESPONDENCE_HIDES_MISMATCH"),
    ("no_lineage_overwrite", ("lineage_overwritten", "overwrite_lineage", "lineage_replaced"), "CORRESPONDENCE_OVERWRITES_LINEAGE"),
)


def resolve_cross_surface_correspondence_boundary(
    selected_surfaces: Sequence[Mapping[str, Any]] | None = None,
    declared_correspondence_question: str | None = None,
    correspondence_type: str | None = None,
) -> dict[str, Any]:
    """Resolve bounded correspondence for selected standing surface mappings."""

    failures: list[str] = []
    normalized: list[dict[str, Any]] = []
    for index, surface in enumerate(selected_surfaces or []):
        if not isinstance(surface, Mapping):
            failures.append("SELECTED_SURFACE_MALFORMED")
            continue
        normalized.append(_normalize_surface(index, copy.deepcopy(dict(surface)), None))

    return _resolve_normalized(
        normalized,
        declared_correspondence_question,
        correspondence_type,
        failures,
    )


def resolve_cross_surface_correspondence_boundary_from_paths(
    selected_surface_paths: Sequence[Path | str],
    declared_correspondence_question: str,
    correspondence_type: str,
) -> dict[str, Any]:
    """Resolve bounded correspondence for selected standing surface JSON paths."""

    failures: list[str] = []
    normalized: list[dict[str, Any]] = []
    for index, selected_path in enumerate(selected_surface_paths):
        path = Path(selected_path)
        try:
            normalized.append(_normalize_surface(index, _read_json_mapping(path), path))
        except CrossSurfaceCorrespondenceBoundaryError as exc:
            code = "SELECTED_SURFACE_UNREADABLE"
            if "malformed" in str(exc):
                code = "SELECTED_SURFACE_MALFORMED"
            failures.append(code)

    return _resolve_normalized(
        normalized,
        declared_correspondence_question,
        correspondence_type,
        failures,
    )


def write_cross_surface_correspondence_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a bounded correspondence result artifact without overwriting."""

    if output_path is None:
        basis = _as_mapping(result.get("correspondence_basis"))
        surfaces = result.get("selected_surfaces")
        first_surface_id = "selected_surface"
        if isinstance(surfaces, list) and surfaces and isinstance(surfaces[0], Mapping):
            first_surface_id = str(surfaces[0].get("surface_id") or first_surface_id)
        filename = (
            f"{_slug(str(basis.get('correspondence_type') or 'correspondence'))}__"
            f"{_slug(first_surface_id)}__cross_surface_correspondence_result.json"
        )
        target = CROSS_SURFACE_CORRESPONDENCE_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)

    target = _non_overwriting_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_cross_surface_correspondence_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact bounded summary for a correspondence result."""

    checks = _mapping_list(result.get("correspondence_checks"))
    selected_surfaces = _mapping_list(result.get("selected_surfaces"))
    non_claims = _as_mapping(result.get("non_claims"))
    basis = _as_mapping(result.get("correspondence_basis"))
    block = _as_mapping(result.get("block"))
    failed_count = sum(1 for check in checks if check.get("passed") is False)
    passed_count = sum(1 for check in checks if check.get("passed") is True)

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "selected_surface_count": len(selected_surfaces),
        "selected_surface_ids": [surface.get("surface_id") for surface in selected_surfaces],
        "selected_surface_outcomes": [
            surface.get("surface_outcome") for surface in selected_surfaces
        ],
        "declared_correspondence_question": result.get("declared_correspondence_question"),
        "correspondence_type": basis.get("correspondence_type"),
        "correspondence_recognized": result.get("outcome") == CORRESPONDENCE_RECOGNIZED,
        "no_correspondence": result.get("outcome") == NO_CORRESPONDENCE,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "rank_preserved": bool(basis.get("rank_preserved")),
        "source_preserved": bool(basis.get("source_preserved")),
        "scope_preserved": bool(basis.get("scope_preserved")),
        "lineage_preserved": bool(basis.get("lineage_preserved")),
        "non_claims_preserved": bool(basis.get("non_claims_preserved")),
        "source_rank_scope_lineage_non_claims_preserved": bool(
            basis.get("rank_preserved")
            and basis.get("source_preserved")
            and basis.get("scope_preserved")
            and basis.get("lineage_preserved")
            and basis.get("non_claims_preserved")
        ),
        "correspondence_created_authority": bool(non_claims.get("authority_created")),
        "correspondence_created_currentness": bool(non_claims.get("currentness_created")),
        "correspondence_created_permission": bool(non_claims.get("permission_created")),
        "correspondence_created_signal": bool(non_claims.get("signal_created_by_default")),
        "correspondence_established_presence": bool(non_claims.get("presence_established")),
        "correspondence_established_threshold": bool(non_claims.get("threshold_met")),
        "correspondence_created_truth": bool(non_claims.get("truth_created")),
        "correspondence_authorized_action": bool(non_claims.get("action_authorized")),
        "correspondence_created_consequence": bool(non_claims.get("consequence_created")),
        "self_orientation_successor_forced": bool(
            non_claims.get("self_orientation_successor_forced")
        ),
        "conformance_successor_forced": bool(non_claims.get("conformance_successor_forced")),
        "continuation_authorized": bool(non_claims.get("continuation_authorized")),
        "key_non_claims": _key_non_claims(non_claims),
    }


def _resolve_normalized(
    surfaces: list[dict[str, Any]],
    question: str | None,
    correspondence_type: str | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    declared_question = (question or "").strip()
    relation_type = (correspondence_type or "").strip()
    non_claims = _build_non_claims(surfaces)
    checks = _build_checks(surfaces, declared_question, relation_type, non_claims, precheck_failures)
    failed_checks = [check for check in checks if check.get("passed") is False]
    basis = _build_basis(surfaces, relation_type, non_claims, failed_checks)

    if failed_checks:
        outcome = BLOCKED
        first_failure = failed_checks[0]
        block_code = str(first_failure.get("block_code"))
        block = {"code": block_code, "reason": BLOCK_REASONS.get(block_code, "Correspondence blocked.")}
        correspondence_result = {
            "correspondence_recognized": False,
            "no_correspondence": False,
            "blocked": True,
            "block_code": block_code,
            "failed_check": first_failure.get("check_name"),
            "blocked_correspondence_does_not_invalidate_selected_surfaces": True,
        }
    else:
        evaluated = _evaluate_relation(surfaces, relation_type, declared_question)
        outcome = evaluated["outcome"]
        block = {"code": None, "reason": None}
        correspondence_result = evaluated["correspondence_result"]

    result: dict[str, Any] = {
        "cross_surface_correspondence_metadata": {
            "cross_surface_correspondence_result_id": _result_id(surfaces, relation_type),
            "cross_surface_correspondence_result_type": "cross_surface_correspondence_boundary_result",
            "cross_surface_correspondence_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_surfaces": [_public_surface(surface) for surface in surfaces],
        "declared_correspondence_question": declared_question or None,
        "correspondence_basis": basis,
        "correspondence_checks": checks,
        "correspondence_result": correspondence_result,
        "correspondence_non_meaning": _correspondence_non_meaning(),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["cross_surface_correspondence_summary"] = build_cross_surface_correspondence_summary(result)
    return result


def _build_checks(
    surfaces: Sequence[dict[str, Any]],
    question: str,
    relation_type: str,
    non_claims: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, expected: str, actual: Any, code: str) -> None:
        checks.append(
            {
                "check_name": name,
                "passed": bool(passed),
                "expected_posture": expected,
                "actual_posture": actual,
                "block_code": None if passed else code,
            }
        )

    malformed_code = (
        "SELECTED_SURFACE_UNREADABLE"
        if "SELECTED_SURFACE_UNREADABLE" in precheck_failures
        else "SELECTED_SURFACE_MALFORMED"
    )
    add(
        "selected_surfaces_are_parseable_mappings",
        not precheck_failures,
        "all selected surfaces parse as mappings",
        list(precheck_failures),
        malformed_code,
    )
    add("selected_surfaces_exist", len(surfaces) >= 2, "at least two selected surfaces", len(surfaces), "SELECTED_SURFACE_MISSING")
    add("selected_surfaces_have_identity", bool(surfaces) and all(s.get("surface_id") for s in surfaces), "each selected surface exposes identity", [s.get("surface_id") for s in surfaces], "SELECTED_SURFACE_IDENTITY_MISSING")
    add("selected_surfaces_have_outcome", bool(surfaces) and all(s.get("surface_outcome") for s in surfaces), "each selected surface exposes outcome or status", [s.get("surface_outcome") for s in surfaces], "SELECTED_SURFACE_OUTCOME_MISSING")
    add("correspondence_question_declared", bool(question), "declared correspondence question is non-empty", question or None, "CORRESPONDENCE_QUESTION_UNDECLARED")
    add("correspondence_type_supported", relation_type in PERMITTED_CORRESPONDENCE_TYPES, "correspondence type is in bounded permitted set", relation_type or None, "CORRESPONDENCE_TYPE_UNSUPPORTED")

    source_basis_values = _source_basis_values(surfaces)
    source_required = relation_type in {"BASIS_MATCH", "BASIS_MISMATCH"}
    add("source_basis_known_where_required", not source_required or len(source_basis_values) == len(surfaces), "source basis exposed for basis correspondence types", source_basis_values, "SOURCE_BASIS_UNKNOWN")
    add("source_downstream_posture_bounded_where_required", bool(surfaces) and all(s.get("source_downstream_posture") for s in surfaces), "source/downstream posture remains bounded", [s.get("source_downstream_posture") for s in surfaces], "DOWNSTREAM_BASIS_UNKNOWN")

    for name, claim_key, markers, code in ANTI_COLLAPSE_CHECKS:
        passed = not non_claims[claim_key] and not _collapse_attempt_present(surfaces, markers)
        add(name, passed, "correspondence preserves anti-collapse posture", non_claims[claim_key], code)

    for name, markers, code in POSTURE_ONLY_CHECKS:
        add(name, not _collapse_attempt_present(surfaces, markers), "correspondence preserves bounded posture", False, code)

    mutation_or_merge = (
        non_claims["mutation_performed"]
        or non_claims["replay_performed"]
        or non_claims["merge_performed"]
        or _collapse_attempt_present(surfaces, ("mutation_performed", "replay_performed", "merge_performed"))
    )
    add(
        "no_mutation_replay_or_merge",
        not mutation_or_merge,
        "correspondence performs no mutation, replay, or merge",
        {
            "mutation_performed": non_claims["mutation_performed"],
            "replay_performed": non_claims["replay_performed"],
            "merge_performed": non_claims["merge_performed"],
        },
        "MUTATION_REPLAY_OR_MERGE_DETECTED",
    )
    add(
        "required_non_claims_remain_false",
        all(value is False for value in non_claims.values()),
        "all result-level non-claims remain false",
        non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    return checks


def _evaluate_relation(
    surfaces: Sequence[dict[str, Any]],
    relation_type: str,
    question: str,
) -> dict[str, Any]:
    evidence: dict[str, Any] = {}
    recognized = False
    reason = "Required positive correspondence evidence was not exposed."

    if relation_type == "NO_CORRESPONDENCE":
        return _no_correspondence(relation_type, question, "Declared relation type is NO_CORRESPONDENCE.")
    if relation_type == "BASIS_MATCH":
        values = _source_basis_values(surfaces)
        recognized = bool(values) and len(set(values)) == 1
        evidence = {"source_basis_values": values}
        reason = "Exposed source basis values do not all match."
    elif relation_type == "BASIS_MISMATCH":
        values = _source_basis_values(surfaces)
        recognized = bool(values) and len(set(values)) > 1
        evidence = {"source_basis_values": values}
        reason = "Exposed source basis values do not differ."
    elif relation_type == "DOWNSTREAM_RECOGNITION":
        refs = _surface_references(surfaces, broad=False)
        recognized = bool(refs)
        evidence = {"recognized_references": refs}
        reason = "No selected surface explicitly recognizes or selects another."
    elif relation_type == "SCOPE_ALIGNMENT":
        scopes = _scope_values(surfaces)
        common = _common_scope_values(scopes)
        recognized = bool(common)
        evidence = {"scope_or_matter_values": scopes, "common_values": common}
        reason = "No exposed scope or matter values align."
    elif relation_type == "SCOPE_MISMATCH":
        scopes = _scope_values(surfaces)
        recognized = len(scopes) == len(surfaces) and all(scopes) and not _common_scope_values(scopes)
        evidence = {"scope_or_matter_values": scopes}
        reason = "Exposed scope or matter values do not show bounded mismatch."
    elif relation_type == "NON_CLAIM_ALIGNMENT":
        recognized, evidence = _non_claim_alignment(surfaces)
        reason = "Selected surfaces do not expose aligned false non-claim posture."
    elif relation_type == "NON_CLAIM_CONFLICT":
        recognized, evidence = _non_claim_conflict(surfaces)
        reason = "Selected surfaces do not expose a bounded non-claim conflict."
    elif relation_type == "LINEAGE_REFERENCE":
        refs = _surface_references(surfaces, broad=True)
        recognized = bool(refs)
        evidence = {"lineage_references": refs}
        reason = "No selected surface references another as lineage or basis."
    elif relation_type == "CLOSURE_ALIGNMENT":
        recognized, evidence = _closure_alignment(surfaces)
        reason = "Closure, conformance, and v6 basis alignment was not exposed."
    elif relation_type == "REFUSAL_VISIBLE":
        recognized, evidence = _refusal_visible(surfaces)
        reason = "No selected blocked or refused posture is visible."

    if not recognized:
        return _no_correspondence(relation_type, question, reason, evidence)

    return {
        "outcome": CORRESPONDENCE_RECOGNIZED,
        "correspondence_result": {
            "correspondence_recognized": True,
            "no_correspondence": False,
            "correspondence_type": relation_type,
            "declared_correspondence_question": question,
            "correspondence_claim": "Selected surfaces may be read together under bounded correspondence for the declared question.",
            "evidence": evidence,
            "local_outcomes_preserved": True,
            "rank_source_scope_lineage_preserved": True,
            "non_claims_preserved": True,
        },
    }


def _no_correspondence(
    relation_type: str,
    question: str,
    reason: str,
    evidence: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "outcome": NO_CORRESPONDENCE,
        "correspondence_result": {
            "correspondence_recognized": False,
            "no_correspondence": True,
            "correspondence_type": relation_type,
            "declared_correspondence_question": question,
            "reason": reason,
            "evidence": dict(evidence or {}),
            "selected_surfaces_preserved_in_local_posture": True,
        },
    }


def _normalize_surface(
    surface_index: int,
    surface: Mapping[str, Any],
    path: Path | None,
) -> dict[str, Any]:
    surface_copy = dict(surface)
    return {
        "surface_index": surface_index,
        "surface_id": _extract_surface_id(surface_copy),
        "surface_path": str(path) if path is not None else _extract_path(surface_copy),
        "surface_outcome": _extract_surface_outcome(surface_copy),
        "surface_type": _extract_surface_type(surface_copy),
        "source_basis_id": _extract_first_by_keys(surface_copy, SOURCE_ID_KEYS),
        "source_basis_path": _extract_first_by_keys(surface_copy, SOURCE_PATH_KEYS),
        "source_downstream_posture": _extract_source_downstream_posture(surface_copy),
        "non_claims": _extract_non_claims(surface_copy),
        "raw_surface_family_hint": _family_hint(surface_copy),
        "scope_or_matter_values": _extract_scope_values(surface_copy),
        "_raw": surface_copy,
    }


def _public_surface(surface: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "surface_index": surface.get("surface_index"),
        "surface_id": surface.get("surface_id"),
        "surface_path": surface.get("surface_path"),
        "surface_outcome": surface.get("surface_outcome"),
        "surface_type": surface.get("surface_type"),
        "source_basis_id": surface.get("source_basis_id"),
        "source_basis_path": surface.get("source_basis_path"),
        "source_downstream_posture": surface.get("source_downstream_posture"),
        "non_claims": copy.deepcopy(surface.get("non_claims", {})),
        "raw_surface_family_hint": surface.get("raw_surface_family_hint"),
        "scope_or_matter_values": copy.deepcopy(surface.get("scope_or_matter_values", [])),
    }


def _build_basis(
    surfaces: Sequence[dict[str, Any]],
    relation_type: str,
    non_claims: Mapping[str, bool],
    failed_checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    anti_collapse_failed = bool(failed_checks)
    source_preserved = not (
        non_claims.get("source_replaced")
        or non_claims.get("standing_upgraded")
        or non_claims.get("source_derivative_operator_collapsed")
    )
    return {
        "correspondence_type": relation_type or None,
        "permitted_correspondence_types": sorted(PERMITTED_CORRESPONDENCE_TYPES),
        "selected_surface_count": len(surfaces),
        "selected_surface_ids": [surface.get("surface_id") for surface in surfaces],
        "selected_surface_outcomes": [surface.get("surface_outcome") for surface in surfaces],
        "source_basis_values": _source_basis_values(surfaces),
        "scope_or_matter_values": _scope_values(surfaces),
        "rank_preserved": not anti_collapse_failed,
        "source_preserved": source_preserved,
        "scope_preserved": not anti_collapse_failed,
        "lineage_preserved": not anti_collapse_failed,
        "non_claims_preserved": all(value is False for value in non_claims.values()),
        "local_outcomes_remain_local": True,
        "correspondence_does_not_command_work": True,
    }


def _build_non_claims(surfaces: Sequence[Mapping[str, Any]]) -> dict[str, bool]:
    result = dict(NON_CLAIMS)
    for surface in surfaces:
        exposed = _as_mapping(surface.get("non_claims"))
        for key in result:
            if exposed.get(key) is True:
                result[key] = True
    if _collapse_attempt_present(surfaces, ("source_derivative_operator_collapsed",)):
        result["source_derivative_operator_collapsed"] = True
    return result


def _correspondence_non_meaning() -> dict[str, bool]:
    return {
        "does_not_create_equivalence": True,
        "does_not_merge_surfaces": True,
        "does_not_create_explanation_ownership": True,
        "does_not_replace_source": True,
        "does_not_transfer_currentness": True,
        "does_not_transfer_permission": True,
        "does_not_transfer_authority": True,
        "does_not_create_signal_by_default": True,
        "does_not_establish_presence": True,
        "does_not_establish_threshold": True,
        "does_not_create_truth": True,
        "does_not_authorize_action": True,
        "does_not_create_consequence": True,
        "does_not_open_next_work": True,
        "does_not_force_self_orientation_successor": True,
        "does_not_force_conformance_successor": True,
        "does_not_create_routing": True,
        "does_not_create_workflow": True,
        "does_not_create_body_relevance_medium": True,
        "does_not_create_distributed_standing": True,
        "does_not_create_multi_carrier_law": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_surfaces": [
            "presence law",
            "threshold law",
            "truth law",
            "action/consequence law",
            "multi-carrier relation law",
            "persistence/registry law",
            "generalized vessel relation lifecycle",
            "body relevance medium",
            "signal series or accumulation logic",
            "distributed standing",
            "future self-orientation successor only if separately justified",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _extract_surface_id(surface: Mapping[str, Any]) -> str | None:
    for key in ("surface_id", "result_id"):
        if _has_text(surface.get(key)):
            return str(surface[key])
    for metadata_key, id_key in METADATA_ID_PATHS:
        metadata = surface.get(metadata_key)
        if isinstance(metadata, Mapping) and _has_text(metadata.get(id_key)):
            return str(metadata[id_key])
    return _string_or_none(_find_first_key_value(surface, lambda key: key.endswith("_result_id")))


def _extract_surface_outcome(surface: Mapping[str, Any]) -> str | None:
    for key in ("outcome", "surface_outcome", "status"):
        if _has_text(surface.get(key)):
            return str(surface[key])
    for summary_key in SUMMARY_KEYS:
        summary = surface.get(summary_key)
        if isinstance(summary, Mapping):
            for key in ("outcome", "surface_outcome", "status"):
                if _has_text(summary.get(key)):
                    return str(summary[key])
    return _string_or_none(
        _find_first_key_value(surface, lambda key: key == "outcome" or key.endswith("_outcome"))
    )


def _extract_surface_type(surface: Mapping[str, Any]) -> str | None:
    for key in ("surface_type", "result_type"):
        if _has_text(surface.get(key)):
            return str(surface[key])
    for metadata_key, type_key in METADATA_TYPE_PATHS:
        metadata = surface.get(metadata_key)
        if isinstance(metadata, Mapping) and _has_text(metadata.get(type_key)):
            return str(metadata[type_key])
    return _string_or_none(_find_first_key_value(surface, lambda key: key.endswith("_result_type")))


def _extract_path(surface: Mapping[str, Any]) -> str | None:
    for key in (
        "surface_path",
        "result_path",
        "artifact_path",
        "self_orientation_result_path",
        "current_body_conformance_result_path",
        "conformance_closure_result_path",
    ):
        if _has_text(surface.get(key)):
            return str(surface[key])
    return _string_or_none(_find_first_key_value(surface, lambda key: key.endswith("_path")))


def _extract_first_by_keys(surface: Mapping[str, Any], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = _find_first_key_value(surface, lambda found_key, key=key: found_key == key)
        if _has_text(value):
            return str(value)
    return None


def _extract_source_downstream_posture(surface: Mapping[str, Any]) -> str:
    for key in (
        "source_downstream_posture",
        "surface_posture",
        "downstream_posture",
        "source_body_posture",
    ):
        value = _find_first_key_value(surface, lambda found_key, key=key: found_key == key)
        if _has_text(value):
            return str(value)
    family = _family_hint(surface)
    if "self_orientation" in family or "body_pass" in family:
        return "upstream_current_or_source_posture_bounded"
    return "downstream_or_local_posture_bounded"


def _family_hint(surface: Mapping[str, Any]) -> str:
    for key in surface:
        if key.endswith("_metadata"):
            return key.removesuffix("_metadata")
    return "standing_surface"


def _extract_non_claims(surface: Mapping[str, Any]) -> dict[str, Any]:
    combined: dict[str, Any] = {}
    for key, value in _walk_items(surface):
        if key in {"non_claims", "key_non_claims", "false_non_claims"} and isinstance(value, Mapping):
            combined.update(dict(value))
    return combined


def _extract_scope_values(surface: Mapping[str, Any]) -> list[str]:
    values = []
    for key in SCOPE_KEYS:
        value = _find_first_key_value(surface, lambda found_key, key=key: found_key == key)
        if _has_text(value):
            values.append(str(value))
    return _unique(values)


def _surface_references(
    surfaces: Sequence[dict[str, Any]],
    broad: bool,
) -> list[dict[str, Any]]:
    references: list[dict[str, Any]] = []
    lineage_tokens = ("predecessor", "successor", "basis", "selected", "source")
    for source in surfaces:
        raw_text = json.dumps(source.get("_raw", {}), sort_keys=True, default=str)
        lowered = raw_text.lower()
        if broad and not any(token in lowered for token in lineage_tokens):
            continue
        for target in surfaces:
            if source.get("surface_index") == target.get("surface_index"):
                continue
            for marker in (target.get("surface_id"), target.get("surface_path")):
                if marker and str(marker) in raw_text:
                    references.append(
                        {
                            "referencing_surface_id": source.get("surface_id"),
                            "referenced_surface_id": target.get("surface_id"),
                            "reference_marker": str(marker),
                        }
                    )
                    break
    return references


def _closure_alignment(surfaces: Sequence[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    outcomes = {surface.get("surface_outcome") for surface in surfaces}
    refs = _surface_references(surfaces, broad=True)
    closure_present = "CONFORMANCE_CLOSURE_RECORDED" in outcomes
    basis_present = bool({"BODY_CONFORMANT", "SELF_ORIENTED"}.intersection(outcomes))
    return (
        bool(closure_present and basis_present and refs),
        {"surface_outcomes": sorted(str(item) for item in outcomes if item), "alignment_references": refs},
    )


def _refusal_visible(surfaces: Sequence[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    visible = []
    for surface in surfaces:
        block = _find_first_key_value(_as_mapping(surface.get("_raw")), lambda key: key == "block")
        block_code = block.get("code") if isinstance(block, Mapping) else None
        if surface.get("surface_outcome") == BLOCKED or block_code:
            visible.append(
                {
                    "surface_id": surface.get("surface_id"),
                    "surface_outcome": surface.get("surface_outcome"),
                    "block_code": block_code,
                }
            )
    return bool(visible), {"visible_refusals": visible}


def _non_claim_alignment(surfaces: Sequence[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    exposed = [_as_mapping(surface.get("non_claims")) for surface in surfaces if _as_mapping(surface.get("non_claims"))]
    if len(exposed) < 2:
        return False, {"aligned_false_non_claims": {}}
    common_keys = set(exposed[0])
    for claims in exposed[1:]:
        common_keys &= set(claims)
    aligned = {key: False for key in sorted(common_keys) if all(claims.get(key) is False for claims in exposed)}
    return bool(aligned), {"aligned_false_non_claims": aligned}


def _non_claim_conflict(surfaces: Sequence[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    exposed = [_as_mapping(surface.get("non_claims")) for surface in surfaces if _as_mapping(surface.get("non_claims"))]
    conflicts: dict[str, list[Any]] = {}
    keys = set().union(*(claims.keys() for claims in exposed)) if exposed else set()
    for key in sorted(keys):
        values = [claims.get(key) for claims in exposed if key in claims]
        if len({json.dumps(value, sort_keys=True, default=str) for value in values}) > 1:
            conflicts[key] = values
    return bool(conflicts), {"non_claim_conflicts": conflicts}


def _source_basis_values(surfaces: Sequence[Mapping[str, Any]]) -> list[str]:
    values = []
    for surface in surfaces:
        value = surface.get("source_basis_id") or surface.get("source_basis_path")
        if _has_text(value):
            values.append(str(value))
    return values


def _scope_values(surfaces: Sequence[Mapping[str, Any]]) -> list[list[str]]:
    return [list(surface.get("scope_or_matter_values") or []) for surface in surfaces]


def _common_scope_values(scope_values: Sequence[Sequence[str]]) -> list[str]:
    populated = [set(values) for values in scope_values if values]
    return sorted(set.intersection(*populated)) if populated else []


def _collapse_attempt_present(
    surfaces: Sequence[Mapping[str, Any]],
    markers: Sequence[str],
) -> bool:
    for surface in surfaces:
        raw = _as_mapping(surface.get("_raw"))
        for key, value in _walk_items(raw):
            normalized_key = key.lower()
            negating_key = any(fragment in normalized_key for fragment in NEGATING_KEY_FRAGMENTS)
            if value is True and not negating_key and any(marker in normalized_key for marker in markers):
                return True
            if value is False and negating_key and _protective_marker_matches(normalized_key, markers):
                return True
    return False


def _protective_marker_matches(normalized_key: str, markers: Sequence[str]) -> bool:
    if any(marker in normalized_key for marker in markers):
        return True
    marker_text = " ".join(markers)
    tokens = (
        "source",
        "authority",
        "currentness",
        "permission",
        "merge",
        "equivalence",
        "explanation",
        "signal",
        "presence",
        "threshold",
        "truth",
        "action",
        "consequence",
        "scope",
        "mismatch",
        "lineage",
        "precursor",
        "self_orientation_successor",
        "conformance_successor",
        "continuation",
        "latest_file",
        "recency",
        "mutation",
        "replay",
    )
    return any(token in normalized_key and token in marker_text for token in tokens)


def _read_json_mapping(path: Path) -> dict[str, Any]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CrossSurfaceCorrespondenceBoundaryError(f"selected surface unreadable: {path}") from exc
    except OSError as exc:
        raise CrossSurfaceCorrespondenceBoundaryError(f"selected surface unreadable: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CrossSurfaceCorrespondenceBoundaryError(f"selected surface malformed: {path}") from exc
    if not isinstance(parsed, dict):
        raise CrossSurfaceCorrespondenceBoundaryError(f"selected surface malformed: {path}")
    return parsed


def _result_id(surfaces: Sequence[Mapping[str, Any]], relation_type: str) -> str:
    first_id = "selected_surface"
    if surfaces and surfaces[0].get("surface_id"):
        first_id = str(surfaces[0]["surface_id"])
    return f"{_slug(relation_type or 'correspondence')}__{_slug(first_id)}__cross_surface_correspondence_result"


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "authority_created",
        "permission_created",
        "currentness_created",
        "source_replaced",
        "surface_merged",
        "surface_equivalence_created",
        "signal_created_by_default",
        "presence_established",
        "threshold_met",
        "truth_created",
        "action_authorized",
        "consequence_created",
        "self_orientation_successor_forced",
        "conformance_successor_forced",
        "continuation_authorized",
        "latest_file_currentness",
        "recency_fraud",
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    )
    return {key: non_claims.get(key) for key in keys}


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise CrossSurfaceCorrespondenceBoundaryError(f"could not create non-overwriting output path under {path.parent}")


def _slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value)).strip("_")[:120] or "surface"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_or_none(value: Any) -> str | None:
    return str(value) if _has_text(value) else None


def _unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result


def _find_first_key_value(value: Any, predicate: Any) -> Any:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            if predicate(str(key)):
                return nested_value
            found = _find_first_key_value(nested_value, predicate)
            if found is not None:
                return found
    elif isinstance(value, list):
        for item in value:
            found = _find_first_key_value(item, predicate)
            if found is not None:
                return found
    return None


def _walk_items(value: Any) -> Iterable[tuple[str, Any]]:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            yield str(key), nested_value
            yield from _walk_items(nested_value)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_items(item)
