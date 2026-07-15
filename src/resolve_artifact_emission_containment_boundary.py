"""Resolve the artifact emission containment boundary.

This resolver records one bounded posture only: future artifacts should
preserve selected prior results by reference-shaped summaries instead of
recursively embedding full upstream artifacts. It does not mutate prior
artifacts, compact artifacts, invalidate artifacts by size, implement commands,
or authorize any next work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class ArtifactEmissionContainmentBoundaryError(Exception):
    """Raised for hard containment-boundary input/output failures."""


RESOLVER_MODULE = "resolve_artifact_emission_containment_boundary"
RESULT_VERSION = "0.1.0"

ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_artifact_emission_containment_boundary"
)

OUTCOME_RECORDED = "ARTIFACT_EMISSION_CONTAINMENT_RECORDED"
OUTCOME_NOT_RECORDED = "ARTIFACT_EMISSION_CONTAINMENT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = "ARTIFACT_EMISSION_CONTAINMENT_REQUIRES_ADDITIONAL_BASIS"
OUTCOME_BLOCKED = "ARTIFACT_EMISSION_CONTAINMENT_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_ARTIFACT_EMISSION_CONTAINMENT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_ARTIFACT_EMISSION_CONTAINMENT"
INTENT_BLOCK = "BLOCK_ARTIFACT_EMISSION_CONTAINMENT_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_CONTAINMENT_SCOPE = {
    "ARTIFACT_EMISSION_CONTAINMENT_ONLY",
    "REFERENCE_ONLY_SELECTED_BASIS_REQUIRED",
    "SUMMARY_PLUS_REFERENCE_EMISSION_REQUIRED",
    "RECURSIVE_FULL_ARTIFACT_EMBEDDING_BLOCKED",
    "PRIOR_ARTIFACTS_PRESERVED_BY_REFERENCE",
    "PRIOR_ARTIFACTS_NOT_MUTATED",
    "PRIOR_ARTIFACTS_NOT_DELETED",
    "PRIOR_ARTIFACTS_NOT_COMPACTED",
    "PRIOR_ARTIFACTS_NOT_INVALIDATED_BY_SIZE",
    "CONTAINMENT_IS_NOT_CLEANUP",
    "CONTAINMENT_IS_NOT_MIGRATION",
    "CONTAINMENT_IS_NOT_COMMAND",
    "CONTAINMENT_IS_NOT_MANIFEST_IMPLEMENTATION",
    "CONTAINMENT_DOES_NOT_CREATE_CURRENTNESS",
    "CONTAINMENT_DOES_NOT_AUTHORIZE_NEXT_WORK",
}

ALLOWED_REFERENCE_FIELDS = (
    "selected_result_id",
    "selected_result_path",
    "selected_result_outcome",
    "selected_result_failed_check_count",
    "selected_result_passed_check_count",
    "selected_result_summary",
    "selected_result_non_claims",
    "selected_result_basis_reference",
    "selected_result_artifact_family",
    "selected_result_artifact_size_class",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "prior_artifacts_mutated",
    "prior_artifacts_deleted",
    "prior_artifacts_compacted",
    "prior_artifacts_rewritten",
    "prior_artifacts_invalidated_by_size",
    "old_artifacts_replaced",
    "reference_record_became_source",
    "summary_became_source",
    "path_created_currentness",
    "artifact_existence_created_currentness",
    "containment_created_currentness",
    "command_implemented",
    "command_executed",
    "command_authorized_to_run",
    "manifest_implemented",
    "checksum_implemented",
    "signature_implemented",
    "packet_implemented",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
    "source_transferred",
    "source_migrated",
    "source_received",
    "source_receipt_recorded",
    "reception_authorized",
    "operation_permission_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "another_reception_request_authorized",
    "follow_on_work_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "artifact_emission_containment_recorded",
    "reference_only_selected_basis_required",
    "recursive_full_artifact_embedding_blocked",
    "summary_plus_reference_emission_required",
    "prior_artifacts_preserved_by_reference",
)

OUTPUT_FALSE_POSTURE = tuple(
    dict.fromkeys(
        REQUIRED_FALSE_NON_CLAIMS
        + (
            "artifact_cleanup_authorized",
            "artifact_deletion_authorized",
            "artifact_compaction_authorized",
            "artifact_rewrite_authorized",
            "artifact_repair_authorized",
            "artifact_normalization_authorized",
            "artifact_migration_authorized",
            "command_exists",
            "manifest_exists",
            "checksum_exists",
            "signature_exists",
            "packet_exists",
            "authority_created",
            "currentness_created",
            "public_readiness_created",
            "source_receipt_created",
            "next_work_authorized",
        )
    )
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = {
    "prior_artifacts_mutated": "CONTAINMENT_MUTATES_PRIOR_ARTIFACTS",
    "review_mutates_prior_artifacts": "CONTAINMENT_MUTATES_PRIOR_ARTIFACTS",
    "artifact_mutation_performed": "CONTAINMENT_MUTATES_PRIOR_ARTIFACTS",
    "prior_artifacts_deleted": "CONTAINMENT_DELETES_PRIOR_ARTIFACTS",
    "artifact_deletion_authorized": "CONTAINMENT_DELETES_PRIOR_ARTIFACTS",
    "prior_artifacts_compacted": "CONTAINMENT_COMPACTS_PRIOR_ARTIFACTS",
    "artifact_compaction_authorized": "CONTAINMENT_COMPACTS_PRIOR_ARTIFACTS",
    "prior_artifacts_rewritten": "CONTAINMENT_REWRITES_PRIOR_ARTIFACTS",
    "old_artifacts_replaced": "CONTAINMENT_REWRITES_PRIOR_ARTIFACTS",
    "artifact_rewrite_authorized": "CONTAINMENT_REWRITES_PRIOR_ARTIFACTS",
    "prior_artifacts_invalidated_by_size": "CONTAINMENT_INVALIDATES_PRIOR_ARTIFACTS_BY_SIZE",
    "artifact_invalidated_by_size": "CONTAINMENT_INVALIDATES_PRIOR_ARTIFACTS_BY_SIZE",
    "reference_record_became_source": "REFERENCE_RECORD_TREATED_AS_SOURCE",
    "reference_record_treated_as_source": "REFERENCE_RECORD_TREATED_AS_SOURCE",
    "summary_became_source": "SUMMARY_TREATED_AS_SOURCE",
    "summary_treated_as_source": "SUMMARY_TREATED_AS_SOURCE",
    "path_created_currentness": "PATH_TREATED_AS_CURRENTNESS",
    "path_treated_as_currentness": "PATH_TREATED_AS_CURRENTNESS",
    "artifact_existence_created_currentness": "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
    "artifact_existence_treated_as_currentness": "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
    "containment_created_currentness": "CONTAINMENT_CREATES_CURRENTNESS",
    "containment_treated_as_currentness": "CONTAINMENT_CREATES_CURRENTNESS",
    "command_implemented": "CONTAINMENT_AUTHORIZES_COMMAND_IMPLEMENTATION",
    "command_implementation_authorized": "CONTAINMENT_AUTHORIZES_COMMAND_IMPLEMENTATION",
    "command_executed": "CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION",
    "command_authorized_to_run": "CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION",
    "command_execution_authorized": "CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION",
    "manifest_implemented": "CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION",
    "checksum_implemented": "CONTAINMENT_CREATES_CHECKSUM_IMPLEMENTATION",
    "signature_implemented": "CONTAINMENT_CREATES_SIGNATURE_IMPLEMENTATION",
    "packet_implemented": "CONTAINMENT_CREATES_PACKET_IMPLEMENTATION",
    "deployment_created": "CONTAINMENT_CREATES_DEPLOYMENT",
    "runtime_hosting_created": "CONTAINMENT_CREATES_RUNTIME_HOSTING",
    "public_release_created": "CONTAINMENT_CREATES_PUBLIC_RELEASE",
    "source_transferred": "CONTAINMENT_AUTHORIZES_TRANSFER",
    "source_migrated": "CONTAINMENT_AUTHORIZES_MIGRATION",
    "source_received": "CONTAINMENT_AUTHORIZES_SOURCE_RECEIPT",
    "source_receipt_recorded": "CONTAINMENT_AUTHORIZES_SOURCE_RECEIPT",
    "source_receipt_created": "CONTAINMENT_AUTHORIZES_SOURCE_RECEIPT",
    "reception_authorized": "CONTAINMENT_AUTHORIZES_RECEPTION",
    "operation_permission_created": "CONTAINMENT_CREATES_OPERATION_PERMISSION",
    "public_launch_readiness_created": "CONTAINMENT_CREATES_PUBLIC_READINESS",
    "final_completion_claimed": "CONTAINMENT_CLAIMS_FINAL_COMPLETION",
    "continuation_authorized": "CONTAINMENT_AUTHORIZES_CONTINUATION",
    "publication_flow_opened": "CONTAINMENT_AUTHORIZES_CONTINUATION",
    "reusable_permission_created": "CONTAINMENT_CREATES_REUSABLE_PERMISSION",
    "derivative_reception_authorized": "CONTAINMENT_AUTHORIZES_DERIVATIVE_RECEPTION",
    "vessel_relation_authorized": "CONTAINMENT_AUTHORIZES_VESSEL_RELATION",
    "another_reception_request_authorized": "CONTAINMENT_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
    "successor_reception_request_authorized": "CONTAINMENT_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
    "follow_on_work_authorized": "CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK",
}


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "recorded", "blocked"}
    return bool(value)


def _false_only(value: Any) -> bool:
    return isinstance(value, bool) and value is False


def _safe_component(value: Any) -> str:
    text = str(value or "artifact_emission_containment").strip()
    cleaned = []
    for char in text:
        if char.isalnum() or char in {"-", "_"}:
            cleaned.append(char)
        else:
            cleaned.append("_")
    component = "".join(cleaned).strip("_")
    return component or "artifact_emission_containment"


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    path = Path(path_value)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, "DECLARED_CONTAINMENT_REQUEST_UNREADABLE"
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None, "DECLARED_CONTAINMENT_REQUEST_MALFORMED"
    if not isinstance(data, dict):
        return None, "DECLARED_CONTAINMENT_REQUEST_MALFORMED"
    return data, None


def _normalize_basis(value: Any, reference_key: str) -> Any:
    if isinstance(value, Mapping):
        return _deepcopy(dict(value))
    if isinstance(value, str) and value.strip():
        return {
            reference_key: value,
            "basis_reference": value,
            "basis_is_reference_only": True,
        }
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return _deepcopy(list(value))
    return _deepcopy(value)


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, Mapping):
        raw_values = scope.get("selected_scope_values", scope.get("scope_values", scope.get("values", [])))
        if isinstance(raw_values, str):
            return [raw_values]
        if isinstance(raw_values, Sequence) and not isinstance(raw_values, (bytes, bytearray)):
            return [str(value) for value in raw_values]
        return []
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Sequence) and not isinstance(scope, (bytes, bytearray)):
        return [str(value) for value in scope]
    return []


def _contains_truthy_key(value: Any, target_key: str) -> bool:
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            if key == target_key and _truthy(nested_value):
                return True
            if _contains_truthy_key(nested_value, target_key):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, target_key) for item in value)
    return False


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "code": code,
        "reason": reason if reason is not None else code,
    }


def _required_non_claims_false(request: Mapping[str, Any]) -> tuple[bool, str | None]:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False, "declared_non_claims missing or malformed"
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field not in non_claims or not _false_only(non_claims.get(field)):
            return False, field
    return True, None


def _collapse_code(request: Mapping[str, Any]) -> str | None:
    for field in MUTATION_FLAGS:
        if _contains_truthy_key(request, field):
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    for field, code in COLLAPSE_FIELD_CODES.items():
        if _contains_truthy_key(request, field):
            return code
    return None


def _false_posture_for_outcome(outcome: str) -> dict[str, bool]:
    posture = {field: False for field in OUTPUT_FALSE_POSTURE}
    for field in ALLOWED_RECORDED_TRUE_FIELDS:
        posture[field] = outcome == OUTCOME_RECORDED
    return posture


def _containment_non_meaning() -> dict[str, bool]:
    return {
        "containment_does_not_mean_existing_artifacts_invalid": True,
        "containment_does_not_mean_existing_artifacts_deleted": True,
        "containment_does_not_mean_existing_artifacts_compacted": True,
        "containment_does_not_mean_existing_artifacts_rewritten": True,
        "containment_does_not_mean_existing_artifacts_repaired": True,
        "containment_does_not_mean_existing_artifacts_normalized": True,
        "containment_does_not_mean_existing_artifacts_migrated": True,
        "containment_does_not_mean_old_artifacts_replaced": True,
        "containment_does_not_mean_smaller_artifacts_create_currentness": True,
        "containment_does_not_mean_reference_record_became_source": True,
        "containment_does_not_mean_summary_became_source": True,
        "containment_does_not_mean_path_created_currentness": True,
        "containment_does_not_mean_artifact_existence_created_currentness": True,
        "containment_does_not_mean_command_exists": True,
        "containment_does_not_mean_manifest_exists": True,
        "containment_does_not_mean_checksum_exists": True,
        "containment_does_not_mean_signature_exists": True,
        "containment_does_not_mean_packet_exists": True,
        "containment_does_not_mean_deployment_authorized": True,
        "containment_does_not_mean_runtime_hosting_authorized": True,
        "containment_does_not_mean_public_release_authorized": True,
        "containment_does_not_mean_final_completion_claimed": True,
        "containment_does_not_mean_follow_on_work_authorized": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "artifact emission containment test",
            "artifact emission containment live artifact",
            "command-boundary live artifact rerun using contained reference shape",
            "portable verification command implementation",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
            "receiving-context governance",
            "public readiness",
            "final completion",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "follow-on work",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _selected_artifact_emission_pressure_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "selected_artifact_emission_pressure_basis": _normalize_basis(
            request.get("selected_artifact_emission_pressure_basis"),
            "selected_artifact_emission_pressure_basis_reference",
        ),
        "selected_large_artifact_evidence": _normalize_basis(
            request.get("selected_large_artifact_evidence"),
            "selected_large_artifact_evidence_reference",
        ),
        "selected_heavy_artifact_evidence": _normalize_basis(
            request.get("selected_heavy_artifact_evidence"),
            "selected_heavy_artifact_evidence_reference",
        ),
        "selected_artifact_size_pressure_basis": _normalize_basis(
            request.get("selected_artifact_size_pressure_basis"),
            "selected_artifact_size_pressure_basis_reference",
        ),
        "selected_carrier_shape_pressure_basis": _normalize_basis(
            request.get("selected_carrier_shape_pressure_basis"),
            "selected_carrier_shape_pressure_basis_reference",
        ),
        "heavy_artifacts_remain_standing_evidence_if_checks_passed": True,
        "heavy_artifact_evidence_does_not_become_source": True,
        "artifact_size_pressure_is_not_automatic_law_failure": True,
        "carrier_shape_pressure_is_not_currentness_or_authority": True,
        "containment_should_occur_before_further_recursive_live_artifact_emission": True,
    }


def _affected_artifact_families(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "affected_artifact_families": _normalize_basis(
            request.get("affected_artifact_families"),
            "affected_artifact_families_reference",
        ),
        "portable_source_body_verification_family_where_supplied": _normalize_basis(
            request.get("portable_source_body_verification_family"),
            "portable_source_body_verification_family_reference",
        ),
        "evidence_manifest_family_where_supplied": _normalize_basis(
            request.get("evidence_manifest_family"),
            "evidence_manifest_family_reference",
        ),
        "source_body_reception_closure_family_where_supplied": _normalize_basis(
            request.get("source_body_reception_closure_family"),
            "source_body_reception_closure_family_reference",
        ),
        "command_boundary_future_emission_family_where_supplied": _normalize_basis(
            request.get("command_boundary_future_emission_family"),
            "command_boundary_future_emission_family_reference",
        ),
        "affected_family_status_is_descriptive_only": True,
        "affected_family_status_does_not_invalidate_prior_artifacts": True,
    }


def _future_emission_family(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "future_emission_family": _normalize_basis(
            request.get("future_emission_family"),
            "future_emission_family_reference",
        ),
        "command_boundary_live_artifact_family_where_supplied": _normalize_basis(
            request.get("command_boundary_live_artifact_family"),
            "command_boundary_live_artifact_family_reference",
        ),
        "future_artifacts_should_use_reference_only_selected_basis": True,
        "future_artifacts_should_use_summary_plus_reference_emission": True,
        "future_artifacts_should_block_recursive_full_artifact_embedding": True,
        "future_emission_family_is_not_authorized_to_emit_until_separately_reviewed": True,
    }


def _containment_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "containment_basis": _normalize_basis(request.get("containment_basis"), "containment_basis_reference"),
        "reference_only_selected_basis_posture": _normalize_basis(
            request.get("reference_only_selected_basis_posture"),
            "reference_only_selected_basis_posture_reference",
        ),
        "summary_plus_reference_posture": _normalize_basis(
            request.get("summary_plus_reference_posture"),
            "summary_plus_reference_posture_reference",
        ),
        "prohibited_recursive_embedding_posture": _normalize_basis(
            request.get("recursive_embedding_block"),
            "recursive_embedding_block_reference",
        ),
        "prior_artifact_preservation_posture": _normalize_basis(
            request.get("prior_artifact_preservation_posture"),
            "prior_artifact_preservation_posture_reference",
        ),
        "no_prior_artifact_mutation_posture": _normalize_basis(
            request.get("no_prior_artifact_mutation_posture"),
            "no_prior_artifact_mutation_posture_reference",
        ),
        "no_artifact_invalidation_by_size_posture": _normalize_basis(
            request.get("no_artifact_invalidation_by_size_posture"),
            "no_artifact_invalidation_by_size_posture_reference",
        ),
        "containment_basis_does_not_create_cleanup": True,
        "containment_basis_does_not_create_migration": True,
        "containment_basis_does_not_create_command_or_manifest_implementation": True,
        "containment_basis_does_not_authorize_next_work": True,
    }


def _reference_only_selected_basis_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "reference_only_selected_basis_posture": _normalize_basis(
            request.get("reference_only_selected_basis_posture"),
            "reference_only_selected_basis_posture_reference",
        ),
        "selected_prior_result_reference_shape": _normalize_basis(
            request.get("selected_prior_result_reference_shape", request.get("reference_record_shape")),
            "selected_prior_result_reference_shape_reference",
        ),
        "allowed_reference_fields": list(ALLOWED_REFERENCE_FIELDS),
        "future_selected_results_represented_by_reference_records": True,
        "reference_records_do_not_become_source": True,
        "reference_records_do_not_create_currentness": True,
        "paths_do_not_create_currentness": True,
        "size_class_is_descriptive_only_and_not_validity": True,
    }


def _summary_plus_reference_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "summary_plus_reference_posture": _normalize_basis(
            request.get("summary_plus_reference_posture"),
            "summary_plus_reference_posture_reference",
        ),
        "summary_digest_basis": _normalize_basis(
            request.get("summary_digest_basis"),
            "summary_digest_basis_reference",
        ),
        "selected_non_claim_excerpt_basis": _normalize_basis(
            request.get("selected_non_claim_excerpt_basis"),
            "selected_non_claim_excerpt_basis_reference",
        ),
        "summaries_are_bounded_excerpts": True,
        "summary_digest_is_not_cryptographic_digest_unless_separately_specified": True,
        "selected_non_claim_excerpts_preserve_anti_collapse_posture": True,
        "summary_does_not_become_source": True,
        "summary_does_not_create_authority": True,
        "summary_does_not_create_currentness": True,
    }


def _recursive_embedding_block(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "recursive_embedding_block": _normalize_basis(
            request.get("recursive_embedding_block"),
            "recursive_embedding_block_reference",
        ),
        "recursive_full_artifact_embedding_blocked": True,
        "raw_full_artifact_body_embedding_prohibited_unless_separately_permitted": True,
        "full_artifact_bodies_should_not_be_nested_inside_future_artifacts": True,
        "prior_artifacts_preserved_by_reference": True,
        "prohibited_embedding_does_not_mutate_prior_artifacts": True,
    }


def _prior_artifact_preservation_posture(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "prior_artifact_preservation_posture": _normalize_basis(
            request.get("prior_artifact_preservation_posture"),
            "prior_artifact_preservation_posture_reference",
        ),
        "no_prior_artifact_mutation_posture": _normalize_basis(
            request.get("no_prior_artifact_mutation_posture"),
            "no_prior_artifact_mutation_posture_reference",
        ),
        "no_artifact_invalidation_by_size_posture": _normalize_basis(
            request.get("no_artifact_invalidation_by_size_posture"),
            "no_artifact_invalidation_by_size_posture_reference",
        ),
        "prior_artifacts_preserved_by_reference": True,
        "prior_artifacts_not_mutated": True,
        "prior_artifacts_not_deleted": True,
        "prior_artifacts_not_compacted": True,
        "prior_artifacts_not_rewritten": True,
        "prior_artifacts_not_repaired": True,
        "prior_artifacts_not_normalized": True,
        "prior_artifacts_not_migrated": True,
        "prior_artifacts_not_invalidated_by_size": True,
        "old_artifacts_not_replaced": True,
    }


def _containment_scope(request: Mapping[str, Any]) -> dict[str, Any]:
    values = _scope_values(request.get("containment_scope"))
    unsupported = [value for value in values if value not in SUPPORTED_CONTAINMENT_SCOPE]
    return {
        "selected_containment_scope_values": values,
        "all_selected_scope_values_supported": not unsupported,
        "unsupported_scope_values": unsupported,
        "artifact_emission_containment_only": "ARTIFACT_EMISSION_CONTAINMENT_ONLY" in values,
        "reference_only_selected_basis_required": "REFERENCE_ONLY_SELECTED_BASIS_REQUIRED" in values,
        "summary_plus_reference_emission_required": "SUMMARY_PLUS_REFERENCE_EMISSION_REQUIRED" in values,
        "recursive_full_artifact_embedding_blocked": "RECURSIVE_FULL_ARTIFACT_EMBEDDING_BLOCKED" in values,
        "prior_artifacts_preserved_by_reference": "PRIOR_ARTIFACTS_PRESERVED_BY_REFERENCE" in values,
        "prior_artifacts_not_mutated": "PRIOR_ARTIFACTS_NOT_MUTATED" in values,
        "prior_artifacts_not_deleted": "PRIOR_ARTIFACTS_NOT_DELETED" in values,
        "prior_artifacts_not_compacted": "PRIOR_ARTIFACTS_NOT_COMPACTED" in values,
        "prior_artifacts_not_invalidated_by_size": "PRIOR_ARTIFACTS_NOT_INVALIDATED_BY_SIZE" in values,
        "containment_is_not_cleanup": "CONTAINMENT_IS_NOT_CLEANUP" in values,
        "containment_is_not_migration": "CONTAINMENT_IS_NOT_MIGRATION" in values,
        "containment_is_not_command": "CONTAINMENT_IS_NOT_COMMAND" in values,
        "containment_is_not_manifest_implementation": "CONTAINMENT_IS_NOT_MANIFEST_IMPLEMENTATION" in values,
        "containment_does_not_create_currentness": "CONTAINMENT_DOES_NOT_CREATE_CURRENTNESS" in values,
        "containment_does_not_authorize_next_work": "CONTAINMENT_DOES_NOT_AUTHORIZE_NEXT_WORK" in values,
    }


def _has_no_mutation_posture(request: Mapping[str, Any]) -> bool:
    if _present(request.get("no_prior_artifact_mutation_posture")):
        return True
    preservation = request.get("prior_artifact_preservation_posture")
    if isinstance(preservation, Mapping) and any(
        _truthy(preservation.get(field))
        for field in (
            "prior_artifacts_not_mutated",
            "prior_artifacts_not_deleted",
            "prior_artifacts_not_compacted",
            "prior_artifacts_not_rewritten",
        )
    ):
        return True
    basis = request.get("containment_basis")
    if isinstance(basis, Mapping) and _truthy(basis.get("no_prior_artifact_mutation_posture_declared")):
        return True
    return False


def _has_no_invalidation_posture(request: Mapping[str, Any]) -> bool:
    if _present(request.get("no_artifact_invalidation_by_size_posture")):
        return True
    preservation = request.get("prior_artifact_preservation_posture")
    if isinstance(preservation, Mapping) and _truthy(preservation.get("prior_artifacts_not_invalidated_by_size")):
        return True
    basis = request.get("containment_basis")
    if isinstance(basis, Mapping) and _truthy(basis.get("no_artifact_invalidation_by_size_posture_declared")):
        return True
    return False


def _build_checks(request: Mapping[str, Any], malformed_code: str | None = None) -> list[dict[str, Any]]:
    if malformed_code:
        return [
            _check(
                "declared containment request readable mapping",
                False,
                "declared containment request must be a readable JSON object or mapping",
                malformed_code,
                malformed_code,
            )
        ]

    intent = request.get("containment_intent")
    scope = _containment_scope(request)
    non_claims_ok, non_claim_issue = _required_non_claims_false(request)
    collapse = _collapse_code(request)

    checks = [
        _check(
            "containment question declared",
            _present(request.get("containment_question")),
            "containment question must be declared",
            request.get("containment_question"),
            "CONTAINMENT_QUESTION_UNDECLARED",
        ),
        _check(
            "containment intent supported",
            intent in SUPPORTED_INTENTS,
            "containment intent must be supported",
            intent,
            "CONTAINMENT_INTENT_UNSUPPORTED",
        ),
        _check(
            "artifact-emission pressure basis declared",
            _present(request.get("selected_artifact_emission_pressure_basis")),
            "artifact-emission pressure basis must be declared",
            request.get("selected_artifact_emission_pressure_basis"),
            "ARTIFACT_EMISSION_PRESSURE_BASIS_MISSING",
        ),
        _check(
            "affected artifact family declared",
            _present(request.get("affected_artifact_families")),
            "affected artifact family must be declared",
            request.get("affected_artifact_families"),
            "AFFECTED_ARTIFACT_FAMILY_MISSING",
        ),
        _check(
            "future emission family declared",
            _present(request.get("future_emission_family")),
            "future emission family must be declared",
            request.get("future_emission_family"),
            "FUTURE_EMISSION_FAMILY_MISSING",
        ),
        _check(
            "containment basis declared",
            _present(request.get("containment_basis")),
            "containment basis must be declared",
            request.get("containment_basis"),
            "CONTAINMENT_BASIS_MISSING",
        ),
        _check(
            "reference-only selected-basis posture declared",
            _present(request.get("reference_only_selected_basis_posture")),
            "reference-only selected-basis posture must be declared",
            request.get("reference_only_selected_basis_posture"),
            "REFERENCE_ONLY_SELECTED_BASIS_POSTURE_MISSING",
        ),
        _check(
            "summary-plus-reference posture declared",
            _present(request.get("summary_plus_reference_posture")),
            "summary-plus-reference posture must be declared",
            request.get("summary_plus_reference_posture"),
            "SUMMARY_PLUS_REFERENCE_POSTURE_MISSING",
        ),
        _check(
            "recursive full-artifact embedding blocked",
            _present(request.get("recursive_embedding_block")),
            "recursive full-artifact embedding block must be declared",
            request.get("recursive_embedding_block"),
            "RECURSIVE_EMBEDDING_BLOCK_MISSING",
        ),
        _check(
            "prior artifacts preserved by reference",
            _present(request.get("prior_artifact_preservation_posture")),
            "prior artifact preservation posture must be declared",
            request.get("prior_artifact_preservation_posture"),
            "PRIOR_ARTIFACT_PRESERVATION_POSTURE_MISSING",
        ),
        _check(
            "prior artifacts not mutated",
            _has_no_mutation_posture(request),
            "no-prior-artifact-mutation posture must be declared",
            _first_present(
                request.get("no_prior_artifact_mutation_posture"),
                request.get("prior_artifact_preservation_posture"),
            ),
            "NO_MUTATION_POSTURE_MISSING",
        ),
        _check(
            "prior artifacts not deleted",
            not _contains_truthy_key(request, "prior_artifacts_deleted"),
            "containment must not delete prior artifacts",
            request.get("declared_non_claims", {}).get("prior_artifacts_deleted")
            if isinstance(request.get("declared_non_claims"), Mapping)
            else None,
            "CONTAINMENT_DELETES_PRIOR_ARTIFACTS",
        ),
        _check(
            "prior artifacts not compacted",
            not _contains_truthy_key(request, "prior_artifacts_compacted"),
            "containment must not compact prior artifacts",
            request.get("declared_non_claims", {}).get("prior_artifacts_compacted")
            if isinstance(request.get("declared_non_claims"), Mapping)
            else None,
            "CONTAINMENT_COMPACTS_PRIOR_ARTIFACTS",
        ),
        _check(
            "prior artifacts not invalidated by size",
            _has_no_invalidation_posture(request),
            "no-artifact-invalidation-by-size posture must be declared",
            _first_present(
                request.get("no_artifact_invalidation_by_size_posture"),
                request.get("prior_artifact_preservation_posture"),
            ),
            "CONTAINMENT_INVALIDATES_PRIOR_ARTIFACTS_BY_SIZE",
        ),
        _check(
            "containment scope supported",
            _present(scope["selected_containment_scope_values"]) and scope["all_selected_scope_values_supported"],
            "containment scope values must be declared and supported",
            scope["selected_containment_scope_values"],
            "UNSUPPORTED_CONTAINMENT_SCOPE",
        ),
        _check(
            "containment is not cleanup",
            not _contains_truthy_key(request, "artifact_cleanup_authorized"),
            "containment must not authorize cleanup",
            request.get("artifact_cleanup_authorized"),
            "CONTAINMENT_OVERREAD_AS_CLEANUP",
        ),
        _check(
            "containment is not migration",
            not _contains_truthy_key(request, "artifact_migration_authorized"),
            "containment must not authorize migration",
            request.get("artifact_migration_authorized"),
            "CONTAINMENT_OVERREAD_AS_MIGRATION",
        ),
        _check(
            "containment is not command",
            not _contains_truthy_key(request, "command_implemented")
            and not _contains_truthy_key(request, "command_authorized_to_run"),
            "containment must not be command implementation or execution",
            {
                "command_implemented": _contains_truthy_key(request, "command_implemented"),
                "command_authorized_to_run": _contains_truthy_key(request, "command_authorized_to_run"),
            },
            "CONTAINMENT_AUTHORIZES_COMMAND_IMPLEMENTATION",
        ),
        _check(
            "containment is not manifest/checksum/signature/packet implementation",
            not any(
                _contains_truthy_key(request, field)
                for field in ("manifest_implemented", "checksum_implemented", "signature_implemented", "packet_implemented")
            ),
            "containment must not implement manifest/checksum/signature/packet",
            {
                field: _contains_truthy_key(request, field)
                for field in ("manifest_implemented", "checksum_implemented", "signature_implemented", "packet_implemented")
            },
            "CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION",
        ),
        _check(
            "containment does not create currentness",
            not _contains_truthy_key(request, "containment_created_currentness"),
            "containment must not create currentness",
            request.get("containment_created_currentness"),
            "CONTAINMENT_CREATES_CURRENTNESS",
        ),
        _check(
            "containment does not authorize next work",
            not _contains_truthy_key(request, "follow_on_work_authorized"),
            "containment must not authorize next work",
            request.get("follow_on_work_authorized"),
            "CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK",
        ),
        _check(
            "reference record not source",
            not _contains_truthy_key(request, "reference_record_became_source"),
            "reference record must not become source",
            request.get("reference_record_became_source"),
            "REFERENCE_RECORD_TREATED_AS_SOURCE",
        ),
        _check(
            "summary not source",
            not _contains_truthy_key(request, "summary_became_source"),
            "summary must not become source",
            request.get("summary_became_source"),
            "SUMMARY_TREATED_AS_SOURCE",
        ),
        _check(
            "path not currentness",
            not _contains_truthy_key(request, "path_created_currentness"),
            "path must not create currentness",
            request.get("path_created_currentness"),
            "PATH_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "artifact existence not currentness",
            not _contains_truthy_key(request, "artifact_existence_created_currentness"),
            "artifact existence must not create currentness",
            request.get("artifact_existence_created_currentness"),
            "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "no command implementation/execution/authorization",
            not any(
                _contains_truthy_key(request, field)
                for field in ("command_implemented", "command_executed", "command_authorized_to_run")
            ),
            "containment must not implement, execute, or authorize command",
            {
                field: _contains_truthy_key(request, field)
                for field in ("command_implemented", "command_executed", "command_authorized_to_run")
            },
            "CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION",
        ),
        _check(
            "no manifest/checksum/signature/packet implementation",
            not any(
                _contains_truthy_key(request, field)
                for field in ("manifest_implemented", "checksum_implemented", "signature_implemented", "packet_implemented")
            ),
            "containment must not implement manifest/checksum/signature/packet",
            {
                field: _contains_truthy_key(request, field)
                for field in ("manifest_implemented", "checksum_implemented", "signature_implemented", "packet_implemented")
            },
            "CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION",
        ),
        _check(
            "no deployment/runtime/public release",
            not any(
                _contains_truthy_key(request, field)
                for field in ("deployment_created", "runtime_hosting_created", "public_release_created")
            ),
            "containment must not create deployment/runtime/public release",
            {
                field: _contains_truthy_key(request, field)
                for field in ("deployment_created", "runtime_hosting_created", "public_release_created")
            },
            "CONTAINMENT_CREATES_DEPLOYMENT",
        ),
        _check(
            "no source transfer/migration/receipt/reception authorization",
            not any(
                _contains_truthy_key(request, field)
                for field in ("source_transferred", "source_migrated", "source_received", "source_receipt_recorded", "reception_authorized")
            ),
            "containment must not transfer, migrate, receive, receipt, or authorize reception",
            {
                field: _contains_truthy_key(request, field)
                for field in (
                    "source_transferred",
                    "source_migrated",
                    "source_received",
                    "source_receipt_recorded",
                    "reception_authorized",
                )
            },
            "CONTAINMENT_AUTHORIZES_TRANSFER",
        ),
        _check(
            "no final completion/continuation/reusable permission/follow-on work",
            not any(
                _contains_truthy_key(request, field)
                for field in (
                    "final_completion_claimed",
                    "continuation_authorized",
                    "reusable_permission_created",
                    "follow_on_work_authorized",
                )
            ),
            "containment must not complete, continue, create reusable permission, or authorize follow-on work",
            {
                field: _contains_truthy_key(request, field)
                for field in (
                    "final_completion_claimed",
                    "continuation_authorized",
                    "reusable_permission_created",
                    "follow_on_work_authorized",
                )
            },
            "CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK",
        ),
        _check(
            "no mutation/replay/merge",
            not any(_contains_truthy_key(request, field) for field in MUTATION_FLAGS),
            "containment review must not mutate, replay, or merge",
            {field: _contains_truthy_key(request, field) for field in MUTATION_FLAGS},
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non-claims remain false",
            non_claims_ok,
            "required non-claims must be explicit and false",
            non_claim_issue or "all required non-claims false",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]

    if collapse:
        checks.append(
            _check(
                "collapse posture absent",
                False,
                "containment request must not carry cleanup, mutation, source, currentness, command, deployment, continuation, or follow-on collapse flags",
                collapse,
                collapse,
            )
        )

    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if not check.get("passed"):
            return str(check.get("block_code") or check.get("failure_code") or "CONTAINMENT_REVIEW_BLOCKED")
    return None


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    context = _normalize_basis(request.get("additional_basis_context"), "additional_basis_context_reference")
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": context if required else {},
        "representative_missing_basis": [
            "artifact-emission pressure basis unclear",
            "affected artifact family unclear",
            "future emission family unclear",
            "reference-only selected-basis posture unclear",
            "summary-plus-reference posture unclear",
            "prohibited embedding posture unclear",
            "prior artifact preservation posture unclear",
            "no-mutation posture unclear",
            "size-pressure relation to standing artifacts unclear",
            "non-claims incomplete but not flipped",
        ]
        if required
        else [],
        "missing_basis_scheduled": False,
        "missing_basis_authorized": False,
        "missing_basis_executed": False,
    }


def _not_recorded_basis(
    outcome: str,
    request: Mapping[str, Any],
    failed_checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    basis = _normalize_basis(request.get("not_recorded_basis"), "not_recorded_basis_reference")
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": basis if not_recorded else {},
        "failed_containment_reasons": [
            "containment basis cannot be bounded",
            "containment overread as cleanup",
            "containment overread as artifact invalidation",
            "containment requires artifact mutation",
            "containment requires artifact deletion",
            "containment requires artifact compaction",
            "containment requires artifact migration",
            "containment cannot separate reference records from source/currentness",
            "containment would authorize next live artifact without containing recursive embedding",
        ]
        if not_recorded
        else [],
        "failed_checks": _deepcopy(list(failed_checks)) if not_recorded else [],
        "not_recorded_mutates_prior_artifacts": False,
        "not_recorded_repairs_prior_artifacts": False,
        "not_recorded_authorizes_cleanup": False,
        "not_recorded_deletes_prior_artifacts": False,
        "not_recorded_compacts_prior_artifacts": False,
        "not_recorded_rewrites_prior_artifacts": False,
        "not_recorded_migrates_prior_artifacts": False,
        "not_recorded_implements_command": False,
        "not_recorded_executes_command": False,
        "not_recorded_authorizes_follow_on_work": False,
    }


def _containment_statement(outcome: str) -> dict[str, Any]:
    statement = {
        "artifact_emission_containment_recorded": outcome == OUTCOME_RECORDED,
        "reference_only_selected_basis_required": outcome == OUTCOME_RECORDED,
        "recursive_full_artifact_embedding_blocked": outcome == OUTCOME_RECORDED,
        "summary_plus_reference_emission_required": outcome == OUTCOME_RECORDED,
        "prior_artifacts_preserved_by_reference": outcome == OUTCOME_RECORDED,
        "artifact_emission_containment_only": outcome == OUTCOME_RECORDED,
        "future_artifacts_should_use_reference_records": outcome == OUTCOME_RECORDED,
        "future_artifacts_should_not_embed_full_prior_artifacts": outcome == OUTCOME_RECORDED,
        "heavy_artifacts_remain_visible_evidence": outcome == OUTCOME_RECORDED,
        "artifact_size_pressure_is_not_law_failure_by_itself": outcome == OUTCOME_RECORDED,
        "carrier_shape_pressure_recorded": outcome == OUTCOME_RECORDED,
    }
    statement.update(_false_posture_for_outcome(outcome))
    return statement


def _metadata(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    result_id_basis = request.get("containment_request_id") or "artifact_emission_containment"
    return {
        "artifact_emission_containment_result_id": f"{_safe_component(result_id_basis)}__artifact_emission_containment_result",
        "artifact_emission_containment_result_type": "artifact_emission_containment_boundary_result",
        "artifact_emission_containment_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "resolver_module": RESOLVER_MODULE,
        "outcome_recorded_in_metadata": outcome,
    }


def _declared_containment_question(
    request: Mapping[str, Any],
    request_path: str | None,
) -> dict[str, Any]:
    return {
        "containment_request_id": request.get("containment_request_id"),
        "containment_question": request.get("containment_question"),
        "containment_intent": request.get("containment_intent"),
        "declared_containment_request_path": request_path,
        "containment_is_not_cleanup": True,
        "containment_is_not_artifact_deletion": True,
        "containment_is_not_artifact_compaction": True,
        "containment_is_not_artifact_rewriting": True,
        "containment_is_not_artifact_invalidation": True,
        "containment_is_not_command_implementation": True,
        "containment_is_not_command_execution": True,
        "containment_is_not_manifest_checksum_signature_packet_implementation": True,
        "containment_does_not_authorize_next_work": True,
    }


def _result_from_request(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    malformed_code: str | None = None,
) -> dict[str, Any]:
    request_copy = _deepcopy(dict(request))
    checks = _build_checks(request_copy, malformed_code)
    failed_checks = [check for check in checks if not check.get("passed")]
    failed_code = _first_failed_code(checks)

    requested_outcome = request_copy.get("requested_containment_outcome", OUTCOME_RECORDED)
    intent = request_copy.get("containment_intent")

    if malformed_code:
        outcome = OUTCOME_BLOCKED
        block_code = malformed_code
    elif intent == INTENT_BLOCK:
        outcome = OUTCOME_BLOCKED
        block_code = request_copy.get("block_reason") or "CONTAINMENT_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    elif failed_code:
        outcome = OUTCOME_BLOCKED
        block_code = failed_code
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        block_code = None
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = str(requested_outcome)
        block_code = None if requested_outcome != OUTCOME_BLOCKED else request_copy.get("block_reason") or OUTCOME_BLOCKED
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "CONTAINMENT_INTENT_UNSUPPORTED"

    if outcome == OUTCOME_RECORDED and failed_checks:
        outcome = OUTCOME_BLOCKED
        block_code = failed_code or "CONTAINMENT_REVIEW_BLOCKED"

    if outcome == OUTCOME_NOT_RECORDED and not _present(request_copy.get("not_recorded_basis")):
        request_copy["not_recorded_basis"] = {
            "not_recorded_reason": "readable containment basis was not recorded"
        }

    if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS and not _present(request_copy.get("additional_basis_context")):
        request_copy["additional_basis_context"] = {
            "additional_basis_reason": "non-collapse-shaped containment review needs more basis"
        }

    summary_placeholder: dict[str, Any] = {}
    result = {
        "artifact_emission_containment_metadata": _metadata(request_copy, outcome),
        "declared_containment_question": _declared_containment_question(request_copy, request_path),
        "selected_artifact_emission_pressure_basis": _selected_artifact_emission_pressure_basis(request_copy),
        "affected_artifact_families": _affected_artifact_families(request_copy),
        "future_emission_family": _future_emission_family(request_copy),
        "containment_basis": _containment_basis(request_copy),
        "reference_only_selected_basis_posture": _reference_only_selected_basis_posture(request_copy),
        "summary_plus_reference_posture": _summary_plus_reference_posture(request_copy),
        "recursive_embedding_block": _recursive_embedding_block(request_copy),
        "prior_artifact_preservation_posture": _prior_artifact_preservation_posture(request_copy),
        "containment_scope": _containment_scope(request_copy),
        "containment_checks": checks,
        "containment_statement": _containment_statement(outcome),
        "containment_non_meaning": _containment_non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request_copy),
        "not_recorded_basis": _not_recorded_basis(outcome, request_copy, failed_checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _false_posture_for_outcome(outcome),
        "outcome": outcome,
        "block": _block(block_code, request_copy.get("block_reason") if block_code else None),
        "artifact_emission_containment_summary": summary_placeholder,
    }
    result["artifact_emission_containment_summary"] = build_artifact_emission_containment_summary(result)
    return result


def resolve_artifact_emission_containment_boundary(
    declared_containment_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared artifact emission containment request."""

    if declared_containment_request is None:
        return _result_from_request({}, malformed_code=None)
    if not isinstance(declared_containment_request, Mapping):
        return _result_from_request({}, malformed_code="DECLARED_CONTAINMENT_REQUEST_MALFORMED")
    return _result_from_request(declared_containment_request)


def resolve_artifact_emission_containment_boundary_from_path(
    declared_containment_request_path: Path | str,
) -> dict:
    """Resolve one containment request from a JSON object file."""

    data, error = _read_json_object(declared_containment_request_path)
    if error:
        return _result_from_request(
            {},
            request_path=str(Path(declared_containment_request_path)),
            malformed_code=error,
        )
    assert data is not None
    return _result_from_request(data, request_path=str(Path(declared_containment_request_path)))


def build_artifact_emission_containment_summary(result: Mapping[str, Any]) -> dict:
    """Build a bounded summary for an artifact emission containment result."""

    checks = result.get("containment_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes, bytearray)):
        checks = []
    passed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed"))
    failed_check_count = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))

    statement = result.get("containment_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    question = result.get("declared_containment_question", {})
    if not isinstance(question, Mapping):
        question = {}
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}
    scope = result.get("containment_scope", {})
    if not isinstance(scope, Mapping):
        scope = {}
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code"),
        "block_reason": block.get("reason"),
        "containment_request_id": question.get("containment_request_id"),
        "containment_question": question.get("containment_question"),
        "containment_intent": question.get("containment_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "artifact_emission_containment_recorded": bool(statement.get("artifact_emission_containment_recorded")),
        "reference_only_selected_basis_required": bool(statement.get("reference_only_selected_basis_required")),
        "recursive_full_artifact_embedding_blocked": bool(statement.get("recursive_full_artifact_embedding_blocked")),
        "summary_plus_reference_emission_required": bool(statement.get("summary_plus_reference_emission_required")),
        "prior_artifacts_preserved_by_reference": bool(statement.get("prior_artifacts_preserved_by_reference")),
        "not_recorded": result.get("outcome") == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": result.get("outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "affected_artifact_families": result.get("affected_artifact_families", {}).get("affected_artifact_families")
        if isinstance(result.get("affected_artifact_families"), Mapping)
        else None,
        "future_emission_family": result.get("future_emission_family", {}).get("future_emission_family")
        if isinstance(result.get("future_emission_family"), Mapping)
        else None,
        "containment_basis_declared": bool(result.get("containment_basis", {}).get("containment_basis"))
        if isinstance(result.get("containment_basis"), Mapping)
        else False,
        "reference_only_posture_declared": bool(
            result.get("reference_only_selected_basis_posture", {}).get("reference_only_selected_basis_posture")
        )
        if isinstance(result.get("reference_only_selected_basis_posture"), Mapping)
        else False,
        "summary_plus_reference_posture_declared": bool(
            result.get("summary_plus_reference_posture", {}).get("summary_plus_reference_posture")
        )
        if isinstance(result.get("summary_plus_reference_posture"), Mapping)
        else False,
        "recursive_embedding_blocked": bool(
            result.get("recursive_embedding_block", {}).get("recursive_full_artifact_embedding_blocked")
        )
        if isinstance(result.get("recursive_embedding_block"), Mapping)
        else False,
        "prior_artifacts_not_mutated": not bool(non_claims.get("prior_artifacts_mutated")),
        "prior_artifacts_not_deleted": not bool(non_claims.get("prior_artifacts_deleted")),
        "prior_artifacts_not_compacted": not bool(non_claims.get("prior_artifacts_compacted")),
        "prior_artifacts_not_rewritten": not bool(non_claims.get("prior_artifacts_rewritten")),
        "prior_artifacts_not_invalidated_by_size": not bool(non_claims.get("prior_artifacts_invalidated_by_size")),
        "artifact_size_pressure_not_law_failure_by_itself": bool(
            statement.get("artifact_size_pressure_is_not_law_failure_by_itself")
        ),
        "heavy_artifacts_remain_visible_evidence": bool(statement.get("heavy_artifacts_remain_visible_evidence")),
        "no_cleanup_compaction_deletion_rewrite_migration_authorized": not any(
            bool(non_claims.get(field))
            for field in (
                "artifact_cleanup_authorized",
                "prior_artifacts_compacted",
                "prior_artifacts_deleted",
                "prior_artifacts_rewritten",
                "artifact_migration_authorized",
            )
        ),
        "no_command_manifest_checksum_signature_packet_implemented": not any(
            bool(non_claims.get(field))
            for field in (
                "command_implemented",
                "manifest_implemented",
                "checksum_implemented",
                "signature_implemented",
                "packet_implemented",
            )
        ),
        "no_deployment_runtime_public_release": not any(
            bool(non_claims.get(field))
            for field in ("deployment_created", "runtime_hosting_created", "public_release_created")
        ),
        "no_source_transferred_migrated_received_receipted": not any(
            bool(non_claims.get(field))
            for field in ("source_transferred", "source_migrated", "source_received", "source_receipt_recorded")
        ),
        "no_operation_permission_public_readiness_final_completion": not any(
            bool(non_claims.get(field))
            for field in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        ),
        "no_continuation_publication_flow_reusable_permission": not any(
            bool(non_claims.get(field))
            for field in ("continuation_authorized", "publication_flow_opened", "reusable_permission_created")
        ),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": not any(
            bool(non_claims.get(field))
            for field in (
                "derivative_reception_authorized",
                "vessel_relation_authorized",
                "another_reception_request_authorized",
                "follow_on_work_authorized",
            )
        ),
        "containment_scope_values": scope.get("selected_containment_scope_values", []),
        "key_non_claims": {field: bool(non_claims.get(field)) for field in REQUIRED_FALSE_NON_CLAIMS},
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    question = result.get("declared_containment_question", {})
    request_id = None
    if isinstance(question, Mapping):
        request_id = question.get("containment_request_id")
    filename = f"{_safe_component(request_id)}__artifact_emission_containment_result.json"
    return ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_ROOT / filename


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_artifact_emission_containment_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a containment result as additive JSON without overwriting."""

    if not isinstance(result, Mapping):
        raise ArtifactEmissionContainmentBoundaryError("result must be a mapping")
    path = Path(output_path) if output_path is not None else _default_output_path(result)
    path = _non_overwriting_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def build_declared_artifact_emission_containment_request(
    containment_request_id: str,
    containment_question: str,
    selected_artifact_emission_pressure_basis: Mapping[str, Any] | str,
    affected_artifact_families: Mapping[str, Any] | Sequence[str] | str,
    future_emission_family: Mapping[str, Any] | str,
    containment_basis: Mapping[str, Any] | str,
    reference_only_selected_basis_posture: Mapping[str, Any] | str,
    summary_plus_reference_posture: Mapping[str, Any] | str,
    recursive_embedding_block: Mapping[str, Any] | str,
    prior_artifact_preservation_posture: Mapping[str, Any] | str,
    containment_scope: Sequence[str] | Mapping[str, Any],
    containment_intent: str = INTENT_RECORD,
    *,
    requested_containment_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded containment request with required non-claims false."""

    request = {
        "containment_request_id": containment_request_id,
        "containment_question": containment_question,
        "containment_intent": containment_intent,
        "selected_artifact_emission_pressure_basis": _normalize_basis(
            selected_artifact_emission_pressure_basis,
            "selected_artifact_emission_pressure_basis_reference",
        ),
        "affected_artifact_families": _normalize_basis(
            affected_artifact_families,
            "affected_artifact_families_reference",
        ),
        "future_emission_family": _normalize_basis(
            future_emission_family,
            "future_emission_family_reference",
        ),
        "containment_basis": _normalize_basis(containment_basis, "containment_basis_reference"),
        "reference_only_selected_basis_posture": _normalize_basis(
            reference_only_selected_basis_posture,
            "reference_only_selected_basis_posture_reference",
        ),
        "summary_plus_reference_posture": _normalize_basis(
            summary_plus_reference_posture,
            "summary_plus_reference_posture_reference",
        ),
        "recursive_embedding_block": _normalize_basis(
            recursive_embedding_block,
            "recursive_embedding_block_reference",
        ),
        "prior_artifact_preservation_posture": _normalize_basis(
            prior_artifact_preservation_posture,
            "prior_artifact_preservation_posture_reference",
        ),
        "no_prior_artifact_mutation_posture": {
            "no_prior_artifact_mutation_posture_declared": True,
            "prior_artifacts_not_mutated": True,
            "prior_artifacts_not_deleted": True,
            "prior_artifacts_not_compacted": True,
            "prior_artifacts_not_rewritten": True,
        },
        "no_artifact_invalidation_by_size_posture": {
            "no_artifact_invalidation_by_size_posture_declared": True,
            "prior_artifacts_not_invalidated_by_size": True,
            "artifact_size_pressure_is_not_law_failure_by_itself": True,
        },
        "containment_scope": _deepcopy(containment_scope),
        "reference_record_shape": list(ALLOWED_REFERENCE_FIELDS),
        "selected_prior_result_reference_shape": {
            "allowed_reference_fields": list(ALLOWED_REFERENCE_FIELDS),
            "reference_record_became_source": False,
            "path_created_currentness": False,
        },
        "requested_containment_outcome": requested_containment_outcome,
        "additional_basis_context": _deepcopy(additional_basis_context) if additional_basis_context else {},
        "not_recorded_basis": _normalize_basis(not_recorded_basis, "not_recorded_basis_reference")
        if not_recorded_basis is not None
        else {},
        "declared_non_claims": {field: False for field in REQUIRED_FALSE_NON_CLAIMS},
    }
    return request
