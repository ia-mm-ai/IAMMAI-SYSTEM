"""Bounded current-body conformance pass over v7 self-orientation posture.

This successor pass audits one current self-orientation v7 result as an
integrated current body line. It does not replay the host, mutate standing
artifacts, merge carrier evidence, infer currentness from latest-file recency,
create authority, create permission, create currentness, create signal posture,
open presence, threshold, truth, action, consequence, multi-carrier law,
distributed standing, successor standing, or authorize continuation.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class CurrentBodyConformancePassV2Error(RuntimeError):
    """Raised for malformed explicit v2 conformance-pass input."""

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

CURRENT_SELF_ORIENTATION_V7_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v7"
)
CURRENT_SELF_ORIENTATION_V6_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)
PREVIOUS_CURRENT_BODY_CONFORMANCE_ROOT = (
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
CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass_v2"
)

RUNNER_MODULE = "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2"
SUCCESSOR_OF_MODULE = "run_integrity_host_v0_min_coexistence_current_body_conformance_pass"
RESULT_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_BODY_CONFORMANCE_PASS_V2_RESULT"
RESULT_VERSION = "0.2.0"
DEFAULT_RESULT_STEM = "current_body_conformance_pass_v2_result"

BODY_CONFORMANT = "BODY_CONFORMANT"
BLOCKED = "BLOCKED"
SELF_ORIENTED = "SELF_ORIENTED"

BLOCK_REASONS = {
    "CURRENT_SELF_ORIENTATION_V7_MISSING": "No current self-orientation v7 result was supplied or discovered.",
    "CURRENT_SELF_ORIENTATION_V7_UNREADABLE": "The selected current self-orientation v7 artifact could not be read.",
    "CURRENT_SELF_ORIENTATION_V7_MALFORMED": "The selected current self-orientation v7 artifact is malformed.",
    "CURRENT_SELF_ORIENTATION_V7_NOT_SELF_ORIENTED": "The selected current self-orientation v7 result is not SELF_ORIENTED.",
    "CURRENT_SELF_ORIENTATION_V7_FAILED_CHECKS_PRESENT": "The selected current self-orientation v7 has failed checks.",
    "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED": "The v7 current/governing basis is not recognized as upstream.",
    "CURRENT_SELF_ORIENTATION_V6_BASIS_MISSING": "The v7 result does not preserve selected v6 basis.",
    "CURRENT_BODY_CONFORMANCE_NOT_RECOGNIZED": "The v7 result does not recognize current-body conformance posture.",
    "POST_CONFORMANCE_CLOSURE_NOT_RECOGNIZED": "The v7 result does not recognize post-conformance closure posture.",
    "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED": "The v7 result does not recognize cross-surface correspondence posture.",
    "CROSS_CARRIER_RECEIPT_NOT_RECOGNIZED": "The v7 result does not recognize cross-carrier receipt posture.",
    "RETURNED_CARRIER_B_RECEIPT_EVIDENCE_NOT_RECOGNIZED": "The v7 result does not recognize returned Carrier B receipt evidence.",
    "RETURNED_CARRIER_B_REFUSAL_EVIDENCE_NOT_VISIBLE": "The v7 result does not preserve visible returned Carrier B refusal evidence.",
    "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED": "The v7 result does not recognize receipt-alignment correspondence.",
    "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED": "The v7 result does not recognize refusal-visible correspondence.",
    "CARRIER_B_RECEIVING_ONLY_POSTURE_FAILED": "Carrier B was not preserved as receiving-carrier evidence only.",
    "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_SUCCESSOR_BODY_COLLAPSE": "Source, currentness, authority, permission, successor, or body posture collapsed.",
    "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION": "Conformance leaked authority, permission, or currentness.",
    "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION": "Closure leaked authority, permission, signal, or continuation.",
    "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION": "Correspondence leaked authority, currentness, permission, signal, presence, threshold, truth, action, or consequence.",
    "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR": "Receipt leaked source, currentness, authority, permission, successor, or body posture.",
    "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE": "Receipt leaked signal, presence, threshold, truth, action, or consequence.",
    "MULTI_CARRIER_LAW_CREATED": "Multi-carrier law was created.",
    "DISTRIBUTED_STANDING_CREATED": "Distributed standing was created.",
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
    "v2_conformance_created_permission",
    "v2_conformance_created_authority",
    "v2_conformance_created_currentness",
    "v2_conformance_authorized_continuation",
)

NON_MEANING = {
    "does_not_create_authority": True,
    "does_not_create_permission": True,
    "does_not_create_currentness": True,
    "does_not_authorize_next_step": True,
    "does_not_authorize_continuation": True,
    "does_not_establish_presence": True,
    "does_not_establish_threshold": True,
    "does_not_create_truth": True,
    "does_not_authorize_action": True,
    "does_not_create_consequence": True,
    "does_not_complete_final_governance": True,
    "does_not_complete_final_system_identity": True,
    "does_not_complete_continuity": True,
    "does_not_create_multi_carrier_law": True,
    "does_not_create_distributed_standing": True,
    "does_not_create_carrier_registry": True,
    "does_not_synchronize_repository": True,
    "does_not_transfer_full_body": True,
    "does_not_create_second_body": True,
    "does_not_create_external_contact": True,
    "does_not_force_self_orientation_successor": True,
    "does_not_force_conformance_successor": True,
}

OPEN_SURFACES = {
    "post-v2 conformance closure, if later required": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "multi-carrier relation law": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "distributed standing": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "persistence/registry law": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "presence law": {"not_scheduled": True, "not_authorized": True, "not_executed": True},
    "threshold law": {"not_scheduled": True, "not_authorized": True, "not_executed": True},
    "truth law": {"not_scheduled": True, "not_authorized": True, "not_executed": True},
    "action/consequence law": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "generalized vessel relation lifecycle": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "body relevance medium": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "signal series or accumulation logic": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
    "future self-orientation successor only if separately justified": {
        "not_scheduled": True,
        "not_authorized": True,
        "not_executed": True,
    },
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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


def _safe_filename_part(value: Any) -> str:
    text = value if isinstance(value, str) and value else DEFAULT_RESULT_STEM
    allowed = []
    for character in text:
        allowed.append(character if character.isalnum() or character in "._-" else "_")
    stem = "".join(allowed).strip("._")
    return stem[:180] or DEFAULT_RESULT_STEM


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


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "Bounded current-body conformance v2 refused.")
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


def _read_json_mapping(
    path: Path | str,
    *,
    unreadable_code: str = "CURRENT_SELF_ORIENTATION_V7_UNREADABLE",
    malformed_code: str = "CURRENT_SELF_ORIENTATION_V7_MALFORMED",
) -> dict[str, Any]:
    target = _repo_path(path)
    if not target.is_file():
        raise CurrentBodyConformancePassV2Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        )
    try:
        with target.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except json.JSONDecodeError as exc:
        raise CurrentBodyConformancePassV2Error(
            f"required JSON artifact is malformed: {_display_path(target)}",
            malformed_code,
        ) from exc
    except OSError as exc:
        raise CurrentBodyConformancePassV2Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CurrentBodyConformancePassV2Error(
            f"required JSON artifact is not an object: {_display_path(target)}",
            malformed_code,
        )
    return copy.deepcopy(dict(loaded))


def _iter_json_artifacts(root: Path | str) -> list[tuple[Path, dict[str, Any]]]:
    resolved = _repo_path(root)
    if not resolved.exists() or not resolved.is_dir():
        return []
    artifacts: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(resolved.glob("*.json")):
        if path.is_file():
            artifacts.append(
                (
                    path,
                    _read_json_mapping(
                        path,
                        unreadable_code="CURRENT_SELF_ORIENTATION_V7_MALFORMED",
                        malformed_code="CURRENT_SELF_ORIENTATION_V7_MALFORMED",
                    ),
                )
            )
    return artifacts


def _result_id(result: Mapping[str, Any] | None) -> str | None:
    if not isinstance(result, Mapping):
        return None
    value = _nested(result, "current_self_orientation_v7_metadata", "self_orientation_result_id")
    return str(value) if _string_or_none(value) else None


def _selected_ref(selected: Mapping[str, Any], key: str) -> dict[str, Any]:
    return _as_mapping(selected.get(key))


def _selected_id(selected: Mapping[str, Any], key: str) -> str | None:
    return _selected_ref(selected, key).get("result_id")


def _selected_path(selected: Mapping[str, Any], key: str) -> str | None:
    return _selected_ref(selected, key).get("result_path")


def _selected_outcome(selected: Mapping[str, Any], key: str) -> str | None:
    return _selected_ref(selected, key).get("outcome")


def _v7_quality_score(result: Mapping[str, Any]) -> int:
    if result.get("outcome") != SELF_ORIENTED:
        return -1
    summary = _as_mapping(result.get("current_self_orientation_summary"))
    required = (
        "current_body_conformance_recognized",
        "post_conformance_closure_recognized",
        "cross_surface_correspondence_recognized",
        "cross_carrier_receipt_recognized",
        "carrier_b_returned_receipt_evidence_recognized",
        "carrier_b_refusal_evidence_remains_visible",
        "receipt_alignment_correspondence_recognized",
        "refusal_visible_correspondence_recognized",
        "correspondence_checks_passed",
    )
    score = 0
    for key in required:
        if summary.get(key) is True:
            score += 1
    if summary.get("failed_check_count") == 0:
        score += 1
    return score


def _select_v7(
    current_self_orientation_v7_result: Mapping[str, Any] | None,
    current_self_orientation_v7_result_path: Path | str | None,
) -> tuple[Path | None, dict[str, Any] | None, str]:
    if current_self_orientation_v7_result_path is not None:
        path = _repo_path(current_self_orientation_v7_result_path)
        return (
            path,
            _read_json_mapping(path),
            "explicit_current_self_orientation_v7_result_path",
        )
    if current_self_orientation_v7_result is not None:
        if not isinstance(current_self_orientation_v7_result, Mapping):
            raise CurrentBodyConformancePassV2Error(
                "current self-orientation v7 input must be a mapping",
                "CURRENT_SELF_ORIENTATION_V7_MALFORMED",
            )
        return (
            None,
            copy.deepcopy(dict(current_self_orientation_v7_result)),
            "mapping_supplied_current_self_orientation_v7",
        )
    candidates = [
        (path, result)
        for path, result in _iter_json_artifacts(CURRENT_SELF_ORIENTATION_V7_ROOT)
        if result.get("outcome") == SELF_ORIENTED
        and _v7_quality_score(result) >= 9
    ]
    if not candidates:
        return None, None, "successful_current_self_orientation_v7_discovery"
    path, result = max(
        candidates,
        key=lambda item: (
            _v7_quality_score(item[1]),
            item[0].stat().st_mtime if item[0].exists() else 0.0,
            item[0].as_posix(),
        ),
    )
    return path, copy.deepcopy(result), "successful_current_self_orientation_v7_discovery"


def _merge_non_claims(v7_result: Mapping[str, Any] | None) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    if isinstance(v7_result, Mapping):
        source = _as_mapping(v7_result.get("non_claims"))
        for key, value in source.items():
            if isinstance(value, bool):
                non_claims[key] = value
    non_claims["v2_conformance_created_permission"] = False
    non_claims["v2_conformance_created_authority"] = False
    non_claims["v2_conformance_created_currentness"] = False
    non_claims["v2_conformance_authorized_continuation"] = False
    return non_claims


def _non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _has_selected_id(selected: Mapping[str, Any], key: str) -> bool:
    return bool(_selected_id(selected, key))


def _summary_bool(summary: Mapping[str, Any], key: str) -> bool:
    return summary.get(key) is True


def _v7_failed_check_count(v7_result: Mapping[str, Any] | None) -> int | None:
    if not isinstance(v7_result, Mapping):
        return None
    summary = _as_mapping(v7_result.get("current_self_orientation_summary"))
    if isinstance(summary.get("failed_check_count"), int):
        return summary["failed_check_count"]
    checks = _mapping_list(v7_result.get("bounded_correspondence_checks"))
    return sum(1 for check in checks if check.get("passed") is not True)


def _build_selected_inputs(
    v7_result: Mapping[str, Any] | None,
    v7_path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    selected = _as_mapping(v7_result.get("selected_orientation_inputs")) if v7_result else {}
    return {
        "selected_current_self_orientation_v7_result": {
            "result_id": _result_id(v7_result),
            "result_path": _display_path(v7_path),
            "outcome": v7_result.get("outcome") if isinstance(v7_result, Mapping) else None,
            "selection_mode": selection_mode,
        },
        "selected_current_self_orientation_v6_result": _selected_ref(
            selected,
            "selected_current_self_orientation_v6_result",
        ),
        "selected_previous_current_body_conformance_result": _selected_ref(
            selected,
            "selected_current_body_conformance_result",
        ),
        "selected_post_conformance_closure_result": _selected_ref(
            selected,
            "selected_post_conformance_closure_result",
        ),
        "selected_closure_alignment_correspondence_result": _selected_ref(
            selected,
            "selected_closure_alignment_correspondence_result",
        ),
        "selected_local_cross_carrier_receipt_result": _selected_ref(
            selected,
            "selected_local_cross_carrier_receipt_result",
        ),
        "selected_returned_carrier_b_blocked_receipt_result": _selected_ref(
            selected,
            "selected_returned_carrier_b_blocked_receipt_result",
        ),
        "selected_returned_carrier_b_successful_receipt_result": _selected_ref(
            selected,
            "selected_returned_carrier_b_successful_receipt_result",
        ),
        "selected_receipt_alignment_correspondence_result": _selected_ref(
            selected,
            "selected_receipt_alignment_correspondence_result",
        ),
        "selected_refusal_visible_correspondence_result": _selected_ref(
            selected,
            "selected_refusal_visible_correspondence_result",
        ),
    }


def _recognized_integrated_body_posture(
    v7_result: Mapping[str, Any] | None,
    selected_inputs: Mapping[str, Any],
) -> dict[str, Any]:
    summary = _as_mapping(v7_result.get("current_self_orientation_summary")) if v7_result else {}
    basis = _as_mapping(v7_result.get("self_orientation_basis")) if v7_result else {}
    return {
        "posture_kind": "current_self_orientation_v7_integrated_body_posture",
        "v7_body_posture_coherent_as_current_body_mirror": summary.get("failed_check_count") == 0,
        "current_governing_basis_remains_upstream": summary.get("current_governing_basis_recognized") is True
        and basis.get("current_governing_basis_remains_inherited_from_v6_upstream_surfaces") is True,
        "reentry_body_signal_derivative_vessel_and_operator_surfaces_remain_downstream": bool(
            summary.get("reentry_surfaces_recognized")
            and summary.get("body_signal_surfaces_recognized")
            and summary.get("derivative_vessel_relation_boundary_recognized")
        ),
        "conformance_closure_correspondence_and_receipt_surfaces_remain_downstream": bool(
            basis.get("conformance_surfaces_remain_downstream_audit_only")
            and basis.get("closure_surfaces_remain_downstream_meaning_closure_only")
            and basis.get("correspondence_surfaces_remain_bounded_reading_relation_only")
            and basis.get("receipt_surfaces_remain_carried_evidence_only")
        ),
        "carrier_b_remains_receiving_carrier_evidence_only": summary.get(
            "carrier_b_remained_receiving_carrier_only"
        )
        is True,
        "visible_refusal_evidence_preserved": summary.get("carrier_b_refusal_evidence_remains_visible")
        is True,
        "successful_returned_receipt_evidence_preserved": summary.get(
            "carrier_b_returned_receipt_evidence_recognized"
        )
        is True,
        "returned_evidence_did_not_replace_source": not _as_mapping(
            v7_result.get("non_claims") if v7_result else {}
        ).get("returned_evidence_replaced_source"),
        "returned_evidence_did_not_create_currentness": not _as_mapping(
            v7_result.get("non_claims") if v7_result else {}
        ).get("returned_evidence_created_currentness"),
        "selected_input_ids": {
            key: _as_mapping(value).get("result_id")
            for key, value in selected_inputs.items()
            if isinstance(value, Mapping)
        },
    }


def _build_checks(
    *,
    v7_result: Mapping[str, Any] | None,
    selected_inputs: Mapping[str, Any],
    non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    summary = _as_mapping(v7_result.get("current_self_orientation_summary")) if v7_result else {}
    basis = _as_mapping(v7_result.get("self_orientation_basis")) if v7_result else {}
    checks = [
        _check(
            "current_self_orientation_v7_exists",
            isinstance(v7_result, Mapping),
            expected="one current self-orientation v7 result",
            actual=bool(v7_result),
            block_code="CURRENT_SELF_ORIENTATION_V7_MISSING",
        ),
        _check(
            "current_self_orientation_v7_is_self_oriented",
            (v7_result or {}).get("outcome") == SELF_ORIENTED,
            expected=SELF_ORIENTED,
            actual=(v7_result or {}).get("outcome") if isinstance(v7_result, Mapping) else None,
            block_code=(
                "CURRENT_SELF_ORIENTATION_V7_NOT_SELF_ORIENTED"
                if isinstance(v7_result, Mapping)
                else "CURRENT_SELF_ORIENTATION_V7_MISSING"
            ),
        ),
        _check(
            "current_self_orientation_v7_failed_checks_absent",
            _v7_failed_check_count(v7_result) == 0,
            expected=0,
            actual=_v7_failed_check_count(v7_result),
            block_code="CURRENT_SELF_ORIENTATION_V7_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "current_governing_basis_recognized",
            _summary_bool(summary, "current_governing_basis_recognized")
            and basis.get("current_governing_basis_remains_inherited_from_v6_upstream_surfaces") is True,
            expected="current/governing basis inherited from v6 upstream surfaces",
            actual={
                "summary_flag": summary.get("current_governing_basis_recognized"),
                "basis_flag": basis.get(
                    "current_governing_basis_remains_inherited_from_v6_upstream_surfaces"
                ),
            },
            block_code="CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
        ),
        _check(
            "v7_preserves_v6_basis",
            _has_selected_id(selected_inputs, "selected_current_self_orientation_v6_result"),
            expected="selected v6 basis id present",
            actual=_selected_ref(selected_inputs, "selected_current_self_orientation_v6_result"),
            block_code="CURRENT_SELF_ORIENTATION_V6_BASIS_MISSING",
        ),
        _check(
            "current_body_conformance_recognized",
            _summary_bool(summary, "current_body_conformance_recognized")
            and _has_selected_id(
                selected_inputs,
                "selected_previous_current_body_conformance_result",
            ),
            expected=True,
            actual=summary.get("current_body_conformance_recognized"),
            block_code="CURRENT_BODY_CONFORMANCE_NOT_RECOGNIZED",
        ),
        _check(
            "post_conformance_closure_recognized",
            _summary_bool(summary, "post_conformance_closure_recognized")
            and _has_selected_id(selected_inputs, "selected_post_conformance_closure_result"),
            expected=True,
            actual=summary.get("post_conformance_closure_recognized"),
            block_code="POST_CONFORMANCE_CLOSURE_NOT_RECOGNIZED",
        ),
        _check(
            "cross_surface_correspondence_recognized",
            _summary_bool(summary, "cross_surface_correspondence_recognized"),
            expected=True,
            actual=summary.get("cross_surface_correspondence_recognized"),
            block_code="CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED",
        ),
        _check(
            "cross_carrier_receipt_recognized",
            _summary_bool(summary, "cross_carrier_receipt_recognized")
            and _has_selected_id(selected_inputs, "selected_local_cross_carrier_receipt_result"),
            expected=True,
            actual=summary.get("cross_carrier_receipt_recognized"),
            block_code="CROSS_CARRIER_RECEIPT_NOT_RECOGNIZED",
        ),
        _check(
            "returned_carrier_b_receipt_evidence_recognized",
            _summary_bool(summary, "carrier_b_returned_receipt_evidence_recognized")
            and _has_selected_id(
                selected_inputs,
                "selected_returned_carrier_b_successful_receipt_result",
            ),
            expected=True,
            actual=summary.get("carrier_b_returned_receipt_evidence_recognized"),
            block_code="RETURNED_CARRIER_B_RECEIPT_EVIDENCE_NOT_RECOGNIZED",
        ),
        _check(
            "returned_carrier_b_refusal_evidence_remains_visible",
            _summary_bool(summary, "carrier_b_refusal_evidence_remains_visible")
            and _has_selected_id(
                selected_inputs,
                "selected_returned_carrier_b_blocked_receipt_result",
            ),
            expected=True,
            actual=summary.get("carrier_b_refusal_evidence_remains_visible"),
            block_code="RETURNED_CARRIER_B_REFUSAL_EVIDENCE_NOT_VISIBLE",
        ),
        _check(
            "receipt_alignment_correspondence_recognized",
            _summary_bool(summary, "receipt_alignment_correspondence_recognized")
            and _has_selected_id(
                selected_inputs,
                "selected_receipt_alignment_correspondence_result",
            ),
            expected=True,
            actual=summary.get("receipt_alignment_correspondence_recognized"),
            block_code="RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED",
        ),
        _check(
            "refusal_visible_correspondence_recognized",
            _summary_bool(summary, "refusal_visible_correspondence_recognized")
            and _has_selected_id(
                selected_inputs,
                "selected_refusal_visible_correspondence_result",
            ),
            expected=True,
            actual=summary.get("refusal_visible_correspondence_recognized"),
            block_code="REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED",
        ),
        _check(
            "conformance_stayed_downstream",
            basis.get("conformance_surfaces_remain_downstream_audit_only") is True,
            expected=True,
            actual=basis.get("conformance_surfaces_remain_downstream_audit_only"),
            block_code="CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION",
        ),
        _check(
            "closure_stayed_downstream",
            basis.get("closure_surfaces_remain_downstream_meaning_closure_only") is True,
            expected=True,
            actual=basis.get("closure_surfaces_remain_downstream_meaning_closure_only"),
            block_code="CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION",
        ),
        _check(
            "correspondence_stayed_downstream",
            basis.get("correspondence_surfaces_remain_bounded_reading_relation_only") is True,
            expected=True,
            actual=basis.get("correspondence_surfaces_remain_bounded_reading_relation_only"),
            block_code="CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION",
        ),
        _check(
            "receipt_stayed_downstream",
            basis.get("receipt_surfaces_remain_carried_evidence_only") is True,
            expected=True,
            actual=basis.get("receipt_surfaces_remain_carried_evidence_only"),
            block_code="RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR",
        ),
        _check(
            "carrier_b_stayed_receiving_carrier_only",
            _summary_bool(summary, "carrier_b_remained_receiving_carrier_only")
            and basis.get("carrier_b_remains_receiving_carrier_only") is True,
            expected=True,
            actual={
                "summary_flag": summary.get("carrier_b_remained_receiving_carrier_only"),
                "basis_flag": basis.get("carrier_b_remains_receiving_carrier_only"),
            },
            block_code="CARRIER_B_RECEIVING_ONLY_POSTURE_FAILED",
        ),
        _check(
            "source_currentness_authority_permission_successor_body_collapse_stayed_false",
            _summary_bool(
                summary,
                "source_currentness_authority_permission_successor_body_collapse_stayed_false",
            ),
            expected=True,
            actual=summary.get(
                "source_currentness_authority_permission_successor_body_collapse_stayed_false"
            ),
            block_code="SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_SUCCESSOR_BODY_COLLAPSE",
        ),
        _check(
            "conformance_did_not_become_authority_permission_or_currentness",
            non_claims.get("conformance_became_authority") is False
            and non_claims.get("conformance_became_permission") is False
            and non_claims.get("conformance_became_currentness") is False,
            expected=False,
            actual={
                "conformance_became_authority": non_claims.get("conformance_became_authority"),
                "conformance_became_permission": non_claims.get("conformance_became_permission"),
                "conformance_became_currentness": non_claims.get("conformance_became_currentness"),
            },
            block_code="CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION",
        ),
        _check(
            "closure_did_not_become_authority_permission_signal_or_continuation",
            non_claims.get("closure_became_authority") is False
            and non_claims.get("closure_became_permission") is False
            and non_claims.get("closure_became_signal") is False
            and non_claims.get("closure_authorized_next_work", False) is False,
            expected=False,
            actual={
                "closure_became_authority": non_claims.get("closure_became_authority"),
                "closure_became_permission": non_claims.get("closure_became_permission"),
                "closure_became_signal": non_claims.get("closure_became_signal"),
                "closure_authorized_next_work": non_claims.get("closure_authorized_next_work"),
            },
            block_code="CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION",
        ),
        _check(
            "correspondence_did_not_become_authority_currentness_permission_signal_or_action",
            non_claims.get("correspondence_became_authority") is False
            and non_claims.get("correspondence_became_currentness") is False
            and non_claims.get("correspondence_became_permission") is False
            and non_claims.get("correspondence_became_signal") is False
            and non_claims.get("correspondence_became_presence", False) is False
            and non_claims.get("correspondence_became_threshold", False) is False
            and non_claims.get("correspondence_became_truth", False) is False
            and non_claims.get("correspondence_became_action", False) is False
            and non_claims.get("correspondence_became_consequence", False) is False,
            expected=False,
            actual={
                key: non_claims.get(key)
                for key in (
                    "correspondence_became_authority",
                    "correspondence_became_currentness",
                    "correspondence_became_permission",
                    "correspondence_became_signal",
                    "correspondence_became_presence",
                    "correspondence_became_threshold",
                    "correspondence_became_truth",
                    "correspondence_became_action",
                    "correspondence_became_consequence",
                )
            },
            block_code="CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION",
        ),
        _check(
            "receipt_did_not_become_source_currentness_authority_permission_successor_or_body",
            non_claims.get("receipt_became_source", False) is False
            and non_claims.get("receipt_became_currentness", False) is False
            and non_claims.get("receipt_became_authority", False) is False
            and non_claims.get("receipt_became_permission", False) is False
            and non_claims.get("receiving_carrier_became_successor") is False
            and non_claims.get("receiving_carrier_became_body") is False
            and non_claims.get("carried_surface_became_source") is False
            and non_claims.get("carried_surface_became_currentness") is False,
            expected=False,
            actual={
                key: non_claims.get(key)
                for key in (
                    "receipt_became_source",
                    "receipt_became_currentness",
                    "receipt_became_authority",
                    "receipt_became_permission",
                    "receiving_carrier_became_successor",
                    "receiving_carrier_became_body",
                    "carried_surface_became_source",
                    "carried_surface_became_currentness",
                )
            },
            block_code="RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR",
        ),
        _check(
            "receipt_did_not_become_signal_presence_threshold_truth_action_or_consequence",
            non_claims.get("carried_surface_became_signal_by_default") is False
            and non_claims.get("signal_created_by_default") is False
            and non_claims.get("presence_established") is False
            and non_claims.get("threshold_met") is False
            and non_claims.get("truth_created") is False
            and non_claims.get("action_authorized") is False
            and non_claims.get("consequence_created") is False,
            expected=False,
            actual={
                key: non_claims.get(key)
                for key in (
                    "carried_surface_became_signal_by_default",
                    "signal_created_by_default",
                    "presence_established",
                    "threshold_met",
                    "truth_created",
                    "action_authorized",
                    "consequence_created",
                )
            },
            block_code="RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE",
        ),
        _check(
            "multi_carrier_law_not_created",
            _summary_bool(summary, "multi_carrier_law_stayed_false")
            and non_claims.get("multi_carrier_law_created") is False,
            expected=False,
            actual={
                "summary_flag": summary.get("multi_carrier_law_stayed_false"),
                "multi_carrier_law_created": non_claims.get("multi_carrier_law_created"),
            },
            block_code="MULTI_CARRIER_LAW_CREATED",
        ),
        _check(
            "distributed_standing_not_created",
            _summary_bool(summary, "distributed_standing_stayed_false")
            and non_claims.get("distributed_standing_created") is False,
            expected=False,
            actual={
                "summary_flag": summary.get("distributed_standing_stayed_false"),
                "distributed_standing_created": non_claims.get("distributed_standing_created"),
            },
            block_code="DISTRIBUTED_STANDING_CREATED",
        ),
        _check(
            "latest_file_currentness_false",
            non_claims.get("latest_file_currentness") is False,
            expected=False,
            actual=non_claims.get("latest_file_currentness"),
            block_code="LATEST_FILE_CURRENTNESS_REFUSED",
        ),
        _check(
            "recency_fraud_false",
            non_claims.get("recency_fraud") is False,
            expected=False,
            actual=non_claims.get("recency_fraud"),
            block_code="LATEST_FILE_CURRENTNESS_REFUSED",
        ),
        _check(
            "mutation_replay_merge_false",
            non_claims.get("mutation_performed") is False
            and non_claims.get("replay_performed") is False
            and non_claims.get("merge_performed") is False,
            expected=False,
            actual={
                "mutation_performed": non_claims.get("mutation_performed"),
                "replay_performed": non_claims.get("replay_performed"),
                "merge_performed": non_claims.get("merge_performed"),
            },
            block_code="MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "follow_on_work_not_authorized",
            non_claims.get("follow_on_steps_authorized") is False
            and non_claims.get("follow_on_work_authorized") is False
            and non_claims.get("v2_conformance_authorized_continuation") is False,
            expected=False,
            actual={
                "follow_on_steps_authorized": non_claims.get("follow_on_steps_authorized"),
                "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
                "v2_conformance_authorized_continuation": non_claims.get(
                    "v2_conformance_authorized_continuation"
                ),
            },
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "self_orientation_successor_not_forced",
            non_claims.get("self_orientation_successor_forced", False) is False,
            expected=False,
            actual=non_claims.get("self_orientation_successor_forced"),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "conformance_successor_not_forced_beyond_this_declared_pass",
            non_claims.get("conformance_successor_forced", False) is False,
            expected=False,
            actual=non_claims.get("conformance_successor_forced"),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "required_non_claims_remain_false",
            _non_claims_false(non_claims),
            expected="all required non-claims false",
            actual={
                key: non_claims.get(key)
                for key in REQUIRED_FALSE_NON_CLAIMS
                if non_claims.get(key) is not False
            },
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _metadata(selected_inputs: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    selected_v7 = _as_mapping(selected_inputs.get("selected_current_self_orientation_v7_result"))
    base = _safe_filename_part(selected_v7.get("result_id") or "current_self_orientation_v7")
    suffix = "body_conformant" if outcome == BODY_CONFORMANT else "blocked"
    return {
        "current_body_conformance_pass_v2_result_id": f"{base}__current_body_conformance_pass_v2_{suffix}",
        "current_body_conformance_pass_v2_result_type": RESULT_TYPE,
        "current_body_conformance_pass_v2_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RUNNER_MODULE,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _conformance_statement(
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    posture: Mapping[str, Any],
) -> dict[str, Any]:
    conformant = outcome == BODY_CONFORMANT and _first_failed(checks) is None
    return {
        "v7_body_posture_conformant": conformant,
        "current_governing_basis_remains_upstream": conformant
        and posture.get("current_governing_basis_remains_upstream") is True,
        "downstream_surfaces_remain_downstream": conformant
        and posture.get(
            "conformance_closure_correspondence_and_receipt_surfaces_remain_downstream"
        )
        is True,
        "carrier_b_remained_receiving_carrier_only": conformant
        and posture.get("carrier_b_remains_receiving_carrier_evidence_only") is True,
        "returned_receipt_evidence_preserved": conformant
        and posture.get("successful_returned_receipt_evidence_preserved") is True,
        "refusal_evidence_preserved": conformant
        and posture.get("visible_refusal_evidence_preserved") is True,
        "no_authority_created": conformant,
        "no_permission_created": conformant,
        "no_currentness_created": conformant,
        "no_source_replaced": conformant,
        "no_multi_carrier_law_created": conformant,
        "no_distributed_standing_created": conformant,
        "no_presence_threshold_truth_action_consequence_created": conformant,
        "no_continuation_authorized": conformant,
    }


def _build_result(
    *,
    selected_inputs: Mapping[str, Any],
    v7_result: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    posture = _recognized_integrated_body_posture(v7_result, selected_inputs)
    result = {
        "current_body_conformance_pass_v2_metadata": _metadata(selected_inputs, outcome),
        "selected_conformance_inputs": copy.deepcopy(dict(selected_inputs)),
        "v7_orientation_basis": {
            "selected_v7_result_id": _selected_id(
                selected_inputs,
                "selected_current_self_orientation_v7_result",
            ),
            "selected_v7_result_path": _selected_path(
                selected_inputs,
                "selected_current_self_orientation_v7_result",
            ),
            "selected_v7_outcome": _selected_outcome(
                selected_inputs,
                "selected_current_self_orientation_v7_result",
            ),
            "selected_v6_result_id": _selected_id(
                selected_inputs,
                "selected_current_self_orientation_v6_result",
            ),
            "v7_basis_posture": _as_mapping(v7_result.get("self_orientation_basis")) if v7_result else {},
            "v7_summary": _as_mapping(v7_result.get("current_self_orientation_summary")) if v7_result else {},
            "v7_is_conformance_input_not_authority": True,
        },
        "recognized_integrated_body_posture": posture,
        "conformance_checks": [copy.deepcopy(dict(check)) for check in checks],
        "conformance_statement": _conformance_statement(outcome, checks, posture),
        "conformance_non_meaning": dict(NON_MEANING),
        "what_remains_open": copy.deepcopy(OPEN_SURFACES),
        "non_claims": dict(non_claims),
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "current_body_conformance_pass_v2_summary": {},
    }
    result["current_body_conformance_pass_v2_summary"] = (
        build_current_body_conformance_pass_v2_summary(result)
    )
    return result


def _empty_selected_inputs() -> dict[str, Any]:
    return {
        "selected_current_self_orientation_v7_result": {},
        "selected_current_self_orientation_v6_result": {},
        "selected_previous_current_body_conformance_result": {},
        "selected_post_conformance_closure_result": {},
        "selected_closure_alignment_correspondence_result": {},
        "selected_local_cross_carrier_receipt_result": {},
        "selected_returned_carrier_b_blocked_receipt_result": {},
        "selected_returned_carrier_b_successful_receipt_result": {},
        "selected_receipt_alignment_correspondence_result": {},
        "selected_refusal_visible_correspondence_result": {},
    }


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    v7_result: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _build_result(
        selected_inputs=selected_inputs or _empty_selected_inputs(),
        v7_result=v7_result,
        checks=checks or [],
        outcome=BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        non_claims=non_claims or {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    )


def _run(
    current_self_orientation_v7_result: Mapping[str, Any] | None = None,
    current_self_orientation_v7_result_path: Path | str | None = None,
) -> dict[str, Any]:
    v7_path, selected_v7, selection_mode = _select_v7(
        current_self_orientation_v7_result,
        current_self_orientation_v7_result_path,
    )
    selected_inputs = _build_selected_inputs(selected_v7, v7_path, selection_mode)
    if selected_v7 is None:
        checks = [
            _check(
                "current_self_orientation_v7_exists",
                False,
                expected="one current self-orientation v7 result",
                actual=False,
                block_code="CURRENT_SELF_ORIENTATION_V7_MISSING",
            )
        ]
        return _blocked_result(
            block_code="CURRENT_SELF_ORIENTATION_V7_MISSING",
            selected_inputs=selected_inputs,
            checks=checks,
        )

    non_claims = _merge_non_claims(selected_v7)
    checks = _build_checks(
        v7_result=selected_v7,
        selected_inputs=selected_inputs,
        non_claims=non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _build_result(
            selected_inputs=selected_inputs,
            v7_result=selected_v7,
            checks=checks,
            outcome=BLOCKED,
            block_code=str(failed.get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED"),
            block_detail=f"failed check: {failed.get('check_name')}",
            non_claims=non_claims,
        )
    return _build_result(
        selected_inputs=selected_inputs,
        v7_result=selected_v7,
        checks=checks,
        outcome=BODY_CONFORMANT,
        block_code=None,
        block_detail=None,
        non_claims=non_claims,
    )


def run_current_body_conformance_pass_v2(
    current_self_orientation_v7_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run one bounded v2 current-body conformance pass over v7 posture."""

    try:
        return _run(current_self_orientation_v7_result=current_self_orientation_v7_result)
    except CurrentBodyConformancePassV2Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs,
            checks=exc.checks,
        )


def run_current_body_conformance_pass_v2_from_path(
    current_self_orientation_v7_result_path: Path | str,
) -> dict[str, Any]:
    """Run one bounded v2 conformance pass from a v7 artifact path."""

    selected_inputs = {
        "selected_current_self_orientation_v7_result": {
            "result_path": _display_path(current_self_orientation_v7_result_path),
            "selection_mode": "explicit_current_self_orientation_v7_result_path",
        }
    }
    try:
        return _run(current_self_orientation_v7_result_path=current_self_orientation_v7_result_path)
    except CurrentBodyConformancePassV2Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs or selected_inputs,
            checks=exc.checks,
        )


def build_current_body_conformance_pass_v2_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact summary for one v2 conformance pass result."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformancePassV2Error(
            "current-body conformance pass v2 result must be an object",
            "CURRENT_SELF_ORIENTATION_V7_MALFORMED",
        )
    selected = _as_mapping(result.get("selected_conformance_inputs"))
    block = _as_mapping(result.get("block"))
    checks = _mapping_list(result.get("conformance_checks"))
    statement = _as_mapping(result.get("conformance_statement"))
    non_claims = _as_mapping(result.get("non_claims"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_v7_id": _selected_id(
            selected,
            "selected_current_self_orientation_v7_result",
        ),
        "selected_v7_path": _selected_path(
            selected,
            "selected_current_self_orientation_v7_result",
        ),
        "selected_v7_outcome": _selected_outcome(
            selected,
            "selected_current_self_orientation_v7_result",
        ),
        "selected_v6_id": _selected_id(
            selected,
            "selected_current_self_orientation_v6_result",
        ),
        "selected_previous_conformance_id": _selected_id(
            selected,
            "selected_previous_current_body_conformance_result",
        ),
        "selected_post_conformance_closure_id": _selected_id(
            selected,
            "selected_post_conformance_closure_result",
        ),
        "selected_closure_alignment_correspondence_id": _selected_id(
            selected,
            "selected_closure_alignment_correspondence_result",
        ),
        "selected_local_receipt_id": _selected_id(
            selected,
            "selected_local_cross_carrier_receipt_result",
        ),
        "selected_returned_carrier_b_blocked_receipt_id": _selected_id(
            selected,
            "selected_returned_carrier_b_blocked_receipt_result",
        ),
        "selected_returned_carrier_b_successful_receipt_id": _selected_id(
            selected,
            "selected_returned_carrier_b_successful_receipt_result",
        ),
        "selected_receipt_alignment_correspondence_id": _selected_id(
            selected,
            "selected_receipt_alignment_correspondence_result",
        ),
        "selected_refusal_visible_correspondence_id": _selected_id(
            selected,
            "selected_refusal_visible_correspondence_result",
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "v7_body_posture_conformant": statement.get("v7_body_posture_conformant"),
        "current_governing_basis_upstream": statement.get(
            "current_governing_basis_remains_upstream"
        ),
        "downstream_surfaces_downstream": statement.get(
            "downstream_surfaces_remain_downstream"
        ),
        "carrier_b_receiving_only": statement.get("carrier_b_remained_receiving_carrier_only"),
        "returned_evidence_preserved": statement.get("returned_receipt_evidence_preserved"),
        "refusal_evidence_preserved": statement.get("refusal_evidence_preserved"),
        "no_authority_permission_currentness_source_replacement": bool(
            statement.get("no_authority_created")
            and statement.get("no_permission_created")
            and statement.get("no_currentness_created")
            and statement.get("no_source_replaced")
        ),
        "no_multi_carrier_law_or_distributed_standing": bool(
            statement.get("no_multi_carrier_law_created")
            and statement.get("no_distributed_standing_created")
        ),
        "no_presence_threshold_truth_action_consequence": statement.get(
            "no_presence_threshold_truth_action_consequence_created"
        ),
        "no_continuation": statement.get("no_continuation_authorized"),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if key in non_claims
        },
    }


def _safe_default_output_path(result: Mapping[str, Any]) -> Path:
    selected = _as_mapping(result.get("selected_conformance_inputs"))
    v7 = _selected_ref(selected, "selected_current_self_orientation_v7_result")
    stem = _safe_filename_part(v7.get("result_id") or "current_self_orientation_v7")
    candidate = CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT
            / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentBodyConformancePassV2Error(
        "no bounded current-body conformance pass v2 filename is available",
        "CURRENT_SELF_ORIENTATION_V7_MALFORMED",
    )


def write_current_body_conformance_pass_v2_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v2 conformance-pass JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformancePassV2Error(
            "current-body conformance pass v2 result must be an object",
            "CURRENT_SELF_ORIENTATION_V7_MALFORMED",
        )
    target = _repo_path(output_path) if output_path is not None else _safe_default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current-body conformance pass v2 result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(dict(result), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def _walk_items(value: Any) -> Iterable[tuple[str, Any]]:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            yield str(key), nested_value
            yield from _walk_items(nested_value)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_items(item)
