"""Carrier registry/persistence boundary resolver v2.

This is a lineage-preserving successor to
``resolve_carrier_registry_persistence_boundary``. V1 remains standing and its
artifacts remain untouched. V2 exists for one narrow reason: the v1 result body
could preserve lifecycle reference evidence inside nested registry/persistence
basis while the summary projected ``lifecycle_reference_preserved`` as false.

V2 keeps the same boundary and outcome family, writes only to a v2 output root,
and improves projection so statement and summary fields correspond to detailed
basis, referenced artifact, and explicit reference preservation. It is still a
reference-preservation boundary only: no registry implementation, persistence
engine, database, authority, currentness, distributed standing, synchronization,
full body transfer, continuation, distributed operation, or evidence erasure is
created here.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CarrierRegistryPersistenceBoundaryV2Error(Exception):
    """Hard failure for malformed or unreadable explicit v2 inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_carrier_registry_persistence_boundary_v2"
)

RESOLVER_MODULE = "resolve_carrier_registry_persistence_boundary_v2"
SUCCESSOR_OF_MODULE = "resolve_carrier_registry_persistence_boundary"
RESULT_VERSION = "0.2.0"
RESULT_TYPE = "carrier_registry_persistence_boundary_v2_result"

RECORD_INTENT = "RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY"
BLOCK_INTENT = "BLOCK_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY"
SUPPORTED_REGISTRY_INTENTS = {
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
}

CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED = (
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED"
)
CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED = (
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED"
)
CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED = (
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED"
)

SUPPORTED_RECORD_CATEGORIES = {
    "CARRIER_IDENTITY_RECORD",
    "CARRIER_LIFECYCLE_STATUS_RECORD",
    "CARRIER_EVIDENCE_REFERENCE_RECORD",
    "CARRIER_RELATION_REFERENCE_RECORD",
    "CARRIER_DIVERGENCE_REFERENCE_RECORD",
    "CARRIER_CURRENTNESS_PARTICIPATION_REFERENCE_RECORD",
    "CARRIER_EXPERIMENT_REFERENCE_RECORD",
    "CARRIER_INTEGRITY_REFERENCE_RECORD",
    "CARRIER_REGISTRY_NON_CLAIM_RECORD",
    "CARRIER_REGISTRY_BLOCK_RECORD",
}

CATEGORIES_REQUIRING_SELECTED_CARRIER = {
    "CARRIER_IDENTITY_RECORD",
    "CARRIER_LIFECYCLE_STATUS_RECORD",
}

CATEGORIES_REQUIRING_REFERENCED_ARTIFACT = {
    "CARRIER_EVIDENCE_REFERENCE_RECORD",
    "CARRIER_RELATION_REFERENCE_RECORD",
    "CARRIER_DIVERGENCE_REFERENCE_RECORD",
    "CARRIER_CURRENTNESS_PARTICIPATION_REFERENCE_RECORD",
    "CARRIER_EXPERIMENT_REFERENCE_RECORD",
    "CARRIER_INTEGRITY_REFERENCE_RECORD",
}

SUPPORTED_LIFECYCLE_STATUSES = {
    "CARRIER_CANDIDATE",
    "CARRIER_DECLARED_FOR_EXPERIMENT",
    "CARRIER_ACTIVE_FOR_OPERATION",
    "CARRIER_HOLDING_EVIDENCE",
    "CARRIER_RETURNED_EVIDENCE",
    "CARRIER_REFUSED_OR_BLOCKED",
    "CARRIER_UNAVAILABLE",
    "CARRIER_STALE",
    "CARRIER_CORRUPTED",
    "CARRIER_WITHDRAWN",
    "CARRIER_REPLACED",
    "CARRIER_REINTRODUCTION_CANDIDATE",
    "CARRIER_REINTRODUCED",
    "CARRIER_RETIRED",
    "CARRIER_LIFECYCLE_BLOCKED",
}

REQUIRED_NON_CLAIMS: dict[str, bool] = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "registry_created_source": False,
    "registry_created_currentness": False,
    "registry_created_authority": False,
    "registry_created_permission": False,
    "registry_created_carrier_hierarchy": False,
    "registry_created_distributed_standing": False,
    "registry_authorized_sync": False,
    "registry_authorized_full_body_transfer": False,
    "registry_created_second_body": False,
    "registry_authorized_continuation": False,
    "registry_authorized_distributed_operation": False,
    "registry_erased_evidence": False,
    "registry_hid_refusal": False,
    "registry_hid_divergence": False,
    "registry_hid_corruption": False,
    "registry_repaired_by_overwrite": False,
    "current_carrier_selected": False,
    "winning_carrier_selected": False,
    "losing_carrier_invalidated": False,
    "distributed_standing_created": False,
    "carrier_registry_created_as_authority": False,
    "repository_synchronization_authorized": False,
    "full_body_transfer_authorized": False,
    "second_body_created": False,
    "continuation_authorized": False,
    "distributed_operation_authorized": False,
    "latest_record_currentness": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
}

BLOCK_REASONS = {
    "DECLARED_REGISTRY_REQUEST_UNREADABLE": "Declared registry/persistence request path could not be read.",
    "DECLARED_REGISTRY_REQUEST_MALFORMED": "Declared registry/persistence request is not a JSON object or mapping.",
    "REGISTRY_QUESTION_UNDECLARED": "Registry question is undeclared.",
    "PERSISTENCE_PURPOSE_UNDECLARED": "Persistence purpose is undeclared.",
    "REGISTRY_INTENT_UNSUPPORTED": "Registry intent is unsupported.",
    "REGISTRY_REQUEST_EXPLICITLY_BLOCKED": "Registry/persistence request explicitly declares a blocked posture.",
    "CARRIER_IDENTITY_MISSING": "Carrier identity is missing where required.",
    "RECORD_CATEGORY_UNSUPPORTED": "Selected record category is missing or unsupported.",
    "REFERENCED_ARTIFACT_MISSING": "Referenced artifact is missing where required.",
    "REFERENCED_ARTIFACT_MALFORMED": "Referenced artifact is malformed.",
    "REFERENCED_ARTIFACT_IDENTITY_MISSING": "Referenced artifact identity is missing.",
    "REFERENCED_ARTIFACT_OUTCOME_MISSING": "Referenced artifact outcome is missing.",
    "REGISTRY_DECIDES_SOURCE": "Registry/persistence decides source.",
    "REGISTRY_DECIDES_CURRENTNESS": "Registry/persistence decides currentness.",
    "REGISTRY_CREATES_AUTHORITY": "Registry/persistence creates authority.",
    "REGISTRY_CREATES_PERMISSION": "Registry/persistence creates permission.",
    "REGISTRY_CREATES_CARRIER_HIERARCHY": "Registry/persistence creates carrier hierarchy.",
    "REGISTRY_SELECTS_CURRENT_CARRIER": "Registry/persistence selects a current carrier.",
    "REGISTRY_SELECTS_WINNING_CARRIER": "Registry/persistence selects a winning carrier.",
    "REGISTRY_INVALIDATES_LOSING_CARRIER": "Registry/persistence invalidates a losing carrier.",
    "REGISTRY_RESOLVES_DIVERGENCE": "Registry/persistence resolves divergence.",
    "REGISTRY_ERASES_EVIDENCE": "Registry/persistence erases evidence.",
    "REGISTRY_HIDES_REFUSAL": "Registry/persistence hides refusal.",
    "REGISTRY_HIDES_DIVERGENCE": "Registry/persistence hides divergence or mismatch.",
    "REGISTRY_HIDES_CORRUPTION": "Registry/persistence hides corruption.",
    "REGISTRY_REPAIRS_BY_OVERWRITE": "Registry/persistence repairs by overwrite.",
    "REGISTRY_CREATES_DISTRIBUTED_STANDING": "Registry/persistence creates distributed standing.",
    "REGISTRY_AUTHORIZES_REPOSITORY_SYNC": "Registry/persistence authorizes repository synchronization.",
    "REGISTRY_AUTHORIZES_FULL_BODY_TRANSFER": "Registry/persistence authorizes full body transfer.",
    "REGISTRY_CREATES_SECOND_BODY": "Registry/persistence creates a second body.",
    "REGISTRY_AUTHORIZES_CONTINUATION": "Registry/persistence authorizes continuation.",
    "REGISTRY_AUTHORIZES_DISTRIBUTED_OPERATION": "Registry/persistence authorizes distributed operation.",
    "LATEST_RECORD_CURRENTNESS": "Latest-record recency is treated as currentness.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency or recency fraud is treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required registry/persistence non-claim is missing or flipped.",
}

REGISTRY_PERSISTENCE_NON_MEANING = {
    "does_not_mean_source": True,
    "does_not_mean_currentness": True,
    "does_not_mean_authority": True,
    "does_not_mean_permission": True,
    "does_not_mean_standing": True,
    "does_not_mean_truth": True,
    "does_not_mean_action": True,
    "does_not_mean_carrier_hierarchy": True,
    "does_not_mean_current_carrier_selected": True,
    "does_not_mean_winning_carrier_selected": True,
    "does_not_mean_losing_carrier_invalidated": True,
    "does_not_mean_divergence_resolved": True,
    "does_not_mean_evidence_erased": True,
    "does_not_mean_repair_by_overwrite": True,
    "does_not_mean_distributed_standing": True,
    "does_not_mean_repository_synchronization": True,
    "does_not_mean_full_body_transfer": True,
    "does_not_mean_second_body": True,
    "does_not_mean_distributed_operation": True,
    "does_not_mean_continuation": True,
    "does_not_mean_future_experiments_authorized": True,
    "does_not_mean_latest_record_currentness": True,
    "does_not_mean_completeness_authority": True,
    "does_not_mean_availability_priority": True,
    "does_not_mean_majority_currentness": True,
    "does_not_mean_registry_presence_as_standing": True,
    "does_not_mean_registry_absence_as_invalidation": True,
}

WHAT_REMAINS_OPEN = {
    "carrier_registry_implementation": True,
    "persistence_implementation": True,
    "standing_propagation_law": True,
    "cross_carrier_currentness_successor_law": True,
    "divergence_consequence_law": True,
    "distributed_standing_boundary": True,
    "distributed_standing": True,
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

DEFAULT_PERSISTENCE_PRESERVATION_RULES = {
    "referenced_artifact_identity_preserved": True,
    "referenced_artifact_outcome_preserved": True,
    "carrier_identity_preserved_where_available": True,
    "lifecycle_posture_preserved_where_available": True,
    "relation_posture_preserved_where_available": True,
    "divergence_posture_preserved_where_available": True,
    "currentness_participation_posture_preserved_where_available": True,
    "admission_posture_preserved_where_available": True,
    "receipt_or_refusal_posture_preserved_where_available": True,
    "non_claims_preserved": True,
    "does_not_mutate_referenced_artifact": True,
    "does_not_repair_by_overwrite": True,
    "does_not_hide_blocked_refused_corrupted_or_stale_posture": True,
    "latest_persisted_record_not_current": True,
    "older_records_not_erased_without_retention_boundary": True,
}

DEFAULT_REGISTRY_NON_AUTHORITY_RULES = {
    "registry_presence_is_not_standing": True,
    "registry_absence_is_not_invalidation": True,
    "registry_freshness_is_not_currentness": True,
    "registry_completeness_is_not_authority": True,
    "registry_majority_is_not_truth": True,
    "registry_availability_is_not_priority": True,
    "registry_order_is_not_rank": True,
    "registry_label_is_not_role": True,
    "registry_role_history_is_not_permanent_role": True,
    "registry_lifecycle_status_is_not_source": True,
    "registry_lifecycle_status_is_not_currentness": True,
    "registry_lifecycle_status_is_not_permission": True,
}


def resolve_carrier_registry_persistence_boundary(
    declared_registry_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded carrier registry/persistence request in v2."""

    if declared_registry_request is None:
        return _resolve_registry_persistence({}, None, [])
    if not isinstance(declared_registry_request, Mapping):
        return _resolve_registry_persistence(
            {},
            None,
            ["DECLARED_REGISTRY_REQUEST_MALFORMED"],
        )
    return _resolve_registry_persistence(copy.deepcopy(dict(declared_registry_request)), None, [])


def resolve_carrier_registry_persistence_boundary_from_path(
    declared_registry_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded carrier registry/persistence request from JSON."""

    path = Path(declared_registry_request_path)
    try:
        request = _read_json_mapping(path)
    except CarrierRegistryPersistenceBoundaryV2Error as exc:
        return _resolve_registry_persistence({}, path, [exc.block_code])
    return _resolve_registry_persistence(request, path, [])


def write_carrier_registry_persistence_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive v2 result without overwriting existing files."""

    if not isinstance(result, Mapping):
        raise CarrierRegistryPersistenceBoundaryV2Error(
            "DECLARED_REGISTRY_REQUEST_MALFORMED",
            "Carrier registry/persistence result must be a mapping.",
        )

    if output_path is None:
        summary = _as_mapping(result.get("carrier_registry_persistence_summary"))
        basis_id = (
            summary.get("registry_request_id")
            or summary.get("selected_record_category")
            or "carrier_registry_persistence"
        )
        output_path = CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_ROOT / (
            f"{_safe_filename_part(basis_id)}__carrier_registry_persistence_v2_result.json"
        )

    target = _non_overwriting_path(Path(output_path))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False, default=str)
        + "\n",
        encoding="utf-8",
    )
    return target


def build_carrier_registry_persistence_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a v2 summary from the full result body, not shallow fields only."""

    checks = _mapping_list(result.get("registry_persistence_checks"))
    question = _as_mapping(result.get("declared_registry_question"))
    purpose = _purpose_from_result(result)
    category = _category_from_result(result)
    selected_carrier = _as_mapping(result.get("selected_carrier"))
    artifacts = _as_mapping(result.get("selected_referenced_artifacts"))
    basis = _as_mapping(result.get("registry_persistence_basis"))
    statement = _as_mapping(result.get("registry_persistence_statement"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    projection = _projection_from_result(result)
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "registry_request_id": question.get("registry_request_id"),
        "registry_question": question.get("registry_question"),
        "persistence_purpose": purpose.get("persistence_purpose"),
        "registry_intent": question.get("registry_intent"),
        "selected_record_category": category.get("selected_record_category"),
        "selected_carrier_id": selected_carrier.get("selected_carrier_id"),
        "selected_referenced_artifact_ids": artifacts.get("referenced_artifact_ids"),
        "selected_referenced_artifact_outcomes": artifacts.get(
            "referenced_artifact_outcomes"
        ),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "carrier_registry_persistence_boundary_recorded": bool(
            statement.get("carrier_registry_persistence_boundary_recorded")
        ),
        "referenced_artifact_identity_preserved": projection[
            "referenced_artifact_identity_preserved"
        ],
        "referenced_artifact_outcome_preserved": projection[
            "referenced_artifact_outcome_preserved"
        ],
        "lifecycle_reference_preserved": projection["lifecycle_reference_preserved"],
        "relation_reference_preserved": projection["relation_reference_preserved"],
        "divergence_reference_preserved": projection["divergence_reference_preserved"],
        "currentness_participation_reference_preserved": projection[
            "currentness_participation_reference_preserved"
        ],
        "evidence_reference_preserved": projection["evidence_reference_preserved"],
        "non_claims_preserved": bool(
            statement.get("non_claims_preserved")
            or _required_non_claims_false(non_claims)
        ),
        "no_source_currentness_authority_permission": not bool(
            statement.get("registry_created_source")
            or statement.get("registry_created_currentness")
            or statement.get("registry_created_authority")
            or statement.get("registry_created_permission")
        ),
        "no_carrier_hierarchy": not bool(
            statement.get("registry_created_carrier_hierarchy")
        ),
        "no_current_winning_losing_carrier_collapse": not bool(
            statement.get("current_carrier_selected")
            or statement.get("winning_carrier_selected")
            or statement.get("losing_carrier_invalidated")
        ),
        "no_divergence_resolution": not bool(statement.get("divergence_resolved")),
        "no_evidence_erasure": not bool(statement.get("registry_erased_evidence")),
        "no_hidden_refusal_divergence_corruption": not bool(
            statement.get("registry_hid_refusal")
            or statement.get("registry_hid_divergence")
            or statement.get("registry_hid_corruption")
        ),
        "no_distributed_standing": not bool(
            statement.get("registry_created_distributed_standing")
        ),
        "no_sync_full_body_transfer_second_body": not bool(
            statement.get("registry_authorized_sync")
            or statement.get("registry_authorized_full_body_transfer")
            or statement.get("registry_created_second_body")
        ),
        "no_continuation": not bool(statement.get("registry_authorized_continuation")),
        "no_distributed_operation": not bool(
            statement.get("registry_authorized_distributed_operation")
        ),
        "no_latest_record_file_currentness": not bool(
            statement.get("latest_record_currentness")
            or statement.get("latest_file_currentness")
        ),
        "key_non_claims": _key_non_claims(non_claims),
        "registry_persistence_basis": basis.get("raw_registry_persistence_basis"),
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def build_declared_carrier_registry_persistence_request(
    registry_request_id: str,
    registry_question: str,
    persistence_purpose: str,
    selected_record_category: str,
    registry_intent: str = RECORD_INTENT,
    *,
    selected_carrier: Mapping[str, Any] | None = None,
    selected_referenced_artifacts: Sequence[Mapping[str, Any]] | None = None,
    registry_persistence_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    """Build one bounded v2 request without inferring authority or standing."""

    request: dict[str, Any] = {
        "registry_request_id": registry_request_id,
        "registry_question": registry_question,
        "persistence_purpose": persistence_purpose,
        "registry_intent": registry_intent,
        "selected_record_category": selected_record_category,
        "registry_persistence_basis": copy.deepcopy(registry_persistence_basis)
        if registry_persistence_basis is not None
        else {
            "basis": "bounded registry/persistence preservation posture",
            "does_not_create_authority": True,
            "does_not_create_currentness": True,
            "does_not_create_distributed_standing": True,
        },
        "persistence_preservation_rules": copy.deepcopy(
            DEFAULT_PERSISTENCE_PRESERVATION_RULES
        ),
        "registry_non_authority_rules": copy.deepcopy(DEFAULT_REGISTRY_NON_AUTHORITY_RULES),
        "declared_non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
    }
    if selected_carrier is not None:
        request["selected_carrier"] = copy.deepcopy(dict(selected_carrier))
    if selected_referenced_artifacts is not None:
        request["selected_referenced_artifacts"] = [
            copy.deepcopy(dict(item)) for item in selected_referenced_artifacts
        ]
    return request


def _resolve_registry_persistence(
    request: Mapping[str, Any],
    request_path: Path | None,
    precheck_failures: Sequence[str],
) -> dict[str, Any]:
    normalized_request = _as_mapping(request)
    question = _declared_registry_question(normalized_request, request_path)
    purpose = _persistence_purpose(normalized_request)
    category = _selected_record_category(normalized_request)
    selected_carrier = _selected_carrier(normalized_request)
    artifacts = _selected_referenced_artifacts(normalized_request, category)
    basis = _registry_persistence_basis(normalized_request)
    preservation_rules = _persistence_preservation_rules(normalized_request)
    non_authority_rules = _registry_non_authority_rules(normalized_request)
    projection = _projection_from_sections(category, artifacts, basis)
    checks = _build_checks(
        normalized_request,
        question,
        purpose,
        category,
        selected_carrier,
        artifacts,
        basis,
        preservation_rules,
        non_authority_rules,
        projection,
        precheck_failures,
    )
    failed_checks = [check for check in checks if check.get("passed") is False]
    intent = question.get("registry_intent")
    explicit_block_code = _declared_block_code(normalized_request)

    if failed_checks:
        outcome = CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED
        block_code = str(failed_checks[0].get("block_code") or "NON_CLAIM_MISSING_OR_FLIPPED")
    elif intent == BLOCK_INTENT:
        outcome = CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED
        block_code = explicit_block_code or "REGISTRY_REQUEST_EXPLICITLY_BLOCKED"
    elif intent == DO_NOT_RECORD_INTENT:
        outcome = CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED
        block_code = None
    else:
        outcome = CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED
        block_code = None

    block_reason = _block_reason(block_code)
    result: dict[str, Any] = {
        "carrier_registry_persistence_metadata": {
            "carrier_registry_persistence_result_id": _result_id(
                question,
                category,
                outcome,
            ),
            "carrier_registry_persistence_result_type": RESULT_TYPE,
            "carrier_registry_persistence_result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
            "successor_of_module": SUCCESSOR_OF_MODULE,
        },
        "declared_registry_question": question,
        "persistence_purpose": purpose,
        "selected_record_category": category,
        "selected_carrier": selected_carrier,
        "selected_referenced_artifacts": artifacts,
        "registry_persistence_basis": basis,
        "persistence_preservation_rules": preservation_rules,
        "registry_non_authority_rules": non_authority_rules,
        "registry_persistence_checks": checks,
        "registry_persistence_statement": _registry_persistence_statement(
            outcome,
            question,
            purpose,
            category,
            selected_carrier,
            artifacts,
            basis,
            checks,
            projection,
            block_code,
            block_reason,
        ),
        "registry_persistence_non_meaning": copy.deepcopy(
            REGISTRY_PERSISTENCE_NON_MEANING
        ),
        "what_remains_open": copy.deepcopy(WHAT_REMAINS_OPEN),
        "non_claims": copy.deepcopy(REQUIRED_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": block_reason,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["carrier_registry_persistence_summary"] = (
        build_carrier_registry_persistence_summary(result)
    )
    return result


def _read_json_mapping(path: Path | str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        loaded = json.loads(artifact_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CarrierRegistryPersistenceBoundaryV2Error(
            "DECLARED_REGISTRY_REQUEST_UNREADABLE",
            BLOCK_REASONS["DECLARED_REGISTRY_REQUEST_UNREADABLE"],
        ) from exc
    except json.JSONDecodeError as exc:
        raise CarrierRegistryPersistenceBoundaryV2Error(
            "DECLARED_REGISTRY_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_REGISTRY_REQUEST_MALFORMED"],
        ) from exc
    if not isinstance(loaded, Mapping):
        raise CarrierRegistryPersistenceBoundaryV2Error(
            "DECLARED_REGISTRY_REQUEST_MALFORMED",
            BLOCK_REASONS["DECLARED_REGISTRY_REQUEST_MALFORMED"],
        )
    return copy.deepcopy(dict(loaded))


def _declared_registry_question(
    request: Mapping[str, Any],
    request_path: Path | None,
) -> dict[str, Any]:
    section = _as_mapping(request.get("declared_registry_question"))
    return {
        "registry_request_id": request.get("registry_request_id")
        or section.get("registry_request_id"),
        "registry_request_path": _display_path(request_path)
        if request_path
        else request.get("_registry_request_path")
        or section.get("registry_request_path"),
        "registry_question": request.get("registry_question")
        or section.get("registry_question"),
        "registry_intent": _normalize_token(
            request.get("registry_intent") or section.get("registry_intent")
        ),
        "not_recorded_reason": request.get("not_recorded_reason")
        or section.get("not_recorded_reason"),
        "operator_note": request.get("operator_note") or section.get("operator_note"),
        "declared_non_claims": copy.deepcopy(
            request.get("declared_non_claims")
            or request.get("non_claims")
            or section.get("declared_non_claims")
        ),
        "records_one_registry_persistence_question": True,
        "registry_is_not_authority": True,
        "persistence_is_not_standing": True,
        "indexing_is_not_currentness": True,
        "record_presence_is_not_permission": True,
        "registry_membership_is_not_distributed_standing": True,
        "does_not_implement_registry_storage": True,
        "does_not_authorize_sync_full_body_transfer_or_distributed_operation": True,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _persistence_purpose(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("persistence_purpose")
    if isinstance(raw, Mapping):
        purpose = raw.get("persistence_purpose")
    else:
        purpose = raw
    return {
        "persistence_purpose": purpose,
        "persistence_purpose_declared": _nonempty(purpose),
        "persistence_purpose_preserved": _nonempty(purpose),
        "persistence_does_not_create_standing": True,
        "persistence_does_not_create_authority": True,
        "persistence_does_not_create_currentness": True,
        "persistence_does_not_create_distributed_standing": True,
    }


def _selected_record_category(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_record_category")
    raw_category = raw.get("selected_record_category") if isinstance(raw, Mapping) else raw
    category = _normalize_token(raw_category)
    return {
        "selected_record_category": category,
        "selected_record_category_declared": category is not None,
        "selected_record_category_supported": category in SUPPORTED_RECORD_CATEGORIES,
        "selected_record_category_preserved": category is not None,
        "category_requires_selected_carrier": category in CATEGORIES_REQUIRING_SELECTED_CARRIER,
        "category_requires_referenced_artifact": category
        in CATEGORIES_REQUIRING_REFERENCED_ARTIFACT,
        "category_is_not_database_schema": True,
        "category_is_not_registry_authority": True,
        "raw_selected_record_category": copy.deepcopy(raw),
    }


def _selected_carrier(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("selected_carrier")
    if isinstance(raw, Mapping):
        carrier = copy.deepcopy(dict(raw))
        carrier_id = (
            carrier.get("selected_carrier_id")
            or carrier.get("carrier_id")
            or carrier.get("carrier_identity")
            or carrier.get("id")
        )
    else:
        carrier = raw
        carrier_id = raw if isinstance(raw, str) else None
    return {
        "selected_carrier_declared": raw is not None,
        "selected_carrier_id": carrier_id,
        "carrier_identity_declared": _nonempty(carrier_id),
        "selected_carrier_preserved": _nonempty(carrier_id),
        "carrier_record_is_not_currentness": True,
        "carrier_record_is_not_source": True,
        "carrier_record_is_not_authority": True,
        "carrier_record_is_not_distributed_standing": True,
        "raw_selected_carrier": copy.deepcopy(carrier),
    }


def _selected_referenced_artifacts(
    request: Mapping[str, Any],
    category: Mapping[str, Any],
) -> dict[str, Any]:
    raw = request.get("selected_referenced_artifacts")
    required = bool(category.get("category_requires_referenced_artifact"))
    if raw is None:
        return {
            "referenced_artifacts_required": required,
            "referenced_artifacts_supplied": False,
            "referenced_artifacts_parseable": True,
            "referenced_artifact_entries": [],
            "referenced_artifact_ids": [],
            "referenced_artifact_outcomes": [],
            "referenced_artifacts_preserved": False,
            "referenced_artifact_identity_preserved": False,
            "referenced_artifact_outcome_preserved": False,
            "raw_selected_referenced_artifacts": None,
        }

    if isinstance(raw, Mapping) and (
        "referenced_artifact_entries" in raw or "referenced_artifact_ids" in raw
    ):
        return _normalize_existing_artifact_section(raw, required)

    entries: list[dict[str, Any]] = []
    parseable = True
    if isinstance(raw, Mapping):
        raw_items = [raw]
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        raw_items = list(raw)
    else:
        raw_items = [raw]
        parseable = False

    for item in raw_items:
        if not isinstance(item, Mapping):
            parseable = False
            continue
        entries.append(_artifact_entry(item))

    return _artifact_section_from_entries(entries, raw, required, parseable)


def _normalize_existing_artifact_section(
    raw: Mapping[str, Any],
    required: bool,
) -> dict[str, Any]:
    raw_entries = raw.get("referenced_artifact_entries")
    entries: list[dict[str, Any]] = []
    if isinstance(raw_entries, list):
        for entry in raw_entries:
            if isinstance(entry, Mapping):
                entries.append(_artifact_entry(entry))
    elif isinstance(raw.get("referenced_artifact_ids"), list):
        outcomes = raw.get("referenced_artifact_outcomes")
        outcomes_list = outcomes if isinstance(outcomes, list) else []
        for index, artifact_id in enumerate(raw.get("referenced_artifact_ids", [])):
            entries.append(
                {
                    "referenced_artifact_id": artifact_id,
                    "referenced_artifact_outcome": outcomes_list[index]
                    if index < len(outcomes_list)
                    else None,
                    "referenced_artifact_path": None,
                    "carrier_id": None,
                    "record_category": None,
                    "raw_referenced_artifact": {
                        "referenced_artifact_id": artifact_id,
                        "referenced_artifact_outcome": outcomes_list[index]
                        if index < len(outcomes_list)
                        else None,
                    },
                }
            )
    return _artifact_section_from_entries(entries, raw, required, True)


def _artifact_section_from_entries(
    entries: Sequence[Mapping[str, Any]],
    raw: Any,
    required: bool,
    parseable: bool,
) -> dict[str, Any]:
    artifact_ids = [entry.get("referenced_artifact_id") for entry in entries]
    outcomes = [entry.get("referenced_artifact_outcome") for entry in entries]
    identity_preserved = bool(entries) and all(_nonempty(item) for item in artifact_ids)
    outcome_preserved = bool(entries) and all(_nonempty(item) for item in outcomes)
    return {
        "referenced_artifacts_required": required,
        "referenced_artifacts_supplied": True,
        "referenced_artifacts_parseable": parseable,
        "referenced_artifact_entries": [copy.deepcopy(dict(item)) for item in entries],
        "referenced_artifact_ids": artifact_ids,
        "referenced_artifact_outcomes": outcomes,
        "referenced_artifacts_preserved": bool(entries),
        "referenced_artifact_identity_preserved": identity_preserved,
        "referenced_artifact_outcome_preserved": outcome_preserved,
        "raw_selected_referenced_artifacts": copy.deepcopy(raw),
    }


def _artifact_entry(raw: Mapping[str, Any]) -> dict[str, Any]:
    artifact = copy.deepcopy(dict(raw))
    return {
        "referenced_artifact_id": _artifact_identity(artifact),
        "referenced_artifact_outcome": _artifact_outcome(artifact),
        "referenced_artifact_path": artifact.get("referenced_artifact_path")
        or artifact.get("path")
        or artifact.get("artifact_path"),
        "carrier_id": artifact.get("carrier_id") or artifact.get("selected_carrier_id"),
        "record_category": artifact.get("record_category")
        or artifact.get("selected_record_category"),
        "raw_referenced_artifact": artifact,
    }


def _registry_persistence_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_basis = request.get("registry_persistence_basis")
    basis_mapping = _as_mapping(raw_basis)
    nested_basis = _nested_basis_mapping(basis_mapping)
    lifecycle = _reference_posture(
        _reference_candidate(
            request,
            basis_mapping,
            nested_basis,
            "lifecycle_status_reference",
            "lifecycle_reference",
        )
    )
    relation = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "relation_reference")
    )
    divergence = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "divergence_reference")
    )
    currentness = _reference_posture(
        _reference_candidate(
            request,
            basis_mapping,
            nested_basis,
            "currentness_participation_reference",
        )
    )
    admission = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "admission_reference")
    )
    receipt = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "receipt_reference")
    )
    experiment = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "experiment_reference")
    )
    integrity = _reference_posture(
        _reference_candidate(request, basis_mapping, nested_basis, "integrity_reference")
    )
    return {
        "registry_persistence_basis_declared": _basis_declared(raw_basis),
        "registry_persistence_basis_preserved": _basis_declared(raw_basis),
        "raw_registry_persistence_basis": copy.deepcopy(
            nested_basis if nested_basis else raw_basis
        ),
        "raw_registry_persistence_basis_section": copy.deepcopy(raw_basis),
        "lifecycle_status_reference": lifecycle,
        "relation_reference": relation,
        "divergence_reference": divergence,
        "currentness_participation_reference": currentness,
        "admission_reference": admission,
        "receipt_reference": receipt,
        "experiment_reference": experiment,
        "integrity_reference": integrity,
        "lifecycle_reference_preserved": lifecycle["preserved"],
        "relation_reference_preserved": relation["preserved"],
        "divergence_reference_preserved": divergence["preserved"],
        "currentness_participation_reference_preserved": currentness["preserved"],
        "admission_reference_preserved": admission["preserved"],
        "receipt_reference_preserved": receipt["preserved"],
        "experiment_reference_preserved": experiment["preserved"],
        "integrity_reference_preserved": integrity["preserved"],
        "registry_preserves_references_only": True,
        "registry_does_not_upgrade_references": True,
        "registry_does_not_create_authority": True,
        "registry_does_not_create_currentness": True,
        "registry_does_not_create_distributed_standing": True,
    }


def _nested_basis_mapping(basis_mapping: Mapping[str, Any]) -> dict[str, Any]:
    nested = basis_mapping.get("raw_registry_persistence_basis")
    if isinstance(nested, Mapping):
        return copy.deepcopy(dict(nested))
    return copy.deepcopy(dict(basis_mapping))


def _reference_candidate(
    request: Mapping[str, Any],
    basis_mapping: Mapping[str, Any],
    nested_basis: Mapping[str, Any],
    key: str,
    alternate_key: str | None = None,
) -> Any:
    keys = (key, alternate_key) if alternate_key else (key,)
    for source in (request, basis_mapping, nested_basis):
        for candidate_key in keys:
            if candidate_key and candidate_key in source:
                value = source.get(candidate_key)
                if _reference_has_signal(value):
                    return value
    return None


def _persistence_preservation_rules(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("persistence_preservation_rules")
    if isinstance(raw, Mapping) and "effective_persistence_preservation_rules" in raw:
        raw_mapping = _as_mapping(raw.get("effective_persistence_preservation_rules"))
    else:
        raw_mapping = _as_mapping(raw)
    effective = copy.deepcopy(DEFAULT_PERSISTENCE_PRESERVATION_RULES)
    effective.update(raw_mapping)
    return {
        "persistence_preservation_rules_supplied": raw is not None,
        "persistence_preservation_rules_derivable": True,
        "persistence_preservation_rules_preserved": _all_rule_values_true(effective),
        "effective_persistence_preservation_rules": effective,
        "raw_persistence_preservation_rules": copy.deepcopy(raw),
    }


def _registry_non_authority_rules(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("registry_non_authority_rules")
    if isinstance(raw, Mapping) and "effective_registry_non_authority_rules" in raw:
        raw_mapping = _as_mapping(raw.get("effective_registry_non_authority_rules"))
    else:
        raw_mapping = _as_mapping(raw)
    effective = copy.deepcopy(DEFAULT_REGISTRY_NON_AUTHORITY_RULES)
    effective.update(raw_mapping)
    return {
        "registry_non_authority_rules_supplied": raw is not None,
        "registry_non_authority_rules_derivable": True,
        "registry_non_authority_rules_preserved": _all_rule_values_true(effective),
        "effective_registry_non_authority_rules": effective,
        "raw_registry_non_authority_rules": copy.deepcopy(raw),
    }


def _build_checks(
    request: Mapping[str, Any],
    question: Mapping[str, Any],
    purpose: Mapping[str, Any],
    category: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    basis: Mapping[str, Any],
    preservation_rules: Mapping[str, Any],
    non_authority_rules: Mapping[str, Any],
    projection: Mapping[str, bool],
    precheck_failures: Sequence[str],
) -> list[dict[str, Any]]:
    collapse_source = _without_safe_sections(request)
    declared_non_claims = _as_mapping(
        request.get("declared_non_claims")
        or request.get("non_claims")
        or question.get("declared_non_claims")
    )
    sources = [
        collapse_source,
        question,
        purpose,
        category,
        selected_carrier,
        artifacts,
        basis,
        preservation_rules,
        non_authority_rules,
        declared_non_claims,
    ]
    precheck_code = precheck_failures[0] if precheck_failures else None
    carrier_required = bool(category.get("category_requires_selected_carrier"))
    artifact_required = bool(artifacts.get("referenced_artifacts_required"))
    lifecycle_signal = _lifecycle_reference_signal(category, artifacts, basis)
    checks = [
        _check(
            "declared_registry_request_parseable_mapping",
            not precheck_failures,
            "declared registry/persistence request is a parseable mapping",
            list(precheck_failures),
            precheck_code or "DECLARED_REGISTRY_REQUEST_MALFORMED",
        ),
        _check(
            "registry_question_declared",
            _nonempty(question.get("registry_question")),
            "registry question is declared",
            question.get("registry_question"),
            "REGISTRY_QUESTION_UNDECLARED",
        ),
        _check(
            "persistence_purpose_declared",
            bool(purpose.get("persistence_purpose_declared")),
            "persistence purpose is declared",
            purpose.get("persistence_purpose"),
            "PERSISTENCE_PURPOSE_UNDECLARED",
        ),
        _check(
            "registry_intent_supported",
            question.get("registry_intent") in SUPPORTED_REGISTRY_INTENTS,
            "registry intent is supported",
            question.get("registry_intent"),
            "REGISTRY_INTENT_UNSUPPORTED",
        ),
        _check(
            "record_category_supported",
            bool(category.get("selected_record_category_supported")),
            "selected record category is supported",
            category.get("selected_record_category"),
            "RECORD_CATEGORY_UNSUPPORTED",
        ),
        _check(
            "selected_carrier_identity_present_where_required",
            not carrier_required or bool(selected_carrier.get("carrier_identity_declared")),
            "selected carrier identity is present where required",
            {
                "category_requires_selected_carrier": carrier_required,
                "selected_carrier_id": selected_carrier.get("selected_carrier_id"),
            },
            "CARRIER_IDENTITY_MISSING",
        ),
        _check(
            "referenced_artifacts_present_where_required",
            not artifact_required or bool(artifacts.get("referenced_artifacts_supplied")),
            "referenced artifact is present where required",
            {
                "category_requires_referenced_artifact": artifact_required,
                "referenced_artifact_ids": artifacts.get("referenced_artifact_ids"),
            },
            "REFERENCED_ARTIFACT_MISSING",
        ),
        _check(
            "referenced_artifact_parseable_where_supplied",
            bool(artifacts.get("referenced_artifacts_parseable")),
            "referenced artifacts are parseable where supplied",
            _shape(artifacts.get("raw_selected_referenced_artifacts")),
            "REFERENCED_ARTIFACT_MALFORMED",
        ),
        _check(
            "referenced_artifact_identity_present_where_required",
            not artifacts.get("referenced_artifacts_supplied")
            or bool(projection.get("referenced_artifact_identity_preserved")),
            "referenced artifact identity is present where supplied",
            artifacts.get("referenced_artifact_ids"),
            "REFERENCED_ARTIFACT_IDENTITY_MISSING",
        ),
        _check(
            "referenced_artifact_outcome_present_where_required",
            not artifacts.get("referenced_artifacts_supplied")
            or bool(projection.get("referenced_artifact_outcome_preserved")),
            "referenced artifact outcome is present where supplied",
            artifacts.get("referenced_artifact_outcomes"),
            "REFERENCED_ARTIFACT_OUTCOME_MISSING",
        ),
        _check(
            "lifecycle_reference_preserved_when_supplied_or_inferable",
            not lifecycle_signal or bool(projection.get("lifecycle_reference_preserved")),
            "lifecycle reference projects true when supplied or inferable",
            {
                "lifecycle_signal": lifecycle_signal,
                "lifecycle_reference_preserved": projection.get(
                    "lifecycle_reference_preserved"
                ),
            },
            "REFERENCED_ARTIFACT_MALFORMED",
        ),
        _reference_check(
            "relation_reference_preserved_where_supplied",
            basis.get("relation_reference"),
        ),
        _reference_check(
            "divergence_reference_preserved_where_supplied",
            basis.get("divergence_reference"),
        ),
        _reference_check(
            "currentness_participation_reference_preserved_where_supplied",
            basis.get("currentness_participation_reference"),
        ),
        _reference_check(
            "admission_reference_preserved_where_supplied",
            basis.get("admission_reference"),
        ),
        _reference_check(
            "receipt_reference_preserved_where_supplied",
            basis.get("receipt_reference"),
        ),
        _reference_check(
            "experiment_reference_preserved_where_supplied",
            basis.get("experiment_reference"),
        ),
        _check(
            "evidence_reference_preserved_where_supplied",
            not artifacts.get("referenced_artifacts_supplied")
            or bool(projection.get("evidence_reference_preserved")),
            "evidence or artifact reference is preserved where supplied",
            artifacts.get("referenced_artifact_ids"),
            "REFERENCED_ARTIFACT_MISSING",
        ),
        _check(
            "persistence_preservation_rules_preserved",
            bool(preservation_rules.get("persistence_preservation_rules_preserved")),
            "persistence preservation rules are preserved",
            preservation_rules.get("effective_persistence_preservation_rules"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "registry_non_authority_rules_preserved",
            bool(non_authority_rules.get("registry_non_authority_rules_preserved")),
            "registry non-authority rules are preserved",
            non_authority_rules.get("effective_registry_non_authority_rules"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _collapse_check(
            "registry_does_not_decide_source",
            sources,
            (
                "source_decided",
                "registry_decides_source",
                "registry_created_source",
                "source_replaced",
            ),
            "registry does not decide source",
            "REGISTRY_DECIDES_SOURCE",
        ),
        _collapse_check(
            "registry_does_not_decide_currentness",
            sources,
            (
                "currentness_decided",
                "registry_decides_currentness",
                "registry_created_currentness",
                "currentness_created",
            ),
            "registry does not decide currentness",
            "REGISTRY_DECIDES_CURRENTNESS",
        ),
        _collapse_check(
            "registry_does_not_create_authority",
            sources,
            (
                "authority_created",
                "registry_created_authority",
                "registry_authority_created",
                "carrier_registry_created_as_authority",
            ),
            "registry does not create authority",
            "REGISTRY_CREATES_AUTHORITY",
        ),
        _collapse_check(
            "registry_does_not_create_permission",
            sources,
            (
                "permission_created",
                "registry_created_permission",
                "permission_beyond_registry_created",
            ),
            "registry does not create permission",
            "REGISTRY_CREATES_PERMISSION",
        ),
        _collapse_check(
            "registry_does_not_create_carrier_hierarchy",
            sources,
            (
                "carrier_hierarchy_created",
                "registry_created_carrier_hierarchy",
                "registry_creates_carrier_hierarchy",
            ),
            "registry does not create carrier hierarchy",
            "REGISTRY_CREATES_CARRIER_HIERARCHY",
        ),
        _collapse_check(
            "registry_does_not_select_current_carrier",
            sources,
            ("current_carrier_selected", "registry_selects_current_carrier"),
            "registry does not select current carrier",
            "REGISTRY_SELECTS_CURRENT_CARRIER",
        ),
        _collapse_check(
            "registry_does_not_select_winning_carrier",
            sources,
            ("winning_carrier_selected", "registry_selects_winning_carrier"),
            "registry does not select winning carrier",
            "REGISTRY_SELECTS_WINNING_CARRIER",
        ),
        _collapse_check(
            "registry_does_not_invalidate_losing_carrier",
            sources,
            ("losing_carrier_invalidated", "registry_invalidates_losing_carrier"),
            "registry does not invalidate losing carrier",
            "REGISTRY_INVALIDATES_LOSING_CARRIER",
        ),
        _collapse_check(
            "registry_does_not_resolve_divergence",
            sources,
            ("divergence_resolved", "registry_resolves_divergence"),
            "registry does not resolve divergence",
            "REGISTRY_RESOLVES_DIVERGENCE",
        ),
        _collapse_check(
            "registry_does_not_erase_evidence",
            sources,
            (
                "evidence_erased",
                "registry_erased_evidence",
                "older_records_erased",
                "prior_evidence_erased",
            ),
            "registry does not erase evidence",
            "REGISTRY_ERASES_EVIDENCE",
        ),
        _collapse_check(
            "registry_does_not_hide_refusal",
            sources,
            ("refusal_hidden", "hidden_refusal", "registry_hid_refusal"),
            "registry does not hide refusal",
            "REGISTRY_HIDES_REFUSAL",
        ),
        _collapse_check(
            "registry_does_not_hide_divergence",
            sources,
            (
                "divergence_hidden",
                "mismatch_hidden",
                "hidden_divergence",
                "hidden_mismatch",
                "registry_hid_divergence",
            ),
            "registry does not hide divergence",
            "REGISTRY_HIDES_DIVERGENCE",
        ),
        _collapse_check(
            "registry_does_not_hide_corruption",
            sources,
            ("corruption_hidden", "hidden_corruption", "registry_hid_corruption"),
            "registry does not hide corruption",
            "REGISTRY_HIDES_CORRUPTION",
        ),
        _collapse_check(
            "registry_does_not_repair_by_overwrite",
            sources,
            (
                "repair_by_overwrite",
                "repaired_by_overwrite",
                "registry_repaired_by_overwrite",
            ),
            "registry does not repair by overwrite",
            "REGISTRY_REPAIRS_BY_OVERWRITE",
        ),
        _collapse_check(
            "registry_does_not_create_distributed_standing",
            sources,
            (
                "distributed_standing_created",
                "registry_created_distributed_standing",
                "registry_creates_distributed_standing",
            ),
            "registry does not create distributed standing",
            "REGISTRY_CREATES_DISTRIBUTED_STANDING",
        ),
        _collapse_check(
            "registry_does_not_authorize_repository_sync",
            sources,
            (
                "repository_synchronization_authorized",
                "repository_sync_authorized",
                "registry_authorized_sync",
            ),
            "registry does not authorize repository synchronization",
            "REGISTRY_AUTHORIZES_REPOSITORY_SYNC",
        ),
        _collapse_check(
            "registry_does_not_authorize_full_body_transfer",
            sources,
            (
                "full_body_transfer_authorized",
                "registry_authorized_full_body_transfer",
            ),
            "registry does not authorize full body transfer",
            "REGISTRY_AUTHORIZES_FULL_BODY_TRANSFER",
        ),
        _collapse_check(
            "registry_does_not_create_second_body",
            sources,
            ("second_body_created", "registry_created_second_body"),
            "registry does not create second body",
            "REGISTRY_CREATES_SECOND_BODY",
        ),
        _collapse_check(
            "registry_does_not_authorize_continuation",
            sources,
            ("continuation_authorized", "registry_authorized_continuation"),
            "registry does not authorize continuation",
            "REGISTRY_AUTHORIZES_CONTINUATION",
        ),
        _collapse_check(
            "registry_does_not_authorize_distributed_operation",
            sources,
            (
                "distributed_operation_authorized",
                "registry_authorized_distributed_operation",
            ),
            "registry does not authorize distributed operation",
            "REGISTRY_AUTHORIZES_DISTRIBUTED_OPERATION",
        ),
        _collapse_check(
            "no_latest_record_currentness",
            sources,
            ("latest_record_currentness", "latest_persisted_record_currentness"),
            "registry does not use latest-record currentness",
            "LATEST_RECORD_CURRENTNESS",
        ),
        _collapse_check(
            "no_latest_file_currentness",
            sources,
            ("latest_file_currentness", "recency_fraud"),
            "registry does not use latest-file currentness or recency fraud",
            "LATEST_FILE_CURRENTNESS",
        ),
        _collapse_check(
            "no_mutation_replay_merge",
            sources,
            (
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "mutation_requested",
                "replay_requested",
                "merge_requested",
            ),
            "registry does not mutate, replay, or merge evidence",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(declared_non_claims),
            "required registry/persistence non-claims are present and false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _registry_persistence_statement(
    outcome: str,
    question: Mapping[str, Any],
    purpose: Mapping[str, Any],
    category: Mapping[str, Any],
    selected_carrier: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    basis: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    projection: Mapping[str, bool],
    block_code: str | None,
    block_reason: str | None,
) -> dict[str, Any]:
    recorded = outcome == CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED
    not_recorded = outcome == CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED
    return {
        "carrier_registry_persistence_boundary_recorded": recorded,
        "not_recorded_reason": question.get("not_recorded_reason")
        or ("registry/persistence boundary explicitly not recorded" if not_recorded else None),
        "block_code": block_code,
        "block_reason": block_reason,
        "registry_question_preserved": _nonempty(question.get("registry_question")),
        "persistence_purpose_preserved": bool(
            purpose.get("persistence_purpose_preserved")
        ),
        "selected_record_category_preserved": bool(
            category.get("selected_record_category_preserved")
        ),
        "selected_carrier_preserved": bool(
            selected_carrier.get("selected_carrier_preserved")
        ),
        "referenced_artifacts_preserved": bool(
            artifacts.get("referenced_artifacts_preserved")
        ),
        "referenced_artifact_identity_preserved": projection[
            "referenced_artifact_identity_preserved"
        ],
        "referenced_artifact_outcome_preserved": projection[
            "referenced_artifact_outcome_preserved"
        ],
        "lifecycle_reference_preserved": projection["lifecycle_reference_preserved"],
        "relation_reference_preserved": projection["relation_reference_preserved"],
        "divergence_reference_preserved": projection["divergence_reference_preserved"],
        "currentness_participation_reference_preserved": projection[
            "currentness_participation_reference_preserved"
        ],
        "admission_reference_preserved": bool(
            basis.get("admission_reference", {}).get("preserved")
        ),
        "receipt_reference_preserved": bool(
            basis.get("receipt_reference", {}).get("preserved")
        ),
        "experiment_reference_preserved": bool(
            basis.get("experiment_reference", {}).get("preserved")
        ),
        "integrity_reference_preserved": bool(
            basis.get("integrity_reference", {}).get("preserved")
        ),
        "evidence_reference_preserved": projection["evidence_reference_preserved"],
        "non_claims_preserved": True,
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is False),
        "registry_presence_created_standing": False,
        "registry_created_source": False,
        "registry_created_currentness": False,
        "registry_created_authority": False,
        "registry_created_permission": False,
        "registry_created_carrier_hierarchy": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "divergence_resolved": False,
        "registry_created_distributed_standing": False,
        "registry_authorized_sync": False,
        "registry_authorized_full_body_transfer": False,
        "registry_created_second_body": False,
        "registry_authorized_continuation": False,
        "registry_authorized_distributed_operation": False,
        "registry_erased_evidence": False,
        "registry_hid_refusal": False,
        "registry_hid_divergence": False,
        "registry_hid_corruption": False,
        "registry_repaired_by_overwrite": False,
        "latest_record_currentness": False,
        "latest_file_currentness": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
        "registry_implemented_storage": False,
        "persistence_engine_implemented": False,
        "database_created": False,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _projection_from_result(result: Mapping[str, Any]) -> dict[str, bool]:
    category = _category_from_result(result)
    artifacts = _as_mapping(result.get("selected_referenced_artifacts"))
    basis = _as_mapping(result.get("registry_persistence_basis"))
    return _projection_from_sections(category, artifacts, basis)


def _projection_from_sections(
    category: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> dict[str, bool]:
    artifact_identity = bool(artifacts.get("referenced_artifact_identity_preserved"))
    artifact_outcome = bool(artifacts.get("referenced_artifact_outcome_preserved"))
    evidence_reference = bool(
        artifacts.get("referenced_artifacts_preserved")
        and artifact_identity
        and artifact_outcome
    )
    return {
        "referenced_artifact_identity_preserved": artifact_identity,
        "referenced_artifact_outcome_preserved": artifact_outcome,
        "lifecycle_reference_preserved": _project_lifecycle_reference(
            category,
            artifacts,
            basis,
        ),
        "relation_reference_preserved": bool(
            basis.get("relation_reference_preserved")
            or _as_mapping(basis.get("relation_reference")).get("preserved")
        ),
        "divergence_reference_preserved": bool(
            basis.get("divergence_reference_preserved")
            or _as_mapping(basis.get("divergence_reference")).get("preserved")
        ),
        "currentness_participation_reference_preserved": bool(
            basis.get("currentness_participation_reference_preserved")
            or _as_mapping(basis.get("currentness_participation_reference")).get("preserved")
        ),
        "evidence_reference_preserved": evidence_reference,
    }


def _project_lifecycle_reference(
    category: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> bool:
    if bool(basis.get("lifecycle_reference_preserved")):
        return True

    lifecycle_posture = _as_mapping(basis.get("lifecycle_status_reference"))
    if lifecycle_posture.get("preserved") is True:
        return True
    if lifecycle_posture.get("supplied") is True and lifecycle_posture.get("parseable") is True:
        return True

    raw_basis = _as_mapping(basis.get("raw_registry_persistence_basis"))
    raw_lifecycle = raw_basis.get("lifecycle_status_reference") or raw_basis.get(
        "lifecycle_reference"
    )
    if _reference_has_signal(raw_lifecycle):
        return True
    if isinstance(raw_lifecycle, Mapping):
        status = _normalize_token(
            raw_lifecycle.get("requested_lifecycle_status")
            or raw_lifecycle.get("raw_requested_lifecycle_status")
            or raw_lifecycle.get("lifecycle_status")
        )
        if raw_lifecycle.get("requested_lifecycle_status_preserved") is True:
            return True
        if (
            raw_lifecycle.get("requested_lifecycle_status_declared") is True
            and status in SUPPORTED_LIFECYCLE_STATUSES
        ):
            return True

    category_name = category.get("selected_record_category")
    artifact_outcomes = {_normalize_token(item) for item in artifacts.get("referenced_artifact_outcomes", [])}
    if (
        category_name == "CARRIER_LIFECYCLE_STATUS_RECORD"
        and "CARRIER_LIFECYCLE_STATUS_RECORDED" in artifact_outcomes
        and artifacts.get("referenced_artifact_identity_preserved") is True
    ):
        return True

    for entry in artifacts.get("referenced_artifact_entries", []):
        if not isinstance(entry, Mapping):
            continue
        raw_entry = _as_mapping(entry.get("raw_referenced_artifact"))
        outcome = _normalize_token(entry.get("referenced_artifact_outcome"))
        record_category = _normalize_token(entry.get("record_category"))
        raw_status = _normalize_token(
            raw_entry.get("requested_lifecycle_status")
            or raw_entry.get("lifecycle_status")
            or raw_entry.get("raw_requested_lifecycle_status")
        )
        has_identity = _nonempty(entry.get("referenced_artifact_id"))
        has_outcome = _nonempty(entry.get("referenced_artifact_outcome"))
        if has_identity and has_outcome and (
            outcome == "CARRIER_LIFECYCLE_STATUS_RECORDED"
            or record_category == "CARRIER_LIFECYCLE_STATUS_RECORD"
            or raw_status in SUPPORTED_LIFECYCLE_STATUSES
        ):
            return True

    return False


def _lifecycle_reference_signal(
    category: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> bool:
    if _project_lifecycle_reference(category, artifacts, basis):
        return True
    lifecycle_posture = _as_mapping(basis.get("lifecycle_status_reference"))
    return bool(lifecycle_posture.get("supplied"))


def _reference_posture(raw: Any) -> dict[str, Any]:
    if raw is None:
        return {
            "supplied": False,
            "parseable": True,
            "preserved": False,
            "reference_id": None,
            "reference_outcome": None,
            "raw_reference": None,
        }
    if isinstance(raw, str):
        return {
            "supplied": True,
            "parseable": True,
            "preserved": _nonempty(raw),
            "reference_id": raw,
            "reference_outcome": None,
            "raw_reference": raw,
        }
    if not isinstance(raw, Mapping):
        return {
            "supplied": True,
            "parseable": False,
            "preserved": False,
            "reference_id": None,
            "reference_outcome": None,
            "raw_reference": copy.deepcopy(raw),
        }
    reference = copy.deepcopy(dict(raw))
    reference_id = _artifact_identity(reference)
    outcome = _artifact_outcome(reference)
    return {
        "supplied": True,
        "parseable": True,
        "preserved": _nonempty(reference_id) or _nonempty(outcome) or bool(reference),
        "reference_id": reference_id,
        "reference_outcome": outcome,
        "carrier_id": reference.get("carrier_id") or reference.get("selected_carrier_id"),
        "raw_reference": reference,
    }


def _reference_check(check_name: str, reference: Any) -> dict[str, Any]:
    ref = _as_mapping(reference)
    return _check(
        check_name,
        not ref.get("supplied") or bool(ref.get("parseable") and ref.get("preserved")),
        "reference is preserved where supplied",
        ref,
        "REFERENCED_ARTIFACT_MALFORMED",
    )


def _artifact_identity(artifact: Mapping[str, Any]) -> Any:
    return (
        artifact.get("referenced_artifact_id")
        or artifact.get("artifact_id")
        or artifact.get("evidence_id")
        or artifact.get("result_id")
        or artifact.get("record_id")
        or artifact.get("id")
        or artifact.get("path")
        or artifact.get("artifact_path")
        or artifact.get("referenced_artifact_path")
    )


def _artifact_outcome(artifact: Mapping[str, Any]) -> Any:
    return (
        artifact.get("referenced_artifact_outcome")
        or artifact.get("artifact_outcome")
        or artifact.get("result_outcome")
        or artifact.get("evidence_outcome")
        or artifact.get("outcome")
        or artifact.get("status")
    )


def _purpose_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    return _as_mapping(result.get("persistence_purpose"))


def _category_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    raw = result.get("selected_record_category")
    if isinstance(raw, Mapping):
        return _as_mapping(raw)
    return {
        "selected_record_category": _normalize_token(raw),
        "selected_record_category_supported": _normalize_token(raw)
        in SUPPORTED_RECORD_CATEGORIES,
    }


def _declared_block_code(request: Mapping[str, Any]) -> str | None:
    block = _as_mapping(request.get("block"))
    code = (
        request.get("declared_block_code")
        or request.get("block_code")
        or block.get("block_code")
        or block.get("code")
    )
    normalized = _normalize_token(code)
    return normalized if normalized in BLOCK_REASONS else None


def _required_non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    if not isinstance(non_claims, Mapping):
        return False
    return all(non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _all_rule_values_true(rules: Mapping[str, Any]) -> bool:
    return all(value is not False for value in rules.values())


def _basis_declared(value: Any) -> bool:
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return _nonempty(value)


def _reference_has_signal(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        if value.get("supplied") is False and not value.get("preserved"):
            return False
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _collapse_check(
    check_name: str,
    sources: Sequence[Mapping[str, Any]],
    flag_keys: Sequence[str],
    expected_posture: str,
    block_code: str,
) -> dict[str, Any]:
    found = _first_true_flag(sources, flag_keys)
    return _check(
        check_name,
        found is None,
        expected_posture,
        found or {key: False for key in flag_keys},
        block_code,
    )


def _first_true_flag(
    sources: Sequence[Mapping[str, Any]],
    flag_keys: Sequence[str],
) -> dict[str, Any] | None:
    for source in sources:
        found = _find_true_flag(source, set(flag_keys))
        if found is not None:
            return found
    return None


def _find_true_flag(value: Any, flag_keys: set[str]) -> dict[str, Any] | None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in flag_keys and item is True:
                return {str(key): item}
            nested = _find_true_flag(item, flag_keys)
            if nested is not None:
                return nested
    elif isinstance(value, list):
        for item in value:
            nested = _find_true_flag(item, flag_keys)
            if nested is not None:
                return nested
    return None


def _without_safe_sections(request: Mapping[str, Any]) -> dict[str, Any]:
    safe_keys = {
        "registry_persistence_non_meaning",
        "what_remains_open",
        "non_meaning",
        "open_items",
    }
    return {key: copy.deepcopy(value) for key, value in request.items() if key not in safe_keys}


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": copy.deepcopy(actual_posture),
        "block_code": None if passed else block_code,
    }


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _normalize_token(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().upper().replace("-", "_").replace(" ", "_")
    return normalized or None


def _shape(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, Mapping):
        return {"type": "mapping", "keys": sorted(str(key) for key in value.keys())}
    if isinstance(value, list):
        return {"type": "list", "length": len(value)}
    return {"type": type(value).__name__, "value": value}


def _block_reason(block_code: str | None) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code, f"Registry/persistence blocked by {block_code}.")


def _result_id(
    question: Mapping[str, Any],
    category: Mapping[str, Any],
    outcome: str,
) -> str:
    basis_id = (
        question.get("registry_request_id")
        or category.get("selected_record_category")
        or "carrier_registry_persistence"
    )
    return (
        f"{_safe_filename_part(basis_id)}__"
        f"{_safe_filename_part(outcome.lower())}__v2"
    )


def _key_non_claims(non_claims: Mapping[str, Any]) -> dict[str, Any]:
    return {key: non_claims.get(key) for key in REQUIRED_NON_CLAIMS}


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "carrier_registry_persistence").strip()
    cleaned = "".join(char if char.isalnum() or char in "._-" else "_" for char in raw)
    return cleaned.strip("._-") or "carrier_registry_persistence"


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise CarrierRegistryPersistenceBoundaryV2Error(
        "NON_CLAIM_MISSING_OR_FLIPPED",
        "Could not allocate a non-overwriting registry/persistence v2 result path.",
    )


def _display_path(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
