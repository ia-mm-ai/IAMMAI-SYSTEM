"""Resolve bounded successor-family adoption for v0-min coexistence.

This module reads the current authority, run-family, preserved-run status,
current-governing, governing re-resolution result, and successor family
artifacts. It emits one bounded adoption result when a coherent successor
family may be adopted for subsequent bounded work. It emits a blocked adoption
result when the bounded checks do not pass.

The resolver is additive engineering. It does not replay source actions into a
live host, merge preserved runs, mutate prior artifacts, complete continuity,
upgrade standing, define persistence or registry law, or treat successor
projection emission as self-executing currentness.
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
    ROLE_CURRENT_AUTHORITY,
    ROLE_ELIGIBLE_NON_AUTHORITY,
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
from resolve_integrity_host_v0_min_coexistence_governing_reresolution import (
    OUTCOME_BLOCKED as RERESOLUTION_BLOCKED,
    OUTCOME_SUCCESSOR_EMITTED,
    GoverningReresolutionError,
    build_governing_reresolution_summary,
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
GOVERNING_RERESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_governing_reresolutions"
)
GOVERNING_SUCCESSOR_ADOPTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_governing_successor_adoptions"
)

ADOPTION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_GOVERNING_SUCCESSOR_ADOPTION_RESULT"
)
ADOPTION_RESULT_VERSION = "0.1.0"
OUTCOME_ADOPTED = "ADOPTED"
OUTCOME_BLOCKED = "BLOCKED"

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
}

BLOCK_REASONS = {
    "NO_SUCCESSOR_PROJECTION_AVAILABLE": "No successor projection is available for adoption.",
    "SUCCESSOR_RESULT_UNREADABLE": "Selected governing re-resolution result is unreadable.",
    "SUCCESSOR_RESULT_NOT_EMITTED": "Selected governing re-resolution result did not emit a successor projection.",
    "SUCCESSOR_FAMILY_UNREADABLE": "One or more successor family artifacts are unreadable.",
    "SUCCESSOR_FAMILY_DOES_NOT_CORRESPOND_TO_CURRENT_FAMILY": "Successor family does not correspond to the current family.",
    "CANONICAL_EXECUTION_LINE_MISMATCH": "Canonical execution line does not match across current and successor families.",
    "SUCCESSOR_FAMILY_NOT_INTERNALLY_COHERENT": "Successor family is not internally coherent.",
    "PRIOR_CURRENT_FAMILY_UNREADABLE": "Prior current family is unreadable.",
    "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT": "Prior family preservation is not evident.",
    "SUCCESSOR_FAMILY_DOES_NOT_PRESERVE_PRIOR_GOVERNING_AS_NON_AUTHORITY": "Successor family does not preserve the prior governing run as non-authority.",
    "SUCCESSOR_FAMILY_DOES_NOT_NAME_ONE_NEW_CURRENT_GOVERNING_RUN": "Successor family does not name exactly one new current governing run.",
    "REPLAY_SHORTCUT_REFUSED": "Replay shortcut is refused during successor-family adoption.",
    "MERGE_SHORTCUT_REFUSED": "Merge shortcut is refused during successor-family adoption.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Adoption may not complete continuity.",
    "SILENT_STANDING_UPGRADE_REFUSED": "Adoption may not silently upgrade standing.",
    "MULTIPLE_SUCCESSOR_FAMILIES_CONFLICT_UNRESOLVED": "Multiple successor families conflict without bounded selection.",
}


class GoverningSuccessorAdoptionError(RuntimeError):
    """Raised when bounded successor-family adoption cannot proceed."""


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


def discover_latest_successor_projection_result(root: Path) -> Path:
    """Return the lexically latest unambiguous successor-projection result."""

    selection = _select_default_reresolution_result(root)
    if selection["block_code"] is not None:
        raise GoverningSuccessorAdoptionError(str(selection["block_reason"]))
    selected = selection["selected_reresolution_result_path"]
    if not isinstance(selected, Path):
        raise GoverningSuccessorAdoptionError("No successor-projection result found")
    return selected


def resolve_governing_successor_adoption(
    reresolution_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded successor-family adoption."""

    stack = _load_current_stack()
    _verify_current_stack(stack)
    base_non_claims = _stack_non_claims(stack)

    if reresolution_result is None:
        selection = _select_default_reresolution_result(GOVERNING_RERESOLUTION_ROOT)
        if selection["block_code"] is not None:
            result = _adoption_result(
                stack=stack,
                reresolution=None,
                reresolution_path=None,
                successor=None,
                checks=[
                    _check(
                        "successor_projection_available",
                        "one readable SUCCESSOR_PROJECTION_EMITTED re-resolution result",
                        selection["actual"],
                        False,
                        str(selection["block_code"]),
                    )
                ],
                outcome=OUTCOME_BLOCKED,
                block_code=str(selection["block_code"]),
                block_reason=str(selection["block_reason"]),
                non_claims=base_non_claims,
                extra_refs=selection.get("input_references"),
            )
            _write_default_adoption_result(result)
            return result
        selected_path = _selection_path(selection)
        reresolution = _read_reresolution_result(selected_path)
        return _resolve_selected(
            stack,
            reresolution,
            selected_path,
            base_non_claims,
            selection.get("input_references"),
        )

    if not isinstance(reresolution_result, Mapping):
        raise GoverningSuccessorAdoptionError("Re-resolution result must be a mapping or None")
    reresolution = _validate_reresolution_result(dict(reresolution_result))
    return _resolve_selected(stack, reresolution, None, base_non_claims, None)


def resolve_governing_successor_adoption_from_path(path: Path | str) -> dict[str, Any]:
    """Read one re-resolution result artifact and resolve adoption from it."""

    result_path = _repo_path(Path(path))
    reresolution = _read_reresolution_result(result_path)
    stack = _load_current_stack()
    _verify_current_stack(stack)
    return _resolve_selected(stack, reresolution, result_path, _stack_non_claims(stack), None)


def write_governing_successor_adoption_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 successor-family adoption result."""

    if not isinstance(result, Mapping):
        raise GoverningSuccessorAdoptionError("Successor adoption result must be a mapping")
    target = _default_result_path(result) if output_path is None else _repo_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise GoverningSuccessorAdoptionError(
            f"Refusing to overwrite successor-adoption result: {_display(target)}"
        )
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_governing_successor_adoption_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one adoption result."""

    metadata = _obj(result, "adoption_metadata", "successor-adoption result")
    block = _obj(result, "block", "successor-adoption result")
    checks = _list(result, "checks", "successor-adoption result")
    selected = _obj(result, "selected_reresolution_result", "successor-adoption result")
    summary = _obj(result, "adoption_summary", "successor-adoption result")
    non_claims = _obj(result, "non_claims", "successor-adoption result")
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed = len(checks) - passed
    return {
        "adoption_result_id": _str(metadata, "adoption_result_id", "successor-adoption metadata"),
        "outcome": _str(result, "outcome", "successor-adoption result"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_reresolution_result_id": selected.get("reresolution_id"),
        "prior_governing_source_run_path": summary.get("prior_governing_source_run_path"),
        "new_governing_source_run_path": summary.get("new_governing_source_run_path"),
        "adopted_family_references": dict(_obj(result, "adopted_family_references", "successor-adoption result")),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": {key: _bool(non_claims, key, "successor-adoption non_claims") for key in NON_CLAIM_DEFAULTS},
    }


def _resolve_selected(
    stack: Mapping[str, Any],
    reresolution: Mapping[str, Any],
    reresolution_path: Path | None,
    base_non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    successor = _load_successor_family_from_reresolution(reresolution)
    non_claims = _combined_non_claims(base_non_claims, reresolution, successor)
    checks = _adoption_checks(stack, reresolution, reresolution_path, successor, non_claims)
    block = _first_block(checks)
    outcome = OUTCOME_BLOCKED if block is not None else OUTCOME_ADOPTED
    result = _adoption_result(
        stack=stack,
        reresolution=reresolution,
        reresolution_path=reresolution_path,
        successor=successor,
        checks=checks,
        outcome=outcome,
        block_code=block["block_code"] if block else None,
        block_reason=block["block_reason"] if block else None,
        non_claims=non_claims,
        extra_refs=extra_refs,
    )
    _write_default_adoption_result(result)
    return result


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
        raise GoverningSuccessorAdoptionError("Current authority must be resolved before adoption")
    if len({_core(authority, "authority"), _core(family, "family"), _core(status, "status"), _core(governing, "governing")}) != 1:
        raise GoverningSuccessorAdoptionError("Canonical core execution file does not match across current family")

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
        raise GoverningSuccessorAdoptionError("Current status packet must name exactly one current authority")
    current = _obj(governing, "current_governing_run", "current-governing packet")
    if _str(current, "status_role", "current-governing packet.current_governing_run") != ROLE_CURRENT_AUTHORITY:
        raise GoverningSuccessorAdoptionError("Current-governing packet lacks current authority role")


def _select_default_reresolution_result(root: Path) -> dict[str, Any]:
    root_path = _repo_path(root)
    if not root_path.exists():
        return _selection_block("NO_SUCCESSOR_PROJECTION_AVAILABLE", "No governing re-resolution root exists.", root_path, [])
    if not root_path.is_dir():
        raise GoverningSuccessorAdoptionError(f"Governing re-resolution root is not a directory: {_display(root_path)}")

    candidates = sorted(
        path
        for path in root_path.rglob("*.json")
        if path.is_file() and "reresolution" in path.name and "result" in path.name
    )
    if not candidates:
        return _selection_block("NO_SUCCESSOR_PROJECTION_AVAILABLE", "No governing re-resolution result artifacts are available.", root_path, [])

    emitted: list[tuple[Path, dict[str, Any]]] = []
    blocked_count = 0
    for path in candidates:
        result = _read_reresolution_result(path)
        outcome = _str(result, "outcome", "governing re-resolution result")
        if outcome == OUTCOME_SUCCESSOR_EMITTED:
            emitted.append((path, result))
        elif outcome == RERESOLUTION_BLOCKED:
            blocked_count += 1

    if not emitted:
        block = _selection_block(
            "NO_SUCCESSOR_PROJECTION_AVAILABLE",
            "Only blocked or non-emitted re-resolution results are available.",
            root_path,
            [],
        )
        block["actual"] = {
            "reresolution_result_artifact_count": len(candidates),
            "blocked_reresolution_result_count": blocked_count,
            "successor_projection_count": 0,
        }
        return block

    identities = {_reresolution_identity(result) for _, result in emitted}
    emitted_paths = [_display(path) for path, _ in emitted]
    if len(identities) > 1:
        block = _selection_block(
            "MULTIPLE_SUCCESSOR_FAMILIES_CONFLICT_UNRESOLVED",
            "Multiple successor families conflict without bounded selection.",
            root_path,
            emitted_paths,
        )
        block["actual"] = {
            "successor_projection_count": len(emitted),
            "successor_projection_artifact_paths": emitted_paths,
        }
        return block

    selected = emitted[-1][0]
    return {
        "selected_reresolution_result_path": selected,
        "block_code": None,
        "block_reason": None,
        "actual": {
            "successor_projection_count": len(emitted),
            "selected_reresolution_result_artifact_path": _display(selected),
        },
        "input_references": {
            "reresolution_root_path": _display(root_path),
            "successor_projection_artifact_paths": emitted_paths,
        },
    }


def _selection_block(code: str, reason: str, root: Path, emitted_paths: list[str]) -> dict[str, Any]:
    return {
        "selected_reresolution_result_path": None,
        "block_code": code,
        "block_reason": reason,
        "actual": {"successor_projection_count": len(emitted_paths)},
        "input_references": {
            "reresolution_root_path": _display(root),
            "successor_projection_artifact_paths": emitted_paths,
        },
    }


def _load_successor_family_from_reresolution(reresolution: Mapping[str, Any]) -> dict[str, Any] | None:
    artifacts = _obj(reresolution, "successor_artifacts", "governing re-resolution result")
    path_keys = (
        "successor_authority_artifact_path",
        "successor_family_packet_path",
        "successor_status_packet_path",
        "successor_governing_packet_path",
    )
    paths: dict[str, Path] = {}
    for key in path_keys:
        value = artifacts.get(key)
        if not isinstance(value, str) or not value:
            return None
        paths[key] = _repo_path(Path(value))
    if not all(path.is_file() for path in paths.values()):
        return None

    authority = _read_json(paths["successor_authority_artifact_path"], "successor authority artifact")
    family = _read_json(paths["successor_family_packet_path"], "successor family packet")
    status = _read_json(paths["successor_status_packet_path"], "successor status packet")
    governing = _read_json(paths["successor_governing_packet_path"], "successor current-governing packet")
    return {
        "authority_path": paths["successor_authority_artifact_path"],
        "family_path": paths["successor_family_packet_path"],
        "status_path": paths["successor_status_packet_path"],
        "governing_path": paths["successor_governing_packet_path"],
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
        "authority_summary": _authority_summary(authority),
        "family_summary": _family_summary(family),
        "status_summary": _status_summary(status),
        "governing_summary": _governing_summary(governing),
    }


def _adoption_checks(
    stack: Mapping[str, Any],
    reresolution: Mapping[str, Any],
    reresolution_path: Path | None,
    successor: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    if successor is None:
        return [
            _check("successor_family_readable", "all successor artifacts readable", None, False, "SUCCESSOR_FAMILY_UNREADABLE")
        ]

    current_authority = _obj(stack, "authority", "current stack")
    current_family = _obj(stack, "family", "current stack")
    current_status = _obj(stack, "status", "current stack")
    current_governing = _obj(stack, "governing", "current stack")
    successor_authority = _obj(successor, "authority", "successor family")
    successor_family = _obj(successor, "family", "successor family")
    successor_status = _obj(successor, "status", "successor family")
    successor_governing = _obj(successor, "governing", "successor family")
    current_summary = _obj(stack, "governing_summary", "current stack")
    successor_auth_summary = _obj(successor, "authority_summary", "successor family")
    successor_family_summary = _obj(successor, "family_summary", "successor family")
    successor_status_summary = _obj(successor, "status_summary", "successor family")
    successor_governing_summary = _obj(successor, "governing_summary", "successor family")
    result_summary = _reresolution_summary(reresolution)
    result_successor_artifacts = _obj(reresolution, "successor_artifacts", "governing re-resolution result")
    projection = _obj(reresolution, "successor_projection_summary", "governing re-resolution result")

    prior_source = current_summary.get("current_governing_source_run_path")
    new_source = successor_governing_summary.get("current_governing_source_run_path")
    prior_status_entry = _find_by_source(
        _list(successor_status, "preserved_run_status_entries", "successor status"),
        str(prior_source),
        "source_run_directory_path",
    )
    successor_current = _obj(successor_governing, "current_governing_run", "successor governing")
    successor_gov_ref = _obj(successor_governing, "authority_reference", "successor governing")

    current_paths_match_result = _current_paths_match_reresolution(stack, reresolution)
    successor_paths_match = all(
        _same(_path_value(successor, successor_key), result_successor_artifacts.get(result_key))
        for successor_key, result_key in (
            ("authority_path", "successor_authority_artifact_path"),
            ("family_path", "successor_family_packet_path"),
            ("status_path", "successor_status_packet_path"),
            ("governing_path", "successor_governing_packet_path"),
        )
    )
    successor_cores_match = len(
        {
            _core(successor_authority, "successor authority"),
            _core(successor_family, "successor family"),
            _core(successor_status, "successor status"),
            _core(successor_governing, "successor governing"),
        }
    ) == 1
    current_cores_match = len(
        {
            _core(current_authority, "current authority"),
            _core(current_family, "current family"),
            _core(current_status, "current status"),
            _core(current_governing, "current governing"),
        }
    ) == 1
    successor_coherent = _successor_family_coherent(successor)

    return [
        _check("input_artifact_correspondence_holds", "current and successor artifacts correspond", current_paths_match_result and successor_paths_match, current_paths_match_result and successor_paths_match, "SUCCESSOR_FAMILY_DOES_NOT_CORRESPOND_TO_CURRENT_FAMILY"),
        _check("selected_reresolution_result_exists_and_readable", "readable re-resolution result", _display(reresolution_path) if reresolution_path else "provided mapping", True, "SUCCESSOR_RESULT_UNREADABLE"),
        _check("selected_reresolution_result_emitted_successor", OUTCOME_SUCCESSOR_EMITTED, reresolution.get("outcome"), reresolution.get("outcome") == OUTCOME_SUCCESSOR_EMITTED, "SUCCESSOR_RESULT_NOT_EMITTED"),
        _check("successor_authority_artifact_readable_and_coherent", "successor authority summary readable", successor_auth_summary, bool(successor_auth_summary), "SUCCESSOR_FAMILY_UNREADABLE"),
        _check("successor_family_packet_readable_and_coherent", "successor family summary readable", successor_family_summary, bool(successor_family_summary), "SUCCESSOR_FAMILY_UNREADABLE"),
        _check("successor_status_packet_readable_and_coherent", "successor status summary readable", successor_status_summary, bool(successor_status_summary), "SUCCESSOR_FAMILY_UNREADABLE"),
        _check("successor_governing_packet_readable_and_coherent", "successor governing summary readable", successor_governing_summary, bool(successor_governing_summary), "SUCCESSOR_FAMILY_UNREADABLE"),
        _check("canonical_core_execution_file_matches", _core(current_family, "current family"), _core(successor_family, "successor family"), current_cores_match and successor_cores_match and _same(_core(current_family, "current family"), _core(successor_family, "successor family")), "CANONICAL_EXECUTION_LINE_MISMATCH"),
        _check("successor_family_internally_coherent", "authority, family, status, governing successor selections align", successor_coherent, successor_coherent, "SUCCESSOR_FAMILY_NOT_INTERNALLY_COHERENT"),
        _check("successor_preserves_prior_governing_as_non_authority", ROLE_ELIGIBLE_NON_AUTHORITY, prior_status_entry.get("status_role") if prior_status_entry else None, prior_status_entry is not None and prior_status_entry.get("status_role") == ROLE_ELIGIBLE_NON_AUTHORITY and prior_status_entry.get("current_authority") is False, "SUCCESSOR_FAMILY_DOES_NOT_PRESERVE_PRIOR_GOVERNING_AS_NON_AUTHORITY"),
        _check("successor_names_one_new_current_governing_run", "one current authority different from prior governing", {"current_authority_run_count": successor_status_summary.get("current_authority_run_count"), "prior_source": prior_source, "new_source": new_source}, successor_status_summary.get("current_authority_run_count") == 1 and isinstance(new_source, str) and not _same(prior_source, new_source), "SUCCESSOR_FAMILY_DOES_NOT_NAME_ONE_NEW_CURRENT_GOVERNING_RUN"),
        _check("successor_governing_run_matches_successor_family", "successor authority/family/status/governing current paths align", {"authority_source": successor_auth_summary.get("selected_source_run_directory_path"), "family_source": successor_family_summary.get("current_authority_source_run_path"), "status_source": successor_status_summary.get("selected_current_authority_source_run_path"), "governing_source": new_source}, _successor_selected_paths_align(successor), "SUCCESSOR_FAMILY_NOT_INTERNALLY_COHERENT"),
        _check("preserved_run_multiplicity_remains_visible", "successor preserved-run counts align", {"family_count": len(_list(successor_family, "preserved_runs", "successor family")), "status_count": len(_list(successor_status, "preserved_run_status_entries", "successor status"))}, len(_list(successor_family, "preserved_runs", "successor family")) == len(_list(successor_status, "preserved_run_status_entries", "successor status")) and successor_status_summary.get("preserved_run_count", 0) >= 1, "SUCCESSOR_FAMILY_NOT_INTERNALLY_COHERENT"),
        _check("successor_non_claim_replay_false", False, non_claims["replayed_into_live_host"], non_claims["replayed_into_live_host"] is False, "REPLAY_SHORTCUT_REFUSED"),
        _check("successor_non_claim_merge_false", False, non_claims["merged_into_local_state"], non_claims["merged_into_local_state"] is False, "MERGE_SHORTCUT_REFUSED"),
        _check("successor_non_claim_continuity_false", False, non_claims["continuity_completed"], non_claims["continuity_completed"] is False, "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
        _check("successor_non_claim_standing_false", False, non_claims["standing_upgraded"], non_claims["standing_upgraded"] is False, "SILENT_STANDING_UPGRADE_REFUSED"),
        _check("prior_family_remains_preserved_after_adoption", "prior current artifacts remain readable and referenced", _prior_family_reference(stack), all(_path_value(stack, key).is_file() for key in ("authority_path", "family_path", "status_path", "governing_path")), "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT"),
        _check("adoption_result_is_explicit", "explicit adoption result with selected re-resolution", result_summary, True, "MULTIPLE_SUCCESSOR_FAMILIES_CONFLICT_UNRESOLVED"),
        _check("adoption_not_inferred_from_latest_ordering", "selected successor artifacts named by re-resolution result", {"successor_paths_match_reresolution": successor_paths_match}, successor_paths_match, "MULTIPLE_SUCCESSOR_FAMILIES_CONFLICT_UNRESOLVED"),
        _check("reresolution_projection_summary_matches_successor", "projection new governing path matches successor governing", {"projection_new_source": projection.get("new_governing_source_run_path"), "successor_governing_source": new_source}, _same(projection.get("new_governing_source_run_path"), new_source), "SUCCESSOR_FAMILY_DOES_NOT_CORRESPOND_TO_CURRENT_FAMILY"),
        _check("successor_current_governing_run_has_current_authority_role", ROLE_CURRENT_AUTHORITY, successor_current.get("status_role"), successor_current.get("status_role") == ROLE_CURRENT_AUTHORITY and successor_current.get("current_authority") is True and successor_current.get("candidate_eligible") is True, "SUCCESSOR_FAMILY_DOES_NOT_NAME_ONE_NEW_CURRENT_GOVERNING_RUN"),
        _check("successor_governing_scope_matches_authority_reference", "governing scope paths match authority reference", _obj(successor_governing, "governing_scope", "successor governing"), _successor_governing_scope_matches(successor_governing, successor_gov_ref), "SUCCESSOR_FAMILY_NOT_INTERNALLY_COHERENT"),
    ]


def _adoption_result(
    *,
    stack: Mapping[str, Any],
    reresolution: Mapping[str, Any] | None,
    reresolution_path: Path | None,
    successor: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    adopted_refs = _adopted_refs(successor) if outcome == OUTCOME_ADOPTED and successor is not None else _null_adopted_refs()
    return {
        "adoption_metadata": {
            "adoption_result_id": _adoption_result_id(reresolution),
            "adoption_result_type": ADOPTION_RESULT_TYPE,
            "adoption_result_version": ADOPTION_RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "prior_current_family": _prior_family_reference(stack),
        "selected_reresolution_result": _selected_reresolution_summary(reresolution, reresolution_path, extra_refs),
        "selected_successor_family": _successor_family_reference(successor),
        "checks": checks,
        "outcome": outcome,
        "block": {"block_code": block_code, "block_reason": block_reason},
        "adopted_family_references": adopted_refs,
        "adoption_summary": _adoption_summary(stack, reresolution, successor, outcome),
        "non_claims": dict(non_claims),
    }


def _prior_family_reference(stack: Mapping[str, Any]) -> dict[str, str]:
    return {
        "prior_authority_artifact_path": _display(_path_value(stack, "authority_path")),
        "prior_family_packet_path": _display(_path_value(stack, "family_path")),
        "prior_status_packet_path": _display(_path_value(stack, "status_path")),
        "prior_current_governing_packet_path": _display(_path_value(stack, "governing_path")),
    }


def _selected_reresolution_summary(
    reresolution: Mapping[str, Any] | None,
    reresolution_path: Path | None,
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if reresolution is None:
        summary = {
            "reresolution_result_artifact_path": None,
            "reresolution_id": None,
            "outcome": None,
            "selected_transition_result_artifact_path": None,
        }
    else:
        metadata = _obj(reresolution, "reresolution_metadata", "governing re-resolution result")
        inputs = _obj(reresolution, "input_references", "governing re-resolution result")
        summary = {
            "reresolution_result_artifact_path": _display(reresolution_path) if reresolution_path is not None else None,
            "reresolution_id": metadata.get("reresolution_id"),
            "outcome": reresolution.get("outcome"),
            "selected_transition_result_artifact_path": inputs.get("selected_transition_result_artifact_path"),
        }
    if extra_refs is not None:
        summary["selection_references"] = _json_ready(extra_refs)
    return summary


def _successor_family_reference(successor: Mapping[str, Any] | None) -> dict[str, str | None]:
    if successor is None:
        return _null_adopted_refs()
    return {
        "successor_authority_artifact_path": _display(_path_value(successor, "authority_path")),
        "successor_family_packet_path": _display(_path_value(successor, "family_path")),
        "successor_status_packet_path": _display(_path_value(successor, "status_path")),
        "successor_current_governing_packet_path": _display(_path_value(successor, "governing_path")),
    }


def _adopted_refs(successor: Mapping[str, Any]) -> dict[str, str]:
    return {
        "adopted_authority_artifact_path": _display(_path_value(successor, "authority_path")),
        "adopted_family_packet_path": _display(_path_value(successor, "family_path")),
        "adopted_status_packet_path": _display(_path_value(successor, "status_path")),
        "adopted_current_governing_packet_path": _display(_path_value(successor, "governing_path")),
    }


def _null_adopted_refs() -> dict[str, None]:
    return {
        "adopted_authority_artifact_path": None,
        "adopted_family_packet_path": None,
        "adopted_status_packet_path": None,
        "adopted_current_governing_packet_path": None,
    }


def _adoption_summary(
    stack: Mapping[str, Any],
    reresolution: Mapping[str, Any] | None,
    successor: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    current_summary = _obj(stack, "governing_summary", "current stack")
    if successor is not None:
        status_summary = _obj(successor, "status_summary", "successor family")
        governing_summary = _obj(successor, "governing_summary", "successor family")
        new_source = governing_summary.get("current_governing_source_run_path")
        return {
            "prior_governing_source_run_path": current_summary.get("current_governing_source_run_path"),
            "new_governing_source_run_path": new_source,
            "preserved_run_count": status_summary.get("preserved_run_count"),
            "preserved_eligible_non_authority_count": status_summary.get("preserved_eligible_non_authority_count"),
            "preserved_ineligible_count": status_summary.get("preserved_ineligible_count"),
            "current_authority_run_count": status_summary.get("current_authority_run_count"),
            "successor_family_adopted": outcome == OUTCOME_ADOPTED,
        }
    candidate_source = None
    if reresolution is not None:
        projection = _obj(reresolution, "successor_projection_summary", "governing re-resolution result")
        candidate_source = projection.get("new_governing_source_run_path")
    return {
        "prior_governing_source_run_path": current_summary.get("current_governing_source_run_path"),
        "new_governing_source_run_path": candidate_source,
        "successor_family_adopted": False,
    }


def _write_default_adoption_result(result: Mapping[str, Any]) -> Path:
    return write_governing_successor_adoption_result(result)


def _default_result_path(result: Mapping[str, Any]) -> Path:
    return _next_json_path(
        _repo_root() / GOVERNING_SUCCESSOR_ADOPTION_ROOT,
        f"{_safe(_adoption_result_id_from_result(result))}__governing_successor_adoption_result",
    )


def _adoption_result_id(reresolution: Mapping[str, Any] | None) -> str:
    if reresolution is None:
        return "no_successor_projection_available__governing_successor_adoption"
    metadata = _obj(reresolution, "reresolution_metadata", "governing re-resolution result")
    return f"{_str(metadata, 'reresolution_id', 'governing re-resolution metadata')}__governing_successor_adoption"


def _adoption_result_id_from_result(result: Mapping[str, Any]) -> str:
    return _str(_obj(result, "adoption_metadata", "successor-adoption result"), "adoption_result_id", "adoption metadata")


def _combined_non_claims(
    base_non_claims: Mapping[str, bool],
    reresolution: Mapping[str, Any],
    successor: Mapping[str, Any] | None,
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for key in NON_CLAIM_DEFAULTS:
        if key in base_non_claims:
            if base_non_claims[key] is not False:
                raise GoverningSuccessorAdoptionError(f"current family non_claims.{key} must remain false")
            non_claims[key] = False
    _merge_non_claims(non_claims, _obj(reresolution, "non_claims", "governing re-resolution result"), "governing re-resolution result")
    if successor is not None:
        for stack_key in ("authority", "family", "status", "governing"):
            artifact = _obj(successor, stack_key, "successor family")
            _merge_non_claims(non_claims, _obj(artifact, "non_claims", f"successor {stack_key} artifact"), f"successor {stack_key} artifact")
    return non_claims


def _stack_non_claims(stack: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for stack_key in ("authority", "family", "status", "governing"):
        artifact = _obj(stack, stack_key, "current stack")
        incoming = _obj(artifact, "non_claims", f"current {stack_key} artifact")
        _merge_non_claims(non_claims, incoming, f"current {stack_key} artifact")
    return non_claims


def _merge_non_claims(target: dict[str, bool], incoming: Mapping[str, Any], context: str) -> None:
    for key in NON_CLAIM_DEFAULTS:
        if key in incoming:
            value = _bool(incoming, key, f"{context}.non_claims")
            if value is not False:
                raise GoverningSuccessorAdoptionError(f"{context}.non_claims.{key} must remain false")
            target[key] = False


def _current_paths_match_reresolution(stack: Mapping[str, Any], reresolution: Mapping[str, Any]) -> bool:
    refs = _obj(reresolution, "input_references", "governing re-resolution result")
    pairs = (
        ("authority_path", "authority_artifact_path"),
        ("family_path", "family_packet_path"),
        ("status_path", "status_packet_path"),
        ("governing_path", "current_governing_packet_path"),
    )
    return all(_same(_path_value(stack, stack_key), refs.get(ref_key)) for stack_key, ref_key in pairs)


def _successor_family_coherent(successor: Mapping[str, Any]) -> bool:
    try:
        return _successor_selected_paths_align(successor) and _successor_current_counts_ok(successor)
    except GoverningSuccessorAdoptionError:
        return False


def _successor_selected_paths_align(successor: Mapping[str, Any]) -> bool:
    authority = _obj(successor, "authority_summary", "successor family")
    family = _obj(successor, "family_summary", "successor family")
    status = _obj(successor, "status_summary", "successor family")
    governing = _obj(successor, "governing_summary", "successor family")
    gov_ref = _obj(_obj(successor, "governing", "successor family"), "authority_reference", "successor governing")
    return (
        _same(authority.get("selected_source_run_directory_path"), family.get("current_authority_source_run_path"))
        and _same(authority.get("selected_source_run_directory_path"), status.get("selected_current_authority_source_run_path"))
        and _same(authority.get("selected_source_run_directory_path"), governing.get("current_governing_source_run_path"))
        and _same(authority.get("selected_ingress_run_directory_path"), family.get("current_authority_ingress_run_path"))
        and _same(authority.get("selected_ingress_run_directory_path"), governing.get("current_governing_ingress_run_path"))
        and _same(authority.get("selected_comparison_artifact_path"), gov_ref.get("selected_comparison_artifact_path"))
    )


def _successor_current_counts_ok(successor: Mapping[str, Any]) -> bool:
    status = _obj(successor, "status_summary", "successor family")
    family = _obj(successor, "family_summary", "successor family")
    return (
        status.get("current_authority_run_count") == 1
        and isinstance(status.get("preserved_run_count"), int)
        and status.get("preserved_run_count") == family.get("preserved_run_count")
    )


def _successor_governing_scope_matches(governing: Mapping[str, Any], authority_ref: Mapping[str, Any]) -> bool:
    scope = _obj(governing, "governing_scope", "successor governing")
    return (
        _same(scope.get("governing_source_run_path"), authority_ref.get("selected_source_run_path"))
        and _same(scope.get("governing_ingress_run_path"), authority_ref.get("selected_ingress_run_path"))
        and _same(scope.get("governing_comparison_artifact_path"), authority_ref.get("selected_comparison_artifact_path"))
        and scope.get("governing_is_bounded") is True
        and scope.get("governing_applies_to_current_execution_line") is True
    )


def _reresolution_summary(reresolution: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_governing_reresolution_summary(reresolution)
    except GoverningReresolutionError as exc:
        raise GoverningSuccessorAdoptionError("Governing re-resolution result is malformed") from exc


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise GoverningSuccessorAdoptionError("Authority artifact is malformed") from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise GoverningSuccessorAdoptionError("Run-family packet is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except PreservedRunStatusPacketError as exc:
        raise GoverningSuccessorAdoptionError("Preserved-run status packet is malformed") from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except CurrentGoverningPacketError as exc:
        raise GoverningSuccessorAdoptionError("Current-governing packet is malformed") from exc


def _validate_reresolution_result(payload: dict[str, Any]) -> dict[str, Any]:
    for key in (
        "reresolution_metadata",
        "input_references",
        "selected_reresolution_result",
        "checks",
        "outcome",
        "block",
        "successor_artifacts",
        "successor_projection_summary",
        "non_claims",
    ):
        if key == "checks":
            _list(payload, key, "governing re-resolution result")
        elif key == "outcome":
            _str(payload, key, "governing re-resolution result")
        else:
            _obj(payload, key, "governing re-resolution result")
    outcome = _str(payload, "outcome", "governing re-resolution result")
    if outcome not in {OUTCOME_SUCCESSOR_EMITTED, RERESOLUTION_BLOCKED}:
        raise GoverningSuccessorAdoptionError("Re-resolution result outcome is not recognized")
    _str(_obj(payload, "reresolution_metadata", "governing re-resolution result"), "reresolution_id", "reresolution metadata")
    return payload


def _read_reresolution_result(path: Path) -> dict[str, Any]:
    return _validate_reresolution_result(_read_json(path, "governing re-resolution result"))


def _read_json(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_path(path)
    try:
        value = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GoverningSuccessorAdoptionError(f"{label.title()} file does not exist: {_display(file_path)}") from exc
    except OSError as exc:
        raise GoverningSuccessorAdoptionError(f"Could not read {label}: {_display(file_path)}") from exc
    except json.JSONDecodeError as exc:
        raise GoverningSuccessorAdoptionError(f"{label.title()} is not valid JSON: {_display(file_path)}") from exc
    if not isinstance(value, dict):
        raise GoverningSuccessorAdoptionError(f"{label.title()} JSON must be an object: {_display(file_path)}")
    return value


def _latest_required(root: Path, pattern: str, label: str) -> Path:
    root_path = _require_dir(root, label)
    artifacts = sorted(path for path in root_path.glob(pattern) if path.is_file())
    if not artifacts:
        raise GoverningSuccessorAdoptionError(f"No artifact matching {pattern} found under {_display(root_path)}")
    return artifacts[-1]


def _require_dir(root: Path, label: str) -> Path:
    root_path = _repo_path(root)
    if not root_path.exists():
        raise GoverningSuccessorAdoptionError(f"{label.title()} does not exist: {_display(root_path)}")
    if not root_path.is_dir():
        raise GoverningSuccessorAdoptionError(f"{label.title()} is not a directory: {_display(root_path)}")
    return root_path


def _selection_path(selection: Mapping[str, Any]) -> Path:
    selected = selection.get("selected_reresolution_result_path")
    if not isinstance(selected, Path):
        raise GoverningSuccessorAdoptionError("Selected re-resolution result path is missing")
    return selected


def _reresolution_identity(result: Mapping[str, Any]) -> tuple[str, ...]:
    artifacts = _obj(result, "successor_artifacts", "governing re-resolution result")
    summary = _obj(result, "successor_projection_summary", "governing re-resolution result")
    return (
        str(summary.get("prior_governing_source_run_path")),
        str(summary.get("new_governing_source_run_path")),
        str(artifacts.get("successor_authority_artifact_path")),
        str(artifacts.get("successor_family_packet_path")),
        str(artifacts.get("successor_status_packet_path")),
        str(artifacts.get("successor_governing_packet_path")),
    )


def _find_by_source(entries: list[Any], source_path: str, source_key: str) -> Mapping[str, Any] | None:
    for value in entries:
        entry = _as_mapping(value, "source-indexed entry")
        candidate = entry.get(source_key)
        if isinstance(candidate, str) and _same(candidate, source_path):
            return entry
    return None


def _first_block(checks: list[Mapping[str, Any]]) -> dict[str, str] | None:
    for check in checks:
        if check.get("passed") is not True:
            code = str(check.get("block_code") or "GOVERNING_SUCCESSOR_ADOPTION_BLOCKED")
            return {
                "block_code": code,
                "block_reason": BLOCK_REASONS.get(code, f"Adoption check failed: {check.get('check', 'unknown check')}"),
            }
    return None


def _check(name: str, required: Any, actual: Any, passed: bool, block_code: str) -> dict[str, Any]:
    return {
        "check": name,
        "required": _json_ready(required),
        "actual": _json_ready(actual),
        "passed": bool(passed),
        "block_code": block_code,
    }


def _path_value(mapping: Mapping[str, Any], key: str) -> Path:
    value = mapping.get(key)
    if not isinstance(value, Path):
        raise GoverningSuccessorAdoptionError(f"{key} must be a Path")
    return value


def _require_same_paths(values: tuple[Any, ...], label: str) -> None:
    present = [value for value in values if value is not None]
    if not present:
        raise GoverningSuccessorAdoptionError(f"Missing {label}")
    first = present[0]
    if any(not _same(first, value) for value in present[1:]):
        raise GoverningSuccessorAdoptionError(f"Artifact mismatch for {label}")


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


def _next_json_path(root: Path, stem: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    candidate = root / f"{stem}.json"
    index = 1
    while candidate.exists():
        candidate = root / f"{stem}_{index:03d}.json"
        index += 1
    return candidate


def _safe(value: str) -> str:
    cleaned = "".join(char if char.isalnum() or char in {"-", "_", "."} else "_" for char in value.strip()).strip("._")
    return cleaned or "governing_successor_adoption"


def _as_mapping(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise GoverningSuccessorAdoptionError(f"{context} must be an object")
    return value


def _obj(mapping: Mapping[str, Any], key: str, context: str) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise GoverningSuccessorAdoptionError(f"{context}.{key} must be an object")
    return value


def _list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise GoverningSuccessorAdoptionError(f"{context}.{key} must be a list")
    return value


def _str(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise GoverningSuccessorAdoptionError(f"{context}.{key} must be a non-empty string")
    return value


def _bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise GoverningSuccessorAdoptionError(f"{context}.{key} must be a boolean")
    return value
