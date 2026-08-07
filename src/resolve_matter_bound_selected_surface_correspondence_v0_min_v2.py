"""Pure V2 matter-bound selected-surface correspondence resolver.

The resolver reconstructs one declared relation for one explicit matter and one
closed ordered manifest. It consumes in-memory mappings only, preserves compact
normalized posture, and creates no persistence, permission, lifecycle, runtime,
Presence, Threshold, Truth, FIELD, workflow, or continuation machinery.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


RESOLVER_MODULE = "resolve_matter_bound_selected_surface_correspondence_v0_min_v2"
RESULT_VERSION = "0.1.0"

CORRESPONDENCE_TYPE = "MATTER_BOUND_SELECTED_SURFACE_CORRESPONDENCE"
CORRESPONDENCE_VERSION = "0.1.0"
CORRESPONDENCE_SCOPE = (
    "ONE_EXPLICIT_MATTER_ONE_EXPLICIT_SELECTED_SURFACE_MANIFEST_"
    "ONE_DECLARED_CORRESPONDENCE_QUESTION_ONLY"
)

CORRESPONDENCE_RECOGNIZED = "CORRESPONDENCE_RECOGNIZED"
NO_CORRESPONDENCE = "NO_CORRESPONDENCE"
BLOCKED = "BLOCKED"
OUTCOMES = (
    CORRESPONDENCE_RECOGNIZED,
    NO_CORRESPONDENCE,
    BLOCKED,
)

ADMITTED_RELATION_TYPES = (
    "BASIS_MATCH",
    "BASIS_MISMATCH",
    "DOWNSTREAM_RECOGNITION",
    "SCOPE_ALIGNMENT",
    "SCOPE_MISMATCH",
    "NON_CLAIM_ALIGNMENT",
    "NON_CLAIM_CONFLICT",
    "LINEAGE_REFERENCE",
    "CLOSURE_ALIGNMENT",
    "REFUSAL_VISIBLE",
    "NO_CORRESPONDENCE",
)

NEGATIVE_RELATION_TYPES = frozenset(
    {
        "BASIS_MISMATCH",
        "SCOPE_MISMATCH",
        "NON_CLAIM_CONFLICT",
        "REFUSAL_VISIBLE",
        "NO_CORRESPONDENCE",
    }
)

REQUIRED_FALSE_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "registry_created",
    "source_replaced",
    "standing_created",
    "standing_upgraded",
    "surface_merged",
    "surface_equivalence_created",
    "explanation_ownership_created",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "identity_created",
    "self_orientation_successor_forced",
    "self_orientation_successor_created",
    "conformance_successor_forced",
    "conformance_successor_created",
    "coverage_successor_created",
    "field_machinery_created",
    "runtime_created",
    "daemon_created",
    "workflow_created",
    "routing_created",
    "continuation_authorized",
    "automatic_next_step_created",
    "mutation_performed",
    "catalogue_authority_created",
    "coverage_authority_created",
    "constitutional_inventory_created",
    "whole_body_coherence_created",
    "whole_body_presence_created",
    "constitutional_presence_created",
    "field_jurisdiction_created",
    "cross_custody_relation_created",
    "answerability_created",
    "consciousness_created",
    "self_awareness_created",
    "agency_created",
    "sentience_created",
    "biological_status_created",
    "reusable_reconstruction_permission_created",
)

CANONICAL_NON_CLAIMS = {
    key: False for key in REQUIRED_FALSE_NON_CLAIMS
}

REQUIRED_FALSE_RECONSTRUCTION_POSTURES = (
    "scope_widened",
    "mismatch_hidden",
    "conflict_hidden",
    "refusal_hidden",
    "non_correspondence_hidden",
    "missing_support_hidden",
    "supported_negative_relation_treated_as_no_correspondence",
    "similarity_treated_as_equivalence",
    "rank_inferred_from_manifest_order",
    "priority_inferred_from_manifest_order",
    "authority_inferred_from_manifest_order",
    "currentness_inferred_from_manifest_order",
    "chronology_inferred_from_manifest_order",
    "precedence_inferred_from_manifest_order",
    "semantic_weight_inferred_from_manifest_order",
    "recency_inference_used",
    "repository_availability_inference_used",
    "timestamp_inference_used",
    "filename_inference_used",
    "sequence_inference_used",
    "directory_position_inference_used",
    "registry_behavior_created",
    "catalogue_behavior_created",
    "coverage_ledger_created",
    "whole_body_mirror_created",
    "complete_artifact_embedded",
    "recursive_ancestry_embedded",
)

REQUEST_KEYS = frozenset(
    {
        "matter",
        "selected_surface_manifest",
        "declared_correspondence_question",
        "correspondence_basis",
        "reconstruction_posture",
        "declared_non_claims",
    }
)
MATTER_FIELD_ORDER = (
    "matter_id",
    "matter_purpose",
    "matter_scope",
    "reading_reason",
    "outside_boundary",
)
MATTER_KEYS = frozenset(MATTER_FIELD_ORDER)
SURFACE_KEYS = frozenset(
    {
        "selected_position",
        "surface_id",
        "surface_reference",
        "surface_outcome",
        "surface_rank",
        "source_basis",
        "surface_scope",
        "lineage_references",
        "source_downstream_posture",
        "non_claims",
    }
)
QUESTION_KEYS = frozenset(
    {
        "question_id",
        "matter_id",
        "selected_surface_ids",
        "relation_type",
        "direction",
        "bounded_claim",
        "basis_references",
    }
)
BASIS_KEYS = frozenset(
    {
        "readable",
        "available",
        "sufficient",
        "contradictory",
        "evidence_items",
    }
)
EVIDENCE_KEYS = frozenset(
    {
        "evidence_id",
        "surface_references",
        "relation_type",
        "relation_supported",
        "basis_fact",
    }
)

BLOCK_REASONS = {
    "REQUEST_NOT_MAPPING": "The in-memory request must be one mapping.",
    "REQUEST_KEYS_INVALID": "The request must contain exactly the bounded V2 input fields.",
    "MATTER_MISSING_OR_MALFORMED": "Exactly one explicit bounded matter is required.",
    "MANIFEST_MISSING_OR_MALFORMED": "Exactly one closed ordered selected-surface manifest is required.",
    "MANIFEST_TOO_SMALL": "The selected-surface manifest must contain at least two surfaces.",
    "SELECTED_SURFACE_MALFORMED": "Every selected surface must expose exact normalized posture.",
    "SELECTED_SURFACE_NON_CLAIMS_INVALID": "Selected-surface non-claims must be explicit false booleans.",
    "MANIFEST_IDENTITY_DUPLICATED": "Manifest identities and references must be unique.",
    "MANIFEST_POSITION_INVALID": "Manifest positions must be unique contiguous one-based integers.",
    "QUESTION_MISSING_OR_MULTIPLE": "Exactly one declared correspondence question is required.",
    "QUESTION_MALFORMED": "The declared question must preserve the exact bounded V2 fields.",
    "QUESTION_MATTER_MISMATCH": "The declared question must reference the exact matter.",
    "QUESTION_SURFACE_MISMATCH": "The declared question must reference the exact manifest identities.",
    "QUESTION_BASIS_REFERENCE_MISMATCH": "The declared question must reference the exact manifest basis.",
    "RELATION_TYPE_MISSING_OR_MULTIPLE": "Exactly one declared relation type is required.",
    "RELATION_TYPE_UNSUPPORTED": "The declared relation type is outside the admitted family.",
    "BASIS_MISSING_OR_MALFORMED": "One exact readable correspondence basis is required.",
    "BASIS_UNREADABLE": "The declared basis is not readable.",
    "BASIS_UNAVAILABLE": "The declared basis is unavailable.",
    "BASIS_CONTRADICTORY": "The declared basis is contradictory.",
    "BASIS_INSUFFICIENT": "The declared basis is insufficient for lawful completion.",
    "EVIDENCE_MISSING_OR_MALFORMED": "Bounded relation evidence is missing or malformed.",
    "EVIDENCE_REFERENCE_MISMATCH": "Evidence must bind the exact selected-surface references.",
    "EVIDENCE_RELATION_UNSUPPORTED": "Evidence uses a relation outside the admitted family.",
    "EVIDENCE_ID_DUPLICATED": "Evidence identities must be unique.",
    "SCOPE_WIDENED": "The reconstruction widens its declared scope.",
    "FINDING_HIDDEN": "Mismatch, conflict, refusal, non-correspondence, or missing support is hidden.",
    "NEGATIVE_RELATION_OUTCOME_COLLAPSE": "A supported negative relation is collapsed into top-level no-correspondence.",
    "SIMILARITY_TREATED_AS_EQUIVALENCE": "Surface similarity is treated as equivalence.",
    "MANIFEST_ORDER_INFERENCE": "Manifest order is treated as rank, priority, authority, currentness, chronology, precedence, or weight.",
    "PROHIBITED_SELECTION_INFERENCE": "Selection is inferred from recency, availability, timestamp, filename, sequence, or directory position.",
    "LANDLORD_BEHAVIOR_CREATED": "The reconstruction creates registry, catalogue, coverage-ledger, or whole-body-mirror behavior.",
    "PROHIBITED_EMBEDDING": "The reconstruction embeds a complete artifact or recursive ancestry.",
    "RECONSTRUCTION_POSTURE_MISSING_OR_FLIPPED": "A required reconstruction guardrail is missing or flipped.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required result-level non-claim is missing or flipped.",
}
BLOCK_CODES = frozenset(BLOCK_REASONS)

NON_MEANING = (
    "correspondence_is_not_conformance",
    "reconstructability_is_not_coherence",
    "legibility_is_not_presence",
    "manifest_coverage_is_not_constitutional_inventory",
    "selection_is_not_universal_vocabulary_admission",
    "surface_similarity_is_not_equivalence",
    "mismatch_is_not_invalidation",
    "conflict_is_not_failure",
    "refusal_visibility_is_not_mandatory_participation",
    "non_correspondence_is_not_deletion_or_rejection",
    "receipt_is_not_current_state_or_latest_truth",
    "system_local_correspondence_is_not_field_correspondence",
    "intra_body_correspondence_is_not_cross_custody_answerability",
    "self_legibility_is_not_consciousness_identity_agency_sentience_or_biology",
)

OPEN_ITEMS = (
    "persisted_result",
    "receipt",
    "terminal_summary",
    "invocation_consumption_or_exhaustion",
    "repeat_prevention_or_operation_lifecycle",
    "self_orientation_or_conformance_successor",
    "presence_threshold_or_truth",
    "field_correspondence_or_cross_custody_answerability",
    "runtime_daemon_action_or_continuation",
)


def resolve_matter_bound_selected_surface_correspondence_v0_min_v2(
    request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Resolve one V2 correspondence reconstruction from one in-memory mapping."""

    checks: list[dict[str, Any]] = []
    matter: dict[str, Any] | None = None
    manifest: list[dict[str, Any]] = []
    question: dict[str, Any] | None = None
    basis: dict[str, Any] | None = None

    def passed(check_id: str) -> None:
        checks.append({"check_id": check_id, "passed": True, "block_code": None})

    def blocked(check_id: str, code: str) -> dict[str, Any]:
        checks.append({"check_id": check_id, "passed": False, "block_code": code})
        return _build_result(
            outcome=BLOCKED,
            matter=matter,
            manifest=manifest,
            question=question,
            basis=basis,
            finding=None,
            checks=checks,
            block_code=code,
        )

    if not isinstance(request, Mapping):
        return blocked("request_is_one_mapping", "REQUEST_NOT_MAPPING")
    if frozenset(request) != REQUEST_KEYS:
        return blocked("request_has_exact_keys", "REQUEST_KEYS_INVALID")
    passed("request_has_exact_keys")

    matter, matter_error = _normalize_matter(request.get("matter"))
    if matter_error:
        return blocked("matter_is_explicit_and_bounded", matter_error)
    passed("matter_is_explicit_and_bounded")

    manifest, manifest_error = _normalize_manifest(request.get("selected_surface_manifest"))
    if manifest_error:
        return blocked("manifest_is_closed_ordered_and_exact", manifest_error)
    passed("manifest_is_closed_ordered_and_exact")

    question, question_error = _normalize_question(
        request.get("declared_correspondence_question"), matter, manifest
    )
    if question_error:
        return blocked("question_is_singular_and_exact", question_error)
    passed("question_is_singular_and_exact")

    basis, basis_error = _normalize_basis(request.get("correspondence_basis"), manifest)
    if basis_error:
        return blocked("basis_is_readable_available_and_sufficient", basis_error)
    passed("basis_is_readable_available_and_sufficient")

    posture_error = _validate_reconstruction_posture(request.get("reconstruction_posture"))
    if posture_error:
        return blocked("reconstruction_guardrails_remain_false", posture_error)
    passed("reconstruction_guardrails_remain_false")

    non_claim_error = _validate_exact_false_mapping(
        request.get("declared_non_claims"), REQUIRED_FALSE_NON_CLAIMS
    )
    if non_claim_error:
        return blocked("required_non_claims_remain_false", "NON_CLAIM_MISSING_OR_FLIPPED")
    passed("required_non_claims_remain_false")

    relation_type = question["relation_type"]
    supporting_evidence_ids = [
        item["evidence_id"]
        for item in basis["evidence_items"]
        if item["relation_type"] == relation_type
        and item["relation_supported"] is True
    ]
    relation_supported = bool(supporting_evidence_ids)
    finding = {
        "finding_code": (
            "DECLARED_RELATION_SUPPORTED"
            if relation_supported
            else "DECLARED_RELATION_NOT_SUPPORTED"
        ),
        "declared_relation_type": relation_type,
        "declared_relation_supported": relation_supported,
        "supporting_evidence_ids": supporting_evidence_ids,
    }
    passed("declared_relation_support_derived_from_exact_evidence")

    outcome = CORRESPONDENCE_RECOGNIZED if relation_supported else NO_CORRESPONDENCE
    return _build_result(
        outcome=outcome,
        matter=matter,
        manifest=manifest,
        question=question,
        basis=basis,
        finding=finding,
        checks=checks,
        block_code=None,
    )


def _normalize_matter(value: Any) -> tuple[dict[str, Any] | None, str | None]:
    if not isinstance(value, Mapping) or frozenset(value) != MATTER_KEYS:
        return None, "MATTER_MISSING_OR_MALFORMED"
    if not all(_has_text(value.get(key)) for key in MATTER_KEYS):
        return None, "MATTER_MISSING_OR_MALFORMED"
    return {key: str(value[key]) for key in MATTER_FIELD_ORDER}, None


def _normalize_manifest(value: Any) -> tuple[list[dict[str, Any]], str | None]:
    if not isinstance(value, list):
        return [], "MANIFEST_MISSING_OR_MALFORMED"
    if len(value) < 2:
        return [], "MANIFEST_TOO_SMALL"

    normalized: list[dict[str, Any]] = []
    for entry in value:
        if not isinstance(entry, Mapping) or frozenset(entry) != SURFACE_KEYS:
            return [], "SELECTED_SURFACE_MALFORMED"
        text_keys = (
            "surface_id",
            "surface_reference",
            "surface_outcome",
            "surface_rank",
            "source_basis",
            "surface_scope",
            "source_downstream_posture",
        )
        if not all(_has_text(entry.get(key)) for key in text_keys):
            return [], "SELECTED_SURFACE_MALFORMED"
        position = entry.get("selected_position")
        if not isinstance(position, int) or isinstance(position, bool):
            return [], "MANIFEST_POSITION_INVALID"
        lineage = _text_list(entry.get("lineage_references"), require_nonempty=True)
        if lineage is None:
            return [], "SELECTED_SURFACE_MALFORMED"
        surface_non_claims = entry.get("non_claims")
        if not isinstance(surface_non_claims, Mapping) or not surface_non_claims:
            return [], "SELECTED_SURFACE_NON_CLAIMS_INVALID"
        if any(
            not _has_text(key) or value is not False
            for key, value in surface_non_claims.items()
        ):
            return [], "SELECTED_SURFACE_NON_CLAIMS_INVALID"
        normalized.append(
            {
                "selected_position": position,
                **{key: str(entry[key]) for key in text_keys},
                "lineage_references": lineage,
                "non_claims": {
                    str(key): False for key in sorted(surface_non_claims)
                },
            }
        )

    expected_positions = list(range(1, len(normalized) + 1))
    if [entry["selected_position"] for entry in normalized] != expected_positions:
        return [], "MANIFEST_POSITION_INVALID"
    ids = [entry["surface_id"] for entry in normalized]
    references = [entry["surface_reference"] for entry in normalized]
    if len(set(ids)) != len(ids) or len(set(references)) != len(references):
        return [], "MANIFEST_IDENTITY_DUPLICATED"
    return normalized, None


def _normalize_question(
    value: Any,
    matter: Mapping[str, Any],
    manifest: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str | None]:
    if not isinstance(value, Mapping):
        return None, "QUESTION_MISSING_OR_MULTIPLE"
    if frozenset(value) != QUESTION_KEYS:
        return None, "QUESTION_MALFORMED"
    for key in ("question_id", "matter_id", "bounded_claim"):
        if not _has_text(value.get(key)):
            return None, "QUESTION_MALFORMED"
    direction = value.get("direction")
    if direction is not None and not _has_text(direction):
        return None, "QUESTION_MALFORMED"

    relation_type = value.get("relation_type")
    if not isinstance(relation_type, str):
        return None, "RELATION_TYPE_MISSING_OR_MULTIPLE"
    if relation_type not in ADMITTED_RELATION_TYPES:
        return None, "RELATION_TYPE_UNSUPPORTED"

    selected_ids = _text_list(value.get("selected_surface_ids"), require_nonempty=True)
    if selected_ids is None:
        return None, "QUESTION_MALFORMED"
    basis_references = _text_list(value.get("basis_references"), require_nonempty=True)
    if basis_references is None:
        return None, "QUESTION_MALFORMED"
    if value["matter_id"] != matter["matter_id"]:
        return None, "QUESTION_MATTER_MISMATCH"
    if selected_ids != [entry["surface_id"] for entry in manifest]:
        return None, "QUESTION_SURFACE_MISMATCH"
    if basis_references != [entry["surface_reference"] for entry in manifest]:
        return None, "QUESTION_BASIS_REFERENCE_MISMATCH"

    return {
        "question_id": str(value["question_id"]),
        "matter_id": str(value["matter_id"]),
        "selected_surface_ids": selected_ids,
        "relation_type": relation_type,
        "direction": None if direction is None else str(direction),
        "bounded_claim": str(value["bounded_claim"]),
        "basis_references": basis_references,
    }, None


def _normalize_basis(
    value: Any,
    manifest: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str | None]:
    if not isinstance(value, Mapping) or frozenset(value) != BASIS_KEYS:
        return None, "BASIS_MISSING_OR_MALFORMED"
    for key in ("readable", "available", "sufficient", "contradictory"):
        if type(value.get(key)) is not bool:
            return None, "BASIS_MISSING_OR_MALFORMED"
    if value["readable"] is not True:
        return None, "BASIS_UNREADABLE"
    if value["available"] is not True:
        return None, "BASIS_UNAVAILABLE"
    if value["contradictory"] is not False:
        return None, "BASIS_CONTRADICTORY"
    if value["sufficient"] is not True:
        return None, "BASIS_INSUFFICIENT"

    items = value.get("evidence_items")
    if not isinstance(items, list) or not items:
        return None, "EVIDENCE_MISSING_OR_MALFORMED"
    expected_references = [entry["surface_reference"] for entry in manifest]
    normalized_items: list[dict[str, Any]] = []
    evidence_ids: list[str] = []
    for item in items:
        if not isinstance(item, Mapping) or frozenset(item) != EVIDENCE_KEYS:
            return None, "EVIDENCE_MISSING_OR_MALFORMED"
        if not _has_text(item.get("evidence_id")) or not _has_text(item.get("basis_fact")):
            return None, "EVIDENCE_MISSING_OR_MALFORMED"
        relation_type = item.get("relation_type")
        if not isinstance(relation_type, str) or relation_type not in ADMITTED_RELATION_TYPES:
            return None, "EVIDENCE_RELATION_UNSUPPORTED"
        if type(item.get("relation_supported")) is not bool:
            return None, "EVIDENCE_MISSING_OR_MALFORMED"
        references = _text_list(item.get("surface_references"), require_nonempty=True)
        if references != expected_references:
            return None, "EVIDENCE_REFERENCE_MISMATCH"
        evidence_id = str(item["evidence_id"])
        evidence_ids.append(evidence_id)
        normalized_items.append(
            {
                "evidence_id": evidence_id,
                "surface_references": references,
                "relation_type": relation_type,
                "relation_supported": item["relation_supported"],
                "basis_fact": str(item["basis_fact"]),
            }
        )
    if len(set(evidence_ids)) != len(evidence_ids):
        return None, "EVIDENCE_ID_DUPLICATED"

    return {
        "readable": True,
        "available": True,
        "sufficient": True,
        "contradictory": False,
        "evidence_items": normalized_items,
    }, None


def _validate_reconstruction_posture(value: Any) -> str | None:
    invalid_key = _validate_exact_false_mapping(
        value, REQUIRED_FALSE_RECONSTRUCTION_POSTURES
    )
    if invalid_key is None:
        return None
    if invalid_key == "scope_widened":
        return "SCOPE_WIDENED"
    if invalid_key in {
        "mismatch_hidden",
        "conflict_hidden",
        "refusal_hidden",
        "non_correspondence_hidden",
        "missing_support_hidden",
    }:
        return "FINDING_HIDDEN"
    if invalid_key == "supported_negative_relation_treated_as_no_correspondence":
        return "NEGATIVE_RELATION_OUTCOME_COLLAPSE"
    if invalid_key == "similarity_treated_as_equivalence":
        return "SIMILARITY_TREATED_AS_EQUIVALENCE"
    if invalid_key in {
        "rank_inferred_from_manifest_order",
        "priority_inferred_from_manifest_order",
        "authority_inferred_from_manifest_order",
        "currentness_inferred_from_manifest_order",
        "chronology_inferred_from_manifest_order",
        "precedence_inferred_from_manifest_order",
        "semantic_weight_inferred_from_manifest_order",
    }:
        return "MANIFEST_ORDER_INFERENCE"
    if invalid_key in {
        "recency_inference_used",
        "repository_availability_inference_used",
        "timestamp_inference_used",
        "filename_inference_used",
        "sequence_inference_used",
        "directory_position_inference_used",
    }:
        return "PROHIBITED_SELECTION_INFERENCE"
    if invalid_key in {
        "registry_behavior_created",
        "catalogue_behavior_created",
        "coverage_ledger_created",
        "whole_body_mirror_created",
    }:
        return "LANDLORD_BEHAVIOR_CREATED"
    if invalid_key in {"complete_artifact_embedded", "recursive_ancestry_embedded"}:
        return "PROHIBITED_EMBEDDING"
    return "RECONSTRUCTION_POSTURE_MISSING_OR_FLIPPED"


def _validate_exact_false_mapping(
    value: Any, required_keys: tuple[str, ...]
) -> str | None:
    if not isinstance(value, Mapping):
        return "__mapping__"
    if frozenset(value) != frozenset(required_keys):
        return "__keys__"
    for key in required_keys:
        if value.get(key) is not False:
            return key
    return None


def _build_result(
    *,
    outcome: str,
    matter: Mapping[str, Any] | None,
    manifest: list[dict[str, Any]],
    question: Mapping[str, Any] | None,
    basis: Mapping[str, Any] | None,
    finding: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
    block_code: str | None,
) -> dict[str, Any]:
    normalized_matter = None if matter is None else dict(matter)
    normalized_manifest = [
        {
            **{key: value for key, value in entry.items() if key not in {"lineage_references", "non_claims"}},
            "lineage_references": list(entry["lineage_references"]),
            "non_claims": dict(entry["non_claims"]),
        }
        for entry in manifest
    ]
    normalized_question = None
    if question is not None:
        normalized_question = {
            **{key: value for key, value in question.items() if key not in {"selected_surface_ids", "basis_references"}},
            "selected_surface_ids": list(question["selected_surface_ids"]),
            "basis_references": list(question["basis_references"]),
        }
    normalized_basis = None
    if basis is not None:
        normalized_basis = {
            "readable": basis["readable"],
            "available": basis["available"],
            "sufficient": basis["sufficient"],
            "contradictory": basis["contradictory"],
            "evidence_items": [
                {
                    **{key: value for key, value in item.items() if key != "surface_references"},
                    "surface_references": list(item["surface_references"]),
                }
                for item in basis["evidence_items"]
            ],
        }
    normalized_finding = None
    if finding is not None:
        normalized_finding = {
            "finding_code": finding["finding_code"],
            "declared_relation_type": finding["declared_relation_type"],
            "declared_relation_supported": finding["declared_relation_supported"],
            "supporting_evidence_ids": list(finding["supporting_evidence_ids"]),
        }

    return {
        "metadata": {
            "matter_bound_selected_surface_correspondence_type": CORRESPONDENCE_TYPE,
            "matter_bound_selected_surface_correspondence_version": CORRESPONDENCE_VERSION,
            "matter_bound_selected_surface_correspondence_scope": CORRESPONDENCE_SCOPE,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
        },
        "matter": normalized_matter,
        "selected_surface_manifest": normalized_manifest,
        "declared_correspondence_question": normalized_question,
        "correspondence_basis": normalized_basis,
        "finding": normalized_finding,
        "checks": [dict(check) for check in checks],
        "result": {
            "outcome": outcome,
            "completion_posture": outcome,
            "bounded_completion_recorded": outcome != BLOCKED,
            "bounded_stopping_recorded": outcome == BLOCKED,
        },
        "non_meaning": list(NON_MEANING),
        "what_remains_open": {
            "open_items": list(OPEN_ITEMS),
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
            "open_does_not_mean_next": True,
        },
        "non_claims": dict(CANONICAL_NON_CLAIMS),
        "outcome": outcome,
        "block": {
            "code": block_code,
            "reason": None if block_code is None else BLOCK_REASONS[block_code],
        },
    }


def _text_list(value: Any, *, require_nonempty: bool) -> list[str] | None:
    if not isinstance(value, list):
        return None
    if require_nonempty and not value:
        return None
    if not all(_has_text(item) for item in value):
        return None
    result = [str(item) for item in value]
    if len(set(result)) != len(result):
        return None
    return result


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


__all__ = [
    "ADMITTED_RELATION_TYPES",
    "BLOCKED",
    "BLOCK_CODES",
    "CANONICAL_NON_CLAIMS",
    "CORRESPONDENCE_RECOGNIZED",
    "CORRESPONDENCE_SCOPE",
    "CORRESPONDENCE_TYPE",
    "CORRESPONDENCE_VERSION",
    "NEGATIVE_RELATION_TYPES",
    "NO_CORRESPONDENCE",
    "OUTCOMES",
    "REQUIRED_FALSE_NON_CLAIMS",
    "REQUIRED_FALSE_RECONSTRUCTION_POSTURES",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "resolve_matter_bound_selected_surface_correspondence_v0_min_v2",
]
