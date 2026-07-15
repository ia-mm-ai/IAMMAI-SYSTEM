"""Resolve the portable source-body verification command implementation boundary.

This resolver answers one question only:

    Can conditions for a future checker-only portable source-body verification
    command implementation be bounded without implementing, executing,
    invoking, or authorizing the command?

The resolver records implementation-boundary conditions only. It is not command
implementation, command execution, command invocation, command output, command
result, command success, manifest implementation, checksum implementation,
signature implementation, packet implementation, deployment, runtime hosting,
public release, source transfer, source migration, source receipt, reception
authorization, authority, currentness, operation permission, public readiness,
final completion, continuation, reusable permission, derivative reception,
vessel relation, another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationCommandImplementationBoundaryError(Exception):
    """Raised for hard command implementation-boundary failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_command_implementation_boundary"
)
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_implementation_boundary"
)

OUTCOME_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = (
    "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY"
)
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY"
)
INTENT_BLOCK = (
    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_REVIEW"
)
SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE = {
    "COMMAND_IMPLEMENTATION_BOUNDARY_ONLY",
    "COMMAND_IMPLEMENTATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_AUTHORIZED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "CHECKER_ONLY_IMPLEMENTATION_CONDITIONS_DECLARED",
    "COMMAND_REQUIRES_DECLARED_EVIDENCE_MANIFEST",
    "COMMAND_REQUIRES_CONTAINED_REFERENCE_SHAPE",
    "COMMAND_OUTPUT_IS_NOT_SOURCE",
    "COMMAND_SUCCESS_IS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_IS_NOT_FINAL_COMPLETION",
    "COMMAND_IS_NOT_AUTHORITY",
    "COMMAND_IS_NOT_DEPLOYMENT",
    "COMMAND_IS_NOT_RUNTIME_HOSTING",
    "COMMAND_IS_NOT_PUBLIC_RELEASE",
    "COMMAND_EXECUTION_REQUIRES_SEPARATE_BOUNDARY",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "command_implementation_boundary_recorded_as_implementation",
    "command_implemented",
    "command_executed",
    "command_authorized_to_run",
    "command_invocation_created",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "command_output_became_source",
    "command_output_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "full_prior_artifacts_embedded",
    "prior_artifacts_mutated",
    "manifest_implemented",
    "checksum_implemented",
    "signature_implemented",
    "packet_implemented",
    "deployment_created",
    "runtime_hosting_created",
    "public_release_created",
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

OUTPUT_FALSE_POSTURE = tuple(
    dict.fromkeys(
        REQUIRED_FALSE_NON_CLAIMS
        + (
            "command_exists",
            "command_can_run",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "command_output_created_source",
            "command_output_created_authority",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "source_receipt_created",
            "reception_authorized",
            "authority_created",
            "currentness_created",
            "public_readiness_created",
            "path_created_currentness",
            "latest_file_created_currentness",
            "artifact_existence_created_currentness",
            "repository_copy_became_body",
            "carrier_possession_created_currentness",
            "narration_created_currentness",
            "next_work_authorized",
        )
    )
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "portable_source_body_verification_command_implementation_boundary_recorded",
    "checker_command_implementation_conditions_declared",
    "command_implementation_must_be_checker_only",
    "command_implementation_requires_contained_reference_shape",
    "command_execution_requires_separate_boundary",
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = (
    ("command_implementation_boundary_recorded_as_implementation", "COMMAND_IMPLEMENTATION_CREATED"),
    ("command_implemented", "COMMAND_IMPLEMENTATION_CREATED"),
    ("command_implementation_created", "COMMAND_IMPLEMENTATION_CREATED"),
    ("command_created", "COMMAND_IMPLEMENTATION_CREATED"),
    ("command_exists", "COMMAND_IMPLEMENTATION_CREATED"),
    ("command_executed", "COMMAND_EXECUTION_AUTHORIZED"),
    ("command_execution_authorized", "COMMAND_EXECUTION_AUTHORIZED"),
    ("command_authorized_to_run", "COMMAND_EXECUTION_AUTHORIZED"),
    ("command_authorized", "COMMAND_EXECUTION_AUTHORIZED"),
    ("command_can_run", "COMMAND_EXECUTION_AUTHORIZED"),
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invocation_exists", "COMMAND_INVOCATION_CREATED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_output_exists", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_result_exists", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("command_success_exists", "COMMAND_SUCCESS_CREATED"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_became_authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
    ("command_output_treated_as_authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
    ("command_result_became_authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("final_completion_claimed", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_became_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("command_treated_as_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"),
    ("full_prior_artifact_embedding_permitted", "FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"),
    ("recursive_full_artifact_embedding_permitted", "FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"),
    ("raw_full_artifact_body_embedded", "FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifact_mutation_performed", "ARTIFACTS_MUTATED"),
    ("manifest_implemented", "MANIFEST_IMPLEMENTATION_CREATED"),
    ("checksum_implemented", "CHECKSUM_IMPLEMENTATION_CREATED"),
    ("signature_implemented", "SIGNATURE_IMPLEMENTATION_CREATED"),
    ("packet_implemented", "PACKET_IMPLEMENTATION_CREATED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("source_transferred", "SOURCE_TRANSFER_CREATED"),
    ("source_migrated", "SOURCE_MIGRATION_CREATED"),
    ("source_received", "SOURCE_RECEIPT_CREATED"),
    ("source_receipt_recorded", "SOURCE_RECEIPT_CREATED"),
    ("source_receipt_created", "SOURCE_RECEIPT_CREATED"),
    ("reception_authorized", "RECEPTION_AUTHORIZED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("publication_flow_opened", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("successor_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("next_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("path_treated_as_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_created_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    ("latest_file_treated_as_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    ("artifact_existence_created_currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
    ("artifact_existence_treated_as_currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
    ("repository_copy_became_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    ("repository_copy_treated_as_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    ("carrier_possession_created_currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("carrier_possession_treated_as_currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("narration_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    ("narration_treated_as_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
)

REFERENCE_SHAPE_KEYS = (
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
    "id",
    "result_id",
    "outcome",
    "failed_check_count",
    "passed_check_count",
    "summary",
    "non_claims",
    "basis_reference",
    "reference",
    "path",
)

FULL_BODY_KEYS = {
    "full_artifact_body",
    "raw_full_artifact_body",
    "artifact_body",
    "raw_artifact_body",
    "embedded_artifact",
    "embedded_artifacts",
    "upstream_artifact_body",
    "full_result",
    "raw_result",
    "raw_selected_basis",
    "raw_selected_command_boundary_basis",
    "raw_selected_artifact_emission_containment_basis",
    "raw_selected_evidence_manifest_basis",
    "raw_selected_portable_verification_basis",
}


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {
            "true",
            "yes",
            "1",
            "implemented",
            "created",
            "executed",
            "authorized",
            "source",
            "authority",
            "current",
            "deployed",
            "released",
            "success",
        }
    return bool(value)


def _is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return value is False
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0"}
    return value == 0


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _value_at(mapping: Any, path: Sequence[str]) -> Any:
    current = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _safe_component(value: Any) -> str:
    text = str(value or "portable_source_body_verification_command_implementation_boundary").strip()
    cleaned = "".join(
        character if character.isalnum() or character in {"-", "_"} else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "portable_source_body_verification_command_implementation_boundary"


def _generated_at() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    request_path = Path(path)
    try:
        payload = json.loads(request_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, UnicodeDecodeError):
        return None, "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_UNREADABLE"
    except json.JSONDecodeError:
        return None, "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED"
    if not isinstance(payload, Mapping):
        return None, "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED"
    return copy.deepcopy(dict(payload)), None


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


def _sanitize_reference_shape(value: Any, depth: int = 0) -> Any:
    if depth > 8:
        return {"reference_shape_depth_limit_reached": True}
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        omitted: list[str] = []
        for key, nested_value in value.items():
            key_text = str(key)
            lowered = key_text.lower()
            raw_artifact_key = (
                key_text in FULL_BODY_KEYS
                or (
                    lowered.startswith("raw_")
                    and any(part in lowered for part in ("artifact", "result", "body"))
                )
                or (
                    "full" in lowered
                    and any(part in lowered for part in ("artifact", "result", "body"))
                )
            )
            if raw_artifact_key:
                omitted.append(key_text)
                continue
            result[key_text] = _sanitize_reference_shape(nested_value, depth + 1)
        if omitted:
            result["omitted_full_artifact_body_keys"] = omitted
            result["full_artifact_body_not_embedded"] = True
        return result
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_sanitize_reference_shape(item, depth + 1) for item in value]
    if isinstance(value, str) and len(value.encode("utf-8")) > 8192:
        return {
            "large_string_omitted_from_reference_shape": True,
            "byte_length": len(value.encode("utf-8")),
        }
    return copy.deepcopy(value)


def _normalize_reference_basis(value: Any, reference_key: str) -> Any:
    if isinstance(value, Mapping):
        return _sanitize_reference_shape(dict(value))
    if isinstance(value, str) and value.strip():
        return {
            reference_key: value,
            "basis_reference": value,
            "basis_is_reference_only": True,
        }
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return _sanitize_reference_shape(list(value))
    return _sanitize_reference_shape(value)


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = _first_present(
            scope.get("selected_scope_values"),
            scope.get("implementation_boundary_scope_values"),
            scope.get("command_implementation_boundary_scope_values"),
            scope.get("scope_values"),
            scope.get("values"),
        )
        if values is None:
            values = [
                key for key, value in scope.items() if isinstance(key, str) and _truthy(value)
            ]
        if isinstance(values, str):
            return [values]
        if isinstance(values, Sequence) and not isinstance(values, (bytes, bytearray)):
            return [str(value) for value in values]
        return []
    if isinstance(scope, Sequence) and not isinstance(scope, (str, bytes, bytearray)):
        return [str(value) for value in scope]
    return []


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
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
        "block_code": code,
        "block_reason": reason if code is not None else None,
        "code": code,
        "reason": reason if code is not None else None,
    }


def _basis_id(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("selected_result_id"),
            basis.get("result_id"),
            basis.get("id"),
            basis.get("portable_source_body_verification_command_boundary_result_id"),
            basis.get("artifact_emission_containment_result_id"),
            basis.get("portable_source_body_verification_evidence_manifest_result_id"),
            basis.get("portable_source_body_verification_result_id"),
            basis.get("basis_id"),
            basis.get("reference"),
            basis.get("basis_reference"),
        ]
    )
    return _first_present(*candidates)


def _basis_outcome(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("selected_result_outcome"),
            basis.get("outcome"),
            _value_at(basis, ("portable_source_body_verification_command_boundary_summary", "outcome")),
            _value_at(basis, ("artifact_emission_containment_summary", "outcome")),
            _value_at(basis, ("portable_source_body_verification_evidence_manifest_summary", "outcome")),
            _value_at(basis, ("portable_source_body_verification_summary", "outcome")),
        ]
    )
    return _first_present(*candidates)


def _basis_reference(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("selected_result_basis_reference"),
            basis.get("basis_reference"),
            basis.get("reference"),
            basis.get("selected_result_path"),
            basis.get("path"),
        ]
    )
    return _first_present(*candidates)


def _required_non_claims_false(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or not _is_false(declared[key]):
            return False
    return True


def _collapse_code(request: Mapping[str, Any]) -> str | None:
    for flag in MUTATION_FLAGS:
        if _contains_truthy_key(request, flag):
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    for key, code in COLLAPSE_FIELD_CODES:
        if _contains_truthy_key(request, key):
            return code
    return None


def _build_non_claims(outcome: str) -> dict[str, Any]:
    non_claims = {key: False for key in OUTPUT_FALSE_POSTURE}
    for key in ALLOWED_RECORDED_TRUE_FIELDS:
        non_claims[key] = outcome == OUTCOME_RECORDED
    non_claims.update(
        {
            "even_when_implementation_boundary_recorded_no_command_is_implemented": True,
            "even_when_implementation_boundary_recorded_no_command_is_authorized_to_run": True,
            "even_when_implementation_boundary_recorded_no_command_invocation_exists": True,
            "even_when_implementation_boundary_recorded_no_command_output_exists": True,
            "even_when_implementation_boundary_recorded_no_command_success_exists": True,
            "even_when_implementation_boundary_recorded_execution_remains_separate_future_work": True,
            "even_when_implementation_boundary_recorded_no_manifest_checksum_signature_packet_runtime_deployment_public_release_transfer_migration_receipt_reception_authority_currentness_permission_readiness_completion_continuation_reusable_permission_derivative_vessel_successor_or_follow_on_work_is_created_or_authorized": True,
        }
    )
    return non_claims


def _implementation_boundary_non_meaning() -> dict[str, bool]:
    names = (
        "command_exists",
        "command_implemented",
        "command_can_run",
        "command_invocation_exists",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "command_success_creates_currentness",
        "command_success_creates_final_completion",
        "command_output_becomes_source",
        "command_output_becomes_authority",
        "deployment_created",
        "runtime_hosting_created",
        "public_release_created",
        "operation_permission_created",
        "public_readiness_created",
        "continuation_authorized",
        "reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_reception_request_authorized",
        "follow_on_work_authorized",
    )
    return {f"implementation_boundary_does_not_mean_{name}": True for name in names}


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command implementation boundary test",
            "command implementation boundary live artifact",
            "actual command implementation",
            "command execution boundary",
            "command invocation",
            "command output",
            "command success",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
            "source transfer",
            "source migration",
            "source receipt",
            "reception authorization",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
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


def _selected_basis_section(
    request: Mapping[str, Any],
    *,
    value_key: str,
    result_path_key: str,
    result_id_key: str,
    result_outcome_key: str,
    terminal_summary_path_key: str | None,
    reference_key: str,
    section_prefix: str,
) -> dict[str, Any]:
    basis = _normalize_reference_basis(request.get(value_key), reference_key)
    basis_mapping = basis if isinstance(basis, Mapping) else None
    result_path = _first_present(
        request.get(result_path_key),
        _value_at(basis_mapping, ("selected_result_path",)),
        _value_at(basis_mapping, ("path",)),
    )
    result_id = _first_present(request.get(result_id_key), _basis_id(basis_mapping))
    result_outcome = _first_present(
        request.get(result_outcome_key),
        _basis_outcome(basis_mapping),
    )
    terminal_path = request.get(terminal_summary_path_key) if terminal_summary_path_key else None
    present_by_reference = any(
        _present(value) for value in (basis, result_path, result_id, result_outcome, terminal_path)
    )
    return {
        f"{section_prefix}_result_id": result_id,
        f"{section_prefix}_result_outcome": result_outcome,
        f"{section_prefix}_result_path": result_path,
        f"{section_prefix}_terminal_summary_path": terminal_path,
        f"{section_prefix}_basis_reference": _basis_reference(basis_mapping),
        f"{section_prefix}_basis_declared": present_by_reference,
        f"{section_prefix}_basis_is_reference_shaped": True,
        f"{section_prefix}_full_artifact_body_not_embedded": True,
        f"{section_prefix}_basis_as_reference_shape": basis,
    }


def _selected_command_boundary_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _selected_basis_section(
        request,
        value_key="selected_command_boundary_basis",
        result_path_key="selected_command_boundary_result_path",
        result_id_key="selected_command_boundary_result_id",
        result_outcome_key="selected_command_boundary_result_outcome",
        terminal_summary_path_key="selected_command_boundary_terminal_summary_path",
        reference_key="selected_command_boundary_basis_reference",
        section_prefix="selected_command_boundary",
    )
    section.update(
        {
            "command_boundary_recorded_posture": _sanitize_reference_shape(
                request.get("command_boundary_recorded_posture")
            ),
            "command_boundary_remains_checker_only_posture": True,
            "command_boundary_did_not_authorize_command_implementation": True,
            "command_boundary_did_not_authorize_command_execution": True,
            "command_boundary_did_not_create_command_output_or_success": True,
            "command_boundary_did_not_create_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
            "selected_basis_is_reference_shaped_not_full_artifact_body": True,
        }
    )
    return section


def _selected_artifact_emission_containment_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _selected_basis_section(
        request,
        value_key="selected_artifact_emission_containment_basis",
        result_path_key="selected_artifact_emission_containment_result_path",
        result_id_key="selected_artifact_emission_containment_result_id",
        result_outcome_key="selected_artifact_emission_containment_result_outcome",
        terminal_summary_path_key=None,
        reference_key="selected_artifact_emission_containment_basis_reference",
        section_prefix="selected_artifact_emission_containment",
    )
    section.update(
        {
            "containment_recorded_posture": _sanitize_reference_shape(
                request.get("containment_recorded_posture")
            ),
            "reference_only_selected_basis_required": True,
            "recursive_full_artifact_embedding_blocked": True,
            "summary_plus_reference_emission_required": True,
            "prior_artifacts_preserved_by_reference": True,
            "existing_artifacts_not_mutated": True,
            "existing_artifacts_not_invalidated_by_size": True,
            "contained_artifact_emission_required_for_future_implementation_boundary_artifacts": True,
        }
    )
    return section


def _selected_evidence_manifest_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _selected_basis_section(
        request,
        value_key="selected_evidence_manifest_basis",
        result_path_key="selected_evidence_manifest_result_path",
        result_id_key="selected_evidence_manifest_result_id",
        result_outcome_key="selected_evidence_manifest_result_outcome",
        terminal_summary_path_key=None,
        reference_key="selected_evidence_manifest_basis_reference",
        section_prefix="selected_evidence_manifest",
    )
    section.update(
        {
            "basis_remains_evidence_only": True,
            "basis_does_not_authorize_implementation_execution_output_success": True,
            "basis_does_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
            "reference_shaped_basis_only": True,
        }
    )
    return section


def _selected_portable_verification_basis(request: Mapping[str, Any]) -> dict[str, Any]:
    section = _selected_basis_section(
        request,
        value_key="selected_portable_verification_basis",
        result_path_key="selected_portable_verification_result_path",
        result_id_key="selected_portable_verification_result_id",
        result_outcome_key="selected_portable_verification_result_outcome",
        terminal_summary_path_key=None,
        reference_key="selected_portable_verification_basis_reference",
        section_prefix="selected_portable_verification",
    )
    section.update(
        {
            "basis_remains_verification_only": True,
            "basis_does_not_authorize_implementation_execution_output_success": True,
            "basis_does_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
            "reference_shaped_basis_only": True,
        }
    )
    return section


def _required_evidence_classes(request: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("selected_required_evidence_classes"),
        request.get("selected_evidence_classes"),
        _value_at(request.get("selected_evidence_manifest_basis"), ("declared_evidence_classes",)),
    )


def _required_surfaces(request: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("selected_required_surfaces"),
        _value_at(request.get("selected_evidence_manifest_basis"), ("required_surfaces",)),
    )


def _reference_shape_requirements(request: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("selected_reference_shaped_input_requirements"),
        request.get("reference_shaped_input_requirements"),
        _value_at(
            request.get("selected_artifact_emission_containment_basis"),
            ("reference_only_selected_basis_posture",),
        ),
    )


def _required_postures(request: Mapping[str, Any]) -> dict[str, Any]:
    implementation_limits = request.get("implementation_limits")
    output_limits = request.get("output_limits")
    execution_limits = request.get("execution_limits")
    checker_basis = request.get("checker_only_implementation_basis")
    return {
        "no_command_authority_posture": _first_present(
            request.get("no_command_authority_posture"),
            _value_at(implementation_limits, ("no_command_authority_posture",)),
        ),
        "no_output_source_posture": _first_present(
            request.get("no_output_source_posture"),
            _value_at(output_limits, ("no_output_source_posture",)),
        ),
        "no_success_currentness_posture": _first_present(
            request.get("no_success_currentness_posture"),
            _value_at(output_limits, ("no_success_currentness_posture",)),
        ),
        "no_success_final_completion_posture": _first_present(
            request.get("no_success_final_completion_posture"),
            _value_at(output_limits, ("no_success_final_completion_posture",)),
        ),
        "contained_artifact_emission_posture": _first_present(
            request.get("contained_artifact_emission_posture"),
            _value_at(implementation_limits, ("contained_artifact_emission_posture",)),
            _value_at(checker_basis, ("contained_artifact_emission_posture",)),
        ),
    }


def _determine_block_code(
    request: Mapping[str, Any],
    *,
    selected_command_boundary_basis: Mapping[str, Any],
    selected_artifact_emission_containment_basis: Mapping[str, Any],
    selected_evidence_manifest_basis: Mapping[str, Any],
    selected_portable_verification_basis: Mapping[str, Any],
    required_evidence_classes: Any,
    required_surfaces: Any,
    reference_shape_requirements: Any,
    required_postures: Mapping[str, Any],
    scope_values: Sequence[str],
) -> str | None:
    if not _present(request.get("command_implementation_boundary_question")):
        return "COMMAND_IMPLEMENTATION_BOUNDARY_QUESTION_UNDECLARED"
    intent = request.get("command_implementation_boundary_intent")
    if intent == INTENT_BLOCK:
        return "COMMAND_IMPLEMENTATION_BOUNDARY_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_INTENTS:
        return "COMMAND_IMPLEMENTATION_BOUNDARY_INTENT_UNSUPPORTED"
    if not selected_command_boundary_basis.get("selected_command_boundary_basis_declared"):
        return "COMMAND_BOUNDARY_BASIS_MISSING"
    if not selected_artifact_emission_containment_basis.get(
        "selected_artifact_emission_containment_basis_declared"
    ):
        return "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"
    if not selected_evidence_manifest_basis.get("selected_evidence_manifest_basis_declared"):
        return "EVIDENCE_MANIFEST_BASIS_MISSING"
    if not selected_portable_verification_basis.get(
        "selected_portable_verification_basis_declared"
    ):
        return "PORTABLE_VERIFICATION_BASIS_MISSING"
    if not _present(required_evidence_classes):
        return "REQUIRED_EVIDENCE_CLASSES_MISSING"
    if not _present(required_surfaces):
        return "REQUIRED_SURFACES_MISSING"
    if not _present(reference_shape_requirements):
        return "REFERENCE_SHAPED_INPUT_REQUIREMENTS_MISSING"
    if not _present(request.get("checker_only_implementation_basis")):
        return "CHECKER_ONLY_IMPLEMENTATION_BASIS_MISSING"
    if not _present(request.get("implementation_limits")):
        return "IMPLEMENTATION_LIMITS_MISSING"
    if not _present(request.get("output_limits")):
        return "OUTPUT_LIMITS_MISSING"
    if not _present(request.get("execution_limits")):
        return "EXECUTION_LIMITS_MISSING"
    for posture_key, code in (
        ("no_command_authority_posture", "NO_COMMAND_AUTHORITY_POSTURE_MISSING"),
        ("no_output_source_posture", "NO_OUTPUT_SOURCE_POSTURE_MISSING"),
        ("no_success_currentness_posture", "NO_SUCCESS_CURRENTNESS_POSTURE_MISSING"),
        ("no_success_final_completion_posture", "NO_SUCCESS_FINAL_COMPLETION_POSTURE_MISSING"),
        ("contained_artifact_emission_posture", "CONTAINED_ARTIFACT_EMISSION_POSTURE_MISSING"),
    ):
        if not _present(required_postures.get(posture_key)):
            return code
    unsupported_scope = [
        value
        for value in scope_values
        if value not in SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE
    ]
    if unsupported_scope:
        return "UNSUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE"
    collapse = _collapse_code(request)
    if collapse is not None:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    *,
    selected_command_boundary_basis: Mapping[str, Any],
    selected_artifact_emission_containment_basis: Mapping[str, Any],
    selected_evidence_manifest_basis: Mapping[str, Any],
    selected_portable_verification_basis: Mapping[str, Any],
    required_evidence_classes: Any,
    required_surfaces: Any,
    reference_shape_requirements: Any,
    required_postures: Mapping[str, Any],
    scope_values: Sequence[str],
) -> list[dict[str, Any]]:
    unsupported_scope = [
        value
        for value in scope_values
        if value not in SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE
    ]
    checks = [
        _check(
            "implementation_boundary_question_declared",
            _present(request.get("command_implementation_boundary_question")),
            "declared implementation-boundary question",
            request.get("command_implementation_boundary_question"),
            "COMMAND_IMPLEMENTATION_BOUNDARY_QUESTION_UNDECLARED",
        ),
        _check(
            "implementation_boundary_intent_supported",
            request.get("command_implementation_boundary_intent")
            in SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_INTENTS
            and request.get("command_implementation_boundary_intent") != INTENT_BLOCK,
            sorted(SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_INTENTS - {INTENT_BLOCK}),
            request.get("command_implementation_boundary_intent"),
            "COMMAND_IMPLEMENTATION_BOUNDARY_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_command_boundary_basis_declared",
            bool(selected_command_boundary_basis.get("selected_command_boundary_basis_declared")),
            "selected command-boundary basis declared",
            selected_command_boundary_basis.get("selected_command_boundary_basis_declared"),
            "COMMAND_BOUNDARY_BASIS_MISSING",
        ),
        _check(
            "artifact_emission_containment_basis_declared",
            bool(
                selected_artifact_emission_containment_basis.get(
                    "selected_artifact_emission_containment_basis_declared"
                )
            ),
            "artifact emission containment basis declared",
            selected_artifact_emission_containment_basis.get(
                "selected_artifact_emission_containment_basis_declared"
            ),
            "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        ),
        _check(
            "evidence_manifest_basis_declared",
            bool(selected_evidence_manifest_basis.get("selected_evidence_manifest_basis_declared")),
            "evidence-manifest basis declared",
            selected_evidence_manifest_basis.get("selected_evidence_manifest_basis_declared"),
            "EVIDENCE_MANIFEST_BASIS_MISSING",
        ),
        _check(
            "portable_verification_basis_declared",
            bool(selected_portable_verification_basis.get("selected_portable_verification_basis_declared")),
            "portable verification basis declared",
            selected_portable_verification_basis.get("selected_portable_verification_basis_declared"),
            "PORTABLE_VERIFICATION_BASIS_MISSING",
        ),
        _check(
            "required_evidence_classes_declared",
            _present(required_evidence_classes),
            "required evidence classes declared",
            required_evidence_classes,
            "REQUIRED_EVIDENCE_CLASSES_MISSING",
        ),
        _check(
            "required_surfaces_declared",
            _present(required_surfaces),
            "required surfaces declared",
            required_surfaces,
            "REQUIRED_SURFACES_MISSING",
        ),
        _check(
            "reference_shaped_input_requirements_declared",
            _present(reference_shape_requirements),
            "reference-shaped input requirements declared",
            reference_shape_requirements,
            "REFERENCE_SHAPED_INPUT_REQUIREMENTS_MISSING",
        ),
        _check(
            "checker_only_implementation_basis_declared",
            _present(request.get("checker_only_implementation_basis")),
            "checker-only implementation basis declared",
            request.get("checker_only_implementation_basis"),
            "CHECKER_ONLY_IMPLEMENTATION_BASIS_MISSING",
        ),
        _check(
            "implementation_limits_declared",
            _present(request.get("implementation_limits")),
            "implementation limits declared",
            request.get("implementation_limits"),
            "IMPLEMENTATION_LIMITS_MISSING",
        ),
        _check(
            "output_limits_declared",
            _present(request.get("output_limits")),
            "output limits declared",
            request.get("output_limits"),
            "OUTPUT_LIMITS_MISSING",
        ),
        _check(
            "execution_limits_declared",
            _present(request.get("execution_limits")),
            "execution limits declared",
            request.get("execution_limits"),
            "EXECUTION_LIMITS_MISSING",
        ),
        _check(
            "implementation_boundary_scope_supported",
            not unsupported_scope,
            "supported implementation-boundary scope only",
            list(scope_values),
            "UNSUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE",
        ),
    ]
    for posture_key, code in (
        ("no_command_authority_posture", "NO_COMMAND_AUTHORITY_POSTURE_MISSING"),
        ("no_output_source_posture", "NO_OUTPUT_SOURCE_POSTURE_MISSING"),
        ("no_success_currentness_posture", "NO_SUCCESS_CURRENTNESS_POSTURE_MISSING"),
        ("no_success_final_completion_posture", "NO_SUCCESS_FINAL_COMPLETION_POSTURE_MISSING"),
        ("contained_artifact_emission_posture", "CONTAINED_ARTIFACT_EMISSION_POSTURE_MISSING"),
    ):
        checks.append(
            _check(
                f"{posture_key}_declared",
                _present(required_postures.get(posture_key)),
                f"{posture_key} declared",
                required_postures.get(posture_key),
                code,
            )
        )
    absence_checks = (
        ("command_implementation_not_created", "command_implemented", "command implementation not created", "COMMAND_IMPLEMENTATION_CREATED"),
        ("command_execution_not_authorized", "command_authorized_to_run", "command execution not authorized", "COMMAND_EXECUTION_AUTHORIZED"),
        ("command_invocation_not_created", "command_invocation_created", "command invocation not created", "COMMAND_INVOCATION_CREATED"),
        ("command_output_not_created", "command_output_created", "command output not created", "COMMAND_OUTPUT_CREATED"),
        ("command_result_not_created", "command_result_created", "command result not created", "COMMAND_RESULT_CREATED"),
        ("command_success_not_created", "command_success_created", "command success not created", "COMMAND_SUCCESS_CREATED"),
        ("command_output_not_source", "command_output_became_source", "command output not source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
        ("command_output_not_authority", "command_output_became_authority", "command output not authority", "COMMAND_OUTPUT_TREATED_AS_AUTHORITY"),
        ("command_success_not_currentness", "command_success_created_currentness", "command success not currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command_success_not_final_completion", "command_success_claimed_final_completion", "command success not final completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("command_not_authority", "command_became_authority", "command not authority", "COMMAND_TREATED_AS_AUTHORITY"),
        ("full_prior_artifacts_not_embedded", "full_prior_artifacts_embedded", "full prior artifacts not embedded", "FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"),
        ("artifacts_not_mutated", "prior_artifacts_mutated", "artifacts not mutated", "ARTIFACTS_MUTATED"),
        ("deployment_not_created", "deployment_created", "deployment not created", "DEPLOYMENT_CREATED"),
        ("runtime_hosting_not_created", "runtime_hosting_created", "runtime hosting not created", "RUNTIME_HOSTING_CREATED"),
        ("public_release_not_created", "public_release_created", "public release not created", "PUBLIC_RELEASE_CREATED"),
        ("source_transfer_not_created", "source_transferred", "source transfer not created", "SOURCE_TRANSFER_CREATED"),
        ("source_migration_not_created", "source_migrated", "source migration not created", "SOURCE_MIGRATION_CREATED"),
        ("source_receipt_not_created", "source_receipt_recorded", "source receipt not created", "SOURCE_RECEIPT_CREATED"),
        ("reception_not_authorized", "reception_authorized", "reception not authorized", "RECEPTION_AUTHORIZED"),
        ("operation_permission_not_created", "operation_permission_created", "operation permission not created", "OPERATION_PERMISSION_CREATED"),
        ("public_readiness_not_created", "public_launch_readiness_created", "public readiness not created", "PUBLIC_READINESS_CREATED"),
        ("final_completion_not_claimed", "final_completion_claimed", "final completion not claimed", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("continuation_not_authorized", "continuation_authorized", "continuation not authorized", "CONTINUATION_AUTHORIZED"),
        ("reusable_permission_not_created", "reusable_permission_created", "reusable permission not created", "REUSABLE_PERMISSION_CREATED"),
        ("derivative_reception_not_authorized", "derivative_reception_authorized", "derivative reception not authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
        ("vessel_relation_not_authorized", "vessel_relation_authorized", "vessel relation not authorized", "VESSEL_RELATION_AUTHORIZED"),
        ("another_reception_request_not_authorized", "another_reception_request_authorized", "another reception request not authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
        ("follow_on_work_not_authorized", "follow_on_work_authorized", "follow-on work not authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    )
    for check_name, key, expected, code in absence_checks:
        checks.append(
            _check(check_name, not _contains_truthy_key(request, key), expected, request.get(key), code)
        )
    checks.extend(
        [
            _check(
                "command_requires_declared_evidence_manifest",
                _present(request.get("selected_evidence_manifest_basis")),
                "command requires declared evidence-manifest",
                request.get("selected_evidence_manifest_basis"),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            _check(
                "command_requires_contained_reference_shape",
                _present(reference_shape_requirements),
                "command requires contained reference shape",
                reference_shape_requirements,
                "REFERENCE_SHAPED_INPUT_REQUIREMENTS_MISSING",
            ),
            _check(
                "execution_requires_separate_boundary",
                _present(request.get("execution_limits")),
                "execution requires separate boundary",
                request.get("execution_limits"),
                "EXECUTION_LIMITS_MISSING",
            ),
            _check(
                "no_mutation_replay_merge",
                not any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS),
                "no mutation/replay/merge",
                {
                    key: _contains_truthy_key(request, key)
                    for key in MUTATION_FLAGS
                },
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
            ),
            _check(
                "non_claims_remain_false",
                _required_non_claims_false(request),
                "required non-claims explicit and false",
                request.get("declared_non_claims"),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
    return checks


def _implementation_boundary_scope(scope_values: Sequence[str]) -> dict[str, Any]:
    return {
        "selected_scope_values": list(scope_values),
        "all_selected_scope_values_supported": all(
            value in SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE
            for value in scope_values
        ),
        "command_implementation_boundary_only": True,
        "command_implementation_not_created": True,
        "command_execution_not_authorized": True,
        "command_output_not_created": True,
        "command_success_not_created": True,
        "checker_only_implementation_conditions_declared": True,
        "command_requires_declared_evidence_manifest": True,
        "command_requires_contained_reference_shape": True,
        "command_output_is_not_source": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_is_not_authority": True,
        "command_is_not_deployment": True,
        "command_is_not_runtime_hosting": True,
        "command_is_not_public_release": True,
        "command_execution_requires_separate_boundary": True,
    }


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    request_malformed_code: str | None = None,
) -> dict[str, Any]:
    selected_command_boundary_basis = _selected_command_boundary_basis(request)
    selected_artifact_emission_containment_basis = (
        _selected_artifact_emission_containment_basis(request)
    )
    selected_evidence_manifest_basis = _selected_evidence_manifest_basis(request)
    selected_portable_verification_basis = _selected_portable_verification_basis(request)
    required_evidence_classes = _required_evidence_classes(request)
    required_surfaces = _required_surfaces(request)
    reference_shape_requirements = _reference_shape_requirements(request)
    required_postures = _required_postures(request)
    scope_values = _scope_values(request.get("implementation_boundary_scope"))

    block_code = request_malformed_code or _determine_block_code(
        request,
        selected_command_boundary_basis=selected_command_boundary_basis,
        selected_artifact_emission_containment_basis=selected_artifact_emission_containment_basis,
        selected_evidence_manifest_basis=selected_evidence_manifest_basis,
        selected_portable_verification_basis=selected_portable_verification_basis,
        required_evidence_classes=required_evidence_classes,
        required_surfaces=required_surfaces,
        reference_shape_requirements=reference_shape_requirements,
        required_postures=required_postures,
        scope_values=scope_values,
    )

    requested_outcome = (
        request.get("requested_command_implementation_boundary_outcome") or OUTCOME_RECORDED
    )
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("command_implementation_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = requested_outcome
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED"

    checks = _build_checks(
        request,
        selected_command_boundary_basis=selected_command_boundary_basis,
        selected_artifact_emission_containment_basis=selected_artifact_emission_containment_basis,
        selected_evidence_manifest_basis=selected_evidence_manifest_basis,
        selected_portable_verification_basis=selected_portable_verification_basis,
        required_evidence_classes=required_evidence_classes,
        required_surfaces=required_surfaces,
        reference_shape_requirements=reference_shape_requirements,
        required_postures=required_postures,
        scope_values=scope_values,
    )
    if outcome == OUTCOME_BLOCKED and block_code is not None:
        matched = any(
            check.get("passed") is False and check.get("block_code") == block_code
            for check in checks
        )
        if not matched:
            checks.append(
                _check(
                    "command_implementation_boundary_review_blocked",
                    False,
                    "non-blocked implementation-boundary review",
                    block_code,
                    block_code,
                )
            )

    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    if outcome == OUTCOME_RECORDED and failed_count != 0:
        outcome = OUTCOME_BLOCKED
        block_code = block_code or "COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED_WITH_FAILED_CHECKS"

    recorded = outcome == OUTCOME_RECORDED
    request_id = request.get("command_implementation_boundary_request_id")
    result_id_seed = _first_present(
        request_id,
        selected_command_boundary_basis.get("selected_command_boundary_result_id"),
        selected_evidence_manifest_basis.get("selected_evidence_manifest_result_id"),
    )
    result_id = (
        f"{_safe_component(result_id_seed)}"
        "__portable_source_body_verification_command_implementation_boundary_result"
    )
    passed_count = sum(1 for check in checks if check.get("passed") is True)

    checker_only_implementation_basis = {
        "checker_only_implementation_basis_as_supplied": _sanitize_reference_shape(
            request.get("checker_only_implementation_basis")
        ),
        "selected_required_evidence_classes": _sanitize_reference_shape(
            required_evidence_classes
        ),
        "selected_required_surfaces": _sanitize_reference_shape(required_surfaces),
        "selected_reference_shaped_input_requirements": _sanitize_reference_shape(
            reference_shape_requirements
        ),
        "future_code_may_only_inspect_declared_evidence_if_separately_implemented": True,
        "future_code_may_only_report_bounded_findings_if_separately_implemented_and_separately_executed": True,
        "implementation_must_require_declared_evidence_manifest_basis": True,
        "implementation_must_require_contained_reference_shape": True,
        "implementation_must_not_embed_full_prior_artifacts": True,
        "implementation_must_not_mutate_artifacts": True,
        "implementation_must_not_create_authority_currentness_final_completion": True,
        "execution_remains_separate_future_boundary": True,
    }
    implementation_limits = {
        "implementation_limits_as_supplied": _sanitize_reference_shape(
            request.get("implementation_limits")
        ),
        "no_command_authority_posture": _sanitize_reference_shape(
            required_postures.get("no_command_authority_posture")
        ),
        "contained_artifact_emission_posture": _sanitize_reference_shape(
            required_postures.get("contained_artifact_emission_posture")
        ),
        "implementation_boundary_only": True,
        "command_implementation_not_created": True,
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_is_not_authority": True,
        "command_requires_evidence_manifest": True,
        "command_requires_contained_reference_shape": True,
        "full_prior_artifact_embedding_blocked": True,
        "artifact_mutation_blocked": True,
        "deployment_runtime_public_release_not_created": True,
        "source_transfer_migration_receipt_reception_authorization_not_created": True,
    }
    output_limits = {
        "output_limits_as_supplied": _sanitize_reference_shape(request.get("output_limits")),
        "no_output_source_posture": _sanitize_reference_shape(
            required_postures.get("no_output_source_posture")
        ),
        "no_success_currentness_posture": _sanitize_reference_shape(
            required_postures.get("no_success_currentness_posture")
        ),
        "no_success_final_completion_posture": _sanitize_reference_shape(
            required_postures.get("no_success_final_completion_posture")
        ),
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_is_not_source": True,
        "command_output_is_not_authority": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_output_cannot_create_operation_permission_public_readiness_continuation_follow_on_work": True,
    }
    execution_limits = {
        "execution_limits_as_supplied": _sanitize_reference_shape(
            request.get("execution_limits")
        ),
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_authorized_to_run": False,
        "execution_requires_separate_boundary": True,
        "execution_cannot_be_inferred_from_implementation_boundary": True,
        "execution_cannot_create_output_success_currentness_final_completion_here": True,
    }
    implementation_boundary_statement = {
        "portable_source_body_verification_command_implementation_boundary_recorded": recorded,
        "checker_command_implementation_conditions_declared": recorded,
        "command_implementation_must_be_checker_only": recorded,
        "command_implementation_requires_contained_reference_shape": recorded,
        "command_execution_requires_separate_boundary": recorded,
        "selected_command_boundary_basis_preserved": recorded,
        "selected_artifact_emission_containment_basis_preserved": recorded,
        "selected_evidence_manifest_basis_preserved": recorded,
        "selected_portable_verification_basis_preserved": recorded,
        "checker_only_implementation_basis_declared": recorded,
        "implementation_limits_declared": recorded,
        "output_limits_declared": recorded,
        "execution_limits_declared": recorded,
        "implementation_boundary_only": True,
        "command_implementation_not_created": True,
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_is_not_source": True,
        "command_output_is_not_authority": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_is_not_authority": True,
        "command_requires_declared_evidence_manifest": True,
        "command_requires_contained_reference_shape": True,
        "command_must_not_embed_full_prior_artifacts": True,
        "command_must_not_mutate_artifacts": True,
        "execution_requires_separate_boundary": True,
        "command_implementation_boundary_recorded_as_implementation": False,
        "command_implemented": False,
        "command_executed": False,
        "command_authorized_to_run": False,
        "command_invocation_created": False,
        "command_output_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_became_source": False,
        "command_output_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "command_became_authority": False,
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
        "manifest_implemented": False,
        "checksum_implemented": False,
        "signature_implemented": False,
        "packet_implemented": False,
        "deployment_created": False,
        "runtime_hosting_created": False,
        "public_release_created": False,
        "operation_permission_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "reusable_permission_created": False,
        "derivative_reception_authorized": False,
        "vessel_relation_authorized": False,
        "another_reception_request_authorized": False,
        "follow_on_work_authorized": False,
        "recorded_true_fields_are_bounded_implementation_boundary_outcomes_only": True,
    }
    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": _sanitize_reference_shape(
            request.get("additional_basis_context")
        )
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }
    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": _sanitize_reference_shape(request.get("not_recorded_basis"))
        if outcome == OUTCOME_NOT_RECORDED
        else {},
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_implement": True,
        "not_recorded_does_not_execute": True,
        "not_recorded_does_not_invoke": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_create_success": True,
        "not_recorded_does_not_deploy_publish_host_currentize_adopt_continue_or_authorize_follow_on_work": True,
    }

    result: dict[str, Any] = {
        "portable_source_body_verification_command_implementation_boundary_metadata": {
            "portable_source_body_verification_command_implementation_boundary_result_id": result_id,
            "portable_source_body_verification_command_implementation_boundary_result_type": "portable_source_body_verification_command_implementation_boundary_result",
            "portable_source_body_verification_command_implementation_boundary_result_version": RESULT_VERSION,
            "generated_at": _generated_at(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_command_implementation_boundary_question": {
            "command_implementation_boundary_request_id": request_id,
            "command_implementation_boundary_question": request.get(
                "command_implementation_boundary_question"
            ),
            "command_implementation_boundary_intent": request.get(
                "command_implementation_boundary_intent"
            ),
            "request_path": request_path,
            "command_implementation_boundary_is_not_implementation": True,
            "command_is_not_executed": True,
            "command_output_is_not_source": True,
            "command_success_is_not_currentness": True,
            "command_success_is_not_final_completion": True,
            "command_execution_requires_separate_boundary": True,
        },
        "selected_command_boundary_basis": selected_command_boundary_basis,
        "selected_artifact_emission_containment_basis": selected_artifact_emission_containment_basis,
        "selected_evidence_manifest_basis": selected_evidence_manifest_basis,
        "selected_portable_verification_basis": selected_portable_verification_basis,
        "checker_only_implementation_basis": checker_only_implementation_basis,
        "implementation_limits": implementation_limits,
        "output_limits": output_limits,
        "execution_limits": execution_limits,
        "implementation_boundary_scope": _implementation_boundary_scope(scope_values),
        "implementation_boundary_checks": checks,
        "implementation_boundary_statement": implementation_boundary_statement,
        "implementation_boundary_non_meaning": _implementation_boundary_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _what_remains_open(),
        "non_claims": _build_non_claims(outcome),
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason")),
    }
    result["portable_source_body_verification_command_implementation_boundary_summary"] = (
        build_portable_source_body_verification_command_implementation_boundary_summary(result)
    )
    result[
        "portable_source_body_verification_command_implementation_boundary_summary"
    ].update(
        {
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
        }
    )
    return result


def resolve_portable_source_body_verification_command_implementation_boundary(
    declared_command_implementation_boundary_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_command_implementation_boundary_request is None:
        request: Mapping[str, Any] = {}
        return _build_result(request)
    if not isinstance(declared_command_implementation_boundary_request, Mapping):
        return _build_result(
            {},
            request_malformed_code="DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED",
        )
    return _build_result(copy.deepcopy(dict(declared_command_implementation_boundary_request)))


def resolve_portable_source_body_verification_command_implementation_boundary_from_path(
    declared_command_implementation_boundary_request_path: Path | str,
) -> dict[str, Any]:
    request, code = _read_json_object(declared_command_implementation_boundary_request_path)
    if code is not None:
        return _build_result(
            {},
            request_path=str(declared_command_implementation_boundary_request_path),
            request_malformed_code=code,
        )
    if request is None:
        return _build_result(
            {},
            request_path=str(declared_command_implementation_boundary_request_path),
            request_malformed_code="DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED",
        )
    return _build_result(
        request,
        request_path=str(declared_command_implementation_boundary_request_path),
    )


def build_portable_source_body_verification_command_implementation_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    statement = result.get("implementation_boundary_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    declared = result.get("declared_command_implementation_boundary_question", {})
    if not isinstance(declared, Mapping):
        declared = {}
    block = result.get("block", {})
    if not isinstance(block, Mapping):
        block = {}
    checks = result.get("implementation_boundary_checks", [])
    if not isinstance(checks, Sequence) or isinstance(checks, (str, bytes, bytearray)):
        checks = []
    passed_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
    )
    failed_count = sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True
    )
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}
    selected_command_boundary = result.get("selected_command_boundary_basis", {})
    selected_containment = result.get("selected_artifact_emission_containment_basis", {})
    selected_evidence_manifest = result.get("selected_evidence_manifest_basis", {})
    selected_portable_verification = result.get("selected_portable_verification_basis", {})
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("block_reason") or block.get("reason"),
        "command_implementation_boundary_request_id": declared.get(
            "command_implementation_boundary_request_id"
        ),
        "command_implementation_boundary_question": declared.get(
            "command_implementation_boundary_question"
        ),
        "command_implementation_boundary_intent": declared.get(
            "command_implementation_boundary_intent"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "command_implementation_boundary_recorded": bool(
            statement.get("portable_source_body_verification_command_implementation_boundary_recorded")
        ),
        "checker_command_implementation_conditions_declared": bool(
            statement.get("checker_command_implementation_conditions_declared")
        ),
        "command_implementation_must_be_checker_only": bool(
            statement.get("command_implementation_must_be_checker_only")
        ),
        "command_implementation_requires_contained_reference_shape": bool(
            statement.get("command_implementation_requires_contained_reference_shape")
        ),
        "command_execution_requires_separate_boundary": bool(
            statement.get("command_execution_requires_separate_boundary")
        ),
        "not_recorded": result.get("outcome") == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": result.get("outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_boundary_basis_preserved": bool(
            statement.get("selected_command_boundary_basis_preserved")
        ),
        "artifact_emission_containment_basis_preserved": bool(
            statement.get("selected_artifact_emission_containment_basis_preserved")
        ),
        "evidence_manifest_basis_preserved": bool(
            statement.get("selected_evidence_manifest_basis_preserved")
        ),
        "portable_verification_basis_preserved": bool(
            statement.get("selected_portable_verification_basis_preserved")
        ),
        "selected_command_boundary_result_id": selected_command_boundary.get(
            "selected_command_boundary_result_id"
        )
        if isinstance(selected_command_boundary, Mapping)
        else None,
        "selected_artifact_emission_containment_result_id": selected_containment.get(
            "selected_artifact_emission_containment_result_id"
        )
        if isinstance(selected_containment, Mapping)
        else None,
        "selected_evidence_manifest_result_id": selected_evidence_manifest.get(
            "selected_evidence_manifest_result_id"
        )
        if isinstance(selected_evidence_manifest, Mapping)
        else None,
        "selected_portable_verification_result_id": selected_portable_verification.get(
            "selected_portable_verification_result_id"
        )
        if isinstance(selected_portable_verification, Mapping)
        else None,
        "checker_only_implementation_basis_declared": bool(
            statement.get("checker_only_implementation_basis_declared")
        ),
        "implementation_limits_declared": bool(statement.get("implementation_limits_declared")),
        "output_limits_declared": bool(statement.get("output_limits_declared")),
        "execution_limits_declared": bool(statement.get("execution_limits_declared")),
        "implementation_boundary_only": bool(statement.get("implementation_boundary_only")),
        "command_implementation_not_created": bool(
            statement.get("command_implementation_not_created")
        ),
        "command_execution_not_authorized": bool(
            statement.get("command_execution_not_authorized")
        ),
        "command_invocation_output_result_success_not_created": all(
            bool(statement.get(key))
            for key in (
                "command_invocation_not_created",
                "command_output_not_created",
                "command_result_not_created",
                "command_success_not_created",
            )
        ),
        "command_output_not_source_or_authority": bool(
            statement.get("command_output_is_not_source")
        )
        and bool(statement.get("command_output_is_not_authority")),
        "command_success_not_currentness_or_final_completion": bool(
            statement.get("command_success_is_not_currentness")
        )
        and bool(statement.get("command_success_is_not_final_completion")),
        "command_not_authority": bool(statement.get("command_is_not_authority")),
        "command_requires_evidence_manifest_and_contained_reference_shape": bool(
            statement.get("command_requires_declared_evidence_manifest")
        )
        and bool(statement.get("command_requires_contained_reference_shape")),
        "no_full_prior_artifacts_embedded": non_claims.get("full_prior_artifacts_embedded") is False,
        "no_artifact_mutation": non_claims.get("prior_artifacts_mutated") is False,
        "no_deployment_runtime_public_release": all(
            non_claims.get(key) is False
            for key in (
                "deployment_created",
                "runtime_hosting_created",
                "public_release_created",
            )
        ),
        "no_operation_permission_public_readiness_final_completion": all(
            non_claims.get(key) is False
            for key in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        ),
        "no_continuation_publication_flow_reusable_permission": all(
            non_claims.get(key) is False
            for key in (
                "continuation_authorized",
                "publication_flow_opened",
                "reusable_permission_created",
            )
        ),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": all(
            non_claims.get(key) is False
            for key in (
                "derivative_reception_authorized",
                "vessel_relation_authorized",
                "another_reception_request_authorized",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if key in non_claims
        },
    }


def _unique_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_command_implementation_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandImplementationBoundaryError(
            "result must be a mapping"
        )
    if output_path is None:
        metadata = result.get(
            "portable_source_body_verification_command_implementation_boundary_metadata",
            {},
        )
        if not isinstance(metadata, Mapping):
            metadata = {}
        result_id = metadata.get(
            "portable_source_body_verification_command_implementation_boundary_result_id"
        )
        filename = (
            f"{_safe_component(result_id)}"
            "__portable_source_body_verification_command_implementation_boundary_result.json"
        )
        path = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
    path = _unique_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_portable_source_body_verification_command_implementation_boundary_request(
    command_implementation_boundary_request_id: str,
    command_implementation_boundary_question: str,
    selected_command_boundary_basis: Mapping[str, Any] | str,
    selected_artifact_emission_containment_basis: Mapping[str, Any] | str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    checker_only_implementation_basis: Mapping[str, Any] | str,
    implementation_limits: Mapping[str, Any] | str,
    output_limits: Mapping[str, Any] | str,
    execution_limits: Mapping[str, Any] | str,
    implementation_boundary_scope: Sequence[str] | Mapping[str, Any],
    command_implementation_boundary_intent: str = INTENT_RECORD,
    *,
    selected_command_boundary_result_path: str | None = None,
    selected_command_boundary_result_id: str | None = None,
    selected_command_boundary_result_outcome: str | None = None,
    requested_command_implementation_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    return {
        "command_implementation_boundary_request_id": command_implementation_boundary_request_id,
        "command_implementation_boundary_question": command_implementation_boundary_question,
        "command_implementation_boundary_intent": command_implementation_boundary_intent,
        "selected_command_boundary_basis": _sanitize_reference_shape(
            selected_command_boundary_basis
        ),
        "selected_artifact_emission_containment_basis": _sanitize_reference_shape(
            selected_artifact_emission_containment_basis
        ),
        "selected_evidence_manifest_basis": _sanitize_reference_shape(
            selected_evidence_manifest_basis
        ),
        "selected_portable_verification_basis": _sanitize_reference_shape(
            selected_portable_verification_basis
        ),
        "checker_only_implementation_basis": _sanitize_reference_shape(
            checker_only_implementation_basis
        ),
        "implementation_limits": _sanitize_reference_shape(implementation_limits),
        "output_limits": _sanitize_reference_shape(output_limits),
        "execution_limits": _sanitize_reference_shape(execution_limits),
        "implementation_boundary_scope": _sanitize_reference_shape(
            implementation_boundary_scope
        ),
        "selected_command_boundary_result_path": selected_command_boundary_result_path,
        "selected_command_boundary_result_id": selected_command_boundary_result_id,
        "selected_command_boundary_result_outcome": selected_command_boundary_result_outcome,
        "selected_required_evidence_classes": {
            "required_evidence_classes_declared": True,
            "evidence_classes_are_evidence_only": True,
            "evidence_classes_do_not_implement_command": True,
            "evidence_classes_do_not_authorize_execution": True,
        },
        "selected_required_surfaces": {
            "required_surfaces_declared": True,
            "surfaces_are_evidence_only": True,
            "surfaces_do_not_create_source_authority_currentness": True,
            "surfaces_do_not_authorize_command_execution": True,
        },
        "selected_reference_shaped_input_requirements": {
            "reference_shaped_input_requirements_declared": True,
            "contained_reference_shape_required": True,
            "full_prior_artifact_embedding_blocked": True,
            "artifact_mutation_blocked": True,
        },
        "no_command_authority_posture": {
            "no_command_authority_posture_declared": True,
            "command_does_not_become_authority": True,
        },
        "no_output_source_posture": {
            "no_output_source_posture_declared": True,
            "command_output_does_not_become_source": True,
        },
        "no_success_currentness_posture": {
            "no_success_currentness_posture_declared": True,
            "command_success_does_not_create_currentness": True,
        },
        "no_success_final_completion_posture": {
            "no_success_final_completion_posture_declared": True,
            "command_success_does_not_claim_final_completion": True,
        },
        "contained_artifact_emission_posture": {
            "contained_artifact_emission_posture_declared": True,
            "reference_shape_required": True,
            "recursive_full_artifact_embedding_blocked": True,
        },
        "requested_command_implementation_boundary_outcome": (
            requested_command_implementation_boundary_outcome
        ),
        "additional_basis_context": _sanitize_reference_shape(additional_basis_context)
        if additional_basis_context is not None
        else None,
        "not_recorded_basis": _sanitize_reference_shape(not_recorded_basis)
        if not_recorded_basis is not None
        else None,
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
