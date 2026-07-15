"""Resolve bounded governing re-resolution for v0-min coexistence.

This module reads the current authority, run-family, preserved-run status,
current-governing, and governing-transition result artifacts. It emits one
bounded successor projection when an accepted transition result corresponds to
the current artifact family. It emits a blocked re-resolution result when the
bounded checks do not pass.

The resolver is additive engineering. It does not replay source actions into a
live host, merge preserved runs, mutate prior artifacts, complete continuity,
upgrade standing, define persistence or registry law, or treat accepted
transition results as self-executing governing state.
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
    ROLE_INELIGIBLE,
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
from resolve_integrity_host_v0_min_coexistence_governing_transition import (
    OUTCOME_ACCEPTED,
    OUTCOME_REFUSED,
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
GOVERNING_TRANSITION_RESULT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_governing_transition_results"
)
GOVERNING_RERESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_governing_reresolutions"
)

RERESOLUTION_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_GOVERNING_RERESOLUTION_RESULT"
)
RERESOLUTION_VERSION = "0.1.0"
OUTCOME_SUCCESSOR_EMITTED = "SUCCESSOR_PROJECTION_EMITTED"
OUTCOME_BLOCKED = "BLOCKED"

SUCCESSOR_AUTHORITY_FILENAME = "successor_execution_authority_resolution.json"
SUCCESSOR_FAMILY_FILENAME = "successor_run_family_packet.json"
SUCCESSOR_STATUS_FILENAME = "successor_preserved_run_status_packet.json"
SUCCESSOR_GOVERNING_FILENAME = "successor_current_governing_packet.json"

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
}

BLOCK_REASONS = {
    "NO_ACCEPTED_TRANSITION_RESULT": "No accepted transition result is available for re-resolution.",
    "ACCEPTED_RESULT_UNREADABLE": "Accepted transition result is unreadable.",
    "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING": "Accepted transition result does not correspond to current governing state.",
    "CANONICAL_EXECUTION_LINE_MISMATCH": "Canonical execution line does not match across required re-resolution surfaces.",
    "AUTHORITY_ARTIFACT_UNREADABLE": "Authority artifact is unreadable.",
    "FAMILY_PACKET_UNREADABLE": "Run-family packet is unreadable.",
    "STATUS_PACKET_UNREADABLE": "Preserved-run status packet is unreadable.",
    "CURRENT_GOVERNING_PACKET_UNREADABLE": "Current-governing packet is unreadable.",
    "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_FAMILY": "Successor is not visible in the preserved-run family.",
    "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS": "Successor is not visible as an eligible non-authority run in preserved-run status.",
    "REPLAY_SHORTCUT_REFUSED": "Replay shortcut is refused during re-resolution.",
    "MERGE_SHORTCUT_REFUSED": "Merge shortcut is refused during re-resolution.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Re-resolution may not complete continuity.",
    "SILENT_STANDING_UPGRADE_REFUSED": "Re-resolution may not silently upgrade standing.",
    "MULTIPLE_ACCEPTED_RESULTS_CONFLICT_UNRESOLVED": "Multiple accepted transition results conflict without bounded arbitration.",
}


class GoverningReresolutionError(RuntimeError):
    """Raised when bounded governing re-resolution cannot proceed."""


def discover_latest_authority_resolution(root: Path) -> Path:
    """Return the lexically latest current execution-authority artifact."""

    return _latest_required(root, "current_execution_authority_resolution*.json", "execution-authority resolution root")


def discover_latest_run_family_packet(root: Path) -> Path:
    """Return the lexically latest current run-family packet artifact."""

    return _latest_required(root, "current_run_family_packet*.json", "run-family packet root")


def discover_latest_preserved_run_status_packet(root: Path) -> Path:
    """Return the lexically latest preserved-run status packet artifact."""

    return _latest_required(root, "current_preserved_run_status_packet*.json", "preserved-run status packet root")


def discover_latest_current_governing_packet(root: Path) -> Path:
    """Return the lexically latest current-governing packet artifact."""

    return _latest_required(root, "current_governing_packet*.json", "current-governing packet root")


def discover_latest_accepted_governing_transition_result(root: Path) -> Path:
    """Return the lexically latest accepted governing-transition result."""

    selection = _select_default_transition_result(root)
    if selection["block_code"] is not None:
        raise GoverningReresolutionError(str(selection["block_reason"]))
    selected = selection["selected_transition_result_path"]
    if not isinstance(selected, Path):
        raise GoverningReresolutionError("No accepted governing-transition result found")
    return selected


def resolve_governing_reresolution(
    transition_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded downstream governing re-resolution."""

    stack = _load_current_stack()
    _verify_current_stack(stack)
    non_claims = _stack_non_claims(stack)

    if transition_result is None:
        selection = _select_default_transition_result(GOVERNING_TRANSITION_RESULT_ROOT)
        if selection["block_code"] is not None:
            return _emit_blocked(
                stack,
                transition=None,
                transition_path=None,
                checks=[
                    _check(
                        "accepted_transition_result_available",
                        "one readable accepted governing-transition result",
                        selection["actual"],
                        False,
                        str(selection["block_code"]),
                    )
                ],
                block_code=str(selection["block_code"]),
                block_reason=str(selection["block_reason"]),
                non_claims=non_claims,
                extra_refs=selection.get("input_references"),
            )
        selected_path = _selection_path(selection)
        transition = _read_transition_result(selected_path)
        extra_refs = selection.get("input_references")
        return _resolve_selected(stack, transition, selected_path, non_claims, extra_refs)

    if not isinstance(transition_result, Mapping):
        raise GoverningReresolutionError("Transition result must be a mapping or None")
    transition = _validate_transition_result(dict(transition_result))
    return _resolve_selected(stack, transition, None, non_claims, None)


def resolve_governing_reresolution_from_path(path: Path | str) -> dict[str, Any]:
    """Read one transition-result artifact and resolve re-resolution from it."""

    transition_path = _repo_path(Path(path))
    transition = _read_transition_result(transition_path)
    stack = _load_current_stack()
    _verify_current_stack(stack)
    return _resolve_selected(stack, transition, transition_path, _stack_non_claims(stack), None)


def write_governing_reresolution_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 re-resolution result artifact."""

    if not isinstance(result, Mapping):
        raise GoverningReresolutionError("Governing re-resolution result must be a mapping")
    target = _default_result_copy_path(result) if output_path is None else _repo_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise GoverningReresolutionError(f"Refusing to overwrite re-resolution result: {_display(target)}")
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_governing_reresolution_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one re-resolution result."""

    metadata = _obj(result, "reresolution_metadata", "re-resolution result")
    block = _obj(result, "block", "re-resolution result")
    checks = _list(result, "checks", "re-resolution result")
    selected = result.get("selected_transition_result")
    selected_map = selected if isinstance(selected, Mapping) else {}
    projection = result.get("successor_projection_summary")
    projection_map = projection if isinstance(projection, Mapping) else {}
    non_claims = _obj(result, "non_claims", "re-resolution result")

    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed = len(checks) - passed
    return {
        "reresolution_id": _str(metadata, "reresolution_id", "re-resolution result.reresolution_metadata"),
        "outcome": _str(result, "outcome", "re-resolution result"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_transition_result_id": selected_map.get("transition_result_id"),
        "prior_governing_source_run_path": projection_map.get("prior_governing_source_run_path"),
        "new_governing_source_run_path": projection_map.get("new_governing_source_run_path"),
        "successor_artifact_paths": dict(_obj(result, "successor_artifacts", "re-resolution result")),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": {key: _bool(non_claims, key, "re-resolution result.non_claims") for key in NON_CLAIM_DEFAULTS},
    }


def _resolve_selected(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    transition_path: Path | None,
    non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    checks = _reresolution_checks(stack, transition, non_claims)
    block = _first_block(checks)
    if block is not None:
        return _emit_blocked(
            stack,
            transition=transition,
            transition_path=transition_path,
            checks=checks,
            block_code=block["block_code"],
            block_reason=block["block_reason"],
            non_claims=non_claims,
            extra_refs=extra_refs,
        )
    return _emit_successor_projection(stack, transition, transition_path, checks, non_claims, extra_refs)


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
    if _str(decision, "decision", "authority resolution.authority_decision") != DECISION_RESOLVED:
        raise GoverningReresolutionError("Governing re-resolution requires resolved current authority")

    cores = {
        _core(authority, "authority resolution"),
        _core(family, "run-family packet"),
        _core(status, "preserved-run status packet"),
        _core(governing, "current-governing packet"),
    }
    if len(cores) != 1:
        raise GoverningReresolutionError("Canonical core execution file does not match across current artifacts")

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
    governing_auth = _obj(governing, "authority_reference", "current-governing packet")
    _require_same_paths(
        (
            authority_summary.get("selected_comparison_artifact_path"),
            governing_auth.get("selected_comparison_artifact_path"),
        ),
        "current governing comparison artifact path",
    )
    if status_summary.get("current_authority_run_count") != 1:
        raise GoverningReresolutionError("Preserved-run status packet must contain exactly one current authority")
    current = _obj(governing, "current_governing_run", "current-governing packet")
    if _str(current, "status_role", "current-governing packet.current_governing_run") != ROLE_CURRENT_AUTHORITY:
        raise GoverningReresolutionError("Current-governing packet does not carry current authority role")


def _select_default_transition_result(root: Path) -> dict[str, Any]:
    root_path = _repo_path(root)
    if not root_path.exists():
        return _selection_block("NO_ACCEPTED_TRANSITION_RESULT", "No governing-transition result root exists.", root_path, [])
    if not root_path.is_dir():
        raise GoverningReresolutionError(f"Governing-transition result root is not a directory: {_display(root_path)}")

    artifacts = sorted(path for path in root_path.glob("*.json") if path.is_file())
    if not artifacts:
        return _selection_block("NO_ACCEPTED_TRANSITION_RESULT", "No governing-transition result artifacts are available.", root_path, [])

    accepted: list[tuple[Path, dict[str, Any]]] = []
    refused_count = 0
    for artifact in artifacts:
        result = _read_transition_result(artifact)
        if _str(result, "outcome", "governing-transition result") == OUTCOME_ACCEPTED:
            accepted.append((artifact, result))
        elif result.get("outcome") == OUTCOME_REFUSED:
            refused_count += 1

    if not accepted:
        block = _selection_block(
            "NO_ACCEPTED_TRANSITION_RESULT",
            "Only refused or non-accepted transition results are available.",
            root_path,
            [],
        )
        block["actual"] = {
            "transition_result_artifact_count": len(artifacts),
            "refused_transition_result_count": refused_count,
            "accepted_transition_result_count": 0,
        }
        return block

    identities = {_transition_identity(result) for _, result in accepted}
    accepted_paths = [_display(path) for path, _ in accepted]
    if len(identities) > 1:
        block = _selection_block(
            "MULTIPLE_ACCEPTED_RESULTS_CONFLICT_UNRESOLVED",
            "Multiple accepted transition results conflict without bounded arbitration.",
            root_path,
            accepted_paths,
        )
        block["actual"] = {
            "accepted_transition_result_count": len(accepted),
            "accepted_transition_result_artifact_paths": accepted_paths,
        }
        return block

    selected = accepted[-1][0]
    return {
        "selected_transition_result_path": selected,
        "block_code": None,
        "block_reason": None,
        "actual": {
            "accepted_transition_result_count": len(accepted),
            "selected_transition_result_artifact_path": _display(selected),
        },
        "input_references": {
            "transition_result_root_path": _display(root_path),
            "accepted_transition_result_artifact_paths": accepted_paths,
        },
    }


def _selection_block(code: str, reason: str, root: Path, accepted_paths: list[str]) -> dict[str, Any]:
    return {
        "selected_transition_result_path": None,
        "block_code": code,
        "block_reason": reason,
        "actual": {"accepted_transition_result_count": len(accepted_paths)},
        "input_references": {
            "transition_result_root_path": _display(root),
            "accepted_transition_result_artifact_paths": accepted_paths,
        },
    }


def _reresolution_checks(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    authority = _obj(stack, "authority", "current stack")
    family = _obj(stack, "family", "current stack")
    status = _obj(stack, "status", "current stack")
    governing = _obj(stack, "governing", "current stack")
    current = _obj(governing, "current_governing_run", "current-governing packet")
    before = _obj(transition, "current_governing_before", "governing-transition result")
    candidate = _obj(transition, "candidate_successor", "governing-transition result")
    after = _obj(transition, "current_governing_after", "governing-transition result")
    transition_non_claims = _obj(transition, "non_claims", "governing-transition result")

    current_source = _str(current, "source_run_directory_path", "current governing run")
    current_ingress = _str(current, "matched_ingress_run_path", "current governing run")
    current_comparison = _str(current, "matched_comparison_artifact_path", "current governing run")
    successor_source = _str(candidate, "source_run_path", "transition candidate")
    successor_ingress = _str(candidate, "ingress_run_path", "transition candidate")
    successor_comparison = _str(candidate, "comparison_artifact_path", "transition candidate")

    family_entry = _find_by_source(_list(family, "preserved_runs", "run-family packet"), successor_source, "source_run_directory_path")
    status_entry = _find_by_source(_list(status, "preserved_run_status_entries", "status packet"), successor_source, "source_run_directory_path")
    authority_entry = _find_by_source(_list(authority, "candidate_runs", "authority resolution"), successor_source, "source_run_directory_path")
    current_status_entry = _find_by_source(_list(status, "preserved_run_status_entries", "status packet"), current_source, "source_run_directory_path")
    authority_checks = _obj(authority_entry, "eligibility_checks", "authority candidate") if authority_entry is not None else {}
    current_preservation = _obj(current_status_entry, "preservation_signals", "current status entry") if current_status_entry is not None else {}

    return [
        _check("input_artifact_correspondence_holds", "current artifacts correspond", "verified before transition checks", True, "CANONICAL_EXECUTION_LINE_MISMATCH"),
        _check("accepted_transition_result_exists", OUTCOME_ACCEPTED, transition.get("outcome"), transition.get("outcome") == OUTCOME_ACCEPTED, "NO_ACCEPTED_TRANSITION_RESULT"),
        _check("canonical_core_execution_file_matches", "same canonical core execution line", authority_checks.get("canonical_core_execution_file_preserved"), _cores_match(stack) and authority_checks.get("canonical_core_execution_file_preserved") is True, "CANONICAL_EXECUTION_LINE_MISMATCH"),
        _check("accepted_result_current_source_matches", current_source, before.get("source_run_path"), _same(current_source, before.get("source_run_path")), "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING"),
        _check("accepted_result_current_ingress_matches", current_ingress, before.get("ingress_run_path"), _same(current_ingress, before.get("ingress_run_path")), "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING"),
        _check("accepted_result_current_comparison_matches", current_comparison, before.get("comparison_artifact_path"), _same(current_comparison, before.get("comparison_artifact_path")), "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING"),
        _check("successor_visible_in_preserved_run_family", "successor appears in family packet", family_entry is not None, family_entry is not None, "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_FAMILY"),
        _check("successor_visible_in_preserved_run_status", "successor appears in status packet", status_entry is not None, status_entry is not None, "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS"),
        _check("successor_was_eligible_non_authority", ROLE_ELIGIBLE_NON_AUTHORITY, status_entry.get("status_role") if status_entry else None, status_entry is not None and status_entry.get("status_role") == ROLE_ELIGIBLE_NON_AUTHORITY, "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS"),
        _check(
            "successor_still_authority_eligible",
            "successor eligible in status, family, and authority artifacts",
            {
                "status_candidate_eligible": status_entry.get("candidate_eligible") if status_entry else False,
                "family_candidate_eligible": family_entry.get("candidate_eligible") if family_entry else False,
                "authority_candidate_eligible": authority_entry.get("eligible") if authority_entry else False,
            },
            status_entry is not None
            and family_entry is not None
            and authority_entry is not None
            and status_entry.get("candidate_eligible") is True
            and family_entry.get("candidate_eligible") is True
            and authority_entry.get("eligible") is True,
            "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS",
        ),
        _check("successor_source_run_readable", "successor source run with manifest is readable", successor_source, _source_readable(successor_source), "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_FAMILY"),
        _check("successor_ingress_run_readable", "successor ingress run with manifest is readable", successor_ingress, _ingress_readable(successor_ingress), "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS"),
        _check("successor_comparison_artifact_readable", "successor comparison artifact is readable", successor_comparison, _file_readable(successor_comparison), "SUCCESSOR_NOT_VISIBLE_IN_PRESERVED_RUN_STATUS"),
        _check("accepted_result_after_names_successor", "current_governing_after names the candidate successor", dict(after), _same(after.get("source_run_path"), successor_source) and _same(after.get("ingress_run_path"), successor_ingress) and _same(after.get("comparison_artifact_path"), successor_comparison), "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING"),
        _check("transition_result_replay_non_claim_false", False, transition_non_claims.get("replayed_into_live_host"), transition_non_claims.get("replayed_into_live_host") is False and non_claims["replayed_into_live_host"] is False, "REPLAY_SHORTCUT_REFUSED"),
        _check("transition_result_merge_non_claim_false", False, transition_non_claims.get("merged_into_local_state"), transition_non_claims.get("merged_into_local_state") is False and non_claims["merged_into_local_state"] is False, "MERGE_SHORTCUT_REFUSED"),
        _check("transition_result_continuity_non_claim_false", False, transition_non_claims.get("continuity_completed"), transition_non_claims.get("continuity_completed") is False and non_claims["continuity_completed"] is False, "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
        _check("transition_result_standing_non_claim_false", False, transition_non_claims.get("standing_upgraded"), transition_non_claims.get("standing_upgraded") is False and non_claims["standing_upgraded"] is False, "SILENT_STANDING_UPGRADE_REFUSED"),
        _check("prior_governing_run_remains_preserved", "prior source, ingress, comparison, and authority visibility remain true", dict(current_preservation), _preservation_true(current_preservation), "ACCEPTED_RESULT_DOES_NOT_CORRESPOND_TO_CURRENT_GOVERNING"),
        _check("preserved_run_multiplicity_remains_visible", "family/status preserved-run counts align", {"family_count": len(_list(family, "preserved_runs", "run-family packet")), "status_count": len(_list(status, "preserved_run_status_entries", "status packet"))}, len(_list(family, "preserved_runs", "run-family packet")) == len(_list(status, "preserved_run_status_entries", "status packet")), "FAMILY_PACKET_UNREADABLE"),
        _check("prior_artifacts_not_silently_mutated", "writes occur only under the re-resolution root", GOVERNING_RERESOLUTION_ROOT.as_posix(), True, "SILENT_STANDING_UPGRADE_REFUSED"),
        _check("reresolution_not_inferred_from_result_existence_alone", "explicit selected transition result plus checks", _transition_selected_summary(transition), True, "MULTIPLE_ACCEPTED_RESULTS_CONFLICT_UNRESOLVED"),
    ]


def _emit_successor_projection(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    transition_path: Path | None,
    checks: list[dict[str, Any]],
    non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    run_dir = _next_run_dir(transition)
    paths = {
        "successor_authority_artifact_path": run_dir / SUCCESSOR_AUTHORITY_FILENAME,
        "successor_family_packet_path": run_dir / SUCCESSOR_FAMILY_FILENAME,
        "successor_status_packet_path": run_dir / SUCCESSOR_STATUS_FILENAME,
        "successor_governing_packet_path": run_dir / SUCCESSOR_GOVERNING_FILENAME,
    }

    authority = _successor_authority(stack, transition)
    family = _successor_family(stack, transition, paths)
    status = _successor_status(stack, transition, paths)
    governing = _successor_governing(stack, transition, paths, status)

    run_dir.mkdir(parents=True, exist_ok=True)
    paths["successor_authority_artifact_path"].write_text(_json_text(authority), encoding="utf-8")
    paths["successor_family_packet_path"].write_text(_json_text(family), encoding="utf-8")
    paths["successor_status_packet_path"].write_text(_json_text(status), encoding="utf-8")
    paths["successor_governing_packet_path"].write_text(_json_text(governing), encoding="utf-8")

    result = _result(
        stack=stack,
        transition=transition,
        transition_path=transition_path,
        run_dir=run_dir,
        checks=checks,
        outcome=OUTCOME_SUCCESSOR_EMITTED,
        block_code=None,
        block_reason=None,
        successor_artifacts={key: _display(path) for key, path in paths.items()},
        successor_summary=_successor_summary(transition, status),
        non_claims=non_claims,
        extra_refs=extra_refs,
    )
    _write_result_in_run_dir(result, run_dir)
    return result


def _emit_blocked(
    stack: Mapping[str, Any],
    *,
    transition: Mapping[str, Any] | None,
    transition_path: Path | None,
    checks: list[dict[str, Any]],
    block_code: str,
    block_reason: str,
    non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    run_dir = _next_run_dir(transition)
    run_dir.mkdir(parents=True, exist_ok=True)
    result = _result(
        stack=stack,
        transition=transition,
        transition_path=transition_path,
        run_dir=run_dir,
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason,
        successor_artifacts={
            "successor_authority_artifact_path": None,
            "successor_family_packet_path": None,
            "successor_status_packet_path": None,
            "successor_governing_packet_path": None,
        },
        successor_summary=_blocked_summary(stack, transition),
        non_claims=non_claims,
        extra_refs=extra_refs,
    )
    _write_result_in_run_dir(result, run_dir)
    return result


def _result(
    *,
    stack: Mapping[str, Any],
    transition: Mapping[str, Any] | None,
    transition_path: Path | None,
    run_dir: Path,
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    successor_artifacts: Mapping[str, Any],
    successor_summary: Mapping[str, Any],
    non_claims: Mapping[str, bool],
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return {
        "reresolution_metadata": {
            "reresolution_id": _reresolution_id(transition),
            "reresolution_type": RERESOLUTION_TYPE,
            "reresolution_version": RERESOLUTION_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "input_references": _input_refs(stack, transition_path, run_dir, extra_refs),
        "selected_transition_result": _transition_summary(transition, transition_path) if transition is not None else None,
        "checks": checks,
        "outcome": outcome,
        "block": {"block_code": block_code, "block_reason": block_reason},
        "successor_artifacts": dict(successor_artifacts),
        "successor_projection_summary": dict(successor_summary),
        "non_claims": dict(non_claims),
    }


def _successor_authority(stack: Mapping[str, Any], transition: Mapping[str, Any]) -> dict[str, Any]:
    authority = _copy_json(_obj(stack, "authority", "current stack"))
    candidate = _obj(transition, "candidate_successor", "transition result")
    metadata = _obj(authority, "resolution_metadata", "successor authority")
    decision = _obj(authority, "authority_decision", "successor authority")
    metadata["generated_at"] = _utc_timestamp()
    metadata["resolver_module"] = __name__
    metadata["successor_projection_reference"] = _projection_ref(stack, transition)
    decision["decision"] = DECISION_RESOLVED
    decision["decision_reason"] = "SUCCESSOR_SELECTED_BY_ACCEPTED_GOVERNING_TRANSITION_RERESOLUTION"
    decision["selected_source_run_directory_path"] = _str(candidate, "source_run_path", "transition candidate")
    decision["selected_ingress_run_directory_path"] = _str(candidate, "ingress_run_path", "transition candidate")
    decision["selected_comparison_artifact_path"] = _str(candidate, "comparison_artifact_path", "transition candidate")
    return authority


def _successor_family(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    paths: Mapping[str, Path],
) -> dict[str, Any]:
    family = _copy_json(_obj(stack, "family", "current stack"))
    candidate = _obj(transition, "candidate_successor", "transition result")
    before = _obj(transition, "current_governing_before", "transition result")
    successor_source = _str(candidate, "source_run_path", "transition candidate")
    prior_source = _str(before, "source_run_path", "transition before")
    _obj(family, "family_metadata", "successor family")["generated_at"] = _utc_timestamp()
    auth_ref = _obj(family, "authority_reference", "successor family")
    _set_selected_authority_ref(auth_ref, candidate)
    auth_ref["resolution_artifact_path"] = _display(paths["successor_authority_artifact_path"])

    for value in _list(family, "preserved_runs", "successor family"):
        entry = _as_mapping(value, "successor family preserved run")
        source = _str(entry, "source_run_directory_path", "successor family preserved run")
        entry["current_authority"] = _same(source, successor_source)
        if _same(source, prior_source):
            entry["candidate_eligible"] = True
            entry["ineligibility_reasons"] = []

    currentness = _obj(family, "currentness_status", "successor family")
    currentness["current_execution_authority_exists"] = True
    currentness["current_execution_authority_source_run_path"] = successor_source
    currentness["current_execution_authority_ingress_run_path"] = _str(candidate, "ingress_run_path", "transition candidate")
    currentness["current_execution_authority_resolved_by_explicit_checks"] = True
    currentness["latest_emitted_is_not_authority_by_default"] = True
    family["successor_projection_reference"] = _projection_ref(stack, transition)
    return family


def _successor_status(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    paths: Mapping[str, Path],
) -> dict[str, Any]:
    status = _copy_json(_obj(stack, "status", "current stack"))
    candidate = _obj(transition, "candidate_successor", "transition result")
    before = _obj(transition, "current_governing_before", "transition result")
    successor_source = _str(candidate, "source_run_path", "transition candidate")
    prior_source = _str(before, "source_run_path", "transition before")
    _obj(status, "status_packet_metadata", "successor status")["generated_at"] = _utc_timestamp()
    auth_ref = _obj(status, "authority_reference", "successor status")
    _set_selected_authority_ref(auth_ref, candidate)
    auth_ref["authority_artifact_path"] = _display(paths["successor_authority_artifact_path"])
    auth_ref["run_family_packet_artifact_path"] = _display(paths["successor_family_packet_path"])

    entries = _list(status, "preserved_run_status_entries", "successor status")
    for value in entries:
        entry = _as_mapping(value, "successor status entry")
        source = _str(entry, "source_run_directory_path", "successor status entry")
        if _same(source, successor_source):
            _set_role(entry, ROLE_CURRENT_AUTHORITY, True, True, [], "SELECTED_BY_ACCEPTED_GOVERNING_TRANSITION_RERESOLUTION")
        elif _same(source, prior_source):
            _set_role(entry, ROLE_ELIGIBLE_NON_AUTHORITY, False, True, [], "PRIOR_GOVERNING_RUN_PRESERVED_AS_NON_AUTHORITY_AFTER_RERESOLUTION")
        elif entry.get("candidate_eligible") is True and not entry.get("ineligibility_reasons"):
            _set_role(entry, ROLE_ELIGIBLE_NON_AUTHORITY, False, True, [], "ELIGIBLE_PRESERVED_RUN_NOT_SELECTED_AFTER_RERESOLUTION")
        else:
            entry["status_role"] = ROLE_INELIGIBLE
            entry["current_authority"] = False

    status["aggregate_status_counts"] = _status_counts(entries)
    status["successor_projection_reference"] = _projection_ref(stack, transition)
    return status


def _successor_governing(
    stack: Mapping[str, Any],
    transition: Mapping[str, Any],
    paths: Mapping[str, Path],
    status: Mapping[str, Any],
) -> dict[str, Any]:
    governing = _copy_json(_obj(stack, "governing", "current stack"))
    candidate = _obj(transition, "candidate_successor", "transition result")
    current_entry = _current_status_entry(status)
    _obj(governing, "governing_packet_metadata", "successor governing")["generated_at"] = _utc_timestamp()
    auth_ref = _obj(governing, "authority_reference", "successor governing")
    _set_selected_authority_ref(auth_ref, candidate)
    auth_ref["authority_artifact_path"] = _display(paths["successor_authority_artifact_path"])
    auth_ref["run_family_packet_artifact_path"] = _display(paths["successor_family_packet_path"])
    auth_ref["preserved_run_status_packet_artifact_path"] = _display(paths["successor_status_packet_path"])

    non_claims = _obj(governing, "non_claims", "successor governing")
    governing["current_governing_run"] = {
        "source_run_directory_path": _str(current_entry, "source_run_directory_path", "successor current status entry"),
        "source_manifest_path": _str(current_entry, "source_manifest_path", "successor current status entry"),
        "matched_ingress_run_path": _str(current_entry, "matched_ingress_run_path", "successor current status entry"),
        "matched_comparison_artifact_path": _str(current_entry, "matched_comparison_artifact_path", "successor current status entry"),
        "status_role": ROLE_CURRENT_AUTHORITY,
        "current_authority": True,
        "candidate_eligible": True,
        "governing_reason": "SUCCESSOR_PROJECTION_FROM_ACCEPTED_GOVERNING_TRANSITION_RESULT",
        "preservation_signals": _preservation_signals(current_entry),
        "non_claims": dict(non_claims),
    }
    governing["preserved_non_governing_runs"] = _non_governing_status_entries(status)
    canonical = _obj(governing, "canonical_execution_line", "successor governing")
    governing["governing_scope"] = {
        "governing_core_execution_file": _str(canonical, "core_execution_file", "successor governing canonical line"),
        "governing_source_run_path": auth_ref["selected_source_run_path"],
        "governing_ingress_run_path": auth_ref["selected_ingress_run_path"],
        "governing_comparison_artifact_path": auth_ref["selected_comparison_artifact_path"],
        "governing_is_bounded": True,
        "governing_applies_to_current_execution_line": True,
        "preserved_non_governing_runs_remain_preserved": True,
        "current_authority_does_not_erase_preserved_runs": True,
    }
    _obj(governing, "forced_system_pressure_signals", "successor governing")[
        "governing_reresolution_pressure"
    ] = "Accepted transition results require explicit successor projection rather than hidden mutation."
    governing["successor_projection_reference"] = _projection_ref(stack, transition)
    return governing


def _set_selected_authority_ref(ref: dict[str, Any], candidate: Mapping[str, Any]) -> None:
    ref["authority_decision"] = DECISION_RESOLVED
    ref["authority_decision_reason"] = "SUCCESSOR_SELECTED_BY_ACCEPTED_GOVERNING_TRANSITION_RERESOLUTION"
    ref["selected_source_run_path"] = _str(candidate, "source_run_path", "transition candidate")
    ref["selected_ingress_run_path"] = _str(candidate, "ingress_run_path", "transition candidate")
    ref["selected_comparison_artifact_path"] = _str(candidate, "comparison_artifact_path", "transition candidate")


def _set_role(
    entry: dict[str, Any],
    role: str,
    current: bool,
    eligible: bool,
    ineligibility_reasons: list[str],
    reason: str,
) -> None:
    entry["status_role"] = role
    entry["current_authority"] = current
    entry["candidate_eligible"] = eligible
    entry["ineligibility_reasons"] = ineligibility_reasons
    entry["status_reason"] = reason


def _current_status_entry(status: Mapping[str, Any]) -> Mapping[str, Any]:
    current = [
        _as_mapping(value, "successor status entry")
        for value in _list(status, "preserved_run_status_entries", "successor status")
        if isinstance(value, Mapping) and value.get("status_role") == ROLE_CURRENT_AUTHORITY
    ]
    if len(current) != 1:
        raise GoverningReresolutionError("Successor status must carry exactly one current authority")
    return current[0]


def _non_governing_status_entries(status: Mapping[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for value in _list(status, "preserved_run_status_entries", "successor status"):
        entry = _as_mapping(value, "successor status entry")
        if entry.get("status_role") == ROLE_CURRENT_AUTHORITY:
            continue
        entries.append(
            {
                "source_run_directory_path": _str(entry, "source_run_directory_path", "successor status entry"),
                "source_manifest_path": _str(entry, "source_manifest_path", "successor status entry"),
                "matched_ingress_run_path": _optional_str(entry, "matched_ingress_run_path", "successor status entry"),
                "matched_comparison_artifact_path": _optional_str(entry, "matched_comparison_artifact_path", "successor status entry"),
                "status_role": _str(entry, "status_role", "successor status entry"),
                "current_authority": _bool(entry, "current_authority", "successor status entry"),
                "candidate_eligible": _bool(entry, "candidate_eligible", "successor status entry"),
                "status_reason": _str(entry, "status_reason", "successor status entry"),
                "ineligibility_reasons": list(entry.get("ineligibility_reasons", [])),
                "preservation_signals": _preservation_signals(entry),
            }
        )
    return entries


def _status_counts(entries: list[Any]) -> dict[str, int]:
    roles = [_as_mapping(entry, "status entry").get("status_role") for entry in entries]
    current = roles.count(ROLE_CURRENT_AUTHORITY)
    eligible_non_authority = roles.count(ROLE_ELIGIBLE_NON_AUTHORITY)
    ineligible = roles.count(ROLE_INELIGIBLE)
    return {
        "preserved_run_count": len(entries),
        "eligible_run_count": current + eligible_non_authority,
        "current_authority_run_count": current,
        "preserved_eligible_non_authority_count": eligible_non_authority,
        "preserved_ineligible_count": ineligible,
    }


def _successor_summary(transition: Mapping[str, Any], status: Mapping[str, Any]) -> dict[str, Any]:
    before = _obj(transition, "current_governing_before", "transition result")
    after = _obj(transition, "current_governing_after", "transition result")
    counts = _obj(status, "aggregate_status_counts", "successor status")
    return {
        "prior_governing_source_run_path": before.get("source_run_path"),
        "new_governing_source_run_path": after.get("source_run_path"),
        "prior_governing_ingress_run_path": before.get("ingress_run_path"),
        "new_governing_ingress_run_path": after.get("ingress_run_path"),
        "preserved_run_count": _int(counts, "preserved_run_count", "successor status counts"),
        "preserved_eligible_non_authority_count": _int(counts, "preserved_eligible_non_authority_count", "successor status counts"),
        "preserved_ineligible_count": _int(counts, "preserved_ineligible_count", "successor status counts"),
        "current_authority_run_count": _int(counts, "current_authority_run_count", "successor status counts"),
    }


def _blocked_summary(stack: Mapping[str, Any], transition: Mapping[str, Any] | None) -> dict[str, Any]:
    current = _obj(_obj(stack, "governing", "current stack"), "current_governing_run", "current-governing packet")
    candidate_source = None
    if transition is not None:
        candidate_source = _obj(transition, "candidate_successor", "transition result").get("source_run_path")
    return {
        "prior_governing_source_run_path": current.get("source_run_directory_path"),
        "new_governing_source_run_path": candidate_source,
        "successor_projection_emitted": False,
    }


def _projection_ref(stack: Mapping[str, Any], transition: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "projection_type": "SUCCESSOR_GOVERNING_PROJECTION_FROM_RERESOLUTION",
        "transition_result_id": _transition_id(transition),
        "prior_authority_artifact_path": _display(_path_value(stack, "authority_path")),
        "prior_family_packet_path": _display(_path_value(stack, "family_path")),
        "prior_status_packet_path": _display(_path_value(stack, "status_path")),
        "prior_current_governing_packet_path": _display(_path_value(stack, "governing_path")),
    }


def _input_refs(
    stack: Mapping[str, Any],
    transition_path: Path | None,
    run_dir: Path,
    extra_refs: Mapping[str, Any] | None,
) -> dict[str, Any]:
    refs = {
        "authority_artifact_path": _display(_path_value(stack, "authority_path")),
        "family_packet_path": _display(_path_value(stack, "family_path")),
        "status_packet_path": _display(_path_value(stack, "status_path")),
        "current_governing_packet_path": _display(_path_value(stack, "governing_path")),
        "selected_transition_result_artifact_path": _display(transition_path) if transition_path is not None else None,
        "reresolution_run_directory_path": _display(run_dir),
    }
    if extra_refs is not None:
        refs.update(_json_ready(extra_refs))
    return refs


def _transition_summary(transition: Mapping[str, Any], transition_path: Path | None) -> dict[str, Any]:
    metadata = _obj(transition, "result_metadata", "transition result")
    proposal = _obj(transition, "proposal", "transition result")
    return {
        "transition_result_id": _str(metadata, "transition_result_id", "transition result metadata"),
        "transition_result_artifact_path": _display(transition_path) if transition_path is not None else None,
        "transition_proposal_id": proposal.get("transition_proposal_id"),
        "outcome": _str(transition, "outcome", "transition result"),
        "current_governing_before": dict(_obj(transition, "current_governing_before", "transition result")),
        "candidate_successor": dict(_obj(transition, "candidate_successor", "transition result")),
        "current_governing_after": dict(_obj(transition, "current_governing_after", "transition result")),
    }


def _transition_selected_summary(transition: Mapping[str, Any]) -> dict[str, Any]:
    metadata = _obj(transition, "result_metadata", "transition result")
    return {
        "transition_result_id": metadata.get("transition_result_id"),
        "outcome": transition.get("outcome"),
    }


def _write_result_in_run_dir(result: Mapping[str, Any], run_dir: Path) -> Path:
    path = run_dir / f"{_safe(_reresolution_id_from_result(result))}_result.json"
    if path.exists():
        raise GoverningReresolutionError(f"Refusing to overwrite re-resolution result: {_display(path)}")
    path.write_text(_json_text(result), encoding="utf-8")
    return path


def _default_result_copy_path(result: Mapping[str, Any]) -> Path:
    return _next_json_path(
        _repo_root() / GOVERNING_RERESOLUTION_ROOT,
        f"{_safe(_reresolution_id_from_result(result))}__governing_reresolution_result",
    )


def _next_run_dir(transition: Mapping[str, Any] | None) -> Path:
    root = _repo_root() / GOVERNING_RERESOLUTION_ROOT
    root.mkdir(parents=True, exist_ok=True)
    stem = _safe(_reresolution_id(transition))
    candidate = root / stem
    index = 1
    while candidate.exists():
        candidate = root / f"{stem}_{index:03d}"
        index += 1
    return candidate


def _reresolution_id(transition: Mapping[str, Any] | None) -> str:
    if transition is None:
        return "no_accepted_transition_result__governing_reresolution"
    return f"{_transition_id(transition)}__governing_reresolution"


def _reresolution_id_from_result(result: Mapping[str, Any]) -> str:
    return _str(_obj(result, "reresolution_metadata", "re-resolution result"), "reresolution_id", "re-resolution metadata")


def _transition_id(transition: Mapping[str, Any]) -> str:
    return _str(_obj(transition, "result_metadata", "transition result"), "transition_result_id", "transition result metadata")


def _validate_transition_result(payload: dict[str, Any]) -> dict[str, Any]:
    for key in (
        "result_metadata",
        "proposal",
        "current_governing_before",
        "candidate_successor",
        "current_governing_after",
        "refusal",
        "non_claims",
    ):
        _obj(payload, key, "governing-transition result")
    _list(payload, "checks", "governing-transition result")
    outcome = _str(payload, "outcome", "governing-transition result")
    if outcome not in {OUTCOME_ACCEPTED, OUTCOME_REFUSED}:
        raise GoverningReresolutionError("Transition result outcome must be ACCEPTED or REFUSED")
    _str(_obj(payload, "result_metadata", "transition result"), "transition_result_id", "transition result metadata")

    required_sections = ("current_governing_before", "candidate_successor")
    if outcome == OUTCOME_ACCEPTED:
        required_sections = required_sections + ("current_governing_after",)
    for section_name in required_sections:
        section = _obj(payload, section_name, "transition result")
        for path_key in ("source_run_path", "ingress_run_path", "comparison_artifact_path"):
            _str(section, path_key, f"transition result.{section_name}")
    return payload


def _read_transition_result(path: Path) -> dict[str, Any]:
    return _validate_transition_result(_read_json(path, "governing-transition result"))


def _read_json(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_path(path)
    try:
        value = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GoverningReresolutionError(f"{label.title()} file does not exist: {_display(file_path)}") from exc
    except OSError as exc:
        raise GoverningReresolutionError(f"Could not read {label}: {_display(file_path)}") from exc
    except json.JSONDecodeError as exc:
        raise GoverningReresolutionError(f"{label.title()} is not valid JSON: {_display(file_path)}") from exc
    if not isinstance(value, dict):
        raise GoverningReresolutionError(f"{label.title()} JSON must be an object: {_display(file_path)}")
    return value


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise GoverningReresolutionError("Authority artifact is malformed") from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise GoverningReresolutionError("Run-family packet is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except PreservedRunStatusPacketError as exc:
        raise GoverningReresolutionError("Preserved-run status packet is malformed") from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except CurrentGoverningPacketError as exc:
        raise GoverningReresolutionError("Current-governing packet is malformed") from exc


def _latest_required(root: Path, pattern: str, label: str) -> Path:
    root_path = _require_dir(root, label)
    artifacts = sorted(path for path in root_path.glob(pattern) if path.is_file())
    if not artifacts:
        raise GoverningReresolutionError(f"No artifact matching {pattern} found under {_display(root_path)}")
    return artifacts[-1]


def _require_dir(root: Path, label: str) -> Path:
    root_path = _repo_path(root)
    if not root_path.exists():
        raise GoverningReresolutionError(f"{label.title()} does not exist: {_display(root_path)}")
    if not root_path.is_dir():
        raise GoverningReresolutionError(f"{label.title()} is not a directory: {_display(root_path)}")
    return root_path


def _selection_path(selection: Mapping[str, Any]) -> Path:
    selected = selection.get("selected_transition_result_path")
    if not isinstance(selected, Path):
        raise GoverningReresolutionError("Selected transition result path is missing")
    return selected


def _path_value(mapping: Mapping[str, Any], key: str) -> Path:
    value = mapping.get(key)
    if not isinstance(value, Path):
        raise GoverningReresolutionError(f"{key} must be a Path")
    return value


def _find_by_source(entries: list[Any], source_path: str, source_key: str) -> Mapping[str, Any] | None:
    for value in entries:
        entry = _as_mapping(value, "source-indexed entry")
        candidate = entry.get(source_key)
        if isinstance(candidate, str) and _same(candidate, source_path):
            return entry
    return None


def _stack_non_claims(stack: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for stack_key in ("authority", "family", "status", "governing"):
        artifact = _obj(stack, stack_key, "current stack")
        incoming = _obj(artifact, "non_claims", f"{stack_key} artifact")
        for key in NON_CLAIM_DEFAULTS:
            if key in incoming:
                value = _bool(incoming, key, f"{stack_key}.non_claims")
                if value is not False:
                    raise GoverningReresolutionError(f"{stack_key}.non_claims.{key} must remain false")
                non_claims[key] = False
    return non_claims


def _preservation_signals(entry: Mapping[str, Any]) -> dict[str, bool]:
    signals = _obj(entry, "preservation_signals", "preserved-run entry")
    return {
        "source_preserved": _bool(signals, "source_preserved", "preserved-run preservation signals"),
        "ingress_preserved": _bool(signals, "ingress_preserved", "preserved-run preservation signals"),
        "comparison_preserved": _bool(signals, "comparison_preserved", "preserved-run preservation signals"),
        "authority_candidate_visible": _bool(signals, "authority_candidate_visible", "preserved-run preservation signals"),
    }


def _preservation_true(signals: Mapping[str, Any]) -> bool:
    return all(
        signals.get(key) is True
        for key in (
            "source_preserved",
            "ingress_preserved",
            "comparison_preserved",
            "authority_candidate_visible",
        )
    )


def _cores_match(stack: Mapping[str, Any]) -> bool:
    return len(
        {
            _core(_obj(stack, "authority", "current stack"), "authority"),
            _core(_obj(stack, "family", "current stack"), "family"),
            _core(_obj(stack, "status", "current stack"), "status"),
            _core(_obj(stack, "governing", "current stack"), "governing"),
        }
    ) == 1


def _core(packet: Mapping[str, Any], label: str) -> str:
    return _str(_obj(packet, "canonical_execution_line", label), "core_execution_file", f"{label}.canonical_execution_line")


def _transition_identity(result: Mapping[str, Any]) -> tuple[str, ...]:
    before = _obj(result, "current_governing_before", "transition result")
    candidate = _obj(result, "candidate_successor", "transition result")
    after = _obj(result, "current_governing_after", "transition result")
    keys = ("source_run_path", "ingress_run_path", "comparison_artifact_path")
    return tuple(str(section.get(key)) for section in (before, candidate, after) for key in keys)


def _first_block(checks: list[Mapping[str, Any]]) -> dict[str, str] | None:
    for check in checks:
        if check.get("passed") is not True:
            code = str(check.get("block_code") or "GOVERNING_RERESOLUTION_BLOCKED")
            return {
                "block_code": code,
                "block_reason": BLOCK_REASONS.get(code, f"Re-resolution check failed: {check.get('check', 'unknown check')}"),
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


def _source_readable(path_text: str) -> bool:
    path = _resolve_path(path_text)
    return path.is_dir() and (path / "manifest.json").is_file()


def _ingress_readable(path_text: str) -> bool:
    path = _resolve_path(path_text)
    return path.is_dir() and (path / "manifest.json").is_file()


def _file_readable(path_text: str) -> bool:
    return _resolve_path(path_text).is_file()


def _require_same_paths(values: tuple[Any, ...], label: str) -> None:
    present = [value for value in values if value is not None]
    if not present:
        raise GoverningReresolutionError(f"Missing {label}")
    first = present[0]
    if any(not _same(first, value) for value in present[1:]):
        raise GoverningReresolutionError(f"Artifact mismatch for {label}")


def _same(left: Any, right: Any) -> bool:
    if not isinstance(left, (str, Path)) or not isinstance(right, (str, Path)):
        return False
    return _resolve_path(str(left)) == _resolve_path(str(right))


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()
    candidates = ((_repo_root() / path).resolve(),)
    return candidates[0]


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


def _copy_json(value: Mapping[str, Any]) -> dict[str, Any]:
    return json.loads(json.dumps(_json_ready(value), sort_keys=True))


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
    return cleaned or "governing_reresolution"


def _as_mapping(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise GoverningReresolutionError(f"{context} must be an object")
    return value


def _obj(mapping: Mapping[str, Any], key: str, context: str) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise GoverningReresolutionError(f"{context}.{key} must be an object")
    return value


def _list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise GoverningReresolutionError(f"{context}.{key} must be a list")
    return value


def _str(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise GoverningReresolutionError(f"{context}.{key} must be a non-empty string")
    return value


def _optional_str(mapping: Mapping[str, Any], key: str, context: str) -> str | None:
    value = mapping.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise GoverningReresolutionError(f"{context}.{key} must be a string or null")
    return value


def _bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise GoverningReresolutionError(f"{context}.{key} must be a boolean")
    return value


def _int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise GoverningReresolutionError(f"{context}.{key} must be an integer")
    return value
