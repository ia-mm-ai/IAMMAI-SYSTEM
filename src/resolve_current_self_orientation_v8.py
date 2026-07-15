"""Bounded current self-orientation v8 resolver.

V8 is a lineage-preserving successor to v7. It keeps the v7 self-orientation
model and mirrors the closed multi-carrier relation band as downstream posture
only. The relation band does not become source, currentness, authority,
permission, carrier hierarchy, distributed standing, continuation, or
authorization for another carrier experiment.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class CurrentSelfOrientationV8Error(RuntimeError):
    """Hard malformed input or impossible bounded shape contradiction."""

    def __init__(self, message: str, *, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REPO_ROOT = Path(__file__).resolve().parents[1]

CURRENT_SELF_ORIENTATION_V6_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)
CURRENT_SELF_ORIENTATION_V7_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v7"
)
CURRENT_SELF_ORIENTATION_V8_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v8"
)
CURRENT_BODY_CONFORMANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance"
)
CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass_v2"
)
POST_CONFORMANCE_CLOSURE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_standing_closure"
)
REENTRY_ADMISSIBILITY_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_reentry_admissibility"
)
REENTRY_RECEIPT_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_reentry_receipt"
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
BOUNDED_DERIVATIVE_VESSEL_READ_ROOT = (
    REPO_ROOT / "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_FACING_TERMINAL_BRIEF_ROOT = (
    REPO_ROOT / "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)
CROSS_SURFACE_CORRESPONDENCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_cross_surface_correspondence_boundary"
)
CROSS_CARRIER_SURFACE_RECEIPT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_surface_receipt_boundary"
)
RETURNED_CARRIER_B_RECEIPT_ROOT = CROSS_CARRIER_SURFACE_RECEIPT_ROOT / "returned_from_carrier_B"
CARRIER_ROLE_EMISSION_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_role_and_emission_boundary"
)
CARRIER_LOCAL_EMISSION_ADMISSION_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_local_emission_admission_boundary"
)
CROSS_CARRIER_DIVERGENCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_divergence_boundary"
)
CROSS_CARRIER_CURRENTNESS_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_currentness_boundary"
)
MULTI_CARRIER_RELATION_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary"
)
MULTI_CARRIER_RELATION_CONFORMANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_conformance"
)
MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_conformance_closure"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v8"
SUCCESSOR_OF_MODULE = "resolve_current_self_orientation_v7"
SELF_ORIENTATION_RESULT_VERSION = "0.8.0"

SELF_ORIENTED = "SELF_ORIENTED"
BLOCKED = "BLOCKED"
BODY_CONFORMANT = "BODY_CONFORMANT"
RELATION_RECOGNIZED = "MULTI_CARRIER_RELATION_RECOGNIZED"
RELATION_CONFORMANT = "MULTI_CARRIER_RELATION_CONFORMANT"
RELATION_CONFORMANCE_CLOSED = "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED"

OPTIONAL_OUTCOMES: dict[str, set[str]] = {
    "carrier_role_emission": {
        "CARRIER_ROLE_AND_EMISSION_RECOGNIZED",
        "CARRIER_ROLE_RECOGNIZED",
        "CARRIER_EMISSION_RECOGNIZED",
    },
    "carrier_local_emission_admission": {
        "CARRIER_LOCAL_EMISSION_ADMITTED",
        "LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
        "EMISSION_ADMITTED_AS_EVIDENCE",
    },
    "cross_carrier_divergence": {
        "CROSS_CARRIER_DIVERGENCE_RECORDED",
        "DIVERGENCE_RECORDED",
    },
    "cross_carrier_currentness": {
        "CROSS_CARRIER_CURRENTNESS_PARTICIPATION_ELIGIBLE",
        "CURRENTNESS_PARTICIPATION_ELIGIBLE",
    },
    "cross_carrier_receipt": {"CARRIED_SURFACE_RECEIVED"},
    "returned_blocked_receipt": {"BLOCKED"},
    "returned_successful_receipt": {"CARRIED_SURFACE_RECEIVED"},
    "cross_surface_correspondence": {
        "CROSS_SURFACE_CORRESPONDENCE_RECOGNIZED",
        "CORRESPONDENCE_RECOGNIZED",
    },
}

SUMMARY_KEYS = (
    "current_self_orientation_summary",
    "current_body_conformance_pass_v2_summary",
    "current_body_conformance_summary",
    "multi_carrier_relation_summary",
    "multi_carrier_relation_conformance_summary",
    "multi_carrier_relation_conformance_closure_summary",
    "cross_carrier_currentness_summary",
    "cross_carrier_divergence_summary",
    "carrier_local_emission_admission_summary",
    "carrier_role_emission_summary",
    "cross_carrier_surface_receipt_summary",
    "cross_surface_correspondence_summary",
)
CHECK_KEYS = (
    "bounded_correspondence_checks",
    "conformance_checks",
    "relation_checks",
    "relation_conformance_checks",
    "closure_checks",
    "currentness_checks",
    "divergence_checks",
    "admission_checks",
    "receipt_checks",
    "correspondence_checks",
)

NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "source_scope_widened": False,
    "continuity_completed": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "standing_upgraded": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "carrier_hierarchy_created": False,
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
    "additional_carrier_experiment_authorized": False,
    "distributed_operation_authorized": False,
    "closure_authorized_expansion": False,
    "closure_forced_self_orientation_successor": False,
    "closure_forced_conformance_successor": False,
    "self_orientation_successor_forced": False,
    "conformance_successor_forced": False,
    "divergence_hidden": False,
    "refusal_hidden": False,
    "mismatch_hidden": False,
    "evidence_overwritten": False,
    "evidence_merged_into_source": False,
    "divergence_resolved_by_majority": False,
    "divergence_resolved_by_latest_file": False,
    "divergence_resolved_by_success_count": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "derivative_upgraded_to_source": False,
    "operator_upgraded_to_source": False,
    "carrier_receipt_created_source": False,
    "carrier_receipt_created_currentness": False,
    "carrier_receipt_created_authority": False,
    "carrier_receipt_created_permission": False,
    "carrier_relation_created_source": False,
    "carrier_relation_created_currentness": False,
    "carrier_relation_created_authority": False,
    "carrier_relation_created_permission": False,
    "carrier_relation_created_successor": False,
    "carrier_relation_created_body": False,
    "carrier_relation_created_hierarchy": False,
    "relation_conformance_created_source": False,
    "relation_conformance_created_currentness": False,
    "relation_conformance_created_authority": False,
    "relation_conformance_created_permission": False,
    "relation_conformance_created_successor": False,
    "relation_conformance_created_body": False,
    "relation_conformance_created_hierarchy": False,
    "relation_conformance_closure_created_source": False,
    "relation_conformance_closure_created_currentness": False,
    "relation_conformance_closure_created_authority": False,
    "relation_conformance_closure_created_permission": False,
    "relation_conformance_closure_created_successor": False,
    "relation_conformance_closure_created_body": False,
    "relation_conformance_closure_created_hierarchy": False,
}

SUMMARY_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "distributed_standing_created",
    "continuation_authorized",
    "additional_carrier_experiment_authorized",
    "distributed_operation_authorized",
    "closure_authorized_expansion",
    "closure_forced_self_orientation_successor",
    "closure_forced_conformance_successor",
    "latest_file_currentness",
    "recency_fraud",
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [dict(item) for item in value if isinstance(item, Mapping)]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    try:
        return str(Path(path).relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _iter_mappings(value: Any) -> Iterable[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        yield value
        for child in value.values():
            yield from _iter_mappings(child)
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for child in value:
            yield from _iter_mappings(child)


def _read_json_mapping(
    path: Path | str,
    *,
    unreadable_code: str = "SELECTED_ARTIFACT_UNREADABLE",
    malformed_code: str = "SELECTED_ARTIFACT_MALFORMED",
) -> dict[str, Any]:
    resolved = _repo_path(path)
    if not resolved.exists() or not resolved.is_file():
        raise CurrentSelfOrientationV8Error(
            f"Unreadable selected artifact: {_display_path(resolved)}",
            block_code=unreadable_code,
        )
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise CurrentSelfOrientationV8Error(
            f"Malformed selected artifact: {_display_path(resolved)}",
            block_code=malformed_code,
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CurrentSelfOrientationV8Error(
            f"Selected artifact is not an object: {_display_path(resolved)}",
            block_code=malformed_code,
        )
    return dict(loaded)


def _iter_artifacts(root: Path) -> Iterable[tuple[Path, dict[str, Any]]]:
    if not root.exists() or not root.is_dir():
        return
    for path in sorted(root.rglob("*.json")):
        try:
            with path.open("r", encoding="utf-8") as handle:
                loaded = json.load(handle)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(loaded, Mapping):
            yield path, dict(loaded)


def _metadata(result: Mapping[str, Any]) -> dict[str, Any]:
    for key, value in result.items():
        if key.endswith("_metadata") and isinstance(value, Mapping):
            return dict(value)
    return {}


def _result_id(result: Mapping[str, Any]) -> str | None:
    metadata = _metadata(result)
    for key, value in metadata.items():
        if key.endswith("_result_id") and isinstance(value, str) and value:
            return value
    return None


def _result_type(result: Mapping[str, Any]) -> str | None:
    metadata = _metadata(result)
    for key, value in metadata.items():
        if key.endswith("_result_type") and isinstance(value, str) and value:
            return value
    return None


def _result_version(result: Mapping[str, Any]) -> str | None:
    metadata = _metadata(result)
    for key, value in metadata.items():
        if key.endswith("_result_version") and isinstance(value, str) and value:
            return value
    return None


def _artifact_ref(
    result: Mapping[str, Any] | None,
    path: Path | str | None = None,
    *,
    label: str | None = None,
) -> dict[str, Any]:
    source = _as_mapping(result)
    return {
        "artifact_label": label,
        "result_id": _result_id(source),
        "result_type": _result_type(source),
        "result_version": _result_version(source),
        "resolver_module": _metadata(source).get("resolver_module"),
        "outcome": source.get("outcome"),
        "path": _display_path(path),
    }


def _failed_count(result: Mapping[str, Any]) -> int | None:
    for key in SUMMARY_KEYS:
        summary = _as_mapping(result.get(key))
        value = summary.get("failed_check_count")
        if isinstance(value, int):
            return value
    for key in CHECK_KEYS:
        checks = _mapping_list(result.get(key))
        if checks:
            return sum(1 for check in checks if check.get("passed") is False)
    return None


def _passed_count(result: Mapping[str, Any]) -> int | None:
    for key in SUMMARY_KEYS:
        summary = _as_mapping(result.get(key))
        value = summary.get("passed_check_count")
        if isinstance(value, int):
            return value
    for key in CHECK_KEYS:
        checks = _mapping_list(result.get(key))
        if checks:
            return sum(1 for check in checks if check.get("passed") is True)
    return None


def _zero_failed(result: Mapping[str, Any]) -> bool:
    return _failed_count(result) in (None, 0)


def _latest_successful(
    root: Path,
    outcomes: set[str],
    *,
    require_zero_failed: bool = True,
) -> tuple[Path, dict[str, Any]] | None:
    candidates: list[tuple[float, str, Path, dict[str, Any]]] = []
    for path, result in _iter_artifacts(root):
        if result.get("outcome") not in outcomes:
            continue
        if require_zero_failed and not _zero_failed(result):
            continue
        try:
            modified_at = path.stat().st_mtime
        except OSError:
            modified_at = 0.0
        candidates.append((modified_at, str(path), path, result))
    if not candidates:
        return None
    _, _, path, result = sorted(candidates)[-1]
    return path, result


def _load_exposed_path(value: Any, expected_outcome: str) -> tuple[Path, dict[str, Any]] | None:
    if not isinstance(value, str) or not value.strip():
        return None
    path = _repo_path(value)
    if not path.exists():
        return None
    try:
        result = _read_json_mapping(path)
    except CurrentSelfOrientationV8Error:
        return None
    if result.get("outcome") == expected_outcome and _zero_failed(result):
        return path, result
    return None


def _section(result: Mapping[str, Any], key: str) -> Any:
    return _copy(result.get(key, {}))


def _safe_filename(value: Any) -> str:
    text = str(value or "current_self_orientation_v8").strip().lower()
    safe = "".join(char if char.isalnum() else "_" for char in text)
    safe = "_".join(part for part in safe.split("_") if part)
    return safe[:140] or "current_self_orientation_v8"


def _truthy_flag(source: Mapping[str, Any], *keys: str) -> bool:
    return any(source.get(key) is True for key in keys)


def _any_flag_true(sources: Sequence[Mapping[str, Any]], flags: Sequence[str]) -> bool:
    for source in sources:
        for mapping in _iter_mappings(source):
            if any(mapping.get(flag) is True for flag in flags):
                return True
    return False


def _merge_non_claims(sources: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    merged = dict(NON_CLAIMS)
    for source in sources:
        for mapping in _iter_mappings(source):
            non_claims = mapping.get("non_claims")
            if isinstance(non_claims, Mapping):
                merged.update(dict(non_claims))
    return merged


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    return {key: non_claims.get(key, False) for key in SUMMARY_NON_CLAIMS}


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
    }


def _counts(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    return (
        sum(1 for check in checks if check.get("passed") is True),
        sum(1 for check in checks if check.get("passed") is False),
    )


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if check.get("passed") is False:
            return dict(check)
    return None


def _block_reason(block_code: str | None) -> str | None:
    reasons = {
        "SELF_ORIENTATION_V7_MISSING": "No successful v7 self-orientation basis was selected.",
        "SELF_ORIENTATION_V7_MALFORMED": "Selected v7 self-orientation basis is malformed.",
        "SELF_ORIENTATION_V7_NOT_SELF_ORIENTED": "Selected v7 basis is not SELF_ORIENTED.",
        "CURRENT_BODY_CONFORMANCE_V2_MISSING": "No successful current-body conformance v2 result was selected.",
        "CURRENT_BODY_CONFORMANCE_V2_NOT_BODY_CONFORMANT": "Selected current-body conformance v2 result is not BODY_CONFORMANT.",
        "MULTI_CARRIER_RELATION_MISSING": "No recognized multi-carrier relation result was selected.",
        "MULTI_CARRIER_RELATION_NOT_RECOGNIZED": "Selected multi-carrier relation result is not recognized.",
        "MULTI_CARRIER_RELATION_CONFORMANCE_MISSING": "No conformant relation conformance result was selected.",
        "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CONFORMANT": "Selected relation conformance result is not conformant.",
        "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_MISSING": "No closed relation conformance closure result was selected.",
        "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_CLOSED": "Selected relation conformance closure result is not closed.",
        "RELATION_CLOSURE_DISTRIBUTED_STANDING_LEAK": "Relation closure leaked distributed standing.",
        "RELATION_CLOSURE_CURRENTNESS_LEAK": "Relation closure leaked currentness or current carrier selection.",
        "RELATION_CLOSURE_AUTHORITY_PERMISSION_LEAK": "Relation closure leaked source, authority, or permission.",
        "RELATION_CLOSURE_CARRIER_HIERARCHY_LEAK": "Relation closure leaked carrier hierarchy or winner/loser collapse.",
        "RELATION_CLOSURE_CONTINUATION_LEAK": "Relation closure leaked continuation authorization.",
        "RELATION_CLOSURE_ADDITIONAL_CARRIER_EXPERIMENT_LEAK": "Relation closure authorized another carrier experiment.",
        "RELATION_CLOSURE_DISTRIBUTED_OPERATION_LEAK": "Relation closure authorized distributed operation.",
        "RELATION_CLOSURE_SUCCESSOR_PRESSURE_LEAK": "Relation closure forced a successor.",
        "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS": "Relation band attempted to determine current/governing basis.",
        "LATEST_FILE_CURRENTNESS_REFUSED": "Latest-file or recency currentness appeared.",
        "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge posture appeared.",
        "NON_CLAIM_MISSING_OR_FLIPPED": "Required non-claim is missing or flipped.",
    }
    return reasons.get(block_code, block_code.replace("_", " ").lower() if block_code else None)


def _select_v7(body_pass_result: Mapping[str, Any] | None) -> tuple[Path | None, dict[str, Any] | None]:
    if body_pass_result is not None:
        if not isinstance(body_pass_result, Mapping):
            raise CurrentSelfOrientationV8Error(
                "Explicit v7 basis must be a mapping.",
                block_code="SELF_ORIENTATION_V7_MALFORMED",
            )
        return None, dict(body_pass_result)
    selected = _latest_successful(CURRENT_SELF_ORIENTATION_V7_ROOT, {SELF_ORIENTED})
    return selected if selected else (None, None)


def _select_body_conformance_v2(
    v7_result: Mapping[str, Any],
    v7_path: Path | None,
) -> tuple[Path | None, dict[str, Any] | None]:
    v7_id = _result_id(v7_result)
    v7_display_path = _display_path(v7_path)
    matching: list[tuple[float, str, Path, dict[str, Any]]] = []
    fallback: list[tuple[float, str, Path, dict[str, Any]]] = []
    for path, result in _iter_artifacts(CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT):
        if result.get("outcome") != BODY_CONFORMANT or not _zero_failed(result):
            continue
        try:
            modified_at = path.stat().st_mtime
        except OSError:
            modified_at = 0.0
        row = (modified_at, str(path), path, result)
        fallback.append(row)
        exposed_id = (
            _nested(result, "v7_orientation_basis", "selected_v7_result_id")
            or _nested(
                result,
                "selected_conformance_inputs",
                "selected_current_self_orientation_v7_result",
                "result_id",
            )
            or _nested(
                result,
                "selected_conformance_inputs",
                "selected_current_self_orientation_v7_result",
                "selected_v7_result_id",
            )
        )
        exposed_path = (
            _nested(result, "v7_orientation_basis", "selected_v7_result_path")
            or _nested(
                result,
                "selected_conformance_inputs",
                "selected_current_self_orientation_v7_result",
                "path",
            )
            or _nested(
                result,
                "selected_conformance_inputs",
                "selected_current_self_orientation_v7_result",
                "selected_v7_result_path",
            )
        )
        if (v7_id and exposed_id == v7_id) or (v7_display_path and exposed_path == v7_display_path):
            matching.append(row)
    candidates = matching or fallback
    if not candidates:
        return None, None
    _, _, path, result = sorted(candidates)[-1]
    return path, result


def _select_relation_closure() -> tuple[Path | None, dict[str, Any] | None]:
    selected = _latest_successful(
        MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT,
        {RELATION_CONFORMANCE_CLOSED},
    )
    return selected if selected else (None, None)


def _select_relation_conformance(
    closure_result: Mapping[str, Any] | None,
) -> tuple[Path | None, dict[str, Any] | None]:
    closure = _as_mapping(closure_result)
    selected = _load_exposed_path(
        _nested(closure, "selected_conformance", "selected_conformance_result_path")
        or _nested(closure, "selected_conformance", "path"),
        RELATION_CONFORMANT,
    )
    if selected:
        return selected
    selected = _latest_successful(MULTI_CARRIER_RELATION_CONFORMANCE_ROOT, {RELATION_CONFORMANT})
    return selected if selected else (None, None)


def _select_relation(
    closure_result: Mapping[str, Any] | None,
    conformance_result: Mapping[str, Any] | None,
) -> tuple[Path | None, dict[str, Any] | None]:
    closure = _as_mapping(closure_result)
    conformance = _as_mapping(conformance_result)
    for exposed_path in (
        _nested(closure, "selected_relation", "selected_relation_result_path"),
        _nested(closure, "selected_relation", "path"),
        _nested(conformance, "selected_relation", "selected_relation_result_path"),
        _nested(conformance, "selected_relation", "path"),
    ):
        selected = _load_exposed_path(exposed_path, RELATION_RECOGNIZED)
        if selected:
            return selected
    selected = _latest_successful(MULTI_CARRIER_RELATION_ROOT, {RELATION_RECOGNIZED})
    return selected if selected else (None, None)


def _select_optional(
    name: str,
    root: Path,
    *,
    require_zero_failed: bool = True,
) -> tuple[Path | None, dict[str, Any] | None]:
    selected = _latest_successful(
        root,
        OPTIONAL_OUTCOMES[name],
        require_zero_failed=require_zero_failed,
    )
    return selected if selected else (None, None)


def _recognize_optional(
    name: str,
    path: Path | None,
    result: Mapping[str, Any] | None,
    posture: str,
) -> dict[str, Any]:
    selected = _as_mapping(result)
    summary: dict[str, Any] = {}
    for key in SUMMARY_KEYS:
        if isinstance(selected.get(key), Mapping):
            summary = _section(selected, key)
            break
    return {
        "recognition_group": name,
        "recognized": selected.get("outcome") in OPTIONAL_OUTCOMES.get(name, set()),
        "selected_artifact": _artifact_ref(selected, path, label=name),
        "posture": posture,
        "downstream_only": True,
        "current_or_governing_basis": False,
        "summary": summary,
        "non_claims": _section(selected, "non_claims"),
    }


def _relation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("multi_carrier_relation_summary"))


def _relation_statement(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("relation_result"))


def _conformance_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("multi_carrier_relation_conformance_summary"))


def _conformance_statement(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("relation_conformance_statement"))


def _closure_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("multi_carrier_relation_conformance_closure_summary"))


def _closure_statement(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("closure_statement"))


def _recognized_relation(path: Path | None, result: Mapping[str, Any] | None) -> dict[str, Any]:
    selected = _as_mapping(result)
    summary = _relation_summary(selected)
    statement = _relation_statement(selected)
    basis = _as_mapping(selected.get("relation_basis"))
    return {
        "recognized": selected.get("outcome") == RELATION_RECOGNIZED,
        "selected_relation_result": _artifact_ref(selected, path, label="multi_carrier_relation"),
        "relation_type": summary.get("relation_type") or statement.get("relation_type"),
        "relation_question": summary.get("relation_question")
        or _nested(selected, "declared_relation_question", "relation_question"),
        "selected_carrier_ids": summary.get("selected_carrier_ids") or basis.get("selected_carrier_ids"),
        "selected_evidence_ids": summary.get("selected_evidence_ids") or basis.get("selected_evidence_ids"),
        "selected_evidence_outcomes": summary.get("selected_evidence_outcomes")
        or basis.get("selected_evidence_outcomes"),
        "visible_refusal_preserved": bool(summary.get("visible_refusal_preserved")),
        "visible_divergence_preserved": bool(summary.get("visible_divergence_preserved")),
        "downstream_evidence_posture_preserved": bool(
            summary.get("downstream_evidence_posture_preserved")
            or statement.get("downstream_evidence_posture_preserved")
        ),
        "current_carrier_not_selected": bool(
            summary.get("current_carrier_not_selected")
            or statement.get("current_carrier_not_selected")
        ),
        "winning_carrier_selected": bool(
            summary.get("winning_carrier_selected") or statement.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            summary.get("losing_carrier_invalidated") or statement.get("losing_carrier_invalidated")
        ),
        "source_currentness_authority_permission_created": bool(
            summary.get("source_currentness_authority_permission_created")
        ),
        "currentness_created": bool(
            summary.get("currentness_created") or statement.get("currentness_created")
        ),
        "authority_created": bool(summary.get("authority_created") or statement.get("authority_created")),
        "permission_created": bool(summary.get("permission_created") or statement.get("permission_created")),
        "source_replaced": bool(summary.get("source_replaced") or statement.get("source_replaced")),
        "carrier_hierarchy_created": bool(
            summary.get("carrier_hierarchy_created") or statement.get("carrier_hierarchy_created")
        ),
        "distributed_standing_created": bool(
            summary.get("distributed_standing_created") or statement.get("distributed_standing_created")
        ),
        "continuation_authorized": bool(
            summary.get("continuation_authorized") or statement.get("continuation_authorized")
        ),
        "downstream_only": True,
        "current_or_governing_basis": False,
        "relation_basis": basis,
        "relation_checks": _mapping_list(selected.get("relation_checks")),
        "selected_carriers": _mapping_list(selected.get("selected_carriers")),
        "selected_carrier_evidence": _mapping_list(selected.get("selected_carrier_evidence")),
        "non_claims": _section(selected, "non_claims"),
    }


def _recognized_conformance(path: Path | None, result: Mapping[str, Any] | None) -> dict[str, Any]:
    selected = _as_mapping(result)
    summary = _conformance_summary(selected)
    statement = _conformance_statement(selected)
    relation = _as_mapping(selected.get("selected_relation"))
    return {
        "recognized": selected.get("outcome") == RELATION_CONFORMANT,
        "selected_conformance_result": _artifact_ref(
            selected,
            path,
            label="multi_carrier_relation_conformance",
        ),
        "selected_relation_id": summary.get("selected_relation_id")
        or relation.get("selected_relation_result_id")
        or relation.get("result_id"),
        "selected_relation_path": summary.get("selected_relation_path")
        or relation.get("selected_relation_result_path")
        or relation.get("path"),
        "selected_relation_outcome": summary.get("selected_relation_outcome")
        or relation.get("selected_relation_outcome")
        or relation.get("outcome"),
        "selected_relation_type": summary.get("selected_relation_type")
        or relation.get("selected_relation_type")
        or relation.get("relation_type"),
        "selected_relation_question": summary.get("selected_relation_question")
        or relation.get("selected_relation_question")
        or relation.get("relation_question"),
        "selected_carrier_count": summary.get("selected_carrier_count"),
        "selected_evidence_count": summary.get("selected_evidence_count"),
        "selected_carrier_ids": summary.get("selected_carrier_ids"),
        "selected_evidence_ids": summary.get("selected_evidence_ids"),
        "selected_evidence_outcomes": summary.get("selected_evidence_outcomes"),
        "passed_check_count": summary.get("passed_check_count") or _passed_count(selected),
        "failed_check_count": summary.get("failed_check_count") or _failed_count(selected) or 0,
        "relation_conformant": bool(
            summary.get("relation_conformant") or statement.get("relation_conformant")
        ),
        "selected_relation_preserved": bool(
            summary.get("selected_relation_preserved") or statement.get("selected_relation_preserved")
        ),
        "selected_carriers_preserved": bool(
            summary.get("selected_carriers_preserved") or statement.get("selected_carriers_preserved")
        ),
        "selected_evidence_preserved": bool(
            summary.get("selected_evidence_preserved") or statement.get("selected_evidence_preserved")
        ),
        "visible_refusal_preserved": bool(
            summary.get("visible_refusal_preserved") or statement.get("visible_refusal_preserved")
        ),
        "visible_divergence_preserved": bool(
            summary.get("visible_divergence_preserved") or statement.get("visible_divergence_preserved")
        ),
        "currentness_participation_remained_participation": bool(
            summary.get("currentness_participation_remained_participation")
            or statement.get("currentness_participation_remained_participation")
        ),
        "current_carrier_not_selected": bool(
            summary.get("current_carrier_not_selected") or statement.get("current_carrier_not_selected")
        ),
        "winning_carrier_selected": bool(
            summary.get("winning_carrier_selected") or statement.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            summary.get("losing_carrier_invalidated") or statement.get("losing_carrier_invalidated")
        ),
        "carrier_hierarchy_created": bool(
            summary.get("carrier_hierarchy_created") or statement.get("carrier_hierarchy_created")
        ),
        "distributed_standing_created": bool(
            summary.get("distributed_standing_created") or statement.get("distributed_standing_created")
        ),
        "continuation_authorized": bool(
            summary.get("continuation_authorized") or statement.get("continuation_authorized")
        ),
        "additional_carrier_experiment_authorized": bool(
            summary.get("additional_carrier_experiment_authorized")
            or statement.get("additional_carrier_experiment_authorized")
        ),
        "distributed_operation_authorized": bool(
            summary.get("distributed_operation_authorized")
            or statement.get("distributed_operation_authorized")
        ),
        "downstream_only": True,
        "current_or_governing_basis": False,
        "selected_relation_basis": _section(selected, "selected_relation_basis"),
        "relation_conformance_checks": _mapping_list(selected.get("relation_conformance_checks")),
        "relation_conformance_statement": statement,
        "relation_conformance_non_meaning": _section(selected, "relation_conformance_non_meaning"),
        "selected_carriers": _mapping_list(selected.get("selected_carriers")),
        "selected_carrier_evidence": _mapping_list(selected.get("selected_carrier_evidence")),
        "non_claims": _section(selected, "non_claims"),
    }


def _recognized_closure(path: Path | None, result: Mapping[str, Any] | None) -> dict[str, Any]:
    selected = _as_mapping(result)
    summary = _closure_summary(selected)
    statement = _closure_statement(selected)
    conformance = _as_mapping(selected.get("selected_conformance"))
    relation = _as_mapping(selected.get("selected_relation"))
    return {
        "recognized": selected.get("outcome") == RELATION_CONFORMANCE_CLOSED,
        "selected_closure_result": _artifact_ref(
            selected,
            path,
            label="multi_carrier_relation_conformance_closure",
        ),
        "selected_conformance_id": summary.get("selected_conformance_id")
        or conformance.get("selected_conformance_result_id")
        or conformance.get("result_id"),
        "selected_conformance_path": summary.get("selected_conformance_path")
        or conformance.get("selected_conformance_result_path")
        or conformance.get("path"),
        "selected_conformance_outcome": summary.get("selected_conformance_outcome")
        or conformance.get("selected_conformance_outcome")
        or conformance.get("outcome"),
        "selected_relation_id": summary.get("selected_relation_id")
        or relation.get("selected_relation_result_id")
        or relation.get("result_id"),
        "selected_relation_path": summary.get("selected_relation_path")
        or relation.get("selected_relation_result_path")
        or relation.get("path"),
        "selected_relation_outcome": summary.get("selected_relation_outcome")
        or relation.get("selected_relation_outcome")
        or relation.get("outcome"),
        "selected_relation_type": summary.get("selected_relation_type")
        or relation.get("selected_relation_type")
        or relation.get("relation_type"),
        "selected_relation_question": summary.get("selected_relation_question")
        or relation.get("selected_relation_question")
        or relation.get("relation_question"),
        "selected_carrier_count": summary.get("selected_carrier_count"),
        "selected_evidence_count": summary.get("selected_evidence_count"),
        "selected_carrier_ids": summary.get("selected_carrier_ids"),
        "selected_evidence_ids": summary.get("selected_evidence_ids"),
        "selected_evidence_outcomes": summary.get("selected_evidence_outcomes"),
        "passed_check_count": summary.get("passed_check_count") or _passed_count(selected),
        "failed_check_count": summary.get("failed_check_count") or _failed_count(selected) or 0,
        "relation_conformance_closed": bool(
            summary.get("relation_conformance_closed") or statement.get("relation_conformance_closed")
        ),
        "conformance_meaning_recorded": bool(
            summary.get("conformance_meaning_recorded") or statement.get("conformance_meaning_recorded")
        ),
        "conformance_non_meaning_recorded": bool(
            summary.get("conformance_non_meaning_recorded")
            or statement.get("conformance_non_meaning_recorded")
        ),
        "selected_carriers_preserved": bool(
            summary.get("selected_carriers_preserved") or statement.get("selected_carriers_preserved")
        ),
        "selected_evidence_preserved": bool(
            summary.get("selected_evidence_preserved") or statement.get("selected_evidence_preserved")
        ),
        "visible_refusal_preserved": bool(
            summary.get("visible_refusal_preserved") or statement.get("visible_refusal_preserved")
        ),
        "visible_divergence_preserved": bool(
            summary.get("visible_divergence_preserved") or statement.get("visible_divergence_preserved")
        ),
        "currentness_participation_remained_participation": bool(
            summary.get("currentness_participation_remained_participation")
            or statement.get("currentness_participation_remained_participation")
        ),
        "current_carrier_not_selected": bool(
            summary.get("current_carrier_not_selected") or statement.get("current_carrier_not_selected")
        ),
        "winning_carrier_selected": bool(
            summary.get("winning_carrier_selected") or statement.get("winning_carrier_selected")
        ),
        "losing_carrier_invalidated": bool(
            summary.get("losing_carrier_invalidated") or statement.get("losing_carrier_invalidated")
        ),
        "carrier_hierarchy_created": bool(
            summary.get("carrier_hierarchy_created") or statement.get("carrier_hierarchy_created")
        ),
        "distributed_standing_created": bool(
            summary.get("distributed_standing_created") or statement.get("distributed_standing_created")
        ),
        "source_replaced": bool(summary.get("source_replaced") or statement.get("source_replaced")),
        "currentness_created": bool(
            summary.get("currentness_created") or statement.get("currentness_created")
        ),
        "authority_created": bool(summary.get("authority_created") or statement.get("authority_created")),
        "permission_created": bool(summary.get("permission_created") or statement.get("permission_created")),
        "source_currentness_authority_permission_created": bool(
            summary.get("source_currentness_authority_permission_created")
        ),
        "continuation_authorized": bool(
            summary.get("continuation_authorized") or statement.get("continuation_authorized")
        ),
        "additional_carrier_experiment_authorized": bool(
            summary.get("additional_carrier_experiment_authorized")
            or statement.get("additional_carrier_experiment_authorized")
        ),
        "distributed_operation_authorized": bool(
            summary.get("distributed_operation_authorized")
            or statement.get("distributed_operation_authorized")
        ),
        "closure_authorized_expansion": bool(
            summary.get("closure_authorized_expansion") or statement.get("closure_authorized_expansion")
        ),
        "self_orientation_successor_forced": bool(
            summary.get("self_orientation_successor_forced")
            or statement.get("self_orientation_successor_forced")
            or statement.get("closure_forced_self_orientation_successor")
        ),
        "conformance_successor_forced": bool(
            summary.get("conformance_successor_forced")
            or statement.get("conformance_successor_forced")
            or statement.get("closure_forced_conformance_successor")
        ),
        "downstream_only": True,
        "current_or_governing_basis": False,
        "closure_basis": _section(selected, "closure_basis"),
        "closure_checks": _mapping_list(selected.get("closure_checks")),
        "closure_statement": statement,
        "closure_non_meaning": _section(selected, "closure_non_meaning"),
        "selected_carriers": _mapping_list(selected.get("selected_carriers")),
        "selected_carrier_evidence": _mapping_list(selected.get("selected_carrier_evidence")),
        "non_claims": _section(selected, "non_claims"),
    }


def _recognized_v2(path: Path | None, result: Mapping[str, Any] | None, inherited: Any) -> dict[str, Any]:
    selected = _as_mapping(result)
    summary = _as_mapping(selected.get("current_body_conformance_pass_v2_summary"))
    statement = _as_mapping(selected.get("conformance_statement"))
    return {
        "inherited_v7_current_body_conformance_surfaces": _copy(inherited),
        "recognized_v2_current_body_conformance": selected.get("outcome") == BODY_CONFORMANT,
        "selected_current_body_conformance_v2_result": _artifact_ref(
            selected,
            path,
            label="current_body_conformance_v2",
        ),
        "v7_orientation_basis": _section(selected, "v7_orientation_basis"),
        "recognized_integrated_body_posture": _section(selected, "recognized_integrated_body_posture"),
        "conformance_statement": statement,
        "passed_check_count": summary.get("passed_check_count") or _passed_count(selected),
        "failed_check_count": summary.get("failed_check_count") or _failed_count(selected) or 0,
        "current_governing_basis_remains_upstream": bool(
            statement.get("current_governing_basis_remains_upstream")
        ),
        "downstream_surfaces_remain_downstream": bool(
            statement.get("downstream_surfaces_remain_downstream", True)
        ),
        "downstream_only": True,
        "current_or_governing_basis": False,
        "non_claims": _section(selected, "non_claims"),
    }


def _selected_inputs(
    refs: Mapping[str, tuple[Path | None, Mapping[str, Any] | None]],
    v7_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    inputs: dict[str, Any] = {
        "inherited_v7_selected_orientation_inputs": _section(
            _as_mapping(v7_result),
            "selected_orientation_inputs",
        ),
        "selection_posture": {
            "v8_uses_v7_as_successor_basis": True,
            "latest_file_currentness_refused": True,
            "multi_carrier_relation_band_downstream_only": True,
            "relation_band_does_not_determine_current_or_governing_basis": True,
        },
    }
    names = {
        "current_self_orientation_v7": "selected_current_self_orientation_v7_result",
        "current_body_conformance_v2": "selected_current_body_conformance_v2_result",
        "multi_carrier_relation": "selected_multi_carrier_relation_result",
        "multi_carrier_relation_conformance": "selected_multi_carrier_relation_conformance_result",
        "multi_carrier_relation_conformance_closure": (
            "selected_multi_carrier_relation_conformance_closure_result"
        ),
        "carrier_role_emission": "selected_carrier_role_emission_result",
        "carrier_local_emission_admission": "selected_carrier_local_emission_admission_result",
        "cross_carrier_divergence": "selected_cross_carrier_divergence_result",
        "cross_carrier_currentness": "selected_cross_carrier_currentness_result",
        "cross_carrier_receipt": "selected_cross_carrier_receipt_result",
        "returned_blocked_receipt": "selected_returned_carrier_b_blocked_receipt_result",
        "returned_successful_receipt": "selected_returned_carrier_b_successful_receipt_result",
        "cross_surface_correspondence": "selected_cross_surface_correspondence_result",
    }
    for name, key in names.items():
        path, result = refs.get(name, (None, None))
        ref = _artifact_ref(result, path, label=name)
        ref.update(
            {
                "selected": result is not None,
                "downstream_only": name != "current_self_orientation_v7",
                "current_or_governing_basis": False,
            }
        )
        inputs[key] = ref
    return inputs


def _build_checks(
    v7: Mapping[str, Any],
    v2: Mapping[str, Any],
    relation: Mapping[str, Any],
    conformance: Mapping[str, Any],
    closure: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    v7_summary = _as_mapping(v7.get("current_self_orientation_summary"))
    relation_recognized = _recognized_relation(None, relation)
    conformance_recognized = _recognized_conformance(None, conformance)
    closure_recognized = _recognized_closure(None, closure)
    sources = [v7, v2, relation, conformance, closure, non_claims]
    required_false = tuple(NON_CLAIMS)

    return [
        _check(
            "selected_v7_stands",
            bool(v7),
            "selected v7 self-orientation exists",
            bool(v7),
            "SELF_ORIENTATION_V7_MISSING",
        ),
        _check(
            "selected_v7_is_self_oriented",
            v7.get("outcome") == SELF_ORIENTED,
            "selected v7 outcome is SELF_ORIENTED",
            v7.get("outcome"),
            "SELF_ORIENTATION_V7_NOT_SELF_ORIENTED",
        ),
        _check(
            "current_governing_basis_remains_upstream",
            bool(
                v7_summary.get("current_governing_basis_recognized")
                or v7.get("recognized_governing_effective_basis")
            ),
            "current/governing basis remains inherited from v7 upstream basis",
            v7_summary.get("current_governing_basis_recognized"),
            "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS",
        ),
        _check(
            "current_body_conformance_v2_exists",
            bool(v2),
            "selected current-body conformance v2 exists",
            bool(v2),
            "CURRENT_BODY_CONFORMANCE_V2_MISSING",
        ),
        _check(
            "current_body_conformance_v2_body_conformant",
            v2.get("outcome") == BODY_CONFORMANT and _zero_failed(v2),
            "selected current-body conformance v2 is BODY_CONFORMANT with zero failed checks",
            {"outcome": v2.get("outcome"), "failed_check_count": _failed_count(v2)},
            "CURRENT_BODY_CONFORMANCE_V2_NOT_BODY_CONFORMANT",
        ),
        _check(
            "multi_carrier_relation_exists",
            bool(relation),
            "selected multi-carrier relation exists",
            bool(relation),
            "MULTI_CARRIER_RELATION_MISSING",
        ),
        _check(
            "multi_carrier_relation_recognized",
            relation.get("outcome") == RELATION_RECOGNIZED and _zero_failed(relation),
            "selected relation is MULTI_CARRIER_RELATION_RECOGNIZED with zero failed checks",
            {"outcome": relation.get("outcome"), "failed_check_count": _failed_count(relation)},
            "MULTI_CARRIER_RELATION_NOT_RECOGNIZED",
        ),
        _check(
            "multi_carrier_relation_conformance_exists",
            bool(conformance),
            "selected multi-carrier relation conformance exists",
            bool(conformance),
            "MULTI_CARRIER_RELATION_CONFORMANCE_MISSING",
        ),
        _check(
            "multi_carrier_relation_conformance_conformant",
            conformance.get("outcome") == RELATION_CONFORMANT and _zero_failed(conformance),
            "selected conformance is MULTI_CARRIER_RELATION_CONFORMANT with zero failed checks",
            {"outcome": conformance.get("outcome"), "failed_check_count": _failed_count(conformance)},
            "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CONFORMANT",
        ),
        _check(
            "multi_carrier_relation_conformance_closure_exists",
            bool(closure),
            "selected multi-carrier relation conformance closure exists",
            bool(closure),
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_MISSING",
        ),
        _check(
            "multi_carrier_relation_conformance_closure_closed",
            closure.get("outcome") == RELATION_CONFORMANCE_CLOSED and _zero_failed(closure),
            "selected closure is MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED with zero failed checks",
            {"outcome": closure.get("outcome"), "failed_check_count": _failed_count(closure)},
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_CLOSED",
        ),
        _check(
            "relation_closure_recorded_meaning",
            bool(closure_recognized.get("conformance_meaning_recorded")),
            "closure records conformance meaning",
            closure_recognized.get("conformance_meaning_recorded"),
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_CLOSED",
        ),
        _check(
            "relation_closure_recorded_non_meaning",
            bool(closure_recognized.get("conformance_non_meaning_recorded")),
            "closure records conformance non-meaning",
            closure_recognized.get("conformance_non_meaning_recorded"),
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_CLOSED",
        ),
        _check(
            "visible_refusal_preserved",
            bool(
                relation_recognized.get("visible_refusal_preserved")
                or conformance_recognized.get("visible_refusal_preserved")
                or closure_recognized.get("visible_refusal_preserved")
            ),
            "visible refusal remains visible where available",
            {
                "relation": relation_recognized.get("visible_refusal_preserved"),
                "conformance": conformance_recognized.get("visible_refusal_preserved"),
                "closure": closure_recognized.get("visible_refusal_preserved"),
            },
            "RELATION_CLOSURE_AUTHORITY_PERMISSION_LEAK",
        ),
        _check(
            "visible_divergence_preserved",
            bool(
                relation_recognized.get("visible_divergence_preserved")
                or conformance_recognized.get("visible_divergence_preserved")
                or closure_recognized.get("visible_divergence_preserved")
            ),
            "visible divergence remains visible where available",
            {
                "relation": relation_recognized.get("visible_divergence_preserved"),
                "conformance": conformance_recognized.get("visible_divergence_preserved"),
                "closure": closure_recognized.get("visible_divergence_preserved"),
            },
            "RELATION_CLOSURE_DISTRIBUTED_STANDING_LEAK",
        ),
        _check(
            "currentness_participation_remained_participation",
            bool(
                conformance_recognized.get("currentness_participation_remained_participation")
                or closure_recognized.get("currentness_participation_remained_participation")
            ),
            "currentness participation remains participation only",
            {
                "conformance": conformance_recognized.get(
                    "currentness_participation_remained_participation"
                ),
                "closure": closure_recognized.get("currentness_participation_remained_participation"),
            },
            "RELATION_CLOSURE_CURRENTNESS_LEAK",
        ),
        _check(
            "relation_band_remains_downstream",
            True,
            "relation band remains downstream posture only",
            "downstream_only",
            "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS",
        ),
        _check(
            "current_carrier_not_selected",
            bool(
                relation_recognized.get("current_carrier_not_selected")
                or conformance_recognized.get("current_carrier_not_selected")
                or closure_recognized.get("current_carrier_not_selected")
            )
            and not _any_flag_true(sources, ("current_carrier_selected",)),
            "no current carrier selected",
            _any_flag_true(sources, ("current_carrier_selected",)),
            "RELATION_CLOSURE_CURRENTNESS_LEAK",
        ),
        _check(
            "winning_losing_carrier_collapse_absent",
            not _any_flag_true(sources, ("winning_carrier_selected", "losing_carrier_invalidated")),
            "no winning carrier selected and no losing carrier invalidated",
            False,
            "RELATION_CLOSURE_CARRIER_HIERARCHY_LEAK",
        ),
        _check(
            "carrier_hierarchy_absent",
            not _any_flag_true(
                sources,
                (
                    "carrier_hierarchy_created",
                    "carrier_relation_created_hierarchy",
                    "relation_conformance_created_hierarchy",
                    "relation_conformance_closure_created_hierarchy",
                ),
            ),
            "carrier hierarchy not created",
            False,
            "RELATION_CLOSURE_CARRIER_HIERARCHY_LEAK",
        ),
        _check(
            "distributed_standing_absent",
            not _any_flag_true(sources, ("distributed_standing_created",)),
            "distributed standing not created",
            False,
            "RELATION_CLOSURE_DISTRIBUTED_STANDING_LEAK",
        ),
        _check(
            "source_currentness_authority_permission_absent",
            not _any_flag_true(
                sources,
                (
                    "source_replaced",
                    "source_created",
                    "currentness_created",
                    "authority_created",
                    "permission_created",
                    "carrier_relation_created_source",
                    "carrier_relation_created_currentness",
                    "carrier_relation_created_authority",
                    "carrier_relation_created_permission",
                    "relation_conformance_created_source",
                    "relation_conformance_created_currentness",
                    "relation_conformance_created_authority",
                    "relation_conformance_created_permission",
                    "relation_conformance_closure_created_source",
                    "relation_conformance_closure_created_currentness",
                    "relation_conformance_closure_created_authority",
                    "relation_conformance_closure_created_permission",
                ),
            ),
            "source/currentness/authority/permission remain false",
            False,
            "RELATION_CLOSURE_AUTHORITY_PERMISSION_LEAK",
        ),
        _check(
            "continuation_absent",
            not _any_flag_true(sources, ("continuation_authorized",)),
            "continuation not authorized",
            False,
            "RELATION_CLOSURE_CONTINUATION_LEAK",
        ),
        _check(
            "additional_carrier_experiment_absent",
            not _any_flag_true(sources, ("additional_carrier_experiment_authorized",)),
            "additional carrier experiment not authorized",
            False,
            "RELATION_CLOSURE_ADDITIONAL_CARRIER_EXPERIMENT_LEAK",
        ),
        _check(
            "distributed_operation_absent",
            not _any_flag_true(sources, ("distributed_operation_authorized",)),
            "distributed operation not authorized",
            False,
            "RELATION_CLOSURE_DISTRIBUTED_OPERATION_LEAK",
        ),
        _check(
            "successor_pressure_absent",
            not _any_flag_true(
                sources,
                (
                    "closure_forced_self_orientation_successor",
                    "closure_forced_conformance_successor",
                    "self_orientation_successor_forced",
                    "conformance_successor_forced",
                ),
            ),
            "closure does not force self-orientation or conformance successor",
            False,
            "RELATION_CLOSURE_SUCCESSOR_PRESSURE_LEAK",
        ),
        _check(
            "divergence_resolution_absent",
            not _any_flag_true(
                sources,
                (
                    "divergence_resolved_by_majority",
                    "divergence_resolved_by_latest_file",
                    "divergence_resolved_by_success_count",
                ),
            ),
            "divergence is not resolved by majority, latest file, or success count",
            False,
            "RELATION_CLOSURE_DISTRIBUTED_STANDING_LEAK",
        ),
        _check(
            "latest_file_currentness_absent",
            not _any_flag_true(sources, ("latest_file_currentness", "recency_fraud")),
            "latest-file currentness and recency fraud remain false",
            False,
            "LATEST_FILE_CURRENTNESS_REFUSED",
        ),
        _check(
            "mutation_replay_merge_absent",
            not _any_flag_true(sources, ("mutation_performed", "replay_performed", "merge_performed")),
            "no mutation, replay, or merge is performed",
            False,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "required_non_claims_remain_false",
            all(non_claims.get(key) is False for key in required_false),
            "all v8 required non-claims are present and false",
            _key_non_claims(non_claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]


def _metadata_for(v7_id: str | None, outcome: str) -> dict[str, Any]:
    result_id = f"{_safe_filename(v7_id)}__current_self_orientation_v8"
    return {
        "self_orientation_result_id": result_id,
        "self_orientation_result_type": "CURRENT_SELF_ORIENTATION_V8_RESULT",
        "self_orientation_result_version": SELF_ORIENTATION_RESULT_VERSION,
        "generated_at": _now(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of_module": SUCCESSOR_OF_MODULE,
        "outcome_family": [SELF_ORIENTED, BLOCKED],
        "outcome": outcome,
    }


def _block(block_code: str | None) -> dict[str, Any]:
    return {
        "blocked": block_code is not None,
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }


def _basis(
    selected_inputs: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    non_claims: Mapping[str, Any],
) -> dict[str, Any]:
    passed, failed = _counts(checks)
    return {
        "basis_statement": (
            "V8 inherits current/governing basis from v7 and recognizes the "
            "closed multi-carrier relation band as downstream posture only."
        ),
        "selected_top_level_basis_ids": {
            "current_self_orientation_v7": _nested(
                selected_inputs,
                "selected_current_self_orientation_v7_result",
                "result_id",
            ),
            "current_body_conformance_v2": _nested(
                selected_inputs,
                "selected_current_body_conformance_v2_result",
                "result_id",
            ),
            "multi_carrier_relation": _nested(
                selected_inputs,
                "selected_multi_carrier_relation_result",
                "result_id",
            ),
            "multi_carrier_relation_conformance": _nested(
                selected_inputs,
                "selected_multi_carrier_relation_conformance_result",
                "result_id",
            ),
            "multi_carrier_relation_conformance_closure": _nested(
                selected_inputs,
                "selected_multi_carrier_relation_conformance_closure_result",
                "result_id",
            ),
        },
        "current_governing_basis_source": "inherited_from_v7_upstream_basis",
        "multi_carrier_relation_band_posture": "downstream_only",
        "closed_relation_band_determines_current_or_governing_basis": False,
        "latest_file_currentness_used": False,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": _key_non_claims(non_claims),
    }


def _blocked_result(
    block_code: str,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    inputs = _copy(dict(selected_inputs or {}))
    claims = dict(NON_CLAIMS)
    claims.update(dict(non_claims or {}))
    check_records = [dict(check) for check in checks or ()]
    v7_id = _nested(inputs, "selected_current_self_orientation_v7_result", "result_id")
    result: dict[str, Any] = {
        "current_self_orientation_v8_metadata": _metadata_for(v7_id, BLOCKED),
        "selected_orientation_inputs": inputs,
        "recognized_current_executable_core_line": {},
        "recognized_governing_effective_basis": {},
        "recognized_current_state_surfaces": {},
        "recognized_continuity_surfaces": {},
        "recognized_derivative_surfaces": {},
        "recognized_operator_facing_surfaces": {},
        "recognized_reentry_surfaces": {},
        "recognized_body_signal_surfaces": {},
        "recognized_derivative_vessel_relation_surfaces": {},
        "recognized_current_body_conformance_surfaces": {},
        "recognized_post_conformance_closure_surfaces": {},
        "recognized_cross_surface_correspondence_surfaces": {},
        "recognized_cross_carrier_receipt_surfaces": {},
        "recognized_carrier_role_emission_surfaces": {},
        "recognized_carrier_local_emission_admission_surfaces": {},
        "recognized_cross_carrier_divergence_surfaces": {},
        "recognized_cross_carrier_currentness_surfaces": {},
        "recognized_multi_carrier_relation_surfaces": {},
        "recognized_multi_carrier_relation_conformance_surfaces": {},
        "recognized_multi_carrier_relation_conformance_closure_surfaces": {},
        "recognized_open_surfaces": {},
        "recognized_blocked_or_refused_surfaces": {
            "blocked": True,
            "block_code": block_code,
            "block_reason": _block_reason(block_code),
        },
        "recognized_touch_admissibility_surfaces": {},
        "bounded_correspondence_checks": check_records,
        "outcome": BLOCKED,
        "block": _block(block_code),
        "self_orientation_basis": _basis(inputs, check_records, claims),
        "current_self_orientation_summary": {},
        "non_claims": claims,
    }
    result["current_self_orientation_summary"] = build_current_self_orientation_summary(result)
    return result


def _build_result(
    refs: Mapping[str, tuple[Path | None, Mapping[str, Any] | None]],
) -> dict[str, Any]:
    v7 = _as_mapping(refs["current_self_orientation_v7"][1])
    v2 = _as_mapping(refs["current_body_conformance_v2"][1])
    relation = _as_mapping(refs["multi_carrier_relation"][1])
    conformance = _as_mapping(refs["multi_carrier_relation_conformance"][1])
    closure = _as_mapping(refs["multi_carrier_relation_conformance_closure"][1])
    sources = [_as_mapping(value) for _, value in refs.values() if value is not None]
    non_claims = _merge_non_claims(sources)
    selected_inputs = _selected_inputs(refs, v7)
    checks = _build_checks(v7, v2, relation, conformance, closure, non_claims)
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            str(failed.get("block_code") or "CURRENT_SELF_ORIENTATION_V8_BLOCKED"),
            selected_inputs=selected_inputs,
            checks=checks,
            non_claims=non_claims,
        )

    local_receipt_path, local_receipt = refs["cross_carrier_receipt"]
    blocked_receipt_path, blocked_receipt = refs["returned_blocked_receipt"]
    success_receipt_path, success_receipt = refs["returned_successful_receipt"]
    v7_id = _result_id(v7)
    result: dict[str, Any] = {
        "current_self_orientation_v8_metadata": _metadata_for(v7_id, SELF_ORIENTED),
        "selected_orientation_inputs": selected_inputs,
        "recognized_current_executable_core_line": _section(
            v7,
            "recognized_current_executable_core_line",
        ),
        "recognized_governing_effective_basis": _section(v7, "recognized_governing_effective_basis"),
        "recognized_current_state_surfaces": _section(v7, "recognized_current_state_surfaces"),
        "recognized_continuity_surfaces": _section(v7, "recognized_continuity_surfaces"),
        "recognized_derivative_surfaces": _section(v7, "recognized_derivative_surfaces"),
        "recognized_operator_facing_surfaces": _section(v7, "recognized_operator_facing_surfaces"),
        "recognized_reentry_surfaces": _section(v7, "recognized_reentry_surfaces"),
        "recognized_body_signal_surfaces": _section(v7, "recognized_body_signal_surfaces"),
        "recognized_derivative_vessel_relation_surfaces": _section(
            v7,
            "recognized_derivative_vessel_relation_surfaces",
        ),
        "recognized_current_body_conformance_surfaces": _recognized_v2(
            refs["current_body_conformance_v2"][0],
            v2,
            _section(v7, "recognized_current_body_conformance_surfaces"),
        ),
        "recognized_post_conformance_closure_surfaces": _section(
            v7,
            "recognized_post_conformance_closure_surfaces",
        ),
        "recognized_cross_surface_correspondence_surfaces": {
            "inherited_v7_cross_surface_correspondence_surfaces": _section(
                v7,
                "recognized_cross_surface_correspondence_surfaces",
            ),
            "selected_cross_surface_correspondence": _recognize_optional(
                "cross_surface_correspondence",
                refs["cross_surface_correspondence"][0],
                refs["cross_surface_correspondence"][1],
                "bounded reading relation only",
            ),
            "correspondence_does_not_create_currentness": True,
            "correspondence_does_not_create_truth_action_or_consequence": True,
        },
        "recognized_cross_carrier_receipt_surfaces": {
            "inherited_v7_cross_carrier_receipt_surfaces": _section(
                v7,
                "recognized_cross_carrier_receipt_surfaces",
            ),
            "local_receipt": _recognize_optional(
                "cross_carrier_receipt",
                local_receipt_path,
                local_receipt,
                "receipt remains receipt/evidence posture only",
            ),
            "returned_blocked_receipt": _recognize_optional(
                "returned_blocked_receipt",
                blocked_receipt_path,
                blocked_receipt,
                "returned refusal evidence remains visible and downstream",
            ),
            "returned_successful_receipt": _recognize_optional(
                "returned_successful_receipt",
                success_receipt_path,
                success_receipt,
                "returned successful receipt remains evidence and downstream",
            ),
            "carrier_b_returned_receipt_evidence_remains_downstream": True,
            "receipt_does_not_create_currentness": True,
            "receipt_does_not_create_authority": True,
            "receipt_does_not_create_distributed_standing": True,
        },
        "recognized_carrier_role_emission_surfaces": _recognize_optional(
            "carrier_role_emission",
            refs["carrier_role_emission"][0],
            refs["carrier_role_emission"][1],
            "carrier role/emission remains operation-local and bounded",
        ),
        "recognized_carrier_local_emission_admission_surfaces": _recognize_optional(
            "carrier_local_emission_admission",
            refs["carrier_local_emission_admission"][0],
            refs["carrier_local_emission_admission"][1],
            "admitted evidence remains downstream evidence posture",
        ),
        "recognized_cross_carrier_divergence_surfaces": _recognize_optional(
            "cross_carrier_divergence",
            refs["cross_carrier_divergence"][0],
            refs["cross_carrier_divergence"][1],
            "visible divergence remains visible and unresolved",
        ),
        "recognized_cross_carrier_currentness_surfaces": _recognize_optional(
            "cross_carrier_currentness",
            refs["cross_carrier_currentness"][0],
            refs["cross_carrier_currentness"][1],
            "currentness participation remains participation only",
        ),
        "recognized_multi_carrier_relation_surfaces": _recognized_relation(
            refs["multi_carrier_relation"][0],
            relation,
        ),
        "recognized_multi_carrier_relation_conformance_surfaces": _recognized_conformance(
            refs["multi_carrier_relation_conformance"][0],
            conformance,
        ),
        "recognized_multi_carrier_relation_conformance_closure_surfaces": _recognized_closure(
            refs["multi_carrier_relation_conformance_closure"][0],
            closure,
        ),
        "recognized_open_surfaces": {
            "inherited_v7_open_surfaces": _section(v7, "recognized_open_surfaces"),
            "distributed_standing": "open_not_scheduled_not_authorized_not_executed",
            "additional_physical_carrier_experiment": (
                "open_only_if_separately_declared_and_bounded"
            ),
            "distributed_operation": "open_only_if_separately_declared_and_bounded",
        },
        "recognized_blocked_or_refused_surfaces": _section(
            v7,
            "recognized_blocked_or_refused_surfaces",
        ),
        "recognized_touch_admissibility_surfaces": _section(
            v7,
            "recognized_touch_admissibility_surfaces",
        ),
        "bounded_correspondence_checks": checks,
        "outcome": SELF_ORIENTED,
        "block": _block(None),
        "self_orientation_basis": _basis(selected_inputs, checks, non_claims),
        "current_self_orientation_summary": {},
        "non_claims": non_claims,
    }
    result["current_self_orientation_summary"] = build_current_self_orientation_summary(result)
    return result


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve current self-orientation v8.

    The argument name is preserved for v7 API compatibility. In v8, the
    supplied mapping is treated as the selected v7 successor basis.
    """

    try:
        v7_path, v7 = _select_v7(body_pass_result)
        if v7 is None:
            return _blocked_result("SELF_ORIENTATION_V7_MISSING")

        v2_path, v2 = _select_body_conformance_v2(v7, v7_path)
        closure_path, closure = _select_relation_closure()
        conformance_path, conformance = _select_relation_conformance(closure)
        relation_path, relation = _select_relation(closure, conformance)
        role_path, role = _select_optional("carrier_role_emission", CARRIER_ROLE_EMISSION_ROOT)
        admission_path, admission = _select_optional(
            "carrier_local_emission_admission",
            CARRIER_LOCAL_EMISSION_ADMISSION_ROOT,
        )
        divergence_path, divergence = _select_optional(
            "cross_carrier_divergence",
            CROSS_CARRIER_DIVERGENCE_ROOT,
        )
        currentness_path, currentness = _select_optional(
            "cross_carrier_currentness",
            CROSS_CARRIER_CURRENTNESS_ROOT,
        )
        receipt_path, receipt = _select_optional(
            "cross_carrier_receipt",
            CROSS_CARRIER_SURFACE_RECEIPT_ROOT,
        )
        blocked_receipt_path, blocked_receipt = _select_optional(
            "returned_blocked_receipt",
            RETURNED_CARRIER_B_RECEIPT_ROOT,
            require_zero_failed=False,
        )
        success_receipt_path, success_receipt = _select_optional(
            "returned_successful_receipt",
            RETURNED_CARRIER_B_RECEIPT_ROOT,
        )
        correspondence_path, correspondence = _select_optional(
            "cross_surface_correspondence",
            CROSS_SURFACE_CORRESPONDENCE_ROOT,
        )

        refs: dict[str, tuple[Path | None, Mapping[str, Any] | None]] = {
            "current_self_orientation_v7": (v7_path, v7),
            "current_body_conformance_v2": (v2_path, v2),
            "multi_carrier_relation": (relation_path, relation),
            "multi_carrier_relation_conformance": (conformance_path, conformance),
            "multi_carrier_relation_conformance_closure": (closure_path, closure),
            "carrier_role_emission": (role_path, role),
            "carrier_local_emission_admission": (admission_path, admission),
            "cross_carrier_divergence": (divergence_path, divergence),
            "cross_carrier_currentness": (currentness_path, currentness),
            "cross_carrier_receipt": (receipt_path, receipt),
            "returned_blocked_receipt": (blocked_receipt_path, blocked_receipt),
            "returned_successful_receipt": (success_receipt_path, success_receipt),
            "cross_surface_correspondence": (correspondence_path, correspondence),
        }
        return _build_result(refs)
    except CurrentSelfOrientationV8Error as exc:
        return _blocked_result(exc.block_code)


def resolve_current_self_orientation_from_path(v7_result_path: Path | str) -> dict:
    selected = _read_json_mapping(
        v7_result_path,
        unreadable_code="SELF_ORIENTATION_V7_UNREADABLE",
        malformed_code="SELF_ORIENTATION_V7_MALFORMED",
    )
    return resolve_current_self_orientation(body_pass_result=selected)


def build_current_self_orientation_summary(result: Mapping[str, Any]) -> dict:
    selected_inputs = _as_mapping(result.get("selected_orientation_inputs"))
    relation = _as_mapping(result.get("recognized_multi_carrier_relation_surfaces"))
    conformance = _as_mapping(result.get("recognized_multi_carrier_relation_conformance_surfaces"))
    closure = _as_mapping(result.get("recognized_multi_carrier_relation_conformance_closure_surfaces"))
    checks = _mapping_list(result.get("bounded_correspondence_checks"))
    passed, failed = _counts(checks)
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))
    v7_ref = _as_mapping(selected_inputs.get("selected_current_self_orientation_v7_result"))
    v2_ref = _as_mapping(selected_inputs.get("selected_current_body_conformance_v2_result"))
    relation_ref = _as_mapping(selected_inputs.get("selected_multi_carrier_relation_result"))
    conformance_ref = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_result")
    )
    closure_ref = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_closure_result")
    )
    source_currentness_authority_permission_false = not any(
        _truthy_flag(
            source,
            "source_currentness_authority_permission_created",
            "source_replaced",
            "currentness_created",
            "authority_created",
            "permission_created",
        )
        for source in (relation, closure)
    )
    successor_not_forced = not _truthy_flag(
        closure,
        "self_orientation_successor_forced",
        "conformance_successor_forced",
    )
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_top_level_basis_ids": {
            "current_self_orientation_v7": v7_ref.get("result_id"),
            "current_body_conformance_v2": v2_ref.get("result_id"),
            "multi_carrier_relation": relation_ref.get("result_id"),
            "multi_carrier_relation_conformance": conformance_ref.get("result_id"),
            "multi_carrier_relation_conformance_closure": closure_ref.get("result_id"),
        },
        "selected_v7_self_orientation_id": v7_ref.get("result_id"),
        "selected_current_body_conformance_v2_id": v2_ref.get("result_id"),
        "selected_multi_carrier_relation_id": relation_ref.get("result_id"),
        "selected_multi_carrier_relation_conformance_id": conformance_ref.get("result_id"),
        "selected_multi_carrier_relation_conformance_closure_id": closure_ref.get("result_id"),
        "current_governing_basis_recognized": bool(
            result.get("recognized_governing_effective_basis")
        ),
        "current_self_orientation_v7_recognized": v7_ref.get("outcome") == SELF_ORIENTED,
        "current_body_conformance_v2_recognized": v2_ref.get("outcome") == BODY_CONFORMANT,
        "carrier_role_emission_recognized": bool(
            _nested(result, "recognized_carrier_role_emission_surfaces", "recognized")
        ),
        "carrier_local_emission_admission_recognized": bool(
            _nested(result, "recognized_carrier_local_emission_admission_surfaces", "recognized")
        ),
        "cross_carrier_divergence_recognized": bool(
            _nested(result, "recognized_cross_carrier_divergence_surfaces", "recognized")
        ),
        "cross_carrier_currentness_participation_recognized": bool(
            _nested(result, "recognized_cross_carrier_currentness_surfaces", "recognized")
        ),
        "multi_carrier_relation_recognized": bool(relation.get("recognized")),
        "multi_carrier_relation_conformance_recognized": bool(conformance.get("recognized")),
        "multi_carrier_relation_conformance_closure_recognized": bool(closure.get("recognized")),
        "relation_conformance_closure_meaning_recorded": bool(
            closure.get("conformance_meaning_recorded")
        ),
        "relation_conformance_closure_non_meaning_recorded": bool(
            closure.get("conformance_non_meaning_recorded")
        ),
        "carrier_b_returned_receipt_evidence_remains_downstream": bool(
            _nested(
                result,
                "recognized_cross_carrier_receipt_surfaces",
                "carrier_b_returned_receipt_evidence_remains_downstream",
            )
        ),
        "visible_refusal_remains_visible": bool(
            relation.get("visible_refusal_preserved")
            or conformance.get("visible_refusal_preserved")
            or closure.get("visible_refusal_preserved")
        ),
        "visible_divergence_remains_visible": bool(
            relation.get("visible_divergence_preserved")
            or conformance.get("visible_divergence_preserved")
            or closure.get("visible_divergence_preserved")
        ),
        "currentness_participation_remained_participation": bool(
            conformance.get("currentness_participation_remained_participation")
            or closure.get("currentness_participation_remained_participation")
        ),
        "current_carrier_not_selected": bool(
            relation.get("current_carrier_not_selected")
            or conformance.get("current_carrier_not_selected")
            or closure.get("current_carrier_not_selected")
        ),
        "no_winning_losing_carrier_collapse_occurred": not _truthy_flag(
            relation,
            "winning_carrier_selected",
            "losing_carrier_invalidated",
        )
        and not _truthy_flag(closure, "winning_carrier_selected", "losing_carrier_invalidated"),
        "carrier_hierarchy_stayed_false": not _truthy_flag(
            relation,
            "carrier_hierarchy_created",
        )
        and not _truthy_flag(closure, "carrier_hierarchy_created"),
        "distributed_standing_stayed_false": not _truthy_flag(
            relation,
            "distributed_standing_created",
        )
        and not _truthy_flag(closure, "distributed_standing_created"),
        "source_currentness_authority_permission_stayed_false": (
            source_currentness_authority_permission_false
        ),
        "continuation_stayed_false": not _truthy_flag(
            relation,
            "continuation_authorized",
        )
        and not _truthy_flag(closure, "continuation_authorized"),
        "additional_carrier_experiment_authorization_stayed_false": not _truthy_flag(
            closure,
            "additional_carrier_experiment_authorized",
        ),
        "distributed_operation_authorization_stayed_false": not _truthy_flag(
            closure,
            "distributed_operation_authorized",
        ),
        "self_orientation_conformance_successor_not_forced": successor_not_forced,
        "correspondence_checks_passed": failed == 0,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": _key_non_claims(non_claims),
    }


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV8Error(
            "Current self-orientation result must be a mapping.",
            block_code="CURRENT_SELF_ORIENTATION_V8_MALFORMED",
        )
    if output_path is None:
        metadata = _as_mapping(result.get("current_self_orientation_v8_metadata"))
        basis = metadata.get("self_orientation_result_id") or _nested(
            result,
            "selected_orientation_inputs",
            "selected_current_self_orientation_v7_result",
            "result_id",
        )
        target = (
            CURRENT_SELF_ORIENTATION_V8_ROOT
            / f"{_safe_filename(basis)}__current_self_orientation_v8_result.json"
        )
    else:
        target = _repo_path(output_path)

    target.parent.mkdir(parents=True, exist_ok=True)
    candidate = target
    counter = 1
    while candidate.exists():
        candidate = target.with_name(f"{target.stem}_{counter:03d}{target.suffix}")
        counter += 1
    with candidate.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
    return candidate
