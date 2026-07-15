"""Resolve the bounded effective current family for v0-min coexistence.

This module reads the current authority, run-family, preserved-run status, and
current-governing artifacts. It may also read one successor-adoption result and
the adopted successor family named by that result. It returns one explicit
effective-family resolution stating which family should be used for subsequent
bounded work.

The resolver is additive engineering. It does not replay source actions into a
live host, merge preserved runs, mutate prior artifacts, complete continuity,
upgrade standing, define persistence or registry law, or treat successor-family
emission as self-executing currentness.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from build_current_integrity_host_v0_min_coexistence_governing_packet import (
    CurrentGoverningPacketError,
    build_current_governing_summary,
)
from build_integrity_host_v0_min_coexistence_preserved_run_status_packet import (
    PreservedRunStatusPacketError,
    build_preserved_run_status_summary,
)
from build_integrity_host_v0_min_coexistence_run_family_packet import (
    RunFamilyPacketError,
    build_run_family_summary,
)
from resolve_current_integrity_host_v0_min_coexistence_execution_authority import (
    DECISION_RESOLVED,
    ExecutionAuthorityResolutionError,
    build_execution_authority_summary,
)
from resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 import (
    OUTCOME_ADOPTED,
    OUTCOME_BLOCKED as ADOPTION_BLOCKED,
    GoverningSuccessorAdoptionError,
    build_governing_successor_adoption_summary,
)


EXECUTION_AUTHORITY_RESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_execution_authority"
)
RUN_FAMILY_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_run_family_packets"
)
PRESERVED_RUN_STATUS_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_preserved_run_status_packets"
)
CURRENT_GOVERNING_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_governing_packets"
)
GOVERNING_SUCCESSOR_ADOPTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_governing_successor_adoptions"
)
EFFECTIVE_FAMILY_RESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_effective_family"
)

EFFECTIVE_FAMILY_RESOLUTION_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_EFFECTIVE_FAMILY_RESOLUTION"
)
EFFECTIVE_FAMILY_RESOLUTION_VERSION = "0.1.0"

OUTCOME_CURRENT_FAMILY_EFFECTIVE = "CURRENT_FAMILY_EFFECTIVE"
OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE = "ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE"

BASIS_CURRENT_FAMILY_REMAINS_EFFECTIVE = "CURRENT_FAMILY_REMAINS_EFFECTIVE"
BASIS_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE = "ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE"

NON_CLAIM_DEFAULTS = {
    "continuity_completed": False,
    "standing_upgraded": False,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
    "minimum_lawful_system_completed": False,
    "final_system_identity_completed": False,
    "final_preserved_run_governance_completed": False,
    "final_governing_scope_completed": False,
    "final_governing_transition_law_completed": False,
    "final_governing_reresolution_completed": False,
    "final_governing_successor_adoption_completed": False,
    "final_effective_family_resolution_completed": False,
}


class EffectiveFamilyResolutionError(RuntimeError):
    """Raised when bounded effective-family resolution cannot proceed."""


def discover_latest_authority_resolution(root: Path) -> Path:
    """Return the lexically latest current execution-authority artifact."""

    return _latest_required(
        root,
        "current_execution_authority_resolution*.json",
        "execution-authority resolution root",
    )


def discover_latest_run_family_packet(root: Path) -> Path:
    """Return the lexically latest current run-family packet artifact."""

    return _latest_required(root, "current_run_family_packet*.json", "run-family packet root")


def discover_latest_preserved_run_status_packet(root: Path) -> Path:
    """Return the lexically latest preserved-run status packet artifact."""

    return _latest_required(
        root,
        "current_preserved_run_status_packet*.json",
        "preserved-run status packet root",
    )


def discover_latest_current_governing_packet(root: Path) -> Path:
    """Return the lexically latest current-governing packet artifact."""

    return _latest_required(
        root,
        "current_governing_packet*.json",
        "current-governing packet root",
    )


def discover_latest_adopted_successor_adoption_result(root: Path) -> Path:
    """Return the lexically latest adopted successor-adoption result."""

    selection = _select_default_adoption_result(root)
    selected = selection["selected_adoption_result_path"]
    if not isinstance(selected, Path):
        raise EffectiveFamilyResolutionError("No adopted successor-adoption result found")
    return selected


def resolve_effective_current_family(
    adoption_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve which artifact family is effective for subsequent bounded work."""

    stack = _load_current_stack()
    _verify_current_stack(stack)
    base_non_claims = _stack_non_claims(stack)

    if adoption_result is None:
        selection = _select_default_adoption_result(GOVERNING_SUCCESSOR_ADOPTION_ROOT)
        selected_path = selection.get("selected_adoption_result_path")
        if selected_path is None:
            return _current_family_result(
                stack=stack,
                selection=selection,
                non_claims=base_non_claims,
                selected_adoption=None,
                adoption_path=None,
            )
        if not isinstance(selected_path, Path):
            raise EffectiveFamilyResolutionError("Selected adoption-result path is malformed")
        selected_adoption = _read_adoption_result(selected_path)
        return _adopted_family_result(
            stack=stack,
            adoption=selected_adoption,
            adoption_path=selected_path,
            base_non_claims=base_non_claims,
            selection=selection,
        )

    if not isinstance(adoption_result, Mapping):
        raise EffectiveFamilyResolutionError("Adoption result must be a mapping or None")
    selected_adoption = _validate_adoption_result(dict(adoption_result))
    if selected_adoption.get("outcome") != OUTCOME_ADOPTED:
        selection = {
            "selected_adoption_result_path": None,
            "actual": {
                "provided_adoption_outcome": selected_adoption.get("outcome"),
                "adopted_successor_result_available": False,
            },
            "input_references": {"adoption_result_source": "provided_mapping"},
        }
        return _current_family_result(
            stack=stack,
            selection=selection,
            non_claims=base_non_claims,
            selected_adoption=selected_adoption,
            adoption_path=None,
        )
    return _adopted_family_result(
        stack=stack,
        adoption=selected_adoption,
        adoption_path=None,
        base_non_claims=base_non_claims,
        selection={"input_references": {"adoption_result_source": "provided_mapping"}},
    )


def resolve_effective_current_family_from_path(path: Path | str) -> dict[str, Any]:
    """Read one adoption-result artifact and resolve the effective family from it."""

    adoption_path = _repo_path(Path(path))
    adoption = _read_adoption_result(adoption_path)
    stack = _load_current_stack()
    _verify_current_stack(stack)
    base_non_claims = _stack_non_claims(stack)
    if adoption.get("outcome") != OUTCOME_ADOPTED:
        selection = {
            "selected_adoption_result_path": None,
            "actual": {
                "provided_adoption_outcome": adoption.get("outcome"),
                "adopted_successor_result_available": False,
            },
            "input_references": {
                "selected_adoption_result_artifact_path": _display(adoption_path)
            },
        }
        return _current_family_result(
            stack=stack,
            selection=selection,
            non_claims=base_non_claims,
            selected_adoption=adoption,
            adoption_path=adoption_path,
        )
    return _adopted_family_result(
        stack=stack,
        adoption=adoption,
        adoption_path=adoption_path,
        base_non_claims=base_non_claims,
        selection={
            "input_references": {
                "selected_adoption_result_artifact_path": _display(adoption_path)
            }
        },
    )


def write_effective_family_resolution(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 effective-family resolution artifact."""

    if not isinstance(result, Mapping):
        raise EffectiveFamilyResolutionError("Effective-family resolution must be a mapping")
    target = (
        _repo_root() / EFFECTIVE_FAMILY_RESOLUTION_ROOT / "current_effective_family_resolution.json"
        if output_path is None
        else _repo_path(Path(output_path))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise EffectiveFamilyResolutionError(
            f"Refusing to overwrite effective-family resolution: {_display(target)}"
        )
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_effective_family_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one effective-family resolution."""

    metadata = _obj(result, "resolution_metadata", "effective-family resolution")
    selected = result.get("selected_adoption_result")
    selected_map = selected if isinstance(selected, Mapping) else {}
    effective = _obj(result, "effective_family", "effective-family resolution")
    prior = _obj(result, "prior_current_family", "effective-family resolution")
    non_claims = _obj(result, "non_claims", "effective-family resolution")
    return {
        "effective_family_resolution_id": _str(
            metadata,
            "effective_family_resolution_id",
            "effective-family resolution metadata",
        ),
        "outcome": _str(result, "outcome", "effective-family resolution"),
        "selected_adoption_result_id": selected_map.get("adoption_result_id"),
        "effective_authority_artifact_path": effective.get(
            "effective_authority_artifact_path"
        ),
        "effective_family_packet_path": effective.get("effective_family_packet_path"),
        "effective_status_packet_path": effective.get("effective_status_packet_path"),
        "effective_current_governing_packet_path": effective.get(
            "effective_current_governing_packet_path"
        ),
        "effective_source_run_path": effective.get("effective_source_run_path"),
        "effective_ingress_run_path": effective.get("effective_ingress_run_path"),
        "prior_current_family": dict(prior),
        "non_claims": {
            key: _bool(non_claims, key, "effective-family resolution.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _current_family_result(
    *,
    stack: Mapping[str, Any],
    selection: Mapping[str, Any],
    non_claims: Mapping[str, bool],
    selected_adoption: Mapping[str, Any] | None,
    adoption_path: Path | None,
) -> dict[str, Any]:
    checks = [
        _check(
            "current_family_artifacts_readable",
            "current authority, family, status, and governing artifacts readable",
            _prior_family_reference(stack),
            True,
        ),
        _check(
            "current_family_canonical_core_matches",
            "one canonical core execution file across current family",
            _current_core_set(stack),
            len(_current_core_set(stack)) == 1,
        ),
        _check(
            "no_adopted_successor_result_available",
            "no adopted successor result selected by default or provided input",
            selection.get("actual"),
            selected_adoption is None or selected_adoption.get("outcome") != OUTCOME_ADOPTED,
        ),
        _check(
            "current_family_not_replaced_by_blocked_adoption",
            "blocked adoption results do not drive effective-family change",
            selected_adoption.get("outcome") if selected_adoption is not None else None,
            selected_adoption is None or selected_adoption.get("outcome") != OUTCOME_ADOPTED,
        ),
        _check(
            "non_claims_remain_false",
            "all effective-family non-claims remain false",
            non_claims,
            _all_non_claims_false(non_claims),
        ),
    ]
    if not all(check["passed"] for check in checks):
        raise EffectiveFamilyResolutionError("Current-family effective checks did not pass")

    return _resolution(
        stack=stack,
        adopted_family=None,
        selected_adoption=selected_adoption,
        adoption_path=adoption_path,
        checks=checks,
        outcome=OUTCOME_CURRENT_FAMILY_EFFECTIVE,
        basis=BASIS_CURRENT_FAMILY_REMAINS_EFFECTIVE,
        basis_reason=(
            "No coherent adopted successor result was selected; the current "
            "artifact family remains effective without invented adoption."
        ),
        non_claims=non_claims,
        selection=selection,
    )


def _adopted_family_result(
    *,
    stack: Mapping[str, Any],
    adoption: Mapping[str, Any],
    adoption_path: Path | None,
    base_non_claims: Mapping[str, bool],
    selection: Mapping[str, Any],
) -> dict[str, Any]:
    adopted_family = _load_adopted_family_from_adoption(adoption)
    non_claims = _combined_non_claims(base_non_claims, adoption, adopted_family)
    checks = _adopted_family_checks(stack, adoption, adoption_path, adopted_family, non_claims)
    if not all(check["passed"] for check in checks):
        failed = next(check for check in checks if check["passed"] is not True)
        raise EffectiveFamilyResolutionError(
            f"Adopted successor family is not coherent: {failed['check']}"
        )

    return _resolution(
        stack=stack,
        adopted_family=adopted_family,
        selected_adoption=adoption,
        adoption_path=adoption_path,
        checks=checks,
        outcome=OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
        basis=BASIS_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
        basis_reason=(
            "A coherent ADOPTED successor-family result was selected and its "
            "adopted family artifacts passed bounded correspondence checks."
        ),
        non_claims=non_claims,
        selection=selection,
    )


def _resolution(
    *,
    stack: Mapping[str, Any],
    adopted_family: Mapping[str, Any] | None,
    selected_adoption: Mapping[str, Any] | None,
    adoption_path: Path | None,
    checks: list[dict[str, Any]],
    outcome: str,
    basis: str,
    basis_reason: str,
    non_claims: Mapping[str, bool],
    selection: Mapping[str, Any],
) -> dict[str, Any]:
    effective_stack = adopted_family if outcome == OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE else stack
    return {
        "resolution_metadata": {
            "effective_family_resolution_id": _effective_family_resolution_id(
                selected_adoption,
                outcome,
            ),
            "effective_family_resolution_type": EFFECTIVE_FAMILY_RESOLUTION_TYPE,
            "effective_family_resolution_version": EFFECTIVE_FAMILY_RESOLUTION_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "canonical_execution_line": _canonical_execution_line(effective_stack),
        "prior_current_family": _prior_family_reference(stack),
        "selected_adoption_result": _selected_adoption_summary(
            selected_adoption,
            adoption_path,
            selection.get("input_references"),
        ),
        "effective_family": _effective_family_reference(effective_stack),
        "resolution_basis": {
            "basis": basis,
            "basis_reason": basis_reason,
        },
        "checks": checks,
        "outcome": outcome,
        "non_effective_preserved_families": _non_effective_families(
            stack,
            adopted_family,
            selected_adoption,
            outcome,
        ),
        "non_claims": dict(non_claims),
    }


def _load_current_stack() -> dict[str, Any]:
    authority_path = discover_latest_authority_resolution(EXECUTION_AUTHORITY_RESOLUTION_ROOT)
    family_path = discover_latest_run_family_packet(RUN_FAMILY_PACKET_ROOT)
    status_path = discover_latest_preserved_run_status_packet(PRESERVED_RUN_STATUS_PACKET_ROOT)
    governing_path = discover_latest_current_governing_packet(CURRENT_GOVERNING_PACKET_ROOT)
    authority = _read_json(authority_path, "authority resolution")
    family = _read_json(family_path, "run-family packet")
    status = _read_json(status_path, "preserved-run status packet")
    governing = _read_json(governing_path, "current-governing packet")
    return {
        "authority_path": authority_path,
        "family_path": family_path,
        "status_path": status_path,
        "governing_path": governing_path,
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
        "authority_summary": _authority_summary(authority),
        "family_summary": _family_summary(family),
        "status_summary": _status_summary(status),
        "governing_summary": _governing_summary(governing),
    }


def _verify_current_stack(stack: Mapping[str, Any]) -> None:
    authority = _obj(stack, "authority", "current stack")
    family = _obj(stack, "family", "current stack")
    status = _obj(stack, "status", "current stack")
    governing = _obj(stack, "governing", "current stack")
    authority_summary = _obj(stack, "authority_summary", "current stack")
    family_summary = _obj(stack, "family_summary", "current stack")
    status_summary = _obj(stack, "status_summary", "current stack")
    governing_summary = _obj(stack, "governing_summary", "current stack")
    decision = _obj(authority, "authority_decision", "authority resolution")

    if _str(decision, "decision", "authority decision") != DECISION_RESOLVED:
        raise EffectiveFamilyResolutionError("Effective-family resolution requires resolved current authority")
    if len({_core(authority, "authority"), _core(family, "family"), _core(status, "status"), _core(governing, "governing")}) != 1:
        raise EffectiveFamilyResolutionError("Canonical core execution file does not match across current family")

    _require_same_paths(
        (
            authority_summary.get("selected_source_run_directory_path"),
            family_summary.get("current_authority_source_run_path"),
            status_summary.get("selected_current_authority_source_run_path"),
            governing_summary.get("current_governing_source_run_path"),
        ),
        "current governing source run path",
    )
    _require_same_paths(
        (
            authority_summary.get("selected_ingress_run_directory_path"),
            family_summary.get("current_authority_ingress_run_path"),
            governing_summary.get("current_governing_ingress_run_path"),
        ),
        "current governing ingress run path",
    )
    governing_ref = _obj(governing, "authority_reference", "current-governing packet")
    _require_same_paths(
        (
            authority_summary.get("selected_comparison_artifact_path"),
            governing_ref.get("selected_comparison_artifact_path"),
        ),
        "current governing comparison artifact path",
    )
    if status_summary.get("current_authority_run_count") != 1:
        raise EffectiveFamilyResolutionError("Current status packet must name exactly one current authority")


def _select_default_adoption_result(root: Path) -> dict[str, Any]:
    root_path = _repo_path(root)
    if not root_path.exists():
        return _adoption_selection_none(root_path, "No successor-adoption root exists.", 0, 0)
    if not root_path.is_dir():
        raise EffectiveFamilyResolutionError(
            f"Successor-adoption root is not a directory: {_display(root_path)}"
        )

    candidates = sorted(
        path
        for path in root_path.rglob("*.json")
        if path.is_file() and "adoption" in path.name and "result" in path.name
    )
    if not candidates:
        return _adoption_selection_none(root_path, "No successor-adoption artifacts are available.", 0, 0)

    adopted: list[tuple[Path, dict[str, Any]]] = []
    blocked_count = 0
    for path in candidates:
        result = _read_adoption_result(path)
        outcome = _str(result, "outcome", "successor-adoption result")
        if outcome == OUTCOME_ADOPTED:
            adopted.append((path, result))
        elif outcome == ADOPTION_BLOCKED:
            blocked_count += 1

    if not adopted:
        return _adoption_selection_none(
            root_path,
            "Only blocked or non-adopted successor-adoption results are available.",
            len(candidates),
            blocked_count,
        )

    selected = adopted[-1][0]
    return {
        "selected_adoption_result_path": selected,
        "actual": {
            "adoption_result_artifact_count": len(candidates),
            "blocked_adoption_result_count": blocked_count,
            "adopted_successor_result_count": len(adopted),
            "selected_adoption_result_artifact_path": _display(selected),
        },
        "input_references": {
            "successor_adoption_root_path": _display(root_path),
            "adopted_successor_adoption_artifact_paths": [
                _display(path) for path, _ in adopted
            ],
        },
    }


def _adoption_selection_none(
    root: Path,
    reason: str,
    artifact_count: int,
    blocked_count: int,
) -> dict[str, Any]:
    return {
        "selected_adoption_result_path": None,
        "actual": {
            "adoption_result_artifact_count": artifact_count,
            "blocked_adoption_result_count": blocked_count,
            "adopted_successor_result_count": 0,
            "reason": reason,
        },
        "input_references": {
            "successor_adoption_root_path": _display(root),
            "adopted_successor_adoption_artifact_paths": [],
        },
    }


def _load_adopted_family_from_adoption(adoption: Mapping[str, Any]) -> dict[str, Any]:
    refs = _obj(adoption, "adopted_family_references", "successor-adoption result")
    path_keys = (
        "adopted_authority_artifact_path",
        "adopted_family_packet_path",
        "adopted_status_packet_path",
        "adopted_current_governing_packet_path",
    )
    paths: dict[str, Path] = {}
    for key in path_keys:
        paths[key] = _repo_path(Path(_str(refs, key, "successor-adoption adopted family references")))

    authority = _read_json(paths["adopted_authority_artifact_path"], "adopted authority artifact")
    family = _read_json(paths["adopted_family_packet_path"], "adopted run-family packet")
    status = _read_json(paths["adopted_status_packet_path"], "adopted status packet")
    governing = _read_json(paths["adopted_current_governing_packet_path"], "adopted current-governing packet")
    return {
        "authority_path": paths["adopted_authority_artifact_path"],
        "family_path": paths["adopted_family_packet_path"],
        "status_path": paths["adopted_status_packet_path"],
        "governing_path": paths["adopted_current_governing_packet_path"],
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
        "authority_summary": _authority_summary(authority),
        "family_summary": _family_summary(family),
        "status_summary": _status_summary(status),
        "governing_summary": _governing_summary(governing),
    }


def _adopted_family_checks(
    stack: Mapping[str, Any],
    adoption: Mapping[str, Any],
    adoption_path: Path | None,
    adopted: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    current_family = _obj(stack, "family", "current stack")
    adopted_family = _obj(adopted, "family", "adopted family")
    current_summary = _obj(stack, "governing_summary", "current stack")
    adopted_summary = _obj(adopted, "governing_summary", "adopted family")
    adoption_summary = _adoption_summary(adoption)
    adopted_refs = _obj(adoption, "adopted_family_references", "successor-adoption result")

    adoption_refs_match = all(
        _same(_path_value(adopted, stack_key), adopted_refs.get(result_key))
        for stack_key, result_key in (
            ("authority_path", "adopted_authority_artifact_path"),
            ("family_path", "adopted_family_packet_path"),
            ("status_path", "adopted_status_packet_path"),
            ("governing_path", "adopted_current_governing_packet_path"),
        )
    )
    selected_successor_refs_match = _selected_successor_family_matches_adopted_refs(
        adoption
    )
    prior_refs_match = _prior_family_matches_adoption(stack, adoption)
    current_core = _core(current_family, "current family")
    adopted_core = _core(adopted_family, "adopted family")
    adopted_coherent = _family_selected_paths_align(adopted)
    prior_source = current_summary.get("current_governing_source_run_path")
    effective_source = adopted_summary.get("current_governing_source_run_path")
    prior_entry = _find_by_source(
        _list(_obj(adopted, "status", "adopted family"), "preserved_run_status_entries", "adopted status"),
        prior_source,
        "source_run_directory_path",
    )

    return [
        _check(
            "selected_adoption_result_exists_and_readable",
            "readable successor-adoption result",
            _display(adoption_path) if adoption_path is not None else "provided mapping",
            True,
        ),
        _check(
            "selected_adoption_result_is_adopted",
            OUTCOME_ADOPTED,
            adoption.get("outcome"),
            adoption.get("outcome") == OUTCOME_ADOPTED,
        ),
        _check(
            "adoption_result_references_match_adopted_family",
            "adopted family paths match adoption result references",
            {
                "adopted_family_references": _json_ready(adopted_refs),
                "selected_successor_family_matches": selected_successor_refs_match,
            },
            adoption_refs_match and selected_successor_refs_match,
        ),
        _check(
            "adoption_result_corresponds_to_prior_current_family",
            "prior current family paths match adoption result",
            _prior_family_reference(stack),
            prior_refs_match,
        ),
        _check(
            "current_and_adopted_canonical_core_match",
            current_core,
            adopted_core,
            _same(current_core, adopted_core),
        ),
        _check(
            "adopted_family_internally_coherent",
            "adopted authority, family, status, and governing selections align",
            _adopted_family_actual(adopted),
            adopted_coherent,
        ),
        _check(
            "adoption_summary_matches_adopted_family",
            "adoption summary new governing path matches adopted governing",
            {
                "adoption_summary_new_source": adoption_summary.get(
                    "new_governing_source_run_path"
                ),
                "adopted_governing_source": effective_source,
            },
            _same(adoption_summary.get("new_governing_source_run_path"), effective_source),
        ),
        _check(
            "adopted_family_differs_from_prior_current_family",
            "adopted family current governing source differs from prior current source",
            {"prior_source": prior_source, "effective_source": effective_source},
            isinstance(effective_source, str) and not _same(prior_source, effective_source),
        ),
        _check(
            "adopted_family_preserves_prior_governing_as_non_authority",
            "prior governing source remains visible and is not current authority",
            prior_entry,
            prior_entry is not None
            and prior_entry.get("current_authority") is False
            and prior_entry.get("status_role") != "CURRENT_EXECUTION_AUTHORITY",
        ),
        _check(
            "prior_current_family_remains_readable",
            "prior current family artifacts remain readable and unchanged",
            _prior_family_reference(stack),
            all(_path_value(stack, key).is_file() for key in ("authority_path", "family_path", "status_path", "governing_path")),
        ),
        _check(
            "adopted_family_non_claims_remain_false",
            "all effective non-claims remain false",
            non_claims,
            _all_non_claims_false(non_claims),
        ),
        _check(
            "effective_family_not_inferred_from_successor_existence_alone",
            "effective family is selected through explicit ADOPTED result",
            _selected_adoption_identity(adoption, adoption_path),
            adoption.get("outcome") == OUTCOME_ADOPTED and adoption_refs_match,
        ),
    ]


def _effective_family_resolution_id(
    adoption: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    if adoption is None or outcome == OUTCOME_CURRENT_FAMILY_EFFECTIVE:
        return "current_family_remains_effective"
    metadata = _obj(adoption, "adoption_metadata", "successor-adoption result")
    return f"{_str(metadata, 'adoption_result_id', 'successor-adoption metadata')}__effective_family"


def _canonical_execution_line(stack: Mapping[str, Any]) -> dict[str, Any]:
    canonical = _obj(_obj(stack, "family", "family stack"), "canonical_execution_line", "run-family packet")
    return {
        "core_execution_file": _str(
            canonical,
            "core_execution_file",
            "run-family packet.canonical_execution_line",
        ),
        "derivative_support_scope": [
            _as_string(value, "derivative support scope")
            for value in _list(canonical, "derivative_support_scope", "run-family packet.canonical_execution_line")
        ],
        "lineage_predecessor_files": [
            _as_string(value, "lineage predecessor file")
            for value in _list(canonical, "lineage_predecessor_files", "run-family packet.canonical_execution_line")
        ],
    }


def _prior_family_reference(stack: Mapping[str, Any]) -> dict[str, str]:
    return {
        "prior_authority_artifact_path": _display(_path_value(stack, "authority_path")),
        "prior_family_packet_path": _display(_path_value(stack, "family_path")),
        "prior_status_packet_path": _display(_path_value(stack, "status_path")),
        "prior_current_governing_packet_path": _display(_path_value(stack, "governing_path")),
    }


def _selected_adoption_summary(
    adoption: Mapping[str, Any] | None,
    adoption_path: Path | None,
    extra_refs: Any,
) -> dict[str, Any] | None:
    if adoption is None:
        return None
    metadata = _obj(adoption, "adoption_metadata", "successor-adoption result")
    summary = {
        "adoption_result_artifact_path": _display(adoption_path) if adoption_path is not None else None,
        "adoption_result_id": metadata.get("adoption_result_id"),
        "outcome": adoption.get("outcome"),
        "adopted_family_references": dict(
            _obj(adoption, "adopted_family_references", "successor-adoption result")
        ),
    }
    if extra_refs is not None:
        summary["selection_references"] = _json_ready(extra_refs)
    return summary


def _effective_family_reference(stack: Mapping[str, Any]) -> dict[str, Any]:
    governing_summary = _obj(stack, "governing_summary", "family stack")
    return {
        "effective_authority_artifact_path": _display(_path_value(stack, "authority_path")),
        "effective_family_packet_path": _display(_path_value(stack, "family_path")),
        "effective_status_packet_path": _display(_path_value(stack, "status_path")),
        "effective_current_governing_packet_path": _display(_path_value(stack, "governing_path")),
        "effective_source_run_path": governing_summary.get("current_governing_source_run_path"),
        "effective_ingress_run_path": governing_summary.get("current_governing_ingress_run_path"),
    }


def _non_effective_families(
    stack: Mapping[str, Any],
    adopted_family: Mapping[str, Any] | None,
    adoption: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    governing = _obj(stack, "governing", "current stack")
    if outcome == OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE and adopted_family is not None:
        return {
            "prior_current_family": _prior_family_reference(stack),
            "prior_current_family_remains_preserved": True,
            "preserved_non_governing_runs_remain_preserved": True,
            "prior_current_governing_run_remains_visible": dict(
                _obj(governing, "current_governing_run", "current-governing packet")
            ),
        }
    return {
        "prior_current_family_is_effective": True,
        "adopted_successor_family_not_effective": (
            _selected_adoption_summary(adoption, None, None) if adoption is not None else None
        ),
        "preserved_non_governing_runs_remain_preserved": True,
        "preserved_non_governing_runs": _json_ready(
            _list(governing, "preserved_non_governing_runs", "current-governing packet")
        ),
    }


def _validate_adoption_result(payload: dict[str, Any]) -> dict[str, Any]:
    for key in (
        "adoption_metadata",
        "prior_current_family",
        "selected_reresolution_result",
        "selected_successor_family",
        "checks",
        "outcome",
        "block",
        "adopted_family_references",
        "adoption_summary",
        "non_claims",
    ):
        if key == "checks":
            _list(payload, key, "successor-adoption result")
        elif key == "outcome":
            _str(payload, key, "successor-adoption result")
        else:
            _obj(payload, key, "successor-adoption result")

    outcome = _str(payload, "outcome", "successor-adoption result")
    if outcome not in {OUTCOME_ADOPTED, ADOPTION_BLOCKED}:
        raise EffectiveFamilyResolutionError("Successor-adoption result outcome is not recognized")
    _str(_obj(payload, "adoption_metadata", "successor-adoption result"), "adoption_result_id", "adoption metadata")
    if outcome == OUTCOME_ADOPTED:
        refs = _obj(payload, "adopted_family_references", "successor-adoption result")
        for key in (
            "adopted_authority_artifact_path",
            "adopted_family_packet_path",
            "adopted_status_packet_path",
            "adopted_current_governing_packet_path",
        ):
            _str(refs, key, "successor-adoption result.adopted_family_references")
    return payload


def _read_adoption_result(path: Path) -> dict[str, Any]:
    return _validate_adoption_result(_read_json(path, "successor-adoption result"))


def _read_json(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_path(path)
    try:
        value = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EffectiveFamilyResolutionError(
            f"{label.title()} file does not exist: {_display(file_path)}"
        ) from exc
    except OSError as exc:
        raise EffectiveFamilyResolutionError(f"Could not read {label}: {_display(file_path)}") from exc
    except json.JSONDecodeError as exc:
        raise EffectiveFamilyResolutionError(
            f"{label.title()} is not valid JSON: {_display(file_path)}"
        ) from exc
    if not isinstance(value, dict):
        raise EffectiveFamilyResolutionError(
            f"{label.title()} JSON must be an object: {_display(file_path)}"
        )
    return value


def _latest_required(root: Path, pattern: str, label: str) -> Path:
    root_path = _require_dir(root, label)
    artifacts = sorted(path for path in root_path.glob(pattern) if path.is_file())
    if not artifacts:
        raise EffectiveFamilyResolutionError(
            f"No artifact matching {pattern} found under {_display(root_path)}"
        )
    return artifacts[-1]


def _require_dir(root: Path, label: str) -> Path:
    root_path = _repo_path(root)
    if not root_path.exists():
        raise EffectiveFamilyResolutionError(f"{label.title()} does not exist: {_display(root_path)}")
    if not root_path.is_dir():
        raise EffectiveFamilyResolutionError(f"{label.title()} is not a directory: {_display(root_path)}")
    return root_path


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise EffectiveFamilyResolutionError("Authority artifact is malformed") from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise EffectiveFamilyResolutionError("Run-family packet is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except PreservedRunStatusPacketError as exc:
        raise EffectiveFamilyResolutionError("Preserved-run status packet is malformed") from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except CurrentGoverningPacketError as exc:
        raise EffectiveFamilyResolutionError("Current-governing packet is malformed") from exc


def _adoption_summary(adoption: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_governing_successor_adoption_summary(adoption)
    except GoverningSuccessorAdoptionError as exc:
        raise EffectiveFamilyResolutionError("Successor-adoption result is malformed") from exc


def _stack_non_claims(stack: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for stack_key in ("authority", "family", "status", "governing"):
        artifact = _obj(stack, stack_key, "current stack")
        incoming = _obj(artifact, "non_claims", f"current {stack_key} artifact")
        _merge_non_claims(non_claims, incoming, f"current {stack_key} artifact")
    return non_claims


def _combined_non_claims(
    base_non_claims: Mapping[str, bool],
    adoption: Mapping[str, Any],
    adopted_family: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    _merge_non_claims(non_claims, base_non_claims, "current family")
    _merge_non_claims(
        non_claims,
        _obj(adoption, "non_claims", "successor-adoption result"),
        "successor-adoption result",
    )
    for stack_key in ("authority", "family", "status", "governing"):
        artifact = _obj(adopted_family, stack_key, "adopted family")
        _merge_non_claims(
            non_claims,
            _obj(artifact, "non_claims", f"adopted {stack_key} artifact"),
            f"adopted {stack_key} artifact",
        )
    return non_claims


def _merge_non_claims(target: dict[str, bool], incoming: Mapping[str, Any], context: str) -> None:
    for key in NON_CLAIM_DEFAULTS:
        if key in incoming:
            value = _bool(incoming, key, f"{context}.non_claims")
            if value is not False:
                raise EffectiveFamilyResolutionError(f"{context}.non_claims.{key} must remain false")
            target[key] = False


def _all_non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in NON_CLAIM_DEFAULTS)


def _prior_family_matches_adoption(stack: Mapping[str, Any], adoption: Mapping[str, Any]) -> bool:
    prior = _obj(adoption, "prior_current_family", "successor-adoption result")
    return all(
        _same(_path_value(stack, stack_key), prior.get(prior_key))
        for stack_key, prior_key in (
            ("authority_path", "prior_authority_artifact_path"),
            ("family_path", "prior_family_packet_path"),
            ("status_path", "prior_status_packet_path"),
            ("governing_path", "prior_current_governing_packet_path"),
        )
    )


def _selected_successor_family_matches_adopted_refs(adoption: Mapping[str, Any]) -> bool:
    selected = _obj(adoption, "selected_successor_family", "successor-adoption result")
    adopted = _obj(adoption, "adopted_family_references", "successor-adoption result")
    return (
        _same(selected.get("successor_authority_artifact_path"), adopted.get("adopted_authority_artifact_path"))
        and _same(selected.get("successor_family_packet_path"), adopted.get("adopted_family_packet_path"))
        and _same(selected.get("successor_status_packet_path"), adopted.get("adopted_status_packet_path"))
        and _same(selected.get("successor_current_governing_packet_path"), adopted.get("adopted_current_governing_packet_path"))
    )


def _family_selected_paths_align(stack: Mapping[str, Any]) -> bool:
    authority = _obj(stack, "authority_summary", "family stack")
    family = _obj(stack, "family_summary", "family stack")
    status = _obj(stack, "status_summary", "family stack")
    governing = _obj(stack, "governing_summary", "family stack")
    governing_ref = _obj(_obj(stack, "governing", "family stack"), "authority_reference", "current-governing packet")
    return (
        _same(authority.get("selected_source_run_directory_path"), family.get("current_authority_source_run_path"))
        and _same(authority.get("selected_source_run_directory_path"), status.get("selected_current_authority_source_run_path"))
        and _same(authority.get("selected_source_run_directory_path"), governing.get("current_governing_source_run_path"))
        and _same(authority.get("selected_ingress_run_directory_path"), family.get("current_authority_ingress_run_path"))
        and _same(authority.get("selected_ingress_run_directory_path"), governing.get("current_governing_ingress_run_path"))
        and _same(authority.get("selected_comparison_artifact_path"), governing_ref.get("selected_comparison_artifact_path"))
        and status.get("current_authority_run_count") == 1
        and status.get("preserved_run_count") == family.get("preserved_run_count")
    )


def _current_core_set(stack: Mapping[str, Any]) -> set[str]:
    return {
        _core(_obj(stack, "authority", "current stack"), "authority"),
        _core(_obj(stack, "family", "current stack"), "family"),
        _core(_obj(stack, "status", "current stack"), "status"),
        _core(_obj(stack, "governing", "current stack"), "governing"),
    }


def _adopted_family_actual(stack: Mapping[str, Any]) -> dict[str, Any]:
    authority = _obj(stack, "authority_summary", "adopted family")
    family = _obj(stack, "family_summary", "adopted family")
    status = _obj(stack, "status_summary", "adopted family")
    governing = _obj(stack, "governing_summary", "adopted family")
    return {
        "authority_source": authority.get("selected_source_run_directory_path"),
        "family_source": family.get("current_authority_source_run_path"),
        "status_source": status.get("selected_current_authority_source_run_path"),
        "governing_source": governing.get("current_governing_source_run_path"),
        "current_authority_run_count": status.get("current_authority_run_count"),
        "preserved_run_count": status.get("preserved_run_count"),
    }


def _find_by_source(
    entries: list[Any],
    source_path: Any,
    source_key: str,
) -> Mapping[str, Any] | None:
    if not isinstance(source_path, (str, Path)):
        return None
    for value in entries:
        if not isinstance(value, Mapping):
            continue
        candidate = value.get(source_key)
        if isinstance(candidate, str) and _same(candidate, source_path):
            return value
    return None


def _selected_adoption_identity(
    adoption: Mapping[str, Any],
    adoption_path: Path | None,
) -> dict[str, Any]:
    metadata = _obj(adoption, "adoption_metadata", "successor-adoption result")
    return {
        "adoption_result_artifact_path": _display(adoption_path) if adoption_path is not None else None,
        "adoption_result_id": metadata.get("adoption_result_id"),
        "outcome": adoption.get("outcome"),
    }


def _check(name: str, required: Any, actual: Any, passed: bool) -> dict[str, Any]:
    return {
        "check": name,
        "required": _json_ready(required),
        "actual": _json_ready(actual),
        "passed": bool(passed),
    }


def _path_value(mapping: Mapping[str, Any], key: str) -> Path:
    value = mapping.get(key)
    if not isinstance(value, Path):
        raise EffectiveFamilyResolutionError(f"{key} must be a Path")
    return value


def _require_same_paths(values: tuple[Any, ...], label: str) -> None:
    present = [value for value in values if value is not None]
    if not present:
        raise EffectiveFamilyResolutionError(f"Missing {label}")
    first = present[0]
    if any(not _same(first, value) for value in present[1:]):
        raise EffectiveFamilyResolutionError(f"Artifact mismatch for {label}")


def _core(packet: Mapping[str, Any], label: str) -> str:
    return _str(_obj(packet, "canonical_execution_line", label), "core_execution_file", f"{label}.canonical_execution_line")


def _same(left: Any, right: Any) -> bool:
    if not isinstance(left, (str, Path)) or not isinstance(right, (str, Path)):
        return False
    return _resolve_path(str(left)) == _resolve_path(str(right))


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path.resolve() if path.is_absolute() else (_repo_root() / path).resolve()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path) -> Path:
    return path.resolve() if path.is_absolute() else (_repo_root() / path).resolve()


def _display(path: Path) -> str:
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
        return _display(value)
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    return str(value)


def _obj(mapping: Mapping[str, Any], key: str, context: str) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise EffectiveFamilyResolutionError(f"{context}.{key} must be an object")
    return value


def _list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise EffectiveFamilyResolutionError(f"{context}.{key} must be a list")
    return value


def _str(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise EffectiveFamilyResolutionError(f"{context}.{key} must be a non-empty string")
    return value


def _bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise EffectiveFamilyResolutionError(f"{context}.{key} must be a boolean")
    return value


def _as_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value:
        raise EffectiveFamilyResolutionError(f"{context} must be a non-empty string")
    return value
