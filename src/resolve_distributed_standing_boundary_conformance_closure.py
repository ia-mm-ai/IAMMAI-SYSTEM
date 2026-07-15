"""Bounded distributed standing boundary conformance closure resolver.

This resolver closes the meaning of one selected distributed standing boundary
conformance result. It records closure of meaning only. It does not re-run
conformance, expand conformance, mutate the selected conformance result, mutate
the selected distributed standing boundary result, authorize continuation,
authorize repository synchronization, authorize full body transfer, create a
second body, authorize distributed operation, create truth or action, claim
final completion, or schedule a self-orientation successor.

The module is self-contained and imports no repository-local modules.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class DistributedStandingBoundaryConformanceClosureError(Exception):
    """Hard failure for malformed or unreadable explicit closure inputs."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_standing_boundary_conformance_closure"
)

RESOLVER_MODULE = "resolve_distributed_standing_boundary_conformance_closure"
RESULT_TYPE = "distributed_standing_boundary_conformance_closure_result"
RESULT_VERSION = "0.1.0"

OUTCOME_CLOSED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED"
OUTCOME_NOT_CLOSED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_NOT_CLOSED"
OUTCOME_BLOCKED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE_BLOCKED"

SUPPORTED_OUTCOMES = {
    OUTCOME_CLOSED,
    OUTCOME_NOT_CLOSED,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE"

SUPPORTED_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

EXPECTED_SELECTED_CONFORMANCE_OUTCOME = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT"
EXPECTED_FAILED_CHECK_COUNT = 0

BLOCKING_FAILURE_CODES = {
    "DECLARED_CLOSURE_REQUEST_MALFORMED",
    "DECLARED_CLOSURE_REQUEST_UNREADABLE",
    "CLOSURE_QUESTION_UNDECLARED",
    "CLOSURE_INTENT_UNSUPPORTED",
    "CLOSURE_REQUEST_EXPLICITLY_BLOCKED",
    "SELECTED_CONFORMANCE_RESULT_MISSING",
    "SELECTED_CONFORMANCE_RESULT_UNREADABLE",
    "SELECTED_CONFORMANCE_RESULT_MALFORMED",
    "SELECTED_CONFORMANCE_RESULT_IDENTITY_MISSING",
    "SELECTED_CONFORMANCE_RESULT_OUTCOME_MISSING",
    "SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE",
}

REQUIRED_NON_CLAIMS = {
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
    "evidence_erased": False,
    "selected_conformance_result_mutated": False,
    "selected_distributed_standing_result_mutated": False,
    "closure_expanded_conformance": False,
    "closure_created_permission": False,
    "closure_authorized_operation": False,
    "closure_claimed_final_completion": False,
    "self_orientation_successor_scheduled": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

SELECTED_CONFORMANCE_FALSE_ALIASES = {
    "authority_created": ("authority_created",),
    "permission_created": ("permission_created",),
    "currentness_created": ("currentness_created",),
    "carrier_currentness_created": ("carrier_currentness_created",),
    "source_replaced": ("source_replaced",),
    "current_carrier_selected": ("current_carrier_selected",),
    "winning_carrier_selected": ("winning_carrier_selected",),
    "losing_carrier_invalidated": ("losing_carrier_invalidated",),
    "divergence_resolved": ("divergence_resolved",),
    "truth_created": ("truth_created",),
    "action_authorized": ("action_authorized",),
    "repository_synchronization_authorized": (
        "repository_synchronization_authorized",
        "conformance_authorized_repository_sync",
    ),
    "full_body_transfer_authorized": (
        "full_body_transfer_authorized",
        "conformance_authorized_full_body_transfer",
    ),
    "second_body_created": ("second_body_created", "conformance_created_second_body"),
    "continuation_authorized": (
        "continuation_authorized",
        "conformance_authorized_continuation",
    ),
    "distributed_operation_authorized": (
        "distributed_operation_authorized",
        "conformance_authorized_distributed_operation",
    ),
    "evidence_erased": ("evidence_erased",),
    "selected_distributed_standing_result_mutated": (
        "selected_result_mutated",
        "selected_distributed_standing_result_mutated",
    ),
    "mutation_performed": ("mutation_performed",),
    "replay_performed": ("replay_performed",),
    "merge_performed": ("merge_performed",),
}

CONFORMANCE_NON_MEANING = {
    "permission": True,
    "continuation": True,
    "operation": True,
    "distributed_operation": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body_creation": True,
    "second_body": True,
    "implementation": True,
    "final_completion": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "self_orientation_successor_by_default": True,
    "closure_by_default": True,
    "conformance_is_not_permission": True,
    "conformance_is_not_continuation": True,
    "conformance_is_not_operation": True,
    "conformance_is_not_synchronization": True,
    "conformance_is_not_full_body_transfer": True,
    "conformance_is_not_second_body_creation": True,
    "conformance_is_not_implementation": True,
    "conformance_is_not_final_completion": True,
    "conformance_is_not_self_orientation_successor_by_default": True,
    "conformance_is_not_closure_by_default": True,
}

CLOSURE_NON_MEANING = {
    "distributed_operation": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body": True,
    "continuation": True,
    "implementation": True,
    "final_completion": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "final_system_identity": True,
    "currentness": True,
    "carrier_currentness": True,
    "current_carrier_selected": True,
    "winning_carrier_selected": True,
    "losing_carrier_invalidated": True,
    "source_replacement": True,
    "authority": True,
    "permission": True,
    "truth": True,
    "action": True,
    "consequence_action_law": True,
    "divergence_resolution": True,
    "evidence_erasure": True,
    "refusal_erasure": True,
    "blocked_attempt_erasure": True,
    "projection_mismatch_erasure": True,
    "selected_conformance_result_mutation": True,
    "selected_distributed_standing_boundary_result_mutation": True,
    "implementation_readiness": True,
    "public_launch_readiness": True,
    "self_orientation_successor_by_default": True,
    "follow_on_work_authorization": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_continuation": True,
    "does_not_mean_implementation": True,
    "does_not_mean_final_completion": True,
    "does_not_mean_final_governance": True,
    "does_not_mean_final_continuity_completion": True,
    "does_not_mean_final_system_identity": True,
    "does_not_mean_currentness": True,
    "does_not_mean_carrier_currentness": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_source_replacement": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_divergence_resolution": True,
    "does_not_mean_evidence_erasure": True,
    "does_not_mean_self_orientation_successor_by_default": True,
}

WHAT_REMAINS_OPEN = {
    "any_self_orientation_successor": "open_not_scheduled_not_authorized_not_executed",
    "distributed_standing_implementation": "open_not_scheduled_not_authorized_not_executed",
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
    "distributed_operation": "open_not_scheduled_not_authorized_not_executed",
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
        raise DistributedStandingBoundaryConformanceClosureError(
            f"Unable to read JSON object from {path}: {exc}",
            unreadable_code,
        ) from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DistributedStandingBoundaryConformanceClosureError(
            f"Malformed JSON object at {path}: {exc}",
            malformed_code,
        ) from exc

    if not isinstance(parsed, Mapping):
        raise DistributedStandingBoundaryConformanceClosureError(
            f"JSON content at {path} is not an object.",
            malformed_code,
        )

    return _deepcopy(dict(parsed))


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(
        value,
        (str, bytes, bytearray),
    ):
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


def _recursive_false(value: Any, keys: Sequence[str]) -> bool:
    if isinstance(value, Mapping):
        for key in keys:
            if value.get(key) is False:
                return True
        return any(_recursive_false(child, keys) for child in value.values())
    if isinstance(value, list):
        return any(_recursive_false(child, keys) for child in value)
    return False


def _recursive_flag_true(value: Any, keys: Sequence[str]) -> bool:
    return _recursive_find(value, keys) is True


def _recursive_flag_false(value: Any, keys: Sequence[str]) -> bool:
    return _recursive_find(value, keys) is False


def _selected_false_preserved(value: Any, key: str) -> bool:
    aliases = SELECTED_CONFORMANCE_FALSE_ALIASES.get(key, (key,))
    return not _recursive_true(value, aliases) and _recursive_false(value, aliases)


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


def _safe_filename_part(value: Any) -> str:
    text = str(value or "distributed_standing_boundary_conformance_closure").strip()
    cleaned = []
    for character in text:
        if character.isalnum() or character in ("-", "_"):
            cleaned.append(character)
        else:
            cleaned.append("_")
    filename = "".join(cleaned).strip("_").lower()
    return filename or "distributed_standing_boundary_conformance_closure"


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


def _selected_conformance_path_value(request: Mapping[str, Any]) -> str | None:
    path = request.get("selected_conformance_result_path")
    if _is_present(path):
        return str(path)
    selected = request.get("selected_conformance_result")
    if isinstance(selected, str) and selected.strip():
        return selected
    return None


def _load_selected_conformance_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any], str | None, list[str]]:
    path_value = _selected_conformance_path_value(request)
    if path_value:
        path = _to_path(path_value)
        try:
            return (
                _read_json_object(
                    path,
                    "SELECTED_CONFORMANCE_RESULT_UNREADABLE",
                    "SELECTED_CONFORMANCE_RESULT_MALFORMED",
                ),
                str(path),
                [],
            )
        except DistributedStandingBoundaryConformanceClosureError as exc:
            return {}, str(path), [exc.block_code]

    selected = request.get("selected_conformance_result")
    if isinstance(selected, Mapping):
        return _deepcopy(dict(selected)), None, []

    if selected is None:
        return {}, None, ["SELECTED_CONFORMANCE_RESULT_MISSING"]

    return {}, None, ["SELECTED_CONFORMANCE_RESULT_MALFORMED"]


def _extract_selected_conformance_result_id(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
) -> str | None:
    metadata = selected.get("distributed_standing_boundary_conformance_metadata")
    summary = selected.get("distributed_standing_boundary_conformance_summary")
    declared = selected.get("declared_conformance_question")
    return _first_present(
        request.get("selected_conformance_result_id"),
        _recursive_find(metadata, ("conformance_result_id", "result_id"))
        if isinstance(metadata, Mapping)
        else None,
        _recursive_find(summary, ("conformance_result_id", "conformance_request_id", "result_id"))
        if isinstance(summary, Mapping)
        else None,
        _recursive_find(declared, ("conformance_request_id", "request_id"))
        if isinstance(declared, Mapping)
        else None,
        selected.get("conformance_result_id"),
        selected.get("result_id"),
    )


def _extract_selected_conformance_result_outcome(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
) -> str | None:
    summary = selected.get("distributed_standing_boundary_conformance_summary")
    return _first_present(
        request.get("selected_conformance_result_outcome"),
        selected.get("outcome"),
        _recursive_find(summary, ("outcome",)) if isinstance(summary, Mapping) else None,
    )


def _selected_conformance_failed_check_count(selected: Mapping[str, Any]) -> int | None:
    summary = selected.get("distributed_standing_boundary_conformance_summary")
    if isinstance(summary, Mapping) and isinstance(summary.get("failed_check_count"), int):
        return int(summary["failed_check_count"])
    checks = selected.get("conformance_checks")
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return None


def _is_distributed_standing_boundary_conformance_result(selected: Mapping[str, Any]) -> bool:
    metadata = selected.get("distributed_standing_boundary_conformance_metadata")
    result_type = (
        _recursive_find(metadata, ("conformance_result_type", "result_type"))
        if isinstance(metadata, Mapping)
        else None
    )
    resolver_module = (
        _recursive_find(metadata, ("resolver_module",)) if isinstance(metadata, Mapping) else None
    )
    return (
        result_type == "distributed_standing_boundary_conformance_result"
        or resolver_module == "resolve_distributed_standing_boundary_conformance"
        or {
            "conformance_checks",
            "conformance_statement",
            "distributed_standing_boundary_conformance_summary",
        }.issubset(set(selected.keys()))
    )


def _build_selected_conformance_result_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    selected_path: str | None,
    load_failures: Sequence[str],
) -> dict[str, Any]:
    result_id = _extract_selected_conformance_result_id(selected, request)
    outcome = _extract_selected_conformance_result_outcome(selected, request)
    expected_outcome = _first_present(
        request.get("expected_selected_conformance_result_outcome"),
        EXPECTED_SELECTED_CONFORMANCE_OUTCOME,
    )
    expected_failed_count = _first_present(
        request.get("expected_failed_check_count"),
        EXPECTED_FAILED_CHECK_COUNT,
    )
    failed_count = _selected_conformance_failed_check_count(selected)
    return {
        "selected_conformance_result_id": result_id,
        "selected_conformance_result_path": selected_path,
        "selected_conformance_result_outcome": outcome,
        "expected_selected_conformance_result_outcome": expected_outcome,
        "selected_conformance_result_failed_check_count": failed_count,
        "expected_failed_check_count": expected_failed_count,
        "selected_conformance_result_preserved": bool(selected),
        "selected_conformance_result_identity_preserved": _is_present(result_id),
        "selected_conformance_result_outcome_preserved": _is_present(outcome),
        "selected_conformance_result_readable_or_supplied": bool(selected) and not load_failures,
        "selected_conformance_result_parseable": bool(selected) and not load_failures,
        "selected_conformance_result_is_conformance_result": (
            bool(selected) and _is_distributed_standing_boundary_conformance_result(selected)
        ),
        "selected_conformance_result_is_conformant": outcome == expected_outcome,
        "selected_conformance_result_failed_check_count_zero": failed_count == expected_failed_count,
        "selected_conformance_result_load_failures": list(load_failures),
        "raw_selected_conformance_result": _deepcopy(dict(selected))
        if isinstance(selected, Mapping)
        else {},
    }


def _build_selected_conformance_result_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_conformance_result_basis")
    return {
        "selected_conformance_result_basis_declared": _is_present(basis),
        "selected_conformance_result_basis": _deepcopy(basis),
        "closure_scope": _deepcopy(request.get("closure_scope")),
        "closure_basis": _deepcopy(request.get("closure_basis")),
        "closure_non_meaning_basis": _deepcopy(request.get("closure_non_meaning_basis")),
        "not_closed_reason": request.get("not_closed_reason"),
        "block_reason": request.get("block_reason"),
        "basis_does_not_authorize_continuation": True,
        "basis_does_not_authorize_repository_sync": True,
        "basis_does_not_authorize_full_body_transfer": True,
        "basis_does_not_create_second_body": True,
        "basis_does_not_authorize_distributed_operation": True,
        "basis_does_not_schedule_self_orientation_successor": True,
    }


def _declared_closure_question_section(
    request: Mapping[str, Any],
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "closure_request_id": request.get("closure_request_id"),
        "closure_question": request.get("closure_question"),
        "closure_intent": request.get("closure_intent"),
        "closure_request_path": request_path,
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "closure_is_not_permission": True,
        "closure_is_not_continuation": True,
        "closure_is_not_operation": True,
        "closure_is_not_synchronization": True,
        "closure_is_not_full_body_transfer": True,
        "closure_is_not_second_body_creation": True,
        "closure_is_not_implementation": True,
        "closure_is_not_final_completion": True,
        "closure_is_not_self_orientation_successor_by_default": True,
    }


def _statement(selected: Mapping[str, Any]) -> Mapping[str, Any]:
    statement = selected.get("conformance_statement")
    return statement if isinstance(statement, Mapping) else {}


def _summary(selected: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = selected.get("distributed_standing_boundary_conformance_summary")
    return summary if isinstance(summary, Mapping) else {}


def _section(selected: Mapping[str, Any], section_name: str) -> Mapping[str, Any]:
    section = selected.get(section_name)
    return section if isinstance(section, Mapping) else {}


def _true_in_statement_or_section(
    selected: Mapping[str, Any],
    statement_key: str,
    section_name: str,
    section_key: str,
) -> bool:
    return (
        _statement(selected).get(statement_key) is True
        or _section(selected, section_name).get(section_key) is True
        or _summary(selected).get(statement_key) is True
    )


def _build_conformance_meaning(selected: Mapping[str, Any]) -> dict[str, Any]:
    selected_section = _section(selected, "selected_distributed_standing_boundary_result")
    section = {
        "selected_distributed_standing_boundary_result_preserved": _true_in_statement_or_section(
            selected,
            "selected_result_preserved",
            "selected_distributed_standing_boundary_result",
            "selected_result_preserved",
        ),
        "selected_distributed_standing_boundary_result_identity_preserved": _true_in_statement_or_section(
            selected,
            "selected_result_identity_preserved",
            "selected_distributed_standing_boundary_result",
            "selected_result_identity_preserved",
        )
        and _is_present(selected_section.get("selected_result_id")),
        "selected_distributed_standing_boundary_result_outcome_preserved": _true_in_statement_or_section(
            selected,
            "selected_result_outcome_preserved",
            "selected_distributed_standing_boundary_result",
            "selected_result_outcome_preserved",
        )
        and _is_present(selected_section.get("selected_result_outcome")),
        "selected_distributed_standing_boundary_result_is_distributed_standing_boundary": _true_in_statement_or_section(
            selected,
            "selected_result_is_distributed_standing_boundary",
            "selected_distributed_standing_boundary_result",
            "selected_result_is_distributed_standing_boundary",
        ),
        "prerequisite_basis_conformant": _true_in_statement_or_section(
            selected,
            "prerequisite_basis_conformant",
            "prerequisite_basis_conformance",
            "prerequisite_basis_conformant",
        ),
        "refusal_divergence_lineage_conformant": _true_in_statement_or_section(
            selected,
            "refusal_divergence_lineage_conformant",
            "refusal_divergence_lineage_conformance",
            "refusal_divergence_lineage_conformant",
        ),
        "non_claim_conformant": _true_in_statement_or_section(
            selected,
            "non_claim_conformant",
            "non_claim_conformance",
            "non_claim_conformant",
        ),
        "summary_detail_correspondence_passed": _true_in_statement_or_section(
            selected,
            "summary_detail_correspondence_passed",
            "summary_detail_correspondence",
            "summary_detail_correspondence_passed",
        ),
        "conformance_can_be_relied_on_as_conformance_not_permission": True,
        "conformance_may_be_preserved_as_closed_meaning_only": True,
    }
    section["conformance_meaning_preserved"] = all(section.values())
    return section


def _build_closure_non_expansion(selected: Mapping[str, Any], request: Mapping[str, Any]) -> dict[str, Any]:
    statement = _statement(selected)
    section = {
        "conformance_did_not_expand_result": statement.get("conformance_did_not_expand_result") is True
        or _summary(selected).get("conformance_did_not_expand_result") is True,
        "conformance_did_not_authorize_continuation": statement.get(
            "conformance_did_not_authorize_continuation"
        )
        is True
        or _summary(selected).get("conformance_did_not_authorize_continuation") is True,
        "conformance_did_not_authorize_repository_sync": statement.get(
            "conformance_did_not_authorize_repository_sync"
        )
        is True
        or _summary(selected).get("conformance_did_not_authorize_repository_sync") is True,
        "conformance_did_not_authorize_full_body_transfer": statement.get(
            "conformance_did_not_authorize_full_body_transfer"
        )
        is True
        or _summary(selected).get("conformance_did_not_authorize_full_body_transfer") is True,
        "conformance_did_not_create_second_body": statement.get(
            "conformance_did_not_create_second_body"
        )
        is True
        or _summary(selected).get("conformance_did_not_create_second_body") is True,
        "conformance_did_not_authorize_distributed_operation": statement.get(
            "conformance_did_not_authorize_distributed_operation"
        )
        is True
        or _summary(selected).get("conformance_did_not_authorize_distributed_operation") is True,
        "closure_does_not_create_new_expansion": not _recursive_true(
            request,
            ("closure_expanded_conformance", "closure_authorized_expansion"),
        ),
        "closure_does_not_mutate_selected_conformance_result": not _recursive_true(
            request,
            ("selected_conformance_result_mutated", "closure_mutates_selected_conformance_result"),
        ),
        "closure_does_not_mutate_selected_distributed_standing_result": not _recursive_true(
            request,
            (
                "selected_distributed_standing_result_mutated",
                "closure_mutates_selected_distributed_standing_result",
            ),
        ),
    }
    section["closure_non_expansion_preserved"] = all(section.values())
    return section


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


def _build_closure_non_meaning_preservation(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    request_non_claims_conform, _, _ = _request_non_claims_conform(request)
    section = {
        "closure_does_not_create_permission": request_non_claims_conform
        and not _recursive_true(request, ("closure_created_permission", "permission_created")),
        "closure_does_not_authorize_continuation": request_non_claims_conform
        and not _recursive_true(request, ("continuation_authorized", "closure_authorizes_continuation")),
        "closure_does_not_authorize_operation": request_non_claims_conform
        and not _recursive_true(
            request,
            ("closure_authorized_operation", "distributed_operation_authorized"),
        ),
        "closure_does_not_authorize_synchronization": request_non_claims_conform
        and not _recursive_true(request, ("repository_synchronization_authorized",)),
        "closure_does_not_authorize_full_body_transfer": request_non_claims_conform
        and not _recursive_true(request, ("full_body_transfer_authorized",)),
        "closure_does_not_create_second_body": request_non_claims_conform
        and not _recursive_true(request, ("second_body_created",)),
        "closure_does_not_create_carrier_currentness": request_non_claims_conform
        and not _recursive_true(request, ("carrier_currentness_created",)),
        "closure_does_not_select_current_carrier": request_non_claims_conform
        and not _recursive_true(request, ("current_carrier_selected",)),
        "closure_does_not_select_winning_carrier": request_non_claims_conform
        and not _recursive_true(request, ("winning_carrier_selected",)),
        "closure_does_not_invalidate_losing_carrier": request_non_claims_conform
        and not _recursive_true(request, ("losing_carrier_invalidated",)),
        "closure_does_not_replace_source": request_non_claims_conform
        and not _recursive_true(request, ("source_replaced",)),
        "closure_does_not_create_authority": request_non_claims_conform
        and not _recursive_true(request, ("authority_created",)),
        "closure_does_not_create_truth_or_action": request_non_claims_conform
        and not _recursive_true(request, ("truth_created", "action_authorized")),
        "closure_does_not_resolve_divergence": request_non_claims_conform
        and not _recursive_true(request, ("divergence_resolved",)),
        "closure_does_not_erase_evidence": request_non_claims_conform
        and not _recursive_true(request, ("evidence_erased",)),
        "closure_does_not_complete_final_governance": request_non_claims_conform
        and not _recursive_true(request, ("final_governance_completed",)),
        "closure_does_not_complete_final_continuity": request_non_claims_conform
        and not _recursive_true(request, ("final_continuity_completed",)),
        "closure_does_not_complete_final_system_identity": request_non_claims_conform
        and not _recursive_true(request, ("final_system_identity_completed",)),
        "closure_does_not_schedule_self_orientation_successor": request_non_claims_conform
        and not _recursive_true(request, ("self_orientation_successor_scheduled",)),
        "no_mutation_replay_or_merge": request_non_claims_conform
        and not _recursive_true(request, ("mutation_performed", "replay_performed", "merge_performed"))
        and _selected_false_preserved(selected, "mutation_performed")
        and _selected_false_preserved(selected, "replay_performed")
        and _selected_false_preserved(selected, "merge_performed"),
    }
    section["closure_non_meaning_preserved"] = all(section.values())
    return section


def _build_closure_checks(
    request: Mapping[str, Any],
    selected_section: Mapping[str, Any],
    basis_section: Mapping[str, Any],
    conformance_meaning: Mapping[str, Any],
    non_expansion: Mapping[str, Any],
    non_meaning: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    intent = request.get("closure_intent")
    request_non_claims_conform, _, _ = _request_non_claims_conform(request)
    load_failures = selected_section.get("selected_conformance_result_load_failures") or []

    checks = [
        _make_check(
            "declared closure request is well formed",
            "DECLARED_CLOSURE_REQUEST_MALFORMED" not in precheck_failures,
            "mapping request",
            "malformed request"
            if "DECLARED_CLOSURE_REQUEST_MALFORMED" in precheck_failures
            else "mapping request",
            "DECLARED_CLOSURE_REQUEST_MALFORMED",
        ),
        _make_check(
            "declared closure request readable",
            "DECLARED_CLOSURE_REQUEST_UNREADABLE" not in precheck_failures,
            "readable request path or supplied mapping",
            "unreadable request path"
            if "DECLARED_CLOSURE_REQUEST_UNREADABLE" in precheck_failures
            else "readable request",
            "DECLARED_CLOSURE_REQUEST_UNREADABLE",
        ),
        _make_check(
            "closure question declared",
            _is_present(request.get("closure_question")),
            "declared closure question",
            request.get("closure_question"),
            "CLOSURE_QUESTION_UNDECLARED",
        ),
        _make_check(
            "closure intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "CLOSURE_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "closure request not explicitly blocked",
            intent != INTENT_BLOCK,
            "not explicit block intent",
            intent,
            "CLOSURE_REQUEST_EXPLICITLY_BLOCKED",
        ),
        _make_check(
            "selected conformance result basis declared",
            bool(basis_section.get("selected_conformance_result_basis_declared")),
            "selected conformance result basis declared",
            basis_section.get("selected_conformance_result_basis_declared"),
            "SELECTED_CONFORMANCE_RESULT_MISSING",
        ),
        _make_check(
            "selected conformance result identity present",
            bool(selected_section.get("selected_conformance_result_identity_preserved")),
            "selected conformance result identity present",
            selected_section.get("selected_conformance_result_id"),
            "SELECTED_CONFORMANCE_RESULT_IDENTITY_MISSING",
        ),
        _make_check(
            "selected conformance result outcome present",
            bool(selected_section.get("selected_conformance_result_outcome_preserved")),
            "selected conformance result outcome present",
            selected_section.get("selected_conformance_result_outcome"),
            "SELECTED_CONFORMANCE_RESULT_OUTCOME_MISSING",
        ),
        _make_check(
            "selected conformance result readable and parseable",
            bool(selected_section.get("selected_conformance_result_readable_or_supplied"))
            and bool(selected_section.get("selected_conformance_result_parseable")),
            "readable parseable selected conformance result",
            load_failures or "readable parseable",
            load_failures[0] if load_failures else "SELECTED_CONFORMANCE_RESULT_MISSING",
        ),
        _make_check(
            "selected conformance result is distributed standing boundary conformance result",
            bool(selected_section.get("selected_conformance_result_is_conformance_result")),
            "distributed standing boundary conformance result",
            selected_section.get("selected_conformance_result_is_conformance_result"),
            "SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE",
        ),
        _make_check(
            "selected conformance result outcome is conformant",
            bool(selected_section.get("selected_conformance_result_is_conformant")),
            selected_section.get("expected_selected_conformance_result_outcome"),
            selected_section.get("selected_conformance_result_outcome"),
            "SELECTED_CONFORMANCE_RESULT_NOT_CONFORMANT",
        ),
        _make_check(
            "selected conformance result failed check count is zero",
            bool(selected_section.get("selected_conformance_result_failed_check_count_zero")),
            selected_section.get("expected_failed_check_count"),
            selected_section.get("selected_conformance_result_failed_check_count"),
            "SELECTED_CONFORMANCE_RESULT_HAS_FAILED_CHECKS",
        ),
        _make_check(
            "selected distributed standing boundary result preserved",
            bool(conformance_meaning.get("selected_distributed_standing_boundary_result_preserved")),
            True,
            conformance_meaning.get("selected_distributed_standing_boundary_result_preserved"),
            "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "selected distributed standing boundary result identity preserved",
            bool(
                conformance_meaning.get(
                    "selected_distributed_standing_boundary_result_identity_preserved"
                )
            ),
            True,
            conformance_meaning.get(
                "selected_distributed_standing_boundary_result_identity_preserved"
            ),
            "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "selected distributed standing boundary result outcome preserved",
            bool(
                conformance_meaning.get(
                    "selected_distributed_standing_boundary_result_outcome_preserved"
                )
            ),
            True,
            conformance_meaning.get(
                "selected_distributed_standing_boundary_result_outcome_preserved"
            ),
            "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "selected distributed standing boundary result is distributed standing boundary",
            bool(
                conformance_meaning.get(
                    "selected_distributed_standing_boundary_result_is_distributed_standing_boundary"
                )
            ),
            True,
            conformance_meaning.get(
                "selected_distributed_standing_boundary_result_is_distributed_standing_boundary"
            ),
            "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "prerequisite basis conformant",
            bool(conformance_meaning.get("prerequisite_basis_conformant")),
            True,
            conformance_meaning.get("prerequisite_basis_conformant"),
            "PREREQUISITE_BASIS_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "refusal divergence lineage conformant",
            bool(conformance_meaning.get("refusal_divergence_lineage_conformant")),
            True,
            conformance_meaning.get("refusal_divergence_lineage_conformant"),
            "REFUSAL_DIVERGENCE_LINEAGE_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "non claim conformant",
            bool(conformance_meaning.get("non_claim_conformant")),
            True,
            conformance_meaning.get("non_claim_conformant"),
            "NON_CLAIM_CONFORMANCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "summary detail correspondence passed",
            bool(conformance_meaning.get("summary_detail_correspondence_passed")),
            True,
            conformance_meaning.get("summary_detail_correspondence_passed"),
            "SUMMARY_DETAIL_CORRESPONDENCE_MISSING_OR_FALSE",
        ),
        _make_check(
            "conformance did not expand result",
            bool(non_expansion.get("conformance_did_not_expand_result")),
            True,
            non_expansion.get("conformance_did_not_expand_result"),
            "CONFORMANCE_EXPANDED_RESULT",
        ),
        _make_check(
            "conformance did not authorize continuation",
            bool(non_expansion.get("conformance_did_not_authorize_continuation")),
            True,
            non_expansion.get("conformance_did_not_authorize_continuation"),
            "CONFORMANCE_AUTHORIZED_CONTINUATION",
        ),
        _make_check(
            "conformance did not authorize repository sync",
            bool(non_expansion.get("conformance_did_not_authorize_repository_sync")),
            True,
            non_expansion.get("conformance_did_not_authorize_repository_sync"),
            "CONFORMANCE_AUTHORIZED_REPOSITORY_SYNC",
        ),
        _make_check(
            "conformance did not authorize full body transfer",
            bool(non_expansion.get("conformance_did_not_authorize_full_body_transfer")),
            True,
            non_expansion.get("conformance_did_not_authorize_full_body_transfer"),
            "CONFORMANCE_AUTHORIZED_FULL_BODY_TRANSFER",
        ),
        _make_check(
            "conformance did not create second body",
            bool(non_expansion.get("conformance_did_not_create_second_body")),
            True,
            non_expansion.get("conformance_did_not_create_second_body"),
            "CONFORMANCE_CREATED_SECOND_BODY",
        ),
        _make_check(
            "conformance did not authorize distributed operation",
            bool(non_expansion.get("conformance_did_not_authorize_distributed_operation")),
            True,
            non_expansion.get("conformance_did_not_authorize_distributed_operation"),
            "CONFORMANCE_AUTHORIZED_DISTRIBUTED_OPERATION",
        ),
        _make_check(
            "closure does not create new expansion",
            bool(non_expansion.get("closure_does_not_create_new_expansion")),
            False,
            False if non_expansion.get("closure_does_not_create_new_expansion") else True,
            "CONFORMANCE_EXPANDED_RESULT",
        ),
        _make_check(
            "closure does not mutate selected conformance result",
            bool(non_expansion.get("closure_does_not_mutate_selected_conformance_result")),
            False,
            False
            if non_expansion.get("closure_does_not_mutate_selected_conformance_result")
            else True,
            "CLOSURE_MUTATES_SELECTED_CONFORMANCE_RESULT",
        ),
        _make_check(
            "closure does not mutate selected distributed standing result",
            bool(
                non_expansion.get(
                    "closure_does_not_mutate_selected_distributed_standing_result"
                )
            ),
            False,
            False
            if non_expansion.get("closure_does_not_mutate_selected_distributed_standing_result")
            else True,
            "CLOSURE_MUTATES_SELECTED_DISTRIBUTED_STANDING_RESULT",
        ),
        _make_check(
            "closure does not create permission",
            bool(non_meaning.get("closure_does_not_create_permission")),
            False,
            False if non_meaning.get("closure_does_not_create_permission") else True,
            "CLOSURE_CREATES_PERMISSION",
        ),
        _make_check(
            "closure does not authorize continuation",
            bool(non_meaning.get("closure_does_not_authorize_continuation")),
            False,
            False if non_meaning.get("closure_does_not_authorize_continuation") else True,
            "CLOSURE_AUTHORIZES_CONTINUATION",
        ),
        _make_check(
            "closure does not authorize operation",
            bool(non_meaning.get("closure_does_not_authorize_operation")),
            False,
            False if non_meaning.get("closure_does_not_authorize_operation") else True,
            "CLOSURE_AUTHORIZES_OPERATION",
        ),
        _make_check(
            "closure does not authorize sync or full body transfer",
            bool(non_meaning.get("closure_does_not_authorize_synchronization"))
            and bool(non_meaning.get("closure_does_not_authorize_full_body_transfer")),
            False,
            False
            if non_meaning.get("closure_does_not_authorize_synchronization")
            and non_meaning.get("closure_does_not_authorize_full_body_transfer")
            else True,
            "CLOSURE_AUTHORIZES_SYNC_OR_FULL_BODY_TRANSFER",
        ),
        _make_check(
            "closure does not create second body",
            bool(non_meaning.get("closure_does_not_create_second_body")),
            False,
            False if non_meaning.get("closure_does_not_create_second_body") else True,
            "CLOSURE_CREATES_SECOND_BODY",
        ),
        _make_check(
            "closure does not create truth or action",
            bool(non_meaning.get("closure_does_not_create_truth_or_action")),
            False,
            False if non_meaning.get("closure_does_not_create_truth_or_action") else True,
            "CLOSURE_CREATES_TRUTH_OR_ACTION",
        ),
        _make_check(
            "closure does not resolve divergence",
            bool(non_meaning.get("closure_does_not_resolve_divergence")),
            False,
            False if non_meaning.get("closure_does_not_resolve_divergence") else True,
            "CLOSURE_RESOLVES_DIVERGENCE",
        ),
        _make_check(
            "closure does not erase evidence",
            bool(non_meaning.get("closure_does_not_erase_evidence")),
            False,
            False if non_meaning.get("closure_does_not_erase_evidence") else True,
            "CLOSURE_ERASES_EVIDENCE",
        ),
        _make_check(
            "closure does not claim final completion",
            bool(non_meaning.get("closure_does_not_complete_final_governance"))
            and bool(non_meaning.get("closure_does_not_complete_final_continuity"))
            and bool(non_meaning.get("closure_does_not_complete_final_system_identity")),
            False,
            False
            if non_meaning.get("closure_does_not_complete_final_governance")
            and non_meaning.get("closure_does_not_complete_final_continuity")
            and non_meaning.get("closure_does_not_complete_final_system_identity")
            else True,
            "CLOSURE_CLAIMS_FINAL_COMPLETION",
        ),
        _make_check(
            "closure does not schedule self-orientation successor",
            bool(non_meaning.get("closure_does_not_schedule_self_orientation_successor")),
            False,
            False
            if non_meaning.get("closure_does_not_schedule_self_orientation_successor")
            else True,
            "CLOSURE_SCHEDULES_SELF_ORIENTATION_SUCCESSOR",
        ),
        _make_check(
            "no mutation replay or merge",
            bool(non_meaning.get("no_mutation_replay_or_merge")),
            False,
            False if non_meaning.get("no_mutation_replay_or_merge") else True,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _make_check(
            "declared closure non claims remain false",
            request_non_claims_conform,
            "required non-claims false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _decide_outcome(
    intent: str | None,
    checks: Sequence[Mapping[str, Any]],
) -> tuple[str, dict[str, Any]]:
    failed_checks = [check for check in checks if not check.get("passed")]
    first_failure_code = next(
        (check.get("failure_code") for check in failed_checks if check.get("failure_code")),
        None,
    )

    if intent == INTENT_BLOCK:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": "CLOSURE_REQUEST_EXPLICITLY_BLOCKED",
                "block_reason": "Closure request explicitly declared block intent.",
            },
        )

    if first_failure_code in BLOCKING_FAILURE_CODES:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": first_failure_code,
                "block_reason": "Closure could not lawfully proceed.",
            },
        )

    if intent == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_CLOSED,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "not_closed_reason": "Request explicitly declined conformance closure recording.",
            },
        )

    if failed_checks:
        return (
            OUTCOME_NOT_CLOSED,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "not_closed_reason": "Selected conformance result failed one or more closure checks.",
                "first_failure_code": first_failure_code,
            },
        )

    return (
        OUTCOME_CLOSED,
        {
            "blocked": False,
            "block_code": None,
            "block_reason": None,
        },
    )


def _build_closure_statement(
    outcome: str,
    selected_section: Mapping[str, Any],
    conformance_meaning: Mapping[str, Any],
    conformance_non_meaning: Mapping[str, Any],
    non_expansion: Mapping[str, Any],
    non_meaning: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    closed = outcome == OUTCOME_CLOSED
    failed_checks = [check for check in checks if not check.get("passed")]
    return {
        "distributed_standing_boundary_conformance_closed": closed,
        "selected_conformance_result_preserved": bool(
            selected_section.get("selected_conformance_result_preserved")
        ),
        "selected_conformance_result_identity_preserved": bool(
            selected_section.get("selected_conformance_result_identity_preserved")
        ),
        "selected_conformance_result_outcome_preserved": bool(
            selected_section.get("selected_conformance_result_outcome_preserved")
        ),
        "selected_conformance_result_is_conformance_result": bool(
            selected_section.get("selected_conformance_result_is_conformance_result")
        ),
        "selected_conformance_result_is_conformant": bool(
            selected_section.get("selected_conformance_result_is_conformant")
        ),
        "selected_conformance_result_failed_check_count_zero": bool(
            selected_section.get("selected_conformance_result_failed_check_count_zero")
        ),
        "conformance_meaning_preserved": bool(
            conformance_meaning.get("conformance_meaning_preserved")
        ),
        "conformance_non_meaning_preserved": all(conformance_non_meaning.values()),
        "closure_did_not_expand_conformance": bool(
            non_expansion.get("closure_does_not_create_new_expansion")
        ),
        "closure_did_not_create_permission": bool(
            non_meaning.get("closure_does_not_create_permission")
        ),
        "closure_did_not_authorize_continuation": bool(
            non_meaning.get("closure_does_not_authorize_continuation")
        ),
        "closure_did_not_authorize_operation": bool(
            non_meaning.get("closure_does_not_authorize_operation")
        ),
        "closure_did_not_authorize_repository_sync": bool(
            non_meaning.get("closure_does_not_authorize_synchronization")
        ),
        "closure_did_not_authorize_full_body_transfer": bool(
            non_meaning.get("closure_does_not_authorize_full_body_transfer")
        ),
        "closure_did_not_create_second_body": bool(
            non_meaning.get("closure_does_not_create_second_body")
        ),
        "closure_did_not_schedule_self_orientation_successor": bool(
            non_meaning.get("closure_does_not_schedule_self_orientation_successor")
        ),
        "closure_did_not_claim_final_completion": bool(
            non_meaning.get("closure_does_not_complete_final_governance")
        )
        and bool(non_meaning.get("closure_does_not_complete_final_continuity"))
        and bool(non_meaning.get("closure_does_not_complete_final_system_identity")),
        "selected_conformance_result_mutated": False,
        "selected_distributed_standing_result_mutated": False,
        "permission_created": False,
        "continuation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "distributed_operation_authorized": False,
        "truth_created": False,
        "action_authorized": False,
        "final_completion_claimed": False,
        "self_orientation_successor_scheduled": False,
        "failed_checks_preserved": _deepcopy(failed_checks),
    }


def build_distributed_standing_boundary_conformance_closure_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact bounded summary for a conformance closure result."""

    checks = result.get("closure_checks", [])
    checks_list = checks if isinstance(checks, list) else []
    passed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and check.get("passed")
    )
    failed_count = sum(
        1 for check in checks_list if isinstance(check, Mapping) and not check.get("passed")
    )

    declared = result.get("declared_closure_question", {})
    selected = result.get("selected_conformance_result", {})
    statement = result.get("closure_statement", {})
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
        "closure_request_id": declared_map.get("closure_request_id"),
        "closure_question": declared_map.get("closure_question"),
        "closure_intent": declared_map.get("closure_intent"),
        "selected_conformance_result_id": selected_map.get("selected_conformance_result_id"),
        "selected_conformance_result_outcome": selected_map.get(
            "selected_conformance_result_outcome"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "distributed_standing_boundary_conformance_closed": statement_map.get(
            "distributed_standing_boundary_conformance_closed"
        ),
        "selected_conformance_result_preserved": statement_map.get(
            "selected_conformance_result_preserved"
        ),
        "selected_conformance_result_identity_preserved": statement_map.get(
            "selected_conformance_result_identity_preserved"
        ),
        "selected_conformance_result_outcome_preserved": statement_map.get(
            "selected_conformance_result_outcome_preserved"
        ),
        "selected_conformance_result_is_conformance_result": statement_map.get(
            "selected_conformance_result_is_conformance_result"
        ),
        "selected_conformance_result_is_conformant": statement_map.get(
            "selected_conformance_result_is_conformant"
        ),
        "selected_conformance_result_failed_check_count_zero": statement_map.get(
            "selected_conformance_result_failed_check_count_zero"
        ),
        "conformance_meaning_preserved": statement_map.get("conformance_meaning_preserved"),
        "conformance_non_meaning_preserved": statement_map.get(
            "conformance_non_meaning_preserved"
        ),
        "closure_did_not_expand_conformance": statement_map.get(
            "closure_did_not_expand_conformance"
        ),
        "closure_did_not_create_permission": statement_map.get(
            "closure_did_not_create_permission"
        ),
        "closure_did_not_authorize_continuation": statement_map.get(
            "closure_did_not_authorize_continuation"
        ),
        "closure_did_not_authorize_operation": statement_map.get(
            "closure_did_not_authorize_operation"
        ),
        "closure_did_not_authorize_repository_sync": statement_map.get(
            "closure_did_not_authorize_repository_sync"
        ),
        "closure_did_not_authorize_full_body_transfer": statement_map.get(
            "closure_did_not_authorize_full_body_transfer"
        ),
        "closure_did_not_create_second_body": statement_map.get(
            "closure_did_not_create_second_body"
        ),
        "closure_did_not_schedule_self_orientation_successor": statement_map.get(
            "closure_did_not_schedule_self_orientation_successor"
        ),
        "closure_did_not_claim_final_completion": statement_map.get(
            "closure_did_not_claim_final_completion"
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
                "selected_conformance_result_mutated",
                "selected_distributed_standing_result_mutated",
                "closure_expanded_conformance",
                "closure_created_permission",
                "closure_authorized_operation",
                "closure_claimed_final_completion",
                "self_orientation_successor_scheduled",
            )
        },
    }


def _build_result(
    request: Mapping[str, Any],
    request_path: str | None,
    selected: Mapping[str, Any],
    selected_path: str | None,
    selected_load_failures: Sequence[str],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    declared = _declared_closure_question_section(request, request_path)
    selected_section = _build_selected_conformance_result_section(
        request,
        selected,
        selected_path,
        selected_load_failures,
    )
    selected_basis = _build_selected_conformance_result_basis(request)
    conformance_meaning = _build_conformance_meaning(selected)
    conformance_non_meaning = _deepcopy(CONFORMANCE_NON_MEANING)
    non_expansion = _build_closure_non_expansion(selected, request)
    non_meaning_preservation = _build_closure_non_meaning_preservation(selected, request)

    checks = _build_closure_checks(
        request,
        selected_section,
        selected_basis,
        conformance_meaning,
        non_expansion,
        non_meaning_preservation,
        precheck_failures,
    )
    outcome, block = _decide_outcome(request.get("closure_intent"), checks)
    statement = _build_closure_statement(
        outcome,
        selected_section,
        conformance_meaning,
        conformance_non_meaning,
        non_expansion,
        non_meaning_preservation,
        checks,
    )
    result_id = _first_present(
        request.get("closure_request_id"),
        selected_section.get("selected_conformance_result_id"),
        "distributed_standing_boundary_conformance_closure",
    )

    result = {
        "distributed_standing_boundary_conformance_closure_metadata": {
            "closure_result_id": f"{result_id}__distributed_standing_boundary_conformance_closure",
            "closure_result_type": RESULT_TYPE,
            "closure_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_closure_question": declared,
        "selected_conformance_result": selected_section,
        "selected_conformance_result_basis": selected_basis,
        "conformance_meaning": conformance_meaning,
        "conformance_non_meaning": conformance_non_meaning,
        "closure_checks": checks,
        "closure_statement": statement,
        "closure_non_meaning": _deepcopy(CLOSURE_NON_MEANING),
        "what_remains_open": _deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": _result_non_claims(request),
        "outcome": outcome,
        "block": block,
    }
    result["distributed_standing_boundary_conformance_closure_summary"] = (
        build_distributed_standing_boundary_conformance_closure_summary(result)
    )
    return result


def resolve_distributed_standing_boundary_conformance_closure(
    declared_closure_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded distributed standing boundary conformance closure request."""

    if declared_closure_request is None:
        request: dict[str, Any] = {}
        precheck_failures: list[str] = []
    elif not isinstance(declared_closure_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_CLOSURE_REQUEST_MALFORMED"]
    else:
        request = _deepcopy(dict(declared_closure_request))
        precheck_failures = []

    selected, selected_path, selected_load_failures = _load_selected_conformance_result(request)
    return _build_result(
        request,
        None,
        selected,
        selected_path,
        selected_load_failures,
        precheck_failures,
    )


def resolve_distributed_standing_boundary_conformance_closure_from_path(
    declared_closure_request_path: Path | str,
) -> dict:
    """Load a JSON object closure request from path and resolve closure."""

    path = _to_path(declared_closure_request_path)
    try:
        request = _read_json_object(
            path,
            "DECLARED_CLOSURE_REQUEST_UNREADABLE",
            "DECLARED_CLOSURE_REQUEST_MALFORMED",
        )
        precheck_failures: list[str] = []
    except DistributedStandingBoundaryConformanceClosureError as exc:
        request = {}
        precheck_failures = [exc.block_code]

    selected, selected_path, selected_load_failures = _load_selected_conformance_result(request)
    return _build_result(
        request,
        str(path),
        selected,
        selected_path,
        selected_load_failures,
        precheck_failures,
    )


def write_distributed_standing_boundary_conformance_closure_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive conformance closure result as stable UTF-8 JSON."""

    if not isinstance(result, Mapping):
        raise DistributedStandingBoundaryConformanceClosureError(
            "Closure result must be a mapping.",
            "SELECTED_CONFORMANCE_RESULT_MALFORMED",
        )

    result_copy = _deepcopy(dict(result))
    if output_path is None:
        summary = result_copy.get("distributed_standing_boundary_conformance_closure_summary", {})
        request_id = summary.get("closure_request_id") if isinstance(summary, Mapping) else None
        selected_id = (
            summary.get("selected_conformance_result_id")
            if isinstance(summary, Mapping)
            else None
        )
        filename_root = _safe_filename_part(_first_present(request_id, selected_id))
        output = (
            DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSURE_ROOT
            / f"{filename_root}__distributed_standing_boundary_conformance_closure_result.json"
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


def build_declared_distributed_standing_boundary_conformance_closure_request(
    closure_request_id: str,
    closure_question: str,
    selected_conformance_result: Mapping[str, Any] | str,
    selected_conformance_result_basis: Mapping[str, Any] | str,
    closure_intent: str = INTENT_RECORD,
    *,
    selected_conformance_result_path: str | None = None,
    selected_conformance_result_id: str | None = None,
    selected_conformance_result_outcome: str | None = None,
    expected_selected_conformance_result_outcome: str = EXPECTED_SELECTED_CONFORMANCE_OUTCOME,
) -> dict:
    """Build a bounded declared closure request with required false non-claims."""

    request = {
        "closure_request_id": closure_request_id,
        "closure_question": closure_question,
        "closure_intent": closure_intent,
        "selected_conformance_result": _deepcopy(selected_conformance_result),
        "selected_conformance_result_basis": _deepcopy(selected_conformance_result_basis),
        "selected_conformance_result_id": selected_conformance_result_id,
        "selected_conformance_result_outcome": selected_conformance_result_outcome,
        "expected_selected_conformance_result_outcome": (
            expected_selected_conformance_result_outcome
        ),
        "expected_failed_check_count": EXPECTED_FAILED_CHECK_COUNT,
        "declared_non_claims": _deepcopy(REQUIRED_NON_CLAIMS),
    }

    if selected_conformance_result_path is not None:
        request["selected_conformance_result_path"] = selected_conformance_result_path

    return request
