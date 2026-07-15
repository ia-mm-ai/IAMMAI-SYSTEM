"""Bounded current self-orientation v9 resolver.

This resolver records the body's current orientation after distributed standing
boundary conformance closure. It preserves what now stands, what does not
stand, what is closed in meaning, and what remains open. It does not mutate v8
or any prior artifact, authorize continuation, authorize operation, synchronize
repositories, transfer the body, create a second body, create carrier
currentness, select carriers, create authority or permission, create truth or
action, claim final completion, create public launch readiness, or schedule
follow-on work.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentSelfOrientationV9Error(Exception):
    """Hard failure for malformed or unreadable explicit v9 orientation inputs."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REPO_ROOT = Path(__file__).resolve().parents[1]
CURRENT_SELF_ORIENTATION_V9_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v9"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v9"
RESULT_TYPE = "current_self_orientation_v9_result"
RESULT_VERSION = "0.1.0"

OUTCOME_RECORDED = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
OUTCOME_NOT_RECORDED = "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"
OUTCOME_BLOCKED = "CURRENT_SELF_ORIENTATION_V9_BLOCKED"

SUPPORTED_OUTCOMES = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_CURRENT_SELF_ORIENTATION_V9"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_CURRENT_SELF_ORIENTATION_V9"
INTENT_BLOCK = "BLOCK_CURRENT_SELF_ORIENTATION_V9"

SUPPORTED_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

EXPECTED_CLOSURE_OUTCOME = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED"
EXPECTED_PRIOR_OUTCOME = "SELF_ORIENTED"
EXPECTED_CLOSURE_FAILED_CHECK_COUNT = 0

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "carrier_currentness_created": False,
    "source_replaced": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "divergence_resolved": False,
    "truth_created": False,
    "action_authorized": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "final_governance_completed": False,
    "final_continuity_completed": False,
    "final_system_identity_completed": False,
    "public_launch_readiness_created": False,
    "follow_on_work_authorized": False,
    "self_orientation_successor_scheduled": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

ORIENTATION_NON_MEANING = {
    "permission": True,
    "continuation": True,
    "operation": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body": True,
    "distributed_operation": True,
    "implementation": True,
    "final_completion": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "final_system_identity": True,
    "public_launch_readiness": True,
    "carrier_currentness": True,
    "current_carrier_selected": True,
    "winning_carrier_selected": True,
    "losing_carrier_invalidated": True,
    "source_replacement": True,
    "authority": True,
    "truth": True,
    "action": True,
    "divergence_resolution": True,
    "evidence_erasure": True,
    "prior_result_mutation": True,
    "follow_on_work_authorization": True,
    "self_orientation_successor_beyond_v9": True,
    "does_not_mean_permission": True,
    "does_not_mean_continuation": True,
    "does_not_mean_operation": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_final_completion": True,
    "does_not_mean_public_launch_readiness": True,
    "does_not_mean_follow_on_work_authorization": True,
}

CANONICAL_WHAT_STANDS = {
    "current_self_orientation_v8_remains_lineage": (
        "current self-orientation v8 remains lineage",
        "v8 remains lineage",
    ),
    "current_body_conformance_v3_closure_remains_basis": (
        "current-body conformance v3 closure remains basis",
        "current body conformance v3 closure remains basis",
    ),
    "carrier_b_successful_receipt_evidence_stands_as_evidence": (
        "carrier b successful receipt evidence stands as evidence",
        "carrier b successful physical receipt evidence",
    ),
    "carrier_c_blocked_receipt_evidence_stands_as_evidence": (
        "carrier c blocked receipt evidence stands as evidence",
        "carrier c blocked physical receipt evidence",
    ),
    "b_c_visible_divergence_stands": (
        "b/c visible divergence stands",
        "b c visible divergence stands",
    ),
    "carrier_c_lifecycle_posture_stands": (
        "carrier c lifecycle posture stands",
    ),
    "registry_persistence_v2_stands_as_reference_posture": (
        "registry/persistence v2 stands as reference posture",
        "carrier registry/persistence v2 stands as reference posture",
    ),
    "standing_propagation_v2_stands_as_evidence_reference_posture": (
        "standing propagation v2 stands as evidence/reference posture",
        "standing propagation v2 stands as evidence reference posture",
    ),
    "continuity_turn_v2_stands_as_lineage_projection_posture": (
        "continuity-turn v2 stands as lineage/projection posture",
        "carrier continuity-turn v2 stands as lineage projection posture",
    ),
    "cross_carrier_currentness_successor_stands_as_body_side_accounting_posture": (
        "cross-carrier currentness successor stands as body-side accounting posture",
        "currentness successor stands as body-side accounting posture",
    ),
    "cross_carrier_divergence_consequence_stands_as_caution_reliance_effect_posture": (
        "cross-carrier divergence consequence stands as caution/reliance-effect posture",
        "divergence consequence stands as caution reliance-effect posture",
    ),
    "distributed_standing_boundary_result_stands_as_bounded_body_side_posture_recording": (
        "distributed standing boundary result stands as bounded body-side posture recording",
    ),
    "distributed_standing_boundary_conformance_stands_as_conformance": (
        "distributed standing boundary conformance stands as conformance",
    ),
    "distributed_standing_boundary_conformance_closure_stands_as_closure_of_conformance_meaning": (
        "distributed standing boundary conformance closure stands as closure of conformance meaning",
    ),
}

CANONICAL_WHAT_DOES_NOT_STAND = {
    "distributed_operation_does_not_stand": ("distributed operation does not stand",),
    "repository_synchronization_does_not_stand": (
        "repository synchronization does not stand",
    ),
    "full_body_transfer_does_not_stand": ("full body transfer does not stand",),
    "second_body_does_not_stand": ("second body does not stand",),
    "continuation_does_not_stand": ("continuation does not stand",),
    "carrier_currentness_does_not_stand": ("carrier currentness does not stand",),
    "current_carrier_selection_does_not_stand": (
        "current carrier selection does not stand",
    ),
    "winning_carrier_selection_does_not_stand": (
        "winning carrier selection does not stand",
    ),
    "losing_carrier_invalidation_does_not_stand": (
        "losing carrier invalidation does not stand",
    ),
    "source_replacement_does_not_stand": ("source replacement does not stand",),
    "authority_creation_does_not_stand": ("authority creation does not stand",),
    "permission_creation_does_not_stand": ("permission creation does not stand",),
    "truth_action_does_not_stand": ("truth/action does not stand",),
    "final_governance_does_not_stand": ("final governance does not stand",),
    "final_continuity_completion_does_not_stand": (
        "final continuity completion does not stand",
    ),
    "final_system_identity_completion_does_not_stand": (
        "final system identity completion does not stand",
    ),
    "public_launch_readiness_does_not_stand": (
        "public launch/readiness does not stand",
        "public launch readiness does not stand",
    ),
    "self_orientation_successor_beyond_v9_does_not_stand": (
        "self-orientation successor beyond v9 does not stand",
    ),
}

CANONICAL_WHAT_IS_CLOSED = {
    "current_orientation_to_distributed_standing_boundary_conformance_closure_closed": (
        "the body's current orientation to distributed standing boundary conformance closure",
        "current orientation to distributed standing boundary conformance closure",
    ),
    "distributed_standing_boundary_conformance_closure_stands_as_closed_meaning": (
        "distributed standing boundary conformance closure now stands as closed meaning",
    ),
    "closure_non_meaning_does_not_authorize_operation_or_continuation_closed": (
        "closure does not authorize operation or continuation",
        "the non-meaning that closure does not authorize operation or continuation",
    ),
    "v8_is_prior_orientation_lineage_not_latest_orientation": (
        "v8 is now prior orientation lineage, not the latest orientation",
    ),
}

WHAT_REMAINS_OPEN = {
    "current_self_orientation_v9_implementation_refinement": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "any_future_self_orientation_successor_beyond_v9": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "distributed_standing_implementation": "open_not_scheduled_not_authorized_not_executed",
    "distributed_operation": "open_not_scheduled_not_authorized_not_executed",
    "repository_synchronization": "open_not_scheduled_not_authorized_not_executed",
    "full_body_transfer": "open_not_scheduled_not_authorized_not_executed",
    "second_body_creation": "open_not_scheduled_not_authorized_not_executed",
    "carrier_registry_implementation": "open_not_scheduled_not_authorized_not_executed",
    "persistence_implementation": "open_not_scheduled_not_authorized_not_executed",
    "standing_propagation_implementation_beyond_boundary_recording": (
        "open_not_scheduled_not_authorized_not_executed"
    ),
    "truth_law": "open_not_scheduled_not_authorized_not_executed",
    "action_consequence_law": "open_not_scheduled_not_authorized_not_executed",
    "presence_law": "open_not_scheduled_not_authorized_not_executed",
    "threshold_law": "open_not_scheduled_not_authorized_not_executed",
    "body_relevance_medium": "open_not_scheduled_not_authorized_not_executed",
    "signal_series_or_accumulation_logic": "open_not_scheduled_not_authorized_not_executed",
    "public_launch_readiness": "open_not_scheduled_not_authorized_not_executed",
    "open_means_not_scheduled": True,
    "open_means_not_authorized": True,
    "open_means_not_executed": True,
}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _to_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return REPO_ROOT / candidate


def _read_json_object(path: Path, unreadable_code: str, malformed_code: str) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CurrentSelfOrientationV9Error(
            f"Unable to read JSON object from {path}: {exc}",
            unreadable_code,
        ) from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationV9Error(
            f"Malformed JSON object at {path}: {exc}",
            malformed_code,
        ) from exc

    if not isinstance(parsed, Mapping):
        raise CurrentSelfOrientationV9Error(
            f"JSON content at {path} is not an object.",
            malformed_code,
        )

    return _deepcopy(dict(parsed))


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _first_present(*values: Any) -> Any:
    for value in values:
        if _is_present(value):
            return value
    return None


def _recursive_find(value: Any, keys: Sequence[str]) -> Any:
    if isinstance(value, Mapping):
        for key in keys:
            if key in value:
                return value[key]
        for child in value.values():
            found = _recursive_find(child, keys)
            if found is not None:
                return found
    elif isinstance(value, list):
        for child in value:
            found = _recursive_find(child, keys)
            if found is not None:
                return found
    return None


def _recursive_true(value: Any, keys: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        for key in keys:
            if value.get(key) is True:
                return True
        return any(_recursive_true(child, keys) for child in value.values())
    if isinstance(value, list):
        return any(_recursive_true(child, keys) for child in value)
    return False


def _normalize_text(value: Any) -> str:
    text = str(value).strip().lower()
    cleaned = []
    for character in text:
        cleaned.append(character if character.isalnum() else " ")
    return " ".join("".join(cleaned).split())


def _sequence_contains(raw: Any, aliases: Sequence[str]) -> bool:
    if isinstance(raw, Mapping) or isinstance(raw, (str, bytes, bytearray)):
        return False
    if not isinstance(raw, Sequence):
        return False
    normalized_items = {_normalize_text(item) for item in raw}
    normalized_aliases = {_normalize_text(alias) for alias in aliases}
    return bool(normalized_items & normalized_aliases)


def _declared_bool(raw: Any, key: str, aliases: Sequence[str]) -> bool:
    if isinstance(raw, Mapping):
        found = _recursive_find(raw, (key, *aliases))
        if isinstance(found, bool):
            return found
        if _is_present(found):
            return True
    return _sequence_contains(raw, (key, *aliases))


def _safe_filename_part(value: Any) -> str:
    text = str(value or "current_self_orientation_v9").strip()
    cleaned = []
    for character in text:
        if character.isalnum() or character in ("-", "_"):
            cleaned.append(character)
        else:
            cleaned.append("_")
    filename = "".join(cleaned).strip("_").lower()
    return filename or "current_self_orientation_v9"


def _non_overwriting_path(path: Path) -> Path:
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


def _path_value(request: Mapping[str, Any], path_key: str, object_key: str) -> str | None:
    explicit = request.get(path_key)
    if _is_present(explicit):
        return str(explicit)
    selected = request.get(object_key)
    if isinstance(selected, str) and selected.strip():
        return selected
    return None


def _load_selected_mapping(
    request: Mapping[str, Any],
    *,
    object_key: str,
    path_key: str,
    missing_code: str,
    unreadable_code: str,
    malformed_code: str,
) -> tuple[dict[str, Any], str | None, list[str]]:
    path_value = _path_value(request, path_key, object_key)
    if path_value:
        path = _to_path(path_value)
        try:
            return _read_json_object(path, unreadable_code, malformed_code), str(path), []
        except CurrentSelfOrientationV9Error as exc:
            return {}, str(path), [exc.block_code]

    selected = request.get(object_key)
    if isinstance(selected, Mapping):
        return _deepcopy(dict(selected)), None, []
    if selected is None:
        return {}, None, [missing_code]
    return {}, None, [malformed_code]


def _summary(mapping: Mapping[str, Any], *summary_keys: str) -> Mapping[str, Any]:
    for key in summary_keys:
        value = mapping.get(key)
        if isinstance(value, Mapping):
            return value
    return {}


def _extract_prior_id(prior: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    metadata = prior.get("current_self_orientation_metadata")
    summary = _summary(prior, "current_self_orientation_summary")
    return _first_present(
        request.get("selected_prior_self_orientation_id"),
        _recursive_find(metadata, ("current_self_orientation_result_id", "result_id"))
        if isinstance(metadata, Mapping)
        else None,
        _recursive_find(summary, ("current_self_orientation_result_id", "result_id"))
        if isinstance(summary, Mapping)
        else None,
        prior.get("current_self_orientation_result_id"),
        prior.get("orientation_result_id"),
        prior.get("result_id"),
    )


def _extract_prior_outcome(prior: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    summary = _summary(prior, "current_self_orientation_summary")
    return _first_present(
        request.get("selected_prior_self_orientation_outcome"),
        prior.get("outcome"),
        _recursive_find(summary, ("outcome",)) if summary else None,
    )


def _prior_is_v8_lineage(prior: Mapping[str, Any], outcome: str | None) -> bool:
    metadata = prior.get("current_self_orientation_metadata")
    resolver_module = (
        _recursive_find(metadata, ("resolver_module",)) if isinstance(metadata, Mapping) else None
    )
    version = (
        _recursive_find(metadata, ("current_self_orientation_result_version", "result_version"))
        if isinstance(metadata, Mapping)
        else None
    )
    return bool(prior) and (
        resolver_module == "resolve_current_self_orientation_v8"
        or version == "0.8.0"
        or outcome == EXPECTED_PRIOR_OUTCOME
    )


def _extract_closure_id(closure: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    metadata = closure.get("distributed_standing_boundary_conformance_closure_metadata")
    summary = _summary(closure, "distributed_standing_boundary_conformance_closure_summary")
    return _first_present(
        request.get("selected_conformance_closure_id"),
        _recursive_find(metadata, ("closure_result_id", "result_id"))
        if isinstance(metadata, Mapping)
        else None,
        _recursive_find(summary, ("closure_result_id", "closure_request_id", "result_id"))
        if summary
        else None,
        closure.get("closure_result_id"),
        closure.get("result_id"),
    )


def _extract_closure_outcome(closure: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    summary = _summary(closure, "distributed_standing_boundary_conformance_closure_summary")
    return _first_present(
        request.get("selected_conformance_closure_outcome"),
        closure.get("outcome"),
        _recursive_find(summary, ("outcome",)) if summary else None,
    )


def _closure_failed_check_count(closure: Mapping[str, Any]) -> int | None:
    summary = _summary(closure, "distributed_standing_boundary_conformance_closure_summary")
    if isinstance(summary.get("failed_check_count"), int):
        return int(summary["failed_check_count"])
    checks = closure.get("closure_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return None


def _closure_is_closure_result(closure: Mapping[str, Any]) -> bool:
    metadata = closure.get("distributed_standing_boundary_conformance_closure_metadata")
    result_type = (
        _recursive_find(metadata, ("closure_result_type", "result_type"))
        if isinstance(metadata, Mapping)
        else None
    )
    resolver_module = (
        _recursive_find(metadata, ("resolver_module",)) if isinstance(metadata, Mapping) else None
    )
    return (
        result_type == RESULT_TYPE
        or resolver_module == "resolve_distributed_standing_boundary_conformance_closure"
        or {
            "closure_checks",
            "closure_statement",
            "distributed_standing_boundary_conformance_closure_summary",
        }.issubset(set(closure.keys()))
    )


def _request_non_claims_conform(request: Mapping[str, Any]) -> tuple[bool, list[str], list[str]]:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False, list(REQUIRED_NON_CLAIMS), []
    missing = [key for key in REQUIRED_NON_CLAIMS if key not in declared]
    flipped = [key for key in REQUIRED_NON_CLAIMS if declared.get(key) is not False]
    return not missing and not flipped, missing, flipped


def _result_non_claims(request: Mapping[str, Any]) -> dict[str, Any]:
    conform, missing, flipped = _request_non_claims_conform(request)
    return {
        **_deepcopy(REQUIRED_NON_CLAIMS),
        "declared_non_claims_preserved": _deepcopy(request.get("declared_non_claims", {})),
        "declared_non_claims_conformant": conform,
        "missing_required_non_claims": missing,
        "flipped_required_non_claims": flipped,
    }


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
    }


def _declared_orientation_question_section(
    request: Mapping[str, Any],
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "orientation_request_id": request.get("orientation_request_id"),
        "orientation_question": request.get("orientation_question"),
        "orientation_intent": request.get("orientation_intent"),
        "orientation_request_path": request_path,
        "orientation_scope": _deepcopy(request.get("orientation_scope")),
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "self_orientation_is_not_permission": True,
        "self_orientation_is_not_continuation": True,
        "self_orientation_is_not_operation": True,
        "self_orientation_is_not_final_completion": True,
        "self_orientation_does_not_mutate_prior_surfaces": True,
    }


def _selected_prior_section(
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    prior_path: str | None,
    load_failures: Sequence[str],
) -> dict[str, Any]:
    prior_id = _extract_prior_id(prior, request)
    outcome = _extract_prior_outcome(prior, request)
    v8_lineage = _prior_is_v8_lineage(prior, outcome)
    return {
        "selected_prior_self_orientation_id": prior_id,
        "selected_prior_self_orientation_path": prior_path,
        "selected_prior_self_orientation_outcome": outcome,
        "selected_prior_self_orientation_preserved": bool(prior) and not load_failures,
        "selected_prior_self_orientation_identity_preserved": _is_present(prior_id),
        "selected_prior_self_orientation_outcome_preserved": _is_present(outcome),
        "v8_preserved_as_lineage": v8_lineage,
        "selected_prior_self_orientation_load_failures": list(load_failures),
        "raw_selected_prior_self_orientation": _deepcopy(dict(prior))
        if isinstance(prior, Mapping)
        else {},
    }


def _closure_section(
    request: Mapping[str, Any],
    closure: Mapping[str, Any],
    closure_path: str | None,
    load_failures: Sequence[str],
) -> dict[str, Any]:
    closure_id = _extract_closure_id(closure, request)
    outcome = _extract_closure_outcome(closure, request)
    failed_count = _closure_failed_check_count(closure)
    boundary_reference = _first_present(
        request.get("distributed_standing_boundary_result_reference"),
        _recursive_find(
            closure,
            (
                "selected_distributed_standing_boundary_result",
                "selected_distributed_standing_result_id",
                "distributed_standing_result_id",
                "distributed_standing_request_id",
            ),
        ),
    )
    conformance_reference = _first_present(
        request.get("distributed_standing_boundary_conformance_reference"),
        _recursive_find(
            closure,
            (
                "selected_conformance_result",
                "selected_conformance_result_id",
                "conformance_result_id",
                "conformance_request_id",
            ),
        ),
    )
    return {
        "selected_conformance_closure_id": closure_id,
        "selected_conformance_closure_path": closure_path,
        "selected_conformance_closure_outcome": outcome,
        "expected_selected_conformance_closure_outcome": EXPECTED_CLOSURE_OUTCOME,
        "selected_conformance_closure_failed_check_count": failed_count,
        "expected_failed_check_count": EXPECTED_CLOSURE_FAILED_CHECK_COUNT,
        "selected_conformance_closure_preserved": bool(closure) and not load_failures,
        "selected_conformance_closure_identity_preserved": _is_present(closure_id),
        "selected_conformance_closure_outcome_preserved": _is_present(outcome),
        "selected_conformance_closure_is_closure_result": bool(closure)
        and _closure_is_closure_result(closure),
        "selected_conformance_closure_closed": outcome == EXPECTED_CLOSURE_OUTCOME,
        "selected_conformance_closure_failed_check_count_zero": (
            failed_count == EXPECTED_CLOSURE_FAILED_CHECK_COUNT
        ),
        "distributed_standing_boundary_result_reference_preserved": _is_present(
            boundary_reference
        ),
        "distributed_standing_boundary_result_reference": _deepcopy(boundary_reference),
        "distributed_standing_boundary_conformance_reference_preserved": _is_present(
            conformance_reference
        ),
        "distributed_standing_boundary_conformance_reference": _deepcopy(
            conformance_reference
        ),
        "selected_conformance_closure_load_failures": list(load_failures),
        "raw_selected_distributed_standing_conformance_closure": _deepcopy(dict(closure))
        if isinstance(closure, Mapping)
        else {},
    }


def _orientation_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("orientation_basis")
    current_body_basis = request.get("current_body_conformance_v3_closure_basis")
    return {
        "orientation_basis_declared": _is_present(basis),
        "orientation_basis": _deepcopy(basis),
        "current_body_conformance_v3_closure_basis_preserved": _is_present(
            current_body_basis
        ),
        "current_body_conformance_v3_closure_basis": _deepcopy(current_body_basis),
        "distributed_standing_boundary_result_reference": _deepcopy(
            request.get("distributed_standing_boundary_result_reference")
        ),
        "distributed_standing_boundary_conformance_reference": _deepcopy(
            request.get("distributed_standing_boundary_conformance_reference")
        ),
        "reference_grounding": _deepcopy(request.get("reference_grounding")),
        "basis_does_not_authorize_continuation": True,
        "basis_does_not_authorize_operation": True,
        "basis_does_not_authorize_repository_sync": True,
        "basis_does_not_authorize_full_body_transfer": True,
        "basis_does_not_create_second_body": True,
        "basis_does_not_schedule_follow_on_work": True,
    }


def _build_canonical_declared_section(
    raw: Any,
    canonical: Mapping[str, Sequence[str]],
    declared_key: str,
    preserved_key: str,
) -> dict[str, Any]:
    section = {
        declared_key: _is_present(raw),
        "raw_declared_basis": _deepcopy(raw),
    }
    for key, aliases in canonical.items():
        section[key] = _declared_bool(raw, key, aliases)
    section[preserved_key] = _is_present(raw) and all(
        bool(section[key]) for key in canonical
    )
    return section


def _build_what_stands(raw: Any) -> dict[str, Any]:
    return _build_canonical_declared_section(
        raw,
        CANONICAL_WHAT_STANDS,
        "what_stands_declared",
        "what_stands_preserved",
    )


def _build_what_does_not_stand(raw: Any, request: Mapping[str, Any]) -> dict[str, Any]:
    section = _build_canonical_declared_section(
        raw,
        CANONICAL_WHAT_DOES_NOT_STAND,
        "what_does_not_stand_declared",
        "what_does_not_stand_declared_posture_preserved",
    )
    request_non_claims_conform, _, _ = _request_non_claims_conform(request)
    no_collapse = request_non_claims_conform and not _recursive_true(
        request,
        (
            "continuation_authorized",
            "orientation_authorizes_continuation",
            "distributed_operation_authorized",
            "orientation_authorizes_operation",
            "repository_synchronization_authorized",
            "orientation_authorizes_repository_sync",
            "full_body_transfer_authorized",
            "orientation_authorizes_full_body_transfer",
            "second_body_created",
            "orientation_creates_second_body",
            "permission_created",
            "orientation_creates_permission",
            "authority_created",
            "orientation_creates_authority",
            "truth_created",
            "action_authorized",
            "orientation_creates_truth",
            "orientation_authorizes_action",
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
            "orientation_claims_final_completion",
            "public_launch_readiness_created",
            "follow_on_work_authorized",
            "orientation_schedules_follow_on_work",
            "self_orientation_successor_scheduled",
        ),
    )
    section["forbidden_postures_remain_absent"] = no_collapse
    section["what_does_not_stand_preserved"] = (
        bool(section["what_does_not_stand_declared_posture_preserved"]) and no_collapse
    )
    return section


def _build_what_is_closed(raw: Any) -> dict[str, Any]:
    return _build_canonical_declared_section(
        raw,
        CANONICAL_WHAT_IS_CLOSED,
        "what_is_closed_declared",
        "what_is_closed_preserved",
    )


def _build_what_remains_open(raw: Any) -> dict[str, Any]:
    return {
        "what_remains_open_declared": _is_present(raw),
        "raw_declared_basis": _deepcopy(raw),
        **_deepcopy(WHAT_REMAINS_OPEN),
        "what_remains_open_preserved": _is_present(raw),
    }


def _no_orientation_continuation(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("continuation_authorized", "orientation_authorizes_continuation"),
    )


def _no_orientation_operation(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("distributed_operation_authorized", "orientation_authorizes_operation"),
    )


def _no_orientation_repository_sync(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("repository_synchronization_authorized", "orientation_authorizes_repository_sync"),
    )


def _no_orientation_full_body_transfer(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("full_body_transfer_authorized", "orientation_authorizes_full_body_transfer"),
    )


def _no_orientation_second_body(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("second_body_created", "orientation_creates_second_body"),
    )


def _no_orientation_permission(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("permission_created", "orientation_creates_permission"),
    )


def _no_orientation_authority(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        ("authority_created", "orientation_creates_authority"),
    )


def _no_orientation_truth_action(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "truth_created",
            "action_authorized",
            "orientation_creates_truth",
            "orientation_authorizes_action",
        ),
    )


def _no_orientation_final_completion(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
            "orientation_claims_final_completion",
            "final_completion_claimed",
        ),
    )


def _no_follow_on_work(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "follow_on_work_authorized",
            "orientation_schedules_follow_on_work",
            "self_orientation_successor_scheduled",
        ),
    )


def _no_prior_mutation(
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    closure: Mapping[str, Any],
) -> bool:
    mutation_keys = (
        "orientation_mutates_prior_result",
        "selected_prior_self_orientation_mutated",
        "selected_conformance_closure_mutated",
    )
    return not _recursive_true(request, mutation_keys) and not _recursive_true(
        prior,
        ("mutation_performed", "replay_performed", "merge_performed"),
    ) and not _recursive_true(
        closure,
        ("mutation_performed", "replay_performed", "merge_performed"),
    )


def _no_mutation_replay_merge(
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    closure: Mapping[str, Any],
) -> bool:
    keys = ("mutation_performed", "replay_performed", "merge_performed")
    return (
        not _recursive_true(request, keys)
        and not _recursive_true(prior, keys)
        and not _recursive_true(closure, keys)
    )


def _build_checks(
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    closure: Mapping[str, Any],
    prior_section: Mapping[str, Any],
    closure_section: Mapping[str, Any],
    basis_section: Mapping[str, Any],
    what_stands: Mapping[str, Any],
    what_does_not_stand: Mapping[str, Any],
    what_is_closed: Mapping[str, Any],
    what_remains_open: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    intent = request.get("orientation_intent")
    request_non_claims_conform, _, _ = _request_non_claims_conform(request)
    prior_load_failures = prior_section.get("selected_prior_self_orientation_load_failures") or []
    closure_load_failures = (
        closure_section.get("selected_conformance_closure_load_failures") or []
    )

    return [
        _make_check(
            "declared orientation request is well formed",
            "DECLARED_ORIENTATION_REQUEST_MALFORMED" not in precheck_failures,
            "mapping request",
            "malformed request"
            if "DECLARED_ORIENTATION_REQUEST_MALFORMED" in precheck_failures
            else "mapping request",
            "DECLARED_ORIENTATION_REQUEST_MALFORMED",
        ),
        _make_check(
            "declared orientation request readable",
            "DECLARED_ORIENTATION_REQUEST_UNREADABLE" not in precheck_failures,
            "readable request path or supplied mapping",
            "unreadable request path"
            if "DECLARED_ORIENTATION_REQUEST_UNREADABLE" in precheck_failures
            else "readable request",
            "DECLARED_ORIENTATION_REQUEST_UNREADABLE",
        ),
        _make_check(
            "orientation question declared",
            _is_present(request.get("orientation_question")),
            "declared orientation question",
            request.get("orientation_question"),
            "ORIENTATION_QUESTION_UNDECLARED",
        ),
        _make_check(
            "orientation intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "ORIENTATION_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "orientation request not explicitly blocked",
            intent != INTENT_BLOCK,
            "not explicit block intent",
            intent,
            "ORIENTATION_REQUEST_EXPLICITLY_BLOCKED",
        ),
        _make_check(
            "prior self-orientation readable and parseable",
            not prior_load_failures and bool(prior),
            "readable parseable prior self-orientation",
            prior_load_failures or "readable parseable",
            prior_load_failures[0] if prior_load_failures else "PRIOR_SELF_ORIENTATION_MISSING",
        ),
        _make_check(
            "prior self-orientation present",
            bool(prior_section.get("selected_prior_self_orientation_preserved")),
            "selected prior self-orientation present",
            prior_section.get("selected_prior_self_orientation_preserved"),
            "PRIOR_SELF_ORIENTATION_MISSING",
        ),
        _make_check(
            "v8 lineage preserved",
            bool(prior_section.get("v8_preserved_as_lineage")),
            "v8 preserved as lineage",
            prior_section.get("v8_preserved_as_lineage"),
            "PRIOR_SELF_ORIENTATION_MISSING",
        ),
        _make_check(
            "distributed standing conformance closure readable and parseable",
            not closure_load_failures and bool(closure),
            "readable parseable distributed standing conformance closure",
            closure_load_failures or "readable parseable",
            closure_load_failures[0]
            if closure_load_failures
            else "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        ),
        _make_check(
            "distributed standing conformance closure present",
            bool(closure_section.get("selected_conformance_closure_preserved")),
            "selected distributed standing conformance closure present",
            closure_section.get("selected_conformance_closure_preserved"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        ),
        _make_check(
            "distributed standing conformance closure is closure result",
            bool(closure_section.get("selected_conformance_closure_is_closure_result")),
            "distributed standing boundary conformance closure result",
            closure_section.get("selected_conformance_closure_is_closure_result"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
        ),
        _make_check(
            "distributed standing conformance closure outcome present",
            bool(closure_section.get("selected_conformance_closure_outcome_preserved")),
            "selected closure outcome present",
            closure_section.get("selected_conformance_closure_outcome"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_OUTCOME_MISSING",
        ),
        _make_check(
            "distributed standing conformance closure outcome closed",
            bool(closure_section.get("selected_conformance_closure_closed")),
            EXPECTED_CLOSURE_OUTCOME,
            closure_section.get("selected_conformance_closure_outcome"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_NOT_CLOSED",
        ),
        _make_check(
            "distributed standing conformance closure failed check count zero",
            bool(closure_section.get("selected_conformance_closure_failed_check_count_zero")),
            EXPECTED_CLOSURE_FAILED_CHECK_COUNT,
            closure_section.get("selected_conformance_closure_failed_check_count"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "distributed standing boundary result referenced",
            bool(
                closure_section.get(
                    "distributed_standing_boundary_result_reference_preserved"
                )
            ),
            "distributed standing boundary result reference",
            closure_section.get("distributed_standing_boundary_result_reference"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
        ),
        _make_check(
            "distributed standing boundary conformance result referenced",
            bool(
                closure_section.get(
                    "distributed_standing_boundary_conformance_reference_preserved"
                )
            ),
            "distributed standing boundary conformance reference",
            closure_section.get("distributed_standing_boundary_conformance_reference"),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
        ),
        _make_check(
            "orientation basis declared",
            bool(basis_section.get("orientation_basis_declared")),
            "orientation basis declared",
            basis_section.get("orientation_basis_declared"),
            "WHAT_STANDS_MISSING",
        ),
        _make_check(
            "current-body conformance v3 closure basis preserved",
            bool(
                basis_section.get("current_body_conformance_v3_closure_basis_preserved")
            ),
            "current-body conformance v3 closure basis preserved",
            basis_section.get("current_body_conformance_v3_closure_basis_preserved"),
            "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
        ),
        _make_check(
            "what stands present",
            bool(what_stands.get("what_stands_preserved")),
            "explicit what stands",
            what_stands.get("what_stands_preserved"),
            "WHAT_STANDS_MISSING",
        ),
        _make_check(
            "what does not stand present",
            bool(what_does_not_stand.get("what_does_not_stand_preserved")),
            "explicit what does not stand",
            what_does_not_stand.get("what_does_not_stand_preserved"),
            "WHAT_DOES_NOT_STAND_MISSING",
        ),
        _make_check(
            "what is closed present",
            bool(what_is_closed.get("what_is_closed_preserved")),
            "explicit what is closed",
            what_is_closed.get("what_is_closed_preserved"),
            "WHAT_IS_CLOSED_MISSING",
        ),
        _make_check(
            "what remains open present",
            bool(what_remains_open.get("what_remains_open_preserved")),
            "explicit what remains open",
            what_remains_open.get("what_remains_open_preserved"),
            "WHAT_REMAINS_OPEN_MISSING",
        ),
        _make_check(
            "no continuation",
            request_non_claims_conform and _no_orientation_continuation(request),
            False,
            False if _no_orientation_continuation(request) else True,
            "ORIENTATION_AUTHORIZES_CONTINUATION",
        ),
        _make_check(
            "no operation",
            request_non_claims_conform and _no_orientation_operation(request),
            False,
            False if _no_orientation_operation(request) else True,
            "ORIENTATION_AUTHORIZES_OPERATION",
        ),
        _make_check(
            "no repository sync",
            request_non_claims_conform and _no_orientation_repository_sync(request),
            False,
            False if _no_orientation_repository_sync(request) else True,
            "ORIENTATION_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _make_check(
            "no full body transfer",
            request_non_claims_conform and _no_orientation_full_body_transfer(request),
            False,
            False if _no_orientation_full_body_transfer(request) else True,
            "ORIENTATION_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _make_check(
            "no second body",
            request_non_claims_conform and _no_orientation_second_body(request),
            False,
            False if _no_orientation_second_body(request) else True,
            "ORIENTATION_CREATES_SECOND_BODY",
        ),
        _make_check(
            "no permission",
            request_non_claims_conform and _no_orientation_permission(request),
            False,
            False if _no_orientation_permission(request) else True,
            "ORIENTATION_CREATES_PERMISSION",
        ),
        _make_check(
            "no authority",
            request_non_claims_conform and _no_orientation_authority(request),
            False,
            False if _no_orientation_authority(request) else True,
            "ORIENTATION_CREATES_AUTHORITY",
        ),
        _make_check(
            "no truth action",
            request_non_claims_conform and _no_orientation_truth_action(request),
            False,
            False if _no_orientation_truth_action(request) else True,
            "ORIENTATION_CREATES_TRUTH_OR_ACTION",
        ),
        _make_check(
            "no final completion",
            request_non_claims_conform and _no_orientation_final_completion(request),
            False,
            False if _no_orientation_final_completion(request) else True,
            "ORIENTATION_CLAIMS_FINAL_COMPLETION",
        ),
        _make_check(
            "no follow-on work authorization",
            request_non_claims_conform and _no_follow_on_work(request),
            False,
            False if _no_follow_on_work(request) else True,
            "ORIENTATION_SCHEDULES_FOLLOW_ON_WORK",
        ),
        _make_check(
            "no prior result mutation",
            request_non_claims_conform and _no_prior_mutation(request, prior, closure),
            False,
            False if _no_prior_mutation(request, prior, closure) else True,
            "ORIENTATION_MUTATES_PRIOR_RESULT",
        ),
        _make_check(
            "no mutation replay or merge",
            request_non_claims_conform and _no_mutation_replay_merge(request, prior, closure),
            False,
            False if _no_mutation_replay_merge(request, prior, closure) else True,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _make_check(
            "non-claims remain false",
            request_non_claims_conform,
            "required non-claims false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]


def _decide_outcome(
    intent: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> tuple[str, dict[str, Any]]:
    failed_checks = [check for check in checks if not check.get("passed")]
    first_block_code = next(
        (check.get("block_code") for check in failed_checks if check.get("block_code")),
        None,
    )

    if intent == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": "ORIENTATION_REQUEST_EXPLICITLY_BLOCKED",
                "block_reason": "Orientation request explicitly declared block intent.",
            },
        )

    if failed_checks:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": first_block_code,
                "block_reason": "Current self-orientation v9 could not lawfully proceed.",
            },
        )

    if intent == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_RECORDED,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "not_recorded_reason": "Request explicitly declined current self-orientation v9 recording.",
            },
        )

    return (
        OUTCOME_RECORDED,
        {
            "blocked": False,
            "block_code": None,
            "block_reason": None,
        },
    )


def _build_orientation_statement(
    outcome: str,
    prior_section: Mapping[str, Any],
    closure_section: Mapping[str, Any],
    basis_section: Mapping[str, Any],
    what_stands: Mapping[str, Any],
    what_does_not_stand: Mapping[str, Any],
    what_is_closed: Mapping[str, Any],
    what_remains_open: Mapping[str, Any],
    request: Mapping[str, Any],
    prior: Mapping[str, Any],
    closure: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    failed_checks = [check for check in checks if not check.get("passed")]
    return {
        "current_self_orientation_v9_recorded": recorded,
        "prior_self_orientation_preserved": bool(
            prior_section.get("selected_prior_self_orientation_preserved")
        ),
        "v8_preserved_as_lineage": bool(prior_section.get("v8_preserved_as_lineage")),
        "distributed_standing_conformance_closure_preserved": bool(
            closure_section.get("selected_conformance_closure_preserved")
        ),
        "distributed_standing_conformance_closure_closed": bool(
            closure_section.get("selected_conformance_closure_closed")
        ),
        "distributed_standing_conformance_closure_failed_check_count_zero": bool(
            closure_section.get("selected_conformance_closure_failed_check_count_zero")
        ),
        "current_body_conformance_v3_closure_basis_preserved": bool(
            basis_section.get("current_body_conformance_v3_closure_basis_preserved")
        ),
        "what_stands_preserved": bool(what_stands.get("what_stands_preserved")),
        "what_does_not_stand_preserved": bool(
            what_does_not_stand.get("what_does_not_stand_preserved")
        ),
        "what_is_closed_preserved": bool(what_is_closed.get("what_is_closed_preserved")),
        "what_remains_open_preserved": bool(
            what_remains_open.get("what_remains_open_preserved")
        ),
        "orientation_did_not_create_permission": _no_orientation_permission(request),
        "orientation_did_not_authorize_continuation": _no_orientation_continuation(
            request
        ),
        "orientation_did_not_authorize_operation": _no_orientation_operation(request),
        "orientation_did_not_authorize_repository_sync": _no_orientation_repository_sync(
            request
        ),
        "orientation_did_not_authorize_full_body_transfer": (
            _no_orientation_full_body_transfer(request)
        ),
        "orientation_did_not_create_second_body": _no_orientation_second_body(request),
        "orientation_did_not_claim_final_completion": _no_orientation_final_completion(
            request
        ),
        "orientation_did_not_schedule_follow_on_work": _no_follow_on_work(request),
        "orientation_did_not_mutate_prior_result": _no_prior_mutation(
            request,
            prior,
            closure,
        ),
        "permission_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "truth_created": False,
        "action_authorized": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "self_orientation_successor_scheduled": False,
        "prior_result_mutated": False,
        "failed_checks_preserved": _deepcopy(failed_checks),
    }


def build_current_self_orientation_v9_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact bounded summary for a current self-orientation v9 result."""

    checks = result.get("orientation_checks", [])
    checks_list = checks if isinstance(checks, list) else []
    passed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and check.get("passed")
    )
    failed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and not check.get("passed")
    )

    declared = result.get("declared_orientation_question", {})
    statement = result.get("orientation_statement", {})
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})

    declared_map = declared if isinstance(declared, Mapping) else {}
    statement_map = statement if isinstance(statement, Mapping) else {}
    block_map = block if isinstance(block, Mapping) else {}
    non_claim_map = non_claims if isinstance(non_claims, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code"),
        "block_reason": block_map.get("block_reason"),
        "orientation_request_id": declared_map.get("orientation_request_id"),
        "orientation_question": declared_map.get("orientation_question"),
        "orientation_intent": declared_map.get("orientation_intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "current_self_orientation_v9_recorded": statement_map.get(
            "current_self_orientation_v9_recorded"
        ),
        "prior_self_orientation_preserved": statement_map.get(
            "prior_self_orientation_preserved"
        ),
        "v8_preserved_as_lineage": statement_map.get("v8_preserved_as_lineage"),
        "distributed_standing_conformance_closure_preserved": statement_map.get(
            "distributed_standing_conformance_closure_preserved"
        ),
        "distributed_standing_conformance_closure_closed": statement_map.get(
            "distributed_standing_conformance_closure_closed"
        ),
        "distributed_standing_conformance_closure_failed_check_count_zero": (
            statement_map.get(
                "distributed_standing_conformance_closure_failed_check_count_zero"
            )
        ),
        "current_body_conformance_v3_closure_basis_preserved": statement_map.get(
            "current_body_conformance_v3_closure_basis_preserved"
        ),
        "what_stands_preserved": statement_map.get("what_stands_preserved"),
        "what_does_not_stand_preserved": statement_map.get(
            "what_does_not_stand_preserved"
        ),
        "what_is_closed_preserved": statement_map.get("what_is_closed_preserved"),
        "what_remains_open_preserved": statement_map.get("what_remains_open_preserved"),
        "orientation_did_not_create_permission": statement_map.get(
            "orientation_did_not_create_permission"
        ),
        "orientation_did_not_authorize_continuation": statement_map.get(
            "orientation_did_not_authorize_continuation"
        ),
        "orientation_did_not_authorize_operation": statement_map.get(
            "orientation_did_not_authorize_operation"
        ),
        "orientation_did_not_authorize_repository_sync": statement_map.get(
            "orientation_did_not_authorize_repository_sync"
        ),
        "orientation_did_not_authorize_full_body_transfer": statement_map.get(
            "orientation_did_not_authorize_full_body_transfer"
        ),
        "orientation_did_not_create_second_body": statement_map.get(
            "orientation_did_not_create_second_body"
        ),
        "orientation_did_not_claim_final_completion": statement_map.get(
            "orientation_did_not_claim_final_completion"
        ),
        "orientation_did_not_schedule_follow_on_work": statement_map.get(
            "orientation_did_not_schedule_follow_on_work"
        ),
        "orientation_did_not_mutate_prior_result": statement_map.get(
            "orientation_did_not_mutate_prior_result"
        ),
        "key_non_claims": {
            key: non_claim_map.get(key)
            for key in (
                "authority_created",
                "permission_created",
                "currentness_created",
                "carrier_currentness_created",
                "source_replaced",
                "current_carrier_selected",
                "winning_carrier_selected",
                "losing_carrier_invalidated",
                "divergence_resolved",
                "truth_created",
                "action_authorized",
                "repository_synchronization_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "continuation_authorized",
                "distributed_operation_authorized",
                "final_governance_completed",
                "final_continuity_completed",
                "final_system_identity_completed",
                "public_launch_readiness_created",
                "follow_on_work_authorized",
                "self_orientation_successor_scheduled",
            )
        },
    }


def _build_result(
    request: Mapping[str, Any],
    request_path: str | None,
    prior: Mapping[str, Any],
    prior_path: str | None,
    prior_load_failures: Sequence[str],
    closure: Mapping[str, Any],
    closure_path: str | None,
    closure_load_failures: Sequence[str],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    declared = _declared_orientation_question_section(request, request_path)
    prior_section = _selected_prior_section(
        request,
        prior,
        prior_path,
        prior_load_failures,
    )
    closure_result_section = _closure_section(
        request,
        closure,
        closure_path,
        closure_load_failures,
    )
    orientation_basis = _orientation_basis_section(request)
    what_stands = _build_what_stands(request.get("what_stands"))
    what_does_not_stand = _build_what_does_not_stand(
        request.get("what_does_not_stand"),
        request,
    )
    what_is_closed = _build_what_is_closed(request.get("what_is_closed"))
    what_remains_open = _build_what_remains_open(request.get("what_remains_open"))

    checks = _build_checks(
        request,
        prior,
        closure,
        prior_section,
        closure_result_section,
        orientation_basis,
        what_stands,
        what_does_not_stand,
        what_is_closed,
        what_remains_open,
        precheck_failures,
    )
    outcome, block = _decide_outcome(request.get("orientation_intent"), checks)
    statement = _build_orientation_statement(
        outcome,
        prior_section,
        closure_result_section,
        orientation_basis,
        what_stands,
        what_does_not_stand,
        what_is_closed,
        what_remains_open,
        request,
        prior,
        closure,
        checks,
    )
    result_id = _first_present(
        request.get("orientation_request_id"),
        "current_self_orientation_v9",
    )

    result = {
        "current_self_orientation_v9_metadata": {
            "current_self_orientation_v9_result_id": (
                f"{result_id}__current_self_orientation_v9"
            ),
            "current_self_orientation_v9_result_type": RESULT_TYPE,
            "current_self_orientation_v9_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_orientation_question": declared,
        "selected_prior_self_orientation": prior_section,
        "selected_distributed_standing_conformance_closure": closure_result_section,
        "orientation_basis": orientation_basis,
        "what_stands": what_stands,
        "what_does_not_stand": what_does_not_stand,
        "what_is_closed": what_is_closed,
        "what_remains_open": what_remains_open,
        "orientation_checks": checks,
        "orientation_statement": statement,
        "orientation_non_meaning": _deepcopy(ORIENTATION_NON_MEANING),
        "non_claims": _result_non_claims(request),
        "outcome": outcome,
        "block": block,
    }
    result["current_self_orientation_v9_summary"] = build_current_self_orientation_v9_summary(
        result
    )
    return result


def resolve_current_self_orientation_v9(
    declared_orientation_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded current self-orientation v9 request."""

    if declared_orientation_request is None:
        request: dict[str, Any] = {}
        precheck_failures: list[str] = []
    elif not isinstance(declared_orientation_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_ORIENTATION_REQUEST_MALFORMED"]
    else:
        request = _deepcopy(dict(declared_orientation_request))
        precheck_failures = []

    prior, prior_path, prior_load_failures = _load_selected_mapping(
        request,
        object_key="selected_prior_self_orientation",
        path_key="selected_prior_self_orientation_path",
        missing_code="PRIOR_SELF_ORIENTATION_MISSING",
        unreadable_code="PRIOR_SELF_ORIENTATION_UNREADABLE",
        malformed_code="PRIOR_SELF_ORIENTATION_MALFORMED",
    )
    closure, closure_path, closure_load_failures = _load_selected_mapping(
        request,
        object_key="selected_distributed_standing_conformance_closure",
        path_key="selected_conformance_closure_path",
        missing_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        unreadable_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_UNREADABLE",
        malformed_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
    )
    return _build_result(
        request,
        None,
        prior,
        prior_path,
        prior_load_failures,
        closure,
        closure_path,
        closure_load_failures,
        precheck_failures,
    )


def resolve_current_self_orientation_v9_from_path(
    declared_orientation_request_path: Path | str,
) -> dict:
    """Load a JSON object orientation request from path and resolve v9."""

    path = _to_path(declared_orientation_request_path)
    try:
        request = _read_json_object(
            path,
            "DECLARED_ORIENTATION_REQUEST_UNREADABLE",
            "DECLARED_ORIENTATION_REQUEST_MALFORMED",
        )
        precheck_failures: list[str] = []
    except CurrentSelfOrientationV9Error as exc:
        request = {}
        precheck_failures = [exc.block_code]

    prior, prior_path, prior_load_failures = _load_selected_mapping(
        request,
        object_key="selected_prior_self_orientation",
        path_key="selected_prior_self_orientation_path",
        missing_code="PRIOR_SELF_ORIENTATION_MISSING",
        unreadable_code="PRIOR_SELF_ORIENTATION_UNREADABLE",
        malformed_code="PRIOR_SELF_ORIENTATION_MALFORMED",
    )
    closure, closure_path, closure_load_failures = _load_selected_mapping(
        request,
        object_key="selected_distributed_standing_conformance_closure",
        path_key="selected_conformance_closure_path",
        missing_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        unreadable_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_UNREADABLE",
        malformed_code="DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
    )
    return _build_result(
        request,
        str(path),
        prior,
        prior_path,
        prior_load_failures,
        closure,
        closure_path,
        closure_load_failures,
        precheck_failures,
    )


def write_current_self_orientation_v9_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current self-orientation v9 result as stable JSON."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV9Error(
            "Current self-orientation v9 result must be a mapping.",
            "CURRENT_SELF_ORIENTATION_V9_RESULT_MALFORMED",
        )

    result_copy = _deepcopy(dict(result))
    if output_path is None:
        summary = result_copy.get("current_self_orientation_v9_summary", {})
        request_id = (
            summary.get("orientation_request_id") if isinstance(summary, Mapping) else None
        )
        filename_root = _safe_filename_part(request_id or "current_self_orientation_v9")
        output = (
            CURRENT_SELF_ORIENTATION_V9_ROOT
            / f"{filename_root}__current_self_orientation_v9_result.json"
        )
    else:
        output = Path(output_path)
        if not output.is_absolute():
            output = REPO_ROOT / output

    output.parent.mkdir(parents=True, exist_ok=True)
    final_path = _non_overwriting_path(output)
    final_path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_current_self_orientation_v9_request(
    orientation_request_id: str,
    orientation_question: str,
    selected_prior_self_orientation: Mapping[str, Any] | str,
    selected_distributed_standing_conformance_closure: Mapping[str, Any] | str,
    orientation_basis: Mapping[str, Any] | str,
    what_stands: Mapping[str, Any] | Sequence[str],
    what_does_not_stand: Mapping[str, Any] | Sequence[str],
    what_is_closed: Mapping[str, Any] | Sequence[str],
    what_remains_open: Mapping[str, Any] | Sequence[str],
    orientation_intent: str = INTENT_RECORD,
    *,
    selected_prior_self_orientation_path: str | None = None,
    selected_conformance_closure_path: str | None = None,
    current_body_conformance_v3_closure_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded declared v9 orientation request with false non-claims."""

    current_body_basis = (
        current_body_conformance_v3_closure_basis
        if current_body_conformance_v3_closure_basis is not None
        else {
            "basis": "current-body conformance v3 closure remains basis for v9 orientation",
            "does_not_authorize_continuation": True,
            "does_not_authorize_operation": True,
        }
    )

    request = {
        "orientation_request_id": orientation_request_id,
        "orientation_question": orientation_question,
        "orientation_intent": orientation_intent,
        "selected_prior_self_orientation": _deepcopy(selected_prior_self_orientation),
        "selected_distributed_standing_conformance_closure": _deepcopy(
            selected_distributed_standing_conformance_closure
        ),
        "orientation_basis": _deepcopy(orientation_basis),
        "what_stands": _deepcopy(what_stands),
        "what_does_not_stand": _deepcopy(what_does_not_stand),
        "what_is_closed": _deepcopy(what_is_closed),
        "what_remains_open": _deepcopy(what_remains_open),
        "current_body_conformance_v3_closure_basis": _deepcopy(current_body_basis),
        "declared_non_claims": _deepcopy(REQUIRED_NON_CLAIMS),
    }

    if selected_prior_self_orientation_path is not None:
        request["selected_prior_self_orientation_path"] = selected_prior_self_orientation_path
    if selected_conformance_closure_path is not None:
        request["selected_conformance_closure_path"] = selected_conformance_closure_path

    return request
