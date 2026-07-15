"""Resolve v2 single live command invocation request/admission boundary.

This successor preserves the v1 boundary meaning while correcting returned
result containment: forbidden full prior artifact bodies are detected, blocked,
and replaced with a bounded marker before any request-derived content is
included in the returned result.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationSingleLiveCommandInvocationRequestAdmissionBoundaryV2Error(
    Exception
):
    """Raised only for impossible v2 request/admission boundary failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary_v2"
)
SUCCESSOR_OF = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary"
)
SUCCESSOR_REASON = (
    "v1 returned-result containment flaw: raw full prior artifact body could be "
    "echoed into result"
)
RESULT_VERSION = "0.2.0"
OMITTED_FULL_BODY_MARKER = (
    "[OMITTED: full prior artifact body blocked by single live command invocation "
    "request/admission boundary v2]"
)
PORTABLE_SOURCE_BODY_VERIFICATION_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_V2_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "single_live_command_invocation_request_admission_boundary_v2"
)

OUTCOME_ADMITTED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
OUTCOME_NOT_ADMITTED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_NOT_ADMITTED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_ADMITTED,
    OUTCOME_NOT_ADMITTED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_ADMIT = "ADMIT_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST"
INTENT_DO_NOT_ADMIT = "DO_NOT_ADMIT_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST"
INTENT_BLOCK = "BLOCK_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW"
SUPPORTED_INTENTS = {INTENT_ADMIT, INTENT_DO_NOT_ADMIT, INTENT_BLOCK}

SUPPORTED_REQUEST_ADMISSION_SCOPE = {
    "SINGLE_INVOCATION_REQUEST_ADMISSION_ONLY",
    "ONE_SHOT_INVOCATION_REQUEST_ONLY",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "INVOCATION_REQUIRES_SEPARATE_EXECUTION_STEP",
    "COMMAND_OUTPUT_MUST_BE_NON_SOURCE",
    "COMMAND_RESULT_MUST_BE_NON_AUTHORITY",
    "COMMAND_SUCCESS_MUST_NOT_CREATE_CURRENTNESS",
    "COMMAND_SUCCESS_MUST_NOT_CLAIM_FINAL_COMPLETION",
    "INVOCATION_MUST_USE_REFERENCE_SHAPED_INPUT",
    "INVOCATION_MUST_NOT_MUTATE_ARTIFACTS",
    "INVOCATION_MUST_NOT_EMBED_FULL_PRIOR_ARTIFACTS",
    "INVOCATION_IS_NOT_DEPLOYMENT",
    "INVOCATION_IS_NOT_RUNTIME_HOSTING",
    "INVOCATION_IS_NOT_PUBLIC_RELEASE",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "single_invocation_request_admission_recorded_as_execution",
    "command_invocation_created",
    "command_executed",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
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

ADMITTED_TRUE_FIELDS = (
    "single_live_command_invocation_request_admitted",
    "single_invocation_request_declared",
    "single_invocation_scope_bounded",
    "single_invocation_admission_conditions_declared",
    "single_invocation_execution_still_not_performed",
    "single_invocation_requires_separate_execution_step",
)

FORBIDDEN_FULL_BODY_KEYS = {
    "full_artifact_body",
    "raw_artifact",
    "raw_result",
    "embedded_artifact",
    "selected_full_artifact",
    "complete_artifact_body",
    "raw_artifact_body",
    "embedded_artifacts",
    "artifact_body",
    "full_result",
    "raw_selected_basis",
}

BASIS_FIELDS = (
    (
        "selected_command_execution_boundary_basis",
        "command_execution_boundary_basis",
        "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
        "selected_command_execution_boundary_result_path",
        "selected_command_execution_boundary_result_id",
        "selected_command_execution_boundary_outcome",
    ),
    (
        "selected_command_report_basis",
        "command_report_basis",
        "COMMAND_REPORT_BASIS_MISSING",
        "selected_command_report_result_path",
        "selected_command_report_result_id",
        "selected_command_report_status",
    ),
    (
        "selected_command_implementation_basis",
        "command_implementation_basis",
        "COMMAND_IMPLEMENTATION_SPEC_MISSING",
        None,
        None,
        None,
    ),
    (
        "selected_artifact_emission_containment_basis",
        "artifact_emission_containment_basis",
        "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
        None,
        None,
        None,
    ),
    (
        "selected_evidence_manifest_basis",
        "evidence_manifest_basis",
        "EVIDENCE_MANIFEST_BASIS_MISSING",
        None,
        None,
        None,
    ),
    (
        "selected_portable_verification_basis",
        "portable_verification_basis",
        "PORTABLE_VERIFICATION_BASIS_MISSING",
        None,
        None,
        None,
    ),
)

REQUIRED_REQUEST_FIELDS = (
    (
        "request/admission question declared",
        "invocation_request_admission_question",
        "INVOCATION_REQUEST_ADMISSION_QUESTION_UNDECLARED",
    ),
    (
        "proposed one-shot invocation mode declared",
        "proposed_one_shot_invocation_mode",
        "PROPOSED_INVOCATION_MODE_MISSING",
    ),
    (
        "proposed invocation surface declared",
        "proposed_invocation_surface",
        "PROPOSED_INVOCATION_SURFACE_MISSING",
    ),
    (
        "proposed input reference bundle declared",
        "proposed_input_reference_bundle",
        "INPUT_REFERENCE_BUNDLE_MISSING",
    ),
    (
        "proposed output/report destination declared",
        "proposed_output_report_destination",
        "OUTPUT_REPORT_DESTINATION_MISSING",
    ),
    ("one-invocation scope declared", "single_invocation_scope", "SINGLE_INVOCATION_SCOPE_MISSING"),
    ("no-repeat posture declared", "no_repeat_posture", "NO_REPEAT_POSTURE_MISSING"),
    (
        "no-standing-invocation-lane posture declared",
        "no_standing_invocation_lane_posture",
        "NO_STANDING_INVOCATION_LANE_POSTURE_MISSING",
    ),
    ("refusal conditions declared", "refusal_conditions", "REFUSAL_CONDITIONS_MISSING"),
    ("output limits declared", "output_limits", "OUTPUT_LIMITS_MISSING"),
    ("result limits declared", "result_limits", "RESULT_LIMITS_MISSING"),
    ("success limits declared", "success_limits", "SUCCESS_LIMITS_MISSING"),
    ("non-authority posture declared", "non_authority_posture", "NON_AUTHORITY_POSTURE_MISSING"),
    ("non-currentness posture declared", "non_currentness_posture", "NON_CURRENTNESS_POSTURE_MISSING"),
    (
        "non-final-completion posture declared",
        "non_final_completion_posture",
        "NON_FINAL_COMPLETION_POSTURE_MISSING",
    ),
)

COLLAPSE_CHECKS = (
    ("command invocation not created", ("command_invocation_created", "command_invoked"), "COMMAND_INVOCATION_CREATED"),
    ("command execution not performed", ("command_executed", "command_execution_performed", "command_execution_authorized", "command_authorized_to_run", "live_verification_authorized", "live_verification_execution_authorized"), "COMMAND_EXECUTION_PERFORMED"),
    ("command output not created", ("command_output_created", "command_output_exists"), "COMMAND_OUTPUT_CREATED"),
    ("command result not created", ("command_result_created", "command_result_exists"), "COMMAND_RESULT_CREATED"),
    ("command success not created", ("command_success_created", "command_success_exists", "live_verification_completed"), "COMMAND_SUCCESS_CREATED"),
    ("no standing invocation lane created", ("standing_invocation_lane_created", "standing_invocation_lane_exists"), "STANDING_INVOCATION_LANE_CREATED"),
    ("no repeat invocation permission created", ("repeat_invocation_permission_created", "repeat_invocation_permission_authorized", "repeated_invocations_authorized"), "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("output remains non-source", ("command_output_became_source", "command_output_treated_as_source"), "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("result remains non-authority", ("command_result_became_authority", "command_result_treated_as_authority", "command_became_authority"), "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("success does not create currentness", ("command_success_created_currentness", "command_success_treated_as_currentness"), "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
    ("success does not claim final completion", ("command_success_claimed_final_completion", "command_success_treated_as_final_completion", "final_completion_claimed"), "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
    ("artifacts not mutated", ("prior_artifacts_mutated", "artifacts_mutated"), "ARTIFACTS_MUTATED"),
    ("deployment not created", ("deployment_created",), "DEPLOYMENT_CREATED"),
    ("runtime hosting not created", ("runtime_hosting_created",), "RUNTIME_HOSTING_CREATED"),
    ("public release not created", ("public_release_created",), "PUBLIC_RELEASE_CREATED"),
    ("operation permission not created", ("operation_permission_created",), "OPERATION_PERMISSION_CREATED"),
    ("public readiness not created", ("public_launch_readiness_created", "public_readiness_created"), "PUBLIC_READINESS_CREATED"),
    ("continuation not authorized", ("continuation_authorized", "publication_flow_opened"), "CONTINUATION_AUTHORIZED"),
    ("reusable permission not created", ("reusable_permission_created",), "REUSABLE_PERMISSION_CREATED"),
    ("derivative reception not authorized", ("derivative_reception_authorized",), "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel relation not authorized", ("vessel_relation_authorized",), "VESSEL_RELATION_AUTHORIZED"),
    ("another reception request not authorized", ("another_reception_request_authorized",), "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow-on work not authorized", ("follow_on_work_authorized",), "FOLLOW_ON_WORK_AUTHORIZED"),
    ("no mutation/replay/merge", ("mutation_performed", "replay_performed", "merge_performed"), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
)

BLOCK_REASONS = {
    "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED": "Declared request/admission must be a JSON object mapping.",
    "DECLARED_INVOCATION_REQUEST_ADMISSION_UNREADABLE": "Declared request/admission path could not be read.",
    "INVOCATION_REQUEST_ADMISSION_REVIEW_EXPLICITLY_BLOCKED": "Declared request/admission intent blocks review.",
    "UNSUPPORTED_INVOCATION_REQUEST_ADMISSION_SCOPE": "Request/admission scope contains unsupported values.",
    "FULL_PRIOR_ARTIFACTS_EMBEDDED": "Forbidden full prior artifact body posture was detected and omitted from the v2 result.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required false non-claim is missing or flipped.",
}


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


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
        return value.strip().lower() in {"true", "yes", "1", "created", "performed"}
    return bool(value)


def _is_false(value: Any) -> bool:
    if value is False:
        return True
    if isinstance(value, str):
        return value.strip().lower() == "false"
    return False


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _safe_component(value: Any, fallback: str) -> str:
    raw = str(value or fallback).strip() or fallback
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in raw)
    return safe.strip("._") or fallback


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            key: OMITTED_FULL_BODY_MARKER if key in FORBIDDEN_FULL_BODY_KEYS else _sanitize(nested)
            for key, nested in value.items()
        }
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return _copy(value)


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            key in FORBIDDEN_FULL_BODY_KEYS or _contains_forbidden_full_body_key(nested)
            for key, nested in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _forbidden_full_body_keys(value: Any) -> list[str]:
    found: set[str] = set()

    def visit(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, nested in item.items():
                if key in FORBIDDEN_FULL_BODY_KEYS:
                    found.add(str(key))
                visit(nested)
        elif isinstance(item, Sequence) and not isinstance(item, (str, bytes, bytearray)):
            for nested_item in item:
                visit(nested_item)

    visit(value)
    return sorted(found)


def _contains_truthy_key(value: Any, key: str) -> bool:
    if isinstance(value, Mapping):
        for current_key, nested in value.items():
            if current_key == key and _truthy(nested):
                return True
            if _contains_truthy_key(nested, key):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, key) for item in value)
    return False


def _first_truthy_key(value: Any, keys: Sequence[str]) -> str | None:
    for key in keys:
        if _contains_truthy_key(value, key):
            return key
    return None


def _first_present(mapping: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        value = mapping.get(key)
        if _present(value):
            return value
    return None


def _basis_id(value: Any) -> Any:
    mapping = _as_mapping(value)
    return _sanitize(_first_present(mapping, ("selected_result_id", "selected_id", "result_id", "id")))


def _basis_path(value: Any) -> Any:
    if isinstance(value, str):
        return value
    mapping = _as_mapping(value)
    return _sanitize(_first_present(mapping, ("selected_result_path", "selected_path", "result_path", "path")))


def _basis_outcome(value: Any) -> Any:
    mapping = _as_mapping(value)
    return _sanitize(
        _first_present(
            mapping,
            ("selected_result_outcome", "selected_result_status", "selected_outcome", "selected_status", "outcome", "status"),
        )
    )


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, Mapping):
        nested = _first_present(
            scope,
            ("scope_values", "selected_scope_values", "request_admission_scope_values", "selected_request_admission_scope_values", "values"),
        )
        return _scope_values(nested if nested is not None else list(scope.keys()))
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Sequence) and not isinstance(scope, (str, bytes, bytearray)):
        return [str(item) for item in scope]
    return []


def _check(name: str, passed: bool, expected: Any, actual: Any, code: str) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims_false(request: Mapping[str, Any]) -> bool:
    claims = _as_mapping(request.get("declared_non_claims"))
    return all(key in claims and _is_false(claims[key]) for key in REQUIRED_FALSE_NON_CLAIMS)


def _reference_section(
    request: Mapping[str, Any],
    request_key: str,
    label: str,
    path_key: str | None,
    id_key: str | None,
    status_key: str | None,
) -> dict[str, Any]:
    value = request.get(request_key)
    selected_path = request.get(path_key) if path_key else None
    selected_id = request.get(id_key) if id_key else None
    selected_status = request.get(status_key) if status_key else None
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": _present(value),
        f"{label}_preserved": _present(value),
        "selected_id": _sanitize(selected_id) if _present(selected_id) else _basis_id(value),
        "selected_path": _sanitize(selected_path) if _present(selected_path) else _basis_path(value),
        "selected_outcome_or_status": _sanitize(selected_status) if _present(selected_status) else _basis_outcome(value),
        "selected_basis": _sanitize(value),
        "reference_shaped_basis_only": not forbidden,
        "basis_remains_non_authoritative": True,
        "basis_does_not_authorize_invocation_execution": True,
        "basis_does_not_create_output_result_success": True,
        "basis_does_not_create_currentness_final_completion_follow_on_work": True,
        "forbidden_full_body_posture_detected": forbidden,
        "forbidden_full_body_keys_detected": _forbidden_full_body_keys(value),
        "full_prior_artifacts_are_not_embedded": not forbidden,
        "full_prior_artifact_raw_values_omitted": True,
        "prior_artifacts_are_not_mutated": not _contains_truthy_key(value, "prior_artifacts_mutated"),
    }


def _proposal_section(value: Any, label: str) -> dict[str, Any]:
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": _present(value),
        "declared_value": _sanitize(value),
        "future_condition_only": True,
        "proposal_is_not_invocation": True,
        "proposal_is_not_execution": True,
        "proposal_is_not_output": True,
        "proposal_is_not_result": True,
        "proposal_is_not_success": True,
        "proposal_does_not_authorize_execution": True,
        "no_standing_invocation_lane_created": True,
        "no_repeat_invocation_permission_created": True,
        "forbidden_full_body_posture_detected": forbidden,
        "forbidden_full_body_keys_detected": _forbidden_full_body_keys(value),
        "full_prior_artifact_raw_values_omitted": True,
    }


def _limit_section(value: Any, label: str) -> dict[str, Any]:
    section = _proposal_section(value, label)
    section.update(
        {
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "command_output_is_not_source": True,
            "command_result_is_not_authority": True,
            "command_success_is_not_currentness": True,
            "command_success_is_not_final_completion": True,
            "invocation_requires_separate_execution_step": True,
            "invocation_requires_reference_shaped_input": True,
            "invocation_must_not_mutate_artifacts": True,
            "invocation_must_not_embed_full_prior_artifacts": True,
            "invocation_is_not_deployment": True,
            "invocation_is_not_runtime_hosting": True,
            "invocation_is_not_public_release": True,
            "invocation_does_not_authorize_continuation": True,
            "invocation_does_not_authorize_follow_on_work": True,
        }
    )
    return section


def _scope_section(scope: Any) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = [value for value in values if value not in SUPPORTED_REQUEST_ADMISSION_SCOPE]
    return {
        "selected_scope_values": _sanitize(values),
        "unsupported_scope_values": _sanitize(unsupported),
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "request_admission_only": "SINGLE_INVOCATION_REQUEST_ADMISSION_ONLY" in values,
        "one_shot_invocation_request_only": "ONE_SHOT_INVOCATION_REQUEST_ONLY" in values,
        "command_invocation_not_created": "COMMAND_INVOCATION_NOT_CREATED" in values,
        "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED" in values,
        "command_output_not_created": "COMMAND_OUTPUT_NOT_CREATED" in values,
        "command_result_not_created": "COMMAND_RESULT_NOT_CREATED" in values,
        "command_success_not_created": "COMMAND_SUCCESS_NOT_CREATED" in values,
        "no_standing_invocation_lane_created": "NO_STANDING_INVOCATION_LANE_CREATED" in values,
        "no_repeat_invocation_permission_created": "NO_REPEAT_INVOCATION_PERMISSION_CREATED" in values,
        "invocation_requires_separate_execution_step": "INVOCATION_REQUIRES_SEPARATE_EXECUTION_STEP" in values,
        "command_output_must_be_non_source": "COMMAND_OUTPUT_MUST_BE_NON_SOURCE" in values,
        "command_result_must_be_non_authority": "COMMAND_RESULT_MUST_BE_NON_AUTHORITY" in values,
        "command_success_must_not_create_currentness": "COMMAND_SUCCESS_MUST_NOT_CREATE_CURRENTNESS" in values,
        "command_success_must_not_claim_final_completion": "COMMAND_SUCCESS_MUST_NOT_CLAIM_FINAL_COMPLETION" in values,
        "invocation_must_use_reference_shaped_input": "INVOCATION_MUST_USE_REFERENCE_SHAPED_INPUT" in values,
        "invocation_must_not_mutate_artifacts": "INVOCATION_MUST_NOT_MUTATE_ARTIFACTS" in values,
        "invocation_must_not_embed_full_prior_artifacts": "INVOCATION_MUST_NOT_EMBED_FULL_PRIOR_ARTIFACTS" in values,
        "invocation_is_not_deployment": "INVOCATION_IS_NOT_DEPLOYMENT" in values,
        "invocation_is_not_runtime_hosting": "INVOCATION_IS_NOT_RUNTIME_HOSTING" in values,
        "invocation_is_not_public_release": "INVOCATION_IS_NOT_PUBLIC_RELEASE" in values,
        "forbidden_full_body_posture_detected": _contains_forbidden_full_body_key(scope),
        "forbidden_full_body_keys_detected": _forbidden_full_body_keys(scope),
        "full_prior_artifact_raw_values_omitted": True,
    }


def _command_module_reference(request: Mapping[str, Any]) -> Any:
    return _first_present(request, ("selected_command_module_reference", "command_module_reference", "selected_command_module_path"))


def _test_surface_reference(request: Mapping[str, Any]) -> Any:
    return _first_present(request, ("selected_test_surface_reference", "test_surface_reference", "selected_command_report_module_test_surface_reference"))


def _build_checks(request: Mapping[str, Any], malformed_code: str | None) -> list[dict[str, Any]]:
    if malformed_code:
        return [
            _check(
                "declared request/admission is a mapping",
                False,
                "mapping",
                malformed_code,
                malformed_code,
            )
        ]

    checks: list[dict[str, Any]] = []
    for name, key, code in REQUIRED_REQUEST_FIELDS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))

    intent = request.get("invocation_request_admission_intent")
    checks.append(
        _check(
            "request/admission intent supported",
            intent in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            intent,
            "INVOCATION_REQUEST_ADMISSION_INTENT_UNSUPPORTED",
        )
    )

    for request_key, label, code, _path_key, _id_key, _status_key in BASIS_FIELDS:
        checks.append(
            _check(
                f"{label.replace('_', ' ')} declared",
                _present(request.get(request_key)),
                "declared basis",
                request.get(request_key),
                code,
            )
        )

    checks.append(
        _check(
            "command module reference declared",
            _present(_command_module_reference(request)),
            "declared command module reference",
            _command_module_reference(request),
            "COMMAND_MODULE_REFERENCE_MISSING",
        )
    )
    checks.append(
        _check(
            "test surface reference declared",
            _present(_test_surface_reference(request)),
            "declared test surface reference",
            _test_surface_reference(request),
            "TEST_SURFACE_REFERENCE_MISSING",
        )
    )

    scope = _scope_section(request.get("request_admission_scope"))
    checks.append(
        _check(
            "request/admission scope supported",
            scope["all_selected_scope_values_supported"],
            sorted(SUPPORTED_REQUEST_ADMISSION_SCOPE),
            scope["selected_scope_values"],
            "UNSUPPORTED_INVOCATION_REQUEST_ADMISSION_SCOPE",
        )
    )

    for name, keys, code in COLLAPSE_CHECKS:
        truthy_key = _first_truthy_key(request, keys)
        checks.append(_check(name, truthy_key is None, False, truthy_key, code))

    forbidden = _contains_forbidden_full_body_key(request) or _contains_truthy_key(
        request, "full_prior_artifacts_embedded"
    )
    checks.append(
        _check(
            "full prior artifacts not embedded",
            not forbidden,
            "no forbidden full prior artifact body keys or posture",
            {
                "forbidden_full_body_posture_detected": forbidden,
                "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request),
            },
            "FULL_PRIOR_ARTIFACTS_EMBEDDED",
        )
    )
    checks.append(
        _check(
            "non-claims remain false",
            _declared_non_claims_false(request),
            _false_non_claims(),
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": _sanitize(reason) if reason is not None else BLOCK_REASONS.get(code or "", code),
        "v2_raw_full_prior_artifact_values_omitted": True,
    }


def _determine_block_code(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    malformed_code: str | None,
) -> str | None:
    if malformed_code:
        return malformed_code
    if request.get("invocation_request_admission_intent") == INTENT_BLOCK:
        return "INVOCATION_REQUEST_ADMISSION_REVIEW_EXPLICITLY_BLOCKED"
    if request.get("requested_invocation_request_admission_outcome") == OUTCOME_BLOCKED:
        return "INVOCATION_REQUEST_ADMISSION_REVIEW_EXPLICITLY_BLOCKED"
    requested = request.get("requested_invocation_request_admission_outcome")
    if _present(requested) and requested not in OUTCOME_FAMILY:
        return "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED"
    if _contains_forbidden_full_body_key(request) or _contains_truthy_key(request, "full_prior_artifacts_embedded"):
        return "FULL_PRIOR_ARTIFACTS_EMBEDDED"
    return _first_failed_code(checks)


def _determine_outcome(request: Mapping[str, Any], block_code: str | None) -> str:
    if block_code is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_invocation_request_admission_outcome")
    if requested in {OUTCOME_ADMITTED, OUTCOME_NOT_ADMITTED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return str(requested)
    if request.get("invocation_request_admission_intent") == INTENT_DO_NOT_ADMIT:
        return OUTCOME_NOT_ADMITTED
    return OUTCOME_ADMITTED


def _statement(outcome: str, sections: Mapping[str, Mapping[str, Any]], request: Mapping[str, Any]) -> dict[str, Any]:
    admitted = outcome == OUTCOME_ADMITTED
    forbidden = _contains_forbidden_full_body_key(request)
    statement = {key: admitted for key in ADMITTED_TRUE_FIELDS}
    statement.update(
        {
            "selected_command_execution_boundary_basis_preserved": bool(sections["selected_command_execution_boundary_basis"].get("command_execution_boundary_basis_preserved")),
            "selected_command_report_basis_preserved": bool(sections["selected_command_report_basis"].get("command_report_basis_preserved")),
            "selected_command_implementation_basis_preserved": bool(sections["selected_command_implementation_basis"].get("command_implementation_basis_preserved")),
            "selected_artifact_emission_containment_basis_preserved": bool(sections["selected_artifact_emission_containment_basis"].get("artifact_emission_containment_basis_preserved")),
            "selected_evidence_manifest_basis_preserved": bool(sections["selected_evidence_manifest_basis"].get("evidence_manifest_basis_preserved")),
            "selected_portable_verification_basis_preserved": bool(sections["selected_portable_verification_basis"].get("portable_verification_basis_preserved")),
            "request_admission_only": True,
            "one_shot_invocation_request_only": True,
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "no_standing_invocation_lane_created": True,
            "no_repeat_invocation_permission_created": True,
            "invocation_requires_separate_execution_step": True,
            "command_output_must_be_non_source": True,
            "command_result_must_be_non_authority": True,
            "command_success_must_not_create_currentness": True,
            "command_success_must_not_claim_final_completion": True,
            "invocation_must_use_reference_shaped_input": True,
            "invocation_must_not_mutate_artifacts": True,
            "invocation_must_not_embed_full_prior_artifacts": True,
            "request_admission_basis_is_reference_shaped": not forbidden,
            "forbidden_full_body_posture_detected": forbidden,
            "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request),
            "v2_raw_full_prior_artifact_values_omitted": True,
            "successor_preserves_v1_as_historical_predecessor": True,
            "successor_does_not_repair_or_hide_v1": True,
            "successor_does_not_claim_v1_passed": True,
        }
    )
    statement.update(_false_non_claims())
    return statement


def _non_meaning() -> dict[str, bool]:
    labels = (
        "command_invoked",
        "command_executed",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "live_verification_completed",
        "invocation_permission_reusable",
        "standing_invocation_lane_exists",
        "repeated_invocations_authorized",
        "command_output_became_source",
        "command_result_became_authority",
        "command_success_created_currentness",
        "command_success_claimed_final_completion",
        "deployment_created",
        "runtime_hosting_created",
        "public_release_created",
        "public_readiness_created",
        "operation_permission_created",
        "continuation_authorized",
        "reusable_permission_created",
        "derivative_reception_authorized",
        "vessel_relation_authorized",
        "another_reception_request_authorized",
        "follow_on_work_authorized",
    )
    return {f"request_admission_does_not_mean_{label}": True for label in labels}


def _additional_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": requires,
        "additional_basis_context": _sanitize(request.get("additional_basis_context") if requires else {}),
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
        "command_not_invoked": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "standing_invocation_lane_not_created": True,
        "repeat_invocation_permission_not_created": True,
        "artifacts_not_mutated": True,
        "v2_raw_full_prior_artifact_values_omitted": True,
    }


def _not_admitted(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    not_admitted = outcome == OUTCOME_NOT_ADMITTED
    return {
        "not_admitted": not_admitted,
        "not_admitted_basis": _sanitize(request.get("not_admitted_basis") if not_admitted else {}),
        "failed_checks": _sanitize([check for check in checks if check.get("passed") is not True] if not_admitted else []),
        "not_admitted_does_not_repair": True,
        "not_admitted_does_not_authorize_invocation": True,
        "not_admitted_does_not_run_command": True,
        "not_admitted_does_not_mutate_artifacts": True,
        "not_admitted_does_not_deploy_or_publish": True,
        "not_admitted_does_not_create_currentness": True,
        "not_admitted_does_not_claim_final_completion": True,
        "not_admitted_does_not_authorize_continuation": True,
        "not_admitted_does_not_create_reusable_permission": True,
        "not_admitted_does_not_authorize_derivative_reception": True,
        "not_admitted_does_not_authorize_vessel_relation": True,
        "not_admitted_does_not_authorize_another_reception_request": True,
        "not_admitted_does_not_authorize_follow_on_work": True,
        "v2_raw_full_prior_artifact_values_omitted": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "request/admission v2 test",
            "request/admission v2 live artifact",
            "actual command invocation",
            "command output from live execution",
            "command result from live execution",
            "command success",
            "live verification result",
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


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = _safe_component(request.get("invocation_request_admission_id"), "unidentified")
    return {
        "single_live_command_invocation_request_admission_result_id": f"{request_id}__single_live_command_invocation_request_admission_result_v2",
        "single_live_command_invocation_request_admission_result_type": "portable_source_body_verification_single_live_command_invocation_request_admission_boundary_result",
        "single_live_command_invocation_request_admission_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of": SUCCESSOR_OF,
        "successor_reason": SUCCESSOR_REASON,
        "v1_lineage_posture": "v1 remains historical predecessor evidence and is not repaired by v2",
        "v2_containment_correction": "raw forbidden full prior artifact body values are omitted from returned results",
    }


def _declared_question(request: Mapping[str, Any], request_path: Path | str | None) -> dict[str, Any]:
    return {
        "invocation_request_admission_id": _sanitize(request.get("invocation_request_admission_id")),
        "invocation_request_admission_question": _sanitize(request.get("invocation_request_admission_question")),
        "invocation_request_admission_intent": _sanitize(request.get("invocation_request_admission_intent")),
        "requested_invocation_request_admission_outcome": _sanitize(request.get("requested_invocation_request_admission_outcome")),
        "declared_invocation_request_admission_path": str(request_path) if request_path is not None else None,
        "question_answered": (
            "Can one future live command invocation request be admitted for later execution "
            "without invoking, executing, creating command output, creating command result, "
            "creating command success, creating a standing invocation lane, creating repeat "
            "invocation permission, or authorizing follow-on work?"
        ),
        "request_admission_is_not_invocation": True,
        "request_admission_is_not_execution": True,
        "request_admission_is_not_output": True,
        "request_admission_is_not_result": True,
        "request_admission_is_not_success": True,
        "request_admission_does_not_authorize_immediate_invocation": True,
        "v2_raw_full_prior_artifact_values_omitted": True,
    }


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, "DECLARED_INVOCATION_REQUEST_ADMISSION_UNREADABLE", str(exc)
    except json.JSONDecodeError as exc:
        return None, "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED", str(exc)
    if not isinstance(loaded, dict):
        return None, "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED", "JSON document must be an object."
    return loaded, None, None


def _build_result(
    request_value: Any,
    *,
    request_path: Path | str | None = None,
    malformed_code: str | None = None,
    path_reason: str | None = None,
) -> dict[str, Any]:
    request = _copy(request_value) if isinstance(request_value, Mapping) else {}
    if not isinstance(request_value, Mapping) and malformed_code is None:
        malformed_code = "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED"

    sections = {
        result_key: _reference_section(request, result_key, label, path_key, id_key, status_key)
        for result_key, label, _code, path_key, id_key, status_key in BASIS_FIELDS
    }
    checks = _build_checks(request, malformed_code)
    block_code = _determine_block_code(request, checks, malformed_code)
    outcome = _determine_outcome(request, block_code)
    statement = _statement(outcome, sections, request)

    result: dict[str, Any] = {
        "single_live_command_invocation_request_admission_metadata": _metadata(request),
        "declared_invocation_request_admission_question": _declared_question(request, request_path),
        "selected_command_execution_boundary_basis": sections["selected_command_execution_boundary_basis"],
        "selected_command_report_basis": sections["selected_command_report_basis"],
        "selected_command_implementation_basis": sections["selected_command_implementation_basis"],
        "selected_artifact_emission_containment_basis": sections["selected_artifact_emission_containment_basis"],
        "selected_evidence_manifest_basis": sections["selected_evidence_manifest_basis"],
        "selected_portable_verification_basis": sections["selected_portable_verification_basis"],
        "proposed_one_shot_invocation_mode": _proposal_section(request.get("proposed_one_shot_invocation_mode"), "proposed_one_shot_invocation_mode"),
        "proposed_invocation_surface": _proposal_section(request.get("proposed_invocation_surface"), "proposed_invocation_surface"),
        "proposed_input_reference_bundle": _proposal_section(request.get("proposed_input_reference_bundle"), "proposed_input_reference_bundle"),
        "proposed_output_report_destination": _proposal_section(request.get("proposed_output_report_destination"), "proposed_output_report_destination"),
        "single_invocation_scope": _proposal_section(request.get("single_invocation_scope"), "single_invocation_scope"),
        "no_repeat_posture": _proposal_section(request.get("no_repeat_posture"), "no_repeat_posture"),
        "no_standing_invocation_lane_posture": _proposal_section(request.get("no_standing_invocation_lane_posture"), "no_standing_invocation_lane_posture"),
        "refusal_conditions": _limit_section(request.get("refusal_conditions"), "refusal_conditions"),
        "output_limits": _limit_section(request.get("output_limits"), "output_limits"),
        "result_limits": _limit_section(request.get("result_limits"), "result_limits"),
        "success_limits": _limit_section(request.get("success_limits"), "success_limits"),
        "request_admission_scope": _scope_section(request.get("request_admission_scope")),
        "request_admission_checks": {
            "checks": _sanitize(checks),
            "passed_check_count": sum(1 for check in checks if check["passed"]),
            "failed_check_count": sum(1 for check in checks if not check["passed"]),
            "v2_raw_full_prior_artifact_values_omitted": True,
        },
        "request_admission_statement": statement,
        "request_admission_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis(outcome, request),
        "not_admitted_basis": _not_admitted(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code, path_reason),
    }
    result["single_live_command_invocation_request_admission_summary"] = (
        build_portable_source_body_verification_single_live_command_invocation_request_admission_summary_v2(
            result
        )
    )
    return _sanitize(result)


def resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
    declared_invocation_request_admission: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared request/admission mapping with v2 containment."""

    if declared_invocation_request_admission is None:
        return _build_result({})
    if not isinstance(declared_invocation_request_admission, Mapping):
        return _build_result({}, malformed_code="DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED")
    return _build_result(declared_invocation_request_admission)


def resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2_from_path(
    declared_invocation_request_admission_path: Path | str,
) -> dict:
    """Resolve one declared request/admission JSON object from a path."""

    request, error_code, error_reason = _read_json_object(declared_invocation_request_admission_path)
    if error_code:
        return _build_result(
            {},
            request_path=declared_invocation_request_admission_path,
            malformed_code=error_code,
            path_reason=error_reason,
        )
    return _build_result(request, request_path=declared_invocation_request_admission_path)


def build_portable_source_body_verification_single_live_command_invocation_request_admission_summary_v2(
    result: Mapping[str, Any]
) -> dict:
    """Build a compact non-authoritative v2 request/admission summary."""

    safe_result = _sanitize(result)
    statement = _as_mapping(safe_result.get("request_admission_statement"))
    checks = _as_mapping(safe_result.get("request_admission_checks"))
    block = _as_mapping(safe_result.get("block"))
    question = _as_mapping(safe_result.get("declared_invocation_request_admission_question"))
    non_claims = _as_mapping(safe_result.get("non_claims"))
    metadata = _as_mapping(safe_result.get("single_live_command_invocation_request_admission_metadata"))
    return {
        "outcome": safe_result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "invocation_request_admission_id": question.get("invocation_request_admission_id"),
        "invocation_request_admission_question": question.get("invocation_request_admission_question"),
        "invocation_request_admission_intent": question.get("invocation_request_admission_intent"),
        "passed_check_count": checks.get("passed_check_count", 0),
        "failed_check_count": checks.get("failed_check_count", 0),
        "single_invocation_request_admitted": statement.get("single_live_command_invocation_request_admitted", False),
        "single_invocation_request_declared": statement.get("single_invocation_request_declared", False),
        "single_invocation_scope_bounded": statement.get("single_invocation_scope_bounded", False),
        "admission_conditions_declared": statement.get("single_invocation_admission_conditions_declared", False),
        "execution_still_not_performed": statement.get("single_invocation_execution_still_not_performed", False),
        "requires_separate_execution_step": statement.get("single_invocation_requires_separate_execution_step", False),
        "not_admitted": safe_result.get("outcome") == OUTCOME_NOT_ADMITTED,
        "requires_additional_basis": safe_result.get("outcome") == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_command_execution_boundary_basis_preserved": statement.get("selected_command_execution_boundary_basis_preserved", False),
        "selected_command_report_basis_preserved": statement.get("selected_command_report_basis_preserved", False),
        "selected_command_implementation_basis_preserved": statement.get("selected_command_implementation_basis_preserved", False),
        "artifact_emission_containment_basis_preserved": statement.get("selected_artifact_emission_containment_basis_preserved", False),
        "evidence_manifest_basis_preserved": statement.get("selected_evidence_manifest_basis_preserved", False),
        "portable_verification_basis_preserved": statement.get("selected_portable_verification_basis_preserved", False),
        "request_admission_only": statement.get("request_admission_only", False),
        "one_shot_invocation_request_only": statement.get("one_shot_invocation_request_only", False),
        "command_invocation_not_created": statement.get("command_invocation_not_created", False),
        "command_execution_not_performed": statement.get("command_execution_not_performed", False),
        "command_output_not_created": statement.get("command_output_not_created", False),
        "command_result_not_created": statement.get("command_result_not_created", False),
        "command_success_not_created": statement.get("command_success_not_created", False),
        "no_standing_invocation_lane": statement.get("no_standing_invocation_lane_created", False),
        "no_repeat_invocation_permission": statement.get("no_repeat_invocation_permission_created", False),
        "output_not_source": statement.get("command_output_must_be_non_source", False),
        "result_not_authority": statement.get("command_result_must_be_non_authority", False),
        "success_not_currentness": statement.get("command_success_must_not_create_currentness", False),
        "success_not_final_completion": statement.get("command_success_must_not_claim_final_completion", False),
        "reference_shaped_input_required": statement.get("invocation_must_use_reference_shaped_input", False),
        "no_full_prior_artifacts_embedded": not non_claims.get("full_prior_artifacts_embedded", True),
        "no_artifact_mutation": not non_claims.get("prior_artifacts_mutated", True),
        "forbidden_full_body_posture_detected": statement.get("forbidden_full_body_posture_detected", False),
        "forbidden_full_body_keys_detected": statement.get("forbidden_full_body_keys_detected", []),
        "v2_raw_full_prior_artifact_values_omitted": True,
        "successor_of": metadata.get("successor_of"),
        "successor_reason": metadata.get("successor_reason"),
        "successor_does_not_repair_or_hide_v1": statement.get("successor_does_not_repair_or_hide_v1", True),
        "successor_does_not_claim_v1_passed": statement.get("successor_does_not_claim_v1_passed", True),
        "no_operation_permission_public_readiness_final_completion": (
            not non_claims.get("operation_permission_created", True)
            and not non_claims.get("public_launch_readiness_created", True)
            and not non_claims.get("final_completion_claimed", True)
        ),
        "no_continuation_publication_flow_reusable_permission": (
            not non_claims.get("continuation_authorized", True)
            and not non_claims.get("publication_flow_opened", True)
            and not non_claims.get("reusable_permission_created", True)
        ),
        "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": (
            not non_claims.get("derivative_reception_authorized", True)
            and not non_claims.get("vessel_relation_authorized", True)
            and not non_claims.get("another_reception_request_authorized", True)
            and not non_claims.get("follow_on_work_authorized", True)
        ),
        "key_non_claims": _sanitize(non_claims),
    }


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v2 request/admission result JSON artifact."""

    result_copy = _sanitize(result)
    if output_path is None:
        question = _as_mapping(result_copy.get("declared_invocation_request_admission_question"))
        request_id = _safe_component(question.get("invocation_request_admission_id"), "invocation_request_admission")
        path = (
            PORTABLE_SOURCE_BODY_VERIFICATION_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_V2_ROOT
            / f"{request_id}__single_live_command_invocation_request_admission_result_v2.json"
        )
    else:
        path = Path(output_path)
        if path.suffix.lower() != ".json":
            question = _as_mapping(result_copy.get("declared_invocation_request_admission_question"))
            request_id = _safe_component(question.get("invocation_request_admission_id"), "invocation_request_admission")
            path = path / f"{request_id}__single_live_command_invocation_request_admission_result_v2.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = _unique_path(path)
    final_path.write_text(
        json.dumps(result_copy, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return final_path
