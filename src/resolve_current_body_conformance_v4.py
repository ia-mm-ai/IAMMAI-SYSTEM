"""Bounded current-body conformance v4 resolver.

This resolver checks whether one selected current self-orientation v9 result
conforms to the current body line after distributed standing boundary
conformance closure. It records conformance of orientation only. It does not
create current self-orientation v10, create current-body conformance v4 closure,
authorize continuation, authorize operation, synchronize repositories, transfer
the body, create a second body, create permission or authority, create truth or
action, claim final completion, create public launch readiness, schedule
follow-on work, or mutate v9, v8, or prior artifacts.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentBodyConformanceV4Error(Exception):
    """Hard failure for malformed or unreadable explicit v4 conformance inputs."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REPO_ROOT = Path(__file__).resolve().parents[1]
CURRENT_BODY_CONFORMANCE_V4_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_v4"
)

RESOLVER_MODULE = "resolve_current_body_conformance_v4"
RESULT_TYPE = "current_body_conformance_v4_result"
RESULT_VERSION = "0.1.0"

OUTCOME_CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_CONFORMANT"
OUTCOME_NOT_CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_NOT_CONFORMANT"
OUTCOME_BLOCKED = "CURRENT_BODY_CONFORMANCE_V4_BLOCKED"

SUPPORTED_OUTCOMES = {
    OUTCOME_CONFORMANT,
    OUTCOME_NOT_CONFORMANT,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_CURRENT_BODY_CONFORMANCE_V4"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_CURRENT_BODY_CONFORMANCE_V4"
INTENT_BLOCK = "BLOCK_CURRENT_BODY_CONFORMANCE_V4"

SUPPORTED_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

EXPECTED_SELECTED_V9_OUTCOME = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
EXPECTED_FAILED_CHECK_COUNT = 0

BLOCKING_FAILURE_CODES = {
    "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
    "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
    "CONFORMANCE_QUESTION_UNDECLARED",
    "CONFORMANCE_INTENT_UNSUPPORTED",
    "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED",
    "CURRENT_SELF_ORIENTATION_V9_MISSING",
    "CURRENT_SELF_ORIENTATION_V9_UNREADABLE",
    "CURRENT_SELF_ORIENTATION_V9_MALFORMED",
    "CURRENT_SELF_ORIENTATION_V9_IDENTITY_MISSING",
    "CURRENT_SELF_ORIENTATION_V9_OUTCOME_MISSING",
}

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
    "conformance_authorized_continuation": False,
    "conformance_authorized_operation": False,
    "conformance_claimed_final_completion": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

SELECTED_V9_REQUIRED_NON_CLAIMS = {
    key
    for key in REQUIRED_NON_CLAIMS
    if key
    not in {
        "conformance_authorized_continuation",
        "conformance_authorized_operation",
        "conformance_claimed_final_completion",
    }
}

CONFORMANCE_NON_MEANING = {
    "continuation": True,
    "operation": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body": True,
    "distributed_standing_implementation": True,
    "distributed_operation": True,
    "final_completion": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "final_system_identity": True,
    "public_launch_readiness": True,
    "permission": True,
    "authority": True,
    "truth": True,
    "action": True,
    "currentness": True,
    "carrier_currentness": True,
    "current_carrier_selected": True,
    "winning_carrier_selected": True,
    "losing_carrier_invalidated": True,
    "source_replacement": True,
    "divergence_resolution": True,
    "evidence_erasure": True,
    "current_self_orientation_v10": True,
    "current_body_conformance_v4_closure_by_default": True,
    "follow_on_work_authorization": True,
    "does_not_mean_continuation": True,
    "does_not_mean_operation": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_final_completion": True,
    "does_not_mean_public_launch_readiness": True,
    "does_not_mean_permission": True,
    "does_not_mean_current_self_orientation_v10": True,
    "does_not_mean_v4_closure_by_default": True,
    "does_not_mean_follow_on_work_authorization": True,
}

WHAT_REMAINS_OPEN = {
    "current_body_conformance_v4_closure": "open_not_scheduled_not_authorized_not_executed",
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
        raise CurrentBodyConformanceV4Error(
            f"Unable to read JSON object from {path}: {exc}",
            unreadable_code,
        ) from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CurrentBodyConformanceV4Error(
            f"Malformed JSON object at {path}: {exc}",
            malformed_code,
        ) from exc

    if not isinstance(parsed, Mapping):
        raise CurrentBodyConformanceV4Error(
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


def _recursive_present(value: Any, keys: Sequence[str]) -> bool:
    found = _recursive_find(value, keys)
    return _is_present(found)


def _summary(mapping: Mapping[str, Any], *summary_keys: str) -> Mapping[str, Any]:
    for key in summary_keys:
        value = mapping.get(key)
        if isinstance(value, Mapping):
            return value
    return {}


def _safe_filename_part(value: Any) -> str:
    text = str(value or "current_body_conformance_v4").strip()
    cleaned = []
    for character in text:
        if character.isalnum() or character in ("-", "_"):
            cleaned.append(character)
        else:
            cleaned.append("_")
    filename = "".join(cleaned).strip("_").lower()
    return filename or "current_body_conformance_v4"


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


def _load_selected_v9(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any], str | None, list[str]]:
    path_value = _path_value(
        request,
        "selected_current_self_orientation_v9_path",
        "selected_current_self_orientation_v9",
    )
    if path_value:
        path = _to_path(path_value)
        try:
            return (
                _read_json_object(
                    path,
                    "CURRENT_SELF_ORIENTATION_V9_UNREADABLE",
                    "CURRENT_SELF_ORIENTATION_V9_MALFORMED",
                ),
                str(path),
                [],
            )
        except CurrentBodyConformanceV4Error as exc:
            return {}, str(path), [exc.block_code]

    selected = request.get("selected_current_self_orientation_v9")
    if isinstance(selected, Mapping):
        return _deepcopy(dict(selected)), None, []
    if selected is None:
        return {}, None, ["CURRENT_SELF_ORIENTATION_V9_MISSING"]
    return {}, None, ["CURRENT_SELF_ORIENTATION_V9_MALFORMED"]


def _extract_v9_id(v9: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    metadata = v9.get("current_self_orientation_v9_metadata")
    summary = _summary(v9, "current_self_orientation_v9_summary")
    return _first_present(
        request.get("selected_current_self_orientation_v9_id"),
        _recursive_find(
            metadata,
            ("current_self_orientation_v9_result_id", "orientation_result_id", "result_id"),
        )
        if isinstance(metadata, Mapping)
        else None,
        _recursive_find(
            summary,
            ("current_self_orientation_v9_result_id", "orientation_request_id", "result_id"),
        )
        if summary
        else None,
        v9.get("current_self_orientation_v9_result_id"),
        v9.get("orientation_result_id"),
        v9.get("result_id"),
    )


def _extract_v9_outcome(v9: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    summary = _summary(v9, "current_self_orientation_v9_summary")
    return _first_present(
        request.get("selected_current_self_orientation_v9_outcome"),
        v9.get("outcome"),
        _recursive_find(summary, ("outcome",)) if summary else None,
    )


def _v9_failed_check_count(v9: Mapping[str, Any]) -> int | None:
    summary = _summary(v9, "current_self_orientation_v9_summary")
    if isinstance(summary.get("failed_check_count"), int):
        return int(summary["failed_check_count"])
    checks = v9.get("orientation_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return None


def _v9_is_current_self_orientation_v9(v9: Mapping[str, Any]) -> bool:
    metadata = v9.get("current_self_orientation_v9_metadata")
    result_type = (
        _recursive_find(metadata, ("current_self_orientation_v9_result_type", "result_type"))
        if isinstance(metadata, Mapping)
        else None
    )
    resolver_module = (
        _recursive_find(metadata, ("resolver_module",)) if isinstance(metadata, Mapping) else None
    )
    return (
        result_type == "current_self_orientation_v9_result"
        or resolver_module == "resolve_current_self_orientation_v9"
        or {
            "orientation_checks",
            "orientation_statement",
            "current_self_orientation_v9_summary",
        }.issubset(set(v9.keys()))
    )


def _statement(v9: Mapping[str, Any]) -> Mapping[str, Any]:
    value = v9.get("orientation_statement")
    return value if isinstance(value, Mapping) else {}


def _orientation_summary(v9: Mapping[str, Any]) -> Mapping[str, Any]:
    return _summary(v9, "current_self_orientation_v9_summary")


def _statement_or_summary_true(v9: Mapping[str, Any], *keys: str) -> bool:
    statement = _statement(v9)
    summary = _orientation_summary(v9)
    return any(statement.get(key) is True or summary.get(key) is True for key in keys)


def _mapping_section(v9: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = v9.get(key)
    return value if isinstance(value, Mapping) else {}


def _selected_v9_non_claims_conform(v9: Mapping[str, Any]) -> tuple[bool, list[str], list[str]]:
    non_claims = v9.get("non_claims")
    if not isinstance(non_claims, Mapping):
        return False, sorted(SELECTED_V9_REQUIRED_NON_CLAIMS), []
    missing = sorted(key for key in SELECTED_V9_REQUIRED_NON_CLAIMS if key not in non_claims)
    flipped = sorted(key for key in SELECTED_V9_REQUIRED_NON_CLAIMS if non_claims.get(key) is not False)
    return not missing and not flipped, missing, flipped


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
    failure_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "failure_code": None if passed else failure_code,
    }


def _declared_conformance_question_section(
    request: Mapping[str, Any],
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "conformance_request_id": request.get("conformance_request_id"),
        "conformance_question": request.get("conformance_question"),
        "conformance_intent": request.get("conformance_intent"),
        "declared_conformance_request_path": request_path,
        "conformance_scope": _deepcopy(request.get("conformance_scope")),
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "conformance_is_not_permission": True,
        "conformance_is_not_continuation": True,
        "conformance_is_not_operation": True,
        "conformance_is_not_final_completion": True,
        "conformance_does_not_create_current_self_orientation_v10": True,
        "conformance_does_not_create_current_body_conformance_v4_closure": True,
        "conformance_does_not_mutate_v9": True,
    }


def _selected_v9_section(
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
    v9_path: str | None,
    load_failures: Sequence[str],
) -> dict[str, Any]:
    v9_id = _extract_v9_id(v9, request)
    outcome = _extract_v9_outcome(v9, request)
    failed_count = _v9_failed_check_count(v9)
    return {
        "selected_current_self_orientation_v9_id": v9_id,
        "selected_current_self_orientation_v9_path": v9_path,
        "selected_current_self_orientation_v9_outcome": outcome,
        "expected_selected_v9_outcome": request.get(
            "expected_selected_v9_outcome",
            EXPECTED_SELECTED_V9_OUTCOME,
        ),
        "selected_v9_failed_check_count": failed_count,
        "expected_failed_check_count": request.get(
            "expected_failed_check_count",
            EXPECTED_FAILED_CHECK_COUNT,
        ),
        "selected_v9_preserved": bool(v9) and not load_failures,
        "selected_v9_identity_preserved": _is_present(v9_id),
        "selected_v9_outcome_preserved": _is_present(outcome),
        "selected_v9_is_current_self_orientation_v9": bool(v9)
        and _v9_is_current_self_orientation_v9(v9),
        "selected_v9_recorded": outcome == EXPECTED_SELECTED_V9_OUTCOME,
        "selected_v9_failed_check_count_zero": failed_count == EXPECTED_FAILED_CHECK_COUNT,
        "selected_v9_load_failures": list(load_failures),
        "raw_selected_current_self_orientation_v9": _deepcopy(dict(v9))
        if isinstance(v9, Mapping)
        else {},
    }


def _basis_item_present(request: Mapping[str, Any], v9: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return _recursive_present(request, keys) or _recursive_present(v9, keys)


def _current_body_conformance_v4_basis_section(
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
) -> dict[str, Any]:
    basis = request.get("current_body_conformance_v4_basis")
    return {
        "current_body_conformance_v4_basis_declared": _is_present(basis),
        "current_body_conformance_v4_basis": _deepcopy(basis),
        "selected_prior_self_orientation_v8": _deepcopy(
            request.get("selected_prior_self_orientation_v8")
        ),
        "selected_distributed_standing_conformance_closure": _deepcopy(
            request.get("selected_distributed_standing_conformance_closure")
        ),
        "current_body_conformance_v3_closure_basis": _deepcopy(
            request.get("current_body_conformance_v3_closure_basis")
        ),
        "distributed_standing_boundary_reference": _deepcopy(
            request.get("distributed_standing_boundary_reference")
        ),
        "distributed_standing_boundary_conformance_reference": _deepcopy(
            request.get("distributed_standing_boundary_conformance_reference")
        ),
        "divergence_consequence_reference": _deepcopy(
            request.get("divergence_consequence_reference")
        ),
        "currentness_successor_reference": _deepcopy(
            request.get("currentness_successor_reference")
        ),
        "continuity_turn_v2_reference": _deepcopy(
            request.get("continuity_turn_v2_reference")
        ),
        "standing_propagation_v2_reference": _deepcopy(
            request.get("standing_propagation_v2_reference")
        ),
        "registry_persistence_v2_reference": _deepcopy(
            request.get("registry_persistence_v2_reference")
        ),
        "lifecycle_reference": _deepcopy(request.get("lifecycle_reference")),
        "relation_conformance_closure_reference": _deepcopy(
            request.get("relation_conformance_closure_reference")
        ),
        "v8_lineage_basis_preserved": _basis_item_present(
            request,
            v9,
            ("selected_prior_self_orientation_v8", "v8_preserved_as_lineage"),
        ),
        "current_body_conformance_v3_closure_basis_preserved": _basis_item_present(
            request,
            v9,
            (
                "current_body_conformance_v3_closure_basis",
                "current_body_conformance_v3_closure_basis_preserved",
            ),
        ),
        "distributed_standing_boundary_result_preserved": _basis_item_present(
            request,
            v9,
            (
                "distributed_standing_boundary_reference",
                "distributed_standing_boundary_result_reference",
                "distributed_standing_boundary_result",
            ),
        ),
        "distributed_standing_boundary_conformance_result_preserved": _basis_item_present(
            request,
            v9,
            (
                "distributed_standing_boundary_conformance_reference",
                "distributed_standing_boundary_conformance_result",
            ),
        ),
        "distributed_standing_boundary_conformance_closure_result_preserved": _basis_item_present(
            request,
            v9,
            (
                "selected_distributed_standing_conformance_closure",
                "distributed_standing_conformance_closure_preserved",
                "distributed_standing_boundary_conformance_closure",
            ),
        ),
        "basis_is_not_permission_set": True,
        "basis_is_not_operation_plan": True,
        "basis_is_not_repository_synchronization_plan": True,
        "basis_is_not_full_body_transfer_plan": True,
        "basis_is_not_second_body_creation_plan": True,
        "basis_is_not_final_governance": True,
    }


def _no_selected_v9_continuation(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_authorize_continuation") and not _recursive_true(
        v9,
        ("continuation_authorized", "orientation_authorizes_continuation"),
    )


def _no_selected_v9_operation(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_authorize_operation") and not _recursive_true(
        v9,
        ("distributed_operation_authorized", "orientation_authorizes_operation"),
    )


def _no_selected_v9_repository_sync(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_authorize_repository_sync") and not _recursive_true(
        v9,
        ("repository_synchronization_authorized", "orientation_authorizes_repository_sync"),
    )


def _no_selected_v9_full_body_transfer(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_authorize_full_body_transfer") and not _recursive_true(
        v9,
        ("full_body_transfer_authorized", "orientation_authorizes_full_body_transfer"),
    )


def _no_selected_v9_second_body(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_create_second_body") and not _recursive_true(
        v9,
        ("second_body_created", "orientation_creates_second_body"),
    )


def _no_selected_v9_permission(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_create_permission") and not _recursive_true(
        v9,
        ("permission_created", "orientation_creates_permission"),
    )


def _no_selected_v9_authority(v9: Mapping[str, Any]) -> bool:
    return not _recursive_true(v9, ("authority_created", "orientation_creates_authority"))


def _no_selected_v9_truth_action(v9: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        v9,
        (
            "truth_created",
            "action_authorized",
            "orientation_creates_truth",
            "orientation_authorizes_action",
        ),
    )


def _no_selected_v9_final_completion(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_claim_final_completion") and not _recursive_true(
        v9,
        (
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
            "orientation_claims_final_completion",
            "final_completion_claimed",
        ),
    )


def _no_selected_v9_follow_on_work(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_schedule_follow_on_work") and not _recursive_true(
        v9,
        (
            "follow_on_work_authorized",
            "orientation_schedules_follow_on_work",
        ),
    )


def _no_selected_v9_self_orientation_successor(v9: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        v9,
        (
            "self_orientation_successor_scheduled",
            "orientation_schedules_self_orientation_successor",
        ),
    )


def _no_selected_v9_prior_mutation(v9: Mapping[str, Any]) -> bool:
    return _statement_or_summary_true(v9, "orientation_did_not_mutate_prior_result") and not _recursive_true(
        v9,
        (
            "orientation_mutates_prior_result",
            "selected_prior_self_orientation_mutated",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
        ),
    )


def _no_conformance_continuation(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "conformance_authorized_continuation",
            "conformance_authorizes_continuation",
            "continuation_authorized",
        ),
    )


def _no_conformance_operation(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "conformance_authorized_operation",
            "conformance_authorizes_operation",
            "distributed_operation_authorized",
        ),
    )


def _no_conformance_permission(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "permission_created",
            "conformance_creates_permission",
            "conformance_created_permission",
        ),
    )


def _no_conformance_final_completion(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "conformance_claimed_final_completion",
            "conformance_claims_final_completion",
            "final_completion_claimed",
            "final_governance_completed",
            "final_continuity_completed",
            "final_system_identity_completed",
            "public_launch_readiness_created",
        ),
    )


def _no_conformance_follow_on_work(request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "follow_on_work_authorized",
            "conformance_schedules_follow_on_work",
            "self_orientation_successor_scheduled",
        ),
    )


def _no_conformance_mutation(v9: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    return not _recursive_true(
        request,
        (
            "conformance_mutated_v9",
            "selected_v9_mutated",
            "v9_mutated",
        ),
    ) and not _recursive_true(v9, ("mutation_performed", "replay_performed", "merge_performed"))


def _no_mutation_replay_merge(v9: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    keys = ("mutation_performed", "replay_performed", "merge_performed")
    return not _recursive_true(request, keys) and not _recursive_true(v9, keys)


def _orientation_non_meaning_preserved(v9: Mapping[str, Any]) -> bool:
    non_meaning = _mapping_section(v9, "orientation_non_meaning")
    required = (
        "permission",
        "continuation",
        "operation",
        "repository_synchronization",
        "full_body_transfer",
        "second_body",
        "distributed_operation",
        "final_completion",
        "public_launch_readiness",
        "follow_on_work_authorization",
        "self_orientation_successor_beyond_v9",
    )
    return bool(non_meaning) and all(non_meaning.get(key) is True for key in required)


def _build_v9_orientation_conformance(v9: Mapping[str, Any]) -> dict[str, Any]:
    statement = _statement(v9)
    what_stands = _mapping_section(v9, "what_stands")
    what_does_not_stand = _mapping_section(v9, "what_does_not_stand")
    what_is_closed = _mapping_section(v9, "what_is_closed")
    what_remains_open = _mapping_section(v9, "what_remains_open")
    v9_non_claims_conform, missing, flipped = _selected_v9_non_claims_conform(v9)

    latest_shortcut_absent = not _recursive_true(
        v9,
        (
            "latest_file_standing_created",
            "latest_turn_standing_created",
            "carrier_possession_created_standing",
            "successful_receipt_count_created_standing",
            "majority_standing_created",
            "registry_presence_created_standing",
            "lifecycle_status_created_standing",
            "summary_projection_created_standing",
            "availability_created_standing",
            "narrative_convenience_created_standing",
        ),
    )

    section = {
        "selected_v9_preserved_v8_as_lineage": _statement_or_summary_true(
            v9,
            "v8_preserved_as_lineage",
        ),
        "selected_v9_preserved_distributed_standing_conformance_closure": (
            _statement_or_summary_true(
                v9,
                "distributed_standing_conformance_closure_preserved",
            )
        ),
        "selected_v9_preserved_distributed_standing_conformance_closure_closed": (
            _statement_or_summary_true(
                v9,
                "distributed_standing_conformance_closure_closed",
            )
        ),
        "selected_v9_preserved_current_body_conformance_v3_closure_basis": (
            _statement_or_summary_true(
                v9,
                "current_body_conformance_v3_closure_basis_preserved",
            )
        ),
        "selected_v9_preserved_what_stands": (
            _statement_or_summary_true(v9, "what_stands_preserved")
            or what_stands.get("what_stands_preserved") is True
        ),
        "selected_v9_preserved_what_does_not_stand": (
            _statement_or_summary_true(v9, "what_does_not_stand_preserved")
            or what_does_not_stand.get("what_does_not_stand_preserved") is True
        ),
        "selected_v9_preserved_what_is_closed": (
            _statement_or_summary_true(v9, "what_is_closed_preserved")
            or what_is_closed.get("what_is_closed_preserved") is True
        ),
        "selected_v9_preserved_what_remains_open": (
            _statement_or_summary_true(v9, "what_remains_open_preserved")
            or what_remains_open.get("what_remains_open_preserved") is True
        ),
        "selected_v9_preserved_orientation_non_meaning": _orientation_non_meaning_preserved(
            v9
        ),
        "selected_v9_preserved_orientation_statement": bool(statement),
        "selected_v9_preserved_orientation_non_claims": v9_non_claims_conform,
        "selected_v9_missing_orientation_non_claims": missing,
        "selected_v9_flipped_orientation_non_claims": flipped,
        "selected_v9_did_not_rely_on_recency_or_majority_shortcut": latest_shortcut_absent,
    }
    section["v9_orientation_conformant"] = all(
        bool(value)
        for key, value in section.items()
        if key
        not in {
            "selected_v9_missing_orientation_non_claims",
            "selected_v9_flipped_orientation_non_claims",
        }
    )
    return section


def _build_basis_preservation_conformance(
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
    v9_orientation: Mapping[str, Any],
) -> dict[str, Any]:
    checks = {
        "v8_as_prior_lineage_preserved": bool(
            v9_orientation.get("selected_v9_preserved_v8_as_lineage")
        ),
        "v9_as_selected_orientation_preserved": bool(v9),
        "current_body_conformance_v3_closure_basis_preserved": bool(
            v9_orientation.get(
                "selected_v9_preserved_current_body_conformance_v3_closure_basis"
            )
        ),
        "distributed_standing_boundary_result_preserved": _basis_item_present(
            request,
            v9,
            (
                "distributed_standing_boundary_reference",
                "distributed_standing_boundary_result_reference",
                "distributed_standing_boundary_result_preserved",
            ),
        ),
        "distributed_standing_boundary_conformance_result_preserved": _basis_item_present(
            request,
            v9,
            (
                "distributed_standing_boundary_conformance_reference",
                "distributed_standing_boundary_conformance_result_preserved",
            ),
        ),
        "distributed_standing_boundary_conformance_closure_result_preserved": bool(
            v9_orientation.get(
                "selected_v9_preserved_distributed_standing_conformance_closure"
            )
        ),
        "divergence_consequence_preserved": _basis_item_present(
            request,
            v9,
            ("divergence_consequence_reference", "divergence_consequence"),
        ),
        "currentness_successor_preserved": _basis_item_present(
            request,
            v9,
            ("currentness_successor_reference", "currentness_successor"),
        ),
        "continuity_turn_v2_preserved": _basis_item_present(
            request,
            v9,
            ("continuity_turn_v2_reference", "continuity_turn_v2"),
        ),
        "standing_propagation_v2_preserved": _basis_item_present(
            request,
            v9,
            ("standing_propagation_v2_reference", "standing_propagation_v2"),
        ),
        "registry_persistence_v2_preserved": _basis_item_present(
            request,
            v9,
            ("registry_persistence_v2_reference", "registry_persistence_v2"),
        ),
        "lifecycle_posture_preserved": _basis_item_present(
            request,
            v9,
            ("lifecycle_reference", "lifecycle_posture", "carrier_c_lifecycle_posture"),
        ),
        "b_c_divergence_preserved": _basis_item_present(
            request,
            v9,
            ("b_c_divergence", "b_c_visible_divergence", "visible_divergence"),
        ),
        "carrier_b_success_preserved": _basis_item_present(
            request,
            v9,
            ("carrier_b_success", "carrier_b_successful_receipt"),
        ),
        "carrier_c_block_preserved": _basis_item_present(
            request,
            v9,
            ("carrier_c_block", "carrier_c_blocked_receipt"),
        ),
        "visible_refusal_preserved_where_exposed": not _recursive_true(
            v9,
            ("visible_refusal_erased", "refusal_erased"),
        ),
        "blocked_attempts_preserved_where_exposed": not _recursive_true(
            v9,
            ("blocked_attempts_erased", "blocked_attempt_erased"),
        ),
        "projection_mismatch_preserved_where_exposed": not _recursive_true(
            v9,
            ("projection_mismatch_erased", "projection_mismatch_hidden"),
        ),
        "relation_conformance_closure_basis_preserved": _basis_item_present(
            request,
            v9,
            (
                "relation_conformance_closure_reference",
                "relation_conformance_closure_basis",
            ),
        ),
        "what_stands_preserved": bool(
            v9_orientation.get("selected_v9_preserved_what_stands")
        ),
        "what_does_not_stand_preserved": bool(
            v9_orientation.get("selected_v9_preserved_what_does_not_stand")
        ),
        "what_is_closed_preserved": bool(
            v9_orientation.get("selected_v9_preserved_what_is_closed")
        ),
        "what_remains_open_preserved": bool(
            v9_orientation.get("selected_v9_preserved_what_remains_open")
        ),
        "all_surfaces_remain_basis_only_not_operation_continuation_or_final_completion": True,
    }
    return {
        **checks,
        "basis_preservation_conformant": all(checks.values()),
    }


def _build_non_claim_conformance(
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
) -> dict[str, Any]:
    declared_conform, declared_missing, declared_flipped = _request_non_claims_conform(request)
    v9_conform, v9_missing, v9_flipped = _selected_v9_non_claims_conform(v9)
    no_mutation = _no_mutation_replay_merge(v9, request)
    section = {
        key: False for key in REQUIRED_NON_CLAIMS
    }
    section.update(
        {
            "declared_non_claims_conformant": declared_conform,
            "declared_missing_required_non_claims": declared_missing,
            "declared_flipped_required_non_claims": declared_flipped,
            "selected_v9_non_claims_conformant": v9_conform,
            "selected_v9_missing_required_non_claims": v9_missing,
            "selected_v9_flipped_required_non_claims": v9_flipped,
            "mutation_replay_or_merge_absent": no_mutation,
            "non_claim_conformant": declared_conform and v9_conform and no_mutation,
        }
    )
    return section


def _build_checks(
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
    v9_section: Mapping[str, Any],
    v9_orientation: Mapping[str, Any],
    basis_conformance: Mapping[str, Any],
    non_claim_conformance: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    intent = request.get("conformance_intent")
    load_failures = v9_section.get("selected_v9_load_failures") or []
    request_non_claims_conform = bool(
        non_claim_conformance.get("declared_non_claims_conformant")
    )

    return [
        _make_check(
            "declared conformance request is well formed",
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED" not in precheck_failures,
            "mapping request",
            "malformed request"
            if "DECLARED_CONFORMANCE_REQUEST_MALFORMED" in precheck_failures
            else "mapping request",
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
        ),
        _make_check(
            "declared conformance request readable",
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE" not in precheck_failures,
            "readable request path or supplied mapping",
            "unreadable request path"
            if "DECLARED_CONFORMANCE_REQUEST_UNREADABLE" in precheck_failures
            else "readable request",
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
        ),
        _make_check(
            "conformance question declared",
            _is_present(request.get("conformance_question")),
            "declared conformance question",
            request.get("conformance_question"),
            "CONFORMANCE_QUESTION_UNDECLARED",
        ),
        _make_check(
            "conformance intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "CONFORMANCE_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "conformance request not explicitly blocked",
            intent != INTENT_BLOCK,
            "not explicit block intent",
            intent,
            "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED",
        ),
        _make_check(
            "selected current self-orientation v9 readable and parseable",
            not load_failures and bool(v9),
            "readable parseable selected v9",
            load_failures or "readable parseable",
            load_failures[0] if load_failures else "CURRENT_SELF_ORIENTATION_V9_MISSING",
        ),
        _make_check(
            "selected current self-orientation v9 present",
            bool(v9_section.get("selected_v9_preserved")),
            "selected current self-orientation v9 present",
            v9_section.get("selected_v9_preserved"),
            "CURRENT_SELF_ORIENTATION_V9_MISSING",
        ),
        _make_check(
            "selected v9 identity present",
            bool(v9_section.get("selected_v9_identity_preserved")),
            "selected v9 identity",
            v9_section.get("selected_current_self_orientation_v9_id"),
            "CURRENT_SELF_ORIENTATION_V9_IDENTITY_MISSING",
        ),
        _make_check(
            "selected v9 outcome present",
            bool(v9_section.get("selected_v9_outcome_preserved")),
            "selected v9 outcome",
            v9_section.get("selected_current_self_orientation_v9_outcome"),
            "CURRENT_SELF_ORIENTATION_V9_OUTCOME_MISSING",
        ),
        _make_check(
            "selected v9 is current self-orientation v9",
            bool(v9_section.get("selected_v9_is_current_self_orientation_v9")),
            "current self-orientation v9 result",
            v9_section.get("selected_v9_is_current_self_orientation_v9"),
            "CURRENT_SELF_ORIENTATION_V9_MALFORMED",
        ),
        _make_check(
            "selected v9 outcome recorded",
            bool(v9_section.get("selected_v9_recorded")),
            EXPECTED_SELECTED_V9_OUTCOME,
            v9_section.get("selected_current_self_orientation_v9_outcome"),
            "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED",
        ),
        _make_check(
            "selected v9 failed check count zero",
            bool(v9_section.get("selected_v9_failed_check_count_zero")),
            EXPECTED_FAILED_CHECK_COUNT,
            v9_section.get("selected_v9_failed_check_count"),
            "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "selected v9 preserves v8 lineage",
            bool(v9_orientation.get("selected_v9_preserved_v8_as_lineage")),
            "v8 lineage preserved",
            v9_orientation.get("selected_v9_preserved_v8_as_lineage"),
            "V8_LINEAGE_MISSING",
        ),
        _make_check(
            "selected v9 preserves distributed standing boundary conformance closure",
            bool(
                v9_orientation.get(
                    "selected_v9_preserved_distributed_standing_conformance_closure"
                )
            ),
            "distributed standing conformance closure preserved",
            v9_orientation.get(
                "selected_v9_preserved_distributed_standing_conformance_closure"
            ),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        ),
        _make_check(
            "selected v9 preserves distributed standing boundary conformance closure closed",
            bool(
                v9_orientation.get(
                    "selected_v9_preserved_distributed_standing_conformance_closure_closed"
                )
            ),
            "distributed standing conformance closure closed",
            v9_orientation.get(
                "selected_v9_preserved_distributed_standing_conformance_closure_closed"
            ),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_NOT_CLOSED",
        ),
        _make_check(
            "selected v9 preserves current-body conformance v3 closure basis",
            bool(
                v9_orientation.get(
                    "selected_v9_preserved_current_body_conformance_v3_closure_basis"
                )
            ),
            "current-body conformance v3 closure basis preserved",
            v9_orientation.get(
                "selected_v9_preserved_current_body_conformance_v3_closure_basis"
            ),
            "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
        ),
        _make_check(
            "selected v9 preserves what stands",
            bool(v9_orientation.get("selected_v9_preserved_what_stands")),
            "what stands preserved",
            v9_orientation.get("selected_v9_preserved_what_stands"),
            "WHAT_STANDS_MISSING",
        ),
        _make_check(
            "selected v9 preserves what does not stand",
            bool(v9_orientation.get("selected_v9_preserved_what_does_not_stand")),
            "what does not stand preserved",
            v9_orientation.get("selected_v9_preserved_what_does_not_stand"),
            "WHAT_DOES_NOT_STAND_MISSING",
        ),
        _make_check(
            "selected v9 preserves what is closed",
            bool(v9_orientation.get("selected_v9_preserved_what_is_closed")),
            "what is closed preserved",
            v9_orientation.get("selected_v9_preserved_what_is_closed"),
            "WHAT_IS_CLOSED_MISSING",
        ),
        _make_check(
            "selected v9 preserves what remains open",
            bool(v9_orientation.get("selected_v9_preserved_what_remains_open")),
            "what remains open preserved",
            v9_orientation.get("selected_v9_preserved_what_remains_open"),
            "WHAT_REMAINS_OPEN_MISSING",
        ),
        _make_check(
            "selected v9 preserves orientation non-claims",
            bool(v9_orientation.get("selected_v9_preserved_orientation_non_claims")),
            "orientation non-claims false",
            {
                "missing": v9_orientation.get("selected_v9_missing_orientation_non_claims"),
                "flipped": v9_orientation.get("selected_v9_flipped_orientation_non_claims"),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _make_check(
            "selected v9 does not authorize continuation",
            request_non_claims_conform and _no_selected_v9_continuation(v9),
            False,
            False if _no_selected_v9_continuation(v9) else True,
            "V9_AUTHORIZES_CONTINUATION",
        ),
        _make_check(
            "selected v9 does not authorize operation",
            request_non_claims_conform and _no_selected_v9_operation(v9),
            False,
            False if _no_selected_v9_operation(v9) else True,
            "V9_AUTHORIZES_OPERATION",
        ),
        _make_check(
            "selected v9 does not authorize repository synchronization",
            request_non_claims_conform and _no_selected_v9_repository_sync(v9),
            False,
            False if _no_selected_v9_repository_sync(v9) else True,
            "V9_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _make_check(
            "selected v9 does not authorize full body transfer",
            request_non_claims_conform and _no_selected_v9_full_body_transfer(v9),
            False,
            False if _no_selected_v9_full_body_transfer(v9) else True,
            "V9_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _make_check(
            "selected v9 does not create second body",
            request_non_claims_conform and _no_selected_v9_second_body(v9),
            False,
            False if _no_selected_v9_second_body(v9) else True,
            "V9_CREATES_SECOND_BODY",
        ),
        _make_check(
            "selected v9 does not create permission",
            request_non_claims_conform and _no_selected_v9_permission(v9),
            False,
            False if _no_selected_v9_permission(v9) else True,
            "V9_CREATES_PERMISSION",
        ),
        _make_check(
            "selected v9 does not create authority",
            request_non_claims_conform and _no_selected_v9_authority(v9),
            False,
            False if _no_selected_v9_authority(v9) else True,
            "V9_CREATES_AUTHORITY",
        ),
        _make_check(
            "selected v9 does not create truth/action",
            request_non_claims_conform and _no_selected_v9_truth_action(v9),
            False,
            False if _no_selected_v9_truth_action(v9) else True,
            "V9_CREATES_TRUTH_OR_ACTION",
        ),
        _make_check(
            "selected v9 does not claim final completion",
            request_non_claims_conform and _no_selected_v9_final_completion(v9),
            False,
            False if _no_selected_v9_final_completion(v9) else True,
            "V9_CLAIMS_FINAL_COMPLETION",
        ),
        _make_check(
            "selected v9 does not schedule follow-on work",
            request_non_claims_conform and _no_selected_v9_follow_on_work(v9),
            False,
            False if _no_selected_v9_follow_on_work(v9) else True,
            "V9_SCHEDULES_FOLLOW_ON_WORK",
        ),
        _make_check(
            "selected v9 does not schedule self-orientation successor beyond v9",
            request_non_claims_conform and _no_selected_v9_self_orientation_successor(v9),
            False,
            False if _no_selected_v9_self_orientation_successor(v9) else True,
            "V9_SCHEDULES_SELF_ORIENTATION_SUCCESSOR",
        ),
        _make_check(
            "selected v9 does not mutate prior result",
            request_non_claims_conform and _no_selected_v9_prior_mutation(v9),
            False,
            False if _no_selected_v9_prior_mutation(v9) else True,
            "V9_MUTATES_PRIOR_RESULT",
        ),
        _make_check(
            "conformance does not authorize continuation",
            request_non_claims_conform and _no_conformance_continuation(request),
            False,
            False if _no_conformance_continuation(request) else True,
            "CONFORMANCE_AUTHORIZES_CONTINUATION",
        ),
        _make_check(
            "conformance does not authorize operation",
            request_non_claims_conform and _no_conformance_operation(request),
            False,
            False if _no_conformance_operation(request) else True,
            "CONFORMANCE_AUTHORIZES_OPERATION",
        ),
        _make_check(
            "conformance does not create permission",
            request_non_claims_conform and _no_conformance_permission(request),
            False,
            False if _no_conformance_permission(request) else True,
            "CONFORMANCE_CREATES_PERMISSION",
        ),
        _make_check(
            "conformance does not claim final completion",
            request_non_claims_conform and _no_conformance_final_completion(request),
            False,
            False if _no_conformance_final_completion(request) else True,
            "CONFORMANCE_CLAIMS_FINAL_COMPLETION",
        ),
        _make_check(
            "conformance does not schedule follow-on work",
            request_non_claims_conform and _no_conformance_follow_on_work(request),
            False,
            False if _no_conformance_follow_on_work(request) else True,
            "CONFORMANCE_CLAIMS_FINAL_COMPLETION",
        ),
        _make_check(
            "conformance does not mutate v9",
            request_non_claims_conform and _no_conformance_mutation(v9, request),
            False,
            False if _no_conformance_mutation(v9, request) else True,
            "V9_MUTATES_PRIOR_RESULT",
        ),
        _make_check(
            "no mutation replay or merge",
            request_non_claims_conform and _no_mutation_replay_merge(v9, request),
            False,
            False if _no_mutation_replay_merge(v9, request) else True,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _make_check(
            "non-claims remain false",
            bool(non_claim_conformance.get("non_claim_conformant")),
            "required non-claims false",
            {
                "declared": request.get("declared_non_claims"),
                "selected_v9_non_claims_conformant": non_claim_conformance.get(
                    "selected_v9_non_claims_conformant"
                ),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _make_check(
            "basis preservation conformant",
            bool(basis_conformance.get("basis_preservation_conformant")),
            "required v4 basis preserved",
            basis_conformance,
            "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
        ),
    ]


def _decide_outcome(
    intent: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> tuple[str, dict[str, Any]]:
    failed_checks = [check for check in checks if not check.get("passed")]
    first_failure_code = next(
        (check.get("failure_code") for check in failed_checks if check.get("failure_code")),
        None,
    )
    first_block_code = next(
        (
            check.get("failure_code")
            for check in failed_checks
            if check.get("failure_code") in BLOCKING_FAILURE_CODES
        ),
        None,
    )

    if intent == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED",
                "block_reason": "Current-body conformance v4 request explicitly declared block intent.",
            },
        )

    if first_block_code:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": first_block_code,
                "block_reason": "Current-body conformance v4 could not lawfully proceed.",
            },
        )

    if failed_checks:
        return (
            OUTCOME_NOT_CONFORMANT,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "first_failure_code": first_failure_code,
                "not_conformant_reason": "Readable selected v9 failed one or more current-body conformance v4 checks.",
            },
        )

    if intent == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_CONFORMANT,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "first_failure_code": "CURRENT_BODY_CONFORMANCE_V4_NOT_REQUESTED",
                "not_recorded_reason": "Request explicitly declined current-body conformance v4 recording.",
            },
        )

    return (
        OUTCOME_CONFORMANT,
        {
            "blocked": False,
            "block_code": None,
            "block_reason": None,
        },
    )


def _build_conformance_statement(
    outcome: str,
    v9_section: Mapping[str, Any],
    v9_orientation: Mapping[str, Any],
    basis_conformance: Mapping[str, Any],
    non_claim_conformance: Mapping[str, Any],
    request: Mapping[str, Any],
    v9: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    conformant = outcome == OUTCOME_CONFORMANT
    failed_checks = [check for check in checks if not check.get("passed")]
    return {
        "current_body_conformance_v4_conformant": conformant,
        "selected_v9_preserved": bool(v9_section.get("selected_v9_preserved")),
        "selected_v9_identity_preserved": bool(
            v9_section.get("selected_v9_identity_preserved")
        ),
        "selected_v9_outcome_preserved": bool(
            v9_section.get("selected_v9_outcome_preserved")
        ),
        "selected_v9_is_current_self_orientation_v9": bool(
            v9_section.get("selected_v9_is_current_self_orientation_v9")
        ),
        "selected_v9_recorded": bool(v9_section.get("selected_v9_recorded")),
        "selected_v9_failed_check_count_zero": bool(
            v9_section.get("selected_v9_failed_check_count_zero")
        ),
        "v9_orientation_conformant": bool(
            v9_orientation.get("v9_orientation_conformant")
        ),
        "basis_preservation_conformant": bool(
            basis_conformance.get("basis_preservation_conformant")
        ),
        "non_claim_conformant": bool(non_claim_conformance.get("non_claim_conformant")),
        "conformance_did_not_mutate_v9": _no_conformance_mutation(v9, request),
        "conformance_did_not_authorize_continuation": _no_conformance_continuation(
            request
        ),
        "conformance_did_not_authorize_operation": _no_conformance_operation(request),
        "conformance_did_not_create_permission": _no_conformance_permission(request),
        "conformance_did_not_claim_final_completion": _no_conformance_final_completion(
            request
        ),
        "conformance_did_not_schedule_follow_on_work": _no_conformance_follow_on_work(
            request
        ),
        "current_self_orientation_v10_created": False,
        "current_body_conformance_v4_closure_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "permission_created": False,
        "authority_created": False,
        "truth_created": False,
        "action_authorized": False,
        "final_completion_claimed": False,
        "public_launch_readiness_created": False,
        "follow_on_work_authorized": False,
        "failed_checks_preserved": _deepcopy(failed_checks),
    }


def build_current_body_conformance_v4_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact bounded summary for a current-body conformance v4 result."""

    checks = result.get("conformance_checks", [])
    checks_list = checks if isinstance(checks, list) else []
    passed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and check.get("passed")
    )
    failed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and not check.get("passed")
    )

    declared = result.get("declared_conformance_question", {})
    selected = result.get("selected_current_self_orientation_v9", {})
    statement = result.get("conformance_statement", {})
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})

    declared_map = declared if isinstance(declared, Mapping) else {}
    selected_map = selected if isinstance(selected, Mapping) else {}
    statement_map = statement if isinstance(statement, Mapping) else {}
    block_map = block if isinstance(block, Mapping) else {}
    non_claim_map = non_claims if isinstance(non_claims, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code"),
        "block_reason": block_map.get("block_reason"),
        "conformance_request_id": declared_map.get("conformance_request_id"),
        "conformance_question": declared_map.get("conformance_question"),
        "conformance_intent": declared_map.get("conformance_intent"),
        "selected_v9_id": selected_map.get("selected_current_self_orientation_v9_id"),
        "selected_v9_outcome": selected_map.get(
            "selected_current_self_orientation_v9_outcome"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "current_body_conformance_v4_conformant": statement_map.get(
            "current_body_conformance_v4_conformant"
        ),
        "selected_v9_preserved": statement_map.get("selected_v9_preserved"),
        "selected_v9_identity_preserved": statement_map.get(
            "selected_v9_identity_preserved"
        ),
        "selected_v9_outcome_preserved": statement_map.get(
            "selected_v9_outcome_preserved"
        ),
        "selected_v9_is_current_self_orientation_v9": statement_map.get(
            "selected_v9_is_current_self_orientation_v9"
        ),
        "selected_v9_recorded": statement_map.get("selected_v9_recorded"),
        "selected_v9_failed_check_count_zero": statement_map.get(
            "selected_v9_failed_check_count_zero"
        ),
        "v9_orientation_conformant": statement_map.get("v9_orientation_conformant"),
        "basis_preservation_conformant": statement_map.get(
            "basis_preservation_conformant"
        ),
        "non_claim_conformant": statement_map.get("non_claim_conformant"),
        "conformance_did_not_mutate_v9": statement_map.get(
            "conformance_did_not_mutate_v9"
        ),
        "conformance_did_not_authorize_continuation": statement_map.get(
            "conformance_did_not_authorize_continuation"
        ),
        "conformance_did_not_authorize_operation": statement_map.get(
            "conformance_did_not_authorize_operation"
        ),
        "conformance_did_not_create_permission": statement_map.get(
            "conformance_did_not_create_permission"
        ),
        "conformance_did_not_claim_final_completion": statement_map.get(
            "conformance_did_not_claim_final_completion"
        ),
        "conformance_did_not_schedule_follow_on_work": statement_map.get(
            "conformance_did_not_schedule_follow_on_work"
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
                "conformance_authorized_continuation",
                "conformance_authorized_operation",
                "conformance_claimed_final_completion",
            )
        },
    }


def _build_result(
    request: Mapping[str, Any],
    request_path: str | None,
    v9: Mapping[str, Any],
    v9_path: str | None,
    v9_load_failures: Sequence[str],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    declared = _declared_conformance_question_section(request, request_path)
    selected_v9 = _selected_v9_section(request, v9, v9_path, v9_load_failures)
    basis = _current_body_conformance_v4_basis_section(request, v9)
    v9_orientation = _build_v9_orientation_conformance(v9)
    basis_conformance = _build_basis_preservation_conformance(
        request,
        v9,
        v9_orientation,
    )
    non_claim_conformance = _build_non_claim_conformance(request, v9)
    checks = _build_checks(
        request,
        v9,
        selected_v9,
        v9_orientation,
        basis_conformance,
        non_claim_conformance,
        precheck_failures,
    )
    outcome, block = _decide_outcome(request.get("conformance_intent"), checks)
    statement = _build_conformance_statement(
        outcome,
        selected_v9,
        v9_orientation,
        basis_conformance,
        non_claim_conformance,
        request,
        v9,
        checks,
    )
    result_id = _first_present(
        request.get("conformance_request_id"),
        selected_v9.get("selected_current_self_orientation_v9_id"),
        "current_body_conformance_v4",
    )

    result = {
        "current_body_conformance_v4_metadata": {
            "current_body_conformance_v4_result_id": (
                f"{result_id}__current_body_conformance_v4"
            ),
            "current_body_conformance_v4_result_type": RESULT_TYPE,
            "current_body_conformance_v4_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_conformance_question": declared,
        "selected_current_self_orientation_v9": selected_v9,
        "current_body_conformance_v4_basis": basis,
        "v9_orientation_conformance": v9_orientation,
        "basis_preservation_conformance": basis_conformance,
        "non_claim_conformance": non_claim_conformance,
        "conformance_checks": checks,
        "conformance_statement": statement,
        "conformance_non_meaning": _deepcopy(CONFORMANCE_NON_MEANING),
        "what_remains_open": _deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": _result_non_claims(request),
        "outcome": outcome,
        "block": block,
    }
    result["current_body_conformance_v4_summary"] = (
        build_current_body_conformance_v4_summary(result)
    )
    return result


def resolve_current_body_conformance_v4(
    declared_conformance_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded current-body conformance v4 request."""

    if declared_conformance_request is None:
        request: dict[str, Any] = {}
        precheck_failures: list[str] = []
    elif not isinstance(declared_conformance_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_CONFORMANCE_REQUEST_MALFORMED"]
    else:
        request = _deepcopy(dict(declared_conformance_request))
        precheck_failures = []

    v9, v9_path, v9_load_failures = _load_selected_v9(request)
    return _build_result(
        request,
        None,
        v9,
        v9_path,
        v9_load_failures,
        precheck_failures,
    )


def resolve_current_body_conformance_v4_from_path(
    declared_conformance_request_path: Path | str,
) -> dict:
    """Load a JSON object conformance request from path and resolve v4."""

    path = _to_path(declared_conformance_request_path)
    try:
        request = _read_json_object(
            path,
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
        )
        precheck_failures: list[str] = []
    except CurrentBodyConformanceV4Error as exc:
        request = {}
        precheck_failures = [exc.block_code]

    v9, v9_path, v9_load_failures = _load_selected_v9(request)
    return _build_result(
        request,
        str(path),
        v9,
        v9_path,
        v9_load_failures,
        precheck_failures,
    )


def write_current_body_conformance_v4_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-body conformance v4 result as stable JSON."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformanceV4Error(
            "Current-body conformance v4 result must be a mapping.",
            "CURRENT_BODY_CONFORMANCE_V4_RESULT_MALFORMED",
        )

    result_copy = _deepcopy(dict(result))
    if output_path is None:
        summary = result_copy.get("current_body_conformance_v4_summary", {})
        request_id = (
            summary.get("conformance_request_id") if isinstance(summary, Mapping) else None
        )
        selected_v9_id = (
            summary.get("selected_v9_id") if isinstance(summary, Mapping) else None
        )
        filename_root = _safe_filename_part(
            request_id or selected_v9_id or "current_body_conformance_v4"
        )
        output = (
            CURRENT_BODY_CONFORMANCE_V4_ROOT
            / f"{filename_root}__current_body_conformance_v4_result.json"
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


def build_declared_current_body_conformance_v4_request(
    conformance_request_id: str,
    conformance_question: str,
    selected_current_self_orientation_v9: Mapping[str, Any] | str,
    current_body_conformance_v4_basis: Mapping[str, Any] | str,
    conformance_intent: str = INTENT_RECORD,
    *,
    selected_current_self_orientation_v9_path: str | None = None,
    selected_current_self_orientation_v9_id: str | None = None,
    selected_current_self_orientation_v9_outcome: str | None = None,
    expected_selected_v9_outcome: str = EXPECTED_SELECTED_V9_OUTCOME,
) -> dict:
    """Build a bounded declared v4 conformance request with false non-claims."""

    request = {
        "conformance_request_id": conformance_request_id,
        "conformance_question": conformance_question,
        "conformance_intent": conformance_intent,
        "selected_current_self_orientation_v9": _deepcopy(
            selected_current_self_orientation_v9
        ),
        "current_body_conformance_v4_basis": _deepcopy(
            current_body_conformance_v4_basis
        ),
        "expected_selected_v9_outcome": expected_selected_v9_outcome,
        "expected_failed_check_count": EXPECTED_FAILED_CHECK_COUNT,
        "declared_non_claims": _deepcopy(REQUIRED_NON_CLAIMS),
    }

    if selected_current_self_orientation_v9_path is not None:
        request["selected_current_self_orientation_v9_path"] = (
            selected_current_self_orientation_v9_path
        )
    if selected_current_self_orientation_v9_id is not None:
        request["selected_current_self_orientation_v9_id"] = (
            selected_current_self_orientation_v9_id
        )
    if selected_current_self_orientation_v9_outcome is not None:
        request["selected_current_self_orientation_v9_outcome"] = (
            selected_current_self_orientation_v9_outcome
        )

    return request
