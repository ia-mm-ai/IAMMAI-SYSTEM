"""Bounded current-body conformance pass over v8 self-orientation posture.

This successor pass audits one current self-orientation v8 result as the
present body line after the closed multi-carrier relation band was mirrored.
It does not replay the host, mutate standing artifacts, merge carriers, infer
currentness from latest-file recency, create authority, create permission,
create currentness, open presence/threshold/truth/action/consequence, create
distributed standing, authorize continuation, authorize another carrier
experiment, authorize distributed operation, or force another successor.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class CurrentBodyConformancePassV3Error(RuntimeError):
    """Raised for malformed explicit v3 conformance-pass input."""

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

CURRENT_SELF_ORIENTATION_V8_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v8"
)
CURRENT_SELF_ORIENTATION_V7_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v7"
)
CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass_v2"
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
CROSS_CARRIER_CURRENTNESS_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_currentness_boundary"
)
CROSS_CARRIER_DIVERGENCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_cross_carrier_divergence_boundary"
)
CARRIER_LOCAL_EMISSION_ADMISSION_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_local_emission_admission_boundary"
)
CARRIER_ROLE_EMISSION_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_role_and_emission_boundary"
)
CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass_v3"
)

RUNNER_MODULE = "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v3"
SUCCESSOR_OF_MODULE = "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2"
RESULT_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_BODY_CONFORMANCE_PASS_V3_RESULT"
RESULT_VERSION = "0.3.0"
DEFAULT_RESULT_STEM = "current_body_conformance_pass_v3_result"

BODY_CONFORMANT = "BODY_CONFORMANT"
BLOCKED = "BLOCKED"
SELF_ORIENTED = "SELF_ORIENTED"

BLOCK_REASONS = {
    "CURRENT_SELF_ORIENTATION_V8_MISSING": "No current self-orientation v8 result was supplied or discovered.",
    "CURRENT_SELF_ORIENTATION_V8_UNREADABLE": "The selected current self-orientation v8 artifact could not be read.",
    "CURRENT_SELF_ORIENTATION_V8_MALFORMED": "The selected current self-orientation v8 artifact is malformed.",
    "CURRENT_SELF_ORIENTATION_V8_NOT_SELF_ORIENTED": "The selected current self-orientation v8 result is not SELF_ORIENTED.",
    "CURRENT_SELF_ORIENTATION_V8_FAILED_CHECKS_PRESENT": "The selected current self-orientation v8 has failed checks.",
    "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED": "The v8 current/governing basis is not recognized as upstream-derived.",
    "CURRENT_SELF_ORIENTATION_V7_BASIS_MISSING": "The v8 result does not preserve selected v7 basis.",
    "CURRENT_BODY_CONFORMANCE_V2_NOT_RECOGNIZED": "The v8 result does not recognize current-body conformance v2 posture.",
    "MULTI_CARRIER_RELATION_NOT_RECOGNIZED": "The v8 result does not recognize the selected multi-carrier relation posture.",
    "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_RECOGNIZED": "The v8 result does not recognize multi-carrier relation conformance posture.",
    "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_RECOGNIZED": "The v8 result does not recognize multi-carrier relation conformance closure posture.",
    "RELATION_CLOSURE_MEANING_NOT_RECORDED": "The relation conformance closure meaning is not recorded.",
    "RELATION_CLOSURE_NON_MEANING_NOT_RECORDED": "The relation conformance closure non-meaning is not recorded.",
    "CARRIER_B_RETURNED_EVIDENCE_NOT_DOWNSTREAM": "Carrier B returned receipt evidence is not preserved as downstream evidence.",
    "VISIBLE_REFUSAL_NOT_PRESERVED": "Visible refusal evidence is not preserved.",
    "VISIBLE_DIVERGENCE_NOT_PRESERVED": "Visible divergence evidence is not preserved.",
    "CURRENTNESS_PARTICIPATION_COLLAPSED": "Currentness participation collapsed into currentness or another stronger posture.",
    "CURRENT_CARRIER_SELECTED": "A current carrier was selected.",
    "WINNING_OR_LOSING_CARRIER_COLLAPSE": "A winning carrier was selected or a losing carrier was invalidated.",
    "CARRIER_HIERARCHY_CREATED": "A carrier hierarchy was created.",
    "DISTRIBUTED_STANDING_CREATED": "Distributed standing was created.",
    "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE": "Source, currentness, authority, or permission posture collapsed.",
    "CONTINUATION_AUTHORIZED": "Continuation was authorized.",
    "ADDITIONAL_CARRIER_EXPERIMENT_AUTHORIZED": "An additional carrier experiment was authorized.",
    "DISTRIBUTED_OPERATION_AUTHORIZED": "Distributed operation was authorized.",
    "SUCCESSOR_PRESSURE_FORCED": "Self-orientation or conformance successor pressure was forced.",
    "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS": "The closed relation band was upgraded into governing basis.",
    "LATEST_FILE_CURRENTNESS_REFUSED": "Latest-file recency is being used as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required non-claim is missing or flipped.",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "source_replaced",
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
    "continuation_authorized",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy_created",
    "distributed_standing_created",
    "carrier_registry_created",
    "repository_synchronization_created",
    "additional_carrier_experiment_authorized",
    "distributed_operation_authorized",
    "relation_band_upgraded_to_governing_basis",
    "v3_conformance_created_permission",
    "v3_conformance_created_authority",
    "v3_conformance_created_currentness",
    "v3_conformance_authorized_continuation",
    "v3_conformance_authorized_expansion",
    "self_orientation_successor_forced",
    "conformance_successor_forced",
    "closure_authorized_expansion",
    "closure_forced_self_orientation_successor",
    "closure_forced_conformance_successor",
)

CONFORMANCE_NON_MEANING = {
    "authority": True,
    "permission": True,
    "currentness": True,
    "next_step_authorization": True,
    "continuation": True,
    "additional_carrier_experiment_authorization": True,
    "distributed_operation_authorization": True,
    "distributed_standing": True,
    "carrier_registry": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body": True,
    "presence": True,
    "threshold": True,
    "truth": True,
    "action": True,
    "consequence": True,
    "final_governance": True,
    "final_system_identity": True,
    "continuity_completion": True,
    "current_carrier_selected": True,
    "winning_carrier_selected": True,
    "losing_carrier_invalidated": True,
    "carrier_hierarchy": True,
    "relation_band_became_governing_basis": True,
    "self_orientation_successor_forced": True,
    "conformance_successor_forced": True,
}

WHAT_REMAINS_OPEN = {
    "post_v3_conformance_closure_if_later_required": True,
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = Path(path)
    try:
        return str(resolved.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _as_sequence(value: Any) -> list[Any]:
    return list(value) if isinstance(value, list) else []


def _nested(mapping: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = mapping
    for key in keys:
        if not isinstance(value, Mapping):
            return default
        value = value.get(key)
    return default if value is None else value


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _bool(value: Any) -> bool:
    return bool(value) if isinstance(value, bool) else bool(value)


def _safe_bool(mapping: Mapping[str, Any], key: str, default: bool = False) -> bool:
    value = mapping.get(key, default)
    return value if isinstance(value, bool) else default


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, "The v3 conformance pass was blocked.")


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any] | None:
    for check in checks:
        if not check.get("passed"):
            return dict(check)
    return None


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        text = artifact_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CurrentBodyConformancePassV3Error(
            f"Unable to read selected v8 artifact at {artifact_path}: {exc}",
            "CURRENT_SELF_ORIENTATION_V8_UNREADABLE",
        ) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CurrentBodyConformancePassV3Error(
            f"Malformed JSON in selected v8 artifact at {artifact_path}: {exc}",
            "CURRENT_SELF_ORIENTATION_V8_MALFORMED",
        ) from exc
    if not isinstance(data, Mapping):
        raise CurrentBodyConformancePassV3Error(
            f"Selected v8 artifact at {artifact_path} is not a JSON object.",
            "CURRENT_SELF_ORIENTATION_V8_MALFORMED",
        )
    return copy.deepcopy(dict(data))


def _iter_json_artifacts(root: Path) -> Iterable[tuple[Path, dict[str, Any]]]:
    if not root.exists():
        return
    for path in sorted(root.rglob("*.json")):
        if not path.is_file():
            continue
        try:
            data = _read_json_mapping(path)
        except CurrentBodyConformancePassV3Error:
            continue
        yield path, data


def _metadata_id(result: Mapping[str, Any]) -> str | None:
    metadata = _as_mapping(result.get("current_self_orientation_v8_metadata"))
    return metadata.get("self_orientation_result_id")


def _summary(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("current_self_orientation_summary"))


def _basis(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("self_orientation_basis"))


def _selected_inputs(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("selected_orientation_inputs"))


def _selected_ref(result: Mapping[str, Any], key: str) -> dict[str, Any]:
    value = _selected_inputs(result).get(key)
    if not isinstance(value, Mapping):
        return {
            "artifact_label": key.removeprefix("selected_").removesuffix("_result"),
            "selected": False,
            "result_id": None,
            "result_path": None,
            "outcome": None,
            "downstream_only": None,
            "current_or_governing_basis": None,
        }

    result_path = _first_present(value.get("result_path"), value.get("path"))
    return {
        "artifact_label": value.get("artifact_label"),
        "selected": value.get("selected"),
        "result_id": value.get("result_id"),
        "result_path": result_path,
        "path": result_path,
        "outcome": value.get("outcome"),
        "result_type": value.get("result_type"),
        "result_version": value.get("result_version"),
        "resolver_module": value.get("resolver_module"),
        "downstream_only": value.get("downstream_only"),
        "current_or_governing_basis": value.get("current_or_governing_basis"),
    }


def _check_counts_from_result(result: Mapping[str, Any]) -> tuple[int, int]:
    summary = _summary(result)
    passed = summary.get("passed_check_count")
    failed = summary.get("failed_check_count")
    if isinstance(passed, int) and isinstance(failed, int):
        return passed, failed

    checks = _as_sequence(result.get("bounded_correspondence_checks"))
    if checks:
        passed_count = sum(
            1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
        )
        failed_count = sum(
            1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False
        )
        return passed_count, failed_count

    basis = _basis(result)
    return (
        basis.get("passed_check_count") if isinstance(basis.get("passed_check_count"), int) else 0,
        basis.get("failed_check_count") if isinstance(basis.get("failed_check_count"), int) else 0,
    )


def _v8_quality_score(result: Mapping[str, Any]) -> int:
    if result.get("outcome") != SELF_ORIENTED:
        return -1
    summary = _summary(result)
    checks_passed = [
        "current_governing_basis_recognized",
        "current_self_orientation_v7_recognized",
        "current_body_conformance_v2_recognized",
        "multi_carrier_relation_recognized",
        "multi_carrier_relation_conformance_recognized",
        "multi_carrier_relation_conformance_closure_recognized",
        "relation_conformance_closure_meaning_recorded",
        "relation_conformance_closure_non_meaning_recorded",
        "visible_refusal_remains_visible",
        "visible_divergence_remains_visible",
        "currentness_participation_remained_participation",
        "carrier_hierarchy_stayed_false",
        "distributed_standing_stayed_false",
        "source_currentness_authority_permission_stayed_false",
        "continuation_stayed_false",
        "additional_carrier_experiment_authorization_stayed_false",
        "distributed_operation_authorization_stayed_false",
        "self_orientation_conformance_successor_not_forced",
        "correspondence_checks_passed",
    ]
    score = sum(1 for key in checks_passed if summary.get(key) is True)
    _, failed = _check_counts_from_result(result)
    if failed == 0:
        score += 5
    return score


def _discover_v8_result() -> tuple[dict[str, Any] | None, Path | None]:
    candidates: list[tuple[int, float, Path, dict[str, Any]]] = []
    for path, data in _iter_json_artifacts(CURRENT_SELF_ORIENTATION_V8_ROOT):
        score = _v8_quality_score(data)
        if score < 0:
            continue
        try:
            mtime = path.stat().st_mtime
        except OSError:
            mtime = 0.0
        candidates.append((score, mtime, path, data))

    if not candidates:
        return None, None

    candidates.sort(key=lambda item: (item[0], item[1], str(item[2])))
    _, _, path, data = candidates[-1]
    return copy.deepcopy(data), path


def _safe_filename_part(value: Any) -> str:
    text = str(value or DEFAULT_RESULT_STEM)
    safe = "".join(character if character.isalnum() or character in "-_" else "_" for character in text)
    safe = "_".join(part for part in safe.split("_") if part)
    return safe[:180] or DEFAULT_RESULT_STEM


def _available_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter:03d}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def _build_non_claims(result: Mapping[str, Any] | None) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    if isinstance(result, Mapping):
        for source in (
            _as_mapping(result.get("non_claims")),
            _as_mapping(_basis(result).get("key_non_claims")),
            _as_mapping(_summary(result).get("key_non_claims")),
        ):
            for key, value in source.items():
                if isinstance(value, bool):
                    non_claims[key] = value

    for key in REQUIRED_FALSE_NON_CLAIMS:
        non_claims.setdefault(key, False)
    return non_claims


def _non_claims_stand_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _source_currentness_authority_permission_false(non_claims: Mapping[str, Any]) -> bool:
    return (
        non_claims.get("source_replaced") is False
        and non_claims.get("currentness_created") is False
        and non_claims.get("authority_created") is False
        and non_claims.get("permission_created") is False
    )


def _recognized_section_bool(result: Mapping[str, Any], section_name: str, key: str) -> bool:
    section = _as_mapping(result.get(section_name))
    return section.get(key) is True


def _relation_band_stands(result: Mapping[str, Any]) -> bool:
    summary = _summary(result)
    return (
        summary.get("multi_carrier_relation_recognized") is True
        and summary.get("multi_carrier_relation_conformance_recognized") is True
        and summary.get("multi_carrier_relation_conformance_closure_recognized") is True
    )


def _downstream_evidence_posture_preserved(result: Mapping[str, Any]) -> bool:
    return _recognized_section_bool(
        result,
        "recognized_multi_carrier_relation_surfaces",
        "downstream_evidence_posture_preserved",
    ) or _recognized_section_bool(
        result,
        "recognized_multi_carrier_relation_conformance_surfaces",
        "downstream_evidence_posture_preserved",
    )


def _carrier_local_admission_posture_acceptable(result: Mapping[str, Any]) -> bool:
    summary = _summary(result)
    if summary.get("carrier_local_emission_admission_recognized") is True:
        return True
    return (
        _relation_band_stands(result)
        and summary.get("visible_refusal_remains_visible") is True
        and summary.get("visible_divergence_remains_visible") is True
        and _downstream_evidence_posture_preserved(result)
    )


def _cross_carrier_divergence_posture_acceptable(result: Mapping[str, Any]) -> bool:
    summary = _summary(result)
    if summary.get("cross_carrier_divergence_recognized") is True:
        return True
    return (
        _relation_band_stands(result)
        and summary.get("visible_refusal_remains_visible") is True
        and summary.get("visible_divergence_remains_visible") is True
    )


def _selected_conformance_inputs(
    result: Mapping[str, Any] | None,
    *,
    selected_path: Path | None,
    selection_mode: str,
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {
            "selection_mode": selection_mode,
            "selected_current_self_orientation_v8_result": {
                "result_id": None,
                "result_path": _display_path(selected_path),
                "outcome": None,
                "selected": False,
            },
        }

    summary = _summary(result)
    metadata = _as_mapping(result.get("current_self_orientation_v8_metadata"))
    selected = {
        "selection_mode": selection_mode,
        "selected_current_self_orientation_v8_result": {
            "result_id": _metadata_id(result),
            "result_path": _display_path(selected_path),
            "outcome": result.get("outcome"),
            "result_type": metadata.get("self_orientation_result_type"),
            "result_version": metadata.get("self_orientation_result_version"),
            "resolver_module": metadata.get("resolver_module"),
            "selected": True,
        },
        "selected_current_self_orientation_v7_result": _selected_ref(
            result, "selected_current_self_orientation_v7_result"
        ),
        "selected_current_body_conformance_v2_result": _selected_ref(
            result, "selected_current_body_conformance_v2_result"
        ),
        "selected_multi_carrier_relation_result": _selected_ref(
            result, "selected_multi_carrier_relation_result"
        ),
        "selected_multi_carrier_relation_conformance_result": _selected_ref(
            result, "selected_multi_carrier_relation_conformance_result"
        ),
        "selected_multi_carrier_relation_conformance_closure_result": _selected_ref(
            result, "selected_multi_carrier_relation_conformance_closure_result"
        ),
        "selected_cross_carrier_currentness_result": _selected_ref(
            result, "selected_cross_carrier_currentness_result"
        ),
        "selected_cross_carrier_divergence_result": _selected_ref(
            result, "selected_cross_carrier_divergence_result"
        ),
        "selected_carrier_local_emission_admission_result": _selected_ref(
            result, "selected_carrier_local_emission_admission_result"
        ),
        "selected_carrier_role_emission_result": _selected_ref(
            result, "selected_carrier_role_emission_result"
        ),
        "selected_cross_carrier_receipt_result": _selected_ref(
            result, "selected_cross_carrier_receipt_result"
        ),
        "selected_returned_carrier_b_blocked_receipt_result": _selected_ref(
            result, "selected_returned_carrier_b_blocked_receipt_result"
        ),
        "selected_returned_carrier_b_successful_receipt_result": _selected_ref(
            result, "selected_returned_carrier_b_successful_receipt_result"
        ),
        "selected_cross_surface_correspondence_result": _selected_ref(
            result, "selected_cross_surface_correspondence_result"
        ),
        "inherited_v7_basis": {
            "selected_v7_self_orientation_id": summary.get("selected_v7_self_orientation_id"),
            "selected_top_level_basis_ids": copy.deepcopy(
                _basis(result).get("selected_top_level_basis_ids")
            ),
            "current_governing_basis_source": _basis(result).get(
                "current_governing_basis_source"
            ),
            "current_governing_basis_recognized": summary.get(
                "current_governing_basis_recognized"
            ),
        },
        "selection_posture": copy.deepcopy(
            _as_mapping(_selected_inputs(result).get("selection_posture"))
        ),
        "hidden_repo_wide_read_posture": False,
    }
    return selected


def _v8_orientation_basis(
    result: Mapping[str, Any] | None,
    selected_inputs: Mapping[str, Any],
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {
            "basis_statement": "No current self-orientation v8 posture was available for v3 conformance.",
            "selected_v8_id": None,
            "selected_v8_path": _nested(
                selected_inputs,
                "selected_current_self_orientation_v8_result",
                "result_path",
            ),
            "selected_v8_outcome": None,
            "current_governing_basis_remains_upstream": False,
            "relation_band_is_downstream_only": False,
        }

    summary = _summary(result)
    basis = _basis(result)
    return {
        "basis_statement": "V3 audits the v8 self-orientation posture as a current-body mirror without making v8 authority.",
        "selected_v8_id": _metadata_id(result),
        "selected_v8_path": _nested(
            selected_inputs,
            "selected_current_self_orientation_v8_result",
            "result_path",
        ),
        "selected_v8_outcome": result.get("outcome"),
        "selected_v7_id": summary.get("selected_v7_self_orientation_id"),
        "selected_current_body_conformance_v2_id": summary.get(
            "selected_current_body_conformance_v2_id"
        ),
        "selected_multi_carrier_relation_id": summary.get("selected_multi_carrier_relation_id"),
        "selected_multi_carrier_relation_conformance_id": summary.get(
            "selected_multi_carrier_relation_conformance_id"
        ),
        "selected_multi_carrier_relation_conformance_closure_id": summary.get(
            "selected_multi_carrier_relation_conformance_closure_id"
        ),
        "v8_summary": copy.deepcopy(summary),
        "v8_self_orientation_basis": copy.deepcopy(basis),
        "current_governing_basis_source": basis.get("current_governing_basis_source"),
        "current_governing_basis_remains_upstream": (
            summary.get("current_governing_basis_recognized") is True
            and basis.get("current_governing_basis_source") == "inherited_from_v7_upstream_basis"
        ),
        "relation_band_is_downstream_only": (
            basis.get("multi_carrier_relation_band_posture") == "downstream_only"
            and basis.get("closed_relation_band_determines_current_or_governing_basis") is False
        ),
        "v8_is_conformance_input_not_authority": True,
        "latest_file_currentness_used": basis.get("latest_file_currentness_used") is True,
    }


def _recognized_integrated_body_posture(
    result: Mapping[str, Any] | None,
    non_claims: Mapping[str, Any],
) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {
            "posture_kind": "current_body_conformance_pass_v3_blocked_without_v8",
            "v8_posture_coherent_as_current_body_mirror": False,
        }

    summary = _summary(result)
    source_currentness_authority_permission_false = _source_currentness_authority_permission_false(
        non_claims
    )
    return {
        "posture_kind": "current_body_conformance_pass_v3_over_v8_self_orientation",
        "v8_posture_coherent_as_current_body_mirror": True,
        "current_governing_basis_remains_upstream": summary.get(
            "current_governing_basis_recognized"
        )
        is True,
        "reentry_body_signal_derivative_vessel_and_operator_surfaces_remain_downstream": True,
        "carrier_receipt_admission_divergence_currentness_relation_conformance_closure_surfaces_remain_downstream": True,
        "closed_multi_carrier_relation_band_remains_closed_in_meaning_only": (
            summary.get("multi_carrier_relation_conformance_closure_recognized") is True
        ),
        "relation_conformance_closure_meaning_preserved": summary.get(
            "relation_conformance_closure_meaning_recorded"
        )
        is True,
        "relation_conformance_closure_non_meaning_preserved": summary.get(
            "relation_conformance_closure_non_meaning_recorded"
        )
        is True,
        "carrier_b_remains_receiving_carrier_evidence_only": summary.get(
            "carrier_b_returned_receipt_evidence_remains_downstream"
        )
        is True,
        "returned_receipt_evidence_preserved": summary.get(
            "carrier_b_returned_receipt_evidence_remains_downstream"
        )
        is True,
        "visible_refusal_evidence_preserved": summary.get("visible_refusal_remains_visible")
        is True,
        "visible_divergence_evidence_preserved": summary.get("visible_divergence_remains_visible")
        is True,
        "currentness_participation_remained_participation": summary.get(
            "currentness_participation_remained_participation"
        )
        is True,
        "returned_evidence_did_not_replace_source": non_claims.get("source_replaced") is False,
        "returned_evidence_did_not_create_currentness": non_claims.get("currentness_created")
        is False,
        "all_selected_non_claims_remain_false": _non_claims_stand_false(non_claims),
        "carrier_role_emission_posture_preserved": summary.get(
            "carrier_role_emission_recognized"
        )
        is True,
        "carrier_local_emission_admission_posture_preserved": _carrier_local_admission_posture_acceptable(
            result
        ),
        "cross_carrier_divergence_posture_preserved": _cross_carrier_divergence_posture_acceptable(
            result
        ),
        "cross_carrier_currentness_participation_recognized": summary.get(
            "cross_carrier_currentness_participation_recognized"
        )
        is True,
        "multi_carrier_relation_recognized": summary.get("multi_carrier_relation_recognized")
        is True,
        "multi_carrier_relation_conformance_recognized": summary.get(
            "multi_carrier_relation_conformance_recognized"
        )
        is True,
        "multi_carrier_relation_conformance_closure_recognized": summary.get(
            "multi_carrier_relation_conformance_closure_recognized"
        )
        is True,
        "source_currentness_authority_permission_stayed_false": source_currentness_authority_permission_false,
    }


def _build_checks(
    result: Mapping[str, Any] | None,
    selected_inputs: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    if not isinstance(result, Mapping):
        return [
            _check(
                "current_self_orientation_v8_exists",
                False,
                "one selected current self-orientation v8 result exists",
                None,
                "CURRENT_SELF_ORIENTATION_V8_MISSING",
            )
        ]

    summary = _summary(result)
    basis = _basis(result)
    passed_count, failed_count = _check_counts_from_result(result)
    v8_selected_path = _nested(
        selected_inputs,
        "selected_current_self_orientation_v8_result",
        "result_path",
    )

    current_governing_upstream = (
        summary.get("current_governing_basis_recognized") is True
        and basis.get("current_governing_basis_source") == "inherited_from_v7_upstream_basis"
    )
    relation_band_downstream = (
        basis.get("multi_carrier_relation_band_posture") == "downstream_only"
        and basis.get("closed_relation_band_determines_current_or_governing_basis") is False
        and _nested(
            selected_inputs,
            "selection_posture",
            "relation_band_does_not_determine_current_or_governing_basis",
            default=True,
        )
        is True
    )
    no_current_carrier_selected = (
        summary.get("current_carrier_not_selected") is True
        and non_claims.get("current_carrier_selected") is False
    )
    no_winning_losing_collapse = (
        summary.get("no_winning_losing_carrier_collapse_occurred") is True
        and non_claims.get("winning_carrier_selected") is False
        and non_claims.get("losing_carrier_invalidated") is False
    )
    source_currentness_authority_permission_false = _source_currentness_authority_permission_false(
        non_claims
    )
    mutation_replay_merge_false = (
        non_claims.get("mutation_performed") is False
        and non_claims.get("replay_performed") is False
        and non_claims.get("merge_performed") is False
    )
    follow_on_not_authorized = (
        non_claims.get("follow_on_steps_authorized") is False
        and non_claims.get("follow_on_work_authorized") is False
    )
    successor_not_forced = (
        summary.get("self_orientation_conformance_successor_not_forced") is True
        and non_claims.get("self_orientation_successor_forced") is False
        and non_claims.get("conformance_successor_forced") is False
        and non_claims.get("closure_forced_self_orientation_successor") is False
        and non_claims.get("closure_forced_conformance_successor") is False
    )

    return [
        _check(
            "current_self_orientation_v8_exists",
            True,
            "one selected current self-orientation v8 result exists",
            {"selected_v8_path": v8_selected_path},
            "CURRENT_SELF_ORIENTATION_V8_MISSING",
        ),
        _check(
            "current_self_orientation_v8_is_self_oriented",
            result.get("outcome") == SELF_ORIENTED,
            SELF_ORIENTED,
            result.get("outcome"),
            "CURRENT_SELF_ORIENTATION_V8_NOT_SELF_ORIENTED",
        ),
        _check(
            "current_self_orientation_v8_failed_checks_absent",
            failed_count == 0,
            "failed check count is zero",
            {"passed_check_count": passed_count, "failed_check_count": failed_count},
            "CURRENT_SELF_ORIENTATION_V8_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "current_governing_basis_recognized",
            summary.get("current_governing_basis_recognized") is True,
            "current/governing basis recognized from upstream",
            summary.get("current_governing_basis_recognized"),
            "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
        ),
        _check(
            "v8_preserves_v7_basis",
            summary.get("current_self_orientation_v7_recognized") is True
            and bool(summary.get("selected_v7_self_orientation_id")),
            "v7 self-orientation basis is selected and recognized",
            {
                "current_self_orientation_v7_recognized": summary.get(
                    "current_self_orientation_v7_recognized"
                ),
                "selected_v7_self_orientation_id": summary.get(
                    "selected_v7_self_orientation_id"
                ),
            },
            "CURRENT_SELF_ORIENTATION_V7_BASIS_MISSING",
        ),
        _check(
            "current_body_conformance_v2_recognized",
            summary.get("current_body_conformance_v2_recognized") is True,
            "current-body conformance v2 recognized as downstream conformance posture",
            summary.get("current_body_conformance_v2_recognized"),
            "CURRENT_BODY_CONFORMANCE_V2_NOT_RECOGNIZED",
        ),
        _check(
            "carrier_role_emission_posture_preserved",
            summary.get("carrier_role_emission_recognized") is True,
            "carrier role/emission posture recognized downstream",
            summary.get("carrier_role_emission_recognized"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "carrier_local_emission_admission_posture_preserved",
            _carrier_local_admission_posture_acceptable(result),
            "admission posture recognized directly or preserved through standing closed relation band",
            {
                "carrier_local_emission_admission_recognized": summary.get(
                    "carrier_local_emission_admission_recognized"
                ),
                "relation_band_stands": _relation_band_stands(result),
                "downstream_evidence_posture_preserved": _downstream_evidence_posture_preserved(
                    result
                ),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "cross_carrier_divergence_posture_preserved",
            _cross_carrier_divergence_posture_acceptable(result),
            "divergence posture recognized directly or preserved through visible closed relation band",
            {
                "cross_carrier_divergence_recognized": summary.get(
                    "cross_carrier_divergence_recognized"
                ),
                "visible_divergence_remains_visible": summary.get(
                    "visible_divergence_remains_visible"
                ),
            },
            "VISIBLE_DIVERGENCE_NOT_PRESERVED",
        ),
        _check(
            "cross_carrier_currentness_participation_recognized",
            summary.get("cross_carrier_currentness_participation_recognized") is True,
            "cross-carrier currentness participation recognized as participation only",
            summary.get("cross_carrier_currentness_participation_recognized"),
            "CURRENTNESS_PARTICIPATION_COLLAPSED",
        ),
        _check(
            "multi_carrier_relation_recognized",
            summary.get("multi_carrier_relation_recognized") is True,
            "multi-carrier relation recognized downstream",
            summary.get("multi_carrier_relation_recognized"),
            "MULTI_CARRIER_RELATION_NOT_RECOGNIZED",
        ),
        _check(
            "multi_carrier_relation_conformance_recognized",
            summary.get("multi_carrier_relation_conformance_recognized") is True,
            "multi-carrier relation conformance recognized downstream",
            summary.get("multi_carrier_relation_conformance_recognized"),
            "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_RECOGNIZED",
        ),
        _check(
            "multi_carrier_relation_conformance_closure_recognized",
            summary.get("multi_carrier_relation_conformance_closure_recognized") is True,
            "multi-carrier relation conformance closure recognized downstream",
            summary.get("multi_carrier_relation_conformance_closure_recognized"),
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_RECOGNIZED",
        ),
        _check(
            "relation_closure_meaning_recorded",
            summary.get("relation_conformance_closure_meaning_recorded") is True,
            "relation conformance closure meaning is recorded",
            summary.get("relation_conformance_closure_meaning_recorded"),
            "RELATION_CLOSURE_MEANING_NOT_RECORDED",
        ),
        _check(
            "relation_closure_non_meaning_recorded",
            summary.get("relation_conformance_closure_non_meaning_recorded") is True,
            "relation conformance closure non-meaning is recorded",
            summary.get("relation_conformance_closure_non_meaning_recorded"),
            "RELATION_CLOSURE_NON_MEANING_NOT_RECORDED",
        ),
        _check(
            "carrier_b_returned_receipt_evidence_remains_downstream",
            summary.get("carrier_b_returned_receipt_evidence_remains_downstream") is True,
            "Carrier B returned receipt evidence remains downstream",
            summary.get("carrier_b_returned_receipt_evidence_remains_downstream"),
            "CARRIER_B_RETURNED_EVIDENCE_NOT_DOWNSTREAM",
        ),
        _check(
            "visible_refusal_preserved",
            summary.get("visible_refusal_remains_visible") is True,
            "visible refusal remains visible",
            summary.get("visible_refusal_remains_visible"),
            "VISIBLE_REFUSAL_NOT_PRESERVED",
        ),
        _check(
            "visible_divergence_preserved",
            summary.get("visible_divergence_remains_visible") is True,
            "visible divergence remains visible",
            summary.get("visible_divergence_remains_visible"),
            "VISIBLE_DIVERGENCE_NOT_PRESERVED",
        ),
        _check(
            "currentness_participation_remained_participation",
            summary.get("currentness_participation_remained_participation") is True,
            "currentness participation remains participation only",
            summary.get("currentness_participation_remained_participation"),
            "CURRENTNESS_PARTICIPATION_COLLAPSED",
        ),
        _check(
            "current_carrier_not_selected",
            no_current_carrier_selected,
            "no current carrier selected",
            {
                "current_carrier_not_selected": summary.get("current_carrier_not_selected"),
                "current_carrier_selected": non_claims.get("current_carrier_selected"),
            },
            "CURRENT_CARRIER_SELECTED",
        ),
        _check(
            "winning_carrier_not_selected",
            no_winning_losing_collapse and non_claims.get("winning_carrier_selected") is False,
            "winning carrier selected remains false",
            {
                "no_winning_losing_carrier_collapse_occurred": summary.get(
                    "no_winning_losing_carrier_collapse_occurred"
                ),
                "winning_carrier_selected": non_claims.get("winning_carrier_selected"),
            },
            "WINNING_OR_LOSING_CARRIER_COLLAPSE",
        ),
        _check(
            "losing_carrier_not_invalidated",
            no_winning_losing_collapse and non_claims.get("losing_carrier_invalidated") is False,
            "losing carrier invalidated remains false",
            {
                "no_winning_losing_carrier_collapse_occurred": summary.get(
                    "no_winning_losing_carrier_collapse_occurred"
                ),
                "losing_carrier_invalidated": non_claims.get("losing_carrier_invalidated"),
            },
            "WINNING_OR_LOSING_CARRIER_COLLAPSE",
        ),
        _check(
            "carrier_hierarchy_stayed_false",
            summary.get("carrier_hierarchy_stayed_false") is True
            and non_claims.get("carrier_hierarchy_created") is False,
            "carrier hierarchy stayed false",
            {
                "carrier_hierarchy_stayed_false": summary.get("carrier_hierarchy_stayed_false"),
                "carrier_hierarchy_created": non_claims.get("carrier_hierarchy_created"),
            },
            "CARRIER_HIERARCHY_CREATED",
        ),
        _check(
            "distributed_standing_stayed_false",
            summary.get("distributed_standing_stayed_false") is True
            and non_claims.get("distributed_standing_created") is False,
            "distributed standing stayed false",
            {
                "distributed_standing_stayed_false": summary.get(
                    "distributed_standing_stayed_false"
                ),
                "distributed_standing_created": non_claims.get("distributed_standing_created"),
            },
            "DISTRIBUTED_STANDING_CREATED",
        ),
        _check(
            "source_currentness_authority_permission_stayed_false",
            summary.get("source_currentness_authority_permission_stayed_false") is True
            and source_currentness_authority_permission_false,
            "source/currentness/authority/permission stayed false",
            {
                "source_currentness_authority_permission_stayed_false": summary.get(
                    "source_currentness_authority_permission_stayed_false"
                ),
                "source_replaced": non_claims.get("source_replaced"),
                "currentness_created": non_claims.get("currentness_created"),
                "authority_created": non_claims.get("authority_created"),
                "permission_created": non_claims.get("permission_created"),
            },
            "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE",
        ),
        _check(
            "continuation_stayed_false",
            summary.get("continuation_stayed_false") is True
            and non_claims.get("continuation_authorized") is False,
            "continuation stayed false",
            {
                "continuation_stayed_false": summary.get("continuation_stayed_false"),
                "continuation_authorized": non_claims.get("continuation_authorized"),
            },
            "CONTINUATION_AUTHORIZED",
        ),
        _check(
            "additional_carrier_experiment_not_authorized",
            summary.get("additional_carrier_experiment_authorization_stayed_false") is True
            and non_claims.get("additional_carrier_experiment_authorized") is False,
            "additional carrier experiment authorization stayed false",
            {
                "additional_carrier_experiment_authorization_stayed_false": summary.get(
                    "additional_carrier_experiment_authorization_stayed_false"
                ),
                "additional_carrier_experiment_authorized": non_claims.get(
                    "additional_carrier_experiment_authorized"
                ),
            },
            "ADDITIONAL_CARRIER_EXPERIMENT_AUTHORIZED",
        ),
        _check(
            "distributed_operation_not_authorized",
            summary.get("distributed_operation_authorization_stayed_false") is True
            and non_claims.get("distributed_operation_authorized") is False,
            "distributed operation authorization stayed false",
            {
                "distributed_operation_authorization_stayed_false": summary.get(
                    "distributed_operation_authorization_stayed_false"
                ),
                "distributed_operation_authorized": non_claims.get(
                    "distributed_operation_authorized"
                ),
            },
            "DISTRIBUTED_OPERATION_AUTHORIZED",
        ),
        _check(
            "self_orientation_conformance_successor_not_forced",
            successor_not_forced,
            "self-orientation/conformance successor not forced by closure or v3",
            {
                "self_orientation_conformance_successor_not_forced": summary.get(
                    "self_orientation_conformance_successor_not_forced"
                ),
                "self_orientation_successor_forced": non_claims.get(
                    "self_orientation_successor_forced"
                ),
                "conformance_successor_forced": non_claims.get("conformance_successor_forced"),
            },
            "SUCCESSOR_PRESSURE_FORCED",
        ),
        _check(
            "v8_current_governing_basis_stayed_upstream",
            current_governing_upstream,
            "v8 current/governing basis stayed inherited from v7 upstream basis",
            {
                "current_governing_basis_recognized": summary.get(
                    "current_governing_basis_recognized"
                ),
                "current_governing_basis_source": basis.get("current_governing_basis_source"),
            },
            "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
        ),
        _check(
            "relation_band_stayed_downstream",
            relation_band_downstream,
            "closed multi-carrier relation band stayed downstream",
            {
                "multi_carrier_relation_band_posture": basis.get(
                    "multi_carrier_relation_band_posture"
                ),
                "relation_band_does_not_determine_current_or_governing_basis": _nested(
                    selected_inputs,
                    "selection_posture",
                    "relation_band_does_not_determine_current_or_governing_basis",
                ),
            },
            "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS",
        ),
        _check(
            "closed_relation_band_did_not_become_governing_basis",
            basis.get("closed_relation_band_determines_current_or_governing_basis") is False
            and non_claims.get("relation_band_upgraded_to_governing_basis") is False,
            "closed relation band did not become current/governing basis",
            {
                "closed_relation_band_determines_current_or_governing_basis": basis.get(
                    "closed_relation_band_determines_current_or_governing_basis"
                ),
                "relation_band_upgraded_to_governing_basis": non_claims.get(
                    "relation_band_upgraded_to_governing_basis"
                ),
            },
            "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS",
        ),
        _check(
            "latest_file_currentness_false",
            non_claims.get("latest_file_currentness") is False
            and basis.get("latest_file_currentness_used") is not True,
            "latest-file currentness false",
            {
                "latest_file_currentness": non_claims.get("latest_file_currentness"),
                "latest_file_currentness_used": basis.get("latest_file_currentness_used"),
            },
            "LATEST_FILE_CURRENTNESS_REFUSED",
        ),
        _check(
            "recency_fraud_false",
            non_claims.get("recency_fraud") is False,
            "recency fraud false",
            non_claims.get("recency_fraud"),
            "LATEST_FILE_CURRENTNESS_REFUSED",
        ),
        _check(
            "mutation_replay_merge_false",
            mutation_replay_merge_false,
            "mutation, replay, and merge remain false",
            {
                "mutation_performed": non_claims.get("mutation_performed"),
                "replay_performed": non_claims.get("replay_performed"),
                "merge_performed": non_claims.get("merge_performed"),
            },
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "follow_on_work_not_authorized",
            follow_on_not_authorized,
            "follow-on work is not authorized by v3 conformance",
            {
                "follow_on_steps_authorized": non_claims.get("follow_on_steps_authorized"),
                "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "required_non_claims_remain_false",
            _non_claims_stand_false(non_claims),
            "all required v3 non-claims remain false",
            {key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]


def _conformance_statement(
    outcome: str,
    posture: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    conformant = outcome == BODY_CONFORMANT
    checks_pass = all(check.get("passed") is True for check in checks)
    return {
        "v8_body_posture_conformant": conformant and checks_pass,
        "current_governing_basis_remains_upstream": conformant
        and posture.get("current_governing_basis_remains_upstream") is True,
        "downstream_surfaces_remain_downstream": conformant
        and posture.get(
            "carrier_receipt_admission_divergence_currentness_relation_conformance_closure_surfaces_remain_downstream"
        )
        is True,
        "closed_multi_carrier_relation_band_remains_downstream": conformant
        and posture.get("closed_multi_carrier_relation_band_remains_closed_in_meaning_only")
        is True,
        "relation_conformance_closure_meaning_preserved": conformant
        and posture.get("relation_conformance_closure_meaning_preserved") is True,
        "relation_conformance_closure_non_meaning_preserved": conformant
        and posture.get("relation_conformance_closure_non_meaning_preserved") is True,
        "carrier_b_remained_receiving_carrier_evidence_only": conformant
        and posture.get("carrier_b_remains_receiving_carrier_evidence_only") is True,
        "returned_receipt_evidence_preserved": conformant
        and posture.get("returned_receipt_evidence_preserved") is True,
        "visible_refusal_evidence_preserved": conformant
        and posture.get("visible_refusal_evidence_preserved") is True,
        "visible_divergence_evidence_preserved": conformant
        and posture.get("visible_divergence_evidence_preserved") is True,
        "currentness_participation_remained_participation": conformant
        and posture.get("currentness_participation_remained_participation") is True,
        "no_current_carrier_selected": conformant,
        "no_winning_carrier_selected": conformant,
        "no_losing_carrier_invalidated": conformant,
        "no_carrier_hierarchy_created": conformant,
        "no_authority_created": conformant,
        "no_permission_created": conformant,
        "no_currentness_created": conformant,
        "no_source_replaced": conformant,
        "no_distributed_standing_created": conformant,
        "no_presence_threshold_truth_action_consequence_created": conformant,
        "no_continuation_authorized": conformant,
        "no_additional_carrier_experiment_authorized": conformant,
        "no_distributed_operation_authorized": conformant,
        "no_successor_forced": conformant,
    }


def _block(block_code: str | None) -> dict[str, Any]:
    return {
        "blocked": block_code is not None,
        "block_code": block_code,
        "block_reason": _block_reason(block_code),
    }


def _result_id(selected_v8_id: str | None, outcome: str) -> str:
    base = selected_v8_id or DEFAULT_RESULT_STEM
    suffix = "body_conformant" if outcome == BODY_CONFORMANT else "blocked"
    return f"{base}__current_body_conformance_pass_v3_{suffix}"


def _build_result(
    result: Mapping[str, Any] | None,
    selected_path: Path | None,
    selection_mode: str,
    checks: Sequence[Mapping[str, Any]],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    selected_inputs = _selected_conformance_inputs(
        result, selected_path=selected_path, selection_mode=selection_mode
    )
    v8_basis = _v8_orientation_basis(result, selected_inputs)
    integrated_posture = _recognized_integrated_body_posture(result, non_claims)
    failed = _first_failed(checks)
    block_code = failed.get("block_code") if failed else None
    outcome = BLOCKED if block_code else BODY_CONFORMANT
    selected_v8_id = _nested(
        selected_inputs,
        "selected_current_self_orientation_v8_result",
        "result_id",
    )

    artifact: dict[str, Any] = {
        "current_body_conformance_pass_v3_metadata": {
            "current_body_conformance_pass_v3_result_id": _result_id(
                selected_v8_id, outcome
            ),
            "current_body_conformance_pass_v3_result_type": RESULT_TYPE,
            "current_body_conformance_pass_v3_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RUNNER_MODULE,
            "successor_of_module": SUCCESSOR_OF_MODULE,
        },
        "selected_conformance_inputs": selected_inputs,
        "v8_orientation_basis": v8_basis,
        "recognized_integrated_body_posture": integrated_posture,
        "conformance_checks": [copy.deepcopy(dict(check)) for check in checks],
        "conformance_statement": _conformance_statement(
            outcome, integrated_posture, checks
        ),
        "conformance_non_meaning": copy.deepcopy(CONFORMANCE_NON_MEANING),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": copy.deepcopy(dict(non_claims)),
        "outcome": outcome,
        "block": _block(block_code),
        "current_body_conformance_pass_v3_summary": {},
    }
    artifact["current_body_conformance_pass_v3_summary"] = (
        build_current_body_conformance_pass_v3_summary(artifact)
    )
    return artifact


def _malformed_result(block_code: str, reason: str) -> dict[str, Any]:
    non_claims = _build_non_claims(None)
    selected_inputs = _selected_conformance_inputs(
        None, selected_path=None, selection_mode="blocked_explicit_input"
    )
    checks = [
        _check(
            "current_self_orientation_v8_exists",
            block_code != "CURRENT_SELF_ORIENTATION_V8_MISSING",
            "one selected current self-orientation v8 result exists",
            reason,
            "CURRENT_SELF_ORIENTATION_V8_MISSING",
        ),
        _check(
            "current_self_orientation_v8_is_parseable_mapping",
            False,
            "selected v8 result is a parseable JSON object/mapping",
            reason,
            block_code,
        ),
    ]
    artifact = _build_result(None, None, "blocked_explicit_input", checks, non_claims)
    artifact["block"] = {
        "blocked": True,
        "block_code": block_code,
        "block_reason": reason,
    }
    artifact["outcome"] = BLOCKED
    artifact["current_body_conformance_pass_v3_summary"] = (
        build_current_body_conformance_pass_v3_summary(artifact)
    )
    return artifact


def run_current_body_conformance_pass_v3(
    current_self_orientation_v8_result: Mapping[str, Any] | None = None,
) -> dict:
    """Run bounded v3 current-body conformance over one v8 result."""

    selected_path: Path | None = None
    selection_mode = "explicit_mapping"

    if current_self_orientation_v8_result is None:
        selected, selected_path = _discover_v8_result()
        selection_mode = "successful_v8_artifact_discovery"
        if selected is None:
            checks = [
                _check(
                    "current_self_orientation_v8_exists",
                    False,
                    "one successful SELF_ORIENTED v8 artifact is discoverable",
                    None,
                    "CURRENT_SELF_ORIENTATION_V8_MISSING",
                )
            ]
            return _build_result(None, None, selection_mode, checks, _build_non_claims(None))
    elif not isinstance(current_self_orientation_v8_result, Mapping):
        return _malformed_result(
            "CURRENT_SELF_ORIENTATION_V8_MALFORMED",
            "Selected current self-orientation v8 input is not a mapping.",
        )
    else:
        selected = copy.deepcopy(dict(current_self_orientation_v8_result))

    non_claims = _build_non_claims(selected)
    selected_inputs = _selected_conformance_inputs(
        selected, selected_path=selected_path, selection_mode=selection_mode
    )
    checks = _build_checks(selected, selected_inputs, non_claims)
    return _build_result(selected, selected_path, selection_mode, checks, non_claims)


def run_current_body_conformance_pass_v3_from_path(
    current_self_orientation_v8_result_path: Path | str,
) -> dict:
    """Run bounded v3 conformance from one explicit v8 artifact path."""

    selected_path = Path(current_self_orientation_v8_result_path)
    try:
        selected = _read_json_mapping(selected_path)
    except CurrentBodyConformancePassV3Error as exc:
        return _malformed_result(exc.block_code, str(exc))

    non_claims = _build_non_claims(selected)
    selected_inputs = _selected_conformance_inputs(
        selected, selected_path=selected_path, selection_mode="explicit_path"
    )
    checks = _build_checks(selected, selected_inputs, non_claims)
    return _build_result(selected, selected_path, "explicit_path", checks, non_claims)


def build_current_body_conformance_pass_v3_summary(result: Mapping[str, Any]) -> dict:
    """Build a bounded summary of a v3 current-body conformance result."""

    selected_inputs = _as_mapping(result.get("selected_conformance_inputs"))
    statement = _as_mapping(result.get("conformance_statement"))
    posture = _as_mapping(result.get("recognized_integrated_body_posture"))
    block = _as_mapping(result.get("block"))
    checks = _as_sequence(result.get("conformance_checks"))
    non_claims = _as_mapping(result.get("non_claims"))

    passed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
    )
    failed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False
    )

    selected_v8 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v8_result"))
    selected_v7 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v7_result"))
    selected_v2 = _as_mapping(selected_inputs.get("selected_current_body_conformance_v2_result"))
    selected_relation = _as_mapping(selected_inputs.get("selected_multi_carrier_relation_result"))
    selected_relation_conformance = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_result")
    )
    selected_relation_closure = _as_mapping(
        selected_inputs.get("selected_multi_carrier_relation_conformance_closure_result")
    )

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_v8_id": selected_v8.get("result_id"),
        "selected_v8_path": selected_v8.get("result_path"),
        "selected_v8_outcome": selected_v8.get("outcome"),
        "selected_v7_id": selected_v7.get("result_id"),
        "selected_current_body_conformance_v2_id": selected_v2.get("result_id"),
        "selected_multi_carrier_relation_id": selected_relation.get("result_id"),
        "selected_multi_carrier_relation_conformance_id": selected_relation_conformance.get(
            "result_id"
        ),
        "selected_multi_carrier_relation_conformance_closure_id": selected_relation_closure.get(
            "result_id"
        ),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "v8_body_posture_conformant": statement.get("v8_body_posture_conformant") is True,
        "current_governing_basis_upstream": statement.get(
            "current_governing_basis_remains_upstream"
        )
        is True,
        "downstream_surfaces_downstream": statement.get(
            "downstream_surfaces_remain_downstream"
        )
        is True,
        "closed_multi_carrier_relation_band_downstream": statement.get(
            "closed_multi_carrier_relation_band_remains_downstream"
        )
        is True,
        "relation_closure_meaning_preserved": statement.get(
            "relation_conformance_closure_meaning_preserved"
        )
        is True,
        "relation_closure_non_meaning_preserved": statement.get(
            "relation_conformance_closure_non_meaning_preserved"
        )
        is True,
        "carrier_b_receiving_evidence_only": statement.get(
            "carrier_b_remained_receiving_carrier_evidence_only"
        )
        is True,
        "returned_evidence_preserved": statement.get("returned_receipt_evidence_preserved")
        is True,
        "visible_refusal_preserved": statement.get("visible_refusal_evidence_preserved")
        is True,
        "visible_divergence_preserved": statement.get("visible_divergence_evidence_preserved")
        is True,
        "currentness_participation_remained_participation": statement.get(
            "currentness_participation_remained_participation"
        )
        is True,
        "no_current_winning_losing_carrier_collapse": (
            statement.get("no_current_carrier_selected") is True
            and statement.get("no_winning_carrier_selected") is True
            and statement.get("no_losing_carrier_invalidated") is True
        ),
        "no_carrier_hierarchy": statement.get("no_carrier_hierarchy_created") is True,
        "no_authority_permission_currentness_source_replacement": (
            statement.get("no_authority_created") is True
            and statement.get("no_permission_created") is True
            and statement.get("no_currentness_created") is True
            and statement.get("no_source_replaced") is True
        ),
        "no_distributed_standing": statement.get("no_distributed_standing_created") is True,
        "no_presence_threshold_truth_action_consequence": statement.get(
            "no_presence_threshold_truth_action_consequence_created"
        )
        is True,
        "no_continuation": statement.get("no_continuation_authorized") is True,
        "no_additional_carrier_experiment": statement.get(
            "no_additional_carrier_experiment_authorized"
        )
        is True,
        "no_distributed_operation": statement.get("no_distributed_operation_authorized")
        is True,
        "no_successor_forced": statement.get("no_successor_forced") is True,
        "carrier_local_emission_admission_posture_preserved": posture.get(
            "carrier_local_emission_admission_posture_preserved"
        )
        is True,
        "cross_carrier_divergence_posture_preserved": posture.get(
            "cross_carrier_divergence_posture_preserved"
        )
        is True,
        "key_non_claims": {
            key: non_claims.get(key) for key in REQUIRED_FALSE_NON_CLAIMS
        },
    }


def write_current_body_conformance_pass_v3_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v3 conformance result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformancePassV3Error(
            "Current-body conformance pass v3 result must be a mapping.",
            "CURRENT_SELF_ORIENTATION_V8_MALFORMED",
        )

    if output_path is None:
        selected_v8_id = _nested(
            result,
            "selected_conformance_inputs",
            "selected_current_self_orientation_v8_result",
            "result_id",
        )
        filename = (
            f"{_safe_filename_part(selected_v8_id or DEFAULT_RESULT_STEM)}"
            "__current_body_conformance_pass_v3_result.json"
        )
        target = CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT / filename
    else:
        target = Path(output_path)

    target = _available_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return target
