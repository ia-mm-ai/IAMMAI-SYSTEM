"""Bounded distributed standing boundary conformance resolver.

This module verifies whether a selected distributed standing boundary result
preserved its declared basis and non-claims. It records conformance only; it
does not authorize continuation, repository synchronization, full body
transfer, second-body creation, distributed operation, carrier selection,
divergence resolution, truth, action, permission, or final completion.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class DistributedStandingBoundaryConformanceError(Exception):
    """Raised for hard conformance resolver failures."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REPO_ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_distributed_standing_boundary_conformance"
)

RESOLVER_MODULE = "resolve_distributed_standing_boundary_conformance"
RESULT_TYPE = "distributed_standing_boundary_conformance_result"
RESULT_VERSION = "0.1.0"

OUTCOME_CONFORMANT = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT"
OUTCOME_NOT_CONFORMANT = "DISTRIBUTED_STANDING_BOUNDARY_NOT_CONFORMANT"
OUTCOME_BLOCKED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_BLOCKED"

SUPPORTED_OUTCOMES = {
    OUTCOME_CONFORMANT,
    OUTCOME_NOT_CONFORMANT,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE"
INTENT_BLOCK = "BLOCK_DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE"

SUPPORTED_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

EXPECTED_SELECTED_RESULT_OUTCOME = "DISTRIBUTED_STANDING_POSTURE_RECORDED"

BLOCKING_FAILURE_CODES = {
    "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
    "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
    "CONFORMANCE_QUESTION_UNDECLARED",
    "CONFORMANCE_INTENT_UNSUPPORTED",
    "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED",
    "SELECTED_DISTRIBUTED_STANDING_RESULT_MISSING",
    "SELECTED_DISTRIBUTED_STANDING_RESULT_UNREADABLE",
    "SELECTED_DISTRIBUTED_STANDING_RESULT_MALFORMED",
    "SELECTED_RESULT_IDENTITY_MISSING",
    "SELECTED_RESULT_OUTCOME_MISSING",
    "SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY",
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
    "summary_overrode_detailed_basis": False,
    "latest_file_standing": False,
    "latest_turn_standing": False,
    "majority_carrier_standing": False,
    "successful_receipt_count_standing": False,
    "registry_record_standing": False,
    "lifecycle_status_standing": False,
    "standing_propagation_standing": False,
    "continuity_turn_standing": False,
    "currentness_successor_standing": False,
    "divergence_consequence_standing": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

SELECTED_RESULT_NON_CLAIM_ALIASES = {
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
        "distributed_standing_authorized_sync",
    ),
    "full_body_transfer_authorized": (
        "full_body_transfer_authorized",
        "distributed_standing_authorized_full_body_transfer",
    ),
    "second_body_created": (
        "second_body_created",
        "distributed_standing_created_second_body",
    ),
    "continuation_authorized": (
        "continuation_authorized",
        "distributed_standing_authorized_continuation",
    ),
    "distributed_operation_authorized": (
        "distributed_operation_authorized",
        "distributed_standing_authorized_distributed_operation",
    ),
    "evidence_erased": ("evidence_erased", "distributed_standing_erased_evidence"),
    "summary_overrode_detailed_basis": ("summary_overrode_detailed_basis",),
    "latest_file_standing": ("latest_file_standing",),
    "latest_turn_standing": ("latest_turn_standing",),
    "majority_carrier_standing": ("majority_carrier_standing",),
    "successful_receipt_count_standing": ("successful_receipt_count_standing",),
    "registry_record_standing": ("registry_record_standing",),
    "lifecycle_status_standing": ("lifecycle_status_standing",),
    "standing_propagation_standing": ("standing_propagation_standing",),
    "continuity_turn_standing": ("continuity_turn_standing",),
    "currentness_successor_standing": ("currentness_successor_standing",),
    "divergence_consequence_standing": ("divergence_consequence_standing",),
    "mutation_performed": ("mutation_performed",),
    "replay_performed": ("replay_performed",),
    "merge_performed": ("merge_performed",),
}

OPEN_ITEMS = {
    "distributed_standing_boundary_conformance_closure": "open_not_scheduled_not_authorized_not_executed",
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

CONFORMANCE_NON_MEANING = {
    "permission": True,
    "continuation": True,
    "distributed_operation": True,
    "repository_synchronization": True,
    "full_body_transfer": True,
    "second_body": True,
    "carrier_sovereignty": True,
    "currentness": True,
    "truth": True,
    "action": True,
    "divergence_resolution": True,
    "evidence_erasure": True,
    "implementation": True,
    "completion": True,
    "launch_publication_readiness": True,
    "final_governance": True,
    "final_continuity_completion": True,
    "self_orientation_successor_by_default": True,
    "closure_by_default": True,
}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _as_plain_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    return dict(value)


def _to_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return REPO_ROOT / candidate


def _read_json_object(path: Path, unreadable_code: str, malformed_code: str) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DistributedStandingBoundaryConformanceError(
            f"Unable to read JSON object from {path}: {exc}",
            unreadable_code,
        ) from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DistributedStandingBoundaryConformanceError(
            f"Malformed JSON object at {path}: {exc}",
            malformed_code,
        ) from exc

    if not isinstance(parsed, Mapping):
        raise DistributedStandingBoundaryConformanceError(
            f"JSON content at {path} is not an object.",
            malformed_code,
        )

    return _deepcopy(dict(parsed))


def _is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(value, (str, bytes, bytearray)):
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


def _recursive_truthy(value: Any, keys: Sequence[str]) -> bool:
    found = _recursive_find(value, keys)
    return bool(found)


def _recursive_flag_true(value: Any, keys: Sequence[str]) -> bool:
    found = _recursive_find(value, keys)
    return found is True


def _false_preserved(value: Any, key: str) -> bool:
    aliases = SELECTED_RESULT_NON_CLAIM_ALIASES.get(key, (key,))
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


def _normalize_identifier(value: Any) -> str:
    text = str(value or "").strip().lower()
    return text.replace("-", "_").replace(" ", "_")


def _extract_selected_result_id(selected_result: Mapping[str, Any], request: Mapping[str, Any]) -> str | None:
    metadata = selected_result.get("distributed_standing_metadata")
    summary = selected_result.get("distributed_standing_summary")
    question = selected_result.get("declared_distributed_standing_question")

    return _first_present(
        request.get("selected_result_id"),
        _recursive_find(metadata, ("distributed_standing_result_id", "result_id"))
        if isinstance(metadata, Mapping)
        else None,
        _recursive_find(summary, ("distributed_standing_request_id", "result_id"))
        if isinstance(summary, Mapping)
        else None,
        _recursive_find(question, ("distributed_standing_request_id", "request_id"))
        if isinstance(question, Mapping)
        else None,
        selected_result.get("distributed_standing_result_id"),
        selected_result.get("result_id"),
    )


def _extract_selected_result_outcome(
    selected_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> str | None:
    return _first_present(
        request.get("selected_result_outcome"),
        selected_result.get("outcome"),
        _recursive_find(selected_result.get("distributed_standing_summary"), ("outcome",))
        if isinstance(selected_result.get("distributed_standing_summary"), Mapping)
        else None,
    )


def _is_distributed_standing_boundary_result(selected_result: Mapping[str, Any]) -> bool:
    metadata = selected_result.get("distributed_standing_metadata")
    result_type = (
        _recursive_find(metadata, ("distributed_standing_result_type", "result_type"))
        if isinstance(metadata, Mapping)
        else None
    )
    resolver_module = (
        _recursive_find(metadata, ("resolver_module",))
        if isinstance(metadata, Mapping)
        else None
    )
    return (
        result_type == "distributed_standing_boundary_result"
        or resolver_module == "resolve_distributed_standing_boundary"
        or {
            "distributed_standing_statement",
            "distributed_standing_checks",
            "distributed_standing_summary",
        }.issubset(set(selected_result.keys()))
    )


def _selected_result_path_value(request: Mapping[str, Any]) -> str | None:
    path = request.get("selected_result_path")
    if _is_present(path):
        return str(path)
    selected = request.get("selected_distributed_standing_boundary_result")
    if isinstance(selected, str) and selected.strip():
        return selected
    return None


def _load_selected_result(request: Mapping[str, Any]) -> tuple[dict[str, Any], str | None, list[str]]:
    path_value = _selected_result_path_value(request)
    if path_value:
        path = _to_path(path_value)
        try:
            return (
                _read_json_object(
                    path,
                    "SELECTED_DISTRIBUTED_STANDING_RESULT_UNREADABLE",
                    "SELECTED_DISTRIBUTED_STANDING_RESULT_MALFORMED",
                ),
                str(path),
                [],
            )
        except DistributedStandingBoundaryConformanceError as exc:
            return {}, str(path), [exc.block_code]

    selected = request.get("selected_distributed_standing_boundary_result")
    if isinstance(selected, Mapping):
        return _deepcopy(dict(selected)), None, []

    if selected is None:
        return {}, None, ["SELECTED_DISTRIBUTED_STANDING_RESULT_MISSING"]

    return {}, None, ["SELECTED_DISTRIBUTED_STANDING_RESULT_MALFORMED"]


def _carrier_evidence_entries(selected_result: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    section = selected_result.get("selected_carrier_evidence")
    candidates: list[Any] = []

    if isinstance(section, list):
        candidates.extend(section)
    elif isinstance(section, Mapping):
        for key in (
            "raw_selected_carrier_evidence",
            "selected_carrier_evidence",
            "carrier_evidence",
            "evidence",
            "evidence_items",
        ):
            value = section.get(key)
            if isinstance(value, list):
                candidates.extend(value)
            elif isinstance(value, Mapping):
                candidates.append(value)
        if any(key in section for key in ("evidence_id", "carrier_id", "evidence_outcome", "outcome")):
            candidates.append(section)

    entries = [item for item in candidates if isinstance(item, Mapping)]
    if entries:
        return entries

    summary = selected_result.get("distributed_standing_summary")
    if isinstance(summary, Mapping):
        ids = summary.get("selected_carrier_evidence_ids") or []
        outcomes = summary.get("selected_carrier_evidence_outcomes") or []
        if isinstance(ids, list):
            built = []
            for index, evidence_id in enumerate(ids):
                built.append(
                    {
                        "evidence_id": evidence_id,
                        "evidence_outcome": outcomes[index]
                        if isinstance(outcomes, list) and index < len(outcomes)
                        else None,
                    }
                )
            return built

    return []


def _entry_text(entry: Mapping[str, Any]) -> str:
    return json.dumps(entry, sort_keys=True, default=str).lower()


def _entry_has(entry: Mapping[str, Any], *tokens: str) -> bool:
    text = _entry_text(entry)
    return all(token.lower() in text for token in tokens)


def _has_carrier_b_success(entries: Sequence[Mapping[str, Any]]) -> bool:
    return any(
        (_entry_has(entry, "carrier_b") or _entry_has(entry, "carrier b"))
        and ("success" in _entry_text(entry) or "received" in _entry_text(entry))
        for entry in entries
    )


def _has_carrier_c_block(entries: Sequence[Mapping[str, Any]]) -> bool:
    return any(
        (_entry_has(entry, "carrier_c") or _entry_has(entry, "carrier c"))
        and ("blocked" in _entry_text(entry) or "refused" in _entry_text(entry))
        for entry in entries
    )


def _has_divergence_evidence(entries: Sequence[Mapping[str, Any]]) -> bool:
    return any("divergence" in _entry_text(entry) for entry in entries)


def _basis_preserved(selected_result: Mapping[str, Any], section_name: str, preserved_key: str) -> bool:
    return _recursive_flag_true(selected_result, (preserved_key,)) or _is_present(
        selected_result.get(section_name)
    )


def _build_prerequisite_basis_conformance(
    selected_result: Mapping[str, Any],
) -> dict[str, Any]:
    entries = _carrier_evidence_entries(selected_result)
    identities_present = all(
        _is_present(_recursive_find(entry, ("evidence_id", "carrier_evidence_id", "id", "carrier_id")))
        for entry in entries
    )
    outcomes_present = all(
        _is_present(_recursive_find(entry, ("evidence_outcome", "outcome", "status", "posture")))
        for entry in entries
    )

    section = {
        "source_body_lineage_preserved": _recursive_flag_true(
            selected_result,
            ("source_body_lineage_preserved",),
        )
        or _is_present(selected_result.get("source_body_lineage")),
        "selected_carrier_evidence_identities_preserved": bool(entries) and identities_present,
        "selected_carrier_evidence_outcomes_preserved": bool(entries) and outcomes_present,
        "carrier_b_successful_receipt_evidence_preserved": _has_carrier_b_success(entries),
        "carrier_c_blocked_receipt_evidence_preserved": _has_carrier_c_block(entries),
        "b_c_divergence_evidence_preserved": _has_divergence_evidence(entries)
        or _is_present(selected_result.get("divergence_basis")),
        "divergence_consequence_basis_preserved": _basis_preserved(
            selected_result,
            "divergence_consequence_basis",
            "divergence_consequence_basis_preserved",
        ),
        "currentness_successor_basis_preserved": _basis_preserved(
            selected_result,
            "currentness_successor_basis",
            "currentness_successor_basis_preserved",
        ),
        "carrier_continuity_turn_v2_basis_preserved": _basis_preserved(
            selected_result,
            "carrier_continuity_turn_basis",
            "carrier_continuity_turn_basis_preserved",
        ),
        "standing_propagation_v2_basis_preserved": _basis_preserved(
            selected_result,
            "standing_propagation_basis",
            "standing_propagation_basis_preserved",
        ),
        "registry_persistence_v2_basis_preserved": _basis_preserved(
            selected_result,
            "registry_persistence_basis",
            "registry_persistence_basis_preserved",
        ),
        "lifecycle_basis_preserved": _basis_preserved(
            selected_result,
            "lifecycle_basis",
            "lifecycle_basis_preserved",
        ),
        "relation_conformance_closure_basis_preserved": _basis_preserved(
            selected_result,
            "relation_conformance_closure_basis",
            "relation_conformance_closure_basis_preserved",
        ),
        "current_body_conformance_v3_closure_basis_preserved": _basis_preserved(
            selected_result,
            "current_body_conformance_v3_closure_basis",
            "current_body_conformance_v3_closure_basis_preserved",
        ),
    }
    section["prerequisite_basis_conformant"] = all(section.values())
    return section


def _build_refusal_divergence_lineage_conformance(
    selected_result: Mapping[str, Any],
) -> dict[str, Any]:
    section = {
        "visible_refusal_preserved": _recursive_flag_true(
            selected_result,
            ("visible_refusal_preserved",),
        ),
        "visible_divergence_preserved": _recursive_flag_true(
            selected_result,
            ("visible_divergence_preserved",),
        ),
        "blocked_attempts_preserved": _recursive_flag_true(
            selected_result,
            ("blocked_attempts_preserved",),
        ),
        "projection_mismatch_preserved": _recursive_flag_true(
            selected_result,
            ("projection_mismatch_preserved",),
        ),
        "detailed_basis_distinguished_from_summary": _recursive_flag_true(
            selected_result,
            ("detailed_basis_distinguished_from_summary",),
        ),
        "summary_did_not_override_detailed_basis": not _recursive_true(
            selected_result,
            ("summary_overrode_detailed_basis",),
        ),
        "source_body_lineage_not_replaced": _false_preserved(selected_result, "source_replaced"),
        "carrier_b_success_did_not_erase_carrier_c_block": _false_preserved(
            selected_result,
            "evidence_erased",
        )
        and _has_carrier_b_success(_carrier_evidence_entries(selected_result))
        and _has_carrier_c_block(_carrier_evidence_entries(selected_result)),
        "carrier_c_block_did_not_invalidate_carrier_b_success": _false_preserved(
            selected_result,
            "losing_carrier_invalidated",
        )
        and _false_preserved(selected_result, "winning_carrier_selected"),
        "b_c_divergence_caution_preserved": _basis_preserved(
            selected_result,
            "divergence_consequence_basis",
            "divergence_consequence_basis_preserved",
        )
        and "caution" in json.dumps(
            selected_result.get("divergence_consequence_basis", {}),
            sort_keys=True,
            default=str,
        ).lower()
        or "caution" in json.dumps(
            selected_result.get("distributed_standing_summary", {}),
            sort_keys=True,
            default=str,
        ).lower(),
    }
    section["refusal_divergence_lineage_conformant"] = all(section.values())
    return section


def _build_non_claim_conformance(selected_result: Mapping[str, Any]) -> dict[str, Any]:
    section = {
        "no_carrier_currentness": _false_preserved(selected_result, "carrier_currentness_created"),
        "no_current_carrier_selected": _false_preserved(selected_result, "current_carrier_selected"),
        "no_winning_carrier_selected": _false_preserved(selected_result, "winning_carrier_selected"),
        "no_losing_carrier_invalidated": _false_preserved(selected_result, "losing_carrier_invalidated"),
        "no_source_replacement": _false_preserved(selected_result, "source_replaced"),
        "no_authority": _false_preserved(selected_result, "authority_created"),
        "no_permission": _false_preserved(selected_result, "permission_created"),
        "no_truth": _false_preserved(selected_result, "truth_created"),
        "no_action": _false_preserved(selected_result, "action_authorized"),
        "no_divergence_resolution": _false_preserved(selected_result, "divergence_resolved"),
        "no_evidence_erasure": _false_preserved(selected_result, "evidence_erased"),
        "no_repository_synchronization": _false_preserved(
            selected_result,
            "repository_synchronization_authorized",
        ),
        "no_full_body_transfer": _false_preserved(selected_result, "full_body_transfer_authorized"),
        "no_second_body": _false_preserved(selected_result, "second_body_created"),
        "no_continuation": _false_preserved(selected_result, "continuation_authorized"),
        "no_distributed_operation": _false_preserved(selected_result, "distributed_operation_authorized"),
        "no_latest_file_standing": _false_preserved(selected_result, "latest_file_standing"),
        "no_latest_turn_standing": _false_preserved(selected_result, "latest_turn_standing"),
        "no_majority_standing": _false_preserved(selected_result, "majority_carrier_standing"),
        "no_success_count_standing": _false_preserved(
            selected_result,
            "successful_receipt_count_standing",
        ),
        "no_registry_standing_by_itself": _false_preserved(selected_result, "registry_record_standing"),
        "no_lifecycle_standing_by_itself": _false_preserved(selected_result, "lifecycle_status_standing"),
        "no_standing_propagation_standing_by_itself": _false_preserved(
            selected_result,
            "standing_propagation_standing",
        ),
        "no_continuity_turn_standing_by_itself": _false_preserved(
            selected_result,
            "continuity_turn_standing",
        ),
        "no_currentness_successor_standing_by_itself": _false_preserved(
            selected_result,
            "currentness_successor_standing",
        ),
        "no_divergence_consequence_standing_by_itself": _false_preserved(
            selected_result,
            "divergence_consequence_standing",
        ),
        "no_mutation": _false_preserved(selected_result, "mutation_performed"),
        "no_replay": _false_preserved(selected_result, "replay_performed"),
        "no_merge": _false_preserved(selected_result, "merge_performed"),
    }
    section["non_claim_conformant"] = all(section.values())
    return section


def _summary_matches_when_exposed(
    summary: Mapping[str, Any],
    statement: Mapping[str, Any],
    keys: Sequence[str],
) -> bool:
    for key in keys:
        if key in summary and key in statement and summary.get(key) != statement.get(key):
            return False
    return True


def _build_summary_detail_correspondence(
    selected_result: Mapping[str, Any],
) -> dict[str, Any]:
    summary = selected_result.get("distributed_standing_summary")
    statement = selected_result.get("distributed_standing_statement")
    checks = selected_result.get("distributed_standing_checks")
    non_claims = selected_result.get("non_claims")

    summary_map = summary if isinstance(summary, Mapping) else {}
    statement_map = statement if isinstance(statement, Mapping) else {}
    checks_list = checks if isinstance(checks, list) else []

    keys = (
        "source_body_lineage_preserved",
        "selected_carrier_evidence_preserved",
        "divergence_consequence_basis_preserved",
        "currentness_successor_basis_preserved",
        "carrier_continuity_turn_basis_preserved",
        "standing_propagation_basis_preserved",
        "registry_persistence_basis_preserved",
        "lifecycle_basis_preserved",
        "relation_conformance_closure_basis_preserved",
        "current_body_conformance_v3_closure_basis_preserved",
        "visible_refusal_preserved",
        "visible_divergence_preserved",
        "blocked_attempts_preserved",
        "projection_mismatch_preserved",
        "detailed_basis_distinguished_from_summary",
        "summary_overrode_detailed_basis",
        "carrier_currentness_created",
        "current_carrier_selected",
        "winning_carrier_selected",
        "losing_carrier_invalidated",
        "source_replaced",
        "authority_created",
        "permission_created",
        "truth_created",
        "action_authorized",
        "divergence_resolved",
        "evidence_erased",
        "repository_synchronization_authorized",
        "full_body_transfer_authorized",
        "second_body_created",
        "continuation_authorized",
        "distributed_operation_authorized",
    )

    failed_summary_count = summary_map.get("failed_check_count")
    actual_failed_count = sum(1 for check in checks_list if isinstance(check, Mapping) and not check.get("passed"))

    section = {
        "selected_result_summary_present": bool(summary_map),
        "selected_result_detail_body_present": bool(statement_map),
        "summary_corresponds_to_detailed_body_where_exposed": _summary_matches_when_exposed(
            summary_map,
            statement_map,
            keys,
        ),
        "summary_does_not_override_detailed_basis": not _recursive_true(
            selected_result,
            ("summary_overrode_detailed_basis",),
        ),
        "checks_statement_and_non_claims_consistent_where_exposed": (
            failed_summary_count in (None, actual_failed_count)
            and isinstance(statement, Mapping)
            and isinstance(non_claims, Mapping)
        ),
        "conformance_does_not_rely_on_summary_alone": bool(statement_map),
        "detailed_body_used_where_summary_incomplete_or_compressed": bool(statement_map),
    }
    section["summary_detail_correspondence_passed"] = all(section.values())
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


def _build_selected_result_section(
    request: Mapping[str, Any],
    selected_result: Mapping[str, Any],
    selected_result_path: str | None,
    selected_load_failures: Sequence[str],
) -> dict[str, Any]:
    selected_result_id = _extract_selected_result_id(selected_result, request)
    selected_result_outcome = _extract_selected_result_outcome(selected_result, request)
    expected_outcome = _first_present(
        request.get("expected_selected_result_outcome"),
        EXPECTED_SELECTED_RESULT_OUTCOME,
    )
    return {
        "selected_result_id": selected_result_id,
        "selected_result_path": selected_result_path,
        "selected_result_outcome": selected_result_outcome,
        "expected_selected_result_outcome": expected_outcome,
        "selected_result_preserved": bool(selected_result),
        "selected_result_identity_preserved": _is_present(selected_result_id),
        "selected_result_outcome_preserved": _is_present(selected_result_outcome),
        "selected_result_readable_or_supplied": bool(selected_result) and not selected_load_failures,
        "selected_result_parseable": bool(selected_result) and not selected_load_failures,
        "selected_result_is_distributed_standing_boundary": (
            bool(selected_result) and _is_distributed_standing_boundary_result(selected_result)
        ),
        "selected_result_load_failures": list(selected_load_failures),
        "raw_selected_distributed_standing_boundary_result": _deepcopy(dict(selected_result))
        if isinstance(selected_result, Mapping)
        else {},
    }


def _build_selected_result_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_result_basis")
    return {
        "selected_result_basis_declared": _is_present(basis),
        "selected_result_basis": _deepcopy(basis),
        "expected_required_basis": _deepcopy(request.get("expected_required_basis")),
        "expected_required_non_claims": _deepcopy(request.get("expected_required_non_claims")),
        "summary_detail_correspondence_basis": _deepcopy(
            request.get("summary_detail_correspondence_basis")
        ),
        "conformance_scope": _deepcopy(request.get("conformance_scope")),
        "not_conformant_reason": request.get("not_conformant_reason"),
        "block_reason": request.get("block_reason"),
        "basis_does_not_authorize_expansion": True,
        "basis_does_not_authorize_continuation": True,
        "basis_does_not_authorize_repository_sync": True,
        "basis_does_not_authorize_full_body_transfer": True,
        "basis_does_not_create_second_body": True,
        "basis_does_not_authorize_distributed_operation": True,
    }


def _declared_question_section(request: Mapping[str, Any], request_path: str | None) -> dict[str, Any]:
    intent = request.get("conformance_intent")
    return {
        "conformance_request_id": request.get("conformance_request_id"),
        "conformance_question": request.get("conformance_question"),
        "conformance_intent": intent,
        "conformance_request_path": request_path,
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "conformance_is_not_permission": True,
        "conformance_is_not_continuation": True,
        "conformance_is_not_distributed_operation": True,
        "conformance_is_not_synchronization": True,
        "conformance_is_not_full_body_transfer": True,
        "conformance_is_not_second_body": True,
        "conformance_does_not_create_currentness": True,
        "conformance_does_not_create_truth_or_action": True,
    }


def _build_conformance_checks(
    request: Mapping[str, Any],
    selected_section: Mapping[str, Any],
    basis_section: Mapping[str, Any],
    prerequisite: Mapping[str, Any],
    refusal: Mapping[str, Any],
    non_claim: Mapping[str, Any],
    summary_detail: Mapping[str, Any],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    intent = request.get("conformance_intent")
    expected_outcome = selected_section.get("expected_selected_result_outcome")
    actual_outcome = selected_section.get("selected_result_outcome")
    request_non_claims_conform, _, _ = _request_non_claims_conform(request)

    checks = [
        _make_check(
            "declared conformance request is well formed",
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED" not in precheck_failures,
            "mapping request",
            "malformed request" if "DECLARED_CONFORMANCE_REQUEST_MALFORMED" in precheck_failures else "mapping request",
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
            "selected result basis declared",
            bool(basis_section.get("selected_result_basis_declared")),
            "selected result basis declared",
            basis_section.get("selected_result_basis_declared"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "selected artifact identity present",
            bool(selected_section.get("selected_result_identity_preserved")),
            "selected result identity present",
            selected_section.get("selected_result_id"),
            "SELECTED_RESULT_IDENTITY_MISSING",
        ),
        _make_check(
            "selected artifact outcome present",
            bool(selected_section.get("selected_result_outcome_preserved")),
            "selected result outcome present",
            actual_outcome,
            "SELECTED_RESULT_OUTCOME_MISSING",
        ),
        _make_check(
            "selected artifact readable and parseable",
            bool(selected_section.get("selected_result_readable_or_supplied"))
            and bool(selected_section.get("selected_result_parseable")),
            "readable parseable selected result",
            selected_section.get("selected_result_load_failures") or "readable parseable",
            selected_section.get("selected_result_load_failures", [None])[0]
            if selected_section.get("selected_result_load_failures")
            else "SELECTED_DISTRIBUTED_STANDING_RESULT_MISSING",
        ),
        _make_check(
            "selected artifact is distributed standing boundary result",
            bool(selected_section.get("selected_result_is_distributed_standing_boundary")),
            "distributed standing boundary result",
            selected_section.get("selected_result_is_distributed_standing_boundary"),
            "SELECTED_RESULT_NOT_DISTRIBUTED_STANDING_BOUNDARY",
        ),
        _make_check(
            "selected artifact outcome matches expected outcome",
            not _is_present(actual_outcome) or actual_outcome == expected_outcome,
            expected_outcome,
            actual_outcome,
            "SELECTED_RESULT_OUTCOME_UNEXPECTED",
        ),
        _make_check(
            "source body lineage preserved",
            bool(prerequisite.get("source_body_lineage_preserved")),
            True,
            prerequisite.get("source_body_lineage_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "carrier b successful receipt evidence preserved",
            bool(prerequisite.get("carrier_b_successful_receipt_evidence_preserved")),
            True,
            prerequisite.get("carrier_b_successful_receipt_evidence_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "carrier c blocked receipt evidence preserved",
            bool(prerequisite.get("carrier_c_blocked_receipt_evidence_preserved")),
            True,
            prerequisite.get("carrier_c_blocked_receipt_evidence_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "b c divergence evidence preserved",
            bool(prerequisite.get("b_c_divergence_evidence_preserved")),
            True,
            prerequisite.get("b_c_divergence_evidence_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "divergence consequence basis preserved",
            bool(prerequisite.get("divergence_consequence_basis_preserved")),
            True,
            prerequisite.get("divergence_consequence_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "currentness successor basis preserved",
            bool(prerequisite.get("currentness_successor_basis_preserved")),
            True,
            prerequisite.get("currentness_successor_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "continuity turn v2 basis preserved",
            bool(prerequisite.get("carrier_continuity_turn_v2_basis_preserved")),
            True,
            prerequisite.get("carrier_continuity_turn_v2_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "standing propagation v2 basis preserved",
            bool(prerequisite.get("standing_propagation_v2_basis_preserved")),
            True,
            prerequisite.get("standing_propagation_v2_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "registry persistence v2 basis preserved",
            bool(prerequisite.get("registry_persistence_v2_basis_preserved")),
            True,
            prerequisite.get("registry_persistence_v2_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "lifecycle basis preserved",
            bool(prerequisite.get("lifecycle_basis_preserved")),
            True,
            prerequisite.get("lifecycle_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "relation conformance closure basis preserved",
            bool(prerequisite.get("relation_conformance_closure_basis_preserved")),
            True,
            prerequisite.get("relation_conformance_closure_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "current body conformance v3 closure basis preserved",
            bool(prerequisite.get("current_body_conformance_v3_closure_basis_preserved")),
            True,
            prerequisite.get("current_body_conformance_v3_closure_basis_preserved"),
            "PREREQUISITE_BASIS_MISSING",
        ),
        _make_check(
            "visible refusal preserved",
            bool(refusal.get("visible_refusal_preserved")),
            True,
            refusal.get("visible_refusal_preserved"),
            "VISIBLE_REFUSAL_NOT_PRESERVED",
        ),
        _make_check(
            "visible divergence preserved",
            bool(refusal.get("visible_divergence_preserved")),
            True,
            refusal.get("visible_divergence_preserved"),
            "VISIBLE_DIVERGENCE_NOT_PRESERVED",
        ),
        _make_check(
            "blocked attempts preserved",
            bool(refusal.get("blocked_attempts_preserved")),
            True,
            refusal.get("blocked_attempts_preserved"),
            "BLOCKED_ATTEMPT_NOT_PRESERVED",
        ),
        _make_check(
            "projection mismatch preserved",
            bool(refusal.get("projection_mismatch_preserved")),
            True,
            refusal.get("projection_mismatch_preserved"),
            "PROJECTION_MISMATCH_NOT_PRESERVED",
        ),
        _make_check(
            "detailed basis distinguished from summary",
            bool(refusal.get("detailed_basis_distinguished_from_summary")),
            True,
            refusal.get("detailed_basis_distinguished_from_summary"),
            "SUMMARY_OVERWRITES_DETAILED_BASIS",
        ),
        _make_check(
            "summary did not override detailed basis",
            bool(refusal.get("summary_did_not_override_detailed_basis")),
            True,
            refusal.get("summary_did_not_override_detailed_basis"),
            "SUMMARY_OVERWRITES_DETAILED_BASIS",
        ),
        _make_check(
            "source body lineage not replaced",
            bool(refusal.get("source_body_lineage_not_replaced")),
            True,
            refusal.get("source_body_lineage_not_replaced"),
            "SOURCE_REPLACED",
        ),
        _make_check(
            "no carrier currentness",
            bool(non_claim.get("no_carrier_currentness")),
            False,
            False if non_claim.get("no_carrier_currentness") else True,
            "CARRIER_CURRENTNESS_CREATED",
        ),
        _make_check(
            "no current carrier selected",
            bool(non_claim.get("no_current_carrier_selected")),
            False,
            False if non_claim.get("no_current_carrier_selected") else True,
            "CURRENT_CARRIER_SELECTED",
        ),
        _make_check(
            "no winning carrier selected",
            bool(non_claim.get("no_winning_carrier_selected")),
            False,
            False if non_claim.get("no_winning_carrier_selected") else True,
            "WINNING_CARRIER_SELECTED",
        ),
        _make_check(
            "no losing carrier invalidated",
            bool(non_claim.get("no_losing_carrier_invalidated")),
            False,
            False if non_claim.get("no_losing_carrier_invalidated") else True,
            "LOSING_CARRIER_INVALIDATED",
        ),
        _make_check(
            "no source replacement",
            bool(non_claim.get("no_source_replacement")),
            False,
            False if non_claim.get("no_source_replacement") else True,
            "SOURCE_REPLACED",
        ),
        _make_check(
            "no authority",
            bool(non_claim.get("no_authority")),
            False,
            False if non_claim.get("no_authority") else True,
            "AUTHORITY_CREATED",
        ),
        _make_check(
            "no permission",
            bool(non_claim.get("no_permission")),
            False,
            False if non_claim.get("no_permission") else True,
            "PERMISSION_CREATED",
        ),
        _make_check(
            "no truth",
            bool(non_claim.get("no_truth")),
            False,
            False if non_claim.get("no_truth") else True,
            "TRUTH_CREATED",
        ),
        _make_check(
            "no action",
            bool(non_claim.get("no_action")),
            False,
            False if non_claim.get("no_action") else True,
            "ACTION_AUTHORIZED",
        ),
        _make_check(
            "no divergence resolution",
            bool(non_claim.get("no_divergence_resolution")),
            False,
            False if non_claim.get("no_divergence_resolution") else True,
            "DIVERGENCE_RESOLVED",
        ),
        _make_check(
            "no evidence erasure",
            bool(non_claim.get("no_evidence_erasure")),
            False,
            False if non_claim.get("no_evidence_erasure") else True,
            "EVIDENCE_ERASED",
        ),
        _make_check(
            "no repository synchronization",
            bool(non_claim.get("no_repository_synchronization")),
            False,
            False if non_claim.get("no_repository_synchronization") else True,
            "REPOSITORY_SYNC_AUTHORIZED",
        ),
        _make_check(
            "no full body transfer",
            bool(non_claim.get("no_full_body_transfer")),
            False,
            False if non_claim.get("no_full_body_transfer") else True,
            "FULL_BODY_TRANSFER_AUTHORIZED",
        ),
        _make_check(
            "no second body",
            bool(non_claim.get("no_second_body")),
            False,
            False if non_claim.get("no_second_body") else True,
            "SECOND_BODY_CREATED",
        ),
        _make_check(
            "no continuation",
            bool(non_claim.get("no_continuation")),
            False,
            False if non_claim.get("no_continuation") else True,
            "CONTINUATION_AUTHORIZED",
        ),
        _make_check(
            "no distributed operation",
            bool(non_claim.get("no_distributed_operation")),
            False,
            False if non_claim.get("no_distributed_operation") else True,
            "DISTRIBUTED_OPERATION_AUTHORIZED",
        ),
        _make_check(
            "no latest file or latest turn standing",
            bool(non_claim.get("no_latest_file_standing"))
            and bool(non_claim.get("no_latest_turn_standing")),
            False,
            False
            if non_claim.get("no_latest_file_standing")
            and non_claim.get("no_latest_turn_standing")
            else True,
            "LATEST_OR_MAJORITY_STANDING_CREATED",
        ),
        _make_check(
            "no majority or success count standing",
            bool(non_claim.get("no_majority_standing"))
            and bool(non_claim.get("no_success_count_standing")),
            False,
            False
            if non_claim.get("no_majority_standing")
            and non_claim.get("no_success_count_standing")
            else True,
            "LATEST_OR_MAJORITY_STANDING_CREATED",
        ),
        _make_check(
            "no prerequisite created standing by itself",
            bool(non_claim.get("no_registry_standing_by_itself"))
            and bool(non_claim.get("no_lifecycle_standing_by_itself"))
            and bool(non_claim.get("no_standing_propagation_standing_by_itself"))
            and bool(non_claim.get("no_continuity_turn_standing_by_itself"))
            and bool(non_claim.get("no_currentness_successor_standing_by_itself"))
            and bool(non_claim.get("no_divergence_consequence_standing_by_itself")),
            False,
            False
            if bool(non_claim.get("no_registry_standing_by_itself"))
            and bool(non_claim.get("no_lifecycle_standing_by_itself"))
            and bool(non_claim.get("no_standing_propagation_standing_by_itself"))
            and bool(non_claim.get("no_continuity_turn_standing_by_itself"))
            and bool(non_claim.get("no_currentness_successor_standing_by_itself"))
            and bool(non_claim.get("no_divergence_consequence_standing_by_itself"))
            else True,
            "PREREQUISITE_CREATED_STANDING_BY_ITSELF",
        ),
        _make_check(
            "no mutation replay or merge",
            bool(non_claim.get("no_mutation"))
            and bool(non_claim.get("no_replay"))
            and bool(non_claim.get("no_merge")),
            False,
            False
            if non_claim.get("no_mutation") and non_claim.get("no_replay") and non_claim.get("no_merge")
            else True,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _make_check(
            "summary detail correspondence passed",
            bool(summary_detail.get("summary_detail_correspondence_passed")),
            True,
            summary_detail.get("summary_detail_correspondence_passed"),
            "SUMMARY_OVERWRITES_DETAILED_BASIS",
        ),
        _make_check(
            "declared request non claims remain false",
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
                "block_code": "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED",
                "block_reason": "Conformance request explicitly declared block intent.",
            },
        )

    if first_failure_code in BLOCKING_FAILURE_CODES:
        return (
            OUTCOME_BLOCKED,
            {
                "blocked": True,
                "block_code": first_failure_code,
                "block_reason": "Conformance could not lawfully proceed.",
            },
        )

    if intent == INTENT_DO_NOT_RECORD:
        return (
            OUTCOME_NOT_CONFORMANT,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "not_recorded_reason": "Request explicitly declined conformance recording.",
            },
        )

    if failed_checks:
        return (
            OUTCOME_NOT_CONFORMANT,
            {
                "blocked": False,
                "block_code": None,
                "block_reason": None,
                "not_conformant_reason": "Selected result failed one or more conformance checks.",
                "first_failure_code": first_failure_code,
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
    selected_section: Mapping[str, Any],
    prerequisite: Mapping[str, Any],
    refusal: Mapping[str, Any],
    non_claim: Mapping[str, Any],
    summary_detail: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    conformant = outcome == OUTCOME_CONFORMANT
    failed_checks = [check for check in checks if not check.get("passed")]
    statement = {
        "distributed_standing_boundary_conformant": conformant,
        "selected_result_preserved": bool(selected_section.get("selected_result_preserved")),
        "selected_result_identity_preserved": bool(
            selected_section.get("selected_result_identity_preserved")
        ),
        "selected_result_outcome_preserved": bool(
            selected_section.get("selected_result_outcome_preserved")
        ),
        "selected_result_is_distributed_standing_boundary": bool(
            selected_section.get("selected_result_is_distributed_standing_boundary")
        ),
        "prerequisite_basis_conformant": bool(prerequisite.get("prerequisite_basis_conformant")),
        "refusal_divergence_lineage_conformant": bool(
            refusal.get("refusal_divergence_lineage_conformant")
        ),
        "non_claim_conformant": bool(non_claim.get("non_claim_conformant")),
        "summary_detail_correspondence_passed": bool(
            summary_detail.get("summary_detail_correspondence_passed")
        ),
        "conformance_did_not_expand_result": True,
        "conformance_did_not_authorize_continuation": True,
        "conformance_did_not_authorize_repository_sync": True,
        "conformance_did_not_authorize_full_body_transfer": True,
        "conformance_did_not_create_second_body": True,
        "conformance_did_not_authorize_distributed_operation": True,
        "selected_result_mutated": False,
        "permission_created": False,
        "continuation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "distributed_operation_authorized": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_replaced": False,
        "truth_created": False,
        "action_authorized": False,
        "divergence_resolved": False,
        "evidence_erased": False,
        "failed_checks_preserved": _deepcopy(failed_checks),
    }
    return statement


def build_distributed_standing_boundary_conformance_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a conformance result."""

    checks = result.get("conformance_checks", [])
    checks_list = checks if isinstance(checks, list) else []
    passed_count = sum(1 for check in checks_list if isinstance(check, Mapping) and check.get("passed"))
    failed_count = sum(1 for check in checks_list if isinstance(check, Mapping) and not check.get("passed"))

    declared = result.get("declared_conformance_question", {})
    selected = result.get("selected_distributed_standing_boundary_result", {})
    statement = result.get("conformance_statement", {})
    block = result.get("block", {})
    non_claims = result.get("non_claims", {})

    selected_map = selected if isinstance(selected, Mapping) else {}
    statement_map = statement if isinstance(statement, Mapping) else {}
    declared_map = declared if isinstance(declared, Mapping) else {}
    block_map = block if isinstance(block, Mapping) else {}
    non_claim_map = non_claims if isinstance(non_claims, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code"),
        "block_reason": block_map.get("block_reason"),
        "conformance_request_id": declared_map.get("conformance_request_id"),
        "conformance_question": declared_map.get("conformance_question"),
        "conformance_intent": declared_map.get("conformance_intent"),
        "selected_distributed_standing_result_id": selected_map.get("selected_result_id"),
        "selected_distributed_standing_result_outcome": selected_map.get(
            "selected_result_outcome"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "distributed_standing_boundary_conformant": statement_map.get(
            "distributed_standing_boundary_conformant"
        ),
        "selected_result_preserved": statement_map.get("selected_result_preserved"),
        "selected_result_identity_preserved": statement_map.get(
            "selected_result_identity_preserved"
        ),
        "selected_result_outcome_preserved": statement_map.get(
            "selected_result_outcome_preserved"
        ),
        "selected_result_is_distributed_standing_boundary": statement_map.get(
            "selected_result_is_distributed_standing_boundary"
        ),
        "prerequisite_basis_conformant": statement_map.get("prerequisite_basis_conformant"),
        "refusal_divergence_lineage_conformant": statement_map.get(
            "refusal_divergence_lineage_conformant"
        ),
        "non_claim_conformant": statement_map.get("non_claim_conformant"),
        "summary_detail_correspondence_passed": statement_map.get(
            "summary_detail_correspondence_passed"
        ),
        "conformance_did_not_expand_result": statement_map.get(
            "conformance_did_not_expand_result"
        ),
        "conformance_did_not_authorize_continuation": statement_map.get(
            "conformance_did_not_authorize_continuation"
        ),
        "conformance_did_not_authorize_repository_sync": statement_map.get(
            "conformance_did_not_authorize_repository_sync"
        ),
        "conformance_did_not_authorize_full_body_transfer": statement_map.get(
            "conformance_did_not_authorize_full_body_transfer"
        ),
        "conformance_did_not_create_second_body": statement_map.get(
            "conformance_did_not_create_second_body"
        ),
        "conformance_did_not_authorize_distributed_operation": statement_map.get(
            "conformance_did_not_authorize_distributed_operation"
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
            )
        },
    }


def _build_result(
    request: Mapping[str, Any],
    request_path: str | None,
    selected_result: Mapping[str, Any],
    selected_result_path: str | None,
    selected_load_failures: Sequence[str],
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    declared = _declared_question_section(request, request_path)
    selected_section = _build_selected_result_section(
        request,
        selected_result,
        selected_result_path,
        selected_load_failures,
    )
    selected_basis = _build_selected_result_basis(request)
    prerequisite = _build_prerequisite_basis_conformance(selected_result)
    refusal = _build_refusal_divergence_lineage_conformance(selected_result)
    non_claim = _build_non_claim_conformance(selected_result)
    summary_detail = _build_summary_detail_correspondence(selected_result)

    checks = _build_conformance_checks(
        request,
        selected_section,
        selected_basis,
        prerequisite,
        refusal,
        non_claim,
        summary_detail,
        precheck_failures,
    )
    outcome, block = _decide_outcome(request.get("conformance_intent"), checks)
    statement = _build_conformance_statement(
        outcome,
        selected_section,
        prerequisite,
        refusal,
        non_claim,
        summary_detail,
        checks,
    )

    result_id = _first_present(
        request.get("conformance_request_id"),
        selected_section.get("selected_result_id"),
        "distributed_standing_boundary_conformance",
    )

    result = {
        "distributed_standing_boundary_conformance_metadata": {
            "conformance_result_id": f"{result_id}__distributed_standing_boundary_conformance",
            "conformance_result_type": RESULT_TYPE,
            "conformance_result_version": RESULT_VERSION,
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_conformance_question": declared,
        "selected_distributed_standing_boundary_result": selected_section,
        "selected_result_basis": selected_basis,
        "prerequisite_basis_conformance": prerequisite,
        "refusal_divergence_lineage_conformance": refusal,
        "non_claim_conformance": non_claim,
        "summary_detail_correspondence": summary_detail,
        "conformance_checks": checks,
        "conformance_statement": statement,
        "conformance_non_meaning": _deepcopy(CONFORMANCE_NON_MEANING),
        "what_remains_open": _deepcopy(OPEN_ITEMS),
        "non_claims": _result_non_claims(request),
        "outcome": outcome,
        "block": block,
    }
    result["distributed_standing_boundary_conformance_summary"] = (
        build_distributed_standing_boundary_conformance_summary(result)
    )
    return result


def resolve_distributed_standing_boundary_conformance(
    declared_conformance_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded distributed standing boundary conformance request."""

    if declared_conformance_request is None:
        request: dict[str, Any] = {}
        precheck_failures: list[str] = []
    elif not isinstance(declared_conformance_request, Mapping):
        request = {}
        precheck_failures = ["DECLARED_CONFORMANCE_REQUEST_MALFORMED"]
    else:
        request = _deepcopy(_as_plain_mapping(declared_conformance_request))
        precheck_failures = []

    selected_result, selected_result_path, selected_load_failures = _load_selected_result(request)
    return _build_result(
        request,
        None,
        selected_result,
        selected_result_path,
        selected_load_failures,
        precheck_failures,
    )


def resolve_distributed_standing_boundary_conformance_from_path(
    declared_conformance_request_path: Path | str,
) -> dict:
    """Load a JSON object request from path and resolve conformance."""

    path = _to_path(declared_conformance_request_path)
    try:
        request = _read_json_object(
            path,
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
        )
        precheck_failures: list[str] = []
    except DistributedStandingBoundaryConformanceError as exc:
        request = {}
        precheck_failures = [exc.block_code]

    selected_result, selected_result_path, selected_load_failures = _load_selected_result(request)
    return _build_result(
        request,
        str(path),
        selected_result,
        selected_result_path,
        selected_load_failures,
        precheck_failures,
    )


def _safe_filename_part(value: Any) -> str:
    text = str(value or "distributed_standing_boundary_conformance").strip()
    cleaned = []
    for character in text:
        if character.isalnum() or character in ("-", "_"):
            cleaned.append(character)
        else:
            cleaned.append("_")
    filename = "".join(cleaned).strip("_").lower()
    return filename or "distributed_standing_boundary_conformance"


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


def write_distributed_standing_boundary_conformance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive conformance result artifact as stable UTF-8 JSON."""

    result_copy = _deepcopy(dict(result))
    if output_path is None:
        summary = result_copy.get("distributed_standing_boundary_conformance_summary", {})
        request_id = summary.get("conformance_request_id") if isinstance(summary, Mapping) else None
        selected_id = (
            summary.get("selected_distributed_standing_result_id")
            if isinstance(summary, Mapping)
            else None
        )
        filename_root = _safe_filename_part(_first_present(request_id, selected_id))
        output = (
            DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_ROOT
            / f"{filename_root}__distributed_standing_boundary_conformance_result.json"
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


def build_declared_distributed_standing_boundary_conformance_request(
    conformance_request_id: str,
    conformance_question: str,
    selected_distributed_standing_boundary_result: Mapping[str, Any] | str,
    selected_result_basis: Mapping[str, Any] | str,
    conformance_intent: str = INTENT_RECORD,
    *,
    selected_result_path: str | None = None,
    selected_result_id: str | None = None,
    selected_result_outcome: str | None = None,
    expected_selected_result_outcome: str = EXPECTED_SELECTED_RESULT_OUTCOME,
) -> dict:
    """Build a bounded declared conformance request with required false non-claims."""

    request = {
        "conformance_request_id": conformance_request_id,
        "conformance_question": conformance_question,
        "conformance_intent": conformance_intent,
        "selected_distributed_standing_boundary_result": _deepcopy(
            selected_distributed_standing_boundary_result
        ),
        "selected_result_basis": _deepcopy(selected_result_basis),
        "selected_result_id": selected_result_id,
        "selected_result_outcome": selected_result_outcome,
        "expected_selected_result_outcome": expected_selected_result_outcome,
        "declared_non_claims": _deepcopy(REQUIRED_NON_CLAIMS),
    }

    if selected_result_path is not None:
        request["selected_result_path"] = selected_result_path

    return request
