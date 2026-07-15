"""Resolve the portable source-body verification evidence-manifest boundary.

This resolver answers one question only:

    Can the evidence basis required for future portable source-body
    verification checks be bounded and recorded without implementing manifest,
    checksum, signature, packet, command, runtime, deployment, public release,
    transfer, migration, source receipt, authority, currentness,
    continuation, reusable permission, derivative reception, vessel relation,
    another reception request, or follow-on work?

Evidence-manifest boundary records declared evidence classes only. It is not a
manifest implementation, command implementation, checksum implementation,
signature implementation, packet implementation, source-body transfer,
migration, source receipt, reception authorization, deployment, runtime
hosting, public release, authority, currentness, final completion,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on authorization.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationEvidenceManifestBoundaryError(Exception):
    """Raised for hard evidence-manifest boundary failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_evidence_manifest_boundary"
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "evidence_manifest_boundary"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_REVIEW"
SUPPORTED_EVIDENCE_MANIFEST_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_EVIDENCE_MANIFEST_SCOPE = {
    "EVIDENCE_MANIFEST_BOUNDARY_ONLY",
    "EVIDENCE_MANIFEST_IS_NOT_MANIFEST_IMPLEMENTATION",
    "EVIDENCE_MANIFEST_IS_NOT_COMMAND",
    "EVIDENCE_MANIFEST_IS_NOT_CHECKSUM",
    "EVIDENCE_MANIFEST_IS_NOT_SIGNATURE",
    "EVIDENCE_MANIFEST_IS_NOT_PACKET",
    "EVIDENCE_MANIFEST_IS_NOT_TRANSFER",
    "EVIDENCE_MANIFEST_IS_NOT_MIGRATION",
    "EVIDENCE_MANIFEST_IS_NOT_SOURCE_RECEIPT",
    "EVIDENCE_MANIFEST_IS_NOT_RECEPTION_AUTHORIZATION",
    "EVIDENCE_MANIFEST_IS_NOT_DEPLOYMENT",
    "EVIDENCE_MANIFEST_IS_NOT_RUNTIME_HOSTING",
    "EVIDENCE_MANIFEST_IS_NOT_PUBLIC_RELEASE",
    "EVIDENCE_DOES_NOT_BECOME_SOURCE",
    "EVIDENCE_DOES_NOT_CREATE_AUTHORITY",
    "EVIDENCE_DOES_NOT_CREATE_CURRENTNESS",
    "PATH_DOES_NOT_CREATE_CURRENTNESS",
    "LATEST_FILE_DOES_NOT_CREATE_CURRENTNESS",
    "ARTIFACT_EXISTENCE_DOES_NOT_CREATE_CURRENTNESS",
    "REPOSITORY_COPY_DOES_NOT_BECOME_BODY",
    "COMMAND_REQUIRES_SEPARATE_BOUNDARY",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "evidence_became_source",
    "evidence_became_authority",
    "evidence_created_currentness",
    "manifest_implemented",
    "checksum_implemented",
    "signature_implemented",
    "packet_implemented",
    "command_implemented",
    "command_authorized",
    "path_created_currentness",
    "latest_file_created_currentness",
    "artifact_existence_created_currentness",
    "repository_copy_became_body",
    "carrier_possession_created_currentness",
    "narration_created_currentness",
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
            "source_receipt_created",
            "authority_created",
            "currentness_created",
            "adoption_created",
            "standing_created",
            "public_readiness_created",
            "manifest_file_created",
            "checksum_file_created",
            "signature_file_created",
            "source_body_packet_created",
            "verification_command_created",
            "command_invocation_created",
            "command_output_created",
            "reproducible_environment_created",
        )
    )
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "portable_source_body_verification_evidence_manifest_recorded",
    "evidence_manifest_basis_declared",
    "required_verification_evidence_classes_declared",
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = (
    ("evidence_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("evidence_treated_as_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("evidence_is_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("manifest_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("checksum_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("signature_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("packet_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("command_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
    ("evidence_became_authority", "EVIDENCE_TREATED_AS_AUTHORITY"),
    ("evidence_treated_as_authority", "EVIDENCE_TREATED_AS_AUTHORITY"),
    ("evidence_created_authority", "EVIDENCE_TREATED_AS_AUTHORITY"),
    ("evidence_created_currentness", "EVIDENCE_TREATED_AS_CURRENTNESS"),
    ("evidence_became_currentness", "EVIDENCE_TREATED_AS_CURRENTNESS"),
    ("evidence_treated_as_currentness", "EVIDENCE_TREATED_AS_CURRENTNESS"),
    ("manifest_implemented", "MANIFEST_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    (
        "manifest_candidate_implemented",
        "MANIFEST_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    (
        "manifest_candidate_treated_as_implementation",
        "MANIFEST_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    ("checksum_implemented", "CHECKSUM_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    (
        "checksum_candidate_treated_as_implementation",
        "CHECKSUM_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    ("signature_implemented", "SIGNATURE_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    (
        "signature_candidate_treated_as_implementation",
        "SIGNATURE_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    ("packet_implemented", "PACKET_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    ("source_body_packet_implemented", "PACKET_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    (
        "packet_candidate_treated_as_implementation",
        "PACKET_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    ("command_implemented", "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    ("command_authorized", "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
    (
        "command_candidate_treated_as_implementation",
        "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION",
    ),
    ("path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("local_path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("path_treated_as_currentness", "PATH_TREATED_AS_CURRENTNESS"),
    ("latest_file_created_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    ("latest_file_treated_as_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
    (
        "artifact_existence_created_currentness",
        "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
    ),
    (
        "artifact_existence_treated_as_currentness",
        "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
    ),
    ("repository_copy_became_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    ("repository_copy_treated_as_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
    (
        "carrier_possession_created_currentness",
        "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS",
    ),
    (
        "archive_possession_created_currentness",
        "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS",
    ),
    ("narration_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    ("narrator_trust_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
    ("source_transferred", "EVIDENCE_REVIEW_CREATES_TRANSFER"),
    ("source_body_transferred", "EVIDENCE_REVIEW_CREATES_TRANSFER"),
    ("source_migrated", "EVIDENCE_REVIEW_CREATES_MIGRATION"),
    ("source_body_migrated", "EVIDENCE_REVIEW_CREATES_MIGRATION"),
    ("source_received", "EVIDENCE_REVIEW_CREATES_SOURCE_RECEIPT"),
    ("source_receipt_recorded", "EVIDENCE_REVIEW_CREATES_SOURCE_RECEIPT"),
    ("source_receipt_created", "EVIDENCE_REVIEW_CREATES_SOURCE_RECEIPT"),
    ("reception_authorized", "EVIDENCE_REVIEW_AUTHORIZES_RECEPTION"),
    ("deployment_created", "EVIDENCE_REVIEW_CREATES_DEPLOYMENT"),
    ("runtime_hosting_created", "EVIDENCE_REVIEW_CREATES_RUNTIME_HOSTING"),
    ("public_release_created", "EVIDENCE_REVIEW_CREATES_PUBLIC_RELEASE"),
    ("operation_permission_created", "EVIDENCE_REVIEW_CREATES_OPERATION_PERMISSION"),
    (
        "public_launch_readiness_created",
        "EVIDENCE_REVIEW_CREATES_PUBLIC_READINESS",
    ),
    ("public_readiness_created", "EVIDENCE_REVIEW_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "EVIDENCE_REVIEW_CLAIMS_FINAL_COMPLETION"),
    ("continuation_authorized", "EVIDENCE_REVIEW_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "EVIDENCE_REVIEW_OPENS_PUBLICATION_FLOW"),
    ("reusable_permission_created", "EVIDENCE_REVIEW_CREATES_REUSABLE_PERMISSION"),
    (
        "derivative_reception_authorized",
        "EVIDENCE_REVIEW_AUTHORIZES_DERIVATIVE_RECEPTION",
    ),
    ("vessel_relation_authorized", "EVIDENCE_REVIEW_AUTHORIZES_VESSEL_RELATION"),
    (
        "another_reception_request_authorized",
        "EVIDENCE_REVIEW_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
    ),
    ("follow_on_work_authorized", "EVIDENCE_REVIEW_AUTHORIZES_FOLLOW_ON_WORK"),
    ("adoption_created", "EVIDENCE_REVIEW_CREATES_ADOPTION"),
    ("authority_created", "EVIDENCE_TREATED_AS_AUTHORITY"),
    ("currentness_created", "EVIDENCE_TREATED_AS_CURRENTNESS"),
    ("standing_created", "EVIDENCE_REVIEW_CREATES_STANDING"),
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
            "current",
            "source",
            "authority",
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
    return basis, path, failure


def _load_selected_source_body_basis(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    return _load_json_basis(
        request,
        value_key="selected_source_body_basis",
        path_key="selected_source_body_basis_path",
        reference_key="selected_source_body_basis_reference",
        unreadable_code="SELECTED_SOURCE_BODY_BASIS_UNREADABLE",
        malformed_code="SELECTED_SOURCE_BODY_BASIS_MALFORMED",
    )


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = _first_present(
            scope.get("selected_evidence_manifest_scope_values"),
            scope.get("evidence_manifest_scope_values"),
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
    text = str(value or "portable_source_body_verification_evidence_manifest").strip()
    cleaned = "".join(
        character if character.isalnum() or character in ("-", "_") else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "portable_source_body_verification_evidence_manifest"


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


def _surface_value(request: Mapping[str, Any], key: str) -> Any:
    surfaces = request.get("required_surfaces")
    return _first_present(
        request.get(key),
        _value_at(surfaces, (key,)),
        _value_at(surfaces, (key.removeprefix("required_"),)),
    )


def _basis_id(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("portable_source_body_verification_result_id"),
            basis.get("selected_portable_verification_result_id"),
            basis.get("selected_portable_verification_basis_id"),
            basis.get("source_body_basis_id"),
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
            basis.get("selected_portable_verification_basis_reference"),
            basis.get("selected_source_body_basis_reference"),
            basis.get("reference"),
            basis.get("path"),
            basis.get("basis_reference"),
        ]
    )
    return _first_present(*candidates)


def _declared_classes_list(value: Any) -> list[Any]:
    if isinstance(value, Mapping):
        values = _first_present(
            value.get("evidence_classes"),
            value.get("declared_evidence_classes"),
            value.get("classes"),
        )
        if values is None:
            return list(value.keys())
        if isinstance(values, Sequence) and not isinstance(values, (str, bytes)):
            return list(values)
        return [values]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return list(value)
    if _present(value):
        return [value]
    return []


def _selected_source_body_terminal_summary(
    request: Mapping[str, Any], source_body_basis: Mapping[str, Any] | None
) -> Any:
    supplied = _first_present(
        request.get("selected_source_body_reception_terminal_summary"),
        _value_at(source_body_basis, ("selected_source_body_reception_terminal_summary",)),
        _value_at(source_body_basis, ("selected_source_body_reception_terminal_summary_basis",)),
        _value_at(source_body_basis, ("selected_terminal_summary_basis",)),
    )
    basis = _normalize_basis(supplied, "selected_source_body_reception_terminal_summary_reference")
    path_value = request.get("selected_source_body_reception_terminal_summary_path")
    if _present(path_value):
        if basis is None:
            basis = {}
        basis["selected_source_body_reception_terminal_summary_path"] = str(path_value)
        basis["selected_source_body_reception_terminal_summary_path_metadata"] = (
            _text_path_metadata(str(path_value))
        )
        basis["terminal_summary_path_is_evidence_only"] = True
        basis["terminal_summary_path_does_not_create_currentness"] = True
    return basis


def _selected_source_body_reception_closure_basis(
    request: Mapping[str, Any], source_body_basis: Mapping[str, Any] | None
) -> Any:
    return _first_present(
        request.get("selected_source_body_reception_closure_basis"),
        _value_at(source_body_basis, ("selected_source_body_reception_closure_basis",)),
        _value_at(source_body_basis, ("selected_reception_closure_basis",)),
    )


def _distributed_operation_basis(request: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("selected_distributed_operation_terminal_basis"),
        request.get("selected_distributed_operation_terminal_summary"),
        request.get("selected_distributed_operation_closure_basis"),
    )


def _current_body_basis(request: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("selected_current_body_basis"),
        request.get("selected_current_body_conformance_basis"),
        request.get("selected_current_self_orientation_basis"),
    )


def _requires_basis(request: Mapping[str, Any], *keys: str) -> bool:
    return any(_truthy(request.get(key)) for key in keys)


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
            "even_when_evidence_manifest_recorded_no_manifest_exists": True,
            "even_when_evidence_manifest_recorded_no_command_exists": True,
            "even_when_evidence_manifest_recorded_no_checksum_signature_or_packet_exists": True,
            "even_when_evidence_manifest_recorded_evidence_does_not_become_source_authority_currentness_permission_deployment_public_release_final_completion_or_continuation": True,
            "even_when_evidence_manifest_recorded_no_source_transfer_migration_receipt_reception_authorization_operation_permission_public_readiness_reusable_permission_derivative_reception_vessel_relation_another_reception_request_or_follow_on_work_is_authorized": True,
        }
    )
    return non_claims


def _build_evidence_manifest_non_meaning() -> dict[str, bool]:
    names = (
        "manifest_exists",
        "checksum_exists",
        "signature_exists",
        "packet_exists",
        "command_exists",
        "source_transferred",
        "source_migrated",
        "source_received",
        "source_receipt_recorded",
        "reception_authorized",
        "carrier_became_source",
        "evidence_became_source",
        "artifact_existence_became_currentness",
        "repository_copy_became_body",
        "local_path_became_currentness",
        "latest_file_became_currentness",
        "runtime_hosting_created",
        "deployment_created",
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
    return {f"evidence_manifest_does_not_mean_{name}": True for name in names}


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "portable source-body verification evidence-manifest test",
            "portable source-body verification evidence-manifest live artifact",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "portable verification command boundary",
            "portable verification command implementation",
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
    portable_verification_basis: Mapping[str, Any] | None,
    portable_verification_basis_load_code: str | None,
    source_body_basis: Mapping[str, Any] | None,
    source_body_basis_load_code: str | None,
    source_body_reception_terminal_summary: Any,
    source_body_reception_closure_basis: Any,
    distributed_operation_basis: Any,
    current_body_basis: Any,
    declared_evidence_classes: Any,
    required_source_surfaces: Any,
    required_spec_surfaces: Any,
    required_resolver_surfaces: Any,
    required_test_surfaces: Any,
    required_artifact_roots: Any,
    required_closure_artifacts: Any,
    required_terminal_summaries: Any,
    evidence_only_posture: Any,
    future_candidate_postures: Any,
    scope_values: Sequence[str],
) -> str | None:
    if not _present(request.get("evidence_manifest_question")):
        return "EVIDENCE_MANIFEST_QUESTION_UNDECLARED"
    intent = request.get("evidence_manifest_intent")
    if intent == INTENT_BLOCK:
        return "EVIDENCE_MANIFEST_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_EVIDENCE_MANIFEST_INTENTS:
        return "EVIDENCE_MANIFEST_INTENT_UNSUPPORTED"
    for load_code in (portable_verification_basis_load_code, source_body_basis_load_code):
        if load_code is not None:
            return load_code
    if portable_verification_basis is None:
        return "PORTABLE_VERIFICATION_BASIS_MISSING"
    if source_body_basis is None:
        return "SELECTED_SOURCE_BODY_BASIS_MISSING"
    if not _present(source_body_reception_terminal_summary):
        return "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING"
    if not _present(source_body_reception_closure_basis):
        return "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING"
    if _requires_basis(
        request,
        "distributed_operation_basis_required",
        "selected_distributed_operation_basis_required",
    ) and not _present(distributed_operation_basis):
        return "DISTRIBUTED_OPERATION_BASIS_MISSING"
    if _requires_basis(
        request,
        "current_body_basis_required",
        "selected_current_body_basis_required",
    ) and not _present(current_body_basis):
        return "CURRENT_BODY_BASIS_MISSING"
    if not _present(declared_evidence_classes):
        return "DECLARED_EVIDENCE_CLASSES_MISSING"
    if not _present(required_source_surfaces):
        return "REQUIRED_SOURCE_SURFACES_MISSING"
    if not _present(required_spec_surfaces):
        return "REQUIRED_SPEC_SURFACES_MISSING"
    if not _present(required_resolver_surfaces):
        return "REQUIRED_RESOLVER_SURFACES_MISSING"
    if not _present(required_test_surfaces):
        return "REQUIRED_TEST_SURFACES_MISSING"
    if not _present(required_artifact_roots):
        return "REQUIRED_ARTIFACT_ROOTS_MISSING"
    if not _present(required_closure_artifacts):
        return "REQUIRED_CLOSURE_ARTIFACTS_MISSING"
    if not _present(required_terminal_summaries):
        return "REQUIRED_TERMINAL_SUMMARIES_MISSING"
    if not _present(evidence_only_posture):
        return "EVIDENCE_ONLY_POSTURE_MISSING"
    if not _present(future_candidate_postures):
        return "FUTURE_CANDIDATE_POSTURE_MISSING"
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_EVIDENCE_MANIFEST_SCOPE
    ]
    if unsupported_scope:
        return "UNSUPPORTED_EVIDENCE_MANIFEST_SCOPE"
    collapse = _collapse_code(request)
    if collapse is not None:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    portable_verification_basis: Mapping[str, Any] | None,
    source_body_basis: Mapping[str, Any] | None,
    source_body_reception_terminal_summary: Any,
    source_body_reception_closure_basis: Any,
    distributed_operation_basis: Any,
    current_body_basis: Any,
    declared_evidence_classes: Any,
    required_source_surfaces: Any,
    required_spec_surfaces: Any,
    required_resolver_surfaces: Any,
    required_test_surfaces: Any,
    required_artifact_roots: Any,
    required_closure_artifacts: Any,
    required_terminal_summaries: Any,
    evidence_only_posture: Any,
    future_candidate_postures: Any,
    scope_values: Sequence[str],
) -> list[dict[str, Any]]:
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_EVIDENCE_MANIFEST_SCOPE
    ]
    checks = [
        _check(
            "evidence_manifest_question_declared",
            _present(request.get("evidence_manifest_question")),
            "declared evidence-manifest question",
            request.get("evidence_manifest_question"),
            "EVIDENCE_MANIFEST_QUESTION_UNDECLARED",
        ),
        _check(
            "evidence_manifest_intent_supported",
            request.get("evidence_manifest_intent")
            in SUPPORTED_EVIDENCE_MANIFEST_INTENTS
            and request.get("evidence_manifest_intent") != INTENT_BLOCK,
            sorted(SUPPORTED_EVIDENCE_MANIFEST_INTENTS - {INTENT_BLOCK}),
            request.get("evidence_manifest_intent"),
            "EVIDENCE_MANIFEST_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_portable_verification_result_or_terminal_summary_declared",
            portable_verification_basis is not None,
            "selected portable verification result or terminal summary declared",
            portable_verification_basis is not None,
            "PORTABLE_VERIFICATION_BASIS_MISSING",
        ),
        _check(
            "selected_source_body_basis_declared",
            source_body_basis is not None,
            "selected source-body basis declared",
            source_body_basis is not None,
            "SELECTED_SOURCE_BODY_BASIS_MISSING",
        ),
        _check(
            "selected_source_body_reception_terminal_summary_declared",
            _present(source_body_reception_terminal_summary),
            "selected source-body reception terminal summary declared",
            source_body_reception_terminal_summary,
            "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING",
        ),
        _check(
            "selected_source_body_reception_closure_basis_declared",
            _present(source_body_reception_closure_basis),
            "selected source-body reception closure basis declared",
            source_body_reception_closure_basis,
            "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING",
        ),
        _check(
            "selected_distributed_operation_terminal_closure_basis_declared_where_applicable",
            not _requires_basis(
                request,
                "distributed_operation_basis_required",
                "selected_distributed_operation_basis_required",
            )
            or _present(distributed_operation_basis),
            "distributed operation terminal / closure basis when required",
            distributed_operation_basis,
            "DISTRIBUTED_OPERATION_BASIS_MISSING",
        ),
        _check(
            "selected_current_body_conformance_orientation_basis_declared_where_applicable",
            not _requires_basis(
                request,
                "current_body_basis_required",
                "selected_current_body_basis_required",
            )
            or _present(current_body_basis),
            "current body conformance / orientation basis when required",
            current_body_basis,
            "CURRENT_BODY_BASIS_MISSING",
        ),
        _check(
            "declared_evidence_classes_present",
            _present(declared_evidence_classes),
            "declared evidence classes present",
            declared_evidence_classes,
            "DECLARED_EVIDENCE_CLASSES_MISSING",
        ),
        _check(
            "required_source_surfaces_declared",
            _present(required_source_surfaces),
            "required source surfaces declared",
            required_source_surfaces,
            "REQUIRED_SOURCE_SURFACES_MISSING",
        ),
        _check(
            "required_spec_surfaces_declared",
            _present(required_spec_surfaces),
            "required spec surfaces declared",
            required_spec_surfaces,
            "REQUIRED_SPEC_SURFACES_MISSING",
        ),
        _check(
            "required_resolver_surfaces_declared",
            _present(required_resolver_surfaces),
            "required resolver surfaces declared",
            required_resolver_surfaces,
            "REQUIRED_RESOLVER_SURFACES_MISSING",
        ),
        _check(
            "required_test_surfaces_declared",
            _present(required_test_surfaces),
            "required test surfaces declared",
            required_test_surfaces,
            "REQUIRED_TEST_SURFACES_MISSING",
        ),
        _check(
            "required_artifact_roots_declared",
            _present(required_artifact_roots),
            "required artifact roots declared",
            required_artifact_roots,
            "REQUIRED_ARTIFACT_ROOTS_MISSING",
        ),
        _check(
            "required_closure_artifacts_declared",
            _present(required_closure_artifacts),
            "required closure artifacts declared",
            required_closure_artifacts,
            "REQUIRED_CLOSURE_ARTIFACTS_MISSING",
        ),
        _check(
            "terminal_summary_surfaces_declared",
            _present(required_terminal_summaries),
            "terminal summary surfaces declared",
            required_terminal_summaries,
            "REQUIRED_TERMINAL_SUMMARIES_MISSING",
        ),
        _check(
            "corrected_closure_artifact_posture_declared_where_relevant",
            _present(request.get("corrected_closure_artifact_posture"))
            or not _requires_basis(request, "corrected_closure_artifact_posture_required"),
            "corrected closure artifact posture declared where relevant",
            request.get("corrected_closure_artifact_posture"),
            "CORRECTED_CLOSURE_ARTIFACT_POSTURE_MISSING",
        ),
        _check(
            "failed_input_evidence_posture_declared_where_relevant",
            _present(request.get("failed_input_evidence_posture"))
            or not _requires_basis(request, "failed_input_evidence_posture_required"),
            "failed-input evidence posture declared where relevant",
            request.get("failed_input_evidence_posture"),
            "FAILED_INPUT_EVIDENCE_POSTURE_MISSING",
        ),
        _check(
            "future_candidate_postures_declared",
            _present(future_candidate_postures),
            "future manifest/checksum/signature/packet/command candidate postures declared",
            future_candidate_postures,
            "FUTURE_CANDIDATE_POSTURE_MISSING",
        ),
        _check(
            "manifest_checksum_signature_packet_command_candidate_postures_future_only",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "manifest_implemented",
                    "checksum_implemented",
                    "signature_implemented",
                    "packet_implemented",
                    "command_implemented",
                    "command_authorized",
                )
            ),
            "candidate postures are future-only",
            "no implementation or authorization flags detected",
            "FUTURE_CANDIDATE_POSTURE_MISSING",
        ),
        _check(
            "evidence_only_posture_declared",
            _present(evidence_only_posture),
            "evidence-only posture declared",
            evidence_only_posture,
            "EVIDENCE_ONLY_POSTURE_MISSING",
        ),
        _check(
            "evidence_manifest_scope_supported",
            not unsupported_scope,
            "supported evidence-manifest scope only",
            list(scope_values),
            "UNSUPPORTED_EVIDENCE_MANIFEST_SCOPE",
        ),
    ]

    absence_checks = (
        (
            "evidence_does_not_become_source",
            "evidence_became_source",
            "evidence does not become source",
            "EVIDENCE_TREATED_AS_SOURCE",
        ),
        (
            "evidence_does_not_create_authority",
            "evidence_became_authority",
            "evidence does not create authority",
            "EVIDENCE_TREATED_AS_AUTHORITY",
        ),
        (
            "evidence_does_not_create_currentness",
            "evidence_created_currentness",
            "evidence does not create currentness",
            "EVIDENCE_TREATED_AS_CURRENTNESS",
        ),
        (
            "path_does_not_create_currentness",
            "path_created_currentness",
            "path does not create currentness",
            "PATH_TREATED_AS_CURRENTNESS",
        ),
        (
            "latest_file_does_not_create_currentness",
            "latest_file_created_currentness",
            "latest file does not create currentness",
            "LATEST_FILE_TREATED_AS_CURRENTNESS",
        ),
        (
            "artifact_existence_does_not_create_currentness",
            "artifact_existence_created_currentness",
            "artifact existence does not create currentness",
            "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
        ),
        (
            "repository_copy_does_not_become_body",
            "repository_copy_became_body",
            "repository copy does not become body",
            "REPOSITORY_COPY_TREATED_AS_BODY",
        ),
        (
            "carrier_possession_does_not_create_currentness",
            "carrier_possession_created_currentness",
            "carrier possession does not create currentness",
            "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS",
        ),
        (
            "narration_does_not_create_currentness",
            "narration_created_currentness",
            "narration does not create currentness",
            "NARRATION_TREATED_AS_CURRENTNESS",
        ),
        (
            "command_remains_future_work",
            "command_implemented",
            "command remains future work",
            "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION",
        ),
        (
            "manifest_implementation_remains_future_work",
            "manifest_implemented",
            "manifest implementation remains future work",
            "MANIFEST_CANDIDATE_TREATED_AS_IMPLEMENTATION",
        ),
        (
            "checksum_signature_implementation_remains_future_work",
            "checksum_implemented",
            "checksum/signature implementation remains future work",
            "CHECKSUM_CANDIDATE_TREATED_AS_IMPLEMENTATION",
        ),
        (
            "packet_implementation_remains_future_work",
            "packet_implemented",
            "packet implementation remains future work",
            "PACKET_CANDIDATE_TREATED_AS_IMPLEMENTATION",
        ),
        (
            "verification_command_remains_future_work",
            "command_authorized",
            "verification command remains future work",
            "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION",
        ),
        (
            "evidence_review_does_not_create_transfer",
            "source_transferred",
            "evidence review does not create transfer",
            "EVIDENCE_REVIEW_CREATES_TRANSFER",
        ),
        (
            "evidence_review_does_not_create_migration",
            "source_migrated",
            "evidence review does not create migration",
            "EVIDENCE_REVIEW_CREATES_MIGRATION",
        ),
        (
            "evidence_review_does_not_create_source_receipt",
            "source_receipt_recorded",
            "evidence review does not create source receipt",
            "EVIDENCE_REVIEW_CREATES_SOURCE_RECEIPT",
        ),
        (
            "evidence_review_does_not_authorize_reception",
            "reception_authorized",
            "evidence review does not authorize reception",
            "EVIDENCE_REVIEW_AUTHORIZES_RECEPTION",
        ),
        (
            "evidence_review_does_not_create_deployment",
            "deployment_created",
            "evidence review does not create deployment",
            "EVIDENCE_REVIEW_CREATES_DEPLOYMENT",
        ),
        (
            "evidence_review_does_not_create_runtime_hosting",
            "runtime_hosting_created",
            "evidence review does not create runtime hosting",
            "EVIDENCE_REVIEW_CREATES_RUNTIME_HOSTING",
        ),
        (
            "evidence_review_does_not_create_public_release",
            "public_release_created",
            "evidence review does not create public release",
            "EVIDENCE_REVIEW_CREATES_PUBLIC_RELEASE",
        ),
        (
            "evidence_review_does_not_authorize_continuation",
            "continuation_authorized",
            "evidence review does not authorize continuation",
            "EVIDENCE_REVIEW_AUTHORIZES_CONTINUATION",
        ),
        (
            "evidence_review_does_not_create_reusable_permission",
            "reusable_permission_created",
            "evidence review does not create reusable permission",
            "EVIDENCE_REVIEW_CREATES_REUSABLE_PERMISSION",
        ),
        (
            "evidence_review_does_not_authorize_derivative_reception",
            "derivative_reception_authorized",
            "evidence review does not authorize derivative reception",
            "EVIDENCE_REVIEW_AUTHORIZES_DERIVATIVE_RECEPTION",
        ),
        (
            "evidence_review_does_not_authorize_vessel_relation",
            "vessel_relation_authorized",
            "evidence review does not authorize vessel relation",
            "EVIDENCE_REVIEW_AUTHORIZES_VESSEL_RELATION",
        ),
        (
            "evidence_review_does_not_authorize_another_reception_request",
            "another_reception_request_authorized",
            "evidence review does not authorize another reception request",
            "EVIDENCE_REVIEW_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
        ),
        (
            "evidence_review_does_not_authorize_follow_on_work",
            "follow_on_work_authorized",
            "evidence review does not authorize follow-on work",
            "EVIDENCE_REVIEW_AUTHORIZES_FOLLOW_ON_WORK",
        ),
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


def _evidence_class_booleans(declared_evidence_classes: Any) -> dict[str, Any]:
    classes = _declared_classes_list(declared_evidence_classes)
    lower_names = {str(item).lower() for item in classes}
    return {
        "declared_evidence_classes_count": len(classes),
        "declared_evidence_classes_representative": copy.deepcopy(classes[:20]),
        "source_surfaces_named": any("source" in item for item in lower_names),
        "spec_surfaces_named": any("spec" in item for item in lower_names),
        "resolver_surfaces_named": any("resolver" in item for item in lower_names),
        "test_surfaces_named": any("test" in item for item in lower_names),
        "artifact_roots_named": any("artifact" in item for item in lower_names),
        "closure_artifacts_named": any("closure" in item for item in lower_names),
        "terminal_summaries_named": any("terminal" in item for item in lower_names),
    }


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    request_malformed_code: str | None = None,
) -> dict[str, Any]:
    portable_basis, portable_basis_path, portable_basis_load_code = (
        _load_selected_portable_verification_basis(request)
    )
    source_body_basis, source_body_basis_path, source_body_basis_load_code = (
        _load_selected_source_body_basis(request)
    )

    source_body_reception_terminal_summary = _selected_source_body_terminal_summary(
        request, source_body_basis
    )
    source_body_reception_closure_basis = _selected_source_body_reception_closure_basis(
        request, source_body_basis
    )
    distributed_basis = _distributed_operation_basis(request)
    current_basis = _current_body_basis(request)
    declared_evidence_classes = request.get("declared_evidence_classes")
    required_source_surfaces = _surface_value(request, "required_source_surfaces")
    required_spec_surfaces = _surface_value(request, "required_spec_surfaces")
    required_resolver_surfaces = _surface_value(request, "required_resolver_surfaces")
    required_test_surfaces = _surface_value(request, "required_test_surfaces")
    required_artifact_roots = _surface_value(request, "required_artifact_roots")
    required_closure_artifacts = _surface_value(request, "required_closure_artifacts")
    required_terminal_summaries = _surface_value(request, "required_terminal_summaries")
    evidence_only_posture = request.get("evidence_only_posture")
    future_candidate_postures = _first_present(
        request.get("future_candidate_postures"),
        request.get("manifest_candidate_posture"),
        request.get("checksum_candidate_posture"),
        request.get("signature_candidate_posture"),
        request.get("packet_candidate_posture"),
        request.get("command_candidate_posture"),
    )
    scope_values = _scope_values(request.get("evidence_manifest_scope"))

    block_code = request_malformed_code or _determine_block_code(
        request,
        portable_basis,
        portable_basis_load_code,
        source_body_basis,
        source_body_basis_load_code,
        source_body_reception_terminal_summary,
        source_body_reception_closure_basis,
        distributed_basis,
        current_basis,
        declared_evidence_classes,
        required_source_surfaces,
        required_spec_surfaces,
        required_resolver_surfaces,
        required_test_surfaces,
        required_artifact_roots,
        required_closure_artifacts,
        required_terminal_summaries,
        evidence_only_posture,
        future_candidate_postures,
        scope_values,
    )

    requested_outcome = (
        request.get("requested_evidence_manifest_outcome") or OUTCOME_RECORDED
    )
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("evidence_manifest_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = requested_outcome
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED"

    checks = _build_checks(
        request,
        portable_basis,
        source_body_basis,
        source_body_reception_terminal_summary,
        source_body_reception_closure_basis,
        distributed_basis,
        current_basis,
        declared_evidence_classes,
        required_source_surfaces,
        required_spec_surfaces,
        required_resolver_surfaces,
        required_test_surfaces,
        required_artifact_roots,
        required_closure_artifacts,
        required_terminal_summaries,
        evidence_only_posture,
        future_candidate_postures,
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
                    "evidence_manifest_review_blocked",
                    False,
                    "non-blocked evidence-manifest review",
                    block_code,
                    block_code,
                )
            )

    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    passed_count = len(checks) - failed_count
    if outcome == OUTCOME_RECORDED and failed_count != 0:
        outcome = OUTCOME_BLOCKED
        block_code = block_code or "PORTABLE_VERIFICATION_BASIS_MISSING"

    portable_basis_id = _first_present(
        request.get("selected_portable_verification_result_id"),
        _basis_id(portable_basis),
    )
    portable_basis_outcome = _first_present(
        request.get("selected_portable_verification_result_outcome"),
        _value_at(portable_basis, ("outcome",)),
        _value_at(
            portable_basis,
            ("portable_source_body_verification_summary", "outcome"),
        ),
    )
    portable_basis_reference = _basis_reference(portable_basis)
    source_body_basis_id = _basis_id(source_body_basis)
    source_body_basis_reference = _basis_reference(source_body_basis)
    result_id_seed = _first_present(
        request.get("evidence_manifest_request_id"),
        portable_basis_id,
        source_body_basis_id,
    )
    result_id = (
        f"{_safe_component(result_id_seed)}"
        "__portable_source_body_verification_evidence_manifest_result"
    )
    recorded = outcome == OUTCOME_RECORDED
    non_claims = _build_non_claims(outcome)
    class_summary = _evidence_class_booleans(declared_evidence_classes)

    selected_portable_verification_basis_section = {
        "selected_portable_verification_result_id": portable_basis_id,
        "selected_portable_verification_result_outcome": portable_basis_outcome,
        "selected_portable_verification_result_path": portable_basis_path
        or request.get("selected_portable_verification_result_path"),
        "selected_portable_verification_terminal_summary_path": request.get(
            "selected_portable_verification_terminal_summary_path"
        ),
        "selected_portable_verification_terminal_summary": copy.deepcopy(
            request.get("selected_portable_verification_terminal_summary")
        ),
        "portable_verification_recorded_posture": copy.deepcopy(
            request.get("portable_verification_recorded_posture")
        ),
        "portable_verification_terminal_summary_posture": copy.deepcopy(
            request.get("portable_verification_terminal_summary_posture")
        ),
        "portable_verification_remains_verification_only": True,
        "portable_verification_did_not_authorize_manifest_checksum_signature_packet_command_work": True,
        "portable_verification_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
        "raw_selected_portable_verification_basis": copy.deepcopy(portable_basis),
    }

    selected_source_body_basis_section = {
        "selected_source_body_basis_id": source_body_basis_id,
        "selected_source_body_basis_reference": source_body_basis_reference,
        "selected_source_body_basis_path": source_body_basis_path,
        "selected_source_body_reception_terminal_summary": copy.deepcopy(
            source_body_reception_terminal_summary
        ),
        "selected_source_body_reception_closure_basis": copy.deepcopy(
            source_body_reception_closure_basis
        ),
        "selected_distributed_operation_terminal_closure_basis": copy.deepcopy(
            distributed_basis
        ),
        "selected_current_body_conformance_orientation_basis": copy.deepcopy(
            current_basis
        ),
        "selected_source_body_basis_remains_bounded_evidence_only": True,
        "selected_source_body_basis_does_not_become_source": True,
        "selected_source_body_basis_does_not_create_currentness": True,
        "selected_source_body_basis_does_not_authorize_next_work": True,
        "raw_selected_source_body_basis": copy.deepcopy(source_body_basis),
    }

    declared_evidence_classes_section = {
        "declared_evidence_classes_as_supplied": copy.deepcopy(declared_evidence_classes),
        **class_summary,
        "source_surfaces": copy.deepcopy(required_source_surfaces),
        "spec_surfaces": copy.deepcopy(required_spec_surfaces),
        "resolver_surfaces": copy.deepcopy(required_resolver_surfaces),
        "test_surfaces": copy.deepcopy(required_test_surfaces),
        "artifact_roots": copy.deepcopy(required_artifact_roots),
        "closure_artifacts": copy.deepcopy(required_closure_artifacts),
        "terminal_summaries": copy.deepcopy(required_terminal_summaries),
        "corrected_closure_evidence": copy.deepcopy(
            request.get("corrected_closure_artifact_posture")
        ),
        "failed_input_evidence_posture": copy.deepcopy(
            request.get("failed_input_evidence_posture")
        ),
        "future_manifest_candidate": copy.deepcopy(
            request.get("manifest_candidate_posture")
        ),
        "future_checksum_candidate": copy.deepcopy(
            request.get("checksum_candidate_posture")
        ),
        "future_signature_candidate": copy.deepcopy(
            request.get("signature_candidate_posture")
        ),
        "future_packet_candidate": copy.deepcopy(request.get("packet_candidate_posture")),
        "future_command_candidate": copy.deepcopy(request.get("command_candidate_posture")),
        "evidence_classes_are_evidence_only": True,
        "evidence_classes_do_not_implement_anything": True,
        "evidence_classes_do_not_authorize_command": True,
    }

    required_surfaces_section = {
        "required_source_surfaces": copy.deepcopy(required_source_surfaces),
        "required_spec_surfaces": copy.deepcopy(required_spec_surfaces),
        "required_resolver_surfaces": copy.deepcopy(required_resolver_surfaces),
        "required_test_surfaces": copy.deepcopy(required_test_surfaces),
        "required_artifact_roots": copy.deepcopy(required_artifact_roots),
        "required_closure_artifacts": copy.deepcopy(required_closure_artifacts),
        "required_terminal_summaries": copy.deepcopy(required_terminal_summaries),
        "corrected_closure_artifact_posture": copy.deepcopy(
            request.get("corrected_closure_artifact_posture")
        ),
        "failed_input_evidence_posture": copy.deepcopy(
            request.get("failed_input_evidence_posture")
        ),
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_source": True,
        "surfaces_do_not_create_authority": True,
        "surfaces_do_not_create_currentness": True,
        "surfaces_do_not_create_permission": True,
        "surfaces_do_not_create_command_execution": True,
        "surfaces_do_not_create_deployment_or_public_release": True,
    }

    evidence_only_posture_section = {
        "evidence_only_posture_as_supplied": copy.deepcopy(evidence_only_posture),
        "no_evidence_authority_posture": copy.deepcopy(
            request.get("no_evidence_authority_posture")
        ),
        "no_currentness_posture": copy.deepcopy(request.get("no_currentness_posture")),
        "evidence_does_not_become_source": True,
        "evidence_does_not_create_authority": True,
        "evidence_does_not_create_currentness": True,
        "evidence_does_not_create_permission": True,
        "path_does_not_create_currentness": True,
        "latest_file_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "carrier_possession_does_not_create_currentness": True,
        "narration_does_not_create_currentness": True,
    }

    future_candidate_postures_section = {
        "future_candidate_postures_as_supplied": copy.deepcopy(
            future_candidate_postures
        ),
        "manifest_candidate_posture": copy.deepcopy(
            request.get("manifest_candidate_posture")
        ),
        "checksum_candidate_posture": copy.deepcopy(
            request.get("checksum_candidate_posture")
        ),
        "signature_candidate_posture": copy.deepcopy(
            request.get("signature_candidate_posture")
        ),
        "packet_candidate_posture": copy.deepcopy(request.get("packet_candidate_posture")),
        "command_candidate_posture": copy.deepcopy(
            request.get("command_candidate_posture")
        ),
        "manifest_candidate_future_only": True,
        "checksum_candidate_future_only": True,
        "signature_candidate_future_only": True,
        "packet_candidate_future_only": True,
        "command_candidate_future_only": True,
        "manifest_not_implemented": True,
        "checksum_not_implemented": True,
        "signature_not_implemented": True,
        "packet_not_implemented": True,
        "command_not_implemented": True,
        "command_not_authorized": True,
        "command_requires_separate_boundary": True,
        "candidates_are_not_source": True,
        "candidates_are_not_authority": True,
        "candidates_are_not_currentness": True,
        "candidates_are_not_permission": True,
    }

    evidence_manifest_scope_section = {
        "selected_evidence_manifest_scope_values": list(scope_values),
        "all_selected_scope_values_supported": all(
            value in SUPPORTED_EVIDENCE_MANIFEST_SCOPE for value in scope_values
        ),
        "evidence_manifest_boundary_only": True,
        "evidence_manifest_is_not_manifest_implementation": True,
        "evidence_manifest_is_not_command": True,
        "evidence_manifest_is_not_checksum": True,
        "evidence_manifest_is_not_signature": True,
        "evidence_manifest_is_not_packet": True,
        "evidence_manifest_is_not_transfer": True,
        "evidence_manifest_is_not_migration": True,
        "evidence_manifest_is_not_source_receipt": True,
        "evidence_manifest_is_not_reception_authorization": True,
        "evidence_manifest_is_not_deployment": True,
        "evidence_manifest_is_not_runtime_hosting": True,
        "evidence_manifest_is_not_public_release": True,
        "evidence_does_not_become_source": True,
        "evidence_does_not_create_authority": True,
        "evidence_does_not_create_currentness": True,
        "path_does_not_create_currentness": True,
        "latest_file_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "command_requires_separate_boundary": True,
    }

    evidence_manifest_statement = {
        "portable_source_body_verification_evidence_manifest_recorded": recorded,
        "evidence_manifest_basis_declared": recorded,
        "required_verification_evidence_classes_declared": recorded,
        "selected_portable_verification_basis_preserved": recorded,
        "selected_source_body_basis_preserved": recorded,
        "declared_evidence_classes_preserved": recorded,
        "required_surfaces_preserved": recorded,
        "evidence_only_posture_declared": recorded,
        "future_candidate_postures_declared": recorded,
        "evidence_manifest_boundary_only": True,
        "evidence_manifest_is_not_manifest_implementation": True,
        "evidence_manifest_is_not_command": True,
        "evidence_manifest_is_not_checksum": True,
        "evidence_manifest_is_not_signature": True,
        "evidence_manifest_is_not_packet": True,
        "evidence_does_not_become_source": True,
        "evidence_does_not_create_authority": True,
        "evidence_does_not_create_currentness": True,
        "path_does_not_create_currentness": True,
        "latest_file_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "command_requires_separate_boundary": True,
        "manifest_implemented": False,
        "checksum_implemented": False,
        "signature_implemented": False,
        "packet_implemented": False,
        "command_implemented": False,
        "command_authorized": False,
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
        "recorded_true_fields_are_bounded_evidence_manifest_outcomes_only": True,
    }

    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": copy.deepcopy(
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
        "evidence_manifest_request_id": request.get("evidence_manifest_request_id"),
        "evidence_manifest_question": request.get("evidence_manifest_question"),
        "evidence_manifest_intent": request.get("evidence_manifest_intent"),
        "declared_request_path": request_path,
        "selected_portable_verification_result_id": portable_basis_id,
        "selected_portable_verification_result_outcome": portable_basis_outcome,
        "selected_portable_verification_result_path": portable_basis_path
        or request.get("selected_portable_verification_result_path"),
        "selected_portable_verification_terminal_summary_path": request.get(
            "selected_portable_verification_terminal_summary_path"
        ),
        "selected_source_body_basis_id": source_body_basis_id,
        "selected_source_body_basis_reference": source_body_basis_reference,
        "declared_evidence_classes_count": class_summary[
            "declared_evidence_classes_count"
        ],
        "evidence_manifest_is_not_manifest_implementation": True,
        "evidence_manifest_is_not_command": True,
        "evidence_manifest_is_not_checksum": True,
        "evidence_manifest_is_not_signature": True,
        "evidence_manifest_is_not_packet": True,
        "evidence_manifest_is_not_transfer": True,
        "evidence_manifest_is_not_migration": True,
        "evidence_manifest_is_not_source_receipt": True,
        "evidence_manifest_is_not_reception_authorization": True,
        "evidence_manifest_is_not_deployment_runtime_public_release": True,
        "no_operation_permission_public_readiness_final_completion_continuation_reusable_permission": True,
        "command_requires_separate_boundary": True,
    }

    result = {
        "portable_source_body_verification_evidence_manifest_metadata": {
            "portable_source_body_verification_evidence_manifest_result_id": result_id,
            "portable_source_body_verification_evidence_manifest_result_type": (
                "portable_source_body_verification_evidence_manifest_boundary_result"
            ),
            "portable_source_body_verification_evidence_manifest_result_version": (
                RESULT_VERSION
            ),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_evidence_manifest_question": declared_question_section,
        "selected_portable_verification_basis": (
            selected_portable_verification_basis_section
        ),
        "selected_source_body_basis": selected_source_body_basis_section,
        "declared_evidence_classes": declared_evidence_classes_section,
        "required_surfaces": required_surfaces_section,
        "evidence_only_posture": evidence_only_posture_section,
        "future_candidate_postures": future_candidate_postures_section,
        "evidence_manifest_scope": evidence_manifest_scope_section,
        "evidence_manifest_checks": checks,
        "evidence_manifest_statement": evidence_manifest_statement,
        "evidence_manifest_non_meaning": _build_evidence_manifest_non_meaning(),
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
    result["portable_source_body_verification_evidence_manifest_summary"] = (
        build_portable_source_body_verification_evidence_manifest_summary(result)
    )
    return result


def _malformed_request_result(
    code: str, reason: str, request_path: str | None = None
) -> dict[str, Any]:
    request = {
        "evidence_manifest_request_id": None,
        "evidence_manifest_question": None,
        "evidence_manifest_intent": None,
        "declared_non_claims": {},
    }
    result = _build_result(
        request,
        request_path=request_path,
        request_malformed_code=code,
    )
    result["block"]["block_reason"] = reason
    return result


def resolve_portable_source_body_verification_evidence_manifest_boundary(
    declared_evidence_manifest_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve a declared portable verification evidence-manifest request."""
    if declared_evidence_manifest_request is None:
        return _build_result({})
    if not isinstance(declared_evidence_manifest_request, Mapping):
        return _malformed_request_result(
            "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
            "declared evidence-manifest request must be a JSON object / mapping",
        )
    return _build_result(copy.deepcopy(dict(declared_evidence_manifest_request)))


def resolve_portable_source_body_verification_evidence_manifest_boundary_from_path(
    declared_evidence_manifest_request_path: Path | str,
) -> dict:
    """Resolve a declared evidence-manifest request read from a JSON object path."""
    path = Path(declared_evidence_manifest_request_path)
    payload, failure = _read_json_object(path)
    if failure == "unreadable":
        return _malformed_request_result(
            "DECLARED_EVIDENCE_MANIFEST_REQUEST_UNREADABLE",
            "declared evidence-manifest request path is unreadable",
            str(path),
        )
    if failure == "malformed":
        return _malformed_request_result(
            "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
            "declared evidence-manifest request path is malformed or not a JSON object",
            str(path),
        )
    if payload is None:
        return _malformed_request_result(
            "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
            "declared evidence-manifest request path did not produce a JSON object",
            str(path),
        )
    return _build_result(payload, request_path=str(path))


def build_portable_source_body_verification_evidence_manifest_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary from an evidence-manifest boundary result."""
    checks = result.get("evidence_manifest_checks", [])
    passed_count = sum(1 for check in checks if check.get("passed") is True)
    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    question = result.get("declared_evidence_manifest_question", {})
    statement = result.get("evidence_manifest_statement", {})
    selected_portable = result.get("selected_portable_verification_basis", {})
    selected_source = result.get("selected_source_body_basis", {})
    classes = result.get("declared_evidence_classes", {})
    surfaces = result.get("required_surfaces", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block", {})
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "evidence_manifest_request_id": question.get("evidence_manifest_request_id"),
        "evidence_manifest_question": question.get("evidence_manifest_question"),
        "evidence_manifest_intent": question.get("evidence_manifest_intent"),
        "selected_portable_verification_result_id": selected_portable.get(
            "selected_portable_verification_result_id"
        ),
        "selected_portable_verification_result_outcome": selected_portable.get(
            "selected_portable_verification_result_outcome"
        ),
        "selected_portable_verification_result_path": selected_portable.get(
            "selected_portable_verification_result_path"
        ),
        "selected_portable_verification_terminal_summary_path": selected_portable.get(
            "selected_portable_verification_terminal_summary_path"
        ),
        "selected_source_body_basis_reference": selected_source.get(
            "selected_source_body_basis_reference"
        ),
        "declared_evidence_classes_count": classes.get(
            "declared_evidence_classes_count"
        ),
        "declared_evidence_classes_representative": classes.get(
            "declared_evidence_classes_representative"
        ),
        "required_source_surfaces_declared": _present(
            surfaces.get("required_source_surfaces")
        ),
        "required_spec_surfaces_declared": _present(
            surfaces.get("required_spec_surfaces")
        ),
        "required_resolver_surfaces_declared": _present(
            surfaces.get("required_resolver_surfaces")
        ),
        "required_test_surfaces_declared": _present(
            surfaces.get("required_test_surfaces")
        ),
        "required_artifact_roots_declared": _present(
            surfaces.get("required_artifact_roots")
        ),
        "required_closure_artifacts_declared": _present(
            surfaces.get("required_closure_artifacts")
        ),
        "required_terminal_summaries_declared": _present(
            surfaces.get("required_terminal_summaries")
        ),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "portable_source_body_verification_evidence_manifest_recorded": statement.get(
            "portable_source_body_verification_evidence_manifest_recorded", False
        ),
        "evidence_manifest_basis_declared": statement.get(
            "evidence_manifest_basis_declared", False
        ),
        "required_verification_evidence_classes_declared": statement.get(
            "required_verification_evidence_classes_declared", False
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_portable_verification_basis_preserved": statement.get(
            "selected_portable_verification_basis_preserved", False
        ),
        "selected_source_body_basis_preserved": statement.get(
            "selected_source_body_basis_preserved", False
        ),
        "declared_evidence_classes_preserved": statement.get(
            "declared_evidence_classes_preserved", False
        ),
        "required_surfaces_preserved": statement.get(
            "required_surfaces_preserved", False
        ),
        "evidence_only_posture_declared": statement.get(
            "evidence_only_posture_declared", False
        ),
        "future_candidate_postures_declared": statement.get(
            "future_candidate_postures_declared", False
        ),
        "evidence_manifest_boundary_only": statement.get(
            "evidence_manifest_boundary_only", True
        ),
        "evidence_manifest_not_manifest_command_checksum_signature_packet": all(
            statement.get(key, False)
            for key in (
                "evidence_manifest_is_not_manifest_implementation",
                "evidence_manifest_is_not_command",
                "evidence_manifest_is_not_checksum",
                "evidence_manifest_is_not_signature",
                "evidence_manifest_is_not_packet",
            )
        ),
        "evidence_does_not_become_source_authority_currentness": all(
            statement.get(key, False)
            for key in (
                "evidence_does_not_become_source",
                "evidence_does_not_create_authority",
                "evidence_does_not_create_currentness",
            )
        ),
        "path_latest_artifact_repository_carrier_narration_not_currentness_body": all(
            non_claims.get(key) is False
            for key in (
                "path_created_currentness",
                "latest_file_created_currentness",
                "artifact_existence_created_currentness",
                "repository_copy_became_body",
                "carrier_possession_created_currentness",
                "narration_created_currentness",
            )
        ),
        "command_requires_separate_boundary": statement.get(
            "command_requires_separate_boundary", True
        ),
        "no_manifest_checksum_signature_packet_command_implemented": all(
            non_claims.get(key) is False
            for key in (
                "manifest_implemented",
                "checksum_implemented",
                "signature_implemented",
                "packet_implemented",
                "command_implemented",
                "command_authorized",
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
            for key in REQUIRED_FALSE_NON_CLAIMS
            + ALLOWED_RECORDED_TRUE_FIELDS
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


def write_portable_source_body_verification_evidence_manifest_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one additive evidence-manifest result artifact as UTF-8 JSON."""
    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationEvidenceManifestBoundaryError(
            "evidence-manifest result must be a mapping"
        )
    if output_path is None:
        summary = result.get(
            "portable_source_body_verification_evidence_manifest_summary", {}
        )
        metadata = result.get(
            "portable_source_body_verification_evidence_manifest_metadata", {}
        )
        seed = _first_present(
            summary.get("evidence_manifest_request_id"),
            summary.get("selected_portable_verification_result_id"),
            metadata.get(
                "portable_source_body_verification_evidence_manifest_result_id"
            ),
        )
        filename = (
            f"{_safe_component(seed)}"
            "__portable_source_body_verification_evidence_manifest_result.json"
        )
        target = PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_ROOT / filename
    else:
        target = Path(output_path)
    target = _deduplicated_output_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def _required_surfaces_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "required_source_surfaces": [value],
        "required_spec_surfaces": [value],
        "required_resolver_surfaces": [value],
        "required_test_surfaces": [value],
        "required_artifact_roots": [value],
        "required_closure_artifacts": [value],
        "required_terminal_summaries": [value],
    }


def _portable_basis_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "selected_portable_verification_basis_reference": value,
        "portable_verification_remains_verification_only": True,
        "portable_verification_did_not_authorize_manifest_checksum_signature_packet_command_work": True,
    }


def _source_body_basis_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "selected_source_body_basis_reference": value,
        "selected_source_body_reception_terminal_summary": {
            "terminal_summary_reference": f"{value}::source_body_reception_terminal_summary",
            "terminal_summary_is_evidence_only": True,
        },
        "selected_source_body_reception_closure_basis": {
            "closure_basis_reference": f"{value}::source_body_reception_closure",
            "closure_basis_is_evidence_only": True,
        },
        "selected_source_body_basis_remains_bounded_evidence_only": True,
    }


def _evidence_only_posture_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "evidence_only_posture_reference": value,
        "evidence_does_not_become_source": True,
        "evidence_does_not_create_authority": True,
        "evidence_does_not_create_currentness": True,
        "path_does_not_create_currentness": True,
        "latest_file_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "carrier_possession_does_not_create_currentness": True,
        "narration_does_not_create_currentness": True,
    }


def _future_candidate_postures_from_value(value: Mapping[str, Any] | str) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {
        "future_candidate_posture_reference": value,
        "manifest_candidate_future_only": True,
        "checksum_candidate_future_only": True,
        "signature_candidate_future_only": True,
        "packet_candidate_future_only": True,
        "command_candidate_future_only": True,
        "manifest_not_implemented": True,
        "checksum_not_implemented": True,
        "signature_not_implemented": True,
        "packet_not_implemented": True,
        "command_not_implemented": True,
        "command_not_authorized": True,
        "command_requires_separate_boundary": True,
    }


def build_declared_portable_source_body_verification_evidence_manifest_request(
    evidence_manifest_request_id: str,
    evidence_manifest_question: str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    selected_source_body_basis: Mapping[str, Any] | str,
    declared_evidence_classes: Mapping[str, Any] | Sequence[str] | str,
    required_surfaces: Mapping[str, Any] | str,
    evidence_only_posture: Mapping[str, Any] | str,
    future_candidate_postures: Mapping[str, Any] | str,
    evidence_manifest_scope: Sequence[str] | Mapping[str, Any],
    evidence_manifest_intent: str = INTENT_RECORD,
    *,
    selected_portable_verification_result_path: str | None = None,
    selected_portable_verification_result_id: str | None = None,
    selected_portable_verification_result_outcome: str | None = None,
    requested_evidence_manifest_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a bounded declared evidence-manifest request."""
    selected_portable = _portable_basis_from_value(selected_portable_verification_basis)
    selected_source = _source_body_basis_from_value(selected_source_body_basis)
    surfaces = _required_surfaces_from_value(required_surfaces)
    future_postures = _future_candidate_postures_from_value(future_candidate_postures)

    request = {
        "evidence_manifest_request_id": evidence_manifest_request_id,
        "evidence_manifest_question": evidence_manifest_question,
        "evidence_manifest_intent": evidence_manifest_intent,
        "selected_portable_verification_basis": selected_portable,
        "selected_source_body_basis": selected_source,
        "declared_evidence_classes": copy.deepcopy(declared_evidence_classes),
        "required_surfaces": copy.deepcopy(surfaces),
        "required_source_surfaces": copy.deepcopy(surfaces.get("required_source_surfaces")),
        "required_spec_surfaces": copy.deepcopy(surfaces.get("required_spec_surfaces")),
        "required_resolver_surfaces": copy.deepcopy(
            surfaces.get("required_resolver_surfaces")
        ),
        "required_test_surfaces": copy.deepcopy(surfaces.get("required_test_surfaces")),
        "required_artifact_roots": copy.deepcopy(surfaces.get("required_artifact_roots")),
        "required_closure_artifacts": copy.deepcopy(
            surfaces.get("required_closure_artifacts")
        ),
        "required_terminal_summaries": copy.deepcopy(
            surfaces.get("required_terminal_summaries")
        ),
        "selected_source_body_reception_terminal_summary": copy.deepcopy(
            selected_source.get("selected_source_body_reception_terminal_summary")
        ),
        "selected_source_body_reception_closure_basis": copy.deepcopy(
            selected_source.get("selected_source_body_reception_closure_basis")
        ),
        "evidence_only_posture": _evidence_only_posture_from_value(
            evidence_only_posture
        ),
        "future_candidate_postures": future_postures,
        "manifest_candidate_posture": copy.deepcopy(
            future_postures.get("manifest_candidate_posture")
            or {"manifest_candidate_future_only": True}
        ),
        "checksum_candidate_posture": copy.deepcopy(
            future_postures.get("checksum_candidate_posture")
            or {"checksum_candidate_future_only": True}
        ),
        "signature_candidate_posture": copy.deepcopy(
            future_postures.get("signature_candidate_posture")
            or {"signature_candidate_future_only": True}
        ),
        "packet_candidate_posture": copy.deepcopy(
            future_postures.get("packet_candidate_posture")
            or {"packet_candidate_future_only": True}
        ),
        "command_candidate_posture": copy.deepcopy(
            future_postures.get("command_candidate_posture")
            or {
                "command_candidate_future_only": True,
                "command_requires_separate_boundary": True,
            }
        ),
        "evidence_manifest_scope": copy.deepcopy(evidence_manifest_scope),
        "selected_portable_verification_result_path": selected_portable_verification_result_path,
        "selected_portable_verification_result_id": selected_portable_verification_result_id,
        "selected_portable_verification_result_outcome": selected_portable_verification_result_outcome,
        "requested_evidence_manifest_outcome": requested_evidence_manifest_outcome,
        "additional_basis_context": copy.deepcopy(additional_basis_context or {}),
        "not_recorded_basis": copy.deepcopy(not_recorded_basis),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }
    return request

