"""Resolve the portable source-body verification command execution boundary.

This resolver answers one question only:

    Can conditions for a future bounded command invocation be recorded without
    executing, invoking, emitting output, creating a result, or creating
    command success?

Execution boundary records future invocation conditions only. It is not command
execution, command invocation, command output, command result, command success,
deployment, runtime hosting, public release, source transfer, source migration,
source receipt, reception authorization, authority, currentness, operation
permission, public readiness, final completion, continuation, reusable
permission, derivative reception, vessel relation, another reception request,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationCommandExecutionBoundaryError(Exception):
    """Raised for hard command execution-boundary failures."""


RESOLVER_MODULE = "resolve_portable_source_body_verification_command_execution_boundary"
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "command_execution_boundary"
)

OUTCOME_RECORDED = "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_RECORDED"
OUTCOME_NOT_RECORDED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_REVIEW_BLOCKED"
)
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY"
)
INTENT_BLOCK = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_REVIEW"
SUPPORTED_COMMAND_EXECUTION_BOUNDARY_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_COMMAND_EXECUTION_BOUNDARY_SCOPE = {
    "COMMAND_EXECUTION_BOUNDARY_ONLY",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "COMMAND_OUTPUT_IS_NOT_SOURCE",
    "COMMAND_RESULT_IS_NOT_AUTHORITY",
    "COMMAND_SUCCESS_IS_NOT_CURRENTNESS",
    "COMMAND_SUCCESS_IS_NOT_FINAL_COMPLETION",
    "EXECUTION_IS_NOT_DEPLOYMENT",
    "EXECUTION_IS_NOT_RUNTIME_HOSTING",
    "EXECUTION_IS_NOT_PUBLIC_RELEASE",
    "EXECUTION_DOES_NOT_AUTHORIZE_CONTINUATION",
    "EXECUTION_DOES_NOT_AUTHORIZE_FOLLOW_ON_WORK",
    "EXECUTION_REQUIRES_REFERENCE_SHAPED_INPUT",
    "EXECUTION_MUST_NOT_MUTATE_ARTIFACTS",
    "EXECUTION_MUST_NOT_EMBED_FULL_PRIOR_ARTIFACTS",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "command_execution_boundary_recorded_as_execution",
    "command_executed",
    "command_invocation_created",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "command_output_became_source",
    "command_result_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "full_prior_artifacts_embedded",
    "prior_artifacts_mutated",
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

ALLOWED_RECORDED_TRUE_FIELDS = (
    "portable_source_body_verification_command_execution_boundary_recorded",
    "command_execution_conditions_declared",
    "command_invocation_must_be_bounded",
    "command_output_must_be_non_authoritative",
    "command_success_must_not_create_currentness",
    "command_success_must_not_claim_final_completion",
)

OUTPUT_FALSE_POSTURE = tuple(
    dict.fromkeys(REQUIRED_FALSE_NON_CLAIMS + ALLOWED_RECORDED_TRUE_FIELDS)
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

FULL_ARTIFACT_BODY_KEYS = {
    "full_artifact_body",
    "raw_artifact",
    "raw_result",
    "embedded_artifact",
    "selected_full_artifact",
    "complete_artifact_body",
}

REFERENCE_RESULT_FIELDS = (
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

COLLAPSE_FIELD_CODES = (
    ("mutation_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
    ("replay_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
    ("merge_performed", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
    ("command_execution_boundary_recorded_as_execution", "COMMAND_EXECUTION_PERFORMED"),
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_created", "COMMAND_EXECUTION_PERFORMED"),
    ("command_authorized_to_run", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_authorized", "COMMAND_EXECUTION_PERFORMED"),
    ("live_verification_authorized", "COMMAND_EXECUTION_PERFORMED"),
    ("live_verification_completed", "COMMAND_SUCCESS_CREATED"),
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invoked", "COMMAND_INVOCATION_CREATED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_output_exists", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_result_exists", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("command_success_exists", "COMMAND_SUCCESS_CREATED"),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("report_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("command_success_treated_as_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    (
        "command_success_claimed_final_completion",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    ),
    (
        "command_success_treated_as_final_completion",
        "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
    ),
    ("command_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifact_mutation_requested", "ARTIFACTS_MUTATED"),
    ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACTS_EMBEDDED"),
    ("full_prior_artifacts_embedding_permitted", "FULL_PRIOR_ARTIFACTS_EMBEDDED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("deployment_requested", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("runtime_hosting_requested", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("public_release_requested", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("final_completion_claimed", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("continuation_requested", "CONTINUATION_AUTHORIZED"),
    ("publication_flow_opened", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("successor_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    ("follow_on_requested", "FOLLOW_ON_WORK_AUTHORIZED"),
)


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _generated_at() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, Mapping):
        return bool(value)
    if isinstance(value, (list, tuple, set)):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if value is False or value is None:
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "created", "authorized"}
    if isinstance(value, (int, float)):
        return value != 0
    return bool(value)


def _is_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() == "false"
    return False


def _value_at(value: Any, keys: Sequence[str]) -> Any:
    current = value
    for key in keys:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _safe_component(value: Any, fallback: str) -> str:
    raw = str(value or fallback).strip() or fallback
    safe = "".join(ch if ch.isalnum() or ch in {"-", "_", "."} else "_" for ch in raw)
    return safe[:160] or fallback


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    request_path = Path(path)
    try:
        parsed = json.loads(request_path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE", str(exc)
    except json.JSONDecodeError as exc:
        return None, "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED", str(exc)
    if not isinstance(parsed, Mapping):
        return (
            None,
            "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            "request JSON must be an object",
        )
    return dict(parsed), None, None


def _contains_key(value: Any, keys: set[str]) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in keys:
                return True
            if _contains_key(nested, keys):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_key(item, keys) for item in value)
    return False


def _contains_truthy_key(value: Any, keys: Sequence[str]) -> bool:
    wanted = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key).lower() in wanted and _truthy(nested):
                return True
            if _contains_truthy_key(nested, keys):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_truthy_key(item, keys) for item in value)
    return False


def _has_full_prior_artifact_body(value: Any) -> bool:
    return _contains_key(value, FULL_ARTIFACT_BODY_KEYS)


def _sanitize_reference_shape(value: Any) -> Any:
    if isinstance(value, Mapping):
        sanitized: dict[str, Any] = {}
        for key, nested in value.items():
            if str(key) in FULL_ARTIFACT_BODY_KEYS:
                continue
            sanitized[str(key)] = _sanitize_reference_shape(nested)
        return sanitized
    if isinstance(value, list):
        return [_sanitize_reference_shape(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_reference_shape(item) for item in value]
    if isinstance(value, str) and len(value) > 2000:
        return value[:2000] + "...[reference-shaped truncation]"
    return _copy(value)


def _basis_id(value: Any) -> Any:
    return _first_present(
        _value_at(value, ("selected_result_id",)),
        _value_at(value, ("result_id",)),
        _value_at(value, ("id",)),
        _value_at(value, ("metadata", "result_id")),
    )


def _basis_path(value: Any) -> Any:
    return _first_present(
        _value_at(value, ("selected_result_path",)),
        _value_at(value, ("result_path",)),
        _value_at(value, ("artifact_path",)),
        _value_at(value, ("file_path",)),
        _value_at(value, ("path",)),
    )


def _basis_outcome(value: Any) -> Any:
    return _first_present(
        _value_at(value, ("selected_result_outcome",)),
        _value_at(value, ("selected_result_status",)),
        _value_at(value, ("result_outcome",)),
        _value_at(value, ("outcome",)),
        _value_at(value, ("status",)),
    )


def _normalize_reference_basis(value: Any) -> dict[str, Any]:
    return {
        "reference_shaped_basis_only": not _has_full_prior_artifact_body(value),
        "basis_shape": "mapping"
        if isinstance(value, Mapping)
        else "sequence"
        if isinstance(value, (list, tuple))
        else "string"
        if isinstance(value, str)
        else type(value).__name__,
        "basis_reference": _sanitize_reference_shape(value),
        "basis_remains_non_authoritative": True,
        "basis_does_not_authorize_execution": True,
        "basis_does_not_create_output_result_success": True,
        "basis_does_not_create_currentness_final_completion_follow_on_work": True,
        "full_prior_artifacts_are_not_embedded": not _has_full_prior_artifact_body(value),
        "prior_artifacts_are_not_mutated": True,
    }


def _scope_values(scope: Any) -> tuple[str, ...]:
    if isinstance(scope, Mapping):
        for key in (
            "scope_values",
            "selected_scope_values",
            "execution_boundary_scope_values",
            "selected_execution_boundary_scope_values",
        ):
            selected = scope.get(key)
            if _present(selected):
                return _scope_values(selected)
        return tuple(str(key) for key, value in scope.items() if _truthy(value))
    if isinstance(scope, str):
        return (scope,) if scope.strip() else ()
    if isinstance(scope, (list, tuple, set)):
        return tuple(str(value) for value in scope if _present(value))
    return ()


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _block(blocked: bool, code: str | None, reason: str | None) -> dict[str, Any]:
    return {
        "blocked": bool(blocked),
        "block_code": code if blocked else None,
        "block_reason": reason if blocked else None,
    }


def _required_non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    return all(key in non_claims and _is_false(non_claims[key]) for key in REQUIRED_FALSE_NON_CLAIMS)


def _collapse_code(request: Mapping[str, Any]) -> str | None:
    if _has_full_prior_artifact_body(request):
        return "FULL_PRIOR_ARTIFACTS_EMBEDDED"
    for field, code in COLLAPSE_FIELD_CODES:
        if _contains_truthy_key(request, (field,)):
            return code
    return None


def _command_module_reference(request: Mapping[str, Any]) -> Any:
    implementation_basis = request.get("selected_command_implementation_basis")
    return _first_present(
        request.get("selected_command_module_reference"),
        _value_at(implementation_basis, ("selected_command_module_reference",)),
        _value_at(implementation_basis, ("implementation_target_candidate",)),
        _value_at(implementation_basis, ("future_implementation_target",)),
        _value_at(implementation_basis, ("implementation_module",)),
        _value_at(implementation_basis, ("module_reference",)),
    )


def _test_surface_reference(request: Mapping[str, Any]) -> Any:
    implementation_basis = request.get("selected_command_implementation_basis")
    return _first_present(
        request.get("selected_test_surface_reference"),
        _value_at(implementation_basis, ("selected_test_surface_reference",)),
        _value_at(implementation_basis, ("test_surface_reference",)),
        _value_at(implementation_basis, ("test_surface",)),
    )


def _selected_basis_section(
    request: Mapping[str, Any],
    value_key: str,
    label: str,
    *,
    result_path_key: str | None = None,
    result_id_key: str | None = None,
    result_status_key: str | None = None,
    terminal_summary_path_key: str | None = None,
) -> dict[str, Any]:
    value = request.get(value_key)
    result_path = request.get(result_path_key) if result_path_key else None
    result_id = request.get(result_id_key) if result_id_key else None
    result_status = request.get(result_status_key) if result_status_key else None
    terminal_summary_path = (
        request.get(terminal_summary_path_key) if terminal_summary_path_key else None
    )
    normalized = _normalize_reference_basis(value)
    return {
        f"{label}_declared": _present(value) or _present(result_path) or _present(result_id),
        f"{label}_preserved": _present(value) or _present(result_path) or _present(result_id),
        "selected_id": _first_present(result_id, _basis_id(value)),
        "selected_path": _first_present(result_path, _basis_path(value)),
        "selected_outcome_or_status": _first_present(result_status, _basis_outcome(value)),
        "selected_terminal_summary_path": terminal_summary_path,
        "selected_basis": normalized,
        "reference_shaped_basis_only": normalized["reference_shaped_basis_only"],
        "basis_remains_non_authoritative": True,
        "basis_does_not_authorize_execution": True,
        "basis_does_not_create_output_result_success": True,
        "basis_does_not_create_currentness_final_completion_follow_on_work": True,
        "full_prior_artifacts_are_not_embedded": normalized[
            "full_prior_artifacts_are_not_embedded"
        ],
        "prior_artifacts_are_not_mutated": True,
    }


def _proposal_section(value: Any, label: str) -> dict[str, Any]:
    return {
        f"{label}_declared": _present(value),
        f"{label}_as_supplied": _sanitize_reference_shape(value),
        "proposal_is_future_condition_only": True,
        "proposal_is_not_execution": True,
        "proposal_is_not_invocation": True,
        "proposal_is_not_output": True,
        "proposal_is_not_result": True,
        "proposal_is_not_success": True,
        "proposal_does_not_authorize_execution": True,
    }


def _limit_section(value: Any, label: str, posture: Any | None = None) -> dict[str, Any]:
    return {
        f"{label}_declared": _present(value),
        f"{label}_as_supplied": _sanitize_reference_shape(value),
        f"{label}_posture": _sanitize_reference_shape(posture) if posture is not None else None,
        "command_execution_not_performed": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_is_not_source": True,
        "command_result_is_not_authority": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "execution_is_not_deployment": True,
        "execution_is_not_runtime_hosting": True,
        "execution_is_not_public_release": True,
        "execution_does_not_authorize_continuation": True,
        "execution_does_not_authorize_follow_on_work": True,
        "execution_requires_reference_shaped_input": True,
        "execution_must_not_mutate_artifacts": True,
        "execution_must_not_embed_full_prior_artifacts": True,
    }


def _execution_boundary_scope_section(scope: Any) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = sorted(set(values) - SUPPORTED_COMMAND_EXECUTION_BOUNDARY_SCOPE)
    selected = set(values)
    return {
        "selected_scope_values": list(values),
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "command_execution_boundary_only": "COMMAND_EXECUTION_BOUNDARY_ONLY" in selected,
        "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED" in selected,
        "command_invocation_not_created": "COMMAND_INVOCATION_NOT_CREATED" in selected,
        "command_output_not_created": "COMMAND_OUTPUT_NOT_CREATED" in selected,
        "command_result_not_created": "COMMAND_RESULT_NOT_CREATED" in selected,
        "command_success_not_created": "COMMAND_SUCCESS_NOT_CREATED" in selected,
        "command_output_not_source": "COMMAND_OUTPUT_IS_NOT_SOURCE" in selected,
        "command_result_not_authority": "COMMAND_RESULT_IS_NOT_AUTHORITY" in selected,
        "command_success_not_currentness": "COMMAND_SUCCESS_IS_NOT_CURRENTNESS" in selected,
        "command_success_not_final_completion": (
            "COMMAND_SUCCESS_IS_NOT_FINAL_COMPLETION" in selected
        ),
        "execution_not_deployment": "EXECUTION_IS_NOT_DEPLOYMENT" in selected,
        "execution_not_runtime_hosting": "EXECUTION_IS_NOT_RUNTIME_HOSTING" in selected,
        "execution_not_public_release": "EXECUTION_IS_NOT_PUBLIC_RELEASE" in selected,
        "execution_does_not_authorize_continuation": (
            "EXECUTION_DOES_NOT_AUTHORIZE_CONTINUATION" in selected
        ),
        "execution_does_not_authorize_follow_on_work": (
            "EXECUTION_DOES_NOT_AUTHORIZE_FOLLOW_ON_WORK" in selected
        ),
        "execution_requires_reference_shaped_input": (
            "EXECUTION_REQUIRES_REFERENCE_SHAPED_INPUT" in selected
        ),
        "execution_must_not_mutate_artifacts": (
            "EXECUTION_MUST_NOT_MUTATE_ARTIFACTS" in selected
        ),
        "execution_must_not_embed_full_prior_artifacts": (
            "EXECUTION_MUST_NOT_EMBED_FULL_PRIOR_ARTIFACTS" in selected
        ),
    }


def _build_checks(
    request: Mapping[str, Any],
    *,
    malformed_code: str | None = None,
) -> list[dict[str, Any]]:
    intent = request.get("command_execution_boundary_intent")
    scope = _execution_boundary_scope_section(request.get("execution_boundary_scope"))
    checks = [
        _check(
            "declared_command_execution_boundary_request_well_formed",
            malformed_code is None,
            "request mapping is readable JSON object when supplied by path",
            malformed_code or "mapping",
            malformed_code or "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
        ),
        _check(
            "execution_boundary_question_declared",
            _present(request.get("command_execution_boundary_question")),
            "execution-boundary question declared",
            request.get("command_execution_boundary_question"),
            "COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
        ),
        _check(
            "execution_boundary_intent_supported",
            intent in SUPPORTED_COMMAND_EXECUTION_BOUNDARY_INTENTS,
            "supported execution-boundary intent",
            intent,
            "COMMAND_EXECUTION_BOUNDARY_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_command_report_basis_declared",
            _present(request.get("selected_command_report_basis")),
            "selected command report basis declared",
            _present(request.get("selected_command_report_basis")),
            "COMMAND_REPORT_BASIS_MISSING",
        ),
        _check(
            "selected_command_implementation_basis_declared",
            _present(request.get("selected_command_implementation_basis")),
            "selected command implementation basis declared",
            _present(request.get("selected_command_implementation_basis")),
            "COMMAND_IMPLEMENTATION_SPEC_MISSING",
        ),
        _check(
            "selected_command_implementation_boundary_basis_declared",
            _present(request.get("selected_command_implementation_boundary_basis")),
            "selected command implementation-boundary basis declared",
            _present(request.get("selected_command_implementation_boundary_basis")),
            "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
        ),
        _check(
            "selected_command_boundary_basis_declared",
            _present(request.get("selected_command_boundary_basis")),
            "selected command-boundary basis declared",
            _present(request.get("selected_command_boundary_basis")),
            "COMMAND_BOUNDARY_BASIS_MISSING",
        ),
        _check(
            "artifact_emission_containment_basis_declared",
            _present(request.get("selected_artifact_emission_containment_basis")),
            "artifact emission containment basis declared",
            _present(request.get("selected_artifact_emission_containment_basis")),
            "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        ),
        _check(
            "evidence_manifest_basis_declared",
            _present(request.get("selected_evidence_manifest_basis")),
            "evidence-manifest basis declared",
            _present(request.get("selected_evidence_manifest_basis")),
            "EVIDENCE_MANIFEST_BASIS_MISSING",
        ),
        _check(
            "portable_verification_basis_declared",
            _present(request.get("selected_portable_verification_basis")),
            "portable verification basis declared",
            _present(request.get("selected_portable_verification_basis")),
            "PORTABLE_VERIFICATION_BASIS_MISSING",
        ),
        _check(
            "command_module_reference_declared",
            _present(_command_module_reference(request)),
            "command module reference declared as basis only",
            _command_module_reference(request),
            "COMMAND_MODULE_REFERENCE_MISSING",
        ),
        _check(
            "test_surface_reference_declared",
            _present(_test_surface_reference(request)),
            "test surface reference declared as basis only",
            _test_surface_reference(request),
            "TEST_SURFACE_REFERENCE_MISSING",
        ),
        _check(
            "proposed_execution_mode_declared",
            _present(request.get("proposed_execution_mode")),
            "proposed execution mode declared as future condition",
            _present(request.get("proposed_execution_mode")),
            "PROPOSED_EXECUTION_MODE_MISSING",
        ),
        _check(
            "proposed_invocation_surface_declared",
            _present(request.get("proposed_invocation_surface")),
            "proposed invocation surface declared as future condition",
            _present(request.get("proposed_invocation_surface")),
            "PROPOSED_INVOCATION_SURFACE_MISSING",
        ),
        _check(
            "proposed_input_reference_bundle_declared",
            _present(request.get("proposed_input_reference_bundle")),
            "proposed input reference bundle declared",
            _present(request.get("proposed_input_reference_bundle")),
            "PROPOSED_INPUT_REFERENCE_BUNDLE_MISSING",
        ),
        _check(
            "proposed_output_report_destination_declared",
            _present(request.get("proposed_output_report_destination")),
            "proposed output/report destination declared",
            _present(request.get("proposed_output_report_destination")),
            "PROPOSED_OUTPUT_REPORT_DESTINATION_MISSING",
        ),
        _check(
            "execution_limits_declared",
            _present(request.get("execution_limits")),
            "execution limits declared",
            _present(request.get("execution_limits")),
            "EXECUTION_LIMITS_MISSING",
        ),
        _check(
            "output_limits_declared",
            _present(request.get("output_limits")),
            "output limits declared",
            _present(request.get("output_limits")),
            "OUTPUT_LIMITS_MISSING",
        ),
        _check(
            "result_limits_declared",
            _present(request.get("result_limits")),
            "result limits declared",
            _present(request.get("result_limits")),
            "RESULT_LIMITS_MISSING",
        ),
        _check(
            "success_limits_declared",
            _present(request.get("success_limits")),
            "success limits declared",
            _present(request.get("success_limits")),
            "SUCCESS_LIMITS_MISSING",
        ),
        _check(
            "refusal_conditions_declared",
            _present(request.get("refusal_conditions")),
            "refusal conditions declared",
            _present(request.get("refusal_conditions")),
            "REFUSAL_CONDITIONS_MISSING",
        ),
        _check(
            "execution_boundary_scope_supported",
            scope["all_selected_scope_values_supported"],
            "all selected execution-boundary scope values are supported",
            scope["selected_scope_values"],
            "UNSUPPORTED_COMMAND_EXECUTION_BOUNDARY_SCOPE",
        ),
        _check(
            "command_execution_not_performed",
            not _contains_truthy_key(
                request,
                (
                    "command_executed",
                    "command_execution_performed",
                    "command_execution_created",
                    "command_authorized_to_run",
                    "command_execution_authorized",
                    "live_verification_authorized",
                ),
            ),
            "command execution not performed or authorized here",
            "not detected",
            "COMMAND_EXECUTION_PERFORMED",
        ),
        _check(
            "command_invocation_not_created",
            not _contains_truthy_key(request, ("command_invocation_created", "command_invoked")),
            "command invocation not created",
            "not detected",
            "COMMAND_INVOCATION_CREATED",
        ),
        _check(
            "command_output_not_created",
            not _contains_truthy_key(
                request, ("command_output_created", "command_output_exists")
            ),
            "command output not created",
            "not detected",
            "COMMAND_OUTPUT_CREATED",
        ),
        _check(
            "command_result_not_created",
            not _contains_truthy_key(
                request, ("command_result_created", "command_result_exists")
            ),
            "command result not created",
            "not detected",
            "COMMAND_RESULT_CREATED",
        ),
        _check(
            "command_success_not_created",
            not _contains_truthy_key(
                request, ("command_success_created", "command_success_exists")
            ),
            "command success not created",
            "not detected",
            "COMMAND_SUCCESS_CREATED",
        ),
        _check(
            "command_output_not_source",
            not _contains_truthy_key(
                request, ("command_output_became_source", "command_output_treated_as_source")
            ),
            "command output is not source",
            "not detected",
            "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        ),
        _check(
            "command_result_not_authority",
            not _contains_truthy_key(
                request,
                (
                    "command_result_became_authority",
                    "command_result_treated_as_authority",
                    "report_treated_as_authority",
                ),
            ),
            "command result is not authority",
            "not detected",
            "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        ),
        _check(
            "command_success_not_currentness",
            not _contains_truthy_key(
                request,
                (
                    "command_success_created_currentness",
                    "command_success_treated_as_currentness",
                ),
            ),
            "command success is not currentness",
            "not detected",
            "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "command_success_not_final_completion",
            not _contains_truthy_key(
                request,
                (
                    "command_success_claimed_final_completion",
                    "command_success_treated_as_final_completion",
                    "final_completion_claimed",
                ),
            ),
            "command success is not final completion",
            "not detected",
            "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        ),
        _check(
            "execution_not_deployment_runtime_public_release",
            not _contains_truthy_key(
                request,
                (
                    "deployment_created",
                    "deployment_requested",
                    "runtime_hosting_created",
                    "runtime_hosting_requested",
                    "public_release_created",
                    "public_release_requested",
                ),
            ),
            "execution does not create deployment, runtime hosting, or public release",
            "not detected",
            "DEPLOYMENT_CREATED",
        ),
        _check(
            "execution_does_not_authorize_continuation_follow_on_work",
            not _contains_truthy_key(
                request,
                (
                    "continuation_authorized",
                    "continuation_requested",
                    "publication_flow_opened",
                    "follow_on_work_authorized",
                    "follow_on_requested",
                ),
            ),
            "execution does not authorize continuation or follow-on work",
            "not detected",
            "CONTINUATION_AUTHORIZED",
        ),
        _check(
            "execution_requires_reference_shaped_input",
            _present(request.get("proposed_input_reference_bundle"))
            and not _has_full_prior_artifact_body(request.get("proposed_input_reference_bundle")),
            "execution input is reference-shaped",
            _present(request.get("proposed_input_reference_bundle")),
            "FULL_PRIOR_ARTIFACTS_EMBEDDED",
        ),
        _check(
            "execution_must_not_mutate_artifacts",
            not _contains_truthy_key(
                request,
                (
                    "artifacts_mutated",
                    "prior_artifacts_mutated",
                    "artifact_mutation_requested",
                ),
            ),
            "execution must not mutate artifacts",
            "not detected",
            "ARTIFACTS_MUTATED",
        ),
        _check(
            "execution_must_not_embed_full_prior_artifacts",
            not _has_full_prior_artifact_body(request),
            "execution boundary must not embed full prior artifacts",
            "not detected",
            "FULL_PRIOR_ARTIFACTS_EMBEDDED",
        ),
        _check(
            "no_mutation_replay_merge",
            not _contains_truthy_key(request, MUTATION_FLAGS),
            "no mutation, replay, or merge performed",
            "not detected",
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(request),
            "required non-claims are explicit and false",
            _sanitize_reference_shape(request.get("declared_non_claims")),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _determine_block_code(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    *,
    malformed_code: str | None,
) -> str | None:
    if malformed_code:
        return malformed_code
    if request.get("command_execution_boundary_intent") == INTENT_BLOCK:
        return "COMMAND_EXECUTION_BOUNDARY_REVIEW_EXPLICITLY_BLOCKED"
    if request.get("requested_command_execution_boundary_outcome") == OUTCOME_BLOCKED:
        return "COMMAND_EXECUTION_BOUNDARY_REVIEW_EXPLICITLY_BLOCKED"
    collapse = _collapse_code(request)
    if collapse:
        return collapse
    requested = request.get("requested_command_execution_boundary_outcome")
    if _present(requested) and requested not in OUTCOME_FAMILY:
        return "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED"
    for check in checks:
        if not check["passed"]:
            return str(check["block_code"])
    return None


def _determine_outcome(
    request: Mapping[str, Any],
    block_code: str | None,
) -> str:
    requested = request.get("requested_command_execution_boundary_outcome")
    intent = request.get("command_execution_boundary_intent")
    if block_code:
        return OUTCOME_BLOCKED
    if requested in {OUTCOME_NOT_RECORDED, OUTCOME_REQUIRES_ADDITIONAL_BASIS, OUTCOME_BLOCKED}:
        return str(requested)
    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _block_reason(request: Mapping[str, Any], block_code: str | None, path_reason: str | None) -> str | None:
    if not block_code:
        return None
    return str(
        _first_present(
            request.get("block_reason"),
            path_reason,
            {
                "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED": (
                    "Declared command execution-boundary request is malformed."
                ),
                "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE": (
                    "Declared command execution-boundary request is unreadable."
                ),
                "COMMAND_EXECUTION_BOUNDARY_REVIEW_EXPLICITLY_BLOCKED": (
                    "Declared intent requested blocked execution-boundary review."
                ),
            }.get(block_code),
            block_code,
        )
    )


def _build_non_claims(outcome: str) -> dict[str, Any]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    for key in ALLOWED_RECORDED_TRUE_FIELDS:
        non_claims[key] = outcome == OUTCOME_RECORDED
    return non_claims


def _statement(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    failed_count = sum(1 for check in checks if not check["passed"])
    statement = {
        "portable_source_body_verification_command_execution_boundary_recorded": recorded,
        "command_execution_conditions_declared": recorded,
        "command_invocation_must_be_bounded": recorded,
        "command_output_must_be_non_authoritative": recorded,
        "command_success_must_not_create_currentness": recorded,
        "command_success_must_not_claim_final_completion": recorded,
        "selected_command_report_basis_preserved": _present(
            request.get("selected_command_report_basis")
        ),
        "selected_command_implementation_basis_preserved": _present(
            request.get("selected_command_implementation_basis")
        ),
        "selected_command_implementation_boundary_basis_preserved": _present(
            request.get("selected_command_implementation_boundary_basis")
        ),
        "selected_command_boundary_basis_preserved": _present(
            request.get("selected_command_boundary_basis")
        ),
        "selected_artifact_emission_containment_basis_preserved": _present(
            request.get("selected_artifact_emission_containment_basis")
        ),
        "selected_evidence_manifest_basis_preserved": _present(
            request.get("selected_evidence_manifest_basis")
        ),
        "selected_portable_verification_basis_preserved": _present(
            request.get("selected_portable_verification_basis")
        ),
        "execution_boundary_only": recorded and failed_count == 0,
        "command_execution_not_performed": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_is_not_source": True,
        "command_result_is_not_authority": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "execution_is_not_deployment": True,
        "execution_is_not_runtime_hosting": True,
        "execution_is_not_public_release": True,
        "execution_does_not_authorize_continuation": True,
        "execution_does_not_authorize_follow_on_work": True,
        "execution_requires_reference_shaped_input": not _has_full_prior_artifact_body(request),
        "execution_must_not_mutate_artifacts": True,
        "execution_must_not_embed_full_prior_artifacts": not _has_full_prior_artifact_body(
            request
        ),
    }
    statement.update({key: False for key in REQUIRED_FALSE_NON_CLAIMS})
    return statement


def _execution_boundary_non_meaning() -> dict[str, bool]:
    return {
        "execution_boundary_does_not_mean_command_executed": True,
        "execution_boundary_does_not_mean_command_invoked": True,
        "execution_boundary_does_not_mean_command_output_exists": True,
        "execution_boundary_does_not_mean_command_result_exists": True,
        "execution_boundary_does_not_mean_command_success_exists": True,
        "execution_boundary_does_not_mean_command_output_became_source": True,
        "execution_boundary_does_not_mean_command_result_became_authority": True,
        "execution_boundary_does_not_mean_command_success_created_currentness": True,
        "execution_boundary_does_not_mean_command_success_claimed_final_completion": True,
        "execution_boundary_does_not_mean_live_verification_completed": True,
        "execution_boundary_does_not_mean_deployment_created": True,
        "execution_boundary_does_not_mean_runtime_hosting_created": True,
        "execution_boundary_does_not_mean_public_release_created": True,
        "execution_boundary_does_not_mean_public_readiness_created": True,
        "execution_boundary_does_not_mean_operation_permission_created": True,
        "execution_boundary_does_not_mean_continuation_authorized": True,
        "execution_boundary_does_not_mean_reusable_permission_created": True,
        "execution_boundary_does_not_mean_derivative_reception_authorized": True,
        "execution_boundary_does_not_mean_vessel_relation_authorized": True,
        "execution_boundary_does_not_mean_another_reception_request_authorized": True,
        "execution_boundary_does_not_mean_follow_on_work_authorized": True,
    }


def _additional_basis_required(
    request: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": _sanitize_reference_shape(
            request.get("additional_basis_context")
        )
        if required
        else {},
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
        "command_not_run": True,
        "command_output_result_success_not_created": True,
        "artifacts_not_mutated": True,
    }


def _not_recorded_basis(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    failed_checks = [check for check in checks if not check["passed"]]
    return {
        "not_recorded": not_recorded,
        "not_recorded_basis": _sanitize_reference_shape(request.get("not_recorded_basis"))
        if not_recorded
        else {},
        "failed_execution_boundary_checks": _sanitize_reference_shape(failed_checks)
        if not_recorded
        else [],
        "not_recorded_does_not_run_command": True,
        "not_recorded_does_not_mutate_artifacts": True,
        "not_recorded_does_not_repair_or_authorize_execution": True,
        "not_recorded_does_not_deploy_publish_currentize_complete_continue": True,
        "not_recorded_does_not_create_reusable_permission_or_follow_on_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "command execution boundary test",
            "command execution boundary live artifact",
            "actual command invocation",
            "command output from live execution",
            "command result from live execution",
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


def _build_result(
    request_value: Mapping[str, Any] | None,
    *,
    request_path: str | None = None,
    malformed_code: str | None = None,
    path_reason: str | None = None,
) -> dict[str, Any]:
    request = _copy(request_value) if isinstance(request_value, Mapping) else {}
    checks = _build_checks(request, malformed_code=malformed_code)
    block_code = _determine_block_code(request, checks, malformed_code=malformed_code)
    outcome = _determine_outcome(request, block_code)
    passed_check_count = sum(1 for check in checks if check["passed"])
    failed_check_count = sum(1 for check in checks if not check["passed"])
    request_id = _safe_component(
        request.get("command_execution_boundary_request_id"),
        "portable_source_body_verification_command_execution_boundary_unresolved",
    )

    result: dict[str, Any] = {
        "portable_source_body_verification_command_execution_boundary_metadata": {
            "portable_source_body_verification_command_execution_boundary_result_id": (
                f"{request_id}__portable_source_body_verification_command_execution_boundary_result"
            ),
            "portable_source_body_verification_command_execution_boundary_result_type": (
                "portable_source_body_verification_command_execution_boundary_result"
            ),
            "portable_source_body_verification_command_execution_boundary_result_version": (
                RESULT_VERSION
            ),
            "generated_at": _generated_at(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_command_execution_boundary_question": {
            "command_execution_boundary_request_id": request.get(
                "command_execution_boundary_request_id"
            ),
            "command_execution_boundary_question": request.get(
                "command_execution_boundary_question"
            ),
            "command_execution_boundary_intent": request.get(
                "command_execution_boundary_intent"
            ),
            "requested_command_execution_boundary_outcome": request.get(
                "requested_command_execution_boundary_outcome"
            ),
            "declared_command_execution_boundary_request_path": request_path,
            "execution_boundary_question_answered": (
                "Can conditions for a future bounded command invocation be recorded "
                "without executing, invoking, emitting output, creating a result, "
                "or creating command success?"
            ),
            "execution_boundary_is_not_execution": True,
            "execution_boundary_is_not_invocation": True,
            "execution_boundary_is_not_output": True,
            "execution_boundary_is_not_result": True,
            "execution_boundary_is_not_success": True,
        },
        "selected_command_report_basis": _selected_basis_section(
            request,
            "selected_command_report_basis",
            "selected_command_report_basis",
            result_path_key="selected_command_report_result_path",
            result_id_key="selected_command_report_result_id",
            result_status_key="selected_command_report_status",
            terminal_summary_path_key="selected_command_report_terminal_summary_path",
        ),
        "selected_command_implementation_basis": _selected_basis_section(
            request,
            "selected_command_implementation_basis",
            "selected_command_implementation_basis",
        ),
        "selected_command_implementation_boundary_basis": _selected_basis_section(
            request,
            "selected_command_implementation_boundary_basis",
            "selected_command_implementation_boundary_basis",
        ),
        "selected_command_boundary_basis": _selected_basis_section(
            request,
            "selected_command_boundary_basis",
            "selected_command_boundary_basis",
        ),
        "selected_artifact_emission_containment_basis": _selected_basis_section(
            request,
            "selected_artifact_emission_containment_basis",
            "selected_artifact_emission_containment_basis",
        ),
        "selected_evidence_manifest_basis": _selected_basis_section(
            request,
            "selected_evidence_manifest_basis",
            "selected_evidence_manifest_basis",
        ),
        "selected_portable_verification_basis": _selected_basis_section(
            request,
            "selected_portable_verification_basis",
            "selected_portable_verification_basis",
        ),
        "proposed_execution_mode": _proposal_section(
            request.get("proposed_execution_mode"), "proposed_execution_mode"
        ),
        "proposed_invocation_surface": _proposal_section(
            request.get("proposed_invocation_surface"), "proposed_invocation_surface"
        ),
        "proposed_input_reference_bundle": _proposal_section(
            request.get("proposed_input_reference_bundle"),
            "proposed_input_reference_bundle",
        ),
        "proposed_output_report_destination": _proposal_section(
            request.get("proposed_output_report_destination"),
            "proposed_output_report_destination",
        ),
        "execution_limits": _limit_section(
            request.get("execution_limits"),
            "execution_limits",
            request.get("non_authority_posture"),
        ),
        "output_limits": _limit_section(
            request.get("output_limits"),
            "output_limits",
            request.get("non_authority_posture"),
        ),
        "result_limits": _limit_section(
            request.get("result_limits"),
            "result_limits",
            request.get("non_currentness_posture"),
        ),
        "success_limits": _limit_section(
            request.get("success_limits"),
            "success_limits",
            request.get("non_final_completion_posture"),
        ),
        "refusal_conditions": _limit_section(
            request.get("refusal_conditions"), "refusal_conditions"
        ),
        "execution_boundary_scope": _execution_boundary_scope_section(
            request.get("execution_boundary_scope")
        ),
        "execution_boundary_checks": checks,
        "execution_boundary_statement": _statement(request, outcome, checks),
        "execution_boundary_non_meaning": _execution_boundary_non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "not_recorded_basis": _not_recorded_basis(request, outcome, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _build_non_claims(outcome),
        "outcome": outcome,
        "block": _block(
            outcome == OUTCOME_BLOCKED,
            block_code,
            _block_reason(request, block_code, path_reason),
        ),
    }
    result["portable_source_body_verification_command_execution_boundary_summary"] = (
        build_portable_source_body_verification_command_execution_boundary_summary(result)
    )
    result[
        "portable_source_body_verification_command_execution_boundary_summary"
    ]["passed_check_count"] = passed_check_count
    result[
        "portable_source_body_verification_command_execution_boundary_summary"
    ]["failed_check_count"] = failed_check_count
    return result


def resolve_portable_source_body_verification_command_execution_boundary(
    declared_command_execution_boundary_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared command execution-boundary request mapping."""

    if declared_command_execution_boundary_request is None:
        return _build_result({})
    if not isinstance(declared_command_execution_boundary_request, Mapping):
        return _build_result(
            {},
            malformed_code="DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
        )
    return _build_result(declared_command_execution_boundary_request)


def resolve_portable_source_body_verification_command_execution_boundary_from_path(
    declared_command_execution_boundary_request_path: Path | str,
) -> dict:
    """Resolve one declared command execution-boundary request from a JSON object."""

    request, error_code, error_reason = _read_json_object(
        declared_command_execution_boundary_request_path
    )
    if error_code:
        return _build_result(
            {},
            request_path=str(declared_command_execution_boundary_request_path),
            malformed_code=error_code,
            path_reason=error_reason,
        )
    return _build_result(
        request,
        request_path=str(declared_command_execution_boundary_request_path),
    )


def build_portable_source_body_verification_command_execution_boundary_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a bounded summary for an execution-boundary result artifact."""

    checks = list(result.get("execution_boundary_checks", []))
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)
    failed_check_count = sum(1 for check in checks if check.get("passed") is not True)
    statement = result.get("execution_boundary_statement", {})
    question = result.get("declared_command_execution_boundary_question", {})
    non_claims = result.get("non_claims", {})
    block = result.get("block", {})
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "command_execution_boundary_request_id": question.get(
            "command_execution_boundary_request_id"
        ),
        "command_execution_boundary_question": question.get(
            "command_execution_boundary_question"
        ),
        "command_execution_boundary_intent": question.get(
            "command_execution_boundary_intent"
        ),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "execution_boundary_recorded": bool(
            statement.get("portable_source_body_verification_command_execution_boundary_recorded")
        ),
        "command_execution_conditions_declared": bool(
            statement.get("command_execution_conditions_declared")
        ),
        "command_invocation_must_be_bounded": bool(
            statement.get("command_invocation_must_be_bounded")
        ),
        "command_output_must_be_non_authoritative": bool(
            statement.get("command_output_must_be_non_authoritative")
        ),
        "command_success_must_not_create_currentness": bool(
            statement.get("command_success_must_not_create_currentness")
        ),
        "command_success_must_not_claim_final_completion": bool(
            statement.get("command_success_must_not_claim_final_completion")
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_report_basis_preserved": bool(
            statement.get("selected_command_report_basis_preserved")
        ),
        "selected_command_implementation_basis_preserved": bool(
            statement.get("selected_command_implementation_basis_preserved")
        ),
        "selected_command_implementation_boundary_basis_preserved": bool(
            statement.get("selected_command_implementation_boundary_basis_preserved")
        ),
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
        "execution_boundary_only": bool(statement.get("execution_boundary_only")),
        "command_execution_not_performed": bool(
            statement.get("command_execution_not_performed")
        ),
        "command_invocation_not_created": bool(
            statement.get("command_invocation_not_created")
        ),
        "command_output_not_created": bool(statement.get("command_output_not_created")),
        "command_result_not_created": bool(statement.get("command_result_not_created")),
        "command_success_not_created": bool(statement.get("command_success_not_created")),
        "command_output_not_source": bool(statement.get("command_output_is_not_source")),
        "command_result_not_authority": bool(
            statement.get("command_result_is_not_authority")
        ),
        "command_success_not_currentness": bool(
            statement.get("command_success_is_not_currentness")
        ),
        "command_success_not_final_completion": bool(
            statement.get("command_success_is_not_final_completion")
        ),
        "execution_not_deployment": bool(statement.get("execution_is_not_deployment")),
        "execution_not_runtime_hosting": bool(
            statement.get("execution_is_not_runtime_hosting")
        ),
        "execution_not_public_release": bool(
            statement.get("execution_is_not_public_release")
        ),
        "execution_requires_reference_shaped_input": bool(
            statement.get("execution_requires_reference_shaped_input")
        ),
        "no_full_prior_artifacts_embedded": not bool(
            non_claims.get("full_prior_artifacts_embedded")
        ),
        "no_artifact_mutation": not bool(non_claims.get("prior_artifacts_mutated")),
        "no_operation_permission_public_readiness_final_completion": not any(
            bool(non_claims.get(key))
            for key in (
                "operation_permission_created",
                "public_launch_readiness_created",
                "final_completion_claimed",
            )
        ),
        "no_continuation_publication_flow_reusable_permission": not any(
            bool(non_claims.get(key))
            for key in (
                "continuation_authorized",
                "publication_flow_opened",
                "reusable_permission_created",
            )
        ),
        "no_derivative_reception_vessel_relation_another_request_follow_on_work": not any(
            bool(non_claims.get(key))
            for key in (
                "derivative_reception_authorized",
                "vessel_relation_authorized",
                "another_reception_request_authorized",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": _sanitize_reference_shape(non_claims),
    }


def _unique_path(path: Path) -> Path:
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


def write_portable_source_body_verification_command_execution_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive execution-boundary result artifact as JSON."""

    if not isinstance(result, Mapping):
        raise PortableSourceBodyVerificationCommandExecutionBoundaryError(
            "result must be a mapping"
        )
    question = result.get("declared_command_execution_boundary_question", {})
    request_id = _safe_component(
        _value_at(question, ("command_execution_boundary_request_id",)),
        "portable_source_body_verification_command_execution_boundary_result",
    )
    filename = f"{request_id}__portable_source_body_verification_command_execution_boundary_result.json"
    destination = (
        PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_ROOT
        if output_path is None
        else Path(output_path)
    )
    if destination.suffix == ".json":
        final_path = destination
    else:
        final_path = destination / filename
    final_path = _unique_path(final_path)
    final_path.parent.mkdir(parents=True, exist_ok=True)
    final_path.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path


def build_declared_portable_source_body_verification_command_execution_boundary_request(
    command_execution_boundary_request_id: str,
    command_execution_boundary_question: str,
    selected_command_report_basis: Mapping[str, Any] | str,
    selected_command_implementation_basis: Mapping[str, Any] | str,
    selected_command_implementation_boundary_basis: Mapping[str, Any] | str,
    selected_command_boundary_basis: Mapping[str, Any] | str,
    selected_artifact_emission_containment_basis: Mapping[str, Any] | str,
    selected_evidence_manifest_basis: Mapping[str, Any] | str,
    selected_portable_verification_basis: Mapping[str, Any] | str,
    proposed_execution_mode: Mapping[str, Any] | str,
    proposed_invocation_surface: Mapping[str, Any] | str,
    proposed_input_reference_bundle: Mapping[str, Any] | str,
    proposed_output_report_destination: Mapping[str, Any] | str,
    execution_limits: Mapping[str, Any] | str,
    output_limits: Mapping[str, Any] | str,
    result_limits: Mapping[str, Any] | str,
    success_limits: Mapping[str, Any] | str,
    refusal_conditions: Mapping[str, Any] | str,
    execution_boundary_scope: Sequence[str] | Mapping[str, Any],
    command_execution_boundary_intent: str = INTENT_RECORD,
    *,
    requested_command_execution_boundary_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared execution-boundary request with required false non-claims."""

    return {
        "command_execution_boundary_request_id": command_execution_boundary_request_id,
        "command_execution_boundary_question": command_execution_boundary_question,
        "command_execution_boundary_intent": command_execution_boundary_intent,
        "selected_command_report_basis": _sanitize_reference_shape(
            selected_command_report_basis
        ),
        "selected_command_implementation_basis": _sanitize_reference_shape(
            selected_command_implementation_basis
        ),
        "selected_command_implementation_boundary_basis": _sanitize_reference_shape(
            selected_command_implementation_boundary_basis
        ),
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
        "selected_command_module_reference": "src/portable_source_body_verification_command.py",
        "selected_test_surface_reference": (
            "tests/test_portable_source_body_verification_command.py"
        ),
        "proposed_execution_mode": _sanitize_reference_shape(proposed_execution_mode),
        "proposed_invocation_surface": _sanitize_reference_shape(proposed_invocation_surface),
        "proposed_input_reference_bundle": _sanitize_reference_shape(
            proposed_input_reference_bundle
        ),
        "proposed_output_report_destination": _sanitize_reference_shape(
            proposed_output_report_destination
        ),
        "execution_limits": _sanitize_reference_shape(execution_limits),
        "output_limits": _sanitize_reference_shape(output_limits),
        "result_limits": _sanitize_reference_shape(result_limits),
        "success_limits": _sanitize_reference_shape(success_limits),
        "refusal_conditions": _sanitize_reference_shape(refusal_conditions),
        "non_authority_posture": {
            "non_authority_posture_declared": True,
            "command_output_is_not_source": True,
            "command_result_is_not_authority": True,
        },
        "non_currentness_posture": {
            "non_currentness_posture_declared": True,
            "command_success_is_not_currentness": True,
        },
        "non_final_completion_posture": {
            "non_final_completion_posture_declared": True,
            "command_success_is_not_final_completion": True,
        },
        "execution_boundary_scope": _sanitize_reference_shape(execution_boundary_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "requested_command_execution_boundary_outcome": (
            requested_command_execution_boundary_outcome
        ),
        "additional_basis_context": _sanitize_reference_shape(additional_basis_context or {}),
        "not_recorded_basis": _sanitize_reference_shape(not_recorded_basis or {}),
    }
