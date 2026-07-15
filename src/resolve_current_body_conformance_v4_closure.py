"""Bounded current-body conformance v4 closure resolver.

This module closes the meaning of one selected conformant current-body
conformance v4 result. It records closure of meaning only. It does not create
current self-orientation v10, authorize continuation or operation, synchronize
repositories, transfer the body, create a second body, create permission,
create truth or action, claim final completion, create public readiness, or
schedule follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentBodyConformanceV4ClosureError(Exception):
    """Raised for impossible internal closure-shape contradictions."""


REPO_ROOT = Path(__file__).resolve().parents[1]
CURRENT_BODY_CONFORMANCE_V4_CLOSURE_ROOT = (
    REPO_ROOT
    / "artifacts"
    / "integrity_host_v0_min_coexistence_current_body_conformance_v4_closure"
)

RESOLVER_MODULE = "resolve_current_body_conformance_v4_closure"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "current_body_conformance_v4_closure_result"

INTENT_RECORD = "RECORD_CURRENT_BODY_CONFORMANCE_V4_CLOSURE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_CURRENT_BODY_CONFORMANCE_V4_CLOSURE"
INTENT_BLOCK = "BLOCK_CURRENT_BODY_CONFORMANCE_V4_CLOSURE"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

OUTCOME_CLOSED = "CURRENT_BODY_CONFORMANCE_V4_CLOSED"
OUTCOME_NOT_CLOSED = "CURRENT_BODY_CONFORMANCE_V4_NOT_CLOSED"
OUTCOME_BLOCKED = "CURRENT_BODY_CONFORMANCE_V4_CLOSURE_BLOCKED"

EXPECTED_SELECTED_V4_OUTCOME = "CURRENT_BODY_CONFORMANCE_V4_CONFORMANT"
EXPECTED_SELECTED_V9_OUTCOME = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
EXPECTED_FAILED_CHECK_COUNT = 0

REQUIRED_NON_CLAIMS = (
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
    "current_self_orientation_v10_created",
    "closure_created_v10",
    "closure_authorized_continuation",
    "closure_authorized_operation",
    "closure_claimed_final_completion",
    "closure_erased_not_conformant_result",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

CLOSURE_COLLAPSE_FIELDS = {
    "current_self_orientation_v10_created": "CLOSURE_CREATES_CURRENT_SELF_ORIENTATION_V10",
    "closure_created_v10": "CLOSURE_CREATES_CURRENT_SELF_ORIENTATION_V10",
    "continuation_authorized": "CLOSURE_AUTHORIZES_CONTINUATION",
    "closure_authorized_continuation": "CLOSURE_AUTHORIZES_CONTINUATION",
    "operation_authorized": "CLOSURE_AUTHORIZES_OPERATION",
    "distributed_operation_authorized": "CLOSURE_AUTHORIZES_OPERATION",
    "closure_authorized_operation": "CLOSURE_AUTHORIZES_OPERATION",
    "repository_synchronization_authorized": "CLOSURE_AUTHORIZES_REPOSITORY_SYNC",
    "full_body_transfer_authorized": "CLOSURE_AUTHORIZES_FULL_BODY_TRANSFER",
    "second_body_created": "CLOSURE_CREATES_SECOND_BODY",
    "permission_created": "CLOSURE_CREATES_PERMISSION",
    "authority_created": "CLOSURE_CREATES_AUTHORITY",
    "truth_created": "CLOSURE_CREATES_TRUTH_OR_ACTION",
    "action_authorized": "CLOSURE_CREATES_TRUTH_OR_ACTION",
    "final_completion_claimed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "final_continuity_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "final_governance_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "final_system_identity_completed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "closure_claimed_final_completion": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "public_launch_readiness_created": "CLOSURE_CREATES_PUBLIC_READINESS",
    "follow_on_work_authorized": "CLOSURE_SCHEDULES_FOLLOW_ON_WORK",
    "self_orientation_successor_scheduled": "CLOSURE_SCHEDULES_FOLLOW_ON_WORK",
    "selected_v4_mutated": "CLOSURE_MUTATES_V4",
    "closure_mutated_v4": "CLOSURE_MUTATES_V4",
    "selected_v9_mutated": "CLOSURE_MUTATES_V9",
    "closure_mutated_v9": "CLOSURE_MUTATES_V9",
    "selected_v8_mutated": "CLOSURE_MUTATES_V8",
    "closure_mutated_v8": "CLOSURE_MUTATES_V8",
    "closure_erased_not_conformant_result": "CLOSURE_ERASES_PRIOR_NOT_CONFORMANT_RESULT",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    try:
        parsed = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, "unreadable"
    if not isinstance(parsed, dict):
        return None, "malformed"
    return parsed, None


def _get_nested(mapping: Mapping[str, Any], paths: Sequence[Sequence[str]]) -> Any:
    for path in paths:
        current: Any = mapping
        found = True
        for key in path:
            if not isinstance(current, Mapping) or key not in current:
                found = False
                break
            current = current[key]
        if found:
            return current
    return None


def _truthy(mapping: Mapping[str, Any] | None, *keys: str) -> bool:
    if not isinstance(mapping, Mapping):
        return False
    for key in keys:
        if mapping.get(key) is True:
            return True
    return False


def _explicit_false(mapping: Mapping[str, Any] | None, key: str) -> bool:
    return isinstance(mapping, Mapping) and mapping.get(key) is False


def _non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, (str, bytes, Sequence, Mapping)) and len(value) == 0:
        return False
    return True


def _failed_check_count_from_checks(checks: Any) -> int | None:
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes)):
        return None
    failed = 0
    saw_check = False
    for check in checks:
        if isinstance(check, Mapping):
            saw_check = True
            if check.get("passed") is not True:
                failed += 1
    return failed if saw_check else None


def _selected_v4_id(v4: Mapping[str, Any], request: Mapping[str, Any]) -> Any:
    return _get_nested(
        request,
        (("selected_current_body_conformance_v4_id",),),
    ) or _get_nested(
        v4,
        (
            ("current_body_conformance_v4_metadata", "current_body_conformance_v4_result_id"),
            ("current_body_conformance_v4_summary", "current_body_conformance_v4_result_id"),
            ("metadata", "current_body_conformance_v4_result_id"),
            ("conformance_request_id",),
            ("id",),
        ),
    )


def _selected_v4_outcome(v4: Mapping[str, Any], request: Mapping[str, Any]) -> Any:
    return _get_nested(
        v4,
        (
            ("outcome",),
            ("current_body_conformance_v4_summary", "outcome"),
            ("summary", "outcome"),
        ),
    ) or _get_nested(
        request,
        (("selected_current_body_conformance_v4_outcome",),),
    )


def _selected_v4_failed_count(v4: Mapping[str, Any], request: Mapping[str, Any]) -> int | None:
    value = _get_nested(
        v4,
        (
            ("current_body_conformance_v4_summary", "failed_check_count"),
            ("summary", "failed_check_count"),
            ("failed_check_count",),
        ),
    )
    if value is not None and not isinstance(value, bool):
        try:
            return int(value)
        except (TypeError, ValueError):
            return None
    return _failed_check_count_from_checks(v4.get("conformance_checks"))


def _selected_v9(v4: Mapping[str, Any], request: Mapping[str, Any]) -> Mapping[str, Any] | None:
    candidate = request.get("selected_current_self_orientation_v9")
    if isinstance(candidate, Mapping):
        return candidate
    candidate = v4.get("selected_current_self_orientation_v9")
    return candidate if isinstance(candidate, Mapping) else None


def _selected_v9_id(v4: Mapping[str, Any], request: Mapping[str, Any]) -> Any:
    v9 = _selected_v9(v4, request) or {}
    return _get_nested(
        v4,
        (
            ("current_body_conformance_v4_summary", "selected_v9_id"),
            ("conformance_statement", "selected_v9_id"),
        ),
    ) or _get_nested(
        v9,
        (
            ("current_self_orientation_v9_metadata", "current_self_orientation_v9_result_id"),
            ("current_self_orientation_v9_summary", "current_self_orientation_v9_result_id"),
            ("id",),
        ),
    )


def _selected_v9_outcome(v4: Mapping[str, Any], request: Mapping[str, Any]) -> Any:
    v9 = _selected_v9(v4, request) or {}
    return _get_nested(
        v4,
        (
            ("current_body_conformance_v4_summary", "selected_v9_outcome"),
            ("conformance_statement", "selected_v9_outcome"),
        ),
    ) or _get_nested(v9, (("outcome",), ("current_self_orientation_v9_summary", "outcome")))


def _selected_v4_is_type(v4: Mapping[str, Any]) -> bool:
    result_type = _get_nested(
        v4,
        (
            ("current_body_conformance_v4_metadata", "current_body_conformance_v4_result_type"),
            ("metadata", "current_body_conformance_v4_result_type"),
        ),
    )
    module = _get_nested(
        v4,
        (
            ("current_body_conformance_v4_metadata", "resolver_module"),
            ("metadata", "resolver_module"),
        ),
    )
    if result_type == "current_body_conformance_v4_result":
        return True
    if module == "resolve_current_body_conformance_v4":
        return True
    return {
        "conformance_checks",
        "conformance_statement",
        "current_body_conformance_v4_summary",
    }.issubset(set(v4.keys()))


def _statement(v4: Mapping[str, Any]) -> Mapping[str, Any]:
    value = v4.get("conformance_statement")
    return value if isinstance(value, Mapping) else {}


def _summary(v4: Mapping[str, Any]) -> Mapping[str, Any]:
    value = v4.get("current_body_conformance_v4_summary")
    return value if isinstance(value, Mapping) else {}


def _section(v4: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = v4.get(key)
    return value if isinstance(value, Mapping) else {}


def _selected_v4_bool(
    v4: Mapping[str, Any],
    *keys: str,
    default: bool = False,
) -> bool:
    for source in (_statement(v4), _summary(v4), v4):
        for key in keys:
            if source.get(key) is True:
                return True
    return default


def _selected_v4_false(
    v4: Mapping[str, Any],
    *keys: str,
    default: bool = False,
) -> bool:
    for source in (_statement(v4), _summary(v4), v4):
        for key in keys:
            if source.get(key) is False:
                return True
    return default


def _selected_v9_failed_count_zero(v4: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    if _selected_v4_bool(v4, "selected_v9_failed_check_count_zero"):
        return True
    v9 = _selected_v9(v4, request)
    if isinstance(v9, Mapping):
        failed = _get_nested(
            v9,
            (
                ("current_self_orientation_v9_summary", "failed_check_count"),
                ("summary", "failed_check_count"),
                ("failed_check_count",),
            ),
        )
        if failed is not None:
            return failed == 0
    return False


def _all_required_non_claims_false(non_claims: Mapping[str, Any] | None) -> bool:
    return isinstance(non_claims, Mapping) and all(
        non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS
    )


def _result_non_claims(request: Mapping[str, Any] | None = None) -> dict[str, bool]:
    declared = request.get("declared_non_claims") if isinstance(request, Mapping) else None
    preserved = {key: False for key in REQUIRED_NON_CLAIMS}
    if isinstance(declared, Mapping):
        for key in REQUIRED_NON_CLAIMS:
            preserved[key] = bool(declared.get(key)) if declared.get(key) is True else False
    return preserved


def _first_collapse_code(request: Mapping[str, Any]) -> str | None:
    containers: list[Mapping[str, Any]] = [request]
    for key in ("selected_v4_closure_basis", "closure_scope", "declared_non_claims"):
        value = request.get(key)
        if isinstance(value, Mapping):
            containers.append(value)
    for container in containers:
        if container.get("mutation_performed") is True:
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
        if container.get("replay_performed") is True:
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
        if container.get("merge_performed") is True:
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
        for field, code in CLOSURE_COLLAPSE_FIELDS.items():
            if container.get(field) is True:
                return code
    return None


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    failure_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "failure_code": None if passed else failure_code,
    }


def _closure_non_meaning() -> dict[str, bool]:
    return {
        "not_current_self_orientation_v10": True,
        "not_continuation": True,
        "not_operation": True,
        "not_repository_synchronization": True,
        "not_full_body_transfer": True,
        "not_second_body": True,
        "not_distributed_standing_implementation": True,
        "not_distributed_operation": True,
        "not_final_completion": True,
        "not_final_governance": True,
        "not_final_continuity_completion": True,
        "not_final_system_identity": True,
        "not_public_launch_readiness": True,
        "not_permission": True,
        "not_authority": True,
        "not_truth": True,
        "not_action": True,
        "not_currentness": True,
        "not_carrier_currentness": True,
        "not_current_carrier_selected": True,
        "not_winning_carrier_selected": True,
        "not_losing_carrier_invalidated": True,
        "not_source_replacement": True,
        "not_divergence_resolution": True,
        "not_evidence_erasure": True,
        "not_refusal_erasure": True,
        "not_blocked_attempt_erasure": True,
        "not_projection_mismatch_erasure": True,
        "not_mutation_of_v9": True,
        "not_mutation_of_v8": True,
        "not_mutation_of_v4_conformance_artifact": True,
        "not_mutation_of_prior_not_conformant_v4_artifact": True,
        "not_erasure_of_prior_not_conformant_v4_lineage": True,
        "not_follow_on_work_authorization": True,
    }


def _v4_non_meaning() -> dict[str, bool]:
    return {
        "v4_conformance_is_not_current_self_orientation_v10": True,
        "v4_conformance_is_not_continuation": True,
        "v4_conformance_is_not_operation": True,
        "v4_conformance_is_not_repository_synchronization": True,
        "v4_conformance_is_not_full_body_transfer": True,
        "v4_conformance_is_not_second_body_creation": True,
        "v4_conformance_is_not_final_completion": True,
        "v4_conformance_is_not_final_governance": True,
        "v4_conformance_is_not_final_continuity_completion": True,
        "v4_conformance_is_not_final_system_identity": True,
        "v4_conformance_is_not_public_launch_readiness": True,
        "v4_conformance_is_not_permission": True,
        "v4_conformance_is_not_authority": True,
        "v4_conformance_is_not_truth_action": True,
        "v4_conformance_is_not_follow_on_work_authorization": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "future_self_orientation_successor_beyond_v9": "open_not_scheduled_not_authorized_not_executed",
        "current_self_orientation_v10_only_if_separately_declared_and_bounded": "open_not_scheduled_not_authorized_not_executed",
        "distributed_standing_implementation": "open_not_scheduled_not_authorized_not_executed",
        "distributed_operation": "open_not_scheduled_not_authorized_not_executed",
        "repository_synchronization": "open_not_scheduled_not_authorized_not_executed",
        "full_body_transfer": "open_not_scheduled_not_authorized_not_executed",
        "second_body_creation": "open_not_scheduled_not_authorized_not_executed",
        "carrier_registry_implementation": "open_not_scheduled_not_authorized_not_executed",
        "persistence_implementation": "open_not_scheduled_not_authorized_not_executed",
        "standing_propagation_implementation_beyond_boundary_recording": "open_not_scheduled_not_authorized_not_executed",
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


def _load_selected_v4(request: Mapping[str, Any]) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = request.get("selected_current_body_conformance_v4_path")
    selected = request.get("selected_current_body_conformance_v4")
    if path:
        parsed, error = _read_json_object(path)
        if error == "unreadable":
            return None, "CURRENT_BODY_CONFORMANCE_V4_UNREADABLE", str(path)
        if error == "malformed":
            return None, "CURRENT_BODY_CONFORMANCE_V4_MALFORMED", str(path)
        return _deepcopy(parsed), None, str(path)
    if isinstance(selected, str):
        parsed, error = _read_json_object(selected)
        if error == "unreadable":
            return None, "CURRENT_BODY_CONFORMANCE_V4_UNREADABLE", selected
        if error == "malformed":
            return None, "CURRENT_BODY_CONFORMANCE_V4_MALFORMED", selected
        return _deepcopy(parsed), None, selected
    if selected is None:
        return None, "CURRENT_BODY_CONFORMANCE_V4_MISSING", None
    if not isinstance(selected, Mapping):
        return None, "CURRENT_BODY_CONFORMANCE_V4_MALFORMED", None
    return _deepcopy(dict(selected)), None, None


def _metadata(request: Mapping[str, Any], selected_v4_id: Any) -> dict[str, Any]:
    request_id = request.get("closure_request_id") or selected_v4_id or "undeclared"
    return {
        "current_body_conformance_v4_closure_result_id": (
            f"{request_id}__current_body_conformance_v4_closure_result"
        ),
        "current_body_conformance_v4_closure_result_type": RESULT_TYPE,
        "current_body_conformance_v4_closure_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question(request: Mapping[str, Any], request_path: str | None = None) -> dict[str, Any]:
    return {
        "closure_request_id": request.get("closure_request_id"),
        "closure_question": request.get("closure_question"),
        "closure_intent": request.get("closure_intent"),
        "declared_non_claims": _deepcopy(request.get("declared_non_claims")),
        "declared_closure_request_path": request_path,
        "closure_is_not_permission": True,
        "closure_is_not_continuation": True,
        "closure_is_not_operation": True,
        "closure_is_not_final_completion": True,
        "closure_is_not_current_self_orientation_v10": True,
        "closure_does_not_mutate_what_it_closes": True,
    }


def _selected_v4_section(
    v4: Mapping[str, Any] | None,
    request: Mapping[str, Any],
    path: str | None,
) -> dict[str, Any]:
    if v4 is None:
        return {
            "selected_current_body_conformance_v4_path": path,
            "selected_v4_preserved": False,
        }
    outcome = _selected_v4_outcome(v4, request)
    failed = _selected_v4_failed_count(v4, request)
    return {
        "selected_current_body_conformance_v4_result": _deepcopy(v4),
        "selected_current_body_conformance_v4_path": path,
        "selected_current_body_conformance_v4_id": _selected_v4_id(v4, request),
        "selected_current_body_conformance_v4_outcome": outcome,
        "selected_current_body_conformance_v4_result_type": _get_nested(
            v4,
            (
                ("current_body_conformance_v4_metadata", "current_body_conformance_v4_result_type"),
                ("metadata", "current_body_conformance_v4_result_type"),
            ),
        ),
        "selected_v4_preserved": True,
        "selected_v4_is_current_body_conformance_v4": _selected_v4_is_type(v4),
        "selected_v4_conformant": outcome == EXPECTED_SELECTED_V4_OUTCOME,
        "selected_v4_failed_check_count": failed,
        "selected_v4_failed_check_count_zero": failed == EXPECTED_FAILED_CHECK_COUNT,
        "selected_v4_not_mutated": True,
    }


def _v4_meaning(v4: Mapping[str, Any] | None, request: Mapping[str, Any]) -> dict[str, Any]:
    if v4 is None:
        return {}
    meaning = {
        "selected_v9_preserved": _selected_v4_bool(v4, "selected_v9_preserved"),
        "selected_v9_identity_preserved": _selected_v4_bool(v4, "selected_v9_identity_preserved"),
        "selected_v9_outcome_preserved": _selected_v4_bool(v4, "selected_v9_outcome_preserved"),
        "selected_v9_is_current_self_orientation_v9": _selected_v4_bool(
            v4, "selected_v9_is_current_self_orientation_v9"
        ),
        "selected_v9_recorded": _selected_v4_bool(v4, "selected_v9_recorded"),
        "selected_v9_failed_check_count_zero": _selected_v9_failed_count_zero(v4, request),
        "v9_orientation_conformant": _selected_v4_bool(v4, "v9_orientation_conformant"),
        "basis_preservation_conformant": _selected_v4_bool(v4, "basis_preservation_conformant"),
        "non_claim_conformant": _selected_v4_bool(v4, "non_claim_conformant"),
        "conformance_did_not_mutate_v9": _selected_v4_bool(
            v4, "conformance_did_not_mutate_v9"
        ),
        "conformance_did_not_authorize_continuation": _selected_v4_bool(
            v4, "conformance_did_not_authorize_continuation"
        ),
        "conformance_did_not_authorize_operation": _selected_v4_bool(
            v4, "conformance_did_not_authorize_operation"
        ),
        "conformance_did_not_create_permission": _selected_v4_bool(
            v4, "conformance_did_not_create_permission"
        ),
        "conformance_did_not_claim_final_completion": _selected_v4_bool(
            v4, "conformance_did_not_claim_final_completion"
        ),
        "conformance_did_not_schedule_follow_on_work": _selected_v4_bool(
            v4, "conformance_did_not_schedule_follow_on_work"
        ),
        "v4_conformance_can_be_relied_on_as_conformance_not_permission": True,
        "v4_conformance_may_be_preserved_as_closed_meaning_only": True,
    }
    selected_v9 = _selected_v9(v4, request)
    if selected_v9 is not None:
        meaning["selected_current_self_orientation_v9"] = _deepcopy(selected_v9)
        meaning["selected_v9_id"] = _selected_v9_id(v4, request)
        meaning["selected_v9_outcome"] = _selected_v9_outcome(v4, request)
    return meaning


def _lineage_preservation(
    request: Mapping[str, Any],
    v4: Mapping[str, Any] | None,
) -> dict[str, Any]:
    basis = request.get("selected_v4_closure_basis")
    basis_mapping = basis if isinstance(basis, Mapping) else {}
    prior_not_conformant = request.get("prior_not_conformant_v4_result")
    prior_visible = prior_not_conformant is not None
    v9_present = v4 is not None and _selected_v9(v4, request) is not None
    return {
        "v8_remains_prior_lineage": bool(
            request.get("selected_prior_self_orientation_v8")
            or basis_mapping.get("v8_remains_prior_lineage")
            or basis_mapping.get("current_self_orientation_v8")
        ),
        "v9_remains_selected_orientation": bool(
            request.get("selected_current_self_orientation_v9")
            or v9_present
            or basis_mapping.get("v9_remains_selected_orientation")
        ),
        "current_body_conformance_v3_closure_remains_basis": bool(
            request.get("current_body_conformance_v3_closure_basis")
            or basis_mapping.get("current_body_conformance_v3_closure_basis_preserved")
            or basis_mapping.get("current_body_conformance_v3_closure")
        ),
        "distributed_standing_boundary_conformance_closure_remains_closed_meaning_basis": bool(
            request.get("distributed_standing_boundary_conformance_closure_basis")
            or basis_mapping.get(
                "distributed_standing_boundary_conformance_closure_basis_preserved"
            )
            or basis_mapping.get("distributed_standing_boundary_conformance_closure")
        ),
        "prior_not_conformant_v4_result_remains_visible": prior_visible,
        "prior_not_conformant_v4_result": _deepcopy(prior_not_conformant),
        "closure_does_not_erase_failed_or_not_conformant_attempts": True,
        "closure_does_not_hide_refusal_blocked_attempts_or_projection_mismatch": True,
        "closure_does_not_mutate_v4_v9_v8_or_prior_artifacts": True,
    }


def _checks(
    request: Mapping[str, Any],
    v4: Mapping[str, Any] | None,
    selected_path: str | None,
    load_code: str | None,
    meaning: Mapping[str, Any],
    lineage: Mapping[str, Any],
) -> list[dict[str, Any]]:
    closure_intent = request.get("closure_intent")
    declared_non_claims = request.get("declared_non_claims")
    v4_id = _selected_v4_id(v4, request) if v4 is not None else None
    v4_outcome = _selected_v4_outcome(v4, request) if v4 is not None else None
    failed = _selected_v4_failed_count(v4, request) if v4 is not None else None
    checks = [
        _make_check(
            "closure question declared",
            bool(request.get("closure_question")),
            "declared closure question",
            request.get("closure_question"),
            "CLOSURE_QUESTION_UNDECLARED",
        ),
        _make_check(
            "closure intent supported",
            closure_intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            closure_intent,
            "CLOSURE_INTENT_UNSUPPORTED",
        ),
        _make_check(
            "selected v4 artifact present",
            v4 is not None,
            "selected current-body conformance v4 result",
            "present" if v4 is not None else "missing",
            load_code or "CURRENT_BODY_CONFORMANCE_V4_MISSING",
        ),
        _make_check(
            "selected v4 artifact identity present",
            bool(v4_id),
            "selected v4 identity declared or exposed",
            v4_id,
            "CURRENT_BODY_CONFORMANCE_V4_IDENTITY_MISSING",
        ),
        _make_check(
            "selected v4 artifact outcome present",
            bool(v4_outcome),
            "selected v4 outcome declared or exposed",
            v4_outcome,
            "CURRENT_BODY_CONFORMANCE_V4_OUTCOME_MISSING",
        ),
        _make_check(
            "selected v4 artifact readable or parseable",
            load_code is None,
            "readable JSON object where path supplied",
            selected_path if selected_path else "mapping supplied",
            load_code or "CURRENT_BODY_CONFORMANCE_V4_MALFORMED",
        ),
        _make_check(
            "selected v4 artifact is current-body conformance v4 result",
            v4 is not None and _selected_v4_is_type(v4),
            "current-body conformance v4 result",
            _selected_v4_is_type(v4) if v4 is not None else False,
            "CURRENT_BODY_CONFORMANCE_V4_MALFORMED",
        ),
        _make_check(
            "selected v4 outcome is conformant",
            v4_outcome == EXPECTED_SELECTED_V4_OUTCOME,
            EXPECTED_SELECTED_V4_OUTCOME,
            v4_outcome,
            "CURRENT_BODY_CONFORMANCE_V4_NOT_CONFORMANT",
        ),
        _make_check(
            "selected v4 failed check count is zero",
            failed == EXPECTED_FAILED_CHECK_COUNT,
            EXPECTED_FAILED_CHECK_COUNT,
            failed,
            "CURRENT_BODY_CONFORMANCE_V4_HAS_FAILED_CHECKS",
        ),
    ]

    meaning_specs = (
        ("selected v9 preserved", "selected_v9_preserved", "CURRENT_SELF_ORIENTATION_V9_MISSING"),
        ("selected v9 recorded", "selected_v9_recorded", "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"),
        (
            "selected v9 failed check count zero",
            "selected_v9_failed_check_count_zero",
            "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS",
        ),
        (
            "v9 orientation conformant",
            "v9_orientation_conformant",
            "V9_ORIENTATION_CONFORMANCE_MISSING_OR_FALSE",
        ),
        (
            "basis preservation conformant",
            "basis_preservation_conformant",
            "BASIS_PRESERVATION_CONFORMANCE_MISSING_OR_FALSE",
        ),
        (
            "non-claim conformant",
            "non_claim_conformant",
            "NON_CLAIM_CONFORMANCE_MISSING_OR_FALSE",
        ),
        (
            "conformance did not mutate v9",
            "conformance_did_not_mutate_v9",
            "CONFORMANCE_MUTATED_V9",
        ),
        (
            "conformance did not authorize continuation",
            "conformance_did_not_authorize_continuation",
            "CONFORMANCE_AUTHORIZED_CONTINUATION",
        ),
        (
            "conformance did not authorize operation",
            "conformance_did_not_authorize_operation",
            "CONFORMANCE_AUTHORIZED_OPERATION",
        ),
        (
            "conformance did not create permission",
            "conformance_did_not_create_permission",
            "CONFORMANCE_CREATED_PERMISSION",
        ),
        (
            "conformance did not claim final completion",
            "conformance_did_not_claim_final_completion",
            "CONFORMANCE_CLAIMED_FINAL_COMPLETION",
        ),
        (
            "conformance did not schedule follow-on work",
            "conformance_did_not_schedule_follow_on_work",
            "CONFORMANCE_SCHEDULED_FOLLOW_ON_WORK",
        ),
    )
    for check_name, key, code in meaning_specs:
        checks.append(_make_check(check_name, meaning.get(key) is True, True, meaning.get(key), code))

    lineage_specs = (
        ("v8 remains prior lineage where exposed", "v8_remains_prior_lineage"),
        ("v9 remains selected orientation", "v9_remains_selected_orientation"),
        (
            "current-body conformance v3 closure remains basis where exposed",
            "current_body_conformance_v3_closure_remains_basis",
        ),
        (
            "distributed standing boundary conformance closure remains closed meaning basis",
            "distributed_standing_boundary_conformance_closure_remains_closed_meaning_basis",
        ),
        (
            "closure does not erase failed or not-conformant attempts",
            "closure_does_not_erase_failed_or_not_conformant_attempts",
        ),
    )
    for check_name, key in lineage_specs:
        checks.append(
            _make_check(
                check_name,
                lineage.get(key) is True,
                True,
                lineage.get(key),
                "CLOSURE_ERASES_PRIOR_NOT_CONFORMANT_RESULT"
                if "erase" in check_name
                else "CURRENT_BODY_CONFORMANCE_V4_MALFORMED",
            )
        )

    collapse_specs = (
        ("closure does not create current self-orientation v10", "current_self_orientation_v10_created", "CLOSURE_CREATES_CURRENT_SELF_ORIENTATION_V10"),
        ("closure does not authorize continuation", "closure_authorized_continuation", "CLOSURE_AUTHORIZES_CONTINUATION"),
        ("closure does not authorize operation", "closure_authorized_operation", "CLOSURE_AUTHORIZES_OPERATION"),
        ("closure does not authorize repository synchronization", "repository_synchronization_authorized", "CLOSURE_AUTHORIZES_REPOSITORY_SYNC"),
        ("closure does not authorize full body transfer", "full_body_transfer_authorized", "CLOSURE_AUTHORIZES_FULL_BODY_TRANSFER"),
        ("closure does not create second body", "second_body_created", "CLOSURE_CREATES_SECOND_BODY"),
        ("closure does not create permission", "permission_created", "CLOSURE_CREATES_PERMISSION"),
        ("closure does not create authority", "authority_created", "CLOSURE_CREATES_AUTHORITY"),
        ("closure does not create truth or action", "truth_created", "CLOSURE_CREATES_TRUTH_OR_ACTION"),
        ("closure does not claim final completion", "closure_claimed_final_completion", "CLOSURE_CLAIMS_FINAL_COMPLETION"),
        ("closure does not create public readiness", "public_launch_readiness_created", "CLOSURE_CREATES_PUBLIC_READINESS"),
        ("closure does not schedule follow-on work", "follow_on_work_authorized", "CLOSURE_SCHEDULES_FOLLOW_ON_WORK"),
        ("closure does not schedule self-orientation successor", "self_orientation_successor_scheduled", "CLOSURE_SCHEDULES_FOLLOW_ON_WORK"),
        ("closure does not mutate v4", "closure_mutated_v4", "CLOSURE_MUTATES_V4"),
        ("closure does not mutate v9", "closure_mutated_v9", "CLOSURE_MUTATES_V9"),
        ("closure does not mutate v8", "closure_mutated_v8", "CLOSURE_MUTATES_V8"),
        (
            "closure does not erase prior not-conformant result",
            "closure_erased_not_conformant_result",
            "CLOSURE_ERASES_PRIOR_NOT_CONFORMANT_RESULT",
        ),
    )
    for check_name, field, code in collapse_specs:
        actual = request.get(field)
        if actual is None and isinstance(request.get("selected_v4_closure_basis"), Mapping):
            actual = request["selected_v4_closure_basis"].get(field)
        if actual is None and isinstance(declared_non_claims, Mapping):
            actual = declared_non_claims.get(field)
        checks.append(_make_check(check_name, actual is not True, False, actual is True, code))

    mutation_detected = any(
        request.get(key) is True
        or (
            isinstance(request.get("selected_v4_closure_basis"), Mapping)
            and request["selected_v4_closure_basis"].get(key) is True
        )
        or (isinstance(declared_non_claims, Mapping) and declared_non_claims.get(key) is True)
        for key in ("mutation_performed", "replay_performed", "merge_performed")
    )
    checks.append(
        _make_check(
            "no mutation replay or merge",
            not mutation_detected,
            False,
            mutation_detected,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
    )
    checks.append(
        _make_check(
            "required non-claims remain false",
            _all_required_non_claims_false(declared_non_claims),
            {key: False for key in REQUIRED_NON_CLAIMS},
            _deepcopy(declared_non_claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("failure_code")
            if code:
                return str(code)
    return None


def _statement_for(
    outcome: str,
    request: Mapping[str, Any],
    v4: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    meaning: Mapping[str, Any],
    lineage: Mapping[str, Any],
) -> dict[str, Any]:
    failed = sum(1 for check in checks if check.get("passed") is not True)
    closed = outcome == OUTCOME_CLOSED
    statement = {
        "current_body_conformance_v4_closed": closed,
        "selected_v4_preserved": v4 is not None,
        "selected_v4_identity_preserved": bool(_selected_v4_id(v4, request)) if v4 is not None else False,
        "selected_v4_outcome_preserved": bool(_selected_v4_outcome(v4, request)) if v4 is not None else False,
        "selected_v4_is_current_body_conformance_v4": _selected_v4_is_type(v4) if v4 is not None else False,
        "selected_v4_conformant": (
            _selected_v4_outcome(v4, request) == EXPECTED_SELECTED_V4_OUTCOME
            if v4 is not None
            else False
        ),
        "selected_v4_failed_check_count_zero": (
            _selected_v4_failed_count(v4, request) == EXPECTED_FAILED_CHECK_COUNT
            if v4 is not None
            else False
        ),
        "selected_v9_preserved": meaning.get("selected_v9_preserved") is True,
        "selected_v9_recorded": meaning.get("selected_v9_recorded") is True,
        "v9_orientation_conformant": meaning.get("v9_orientation_conformant") is True,
        "basis_preservation_conformant": meaning.get("basis_preservation_conformant") is True,
        "non_claim_conformant": meaning.get("non_claim_conformant") is True,
        "v4_conformance_meaning_preserved": bool(meaning),
        "v4_conformance_non_meaning_preserved": True,
        "lineage_preservation_passed": lineage.get("closure_does_not_erase_failed_or_not_conformant_attempts") is True,
        "closure_did_not_create_v10": True,
        "closure_did_not_authorize_continuation": True,
        "closure_did_not_authorize_operation": True,
        "closure_did_not_authorize_repository_sync": True,
        "closure_did_not_authorize_full_body_transfer": True,
        "closure_did_not_create_second_body": True,
        "closure_did_not_create_permission": True,
        "closure_did_not_claim_final_completion": True,
        "closure_did_not_create_public_readiness": True,
        "closure_did_not_schedule_follow_on_work": True,
        "closure_did_not_mutate_v4": True,
        "closure_did_not_mutate_v9": True,
        "closure_did_not_erase_prior_not_conformant_result": True,
        "failed_check_count": failed,
    }
    if outcome == OUTCOME_NOT_CLOSED:
        statement["not_closed_reason"] = request.get("not_closed_reason") or _first_failed_code(checks)
    if outcome == OUTCOME_BLOCKED:
        statement["current_body_conformance_v4_closed"] = False
    return statement


def _block(outcome: str, code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": outcome == OUTCOME_BLOCKED,
        "block_code": code if outcome == OUTCOME_BLOCKED else None,
        "block_reason": reason if outcome == OUTCOME_BLOCKED else None,
    }


def _base_result(
    request: Mapping[str, Any],
    outcome: str,
    block_code: str | None,
    checks: Sequence[Mapping[str, Any]],
    selected_v4: Mapping[str, Any] | None,
    selected_v4_path: str | None,
    meaning: Mapping[str, Any],
    lineage: Mapping[str, Any],
    request_path: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    selected_id = _selected_v4_id(selected_v4, request) if selected_v4 is not None else None
    result = {
        "current_body_conformance_v4_closure_metadata": _metadata(request, selected_id),
        "declared_closure_question": _declared_question(request, request_path),
        "selected_current_body_conformance_v4": _selected_v4_section(
            selected_v4, request, selected_v4_path
        ),
        "selected_v4_closure_basis": _deepcopy(request.get("selected_v4_closure_basis")),
        "v4_conformance_meaning": _deepcopy(meaning),
        "v4_conformance_non_meaning": _v4_non_meaning(),
        "lineage_preservation": _deepcopy(lineage),
        "closure_checks": list(checks),
        "closure_statement": _statement_for(outcome, request, selected_v4, checks, meaning, lineage),
        "closure_non_meaning": _closure_non_meaning(),
        "what_remains_open": _what_remains_open(),
        "non_claims": _result_non_claims(request),
        "outcome": outcome,
        "block": _block(outcome, block_code, block_reason),
    }
    result["current_body_conformance_v4_closure_summary"] = (
        build_current_body_conformance_v4_closure_summary(result)
    )
    return result


def _blocked_result(
    request: Mapping[str, Any] | None,
    code: str,
    reason: str,
    request_path: str | None = None,
    selected_v4: Mapping[str, Any] | None = None,
    selected_v4_path: str | None = None,
) -> dict[str, Any]:
    request = request if isinstance(request, Mapping) else {}
    meaning = _v4_meaning(selected_v4, request)
    lineage = _lineage_preservation(request, selected_v4)
    checks = [
        _make_check(
            "closure blocked",
            False,
            "lawful closure request and selected conformant v4",
            reason,
            code,
        )
    ]
    return _base_result(
        request,
        OUTCOME_BLOCKED,
        code,
        checks,
        selected_v4,
        selected_v4_path,
        meaning,
        lineage,
        request_path,
        reason,
    )


def resolve_current_body_conformance_v4_closure(
    declared_closure_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve closure of meaning for one selected current-body conformance v4 result."""

    if declared_closure_request is None:
        return _blocked_result(
            {},
            "CLOSURE_QUESTION_UNDECLARED",
            "No declared closure request was supplied.",
        )
    if not isinstance(declared_closure_request, Mapping):
        return _blocked_result(
            {},
            "DECLARED_CLOSURE_REQUEST_MALFORMED",
            "Declared closure request must be a mapping.",
        )

    request: dict[str, Any] = _deepcopy(dict(declared_closure_request))
    if not request.get("closure_question"):
        return _blocked_result(
            request,
            "CLOSURE_QUESTION_UNDECLARED",
            "Closure question is undeclared.",
        )
    if request.get("closure_intent") == INTENT_BLOCK:
        return _blocked_result(
            request,
            "CLOSURE_REQUEST_EXPLICITLY_BLOCKED",
            request.get("block_reason") or "Closure request explicitly blocked.",
        )
    if request.get("closure_intent") not in SUPPORTED_INTENTS:
        return _blocked_result(
            request,
            "CLOSURE_INTENT_UNSUPPORTED",
            "Closure intent is unsupported.",
        )

    selected_v4, load_code, selected_path = _load_selected_v4(request)
    if load_code in {
        "CURRENT_BODY_CONFORMANCE_V4_MISSING",
        "CURRENT_BODY_CONFORMANCE_V4_UNREADABLE",
        "CURRENT_BODY_CONFORMANCE_V4_MALFORMED",
    }:
        return _blocked_result(request, load_code, load_code, selected_v4_path=selected_path)

    if selected_v4 is None:
        return _blocked_result(
            request,
            "CURRENT_BODY_CONFORMANCE_V4_MISSING",
            "Selected current-body conformance v4 result is missing.",
        )

    identity = _selected_v4_id(selected_v4, request)
    outcome = _selected_v4_outcome(selected_v4, request)
    if not identity:
        return _blocked_result(
            request,
            "CURRENT_BODY_CONFORMANCE_V4_IDENTITY_MISSING",
            "Selected current-body conformance v4 identity is missing.",
            selected_v4=selected_v4,
            selected_v4_path=selected_path,
        )
    if not outcome:
        return _blocked_result(
            request,
            "CURRENT_BODY_CONFORMANCE_V4_OUTCOME_MISSING",
            "Selected current-body conformance v4 outcome is missing.",
            selected_v4=selected_v4,
            selected_v4_path=selected_path,
        )

    meaning = _v4_meaning(selected_v4, request)
    lineage = _lineage_preservation(request, selected_v4)
    checks = _checks(request, selected_v4, selected_path, load_code, meaning, lineage)
    failed_code = _first_failed_code(checks)
    collapse_code = _first_collapse_code(request)

    if collapse_code:
        return _base_result(
            request,
            OUTCOME_BLOCKED,
            collapse_code,
            checks,
            selected_v4,
            selected_path,
            meaning,
            lineage,
            block_reason=collapse_code,
        )

    if request.get("closure_intent") == INTENT_DO_NOT_RECORD:
        return _base_result(
            request,
            OUTCOME_NOT_CLOSED,
            None,
            checks,
            selected_v4,
            selected_path,
            meaning,
            lineage,
            block_reason=None,
        )

    if failed_code:
        return _base_result(
            request,
            OUTCOME_NOT_CLOSED,
            None,
            checks,
            selected_v4,
            selected_path,
            meaning,
            lineage,
        )

    return _base_result(
        request,
        OUTCOME_CLOSED,
        None,
        checks,
        selected_v4,
        selected_path,
        meaning,
        lineage,
    )


def resolve_current_body_conformance_v4_closure_from_path(
    declared_closure_request_path: Path | str,
) -> dict:
    """Load a declared closure request JSON object and resolve it."""

    path = Path(declared_closure_request_path)
    parsed, error = _read_json_object(path)
    if error == "unreadable":
        return _blocked_result(
            {},
            "DECLARED_CLOSURE_REQUEST_UNREADABLE",
            "Declared closure request path is unreadable or malformed JSON.",
            str(path),
        )
    if error == "malformed":
        return _blocked_result(
            {},
            "DECLARED_CLOSURE_REQUEST_MALFORMED",
            "Declared closure request JSON must be an object.",
            str(path),
        )
    request = _deepcopy(parsed)
    request["declared_closure_request_path"] = str(path)
    result = resolve_current_body_conformance_v4_closure(request)
    result["declared_closure_question"]["declared_closure_request_path"] = str(path)
    result["current_body_conformance_v4_closure_summary"] = (
        build_current_body_conformance_v4_closure_summary(result)
    )
    return result


def build_current_body_conformance_v4_closure_summary(result: Mapping[str, Any]) -> dict:
    """Build a bounded summary for a v4 closure result artifact."""

    checks = result.get("closure_checks")
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes)):
        checks = []
    passed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True)
    failed = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True)
    statement = result.get("closure_statement")
    statement = statement if isinstance(statement, Mapping) else {}
    selected = result.get("selected_current_body_conformance_v4")
    selected = selected if isinstance(selected, Mapping) else {}
    meaning = result.get("v4_conformance_meaning")
    meaning = meaning if isinstance(meaning, Mapping) else {}
    declared = result.get("declared_closure_question")
    declared = declared if isinstance(declared, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "closure_request_id": declared.get("closure_request_id"),
        "closure_question": declared.get("closure_question"),
        "closure_intent": declared.get("closure_intent"),
        "selected_v4_id": selected.get("selected_current_body_conformance_v4_id"),
        "selected_v4_outcome": selected.get("selected_current_body_conformance_v4_outcome"),
        "selected_v9_id": meaning.get("selected_v9_id"),
        "selected_v9_outcome": meaning.get("selected_v9_outcome"),
        "passed_check_count": passed,
        "failed_check_count": failed,
        "current_body_conformance_v4_closed": statement.get(
            "current_body_conformance_v4_closed", False
        ),
        "selected_v4_preserved": statement.get("selected_v4_preserved", False),
        "selected_v4_identity_preserved": statement.get(
            "selected_v4_identity_preserved", False
        ),
        "selected_v4_outcome_preserved": statement.get(
            "selected_v4_outcome_preserved", False
        ),
        "selected_v4_is_current_body_conformance_v4": statement.get(
            "selected_v4_is_current_body_conformance_v4", False
        ),
        "selected_v4_conformant": statement.get("selected_v4_conformant", False),
        "selected_v4_failed_check_count_zero": statement.get(
            "selected_v4_failed_check_count_zero", False
        ),
        "selected_v9_preserved": statement.get("selected_v9_preserved", False),
        "selected_v9_recorded": statement.get("selected_v9_recorded", False),
        "v9_orientation_conformant": statement.get("v9_orientation_conformant", False),
        "basis_preservation_conformant": statement.get(
            "basis_preservation_conformant", False
        ),
        "non_claim_conformant": statement.get("non_claim_conformant", False),
        "v4_conformance_meaning_preserved": statement.get(
            "v4_conformance_meaning_preserved", False
        ),
        "v4_conformance_non_meaning_preserved": statement.get(
            "v4_conformance_non_meaning_preserved", False
        ),
        "lineage_preservation_passed": statement.get("lineage_preservation_passed", False),
        "closure_did_not_create_v10": statement.get("closure_did_not_create_v10", False),
        "closure_did_not_authorize_continuation": statement.get(
            "closure_did_not_authorize_continuation", False
        ),
        "closure_did_not_authorize_operation": statement.get(
            "closure_did_not_authorize_operation", False
        ),
        "closure_did_not_authorize_repository_sync": statement.get(
            "closure_did_not_authorize_repository_sync", False
        ),
        "closure_did_not_authorize_full_body_transfer": statement.get(
            "closure_did_not_authorize_full_body_transfer", False
        ),
        "closure_did_not_create_second_body": statement.get(
            "closure_did_not_create_second_body", False
        ),
        "closure_did_not_create_permission": statement.get(
            "closure_did_not_create_permission", False
        ),
        "closure_did_not_claim_final_completion": statement.get(
            "closure_did_not_claim_final_completion", False
        ),
        "closure_did_not_create_public_readiness": statement.get(
            "closure_did_not_create_public_readiness", False
        ),
        "closure_did_not_schedule_follow_on_work": statement.get(
            "closure_did_not_schedule_follow_on_work", False
        ),
        "closure_did_not_mutate_v4": statement.get("closure_did_not_mutate_v4", False),
        "closure_did_not_mutate_v9": statement.get("closure_did_not_mutate_v9", False),
        "closure_did_not_erase_prior_not_conformant_result": statement.get(
            "closure_did_not_erase_prior_not_conformant_result", False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "permission_created",
                "continuation_authorized",
                "distributed_operation_authorized",
                "repository_synchronization_authorized",
                "full_body_transfer_authorized",
                "second_body_created",
                "current_self_orientation_v10_created",
                "final_governance_completed",
                "public_launch_readiness_created",
                "follow_on_work_authorized",
                "mutation_performed",
            )
        },
    }


def _safe_filename_part(value: Any) -> str:
    text = str(value or "current_body_conformance_v4_closure")
    safe = []
    for char in text:
        safe.append(char if char.isalnum() or char in {"-", "_"} else "_")
    return "".join(safe).strip("_") or "current_body_conformance_v4_closure"


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


def write_current_body_conformance_v4_closure_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a v4 closure result as additive UTF-8 JSON without overwriting."""

    if not isinstance(result, Mapping):
        raise CurrentBodyConformanceV4ClosureError("result must be a mapping")
    if output_path is None:
        summary = result.get("current_body_conformance_v4_closure_summary")
        summary = summary if isinstance(summary, Mapping) else {}
        request_id = summary.get("closure_request_id") or summary.get("selected_v4_id")
        filename = f"{_safe_filename_part(request_id)}__current_body_conformance_v4_closure_result.json"
        output = CURRENT_BODY_CONFORMANCE_V4_CLOSURE_ROOT / filename
    else:
        output = Path(output_path)
    output = _non_overwriting_path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    return output


def build_declared_current_body_conformance_v4_closure_request(
    closure_request_id: str,
    closure_question: str,
    selected_current_body_conformance_v4: Mapping[str, Any] | str,
    selected_v4_closure_basis: Mapping[str, Any] | str,
    closure_intent: str = INTENT_RECORD,
    *,
    selected_current_body_conformance_v4_path: str | None = None,
    selected_current_body_conformance_v4_id: str | None = None,
    selected_current_body_conformance_v4_outcome: str | None = None,
    expected_selected_v4_outcome: str = EXPECTED_SELECTED_V4_OUTCOME,
    selected_current_self_orientation_v9: Mapping[str, Any] | str | None = None,
    prior_not_conformant_v4_result: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded declared v4 closure request with required non-claims false."""

    request = {
        "closure_request_id": closure_request_id,
        "closure_question": closure_question,
        "closure_intent": closure_intent,
        "selected_current_body_conformance_v4": _deepcopy(
            selected_current_body_conformance_v4
        ),
        "selected_v4_closure_basis": _deepcopy(selected_v4_closure_basis),
        "expected_selected_v4_outcome": expected_selected_v4_outcome,
        "expected_failed_check_count": EXPECTED_FAILED_CHECK_COUNT,
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
    if selected_current_body_conformance_v4_path is not None:
        request["selected_current_body_conformance_v4_path"] = (
            selected_current_body_conformance_v4_path
        )
    if selected_current_body_conformance_v4_id is not None:
        request["selected_current_body_conformance_v4_id"] = (
            selected_current_body_conformance_v4_id
        )
    if selected_current_body_conformance_v4_outcome is not None:
        request["selected_current_body_conformance_v4_outcome"] = (
            selected_current_body_conformance_v4_outcome
        )
    if selected_current_self_orientation_v9 is not None:
        request["selected_current_self_orientation_v9"] = _deepcopy(
            selected_current_self_orientation_v9
        )
    if prior_not_conformant_v4_result is not None:
        request["prior_not_conformant_v4_result"] = _deepcopy(
            prior_not_conformant_v4_result
        )
    return request
