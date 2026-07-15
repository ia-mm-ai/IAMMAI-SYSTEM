"""Resolve bounded current self-orientation with post-carrier receipt posture.

This lineage-preserving successor keeps the v6 self-orientation model and adds
only the post-v6 standing surfaces that now need to be mirrored:
post-conformance closure, cross-surface correspondence, local cross-carrier
receipt, and returned physical Carrier B receipt evidence.

The resolver recognizes those surfaces as downstream posture only. It does not
replay the host, merge preserved runs, mutate upstream artifacts, infer
currentness by latest-file recency, create authority, create permission, create
currentness, create a signal, establish presence, meet threshold, create truth,
authorize action or continuation, create multi-carrier law, create distributed
standing, or treat Carrier B as source, currentness, authority, successor, body,
or standing participant.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class CurrentSelfOrientationV7Error(RuntimeError):
    """Raised for malformed selected inputs or impossible correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_inputs: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_inputs = (
            copy.deepcopy(dict(selected_inputs))
            if isinstance(selected_inputs, Mapping)
            else None
        )
        self.checks = [copy.deepcopy(dict(check)) for check in checks or []]


REPO_ROOT = Path(__file__).resolve().parents[1]

CURRENT_SELF_ORIENTATION_V6_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)
CURRENT_SELF_ORIENTATION_V7_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v7"
)
CURRENT_BODY_CONFORMANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass"
)
POST_CONFORMANCE_CLOSURE_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_standing_closure_post_conformance"
)
CROSS_SURFACE_CORRESPONDENCE_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_surface_correspondence_boundary"
)
CROSS_CARRIER_SURFACE_RECEIPT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_surface_receipt_boundary"
)
RETURNED_CARRIER_B_RECEIPT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_surface_receipt_boundary"
    / "returned_from_carrier_B"
)
CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)
BODY_SIGNAL_RECOGNITION_V2_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition_v2"
)
BODY_SIGNAL_ACCEPTANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance"
)
BODY_SIGNAL_SCOPE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_scope"
)
DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_derivative_vessel_relation_boundary"
)
OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT = (
    REPO_ROOT / "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = (
    REPO_ROOT / "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v7"
SUCCESSOR_OF_MODULE = "resolve_current_self_orientation_v6"
CURRENT_SELF_ORIENTATION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V7_RESULT"
)
CURRENT_SELF_ORIENTATION_RESULT_VERSION = "0.7.0"
DEFAULT_RESULT_STEM = "current_self_orientation_v7_result"

OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_BODY_CONFORMANT = "BODY_CONFORMANT"
OUTCOME_CONFORMANCE_CLOSURE_RECORDED = "CONFORMANCE_CLOSURE_RECORDED"
OUTCOME_CORRESPONDENCE_RECOGNIZED = "CORRESPONDENCE_RECOGNIZED"
OUTCOME_CARRIED_SURFACE_RECEIVED = "CARRIED_SURFACE_RECEIVED"

BLOCK_REASONS = {
    "SELF_ORIENTATION_V6_MISSING": "No current self-orientation v6 basis is available.",
    "SELF_ORIENTATION_V6_UNREADABLE": "The selected current self-orientation v6 artifact could not be read.",
    "SELF_ORIENTATION_V6_MALFORMED": "The selected current self-orientation v6 artifact is malformed.",
    "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED": "The selected current self-orientation v6 result is not SELF_ORIENTED.",
    "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED": "The inherited current/governing basis is not recognized.",
    "CURRENT_BODY_CONFORMANCE_MISSING": "No matching current-body conformance result is available.",
    "CURRENT_BODY_CONFORMANCE_MALFORMED": "A current-body conformance artifact is malformed.",
    "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT": "The selected current-body conformance result is not BODY_CONFORMANT.",
    "POST_CONFORMANCE_CLOSURE_MISSING": "No matching post-conformance closure result is available.",
    "POST_CONFORMANCE_CLOSURE_MALFORMED": "A post-conformance closure artifact is malformed.",
    "POST_CONFORMANCE_CLOSURE_NOT_RECORDED": "The selected post-conformance closure result is not recorded.",
    "CONFORMANCE_CLOSURE_PERMISSION_LEAK": "Post-conformance closure leaked permission.",
    "CONFORMANCE_CLOSURE_AUTHORITY_LEAK": "Post-conformance closure leaked authority.",
    "CONFORMANCE_CLOSURE_SIGNAL_LEAK": "Post-conformance closure leaked signal posture.",
    "CONFORMANCE_CLOSURE_CONTINUATION_LEAK": "Post-conformance closure opened continuation or next work.",
    "CROSS_SURFACE_CORRESPONDENCE_MISSING": "A required cross-surface correspondence result is unavailable.",
    "CROSS_SURFACE_CORRESPONDENCE_MALFORMED": "A cross-surface correspondence artifact is malformed.",
    "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED": "A selected cross-surface correspondence result is not recognized.",
    "CROSS_SURFACE_CORRESPONDENCE_COLLAPSE_LEAK": "Cross-surface correspondence leaked collapse posture.",
    "CROSS_CARRIER_RECEIPT_MISSING": "No local cross-carrier surface receipt result is available.",
    "CROSS_CARRIER_RECEIPT_MALFORMED": "A cross-carrier receipt artifact is malformed.",
    "CROSS_CARRIER_RECEIPT_NOT_RECEIVED": "The selected local cross-carrier receipt was not received.",
    "RETURNED_CARRIER_RECEIPT_MISSING": "No returned Carrier B successful receipt result is available.",
    "RETURNED_CARRIER_RECEIPT_NOT_RECEIVED": "The returned Carrier B receipt was not received.",
    "RETURNED_CARRIER_REFUSAL_NOT_VISIBLE": "Returned Carrier B blocked receipt evidence is not visible.",
    "RECEIPT_ALIGNMENT_CORRESPONDENCE_MISSING": "Receipt-alignment correspondence is unavailable.",
    "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED": "Receipt-alignment correspondence is not recognized.",
    "REFUSAL_VISIBLE_CORRESPONDENCE_MISSING": "Refusal-visible correspondence is unavailable.",
    "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED": "Refusal-visible correspondence is not recognized.",
    "RECEIVING_CARRIER_SOURCE_LEAK": "Receiving carrier was treated as source.",
    "RECEIVING_CARRIER_CURRENTNESS_LEAK": "Receiving carrier was treated as currentness.",
    "RECEIVING_CARRIER_AUTHORITY_LEAK": "Receiving carrier was treated as authority.",
    "RECEIVING_CARRIER_SUCCESSOR_LEAK": "Receiving carrier was treated as successor or body.",
    "CARRIED_SURFACE_SOURCE_OR_CURRENTNESS_LEAK": "Carried surface was treated as source or currentness.",
    "CARRIED_SURFACE_PERMISSION_OR_SIGNAL_LEAK": "Carried surface was treated as permission or signal.",
    "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK": "Receipt leaked presence, threshold, truth, action, or consequence.",
    "RECEIPT_MULTI_CARRIER_OR_DISTRIBUTED_STANDING_LEAK": "Receipt leaked multi-carrier law or distributed standing.",
    "RETURNED_EVIDENCE_REPLACED_SOURCE": "Returned evidence replaced local source posture.",
    "RETURNED_EVIDENCE_CREATED_CURRENTNESS": "Returned evidence created currentness.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required carried non-claim is missing or no longer false.",
    "LATEST_FILE_CURRENTNESS_REFUSED": "Currentness inferred by latest-file recency alone is refused.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
}

NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "continuity_completed": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "standing_upgraded": False,
    "source_replaced": False,
    "source_scope_widened": False,
    "derivative_upgraded_to_source": False,
    "derivative_outputs_upgraded_to_source": False,
    "operator_upgraded_to_source": False,
    "operator_outputs_upgraded_to_source": False,
    "reentry_admissibility_became_authority": False,
    "receipt_became_authority": False,
    "signal_recognition_became_authority": False,
    "signal_acceptance_became_authority": False,
    "signal_scope_became_authority": False,
    "signal_surface_became_current_or_governing_basis": False,
    "general_permission_created": False,
    "follow_on_steps_authorized": False,
    "follow_on_work_authorized": False,
    "admission_reusable": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "roadmap_created": False,
    "workflow_engine_created": False,
    "workflow_created": False,
    "signal_router_created": False,
    "event_bus_created": False,
    "body_relevance_medium_created": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "consequence_created": False,
    "applied_outside_declared_scope": False,
    "source_derivative_operator_collapsed": False,
    "derivative_vessel_relation_became_authority": False,
    "derivative_vessel_relation_became_currentness": False,
    "derivative_vessel_relation_became_permission": False,
    "derivative_vessel_relation_became_current_or_governing_basis": False,
    "derivative_vessel_relation_created_adoption": False,
    "derivative_vessel_relation_created_privileged_standing": False,
    "derivative_vessel_relation_created_public_release": False,
    "derivative_vessel_relation_replaced_source": False,
    "derivative_vessel_relation_completed_final_governance": False,
    "derivative_vessel_relation_completed_final_system_identity": False,
    "derivative_vessel_relation_completed_continuity": False,
    "derivative_vessel_relation_created_general_vessel_permission": False,
    "derivative_vessel_relation_authorized_follow_on_vessels": False,
    "conformance_became_authority": False,
    "conformance_became_permission": False,
    "conformance_became_currentness": False,
    "conformance_became_signal": False,
    "conformance_became_presence": False,
    "conformance_became_threshold": False,
    "conformance_became_truth": False,
    "conformance_became_action": False,
    "conformance_became_completion": False,
    "conformance_authorized_next_step": False,
    "conformance_became_signal_by_default": False,
    "conformance_opened_continuation": False,
    "closure_became_authority": False,
    "closure_became_permission": False,
    "closure_became_signal": False,
    "closure_authorized_next_work": False,
    "closure_forced_self_orientation_successor": False,
    "self_orientation_successor_forced": False,
    "conformance_successor_forced": False,
    "correspondence_became_authority": False,
    "correspondence_became_currentness": False,
    "correspondence_became_permission": False,
    "correspondence_became_signal": False,
    "correspondence_became_presence": False,
    "correspondence_became_threshold": False,
    "correspondence_became_truth": False,
    "correspondence_became_action": False,
    "correspondence_became_consequence": False,
    "correspondence_authorized_continuation": False,
    "correspondence_forced_self_orientation_successor": False,
    "correspondence_forced_conformance_successor": False,
    "signal_created_by_default": False,
    "surface_merged": False,
    "surface_equivalence_created": False,
    "explanation_ownership_created": False,
    "receipt_became_authority": False,
    "receipt_became_currentness": False,
    "receipt_became_source": False,
    "receipt_became_permission": False,
    "receipt_became_signal": False,
    "receipt_became_presence": False,
    "receipt_became_threshold": False,
    "receipt_became_truth": False,
    "receipt_became_action": False,
    "receipt_became_consequence": False,
    "receipt_authorized_continuation": False,
    "receipt_created_multi_carrier_law": False,
    "receipt_created_distributed_standing": False,
    "receiving_carrier_became_source": False,
    "receiving_carrier_became_current": False,
    "receiving_carrier_became_authority": False,
    "receiving_carrier_became_successor": False,
    "receiving_carrier_became_body": False,
    "carrier_b_became_source": False,
    "carrier_b_became_currentness": False,
    "carrier_b_became_authority": False,
    "carrier_b_became_successor": False,
    "carrier_b_became_body": False,
    "carried_surface_became_source": False,
    "carried_surface_became_currentness": False,
    "carried_surface_became_permission": False,
    "carried_surface_became_signal_by_default": False,
    "carrier_merge_performed": False,
    "local_copy_currentness": False,
    "source_body_replayed": False,
    "upstream_mechanisms_run": False,
    "continuation_authorized": False,
    "multi_carrier_law_created": False,
    "distributed_standing_created": False,
    "returned_evidence_replaced_source": False,
    "returned_evidence_created_currentness": False,
    "self_orientation_became_authority": False,
}

SUMMARY_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "source_derivative_operator_collapsed",
    "conformance_became_authority",
    "conformance_became_permission",
    "conformance_became_currentness",
    "closure_became_authority",
    "closure_became_permission",
    "closure_became_signal",
    "correspondence_became_authority",
    "correspondence_became_currentness",
    "correspondence_became_permission",
    "signal_created_by_default",
    "receiving_carrier_became_source",
    "receiving_carrier_became_current",
    "receiving_carrier_became_authority",
    "receiving_carrier_became_successor",
    "receiving_carrier_became_body",
    "carried_surface_became_source",
    "carried_surface_became_currentness",
    "carried_surface_became_permission",
    "carried_surface_became_signal_by_default",
    "multi_carrier_law_created",
    "distributed_standing_created",
    "returned_evidence_replaced_source",
    "returned_evidence_created_currentness",
)

METADATA_ID_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_id"),
    ("current_body_conformance_metadata", "current_body_conformance_result_id"),
    ("conformance_closure_metadata", "conformance_closure_result_id"),
    ("cross_surface_correspondence_metadata", "cross_surface_correspondence_result_id"),
    (
        "cross_carrier_surface_receipt_metadata",
        "cross_carrier_surface_receipt_result_id",
    ),
    ("body_signal_recognition_metadata", "body_signal_recognition_result_id"),
    ("body_signal_acceptance_metadata", "body_signal_acceptance_result_id"),
    ("body_signal_scope_metadata", "body_signal_scope_result_id"),
    (
        "derivative_vessel_relation_boundary_metadata",
        "derivative_vessel_relation_boundary_result_id",
    ),
)

METADATA_TYPE_PATHS = (
    ("current_self_orientation_v6_metadata", "self_orientation_result_type"),
    ("current_body_conformance_metadata", "current_body_conformance_result_type"),
    ("conformance_closure_metadata", "conformance_closure_result_type"),
    ("cross_surface_correspondence_metadata", "cross_surface_correspondence_result_type"),
    (
        "cross_carrier_surface_receipt_metadata",
        "cross_carrier_surface_receipt_result_type",
    ),
    ("body_signal_recognition_metadata", "body_signal_recognition_result_type"),
    ("body_signal_acceptance_metadata", "body_signal_acceptance_result_type"),
    ("body_signal_scope_metadata", "body_signal_scope_result_type"),
    (
        "derivative_vessel_relation_boundary_metadata",
        "derivative_vessel_relation_boundary_result_type",
    ),
)


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    candidate = Path(path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return candidate.as_posix()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _nested(mapping: Mapping[str, Any] | None, *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _string_or_none(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None


def _safe_filename_part(value: Any) -> str:
    text = value if isinstance(value, str) and value else DEFAULT_RESULT_STEM
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("._")
    return text[:180] or DEFAULT_RESULT_STEM


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "Bounded current self-orientation refused.")
    if detail:
        return f"{reason} {detail}"
    return reason


def _check(
    check_name: str,
    passed: bool,
    *,
    expected: Any,
    actual: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _all_checks_passed(checks: Sequence[Any]) -> bool:
    return bool(checks) and all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def _read_json_mapping(
    path: Path | str,
    *,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    target = _repo_path(path)
    if not target.is_file():
        raise CurrentSelfOrientationV7Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        )
    try:
        with target.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationV7Error(
            f"required JSON artifact is malformed: {_display_path(target)}",
            malformed_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationV7Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CurrentSelfOrientationV7Error(
            f"required JSON artifact is not an object: {_display_path(target)}",
            malformed_code,
        )
    return copy.deepcopy(dict(loaded))


def _iter_json_artifacts(
    root: Path | str,
    *,
    malformed_code: str,
    recursive: bool = False,
) -> list[tuple[Path, dict[str, Any]]]:
    resolved = _repo_path(root)
    if not resolved.exists() or not resolved.is_dir():
        return []
    pattern = "**/*.json" if recursive else "*.json"
    artifacts: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(resolved.glob(pattern)):
        if not path.is_file():
            continue
        artifacts.append(
            (
                path,
                _read_json_mapping(
                    path,
                    unreadable_code=malformed_code,
                    malformed_code=malformed_code,
                ),
            )
        )
    return artifacts


def _latest_artifact(
    candidates: Sequence[tuple[Path, Mapping[str, Any]]],
) -> tuple[Path, dict[str, Any]] | None:
    if not candidates:
        return None
    path, data = max(
        candidates,
        key=lambda item: (
            item[0].stat().st_mtime if item[0].exists() else 0.0,
            item[0].as_posix(),
        ),
    )
    return path, copy.deepcopy(dict(data))


def _result_id(artifact: Mapping[str, Any] | None) -> str | None:
    if not isinstance(artifact, Mapping):
        return None
    for key in ("result_id", "surface_id"):
        if _string_or_none(artifact.get(key)):
            return str(artifact[key])
    for metadata_key, id_key in METADATA_ID_PATHS:
        value = _nested(artifact, metadata_key, id_key)
        if _string_or_none(value):
            return str(value)
    found = _find_first_key_value(
        artifact,
        lambda key: key.endswith("_result_id") or key.endswith("_surface_id"),
    )
    return str(found) if _string_or_none(found) else None


def _result_type(artifact: Mapping[str, Any] | None) -> str | None:
    if not isinstance(artifact, Mapping):
        return None
    for key in ("result_type", "surface_type"):
        if _string_or_none(artifact.get(key)):
            return str(artifact[key])
    for metadata_key, type_key in METADATA_TYPE_PATHS:
        value = _nested(artifact, metadata_key, type_key)
        if _string_or_none(value):
            return str(value)
    found = _find_first_key_value(artifact, lambda key: key.endswith("_result_type"))
    return str(found) if _string_or_none(found) else None


def _result_version(artifact: Mapping[str, Any] | None) -> str | None:
    if not isinstance(artifact, Mapping):
        return None
    for key, value in _walk_items(artifact):
        if key.endswith("_result_version") and _string_or_none(value):
            return str(value)
    return None


def _resolver_or_runner(artifact: Mapping[str, Any] | None) -> str | None:
    if not isinstance(artifact, Mapping):
        return None
    for key, value in _walk_items(artifact):
        if key in {"resolver_module", "runner_module"} and _string_or_none(value):
            return str(value)
    return None


def _artifact_ref(
    artifact: Mapping[str, Any] | None,
    path: Path | str | None,
    selection_mode: str,
    *,
    result_family: str,
) -> dict[str, Any]:
    block = _as_mapping(artifact.get("block")) if isinstance(artifact, Mapping) else {}
    return {
        "result_id": _result_id(artifact),
        "result_path": _display_path(path) if path is not None else None,
        "result_type": _result_type(artifact),
        "result_version": _result_version(artifact),
        "resolver_or_runner_module": _resolver_or_runner(artifact),
        "result_family": result_family,
        "outcome": artifact.get("outcome") if isinstance(artifact, Mapping) else None,
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "selection_mode": selection_mode,
    }


def _selected_v6_from_conformance(result: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    return {
        "result_id": (
            _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "result_id")
            or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_result_id")
            or _nested(result, "current_body_conformance_summary", "selected_self_orientation_v6_id")
        ),
        "result_path": (
            _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "result_path")
            or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_result_path")
            or _nested(result, "current_body_conformance_summary", "selected_self_orientation_v6_path")
        ),
        "outcome": (
            _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "outcome")
            or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_outcome")
            or _nested(result, "current_body_conformance_summary", "selected_self_orientation_v6_outcome")
        ),
    }


def _selected_v6_from_closure(result: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    basis = _as_mapping(result.get("selected_self_orientation_v6_basis"))
    summary = _as_mapping(result.get("current_body_standing_closure_summary"))
    return {
        "result_id": basis.get("self_orientation_result_id")
        or summary.get("selected_self_orientation_v6_id"),
        "result_path": basis.get("result_path")
        or summary.get("selected_self_orientation_v6_path"),
        "outcome": basis.get("outcome")
        or summary.get("selected_self_orientation_v6_outcome"),
    }


def _selected_conformance_from_closure(result: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    basis = _as_mapping(result.get("selected_current_body_conformance_basis"))
    summary = _as_mapping(result.get("current_body_standing_closure_summary"))
    return {
        "result_id": basis.get("current_body_conformance_result_id")
        or summary.get("selected_conformance_id"),
        "result_path": basis.get("result_path")
        or summary.get("selected_conformance_path"),
        "outcome": basis.get("outcome")
        or summary.get("selected_conformance_outcome"),
    }


def _identity_corresponds(
    selected: Mapping[str, Any],
    exposed: Mapping[str, Any],
) -> bool:
    comparisons: list[bool] = []
    selected_id = _string_or_none(selected.get("result_id"))
    exposed_id = _string_or_none(exposed.get("result_id"))
    if selected_id and exposed_id:
        comparisons.append(selected_id == exposed_id)
    selected_path = _string_or_none(selected.get("result_path"))
    exposed_path = _string_or_none(exposed.get("result_path"))
    if selected_path and exposed_path:
        comparisons.append(
            selected_path == exposed_path
            or _display_path(selected_path) == _display_path(exposed_path)
        )
    return all(comparisons) if comparisons else True


def _select_v6(
    v6_result: Mapping[str, Any] | None,
    v6_result_path: Path | str | None,
) -> tuple[Path | None, dict[str, Any] | None, str]:
    if v6_result_path is not None:
        path = _repo_path(v6_result_path)
        data = _read_json_mapping(
            path,
            unreadable_code="SELF_ORIENTATION_V6_UNREADABLE",
            malformed_code="SELF_ORIENTATION_V6_MALFORMED",
        )
        return path, data, "explicit_current_self_orientation_v6_result_path"
    if v6_result is not None:
        if not isinstance(v6_result, Mapping):
            raise CurrentSelfOrientationV7Error(
                "current self-orientation v6 input must be a mapping",
                "SELF_ORIENTATION_V6_MALFORMED",
            )
        return None, copy.deepcopy(dict(v6_result)), "mapping_supplied_current_self_orientation_v6"

    candidates = [
        (path, data)
        for path, data in _iter_json_artifacts(
            CURRENT_SELF_ORIENTATION_V6_ROOT,
            malformed_code="SELF_ORIENTATION_V6_MALFORMED",
        )
        if data.get("outcome") == OUTCOME_SELF_ORIENTED
    ]
    selected = _latest_artifact(candidates)
    if selected is None:
        return None, None, "successful_self_orientation_v6_discovery"
    path, data = selected
    return path, data, "successful_self_orientation_v6_discovery"


def _select_conformance(
    v6_identity: Mapping[str, Any],
) -> tuple[Path | None, dict[str, Any] | None, str]:
    candidates = [
        (path, data)
        for path, data in _iter_json_artifacts(
            CURRENT_BODY_CONFORMANCE_ROOT,
            malformed_code="CURRENT_BODY_CONFORMANCE_MALFORMED",
        )
        if data.get("outcome") == OUTCOME_BODY_CONFORMANT
        and _identity_corresponds(v6_identity, _selected_v6_from_conformance(data))
    ]
    selected = _latest_artifact(candidates)
    if selected is None:
        return None, None, "matching_body_conformant_conformance_discovery"
    path, data = selected
    return path, data, "matching_body_conformant_conformance_discovery"


def _select_closure(
    v6_identity: Mapping[str, Any],
    conformance_identity: Mapping[str, Any],
) -> tuple[Path | None, dict[str, Any] | None, str]:
    candidates = [
        (path, data)
        for path, data in _iter_json_artifacts(
            POST_CONFORMANCE_CLOSURE_ROOT,
            malformed_code="POST_CONFORMANCE_CLOSURE_MALFORMED",
        )
        if data.get("outcome") == OUTCOME_CONFORMANCE_CLOSURE_RECORDED
        and _identity_corresponds(v6_identity, _selected_v6_from_closure(data))
        and _identity_corresponds(
            conformance_identity,
            _selected_conformance_from_closure(data),
        )
    ]
    selected = _latest_artifact(candidates)
    if selected is None:
        return None, None, "matching_post_conformance_closure_discovery"
    path, data = selected
    return path, data, "matching_post_conformance_closure_discovery"


def _select_correspondence(
    correspondence_type: str,
    *,
    selected_surface_outcomes: set[str] | None = None,
) -> tuple[Path | None, dict[str, Any] | None, str]:
    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path, data in _iter_json_artifacts(
        CROSS_SURFACE_CORRESPONDENCE_ROOT,
        malformed_code="CROSS_SURFACE_CORRESPONDENCE_MALFORMED",
    ):
        basis = _as_mapping(data.get("correspondence_basis"))
        outcomes = {
            str(outcome)
            for outcome in basis.get("selected_surface_outcomes", [])
            if isinstance(outcome, str)
        }
        if data.get("outcome") != OUTCOME_CORRESPONDENCE_RECOGNIZED:
            continue
        if basis.get("correspondence_type") != correspondence_type:
            continue
        if selected_surface_outcomes is not None and not selected_surface_outcomes.issubset(outcomes):
            continue
        candidates.append((path, data))
    selected = _latest_artifact(candidates)
    if selected is None:
        return None, None, f"{correspondence_type.lower()}_correspondence_discovery"
    path, data = selected
    return path, data, f"{correspondence_type.lower()}_correspondence_discovery"


def _select_receipt(
    root: Path,
    outcome: str,
    selection_mode: str,
) -> tuple[Path | None, dict[str, Any] | None, str]:
    candidates = [
        (path, data)
        for path, data in _iter_json_artifacts(
            root,
            malformed_code="CROSS_CARRIER_RECEIPT_MALFORMED",
        )
        if data.get("outcome") == outcome
    ]
    selected = _latest_artifact(candidates)
    if selected is None:
        return None, None, selection_mode
    path, data = selected
    return path, data, selection_mode


def _failed_check_count(
    artifact: Mapping[str, Any] | None,
    summary_key: str,
    checks_key: str,
) -> int | None:
    if not isinstance(artifact, Mapping):
        return None
    summary_count = _nested(artifact, summary_key, "failed_check_count")
    if isinstance(summary_count, int):
        return summary_count
    checks = _mapping_list(artifact.get(checks_key))
    if checks:
        return sum(1 for check in checks if check.get("passed") is not True)
    return None


def _passed_check_count(
    artifact: Mapping[str, Any] | None,
    summary_key: str,
    checks_key: str,
) -> int | None:
    if not isinstance(artifact, Mapping):
        return None
    summary_count = _nested(artifact, summary_key, "passed_check_count")
    if isinstance(summary_count, int):
        return summary_count
    checks = _mapping_list(artifact.get(checks_key))
    if checks:
        return sum(1 for check in checks if check.get("passed") is True)
    return None


def _section(predecessor_result: Mapping[str, Any] | None, key: str) -> dict[str, Any]:
    if not isinstance(predecessor_result, Mapping):
        return {}
    return _as_mapping(predecessor_result.get(key))


def _recognized_blocked_or_refused_surfaces(
    v6_result: Mapping[str, Any] | None,
    returned_blocked_ref: Mapping[str, Any],
) -> dict[str, Any]:
    section = _section(v6_result, "recognized_blocked_or_refused_surfaces")
    if returned_blocked_ref.get("result_id"):
        section["returned_carrier_b_blocked_receipt_refusal"] = {
            "recognition_posture": "visible_returned_physical_carrier_refusal_evidence_only",
            "selected_returned_carrier_b_blocked_receipt_result": copy.deepcopy(
                dict(returned_blocked_ref)
            ),
            "blocked_receipt_remains_refusal_evidence": True,
            "blocked_receipt_does_not_invalidate_successful_receipt": True,
            "blocked_receipt_does_not_create_source_currentness_authority_or_permission": True,
        }
    return section


def _recognized_current_body_conformance_surfaces(
    conformance_ref: Mapping[str, Any],
    conformance_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(conformance_result, Mapping):
        return {}
    summary = _as_mapping(conformance_result.get("current_body_conformance_summary"))
    basis = _as_mapping(conformance_result.get("current_body_conformance_basis"))
    integrated = _as_mapping(conformance_result.get("integrated_non_claims"))
    return {
        "recognition_posture": "downstream_integrated_current_body_conformance_audit_only",
        "selected_current_body_conformance_result": copy.deepcopy(dict(conformance_ref)),
        "selected_self_orientation_v6_basis": _selected_v6_from_conformance(conformance_result),
        "current_body_conformance_basis": basis,
        "passed_check_count": _passed_check_count(
            conformance_result,
            "current_body_conformance_summary",
            "current_body_conformance_checks",
        ),
        "failed_check_count": _failed_check_count(
            conformance_result,
            "current_body_conformance_summary",
            "current_body_conformance_checks",
        ),
        "current_governing_basis_passed": summary.get("current_governing_basis_passed"),
        "reentry_posture_passed": summary.get("reentry_posture_passed"),
        "body_signal_posture_passed": summary.get("body_signal_posture_passed"),
        "derivative_vessel_posture_passed": summary.get("derivative_vessel_posture_passed"),
        "operator_posture_passed": summary.get("operator_posture_passed"),
        "integrated_non_claims_passed": summary.get("integrated_non_claims_passed"),
        "conformance_non_claims": _as_mapping(conformance_result.get("non_claims")),
        "integrated_non_claims": integrated,
        "conformance_remains_audit_posture": True,
        "conformance_creates_no_authority": True,
        "conformance_creates_no_permission": True,
        "conformance_creates_no_currentness": True,
        "conformance_creates_no_signal": True,
        "conformance_creates_no_presence_threshold_truth_action_or_consequence": True,
        "conformance_authorizes_no_continuation": True,
        "conformance_does_not_complete_whole_body": True,
    }


def _recognized_post_conformance_closure_surfaces(
    closure_ref: Mapping[str, Any],
    closure_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(closure_result, Mapping):
        return {}
    statement = _as_mapping(closure_result.get("closure_statement"))
    summary = _as_mapping(closure_result.get("current_body_standing_closure_summary"))
    return {
        "recognition_posture": "downstream_post_conformance_meaning_closure_only",
        "selected_post_conformance_closure_result": copy.deepcopy(dict(closure_ref)),
        "selected_self_orientation_v6_basis": _selected_v6_from_closure(closure_result),
        "selected_current_body_conformance_basis": _selected_conformance_from_closure(
            closure_result
        ),
        "closure_recorded": closure_result.get("outcome")
        == OUTCOME_CONFORMANCE_CLOSURE_RECORDED,
        "conformance_question_closed": statement.get("conformance_question_closed"),
        "next_work_question_opened": statement.get("next_work_question_opened"),
        "conformance_recorded_as_permission": statement.get(
            "conformance_recorded_as_permission"
        ),
        "conformance_recorded_as_authority": statement.get(
            "conformance_recorded_as_authority"
        ),
        "conformance_recorded_as_signal": statement.get("conformance_recorded_as_signal"),
        "self_orientation_successor_forced": statement.get(
            "self_orientation_successor_forced"
        ),
        "passed_check_count": summary.get("passed_check_count"),
        "failed_check_count": summary.get("failed_check_count"),
        "closure_non_claims": _as_mapping(closure_result.get("non_claims")),
        "closure_remains_meaning_closure": True,
        "closure_creates_no_authority_permission_signal_or_continuation": True,
    }


def _correspondence_public(
    ref: Mapping[str, Any],
    result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    basis = _as_mapping(result.get("correspondence_basis"))
    summary = _as_mapping(result.get("cross_surface_correspondence_summary"))
    correspondence = _as_mapping(result.get("correspondence_result"))
    return {
        "selected_correspondence_result": copy.deepcopy(dict(ref)),
        "declared_correspondence_question": result.get("declared_correspondence_question"),
        "correspondence_type": basis.get("correspondence_type"),
        "selected_surface_ids": basis.get("selected_surface_ids"),
        "selected_surface_outcomes": basis.get("selected_surface_outcomes"),
        "passed_check_count": summary.get("passed_check_count"),
        "failed_check_count": summary.get("failed_check_count"),
        "rank_preserved": summary.get("rank_preserved"),
        "source_preserved": summary.get("source_preserved"),
        "scope_preserved": summary.get("scope_preserved"),
        "lineage_preserved": summary.get("lineage_preserved"),
        "non_claims_preserved": summary.get("non_claims_preserved"),
        "correspondence_recognized": correspondence.get("correspondence_recognized")
        is True,
        "no_correspondence": correspondence.get("no_correspondence") is True,
        "correspondence_evidence": correspondence.get("evidence"),
        "key_non_claims": summary.get("key_non_claims"),
    }


def _recognized_cross_surface_correspondence_surfaces(
    closure_alignment_ref: Mapping[str, Any],
    closure_alignment_result: Mapping[str, Any] | None,
    receipt_alignment_ref: Mapping[str, Any],
    receipt_alignment_result: Mapping[str, Any] | None,
    refusal_visible_ref: Mapping[str, Any],
    refusal_visible_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return {
        "recognition_posture": "bounded_cross_surface_reading_relation_downstream_only",
        "selected_closure_alignment_correspondence": _correspondence_public(
            closure_alignment_ref,
            closure_alignment_result,
        ),
        "selected_receipt_alignment_correspondence": _correspondence_public(
            receipt_alignment_ref,
            receipt_alignment_result,
        ),
        "selected_refusal_visible_correspondence": _correspondence_public(
            refusal_visible_ref,
            refusal_visible_result,
        ),
        "correspondence_creates_no_authority": True,
        "correspondence_creates_no_currentness": True,
        "correspondence_creates_no_permission": True,
        "correspondence_creates_no_signal": True,
        "correspondence_establishes_no_presence_threshold_truth_action_or_consequence": True,
        "correspondence_forces_no_self_orientation_successor": True,
        "correspondence_forces_no_conformance_successor": True,
        "correspondence_authorizes_no_continuation": True,
        "correspondence_remains_downstream_and_non_authoritative": True,
    }


def _receipt_public(
    ref: Mapping[str, Any],
    result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    statement = _as_mapping(result.get("receipt_statement"))
    summary = _as_mapping(result.get("cross_carrier_surface_receipt_summary"))
    return {
        "selected_receipt_result": copy.deepcopy(dict(ref)),
        "source_carrier_basis": _as_mapping(result.get("source_carrier_basis")),
        "receiving_carrier_basis": _as_mapping(result.get("receiving_carrier_basis")),
        "carried_surface_basis": _as_mapping(result.get("carried_surface_basis")),
        "carried_surface_integrity_check": _as_mapping(
            result.get("carried_surface_integrity_check")
        ),
        "receipt_statement": statement,
        "passed_check_count": summary.get("passed_check_count"),
        "failed_check_count": summary.get("failed_check_count"),
        "carried_surface_received": statement.get("carried_surface_received"),
        "received_as_carried_evidence": statement.get("received_as_carried_evidence"),
        "source_carrier_preserved": statement.get("source_carrier_preserved"),
        "receiving_carrier_declared": statement.get("receiving_carrier_declared"),
        "receiving_carrier_became_source": statement.get("receiving_carrier_became_source"),
        "receiving_carrier_became_current": statement.get("receiving_carrier_became_current"),
        "receiving_carrier_became_authority": statement.get("receiving_carrier_became_authority"),
        "receiving_carrier_became_successor": statement.get("receiving_carrier_became_successor"),
        "carried_surface_became_source": statement.get("carried_surface_became_source"),
        "carried_surface_became_currentness": statement.get("carried_surface_became_currentness"),
        "carried_surface_became_permission": statement.get("carried_surface_became_permission"),
        "receipt_created_signal_by_default": statement.get(
            "receipt_created_signal_by_default"
        ),
        "receipt_established_presence": statement.get("receipt_established_presence"),
        "receipt_established_threshold": statement.get("receipt_established_threshold"),
        "receipt_created_truth": statement.get("receipt_created_truth"),
        "receipt_authorized_action": statement.get("receipt_authorized_action"),
        "receipt_created_consequence": statement.get("receipt_created_consequence"),
        "receipt_authorized_continuation": statement.get(
            "receipt_authorized_continuation"
        ),
        "multi_carrier_law_created": statement.get("multi_carrier_law_created"),
        "distributed_standing_created": statement.get("distributed_standing_created"),
        "key_non_claims": summary.get("key_non_claims"),
    }


def _recognized_cross_carrier_receipt_surfaces(
    local_receipt_ref: Mapping[str, Any],
    local_receipt_result: Mapping[str, Any] | None,
    returned_blocked_ref: Mapping[str, Any],
    returned_blocked_result: Mapping[str, Any] | None,
    returned_success_ref: Mapping[str, Any],
    returned_success_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return {
        "recognition_posture": "cross_carrier_receipt_evidence_downstream_only",
        "selected_local_cross_carrier_receipt": _receipt_public(
            local_receipt_ref,
            local_receipt_result,
        ),
        "selected_returned_carrier_b_blocked_receipt": _receipt_public(
            returned_blocked_ref,
            returned_blocked_result,
        ),
        "selected_returned_carrier_b_successful_receipt": _receipt_public(
            returned_success_ref,
            returned_success_result,
        ),
        "carrier_b_remains_physical_receiving_carrier_evidence_only": True,
        "carrier_b_became_source": False,
        "carrier_b_became_currentness": False,
        "carrier_b_became_authority": False,
        "carrier_b_became_successor": False,
        "carrier_b_became_body": False,
        "receipt_creates_no_authority": True,
        "receipt_creates_no_permission": True,
        "receipt_creates_no_currentness": True,
        "receipt_creates_no_signal": True,
        "receipt_establishes_no_presence_threshold_truth_action_or_consequence": True,
        "receipt_authorizes_no_continuation": True,
        "receipt_creates_no_multi_carrier_law": True,
        "receipt_creates_no_distributed_standing": True,
        "returned_evidence_does_not_replace_local_source": True,
        "returned_evidence_does_not_create_currentness": True,
    }


def _collect_non_claim_maps(artifact: Mapping[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(artifact, Mapping):
        return []
    maps: list[dict[str, Any]] = []
    for key, value in _walk_items(artifact):
        if key in {"non_claims", "key_non_claims", "false_non_claims"} and isinstance(
            value,
            Mapping,
        ):
            maps.append(copy.deepcopy(dict(value)))
    return maps


def _merge_non_claims(*artifacts: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for artifact in artifacts:
        for source in _collect_non_claim_maps(artifact):
            for key, value in source.items():
                if key not in merged and isinstance(value, bool):
                    merged[key] = False
                if isinstance(value, bool) and value is True:
                    merged[key] = True
    return merged


def _non_claims_all_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in NON_CLAIM_DEFAULTS)


def _conformance_flags_passed(conformance: Mapping[str, Any] | None) -> bool:
    summary = _as_mapping(conformance.get("current_body_conformance_summary")) if conformance else {}
    return all(
        summary.get(key) is True
        for key in (
            "current_governing_basis_passed",
            "reentry_posture_passed",
            "body_signal_posture_passed",
            "derivative_vessel_posture_passed",
            "operator_posture_passed",
            "integrated_non_claims_passed",
        )
    )


def _closure_statement_clear(closure: Mapping[str, Any] | None) -> dict[str, bool]:
    statement = _as_mapping(closure.get("closure_statement")) if closure else {}
    return {
        "permission_clear": statement.get("conformance_recorded_as_permission") is False,
        "authority_clear": statement.get("conformance_recorded_as_authority") is False,
        "signal_clear": statement.get("conformance_recorded_as_signal") is False,
        "continuation_clear": statement.get("next_work_question_opened") is False,
        "successor_clear": statement.get("self_orientation_successor_forced") is False,
        "question_closed": statement.get("conformance_question_closed") is True,
    }


def _correspondence_clear(correspondence: Mapping[str, Any] | None) -> bool:
    if not isinstance(correspondence, Mapping):
        return False
    summary = _as_mapping(correspondence.get("cross_surface_correspondence_summary"))
    return (
        summary.get("correspondence_recognized") is True
        and summary.get("failed_check_count") == 0
        and summary.get("source_rank_scope_lineage_non_claims_preserved") is True
        and not summary.get("correspondence_created_authority")
        and not summary.get("correspondence_created_currentness")
        and not summary.get("correspondence_created_permission")
        and not summary.get("correspondence_created_signal")
        and not summary.get("correspondence_established_presence")
        and not summary.get("correspondence_established_threshold")
        and not summary.get("correspondence_created_truth")
        and not summary.get("correspondence_authorized_action")
        and not summary.get("correspondence_created_consequence")
        and not summary.get("self_orientation_successor_forced")
        and not summary.get("conformance_successor_forced")
        and not summary.get("continuation_authorized")
    )


def _receipt_clear(receipt: Mapping[str, Any] | None, *, require_received: bool) -> bool:
    if not isinstance(receipt, Mapping):
        return False
    statement = _as_mapping(receipt.get("receipt_statement"))
    summary = _as_mapping(receipt.get("cross_carrier_surface_receipt_summary"))
    if require_received and receipt.get("outcome") != OUTCOME_CARRIED_SURFACE_RECEIVED:
        return False
    return (
        summary.get("failed_check_count") in {0, None}
        and statement.get("receiving_carrier_became_source") is False
        and statement.get("receiving_carrier_became_current") is False
        and statement.get("receiving_carrier_became_authority") is False
        and statement.get("receiving_carrier_became_successor") is False
        and statement.get("carried_surface_became_source") is False
        and statement.get("carried_surface_became_currentness") is False
        and statement.get("carried_surface_became_permission") is False
        and statement.get("receipt_created_signal_by_default") is False
        and statement.get("receipt_established_presence") is False
        and statement.get("receipt_established_threshold") is False
        and statement.get("receipt_created_truth") is False
        and statement.get("receipt_authorized_action") is False
        and statement.get("receipt_created_consequence") is False
        and statement.get("receipt_authorized_continuation") is False
        and statement.get("multi_carrier_law_created") is False
        and statement.get("distributed_standing_created") is False
    )


def _build_checks(
    *,
    v6_result: Mapping[str, Any] | None,
    conformance_result: Mapping[str, Any] | None,
    closure_result: Mapping[str, Any] | None,
    closure_alignment_result: Mapping[str, Any] | None,
    local_receipt_result: Mapping[str, Any] | None,
    returned_blocked_result: Mapping[str, Any] | None,
    returned_success_result: Mapping[str, Any] | None,
    receipt_alignment_result: Mapping[str, Any] | None,
    refusal_visible_result: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    checks = [
        *_mapping_list(v6_result.get("bounded_correspondence_checks") if v6_result else []),
    ]
    v6_summary = _as_mapping(v6_result.get("current_self_orientation_summary")) if v6_result else {}
    closure_clear = _closure_statement_clear(closure_result)
    local_receipt_statement = (
        _as_mapping(local_receipt_result.get("receipt_statement"))
        if isinstance(local_receipt_result, Mapping)
        else {}
    )
    returned_success_statement = (
        _as_mapping(returned_success_result.get("receipt_statement"))
        if isinstance(returned_success_result, Mapping)
        else {}
    )
    returned_blocked_block = (
        _as_mapping(returned_blocked_result.get("block"))
        if isinstance(returned_blocked_result, Mapping)
        else {}
    )

    checks.extend(
        [
            _check(
                "self_orientation_v6_stands",
                isinstance(v6_result, Mapping),
                expected="one current self-orientation v6 result is selected",
                actual=bool(v6_result),
                block_code="SELF_ORIENTATION_V6_MISSING",
            ),
            _check(
                "self_orientation_v6_is_self_oriented",
                (v6_result or {}).get("outcome") == OUTCOME_SELF_ORIENTED,
                expected=OUTCOME_SELF_ORIENTED,
                actual=(v6_result or {}).get("outcome"),
                block_code="SELF_ORIENTATION_V6_NOT_SELF_ORIENTED",
            ),
            _check(
                "current_governing_basis_remains_upstream_derived",
                bool(
                    v6_summary.get("current_executable_core_line_recognized")
                    and v6_summary.get("governing_effective_basis_recognized")
                    and v6_summary.get("current_state_surfaces_recognized")
                    and not v6_summary.get("latest_file_currentness")
                    and not v6_summary.get("recency_fraud")
                ),
                expected="v6 recognizes current/governing basis from upstream surfaces",
                actual={
                    "current_executable_core_line_recognized": v6_summary.get(
                        "current_executable_core_line_recognized"
                    ),
                    "governing_effective_basis_recognized": v6_summary.get(
                        "governing_effective_basis_recognized"
                    ),
                    "current_state_surfaces_recognized": v6_summary.get(
                        "current_state_surfaces_recognized"
                    ),
                    "latest_file_currentness": v6_summary.get("latest_file_currentness"),
                    "recency_fraud": v6_summary.get("recency_fraud"),
                },
                block_code="CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
            ),
            _check(
                "reentry_signal_derivative_relation_surfaces_remain_downstream",
                bool(
                    v6_summary.get("reentry_surfaces_recognized")
                    and v6_summary.get("body_signal_surfaces_recognized")
                    and v6_summary.get("derivative_vessel_relation_boundary_recognized")
                ),
                expected="v6 downstream re-entry, signal, and relation surfaces recognized",
                actual={
                    "reentry_surfaces_recognized": v6_summary.get(
                        "reentry_surfaces_recognized"
                    ),
                    "body_signal_surfaces_recognized": v6_summary.get(
                        "body_signal_surfaces_recognized"
                    ),
                    "derivative_vessel_relation_boundary_recognized": v6_summary.get(
                        "derivative_vessel_relation_boundary_recognized"
                    ),
                },
                block_code="CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
            ),
            _check(
                "current_body_conformance_result_is_body_conformant",
                isinstance(conformance_result, Mapping)
                and conformance_result.get("outcome") == OUTCOME_BODY_CONFORMANT,
                expected=OUTCOME_BODY_CONFORMANT,
                actual=(conformance_result or {}).get("outcome")
                if isinstance(conformance_result, Mapping)
                else None,
                block_code=(
                    "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT"
                    if isinstance(conformance_result, Mapping)
                    else "CURRENT_BODY_CONFORMANCE_MISSING"
                ),
            ),
            _check(
                "current_body_conformance_has_zero_failed_checks_and_posture_flags_pass",
                isinstance(conformance_result, Mapping)
                and _failed_check_count(
                    conformance_result,
                    "current_body_conformance_summary",
                    "current_body_conformance_checks",
                )
                == 0
                and _conformance_flags_passed(conformance_result),
                expected="zero failed conformance checks and all posture flags true",
                actual={
                    "failed_check_count": _failed_check_count(
                        conformance_result,
                        "current_body_conformance_summary",
                        "current_body_conformance_checks",
                    ),
                    "posture_flags_passed": _conformance_flags_passed(
                        conformance_result
                    ),
                },
                block_code="CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT",
            ),
            _check(
                "post_conformance_closure_is_recorded",
                isinstance(closure_result, Mapping)
                and closure_result.get("outcome")
                == OUTCOME_CONFORMANCE_CLOSURE_RECORDED,
                expected=OUTCOME_CONFORMANCE_CLOSURE_RECORDED,
                actual=(closure_result or {}).get("outcome")
                if isinstance(closure_result, Mapping)
                else None,
                block_code=(
                    "POST_CONFORMANCE_CLOSURE_NOT_RECORDED"
                    if isinstance(closure_result, Mapping)
                    else "POST_CONFORMANCE_CLOSURE_MISSING"
                ),
            ),
            _check(
                "post_conformance_closure_does_not_create_permission",
                closure_clear.get("permission_clear") is True,
                expected=False,
                actual=not closure_clear.get("permission_clear"),
                block_code="CONFORMANCE_CLOSURE_PERMISSION_LEAK",
            ),
            _check(
                "post_conformance_closure_does_not_create_authority",
                closure_clear.get("authority_clear") is True,
                expected=False,
                actual=not closure_clear.get("authority_clear"),
                block_code="CONFORMANCE_CLOSURE_AUTHORITY_LEAK",
            ),
            _check(
                "post_conformance_closure_does_not_create_signal",
                closure_clear.get("signal_clear") is True,
                expected=False,
                actual=not closure_clear.get("signal_clear"),
                block_code="CONFORMANCE_CLOSURE_SIGNAL_LEAK",
            ),
            _check(
                "post_conformance_closure_does_not_authorize_next_work_or_successor",
                closure_clear.get("continuation_clear") is True
                and closure_clear.get("successor_clear") is True,
                expected="no next work and no forced successor",
                actual={
                    "next_work_question_opened": not closure_clear.get(
                        "continuation_clear"
                    ),
                    "self_orientation_successor_forced": not closure_clear.get(
                        "successor_clear"
                    ),
                },
                block_code="CONFORMANCE_CLOSURE_CONTINUATION_LEAK",
            ),
            _check(
                "closure_alignment_correspondence_is_recognized_where_selected",
                _correspondence_clear(closure_alignment_result),
                expected="CLOSURE_ALIGNMENT correspondence recognized with no failed checks",
                actual=_as_mapping(
                    (closure_alignment_result or {}).get(
                        "cross_surface_correspondence_summary"
                    )
                )
                if isinstance(closure_alignment_result, Mapping)
                else None,
                block_code=(
                    "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED"
                    if isinstance(closure_alignment_result, Mapping)
                    else "CROSS_SURFACE_CORRESPONDENCE_MISSING"
                ),
            ),
            _check(
                "local_cross_carrier_receipt_is_received",
                _receipt_clear(local_receipt_result, require_received=True),
                expected=OUTCOME_CARRIED_SURFACE_RECEIVED,
                actual=(local_receipt_result or {}).get("outcome")
                if isinstance(local_receipt_result, Mapping)
                else None,
                block_code=(
                    "CROSS_CARRIER_RECEIPT_NOT_RECEIVED"
                    if isinstance(local_receipt_result, Mapping)
                    else "CROSS_CARRIER_RECEIPT_MISSING"
                ),
            ),
            _check(
                "returned_carrier_b_successful_receipt_is_received",
                _receipt_clear(returned_success_result, require_received=True),
                expected=OUTCOME_CARRIED_SURFACE_RECEIVED,
                actual=(returned_success_result or {}).get("outcome")
                if isinstance(returned_success_result, Mapping)
                else None,
                block_code=(
                    "RETURNED_CARRIER_RECEIPT_NOT_RECEIVED"
                    if isinstance(returned_success_result, Mapping)
                    else "RETURNED_CARRIER_RECEIPT_MISSING"
                ),
            ),
            _check(
                "returned_carrier_b_blocked_receipt_refusal_remains_visible",
                isinstance(returned_blocked_result, Mapping)
                and returned_blocked_result.get("outcome") == OUTCOME_BLOCKED
                and bool(returned_blocked_block.get("code") or returned_blocked_block.get("block_code")),
                expected="returned Carrier B blocked receipt remains visible as refusal evidence",
                actual={
                    "outcome": returned_blocked_result.get("outcome")
                    if isinstance(returned_blocked_result, Mapping)
                    else None,
                    "block_code": returned_blocked_block.get("code")
                    or returned_blocked_block.get("block_code"),
                },
                block_code="RETURNED_CARRIER_REFUSAL_NOT_VISIBLE",
            ),
            _check(
                "receipt_alignment_correspondence_is_recognized",
                _correspondence_clear(receipt_alignment_result),
                expected="NON_CLAIM_ALIGNMENT correspondence recognized",
                actual=_as_mapping(
                    (receipt_alignment_result or {}).get(
                        "cross_surface_correspondence_summary"
                    )
                )
                if isinstance(receipt_alignment_result, Mapping)
                else None,
                block_code=(
                    "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED"
                    if isinstance(receipt_alignment_result, Mapping)
                    else "RECEIPT_ALIGNMENT_CORRESPONDENCE_MISSING"
                ),
            ),
            _check(
                "refusal_visible_correspondence_is_recognized",
                _correspondence_clear(refusal_visible_result),
                expected="REFUSAL_VISIBLE correspondence recognized",
                actual=_as_mapping(
                    (refusal_visible_result or {}).get(
                        "cross_surface_correspondence_summary"
                    )
                )
                if isinstance(refusal_visible_result, Mapping)
                else None,
                block_code=(
                    "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED"
                    if isinstance(refusal_visible_result, Mapping)
                    else "REFUSAL_VISIBLE_CORRESPONDENCE_MISSING"
                ),
            ),
            _check(
                "carrier_b_remains_receiving_carrier_only",
                returned_success_statement.get("receiving_carrier_became_source") is False
                and returned_success_statement.get("receiving_carrier_became_current") is False
                and returned_success_statement.get("receiving_carrier_became_authority") is False
                and returned_success_statement.get("receiving_carrier_became_successor") is False,
                expected="Carrier B remains receiving carrier evidence only",
                actual={
                    "receiving_carrier_became_source": returned_success_statement.get(
                        "receiving_carrier_became_source"
                    ),
                    "receiving_carrier_became_current": returned_success_statement.get(
                        "receiving_carrier_became_current"
                    ),
                    "receiving_carrier_became_authority": returned_success_statement.get(
                        "receiving_carrier_became_authority"
                    ),
                    "receiving_carrier_became_successor": returned_success_statement.get(
                        "receiving_carrier_became_successor"
                    ),
                },
                block_code="RECEIVING_CARRIER_SOURCE_LEAK",
            ),
            _check(
                "carried_surface_remains_carried_evidence_only",
                local_receipt_statement.get("carried_surface_became_source") is False
                and local_receipt_statement.get("carried_surface_became_currentness") is False
                and returned_success_statement.get("carried_surface_became_source") is False
                and returned_success_statement.get("carried_surface_became_currentness") is False
                and returned_success_statement.get("carried_surface_became_permission") is False
                and returned_success_statement.get("receipt_created_signal_by_default") is False,
                expected="carried surface stays non-source, non-currentness, non-permission, non-signal",
                actual={
                    "local_carried_surface_became_source": local_receipt_statement.get(
                        "carried_surface_became_source"
                    ),
                    "local_carried_surface_became_currentness": local_receipt_statement.get(
                        "carried_surface_became_currentness"
                    ),
                    "returned_carried_surface_became_source": returned_success_statement.get(
                        "carried_surface_became_source"
                    ),
                    "returned_carried_surface_became_currentness": returned_success_statement.get(
                        "carried_surface_became_currentness"
                    ),
                    "returned_carried_surface_became_permission": returned_success_statement.get(
                        "carried_surface_became_permission"
                    ),
                    "returned_receipt_created_signal_by_default": returned_success_statement.get(
                        "receipt_created_signal_by_default"
                    ),
                },
                block_code="CARRIED_SURFACE_SOURCE_OR_CURRENTNESS_LEAK",
            ),
            _check(
                "receipt_does_not_create_presence_threshold_truth_action_or_consequence",
                returned_success_statement.get("receipt_established_presence") is False
                and returned_success_statement.get("receipt_established_threshold") is False
                and returned_success_statement.get("receipt_created_truth") is False
                and returned_success_statement.get("receipt_authorized_action") is False
                and returned_success_statement.get("receipt_created_consequence") is False,
                expected="receipt creates no presence, threshold, truth, action, or consequence",
                actual={
                    "receipt_established_presence": returned_success_statement.get(
                        "receipt_established_presence"
                    ),
                    "receipt_established_threshold": returned_success_statement.get(
                        "receipt_established_threshold"
                    ),
                    "receipt_created_truth": returned_success_statement.get(
                        "receipt_created_truth"
                    ),
                    "receipt_authorized_action": returned_success_statement.get(
                        "receipt_authorized_action"
                    ),
                    "receipt_created_consequence": returned_success_statement.get(
                        "receipt_created_consequence"
                    ),
                },
                block_code="RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK",
            ),
            _check(
                "receipt_does_not_create_multi_carrier_law_or_distributed_standing",
                returned_success_statement.get("multi_carrier_law_created") is False
                and returned_success_statement.get("distributed_standing_created") is False
                and local_receipt_statement.get("multi_carrier_law_created") is False
                and local_receipt_statement.get("distributed_standing_created") is False,
                expected="receipt creates no multi-carrier law and no distributed standing",
                actual={
                    "local_multi_carrier_law_created": local_receipt_statement.get(
                        "multi_carrier_law_created"
                    ),
                    "local_distributed_standing_created": local_receipt_statement.get(
                        "distributed_standing_created"
                    ),
                    "returned_multi_carrier_law_created": returned_success_statement.get(
                        "multi_carrier_law_created"
                    ),
                    "returned_distributed_standing_created": returned_success_statement.get(
                        "distributed_standing_created"
                    ),
                },
                block_code="RECEIPT_MULTI_CARRIER_OR_DISTRIBUTED_STANDING_LEAK",
            ),
            _check(
                "post_v6_correspondence_and_receipt_surfaces_do_not_determine_current_governing_basis",
                True,
                expected="current/governing basis remains inherited from v6 upstream surfaces",
                actual="conformance, closure, correspondence, receipt, and Carrier B evidence recognized downstream only",
                block_code="RETURNED_EVIDENCE_CREATED_CURRENTNESS",
            ),
            _check(
                "non_claims_remain_false_and_carried_forward",
                _non_claims_all_false(non_claims),
                expected="all carried non-claims remain false",
                actual={
                    key: value
                    for key, value in sorted(non_claims.items())
                    if value is not False
                },
                block_code="NON_CLAIM_MISSING_OR_FLIPPED",
            ),
            _check(
                "latest_file_currentness_is_refused",
                non_claims.get("latest_file_currentness") is False
                and non_claims.get("recency_fraud") is False,
                expected=False,
                actual={
                    "latest_file_currentness": non_claims.get("latest_file_currentness"),
                    "recency_fraud": non_claims.get("recency_fraud"),
                },
                block_code="LATEST_FILE_CURRENTNESS_REFUSED",
            ),
            _check(
                "mutation_replay_merge_remain_false",
                non_claims.get("mutation_performed") is False
                and non_claims.get("replay_performed") is False
                and non_claims.get("merge_performed") is False
                and non_claims.get("carrier_merge_performed") is False,
                expected=False,
                actual={
                    "mutation_performed": non_claims.get("mutation_performed"),
                    "replay_performed": non_claims.get("replay_performed"),
                    "merge_performed": non_claims.get("merge_performed"),
                    "carrier_merge_performed": non_claims.get("carrier_merge_performed"),
                },
                block_code="MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
        ]
    )
    return checks


def _metadata(selected_inputs: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    v6 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v6_result"))
    base = _string_or_none(v6.get("result_id")) or "current_self_orientation_v7"
    suffix = "self_oriented" if outcome == OUTCOME_SELF_ORIENTED else "blocked"
    return {
        "self_orientation_result_id": f"{base}__current_self_orientation_v7_{suffix}",
        "self_orientation_result_type": CURRENT_SELF_ORIENTATION_RESULT_TYPE,
        "self_orientation_result_version": CURRENT_SELF_ORIENTATION_RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _empty_selected_inputs() -> dict[str, Any]:
    return {
        "selected_current_self_orientation_v6_result": {},
        "selected_current_body_conformance_result": {},
        "selected_post_conformance_closure_result": {},
        "selected_closure_alignment_correspondence_result": {},
        "selected_local_cross_carrier_receipt_result": {},
        "selected_returned_carrier_b_blocked_receipt_result": {},
        "selected_returned_carrier_b_successful_receipt_result": {},
        "selected_receipt_alignment_correspondence_result": {},
        "selected_refusal_visible_correspondence_result": {},
    }


def _selected_inputs(
    v6_result: Mapping[str, Any] | None,
    v6_ref: Mapping[str, Any],
    conformance_ref: Mapping[str, Any],
    closure_ref: Mapping[str, Any],
    closure_alignment_ref: Mapping[str, Any],
    local_receipt_ref: Mapping[str, Any],
    returned_blocked_ref: Mapping[str, Any],
    returned_success_ref: Mapping[str, Any],
    receipt_alignment_ref: Mapping[str, Any],
    refusal_visible_ref: Mapping[str, Any],
) -> dict[str, Any]:
    selected = _as_mapping(v6_result.get("selected_orientation_inputs")) if v6_result else {}
    selected["selected_current_self_orientation_v6_result"] = copy.deepcopy(dict(v6_ref))
    selected["selected_current_body_conformance_result"] = copy.deepcopy(
        dict(conformance_ref)
    )
    selected["selected_post_conformance_closure_result"] = copy.deepcopy(dict(closure_ref))
    selected["selected_closure_alignment_correspondence_result"] = copy.deepcopy(
        dict(closure_alignment_ref)
    )
    selected["selected_local_cross_carrier_receipt_result"] = copy.deepcopy(
        dict(local_receipt_ref)
    )
    selected["selected_returned_carrier_b_blocked_receipt_result"] = copy.deepcopy(
        dict(returned_blocked_ref)
    )
    selected["selected_returned_carrier_b_successful_receipt_result"] = copy.deepcopy(
        dict(returned_success_ref)
    )
    selected["selected_receipt_alignment_correspondence_result"] = copy.deepcopy(
        dict(receipt_alignment_ref)
    )
    selected["selected_refusal_visible_correspondence_result"] = copy.deepcopy(
        dict(refusal_visible_ref)
    )
    return selected


def _self_orientation_basis(
    selected_inputs: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    v6 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v6_result"))
    conformance = _as_mapping(selected_inputs.get("selected_current_body_conformance_result"))
    closure = _as_mapping(selected_inputs.get("selected_post_conformance_closure_result"))
    closure_alignment = _as_mapping(
        selected_inputs.get("selected_closure_alignment_correspondence_result")
    )
    local_receipt = _as_mapping(selected_inputs.get("selected_local_cross_carrier_receipt_result"))
    returned_blocked = _as_mapping(
        selected_inputs.get("selected_returned_carrier_b_blocked_receipt_result")
    )
    returned_success = _as_mapping(
        selected_inputs.get("selected_returned_carrier_b_successful_receipt_result")
    )
    receipt_alignment = _as_mapping(
        selected_inputs.get("selected_receipt_alignment_correspondence_result")
    )
    refusal_visible = _as_mapping(
        selected_inputs.get("selected_refusal_visible_correspondence_result")
    )
    return {
        "basis_kind": "v6_self_orientation_plus_post_conformance_correspondence_and_receipt_downstream_posture",
        "successor_of_module": SUCCESSOR_OF_MODULE,
        "selected_current_self_orientation_v6_result_id": v6.get("result_id"),
        "selected_current_self_orientation_v6_result_path": v6.get("result_path"),
        "selected_current_body_conformance_result_id": conformance.get("result_id"),
        "selected_current_body_conformance_result_path": conformance.get("result_path"),
        "selected_post_conformance_closure_result_id": closure.get("result_id"),
        "selected_post_conformance_closure_result_path": closure.get("result_path"),
        "selected_closure_alignment_correspondence_result_id": closure_alignment.get(
            "result_id"
        ),
        "selected_local_cross_carrier_receipt_result_id": local_receipt.get("result_id"),
        "selected_returned_carrier_b_blocked_receipt_result_id": returned_blocked.get(
            "result_id"
        ),
        "selected_returned_carrier_b_successful_receipt_result_id": returned_success.get(
            "result_id"
        ),
        "selected_receipt_alignment_correspondence_result_id": receipt_alignment.get(
            "result_id"
        ),
        "selected_refusal_visible_correspondence_result_id": refusal_visible.get(
            "result_id"
        ),
        "current_governing_basis_remains_inherited_from_v6_upstream_surfaces": True,
        "conformance_surfaces_remain_downstream_audit_only": True,
        "closure_surfaces_remain_downstream_meaning_closure_only": True,
        "correspondence_surfaces_remain_bounded_reading_relation_only": True,
        "receipt_surfaces_remain_carried_evidence_only": True,
        "carrier_b_remains_receiving_carrier_only": True,
        "post_v6_surfaces_create_authority": False,
        "post_v6_surfaces_create_permission": False,
        "post_v6_surfaces_create_currentness": False,
        "post_v6_surfaces_create_signal": False,
        "post_v6_surfaces_create_presence_threshold_truth_action_or_consequence": False,
        "post_v6_surfaces_authorize_continuation": False,
        "post_v6_surfaces_create_multi_carrier_law": False,
        "post_v6_surfaces_create_distributed_standing": False,
        "correspondence_checks_passed": _all_checks_passed(checks),
    }


def _build_result(
    *,
    selected_inputs: Mapping[str, Any],
    v6_result: Mapping[str, Any] | None,
    conformance_result: Mapping[str, Any] | None,
    closure_result: Mapping[str, Any] | None,
    closure_alignment_result: Mapping[str, Any] | None,
    local_receipt_result: Mapping[str, Any] | None,
    returned_blocked_result: Mapping[str, Any] | None,
    returned_success_result: Mapping[str, Any] | None,
    receipt_alignment_result: Mapping[str, Any] | None,
    refusal_visible_result: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    selected_v6_ref = _as_mapping(selected_inputs.get("selected_current_self_orientation_v6_result"))
    conformance_ref = _as_mapping(selected_inputs.get("selected_current_body_conformance_result"))
    closure_ref = _as_mapping(selected_inputs.get("selected_post_conformance_closure_result"))
    closure_alignment_ref = _as_mapping(
        selected_inputs.get("selected_closure_alignment_correspondence_result")
    )
    local_receipt_ref = _as_mapping(selected_inputs.get("selected_local_cross_carrier_receipt_result"))
    returned_blocked_ref = _as_mapping(
        selected_inputs.get("selected_returned_carrier_b_blocked_receipt_result")
    )
    returned_success_ref = _as_mapping(
        selected_inputs.get("selected_returned_carrier_b_successful_receipt_result")
    )
    receipt_alignment_ref = _as_mapping(
        selected_inputs.get("selected_receipt_alignment_correspondence_result")
    )
    refusal_visible_ref = _as_mapping(
        selected_inputs.get("selected_refusal_visible_correspondence_result")
    )

    result = {
        "current_self_orientation_v7_metadata": _metadata(selected_inputs, outcome),
        "selected_orientation_inputs": copy.deepcopy(dict(selected_inputs)),
        "recognized_current_executable_core_line": _section(
            v6_result,
            "recognized_current_executable_core_line",
        ),
        "recognized_governing_effective_basis": _section(
            v6_result,
            "recognized_governing_effective_basis",
        ),
        "recognized_current_state_surfaces": _section(
            v6_result,
            "recognized_current_state_surfaces",
        ),
        "recognized_continuity_surfaces": _section(
            v6_result,
            "recognized_continuity_surfaces",
        ),
        "recognized_derivative_surfaces": _section(
            v6_result,
            "recognized_derivative_surfaces",
        ),
        "recognized_operator_facing_surfaces": _section(
            v6_result,
            "recognized_operator_facing_surfaces",
        ),
        "recognized_reentry_surfaces": _section(
            v6_result,
            "recognized_reentry_surfaces",
        ),
        "recognized_body_signal_surfaces": _section(
            v6_result,
            "recognized_body_signal_surfaces",
        ),
        "recognized_derivative_vessel_relation_surfaces": _section(
            v6_result,
            "recognized_derivative_vessel_relation_surfaces",
        ),
        "recognized_current_body_conformance_surfaces": _recognized_current_body_conformance_surfaces(
            conformance_ref,
            conformance_result,
        ),
        "recognized_post_conformance_closure_surfaces": _recognized_post_conformance_closure_surfaces(
            closure_ref,
            closure_result,
        ),
        "recognized_cross_surface_correspondence_surfaces": _recognized_cross_surface_correspondence_surfaces(
            closure_alignment_ref,
            closure_alignment_result,
            receipt_alignment_ref,
            receipt_alignment_result,
            refusal_visible_ref,
            refusal_visible_result,
        ),
        "recognized_cross_carrier_receipt_surfaces": _recognized_cross_carrier_receipt_surfaces(
            local_receipt_ref,
            local_receipt_result,
            returned_blocked_ref,
            returned_blocked_result,
            returned_success_ref,
            returned_success_result,
        ),
        "recognized_open_surfaces": _section(v6_result, "recognized_open_surfaces"),
        "recognized_blocked_or_refused_surfaces": _recognized_blocked_or_refused_surfaces(
            v6_result,
            returned_blocked_ref,
        ),
        "recognized_touch_admissibility_surfaces": _section(
            v6_result,
            "recognized_touch_admissibility_surfaces",
        ),
        "bounded_correspondence_checks": [
            copy.deepcopy(dict(check)) for check in checks
        ],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "self_orientation_basis": _self_orientation_basis(selected_inputs, checks),
        "current_self_orientation_summary": {},
        "non_claims": dict(non_claims),
    }
    result["current_self_orientation_summary"] = build_current_self_orientation_summary(
        result
    )
    return result


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    v6_result: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    selected = selected_inputs if isinstance(selected_inputs, Mapping) else _empty_selected_inputs()
    return _build_result(
        selected_inputs=selected,
        v6_result=v6_result,
        conformance_result=None,
        closure_result=None,
        closure_alignment_result=None,
        local_receipt_result=None,
        returned_blocked_result=None,
        returned_success_result=None,
        receipt_alignment_result=None,
        refusal_visible_result=None,
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _resolve(
    v6_result: Mapping[str, Any] | None = None,
    v6_result_path: Path | str | None = None,
) -> dict[str, Any]:
    v6_path, selected_v6, v6_selection_mode = _select_v6(v6_result, v6_result_path)
    v6_ref = _artifact_ref(
        selected_v6,
        v6_path,
        v6_selection_mode,
        result_family="current_self_orientation_v6_result",
    )

    if selected_v6 is None:
        checks = [
            _check(
                "self_orientation_v6_stands",
                False,
                expected="one current self-orientation v6 result is selected",
                actual=False,
                block_code="SELF_ORIENTATION_V6_MISSING",
            )
        ]
        return _blocked_result(
            block_code="SELF_ORIENTATION_V6_MISSING",
            selected_inputs={"selected_current_self_orientation_v6_result": v6_ref},
            checks=checks,
        )

    selected_inputs = _selected_inputs(
        selected_v6,
        v6_ref,
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
    )

    conformance_path, conformance_result, conformance_selection = _select_conformance(
        v6_ref
    )
    conformance_ref = _artifact_ref(
        conformance_result,
        conformance_path,
        conformance_selection,
        result_family="current_body_conformance_result",
    )
    closure_path, closure_result, closure_selection = _select_closure(
        v6_ref,
        conformance_ref,
    )
    closure_ref = _artifact_ref(
        closure_result,
        closure_path,
        closure_selection,
        result_family="post_conformance_closure_result",
    )
    (
        closure_alignment_path,
        closure_alignment_result,
        closure_alignment_selection,
    ) = _select_correspondence(
        "CLOSURE_ALIGNMENT",
        selected_surface_outcomes={
            OUTCOME_BODY_CONFORMANT,
            OUTCOME_CONFORMANCE_CLOSURE_RECORDED,
        },
    )
    closure_alignment_ref = _artifact_ref(
        closure_alignment_result,
        closure_alignment_path,
        closure_alignment_selection,
        result_family="cross_surface_correspondence_result",
    )
    local_receipt_path, local_receipt_result, local_receipt_selection = _select_receipt(
        CROSS_CARRIER_SURFACE_RECEIPT_ROOT,
        OUTCOME_CARRIED_SURFACE_RECEIVED,
        "local_cross_carrier_receipt_discovery",
    )
    local_receipt_ref = _artifact_ref(
        local_receipt_result,
        local_receipt_path,
        local_receipt_selection,
        result_family="cross_carrier_surface_receipt_result",
    )
    (
        returned_blocked_path,
        returned_blocked_result,
        returned_blocked_selection,
    ) = _select_receipt(
        RETURNED_CARRIER_B_RECEIPT_ROOT,
        OUTCOME_BLOCKED,
        "returned_carrier_b_blocked_receipt_discovery",
    )
    returned_blocked_ref = _artifact_ref(
        returned_blocked_result,
        returned_blocked_path,
        returned_blocked_selection,
        result_family="returned_carrier_b_cross_carrier_surface_receipt_result",
    )
    (
        returned_success_path,
        returned_success_result,
        returned_success_selection,
    ) = _select_receipt(
        RETURNED_CARRIER_B_RECEIPT_ROOT,
        OUTCOME_CARRIED_SURFACE_RECEIVED,
        "returned_carrier_b_successful_receipt_discovery",
    )
    returned_success_ref = _artifact_ref(
        returned_success_result,
        returned_success_path,
        returned_success_selection,
        result_family="returned_carrier_b_cross_carrier_surface_receipt_result",
    )
    (
        receipt_alignment_path,
        receipt_alignment_result,
        receipt_alignment_selection,
    ) = _select_correspondence(
        "NON_CLAIM_ALIGNMENT",
        selected_surface_outcomes={OUTCOME_CARRIED_SURFACE_RECEIVED},
    )
    receipt_alignment_ref = _artifact_ref(
        receipt_alignment_result,
        receipt_alignment_path,
        receipt_alignment_selection,
        result_family="cross_surface_correspondence_result",
    )
    (
        refusal_visible_path,
        refusal_visible_result,
        refusal_visible_selection,
    ) = _select_correspondence(
        "REFUSAL_VISIBLE",
        selected_surface_outcomes={OUTCOME_BLOCKED, OUTCOME_CARRIED_SURFACE_RECEIVED},
    )
    refusal_visible_ref = _artifact_ref(
        refusal_visible_result,
        refusal_visible_path,
        refusal_visible_selection,
        result_family="cross_surface_correspondence_result",
    )

    selected_inputs = _selected_inputs(
        selected_v6,
        v6_ref,
        conformance_ref,
        closure_ref,
        closure_alignment_ref,
        local_receipt_ref,
        returned_blocked_ref,
        returned_success_ref,
        receipt_alignment_ref,
        refusal_visible_ref,
    )
    non_claims = _merge_non_claims(
        selected_v6,
        conformance_result,
        closure_result,
        closure_alignment_result,
        local_receipt_result,
        returned_blocked_result,
        returned_success_result,
        receipt_alignment_result,
        refusal_visible_result,
    )
    checks = _build_checks(
        v6_result=selected_v6,
        conformance_result=conformance_result,
        closure_result=closure_result,
        closure_alignment_result=closure_alignment_result,
        local_receipt_result=local_receipt_result,
        returned_blocked_result=returned_blocked_result,
        returned_success_result=returned_success_result,
        receipt_alignment_result=receipt_alignment_result,
        refusal_visible_result=refusal_visible_result,
        non_claims=non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _build_result(
            selected_inputs=selected_inputs,
            v6_result=selected_v6,
            conformance_result=conformance_result,
            closure_result=closure_result,
            closure_alignment_result=closure_alignment_result,
            local_receipt_result=local_receipt_result,
            returned_blocked_result=returned_blocked_result,
            returned_success_result=returned_success_result,
            receipt_alignment_result=receipt_alignment_result,
            refusal_visible_result=refusal_visible_result,
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code=str(failed.get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED"),
            block_detail=f"failed check: {failed.get('check_name')}",
            non_claims=non_claims,
        )

    return _build_result(
        selected_inputs=selected_inputs,
        v6_result=selected_v6,
        conformance_result=conformance_result,
        closure_result=closure_result,
        closure_alignment_result=closure_alignment_result,
        local_receipt_result=local_receipt_result,
        returned_blocked_result=returned_blocked_result,
        returned_success_result=returned_success_result,
        receipt_alignment_result=receipt_alignment_result,
        refusal_visible_result=refusal_visible_result,
        checks=checks,
        outcome=OUTCOME_SELF_ORIENTED,
        block_code=None,
        block_detail=None,
        non_claims=non_claims,
    )


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded v7 self-orientation result.

    The argument name is retained for API continuity with earlier resolver
    lines. In v7, a supplied mapping is treated as the selected current
    self-orientation v6 successor basis.
    """

    try:
        return _resolve(v6_result=body_pass_result)
    except CurrentSelfOrientationV7Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs,
            checks=exc.checks,
        )


def resolve_current_self_orientation_from_path(v6_result_path: Path | str) -> dict[str, Any]:
    """Resolve one bounded v7 self-orientation result from a v6 basis path."""

    selected_inputs = {
        "selected_current_self_orientation_v6_result": {
            "result_path": _display_path(v6_result_path),
            "selection_mode": "explicit_current_self_orientation_v6_result_path",
        }
    }
    try:
        return _resolve(v6_result_path=v6_result_path)
    except CurrentSelfOrientationV7Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs or selected_inputs,
            checks=exc.checks,
        )


def build_current_self_orientation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact bounded v7 self-orientation summary."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV7Error(
            "current self-orientation result must be an object",
            "SELF_ORIENTATION_V6_MALFORMED",
        )
    selected = _as_mapping(result.get("selected_orientation_inputs"))
    block = _as_mapping(result.get("block"))
    checks = _mapping_list(result.get("bounded_correspondence_checks"))
    non_claims = _as_mapping(result.get("non_claims"))

    v6 = _as_mapping(selected.get("selected_current_self_orientation_v6_result"))
    conformance = _as_mapping(selected.get("selected_current_body_conformance_result"))
    closure = _as_mapping(selected.get("selected_post_conformance_closure_result"))
    closure_alignment = _as_mapping(
        selected.get("selected_closure_alignment_correspondence_result")
    )
    local_receipt = _as_mapping(selected.get("selected_local_cross_carrier_receipt_result"))
    returned_blocked = _as_mapping(
        selected.get("selected_returned_carrier_b_blocked_receipt_result")
    )
    returned_success = _as_mapping(
        selected.get("selected_returned_carrier_b_successful_receipt_result")
    )
    receipt_alignment = _as_mapping(
        selected.get("selected_receipt_alignment_correspondence_result")
    )
    refusal_visible = _as_mapping(
        selected.get("selected_refusal_visible_correspondence_result")
    )
    basis = _as_mapping(result.get("self_orientation_basis"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_top_level_basis_ids": {
            "current_self_orientation_v6": v6.get("result_id"),
            "current_body_conformance": conformance.get("result_id"),
            "post_conformance_closure": closure.get("result_id"),
            "closure_alignment_correspondence": closure_alignment.get("result_id"),
            "local_cross_carrier_receipt": local_receipt.get("result_id"),
            "returned_carrier_b_blocked_receipt": returned_blocked.get("result_id"),
            "returned_carrier_b_successful_receipt": returned_success.get("result_id"),
            "receipt_alignment_correspondence": receipt_alignment.get("result_id"),
            "refusal_visible_correspondence": refusal_visible.get("result_id"),
        },
        "selected_current_self_orientation_v6_id": v6.get("result_id"),
        "selected_current_self_orientation_v6_path": v6.get("result_path"),
        "selected_current_body_conformance_id": conformance.get("result_id"),
        "selected_post_conformance_closure_id": closure.get("result_id"),
        "selected_closure_alignment_correspondence_id": closure_alignment.get("result_id"),
        "selected_local_cross_carrier_receipt_id": local_receipt.get("result_id"),
        "selected_returned_carrier_b_blocked_receipt_id": returned_blocked.get("result_id"),
        "selected_returned_carrier_b_successful_receipt_id": returned_success.get("result_id"),
        "selected_receipt_alignment_correspondence_id": receipt_alignment.get("result_id"),
        "selected_refusal_visible_correspondence_id": refusal_visible.get("result_id"),
        "current_governing_basis_recognized": bool(
            result.get("recognized_current_executable_core_line")
            and result.get("recognized_governing_effective_basis")
            and result.get("recognized_current_state_surfaces")
        ),
        "reentry_surfaces_recognized": bool(result.get("recognized_reentry_surfaces")),
        "body_signal_surfaces_recognized": bool(
            result.get("recognized_body_signal_surfaces")
        ),
        "derivative_vessel_relation_boundary_recognized": bool(
            result.get("recognized_derivative_vessel_relation_surfaces")
        ),
        "current_body_conformance_recognized": bool(
            result.get("recognized_current_body_conformance_surfaces")
        ),
        "post_conformance_closure_recognized": bool(
            result.get("recognized_post_conformance_closure_surfaces")
        ),
        "cross_surface_correspondence_recognized": bool(
            result.get("recognized_cross_surface_correspondence_surfaces")
        ),
        "cross_carrier_receipt_recognized": bool(
            result.get("recognized_cross_carrier_receipt_surfaces")
        ),
        "carrier_b_returned_receipt_evidence_recognized": bool(
            returned_success.get("result_id")
        ),
        "carrier_b_refusal_evidence_remains_visible": bool(
            returned_blocked.get("result_id")
        ),
        "receipt_alignment_correspondence_recognized": bool(
            receipt_alignment.get("result_id")
        ),
        "refusal_visible_correspondence_recognized": bool(
            refusal_visible.get("result_id")
        ),
        "carrier_b_remained_receiving_carrier_only": basis.get(
            "carrier_b_remains_receiving_carrier_only"
        ),
        "source_currentness_authority_permission_successor_body_collapse_stayed_false": not (
            non_claims.get("source_replaced")
            or non_claims.get("currentness_created")
            or non_claims.get("authority_created")
            or non_claims.get("permission_created")
            or non_claims.get("receiving_carrier_became_successor")
            or non_claims.get("receiving_carrier_became_body")
        ),
        "multi_carrier_law_stayed_false": non_claims.get("multi_carrier_law_created")
        is False,
        "distributed_standing_stayed_false": non_claims.get(
            "distributed_standing_created"
        )
        is False,
        "presence_threshold_truth_action_consequence_stayed_false": not (
            non_claims.get("presence_established")
            or non_claims.get("threshold_met")
            or non_claims.get("truth_created")
            or non_claims.get("action_authorized")
            or non_claims.get("consequence_created")
        ),
        "correspondence_checks_passed": _all_checks_passed(checks),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in SUMMARY_NON_CLAIMS
            if key in non_claims
        },
    }


def _safe_default_output_path(result: Mapping[str, Any]) -> Path:
    selected = _as_mapping(result.get("selected_orientation_inputs"))
    v6 = _as_mapping(selected.get("selected_current_self_orientation_v6_result"))
    stem = _safe_filename_part(v6.get("result_id") or "current_self_orientation_v7")
    candidate = CURRENT_SELF_ORIENTATION_V7_ROOT / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            CURRENT_SELF_ORIENTATION_V7_ROOT
            / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentSelfOrientationV7Error(
        "no bounded current self-orientation v7 filename is available",
        "SELF_ORIENTATION_V6_MALFORMED",
    )


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v7 self-orientation JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV7Error(
            "current self-orientation result must be an object",
            "SELF_ORIENTATION_V6_MALFORMED",
        )
    target = _repo_path(output_path) if output_path is not None else _safe_default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current self-orientation v7 result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


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
