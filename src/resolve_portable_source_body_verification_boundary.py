"""Resolve the portable source-body verification boundary.

This resolver answers one question only:

    Can this selected closed source-body basis be verified on another
    technical carrier without carrier capture or carrier authority?

Portable source-body verification records carrier-independent verification
only. It is not source transfer, migration, source receipt, reception
authorization, deployment, runtime hosting, publication, adoption, authority,
currentness, public readiness, final completion, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on authorization.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationBoundaryError(Exception):
    """Raised for impossible portable verification boundary failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_boundary"
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_boundary"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED"
OUTCOME_NOT_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "PORTABLE_SOURCE_BODY_VERIFICATION_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION"
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_REVIEW"
SUPPORTED_PORTABLE_VERIFICATION_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_PORTABLE_VERIFICATION_SCOPE = {
    "PORTABLE_SOURCE_BODY_VERIFICATION_ONLY",
    "VERIFICATION_IS_NOT_TRANSFER",
    "VERIFICATION_IS_NOT_MIGRATION",
    "VERIFICATION_IS_NOT_SOURCE_RECEIPT",
    "VERIFICATION_IS_NOT_RECEPTION_AUTHORIZATION",
    "VERIFICATION_IS_NOT_DEPLOYMENT",
    "VERIFICATION_IS_NOT_RUNTIME_HOSTING",
    "VERIFICATION_IS_NOT_PUBLICATION",
    "VERIFICATION_IS_NOT_ADOPTION",
    "VERIFICATION_IS_NOT_AUTHORITY",
    "VERIFICATION_IS_NOT_CURRENTNESS",
    "VERIFYING_CARRIER_IS_NOT_SOURCE",
    "VERIFYING_CARRIER_IS_NOT_AUTHORITY",
    "DEVICE_IS_NOT_AUTHORITY",
    "OS_IS_NOT_AUTHORITY",
    "VENDOR_IS_NOT_AUTHORITY",
    "LOCAL_PATH_IS_NOT_CURRENTNESS",
    "LATEST_FILE_IS_NOT_CURRENTNESS",
    "REPOSITORY_COPY_IS_NOT_BODY",
    "NARRATION_IS_NOT_CURRENTNESS",
    "NO_OPERATION_PERMISSION",
    "NO_PUBLIC_READINESS",
    "NO_FINAL_COMPLETION",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "carrier_became_source",
    "carrier_became_authority",
    "device_became_authority",
    "os_became_authority",
    "vendor_environment_became_authority",
    "account_became_authority",
    "local_path_created_currentness",
    "latest_file_created_currentness",
    "recency_created_currentness",
    "repository_copy_became_body",
    "artifact_existence_created_currentness",
    "carrier_possession_created_currentness",
    "archive_possession_created_currentness",
    "narration_created_currentness",
    "source_replaced",
    "source_transferred",
    "source_migrated",
    "source_received",
    "source_receipt_recorded",
    "reception_authorized",
    "adoption_created",
    "authority_created",
    "currentness_created",
    "standing_created",
    "operation_permission_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "continuation_authorized",
    "publication_flow_opened",
    "reusable_permission_created",
    "another_reception_request_authorized",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "runtime_hosting_created",
    "deployment_created",
    "public_release_created",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

OUTPUT_FALSE_POSTURE = tuple(
    dict.fromkeys(
        REQUIRED_FALSE_NON_CLAIMS
        + (
            "source_receipt_created",
            "repository_possession_created_currentness",
            "public_readiness_created",
        )
    )
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "portable_source_body_verification_recorded",
    "portable_source_body_basis_verified",
    "carrier_independent_verification_recorded",
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = (
    ("carrier_became_source", "VERIFICATION_TREATS_CARRIER_AS_SOURCE"),
    ("verifying_carrier_became_source", "VERIFICATION_TREATS_CARRIER_AS_SOURCE"),
    ("carrier_became_authority", "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY"),
    ("verifying_carrier_became_authority", "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY"),
    ("original_carrier_continuing_authority", "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY"),
    ("device_became_authority", "VERIFICATION_TREATS_DEVICE_AS_AUTHORITY"),
    ("os_became_authority", "VERIFICATION_TREATS_OS_AS_AUTHORITY"),
    ("operating_system_became_authority", "VERIFICATION_TREATS_OS_AS_AUTHORITY"),
    ("vendor_environment_became_authority", "VERIFICATION_TREATS_VENDOR_AS_AUTHORITY"),
    ("vendor_became_authority", "VERIFICATION_TREATS_VENDOR_AS_AUTHORITY"),
    ("account_became_authority", "VERIFICATION_TREATS_ACCOUNT_AS_AUTHORITY"),
    ("local_path_created_currentness", "VERIFICATION_TREATS_LOCAL_PATH_AS_CURRENTNESS"),
    ("path_currentness_created", "VERIFICATION_TREATS_LOCAL_PATH_AS_CURRENTNESS"),
    ("latest_file_created_currentness", "VERIFICATION_TREATS_LATEST_FILE_AS_CURRENTNESS"),
    ("latest_file_currentness_created", "VERIFICATION_TREATS_LATEST_FILE_AS_CURRENTNESS"),
    ("recency_created_currentness", "VERIFICATION_TREATS_RECENCY_AS_CURRENTNESS"),
    ("repository_copy_became_body", "VERIFICATION_TREATS_REPOSITORY_COPY_AS_BODY"),
    (
        "repository_possession_created_currentness",
        "VERIFICATION_TREATS_REPOSITORY_POSSESSION_AS_CURRENTNESS",
    ),
    (
        "repository_possession_currentness_created",
        "VERIFICATION_TREATS_REPOSITORY_POSSESSION_AS_CURRENTNESS",
    ),
    (
        "artifact_existence_created_currentness",
        "VERIFICATION_TREATS_ARTIFACT_EXISTENCE_AS_CURRENTNESS",
    ),
    (
        "carrier_possession_created_currentness",
        "VERIFICATION_TREATS_CARRIER_POSSESSION_AS_CURRENTNESS",
    ),
    (
        "archive_possession_created_currentness",
        "VERIFICATION_TREATS_ARCHIVE_POSSESSION_AS_CURRENTNESS",
    ),
    ("narration_created_currentness", "VERIFICATION_TREATS_NARRATION_AS_CURRENTNESS"),
    ("human_narration_created_currentness", "VERIFICATION_TREATS_NARRATION_AS_CURRENTNESS"),
    ("source_replaced", "VERIFICATION_REPLACES_SOURCE"),
    ("source_transferred", "VERIFICATION_TRANSFERS_SOURCE"),
    ("source_migrated", "VERIFICATION_MIGRATES_SOURCE"),
    ("reception_authorized", "VERIFICATION_AUTHORIZES_RECEPTION"),
    ("source_received", "VERIFICATION_RECEIVES_SOURCE"),
    ("source_receipt_recorded", "VERIFICATION_RECORDS_SOURCE_RECEIPT"),
    ("source_receipt_created", "VERIFICATION_CREATES_SOURCE_RECEIPT"),
    ("adoption_created", "VERIFICATION_CREATES_ADOPTION"),
    ("authority_created", "VERIFICATION_CREATES_AUTHORITY"),
    ("currentness_created", "VERIFICATION_CREATES_CURRENTNESS"),
    ("standing_created", "VERIFICATION_CREATES_STANDING"),
    ("operation_permission_created", "VERIFICATION_CREATES_OPERATION_PERMISSION"),
    ("public_launch_readiness_created", "VERIFICATION_CREATES_PUBLIC_READINESS"),
    ("public_readiness_created", "VERIFICATION_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "VERIFICATION_CLAIMS_FINAL_COMPLETION"),
    ("continuation_authorized", "VERIFICATION_AUTHORIZES_CONTINUATION"),
    ("follow_on_work_authorized", "VERIFICATION_AUTHORIZES_FOLLOW_ON_WORK"),
    ("publication_flow_opened", "VERIFICATION_OPENS_PUBLICATION_FLOW"),
    ("reusable_permission_created", "VERIFICATION_CREATES_REUSABLE_PERMISSION"),
    (
        "another_reception_request_authorized",
        "VERIFICATION_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
    ),
    ("successor_reception_authorized", "VERIFICATION_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
    ("derivative_reception_authorized", "VERIFICATION_AUTHORIZES_DERIVATIVE_RECEPTION"),
    ("vessel_relation_authorized", "VERIFICATION_AUTHORIZES_VESSEL_RELATION"),
    ("runtime_hosting_created", "VERIFICATION_CREATES_RUNTIME_HOSTING"),
    ("deployment_created", "VERIFICATION_CREATES_DEPLOYMENT"),
    ("public_release_created", "VERIFICATION_CREATES_PUBLIC_RELEASE"),
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
            "recorded",
            "passed",
            "authorized",
            "created",
            "current",
            "source",
        }
    return bool(value)


def _is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return value is False
    if isinstance(value, str):
        return value.strip().lower() in {"false", "no", "0"}
    return value == 0


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
        "path_does_not_create_authority": True,
        "path_does_not_create_currentness": True,
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


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = _first_present(
            scope.get("selected_verification_scope_values"),
            scope.get("verification_scope_values"),
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
    text = str(value or "portable_source_body_verification").strip()
    cleaned = "".join(
        character if character.isalnum() or character in ("-", "_") else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "portable_source_body_verification"


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


def _load_selected_reception_closure_basis(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    return _load_json_basis(
        request,
        value_key="selected_reception_closure_basis",
        path_key="selected_reception_closure_artifact_path",
        reference_key="selected_reception_closure_basis_reference",
        unreadable_code="SOURCE_BODY_RECEPTION_CLOSURE_BASIS_UNREADABLE",
        malformed_code="SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MALFORMED",
    )


def _load_terminal_summary_basis(request: Mapping[str, Any]) -> dict[str, Any] | None:
    supplied = request.get("selected_terminal_summary_basis")
    basis = _normalize_basis(supplied, "selected_terminal_summary_basis_reference")
    path_value = request.get("selected_reception_terminal_summary_path")
    if _present(path_value):
        metadata = _text_path_metadata(str(path_value))
        if basis is None:
            basis = {}
        basis["selected_reception_terminal_summary_path"] = str(path_value)
        basis["selected_reception_terminal_summary_path_metadata"] = metadata
        basis["terminal_summary_path_is_evidence_only"] = True
        basis["terminal_summary_path_does_not_create_currentness"] = True
    return basis


def _basis_id(basis: Mapping[str, Any] | None, *keys: str) -> Any:
    if not isinstance(basis, Mapping):
        return None
    candidates = [basis.get(key) for key in keys]
    candidates.extend(
        [
            basis.get("selected_source_body_basis_id"),
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
            basis.get("selected_source_body_basis_reference"),
            basis.get("reference"),
            basis.get("path"),
            basis.get("basis_reference"),
        ]
    )
    return _first_present(*candidates)


def _closure_artifact_id(
    request: Mapping[str, Any], closure_basis: Mapping[str, Any] | None
) -> Any:
    return _first_present(
        request.get("selected_reception_closure_artifact_id"),
        _value_at(
            closure_basis,
            ("source_body_reception_closure_metadata", "source_body_reception_closure_result_id"),
        ),
        _value_at(
            closure_basis,
            ("source_body_reception_closure_summary", "source_body_reception_closure_result_id"),
        ),
        _value_at(closure_basis, ("source_body_reception_closure_result_id",)),
        _value_at(closure_basis, ("closure_request_id",)),
        _value_at(closure_basis, ("id",)),
    )


def _closure_artifact_outcome(
    request: Mapping[str, Any], closure_basis: Mapping[str, Any] | None
) -> Any:
    return _first_present(
        request.get("selected_reception_closure_artifact_outcome"),
        _value_at(closure_basis, ("outcome",)),
        _value_at(closure_basis, ("source_body_reception_closure_summary", "outcome")),
        _value_at(closure_basis, ("closure_statement", "outcome")),
    )


def _carrier_value(carrier: Mapping[str, Any] | None, prefixed_key: str, generic: str) -> Any:
    if not isinstance(carrier, Mapping):
        return None
    return _first_present(
        carrier.get(prefixed_key),
        carrier.get(generic),
        carrier.get("name") if generic == "id" else None,
        carrier.get("reference") if generic == "id" else None,
    )


def _surface_value(request: Mapping[str, Any], key: str) -> Any:
    surfaces = request.get("required_surfaces")
    return _first_present(
        request.get(key),
        _value_at(surfaces, (key,)),
        _value_at(surfaces, (key.removeprefix("required_"),)),
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
            "even_when_verification_recorded_carrier_does_not_become_source": True,
            "even_when_verification_recorded_carrier_does_not_become_authority": True,
            "even_when_verification_recorded_no_device_os_vendor_account_path_recency_latest_file_repository_artifact_or_narration_becomes_authority_or_currentness": True,
            "even_when_verification_recorded_source_is_not_transferred_migrated_received_replaced_adopted_or_operationalized": True,
            "even_when_verification_recorded_no_public_readiness_final_completion_continuation_reusable_permission_or_next_work_is_authorized": True,
            "even_when_verification_recorded_derivative_reception_vessel_relation_runtime_hosting_deployment_public_release_another_reception_request_publication_flow_and_follow_on_work_remain_unauthorized": True,
        }
    )
    return non_claims


def _build_verification_non_meaning() -> dict[str, bool]:
    names = (
        "source_body_transferred",
        "source_body_migrated",
        "source_received",
        "source_receipt_recorded",
        "source_receipt_created",
        "carrier_became_source",
        "carrier_became_authority",
        "device_became_authority",
        "operating_system_became_authority",
        "vendor_environment_became_authority",
        "account_became_authority",
        "repository_copy_became_source_body",
        "local_path_created_currentness",
        "latest_file_created_currentness",
        "recency_created_currentness",
        "human_narration_created_currentness",
        "artifact_existence_created_currentness",
        "carrier_possession_created_currentness",
        "archive_possession_created_currentness",
        "adoption_created",
        "authority_created",
        "currentness_created",
        "standing_created",
        "operation_permission_created",
        "public_readiness_created",
        "final_completion_claimed",
        "continuation_authorized",
        "follow_on_work_authorized",
        "publication_flow_opened",
        "reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_source_body_reception_request_authorized",
        "runtime_hosting_created",
        "deployment_created",
        "product_packaging_created",
        "public_release_created",
    )
    return {f"verification_does_not_mean_{name}": True for name in names}


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "portable source-body verification test",
            "portable source-body verification live artifact",
            "manifest or source-body packet work",
            "checksum or signature work",
            "portable verification command",
            "reproducible environment declaration",
            "technical carrier packet",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "standing creation",
            "operation permission",
            "receiving-context governance",
            "public readiness",
            "final completion",
            "follow-on work",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "runtime hosting",
            "deployment",
            "public release",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _determine_block_code(
    request: Mapping[str, Any],
    source_body_basis: Mapping[str, Any] | None,
    source_body_basis_load_code: str | None,
    closure_basis: Any,
    reception_closure_basis: Mapping[str, Any] | None,
    reception_closure_load_code: str | None,
    terminal_summary_basis: Any,
    distributed_operation_basis: Any,
    current_body_basis: Any,
    required_source_surfaces: Any,
    required_spec_surfaces: Any,
    required_resolver_surfaces: Any,
    required_test_surfaces: Any,
    required_artifact_roots: Any,
    required_closure_artifacts: Any,
    verifying_carrier: Any,
    original_carrier: Any,
    carrier_independence_basis: Any,
    verification_evidence_basis: Any,
    scope_values: Sequence[str],
) -> str | None:
    if not _present(request.get("portable_verification_question")):
        return "PORTABLE_VERIFICATION_QUESTION_UNDECLARED"
    intent = request.get("portable_verification_intent")
    if intent == INTENT_BLOCK:
        return "PORTABLE_VERIFICATION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_PORTABLE_VERIFICATION_INTENTS:
        return "PORTABLE_VERIFICATION_INTENT_UNSUPPORTED"
    for load_code in (source_body_basis_load_code, reception_closure_load_code):
        if load_code is not None:
            return load_code
    if source_body_basis is None:
        return "SELECTED_SOURCE_BODY_BASIS_MISSING"
    if not _present(closure_basis):
        return "SELECTED_SOURCE_BODY_CLOSURE_BASIS_MISSING"
    if not _present(terminal_summary_basis):
        return "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING"
    if reception_closure_basis is None:
        return "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING"
    if _requires_basis(
        request,
        "distributed_operation_basis_required",
        "selected_distributed_operation_basis_required",
    ) and not _present(distributed_operation_basis):
        return "DISTRIBUTED_OPERATION_CLOSURE_BASIS_MISSING"
    if _requires_basis(
        request,
        "current_body_basis_required",
        "selected_current_body_basis_required",
    ) and not _present(current_body_basis):
        return "CURRENT_BODY_BASIS_MISSING"
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
    if not _present(verifying_carrier):
        return "VERIFYING_CARRIER_MISSING"
    if not _present(original_carrier):
        return "ORIGINAL_CARRIER_MISSING"
    if not _present(carrier_independence_basis):
        return "CARRIER_INDEPENDENCE_BASIS_MISSING"
    if not _present(verification_evidence_basis):
        return "VERIFICATION_EVIDENCE_BASIS_MISSING"
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_PORTABLE_VERIFICATION_SCOPE
    ]
    if unsupported_scope:
        return "UNSUPPORTED_PORTABLE_VERIFICATION_SCOPE"
    collapse = _collapse_code(request)
    if collapse is not None:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    source_body_basis: Mapping[str, Any] | None,
    closure_basis: Any,
    reception_closure_basis: Mapping[str, Any] | None,
    terminal_summary_basis: Any,
    distributed_operation_basis: Any,
    current_body_basis: Any,
    required_source_surfaces: Any,
    required_spec_surfaces: Any,
    required_resolver_surfaces: Any,
    required_test_surfaces: Any,
    required_artifact_roots: Any,
    required_closure_artifacts: Any,
    verifying_carrier: Any,
    original_carrier: Any,
    carrier_independence_basis: Any,
    verification_evidence_basis: Any,
    scope_values: Sequence[str],
) -> list[dict[str, Any]]:
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_PORTABLE_VERIFICATION_SCOPE
    ]
    checks = [
        _check(
            "portable_verification_question_declared",
            _present(request.get("portable_verification_question")),
            "declared portable verification question",
            request.get("portable_verification_question"),
            "PORTABLE_VERIFICATION_QUESTION_UNDECLARED",
        ),
        _check(
            "portable_verification_intent_supported",
            request.get("portable_verification_intent")
            in SUPPORTED_PORTABLE_VERIFICATION_INTENTS
            and request.get("portable_verification_intent") != INTENT_BLOCK,
            sorted(SUPPORTED_PORTABLE_VERIFICATION_INTENTS - {INTENT_BLOCK}),
            request.get("portable_verification_intent"),
            "PORTABLE_VERIFICATION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_closed_source_body_basis_declared",
            source_body_basis is not None,
            "selected closed source-body basis declared",
            source_body_basis is not None,
            "SELECTED_SOURCE_BODY_BASIS_MISSING",
        ),
        _check(
            "selected_source_body_closure_basis_declared",
            _present(closure_basis),
            "selected source-body closure basis declared",
            closure_basis,
            "SELECTED_SOURCE_BODY_CLOSURE_BASIS_MISSING",
        ),
        _check(
            "selected_source_body_reception_terminal_summary_declared",
            _present(terminal_summary_basis),
            "selected source-body reception terminal summary declared",
            terminal_summary_basis,
            "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING",
        ),
        _check(
            "selected_source_body_reception_closure_basis_declared",
            reception_closure_basis is not None,
            "selected source-body reception closure basis declared",
            reception_closure_basis is not None,
            "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING",
        ),
        _check(
            "selected_distributed_operation_closure_terminal_basis_declared_where_applicable",
            not _requires_basis(
                request,
                "distributed_operation_basis_required",
                "selected_distributed_operation_basis_required",
            )
            or _present(distributed_operation_basis),
            "distributed operation closure / terminal basis when required",
            distributed_operation_basis,
            "DISTRIBUTED_OPERATION_CLOSURE_BASIS_MISSING",
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
            "verifying_carrier_declared",
            _present(verifying_carrier),
            "verifying carrier declared",
            verifying_carrier,
            "VERIFYING_CARRIER_MISSING",
        ),
        _check(
            "original_carrier_declared",
            _present(original_carrier),
            "original carrier declared",
            original_carrier,
            "ORIGINAL_CARRIER_MISSING",
        ),
        _check(
            "carrier_independence_basis_declared",
            _present(carrier_independence_basis),
            "carrier independence basis declared",
            carrier_independence_basis,
            "CARRIER_INDEPENDENCE_BASIS_MISSING",
        ),
        _check(
            "verification_evidence_basis_declared",
            _present(verification_evidence_basis),
            "verification evidence basis declared",
            verification_evidence_basis,
            "VERIFICATION_EVIDENCE_BASIS_MISSING",
        ),
        _check(
            "verification_scope_supported",
            not unsupported_scope,
            "supported portable verification scope only",
            list(scope_values),
            "UNSUPPORTED_PORTABLE_VERIFICATION_SCOPE",
        ),
        _check(
            "selected_closure_basis_bounded_closure_only",
            not any(_contains_truthy_key(request, key) for key, _ in COLLAPSE_FIELD_CODES),
            "selected closure basis remains bounded closure only",
            "no capture flags detected",
            "VERIFICATION_REPLACES_SOURCE",
        ),
        _check(
            "selected_reception_closure_did_not_authorize_permission",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "reception_authorized",
                    "follow_on_work_authorized",
                    "continuation_authorized",
                    "publication_flow_opened",
                    "reusable_permission_created",
                    "another_reception_request_authorized",
                )
            ),
            "selected reception closure did not authorize permission",
            "no permission flags detected",
            "VERIFICATION_AUTHORIZES_RECEPTION",
        ),
        _check(
            "source_unreplaced",
            not _contains_truthy_key(request, "source_replaced"),
            "source remains unreplaced",
            request.get("source_replaced"),
            "VERIFICATION_REPLACES_SOURCE",
        ),
    ]

    absence_checks = (
        (
            "verifying_carrier_not_source",
            "carrier_became_source",
            "verifying carrier is not source",
            "VERIFICATION_TREATS_CARRIER_AS_SOURCE",
        ),
        (
            "verifying_carrier_not_authority",
            "carrier_became_authority",
            "verifying carrier is not authority",
            "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY",
        ),
        (
            "original_carrier_not_continuing_authority_by_default",
            "original_carrier_continuing_authority",
            "original carrier is not continuing authority by default",
            "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY",
        ),
        (
            "device_not_authority",
            "device_became_authority",
            "device is not authority",
            "VERIFICATION_TREATS_DEVICE_AS_AUTHORITY",
        ),
        (
            "os_not_authority",
            "os_became_authority",
            "OS is not authority",
            "VERIFICATION_TREATS_OS_AS_AUTHORITY",
        ),
        (
            "vendor_not_authority",
            "vendor_environment_became_authority",
            "vendor is not authority",
            "VERIFICATION_TREATS_VENDOR_AS_AUTHORITY",
        ),
        (
            "account_not_authority",
            "account_became_authority",
            "account is not authority",
            "VERIFICATION_TREATS_ACCOUNT_AS_AUTHORITY",
        ),
        (
            "local_path_not_currentness",
            "local_path_created_currentness",
            "local path is not currentness",
            "VERIFICATION_TREATS_LOCAL_PATH_AS_CURRENTNESS",
        ),
        (
            "latest_file_not_currentness",
            "latest_file_created_currentness",
            "latest file is not currentness",
            "VERIFICATION_TREATS_LATEST_FILE_AS_CURRENTNESS",
        ),
        (
            "recency_not_currentness",
            "recency_created_currentness",
            "recency is not currentness",
            "VERIFICATION_TREATS_RECENCY_AS_CURRENTNESS",
        ),
        (
            "repository_possession_not_currentness",
            "repository_possession_created_currentness",
            "repository possession is not currentness",
            "VERIFICATION_TREATS_REPOSITORY_POSSESSION_AS_CURRENTNESS",
        ),
        (
            "artifact_existence_not_currentness",
            "artifact_existence_created_currentness",
            "artifact existence is not currentness",
            "VERIFICATION_TREATS_ARTIFACT_EXISTENCE_AS_CURRENTNESS",
        ),
        (
            "carrier_possession_not_currentness",
            "carrier_possession_created_currentness",
            "carrier possession is not currentness",
            "VERIFICATION_TREATS_CARRIER_POSSESSION_AS_CURRENTNESS",
        ),
        (
            "archive_possession_not_currentness",
            "archive_possession_created_currentness",
            "archive possession is not currentness",
            "VERIFICATION_TREATS_ARCHIVE_POSSESSION_AS_CURRENTNESS",
        ),
        (
            "human_narration_not_currentness",
            "narration_created_currentness",
            "human narration is not currentness",
            "VERIFICATION_TREATS_NARRATION_AS_CURRENTNESS",
        ),
        (
            "verification_does_not_authorize_reception",
            "reception_authorized",
            "verification does not authorize reception",
            "VERIFICATION_AUTHORIZES_RECEPTION",
        ),
        (
            "verification_does_not_receive_source",
            "source_received",
            "verification does not receive source",
            "VERIFICATION_RECEIVES_SOURCE",
        ),
        (
            "verification_does_not_record_source_receipt",
            "source_receipt_recorded",
            "verification does not record source receipt",
            "VERIFICATION_RECORDS_SOURCE_RECEIPT",
        ),
        (
            "verification_does_not_create_source_receipt",
            "source_receipt_created",
            "verification does not create source receipt",
            "VERIFICATION_CREATES_SOURCE_RECEIPT",
        ),
        (
            "verification_does_not_transfer_source",
            "source_transferred",
            "verification does not transfer source",
            "VERIFICATION_TRANSFERS_SOURCE",
        ),
        (
            "verification_does_not_migrate_source",
            "source_migrated",
            "verification does not migrate source",
            "VERIFICATION_MIGRATES_SOURCE",
        ),
        (
            "verification_does_not_create_adoption",
            "adoption_created",
            "verification does not create adoption",
            "VERIFICATION_CREATES_ADOPTION",
        ),
        (
            "verification_does_not_create_authority",
            "authority_created",
            "verification does not create authority",
            "VERIFICATION_CREATES_AUTHORITY",
        ),
        (
            "verification_does_not_create_currentness",
            "currentness_created",
            "verification does not create currentness",
            "VERIFICATION_CREATES_CURRENTNESS",
        ),
        (
            "verification_does_not_create_standing",
            "standing_created",
            "verification does not create standing",
            "VERIFICATION_CREATES_STANDING",
        ),
        (
            "verification_does_not_create_operation_permission",
            "operation_permission_created",
            "verification does not create operation permission",
            "VERIFICATION_CREATES_OPERATION_PERMISSION",
        ),
        (
            "verification_does_not_create_public_readiness",
            "public_launch_readiness_created",
            "verification does not create public readiness",
            "VERIFICATION_CREATES_PUBLIC_READINESS",
        ),
        (
            "verification_does_not_claim_final_completion",
            "final_completion_claimed",
            "verification does not claim final completion",
            "VERIFICATION_CLAIMS_FINAL_COMPLETION",
        ),
        (
            "verification_does_not_authorize_continuation",
            "continuation_authorized",
            "verification does not authorize continuation",
            "VERIFICATION_AUTHORIZES_CONTINUATION",
        ),
        (
            "verification_does_not_authorize_follow_on_work",
            "follow_on_work_authorized",
            "verification does not authorize follow-on work",
            "VERIFICATION_AUTHORIZES_FOLLOW_ON_WORK",
        ),
        (
            "verification_does_not_open_publication_flow",
            "publication_flow_opened",
            "verification does not open publication flow",
            "VERIFICATION_OPENS_PUBLICATION_FLOW",
        ),
        (
            "verification_does_not_create_reusable_permission",
            "reusable_permission_created",
            "verification does not create reusable permission",
            "VERIFICATION_CREATES_REUSABLE_PERMISSION",
        ),
        (
            "verification_does_not_authorize_another_reception_request",
            "another_reception_request_authorized",
            "verification does not authorize another reception request",
            "VERIFICATION_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
        ),
        (
            "verification_does_not_authorize_derivative_reception",
            "derivative_reception_authorized",
            "verification does not authorize derivative reception",
            "VERIFICATION_AUTHORIZES_DERIVATIVE_RECEPTION",
        ),
        (
            "verification_does_not_authorize_vessel_relation",
            "vessel_relation_authorized",
            "verification does not authorize vessel relation",
            "VERIFICATION_AUTHORIZES_VESSEL_RELATION",
        ),
        (
            "verification_does_not_create_runtime_hosting",
            "runtime_hosting_created",
            "verification does not create runtime hosting",
            "VERIFICATION_CREATES_RUNTIME_HOSTING",
        ),
        (
            "verification_does_not_create_deployment",
            "deployment_created",
            "verification does not create deployment",
            "VERIFICATION_CREATES_DEPLOYMENT",
        ),
        (
            "verification_does_not_create_public_release",
            "public_release_created",
            "verification does not create public release",
            "VERIFICATION_CREATES_PUBLIC_RELEASE",
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


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    request_malformed_code: str | None = None,
) -> dict[str, Any]:
    source_body_basis, source_body_basis_path, source_body_basis_load_code = (
        _load_selected_source_body_basis(request)
    )
    reception_closure_basis, reception_closure_path, reception_closure_load_code = (
        _load_selected_reception_closure_basis(request)
    )
    terminal_summary_basis = _load_terminal_summary_basis(request)

    selected_closure_basis = copy.deepcopy(request.get("selected_closure_basis"))
    distributed_operation_basis = _first_present(
        request.get("selected_distributed_operation_terminal_summary"),
        request.get("selected_distributed_operation_closure_basis"),
    )
    current_body_basis = _first_present(
        request.get("selected_current_body_basis"),
        request.get("selected_current_body_conformance_basis"),
        request.get("selected_current_self_orientation_basis"),
    )
    required_source_surfaces = _surface_value(request, "required_source_surfaces")
    required_spec_surfaces = _surface_value(request, "required_spec_surfaces")
    required_resolver_surfaces = _surface_value(request, "required_resolver_surfaces")
    required_test_surfaces = _surface_value(request, "required_test_surfaces")
    required_artifact_roots = _surface_value(request, "required_artifact_roots")
    required_closure_artifacts = _surface_value(request, "required_closure_artifacts")
    verification_evidence_basis = request.get("verification_evidence_basis")
    carrier_independence_basis = request.get("carrier_independence_basis")
    verifying_carrier = _normalize_basis(request.get("verifying_carrier"), "verifying_carrier_reference")
    original_carrier = _normalize_basis(request.get("original_carrier"), "original_carrier_reference")
    scope_values = _scope_values(request.get("verification_scope"))

    block_code = request_malformed_code or _determine_block_code(
        request,
        source_body_basis,
        source_body_basis_load_code,
        selected_closure_basis,
        reception_closure_basis,
        reception_closure_load_code,
        terminal_summary_basis,
        distributed_operation_basis,
        current_body_basis,
        required_source_surfaces,
        required_spec_surfaces,
        required_resolver_surfaces,
        required_test_surfaces,
        required_artifact_roots,
        required_closure_artifacts,
        verifying_carrier,
        original_carrier,
        carrier_independence_basis,
        verification_evidence_basis,
        scope_values,
    )

    requested_outcome = request.get("requested_verification_outcome") or OUTCOME_RECORDED
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("portable_verification_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = requested_outcome
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED"

    checks = _build_checks(
        request,
        source_body_basis,
        selected_closure_basis,
        reception_closure_basis,
        terminal_summary_basis,
        distributed_operation_basis,
        current_body_basis,
        required_source_surfaces,
        required_spec_surfaces,
        required_resolver_surfaces,
        required_test_surfaces,
        required_artifact_roots,
        required_closure_artifacts,
        verifying_carrier,
        original_carrier,
        carrier_independence_basis,
        verification_evidence_basis,
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
                    "portable_verification_review_blocked",
                    False,
                    "non-blocked portable verification review",
                    block_code,
                    block_code,
                )
            )

    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    passed_count = len(checks) - failed_count
    if outcome == OUTCOME_RECORDED and failed_count != 0:
        outcome = OUTCOME_BLOCKED
        block_code = block_code or "SELECTED_SOURCE_BODY_BASIS_MISSING"

    source_body_basis_id = _first_present(
        request.get("selected_source_body_basis_id"),
        _basis_id(source_body_basis),
    )
    source_body_basis_reference = _first_present(
        request.get("selected_source_body_basis_reference"),
        _basis_reference(source_body_basis),
    )
    closure_artifact_id = _closure_artifact_id(request, reception_closure_basis)
    closure_artifact_outcome = _closure_artifact_outcome(request, reception_closure_basis)

    verifying_carrier_id = _carrier_value(verifying_carrier, "verifying_carrier_id", "id")
    verifying_carrier_type = _first_present(
        _carrier_value(verifying_carrier, "verifying_carrier_type", "type"),
        request.get("verifying_carrier_type"),
    )
    verifying_carrier_reference = _first_present(
        _carrier_value(verifying_carrier, "verifying_carrier_reference", "reference"),
        _carrier_value(verifying_carrier, "verifying_carrier_id", "id"),
    )
    original_carrier_id = _carrier_value(original_carrier, "original_carrier_id", "id")
    original_carrier_type = _first_present(
        _carrier_value(original_carrier, "original_carrier_type", "type"),
        request.get("original_carrier_type"),
    )
    original_carrier_reference = _first_present(
        _carrier_value(original_carrier, "original_carrier_reference", "reference"),
        _carrier_value(original_carrier, "original_carrier_id", "id"),
    )

    result_id_seed = _first_present(
        request.get("portable_verification_request_id"),
        source_body_basis_id,
        closure_artifact_id,
    )
    result_id = f"{_safe_component(result_id_seed)}__portable_source_body_verification_result"
    non_claims = _build_non_claims(outcome)
    recorded = outcome == OUTCOME_RECORDED

    selected_source_body_basis_section = {
        "selected_source_body_basis_id": source_body_basis_id,
        "selected_source_body_basis_reference": source_body_basis_reference,
        "selected_source_body_basis_path": source_body_basis_path,
        "selected_source_body_closure_basis": copy.deepcopy(selected_closure_basis),
        "selected_source_body_reception_closure_basis": copy.deepcopy(reception_closure_basis),
        "selected_source_body_reception_terminal_summary": copy.deepcopy(
            terminal_summary_basis
        ),
        "selected_distributed_operation_closure_terminal_basis": copy.deepcopy(
            distributed_operation_basis
        ),
        "selected_current_body_conformance_orientation_basis": copy.deepcopy(
            current_body_basis
        ),
        "required_source_surfaces": copy.deepcopy(required_source_surfaces),
        "required_spec_surfaces": copy.deepcopy(required_spec_surfaces),
        "required_resolver_surfaces": copy.deepcopy(required_resolver_surfaces),
        "required_test_surfaces": copy.deepcopy(required_test_surfaces),
        "required_artifact_roots": copy.deepcopy(required_artifact_roots),
        "required_closure_artifacts": copy.deepcopy(required_closure_artifacts),
        "selected_corrected_closure_artifacts": copy.deepcopy(
            request.get("selected_corrected_closure_artifacts")
        ),
        "selected_failed_input_evidence_artifacts": copy.deepcopy(
            request.get("selected_failed_input_evidence_artifacts")
        ),
        "failed_input_evidence_posture": copy.deepcopy(
            request.get("failed_input_evidence_posture")
        ),
        "selected_basis_remains_bounded_evidence_only": True,
        "selected_basis_does_not_create_source_transfer": True,
        "selected_basis_does_not_create_source_migration": True,
        "selected_basis_does_not_create_currentness": True,
        "selected_basis_does_not_create_carrier_authority": True,
        "selected_basis_does_not_authorize_next_work": True,
        "raw_selected_source_body_basis": copy.deepcopy(source_body_basis),
    }

    verifying_carrier_section = {
        "verifying_carrier_id": verifying_carrier_id,
        "verifying_carrier_name": _first_present(
            _value_at(verifying_carrier, ("verifying_carrier_name",)),
            _value_at(verifying_carrier, ("name",)),
        ),
        "verifying_carrier_reference": verifying_carrier_reference,
        "verifying_carrier_type": verifying_carrier_type,
        "verifying_carrier_declared": _present(verifying_carrier),
        "verifying_carrier_may_hold_evidence": True,
        "verifying_carrier_may_check_evidence": True,
        "verifying_carrier_is_not_source": True,
        "verifying_carrier_is_not_authority": True,
        "verifying_carrier_is_not_current": True,
        "verifying_carrier_does_not_replace_source": True,
        "verifying_carrier_does_not_receive_source": True,
        "verifying_carrier_does_not_create_source_receipt": True,
        "verifying_carrier_does_not_create_currentness": True,
        "verifying_carrier_does_not_create_operation_permission": True,
        "verifying_carrier_does_not_create_public_readiness": True,
        "verifying_carrier_does_not_authorize_continuation": True,
        "verifying_carrier_does_not_create_reusable_permission": True,
        "verifying_carrier_does_not_authorize_another_reception_request": True,
        "raw_verifying_carrier": copy.deepcopy(verifying_carrier),
    }

    original_carrier_section = {
        "original_carrier_id": original_carrier_id,
        "original_carrier_name": _first_present(
            _value_at(original_carrier, ("original_carrier_name",)),
            _value_at(original_carrier, ("name",)),
        ),
        "original_carrier_reference": original_carrier_reference,
        "original_carrier_type": original_carrier_type,
        "original_carrier_declared": _present(original_carrier),
        "original_carrier_is_not_continuing_authority_by_default": True,
        "original_carrier_is_not_source_merely_because_it_was_original": True,
        "original_carrier_possession_is_not_currentness": True,
        "original_carrier_path_recency_vendor_account_posture_does_not_create_authority": True,
        "raw_original_carrier": copy.deepcopy(original_carrier),
    }

    required_surfaces_section = {
        "required_source_surfaces": copy.deepcopy(required_source_surfaces),
        "required_spec_surfaces": copy.deepcopy(required_spec_surfaces),
        "required_resolver_surfaces": copy.deepcopy(required_resolver_surfaces),
        "required_test_surfaces": copy.deepcopy(required_test_surfaces),
        "required_artifact_roots": copy.deepcopy(required_artifact_roots),
        "required_closure_artifacts": copy.deepcopy(required_closure_artifacts),
        "selected_terminal_summaries": copy.deepcopy(terminal_summary_basis),
        "selected_corrected_closure_artifacts": copy.deepcopy(
            request.get("selected_corrected_closure_artifacts")
        ),
        "selected_failed_input_evidence_artifacts": copy.deepcopy(
            request.get("selected_failed_input_evidence_artifacts")
        ),
        "manifest_candidate_basis": copy.deepcopy(request.get("manifest_candidate_basis")),
        "checksum_candidate_basis": copy.deepcopy(request.get("checksum_candidate_basis")),
        "signature_candidate_basis": copy.deepcopy(request.get("signature_candidate_basis")),
        "manifest_checksum_signature_are_future_evidence_language_only": True,
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_currentness_by_existence": True,
        "surfaces_do_not_create_permission_by_existence": True,
    }

    verification_evidence_basis_section = {
        "verification_evidence_basis_as_supplied": copy.deepcopy(verification_evidence_basis),
        "declared_evidence_classes": copy.deepcopy(request.get("declared_evidence_classes")),
        "selected_source_body_basis": copy.deepcopy(source_body_basis),
        "selected_reception_closure_basis": copy.deepcopy(reception_closure_basis),
        "selected_terminal_summary_basis": copy.deepcopy(terminal_summary_basis),
        "carrier_independent_verification_evidence": True,
        "verification_surface_readability": copy.deepcopy(
            request.get("verification_surface_readability")
        ),
        "manifest_candidate_basis": copy.deepcopy(request.get("manifest_candidate_basis")),
        "checksum_candidate_basis": copy.deepcopy(request.get("checksum_candidate_basis")),
        "signature_candidate_basis": copy.deepcopy(request.get("signature_candidate_basis")),
        "evidence_does_not_replace_source": True,
        "evidence_does_not_make_carrier_source": True,
        "evidence_does_not_create_currentness": True,
        "evidence_does_not_create_transfer_migration_source_receipt_authorization_deployment_public_release_runtime_hosting": True,
    }

    carrier_independence_basis_section = {
        "carrier_independence_basis_as_supplied": copy.deepcopy(
            carrier_independence_basis
        ),
        "no_carrier_authority": True,
        "no_device_authority": True,
        "no_operating_system_authority": True,
        "no_vendor_authority": True,
        "no_account_authority": True,
        "no_local_path_currentness": True,
        "no_latest_file_currentness": True,
        "no_recency_currentness": True,
        "no_repository_possession_currentness": True,
        "no_artifact_existence_currentness": True,
        "no_carrier_possession_currentness": True,
        "no_archive_possession_currentness": True,
        "no_narrator_trust_currentness": True,
        "source_is_not_replaced_by_carrier_copy_archive_path_manifest_checksum_repository": True,
        "original_carrier_is_not_sovereign_by_default": True,
        "verifying_carrier_is_not_source_or_authority": True,
    }

    verification_scope_section = {
        "selected_verification_scope_values": list(scope_values),
        "unsupported_verification_scope_values": [
            value
            for value in scope_values
            if value not in SUPPORTED_PORTABLE_VERIFICATION_SCOPE
        ],
        "all_selected_scope_values_supported": all(
            value in SUPPORTED_PORTABLE_VERIFICATION_SCOPE for value in scope_values
        ),
        "supported_verification_scope_values": sorted(SUPPORTED_PORTABLE_VERIFICATION_SCOPE),
        "portable_source_body_verification_only": True,
        "verification_is_not_transfer": True,
        "verification_is_not_migration": True,
        "verification_is_not_source_receipt": True,
        "verification_is_not_reception_authorization": True,
        "verification_is_not_deployment": True,
        "verification_is_not_runtime_hosting": True,
        "verification_is_not_publication": True,
        "verification_is_not_adoption": True,
        "verification_is_not_authority": True,
        "verification_is_not_currentness": True,
        "verifying_carrier_is_not_source": True,
        "verifying_carrier_is_not_authority": True,
        "device_is_not_authority": True,
        "os_is_not_authority": True,
        "vendor_is_not_authority": True,
        "local_path_is_not_currentness": True,
        "latest_file_is_not_currentness": True,
        "repository_copy_is_not_body": True,
        "narration_is_not_currentness": True,
        "no_operation_permission": True,
        "no_public_readiness": True,
        "no_final_completion": True,
        "no_continuation_authorized": True,
        "no_reusable_permission": True,
    }

    verification_statement = {
        "portable_source_body_verification_recorded": recorded,
        "portable_source_body_basis_verified": recorded,
        "carrier_independent_verification_recorded": recorded,
        "selected_source_body_basis_preserved": source_body_basis is not None,
        "selected_closure_basis_preserved": _present(selected_closure_basis),
        "selected_reception_closure_basis_preserved": reception_closure_basis is not None,
        "selected_terminal_summary_basis_preserved": _present(terminal_summary_basis),
        "required_surfaces_preserved": all(
            _present(value)
            for value in (
                required_source_surfaces,
                required_spec_surfaces,
                required_resolver_surfaces,
                required_test_surfaces,
                required_artifact_roots,
                required_closure_artifacts,
            )
        ),
        "verification_evidence_basis_declared": _present(verification_evidence_basis),
        "carrier_independence_basis_declared": _present(carrier_independence_basis),
        "verifying_carrier_declared": _present(verifying_carrier),
        "original_carrier_declared": _present(original_carrier),
        "verification_only_posture": True,
        "carrier_independent_verification_only": True,
        "verifying_carrier_is_not_source": True,
        "verifying_carrier_is_not_authority": True,
        "original_carrier_is_not_continuing_authority_by_default": True,
        "device_is_not_authority": True,
        "os_is_not_authority": True,
        "vendor_is_not_authority": True,
        "account_is_not_authority": True,
        "local_path_is_not_currentness": True,
        "latest_file_is_not_currentness": True,
        "recency_is_not_currentness": True,
        "repository_possession_is_not_currentness": True,
        "artifact_existence_is_not_currentness": True,
        "carrier_possession_is_not_currentness": True,
        "archive_possession_is_not_currentness": True,
        "narration_is_not_currentness": True,
        "verification_is_not_transfer": True,
        "verification_is_not_migration": True,
        "verification_is_not_source_receipt": True,
        "verification_is_not_reception_authorization": True,
        "verification_is_not_deployment": True,
        "verification_is_not_runtime_hosting": True,
        "verification_is_not_publication": True,
        "verification_is_not_adoption": True,
        "verification_is_not_authority": True,
        "verification_is_not_currentness": True,
    }
    for key in OUTPUT_FALSE_POSTURE:
        verification_statement[key] = False

    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": copy.deepcopy(request.get("additional_basis_context"))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else None,
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
        "does_not_create_manifest_checksum_packet_command_runtime_deployment_public_release_operation_permission_continuation_reusable_permission_derivative_reception_vessel_relation_or_follow_on_work": True,
    }

    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": copy.deepcopy(request.get("not_recorded_basis"))
        if outcome == OUTCOME_NOT_RECORDED
        else None,
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

    result: dict[str, Any] = {
        "portable_source_body_verification_metadata": {
            "portable_source_body_verification_result_id": result_id,
            "portable_source_body_verification_result_type": "portable_source_body_verification_boundary_result",
            "portable_source_body_verification_result_version": RESULT_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_portable_verification_question": {
            "portable_verification_request_id": request.get(
                "portable_verification_request_id"
            ),
            "portable_verification_question": request.get(
                "portable_verification_question"
            ),
            "portable_verification_intent": request.get(
                "portable_verification_intent"
            ),
            "declared_portable_verification_request_path": request_path,
            "selected_source_body_basis_id": source_body_basis_id,
            "selected_source_body_basis_reference": source_body_basis_reference,
            "selected_reception_closure_artifact_id": closure_artifact_id,
            "selected_reception_closure_artifact_outcome": closure_artifact_outcome,
            "selected_reception_closure_artifact_path": reception_closure_path,
            "selected_terminal_summary_basis_reference": _basis_reference(
                terminal_summary_basis,
                "selected_terminal_summary_basis_reference",
            ),
            "selected_reception_terminal_summary_path": request.get(
                "selected_reception_terminal_summary_path"
            ),
            "verifying_carrier_id": verifying_carrier_id,
            "verifying_carrier_type": verifying_carrier_type,
            "verifying_carrier_reference": verifying_carrier_reference,
            "original_carrier_id": original_carrier_id,
            "original_carrier_type": original_carrier_type,
            "original_carrier_reference": original_carrier_reference,
            "verification_is_not_transfer": True,
            "verification_is_not_migration": True,
            "verification_is_not_source_receipt": True,
            "verification_is_not_reception_authorization": True,
            "verification_is_not_deployment": True,
            "verification_is_not_runtime_hosting": True,
            "verification_is_not_publication": True,
            "verification_is_not_adoption": True,
            "verification_is_not_authority": True,
            "verification_is_not_currentness": True,
            "verification_does_not_authorize_continuation": True,
            "verification_does_not_authorize_follow_on_work": True,
            "verification_does_not_create_reusable_permission": True,
            "verification_does_not_authorize_another_reception_request": True,
        },
        "selected_source_body_basis": selected_source_body_basis_section,
        "selected_closure_basis": {
            "selected_closure_basis_as_supplied": copy.deepcopy(selected_closure_basis),
            "selected_closure_basis_preserved": _present(selected_closure_basis),
            "selected_closure_basis_remains_bounded_closure_only": True,
            "selected_closure_basis_does_not_authorize_permission": True,
            "selected_closure_basis_does_not_create_currentness": True,
        },
        "selected_reception_closure_basis": {
            "selected_reception_closure_artifact_id": closure_artifact_id,
            "selected_reception_closure_artifact_outcome": closure_artifact_outcome,
            "selected_reception_closure_artifact_path": reception_closure_path,
            "selected_reception_closure_basis_preserved": reception_closure_basis
            is not None,
            "selected_reception_closure_basis_did_not_authorize_permission": True,
            "selected_reception_closure_basis_is_evidence_only": True,
            "raw_selected_reception_closure_basis": copy.deepcopy(
                reception_closure_basis
            ),
        },
        "selected_terminal_summary_basis": {
            "selected_terminal_summary_basis_reference": _basis_reference(
                terminal_summary_basis,
                "selected_terminal_summary_basis_reference",
            ),
            "selected_reception_terminal_summary_path": request.get(
                "selected_reception_terminal_summary_path"
            ),
            "selected_terminal_summary_basis_preserved": _present(
                terminal_summary_basis
            ),
            "selected_terminal_summary_basis_is_evidence_only": True,
            "selected_terminal_summary_basis_does_not_create_authority": True,
            "selected_terminal_summary_basis_does_not_create_currentness": True,
            "raw_selected_terminal_summary_basis": copy.deepcopy(
                terminal_summary_basis
            ),
        },
        "verifying_carrier": verifying_carrier_section,
        "original_carrier": original_carrier_section,
        "required_surfaces": required_surfaces_section,
        "verification_evidence_basis": verification_evidence_basis_section,
        "carrier_independence_basis": carrier_independence_basis_section,
        "verification_scope": verification_scope_section,
        "verification_checks": checks,
        "verification_statement": verification_statement,
        "verification_non_meaning": _build_verification_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason") or block_code),
    }
    result["portable_source_body_verification_summary"] = (
        build_portable_source_body_verification_summary(result)
    )
    result["portable_source_body_verification_summary"][
        "passed_check_count"
    ] = passed_count
    result["portable_source_body_verification_summary"][
        "failed_check_count"
    ] = failed_count
    return result


def resolve_portable_source_body_verification_boundary(
    declared_portable_verification_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared portable source-body verification request."""

    if declared_portable_verification_request is None:
        return _build_result({})
    if not isinstance(declared_portable_verification_request, Mapping):
        return _build_result(
            {},
            request_malformed_code="DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED",
        )
    return _build_result(copy.deepcopy(dict(declared_portable_verification_request)))


def resolve_portable_source_body_verification_boundary_from_path(
    declared_portable_verification_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve a portable source-body verification request from a JSON object path."""

    path = Path(declared_portable_verification_request_path)
    loaded, failure = _read_json_object(path)
    if failure == "unreadable":
        return _build_result(
            {"portable_verification_question": "declared portable verification request unreadable"},
            request_path=str(path),
            request_malformed_code="DECLARED_PORTABLE_VERIFICATION_REQUEST_UNREADABLE",
        )
    if failure == "malformed":
        return _build_result(
            {"portable_verification_question": "declared portable verification request malformed"},
            request_path=str(path),
            request_malformed_code="DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED",
        )
    if loaded is None:
        return _build_result(
            {"portable_verification_question": "declared portable verification request unreadable"},
            request_path=str(path),
            request_malformed_code="DECLARED_PORTABLE_VERIFICATION_REQUEST_UNREADABLE",
        )
    return _build_result(copy.deepcopy(loaded), request_path=str(path))


def build_portable_source_body_verification_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a portable verification boundary result."""

    statement = result.get("verification_statement", {})
    selected = result.get("selected_source_body_basis", {})
    closure = result.get("selected_reception_closure_basis", {})
    terminal = result.get("selected_terminal_summary_basis", {})
    verifying = result.get("verifying_carrier", {})
    original = result.get("original_carrier", {})
    declared = result.get("declared_portable_verification_question", {})
    block = result.get("block", {})
    checks = result.get("verification_checks", [])
    non_claims = result.get("non_claims", {})
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes)):
        passed_count = sum(
            1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
        )
        failed_count = sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    else:
        passed_count = 0
        failed_count = 0
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "portable_verification_request_id": declared.get("portable_verification_request_id")
        if isinstance(declared, Mapping)
        else None,
        "portable_verification_question": declared.get("portable_verification_question")
        if isinstance(declared, Mapping)
        else None,
        "portable_verification_intent": declared.get("portable_verification_intent")
        if isinstance(declared, Mapping)
        else None,
        "selected_source_body_basis_id": selected.get("selected_source_body_basis_id")
        if isinstance(selected, Mapping)
        else None,
        "selected_source_body_basis_reference": selected.get(
            "selected_source_body_basis_reference"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_reception_closure_artifact_id": closure.get(
            "selected_reception_closure_artifact_id"
        )
        if isinstance(closure, Mapping)
        else None,
        "selected_reception_closure_artifact_outcome": closure.get(
            "selected_reception_closure_artifact_outcome"
        )
        if isinstance(closure, Mapping)
        else None,
        "selected_reception_closure_artifact_path": closure.get(
            "selected_reception_closure_artifact_path"
        )
        if isinstance(closure, Mapping)
        else None,
        "selected_terminal_summary_basis_reference": terminal.get(
            "selected_terminal_summary_basis_reference"
        )
        if isinstance(terminal, Mapping)
        else None,
        "selected_terminal_summary_basis_path": terminal.get(
            "selected_reception_terminal_summary_path"
        )
        if isinstance(terminal, Mapping)
        else None,
        "verifying_carrier_id": verifying.get("verifying_carrier_id")
        if isinstance(verifying, Mapping)
        else None,
        "verifying_carrier_type": verifying.get("verifying_carrier_type")
        if isinstance(verifying, Mapping)
        else None,
        "verifying_carrier_reference": verifying.get("verifying_carrier_reference")
        if isinstance(verifying, Mapping)
        else None,
        "original_carrier_id": original.get("original_carrier_id")
        if isinstance(original, Mapping)
        else None,
        "original_carrier_type": original.get("original_carrier_type")
        if isinstance(original, Mapping)
        else None,
        "original_carrier_reference": original.get("original_carrier_reference")
        if isinstance(original, Mapping)
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "portable_verification_recorded": bool(
            isinstance(statement, Mapping)
            and statement.get("portable_source_body_verification_recorded") is True
        ),
        "portable_source_body_basis_verified": bool(
            isinstance(statement, Mapping)
            and statement.get("portable_source_body_basis_verified") is True
        ),
        "carrier_independent_verification_recorded": bool(
            isinstance(statement, Mapping)
            and statement.get("carrier_independent_verification_recorded") is True
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_source_body_basis_preserved": statement.get(
            "selected_source_body_basis_preserved"
        )
        if isinstance(statement, Mapping)
        else None,
        "selected_closure_basis_preserved": statement.get("selected_closure_basis_preserved")
        if isinstance(statement, Mapping)
        else None,
        "selected_reception_closure_basis_preserved": statement.get(
            "selected_reception_closure_basis_preserved"
        )
        if isinstance(statement, Mapping)
        else None,
        "selected_terminal_summary_basis_preserved": statement.get(
            "selected_terminal_summary_basis_preserved"
        )
        if isinstance(statement, Mapping)
        else None,
        "required_surfaces_preserved": statement.get("required_surfaces_preserved")
        if isinstance(statement, Mapping)
        else None,
        "verification_evidence_basis_declared": statement.get(
            "verification_evidence_basis_declared"
        )
        if isinstance(statement, Mapping)
        else None,
        "carrier_independence_basis_declared": statement.get(
            "carrier_independence_basis_declared"
        )
        if isinstance(statement, Mapping)
        else None,
        "verification_only_posture": statement.get("verification_only_posture")
        if isinstance(statement, Mapping)
        else None,
        "verifying_carrier_not_source": statement.get("verifying_carrier_is_not_source")
        if isinstance(statement, Mapping)
        else None,
        "verifying_carrier_not_authority": statement.get(
            "verifying_carrier_is_not_authority"
        )
        if isinstance(statement, Mapping)
        else None,
        "original_carrier_not_continuing_authority_by_default": statement.get(
            "original_carrier_is_not_continuing_authority_by_default"
        )
        if isinstance(statement, Mapping)
        else None,
        "device_os_vendor_account_not_authority": all(
            statement.get(key) is True
            for key in (
                "device_is_not_authority",
                "os_is_not_authority",
                "vendor_is_not_authority",
                "account_is_not_authority",
            )
        )
        if isinstance(statement, Mapping)
        else None,
        "path_latest_recency_repository_artifact_carrier_archive_narration_not_currentness": all(
            statement.get(key) is True
            for key in (
                "local_path_is_not_currentness",
                "latest_file_is_not_currentness",
                "recency_is_not_currentness",
                "repository_possession_is_not_currentness",
                "artifact_existence_is_not_currentness",
                "carrier_possession_is_not_currentness",
                "archive_possession_is_not_currentness",
                "narration_is_not_currentness",
            )
        )
        if isinstance(statement, Mapping)
        else None,
        "verification_not_transfer_migration_source_receipt_reception_authorization_deployment_runtime_publication_adoption_authority_currentness": all(
            statement.get(key) is True
            for key in (
                "verification_is_not_transfer",
                "verification_is_not_migration",
                "verification_is_not_source_receipt",
                "verification_is_not_reception_authorization",
                "verification_is_not_deployment",
                "verification_is_not_runtime_hosting",
                "verification_is_not_publication",
                "verification_is_not_adoption",
                "verification_is_not_authority",
                "verification_is_not_currentness",
            )
        )
        if isinstance(statement, Mapping)
        else None,
        "no_source_replaced_transferred_migrated_received": all(
            non_claims.get(key) is False
            for key in ("source_replaced", "source_transferred", "source_migrated", "source_received")
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_source_receipt_recorded": non_claims.get("source_receipt_recorded") is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_adoption_authority_currentness_standing": all(
            non_claims.get(key) is False
            for key in ("adoption_created", "authority_created", "currentness_created", "standing_created")
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_operation_permission_public_readiness_final_completion": all(
            non_claims.get(key) is False
            for key in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_continuation_publication_flow_reusable_permission": all(
            non_claims.get(key) is False
            for key in (
                "continuation_authorized",
                "publication_flow_opened",
                "reusable_permission_created",
            )
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_another_reception_request_authorized": non_claims.get(
            "another_reception_request_authorized"
        )
        is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_derivative_reception_vessel_relation": all(
            non_claims.get(key) is False
            for key in ("derivative_reception_authorized", "vessel_relation_authorized")
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_runtime_hosting_deployment_public_release": all(
            non_claims.get(key) is False
            for key in ("runtime_hosting_created", "deployment_created", "public_release_created")
        )
        if isinstance(non_claims, Mapping)
        else None,
        "key_non_claims": copy.deepcopy(non_claims)
        if isinstance(non_claims, Mapping)
        else {},
    }


def write_portable_source_body_verification_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded additive portable verification result JSON artifact."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationBoundaryError(
            "portable verification result must be a mapping"
        )
    if output_path is None:
        metadata = result.get("portable_source_body_verification_metadata", {})
        result_id = (
            metadata.get("portable_source_body_verification_result_id")
            if isinstance(metadata, Mapping)
            else None
        )
        filename = f"{_safe_component(result_id)}.json"
        path = PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    candidate = path
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix or ".json"
        index = 1
        while candidate.exists():
            candidate = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            index += 1
    candidate.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_portable_source_body_verification_request(
    portable_verification_request_id: str,
    portable_verification_question: str,
    selected_source_body_basis: Mapping[str, Any] | str,
    selected_closure_basis: Mapping[str, Any] | str,
    selected_reception_closure_basis: Mapping[str, Any] | str,
    selected_terminal_summary_basis: Mapping[str, Any] | str,
    verifying_carrier: Mapping[str, Any] | str,
    original_carrier: Mapping[str, Any] | str,
    required_surfaces: Mapping[str, Any] | str,
    verification_evidence_basis: Mapping[str, Any] | str,
    carrier_independence_basis: Mapping[str, Any] | str,
    verification_scope: Sequence[str] | Mapping[str, Any],
    portable_verification_intent: str = INTENT_RECORD,
    *,
    selected_source_body_basis_path: str | None = None,
    selected_reception_closure_artifact_path: str | None = None,
    selected_reception_closure_artifact_id: str | None = None,
    selected_reception_closure_artifact_outcome: str | None = None,
    requested_verification_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    """Build a declared portable verification request with false non-claims."""

    required_surfaces_copy = copy.deepcopy(required_surfaces)
    if isinstance(required_surfaces_copy, Mapping):
        required_source_surfaces = required_surfaces_copy.get("required_source_surfaces")
        required_spec_surfaces = required_surfaces_copy.get("required_spec_surfaces")
        required_resolver_surfaces = required_surfaces_copy.get("required_resolver_surfaces")
        required_test_surfaces = required_surfaces_copy.get("required_test_surfaces")
        required_artifact_roots = required_surfaces_copy.get("required_artifact_roots")
        required_closure_artifacts = required_surfaces_copy.get("required_closure_artifacts")
    else:
        required_source_surfaces = required_surfaces_copy
        required_spec_surfaces = required_surfaces_copy
        required_resolver_surfaces = required_surfaces_copy
        required_test_surfaces = required_surfaces_copy
        required_artifact_roots = required_surfaces_copy
        required_closure_artifacts = required_surfaces_copy

    request: dict[str, Any] = {
        "portable_verification_request_id": portable_verification_request_id,
        "portable_verification_question": portable_verification_question,
        "portable_verification_intent": portable_verification_intent,
        "selected_closure_basis": copy.deepcopy(selected_closure_basis),
        "selected_terminal_summary_basis": copy.deepcopy(selected_terminal_summary_basis),
        "verifying_carrier": copy.deepcopy(verifying_carrier),
        "original_carrier": copy.deepcopy(original_carrier),
        "required_surfaces": required_surfaces_copy,
        "required_source_surfaces": copy.deepcopy(required_source_surfaces),
        "required_spec_surfaces": copy.deepcopy(required_spec_surfaces),
        "required_resolver_surfaces": copy.deepcopy(required_resolver_surfaces),
        "required_test_surfaces": copy.deepcopy(required_test_surfaces),
        "required_artifact_roots": copy.deepcopy(required_artifact_roots),
        "required_closure_artifacts": copy.deepcopy(required_closure_artifacts),
        "verification_evidence_basis": copy.deepcopy(verification_evidence_basis),
        "carrier_independence_basis": copy.deepcopy(carrier_independence_basis),
        "verification_scope": copy.deepcopy(verification_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "requested_verification_outcome": requested_verification_outcome,
    }
    for key in OUTPUT_FALSE_POSTURE:
        request[key] = False
    if selected_source_body_basis_path is not None:
        request["selected_source_body_basis_path"] = selected_source_body_basis_path
    else:
        request["selected_source_body_basis"] = copy.deepcopy(selected_source_body_basis)
    if selected_reception_closure_artifact_path is not None:
        request["selected_reception_closure_artifact_path"] = (
            selected_reception_closure_artifact_path
        )
    else:
        request["selected_reception_closure_basis"] = copy.deepcopy(
            selected_reception_closure_basis
        )
    if selected_reception_closure_artifact_id is not None:
        request["selected_reception_closure_artifact_id"] = (
            selected_reception_closure_artifact_id
        )
    if selected_reception_closure_artifact_outcome is not None:
        request["selected_reception_closure_artifact_outcome"] = (
            selected_reception_closure_artifact_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = copy.deepcopy(additional_basis_context)
    if not_recorded_basis is not None:
        request["not_recorded_basis"] = copy.deepcopy(not_recorded_basis)
    return request
