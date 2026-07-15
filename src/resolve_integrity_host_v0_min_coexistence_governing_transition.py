"""Resolve one bounded governing-transition proposal for v0-min coexistence.

This module reads the current execution-authority, run-family, preserved-run
status, and current-governing artifacts, then resolves one explicit governing
transition proposal into one additive result artifact.

It does not replay source actions into a live host, merge preserved runs, mutate
preserved artifacts, define persistence or registry law, complete continuity, or
promote latest-emitted/latest-eligible recency into self-executing transition
law.
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

TRANSITION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_GOVERNING_TRANSITION_RESULT"
)
TRANSITION_RESULT_VERSION = "0.1.0"

OUTCOME_ACCEPTED = "ACCEPTED"
OUTCOME_REFUSED = "REFUSED"

REQUIRED_PROPOSAL_FIELDS = (
    "transition_proposal_id",
    "current_governing_source_run_path",
    "candidate_successor_source_run_path",
    "current_governing_ingress_run_path",
    "candidate_successor_ingress_run_path",
    "current_governing_comparison_artifact_path",
    "candidate_successor_comparison_artifact_path",
    "proposal_basis_ref",
    "proposed_at",
    "proposed_by_surface",
)

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
}


class GoverningTransitionResolutionError(RuntimeError):
    """Raised when a governing-transition result cannot be resolved."""


def resolve_governing_transition(proposal: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve one explicit governing-transition proposal."""

    normalized_proposal = _validate_proposal(proposal)
    artifacts = _load_current_artifacts()
    _verify_artifact_correspondence(artifacts)

    non_claims = _non_claims(artifacts)
    current_entry = _current_governing_entry(artifacts["governing"])
    candidate_entry = _find_status_entry(
        artifacts["status"],
        normalized_proposal["candidate_successor_source_run_path"],
    )
    candidate_family_entry = _find_family_entry(
        artifacts["family"],
        normalized_proposal["candidate_successor_source_run_path"],
    )
    candidate_authority_entry = _find_authority_candidate(
        artifacts["authority"],
        normalized_proposal["candidate_successor_source_run_path"],
    )

    checks = _transition_checks(
        normalized_proposal,
        artifacts,
        current_entry,
        candidate_entry,
        candidate_family_entry,
        candidate_authority_entry,
        non_claims,
    )
    refusal = _refusal_from_checks(checks)
    accepted = refusal is None

    current_before = _current_before(current_entry)
    candidate = _candidate_successor(normalized_proposal, candidate_entry)
    current_after = (
        {
            "source_run_path": normalized_proposal[
                "candidate_successor_source_run_path"
            ],
            "ingress_run_path": normalized_proposal[
                "candidate_successor_ingress_run_path"
            ],
            "comparison_artifact_path": normalized_proposal[
                "candidate_successor_comparison_artifact_path"
            ],
        }
        if accepted
        else {
            "source_run_path": None,
            "ingress_run_path": None,
            "comparison_artifact_path": None,
        }
    )

    return {
        "result_metadata": {
            "transition_result_id": _transition_result_id(normalized_proposal),
            "transition_result_type": TRANSITION_RESULT_TYPE,
            "transition_result_version": TRANSITION_RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
            "result_basis_ref": normalized_proposal["proposal_basis_ref"],
        },
        "proposal": dict(normalized_proposal),
        "current_governing_before": current_before,
        "candidate_successor": candidate,
        "current_governing_after": current_after,
        "outcome": OUTCOME_ACCEPTED if accepted else OUTCOME_REFUSED,
        "refusal": {
            "refusal_code": None if accepted else refusal["refusal_code"],
            "refusal_reason": None if accepted else refusal["refusal_reason"],
        },
        "checks": checks,
        "non_claims": non_claims,
    }


def resolve_governing_transition_from_path(path: Path | str) -> dict[str, Any]:
    """Read a JSON proposal from ``path`` and resolve it."""

    proposal_path = _repo_relative_path(Path(path))
    proposal = _read_json_object(proposal_path, "governing transition proposal")
    return resolve_governing_transition(proposal)


def write_governing_transition_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 JSON governing-transition result artifact."""

    if not isinstance(result, Mapping):
        raise GoverningTransitionResolutionError(
            "Governing-transition result must be a mapping"
        )

    target = (
        _next_default_result_path(result)
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise GoverningTransitionResolutionError(
            f"Refusing to overwrite governing-transition result: {_display_path(target)}"
        )
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_governing_transition_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one transition result."""

    metadata = _require_mapping(result, "result_metadata", "transition result")
    current_before = _require_mapping(
        result,
        "current_governing_before",
        "transition result",
    )
    candidate = _require_mapping(result, "candidate_successor", "transition result")
    current_after = _require_mapping(
        result,
        "current_governing_after",
        "transition result",
    )
    refusal = _require_mapping(result, "refusal", "transition result")
    checks = _require_list(result, "checks", "transition result")
    non_claims = _require_mapping(result, "non_claims", "transition result")

    passed = sum(1 for check in checks if bool(check.get("passed")) is True)
    failed = len(checks) - passed

    return {
        "transition_result_id": _require_string(
            metadata,
            "transition_result_id",
            "transition result.result_metadata",
        ),
        "outcome": _require_string(result, "outcome", "transition result"),
        "refusal_code": refusal.get("refusal_code"),
        "refusal_reason": refusal.get("refusal_reason"),
        "current_governing_before": dict(current_before),
        "candidate_successor": dict(candidate),
        "current_governing_after": dict(current_after),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": {
            key: _require_bool(non_claims, key, "transition result.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _load_current_artifacts() -> dict[str, Any]:
    authority_path = _discover_latest_artifact(
        EXECUTION_AUTHORITY_RESOLUTION_ROOT,
        "current_execution_authority_resolution*.json",
        "execution-authority resolution root",
    )
    family_path = _discover_latest_artifact(
        RUN_FAMILY_PACKET_ROOT,
        "current_run_family_packet*.json",
        "run-family packet root",
    )
    status_path = _discover_latest_artifact(
        PRESERVED_RUN_STATUS_PACKET_ROOT,
        "current_preserved_run_status_packet*.json",
        "preserved-run status packet root",
    )
    governing_path = _discover_latest_artifact(
        CURRENT_GOVERNING_PACKET_ROOT,
        "current_governing_packet*.json",
        "current-governing packet root",
    )

    authority = _read_json_object(authority_path, "authority resolution")
    family = _read_json_object(family_path, "run-family packet")
    status = _read_json_object(status_path, "preserved-run status packet")
    governing = _read_json_object(governing_path, "current-governing packet")

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


def _verify_artifact_correspondence(artifacts: Mapping[str, Any]) -> None:
    authority = _require_mapping(artifacts, "authority", "artifacts")
    family = _require_mapping(artifacts, "family", "artifacts")
    status = _require_mapping(artifacts, "status", "artifacts")
    governing = _require_mapping(artifacts, "governing", "artifacts")
    authority_summary = _require_mapping(
        artifacts,
        "authority_summary",
        "artifacts",
    )
    family_summary = _require_mapping(artifacts, "family_summary", "artifacts")
    status_summary = _require_mapping(artifacts, "status_summary", "artifacts")
    governing_summary = _require_mapping(
        artifacts,
        "governing_summary",
        "artifacts",
    )

    decision = _require_mapping(authority, "authority_decision", "authority resolution")
    if _require_string(
        decision,
        "decision",
        "authority resolution.authority_decision",
    ) != DECISION_RESOLVED:
        raise GoverningTransitionResolutionError(
            "Governing transition requires a resolved current authority"
        )

    cores = {
        _core_execution_file(authority, "authority resolution"),
        _core_execution_file(family, "run-family packet"),
        _core_execution_file(status, "preserved-run status packet"),
        _core_execution_file(governing, "current-governing packet"),
    }
    if len(cores) != 1:
        raise GoverningTransitionResolutionError(
            "Canonical core execution file does not match across governing artifacts"
        )

    _require_matching_paths(
        (
            authority_summary.get("selected_source_run_directory_path"),
            family_summary.get("current_authority_source_run_path"),
            status_summary.get("selected_current_authority_source_run_path"),
            governing_summary.get("current_governing_source_run_path"),
        ),
        "selected current governing source run path",
    )
    _require_matching_paths(
        (
            authority_summary.get("selected_ingress_run_directory_path"),
            family_summary.get("current_authority_ingress_run_path"),
            governing_summary.get("current_governing_ingress_run_path"),
        ),
        "selected current governing ingress run path",
    )

    governing_authority = _require_mapping(
        governing,
        "authority_reference",
        "current-governing packet",
    )
    _require_matching_paths(
        (
            authority_summary.get("selected_comparison_artifact_path"),
            governing_authority.get("selected_comparison_artifact_path"),
        ),
        "selected current governing comparison artifact path",
    )

    current_entries = _current_status_entries(status)
    if len(current_entries) != 1:
        raise GoverningTransitionResolutionError(
            "Preserved-run status packet must contain exactly one current authority entry"
        )


def _transition_checks(
    proposal: Mapping[str, str],
    artifacts: Mapping[str, Any],
    current_entry: Mapping[str, Any],
    candidate_entry: Mapping[str, Any] | None,
    candidate_family_entry: Mapping[str, Any] | None,
    candidate_authority_entry: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    current = _require_mapping(
        artifacts["governing"],
        "current_governing_run",
        "current-governing packet",
    )
    current_source = _require_string(
        current,
        "source_run_directory_path",
        "current-governing packet.current_governing_run",
    )
    current_ingress = _require_string(
        current,
        "matched_ingress_run_path",
        "current-governing packet.current_governing_run",
    )
    current_comparison = _require_string(
        current,
        "matched_comparison_artifact_path",
        "current-governing packet.current_governing_run",
    )
    candidate_source = proposal["candidate_successor_source_run_path"]
    candidate_ingress = proposal["candidate_successor_ingress_run_path"]
    candidate_comparison = proposal["candidate_successor_comparison_artifact_path"]

    candidate_preservation = (
        _require_mapping(
            candidate_entry,
            "preservation_signals",
            "candidate preserved-run status entry",
        )
        if candidate_entry is not None
        else {}
    )
    current_preservation = _require_mapping(
        current_entry,
        "preservation_signals",
        "current preserved-run status entry",
    )
    candidate_role = (
        _require_string(
            candidate_entry,
            "status_role",
            "candidate preserved-run status entry",
        )
        if candidate_entry is not None
        else None
    )
    candidate_status_eligible = (
        _require_bool(
            candidate_entry,
            "candidate_eligible",
            "candidate preserved-run status entry",
        )
        if candidate_entry is not None
        else False
    )
    family_candidate_eligible = (
        _require_bool(
            candidate_family_entry,
            "candidate_eligible",
            "candidate run-family entry",
        )
        if candidate_family_entry is not None
        else False
    )
    authority_candidate_eligible = (
        _require_bool(
            candidate_authority_entry,
            "eligible",
            "candidate authority entry",
        )
        if candidate_authority_entry is not None
        else False
    )
    authority_candidate_checks = (
        _require_mapping(
            candidate_authority_entry,
            "eligibility_checks",
            "candidate authority entry",
        )
        if candidate_authority_entry is not None
        else {}
    )

    basis_text = proposal["proposal_basis_ref"].strip()
    source_surface_text = proposal["proposed_by_surface"].strip()

    return [
        _check(
            "current_governing_source_run_matches",
            "proposal current governing source run path matches current-governing packet",
            proposal["current_governing_source_run_path"],
            _same_path(proposal["current_governing_source_run_path"], current_source),
            "CURRENT_GOVERNING_MISMATCH",
        ),
        _check(
            "current_governing_ingress_run_matches",
            "proposal current governing ingress run path matches current-governing packet",
            proposal["current_governing_ingress_run_path"],
            _same_path(proposal["current_governing_ingress_run_path"], current_ingress),
            "CURRENT_GOVERNING_MISMATCH",
        ),
        _check(
            "current_governing_comparison_artifact_matches",
            "proposal current governing comparison artifact path matches current-governing packet",
            proposal["current_governing_comparison_artifact_path"],
            _same_path(
                proposal["current_governing_comparison_artifact_path"],
                current_comparison,
            ),
            "CURRENT_GOVERNING_MISMATCH",
        ),
        _check(
            "candidate_successor_source_run_readable",
            "candidate successor source run exists with manifest",
            candidate_source,
            _source_run_readable(candidate_source),
            "CANDIDATE_NOT_PRESERVED",
        ),
        _check(
            "candidate_successor_ingress_run_readable",
            "candidate successor ingress run exists with manifest",
            candidate_ingress,
            _ingress_run_readable(candidate_ingress),
            "CANDIDATE_NOT_PRESERVED",
        ),
        _check(
            "candidate_successor_comparison_artifact_readable",
            "candidate successor comparison artifact exists",
            candidate_comparison,
            _file_readable(candidate_comparison),
            "CANDIDATE_NOT_PRESERVED",
        ),
        _check(
            "candidate_successor_visible_in_status_packet",
            "candidate successor appears in preserved-run status packet",
            candidate_entry is not None,
            candidate_entry is not None,
            "CANDIDATE_NOT_VISIBLE_IN_STATUS_PACKET",
        ),
        _check(
            "candidate_successor_role_is_eligible_non_authority",
            ROLE_ELIGIBLE_NON_AUTHORITY,
            candidate_role,
            candidate_role == ROLE_ELIGIBLE_NON_AUTHORITY,
            "CANDIDATE_NOT_ELIGIBLE",
        ),
        _check(
            "candidate_successor_still_authority_eligible",
            "candidate remains eligible in status, family, and authority artifacts",
            {
                "status_candidate_eligible": candidate_status_eligible,
                "family_candidate_eligible": family_candidate_eligible,
                "authority_candidate_eligible": authority_candidate_eligible,
            },
            (
                candidate_status_eligible
                and family_candidate_eligible
                and authority_candidate_eligible
            ),
            "CANDIDATE_NOT_ELIGIBLE",
        ),
        _check(
            "candidate_successor_is_not_current_governing",
            "candidate successor is not already current governing",
            candidate_source,
            not _same_path(candidate_source, current_source),
            "CANDIDATE_ALREADY_CURRENT_GOVERNING",
        ),
        _check(
            "proposal_basis_non_empty",
            "non-empty proposal_basis_ref",
            proposal["proposal_basis_ref"],
            bool(basis_text),
            "MISSING_PROPOSAL_BASIS",
        ),
        _check(
            "proposal_source_surface_non_empty",
            "non-empty proposed_by_surface",
            proposal["proposed_by_surface"],
            bool(source_surface_text),
            "MISSING_PROPOSAL_SOURCE_SURFACE",
        ),
        _check(
            "canonical_core_execution_file_matches",
            "candidate and current artifacts preserve the same canonical core execution file",
            authority_candidate_checks.get("canonical_core_execution_file_preserved"),
            (
                _all_core_execution_files_match(artifacts)
                and bool(
                    authority_candidate_checks.get(
                        "canonical_core_execution_file_preserved"
                    )
                )
            ),
            "CANONICAL_EXECUTION_LINE_MISMATCH",
        ),
        _check(
            "replay_remains_false",
            "proposal does not require replay and artifacts carry replay non-claim",
            _proposal_replay_request(proposal),
            not _proposal_replay_request(proposal)
            and non_claims["replayed_into_live_host"] is False,
            "REPLAY_BASED_TRANSITION_REFUSED",
        ),
        _check(
            "merge_remains_false",
            "proposal does not require merge and artifacts carry merge non-claim",
            _proposal_merge_request(proposal),
            not _proposal_merge_request(proposal)
            and non_claims["merged_into_local_state"] is False,
            "MERGE_BASED_TRANSITION_REFUSED",
        ),
        _check(
            "continuity_completion_remains_false",
            "proposal does not complete continuity",
            _proposal_continuity_completion_request(proposal),
            not _proposal_continuity_completion_request(proposal)
            and non_claims["continuity_completed"] is False,
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "standing_upgrade_remains_false",
            "proposal does not silently upgrade standing",
            _proposal_standing_upgrade_request(proposal),
            not _proposal_standing_upgrade_request(proposal)
            and non_claims["standing_upgraded"] is False,
            "SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "prior_governing_run_remains_preserved",
            "prior governing source, ingress, and comparison remain preserved",
            dict(current_preservation),
            (
                _require_bool(
                    current_preservation,
                    "source_preserved",
                    "current preservation signals",
                )
                and _require_bool(
                    current_preservation,
                    "ingress_preserved",
                    "current preservation signals",
                )
                and _require_bool(
                    current_preservation,
                    "comparison_preserved",
                    "current preservation signals",
                )
            ),
            "PRIOR_GOVERNING_ERASURE_REFUSED",
        ),
        _check(
            "transition_not_latest_emitted_inference",
            "transition is not inferred from latest-emitted ordering alone",
            {
                "proposal_basis_ref": proposal["proposal_basis_ref"],
                "proposed_by_surface": proposal["proposed_by_surface"],
            },
            not _contains_inference_text(proposal, "latest_emitted"),
            "LATEST_EMITTED_INFERENCE_REFUSED",
        ),
        _check(
            "transition_not_latest_eligible_inference",
            "transition is not inferred from latest-eligible ordering alone",
            {
                "proposal_basis_ref": proposal["proposal_basis_ref"],
                "proposed_by_surface": proposal["proposed_by_surface"],
            },
            not _contains_inference_text(proposal, "latest_eligible"),
            "LATEST_ELIGIBLE_INFERENCE_REFUSED",
        ),
    ]


def _check(
    name: str,
    required: Any,
    actual: Any,
    passed: bool,
    refusal_code: str,
) -> dict[str, Any]:
    return {
        "check": name,
        "required": _json_ready(required),
        "actual": _json_ready(actual),
        "passed": bool(passed),
        "refusal_code": refusal_code,
    }


def _refusal_from_checks(checks: list[Mapping[str, Any]]) -> dict[str, str] | None:
    for check in checks:
        if check.get("passed") is not True:
            code = str(check.get("refusal_code") or "GOVERNING_TRANSITION_REFUSED")
            return {
                "refusal_code": code,
                "refusal_reason": _refusal_reason(code, check),
            }
    return None


def _refusal_reason(code: str, check: Mapping[str, Any]) -> str:
    reasons = {
        "CANDIDATE_NOT_PRESERVED": "Candidate successor run or its required artifacts are not preserved and readable.",
        "CANDIDATE_NOT_VISIBLE_IN_STATUS_PACKET": "Candidate successor is not visible in the preserved-run status packet.",
        "CANDIDATE_NOT_ELIGIBLE": "Candidate successor is not a preserved eligible non-authority run.",
        "CANDIDATE_ALREADY_CURRENT_GOVERNING": "Candidate successor is already the current governing run.",
        "CURRENT_GOVERNING_MISSING": "Current governing run is missing.",
        "CURRENT_GOVERNING_UNREADABLE": "Current governing run is unreadable.",
        "CURRENT_GOVERNING_MISMATCH": "Proposal current governing identity does not match the current-governing packet.",
        "CANONICAL_EXECUTION_LINE_MISMATCH": "Canonical execution line does not match across required transition surfaces.",
        "MISSING_PROPOSAL_BASIS": "Proposal basis is empty.",
        "MISSING_PROPOSAL_SOURCE_SURFACE": "Proposal source surface is empty.",
        "REPLAY_BASED_TRANSITION_REFUSED": "Replay-based governing transition is refused.",
        "MERGE_BASED_TRANSITION_REFUSED": "Merge-based governing transition is refused.",
        "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Transition may not complete continuity.",
        "SILENT_STANDING_UPGRADE_REFUSED": "Transition may not silently upgrade standing.",
        "PRIOR_GOVERNING_ERASURE_REFUSED": "Prior governing run must remain preserved after transition.",
        "LATEST_EMITTED_INFERENCE_REFUSED": "Transition may not be inferred from latest-emitted ordering alone.",
        "LATEST_ELIGIBLE_INFERENCE_REFUSED": "Transition may not be inferred from latest-eligible ordering alone.",
    }
    return reasons.get(
        code,
        f"Transition check failed: {check.get('check', 'unknown check')}",
    )


def _current_before(current_entry: Mapping[str, Any]) -> dict[str, str]:
    return {
        "source_run_path": _require_string(
            current_entry,
            "source_run_directory_path",
            "current governing entry",
        ),
        "ingress_run_path": _require_string(
            current_entry,
            "matched_ingress_run_path",
            "current governing entry",
        ),
        "comparison_artifact_path": _require_string(
            current_entry,
            "matched_comparison_artifact_path",
            "current governing entry",
        ),
    }


def _candidate_successor(
    proposal: Mapping[str, str],
    candidate_entry: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return {
        "source_run_path": proposal["candidate_successor_source_run_path"],
        "ingress_run_path": proposal["candidate_successor_ingress_run_path"],
        "comparison_artifact_path": proposal[
            "candidate_successor_comparison_artifact_path"
        ],
        "candidate_status_role": (
            _require_string(
                candidate_entry,
                "status_role",
                "candidate preserved-run status entry",
            )
            if candidate_entry is not None
            else None
        ),
    }


def _validate_proposal(proposal: Mapping[str, Any]) -> dict[str, str]:
    if not isinstance(proposal, Mapping):
        raise GoverningTransitionResolutionError("Proposal must be a mapping")

    normalized: dict[str, str] = {}
    for key in REQUIRED_PROPOSAL_FIELDS:
        if key not in proposal:
            raise GoverningTransitionResolutionError(
                f"Proposal missing required field: {key}"
            )
        value = proposal[key]
        if not isinstance(value, str):
            raise GoverningTransitionResolutionError(
                f"Proposal field must be a string: {key}"
            )
        normalized[key] = value

    if not normalized["transition_proposal_id"].strip():
        raise GoverningTransitionResolutionError(
            "Proposal transition_proposal_id must be non-empty"
        )
    if not normalized["proposed_at"].strip():
        raise GoverningTransitionResolutionError("Proposal proposed_at must be non-empty")
    return normalized


def _discover_latest_artifact(root: Path, pattern: str, label: str) -> Path:
    root_path = _require_directory(root, label)
    try:
        artifacts = sorted(path for path in root_path.glob(pattern) if path.is_file())
    except OSError as exc:
        raise GoverningTransitionResolutionError(
            f"Could not read {label}: {_display_path(root_path)}"
        ) from exc
    if not artifacts:
        raise GoverningTransitionResolutionError(
            f"No artifact matching {pattern} found under {_display_path(root_path)}"
        )
    return artifacts[-1]


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GoverningTransitionResolutionError(
            f"{label.title()} file does not exist: {_display_path(path)}"
        ) from exc
    except OSError as exc:
        raise GoverningTransitionResolutionError(
            f"Could not read {label}: {_display_path(path)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise GoverningTransitionResolutionError(
            f"{label.title()} is not valid JSON: {_display_path(path)}"
        ) from exc

    if not isinstance(parsed, dict):
        raise GoverningTransitionResolutionError(
            f"{label.title()} JSON must be an object: {_display_path(path)}"
        )
    return parsed


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise GoverningTransitionResolutionError(
            "Authority resolution artifact is malformed"
        ) from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise GoverningTransitionResolutionError(
            "Run-family packet artifact is malformed"
        ) from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except PreservedRunStatusPacketError as exc:
        raise GoverningTransitionResolutionError(
            "Preserved-run status packet artifact is malformed"
        ) from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except CurrentGoverningPacketError as exc:
        raise GoverningTransitionResolutionError(
            "Current-governing packet artifact is malformed"
        ) from exc


def _current_governing_entry(governing: Mapping[str, Any]) -> Mapping[str, Any]:
    current = _require_mapping(
        governing,
        "current_governing_run",
        "current-governing packet",
    )
    if _require_bool(current, "current_authority", "current governing run") is not True:
        raise GoverningTransitionResolutionError(
            "Current-governing packet current run is not marked current_authority"
        )
    if _require_bool(current, "candidate_eligible", "current governing run") is not True:
        raise GoverningTransitionResolutionError(
            "Current-governing packet current run is not candidate eligible"
        )
    return current


def _current_status_entries(status: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    entries = _require_list(
        status,
        "preserved_run_status_entries",
        "preserved-run status packet",
    )
    current_entries: list[Mapping[str, Any]] = []
    for index, value in enumerate(entries):
        entry = _require_mapping(
            value,
            f"preserved-run status packet.preserved_run_status_entries[{index}]",
        )
        if (
            _require_string(entry, "status_role", "preserved-run status entry")
            == ROLE_CURRENT_AUTHORITY
        ):
            current_entries.append(entry)
    return current_entries


def _find_status_entry(
    status: Mapping[str, Any],
    source_path: str,
) -> Mapping[str, Any] | None:
    entries = _require_list(
        status,
        "preserved_run_status_entries",
        "preserved-run status packet",
    )
    for index, value in enumerate(entries):
        entry = _require_mapping(
            value,
            f"preserved-run status packet.preserved_run_status_entries[{index}]",
        )
        entry_source = _require_string(
            entry,
            "source_run_directory_path",
            "preserved-run status entry",
        )
        if _same_path(entry_source, source_path):
            return entry
    return None


def _find_family_entry(
    family: Mapping[str, Any],
    source_path: str,
) -> Mapping[str, Any] | None:
    entries = _require_list(family, "preserved_runs", "run-family packet")
    for index, value in enumerate(entries):
        entry = _require_mapping(value, f"run-family packet.preserved_runs[{index}]")
        entry_source = _require_string(
            entry,
            "source_run_directory_path",
            "run-family preserved run",
        )
        if _same_path(entry_source, source_path):
            return entry
    return None


def _find_authority_candidate(
    authority: Mapping[str, Any],
    source_path: str,
) -> Mapping[str, Any] | None:
    entries = _require_list(authority, "candidate_runs", "authority resolution")
    for index, value in enumerate(entries):
        entry = _require_mapping(value, f"authority resolution.candidate_runs[{index}]")
        entry_source = _require_string(
            entry,
            "source_run_directory_path",
            "authority candidate run",
        )
        if _same_path(entry_source, source_path):
            return entry
    return None


def _all_core_execution_files_match(artifacts: Mapping[str, Any]) -> bool:
    cores = {
        _core_execution_file(artifacts["authority"], "authority resolution"),
        _core_execution_file(artifacts["family"], "run-family packet"),
        _core_execution_file(artifacts["status"], "preserved-run status packet"),
        _core_execution_file(artifacts["governing"], "current-governing packet"),
    }
    return len(cores) == 1


def _core_execution_file(packet: Mapping[str, Any], label: str) -> str:
    canonical = _require_mapping(packet, "canonical_execution_line", label)
    return _require_string(canonical, "core_execution_file", f"{label}.canonical_execution_line")


def _non_claims(artifacts: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for label in ("authority", "family", "status", "governing"):
        artifact = _require_mapping(artifacts, label, "artifacts")
        incoming = _require_mapping(artifact, "non_claims", f"{label} artifact")
        for key in NON_CLAIM_DEFAULTS:
            if key in incoming:
                value = _require_bool(incoming, key, f"{label}.non_claims")
                if value is not False:
                    raise GoverningTransitionResolutionError(
                        f"{label}.non_claims.{key} must remain false"
                    )
                non_claims[key] = False
    return non_claims


def _source_run_readable(path_text: str) -> bool:
    path = _resolve_path_text(path_text, base_dir=_repo_root())
    return path.exists() and path.is_dir() and (path / "manifest.json").is_file()


def _ingress_run_readable(path_text: str) -> bool:
    path = _resolve_path_text(path_text, base_dir=_repo_root())
    return path.exists() and path.is_dir() and (path / "manifest.json").is_file()


def _file_readable(path_text: str) -> bool:
    path = _resolve_path_text(path_text, base_dir=_repo_root())
    return path.exists() and path.is_file()


def _proposal_replay_request(proposal: Mapping[str, Any]) -> bool:
    return _proposal_flag_true(proposal, ("requires_replay", "replayed_into_live_host"))


def _proposal_merge_request(proposal: Mapping[str, Any]) -> bool:
    return _proposal_flag_true(proposal, ("requires_merge", "merged_into_local_state"))


def _proposal_continuity_completion_request(proposal: Mapping[str, Any]) -> bool:
    return _proposal_flag_true(proposal, ("continuity_completed",))


def _proposal_standing_upgrade_request(proposal: Mapping[str, Any]) -> bool:
    return _proposal_flag_true(proposal, ("standing_upgraded",))


def _proposal_flag_true(proposal: Mapping[str, Any], keys: tuple[str, ...]) -> bool:
    for key in keys:
        value = proposal.get(key)
        if value is True:
            return True
        if isinstance(value, str) and value.strip().lower() in {"true", "yes", "1"}:
            return True
    return False


def _contains_inference_text(proposal: Mapping[str, str], marker: str) -> bool:
    marker_text = marker.lower()
    haystack = " ".join(
        (
            proposal.get("proposal_basis_ref", ""),
            proposal.get("proposed_by_surface", ""),
        )
    ).lower().replace("-", "_").replace(" ", "_")
    return marker_text in haystack


def _transition_result_id(proposal: Mapping[str, str]) -> str:
    return f"{proposal['transition_proposal_id']}__governing_transition_result"


def _next_default_result_path(result: Mapping[str, Any]) -> Path:
    metadata = _require_mapping(result, "result_metadata", "transition result")
    result_id = _require_string(
        metadata,
        "transition_result_id",
        "transition result.result_metadata",
    )
    stem = _safe_filename(result_id)
    return _next_available_path(_repo_root() / GOVERNING_TRANSITION_RESULT_ROOT, stem)


def _next_available_path(root: Path, stem: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    first = root / f"{stem}.json"
    if not first.exists():
        return first
    index = 1
    while True:
        candidate = root / f"{stem}_{index:03d}.json"
        if not candidate.exists():
            return candidate
        index += 1


def _safe_filename(value: str) -> str:
    cleaned = "".join(
        char if char.isalnum() or char in {"-", "_", "."} else "_"
        for char in value.strip()
    ).strip("._")
    return cleaned or "governing_transition_result"


def _require_directory(root: Path, label: str) -> Path:
    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise GoverningTransitionResolutionError(
            f"{label.title()} does not exist: {_display_path(root_path)}"
        )
    if not root_path.is_dir():
        raise GoverningTransitionResolutionError(
            f"{label.title()} is not a directory: {_display_path(root_path)}"
        )
    return root_path


def _require_matching_paths(values: tuple[Any, ...], label: str) -> None:
    present = [value for value in values if value is not None]
    if not present:
        raise GoverningTransitionResolutionError(f"Missing {label}")
    first = present[0]
    if any(not _same_path(first, value) for value in present[1:]):
        raise GoverningTransitionResolutionError(f"Artifact mismatch for {label}")


def _same_path(left: str | Path, right: str | Path) -> bool:
    return _resolve_path_text(str(left), base_dir=_repo_root()) == _resolve_path_text(
        str(right),
        base_dir=_repo_root(),
    )


def _resolve_path_text(path_text: str, *, base_dir: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()
    return (base_dir / path).resolve()


def _repo_root() -> Path:
    return Path.cwd().resolve()


def _repo_relative_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (_repo_root() / path).resolve()


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00",
        "Z",
    )


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return _display_path(value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _require_mapping(
    value: Any,
    key: str,
    context: str | None = None,
) -> Mapping[str, Any]:
    if context is None:
        if not isinstance(value, Mapping):
            raise GoverningTransitionResolutionError(f"{key} must be a mapping")
        return value
    if not isinstance(value, Mapping):
        raise GoverningTransitionResolutionError(f"{context} must be a mapping")
    item = value.get(key)
    if not isinstance(item, Mapping):
        raise GoverningTransitionResolutionError(f"{context}.{key} must be a mapping")
    return item


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise GoverningTransitionResolutionError(f"{context}.{key} must be a list")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise GoverningTransitionResolutionError(
            f"{context}.{key} must be a non-empty string"
        )
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise GoverningTransitionResolutionError(f"{context}.{key} must be a boolean")
    return value
