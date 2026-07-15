"""Resolve admitted single live command invocation request consumption.

This resolver answers one question only:

    Can the already-admitted single live command invocation request be consumed
    exactly once as closed basis for a later command execution review, without
    invoking or executing the command and without creating command output,
    command result, command success, standing invocation lane, repeat
    permission, execution permission, authority, currentness, final completion,
    continuation, reusable permission, derivative reception, vessel relation,
    another reception request, or follow-on work?

The resolver records request consumption only. It closes the admitted one-shot
request token as consumed basis when the declared basis is bounded. It does not
invoke or execute a command, create command output/result/success, create
execution permission, repair or hide the predecessor line, mutate artifacts,
deploy, host, publish, create authority/currentness, or authorize follow-on
work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class PortableSourceBodyVerificationAdmittedSingleLiveCommandInvocationRequestConsumptionError(
    Exception
):
    """Raised for hard request-consumption input/output failures."""


RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_admitted_single_live_command_"
    "invocation_request_consumption"
)
RESULT_VERSION = "0.1.0"
PORTABLE_SOURCE_BODY_VERIFICATION_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_portable_source_body_verification_"
    "admitted_single_live_command_invocation_request_consumption"
)

OUTCOME_CONSUMED = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMED"
OUTCOME_NOT_CONSUMED = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_NOT_CONSUMED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_CONSUMED,
    OUTCOME_NOT_CONSUMED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION"
)
INTENT_BLOCK = "BLOCK_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_REVIEW"
SUPPORTED_REQUEST_CONSUMPTION_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SELECTED_ADMISSION_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
SELECTED_ADMISSION_VERSION = "0.2.0"
SELECTED_ADMISSION_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary_v2"
)
PREDECESSOR_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_"
    "request_admission_boundary"
)
CONSUMPTION_BOUNDARY_RECORDED_OUTCOME = (
    "ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BOUNDARY_RECORDED"
)

SUPPORTED_REQUEST_CONSUMPTION_SCOPE = {
    "REQUEST_CONSUMPTION_ONLY",
    "ADMITTED_REQUEST_CONSUMED_AS_BASIS_ONLY",
    "ONE_SHOT_CONSUMPTION_ONLY",
    "CONSUMED_REQUEST_BASIS_FOR_LATER_EXECUTION_REVIEW_ONLY",
    "COMMAND_INVOCATION_NOT_CREATED",
    "COMMAND_EXECUTION_NOT_PERFORMED",
    "COMMAND_OUTPUT_NOT_CREATED",
    "COMMAND_RESULT_NOT_CREATED",
    "COMMAND_SUCCESS_NOT_CREATED",
    "NO_STANDING_INVOCATION_LANE_CREATED",
    "NO_REPEAT_INVOCATION_PERMISSION_CREATED",
    "EXECUTION_REQUIRES_SEPARATE_REVIEW",
    "CONSUMPTION_IS_NOT_EXECUTION_PERMISSION",
    "CONSUMPTION_IS_NOT_COMMAND_SUCCESS",
    "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE",
    "V2_SUCCESSOR_DOES_NOT_REPAIR_V1",
    "RETURNED_RESULT_CONTAINMENT_PRESERVED",
    "REFERENCE_SHAPED_BASIS_REQUIRED",
    "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED",
    "NO_AUTHORITY_CREATED",
    "NO_CURRENTNESS_CREATED",
    "NO_FINAL_COMPLETION",
    "NO_CONTINUATION_AUTHORIZED",
    "NO_REUSABLE_PERMISSION",
    "NO_FOLLOW_ON_WORK_AUTHORIZED",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "command_invocation_created",
    "command_executed",
    "command_execution_performed",
    "command_output_created",
    "command_result_created",
    "command_success_created",
    "standing_invocation_lane_created",
    "repeat_invocation_permission_created",
    "consumption_treated_as_execution_permission",
    "consumption_treated_as_command_success",
    "command_output_became_source",
    "command_result_became_authority",
    "command_success_created_currentness",
    "command_success_claimed_final_completion",
    "command_became_authority",
    "full_prior_artifacts_embedded",
    "raw_full_prior_artifact_body_returned",
    "prior_artifacts_mutated",
    "v1_repaired",
    "v1_hidden",
    "v1_claimed_passed",
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
            "command_invocation_exists",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "execution_permission_created",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "source_receipt_created",
            "reception_authorized",
            "authority_created",
            "currentness_created",
            "adoption_created",
            "standing_created",
            "public_readiness_created",
            "publication_flow_authorized",
            "next_work_authorized",
        )
    )
)

ALLOWED_CONSUMED_TRUE_FIELDS = (
    "admitted_single_live_command_invocation_request_consumed",
    "request_consumed",
    "consumption_token_closed",
    "consumed_request_basis_recorded",
    "one_shot_consumption_preserved",
    "execution_requires_separate_review",
    "v1_predecessor_failure_preserved",
    "returned_result_containment_preserved",
)

FORBIDDEN_FULL_BODY_KEYS = {
    "full_artifact_body",
    "raw_full_artifact_body",
    "full_prior_artifact_body",
    "raw_prior_artifact_body",
    "artifact_body",
    "complete_artifact_body",
    "raw_artifact",
    "embedded_artifact",
    "selected_full_artifact",
    "full_result",
    "raw_result",
    "complete_result",
    "raw_body",
    "full_body",
}
FULL_BODY_OMISSION_MARKER = (
    "[OMITTED: full prior artifact body blocked by admitted single live command "
    "invocation request consumption]"
)

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")

COLLAPSE_FIELD_CODES = (
    ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
    ("command_invocation_exists", "COMMAND_INVOCATION_CREATED"),
    ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
    ("command_output_created", "COMMAND_OUTPUT_CREATED"),
    ("command_output_exists", "COMMAND_OUTPUT_CREATED"),
    ("command_result_created", "COMMAND_RESULT_CREATED"),
    ("command_result_exists", "COMMAND_RESULT_CREATED"),
    ("command_success_created", "COMMAND_SUCCESS_CREATED"),
    ("command_success_exists", "COMMAND_SUCCESS_CREATED"),
    ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
    ("standing_invocation_lane_exists", "STANDING_INVOCATION_LANE_CREATED"),
    ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    ("repeated_invocations_authorized", "REPEAT_INVOCATION_PERMISSION_CREATED"),
    (
        "consumption_treated_as_execution_permission",
        "CONSUMPTION_TREATED_AS_EXECUTION_PERMISSION",
    ),
    (
        "request_consumption_treated_as_execution_permission",
        "CONSUMPTION_TREATED_AS_EXECUTION_PERMISSION",
    ),
    ("execution_permission_created", "CONSUMPTION_TREATED_AS_EXECUTION_PERMISSION"),
    ("consumption_treated_as_command_success", "CONSUMPTION_TREATED_AS_COMMAND_SUCCESS"),
    (
        "request_consumption_treated_as_command_success",
        "CONSUMPTION_TREATED_AS_COMMAND_SUCCESS",
    ),
    ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_output_treated_as_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
    ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
    ("command_result_treated_as_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
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
    ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
    ("raw_full_prior_artifact_body_returned", "FULL_PRIOR_ARTIFACT_BODY_EMITTED"),
    ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifacts_mutated", "ARTIFACTS_MUTATED"),
    ("artifact_mutation_performed", "ARTIFACTS_MUTATED"),
    ("v1_repaired", "V2_TREATED_AS_REPAIRING_V1"),
    ("v2_treated_as_repairing_v1", "V2_TREATED_AS_REPAIRING_V1"),
    ("v1_hidden", "V1_FAILURE_HIDDEN"),
    ("v1_failure_hidden", "V1_FAILURE_HIDDEN"),
    ("v1_claimed_passed", "V1_CLAIMED_PASSED"),
    ("v1_passed", "V1_CLAIMED_PASSED"),
    ("deployment_created", "DEPLOYMENT_CREATED"),
    ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
    ("public_release_created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
    ("public_launch_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
    ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
    ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
    ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
    ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
    ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
    ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
)

REQUIRED_BASIS_FIELDS = (
    (
        "selected v2 admitted request basis declared",
        "selected_v2_admitted_request_basis",
        "V2_ADMITTED_REQUEST_BASIS_MISSING",
    ),
    (
        "selected consumption-boundary live artifact basis declared",
        "selected_consumption_boundary_basis",
        "CONSUMPTION_BOUNDARY_BASIS_MISSING",
    ),
    (
        "selected consumption-boundary terminal summary basis declared",
        "selected_consumption_boundary_terminal_summary_basis",
        "CONSUMPTION_BOUNDARY_TERMINAL_SUMMARY_MISSING",
    ),
    (
        "selected v1 predecessor/failure basis declared",
        "selected_v1_predecessor_failure_basis",
        "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
    ),
)

REQUIRED_POSTURE_FIELDS = (
    (
        "one-shot consumption posture declared",
        "one_shot_consumption_posture",
        "ONE_SHOT_CONSUMPTION_POSTURE_MISSING",
    ),
    (
        "consumed-request-basis posture declared",
        "consumed_request_basis",
        "CONSUMED_REQUEST_BASIS_MISSING",
    ),
    (
        "no-standing-lane posture declared",
        "no_standing_lane_posture",
        "NO_STANDING_LANE_POSTURE_MISSING",
    ),
    (
        "no-repeat-permission posture declared",
        "no_repeat_permission_posture",
        "NO_REPEAT_PERMISSION_POSTURE_MISSING",
    ),
)

BLOCK_REASONS = {
    "DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED": (
        "Declared request-consumption request is malformed."
    ),
    "DECLARED_REQUEST_CONSUMPTION_REQUEST_UNREADABLE": (
        "Declared request-consumption request path could not be read."
    ),
    "REQUEST_CONSUMPTION_QUESTION_UNDECLARED": (
        "Request-consumption question is undeclared."
    ),
    "REQUEST_CONSUMPTION_INTENT_UNSUPPORTED": (
        "Request-consumption intent is unsupported."
    ),
    "REQUEST_CONSUMPTION_REVIEW_EXPLICITLY_BLOCKED": (
        "Request-consumption review was explicitly blocked by declared intent."
    ),
    "V2_ADMITTED_REQUEST_BASIS_MISSING": "Selected admitted request basis is missing.",
    "V2_ADMITTED_REQUEST_NOT_ADMITTED": (
        "Selected admitted request basis is not an admitted request."
    ),
    "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0": (
        "Selected admitted request basis is not version 0.2.0."
    ),
    "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT": (
        "Selected admitted request basis has failed checks."
    ),
    "V2_SUCCESSOR_METADATA_MISSING": (
        "Selected admitted request basis lacks successor metadata."
    ),
    "V2_RETURNED_RESULT_CONTAINMENT_MISSING": (
        "Selected admitted request basis does not preserve returned-result containment."
    ),
    "CONSUMPTION_BOUNDARY_BASIS_MISSING": (
        "Selected consumption-boundary live artifact basis is missing."
    ),
    "CONSUMPTION_BOUNDARY_NOT_RECORDED": (
        "Selected consumption-boundary basis is not recorded."
    ),
    "CONSUMPTION_BOUNDARY_FAILED_CHECKS_PRESENT": (
        "Selected consumption-boundary basis has failed checks."
    ),
    "CONSUMPTION_BOUNDARY_TERMINAL_SUMMARY_MISSING": (
        "Selected consumption-boundary terminal summary basis is missing."
    ),
    "V1_PREDECESSOR_FAILURE_BASIS_MISSING": (
        "Selected predecessor/failure basis is missing."
    ),
    "V2_TREATED_AS_REPAIRING_V1": "Successor basis is treated as repairing v1.",
    "V1_FAILURE_HIDDEN": "Predecessor failure evidence is hidden.",
    "V1_CLAIMED_PASSED": "Predecessor line is claimed passed.",
    "UNSUPPORTED_REQUEST_CONSUMPTION_SCOPE": (
        "Request-consumption scope contains unsupported values."
    ),
    "FULL_PRIOR_ARTIFACT_BODY_EMITTED": (
        "Raw full prior artifact body posture is present."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "Required non-claims are missing or not explicitly false."
    ),
}


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


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
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "created", "authorized"}
    return False


def _to_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return None
    return None


def _safe_component(value: Any, fallback: str) -> str:
    text = str(value).strip() if value is not None else ""
    if not text:
        text = fallback
    safe = []
    for char in text:
        if char.isalnum() or char in {"-", "_", "."}:
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("._") or fallback


def _false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text.lower() in FORBIDDEN_FULL_BODY_KEYS:
                result[key_text] = FULL_BODY_OMISSION_MARKER
            else:
                result[key_text] = _sanitize(item)
        return result
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return _copy(value)


def _contains_forbidden_full_body_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in FORBIDDEN_FULL_BODY_KEYS:
                return True
            if _contains_forbidden_full_body_key(item):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_forbidden_full_body_key(item) for item in value)
    return False


def _forbidden_full_body_keys(value: Any) -> list[str]:
    found: list[str] = []

    def walk(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                key_text = str(key)
                if key_text.lower() in FORBIDDEN_FULL_BODY_KEYS:
                    found.append(key_text)
                walk(child)
        elif isinstance(item, Sequence) and not isinstance(item, (str, bytes, bytearray)):
            for child in item:
                walk(child)

    walk(value)
    return sorted(dict.fromkeys(found))


def _contains_truthy_key(value: Any, key_name: str) -> bool:
    key_name = key_name.lower()
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() == key_name and _truthy(item):
                return True
            if _contains_truthy_key(item, key_name):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, key_name) for item in value)
    return False


def _first_truthy_key(value: Any, key_names: Sequence[str]) -> str | None:
    names = {name.lower() for name in key_names}
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            if key_text.lower() in names and _truthy(item):
                return key_text
            nested = _first_truthy_key(item, key_names)
            if nested is not None:
                return nested
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            nested = _first_truthy_key(item, key_names)
            if nested is not None:
                return nested
    return None


def _find_first(value: Any, keys: Sequence[str]) -> Any:
    names = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in names and _present(item):
                return item
        for item in value.values():
            found = _find_first(item, keys)
            if _present(found):
                return found
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for item in value:
            found = _find_first(item, keys)
            if _present(found):
                return found
    return None


def _find_truthy(value: Any, keys: Sequence[str]) -> bool:
    names = {key.lower() for key in keys}
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key).lower() in names and _truthy(item):
                return True
            if _find_truthy(item, keys):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_find_truthy(item, keys) for item in value)
    return False


def _scope_values(value: Any) -> list[str]:
    if isinstance(value, Mapping):
        for key in ("selected_scope_values", "scope_values", "request_consumption_scope"):
            selected = value.get(key)
            if isinstance(selected, Sequence) and not isinstance(
                selected, (str, bytes, bytearray)
            ):
                return [str(item) for item in selected]
        values = []
        for key, item in value.items():
            if isinstance(key, str) and key.upper() == key and _truthy(item):
                values.append(key)
        return values
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence):
        return [str(item) for item in value]
    return []


def _declared_non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    return all(name in non_claims and non_claims[name] is False for name in REQUIRED_FALSE_NON_CLAIMS)


def _declared_non_claims_actual(request: Mapping[str, Any]) -> dict[str, Any]:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return {
            "declared_non_claims_present": False,
            "missing_non_claims": list(REQUIRED_FALSE_NON_CLAIMS),
            "flipped_non_claims": [],
        }
    missing = [name for name in REQUIRED_FALSE_NON_CLAIMS if name not in non_claims]
    flipped = [
        name
        for name in REQUIRED_FALSE_NON_CLAIMS
        if name in non_claims and non_claims[name] is not False
    ]
    return {
        "declared_non_claims_present": True,
        "missing_non_claims": missing,
        "flipped_non_claims": flipped,
        "declared_non_claims": _sanitize(non_claims),
    }


def _selected_basis_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return _sanitize(value)
    if isinstance(value, (str, Path)):
        return {
            "selected_basis_reference": str(value),
            "selected_basis_is_path_reference": True,
        }
    return _sanitize(value)


def _basis_section(value: Any, label: str) -> dict[str, Any]:
    declared = _present(value)
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": declared,
        "selected_basis": _selected_basis_value(value) if declared else {},
        "selected_basis_is_reference_shaped": declared and not forbidden,
        "selected_basis_remains_non_authoritative": True,
        "selected_basis_does_not_invoke_command": True,
        "selected_basis_does_not_execute_command": True,
        "selected_basis_does_not_create_command_output": True,
        "selected_basis_does_not_create_command_result": True,
        "selected_basis_does_not_create_command_success": True,
        "selected_basis_does_not_create_standing_lane": True,
        "selected_basis_does_not_create_repeat_permission": True,
        "selected_basis_does_not_create_execution_permission": True,
        "selected_basis_does_not_create_authority_currentness_final_completion": True,
        "selected_basis_does_not_authorize_continuation_or_follow_on_work": True,
        "full_prior_artifact_body_not_emitted": not forbidden,
        "prior_artifacts_not_mutated": True,
    }


def _v2_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_v2_admitted_request_basis")


def _v2_outcome(request: Mapping[str, Any]) -> Any:
    basis = _v2_basis(request)
    return (
        request.get("selected_v2_admitted_request_outcome")
        or _find_first(
            basis,
            (
                "selected_v2_admitted_request_outcome",
                "selected_result_outcome",
                "outcome",
            ),
        )
    )


def _v2_version(request: Mapping[str, Any]) -> Any:
    basis = _v2_basis(request)
    return (
        request.get("selected_v2_admitted_request_version")
        or _find_first(
            basis,
            (
                "selected_v2_admitted_request_version",
                "single_live_command_invocation_request_admission_result_version",
                "selected_result_version",
                "result_version",
                "version",
            ),
        )
    )


def _v2_failed_check_count(request: Mapping[str, Any]) -> int | None:
    basis = _v2_basis(request)
    for value in (
        request.get("selected_v2_failed_check_count"),
        _find_first(
            basis,
            (
                "selected_v2_failed_check_count",
                "selected_result_failed_check_count",
                "failed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _v2_passed_check_count(request: Mapping[str, Any]) -> int | None:
    basis = _v2_basis(request)
    for value in (
        request.get("selected_v2_passed_check_count"),
        _find_first(
            basis,
            (
                "selected_v2_passed_check_count",
                "selected_result_passed_check_count",
                "passed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _v2_successor_metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    explicit = request.get("selected_v2_successor_metadata")
    basis = _v2_basis(request)
    metadata = _sanitize(explicit) if isinstance(explicit, Mapping) else {}
    successor_of = metadata.get("successor_of") or _find_first(basis, ("successor_of",))
    successor_reason = metadata.get("successor_reason") or _find_first(
        basis, ("successor_reason",)
    )
    resolver_module = metadata.get("resolver_module") or _find_first(
        basis, ("resolver_module",)
    )
    if successor_of is not None:
        metadata["successor_of"] = _sanitize(successor_of)
    if successor_reason is not None:
        metadata["successor_reason"] = _sanitize(successor_reason)
    if resolver_module is not None:
        metadata["resolver_module"] = _sanitize(resolver_module)
    return metadata


def _v2_successor_metadata_preserved(request: Mapping[str, Any]) -> bool:
    metadata = _v2_successor_metadata(request)
    successor_of = metadata.get("successor_of")
    successor_reason = metadata.get("successor_reason")
    resolver_module = metadata.get("resolver_module")
    return (
        successor_of == PREDECESSOR_RESOLVER_MODULE
        and _present(successor_reason)
        and resolver_module in {None, SELECTED_ADMISSION_RESOLVER_MODULE}
    )


def _returned_result_containment_preserved(request: Mapping[str, Any]) -> bool:
    basis = _v2_basis(request)
    posture = request.get("returned_result_containment_posture")
    return (
        _find_truthy(
            basis,
            (
                "returned_result_containment_preserved",
                "v2_raw_full_prior_artifact_values_omitted",
                "raw_full_prior_artifact_values_omitted",
                "full_prior_artifact_body_not_returned",
            ),
        )
        or _find_truthy(
            posture,
            (
                "returned_result_containment_preserved",
                "raw_full_prior_artifact_body_not_returned",
                "full_prior_artifact_body_not_emitted",
            ),
        )
    )


def _selected_v2_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _v2_basis(request)
    section = _basis_section(basis, "selected_v2_admitted_request_basis")
    section.update(
        {
            "selected_v2_admitted_request_artifact_id": _sanitize(
                request.get("selected_v2_admitted_request_artifact_id")
                or _find_first(
                    basis,
                    (
                        "single_live_command_invocation_request_admission_result_id",
                        "selected_result_id",
                        "result_id",
                    ),
                )
            ),
            "selected_v2_admitted_request_artifact_path": _sanitize(
                request.get("selected_v2_admitted_request_artifact_path")
                or _find_first(basis, ("selected_result_path", "artifact_path", "path"))
            ),
            "selected_v2_admitted_request_outcome": _sanitize(_v2_outcome(request)),
            "selected_v2_admitted_request_version": _sanitize(_v2_version(request)),
            "selected_v2_failed_check_count": _v2_failed_check_count(request),
            "selected_v2_passed_check_count": _v2_passed_check_count(request),
            "selected_v2_successor_metadata": _v2_successor_metadata(request),
            "selected_v2_outcome_is_admitted_request": (
                _v2_outcome(request) == SELECTED_ADMISSION_OUTCOME
            ),
            "selected_v2_version_is_0_2_0": _v2_version(request) == SELECTED_ADMISSION_VERSION,
            "selected_v2_failed_check_count_zero": _v2_failed_check_count(request) == 0,
            "selected_v2_successor_metadata_preserved": _v2_successor_metadata_preserved(
                request
            ),
            "selected_v2_returned_result_containment_preserved": _returned_result_containment_preserved(
                request
            ),
            "admitted_request_basis_is_consumed_once_only_in_consumed_outcome": True,
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_result_success_not_created": True,
            "no_standing_invocation_lane": True,
            "no_repeat_invocation_permission": True,
            "no_execution_permission": True,
            "no_authority_currentness_final_completion_continuation_follow_on_work": True,
        }
    )
    return section


def _consumption_boundary_basis(request: Mapping[str, Any]) -> Any:
    return request.get("selected_consumption_boundary_basis")


def _consumption_boundary_outcome(request: Mapping[str, Any]) -> Any:
    basis = _consumption_boundary_basis(request)
    return (
        request.get("selected_consumption_boundary_result_outcome")
        or _find_first(
            basis,
            (
                "selected_consumption_boundary_result_outcome",
                "selected_result_outcome",
                "outcome",
            ),
        )
    )


def _consumption_boundary_failed_check_count(request: Mapping[str, Any]) -> int | None:
    basis = _consumption_boundary_basis(request)
    for value in (
        request.get("selected_consumption_boundary_failed_check_count"),
        _find_first(
            basis,
            (
                "selected_consumption_boundary_failed_check_count",
                "selected_result_failed_check_count",
                "failed_check_count",
            ),
        ),
    ):
        count = _to_int(value)
        if count is not None:
            return count
    return None


def _selected_consumption_boundary_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _consumption_boundary_basis(request)
    section = _basis_section(basis, "selected_consumption_boundary_basis")
    section.update(
        {
            "selected_consumption_boundary_result_id": _sanitize(
                request.get("selected_consumption_boundary_result_id")
                or _find_first(basis, ("selected_result_id", "result_id", "artifact_id"))
            ),
            "selected_consumption_boundary_result_path": _sanitize(
                request.get("selected_consumption_boundary_result_path")
                or _find_first(basis, ("selected_result_path", "artifact_path", "path"))
            ),
            "selected_consumption_boundary_result_outcome": _sanitize(
                _consumption_boundary_outcome(request)
            ),
            "selected_consumption_boundary_failed_check_count": (
                _consumption_boundary_failed_check_count(request)
            ),
            "selected_consumption_boundary_outcome_recorded": (
                _consumption_boundary_outcome(request) == CONSUMPTION_BOUNDARY_RECORDED_OUTCOME
            ),
            "selected_consumption_boundary_failed_check_count_zero": (
                _consumption_boundary_failed_check_count(request) == 0
            ),
            "boundary_remains_pre_consumption_pre_execution_basis_only": True,
            "boundary_did_not_consume_request": True,
            "boundary_did_not_authorize_execution": True,
            "boundary_did_not_create_output_result_success": True,
            "boundary_did_not_authorize_follow_on_work": True,
        }
    )
    return section


def _selected_consumption_boundary_terminal_summary_section(
    request: Mapping[str, Any]
) -> dict[str, Any]:
    basis = request.get("selected_consumption_boundary_terminal_summary_basis")
    section = _basis_section(
        basis,
        "selected_consumption_boundary_terminal_summary_basis",
    )
    section.update(
        {
            "selected_consumption_boundary_terminal_summary_path": _sanitize(
                request.get("selected_consumption_boundary_terminal_summary_path")
                or _find_first(
                    basis,
                    ("selected_result_path", "terminal_summary_path", "path"),
                )
            ),
            "terminal_summary_remains_readability_basis_only": True,
            "terminal_summary_does_not_consume_request": True,
            "terminal_summary_does_not_authorize_execution": True,
            "terminal_summary_does_not_create_output_result_success": True,
            "terminal_summary_does_not_authorize_follow_on_work": True,
        }
    )
    return section


def _selected_v1_predecessor_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = request.get("selected_v1_predecessor_failure_basis")
    section = _basis_section(basis, "selected_v1_predecessor_failure_basis")
    hidden = _contains_truthy_key(basis, "v1_hidden") or _contains_truthy_key(
        request, "v1_hidden"
    )
    repaired = _contains_truthy_key(basis, "v1_repaired") or _contains_truthy_key(
        request, "v1_repaired"
    )
    claimed_passed = _contains_truthy_key(
        basis, "v1_claimed_passed"
    ) or _contains_truthy_key(request, "v1_claimed_passed")
    section.update(
        {
            "selected_v1_predecessor_artifact_id": _sanitize(
                request.get("selected_v1_predecessor_artifact_id")
                or _find_first(basis, ("selected_result_id", "result_id", "artifact_id"))
            ),
            "selected_v1_predecessor_artifact_path": _sanitize(
                request.get("selected_v1_predecessor_artifact_path")
                or _find_first(basis, ("selected_result_path", "artifact_path", "path"))
            ),
            "selected_v1_predecessor_outcome": _sanitize(
                request.get("selected_v1_predecessor_outcome")
                or _find_first(basis, ("selected_result_outcome", "outcome"))
            ),
            "v1_predecessor_failure_basis_declared": _present(basis),
            "v1_remains_visible_predecessor_failure_evidence": _present(basis)
            and not hidden,
            "v1_is_not_repaired": not repaired,
            "v1_is_not_hidden": not hidden,
            "v1_is_not_claimed_passed": not claimed_passed,
            "v2_successor_does_not_erase_v1": True,
            "predecessor_failure_evidence_is_lineage_evidence_only": True,
        }
    )
    return section


def _posture_section(value: Any, label: str) -> dict[str, Any]:
    declared = _present(value)
    forbidden = _contains_forbidden_full_body_key(value)
    return {
        f"{label}_declared": declared,
        "declared_posture": _selected_basis_value(value) if declared else {},
        "posture_is_reference_shaped": declared and not forbidden,
        "one_shot_consumption_declared": label == "one_shot_consumption_posture"
        or _find_truthy(value, ("one_shot_consumption_declared", "one_shot_consumption_preserved")),
        "consumed_request_basis_recordable": label == "consumed_request_basis"
        or _find_truthy(value, ("consumed_request_basis_recorded", "consumed_request_basis_recordable")),
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "no_standing_invocation_lane_created": True,
        "no_repeat_invocation_permission_created": True,
        "no_execution_permission_created": True,
        "execution_still_requires_separate_review": True,
        "returned_result_containment_preserved": label == "returned_result_containment_posture"
        or _find_truthy(value, ("returned_result_containment_preserved",)),
        "raw_full_prior_artifact_body_not_returned": not forbidden,
    }


def _scope_section(value: Any) -> dict[str, Any]:
    values = _scope_values(value)
    unsupported = [item for item in values if item not in SUPPORTED_REQUEST_CONSUMPTION_SCOPE]
    value_set = set(values)
    return {
        "selected_scope_values": values,
        "unsupported_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "request_consumption_only": "REQUEST_CONSUMPTION_ONLY" in value_set,
        "admitted_request_consumed_as_basis_only": (
            "ADMITTED_REQUEST_CONSUMED_AS_BASIS_ONLY" in value_set
        ),
        "one_shot_consumption_only": "ONE_SHOT_CONSUMPTION_ONLY" in value_set,
        "consumed_request_basis_for_later_execution_review_only": (
            "CONSUMED_REQUEST_BASIS_FOR_LATER_EXECUTION_REVIEW_ONLY" in value_set
        ),
        "command_invocation_not_created": "COMMAND_INVOCATION_NOT_CREATED" in value_set,
        "command_execution_not_performed": "COMMAND_EXECUTION_NOT_PERFORMED" in value_set,
        "command_output_not_created": "COMMAND_OUTPUT_NOT_CREATED" in value_set,
        "command_result_not_created": "COMMAND_RESULT_NOT_CREATED" in value_set,
        "command_success_not_created": "COMMAND_SUCCESS_NOT_CREATED" in value_set,
        "no_standing_invocation_lane_created": (
            "NO_STANDING_INVOCATION_LANE_CREATED" in value_set
        ),
        "no_repeat_invocation_permission_created": (
            "NO_REPEAT_INVOCATION_PERMISSION_CREATED" in value_set
        ),
        "execution_requires_separate_review": "EXECUTION_REQUIRES_SEPARATE_REVIEW" in value_set,
        "consumption_is_not_execution_permission": (
            "CONSUMPTION_IS_NOT_EXECUTION_PERMISSION" in value_set
        ),
        "consumption_is_not_command_success": (
            "CONSUMPTION_IS_NOT_COMMAND_SUCCESS" in value_set
        ),
        "v1_predecessor_failure_remains_visible": (
            "V1_PREDECESSOR_FAILURE_REMAINS_VISIBLE" in value_set
        ),
        "v2_successor_does_not_repair_v1": (
            "V2_SUCCESSOR_DOES_NOT_REPAIR_V1" in value_set
        ),
        "returned_result_containment_preserved": (
            "RETURNED_RESULT_CONTAINMENT_PRESERVED" in value_set
        ),
        "reference_shaped_basis_required": "REFERENCE_SHAPED_BASIS_REQUIRED" in value_set,
        "full_prior_artifact_body_not_emitted": (
            "FULL_PRIOR_ARTIFACT_BODY_NOT_EMITTED" in value_set
        ),
        "no_authority_created": "NO_AUTHORITY_CREATED" in value_set,
        "no_currentness_created": "NO_CURRENTNESS_CREATED" in value_set,
        "no_final_completion": "NO_FINAL_COMPLETION" in value_set,
        "no_continuation_authorized": "NO_CONTINUATION_AUTHORIZED" in value_set,
        "no_reusable_permission": "NO_REUSABLE_PERMISSION" in value_set,
        "no_follow_on_work_authorized": "NO_FOLLOW_ON_WORK_AUTHORIZED" in value_set,
    }


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _build_checks(request: Mapping[str, Any], malformed_code: str | None) -> list[dict[str, Any]]:
    if malformed_code:
        return [
            _check(
                "declared request-consumption request is a mapping",
                False,
                "mapping",
                malformed_code,
                malformed_code,
            )
        ]

    checks: list[dict[str, Any]] = []
    checks.append(
        _check(
            "request consumption question declared",
            _present(request.get("request_consumption_question")),
            "declared question",
            request.get("request_consumption_question"),
            "REQUEST_CONSUMPTION_QUESTION_UNDECLARED",
        )
    )
    intent = request.get("request_consumption_intent")
    checks.append(
        _check(
            "request consumption intent supported",
            intent in SUPPORTED_REQUEST_CONSUMPTION_INTENTS,
            sorted(SUPPORTED_REQUEST_CONSUMPTION_INTENTS),
            intent,
            "REQUEST_CONSUMPTION_INTENT_UNSUPPORTED",
        )
    )

    for name, key, code in REQUIRED_BASIS_FIELDS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))

    checks.extend(
        [
            _check(
                "v2 admitted request outcome is SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED",
                _v2_outcome(request) == SELECTED_ADMISSION_OUTCOME,
                SELECTED_ADMISSION_OUTCOME,
                _v2_outcome(request),
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            _check(
                "v2 admitted request version is 0.2.0",
                _v2_version(request) == SELECTED_ADMISSION_VERSION,
                SELECTED_ADMISSION_VERSION,
                _v2_version(request),
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            _check(
                "v2 admitted request failed check count zero",
                _v2_failed_check_count(request) == 0,
                0,
                _v2_failed_check_count(request),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            _check(
                "v2 successor metadata preserved",
                _v2_successor_metadata_preserved(request),
                {
                    "successor_of": PREDECESSOR_RESOLVER_MODULE,
                    "successor_reason": "declared",
                },
                _v2_successor_metadata(request),
                "V2_SUCCESSOR_METADATA_MISSING",
            ),
            _check(
                "v2 returned-result containment preserved",
                _returned_result_containment_preserved(request),
                "returned-result containment preserved",
                {
                    "returned_result_containment_preserved": _returned_result_containment_preserved(
                        request
                    )
                },
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
            _check(
                "consumption-boundary live artifact recorded outcome",
                _consumption_boundary_outcome(request) == CONSUMPTION_BOUNDARY_RECORDED_OUTCOME,
                CONSUMPTION_BOUNDARY_RECORDED_OUTCOME,
                _consumption_boundary_outcome(request),
                "CONSUMPTION_BOUNDARY_NOT_RECORDED",
            ),
            _check(
                "consumption-boundary live artifact failed check count zero",
                _consumption_boundary_failed_check_count(request) == 0,
                0,
                _consumption_boundary_failed_check_count(request),
                "CONSUMPTION_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
        ]
    )

    v1_basis = request.get("selected_v1_predecessor_failure_basis")
    checks.extend(
        [
            _check(
                "v1 predecessor failure remains visible",
                _present(v1_basis) and not _contains_truthy_key(request, "v1_hidden"),
                "visible predecessor failure evidence",
                {
                    "selected_v1_predecessor_failure_basis_declared": _present(v1_basis),
                    "v1_hidden": _contains_truthy_key(request, "v1_hidden"),
                },
                "V1_FAILURE_HIDDEN",
            ),
            _check(
                "v2 does not repair v1",
                not _contains_truthy_key(request, "v1_repaired")
                and not _contains_truthy_key(request, "v2_treated_as_repairing_v1"),
                False,
                _first_truthy_key(request, ("v1_repaired", "v2_treated_as_repairing_v1")),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            _check(
                "v2 does not claim v1 passed",
                not _contains_truthy_key(request, "v1_claimed_passed")
                and not _contains_truthy_key(request, "v1_passed"),
                False,
                {
                    "v1_claimed_passed": _contains_truthy_key(
                        request, "v1_claimed_passed"
                    ),
                    "v1_passed": _contains_truthy_key(request, "v1_passed"),
                },
                "V1_CLAIMED_PASSED",
            ),
        ]
    )

    for name, key, code in REQUIRED_POSTURE_FIELDS:
        checks.append(_check(name, _present(request.get(key)), "declared", request.get(key), code))

    scope = _scope_section(request.get("request_consumption_scope"))
    checks.append(
        _check(
            "request-consumption scope supported",
            scope["all_selected_scope_values_supported"],
            sorted(SUPPORTED_REQUEST_CONSUMPTION_SCOPE),
            scope["selected_scope_values"],
            "UNSUPPORTED_REQUEST_CONSUMPTION_SCOPE",
        )
    )

    checks.extend(
        [
            _check(
                "execution separation posture declared",
                _present(request.get("execution_separation_posture")),
                "declared execution separation posture",
                request.get("execution_separation_posture"),
                "CONSUMED_REQUEST_BASIS_MISSING",
            ),
            _check(
                "returned-result containment posture declared",
                _present(request.get("returned_result_containment_posture")),
                "declared returned-result containment posture",
                request.get("returned_result_containment_posture"),
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
            _check(
                "no-command-invocation posture declared or preserved by non-claim",
                _present(request.get("no_command_invocation_posture"))
                or not _contains_truthy_key(request, "command_invocation_created"),
                "no command invocation created",
                request.get("no_command_invocation_posture"),
                "COMMAND_INVOCATION_CREATED",
            ),
            _check(
                "no-command-execution posture declared or preserved by non-claim",
                _present(request.get("no_command_execution_posture"))
                or (
                    not _contains_truthy_key(request, "command_execution_performed")
                    and not _contains_truthy_key(request, "command_executed")
                ),
                "no command execution performed",
                request.get("no_command_execution_posture"),
                "COMMAND_EXECUTION_PERFORMED",
            ),
            _check(
                "no-output/result/success posture declared or preserved by non-claim",
                _present(request.get("no_output_result_success_posture"))
                or not any(
                    _contains_truthy_key(request, key)
                    for key in (
                        "command_output_created",
                        "command_result_created",
                        "command_success_created",
                    )
                ),
                "no output/result/success created",
                request.get("no_output_result_success_posture"),
                "COMMAND_OUTPUT_CREATED",
            ),
        ]
    )

    checks.append(
        _check(
            "command invocation not created",
            not _contains_truthy_key(request, "command_invocation_created"),
            False,
            _first_truthy_key(request, ("command_invocation_created",)),
            "COMMAND_INVOCATION_CREATED",
        )
    )
    checks.append(
        _check(
            "command execution not performed",
            not _contains_truthy_key(request, "command_execution_performed")
            and not _contains_truthy_key(request, "command_executed"),
            False,
            _first_truthy_key(request, ("command_execution_performed", "command_executed")),
            "COMMAND_EXECUTION_PERFORMED",
        )
    )
    for check_name, key, code in (
        ("command output not created", "command_output_created", "COMMAND_OUTPUT_CREATED"),
        ("command result not created", "command_result_created", "COMMAND_RESULT_CREATED"),
        ("command success not created", "command_success_created", "COMMAND_SUCCESS_CREATED"),
        (
            "standing invocation lane not created",
            "standing_invocation_lane_created",
            "STANDING_INVOCATION_LANE_CREATED",
        ),
        (
            "repeat invocation permission not created",
            "repeat_invocation_permission_created",
            "REPEAT_INVOCATION_PERMISSION_CREATED",
        ),
        (
            "consumption not execution permission",
            "consumption_treated_as_execution_permission",
            "CONSUMPTION_TREATED_AS_EXECUTION_PERMISSION",
        ),
        (
            "consumption not command success",
            "consumption_treated_as_command_success",
            "CONSUMPTION_TREATED_AS_COMMAND_SUCCESS",
        ),
        (
            "command output not source",
            "command_output_became_source",
            "COMMAND_OUTPUT_TREATED_AS_SOURCE",
        ),
        (
            "command result not authority",
            "command_result_became_authority",
            "COMMAND_RESULT_TREATED_AS_AUTHORITY",
        ),
        (
            "command success not currentness",
            "command_success_created_currentness",
            "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
        ),
        (
            "command success not final completion",
            "command_success_claimed_final_completion",
            "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
        ),
    ):
        checks.append(
            _check(
                check_name,
                not _contains_truthy_key(request, key),
                False,
                _first_truthy_key(request, (key,)),
                code,
            )
        )

    forbidden = _contains_forbidden_full_body_key(request)
    checks.append(
        _check(
            "raw full prior artifact body not emitted",
            not forbidden
            and not _contains_truthy_key(request, "raw_full_prior_artifact_body_returned"),
            "no forbidden full prior artifact body keys or posture",
            {
                "forbidden_full_body_keys_detected": _forbidden_full_body_keys(request),
                "raw_full_prior_artifact_body_returned": _contains_truthy_key(
                    request, "raw_full_prior_artifact_body_returned"
                ),
            },
            "FULL_PRIOR_ARTIFACT_BODY_EMITTED",
        )
    )
    checks.append(
        _check(
            "artifacts not mutated",
            not _contains_truthy_key(request, "prior_artifacts_mutated")
            and not _contains_truthy_key(request, "artifacts_mutated"),
            False,
            _first_truthy_key(request, ("prior_artifacts_mutated", "artifacts_mutated")),
            "ARTIFACTS_MUTATED",
        )
    )
    checks.append(
        _check(
            "deployment/runtime/public release not created",
            not any(
                _contains_truthy_key(request, key)
                for key in ("deployment_created", "runtime_hosting_created", "public_release_created")
            ),
            False,
            _first_truthy_key(
                request,
                ("deployment_created", "runtime_hosting_created", "public_release_created"),
            ),
            "DEPLOYMENT_CREATED",
        )
    )
    checks.append(
        _check(
            "operation permission/public readiness/final completion not created",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "operation_permission_created",
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                )
            ),
            False,
            _first_truthy_key(
                request,
                (
                    "operation_permission_created",
                    "public_launch_readiness_created",
                    "public_readiness_created",
                    "final_completion_claimed",
                ),
            ),
            "OPERATION_PERMISSION_CREATED",
        )
    )
    checks.append(
        _check(
            "continuation/reusable permission/follow-on work not authorized",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "continuation_authorized",
                    "reusable_permission_created",
                    "follow_on_work_authorized",
                )
            ),
            False,
            _first_truthy_key(
                request,
                (
                    "continuation_authorized",
                    "reusable_permission_created",
                    "follow_on_work_authorized",
                ),
            ),
            "CONTINUATION_AUTHORIZED",
        )
    )
    checks.append(
        _check(
            "derivative reception/vessel relation/another reception request not authorized",
            not any(
                _contains_truthy_key(request, key)
                for key in (
                    "derivative_reception_authorized",
                    "vessel_relation_authorized",
                    "another_reception_request_authorized",
                )
            ),
            False,
            _first_truthy_key(
                request,
                (
                    "derivative_reception_authorized",
                    "vessel_relation_authorized",
                    "another_reception_request_authorized",
                ),
            ),
            "DERIVATIVE_RECEPTION_AUTHORIZED",
        )
    )
    checks.append(
        _check(
            "no mutation/replay/merge",
            not any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS),
            False,
            _first_truthy_key(request, MUTATION_FLAGS),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
    )
    checks.append(
        _check(
            "non-claims remain false",
            _declared_non_claims_false(request),
            _false_non_claims(),
            _declared_non_claims_actual(request),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            return str(check.get("block_code") or check.get("failure_code"))
    return None


def _first_collapse_code(request: Mapping[str, Any]) -> str | None:
    for key, code in COLLAPSE_FIELD_CODES:
        if _contains_truthy_key(request, key):
            return code
    if any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _determine_block_code(
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    malformed_code: str | None,
) -> str | None:
    if malformed_code:
        return malformed_code
    if request.get("request_consumption_intent") == INTENT_BLOCK:
        return "REQUEST_CONSUMPTION_REVIEW_EXPLICITLY_BLOCKED"
    if request.get("requested_request_consumption_outcome") == OUTCOME_BLOCKED:
        return "REQUEST_CONSUMPTION_REVIEW_EXPLICITLY_BLOCKED"
    requested = request.get("requested_request_consumption_outcome")
    if _present(requested) and requested not in OUTCOME_FAMILY:
        return "DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED"
    if _contains_forbidden_full_body_key(request) or _contains_truthy_key(
        request, "raw_full_prior_artifact_body_returned"
    ):
        return "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
    collapse_code = _first_collapse_code(request)
    if collapse_code is not None:
        return collapse_code
    return _first_failed_code(checks)


def _determine_outcome(request: Mapping[str, Any], block_code: str | None) -> str:
    if block_code is not None:
        return OUTCOME_BLOCKED
    requested = request.get("requested_request_consumption_outcome")
    if requested in {
        OUTCOME_CONSUMED,
        OUTCOME_NOT_CONSUMED,
        OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    }:
        return str(requested)
    if request.get("request_consumption_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_CONSUMED
    return OUTCOME_CONSUMED


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": _sanitize(reason) if reason is not None else BLOCK_REASONS.get(code or "", code),
        "raw_full_prior_artifact_body_returned": False,
        "block_evidence_is_contained": True,
    }


def _statement(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    consumed = outcome == OUTCOME_CONSUMED
    statement = {key: consumed for key in ALLOWED_CONSUMED_TRUE_FIELDS}
    statement.update(
        {
            "request_consumption_only": True,
            "admitted_request_consumed_as_basis_only": consumed,
            "consumed_request_basis_for_later_execution_review_only": True,
            "command_invocation_created": False,
            "command_executed": False,
            "command_execution_performed": False,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "standing_invocation_lane_created": False,
            "repeat_invocation_permission_created": False,
            "consumption_treated_as_execution_permission": False,
            "consumption_treated_as_command_success": False,
            "command_output_became_source": False,
            "command_result_became_authority": False,
            "command_success_created_currentness": False,
            "command_success_claimed_final_completion": False,
            "command_became_authority": False,
            "full_prior_artifacts_embedded": False,
            "raw_full_prior_artifact_body_returned": False,
            "prior_artifacts_mutated": False,
            "v1_repaired": False,
            "v1_hidden": False,
            "v1_claimed_passed": False,
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
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "no_standing_invocation_lane_created": True,
            "no_repeat_invocation_permission_created": True,
            "no_execution_permission_created": True,
            "consumption_not_execution_permission": True,
            "consumption_not_command_success": True,
            "command_output_not_source": True,
            "command_result_not_authority": True,
            "command_success_not_currentness": True,
            "command_success_not_final_completion": True,
            "reference_shaped_basis_required": True,
            "full_prior_artifact_body_not_emitted": not _contains_forbidden_full_body_key(request),
            "artifacts_not_mutated": True,
            "deployment_runtime_public_release_not_created": True,
            "operation_permission_public_readiness_final_completion_not_created": True,
            "continuation_reusable_permission_follow_on_work_not_authorized": True,
            "derivative_reception_vessel_relation_another_reception_request_not_authorized": True,
        }
    )
    statement.update(_false_non_claims())
    return statement


def _non_meaning() -> dict[str, bool]:
    labels = (
        "command_invocation_created",
        "command_executed",
        "command_output_exists",
        "command_result_exists",
        "command_success_exists",
        "command_success_creates_currentness",
        "command_success_claims_final_completion",
        "command_output_becomes_source",
        "command_result_becomes_authority",
        "standing_invocation_lane_exists",
        "repeat_invocation_permission_exists",
        "execution_permission_exists",
        "v1_was_repaired",
        "v1_was_hidden",
        "v1_passed",
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
    return {f"request_consumption_does_not_mean_{label}": True for label in labels}


def _additional_basis(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    requires = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": requires,
        "additional_basis_context": _sanitize(request.get("additional_basis_context") if requires else {}),
        "additional_basis_not_scheduled": True,
        "additional_basis_not_authorized": True,
        "additional_basis_not_executed": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "standing_lane_not_created": True,
        "repeat_permission_not_created": True,
        "execution_permission_not_created": True,
        "artifacts_not_mutated": True,
    }


def _not_consumed(
    outcome: str,
    request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_consumed = outcome == OUTCOME_NOT_CONSUMED
    return {
        "not_consumed": not_consumed,
        "not_consumed_basis": _sanitize(request.get("not_consumed_basis") if not_consumed else {}),
        "failed_checks": _sanitize(
            [check for check in checks if check.get("passed") is not True]
            if not_consumed
            else []
        ),
        "not_consumed_does_not_mutate": True,
        "not_consumed_does_not_repair": True,
        "not_consumed_does_not_invoke_command": True,
        "not_consumed_does_not_execute_command": True,
        "not_consumed_does_not_emit_output": True,
        "not_consumed_does_not_create_result": True,
        "not_consumed_does_not_create_success": True,
        "not_consumed_does_not_create_standing_lane": True,
        "not_consumed_does_not_create_repeat_permission": True,
        "not_consumed_does_not_create_execution_permission": True,
        "not_consumed_does_not_deploy_publish_host": True,
        "not_consumed_does_not_currentize_complete_continue": True,
        "not_consumed_does_not_authorize_follow_on_work": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "request consumption test",
            "request consumption live artifact",
            "command execution review",
            "command invocation",
            "command execution",
            "command output",
            "command result",
            "command success",
            "command output/report artifact from live execution",
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


def _checks_summary(checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    records = [_sanitize(check) for check in checks]
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = len(checks) - passed
    return {
        "records": records,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "failed_check_codes": [
            check.get("block_code") or check.get("failure_code")
            for check in checks
            if check.get("passed") is not True
        ],
    }


def _metadata(request: Mapping[str, Any]) -> dict[str, Any]:
    request_id = _safe_component(request.get("request_consumption_request_id"), "unidentified")
    return {
        "admitted_single_live_command_invocation_request_consumption_result_id": (
            f"{request_id}__admitted_single_live_command_invocation_request_consumption_result"
        ),
        "admitted_single_live_command_invocation_request_consumption_result_type": (
            "portable_source_body_verification_admitted_single_live_command_invocation_"
            "request_consumption_result"
        ),
        "admitted_single_live_command_invocation_request_consumption_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }


def _declared_question(request: Mapping[str, Any], request_path: Path | str | None) -> dict[str, Any]:
    return {
        "request_consumption_request_id": _sanitize(request.get("request_consumption_request_id")),
        "request_consumption_question": _sanitize(request.get("request_consumption_question")),
        "request_consumption_intent": _sanitize(request.get("request_consumption_intent")),
        "requested_request_consumption_outcome": _sanitize(
            request.get("requested_request_consumption_outcome")
        ),
        "declared_request_consumption_request_path": str(request_path) if request_path is not None else None,
        "question_answered": (
            "Can the already-admitted single live command invocation request be "
            "consumed exactly once as closed basis for a later command execution "
            "review, without invoking or executing the command and without creating "
            "command output, command result, command success, standing invocation "
            "lane, repeat permission, execution permission, authority, currentness, "
            "final completion, continuation, reusable permission, derivative "
            "reception, vessel relation, another reception request, or follow-on work?"
        ),
        "request_consumption_is_not_command_invocation": True,
        "request_consumption_is_not_command_execution": True,
        "request_consumption_is_not_output_result_success": True,
        "request_consumption_is_not_execution_permission": True,
        "request_consumption_does_not_authorize_next_work": True,
    }


def _read_json_object(path_value: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = Path(path_value)
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, "DECLARED_REQUEST_CONSUMPTION_REQUEST_UNREADABLE", str(exc)
    except json.JSONDecodeError as exc:
        return None, "DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED", str(exc)
    if not isinstance(loaded, dict):
        return None, "DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED", "JSON document must be an object."
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
        malformed_code = "DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED"

    checks = _build_checks(request, malformed_code)
    block_code = _determine_block_code(request, checks, malformed_code)
    outcome = _determine_outcome(request, block_code)
    statement = _statement(outcome, request)

    result: dict[str, Any] = {
        "admitted_single_live_command_invocation_request_consumption_metadata": _metadata(request),
        "declared_request_consumption_question": _declared_question(request, request_path),
        "selected_v2_admitted_request_basis": _selected_v2_basis_section(request),
        "selected_consumption_boundary_basis": _selected_consumption_boundary_section(request),
        "selected_consumption_boundary_terminal_summary_basis": _selected_consumption_boundary_terminal_summary_section(
            request
        ),
        "selected_v1_predecessor_failure_basis": _selected_v1_predecessor_section(request),
        "one_shot_consumption_posture": _posture_section(
            request.get("one_shot_consumption_posture"), "one_shot_consumption_posture"
        ),
        "consumed_request_basis": _posture_section(
            request.get("consumed_request_basis"), "consumed_request_basis"
        ),
        "no_standing_lane_posture": _posture_section(
            request.get("no_standing_lane_posture"), "no_standing_lane_posture"
        ),
        "no_repeat_permission_posture": _posture_section(
            request.get("no_repeat_permission_posture"), "no_repeat_permission_posture"
        ),
        "execution_separation_posture": _posture_section(
            request.get("execution_separation_posture"), "execution_separation_posture"
        ),
        "returned_result_containment_posture": _posture_section(
            request.get("returned_result_containment_posture"),
            "returned_result_containment_posture",
        ),
        "request_consumption_scope": _scope_section(request.get("request_consumption_scope")),
        "request_consumption_checks": _checks_summary(checks),
        "request_consumption_statement": statement,
        "request_consumption_non_meaning": _non_meaning(),
        "additional_basis_required": _additional_basis(outcome, request),
        "not_consumed_basis": _not_consumed(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _false_non_claims(),
        "outcome": outcome,
        "block": _block(block_code, path_reason or request.get("block_reason")),
    }
    result["admitted_single_live_command_invocation_request_consumption_summary"] = (
        build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_summary(
            result
        )
    )
    return _sanitize(result)


def resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption(
    declared_request_consumption_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared request-consumption request mapping."""

    if declared_request_consumption_request is None:
        return _build_result({})
    if not isinstance(declared_request_consumption_request, Mapping):
        return _build_result(
            {},
            malformed_code="DECLARED_REQUEST_CONSUMPTION_REQUEST_MALFORMED",
        )
    return _build_result(declared_request_consumption_request)


def resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_from_path(
    declared_request_consumption_request_path: Path | str,
) -> dict:
    """Resolve one declared request-consumption JSON object from a path."""

    request, error_code, error_reason = _read_json_object(
        declared_request_consumption_request_path
    )
    if error_code:
        return _build_result(
            {},
            request_path=declared_request_consumption_request_path,
            malformed_code=error_code,
            path_reason=error_reason,
        )
    return _build_result(request, request_path=declared_request_consumption_request_path)


def build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_summary(
    result: Mapping[str, Any]
) -> dict:
    """Build a compact non-authoritative request-consumption summary."""

    safe_result = _sanitize(result)
    statement = _as_mapping(safe_result.get("request_consumption_statement"))
    checks = _as_mapping(safe_result.get("request_consumption_checks"))
    block = _as_mapping(safe_result.get("block"))
    question = _as_mapping(safe_result.get("declared_request_consumption_question"))
    non_claims = _as_mapping(safe_result.get("non_claims"))
    selected_v2 = _as_mapping(safe_result.get("selected_v2_admitted_request_basis"))
    boundary = _as_mapping(safe_result.get("selected_consumption_boundary_basis"))
    return {
        "outcome": safe_result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "request_consumption_request_id": question.get("request_consumption_request_id"),
        "request_consumption_question": question.get("request_consumption_question"),
        "request_consumption_intent": question.get("request_consumption_intent"),
        "passed_check_count": checks.get("passed_check_count", 0),
        "failed_check_count": checks.get("failed_check_count", 0),
        "admitted_request_consumed": statement.get(
            "admitted_single_live_command_invocation_request_consumed", False
        ),
        "request_consumed": statement.get("request_consumed", False),
        "consumption_token_closed": statement.get("consumption_token_closed", False),
        "consumed_request_basis_recorded": statement.get(
            "consumed_request_basis_recorded", False
        ),
        "one_shot_consumption_preserved": statement.get(
            "one_shot_consumption_preserved", False
        ),
        "execution_requires_separate_review": statement.get(
            "execution_requires_separate_review", False
        ),
        "v1_predecessor_failure_preserved": statement.get(
            "v1_predecessor_failure_preserved", False
        ),
        "returned_result_containment_preserved": statement.get(
            "returned_result_containment_preserved", False
        ),
        "not_consumed": safe_result.get("outcome") == OUTCOME_NOT_CONSUMED,
        "requires_additional_basis": safe_result.get("outcome")
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_v2_admitted_request_outcome": selected_v2.get(
            "selected_v2_admitted_request_outcome"
        ),
        "selected_v2_admitted_request_version": selected_v2.get(
            "selected_v2_admitted_request_version"
        ),
        "selected_v2_failed_check_count": selected_v2.get(
            "selected_v2_failed_check_count"
        ),
        "selected_consumption_boundary_outcome": boundary.get(
            "selected_consumption_boundary_result_outcome"
        ),
        "selected_consumption_boundary_failed_check_count": boundary.get(
            "selected_consumption_boundary_failed_check_count"
        ),
        "command_invocation_not_created": statement.get(
            "command_invocation_not_created", True
        ),
        "command_execution_not_performed": statement.get(
            "command_execution_not_performed", True
        ),
        "command_output_not_created": statement.get("command_output_not_created", True),
        "command_result_not_created": statement.get("command_result_not_created", True),
        "command_success_not_created": statement.get("command_success_not_created", True),
        "no_standing_lane": statement.get("no_standing_invocation_lane_created", True),
        "no_repeat_permission": statement.get(
            "no_repeat_invocation_permission_created", True
        ),
        "no_execution_permission": statement.get("no_execution_permission_created", True),
        "consumption_not_command_success": statement.get(
            "consumption_not_command_success", True
        ),
        "v1_not_repaired": not non_claims.get("v1_repaired", True),
        "v1_not_hidden": not non_claims.get("v1_hidden", True),
        "v1_not_claimed_passed": not non_claims.get("v1_claimed_passed", True),
        "no_raw_full_prior_artifact_body_returned": not non_claims.get(
            "raw_full_prior_artifact_body_returned", True
        ),
        "no_artifact_mutation": not non_claims.get("prior_artifacts_mutated", True),
        "no_deployment_runtime_public_release": (
            not non_claims.get("deployment_created", True)
            and not non_claims.get("runtime_hosting_created", True)
            and not non_claims.get("public_release_created", True)
        ),
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
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise PortableSourceBodyVerificationAdmittedSingleLiveCommandInvocationRequestConsumptionError(
        f"Could not allocate non-overwriting output path for {path}"
    )


def write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded request-consumption result JSON file."""

    safe_result = _sanitize(result)
    question = _as_mapping(safe_result.get("declared_request_consumption_question"))
    request_id = _safe_component(question.get("request_consumption_request_id"), "unidentified")
    filename = (
        f"{request_id}__admitted_single_live_command_invocation_request_"
        "consumption_result.json"
    )
    if output_path is None:
        target = (
            PORTABLE_SOURCE_BODY_VERIFICATION_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_ROOT
            / filename
        )
    else:
        target = Path(output_path)
        if target.suffix == "":
            target = target / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target = _unique_path(target)
    target.write_text(
        json.dumps(safe_result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_request(
    request_consumption_request_id: str,
    request_consumption_question: str,
    selected_v2_admitted_request_basis: Mapping[str, Any] | str,
    selected_consumption_boundary_basis: Mapping[str, Any] | str,
    selected_consumption_boundary_terminal_summary_basis: Mapping[str, Any] | str,
    selected_v1_predecessor_failure_basis: Mapping[str, Any] | str,
    one_shot_consumption_posture: Mapping[str, Any] | str,
    consumed_request_basis: Mapping[str, Any] | str,
    no_standing_lane_posture: Mapping[str, Any] | str,
    no_repeat_permission_posture: Mapping[str, Any] | str,
    execution_separation_posture: Mapping[str, Any] | str,
    returned_result_containment_posture: Mapping[str, Any] | str,
    request_consumption_scope: Sequence[str] | Mapping[str, Any],
    request_consumption_intent: str = INTENT_RECORD,
    *,
    selected_v2_admitted_request_artifact_path: str | None = None,
    selected_v2_admitted_request_artifact_id: str | None = None,
    selected_v2_admitted_request_outcome: str | None = None,
    selected_v2_admitted_request_version: str | None = None,
    selected_v2_failed_check_count: int | None = None,
    selected_consumption_boundary_result_path: str | None = None,
    selected_consumption_boundary_result_id: str | None = None,
    selected_consumption_boundary_result_outcome: str | None = None,
    selected_consumption_boundary_failed_check_count: int | None = None,
    requested_request_consumption_outcome: str = OUTCOME_CONSUMED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_consumed_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared request-consumption request with false non-claims."""

    request: dict[str, Any] = {
        "request_consumption_request_id": request_consumption_request_id,
        "request_consumption_question": request_consumption_question,
        "request_consumption_intent": request_consumption_intent,
        "selected_v2_admitted_request_basis": _copy(selected_v2_admitted_request_basis),
        "selected_consumption_boundary_basis": _copy(selected_consumption_boundary_basis),
        "selected_consumption_boundary_terminal_summary_basis": _copy(
            selected_consumption_boundary_terminal_summary_basis
        ),
        "selected_v1_predecessor_failure_basis": _copy(
            selected_v1_predecessor_failure_basis
        ),
        "one_shot_consumption_posture": _copy(one_shot_consumption_posture),
        "consumed_request_basis": _copy(consumed_request_basis),
        "no_standing_lane_posture": _copy(no_standing_lane_posture),
        "no_repeat_permission_posture": _copy(no_repeat_permission_posture),
        "execution_separation_posture": _copy(execution_separation_posture),
        "returned_result_containment_posture": _copy(returned_result_containment_posture),
        "request_consumption_scope": _copy(request_consumption_scope),
        "requested_request_consumption_outcome": requested_request_consumption_outcome,
        "declared_non_claims": _false_non_claims(),
    }
    optional_values = {
        "selected_v2_admitted_request_artifact_path": selected_v2_admitted_request_artifact_path,
        "selected_v2_admitted_request_artifact_id": selected_v2_admitted_request_artifact_id,
        "selected_v2_admitted_request_outcome": selected_v2_admitted_request_outcome,
        "selected_v2_admitted_request_version": selected_v2_admitted_request_version,
        "selected_v2_failed_check_count": selected_v2_failed_check_count,
        "selected_consumption_boundary_result_path": selected_consumption_boundary_result_path,
        "selected_consumption_boundary_result_id": selected_consumption_boundary_result_id,
        "selected_consumption_boundary_result_outcome": selected_consumption_boundary_result_outcome,
        "selected_consumption_boundary_failed_check_count": selected_consumption_boundary_failed_check_count,
        "additional_basis_context": additional_basis_context,
        "not_consumed_basis": not_consumed_basis,
    }
    for key, value in optional_values.items():
        if value is not None:
            request[key] = _copy(value)
    return request
