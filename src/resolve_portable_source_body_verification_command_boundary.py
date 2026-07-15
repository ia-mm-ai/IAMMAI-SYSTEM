"""Resolve the portable source-body verification command boundary.

This resolver answers one question only:

    Can a future portable source-body verification command posture be bounded
    as checker-only without implementing or authorizing a command?

Command boundary records declared checker-only command posture only. It is not
command implementation, command execution, command invocation, command output,
command success, manifest implementation, checksum implementation, signature
implementation, packet implementation, source transfer, migration, source
receipt, reception authorization, deployment, runtime hosting, public release,
authority, currentness, operation permission, public readiness, final
completion, continuation, reusable permission, derivative reception, vessel
relation, another reception request, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationCommandBoundaryError(Exception):
    """Raised for hard command-boundary failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_boundary"
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_boundary"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_REVIEW"
SUPPORTED_COMMAND_BOUNDARY_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_COMMAND_BOUNDARY_SCOPE = {
    "COMMAND_BOUNDARY_ONLY",
    "COMMAND_IS_CHECKER_ONLY_IF_SEPARATELY_IMPLEMENTED",
    "COMMAND_IS_NOT_IMPLEMENTED",
    "COMMAND_IS_NOT_EXECUTED",
    "COMMAND_OUTPUT_IS_NOT_SOURCE",
    "COMMAND_SUCCESS_IS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_IS_NOT_FINAL_COMPLETION",
    "COMMAND_IS_NOT_AUTHORITY",
    "COMMAND_IS_NOT_MANIFEST",
    "COMMAND_IS_NOT_CHECKSUM",
    "COMMAND_IS_NOT_SIGNATURE",
    "COMMAND_IS_NOT_PACKET",
    "COMMAND_IS_NOT_TRANSFER",
    "COMMAND_IS_NOT_MIGRATION",
    "COMMAND_IS_NOT_SOURCE_RECEIPT",
    "COMMAND_IS_NOT_RECEPTION_AUTHORIZATION",
    "COMMAND_IS_NOT_DEPLOYMENT",
    "COMMAND_IS_NOT_RUNTIME_HOSTING",
    "COMMAND_IS_NOT_PUBLIC_RELEASE",
    "COMMAND_REQUIRES_EVIDENCE_MANIFEST",
    "COMMAND_IMPLEMENTATION_REQUIRES_SEPARATE_BOUNDARY",
    "PATH_DOES_NOT_CREATE_CURRENTNESS",
    "ARTIFACT_EXISTENCE_DOES_NOT_CREATE_CURRENTNESS",
    "REPOSITORY_COPY_DOES_NOT_BECOME_BODY",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "command_boundary_recorded_as_implementation",
    "command_implemented",
    "command_executed",
    "command_authorized_to_run",
    "command_output_created",
    "command_output_became_source",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "manifest_implemented",
    "checksum_implemented",
    "signature_implemented",
    "packet_implemented",
    "source_transferred",
    "source_migrated",
    "source_received",
    "source_receipt_recorded",
    "reception_authorized",
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
            "command_invocation_created",
            "command_result_created",
            "command_success_created",
            "manifest_exists",
            "checksum_exists",
            "signature_exists",
            "packet_exists",
            "source_receipt_created",
            "authority_created",
            "currentness_created",
            "adoption_created",
            "standing_created",
            "public_readiness_created",
            "path_created_currentness",
            "local_path_created_currentness",
            "latest_file_created_currentness",
            "artifact_existence_created_currentness",
            "repository_copy_became_body",
            "carrier_possession_created_currentness",
            "archive_possession_created_currentness",
            "exit_code_created_currentness",
            "environment_state_created_authority",
            "environment_state_created_currentness",
            "os_became_authority",
            "vendor_environment_became_authority",
            "account_became_authority",
            "narration_created_currentness",
        )
    )
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "portable_source_body_verification_command_boundary_recorded",
    "verification_command_posture_declared",
    "verification_command_checker_role_bounded",
    "command_requires_declared_evidence_manifest",
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = (
    ("command_boundary_recorded_as_implementation", "COMMAND_TREATED_AS_IMPLEMENTED"),
    ("command_implemented", "COMMAND_TREATED_AS_IMPLEMENTED"),
    ("command_treated_as_implemented", "COMMAND_TREATED_AS_IMPLEMENTED"),
    ("command_exists", "COMMAND_TREATED_AS_IMPLEMENTED"),
    ("command_executed", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_invocation_created", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_executable", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_treated_as_executable", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_authorized_to_run", "COMMAND_TREATED_AS_AUTHORIZED_TO_RUN"),
    ("command_authorized", "COMMAND_TREATED_AS_AUTHORIZED_TO_RUN"),
    ("command_treated_as_authorized_to_run", "COMMAND_TREATED_AS_AUTHORIZED_TO_RUN"),
    ("command_output_created", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_result_created", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_success_created", "COMMAND_TREATED_AS_EXECUTABLE"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_success_treated_as_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("command_became_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("command_treated_as_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("command_result_became_authority", "COMMAND_TREATED_AS_AUTHORITY"),
    ("manifest_implemented", "COMMAND_CREATES_MANIFEST"),
    ("manifest_created", "COMMAND_CREATES_MANIFEST"),
    ("checksum_implemented", "COMMAND_CREATES_CHECKSUM"),
    ("checksum_created", "COMMAND_CREATES_CHECKSUM"),
    ("signature_implemented", "COMMAND_CREATES_SIGNATURE"),
    ("signature_created", "COMMAND_CREATES_SIGNATURE"),
    ("packet_implemented", "COMMAND_CREATES_PACKET"),
    ("source_body_packet_implemented", "COMMAND_CREATES_PACKET"),
    ("packet_created", "COMMAND_CREATES_PACKET"),
    ("source_transferred", "COMMAND_CREATES_TRANSFER"),
    ("source_body_transferred", "COMMAND_CREATES_TRANSFER"),
    ("source_migrated", "COMMAND_CREATES_MIGRATION"),
    ("source_body_migrated", "COMMAND_CREATES_MIGRATION"),
    ("source_received", "COMMAND_CREATES_SOURCE_RECEIPT"),
    ("source_receipt_recorded", "COMMAND_CREATES_SOURCE_RECEIPT"),
    ("source_receipt_created", "COMMAND_CREATES_SOURCE_RECEIPT"),
    ("reception_authorized", "COMMAND_AUTHORIZES_RECEPTION"),
    ("deployment_created", "COMMAND_CREATES_DEPLOYMENT"),
    ("runtime_hosting_created", "COMMAND_CREATES_RUNTIME_HOSTING"),
    ("public_release_created", "COMMAND_CREATES_PUBLIC_RELEASE"),
    ("operation_permission_created", "COMMAND_CREATES_OPERATION_PERMISSION"),
    ("public_launch_readiness_created", "COMMAND_CREATES_PUBLIC_READINESS"),
    ("public_readiness_created", "COMMAND_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("continuation_authorized", "COMMAND_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "COMMAND_AUTHORIZES_CONTINUATION"),
    ("reusable_permission_created", "COMMAND_CREATES_REUSABLE_PERMISSION"),
    ("derivative_reception_authorized", "COMMAND_AUTHORIZES_DERIVATIVE_RECEPTION"),
    ("vessel_relation_authorized", "COMMAND_AUTHORIZES_VESSEL_RELATION"),
    ("another_reception_request_authorized", "COMMAND_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
    ("successor_reception_request_authorized", "COMMAND_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
    ("follow_on_work_authorized", "COMMAND_AUTHORIZES_FOLLOW_ON_WORK"),
    ("path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("local_path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("path_treated_as_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_created_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    ("latest_file_treated_as_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    ("artifact_existence_created_currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
    ("artifact_existence_treated_as_currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
    ("repository_copy_became_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    ("repository_copy_treated_as_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    ("carrier_possession_created_currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("carrier_possession_treated_as_currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("archive_possession_created_currentness", "ARCHIVE_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("archive_possession_treated_as_currentness", "ARCHIVE_POSSESSION_TREATED_AS_CURRENTNESS"),
    ("exit_code_created_currentness", "EXIT_CODE_TREATED_AS_CURRENTNESS"),
    ("exit_code_treated_as_currentness", "EXIT_CODE_TREATED_AS_CURRENTNESS"),
    ("environment_state_created_authority", "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS"),
    ("environment_state_created_currentness", "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS"),
    ("environment_state_treated_as_authority", "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS"),
    ("environment_state_treated_as_currentness", "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS"),
    ("os_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("operating_system_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("vendor_environment_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("vendor_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("account_became_authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
    ("narration_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    ("narrator_trust_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
)


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
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
            "authorized",
            "created",
            "executed",
            "run",
            "source",
            "authority",
            "current",
            "deployed",
            "released",
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


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    json_path = Path(path)
    try:
        payload = json.loads(json_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError):
        return None, "unreadable"
    except json.JSONDecodeError:
        return None, "malformed"
    if not isinstance(payload, Mapping):
        return None, "malformed"
    return copy.deepcopy(dict(payload)), None


def _text_path_metadata(path: Path | str) -> dict[str, Any]:
    text_path = Path(path)
    metadata: dict[str, Any] = {
        "path": str(text_path),
        "path_supplied": True,
        "path_readable": False,
        "path_read_error": None,
        "path_is_evidence_only": True,
        "path_does_not_create_source": True,
        "path_does_not_create_authority": True,
        "path_does_not_create_currentness": True,
        "path_does_not_authorize_command": True,
        "path_does_not_create_command_output": True,
    }
    try:
        text = text_path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError) as exc:
        metadata["path_read_error"] = type(exc).__name__
        return metadata
    metadata["path_readable"] = True
    metadata["byte_length"] = len(text.encode("utf-8"))
    metadata["line_count"] = len(text.splitlines())
    return metadata


def _normalize_basis(value: Any, reference_key: str) -> dict[str, Any] | None:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    if _present(value):
        return {
            reference_key: value,
            "basis_reference": value,
            "basis_is_reference_only": True,
        }
    return None


def _load_json_basis(
    request: Mapping[str, Any],
    *,
    value_key: str,
    path_key: str,
    reference_key: str,
    unreadable_code: str,
    malformed_code: str,
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path_value = request.get(path_key)
    if _present(path_value):
        loaded, failure = _read_json_object(Path(str(path_value)))
        if failure == "unreadable":
            return None, str(path_value), unreadable_code
        if failure == "malformed":
            return None, str(path_value), malformed_code
        return loaded, str(path_value), None
    return _normalize_basis(request.get(value_key), reference_key), None, None


def _load_selected_evidence_manifest_basis(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    basis, path, failure = _load_json_basis(
        request,
        value_key="selected_evidence_manifest_basis",
        path_key="selected_evidence_manifest_result_path",
        reference_key="selected_evidence_manifest_basis_reference",
        unreadable_code="EVIDENCE_MANIFEST_BASIS_UNREADABLE",
        malformed_code="EVIDENCE_MANIFEST_BASIS_MALFORMED",
    )
    terminal_summary_path = request.get("selected_evidence_manifest_terminal_summary_path")
    if _present(terminal_summary_path):
        if basis is None:
            basis = {}
        basis["selected_evidence_manifest_terminal_summary_path"] = str(
            terminal_summary_path
        )
        basis["selected_evidence_manifest_terminal_summary_path_metadata"] = (
            _text_path_metadata(str(terminal_summary_path))
        )
        basis["terminal_summary_path_is_evidence_only"] = True
        basis["terminal_summary_path_does_not_create_currentness"] = True
        basis["terminal_summary_path_does_not_authorize_command"] = True
    return basis, path, failure


def _load_selected_portable_verification_basis(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    basis, path, failure = _load_json_basis(
        request,
        value_key="selected_portable_verification_basis",
        path_key="selected_portable_verification_result_path",
        reference_key="selected_portable_verification_basis_reference",
        unreadable_code="PORTABLE_VERIFICATION_BASIS_UNREADABLE",
        malformed_code="PORTABLE_VERIFICATION_BASIS_MALFORMED",
    )
    terminal_summary_path = request.get("selected_portable_verification_terminal_summary_path")
    if _present(terminal_summary_path):
        if basis is None:
            basis = {}
        basis["selected_portable_verification_terminal_summary_path"] = str(
            terminal_summary_path
        )
        basis["selected_portable_verification_terminal_summary_path_metadata"] = (
            _text_path_metadata(str(terminal_summary_path))
        )
        basis["terminal_summary_path_is_evidence_only"] = True
        basis["terminal_summary_path_does_not_create_currentness"] = True
        basis["terminal_summary_path_does_not_authorize_command"] = True
    return basis, path, failure


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = _first_present(
            scope.get("selected_command_scope_values"),
            scope.get("command_boundary_scope_values"),
            scope.get("command_scope_values"),
            scope.get("selected_scope_values"),
            scope.get("scope_values"),
        )
        if values is None:
            values = [
                key for key, value in scope.items() if isinstance(key, str) and _truthy(value)
            ]
        return [str(value) for value in values] if isinstance(values, Sequence) else []
    if isinstance(scope, Sequence) and not isinstance(scope, (str, bytes)):
        return [str(value) for value in scope]
    return []


def _contains_truthy_key(value: Any, key: str) -> bool:
    if isinstance(value, Mapping):
        for current_key, current_value in value.items():
            if current_key == key and _truthy(current_value):
                return True
            if _contains_truthy_key(current_value, key):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_truthy_key(item, key) for item in value)
    return False


def _safe_component(value: Any) -> str:
    text = str(value or "portable_source_body_verification_command_boundary").strip()
    cleaned = "".join(
        character if character.isalnum() or character in ("-", "_") else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "portable_source_body_verification_command_boundary"


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": reason if code is not None else None,
    }


def _basis_id(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("portable_source_body_verification_evidence_manifest_result_id"),
            basis.get("selected_evidence_manifest_result_id"),
            basis.get("selected_evidence_manifest_basis_id"),
            basis.get("portable_source_body_verification_result_id"),
            basis.get("selected_portable_verification_result_id"),
            basis.get("selected_portable_verification_basis_id"),
            basis.get("basis_id"),
            basis.get("id"),
            basis.get("reference"),
            basis.get("basis_reference"),
        ]
    )
    return _first_present(*candidates)


def _basis_reference(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("selected_evidence_manifest_basis_reference"),
            basis.get("selected_portable_verification_basis_reference"),
            basis.get("reference"),
            basis.get("path"),
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
            basis.get("outcome"),
            _value_at(basis, ("portable_source_body_verification_evidence_manifest_summary", "outcome")),
            _value_at(basis, ("portable_source_body_verification_summary", "outcome")),
        ]
    )
    return _first_present(*candidates)


def _selected_evidence_classes(
    request: Mapping[str, Any],
    evidence_manifest_basis: Mapping[str, Any] | None,
) -> Any:
    return _first_present(
        request.get("selected_evidence_classes"),
        _value_at(evidence_manifest_basis, ("declared_evidence_classes",)),
        _value_at(evidence_manifest_basis, ("declared_evidence_classes", "declared_evidence_classes_as_supplied")),
        _value_at(evidence_manifest_basis, ("declared_evidence_classes", "declared_evidence_classes_representative")),
        _value_at(evidence_manifest_basis, ("portable_source_body_verification_evidence_manifest_summary", "declared_evidence_classes_representative")),
    )


def _selected_required_surfaces(
    request: Mapping[str, Any],
    evidence_manifest_basis: Mapping[str, Any] | None,
) -> Any:
    return _first_present(
        request.get("selected_required_surfaces"),
        _value_at(evidence_manifest_basis, ("required_surfaces",)),
    )


def _selected_future_candidate_postures(
    request: Mapping[str, Any],
    evidence_manifest_basis: Mapping[str, Any] | None,
) -> Any:
    return _first_present(
        request.get("selected_future_candidate_postures"),
        _value_at(evidence_manifest_basis, ("future_candidate_postures",)),
    )


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
            "even_when_command_boundary_recorded_no_command_exists": True,
            "even_when_command_boundary_recorded_no_command_is_implemented": True,
            "even_when_command_boundary_recorded_no_command_is_authorized_to_run": True,
            "even_when_command_boundary_recorded_no_command_is_executed": True,
            "even_when_command_boundary_recorded_no_command_output_exists": True,
            "even_when_command_boundary_recorded_no_command_success_exists": True,
            "even_when_command_boundary_recorded_command_implementation_remains_future_work": True,
            "even_when_command_boundary_recorded_no_manifest_checksum_signature_packet_runtime_deployment_public_release_transfer_migration_receipt_reception_authority_currentness_permission_readiness_completion_continuation_reusable_permission_derivative_vessel_successor_or_follow_on_work_is_created_or_authorized": True,
        }
    )
    return non_claims


def _build_command_boundary_non_meaning() -> dict[str, bool]:
    names = (
        "command_exists",
        "command_is_implemented",
        "command_is_executable",
        "command_is_authorized_to_run",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "command_success_creates_currentness",
        "command_success_creates_final_completion",
        "command_output_becomes_source",
        "manifest_exists",
        "checksum_exists",
        "signature_exists",
        "packet_exists",
        "source_transferred",
        "source_migrated",
        "source_received",
        "source_receipt_recorded",
        "reception_authorized",
        "deployment_created",
        "runtime_hosting_created",
        "public_release_created",
        "public_readiness_created",
        "final_completion_claimed",
        "continuation_authorized",
        "reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_reception_request_authorized",
        "follow_on_work_authorized",
    )
    return {f"command_boundary_does_not_mean_{name}": True for name in names}


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "portable verification command boundary test",
            "portable verification command boundary live artifact",
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


def _determine_block_code(
    request: Mapping[str, Any],
    evidence_manifest_basis: Mapping[str, Any] | None,
    evidence_manifest_basis_load_code: str | None,
    portable_verification_basis: Mapping[str, Any] | None,
    portable_verification_basis_load_code: str | None,
    selected_evidence_classes: Any,
    selected_required_surfaces: Any,
    selected_future_candidate_postures: Any,
    checker_command_basis: Any,
    command_limits: Any,
    command_dependency_on_evidence_manifest: Any,
    no_command_authority_posture: Any,
    no_command_currentness_posture: Any,
    no_command_output_source_posture: Any,
    no_command_success_final_completion_posture: Any,
    non_execution_posture: Any,
    scope_values: Sequence[str],
) -> str | None:
    if not _present(request.get("command_boundary_question")):
        return "COMMAND_BOUNDARY_QUESTION_UNDECLARED"
    intent = request.get("command_boundary_intent")
    if intent == INTENT_BLOCK:
        return "COMMAND_BOUNDARY_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_COMMAND_BOUNDARY_INTENTS:
        return "COMMAND_BOUNDARY_INTENT_UNSUPPORTED"
    for load_code in (evidence_manifest_basis_load_code, portable_verification_basis_load_code):
        if load_code is not None:
            return load_code
    if evidence_manifest_basis is None:
        return "EVIDENCE_MANIFEST_BASIS_MISSING"
    if portable_verification_basis is None:
        return "PORTABLE_VERIFICATION_BASIS_MISSING"
    if not _present(selected_evidence_classes):
        return "EVIDENCE_CLASSES_MISSING"
    if not _present(selected_required_surfaces):
        return "REQUIRED_SURFACES_MISSING"
    if not _present(selected_future_candidate_postures):
        return "FUTURE_CANDIDATE_POSTURES_MISSING"
    if not _present(checker_command_basis):
        return "CHECKER_COMMAND_BASIS_MISSING"
    if not _present(command_limits):
        return "COMMAND_LIMITS_MISSING"
    if not _present(command_dependency_on_evidence_manifest):
        return "COMMAND_DEPENDENCY_ON_EVIDENCE_MANIFEST_MISSING"
    if not _present(no_command_authority_posture):
        return "NO_COMMAND_AUTHORITY_POSTURE_MISSING"
    if not _present(no_command_currentness_posture):
        return "NO_COMMAND_CURRENTNESS_POSTURE_MISSING"
    if not _present(no_command_output_source_posture):
        return "NO_COMMAND_OUTPUT_SOURCE_POSTURE_MISSING"
    if not _present(no_command_success_final_completion_posture):
        return "NO_COMMAND_SUCCESS_FINAL_COMPLETION_POSTURE_MISSING"
    if not _present(non_execution_posture):
        return "NON_EXECUTION_POSTURE_MISSING"
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_COMMAND_BOUNDARY_SCOPE
    ]
    if unsupported_scope:
        return "UNSUPPORTED_COMMAND_BOUNDARY_SCOPE"
    collapse = _collapse_code(request)
    if collapse is not None:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    evidence_manifest_basis: Mapping[str, Any] | None,
    portable_verification_basis: Mapping[str, Any] | None,
    selected_evidence_classes: Any,
    selected_required_surfaces: Any,
    selected_future_candidate_postures: Any,
    checker_command_basis: Any,
    command_limits: Any,
    command_dependency_on_evidence_manifest: Any,
    no_command_authority_posture: Any,
    no_command_currentness_posture: Any,
    no_command_output_source_posture: Any,
    no_command_success_final_completion_posture: Any,
    non_execution_posture: Any,
    scope_values: Sequence[str],
) -> list[dict[str, Any]]:
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_COMMAND_BOUNDARY_SCOPE
    ]
    checks = [
        _check(
            "command_boundary_question_declared",
            _present(request.get("command_boundary_question")),
            "declared command-boundary question",
            request.get("command_boundary_question"),
            "COMMAND_BOUNDARY_QUESTION_UNDECLARED",
        ),
        _check(
            "command_boundary_intent_supported",
            request.get("command_boundary_intent") in SUPPORTED_COMMAND_BOUNDARY_INTENTS
            and request.get("command_boundary_intent") != INTENT_BLOCK,
            sorted(SUPPORTED_COMMAND_BOUNDARY_INTENTS - {INTENT_BLOCK}),
            request.get("command_boundary_intent"),
            "COMMAND_BOUNDARY_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_evidence_manifest_result_or_terminal_summary_declared",
            evidence_manifest_basis is not None,
            "selected evidence-manifest result or terminal summary declared",
            evidence_manifest_basis is not None,
            "EVIDENCE_MANIFEST_BASIS_MISSING",
        ),
        _check(
            "selected_portable_verification_result_or_terminal_summary_declared",
            portable_verification_basis is not None,
            "selected portable verification result or terminal summary declared",
            portable_verification_basis is not None,
            "PORTABLE_VERIFICATION_BASIS_MISSING",
        ),
        _check(
            "selected_evidence_manifest_basis_declared",
            evidence_manifest_basis is not None,
            "selected evidence-manifest basis declared",
            evidence_manifest_basis is not None,
            "EVIDENCE_MANIFEST_BASIS_MISSING",
        ),
        _check(
            "selected_evidence_classes_declared",
            _present(selected_evidence_classes),
            "selected evidence classes declared",
            selected_evidence_classes,
            "EVIDENCE_CLASSES_MISSING",
        ),
        _check(
            "selected_required_surfaces_declared",
            _present(selected_required_surfaces),
            "selected required surfaces declared",
            selected_required_surfaces,
            "REQUIRED_SURFACES_MISSING",
        ),
        _check(
            "future_candidate_postures_declared",
            _present(selected_future_candidate_postures),
            "future candidate postures declared",
            selected_future_candidate_postures,
            "FUTURE_CANDIDATE_POSTURES_MISSING",
        ),
        _check(
            "checker_only_command_basis_declared",
            _present(checker_command_basis),
            "checker-only command basis declared",
            checker_command_basis,
            "CHECKER_COMMAND_BASIS_MISSING",
        ),
        _check(
            "command_limits_declared",
            _present(command_limits),
            "command limits declared",
            command_limits,
            "COMMAND_LIMITS_MISSING",
        ),
        _check(
            "command_dependency_on_evidence_manifest_declared",
            _present(command_dependency_on_evidence_manifest),
            "command dependency on evidence-manifest declared",
            command_dependency_on_evidence_manifest,
            "COMMAND_DEPENDENCY_ON_EVIDENCE_MANIFEST_MISSING",
        ),
        _check(
            "no_command_authority_posture_declared",
            _present(no_command_authority_posture),
            "no-command-authority posture declared",
            no_command_authority_posture,
            "NO_COMMAND_AUTHORITY_POSTURE_MISSING",
        ),
        _check(
            "no_command_currentness_posture_declared",
            _present(no_command_currentness_posture),
            "no-command-currentness posture declared",
            no_command_currentness_posture,
            "NO_COMMAND_CURRENTNESS_POSTURE_MISSING",
        ),
        _check(
            "no_command_output_source_posture_declared",
            _present(no_command_output_source_posture),
            "no-command-output-source posture declared",
            no_command_output_source_posture,
            "NO_COMMAND_OUTPUT_SOURCE_POSTURE_MISSING",
        ),
        _check(
            "no_command_success_final_completion_posture_declared",
            _present(no_command_success_final_completion_posture),
            "no-command-success-final-completion posture declared",
            no_command_success_final_completion_posture,
            "NO_COMMAND_SUCCESS_FINAL_COMPLETION_POSTURE_MISSING",
        ),
        _check(
            "explicit_non_execution_posture_declared",
            _present(non_execution_posture),
            "explicit non-execution posture declared",
            non_execution_posture,
            "NON_EXECUTION_POSTURE_MISSING",
        ),
        _check(
            "command_boundary_scope_supported",
            not unsupported_scope,
            "supported command-boundary scope only",
            list(scope_values),
            "UNSUPPORTED_COMMAND_BOUNDARY_SCOPE",
        ),
    ]

    absence_checks = (
        ("command_checker_only_if_separately_implemented", "command_implemented", "command checker-only if separately implemented", "COMMAND_TREATED_AS_IMPLEMENTED"),
        ("command_not_implemented", "command_implemented", "command not implemented", "COMMAND_TREATED_AS_IMPLEMENTED"),
        ("command_not_executed", "command_executed", "command not executed", "COMMAND_TREATED_AS_EXECUTABLE"),
        ("command_not_authorized_to_run", "command_authorized_to_run", "command not authorized to run", "COMMAND_TREATED_AS_AUTHORIZED_TO_RUN"),
        ("command_output_not_created", "command_output_created", "command output not created", "COMMAND_TREATED_AS_EXECUTABLE"),
        ("command_output_not_source", "command_output_became_source", "command output not source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
        ("command_success_not_currentness", "command_success_created_currentness", "command success not currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("command_success_not_final_completion", "command_success_claimed_final_completion", "command success not final completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
        ("command_not_authority", "command_became_authority", "command not authority", "COMMAND_TREATED_AS_AUTHORITY"),
        ("command_does_not_create_manifest", "manifest_implemented", "command does not create manifest", "COMMAND_CREATES_MANIFEST"),
        ("command_does_not_create_checksum", "checksum_implemented", "command does not create checksum", "COMMAND_CREATES_CHECKSUM"),
        ("command_does_not_create_signature", "signature_implemented", "command does not create signature", "COMMAND_CREATES_SIGNATURE"),
        ("command_does_not_create_packet", "packet_implemented", "command does not create packet", "COMMAND_CREATES_PACKET"),
        ("command_does_not_create_transfer", "source_transferred", "command does not create transfer", "COMMAND_CREATES_TRANSFER"),
        ("command_does_not_create_migration", "source_migrated", "command does not create migration", "COMMAND_CREATES_MIGRATION"),
        ("command_does_not_create_source_receipt", "source_receipt_recorded", "command does not create source receipt", "COMMAND_CREATES_SOURCE_RECEIPT"),
        ("command_does_not_authorize_reception", "reception_authorized", "command does not authorize reception", "COMMAND_AUTHORIZES_RECEPTION"),
        ("command_does_not_create_deployment", "deployment_created", "command does not create deployment", "COMMAND_CREATES_DEPLOYMENT"),
        ("command_does_not_create_runtime_hosting", "runtime_hosting_created", "command does not create runtime hosting", "COMMAND_CREATES_RUNTIME_HOSTING"),
        ("command_does_not_create_public_release", "public_release_created", "command does not create public release", "COMMAND_CREATES_PUBLIC_RELEASE"),
        ("command_does_not_authorize_continuation", "continuation_authorized", "command does not authorize continuation", "COMMAND_AUTHORIZES_CONTINUATION"),
        ("command_does_not_create_reusable_permission", "reusable_permission_created", "command does not create reusable permission", "COMMAND_CREATES_REUSABLE_PERMISSION"),
        ("command_does_not_authorize_derivative_reception", "derivative_reception_authorized", "command does not authorize derivative reception", "COMMAND_AUTHORIZES_DERIVATIVE_RECEPTION"),
        ("command_does_not_authorize_vessel_relation", "vessel_relation_authorized", "command does not authorize vessel relation", "COMMAND_AUTHORIZES_VESSEL_RELATION"),
        ("command_does_not_authorize_another_source_body_reception_request", "another_reception_request_authorized", "command does not authorize another source-body reception request", "COMMAND_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
        ("command_does_not_authorize_follow_on_work", "follow_on_work_authorized", "command does not authorize follow-on work", "COMMAND_AUTHORIZES_FOLLOW_ON_WORK"),
        ("path_does_not_create_currentness", "path_created_currentness", "path does not create currentness", "PATH_TREATED_AS_CURRENTNESS"),
        ("latest_file_does_not_create_currentness", "latest_file_created_currentness", "latest file does not create currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
        ("artifact_existence_does_not_create_currentness", "artifact_existence_created_currentness", "artifact existence does not create currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
        ("repository_copy_does_not_become_body", "repository_copy_became_body", "repository copy does not become body", "REPOSITORY_COPY_TREATED_AS_BODY"),
        ("carrier_possession_does_not_create_currentness", "carrier_possession_created_currentness", "carrier possession does not create currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
        ("archive_possession_does_not_create_currentness", "archive_possession_created_currentness", "archive possession does not create currentness", "ARCHIVE_POSSESSION_TREATED_AS_CURRENTNESS"),
        ("command_success_does_not_create_currentness", "command_success_created_currentness", "command success does not create currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
        ("exit_code_does_not_create_currentness", "exit_code_created_currentness", "exit code does not create currentness", "EXIT_CODE_TREATED_AS_CURRENTNESS"),
        ("environment_state_does_not_create_authority_or_currentness", "environment_state_created_authority", "environment state does not create authority/currentness", "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS"),
        ("os_vendor_account_do_not_create_authority", "os_became_authority", "OS/vendor/account do not create authority", "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY"),
        ("narration_does_not_create_currentness", "narration_created_currentness", "narration does not create currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    )
    for check_name, key, expected, code in absence_checks:
        checks.append(
            _check(
                check_name,
                not _contains_truthy_key(request, key),
                expected,
                request.get(key),
                code,
            )
        )

    no_mutation = not any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS)
    checks.extend(
        [
            _check(
                "no_mutation_replay_merge",
                no_mutation,
                "no mutation/replay/merge",
                no_mutation,
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


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    request_malformed_code: str | None = None,
) -> dict[str, Any]:
    evidence_manifest_basis, evidence_manifest_basis_path, evidence_manifest_load_code = (
        _load_selected_evidence_manifest_basis(request)
    )
    portable_verification_basis, portable_verification_basis_path, portable_load_code = (
        _load_selected_portable_verification_basis(request)
    )
    selected_evidence_classes = _selected_evidence_classes(request, evidence_manifest_basis)
    selected_required_surfaces = _selected_required_surfaces(
        request, evidence_manifest_basis
    )
    selected_future_candidate_postures = _selected_future_candidate_postures(
        request, evidence_manifest_basis
    )
    checker_command_basis = request.get("checker_command_basis")
    command_limits = request.get("command_limits")
    command_dependency_on_evidence_manifest = _first_present(
        request.get("command_dependency_on_evidence_manifest"),
        _value_at(checker_command_basis, ("command_dependency_on_evidence_manifest",)),
        _value_at(command_limits, ("command_dependency_on_evidence_manifest",)),
    )
    no_command_authority_posture = _first_present(
        request.get("no_command_authority_posture"),
        _value_at(command_limits, ("no_command_authority_posture",)),
    )
    no_command_currentness_posture = _first_present(
        request.get("no_command_currentness_posture"),
        _value_at(command_limits, ("no_command_currentness_posture",)),
    )
    no_command_output_source_posture = _first_present(
        request.get("no_command_output_source_posture"),
        _value_at(command_limits, ("no_command_output_source_posture",)),
    )
    no_command_success_final_completion_posture = _first_present(
        request.get("no_command_success_final_completion_posture"),
        _value_at(command_limits, ("no_command_success_final_completion_posture",)),
    )
    non_execution_posture = _first_present(
        request.get("non_execution_posture"),
        _value_at(command_limits, ("non_execution_posture",)),
    )
    scope_values = _scope_values(request.get("command_scope"))

    block_code = request_malformed_code or _determine_block_code(
        request,
        evidence_manifest_basis,
        evidence_manifest_load_code,
        portable_verification_basis,
        portable_load_code,
        selected_evidence_classes,
        selected_required_surfaces,
        selected_future_candidate_postures,
        checker_command_basis,
        command_limits,
        command_dependency_on_evidence_manifest,
        no_command_authority_posture,
        no_command_currentness_posture,
        no_command_output_source_posture,
        no_command_success_final_completion_posture,
        non_execution_posture,
        scope_values,
    )

    requested_outcome = request.get("requested_command_boundary_outcome") or OUTCOME_RECORDED
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("command_boundary_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = requested_outcome
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED"

    checks = _build_checks(
        request,
        evidence_manifest_basis,
        portable_verification_basis,
        selected_evidence_classes,
        selected_required_surfaces,
        selected_future_candidate_postures,
        checker_command_basis,
        command_limits,
        command_dependency_on_evidence_manifest,
        no_command_authority_posture,
        no_command_currentness_posture,
        no_command_output_source_posture,
        no_command_success_final_completion_posture,
        non_execution_posture,
        scope_values,
    )
    if outcome == OUTCOME_BLOCKED and block_code is not None:
        matched = any(
            check.get("block_code") == block_code and check.get("passed") is False
            for check in checks
        )
        if not matched:
            checks.append(
                _check(
                    "command_boundary_review_blocked",
                    False,
                    "non-blocked command-boundary review",
                    block_code,
                    block_code,
                )
            )

    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    if outcome == OUTCOME_RECORDED and failed_count != 0:
        outcome = OUTCOME_BLOCKED
        block_code = block_code or "EVIDENCE_MANIFEST_BASIS_MISSING"

    evidence_manifest_basis_id = _first_present(
        request.get("selected_evidence_manifest_result_id"),
        _basis_id(evidence_manifest_basis),
    )
    evidence_manifest_basis_outcome = _first_present(
        request.get("selected_evidence_manifest_result_outcome"),
        _basis_outcome(evidence_manifest_basis),
    )
    evidence_manifest_basis_reference = _basis_reference(evidence_manifest_basis)
    portable_verification_basis_id = _first_present(
        request.get("selected_portable_verification_result_id"),
        _basis_id(portable_verification_basis),
    )
    portable_verification_basis_outcome = _first_present(
        request.get("selected_portable_verification_result_outcome"),
        _basis_outcome(portable_verification_basis),
    )
    portable_verification_basis_reference = _basis_reference(portable_verification_basis)
    result_id_seed = _first_present(
        request.get("command_boundary_request_id"),
        evidence_manifest_basis_id,
        portable_verification_basis_id,
    )
    result_id = (
        f"{_safe_component(result_id_seed)}"
        "__portable_source_body_verification_command_boundary_result"
    )
    recorded = outcome == OUTCOME_RECORDED
    non_claims = _build_non_claims(outcome)

    selected_evidence_manifest_basis_section = {
        "selected_evidence_manifest_result_id": evidence_manifest_basis_id,
        "selected_evidence_manifest_result_outcome": evidence_manifest_basis_outcome,
        "selected_evidence_manifest_result_path": evidence_manifest_basis_path
        or request.get("selected_evidence_manifest_result_path"),
        "selected_evidence_manifest_terminal_summary_path": request.get(
            "selected_evidence_manifest_terminal_summary_path"
        ),
        "selected_evidence_manifest_basis_reference": evidence_manifest_basis_reference,
        "evidence_manifest_recorded_posture": copy.deepcopy(
            request.get("evidence_manifest_recorded_posture")
        ),
        "evidence_manifest_terminal_summary_posture": copy.deepcopy(
            request.get("evidence_manifest_terminal_summary_posture")
        ),
        "evidence_manifest_remains_evidence_definition_only": True,
        "evidence_manifest_did_not_authorize_command_implementation": True,
        "evidence_manifest_did_not_authorize_command_execution": True,
        "evidence_manifest_did_not_create_manifest_checksum_signature_packet_command": True,
        "evidence_manifest_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
        "raw_selected_evidence_manifest_basis": copy.deepcopy(evidence_manifest_basis),
    }

    selected_portable_verification_basis_section = {
        "selected_portable_verification_result_id": portable_verification_basis_id,
        "selected_portable_verification_result_outcome": portable_verification_basis_outcome,
        "selected_portable_verification_result_path": portable_verification_basis_path
        or request.get("selected_portable_verification_result_path"),
        "selected_portable_verification_terminal_summary_path": request.get(
            "selected_portable_verification_terminal_summary_path"
        ),
        "selected_portable_verification_basis_reference": portable_verification_basis_reference,
        "portable_verification_remains_verification_only": True,
        "portable_verification_did_not_authorize_command_manifest_checksum_signature_packet_work": True,
        "portable_verification_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
        "raw_selected_portable_verification_basis": copy.deepcopy(
            portable_verification_basis
        ),
    }

    checker_command_basis_section = {
        "checker_command_basis_as_supplied": copy.deepcopy(checker_command_basis),
        "selected_evidence_classes": copy.deepcopy(selected_evidence_classes),
        "selected_required_surfaces": copy.deepcopy(selected_required_surfaces),
        "selected_future_candidate_postures": copy.deepcopy(
            selected_future_candidate_postures
        ),
        "command_candidate_is_future_only": True,
        "command_is_checker_only_if_separately_implemented": True,
        "command_requires_declared_evidence_manifest_basis": True,
        "command_implementation_requires_separate_boundary": True,
        "command_execution_remains_future": True,
        "command_output_remains_future": True,
        "command_success_remains_future": True,
        "command_cannot_create_source_authority_currentness_final_completion": True,
        "command_cannot_authorize_continuation_follow_on_work": True,
    }

    command_limits_section = {
        "command_limits_as_supplied": copy.deepcopy(command_limits),
        "command_dependency_on_evidence_manifest": copy.deepcopy(
            command_dependency_on_evidence_manifest
        ),
        "no_command_authority_posture": copy.deepcopy(no_command_authority_posture),
        "no_command_currentness_posture": copy.deepcopy(no_command_currentness_posture),
        "no_command_output_source_posture": copy.deepcopy(
            no_command_output_source_posture
        ),
        "no_command_success_final_completion_posture": copy.deepcopy(
            no_command_success_final_completion_posture
        ),
        "non_execution_posture": copy.deepcopy(non_execution_posture),
        "command_boundary_only": True,
        "command_is_not_implemented": True,
        "command_is_not_executed": True,
        "command_is_not_authorized_to_run": True,
        "command_output_is_not_source": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_is_not_authority": True,
        "command_does_not_create_manifest_checksum_signature_packet": True,
        "command_does_not_create_transfer_migration_source_receipt": True,
        "command_does_not_authorize_reception": True,
        "command_does_not_create_deployment_runtime_hosting_public_release": True,
        "command_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "path_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
    }

    command_scope_section = {
        "selected_command_scope_values": list(scope_values),
        "all_selected_scope_values_supported": all(
            value in SUPPORTED_COMMAND_BOUNDARY_SCOPE for value in scope_values
        ),
        "command_boundary_only": True,
        "command_checker_only_if_separately_implemented": True,
        "command_not_implemented": True,
        "command_not_executed": True,
        "command_output_not_source": True,
        "command_success_not_currentness": True,
        "command_success_not_final_completion": True,
        "command_not_authority": True,
        "command_not_manifest_checksum_signature_packet": True,
        "command_not_transfer_migration_source_receipt_reception_authorization": True,
        "command_not_deployment_runtime_hosting_public_release": True,
        "command_requires_evidence_manifest": True,
        "command_implementation_requires_separate_boundary": True,
        "path_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
    }

    command_boundary_statement = {
        "portable_source_body_verification_command_boundary_recorded": recorded,
        "verification_command_posture_declared": recorded,
        "verification_command_checker_role_bounded": recorded,
        "command_requires_declared_evidence_manifest": recorded,
        "selected_evidence_manifest_basis_preserved": recorded,
        "selected_portable_verification_basis_preserved": recorded,
        "checker_command_basis_declared": recorded,
        "command_limits_declared": recorded,
        "command_dependency_on_evidence_manifest_declared": recorded,
        "command_boundary_only": True,
        "command_is_checker_only_if_separately_implemented": True,
        "command_is_not_implemented": True,
        "command_is_not_executed": True,
        "command_is_not_authorized_to_run": True,
        "command_output_is_not_source": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_is_not_authority": True,
        "command_implementation_requires_separate_boundary": True,
        "command_boundary_recorded_as_implementation": False,
        "command_implemented": False,
        "command_executed": False,
        "command_authorized_to_run": False,
        "command_output_created": False,
        "command_output_became_source": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "command_became_authority": False,
        "manifest_implemented": False,
        "checksum_implemented": False,
        "signature_implemented": False,
        "packet_implemented": False,
        "source_transferred": False,
        "source_migrated": False,
        "source_received": False,
        "source_receipt_recorded": False,
        "reception_authorized": False,
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
        "recorded_true_fields_are_bounded_command_boundary_outcomes_only": True,
    }

    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": copy.deepcopy(request.get("additional_basis_context"))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }

    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": copy.deepcopy(request.get("not_recorded_basis"))
        if outcome == OUTCOME_NOT_RECORDED
        else {},
        "failed_checks": copy.deepcopy(
            [check for check in checks if check.get("passed") is not True]
        )
        if outcome == OUTCOME_NOT_RECORDED
        else [],
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_authorize": True,
        "not_recorded_does_not_implement": True,
        "not_recorded_does_not_execute": True,
        "not_recorded_does_not_emit_output": True,
        "not_recorded_does_not_receive": True,
        "not_recorded_does_not_transfer": True,
        "not_recorded_does_not_migrate": True,
        "not_recorded_does_not_deploy": True,
        "not_recorded_does_not_publish": True,
        "not_recorded_does_not_host": True,
        "not_recorded_does_not_currentize": True,
        "not_recorded_does_not_adopt": True,
        "not_recorded_does_not_continue": True,
        "not_recorded_does_not_create_reusable_permission": True,
        "not_recorded_does_not_authorize_derivative_reception": True,
        "not_recorded_does_not_authorize_vessel_relation": True,
        "not_recorded_does_not_authorize_another_reception_request": True,
        "not_recorded_does_not_authorize_follow_on_work": True,
    }

    declared_question_section = {
        "command_boundary_request_id": request.get("command_boundary_request_id"),
        "command_boundary_question": request.get("command_boundary_question"),
        "command_boundary_intent": request.get("command_boundary_intent"),
        "declared_request_path": request_path,
        "selected_evidence_manifest_result_id": evidence_manifest_basis_id,
        "selected_evidence_manifest_result_outcome": evidence_manifest_basis_outcome,
        "selected_evidence_manifest_result_path": evidence_manifest_basis_path
        or request.get("selected_evidence_manifest_result_path"),
        "selected_evidence_manifest_terminal_summary_path": request.get(
            "selected_evidence_manifest_terminal_summary_path"
        ),
        "selected_portable_verification_result_id": portable_verification_basis_id,
        "selected_portable_verification_result_outcome": portable_verification_basis_outcome,
        "selected_portable_verification_result_path": portable_verification_basis_path
        or request.get("selected_portable_verification_result_path"),
        "selected_portable_verification_terminal_summary_path": request.get(
            "selected_portable_verification_terminal_summary_path"
        ),
        "command_boundary_is_not_command_implementation": True,
        "command_boundary_is_not_command_execution": True,
        "command_boundary_is_not_command_output": True,
        "command_boundary_is_not_source": True,
        "command_boundary_is_not_authority": True,
        "command_boundary_is_not_currentness": True,
        "command_requires_evidence_manifest": True,
        "command_implementation_requires_separate_boundary": True,
    }

    result = {
        "portable_source_body_verification_command_boundary_metadata": {
            "portable_source_body_verification_command_boundary_result_id": result_id,
            "portable_source_body_verification_command_boundary_result_type": (
                "portable_source_body_verification_command_boundary_result"
            ),
            "portable_source_body_verification_command_boundary_result_version": (
                RESULT_VERSION
            ),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_command_boundary_question": declared_question_section,
        "selected_evidence_manifest_basis": selected_evidence_manifest_basis_section,
        "selected_portable_verification_basis": selected_portable_verification_basis_section,
        "checker_command_basis": checker_command_basis_section,
        "command_limits": command_limits_section,
        "command_scope": command_scope_section,
        "command_boundary_checks": checks,
        "command_boundary_statement": command_boundary_statement,
        "command_boundary_non_meaning": _build_command_boundary_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(
            block_code if outcome == OUTCOME_BLOCKED else None,
            request.get("block_reason") or block_code,
        ),
    }
    result["portable_source_body_verification_command_boundary_summary"] = (
        build_portable_source_body_verification_command_boundary_summary(result)
    )
    return result


def _malformed_request_result(
    code: str, reason: str, request_path: str | None = None
) -> dict[str, Any]:
    request = {
        "command_boundary_request_id": None,
        "command_boundary_question": None,
        "command_boundary_intent": None,
        "declared_non_claims": {},
    }
    result = _build_result(
        request,
        request_path=request_path,
        request_malformed_code=code,
    )
    result["block"]["block_reason"] = reason
    return result


def resolve_portable_source_body_verification_command_boundary(
    declared_command_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve a declared portable verification command-boundary request."""
    if declared_command_boundary_request is None:
        return _build_result({})
    if not isinstance(declared_command_boundary_request, Mapping):
        return _malformed_request_result(
            "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
            "declared command-boundary request must be a JSON object / mapping",
        )
    return _build_result(copy.deepcopy(dict(declared_command_boundary_request)))


def resolve_portable_source_body_verification_command_boundary_from_path(
    declared_command_boundary_request_path: Path | str,
) -> dict:
    """Resolve a declared command-boundary request read from a JSON object path."""
    path = Path(declared_command_boundary_request_path)
    payload, failure = _read_json_object(path)
    if failure == "unreadable":
        return _malformed_request_result(
            "DECLARED_COMMAND_BOUNDARY_REQUEST_UNREADABLE",
            "declared command-boundary request path is unreadable",
            str(path),
        )
    if failure == "malformed":
        return _malformed_request_result(
            "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
            "declared command-boundary request path is malformed or not a JSON object",
            str(path),
        )
    if payload is None:
        return _malformed_request_result(
            "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
            "declared command-boundary request path did not produce a JSON object",
            str(path),
        )
    return _build_result(payload, request_path=str(path))


def build_portable_source_body_verification_command_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from a command-boundary result."""
    checks = result.get("command_boundary_checks", [])
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    question = result.get("declared_command_boundary_question", {})
    statement = result.get("command_boundary_statement", {})
    selected_evidence_manifest = result.get("selected_evidence_manifest_basis", {})
    selected_portable = result.get("selected_portable_verification_basis", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block", {})
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "command_boundary_request_id": question.get("command_boundary_request_id"),
        "command_boundary_question": question.get("command_boundary_question"),
        "command_boundary_intent": question.get("command_boundary_intent"),
        "selected_evidence_manifest_result_id": selected_evidence_manifest.get(
            "selected_evidence_manifest_result_id"
        ),
        "selected_evidence_manifest_result_outcome": selected_evidence_manifest.get(
            "selected_evidence_manifest_result_outcome"
        ),
        "selected_evidence_manifest_result_path": selected_evidence_manifest.get(
            "selected_evidence_manifest_result_path"
        ),
        "selected_evidence_manifest_terminal_summary_path": selected_evidence_manifest.get(
            "selected_evidence_manifest_terminal_summary_path"
        ),
        "selected_portable_verification_result_id": selected_portable.get(
            "selected_portable_verification_result_id"
        ),
        "selected_portable_verification_result_outcome": selected_portable.get(
            "selected_portable_verification_result_outcome"
        ),
        "selected_portable_verification_result_path": selected_portable.get(
            "selected_portable_verification_result_path"
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "portable_source_body_verification_command_boundary_recorded": statement.get(
            "portable_source_body_verification_command_boundary_recorded", False
        ),
        "verification_command_posture_declared": statement.get(
            "verification_command_posture_declared", False
        ),
        "verification_command_checker_role_bounded": statement.get(
            "verification_command_checker_role_bounded", False
        ),
        "command_requires_declared_evidence_manifest": statement.get(
            "command_requires_declared_evidence_manifest", False
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_evidence_manifest_basis_preserved": statement.get(
            "selected_evidence_manifest_basis_preserved", False
        ),
        "selected_portable_verification_basis_preserved": statement.get(
            "selected_portable_verification_basis_preserved", False
        ),
        "checker_command_basis_declared": statement.get(
            "checker_command_basis_declared", False
        ),
        "command_limits_declared": statement.get("command_limits_declared", False),
        "command_dependency_on_evidence_manifest_declared": statement.get(
            "command_dependency_on_evidence_manifest_declared", False
        ),
        "command_boundary_only": statement.get("command_boundary_only", True),
        "command_checker_only_if_separately_implemented": statement.get(
            "command_is_checker_only_if_separately_implemented", True
        ),
        "command_not_implemented": statement.get("command_is_not_implemented", True),
        "command_not_executed": statement.get("command_is_not_executed", True),
        "command_not_authorized_to_run": statement.get(
            "command_is_not_authorized_to_run", True
        ),
        "command_output_not_created": non_claims.get("command_output_created") is False,
        "command_output_not_source": statement.get("command_output_is_not_source", True),
        "command_success_not_currentness": statement.get(
            "command_success_is_not_currentness", True
        ),
        "command_success_not_final_completion": statement.get(
            "command_success_is_not_final_completion", True
        ),
        "command_not_authority": statement.get("command_is_not_authority", True),
        "command_implementation_requires_separate_boundary": statement.get(
            "command_implementation_requires_separate_boundary", True
        ),
        "no_manifest_checksum_signature_packet_implemented": all(
            non_claims.get(key) is False
            for key in (
                "manifest_implemented",
                "checksum_implemented",
                "signature_implemented",
                "packet_implemented",
            )
        ),
        "no_source_transferred_migrated_received_receipted": all(
            non_claims.get(key) is False
            for key in (
                "source_transferred",
                "source_migrated",
                "source_received",
                "source_receipt_recorded",
            )
        ),
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
            for key in REQUIRED_FALSE_NON_CLAIMS + ALLOWED_RECORDED_TRUE_FIELDS
        },
    }


def _deduplicated_output_path(path: Path) -> Path:
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


def write_portable_source_body_verification_command_boundary_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one additive command-boundary result artifact as UTF-8 JSON."""
    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandBoundaryError(
            "command-boundary result must be a mapping"
        )
    if output_path is None:
        summary = result.get("portable_source_body_verification_command_boundary_summary", {})
        metadata = result.get("portable_source_body_verification_command_boundary_metadata", {})
        seed = _first_present(
            summary.get("command_boundary_request_id"),
            summary.get("selected_evidence_manifest_result_id"),
            metadata.get("portable_source_body_verification_command_boundary_result_id"),
        )
        filename = (
            f"{_safe_component(seed)}"
            "__portable_source_body_verification_command_boundary_result.json"
        )
        target = PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _deduplicated_output_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def _basis_from_value(value: Mapping[str, Any] | str, key: str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        key: value,
        "basis_reference": value,
        "basis_is_reference_only": True,
    }


def _checker_command_basis_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "checker_command_basis_reference": value,
        "command_candidate_is_future_only": True,
        "command_is_checker_only_if_separately_implemented": True,
        "command_requires_declared_evidence_manifest_basis": True,
        "command_implementation_requires_separate_boundary": True,
        "command_execution_remains_future": True,
        "command_output_remains_future": True,
        "command_success_remains_future": True,
    }


def _command_limits_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        limits = copy.deepcopy(dict(value))
    else:
        limits = {"command_limits_reference": value}
    limits.setdefault(
        "command_dependency_on_evidence_manifest",
        {"command_requires_declared_evidence_manifest": True},
    )
    limits.setdefault(
        "no_command_authority_posture",
        {"command_does_not_become_authority": True},
    )
    limits.setdefault(
        "no_command_currentness_posture",
        {"command_success_does_not_create_currentness": True},
    )
    limits.setdefault(
        "no_command_output_source_posture",
        {"command_output_does_not_become_source": True},
    )
    limits.setdefault(
        "no_command_success_final_completion_posture",
        {"command_success_does_not_claim_final_completion": True},
    )
    limits.setdefault("non_execution_posture", {"command_is_not_executed": True})
    limits.update(
        {
            "command_boundary_only": True,
            "command_is_not_implemented": True,
            "command_is_not_executed": True,
            "command_is_not_authorized_to_run": True,
            "command_output_is_not_source": True,
            "command_success_is_not_currentness": True,
            "command_success_is_not_final_completion": True,
            "command_is_not_authority": True,
            "path_does_not_create_currentness": True,
            "artifact_existence_does_not_create_currentness": True,
            "repository_copy_does_not_become_body": True,
        }
    )
    return limits


def _evidence_classes_from_basis(value: Mapping[str, Any]) -> Any:
    return _first_present(
        value.get("selected_evidence_classes"),
        _value_at(value, ("declared_evidence_classes",)),
        _value_at(value, ("declared_evidence_classes", "declared_evidence_classes_as_supplied")),
        _value_at(value, ("declared_evidence_classes", "declared_evidence_classes_representative")),
        [
            "required_source_surfaces",
            "required_spec_surfaces",
            "required_resolver_surfaces",
            "required_test_surfaces",
            "required_artifact_roots",
            "required_closure_artifacts",
            "required_terminal_summaries",
            "future_command_candidate",
        ],
    )


def _required_surfaces_from_basis(value: Mapping[str, Any]) -> Any:
    return _first_present(
        value.get("selected_required_surfaces"),
        value.get("required_surfaces"),
        {
            "required_source_surfaces": ["declared by command-boundary helper"],
            "required_spec_surfaces": ["declared by command-boundary helper"],
            "required_resolver_surfaces": ["declared by command-boundary helper"],
            "required_test_surfaces": ["declared by command-boundary helper"],
            "required_artifact_roots": ["declared by command-boundary helper"],
            "required_closure_artifacts": ["declared by command-boundary helper"],
        },
    )


def _future_candidate_postures_from_basis(value: Mapping[str, Any]) -> Any:
    return _first_present(
        value.get("selected_future_candidate_postures"),
        value.get("future_candidate_postures"),
        {
            "manifest_candidate_future_only": True,
            "checksum_candidate_future_only": True,
            "signature_candidate_future_only": True,
            "packet_candidate_future_only": True,
            "command_candidate_future_only": True,
            "command_not_implemented": True,
            "command_not_authorized": True,
            "command_requires_separate_boundary": True,
        },
    )


def build_declared_portable_source_body_verification_command_boundary_request(
    command_boundary_request_id: str,
    command_boundary_question: str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    checker_command_basis: Mapping[str, Any] | str,
    command_limits: Mapping[str, Any] | str,
    command_scope: Sequence[str] | Mapping[str, Any],
    command_boundary_intent: str = INTENT_RECORD,
    *,
    selected_evidence_manifest_result_path: str | None = None,
    selected_evidence_manifest_result_id: str | None = None,
    selected_evidence_manifest_result_outcome: str | None = None,
    requested_command_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded declared command-boundary request."""
    selected_evidence = _basis_from_value(
        selected_evidence_manifest_basis,
        "selected_evidence_manifest_basis_reference",
    )
    selected_portable = _basis_from_value(
        selected_portable_verification_basis,
        "selected_portable_verification_basis_reference",
    )
    checker_basis = _checker_command_basis_from_value(checker_command_basis)
    limits = _command_limits_from_value(command_limits)

    request = {
        "command_boundary_request_id": command_boundary_request_id,
        "command_boundary_question": command_boundary_question,
        "command_boundary_intent": command_boundary_intent,
        "selected_evidence_manifest_basis": copy.deepcopy(selected_evidence),
        "selected_portable_verification_basis": copy.deepcopy(selected_portable),
        "selected_evidence_classes": copy.deepcopy(
            _evidence_classes_from_basis(selected_evidence)
        ),
        "selected_required_surfaces": copy.deepcopy(
            _required_surfaces_from_basis(selected_evidence)
        ),
        "selected_future_candidate_postures": copy.deepcopy(
            _future_candidate_postures_from_basis(selected_evidence)
        ),
        "checker_command_basis": checker_basis,
        "command_limits": limits,
        "command_dependency_on_evidence_manifest": copy.deepcopy(
            limits.get("command_dependency_on_evidence_manifest")
        ),
        "no_command_authority_posture": copy.deepcopy(
            limits.get("no_command_authority_posture")
        ),
        "no_command_currentness_posture": copy.deepcopy(
            limits.get("no_command_currentness_posture")
        ),
        "no_command_output_source_posture": copy.deepcopy(
            limits.get("no_command_output_source_posture")
        ),
        "no_command_success_final_completion_posture": copy.deepcopy(
            limits.get("no_command_success_final_completion_posture")
        ),
        "non_execution_posture": copy.deepcopy(limits.get("non_execution_posture")),
        "command_scope": copy.deepcopy(command_scope),
        "selected_evidence_manifest_result_path": selected_evidence_manifest_result_path,
        "selected_evidence_manifest_result_id": selected_evidence_manifest_result_id,
        "selected_evidence_manifest_result_outcome": selected_evidence_manifest_result_outcome,
        "requested_command_boundary_outcome": requested_command_boundary_outcome,
        "additional_basis_context": copy.deepcopy(additional_basis_context or {}),
        "not_recorded_basis": copy.deepcopy(not_recorded_basis),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    return request
